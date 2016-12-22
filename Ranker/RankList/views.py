#coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render
from models import User
import requests
import json

def RankPage(request):
    users = User.objects.all()
    return render(request, 'RankPage.html', {'datas': users})


