---
title: Solution exacte pour « Exact Change »
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-03-21T18:21:46.000Z'
originalURL: https://freecodecamp.org/news/exact-solution-for-exact-change-81e1d23bfe58
coverImage: https://cdn-media-1.freecodecamp.org/images/1*GWYeOS6UQpnQTPOfrtU9VA.jpeg
tags:
- name: algorithms
  slug: algorithms
- name: JavaScript
  slug: javascript
- name: learning to code
  slug: learning-to-code
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Solution exacte pour « Exact Change »
seo_desc: 'By DemiPixel

  NOTE: If you’re working through Free Code Camp and haven’t completed this problem,
  I really recommend try it first!

  I was messing around with Free Code Camp and was challenged by someone to try and
  correctly complete the “Exact Change” p...'
---

Par DemiPixel

REMARQUE : Si vous travaillez sur Free Code Camp et n'avez pas encore résolu ce problème, je vous recommande vraiment d'essayer d'abord !

Je m'amusais avec Free Code Camp et quelqu'un m'a lancé le défi de tenter de résoudre correctement le problème « Exact Change ».

#### Le Problème

[Le problème Exact Change](https://www.freecodecamp.com/challenges/exact-change) vous demande d'écrire une fonction qui donne le nombre minimal de pièces pour atteindre un montant donné et un tableau 2D de pièces formaté comme suit :

```
[["PENNY", 1.01], ["NICKEL", 2.05], ["DIME", 3.10], ["QUARTER", 4.25], ["ONE", 90.00], ["FIVE", 55.00], ["TEN", 20.00], ["TWENTY", 60.00], ["ONE HUNDRED", 100.00]]
```

Remarquez comment il indique que nous avons 1,01 $ en pennies au lieu de dire « 101 pennies ».

#### Solution Incorrecte

Free Code Camp est destiné aux débutants, donc je peux comprendre que la réponse qu'ils fournissent soit la plus intuitive pour les personnes qui essaient de comprendre comment cela fonctionne. Malheureusement, l'algorithme n'a pas toujours l'effet souhaité. Vous pouvez voir l'extrait de code complet [ici](https://github.com/FreeCodeCamp/FreeCodeCamp/wiki/Algorithm-Exact-Change), mais voici un bref résumé de ce qu'il fait :

```
coinList = []
```

```
pour chaque dénomination    tant que amountLeft < coinValue && coinLeft > 0        Ajouter la pièce à coinList        coinLeft--        amountLeft -= coinValue
```

```
si (coinList.length == 0 || amountLeft > 0)  return "Fonds insuffisants"sinon return le tableau
```

Et bien que cela puisse sembler une solution simple et brillante, nous rencontrons quelques problèmes. On m'a spécifiquement défié pour le test suivant :

#### 0,30 $ avec des dimes et des quarters

Supposons que nous voulons obtenir 0,30 $ avec 10 dimes et 10 quarters (donc nous avons plus qu'assez de dimes ou de quarters). C'est là que l'algorithme précédent trébuche un peu.

La méthode qu'il utilise consiste à utiliser la plus haute dénomination et à descendre jusqu'à atteindre l'objectif ou la plus basse dénomination. Il essaie d'abord d'utiliser un quarter (puisque c'est la plus haute dénomination disponible) et il reste avec 0,05 $.

Puisque amountLeft (le montant d'argent restant à faire avec les pièces) est > 0, il retourne « Fonds insuffisants » parce qu'un dime vaut plus que 0,05 $ et qu'il n'y a pas d'autres dénominations restantes. Cependant, nous savons tous que la solution correcte est de faire 0,30 $ avec trois dimes !

Nous ne pouvons pas commencer par la plus basse dénomination et remonter (comme commencer par les dimes, puis passer aux quarters) car nous pourrions rencontrer un problème comme 0,40 $ avec 1 nickel, 3 dimes et 1 quarter.

Le programme commencera par essayer d'utiliser le nickel (0,05 $, plus basse dénomination), puis les 3 dimes (0,35 $, deuxième dénomination à utiliser), et retournera « Fonds insuffisants » parce que nous ne pouvons pas faire les 0,05 $ restants avec des dimes ni des quarters. Il n'a pas essayé 1 nickel, 1 dime et 1 quarter (ce qui fait exactement 0,40 $).

#### Problèmes plus petits

Commençons simplement. Comment pourrions-nous résoudre le problème si nous voulions les pièces pour faire 0,01 $ ? Eh bien, nous passons en revue les dénominations et vérifions que nous avons assez de cette pièce (c'est-à-dire assez de pennies) et que cette pièce vaut <= 0,01 $ (ce qu'un penny est).

Maintenant, regardons 0,02 $. Pour les humains, il est facile de voir que 0,02 $ est simplement deux pennies de plus que 0,00 $.

Cependant, pour un ordinateur, ce n'est pas si simple. Ce que nous pouvons faire pour l'ordinateur, c'est exprimer l'atteinte de 0,02 $ comme « 1 penny de plus que 0,01 $ ». Nous pouvons aussi exprimer 0,03 $ comme un penny de plus que 0,02 $.

![Image](https://cdn-media-1.freecodecamp.org/images/1*V03eYiLE2TQEkN-zUUyMfg.png)
_La meilleure façon d'obtenir 1,00 $ est d'essayer d'utiliser chaque dénomination et de voir quelles autres pièces vous auriez besoin. Ici, le meilleur choix est le billet de 1,00 $ car il ne nécessiterait aucune autre pièce._

Un exemple plus grand serait avec 1,00 $. 1,00 $ est un penny + 0,99 $ ou un nickel + 0,95 $ ou un dime + 0,90 $ ou un quarter + 0,75 $ ou un billet d'un dollar + 0,00 $. Puisqu'un billet de cinq dollars est supérieur à 1,00 $, nous l'ignorons simplement (et toute dénomination plus élevée).

Donc, si nous revenons à notre problème initial et voulons calculer 0,30 $ à partir de dimes et de quarters, nous devons d'abord calculer et sauvegarder la combinaison de pièces pour faire 0,01 $. Ensuite, calculer et sauvegarder pour 0,02 $. Puis pour 0,03 $, 0,04 $, 0,05 $, et ainsi de suite jusqu'à ce que nous arrivions à 0,30 $.

Chaque fois que nous voulons la valeur suivante (par exemple 0,20 $), nous regardons la valeur de 0,20 $ et soustrayons le type de pièce sur lequel nous nous trouvons dans la boucle de dénomination (par exemple, un dime).

Cela nous laisse avec 0,20 $ moins un dime, ce qui fait 0,10 $, et nous pouvons simplement dire « ajouter un dime + les pièces qui composent 0,10 $ ». Cela sera probablement représenté comme un tableau de pièces, donc imaginez que 0,10 $ est ["dime"]. Puisque nous disons que « un dime + les pièces qui composent 0,10 $ » donne 0,20 $, nous pouvons dire que 0,20 $ est ["dime", "dime"] parce que nous ajoutons une pièce supplémentaire (le dime) à notre liste.

Parfait ! 0,20 $ est deux dimes.

#### Meilleure Valeur

Si nous revenons à notre 1,00 $, nous avons beaucoup de façons d'atteindre la même valeur. Comment savons-nous laquelle est la meilleure ? Comment savons-nous s'il est préférable d'utiliser un billet d'un dollar, ou mieux d'utiliser un dime + 0,90 $ en pièces ? Nous pourrions dire « la plus grande dénomination est la meilleure ». Puisque le billet d'un dollar est notre plus grande dénomination utilisable, nous dirions simplement que le billet d'un dollar est le meilleur choix (et définir 1,00 $ à ["1 dollar"]).

Alors, que faire avec 0,30 $ donné 5 pennies, 3 dimes et 1 quarter ? En utilisant la méthode de la « plus grande dénomination », nous essaierions de faire 0,30 $ à partir de « dime + 0,20 $ » ou « quarter + 0,05 $ ». Il semble que le quarter soit la meilleure option (quarter + 0,05 $), alors qu'en réalité cela nous donne une réponse à six pièces (un quarter et cinq pennies), alors que nous voulons une réponse à trois pièces (trois dimes) !

Ce que nous voulons vraiment, c'est comparer le nombre de pièces. Puisqu'il y a moins de pièces dans 0,20 $ (deux dimes) que dans 0,05 $ (cinq pennies), le 0,20 $ + dime serait le choix optimal pour 0,30 $.

#### En Pratique

Puisque nous cherchons simplement la meilleure valeur pour 0,01 $, puis 0,02 $, puis 0,03 $, et ainsi de suite, nous pouvons simplement utiliser une boucle for au lieu de la récursivité ou d'une boucle while !

En réalité, il serait impossible de stocker les valeurs comme ["dime", "dime", "quarter"] comme je l'ai mentionné ci-dessus. La façon dont je l'ai stocké était avec un tableau d'entiers, au format [pennies, nickels, dimes, quarters, etc]. Donc 3 quarters et 2 dimes seraient [0, 0, 2, 3, 0, 0, 0, 0] (jusqu'au billet de 20 $ puisque c'est la dénomination maximale dans le problème).

Dans mon code, j'appelle le nombre de pièces un « score ». Si vous n'êtes pas familier avec cela, O(_), c'est un format qui permet aux programmeurs de montrer à quel point un programme spécifique est efficace et comment il se comportera lorsqu'il sera mis à l'échelle.

Maintenant, je voulais que l'algorithme soit O(money*denominations), mais devoir recalculer le score à chaque fois le rendrait O(money*denominations^2). Ce que j'ai décidé de faire, c'est simplement créer une autre variable pour stocker le score comme je stocke les meilleurs montants. Donc, si je voulais 0,30 $ à partir d'un dime + 0,20 $, je pourrais regarder bestScoreList[0,20 $] et voir qu'il donne la valeur « 2 ».

Puisqu'un dime est une pièce, nous faisons simplement bestScoreList[0,20 $] + 1 ce qui fait 3. Si cela vous confond, ne vous inquiétez pas. Rappelez-vous simplement que bestScoreList[i] (valeur exemple : 5) va sauvegarder le nombre de pièces dans best[i] (valeur exemple : [2, 0, 3, 0, 0, 0, 0, 0]) sans avoir à toujours le recalculer.

Enfin, dans notre problème de 0,30 $, nous obtenons 0,20 $ + un dime ou 0,05 $ + un quarter. Puisque 0,05 $ est 0 pièce (puisqu'il n'y a aucun moyen d'obtenir 0,05 $ avec des quarters et des dimes), il indique qu'un quarter est la meilleure solution.

La meilleure façon de contrer cela est de simplement ruiner le score si le score est 0 et qu'il n'accède pas à 0,00 $. Par exemple, 0,10 $ avec un dime pourrait retourner un score de « 1 » parce que 0,00 $ a un score de 0, et donc il ajoute 1. Si, cependant, nous avons 0,15 $ avec seulement des dimes, il retournerait un score de « 0 » parce que 0,05 $ a un score de 0 (aucun moyen de faire 0,05 $ avec des dimes !) et 0,05 $ n'est pas 0,00 $ (évidemment).

Nous ruinons le score parce que cela signifie que c'est une solution impossible (puisque nous voulons atteindre 0,00 $ et ce n'est pas possible avec cette dénomination spécifique).

#### Code

Voici le code et un cas de test du problème de 0,30 $ avec des dimes et des quarters. Il utilise un peu d'ES6, alors changez cela si vous ne pouvez pas l'utiliser pour une raison quelconque. Notez également que le problème a donné « cash given » (en espèces) et « price of item » en prix. Cela signifie que nous cherchons en fait à leur donner des pièces cash-price. Le voici !