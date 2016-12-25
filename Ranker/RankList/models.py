from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length = 30)
    codeforces_id = models.CharField(max_length = 30, null = True)
    codeforces_rating = models.IntegerField(default = 0, null = True)
    bestcoder_id = models.CharField(max_length = 30, null = True)
    bestcoder_rating = models.IntegerField(default = 0, null = True)
    hdu_id = models.CharField(max_length = 30, null = True)
    hdu_problems = models.IntegerField(default = 0, null = True)
    poj_id = models.CharField(max_length = 30, null = True)
    poj_problems = models.IntegerField(default = 0, null = True)
    vj_id = models.CharField(max_length = 30, null = True)
    vj_problems = models.IntegerField(default = 0, null = True)

    def __unicode__(self):
        return self.name

