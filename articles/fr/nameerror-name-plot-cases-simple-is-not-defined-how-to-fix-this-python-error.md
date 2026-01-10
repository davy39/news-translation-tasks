---
title: 'NameError: Le nom plot_cases_simple n''est pas défini – Comment corriger cette
  erreur Python'
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-06-27T15:58:39.000Z'
originalURL: https://freecodecamp.org/news/nameerror-name-plot-cases-simple-is-not-defined-how-to-fix-this-python-error
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/brett-jordan-Ss3U6bEtKww-unsplash.jpg
tags:
- name: error handling
  slug: error-handling
- name: Python
  slug: python
seo_title: 'NameError: Le nom plot_cases_simple n''est pas défini – Comment corriger
  cette erreur Python'
seo_desc: "This first step in fixing a coding error is to understand the error. Although\
  \ some error messages may seem confusing, most of them will help you fix the error.\
  \ \nIn this article, we'll be talking about an error that falls under the NameError\
  \ category ..."
---

La première étape pour corriger une erreur de codage est de comprendre l'erreur. Bien que certains messages d'erreur puissent sembler confus, la plupart d'entre eux vous aideront à corriger l'erreur. 

Dans cet article, nous allons parler d'une erreur qui relève de la catégorie **NameError** en Python.

Vous verrez ce qu'est un **NameError**, quelques exemples de code pour montrer comment/pourquoi l'erreur se produit, et comment les corriger. 

## Qu'est-ce qu'un NameError en Python ?

En Python, le **NameError** se produit lorsque vous essayez d'utiliser une variable, une fonction ou un module qui n'existe pas ou qui n'a pas été utilisé de manière valide. 

Voici quelques-unes des erreurs courantes qui provoquent cette erreur :

* Utiliser une variable ou un nom de fonction qui n'a pas encore été défini.
* Faire une faute de frappe dans le nom d'une variable/fonction lors de l'appel de la variable/fonction. 
* Utiliser un module Python sans importer le module, et ainsi de suite.

## Comment corriger "NameError: Name Is Not Defined" en Python

Dans cette section, vous verrez comment corriger l'erreur "NameError: Name is Not Defined" en Python. 

J'ai divisé cette section en sous-sections pour montrer l'erreur ci-dessus lors de l'utilisation de variables, de fonctions et de modules.

Nous commencerons par des blocs de code qui déclenchent l'erreur, puis nous verrons comment les corriger.

### Exemple #1 - Le nom de la variable n'est pas défini en Python

```python
name = "John"

print(age)
# NameError: name 'age' is not defined
```

Dans le code ci-dessus, nous avons défini une variable `name` mais nous avons essayé d'imprimer `age` qui n'a pas encore été défini. 

Nous avons obtenu une erreur qui dit : `NameError: name 'age' is not defined` pour montrer que la variable `age` n'existe pas. 

Pour corriger cela, nous pouvons créer la variable et notre code fonctionnera correctement. Voici comment :

```python
name = "John"
age = 12

print(age)
# 12
```

Maintenant, la valeur de `age` est imprimée. 

De même, la même erreur peut être déclenchée lorsque nous faisons une faute de frappe dans le nom d'une variable. Voici un exemple :

```python
name = "John"

print(nam)
# NameError: name 'nam' is not defined
```

Dans le code ci-dessus, nous avons écrit `nam` au lieu de `name`. Pour corriger des erreurs comme celle-ci, vous devez simplement orthographier correctement le nom de la variable. 

### Exemple #2 - Le nom de la fonction n'est pas défini en Python

```python
def sayHello():
    print("Hello World!")
    
sayHelloo()
# NameError: name 'sayHelloo' is not defined
```

Dans l'exemple ci-dessus, nous avons ajouté un o supplémentaire lors de l'appel de la fonction — `sayHelloo()` au lieu de `sayHello()`.

Nous avons obtenu l'erreur : `NameError: name 'sayHelloo' is not defined`. Les erreurs d'orthographe comme celle-ci sont très faciles à manquer. Le message d'erreur aide généralement à corriger cela. 

Voici la bonne façon d'appeler la fonction :

```python
def sayHello():
    print("Hello World!")
    
sayHello()
# Hello World!

```

Comme nous l'avons vu dans la section précédente, l'appel d'une variable qui n'a pas encore été définie déclenche une erreur. Il en va de même pour les fonctions. 

Voici un exemple :

```python
def sayHello():
    print("Hello World!")
    
sayHello()
# Hello World!

addTWoNumbers()
# NameError: name 'addTWoNumbers' is not defined
```

Dans le code ci-dessus, nous avons appelé une fonction — `addTWoNumbers()` — qui n'avait pas encore été définie dans le programme. Pour corriger cela, vous pouvez créer la fonction si vous en avez besoin ou simplement supprimer la fonction si elle est sans importance. 

Notez que l'appel d'une fonction avant de la créer déclenchera la même erreur. C'est-à-dire :

```python
sayHello()

def sayHello():
    print("Hello World!")
    
# NameError: name 'sayHello' is not defined
```

Vous devez donc toujours définir vos fonctions avant de les appeler.

### Exemple #3 - Utilisation d'un module sans importer le module en Python

```python
x = 5.5

print(math.ceil(x))
# NameError: name 'math' is not defined
```

Dans l'exemple ci-dessus, nous utilisons la méthode `math.ceil` de Python sans importer le module `math`. 

L'erreur résultante était : `NameError: name 'math' is not defined`. Cela s'est produit parce que l'interpréteur n'a pas reconnu le mot-clé `math`.

Avec d'autres méthodes mathématiques en Python, nous devons d'abord importer le module `math` pour l'utiliser. 

Voici une correction :

```python
import math

x = 5.5

print(math.ceil(x))
# 6
```

Dans la première ligne du code, nous avons importé le module `math`. Maintenant, lorsque vous exécutez le code ci-dessus, vous devriez obtenir 6 en retour. 

## Résumé

Dans cet article, nous avons parlé de l'erreur "NameError: Name is Not Defined" en Python. 

Nous avons d'abord défini ce qu'est un **NameError** en Python. 

Nous avons ensuite vu quelques exemples qui pourraient déclencher un **NameError** lors de l'utilisation de variables, de fonctions et de modules en Python. Chaque exemple, divisé en sections, a montré comment corriger les erreurs. 

Bon codage !