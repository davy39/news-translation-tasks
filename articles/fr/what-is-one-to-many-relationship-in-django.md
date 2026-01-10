---
title: Comment utiliser une clé étrangère pour créer des relations plusieurs-à-un
  dans Django
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-07-06T20:33:56.000Z'
originalURL: https://freecodecamp.org/news/what-is-one-to-many-relationship-in-django
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/Add-a-subheading--5-.png
tags:
- name: Django
  slug: django
- name: Python
  slug: python
seo_title: Comment utiliser une clé étrangère pour créer des relations plusieurs-à-un
  dans Django
seo_desc: 'By Sampurna Chapagain

  In Django, there are three main types of relationships: one-to-one, many-to-one,
  and many-to-many.

  In this article, I will explain the many-to-one relationship in Django. If you are
  a beginner with some knowledge about Django pr...'
---

Par Sampurna Chapagain

Dans Django, il existe trois types principaux de relations : un-à-un, plusieurs-à-un et plusieurs-à-plusieurs.

Dans cet article, je vais expliquer la relation plusieurs-à-un dans Django. Si vous êtes débutant avec quelques connaissances sur la configuration de projet Django ou même si vous avez une certaine expérience dans Django, vous pouvez suivre cet article.

Les relations plusieurs-à-un sont parfois appelées relations un-à-plusieurs. Comme vous le verrez ci-dessous, ce sont des termes liés.

## Qu'est-ce qu'une relation plusieurs-à-un ?

Une relation `plusieurs-à-un` est un type de relation où plusieurs enregistrements dans une table sont associés à un seul enregistrement dans une autre table.

Supposons que nous avons deux tables dans une base de données : `Department` (Département) et `Employee` (Employé). La relation entre `Department` et `Employee` est une relation `un-à-plusieurs`. Un `département` peut avoir plusieurs `employés` et chaque `employé` appartient à un `département`.

Et, la relation entre les `employés` et les `départements` est une relation `plusieurs-à-un`.

Cela peut être illustré avec le diagramme ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2023/07/Add-a-little-bit-of-body-text.png)
_Diagramme pour illustrer la relation plusieurs-à-un_

Par exemple, un département `Account` (Comptabilité) peut avoir plusieurs `employés` (un-à-plusieurs) et ces `employés` appartiennent tous au département `account` (plusieurs-à-un).

## Comment créer des modèles pour les relations plusieurs-à-un

Pour ce tutoriel, l'application aura deux modèles : `Department` et `Employee`.

Alors, commençons à ajouter du code pour les modèles.

```python
from django.db import models

class Department(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Employee(models.Model):
    name=models.CharField(max_length=70)
    address=models.CharField(max_length=90)
    department=models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
```

Le modèle `Department` ne contient qu'un seul champ, `name` (nom).

Le modèle `Employee` contient les champs `name` (nom) et `address` (adresse), ainsi qu'un champ `ForeignKey` (`department`) qui référence le modèle `Department`. C'est la raison pour laquelle il passe `Department` comme premier argument.

Le deuxième argument, `on_delete`, spécifie le comportement à adopter lorsque l'objet de référence est supprimé, qui est `Department` dans ce cas. L'option `models.CASCADE` signifie que si un objet `Department` est supprimé, tous les objets `Employee` associés seront également supprimés.

### Qu'est-ce qu'une clé étrangère dans un modèle Django ?

La clé étrangère est utilisée pour connecter deux tables et établit la relation `plusieurs-à-un`. Vous pouvez définir une `clé étrangère` dans un modèle Django en utilisant le champ `models.ForeignKey`. Et ce champ `ForeignKey` prend au moins deux arguments :

```python
department = models.ForeignKey(Department, on_delete=models.CASCADE)
```

Nous avons déjà discuté de ces deux arguments dans la section ci-dessus.

Et vous pouvez également passer d'autres arguments comme `related_name` avec une valeur qui vous permet d'accéder aux `clés étrangères` définies dans vos modèles Django en sens inverse.

### Migrations de la base de données

Maintenant, vous pouvez effectuer les migrations en utilisant la commande `makemigrations`.

```python
manage.py makemigrations
```

Ensuite, vous pouvez apporter des modifications à la base de données en utilisant la commande `migrate`.

```python
manage.py migrate
```

## Comment interagir avec les modèles

Maintenant, jouons un peu avec le shell pour comprendre les concepts principaux des relations `plusieurs-à-un`.

Tout d'abord, vous devez exécuter la commande `shell` :

![Image](https://www.freecodecamp.org/news/content/images/2023/07/Screenshot-from-2023-07-03-18-26-26.png)

Ensuite, importez les modèles dans le `shell`. Ici, le nom de l'application est `company` (entreprise).

![Image](https://www.freecodecamp.org/news/content/images/2023/07/Screenshot-from-2023-07-03-18-23-46.png)

Et maintenant, créons quelques départements.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/Screenshot-from-2023-07-03-18-23-57.png)

Maintenant, vous pouvez effectuer une requête `Department.objects.all()` pour retourner un `QuerySet` qui contient tous les objets `Department` dans la base de données.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/Screenshot-from-2023-07-03-18-24-18.png)

À l'étape suivante, créons quelques employés, `emp1`, `emp2` et `emp3` :

![Image](https://www.freecodecamp.org/news/content/images/2023/07/Screenshot-from-2023-07-03-18-24-28.png)

Ici, vous passez l'instance de l'objet `department` pour le champ `department`.

Si vous souhaitez récupérer tous les `employees` pour un `department` spécifique, qui est `programming` dans cet exemple, vous pouvez utiliser la requête suivante :

![Image](https://www.freecodecamp.org/news/content/images/2023/07/Screenshot-from-2023-07-03-18-24-38.png)

Vous pouvez également utiliser n'importe quel objet `employee` pour récupérer un enregistrement à partir de `department`. Ici, il utilise l'objet `emp1`.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/Screenshot-from-2023-07-03-18-40-45.png)

## Conclusion

Les relations plusieurs-à-un sont largement utilisées dans les applications Django.

Elles aident à créer des relations entre les modèles et facilitent l'exécution des requêtes de base de données.

J'espère que vous avez trouvé cet article utile.

Vous pouvez me trouver sur [Twitter](https://twitter.com/saam_codes) pour du contenu quotidien concernant le développement Web.

Bon codage en Python !