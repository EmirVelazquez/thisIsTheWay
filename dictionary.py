# Dictionaries (Like a json object, note: keys can be numbers too)
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

# Access info in dictionary
print(monthConversions["Nov"])
print(monthConversions.get("Mar"))
# Able to use get() to provide a default value if the key doesn't exist
print(monthConversions.get("Dod", "Not a valid key"))
