from django.shortcuts import render

# Create your views here.
def createDream(request):
    return render('dreams/new.html',{{}})

def mainPage(request):
    return render(request, 'dreams/main.html')