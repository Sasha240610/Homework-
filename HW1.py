###################################
# Задача 1.
# Написати програму, в якій випадковим чином створюється число в діапазоні від 1 до 10.
# Користувач намагається вгадати число. Програма може давати підказки тільки "More", "Less", "You won!".
# Приклад:
# Програма створила число 3.
# Програма пропонує вгадати число. Користувач вводить 5. Програма пише "Less".
# Програма пропонує вгадати число. Користувач вводить 1. Програма пише "More".
# Програма пропонує вгадати число. Користувач вводить 2. Програма пише "More".
# Програма пропонує вгадати число. Користувач вводить 3. Програма пише "You won!".
# Програма завершується.

import random

number = random.randint(1, 10)
print("Програма створила число. Спробуйте його вгадати!")
while True:
    try:
        guess = int(input("Ваш варіант: "))
        if guess < number:
            print("More")
        elif guess > number:
            print("Less")
        else:
            print("You won!")
            break
    except ValueError:
        print("Введіть коректне число!")

###################################

# Задача 2.
# Написати програму, в якій випадковим чином створюється число в діапазоні від 1 до 12.
# Програма виводить на екран число, яке створено, і назву місяця, який відповідає цьому числу.
# Приклад:
# Програма створила число 3.
# На екран виводиться повідомлення: "3 - March".
# Програма завершується.

import random

months = [
    "January", "February", "March", "April", "May", "June", 
    "July", "August", "September", "October", "November", "December"
]

number = random.randint(1, 12)
print(f"{number} - {months[number - 1]}")

###################################

# Задача 3.
# Написати програму, в якій користувач вводить два цілих числа.
# Програма виводить результат піднесення першого числа у степінь, відповідний другому числу.
# Зробити обробку всіх можливих помилок.
# В разі неможливості виконання дії - вивести відповідне повідомлення. ("Введено не число", тощо ... )
# Приклад:
# Користувач вводить число 2.
# Користувач вводить число 5.
# На екран виводиться число 32.
# Програма завершується.

try:
    base = int(input("Введіть основу (ціле число): "))
    exponent = int(input("Введіть показник степеня (ціле число): "))
    result = base ** exponent
    print(f"Результат: {result}")
except ValueError:
    print("Введено не число. Будь ласка, спробуйте ще раз.")
except Exception as e:
    print(f"Сталася помилка: {e}")
