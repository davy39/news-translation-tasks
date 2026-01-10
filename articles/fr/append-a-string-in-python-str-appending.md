---
title: Ajouter une chaîne de caractères en Python – Ajout de chaînes
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-10-18T19:33:59.000Z'
originalURL: https://freecodecamp.org/news/append-a-string-in-python-str-appending
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/alex-chumak-zGuBURGGmdY-unsplash.jpg
tags:
- name: Python
  slug: python
seo_title: Ajouter une chaîne de caractères en Python – Ajout de chaînes
seo_desc: "In this article, you'll learn the different methods of appending strings\
  \ in Python. \nAnother term commonly used when talking about appending strings is\
  \ concatenation. So you'll often see these terms — append and concatenate — used\
  \ interchangeably. \nE..."
---

Dans cet article, vous apprendrez les différentes méthodes pour ajouter des chaînes de caractères en Python. 

Un autre terme couramment utilisé lorsqu'on parle d'ajout de chaînes est la concaténation. Vous verrez donc souvent ces termes — ajouter et concaténer — utilisés de manière interchangeable. 

Dans les deux cas, ajouter ou concaténer des chaînes signifie ajouter ou joindre la valeur d'une chaîne à une autre chaîne.  

Examinons les différentes façons de procéder avec des exemples de code simples. 

## Comment ajouter une chaîne de caractères en Python en utilisant l'opérateur `+`

Vous pouvez utiliser l'opérateur `+` pour ajouter deux chaînes ou plus. Voici un exemple :

```python
first_name = "John"
last_name = "Doe"

print(first_name + last_name)
# JohnDoe
```

Dans l'exemple ci-dessus, nous avons créé deux variables de chaîne — `first_name` et `last_name`. Elles avaient respectivement les valeurs "John" et "Doe". 

Pour ajouter ces variables, nous avons utilisé l'opérateur `+` : `first_name + last_name`. 

Vous remarquerez dans la sortie que nous avons obtenu les deux variables jointes sans aucun espace : `JohnDoe`. 

Vous pouvez ajouter un espace après la valeur `first_name` : "John ". Ou avant la valeur `last_name` : " Doe". C'est-à-dire : 

```python
first_name = "John "
last_name = "Doe"

print(first_name + last_name)
# John Doe
```

Vous pouvez également ajouter un espace en utilisant des guillemets lors de l'ajout des chaînes. Voici comment : 

```python
first_name = "John "
last_name = "Doe"

print(first_name + " " + last_name)
# John Doe
```

## Comment ajouter une chaîne de caractères en Python en utilisant la méthode `join()`

Une autre façon d'ajouter des chaînes en Python est d'utiliser la méthode `join()`.

La méthode `join()` prend un objet itérable — Listes, Tuples, Chaînes, Ensembles, Dictionnaires — comme paramètre. Voici à quoi ressemble la syntaxe :

```python
string.join(iterable_object)
```

Voici un exemple montrant comment utiliser la méthode `join()` pour ajouter des chaînes : 

```python
first_name = "John"
last_name = "Doe"

print("".join([first_name, last_name]))
# JohnDoe
```

Ici, nous avons passé nos deux variables de chaîne comme paramètres à la méthode `join()`. 

Vous remarquerez également que les variables étaient imbriquées dans des crochets `[]`, ce qui en fait une liste de chaînes : `[first_name, last_name]`. Cela est dû au fait que la méthode ne prend qu'un seul paramètre qui doit être un objet itérable. 

Une chose étrange à propos de la méthode `join()` est les guillemets qui précèdent le point. 

Vous pouvez utiliser ces guillemets pour indiquer ce qui apparaît entre les éléments de vos valeurs d'objet itérable. Permettez-moi de démontrer avec un exemple. 

```python
first_name = "John"
last_name = "Doe"

print("#".join([first_name, last_name]))
# John#Doe
```

Dans l'exemple ci-dessus, j'ai ajouté le symbole `#` aux guillemets : `"#".join([first_name, last_name])`. Ce `#` a été ajouté entre nos chaînes : `John#Doe`. 

Dans la dernière section, nous avons dû utiliser différentes méthodes pour ajouter un espace entre nos chaînes. Vous pouvez y parvenir facilement en ajoutant un espace dans les guillemets qui précèdent la méthode `join()` : 

```python
first_name = "John"
last_name = "Doe"

print(" ".join([first_name, last_name]))
# John Doe
```

## Comment ajouter une chaîne de caractères en Python en utilisant la méthode `format()` de chaîne

Voici à quoi ressemble la syntaxe de la méthode `format()` de chaîne : 

```txt
{}.format(value)
```

En gros, la méthode de formatage de chaîne prend le paramètre `value` dans la syntaxe ci-dessus et l'insère dans l'accolade. La valeur résultante sera une chaîne.

Voici un exemple :

```python
first_name = "John"
last_name = "Doe"

print("{} {}".format(first_name, last_name))
# John Doe
```

Puisque nous avons fourni deux accolades dans l'exemple et deux paramètres (`first_name` et `last_name`), la méthode `format()` de chaîne insère les chaînes dans leurs accolades respectives. 

Vous pouvez ajouter plus de chaînes dans les guillemets où vous trouvez les accolades. Cela ne modifiera pas le fonctionnement de la méthode `format()` de chaîne — les chaînes seront toujours insérées dans les accolades. C'est-à-dire : 

```python
first_name = "John"
last_name = "Doe"

print("My name is {} {}".format(first_name, last_name))
# My name is John Doe
```

## Comment ajouter une chaîne de caractères en Python en utilisant les f-strings

Cette méthode est assez facile à comprendre. Les f-strings ont été introduites en Python pour faciliter le formatage et l'interpolation des chaînes. Mais vous pouvez également les utiliser pour ajouter des chaînes. 

Pour utiliser les f-strings, vous écrivez simplement un f suivi de guillemets : `f""`. Vous pouvez ensuite insérer des chaînes et des noms de variables entre les guillemets. Tous les noms de variables doivent être imbriqués dans des accolades. 

Voici un exemple :

```python
first_name = "John"
last_name = "Doe"

print(f"{first_name} {last_name}")
# John Doe
```

## Résumé

Dans cet article, nous avons discuté des différentes méthodes que vous pouvez utiliser pour ajouter des chaînes en Python. 

Ajouter une chaîne à une autre signifie les joindre ensemble. 

Comme discuté dans cet article, avec des exemples de code, vous pouvez ajouter des chaînes en Python en utilisant l'opérateur `+`, la méthode `join()`, la méthode `format()` de chaîne et les f-strings. 

Bon codage !