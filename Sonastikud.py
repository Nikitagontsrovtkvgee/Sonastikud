from gtts import gTTS
from playsound import playsound
import random

# Словарь с эстонско-русскими переводами
sonastik = {
    'koer': 'собака',   
    'kass': 'кошка',     
    'maja': 'дом',     
    'auto': 'машина',   
    'päike': 'солнце' 
}

# Функция для озвучки текста на заданном языке
def raagi(tekst, keel='et'):
    heli = gTTS(text=tekst, lang=keel)  # создаём объект для озвучки
    heli.save("heli.mp3")               # сохраняем в файл
    playsound("heli.mp3")               # проигрываем аудио

# Функция для перевода с эстонского на русский
def tolgi_est_rus():
    sona = input("Sisesta sõna eesti keeles: ")  # Запрос слова на эстонском
    if sona in sonastik:  # Если слово есть в словаре
        print("Vene keeles:", sonastik[sona])   # Выводим перевод на русский
        raagi(sona, 'et')  # Озвучиваем слово на эстонском
        raagi(sonastik[sona], 'ru')  # Озвучиваем перевод на русском
    else:
        print("Sõna ei leitud.")  # Если слова нет в словаре

# Функция для перевода с русского на эстонский
def tolgi_rus_est():
    sona = input("Sisesta sõna vene keeles: ")  # Запрос слова на русском
    vasted = [e for e, v in sonastik.items() if v == sona]  # Поиск слова в словаре
    if vasted:  # Если найдено хотя бы одно слово
        print("Eesti keeles:", ', '.join(vasted))  # Выводим переводы на эстонском
        raagi(sona, 'ru')  # Озвучиваем слово на русском
        raagi(vasted[0], 'et')  # Озвучиваем перевод на эстонском
    else:
        print("Sõna ei leitud.")  # Если слова нет в словаре

# Функция для добавления нового слова в словарь
def lisa_sona():
    eesti = input("Sisesta uus sõna eesti keeles: ")  # Запрос нового слова на эстонском
    vene = input("Sisesta selle vene tõlge: ")  # Запрос перевода на русский
    sonastik[eesti] = vene  # Добавляем пару в словарь
    print("Sõna lisatud!")  # Подтверждение

# Функция для исправления слова в словаре
def paranda_sona():
    eesti = input("Millist eesti sõna soovid parandada? ")  # Запрос слова для исправления
    if eesti in sonastik:  # Если слово есть в словаре
        uus = input("Sisesta parandatud eesti sõna (või vajuta Enter kui sama): ")  # Запрос нового слова
        vene = input("Sisesta uus vene tõlge: ")  # Запрос нового перевода
        uus = uus or eesti  # Если новое слово не введено, оставляем старое
        del sonastik[eesti]  # Удаляем старую пару
        sonastik[uus] = vene  # Добавляем исправленную пару
        print("Sõna parandatud!")  # Подтверждение
    else:
        print("Sõna ei leitud.")  # Если слово не найдено в словаре

# Функция для теста знаний пользователя
def testi_teadmisi():
    print("Test algab!")  # Начало теста
    kysimused = list(sonastik.items())  # Переводим словарь в список
    random.shuffle(kysimused)  # Перемешиваем вопросы
    oiged = 0  # Счётчик правильных ответов
    for est, rus in kysimused:  # Проходим по всем словам
        vastus = input(f"Sisesta vene tõlge sõnale '{est}': ")  # Запрос ответа
        if vastus.lower() == rus.lower():  # Проверка ответа
            print("Õige!")  # Если правильно
            oiged += 1  # Увеличиваем счётчик
        else:
            print(f"Vale! Õige vastus: {rus}")  # Если неправильно
    protsent = round((oiged / len(kysimused)) * 100)  # Рассчитываем процент правильных ответов
    print(f"Test lõppenud. Tulemus: {protsent}%")  # Выводим результат

# Меню программы
def menuu():
    while True:  # Цикл, который работает, пока пользователь не выберет "выход"
        print("\n--- Eesti-Vene sõnastik ---")
        print("1 - Tõlgi eesti -> vene")  # Перевод с эстонского на русский
        print("2 - Tõlgi vene -> eesti")  # Перевод с русского на эстонский
        print("3 - Lisa uus sõna")  # Добавление нового слова
        print("4 - Paranda sõna")  # Исправление слова
        print("5 - Testi teadmisi")  # Тестирование знаний
        print("6 - Välju")  # Выход из программы
        valik = input("Tee oma valik: ")  # Запрос выбора пользователя

        if valik == "1":
            tolgi_est_rus()  # Перевод с эстонского на русский
        elif valik == "2":
            tolgi_rus_est()  # Перевод с русского на эстонский
        elif valik == "3":
            lisa_sona()  # Добавление нового слова
        elif valik == "4":
            paranda_sona()  # Исправление слова
        elif valik == "5":
            testi_teadmisi()  # Тестирование знаний
        elif valik == "6":
            print("Head aega!")  # Прощание с пользователем
            break  # Выход из программы
        else:
            print("Tundmatu valik.")  # Если введён некорректный выбор

# Запуск программы
menuu()