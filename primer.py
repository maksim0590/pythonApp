import operator
import random
while True:
    a = random.randint(1, 10 )
    b = random.randint(1, 10 )
    list = [a, b]
    operations = sum(list)

    rezult = input(f'Сложите числа: {a}+{b}=')

    if operations == int(rezult):
        print('ВЕРНО')
    else:
        print('Ответ неверный')