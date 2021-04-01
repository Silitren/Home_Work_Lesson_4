# Task_5
from functools import reduce

print(f"Сумма ччетных чисел от 100 до 1000 составляет: {reduce(lambda x, y: x + y, [el for el in range(100, 1001, 2)])}")