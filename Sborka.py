import random
import time
import calendar
import math

def calculator():
    try:
        num1 = float(input("Введите первое число: "))
        op = input("Введите оператор (+, -, *, /): ")
        num2 = float(input("Введите второе число: "))
        
        if op == "+":
            print("Результат:", num1 + num2)
        elif op == "-":
            print("Результат:", num1 - num2)
        elif op == "*":
            print("Результат:", num1 * num2)
        elif op == "/":
            if num2 != 0:
                print("Результат:", num1 / num2)
            else:
                print("Ошибка: деление на ноль!")
        else:
            print("Ошибка: неверный оператор!")
    except ValueError:
        print("Ошибка: введите числа!")

def random_number():
    print("Случайное число:", random.randint(1, 100))

def timer():
    seconds = int(input("Введите количество секунд: "))
    print("Таймер запущен...")
    time.sleep(seconds)
    print("Время вышло!")

def password_generator():
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"
    length = int(input("Длина пароля: "))
    password = "".join(random.choice(chars) for _ in range(length))
    print("Сгенерированный пароль:", password)

def coin_flip():
    print("Результат подбрасывания монеты:", random.choice(["Орел", "Решка"]))

def rock_paper_scissors():
    choices = ["Камень", "Ножницы", "Бумага"]
    user = input("Выберите (Камень, Ножницы, Бумага): ").capitalize()
    computer = random.choice(choices)
    print("Компьютер выбрал:", computer)
    
    if user == computer:
        print("Ничья!")
    elif (user == "Камень" and computer == "Ножницы") or \
         (user == "Ножницы" and computer == "Бумага") or \
         (user == "Бумага" and computer == "Камень"):
        print("Вы победили!")
    else:
        print("Вы проиграли!")

def calendar_view():
    year = int(input("Введите год: "))
    month = int(input("Введите месяц (1-12): "))
    print(calendar.month(year, month))

def factorial():
    num = int(input("Введите число: "))
    print("Факториал:", math.factorial(num))

def quadratic_solver():
    print("Решение уравнения ax² + bx + c = 0")
    a = float(input("Введите a: "))
    b = float(input("Введите b: "))
    c = float(input("Введите c: "))
    d = b**2 - 4*a*c
    
    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2*a)
        x2 = (-b - math.sqrt(d)) / (2*a)
        print(f"Корни уравнения: {x1}, {x2}")
    elif d == 0:
        x = -b / (2*a)
        print(f"Один корень: {x}")
    else:
        print("Корней нет!")

def even_or_odd():
    num = int(input("Введите число: "))
    print("Четное" if num % 2 == 0 else "Нечетное")

def guess_number():
    num = random.randint(1, 10)
    guess = int(input("Угадайте число от 1 до 10: "))
    print("Вы угадали!" if guess == num else f"Неверно! Было {num}")

def string_reverser():
    text = input("Введите строку: ")
    print("Перевернутая строка:", text[::-1])

def fibonacci():
    n = int(input("Введите количество чисел Фибоначчи: "))
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()

def bmi_calculator():
    weight = float(input("Введите вес (кг): "))
    height = float(input("Введите рост (м): "))
    bmi = weight / (height ** 2)
    print("Ваш ИМТ:", round(bmi, 2))

def text_counter():
    text = input("Введите текст: ")
    print("Количество символов:", len(text))

def anagram_checker():
    word1 = input("Введите первое слово: ").replace(" ", "").lower()
    word2 = input("Введите второе слово: ").replace(" ", "").lower()
    print("Это анаграмма!" if sorted(word1) == sorted(word2) else "Не анаграмма.")

def simple_timer():
    seconds = int(input("Введите секунды для обратного отсчета: "))
    while seconds:
        print(seconds)
        time.sleep(1)
        seconds -= 1
    print("Время вышло!")

def day_of_week():
    year = int(input("Введите год: "))
    month = int(input("Введите месяц: "))
    day = int(input("Введите день: "))
    days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
    print("Это был", days[calendar.weekday(year, month, day)])

def main():
    options = {
        "1": ("Калькулятор", calculator),
        "2": ("Случайное число", random_number),
        "3": ("Таймер", timer),
        "4": ("Генератор паролей", password_generator),
        "5": ("Монетка", coin_flip),
        "6": ("Камень-ножницы-бумага", rock_paper_scissors),
        "7": ("Календарь", calendar_view),
        "8": ("Факториал", factorial),
        "9": ("Решение квадратных уравнений", quadratic_solver),
        "10": ("Четное или нечетное", even_or_odd),
        "11": ("Угадай число", guess_number),
        "12": ("Перевернуть строку", string_reverser),
        "13": ("Числа Фибоначчи", fibonacci),
        "14": ("Калькулятор ИМТ", bmi_calculator),
        "15": ("Счетчик символов", text_counter),
        "16": ("Проверка анаграмм", anagram_checker),
        "17": ("Простой таймер", simple_timer),
        "18": ("День недели", day_of_week),
    }

    while True:
        print("\nВыберите программу:")
        for key, (name, _) in options.items():
            print(f"{key}. {name}")

        choice = input("Введите номер (или 'exit' для выхода): ")
        if choice.lower() == "exit":
            break
        elif choice in options:
            options[choice][1]()
        else:
            print("Неверный ввод, попробуйте снова.")

if __name__ == "__main__":
    main()
