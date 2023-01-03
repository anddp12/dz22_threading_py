import threading
from random import randint 

# Завдання 1
# При старті додатку запускаються три потоки. Перший потік заповнює список випадковими числами. 
# Два інші потоки очікують на заповнення. Коли перелік заповнений, обидва потоки запускаються. 
# Перший потік знаходить суму елементів списку, другий потік знаходить середнє арифметичне значення у списку. 
# Отриманий список, сума та середнє арифметичне виводяться на екран. 

numbers = []

def task1(): # функция для наполнения списка случайными числами
    global numbers
    for i in range(10):
        numbers.append(randint(1, 100))
    print(numbers)
    return numbers

def task2(): # функция для вычисления суммы чисел в списке
    global numbers
    s = sum(numbers)
    print(s)
    return s

def task3(): # функция для вычисления среднеарифметического чисел в списке
    global numbers
    s = sum(numbers)
    a = s/len(numbers)
    print(a)
    return a


th1 = threading.Thread(target=task1) # создаем первый поток
th2 = threading.Thread(target=task2) # создаем второй поток
th3 = threading.Thread(target=task3) # создаем третий поток

th1.start() # старт первого потока
th1.join() # ожидание завершения первого потока

th2.start() # старт второго потока
th3.start() # старт третьего потока

th2.join() # ожидание завершения второго потока
th3.join() # ожидание завершения третьего потока