#Ввести с клавиатуры строку.
#Вывести эту же строку вертикально: по одному символу на строку консоли.
import itertools

list_1 = [11, 12, 51, 66, 74, 342, 2222, 523, 0, 9]
for x in list_1:
    x += 1
    print (x, end=',') 
print ('')

str_1 = str(input('Введите слово: '))
for i in str_1:
    print (i)

#Создать список из словарей с оценками учеников разных классов школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
#Посчитать и вывести средний балл по всей школе.
#Посчитать и вывести средний балл по каждому классу.

student = [{'school_class': '666F', 'progress': [5, 4, 2, 5, 3]},
{'school_class': '5D', 'progress': [3, 2, 3, 4, 3]},
{'school_class': '7E', 'progress': [2, 2, 2, 4, 5]},
{'school_class': '2G', 'progress': [5, 4, 4, 5, 5]}]

score = 0
summ = 0
for dicts in student:
    a = dicts.get('progress')
    b = dicts.get('school_class') 
    c = sum(a)/len(a)
    print(f'средний балл по классу {b} - {c}')
    summ1 = 0
    for  mark in a:
        summ1 += mark
    score += summ1  #сумма оценок по школе
    for progr in a:
        summ +=1     # кол-во оценок по школе
print(f'средний балл по школе - {float(score/summ)}') 


'''
sum = 0
sum1 = 0
sum2 = 0
sum3 = 0
sum4 = 0

q = student[0]['progress']
w = student[1]['progress']
e = student[2]['progress']
t = student[3]['progress']

h = list(q + w + e + t)

for a in h:
    sum+=a
    b = len(h)
print ('средний бал по школе', '-', sum/b)

for y in q:
    sum1+=y
    b1 = len(q)
print ('средний бал по классу', student[0]['school_class'], '-', sum1/b1)

for r in w:
    sum2+=r
    b2 = len(w)
print ('средний бал по классу', student[1]['school_class'], '-', sum2/b2)

for u in e:
    sum3+=u
    b3 = len(e)
print ('средний бал по классу', student[2]['school_class'], '-', sum3/b3)

for k in t:
    sum4+=k
    b4 = len(t)
print ('средний бал по классу', student[3]['school_class'], '-', sum4/b4)
'''
