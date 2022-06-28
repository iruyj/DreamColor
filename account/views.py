from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from account.forms import UserForm

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
            login(request,isUser)
            return redirect('/')
        else:
            form = UserForm()
        return render(request, 'account/signup.html', {'form': form})
