#How to call same function with decorator and without decorator:
def decor(func):
    def inner(name):
        if name=="sunny":
            print("Hello",name,"its your bad mornining")
        else:
            func(name)
    return inner


def wish(name):
    print("Hello",name,"Its your good mornining")

decorfunction=decor(wish)

wish('shivanshu')#Decorater wont we executed
wish('sunny')#Decorater wont we executed

decorfunction("shivanshu")
decorfunction("sunny")