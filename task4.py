# 4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
# *Пример:*

# - 1 -> x > 0, y > 0
# - 8 -> нет такой четверти

def plane(num):
    print(f'вы указали {num}-й номер четверти') 
    
    for el in diapason:
      if(num-1)==int(diapason.index(el)):
        print(f'возможный диапазон: {el}')


num = int(input("Укажите четверть системы координат (от 1 до 4): "))

if  num<=0 or num>=5:
  print('Надо ввести: от 1 до 4')
  #stop # не срабатывает

diapason = [
'(0 до +∞ и от 0 до +∞)',
'(0 до -∞ и от 0 до +∞)',
'(0 до -∞ и от 0 до -∞)',
'(0 до +∞ и от 0 до -∞)']

plane(num)