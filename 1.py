# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
number = input("Введите вещественное число: ")
total = 0
for i in number:
    if i.isdigit():
        total += int(i)
print(total)