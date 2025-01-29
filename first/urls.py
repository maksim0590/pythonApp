from tkinter.font import names

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('welcome', views.welcome, name='welcome'),
    path('gogames', views.gogames, name='gogames'),
    path('gogamesshow', views.gogamesShow, name='gogamesshow'),
    path('mainuser', views.mainuser, name='mainuser'),
    path('mainusershow', views.mainuserShow, name='mainusershow'),
    path('tasks', views.tasks, name='task'),
    path('status/<str:day>/', views.status, name='status'),
    path('delete', views.delete, name='delete'),
    path('test', views.test, name='test'),
    path('test2', views.test2, name='test2'),

]