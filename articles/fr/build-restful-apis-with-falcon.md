---
title: Comment construire des API RESTful avec Falcon
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-06T01:15:00.000Z'
originalURL: https://freecodecamp.org/news/build-restful-apis-with-falcon
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e23740569d1a4ca3b8d.jpg
tags:
- name: Python
  slug: python
- name: REST API
  slug: rest-api
- name: toothbrush
  slug: toothbrush
seo_title: Comment construire des API RESTful avec Falcon
seo_desc: "Introduction\nRESTful APIs are a major component of any well-architected\
  \ stack, and Python happens to have some brilliant frameworks for quickly composing\
  \ APIs. \nOne of these frameworks is called Falcon - and it’s great! Essentially\
  \ a microframework, ..."
---

## **Introduction**

Les API RESTful sont un composant majeur de toute pile bien architecturée, et Python dispose de quelques frameworks brillants pour composer rapidement des API. 

L'un de ces frameworks s'appelle [Falcon](https://falconframework.org/) - et il est génial ! Essentiellement un microframework, il offre un nombre considérable d'avantages :

1. Il est rapide. Vraiment rapide. Consultez les benchmarks [ici](https://falconframework.org/#sectionBenchmarks).
2. Les ressources HTTP sont définies comme des classes, avec des méthodes de classe utilisées pour différentes opérations REST sur ces ressources. Cela aide à maintenir une base de code propre.
3. Il est assez extensible - consultez [cette section](https://github.com/falconry/falcon/wiki/Complementary-Packages) sur leur wiki pour vous en faire une idée.
4. Il est basé sur WSGI - le standard Python pour les applications web - donc il fonctionne avec Python 2.6, 2.7 et 3.3+. Et si vous avez besoin de plus de performance, exécutez-le avec PyPy !

## **Mise en route**

Tout d'abord, préparons notre environnement. Personnellement, il est toujours préférable de travailler dans des environnements virtuels - vous pouvez utiliser `virtualenv`, `virtualenvwrapper` ou `venv`. Ensuite, installez Falcon en utilisant `pip` : `pip install falcon`.

Nous allons développer une petite API d'exemple qui effectue des manipulations très basiques de fuseaux horaires pour nous. Elle affichera l'heure actuelle en UTC, ainsi que l'heure epoch correspondante. À cette fin, nous allons récupérer une bibliothèque pratique appelée `arrow` : `pip install arrow`.

Vous pouvez trouver l'exemple terminé à l'adresse [https://github.com/rudimk/freecodecamp-guides-rest-api-falcon](https://github.com/rudimk/freecodecamp-guides-rest-api-falcon).

## **Ressources**

Considérez une ressource comme une entité que votre API doit manipuler. Dans notre cas, la meilleure ressource serait un `Timestamp`. Notre routage serait typiquement quelque chose comme ceci :

```text
GET /timestamp
```

Ici, `GET` est le verbe HTTP utilisé pour appeler cet endpoint, et `/timestamp` est l'URL elle-même. Maintenant que nous avons clarifié ce point, créons un module !

`$ touch timestamp.py`

Il est temps d'importer la bibliothèque Falcon :

```python
import json

import falcon

import arrow
```

Notez que nous avons également importé le package `json` et la bibliothèque `arrow`. Maintenant, définissons une classe pour notre ressource :

```python
class Timestamp(object):

	def on_get(self, req, resp):
		payload = {}
		payload['utc'] = arrow.utcnow().format('YYYY-MM-DD HH:mm:SS')
		payload['unix'] = arrow.utcnow().timestamp

		resp.body = json.dumps(payload)
		resp.status = falcon.HTTP_200
```

Analysons ce snippet. Nous avons défini une classe `Timestamp`, et défini une méthode de classe appelée `on_get` - cette fonction indique à Falcon que lorsqu'une requête `GET` est émise vers un endpoint pour cette ressource, exécutez la fonction `on_get` et fournissez les objets de requête et de réponse comme paramètres. 

Après cela, c'est simple - nous créons un dictionnaire vide, le remplissons avec les timestamps UTC et UNIX actuels, le convertissons en JSON et l'attachons à l'objet de réponse.

Assez simple, n'est-ce pas ? Mais malheureusement, ce n'est pas tout. Nous devons maintenant créer un serveur Falcon et connecter la classe de ressource que nous venons de définir à un endpoint réel.

`$ touch app.py`

Maintenant, ajoutez le code ci-dessous :

```python
import falcon

from timestamp import Timestamp

api = application = falcon.API()

timestamp = Timestamp()

api.add_route('/timestamp', timestamp)
```

Ici, nous avons défini une API Falcon, et initialisé une instance de la classe de ressource que nous avons créée précédemment. Ensuite, nous avons connecté l'endpoint `/timestamp` avec l'instance de la classe - et maintenant nous sommes prêts à partir ! Pour tester cette API, installez `gunicorn` (`pip install gunicorn`), et exécutez `gunicorn app`. Utilisez Postman ou un simple `cURL` pour tester ceci :

```text
$ curl http://localhost:8000/timestamp                                                    
{"utc": "2017-10-20 06:03:14", "unix": 1508479437}
```

Et voilà !

## **Aller plus loin**

Une fois que vous avez compris Falcon, composer des API RESTful puissantes qui interagissent avec des bases de données ou des files d'attente de messages est très facile. Consultez la [documentation de Falcon](https://falcon.readthedocs.io/en/stable/index.html), ainsi que PyPI pour des modules Falcon intéressants qui continuent d'apparaître.