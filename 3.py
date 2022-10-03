# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
number = int(input())
sum_of_total = 0
for i in range(1, number + 1):
    total = round((i + 1 / i ) ** i, 2)
    print(f'{i}: {total}')
    sum_of_total += total
print(f'Сумма: {sum_of_total}')