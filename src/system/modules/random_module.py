functions = ["int","char","intrange"]
import random
def rand_int():
    return str(random.random())
def rand_char():
    return random.choice(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"])
def rand_intrange(min,max):
    return str(random.randint(int(min),int(max)))
