from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from account.forms import UserForm, LoginForm


# Create your views here.
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

def mypage(request):
    return render(request, 'account/mypage.html')