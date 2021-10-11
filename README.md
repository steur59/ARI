Django Projet Forum

0 Intro	2
1.Set-up	3
1.A Installation de Python	3
1.B Installation de Django	3
1.C Création du projet.	3
1.D Création de la partie Forum	3
1.E Vérifier le bon fonctionnement du serveur	3
2.Gestion des Views (vues)	4
2.A Créer notre index	4
2.B Ajouter notre index dans l’url pattern de Forum	4
2.C Ajouter l’url à la racine	4
3.Gestion des modèles :	5
3.A Créer le modèle article	5
3.B Créer le modèle commentaire	5
3.C Déclarer la base de donnée	5
3.C Lancer la migration du modèle	5
3.D Créer des données en Admin	6
4. Gestion des templates	7
4.A Set-up de notre premier template	7
5 A vous de jouer	9
5.A Afficher les détails d’un article	9
5.B Afficher la liste des articles	9
5.C Lié chaque article à sa page	10
5.D Ajouter les commentaires dans le détail des articles	10
5.E Ajouter les fonctionnalités de like et dislike	10
5.F Ajouter le formulaire de création d’articles	10
5.G Ajouter le formulaire de création de commentaires	11


0 Intro
Nous souhaitons créer un forum où les personnes pourraient librement créer leurs articles, les commenter et ajouter une réaction positif ou négatif

1.Set-up
1.A Installation de Python
Installer Python
Pour vérifier son installation lancer dans un terminal n’importe ou:
$Python3
 (ou python / ou py selon votre OS)
puis pour quitter entrer :
exit()
1.B Installation de Django
Lancer dans un terminal n’importe ou
$python3 -m pip install Django
1.C Création du projet.
Lancer dans un terminal à l’endroit ou vous souhaitez créer votre projet :
$python3 -m django startproject Tp_django
ou télécharger le projet vierge sur : https://drive.google.com/drive/folders/1gi9qDyBpflvOYTy_pfxg4pp9vdsOq-rA?usp=sharing
1.D Création de la partie Forum
Lancer dans un terminal à la racine du projet (/Tp_django)
$python3 manage.py startapp Forum
1.E Vérifier le bon fonctionnement du serveur 
Lancer dans un terminal à la racine du projet (/Tp_Django)
$python3 manage.py runserver

Connection via un navigateur
http://127.0.0.1:8000/
http://localhost:8000/

Vous pouvez le maintenir allumé car le serveur reboot si nécessaire à chaque modification.
2.Gestion des Views (vues)
2.A Créer notre index
Dans Tp_django/Forum/views.py
from django.shortcuts import render
 
from django.http import HttpResponse
 
 
def index(request):
    return HttpResponse("Miage over flow")
 

2.B Ajouter notre index dans l’url pattern de Forum
Ajoutons dans l’url patterns le chemin vers notre partie forum 
Dans Tp_django/Forum créer un fichier urls.py :
from django.urls import path
 
from . import views
 
 
urlpatterns = [
    path('', views.index, name='index'),
]
 
2.C Ajouter l’url à la racine
Ajoutons dans l’url patterns le chemin vers notre partie forum 
Dans Tp_django/Tp_django/urls.py
*Attention à ajouter l’import include*
from django.contrib import admin
from django.urls import path,include
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('forum/', include('forum.urls')),
]

FÉLICITATIONS VOUS AVEZ VOTRE PREMIÈRE PAGE YOUHOU 
http://127.0.0.1:8000/Forum/
3.Gestion des modèles :
3.A Créer le modèle article
class Article(models.Model):
    title = #TODO
    contents = #TODO
    author = #TODO
    date = #TODO
    positif = #TODO
    negatif = #TODO                                                                
( Il faut préciser ce que veut dire positif et negatif pour qu’ils puissent deviner le type)
3.B Créer le modèle commentaire
class Commentary(models.Model):
    article = #TODO article
    contents = #TODO
    author = #TODO
    date = #TODO

3.C Déclarer la base de donnée
Dans Tp_django/settings.py ajouter 'Forum.apps.ForumConfig' 
dans INSTALLED_APPS = []
cela doit ressembler à ça : 

# Application definition
 
INSTALLED_APPS = [
    'Forum.apps.ForumConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
3.C Lancer la migration du modèle
Dans Tp_django lancer dans un terminal : 
$python3 manage.py makemigrations Forum

vous devriez obtenir :
Migrations for 'Forum':
  Forum\migrations\0001_initial.py
    - Create model Article
    - Create model Commentary

Puis dans Tp_django lancer dans un terminal : 
$python3 manage.py migrate

FÉLICITATIONS VOUS AVEZ VOS PREMIERS MODÈLES DE DONNÉES
3.D Créer des données en Admin
Pour commencer créer un compte admin
Dans Tp_django lancer dans un terminal : 
$python3 manage.py createsuperuser

Maintenant que votre compte admin est créé rendez-vous sur :
http://127.0.0.1:8000/admin/

Comme vous pouvez le constater actuellement il n’y a des tables user et group qui servent à la gestion des utilisateurs et de leurs droits sur la base donnée.

Il faut donc indiquer à Django les deux nouveaux modèles
Compléter Tp_django/Forum/admin.py :
from django.contrib import admin
from .models import Article,Commentary
 
# Register your models here.
 
 
 
admin.site.register(Article)
admin.site.register(Commentary)

Amusez-vous à découvrir le panneau d’administration ...
4. Gestion des templates
4.A Set-up de notre premier template
Créer l’architecture de dossiers Tp_django/Forum/templates/Forum
Ainsi que notre premier fichier template base.html de tel sorte que :
Dans Tp_django/Forum/templates/Forum/base.html

On retrouve : 

<body>
    <!DOCTYPE html>
    <html lang="fr">
    <title>Miage Overflow</title>
    <meta charset="UTF-8">
 
<body>
 
<!-- NAVBAR -->
<div style="background-color: black; font-size: 50px; ">
        <a style="text-decoration: none; color: rgb(255, 255, 255);" href="http://127.0.0.1:8000/Forum">Miage Overflow</a>
</div>
<!-- END NAVBAR -->
<br/>
<!-- MAIN -->
<div style=" border : solid ;" >
    {% block content %}
    <div  id=content>
        <!-- CONTENT -->
    </div>
    {% endblock %}
<!-- END MAIN -->
</div>
</body>
</html>
 

puis créer Tp_django/Forum/templates/Forum/home.html
tel sorte que :
{% extends 'Forum/base.html' %}
 
{% block content %}
Bienvenue sur Miage Overflow !
{% endblock %}
puis modifier le fichier Tp Django/Forum/view.py de tel sorte qu’il ressemble à ça :

from django.shortcuts import render
 
def index(request):
    return render(request,'Forum/home.html')

retourner sur http://127.0.0.1:8000/Forum/

FÉLICITATIONS VOUS AVEZ VOS PREMIER TEMPLATE !


5 A vous de jouer
5.A Afficher les détails d’un article
A partir de http://127.0.0.1:8000/Forum/article/1 obtenir les informations de l’article d’id 1
Pour  rappel : 
Il faut ajouter le path dans Forum/url.py
Ajouter une fonction dans Forum/views.py
Créer le template associé dans Forum/Templates/Forum

5.B Afficher la liste des articles
A partir de http://127.0.0.1:8000/Forum/articles obtenir la liste des articles



5.C Lié chaque article à sa page
href="http://127.0.0.1:8000/Forum/article/{{article.id}}"

5.D Ajouter les commentaires dans le détail des articles

5.E Ajouter les fonctionnalités de like et dislike
Ajouter des boutons pour permettre d’ajouter un like ou dislike aux articles

5.F Ajouter le formulaire de création d’articles

5.G Ajouter le formulaire de création de commentaires

