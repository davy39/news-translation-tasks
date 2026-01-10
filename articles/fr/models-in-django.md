---
title: Comment effectuer des opérations CRUD avec les modèles Django
subtitle: ''
author: Chepkirui Dorothy
co_authors: []
series: null
date: '2024-01-18T16:10:49.000Z'
originalURL: https://freecodecamp.org/news/models-in-django
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/coding-924920.jpg
tags:
- name: Django
  slug: django
- name: Python
  slug: python
seo_title: Comment effectuer des opérations CRUD avec les modèles Django
seo_desc: 'Django is a super useful tool for building web applications with Python.
  It follows the Model-View-Template (MVT) architecture, which is a popular design
  pattern for building web apps.

  In the MVT architecture, the Model refers to the internal represe...'
---

Django est un outil super utile pour construire des applications web avec Python. Il suit l'architecture Model-View-Template (MVT), qui est un modèle de conception populaire pour construire des applications web.

Dans l'architecture MVT, le Model fait référence à la représentation interne des informations stockées, la View est responsable du traitement des requêtes utilisateur et du retour des réponses appropriées, et le Template est responsable du rendu des données reçues de la View.

Ce guide se concentre sur la partie Model de l'architecture, qui est le composant central de votre application et où vous commencez généralement lorsque vous concevez vos applications. Le Model est responsable de la représentation interne de vos données et fournit une interface pour interagir directement avec la base de données.

Dans ce tutoriel, vous apprendrez à utiliser le shell interactif de Django pour créer, lire, mettre à jour et supprimer des objets. Vous apprendrez également à enregistrer des modèles dans l'interface d'administration, ce qui est utile pour concevoir des bases de données bien organisées pour vos projets Django.

Ces compétences vous permettront de gérer vos projets plus efficacement et de garantir leur bon fonctionnement.

### Prérequis

Pour tirer le meilleur parti de ce tutoriel, vous aurez besoin d'une compréhension de base de Python et Django.

## Comment installer le projet

Pour vous aider à comprendre les concepts de ce tutoriel, vous allez développer une simple application 'todo'.

Pour commencer, créez un nouveau répertoire où vous allez héberger le projet, puis changez de répertoire.

Une fois dans le dossier, installez `virtualenv`, un outil pour établir des environnements Python isolés.

```bash
pip install virtualenv
virtualenv venv
source venv/bin/activate
```

`pip install virtualenv` installe l'outil nécessaire. `virtualenv venv` crée un environnement virtuel appelé venv. Enfin, `source venv/bin/activate` active l'environnement virtuel, permettant un développement Python isolé dans l'environnement désigné.

N'hésitez pas à remplacer "venv" par le nom que vous avez choisi lors de la création de l'environnement virtuel.

Assurez-vous que Django est installé. Si ce n'est pas le cas, installez-le via la ligne de commande comme ceci :

```bash
pip install django
```

Démarrez un projet en utilisant la commande suivante :

```bash
django-admin startproject todoproject
```

Changez de répertoire pour le répertoire du projet, `todoproject`, puis créez une nouvelle application.

```bash
cd todoproject
python manage.py startapp todoapp

```

Ensuite, incluez le nom de l'application dans la liste `INSTALLED_APPS` dans `settings.py`. Dans votre éditeur de code, naviguez vers le fichier `settings.py`.

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'todoapp' # nouvelle application
]

```

## Modèles Django

Un [modèle](https://docs.djangoproject.com/en/5.0/topics/db/models/) est comme l'expert de référence pour toutes vos données dans Django. C'est comme un plan détaillé qui indique quelles informations vous souhaitez stocker, comment les stocker et comment elles peuvent être récupérées.

L'application todo stockera des tâches. Vous allez la garder simple en ne stockant que le titre de la tâche à faire et son statut de complétion – c'est-à-dire si la tâche a été faite ou non. Ouvrez le fichier `models.py` dans votre éditeur de texte et ajoutez le code suivant :

```python
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
```

Dans ce modèle super simple :

* `Task` est le nom du modèle.
* `title` est un champ de type `CharField` avec une longueur maximale de 100 caractères. Ce champ est adapté pour stocker du texte court.
* `completed` est un champ de type `BooleanField` avec une valeur par défaut de `False`. Ce champ est un booléen (Vrai/Faux). La valeur par défaut est définie sur `False`, en supposant que les tâches commencent par défaut comme non complétées.

La partie principale d'un modèle est la liste des choses qu'il stocke (appelées champs). `title` et `completed` sont des champs, qui sont des types de champs `BooleanField` et `CharField`.

D'autres exemples de types de champs que vous pouvez utiliser incluent :

* `AutoField` : un `IntegerField` qui s'incrémente automatiquement.
* `BooleanField` : représente des valeurs vrai/faux.
* `CharField` : stocke des valeurs basées sur du texte.
* `DateField` : représente une date en utilisant une instance `datetime.date`.
* `DateTimeField` : représente la date et l'heure en utilisant une instance `datetime.datetime`.
* `DecimalField` : représente un nombre décimal à précision fixe en utilisant une instance `Decimal`.
* `EmailField` : un `CharField` validant la valeur comme une adresse email valide.
* `ImageField` : hérite de `FileField`, garantissant que les objets téléchargés sont des images valides.
* `IntegerField` : stocke des valeurs entières dans une plage sûre.
* `SlugField` : représente une étiquette courte pour quelque chose, généralement utilisée dans les URLs.
* `TextField` : un grand champ de texte.
* `TimeField` : représente l'heure en utilisant une instance `datetime.time`.
* `URLField` : un `CharField` pour les URLs.

D'autres types de champs expliquent la relation entre les tables :

* `ForeignKey` : représente une relation plusieurs-à-un.
* `ManyToManyField` : représente une relation plusieurs-à-plusieurs.
* `OneToOneField` : signifie une relation un-à-un. Essentiellement, c'est similaire à une `ForeignKey` avec `unique=True`, mais le côté "inverse" de la relation donne directement un seul objet.

Pour synchroniser votre base de données avec les dernières modifications de vos modèles Django, vous devez exécuter les migrations. Assurez-vous d'être dans le même répertoire que le fichier `manage.py`, puis exécutez les commandes suivantes :

```bash
python manage.py makemigrations
python manage.py migrate

```

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-from-2024-01-12-14-48-39.png)
_création des migrations_

Enregistrez vos modèles dans le fichier `admin.py`. Cela permet aux administrateurs de visualiser, ajouter, modifier et supprimer des instances du modèle `Task` via l'interface d'administration de Django. C'est une manière pratique d'interagir avec vos données pendant le développement et les tests.

```python
#admin.py
from django.contrib import admin
from .models import Task
# Enregistrez vos modèles ici.

admin.site.register(Task)
```

Vous devez créer un `superuser` afin d'accéder à l'interface d'administration de Django. Dans le terminal, exécutez la commande suivante :

```python
python manage.py createsuperuser
```

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-from-2024-01-12-14-52-19.png)
_création d'un superutilisateur_

Suivez les instructions, et vous devriez avoir un compte superutilisateur pour accéder à l'interface d'administration.

## Le shell Django

Vous écriviez généralement votre logique dans une vue, mais comme nous voulons faire plus d'expériences, vous allez utiliser le shell Django. C'est un outil puissant et polyvalent qui améliore l'expérience de développement et de test de vos projets Django. Le shell fournit également un environnement dynamique et interactif pour travailler avec votre code, vos données et vos modèles.

Pour accéder au shell, exécutez la commande suivante depuis le répertoire du projet :

```bash
python manage.py shell
```

Commencez par importer le modèle Task.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-from-2024-01-12-15-15-57.png)
_importation du modèle dans le shell Django_

Les opérations de base effectuées sur un modèle seront généralement la création, la lecture, la mise à jour et la suppression – d'où le nom d'application CRUD. Vous apprendrez à effectuer les quatre opérations ici.

### CRÉER

Pour créer une nouvelle tâche, tapez ce qui suit dans votre shell :

```bash

>>> new_task = Task(title='Complete Assignment', completed=False)
>>> new_task.save()

```

Alternativement, vous pouvez utiliser la fonction `create`, comme ceci :

```bash

Task.objects.create(title='Another Task', completed=False)

```

Pour vérifier toutes les tâches, entrez ce qui suit :

```bash
Task.objects.all()

```

Vous devriez obtenir quelque chose de similaire à ce que vous voyez dans l'image ci-dessous. Remarquez qu'un queryset est retourné avec la tâche que vous venez de créer :

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-from-2024-01-15-12-32-55.png)
_création d'objets dans le shell Django_

### LIRE

Une fois que vous avez créé les objets, vous devriez être en mesure de les lire. Pour ce faire, Django fournit les méthodes `get()` et `filter()`.

La méthode `get()` récupère un seul objet de la base de données en fonction des conditions spécifiées. Elle lève des exceptions si aucun objet ou plusieurs objets sont trouvés, ce qui la rend adaptée aux requêtes uniques.

La méthode `filter()` récupère un queryset d'objets de la base de données correspondant aux conditions spécifiées. Elle ne lève pas d'exceptions si plusieurs objets ou aucun objet n'est trouvé et est donc idéale pour les requêtes avec plusieurs résultats possibles.

Vous pouvez utiliser la méthode `get()` pour récupérer la tâche avec un titre spécifique.

```bash

specific_task = Task.objects.get(title='Complete Assignment')
print(f'Title: {specific_task.title}, Completed: {specific_task.completed}')

```

La sortie du code ci-dessus est la suivante :

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-from-2024-01-15-13-59-07.png)
_récupération d'un objet spécifique dans le shell Django_



Vous pouvez également récupérer une tâche si elle répond à une condition spécifique. C'est là que la méthode filter excelle.

Supposons que vous souhaitiez obtenir les tâches incomplètes, c'est-à-dire les tâches avec le champ `completed` défini sur `False`. Vous pouvez ajouter ce code :

```bash
incomplete_tasks = Task.objects.filter(completed=False)
for task in incomplete_tasks:
    print(f'Title: {task.title}, Completed: {task.completed}')

```

Cela retournera toutes les tâches qui n'ont pas été complétées.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-from-2024-01-15-14-02-44-1.png)
_récupération d'objets qui répondent à une condition spécifique dans le shell Django_

Cette méthode est idéale pour récupérer plusieurs objets en fonction de certaines conditions.

### METTRE À JOUR

Si vous souhaitez apporter des modifications, vous pouvez le faire en utilisant la méthode `update()`. Supposons que vous avez complété toutes les tâches et que vous souhaitez maintenant les marquer comme terminées. Voici le code pour cela :

```bash
incomplete_tasks = Task.objects.filter(completed=False)
incomplete_tasks.update(completed=True)

all_tasks = Task.objects.all()

for task in all_tasks:
    print(f'Title: {task.title}, Completed: {task.completed}')

```

La sortie du code ci-dessus est :

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-from-2024-01-15-14-37-07-1.png)
_mise à jour des objets dans le shell Django_

Cela met d'abord à jour le statut des tâches à `completed`, puis imprime les tâches complétées.

### SUPPRIMER

Après tout, vous pouvez vouloir supprimer toutes les tâches ou une tâche spécifique. Vous pouvez le faire en utilisant la méthode `delete()`, comme ceci :

```bash
task_to_delete = Task.objects.get(title='Another Task')
task_to_delete.delete()
all_tasks_after_deletion = Task.objects.all()

for task in all_tasks_after_deletion:
    print(f'Title: {task.title}, Completed: {task.completed}')
```

Le code ci-dessus récupère la tâche avec le titre "Another Task" en utilisant la méthode `get` puis la supprime en utilisant la méthode `delete`. Enfin, il imprime les détails de toutes les tâches restantes pour vérifier que la suppression a été réussie.

La sortie est :

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-from-2024-01-15-14-53-40.png)
_suppression d'objets dans le shell Django_

Alternativement, vous pouvez simplifier le code ci-dessus comme ceci :

```bash
task_to_delete = Task.objects.get(title='Another Task').delete()
all_tasks_after_deletion = Task.objects.all()

for task in all_tasks_after_deletion:
    print(f'Title: {task.title}, Completed: {task.completed}')
```

Vous pouvez accéder à toutes les tâches que vous avez créées dans le panneau d'administration de Django. Démarrez le serveur dans le terminal comme suit :

```bash
python manage.py runserver

```

Puis, sur votre navigateur, visitez le site [`http://127.0.0.1:8000/admin/`](http://127.0.0.1:8000/admin/) et entrez les identifiants du superutilisateur que vous avez créés précédemment. Là, vous pouvez accéder à toutes les tâches que vous avez créées.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-from-2024-01-15-14-59-40.png)
_interface d'administration de Django_

Nous avons supprimé l'autre tâche, donc la tâche restante est la tâche 'Complete assignment' comme montré ci-dessus.

## Conclusion

Dans ce tutoriel, vous avez exploré des exemples pratiques de création, lecture, mise à jour et suppression d'objets, améliorant votre maîtrise de l'utilisation du shell interactif de Django.

Vous avez également appris l'importance d'enregistrer des modèles dans l'interface d'administration pour une gestion facile pendant le développement.

Avec cette connaissance, vous êtes maintenant équipé pour concevoir des bases de données robustes et organisées, assurant le bon fonctionnement de vos projets Django. Explorez les capacités de Django et libérez votre créativité dans la construction d'applications web dynamiques et interactives.

Bon codage.