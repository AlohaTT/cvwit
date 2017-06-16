# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='论文栏目名称', max_length=256)),
                ('slug', models.CharField(verbose_name='论文栏目网址', db_index=True, max_length=256)),
                ('intro', models.TextField(verbose_name='论文栏目简介', default='')),
                ('nav_display', models.BooleanField(verbose_name='导航显示', default=False)),
                ('home_display', models.BooleanField(verbose_name='首页显示', default=False)),
            ],
            options={
                'verbose_name': '论文栏目',
                'verbose_name_plural': '论文栏目',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='文章题目', max_length=256)),
                ('slug', models.CharField(verbose_name='网址', db_index=True, max_length=256)),
                ('author', models.CharField(verbose_name='文章作者', max_length=256)),
                ('file', models.FileField(verbose_name='文件', upload_to='')),
                ('column', models.ForeignKey(verbose_name='归属栏目', to='paper.Column')),
            ],
        ),
    ]
