---
title: Comment créer des modèles dans votre projet Django
subtitle: ''
author: Udemezue John
co_authors: []
series: null
date: '2025-04-25T19:47:47.633Z'
originalURL: https://freecodecamp.org/news/how-to-create-models-in-your-django-project
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1745610452559/e009644b-bfef-4e43-9f1b-5f2e4deebdfa.png
tags:
- name: Python
  slug: python
- name: Django
  slug: django
seo_title: Comment créer des modèles dans votre projet Django
seo_desc: 'If you''re building something with Django, there''s one thing you can''t
  skip: creating models. Models are the heart of any Django app. They define how your
  data is structured, how it''s stored in the database, and how Django can interact
  with it.

  Now, i...'
---

Si vous construisez quelque chose avec Django, il y a une chose que vous ne pouvez pas sauter : créer des modèles. Les modèles sont le cœur de toute application Django. Ils définissent comment vos données sont structurées, comment elles sont stockées dans la base de données et comment Django peut interagir avec elles.

Maintenant, si vous êtes nouveau dans Django ou si vous essayez encore de comprendre les bases, ne vous inquiétez pas. J'ai été là aussi. Les modèles peuvent sembler un peu intimidants au début, mais ils sont assez simples une fois que vous voyez comment ils fonctionnent.

Je vais vous guider à travers tout cela, étape par étape, afin qu'à la fin de cet article, vous sachiez non seulement comment créer des modèles, mais aussi comment les utiliser dans des projets réels.

Commençons.

### Voici ce que nous allons couvrir :

1. [Qu'est-ce qu'un modèle dans Django ?](#heading-quest-ce-quun-modele-dans-django)

2. [Comment créer des modèles dans Django](#heading-comment-creer-des-modeles-dans-django)

   * [Étape 1 : Démarrer un projet Django (si ce n'est pas déjà fait)](#heading-etape-1-demarrer-un-projet-django-si-ce-nest-pas-deja-fait)

   * [Étape 2 : Définir votre modèle](#heading-etape-2-definir-votre-modele)

   * [Étape 3 : Enregistrer l'application et créer la base de données](#heading-etape-3-enregistrer-lapplication-et-creer-la-base-de-donnees)

   * [Étape 4 : Créer et utiliser des objets](#heading-etape-4-creer-et-utiliser-des-objets)

3. [Fonctionnalités supplémentaires des modèles que vous utiliserez](#heading-fonctionnalites-supplementaires-des-modeles-que-vous-utiliserez)

   * [1. Valeurs par défaut](#heading-1-valeurs-par-defaut)

   * [2. Horodatages automatiques](#heading-2-horodatages-automatiques)

   * [3. Options Meta du modèle](#heading-3-options-meta-du-modele)

4. [Utilisation des modèles dans l'admin Django](#heading-utilisation-des-modeles-dans-ladmin-django)

5. [FAQ](#heading-faq)

6. [Réflexions finales](#heading-reflexions-finales)

## Qu'est-ce qu'un modèle dans Django ?

Un modèle dans Django est simplement une classe Python qui indique à Django comment vous voulez que vos données soient structurées. Django s'occupe de la partie difficile (communiquer avec la base de données), afin que vous puissiez vous concentrer sur la description de vos données en code Python simple.

Voici un exemple rapide d'un modèle de base :

```python
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    published_date = models.DateField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
```

Permettez-moi de le décomposer :

* `title` et `author` sont simplement des morceaux de texte courts, donc j'utilise `CharField`.

* `published_date` est une date - assez simple, c'est à cela que sert `DateField`.

* `price` est un nombre avec des décimales, donc `DecimalField` fait le travail.

Chaque ligne décrit une partie des données que je veux stocker pour chaque livre. Simple, non ?

## Comment créer des modèles dans Django

### Étape 1 : Démarrer un projet Django (si ce n'est pas déjà fait)

Si vous êtes tout nouveau, vous avez d'abord besoin d'un projet Django :

```bash
django-admin startproject mysite
cd mysite
python manage.py startapp books
```

Maintenant, vous avez une application Django appelée `books` où vous pouvez mettre vos modèles.

### Étape 2 : Définir votre modèle

À l'intérieur de votre dossier d'application (`books`), ouvrez `models.py`. C'est là que vous définirez votre modèle.

Voici un exemple un peu plus réaliste :

```python
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    birthdate = models.DateField()

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    summary = models.TextField()
    isbn = models.CharField(max_length=13, unique=True)
    published = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title
```

Ce qui se passe ici :

* J'ai créé deux modèles : `Author` et `Book`.

* `Book` a une relation avec `Author` en utilisant `ForeignKey`. Cela signifie qu'un auteur peut avoir plusieurs livres.

* J'utilise `__str__()` pour retourner un nom agréable lorsque je regarde les objets dans l'admin Django.

### Étape 3 : Enregistrer l'application et créer la base de données

Avant que Django puisse utiliser vos modèles, assurez-vous que votre application est ajoutée aux paramètres du projet.

Ouvrez `mysite/settings.py` et trouvez la liste `INSTALLED_APPS`. Ajoutez `'books',` à celle-ci :

```python
INSTALLED_APPS = [
    # autres applications
    'books',
]
```

Maintenant, exécutez les migrations pour créer les tables de la base de données pour vos modèles :

```bash
python manage.py makemigrations
python manage.py migrate
```

C'est ainsi que Django transforme votre code Python en tables de base de données réelles. La première commande crée un fichier de migration (basiquement, des instructions pour la base de données), et la seconde l'applique.

### Étape 4 : Créer et utiliser des objets

Maintenant, vous pouvez utiliser ces modèles dans votre code. Ouvrez le shell Django :

```bash
python manage.py shell
```

Puis essayez ceci :

```python
from books.models import Author, Book
from datetime import date

# Créer un auteur
jane = Author.objects.create(name="Jane Austen", birthdate=date(1775, 12, 16))

# Créer un livre
book = Book.objects.create(
    title="Pride and Prejudice",
    author=jane,
    summary="Un roman sur les manières et le mariage en Angleterre au début du 19ème siècle.",
    isbn="1234567890123",
    published=date(1813, 1, 28),
    price=9.99
)

print(book)
```

Django enregistrera automatiquement ces données dans votre base de données.

## Fonctionnalités supplémentaires des modèles que vous utiliserez

### 1. Valeurs par défaut

Vous pouvez donner à un champ une valeur par défaut :

```python
is_published = models.BooleanField(default=False)
```

### 2. Horodatages automatiques

Ceux-ci sont super utiles pour suivre les heures de création ou de mise à jour :

```python
created_at = models.DateTimeField(auto_now_add=True)
updated_at = models.DateTimeField(auto_now=True)
```

### 3. Options Meta du modèle

Vous pouvez ajouter class Meta pour personnaliser des choses comme le tri par défaut :

```python
class Book(models.Model):
    # champs...

    class Meta:
        ordering = ['published']
```

## Utilisation des modèles dans l'admin Django

Le panneau d'administration intégré de Django est l'une des meilleures parties du framework. Mais vos modèles n'y apparaîtront pas à moins que vous ne les enregistriez.

Dans `books/admin.py`, ajoutez :

```python
from django.contrib import admin
from .models import Author, Book

admin.site.register(Author)
admin.site.register(Book)
```

Maintenant, exécutez :

```bash
python manage.py createsuperuser
```

Puis allez sur [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin), connectez-vous, et voilà - vos modèles sont là, avec une interface complète.

## FAQ

### **Puis-je modifier un modèle après l'avoir créé ?**

Oui, mais vous devrez créer une nouvelle migration :

```bash
python manage.py makemigrations
python manage.py migrate
```

### **Quelles bases de données fonctionnent avec Django ?**

Django fonctionne avec PostgreSQL, MySQL, SQLite (par défaut), et plus encore. La plupart des gens commencent avec SQLite lorsqu'ils apprennent car c'est facile et ça fonctionne directement.

### **Quelle est la différence entre CharField et TextField ?**

Utilisez `CharField` pour du texte court avec une longueur maximale (comme un nom ou un titre). Utilisez `TextField` pour du texte plus long (comme un article de blog ou un résumé).

## Réflexions finales

Une fois que vous comprenez les modèles, le reste de Django commence à s'emboîter. Tout - les formulaires, les vues, les templates - finit par se connecter au modèle. C'est ainsi que votre application stocke et travaille avec des données réelles.

La meilleure façon d'apprendre est de construire quelque chose. Commencez petit, peut-être un catalogue de livres, un gestionnaire de tâches ou un blog personnel. Ajoutez des modèles un à la fois et jouez avec eux dans l'admin.

### Ressources supplémentaires

* [Documentation officielle de Django - Modèles](https://docs.djangoproject.com/en/stable/topics/db/models/)

* [Référence des champs de modèle Django](https://docs.djangoproject.com/en/stable/ref/models/fields/)

* [Tutoriel Django simple - Mozilla Developer Network](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django)