from django.db import models
from django.contrib import admin


'''
类和Django Model
django的数据model（django的核心),是从django的内置类django.db.models.zModel继承而来的子类。django的Model
类提供了大量的强大特性
'''
class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()


    class Meta:
        ordering = ('-timestamp')
