---
title: Python split() – Exemple de division de chaîne
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-05-11T23:12:18.000Z'
originalURL: https://freecodecamp.org/news/python-split-string-splitting-example
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/tania-melnyczuk-eIY9QaolhLg-unsplash--3-.jpg
tags:
- name: Python
  slug: python
seo_title: Python split() – Exemple de division de chaîne
seo_desc: "The split() method in Python splits characters in a string into separate\
  \ items in a list. \nIn this tutorial, we'll go over some examples to help you learn\
  \ how to use the split() method. We'll start from the syntax and then see how we\
  \ can modify the l..."
---

La méthode `split()` en Python divise les caractères d'une chaîne en éléments séparés dans une liste. 

Dans ce tutoriel, nous allons passer en revue quelques exemples pour vous aider à apprendre à utiliser la méthode `split()`. Nous commencerons par la syntaxe, puis nous verrons comment nous pouvons modifier la liste retournée en utilisant les paramètres de la méthode `split()`. 

## Syntaxe de la méthode `split()` en Python

La méthode `split()` prend deux paramètres. Voici à quoi ressemble la syntaxe :

```python
str.split(séparateur, maxsplit)
```

Les paramètres ci-dessus sont `separateur` et `maxsplit`. Ces paramètres sont tous deux optionnels, mais voyons ce qu'ils font.

`separateur` spécifie le caractère au niveau duquel la division se produit. Si non spécifié, les espaces blancs seront utilisés comme caractère par défaut où la division se produit. Vous comprendrez mieux cela dans les exemples des sections suivantes.

`maxsplit` spécifie le nombre maximum de divisions. La valeur par défaut est -1, ce qui permet un nombre continu de divisions. Cet argument est également optionnel.

## Comment utiliser la méthode `split()` sans paramètres

Dans cette section, nous allons voir quelques exemples de division de chaîne en utilisant la méthode `split()` sans passer de paramètres.

```python
myString = "Python est un langage de programmation"

print(myString.split())

# ['Python', 'est', 'un', 'langage', 'de', 'programmation']
```

Dans le code ci-dessus, nous avons créé une chaîne appelée `myString` avec cinq mots composant la chaîne : "Python est un langage de programmation".

Nous avons ensuite utilisé la méthode `split()` sur notre chaîne en utilisant la notation par point.

Lorsqu'elle est imprimée dans la console, chaque mot de la chaîne est devenu un élément séparé dans un type de données de liste : `['Python', 'est', 'un', 'langage', 'de', 'programmation']`. 

La méthode `split()` est capable de séparer chaque mot car, par défaut, les espaces blancs indiquent le point de division pour chaque caractère (voir le paramètre `separateur` dans la section précédente).

## Comment utiliser la méthode `split()` avec des paramètres

Dans cette section, nous allons comprendre comment utiliser les paramètres de la méthode `split()` avec des exemples.

```python
myString = "Bonjour le monde!, si vous lisez ceci, vous êtes génial"

print(myString.split(", "))

# ['Bonjour le monde!', "si vous lisez ceci", "vous êtes génial"]
```

Dans l'exemple ci-dessus, nous avons passé une virgule (,) comme `separateur` : `myString.split(", ")`. 

Ainsi, au lieu de diviser les caractères après chaque espace blanc, les caractères ne seront divisés que lorsqu'une virgule apparaît : `['Bonjour le monde!', "si vous lisez ceci", "vous êtes génial"]`. Cela signifie que les caractères qui apparaissent avant une virgule seront regroupés.

Dans l'exemple suivant, nous allons travailler avec le deuxième paramètre – `maxsplit`.

```
myString = "Bonjour le monde!, si vous lisez ceci, vous êtes génial"

print(myString.split(", ", 0))

# ["Bonjour le monde!, si vous lisez ceci, vous êtes génial"]
```

Nous avons ajouté une valeur `maxsplit` de 0 dans le code ci-dessus. Cela contrôle la façon dont la chaîne est divisée. 0 implique 1, donc les caractères sont retournés comme un seul élément dans une liste : `["Bonjour le monde!, si vous lisez ceci, vous êtes génial"]`

Changeons le nombre et voyons ce qui se passe

```python
myString = "Bonjour le monde!, si vous lisez ceci, vous êtes génial"

print(myString.split(", ", 1))

# ['Bonjour le monde!', "si vous lisez ceci, vous êtes génial"]
```

Maintenant que nous avons changé le nombre à 1, les caractères sont divisés en deux éléments dans la liste – 'Bonjour le monde!' et "si vous lisez ceci, vous êtes génial".

Omettre la valeur `maxsplit` la définira à -1 par défaut. Cette valeur négative permet aux méthodes `split()` de diviser chaque caractère en continu en éléments séparés jusqu'à ce qu'il n'y ait plus de caractères. Si un `separateur` est spécifié, la division sera effectuée en fonction de cette valeur – sinon, les espaces blancs seront utilisés.

## Conclusion

Dans cet article, nous avons parlé de la méthode `split()` en Python qui divise les caractères d'une chaîne et les retourne sous forme d'éléments dans une liste.

Nous avons vu la syntaxe de la méthode `split()` et les deux paramètres fournis par défaut – les paramètres `separateur` et `maxsplit`.

Nous avons également vu quelques exemples divisés en deux sections. La première section a montré comment utiliser la méthode `split()` sans paramètres, tandis que la deuxième a montré comment nous utiliserions les paramètres de la méthode pour obtenir des résultats variés.

Bon codage !