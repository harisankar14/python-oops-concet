class person:
    def __init__(self,name):
        self.name=name #it is instnce varible (means this variable belongs to the object)
        name="john" #it is local variable
        print(name)
    def display(self):
        print("hello",self.name)

p1=person("hari")
p1.display()

''' o/p-john
        hello hari'''
    
    
