from django.shortcuts import render
from models import Article
# Create your views here.


def index(request):
    return render(request, 'seclab/index.html')


def page(request, slug):
    return render(request, 'seclab/page/' + slug + '.html')


def article(request, pk):
    article = Article.objects.get(pk=pk)
    return render(request, 'seclab/article.html', {'article': article})
