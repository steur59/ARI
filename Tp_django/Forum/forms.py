from django import forms

from .models import Article,Commentary

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('author', 'title','contents')

class CommentaryForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ('author', 'contents')

