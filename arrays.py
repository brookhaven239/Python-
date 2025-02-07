
courses = ["MIT","Python","Android"]
print(courses)


#accessing an element
print(courses[0])

#looping through an array
for cour in courses:
    print(cour)

#Adding a new element into an array
courses.append("java")
print(courses)


#Removing an element
courses.remove("Android")
print(courses)
in