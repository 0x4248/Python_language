def replace_str(string, replace_with, replace_with_this):
    return string.replace(replace_with, replace_with_this)
def trim(string,trim):
    return string[int(trim)]
def merge(argv):
    output = ""
    for i in argv:
        output += str(i)
    return output