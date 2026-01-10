---
title: Comment utiliser DefaultDict en Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2024-05-01T21:15:48.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-defaultdict-python
coverImage: https://www.freecodecamp.org/news/content/images/2024/05/Add-To-Your-Python-Toolbox.png
tags:
- name: dictionary
  slug: dictionary
- name: Python
  slug: python
seo_title: Comment utiliser DefaultDict en Python
seo_desc: 'By Gage Schaffer

  Throughout my time working with datasets in Python, the dictionary has been my most
  used data structure. It’s versatile and easy to use.

  Need to count occurrences of a character? Use a dictionary!

  Want to create a list of soccer play...'
---

Par Gage Schaffer

Tout au long de mon travail avec des ensembles de données en Python, le dictionnaire a été ma structure de données la plus utilisée. Il est polyvalent et facile à utiliser.

Besoin de compter les occurrences d'un caractère ? Utilisez un dictionnaire !

Vous voulez créer une liste de joueurs de football et leurs statistiques associées ? Dictionnaire !

Ils ne sont pas infaillibles, cependant. Dans de nombreuses tâches, vous rencontrerez des KeyErrors à foison lors de l'analyse de données, ce qui peut être frustrant à gérer.

Gérer ces erreurs entraîne plusieurs lignes de code supplémentaires. Cela réduit la lisibilité et augmente la complexité. Si vous manipulez beaucoup de données, ce problème peut devenir incontrôlable.

Le module collections aborde ce problème de complexité. Le module collections fait partie de la bibliothèque standard de Python et contient quelques méthodes géniales pour manipuler les données. L'objectif principal du module est de rendre votre code plus lisible et de simplifier le traitement des données avec quelques types supplémentaires.

Celui que j'utilise le plus est `defaultdict`, et nous allons explorer quelques cas d'utilisation simples pour celui-ci aujourd'hui. Pour apprécier pleinement ce conteneur de données, vous devez avoir une connaissance pratique de Python. Plus spécifiquement, le type de dictionnaire standard.

## Comment simplifier votre code avec DefaultDict

Avant d'aborder le sujet d'aujourd'hui, examinons une situation. Je veux créer un dictionnaire qui me donne le nombre de toutes les différentes lettres dans le mot « Mississippi ». Il y a beaucoup de S et de P, et je n'ai pas le temps de les compter tous à la main.

Voici comment je ferais cela en utilisant un dictionnaire standard :

```python
letters = {}

for letter in "Mississippi":
    if letter not in letters:
    	letters[letter] = 1
    else:
    	letters[letter] +=1
    
print(letters)
# {'M': 1, 'i': 4, 's': 4, 'p': 2}
```

Assez simple. Ce programme :

* A itéré à travers la chaîne.
* À chaque itération, il a vérifié si la lettre avait déjà une entrée dans notre dictionnaire de lettres.
* Si la lettre est présente, il ajoute un à la valeur actuelle.
* Si la lettre n'est pas présente dans le dictionnaire de lettres, il crée l'entrée et définit la valeur initiale à 1.

Cet exemple était assez facile, mais vous pouvez voir la complexité du code s'immiscer déjà. Voyons comment nous pouvons faire mieux :

```python
from collections import defaultdict

letters = defaultdict(int)

for letter in "Mississippi":
    letters[letter] += 1
    
print(letters)
# defaultdict(<class 'int'>, {'M': 1, 'i': 4, 's': 4, 'p': 2})
```

Vous devriez remarquer que toutes les instructions conditionnelles ont maintenant disparu. Le code devrait être un peu plus facile à lire, mais nous avons toujours obtenu le même résultat à la fin du programme.

C'est l'avantage de `defaultdict`. Décomposons ce conteneur de données.

### Explorer le conteneur de données DefaultDict

L'idée d'un `defaultdict` est simple : si nous essayons d'accéder ou de modifier la valeur d'une clé qui n'existe pas, il crée l'entrée dans le dictionnaire avec la valeur par défaut donnée.

Dans l'exemple ci-dessus, nous avons commencé avec un defaultdict vide sans entrées. Pour chaque lettre unique que nous avons analysée, le dictionnaire a créé une entrée. Puisque nous avons utilisé `int` comme valeur par défaut, la valeur de l'entrée créée était 0. Après que le dictionnaire ait créé l'entrée, il a ajouté un à l'entrée.

À la fin du programme, le compte des lettres a été produit sans conditionnelles ni intervention manuelle. Très Pythonique.

### Comment définir la valeur par défaut dans DefaultDict

Le conteneur de données `defaultdict` prend un seul argument lors de son initialisation, nommé `default_factory`.

Cet argument `default_factory` est une fonction. Lorsque le programme tente d'accéder à une entrée qui n'existe pas, le `defaultdict` appelle le `default_factory` sans aucun argument. Donc, par exemple, je peux appeler un `defaultdict` avec la fonction `int()` comme ceci :

```python
d1 = defaultdict(int)
```

Lorsque j'essaie d'accéder à une entrée qui n'existe pas, elle ajoutera cette entrée avec la valeur de la fonction `int`, qui est 0.

```python
d1 = defaultdict(int)

d1["Adding an entry!"]

Print(d1)
# defaultdict(<class 'int'>, {'Adding an Entry!': 0})
```

## Explorer les possibilités de DefaultDict

Maintenant que vous connaissez l'utilisation de base de `defaultdict`, nous pouvons explorer les possibilités.

Comme je l'ai mentionné plus tôt, le `default_factory` est une fonction sans arguments. Cela signifie que nous pouvons utiliser des types de données intégrés ainsi que des fonctions définies par l'utilisateur — tant qu'elles ne prennent pas d'arguments.

Revenons à notre exemple de Mississippi. Je veux connaître l'index réel de toutes les lettres I. Je vais utiliser un `defaultdict` avec une liste pour l'argument `default_factory` afin que nous puissions suivre tous les index.

```python
from collections import defaultdict

my_word = "Mississippi"

d1 = defaultdict(list)

for index, letter in enumerate(my_word):
	if letter == "i":
		d1[letter].append(index)
        
print(d1)
# defaultdict(<class 'list'>, {'i': [1, 4, 7, 10]})
```

Génial ! J'ai vérifié cet exemple à la main, et il semble correct. Il y a la lettre I située aux index 1, 4, 7 et 10.

Cet exemple semble un peu différent, mais l'idée est toujours la même. Voici les étapes :

* J'ai créé un `defaultdict` avec l'argument `default_factory` de `list`.
* J'ai itéré à travers le mot « Mississippi ».
* Si la lettre itérée est égale à « i », j'accède au dictionnaire avec la clé « i ».
* Si cette entrée dans le dictionnaire n'existe pas déjà, le conteneur de données `defaultdict` la créera pour moi et utilisera une liste vide comme valeur.
* J'utilise ensuite la méthode append de la liste pour ajouter l'index de la lettre itérée.

Explorons un peu plus. Puisque le `default_factory` prend une fonction comme argument, nous pouvons définir la nôtre — tant que notre fonction personnalisée ne prend pas d'argument.

```python
from collections import defaultdict

def return_hello():
	return "Hello!"
    
d1 = defaultdict(return_hello)

d1[1]
d1[2]
d1[3]

print(d1)
# defaultdict(<function return_hello at 0x0000014FC5D28DC0>, {1: 'Hello!', 2: 'Hello!', 3: 'Hello!'})
```

J'ai défini une fonction ici pour simplement retourner « Hello! » et je l'ai assignée à l'argument `default_factory`. Maintenant, lorsque nous essayons d'accéder à des entrées dans notre dictionnaire qui n'existent pas, le `defaultdict` appelle ma fonction personnalisée pour déterminer la valeur par défaut !

## Pour résumer

Dans ce guide, nous avons passé en revue le `defaultdict`, qui est un conteneur de données dans le module collections intégré de la bibliothèque standard de Python. Il nous permet d'accéder à des entrées dans un dictionnaire qui n'existent pas en les créant à la volée et en leur attribuant une valeur par défaut.

Nous avons vu que le `defaultdict` prend un argument `default_factory`, qui indique au dictionnaire la valeur par défaut à donner à une clé. Ceux-ci peuvent être des fonctions intégrées, telles que `int` ou `list`, ou peuvent être des fonctions définies par l'utilisateur, telles que notre fonction `return_hello` ci-dessus.

J'espère que vous avez appris quelque chose aujourd'hui !