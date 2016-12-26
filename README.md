
![](Ranker-banner.png)

# Ranker - ACMer 实力评估系统

![](https://img.shields.io/badge/Python-2.7-green.svg)
![](https://img.shields.io/badge/Django-1.9.0-green.svg)
![](https://img.shields.io/badge/license-MIT-green.svg?style=flat)

## Description

用于 ACM 校集训队对队员的实例评测系统。从 Codeforces、hdu、poj 等各大网站获取比赛及刷题数据,通过排名算法进行实力评估。

## The Simple Docs for dev.

[The docs of virtualenv](http://pythonguidecn.readthedocs.io/zh/latest/dev/virtualenvs.html)

[The docs of bs4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html)

[The docs of Django v1.9](https://docs.djangoproject.com/en/1.9/)

[A good tutorial of Django Dev.](http://www.ziqiangxuetang.com/django/django-tutorial.html)

## The Dev. Flow

* 开发方式与分支管理

组内成员请在 `dev` 分支下进行开发。你可以细化功能，对 `dev` 分支进行分离，创建新的开发分支，命名为 `dev-[function name]` 。倘若非组内成员想发起 `pull request` ，请确定 base  为 `dev` 分支，否则不经 review 直接 close。

* 接口的开发及后期的可移植性

数据库暂时采用 `sqlite3` 由于我校需求量较小。由于 Django 1.7 之后的版本是自带 source 工具的，所以可迁移数据库。

## MIT License

Copyright (c) 2016 swjtuacmer

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

