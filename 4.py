# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
number = int(input("Введите число: "))
# создание списка, который будет заполняться числами от -n До n
list = []
# начальное значение произведения
product = 1
for i in range(- number, number + 1):
    list.append(i)
print(list)
# считываем индексы из файла
path = 'file.txt'
index = open(path, 'r')
for line in index:
    product *= list[int(line)]
index.close()
print(f'Произведение чисел по индексам в файле file.txt: {product}')