# -*- coding: utf-8 -*-
import json
import requests
from bs4 import BeautifulSoup
import re

# 获取 codeforces rating 数据
def UpdateCodeforces(codeforces_id):
    url = "http://codeforces.com/api/user.info?handles="
    try:
        data = requests.get(url + codeforces_id)
        dic_res = json.loads(data.text)
        res_rating = dic_res['result'][0]['rating']
    except:
        res_rating = -1
    return res_rating

# 获取 BestCoder rating 数据
def UpdateBestCoder(bestcoder_id):
    url_bestcoder = "http://bestcoder.hdu.edu.cn/ranklist.php?type=username&keyword="
    try:
        data = requests.get(url_bestcoder + bestcoder_id)
        soup = BeautifulSoup(data.text, "html.parser")
        # print(soup.prettify())
        links = soup.find_all("td")[-1].string
        res_rating = int(links)
    except:
        res_rating = -1
    return res_rating


# 获取 HDU 数据
def UpdateHduProblems(hdu_id):
    url_hdu = "http://acm.hdu.edu.cn/search.php?field=author&key="
    try:
        data = requests.get(url_hdu + hdu_id)
        soup = BeautifulSoup(data.text, "html.parser")
        #print(soup.prettify())
        links = str(soup.find_all("tbody")[0])
        pattern = re.compile(r"(</td><td>)(\d+)(</td>)")
        match = re.search(pattern, links)
        res_problems = int(match.group(2))
    except:
        res_problems = -1
    return res_problems

# 获取 POJ 数据
def UpdatePojProblems(poj_id):
    url_poj = "http://poj.org/searchuser?key=***&B1=Search"
    try:
        url = url_poj.replace("***", poj_id)
        data = requests.get(url)
        soup = BeautifulSoup(data.text, "html.parser")
        # print(soup.prettify())
        links = soup.find_all("td")[-2].string
        res_problems = int(links)
    except:
        res_problems = -1
    return res_problems

