---
title: Comment construire une API JSON avec Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-30T11:59:00.000Z'
originalURL: https://freecodecamp.org/news/build-a-simple-json-api-in-python
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca129740569d1a4ca4d0e.jpg
tags:
- name: Python
  slug: python
seo_title: Comment construire une API JSON avec Python
seo_desc: 'By Peter Gleeson

  The JSON API specification is a powerful way for enabling communication between
  client and server. It specifies the structure of the requests and responses sent
  between the two, using the JSON format.

  As a data format, JSON has the a...'
---

Par Peter Gleeson

La [spécification de l'API JSON](https://jsonapi.org/) est un moyen puissant pour permettre la communication entre le client et le serveur. Elle spécifie la structure des requêtes et des réponses envoyées entre les deux, en utilisant le format JSON.

En tant que format de données, JSON a l'avantage d'être léger et lisible. Cela le rend très facile à utiliser rapidement et de manière productive. La spécification est conçue pour minimiser le nombre de requêtes et la quantité de données qui doivent être envoyées entre le client et le serveur.

Ici, vous pouvez apprendre comment créer une API JSON de base en utilisant Python et Flask. Ensuite, le reste de l'article vous montrera comment essayer certaines des fonctionnalités que la spécification de l'API JSON a à offrir.

[Flask est une bibliothèque Python](https://flask.palletsprojects.com/en/1.1.x/) qui fournit un 'micro-framework' pour le développement web. Il est idéal pour le développement rapide car il vient avec une fonctionnalité centrale simple mais extensible. 

Un exemple vraiment basique de la façon d'envoyer une réponse de type JSON en utilisant Flask est montré ci-dessous :

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def example():
   return '{"name":"Bob"}'

if __name__ == '__main__':
    app.run()
```

Cet article utilisera deux extensions pour Flask : 

* [Flask-REST-JSONAPI](https://flask-rest-jsonapi.readthedocs.io/en/latest/) aidera à développer une API qui suit de près la spécification de l'API JSON.
* [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) utilisera [SQLAlchemy](https://www.sqlalchemy.org/) pour rendre la création et l'interaction avec une base de données simple très directe. 

### Vue d'ensemble

L'objectif final est de créer une API qui permet une interaction côté client avec une base de données sous-jacente. Il y aura quelques couches entre la base de données et le client - une couche d'abstraction de données et une couche de gestion des ressources.

![Image](https://www.freecodecamp.org/news/content/images/2019/07/flow.png)

Voici un aperçu des étapes impliquées :

1. Définir une base de données en utilisant Flask-SQLAlchemy
2. Créer une abstraction de données avec [Marshmallow-JSONAPI](https://marshmallow-jsonapi.readthedocs.io/en/latest/)
3. Créer des gestionnaires de ressources avec Flask-REST-JSONAPI
4. Créer des points de terminaison d'URL et démarrer le serveur avec Flask

Cet exemple utilisera un schéma simple décrivant des artistes modernes et leurs relations avec différentes œuvres d'art.

### Installer tout

Avant de commencer, vous devrez configurer le projet. Cela implique de créer un espace de travail et un environnement virtuel, d'installer les modules requis et de créer les fichiers principaux Python et de base de données pour le projet.

À partir de la ligne de commande, créez un nouveau répertoire et naviguez à l'intérieur.

```
$ mkdir flask-jsonapi-demo
$ cd flask-jsonapi-demo/
```

Il est bon de [créer des environnements virtuels](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/) pour chacun de vos projets Python. Vous pouvez sauter cette étape, mais elle est fortement recommandée.

```
$ python -m venv .venv
$ source .venv/bin/activate

```

Une fois que votre environnement virtuel a été créé et activé, vous pouvez installer les modules nécessaires pour ce projet.

```
$ pip install flask-rest-jsonapi flask-sqlalchemy
```

Tout ce dont vous aurez besoin sera installé en tant que dépendances pour ces deux extensions. Cela inclut Flask lui-même et SQLAlchemy.

L'étape suivante consiste à créer un fichier Python et une base de données pour le projet.

```
$ touch application.py artists.db
```

### Créer le schéma de la base de données

Ici, vous allez commencer à modifier `application.py` pour définir et créer le schéma de la base de données pour le projet.

Ouvrez `application.py` dans votre éditeur de texte préféré. Commencez par importer quelques modules. Pour plus de clarté, les modules seront importés au fur et à mesure.

Ensuite, créez un objet appelé `app` en tant qu'instance de la classe Flask.

Après cela, utilisez SQLAlchemy pour vous connecter au fichier de base de données que vous avez créé. La dernière étape consiste à définir et créer une table appelée `artists`.

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Créer une nouvelle application Flask
app = Flask(__name__)

# Configurer SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////artists.db'
db = SQLAlchemy(app)

# Définir une classe pour la table Artist
class Artist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    birth_year = db.Column(db.Integer)
    genre = db.Column(db.String)

# Créer la table
db.create_all()
```

### Créer une couche d'abstraction

L'étape suivante utilise le module [Marshmallow-JSONAPI](https://marshmallow-jsonapi.readthedocs.io/en/latest/) pour créer une abstraction de données logique sur les tables nouvellement définies.

La raison de créer cette couche d'abstraction est simple. Elle vous donne plus de contrôle sur la manière dont vos données sous-jacentes sont exposées via l'API. Considérez cette couche comme une lentille à travers laquelle le client de l'API peut voir clairement les données sous-jacentes, et uniquement les parties qu'il doit voir.

![Image](https://www.freecodecamp.org/news/content/images/2019/07/Untitled-Diagram-Page-2.png)

Dans le code ci-dessous, la couche d'abstraction de données est définie comme une classe qui hérite de la classe `Schema` de Marshmallow-JSONAPI. Elle fournira un accès via l'API à la fois aux enregistrements uniques et aux enregistrements multiples de la table des artistes.

À l'intérieur de ce bloc, la classe `Meta` définit quelques métadonnées. Plus précisément, le nom du point de terminaison de l'URL pour interagir avec les enregistrements uniques sera `artist_one`, où chaque artiste sera identifié par un paramètre d'URL `<id>`. Le nom du point de terminaison pour interagir avec plusieurs enregistrements sera `artist_many`.

Les autres attributs définis concernent les colonnes de la table des artistes. Ici, vous pouvez contrôler davantage comment chacun est exposé via l'API.

Par exemple, lors de l'envoi de requêtes POST pour ajouter de nouveaux artistes à la base de données, vous pouvez vous assurer que le champ `name` est obligatoire en définissant `required=True`.

Et si pour une raison quelconque vous ne vouliez pas que le champ `birth_year` soit retourné lors de l'envoi de requêtes GET, vous pouvez le spécifier en définissant `load_only=True`.

```python
from marshmallow_jsonapi.flask import Schema
from marshmallow_jsonapi import fields

# Créer une couche d'abstraction de données
class ArtistSchema(Schema):
    class Meta:
        type_ = 'artist'
        self_view = 'artist_one'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'artist_many'

    id = fields.Integer()
    name = fields.Str(required=True)
    birth_year = fields.Integer(load_only=True)
    genre = fields.Str()

```

### Créer des gestionnaires de ressources et des points de terminaison d'URL

La dernière pièce du puzzle est de créer un gestionnaire de ressources et un point de terminaison correspondant pour chacune des routes /artists et /artists/id.

Chaque gestionnaire de ressources est défini comme une classe qui hérite des classes `ResourceList` et `ResourceDetail` de Flask-REST-JSONAPI. 

Ici, ils prennent deux attributs. `schema` est utilisé pour indiquer la couche d'abstraction de données que le gestionnaire de ressources utilise, et `data_layer` indique la session et le modèle de données qui seront utilisés pour la couche de données.

Ensuite, définissez `api` comme une instance de la classe `Api` de Flask-REST-JSONAPI, et créez les routes pour l'API avec `api.route()`. Cette méthode prend trois arguments - la classe de la couche d'abstraction de données, le nom du point de terminaison et le chemin de l'URL.

La dernière étape consiste à écrire une boucle principale pour lancer l'application en mode débogage lorsque le script est exécuté directement. Le mode débogage est idéal pour le développement, mais il n'est pas adapté pour une utilisation en production.

```python
# Créer des gestionnaires de ressources et des points de terminaison

from flask_rest_jsonapi import Api, ResourceDetail, ResourceList

class ArtistMany(ResourceList):
    schema = ArtistSchema
    data_layer = {'session': db.session,
                  'model': Artist}

class ArtistOne(ResourceDetail):
    schema = ArtistSchema
    data_layer = {'session': db.session,
                  'model': Artist}

api = Api(app)
api.route(ArtistMany, 'artist_many', '/artists')
api.route(ArtistOne, 'artist_one', '/artists/<int:id>')

# boucle principale pour exécuter l'application en mode débogage
if __name__ == '__main__':
    app.run(debug=True)
```

### Faire des requêtes GET et POST

Maintenant, vous pouvez commencer à utiliser l'API pour [faire des requêtes HTTP](https://restfulapi.net/http-methods/). Cela peut être fait à partir d'un navigateur web, ou à partir d'un outil de ligne de commande comme curl, ou à partir d'un autre programme (par exemple, un script Python utilisant la bibliothèque Requests).

Pour lancer le serveur, exécutez le script `application.py` avec :

```
$ python application.py
```

Dans votre navigateur, accédez à [http://localhost:5000/artists](http://localhost:5000/artists). Vous verrez une sortie JSON de tous les enregistrements dans la base de données jusqu'à présent. Sauf qu'il n'y en a aucun.

Pour commencer à ajouter des enregistrements à la base de données, vous pouvez faire une requête POST. Une façon de faire cela est à partir de la ligne de commande en utilisant curl. Alternativement, vous pourriez utiliser un outil comme [Insomnia](https://insomnia.rest/), ou peut-être coder une interface utilisateur HTML simple qui envoie des données en utilisant un formulaire.

Avec [curl](https://curl.haxx.se/), à partir de la ligne de commande :

```
curl -i -X POST -H 'Content-Type: application/json' -d '{"data":{"type":"artist", "attributes":{"name":"Salvador Dali", "birth_year":1904, "genre":"Surrealism"}}}' http://localhost:5000/artists
```

Maintenant, si vous accédez à [http://localhost:5000/artists](http://localhost:5000/artists), vous verrez l'enregistrement que vous venez d'ajouter. Si vous deviez ajouter plus d'enregistrements, ils s'afficheraient tous ici également, car ce chemin d'URL appelle le point de terminaison `artists_many`.

Pour voir un seul artiste par son numéro `id`, vous pouvez accéder à l'URL pertinente. Par exemple, pour voir le premier artiste, essayez [http://localhost:5000/artists/1](http://localhost:5000/artists/1).

### Filtrer et trier

L'une des fonctionnalités intéressantes de la spécification de l'API JSON est la possibilité de retourner la réponse de manière plus utile en définissant certains paramètres dans l'URL. Par exemple, vous pouvez trier les résultats selon un champ choisi, ou filtrer en fonction de certains critères. 

Flask-REST-JSONAPI est livré avec cette fonctionnalité intégrée.

Pour trier les artistes par ordre d'année de naissance, accédez simplement à [http://localhost:5000/artists?sort=birth_year](http://localhost:5000/artists?sort=birth_year). Dans une application web, cela vous évitera de devoir trier les résultats côté client, ce qui pourrait être coûteux en termes de performance et donc impacter l'expérience utilisateur.

Le filtrage est également facile. Vous ajoutez à l'URL les critères que vous souhaitez filtrer, contenus dans des crochets. Il y a trois morceaux d'information à inclure :

* "name" - le champ par lequel vous filtrez (par exemple, `birth_year`)
* "op" - l'opération de filtrage ("égal à", "supérieur à", "inférieur à", etc.)
* "val" - la valeur à filtrer (par exemple, 1900)

Par exemple, l'URL ci-dessous récupère les artistes dont l'année de naissance est supérieure à 1900 :

[http://localhost:5000/artists?filter=[{"name":"birth_year","op":"gt","val":1900}]](http://localhost:5000/artists?filter=[{"name":"birth_year","op":"gt","val":1900}])

Cette fonctionnalité facilite grandement la récupération des seules informations pertinentes lors de l'appel de l'API. Cela est précieux pour améliorer les performances, surtout lors de la récupération de potentiellement grands volumes de données sur une connexion lente.

### Pagination

Une autre fonctionnalité de la spécification de l'API JSON qui aide à la performance est la pagination. C'est lorsque de grandes réponses sont envoyées sur plusieurs "pages", plutôt que toutes en une seule fois. Vous pouvez contrôler la taille de la page et le numéro de la page que vous demandez dans l'URL.

Ainsi, par exemple, vous pourriez recevoir 100 résultats sur 10 pages au lieu de charger les 100 en une seule fois. La première page contiendrait les résultats 1-10, la deuxième page contiendrait les résultats 11-20, et ainsi de suite.

Pour spécifier le nombre de résultats que vous souhaitez recevoir par page, vous pouvez ajouter le paramètre ?page[size]=X à l'URL, où X est le nombre de résultats. Flask-REST-JSONAPI utilise 30 comme taille de page par défaut.

Pour demander un numéro de page donné, vous pouvez ajouter le paramètre ?page[number]=X, où X est le numéro de page. Vous pouvez combiner les deux paramètres comme montré ci-dessous :

[http://localhost:5000/artists?page[size]=2&page[number]=2](http://localhost:5000/artists?page[size]=2&page[number]=1)

Cette URL définit la taille de la page à deux résultats par page et demande la deuxième page de résultats. Cela retournerait les troisième et quatrième résultats de la réponse globale.

### Relations

Presque toujours, les données dans une table seront liées aux données stockées dans une autre. Par exemple, si vous avez une table d'artistes, il est probable que vous souhaitiez également une table d'œuvres d'art. Chaque œuvre d'art est liée à l'artiste qui l'a créée.

La spécification de l'API JSON vous permet de travailler facilement avec des données relationnelles, et Flask-REST-JSONAPI vous permet de tirer parti de cela. Ici, cela sera démontré en ajoutant une table d'œuvres d'art à la base de données et en incluant des relations entre les artistes et les œuvres d'art.

Pour implémenter l'exemple des œuvres d'art, il sera nécessaire d'apporter quelques modifications au code dans `application.py`.

Tout d'abord, faites quelques imports supplémentaires, puis créez une nouvelle table qui relie chaque œuvre d'art à un artiste :

```python
from marshmallow_jsonapi.flask import Relationship
from flask_rest_jsonapi import ResourceRelationship


# Définir la table Artwork
class Artwork(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    artist_id = db.Column(db.Integer, 
        db.ForeignKey('artist.id'))
    artist = db.relationship('Artist',
        backref=db.backref('artworks'))
```

Ensuite, réécrivez la couche d'abstraction :

```python
# Créer une abstraction de données
class ArtistSchema(Schema):
    class Meta:
        type_ = 'artist'
        self_view = 'artist_one'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'artist_many'

    id = fields.Integer()
    name = fields.Str(required=True)
    birth_year = fields.Integer(load_only=True)
    genre = fields.Str()
    artworks = Relationship(self_view = 'artist_artworks',
        self_view_kwargs = {'id': '<id>'},
        related_view = 'artwork_many',
        many = True,
        schema = 'ArtworkSchema',
        type_ = 'artwork')

class ArtworkSchema(Schema):
    class Meta:
        type_ = 'artwork'
        self_view = 'artwork_one'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'artwork_many'

    id = fields.Integer()
    title = fields.Str(required=True)
    artist_id = fields.Integer(required=True)

```

Cela définit une couche d'abstraction pour la table des œuvres d'art et ajoute une relation entre l'artiste et l'œuvre d'art à la classe `ArtistSchema`.

Ensuite, définissez de nouveaux gestionnaires de ressources pour accéder aux œuvres d'art plusieurs à la fois et une à la fois, ainsi que pour accéder aux relations entre l'artiste et l'œuvre d'art.

```python
class ArtworkMany(ResourceList):
    schema = ArtworkSchema
    data_layer = {'session': db.session,
                  'model': Artwork}

class ArtworkOne(ResourceDetail):
    schema = ArtworkSchema
    data_layer = {'session': db.session,
                  'model': Artwork}

class ArtistArtwork(ResourceRelationship):
    schema = ArtistSchema
    data_layer = {'session': db.session,
                  'model': Artist}
```

Enfin, ajoutez quelques nouveaux points de terminaison :

```python
api.route(ArtworkOne, 'artwork_one', '/artworks/<int:id>')
api.route(ArtworkMany, 'artwork_many', '/artworks')
api.route(ArtistArtwork, 'artist_artworks',
    '/artists/<int:id>/relationships/artworks')
```

Exécutez `application.py` et essayez d'envoyer des données à partir de la ligne de commande via curl :

```
curl -i -X POST -H 'Content-Type: application/json' -d '{"data":{"type":"artwork", "attributes":{"title":"The Persistance of Memory", "artist_id":1}}}' http://localhost:5000/artworks
```

Cela créera une œuvre d'art liée à l'artiste avec `id=1`.

Dans le navigateur, accédez à [http://localhost:5000/artists/1/relationships/artworks](http://localhost:5000/artists/1/relationships/artworks). Cela devrait afficher les œuvres d'art liées à l'artiste avec `id=1`. Cela vous évite d'écrire une URL plus complexe avec des paramètres pour filtrer les œuvres d'art par leur champ `artist_id`. Vous pouvez rapidement lister toutes les relations entre un artiste donné et ses œuvres d'art.

Une autre fonctionnalité est la possibilité d'inclure des résultats liés dans la réponse à l'appel du point de terminaison `artists_one` :

[http://localhost:5000/artists/1?include=artworks](http://localhost:5000/artists/1?include=artworks)

Cela retournera la réponse habituelle pour le point de terminaison des artistes, ainsi que les résultats pour chacune des œuvres d'art de cet artiste.

### Champs épars

Une dernière fonctionnalité à mentionner - les champs épars. Lorsque vous travaillez avec de grandes ressources de données ayant de nombreuses relations complexes, les tailles de réponse peuvent exploser très rapidement. Il est utile de ne récupérer que les champs qui vous intéressent.

La spécification de l'API JSON vous permet de faire cela en ajoutant un paramètre de champs à l'URL. Par exemple, l'URL ci-dessous obtient la réponse pour un artiste donné et ses œuvres d'art associées. Cependant, au lieu de retourner tous les champs pour l'œuvre d'art donnée, elle retourne uniquement le titre.

[http://localhost:5000/artists/1?include=artworks&fields[artwork]=title](http://localhost:5000/artists/1?include=artworks&fields[artwork]=title)

Cela est à nouveau très utile pour améliorer les performances, surtout sur des connexions lentes. En règle générale, vous ne devez faire des requêtes vers et depuis le serveur qu'avec la quantité minimale de données requise.

### Remarques finales

La spécification de l'API JSON est un cadre très utile pour envoyer des données entre le serveur et le client dans un format propre et flexible. Cet article a fourni un aperçu de ce que vous pouvez faire avec elle, avec un exemple concret en Python utilisant la bibliothèque Flask-REST-JSONAPI.

Alors, que ferez-vous ensuite ? Les possibilités sont nombreuses. L'exemple de cet article a été une preuve de concept simple, avec seulement deux tables et une seule relation entre elles. Vous pouvez développer une application aussi sophistiquée que vous le souhaitez, et créer une API puissante pour interagir avec elle en utilisant tous les outils fournis ici.

Merci d'avoir lu, et continuez à coder en Python !