# Importing the Student class from the studentFile that has the class structure
from studentFile import Student

# Making an object here using the Student class
student1 = Student("Ricky Bobby", "Culinary Arts", 3.5, False)
student2 = Student("Michael Scott", "Business Management", 1.9, True)

print(student1.name, student1.gpa)
print(student2.name, student1.major)
