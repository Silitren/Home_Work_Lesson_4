# Task_4
my_list = input("Введите исходный список: ").split()
print(f"Элементы списка, не имеющие повторений: {[el for el in my_list if my_list.count(el) == 1]}")
