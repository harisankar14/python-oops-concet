#inheritance means more than one class
#it allows one class to inherit the properties of another class
#means we can create one class using already existing class properties

class animal:
    def eat(self):
        print("eating")

'''class dog:
    def eat(self):####
        print("eating")###
    def bark(self):
        print("barking")'''#in normal oops we write like this to create two diffrent class ,under dog class also we had to mention again the eat property 

#but in inheritance we will inherit the property eat from the animal class i.e. parent class
class dog(animal):
    def bark(self):
        print("barking")


d=dog()
d.eat()
d.bark()

''' here inside dog class we have not given the eating property but it will inherit the eat property from the animal class and it will print ""eating" when we call d.eat() '''
