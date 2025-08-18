# core 074

# closure definition
def create_greeting(msg):
    def greet(name):
        return f"{msg}, {name}."

    return greet


new_greeting = create_greeting("good morning")
print(new_greeting("sunshine"))

old_greeting = create_greeting("good night")
print(old_greeting("coder"))
