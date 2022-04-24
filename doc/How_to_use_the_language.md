This language is a language that is interpreted. This wiki will walk you through how to use the language

# Examples
Here are some examples of the language
## Hello World
Script:
```python
module.imports =  [
    system
]
system.out("Hello World")
```
Output:
```
Hello World
```
## Hello World with variables
Script:
```python
module.imports =  [
    system
    string
]
var.set a = Hello 
var.set b = World
system.out(string.merge(var.get(a),var.get(b))
```
Output:
```
Hello World
```
## If Statements
Script:
```python
module.imports =  [
    system
]
var.set a = test
if(a,"test"){
    system.out("A is equal to test")
} endif
```
Output:
```
A is equal to test
```
## Using function to a variable
Script:
```python
module.imports =  [
    system
    random
]
var.set a ~ random.int()
system.out(var.get(a))
```
Output would be anything from 1 - 0
## Inputs
Script:
```python
module.imports =  [
    system
    string
]
system.in("Enter your name:",name)
system.out(string.merge(Hello ,var.get(name),!))
```
Output:
```
Enter your name:Bob
Hello Bob!
```
# Keywords
These are the main and important keywords for this language
## module.imports
This is a system call to import the modules for the script to run

The current builtin modules are 
```json
{
    "modules": [
        "system",
        "random",
        "string"
    ]
}
```

The proper way to import a module is 
```python
module.imports =  [
    module_1
    module_2
]
```



