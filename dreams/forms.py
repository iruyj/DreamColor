from django.contrib.auth.forms import UserCreationForm

from dreams.models import DreamModel

class DreamForm(UserCreationForm):   # 장고의 UserCreationForm 클래스 상속

    class Meta:
        model = DreamModel
        fields = ['title','date_dream','created','read_cnt','color','contents','user']
