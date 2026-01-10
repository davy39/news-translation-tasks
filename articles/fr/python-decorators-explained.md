---
title: Les Décorateurs Python Expliqués Pour Débutants
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-06-06T18:50:33.000Z'
originalURL: https://freecodecamp.org/news/python-decorators-explained
coverImage: https://www.freecodecamp.org/news/content/images/2023/06/python_decorators_explained.png
tags:
- name: beginner
  slug: beginner
- name: decorator
  slug: decorator
- name: Python
  slug: python
seo_title: Les Décorateurs Python Expliqués Pour Débutants
seo_desc: "By Roy Chng\nIn the world of Python programming, decorators can be an elegant\
  \ and powerful tool in the hands of experienced developers. \nDecorators give you\
  \ the ability to modify the behavior of functions without altering their source\
  \ code, providing ..."
---

Par Roy Chng

Dans le monde de la programmation Python, les décorateurs peuvent être un outil élégant et puissant entre les mains des développeurs expérimentés. 

Les décorateurs vous donnent la capacité de modifier le comportement des fonctions sans altérer leur code source, fournissant une manière concise et flexible d'améliorer et d'étendre leur fonctionnalité.

Dans cet article, je vais passer en revue les intricacies de l'utilisation des décorateurs en Python, et montrer des exemples où ils sont utiles.

## Récapitulatif Rapide des Fonctions

Simplement dit, une fonction est une manière d'exécuter un bloc de code à plusieurs reprises avec différents arguments. 

En d'autres termes, elle peut prendre des entrées, utiliser ces entrées pour exécuter un ensemble de code pré-défini, et ensuite retourner une sortie.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/functions.png)
_Les fonctions prennent des entrées, les utilisent pour exécuter un ensemble de code et retournent une sortie_

En Python, une fonction est écrite comme suit :

```python
def add_one(num):
	return num + 1
```

Lorsque nous voulons l'appeler, nous pouvons écrire le nom de la fonction avec des parenthèses et passer les entrées nécessaires (arguments) :

```python
final_value = add_one(1)
print(final_value) # 2
```

Notez que pour la plupart, les arguments et les paramètres signifient la même chose. Ce sont les variables utilisées dans la fonction. 

La différence réside dans l'endroit où nous nous référons à eux. Les arguments sont ce que nous passons à la fonction lors de son appel, et les paramètres sont ce qui est déclaré dans la fonction.

## Comment Passer des Fonctions en tant qu'Arguments

Communément, lors de l'appel de fonctions avec des arguments, nous passons des valeurs telles que des entiers, des flottants, des chaînes de caractères, des listes, des dictionnaires et d'autres types de données.

Mais, quelque chose que nous pouvons aussi faire est de passer une fonction en tant qu'argument également :

```python
def inner_function():
	print("inner_function est appelée")
    
def outer_function(func):
	print("outer_function est appelée")
 	func()
   
outer_function(inner_function)
# outer_function est appelée
# inner_function est appelée
    
```

Dans cet exemple, nous créons deux fonctions : `inner_function` et `outer_function`.

 `outer_function` a un paramètre appelé `func` qu'elle appelle après avoir été elle-même appelée.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/first_class_citizens.png)
_outer_function s'exécute en premier. Elle appelle ensuite la fonction qui a été passée en tant que paramètre_

Pensez-y comme à la manière dont nous pouvons traiter les fonctions comme n'importe quelle autre valeur ou variable. 

Le terme approprié pour cela est que les fonctions sont des **citoyens de première classe**. Cela signifie qu'elles sont comme n'importe quel autre objet et peuvent être passées en tant qu'arguments dans d'autres fonctions, être assignées à des variables, ou retournées par d'autres fonctions.

Ainsi, `outer_function` peut prendre une fonction en tant que paramètre et l'appeler lorsqu'elle est exécutée.

## Comment Retourner des Fonctions

Un autre avantage de pouvoir traiter les fonctions comme des objets est que nous pouvons les définir dans d'autres fonctions et les retourner également :

```python
def outer_function():
	print("outer_function est appelée")
    
	def inner_function():
    		print("inner_function est appelée")
      
	return inner_function
```

Notez que dans cet exemple, lorsque nous retournons `inner_function`, nous ne l'avons pas appelée. 

Nous avons seulement retourné la référence à celle-ci, afin de pouvoir la stocker et l'appeler plus tard :

```python
returned_function = outer_function()
# outer_funciton est appelée

returned_function()
# inner_function est appelée
```

Si vous êtes comme moi, cela peut sembler intéressant et tout, mais vous vous demandez probablement encore comment cela peut être utile dans des programmes réels 🤔. C'est quelque chose que nous allons examiner dans un moment !

## Comment Créer des Décorateurs en Python

Accepter des fonctions en tant qu'arguments, définir des fonctions au sein d'autres fonctions, et les retourner sont exactement ce que nous devons savoir pour créer des décorateurs en Python. Nous utilisons des décorateurs pour ajouter des fonctionnalités supplémentaires aux fonctions existantes.

Par exemple, si nous voulions créer un décorateur qui ajoutera 1 à la valeur de retour de n'importe quelle fonction, nous pouvons le faire comme suit :

```python
def add_one_decorator(func):
	def add_one():
    	value = func()
        return value + 1
        
	return add_one
```

Maintenant, si nous avons une fonction qui retourne un nombre, nous pouvons utiliser ce décorateur pour ajouter 1 à n'importe quelle valeur qu'elle produit.

```python
def example_function():
	return 1
    
final_value = add_one_decorator(example_function)
print(final_value()) # 2
```

Dans cet exemple, nous appelons la fonction `add_one_decorator` et passons la référence à `example_function`. 

Lorsque nous appelons la fonction `add_one_decorator`, elle crée une nouvelle fonction, `add_one`, définie à l'intérieur et retourne une référence à cette nouvelle fonction. Nous stockons cette fonction dans la variable `final_value`.

Ainsi, lorsque nous exécutons la fonction `final_value`, la fonction `add_one` est appelée.

La fonction `add_one` définie dans `add_one_decorator` appellera ensuite `example_function`, stockera sa valeur, et ajoutera un à celle-ci.

En fin de compte, cela résulte en `2` étant retourné et affiché dans la console.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/python_decorators-1.gif)
_Processus de la manière dont le code sera exécuté_

Remarquez comment nous n'avons pas eu à changer la fonction originale `example_function` pour modifier sa valeur de retour et ajouter des fonctionnalités à celle-ci. C'est ce qui rend les décorateurs si utiles !

Juste pour clarifier, les décorateurs ne sont pas spécifiques à Python. Ce sont un concept qui peut être appliqué dans d'autres langages de programmation. Mais en Python, vous pouvez les utiliser facilement en utilisant la syntaxe `@`.

## Comment Utiliser la Syntaxe `@` en Python

![Image](https://www.freecodecamp.org/news/content/images/2023/06/at_syntax.png)
_Le caractère @_

Comme nous l'avons vu ci-dessus, lorsque nous voulons utiliser des décorateurs, nous devons appeler la fonction décorateur et passer la fonction que nous voulons modifier.

En Python, nous pouvons utiliser la syntaxe `@` pour être beaucoup plus efficaces.

```python
@add_one_decorator
def example_function():
	return 1
```

En écrivant `@add_one_decorator` au-dessus de notre fonction, cela est équivalent à ce qui suit :

```python
example_function = add_one_decorator(example_function)
```

Cela signifie que chaque fois que nous appelons la fonction `example_function`, nous appellerons essentiellement la fonction `add_one` définie dans le décorateur.

## Comment Passer des Arguments Avec des Décorateurs

Lorsque nous utilisons des décorateurs, nous pouvons aussi vouloir que la fonction décorée puisse recevoir des arguments lorsqu'elle est appelée depuis la fonction wrapper.

Par exemple, si nous avions une fonction qui nécessite deux paramètres et retourne leur somme :

```python
def add(a,b):
	return a + b
    
print(add(1,2)) # 3
```

Et si nous utilisions un décorateur qui ajoutait 1 à la sortie :

```python
def add_one_decorator(func):
	def add_one():
    	value = func()
        return value + 1
        
    return add_one
    
@add_one_decorator
def add(a,b):
	return a + b
    
add(1,2)
# TypeError: add_one_decorator.<locals>.add_one() takes 0 positional arguments but 2 were given


```

En faisant cela, nous rencontrons une erreur : la fonction wrapper (`add_one`) ne prend aucun argument mais nous avons fourni deux arguments. 

Pour corriger cela, nous devons transmettre tous les arguments reçus de `add_one` à la fonction décorée lors de son appel :

```python
def add_one_decorator(func):
	def add_one(*args, **kwargs):
    	value = func(*args, **kwargs)
        return value + 1
        
     return add_one
     
 @add_one_decorator
 def add(a,b):
 	return a+b
    
 print(add(1,2)) # 4
```

Nous utilisons `*args` et `**kwargs` pour indiquer que la fonction wrapper `add_one` doit pouvoir recevoir n'importe quelle quantité d'arguments positionnels (`args`) et d'arguments mots-clés (`kwargs`). 

`args` sera une liste de tous les mots-clés positionnels donnés, dans ce cas `[1,2].`

`kwargs` sera un dictionnaire avec les clés comme arguments mots-clés utilisés et les valeurs comme les valeurs qui leur sont assignées, dans ce cas un dictionnaire vide.

Écrire `func(*args, **kwargs)` indique que nous voulons appeler `func` avec les mêmes arguments positionnels et mots-clés qui ont été reçus

Cela garantit que tous les arguments positionnels et mots-clés passés dans la fonction décorée seront passés dans la fonction originale.

## Pourquoi les Décorateurs en Python sont-ils Utiles ? Exemples de Code Réels

Maintenant que nous avons examiné ce que sont exactement les décorateurs Python, voyons quelques exemples concrets de quand les décorateurs sont utiles.

### Journalisation

Lors de la construction d'applications plus grandes, il est souvent utile d'avoir des journaux de quelles fonctions ont été exécutées avec des informations, telles que les arguments utilisés, et ce que la fonction a retourné pendant le temps d'exécution de l'application.

Cela peut être incroyablement utile pour le dépannage et le débogage lorsque les choses tournent mal, pour aider à localiser d'où le problème provient. Même si ce n'est pas pour le débogage, la journalisation peut être utile pour surveiller l'état de votre programme.

Voici un exemple simple de la manière dont nous pouvons créer un journaliseur simple (en utilisant le package `logging` intégré de Python) pour sauvegarder des informations sur notre application pendant qu'elle s'exécute, dans un fichier nommé `main.log` :

```python
import logging

def function_logger(func):
    logging.basicConfig(level = logging.INFO, filename="main.log")
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} ran with positional arguments: {args} and keyword arguments: {kwargs}. Return value: {result}")
        return result
    
    return wrapper

@function_logger
def add_one(value):
    return value + 1

print(add_one(1))
```

Chaque fois que la fonction `add_one` s'exécute, un nouveau journal sera ajouté au fichier `main.log` :

```
INFO:root:add_one ran with positional arguments: (1,) and keyword arguments: {}. Return value: 2

```

### Mise en Cache

Si nous avons une application qui nécessite l'exécution de la même fonction plusieurs fois avec les mêmes arguments, retournant la même valeur, cela peut rapidement devenir inefficace et prendre des ressources inutiles.

Pour éviter cela, il peut être utile de stocker les arguments utilisés et la valeur retournée de la fonction chaque fois qu'elle est appelée, et de simplement réutiliser la valeur retournée si nous avons déjà appelé la fonction avec les mêmes arguments.

En Python, cela peut être implémenté en utilisant le décorateur `@lru_cache` du module `functools` qui est installé avec Python.

**LRU** fait référence à **Least Recently Used**, ce qui signifie que chaque fois que la fonction a été appelée, les arguments utilisés et la valeur retournée seront stockés. Mais une fois que le nombre de ces entrées a atteint la taille maximale, qui par défaut est 128, l'entrée la moins récemment utilisée sera supprimée.

```python
from functools import lru_cache

@lru_cache
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

```

Dans cet exemple, la fonction `fibonacci` prend l'argument `n` et si celui-ci est inférieur à `1`, retourne `n`, sinon retourne la somme de la fonction appelée avec `n-1` et `n-2`.

Ainsi, si la fonction est appelée avec `n=10`, elle retourne `55` :

```python
print(fibnoacci(10))
# 55
```

Dans ce cas, lorsque nous appelons la fonction `fibonacci(10)`, elle appelle la fonction `fibonacci(9)` et `fibonacci(8)`, et ainsi de suite, jusqu'à ce qu'elle atteigne 1 ou 0.

Si nous devions ensuite utiliser cette fonction plus d'une fois :

```python
fibonacci(50)
fibonacci(100)
```

Nous pouvons utiliser le cache des entrées qui ont été sauvegardées. Ainsi, lorsque nous appelons `fibonacci(50)`, elle peut arrêter d'appeler la fonction `fibonacci` une fois qu'elle atteint `10` et lorsque nous appelons `fibonacci(100)`, elle peut arrêter d'appeler la fonction une fois qu'elle atteint `50`, rendant le programme beaucoup plus efficace.

Ces exemples ont un point commun, qui est qu'ils sont incroyablement faciles à implémenter dans vos fonctions préexistantes en Python. Vous n'avez pas besoin de modifier votre code ou d'envelopper manuellement votre fonction dans une autre. 

Pouvoir simplement utiliser la syntaxe `@` rend l'utilisation de modules et de packages supplémentaires très facile.

## Résumé

Les décorateurs Python rendent possible l'extension sans effort des fonctions sans avoir à les modifier. Dans ce tutoriel, vous avez appris comment fonctionnent les décorateurs et vu quelques exemples de leur utilisation.

Si vous appréciez mon écriture, envisagez de consulter ma [chaîne YouTube](https://www.youtube.com/@turbinethree) pour plus de contenu Python.

Bonne programmation !