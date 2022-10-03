# Реализуйте алгоритм перемешивания списка.
import random
 
# оригинальный список
original_list = [random.randint(0,10) for i in range(random.randint(3,10))]
print(f'Оригинальный список: {original_list}')

#перемешивание (меняем местами, начиная с крайнего элемента)
for i in range(len(original_list) - 1, 0, - 1):
    j = random.randint(0, i + 1)
    original_list[i], original_list[j] = original_list[j], original_list[i]

print (f'Перемешанный список: {original_list}')

