# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
number = int(input())
list = []
product = 1
for i in range(- number, number + 1):
    list.append(i)
print(list)
path = 'file.txt'
coords = open(path, 'r')
for line in coords:
    product *= list[int(line)]
coords.close()
print(product)