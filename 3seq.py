input1 = input("Введите элементы 1-го списка через запятую: ")
input2 = input("Введите элементы 2-го списка через запятую: ")

list1 = [item.strip() for item in input1.split(',')]
list2 = [item.strip() for item in input2.split(',')]

result_list = [x for x in list1 if x not in list2]

print(f"Результат: {', '.join(result_list)}")
