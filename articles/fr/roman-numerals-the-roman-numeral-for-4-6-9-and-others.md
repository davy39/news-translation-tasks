---
title: Les chiffres romains – les chiffres romains pour 4, 6, 9 et autres
subtitle: ''
author: Kristofer Koishigawa
co_authors: []
series: null
date: '2022-03-28T17:41:16.000Z'
originalURL: https://freecodecamp.org/news/roman-numerals-the-roman-numeral-for-4-6-9-and-others
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/thomas-bormans-JsTmUnHdVYQ-unsplash.jpg
tags:
- name: Math
  slug: math
- name: Mathematics
  slug: mathematics
seo_title: Les chiffres romains – les chiffres romains pour 4, 6, 9 et autres
seo_desc: 'Roman numerals are a numerical system that originated in ancient Rome.
  They are used to represent numbers in the decimal system, but they are not used
  for mathematical operations.

  In this system, symbols are used to represent different numbers, with ...'
---

Les chiffres romains sont un système de numération qui a vu le jour dans la Rome antique. Ils sont utilisés pour représenter des nombres dans le système décimal, mais ils ne sont pas utilisés pour les opérations mathématiques.

Dans ce système, des symboles sont utilisés pour représenter différents nombres : I représente 1, V représente 5, X représente 10, L représente 50, C représente 100, D représente 500 et M représente 1 000.

Voici un tableau des symboles utilisés dans le système des chiffres romains :

<table>
  <thead>
    <tr>
      <th style="text-align: center">1</th>
      <th style="text-align: center">5</th>
      <th style="text-align: center">10</th>
      <th style="text-align: center">50</th>
      <th style="text-align: center">100</th>
      <th style="text-align: center">500</th>
      <th style="text-align: center">1 000</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align: center">I</td>
      <td style="text-align: center">V</td>
      <td style="text-align: center">X</td>
      <td style="text-align: center">L</td>
      <td style="text-align: center">C</td>
      <td style="text-align: center">D</td>
      <td style="text-align: center">M</td>
    </tr>
  </tbody>
</table>

La valeur d'un chiffre est déterminée par sa position par rapport aux autres symboles. Lorsqu'un symbole de valeur égale ou inférieure est placé après un autre symbole, leurs valeurs s'additionnent. Mais lorsque certains symboles de valeur inférieure sont placés avant un autre symbole, leurs valeurs sont soustraites.

Par exemple, le chiffre VI, ou 6, se lirait « cinq plus un » (5 + 1), et XI, ou 11, est « dix plus un » (10 + 1).

Mais les méthodes de représentation de 4 et 9 sont spéciales. Le chiffre romain IV, ou 4, se lirait « un de moins que 5 » (5 - 1). De même, le chiffre IX, ou 9, se lirait « un de moins que 10 » (10 - 1).

Voici un tableau des nombres et de leur équivalent en chiffres romains, suivi d'explications plus détaillées sur la manière d'effectuer les conversions. Faites simplement défiler le tableau ou utilisez Ctrl/Cmd + f pour trouver la valeur que vous recherchez :

| Nombre | Chiffre romain |
|--------|---------------|
| 1      | I             |
| 2      | II            |
| 3      | III           |
| 4      | IV            |
| 5      | V             |
| 6      | VI            |
| 7      | VII           |
| 8      | VIII          |
| 9      | IX            |
| 10     | X             |
| 11     | XI            |
| 12     | XII           |
| 13     | XIII          |
| 14     | XIV           |
| 15     | XV            |
| 16     | XVI           |
| 17     | XVII          |
| 18     | XVIII         |
| 19     | XIX           |
| 20     | XX            |
| 21     | XXI           |
| 22     | XXII          |
| 23     | XXIII         |
| 24     | XXIV          |
| 25     | XXV           |
| 30     | XXX           |
| 40     | XL            |
| 50     | L             |
| 60     | LX            |
| 70     | LXX           |
| 80     | LXXX          |
| 90     | XC            |
| 100    | C             |
| 101    | CI            |
| 102    | CII           |
| 103    | CIII          |
| 104    | CIV           |
| 105    | CV            |
| 200    | CC            |
| 300    | CCC           |
| 400    | CD            |
| 500    | D             |
| 600    | DC            |
| 700    | DCC           |
| 800    | DCCC          |
| 900    | CM            |
| 1 000  | M             |
| 1 001  | MI            |
| 1 002  | MII           |
| 1 003  | MIII          |
| 1 004  | MIV           |
| 1 005  | MV            |
| 1 900  | MCM           |
| 2 000  | MM            |
| 3 000  | MMM           |
| 3 999  | MMMCMXCIX     |

## Comment convertir un nombre en chiffres romains

Comme les chiffres romains sont souvent ordonnés du plus grand au plus petit, décomposez le nombre que vous convertissez en groupes de milliers, centaines, dizaines et unités, puis effectuez la conversion sur chaque groupe.

Par exemple, si vous souhaitez convertir le nombre 2 014 (l'année de fondation de freeCodeCamp) en chiffres romains, décomposez le nombre comme suit :

```
2 014 = 2 000 + 10 + 4
```

Ensuite, effectuez la conversion pour chaque groupe et combinez-les pour obtenir l'équivalent en chiffre romain :

```
* 2 000 = MM
* 10 = X
* 4 = IV

2 014 = 2 000 + 10 + 4 = MMXIV
```

## Comment représenter de grands nombres en chiffres romains

Vous avez peut-être remarqué que le tableau ci-dessus ne va que de 1 à 3 999.

Cela est dû aux méthodes spéciales de représentation de 4 et 9 mentionnées précédemment. Si vous consultez le tableau ci-dessus, vous verrez que chaque fois qu'un 4 ou un 9 apparaît (y compris 40, 90, 400, 900), les chiffres romains sont ordonnés de manière particulière afin que le symbole inférieur soit soustrait de celui de plus grande valeur qui le suit immédiatement.

Comme les chiffres romains n'ont jamais été totalement standardisés, il se peut que vous voyiez le nombre 4 000 représenté par MMMM.

Cela fonctionne, mais beaucoup considèrent cela comme invalide car 4 (et 9) ont des représentations spéciales dans les nombres inférieurs.

Au lieu de cela, l'une des façons les plus courantes de représenter des chiffres romains plus grands est d'utiliser un [vinculum](https://en.wikipedia.org/wiki/Roman_numerals#Vinculum), ou une ligne horizontale droite au-dessus d'un ou plusieurs symboles.

Si vous voyez un symbole de chiffre romain surmonté d'une ligne horizontale, cela signifie simplement qu'il faut multiplier ce symbole par 1 000.

Voici les symboles des chiffres romains avec le vinculum appliqué :

<table>
  <thead>
    <tr>
      <th style="text-align: center">1 000</th>
      <th style="text-align: center">5 000</th>
      <th style="text-align: center">10 000</th>
      <th style="text-align: center">50 000</th>
      <th style="text-align: center">100 000</th>
      <th style="text-align: center">500 000</th>
      <th style="text-align: center">1 000 000</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align: center;">M ou <span style="text-decoration: overline;">I</span></td>
      <td style="text-align: center; text-decoration: overline;">V</td>
      <td style="text-align: center; text-decoration: overline;">X</td>
      <td style="text-align: center; text-decoration: overline;">L</td>
      <td style="text-align: center; text-decoration: overline">C</td>
      <td style="text-align: center; text-decoration: overline;">D</td>
      <td style="text-align: center; text-decoration: overline;">M</td>
    </tr>
  </tbody>
</table>

Avec cet ensemble étendu de symboles, 4 000 serait représenté comme suit :

<p><span style="text-decoration: overline;">IV</span></p>

Et voici un tableau de nombres plus grands et leurs représentations en chiffres romains pour commencer :

<table>
  <thead>
    <tr>
      <th>Nombre</th>
      <th>Chiffre romain</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>4 000</td>
      <td><span style="text-decoration: overline;">IV</span></td>
    </tr>
    <tr>
      <td>4 001</td>
      <td><span style="text-decoration: overline;">IV</span>I</td>
    </tr>
    <tr>
      <td>4 002</td>
      <td><span style="text-decoration: overline;">IV</span>II</td>
    </tr>
    <tr>
      <td>4 003</td>
      <td><span style="text-decoration: overline;">IV</span>III</td>
    </tr>
    <tr>
      <td>5 000</td>
      <td><span style="text-decoration: overline;">V</span></td>
    </tr>
    <tr>
      <td>6 000</td>
      <td><span style="text-decoration: overline;">VI</span></td>
    </tr>
    <tr>
      <td>7 000</td>
      <td><span style="text-decoration: overline;">VII</span></td>
    </tr>
    <tr>
      <td>8 000</td>
      <td><span style="text-decoration: overline;">VIII</span></td>
    </tr>
    <tr>
      <td>9 000</td>
      <td><span style="text-decoration: overline;">IX</span></td>
    </tr>
    <tr>
      <td>10 000</td>
      <td><span style="text-decoration: overline;">X</span></td>
    </tr>
    <tr>
      <td>40 000</td>
      <td><span style="text-decoration: overline;">XL</span></td>
    </tr>
    <tr>
      <td>90 000</td>
      <td><span style="text-decoration: overline;">XC</span></td>
    </tr>
    <tr>
      <td>400 000</td>
      <td><span style="text-decoration: overline;">CD</span></td>
    </tr>
    <tr>
      <td>900 000</td>
      <td><span style="text-decoration: overline;">CM</span></td>
    </tr>
    <tr>
      <td>1 000 000</td>
      <td><span style="text-decoration: overline;">M</span></td>
    </tr>
  </tbody>
</table>

## Comment ajouter un vinculum ou une ligne horizontale sur les chiffres romains avec HTML et CSS

Pour les développeurs, le moyen le plus simple d'ajouter un vinculum aux chiffres romains en ligne est d'envelopper les symboles dans un élément et d'utiliser un peu de CSS.

Par exemple, pour ajouter une ligne horizontale sur les symboles IV dans IVIII, vous pouvez les envelopper dans une balise `span` et définir sa propriété `text-decoration` sur `overline` :

```html
<p><span style="text-decoration: overline;">IV</span>III</p>
```

Ce qui donnera le résultat suivant :

<p><span style="text-decoration: overline;">IV</span>III</p>

## **Merci de votre lecture**

Si vous avez trouvé cette explication des chiffres romains utile, n'hésitez pas à la partager avec vos amis pour que d'autres puissent en profiter.

N'hésitez pas non plus à me contacter sur [Twitter](https://twitter.com/kriskoishigawa) pour me donner votre avis.