---
title: Comment créer un tableau de bord basé sur le web avec Django, MongoDB et Pivot
  Table
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-04-28T14:48:02.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-web-based-dashboard-with-django-mongodb-and-pivot-table
coverImage: https://www.freecodecamp.org/news/content/images/2020/04/animation--2--1.gif
tags: []
seo_title: Comment créer un tableau de bord basé sur le web avec Django, MongoDB et
  Pivot Table
seo_desc: "By Veronika Rovnik\nHi, the freeCodeCamp community!\nIn this tutorial,\
  \ I’d like to share with you an approach to data visualization in Python which you\
  \ can further apply in the Django development. \nIf you ever encountered the necessity\
  \ to build an inte..."
---

Par Veronika Rovnik

Bonjour, la communauté freeCodeCamp !

Dans ce tutoriel, je souhaite partager avec vous une approche de la visualisation de données en Python que vous pourrez appliquer dans le développement Django.

Si vous avez déjà eu besoin de créer un **tableau de bord interactif** ou si vous souhaitez essayer, vous êtes les bienvenus pour suivre les étapes de ce tutoriel.

Si vous avez des questions concernant le processus, n'hésitez pas à les poser dans les commentaires. Je serai heureuse de vous aider.

Voici la liste des compétences que vous allez maîtriser à la fin de ce tutoriel :

* Comment créer une application **Django** basique
* Comment héberger des données **MongoDB** distantes dans **MongoDB Atlas**
* Comment importer des données **JSON** et **CSV** dans **MongoDB**
* Comment ajouter un **outil de reporting** à l'application Django

Commençons ! ??????

## Prérequis

* Connaissance de base du développement web
* Bonne connaissance de **Python**
* Expérience de base avec les bases de données **NoSQL** (par exemple, MongoDB)

## Outils

* **Django** - un framework web Python de haut niveau.
* **MongoDB Atlas** - un service de base de données cloud pour les applications modernes. Ici, nous hébergerons notre base de données MongoDB.
* **Flexmonster Pivot Table & Charts** - un composant web JavaScript pour le reporting. Il gérera les tâches de visualisation de données côté client.
* **Le connecteur MongoDB pour Flexmonster** - un outil côté serveur pour une communication rapide entre Pivot Table et MongoDB.
* **PyCharm Community Edition** - un IDE pour le développement Python.
* Données **Kaggle**

## Établir un projet Django

Si vous êtes nouveau dans le développement Django, ce n'est pas grave. Nous allons configurer tout étape par étape pour rendre notre application exceptionnelle.

* Assurez-vous d'avoir préalablement [installé Django sur votre machine](https://docs.djangoproject.com/en/3.0/topics/install/#installing-an-official-release-with-pip).
* Tout d'abord, ouvrez le répertoire où vous souhaitez créer votre projet. Ouvrez la console et exécutez la commande suivante pour créer un nouveau projet Django :

_`django-admin startproject django_reporting_project`_

* Ensuite, naviguez vers ce projet :

_`cd django_reporting_project`_

* Vérifions si tout fonctionne comme prévu. Lancez le serveur Django :

_`python manage.py runserver`_

Sauf indication contraire, le serveur de développement démarre sur le port **8000**. Ouvrez [`http://127.0.0.1:8000/`](http://127.0.0.1:8000/) dans votre navigateur. Si vous voyez cette fusée, nous sommes sur la bonne voie !

![Image](https://lh4.googleusercontent.com/_lqtoZcHe7ESb0dKXfqmjHGvWG8pW7Bek734ML7YnIafTKncYYaRdPrZbO-Kwef8U4WcRzAYJett_QV5QWrAwND2JbxJl4x6c-HREBAvoMwvvpctdhwGHq6otm63nD8-cuN5EzE_)

## Créer une application

Il est maintenant temps de créer notre application avec des fonctionnalités de reporting.

> _Si vous ne vous sentez pas à l'aise avec la différence entre les projets et les applications dans Django, voici un [guide rapide](https://learndjango.com/tutorials/django-best-practices-projects-vs-apps) pour vous aider à comprendre._

* Appelons-la _`dashboard`_ :

_`python manage.py startapp dashboard`_

* Ensuite, ouvrez le projet dans votre IDE préféré. Je recommande vivement d'utiliser **PyCharm** car il rend le processus de programmation en Python très agréable. Il gère également de manière pratique la création d'un environnement virtuel isolé spécifique au projet.
* Après la création de l'application, il est nécessaire de l'enregistrer au niveau du projet. Ouvrez le fichier _`django_reporting_project/settings.py`_ et ajoutez le nom de l'application à la fin de la liste _`INSTALLED_APPS`_ :

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

Hourra ! Maintenant, le projet connaît l'existence de votre application et nous sommes prêts à passer à la configuration de la base de données.

## Configurer une base de données MongoDB en utilisant MongoDB Atlas

Mettons de côté l'application jusqu'à ce que nous ayons terminé la configuration de notre base de données. Je suggère de pratiquer la création de la base de données MongoDB distante en l'hébergeant sur MongoDB Atlas, un service de base de données cloud pour les applications. Alternativement, vous pouvez préparer une base de données locale et travailler avec elle de manière pratique (par exemple, via [MongoDB Compass](https://www.mongodb.com/products/compass) ou le [mongo shell](https://docs.mongodb.com/manual/mongo/)).

* Après vous être connecté à votre compte MongoDB, créez notre premier projet. Appelons-le _`ECommerceData`_ :

![Image](https://lh3.googleusercontent.com/fySeUI8EiBjYHRWLtt9LNNEsAilie8bDcEhpOEYWca-t1t4f44CYdx9XsABCoRQogCHw1MmsX61f4w3PW78j-XQ7eYNM3TOkzAfVPhQN8N-3zb1DwgHsqq8ihaEpk7zHuo39rN93)

* Ensuite, ajoutez des membres (si nécessaire) et définissez les permissions. Vous pouvez inviter des utilisateurs à participer à votre projet via leur adresse e-mail.
* Créez un cluster :

![Image](https://lh4.googleusercontent.com/I3Z6F1uTTSJsGlylgR-Fe0Jvk6AuljINzT7DDBXiMWQJJcQ93PPJJi0xQqn3ZqqwivEHvaKN1XA5DjaM9nUJOAoFmUcGfJE0UBSgaOS1_UT5el94yqto_oGadfuEWHS7HLVT4PAN)

* Choisissez le plan. Puisque nous sommes en phase d'apprentissage, le plan gratuit le plus simple sera suffisant pour nos besoins.
* Sélectionnez un fournisseur cloud et une région. Les régions recommandées sont déduites via votre localisation et marquées avec des étoiles.
* Donnez un nom significatif à notre tout nouveau cluster. Notez qu'il ne peut pas être changé plus tard. Appelons-le _`ReportingData`_ :

![Image](https://lh3.googleusercontent.com/b3Lic8LQJcVHqB2pVGUMzyca817PTI3HSGAg_RvxEE8w12-qZjG6ZNIQxy7fCTlaMBPARyOOAZ1k1iKMgu3ZL4GNhnDY3Ut9jYDJx5cl83Gpcf6qLEGGZ_TvloST6K6cZ9vRj17Z)

## Préparer les données

Pendant que vous attendez que votre cluster soit créé, examinons de plus près les données avec lesquelles nous allons travailler. Pour ce tutoriel, nous allons utiliser [le jeu de données Kaggle](https://www.kaggle.com/carrie1/ecommerce-data) avec des transactions d'un détaillant britannique. En utilisant ces données, nous allons essayer de construire un rapport significatif qui peut servir à l'_analyse exploratoire des données_ au sein d'une organisation réelle.

En outre, nous allons utiliser des données **JSON** fictives sur le marketing. Cela nous aidera à atteindre l'objectif d'établir différents outils de reporting au sein de la même application. Vous pouvez choisir n'importe quelles données de votre préférence.

## Se connecter à votre cluster

Maintenant que notre cluster est prêt, connectons-nous à celui-ci !

* Ajoutez votre adresse IP actuelle à la liste blanche ou ajoutez une autre adresse.
* Créez un utilisateur MongoDB. Le premier aura des permissions _atlasAdmin_ pour le projet actuel, ce qui signifie qu'il possède [les rôles et actions de privilèges suivants](https://docs.atlas.mongodb.com/security-add-mongodb-users/#Atlas-admin). Pour des raisons de sécurité, il est recommandé de générer automatiquement un mot de passe fort.
* Choisissez une **méthode de connexion** qui vous convient le mieux. Pour tester la connexion, nous pouvons d'abord utiliser la chaîne de connexion pour le mongo shell. Plus tard, nous utiliserons également une chaîne de connexion pour une application.

![Image](https://lh3.googleusercontent.com/SrmLY8KbbhYdm8ljnv_MlY7oCQI04PCeVVt3IcgbvoOdeg3D02UvDbiFLD53J-8sE09-j2wWx57WlCbSBy4Igv1HIdmpNkkd4RFaOEjhDxE5dhqoVwiAL-hZB76GhLyZSRYo7ETE)

* Connectez-vous via le mongo shell. Ouvrez la ligne de commande et exécutez ce qui suit :

_`mongo "mongodb+srv://reportingdata-n8b3j.mongodb.net/test"  --username yourUserName`_

L'invite interactive vous demandera un mot de passe pour l'authentification.

## Vérifier les métriques du cluster

Ouf ! Nous y sommes presque.

Maintenant, retournez à la page avec le résumé du cluster et voyez comment il a pris vie ! À partir de maintenant, nous pouvons obtenir des informations sur les opérations d'écriture et de lecture de la base de données MongoDB, le nombre de connexions actives, la taille logique de notre ensemble de réplicas - toutes ces informations statistiques sont à votre disposition. Mais surtout, il est maintenant possible de _créer et gérer des bases de données et des collections._

## Créer une base de données

Créez votre première base de données et deux collections. Appelons-les _ecommerce_, _transactions_, et _marketing_ respectivement.

Voici à quoi ressemble notre espace de travail maintenant :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-235.png)

Cela semble assez vide, n'est-ce pas ?

## Importer des données dans MongoDB

_Peuplons la collection avec des données_. Nous commencerons par les données de détail précédemment téléchargées depuis [**Kaggle**](https://www.kaggle.com/carrie1/ecommerce-data).

* Décompressez l'archive et naviguez jusqu'au répertoire où son contenu est stocké.
* Ensuite, ouvrez l'invite de commande et importez les données dans la collection _**transactions**_ de la base de données **_ecommerce_** en utilisant la commande _`mongoimport`_ et la chaîne de connexion donnée pour le mongo shell :

_`mongoimport --uri "mongodb+srv://username:password@reportingdata-n8b3j.mongodb.net/ecommerce?retryWrites=true&w=majority" --collection transactions --drop --type csv --headerline --file data.csv`_

⚠️Veuillez vous souvenir de remplacer les mots-clés _username_ et _password_ par **vos identifiants**.

---

Félicitations ! _Nous venons de télécharger 541909 documents dans notre collection_. **Qu'est-ce qui suit ?**

* Téléchargez le jeu de données avec les métriques marketing dans la collection _**marketing**_. Voici le [fichier **JSON**](https://gist.github.com/veronikaro/b631874a1681b89506ba5b9880889e8e) avec les données d'exemple que nous allons utiliser.

Importez le tableau JSON dans la collection en utilisant la commande suivante :

_`mongoimport --uri "mongodb+srv://username:password@reportingdata-n8b3j.mongodb.net/ecommerce?retryWrites=true&w=majority" --collection marketing --drop --jsonArray marketing_data.json`_

Si ces données ne suffisent pas, nous pourrions générer dynamiquement plus de données en utilisant les modèles **mongoengine / PyMongo**. C'est ce à quoi sera dédié notre prochain tutoriel de cette série. Mais pour l'instant, nous allons sauter cette partie et travailler avec les données que nous avons déjà.

---

Maintenant que nos collections contiennent des données, nous pouvons explorer le nombre de documents dans chaque collection ainsi que leur structure. Pour plus d'informations, je recommande d'utiliser **MongoDB Compass**, l'outil GUI officiel pour MongoDB. Avec celui-ci, vous pouvez explorer la structure de chaque collection, vérifier la distribution des types de champs, construire des pipelines d'agrégation, exécuter des requêtes, évaluer et optimiser leurs performances. Pour commencer, [téléchargez l'application](https://www.mongodb.com/download-center/compass) et utilisez la chaîne de connexion pour Compass fournie par MongoDB Atlas.

## Mapper les motifs d'URL aux vues

Retour à Django.

* Créez _`urls.py`_ dans le dossier de l'application (à l'intérieur de _`dashboard`_). Ici, nous stockerons les routes URL pour notre application. Ces motifs d'URL seront associés aux vues définies dans `dashboard/views.py` :

```python
from django.urls import path
from . import views

urlpatterns = [
    path('report/retail', views.ecommerce_report_page, name='retail_report'),
    path('report/marketing', views.marketing_report_page, name='marketing_report'),
]

```

* Les URL de l'application doivent être enregistrées au niveau du projet. Ouvrez _`django-reporting-project/urls.py`_ et remplacez le contenu par le code suivant :

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),
]
```

## Créer des vues

Une vue est simplement une fonction qui accepte une requête web et retourne une réponse web. La réponse peut être de n'importe quel type. En utilisant la fonction [render()](https://docs.djangoproject.com/en/3.0/topics/http/shortcuts/#render), nous retournerons un modèle HTML et un contexte combinés en un seul objet [HttpResponse](https://docs.djangoproject.com/en/3.0/ref/request-response/). Notez que les vues dans Django peuvent également être [basées sur des classes](https://docs.djangoproject.com/en/3.0/topics/class-based-views/).

* Dans _`dashboard/views.py`_, créons deux vues simples pour nos rapports :

```python
from django.shortcuts import render


def ecommerce_report_page(request):
   return render(request, 'retail_report.html', {})


def marketing_report_page(request):
   return render(request, 'marketing_report.html', {})

```

## Créer des templates

* Tout d'abord, créez le dossier _`templates`_ à l'intérieur du répertoire de votre application. C'est là que Django recherchera vos pages HTML.

* Ensuite, concevons la mise en page de notre application. Je suggère d'ajouter une barre de navigation qui sera affichée sur chaque page. Pour cela, nous créerons un template de base appelé _`base.html`_ que toutes les autres pages étendront selon la logique métier. De cette façon, nous tirerons parti de **l'héritage de template** - une partie puissante du moteur de template de Django. Veuillez trouver le code HTML sur [GitHub](https://gist.github.com/veronikaro/9bc763f5717f86872420ab30357e4573).

Comme vous l'avez peut-être remarqué, nous allons utiliser les styles Bootstrap. Cela permet de rendre nos pages plus jolies avec des composants UI prêts à l'emploi.

Notez que dans la barre de navigation, nous avons ajouté deux liens qui redirigent vers les pages de rapport. Vous pouvez le faire en définissant la propriété _`href`_ du lien sur le nom du motif d'URL, spécifié par le mot-clé _name_ dans le motif d'URL. Par exemple, de la manière suivante :

_`href="{% url 'marketing_report' %}"`_

* Il est temps de créer des pages où les rapports seront situés. Permettez-moi de vous montrer comment créer un rapport de détail en premier. En suivant ces principes, vous pouvez créer autant d'autres pages de rapport que vous le souhaitez.

1. Dans les templates, créez _`marketing_report.html`_.
2. Ajoutez une balise **extends** pour hériter du template de base : `{% extends "base.html" %}`
3. Ajoutez une balise **block** pour définir le _content_ de notre template enfant : `{% block content %}  
{% endblock %}`
4. Dans le bloc, ajoutez les scripts Flexmonster et les conteneurs où les composants de reporting seront placés (c'est-à-dire, le tableau croisé dynamique et les graphiques croisés dynamiques) : `<script src="https://cdn.flexmonster.com/flexmonster.js"></script> <div id="pivot"></div>  
<div id="pivot_chart"></div>`
5. Ajoutez des balises `<script>` où le code JavaScript sera exécuté. Dans ces balises, instanciez deux objets Flexmonster en utilisant des [appels API init](https://www.flexmonster.com/api/new-flexmonster/).

```javascript
var pivot = new Flexmonster({
    container: "#pivot",
    componentFolder: "https://cdn.flexmonster.com/",
    height: 600,
    toolbar: true,
    report: {}
});
var pivot_charts = new Flexmonster({
    container: "#pivot_charts",
    componentFolder: "https://cdn.flexmonster.com/",
    height: 600,
    toolbar: true,
    report: {}
});
```

Vous pouvez placer autant de composants Flexmonster que vous le souhaitez. Plus tard, nous remplirons ces composants avec des données et composerons des rapports personnalisés.

## Configurer le connecteur MongoDB

Pour établir une communication efficace entre Flexmonster Pivot Table et la base de données MongoDB, nous pouvons utiliser le [Connecteur MongoDB](https://www.flexmonster.com/doc/how-to-connect-to-mongodb/?r=fr6) fourni par Flexmonster. Il s'agit d'un outil côté serveur qui fait tout le travail difficile pour nous, à savoir :

1. se connecte à la base de données MongoDB
2. obtient la structure de la collection
3. interroge les données chaque fois que la structure du rapport est modifiée
4. envoie les données agrégées pour les afficher dans le tableau croisé dynamique.

Pour l'exécuter, clonons [cet exemple depuis GitHub](https://github.com/flexmonster/pivot-mongo), naviguons jusqu'à son répertoire et installons les packages npm en exécutant _npm install_.

* Dans _`src/server.ts`_, vous pouvez vérifier sur quel port le connecteur sera exécuté. Vous pouvez changer celui par défaut. Ici, vous pouvez également spécifier quel module gérera les requêtes arrivant à l'endpoint ( `mongo.ts` dans notre cas).
* Après, spécifiez les identifiants de la base de données dans _`src/controller/mongo.ts`_. Là, ajoutez la chaîne de connexion pour l'application fournie par MongoDB Atlas et spécifiez le nom de la base de données.

## Définir les rapports

Maintenant, nous sommes prêts à définir la configuration du rapport côté client.

* Voici une configuration minimale qui fait fonctionner le tableau croisé dynamique avec les données MongoDB via le connecteur :

```javascript
var pivot = new Flexmonster({
    container: "#pivot",
    componentFolder: "https://cdn.flexmonster.com/",
    height: 600,
    toolbar: true,
    report: {
        "dataSource": {
            "type": "api",
            "url": "http://localhost:9204/mongo", // l'url où notre connecteur est en cours d'exécution
            "index": "marketing" // spécifiez le nom de la collection
        },
        "slice": {}
    }
});
```

* Spécifiez une **slice** - l'ensemble des hiérarchies qui seront affichées sur la grille ou sur le graphique. Voici la configuration d'exemple pour la grille pivot.


```javascript
"slice": {
        "rows": [
            {
                "uniqueName": "Country"
            }
        ],
        "columns": [
            {
                "uniqueName": "[Measures]"
            }
        ],
        "measures": [
            {
                "uniqueName": "Leads",
                "aggregation": "sum"
            },
            {
                "uniqueName": "Opportunities",
                "aggregation": "sum"
            }
        ]
    }
```

## Exécuter votre application de reporting

Maintenant que nous avons configuré le côté client, naviguons jusqu'au répertoire du connecteur MongoDB et lançons le serveur :

_`npm run build`_

_`npm run start`_

* Ensuite, retournez au projet PyCharm et lancez le serveur Django :
_`python manage.py runserver`_
* Ouvrez [`http://127.0.0.1:8000/report/marketing`](http://127.0.0.1:8000/report/). Pour passer à un autre rapport, cliquez sur le nom du rapport dans la barre de navigation.

Il est temps d'évaluer les résultats ! Voici le rapport pour le département marketing :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/freeCodeCampMongo.gif)

Essayez d'expérimenter avec la mise en page :

* **Découpez** et **tranchez** les données pour obtenir votre perspective unique.
* Changez les fonctions de **résumé**, **filtrez** et **triez** les enregistrements.
* Passez de la forme **classique** à la forme **compacte** pour savoir ce qui est le mieux.

## Profitez du tableau de bord analytique en Python

Félicitations ! Excellent travail. Nous avons donné vie à nos données. Maintenant, vous avez une puissante **application Django** avec des fonctionnalités de **reporting** et de **visualisation de données**. 

Ce que vos utilisateurs finaux peuvent trouver extrêmement confortable, c'est qu'il est possible de configurer un rapport, de l'enregistrer et de reprendre là où vous vous êtes arrêté plus tard en le chargeant dans le tableau croisé dynamique. Les rapports sont des fichiers **JSON** soignés qui peuvent être stockés localement ou sur le serveur. De plus, il est possible d'exporter des rapports dans des fichiers **PDF**, **HTML**, **Image** ou **Excel**. 

N'hésitez pas à adapter l'application selon vos besoins métiers ! Vous pouvez ajouter une logique plus complexe, changer la _source de données_ (par exemple, _MySQL_, _PostgreSQL_, _Oracle_, _Microsoft Analysis Services_, _Elasticsearch_, etc), et personnaliser l'apparence et/ou la fonctionnalité du tableau croisé dynamique et des graphiques croisés dynamiques.

## Lectures complémentaires

* [**Code complet sur GitHub**](https://github.com/veronikaro/analytics-django-mongodb) ⭐
* Un [guide complet](https://docs.atlas.mongodb.com/getting-started/) sur la façon de commencer avec MongoDB Atlas
* [Prise en main de Flexmonster Pivot Table & Charts](https://www.flexmonster.com/doc/how-to-create-js-pivottable/?r=fr6)
* [Prise en main de Django](https://docs.djangoproject.com/en/3.0/intro/)
* [Introduction au connecteur MongoDB](https://www.flexmonster.com/doc/mongodb-connector/?r=fr6)
* L'[API du connecteur MongoDB](https://www.flexmonster.com/api/all-methods/?r=fr6)
* [Comment changer les thèmes des rapports](https://www.flexmonster.com/demos/themes/?r=fr6)
* [Comment localiser le composant de tableau croisé dynamique](https://www.flexmonster.com/demos/localization/?r=fr6)

## Paramètres supplémentaires pour embellir votre rapport

Voici une section supplémentaire pour les esprits curieux !

Pour embellir les légendes des hiérarchies et définir les types de champs, nous allons ajouter un **[mapping](https://www.flexmonster.com/doc/mapping/?r=fr6)** - un objet spécial dans la configuration de la source de données du rapport. **Mapping** nous aide à définir comment afficher les noms des champs en définissant des légendes. De plus, il est possible de définir explicitement les types de champs (nombres, chaînes, différents types de dates). Chaque partie de la configuration dépend de votre logique métier.

_En général, le mapping crée un niveau supplémentaire d'abstraction entre la source de données et sa représentation._

Voici un exemple de la façon dont il peut être défini pour le jeu de données de détail :

```javascript
"mapping": {
    "InvoiceNo": {
        "caption": "Numéro de facture",
        "type": "string"
    },
    "StockCode": {
        "caption": "Code de stock",
        "type": "string"
    },
    "Description": {
        "type": "string"
    },
    "Quantity": {
        "type": "number"
    },
    "InvoiceDate": {
        "type": "string",
        "caption": "Date de facture"
    },
    "UnitPrice": {
        "type": "number",
        "caption": "Prix unitaire"
    },
    "CustomerID": {
        "type": "string",
        "caption": "ID du client"
    },
    "Country": {
        "type": "string"
    }
}
```

##