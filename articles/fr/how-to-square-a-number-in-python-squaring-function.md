---
title: Comment élever un nombre au carré en Python – Fonction de mise au carré
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-05-31T15:03:14.000Z'
originalURL: https://freecodecamp.org/news/how-to-square-a-number-in-python-squaring-function
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/square-number-python.png
tags:
- name: Math
  slug: math
- name: Python
  slug: python
seo_title: Comment élever un nombre au carré en Python – Fonction de mise au carré
seo_desc: "By Dillion Megida\nTo square a number, you multiply that number by itself.\
  \ And there are multiple ways to do this in Python. \nYou can directly multiple\
  \ a number by itself (number * number) but in this article, I'll show you three\
  \ ways you can do this ..."
---

Par Dillion Megida

Pour élever un nombre au carré, vous multipliez ce nombre par lui-même. Et il existe plusieurs façons de le faire en Python. 

Vous pouvez multiplier directement un nombre par lui-même (**nombre * nombre**), mais dans cet article, je vais vous montrer trois façons de le faire sans coder en dur les deux nombres.

Les trois méthodes sont :
* **, l'opérateur de puissance
* la fonction intégrée `pow()`
* la fonction `math.pow()` du module `math`

## Comment utiliser l'opérateur de puissance (**) en Python

`**` est appelé l'opérateur de puissance. Vous l'utilisez pour élever un nombre à une puissance spécifiée. Voici la syntaxe :

```Python
nombre ** exposant
```

L'expression ci-dessus est évaluée comme **nombre * nombre...** (autant de fois que la valeur de l'exposant). Vous pouvez également lire l'expression comme **5<sup>2</sup>**.

En utilisant cet opérateur, vous pouvez trouver le carré d'un nombre en utilisant **2** comme exposant. Par exemple, pour trouver le carré de 5, vous pouvez faire ceci :

```Python
carre = 5 ** 2

print(carre)
# 25
```

L'opérateur de puissance évalue l'expression comme **5 * 5**, ce qui donne 25.

## Comment utiliser la fonction `pow()` en Python

Python dispose d'une fonction intégrée `pow()`, qui évalue un nombre à la puissance d'un autre nombre. Voici la syntaxe :

```Python
pow(base, exposant)
// interprété comme ^3
```

Le code ci-dessus est interprété comme base<sup>exposant</sup>.

La fonction accepte deux arguments : le nombre à élever (appelé la **base**) et la puissance à laquelle le nombre doit être élevé (l'**exposant**).
    
Pour trouver le carré d'un nombre en utilisant cette fonction, le nombre sera la base, et l'exposant sera **2**, ce qui signifie nombre<sup>2</sup>.
    
Pour trouver le carré de **5**, par exemple, vous pouvez utiliser cette fonction comme ceci :
    
```Python
carre = pow(5, 2)
    
print(carre)
# 25
```
    
La fonction `pow()` accepte également un troisième argument : le **modulo**. Le signe pour modulo est **%**. Cet argument évalue le reste lorsque une valeur est divisée par une autre.
    
Par exemple, **5 % 2** donne **1** car 5 divisé par 2 est 2, reste 1.
    
Appliquer le modulo à la fonction `pow()` ressemble à ceci :
    
```python
mod = pow(5, 2, 3)

print(mod)
## 1
## 5 * 5 est 25
## 25 % 3 est 1
```
    
Selon la [documentation Python sur pow](https://docs.python.org/2/library/functions.html#pow), cette approche calcule plus efficacement que `pow(5,2) % 3`
    
## Comment utiliser la fonction math.pow() en Python
    
`math.pow()` provient du module `math` de Python. Cette fonction est similaire à la fonction intégrée `pow()` en termes d'utilisation et de syntaxe, sauf qu'elle présente deux différences :

* elle n'accepte que deux arguments : la **base** et l'**exposant**
* elle retourne toujours un nombre à virgule flottante même lorsque le nombre élevé est un nombre entier.

Ainsi, `math.pow(5, 2)` retourne **25.0**.

`pow()` ne retournera un nombre à virgule flottante que si le nombre est un float. Elle retournera un entier si le nombre est entier. Mais `math.pow()` retourne toujours un nombre à virgule flottante.

Vous savez maintenant comment élever des nombres au carré en Python ! Merci d'avoir lu.