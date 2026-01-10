---
title: Les Mathématiques Martiennes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-03-16T18:09:51.000Z'
originalURL: https://freecodecamp.org/news/martian-math-812a029e2ea0
coverImage: https://cdn-media-1.freecodecamp.org/images/1*mK-q8ZwVLhz_XB5XUuItow.png
tags:
- name: education
  slug: education
- name: Life lessons
  slug: life-lessons
- name: Math
  slug: math
- name: Mathematics
  slug: mathematics
- name: 'self-improvement '
  slug: self-improvement
seo_title: Les Mathématiques Martiennes
seo_desc: 'By Chet Corcos

  We’re going to explore number systems by solving one of my favorite riddles.


  You are the first explorer on Mars and you discover a math equation carved into
  a rock: 12 + 24 = 40. How many fingers did Martians have?


  I love this riddle...'
---

Par Chet Corcos

Nous allons explorer les systèmes de numération en résolvant une de mes énigmes préférées.

> Vous êtes le premier explorateur sur Mars et vous découvrez une équation mathématique gravée dans une roche : 12 + 24 = 40. Combien de doigts avaient les Martiens ?

J'adore cette énigme parce qu'elle vous fait repenser toute votre compréhension des nombres. Elle démontre également un problème dans la manière dont les mathématiques sont enseignées à l'école — plutôt que d'enseigner pour une compréhension fondamentale, on nous apprend à passer un test. Ainsi, nous sommes coincés avec une compréhension superficielle de concepts simples comme les nombres ! Mais assez de prêchi-prêcha, apprenons quelque chose.

Conceptuellement, les nombres sont simplement des quantités, mais la manière dont nous représentons ces quantités peut varier. Nous représentons généralement les nombres dans un système de numération en base 10. Cela signifie que chaque chiffre d'un nombre représente une puissance de 10. C'est-à-dire que le nombre 123 représente 1×10³ + 2×10¹ + 3×10⁰. Cependant, il est _possible_ d'utiliser un système de numération qui n'est pas basé sur les puissances de 10. Il est difficile d'imaginer vivre dans un monde qui utilise un système de numération non décimal, mais en réalité, la manière de représenter les nombres est complètement arbitraire ! Alors pourquoi utilisons-nous un système de numération en base 10 ? Vous l'avez deviné — nous avons 10 doigts !

Voici une petite visualisation de la manière dont fonctionne un système de numération en base 10. Remarquez que chaque fois qu'une colonne est remplie, nous ajoutons une unité à la colonne suivante.

![Image](https://cdn-media-1.freecodecamp.org/images/oOPEy9HbZZJKT0unnLLhU7R0z788utfKw6ee)

La beauté de cette façon de voir les nombres est que le concept de quantité semble naturel pour tous les systèmes de numération, pas seulement pour la base 10. Alors explorons quelques autres systèmes de numération.

Les ordinateurs représentent les nombres en utilisant le _binaire_, qui est un système de numération en base 2. C'est le même concept, sauf qu'au lieu de passer à la colonne suivante après que 9 points soient remplis, vous passez après seulement 1.

![Image](https://cdn-media-1.freecodecamp.org/images/dmDH1UFoM7SGmQ16oFuaqH4BPfh-bQlW-Q88)

Les programmeurs représentent souvent les nombres en utilisant l'_hexadécimal_, qui est un système de numération en base 16. Ils le font parce que le binaire n'est pas très compact — il faut 4 chiffres binaires pour représenter le nombre 16 — et parce que 16 est une puissance de 2, ce qui facilite la conversion entre les deux systèmes de numération.

Puisqu'il serait étrange qu'un nombre comme 12 ne représente qu'une seule place de chiffre lorsque nous l'écrivons, nous commençons généralement à compter l'alphabet après 9. C'est-à-dire que _A_ représente 10, _B_ représente 11, _C_ représente 12, et ainsi de suite.

![Image](https://cdn-media-1.freecodecamp.org/images/Y84nHlT9MBSLUSFWnkxMsYZjexLEIO1hBY0e)

Et maintenant, notre énigme ! D'abord, essayez de la résoudre vous-même. Si vous le souhaitez, vous pouvez [jouer avec l'outil de visualisation vous-même](http://aprt.us/editor/?load=https://gist.githubusercontent.com/ccorcos/5bae90fda25c82f924cd59c475608f30/raw/c39ecec1e3ccb2e79b7f6a8f665ab80f6962a8ff/Number%2520System.json&fullScreen=1).

Je vous ai déjà donné un grand indice — nous avons un système de numération en base 10 parce que nous avons 10 doigts ! Donc, si nous pouvons trouver un système de numération où ces _symboles_ représentent des _nombres_ qui satisfont l'équation, alors nous avons résolu l'énigme.

Il y a une manière plus directe de trouver la réponse, mais utilisons simplement notre bon ami « essai et erreur ». Puisque chaque Martien dans chaque référence de la culture populaire a 6 doigts, essayons cela.

Rappelons l'équation pour référence : 12 + 24 = 40.

![Image](https://cdn-media-1.freecodecamp.org/images/0E7nunEtuSXaDbx1lmNRIuHGWa7tgsgewXX5)

Comme vous pouvez le voir, 8 est représenté comme 12 dans un système de numération en base 6. C'est parce que 8 = 1×6¹ + 2×6⁰.

![Image](https://cdn-media-1.freecodecamp.org/images/UtxwtxfWwbowuUj8Wck4Q6VpfXXgiLTAupV0)

Ici, vous pouvez voir que 16 est représenté comme 23 dans un système de numération en base 6.

![Image](https://cdn-media-1.freecodecamp.org/images/PesMnNMfjzFaxllaQN6VIqyP5RDnQuiP11Q4)

Et enfin, 24 est représenté comme 40 dans un système de numération en base 6. Ainsi, si nous devions convertir cette équation dans un système de numération en base 10, nous aurions 8 + 16 = 24. Donc, voici la réponse à l'énigme — les Martiens ont 6 doigts !

Il est difficile de comprendre cette équation parce que c'est ainsi que nous avons appris à résoudre mécaniquement les problèmes de mathématiques. Mais nous utilisons en réalité des systèmes de numération non décimaux tous les jours. Je parie que cette équation a du sens pour vous : 0:30 + 1:45 = 2:15. Le temps est un exemple parfait d'un système de numération qui n'est pas en base 10. Et si vous vivez aux États-Unis et que vous devez utiliser notre système de mesure horrible, vous trouverez des systèmes de numération bizarres partout.

À la fin de la journée, ce que j'espère que vous avez retenu de cet article est une appréciation de la différence entre des concepts comme les quantités et les représentations symboliques que nous utilisons pour encoder ces concepts. Ce sont des concepts subtils comme celui-ci qui sont bien plus importants que l'exercice mécanique d'additionner deux nombres sur papier.

P.S. Découvrez [Apparatus](http://aprt.us/) ! C'est un logiciel incroyable pour créer des diagrammes interactifs.

Si vous êtes intéressé par ce genre de choses, vous pourriez aimer lire ma newsletter hebdomadaire de tout ce que je trouve intéressant. Vous pouvez [vous abonner ici](http://news.chetcorcos.com/).