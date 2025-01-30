import random

count = 0
while True:
    a = random.randint(1, 10 )
    b = random.randint(1, 10 )
    list = [a, b]
    operations = sum(list)
    rezult = input(f'Сложите числа: {a}+{b}=')
    if operations == int(rezult):
        count +=1
        print(f'ВЕРНО! \n У тебя на счету {count} звезд')
    else:
        print(f'Ответ неверный \n Подумай еще')
        while True:
            rezult = input(f'Сложите числа: {a}+{b}=')
            if operations == int(rezult):
                print(f'ВЕРНО! \n У тебя на счету {count} звезд')
                count += 1
                print(count)
                break
            else:
                print(f'Ответ неверный \n Подумай еще')