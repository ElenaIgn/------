user_input = input("Введите элементы списка через запятую, точку с запятой или слэш: ")


separator = None
for sep in [',', ';', '/']:
    if sep in user_input:
        separator = sep
        break


if separator is None:
    source_list = [user_input.strip()] if user_input.strip() else []
else:
    other_separators = [sep for sep in [',', ';', '/'] if sep != separator]
    if any(other_sep in user_input for other_sep in other_separators):
        print("Ошибка: нельзя использовать разные разделители одновременно!")
        exit()
    
    source_list = [item.strip() for item in user_input.split(separator)]

unique_list = [x for x in source_list if source_list.count(x) == 1]

result_str = ", ".join(unique_list)
print(f"Результат: {result_str}")
