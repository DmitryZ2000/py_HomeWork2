# Реализуйте алгоритм перемешивания списка.
import random

my_list = list(range(10))
print(my_list)
mix_list = random.sample(my_list, len(my_list))
print(mix_list)