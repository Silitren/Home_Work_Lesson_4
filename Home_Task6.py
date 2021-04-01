# Task_6
from sys import argv
import itertools

list_1 = [1, "b", 3, 554, True]
try:
    skript_test, cycle_1 = argv
    a = itertools.count(int(cycle_1), 1)
    b = itertools.cycle(list_1)
    c = next(a)
    try:
       while c < 10:
           c = next(a)
           print(f"Следующее целое число: {c}")
       for el in range(15):
           print(f"Ваш повторяющиеся значения: {next(b)}")
    except ValueError:
        print("Вы ввели текст")
except ValueError:
    print("Вы ввели недостаточное количество значений")
