---
title: Comment analyser une chaîne de caractères en Python – Explication de l'analyse
  de chaînes
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2023-05-04T21:04:02.000Z'
originalURL: https://freecodecamp.org/news/how-to-parse-a-string-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/split-and-split-methods-in-python.png
tags:
- name: Python
  slug: python
seo_title: Comment analyser une chaîne de caractères en Python – Explication de l'analyse
  de chaînes
seo_desc: "Parsing a string can mean different things in Python. You can parse a string\
  \ by splitting or extracting the substrings. \nYou can also parse a string by converting\
  \ it to an integer or float variable. Although this should be categorized as a type\
  \ conve..."
---

Analyser une chaîne de caractères peut signifier différentes choses en Python. Vous pouvez analyser une chaîne en la divisant ou en extrayant les sous-chaînes. 

Vous pouvez également analyser une chaîne en la convertissant en une variable entière ou flottante. Bien que cela doive être catégorisé comme une opération de conversion de type, vous rencontrerez des ressources qui y font référence comme à l'analyse de chaînes. 

Dans cet article, vous apprendrez à analyser une chaîne en utilisant les méthodes `split()` et `strip()`. Vous apprendrez également à convertir une chaîne en un entier en utilisant la fonction `int()`.

## Comment analyser une chaîne en Python en utilisant la méthode `split()`

Vous pouvez utiliser la méthode `split()` en Python pour "diviser" les sous-chaînes d'une chaîne en une liste. 

Voici à quoi ressemble le paramètre : 

```txt
string.split(separator, maxsplit)
```

La méthode `split()` a deux paramètres optionnels :

* `separator` spécifie où commencer la division (vous comprendrez mieux cela avec les exemples dans la section suivante). 
* `maxsplit` spécifie le nombre maximum de divisions. 

### Exemple de la méthode `split()` #1 - Comment utiliser le paramètre Separator

```python
favorite_languages = "JavaScript, Python, and Java"

lang_split = favorite_languages.split(",")

print(lang_split)
# ['JavaScript', ' Python', ' and Java']

```

Dans l'exemple ci-dessus, nous avons créé une chaîne appelée `favorite_languages` qui contenait trois sous-chaînes : "JavaScript, Python, and Java". 

En utilisant la méthode `split()`, nous avons spécifié que chaque sous-chaîne devait être divisée après chaque virgule dans la chaîne : `favorite_languages.split(",")`. 

Le résultat était une liste de chaque sous-chaîne : ['JavaScript', ' Python', ' and Java']. 

Cet exemple montre comment utiliser le premier paramètre de la méthode `split()`. L'exemple suivant vous aidera à comprendre le deuxième paramètre. 

### Exemple de la méthode `split()` #2 - Comment utiliser le paramètre Maxsplit

```python
favorite_languages = "JavaScript, Python, and Java"

lang_split = favorite_languages.split(",", 1)

print(lang_split)
# ['JavaScript', ' Python, and Java']
```

Dans le code ci-dessus, nous avons utilisé le paramètre `maxsplit` qui spécifie le nombre de divisions à effectuer. 

Ainsi, `favorite_languages.split(",", 1)` signifie qu'une seule sous-chaîne doit être divisée, tandis que le reste resterait tel qu'il était dans la chaîne originale. 

Dans la sortie du code, seul JavaScript a été divisé, tandis que Python et Java ont conservé leurs positions initiales dans la chaîne. C'est-à-dire : `['JavaScript', ' Python, and Java']`. 

## Comment analyser une chaîne en Python en utilisant la méthode `strip()`

Vous pouvez utiliser la méthode `strip()` pour supprimer les espaces blancs ou les caractères spécifiés dans une chaîne.

Voici à quoi ressemble la syntaxe :

```python
string.strip([chars])
```

Le paramètre `chars` spécifie l'ensemble des caractères à supprimer. Ce paramètre est optionnel, donc laisser les parenthèses vides ne supprimera que les espaces blancs. 

Voyons quelques exemples.

### Exemple de la méthode `strip()` #1

```python
username = "       Doe      "

user = username.strip()

print(user) 
# Doe
```

Dans l'exemple ci-dessus, nous avions une chaîne avec des caractères d'espace blanc en début et en fin : "       Doe      ". 

En utilisant la méthode strip sans aucun paramètre, nous nous sommes débarrassés des espaces blancs : `username.strip()`. 

Dans l'exemple suivant, nous allons passer des paramètres à la méthode `strip()`. 

### Exemple de la méthode `strip()` #2

Dans cette section, nous allons utiliser une chaîne qui contient différents caractères qui ne sont pas des espaces blancs : 

```python
username = "=+---Doe---+="
```

L'objectif ici est de se débarrasser des caractères indésirables (=+-) trouvés dans la variable `username`.

Si vous utilisez la méthode `strip()` sans aucun paramètre, elle ne se débarrassera pas de ces caractères. Sans paramètres, la méthode `strip()` ne supprime que les espaces blancs. 

Pour supprimer les caractères dans la chaîne, vous devez les utiliser comme paramètre pour indiquer à la méthode `strip()` qu'ils doivent être supprimés. C'est-à-dire : 

```python
username = "=+---Doe---+="

user = username.strip("=+-")

print(user) 
# Doe
```

Dans le code ci-dessus, nous avons passé les caractères à supprimer de la chaîne en tant que paramètre à la méthode `strip()` : `username.strip("=+-")`. 

Notez que vous devez imbriquer ces caractères entre guillemets ("=+-").

## Comment convertir une chaîne en un entier en utilisant la fonction `int()`

La conversion de type de données vous aide à effectuer certaines opérations qui impliquent des types de données incompatibles. 

Par exemple, l'exemple ci-dessous montre ce qui se passe lorsque vous essayez d'additionner un entier et une chaîne : 

```python
age = "300"

print(age + 300) 
# TypeError: can only concatenate str (not "int") to str
```

Dans le code ci-dessus, nous avons créé une valeur de chaîne avec une valeur de "300". Lorsque nous avons essayé de l'ajouter à une valeur entière de 300, nous avons obtenu une erreur.

L'erreur est lancée parce que le compilateur suppose que nous essayons d'ajouter deux chaînes. [La concaténation de chaînes en Python](https://www.freecodecamp.org/news/python-concatenate-strings-how-to-combine-and-append-strings-in-python/) ne peut pas être effectuée en utilisant une chaîne et un entier. 

Pour résoudre ce problème, vous pouvez convertir la chaîne en un entier avant de l'utiliser dans une opération mathématique. 

Voici comment vous pouvez faire cela en utilisant la fonction `int()` :

```python
age = "300"

age_to_int = int(age)

print(age_to_int + 300) 
# 600
```

Dans le code ci-dessus, nous avons utilisé la fonction `int()` pour convertir la chaîne `age` en un entier : `int(age)`. 

Maintenant, vous devez utiliser la variable comme un entier. 

Un cas d'utilisation courant pour la conversion d'une chaîne en un entier est observé lors de la réception d'une entrée d'un utilisateur. Vous pouvez voir un exemple comme celui-ci dans [cet article](https://www.freecodecamp.org/news/python-convert-string-to-int-how-to-cast-a-string-in-python/#:~:text=A%20practical%20example%20of%20converting%20a%20string%20to%20an%20int).

## Résumé

Dans cet article, nous avons parlé de l'analyse de chaînes en Python. 

Nous avons vu des exemples qui montraient comment analyser une chaîne en utilisant les méthodes `split()` et `strip()`. 

Nous avons également vu comment convertir une chaîne en un entier en utilisant la fonction `int()`. 

Bonne programmation ! Je parle également de Python sur [mon blog](https://ihechikara.com/).