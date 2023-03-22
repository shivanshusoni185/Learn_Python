def star_pattern(func):
    def wrapper(n):
        for i in range(n):
            #print("star")
            func(i, n)
    return wrapper

@star_pattern
def right_triangle(i, n):
    print("* "*(i+1))

@star_pattern
def inverted_right_triangle(i, n):
    print("* "*(n-i))

@star_pattern
def diamond_pattern(i, n):
    if i < n//2:
        print(" "*(n//2-i) + "* "*(i+1))
    else:
        print(" "*(i-n//2) + "* "*(n-i))

n = int(input("Enter the number of rows: "))
print("Right Triangle Star Pattern:")
right_triangle(n)
print("\nInverted Right Triangle Star Pattern:")
inverted_right_triangle(n)
print("\nDiamond Star Pattern:")
diamond_pattern(n)
