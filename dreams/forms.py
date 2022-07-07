from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db.models import Q
from django.views.generic import FormView

from dreams.models import DreamModel


class DreamForm(forms.ModelForm):   # 장고의 UserCreationForm 클래스 상속
    class Meta:
        model = DreamModel
        fields = ['title','date_dream','color','contents']
