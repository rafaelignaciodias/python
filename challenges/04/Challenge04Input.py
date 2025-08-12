# Challenge 02
# Asking name and age before showing these details

first_name = input("What is your name? ")
age = int(input("How old are you? "))

print(f"Hi, {first_name}! You are {age} years old.")
print("Hi, {}! You are {} years old.".format(first_name, age))