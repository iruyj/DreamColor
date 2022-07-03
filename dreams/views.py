import datetime

from django.shortcuts import render, redirect

# Create your views here.
from dreams.forms import DreamForm


def createDream(request):
    if request.method == 'POST':
        form = DreamForm(request.POST)
        if form.is_valid():
            dream = form.save(commit=False)
            dream.created = datetime.datetime.now()
            dream.read_cnt = 0
            dream.author = request.user
            dream.save()
            return redirect('first')
    else:
        form = DreamForm()
    return render(request,'dreams/new.html',{'form':form})

def viewDream(request):
    dream = {'title':'추락하는 꿈', 'date_dream':datetime.date,'bg':'#fffff','contents':'내용ㅇㅇㅇ'
             ,'author':'ㅇㄹㅇㄴ', 'read':21}
    user = request.user
    return render(request,'dreams/view.html',{'dream':dream, 'user':user})

def mainPage(request):
    dream_list = {'title': '추락하는 꿈', 'date_dream': datetime.date, 'bg': '#F2C4DA', 'contents': '내용ㅇㅇㅇ'
        , 'author': 'ㅇㄹㅇㄴ', 'read': 21}
    return render(request, 'dreams/main.html',{'dream':dream_list})

def findKey(request):
    return render(request, 'dreams/search.html')