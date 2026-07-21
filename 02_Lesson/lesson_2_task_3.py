import math


def square(side):
    area = side * side
    return math.ceil(area)


# Пример
side_length = 5.2
result = square(side_length)
print(f"Площадь квадрата со стороной {side_length}: {result}")
