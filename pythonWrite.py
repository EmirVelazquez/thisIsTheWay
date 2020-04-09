# Appending into a file
employee_file = open("employees.txt", "a")
# Overwriting everything in an existing file or creating a new file
employee_file = open("employees.txt", "w")

employee_file.write("\nMonica Hall - Board Member")

employee_file.close()
