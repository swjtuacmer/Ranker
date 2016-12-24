# -*- coding: utf-8 -*-
import urllib2
import json

# 获取 codeforces rating 数据
def UpdateCodeforces(codeforces_id):
    url = "http://codeforces.com/api/user.info?handles="
    req = urllib2.Request(url + codeforces_id)
    res_data = urllib2.urlopen(req)
    res = res_data.read()
    dic_res = json.loads(res)
    res_rating = dic_res['result'][0]['rating']
    return res_rating

# 获取 BestCoder rating 数据
def UpdateBestCoder(bestcoder_id):
    res_rating = 0
    return res_rating

# 获取 HDU 数据
def UpdateHduProblems(hdu_id):
    res_problems = 0
    return res_problems

# 获取 POJ 数据
def UpdatePojProblems(poj_id):
    res_problems = 0
    return res_problems

