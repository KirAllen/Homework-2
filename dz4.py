# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

n = int(input())
lst = []
sum = 1

for i in range (-n, n+1):
    lst.append(i)
print(lst)

path = "file.txt"
data = open(path, "r")
for j in data:
    sum *= (lst[int(j)])
data.close()
print(sum)
exit()