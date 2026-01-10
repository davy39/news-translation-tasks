---
title: Comment commencer avec TinyDB en Python
subtitle: ''
author: Ashutosh Krishna
co_authors: []
series: null
date: '2022-01-13T18:46:34.000Z'
originalURL: https://freecodecamp.org/news/get-started-with-tinydb-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/tinydb--1-.png
tags:
- name: database
  slug: database
- name: Python
  slug: python
seo_title: Comment commencer avec TinyDB en Python
seo_desc: "While working on your personal projects, you'll often need to store some\
  \ data. You could use a SQL or NoSQL database with a server, but that would require\
  \ you to do a bit of setup. \nIn this article, we'll learn about TinyDB and how\
  \ to use it to store..."
---

Lorsque vous travaillez sur vos projets personnels, vous aurez souvent besoin de stocker des données. Vous pourriez utiliser une base de données SQL ou NoSQL avec un serveur, mais cela nécessiterait un peu de configuration. 

Dans cet article, nous allons découvrir TinyDB et comment l'utiliser pour stocker nos données au format JSON.

## Qu'est-ce que TinyDB ?

TinyDB est une base de données orientée document écrite en Python pur sans dépendances externes. 

Elle est conçue pour être facile et amusante à utiliser en fournissant une API simple et propre. Elle est assez simple à apprendre et à configurer, même pour un débutant.

### Quand ne pas utiliser TinyDB

Comme mentionné dans la documentation de TinyDB elle-même, ce n'est pas toujours le bon choix pour vos projets. Si vous avez besoin de fonctionnalités avancées comme :

* l'accès depuis plusieurs processus ou threads,
* la création d'index pour les tables,
* un serveur HTTP,
* la gestion des relations entre les tables ou similaires,
* [les garanties ACID](https://en.wikipedia.org/wiki/ACID).

TinyDB n'est pas la bonne base de données pour vous. Dans ces cas, envisagez d'utiliser des bases de données comme [SQLite](https://www.sqlite.org/), [Buzhug](https://buzhug.sourceforge.net/), [CodernityDB](http://labs.codernity.com/codernitydb/) ou [MongoDB](https://mongodb.org/).

## Comment installer TinyDB

Il est extrêmement facile d'installer TinyDB. Il suffit d'exécuter cette commande dans votre terminal :

```bash
pip install tinydb
```

## Comment utiliser TinyDB

Prenons l'exemple d'une application Todo où nous devons simplement effectuer des opérations CRUD. Maintenant que nous avons installé TinyDB, voyons comment nous pouvons stocker nos données en utilisant TinyDB. TinyDB fait tout en utilisant JSON.

La toute première chose que nous allons faire est d'importer les classes requises du module `tinydb`. Alors, lancez votre shell Python pour coder.

```bash
$ python
Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

Maintenant, nous sommes prêts à coder.

```repl
>>> from tinydb import TinyDB       
>>> db = TinyDB("todo_db.json")
>>> 
```

Nous avons créé une instance de la classe _TinyDB_ et lui avons passé le nom de fichier. Cela créera un fichier JSON `todo_app.json` où nos données seront stockées.

### Comment insérer des données dans TinyDB

Puisque nous traitons avec JSON, les données à ajouter ne seront rien d'autre qu'un [Dictionnaire Python](https://iread.ga/posts/84/everything-you-need-to-know-about-python-dictionaries). Alors, voyons comment nous pouvons insérer un élément :

```repl
>>> new_item = {"name": "Book", "quantity": 5}
>>> db.insert(new_item) 
1
>>> 
```

Tout d'abord, nous avons créé un nouveau dictionnaire appelé `new_item` avec `name` et `quantity` définis respectivement à `Book` et `5`. Ensuite, nous avons utilisé la méthode `insert()` dans la classe _TinyDB_ pour insérer les données dans la base de données. La méthode `insert()` retourne l'`id` du nouvel objet créé.

À ce stade, un nouveau fichier JSON appelé `todo_db.json` sera créé et après l'insertion des données. Il ressemblera à ceci :

```json
{"_default": {"1": {"name": "Book", "quantity": 5}}}
```

Si vous regardez de plus près, `_default` est le nom de la table (définie par défaut mais peut être changée), `1` est l'id du nouvel objet créé, et sa valeur est la donnée que nous venons d'insérer. Donc, en gros, ce n'est qu'un dictionnaire imbriqué.

Nous pouvons également insérer plusieurs éléments à la fois comme ceci :

```python
>>> items = [
...         {"name": "Cake", "quantity": 1},
...         {"name": "Candles", "quantity": 10},
...         {"name": "Balloons", "quantity": 50}
...     ]
>>> db.insert_multiple(items)   
[2, 3, 4]
```

Dans ce cas, nous avons créé une liste de dictionnaires appelée `items` et utilisé la méthode `insert_multiple()` pour insérer les éléments. Cette méthode retourne également une liste d'`id` des objets insérés.

Le fichier `todo_db.json` ressemble maintenant à ceci :

```json
{
  "_default": {
    "1": { "name": "Book", "quantity": 5 },
    "2": { "name": "Cake", "quantity": 1 },
    "3": { "name": "Candles", "quantity": 10 },
    "4": { "name": "Balloons", "quantity": 50 }
  }
}

```

### Comment récupérer des données de TinyDB

Il existe plusieurs façons de récupérer des données de votre base de données. Mais vous devrez d'abord créer une instance de la classe _Query_. Alors, faisons cela :

```repl
>>> from tinydb import Query
>>> Todo = Query()
>>> 
```

Vous pouvez utiliser la méthode `db.search()` pour récupérer des données. 

```repl
>>> db.search(Todo.name == 'Book')
[{'name': 'Book', 'quantity': 5}]
>>> db.search(Todo.name == 'Copies') 
[]
>>>
```

La méthode `search()` retourne la liste des éléments correspondant à la requête. Si aucun élément ne correspond, elle retourne une liste vide.

Nous pouvons également utiliser la méthode `get()` pour obtenir un élément.

```repl
>>> db.get(Todo.name == 'Book')
{'name': 'Book', 'quantity': 5}
>>> db.get(Todo.name == 'Copies') 
>>> 
```

La méthode `get()` retourne uniquement un document correspondant. Si aucun document ne correspond, elle retourne `None`.

Pour vérifier si un document existe dans la base de données ou non, nous utilisons la méthode `contains()`.

```repl
>>> db.contains(Todo.name == 'Copies') 
False
>>> db.contains(Todo.name == 'Book')   
True
>>>
```

Nous pouvons également obtenir le nombre de documents correspondant à notre requête en utilisant la méthode `count()`.

```repl
>>> db.insert({"name": "Balloons", "quantity": 500}) 
5
>>> db.count(Todo.name == 'Balloons') 
2
>>> 
```

Pour obtenir le nombre total de documents stockés dans la base de données, nous utilisons la méthode `len()`.

```repl
>>> len(db)
5
>>>
```

Pour obtenir tous les documents de la base de données, nous pouvons utiliser la méthode `all()` :

```repl
>>> db.all()
[{'name': 'Book', 'quantity': 5}, {'name': 'Cake', 'quantity': 1}, {'name': 'Candles', 'quantity': 10}, {'name': 'Balloons', 'quantity': 50}, {'name': 'Balloons', 'quantity': 500}]
>>>
```

### Comment mettre à jour des données dans TinyDB

La méthode `update()` prend les champs que les documents correspondants auront ou une méthode qui mettra à jour les documents. Elle peut également prendre une condition pour interroger un argument de manière optionnelle.

Pour mettre à jour un document correspondant à une requête, nous pouvons faire ceci :

```repl
>>> db.update({'name': 'Books'}, Todo.name == 'Book')
[1]
>>>
```

Ici, nous avons mis à jour le nom du document en `Books` (son nom était `Book` ci-dessus).

Parfois, nous devons mettre à jour tous les documents. Dans ce cas, nous n'écrivons pas l'argument de la requête.

```repl
>>> db.update({'quantity': 10}) 
[1, 2, 3, 4, 5]
>>> db.all()
[{'name': 'Books', 'quantity': 10}, {'name': 'Cake', 'quantity': 10}, {'name': 'Candles', 'quantity': 10}, {'name': 'Balloons', 'quantity': 10}, {'name': 'Balloons', 'quantity': 10}]
>>> 
```

Nous avons mis à jour la quantité de tous les documents à `10`.

### Comment supprimer des données dans TinyDB

Pour supprimer des documents de la base de données, nous utilisons la méthode `remove()`. Cette méthode prend une condition optionnelle et une liste optionnelle d'ids de documents. Si la condition est remplie, le document sera supprimé.

```repl
>>> db.remove(Todo.name == 'Cake')                              
[2]
>>> db.all()                      
[{'name': 'Books', 'quantity': 10}, {'name': 'Candles', 'quantity': 10}, {'name': 'Balloons', 'quantity': 10}, {'name': 'Balloons', 'quantity': 10}]
>>> db.remove(Todo.name == 'Copies')
[]
>>> 
```

Pour supprimer des documents en utilisant l'id du document, nous pouvons écrire ce code :

```repl
>>> db.remove(doc_ids=[4,5]) 
[4, 5]
>>> db.all()
[{'name': 'Books', 'quantity': 10}, {'name': 'Candles', 'quantity': 10}]
>>>
```

Pour tout supprimer de la base de données, nous pouvons utiliser la méthode `truncate()` :

```repl
>>> db.truncate()
>>> db.all()
[]
>>>
```

## Conclusion

Dans cet article, nous avons parlé de TinyDB et de la façon d'effectuer des opérations CRUD sur la base de données. 

Ce n'était qu'un tutoriel de base. Pour en savoir plus sur les utilisations avancées de TinyDB, vous pouvez consulter sa [documentation officielle](https://tinydb.readthedocs.io/en/latest/index.html).

Merci d'avoir lu !

<a class="cta-button" href="https://newsletter.ashutoshkrris.tk" target="_blank">S'abonner à ma newsletter</a>