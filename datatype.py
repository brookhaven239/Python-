
number = 20 #Integer "Int"
num = 35.32 #Float
greeting = "Hello there" #String "str"
IsPythonIntresting = True #Boolean



#Data structures
#list "just a list ol & ul""[]"
cars = ["Bughati","porsche","Toyota supra"]
#tuple "is on value carrying multiple values""()"
fruits = ("banana","apple","orange")
#set "{}" "They don't follow any format"
countries = {"kenya","Tanzania","England","Italy","Brazil","Jamaica"}
#Dictionary "{}" "is a key value-pair"
details = {
    "firstname" : "Leon",
    "course" : "MIT",
    "nationality" : "Kenyan",
    "age" : 17.8
}


print(number)
print(num)
print(greeting)
print(IsPythonIntresting)

print(cars)
print(fruits)
print(countries)
print(details)
print(details["nationality"])

#Determining the datatype
print(type(greeting))
print(type(countries))

#Typecasting "converting one datatype to another"
print(float(number))
print(int(num))


