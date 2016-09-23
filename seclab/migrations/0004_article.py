# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-18 03:01
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('seclab', '0003_auto_20160515_1305'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=20, verbose_name='\u7c7b\u578b')),
                ('title', models.CharField(max_length=100, verbose_name='\u6807\u9898')),
                ('content', models.TextField(verbose_name='\u5185\u5bb9')),
                ('slug', models.CharField(db_index=True, max_length=100, verbose_name='\u94fe\u63a5')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='\u53d1\u8868\u65f6\u95f4')),
                ('home_display', models.BooleanField(default=False, verbose_name='\u9996\u9875\u663e\u793a')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u4f5c\u8005')),
            ],
            options={
                'verbose_name': '\u6587\u7ae0',
                'verbose_name_plural': '\u6587\u7ae0',
            },
        ),
    ]