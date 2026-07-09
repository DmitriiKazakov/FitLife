# Проект FitLife - MVP версия 1.0

WATER_PER_KG = 30  # Колличество мл на 1 кг веса
LI_TO_ML = 1000  # Константа кол-во мл в л

# 1. Знакомство

print('Добро пожаловатьв сервис FitLife! Давайте знакомится!')
user_name = input('Как вас зовут? ')  # Знакомство с пользователем
user_name = user_name.title()  # Имя с заглавной буквы

print('Для точного расчета, нам понадобится немного информации о Вас')
user_age = input('Напишите сколько Вам лет? ')  # Запрашиваем возраст
user_age = int(user_age)  # Переводим в число

# 2. Сбор данных, вес и рост

user_weight = input('Введите ваш вес в кг ')  # Запрашиваем вес
if ',' in user_weight:  # Проверяем правильность написания дробного числа
    _a = user_weight.replace(',', '.')  # заменяем символ , на .
    user_weight = float(_a)  # Переводим вес в дробное число
else:
    user_weight = float(user_weight)

user_height = input('Введите ваш рост в м ')  # Запрашиваем рост
if ',' in user_height:  # Проверяем правильность написания дробного числа
    _a = user_height.replace(',', '.')  # заменяем символ , на .
    user_height = float(_a)  # Переводим вес в дробное число
else:
    user_height = float(user_height)

# 3. Рассчет bmi (Индекс массы тела)

bmi = round((user_weight / (user_height ** 2)), 1)  # Расчет ИМТ

# Подсчет воды: вес * 30 мл

water_needed = (user_weight * WATER_PER_KG / LI_TO_ML)  # расчет нормы воды в л

# 4. Вывод красивого результата
print('-' * 40)  # наводим красоту :-)
print(f'Ваш отчет готов: {user_name} !')
print(f'Ваши данные: \n Возраст - {user_age} \n Рост - {user_height} м \
       \n вес: {user_weight} кг \т ИМТ: {bmi}')
print(f'Рекомендуемая норма воды: {water_needed:.1f} л. в день')
print('-' * 40)
