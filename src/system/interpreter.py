from system import Raise
import json

from system import function_runner


class states:
    current_funcution = "none"
    imported_modules = []
    in_import = False
    in_if = False
    if_continue = False


variables = {}
variables["names"] = []
variables["values"] = []


def interpreter(code, preimport=[]):
    """
    Interprets the code
    """

    states.imported_modules = preimport

    code_split = code.split("\n")
    for line in code_split:
        line = line.replace("\t", "")
        line = line.lstrip()
        if line == "":
            continue

        if states.in_import == False:
            if states.in_if and states.if_continue == False:
                if line.startswith("} endif"):
                    states.in_if = False
                    states.if_continue = False
                continue
            elif line.startswith("//"):
                continue
            elif line.startswith("#"):
                continue
            elif line.startswith("module.imports ="):
                if line.endswith("["):
                    states.in_import = True
                    continue
                else:
                    Raise.error(
                        name="Syntax Error",
                        message="Expected '[' after 'module.imports ='\nError on line: "
                        + line,
                    )
            elif line.startswith("if"):
                if line.startswith("if(") and line.endswith("){"):
                    states.in_if = True
                    statement = line.replace("if(", "").replace("){", "")
                    statement = statement.split(",")
                    if statement[1].startswith('"' or "'"):
                        if variables["values"][
                            variables["names"].index(statement[0])
                        ] == statement[1].replace('"', "").replace("'", ""):
                            states.if_continue = True
                        else:
                            states.if_continue = False
                    else:
                        try:
                            if (
                                variables["values"][
                                    variables["names"].index(statement[0])
                                ]
                                == variables["values"][
                                    variables["names"].index(statement[1])
                                ]
                            ):
                                states.if_continue = True
                            else:
                                states.if_continue = False
                        except ValueError:
                            Raise.error(
                                name="Variable Error",
                                message="Variable dose not exist\nWhy not try:\n\tvar.set variable = 'Hello World'\nError on line: "
                                + line,
                            )

            elif line.startswith("var"):
                if line.startswith("var.set"):
                    if line.split(" ")[1] in variables["names"]:
                        Raise.error(
                            name="Variable Error",
                            message="Variable already exists\nWhy not try:\n\tvar.del(variable)\n\tvar.set variable = 'Hello World'\nError on line: "
                            + line,
                        )
                    if line.split(" ")[2] == "~":
                        if (
                            line.replace(
                                "var.set " + line.split(" ")[1] + " ~ ", ""
                            ).split(".")[0]
                            in states.imported_modules
                        ):
                            variables["names"].append(line.split(" ")[1])
                            variables["values"].append(
                                str(
                                    function_runner.run(
                                        line.replace(
                                            "var.set " + line.split(" ")[1] + " ~ ", ""
                                        )
                                    )
                                )
                            )

                    variables["names"].append(line.split(" ")[1])
                    variables["values"].append(
                        line.replace("var.set " + line.split(" ")[1] + " = ", "")
                    )
                elif line.startswith("var.get"):
                    Raise.error(
                        name="Syntax Error",
                        message="Cannot use 'var.get' outside a function\nWhy not try:\n\tsystem.out(var.get(variable))\nError on line: "
                        + line,
                    )
                elif line.startswith("var.del"):
                    if line.startswith("var.del(") and line.endswith(")"):
                        if (
                            line.replace("var.del(", "").replace(")", "")
                            in variables["names"]
                        ):
                            del variables["values"][
                                variables["names"].index(
                                    line.replace("var.del(", "").replace(")", "")
                                )
                            ]
                            variables["names"].remove(
                                line.replace("var.del(", "").replace(")", "")
                            )
                        else:
                            Raise.error(
                                name="Variable Error",
                                message="Cannot delete a variable that doesn't exist\nError on line: "
                                + line,
                            )
                    else:
                        Raise.error(
                            name="Syntax Error",
                            message="Expected ( 'var.del(variable)'\nError on line: "
                            + line,
                        )
            elif line.startswith("system"):
                if "system" in states.imported_modules:
                    if line.startswith("system.out"):
                        if line.startswith("system.out(") and line.endswith(")"):
                            o = line.replace("system.out(", "")[:-1]
                            if (
                                o.startswith("'")
                                and o.endswith("'")
                                or o.startswith('"')
                                and o.endswith('"')
                            ):
                                print(o.replace("'", "").replace('"', ""))
                            elif o.startswith("var.get(") and o.endswith(")"):
                                if (
                                    o.replace("var.get(", "").replace(")", "")
                                    in variables["names"]
                                ):
                                    print(
                                        variables["values"][
                                            variables["names"].index(
                                                o.replace("var.get(", "").replace(
                                                    ")", ""
                                                )
                                            )
                                        ]
                                    )
                                else:
                                    Raise.error(
                                        name="Variable Error",
                                        message="Cannot get a variable that doesn't exist\nError on line: "
                                        + line,
                                    )
                            elif o.split(".")[0] in states.imported_modules:
                                print(function_runner.run(o))

                            else:
                                Raise.error(
                                    name="Syntax Error",
                                    message="No function or input was added\nError on line: "
                                    + line,
                                )
                        else:
                            Raise.error(
                                name="Syntax Error",
                                message="Expected ( 'system.out(variable)'\nError on line: "
                                + line,
                            )
                    elif line.startswith("system.in"):
                        o = line.replace("system.in(", "")[:-1]
                        o = o.split(",")
                        i = input(o[0].replace("'", "").replace('"', ""))
                        if len(o) == 1:
                            continue
                        elif len(o) == 2:
                            if o[1] in variables["names"]:
                                Raise.error(
                                    name="Variable Error",
                                    message="Variable already exists\nWhy not try:\n\tvar.del(variable)\n\tsystem.in('input>',variable)\nError on line: "
                                    + line,
                                )
                            variables["names"].append(o[1])
                            variables["values"].append(i)
                else:
                    Raise.error(
                        name="Module Error",
                        message="Cannot use 'system' outside a module\nError on line: "
                        + line,
                    )
            elif line.split(".")[0] in states.imported_modules:
                function_runner.run(line)
            else:
                if line.endswith("} endif"):
                    states.in_if = False
                    states.if_continue = False
                    continue
                Raise.error(
                    name="Syntax Error",
                    message="Unknown command or function\nError on line: " + line,
                )

        # States
        elif states.in_import == True:
            with open("./system/builtins.json") as json_file:
                if line == "module.imports = [":
                    continue
                if line.endswith("]"):
                    states.in_import = False
                    continue
                data = json.load(json_file)
                if line in data["modules"]:
                    states.imported_modules.append(line)
                else:
                    Raise.error(
                        name="Module Not Found",
                        message="Module not found: "
                        + line
                        + "\nError on line: "
                        + line,
                    )

        elif states.in_if:
            if line.startswith("}"):
                states.in_if = False
                states.if_continue = False
                continue
