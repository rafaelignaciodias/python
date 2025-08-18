# core 069

# debugging class using core068 as the source
x = 1
y = 2


def scope():
    x = 10

    print(x)
    print(y)


scope()
