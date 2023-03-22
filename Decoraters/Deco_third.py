#Decorator Chaining
def decor(func):
    def inner(name):
        print("First Decor Function Execution")
        func(name)
    return inner

def decor1(func):
    def inner(name):
        print("Second Decor Exexution")
        func(name)
    return inner

@decor1
@decor
def wish(name):
    print("Hello",name,"Good Day")
wish("Shivanshu")