# _*_ coding:utf-8 _*_
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.


class FatherMenu(models.Model):

    title = models.CharField(u"菜单名", max_length=20)
    slug = models.CharField(u"链接", max_length=100, db_index=True)
    son = models.BooleanField("子菜单?", default=False)

    class Meta:
        verbose_name = u"一级菜单"
        verbose_name_plural = u"一级菜单"

    def __str__(self):
        return self.title


class SonMenu(models.Model):

    title = models.CharField(u"菜单名", max_length=20)
    slug = models.CharField(u"链接", max_length=100, db_index=True)
    father = models.ForeignKey(
        'seclab.FatherMenu', blank=True, null=True, verbose_name=u"父菜单")

    class Meta:
        verbose_name = u"二级菜单"
        verbose_name_plural = u"二级菜单"

    def __str__(self):
        return self.title


class Img(models.Model):
    tag = models.CharField(u"类型", max_length=20)
    tagId = models.IntegerField(u"序号")
    intro = models.CharField(u"描述", max_length=100)
    title = models.CharField(u"标题", max_length=100)
    slug = models.CharField(u"链接", max_length=100, db_index=True)

    class Meta:
        verbose_name = u"图片"
        verbose_name_plural = u"图片"

    def __str__(self):
        return self.slug


class Article(models.Model):
    tag = models.CharField(u"类型", max_length=20)
    title = models.CharField(u"标题", max_length=100)
    content = models.TextField(u"内容", default=u'', blank=True)
    author = models.CharField(u"作者", max_length=100)
    pub_date = models.DateField(u'发表日期', auto_now_add=True, editable=True)
    home_display = models.BooleanField(u"首页显示", default=False)

    class Meta:
        verbose_name = u"文章"
        verbose_name_plural = u"文章"

    def __str__(self):
        return self.title
