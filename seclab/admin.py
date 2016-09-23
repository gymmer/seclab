from django.contrib import admin

# Register your models here.
from models import *


class FatherMenuAdmin(admin.ModelAdmin):
    list_play = ('title', 'slug', 'son')


class SonMenuAdmin(admin.ModelAdmin):
    list_play = ('title', 'slug', 'FatherMenu')


class ImgAdmin(admin.ModelAdmin):
    list_play = ('tag', 'tagId', 'intro', 'title', 'slag')


class ArticleAdmin(admin.ModelAdmin):
    list_play = ('tag', 'title', 'author', 'pub_date', 'home_display')

admin.site.register(FatherMenu, FatherMenuAdmin)
admin.site.register(SonMenu, SonMenuAdmin)
admin.site.register(Img, ImgAdmin)
admin.site.register(Article, ArticleAdmin)
