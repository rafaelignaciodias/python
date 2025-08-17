# core 068

# function scope
x = 1
y = 2


def scope():
    x = 10

    print(x)
    print(y)


scope()
