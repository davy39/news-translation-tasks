---
title: Python Lire un Fichier JSON – Comment Charger du JSON depuis un Fichier et
  Analyser des Dumps
subtitle: ''
author: Estefania Cassingena Navone
co_authors: []
series: null
date: '2020-10-27T16:02:05.000Z'
originalURL: https://freecodecamp.org/news/python-read-json-file-how-to-load-json-from-a-file-and-parse-dumps
coverImage: https://www.freecodecamp.org/news/content/images/2020/08/Read-JSON-image.png
tags:
- name: dictionary
  slug: dictionary
- name: json
  slug: json
- name: Python
  slug: python
- name: Web Development
  slug: web-development
seo_title: Python Lire un Fichier JSON – Comment Charger du JSON depuis un Fichier
  et Analyser des Dumps
seo_desc: "Welcome! If you want to learn how to work with JSON files in Python, then\
  \ this article is for you. \nYou will learn:\n\nWhy the JSON format is so important.\n\
  Its basic structure and data types.\nHow JSON and Python Dictionaries work together\
  \ in Python.\nHo..."
---

Bienvenue ! Si vous souhaitez apprendre à travailler avec des fichiers JSON en Python, alors cet article est fait pour vous. 

**Vous apprendrez :**

* Pourquoi le format JSON est si important.
* Sa structure de base et ses types de données.
* Comment JSON et les dictionnaires Python fonctionnent ensemble en Python.
* Comment travailler avec le module intégré `json` de Python. 
* Comment convertir des chaînes JSON en objets Python et vice versa.
* Comment utiliser `loads()` et `dumps()`
* Comment indenter automatiquement les chaînes JSON.
* Comment lire des fichiers JSON en Python en utilisant `load()`
* Comment écrire dans des fichiers JSON en Python en utilisant `dump()`
* Et plus encore !

Êtes-vous prêt ? Commençons ! ✨

## 📝 Introduction : Qu'est-ce que JSON ?

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image-98.png)

Le format JSON a été initialement inspiré par la syntaxe de JavaScript (un langage de programmation utilisé pour le développement web). Mais depuis, il est devenu un **format de données indépendant du langage** et la plupart des langages de programmation que nous utilisons aujourd'hui peuvent générer et lire du JSON.

### Importance et Cas d'Utilisation de JSON

JSON est essentiellement un format utilisé pour stocker ou représenter des données. Ses cas d'utilisation courants incluent le développement web et les fichiers de configuration. 

Voyons pourquoi :

* **Développement Web :** JSON est couramment utilisé pour envoyer des données du serveur au client et vice versa dans les applications web. 

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image-65.png)

* **Fichiers de configuration :** JSON est également utilisé pour stocker des configurations et des paramètres. Par exemple, pour créer une [Application Google Chrome](https://developer.chrome.com/apps/first_app#one), vous devez inclure un fichier JSON appelé `manifest.json` pour spécifier le nom de l'application, sa description, la version actuelle, et d'autres propriétés et paramètres.  

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image-99.png)

## 📝 Structure et Format JSON

Maintenant que vous savez à quoi sert le format JSON, voyons sa structure de base avec un exemple qui représente les données d'une commande de pizza :

```json
{ 
	"size": "medium",
	"price": 15.67,
	"toppings": ["mushrooms", "pepperoni", "basil"],
	"extra_cheese": false,
	"delivery": true,
	"client": {
		"name": "Jane Doe",
		"phone": null,
		"email": "janedoe@email.com"
	}
}
```

Voici les principales caractéristiques du format JSON :

* Il y a une séquence de paires clé-valeur entourées par des accolades `{}`.
* Chaque clé est associée à une valeur particulière en utilisant ce format :

```
"key": <value> 
```

💡 **Astuce :** Les valeurs qui nécessitent des guillemets doivent être entourées de guillemets doubles.

* Les paires clé-valeur sont séparées par une virgule. Seule la dernière paire n'est pas suivie d'une virgule.

```json
{
	"size": "medium", # Virgule !
	"price": 15.67
}
```

💡 **Astuce :** Nous formatons généralement JSON avec différents niveaux d'indentation pour rendre les données plus faciles à lire. Dans cet article, vous apprendrez comment ajouter l'indentation automatiquement avec Python.

### Types de Données JSON : Clés et Valeurs

Les fichiers JSON ont des règles spécifiques qui déterminent quels types de données sont valides pour les clés et les valeurs.

* Les **clés** doivent être des chaînes de caractères.
* Les **valeurs** peuvent être une chaîne de caractères, un nombre, un tableau, une valeur booléenne (`true`/`false`), `null`, ou un objet JSON.

Selon la [Documentation Python](https://docs.python.org/3/library/json.html#json.dumps) :

> Les clés dans les paires clé/valeur de JSON sont toujours de type [`str`](https://docs.python.org/3/library/stdtypes.html#str). Lorsqu'un dictionnaire est converti en JSON, toutes les clés du dictionnaire sont converties en chaînes de caractères.

### Guide de Style

Selon le [Guide de Style JSON de Google](https://google.github.io/styleguide/jsoncstyleguide.xml) :

* Choisissez toujours des noms significatifs.
* Les types de tableau doivent avoir des noms de clés au pluriel. Tous les autres noms de clés doivent être au singulier. Par exemple : utilisez `"orders"` au lieu de `"order"` si la valeur correspondante est un tableau.
* Il ne doit pas y avoir de commentaires dans les objets JSON.

## 📝 JSON vs. Dictionnaires Python

JSON et les dictionnaires peuvent sembler très similaires au premier abord (visuellement), mais ils sont assez différents. Voyons comment ils sont "connectés" et comment ils se complètent pour faire de Python un outil puissant pour travailler avec des fichiers JSON.

JSON est un format de fichier utilisé pour représenter et stocker des données, tandis qu'un dictionnaire Python est la structure de données réelle (objet) qui est conservée en mémoire pendant l'exécution d'un programme Python.

### Comment JSON et les Dictionnaires Python Fonctionnent Ensemble

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image-100.png)

Lorsque nous travaillons avec des fichiers JSON en Python, nous ne pouvons pas simplement les lire et utiliser les données dans notre programme directement. Cela est dû au fait que l'ensemble du fichier serait représenté comme une seule chaîne et nous ne pourrions pas accéder aux paires clé-valeur individuellement.

Sauf si...

Nous utilisons les paires clé-valeur du fichier JSON pour créer un dictionnaire Python que nous pouvons utiliser dans notre programme pour lire les données, les utiliser et les modifier (si nécessaire).

C'est la principale connexion entre JSON et les dictionnaires Python. JSON est la représentation sous forme de chaîne des données et les dictionnaires sont les structures de données réelles en mémoire qui sont créées lorsque le programme s'exécute.

Super. Maintenant que vous en savez plus sur JSON, commençons à plonger dans les aspects pratiques de la façon dont vous pouvez travailler avec JSON en Python.

## 📝 Le Module JSON

Heureusement pour nous, Python est livré avec un module intégré appelé `json`. Il est installé automatiquement lorsque vous installez Python et il inclut des fonctions pour vous aider à travailler avec des fichiers et des chaînes JSON.

Nous utiliserons ce module dans les exemples à venir.

### Comment Importer le Module JSON

Pour utiliser `json` dans notre programme, nous devons simplement écrire une instruction d'importation en haut du fichier.

Comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image-73.png)

Avec cette ligne, vous aurez accès aux fonctions définies dans le module. Nous en utiliserons plusieurs dans les exemples.

**💡 Astuce :** Si vous écrivez cette instruction d'importation, vous devrez utiliser cette syntaxe pour appeler une fonction définie dans le module `json` :

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image-76.png)

## 📝 Python et les Chaînes JSON

Pour illustrer le fonctionnement de certaines des fonctions les plus importantes du module `json`, nous utiliserons une chaîne multi-lignes au format JSON.

### Chaîne JSON

En particulier, nous utiliserons cette chaîne dans les exemples. Il s'agit simplement d'une chaîne Python multi-lignes régulière qui suit le format JSON.

```python
data_JSON =  """
{
	"size": "Medium",
	"price": 15.67,
	"toppings": ["Mushrooms", "Extra Cheese", "Pepperoni", "Basil"],
	"client": {
		"name": "Jane Doe",
		"phone": "455-344-234",
		"email": "janedoe@email.com"
	}
}
"""
```

* Pour définir une chaîne multi-lignes en Python, nous utilisons des guillemets triples.
* Ensuite, nous attribuons la chaîne à la variable `data_JSON`.

💡 **Astuce :** Le [Guide de Style Python](https://www.python.org/dev/peps/pep-0008/#string-quotes) recommande d'utiliser des guillemets doubles pour les chaînes entre guillemets triples.

### Chaîne JSON vers Dictionnaire Python

Nous utiliserons la chaîne au format JSON pour créer un dictionnaire Python auquel nous pourrons accéder, travailler et modifier.

Pour ce faire, nous utiliserons la fonction `loads()` du module `json`, en passant la chaîne comme argument.

Voici la syntaxe de base :

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image-77.png)

Voici le code :

```python
# Importer le module
import json

# Chaîne avec format JSON
data_JSON =  """
{
	"size": "Medium",
	"price": 15.67,
	"toppings": ["Mushrooms", "Extra Cheese", "Pepperoni", "Basil"],
	"client": {
		"name": "Jane Doe",
		"phone": "455-344-234",
		"email": "janedoe@email.com"
	}
}
"""

# Convertir la chaîne JSON en dictionnaire
data_dict = json.loads(data_JSON)

```

Concentrons-nous sur cette ligne :

```python
data_dict = json.loads(data_JSON)
```

* `json.loads(data_JSON)` crée un nouveau dictionnaire avec les paires clé-valeur de la chaîne JSON et retourne ce nouveau dictionnaire.
* Ensuite, le dictionnaire retourné est attribué à la variable `data_dict`.

**Super !** Si nous imprimons ce dictionnaire, nous voyons cette sortie :

```python
{'size': 'Medium', 'price': 15.67, 'toppings': ['Mushrooms', 'Extra Cheese', 'Pepperoni', 'Basil'], 'client': {'name': 'Jane Doe', 'phone': '455-344-234', 'email': 'janedoe@email.com'}}
```

Le dictionnaire a été rempli avec les données de la chaîne JSON. Chaque paire clé-valeur a été ajoutée avec succès.

Maintenant, voyons ce qui se passe lorsque nous essayons d'accéder aux valeurs des paires clé-valeur avec la même syntaxe que nous utiliserions pour accéder aux valeurs d'un dictionnaire Python régulier :

```python
print(data_dict["size"])
print(data_dict["price"])
print(data_dict["toppings"])
print(data_dict["client"])
```

La sortie est :

```
Medium
15.67
['Mushrooms', 'Extra Cheese', 'Pepperoni', 'Basil']
{'name': 'Jane Doe', 'phone': '455-344-234', 'email': 'janedoe@email.com'}
```

Exactement ce que nous attendions. Chaque clé peut être utilisée pour accéder à sa valeur correspondante.

💡 **Astuce :** Nous pouvons utiliser ce dictionnaire comme n'importe quel autre dictionnaire Python. Par exemple, nous pouvons appeler des méthodes de dictionnaire, ajouter, mettre à jour et supprimer des paires clé-valeur, et plus encore. Nous pouvons même l'utiliser dans une boucle for.

### JSON vers Python : Conversion de Type

Lorsque vous utilisez `loads()` pour créer un dictionnaire Python à partir d'une chaîne JSON, vous remarquerez que certaines valeurs seront converties en leurs valeurs et types de données Python correspondants.

Ce tableau présenté dans la [Documentation Python](https://docs.python.org/3/library/json.html#encoders-and-decoders) pour le module `json` résume la correspondance entre les types de données et valeurs JSON et les types de données et valeurs Python :

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image-79.png)
_Tableau présenté dans la documentation officielle du [module json](https://docs.python.org/3/library/json.html#encoders-and-decoders)_

**💡 Astuce :** Le même tableau de conversion s'applique lorsque nous travaillons avec des fichiers JSON.

### Dictionnaire Python vers Chaîne JSON

Maintenant que vous savez comment créer un dictionnaire Python à partir d'une chaîne au format JSON.

Mais parfois, nous pourrions avoir besoin de faire exactement l'inverse, créer une chaîne au format JSON à partir d'un objet (par exemple, un dictionnaire) pour l'imprimer, l'afficher, le stocker ou travailler avec comme une chaîne.

Pour ce faire, nous pouvons utiliser la fonction `dumps` du module `json`, en passant l'objet comme argument :

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image-80.png)

**💡 Astuce :** Cette fonction retournera une chaîne.

Voici un exemple où nous convertissons le dictionnaire Python `client` en une chaîne au format JSON et la stockons dans une variable :

```python
# Dictionnaire Python
client = {
    "name": "Nora",
    "age": 56,
    "id": "45355",
    "eye_color": "green",
    "wears_glasses": False
}

# Obtenir une chaîne formatée JSON
client_JSON = json.dumps(client)
```

Concentrons-nous sur cette ligne :

```python
client_JSON = json.dumps(client)
```

* `json.dumps(client)` crée et retourne une chaîne avec toutes les paires clé-valeur du dictionnaire au format JSON.
* Ensuite, cette chaîne est attribuée à la variable `client_JSON`.

Si nous imprimons cette chaîne, nous voyons cette sortie :

```python
{"name": "Nora", "age": 56, "id": "45355", "eye_color": "green", "wears_glasses": false}
```

💡 **Astuce :** Remarquez que la dernière valeur (`false`) a été modifiée. Dans le dictionnaire Python, cette valeur était `False` mais en JSON, la valeur équivalente est `false`. Cela nous aide à confirmer que, en effet, le dictionnaire original est maintenant représenté comme une chaîne au format JSON.

Si nous vérifions le type de données de cette variable, nous voyons :

```python
<class 'str'>
```

Donc la valeur de retour de cette fonction était définitivement une chaîne.

### Python vers JSON : Conversion de Type

Un processus de conversion de type se produit également lorsque nous convertissons un dictionnaire en une chaîne JSON. Ce tableau de la [Documentation Python](https://docs.python.org/3/library/json.html#json.JSONEncoder) illustre les valeurs correspondantes :

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image-81.png)
_Tableau de la [documentation officielle du module json](https://docs.python.org/3/library/json.html#json.JSONEncoder)._

### Comment Imprimer du JSON avec Indentation

Si nous utilisons la fonction `dumps` et que nous imprimons la chaîne que nous avons obtenue dans l'exemple précédent, nous voyons :

```python
{"name": "Nora", "age": 56, "id": "45355", "eye_color": "green", "wears_glasses": false}
```

Mais ce n'est pas très lisible, n'est-ce pas ?

Nous pouvons améliorer la lisibilité de la chaîne JSON en ajoutant une **indentation**.

Pour le faire automatiquement, nous devons simplement passer un deuxième argument pour spécifier le nombre d'espaces que nous voulons utiliser pour indenter la chaîne JSON :

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image-111.png)

**💡 Astuce :** le deuxième argument doit être un entier non négatif (nombre d'espaces) ou une chaîne. Si l'indentation est une chaîne (comme `"\t"`), cette chaîne est utilisée pour indenter chaque niveau ([source](https://docs.python.org/3/library/json.html#json.dump)).

Maintenant, si nous appelons `dumps` avec ce deuxième argument :

```python
client_JSON = json.dumps(client, indent=4)
```

Le résultat de l'impression de `client_JSON` est :

```python
{
    "name": "Nora",
    "age": 56,
    "id": "45355",
    "eye_color": "green",
    "wears_glasses": false
}
```

C'est super, n'est-ce pas ? Maintenant notre chaîne est bien formatée. Cela sera très utile lorsque nous commencerons à travailler avec des fichiers pour stocker les données dans un format lisible par l'homme.

### Comment Trier les Clés

Vous pouvez également trier les clés par ordre alphabétique si nécessaire. Pour ce faire, vous devez simplement écrire le nom du paramètre `sort_keys` et passer la valeur `True` :

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image-84.png)

💡 **Astuce :** La valeur de `sort_keys` est `False` par défaut si vous ne passez pas de valeur.

Par exemple :

```python
client_JSON = json.dumps(client, sort_keys=True)
```

Retourne cette chaîne avec les clés triées par ordre alphabétique :

```python
{"age": 56, "eye_color": "green", "id": "45355", "name": "Nora", "wears_glasses": false}
```

### Comment Trier par Ordre Alphabétique et Indenter (en même temps)

Pour générer une chaîne JSON qui est triée par ordre alphabétique et indentée, vous devez simplement passer les deux arguments :

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image-104.png)

Dans ce cas, la sortie est :

```python
{
    "age": 56,
    "eye_color": "green",
    "id": "45355",
    "name": "Nora",
    "wears_glasses": false
}
```

**💡 Astuce :** Vous pouvez passer ces arguments dans n'importe quel ordre (relativement l'un à l'autre), mais l'objet doit être le premier argument de la liste.

Super. Maintenant que vous savez comment travailler avec des chaînes JSON, voyons comment vous pouvez travailler avec des fichiers JSON dans vos programmes Python.

## 📝 JSON et Fichiers

Typiquement, JSON est utilisé pour stocker des données dans des fichiers, donc Python nous donne les outils dont nous avons besoin pour lire ces types de fichiers dans notre programme, travailler avec leurs données et écrire de nouvelles données.

**💡 Astuce :** un fichier JSON a une extension `.json` :

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image-62.png)

Voyons comment nous pouvons travailler avec des fichiers `.json` en Python.

### Comment Lire un Fichier JSON en Python

Supposons que nous avons créé un fichier `orders.json` avec ces données qui représentent deux commandes dans une pizzeria :

```python
{
	"orders": [ 
		{
			"size": "medium",
			"price": 15.67,
			"toppings": ["mushrooms", "pepperoni", "basil"],
			"extra_cheese": false,
			"delivery": true,
			"client": {
				"name": "Jane Doe",
				"phone": null,
				"email": "janedoe@email.com"
			}
		},
		{
			"size": "small",
			"price": 6.54,
			"toppings": null,
			"extra_cheese": true,
			"delivery": false,
			"client": {
				"name": "Foo Jones",
				"phone": "556-342-452",
				"email": null
			}
		}
	]
}
```

Veuillez prendre un moment pour analyser la structure de ce fichier JSON.

Voici quelques conseils rapides :

* Remarquez les types de données des valeurs, l'indentation et la structure globale du fichier.
* La valeur de la clé principale `"orders"` est un tableau d'objets JSON (ce tableau sera représenté comme une liste en Python). Chaque objet JSON contient les données d'une commande de pizza.

Si nous voulons lire ce fichier en Python, nous devons simplement utiliser une instruction `with` :

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image-87.png)

💡 **Astuce :** Dans la syntaxe ci-dessus, nous pouvons attribuer n'importe quel nom à `file` (boîte verte). Il s'agit d'une variable que nous pouvons utiliser dans l'instruction `with` pour faire référence à l'objet fichier.

La ligne de code clé dans cette syntaxe est :

```
data = json.load(file)
```

* `json.load(file)` crée et retourne un nouveau dictionnaire Python avec les paires clé-valeur du fichier JSON.
* Ensuite, ce dictionnaire est attribué à la variable `data`.

💡 **Astuce :** Remarquez que nous utilisons `load()` au lieu de `loads()`. Il s'agit d'une fonction différente dans le module `json`. Vous en apprendrez plus sur leurs différences à la fin de cet article.

Une fois que nous avons le contenu du fichier JSON stocké dans la variable `data` sous forme de dictionnaire, nous pouvons l'utiliser pour faire pratiquement tout ce que nous voulons.

### Exemples

Par exemple, si nous écrivons :

```python
print(len(data["orders"]))
```

La sortie est `2` car la valeur de la clé principale `"orders"` est une liste avec deux éléments.

Nous pouvons également utiliser les clés pour accéder à leurs valeurs correspondantes. C'est ce que nous faisons généralement lorsque nous travaillons avec des fichiers JSON.

Par exemple, pour accéder aux garnitures de la première commande, nous écririons :

```
data["orders"][0]["toppings"]
```

* Tout d'abord, nous sélectionnons la clé principale `"orders"`
* Ensuite, nous sélectionnons le premier élément de la liste (index `0`).
* Enfin, nous sélectionnons la valeur qui correspond à la clé `"toppings"`

Vous pouvez voir ce "chemin" graphiquement dans le diagramme :

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image-101.png)

Si nous imprimons cette valeur, la sortie est :

```python
['mushrooms', 'pepperoni', 'basil']
```

Exactement ce que nous attendions. Vous devez simplement "plonger plus profondément" dans la structure du dictionnaire en utilisant les clés et indices nécessaires. Vous pouvez utiliser le fichier/chaîne JSON original comme référence visuelle. De cette façon, vous pouvez accéder, modifier ou supprimer n'importe quelle valeur.

**💡 Astuce :** N'oubliez pas que nous travaillons avec le nouveau dictionnaire. Les modifications apportées à ce dictionnaire n'affecteront pas le fichier JSON. Pour mettre à jour le contenu du fichier, nous devons écrire dans le fichier.

### Comment Écrire dans un Fichier JSON

Voyons comment vous pouvez écrire dans un fichier JSON.

La première ligne de l'instruction `with` est très similaire. Le seul changement est que vous devez ouvrir le fichier en mode `'w'` (écriture) pour pouvoir modifier le fichier.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image-105.png)

**💡 Astuce :** Si le fichier n'existe pas déjà dans le répertoire de travail actuel (dossier), il sera créé automatiquement. En utilisant le mode `'w'`, nous remplacerons l'intégralité du contenu du fichier s'il existe déjà.

Il existe deux façons alternatives d'écrire dans un fichier JSON dans le corps de l'instruction `with` :

* `dump`
* `dumps`

Examinons-les en détail.

**Première Approche : `dump`**

Il s'agit d'une fonction qui prend deux arguments :

* L'objet qui sera stocké au format JSON (par exemple, un dictionnaire).
* Le fichier où il sera stocké (un objet fichier).

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image-91.png)

Supposons que la pizzeria souhaite supprimer les données des clients du fichier JSON et créer un nouveau fichier JSON appelé `orders_new.json` avec cette nouvelle version.

Nous pouvons faire cela avec ce code :

```python
# Ouvrir le fichier orders.json
with open("orders.json") as file:
    # Charger son contenu et créer un nouveau dictionnaire
    data = json.load(file)

    # Supprimer la paire clé-valeur "client" de chaque commande
    for order in data["orders"]:
        del order["client"]

# Ouvrir (ou créer) un fichier orders_new.json
# et stocker la nouvelle version des données.
with open("orders_new.json", 'w') as file:
    json.dump(data, file)
```

Voici la version originale des données dans le fichier `orders.json`. Remarquez que la paire clé-valeur `"client"` existe.

```python
{
	"orders": [ 
		{
			"size": "medium",
			"price": 15.67,
			"toppings": ["mushrooms", "pepperoni", "basil"],
			"extra_cheese": false,
			"delivery": true,
			"client": {
				"name": "Jane Doe",
				"phone": null,
				"email": "janedoe@email.com"
			}
		},
		{
			"size": "small",
			"price": 6.54,
			"toppings": null,
			"extra_cheese": true,
			"delivery": false,
			"client": {
				"name": "Foo Jones",
				"phone": "556-342-452",
				"email": null
			}
		}
	]
}

```

Voici la nouvelle version dans le fichier `orders_new.json` :

```python
{"orders": [{"size": "medium", "price": 15.67, "toppings": ["mushrooms", "pepperoni", "basil"], "extra_cheese": false, "delivery": true}, {"size": "small", "price": 6.54, "toppings": null, "extra_cheese": true, "delivery": false}]}
```

Si vous analysez cela attentivement, vous verrez que la paire clé-valeur `"clients"` a été supprimée de toutes les commandes.

Cependant, il manque quelque chose dans ce fichier, n'est-ce pas ?

Veuillez prendre un moment pour réfléchir à cela... Qu'est-ce que cela pourrait être ?

L'indentation, bien sûr !

Le fichier ne ressemble pas vraiment à un fichier JSON, mais nous pouvons facilement corriger cela en passant l'argument `indentation=4` à `dump()`.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image-92.png)

Maintenant, le contenu du fichier ressemble à ceci :

```python
{
    "orders": [
        {
            "size": "medium",
            "price": 15.67,
            "toppings": [
                "mushrooms",
                "pepperoni",
                "basil"
            ],
            "extra_cheese": false,
            "delivery": true
        },
        {
            "size": "small",
            "price": 6.54,
            "toppings": null,
            "extra_cheese": true,
            "delivery": false
        }
    ]
}
```

Quelle différence ! C'est exactement ce que nous attendrions d'un fichier JSON.

Maintenant que vous savez comment lire et écrire dans des fichiers JSON en utilisant `load()` et `dump()`, voyons les différences entre ces fonctions et les fonctions que nous avons utilisées pour travailler avec des chaînes JSON.

## 📝 load() vs. loads()

Ce tableau résume les principales différences entre ces deux fonctions :

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image-110.png)

💡 **Astuce :** Pensez à `loads()` comme "load string" et cela vous aidera à vous souvenir de la fonction utilisée pour chaque but.

## 📝 dump() vs. dumps()

Voici un tableau qui résume les principales différences entre ces deux fonctions :

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image-109.png)

💡 **Astuce :** Pensez à `dumps()` comme un "dump string" et cela vous aidera à vous souvenir de la fonction utilisée pour chaque but.

## 📝 Terminologie Importante en JSON

Enfin, il y a deux termes importants que vous devez connaître pour travailler avec JSON :

* **Sérialisation :** convertir un objet en une chaîne JSON.
* **Désérialisation :** convertir une chaîne JSON en un objet.

## 📝 En Résumé

* JSON (JavaScript Object Notation) est un format utilisé pour représenter et stocker des données.
* Il est couramment utilisé pour transférer des données sur le web et pour stocker des paramètres de configuration.
* Les fichiers JSON ont une extension `.json`.
* Vous pouvez convertir des chaînes JSON en objets Python et vice versa.
* Vous pouvez lire des fichiers JSON et créer des objets Python à partir de leurs paires clé-valeur.
* Vous pouvez écrire dans des fichiers JSON pour stocker le contenu des objets Python au format JSON.

**J'espère vraiment que vous avez aimé mon article et que vous l'avez trouvé utile.** Maintenant, vous savez comment travailler avec JSON en Python. Suivez-moi sur Twitter [@EstefaniaCassN](https://twitter.com/EstefaniaCassN) et [découvrez mes cours en ligne](https://www.udemy.com/user/estefania-cn/).