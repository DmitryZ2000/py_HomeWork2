# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.
n = 9
my_list = list(range(-n, n+1))
print(my_list)
path = "myfile.txt"
data = open(path, "r")
rez = 1
for i in data:
    rez *=my_list[int(i)]
data.close()
print(rez)

