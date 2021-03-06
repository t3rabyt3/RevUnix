#!/usr/bin/python
from modules import server
from modules import helper as h
import sys, os
server = server.Server()


class RevUnix:
    def __init__(self):
        h.generate_keys()
        self.payloads = self.import_payloads()
        self.banner_text = h.GREEN+"""
 ____            _   _       _
|  _ \ _____   _| | | |_ __ (_)_  __
| |_) / _ \ \ / / | | | '_ \| \ \/ /
|  _ <  __/\ V /| |_| | | | | |>  <
|_| \_\___| \_/  \___/|_| |_|_/_/\_\`"""+h.COLOR_INFO+"""
"""+h.WHITE+"\nVersion: 1.0\nCreated By Akash Sharma (@T3raByt3)\n"+"-"*40+"\nTwitter  --> @t3rabyt3_akash \nLinkedIn --> @iamakashsharma \nGitHub   --> @T3raByt3\n"+h.ENDC
        self.main_menu_text = h.WHITE+"-"*40+"\n"+"""\nMenu:\n
    1): Initialize Server
    2): Launch MultiHandler
    3): Generate Payload
    4): Get Out Of Here
""" + "\n"+h.NES



    def print_payload(self,payload,number_option):
        print " " * 4 + str(number_option) + "): " + payload.name


    def start_single_server(self):
        if not server.set_host_port():
            return
        server.start_single_handler()


    def start_multi_handler(self):
        if not server.set_host_port():
            return
        server.start_multi_handler()


    def prompt_run_server(self):
        if raw_input(h.NES+"Start Server? (Press Enter): ") == "n":
            return
        else:
            if raw_input(h.NES+"MultiHandler? (Press Enter): ") == "y":
                server.start_multi_handler()
            else:
                server.start_single_handler()


    def import_payloads(self):
        path = "modules/payloads"
        sys.path.append(path)
        modules = dict()
        for mod in os.listdir(path):
            if mod == '__init__.py' or mod[-3:] != '.py':
                continue
            else:
                m = __import__(mod[:-3]).payload()
                modules[m.name] = m
        return modules


    def exit_menu(self):
        exit()


    def choose_payload(self):
        print h.WHITE+"-"*40+h.ENDC
        print "Payload:\n"
        number_option = 1
        for key in self.payloads:
            payload = self.payloads[key]
            self.print_payload(payload,number_option)
            number_option += 1
        print ""
        while 1:
            try:
                # choose payload
                option = raw_input(h.info_general_raw(" '1' To Proceed --> "))
                if not option:
                  continue
                selected_payload = self.payloads[self.payloads.keys()[int(option) - 1]]

                server.set_host_port()

                selected_payload.run(server)

                self.prompt_run_server()
                break
            except KeyboardInterrupt:
                print "Damn!!"
                break
            except Exception as e:
                print e
                break


    def menu(self,err=""):
        while 1:
            try:
                h.clear()
                if err:
                    print err
                sys.stdout.write(self.banner_text)
                option = raw_input(self.main_menu_text)
                choose = {
                    "1" : self.start_single_server,
                    "2" : self.start_multi_handler,
                    "3" : self.choose_payload,
                    "4" : self.exit_menu
                }
                try:
                    choose[option]()
                    self.menu()
                except KeyError:
                    if option:
                        self.menu("Oops: " + option + " is not an option")
                    else:
                        self.menu()
                except KeyboardInterrupt:
                    continue

            except KeyboardInterrupt:
                print "\nSayonara!\n"
                exit()


if __name__ == "__main__":
    revunix = RevUnix()
    revunix.menu()
