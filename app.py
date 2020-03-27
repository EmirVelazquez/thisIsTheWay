# Common examples of working with string datatypes and common functions
phrase = "Peky's Bakery"
print(phrase.lower())
print(phrase.upper().isupper())
print(len(phrase))
print(phrase[0])
print(phrase.index("e"))
print(phrase.replace("Peky's", "Bruno & Peky's"))

# This grabs a module to access more math functions from python
from math import *

# Common examples of working with number datatypes and common functions
first_num = -5
print(str(first_num) + " comes after 4.")
print(abs(first_num))
print(pow(3, 2))
print(max(5, 2))
print(min(10, 1))
print(round(3.646))
print(floor(3.5))
print(ceil(3.7))
print(sqrt(36))
