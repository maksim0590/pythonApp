from dbm import error
from lib2to3.fixes.fix_input import context
from turtle import TurtleGraphicsError

from pyexpat.errors import messages
from django.http import HttpResponse
from .forms import TestForms
from .services import sendMessage
from .models import Progress
from django.shortcuts import render, redirect
import datetime
import sys
from .servicesDb import DbData
import random
from .models import Calcul

def index(request):
    return render(request, 'first/index.html')

def welcome(request):
    return render(request, 'first/welcome_pg.html')

def mainuser(request):
    nameFromInput = request.POST.get('name')
    nameDbObject = Progress.objects.get(name=nameFromInput)
    if nameDbObject:
        return redirect('task')

        # return render(request, "first/tasks.html", context={'count': nameDbObject.count_zvezd, 'user':nameDbObject.name, 'dayWeek':dayWeek})
#     else:
#         objectUser = Progress.objects.create(name=nameDbObject, prize='none', count_zvezd=1, date=datetime.datetime.now())
#         request.session['id_name'] = objectUser.id
#         object = Calcul.objects.create(number1=0, number2=0, number3=0, rezult=0, rezultUser=0)
#         return redirect('mainusershow')
def mainuserShow(request):
    id = request.session.get('id_name')
    user = Progress.objects.get(id=id)
    count = user.count_zvezd
    name = user.name
    return render(request, 'first/main.html', context={'name': name, 'count': count, 'session':id})


def gogames(request):
    prize = request.POST.get('prize')
    id = request.session.get('id_name')
    save_prize = Progress.objects.get(id=id)
    save_prize.prize = prize
    save_prize.count_zvezd +=1
    count = save_prize.count_zvezd
    save_prize.save()
    return redirect('gogamesshow')
def gogamesShow(request):
    id = request.session.get('id_name')
    user = Progress.objects.get(id=id)
    count = user.count_zvezd
    prize = user.prize
    message = f'{user.name} приступила к выполнению заданий  \nВ качестве вознаграждения хочет получить: {user.prize} '
    sendMessage(message)
    return render(request, "first/gogames.html", context={ 'prize':prize, 'count':count})


def tasks(request):
    id = request.session.get('id_name')
    user = Progress.objects.get(id=id)
    count = user.count_zvezd
    data = datetime.datetime.now()
    dayWeek = data.weekday()
    return render(request, "first/tasks.html", context={'count':count, 'user':user, 'dayWeek':dayWeek})
def status(request, day):
    id = request.session.get('id_name')
    user = Progress.objects.get(id=id)
    setattr(user, day, True)
    user.count_zvezd += 1
    user.save()
    if day[:-3] == 'teeth':
        task = 'Почитсить зубы'
    elif day[:-3] == 'hair':
        task = 'Расчесать волосы'
    elif day[:-3] == 'makeBed':
        task = 'Заправить постель'
    elif day[:-3] == 'washShoes':
        task = 'Помыть обувь'
    elif day[:-3] == 'lessons':
        task = 'Сделать уроки'
    elif day[:-3] == 'briefcase':
        task = 'Собрать портфель'
    elif day[:-3] == 'feedTheCat':
        task = 'Покормить кошку'
    elif day[:-3] == 'tePlay':
        task = 'Поиграть с Варей'
    elif day[:-3] == 'removeTable':
        task = 'Помыть посуду/убрать со стола'
    sendMessage(f'Пользователь: **{user.name}** \n Выполнил задание: **{task}** \n На счету у пользователя:**{user.count_zvezd}** звезд')
    return redirect('task')
def delete(request):
    DbData.deleteAll(request=request)
    return redirect('index')



def bonus(request):
    global object
    title = 'Реши пример'

    rezult_input = request.POST.get('rezult')
    if rezult_input == None:
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        c = a + b
        object = Calcul.objects.create(number1=a, number2=b, number3=0, rezult=c,  count_zvezd=0)
        request.session['id'] = object.id
        object.save()
        return render(request, 'first/bonus_task.html',
                      {'name': 0, 'title': title, 'a': object.number1, 'b': object.number2,
                       'id': object.id})

    else:
        id = request.session.get('id')
        object = Calcul.objects.get(id=id)
        object.rezultUser = int(rezult_input)
        object.save()
        if object.rezult == object.rezultUser:
            message_correct = 'Верно'
            zvezd = object.count_zvezd + 1
            object.save()

            rezult_input = request.POST.get('rezult')
            rezultUser = int(rezult_input)
            a = random.randint(1, 10)
            b = random.randint(1, 10)
            c = a + b
            object = Calcul.objects.create(number1=a, number2=b, number3=0, rezult=c, rezultUser=rezultUser,
                                           count_zvezd=zvezd)
            request.session['id'] = object.id
            object.save()

            if object.count_zvezd >= 16:
                message_endplay = 'Ты справилась!!'
                id = request.session.get('id_name')
                objectUser = Progress.objects.get(id=id)
                objectUser.count_zvezd += 10
                objectUser.save()
                return render(request, 'first/bonus_task.html',
                          {'count': object.count_zvezd, 'title': title, 'a': object.number1,
                           'b': object.number2,
                           'id': object.id, 'message_correct': message_correct, 'message_endplay':message_endplay})

            return render(request, 'first/bonus_task.html',
                          {'count': object.count_zvezd, 'title': title, 'a': object.number1,
                           'b': object.number2,
                           'id': object.id, 'message_correct': message_correct})
        else:
            message_error = 'Не верно'
            id = request.session.get('id')
            object = Calcul.objects.get(id=id)
            if object.count_zvezd < 0:
                message_minus = 'Подумай хорошо'
                return render(request, 'first/bonus_task.html',
                              {'count': object.count_zvezd, 'message_minus': message_minus, 'title': title,
                               'a': object.number1, 'b': object.number2,
                               'id': object.id, 'message_error': message_error})
            else:
                object.count_zvezd -= 1
                object.save()
                return render(request, 'first/bonus_task.html',
                              {'count': object.count_zvezd, 'title': title, 'a': object.number1, 'b': object.number2,
                               'id': object.id, 'message_error': message_error})


def exitplay(request):
    object = Calcul.objects.all()
    object.delete()
    del request.session['id']
    return redirect('task')



















#_________________________________________________________________________

def testForm(request):
    error = ''
    if request.method == 'POST':
        form = TestForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('test2')
        else:
            error = 'Форма заполнена не верно'
    form = TestForms()
    data = {
        'form':form,
        'error':error
    }
    return render(request, 'first/test.html', context=data )

def test2(request):
    r= DbData.proba()
    return render(request, 'first/test2.html', context={'r':r})