---
title: Apprendre Django en créant une application de calculatrice
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-06-27T17:29:01.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-calculator-app-in-django
coverImage: https://www.freecodecamp.org/news/content/images/2023/06/Add-a-subheading--3-.png
tags:
- name: Django
  slug: django
- name: Python
  slug: python
seo_title: Apprendre Django en créant une application de calculatrice
seo_desc: 'By Sampurna Chapagain

  Django is a free and open-source Python web framework that helps you quickly develop
  secure and maintainable web applications.

  In this tutorial, I will guide you step by step as we create a calculator app using
  django.

  This is a...'
---

Par Sampurna Chapagain

Django est un framework web Python gratuit et open-source qui vous aide à développer rapidement des applications web sécurisées et maintenables.

Dans ce tutoriel, je vais vous guider étape par étape pour créer une application de calculatrice en utilisant Django.

Ce tutoriel est adapté aux débutants, donc si vous êtes nouveau dans Django, vous pouvez suivre.

### À quoi ressemblera notre application de calculatrice ?

![Image](https://www.freecodecamp.org/news/content/images/2023/06/calculator-1.gif)
_Calculatrice avec des opérations d'addition, de soustraction, de multiplication et de division_

Vous pouvez obtenir le code complet dans ce [dépôt GitHub](https://github.com/SampurnaC/calculator).

## Comment configurer le projet de calculatrice Django

En supposant que vous avez Django installé sur votre système, nous allons maintenant travailler sur la création du projet. Pour cela, vous devez ouvrir le terminal et utiliser la commande suivante :

```py
django-admin startproject calculator
```

Cette commande crée la structure par défaut du projet avec des fichiers comme `manage.py`, et un dossier avec le nom du projet qui contient des fichiers comme `settings.py`, `urls.py` et ainsi de suite. Nous passerons en revue ces fichiers au fur et à mesure que nous travaillerons sur notre application.

Après la création du projet, nous devons changer le répertoire de travail pour le répertoire du projet. Sous Linux, la commande est `cd calculator/`.

L'étape suivante consiste à créer une application Django nommée `calculatorapp` avec la commande suivante :

```python
python manage.py startapp calculatorapp
```

Cette application contient des fichiers comme `models.py`, `views.py`, `admin.py`, `migrations`, et ainsi de suite.

Une fois l'application créée, la première chose importante est d'enregistrer l'application dans la liste `INSTALLED_APPS` du fichier `settings.py`.

Pour cela, vous devrez naviguer jusqu'au fichier `settings.py` qui se trouve à l'intérieur de votre projet Django, et qui est `calculator` dans ce tutoriel. Le fichier `settings.py` contient la liste `INSTALLED_APPS` et vous devrez ajouter le nom de votre application à la liste. Ainsi, la liste `INSTALLED_APPS` devrait ressembler à ceci :

```python
INSTALLED_APPS = [
    'calculatorapp',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

Maintenant que l'application est enregistrée, nous sommes prêts à travailler sur le projet.

### Comment ajouter des routes

Maintenant, travaillons sur l'ajout des routes. Vous devez créer un fichier `urls.py` dans le répertoire `calculatorapp`. Le code est ajouté ci-dessous :

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
```

Ici, vous devrez importer `path` depuis `django.urls` puis importer `views`.

Dans la liste `urlpatterns`, vous devez passer votre fonction de vue, que nous allons créer très bientôt.

Mais d'abord, enregistrons ce fichier d'URL d'application dans le fichier `urls.py` du projet.

Ainsi, vous devrez ouvrir le fichier `urls.py` à l'intérieur du répertoire calculator et ajouter le code suivant :

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('calculatorapp.urls')),
]
```

Ici, il inclut l'URL de `calculatorapp`. Si vous souhaitez ajouter une nouvelle URL pour votre `calculatorapp`, vous pouvez le faire depuis le fichier `calculatorapp/urls.py`.

### Comment écrire des vues

Maintenant, si vous essayez de visiter l'URL [`http://localhost:8000/`](http://localhost:8000/), vous obtiendrez une erreur car il recherche la fonction de vue `home`. La fonction de vue pour la route `/` est `home` et comme il n'y a pas de vue `home`, cela génère une erreur.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/Screenshot-from-2023-06-24-18-27-10.png)
_erreur dans le terminal lors de la visite de la page racine_

Dans Django, il existe deux types de vues : les vues basées sur des fonctions et les vues basées sur des classes. Dans ce tutoriel, nous utiliserons des vues basées sur des fonctions et elles commencent par le mot-clé `def`.

Pour corriger l'erreur ci-dessus, vous devrez aller dans le fichier `views.py` qui se trouve à l'intérieur de `calculatorapp` et créer une fonction de vue `home`.

```python
def home(request):
    pass
```

### Comment ajouter des templates à l'application

Maintenant, si vous essayez de visiter l'URL [`http://localhost:8000/`](http://localhost:8000/), vous obtiendrez une erreur différente. Comme vous pouvez le voir sur la capture d'écran ci-dessous, il recherche une réponse à retourner.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/Screenshot-from-2023-06-24-18-30-31.png)
_erreur dans le navigateur recherchant la réponse des vues_

Ainsi, au lieu d'utiliser simplement un texte aléatoire comme `pass`, vous devrez rendre un template HTML. Les templates sont utilisés pour rendre le contenu HTML dynamique.

```python
def home(request):
    return render(request, 'home.html')
```

Comme vous pouvez le voir pour la vue `home`, elle retourne le template `home.html`.

Maintenant, vous devrez créer un dossier templates dans le répertoire racine de votre application, qui est `calculatorapp` dans ce tutoriel.

À l'intérieur de ce dossier templates, vous devrez créer un fichier `home.html`.

Ce template `home.html` contiendra le formulaire avec différents boutons pour la calculatrice.

Le fichier `home.html` contiendra le code suivant :

```html
<div class="center">
<h1>Calculatrice Basique</h1>

<form action="result">
    <input type="number" name="number1" placeholder="Entrez le premier nombre">
    <br>
    <br> 
    <input type="number" name="number2" placeholder="Entrez le deuxième nombre">
    <br>
    <br>
    <button type="submit" name="add">Additionner</button>
    <button type="submit" name="subtract">Soustraire</button>
    <button type="submit" name="multiply">Multiplier</button>
    <button type="submit" name="divide">Diviser</button>

</form>
</div>

<style>
  .center {
    margin: auto;
    width: 60%;
    border: 3px solid #a5addb;
    padding: 10px;
  }
</style>
```

Le code ci-dessus contient un formulaire `HTML` simple avec deux champs de saisie et quatre boutons. Il y a un peu de style pour afficher le code au centre avec une bordure.

L'élément important à noter dans le code ci-dessus est `<form action="result">`, ce qui signifie qu'à la soumission du formulaire, il sera redirigé vers l'URL `result`.

Maintenant, si vous essayez d'effectuer des opérations dans le navigateur, vous obtiendrez une nouvelle erreur car il n'y a pas de page de résultat.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/error.gif)
_Erreur après la soumission du bouton car il n'y a pas de page de résultat_

### Comment ajouter l'URL pour la page de résultat

À la soumission du formulaire, il recherche le chemin `result`. Ainsi, l'étape suivante consiste à créer la vue `result` et à ajouter un template et une URL pour celle-ci.

Le fichier `urls.py` mis à jour sera le suivant :

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('result/', views.result, name='result'),
]
```

### Comment ajouter le code de template pour la vue de résultat

La deuxième URL de la liste `urlpatterns` recherche la vue `result`. Alors, travaillons dessus maintenant. Tout d'abord, je vais vous montrer le code pour la vue `result` puis expliquer ce que fait chaque ligne.

```python
def result(request):
    num1 = int(request.GET.get('number1'))
    num2 = int(request.GET.get('number2'))

    
    if request.GET.get('add') == "":
        ans = num1 + num2

    elif request.GET.get('subtract') == "":    
        ans = num1 - num2

    elif request.GET.get('multiply') == "":    
        ans = num1 * num2

    else:
        ans = num1 / num2

    return render(request, 'result.html', {'ans': ans})
```

Maintenant, décomposons le code ci-dessus :

* Il obtient la valeur des champs de saisie `number1` et `number2` que vous obtenez depuis le formulaire.
* Ensuite, il vérifie les conditions en fonction des boutons cliqués.
* Comme tous les boutons ont des noms différents, cliquer sur ceux-ci donne la valeur de chaîne vide dans l'URL. Et en fonction de cela, il ajoute des conditions pour `add`, `subtract`, `multiply`, et `divide`.
* Il rend le template `result.html` avec le contexte `ans`. Le contexte dans Django est un dictionnaire avec des paires clé-valeur qui peuvent être passées au template.

Maintenant, vous devrez créer un fichier `result.html` à l'intérieur du dossier `templates` et ajouter le code suivant :

```html
<div class="center">
Le résultat est : 
<h1>{{ans}}</h1>

<a href="{% url 'home' %}">Retour</a>
</div>
<style>
  .center {
    margin: auto;
    width: 60%;
    border: 3px solid #a5addb;
    padding: 10px;
  }
</style>
```

Ici, il affiche la valeur de `ans`. Et il contient également l'URL `home` avec un peu de style de base pour la page.

Dans Django, les doubles accolades `{{}}` sont utilisées pour afficher la valeur des variables. Et les variables sortent la valeur du contexte.

Enfin, nous avons terminé la création d'une application de calculatrice avec des fonctionnalités de base comme l'addition, la soustraction, la multiplication et la division dans Django.

## Conclusion

Voici comment vous pouvez créer une application de calculatrice basique dans Django.

Dans ce tutoriel, vous avez appris à gérer les vues, les templates, les URLs et les configurations nécessaires pour rendre l'application Django fonctionnelle.

Je n'ai pas couvert les modèles dans cet article. Donc, si vous souhaitez enregistrer les résultats dans la base de données, vous pouvez explorer cela plus loin.

J'espère que vous avez trouvé ce tutoriel utile.

Vous pouvez me trouver sur [Twitter](https://twitter.com/saam_codes) pour du contenu quotidien concernant le développement web.

Bon codage en Python !