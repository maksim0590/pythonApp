from.models import Test
from django.forms import ModelForm, TextInput


class TestForms(ModelForm): # название класса произвольное
    class Meta:
        model = Test
        fields = ['name', 'age', 'text']
        widgets = {
            'name': TextInput(attrs={
                'class':'form-control',
                'placeholder': 'Ваше имя'
            }),
            'age': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Возраст'
            }),
            'text': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Текст'
            }),
        }