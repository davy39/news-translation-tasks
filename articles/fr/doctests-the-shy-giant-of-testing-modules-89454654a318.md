---
title: Rencontrez les doctests, les géants timides des modules de test
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-29T19:08:25.000Z'
originalURL: https://freecodecamp.org/news/doctests-the-shy-giant-of-testing-modules-89454654a318
coverImage: https://cdn-media-1.freecodecamp.org/images/1*eMH1zFW_YagZqorGErpcVg.jpeg
tags:
- name: coding
  slug: coding
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: technology
  slug: technology
- name: Testing
  slug: testing
seo_title: Rencontrez les doctests, les géants timides des modules de test
seo_desc: 'By Periklis Gkolias

  Do you use Python, even to wash your clothes? And do you find unit testing boring,
  but still have to do it, because you find value in automated testing? Then this
  article is for you.

  The idea

  If you are a Python fan, then I believ...'
---

Par Periklis Gkolias

Utilisez-vous Python, même pour laver vos vêtements ? Et trouvez-vous les tests unitaires ennuyeux, mais devez-vous quand même les faire, parce que vous trouvez de la valeur dans les tests automatisés ? Alors cet article est pour vous.

### L'idée

Si vous êtes un fan de Python, alors je crois que vous avez utilisé la console Python de temps en temps. Supposons que vous écrivez quelques fonctions en ligne comme ci-dessous, pour expérimenter des choses :

```
$ python
Python 3.6.4 |Anaconda custom (64-bit)| (default, Jan 16 2018, 18:10:19) 
[GCC 7.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> def addme(a):
...     return a + a
... 
>>> addme(2)
4
>>> addme(1.9)
3.8
>>> addme(0)
0
>>>
```

Donc, vous avez écrit une fonction en ligne, et vous avez fait quelques tests pour faire des vérifications de base. Et si Python pouvait lire la sortie ci-dessus et faire le raisonnement pour vous, à l'exécution ? C'est l'idée derrière les doctests, mon ami.

### Sérieusement ?

![Image](https://cdn-media-1.freecodecamp.org/images/V3es93rVCDb3SSQnkAYWHMY1T8zo38gaupW4)
_Calme-toi Patrick_

Oui, totalement ! Python a introduit beaucoup de fonctionnalités intuitives et... décevantes de temps en temps, qui sont maintenant courantes dans quelques langues principales. Pourquoi celle-ci ne le serait-elle pas aussi ?

### Avantages des doctests

Les avantages des doctests sont assez nombreux.

Tout d'abord, ils sont ridiculement faciles à écrire. Je veux dire, vous pourriez même les sous-traiter à votre jeune cousin, qui étudie l'anatomie des atomes de sol (et non la programmation), parce qu'il vous doit pour avoir réparé son ordinateur.

Deuxièmement, à moins que vous ne trouviez le copier-coller difficile, ils sont plus joyeux à écrire. Cette fois, vous devez être familier avec l'environnement terminal, cependant.

Troisièmement, il n'est pas nécessaire d'ouvrir un autre fichier (même si vous pouvez mettre tous les doctests pour votre application dans un seul fichier) pour lire le code de test pour une fonction, car ils se trouvent juste sous la signature de chaque fonction.

Et enfin, ils sont exécutables avec le module doctest et lisibles sans connaître un peu de Python.

### Et les tests unitaires ?

Les tests unitaires offrent encore une grande valeur et des capacités avancées de test. Alors que les doctests sont excellents pour valider des fonctions simples et pures, ils ne sont pas très utiles lorsque vous devez faire une validation complexe (par exemple, si une séquence de commandes a été appelée pendant le test).

### Et le mocking ?

Les doctests peuvent gérer le mocking avec grâce avec une excellente bibliothèque appelée [Minimock](https://pypi.org/project/MiniMock/). Je vous encourage à l'essayer et à me faire part de vos réflexions.

Même si j'aime l'initiative, je préfère que mes tests aient des rôles séparés. Je ne veux pas que mes doctests soient lourdement chargés et universels. Mais c'est vraiment une question de goût — et il n'y a rien de mal si vous n'êtes pas d'accord. Je suis plus qu'heureux d'entendre votre raisonnement, si c'est le cas.

### Un exemple fonctionnel

Les paroles sont bon marché, alors écrivons du code. Ci-dessous se trouve un exemple fonctionnel utilisant la fonction de l'invite ci-dessus.

```py
addme(a):
    """
    Ceci est une docstring, généralement pour expliquer l'utilisation d'une fonction. Veuillez ne pas la confondre avec les doctests. Elles visent toutes deux à fournir des formes de documentation, mais les doctests sont également exécutables.
    >>> addme(4)
    8
    >>> addme('a')
    'aa'
    >>> addme(set())
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for +: 'set' and 'set'
    """
    return a + a

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(addme(1))
```

Il y a quelques points qui valent la peine d'être notés ici :

* Les doctests doivent vivre à l'intérieur d'une docstring. Là, il suffit de "copier-coller" la sortie de vos tests rapides de la console Python.
* Si vous devez simuler un cas d'exception, vous n'avez besoin d'ajouter que la première et la dernière ligne du message d'exception. Vous vous attendiez à coder en dur les chemins ou à faire une logique étrange pour obtenir le chemin complet du fichier et l'imprimer en entier ? Allons, Python ne fera pas ça :)
* Vous avez besoin de la bibliothèque doctest pour exécuter les tests. Nose n'en a pas besoin cependant.
* Vous pouvez exécuter ce qui précède, comme d'habitude, avec `python mydoctests.py`

### J'ai besoin que mes tests s'exécutent dans le cadre du cycle CI/CD/CT. Qu'est-ce qui m'attend ?

Je ne suis pas là pour vous décevoir, n'est-ce pas ? :)

Le [nose](http://nose.readthedocs.io/en/latest/) test runner prend en charge l'exécution de tous vos doctests en plus de vos tests unitaires. Il suffit d'ajouter le flag `--with-doctest` et vous êtes prêt à partir.

### Des trucs sympas, où vais-je à partir de là ?

* Lisez la [documentation](https://docs.python.org/3.6/library/doctest.html) de Python pour plus de détails et de cas.
* Lisez ce livre fantastique [livre](https://amzn.to/2sjvKoP) et surtout le chapitre 4, qui couvre les doctests.
* Vérifiez les implémentations d'autres langues. Par exemple, celle pour [NodeJS](https://github.com/davidchambers/doctest)
* [Doctests et nose](http://nose.readthedocs.io/en/latest/plugins/doctests.html)

Merci d'avoir lu cet article, j'espère que vous l'avez apprécié et que l'article a suscité votre intérêt pour l'écriture de plus de tests (et moins douloureux). N'hésitez pas à partager l'amour avec les boutons ci-dessous si c'est le cas. N'hésitez pas à ajouter vos propres pensées et expériences avec les doctests aussi.

Publié à l'origine sur [mon blog](https://perigk.github.io).