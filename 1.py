# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
numbers = input("Введите вещественное число: ")
sum_numbers = 0
for i in numbers:
    # берем в расчет только цифры
    if i.isdigit():
        sum_numbers += int(i)
print(sum_numbers)