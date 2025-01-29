from urllib3 import request

from .models import Test
from .models import Progress

class DbData:
    # def proba(*kwargs):
    #     r = Test.objects.all()
    #     for data in r:
    #         data = data
    #     return data

    def getAll(*kwargs):
        object = Progress.objects.all()
        return object

    def getUser(id):
        objectUser = Progress.objects.filter(id=id)
        return objectUser

    def deleteAll(*kwargs):
        object = Progress.objects.all()
        object.delete()
