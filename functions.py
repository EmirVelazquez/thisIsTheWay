# Making a function here
def greet_user(name, room):
    print("Hello Mister " + name + ", your room is " + str(room) + ".")


greet_user("Juan", 20)
greet_user("Cuauhtémoc", 24)

# Getting information back from a function
def cube_this(numb):
    return numb * numb * numb


result = cube_this(3)
print(result)
