import datetime

from django.shortcuts import render

# Create your views here.
def createDream(request):
    return render(request,'dreams/new.html')

def viewDream(request):
    dream = {'title':'추락하는 꿈', 'date_dream':datetime.date,'keyword':['나라','사랑','친구'],'bg':'#fffff','contents':'내용ㅇㅇㅇ'
             ,'user':'ㅇㄹㅇㄴ', 'read':21}
    return render(request,'dreams/view.html',{'dream':dream})

def mainPage(request):
    return render(request, 'dreams/main.html')

def findKey(request):
    return render(request, 'dreams/search.html')