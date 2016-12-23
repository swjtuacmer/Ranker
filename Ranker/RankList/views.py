# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from models import User
import urllib2
import json

def RankPage(request):
    users = User.objects.order_by('-codeforces_rating')
    return render(request, 'RankPage.html', {'datas': users})

def UpdateDB(request):
    users = User.objects.all()
    # print users
    for item in users:
        item_codeforces_rating = UpdateCodeforces(item.codeforces_id)
        item.codeforces_rating = item_codeforces_rating
        item.save()
    return HttpResponse('success')

def UpdateCodeforces(codeforces_id):
    # codeforces_id = "Desgard_Duan"
    url = "http://codeforces.com/api/user.info?handles="
    req = urllib2.Request(url + codeforces_id)
    res_data = urllib2.urlopen(req)
    res = res_data.read()
    dic_res = json.loads(res)
    res_rating = dic_res['result'][0]['rating']
    return res_rating

