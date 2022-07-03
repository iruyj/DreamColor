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
            return redirect('dream:detail', id=dream.id)
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
    import urllib.request
    from bs4 import BeautifulSoup

    results =[]
    for key in keywords:
        word = urllib.parse.quote_plus(key+'꿈해몽')

        url = f'https://search.naver.com/search.naver?date_from=&date_option=0&date_to=&dup_remove=1&nso=&post_blogurl=&post_blogurl_without=&query={word}&sm=tab_pge&srchby=all&st=sim&where=post&start=5'
        html = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(html, 'html.parser')

        titles = soup.find_all(class_='api_txt_lines total_tit')

        results = []
        for index, title in enumerate(titles):
            if index == 3: break
            results.append((''.join((title.find_all(text=True))),title.attrs['href']))
            # print(''.join((title.find_all(text=True))))
            # print(title.attrs['href'])

    if len(results)==0:
        results.append(('제목에 해당하는 해몽을 찾지 못했습니다.',''))

    isUser = request.user == dream.author
    return render(request,'dreams/view.html',{'dream':dream, 'isUser':isUser, 'results':results})

def mainPage(request):
    dream_list = {'title': '추락하는 꿈', 'date_dream': datetime.date, 'bg': '#F2C4DA', 'contents': '내용ㅇㅇㅇ'
        , 'author': 'ㅇㄹㅇㄴ', 'read': 21}
    return render(request, 'dreams/main.html',{'dream':dream_list})

def findKey(request):
    return render(request, 'dreams/search.html')