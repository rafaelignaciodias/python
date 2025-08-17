# core 067

# defining function
def print_sum(x, y, z=None):
    if z is not None:
        print("x + y + z:", x + y + z)
    else:
        print("x + y:", x + y)


print_sum(3, 4)
print_sum(13, 24)
print_sum(23, 24, 8)
