---
title: Apprenez les bases de la programmation fonctionnelle — gratuitement, dans votre
  boîte mail
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-01-20T16:24:44.000Z'
originalURL: https://freecodecamp.org/news/learning-the-fundamentals-of-functional-programming-425c9fd901c6
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Zy10ES24gQ6soFqjRNpZVg.jpeg
tags:
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: learning
  slug: learning
- name: learning to code
  slug: learning-to-code
- name: 'self-improvement '
  slug: self-improvement
seo_title: Apprenez les bases de la programmation fonctionnelle — gratuitement, dans
  votre boîte mail
seo_desc: 'By Preethi Kasireddy

  If you’re a software developer, you’ve probably noticed a growing trend: software
  applications keep getting more complicated.

  It falls on our shoulders as developers to build, test, maintain, and scale these
  complex systems. To d...'
---

Par Preethi Kasireddy

Si vous êtes un développeur logiciel, vous avez probablement remarqué une tendance croissante : **les applications logicielles deviennent de plus en plus compliquées.**

Il incombe à nous, en tant que développeurs, de construire, tester, maintenir et mettre à l'échelle ces systèmes complexes. Pour ce faire, nous devons créer un code bien structuré qui soit facile à comprendre, écrire, déboguer, réutiliser et maintenir.

Mais écrire des programmes de cette manière nécessite bien plus que de la pratique et de la patience.

Dans mon prochain cours, _Apprendre le JavaScript fonctionnel de la bonne manière_, je vous enseignerai comment utiliser la programmation fonctionnelle pour créer un code bien structuré.

Mais avant de vous lancer dans ce cours (et j'espère que vous le ferez !), il y a un prérequis important : construire une base solide dans **les principes sous-jacents de la programmation fonctionnelle**.

J'ai donc créé un nouveau [cours gratuit par e-mail](https://preethikasireddy.typeform.com/to/yC9qQr) qui vous emmènera dans un voyage amusant et exploratoire pour comprendre certains de ces principes fondamentaux.

Regardons ce que le cours par e-mail couvrira, afin que vous puissiez décider comment il s'intègre dans votre éducation en programmation.

### Qu'est-ce que la programmation fonctionnelle ?

Alors. Qu'est-ce que la "programmation fonctionnelle", exactement ?

La programmation fonctionnelle n'est pas un framework ou un outil, mais une **façon** d'écrire du code. En programmation fonctionnelle, nous mettons un accent majeur sur l'écriture de code en utilisant des **fonctions comme "blocs de construction"**.

Votre programme est défini en termes d'une fonction principale. Cette fonction principale est définie en termes d'autres fonctions, qui sont à leur tour définies en termes de encore plus de fonctions — jusqu'au niveau le plus bas où les fonctions sont simplement des primitives de langage comme "nombre" ou "chaîne de caractères".

![Image](https://cdn-media-1.freecodecamp.org/images/AziWGQ2dGtkvzvUL0v1RIWwIJu6V-h6W7c-e)

Si vous lisez ceci en pensant, _"Hmm, mais attendez ? Est-ce que chaque langage n'utilise pas des fonctions pour écrire du code ?"_ alors bien joué ?. Cela signifie que vous faites attention.

Vous avez raison — chaque langage de programmation a des fonctions. Mais la programmation fonctionnelle l'emmène à un **tout autre niveau ?**

![Image](https://cdn-media-1.freecodecamp.org/images/UDgSl91kyBG7odfIYdysSd-StB-rNoXxcCjw)
_Des fonctions à un tout autre niveau_

Pour comprendre ce que je veux dire, revenons en arrière et commençons par les bases.

Chaque programme logiciel a deux choses :

1. Comportement
2. Données

Lorsque nous apprenons un paradigme de programmation — comme la programmation fonctionnelle — il est souvent utile de considérer comment le paradigme aborde le comportement et les données respectivement.

Le **comportement**, par exemple, est géré purement en utilisant des fonctions en programmation fonctionnelle.

Les **fonctions** sont des morceaux de code "auto-contournés" qui accomplissent une tâche spécifique. Elles définissent une relation entre un ensemble d'entrées possibles et un ensemble de sorties possibles — elles prennent généralement des données, les traitent et retournent un résultat. Une fois qu'une fonction est écrite, elle peut être utilisée encore et encore.

Les **données** sont, eh bien, des données. En programmation fonctionnelle, les données sont immuables — ce qui signifie qu'elles ne peuvent pas être modifiées. Plutôt que de modifier les données qu'elles prennent en entrée, les fonctions en programmation fonctionnelle prennent des données en entrée et produisent des **nouvelles** valeurs en sortie. Toujours.

Les fonctions et les données immuables sont les deux seules choses avec lesquelles vous devez traiter en programmation fonctionnelle. Pour simplifier encore, les fonctions sont traitées de la même manière que les données.

En d'autres termes, **les fonctions en programmation fonctionnelle peuvent être transmises aussi facilement que des données.** Vous pouvez les référencer à partir de _constantes_ et de _variables_, les passer en tant que _paramètres_ à d'autres fonctions, et les retourner en tant que _résultats_ d'autres fonctions.

C'est la chose la plus importante à comprendre lorsque l'on aborde la programmation fonctionnelle.

![Image](https://cdn-media-1.freecodecamp.org/images/oqb79dext6W9vY7dpo80KccktAKfwUgHp8U-)

En traitant les fonctions comme rien de plus spécial qu'un morceau de données et en n'utilisant que des données immuables, nous avons beaucoup plus de liberté en termes de la manière dont nous pouvons utiliser les fonctions.

Notamment, cela nous permet de créer de petites fonctions indépendantes qui peuvent être réutilisées et combinées ensemble pour construire une logique de plus en plus complexe. Nous pouvons **décomposer tout problème complexe en sous-problèmes plus petits, les résoudre en utilisant des fonctions, et enfin les combiner pour résoudre le problème plus grand.**

Considérant la complexité toujours croissante des applications logicielles, cette approche de "blocs de construction" fait une énorme différence pour garder les programmes simples, modulaires et compréhensibles. C'est aussi pourquoi les développeurs s'efforcent de rendre leurs fonctions aussi **polyvalentes** que possible, afin qu'elles puissent être **combinées** pour résoudre de grands problèmes complexes et **réutilisées** pour accélérer le temps de développement des programmes suivants.

![Image](https://cdn-media-1.freecodecamp.org/images/vE7OgoYjLrRIs1QUL3dmD-QHmwvwfYijiMUD)
_Composition de fonctions_

En fin de compte, la raison pour laquelle les fonctions sont si puissantes en programmation fonctionnelle est que les fonctions suivent certains principes fondamentaux. Ces principes seront le sujet de mon cours par e-mail :

* Les fonctions sont pures
* Les fonctions utilisent des données immuables
* Les fonctions garantissent la transparence référentielle
* Les fonctions sont des entités de première classe

Après cela, j'aborderai brièvement comment la programmation fonctionnelle applique ces principes pour nous encourager à réfléchir soigneusement à nos données et aux fonctions qui interagissent avec elles.

À la fin, vous serez en mesure de comprendre comment cette approche conduit à un code qui est :

* Plus facile à comprendre (c'est-à-dire, "expressif")
* Plus facile à réutiliser
* Plus facile à tester
* Plus facile à maintenir
* Plus facile à refactoriser
* Plus facile à optimiser
* Plus facile à raisonner

Ça a l'air excitant ? Venez pour le voyage !

[Inscrivez-vous dès maintenant au cours gratuit par e-mail](https://preethikasireddy.typeform.com/to/yC9qQr). Vous recevrez ensuite la première leçon dans votre boîte mail dans les 1 à 3 jours suivant votre inscription ?