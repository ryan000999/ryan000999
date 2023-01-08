# class object
# class - blueprint
# object
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set_age(self, age):
        self.age = age

    @property
    def increase_15(self):
        return self.age + 15

    def __str__(self):
        return f"<Student: name={self.name}, age={self.age}>"


    def __gt__(self, other):
        return self.age > other.age

    @classmethod
    def create_student(cls, name):
        return cls(name, 18)

    @staticmethod
    def calc_year(age):
        return 2023 - age


student_one = Student("Kenny", 23)

print(student_one.name)
print(student_one.age)

student_one.name = "Anna"
print(student_one.name)

# student_one.age = 46
student_one.set_age(46) # Student.set_age(student_one, 46)
print(student_one.age)

student_18 = Student.create_student("Henry")
print(student_18)

# Calc birth year
year = Student.calc_year(student_18.age)
print(year)

print(student_18.calc_year(28))

print('-' * 30)

print(student_one > student_18)

print(student_18.increase_15)
