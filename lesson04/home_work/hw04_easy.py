# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

import random

numbers = [random.randint(-10, 10) for _ in range(4)]
print('numbers = ', numbers)

numbers_sq = [num**2 for num in numbers ]
print(numbers_sq)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

import random

alco_strong = ("Абсент", "Виски", "Текила", "Самбука")
alco_lite = ("Пиво", "Сидр", "Медовуха", "Шампанское", "Портвейн")

random_alco_strong = random.choice(alco_strong)
random_alco_lite = random.choice(alco_lite)

print("Ну какие фрукты, четверг - это маленькая пятница...","\n""Хочу быть в говно!")
print("Мой выбор:", random_alco_strong + "-" + random_alco_lite)

# Ладно, ладно...

import random

fruits_1 = ("Банан", "Манго", "Апельсин", "Киви")
fruits_2 = ("Слива", "Яблоко", "Груша", "Дыня", "Гранат")

random_fruit_1 = random.choice(fruits_1)
random_fruit_2 = random.choice(fruits_2)

print(random_fruit_1, random_fruit_2)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

import random

numbers = [random.randint(-10, 10) for _ in range(8)]

result = list(num for num in numbers if (num % 3 == 0 and num > 0 and num % 4 != 0) )

print(numbers)
print(result)
