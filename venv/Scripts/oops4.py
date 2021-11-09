class Human:
    number_of_humans = 10

    def __init__(self,name,age,color):
        self.name = name
        self.age = age
        self.color = color

    def human_good(self,string):
        return string

    def bad_human(self,string):
        return string

    @classmethod
    def change_humans(cls,new_humans):
        cls.number_of_humans = new_humans

    @classmethod
    def from_str(cls,string):
        params = string.split("-")
        return cls(params[0],params[1],params[2])




h1 = Human("rohit",45,"black")
h2 = Human("sohit",33,"fair")
h3 = Human.from_str("ramesh-33-savla")

print(h3.color)


