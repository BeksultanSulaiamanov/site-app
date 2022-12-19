from .models import Elektro, Acsessuar, Nout
from django.forms import ModelForm, TextInput, IntegerField, ImageField

class ElektroForm(ModelForm):
    class Meta:
        model = Elektro
        fields = ['model', 'mark', 'price', 'color', 'img', 'description']

        widgets = {
            'model': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Модель'
            }),
            'mark': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Марка'
            }),
            'price': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'цена'
            }),
            'color': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'цвет'
            }),
            'description': TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+'
            }),
            'img': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'обзор'
            }),
        }






