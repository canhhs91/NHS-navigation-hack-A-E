from django.db import models
from datetime import datetime
from django.db.models import Sum, F
# Create your models here.


class Question(models.Model):
    content = models.CharField(blank=True, max_length=2000, verbose_name='Question', default = '')
    picture = models.ImageField(upload_to='images/authors/', null=True, blank=True)
    next_if_yes = models.IntegerField(blank=True, default = 0, verbose_name='Next If Yes')
    next_if_no = models.IntegerField(blank=True, default = 0, verbose_name='Next If No')
    important = models.BooleanField(default = False, verbose_name='Show in summary')
    short_title = models.CharField(blank=True, max_length=2000, verbose_name='Short  title', default = '')