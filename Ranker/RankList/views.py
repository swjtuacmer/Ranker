# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from models import User
from dc import crawler


def RankPage(request):
    users = User.objects.order_by('-codeforces_rating')
    return render(request, 'RankPage.html', {'datas': users})

def UpdateDB(request):
    users = User.objects.all()
    # print users
    for item in users:
        item_codeforces_rating = crawler.UpdateCodeforces(item.codeforces_id)
        item.codeforces_rating = item_codeforces_rating
        item.save()
    return HttpResponse('success')

def about(request):
    return render(request, 'about.html')


