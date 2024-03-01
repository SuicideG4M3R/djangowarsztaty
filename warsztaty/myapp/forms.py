from django import forms
from .models import Sala, Rezerwacja
import datetime


class SalaForm(forms.ModelForm):
    class Meta:
        model = Sala
        fields = ('nazwa', 'pojemnosc', 'rzutnik_dostepny')

        widgets = {
            'nazwa': forms.TextInput(attrs={'required': True}),
            'pojemnosc': forms.NumberInput(attrs={'required': True}),
            'rzutnik_dostepny': forms.CheckboxInput()
        }


class RezerwacjaForm(forms.ModelForm):
    class Meta:
        model = Rezerwacja
        fields = ['data', 'komentarz']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_data(self):
        data = self.cleaned_data['data']
        if data < datetime.date.today():
            raise forms.ValidationError("Data nie może być w przeszłości.")
        return data
