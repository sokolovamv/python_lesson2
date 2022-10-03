# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
number = int(input())
sum = 0
for i in range(1, number + 1):
    total = round((i + 1 / i ) ** i, 2)
    print(f'{i}: {total}')
    sum += total
print(f'Сумма: {sum}')