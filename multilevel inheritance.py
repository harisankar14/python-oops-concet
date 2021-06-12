#multi level inherittance

class person:
    def display(self):
        print("hello this is parent class")

class employee(person):
    def printing(self):
        print("hello this 1st derived class")

class programmer(employee):
    def show(self):
        print("hello this is 2nd derived class")

p1=programmer()
p1.display()
p1.printing()
p1.show()
