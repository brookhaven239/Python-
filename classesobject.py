class Student:
    #Properties/Variables/Characteristics/Attribute
    name = "Tess"
    gender = "Female"
    age = 21

    #Behaviour/method
    def study(self):
        print("Student is studying")

mystudent = Student() #Creating an object
mystudent.study()

print(mystudent.name)

