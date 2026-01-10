---
title: Projet Python – Comment créer une API d'horoscope avec Beautiful Soup et Flask
subtitle: ''
author: Ashutosh Krishna
co_authors: []
series: null
date: '2021-12-17T18:29:53.000Z'
originalURL: https://freecodecamp.org/news/python-project-build-an-api-with-beautiful-soup-and-flask
coverImage: https://www.freecodecamp.org/news/content/images/2021/12/horoscope-api-1.png
tags:
- name: api
  slug: api
- name: Flask Framework
  slug: flask
- name: Python
  slug: python
- name: web scraping
  slug: web-scraping
seo_title: Projet Python – Comment créer une API d'horoscope avec Beautiful Soup et
  Flask
seo_desc: "Have you ever read your horoscope in the newspaper or seen it on television?\
  \ Well, I'm not sure about other countries, but in my country of India, people still\
  \ read their horoscopes. \nAnd this is where I got the idea for this tutorial. It\
  \ might sound..."
---

Avez-vous déjà lu votre horoscope dans le journal ou à la télévision ? Eh bien, je ne suis pas sûr pour les autres pays, mais dans mon pays, l'Inde, les gens lisent encore leur horoscope. 

Et c'est là que j'ai eu l'idée pour ce tutoriel. Cela peut sembler un peu vieux jeu, mais l'objectif principal ici n'est pas l'horoscope lui-même – c'est juste le véhicule pour notre apprentissage. 

Dans cet article, nous allons scraper un site web appelé [Horoscope.com](https://www.horoscope.com/us/index.aspx) en utilisant Beautiful Soup, puis créer notre propre API en utilisant Flask. Cette API, si elle est déployée sur un serveur public, pourra ensuite être utilisée par d'autres développeurs qui souhaiteraient créer un site web pour afficher leur horoscope ou une application pour la même chose.

## Comment configurer le projet

Tout d'abord, nous allons créer un environnement virtuel dans lequel nous installerons toutes les dépendances requises. 

Python est maintenant livré avec la bibliothèque préinstallée `venv`. Donc, pour créer un environnement virtuel, vous pouvez utiliser la commande suivante :

```bash
$ python -m venv env
```

Pour activer l'environnement virtuel nommé `env`, utilisez la commande :

* Sur Windows :

```terminal
env\Scripts\activate.bat
```

* Sur Linux et MacOS :

```bash
source env/bin/activate
```

Pour désactiver l'environnement (non requis à ce stade) :

```bash
deactivate
```

Nous sommes maintenant prêts à installer les dépendances. Les modules et bibliothèques que nous allons utiliser dans ce projet sont :

<ul>
	<li>requests : <a href="https://docs.python-requests.org/en/latest/">Requests</a> vous permet d'envoyer des requêtes HTTP/1.1 extrêmement facilement. Le module n'est pas préinstallé avec Python, nous devons donc l'installer en utilisant la commande :

	<pre>
<code class="language-bash">$ pip install requests</code></pre>
	</li>
	<li>bs4 : <strong><a href="http://www.crummy.com/software/BeautifulSoup/">Beautiful Soup</a></strong>(bs4) est une bibliothèque Python pour extraire des données des fichiers HTML et XML. Le module n'est pas préinstallé avec Python, nous devons donc l'installer en utilisant la commande :
	<pre>
<code class="language-bash">$ pip install bs4</code></pre>
	</li>
    <li>Flask : <strong><a href="https://flask.palletsprojects.com/">Flask</a></strong> est un microframework simple et facile à utiliser pour Python qui peut aider à construire des applications web scalables et sécurisées. Le module n'est pas préinstallé avec Python, nous devons donc l'installer en utilisant la commande :
	<pre>
<code class="language-bash">$ pip install flask</code></pre>
	</li>
    <li>Flask-RESTX : <strong><a href="https://flask-restx.readthedocs.io/en/latest/quickstart.html">Flask-RESTX</a></strong> vous permet de créer des APIs avec une documentation Swagger. Le module n'est pas préinstallé avec Python, nous devons donc l'installer en utilisant la commande :
	<pre>
<code class="language-bash">$ pip install flask-restx</code></pre>
	</li>
</ul>

Nous allons également utiliser des variables d'environnement dans ce projet. Donc, nous allons installer un autre module appelé **python-decouple** pour gérer cela :

```bash
pip install python-decouple
```

Pour en savoir plus sur les variables d'environnement en Python, vous pouvez consulter [cet article](https://iread.ga/posts/49/do-you-really-need-environment-variables-in-python).

## Workflow du projet

Le workflow de base du projet sera le suivant :

1. Les données de l'horoscope seront scrapées depuis [Horoscope.com](https://www.horoscope.com/us/index.aspx).
2. Les données seront ensuite utilisées par notre serveur Flask pour envoyer une réponse JSON à l'utilisateur.

## Comment configurer un projet Flask

La première chose que nous allons faire est de créer un projet Flask. Si vous consultez la [documentation officielle](https://flask.palletsprojects.com/en/2.0.x/quickstart/) de Flask, vous y trouverez une [application minimale](https://flask.palletsprojects.com/en/2.0.x/quickstart/#a-minimal-application). 

Mais nous ne allons pas suivre cela. Nous allons écrire une application plus extensible et ayant une bonne structure de base. Si vous le souhaitez, vous pouvez suivre [ce guide](https://iread.ga/posts/54/getting-started-with-flask) pour commencer avec Flask.

Notre application existera dans un package appelé **core**. Pour convertir un répertoire habituel en un package Python, nous devons simplement inclure un fichier `__init__.py`. Donc, créons d'abord notre package core.

```bash
$ mkdir core
```

Après cela, créons le fichier `__init__.py` à l'intérieur du répertoire core :

```bash
$ cd core
$ touch __init__.py
$ cd ..
```

Dans le répertoire racine du projet, créez un fichier appelé `config.py`. Nous allons stocker les configurations pour le projet dans ce fichier. À l'intérieur du fichier, ajoutez le contenu suivant :

```python
from decouple import config


class Config(object):
    SECRET_KEY = config('SECRET_KEY', default='guess-me')
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True


class ProductionConfig(Config):
    DEBUG = False
    MAIL_DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True

```

Dans le script ci-dessus, nous avons créé une classe _Config_ et défini divers attributs à l'intérieur. Nous avons également créé différentes classes enfants (selon les différentes étapes du développement) qui héritent de la classe _Config_.

Remarquez que nous avons défini SECRET_KEY sur une variable d'environnement nommée **SECRET_KEY**. Créez un fichier nommé `.env` dans le répertoire racine et ajoutez le contenu suivant :

```env
APP_SETTINGS=config.DevelopmentConfig
SECRET_KEY=gufldksfjsdf
```

En plus de **SECRET_KEY**, nous avons **APP_SETTINGS** qui fait référence à l'une des classes que nous avons créées dans le fichier `config.py`. Nous le définissons à l'étape actuelle du projet.

Maintenant, nous pouvons ajouter le contenu suivant dans le fichier `__init__.py` :

```python
from flask import Flask
from decouple import config
from flask_restx import Api

app = Flask(__name__)
app.config.from_object(config("APP_SETTINGS"))
api = Api(
    app,
    version='1.0',
    title='Horoscope API',
    description='Obtenez facilement des données d\'horoscope en utilisant les APIs ci-dessous',
    license='MIT',
    contact='Ashutosh Krishna',
    contact_url='https://ashutoshkrris.tk',
    contact_email='contact@ashutoshkrris.tk',
    doc='/',
    prefix='/api/v1'
)

```

Dans le script Python ci-dessus, nous importons d'abord la classe Flask du module Flask que nous avons installé. Ensuite, nous créons un objet `app` de la classe Flask. Nous utilisons l'argument `__name__` pour indiquer le module ou le package de l'application, afin que Flask sache où trouver d'autres fichiers tels que les templates. 

Ensuite, nous définissons les configurations de l'application selon **APP_SETTINGS** conformément à la variable dans le fichier `.env`. 

En plus de cela, nous avons créé un objet de la classe _Api_. Nous devons lui passer divers arguments. Nous pouvons trouver la documentation Swagger sur la route `/`. Le `/api/v1` sera préfixé sur chaque route de l'API. 

Pour l'instant, créons un fichier `routes.py` dans le package `core` et ajoutons simplement l'espace de noms suivant :

```py
from core import api
from flask import jsonify

ns = api.namespace('/', description='APIs d\'horoscope')
```

Nous devons importer les routes dans le fichier `__init__.py` :

```python
from flask import Flask
from decouple import config
from flask_restx import Api

app = Flask(__name__)
app.config.from_object(config("APP_SETTINGS"))
api = Api(
    app,
    version='1.0',
    title='Horoscope API',
    description='Obtenez facilement des données d\'horoscope en utilisant les APIs ci-dessous',
    license='MIT',
    contact='Ashutosh Krishna',
    contact_url='https://ashutoshkrris.tk',
    contact_email='contact@ashutoshkrris.tk',
    doc='/',
    prefix='/api/v1'
)

from core import routes			# Ajoutez cette ligne
```

Il ne nous reste plus qu'un fichier qui nous aidera à exécuter le serveur Flask :

```python
from core import app

if __name__ == '__main__':
    app.run()

```

Une fois que vous exécutez ce fichier en utilisant la commande `python main.py`, vous verrez une sortie similaire :

![Image](https://www.freecodecamp.org/news/content/images/2021/12/Screenshot-2021-12-16-160820.png)

Maintenant, nous sommes prêts à scraper les données du site web Horoscope.

## Comment scraper les données de Horoscope.com

Si vous ouvrez [Horoscope.com](https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx) et choisissez votre signe du zodiaque, les données de l'horoscope pour votre signe du zodiaque pour aujourd'hui seront affichées.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/Screenshot-2021-12-16-073450.png)
_Source : Horoscope.com_

Dans l'image ci-dessus, vous pouvez voir que vous pouvez consulter l'horoscope pour hier, demain, la semaine, le mois ou même une date personnalisée. Nous allons utiliser toutes ces options.

Mais d'abord, si vous regardez l'URL de la page actuelle, elle ressemble à quelque chose comme : [https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=10](https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=10). 

L'URL a deux variables, si vous regardez attentivement, **sign** et **today**. La valeur de la variable **sign** sera attribuée selon le signe du zodiaque. La variable **today** peut être remplacée par **yesterday** et **tomorrow**.

Le dictionnaire ci-dessous peut nous aider avec les signes du zodiaque :

```python
ZODIAC_SIGNS = {
    "Aries": 1,
    "Taurus": 2,
    "Gemini": 3,
    "Cancer": 4,
    "Leo": 5,
    "Virgo": 6,
    "Libra": 7,
    "Scorpio": 8,
    "Sagittarius": 9,
    "Capricorn": 10,
    "Aquarius": 11,
    "Pisces": 12
}
```

Cela signifie que si votre signe du zodiaque est **Capricorn**, la valeur de **sign** dans l'URL sera **10**. 

Ensuite, si nous souhaitons obtenir les données de l'horoscope pour une date personnalisée, l'URL [https://www.horoscope.com/us/horoscopes/general/horoscope-archive.aspx?sign=10&laDate=20211213](https://www.horoscope.com/us/horoscopes/general/horoscope-archive.aspx?sign=10&laDate=20211213) nous aidera. 

Elle a la même variable **sign**, mais elle a une autre variable **laDate** qui prend la date au format **YYYYMMDD**. 

Maintenant, nous sommes prêts à créer différentes fonctions pour récupérer les données de l'horoscope. Créez un fichier `utils.py` et suivez les instructions.

### Comment obtenir un horoscope pour le jour

```python
import requests
from bs4 import BeautifulSoup


def get_horoscope_by_day(zodiac_sign: int, day: str):
    if not "-" in day:
        res = requests.get(f"https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-{day}.aspx?sign={zodiac_sign}")
    else:
        day = day.replace("-", "")
        res = requests.get(f"https://www.horoscope.com/us/horoscopes/general/horoscope-archive.aspx?sign={zodiac_sign}&laDate={day}")
    soup = BeautifulSoup(res.content, 'html.parser')
    data = soup.find('div', attrs={'class': 'main-horoscope'})
    return data.p.text
```

Nous avons créé notre première fonction qui accepte deux arguments – un entier **zodiac_sign** et une chaîne **day**. Le jour peut être aujourd'hui, demain, hier ou toute date personnalisée avant aujourd'hui au format YYYY-MM-DD. 

Si le jour n'est pas une date personnalisée, il n'aura pas le symbole de trait d'union (-). Nous avons donc mis une condition pour cela. 

Si le symbole de trait d'union n'est pas présent, nous faisons une requête GET sur `https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-{_day_}.aspx?sign={_zodiac_sign_}`. Sinon, nous changeons d'abord la date du format YYYY-MM-DD au format YYYYMMDD. 

Ensuite, nous faisons une requête GET sur `https://www.horoscope.com/us/horoscopes/general/horoscope-archive.aspx?sign={_zodiac_sign_}&laDate={_day_}`. 

Après cela, nous extrayons les données HTML du contenu de la réponse de la page en utilisant BeautifulSoup. Maintenant, nous devons obtenir le texte de l'horoscope à partir de ce code HTML. Si vous inspectez le code de l'une des pages web, vous trouverez ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/12/screenshot-2021-12-07-081318_nwhwwf.png)

Le texte de l'horoscope est contenu dans une **div** avec la classe **main-horoscope**. Ainsi, nous utilisons la fonction `soup.find()` pour extraire la chaîne de texte du paragraphe et la retourner.

### Comment obtenir un horoscope pour la semaine

```python
def get_horoscope_by_week(zodiac_sign: int):
    res = requests.get(f"https://www.horoscope.com/us/horoscopes/general/horoscope-general-weekly.aspx?sign={zodiac_sign}")
    soup = BeautifulSoup(res.content, 'html.parser')
    data = soup.find('div', attrs={'class': 'main-horoscope'})
    return data.p.text
```

La fonction ci-dessus est assez similaire à la précédente. Nous avons simplement changé l'URL en `https://www.horoscope.com/us/horoscopes/general/horoscope-general-weekly.aspx?sign={_zodiac_sign_}`.

### Comment obtenir un horoscope pour le mois

```python
def get_horoscope_by_month(zodiac_sign: int):
    res = requests.get(f"https://www.horoscope.com/us/horoscopes/general/horoscope-general-monthly.aspx?sign={zodiac_sign}")
    soup = BeautifulSoup(res.content, 'html.parser')
    data = soup.find('div', attrs={'class': 'main-horoscope'})
    return data.p.text

```

Cette fonction est également similaire aux deux autres, à l'exception de l'URL qui a maintenant été changée en `https://www.horoscope.com/us/horoscopes/general/horoscope-general-monthly.aspx?sign={_zodiac_sign_}`.

## Comment créer des routes API

Nous allons utiliser Flask-RESTX pour créer nos routes API. Les routes API ressembleront à ceci :

* Pour les dates quotidiennes ou personnalisées : `/api/v1/get-horoscope/daily?day=today&sign=capricorn` ou `api/v1/get-horoscope/daily?day=2022-12-14&sign=capricorn`
* Pour les données hebdomadaires : `api/v1/get-horoscope/weekly?sign=capricorn`
* Pour les données mensuelles : `api/v1/get-horoscope/monthly?sign=capricorn`

Nous avons deux paramètres de requête dans les URL : **day** et **sign**. Le paramètre **day** peut prendre des valeurs comme today, yesterday, ou des dates personnalisées comme 2022-12-14. Le paramètre **sign** prendra le nom du signe du zodiaque qui peut être en majuscules ou en minuscules, cela n'a pas d'importance.

Pour analyser les paramètres de requête de l'URL, Flask-RESTX a un support intégré pour la validation des données de requête en utilisant une bibliothèque similaire à [**argparse**](https://docs.python.org/3/library/argparse.html#module-argparse) appelée **reqparse**. Pour ajouter des arguments dans l'URL, nous utiliserons la méthode **add_argument** de la classe _RequestParser_.

```python
parser = reqparse.RequestParser()
parser.add_argument('sign', type=str, required=True)

```

Le paramètre `type` prendra le type de paramètre. Le `required=True` rend le paramètre de requête obligatoire.

Maintenant, nous avons besoin d'un autre paramètre de requête day. Mais ce paramètre ne sera utilisé que dans l'URL de l'horoscope quotidien. 

Au lieu de réécrire les arguments, nous pouvons écrire un analyseur parent contenant tous les arguments partagés, puis étendre l'analyseur avec [`copy()`](https://flask-restplus.readthedocs.io/en/stable/api.html#flask_restplus.reqparse.RequestParser.copy).

```python
parser_copy = parser.copy()
parser_copy.add_argument('day', type=str, required=True)
```

Le `parser_copy` contiendra non seulement **day**, mais aussi **sign**. C'est ce dont nous aurons besoin pour l'horoscope quotidien.

Les principaux éléments de construction fournis par Flask-RESTX sont les ressources. Les ressources sont construites sur le dessus des [vues pluggables de Flask](https://flask.palletsprojects.com/en/2.0.x/views/), vous donnant un accès facile à plusieurs méthodes HTTP simplement en définissant des méthodes sur votre ressource. 

Créons la classe _DailyHoroscopeAPI_ qui hérite de la classe _Resource_ de `flask_restx`.

```python
@ns.route('/get-horoscope/daily')
class DailyHoroscopeAPI(Resource):
    '''Affiche l'horoscope quotidien des signes du zodiaque'''
    @ns.doc(parser=parser_copy)
    def get(self):
        args = parser_copy.parse_args()
        day = args.get('day')
        zodiac_sign = args.get('sign')
        try:
            zodiac_num = ZODIAC_SIGNS[zodiac_sign.capitalize()]
            if "-" in day:
                datetime.strptime(day, '%Y-%m-%d')
            horoscope_data = get_horoscope_by_day(zodiac_num, day)
            return jsonify(success=True, data=horoscope_data, status=200)
        except KeyError:
            raise NotFound('Aucun signe du zodiaque n\'existe')
        except AttributeError:
            raise BadRequest(
                'Quelque chose s\'est mal passé, veuillez vérifier l\'URL et les arguments.')
        except ValueError:
            raise BadRequest('Veuillez entrer le jour au format correct : YYYY-MM-DD')
```

Le décorateur `@ns.route()` définit la route de l'API. À l'intérieur de la classe _DailyHoroscopeAPI_, nous avons la méthode **get** qui gérera les requêtes GET. Le décorateur `@ns.doc()` nous aidera à ajouter les paramètres de requête sur l'URL. 

Pour obtenir les valeurs des paramètres de requête, nous utiliserons la méthode **parse_args()** qui nous retournera un dictionnaire comme ceci :

```bash
{'sign': 'capricorn', 'day': '2022-12-14'}
```

Nous pouvons ensuite obtenir les valeurs en utilisant les clés **day** et **sign**.

Comme défini au début, nous aurons un dictionnaire ZODIAC_SIGNS. Nous utilisons un bloc **try-except** pour gérer la requête. Si le signe du zodiaque n'est pas dans le dictionnaire, une exception _KeyError_ est levée. Dans ce cas, nous répondons avec une erreur _NotFound_ (Erreur 404). 

De plus, si le paramètre **day** contient un trait d'union, nous essayons de faire correspondre le format de la date avec YYYY-MM-DD. Si ce n'est pas dans ce format, nous levons une erreur _BadRequest_ (Erreur 400). Si le **day** ne contient pas de trait d'union, nous appelons directement la méthode `get_horoscope_by_day()` avec les arguments **sign** et **day**. 

Si des valeurs absurdes sont passées en tant que valeur de paramètre, une _AttributeError_ est levée. Dans ce cas, nous levons une erreur _BadRequest_.

Les deux autres routes sont également assez similaires à celle ci-dessus. La différence est que nous n'avons pas besoin d'un paramètre day ici. Donc, au lieu d'utiliser `parser_copy`, nous utiliserons `parser` ici.

```python
@ns.route('/get-horoscope/weekly')
class WeeklyHoroscopeAPI(Resource):
    '''Affiche l'horoscope hebdomadaire des signes du zodiaque'''
    @ns.doc(parser=parser)
    def get(self):
        args = parser.parse_args()
        zodiac_sign = args.get('sign')
        try:
            zodiac_num = ZODIAC_SIGNS[zodiac_sign.capitalize()]
            horoscope_data = get_horoscope_by_week(zodiac_num)
            return jsonify(success=True, data=horoscope_data, status=200)
        except KeyError:
            raise NotFound('Aucun signe du zodiaque n\'existe')
        except AttributeError:
            raise BadRequest('Quelque chose s\'est mal passé, veuillez vérifier l\'URL et les arguments.')


@ns.route('/get-horoscope/monthly')
class MonthlyHoroscopeAPI(Resource):
    '''Affiche l'horoscope mensuel des signes du zodiaque'''
    @ns.doc(parser=parser)
    def get(self):
        args = parser.parse_args()
        zodiac_sign = args.get('sign')
        try:
            zodiac_num = ZODIAC_SIGNS[zodiac_sign.capitalize()]
            horoscope_data = get_horoscope_by_month(zodiac_num)
            return jsonify(success=True, data=horoscope_data, status=200)
        except KeyError:
            raise NotFound('Aucun signe du zodiaque n\'existe')
        except AttributeError:
            raise BadRequest('Quelque chose s\'est mal passé, veuillez vérifier l\'URL et les arguments.')

```

Maintenant, nos routes sont terminées. Pour tester les APIs, vous pouvez utiliser la documentation Swagger disponible sur la route `/`, ou vous pouvez utiliser [Postman](https://www.postman.com/). Lançons le serveur et testons-le.

%[https://www.youtube.com/watch?v=yggJPOqr6jc]

Vous pouvez également déployer le projet sur un serveur public afin que d'autres développeurs puissent accéder et utiliser l'API également.

## Conclusion

Dans ce tutoriel, nous avons appris comment scraper des données d'un site web en utilisant requests et Beautiful Soup. Ensuite, nous avons créé une API en utilisant Flask et Flask-RESTX. 

Si vous souhaitez apprendre comment interagir avec des APIs en utilisant Python, consultez [ce guide](https://www.freecodecamp.org/news/how-to-interact-with-web-services-using-python/).

J'espère que vous avez apprécié – et merci d'avoir lu !

Code pour le tutoriel : [https://github.com/ashutoshkrris/Horoscope-API](https://github.com/ashutoshkrris/Horoscope-API)