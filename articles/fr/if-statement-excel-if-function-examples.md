---
title: Instruction IF Excel – Exemples de la fonction Si
subtitle: ''
author: Ilenia Magoni
co_authors: []
series: null
date: '2021-08-16T16:10:37.000Z'
originalURL: https://freecodecamp.org/news/if-statement-excel-if-function-examples
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/pexels-energepiccom-159888.jpg
tags:
- name: data analysis
  slug: data-analysis
- name: excel
  slug: excel
seo_title: Instruction IF Excel – Exemples de la fonction Si
seo_desc: 'If you are analysing data in Excel and need to set the value of a cell
  conditionally, you can use an IF statement to do so.

  The syntax is IF(logical_test, [value_if_true], [value_if_false]), where:


  logical_test is an expression that evaluates to TRU...'
---

Si vous analysez des données dans Excel et que vous devez définir la valeur d'une cellule de manière conditionnelle, vous pouvez utiliser une instruction `IF` pour ce faire.

La syntaxe est `IF(logical_test, [value_if_true], [value_if_false])`, où :

* `logical_test` est une expression qui évalue à `TRUE` ou `FALSE`,
* `value_if_true` est un argument facultatif, et c'est ce à quoi l'expression évalue si `logical_test` est vrai, et
* `value_if_false` est un argument facultatif qui détermine la valeur dans le cas où `logical_test` est faux.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/image-65.png)

# Exemples d'instruction IF

Voyons comment nous pouvons utiliser l'instruction `IF` en pratique pour mieux comprendre comment elle fonctionne.

## Exemple d'instruction IF 1

Supposons que nous avons une liste d'étudiants et les notes qu'ils ont obtenues à un examen, comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/08/image-60.png)

Nous voulons marquer chaque étudiant comme ayant réussi ou échoué à l'examen, et nous pouvons utiliser une instruction `IF` pour vérifier si leur note est inférieure ou supérieure à la note de passage. Une note de passage est 60, donc si les étudiants ont obtenu moins de 60, cela signifie qu'ils ont échoué à l'examen, sinon ils l'ont réussi.

Nous pouvons écrire cela dans Excel comme `IF(B2<60, "échoué", "réussi")`, comme ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/image-63.png)

Ensuite, nous pouvons simplement remplir ces informations dans toutes les cellules de la colonne. Nous obtiendrons ce résultat :

![Image](https://www.freecodecamp.org/news/content/images/2021/08/image-62.png)

J'ai utilisé un peu de [mise en forme conditionnelle](https://support.microsoft.com/en-us/office/use-conditional-formatting-to-highlight-information-fed60dfa-1d3f-4e13-9ecb-f1951ff89d7f) pour faciliter la distinction entre les deux résultats.

## Exemple d'instruction IF 2

Vous pouvez également imbriquer des instructions if pour une logique plus complexe. J'ai écrit sur la façon de le faire dans [cet article](https://www.freecodecamp.org/news/if-function-excel-tutorial-and-how-to-do-multiple-if-statements-in-excel/). Voyons cela à nouveau ici avec un exemple dans le domaine médical.

Nous avons les résultats des analyses sanguines d'un patient, ainsi que les valeurs de la plage normale (qui diffèrent en fonction du sexe du patient). Utilisons une instruction `IF` pour vérifier si les résultats des analyses sanguines sont à l'intérieur ou à l'extérieur de la plage normale :

![Image](https://www.freecodecamp.org/news/content/images/2021/08/image-68.png)

Les plages normales pour les patients masculins et féminins sont différentes, nous devons donc vérifier le sexe du patient avant de savoir quelle plage utiliser pour vérifier le résultat du test.

Nous commençons d'abord par vérifier `$H$1="male"` (nous utilisons le symbole `$` pour fixer cette cellule lorsque nous copions et collons la formule dans d'autres cellules). Ensuite, nous utilisons une instruction `IF` imbriquée pour comparer la valeur de l'analyse sanguine à la plage.

Si le patient est de sexe masculin, nous utilisons `IF(OR(J2<C2, J2>D2), "ANORMAL", "normal")`. Si le patient est de sexe féminin, nous utilisons `IF(OR(J2<C3, J2>D3), "ANORMAL", "normal")`.

[La fonction `OR`](https://support.microsoft.com/en-us/office/or-function-7d17ad14-8700-4281-b308-00b131e22af0) retourne vrai si au moins un des arguments est vrai, et faux si aucun des arguments n'est vrai. Dans ce cas, nous l'utilisons pour vérifier si le résultat du test est inférieur à la valeur inférieure de la plage ou supérieur à la valeur supérieure de la plage. Si il est en dehors de la plage, nous retournons `ANORMAL`, et s'il est dans la plage, nous retournons `normal`.

Ensemble, la formule ressemble à ceci :

`=IF(H$1="male", IF(OR(J2<C2, J2>D2), "ANORMAL", "normal"), IF(OR(J2<C3, J2>D3), "ANORMAL", "normal"))`.

Pour le nombre de globules blancs et le nombre de plaquettes, il n'y a pas de différence basée sur le sexe du patient, donc la formule est plus simple :

`=IF(OR(J8<C8, J8>D8), "ANORMAL", "normal")`.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/image-67.png)

## Exemple d'instruction IF 3

Dans ce troisième exemple, considérons ce qu'un groupe de commerciaux a pu vendre sur une certaine période.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/image-69.png)

Dans ce groupe, s'ils ont pu vendre plus que la moyenne, ils obtiennent un bonus. Vérifions donc chacun de leurs gains par rapport à la moyenne avec cette formule :

`=IF(B2>B$10, "BONUS !", "non")`

![Image](https://www.freecodecamp.org/news/content/images/2021/08/image-72.png)

Il semble que quatre d'entre eux recevront un bonus pour cette période !

# Conclusion

Si vous devez analyser des données, alors l'instruction `IF` dans Excel est assez utile.

Nous l'avons vue ici en action à travers trois exemples différents, mais ce que vous pouvez faire avec elle n'est limité que par votre créativité. Amusez-vous !