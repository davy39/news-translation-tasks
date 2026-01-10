---
title: La programmation dynamique simplifiée
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-09-15T19:00:00.000Z'
originalURL: https://freecodecamp.org/news/dynamic-programming-made-easy
coverImage: https://www.freecodecamp.org/news/content/images/2020/09/thisisengineering-raeng-uOhBxB23Wao-unsplash.jpg
tags:
- name: Dynamic Programming
  slug: dynamic-programming
seo_title: La programmation dynamique simplifiée
seo_desc: 'By Ashwin Sharma P

  Dynamic Programming is an approach where the main problem is divided into smaller
  sub-problems, but these sub-problems are not solved independently.

  For a problem to be solved using dynamic programming, the sub-problems must be ove...'
---

Par Ashwin Sharma P

La programmation dynamique est une approche où le problème principal est divisé en sous-problèmes plus petits, mais ces sous-problèmes ne sont pas résolus indépendamment.

Pour qu'un problème soit résolu en utilisant la programmation dynamique, les sous-problèmes doivent se chevaucher. Cela signifie que deux sous-problèmes ou plus évalueront pour donner le même résultat.

Ainsi, nous utilisons la technique de mémoïsation pour rappeler le résultat des sous-problèmes déjà résolus pour une utilisation future. Nous utilisons ensuite le stockage en cache pour stocker ce résultat, qui est utilisé lorsqu'un sous-problème similaire est rencontré à l'avenir.

Examinons maintenant ce sujet plus en détail.

## Qu'est-ce que la mémoïsation ?

La mémoïsation est la technique de mémorisation des résultats de certains états spécifiques, qui peuvent ensuite être accessibles pour résoudre des sous-problèmes similaires. En d'autres termes, c'est une forme spécifique de mise en cache.

Cela garantit que les résultats déjà calculés sont stockés généralement sous forme de hashmap. Cela diminue considérablement le temps d'exécution et conduit également à un code moins compliqué.

Mais nous savons que tout avantage a un coût. Ainsi, lorsque nous utilisons la programmation dynamique, la complexité temporelle diminue tandis que la complexité spatiale augmente.

## Différentes approches en programmation dynamique

En programmation dynamique, nous pouvons utiliser soit une approche descendante, soit une approche ascendante.

L'approche descendante implique de résoudre le problème de manière directe et de vérifier si nous avons déjà calculé la solution au sous-problème.

Cette approche inclut des appels récursifs _(appels répétés de la même fonction)_. Elle construit une pile d'appels, ce qui entraîne des coûts de mémoire. Elle est également vulnérable aux erreurs de débordement de pile.

L'approche ascendante inclut d'abord l'examen des sous-problèmes plus petits, puis la résolution des sous-problèmes plus grands en utilisant la solution aux problèmes plus petits.

Cette approche évite les coûts de mémoire résultant de la récursivité.

Mais l'approche descendante et l'approche ascendante en programmation dynamique ont la même complexité temporelle et spatiale. Ainsi, à la fin, l'utilisation de l'une ou l'autre de ces approches ne fait pas grande différence.

Juste une note rapide : la programmation dynamique n'est pas un algorithme. Mais j'ai vu certaines personnes la confondre avec un algorithme (y compris moi-même au début).

Elle est utilisée uniquement lorsque nous avons un sous-problème chevauchant ou lorsque des appels récursifs extensifs sont nécessaires. C'est un moyen d'améliorer les performances des algorithmes existants lents.

Cela signifie également que la complexité temporelle et spatiale de la programmation dynamique varie selon le problème.

## Exemple de programmation dynamique

Résolvons maintenant un problème pour mieux comprendre comment fonctionne réellement la programmation dynamique.

Considérons le problème de trouver la plus longue sous-séquence commune à partir des deux séquences données.

➡ _'gtcab'_ et _'gxtxab'_

Nous pouvons résoudre ce problème en utilisant une approche naïve, en générant toutes les sous-séquences pour les deux et en trouvant ensuite la plus longue sous-séquence commune parmi elles.

Mais la complexité temporelle de cette solution croît exponentiellement à mesure que la longueur de l'entrée continue d'augmenter.

**Alors, comment savons-nous que ce problème peut être résolu en utilisant la programmation dynamique ?**

Pour les deux chaînes que nous avons prises, nous utilisons le processus ci-dessous pour calculer la plus longue sous-séquence commune (LCS).

Comme nous pouvons le voir, ici nous divisons le problème principal en sous-problèmes plus petits. Vérifions si un sous-problème est répété ici.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/freecodecamp_first_article--2.png)
_Division du problème principal en sous-problèmes_

Nous pouvons voir ici que deux sous-problèmes se chevauchent lorsque nous divisons le problème à deux niveaux.

Si nous continuons à diviser l'arbre, nous pouvons voir beaucoup plus de sous-problèmes qui se chevauchent. Nous concluons donc que cela peut être résolu en utilisant la programmation dynamique.

Ensuite, examinons l'approche générale par laquelle nous pouvons trouver la plus longue sous-séquence commune (LCS) en utilisant la programmation dynamique.

## Comment remplir la matrice ?

Nous utiliserons la méthode de la matrice pour comprendre la logique de résolution de la plus longue sous-séquence commune en utilisant la programmation dynamique.

Ici, nous ne discuterons que de la manière de résoudre ce problème – c'est-à-dire la partie algorithme. Et pour cela, nous utilisons la méthode de la matrice.

Regardez la matrice ci-dessous. Nous avons rempli la première ligne avec la première séquence et la première colonne avec la deuxième séquence.

Ensuite, nous avons peuplé la deuxième ligne et la deuxième colonne avec des zéros pour que l'algorithme commence. Nous désignons les lignes par **'i'** et les colonnes par **'j'**.

![Entrée de la matrice](https://www.freecodecamp.org/news/content/images/2020/09/freecodecamp_first_article2.png)
_Entrée de la matrice_

Maintenant, nous passons au remplissage des cellules de la matrice. Comparez les deux séquences jusqu'à la cellule particulière où nous sommes sur le point de faire l'entrée.

La longueur/compte des sous-séquences communes reste la même jusqu'à ce que le dernier caractère des deux séquences en cours de comparaison devienne le même.

Si les séquences que nous comparons n'ont pas leur dernier caractère égal, alors l'entrée sera le maximum de l'entrée dans la colonne à gauche et de l'entrée de la ligne au-dessus.

Lorsque les derniers caractères des deux séquences sont égaux, l'entrée est remplie en incrémentant l'entrée diagonale supérieure gauche de cette cellule particulière de **1**.

**La logique que nous utilisons ici pour remplir la matrice est donnée ci-dessous :**

```
if(input[i]==input[j])              //Vérifie si les derniers caractères sont égaux
T[i][j]=T[i-1][j-1]+1               //L'entrée est l'incrément de l'élément en haut à gauche
else                                //Si les derniers caractères ne sont pas égaux
T[i][j]=max(T[i-1][j], T[i][j-1])   //L'entrée est le max de l'élément à sa gauche et en haut
```

L'entrée en bas à droite de toute la matrice nous donne la longueur de la plus longue sous-séquence commune.

## Trouver la plus longue sous-séquence commune

Pour obtenir la plus longue sous-séquence commune, nous devons parcourir à partir du coin inférieur droit de la matrice. Ensuite, nous vérifions d'où provient l'entrée particulière.

C'est-à-dire, nous pouvons vérifier _si elle est le maximum de son entrée à gauche et en haut_ ou si elle est _l'entrée incrémentale de l'élément diagonal supérieur gauche ?_

Nous répétons ce processus jusqu'à ce que nous atteignions le coin supérieur gauche de la matrice. La sous-séquence que nous obtenons en combinant le chemin que nous parcourons _(ne considérer que les caractères où la flèche se déplace en diagonale)_ sera dans l'ordre inverse.

Nous devons inverser cette séquence obtenue pour obtenir la plus longue sous-séquence commune correcte. Ainsi, dans cet exemple particulier, la plus longue sous-séquence commune est **'gtab'**.

J'ai fait une vidéo détaillée sur la manière dont nous remplissons la matrice afin que vous puissiez mieux comprendre. Vous pouvez la trouver ici : [**Explication vidéo**](https://youtu.be/hVx1X46iLVk).

## Qu'avons-nous appris ?

Dans cet article, nous avons appris ce qu'est la programmation dynamique et comment identifier si un problème peut être résolu en utilisant la programmation dynamique.

Ensuite, nous avons étudié la complexité d'un problème de programmation dynamique.

Ensuite, nous avons appris comment résoudre le problème de la plus longue sous-séquence commune en utilisant la programmation dynamique.

J'espère que vous l'avez apprécié et que vous avez appris quelque chose d'utile dans cet article.

Si vous avez trouvé cet article utile, veuillez le partager. Si vous avez des commentaires, n'hésitez pas à me contacter sur [Twitter](https://twitter.com/ashwinsharmap).