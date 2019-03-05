#Напишите функцию get_summ(num_one, num_two), 
#которая принимает на вход два целых числа (int) и складывает их
#Оба аргумента нужно приводить к целому числу при помощи int() и 
#перехватывать исключение ValueError если приведение типов 
#не сработало

def get_summ(num_one, num_two):     
    while True:
        try:
            num_one = int(num_one)
            num_two = int(num_two)
            return num_one + num_two
        except ValueError:
            print('должно быть целое число...')
            break
    
p = get_summ(3, 4)
print(p)

p = get_summ(3.343, 6.44)
print(p)

p = get_summ('f', 'df')
print(p)

