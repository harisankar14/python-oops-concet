#multi level inheritance
class land_animal:              #father class
    def display(self):
        print("this animal lives in the land")

class water_animal:              #mother class
    def show(self):
        print("this animal lives in the water")


class frog(land_animal,water_animal):
    pass


f1=frog()
f1.display()
f1.show()
