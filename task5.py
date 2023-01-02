# 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

def result(xa, xb, ya, yb):
    import math
    distance = math.sqrt(((xb - xa) **2) + ((yb-ya)**2))
    print(f'Расстояние между {xa, ya} и {xb, yb}: {round(distance, 2)}')

xa = float(input('Введите координату x для точки А: '))
xb = float(input('Введите координату x для точки B: '))

ya = float( input('Введите координату y для точки А: '))
yb = float( input('Введите координату y для точки B: '))

result(xa, xb, ya, yb)