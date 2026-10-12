count = int(input("Введите количество элементов: "))

elements = []

for i in range(1, count + 1):
    num = int(input(f"Введите {i} элемент: "))
    elements.append(num)

elements.sort()

print(f"Вывод: {elements}")
