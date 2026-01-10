---
title: Comment manipuler les données avec les migrations Django
subtitle: ''
author: Victoria Drake
co_authors: []
series: null
date: '2020-09-17T16:23:19.000Z'
originalURL: https://freecodecamp.org/news/how-to-manipulate-data-with-django-migrations
coverImage: https://www.freecodecamp.org/news/content/images/2020/09/cover-1.png
tags:
- name: database
  slug: database
- name: Django
  slug: django
- name: Python
  slug: python
seo_title: Comment manipuler les données avec les migrations Django
seo_desc: 'In this article, we''ll learn how to update Django models and manipulate
  existing data using migrations.

  Successful applications that are growing are a lovely problem to have. As a product
  develops, it tends to accumulate complication the way your wee...'
---

Dans cet article, nous allons apprendre comment mettre à jour les modèles Django et manipuler les données existantes en utilisant les migrations.

Les applications réussies qui sont en croissance sont un problème agréable à avoir. À mesure qu'un produit se développe, il tend à accumuler des complications de la même manière que votre projet de gâteau du week-end accumule des couches de glaçage. 

Heureusement, Django, mon framework préféré avec tout inclus, gère assez bien la complexité.

Les modèles Django aident les humains à travailler avec les données d'une manière qui a du sens pour nos cerveaux. Et le framework offre de nombreuses classes que vous pouvez hériter pour vous aider à développer rapidement une application robuste à partir de zéro. 

En ce qui concerne le développement sur des applications Django existantes, il y a aussi une fonctionnalité pour cela.

Dans cet article, nous allons couvrir comment utiliser les migrations Django pour mettre à jour vos modèles et votre base de données existants.

## Ce qui se cache sous le capot

Les migrations Django sont des fichiers Python qui vous aident à ajouter et à modifier des éléments dans vos tables de base de données pour refléter les changements dans vos modèles Django. 

Pour comprendre comment les migrations Django vous aident à travailler avec les données, il peut être utile de comprendre les structures sous-jacentes avec lesquelles nous travaillons.

### Qu'est-ce qu'une table de base de données ?

Si vous avez déjà posé les yeux sur un tableur, vous êtes déjà en grande partie sur la voie de la compréhension d'une table de base de données. 

Dans une base de données relationnelle, par exemple une base de données PostgreSQL, vous pouvez vous attendre à voir des données organisées en colonnes et en lignes. Une table de base de données relationnelle peut avoir un nombre défini de colonnes et un nombre quelconque de lignes.

Dans Django, chaque modèle est sa propre table. Par exemple, voici un modèle Django :

```python
from django.db import models


class Lunch(models.Model):
    left_side = models.CharField(max_length=100, null=True)
    center = models.CharField(max_length=100, null=True)
    right_side = models.CharField(max_length=100, null=True)

```

Chaque champ est une colonne, et chaque ligne est une instance d'objet Django de ce modèle. 

Voici une représentation d'une table de base de données pour le modèle Django "Lunch" ci-dessus. Dans la base de données, son nom serait `lunch_table`.

| id | left\_side | center | right\_side |
| --- | --- | --- | --- |
| 1 | Fork | Plate | Spoon |

Le modèle `Lunch` a trois champs : `left_side`, `center`, et `right_side`. Une instance de l'objet `Lunch` aurait "Fork" pour `left_side`, une "Plate" pour `center`, et "Spoon" pour `right_side`. 

Django [ajoute automatiquement un champ `id`](https://docs.djangoproject.com/en/3.1/topics/db/models/#automatic-primary-key-fields) si vous ne spécifiez pas de clé primaire.

Si vous vouliez changer le nom de votre modèle Lunch, vous le feriez dans votre code `models.py`. 

Par exemple, changez "Lunch" en "Dinner", puis [exécutez `python manage.py makemigrations`](https://docs.djangoproject.com/en/3.1/ref/django-admin/#makemigrations). Vous verrez :

```text
python manage.py makemigrations
Did you rename the backend.Lunch model to Dinner? [y/N] y
Migrations for 'backend':
  backend/migrations/0003_auto_20200922_2331.py
    - Rename model Lunch to Dinner

```

Django génère automatiquement les fichiers de migration appropriés. La ligne pertinente du fichier de migration généré dans ce cas ressemblerait à :

```python
migrations.RenameModel(old_name="Lunch", new_name="Dinner"),

```

Cette opération renommerait notre modèle "Lunch" en "Dinner" tout en gardant tout le reste identique. 

Mais que faire si vous vouliez également changer la structure de la table de base de données elle-même, son schéma, ainsi que vous assurer que les données existantes se retrouvent au bon endroit sur votre table Dinner ?

![Image](https://www.freecodecamp.org/news/content/images/2020/09/cover-2.png)
_Dessin animé terrible par l'auteur._

Explorons comment transformer notre modèle Lunch en un modèle Dinner qui ressemble à ceci :

```python
from django.db import models


class Dinner(models.Model):
    top_left = models.CharField(max_length=100, null=True)
    top_center = models.CharField(max_length=100, null=True)
    top_right = models.CharField(max_length=100, null=True)
    bottom_left = models.CharField(max_length=100, null=True)
    bottom_center = models.CharField(max_length=100, null=True)
    bottom_right = models.CharField(max_length=100, null=True)

```

...avec une table de base de données qui ressemblerait à ceci :

| id | top\_left | top\_center | top\_right | bottom\_left | bottom\_center | bottom\_right |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Bread plate | Spoon | Glass | Fork | Plate | Knife |

## Comment manipuler les données avec les migrations Django

Avant de commencer à manipuler vos données, il est toujours bon de créer une sauvegarde de votre base de données que vous pouvez restaurer en cas de problème. 

Il existe diverses façons de faire cela selon la base de données que vous utilisez. Vous pouvez généralement trouver des instructions en recherchant `<nom de votre base de données>` et des mots-clés comme `backup`, `recovery`, ou `snapshot`.

Afin de concevoir votre migration, il est utile de vous familiariser avec les [opérations de migration disponibles](https://docs.djangoproject.com/en/3.1/ref/migration-operations/). 

Les migrations sont exécutées étape par étape, et chaque opération est une variante de l'ajout, de la suppression ou de la modification de données. Comme un puzzle stratégique, il est important d'apporter des modifications aux modèles une étape à la fois afin que les migrations générées aient le résultat correct.

Nous avons déjà renommé notre modèle avec succès. Maintenant, nous allons renommer les champs qui contiennent les données que nous voulons conserver :

```python
class Dinner(models.Model):
    bottom_left = models.CharField(max_length=100, null=True)
    bottom_center = models.CharField(max_length=100, null=True)
    top_center = models.CharField(max_length=100, null=True)

```

Django est parfois assez intelligent pour déterminer correctement les anciens et nouveaux noms de champs. Vous serez invité à confirmer :

```text
python manage.py makemigrations
Did you rename dinner.center to dinner.bottom_center (a CharField)? [y/N] y
Did you rename dinner.left_side to dinner.bottom_left (a CharField)? [y/N] y
Did you rename dinner.right_side to dinner.top_center (a CharField)? [y/N] y
Migrations for 'backend':
  backend/migrations/0004_auto_20200914_2345.py
    - Rename field center on dinner to bottom_center
    - Rename field left_side on dinner to bottom_left
    - Rename field right_side on dinner to top_center

```

Dans certains cas, vous voudrez essayer de renommer le champ et d'exécuter `makemigrations` un à la fois.

Maintenant que les champs existants ont été migrés vers leurs nouveaux noms, ajoutez les champs restants au modèle :

```python
class Dinner(models.Model):
    top_left = models.CharField(max_length=100, null=True)
    top_center = models.CharField(max_length=100, null=True)
    top_right = models.CharField(max_length=100, null=True)
    bottom_left = models.CharField(max_length=100, null=True)
    bottom_center = models.CharField(max_length=100, null=True)
    bottom_right = models.CharField(max_length=100, null=True)

```

L'exécution de `makemigrations` à nouveau nous donne maintenant :

```text
python manage.py makemigrations
Migrations for 'backend':
  backend/migrations/0005_auto_20200914_2351.py
    - Add field bottom_right to dinner
    - Add field top_left to dinner
    - Add field top_right to dinner

```

Vous avez terminé ! En générant des migrations Django, vous avez réussi à configurer votre `dinner_table` et à déplacer les données existantes à leur nouvel emplacement.

## Complexité supplémentaire

Vous remarquerez que nos modèles Lunch et Dinner ne sont pas très complexes. Parmi les nombreuses [options de champs de modèle de Django](https://docs.djangoproject.com/en/3.1/ref/models/fields/#field-types), nous utilisons uniquement `CharField`. Nous avons également défini `null=True` pour permettre à Django de stocker les valeurs vides comme `NULL` dans la base de données.

Les migrations Django peuvent gérer une complexité supplémentaire, telle que le changement de types de champs, et si une valeur vide ou nulle est autorisée. Je garde la [référence des champs de modèle de Django](https://docs.djangoproject.com/en/3.1/ref/models/fields/#) à portée de main lorsque je travaille avec différents types de données et cas d'utilisation.

## Migrations démystifiées

J'espère que cet article vous a aidé à mieux comprendre les migrations Django et leur fonctionnement !

Maintenant que vous pouvez changer les modèles et manipuler les données existantes dans votre application Django, assurez-vous d'utiliser vos pouvoirs avec sagesse. 

Sauvegardez votre base de données, recherchez et planifiez vos migrations, et exécutez toujours des tests avant de travailler avec les données des clients. En faisant cela, vous avez le potentiel d'enrichir votre application et de gérer des niveaux de complexité raisonnables.