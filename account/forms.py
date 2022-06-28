from django import forms
from django.contrib.auth.forms import UserCreationForm

from account.models import CustomUser


class UserForm(UserCreationForm):   # 장고의 UserCreationForm 클래스 상속

    class Meta:
        model = CustomUser
        fields = ("username", "nickname", "password1", "password2", "usercolor")
