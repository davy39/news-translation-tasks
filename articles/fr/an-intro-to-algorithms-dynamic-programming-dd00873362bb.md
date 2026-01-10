---
title: 'Une introduction aux algorithmes : la programmation dynamique'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-30T15:33:33.000Z'
originalURL: https://freecodecamp.org/news/an-intro-to-algorithms-dynamic-programming-dd00873362bb
coverImage: https://cdn-media-1.freecodecamp.org/images/1*aExd095nIEBdoJ_ANTVCbw.png
tags:
- name: algorithms
  slug: algorithms
- name: coding
  slug: coding
- name: Dynamic Programming
  slug: dynamic-programming
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: 'Une introduction aux algorithmes : la programmation dynamique'
seo_desc: 'By Meet Zaveri

  Suppose you are doing some calculation using an appropriate series of input. There
  is some computation done at every instance to derive some result. You don’t know
  that you had encountered the same output when you had supplied the same...'
---

Par Meet Zaveri

Supposons que vous effectuez un calcul en utilisant une série appropriée d'entrées. Il y a un calcul effectué à chaque instance pour obtenir un résultat. Vous ne savez pas que vous avez rencontré la **même sortie** lorsque vous avez fourni la **même entrée**. C'est comme si vous refaisiez un calcul de résultat qui avait déjà été obtenu par une entrée spécifique pour sa sortie respective.

Mais quel est le problème ici ? Le problème est que votre temps précieux est gaspillé. Vous pouvez facilement résoudre le problème en conservant des enregistrements qui mappent les résultats précédemment calculés. Par exemple, vous pourriez stocker l'entrée comme clé et la sortie comme valeur (faisant partie du mappage).

> Ceux qui ne peuvent pas se souvenir du passé sont condamnés à le répéter. ~Programmation dynamique

Maintenant, en analysant le problème, stockez son entrée si elle est nouvelle (ou non dans la structure de données) avec sa sortie respective. Sinon, vérifiez cette clé d'entrée et obtenez la sortie résultante à partir de sa valeur. Ainsi, lorsque vous effectuez un calcul et vérifiez si cette entrée existait dans cette structure de données, vous pouvez obtenir directement le résultat. Ainsi, nous pouvons relier cette approche aux techniques de programmation dynamique.

### Plonger dans la programmation dynamique

En résumé, nous pouvons dire que la programmation dynamique est utilisée principalement pour optimiser les problèmes, où nous souhaitons trouver la "meilleure" façon de faire quelque chose.

Un certain scénario est que des sous-problèmes récurrents apparaissent, qui à leur tour ont leurs propres sous-problèmes plus petits. Au lieu d'essayer de résoudre ces sous-problèmes réapparaissants encore et encore, la programmation dynamique suggère de résoudre chacun des sous-problèmes plus petits une seule fois. Ensuite, vous enregistrez les résultats dans un tableau à partir duquel une solution au problème original peut être obtenue.

Par exemple, les nombres de [Fibonacci](http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fibonacci/fib.html) `0,1,1,2,3,5,8,13,…` ont une description simple où chaque terme est lié aux deux termes précédents. Si `F(n)` est le `n`ième terme de cette série, alors nous avons `F(n) = F(n-1) + F(n-2)`. Cela s'appelle une **formule récursive** ou une **relation de récurrence**. Elle nécessite que les termes précédents aient été calculés afin de calculer un terme ultérieur.

![Image](https://cdn-media-1.freecodecamp.org/images/2MrMcNofQOnzWkh-hkALV4udgyak1WqE7D1w)

La majorité des problèmes de programmation dynamique peuvent être catégorisés en deux types :

1. **Problèmes d'optimisation.**
2. **Problèmes combinatoires.**

Les problèmes d'optimisation vous demandent de sélectionner une solution réalisable de sorte que la valeur de la fonction requise soit minimisée ou maximisée. Les problèmes combinatoires vous demandent de déterminer le nombre de façons de faire quelque chose ou la probabilité qu'un événement se produise.

### Une approche pour résoudre : de haut en bas vs de bas en haut

Il existe deux principales façons différentes de résoudre le problème :

**De haut en bas :** Vous commencez par le haut, en résolvant le problème en le décomposant. Si vous voyez que le problème a déjà été résolu, alors retournez simplement la réponse sauvegardée. Cela est appelé **_Mémoïsation_**.

**De bas en haut :** Vous commencez directement à résoudre les sous-problèmes plus petits, en remontant vers le haut pour obtenir la solution finale de ce grand problème. Dans ce processus, il est garanti que les sous-problèmes sont résolus avant de résoudre le problème. Cela peut être appelé **_Tabulation_** (**algorithme de remplissage de tableau**).

En référence à l'itération vs la récursion, le bas en haut utilise l'itération et le haut en bas utilise la récursion.

![Image](https://cdn-media-1.freecodecamp.org/images/bcZt7dF4Z8GUcRAicU7eETW98YOikSzsJqKa)
_La visualisation affichée dans l'image n'est pas correcte selon les connaissances théoriques, mais je l'ai affichée de manière compréhensible_

Ici, il y a une comparaison entre une approche naïve et une approche DP. Vous pouvez voir la différence par la complexité temporelle des deux.

### Mémoïsation : Ne pas oublier

[Jeff Erickson](http://jeffe.cs.illinois.edu/) décrit dans ses notes, pour les nombres de Fibonacci :

> La raison évidente du manque de vitesse de l'algorithme récursif est qu'il calcule les mêmes nombres de Fibonacci encore et encore.

![Image](https://cdn-media-1.freecodecamp.org/images/y9J0-FSzmI3RgyCX1FOkgFOfoy0gnKZtTObP)
_Notes de Jeff Erickson CC : [http://jeffe.cs.illinois.edu/](http://jeffe.cs.illinois.edu/" rel="noopener" target="_blank" title=")_

Nous pouvons accélérer considérablement notre algorithme récursif simplement en notant les résultats de nos appels récursifs. Ensuite, nous pouvons les consulter à nouveau si nous en avons besoin plus tard.

**Mémoïsation** fait référence à la technique de mise en cache et de réutilisation des résultats précédemment calculés.

Si vous utilisez la mémoïsation pour résoudre le problème, vous le faites en maintenant une carte des sous-problèmes déjà résolus (comme nous en avons parlé plus tôt, le **mappage** de la clé et de la valeur). Vous le faites "**de haut en bas**" dans le sens où vous résolvez d'abord le problème "du haut" (qui récurse généralement vers le bas pour résoudre les sous-problèmes).

**Pseudocode pour la mémoïsation :**

![Image](https://cdn-media-1.freecodecamp.org/images/Zc2XojBYGYnFvIdKnjs-vh5uy-TETK5h2guX)

Ainsi, en utilisant la récursion, nous effectuons cela avec une mémoire supplémentaire (c'est-à-dire ici la recherche) pour stocker les résultats. Si une valeur est stockée dans la recherche, nous la retournons directement ou nous l'ajoutons à la recherche pour cet index spécifique.

N'oubliez pas qu'il y a un compromis de mémoire supplémentaire par rapport à la méthode de tabulation.

Cependant, si vous voulez plus de visualisations pour la mémoïsation, je vous suggère de regarder [cette vidéo](https://www.youtube.com/watch?v=Taa9JDeakyU).

![Image](https://cdn-media-1.freecodecamp.org/images/pw42NcPn9a9mVCLeKSQI-y75vTGTcQifI8Pt)
_De manière descendante._

### Tabulation : Remplissage sous forme tabulaire

Mais une fois que nous voyons comment le tableau (solution mémoïsée) est rempli, nous pouvons remplacer la récursion par une simple boucle qui remplit intentionnellement le tableau dans l'ordre, au lieu de compter sur la récursion compliquée pour le faire pour nous 'accidentellement'.

![Image](https://cdn-media-1.freecodecamp.org/images/N61EAtUcJ04sfTINdBEzulljU56WqnSGPelV)
_Notes de Jeff Erickson CC : [http://jeffe.cs.illinois.edu/](http://jeffe.cs.illinois.edu/" rel="noopener" target="_blank" title=")_

La tabulation le fait de manière "**de bas en haut**". C'est plus direct, elle calcule toutes les valeurs. Elle nécessite moins de mémoire car elle n'a pas à maintenir de mappage et stocke les données sous forme tabulaire pour chaque valeur. Elle peut également calculer des valeurs inutiles. Cela peut être utilisé si tout ce que vous voulez est de calculer toutes les valeurs pour votre problème.

**Pseudocode pour la tabulation :**

![Image](https://cdn-media-1.freecodecamp.org/images/sluFNyPCslPYri9s1Jip7-xyYdvKJcOWlnhJ)
_Pseudocode avec l'arbre de Fibonacci_

Comme vous pouvez le voir dans le pseudocode (côté droit) sur une image, il utilise l'itération (c'est-à-dire des boucles jusqu'à la fin d'un tableau). Il commence simplement par fib(0), fib(1), fib(2), … Ainsi, avec l'approche de tabulation, nous pouvons éliminer le besoin de récursion et simplement retourner le résultat en bouclant sur les éléments.

### Retour sur l'histoire

Richard Bellman était l'homme derrière ce concept. Il a eu cette idée lorsqu'il travaillait pour la RAND Corporation au milieu des années 1950. La raison pour laquelle il a choisi ce nom "programmation dynamique" était de cacher le travail mathématique qu'il avait fait pour cette recherche. Il avait peur que ses patrons s'opposent ou n'aiment pas tout type de recherche mathématique.

D'accord, donc le mot "programmation" est juste une référence pour clarifier que c'était une manière à l'ancienne de planifier ou de programmer, typiquement en remplissant un tableau (de manière dynamique plutôt que linéaire) au fil du temps plutôt que tout à la fois.

#### Conclusion

C'est tout. Cela fait partie de la série d'algorithmes que j'ai commencée l'année dernière. Dans mon [précédent article](https://codeburst.io/algorithms-i-searching-and-sorting-algorithms-56497dbaef20), nous avons discuté des algorithmes de recherche et de tri. Je m'excuse de ne pas avoir pu livrer cela plus tôt. Mais je suis prêt à accélérer les choses dans les mois à venir.

J'espère que cela vous a plu et je chercherai bientôt à ajouter un troisième article dans la série. Bon codage !

Ressources :

[**Introduction à la programmation dynamique 1 Tutoriels & Notes | Algorithmes | HackerEarth**](https://www.hackerearth.com/practice/algorithms/dynamic-programming)
[L'image ci-dessus en dit long sur la programmation dynamique. Donc, est-ce répéter les choses pour lesquelles vous avez déjà... www.hackerearth.com](https://www.hackerearth.com/practice/algorithms/dynamic-programming)
[**Communauté — Programmation compétitive — Tutoriels de programmation compétitive — Programmation dynamique : De...**](https://www.topcoder.com/community/competitive-programming/tutorials/dynamic-programming-from-novice-to-advanced/)
[Communauté — Programmation compétitive — Tutoriels de programmation compétitive — Programmation dynamique : De débutant à avancé www.topcoder.com](https://www.topcoder.com/community/competitive-programming/tutorials/dynamic-programming-from-novice-to-advanced/)

[https://www.geeksforgeeks.org/overlapping-subproblems-property-in-dynamic-programming-dp-1/](https://www.geeksforgeeks.org/overlapping-subproblems-property-in-dynamic-programming-dp-1/)

Un merci spécial à Jeff Erickson et ses notes sur les algorithmes — [http://jeffe.cs.illinois.edu/](http://jeffe.cs.illinois.edu/)

![Image](https://cdn-media-1.freecodecamp.org/images/3MSAzv4xVUKSIIQEkTfiAK2lq8mzGKmmOBzB)