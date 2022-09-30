# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

number = -12345.6789
print(number)
number_string = str(abs(number))
my_sum = 0
for i in number_string:
    if i != "." : 
        my_sum += int(i)
print(my_sum)