def decor(func):
    def inner(name):
        if name=="sunny":
            print("Hello",name,"its your bad mornining")
        else:
            func(name)
    return inner
@decor
def wish(name):
    print("Hello",name,"Its your good mornining")

wish('shivanshu')
wish('sahil')
wish('sunny')
wish('manoj')