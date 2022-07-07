import cgi
import datetime
from collections import Counter

from pyexpat.errors import messages

from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import FormView

from dreams.forms import DreamForm
from dreams.models import DreamModel
from account.models import CustomUser
@csrf_exempt
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
    # 꿈 단어 제외하고 검색결과 가져오기
    for key in keywords[:-1]:
        word = urllib.parse.quote_plus(key+'꿈해몽')

        url = f'https://search.naver.com/search.naver?date_from=&date_option=0&date_to=&dup_remove=1&nso=&post_blogurl=&post_blogurl_without=&query={word}&sm=tab_pge&srchby=all&st=sim&where=post&start=5'
        html = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(html, 'html.parser')

        titles = soup.find_all(class_='api_txt_lines total_tit')

        results = []
        for index, title in enumerate(titles):
            if index == 6: break
            results.append((''.join((title.find_all(text=True))),title.attrs['href']))
            # print(''.join((title.find_all(text=True))))
            # print(title.attrs['href'])

    if len(results)==0:
        results.append(('제목에 해당하는 해몽을 찾지 못했습니다.',''))

    isUser = request.user == dream.author
    return render(request,'dreams/view.html',{'dream':dream, 'isUser':isUser, 'results':results})

def mainPage(request):
    # dream 전체 게시물 가져오기
    dream = DreamModel.objects.all()
    return render(request, 'dreams/main.html',{'dream_list':dream})


def search(request):
    datas = DreamModel.objects.values_list('color', flat=True)
    counter = dict(Counter(datas))
    sorted_color = sorted(counter, key=lambda x: x[1], reverse=True)[:5]
    context = {}
    context['colors'] = sorted_color
    return render(request, 'dreams/search.html', context)

def search_color(request, color_id):
    dream_list = DreamModel.objects.filter(color__contains=color_id)
    context = {'dream_list':dream_list}
    return render(request, 'dreams/main.html',context)


def search_title(request):
    context = {}
    # 검색
    search_word = request.GET.get('search_word','')

    dream_list = DreamModel.objects.filter(title__contains=search_word)
    context['dream_list'] = dream_list

    return render(request, 'dreams/main.html', {'dream_list':dream_list})


# 수정하기
def modify(request,id):
    dream = get_object_or_404(DreamModel,pk=id)
    if request.user != dream.author:
        messages.error(request, '수정권한이 없습니다.')
        return redirect(request,'dream:')

    if request.method == "POST":
        form = DreamForm(request.POST, instance=dream)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.save()
            return redirect('dream:detail', id=dream.id)
    else:
        form = DreamForm(instance=dream)
    context = {'form': form,'dream':dream}
    return render(request, 'dreams/modify.html', context)

# 카운트 업데이트
def read_count(request,id):
    dream = get_object_or_404(DreamModel,pk=id)
    dream.read_cnt = dream.read_cnt+1
    dream.save()
    return redirect('dream:detail',id=dream.id)

# 삭제하기
def delete(request,id):
    dream = get_object_or_404(DreamModel,pk=id)
    dream.delete()
    return redirect('dream:main')