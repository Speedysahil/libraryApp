class Dog:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def add_one(self,x):
        return x+1

    def bark(self):
        print("bark")

    def get_name(self):
        return self.name
    def get_age(self):
        return self.age

    def set_age(self,age):
        self.age = age


dog1_name = "rocky"
dog1_age = 33

