#Using **kwargs to pass the variable keyword arguments to the function
def intro(**data):
    print("\nData type of argument:",type(data))

    for key, value in data.items():
        print("{} is {}".format(key,value))

intro(Firstname="shivu", Lastname="soni", Age=22, Phone=1234567890)
intro(Firstname="sahil", Lastname="soni", Email="sahilsoni@nomail.com", Country="india", Age=21, Phone=11111111)