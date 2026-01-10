---
title: Comment rendre votre code rapide et asynchrone avec Python et Sanic
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-28T08:57:06.000Z'
originalURL: https://freecodecamp.org/news/goin-fast-and-asynchronous-with-python-and-sanic-387d722f3668
coverImage: https://cdn-media-1.freecodecamp.org/images/1*vJxAS5gEDCUgnTntr5eSRg.jpeg
tags:
- name: Sanic
  slug: sanic
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: 'tech '
  slug: tech
seo_title: Comment rendre votre code rapide et asynchrone avec Python et Sanic
seo_desc: 'By Davit Tovmasyan

  Hello everybody. In this article I’ll talk about building simple asynchronous projects
  with the Sanic framework.


  Goin’ Fast

  Introduction

  Sanic is a very flask-like open-source Python web server and web framework with
  more than 10K...'
---

Par Davit Tovmasyan

Bonjour à tous. Dans cet article, je vais parler de la création de projets asynchrones simples avec le framework Sanic.

![Image](https://cdn-media-1.freecodecamp.org/images/F0Jro1PM0OTKI0on7Hz0sEIFNlIb9JWZ58JO)
_Aller Vite_

### Introduction

[Sanic](https://sanicframework.org/) est un serveur web et un framework web open-source très similaire à Flask, avec plus de [10K étoiles](https://github.com/huge-success/sanic), écrit pour aller vite. Il permet l'utilisation de la syntaxe `async/await` ajoutée dans Python 3.5 ([en savoir plus](https://docs.python.org/3/library/asyncio-task.html)), ce qui rend votre code [non-bloquant](https://medium.com/vaidikkapoor/understanding-non-blocking-i-o-with-python-part-1-ec31a2e2db9b) et rapide.

Sanic dispose d'une [documentation](https://sanic.readthedocs.io/en/latest/) assez bonne et il est maintenu par la communauté, pour la communauté.

> Le but du projet est de fournir un moyen simple de mettre en place un serveur HTTP hautement performant, facile à construire, à étendre et finalement à mettre à l'échelle.

### Prérequis

Avant de commencer, installons quelques packages et assurons-nous que tout est prêt pour le développement de ce projet.

_Note : Le code source est disponible dans mon dépôt [github.com](https://github.com/davitovmasyan/sanic-project). Pour chaque étape, il y a un commit correspondant._

#### Conditions préalables :

* Python 3.6+
* [pipenv](https://github.com/pypa/pipenv) (vous pouvez utiliser tout autre installateur de packages)
* [PostgreSQL](https://www.postgresql.org/) (pour la base de données, peut aussi être MySQL ou SQLite)

#### Packages :

* [secure](https://pypi.org/project/secure/) est un package léger qui ajoute des en-têtes de sécurité optionnels et des attributs de cookie pour les frameworks web Python.
* [environs](https://pypi.org/project/environs/) est une bibliothèque Python pour analyser les variables d'environnement. Elle vous permet de stocker la configuration séparément de votre code, selon la méthodologie [The Twelve-Factor App](https://12factor.net/config).
* [sanic-envconfig](https://github.com/jamesstidard/sanic-envconfig) est une extension qui vous aide à intégrer les variables de ligne de commande et d'environnement dans votre configuration Sanic.
* [databases](https://pypi.org/project/databases/) est un package Python qui vous permet de faire des requêtes en utilisant le puissant langage d'expression [SQLAlchemy Core](https://docs.sqlalchemy.org/en/latest/core/), et fournit un support pour PostgreSQL, MySQL et SQLite.

Créons un répertoire vide et initialisons un `Pipfile` vide.

```
pipenv --python python3.6
```

Installez tous les packages nécessaires en utilisant les commandes **pipenv** ci-dessous.

```
pipenv install sanic secure environs sanic-envconfig
```

Pour la base de données :

```
pipenv install databases[postgresql]
```

Les choix sont **postgresql, mysql, sqlite.**

### Structure

Maintenant, créons quelques fichiers et dossiers où nous écrirons notre code réel.

```
├── .env
├── Pipfile
├── Pipfile.lock
├── setup.py
└── project
    ├── __init__.py
    ├── __main__.py
    ├── main.py
    ├── middlewares.py
    ├── routes.py
    ├── settings.py
    └── tables.py
```

Nous utiliserons le fichier `setup.py` pour rendre le dossier `project` disponible en tant que package dans notre code.

```
from setuptools import setup

setup(
    name='project',
)
```

_Installation…_

```
pipenv install -e .
```

Dans le fichier `.env`, nous stockerons quelques variables globales comme l'URL de connexion à la base de données.

`__main__.py` est créé pour rendre notre package `project` exécutable depuis la ligne de commande.

```
pipenv run python -m project
```

### Initialisation

Faisons notre premier appel dans le fichier **__main__.py**.

```
from project.main import init

init()
```

C'est le début de notre application. Maintenant, nous devons créer la fonction `init` à l'intérieur du fichier **main.py**.

```
from sanic import Sanic

app = Sanic(__name__)

def init():
    app.run(host='0.0.0.0', port=8000, debug=True)
```

Simplement en créant l'application à partir de la classe _Sanic_, nous pouvons l'exécuter en spécifiant **host**, **port** et l'argument clé optionnel **debug**.

_Exécution…_

```
pipenv run python -m project
```

![Image](https://cdn-media-1.freecodecamp.org/images/7GwhssZorNRLRt-O9V-Dlm0E9VCqTFqNeOE0)
_Sortie de la console Sanic_

Voici à quoi devrait ressembler une sortie réussie dans votre application Sanic. Si vous ouvrez [http://0.0.0.0:8000](http://0.0.0.0:8000) dans votre navigateur, vous verrez

> Erreur : URL demandée / introuvable

Nous n'avons pas encore créé de **routes**, donc c'est normal pour l'instant. Nous ajouterons quelques routes ci-dessous.

### Paramètres

Maintenant, nous pouvons modifier l'environnement et les paramètres. Nous devons ajouter quelques variables dans le fichier **.env**, les lire et les passer à la configuration de l'application Sanic.

**Fichier _.env_.**

```
DEBUG=True
HOST=0.0.0.0
POST=8000
```

_Configuration…_

```
from sanic import Sanic
```

```
from environs import Env
from project.settings import Settings
```

```
app = Sanic(__name__)
```

```
def init():
    env = Env()
    env.read_env()
    app.config.from_object(Settings)
    app.run(
        host=app.config.HOST,
        port=app.config.PORT,
        debug=app.config.DEBUG,
        auto_reload=app.config.DEBUG,
    )
```

**Fichier _settings.py_.**

```
from sanic_envconfig import EnvConfig

class Settings(EnvConfig):
    DEBUG: bool = True
    HOST: str = '0.0.0.0'
    PORT: int = 8000
```

Veuillez noter que j'ai ajouté un argument optionnel **auto_reload** qui activera ou désactivera le Rechargeur Automatique.

### Base de données

Maintenant, il est temps de configurer une base de données.

Une petite note sur le package **databases** avant de continuer :

> Le package **databases** utilise [asyncpg](https://github.com/MagicStack/asyncpg) qui est une bibliothèque d'interface asynchrone pour PostgreSQL. C'est assez rapide. Voir les résultats ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/RvldCRR3gSuI4UKswmylnrJYrIDQhQ9wetEd)

Nous allons utiliser deux des [listeners](https://sanic.readthedocs.io/en/latest/sanic/middleware.html#listeners) de Sanic où nous spécifierons les opérations de connexion et de déconnexion de la base de données. Voici les listeners que nous allons utiliser :

* **after_server_start**
* **after_server_stop**

**Fichier _main.py_.**

```
from sanic import Sanic
```

```
from databases import Database
```

```
from environs import Env
from project.settings import Settings
```

```
app = Sanic(__name__)
```

```
def setup_database():
    app.db = Database(app.config.DB_URL)
    @app.listener('after_server_start')
    async def connect_to_db(*args, **kwargs):
        await app.db.connect()
    @app.listener('after_server_stop')
    async def disconnect_from_db(*args, **kwargs):
        await app.db.disconnect()
```

```
def init():
    env = Env()
    env.read_env()
    app.config.from_object(Settings)
```

```
    setup_database()
```

```
    app.run(
        host=app.config.HOST,
        port=app.config.PORT,
        debug=app.config.DEBUG,
        auto_reload=app.config.DEBUG,
    )
```

Une dernière chose. Nous devons spécifier **DB_URL** dans les paramètres du projet et l'environnement.

**Fichier _.env_.**

```
DEBUG=True
HOST=0.0.0.0
POST=8000
DB_URL=postgresql://postgres:postgres@localhost/postgres
```

_Et le fichier **settings.py**._

```
from sanic_envconfig import EnvConfig

class Settings(EnvConfig):
    DEBUG: bool = True
    HOST: str = '0.0.0.0'
    PORT: int = 8000
    DB_URL: str = ''
```

Assurez-vous que **DB_URL** est correct et que votre base de données est en cours d'exécution. Maintenant, vous pouvez accéder à la base de données en utilisant **app.db**. Voir plus d'informations détaillées dans la section suivante.

### Tables

Maintenant, nous avons une connexion à notre base de données et nous pouvons essayer de faire quelques requêtes SQL.

Déclarons une table dans le fichier **tables.py** en utilisant SQLAlchemy.

```
import sqlalchemy

metadata = sqlalchemy.MetaData()
books = sqlalchemy.Table(
    'books',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('title', sqlalchemy.String(length=100)),
    sqlalchemy.Column('author', sqlalchemy.String(length=60)),
)
```

Ici, je suppose que vous avez déjà une base de données **migrée** avec une table **books**. Pour créer des migrations de base de données, je vous recommande d'utiliser [Alembic](https://alembic.sqlalchemy.org/) qui est un outil léger et facile à utiliser que vous pouvez utiliser avec le SQLAlchemy Database Toolkit pour Python.

Maintenant, nous pouvons utiliser n'importe quelle requête [SQLAlchemy core](https://docs.sqlalchemy.org/en/latest/core/). Consultez quelques exemples ci-dessous.

```
# Exécution de plusieurs requêtes
query = books.insert()
values = [
    {"title": "No Highway", "author": "Nevil Shute"},
    {"title": "The Daffodil", "author": "SkyH. E. Bates"},
]
await app.db.execute_many(query, values)

# Récupération de plusieurs lignes
query = books.select()
rows = await app.db.fetch_all(query)

# Récupération d'une seule ligne
query = books.select()
row = await app.db.fetch_one(query)
```

### Routes

Maintenant, nous devons configurer les routes. Allons dans **routes.py** et ajoutons une nouvelle route pour les livres.

```
from sanic.response import json
```

```
from project.tables import books
```

```
def setup_routes(app):
    @app.route("/books")
    async def book_list(request):
        query = books.select()
        rows = await request.app.db.fetch_all(query)
        return json({
            'books': [{row['title']: row['author']} for row in rows]
        })
```

Bien sûr, nous devons appeler **setup_routes** dans **init** pour que cela fonctionne.

```
from project.routes import setup_routes
```

```
app = Sanic(__name__)
```

```
def init():
    ...
    app.config.from_object(Settings)
    setup_database()
    setup_routes(app)
    ...
```

_Requête…_

```
$ curl localhost:8000/books
{"books":[{"No Highway":"Nevil Shute"},{"The Daffodil":"SkyH. E. Bates"}]}
```

### Middlewares

Que diriez-vous de vérifier les en-têtes de **réponse** et de voir ce que nous pouvons ajouter ou corriger ?

```
$ curl -I localhost:8000
Connection: keep-alive
Keep-Alive: 5
Content-Length: 32
Content-Type: text/plain; charset=utf-8
```

Comme vous pouvez le voir, nous avons besoin de quelques améliorations de sécurité. Il manque certains en-têtes comme **X-XSS-Protection, Strict-Transport-Security**… alors prenons soin d'eux en utilisant une combinaison de [middlewares](https://sanic.readthedocs.io/en/latest/sanic/middleware.html#middleware) et de packages **secure**.

**Fichier _middlewares.py_.**

```
from secure import SecureHeaders

secure_headers = SecureHeaders()

def setup_middlewares(app):
    @app.middleware('response')
    async def set_secure_headers(request, response):
        secure_headers.sanic(response)
```

_Configuration des middlewares dans le fichier **main.py**._

```
from project.middlewares import setup_middlewares
```

```
app = Sanic(__name__)
```

```
def init():
    ...
    app.config.from_object(Settings)
    setup_database()
    setup_routes(app)
    setup_middlewares(app)
    ...
```

_Le résultat est :_

```
$ curl -I localhost:8000/books
Connection: keep-alive
Keep-Alive: 5
Strict-Transport-Security: max-age=63072000; includeSubdomains
X-Frame-Options: SAMEORIGIN
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
Referrer-Policy: no-referrer, strict-origin-when-cross-origin
Pragma: no-cache
Expires: 0
Cache-control: no-cache, no-store, must-revalidate, max-age=0
Content-Length: 32
Content-Type: text/plain; charset=utf-8
```

Comme je l'ai promis au début, il y a un [dépôt github](https://github.com/davitovmasyan/sanic-project) pour chaque [section](https://github.com/davitovmasyan/sanic-project/tags) dans cet article. J'espère que ce petit tutoriel vous a aidé à commencer avec Sanic. Il reste encore de nombreuses fonctionnalités inexplorées dans le framework Sanic que vous pouvez trouver et consulter dans la [documentation](https://sanic.readthedocs.io/en/latest/).

[**davitovmasyan/sanic-project**](https://github.com/davitovmasyan/sanic-project)
[_Aller vite et asynchrone avec Python et Sanic ! - davitovmasyan/sanic-project_github.com](https://github.com/davitovmasyan/sanic-project)

Si vous avez des réflexions à ce sujet, n'hésitez pas à laisser un commentaire.

Si vous avez trouvé cet article utile, donnez-moi quelques applaudissements ?

Merci d'avoir lu. Allez vite avec Sanic et bonne chance !!!