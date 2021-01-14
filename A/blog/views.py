from django.shortcuts import render
from .models import Article

# Create your views here.
def all_articles(request):
    all_articles = Article.objects.all()
    return render(request,'blog/all_articles.html',{'all_articles':all_articles})

def article_detail(request,id,slug):
    article = Article.objects.get(id = id)
    return render(request,'blog/article_detail.html',{'article':article})
