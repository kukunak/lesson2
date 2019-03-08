#Перепишите функцию ask_user() из задания про while, 
#чтобы она перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
#и завершала работу при помощи оператора break

a = 7
def ask_user():
    while True:
        try:
            if len(input('Как дела? ')) < a:
                print ('мало букв')
            else:
                print('меня не остановить, попробуй ctrl+C')
                continue
        except KeyboardInterrupt:
            print('\nПока')
            break

ask_user()
