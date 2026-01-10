---
title: Python Arrondir à un Entier – Comment Arrondir vers le Haut ou vers le Bas
  au Nombre Entier le Plus Proche
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-05-24T16:52:40.000Z'
originalURL: https://freecodecamp.org/news/how-to-round-numbers-up-or-down-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/volkan-olmez-aG-pvyMsbis-unsplash-1.jpg
tags:
- name: Math
  slug: math
- name: Python
  slug: python
seo_title: Python Arrondir à un Entier – Comment Arrondir vers le Haut ou vers le
  Bas au Nombre Entier le Plus Proche
seo_desc: "When working with float values (numbers with decimal values) in our Python\
  \ program, we might want to round them up or down, or to the nearest whole number.\
  \ \nIn this article, we'll see some built-in functionalities that let us round numbers\
  \ in Python...."
---

Lorsque nous travaillons avec des valeurs flottantes (nombres avec des décimales) dans notre programme Python, nous pouvons vouloir les arrondir vers le haut ou vers le bas, ou au nombre entier le plus proche. 

Dans cet article, nous verrons certaines fonctionnalités intégrées qui nous permettent d'arrondir des nombres en Python. Et nous verrons comment les utiliser avec quelques exemples.

Nous commencerons par la fonction `round()`. Par défaut, elle arrondit un nombre au nombre entier le plus proche. Nous verrons également comment utiliser les paramètres de la fonction pour changer le type de résultat retourné.

Nous parlerons ensuite des méthodes `math.ceil()` et `math.floor()` qui arrondissent respectivement un nombre vers le haut et vers le bas au nombre entier le plus proche. Ces deux méthodes proviennent du module intégré `math` en Python.

## Comment Utiliser la Fonction `round()` pour Arrondir au Nombre Entier le Plus Proche

La fonction `round()` prend deux paramètres. Voici à quoi ressemble la syntaxe :

```txt
round(nombre, chiffres_decimaux)
```

Le premier paramètre – `nombre` – est le nombre que nous arrondissons au nombre entier le plus proche.

Le deuxième paramètre – `chiffres_decimaux` – est le nombre de décimales à retourner. La valeur par défaut est 0.

Voyons quelques exemples.

```python
x = 2.56789

print(round(x))
# 3

```

Dans notre premier exemple, nous utilisons uniquement un paramètre – le nombre à arrondir, qui est `2.56789`.

Lorsque nous avons passé la variable nombre à la fonction `round()`, elle a été arrondie au nombre entier le plus proche, qui est 3.

C'est aussi simple que cela !

Maintenant, travaillons avec le deuxième paramètre.

```python
x = 2.56789

print(round(x, 2))
# 2.57
```

Le code ci-dessus est similaire au dernier exemple, sauf pour le deuxième paramètre. Nous avons passé une valeur de deux. Cela arrondira le nombre au centième le plus proche (deux décimales).

Dans notre cas, 2.57 a été retourné. C'est-à-dire, 2.56789 à 2.57.

Voyons un dernier exemple pour bien comprendre comment fonctionne le deuxième paramètre.

```python
x = 2.56789

print(round(x, 3))
# 2.568

```

Maintenant, nous avons fait en sorte que le deuxième paramètre soit 3. Nous obtiendrons le nombre arrondi au millième le plus proche (trois décimales).

Le nombre initial – 2.56789 – a été arrondi à 2.568.

## Comment Utiliser la Méthode `math.ceil()` pour Arrondir un Nombre vers le Haut au Nombre Entier le Plus Proche

La méthode `math.ceil()` prend simplement le nombre à arrondir vers le haut comme paramètre. Voici à quoi ressemble la syntaxe :

```txt
math.ceil(nombre)
```

Voici un exemple :

```python
import math

x = 5.57468465

print(math.ceil(x))
# 6

```

Dans le code ci-dessus, vous remarquerez que nous avons d'abord importé le module `math` : `import math`. Cela nous donne accès à toutes les méthodes fournies par le module.

Nous avons créé une variable `x` qui a 5.57468465 comme valeur.

Afin d'arrondir ce nombre vers le haut au nombre entier le plus proche, nous avons passé le nombre (dans la variable `x`) à la méthode `math.ceil()` : `math.ceil(x)`.

La valeur résultante de cette opération, comme on peut le voir dans le code ci-dessus, est 6.

## Comment Utiliser la Méthode `math.floor()` pour Arrondir un Nombre vers le Bas au Nombre Entier le Plus Proche

Tout comme nous l'avons fait dans la dernière section, afin d'utiliser la méthode `math.floor()`, nous devons d'abord importer le module `math`.

Voici la syntaxe de la méthode `math.floor()` :

```txt
math.floor(nombre)
```

Voyons un exemple.

```python
import math

x = 5.57468465

print(math.floor(x))
# 5
```

Comme prévu, nous avons passé le nombre à arrondir vers le bas à la méthode `math.floor()` : `math.floor(x)`. La variable `x` a le nombre 5.57468465 stocké dedans.

Ce nombre a été arrondi vers le bas à 5.

## Conclusion

Dans cet article, nous avons parlé de trois fonctionnalités intégrées en Python qui nous permettent d'arrondir des nombres.

La fonction `round()` arrondit un nombre au nombre entier le plus proche.

La méthode `math.ceil()` arrondit un nombre vers le haut au nombre entier le plus proche tandis que la méthode `math.floor()` arrondit un nombre vers le bas au nombre entier le plus proche. Ces deux méthodes sont toutes deux accessibles via le module `math`.

Avec les exemples donnés dans chaque section, nous avons pu voir comment utiliser chaque fonctionnalité pour obtenir le résultat souhaité.

Bon codage !