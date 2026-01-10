---
title: Comment utiliser une clé étrangère dans Django
subtitle: ''
author: Udemezue John
co_authors: []
series: null
date: '2025-04-22T14:05:27.872Z'
originalURL: https://freecodecamp.org/news/how-to-use-a-foreign-key-in-django
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1745330646960/e2fc7f1d-73f9-4e25-b870-e0928833e7a5.png
tags:
- name: Django
  slug: django
- name: Python
  slug: python
seo_title: Comment utiliser une clé étrangère dans Django
seo_desc: 'When you''re building something in Django – whether it''s a blog, a to-do
  app, or even something way more complex – at some point, you''ll want to connect
  different pieces of data.

  That’s where ForeignKey comes in. It helps link one model to another, li...'
---

Lorsque vous construisez quelque chose dans Django, qu'il s'agisse d'un blog, d'une application de liste de tâches ou même de quelque chose de bien plus complexe, à un moment donné, vous voudrez connecter différentes pièces de données.

C'est là que `ForeignKey` intervient. Il aide à lier un modèle à un autre, comme attacher un commentaire à un article, ou une commande à un client.

C'est l'une de ces choses dans Django qui peut sembler confuse au début, mais une fois que vous avez compris, vous vous demanderez comment vous avez pu construire des applications sans cela.

Alors, décomposons tout cela. Je vais vous guider à travers tout, de ce qu'est une ForeignKey, à comment l'utiliser dans votre projet Django.

## Voici ce que nous allons couvrir :

* [Qu'est-ce qu'une clé étrangère dans Django ?](#heading-questce-quune-cle-etrangere-dans-django)

* [Pourquoi utiliser une ForeignKey au lieu de stocker les IDs manuellement ?](#heading-pourquoi-utiliser-une-foreignkey-au-lieu-de-stocker-les-ids-manuellement)

* [Exemple concret : Articles de blog et commentaires](#heading-exemple-concret-articles-de-blog-et-commentaires)

* [Qu'est-ce que on_delete et pourquoi est-ce important ?](#heading-questce-que-ondelete-et-pourquoi-estce-important)

* [Comment accéder aux objets liés dans Django](#heading-comment-acceder-aux-objets-lies-dans-django)

* [Comment créer des relations de clé étrangère dans Django Admin](#heading-comment-creer-des-relations-de-cle-etrangere-dans-django-admin)

  * [Que se passe-t-il dans la base de données ?](#heading-que-se-passe-t-il-dans-la-base-de-donnees)

* [Comment interroger avec ForeignKey](#heading-comment-interroger-avec-foreignkey)

  * [Obtenir tous les commentaires pour un article avec id=1 :](#heading-obtenir-tous-les-commentaires-pour-un-article-avec-id1)

  * [Obtenir tous les articles qui ont au moins un commentaire d'un utilisateur spécifique :](#heading-obtenir-tous-les-articles-qui-ont-au-moins-un-commentaire-dun-utilisateur-specifique)

* [FAQ](#heading-faq)

  * [Une ForeignKey peut-elle être optionnelle ?](#heading-une-foreignkey-peutelle-etre-optionnelle)

  * [Une ForeignKey peut-elle pointer vers le même modèle (self) ?](#heading-une-foreignkey-peutelle-pointer-vers-le-meme-modele-self)

  * [Un modèle peut-il avoir plus d'une ForeignKey ?](#heading-un-modele-peutil-avoir-plus-dune-foreignkey)

* [Réflexions finales](#heading-reflexions-finales)

  * [Ressources supplémentaires](#heading-ressources-supplementaires)

## Qu'est-ce qu'une clé étrangère dans Django ?

En termes simples, une clé étrangère dans Django crée une relation plusieurs-à-un entre deux modèles. Cela signifie que plusieurs lignes dans une table peuvent être liées à une seule ligne dans une autre.

Par exemple :

* Un article de blog peut avoir **plusieurs commentaires**

* Un client peut avoir **plusieurs commandes**

* Un auteur peut écrire **plusieurs livres**

Si vous venez d'un environnement de tableur, pensez à cela comme à la liaison de deux feuilles à l'aide d'une colonne partagée. Dans Django, vous faites cela dans vos définitions de modèle.

## Pourquoi utiliser une ForeignKey au lieu de stocker les IDs manuellement ?

Vous pourriez vous demander, "Pourquoi ne pas simplement stocker l'ID de l'objet lié dans un champ entier simple ?"

Eh bien, vous pourriez – mais vous perdriez une tonne de puissance. Sans une ForeignKey :

* Vous n'avez pas de validation automatique que l'objet lié existe.

* Vous ne pouvez pas suivre les relations facilement dans les requêtes (par exemple, `post.comments.all()` ne serait pas possible).

* L'admin Django ne peut pas fournir de listes déroulantes ou de formulaires en ligne pour les données liées.

* Vous perdez des fonctionnalités utiles comme le comportement `on_delete` et le nommage des objets liés.

Les champs ForeignKey automatisent et renforcent ces relations, rendant votre code plus propre, plus sécurisé et plus facile à maintenir.

## Exemple concret : Articles de blog et commentaires

Disons que vous construisez un blog. Vous aurez probablement un modèle `Post` et un modèle `Comment`. Chaque commentaire doit être lié à un article spécifique.

Voici à quoi cela ressemble en code :

```python
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Commentaire par {self.author}'
```

Laissez-moi expliquer chaque partie de cela :

* `models.ForeignKey(Post, on_delete=models.CASCADE)` : Cette ligne crée la connexion. Cela signifie que chaque commentaire est lié à un article. La partie `on_delete=models.CASCADE` indique à Django de supprimer tous les commentaires liés si un article est supprimé.

* Les méthodes `__str__` facilitent simplement la lecture des choses dans l'admin ou le shell.

## Qu'est-ce que `on_delete` et pourquoi est-ce important ?

Lorsque vous créez une ForeignKey dans Django, vous devez inclure un argument `on_delete`. Cela contrôle ce qui se passe avec les lignes enfants (comme les commentaires) si la ligne parente (comme un article de blog) est supprimée.

Voici les options courantes :

* `models.CASCADE` : Supprime également les lignes enfants (comme supprimer tous les commentaires lorsqu'un article est supprimé).

* `models.PROTECT` : Empêche la suppression s'il y a des objets liés.

* `models.SET_NULL` : Définit la ForeignKey sur `NULL` au lieu de supprimer.

* `models.SET_DEFAULT` : Définit une valeur par défaut.

* `models.DO_NOTHING` : Ne fait rien (non recommandé sauf si vous savez vraiment ce que vous faites).

Je choisis généralement `CASCADE` pour les applications simples, mais cela vaut la peine d'y réfléchir en fonction de la situation.

## Comment accéder aux objets liés dans Django

Une fois que vous avez configuré la ForeignKey, Django vous donne quelques outils pratiques pour travailler avec les données liées.

Par exemple, disons que vous avez un objet article :

```python
post = Post.objects.get(id=1)
```

Vous pouvez obtenir tous les commentaires pour cet article comme ceci :

```python
comments = post.comment_set.all()
```

Le `comment_set` est automatiquement créé par Django, et vous pouvez personnaliser le nom avec `related_name` :

```python
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
```

Maintenant vous pouvez faire :

```python
post.comments.all()
```

Beaucoup plus propre, n'est-ce pas ?

## Comment créer des relations de clé étrangère dans Django Admin

L'admin Django gère bien les ForeignKeys. Si vous avez les modèles `Post` et `Comment` enregistrés dans `admin.py`, vous obtiendrez une liste déroulante dans le formulaire de commentaire pour sélectionner l'article auquel il appartient.

Vous pouvez également créer des formulaires en ligne, afin de pouvoir ajouter des commentaires tout en éditant un article. Voici un exemple rapide :

```python
from django.contrib import admin
from .models import Post, Comment

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1

class PostAdmin(admin.ModelAdmin):
    inlines = [CommentInline]

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
```

Maintenant, lorsque vous éditez un article, vous pouvez ajouter ou éditer des commentaires directement sur la même page.

### Que se passe-t-il dans la base de données ?

Django utilise une base de données relationnelle (comme PostgreSQL, MySQL ou SQLite), et ForeignKey crée une colonne dans la table de la base de données qui contient l'ID de l'objet lié.

Si vous exécutez `python manage.py makemigrations` puis `python manage.py migrate`, Django créera les tables de base de données réelles avec les relations appropriées en arrière-plan.

## Comment interroger avec ForeignKey

Vous pouvez également filtrer ou rechercher en fonction des relations ForeignKey :

### Obtenir tous les commentaires pour un article avec id=1 :

```python
Comment.objects.filter(post_id=1)
```

Ou, en utilisant l'objet article :

```python
post = Post.objects.get(id=1)
comments = Comment.objects.filter(post=post)
```

### Obtenir tous les articles qui ont au moins un commentaire d'un utilisateur spécifique :

```python
Post.objects.filter(comments__author='John')
```

Cette partie `comments__author` est grâce au `related_name='comments'` que j'ai ajouté précédemment.

## FAQ

### **Une ForeignKey peut-elle être optionnelle ?**

Oui, il suffit d'ajouter `null=True, blank=True` comme ceci :

```python
post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True, blank=True)
```

Vous pourriez vouloir cela si l'objet lié n'est pas toujours requis. Par exemple, un `Comment` pourrait *optionnellement* appartenir à un `Post`, ou une `Task` pourrait optionnellement avoir un `Project` lié. C'est utile lorsque vous construisez des brouillons, des suppressions logiques ou que vous gérez des données héritées.

### **Une ForeignKey peut-elle pointer vers le même modèle (self) ?**

Absolument. Cela s'appelle une ForeignKey autoréférentielle, souvent utilisée pour des choses comme les commentaires en fils ou les catégories.

```python
class Category(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)
```

### **Un modèle peut-il avoir plus d'une ForeignKey ?**

Totalement. Par exemple, un modèle Order pourrait avoir une ForeignKey vers un Customer, et une autre vers une ShippingAddress.

## Réflexions finales

Si vous construisez quelque chose dans Django qui traite avec plus d'un modèle, comprendre ForeignKey est essentiel. Cela rend votre application plus structurée, plus facile à interroger et bien plus puissante.

Au début, cela peut sembler beaucoup, mais une fois que vous avez construit une ou deux relations et que vous voyez tout cela fonctionner dans l'admin et vos vues, cela devient clair.

Et si quelque chose n'est toujours pas clair, c'est normal. J'ai dû construire quelques mini-projets avant que cela ne commence à sembler naturel.

### Ressources supplémentaires

* Docs Django sur [ForeignKey](https://docs.djangoproject.com/en/stable/ref/models/fields/#foreignkey)

* [Référence des champs de modèle Django](https://docs.djangoproject.com/en/stable/ref/models/fields/)

* [Écrire des modèles dans Django](https://docs.djangoproject.com/en/stable/topics/db/models/)

* [Docs Django Admin](https://docs.djangoproject.com/en/stable/ref/contrib/admin/)