#Напишите функцию ask_user(), которая с помощью input() спрашивает пользователя “Как дела?”, пока он не ответит “Хорошо”
#Создайте словарь типа "вопрос": "ответ", например: {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
#Доработайте ask_user() так, чтобы когда пользователь вводил вопрос который есть в словаре, программа давала ему соотвествующий ответ. Например:
#Пользователь: Что делаешь?
#Программа: Программирую
def ask_user():
    while True:
        dict_1 = {'У тебя есть планы на завтра?': 'да, спать',
        "Хочешь есть ?": 'Я сыт, спасибо'}
        question = str(input('Как дела? '))
        if question == "Хорошо":
            print('Это радует =)')
            pass
            for key in dict_1:
                a = str(input('User: '))
                #print ()
                if key == a:
                    print ('\nbot: %s' % (dict_1[key]))
                    break
                else:
                    print('Научись задавать правильные вопросы')
            break
        else:
            print(f'Твой ответ {question} меня не устраивает')
ask_user()

    
