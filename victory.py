import random

# Словарь из 10 известных людей и их дат рождения
famous_people = {
    "Александр Пушкин": "06.06.1799",
    "Юрий Гагарин": "09.03.1934",
    "Альберт Эйнштейн": "14.03.1879",
    "Леонардо да Винчи": "15.04.1452",
    "Исаак Ньютон": "04.01.1643",
    "Михаил Ломоносов": "19.11.1711",
    "Лев Толстой": "09.09.1828",
    "Дмитрий Менделеев": "08.02.1834",
    "Вольфганг Моцарт": "27.01.1756",
    "Петр Первый": "09.06.1672"
}

# Вспомогательный словарь для текстового вывода месяцев
months_dict = {
    "01": "января", "02": "февраля", "03": "марта", "04": "апреля",
    "05": "мая", "06": "июня", "07": "июля", "08": "августа",
    "09": "сентября", "10": "октября", "11": "ноября", "12": "декабря"
}

while True:
    # Выбираем 5 случайных имен из ключей словаря
    sampled_names = random.sample(list(famous_people.keys()), 5)
    
    correct_answers = 0
    wrong_answers = 0
    
    print("\n--- Начало викторины! ---")
    
    for name in sampled_names:
        correct_date = famous_people[name]
        user_answer = input(f"Угадайте дату рождения ({name}) в формате dd.mm.yyyy: ").strip()
        
        if user_answer == correct_date:
            print("Правильно!")
            correct_answers += 1
        else:
            day, month, year = correct_date.split('.')
            day_clean = str(int(day)) 
            month_word = months_dict[month]
            
            print(f"Неверно. Правильный ответ: {day_clean} {month_word} {year} года")
            wrong_answers += 1
            
    print("\n--- Итоги викторины ---")
    print(f"Количество правильных ответов: {correct_answers}")
    print(f"Количество ошибок: {wrong_answers}")
    
    play_again = input("Хотите начать сначала? (да/нет): ").strip().lower()
    if play_again != 'да':
        print("Спасибо за игру!")
        break
