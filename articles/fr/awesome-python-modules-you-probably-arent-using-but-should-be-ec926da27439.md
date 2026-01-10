---
title: Modules Python géniaux que vous n'utilisez probablement pas (mais que vous
  devriez)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-15T15:35:50.000Z'
originalURL: https://freecodecamp.org/news/awesome-python-modules-you-probably-arent-using-but-should-be-ec926da27439
coverImage: https://cdn-media-1.freecodecamp.org/images/0*oG_N_s-TEk-wMau5
tags:
- name: code
  slug: code
- name: development
  slug: development
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: technology
  slug: technology
seo_title: Modules Python géniaux que vous n'utilisez probablement pas (mais que vous
  devriez)
seo_desc: 'By Adam Goldschmidt


  Python is a beautiful language, and it contains many built-in modules that aim to
  help us write better, prettier code.

  Objective

  Throughout this article, we will use some lesser-known modules and methods that
  I think can improve ...'
---

Par Adam Goldschmidt

![Image](https://cdn-media-1.freecodecamp.org/images/1*_qzk08ccorLRF4zS6EwBBQ.png)

**Python** est un langage magnifique, et il contient de nombreux modules intégrés qui visent à nous aider à écrire un meilleur code, plus élégant.

### Objectif

Tout au long de cet article, nous utiliserons certains modules et méthodes moins connus qui, je pense, peuvent améliorer la façon dont nous codons - tant en visibilité qu'en efficacité.

### NamedTuple

Je crois que certains d'entre vous connaissent déjà le `namedtuple` plus populaire du module `collections` (si ce n'est pas le cas - [consultez-le](https://docs.python.org/3.6/library/collections.html#collections.namedtuple)), mais depuis Python 3.6, une nouvelle classe est disponible dans le module `typing` : `NamedTuple`. Tous deux sont conçus pour vous aider à créer rapidement des objets immuables et lisibles.

`NamedTuple` est en fait une version typée de `namedtuple`, et à mon avis, est beaucoup plus lisible :

Voici l'alternative `namedtuple` :

### array.array

> _Tableaux efficaces de valeurs numériques. Les tableaux sont des types de séquence et se comportent beaucoup comme des listes, sauf que le type d'objets stockés dans ceux-ci est contraint. — [Documentation Python](https://docs.python.org/3.6/library/array.html)_

Lors de l'utilisation du module `array`, nous devons l'instancier avec un typecode, qui est le type que tous ses éléments utiliseront. Comparons l'efficacité temporelle avec une liste normale, en écrivant de nombreux entiers dans un fichier (en utilisant le module `[pickle](https://docs.python.org/3.7/library/pickle.html)` pour une liste régulière) :

![Image](https://cdn-media-1.freecodecamp.org/images/1*vPfWDCLXCikKuJOuWj5Xkg.png)
_[https://gist.github.com/AdamGold/961758c66cdfe92642eabb61d9ce9866](https://gist.github.com/AdamGold/961758c66cdfe92642eabb61d9ce9866" rel="noopener" target="_blank" title=")_

**14 fois** plus rapide. C'est beaucoup. Bien sûr, cela dépend aussi du module `pickle`, mais le tableau reste bien plus compact que la liste. Donc, si vous utilisez des valeurs numériques simples, vous devriez envisager d'utiliser le module `array`.

### itertools.combinations

`itertools` est un module impressionnant. Il possède tant de méthodes différentes pour gagner du temps, toutes listées [ici](https://docs.python.org/3/library/itertools.html). Il existe même un dépôt GitHub contenant [plus d'itertools](https://github.com/erikrose/more-itertools) !

J'ai eu l'occasion d'utiliser la méthode `combinations` cette semaine et j'ai pensé la partager. Cette méthode prend un itérable et un entier comme arguments, et crée un générateur composé de toutes les combinaisons possibles de l'itérable avec une longueur maximale de l'entier donné, sans duplication :

### dict.fromkeys

Une manière rapide et élégante de créer un dictionnaire avec des valeurs par défaut :

### Dernier mais non des moindres - le module `dis`

> _Le module `[dis](https://docs.python.org/3/library/dis.html#module-dis)` prend en charge l'analyse du [bytecode](https://docs.python.org/3/glossary.html#term-bytecode) CPython en le désassemblant._

Comme vous le savez peut-être ou non, Python compile le code source en un ensemble d'instructions appelé « bytecode ». Le module `dis` nous aide à gérer ces instructions, et c'est un excellent outil de débogage.

Voici un exemple du livre [Fluent Python](http://shop.oreilly.com/product/0636920032519.do) :

Nous avons obtenu une erreur — mais l'opération a tout de même réussi. Comment cela se fait-il ? Eh bien, si nous regardons le bytecode (j'ai ajouté des commentaires près des parties importantes) :

### Avant de partir...

Merci d'avoir lu ! Pour plus d'articles liés à Python et d'autres choses sympas, vous pouvez me suivre sur [Medium](https://medium.com/@adamgoldschmidt) ou [GitHub](https://github.com/AdamGold) (je marque quelques dépôts géniaux !).

Si vous avez aimé cet article, n'hésitez pas à maintenir le bouton d'applaudissements ? enfoncé pour aider les autres à le trouver. Plus vous le maintenez enfoncé, plus vous donnez d'applaudissements !

Et n'hésitez pas à partager d'autres pépites cachées de Python dans les commentaires ci-dessous.