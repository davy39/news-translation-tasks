---
title: Comment gérer les KeyErrors en Python – avec des exemples de code
subtitle: ''
author: Bala Priya C
co_authors: []
series: null
date: '2024-06-17T18:24:14.000Z'
originalURL: https://freecodecamp.org/news/how-to-handle-keyerror-exceptions-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2024/06/fimg-key-errors.png
tags:
- name: error handling
  slug: error-handling
- name: Python
  slug: python
seo_title: Comment gérer les KeyErrors en Python – avec des exemples de code
seo_desc: 'When working with dictionaries in Python, you’d often run into KeyError
  exceptions.

  Dictionaries are built-in data structures of key value pairs. So you can look up
  a value—in constant time—using the corresponding key like so: dict[key] returns
  value...'
---

Lorsque vous travaillez avec des dictionnaires en Python, vous rencontrez souvent des exceptions `KeyError`.

Les dictionnaires sont des structures de données intégrées de paires clé-valeur. Vous pouvez donc rechercher une valeur—en temps constant—en utilisant la clé correspondante comme suit : `dict[key]` retourne `value`. Mais que se passe-t-il si la clé n'existe pas dans le dictionnaire ? Eh bien, c'est à ce moment-là que vous obtenez un `KeyError` en Python.

Il existe plusieurs façons de gérer ces exceptions `KeyError`. Vous pouvez les gérer explicitement ou utiliser certaines méthodes de dictionnaire pour définir des valeurs par défaut pour les clés manquantes. Et dans ce tutoriel, nous examinerons les méthodes suivantes en codant un exemple simple :

* Utilisation des blocs `try-except`
* Utilisation de la méthode de dictionnaire `get()`
* Utilisation de `defaultdict` du module `collections`

Commençons.

## 1. Comment gérer les exceptions KeyError avec les blocs `try-except`

Commençons par examiner quand les KeyErrors se produisent et comment nous pouvons gérer ces exceptions en utilisant des blocs `try-except`.

### Quand une KeyError se produit-elle ?

En Python, une exception `KeyError` se produit lorsque vous essayez d'accéder à la valeur correspondant à une clé qui n'existe pas. Considérez le dictionnaire `books` suivant :

```python
books = {
	"1984": "George Orwell",
	"To Kill a Mockingbird": "Harper Lee",
	"The Great Gatsby": "F. Scott Fitzgerald"
}

```

Dans le dictionnaire `books`, les clés sont les titres des livres et les valeurs sont les noms des auteurs. Vous pouvez donc rechercher l'auteur d'un livre en utilisant le titre comme clé.

Essayons maintenant de rechercher l'auteur d'un livre qui n'existe pas dans le dictionnaire :

```python
print(books["Brave New World"])
```

Vous rencontrerez l'exception `KeyError` suivante :

```
Traceback (most recent call last):
  File "/home/balapriya/keyerror/main.py", line 7, in <module>
	print(books["Brave New World"])
      	~~~~~^^^^^^^^^^^^^^^^^^^
KeyError: 'Brave New World'

```

### Comment gérer les exceptions KeyError

Vous pouvez gérer explicitement ces exceptions `KeyError` en utilisant des blocs `try-except` comme suit :

```python
try:
	value = dictionary[key]
except KeyError:
	value = default_value

```

Ici :

* Nous enveloppons le bloc de code qui pourrait lever une exception dans le bloc try. Dans ce cas, nous tentons d'accéder à la valeur associée à la clé.
* Si une `KeyError` est levée, nous la gérons dans le bloc `except` en attribuant une valeur par défaut.

Pour l'exemple du dictionnaire `books`, nous avons :

```python
books = {
	"1984": "George Orwell",
	"To Kill a Mockingbird": "Harper Lee",
	"The Great Gatsby": "F. Scott Fitzgerald"
}

try:
    # Essayez d'accéder à la clé "Brave New World"
	author = books["Brave New World"]  
    # Attrapez le KeyError si la clé n'existe pas
except KeyError:  
	author = "Livre non trouvé"  

print(author) 

```

Nous essayons de rechercher l'auteur de "Brave New World" à nouveau. Mais cette fois, le `KeyError` déclenche le bloc except, et nous obtenons "Livre non trouvé".

```python
Output >>> Livre non trouvé

```

## 2. Comment gérer les KeyErrors en utilisant la méthode de dictionnaire `get()`

Une autre façon de gérer les clés manquantes sans lever d'exception est d'utiliser la méthode de dictionnaire `get()`.

Vous pouvez utiliser la méthode `get()` sur n'importe quel objet dictionnaire valide. La méthode `get()` retourne la valeur pour une clé donnée si elle existe—sinon, elle retourne une valeur par défaut spécifiée. Vous pouvez l'utiliser comme suit :

```python
value = dictionary.get(key, default_value)
```

En essence, la méthode `get()` essaie d'obtenir la valeur pour la clé spécifiée :

* Si la clé existe, elle retourne la valeur correspondante.
* Si la clé n'existe pas, elle retourne la `default_value`.

Utilisons maintenant la méthode `get()` sur le dictionnaire books. Nous passons "Livre non trouvé" comme valeur par défaut dans l'appel de la méthode.

```python
books = {
	"1984": "George Orwell",
	"To Kill a Mockingbird": "Harper Lee",
	"The Great Gatsby": "F. Scott Fitzgerald"
}

# Essayez d'obtenir la valeur pour "Brave New World"
author = books.get("Brave New World", "Livre non trouvé")  
print(author)  

```

Comme prévu, vous devriez obtenir la sortie suivante :

```python
Output >>> Livre non trouvé
```

**Note** : La méthode `get()` ne modifie pas le dictionnaire original. Si vous souhaitez également ajouter la clé manquante avec une valeur par défaut, vous pouvez utiliser la méthode `setdefault()` à la place avec la syntaxe `dictionary.setdefault(key,default_value)`.

## 3. Comment utiliser `defaultdict` du module `collections`

Une façon (beaucoup) plus propre de gérer les KeyErrors est d'utiliser `defaultdict` du module `collections` de Python. Defaultdict étend les capacités du dictionnaire intégré de Python en vous permettant de fournir une valeur par défaut pour les clés qui n'ont pas été explicitement définies.

Le constructeur `defaultdict` prend une fonction d'usine par défaut comme argument. Cette fonction d'usine est appelée _sans_ arguments pour fournir une valeur par défaut pour une clé inexistante.

La syntaxe pour créer un `defaultdict` est la suivante :

```python
from collections import defaultdict

# Syntaxe
defaultdict(default_factory)

```

Créons un `defaultdict` à partir du dictionnaire `books` comme montré :

```python
from collections import defaultdict

books = {
	"1984": "George Orwell",
	"To Kill a Mockingbird": "Harper Lee",
	"The Great Gatsby": "F. Scott Fitzgerald"
}

books_default = defaultdict(lambda: "Livre non trouvé",books)  
# Accédez à la clé "Brave New World"
author = books_default["Brave New World"]  
print(author) 

```

Pour la fonction d'usine par défaut, nous utilisons une simple fonction lambda qui retourne la chaîne "Livre non trouvé". Cette fonction est appelée chaque fois que vous essayez d'accéder à une clé qui n'est pas présente dans le dictionnaire.

L'exécution de l'extrait ci-dessus devrait également vous donner :

```
Output >>> Livre non trouvé
```

L'utilisation de `defaultdict` peut être particulièrement utile lorsque vous devez accéder dynamiquement à de nombreuses clés.

## Conclusion

Et c'est tout ! J'espère que vous avez appris comment gérer les exceptions KeyError en Python. Récapitulons ce que nous avons appris :

* Pour gérer explicitement une `KeyError`, vous pouvez envelopper le code d'accès au dictionnaire avec un bloc `try`, et attraper la `KeyError` dans le bloc `except`.
* Utilisez la méthode `get()` pour accéder à la valeur d'une clé, avec l'option de retourner une valeur par défaut si la clé n'existe pas.
* Vous pouvez initialiser un `defaultdict` du module `collections` avec une fonction d'usine qui retourne la valeur par défaut.

Si vous souhaitez en savoir plus sur la gestion des exceptions en Python, lisez [Python Try and Except Statements - How to Handle Exceptions in Python](https://www.freecodecamp.org/news/python-try-and-except-statements-how-to-handle-exceptions-in-python/).