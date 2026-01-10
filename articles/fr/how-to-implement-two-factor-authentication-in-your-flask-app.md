---
title: Comment implémenter l'authentification à deux facteurs avec PyOTP et Google
  Authenticator dans votre application Flask
subtitle: ''
author: Ashutosh Krishna
co_authors: []
series: null
date: '2023-11-27T21:41:12.000Z'
originalURL: https://freecodecamp.org/news/how-to-implement-two-factor-authentication-in-your-flask-app
coverImage: https://www.freecodecamp.org/news/content/images/2023/11/2fa-tutorial.png
tags:
- name: authentication
  slug: authentication
- name: Flask Framework
  slug: flask
- name: Python
  slug: python
- name: Two-factor authentication
  slug: two-factor-authentication
seo_title: Comment implémenter l'authentification à deux facteurs avec PyOTP et Google
  Authenticator dans votre application Flask
seo_desc: 'Two-Factor Authentication, or 2FA, is like having an extra lock on the
  door to your online accounts. Instead of just using a password, 2FA adds another
  layer of security. It''s a bit like needing both a key and a special code to open
  a vault.

  Think of...'
---

L'authentification à deux facteurs, ou 2FA, est comme avoir un verrou supplémentaire sur la porte de vos comptes en ligne. Au lieu d'utiliser uniquement un mot de passe, le 2FA ajoute une couche de sécurité supplémentaire. C'est un peu comme avoir besoin à la fois d'une clé et d'un code spécial pour ouvrir un coffre-fort.

Imaginez cela comme un bouclier pour vos comptes. Les mots de passe peuvent parfois être devinés ou volés, mais avec le 2FA, même si quelqu'un obtient votre mot de passe, il aurait toujours besoin de ce code ou de cet appareil supplémentaire pour entrer. C'est une étape supplémentaire qui rend vos comptes beaucoup plus difficiles à pirater pour les hackers.

Alors, explorons comment configurer cette couche de protection supplémentaire en utilisant PyOTP et Google Authenticator dans votre application Flask.

### Table des matières :

1. [Aperçu de PyOTP et Google Authenticator](#heading-apercu-de-pyotp-et-google-authenticator)
2. [Flux de travail de l'authentification à deux facteurs dans notre application](#heading-flux-de-travail-de-l-authentification-a-deux-facteurs-dans-notre-application)
3. [Prérequis](#heading-prerequis)
4. [Préparez vos outils](#heading-preparez-vos-outils)
5. [Comment configurer le projet](#heading-comment-configurer-le-projet)
6. [Comment créer des plans pour les comptes et le cœur](#heading-comment-creer-des-plans-pour-les-comptes-et-le-cœur)
7. [Comment créer un modèle d'utilisateur](#heading-comment-creer-un-modele-d-utilisateur)
8. [Comment ajouter Flask-Login](#heading-comment-ajouter-flask-login)
9. [Comment ajouter des modèles et des fichiers statiques](#heading-comment-ajouter-des-modeles-et-des-fichiers-statiques)
10. [Comment créer la page d'accueil](#heading-comment-creer-la-page-d-accueil)
11. [Comment implémenter l'inscription des utilisateurs](#heading-comment-implementer-l-inscription-des-utilisateurs)
12. [Comment implémenter la connexion des utilisateurs](#heading-comment-implementer-la-connexion-des-utilisateurs)
13. [Comment déconnecter les utilisateurs](#heading-comment-deconnecter-les-utilisateurs)
14. [Comment ajouter la page de configuration du 2FA](#heading-comment-ajouter-la-page-de-configuration-du-2fa)
15. [Comment ajouter une page de vérification du 2FA](#heading-comment-ajouter-une-page-de-verification-du-2fa)
16. [Comment exécuter l'application terminée pour la première fois](#heading-comment-executer-l-application-terminee-pour-la-premiere-fois)
17. [Conclusion](#heading-conclusion)

## Aperçu de PyOTP et Google Authenticator

PyOTP est une bibliothèque Python incroyablement pratique pour générer des mots de passe à usage unique basés sur le temps (TOTP) et des mots de passe à usage unique basés sur HMAC (HOTP). Son rôle principal consiste à créer ces codes uniques et sensibles au temps qui ajoutent une couche de sécurité supplémentaire aux comptes utilisateurs.

En intégrant PyOTP dans votre application Flask, vous pouvez facilement implémenter l'authentification à deux facteurs (2FA) en générant et en vérifiant ces OTP.

Si vous êtes nouveau dans PyOTP ou si vous souhaitez une révision de ses fonctionnalités, je vous recommande de consulter mon précédent [guide sur PyOTP](https://blog.ashutoshkrris.in/how-to-generate-otps-using-pyotp-in-python). Cette compréhension sera bénéfique lorsque nous aborderons l'intégration de PyOTP dans votre application Flask pour l'authentification à deux facteurs (2FA).

Google Authenticator, quant à lui, se distingue comme l'une des applications de génération d'OTP les plus largement utilisées disponibles. Il fonctionne comme une plateforme sécurisée pour générer des OTP basés sur le temps, compatible avec divers services et applications prenant en charge le 2FA. Les utilisateurs peuvent facilement configurer Google Authenticator sur leurs appareils pour générer ces codes sensibles au temps, ajoutant un niveau de sécurité supplémentaire à leurs comptes.

## Flux de travail de l'authentification à deux facteurs dans notre application

Voici une description du flux de l'authentification à deux facteurs dans notre application :

1. **Inscription avec configuration du 2FA** : Lorsque les utilisateurs s'inscrivent sur notre site web, ils sont invités à configurer une couche de sécurité supplémentaire—le 2FA. Cela implique de scanner un code QR à l'aide d'une application d'authentification, telle que Google Authenticator, pour lier leur compte de manière sécurisée.
2. **Initiation de la connexion** : Lorsque les utilisateurs reviennent pour se connecter, ils commencent par entrer leur combinaison habituelle email/nom d'utilisateur et mot de passe pour accéder à leur compte.
3. **Vérification de sécurité supplémentaire** : Avant d'accorder l'accès, notre site web ajoute un obstacle supplémentaire : les utilisateurs doivent fournir un OTP (mot de passe à usage unique) affiché sur leur application d'authentification. Cela garantit qu'ils ne saisissent pas seulement le mot de passe, mais confirment également leur identité avec un code unique et sensible au temps.
4. **Validation et autorisation** : L'utilisateur saisit l'OTP reçu dans notre plateforme. Le système vérifie ensuite cet OTP par rapport au code attendu, validant les informations. Si l'OTP correspond, c'est comme donner la poignée de main secrète, accordant à l'utilisateur l'accès à son compte.

Cet échange fluide entre les mots de passe, les applications d'authentification et les codes uniques garantit que seul le propriétaire légitime du compte peut accéder au contenu précieux derrière les portes numériques de votre site web.

Si vous aimez également l'apprentissage visuel, voici une vidéo montrant comment l'application fonctionne.

%[https://www.youtube.com/watch?v=qzLcbq5-UNA]

Maintenant, passons à un peu de codage !

## Prérequis

Avant de commencer avec le tutoriel, assurez-vous d'avoir satisfait les exigences suivantes :

* Connaissance pratique de Python
* Python 3.8+ installé sur votre système
* Connaissance de base de [Flask](https://ashutoshkrris.hashnode.dev/getting-started-with-flask) et des [Flask Blueprints](https://ashutoshkrris.hashnode.dev/how-to-use-blueprints-to-organize-your-flask-apps)
* Connaissance de [l'authentification de base dans Flask](https://blog.ashutoshkrris.in/how-to-set-up-basic-user-authentication-in-a-flask-app) (optionnel)

## **Préparez vos outils**

Vous aurez besoin de quelques bibliothèques externes pour ce projet. Apprenons-en plus sur elles et installons-les une par une.

Mais avant de les installer, créons un environnement virtuel et activons-le.

Commencez par créer le répertoire du projet et naviguez jusqu'à lui comme ceci :

```bash
mkdir flask-two-factor-auth
cd flask-two-factor-auth
```

Nous allons créer un environnement virtuel en utilisant `venv`. Python est maintenant livré avec une bibliothèque `venv` préinstallée. Donc, pour créer un environnement virtuel, vous pouvez utiliser la commande suivante :

```bash
python -m venv env
```

La commande ci-dessus créera un environnement virtuel nommé env. Maintenant, nous devons activer l'environnement en utilisant cette commande :

```bash
source env/Scripts/activate
```

Pour vérifier si l'environnement a été activé ou non, vous pouvez voir `(env)` dans votre terminal. Maintenant, nous pouvons installer les bibliothèques.

* [Flask](https://flask.palletsprojects.com/en/2.2.x/) est un microframework simple et facile à utiliser pour Python qui vous aide à construire des applications web scalables et sécurisées.
* [Flask-Login](https://flask-login.readthedocs.io/en/latest/) fournit une gestion de session utilisateur pour Flask. Il gère les tâches courantes de connexion, de déconnexion et de mémorisation des sessions de vos utilisateurs sur de longues périodes.
* [Flask-Bcrypt](https://flask-bcrypt.readthedocs.io/en/1.0.1/) est une extension Flask qui fournit des utilitaires de hachage bcrypt pour votre application.
* [Flask-WTF](https://flask-wtf.readthedocs.io/en/1.0.x/) est une intégration simple de Flask et WTForms qui vous aide à créer des formulaires dans Flask.
* [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/) est une extension qui gère les migrations de base de données SQLAlchemy pour les applications Flask en utilisant Alembic. Les opérations de base de données sont disponibles via l'interface de ligne de commande Flask.
* [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) est une extension pour Flask qui ajoute le support de SQLAlchemy à votre application. Il vous aide à simplifier les choses en utilisant SQLAlchemy avec Flask en vous donnant des valeurs par défaut utiles et des aides supplémentaires qui facilitent l'exécution des tâches courantes.
* [PyOTP](https://blog.ashutoshkrris.in/how-to-generate-otps-using-pyotp-in-python) vous aide à générer des OTP en utilisant des algorithmes OTP basés sur le temps (TOTP) et OTP basés sur HMAC (HOTP) sans effort.
* [QRCode](https://pypi.org/project/qrcode/) vous aide à générer des codes QR en Python
* [Python Decouple](https://pypi.org/project/python-decouple/) vous aide à utiliser des variables d'environnement dans votre projet Python.

Pour installer les bibliothèques mentionnées ci-dessus en une seule fois, exécutez la commande suivante :

```bash
pip install Flask Flask-Login Flask-Bcrypt Flask-WTF Flask-Migrate Flask-SQLAlchemy pyotp qrcode python-decouple
```

## **Comment configurer le projet**

Commençons par créer un répertoire `src` :

```bash
mkdir src
```

Le premier fichier sera le fichier `__init__.py` pour le projet :

```python
from decouple import config
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(config("APP_SETTINGS"))

bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Enregistrement des blueprints
from src.accounts.views import accounts_bp
from src.core.views import core_bp

app.register_blueprint(accounts_bp)
app.register_blueprint(core_bp)
```

Dans le script ci-dessus, nous avons créé une application Flask appelée `app`. Nous utilisons l'argument `__name__` pour indiquer le module ou le package de l'application afin que Flask sache où trouver d'autres fichiers tels que les templates. Nous avons également défini la configuration de l'application en utilisant une variable d'environnement appelée `APP_SETTINGS`. Nous l'exporterons plus tard.

Pour utiliser Flask-Bcrypt, Flask-SQLAlchemy et Flask-Migrate dans notre application, nous devons simplement créer des objets des classes `Bcrypt`, `SQLAlchemy` et `Migrate` des bibliothèques `flask_bcrypt`, `flask_sqlalchemy` et `flask_migrate`, respectivement.

Nous avons également enregistré des blueprints appelés `accounts_bp` et `core_bp` dans l'application. Nous les définirons plus tard dans le tutoriel.

Dans le répertoire racine du projet (c'est-à-dire à l'extérieur du répertoire `src`), créez un fichier appelé `config.py`. Nous stockerons les configurations pour le projet dans ce fichier. À l'intérieur du fichier, ajoutez le contenu suivant :

```python
from decouple import config

DATABASE_URI = config("DATABASE_URL")
if DATABASE_URI.startswith("postgres://"):
    DATABASE_URI = DATABASE_URI.replace("postgres://", "postgresql://", 1)


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = config("SECRET_KEY", default="guess-me")
    SQLALCHEMY_DATABASE_URI = DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BCRYPT_LOG_ROUNDS = 13
    WTF_CSRF_ENABLED = True
    DEBUG_TB_ENABLED = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    APP_NAME = config("APP_NAME")


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    WTF_CSRF_ENABLED = False
    DEBUG_TB_ENABLED = True


class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///testdb.sqlite"
    BCRYPT_LOG_ROUNDS = 1
    WTF_CSRF_ENABLED = False


class ProductionConfig(Config):
    DEBUG = False
    DEBUG_TB_ENABLED = False

```

Dans le script ci-dessus, nous avons créé une classe `Config` et défini divers attributs à l'intérieur de celle-ci. Nous avons également créé différentes classes enfants (selon les différentes étapes de développement) qui héritent de la classe `Config`.

Remarquez que nous utilisons quelques variables d'environnement comme `SECRET_KEY`, `DATABASE_URL` et `APP_NAME`. Créez un fichier nommé `.env` dans le répertoire racine et ajoutez le contenu suivant :

```python
export SECRET_KEY=fdkjshfhjsdfdskfdsfdcbsjdkfdsdf
export DEBUG=True
export APP_SETTINGS=config.DevelopmentConfig
export DATABASE_URL=sqlite:///db.sqlite
export FLASK_APP=src
export FLASK_DEBUG=1
export APP_NAME="Flask User Authentication App"
```

En plus de `SECRET_KEY`, `DATABASE_URL` et `APP_NAME`, nous avons également exporté `APP_SETTINGS`, `DEBUG`, `FLASK_APP` et `FLASK_DEBUG`.

`APP_SETTINGS` fait référence à l'une des classes que nous avons créées dans le fichier `config.py`. Nous le définissons à l'étape actuelle du projet.

La valeur de `FLASK_APP` est le nom du package que nous avons créé. Comme l'application est en phase de développement, vous pouvez définir les valeurs de `DEBUG` et `FLASK_DEBUG` à `True` et `1`, respectivement.

Exécutez la commande suivante pour exporter toutes les variables d'environnement du fichier `.env` :

```bash
source .env
```

Ensuite, nous allons créer une application CLI de l'application afin que nous puissions ajouter des commandes personnalisées si nécessaire.

Créez un fichier `manage.py` dans le répertoire racine de l'application et ajoutez le code suivant :

```python
from flask.cli import FlaskGroup

from src import app

cli = FlaskGroup(app)


if __name__ == "__main__":
    cli()

```

Maintenant, votre application de base est prête. Vous pouvez l'exécuter en utilisant la commande suivante :

```bash
python manage.py run
```

Votre structure de fichiers devrait ressembler à ce qui suit pour l'instant :

```bash
flask-two-factor-auth/
├── src/
│   └── __init__.py
├── .env
├── config.py
└── manage.py
```

## **Comment créer des blueprints pour les comptes et le cœur**

Comme mentionné précédemment, vous utiliserez les concepts de blueprints dans le projet. Créons deux blueprints – `accounts_bp` et `core_bp` – dans cette section.

Tout d'abord, créez un répertoire appelé `accounts` comme ceci :

```bash
mkdir accounts
cd accounts
```

Ensuite, ajoutez un fichier `__init__.py` vide pour le convertir en un package Python. Maintenant, créez un fichier `views.py` à l'intérieur du package où vous stockerez toutes vos routes liées à l'authentification des utilisateurs.

```bash
touch __init__.py views.py
```

Ajoutez le code suivant à l'intérieur du fichier `views.py` :

```python
from flask import Blueprint

accounts_bp = Blueprint("accounts", __name__)
```

Dans le script ci-dessus, vous avez créé un blueprint appelé `accounts_bp` pour le package `accounts`.

De même, vous pouvez créer un package `core` dans le répertoire racine et ajouter un fichier `views.py`.

```bash
mkdir core
cd core
touch __init__.py views.py
```

Maintenant, ajoutez le code suivant à l'intérieur du fichier `views.py` :

```python
from flask import Blueprint

core_bp = Blueprint("core", __name__)
```

Remarque : Si vous êtes nouveau dans Flask Blueprints, assurez-vous de consulter [ce tutoriel](https://ashutoshkrris.hashnode.dev/how-to-use-blueprints-to-organize-your-flask-apps) pour en savoir plus sur son fonctionnement.

Maintenant, votre structure de fichiers devrait ressembler à ce que vous voyez ci-dessous :

```bash
flask-two-factor-auth/
├── src/
│   ├── accounts/
│   │   ├── __init__.py
│   │   └── views.py
│   ├── core/
│   │   ├── __init__.py
│   │   └── views.py
│   └── __init__.py
├── .env
├── config.py
└── manage.py
```

## **Comment créer un modèle d'utilisateur**

Créons un fichier `models.py` à l'intérieur du package `accounts`.

```bash
touch src/accounts/models.py
```

À l'intérieur du fichier `models.py`, ajoutez le code suivant :

```python
from datetime import datetime

import pyotp
from flask_login import UserMixin

from src import bcrypt, db
from config import Config


class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    is_two_factor_authentication_enabled = db.Column(
        db.Boolean, nullable=False, default=False)
    secret_token = db.Column(db.String, unique=True)

    def __init__(self, username, password):
        self.username = username
        self.password = bcrypt.generate_password_hash(password)
        self.created_at = datetime.now()
        self.secret_token = pyotp.random_base32()

    def get_authentication_setup_uri(self):
        return pyotp.totp.TOTP(self.secret_token).provisioning_uri(
            name=self.username, issuer_name=Config.APP_NAME)

    def is_otp_valid(self, user_otp):
        totp = pyotp.parse_uri(self.get_authentication_setup_uri())
        return totp.verify(user_otp)

    def __repr__(self):
        return f"<user {self.username}>"
```

Dans le code ci-dessus, vous avez créé un modèle `User` en héritant de la classe `db.Model`. Le modèle `User` se compose des champs suivants :

* `id` : stocke la clé primaire pour la table `users`
* `username` : stocke le nom d'utilisateur de l'utilisateur
* `password` : stocke le mot de passe haché de l'utilisateur
* `created_at` : stocke l'horodatage lorsque l'utilisateur a été créé
* `is_two_factor_authentication_enabled` : indicateur booléen qui stocke si l'utilisateur a activé l'authentification à deux facteurs. La valeur par défaut est `False`.
* `secret_token` : stocke un jeton unique généré pour chaque utilisateur, essentiel pour implémenter l'authentification à deux facteurs.

Le constructeur initialise l'objet `User` lors de l'instanciation en acceptant les paramètres `username` et `password`. Il hache le mot de passe fourni en utilisant `bcrypt.generate_password_hash(password)`, enregistre l'horodatage actuel comme valeur `created_at`, et génère un `secret_token` unique en utilisant `pyotp.random_base32()` pour la configuration du 2FA.

La méthode `get_authentication_setup_uri()` génère une URI de configuration utilisée par les applications d'authentification comme Google Authenticator. Elle construit une URI contenant le nom d'utilisateur de l'utilisateur et le nom de l'application (`Config.APP_NAME`) nécessaire pour configurer l'authentification à deux facteurs. Le format de base de l'URI est :

```bash
otpauth://totp/Example:alice@google.com?secret=JBSWY3DPEHPK3PXP&issuer=Example
```

où alice@google.com est le nom d'utilisateur de l'utilisateur et Example est le nom de l'application.

Ensuite, la méthode `is_otp_valid()` vérifie le mot de passe à usage unique (OTP) saisi par l'utilisateur lors de la connexion. Elle analyse l'URI de configuration générée précédemment, vérifie la validité de l'OTP fourni (`user_otp`), et retourne `True` si l'OTP correspond, garantissant une authentification sécurisée.

Enfin, la méthode `__repr__` fournit une représentation sous forme de chaîne de l'objet `User`, affichant le nom d'utilisateur associé lorsqu'une instance de la classe est imprimée ou représentée sous forme de chaîne.

## **Comment ajouter Flask-Login**

La partie la plus importante de Flask-Login est la classe `LoginManager` qui permet à votre application et Flask-Login de travailler ensemble.

Dans le fichier `src/__init__.py`, ajoutez le code suivant :

```python
from decouple import config
from flask import Flask
from flask_login import LoginManager # Ajoutez cette ligne
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(config("APP_SETTINGS"))

login_manager = LoginManager() # Ajoutez cette ligne
login_manager.init_app(app) # Ajoutez cette ligne
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Enregistrement des blueprints
from src.accounts.views import accounts_bp
from src.core.views import core_bp

app.register_blueprint(accounts_bp)
app.register_blueprint(core_bp)
```

Dans le script ci-dessus, nous avons créé et initialisé le gestionnaire de connexion dans notre application.

Ensuite, nous devons fournir un rappel `user_loader`. Ce rappel est utilisé pour recharger l'objet utilisateur à partir de l'ID d'utilisateur stocké dans la session. Il doit prendre l'ID d'un utilisateur et retourner l'objet utilisateur correspondant.

```python
from src.accounts.models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == int(user_id)).first()
```

Le modèle `User` doit implémenter les propriétés et méthodes suivantes :

* `is_authenticated` : Cette propriété retourne True si l'utilisateur est authentifié.
* `is_active` : Cette propriété retourne True si cet utilisateur est actif (le compte est activé)
* `is_anonymous` : Cette propriété retourne True si cet utilisateur est anonyme (les utilisateurs réels retournent False).
* `get_id()` : Cette méthode retourne une chaîne qui identifie de manière unique cet utilisateur et peut être utilisée pour charger l'utilisateur à partir du rappel `user_loader`.

Maintenant, nous n'avons pas besoin de les implémenter explicitement. Au lieu de cela, Flask-Login fournit une classe `UserMixin` qui contient les implémentations par défaut pour toutes ces propriétés et méthodes. Nous devons simplement en hériter de la manière suivante :

```python
from datetime import datetime

from flask_login import UserMixin # Ajoutez cette ligne

from src import bcrypt, db


class User(UserMixin, db.Model): # Changez cette ligne
	....
```

Nous pouvons également personnaliser le processus de connexion par défaut dans le fichier `src/__init__.py`.

Le nom de la vue de connexion peut être défini comme `LoginManager.login_view`. La valeur fait référence au nom de la fonction qui gérera le processus de connexion.

```python
login_manager.login_view = "accounts.login"
```

Pour personnaliser la catégorie du message, définissez `LoginManager.login_message_category` :

```python
login_manager.login_message_category = "danger"
```

## **Comment ajouter des modèles et des fichiers statiques**

Créons un fichier CSS appelé `styles.css` dans le dossier `src/static` :

```css
.error {
  color: red;
  margin-bottom: 5px;
  text-align: center;
}

a {
  text-decoration: none;
}

```

Créons également les modèles de base dans le dossier `src/templates`. Créez un fichier `_base.html` et ajoutez le code suivant :

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Two Factor Authentication</title>
    <!-- meta -->
    <meta name="description" content="">
    <meta name="author" content="">
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <!-- styles -->
    <!-- CSS only -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
    <link rel="stylesheet" href="{{url_for('static', filename="styles.css")}}">
    {% block css %}{% endblock %}
  </head>
  <body>

    {% include "navigation.html" %}

    <div class="container">

      <br>

      <!-- messages -->
      {% with messages = get_flashed_messages(with_categories=true) %}
      {% if messages %}
      <div class="row">
        <div class="col-md-4"></div>
        <div class="col-md-4">
          {% for category, message in messages %}
          <div class="alert alert-{{ category }} alert-dismissible fade show" role="alert">
           {{message}}
           <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
          </div>
          {% endfor %}
        </div>
        <div class="col-md-4"></div>
      </div>
      {% endif %}
      {% endwith %}

      <!-- child template -->
      {% block content %}{% endblock %}

    </div>

    <!-- scripts -->
    <script src="https://code.jquery.com/jquery-3.7.1.min.js" integrity="sha256-/JqT3SQfawRcv/BIHPThkBvs0OEvtFFmqPF/lYI/Cxo=" crossorigin="anonymous"></script>
    <!-- JavaScript Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js" integrity="sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.min.js" integrity="sha384-BBtl+eGJRgqQAUMxJ7pMwbEyER4l1g+O15P+16Ep7Q9Q+zqX6gSbd85u4mG4QzX+" crossorigin="anonymous"></script>
    {% block js %}{% endblock %}
  </body>
</html>
```

Le fichier `_base.html` est le fichier HTML parent qui sera hérité par les autres modèles. Nous avons ajouté la prise en charge de Bootstrap 5 dans le fichier ci-dessus. Nous utilisons également les messages flash de Flask pour afficher des alertes Bootstrap dans l'application.

Créons également un fichier `navigation.html` qui contient la barre de navigation de l'application :

```html
<!-- Navigation -->
<nav class="navbar bg-dark navbar-expand-lg bg-body-tertiary p-3" data-bs-theme="dark">
  <div class="container-fluid">
    <a class="navbar-brand" href="{{ url_for('core.home') }}">Two-Factor Authentication App</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      {% if current_user.is_authenticated %}
      <a href="{{ url_for('accounts.logout') }}"><button type="button" class="btn btn-danger me-2">Logout</button></a>
      {% endif %}
    </div>
  </div>
</nav>
```

Notez que nous n'avons pas encore créé les vues utilisées ci-dessus.

## **Comment créer la page d'accueil**

Dans cette section, nous allons d'abord créer une fonction de vue pour la page d'accueil à l'intérieur du fichier `core/views.py`. Ajoutez le code suivant :

```python
from flask import Blueprint, render_template
from flask_login import login_required

core_bp = Blueprint("core", __name__)


@core_bp.route("/")
@login_required
def home():
    return render_template("core/index.html")

```

Remarquez que nous avons utilisé le blueprint pour ajouter la route. Nous avons également ajouté un middleware `@login_required` pour empêcher l'accès aux utilisateurs non authentifiés.

Ensuite, créons un fichier `index.html` à l'intérieur du dossier `templates/core` et ajoutons le code suivant :

```html
{% extends "_base.html" %}
{% block content %}

<h1 class="text-center">Bienvenue {{current_user.username}} !</h1>

{% endblock %}
```

La page HTML aura simplement un message de bienvenue pour les utilisateurs authentifiés.

Votre structure de fichiers devrait ressembler à ce qui suit pour l'instant :

```bash
flask-two-factor-auth/
├── src/
│   ├── accounts/
│   │   ├── __init__.py
│   │   └── views.py
│   ├── core/
│   │   ├── __init__.py
│   │   └── views.py
│   ├── static/
│   │   └── styles.css
│   ├── templates/
│   │   ├── core/
│   │   │   └── index.html
│   │   ├── _base.html
│   │   └── navigation.html
│   └── __init__.py
├── .env
├── config.py
└── manage.py
```

## **Comment implémenter l'inscription des utilisateurs**

Tout d'abord, nous allons créer un formulaire d'inscription en utilisant Flask-WTF. Créez un fichier `forms.py` à l'intérieur du package `accounts` et ajoutez le code suivant :

```python
from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo, Length

from src.accounts.models import User


class RegisterForm(FlaskForm):
    username = StringField(
        "Nom d'utilisateur", validators=[DataRequired(), Length(min=6, max=40)]
    )
    password = PasswordField(
        "Mot de passe", validators=[DataRequired(), Length(min=6, max=25)]
    )
    confirm = PasswordField(
        "Répéter le mot de passe",
        validators=[
            DataRequired(),
            EqualTo("password", message="Les mots de passe doivent correspondre."),
        ],
    )

    def validate(self, extra_validators):
        initial_validation = super(RegisterForm, self).validate(extra_validators)
        if not initial_validation:
            return False
        user = User.query.filter_by(username=self.username.data).first()
        if user:
            self.username.errors.append("Nom d'utilisateur déjà enregistré")
            return False
        if self.password.data != self.confirm.data:
            self.password.errors.append("Les mots de passe doivent correspondre")
            return False
        return True

```

Le `RegisterForm` étend la classe `FlaskForm` et contient trois champs – `username`, `password` et `confirm`. Nous avons ajouté différents validateurs tels que `DataRequired`, `Length`, `Email` et `EqualTo` aux champs respectifs.

Nous avons également défini une méthode `validate()` qui est automatiquement appelée lorsque le formulaire est soumis.

À l'intérieur de la méthode, nous effectuons d'abord la validation initiale fournie par FlaskForm. Si celle-ci est réussie, nous effectuons notre validation personnalisée telle que la vérification si l'utilisateur est déjà enregistré et la correspondance du mot de passe avec le mot de passe confirmé. Si des erreurs surviennent, nous ajoutons le message d'erreur dans les champs respectifs.

Maintenant, utilisons ce formulaire dans le fichier HTML. Créez un répertoire `accounts` dans le dossier `templates` et ajoutez un nouveau fichier appelé `register.html` à l'intérieur. Ajoutez le code suivant :

```html
{% extends "_base.html" %}

{% block content %}

<div class="row">
  <div class="col-md-4"></div>
  <div class="col-md-4">
    <main class="form-signin w-100 m-auto">
      <form role="form" method="post" action="">
        {{ form.csrf_token }}
        <h1 class="h3 mb-3 fw-normal text-center">Veuillez vous inscrire</h1>

        <div class="form-floating">
          {{ form.username(placeholder="Nom d'utilisateur", class="form-control mb-2") }}
          {{ form.username.label }}
            {% if form.username.errors %}
              {% for error in form.username.errors %}
                <div class="alert alert-danger" role="alert">
                  {{ error }}
                </div>
              {% endfor %}
            {% endif %}
        </div>
        <div class="form-floating">
          {{ form.password(placeholder="Mot de passe", class="form-control mb-2") }}
          {{ form.password.label }}
            {% if form.password.errors %}
              {% for error in form.password.errors %}
                <div class="alert alert-danger" role="alert">
                  {{ error }}
                </div>
              {% endfor %}
            {% endif %}
        </div>
        <div class="form-floating">
          {{ form.confirm(placeholder="Confirmer le mot de passe", class="form-control mb-2") }}
          {{ form.confirm.label }}
            {% if form.confirm.errors %}
              {% for error in form.confirm.errors %}
                <div class="alert alert-danger" role="alert">
                  {{ error }}
                </div>
              {% endfor %}
            {% endif %}
        </div>
        <button class="w-100 btn btn-lg btn-primary" type="submit">S'inscrire</button>
        <p class="text-center mt-3">Déjà inscrit ? <a href="{{ url_for('accounts.login') }}">Connectez-vous maintenant</a></p>
      </form>
    </main>
  </div>
  <div class="col-md-4"></div>
</div>

{% endblock %}
```

Dans le modèle Jinja ci-dessus, nous utilisons le formulaire que nous avons créé et ajoutons une logique de gestion des erreurs pertinente pour les erreurs de validation dans chaque champ. Les utilisateurs peuvent soumettre le formulaire en cliquant sur le bouton "S'inscrire", et un lien en dessous du formulaire permet aux utilisateurs déjà inscrits de naviguer vers la page de connexion pour l'authentification.

Ensuite, utilisons ce formulaire dans le fichier `views.py` pour créer une fonction de gestion du processus d'inscription.

```python
from .forms import RegisterForm
from src.accounts.models import User
from src import db, bcrypt
from flask_login import current_user
from flask import Blueprint, flash, redirect, render_template, request, url_for

accounts_bp = Blueprint("accounts", __name__)

HOME_URL = "core.home"
SETUP_2FA_URL = "accounts.setup_two_factor_auth"
VERIFY_2FA_URL = "accounts.verify_two_factor_auth"

@accounts_bp.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        if current_user.is_two_factor_authentication_enabled:
            flash("Vous êtes déjà inscrit.", "info")
            return redirect(url_for(HOME_URL))
        else:
            flash("Vous n'avez pas activé l'authentification à deux facteurs. Veuillez l'activer d'abord pour vous connecter.", "info")
            return redirect(url_for(SETUP_2FA_URL))
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        try:
            user = User(username=form.username.data, password=form.password.data)
            db.session.add(user)
            db.session.commit()

            login_user(user)
            flash("Vous êtes inscrit. Vous devez activer l'authentification à deux facteurs d'abord pour vous connecter.", "success")

            return redirect(url_for(SETUP_2FA_URL))
        except Exception:
            db.session.rollback()
            flash("L'inscription a échoué. Veuillez réessayer.", "danger")

    return render_template("accounts/register.html", form=form)

```

La route commence par vérifier si l'utilisateur actuel est déjà authentifié. Si c'est le cas, elle vérifie si le 2FA est activé pour l'utilisateur. Si le 2FA est déjà activé, un message informe l'utilisateur qu'il est déjà inscrit, le redirigeant vers l'URL de la page d'accueil. Cependant, si l'utilisateur est authentifié mais que le 2FA n'est pas activé, un message flash invite l'utilisateur à activer le 2FA avant de se connecter, le redirigeant vers l'URL de configuration du 2FA.

Si l'utilisateur n'est pas authentifié ou n'a pas encore enregistré le 2FA, le code initialise un formulaire d'inscription et procède à la validation des données du formulaire lors de la soumission. Une fois la validation du formulaire réussie, nous créons un nouvel objet `User` avec le nom d'utilisateur et le mot de passe fournis et l'enregistrons dans la base de données.

Une fois l'inscription de l'utilisateur réussie, le nouvel utilisateur inscrit est connecté. Un message de succès s'affiche, informant l'utilisateur de l'inscription réussie et l'invitant à activer le 2FA avant de se connecter. Par la suite, l'utilisateur est redirigé vers l'URL de configuration du 2FA pour activer le 2FA.

## **Comment implémenter la connexion des utilisateurs**

Tout d'abord, créons un formulaire de connexion dans le fichier `accounts/forms.py` :

```python
class LoginForm(FlaskForm):
    username = StringField("Nom d'utilisateur", validators=[DataRequired()])
    password = PasswordField("Mot de passe", validators=[DataRequired()])
```

Le formulaire est similaire au formulaire d'inscription mais il n'a que deux champs – `username` et `password`.

Maintenant, utilisons ce formulaire dans un nouveau fichier HTML appelé `login.html` créé dans le répertoire `templates/accounts`. Ajoutez le code suivant :

```html
{% extends "_base.html" %}

{% block content %}

<div class="row">
  <div class="col-md-4"></div>
  <div class="col-md-4">
    <main class="form-signin w-100 m-auto">
      <form role="form" method="post" action="">
        {{ form.csrf_token }}
        <h1 class="h3 mb-3 fw-normal text-center">Veuillez vous connecter</h1>

        <div class="form-floating">
          {{ form.username(placeholder="Nom d'utilisateur", class="form-control mb-2") }}
          {{ form.username.label }}
            {% if form.username.errors %}
              {% for error in form.username.errors %}
              <div class="alert alert-danger" role="alert">
                {{ error }}
              </div>
              {% endfor %}
            {% endif %}
        </div>
        <div class="form-floating">
          {{ form.password(placeholder="Mot de passe", class="form-control mb-2") }}
          {{ form.password.label }}
            {% if form.password.errors %}
              {% for error in form.password.errors %}
                <div class="alert alert-danger" role="alert">
                  {{ error }}
                </div>
              {% endfor %}
            {% endif %}
        </div>
        <button class="w-100 btn btn-lg btn-primary" type="submit">Se connecter</button>
        <p class="text-center mt-3">Nouvel utilisateur ? <a href="{{ url_for('accounts.register') }}">Inscrivez-vous maintenant</a></p>
      </form>
    </main>
  </div>
  <div class="col-md-4"></div>
</div>

{% endblock %}
```

Le fichier HTML ci-dessus est également similaire au fichier `register.html` mais avec seulement deux champs pour le nom d'utilisateur et le mot de passe.

Ensuite, créons une fonction de vue pour gérer le processus de connexion à l'intérieur du fichier `accounts/views.py` :

```python
from .forms import LoginForm, RegisterForm

@accounts_bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        if current_user.is_two_factor_authentication_enabled:
            flash("Vous êtes déjà connecté.", "info")
            return redirect(url_for(HOME_URL))
        else:
            flash("Vous n'avez pas activé l'authentification à deux facteurs. Veuillez l'activer d'abord pour vous connecter.", "info")
            return redirect(url_for(SETUP_2FA_URL))
        
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, request.form["password"]):
            login_user(user)
            if not current_user.is_two_factor_authentication_enabled:
                flash(
                    "Vous n'avez pas activé l'authentification à deux facteurs. Veuillez l'activer d'abord pour vous connecter.", "info")
                return redirect(url_for(SETUP_2FA_URL))
            return redirect(url_for(VERIFY_2FA_URL))
        elif not user:
            flash("Vous n'êtes pas inscrit. Veuillez vous inscrire.", "danger")
        else:
            flash("Nom d'utilisateur et/ou mot de passe invalide.", "danger")
    return render_template("accounts/login.html", form=form)
```

La route commence par vérifier si l'utilisateur actuel est déjà authentifié. Si l'utilisateur est authentifié et que le 2FA est activé, un message informe l'utilisateur qu'il est déjà connecté, le redirigeant vers l'URL de la page d'accueil. Si l'utilisateur est authentifié mais que le 2FA n'est pas activé, un message flash invite l'utilisateur à activer le 2FA avant de se connecter, le redirigeant vers l'URL de configuration du 2FA.

Si l'utilisateur n'est pas authentifié, le code initialise un formulaire de connexion et valide les données du formulaire lors de la soumission. Une fois la validation réussie, il interroge la base de données pour trouver un utilisateur correspondant au nom d'utilisateur fourni. Si l'utilisateur existe et que le mot de passe correspond au mot de passe haché stocké dans la base de données, l'utilisateur est connecté.

De plus, si le 2FA n'est pas activé pour l'utilisateur actuel après une connexion réussie, un message flash invite l'utilisateur à activer le 2FA avant de continuer, le redirigeant vers l'URL de configuration du 2FA. Si la connexion est réussie et que le 2FA est activé, l'utilisateur est redirigé vers l'URL de vérification du 2FA.

Si l'utilisateur n'est pas inscrit, un message flash l'informe de s'inscrire. S'il y a une non-correspondance dans le nom d'utilisateur ou le mot de passe fourni, un autre message flash notifie à l'utilisateur des informations d'identification invalides.

## Comment déconnecter les utilisateurs

Déconnecter l'utilisateur est un processus très simple. Vous devez simplement créer une fonction de vue pour cela à l'intérieur du fichier `accounts/views.py` :

```python
from flask_login import login_required, login_user, logout_user


@accounts_bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Vous avez été déconnecté.", "success")
    return redirect(url_for("accounts.login"))

```

La bibliothèque `Flask-Login` contient une méthode `logout_user` qui supprime l'utilisateur de la session. Nous avons utilisé le décorateur `@login_required` afin que seuls les utilisateurs authentifiés puissent se déconnecter.

## Comment ajouter la page de configuration du 2FA

Jusqu'à présent, nous avons redirigé les utilisateurs vers la page de configuration du 2FA chaque fois que le 2FA n'est pas activé dans leurs comptes, mais nous ne l'avons pas encore implémenté. Faisons cela dans cette section.

Commençons par la route de la page :

```python
from src.utils import get_b64encoded_qr_image

@accounts_bp.route("/setup-2fa")
@login_required
def setup_two_factor_auth():
    secret = current_user.secret_token
    uri = current_user.get_authentication_setup_uri()
    base64_qr_image = get_b64encoded_qr_image(uri)
    return render_template("accounts/setup-2fa.html", secret=secret, qr_image=base64_qr_image)

```

La route, créée dans `accounts/views.py`, garantit que seuls les utilisateurs authentifiés peuvent y accéder en utilisant le décorateur `@login_required`.

Lors de l'accès à cette route, la fonction récupère le `secret_token` de l'utilisateur actuel pour la configuration du 2FA et génère une URI via `current_user.get_authentication_setup_uri()` pour configurer une application d'authentification comme Google Authenticator.

Elle utilise également `get_b64encoded_qr_image(uri)` pour obtenir une image de code QR encodée en Base64 représentant cette URI de configuration. Nous allons la définir ci-dessous.

Enfin, elle rend le modèle `setup-2fa.html`, en passant le `secret_token` de l'utilisateur et l'image QR encodée en Base64 au modèle pour que les utilisateurs puissent la scanner.

Ensuite, créez un fichier `utils.py` dans le répertoire `src` et ajoutez le code suivant pour [générer le QR](https://blog.ashutoshkrris.in/5-quick-python-projects#heading-qr-codes-in-python) :

```python
from io import BytesIO
import qrcode
from base64 import b64encode


def get_b64encoded_qr_image(data):
    print(data)
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color='black', back_color='white')
    buffered = BytesIO()
    img.save(buffered)
    return b64encode(buffered.getvalue()).decode("utf-8")

```

Vous vous souvenez de la bibliothèque `qrcode` que nous avons installée au début du tutoriel ? C'est ici que nous allons l'utiliser.

Lors de la réception de `data` en entrée, représentant le contenu à intégrer dans le code QR, la fonction initialise un objet QRCode en utilisant la bibliothèque `qrcode`. Elle ajoute les données fournies à cette instance de code QR et génère le code QR. Le code convertit ensuite ce code QR en une représentation d'image.

En utilisant un objet BytesIO, il stocke cette image en mémoire. La fonction procède à l'encodage du contenu de ce tampon en mémoire, représentant l'image du code QR, au format Base64. Enfin, elle retourne cette chaîne encodée en Base64, encapsulant l'image du code QR, prête pour la transmission ou l'affichage dans diverses applications.

Ensuite, créons la page `setup-2fa.html` dans le dossier `templates/accounts` et ajoutons le contenu suivant :

```html
{% extends "_base.html" %}

{% block content %}

<div class="row">
  <div class="col-md-4"></div>
  <div class="col-md-4">
    <main class="form-signin w-100 m-auto">
      <form role="form">
        <h5>Instructions !</h5>
          <ul>
            <li>Téléchargez <a href="https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2&hl=en&gl=US" target="_blank">Google Authenticator</a> sur votre mobile.</li>
            <li>Configurez un nouvel authentificateur.</li>
            <li>Une fois que vous avez scanné le QR, veuillez cliquer <a href="{{ url_for('accounts.verify_two_factor_auth') }}">ici.</li>
          </ul>
          <div class="text-center">
            <img src="data:image/png;base64, {{ qr_image }}" alt="Jeton Secret" style="width:200px;height:200px"/>
          </div>
        <div class="form-group">
          <label for="secret">Jeton Secret</label>
          <input type="text" class="form-control" id="secret" value="{{ secret }}" readonly>
        </div>
        <div class="text-center mt-2">
          <button type="button" class="btn btn-primary" onclick="copySecret()">
            Copier le Secret
          </button>
        </div>
        <p class="mt-4 text-center">
          Une fois que vous avez scanné le QR, veuillez cliquer <a href="{{ url_for('accounts.verify_two_factor_auth') }}">ici</a>.
        </p>
      </form>
    </main>
  </div>
  <div class="col-md-4"></div>
</div>

{% endblock %}

{% block js %}
<script>
    function copySecret() {
    var copyText = document.getElementById("secret");
    copyText.select();
    copyText.setSelectionRange(0, 99999); /*Pour les appareils mobiles*/
    document.execCommand("copy");
    alert("Jeton secret TOTP copié avec succès !");
  }
</script>
{% endblock %}
```

Nous ajoutons quelques instructions dans la page pour que les utilisateurs les suivent. Ces instructions fournissent des étapes claires pour que les utilisateurs activent le 2FA : en les dirigeant pour télécharger l'application Google Authenticator via un lien, en les guidant dans le processus de configuration dans l'application, et en les invitant à cliquer sur un lien après avoir scanné le code QR affiché.

L'affichage du code QR est central dans le processus de configuration. Le modèle intègre l'image du code QR en utilisant une balise `<img>` avec sa source définie sur une chaîne encodée en Base64 (`{{ qr_image }}`). Cette image représente la clé secrète essentielle pour la configuration du 2FA.

Nous affichons également la clé secrète en mode lecture seule, permettant aux utilisateurs de voir la clé sans pouvoir la modifier. Nous avons ajouté un bouton de copie pour faciliter la copie de la clé par les utilisateurs.

De plus, nous avons ajouté un lien vers la page de vérification du 2FA, guidant les utilisateurs à poursuivre le processus de configuration après avoir scanné le code QR. Nous implémenterons cette fonctionnalité dans la section suivante.

Voici à quoi ressemble votre page pour l'instant :

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Screenshot-2023-11-26-010925.png)
_Page de configuration du 2FA_

## Comment ajouter une page de vérification du 2FA

Dans cette section, implémentons la vérification du 2FA. Pour commencer, nous aurons besoin d'un formulaire OTP où les utilisateurs peuvent entrer leur OTP. Ajoutez le contenu suivant dans le fichier `accounts/forms.py` :

```python
class TwoFactorForm(FlaskForm):
    otp = StringField('Entrez l\'OTP', validators=[
                      InputRequired(), Length(min=6, max=6)])
```

Le `TwoFactorForm` contient un seul champ (`otp`) pour obtenir l'OTP des utilisateurs.

Maintenant, utilisons ce formulaire dans le fichier `verify-2fa.html` à l'intérieur du dossier `templates/accounts` :

```html
{% extends "_base.html" %}

{% block content %}

<div class="row">
  <div class="col-md-4"></div>
  <div class="col-md-4">
    <main class="form-signin w-100 m-auto">
      <form role="form" method="post" action="">
        {{ form.csrf_token }}
        <h1 class="h3 mb-3 fw-normal text-center">Entrez l'OTP</h1>

        <div class="form-floating">
          {{ form.otp(placeholder="OTP", class="form-control mb-2") }}
          {{ form.otp.label }}
            {% if form.otp.errors %}
              {% for error in form.otp.errors %}
              <div class="alert alert-danger" role="alert">
                {{ error }}
              </div>
              {% endfor %}
            {% endif %}
        </div>
        <button class="w-100 btn btn-lg btn-primary" type="submit">Vérifier</button>
      </form>
    </main>
  </div>
  <div class="col-md-4"></div>
</div>

{% endblock %}
```

Le modèle Jinja contient essentiellement un formulaire avec un champ pour l'OTP et un bouton de vérification.

Créons la route qui gère la soumission de ce formulaire à l'intérieur du fichier `accounts/views.py` :

```python
@accounts_bp.route("/verify-2fa", methods=["GET", "POST"])
@login_required
def verify_two_factor_auth():
    form = TwoFactorForm(request.form)
    if form.validate_on_submit():
        if current_user.is_otp_valid(form.otp.data):
            if current_user.is_two_factor_authentication_enabled:
                flash("Vérification 2FA réussie. Vous êtes connecté !", "success")
                return redirect(url_for(HOME_URL))
            else:
                try:
                    current_user.is_two_factor_authentication_enabled = True
                    db.session.commit()
                    flash("Configuration 2FA réussie. Vous êtes connecté !", "success")
                    return redirect(url_for(HOME_URL))
                except Exception:
                    db.session.rollback()
                    flash("La configuration 2FA a échoué. Veuillez réessayer.", "danger")
                    return redirect(url_for(VERIFY_2FA_URL))
        else:
            flash("OTP invalide. Veuillez réessayer.", "danger")
            return redirect(url_for(VERIFY_2FA_URL))
    else:
        if not current_user.is_two_factor_authentication_enabled:
            flash(
                "Vous n'avez pas activé l'authentification à deux facteurs. Veuillez l'activer d'abord.", "info")
        return render_template("accounts/verify-2fa.html", form=form)

```

La route commence par initialiser un formulaire (`TwoFactorForm`) destiné à la vérification du 2FA en utilisant les données obtenues de la requête. Lors de la soumission du formulaire, le code procède à plusieurs vérifications conditionnelles pour valider l'OTP saisi par l'utilisateur.

Une fois le formulaire soumis et validé avec succès, le code vérifie l'authenticité de l'OTP en utilisant `current_user.is_otp_valid(form.otp.data)`, qui vérifie si l'OTP saisi est valide pour l'utilisateur actuel. Si l'OTP est valide, le code exécute la logique suivante :

* Si l'OTP fourni est valide et que le 2FA est déjà activé pour l'utilisateur, un message de succès est affiché indiquant une vérification 2FA réussie, et l'utilisateur est redirigé vers l'URL de la page d'accueil.
* Si l'OTP est valide mais que le 2FA n'est pas activé pour l'utilisateur, il tente d'activer le 2FA pour cet utilisateur. Une fois l'activation réussie, un message de succès est affiché, et l'utilisateur est redirigé vers l'URL de la page d'accueil.

De plus, si l'OTP saisi par l'utilisateur est invalide, le code affiche un message d'erreur indiquant un OTP invalide et redirige l'utilisateur vers l'URL de vérification du 2FA pour réessayer le processus de vérification.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Screenshot-2023-11-26-011107.png)
_Page de vérification du 2FA_

Avec cela, nous avons terminé l'implémentation de toutes les fonctionnalités ! 🎉

## **Comment exécuter l'application terminée pour la première fois**

Maintenant que notre application est prête, vous pouvez d'abord migrer la base de données, puis exécuter l'application.

Pour initialiser la base de données (créer un dépôt de migration), utilisez la commande :

```bash
flask db init
```

Pour migrer les changements de la base de données, utilisez la commande :

```bash
flask db migrate
```

Pour appliquer les migrations, utilisez la commande :

```bash
flask db upgrade
```

Comme c'est la première fois que nous exécutons notre application, vous devrez exécuter toutes les commandes ci-dessus. Plus tard, chaque fois que vous apporterez des modifications à la base de données, vous devrez simplement exécuter les deux dernières commandes.

Après cela, vous pouvez exécuter votre application en utilisant la commande :

```
python manage.py run
```

Puisque nous avons terminé le développement, voici à quoi devrait ressembler votre structure de fichiers :

```bash
flask-two-factor-auth/
├── migrations/
├── src/
│   ├── accounts/
│   │   ├── __init__.py
│   │   ├── forms.py
│   │   ├── models.py
│   │   └── views.py
│   ├── core/
│   │   ├── __init__.py
│   │   └── views.py
│   ├── static/
│   │   └── styles.css
│   ├── templates/
│   │   ├── accounts/
│   │   │   ├── login.html
│   │   │   ├── register.html
│   │   │   ├── setup-2fa.html
│   │   │   └── verify-2fa.html
│   │   ├── core/
│   │   │   └── index.html
│   │   ├── _base.html
│   │   └── navigation.html
│   ├── __init__.py
│   └── utils.py
├── .env
├── config.py
└── manage.py
```

## **Conclusion**

Dans ce tutoriel, vous avez appris comment configurer l'authentification à deux facteurs dans votre application Flask en utilisant PyOTP.

Voici le lien vers le [dépôt GitHub](https://github.com/ashutoshkrris/Flask-Two-Factor-Authentication). N'hésitez pas à le consulter chaque fois que vous êtes bloqué.

Voici quelques autres tutoriels que j'ai écrits sur l'authentification, la vérification par e-mail et les OTP que vous pourriez apprécier :

* [Comment configurer l'authentification de base des utilisateurs dans une application Flask](https://blog.ashutoshkrris.in/how-to-set-up-basic-user-authentication-in-a-flask-app)
* [Comment configurer la vérification par e-mail dans une application Flask](https://www.freecodecamp.org/news/how-to-setup-user-authentication-in-flask/)
* [Comment générer des OTP en utilisant PyOTP en Python](https://blog.ashutoshkrris.in/how-to-generate-otps-using-pyotp-in-python)

Merci d'avoir lu. J'espère que vous avez trouvé cet article utile. Vous pouvez me suivre sur [Twitter](https://twitter.com/ashutoshkrris).