from dataclasses import field
from pyexpat import model
from django.forms import ModelForm
from .models import Room
class RoomForm(ModelForm):
    class Meta:
        model = Room
        field = '__all__'