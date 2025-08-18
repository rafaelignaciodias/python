# core 075

# practicing a interger argument
def multiply_argument(x):
    value = ""
    for _ in range(x):
        value += str(x)

    return value


def create_multiplier(multiplicator):
    def multiply(number):
        return number * multiplicator

    return multiply


duplicate = create_multiplier(2)
triplicate = create_multiplier(3)

print(duplicate(2))
print(triplicate(15.6))


print(multiply_argument(2))
print(multiply_argument(3))
print(multiply_argument(4))
