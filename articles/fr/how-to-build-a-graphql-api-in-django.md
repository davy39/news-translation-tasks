---
title: Comment construire une API GraphQL dans Django
subtitle: ''
author: Udemezue John
co_authors: []
series: null
date: '2025-04-16T13:22:37.122Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-graphql-api-in-django
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1744809748866/9a626cc9-4e67-4d63-bdde-1834180db645.png
tags:
- name: Django
  slug: django
- name: Python
  slug: python
- name: GraphQL
  slug: graphql
seo_title: Comment construire une API GraphQL dans Django
seo_desc: 'If you''re building an app with Django and thinking about using GraphQL,
  you''re not alone.

  REST has been the go-to for years, but GraphQL is quickly becoming a favourite option
  for developers who want more flexibility and less back-and-forth between f...'
---

Si vous construisez une application avec Django et que vous envisagez d'utiliser GraphQL, vous n'êtes pas seul.

REST a été la référence pendant des années, mais GraphQL devient rapidement une option favorite pour les développeurs qui veulent plus de flexibilité et moins d'allers-retours entre le frontend et le backend.

J'ai passé beaucoup de temps à travailler avec Django et à explorer différentes façons de rendre les API plus fluides, et je comprends pourquoi les gens passent à GraphQL.

Vous demandez exactement les données dont vous avez besoin, et vous obtenez exactement cela. Pas de superflu, pas de multiples requêtes pour assembler les données — c'est comme commander dans un menu et obtenir exactement ce que vous vouliez, à chaque fois.

Alors, si vous êtes curieux de savoir comment construire une API GraphQL en utilisant Django, je vous couvre.

Je vais vous guider à travers ce qu'est GraphQL, pourquoi il pourrait être une meilleure option que REST dans certains cas, et comment vous pouvez commencer à partir de zéro — même si vous n'êtes pas (encore) un expert GraphQL.

### Voici ce que nous allons couvrir :

1. [Qu'est-ce que GraphQL et pourquoi est-ce important ?](#heading-quest-ce-que-graphql-et-pourquoi-est-ce-important)

2. [Ce dont vous aurez besoin avant de commencer](#heading-ce-dont-vous-aurez-besoin-avant-de-commencer)

3. [Comment construire une API GraphQL dans Django](#heading-comment-construire-une-api-graphql-dans-django)

4. [Comment ajouter des mutations (aussi connu comme l'écriture de données)](#heading-comment-ajouter-des-mutations-aussi-connu-comme-lecriture-de-donnees)

5. [Parcours du code : Créer un post via une mutation dans GraphQL](#heading-parcours-du-code-creer-un-post-via-une-mutation-dans-graphql)

6. [Comment un client utiliserait cela](#heading-comment-un-client-utiliserait-cela)

7. [Avantages et inconvénients de l'utilisation de GraphQL dans Django](#heading-avantages-et-inconvenients-de-lutilisation-de-graphql-dans-django)

8. [FAQ](#heading-faq)

9. [Quelle est la suite ?](#heading-quelle-est-la-suite)

10. [Réflexions finales](#heading-reflexions-finales)

## Qu'est-ce que GraphQL et pourquoi est-ce important ?

GraphQL est un langage de requête pour les API — et plus important encore, c'est un runtime pour exécuter ces requêtes avec vos données.

Il a été développé par Facebook en 2012 et rendu public en 2015. Depuis, il a été utilisé par des entreprises comme GitHub, Shopify, Twitter et Pinterest.

Contrairement à REST, où vous devez souvent faire plusieurs requêtes pour obtenir toutes les données dont vous avez besoin, GraphQL vous permet de récupérer toutes vos données en une seule requête.

C'est une grande avancée, surtout pour les applications mobiles ou les réseaux lents où moins de requêtes signifient de meilleures performances.

Supposons que vous vouliez le nom d'un utilisateur, sa photo de profil et ses 3 derniers articles de blog. Avec REST, vous pourriez avoir besoin de frapper 2-3 points de terminaison différents. Avec GraphQL ? Une requête, c'est fait.

C'est aussi génial pour les développeurs frontend car ils peuvent façonner les données qu'ils reçoivent sans attendre que les développeurs backend créent de nouveaux points de terminaison.

## Ce dont vous aurez besoin avant de commencer

Avant de vous lancer, voici ce que vous devriez déjà avoir :

* Connaissance de base de Django (modèles, vues, etc.)

* Python installé (3.8+ est le meilleur)

* Un projet Django configuré

* pip ou pipenv pour la gestion des paquets

Si vous commencez à partir de zéro, vous pouvez créer un nouveau projet Django avec :

```bash
django-admin startproject monprojet
cd monprojet
python manage.py startapp monapp
```

## Comment construire une API GraphQL dans Django

Commençons.

### 1. Installer Graphene-Django

Graphene est la bibliothèque la plus populaire pour utiliser GraphQL avec Python. Pour Django spécifiquement, il existe un package appelé `graphene-django`.

Vous pouvez l'installer comme ceci :

```bash
pip install graphene-django
```

Ensuite, ajoutez-le à votre `INSTALLED_APPS` :

```python
INSTALLED_APPS = [
    ...
    'graphene_django',
]
```

### 2. Ajouter un modèle simple

Voici un modèle rapide avec lequel travailler. Dans `monapp/models.py` :

```python
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
```

Ensuite, exécutez vos migrations :

```bash
python manage.py makemigrations
python manage.py migrate
```

### 3. Créer un schéma

Dans `monapp/schema.py`, commencez avec :

```python
import graphene
from graphene_django.types import DjangoObjectType
from .models import Post

class PostType(DjangoObjectType):
    class Meta:
        model = Post

class Query(graphene.ObjectType):
    all_posts = graphene.List(PostType)

    def resolve_all_posts(root, info):
        return Post.objects.all()

schema = graphene.Schema(query=Query)
```

Ensuite, dans les paramètres de votre projet Django, ajoutez :

```python
GRAPHENE = {
    "SCHEMA": "monapp.schema.schema"
}
```

Et enfin, dans votre `urls.py` :

```python
from django.urls import path
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True))),
]
```

Maintenant, visitez `http://localhost:8000/graphql` et essayez cette requête :

```graphql
{
  allPosts {
    title
    content
    published
  }
}
```

Boom. Vous venez d'interroger votre base de données en utilisant GraphQL.

Voici à quoi devrait ressembler votre interface GraphQL.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1744454293412/8820e7dd-ff86-4c7d-9c8c-ec21dc43b09b.png align="center")

## Comment ajouter des mutations (aussi connu comme l'écriture de données)

GraphQL n'est pas seulement pour lire des données. Vous pouvez également créer, mettre à jour et supprimer. Voici comment ajouter une mutation pour créer un post :

Dans `monapp/schema.py` :

```python
class CreatePost(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        content = graphene.String(required=True)

    post = graphene.Field(PostType)

    def mutate(self, info, title, content):
        post = Post(title=title, content=content)
        post.save()
        return CreatePost(post=post)

class Mutation(graphene.ObjectType):
    create_post = CreatePost.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
```

Maintenant, dans l'interface GraphiQL, vous pouvez exécuter :

```graphql
mutation {
  createPost(title: "Mon premier post", content: "Bonjour GraphQL !") {
    post {
      id
      title
    }
  }
}
```

Plutôt propre, non ?

## Parcours du code : Créer un post via une mutation dans GraphQL

Laissez-moi vous guider à travers le code, expliquer ce qu'il fait et comment GraphQL le rend possible.

### Étape 1 : La classe de mutation `CreatePost`

```python
class CreatePost(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        content = graphene.String(required=True)

    post = graphene.Field(PostType)

    def mutate(self, info, title, content):
        post = Post(title=title, content=content)
        post.save()
        return CreatePost(post=post)
```

Voici ce qui se passe dans cette partie :

* `graphene.Mutation` : Cela définit une **mutation** personnalisée, qui dans GraphQL est la façon dont nous modifions les données côté serveur (similaire à POST, PUT et DELETE dans REST).

* `class Arguments` : Pensez à cela comme la partie "entrée" de la mutation. Nous exigeons un `title` et un `content`, tous deux sous forme de chaînes. Ce sont les éléments que le client doit fournir lors de l'appel de la mutation.

* `post = graphene.Field(PostType)` : Cela définit le type de retour de la mutation. Dans ce cas, une fois qu'un post est créé, nous le retournons en utilisant un type GraphQL personnalisé appelé `PostType`.

* `mutate(self, info, title, content)` : Cette méthode est appelée lorsque la mutation est exécutée. À l'intérieur :

  * Nous créons une nouvelle instance du modèle `Post`.

  * Nous l'enregistrons dans la base de données.

  * Nous retournons le résultat de la mutation sous forme d'objet `CreatePost` avec le nouveau post attaché.

* Cela garde la logique serrée, lisible et testable — un excellent exemple de conception d'API propre.

### Étape 2 : Intégration de la mutation dans le schéma

```python
class Mutation(graphene.ObjectType):
    create_post = CreatePost.Field()
```

C'est là que nous **enregistrons** notre mutation. Dans GraphQL, toutes les opérations (requêtes et mutations) doivent faire partie du schéma. En ajoutant `create_post` à la classe `Mutation`, nous l'exposons au point de terminaison GraphQL.

### Étape 3 : Le schéma final

```python
schema = graphene.Schema(query=Query, mutation=Mutation)
```

Dans ce code :

* Nous créons un nouveau `graphene.Schema`.

* Nous passons une classe `Query` (supposée être définie ailleurs pour les opérations de lecture) et notre classe `Mutation` pour les opérations d'écriture.

C'est l'équivalent GraphQL de la configuration des [`urls.py`](http://urls.py) de Django — c'est ce qui est exposé aux clients lorsqu'ils accèdent à votre point de terminaison `/graphql/`.

## Comment un client utiliserait cela

Un client (frontend ou outil de test d'API comme Insomnia/Postman) enverrait une mutation comme ceci :

```python
mutation {
  createPost(title: "GraphQL est génial", content: "Construisons des API avec !") {
    post {
      id
      title
      content
    }
  }
}
```

Et obtiendrait une réponse comme :

```python
{
  "data": {
    "createPost": {
      "post": {
        "id": "1",
        "title": "GraphQL est génial",
        "content": "Construisons des API avec !"
      }
    }
  }
}
```

## Bonus : Pourquoi c'est génial pour les développeurs

* Les **équipes frontend** peuvent maintenant construire des formulaires et voir instantanément la structure de la réponse.

* Les **développeurs backend** définissent ce qui est autorisé et gèrent uniquement la logique nécessaire.

* **Plus de sur-récupération ou de sous-récupération de données** — GraphQL vous donne exactement ce que vous demandez.

* Facile à tester, déboguer et mettre à l'échelle.

## Assurez-vous d'avoir les éléments suivants en place

* Assurez-vous d'avoir installé `graphene-django`.

* Ajoutez `'graphene_django'` à votre `INSTALLED_APPS`.

* Configurez le schéma dans le fichier [`urls.py`](http://urls.py) de votre projet Django.

```python
from django.urls import path
from graphene_django.views import GraphQLView
from monapp.schema import schema

urlpatterns = [
    path("graphql/", GraphQLView.as_view(graphiql=True, schema=schema)),
]
```

## Avantages et inconvénients de l'utilisation de GraphQL dans Django

### Avantages :

* Requêtes flexibles

* Génial pour les développeurs frontend

* Moins d'appels API

* Schéma fortement typé

* Meilleure performance sur les réseaux lents

### Inconvénients :

* Courbe d'apprentissage légèrement plus raide

* Plus de configuration que REST

* Peut être excessif pour les API simples

## FAQ

### GraphQL est-il meilleur que REST ?

Cela dépend. GraphQL vous donne plus de contrôle et de flexibilité, mais REST est plus facile à mettre en cache et plus simple à configurer pour les petits projets.

### Graphene est-il le seul moyen d'utiliser GraphQL avec Django ?

Non. Vous pouvez également utiliser Ariadne ou Strawberry. Mais Graphene est le plus mature et le plus largement utilisé pour l'instant.

### GraphQL fonctionne-t-il bien avec Django REST Framework ?

Ils peuvent coexister. Si vous avez déjà une API REST et que vous souhaitez ajouter GraphQL, vous n'avez pas besoin de tout jeter.

## Quelle est la suite ?

Une fois que vous avez maîtrisé les bases, vous pouvez :

* Ajouter une authentification avec JWT ou des sessions

* Utiliser Relay si vous avez besoin de pagination et de filtrage

* Connecter votre API GraphQL à React, Vue ou tout autre frontend

## Réflexions finales

Si vous utilisez Django depuis un certain temps et que vous souhaitez donner à votre API un peu plus de puissance et de flexibilité, GraphQL vaut 100 % le coup d'œil.

### Ressources supplémentaires

* [Documentation Graphene-Django](https://docs.graphene-python.org/projects/django/en/latest/)

* [Documentation officielle GraphQL](https://graphql.org/learn/)

* [Ariadne – Une bibliothèque GraphQL "schema-first" pour Python](https://ariadnegraphql.org/)

* [GraphQL vs REST : Différences clés](https://www.apollographql.com/blog/graphql/basics/graphql-vs-rest/)