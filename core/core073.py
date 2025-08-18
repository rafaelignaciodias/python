# core 073

# higher order functions - first class functions
def create_greeting(msg, name):
    return f"{msg}, {name}."


def execute(function, *args):
    return function(*args)


print(execute(create_greeting, "good morning", "coder"))
print(execute(create_greeting, "good evening", "tester"))
