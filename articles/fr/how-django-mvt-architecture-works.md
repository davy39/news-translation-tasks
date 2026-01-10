---
title: 'Comment fonctionne l''architecture MVT de Django : Une plongée approfondie
  dans les Modèles, Vues et Templates'
subtitle: ''
author: Timothy Olanrewaju
co_authors: []
series: null
date: '2024-12-10T22:31:04.246Z'
originalURL: https://freecodecamp.org/news/how-django-mvt-architecture-works
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1733732493858/a06ee65a-de97-4c7f-b3bd-7ca8c1b6fe82.png
tags:
- name: Web Development
  slug: web-development
- name: Django
  slug: django
- name: Python
  slug: python
seo_title: 'Comment fonctionne l''architecture MVT de Django : Une plongée approfondie
  dans les Modèles, Vues et Templates'
seo_desc: 'Django is a high-level Python framework. It’s popular for its simplicity
  and efficiency in building robust web applications.

  At the heart of Django’s architecture is the Model-View-Template (MVT) pattern.
  Having a good understanding of how Models, Vi...'
---

Django est un framework Python de haut niveau. Il est populaire pour sa simplicité et son efficacité dans la création d'applications web robustes.

Au cœur de l'architecture de Django se trouve le modèle Model-View-Template (MVT). Avoir une bonne compréhension de la manière dont les Modèles, Vues et Templates interagissent est crucial si vous cherchez à exploiter toute la puissance de Django.

Que vous soyez complètement nouveau dans Django ou un débutant, cet article servira de guide complet vous montrant comment ces composants fonctionnent et interagissent les uns avec les autres pour créer des applications web dynamiques.

Pour le rendre encore plus compréhensible, nous allons construire une application simple pour vous aider à mieux comprendre l'interconnectivité de ces composants.

Si vous êtes déjà excité, commençons tout de suite !

### Voici ce que nous allons couvrir :

* [Prérequis](#heading-prerequis)
    
* [Qu'est-ce que l'architecture MVT ?](#heading-quest-ce-que-larchitecture-mvt)
    
* [Le composant Modèle](#heading-le-composant-modele)
    
* [Le composant Vue](#heading-le-composant-vue)
    
* [Le composant Template](#heading-le-composant-template)
    
* [Diagramme montrant le flux de travail MVT](#heading-diagramme-montrant-le-flux-de-travail-mvt)
    
* [Analogie réelle de MVT](#heading-analogie-reelle-de-mvt)
    
* [Mettre tout ensemble dans un projet](#heading-mettre-tout-ensemble-dans-un-projet)
    
* [Conclusion](#heading-conclusion)
    

## Prérequis

Pour suivre, vous avez besoin de :

* Une compréhension de base du fonctionnement des applications web, y compris l'architecture client-serveur.
    
* Une connaissance de base de Python.
    

## Qu'est-ce que l'architecture MVT ?

Le modèle MVT est l'approche de Django pour organiser la base de code et le flux de travail d'une application web. Les composants qui constituent cette architecture sont le Modèle, la Vue et le Template. Chaque composant effectue des fonctions spécifiques puis passe le processus aux autres composants pour qu'ils fassent les leurs.

Jetons un rapide coup d'œil aux composants avec les fonctions spécifiques qu'ils remplissent :

* **Modèle** : Également connu sous le nom de couche de données, il gère les données et interagit avec la base de données.
    
* **Vue** : Également connue sous le nom de couche logique, elle agit comme intermédiaire, gère la logique et le flux de données.
    
* **Template** : Également connu sous le nom de couche de présentation, il rend le contenu HTML sur l'interface utilisateur.
    

Maintenant que vous avez une idée des composants et de leurs rôles dans une application Django, nous allons examiner en détail chaque composant et comment ils interagissent dans l'architecture.

## Le composant Modèle

Les Modèles gèrent la structure et l'interaction des données au sein d'une application Django, ce qui en fait la base des applications Django en raison du rôle crucial que jouent les données.

Les modèles Django utilisent une fonctionnalité puissante appelée [Object-Relational Mapping (ORM)](https://www.freecodecamp.org/news/what-is-an-orm-the-meaning-of-object-relational-mapping-database-tools/), qui comble le fossé entre une base de données relationnelle et le code Python. Il convertit les objets Python (classes) en tables de base de données, leurs attributs en colonnes, et les instances en lignes au sein de ces tables.

Un grand avantage de l'ORM est qu'il vous permet d'interagir avec la base de données en utilisant des objets Python au lieu d'écrire des requêtes SQL. Pensez-y comme à un traducteur qui convertit une langue en une autre pour qu'un public puisse comprendre. Dans ce cas, l'ORM traduit le code Python en commandes SQL que la base de données peut exécuter, et vice versa.

Les modèles Django encapsulent toute la logique liée à la base de données et définissent la structure de votre base de données, agissant comme un plan pour les données que vous souhaitez stocker.

### **Format général d'un Modèle Django**

Dans Django, chaque modèle suit une manière particulière de déclaration. Voici la structure de base d'une déclaration de modèle :

```python
class <nom_du_modele>(models.Model):
    <nom_du_champ> = models.<type_de_champ>(<caracteristiques_du_champ_facultatives>)
```

Décomposons cela :

* `class` : le mot-clé utilisé pour définir un modèle dans Django.
    
* `nom_du_modele` : le nom du modèle.
    
* `models.Model` : la classe de base dont la classe du modèle hérite.
    
* `nom_du_champ` : le nom de la colonne de la base de données.
    
* `type_de_champ` : fait référence au type de données que le champ contient, comme `CharField`, `BooleanField`, etc.
    
* `caracteristiques_du_champ_facultatives` : utilisé pour définir davantage le comportement du champ, comme `max_length`, `default`, etc.
    

### **Exemple de Modèle**

Ayant tout appris sur les modèles jusqu'à ce point, nous allons en construire un pour une liste de tâches. Elle contient généralement le titre de la tâche, la description et un indicateur indiquant si les tâches ont été complétées ou non.

```python
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)
```

Dans ce modèle :

* Task est le nom du modèle.
    
* Le modèle Task a trois champs :
    
    * `title` : Un `CharField` qui contient du texte, avec une longueur maximale de 100 caractères.
        
    * `description` : Un `TextField` pour du texte plus long.
        
    * `completed` : Un `BooleanField` qui stocke une valeur `True` ou `False`, avec une valeur par défaut de `False`.
        

## Le composant Vue

Les vues Django sont responsables du traitement des requêtes utilisateur et du retour des réponses. Elles agissent comme un pont entre le Modèle et le Template en collectant des données à partir d'objets Modèle, en effectuant des opérations logiques sur celles-ci (comme des requêtes basées sur certains critères), puis en passant les données au template pour l'affichage.

Les vues peuvent être écrites sous forme de fonctions ou basées sur des classes, selon la complexité et les exigences de votre application.

### **Format général d'une Vue Django**

Voici la structure de base d'une Vue :

```python
def <nom_de_la_vue>(request):
    # La logique de la Vue va ici....
    return render(request, <template>, <contexte>)
```

Décomposons cela :

* `nom_de_la_vue` : le nom de la fonction de vue.
    
* `request` : la requête HTTP envoyée par le client au serveur Django, qui peut être déclenchée par des soumissions de formulaire ou en cliquant sur un bouton.
    
* `return render` : utilisé pour générer la réponse HTML. Il prend :
    
    * `request` : l'objet de requête, qui contient des informations sur la requête entrante.
        
    * `template` : le fichier de template à rendre.
        
    * `contexte` : contient des variables à rendre disponibles dans le template, il se présente généralement sous la forme d'un dictionnaire.
        

### **Exemple de Vue**

En continuant avec notre liste de tâches, voici à quoi ressemblerait notre vue :

```python
def task_list(request):
    # La logique va ici...
    return render(request, <template>, {'tasks': tasks})
```

## Le composant Template

Les templates Django sont responsables du rendu du contenu HTML final dans le navigateur. Ils définissent comment les données doivent être présentées, en utilisant une combinaison de HTML et du langage de templating de Django.

Le langage de templating de Django implique l'utilisation de **balises de template** `{% %}` et de **variables de template** `{{ }}` qui vous permettent d'entrer en mode Django dans votre template HTML. Dans ce mode, vous pouvez accéder aux variables définies dans vos Vues et utiliser des structures de contrôle dans votre template.

Les templates peuvent également être stylisés en utilisant CSS ou l'un de vos frameworks CSS préférés pour rendre votre interface utilisateur plus présentable.

### **Exemple de Template**

Notre template est un fichier HTML normal avec le langage de templating de Django. Voici à quoi ressemblerait notre template de liste de tâches :

```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Liste de tâches</title>
</head>
<body>
    <h1>Liste de tâches</h1>
    <ul>
        {% for task in tasks %}
            <li>{{ task.title }} - {{ task.completed|yesno:"Fait,Non fait" }}</li>
        {% empty %}
            <p>Aucune tâche disponible.</p>
        {% endfor %}
    </ul>
</body>
</html>
```

Dans ce template :

* La boucle `for` parcourt chaque tâche dans la liste `tasks` (rappelons qu'elle a été passée en contexte dans nos vues).
    
* Pour chaque tâche, elle affiche le `title` de la tâche et son statut `completed` (soit "Fait" soit "Non fait").
    
* Si la liste `tasks` est vide, le bloc `{% empty %}` affiche un message de repli disant "Aucune tâche disponible.".
    

## Diagramme montrant le flux de travail MVT

Ce diagramme montre comment les données circulent au sein de l'architecture MVT de Django :

![Diagramme de l'architecture MVT montrant comment les données circulent entre le client et le serveur](https://cdn.hashnode.com/res/hashnode/image/upload/v1733727208715/06e27a48-ba51-421c-acc6-f0949b37a954.png align="center")

## Analogie réelle de MVT

Imaginez que vous allez dans un restaurant et que vous passez une commande pour votre plat préféré. Derrière la scène, le restaurant a un livre de recettes qui décrit comment chaque plat doit être préparé. Le chef utilise les recettes pour préparer votre repas exactement comme vous l'avez commandé. Une fois prêt, le serveur vous apporte le repas de manière présentable.

Tout comme un chef suit la recette pour créer le plat, la Vue utilise le Modèle pour collecter et traiter les données. Enfin, comme le serveur qui apporte le plat, le Template garantit que la sortie finale est présentée de manière claire et engageante à l'utilisateur.

## Mettre tout ensemble dans un projet

Cette section vous guidera, du début à la fin, sur la façon de configurer la liste de tâches que nous avons utilisée comme exemple dans l'article. À la fin, vous devriez avoir une application fonctionnelle avec l'architecture MVT en plein flux.

### Installer Python

Tout d'abord, assurez-vous d'avoir Python installé. Vous pouvez visiter le [Site Officiel de Python](https://www.python.org/downloads/) pour télécharger la dernière version de Python.

### Configurer le projet Django et l'application

Ensuite, installez Django. Vous pouvez l'installer en utilisant pip :

```bash
pip install django
```

Créez un dossier et ouvrez-le dans votre éditeur de code préféré.

Créez un nouveau projet Django et une application en exécutant les commandes suivantes dans votre terminal, l'une après l'autre :

```bash
django-admin startproject monprojet 
cd monprojet
django-admin startapp monapp
```

### Définir le Modèle

Dans votre fichier `monapp/models.py` :

```python
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)
```

### Créer un Formulaire

Nous avons besoin d'un formulaire Django basé sur le modèle Task, nous allons donc en créer un en utilisant le ModelForm de Django.

Dans votre dossier `monapp`, créez un fichier, nommez-le `forms.py`, et insérez ce code :

```python
from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed']
```

Dans ce code :

* `Task` est importé depuis `.models`.
    
* `class TaskForm(forms.ModelForm)` : Cela crée une nouvelle classe appelée `TaskForm`, qui est une sous-classe de `forms.ModelForm`.
    
* `class Meta:` : est une classe spéciale utilisée par le `ModelForm` de Django pour fournir une configuration pour le formulaire. La classe `Meta` indique à Django comment créer le formulaire en spécifiant le modèle associé et les champs à inclure dans le formulaire.
    
* `model = Task` : spécifie le modèle sur lequel le formulaire est basé. Dans ce cas, le formulaire est basé sur le modèle `Task`.
    
* `fields = ['title', 'description', 'completed']` : spécifie quels champs du modèle `Task` doivent être inclus dans le formulaire. Cela vous permet de contrôler quels champs du modèle apparaissent dans le formulaire, et il peut être personnalisé pour inclure uniquement certains champs, plutôt que tous les champs du modèle.
    

### Créer la Vue

Dans votre fichier `monapp/views.py`, insérez ce code :

```python
from django.shortcuts import render,redirect
from .models import Task
from .forms import TaskForm

def task_list(request):
    tasks = Task.objects.all()    # Récupérer toutes les tâches
    
    if request.method == 'POST':    # Gérer les soumissions de formulaire
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')  # Rediriger pour éviter les soumissions en double
    else:
        form = TaskForm()

    # Passer les tâches et le formulaire au template
    return render(request, 'task_list.html', {'tasks': tasks, 'form': form})
```

Dans cette vue,

* `TaskForm` est importé depuis `forms`.
    
* Le code vérifie si la méthode de requête est `POST`, indiquant que l'utilisateur a soumis un formulaire.
    
* Si la méthode est `POST`, il crée une instance de `TaskForm` en utilisant les données soumises ([`request.POST`](http://request.POST)).
    
* Le formulaire est ensuite validé en utilisant [`form.is`](http://form.is)`_valid()`, et s'il est valide, le formulaire est enregistré dans la base de données.
    
* Après l'enregistrement, l'utilisateur est redirigé vers la page de liste des tâches pour éviter les soumissions en double.
    

### Définir le Template

Dans votre répertoire `monapp`, créez un dossier `templates`. À l'intérieur du dossier templates, créez un fichier et nommez-le `task_list.html`. Nous devons ajouter un élément de formulaire qui collecte les entrées de l'utilisateur et les affiche dans une liste sur l'interface utilisateur.

Dans le fichier HTML `task_list`, nous avons :

```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Liste de tâches</title>
</head>
<body>
    <h1>Liste de tâches</h1>
    <ul>
        {% for task in tasks %}
            <li>{{ task.title }} - {{ task.completed|yesno:"Fait,Non fait" }}</li>
        {% empty %}
            <p>Aucune tâche disponible.</p>
        {% endfor %}
    </ul>

    <h2>Ajouter une nouvelle tâche</h2>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Ajouter une tâche</button>
    </form>
</body>
</html>
```

Dans le code de formulaire ajouté :

* Nous avons créé un formulaire HTML avec la méthode `POST` pour soumettre les données. Il inclut un `{% csrf_token %}` pour se protéger contre les attaques CSRF.
    
* Les champs du formulaire sont rendus en utilisant `{{ form.as_p }}`, qui affiche chaque champ dans une balise `<p>`.
    
* Enfin, un bouton de soumission étiqueté "Ajouter une tâche" est fourni, permettant à l'utilisateur de soumettre les données du formulaire.
    

### Structure du dossier

À ce stade, il est important de vérifier si vous configurez votre application de la bonne manière. Voici à quoi devrait ressembler votre structure de dossier/fichier :

```python
[34m[1m[4mmonprojet[0m
    [34m[1m[4mmonapp[0m
        [34m[1m[4m__pycache__[0m
        [34m[1m[4mmigrations[0m
        [34m[1m[4mtemplates[0m
            [34m[1m[4mtask_list.html[0m
        [34m[1m[4m__init__.py[0m
        [34m[1m[4madmin.py[0m
        [34m[1m[4mapps.py[0m
        [34m[1m[4mforms.py[0m
        [34m[1m[4mmodels.py[0m
        [34m[1m[4mtests.py[0m
        [34m[1m[4murls.py[0m
        [34m[1m[4mviews.py[0m
    [34m[1m[4mmonprojet[0m
        [34m[1m[4m__pycache__[0m
        [34m[1m[4m__init__.py[0m
        [34m[1m[4masgi.py[0m
        [34m[1m[4msettings.py[0m
        [34m[1m[4murls.py[0m
        [34m[1m[4mwsgi.py[0m
    [34m[1m[4mdb.sqlite3[0m
    [34m[1m[4mmanage.py[0m
```

### Configurer l'URL du projet

Dans votre fichier `monprojet/urls.py`, incluez l'URL de votre `monapp` :

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('monapp.urls')),
]
```

### Ajouter l'application aux paramètres du projet

Ajoutez votre `monapp` à la liste des **applications installées** dans votre fichier `monprojet/settings.py` :

```python
INSTALLED_APPS = [
    'monapp',      # ajouté notre application monapp
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

### Lancer le serveur

Appliquez les migrations et lancez le serveur en entrant ces commandes :

```python
python manage.py migrate

python manage.py runserver
```

Visitez [`http://127.0.0.1:8000/`](http://127.0.0.1:8000/items/) dans votre navigateur pour tester votre application.

### Apparence finale

Voici à quoi ressemble notre application de liste de tâches dans le navigateur après avoir ajouté quelques tâches en utilisant le formulaire. Vous pouvez apporter des améliorations supplémentaires au style du template comme vous le souhaitez.

![Interface finale de l'application de tâches](https://cdn.hashnode.com/res/hashnode/image/upload/v1733688592866/d481df60-143e-42c7-acfe-0c329130c591.png align="center")

## Conclusion

Dans cet article, vous avez appris les composants de l'architecture MVT de Django, comment ils interagissent les uns avec les autres et comment ils rendent les expériences web fluides. Nous avons également construit un projet simple pour voir comment cela fonctionne en pratique, et j'espère que vous le comprenez mieux maintenant.

Si vous avez aimé lire cet article, vous pouvez me suivre sur [X](https://x.com/SmoothTee_DC) ou vous connecter avec moi sur [LinkedIn](https://www.linkedin.com/in/timothy-olanrewaju750/) pour plus d'articles et de publications sur la programmation.

À la prochaine !