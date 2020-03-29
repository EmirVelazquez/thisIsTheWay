# Working with lists basics (similar to an array from JS)
random_numbers = [44, 4, 5, 24, 42, 10]
office_char = ["Michael", "Jim", "Dwight", "Pam", "Karen", "Toby", "Dwight", "Dwight"]

print(office_char)
# Return element index 4
print(office_char[4])
# Return element from index 2 and forward
print(office_char[2:])
# Return elements within specified range
print(office_char[1:4])

# ==================================================================================
# Common list functions
# ==================================================================================
# Combines the passed list at the end of the list
office_char.extend(random_numbers)
print(office_char)

# Inserts the speficifed element to the end of list
office_char.append("Oscar")
print(office_char)

# Inserts the second paramater at the specific index
office_char.insert(1, "Michael")
print(office_char)

# Removes a specific element from the list
office_char.remove("Toby")
print(office_char)

# Removes all of the elements from the list
office_char.clear()
print(office_char)

# Removes last element from list
office_char.pop()
print(office_char)

# Get the index of an existing element in the list only (will error if it doesn't exist in list)
print(office_char.index("Jim"))
print(office_char.index("Creed"))

# Will return the number of times the specified element exists in the list
print(office_char.count("Dwight"))

# Will sort in ascending order (Alphabetical in this case)
office_char.sort()
print(office_char)
# Ascending order (lowest number to highest)
random_numbers.sort()
print(random_numbers)

# Self explanatory
random_numbers.reverse()
print(random_numbers)

office_char2 = office_char.copy()
print(office_char2)
