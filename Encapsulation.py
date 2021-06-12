#Encapsulation--->it is used to prevent the data from being modified accidentaly.

class car:
    def __init__(self):
        self.__updatesoftware()
    def drive(self):
        print("driving")
    def __updatesoftware(self):
        print("updating software")

car1=car()
car1.drive()
