# Reading a file from an outside source (modes are 'r' for read 'w' for write 'a' for append 'r+' read and write)
employee_file = open("employees.txt", "r")

# check to see if file is readable (boolean)
print(employee_file.readable())

# will read the whole file
print(employee_file.read())

# will read a line
print(employee_file.readline())

# will read all of the lines and put them in an array
print(employee_file.readlines())

# loop through a file
for employee in employee_file.readlines():
    print(employee)

# this closes the file
employee_file.close()
