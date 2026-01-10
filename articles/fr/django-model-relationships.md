---
title: Comment définir les relations entre les modèles Django
subtitle: ''
author: Damilola Oladele
co_authors: []
series: null
date: '2023-03-20T16:05:18.000Z'
originalURL: https://freecodecamp.org/news/django-model-relationships
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/Blog-Banner-560x315-px-1.png
tags:
- name: database
  slug: database
- name: Django
  slug: django
- name: Python
  slug: python
seo_title: Comment définir les relations entre les modèles Django
seo_desc: 'Django is a free and open-source web framework written in Python. It helps
  with rapid web development and provides out-of-the-box web security.

  Websites must be able to store and retrieve data from databases. Django makes provisions
  for this. By defa...'
---

[Django](https://www.djangoproject.com/) est un Framework web libre et open-source écrit en Python. Il facilite le développement web rapide et offre une sécurité web prête à l'emploi.

Les sites web doivent être capables de stocker et de récupérer des données à partir de bases de données. Django prévoit des dispositions à cet effet. Par défaut, Django exploite un système de gestion de base de données relationnelle (SGBDR).

> Une base de données relationnelle est un type de base de données qui stocke et fournit l'accès à des points de données liés les uns aux autres. Les bases de données relationnelles sont basées sur le modèle relationnel, une manière intuitive et simple de représenter les données dans des tables. Dans une base de données relationnelle, chaque ligne de la table est un enregistrement avec un identifiant unique appelé clé. [(Source : Oracle Cloud)](https://www.oracle.com/ng/database/what-is-a-relational-database/#:~:text=The%20software%20used%20to%20store,storage%2C%20access%2C%20and%20performance.)

Un avantage majeur d'un système de gestion de base de données relationnelle est de pouvoir définir les types de relations entre les différentes données contenues dans les différentes tables de votre base de données.

Ce tutoriel vous montre comment définir les relations entre vos [modèles](https://docs.djangoproject.com/en/3.2/topics/db/models/) Django. Pour tirer le meilleur parti de ce tutoriel, vous devriez avoir une compréhension de base du Framework web Django, en particulier de la structure des fichiers Django et des [modèles](https://docs.djangoproject.com/en/3.2/topics/db/models/).

## **Différents types de relations de modèles dans Django**

Chaque [modèle](https://docs.djangoproject.com/en/3.2/topics/db/models/) dans une application [Django](https://www.djangoproject.com/) représente une table de base de données. Cela signifie que vous pouvez définir le type de relation que vous souhaitez entre les différents modèles de votre application Django.

Django prend en charge trois types principaux de relations entre ses modèles. Ils sont les suivants :

### **Relation un-à-un**

Une relation **un-à-un** signifie qu'un enregistrement dans une table est lié à un seul enregistrement dans une autre table.

Par exemple, si vous avez un modèle Django qui définit les utilisateurs, ce modèle peut alors avoir une relation un-à-un avec un autre modèle Django qui définit les profils des utilisateurs. Dans ce scénario, un utilisateur ne peut avoir qu'un seul profil et un profil ne peut être associé qu'à un seul utilisateur.

Le diagramme suivant illustre une relation **un-à-un** :

![diagramme indiquant une relation un-à-un](https://www.freecodecamp.org/news/content/images/2023/03/Untitled-drawing--5--2.png align="left")

*Un diagramme montrant une relation un-à-un entre un modèle User et un modèle Profile.*

Django vous fournit `OneToOneField`**,** qui aide à définir une relation un-à-un entre deux modèles différents.

Le code suivant vous montre comment définir une relation **un-à-un** dans Django. Allez dans votre `<app>/models.py` et écrivez le code suivant :

```python
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)

class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.PROTECT,
        primary_key=True,
    )
    language = models.CharField(max_length=50)
    email = models.EmailField(max_length=70,blank=True,unique=True)

    def __str__(self):
        return str(self.email)
```

Voyons ce qui se passe dans le code ci-dessus :

1. La ligne une importe le sous-module `models` du module `django.db`.
    
2. La ligne trois définit un modèle Django nommé `User`.
    
3. La ligne quatre définit une propriété `name` au sein du modèle `User`, et le mot-clé `CharField` est la manière de définir du texte avec un nombre limité de caractères.
    
4. Les lignes six et sept constituent une méthode spéciale au sein du modèle `User` et renvoient une représentation sous forme de chaîne de caractères du modèle `User` qui inclut la propriété `name`.
    
5. La ligne neuf définit un modèle Django nommé `Profile`.
    
6. La ligne dix définit une relation **un-à-un** entre le modèle `Profile` et le modèle `User` en utilisant le mot-clé `OneToOneField`.
    
7. Les lignes onze et douze définissent les propriétés `language` et `email` au sein du modèle `Profile`.
    
8. Les lignes douze et treize constituent une méthode spéciale au sein du modèle `Profile` et renvoient une représentation sous forme de chaîne de caractères du modèle `Profile` qui inclut la propriété `email`.
    

### **Relation plusieurs-à-un**

Dans une relation **plusieurs-à-un**, un enregistrement dans une table est lié à plusieurs enregistrements dans une autre table. Certaines ressources désignent une relation **plusieurs-à-un** comme une relation *un-à-plusieurs*. Ces deux termes signifient la même chose.

Un exemple de relation un-à-plusieurs est la relation entre un auteur et ses livres publiés. Alors qu'un auteur peut avoir plus d'un livre à son nom, il est moins courant de trouver un livre avec plus d'un auteur. Vous pouvez voir ce genre de relation comme une relation parent-enfant.

Le diagramme suivant illustre une relation **un-à-plusieurs** :

![diagramme indiquant une relation un-à-plusieurs](https://www.freecodecamp.org/news/content/images/2023/03/Untitled-drawing-1.png align="left")

*Un diagramme montrant une relation un-à-plusieurs entre un modèle Author et un modèle Book.*

Django vous fournit `ForeignKey`, qui aide à définir une relation **plusieurs-à-un** entre deux modèles différents.

Le code suivant vous montre comment définir une relation **plusieurs-à-un** dans Django. Allez dans votre `<app>/models.py` et écrivez le code suivant :

```python
from django.db import models

class Author(models.Model): 
    name = models.CharField(max_length=50, blank=False, unique=True)

    def __str__(self):
        return str(self.name)
    
class Book(models.Model):
    author = models.ForeignKey(
        Author,
        on_delete=models.PROTECT,
        blank=False
    )

    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
```

Ce code est similaire au code du premier exemple. Cependant, à la ligne dix ici, le mot-clé `ForeignKey` est ce que vous utilisez pour définir une relation plusieurs-à-un entre deux modèles Django. Dans ce cas, le modèle actuel aura une relation **plusieurs-à-un** avec le modèle `Author`.

### **Relation plusieurs-à-plusieurs**

Dans une relation **plusieurs-à-plusieurs**, plusieurs enregistrements dans une table sont liés à de nombreux enregistrements dans une autre table. Par exemple, vous pouvez avoir un modèle de collection dans votre application, dans lequel une collection contient de nombreux livres. De la même manière, un livre peut appartenir à plusieurs collections.

Le diagramme suivant illustre une relation **plusieurs-à-plusieurs** :

![diagramme indiquant une relation plusieurs-à-plusieurs](https://www.freecodecamp.org/news/content/images/2023/03/Untitled-drawing--3-.png align="left")

*Un diagramme montrant une relation plusieurs-à-plusieurs entre un modèle Collection et un modèle Book.*

Django vous fournit un [`ManyToManyField`](https://docs.djangoproject.com/en/4.1/ref/models/fields/#django.db.models.ManyToManyField) qui aide à définir une relation **plusieurs-à-plusieurs** entre deux modèles différents.

Le code suivant vous montre comment définir une relation plusieurs-à-plusieurs dans Django. Allez dans votre `<app>/models.py` et saisissez le code suivant :

```python
from django.db import models

class Collection(models.Model):
  name = models.CharField(max_length=50)
  
  def __str__(self):
        return str(self.name)
    
class Book(models.Model):
  collection = models.ManyToManyField(Collection)
  
  title = models.CharField(max_length=100)
  
  def __str__(self):
        return str(self.title)
```

Dans cet exemple de code, le mot-clé `ManyToManyField` à la ligne 10 est ce que vous utilisez pour définir une relation **plusieurs-à-plusieurs** entre les modèles `Collection` et `Book`.

## **Conclusion**

Bien que ce tutoriel explique les bases des relations de modèles Django pour vous aider à acquérir une compréhension fondamentale, les projets réels peuvent devenir plus complexes.

La complexité des relations de vos modèles Django dépend de la complexité de votre application. Ainsi, avant de construire vos applications, il est important de planifier les relations de votre base de données. Faire cela vous fait gagner beaucoup de temps et d'efforts par rapport à la découverte de problèmes et à la nécessité de revenir en arrière plus tard.