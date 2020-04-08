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

# Exponent function
def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result


print(raise_to_power(3, 4))
print(raise_to_power(3, 2))
print(raise_to_power(2, 3))
