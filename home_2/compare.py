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
    elif line1 !=line2 and len(line1) > len(line2):
        return 2
    elif line1 !=line2 and line2 == 'learn':
        return 3
    
    
print(func('call', 45))
print(func(4.55, 'dog'))
print(func('why me', 'hot'))
print(func('join', 'learn'))
print(func('try', 'python'))
print(func('python', 'python'))