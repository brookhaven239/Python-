#Built-n functions

y = max(56,75,23,18,25)
print("The maximum value is",y)

x = min(23,1,0,40,32,76,23)
print("The minumum value is",x)

#user-defined functions
def name():
    print("Leon")
name() #calling a function

def product():
    a = 10
    b = 20
    print(a*b)
product()


#Parameter/variable and Argument/value
def sum(num1,num2):
     print(num1+num2)
sum(5,6)
sum(10,20)
sum(30,40)

def Employee(name,age,position,salary):
    print(name,age,position,salary)
Employee("Leon",30,"CEO",600000.00)
Employee("James",20,"manager",500000.00)
Employee("Mary",20,"supervisor",400000.00)
Employee("Antony",25,"HR",300000.00)
Employee("Shanice",19,"Receptionist",205000.00)
Employee("Shetty",22,"Secretary",200000.00)
Employee("Duran",20,"Janitor",150000.00)
Employee("Mike",38,"Cook",100000.00)


# A program to display user information of five students
def student(fullname,age,course,gender,nationality):
    print(fullname,age,course,gender,nationality)
student("John leon",18,"MIT","Male","kenyan")
student("Shetty bestie",19,"Carbin crew","Female","Spanish")
student("Antony Karanja",17,"Cyber security","Male","Brazilian")
student("Shanice muthoni",18,"Hacking","FeMale","Tazanian")
student("Vybz kartel",19,"MIT","Male","Jamaican")



