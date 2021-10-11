from django.shortcuts import render
from django.template import context
from django.utils.timezone import datetime

from .forms import ArticleForm, CommentaryForm


from .models import Article, Commentary

def index(request):
    return render(request,'Forum/home.html')

def article_detail(request,pk):
    article = Article.objects.get(id=pk)
    commentarys = Commentary.objects.filter(article__pk=pk)
    context = {
        'title' : article.title,
        'contents' : article.contents,
        'author' : article.author,
        'date' : article.date,
        'positif' : article.positif,
        'negatif' : article.negatif,
        'commentarys' : commentarys,
        'id' : pk,
    }
    commenentarys = Commentary.objects.filter(article__pk=pk)
    return render (request,"Forum/detail.html",context)

def article_list (request):
    articles = Article.objects.all()
    context = { 'articles' : articles }
    return render (request,"Forum/list.html",context)

def article_like (request,pk):
    article = Article.objects.get(id=pk)
    article.positif = article.positif + 1
    article.save()
    return article_detail(request,pk)

def article_dislike(request,pk):
    article = Article.objects.get(id=pk)
    article.negatif = article.negatif + 1
    article.save()
    return article_detail(request,pk)

def article_new (request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.date = datetime.today()
            article.save()
            pk = article.id
            return article_detail(request,pk)
        else:
            form = ArticleForm()
            context = { 'form' : form ,
                        'error' : "Post invalid"}
            return render(request,"Forum/article.html",context)
    else:
        form = ArticleForm()
        context = { 'form' : form }
        return render(request,"Forum/article.html",context)

def commentary_new (request,pk):
    if request.method == "POST":
        form = CommentaryForm(request.POST)
        if form.is_valid():
            article = Article.objects.get(id=pk)
            commentary = form.save(commit=False)
            commentary.date = datetime.today()
            commentary.article = article
            commentary.save()
            return article_detail(request,pk)
        else:
            form = CommentaryForm()
            context = { 'form' : form ,
                        'error' : "Post invalid"}
            return render(request,"Forum/commentary.html",context)
    else:
        form = ArticleForm()
        context = { 'form' : form }
        return render(request,"Forum/commentary.html",context)