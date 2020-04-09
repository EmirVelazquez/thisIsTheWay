# Translator that changes any vowels to g
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation.lower()


print(translate(input("Enter a phrase: ")))

# Try Except Blocks
try:
    value = 10 / 0
    number = float(input("Enter a number: "))
    print(number)
# Catching specific errors
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid input")
