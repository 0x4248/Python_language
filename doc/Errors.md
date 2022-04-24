This language will catch errors when needed

# About the module
The module that handles the system errors is located at: `./system/Raise.py`
```python
import colorama
from colorama import Fore, Back, Style
from system import shell
def error(name="Unidentified", message="Unidentified"):
    print(Fore.RED+"Error: "+name+Style.RESET_ALL)
    print(message)
    if shell.in_shell == False:
        print(Fore.YELLOW+"Closing on exit code 1"+Style.RESET_ALL)
        exit(1)
```
To raise an error in interpreter:
```python
from system import Raise
Raise.error("Name", "Message")
```

# System errors in the language
A system error will only be called if the interpreter cant run continue because of an error in the script.

This is what an error looks like:
```
Error: Syntax Error
Unknown command or function
Error on line: This is an incorrect line of code
```

There are many reasons why an error can be called. Here are the most common ones:
- The interpreter cant find the command or function
- The interpreter cant find the variable
- The interpreter cant make a variable
- The interpreter cant find the file
