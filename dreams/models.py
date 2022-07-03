import datetime
from django.db import models

import account.models


class DreamModel(models.Model):
    title = models.CharField(max_length=30)
    date_dream = models.DateField()
    created = models.DateTimeField()
    read_cnt = models.IntegerField()
    color = models.CharField(max_length=10)
    contents = models.TextField()
    author = models.ForeignKey(account.models.CustomUser, on_delete=models.CASCADE)

    class Meta:
        db_table = 'dreammodel'