from django.db import models

# Create your models here.
from account.models import CustomUser
from dreamColor import settings


class DreamModel(models.Model):
    title = models.CharField(verbose_name='제목' ,max_length=30),
    date_dream = models.DateField(verbose_name='꿈꾼날짜'),
    created = models.DateTimeField(verbose_name='생성시각',auto_now_add=True),
    keyword = models.CharField(verbose_name='키워드들', max_length=40),
    read_cnt = models.IntegerField(verbose_name='읽음개수',default=0),
    color = models.CharField(verbose_name='꿈색깔',max_length=10),
    contents = models.TextField(verbose_name='내용'),
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title