import random

import form as form
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.db.models import Max
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from account.forms import UserForm, LoginForm


# Create your views here.
from account.models import CustomUser
from dreams.models import DreamModel

@csrf_exempt
def signup(request):
    # 계정 생성
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            userid = form.cleaned_data.get('username')
            pw = form.cleaned_data.get("password1")
            # 사용자명과 비밀번호 정확한지 검증
            isUser = authenticate(username=userid, password=pw)
            # 자동으로 로그인하기
            print('로그인됨')
            auth_login(request,isUser)
            return redirect('/')
    else:
        form = UserForm()
    return render(request, 'account/signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        id = request.POST.get('username')
        pw = request.POST.get('password')
        user = authenticate(username=id,password =pw)
        if user is not None:
            print(user)
            auth_login(request,user)
            return redirect('/')
        return render(request,'account/login.html',{'form':form,'state':'false'})
    else:
        form = LoginForm()
        return render(request, 'account/login.html',{'form':form,'state':'true'})

def mypage(request, userid):

    # cur_user = request.user
    if request.user.is_authenticated:
        user = CustomUser.objects.get(username=userid)
        dream = DreamModel.objects.filter(author=user)

        # 랜덤 정보 생성 함수 호출
        dreams = get_random_dreams()
        random_dreams = DreamModel.objects.filter(id__in=dreams)
        return render(request, 'account/mypage.html', {'user': user, 'dreams': dream, 'random':random_dreams})
    else:
        return render(request, 'account/login.html')

def get_random_dreams():
    max_id = DreamModel.objects.all().aggregate(max_id = Max("id"))['max_id']
    list = []
    ran_num = random.randint(1, max_id)
    for i in range(6):
        while ran_num in list:
            ran_num = random.randint(1,max_id)
        list.append(ran_num)
    list.sort()
    return list
