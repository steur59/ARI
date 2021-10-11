from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('article/<int:pk>',views.article_detail),
    path('articles/',views.article_list),
    path('article/<int:pk>/like',views.article_like),
    path('article/<int:pk>/dislike',views.article_dislike),
    path('article/<int:pk>/commentary',views.commentary_new),
    path('article/new',views.article_new),
]