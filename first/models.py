from django.db import models


class Progress(models.Model):
    name = models.CharField('Имя', max_length=50)
    prize = models.CharField('Приз', max_length=250)
    count_zvezd = models.IntegerField('Количество звезд')

    teethMon = models.BooleanField('Чистка зубов в понедельник',default=False)
    teethTue = models.BooleanField('Чистка зубов во вторник', default=False)
    teethWed = models.BooleanField('Чистка зубов в среду', default=False)
    teethThu = models.BooleanField('Чистка зубов в четверг', default=False)
    teethFri = models.BooleanField('Чистка зубов в пятницу', default=False)
    teethSat = models.BooleanField('Чистка зубов в субботу', default=False)
    teethSun = models.BooleanField('Чистка зубов в воскр', default=False)

    hairMon = models.BooleanField('Расчесать волосы в понедельник', default=False)
    hairTue = models.BooleanField('Расчесать волосы во вторник', default=False)
    hairWed = models.BooleanField('Расчесать волосы в среду', default=False)
    hairThu = models.BooleanField('Расчесать волосы в четверг', default=False)
    hairFri = models.BooleanField('Расчесать волосы в пятницу', default=False)
    hairSat = models.BooleanField('Расчесать волосы в субботу', default=False)
    hairSun = models.BooleanField('Расчесать волосы в воскр', default=False)

    makeBedMon = models.BooleanField('Заправить постель в понедельник', default=False)
    makeBedTue = models.BooleanField('Заправить постель во вторник', default=False)
    makeBedWed = models.BooleanField('Заправить постель в среду', default=False)
    makeBedThu = models.BooleanField('Заправить постель в четверг', default=False)
    makeBedFri = models.BooleanField('Заправить постель в пятницу', default=False)
    makeBedSat = models.BooleanField('Заправить постель в субботу', default=False)
    makeBedSun = models.BooleanField('Заправить постель в воскр', default=False)

    washShoesMon = models.BooleanField('Помыть обувь в понедельник', default=False)
    washShoesTue = models.BooleanField('Помыть обувь во вторник', default=False)
    washShoesWed = models.BooleanField('Помыть обувь в среду', default=False)
    washShoesThu = models.BooleanField('Помыть обувь в четверг', default=False)
    washShoesFri = models.BooleanField('Помыть обувь в пятницу', default=False)
    washShoesSat = models.BooleanField('Помыть обувь в субботу', default=False)
    washShoesSun = models.BooleanField('Помыть обувь в воскр', default=False)

    lessonsMon = models.BooleanField('Уроки в понедельник', default=False)
    lessonsTue = models.BooleanField('Уроки во вторник', default=False)
    lessonsWed = models.BooleanField('Уроки в среду', default=False)
    lessonsThu = models.BooleanField('Уроки в четверг', default=False)
    lessonsFri = models.BooleanField('Уроки в пятницу', default=False)
    lessonsSat = models.BooleanField('Уроки в субботу', default=False)
    lessonsSun = models.BooleanField('Уроки в воскр', default=False)

    briefcaseMon = models.BooleanField('Собрать портфель в понедельник', default=False)
    briefcaseTue = models.BooleanField('Собрать портфель во вторник', default=False)
    briefcaseWed = models.BooleanField('Собрать портфель в среду', default=False)
    briefcaseThu = models.BooleanField('Собрать портфельв четверг', default=False)
    briefcaseFri = models.BooleanField('Собрать портфель в пятницу', default=False)
    briefcaseSat = models.BooleanField('Собрать портфель в субботу', default=False)
    briefcaseSun = models.BooleanField('Собрать портфель в воскр', default=False)

    feedTheCatMon = models.BooleanField('Покормить кошку в понедельник', default=False)
    feedTheCatTue = models.BooleanField('Покормить кошку во вторник', default=False)
    feedTheCatWed = models.BooleanField('Покормить кошку в среду', default=False)
    feedTheCatThu = models.BooleanField('Покормить кошку в четверг', default=False)
    feedTheCatFri = models.BooleanField('Покормить кошку в пятницу', default=False)
    feedTheCatSat = models.BooleanField('Покормить кошку в субботу', default=False)
    feedTheCatSun = models.BooleanField('Покормить кошку в воскр', default=False)

    tePlayMon = models.BooleanField('Поиграть с сестрой в понедельник', default=False)
    tePlayTue = models.BooleanField('Поиграть с сестрой во вторник', default=False)
    tePlayWed = models.BooleanField('Поиграть с сестрой в среду', default=False)
    tePlayThu = models.BooleanField('Поиграть с сестрой в четверг', default=False)
    tePlayFri = models.BooleanField('Поиграть с сестрой в пятницу', default=False)
    tePlaySat = models.BooleanField('Поиграть с сестрой в субботу', default=False)
    tePlaySun = models.BooleanField('Поиграть с сестрой в воскр', default=False)

    removeTableMon = models.BooleanField('Убрать со стола в понедельник', default=False)
    removeTableTue = models.BooleanField('ПоУбрать со стола во вторник', default=False)
    removeTableWed = models.BooleanField('Убрать со стола в среду', default=False)
    removeTableThu = models.BooleanField('Убрать со стола в четверг', default=False)
    removeTableFri = models.BooleanField('Убрать со стола в пятницу', default=False)
    removeTableSat = models.BooleanField('Убрать со стола в субботу', default=False)
    removeTableSun = models.BooleanField('Убрать со стола в воскр', default=False)

    date = models.DateTimeField('Дата')


    def __str__(self):
        return self.name

class Test(models.Model):
    name = models.CharField('Имя', max_length=50)
    age = models.CharField('Возраст', max_length=250)
    text = models.CharField('Текст', max_length=250)

    def __str__(self):
        return self.name

class Calcul(models.Model):
    number1 = models.IntegerField('Первое значение')
    number2 = models.IntegerField('Второе значение')
    number3 = models.IntegerField('Третье значение')
    rezult = models.IntegerField('Результат')
    rezultUser = models.IntegerField('Результат пользователя')

