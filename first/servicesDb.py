from urllib3 import request
from .models import Test
from .models import Progress
import datetime


class DbData:
    # def proba(*kwargs):
    #     r = Test.objects.all()
    #     for data in r:
    #         data = data
    #     return data

    def getAll(*kwargs):
        object = Progress.objects.all()
        return object

    def updateUser(request):
        id = request.session.get('id_name')
        object = Progress.objects.filter(id=id)
        return object

    def deleteAll(request):
        object = Progress.objects.all()
        del request.session['id_name']
        object.delete()

    def createUser(request, name):
        object = Progress.objects.create(name=name, prize='none', count_zvezd=1, date=datetime.datetime.now())
        request.session['id_name'] = object.id
        return object