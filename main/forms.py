from django.forms import ModelForm, TextInput,NumberInput
from .models import Builders


class BuildersForm(ModelForm):
    class Meta:
        model = Builders
        fields = ['name', 'second_name']

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder' : 'Имя'
            }),

            "second_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия'
            }),



        }