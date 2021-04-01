# Task_7
# Надеюсь я понял правильно задание
import math


def my_generator():
    """
    Формирование промижуточных значений факториала n
    :return:
    """
    for el in range(1, n + 1):
        yield math.factorial(el)


while True:
    n = int(input("Введите чилсо: "))
    try:
        for el in my_generator():
            print(el)
        break
    except ValueError:
        print("Введите число")