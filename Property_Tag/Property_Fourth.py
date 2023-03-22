class Student:
    def __init__(self, name, age, major):
        self._name = name
        self._age = age
        self._major = major
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

    def print_courses(self):
        print(f"{self.name}'s courses:")
        for course in self.courses:
            print(f"- {course}")

    def change_major(self, new_major):
        self._major = new_major

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @name.deleter
    def name(self):
        del self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

    @age.deleter
    def age(self):
        del self._age

    @property
    def major(self):
        return self._major

    @major.setter
    def major(self, value):
        self._major = value

    @major.deleter
    def major(self):
        del self._major
student1 = Student("shivanshu", 23, "Computer Science")
student1.add_course("Programming 101")
student1.add_course("Data Structures")
student1.print_courses()

student1.change_major("Information Science")
print(f"{student1.name}'s new major is {student1.major}.")

student1.name = "sahil"
print(f"{student1.name}'s age is {student1.age}.")

del student1.major
print(f"{student1.name} has no major.")
