# core 072

# practicing functions
def multiply_values(*args):
    acumulator = 1
    for arg in args:
        acumulator *= arg
    return acumulator


def odd_right(x):
    if x % 2 == 0:
        return "right"
    else:
        return "odd"


total = multiply_values(1, 2, 3, 4, 5)
print(f"The total is {total}, and this number is {odd_right(total)}.")
