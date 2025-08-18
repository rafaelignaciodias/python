# core 071

# Using *args as parameters
def adding_args(*args):
    sum_value = 0
    for arg in args:
        sum_value += arg

    return sum_value


sum_value = adding_args(6, 5, 4, 3, 2, 1)
print(sum_value)
print(sum((6, 5, 4, 3, 2, 1)))
