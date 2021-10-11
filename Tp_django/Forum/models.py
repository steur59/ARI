from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=30)
    contents = models.CharField(max_length=600)
    author = models.CharField(max_length=30)
    date = models.DateField()
    positif = models.PositiveIntegerField(default=0)
    negatif = models.PositiveIntegerField(default=0)

class Commentary(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    contents = models.CharField(max_length=300)
    author = models.CharField(max_length=30)
    date = models.DateField()

