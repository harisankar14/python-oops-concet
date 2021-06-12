#method over ridding
class a:
    def display(self):
        print("this method belongs to class a")

class b(a):
    def display(self):
        print("this methodbelongs to class b")


obj=b()
obj.display()

''' Here content of display method in class a is changed in class b by overridding it so whenever we will call the display method then the content of display method in class b will be printed'''
