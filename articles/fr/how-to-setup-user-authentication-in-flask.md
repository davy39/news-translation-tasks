---
title: Comment configurer l'authentification de base des utilisateurs dans une application
  Flask
subtitle: ''
author: Ashutosh Krishna
co_authors: []
series: null
date: '2023-01-03T14:57:06.000Z'
originalURL: https://freecodecamp.org/news/how-to-setup-user-authentication-in-flask
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/basic-auth.png
tags:
- name: authentication
  slug: authentication
- name: Flask Framework
  slug: flask
seo_title: Comment configurer l'authentification de base des utilisateurs dans une
  application Flask
seo_desc: User authentication is important for protecting sensitive information and
  resources from unauthorized access. It helps ensure that only authorized users can
  access and make changes to data, and helps prevent unauthorized users from gaining
  access to ...
---

L'authentification des utilisateurs est importante pour protéger les informations et ressources sensibles contre les accès non autorisés. Elle aide à garantir que seuls les utilisateurs autorisés peuvent accéder et apporter des modifications aux données, et empêche les utilisateurs non autorisés d'accéder à des informations sensibles.

Il existe différentes méthodes pour implémenter l'authentification des utilisateurs, y compris l'authentification basée sur un mot de passe, l'authentification basée sur un jeton, et ainsi de suite.

Dans ce tutoriel, vous apprendrez comment configurer une authentification de base des utilisateurs – c'est-à-dire une authentification basée sur un mot de passe – dans votre application Flask.

## Démonstration du projet

Voici à quoi ressemblera le résultat final :

%[https://www.youtube.com/watch?v=XxSESg89xEI]

Le lien vers le dépôt GitHub est disponible à la fin du tutoriel. N'hésitez pas à le consulter chaque fois que vous êtes bloqué.

## Prérequis

Avant de commencer le tutoriel, assurez-vous que les conditions suivantes sont remplies :

* Connaissance pratique de Python
* Python 3.8+ installé sur votre système
* Connaissance de base de [Flask](https://ashutoshkrris.hashnode.dev/getting-started-with-flask) et des [Flask Blueprints](https://ashutoshkrris.hashnode.dev/how-to-use-blueprints-to-organize-your-flask-apps)

## Préparez vos outils

Vous aurez besoin de quelques bibliothèques externes pour ce projet. Apprenons-en plus sur elles et installons-les une par une.

Mais avant de les installer, créons un environnement virtuel et activons-le.

Commencez par créer le répertoire du projet et naviguez jusqu'à lui comme ceci :

```bash
mkdir flask-basic-auth
cd flask-basic-auth
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
* [Flask-Login](https://flask-login.readthedocs.io/en/latest/) fournit une gestion de session utilisateur pour Flask. Il gère les tâches courantes de connexion, de déconnexion et de mémorisation des sessions de vos utilisateurs sur des périodes prolongées.
* [Flask-Bcrypt](https://flask-bcrypt.readthedocs.io/en/1.0.1/) est une extension Flask qui fournit des utilitaires de hachage bcrypt pour votre application.
* [Flask-WTF](https://flask-wtf.readthedocs.io/en/1.0.x/) est une intégration simple de Flask et WTForms qui vous aide à créer des formulaires dans Flask.
* [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/) est une extension qui gère les migrations de base de données SQLAlchemy pour les applications Flask en utilisant Alembic. Les opérations de base de données sont disponibles via l'interface de ligne de commande Flask.
* [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) est une extension pour Flask qui ajoute le support de SQLAlchemy à votre application. Elle vous aide à simplifier les choses en utilisant SQLAlchemy avec Flask en vous donnant des valeurs par défaut utiles et des aides supplémentaires qui facilitent l'exécution des tâches courantes.
* L'extension [Flask-Testing](https://pythonhosted.org/Flask-Testing/) fournit des utilitaires de test unitaire pour Flask.
* [Python Decouple](https://pypi.org/project/python-decouple/) vous aide à utiliser des variables d'environnement dans votre projet Python.

Pour installer les bibliothèques mentionnées ci-dessus, exécutez la commande suivante :

```bash
pip install Flask Flask-Login Flask-Bcrypt Flask-WTF Flask-Migrate Flask-SQLAlchemy Flask-Testing python-decouple
```

> Ce tutoriel a été vérifié avec Python V3.11, Flask V2.2.2, Flask-Login V0.6.0, Flask-Bcrypt V1.0.1, Flask-WTF V1.0.1, Flask-SQLAlchemy V2.5.1 et Flask-Testing V0.8.1.

## Comment configurer le projet

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

Dans le script ci-dessus, nous avons créé une application Flask appelée `app`. Nous utilisons l'argument `__name__` pour indiquer le module ou le package de l'application afin que Flask sache où trouver d'autres fichiers tels que les templates. Vous définissez également la configuration de l'application en utilisant une variable d'environnement appelée `APP_SETTINGS`. Vous l'exporterez plus tard.

Pour utiliser Flask-Bcrypt, Flask-SQLAlchemy et Flask-Migrate dans votre application, vous devez simplement créer des objets des classes `Bcrypt`, `SQLAlchemy` et `Migrate` des bibliothèques `flask_bcrypt`, `flask_sqlalchemy` et `flask_migrate`, respectivement.

Vous avez également enregistré des blueprints appelés `accounts_bp` et `core_bp` dans l'application. Vous les définirez plus tard dans le tutoriel.

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

Dans le script ci-dessus, nous avons créé une classe `Config` et défini divers attributs à l'intérieur. Nous avons également créé différentes classes enfants (selon les différentes étapes du développement) qui héritent de la classe `Config`.

Remarquez que nous utilisons quelques variables d'environnement comme `SECRET_KEY` et `DATABASE_URL`. Créez un fichier nommé `.env` dans le répertoire racine et ajoutez le contenu suivant :

```
export SECRET_KEY=fdkjshfhjsdfdskfdsfdcbsjdkfdsdf
export DEBUG=True
export APP_SETTINGS=config.DevelopmentConfig
export DATABASE_URL=sqlite:///db.sqlite
export FLASK_APP=src
export FLASK_DEBUG=1
```

En plus de `SECRET_KEY` et `DATABASE_URL`, nous avons également exporté `APP_SETTINGS`, `DEBUG`, `FLASK_APP` et `FLASK_DEBUG`.

`APP_SETTINGS` fait référence à l'une des classes que nous avons créées dans le fichier `config.py`. Nous le définissons à l'étape actuelle du projet.

La valeur de `FLASK_APP` est le nom du package que nous avons créé. Puisque l'application est en phase de développement, vous pouvez définir les valeurs de `DEBUG` et `FLASK_DEBUG` à `True` et `1`, respectivement.

Exécutez la commande suivante pour exporter toutes les variables d'environnement du fichier `.env` :

```bash
source .env
```

Ensuite, vous allez créer une application CLI de l'application afin de pouvoir ajouter ultérieurement des commandes personnalisées telles que `test` et `create_admin` afin de tester l'application et de créer un administrateur, respectivement.

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

## Comment créer des Blueprints pour les comptes et le cœur

Comme mentionné précédemment, vous allez utiliser les concepts de blueprints dans le projet. Créons deux blueprints – `accounts_bp` et `core_bp` – dans cette section.

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

De même, vous pouvez créer un package `core` dans le répertoire racine, et ajouter un fichier `views.py`.

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

Note : Si vous êtes nouveau dans Flask Blueprints, assurez-vous de parcourir [ce tutoriel](https://ashutoshkrris.hashnode.dev/how-to-use-blueprints-to-organize-your-flask-apps) pour en savoir plus sur son fonctionnement.

## Comment créer un modèle d'utilisateur

Créons un fichier `models.py` à l'intérieur du package `accounts`.

```bash
touch src/accounts/models.py
```

À l'intérieur du fichier `models.py`, ajoutez le code suivant :

```python
from datetime import datetime

from src import bcrypt, db


class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    created_on = db.Column(db.DateTime, nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, email, password, is_admin=False):
        self.email = email
        self.password = bcrypt.generate_password_hash(password)
        self.created_on = datetime.now()
        self.is_admin = is_admin

    def __repr__(self):
        return f"<email {self.email}>"

```

Dans le code ci-dessus, vous avez créé un modèle `User` en héritant de la classe `db.Model`. Le modèle `User` se compose des champs suivants :

* `id` : stocke la clé primaire pour la table `users`
* `email` : stocke l'email de l'utilisateur
* `password` : stocke le mot de passe haché de l'utilisateur
* `created_on` : stocke l'horodatage lorsque l'utilisateur a été créé
* `is_admin` : stocke si l'utilisateur est administrateur ou non

Dans le constructeur de la classe, vous définissez les champs. Remarquez le champ password où vous générez le hachage du mot de passe en utilisant l'objet `bcrypt` importé de l'application.

## Comment ajouter Flask-Login

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

Dans le script ci-dessus, vous avez créé et initialisé le gestionnaire de connexion dans votre application.

Ensuite, vous devez fournir une fonction de rappel `user_loader`. Cette fonction de rappel est utilisée pour recharger l'objet utilisateur à partir de l'ID d'utilisateur stocké dans la session. Elle doit prendre l'ID d'un utilisateur et retourner l'objet utilisateur correspondant.

```python
from src.accounts.models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == int(user_id)).first()
```

Le modèle `User` doit implémenter les propriétés et méthodes suivantes :

* `is_authenticated` : Cette propriété retourne True si l'utilisateur est authentifié.
* `is_active` : Cette propriété retourne True si c'est un utilisateur actif (le compte est activé)
* `is_anonymous` : Cette propriété retourne True si c'est un utilisateur anonyme (les utilisateurs réels retournent False).
* `get_id()` : Cette méthode retourne une chaîne qui identifie de manière unique cet utilisateur, et peut être utilisée pour charger l'utilisateur à partir de la fonction de rappel `user_loader`.

Maintenant, vous n'avez pas besoin de les implémenter explicitement. Au lieu de cela, Flask-Login fournit une classe `UserMixin` qui contient les implémentations par défaut pour toutes ces propriétés et méthodes. Vous devez simplement l'hériter de la manière suivante :

```python
from datetime import datetime

from flask_login import UserMixin # Ajoutez cette ligne

from src import bcrypt, db


class User(UserMixin, db.Model): # Changez cette ligne

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    created_on = db.Column(db.DateTime, nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, email, password, is_admin=False):
        self.email = email
        self.password = bcrypt.generate_password_hash(password)
        self.created_on = datetime.now()
        self.is_admin = is_admin

    def __repr__(self):
        return f"<email {self.email}>"

```

Vous pouvez également personnaliser le processus de connexion par défaut dans le fichier `src/__init__.py`.

Le nom de la vue de connexion peut être défini comme `LoginManager.login_view`. La valeur fait référence au nom de la fonction qui gérera le processus de connexion.

```python
login_manager.login_view = "accounts.login"
```

Pour personnaliser la catégorie de message, définissez `LoginManager.login_message_category` :

```python
login_manager.login_message_category = "danger"
```

## Comment ajouter des templates et des fichiers statiques

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

Créons également les templates de base dans le dossier `src/templates`. Créez un fichier `_base.html` et ajoutez le code suivant :

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Gestion des utilisateurs Flask</title>
    <!-- meta -->
    <meta name="description" content="">
    <meta name="author" content="">
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <!-- styles -->
    <!-- CSS only -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
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
    <script src="https://code.jquery.com/jquery-3.6.1.min.js" type="text/javascript"></script>
    <!-- JavaScript Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>
    {% block js %}{% endblock %}
  </body>
</html>
```

Le fichier `_base.html` est le fichier HTML parent qui sera hérité par les autres templates. Nous avons ajouté le support de Bootstrap 5 dans le fichier ci-dessus. Nous utilisons également les messages Flash de Flask pour afficher des alertes Bootstrap dans l'application.

Créons également un fichier `navigation.html` qui contient la barre de navigation de l'application :

```html
<!-- Navigation -->
<header class="p-3 text-bg-dark">
  <div class="container">
    <div class="d-flex flex-wrap align-items-center justify-content-center justify-content-lg-start">
      <ul class="nav col-12 col-lg-auto me-lg-auto mb-2 justify-content-center mb-md-0">
        <li><a href="{{ url_for('core.home') }}" class="nav-link px-2 text-secondary">Accueil</a></li>
      </ul>

      <div class="text-end">
        {% if current_user.is_authenticated %}
        <a href="{{ url_for('accounts.logout') }}"><button type="button" class="btn btn-danger me-2">Déconnexion</button></a>
        {% else %}
          <a href="{{ url_for('accounts.login') }}"><button type="button" class="btn btn-outline-light me-2">Connexion</button></a>
          <a href="{{ url_for('accounts.register') }}"><button type="button" class="btn btn-success">S'inscrire</button></a>
        {% endif %}
          
      </div>
    </div>
  </div>
</header>
```

Notez que nous n'avons pas encore créé les vues utilisées ci-dessus.

## Comment créer la page d'accueil

Dans cette section, vous allez d'abord créer une fonction de vue pour la page d'accueil à l'intérieur du fichier `core/views.py`. Ajoutez le code suivant :

```python
from flask import Blueprint, render_template
from flask_login import login_required

core_bp = Blueprint("core", __name__)


@core_bp.route("/")
@login_required
def home():
    return render_template("core/index.html")

```

Remarquez que nous avons utilisé le blueprint pour ajouter la route. Nous avons également ajouté un middleware `@login_required` pour empêcher l'accès des utilisateurs non authentifiés.

Ensuite, créons un fichier `index.html` à l'intérieur du dossier `templates/core`, et ajoutons le code suivant :

```html
{% extends "_base.html" %}
{% block content %}

<h1 class="text-center">Bienvenue {{current_user.email}} !</h1>

{% endblock %}
```

La page HTML aura simplement un message de bienvenue pour les utilisateurs authentifiés.

## Comment implémenter l'inscription des utilisateurs

Tout d'abord, nous allons créer un formulaire d'inscription en utilisant Flask-WTF. Créez un fichier `forms.py` à l'intérieur du package `accounts` et ajoutez le code suivant :

```python
from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo, Length

from src.accounts.models import User


class RegisterForm(FlaskForm):
    email = EmailField(
        "Email", validators=[DataRequired(), Email(message=None), Length(min=6, max=40)]
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

    def validate(self):
        initial_validation = super(RegisterForm, self).validate()
        if not initial_validation:
            return False
        user = User.query.filter_by(email=self.email.data).first()
        if user:
            self.email.errors.append("Email déjà enregistré")
            return False
        if self.password.data != self.confirm.data:
            self.password.errors.append("Les mots de passe doivent correspondre")
            return False
        return True

```

Le `RegisterForm` étend la classe `FlaskForm` et contient trois champs – `email`, `password` et `confirm`. Nous avons ajouté différents validateurs tels que `DataRequired`, `Length`, `Email` et `EqualTo` aux champs respectifs.

Nous avons également défini une méthode `validate()` qui est automatiquement appelée lorsque le formulaire est soumis.

À l'intérieur de la méthode, nous effectuons d'abord la validation initiale fournie par FlaskForm. Si celle-ci est réussie, nous effectuons notre validation personnalisée telle que la vérification si l'utilisateur est déjà enregistré et la correspondance du mot de passe avec le mot de passe confirmé. Si des erreurs surviennent, nous ajoutons le message d'erreur dans les champs respectifs.

Utilisons ce formulaire dans le fichier `views.py` pour créer une fonction de gestion du processus d'inscription.

```python
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_user

from src import db
from src.accounts.models import User

from .forms import RegisterForm


@accounts_bp.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        flash("Vous êtes déjà inscrit.", "info")
        return redirect(url_for("core.home"))
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        user = User(email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()

        login_user(user)
        flash("Vous êtes inscrit et maintenant connecté. Bienvenue !", "success")

        return redirect(url_for("core.home"))

    return render_template("accounts/register.html", form=form)
```

Dans la fonction ci-dessus, notez que nous utilisons le blueprint pour ajouter la route de la fonction. Initialement, nous vérifions si un utilisateur est déjà authentifié en utilisant la propriété `is_authenticated`. Si c'est le cas, nous le redirigeons vers la page d'accueil avec un message.

Si aucun utilisateur n'est authentifié, nous créons d'abord une instance de la classe `RegisterForm`. Si la méthode de requête est GET, nous rendons un fichier HTML avec le formulaire. Sinon, nous vérifions si le formulaire a des entrées valides en utilisant la méthode `validate_on_submit()`.

Si les entrées sont valides, nous créons une instance de la classe `User` avec l'email et le mot de passe fournis par l'utilisateur, et nous l'ajoutons à la base de données.

Ensuite, nous connectons l'utilisateur en utilisant la méthode `login_user()` qui accepte l'objet `user`. Nous affichons également un message de succès et redirigeons l'utilisateur vers la page d'accueil.

Maintenant, utilisons ce formulaire à l'intérieur du fichier HTML. Créez un répertoire `accounts` à l'intérieur du dossier `templates` et ajoutez un nouveau fichier appelé `register.html` à l'intérieur. Ajoutez le code suivant :

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
          {{ form.email(placeholder="email", class="form-control mb-2") }}
          {{ form.email.label }}
            {% if form.email.errors %}
              {% for error in form.email.errors %}
                <div class="alert alert-danger" role="alert">
                  {{ error }}
                </div>
              {% endfor %}
            {% endif %}
        </div>
        <div class="form-floating">
          {{ form.password(placeholder="mot de passe", class="form-control mb-2") }}
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

Dans le code ci-dessus, nous avons créé un formulaire HTML où nous utilisons l'instance `form` qui contient les champs de formulaire avec leurs libellés et erreurs. Nous avons utilisé une fonction de vue `accounts.login` qui n'existe pas encore.

## Comment implémenter la connexion et la déconnexion des utilisateurs

Tout d'abord, créons un formulaire de connexion dans le fichier `accounts/forms.py` :

```python
class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Mot de passe", validators=[DataRequired()])
```

Le formulaire est similaire au formulaire d'inscription mais il n'a que deux champs – `email` et `password`.

Ensuite, créons une fonction de vue pour gérer le processus de connexion à l'intérieur du fichier `accounts/views.py` :

```python
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_user

from src import bcrypt, db
from src.accounts.models import User

from .forms import LoginForm, RegisterForm


@accounts_bp.route("/login", methods=["GET", "POST"])
def login():
	if current_user.is_authenticated:
        flash("Vous êtes déjà connecté.", "info")
        return redirect(url_for("core.home"))
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, request.form["password"]):
            login_user(user)
            return redirect(url_for("core.home"))
        else:
            flash("Email et/ou mot de passe invalide.", "danger")
            return render_template("accounts/login.html", form=form)
    return render_template("accounts/login.html", form=form)

```

Similaire à la fonction de vue d'inscription, nous vérifions d'abord si un utilisateur est déjà authentifié en utilisant la propriété `is_authenticated`. Si c'est le cas, nous le redirigeons vers la page d'accueil avec un message.

Si l'utilisateur n'est pas authentifié, nous créons une instance du formulaire de connexion. Si la méthode de requête est GET, nous rendons simplement un fichier `login.html` avec le formulaire. Sinon, le formulaire est validé.

Lors de la validation, nous utilisons la méthode `check_password_hash` de la bibliothèque `Flask-Bcrypt` pour faire correspondre les mots de passe hachés. Si les mots de passe correspondent, nous connectons l'utilisateur en utilisant la méthode `login_user()` et redirigeons vers la page d'accueil. Sinon, nous affichons un message d'erreur et rendons la même page HTML.

Maintenant, créons un fichier `login.html` à l'intérieur du dossier `templates/accounts` :

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
          {{ form.email(placeholder="email", class="form-control mb-2") }}
          {{ form.email.label }}
            {% if form.email.errors %}
              {% for error in form.email.errors %}
              <div class="alert alert-danger" role="alert">
                {{ error }}
              </div>
              {% endfor %}
            {% endif %}
        </div>
        <div class="form-floating">
          {{ form.password(placeholder="mot de passe", class="form-control mb-2") }}
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
        <p class="text-center mt-3">Nouvel utilisateur ? <a href="{{ url_for('accounts.register') }}">Inscription maintenant</a></p>
      </form>
    </main>
  </div>
  <div class="col-md-4"></div>
</div>

{% endblock %}
```

Le formulaire de connexion est similaire au formulaire d'inscription mais avec seulement deux champs pour l'email et le mot de passe.

La déconnexion de l'utilisateur est un processus très simple. Vous devez simplement créer une fonction de vue pour cela à l'intérieur du fichier `accounts/views.py` :

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

## Comment exécuter l'application complète pour la première fois

Maintenant que votre application est prête (sans les tests), vous pouvez d'abord migrer la base de données, puis exécuter l'application.

* Pour initialiser la base de données (créer un dépôt de migration), utilisez la commande :

```bash
flask db init
```

* Pour migrer les modifications de la base de données, utilisez la commande :

```bash
flask db migrate
```

* Pour appliquer les migrations, utilisez la commande :

```bash
flask db upgrade
```

Puisque c'est la première fois que nous exécutons notre application, vous devrez exécuter toutes les commandes ci-dessus. Plus tard, chaque fois que vous apporterez des modifications à la base de données, vous devrez simplement exécuter les deux dernières commandes.

Après cela, vous pouvez exécuter votre application en utilisant la commande :

```
python manage.py run
```

## Comment ajouter des tests unitaires à l'application

Maintenant que nous avons toutes les fonctionnalités prêtes, créons un dossier `tests` dans le répertoire racine et convertissons-le en un package en ajoutant un fichier `__init__.py` vide.

### Comment créer un cas de test de base

Créons un cas de test de base qui sera étendu par les autres cas de test. Créez un fichier `base_test.py` à l'intérieur du package `tests`, et ajoutez le code suivant :

```python
import os

from flask_testing import TestCase

from src import app, db
from src.accounts.models import User


class BaseTestCase(TestCase):
    def create_app(self):
        app.config.from_object("config.TestingConfig")
        return app

    def setUp(self):
        db.create_all()
        user = User(email="ad@min.com", password="admin_user")
        db.session.add(user)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        testdb_path = os.path.join("src", "testdb.sqlite")
        os.remove(testdb_path)

```

La classe `BaseTestCase` étend la classe `TestCase` et implémente les trois méthodes suivantes :

* La méthode `create_app()` est une méthode requise qui doit retourner une instance Flask. Si vous ne définissez pas `create_app()`, une `NotImplementedError` sera levée. Remarquez que nous utilisons `TestingConfig` dans ce cas.
* La méthode `setUp()` est appelée avant l'exécution de tout test. Dans cette méthode, nous créons toutes les tables de la base de données. De plus, nous créons également un utilisateur afin de pouvoir l'utiliser plus tard.
* La méthode `tearDown()` est appelée après l'exécution de tous les cas de test. Donc, dans cette méthode, nous nettoierons toutes les données de test.

### Comment écrire des tests pour les formulaires

Dans les sections ci-dessus, nous avons créé deux formulaires – `RegisterForm` et `LoginForm`. Testons ces formulaires dans un nouveau fichier de test nommé `test_forms.py` à l'intérieur du package `tests`.

```python
import unittest

from base_test import BaseTestCase

from src.accounts.forms import LoginForm, RegisterForm


class TestRegisterForm(BaseTestCase):
    def test_validate_success_register_form(self):
        # Assurez-vous que les données correctes sont validées.
        form = RegisterForm(email="new@test.com", password="example", confirm="example")
        self.assertTrue(form.validate())

    def test_validate_invalid_password_format(self):
        # Assurez-vous que les données incorrectes ne sont pas validées.
        form = RegisterForm(email="new@test.com", password="example", confirm="")
        self.assertFalse(form.validate())

    def test_validate_email_already_registered(self):
        # Assurez-vous que l'utilisateur ne peut pas s'inscrire lorsqu'un email dupliqué est utilisé
        form = RegisterForm(
            email="ad@min.com", password="admin_user", confirm="admin_user"
        )
        self.assertFalse(form.validate())


class TestLoginForm(BaseTestCase):
    def test_validate_success_login_form(self):
        # Assurez-vous que les données correctes sont validées.
        form = LoginForm(email="ad@min.com", password="admin_user")
        self.assertTrue(form.validate())

    def test_validate_invalid_email_format(self):
        # Assurez-vous que le format d'email invalide génère une erreur.
        form = LoginForm(email="unknown", password="example")
        self.assertFalse(form.validate())


if __name__ == "__main__":
    unittest.main()

```

La classe `TestRegisterForm` définit trois méthodes de test pour tester la méthode `validate` de la classe `RegisterForm`.

La première méthode de test vérifie que le formulaire valide avec des données d'entrée correctes. La deuxième méthode de test vérifie que le formulaire ne valide pas avec un format de mot de passe invalide. Et la troisième méthode de test vérifie que le formulaire ne valide pas lorsqu'un email dupliqué est utilisé pour l'inscription.

La classe `TestLoginForm` définit deux méthodes de test pour tester la méthode `validate` de la classe `LoginForm`. La première méthode de test vérifie que le formulaire valide avec des données d'entrée correctes, et la deuxième méthode de test vérifie que le formulaire ne valide pas avec un format d'email invalide.

### Comment tester le modèle d'utilisateur

Testons maintenant le modèle `User` dans un nouveau fichier nommé `test_models.py` à l'intérieur du package `tests`.

```py
import datetime
import unittest

from base_test import BaseTestCase
from flask_login import current_user

from src import bcrypt
from src.accounts.models import User


class TestUser(BaseTestCase):
    def test_user_registration(self):
        # Assurez-vous que l'inscription de l'utilisateur se comporte correctement.
        with self.client:
            self.client.get("/logout", follow_redirects=True)
            self.client.post(
                "/register",
                data=dict(
                    email="test@user.com", password="test_user", confirm="test_user"
                ),
                follow_redirects=True,
            )
            user = User.query.filter_by(email="test@user.com").first()
            self.assertTrue(user.id)
            self.assertTrue(user.email == "test@user.com")
            self.assertFalse(user.is_admin)

    def test_get_by_id(self):
        # Assurez-vous que l'id est correct pour l'utilisateur actuel/connecté
        with self.client:
            self.client.get("/logout", follow_redirects=True)
            self.client.post(
                "/login",
                data=dict(email="ad@min.com", password="admin_user"),
                follow_redirects=True,
            )
            self.assertTrue(current_user.id == 1)

    def test_created_on_defaults_to_datetime(self):
        # Assurez-vous que registered_on est un datetime
        with self.client:
            self.client.get("/logout", follow_redirects=True)
            self.client.post(
                "/login",
                data=dict(email="ad@min.com", password="admin_user"),
                follow_redirects=True,
            )
            user = User.query.filter_by(email="ad@min.com").first()
            self.assertIsInstance(user.created_on, datetime.datetime)

    def test_check_password(self):
        # Assurez-vous que le mot de passe donné est correct après le déhashage
        user = User.query.filter_by(email="ad@min.com").first()
        self.assertTrue(bcrypt.check_password_hash(user.password, "admin_user"))
        self.assertFalse(bcrypt.check_password_hash(user.password, "foobar"))

    def test_validate_invalid_password(self):
        # Assurez-vous que l'utilisateur ne peut pas se connecter lorsque le mot de passe est incorrect
        with self.client:
            self.client.get("/logout", follow_redirects=True)
            response = self.client.post(
                "/login",
                data=dict(email="ad@min.com", password="foo_bar"),
                follow_redirects=True,
            )
        self.assertIn(b"Email et/ou mot de passe invalide.", response.data)


if __name__ == "__main__":
    unittest.main()
```

La classe `TestUser` définit quatre méthodes de test pour tester divers aspects de la classe de modèle `User`.

* La première méthode de test teste le processus d'inscription de l'utilisateur en postant une demande d'inscription au serveur avec l'objet `client`, qui est un client de test Flask. Le test vérifie qu'un nouvel utilisateur est correctement ajouté à la base de données et que les attributs de l'utilisateur sont correctement définis.
* La deuxième méthode de test teste la méthode `get_by_id`, qui est une méthode d'assistance pour obtenir l'objet utilisateur de la base de données par son id. Le test connecte un utilisateur et vérifie que l'id de l'utilisateur actuel est correct.
* La troisième méthode de test vérifie que l'attribut `created_on` de l'objet utilisateur est un objet datetime.
* La quatrième méthode de test teste la méthode `check_password`, qui est une méthode d'assistance pour vérifier le mot de passe de l'utilisateur. Le test vérifie que la méthode vérifie correctement un mot de passe correct et un mot de passe incorrect.
* La cinquième méthode de test teste le processus de connexion en postant une demande de connexion au serveur avec l'objet `client` et vérifie que le serveur répond avec un message d'erreur lorsque le mot de passe est incorrect.

### Comment tester les routes

Testons maintenant les routes dans un nouveau fichier nommé `test_routes.py` à l'intérieur du package `tests`.

```python
import unittest

from base_test import BaseTestCase
from flask_login import current_user


class TestPublic(BaseTestCase):
    def test_main_route_requires_login(self):
        # Assurez-vous que la route principale nécessite un utilisateur connecté.
        response = self.client.get("/", follow_redirects=True)
        self.assertTrue(response.status_code == 200)
        self.assertIn(b"Veuillez vous connecter pour accéder à cette page", response.data)

    def test_logout_route_requires_login(self):
        # Assurez-vous que la route de déconnexion nécessite un utilisateur connecté.
        response = self.client.get("/logout", follow_redirects=True)
        self.assertIn(b"Veuillez vous connecter pour accéder à cette page", response.data)


class TestLoggingInOut(BaseTestCase):
    def test_correct_login(self):
        # Assurez-vous que la connexion se comporte correctement avec des identifiants corrects
        with self.client:
            response = self.client.post(
                "/login",
                data=dict(email="ad@min.com", password="admin_user"),
                follow_redirects=True,
            )
            self.assertTrue(current_user.email == "ad@min.com")
            self.assertTrue(current_user.is_active)
            self.assertTrue(response.status_code == 200)

    def test_logout_behaves_correctly(self):
        # Assurez-vous que la déconnexion se comporte correctement, concernant la session
        with self.client:
            self.client.post(
                "/login",
                data=dict(email="ad@min.com", password="admin_user"),
                follow_redirects=True,
            )
            response = self.client.get("/logout", follow_redirects=True)
            self.assertIn(b"Vous avez été déconnecté.", response.data)
            self.assertFalse(current_user.is_active)


if __name__ == "__main__":
    unittest.main()

```

La classe `TestPublic` définit deux méthodes de test pour tester le contrôle d'accès de certaines routes.

La première méthode de test vérifie que la route principale nécessite un utilisateur connecté en tentant d'y accéder avec l'objet `client`, qui est un client de test Flask. Le test vérifie que le serveur répond avec une invite de connexion. La deuxième méthode de test vérifie que la route de déconnexion nécessite également un utilisateur connecté.

La classe `TestLoggingInOut` définit deux méthodes de test pour tester les fonctionnalités de connexion et de déconnexion.

La première méthode de test vérifie le processus de connexion en postant une demande de connexion au serveur avec l'objet `client` et vérifie que le serveur répond avec une connexion réussie. La deuxième méthode de test vérifie le processus de déconnexion en postant une demande de déconnexion au serveur avec l'objet `client`. Elle vérifie ensuite que le serveur répond avec un message de déconnexion et que l'utilisateur n'est plus connecté.

### Comment exécuter les tests

Maintenant que nous avons tous les tests prêts, nous sommes prêts à exécuter les cas de test. Mais avant cela, comme mentionné au début, nous devrons ajouter une commande dans le fichier `manage.py` pour exécuter les tests.

```python
import unittest


@cli.command("test")
def test():
    """Exécute les tests unitaires sans couverture."""
    tests = unittest.TestLoader().discover("tests")
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    else:
        return 1
```

La commande exécute les tests unitaires dans le package `tests` et affiche les résultats dans le terminal.

Vous utilisez la méthode `unittest.TestLoader().discover()` pour découvrir et exécuter tous les tests unitaires dans le package `tests`. Vous utilisez la méthode `unittest.TextTestRunner()` pour exécuter les tests unitaires et imprimer les résultats dans le terminal. L'argument `verbosity` contrôle le niveau de détail dans la sortie.

Si tous les tests unitaires réussissent, la commande `test` retourne un code de sortie de 0. Si l'un des tests unitaires échoue, la commande retourne un code de sortie de 1.

Maintenant, vous pouvez exécuter tous les tests en utilisant la commande :

```bash
python manage.py test
```

Cela donnera la sortie suivante :

```bash
test_validate_invalid_email_format (test_forms.TestLoginForm) ... ok
test_validate_success_login_form (test_forms.TestLoginForm) ... ok
test_validate_email_already_registered (test_forms.TestRegisterForm) ... ok
test_validate_invalid_password_format (test_forms.TestRegisterForm) ... ok
test_validate_success_register_form (test_forms.TestRegisterForm) ... ok
test_check_password (test_models.TestUser) ... ok
test_created_on_defaults_to_datetime (test_models.TestUser) ... ok
test_get_by_id (test_models.TestUser) ... ok
test_user_registration (test_models.TestUser) ... ok
test_validate_invalid_password (test_models.TestUser) ... ok
test_correct_login (test_routes.TestLoggingInOut) ... ok
test_logout_behaves_correctly (test_routes.TestLoggingInOut) ... ok
test_logout_route_requires_login (test_routes.TestPublic) ... ok
test_main_route_requires_login (test_routes.TestPublic) ... ok

----------------------------------------------------------------------
Ran 14 tests in 19.577s

OK
```

## Fonctionnalités à ajouter à votre application

Voici quelques éléments supplémentaires que vous pouvez ajouter à votre application. Notez que ceux-ci sont optionnels.

### Comment créer un administrateur

Similaire à la commande `test`, vous pouvez ajouter une commande `create_admin` pour créer un administrateur dans votre application. Ajoutez le code suivant à l'intérieur du fichier `manage.py` :

```python
import getpass


@cli.command("create_admin")
def create_admin():
    """Crée l'utilisateur administrateur."""
    email = input("Entrez l'adresse email : ")
    password = getpass.getpass("Entrez le mot de passe : ")
    confirm_password = getpass.getpass("Entrez le mot de passe à nouveau : ")
    if password != confirm_password:
        print("Les mots de passe ne correspondent pas")
        return 1
    try:
        user = User(email=email, password=password, is_admin=True)
        db.session.add(user)
        db.session.commit()
    except Exception:
        print("Impossible de créer l'utilisateur administrateur.")
```

La commande invite l'utilisateur à entrer une adresse email et un mot de passe pour l'utilisateur administrateur. Le mot de passe est saisi en utilisant le module `getpass`, qui masque la saisie du mot de passe dans le terminal. La commande vérifie ensuite si le mot de passe saisi et le mot de passe confirmé correspondent. Si les mots de passe ne correspondent pas, la commande imprime un message d'erreur et retourne un code de sortie de 1.

Si les mots de passe correspondent, la commande crée un nouvel objet `User` avec l'adresse email saisie, le mot de passe et l'attribut `is_admin` défini sur `True`. La commande ajoute ensuite l'objet utilisateur à la session de la base de données et valide les modifications dans la base de données. Si une exception est levée pendant ce processus, la commande imprime un message d'erreur.

Vous pouvez exécuter la commande suivante pour en créer un :

```bash
python manage.py create_admin
```

Sortie :

```bash
> python manage.py create_admin
Entrez l'adresse email : admin@myapp.com
Entrez le mot de passe : 
Entrez le mot de passe à nouveau : 
Admin avec l'email admin@myapp.com créé avec succès !
```

### Comment créer des pages d'erreur

Notre application peut rencontrer des erreurs à tout moment. Les erreurs les plus courantes que nous rencontrons sont Non autorisé (401), Non trouvé (404) et Erreur de serveur (500).

Créons un répertoire `errors` à l'intérieur du répertoire `templates` et créons trois pages HTML comme suit :

* 401.html

```html
{% extends "_base.html" %}
{% block content %}
<h1>401</h1>
<p>Allez-vous en !</p>
<p><em>Retourner à <a href="{{url_for('core.home')}}">Accueil</a> ?</em></p>
{% endblock %}

```

* 404.html

```html
{% extends "_base.html" %}
{% block content %}
<h1>404</h1>
<p>Il n'y a rien ici !</p>
<p><em>Retourner à <a href="{{url_for('core.home')}}">Accueil</a> ?</em></p>
{% endblock %}

```

* 500.html

```html
{% extends "_base.html" %}
{% block content %}
<h1>500</h1>
<p>Quelque chose ne va pas ! Nous sommes sur le coup.</p>
<p><em>Retourner à <a href="{{url_for('core.home')}}">Accueil</a> ?</em></p>
{% endblock %}

```

Ensuite, nous devons ajouter des gestionnaires d'erreurs pour ces erreurs. Ouvrez le fichier `src/__init__.py` et ajoutez le code suivant en bas du fichier :

```python
@app.errorhandler(401)
def unauthorized_page(error):
    return render_template("errors/401.html"), 401


@app.errorhandler(404)
def page_not_found(error):
    return render_template("errors/404.html"), 404


@app.errorhandler(500)
def server_error_page(error):
    return render_template("errors/500.html"), 500

```

Ce fragment de code ci-dessus enregistre des fonctions de gestion des erreurs pour les codes d'erreur HTTP 401, 404 et 500 dans une application Flask. Une fonction de gestion des erreurs est une fonction qui est appelée lorsqu'une erreur se produit dans l'application.

Les fonctions de gestion des erreurs sont décorées avec le décorateur `@app.errorhandler`, qui les enregistre avec l'application Flask. Le décorateur prend un code d'erreur comme argument, et la fonction est appelée lorsque le code d'erreur est levé.

Chaque fonction de gestion des erreurs retourne un template rendu et le code d'erreur comme réponse au client. Les templates sont des fichiers HTML situés dans le dossier `errors` et contiennent le contenu à afficher à l'utilisateur pour chaque erreur. Le code d'erreur est passé comme argument à la fonction `render_template` pour déterminer quel template rendre.

## Conclusion

Dans ce tutoriel, vous avez appris comment configurer une authentification de base des utilisateurs dans votre application Flask. Vous avez également écrit quelques cas de test afin de tester les fonctionnalités.

Voici le lien vers le [dépôt GitHub](https://github.com/ashutoshkrris/Flask-User-Authentication). N'hésitez pas à le consulter chaque fois que vous êtes bloqué.

### Étapes suivantes recommandées

* Vous pouvez ajouter plus de sécurité telle que la vérification par email, ou l'authentification basée sur des jetons dans l'application.
* Vous pouvez ajouter une fonctionnalité "mot de passe oublié" dans l'application.
* Vous pouvez ajouter plus de cas de test afin de tester l'application plus en profondeur.

Merci d'avoir lu. J'espère que vous avez trouvé cet article utile. Vous pouvez me suivre sur [Twitter](https://twitter.com/ashutoshkrris).