---
title: Apprendre la programmation fonctionnelle m'a rendu 10 fois meilleur développeur
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-02T14:55:05.000Z'
originalURL: https://freecodecamp.org/news/learn-the-fundamentals-of-functional-programming
coverImage: https://www.freecodecamp.org/news/content/images/2019/11/Screen-Shot-2019-11-28-at-12.23.08-PM-2.png
tags:
- name: Functional Programming
  slug: functional-programming
- name: technology
  slug: technology
seo_title: Apprendre la programmation fonctionnelle m'a rendu 10 fois meilleur développeur
seo_desc: 'By Preethi Kasireddy

  Learning functional programming made me a 10x better developer. It helped me learn
  how write code that is clean, easy to maintain, and scalable.

  This is especially important in this day and age where software applications keep
  ge...'
---

Par Preethi Kasireddy

Apprendre la programmation fonctionnelle m'a rendu 10 fois meilleur développeur. Cela m'a aidé à apprendre à écrire du code qui est propre, facile à maintenir et évolutif.

Cela est particulièrement important de nos jours où **les applications logicielles deviennent de plus en plus compliquées.** Les jours de construction et de maintenance d'une simple application web sont révolus.

En tant que développeur, les attentes placées sur vous sont plus élevées que jamais. Il incombe désormais à nos épaules de construire, tester, maintenir et mettre à l'échelle des applications complexes qui impactent des millions de personnes quotidiennement. Cela peut être particulièrement décourageant pour un débutant car nous commençons tout juste à maîtriser l'écriture de code qui fonctionne réellement, sans parler d'écrire du code qui est facile à comprendre, écrire, déboguer, réutiliser et maintenir.

C'est là que la programmation fonctionnelle a fait la différence pour moi—elle m'a aidé à apprendre à coder de manière facile à comprendre, écrire, déboguer, réutiliser et maintenir. En conséquence, je me sens beaucoup plus confiant dans mes capacités de codage.

Même si vous n'utilisez pas un langage de programmation fonctionnelle au travail ou dans vos projets personnels, connaître les bases de la programmation fonctionnelle vous équipe d'un ensemble puissant d'outils pour écrire un meilleur code.

Dans mon nouveau [e-book](https://gum.co/CkFTl), je vous enseignerai les bases de la programmation fonctionnelle afin que vous ayez toutes les connaissances fondamentales nécessaires pour appliquer les principes au travail, lors de votre prochain entretien d'embauche ou dans votre prochain projet personnel.

Le reste de l'article vous donnera une explication simple de ce qu'est la programmation fonctionnelle, ce que vous devez savoir avant de plonger dans le [e-book](https://gum.co/CkFTl). ?

Commençons tout de suite ! ?

# Qu'est-ce que la programmation fonctionnelle ?

Alors. Qu'est-ce que la "programmation fonctionnelle", exactement ?

La programmation fonctionnelle n'est pas un framework ou un outil, mais une _manière_ d'écrire du code. En programmation fonctionnelle, nous mettons un accent majeur sur l'écriture de code en utilisant des **fonctions comme "blocs de construction".**

Votre programme est défini en termes d'une fonction principale. Cette fonction principale est définie en termes d'autres fonctions, qui sont à leur tour définies en termes de encore plus de fonctions — jusqu'au niveau le plus bas où les fonctions sont simplement des primitives de langage comme "nombre" ou "chaîne".

![Image](https://www.freecodecamp.org/news/content/images/2019/11/1_u9reFf6xlLAZAEhFZznn0w.png)

Si vous lisez ceci en pensant, _"Hmm, mais attendez ? Est-ce que chaque langage n'utilise pas des fonctions pour écrire du code ?"_ alors bien ?. Cela signifie que vous faites attention.  
  
Vous avez raison — chaque langage de programmation a des fonctions. Mais la programmation fonctionnelle le porte à un tout autre niveau ?

![Image](https://www.freecodecamp.org/news/content/images/2019/11/1_7xgYTLL5_cPr9QRrOzjoeQ.png)

Pour comprendre ce que je veux dire, revenons en arrière et commençons par les bases.  
  
Chaque programme logiciel a deux choses :

1. **Comportement** (ce que le programme fait)
2. **Données** (les données, eh bien, sont des données)

Lorsque nous apprenons un paradigme de programmation — comme la programmation fonctionnelle — il est souvent utile de considérer comment le paradigme aborde le comportement et les données respectivement.  
  
**Le comportement**, en programmation fonctionnelle, est géré purement en utilisant des **fonctions** en programmation fonctionnelle. Les fonctions sont des morceaux de code "auto-contournés" qui accomplissent une tâche spécifique. Elles définissent une relation entre un ensemble d'entrées possibles et un ensemble de sorties possibles — elles prennent généralement des données, les traitent et retournent un résultat. Une fois qu'une fonction est écrite, elle peut être utilisée encore et encore.

**Les données**, en programmation fonctionnelle, sont immuables — ce qui signifie qu'elles ne peuvent pas être changées. Plutôt que de changer les données qu'elles prennent en entrée, les fonctions en programmation fonctionnelle prennent des données en entrée et produisent des **nouvelles** valeurs en sortie. Toujours.

**Les fonctions** et les **données immuables** sont les deux seules choses avec lesquelles vous devez traiter en programmation fonctionnelle. Pour simplifier encore, les fonctions sont traitées de la même manière que les données.

En d'autres termes, les fonctions en programmation fonctionnelle peuvent être transmises aussi facilement que des données. Vous pouvez vous référer à elles à partir de _constantes_ et de _variables_, les passer en tant que _paramètres_ à d'autres fonctions, et les retourner en tant que _résultats_ d'autres fonctions.  
  
C'est la chose la plus importante à comprendre lorsque l'on aborde la programmation fonctionnelle.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/1__jVtvLPzVIlJaKatp_48Wg.png)

En traitant les fonctions comme rien de plus spécial qu'un morceau de données et en n'utilisant que des données immuables, nous avons beaucoup plus de liberté en termes de la manière dont nous pouvons utiliser les fonctions.

À savoir, cela nous permet de créer de petites fonctions indépendantes qui peuvent être réutilisées et combinées ensemble pour construire une logique de plus en plus complexe. Nous pouvons **décomposer tout problème complexe en sous-problèmes plus petits, les résoudre en utilisant des fonctions, et enfin les combiner pour résoudre le problème plus grand.**  
  
Considérant la complexité croissante des applications logicielles, ce type d'approche "bloc de construction" fait une énorme différence pour garder les programmes simples, modulaires et compréhensibles. C'est aussi pourquoi les développeurs s'efforcent de rendre leurs fonctions aussi **polyvalentes** que possible, afin qu'elles puissent être **combinées** pour résoudre de grands problèmes complexes et **réutilisées** pour accélérer le temps de développement des programmes suivants.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/1_1kZojkIWzzSASoxtu3SctQ.png)

En fin de compte, la raison pour laquelle les fonctions sont si puissantes en programmation fonctionnelle est que les fonctions suivent certains principes de base. Ces principes seront le sujet de mon cours par email :

* Les fonctions sont pures
* Les fonctions utilisent des données immuables
* Les fonctions garantissent la transparence référentielle
* Les fonctions sont des entités de première classe

Après cela, je toucherai brièvement à la manière dont la programmation fonctionnelle applique ces principes pour nous encourager à réfléchir soigneusement à nos données et aux fonctions qui interagissent avec elles.

À la fin, vous serez en mesure de comprendre comment cette approche conduit à un code qui est :

* Plus facile à comprendre (c'est-à-dire, "expressif")
* Plus facile à réutiliser
* Plus facile à tester
* Plus facile à maintenir
* Plus facile à refactoriser
* Plus facile à optimiser
* Plus facile à raisonner

Cela semble excitant ? Si oui, vous allez adorer le nouveau [e-book.](https://gum.co/CkFTl) ?

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screen-Shot-2019-11-28-at-12.23.08-PM-1.png)

Le [e-book](https://gum.co/CkFTl) sera publié le **13 décembre**. **Vous pouvez pré-commander **[le e-book](https://gum.co/CkFTl)**** maintenant pour seulement **49 $ !** Et en offre spéciale pour la communauté freeCodeCamp, je propose **10 $ de réduction** avec le code de réduction "**freecodecamp**".

À bientôt ! ??f4ddf3fb