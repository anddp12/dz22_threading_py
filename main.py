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
    return numbers

print(task1())

def task2(): # функция для вычисления суммы чисел в списке
    global numbers
    s = sum(numbers)
    return s

print (task2())

def task3(): # функция для вычисления среднеарифметического чисел в списке
    global numbers
    s = sum(numbers)
    a = s/len(numbers)
    return a

print (task3())