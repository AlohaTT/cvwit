# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from DjangoUeditor.models import UEditorField

from django.core.urlresolvers import reverse
@python_2_unicode_compatible

class Column(models.Model):
    name = models.CharField('论文栏目名称', max_length=256)
    slug = models.CharField('论文栏目网址', max_length=256, db_index=True)
    intro = models.TextField('论文栏目简介', default='')

    nav_display = models.BooleanField('导航显示', default=False)
    home_display = models.BooleanField('首页显示', default=False)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('column', args=(self.slug,))

    class Meta:
        verbose_name = '论文栏目'
        verbose_name_plural = '论文栏目'
        ordering = ['name']

@python_2_unicode_compatible
class Paper(models.Model):
    column = models.ForeignKey(Column, verbose_name='归属栏目')

    title = models.CharField('文章题目', max_length=256)
    slug = models.CharField('网址', max_length=256, db_index=True)

    author = models.CharField('文章作者', max_length=256)
    #仅修改 content 字段

    def get_absolute_url(self):
        return reverse('article', args=(self.pk, self.slug))

    def __str__(self):
        return self.title
