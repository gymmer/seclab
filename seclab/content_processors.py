from models import *


def allItem(request):
    father_menu = FatherMenu.objects.all()
    son_menu = SonMenu.objects.all()
    slide_img = Img.objects.filter(tag='slideImg')
    activity = Article.objects.filter(tag='activity')
    news = Article.objects.filter(tag='news')

    para = {
        'father_menu': father_menu,
        'son_menu': son_menu,
        'slide_img': slide_img,
        'activity': activity,
        'news': news,
    }
    return para
