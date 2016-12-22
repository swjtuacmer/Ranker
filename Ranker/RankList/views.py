#coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render

def RankPage(request):
    return render(request, 'RankPage.html')
