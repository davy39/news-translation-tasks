---
title: Comment créer un tableau de bord analytique dans une application Django
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-12T10:10:30.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-an-analytics-dashboard-in-django-app
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9c9e740569d1a4ca3336.jpg
tags:
- name: 'BUSINESS INTELLIGENCE '
  slug: business-intelligence
- name: data analytics
  slug: data-analytics
- name: Data Science
  slug: data-science
- name: data visualization
  slug: data-visualization
- name: Django
  slug: django
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: Web Development
  slug: web-development
seo_title: Comment créer un tableau de bord analytique dans une application Django
seo_desc: 'By Veronika Rovnik

  Hi folks!

  Python, data visualization, and programming are the topics I''m profoundly devoted
  to. That’s why I’d like to share with you my ideas as well as my enthusiasm for
  discovering new ways to present data in a meaningful way.

  T...'
---

Par Veronika Rovnik

Salut à tous !

**Python**, **la visualisation de données** et **la programmation** sont les sujets auxquels je suis profondément dévouée. C'est pourquoi je souhaite partager avec vous mes idées ainsi que mon enthousiasme pour la découverte de nouvelles façons de présenter les données de manière significative.

Le cas que je vais aborder est assez courant : vous avez des données dans le back-end de votre application et vous souhaitez leur donner une forme dans le front-end. Si une telle situation vous semble familière, alors ce tutoriel pourrait vous être utile.

Une fois que vous l'aurez terminé, vous aurez une **application alimentée par Django** avec des **tableaux croisés dynamiques** et des **graphiques** interactifs.

## Prérequis

Pour suivre les étapes en toute confiance, vous avez besoin d'une connaissance de base du framework Django et _d'un peu de créativité_. ✨

Pour suivre ce tutoriel, vous pouvez télécharger l'exemple [GitHub](https://github.com/veronikaro/django-dashboard-app).

Voici une brève liste des outils que nous allons utiliser :

* **[Python 3.7.4](https://www.python.org/downloads/release/python-374/)**
* **[Django](https://www.djangoproject.com/?r=fr5)**
* **[Virtualenv](https://virtualenv.pypa.io/en/latest/)**
* **[Flexmonster Pivot Table & Charts](https://www.flexmonster.com/?r=fr5)** (bibliothèque JavaScript)
* **[SQLite](https://www.sqlite.org/index.html)**

Si vous avez déjà configuré un projet Django et que vous vous sentez à l'aise avec le flux de base de création d'applications, vous pouvez passer directement à la section **Connexion des données à Flexmonster** qui explique comment ajouter des composants de visualisation de données.

Commençons !

## Démarrage avec Django

Tout d'abord, assurons-nous que vous avez installé Django sur votre machine. La règle générale est de l'installer dans votre environnement virtuel précédemment configuré - un outil puissant pour isoler vos projets les uns des autres.

Assurez-vous également de l'avoir activé dans un répertoire nouvellement créé. Ouvrez votre console et initialisez un projet Django avec cette commande :

`django-admin startproject analytics_project`

Maintenant, il y a un nouveau répertoire appelé `analytics_project`. Vérifions si nous avons tout fait correctement. Allez dans `analytics_project` et démarrez le serveur avec la commande de la console :

`python manage.py runserver`

Ouvrez [`http://127.0.0.1:8000/`](http://127.0.0.1:8000/) dans votre navigateur. Si vous voyez cette fusée géniale, alors tout est en ordre :

![Image](https://www.freecodecamp.org/news/content/images/2020/02/DjangoRocket.gif)

Ensuite, créez une nouvelle application dans votre projet. Appelons-la `dashboard` :

`python manage.py startapp dashboard`

> _Voici un conseil_ : si vous n'êtes pas sûr de la [différence entre les concepts d'applications et de projets dans Django](https://wsvincent.com/django-projects-vs-apps/), prenez le temps de vous renseigner pour avoir une image claire de l'organisation des projets Django.

Nous y voilà. Maintenant, nous voyons un nouveau répertoire dans le projet. Il contient les fichiers suivants :

`__init__.py` pour que Python le traite comme un package

`admin.py` - paramètres pour les pages d'administration de Django

`apps.py` - paramètres pour les configurations de l'application

`models.py` - classes qui seront converties en tables de base de données par l'ORM de Django

`tests.py` - classes de test

`views.py` - fonctions et classes qui définissent comment les données sont affichées dans les templates

Ensuite, il est nécessaire d'enregistrer l'application dans le projet. 
Allez dans `analytics_project/settings.py` et ajoutez le nom de l'application à la liste `INSTALLED_APPS` :

```python
INSTALLED_APPS = [
	'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'dashboard',
]
```

Maintenant, notre projet est conscient de l'existence de l'application.

## Vues

Dans le fichier `dashboard/views.py`, nous allons créer une fonction qui dirige un utilisateur vers les templates spécifiques définis dans le dossier `dashboard/templates`. Les vues peuvent également contenir des classes.

Voici comment nous la définissons :

```python
from django.http import JsonResponse
from django.shortcuts import render
from dashboard.models import Order
from django.core import serializers

def dashboard_with_pivot(request):
    return render(request, 'dashboard_with_pivot.html', {})
```

Une fois appelée, cette fonction rendra `dashboard_with_pivot.html` - un template que nous définirons bientôt. Il contiendra les composants de tableau croisé dynamique et de graphiques.

Quelques mots de plus sur cette fonction. Son argument `request`, une instance de `HttpRequestObject`, contient des informations sur la requête, par exemple, la méthode HTTP utilisée (GET ou POST). La méthode `render` recherche des templates HTML dans un répertoire `templates` situé dans le répertoire de l'application.

Nous devons également créer une méthode auxiliaire qui envoie la réponse avec les données au tableau croisé dynamique sur le front-end de l'application. Appelons-la `pivot_data` :

```python
def pivot_data(request):
    dataset = Order.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)
```

Probablement, votre IDE vous indique qu'il ne trouve pas de référence `Order` dans `models.py`. Pas de problème - nous nous en occuperons plus tard.

## Templates

Pour l'instant, nous allons profiter du système de templates de Django.

Créons un nouveau répertoire `templates` dans `dashboard` et créons le premier template HTML appelé **`dashboard_with_pivot.html`**. Il sera affiché à l'utilisateur sur demande. Ici, nous ajoutons également les scripts et les conteneurs pour les composants de visualisation de données :

```html
<head>
  <meta charset="UTF-8">
  <title>Tableau de bord avec Flexmonster</title>
  <script src="https://cdn.flexmonster.com/flexmonster.js"></script>
  <script src="https://code.jquery.com/jquery-3.3.1.min.js"></script>
  <link rel="stylesheet" href="https://cdn.flexmonster.com/demo.css">
</head>
<body>
<div id="pivot-table-container" data-url="{% url 'pivot_data' %}"></div>
<div id="pivot-chart-container"></div>
</body>
```

## Mapping des fonctions de vues aux URLs

Pour appeler les vues et afficher les templates HTML rendus à l'utilisateur, nous devons mapper les vues aux URLs correspondantes.

> Voici un conseil : [l'un des principes de conception des URLs de Django parle de couplage lâche](https://docs.djangoproject.com/en/2.1/misc/design-philosophies/#id8), nous ne devrions pas créer des URLs avec les mêmes noms que les fonctions Python.

Allez dans `analytics_app/urls.py` et ajoutez les configurations pertinentes pour l'application `dashboard` au niveau du projet.

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', include('dashboard.urls')),
]

```

Maintenant, les URLs de l'application `dashboard` peuvent être accessibles mais seulement si elles sont précédées par `dashboard`.

Ensuite, allez dans `dashboard/urls.py` (créez ce fichier s'il n'existe pas) et ajoutez une liste de motifs d'URL qui sont mappés aux fonctions de vue :

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_with_pivot, name='dashboard_with_pivot'),
    path('data', views.pivot_data, name='pivot_data'),
]
```

## Modèle

Et enfin, nous en arrivons à la **modélisation des données**. C'est ma partie préférée.

Comme vous le savez peut-être, un modèle de données est une représentation conceptuelle des données stockées dans une base de données.

Puisque le but de ce tutoriel est de montrer comment construire une visualisation de données interactive dans l'application, nous ne nous soucierons pas trop du choix de la base de données. Nous utiliserons **SQLite** - une base de données légère qui est fournie avec le serveur de développement web Django.

Mais gardez à l'esprit que cette base de données n'est pas le choix approprié pour le développement en production. Avec l'ORM de Django, vous pouvez utiliser d'autres bases de données qui utilisent le langage SQL, telles que PostgreSQL ou MySQL.

Pour simplifier, notre modèle sera composé d'une seule classe. Vous pouvez créer plus de classes et définir des relations entre elles, complexes ou simples.

Imaginons que nous concevons un **tableau de bord pour le département des ventes**. Alors, créons une classe **Order** et définissons ses attributs dans `dashboard/models.py` :

```python
from django.db import models


class Order(models.Model):
    product_category = models.CharField(max_length=20)
    payment_method = models.CharField(max_length=50)
    shipping_cost = models.CharField(max_length=50)
    unit_price = models.DecimalField(max_digits=5, decimal_places=2)
```

## Travailler avec une base de données

Maintenant, nous devons créer une base de données et la remplir avec des enregistrements.

_Mais comment pouvons-nous traduire notre classe de modèle en une table de base de données ?_

C'est là que le concept de **migration** entre en jeu. Une **migration** est simplement un fichier qui décrit les changements qui doivent être appliqués à la base de données. Chaque fois que nous devons créer une base de données basée sur le modèle décrit par des classes Python, nous utilisons la migration.

Les données peuvent provenir d'objets Python, de dictionnaires ou de listes. Cette fois, nous représenterons les entités de la base de données en utilisant des classes Python qui se trouvent dans le répertoire `models`.

Créez une migration pour l'application avec une commande :

`python manage.py makemigrations dashboard`

Ici, nous avons spécifié que l'application doit dire à Django d'appliquer les migrations pour les modèles de l'application `dashboard`.

Après avoir créé un fichier de migration, appliquez les migrations décrites dans celui-ci et créez une base de données :

`python manage.py migrate dashboard`

Si vous voyez un nouveau fichier `db.sqlite3` dans le répertoire du projet, nous sommes prêts à travailler avec la base de données.

Créons des instances de notre classe Order. Pour cela, nous utiliserons le shell Django - il est similaire au shell Python mais permet d'accéder à la base de données et de créer de nouvelles entrées.

Alors, démarrez le shell Django :

`python manage.py shell`

Et écrivez le code suivant dans la console interactive :

```python
from dashboard.models import Order

>>> o1 = Order(
... product_category='Books',
... payment_method='Credit Card',
... shipping_cost=39,
... unit_price=59
... )
>>> o1.save()
```

De manière similaire, vous pouvez créer et sauvegarder autant d'objets que vous le souhaitez.

## Connexion des données à Flexmonster

Et voici ce que j'ai promis d'expliquer.

Découvrons comment passer les données de votre modèle à l'outil de visualisation de données sur le front-end.

Pour faire communiquer le back-end et Flexmonster, nous pouvons suivre deux approches différentes :

* _Utiliser le cycle requête-réponse._ Nous pouvons utiliser Python et le moteur de templates Django pour écrire du code JavaScript directement dans le template.
* _Utiliser une requête asynchrone (AJAX)_ qui retourne les données en JSON.

À mon avis, la deuxième approche est la plus pratique pour plusieurs raisons. Tout d'abord, Flexmonster comprend le JSON. Pour être précis, il peut accepter un tableau d'objets JSON comme données d'entrée. Un autre avantage de l'utilisation de requêtes asynchrones est la meilleure vitesse de chargement de la page et un code plus maintenable.

Voyons comment cela fonctionne.

Allez dans le fichier `templates/dashboard_pivot.html`.

Ici, nous avons créé deux conteneurs `div` où le tableau croisé dynamique et les graphiques seront rendus.

Dans l'appel AJAX, nous faisons une requête basée sur l'URL contenue dans la propriété `data-URL`. Ensuite, nous indiquons à la requête AJAX que nous attendons un objet JSON à retourner (définie par `dataType`).

Une fois la requête terminée, la réponse JSON retournée par notre serveur est définie dans le paramètre `data`, et le tableau croisé dynamique, rempli avec ces données, est rendu.

Le résultat de la requête (l'instance de `JSONResponse`) retourne une chaîne qui contient un objet de tableau avec des informations méta supplémentaires, donc nous devons ajouter une petite fonction pour le traitement des données sur le front-end. Elle extraira uniquement les objets imbriqués dont nous avons besoin et les placera dans un seul tableau. Cela est dû au fait que Flexmonster accepte un tableau d'objets JSON sans niveaux imbriqués.

```javascript
function processData(dataset) {
    var result = []
    dataset = JSON.parse(dataset);
    dataset.forEach(item => result.push(item.fields));
    return result;
}
```

Après avoir traité les données, le composant les reçoit dans le bon format et effectue tout le travail difficile de visualisation des données. Un énorme avantage est qu'il n'est pas nécessaire de regrouper ou d'agréger manuellement les valeurs des objets.

Voici à quoi ressemble l'ensemble du script dans le template :

```javascript
function processData(dataset) {
    var result = []
    dataset = JSON.parse(dataset);
    dataset.forEach(item => result.push(item.fields));
    return result;
}
$.ajax({
    url: $("#pivot-table-container").attr("data-url"),
    dataType: 'json',
    success: function(data) {
        new Flexmonster({
            container: "#pivot-table-container",
            componentFolder: "https://cdn.flexmonster.com/",
            width: "100%",
            height: 430,
            toolbar: true,
            report: {
                dataSource: {
                    type: "json",
                    data: processData(data)
                },
                slice: {}
            }
        });
        new Flexmonster({
            container: "#pivot-chart-container",
            componentFolder: "https://cdn.flexmonster.com/",
            width: "100%",
            height: 430,
            //toolbar: true,
            report: {
                dataSource: {
                    type: "json",
                    data: processData(data)
                },
                slice: {},
                "options": {
                    "viewType": "charts",
                    "chart": {
                        "type": "pie"
                    }
                }
            }
        });
    }
});
```

N'oubliez pas d'encadrer ce code JavaScript dans des balises `<script>`. 

_Ouf ! Nous y sommes presque avec cette application._

## Personnalisation des champs

Flexmonster fournit une propriété spéciale de la source de données qui permet de définir les types de données des champs, les légendes personnalisées et de définir des hiérarchies multi-niveaux.

C'est une fonctionnalité agréable à avoir - nous pouvons élégamment séparer les données et leur présentation directement dans la configuration du rapport.

Ajoutez-la à la propriété `dataSource` du rapport :

```javascript
mapping: {
    "product_category": {
        "caption": "Catégorie de produit",
        "type": "string"
    },
    "payment_method": {
        "caption": "Méthode de paiement",
        "type": "string"
    },
    "shipping_cost": {
        "caption": "Coût de livraison",
        "type": "number"
    },
    "unit_price": {
        "caption": "Prix unitaire",
        "type": "number"
    }
}
```

## Conception du tableau de bord

Pour créer le tableau de bord, nous avons rendu deux instances de Flexmonster (vous pouvez en créer autant que vous le souhaitez, en fonction des objectifs de visualisation de données que vous souhaitez atteindre). L'une est pour le tableau croisé dynamique avec des données résumées, et l'autre est pour les graphiques. 

Les deux instances partagent la même source de données de notre modèle. Je vous encourage à essayer de les faire fonctionner en synchronisation : avec l'événement `[reportchange](https://www.flexmonster.com/api/reportchange/?r=fr5)`, vous pouvez faire en sorte qu'une instance réagisse aux changements dans une autre.

Vous pouvez également redéfinir la fonctionnalité du bouton 'Export' sur la barre d'outils pour qu'il sauvegarde vos rapports sur le serveur.

## Résultats

Démarrons le serveur de développement Django et ouvrons [`http://127.0.0.1:8000/dashboard/`](http://127.0.0.1:8000/dashboard/) pour voir le tableau de bord résultant :

![Image](https://www.freecodecamp.org/news/content/images/2020/02/DjangoFlexmonster.gif)

Cela a l'air bien, n'est-ce pas ?

## Feedback

Cette fois, nous avons appris **comment créer une application Django simple** et afficher les données côté client sous la forme d'un **tableau de bord analytique**.

J'espère que vous avez apprécié le tutoriel !

Veuillez laisser vos commentaires ci-dessous - tout retour sur l'amélioration du code est grandement apprécié.

## Références

Le code source du tutoriel peut être trouvé sur [GitHub](https://github.com/veronikaro/django-dashboard-app).

Et voici le projet avec [l'intégration de Flexmonster & Django](https://www.flexmonster.com/doc/integration-with-django/?r=fr5) qui m'a inspiré pour ce tutoriel.

Ensuite, je recommande de parcourir les concepts importants dans la documentation pour maîtriser Django :

* [Migrations dans Django](https://docs.djangoproject.com/en/3.0/topics/migrations/)
* [QuerySets](https://docs.djangoproject.com/en/3.0/ref/models/querysets/)
* [Sérialisation des objets Django](https://docs.djangoproject.com/en/3.0/topics/serialization/)