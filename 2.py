# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
number = int(input("Введите число: "))
product = 1
list = []
for i in range(1, number + 1):
    product *= i
    list.append(product)
print(list)