#!/usr/bin/env python
# coding:utf-8

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
'''
Django 版本大于等于1.7的时候，需要加上下面两句
import django
django.setup()
否则会抛出错误 django.core.exceptions.AppRegistryNotReady: Models aren't loaded yet.
'''

import django

if django.VERSION >= (1, 7):  # 自动判断版本
    django.setup()


def main():
    from blogapp.models import Access
    f = open('2.txt')
    for line in f:
        ip, date, url, full_url = line.split(',')
        Access.objects.create(ip=ip, date=date, url=url, full_url=full_url)
    f.close()


if __name__ == "__main__":
    main()
    print('Done!')