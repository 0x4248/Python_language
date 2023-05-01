from system import interpreter

in_shell = False


def run():
    print("Welcome to the shell all builtin modules have been imported")
    while True:
        interpreter.interpreter(input(">>"), preimport=["system", "random", "string"])
