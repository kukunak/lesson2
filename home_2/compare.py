#Написать функцию, которая принимает на вход две строки
#Проверить, является ли то, что передано функции, строками. Если нет - вернуть 0
#Если строки одинаковые, вернуть 1
#Если строки разные и первая длиннее, вернуть 2
#Если строки разные и вторая строка 'learn', возвращает 3
#Вызвать функцию несколько раз, передавая ей разные праметры и выводя на экран результаты

def func(line1, line2):  
    if type(line1) != str or type(line2) != str:      
        return 0 
    elif line1 == line2:
        return 1
    elif line1 != line2 and len(line1) > len(line2) and line2 != 'learn':
        return 2
    elif line1 != line2 and line2 == 'learn':
        return 3
    
    
print(func('call', 45))
print(func(4.55, 'dog'))
print(func('why me', 'hot'))
print(func('join', 'learn'))
print(func('try', 'python'))
print(func('python', 'python'))
print(func('123456', 'learn'))
print(func('learn', 'learn'))
print(func('12345', 'еearn')) # если в 11 строчке поставить len, тогда здесь на выходе 
# будет 1, но содержимое строк разное, а так выведет None