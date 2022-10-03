# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
number = float(input("Введите вещественное число: "))
str_number = str(number)
total = 0
for i in str_number:
    if i.isdigit():
        total += int(i)
print(total)