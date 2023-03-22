class Human:
    def __init__(self, age):
        self.age = age

    @property
    def age(self):
        return self._age

    @property
    def months(self):
        return self._age * 12

    @age.setter
    def age(self, new_age):
        self._age = new_age
shivu = Human(26)

print('I am ')
print(shivu.age)
print(' years old.')