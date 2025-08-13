# Challenge 05
# Asking two values and calculating addition, subtraction, multiplication, division and power

value1 = float(input("First  value   : "))
value2 = float(input("Second value   : "))

addition_value = value1 + value2
subtraction_value = value1 - value2
multiplication_value = value1 * value2

if value2 != 0:
    division_value = value1 / value2
else:
    division_value = "undefined (division by zero)"

power_value = value1 ** value2

print(f"\nAddition       : {addition_value}")
print(f"Subtraction    : {subtraction_value}")
print(f"Multiplication : {multiplication_value}")
print(f"Division       : {division_value}")
print(f"Power          : {power_value}")