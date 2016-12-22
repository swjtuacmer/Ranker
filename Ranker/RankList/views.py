#coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render
from models import User
import requests
import json

def RankPage(request):
    users = User.objects.all()
    print users[0].name
    return render(request, 'RankPage.html')


