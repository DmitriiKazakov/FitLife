# Проект FitLife - MVP версия 1.0

WATER_PER_KG = 30  # Колличество мл на 1 кг веса
LI_TO_ML = 1000  # Константа кол-во мл в л

# 1. Знакомство

print('Добро пожаловать в сервис FitLife! Давайте знакомится!')
while True:
    user_name = input('Как вас зовут? ')  #  Знакомство с пользователем
    if not user_name.isalpha():  # Проверяем наличие букв 
        print("Введите пожалуйста имя!")
    else:
        break
user_name = user_name.title()  # Имя с заглавной буквы

print('Для точного расчета, нам понадобится немного информации о Вас')
while True:  # Проверяем наличие цифр, вызываем цикл пока не ввести число
    try:
        user_age = int(input('Напишите сколько Вам лет? '))  # Запрашиваем возраст
        break
    except ValueError:
        print('Необходимо вводить только цифры!')

# 2. Сбор данных, вес и рост

while True:  # Проверяем наличие цифр, вызываем цикл пока не ввести число
    try:
        user_weight = input('Введите ваш вес в кг ')  # Запрашиваем вес
        _a = user_weight.replace(',', '.')  # заменяем символ , на .
        user_weight = float(_a)  # Переводим вес в дробное число
        break
    except ValueError:
        print("Необходимо ввести число!")

while True:  # Проверяем наличие цифр, вызываем цикл пока не ввести число
    try:
        user_height = input('Введите ваш рост в м ')  # Запрашиваем рост
        _a = user_height.replace(',', '.')  # заменяем символ , на .
        user_height = float(_a)  # Переводим вес в дробное число
        break
    except ValueError:
        print("Необходимо ввести число!")

# 3. Рассчет bmi (Индекс массы тела)

bmi = round((user_weight / (user_height ** 2)), 1)  #Расчет индекса массы тела

# Подсчет воды: вес * 30 мл

water_needed = (user_weight * WATER_PER_KG / LI_TO_ML)  # расчет нормы воды в л

# 4. Вывод красивого результата
print('-' * 40)  # наводим красоту :-)
print(f'Ваш отчет готов: {user_name} !')
print(f'Ваши данные: \n Возраст - {user_age} \n Рост - {user_height} \
м \n Вес: {user_weight} кг \n ИМТ: {bmi}')
print(f'Рекомендуемая норма воды: {water_needed:.1f} л. в день')
print('-' * 40)
