---
title: Méthodes de Chaînes Python Expliquées avec des Exemples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-30T23:12:00.000Z'
originalURL: https://freecodecamp.org/news/the-string-strip-method-in-python-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d41740569d1a4ca36bc.jpg
tags:
- name: Python
  slug: python
- name: toothbrush
  slug: toothbrush
seo_title: Méthodes de Chaînes Python Expliquées avec des Exemples
seo_desc: 'String Find Method

  There are two options for finding a substring within a string in Python, find()
  and rfind().

  Each will return the position that the substring is found at. The difference between
  the two is that find() returns the lowest position, a...'
---

## **Méthode Find de Chaîne**

Il existe deux options pour trouver une sous-chaîne dans une chaîne en Python, `find()` et `rfind()`.

Chacune retournera la position à laquelle la sous-chaîne est trouvée. La différence entre les deux est que `find()` retourne la position la plus basse, et `rfind()` retourne la position la plus haute.

Des arguments de début et de fin optionnels peuvent être fournis pour limiter la recherche de la sous-chaîne à des portions de la chaîne.

Exemple :

```shell
>>> string = "Don't you call me a mindless philosopher, you overweight glob of grease!"
>>> string.find('you')
6
>>> string.rfind('you')
42
```

Si la sous-chaîne n'est pas trouvée, -1 est retourné.

```shell
>>> string = "Don't you call me a mindless philosopher, you overweight glob of grease!"
>>> string.find('you', 43)  # trouver 'you' dans la chaîne n'importe où à partir de la position 43 jusqu'à la fin de la chaîne
-1
```

Plus d'informations :

Méthodes de chaîne [documentation](https://docs.python.org/3/library/stdtypes.html#string-methods).

## **Méthode Join de Chaîne**

La méthode `str.join(iterable)` est utilisée pour joindre tous les éléments d'un `iterable` avec une chaîne spécifiée `str`. Si l'itérable contient des valeurs non chaînées, elle lève une exception TypeError.

`iterable` : Tous les itérables de chaîne. Cela pourrait être une liste de chaînes, un tuple de chaîne ou même une chaîne simple.

#### **Exemples**

Joindre une liste de chaînes avec `":"`

```python
print ":".join(["freeCodeCamp", "is", "fun"])
```

Sortie

```shell
freeCodeCamp:is:fun
```

Joindre un tuple de chaînes avec `" and "`

```python
print " and ".join(["A", "B", "C"])
```

Sortie

```shell
A and B and C
```

Insérer un `" "` après chaque caractère dans une chaîne

```python
print " ".join("freeCodeCamp")
```

Sortie :

```shell
f r e e C o d e C a m p
```

Joindre avec une chaîne vide.

```python
list1 = ['p','r','o','g','r','a','m']  
print("".join(list1))
```

Sortie :

```shell
program
```

Joindre avec des ensembles.

```python
test =  {'2', '1', '3'}
s = ', '
print(s.join(test))
```

Sortie :

```shell
2, 3, 1
```

#### **Plus d'informations :**

[Documentation Python sur String Join](https://docs.python.org/2/library/stdtypes.html#str.join)

## **Méthode Replace de Chaîne**

La méthode `str.replace(old, new, max)` est utilisée pour remplacer la sous-chaîne `old` par la chaîne `new` pour un total de `max` fois. Cette méthode retourne une nouvelle copie de la chaîne avec le remplacement. La chaîne originale `str` reste inchangée.

#### **Exemples**

1. Remplacer toutes les occurrences de `"is"` par `"WAS"`

```python
string = "This is nice. This is good."
newString = string.replace("is","WAS")
print(newString)
```

Sortie

```python
ThWAS WAS nice. ThWAS WAS good.
```

1. Remplacer les 2 premières occurrences de `"is"` par `"WAS"`

```python
string = "This is nice. This is good."
newString = string.replace("is","WAS", 2)
print(newString)
```

Sortie

```python
ThWAS WAS nice. This is good.
```

#### **Plus d'informations :**

Lisez plus sur le remplacement de chaîne dans la [documentation Python](https://docs.python.org/2/library/string.html#string.replace)

## **Méthode Strip de Chaîne**

Il existe trois options pour supprimer des caractères d'une chaîne en Python, `lstrip()`, `rstrip()` et `strip()`.

Chacune retournera une copie de la chaîne avec les caractères supprimés, au début, à la fin ou aux deux extrémités. Si aucun argument n'est donné, par défaut, les caractères d'espace blanc sont supprimés.

Exemple :

```py
>>> string = '   Hello, World!    '
>>> strip_beginning = string.lstrip()
>>> strip_beginning
'Hello, World!    '
>>> strip_end = string.rstrip()
>>> strip_end
'   Hello, World!'
>>> strip_both = string.strip()
>>> strip_both
'Hello, World!'
```

Un argument optionnel peut être fourni sous forme de chaîne contenant tous les caractères que vous souhaitez supprimer.

```py
>>> url = 'www.example.com/'
>>> url.strip('w./')
'example.com'
```

Cependant, notez que seul le premier `.` a été supprimé de la chaîne. Cela est dû au fait que la fonction `strip` ne supprime que les caractères de l'argument qui se trouvent à l'extrême gauche ou à l'extrême droite. Puisque w vient avant le premier `.`, ils sont supprimés ensemble, alors que 'com' est présent à l'extrémité droite avant le `.` après la suppression de `/`.

## **Méthode Split de Chaîne**

La fonction `split()` est couramment utilisée pour diviser des chaînes en Python.

#### **La méthode `split()`**

Modèle : `string.split(separator, maxsplit)`

`separator` : La chaîne délimitrice. Vous divisez la chaîne en fonction de ce caractère. Par exemple, cela pourrait être " ", ":", ";" etc.

`maxsplit` : Le nombre de fois où diviser la chaîne en fonction du `separator`. Si non spécifié ou -1, la chaîne est divisée en fonction de toutes les occurrences du `separator`

Cette méthode retourne une liste de sous-chaînes délimitées par le `separator`

#### **Exemples**

Diviser la chaîne sur l'espace : " "

```python
string = "freeCodeCamp is fun."
print(string.split(" "))
```

Sortie :

```python
['freeCodeCamp', 'is', 'fun.']
```

Diviser la chaîne sur la virgule : ","

```python
string = "freeCodeCamp,is fun, and informative"
print(string.split(","))
```

Sortie :

```python
['freeCodeCamp', 'is fun', ' and informative']
```

Aucun `separator` spécifié

```python
string = "freeCodeCamp is fun and informative"
print(string.split())
```

Sortie :

```python
['freeCodeCamp', 'is', 'fun', 'and', 'informative']
```

Note : Si aucun `separator` n'est spécifié, alors la chaîne est dépouillée de **tous** les espaces blancs

```python
string = "freeCodeCamp        is     fun and    informative"
print(string.split())
```

Sortie :

```python
['freeCodeCamp', 'is', 'fun', 'and', 'informative']
```

Diviser la chaîne en utilisant `maxsplit`. Ici, nous divisons la chaîne sur " " deux fois :

```python
string = "freeCodeCamp is fun and informative"
print(string.split(" ", 2))
```

Sortie :

```python
['freeCodeCamp', 'is', 'fun and informative']
```

#### **Plus d'informations**

Consultez la [documentation Python sur la division de chaîne](https://docs.python.org/2/library/stdtypes.html#str.split)