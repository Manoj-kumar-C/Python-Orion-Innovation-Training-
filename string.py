# String basics
name = "Manoj Kumar"

# Accessing characters
print(name[0])  # M

# String methods
print(name.upper())      # MANOJ KUMAR
print(name.lower())      # manoj kumar
print(name.replace(" ", "_"))  # Manoj_Kumar
print(name.split())      # ['Manoj', 'Kumar']

# f-strings
age = 21
print(f"My name is {name} and I am {age} years old.")
