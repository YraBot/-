import keyboard
import time


def klava_spam():
    a = input("Введите клавишу для спама(если их несколько, разделяйте знаком +): ")
    b = int(input("Введите кол-во раз для спама: "))
    c = float(input("Введите задержку: "))
    d = float(input("Сколько нужно секунд подождать до спама? "))
    time.sleep(d)
    for i in range(int(b)):
        keyboard.press_and_release(a)
        keyboard.press_and_release('enter')
        time.sleep(c)

def both_spam():
    a = input("Введите текст спама: ")
    e = input("Введите клавишу для спама(если их несколько, разделяйте знаком +): ")
    b = int(input("Введите кол-во раз для спама: "))
    c = float(input("Введите задержку: "))
    d = float(input("Сколько нужно секунд подождать до спама? "))
    time.sleep(d)
    for i in range(int(b)):
        keyboard.write(a)
        keyboard.press_and_release(e)
        time.sleep(c)

def spam():
    a = input("Введите текст спама: ")
    b = int(input("Введите кол-во раз для спама: "))
    c = float(input("Введите задержку: "))
    d = float(input("Сколько нужно секунд подождать до спама? "))
    time.sleep(d)
    for i in range(int(b)):
        keyboard.write(a)
        keyboard.press_and_release('enter')
        time.sleep(c)

while True:
    print("")
    tip = int(input("Вы хотите спамить текстом(1),клавишами(2) или смешенное(3) "))
    if tip == 1:
        spam()
    elif tip == 3:
        both_spam()
    else:
        klava_spam()
