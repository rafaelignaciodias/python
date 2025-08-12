# Challenge 02
# Asking name and age before showing these details

first_name = input("What is your name? ")
try:
    age = int(input("How old are you? "))
except ValueError:
    print("Please enter a valid number for age.")
    exit()

print(f"Hi, {first_name}! You are {age} years old.")
print("Hi, {}! You are {} years old.".format(first_name, age))