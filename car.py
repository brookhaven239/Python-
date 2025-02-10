class Car:
    def __init__(self,brand,color,yom):
        self.brand = brand
        self.color = color
        self.yom = yom

    def drive(self):
            print("You drive a",self.brand,"of a",self.color," color")
car1 = Car("Mercedace","Black",2025)
print(car1.brand)
print(car1.color)
print(car1.yom)
car1.drive()

car2 = Car("BMW","silver",2023)
print(car2.brand)
print(car2.color)
print(car2.yom)
car2.drive()
