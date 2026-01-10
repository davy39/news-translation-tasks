---
title: Tutoriel Python – Comment créer un raccourcisseur d'URL avec Flask
subtitle: ''
author: Ashutosh Krishna
co_authors: []
series: null
date: '2022-01-03T18:26:36.000Z'
originalURL: https://freecodecamp.org/news/python-tutorial-how-to-create-a-url-shortener-using-flask
coverImage: https://www.freecodecamp.org/news/content/images/2021/12/URL-Shortener.png
tags:
- name: Flask Framework
  slug: flask
- name: projects
  slug: projects
- name: Python
  slug: python
seo_title: Tutoriel Python – Comment créer un raccourcisseur d'URL avec Flask
seo_desc: "In this tutorial, we will build a URL shortener using Flask. This tool\
  \ takes any URL and generates a shorter, more readable version like bit.ly. \nThe\
  \ application will allow users to enter a URL and an optional custom short id and\
  \ generate a shorter v..."
---

Dans ce tutoriel, nous allons créer un raccourcisseur d'URL en utilisant Flask. Cet outil prend n'importe quelle URL et génère une version plus courte et plus lisible comme [bit.ly](https://bitly.com/). 

L'application permettra aux utilisateurs de saisir une URL et un identifiant court personnalisé optionnel, puis de générer une version plus courte.

Voici ce que nous allons construire :

%[https://www.youtube.com/watch?v=g6chXThUReU]

L'interface de l'application n'est pas attrayante, car l'objectif principal du projet est de construire un projet backend. 

Quelques exemples d'URLs raccourcies sont [https://shorty-flask.herokuapp.com/mzkpK8sw](https://shorty-flask.herokuapp.com/mzkpK8sw) et [https://shorty-flask.herokuapp.com/linkify](https://shorty-flask.herokuapp.com/linkify).

## Créer l'environnement virtuel et installer les dépendances

Dans ce tutoriel, nous allons utiliser Pipenv pour gérer notre environnement virtuel.

[Pipenv](https://pypi.org/project/pipenv/) est un outil qui crée et gère automatiquement un virtualenv pour vos projets, ainsi qu'ajoute/supprime des packages de votre `Pipfile` lorsque vous installez/désinstallez des packages. Il génère également le très important `Pipfile.lock`, qui est utilisé pour produire des builds déterministes. 

Vous pouvez lire [cet article](https://medium.com/analytics-vidhya/why-pipenv-over-venv-for-python-projects-a51fb6e4f31e) pour en savoir plus.

Pipenv est une bibliothèque externe et nous devons l'installer explicitement. Pour installer la bibliothèque, utilisez la commande pip :

```bash
pip install pipenv
```

Une fois installé, nous pouvons créer un environnement virtuel et l'activer avec cette commande :

```bash
pipenv shell
```

Pour désactiver l'environnement virtuel, nous avons une commande simple :

```bash
exit
```

Une fois que vous avez créé et activé l'environnement virtuel, vous êtes prêt à installer les bibliothèques requises.

* [Flask](https://flask.palletsprojects.com/en/2.0.x/) est un microframework simple et facile à utiliser pour Python qui peut aider à construire des applications web scalables et sécurisées. Le module n'est pas préinstallé avec Python, nous devons donc l'installer avec la commande :
    ```bash
    pipenv install Flask
    ```
    
* [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/) est une extension qui gère les migrations de base de données SQLAlchemy pour les applications Flask en utilisant Alembic. Les opérations de base de données sont disponibles via l'interface de ligne de commande Flask. Pour installer le module, utilisez la commande :
    ```bash
    pipenv install Flask-Migrate
    ```
    
* [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) est une extension pour Flask qui ajoute le support de SQLAlchemy à votre application. Elle vous aide à simplifier les choses en utilisant SQLAlchemy avec Flask en vous donnant des valeurs par défaut utiles et des aides supplémentaires qui facilitent l'exécution des tâches courantes. Pour installer le module, utilisez la commande :
    ```bash
    pipenv install Flask-SQLAlchemy
    ```
    
* [Psycopg2](https://pypi.org/project/psycopg2/) est l'adaptateur de base de données PostgreSQL le plus populaire pour le langage de programmation Python. Pour installer le module, utilisez la commande :
    ```bash
    pipenv install psycopg2
    ```
    
* [Gunicorn](https://gunicorn.org/) est un serveur HTTP WSGI Python pour UNIX. Pour installer le module, utilisez la commande :
    ```bash
    pipenv install gunicorn
    ```
    
* [Python Decouple](https://pypi.org/project/python-decouple/) : Nous allons également utiliser des [variables d'environnement](https://iread.ga/posts/49/do-you-really-need-environment-variables-in-python) dans ce projet. Nous allons donc installer un autre module appelé python-decouple pour gérer cela :
    ```bash
    pipenv install python-decouple
    ```

## Comment configurer le projet Flask

La première chose que nous allons faire est de créer un projet Flask. Si vous consultez la [documentation officielle](https://flask.palletsprojects.com/en/2.0.x/quickstart/) de Flask, vous y trouverez une [application minimale](https://flask.palletsprojects.com/en/2.0.x/quickstart/#a-minimal-application).

Mais nous ne allons pas suivre cela. Nous allons écrire une application plus extensible et avec une bonne structure de base. Si vous le souhaitez, vous pouvez suivre [ce guide](https://iread.ga/posts/54/getting-started-with-flask) pour commencer avec Flask.

Notre application existera dans un package appelé **core**. Pour convertir un répertoire habituel en un package Python, nous devons simplement inclure un fichier `__init__.py`. Alors, créons d'abord notre package core.

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


DATABASE_URI = config("DATABASE_URL")
if DATABASE_URI.startswith("postgres://"):
    DATABASE_URI = DATABASE_URI.replace("postgres://", "postgresql://", 1)


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = config('SECRET_KEY', default='guess-me')
    SQLALCHEMY_DATABASE_URI = DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
```

Dans le script ci-dessus, nous avons créé une classe `Config` et défini divers attributs à l'intérieur. Nous avons également créé différentes classes enfants (selon les différentes étapes du développement) qui héritent de la classe `Config`.

Remarquez que nous utilisons quelques variables d'environnement comme **SECRET_KEY** et **DATABASE_URL**. Créez un fichier nommé `.env` dans le répertoire racine et ajoutez le contenu suivant :

```
SECRET_KEY=verysecretkey
DATABASE_URL=sqlite:///shorty.db
APP_SETTINGS=config.DevelopmentConfig
FLASK_APP=core
```

En plus de **SECRET_KEY** et **DATABASE_URL**, nous avons également spécifié **APP_SETTINGS** et **FLASK_APP**. 

**APP_SETTINGS** fait référence à l'une des classes que nous avons créées dans le fichier `config.py`. Nous le définissons à l'étape actuelle du projet. La valeur de **FLASK_APP** est le nom du package que nous avons créé.

Maintenant, nous pouvons ajouter le contenu suivant dans le fichier `core/__init__.py` :

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from decouple import config

app = Flask(__name__)
app.config.from_object(config("APP_SETTINGS"))

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from core import routes
```

Dans le script Python ci-dessus, nous importons d'abord la classe Flask du module Flask que nous avons installé. Ensuite, nous créons un objet `app` de la classe Flask. Nous utilisons l'argument `__name__` pour indiquer le module ou le package de l'application, afin que Flask sache où trouver d'autres fichiers tels que les templates.

Ensuite, nous définissons les configurations de l'application selon **APP_SETTINGS** conformément à la variable dans le fichier `.env`. Pour utiliser Flask-SQLAlchemy et Flask-Migrate dans notre application, nous devons simplement créer des objets des classes `SQLAlchemy` et `Migrate` des bibliothèques `flask_sqlalchemy` et `flask_migrate` respectivement.

L'application importe ensuite le module `routes`, qui n'existe pas encore.

Pour exécuter l'application, nous allons utiliser un fichier `main.py` avec le contenu suivant :

```python
from core import app

if __name__ == '__main__':
    app.run()
```

## Comment créer la table de la base de données

Pour définir nos tables de base de données, nous allons créer un fichier `models.py` dans le package core. À l'intérieur, nous pouvons écrire le code suivant :

```python
from core import db
from datetime import datetime

class ShortUrls(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(500), nullable=False)
    short_id = db.Column(db.String(20), nullable=False, unique=True)
    created_at = db.Column(db.DateTime(), default=datetime.now(), nullable=False)
```

Nous avons d'abord importé l'objet `db` que nous avions initialisé dans le fichier `__init__.py`. Ensuite, nous avons créé une classe `ShortUrls` avec quelques champs tels que **id** (clé primaire), **original_url** (fournie par l'utilisateur), **short_id** (générée par nous ou fournie par l'utilisateur), et **created_at** (horodatage).

Nous pouvons ensuite utiliser les commandes **Flask-Migrate** pour migrer la base de données avec les nouvelles tables. Les commandes que nous allons utiliser sont :

* `flask db init`

 pour initialiser la base de données au début (à utiliser une seule fois)
* `flask db migrate`

 pour migrer les nouvelles modifications vers la base de données (à utiliser chaque fois que nous apportons des modifications aux tables de la base de données)
* `flask db upgrade`

 pour mettre à niveau notre base de données avec les nouvelles modifications (à utiliser avec la commande migrate)

Après avoir exécuté l'initialisation de la base de données, nous verrons un nouveau dossier appelé "**migrations**" dans le projet. Cela contient la configuration nécessaire pour qu'Alembic exécute les migrations contre le projet. 

À l'intérieur de "migrations", nous verrons qu'il contient un dossier appelé "versions", qui contiendra les scripts de migration au fur et à mesure de leur création.

# **Comment créer la page d'accueil pour raccourcir les URLs**

Dans cette étape, nous allons créer une route Flask pour la page d'index, qui permettra aux utilisateurs de saisir une URL que nous enregistrerons ensuite dans la base de données. Cette route utilisera l'identifiant court personnalisé fourni par l'utilisateur ou en générera un elle-même, construira l'URL courte, puis la rendra comme résultat.

Tout d'abord, créons un fichier `routes.py` dans le package core et créons une fonction Python pour générer un identifiant court.

```python
from random import choice
import string

def generate_short_id(num_of_chars: int):
    """Fonction pour générer un short_id avec un nombre spécifié de caractères"""
    return ''.join(choice(string.ascii_letters+string.digits) for _ in range(num_of_chars))
```

Pour générer un identifiant court, nous avons utilisé la méthode **choice** du module **random** de Python. Nous avons également utilisé le module **string** intégré de Python pour les lettres (minuscules + majuscules) et les chiffres.

Maintenant, nous devons créer un template pour la page d'index qui sera servie par la route d'index. Ce template aura un formulaire simple où un utilisateur peut entrer l'URL originale et un identifiant court personnalisé (optionnel) et le soumettre. 

Mais nous ne allons pas créer `index.html` directement. Nous pouvons utiliser le concept d'héritage de template dans Jinja2. Alors, créons un répertoire **templates** dans le package `core` et créons un fichier `base.html` à l'intérieur. Vous pouvez coller le code HTML dans ce fichier.

```html
<!doctype html>
<html lang="en">
  <head>
    <!-- Balises meta requises -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- CSS Bootstrap -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KyZXEAg3QhqLMpG8r+8fhAXLRk2vvoC2f3B09zVXn8CA5QIVfZOJ3BCsw2P0p/We" crossorigin="anonymous">

    <title>{% block title %} {% endblock %}</title>
  </head>
  <body>
    <div class="container mt-3">
        {% for message in get_flashed_messages() %}
            <div class="alert alert-danger">{{ message }}</div>
        {% endfor %}
        {% block content %} {% endblock %}
    </div>

    <!-- JavaScript optionnel -->
    <!-- jQuery d'abord, puis Popper.js, puis Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.3/dist/umd/popper.min.js" integrity="sha384-eMNCOe7tC1doHpGoWe/6oMVemdAVTMs2xqW4mwXrXsW0L84Iytr2wi5v2QjrP/xp" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/js/bootstrap.min.js" integrity="sha384-cn7l7gDp0eyniUwwAZgrzD06kc/tftFf19TOAs2zVinnD/C7E91j9yyk5//jjpt/" crossorigin="anonymous"></script>
  </body>
</html>
```

Notez que, pour le style, nous utilisons [Bootstrap](https://getbootstrap.com/) ici.

La plupart du code dans le bloc précédent est du code HTML standard requis pour Bootstrap. Les balises `<meta>` fournissent des informations pour le navigateur web, la balise `<link>` lie les fichiers CSS de Bootstrap, et les balises `<script>` sont des liens vers le code JavaScript qui permet certaines fonctionnalités supplémentaires de Bootstrap. 

Vous pouvez consulter la [documentation Bootstrap](https://getbootstrap.com/) pour plus d'informations.

La balise `<title>{% block title %} {% endblock %}</title>` permet aux templates hérités de définir un titre personnalisé. 

Nous utilisons la boucle `for message in get_flashed_messages()` pour afficher les messages flashés (avertissements, alertes, etc.). 

Le placeholder `{% block content %} {% endblock %}` est l'endroit où les templates hérités placent le contenu afin que tous les templates aient accès à ce template de base, ce qui évite la répétition.

Ensuite, créez le fichier `index.html` qui étendra ce fichier `base.html` :

```html
{% extends 'base.html' %}

{% block content %}
    <h1 class="text-center mb-3">{% block title %} Bienvenue sur Shorty {% endblock %}</h1>
    <div class="row">
        <div class="col-md-2"></div>
        <div class="col-md-8">
            <form method="post" action="{{url_for('index')}}">
            <div class="form-floating mb-3">
                <input type="text" name="url" id="url"
                    placeholder="Entrez une URL looooooooooooongue" class="form-control"
                    value="{{ request.form['url'] }}" autofocus></input>
                <label for="url">URL</label>
            </div>
            <div class="form-floating mb-3">
                <input type="text" name="custom_id" id="custom_id"
                    placeholder="Souhaitez-vous personnaliser ? (optionnel)" class="form-control"
                    value="{{ request.form['custom_id'] }}"></input>
                <label for="custom_id">Identifiant court personnalisé</label>
            </div>

            <div class="form-group text-center">
                <button type="submit" class="btn btn-lg btn-primary">Raccourcir</button>
            </div>
            </form>

            {% if short_url %}
            <hr>
            <span><a href="{{ short_url }}" target="_blank">{{ short_url }}</a></span>
            {% endif %}
        </div>
        <div class="col-md-2"></div>
    </div>
{% endblock %}
```

Ici, nous étendons `base.html`, définissons un titre et créons un formulaire avec deux entrées nommées `url` et `custom_id`. 

L'entrée `url` permettra aux utilisateurs de saisir des URLs à raccourcir. Elle a une valeur de `request.form['url']`, qui stocke les données en cas d'échec de soumission (c'est-à-dire si l'utilisateur ne fournit aucune URL). De même, l'entrée `custom_id` permettra aux utilisateurs de saisir un identifiant court personnalisé. Nous avons ensuite un bouton de soumission.

Ensuite, nous vérifions si la variable `short_url` a une valeur — cela est vrai si le formulaire est soumis et que l'URL courte est générée avec succès. Si la condition est vraie, nous affichons l'URL courte sous le formulaire.

Maintenant, nous pouvons réécrire notre fonction de vue d'index dans `routes.py` comme suit :

```python
from datetime import datetime
from core.models import ShortUrls
from core import app, db
from random import choice
import string
from flask import render_template, request, flash, redirect, url_for


def generate_short_id(num_of_chars: int):
    """Fonction pour générer un short_id avec un nombre spécifié de caractères"""
    return ''.join(choice(string.ascii_letters+string.digits) for _ in range(num_of_chars))


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        short_id = request.form['custom_id']

        if short_id and ShortUrls.query.filter_by(short_id=short_id).first() is not None:
            flash('Veuillez entrer un identifiant personnalisé différent !')
            return redirect(url_for('index'))

        if not url:
            flash("L'URL est requise !")
            return redirect(url_for('index'))

        if not short_id:
            short_id = generate_short_id(8)

        new_link = ShortUrls(
            original_url=url, short_id=short_id, created_at=datetime.now())
        db.session.add(new_link)
        db.session.commit()
        short_url = request.host_url + short_id

        return render_template('index.html', short_url=short_url)

    return render_template('index.html')

```

La fonction `index()` est une fonction de **vue** Flask, qui est une fonction décorée en utilisant le décorateur spécial `@app.route`. Sa valeur de retour est convertie en une réponse HTTP qu'un client HTTP, tel qu'un navigateur web, affiche.

À l'intérieur de la fonction de vue `index()`, nous acceptons les requêtes GET et POST en passant `methods=['GET', 'POST']` au décorateur `app.route()`.

Ensuite, si la requête est une requête GET, elle saute la condition `if request.method == 'POST'` jusqu'à la dernière ligne. C'est ici que nous rendons un template appelé `index.html`, qui contiendra un formulaire pour que les utilisateurs saisissent une URL à raccourcir.

Si la requête est une requête POST, la condition `if request.method == 'POST'` est vraie, ce qui signifie qu'un utilisateur a soumis une URL. Nous stockons l'URL dans la variable `url`. Si l'utilisateur a soumis un formulaire vide, vous affichez le message `L'URL est requise !` et redirigez vers la page d'index. 

Si l'utilisateur a entré `custom_id`, nous le stockons dans **short_id**, sinon nous générons un identifiant court aléatoire en utilisant la fonction que nous avions créée auparavant.

Si l'utilisateur a soumis une URL, nous créons un `new_link` avec toutes les données telles que `original_url`, `short_id` et `created_at`. Ensuite, nous validons la transaction.

Nous construisons ensuite l'URL courte en utilisant `request.host_url`, qui est un attribut que l'objet `request` de Flask fournit pour accéder à l'URL de l'hôte de l'application. Cela sera `http://127.0.0.1:5000/` dans un environnement de développement et `our_domain` si nous déployons notre application. 

Par exemple, la variable `short_url` aura une valeur comme `http://127.0.0.1:5000/asdf1gHJ`, qui est l'URL courte qui redirigera les utilisateurs vers l'URL originale stockée dans la base de données avec l'ID qui correspond à `asdf1gHJ`.

Enfin, nous rendons le template `index.html` en passant la variable `short_url`.

Nous pouvons maintenant exécuter le serveur et tester notre fonction de vue.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/1_ufNnbLzmSkxovhLYbJybHA.png)

Nous avons créé une application Flask avec une page qui accepte les URLs et en génère des versions plus courtes, mais les URLs ne font encore rien. 

Dans l'étape suivante, nous allons ajouter une route qui extrait le short_id de l'URL courte, trouve l'URL originale et redirige les utilisateurs vers celle-ci.

## Comment ajouter la route de redirection

Dans cette étape, nous allons ajouter une nouvelle route qui prend l'identifiant court généré par l'application et récupère l'URL originale. Enfin, nous allons rediriger les utilisateurs vers l'URL originale.

```python
@app.route('/<short_id>')
def redirect_url(short_id):
    link = ShortUrls.query.filter_by(short_id=short_id).first()
    if link:
        return redirect(link.original_url)
    else:
        flash('URL invalide')
        return redirect(url_for('index'))
```

Cette nouvelle route accepte une valeur `short_id` via l'URL et la passe à la fonction de vue `url_redirect()`. Par exemple, visiter `[http://127.0.0.1:5000/asdf1gHJ](http://127.0.0.1:5000/asdf1gHJ)` passerait la chaîne `'asdf1gHJ'` au paramètre `short_id`.

À l'intérieur de la fonction de vue, nous récupérons le lien de la base de données en utilisant le `short_id`. Si ce n'est pas None, la fonction de vue redirigera l'utilisateur vers l'`original_url` associée à ce `short_id` en utilisant la fonction d'assistance `redirect()` de Flask. Sinon, elle affichera un message d'erreur pour informer l'utilisateur que l'URL est invalide et le redirigera vers la page d'index.

Maintenant, nous pouvons à nouveau exécuter le serveur et enfin tester l'application.

## Comment déployer l'application sur Heroku

Pour déployer notre application sur [Heroku](https://heroku.com/), nous devons apporter quelques modifications à notre projet. Mais d'abord, vous devriez créer un compte gratuit sur Heroku. 

Rendez-vous sur [heroku.com](https://signup.heroku.com/) et créez un compte. Une fois que vous avez créé le compte, vous êtes prêt à continuer.

Connectez-vous à votre compte Heroku, et vous serez accueilli avec un écran similaire à celui-ci :

![Image](https://www.freecodecamp.org/news/content/images/2021/12/Screenshot-2021-12-26-130519.png)

Cliquez sur le bouton **Nouveau** puis sur **Créer une nouvelle application**. Entrez le nom de l'application puis cliquez sur le bouton **Créer une application**. Assurez-vous que le nom est disponible.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/Screenshot-2021-12-26-130553.png)

Cliquez sur l'onglet **Paramètres**, et faites défiler jusqu'à **Buildpacks**. Cliquez sur le bouton **Ajouter un buildpack** et ajoutez **Python**.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/Screenshot-2021-12-26-130636.png)

Puisque nous aurons besoin d'une base de données pour cette application, nous allons ajouter une base de données Postgres (disponible gratuitement sur Heroku) dans les ressources. 

Cliquez sur l'onglet **Ressources** et recherchez Postgres dans la boîte de recherche. Sélectionnez **Heroku Postgres** dans les résultats de recherche, puis cliquez sur **Soumettre le formulaire de commande** pour l'ajouter aux ressources.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/Screenshot-2021-12-26-131308.png)

Comme nous avons utilisé des variables d'environnement dans notre projet, nous devons les ajouter sur Heroku. 

Cliquez sur l'onglet **Paramètres** et faites défiler jusqu'à **Config Vars** puis cliquez sur **Reveal Config Vars**. Ouvrez votre fichier `.env` dans le projet et copiez-collez-le dans vos Config Vars comme ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2021/12/Screenshot-2021-12-26-131347.png)

Remarquez que nous avons défini `APP_SETTINGS` sur `config.ProductionConfig` car nous déployons l'application publiquement. 

Nous allons déployer notre application en utilisant GitHub, ce qui rendra notre tâche plus facile. Si vous n'avez pas de compte GitHub, créez-en un pour vous [ici](https://github.com/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F&source=header-home). Si vous avez un compte GitHub, connectez-vous à votre compte. Une fois connecté, vous verrez un écran similaire :

![Image](https://www.freecodecamp.org/news/content/images/2021/12/screenshot-2021-12-02-095432_kwefk5.png)

Créez un dépôt pour votre projet en utilisant le bouton vert **Nouveau**. Allez ensuite dans votre projet sur votre système. Assurez-vous que Git est installé dans votre système. Si ce n'est pas le cas, installez-le depuis [ici](https://git-scm.com/downloads). Ouvrez un terminal dans votre projet et écrivez les commandes ci-dessous :

```bash
$ git init
$ git remote add origin <votre-url-de-dépôt-ici>
$ git add .
$ git commit -m "Commit initial"
$ git push origin main
```

Remplacez `<votre-url-de-dépôt-ici>` par l'URL fournie par GitHub.

Maintenant, nous devons ajouter deux nouveaux fichiers requis par Heroku — `Procfile` et `runtime.txt` :

```procfile
web: gunicorn main:app
```

Cela déclare un seul type de processus, `web`, et la commande nécessaire pour l'exécuter. 

Le nom `web` est important ici. Il déclare que ce type de processus sera attaché à la [pile de routage HTTP](https://devcenter.heroku.com/articles/http-routing) de Heroku, et recevra le trafic web lors du déploiement. Remarquez que le fichier Procfile n'a aucune extension.

Ensuite, créez un fichier `runtime.txt` et ajoutez votre version de Python comme suit :

```markdown
python-3.9.7
```

Créez également un fichier `.gitignore` et ajoutez le contenu suivant :

```markdown
# Django #
*.log
*.pot
*.pyc
__pycache__
media
db.sqlite3

# Fichiers de sauvegarde # 
*.bak 

# Si vous utilisez PyCharm # 
.idea/**/workspace.xml 
.idea/**/tasks.xml 
.idea/dictionaries 
.idea/**/dataSources/ 
.idea/**/dataSources.ids 
.idea/**/dataSources.xml 
.idea/**/dataSources.local.xml 
.idea/**/sqlDataSources.xml 
.idea/**/dynamic.xml 
.idea/**/uiDesigner.xml 
.idea/**/gradle.xml 
.idea/**/libraries 
*.iws /out/ 

# Python # 
*.py[cod] 
*$py.class 

# Distribution / packaging 
.Python build/ 
develop-eggs/ 
dist/ 
downloads/ 
eggs/ 
.eggs/ 
lib/ 
lib64/ 
parts/ 
sdist/ 
var/ 
wheels/ 
*.egg-info/ 
.installed.cfg 
*.egg 
*.manifest 
*.spec 

# Journaux d'installation 
pip-log.txt 
pip-delete-this-directory.txt 

# Rapports de test unitaire / couverture 
htmlcov/ 
.tox/ 
.coverage 
.coverage.* 
.cache 
.pytest_cache/ 
nosetests.xml 
coverage.xml 
*.cover 
.hypothesis/ 

# Jupyter Notebook 
.ipynb_checkpoints 

# pyenv 
.python-version 

# celery 
celerybeat-schedule.* 

# Fichiers analysés SageMath 
*.sage.py 

# Environnements 
.env 
.venv 
env/ 
venv/ 
ENV/ 
env.bak/ 
venv.bak/ 

# Documentation mkdocs 
/site 

# mypy 
.mypy_cache/ 

# Sublime Text # 
*.tmlanguage.cache 
*.tmPreferences.cache 
*.stTheme.cache 
*.sublime-workspace 
*.sublime-project 

# Fichier de configuration sftp 
sftp-config.json 

# Fichiers spécifiques au contrôle de package Package 
Control.last-run 
Control.ca-list 
Control.ca-bundle 
Control.system-ca-bundle 
GitHub.sublime-settings 

# Visual Studio Code # 
.vscode/* 
!.vscode/settings.json 
!.vscode/tasks.json 
!.vscode/launch.json 
!.vscode/extensions.json 
.history
```

Cela indique à Git d'ignorer ces fichiers.

Maintenant, nous avons apporté suffisamment de modifications et nous sommes prêts à valider et à pousser vers le dépôt GitHub en utilisant les commandes :

```bash
$ git add .
$ git commit -m "Prêt pour le déploiement"
$ git push origin main
```

Maintenant, nous sommes complètement prêts à déployer notre application sur Heroku. 

Ouvrez l'application Heroku et cliquez sur l'onglet **Déployer**. Dans la **Méthode de déploiement** sur la page, choisissez GitHub. Recherchez votre dépôt et cliquez sur Connecter pour le sélectionner.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/Screenshot-2021-12-26-131430.png)

Une fois connecté avec succès, vous verrez un bouton appelé Déployer la branche. Cliquez sur le bouton et le processus de déploiement commencera :

![Image](https://www.freecodecamp.org/news/content/images/2021/12/Screenshot-2021-12-26-131502.png)

Heroku installera toutes les dépendances mentionnées dans le fichier requirements.txt et utilisera la version de Python mentionnée dans le fichier runtime.txt. Après la fin du processus, vous verrez un message de succès comme celui-ci :

![Image](https://www.freecodecamp.org/news/content/images/2021/12/Screenshot-2021-12-26-131709.png)

Notre application a été déployée avec succès !

Mais il reste encore une étape. Si vous vous souvenez, chaque fois que nous avons apporté des modifications à la base de données, nous devions migrer la base de données. De même ici, nous devons migrer la base de données. 

Cliquez sur **Plus** puis sur **Exécuter la console** pour exécuter bash. Une fois que vous avez cliqué dessus, vous trouverez une boîte de texte. Écrivez la commande suivante :

![Image](https://www.freecodecamp.org/news/content/images/2021/12/Screenshot-2021-12-26-132156.png)

Une fois que vous avez exécuté la commande, vous verrez les migrations de la base de données se produire. Avec cela, votre application a été déployée avec succès et vous êtes prêt à la tester !

Maintenant, vous pouvez suivre [ce tutoriel](https://devcenter.heroku.com/articles/custom-domains) pour ajouter un domaine personnalisé à votre application Heroku car l'URL Heroku est beaucoup trop longue.

# **Conclusion**

Nous avons créé une application Flask qui permet aux utilisateurs de saisir une URL longue et de générer une version plus courte. Si vous le souhaitez, vous pouvez ajouter plus de fonctionnalités à cette application telles que l'authentification des utilisateurs, les statistiques des URLs raccourcies, etc.

Merci d'avoir lu !

Dépôt GitHub : [https://github.com/ashutoshkrris/Flask-URL-Shortener](https://github.com/ashutoshkrris/Flask-URL-Shortener)