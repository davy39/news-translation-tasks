---
title: 'Formule de complétion du carré : Comment compléter le carré avec une équation
  quadratique'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-17T22:51:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-complete-the-square-a-method-for-completing-the-square
coverImage: https://www.freecodecamp.org/news/content/images/2020/02/header-2.png
tags:
- name: Math
  slug: math
seo_title: 'Formule de complétion du carré : Comment compléter le carré avec une équation
  quadratique'
seo_desc: 'By Alexander Arobelidze

  Consider the following quadratic equation: x2 = 9. If asked to solve it, we would
  naturally take the square root of 9 and end up with 3 and -3. But what if simple
  square root methods won''t do? What if the equation includes x r...'
---

Par Alexander Arobelidze

<p>Considérons l'équation quadratique suivante : <b><em>x<sup>2</sup> = 9</em></b>. Si on nous demande de la résoudre, nous prendrions naturellement la racine carrée de <b><em>9</em></b> et obtiendrions <b><em>3</em></b> et <b><em>-3</em></b>. Mais que faire si les méthodes simples de racine carrée ne suffisent pas ? Que faire si l'équation inclut <b><em>x</em></b> élevé à la première puissance et ne peut pas être facilement factorisé ?

Heureusement, il existe une méthode pour **compléter le carré**. Ainsi, une équation quadratique peut être résolue en prenant la racine carrée. Explorons cela étape par étape ensemble.

Disons que nous avons l'équation suivante :

![Image](https://www.freecodecamp.org/news/content/images/2020/02/intro1.png)
_Équation donnée : 4x<sup>2</sup> + 13x + 7 = x + 6_

## EXEMPLE 1 : Compléter le carré

### ÉTAPE 1 : Séparer les termes variables des termes constants

![Image](https://www.freecodecamp.org/news/content/images/2020/02/step1.png)
_Séparer les termes pour simplifier : 4x<sup>2</sup> + 13x **- x** = 6 **- 7**_

Simplifions notre équation. D'abord, séparons les termes qui incluent des variables des termes constants. Ensuite, soustrayons **x** de **13x** (résultat est **12x**) et soustrayons **7** de **6** (résultat est **-1**).

### ÉTAPE 2 : Assurer que le coefficient de x au carré est égal à 1

![Image](https://www.freecodecamp.org/news/content/images/2020/02/step2.png)
_Diviser par le terme de x<sup>2</sup> : x<sup>2</sup> + 3x = -1/4_

La méthode de complétion du carré fonctionne beaucoup plus facilement lorsque le coefficient de **x<sup>2</sup>** est égal à 1. Le coefficient dans notre cas est égal à **4**. Diviser 4 dans chaque membre donne **x<sup>2</sup> + 3x = - 1/4**. 

### ÉTAPE 3 : Compléter le carré

![Image](https://www.freecodecamp.org/news/content/images/2020/02/step3a.png)
_Le coefficient de x est divisé par 2 et mis au carré : (3 / 2)<sup>2</sup> = 9/4_

D'abord, nous devons trouver le terme constant de notre carré complet. Le coefficient de **x**, qui est égal à 3, est divisé par **2** et mis au carré, ce qui nous donne **9/4**.

![Image](https://www.freecodecamp.org/news/content/images/2020/02/step3b.png)
_Le 9/4 résultant est ajouté et soustrait : x<sup>2</sup> + 3x + 9/4 - 9/4 = -1/4_

Ensuite, nous ajoutons et soustrayons **9/4** comme indiqué ci-dessus. Cela n'affecte pas notre équation (**9/4 - 9/4 = 0**), mais nous donne une expression pour le carré complet **x<sup>2</sup> + 3x + 9/4**.

### ÉTAPE 4 : Factoriser l'expression x au carré + 3x + 9/4

![Image](https://www.freecodecamp.org/news/content/images/2020/02/step4.png)
_La factorisation de x<sup>2</sup> + 3x + 9/4 nous donne (x + 3/2)<sup>2</sup>_

Rappelons maintenant une forme plus générale **(x + a)<sup>2</sup> = x<sup>2</sup> + 2ax + a<sup>2</sup>** et utilisons-la dans l'exemple actuel. En substituant nos nombres, nous obtenons : **x<sup>2</sup> + 3x + 9/4 = x<sup>2</sup> + 2*(3/2)*x + (3/2)<sup>2</sup> =** **(x + 3/2)<sup>2</sup>**.

### ÉTAPE 5 : Prendre la racine carrée

![Image](https://www.freecodecamp.org/news/content/images/2020/02/step5.png)
_Prenant la racine carrée : ((x + 3/2)<sup>2</sup>)<sup>1/2</sup> = (2)<sup>1/2</sup>. x = 2<sup>1/2</sup> - 3/2 & x = -2<sup>1/2</sup> - 3/2_

Enfin, en prenant la racine carrée des deux côtés, nous obtenons **√(x + 3/2)<sup>2</sup> = ±√2**. Ou simplement x + 3/2 = ±√2. Nous concluons cela en résolvant pour **x** : **X<sub>1</sub>= √2 - 3/2** et **X<sub>2</sub> = - √2 - 3/2**._** 

## EXEMPLE 2 : Résolvons-en une autre

![Image](https://www.freecodecamp.org/news/content/images/2020/02/EX2header.png)
_Équation donnée : 2x<sup>2</sup> + x - 7 = x<sup>2</sup> + 9x - 12_

### ÉTAPE 1 : Séparer les termes variables des termes constants

![Image](https://www.freecodecamp.org/news/content/images/2020/02/EX2step1.png)
_Séparer les termes pour simplifier : 2x<sup>2</sup> **- x<sup>2</sup>** + x **- 9x** = -12 **+ 7**_

Simplifiez en séparant les termes avec variables des termes constants. Ensuite, effectuez la soustraction et l'addition des deux côtés de l'équation.

### ÉTAPE 2 : Assurer que le coefficient de x au carré est égal à 1

![Image](https://www.freecodecamp.org/news/content/images/2020/02/EX2step2.png)
_Le coefficient de x<sup>2</sup> est égal à 1_

Ici, le coefficient de **X<sup>2</sup>** est déjà égal à **1**, donc aucune action supplémentaire n'est nécessaire.

### ÉTAPE 3 : Compléter le carré

![Image](https://www.freecodecamp.org/news/content/images/2020/02/EX2step3.png)
_Le coefficient de x est divisé par 2 et mis au carré : (-8 / 2)<sup>2</sup> = 16_

Comme dans l'exemple précédent, nous trouvons le terme constant de notre carré complet. Le coefficient de **x**, qui est égal à -8, est divisé par **2** et mis au carré, ce qui nous donne **16**.

![Image](https://www.freecodecamp.org/news/content/images/2020/02/EX2step3b.png)
_Le 16 résultant est ajouté et soustrait : x<sup>2</sup> - 8x + 16 - 16 = -5_

Nous ajoutons et soustrayons **16** et pouvons voir que **x<sup>2</sup> - 8x + 16** nous donne un carré complet.

### ÉTAPE 4 : Factoriser l'expression x au carré - 8x + 16

![Image](https://www.freecodecamp.org/news/content/images/2020/02/EX2step4.png)
_La factorisation de x<sup>2</sup> - 8x + 16 nous donne (x - 4)<sup>2</sup>_

Puisque le terme constant **-8** est avec le signe moins, nous utilisons cette forme générale : **(x - a)<sup>2</sup> = x<sup>2</sup> - 2ax + a<sup>2</sup>**. En utilisant nos nombres, nous obtenons : **x<sup>2</sup> - 8x + 16 = x<sup>2</sup> - 2*(4)*x + (4)<sup>2</sup> = (x - 4)<sup>2</sup>**.                               

### ÉTAPE 5 : Prendre la racine carrée

![Image](https://www.freecodecamp.org/news/content/images/2020/02/EX2step5.png)
_Prenant la racine carrée : ((x - 4)<sup>2</sup>)<sup>1/2</sup> = (11)<sup>1/2</sup>. x = 4 + 11<sup>1/2</sup> & x = 4 - 11<sup>1/2</sup>_

Enfin, en prenant la racine carrée des deux côtés, nous obtenons **√(x - 4)<sup>2</sup> = ±√11**. Ou simplement x - 4 = ±√11. Nous concluons cela en résolvant pour **_x_** : **X<sub>1</sub> = 4 + √11** et **X<sub>2</sub> = 4 - √11** 

Et voilà !