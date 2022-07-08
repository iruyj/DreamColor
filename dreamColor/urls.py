"""dreamColor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from dreams import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('dream/', include('dreams.urls')),
    path('', views.mainPage, name='first'),
]
if settings.DEBUG:
    # static이라는 것을 가져와서 사용할 것인데,
    # 정적 파일들의 url을 관리하는 함수
    # 기본적으로 접근할 URL, 그곳으로 접근 시 media 파일의 경로는 어디인지를 넣어줌
    # 자동으로 접속한 url에 대한 파일을 가져와 보여줄 것
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
