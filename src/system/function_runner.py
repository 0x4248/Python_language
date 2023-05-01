"""
This is the main runner for the command except from main and system call it using function_runner.run(command) and will return the output of the command or function
"""


def get_var(command):
    from system import interpreter

    command = command.replace("var.get(", "")
    if command in interpreter.variables["names"]:
        return interpreter.variables["values"][
            interpreter.variables["names"].index(command)
        ]
    # TODO: add raise


def run(command):
    if command.startswith("random"):
        if (
            command.split(".")[1].startswith("int")
            and command.split(".")[1].startswith("intrange") == False
        ):
            from system.modules import random_module

            return random_module.rand_int()

        elif command.split(".")[1].startswith("char"):
            from system.modules import random_module

            return random_module.rand_char()

        elif command.split(".")[1].startswith("intrange"):
            from system.modules import random_module

            x = command.split(".")[1].replace("intrange(", "").replace(")", "")
            return random_module.rand_intrange(x.split(",")[0], x.split(",")[1])

    elif command.startswith("string"):
        if command.split(".")[1].startswith("replace"):
            from system.modules import module_string

            x = command.split(".r")[1].replace("eplace(", "").replace(")", "")
            args = x.split(",")
            for i in args:
                if i.startswith("var.get("):
                    args[args.index(i)] = str(get_var(str(i)))
                else:
                    args[args.index(i)] = i
            return module_string.replace_str(str(args[0]), args[1], args[2])
        elif command.split(".")[1].startswith("trim"):
            from system.modules import module_string

            x = command.split(".t")[1].replace("rim(", "").replace(")", "")
            args = x.split(",")
            for i in args:
                if i.startswith("var.get("):
                    args[args.index(i)] = str(get_var(str(i)))
                else:
                    args[args.index(i)] = i
            print(args)
            return module_string.trim(args[0], args[1])
        elif command.split(".")[1].startswith("merge"):
            from system.modules import module_string

            x = command.split(".m")[1].replace("erge(", "").replace(")", "")
            args = x.split(",")
            for i in args:
                if i.startswith("var.get("):
                    args[args.index(i)] = str(get_var(str(i)))
                else:
                    args[args.index(i)] = i
            return module_string.merge(args)
