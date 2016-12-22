from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length = 30)
    codeforces_id = models.CharField(max_length = 30)
    codeforces_rating = models.IntegerField()
    bestcoder_id = models.CharField(max_length = 30)
    bestcoder_rating = models.IntegerField()
    hdu_id = models.CharField(max_length = 30)
    hdu_problems = models.IntegerField()
    poj_id = models.CharField(max_length = 30)
    poj_problems = models.IntegerField()

    def __unicode__(self):
        return self.name


