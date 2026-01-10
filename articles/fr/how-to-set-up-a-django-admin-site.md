---
title: Comment configurer un site d'administration Django
subtitle: ''
author: Victoria (Burah) Poromon
co_authors: []
series: null
date: '2024-03-04T14:19:57.000Z'
originalURL: https://freecodecamp.org/news/how-to-set-up-a-django-admin-site
coverImage: https://www.freecodecamp.org/news/content/images/2024/03/django-admin-cover.jpg
tags:
- name: Django
  slug: django
- name: Python
  slug: python
seo_title: Comment configurer un site d'administration Django
seo_desc: "The Django admin site provides developers with a simple yet effective way\
  \ to manage their models and build sustainable projects. It allows you to create,\
  \ view, update, and remove records from your applications. \nIn this article, you\
  \ will learn how to..."
---

Le site d'administration Django offre aux développeurs un moyen simple mais efficace de gérer leurs modèles et de construire des projets durables. Il vous permet de créer, de visualiser, de mettre à jour et de supprimer des enregistrements de vos applications. 

Dans cet article, vous apprendrez à enregistrer vos `models` avec votre site d'administration, à créer votre compte superutilisateur, à vous connecter et à utiliser votre site, et à personnaliser votre site d'administration.

En tant que développeur, si vous envisagez de construire un projet Django ou si vous êtes en train de construire un projet, la création du site d'administration Django est l'étape suivante après la création de votre modèle Django.

## Comment enregistrer vos modèles

Enregistrez vos modèles dans votre fichier `admin.py`. En enregistrant vos `models`, vous permettez à Django de générer des formulaires basés sur les informations du modèle. Cela sert également de forme de documentation pour votre projet et vous permet de gérer les données de manière sécurisée.

Voici comment enregistrer vos `models` :

```python
from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(BookInstance)
admin.site.register(Language)
```

La première ligne importe `django.contrib.admin`. Elle active l'administration Django pour votre projet et vous permet d'y accéder à une URL spécifique (/admin/) dans votre navigateur web.

La deuxième ligne du code importe vos `models`, tandis que les quatre dernières lignes de code appellent `admin.site.register` pour enregistrer chacun d'eux.

Vos `models` peuvent être plus ou moins nombreux, selon la complexité de votre projet.

## Comment créer un superutilisateur

Un compte superutilisateur vous permet de vous connecter au site d'administration, de créer des enregistrements et de gérer des objets. 

La commande suivante créera un compte superutilisateur avec un accès complet au site d'administration et toutes les permissions nécessaires :

```bash
# Pour macOS/Linux
python3 manage.py createsuperuser

# Pour Windows
py manage.py createsuperuser
```

Vous recevrez une invite pour entrer un nom d'utilisateur, un email et un mot de passe. Une fois cette commande terminée, vous aurez un compte superutilisateur, et vous pourrez redémarrer votre serveur de développement et tester vos identifiants de connexion en utilisant la commande suivante :

```bash
# Pour macOS/Linux
python3 manage.py runserver

# Pour Windows
py manage.py runserver
```

Lorsque vous exécutez ces commandes, assurez-vous d'être dans le même répertoire que `manage.py`.

## Comment se connecter et utiliser votre site

Pour vous connecter à votre site, ouvrez votre URL `/admin` (ou [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)) dans votre navigateur. Vous verrez une page qui ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Screenshot--23-.png)
_La page de connexion de l'administration Django._

Entrez les détails de votre compte superutilisateur, cliquez sur connexion, et vous verrez une nouvelle page qui ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Screenshot--24-.png)
_La page d'accueil de l'administration Django._

La nouvelle page ci-dessus est le site d'administration Django qui affiche tous les modèles enregistrés.  
Cliquez sur le lien ajouter à côté de chaque modèle pour commencer à créer vos enregistrements.

Après avoir ajouté un enregistrement à un modèle, cliquez sur `SAVE`, `Save and add another`, ou `Save and continue editing` pour sauvegarder votre enregistrement. Votre écran devrait ressembler à celui ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Screenshot--26-.png)
_Les 3 options de sauvegarde sur le site d'administration Django._

Les captures d'écran ci-dessus ne montrent que des exemples de l'apparence du site d'administration Django. Selon les besoins de votre projet, vos modèles et champs peuvent être différents des exemples de cet article.

## Comment personnaliser votre site d'administration

Django fait un excellent travail en créant votre site d'administration avec les informations des modèles que vous enregistrez. Il vous permet également de personnaliser votre interface d'administration pour répondre aux besoins de votre projet.

Les sections suivantes vous montreront comment effectuer ces personnalisations.

### Comment enregistrer une classe `ModelAdmin`

Une classe `ModelAdmin` représente un modèle dans votre interface d'administration. En enregistrant cette classe, vous pouvez personnaliser le comportement d'un modèle spécifique dans votre interface d'administration. Cela garde également votre base de code organisée et facilite sa maintenance :

```python
# Commentez votre enregistrement original
# admin.site.register(Author)

# Définissez la classe admin
class AuthorAdmin(admin.ModelAdmin):
    pass

# Enregistrez la classe admin avec le modèle qu'elle représente
admin.site.register(Author, AuthorAdmin)
```

L'extrait de code ci-dessus définit et enregistre une classe admin vide pour le modèle Author.

Toujours commenter votre enregistrement original avant d'enregistrer une classe `ModelAdmin`.

### Comment personnaliser votre vue de liste

En considérant le modèle ci-dessus, si vous avez plusieurs auteurs ou si vous devez afficher des informations supplémentaires sur vos auteurs, la méthode `list_display` vous permet de personnaliser votre vue de liste.

Voici un exemple de la façon de personnaliser votre interface en utilisant la méthode `list_display` :

```python
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death',)

```

L'extrait de code ci-dessus montre la classe `AuthorAdmin` et un tuple des noms de champs que vous souhaitez afficher dans la liste, dans l'ordre que vous requérez.

Vous devez toujours spécifier ces champs dans votre modèle Django (fichier `models.py`). Sinon, ils ne seront pas affichés.

Le résultat devrait être une interface comme celle ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Screenshot--27-.png)
_Le résultat de la personnalisation de la vue de liste._

En utilisant cette méthode, vous pouvez personnaliser la vue de liste de n'importe quel modèle pour répondre aux besoins de votre projet.

### Comment personnaliser la vue de détail

Django dispose les vues de détail verticalement par défaut, dans l'ordre où elles sont définies dans le modèle. Mais vous pouvez changer cela pour répondre à vos besoins, et décider quels champs vous souhaitez afficher ou exclure. 

Vous pouvez faire cela en ajoutant l'attribut `field` à votre classe admin. Par exemple :

```python
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')

    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
```

L'attribut field dans l'extrait de code ci-dessus change l'ordre de vos champs. `first_name` vient maintenant avant `last_name`. Les champs s'affichent verticalement par défaut, mais en les regroupant dans un tuple (dans le champ des dates), ils s'affichent maintenant horizontalement.

La vue de détail de l'auteur devrait maintenant apparaître comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Screenshot--28-.png)
_Le résultat de la personnalisation de la vue de détail._

De plus, vous pouvez utiliser l'attribut `exclude` pour exclure/supprimer des champs du formulaire.

## Conclusion

La configuration de votre site d'administration Django est importante pour gérer vos modèles efficacement dans votre projet Django. Savoir comment utiliser et personnaliser votre interface Django améliore la qualité et la maintenabilité de votre projet.

Cet article décrit comment configurer votre site d'administration et comment vous pouvez le personnaliser pour répondre aux besoins de votre projet. Bon codage !