---
title: Comment — et pourquoi — vous devriez utiliser les générateurs Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-07T11:14:49.000Z'
originalURL: https://freecodecamp.org/news/how-and-why-you-should-use-python-generators-f6fb56650888
coverImage: https://cdn-media-1.freecodecamp.org/images/1*UifvzyheweFeO0u6nS7Q0g.jpeg
tags:
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: startup
  slug: startup
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Comment — et pourquoi — vous devriez utiliser les générateurs Python
seo_desc: 'By Radu Raicea

  Generators have been an important part of Python ever since they were introduced
  with PEP 255.

  Generator functions allow you to declare a function that behaves like an iterator.

  They allow programmers to make an iterator in a fast, eas...'
---

Par Radu Raicea

Les **générateurs** font partie intégrante de Python depuis leur introduction avec [PEP 255](https://www.python.org/dev/peps/pep-0255/).

Les fonctions génératrices vous permettent de déclarer une fonction qui se comporte comme un itérateur.

Elles permettent aux programmeurs de créer un itérateur de manière rapide, facile et propre.

Qu'est-ce qu'un itérateur, pourriez-vous demander ?

Un [**itérable**](https://en.wikipedia.org/wiki/Iterator) est un objet sur lequel on peut itérer (boucler). Il est utilisé pour abstraire un conteneur de données afin qu'il se comporte comme un objet itérable. Vous utilisez probablement déjà quelques objets itérables chaque jour : chaînes de caractères, listes et dictionnaires, pour en nommer quelques-uns.

Un itérateur est défini par une classe qui implémente le [**Protocole Itérateur**](https://docs.python.org/3/c-api/iter.html). Ce protocole recherche deux méthodes dans la classe : `__iter__` et `__next__`.

Attendez, reculez. Pourquoi voudriez-vous même créer des itérateurs ?

#### Économiser de l'espace mémoire

Les itérateurs ne calculent pas la valeur de chaque élément lors de leur instanciation. Ils ne la calculent que lorsque vous la demandez. Cela est connu sous le nom d'[évaluation paresseuse](https://en.wikipedia.org/wiki/Lazy_evaluation).

L'évaluation paresseuse est utile lorsque vous avez un très grand ensemble de données à calculer. Elle vous permet de commencer à utiliser les données immédiatement, tandis que l'ensemble complet des données est en cours de calcul.

Supposons que nous voulons obtenir tous les nombres premiers qui sont inférieurs à un nombre maximum.

Nous définissons d'abord la fonction qui vérifie si un nombre est premier :

```
def check_prime(number):    for divisor in range(2, int(number ** 0.5) + 1):        if number % divisor == 0:            return False    return True
```

Ensuite, nous définissons la classe itérateur qui inclura les méthodes `__iter__` et `__next__` :

```
class Primes:    def __init__(self, max):        self.max = max        self.number = 1
```

```
    def __iter__(self):        return self
```

```
    def __next__(self):        self.number += 1        if self.number >= self.max:            raise StopIteration        elif check_prime(self.number):            return self.number        else:            return self.__next__()
```

`Primes` est instancié avec une valeur maximale. Si le nombre premier suivant est supérieur ou égal à `max`, l'itérable lèvera une exception `StopIteration`, ce qui mettra fin à l'itérable.

Lorsque nous demandons l'élément suivant dans l'itérable, il incrémentera `number` de 1 et vérifiera s'il s'agit d'un nombre premier. Si ce n'est pas le cas, il appellera `__next__` à nouveau jusqu'à ce que `number` soit premier. Une fois que c'est le cas, l'itérable retourne le nombre.

En utilisant un itérable, nous ne créons pas une liste de nombres premiers dans notre mémoire. Au lieu de cela, nous générons le nombre premier suivant chaque fois que nous le demandons.

Essayons cela :

```
primes = Primes(100000000000)
```

```
print(primes)
```

```
for x in primes:    print(x)
```

```
---------
```

```
<__main__.Primes object at 0x1021834a8>235711...
```

Chaque itération de l'objet `Primes` appelle `__next__` pour générer le nombre premier suivant.

**Les itérateurs ne peuvent être itérés qu'une seule fois.** Si vous essayez d'itérer à nouveau sur `primes`, aucune valeur ne sera retournée. Il se comportera comme une liste vide.

Maintenant que nous savons ce que sont les itérateurs et comment en créer un, nous passerons aux générateurs.

### Générateurs

Rappelons que les fonctions génératrices nous permettent de créer des itérateurs de manière plus simple.

Les générateurs introduisent l'instruction `yield` en Python. Elle fonctionne un peu comme `return` car elle retourne une valeur.

La différence est qu'**elle sauvegarde l'état** de la fonction. La prochaine fois que la fonction est appelée, l'exécution reprend **là où elle s'était arrêtée**, avec les **mêmes valeurs de variables** qu'elle avait avant le yield.

Si nous transformons notre itérateur `Primes` en un générateur, il ressemblera à ceci :

```
def Primes(max):    number = 1    while number < max:        number += 1        if check_prime(number):            yield number
```

```
primes = Primes(100000000000)
```

```
print(primes)
```

```
for x in primes:    print(x)
```

```
---------
```

```
<generator object Primes at 0x10214de08>235711...
```

C'est assez pythonique ! Peut-on faire mieux ?

Oui ! Nous pouvons utiliser les **Expressions Génératrices**, introduites avec [PEP 289](https://www.python.org/dev/peps/pep-0289/).

Il s'agit de l'équivalent des compréhensions de liste pour les générateurs. Cela fonctionne exactement de la même manière qu'une compréhension de liste, mais l'expression est entourée de `()` au lieu de `[]`.

L'expression suivante peut remplacer notre fonction génératrice ci-dessus :

```
primes = (i for i in range(2, 100000000000) if check_prime(i))
```

```
print(primes)
```

```
for x in primes:    print(x)
```

```
---------
```

```
<generator object <genexpr> at 0x101868e08>235711...
```

C'est la beauté des générateurs en Python.

### En résumé...

* Les générateurs vous permettent de créer des itérateurs de manière très pythonique.
* Les itérateurs permettent une évaluation paresseuse, ne générant l'élément suivant d'un objet itérable que lorsqu'il est demandé. Cela est utile pour les très grands ensembles de données.
* Les itérateurs et les générateurs ne peuvent être itérés qu'une seule fois.
* Les fonctions génératrices sont meilleures que les itérateurs.
* Les expressions génératrices sont meilleures que les itérateurs (uniquement pour les cas simples).

Vous pouvez également consulter mon [explication](https://medium.freecodecamp.org/how-i-used-python-to-find-interesting-people-on-medium-be9261b924b0) de la manière dont j'ai utilisé Python pour trouver des personnes intéressantes à suivre sur Medium.

Pour plus de mises à jour, suivez-moi sur [Twitter](https://twitter.com/radu_raicea).