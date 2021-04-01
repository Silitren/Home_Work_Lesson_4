# Task_2
my_list = input(f"Введите числовые значения через пробел: ").split()
for el in my_list:
    try:
        a = int(el)
    except ValueError:
        my_list.remove(el)
new_list = [my_list[el] for el in range(len(my_list)) if my_list[el] > my_list[el - 1]]
print(f"Ваш список: {new_list}")
