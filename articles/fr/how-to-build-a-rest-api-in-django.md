---
title: Comment créer une API REST dans Django
subtitle: ''
author: Udemezue John
co_authors: []
series: null
date: '2025-04-16T14:53:12.442Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-rest-api-in-django
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1744814822505/5195929b-c1d8-4c9e-a12b-44697db44c5b.png
tags:
- name: Django
  slug: django
- name: Python
  slug: python
- name: REST API
  slug: rest-api
seo_title: Comment créer une API REST dans Django
seo_desc: 'If you’re building a web or mobile app, chances are you’re going to need
  a way to send and receive data between your app and a server.

  That’s where REST APIs come in. They help apps talk to each other – kind of like
  a waiter taking your order and bri...'
---

Si vous construisez une application web ou mobile, il est probable que vous aurez besoin d'un moyen d'envoyer et de recevoir des données entre votre application et un serveur.

C'est là que les API REST interviennent. Elles aident les applications à communiquer entre elles - un peu comme un serveur qui prend votre commande et vous apporte votre nourriture. Et si vous utilisez Django, vous êtes déjà à moitié là.

Django est l'un des frameworks web les plus populaires. Il est rapide, sécurisé et rempli d'outils utiles. Combinez-le avec Django REST Framework (DRF), et vous avez tout ce dont vous avez besoin pour construire une API REST solide sans passer des semaines à tout comprendre.

Dans ce guide, je vais vous guider à travers tout le processus de création d'une API REST dans Django à partir de zéro.

### Ce que nous allons couvrir :

1. [Qu'est-ce qu'une API REST ?](#heading-quest-ce-quune-api-rest)

2. [Outils dont vous aurez besoin](#heading-outils-dont-vous-aurez-besoin)

3. [Comment créer une API REST dans Django](#heading-comment-creer-une-api-rest-dans-django)

   * [Étape 1 : Configurer votre projet Django](#heading-etape-1-configurer-votre-projet-django)

   * [Étape 2 : Créer un modèle](#heading-etape-2-creer-un-modele)

   * [Étape 3 : Créer un serialiseur](#heading-etape-3-creer-un-serialiseur)

   * [Étape 4 : Créer les vues](#heading-etape-4-creer-les-vues)

   * [Étape 5 : Configurer les URLs](#heading-etape-5-configurer-les-urls)

   * [Étape 6 : Testez-la !](#heading-etape-6-testez-la)

4. [Permissions DRF](#heading-permissions-drf)

   * [Permissions intégrées courantes](#heading-permissions-integrees-courantes)

   * [Permissions personnalisées](#heading-permissions-personnalisees)

   * [Combinaison de permissions](#heading-combinaison-de-permissions)

5. [FAQ](#heading-faq)

6. [Réflexions finales](#heading-reflexions-finales)

## Qu'est-ce qu'une API REST ?

Avant de commencer, clarifions une chose : qu'est-ce qu'une API REST ?

Une API REST (abréviation de "Representational State Transfer") est un moyen pour deux systèmes - comme un site web et un serveur - de communiquer entre eux en utilisant des méthodes HTTP standard comme GET, POST, PUT et DELETE.

Disons que vous avez une application de liste de tâches. Vous voulez :

* **Obtenir** une liste de tâches

* **Ajouter** une nouvelle tâche

* **Mettre à jour** une tâche

* **Supprimer** une tâche

Vous pouvez faire tout cela via une API REST. C'est comme configurer votre propre menu de commandes que d'autres applications (ou votre frontend) peuvent utiliser pour travailler avec vos données.

## Outils dont vous aurez besoin :

Voici ce que vous allez utiliser dans ce tutoriel :

* **Python** (de préférence 3.8+)

* **Django** (framework web)

* **Django REST Framework (DRF)** (pour construire des APIs)

* **Postman ou curl** (pour les tests)

Vous pouvez installer DRF avec :

```bash
pip install djangorestframework
```

## **Comment créer une API REST dans Django**

Voici comment commencer :

### Étape 1 : Configurer votre projet Django

Si ce n'est pas déjà fait, commencez un nouveau projet Django :

```bash
django-admin startproject monprojet
cd monprojet
python manage.py startapp api
```

* `django-admin startproject monprojet` - Crée un nouveau projet Django nommé `monprojet`, qui contient les fichiers de configuration pour votre site.

* `cd monprojet` - Déplacez-vous dans votre nouveau répertoire de projet.

* `python` [`manage.py`](http://manage.py) `startapp api` - Crée une nouvelle application Django nommée `api` où vos modèles, vues et logique d'API résideront.

Maintenant, ajoutez `'rest_framework'` et `'api'` à votre `INSTALLED_APPS` dans `settings.py` :

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'api',
]
```

* `rest_framework` est le Django REST Framework - il vous donne des outils pour créer facilement des APIs.

* `'api'` indique à Django de chercher dans le dossier `api` pour les modèles, vues, etc.

### Étape 2 : Créer un modèle

Créons un modèle simple - une liste de tâches.

Dans `api/models.py` :

```python
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
```

* `title` : Un court texte (comme "Acheter des courses"). `CharField` est utilisé pour les chaînes de caractères.

* `completed` : Un booléen (Vrai ou Faux) pour marquer si une tâche est terminée.

* `__str__` : Cette méthode spéciale retourne une version chaîne du modèle lorsqu'il est imprimé - utile pour le débogage et le panneau d'administration.

Ensuite, exécutez :

```bash
python manage.py makemigrations
python manage.py migrate
```

* `makemigrations` : Prépare les changements pour le schéma de la base de données.

* `migrate` : Applique ces changements à la base de données réelle.

### Étape 3 : Créer un serialiseur

Les serialiseurs transforment votre modèle Django en JSON (le format de données utilisé dans les APIs) et vice versa.

Dans `api/serializers.py` :

```python
from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
```

* Les **Serializers** convertissent les instances de modèle (comme une `Task`) en **JSON** et vice versa, afin qu'ils puissent être envoyés sur le web.

* `ModelSerializer` est un raccourci qui gère automatiquement la plupart des choses basées sur votre modèle.

* `fields = '__all__'` signifie inclure tous les champs du modèle (title et completed).

### Étape 4 : Créer les vues

C'est ici que la logique réside. Vous pouvez utiliser des vues basées sur des classes ou des fonctions. Utilisons des vues basées sur des classes en utilisant les `generics` de DRF.

Dans `api/views.py` :

```python
from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer

class TaskListCreate(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
```

Ce sont des **vues génériques basées sur des classes** fournies par Django REST Framework pour vous faire gagner du temps.

1. `TaskListCreate` :

   * Gère les requêtes GET pour lister toutes les tâches.

   * Gère les requêtes POST pour créer de nouvelles tâches.

2. `TaskDetail` :

   * Gère GET pour une tâche, PUT/PATCH pour la mise à jour, et DELETE pour supprimer une tâche

### Étape 5 : Configurer les URLs

Tout d'abord, créez un fichier `urls.py` dans le dossier `api` (s'il n'existe pas).

Dans `api/urls.py` :

```python
from django.urls import path
from .views import TaskListCreate, TaskDetail

urlpatterns = [
    path('tasks/', TaskListCreate.as_view(), name='task-list'),
    path('tasks/<int:pk>/', TaskDetail.as_view(), name='task-detail'),
]
```

* `tasks/` : La route pour accéder ou créer des tâches.

* `tasks/<int:pk>/` : La route pour obtenir, mettre à jour ou supprimer une seule tâche par sa clé primaire (`pk`).

Ensuite, dans votre `myproject/`[`urls.py`](http://urls.py) :

Maintenant, intégrez cela dans le `urls.py` principal de votre dossier de projet :

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]
```

### Étape 6 : Testez-la !

Démarrez le serveur :

```bash
python manage.py runserver
```

Ouvrez Postman ou curl et essayez d'appeler ces endpoints :

* `GET /api/tasks/` - obtenir toutes les tâches

* `POST /api/tasks/` - créer une nouvelle tâche

* `GET /api/tasks/1/` - obtenir une tâche spécifique

* `PUT /api/tasks/1/` - mettre à jour une tâche

* `DELETE /api/tasks/1/` - supprimer une tâche

Et voilà - vous avez une API REST fonctionnelle.

Cette configuration vous donne une API REST entièrement fonctionnelle avec seulement quelques lignes de code, grâce à Django REST Framework. Vous devriez maintenant comprendre :

* Comment les modèles définissent la structure de votre base de données

* Comment les serialiseurs transforment les modèles en JSON et vice versa

* Comment les vues contrôlent le comportement de l'API (get, post, update, delete)

* Comment le routage des URLs connecte vos vues aux requêtes web

## Permissions DRF

Actuellement, n'importe qui peut utiliser votre API. Mais que faire si vous voulez que seuls certains utilisateurs y aient accès ?

DRF vous offre des moyens simples de gérer cela. Par exemple, pour rendre une API accessible uniquement aux utilisateurs connectés :

```python
from rest_framework.permissions import IsAuthenticated

class TaskListCreate(generics.ListCreateAPIView):
    ...
    permission_classes = [IsAuthenticated]
```

Il existe d'autres permissions que vous pouvez utiliser, comme `IsAdminUser`, des permissions personnalisées, par exemple.

Décortiquons cela et approfondissons les **permissions** dans Django REST Framework (DRF), y compris :

### Qu'est-ce que les permissions dans DRF ?

Les permissions dans DRF contrôlent **qui** peut accéder à votre API et **quelles actions** ils peuvent effectuer (lire, écrire, supprimer, etc.).

Elles sont appliquées par vue (ou viewset), et elles sont vérifiées après l'authentification, ce qui signifie qu'elles s'appuient sur la vérification de l'authentification de l'utilisateur.

### Permissions intégrées courantes

DRF vous offre quelques classes de permissions intégrées très utiles :

#### 1. `IsAuthenticated`

Cela garantit que seuls les utilisateurs connectés peuvent accéder à la vue :

```python
from rest_framework.permissions import IsAuthenticated

class TaskListCreate(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
```

Seuls les utilisateurs qui ont été authentifiés (par exemple, via une connexion de session ou un jeton) pourront lister ou créer des tâches. Les autres recevront une réponse `403 Forbidden`.

#### 2. `IsAdminUser`

Autorise uniquement l'accès si `user.is_staff` est `True`.

```python
from rest_framework.permissions import IsAdminUser

class AdminOnlyView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
```

Seuls les utilisateurs administrateurs (généralement définis via l'admin Django ou le statut superutilisateur) peuvent accéder à cette vue.

#### 3. `AllowAny`

Autorise **tous** les utilisateurs, même non authentifiés. C'est le comportement par défaut pour les APIs ouvertes comme les pages d'inscription.

```python
from rest_framework.permissions import AllowAny

class PublicSignupView(generics.CreateAPIView):
    serializer_class = SignupSerializer
    permission_classes = [AllowAny]
```

#### 4. `IsAuthenticatedOrReadOnly`

Les utilisateurs authentifiés peuvent lire et écrire, les utilisateurs non authentifiés ne peuvent que lire (GET, HEAD, OPTIONS).

```python
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class ArticleView(generics.RetrieveUpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
```

**Cas d'utilisation :** Idéal pour les blogs ou les APIs d'articles où le public peut lire mais seuls les utilisateurs enregistrés peuvent écrire/mettre à jour.

### Permissions personnalisées

Vous voulez plus de contrôle ? Vous pouvez créer vos propres permissions en sous-classant `BasePermission`.

#### Exemple : Autoriser uniquement les propriétaires d'un objet à l'éditer

```python
from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user
```

Ensuite, utilisez-le comme ceci :

```python
class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsOwner]
```

* Tout d'abord, un utilisateur doit être connecté (`IsAuthenticated`).

* Ensuite, seul le propriétaire de cette `Task` spécifique peut la consulter, la mettre à jour ou la supprimer.

### Combinaison de permissions

Vous pouvez combiner plusieurs classes de permissions, et toutes doivent retourner `True` pour que l'accès soit accordé.

```python
permission_classes = [IsAuthenticated, IsAdminUser]
```

Cela signifie : l'utilisateur doit être à la fois authentifié et administrateur.

#### TL;DR

| Permission | Qui obtient l'accès ? |
| --- | --- |
| `AllowAny` | Tout le monde (même les utilisateurs non connectés) |
| `IsAuthenticated` | Seuls les utilisateurs connectés |
| `IsAdminUser` | Seuls les utilisateurs administrateurs/staff |
| `IsAuthenticatedOrReadOnly` | Lecture : tout le monde / Écriture : seuls les utilisateurs connectés |
| `Custom Permissions` | Vos règles (par exemple, seulement les propriétaires) |

## FAQ

### **Ai-je besoin de Django REST Framework pour créer une API dans Django ?**

Techniquement, non - mais DRF vous facilite grandement la vie. Sans DRF, vous devriez gérer manuellement des choses comme :

* L'analyse et la validation des requêtes JSON

* L'écriture de vues pour sérialiser les objets Python en JSON

* La gestion des codes de statut HTTP et des réponses

* La gestion de l'authentification et des permissions par vous-même

En bref, vous réinventeriez la roue - mais DRF fait tout cela pour vous avec beaucoup moins de code.

### **Puis-je utiliser cette API avec un frontend React ou Vue ?**

Absolument. Votre API Django enverra et recevra des données au format JSON - ce qui est exactement ce pour quoi les frameworks frontend modernes comme React et Vue sont conçus pour travailler. Assurez-vous simplement de gérer correctement le CORS (Cross-Origin Resource Sharing).

### **Comment rendre mon API plus rapide ?**

Vous pouvez :

* Utiliser le **caching** pour stocker les réponses fréquentes

* Activer la **pagination** pour réduire la charge de données

* Explorer les **vues asynchrones** (Django 3.1+ supporte l'async) pour un I/O plus rapide

DRF offre également des outils intégrés pour la pagination, la limitation de débit et d'autres optimisations de performance.

## Réflexions finales

Construire une API REST dans Django peut sembler une tâche ardue, mais ce n'est qu'une série de petites étapes gérables.

Une fois que vous l'avez fait une fois, cela devient beaucoup plus facile la fois suivante. De plus, l'utilisation de Django REST Framework vous fait gagner un temps précieux - vous ne réinventez pas la roue à chaque fois.

### Ressources supplémentaires

Vous voulez continuer à apprendre ? Voici quelques bonnes ressources pour approfondir :

* [Documentation officielle de Django REST Framework](https://www.django-rest-framework.org/)

* [Documentation officielle de Django](https://docs.djangoproject.com/en/stable/)

* [Simple JWT pour l'authentification par jeton](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)

* [Testez votre API avec Postman](https://www.postman.com/)

* [Guide Django API de Real Python](https://realpython.com/django-rest-framework-quick-start/)