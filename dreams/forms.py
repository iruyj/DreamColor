from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from dreams.models import DreamModel


class DreamForm(ModelForm):   # 장고의 UserCreationForm 클래스 상속

    class Meta:
        model = DreamModel
        fields = ['title','date_dream','color','contents']
