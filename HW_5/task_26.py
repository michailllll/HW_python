# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
a = int(input("Введите основание степени  "))
b = int(input("Введите показатель степени  "))

def step(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    return step(a, b-1) * a
    

result = step(a, b)
print(result)
