from django.forms import ModelForm
from django.forms.fields import CharField
from .models import ReservationCode, random_string

class ReservationForm(ModelForm):

    code = CharField(disabled=True, initial=random_string())

    class Meta:
        model = ReservationCode
        fields = ['code','event']
        