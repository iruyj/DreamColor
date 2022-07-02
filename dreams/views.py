import datetime

from django.shortcuts import render

# Create your views here.
from dreams.forms import DreamForm


def createDream(request):
    if request.method == 'POST':
        form = DreamForm(request.POST)
        if form.is_valid():
            dream = form.save(commit=False)
            dream.created = datetime.datetime.now()

    return render(request,'dreams/new.html')

def viewDream(request):
    dream = {'title':'추락하는 꿈', 'date_dream':datetime.date,'bg':'#fffff','contents':'내용ㅇㅇㅇ'
             ,'user':'ㅇㄹㅇㄴ', 'read':21}
    user = request.user
    return render(request,'dreams/view.html',{'dream':dream, 'user':user})

def mainPage(request):
    return render(request, 'dreams/main.html')

def findKey(request):
    return render(request, 'dreams/search.html')