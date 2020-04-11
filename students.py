# Importing the Student class from the studentFile that has the class structure
from studentClass import Student

# Making an object here using the Student class
student1 = Student("Ricky Bobby", "Culinary Arts", 3.5, False)
student2 = Student("Michael Scott", "Business Management", 1.9, True)
student3 = Student("Bruno Velazquez", "Psychology", 4.0, True)

# Printing object values from student class
print(student1.name, student1.gpa)
print(student2.name, student1.major)

# Using function in class to check if the student is on dean's list
print(student3.on_dean_list())
print(student2.on_dean_list())
print(student1.on_dean_list())
