day = int(input('введите день недели от 1 до 7: '))

while day > 7 or day < 1:
    print('Такого дня недели не существует')
    break
if day == 6 or day == 7:
    print('Это выходной день')
else:
    print('Это рабочий день')

