# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
number = int(input("Введите число: "))
total = 1
list_of_total = []
for i in range(1, number + 1):
    total *= i
    list_of_total.append(total)
print(list_of_total)