---
title: Comment enregistrer des modèles dans Django Admin
subtitle: ''
author: Udemezue John
co_authors: []
series: null
date: '2025-04-29T14:43:46.511Z'
originalURL: https://freecodecamp.org/news/how-to-register-models-in-django-admin
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1745937579596/e8aed227-b7c3-4bf6-a448-a66782aeea42.png
tags:
- name: Python
  slug: python
- name: Django
  slug: django
seo_title: Comment enregistrer des modèles dans Django Admin
seo_desc: 'When you''re building a website or an app with Django, one of the most
  exciting moments is when your database models finally come to life.

  But to manage your data easily – adding, editing, or deleting entries – you need
  Django’s Admin panel.

  Now, here...'
---

Lorsque vous construisez un site web ou une application avec Django, l'un des moments les plus excitants est lorsque vos modèles de base de données prennent enfin vie.

Mais pour gérer vos données facilement – ajouter, modifier ou supprimer des entrées – vous avez besoin du panneau d'administration de Django.

Voici le piège : simplement créer un modèle n'est pas suffisant. Si vous voulez qu'il apparaisse dans le panneau d'administration, vous devez l'**enregistrer**.

Et honnêtement, l'enregistrement des modèles dans Django Admin est l'une des étapes les plus simples mais les plus importantes. Si vous l'oubliez, cela donne l'impression que votre modèle n'existe même pas.

Dans ce guide, je vais vous expliquer exactement comment enregistrer vos modèles dans Django Admin, étape par étape, avec des exemples de code faciles à comprendre.

## Table des matières

* [Pourquoi Django Admin est important](#heading-pourquoi-django-admin-est-important)
    
* [Comment enregistrer des modèles dans Django Admin](#heading-comment-enregistrer-des-modeles-dans-django-admin)
    
    * [Étape 1 : Assurez-vous d'avoir un modèle](#heading-etape-1-assurez-vous-davoir-un-modele)
        
    * [Étape 2 : Enregistrez votre modèle dans Admin](#heading-etape-2-enregistrez-votre-modele-dans-admin)
        
    * [Étape 3 : (Optionnel) Personnalisez l'apparence de votre modèle dans Admin](#heading-etape-3-optionnel-personnalisez-lapparence-de-votre-modele-dans-admin)
        
* [FAQ](#heading-faq)
    
    * [1\. J'ai ajouté un modèle, mais il n'apparaît pas dans Admin. Que s'est-il passé ?](#heading-1-jai-ajoute-un-modele-mais-il-napparait-pas-dans-admin-quest-ce-qui-sest-passe)
        
    * [2\. Dois-je enregistrer chaque modèle séparément ?](#heading-2-dois-je-enregistrer-chaque-modele-separement)
        
    * [3\. Comment désenregistrer un modèle ?](#heading-3-comment-desenregistrer-un-modele)
        
* [Liens et ressources utiles](#heading-liens-et-ressources-utiles)
    
* [Réflexions finales](#heading-reflexions-finales)
    

## Pourquoi Django Admin est important

Django Admin est comme votre tableau de bord personnel pour le backend de votre site web. Une fois que vous avez enregistré vos modèles, vous pouvez gérer le contenu de votre application sans toucher une seule ligne de code.

Imaginez pouvoir ajouter de nouveaux articles de blog, approuver des utilisateurs, mettre à jour des listes de produits – tout cela en quelques clics. C'est la magie de Django Admin.

Sans enregistrer correctement vos modèles, vous êtes coincé à tout gérer manuellement, ce qui peut rapidement devenir compliqué.

De plus, Django Admin fait gagner des heures de temps aux développeurs. C'est l'une des raisons pour lesquelles Django est un framework si puissant.

## Comment enregistrer des modèles dans Django Admin

### Étape 1 : Assurez-vous d'avoir un modèle

Avant de pouvoir enregistrer quoi que ce soit, vous avez besoin d'un modèle. Voici un exemple super basique d'un modèle à l'intérieur d'une application Django appelée `blog`.

À l'intérieur de `blog/models.py` :

```python
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
```

Dans ce modèle :

* `title` est un champ de texte court.
    
* `body` est pour du contenu plus long.
    
* `date_created` stocke automatiquement l'heure à laquelle l'article est créé.
    

Et cette méthode `__str__` ? Elle indique simplement à Django comment afficher chaque Post dans l'Admin – elle affichera le titre de l'article au lieu de quelque chose comme `Post object (1)`.

**Astuce rapide** : Ajoutez toujours une méthode `__str__` à vos modèles. Cela rend votre interface Admin beaucoup plus propre.

### Étape 2 : Enregistrez votre modèle dans Admin

Très bien, votre modèle est prêt. Il est temps de l'enregistrer !

Ouvrez `blog/admin.py`. Lorsque vous créez une nouvelle application Django, ce fichier est vide par défaut.

Voici comment enregistrer le modèle `Post` :

```python
from django.contrib import admin
from .models import Post

admin.site.register(Post)
```

**Que se passe-t-il ici ?**

* Tout d'abord, vous importez le module admin de Django.
    
* Ensuite, vous importez votre modèle (`Post`).
    
* Enfin, vous utilisez `admin.site.register()` pour dire à Django : "Hey, je veux que ce modèle apparaisse dans le panneau d'administration."
    

Enregistrez le fichier. Maintenant, si vous allez sur votre site Admin (généralement à l'adresse `http://127.0.0.1:8000/admin`), vous verrez **Posts** listé là.

### Étape 3 : (Optionnel) Personnalisez l'apparence de votre modèle dans Admin

Par défaut, Django Admin affiche vos modèles dans un tableau très basique. Mais vous pouvez le rendre beaucoup mieux avec un peu de personnalisation.

Voici comment vous pouvez faire en sorte que les Posts affichent le titre et la date de création en un coup d'œil.

Toujours à l'intérieur de `blog/admin.py` :

```python
from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created')

admin.site.register(Post, PostAdmin)
```

Maintenant :

* `list_display` indique à Django quels champs vous voulez afficher dans la vue de liste.
    
* Vous créez une classe `PostAdmin` qui décrit comment le modèle `Post` doit se comporter dans Admin.
    
* Lorsque vous enregistrez, vous passez à la fois le modèle (`Post`) et la classe admin (`PostAdmin`).
    

**Astuce rapide** : Personnaliser votre Admin améliore votre flux de travail *beaucoup* – surtout lorsque vous gérez de nombreuses entrées.

## FAQ

### 1\. J'ai ajouté un modèle, mais il n'apparaît pas dans Admin. Que s'est-il passé ?

Assurez-vous que vous avez :

* Enregistré le modèle à l'intérieur de `admin.py`.
    
* Exécuté les migrations (`python manage.py makemigrations` et `python manage.py migrate`) si vous avez changé quelque chose dans le modèle.
    

De plus, vérifiez si l'application est listée dans votre `INSTALLED_APPS` à l'intérieur de `settings.py`.

### 2\. Dois-je enregistrer chaque modèle séparément ?

Oui. Chaque modèle que vous souhaitez gérer dans Admin doit être enregistré. Mais vous pouvez enregistrer plusieurs modèles ensemble aussi :

```python
from .models import Post, Comment, Category

admin.site.register([Post, Comment, Category])
```

### 3\. Comment désenregistrer un modèle ?

Vous pouvez utiliser :

```python
from django.contrib import admin
from .models import Post

admin.site.unregister(Post)
```

Mais honnêtement, la plupart du temps, vous arrêtez simplement de l'enregistrer si vous ne voulez plus qu'il apparaisse.

## Réflexions finales

Enregistrer des modèles dans Django Admin peut sembler une petite étape, mais cela a un impact énorme sur la façon dont vous travaillez avec vos données.

Cela transforme votre base de données en un tableau de bord convivial que tout le monde peut utiliser – même les personnes non techniques.

Une fois que vous serez à l'aise avec l'enregistrement et la personnalisation de vos modèles, vous irez plus vite et vous vous sentirez beaucoup plus en contrôle de votre application.

Maintenant, je suis curieux – **quel modèle êtes-vous le plus excité d'enregistrer dans votre Django Admin ?** Parlons-en sur [X](http://x.com/_udemezue).

### Liens et ressources utiles

* [Documentation officielle de Django – Site Admin](https://docs.djangoproject.com/en/stable/ref/contrib/admin/)
    
* [Comprendre les modèles Django (Real Python)](https://realpython.com/get-started-with-django-1/)
    
* [Tutoriel Django Girls – Introduction à Django Admin](https://tutorial.djangogirls.org/en/django_admin/)
    

Ce sont d'excellents endroits pour approfondir la personnalisation de Django Admin.