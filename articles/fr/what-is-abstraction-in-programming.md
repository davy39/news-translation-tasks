---
title: Qu'est-ce que l'abstraction en programmation – Et pourquoi est-elle utile ?
subtitle: ''
author: Tiago Capelo Monteiro
co_authors: []
series: null
date: '2022-07-13T22:54:18.000Z'
originalURL: https://freecodecamp.org/news/what-is-abstraction-in-programming
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/Screenshot--518-.png
tags:
- name: coding
  slug: coding
- name: General Programming
  slug: programming
- name: Python
  slug: python
seo_title: Qu'est-ce que l'abstraction en programmation – Et pourquoi est-elle utile
  ?
seo_desc: 'Did you know that abstraction is one of the most important concepts for
  any software engineer to know?

  That''s right!

  Without the use of abstraction when developing new technologies and concepts, we
  would never have been able to invent most software o...'
---

Saviez-vous que l'abstraction est l'un des concepts les plus importants pour tout ingénieur logiciel à connaître ?

C'est exact !

Sans l'utilisation de l'abstraction lors du développement de nouvelles technologies et concepts, nous n'aurions jamais pu inventer la plupart des logiciels ou même la plupart des choses.

Ainsi, comprendre ce concept est vraiment important pour le développement logiciel.

## Qu'est-ce que l'abstraction en programmation ?

Vous avez utilisé l'abstraction de nombreuses manières, mais vous ne l'avez peut-être pas su.

La pensée abstraite est l'une des choses que les humains font dans tant de domaines :

* Philosophie
* Art
* Mathématiques
* Informatique
* et bien plus encore...

Mais qu'est-ce que c'est vraiment ? Vous allez tout apprendre à ce sujet dans cet article.

## Ce que nous allons couvrir :

1. Analogie de l'abstraction
2. Exemple Python d'abstraction
3. Exemple général d'électronique d'abstraction
4. Exemple de systèmes embarqués d'abstraction
5. Pourquoi comprendre l'abstraction est-il utile ?

## Analogie de l'abstraction

![Image](https://www.freecodecamp.org/news/content/images/2022/07/pexels-torsten-dettlaff-70912.jpg)
_Photo par Torsten Dettlaff de Pexels : https://www.pexels.com/photo/black-coupes-70912/_

Disons que vous êtes dans une auto-école pour obtenir votre permis de conduire.

Dans l'école, vous apprenez comment fonctionnent les principaux composants de la voiture :

* Freins
* Transmission
* Système de suspension
* Batterie

Vous n'avez pas besoin de comprendre à un niveau technique chaque composant pour apprendre à conduire.

Vous avez juste besoin d'une image mentale de ce que font les freins lorsque vous appuyez sur la pédale. Ou de ce qui se passe dans la transmission lorsque vous changez de vitesse... et ainsi de suite.

Vous avez seulement besoin d'une **représentation mentale de base** du composant que vous utilisez.

Cela signifie que vous avez seulement besoin d'une **abstraction** du composant de la voiture.

Notre utilisation des abstractions pour apprendre et utiliser les choses est partout :

* Vous n'avez pas besoin de connaître les parties internes d'une voiture pour la conduire. Mais connaître leur fonctionnement peut faire de vous un **meilleur conducteur.**
* Vous n'avez pas besoin de connaître les parties internes d'un vélo pour savoir comment le monter. Mais connaître leur fonctionnement peut faire de vous un **meilleur cycliste.**
* Vous n'avez pas besoin de connaître les parties internes d'une fonction ou d'un framework en programmation pour l'utiliser. Mais connaître leur fonctionnement peut faire de vous un **meilleur programmeur.**

## Exemple Python d'abstraction

![Image](https://www.freecodecamp.org/news/content/images/2022/03/code.png)

Ceci est du code écrit en Python. Nous utilisons simplement la fonction print pour afficher le texte « Hello world » à l'écran.

Pour cela, vous avez juste besoin de savoir comment utiliser la fonction print.

Vous n'avez pas besoin de comprendre comment elle fonctionne sous le capot.

Mais il est parfois bon de comprendre comment une certaine fonction fonctionne en arrière-plan afin de l'utiliser plus efficacement.

En sachant comment elle fonctionne :

* Vous deviendrez un meilleur programmeur en comprenant le code des autres
* Vous comprendrez plus facilement les bugs dans les bibliothèques que vous utilisez
* Au lieu d'importer une bibliothèque entière, vous pouvez copier le code dont vous avez besoin depuis un autre projet. Un projet avec moins de dépendances sera plus facile à gérer

Par exemple, disons que vous voulez utiliser le [module statistics de Python](https://docs.python.org/3/library/statistics.html), qui est un module intégré dans Python. Cela signifie que Python vient déjà avec le module dans sa bibliothèque.

Vous n'avez pas besoin de [l'importer avec PIP](https://www.freecodecamp.org/news/how-to-use-pip-install-in-python/).

Disons que je veux utiliser la [fonction mean](https://docs.python.org/3/library/statistics.html#statistics.mean) :

```
from statistics import mean 

randomList = [-1.0, 2.5, 3.25, 5.75]

print(mean(randomList))
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/python-example.png)

Si aucune donnée n'est présente, [Statistics.error](https://docs.python.org/3/library/statistics.html#statistics.StatisticsError) sera levée.

Cela affichera 2,625.

Mais comment cela fonctionne-t-il à l'intérieur ?

Si vous allez à [https://github.com/python/cpython/blob/main/Lib/statistics.py](https://github.com/python/cpython/blob/main/Lib/statistics.py), vous trouverez à la ligne 414 le code pour la fonction mean :

```python
def mean(data):
    """
    Retourne la moyenne arithmétique de l'échantillon de données.
    >>> mean([1, 2, 3, 4, 4])
    2.8
    >>> from fractions import Fraction as F
    >>> mean([F(3, 7), F(1, 21), F(5, 3), F(1, 3)])
    Fraction(13, 21)
    >>> from decimal import Decimal as D
    >>> mean([D("0.5"), D("0.75"), D("0.625"), D("0.375")])
    Decimal('0.5625')
    Si ``data`` est vide, StatisticsError sera levée.
    """
    T, total, n = _sum(data)
    if n < 1:
        raise StatisticsError('mean requires at least one data point')
    return _convert(total / n, T)
    
    
 
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/https-__github.com_python_cpython_blob_main_Lib_statistics.py.png)

Ceci est le code interne qui s'exécute lorsque vous utilisez le module intégré statistics que Python vous fournit.

## Exemple général d'électronique d'abstraction

Tout système embarqué ou dispositif électronique nécessite des circuits.

Les circuits sont composés de nombreux fils et composants. Les ingénieurs en électronique conçoivent ces dispositifs.

Dans tout programme d'ingénierie électrique ou apparenté, les étudiants universitaires n'apprennent pas seulement à concevoir des circuits, mais aussi la physique réelle derrière chaque composant qui constitue le circuit.

Après l'université, de nombreux ingénieurs électriques _travaillent_ sur de petits circuits pour développer des dispositifs électroniques pour des calculatrices, des micro-ondes, des imprimantes et d'autres appareils.

Alors que les ingénieurs électriques travaillent à fabriquer les circuits, qui travaille à fabriquer les composants ?

Eh bien, certains ingénieurs électriques, ingénieurs en matériaux, physiciens appliqués, et autres.

Dans cet exemple, nous utiliserons les physiciens appliqués – des scientifiques qui appliquent la physique pour résoudre des problèmes techniques difficiles.

Certains physiciens appliqués se concentrent sur l'étude et la création des composants utilisés dans un circuit.

Certains physiciens appliqués s'occupent de développer des éléments qui deviendront les blocs de construction des circuits comme :

* LED
* Écrans LCD
* Condensateurs
* Photorésistances

Les ingénieurs électriques développent les circuits et les applications électroniques avec ces composants.

Ils ne se soucient pas au même niveau de détail que les physiciens appliqués de la composition de ces composants.

Ce qui les intéresse, c'est d'utiliser ces matériaux pour résoudre des problèmes avec l'électronique.

C'est l'abstraction !

Les physiciens appliqués se concentrent sur le niveau d'abstraction où les composants sont créés, avec quels matériaux, avec le temps pour les créer...

L'ingénieur électrique se concentre sur le niveau d'abstraction où les composants sont utilisés pour créer des circuits et des dispositifs.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/abstraction.drawio.png)
_**Sur quoi chaque professionnel travaille-t-il ?**_

## Exemple de systèmes embarqués d'abstraction

Un ingénieur en systèmes embarqués (ingénieurs qui créent de petits systèmes informatiques avec une fonction dédiée, comme un grille-pain, une calculatrice scientifique, une souris, un clavier, etc.) doit savoir comment coder près du matériel.

Pour cela, il doit avoir une bonne compréhension du C et du langage d'assemblage, car ils sont étroitement liés l'un à l'autre.

Par exemple, dans les systèmes embarqués critiques (applications en temps réel qui traitent des données et des événements ayant des contraintes de temps critiques) comme :

* Dispositifs médicaux
* Systèmes de contrôle d'avion
* Systèmes de guidage de missile

Un ingénieur doit être capable de comprendre le code C et l'assemblage. L'assemblage est normalement utilisé dans des fonctions très spécifiques lorsque l'assemblage pur s'exécute mieux que le code C compilé.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/abstraction.drawio-2.png)
_**Exemple de différents niveaux d'abstraction**_

Chaque boîte est un niveau d'abstraction différent.

Ces composants électriques sont fabriqués et étudiés par des physiciens appliqués, des ingénieurs en matériaux et certains ingénieurs électriques.

Ces composants logiciels (fonctions, classes) sont utilisés et créés par les programmeurs de systèmes embarqués.

## Pourquoi comprendre l'abstraction est-il utile ?

Comprendre l'abstraction vous permettra de savoir quand vous devez connaître quelque chose de technique ou simplement comment l'utiliser.

Une autre raison de bien comprendre l'abstraction est lorsque vous commencez à apprendre un framework en dehors de votre domaine de travail.

Lorsque vous apprenez d'abord un framework, vous apprenez à l'utiliser. En apprenant comment le framework fonctionne, vous commencez à comprendre ses limites.

En conséquence, vous apprenez comment les classes et les fonctions sont réellement écrites.

En comprenant les bibliothèques, les frameworks et d'autres aspects de la programmation à un niveau avancé, vous serez en mesure de créer vos propres bibliothèques et frameworks.

De cette manière, vous pourrez progresser dans votre carrière et vous pourrez même être en mesure de résoudre certains problèmes de travail difficiles.

Réduire les dépendances dans un projet est une autre raison de comprendre l'abstraction.

Lorsque vous utilisez quelques fonctions d'une bibliothèque externe, vous pouvez voir comment le code est écrit et simplement ajouter votre propre fonction ou classe.

De cette manière, votre projet a moins de dépendances. Cela facilite l'exécution de votre code par les autres sans avoir à installer d'autres dépendances.

## Conclusion

Merci d'avoir lu ! Maintenant, vous savez :

* Ce qu'est l'abstraction
* Trois exemples d'abstraction : Python, électronique générale et systèmes embarqués
* Pourquoi comprendre l'abstraction est utile