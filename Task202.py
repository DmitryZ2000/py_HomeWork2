# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

number = input("Введите целое положительное число: ")
while not number.isdigit():
    number = input("Введите целое положительное число: ") # Защита от ввода символов5
number = int(number)
mylist = [1]
for i in range(1, number):
    mylist.append(mylist[i-1] * (1+i))
print(mylist)