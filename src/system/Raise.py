import colorama
from colorama import Fore, Back, Style
from system import shell


def error(name="Unidentified", message="Unidentified"):
    print(Fore.RED + "Error: " + name + Style.RESET_ALL)
    print(message)
    if shell.in_shell == False:
        print(Fore.YELLOW + "Closing on exit code 1" + Style.RESET_ALL)
        exit(1)
