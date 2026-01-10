---
title: Comment Implémenter la Recherche Instantanée avec Flask et HTMX
subtitle: ''
author: Ashutosh Krishna
co_authors: []
series: null
date: '2024-07-22T11:36:53.000Z'
originalURL: https://freecodecamp.org/news/how-to-implement-instant-search-with-flask-and-htmx
coverImage: https://www.freecodecamp.org/news/content/images/2024/07/instant-search.png
tags:
- name: Flask Framework
  slug: flask
seo_title: Comment Implémenter la Recherche Instantanée avec Flask et HTMX
seo_desc: Instant search is a feature that shows search results as users type their
  query. Instead of waiting for a full page reload or submitting a form, results appear
  instantly, allowing users to find what they are looking for quickly. For example,
  when you...
---

La recherche instantanée est une fonctionnalité qui affiche les résultats de recherche au fur et à mesure que les utilisateurs saisissent leur requête. Au lieu d'attendre un rechargement complet de la page ou la soumission d'un formulaire, les résultats apparaissent instantanément, permettant aux utilisateurs de trouver rapidement ce qu'ils cherchent. Par exemple, lorsque vous commencez à taper dans une boîte de recherche, des suggestions ou des éléments correspondants apparaissent immédiatement, rendant le processus plus fluide et plus efficace.

Dans ce tutoriel, vous apprendrez à créer une fonctionnalité de recherche instantanée simple en utilisant Flask et HTMX. Cela vous aidera à construire des applications web interactives avec une meilleure expérience utilisateur.

## Table des Matières :

1. [Comment Configurer l'Environnement](#heading-installation)
2. [Comment Configurer la Base de Données](#heading-configuration-base-de-donnees)
3. [Comment Configurer le Routage de Base et le HTML](#heading-configuration-routage-html)
4. [Comment Ajouter HTMX pour la Recherche Instantanée](#heading-ajout-htmx-recherche-instantanee)
5. [Démonstration](#heading-demo)
6. [Conclusion](#heading-conclusion)

### **Pourquoi Utiliser la Recherche Instantanée ?**

* **Vitesse** : Les utilisateurs obtiennent un retour immédiat, ce qui les aide à affiner leur recherche.
* **Confort** : Cela réduit le nombre de clics et de rechargements de page, conduisant à une expérience plus fluide.
* **Engagement** : Les utilisateurs sont plus susceptibles de rester sur votre site s'ils peuvent trouver facilement ce dont ils ont besoin.

### **Technologies Utilisées**

Pour implémenter cette fonctionnalité de recherche instantanée, nous utiliserons deux technologies principales :

* **Flask** : [Flask](https://blog.ashutoshkrris.in/getting-started-with-flask) est un framework web populaire pour Python. Il est simple et léger, ce qui le rend facile à configurer et à commencer à construire rapidement des applications web. Flask vous permet de créer des routes, de gérer les requêtes et de servir des templates HTML avec une configuration minimale.
* **HTMX** : Il s'agit d'une bibliothèque JavaScript puissante qui vous permet de créer des pages web dynamiques sans avoir à écrire beaucoup de code JavaScript. Avec HTMX, vous pouvez mettre à jour des parties d'une page en fonction des actions de l'utilisateur, comme la saisie dans une boîte de recherche. Cela facilite le chargement des données depuis le serveur et leur affichage sur la page sans rechargement complet.

## Comment Configurer l'Environnement

Dans cette section, nous allons configurer l'environnement pour notre projet Flask, y compris l'installation des packages nécessaires et l'organisation de la structure du projet.

#### 1. Comment Installer Flask et HTMX

Tout d'abord, vous devez installer Flask, Flask-SQLAlchemy et Flask-Migrate. Vous pouvez le faire en utilisant pip. Ouvrez votre terminal et exécutez :

```bash
pip install Flask Flask-SQLAlchemy Flask-Migrate
```

Pour HTMX, nous l'inclurons dans notre template HTML directement depuis un CDN.

#### 2. Comment Créer un Environnement Virtuel

Il est bon de créer un environnement virtuel pour vos projets afin de gérer les dépendances. Voici comment en créer un :

```bash
python -m venv venv
```

Ensuite, activez l'environnement :

```bash
# Sur Windows
venv\Scripts\activate

# Sur macOS/Linux
source venv/bin/activate
```

#### 3. Comment Configurer la Structure du Projet

Maintenant, configurez la structure de votre projet comme suit :

```bash
my_flask_app/
├── core/
│   ├── __init__.py
│   ├── models.py
│   └── routes.py
├── config.py
└── main.py
```

Commençons par créer le premier fichier : **core/__init__.py**. Ce fichier est le script d'initialisation pour le module principal de notre application Flask. Il configure l'instance de l'application Flask et la paramètre en utilisant les paramètres de la classe `DevelopmentConfig`, et initialise la base de données et le système de migration.

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import DevelopmentConfig

# Créer l'instance de l'application Flask
app = Flask(__name__)

# Charger la configuration depuis DevelopmentConfig
app.config.from_object(DevelopmentConfig)

# Initialiser SQLAlchemy avec l'instance de l'application
db = SQLAlchemy(app)

# Initialiser Flask-Migrate avec l'instance de l'application et la base de données
migrate = Migrate(app, db)

# Importer les routes pour les enregistrer avec l'application
from core import routes
```

Ensuite, nous allons créer le fichier **config.py** à partir duquel nous importerons la classe `DevelopmentConfig`. Ce fichier contient les paramètres de configuration pour différents environnements (développement, test, production). Ces paramètres aident à gérer différents comportements et configurations en fonction de l'endroit où votre application est exécutée.

```python
class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = "guess-me"
    SQLALCHEMY_DATABASE_URI = "sqlite:///db.sqlite"
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

* `Config` : La classe de configuration de base avec les paramètres par défaut.
* `DevelopmentConfig` : Hérite de `Config` et remplace les paramètres de développement.
* `TestingConfig` : Hérite de `Config` et remplace les paramètres pour les tests.
* `ProductionConfig` : Hérite de `Config` et remplace les paramètres de production.

Enfin, nous allons créer le fichier **main.py**. Il s'agit du point d'entrée de notre application. Lorsque nous exécutons ce fichier, il démarre le serveur web Flask.

```python
from core import app

# Démarrer l'application Flask
if __name__ == '__main__':
    app.run(debug=True)
```

* `if __name__ == '__main__'` : Cela garantit que l'application Flask ne s'exécute que si le script est exécuté directement (et non importé en tant que module).
* `app.run(debug=True)` : Démarre le serveur de développement Flask avec le mode débogage activé, ce qui fournit des messages d'erreur détaillés et un rechargement automatique.

Maintenant que vous comprenez les fichiers du projet, nous pouvons procéder à l'implémentation de la fonctionnalité de recherche instantanée. Cela impliquera la création des modèles et de la route de recherche, la configuration du front-end alimenté par HTMX, et la connexion de tout pour récupérer et afficher dynamiquement les résultats de recherche.

## Comment Configurer la Base de Données

Dans cette section, nous allons configurer la base de données pour notre application Flask. Nous utiliserons SQLite pour sa simplicité. Nous allons créer un modèle pour les données que nous voulons rechercher et alimenter la base de données avec des données d'exemple.

SQLite est une base de données légère, basée sur le disque, qui ne nécessite pas de processus serveur séparé. C'est un excellent choix pour le développement et les petits projets car il est facile à configurer et à utiliser.

### Comment Créer un Modèle pour les Données à Rechercher

Nous allons créer un modèle `Book` pour représenter les données dans notre base de données. Ce modèle inclura des champs comme le titre du livre et l'auteur.

Créons le fichier `core/models.py` et ajoutons le modèle :

```python
from core import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
```

### Comment Appliquer les Migrations avec Flask-Migrate

Avant de pouvoir alimenter notre base de données, nous devons configurer les migrations de base de données en utilisant Flask-Migrate. Cet outil nous aide à gérer les changements de base de données, tels que la création de tables et la modification de schémas, de manière systématique.

Initialisez le dossier des migrations en exécutant la commande suivante dans votre répertoire de projet :

```bash
flask db init
```

Cette commande crée un répertoire **migrations** dans notre projet, qui stockera les scripts de migration.

Générez un script de migration qui crée les tables de base de données nécessaires en fonction de vos modèles :

```bash
flask db migrate -m "Initial migration"
```

Cette commande analyse vos modèles et génère un nouveau script de migration dans le dossier **migrations**.

Appliquez la migration pour créer les tables dans votre base de données :

```bash
flask db upgrade
```

Cette commande exécute le script de migration, créant les tables définies par vos modèles dans la base de données. Après cette étape, vous verrez un fichier **instance/db.sqlite** créé.

### Comment Alimenter la Base de Données

Maintenant que nous avons configuré la base de données et appliqué la migration, nous pouvons procéder à l'alimentation de la base de données. Créez un fichier nommé **seeder.py** avec le contenu suivant :

```python
import csv
from sqlalchemy.exc import IntegrityError

from core import db, app
from core.models import Book


def seed_data():
    with app.app_context():
        # Ouvrir le fichier CSV
        with open("data.csv", newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)

            # Itérer sur les lignes du fichier CSV
            for row in reader:
                # Créer une nouvelle instance de Book
                book = Book(
                    title=row['Book Name'],
                    author=row['Author Name']
                )

                # Ajouter le livre à la session
                db.session.add(book)

            try:
                # Valider la session pour écrire les livres dans la base de données
                db.session.commit()
                print("Livres ajoutés avec succès.")
            except IntegrityError as e:
                db.session.rollback()
                print(f"Erreur survenue : {e}")


if __name__ == "__main__":
    seed_data()
```

Le script de peuplement est responsable de l'alimentation de la base de données avec des données initiales. Cela est utile pour les tests et le développement, vous permettant de travailler avec un ensemble de données d'exemple. Ce script lit les données depuis **data.csv**, et les traite pour les insérer dans la base de données.

**Note** : Vous pouvez télécharger le fichier [data.csv](https://github.com/ashutoshkrris/instant-search-with-flask-htmx/blob/main/data.csv) ici.

Pour utiliser ce script, assurez-vous que votre fichier **data.csv** existe dans le même répertoire que **seeder.py**. Exécutez le script en utilisant Python :

```bash
python seeder.py
```

## Comment Configurer le Routage de Base et le HTML

Dans cette section, nous allons configurer une route de base dans Flask pour servir une page d'index (**index.html**) où les utilisateurs peuvent rechercher et afficher des livres.

### Comment Configurer la Route Flask

Configurons une route Flask (`/`) pour rendre un template **index.html** et afficher des livres. Pour cela, créez un fichier **core/routes.py** et ajoutez la route suivante :

```python
from flask import render_template
from core import app
from core.models import Book

@app.route('/')
def index():
    # Récupérer les 20 premiers livres à afficher par défaut
    books = Book.query.limit(20).all()
    return render_template("index.html", books=books)
```

L'application Flask gère le routage via le décorateur `@app.route('/')`, qui dirige les requêtes vers l'URL racine (`/`). Lorsque l'utilisateur visite la page d'accueil, la fonction `index()` est appelée. 

À l'intérieur de cette fonction, nous interrogeons le modèle `Book` en utilisant SQLAlchemy pour récupérer les 20 premiers livres de la base de données. Ces livres sont ensuite passés en tant que paramètre (`books`) à la fonction `render_template`, qui rend le template **index.html**.

### Comment Créer le Template index.html

Créez un fichier nommé **index.html** à l'intérieur d'un répertoire **templates** dans votre projet. Le répertoire **templates** se trouvera dans le package `core`. Ce fichier contiendra la structure HTML de notre page de recherche de livres.

```xml
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Book Search</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.9.4/css/bulma.min.css" />
</head>
<body>
  <section class="section">
    <div class="columns">
      <div class="column is-one-third is-offset-one-third">
        <input type="text" class="input" placeholder="Search" name="query" />
      </div>
    </div>
    <table class="table is-fullwidth">
      <thead>
        <tr>
          <th>ID</th>
          <th>Book Title</th>
          <th>Book Author</th>
        </tr>
      </thead>
      <tbody id="results">
        {% for book in books %}
        <tr>
          <td>{{ book.id }}</td>
          <td>{{ book.title }}</td>
          <td>{{ book.author }}</td>
        </tr>
        {% endfor %}
      </tbody>
    </table>
  </section>
</body>
</html>
```

Ce fichier HTML utilise le framework CSS Bulma pour le style et inclut des éléments tels qu'un champ de saisie pour les recherches des utilisateurs et un tableau pour afficher les détails des livres récupérés de la base de données.

Le template `index.html` utilise le templating Jinja2 pour remplir dynamiquement les lignes du tableau (`<tr>`) avec les données des livres récupérées depuis le backend Flask. L'`ID`, le `titre` et l'`auteur` de chaque livre sont affichés dans les lignes du tableau en utilisant `{{ book.id }}`, `{{ book.title }}`, et `{{ book.author }}` respectivement.

### Comment Exécuter l'Application

Exécutons l'application en utilisant la commande suivante :

```bash
flask run
```

Une fois votre application lancée, voici à quoi elle devrait ressembler :

![Page d'Accueil de l'Application de Recherche de Livres](https://cdn.hashnode.com/res/hashnode/image/upload/v1721316465728/d5037fd3-f49b-4c59-993c-4ff7c23cabef.png)
_page web avec ID, titres de livres et auteurs de livres_

## Comment Ajouter HTMX pour la Recherche Instantanée

Enfin, nous allons ajouter HTMX pour améliorer notre application Flask avec des capacités de recherche dynamique. Pour cela, nous introduirons une nouvelle route et modifierons le template HTML existant.

### Comment Créer la Route de Recherche

Tout d'abord, créez une nouvelle route `/search` dans votre application Flask pour gérer les recherches de livres en fonction de l'entrée de l'utilisateur :

```python
from flask import render_template, request
from core import app
from core.models import Book

@app.route('/search')
def search():
    query = request.args.get("query")
    if query:
        results = Book.query.filter(Book.title.ilike(f"%{query}%") | Book.author.ilike(f"%{query}%")).limit(10).all()
    else:
        results = Book.query.limit(20).all()
    return render_template("search_results.html", results=results)
```

Cette route écoute les requêtes `GET` vers `/search`. Elle récupère la requête de recherche depuis le paramètre d'URL en utilisant `request.args.get("query")`. 

Si un paramètre `query` est présent, elle utilise la méthode `ilike` de SQLAlchemy pour effectuer une recherche insensible à la casse sur les colonnes `title` et `author` de la table `Book`, récupérant jusqu'à 10 résultats.

Si aucun paramètre de requête n'est fourni, elle récupère par défaut les 20 premiers livres de la base de données. Les résultats sont passés à un nouveau template `search_results.html` pour le rendu.

### Comment Modifier index.html pour Ajouter HTMX

```xml
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Book Search</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.9.4/css/bulma.min.css" />
  <!-- Inclure la bibliothèque HTMX -->
  <script src="https://cdn.jsdelivr.net/npm/htmx.org/dist/htmx.min.js"></script>
</head>
<body>
  <section class="section">
    <div class="columns">
      <div class="column is-one-third is-offset-one-third">
        <!-- Champ de recherche activé par HTMX -->
        <input
            type="text"
            class="input"
            placeholder="Search"
            name="query"
            hx-get="/search"
            hx-trigger="keyup changed delay:500ms"
            hx-target="#results"
          />
      </div>
    </div>
    <table class="table is-fullwidth">
      <thead>
        <tr>
          <th>ID</th>
          <th>Book Title</th>
          <th>Book Author</th>
        </tr>
      </thead>
      <tbody id="results">
        {% for book in books %}
          <tr>
            <td>{{ book.id }}</td>
            <td>{{ book.title }}</td>
            <td>{{ book.author }}</td>
          </tr>
        {% endfor %}
      </tbody>
    </table>
  </section>
</body>
</html>
```

La balise `<script>` importe la bibliothèque HTMX depuis un CDN, permettant des interactions côté client sans nécessiter de JavaScript complexe. En plus de cela, nous avons amélioré l'élément `<input>` avec des attributs HTMX :

* `hx-get="/search"` : Spécifie le point de terminaison (`/search`) pour envoyer des requêtes GET lorsque l'utilisateur tape dans le champ de saisie.
* `hx-trigger="keyup changed delay:500ms"` : Déclenche l'action de recherche après un délai de 500ms lorsque l'utilisateur tape (`keyup`) ou modifie la saisie (`changed`).
* `hx-target="#results"` : Met à jour le contenu de l'élément avec `id="results"` avec la réponse du point de terminaison `/search`.

### Comment Créer le Template search_results.html

Ensuite, nous allons créer un nouveau template **search_results.html** pour afficher les résultats de recherche :

```xml
{% for result in results %}
<tr>
    <td>{{ result.id }}</td>
    <td>{{ result.title }}</td>
    <td>{{ result.author }}</td>
</tr>
{% endfor %}
```

Ce template itère sur `results`, qui sont passés depuis la route `/search`. Pour chaque livre dans `results`, il génère une ligne de tableau (`<tr>`) qui affiche l'ID, le titre et l'auteur du livre.

## Démonstration

Enfin, nous avons implémenté la recherche instantanée avec HTMX dans notre application Flask. Voici à quoi notre application finale devrait ressembler :

%[https://youtu.be/llCmZXaopX0]

Vous remarquerez un délai dans les résultats de recherche. Cela s'appelle le debouncing. Il s'agit d'une technique utilisée en programmation et en développement web pour limiter le taux auquel une fonction ou un gestionnaire d'événements est exécuté. Elle garantit qu'une fonction n'est exécutée qu'après qu'un certain temps se soit écoulé depuis le dernier appel de la fonction. 

Dans notre cas, nous avons défini le délai à 500ms avant qu'il n'appelle à nouveau l'API `/search`. Cela garantit que nous ne frappons pas l'API pour chaque caractère que l'utilisateur tape.

## Conclusion

Dans ce tutoriel, vous avez appris à implémenter la recherche instantanée en utilisant Flask et HTMX, en vous concentrant sur l'amélioration de l'interaction utilisateur et des performances. En intégrant HTMX pour les interactions AJAX, nous avons permis des mises à jour dynamiques des résultats de recherche sans recharger toute la page. 

Cette approche améliore non seulement l'expérience utilisateur en fournissant un retour en temps réel, mais optimise également la charge du serveur en utilisant le debouncing pour les requêtes de recherche. 

En maîtrisant ces techniques, vous êtes équipé pour construire des applications web réactives qui offrent des expériences de recherche fluides, combinant la flexibilité de Flask avec l'interactivité de HTMX pour répondre efficacement et efficacement aux divers besoins des utilisateurs.

Vous pouvez trouver le code de ce tutoriel dans ce dépôt : [https://github.com/ashutoshkrris/instant-search-with-flask-htmx](https://github.com/ashutoshkrris/instant-search-with-flask-htmx)