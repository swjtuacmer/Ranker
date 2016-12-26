# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from models import User
from dc import crawler

# 页面处理部分
def RankPage(request):
    users = User.objects.order_by('-codeforces_rating')
    rank = 1
    for item in users:
        item.rank = rank
        rank += 1
    return render(request, 'RankPage.html', {'datas': users})

def Add(request):
    return render(request, 'add.html')

def about(request):
    return render(request, 'about.html')



# 表单提交处理
def AddUser(request):
    user_name = request.GET['user_name']
    codeforces_id = request.GET['codeforces_id']
    hdu_id = request.GET['hdu_id']
    poj_id = request.GET['poj_id']
    # print user_name, codeforces_id, hdu_id, poj_id
    try:
        user = User.objects.get(name=user_name)
    except:
        user = None
    if user is None:
        print "no one"
    return HttpResponse('success')

# 更新数据库操作
def UpdateDB(request):
    users = User.objects.all()
    # print users
    for item in users:
        item_codeforces_rating = crawler.UpdateCodeforces(item.codeforces_id)
        item.codeforces_rating = item_codeforces_rating
        item_bestcoder_rating = crawler.UpdateBestCoder(item.bestcoder_id)
        item.bestcoder_rating = item_bestcoder_rating
        item_hdu_problems = crawler.UpdateHduProblems(item.hdu_id)
        item.hdu_problems = item_hdu_problems
        item_poj_problems = crawler.UpdatePojProblems(item.poj_id)
        item.poj_problems = item_poj_problems
        item.save()
    return HttpResponse('success')
