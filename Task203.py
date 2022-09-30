# Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.
# Пример: Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

number = input("Введите целое положительное число: ")
while not number.isdigit():
    number = input("Введите целое положительное число: ") # Защита от ввода символов

number = int(number)
my_dic = {}
for key in range(number):
    for i in range(1,number):
        rezult = int((1+1/i)**i)
        my_dic[key] = [rezult]
print(my_dic)   
