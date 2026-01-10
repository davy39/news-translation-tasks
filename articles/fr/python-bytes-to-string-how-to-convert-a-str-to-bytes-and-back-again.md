---
title: Exposant en Python – Fonction de puissance et exposants à l'aide d'une boucle
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-02-14T17:54:02.000Z'
originalURL: https://freecodecamp.org/news/python-bytes-to-string-how-to-convert-a-str-to-bytes-and-back-again
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/21.-exponents.png
tags:
- name: Math
  slug: math
- name: Python
  slug: python
seo_title: Exposant en Python – Fonction de puissance et exposants à l'aide d'une
  boucle
seo_desc: 'By Dillion Megida

  The exponent of a number refers to the power to which that number should be raised.
  In this article, I''ll show you how to find exponents using two ways: the power
  function and a loop.

  Exponents are usually written like this: Baseexp...'
---

Par Dillion Megida

L'exposant d'un nombre fait référence à la puissance à laquelle ce nombre doit être élevé. Dans cet article, je vais vous montrer comment trouver des exposants en utilisant deux méthodes : la fonction de puissance et une boucle.

Les exposants sont généralement écrits comme ceci : **Base<sup>exposant</sup>**

Prenons un exemple comme **10<sup>3</sup>**. Cela signifie "10, élevé à la puissance de 3". Le résultat de ceci est évalué comme `10 * 10 * 10` (10 multiplié par lui-même 3 fois), ce qui donne `1000`.

Il existe différentes façons d'évaluer l'exposant d'un nombre (le nombre est appelé la base). Une façon est d'utiliser l'opérateur `**`. Avec cet opérateur, vous avez le nombre, suivi de l'opérateur, puis l'exposant comme ceci `10 ** 3` qui est 10<sup>3</sup>

Mais dans cet article, je vais vous montrer deux autres façons, qui sont la fonction `pow` et l'utilisation d'une boucle.

## Exposants avec la fonction `pow`

`pow` est une fonction intégrée en Python pour évaluer un nombre élevé à un exposant. La syntaxe de cette fonction est :

```python
pow(base, exposant, modulo)
```

Cette fonction accepte trois arguments :
* `base` : le nombre qui sera élevé
* `exposant` : la puissance à laquelle le nombre sera élevé
* `modulo` : un nombre optionnel qui évalue le reste lorsque le nombre élevé est divisé par celui-ci

Le dernier argument est optionnel, mais selon la [documentation Python sur pow](https://docs.python.org/2/library/functions.html#pow), cet argument calcule plus efficacement que `pow(base, exposant) % nombre`.

Voyons quelques exemples :

```python
resultat1 = pow(100, 3)
print(resultat1) # 1000000

resultat2 = pow(5, 4)
print(resultat2) # 625

resultat3 = pow(3, 2, 5)
print(resultat3) # 4
```

Dans le dernier exemple, nous avons `pow(3, 2, 5)`. Ce qui se passe ici, c'est que 3 est d'abord élevé à la puissance de 2, ce qui donne 9. Ensuite, 9 est divisé par 5, et le reste, qui est retourné, est `4`.

Notez qu'il existe également une fonction `Math.pow` en Python. La différence entre celle-ci et pow(), c'est que `pow()` ne retournera un nombre à virgule flottante que lorsque le nombre est un float. Elle retournera un entier si le nombre est entier. Mais `math.pow()` retourne toujours un nombre à virgule flottante.

## Exposants avec une boucle

Vous pouvez utiliser n'importe quel type de boucle pour y parvenir, mais pour cet article, j'utiliserai une boucle `while`.

La syntaxe pour une boucle `while` est :

```python
while condition:
  # code à exécuter
```

Pour les exposants, je peux mettre cette boucle dans une fonction comme ceci :

```python
def loopExp(nombre, exp):
  resultat = nombre
  compteur = 1
  
  while compteur < exp:
    resultat *= nombre
    compteur += 1
   
  return resultat
```

Ici, nous avons défini une fonction `loopExp` qui prend deux entrées : `nombre` et `exp` qui signifie exposant.

Dans la fonction, nous initialisons les variables `resultat` et `compteur` avec la valeur de `nombre` et `1` respectivement. Ensuite, nous avons la boucle `while` qui s'exécute tant que la variable `compteur` est inférieure à l'entrée `exp`.

À chaque itération de la boucle, nous mettons à jour la variable `resultat` en multipliant la valeur précédente de `resultat` par l'entrée `nombre`. Nous incrémentons également la variable `compteur` de 1. Ensuite, nous retournons la variable `resultat`.

Voyons cette fonction en action :

```python
resultat1 = loopExp(100, 3)
print(resultat1) # 1000000

resultat2 = loopExp(5, 4)
print(resultat2) # 625

resultat3 = loopExp(3, 2)
print(resultat3) # 9
```

Comme vous pouvez le voir dans les résultats, nous avons les exposants calculés en utilisant la boucle dans la fonction `loopExp`.

## Conclusion

Dans cet article, je vous ai montré comment évaluer les exposants de différentes manières. J'ai utilisé des exemples pour vous montrer l'opérateur `**`, les fonctions `pow` et `Math.pow`, ainsi que l'utilisation d'une boucle.

N'hésitez pas à partager ceci si vous trouvez cela utile :)