# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
num = input()
result = 0
for i in num:
    if i.isdigit():
        result += int(i)
print(result)