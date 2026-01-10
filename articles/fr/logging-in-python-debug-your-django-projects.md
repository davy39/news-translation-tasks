---
title: Journalisation en Python – Comment utiliser les logs pour déboguer vos projets
  Django
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-08-31T20:46:24.000Z'
originalURL: https://freecodecamp.org/news/logging-in-python-debug-your-django-projects
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/Django-Logger.png
tags:
- name: debugging
  slug: debugging
- name: Django
  slug: django
- name: logging
  slug: logging
- name: Python
  slug: python
seo_title: Journalisation en Python – Comment utiliser les logs pour déboguer vos
  projets Django
seo_desc: "By Md. Saifur Rahman\nThe only perfect code is code that has never been\
  \ written. As a developer, you are bound to face errors and will be responsible\
  \ for debugging them. \nIf you're coding in Python, you can always look at its error\
  \ messages to figure ..."
---

Par Md. Saifur Rahman

Le seul code parfait est celui qui n'a jamais été écrit. En tant que développeur, vous êtes amené à rencontrer des erreurs et serez responsable de leur débogage. 

Si vous codez en Python, vous pouvez toujours consulter ses messages d'erreur pour comprendre ce qui se passe. Mais que faire si une erreur survient et que vous n'avez aucune idée de ce qui casse votre code ? 

Quelque chose pourrait être étrangement incorrect en arrière-plan, mais vous ne parvenez pas à l'identifier. Vous pouvez toujours éteindre et rallumer – ou mieux encore, vous pouvez vérifier les logs.

## Qu'est-ce que la journalisation ?

Si une erreur survient ou si votre application décide de fonctionner étrangement, vos fichiers de log seront utiles. Vous pouvez les parcourir et découvrir où exactement l'application rencontre des problèmes et comment vous pouvez reproduire ces problèmes.

En reproduisant le problème, vous pouvez creuser plus profondément et trouver une solution raisonnable pour les erreurs. Quelque chose qui pourrait autrement prendre plusieurs heures à détecter pourrait ne prendre que quelques minutes à diagnostiquer avec la présence de fichiers de log.

## Comment fonctionne la journalisation dans Django

Heureusement, Django prend en charge la journalisation et la plupart du travail difficile a déjà été fait par ses développeurs. Django utilise le module de journalisation intégré de Python pour exploiter la journalisation système. 

Le module de journalisation Python comporte quatre parties principales :

1. [Loggers](#heading-1-loggers)
2. [Handlers](#heading-2-handlers)
3. [Filters](#heading-3-filters)
4. [Formatters](#heading-4-formatters)

Chaque composant est expliqué méticuleusement dans la [Documentation officielle de Django](https://docs.djangoproject.com/en/3.2/topics/logging/). Je ne veux pas vous submerger avec sa complexité, donc je vais expliquer chaque partie brièvement :

<h3 id="loggers">1. Loggers</h3>

Les loggers sont essentiellement le point d'entrée du système de journalisation. C'est ce avec quoi vous allez réellement travailler en tant que développeur. 

Lorsque qu'un message est reçu par le logger, le niveau de log est comparé au niveau de log du logger. Si il est le même ou dépasse le niveau de log du logger, **le message est envoyé au handler pour un traitement ultérieur.** Les niveaux de log sont :

* **DEBUG :** Informations système de bas niveau
* **INFO :** Informations générales du système
* **WARNING :** Informations sur les problèmes mineurs
* **ERROR :** Informations sur les problèmes majeurs
* **CRITICAL :** Informations sur les problèmes critiques

<h3 id="handlers">2. Handlers</h3>

Les handlers déterminent essentiellement ce qui arrive à chaque message dans un logger. Ils ont les mêmes niveaux de log que les Loggers. Mais, nous pouvons essentiellement définir la manière dont nous voulons traiter chaque niveau de log. 

Par exemple : les messages de niveau de log **ERROR** peuvent être envoyés en temps réel au développeur, tandis que les niveaux de log **INFO** peuvent simplement être stockés dans un fichier système.

Il indique essentiellement au système quoi faire avec le message, comme l'écrire à l'écran, dans un fichier, ou sur une socket réseau.

<h3 id="filters">3. Filtres</h3>

Un filtre peut se situer entre un **Logger** et un **Handler**. Il peut être utilisé pour filtrer l'enregistrement du log. 

Par exemple : dans les messages **CRITICAL**, vous pouvez définir un filtre qui ne permet de traiter qu'une source particulière.

<h3 id="formatters">4. Formatters</h3>

Comme le nom l'indique, les formatters décrivent le format du texte qui sera rendu.

Maintenant que nous avons couvert les bases, creusons plus profondément avec un exemple concret. [Cliquez ici pour le code source](https://github.com/sa1if3/django-logging-tutorial). 

**Veuillez noter que ce tutoriel suppose que vous êtes déjà familiarisé avec les bases de Django.**

## Installation du projet

Tout d'abord, créez un environnement virtuel appelé **`venv`** dans votre dossier de projet `django-logging-tutorial` avec la commande ci-dessous et activez-le.

``` bash
mkdir django-logging-tutorial
virtualenv venv
source venv/bin/activate

Créez un nouveau projet Django appelé `django_logging_tutorial`. Remarquez que le nom du dossier de projet est avec un trait d'union tandis que le nom du projet est avec un trait de soulignement (- vs _). Nous allons également exécuter une série de commandes rapidement pour configurer notre projet.

## Comment configurer vos fichiers de log

Configurons d'abord le fichier `settings.py` de notre projet. Attention – remarquez mes commentaires dans le code qui vous aideront à mieux comprendre ce processus. 

Ce code est également mentionné dans le [3ème exemple de la documentation officielle](https://docs.djangoproject.com/en/3.2/topics/logging/#examples) et dans la plupart de nos projets, il conviendra parfaitement. Je l'ai légèrement modifié pour le rendre plus robuste.

``` python

LOGGING = {
    'version': 1,
    # Le numéro de version de notre log
    'disable_existing_loggers': False,
    # django utilise certains de ses propres loggers pour les opérations internes. Au cas où vous voudriez les désactiver, remplacez simplement le False ci-dessus par true.
    # Un handler pour WARNING. Il écrit essentiellement les messages WARNING dans un fichier appelé WARNING.log
    'handlers': {
        'file': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'warning.log',
        },
    },
    # Un logger pour WARNING qui a un handler appelé 'file'. Un logger peut avoir plusieurs handlers
    'loggers': {
       # remarquez le blanc '', habituellement vous mettriez des loggers intégrés comme django ou root ici en fonction de vos besoins
        '': {
            'handlers': ['file'], #remarquez comment la variable file est appelée dans handler qui a été définie ci-dessus
            'level': 'WARNING',
            'propagate': True,
        },
    },
}

Si vous avez lu mes commentaires ci-dessus, vous avez peut-être remarqué que la partie logger était simplement vide. Ce qui signifie essentiellement n'importe quel logger. 

Soyez prudent avec cette approche car la plupart de nos travaux peuvent être satisfaits avec les loggers intégrés de [Django](https://docs.djangoproject.com/en/3.2/topics/logging/#django-s-logging-extensions) comme `django.request` ou `django.db.backends`. 

De plus, pour simplifier, j'ai seulement utilisé un fichier pour stocker les logs. Selon votre cas d'utilisation, vous pourriez également choisir d'envoyer un email lorsque des messages **CRITICAL** ou **ERROR** sont rencontrés. 

Pour en savoir plus à ce sujet, je vous encourage à lire la partie [handler](https://docs.djangoproject.com/en/3.2/topics/logging/#id4) des docs. Les docs peuvent sembler écrasantes au début, mais plus vous vous habituez à les lire, plus vous pourriez découvrir d'autres approches intéressantes ou meilleures. 

Ne vous inquiétez pas si c'est votre première fois avec la documentation. Il y a toujours une première fois pour tout.

J'ai expliqué la plupart du code dans les commentaires, mais nous n'avons pas encore abordé `propagate`. Qu'est-ce que c'est ? 

Lorsque `propagate` est défini sur **True**, un enfant propagera tous ses appels de journalisation au parent. Cela signifie que nous pouvons définir un handler à la racine (parent) de l'arborescence du logger et tous les appels de journalisation dans le sous-arbre (enfant) vont au handler défini dans le parent. 

Il est également important de noter que la hiérarchie est importante ici. Nous pouvons également simplement le configurer comme **True** dans notre projet car cela n'aura pas d'importance dans notre cas puisque il n'y a pas de sous-arbre.

## Comment déclencher des logs en Python

Maintenant, nous devons créer quelques messages de log afin que nous puissions essayer notre configuration dans **`settings.py`**. 

Avoir une page d'accueil par défaut qui affiche simplement '**Bonjour Lecteur de FreeCodeCamp.org :)**' et chaque fois que quelqu'un visite la page, nous notons un message **WARNING** dans notre fichier `warning.log` comme 'La page d'accueil a été consultée à 2021-08-29 22:23:33.551543 heures !'

Allez dans votre application `logging_example`, et dans `views.py` incluez le code suivant. Assurez-vous d'avoir ajouté `logging_example` dans les `INSTALLED_APPS` dans `setting.py`.

``` python

from django.http import HttpResponse
import datetime
# importer la bibliothèque de journalisation
import logging
# Obtenir une instance d'un logger
logger = logging.getLogger(__name__)

def hello_reader(request):
    logger.warning('La page d\'accueil a été consultée à '+str(datetime.datetime.now())+' heures!')
    return HttpResponse("<h1>Bonjour Lecteur de FreeCodeCamp.org :)</h1>")



Dans le fichier `urls.py` du projet, ajoutez le code suivant afin que lorsque nous accédons à la page d'accueil, la bonne fonction soit appelée.

``` python
from django.contrib import admin
from django.urls import path
from logging_example import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.hello_reader, name="hello_reader")
]

## Temps pour quelques tests

Enfin, notre configuration simple est terminée. Tout ce que nous devons faire maintenant est de démarrer notre serveur et de tester notre log.

Lancez le serveur de développement avec cette commande :

``` bash
python manage.py runserver

Maintenant, allez sur votre page d'accueil **127.0.0.1:8000** où vous serez accueilli avec le message que nous avons codé. Maintenant, vérifiez votre fichier `warning.log` dans le chemin créé. Un exemple de sortie est montré ci-dessous :

``` txt
La page d\'accueil a été consultée à 2021-08-29 22:38:29.922510 heures!
La page d\'accueil a été consultée à 2021-08-29 22:48:35.088296 heures!


C'est tout ! Maintenant vous savez comment effectuer la journalisation dans Django. Si vous avez des questions, envoyez-moi simplement un message. Je promets de vous aider :)

Si vous avez trouvé mon article utile et que vous souhaitez en lire plus, veuillez consulter quelques tutoriels Django sur mon blog [Techflow360.com](https://techflow360.com/category/web-development/django/).