---
title: Variable Globale en Python – Variables Non-Locales en Python
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-06-10T21:21:45.000Z'
originalURL: https://freecodecamp.org/news/global-variable-in-python-non-local-python-variables
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/kevin-ku-w7ZyuGYNpRQ-unsplash.jpg
tags:
- name: Python
  slug: python
- name: variables
  slug: variables
seo_title: Variable Globale en Python – Variables Non-Locales en Python
seo_desc: "In Python and most programming languages, variables declared outside a\
  \ function are known as global variables. You can access such variables inside and\
  \ outside of a function, as they have global scope. \nHere's an example of a global\
  \ variable:\nx = 10 ..."
---

En Python et dans la plupart des langages de programmation, les variables déclarées en dehors d'une fonction sont appelées variables globales. Vous pouvez accéder à ces variables à l'intérieur et à l'extérieur d'une fonction, car elles ont une portée globale. 

Voici un exemple de variable globale :

```python
x = 10 

def showX():
    print("La valeur de x est", x)
    
showX()
# La valeur de x est 10
```

La variable `x` dans le code ci-dessus a été déclarée en dehors d'une fonction : `x = 10`. 

En utilisant la fonction `showX()`, nous avons pu accéder à `x` car elle a été déclarée dans une portée globale. 

Regardons un autre exemple qui montre ce qui se passe lorsque nous déclarons une variable à l'intérieur d'une fonction et essayons d'y accéder ailleurs.

```python
def X():
    x = 10 

X()

def showX():
    print("La valeur de x est", x)
    
showX()
NameError: name 'x' is not defined
```

Dans l'exemple ci-dessus, nous avons déclaré `x` à l'intérieur d'une fonction et avons essayé d'y accéder dans une autre fonction. Cela a entraîné une erreur NameError car `x` n'était pas défini globalement. 

Les variables définies à l'intérieur des fonctions sont appelées variables locales. Leur valeur ne peut être utilisée que dans la fonction où elles sont déclarées. 

Vous pouvez changer la portée d'une variable locale en utilisant le mot-clé `global` – ce que nous allons discuter dans la section suivante.

## À quoi sert le mot-clé `global` en Python ?

Le mot-clé global est principalement utilisé pour deux raisons :

* Pour modifier la valeur d'une variable globale.
* Pour rendre une variable locale accessible en dehors de la portée locale. 

Regardons quelques exemples pour chaque scénario afin de mieux comprendre. 

### Exemple #1 - Modifier une Variable Globale en Utilisant le Mot-Clé `global`

Dans la dernière section où nous avons déclaré une variable globale, nous n'avons pas essayé de changer la valeur de la variable. Tout ce que nous avons fait, c'est accéder et imprimer sa valeur dans une fonction. 

Essayons de changer la valeur d'une variable globale et voyons ce qui se passe :

```python
x = 10 

def showX():
    x = x + 2
    print("La valeur de x est", x)
    
showX()
# local variable 'x' referenced before assignment
```

Comme vous pouvez le voir ci-dessus, lorsque nous avons essayé d'ajouter 2 à la valeur de `x`, nous avons obtenu une erreur. Cela est dû au fait que nous pouvons seulement accéder à `x` mais pas la modifier. 

Pour corriger cela, nous utilisons la variable `global`. Voici comment :

```python
x = 10 

def showX():
    global x
    x = x + 2
    print("La valeur de x est", x)
    
showX()
# La valeur de x est 12
```

En utilisant le mot-clé `global` dans le code ci-dessus, nous avons pu modifier `x` et ajouter 2 à sa valeur initiale. 

### Exemple #2 - Comment Rendre une Variable Locale Accessible en Dehors de la Portée Locale en Utilisant le Mot-Clé `global`

Lorsque nous avons créé une variable à l'intérieur d'une fonction, il n'était pas possible d'utiliser sa valeur à l'intérieur d'une autre fonction car le compilateur ne reconnaissait pas la variable.

Voici comment nous pouvons corriger cela en utilisant le mot-clé `global` :

```python
def X():
    global x
    x = 10 
    
X()
    
def showX():
    print("La valeur de x est", x)
    
showX()
# La valeur de x est 10
```

Pour rendre possible l'accès à `x` en dehors de sa portée locale, nous l'avons déclaré en utilisant le mot-clé `global` : `global x`. 

Après cela, nous avons assigné une valeur à `x`. Nous avons ensuite appelé la fonction que nous avons utilisée pour la déclarer : `X()`

Lorsque nous avons appelé la fonction `showX()`, qui imprime la valeur de `x` déclarée dans la fonction `X()`, nous n'avons pas obtenu d'erreur car `x` a une portée globale. 

## Résumé

Dans cet article, nous avons parlé des variables globales et locales en Python.

Les exemples ont montré comment déclarer des variables globales et locales. 

Nous avons également parlé du mot-clé `global` qui vous permet de modifier la valeur d'une variable globale ou de rendre une variable locale accessible en dehors de sa portée. 

Bon codage !