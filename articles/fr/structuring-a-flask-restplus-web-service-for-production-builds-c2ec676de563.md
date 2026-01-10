---
title: Comment structurer un service web Flask-RESTPlus pour les builds de production
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-15T03:01:52.000Z'
originalURL: https://freecodecamp.org/news/structuring-a-flask-restplus-web-service-for-production-builds-c2ec676de563
coverImage: https://cdn-media-1.freecodecamp.org/images/1*TSbCf17bFXOYAb-l0HJ7rQ.jpeg
tags:
- name: Python
  slug: python
- name: software
  slug: software
- name: software development
  slug: software-development
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Comment structurer un service web Flask-RESTPlus pour les builds de production
seo_desc: 'By Greg Obinna

  In this guide I’ll show you a step by step approach for structuring a Flask RESTPlus
  web application for testing, development and production environments. I will be
  using a Linux based OS (Ubuntu), but most of the steps can be replicat...'
---

Par Greg Obinna

Dans ce guide, je vais vous montrer une approche étape par étape pour structurer une application web Flask RESTPlus pour les environnements de test, de développement et de production. J'utiliserai un système d'exploitation basé sur Linux (Ubuntu), mais la plupart des étapes peuvent être reproduites sur Windows et Mac.

Avant de continuer avec ce guide, vous devriez avoir une compréhension de base du langage de programmation Python et du micro framework Flask. Si vous n'êtes pas familier avec ceux-ci, je recommande de consulter un article d'introduction - [Comment utiliser Python et Flask pour construire une application web.](https://medium.freecodecamp.org/how-to-use-python-and-flask-to-build-a-web-app-an-in-depth-tutorial-437dbfe9f1c6)

#### Comment ce guide est structuré

Ce guide est divisé en les parties suivantes :

* [Fonctionnalités](https://www.freecodecamp.org/news/structuring-a-flask-restplus-web-service-for-production-builds-c2ec676de563/#features)
* [Qu'est-ce que Flask-RESTPlus ?](https://www.freecodecamp.org/news/structuring-a-flask-restplus-web-service-for-production-builds-c2ec676de563/#what-is-flask-restplus)
* [Installation](https://www.freecodecamp.org/news/structuring-a-flask-restplus-web-service-for-production-builds-c2ec676de563/#setup-and-installation)
* [Configuration du projet et organisation](https://www.freecodecamp.org/news/structuring-a-flask-restplus-web-service-for-production-builds-c2ec676de563/#project-setup-and-organization)
* [Paramètres de configuration](https://www.freecodecamp.org/news/structuring-a-flask-restplus-web-service-for-production-builds-c2ec676de563/#configuration-settings)
* [Script Flask](https://www.freecodecamp.org/news/structuring-a-flask-restplus-web-service-for-production-builds-c2ec676de563/#flask-script)
* [Modèles de base de données et migration](https://www.freecodecamp.org/news/structuring-a-flask-restplus-web-service-for-production-builds-c2ec676de563/#database-models-and-migration)
* [Tests](https://www.freecodecamp.org/news/structuring-a-flask-restplus-web-service-for-production-builds-c2ec676de563/#testing)
* [Configuration](https://www.freecodecamp.org/news/structuring-a-flask-restplus-web-service-for-production-builds-c2ec676de563/#configuration)
* [Opérations utilisateur](https://www.freecodecamp.org/news/structuring-a-flask-restplus-web-service-for-production-builds-c2ec676de563/#user-operations)
* [Sécurité et authentification](https://www.freecodecamp.org/news/structuring-a-flask-restplus-web-service-for-production-builds-c2ec676de563/#security-and-authentication)
* [Protection des routes et autorisation](https://www.freecodecamp.org/news/structuring-a-flask-restplus-web-service-for-production-builds-c2ec676de563/#route-protection-and-authorization)
* [Conseils supplémentaires](https://www.freecodecamp.org/news/structuring-a-flask-restplus-web-service-for-production-builds-c2ec676de563/#extra-tips)
* [Étendre l'application & Conclusion](https://www.freecodecamp.org/news/structuring-a-flask-restplus-web-service-for-production-builds-c2ec676de563/#extending-the-app-conclusion)

#### Fonctionnalités

Nous utiliserons les fonctionnalités et extensions suivantes dans notre projet.

* [Flask-Bcrypt](https://flask-bcrypt.readthedocs.io/) : Une _extension Flask qui fournit des utilitaires de hachage bcrypt pour votre application_.
* [Flask-Migrate](https://flask-migrate.readthedocs.io/) : _Une extension qui gère les migrations de base de données SQLAlchemy pour les applications Flask en utilisant Alembic. Les opérations de base de données sont disponibles via l'interface de ligne de commande Flask ou via l'extension Flask-Script._
* [Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org/) : _Une extension pour [Flask](http://flask.pocoo.org/) qui ajoute le support pour [SQLAlchemy](http://www.sqlalchemy.org/) à votre application._
* [PyJWT](https://pyjwt.readthedocs.io/) : _Une bibliothèque Python qui vous permet d'encoder et de décoder des JSON Web Tokens (JWT). JWT est un standard ouvert et industriel ([RFC 7519](https://tools.ietf.org/html/rfc7519)) pour représenter des revendications de manière sécurisée entre deux parties._
* [Flask-Script](https://flask-script.readthedocs.io/) : _Une extension qui fournit un support pour écrire des scripts externes dans Flask et d'autres tâches en ligne de commande qui appartiennent en dehors de l'application web elle-même._
* [Namespaces](http://flask-restplus.readthedocs.io/en/stable/scaling.html) ([Blueprints](http://exploreflask.com/en/latest/blueprints.html))
* [Flask-restplus](https://flask-restplus.readthedocs.io/)
* UnitTest

#### Qu'est-ce que Flask-RESTPlus ?

Flask-RESTPlus est une extension pour Flask qui ajoute un support pour construire rapidement des API REST. Flask-RESTPlus encourage les meilleures pratiques avec une configuration minimale. Il fournit une collection cohérente de décorateurs et d'outils pour décrire votre API et exposer sa documentation correctement (en utilisant Swagger).

#### Installation

Vérifiez si vous avez pip installé en tapant la commande `pip --version` dans le terminal, puis appuyez sur Entrée.

```bash
pip --version
```

Si le terminal répond avec le numéro de version, cela signifie que pip est installé, passez donc à l'étape suivante, sinon [installez pip](https://pip.pypa.io/en/latest/installing/) ou utilisez le gestionnaire de paquets Linux, exécutez la commande ci-dessous dans le terminal et appuyez sur Entrée. Choisissez soit la version Python 2.x OU 3.x.

* Python 2.x

```bash
sudo apt-get install python-pip
```

* Python 3.x

```bash
sudo apt-get install python3-pip
```

Configurez l'environnement virtuel et l'enveloppe de l'environnement virtuel (vous n'avez besoin que d'un seul de ceux-ci, selon la version installée ci-dessus) :

```bash
sudo pip install virtualenv

sudo pip3 install virtualenvwrapper
```

Suivez [ce lien](https://medium.com/@gitudaniel/installing-virtualenvwrapper-for-python3-ad3dfea7c717) pour une configuration complète de l'enveloppe de l'environnement virtuel.

Créez un nouvel environnement et activez-le en exécutant la commande suivante dans le terminal :

```bash
mkproject nom_de_votre_projet
```

#### Configuration du projet et organisation

Je vais utiliser une [structure fonctionnelle](http://exploreflask.com/en/latest/blueprints.html#functional-structure) pour organiser les fichiers du projet par ce qu'ils font. Dans une structure fonctionnelle, les templates sont regroupés dans un seul répertoire, les fichiers statiques dans un autre et les vues dans un troisième.

Dans le répertoire du projet, créez un nouveau package appelé `app`. À l'intérieur de `app`, créez deux packages `main` et `test`. Votre structure de répertoire devrait ressembler à celle ci-dessous.

```
.
├── app
│   ├── __init__.py
│   ├── main
│   │   └── __init__.py
│   └── test
│       └── __init__.py
└── requirements.txt
```

Nous allons utiliser une structure fonctionnelle pour modulariser notre application. À l'intérieur du package `main`, créez trois autres packages nommés : `controller`, `service` et `model`. Le package `model` contiendra tous nos modèles de base de données tandis que le package `service` contiendra toute la logique métier de notre application et enfin le package `controller` contiendra tous nos points de terminaison d'application. La structure de l'arborescence devrait maintenant ressembler à ce qui suit :

```
.
├── app
│   ├── __init__.py
│   ├── main
│   │   ├── controller
│   │   │   └── __init__.py
│   │   ├── __init__.py
│   │   ├── model
│   │   │   └── __init__.py
│   │   └── service
│   │       └── __init__.py
│   └── test
│       └── __init__.py
└── requirements.txt
```

Maintenant, installons les packages requis. Assurez-vous que l'environnement virtuel que vous avez créé est activé et exécutez les commandes suivantes dans le terminal :

```bash
pip install flask-bcrypt

pip install flask-restplus

pip install Flask-Migrate

pip install pyjwt

pip install Flask-Script

pip install flask_testing
```

Créez ou mettez à jour le fichier `requirements.txt` en exécutant la commande :

```bash
pip freeze > requirements.txt
```

Le fichier `requirements.txt` généré devrait ressembler à celui ci-dessous :

```
alembic==0.9.8
aniso8601==3.0.0
bcrypt==3.1.4
cffi==1.11.5
click==6.7
Flask==0.12.2
Flask-Bcrypt==0.7.1
Flask-Migrate==2.1.1
flask-restplus==0.10.1
Flask-Script==2.0.6
Flask-SQLAlchemy==2.3.2
Flask-Testing==0.7.1
itsdangerous==0.24
Jinja2==2.10
jsonschema==2.6.0
Mako==1.0.7
MarkupSafe==1.0
pycparser==2.18
PyJWT==1.6.0
python-dateutil==2.7.0
python-editor==1.0.3
pytz==2018.3
six==1.11.0
SQLAlchemy==1.2.5
Werkzeug==0.14.1
```

#### Paramètres de configuration

Dans le package `main`, créez un fichier appelé `config.py` avec le contenu suivant :

```py
import os

# décommentez la ligne ci-dessous pour l'URL de la base de données postgres à partir de la variable d'environnement
# postgres_local_base = os.environ['DATABASE_URL']

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')
    DEBUG = False


class DevelopmentConfig(Config):
    # décommentez la ligne ci-dessous pour utiliser postgres
    # SQLALCHEMY_DATABASE_URI = postgres_local_base
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'flask_boilerplate_main.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'flask_boilerplate_test.db')
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False
    # décommentez la ligne ci-dessous pour utiliser postgres
    # SQLALCHEMY_DATABASE_URI = postgres_local_base


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY
```

Le fichier de configuration contient trois classes de configuration d'environnement qui incluent `testing`, `development` et `production`.

Nous allons utiliser le [modèle de fabrique d'applications](http://flask.pocoo.org/docs/0.12/patterns/appfactories/) pour créer notre objet Flask. Ce modèle est le plus utile pour créer plusieurs instances de notre application avec différents paramètres. Cela facilite le passage entre nos environnements de test, de développement et de production en appelant la fonction `create_app` avec le paramètre requis.

Dans le fichier `__init__.py` à l'intérieur du package `main`, entrez les lignes de code suivantes :

```py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

from .config import config_by_name

db = SQLAlchemy()
flask_bcrypt = Bcrypt()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)
    flask_bcrypt.init_app(app)

    return app
```

#### Script Flask

Maintenant, créons notre point d'entrée d'application. Dans le répertoire racine du projet, créez un fichier appelé `manage.py` avec le contenu suivant :

```py
import os
import unittest

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app.main import create_app, db

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')

app.app_context().push()

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

@manager.command
def run():
    app.run()

@manager.command
def test():
    """Exécute les tests unitaires."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

if __name__ == '__main__':
    manager.run()
```

Le code ci-dessus dans `manage.py` fait ce qui suit :

* `ligne 4` et `5` importent les modules migrate et manager respectivement (nous utiliserons bientôt la commande migrate).
* `ligne 9` appelle la fonction `create_app` que nous avons créée initialement pour créer l'instance d'application avec le paramètre requis à partir de la variable d'environnement qui peut être l'une des suivantes - `dev`, `prod`, `test`. Si aucune n'est définie dans la variable d'environnement, le `dev` par défaut est utilisé.
* `ligne 13` et `15` instancient les classes manager et migrate en passant l'instance `app` à leurs constructeurs respectifs.
* Dans `ligne 17`, nous passons les instances `db` et `MigrateCommand` à l'interface `add_command` du `manager` pour exposer toutes les commandes de migration de base de données via Flask-Script.
* `ligne 20` et `25` marquent les deux fonctions comme exécutables à partir de la ligne de commande.

> _Flask-Migrate expose deux classes, `Migrate` et `MigrateCommand`. La classe `Migrate` contient toutes les fonctionnalités de l'extension. La classe `MigrateCommand` n'est utilisée que lorsqu'il est souhaité d'exposer les commandes de migration de base de données via l'extension Flask-Script._

À ce stade, nous pouvons tester l'application en exécutant la commande ci-dessous dans le répertoire racine du projet.

```bash
python manage.py run
```

Si tout est correct, vous devriez voir quelque chose comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*5_9GQCi5Z7J13iUbp82bHw.png)

#### Modèles de base de données et migration

Maintenant, créons nos modèles. Nous utiliserons l'instance `db` de sqlalchemy pour créer nos modèles.

L'instance `db` contient toutes les fonctions et aides de `**sqlalchemy**` et `[**sqlalchemy.orm**](http://docs.sqlalchemy.org/en/latest/orm/scalar_mapping.html#module-sqlalchemy.orm)` et elle fournit une classe appelée `Model` qui est une base déclarative pouvant être utilisée pour déclarer des modèles.

Dans le package `model`, créez un fichier appelé `user.py` avec le contenu suivant :

```py
from .. import db, flask_bcrypt

class User(db.Model):
    """ Modèle d'utilisateur pour stocker les détails liés à l'utilisateur """
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)
    public_id = db.Column(db.String(100), unique=True)
    username = db.Column(db.String(50), unique=True)
    password_hash = db.Column(db.String(100))

    @property
    def password(self):
        raise AttributeError('password: champ en écriture seule')

    @password.setter
    def password(self, password):
        self.password_hash = flask_bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return flask_bcrypt.check_password_hash(self.password_hash, password)

    def __repr__(self):
        return "<User '{}'>".format(self.username)
```

Le code ci-dessus dans `user.py` fait ce qui suit :

* `ligne 3` : La classe `user` hérite de la classe `db.Model` qui déclare la classe comme un modèle pour sqlalchemy.
* `ligne 7` à `13` crée les colonnes requises pour la table utilisateur.
* `ligne 21` est un setter pour le champ `password_hash` et il utilise `flask-bcrypt` pour générer un hachage en utilisant le mot de passe fourni.
* `ligne 24` compare un mot de passe donné avec le `password_hash` déjà enregistré.

Maintenant, pour générer la table de base de données à partir du modèle `user` que nous venons de créer, nous utiliserons `migrateCommand` via l'interface `manager`. Pour que `manager` détecte nos modèles, nous devrons importer le modèle `user` en ajoutant le code ci-dessous au fichier `manage.py` :

```bash
...
from app.main.model import user
...
```

Maintenant, nous pouvons procéder à la **migration** en exécutant les commandes suivantes dans le répertoire racine du projet :

1. Initialisez un dossier de migration en utilisant la commande `init` pour qu'Alembic effectue les migrations.

```bash
python manage.py db init
```

2. Créez un script de migration à partir des changements détectés dans le modèle en utilisant la commande `migrate`. Cela n'affecte pas encore la base de données.

```bash
python manage.py db migrate --message 'initial database migration'
```

3. Appliquez le script de migration à la base de données en utilisant la commande `upgrade`

```bash
python manage.py db upgrade
```

Si tout se passe bien, vous devriez avoir une nouvelle base de données sqlLite `flask_boilerplate_main.db` générée à l'intérieur du package principal.

> Chaque fois que le modèle de base de données change, répétez les commandes `migrate` et `upgrade`

### Tests

#### Configuration

Pour être sûr que la configuration de notre environnement est correcte, écrivons quelques tests pour cela.

Créez un fichier appelé `test_config.py` dans le package de test avec le contenu suivant :

```py
import os
import unittest

from flask import current_app
from flask_testing import TestCase

from manage import app
from app.main.config import basedir


class TestDevelopmentConfig(TestCase):
    def create_app(self):
        app.config.from_object('app.main.config.DevelopmentConfig')
        return app

    def test_app_is_development(self):
        self.assertFalse(app.config['SECRET_KEY'] is 'my_precious')
        self.assertTrue(app.config['DEBUG'] is True)
        self.assertFalse(current_app is None)
        self.assertTrue(
            app.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:///' + os.path.join(basedir, 'flask_boilerplate_main.db')
        )


class TestTestingConfig(TestCase):
    def create_app(self):
        app.config.from_object('app.main.config.TestingConfig')
        return app

    def test_app_is_testing(self):
        self.assertFalse(app.config['SECRET_KEY'] is 'my_precious')
        self.assertTrue(app.config['DEBUG'])
        self.assertTrue(
            app.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:///' + os.path.join(basedir, 'flask_boilerplate_test.db')
        )


class TestProductionConfig(TestCase):
    def create_app(self):
        app.config.from_object('app.main.config.ProductionConfig')
        return app

    def test_app_is_production(self):
        self.assertTrue(app.config['DEBUG'] is False)


if __name__ == '__main__':
    unittest.main()
```

Exécutez le test en utilisant la commande suivante :

```bash
python manage.py test
```

Vous devriez obtenir le résultat suivant :

![Image](https://cdn-media-1.freecodecamp.org/images/1*6_E40FN6IFz5EtwL1JqQTw.png)

#### Opérations utilisateur

Maintenant, travaillons sur les opérations suivantes liées à l'utilisateur :

* créer un nouvel utilisateur
* obtenir un utilisateur enregistré avec son `public_id`
* obtenir tous les utilisateurs enregistrés.

**Classe de service utilisateur :** Cette classe gère toute la logique relative au modèle utilisateur. Dans le package `service`, créez un nouveau fichier `user_service.py` avec le contenu suivant :

```py
import uuid
import datetime

from app.main import db
from app.main.model.user import User


def save_new_user(data):
    user = User.query.filter_by(email=data['email']).first()
    if not user:
        new_user = User(
            public_id=str(uuid.uuid4()),
            email=data['email'],
            username=data['username'],
            password=data['password'],
            registered_on=datetime.datetime.utcnow()
        )
        save_changes(new_user)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409


def get_all_users():
    return User.query.all()


def get_a_user(public_id):
    return User.query.filter_by(public_id=public_id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()

```

Le code ci-dessus dans `user_service.py` fait ce qui suit :

* `ligne 8` à `29` crée un nouvel utilisateur en vérifiant d'abord si l'utilisateur existe déjà ; il retourne un `response_object` de succès si l'utilisateur n'existe pas, sinon il retourne un code d'erreur `409` et un `response_object` d'échec.
* `ligne 33` et `37` retournent une liste de tous les utilisateurs enregistrés et un objet utilisateur en fournissant le `public_id` respectivement.
* `ligne 40` à `42` valide les changements dans la base de données.

> Pas besoin d'utiliser [jsonify](http://flask.pocoo.org/docs/0.12/api/#module-flask.json) pour formater un objet en JSON, Flask-restplus le fait automatiquement

Dans le package `main`, créez un nouveau package appelé `util`. Ce package contiendra toutes les utilités nécessaires dont nous pourrions avoir besoin dans notre application.

Dans le package `util`, créez un nouveau fichier `dto.py`. Comme son nom l'indique, l'objet de transfert de données ([DTO](https://en.wikipedia.org/wiki/Data_transfer_object)) sera responsable du transport des données entre les processus. Dans notre cas, il sera utilisé pour marshaler les données pour nos appels d'API. Nous comprendrons mieux cela au fur et à mesure.

```py
from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'public_id': fields.String(description='user Identifier')
    })
```

Le code ci-dessus dans `dto.py` fait ce qui suit :

* `ligne 5` crée un nouvel espace de noms pour les opérations liées à l'utilisateur. Flask-RESTPlus fournit un moyen d'utiliser presque le même modèle que [Blueprint](http://exploreflask.com/en/latest/blueprints.html#what-is-a-blueprint). L'idée principale est de diviser votre application en espaces de noms réutilisables. Un module d'espace de noms contiendra des déclarations de modèles et de ressources.
* `ligne 6` crée un nouvel utilisateur dto via l'interface `model` fournie par l'espace de noms `api` à la `ligne 5`.

**Contrôleur utilisateur :** La classe de contrôleur utilisateur gère toutes les requêtes HTTP entrantes relatives à l'utilisateur.

Sous le package `controller`, créez un nouveau fichier appelé `user_controller.py` avec le contenu suivant :

```py
from flask import request
from flask_restplus import Resource

from ..util.dto import UserDto
from ..service.user_service import save_new_user, get_all_users, get_a_user

api = UserDto.api
_user = UserDto.user


@api.route('/')
class UserList(Resource):
    @api.doc('list_of_registered_users')
    @api.marshal_list_with(_user, envelope='data')
    def get(self):
        """Liste tous les utilisateurs enregistrés"""
        return get_all_users()

    @api.response(201, 'User successfully created.')
    @api.doc('create a new user')
    @api.expect(_user, validate=True)
    def post(self):
        """Crée un nouvel utilisateur"""
        data = request.json
        return save_new_user(data=data)


@api.route('/<public_id>')
@api.param('public_id', 'The User identifier')
@api.response(404, 'User not found.')
class User(Resource):
    @api.doc('get a user')
    @api.marshal_with(_user)
    def get(self, public_id):
        """obtenir un utilisateur donné son identifiant"""
        user = get_a_user(public_id)
        if not user:
            api.abort(404)
        else:
            return user
```

`ligne 1` à `8` importe toutes les ressources requises pour le contrôleur utilisateur. Nous avons défini deux classes concrètes dans notre contrôleur utilisateur qui sont `userList` et `user`. Ces deux classes étendent la ressource abstraite flask-restplus.

> _Les ressources concrètes doivent étendre cette classe et exposer des méthodes pour chaque méthode HTTP prise en charge. Si une ressource est invoquée avec une méthode HTTP non prise en charge, l'API retournera une réponse avec le statut 405 Méthode non autorisée. Sinon, la méthode appropriée est appelée et tous les arguments de la règle d'URL utilisée lors de l'ajout de la ressource à une instance d'API lui sont passés._

L'espace de noms `api` à la `ligne 7` ci-dessus fournit au contrôleur plusieurs décorateurs qui incluent, sans s'y limiter, les suivants :

* api.**route** : _Un décorateur pour router les ressources_
* api.**marshal_with** : _Un décorateur spécifiant les champs à utiliser pour la sérialisation (C'est ici que nous utilisons le `_userDto` que nous avons créé précédemment)_
* api.**marshal_list_with** : _Un décorateur raccourci pour `_marshal_with` ci-dessus avec `_as_list = True`_
* api.**doc** : _Un décorateur pour ajouter une documentation d'API à l'objet décoré_
* api.**response** : _Un décorateur pour spécifier l'une des réponses attendues_
* api.**expect** : _Un décorateur pour spécifier le modèle d'entrée attendu (nous utilisons toujours le `_userDto` pour l'entrée attendue)_
* api.**param** : _Un décorateur pour spécifier l'un des paramètres attendus_

Nous avons maintenant défini notre espace de noms avec le contrôleur utilisateur. Il est maintenant temps de l'ajouter au point d'entrée de l'application.

Dans le fichier `__init__.py` du package `app`, entrez ce qui suit :

```py
# app/__init__.py

from flask_restplus import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FLASK RESTPLUS API BOILER-PLATE WITH JWT',
          version='1.0',
          description='a boilerplate for flask restplus web service'
          )

api.add_namespace(user_ns, path='/user')
```

Le code ci-dessus dans `blueprint.py` fait ce qui suit :

* Dans `ligne 8`, nous créons une instance de blueprint en passant `name` et `import_name`. `API` est le point d'entrée principal pour les ressources de l'application et doit donc être initialisé avec le `blueprint` dans `ligne 10`.
* Dans `ligne 16`, nous ajoutons l'espace de noms utilisateur `user_ns` à la liste des espaces de noms dans l'instance `API`.

Nous avons maintenant défini notre blueprint. Il est temps de l'enregistrer sur notre application Flask. Mettez à jour `manage.py` en important `blueprint` et en l'enregistrant avec l'instance d'application Flask.

```py
from app import blueprint
...

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
app.register_blueprint(blueprint)

app.app_context().push()

...
```

Nous pouvons maintenant tester notre application pour voir que tout fonctionne bien.

```bash
python manage.py run
```

Ouvrez maintenant l'URL `[http://127.0.0.1:5000](http://127.0.0.1:5000)` dans votre navigateur. Vous devriez voir la documentation Swagger.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Us_S2WLR3AQAyfOvkzZ38Q.png)

Testons le point de terminaison **créer un nouvel utilisateur** en utilisant la fonctionnalité de test Swagger.

![Image](https://cdn-media-1.freecodecamp.org/images/1*x3oZjCsUXVHjP4_YgndmFA.png)

Vous devriez obtenir la réponse suivante

![Image](https://cdn-media-1.freecodecamp.org/images/1*ITTWVn8rJbIG-muhQCXsWg.png)

#### Sécurité et authentification

Créons un modèle `blacklistToken` pour stocker les jetons blacklistés. Dans le package `models`, créez un fichier `blacklist.py` avec le contenu suivant :

```py
from .. import db
import datetime


class BlacklistToken(db.Model):
    """
    Modèle de jeton pour stocker les jetons JWT
    """
    __tablename__ = 'blacklist_tokens'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    token = db.Column(db.String(500), unique=True, nullable=False)
    blacklisted_on = db.Column(db.DateTime, nullable=False)

    def __init__(self, token):
        self.token = token
        self.blacklisted_on = datetime.datetime.now()

    def __repr__(self):
        return '<id: token: {}'.format(self.token)

    @staticmethod
    def check_blacklist(auth_token):
        # vérifier si le jeton d'authentification a été blacklisté
        res = BlacklistToken.query.filter_by(token=str(auth_token)).first()
        if res:
            return True
        else:
            return False
```

N'oublions pas de migrer les changements pour qu'ils prennent effet sur notre base de données. Importez la classe `blacklist` dans `manage.py`.

```py
from app.main.model import blacklist
```

Exécutez les commandes `migrate` et `upgrade`

```bash
python manage.py db migrate --message 'add blacklist table'

python manage.py db upgrade
```

Ensuite, créez `blacklist_service.py` dans le package de service avec le contenu suivant pour blacklister un jeton :

```py
from app.main import db
from app.main.model.blacklist import BlacklistToken


def save_token(token):
    blacklist_token = BlacklistToken(token=token)
    try:
        # insérer le jeton
        db.session.add(blacklist_token)
        db.session.commit()
        response_object = {
            'status': 'success',
            'message': 'Successfully logged out.'
        }
        return response_object, 200
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': e
        }
        return response_object, 200
```

Mettez à jour le modèle `user` avec deux méthodes statiques pour encoder et décoder les jetons. Ajoutez les importations suivantes :

```py
import datetime
import jwt
from app.main.model.blacklist import BlacklistToken
from ..config import key
```

* Encodage

```py
def encode_auth_token(self, user_id):
        """
        Génère le jeton d'authentification
        :return: string
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1, seconds=5),
                'iat': datetime.datetime.utcnow(),
                'sub': user_id
            }
            return jwt.encode(
                payload,
                key,
                algorithm='HS256'
            )
        except Exception as e:
            return e
```

* Décodage : Le jeton blacklisté, le jeton expiré et le jeton invalide sont pris en compte lors du décodage du jeton d'authentification.

```py
  @staticmethod  
  def decode_auth_token(auth_token):
        """
        Décode le jeton d'authentification
        :param auth_token:
        :return: integer|string
        """
        try:
            payload = jwt.decode(auth_token, key)
            is_blacklisted_token = BlacklistToken.check_blacklist(auth_token)
            if is_blacklisted_token:
                return 'Token blacklisted. Please log in again.'
            else:
                return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'
```

Maintenant, écrivons un test pour le modèle `user` pour nous assurer que nos fonctions `encode` et `decode` fonctionnent correctement.

Dans le package `test`, créez un fichier `base.py` avec le contenu suivant :

```py
from flask_testing import TestCase
from app.main import db
from manage import app


class BaseTestCase(TestCase):
    """ Tests de base """

    def create_app(self):
        app.config.from_object('app.main.config.TestingConfig')
        return app

    def setUp(self):
        db.create_all()
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
```

Le `BaseTestCase` configure notre environnement de test prêt avant et après chaque cas de test qui l'étend.

Créez `test_user_medol.py` avec les cas de test suivants :

```py
import unittest
import datetime

from app.main import db
from app.main.model.user import User
from app.test.base import BaseTestCase


class TestUserModel(BaseTestCase):

    def test_encode_auth_token(self):
        user = User(
            email='test@test.com',
            password='test',
            registered_on=datetime.datetime.utcnow()
        )
        db.session.add(user)
        db.session.commit()
        auth_token = user.encode_auth_token(user.id)
        self.assertTrue(isinstance(auth_token, bytes))

    def test_decode_auth_token(self):
        user = User(
            email='test@test.com',
            password='test',
            registered_on=datetime.datetime.utcnow()
        )
        db.session.add(user)
        db.session.commit()
        auth_token = user.encode_auth_token(user.id)
        self.assertTrue(isinstance(auth_token, bytes))
        self.assertTrue(User.decode_auth_token(auth_token.decode("utf-8") ) == 1)


if __name__ == '__main__':
    unittest.main()

```

Exécutez le test avec `python manage.py test`. Tous les tests devraient réussir.

Créons les **points de terminaison d'authentification** pour **login** et **logout**.

* Tout d'abord, nous avons besoin d'un `dto` pour la charge utile de connexion. Nous utiliserons le dto d'authentification pour l'annotation `@expect` dans le point de terminaison `login`. Ajoutez le code ci-dessous à `dto.py`

```py
class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })
```

* Ensuite, nous créons une classe d'assistance d'authentification pour gérer toutes les opérations liées à l'authentification. Ce fichier `auth_helper.py` sera dans le package de service et contiendra deux méthodes statiques qui sont `login_user` et `logout_user`

> _Lorsqu'un utilisateur se déconnecte, le jeton de l'utilisateur est blacklisté, c'est-à-dire que l'utilisateur ne peut pas se reconnecter avec ce même jeton._

```py
from app.main.model.user import User
from ..service.blacklist_service import save_token


class Auth:

    @staticmethod
    def login_user(data):
        try:
            # récupérer les données de l'utilisateur
            user = User.query.filter_by(email=data.get('email')).first()
            if user and user.check_password(data.get('password')):
                auth_token = user.encode_auth_token(user.id)
                if auth_token:
                    response_object = {
                        'status': 'success',
                        'message': 'Successfully logged in.',
                        'Authorization': auth_token.decode()
                    }
                    return response_object, 200
            else:
                response_object = {
                    'status': 'fail',
                    'message': 'email or password does not match.'
                }
                return response_object, 401

        except Exception as e:
            print(e)
            response_object = {
                'status': 'fail',
                'message': 'Try again'
            }
            return response_object, 500

    @staticmethod
    def logout_user(data):
        if data:
            auth_token = data.split(" ")[1]
        else:
            auth_token = ''
        if auth_token:
            resp = User.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                # marquer le jeton comme blacklisté
                return save_token(token=auth_token)
            else:
                response_object = {
                    'status': 'fail',
                    'message': resp
                }
                return response_object, 401
        else:
            response_object = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return response_object, 403
```

* Créons maintenant des points de terminaison pour les opérations de `login` et `logout`. Dans le package de contrôleur, créez `auth_controller.py` avec le contenu suivant :

```py
from flask import request
from flask_restplus import Resource

from app.main.service.auth_helper import Auth
from ..util.dto import AuthDto

api = AuthDto.api
user_auth = AuthDto.user_auth


@api.route('/login')
class UserLogin(Resource):
    """
        Ressource de connexion utilisateur
    """
    @api.doc('user login')
    @api.expect(user_auth, validate=True)
    def post(self):
        # obtenir les données de la requête
        post_data = request.json
        return Auth.login_user(data=post_data)


@api.route('/logout')
class LogoutAPI(Resource):
    """
    Ressource de déconnexion
    """
    @api.doc('logout a user')
    def post(self):
        # obtenir le jeton d'authentification
        auth_header = request.headers.get('Authorization')
        return Auth.logout_user(data=auth_header)
```

* À ce stade, la seule chose restante est d'enregistrer l'espace de noms `api` d'authentification avec le `Blueprint` de l'application

Mettez à jour le fichier `__init__.py` du package `app` avec ce qui suit

```py
# app/__init__.py

from flask_restplus import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FLASK RESTPLUS API BOILER-PLATE WITH JWT',
          version='1.0',
          description='a boilerplate for flask restplus web service'
          )

api.add_namespace(user_ns, path='/user')
api.add_namespace(auth_ns)
```

Exécutez l'application avec `python manage.py run` et ouvrez l'URL `[http://127.0.0.1:5000](http://127.0.0.1:5000)` dans votre navigateur.

La documentation Swagger devrait maintenant refléter le nouvel espace de noms `auth` avec les points de terminaison `login` et `logout`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*K4ZVMOwsOIIzBOV8bfqJew.png)

Avant d'écrire quelques tests pour nous assurer que notre authentification fonctionne comme prévu, modifions notre point de terminaison d'inscription pour connecter automatiquement un utilisateur une fois l'inscription réussie.

Ajoutez la méthode `generate_token` ci-dessous à `user_service.py` :

```py
def generate_token(user):
    try:
        # générer le jeton d'authentification
        auth_token = user.encode_auth_token(user.id)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.',
            'Authorization': auth_token.decode()
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401
```

La méthode `generate_token` génère un **jeton** d'authentification en encodant l'`id` de l'utilisateur. Ce **jeton** est retourné en tant que réponse.

Ensuite, remplacez le bloc **return** dans la méthode `save_new_user` ci-dessous

```py
response_object = {
    'status': 'success',
    'message': 'Successfully registered.'
}
return response_object, 201
```

par

```py
return generate_token(new_user)
```

Il est maintenant temps de tester les fonctionnalités de `login` et `logout`. Créez un nouveau fichier de test `test_auth.py` dans le package de test avec le contenu suivant :

```py
import unittest
import json
from app.test.base import BaseTestCase


def register_user(self):
    return self.client.post(
        '/user/',
        data=json.dumps(dict(
            email='example@gmail.com',
            username='username',
            password='123456'
        )),
        content_type='application/json'
    )


def login_user(self):
    return self.client.post(
        '/auth/login',
        data=json.dumps(dict(
            email='example@gmail.com',
            password='123456'
        )),
        content_type='application/json'
    )


class TestAuthBlueprint(BaseTestCase):

    def test_registered_user_login(self):
            """ Test pour la connexion d'un utilisateur enregistré """
            with self.client:
                # inscription de l'utilisateur
                user_response = register_user(self)
                response_data = json.loads(user_response.data.decode())
                self.assertTrue(response_data['Authorization'])
                self.assertEqual(user_response.status_code, 201)

                # connexion de l'utilisateur enregistré
                login_response = login_user(self)
                data = json.loads(login_response.data.decode())
                self.assertTrue(data['Authorization'])
                self.assertEqual(login_response.status_code, 200)

    def test_valid_logout(self):
        """ Test pour la déconnexion avant l'expiration du jeton """
        with self.client:
            # inscription de l'utilisateur
            user_response = register_user(self)
            response_data = json.loads(user_response.data.decode())
            self.assertTrue(response_data['Authorization'])
            self.assertEqual(user_response.status_code, 201)

            # connexion de l'utilisateur enregistré
            login_response = login_user(self)
            data = json.loads(login_response.data.decode())
            self.assertTrue(data['Authorization'])
            self.assertEqual(login_response.status_code, 200)

            # déconnexion avec un jeton valide
            response = self.client.post(
                '/auth/logout',
                headers=dict(
                    Authorization='Bearer ' + json.loads(
                        login_response.data.decode()
                    )['Authorization']
                )
            )
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'success')
            self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
```

Visitez le [dépôt github](https://github.com/cosmic-byte/flask-restplus-boilerplate) pour des cas de test plus exhaustifs.

#### Protection des routes et autorisation

Jusqu'à présent, nous avons créé avec succès nos points de terminaison, implémenté les fonctionnalités de connexion et de déconnexion, mais nos points de terminaison restent non protégés.

Nous avons besoin d'un moyen de définir des règles qui déterminent quels points de terminaison sont ouverts ou nécessitent une authentification, voire un privilège d'administrateur.

Nous pouvons y parvenir en créant des décorateurs personnalisés pour nos points de terminaison.

Avant de pouvoir protéger ou autoriser l'un de nos points de terminaison, nous devons connaître l'utilisateur actuellement connecté. Nous pouvons le faire en extrayant le `jeton d'autorisation` de l'en-tête de la requête actuelle en utilisant la bibliothèque flask `request`. Nous décodons ensuite les détails de l'utilisateur à partir du `jeton d'autorisation`.

Dans la classe `Auth` du fichier `auth_helper.py`, ajoutez la méthode statique suivante :

```py
@staticmethod
def get_logged_in_user(new_request):
        # obtenir le jeton d'authentification
        auth_token = new_request.headers.get('Authorization')
        if auth_token:
            resp = User.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                user = User.query.filter_by(id=resp).first()
                response_object = {
                    'status': 'success',
                    'data': {
                        'user_id': user.id,
                        'email': user.email,
                        'admin': user.admin,
                        'registered_on': str(user.registered_on)
                    }
                }
                return response_object, 200
            response_object = {
                'status': 'fail',
                'message': resp
            }
            return response_object, 401
        else:
            response_object = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return response_object, 401
```

Maintenant que nous pouvons récupérer l'utilisateur connecté à partir de la requête, allons-y et créons les `décorateurs`.

Créez un fichier `decorator.py` dans le package `util` avec le contenu suivant :

```py
from functools import wraps
from flask import request

from app.main.service.auth_helper import Auth


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        data, status = Auth.get_logged_in_user(request)
        token = data.get('data')

        if not token:
            return data, status

        return f(*args, **kwargs)

    return decorated


def admin_token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        data, status = Auth.get_logged_in_user(request)
        token = data.get('data')

        if not token:
            return data, status

        admin = token.get('admin')
        if not admin:
            response_object = {
                'status': 'fail',
                'message': 'admin token required'
            }
            return response_object, 401

        return f(*args, **kwargs)

    return decorated
```

Pour plus d'informations sur les **décorateurs** et comment les créer, consultez [ce lien](https://realpython.com/primer-on-python-decorators/).

Maintenant que nous avons créé les décorateurs `token_required` et `admin_token_required` pour un jeton valide et pour un jeton d'administrateur respectivement, il ne reste plus qu'à annoter les points de terminaison que nous souhaitons protéger avec le **décorateur** approprié.

#### Conseils supplémentaires

Actuellement, pour effectuer certaines tâches dans notre application, nous devons exécuter différentes commandes pour démarrer l'application, exécuter des tests, installer des dépendances, etc. Nous pouvons automatiser ces processus en organisant toutes les commandes dans un seul fichier en utilisant `Makefile`.

Dans le répertoire racine de l'application, créez un `Makefile` sans extension de fichier. Le fichier doit contenir ce qui suit :

```
.PHONY: clean system-packages python-packages install tests run all

clean:
   find . -type f -name '*.pyc' -delete
   find . -type f -name '*.log' -delete

system-packages:
   sudo apt install python-pip -y

python-packages:
   pip install -r requirements.txt

install: system-packages python-packages

tests:
   python manage.py test

run:
   python manage.py run

all: clean install tests run
```

Voici les options du fichier make.

1. `make install` : installe à la fois les system-packages et les python-packages
2. `make clean` : nettoie l'application
3. `make tests` : exécute tous les tests
4. `make run` : démarre l'application
5. `make all` : effectue le `nettoyage`, l'`installation`, exécute les `tests` et `démarre` l'application.

### Étendre l'application & Conclusion

Il est assez facile de copier la structure actuelle de l'application et de l'étendre pour ajouter plus de fonctionnalités/points de terminaison à l'application. Il suffit de consulter l'une des routes précédentes qui ont été implémentées.

_N'hésitez pas à laisser un commentaire si vous avez des questions, des observations ou des recommandations. De plus, si cet article vous a été utile, cliquez sur l'icône d'applaudissements pour que d'autres puissent le voir ici et en bénéficier également._

Visitez le [dépôt github](https://github.com/cosmic-byte/flask-restplus-boilerplate) pour le projet complet.

Merci d'avoir lu et bonne chance !