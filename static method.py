class person:
     '''what if i dont want to use self inside the display method then i have to mention @static method after declaring the class else instead of self i may use myself,ram,krushna etc whatever'''
    #def display(self): '''i dont want to write like this'''
     @staticmethod
     def display():
        print("hello")
    
p=person()
p.display()
