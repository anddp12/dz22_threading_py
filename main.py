import threading
from random import randint

# Завдання 1
# При старті додатку запускаються три потоки. Перший потік заповнює список випадковими числами. 
# Два інші потоки очікують на заповнення. Коли перелік заповнений, обидва потоки запускаються. 
# Перший потік знаходить суму елементів списку, другий потік знаходить середнє арифметичне значення у списку. 
# Отриманий список, сума та середнє арифметичне виводяться на екран. 

l1 = threading.Lock()

numbers = []

def task1(): # функция для наполнения списка случайными числами
    global l1
    l1.acquire()
    print("start 1")
    global numbers
    for i in range(10):
        numbers.append(randint(1, 100))
    print(f'Список из случайный чисел - {numbers}')
    l1.release()
    return numbers


def task2(): # функция для вычисления суммы чисел в списке
    global l1
    while l1.locked():
        pass
    print("start 2")
    global numbers
    s = sum(numbers)
    print(f'Сумма чисел из списка - {s}')
    return s

def task3(): # функция для вычисления среднеарифметического чисел в списке
    global l1
    while l1.locked():
        pass
    print("start 3")
    global numbers
    s = sum(numbers)
    a = s/len(numbers)
    print(f'Среднеарифметического чисел в списке - {a}')
    return a


th1 = threading.Thread(target=task1) # создаем первый поток
th2 = threading.Thread(target=task2) # создаем второй поток
th3 = threading.Thread(target=task3) # создаем третий поток

th1.start() # старт первого потока
th1.join() # ожидание завершения потока

th2.start() # старт второго потока
th3.start() # старт третьего потока

# th2.join() # ожидание завершения потока
# th3.join() # ожидание завершения потока