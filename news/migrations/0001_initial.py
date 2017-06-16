# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import DjangoUeditor.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='标题', max_length=256)),
                ('slug', models.CharField(verbose_name='网址', max_length=256, db_index=True)),
                ('content', DjangoUeditor.models.UEditorField(verbose_name='内容', blank=True, default='')),
                ('published', models.BooleanField(verbose_name='正式发布', default=True)),
                ('pub_date', models.DateTimeField(verbose_name='发表时间', auto_now_add=True)),
                ('update_time', models.DateTimeField(verbose_name='更新时间', null=True, auto_now=True)),
                ('author', models.ForeignKey(verbose_name='作者', blank=True, null=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='栏目名称', max_length=256)),
                ('slug', models.CharField(verbose_name='栏目网址', max_length=256, db_index=True)),
                ('intro', models.TextField(verbose_name='栏目简介', default='')),
                ('nav_display', models.BooleanField(verbose_name='导航显示', default=False)),
                ('home_display', models.BooleanField(verbose_name='首页显示', default=False)),
            ],
            options={
                'verbose_name': '栏目',
                'verbose_name_plural': '栏目',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='article',
            name='column',
            field=models.ForeignKey(verbose_name='归属栏目', to='news.Column'),
        ),
    ]
