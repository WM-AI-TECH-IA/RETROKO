import sys
import os


class CommanderRETRO: 
    def list_commands(self):
        return ["load", "upscale", "views", "export", "reset"]

    def run_command(self, cmd):
        if cmd == "load":
            os.system("python plot_retroko.py")
        elif cmd == "upscale":
            print("Upgrading matrix vis dimensions")
        elif cmd == "views":
            sys.stdout.write("Exploration activee retroko...")
        else:
            print("Conmande non reconue")