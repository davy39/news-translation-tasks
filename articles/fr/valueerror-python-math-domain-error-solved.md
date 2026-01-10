---
title: 'ValueError: math domain error [Résolu Erreur Python]'
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2023-02-22T16:11:13.000Z'
originalURL: https://freecodecamp.org/news/valueerror-python-math-domain-error-solved
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/python-math-domain-error.png
tags:
- name: error
  slug: error
- name: Python
  slug: python
seo_title: 'ValueError: math domain error [Résolu Erreur Python]'
seo_desc: "In mathematics, there are certain operations that are considered to be\
  \ mathematically undefined operations. \nSome examples of these undefined operations\
  \ are:\n\nThe square root of a negative number (√-2). \nA divisor with a value of\
  \ zero (20/0). \n\nThe \"..."
---

En mathématiques, il existe certaines opérations qui sont considérées comme des opérations mathématiquement non définies. 

Voici quelques exemples de ces opérations non définies :

* La racine carrée d'un nombre négatif (√-2). 
* Un diviseur avec une valeur de zéro (20/0). 

L'erreur "ValueError: math domain error" en Python se produit lorsque vous effectuez une opération mathématique qui sort du domaine de l'opération.

En termes simples, cette erreur se produit en Python lorsque vous effectuez une opération mathématique avec des valeurs mathématiquement non définies. 

Dans cet article, vous apprendrez à corriger l'erreur "ValueError: math domain error" en Python. 

Vous commencerez par apprendre la signification des mots-clés trouvés dans le message d'erreur. Vous verrez ensuite des exemples de code pratiques qui génèrent l'erreur et une solution pour chaque exemple. 

Commençons !

## Comment corriger l'erreur "ValueError: math domain error" en Python

Une `ValueError` est générée lorsqu'une fonction ou une opération reçoit un paramètre avec une valeur invalide. 

Un domaine en mathématiques est l'ensemble de toutes les valeurs possibles qu'une fonction peut accepter. Toutes les valeurs qui sortent du domaine sont considérées comme "non définies" par la fonction. 

Ainsi, le message `math domain error` signifie simplement que vous utilisez une valeur qui sort du domaine accepté d'une fonction.

Voici quelques exemples :

### Exemple #1 – Erreur de domaine mathématique Python avec `math.sqrt`

```python
import math

print(math.sqrt(-1))
# ValueError: math domain error
```

Dans le code ci-dessus, nous utilisons la méthode `sqrt` du module `math` pour obtenir la racine carrée d'un nombre. 

Nous obtenons l'erreur "ValueError: math domain error" car -1 sort de la plage des nombres dont la racine carrée peut être obtenue mathématiquement. 

### Solution #1 – Erreur de domaine mathématique Python avec `math.sqrt`

Pour corriger cette erreur, utilisez simplement une instruction `if` pour vérifier si le nombre est négatif avant de procéder à la recherche de la racine carrée. 

Si le nombre est supérieur ou égal à zéro, alors le code peut être exécuté. Sinon, un message sera affiché pour informer l'utilisateur qu'un nombre négatif ne peut pas être utilisé. 

Voici un exemple de code :

```python
import math

number = float(input('Entrez un nombre : '))

if number >= 0:
    print(f'La racine carrée de {number} est {math.sqrt(number)}')
else: 
    print('Impossible de trouver la racine carrée d\'un nombre négatif')
```

### Exemple #2 – Erreur de domaine mathématique Python avec `math.log`

Vous utilisez la méthode `math.log` pour obtenir le logarithme d'un nombre. Tout comme la méthode `sqrt`, vous ne pouvez pas obtenir le logarithme d'un nombre négatif. 

De plus, vous ne pouvez pas obtenir le logarithme du nombre 0. Nous devons donc modifier la condition de l'instruction `if` pour vérifier cela. 

Voici un exemple qui génère l'erreur :

```python
import math

print(math.log(0))
# ValueError: math domain error
```

### Solution #2 – Erreur de domaine mathématique Python avec `math.log`

```python
import math

number = float(input('Entrez un nombre : '))

if number > 0:
    print(f'Le logarithme de {number} est {math.log(number)}')
else: 
    print('Impossible de trouver le logarithme de 0 ou d\'un nombre négatif')
```

Dans le code ci-dessus, nous utilisons la condition de l'instruction `if` pour nous assurer que le nombre saisi par l'utilisateur n'est ni zéro ni un nombre négatif (le nombre doit être supérieur à zéro).

### Exemple #3 – Erreur de domaine mathématique Python avec `math.acos`

Vous utilisez la méthode `math.acos` pour trouver la valeur de l'arc cosinus d'un nombre. 

Le domaine de la méthode `acos` est de -1 à 1, donc toute valeur qui sort de cette plage générera l'erreur "ValueError: math domain error". 

Voici un exemple :

```python
import math

print(math.acos(2))
# ValueError: math domain error
```

### Solution #3 – Erreur de domaine mathématique Python avec `math.acos`

```python
import math

number = float(input('Entrez un nombre : '))

if -1 <= number <= 1:
    print(f'L\'arc cosinus de {number} est {math.acos(number)}')
else:
    print('Veuillez entrer un nombre entre -1 et 1.')

```

Tout comme la solution dans les autres exemples, nous utilisons une instruction `if` pour nous assurer que le nombre saisi par l'utilisateur ne dépasse pas une certaine plage. 

C'est-à-dire que toute valeur qui sort de la plage de -1 à 1 demandera à l'utilisateur de saisir une valeur correcte. 

## Résumé

Dans cet article, nous avons parlé de l'erreur "ValueError: math domain error" en Python. 

Nous avons examiné des exemples de code qui génèrent l'erreur, et comment les vérifier et les corriger en utilisant une instruction `if`. 

Bon codage !