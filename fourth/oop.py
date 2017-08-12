class Student:

    def __init__(self,n,a = None):
        self.full_name = n
        self.age= a

    def get_age(self):
        return self.age

    def get_name(self):
        return self.full_name

    def __str__(self):
        return "Name :" + str(self.full_name) + "\n" + "Age:" + str(self.age)

obj = Student("Saurav",20)
obj1 = Student("Saurav")
print(obj)
print(obj.get_name())
print(obj1.get_name())