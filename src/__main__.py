import os
import sys
import pylog

from system import Raise
from system import interpreter
from system import shell

if __name__ == "__main__":
    for i in sys.argv:
        if i == "--shell":
            shell.in_shell = True
            shell.run()
    if len(sys.argv) > 1:
        if os.path.isfile(sys.argv[1]):
            interpreter.interpreter(open(sys.argv[1]).read())
        else:
            Raise.error(name="File Not Found", message="File does not exist: "+sys.argv[1])
    else:
        choice = input("Would you like to enter the shell? (y/n)")
        if choice == "y" or choice == "Y":
            shell.in_shell = True
            shell.run()
        else:
            exit(0)
