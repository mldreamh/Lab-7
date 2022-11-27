import numpy as np 
import logging

logging.basicConfig(filename = "base_log.log", level=logging.INFO)

# Ввод данных полей
while True:
    k = int(input('Введите первое число по вертикали:')) - 1
    l = int(input('Введите первое число по горизонтали:')) - 1
    m = int(input('Введите второе число по вертикали:')) - 1
    n = int(input('Введите второе число по горизонтали:')) - 1
    if  0 > k or k > 8 or 0 > l or l > 8 or 0 > m or m > 8  or 0 > n or n > 8:
        print('Введите значение в каждом поле от 0 до 8')
        continue
    else:
        break

# Создание шахматного поля матричным способом (1 - черное, 0 - белое)
area = np.full((8, 8), 1)

for i in range(len(area)):
    for j in range(len(area[i])):
        if ((i + 1) % 2 == 0) and (j % 2 != 0):
            area[i][j] -= 1
        elif ((i + 1) % 2 != 0) and (j % 2 == 0):
            area[i][j] -= 1

# Вывод шахматного поля матричным способом
print('1 - черное поле, 0 - белое поле, 9 - поле (k, l), 8 - поле (m, n)')
area[7 - l][k] = 9
area[7 - n][m] = 8

print(area)

# Проверка 2-ух полей на сходимость цвета
if area[7-l][k] == area[7-n][m]:
    print('Поля имеют одинаковый цвет')
else:
    print('Поля имеют разные цвета')

# Проверка на угрозу поля (m, n)
name_list = ['ладья', 'конь', 'ферзь', 'слон']
while True:
    name_area = input('Укажите наименование фигуры для поля (k, l) (ладья, конь, ферзь или слон): ').lower()
    if name_area not in name_list:
        print('Введите правильное название фигуры (ладья, конь, ферзь или слон)')
        continue
    else:
        break

def queen(x0, y0, x1, y1):
    logging.info("Function call queen")
    x = x0
    y = y0

    if (y0 == y1) or (x0 == x1):
            return True
    elif y0 < y1:
        for i in range(y0, y1 + 1):
            x0 += 1
            y0 += 1
            if x0 == x1 and y0 == y1:
                return True
    elif y0 > y1:
        for i in range(y1, y0 + 1):
            x0 -= 1
            y0 -= 1
            if x0 == x1 and y0 == y1:
                return True
    x0 = x
    y0 = y
    if x0 < x1:
        for i in range(x0, x1 + 1):
            x0 += 1
            y0 -= 1
            if x0 == x1 and y0 == y1:
                return True
    elif x0 > x1:
        for i in range(x1, x0 + 1):
            x0 -= 1
            y0 += 1
            if x0 == x1 and y0 == y1:
                return True

def rook(x0, y0, x1, y1):
    logging.info("Function call rook")
    if (y0 == y1) or (x0 == x1):
            return True

def eleph(x0, y0, x1, y1):
    logging.info("Function call eleph")
    x = x0
    y = y0

    if y0 < y1:
        for i in range(y0, y1 + 1):
            x0 += 1
            y0 += 1
            if x0 == x1 and y0 == y1:
                return True
    elif y0 > y1:
        for i in range(y1, y0 + 1):
            x0 -= 1
            y0 -= 1
            if x0 == x1 and y0 == y1:
                return True
    x0 = x
    y0 = y
    if x0 < x1:
        for i in range(x0, x1 + 1):
            x0 += 1
            y0 -= 1
            if x0 == x1 and y0 == y1:
                return True
                break
    elif x0 > x1:
        for i in range(x1, x0 + 1):
            x0 -= 1
            y0 += 1
            if x0 == x1 and y0 == y1:
                return True

def horse(x0, y0, x1, y1):
    logging.info("Function call horse")
    if y0 + 2 == y1 and x0 - 1 == x1:
        return True
    elif y0 + 2 == y1 and x0 + 1 == x1:
        return True
    elif y0 - 2 == y1 and x0 - 1 == x1:
        return True
    elif y0 - 2 == y1 and x0 + 1 == x1:
        return True
    elif x0 + 2 == x1 and y0 + 1 == y1:
        return True
    elif x0 + 2 == x1 and y0 - 1 == y1:
        return True
    elif x0 - 2 == x1 and y0 + 1 == y1:
        return True
    elif x0 - 2 == x1 and y0 - 1 == y1:
        return True

# Проверка на угрозу
if name_area == 'ферзь':
    if queen(k, l, m, n):
        print('Угрожает полю (m, n)')
    else:
        print('Не угрожает полю (m, n)')
elif name_area == 'ладья':
    if rook(k, l, m, n):
        print('Угрожает полю (m, n)')
    else:
        print('Не угрожает полю (m, n)')
elif name_area == 'слон':
    if eleph(k, l, m, n):
        print('Угрожает полю (m, n)')
    else:
        print('Не угрожает полю (m, n)')
elif name_area == 'конь':
    if horse(k, l, m, n):
        print('Угрожает полю (m, n)')
    else:
        print('Не угрожает полю (m, n)')

def queen_move(x0, y0, x1, y1):
    logging.info("Function call queen_move")
    x0 = x1
    print('Первый ход: фигура перемещена на поле ({}, {})'.format(x0 + 1, y0 + 1))
    y0 = y1
    if x0 == x1 and y0 == y1:
        print('Фигура достигла поля (m, n)')
    else:
        print('Перемещение за один или два хода невозможно')

def rook_move(x0, y0, x1, y1):
    logging.info("Function call rook_move")
    x0 = x1
    print('Первый ход: фигура перемещена на поле ({}, {})'.format(x0 + 1, y0 + 1))
    y0 = y1
    if x0 == x1 and y0 == y1:
        print('Фигура достигла поля (m, n)')
    else:
        print('Перемещение за один или два хода невозможно')

def eleph_move(x0, y0, x1, y1):
    logging.info("Function call eleph_move")
    for i in range(8):
        x0 -= 1
        y0 += 1
        x = x0
        y = y0
        for n in range(8):
            x -= 1
            y -= 1
            if x == x1 and y == y1:
                print('Первый ход: фигура перемещена на поле ({}, {})'.format(x0 + 1, y0 + 1))
                print('Фигура достигла поля (m, n)')
                return 0
    x0 = k
    y0 = l
    for i in range(8):
        x0 -= 1
        y0 += 1
        x = x0
        y = y0
        for n in range(8):
            x += 1
            y += 1
            if x == x1 and y == y1:
                print('Первый ход: фигура перемещена на поле ({}, {})'.format(x0 + 1, y0 + 1))
                print('Фигура достигла поля (m, n)')
                return 0
    x0 = k
    y0 = l
    for i in range(8):
        x0 -= 1
        y0 -= 1
        x = x0
        y = y0
        for n in range(8):
            x -= 1
            y += 1
            if x == x1 and y == y1:
                print('Первый ход: фигура перемещена на поле ({}, {})'.format(x0 + 1, y0 + 1))
                print('Фигура достигла поля (m, n)')
                return 0
    x0 = k
    y0 = l
    for i in range(8):
        x0 -= 1
        y0 -= 1
        x = x0
        y = y0
        for n in range(8):
            x += 1
            y -= 1
            if x == x1 and y == y1:
                print('Первый ход: фигура перемещена на поле ({}, {})'.format(x0 + 1, y0 + 1))
                print('Фигура достигла поля (m, n)')
                return 0
    x0 = k
    y0 = l
    for i in range(8):
        x0 += 1
        y0 -= 1
        x = x0
        y = y0
        for n in range(8):
            x -= 1
            y -= 1
            if x == x1 and y == y1:
                print('Первый ход: фигура перемещена на поле ({}, {})'.format(x0 + 1, y0 + 1))
                print('Фигура достигла поля (m, n)')
                return 0
    x0 = k
    y0 = l
    for i in range(8):
        x0 += 1
        y0 -= 1
        x = x0
        y = y0
        for n in range(8):
            x += 1
            y += 1
            if x == x1 and y == y1:
                print('Первый ход: фигура перемещена на поле ({}, {})'.format(x0 + 1, y0 + 1))
                print('Фигура достигла поля (m, n)')
                return 0
    x0 = k
    y0 = l
    for i in range(8):
        x0 += 1
        y0 += 1
        x = x0
        y = y0
        for n in range(8):
            x -= 1
            y += 1
            if x == x1 and y == y1:
                print('Первый ход: фигура перемещена на поле ({}, {})'.format(x0 + 1, y0 + 1))
                print('Фигура достигла поля (m, n)')
                return 0
    x0 = k
    y0 = l
    for i in range(8):
        x0 += 1
        y0 += 1
        x = x0
        y = y0
        for n in range(8):
            x += 1
            y -= 1
            if x == x1 and y == y1:
                print('Первый ход: фигура перемещена на поле ({}, {})'.format(x0 + 1, y0 + 1))
                print('Фигура достигла поля (m, n)')
                return 0
    x0 = k
    y0 = l
        
# Проверка на перемещение на поле (m, n) за один ход или же за два
if name_area == 'ферзь':
    if queen(k, l, m, n):
        print('Можно попасть одним ходом на поле (m, n)')
    else:
        queen_move(k, l, m, n)
elif name_area == 'ладья':
    if rook(k, l, m, n):
        print('Можно попасть одним ходом на поле (m, n)')
    else:
        rook_move(k, l, m, n)
elif name_area == 'слон':
    if eleph(k, l, m, n):
        print('Можно попасть одним ходом на поле (m, n)')
    else:
        eleph_move(k, l, m, n)
    
