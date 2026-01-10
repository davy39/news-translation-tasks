---
title: Fonctions imbriquées en Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-06T00:54:00.000Z'
originalURL: https://freecodecamp.org/news/nested-functions-in-python
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e24740569d1a4ca3b94.jpg
tags:
- name: Python
  slug: python
- name: toothbrush
  slug: toothbrush
seo_title: Fonctions imbriquées en Python
seo_desc: 'A nested function is simply a function within another function, and is
  sometimes called an "inner function". There are many reasons why you would want
  to use nested functions, and we''ll go over the most common in this article.

  How to define a nested ...'
---

Une fonction imbriquée est simplement une fonction à l'intérieur d'une autre fonction, et est parfois appelée une "fonction interne". Il existe de nombreuses raisons pour lesquelles vous pourriez vouloir utiliser des fonctions imbriquées, et nous allons passer en revue les plus courantes dans cet article.

### Comment définir une fonction imbriquée

Pour définir une fonction imbriquée, il suffit d'initialiser une autre fonction à l'intérieur d'une fonction en utilisant le mot-clé `def` :

```py
def greeting(first, last):
  # fonction helper imbriquée
  def getFullName():
    return first + " " + last

  print("Hi, " + getFullName() + "!")

greeting('Quincy', 'Larson')
```

**Sortie :**

```sh
Hi, Quincy Larson!
```

Comme vous pouvez le voir, la fonction imbriquée `getFullName` a accès aux paramètres de la fonction externe `greeting`, `first` et `last`. Il s'agit d'un cas d'utilisation courant pour les fonctions imbriquées : servir de petite fonction helper à une fonction externe plus complexe.

## Raisons d'utiliser des fonctions imbriquées

Bien qu'il existe de nombreuses raisons valables d'utiliser des fonctions imbriquées, parmi les plus courantes figurent l'encapsulation et les fermetures / fonctions d'usine.

### Encapsulation des données

Il arrive que vous souhaitiez empêcher une fonction ou les données auxquelles elle a accès d'être accessibles depuis d'autres parties de votre code, vous pouvez donc l'_encapsuler_ dans une autre fonction.

Lorsque vous imbriquez une fonction de cette manière, elle est masquée de la portée globale. En raison de ce comportement, l'encapsulation des données est parfois appelée **masquage de données** ou **confidentialité des données**. Par exemple :

```py
def outer():
  print("Je suis la fonction externe.")
  def inner():
    print("Et je suis la fonction interne.")
  inner()

inner()
```

**Sortie :**

```sh
Traceback (most recent call last):
  File "main.py", line 16, in <module>
    inner()
NameError: name 'inner' is not defined
```

Dans le code ci-dessus, la fonction `inner` n'est disponible que depuis l'intérieur de la fonction `outer`. Si vous essayez d'appeler `inner` depuis l'extérieur de la fonction, vous obtiendrez l'erreur ci-dessus.

Au lieu de cela, vous devez appeler la fonction `outer` comme suit :

```py
def outer():
  print("Je suis la fonction externe.")
  def inner():
    print("Et je suis la fonction interne.")
  inner()

outer()
```

**Sortie :**

```sh
Je suis la fonction externe.
Et je suis la fonction interne.
```

### Fermetures

Mais que se passerait-il si la fonction externe retournait la fonction interne elle-même, plutôt que de l'appeler comme dans l'exemple ci-dessus ? Dans ce cas, vous auriez ce qu'on appelle une fermeture.

Les conditions suivantes doivent être remplies pour créer une fermeture en Python :

Voici les conditions nécessaires pour créer une fermeture en Python :

> 1. Il doit y avoir une fonction imbriquée  
>   
> 2. La fonction interne doit faire référence à une valeur définie dans la portée englobante  
>   
> 3. La fonction englobante doit retourner la fonction imbriquée  
>   
> - Source : [https://stackabuse.com/python-nested-functions/](https://stackabuse.com/python-nested-functions/)

Voici un exemple simple de fermeture :

```py
def num1(x):
  def num2(y):
    return x + y
  return num2

print(num1(10)(5))
```

**Sortie :**

```sh
15
```

Les fermetures permettent de passer des données aux fonctions internes sans d'abord les passer aux fonctions externes avec des paramètres comme dans l'exemple `greeting` au début de l'article. Elles permettent également d'invoquer la fonction interne depuis l'extérieur de la fonction externe encapsulante. Tout cela avec l'avantage de l'encapsulation/masquage des données mentionné précédemment.

Maintenant que vous comprenez comment et pourquoi imbriquer des fonctions en Python, allez-y et imbriquez-les avec les meilleurs.