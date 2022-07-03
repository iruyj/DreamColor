import datetime

from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from dreams.forms import DreamForm
from dreams.models import DreamModel


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

def viewDream(request, id):
    # dream 게시물 가져오기
    dream = get_object_or_404(DreamModel,id=id)
    # 제목 키워드 분석
    from konlpy.tag import Okt
    okt = Okt()
    keywords = okt.nouns(dream.title)
    # 해당 해몽들 보여주기
    # 글쓴이인지 판별
    isUser = request.user == dream.author
    return render(request,'dreams/view.html',{'dream':dream, 'isUser':isUser})

def mainPage(request):
    dream_list = {'title': '추락하는 꿈', 'date_dream': datetime.date, 'bg': '#F2C4DA', 'contents': '내용ㅇㅇㅇ'
        , 'author': 'ㅇㄹㅇㄴ', 'read': 21}
    return render(request, 'dreams/main.html',{'dream':dream_list})

def findKey(request):
    return render(request, 'dreams/search.html')