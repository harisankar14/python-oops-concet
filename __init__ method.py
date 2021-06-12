#__init__ method

class person:
    def __init__(self,name):   #syntax for initialization
        self.name=name  #initialized


#now i take another function/method
        
    def display(self):
        print("hello",self.name)

#now outside the class we will create an object

p1=person("Hari")

#now no need to call __init__ method because when we created the object automatically it was called so we will call the display method

p1.display()


#o/p-hello Hari
''' here we use self in every method inside  class but why do we do that ?? it is just to diffrentiate between the instance variable and the global variable
then what is local or instance variable ??- it means the variable is belongs to the object.Here self.name is the instance variable'''
        
    
