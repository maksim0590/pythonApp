from dbm import error
from lib2to3.fixes.fix_input import context
from turtle import TurtleGraphicsError
from .forms import TestForms
from .services import sendMessage
from .models import Progress
from django.shortcuts import render, redirect
import datetime
import sys
# from .servicesDb import proba
# from .servicesDb import deleteAll

from .servicesDb import DbData


def index(request):
    return render(request, 'first/index.html')

def welcome(request):
    return render(request, 'first/welcome_pg.html')

def mainuser(request):
    name = request.POST.get('name')
    mes = Progress.objects.filter(name__contains=name)
    if mes:
        for i in mes:
            id = i
        name = Progress.objects.get(name=i)
        id_user = name.id
        user = Progress.objects.get(id=id_user)
        count = user.count_zvezd
        data = datetime.datetime.now()
        dayWeek = data.weekday()
        return render(request, "first/tasks.html", context={'count': count, 'user':user, 'dayWeek':dayWeek})

    else:
        info = Progress.objects.create(name=name, prize='none', count_zvezd=1, date=datetime.datetime.now())
        request.session['id_name'] = info.id
        return redirect('mainusershow')
def mainuserShow(request):
    id = request.session.get('id_name')
    user = Progress.objects.get(id=id)
    count = user.count_zvezd
    name = user.name
    return render(request, 'first/main.html', context={'name': name, 'count': count})


def gogames(request):
    prize = request.POST.get('prize')
    id = request.session.get('id_name')
    save_prize = Progress.objects.get(id=id)
    save_prize.prize = prize
    save_prize.count_zvezd +=1
    count = save_prize.count_zvezd
    save_prize.save(update_fields=["prize", 'count_zvezd'])
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
    DbData.deleteAll()
    del request.session['id_name']
    return redirect('index')



#_________________________________________________________________________

def test(request):
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