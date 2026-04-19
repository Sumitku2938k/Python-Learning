# class -> blank reservation of a form
# object -> filled railway reservation form

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def getSalary(self):
        print(self.salary)


rohan = Employee("Rohan",5000)
# print(rohan.name)
# print(rohan.salary)
rohan.getSalary()

goutam = Employee("Goutam",10000000)
# print(goutam.name)
# print(goutam.salary)
goutam.getSalary()