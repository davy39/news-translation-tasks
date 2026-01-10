---
title: Comment les valeurs non entières sont stockées dans un float (et pourquoi il
  flotte)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-28T15:53:47.000Z'
originalURL: https://freecodecamp.org/news/how-non-integer-values-are-stored-in-a-float-and-why-it-floats-902effacbfb9
coverImage: https://cdn-media-1.freecodecamp.org/images/0*sgfbQZhatWzdqD46
tags:
- name: coding
  slug: coding
- name: Computer Science
  slug: computer-science
- name: interview
  slug: interview
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
seo_title: Comment les valeurs non entières sont stockées dans un float (et pourquoi
  il flotte)
seo_desc: 'By Shukant Pal

  Did you ever think how computers work on floating-point numbers? I mean — where
  does the decimal point go? What if you’re asked in an interview?


  _Photo by [Unsplash](https://unsplash.com/@jplenio?utm_source=medium&utm_medium=referral"...'
---

Par Shukant Pal

Avez-vous déjà pensé à la manière dont les ordinateurs traitent les nombres à virgule flottante ? Je veux dire — où va la virgule décimale ? Et si on vous posait la question lors d'un entretien ?

![Image](https://cdn-media-1.freecodecamp.org/images/wO60yF7x15-i5BWPFtfyz-MkgKtoqrIVY5yf)
_Photo par [Unsplash](https://unsplash.com/@jplenio?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Johannes Plenio</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

La norme IEEE 754 à virgule flottante définit comment les valeurs non entières sont encodées dans des types de taille fixe, comme le float en C++ et le Number en JavaScript. Elle nous donne cinq formats différents — mais ne vous inquiétez pas, ils sont tous basés sur le même concept. Dans le reste de cet article, je l'appellerai l'IEEE 754.

Si vous êtes submergé en lisant tous les différents trucs utilisés dans l'IEEE 754 — ne vous inquiétez pas, j'ai donné suffisamment d'exemples à la fin pour que tout soit clair dans votre tête.

## Concept

Tout comme les entiers peuvent être écrits dans n'importe quelle "base", les valeurs non entières peuvent également être écrites dans n'importe quelle base.

5.1 = 1(2²) + 0(2¹) + 1(2⁰) + 1/2¹ = 1011.1

De même, nous pouvons écrire 3.25 = 11.01, 8.75 = 1000.11. Les valeurs après le point "radix" (ce n'est plus un point décimal) sont multipliées par des puissances négatives de 2.

L'IEEE 754 est basé sur cette technique. Pour convertir une valeur au format IEEE 754, nous devons suivre ces étapes :

1. Écrire le nombre sous forme binaire, avec le point radix.
2. Le formater en notation scientifique de sorte qu'un seul chiffre soit placé avant le point radix.
3. Encoder les différents composants comme dirigé par le format IEEE choisi.

Par exemple, prenons la valeur 934893.109375 :

1. 934893.109375 peut être représenté exactement (plus à ce sujet plus tard) en forme binaire comme 11100100001111101101.000111.
2. Forme scientifique : 1.1100100001111101101000111 x 2^-19

NOTE : Certaines valeurs décimales ne peuvent pas être représentées exactement en base 2, tout comme un tiers ne peut pas être écrit exactement en base 10. Cependant, vous pourriez approximer 1/3 à .3333333333. De même, la valeur peut être approximée en base 2 (plutôt que d'être exacte). Par exemple, 1.9 est approximé à 1.11100110011001100110011 en binaire (remarquez le 0011 répétitif, c'est parce que 1.9 est rationnel et la valeur exacte serait représentée en le répétant à l'infini).

## Le Format

L'IEEE 754 définit trois composants qui sont écrits dans une valeur de 16/32/64 bits ou plus : un bit de signe, l'exposant et la mantisse.

Ces composants sont écrits dans l'ordre suivant :

* **Bit de signe**(s) : Le bit de signe a une valeur de 0 pour les valeurs positives et 1 pour les valeurs négatives.
* **Exposant**(e) : Cela est égal à l'exposant que nous obtenons en forme scientifique.
* **Mantisse**(m) : La mantisse, ou le _significande_, est le coefficient écrit en forme scientifique, simplement sans le point radix. Donc la mantisse de 3.25=11.01 serait 1101 ou 13.

Pour obtenir notre valeur à partir de l'IEEE 754 : _V = s_ x _(m^e)_

Les largeurs de chaque format sont fixes, et il en va de même pour les largeurs de la mantisse et des exposants. _La largeur de la mantisse définit la précision, tandis que la largeur de l'exposant définit la plage de la valeur._

Maintenant, l'IEEE 754 utilise également quelques astuces pour encoder les nombres réels, que j'ai listées ci-dessous dans différents titres :

* Biais de l'exposant
* Convention du bit de tête
* Nombres subnormaux
* ±Infinité et NaN
* ±Zéro (et exemples en ECMAScript)

## Biais de l'exposant

L'exposant _e_ peut être négatif et pour supporter les nombres négatifs, l'IEEE 754 définit le _biais_. Le biais est ajouté à l'exposant pour obtenir l'exposant encodé réel. Par exemple, le format binaire32 fournit 8 bits aux exposants, où le biais est 2⁷-1=127 dans le champ de l'exposant. Donc -1 serait encodé comme -1+127=128 et un exposant +5 serait encodé comme 5+127=132.

Le biais est choisi de telle sorte que le plus petit exposant serait encodé comme 1 et le plus grand exposant serait encodé comme 2⁸ - 2 = 254 (en binaire32). Cela explique pourquoi _emin_ est -126 et _emax_ est +127.

NOTE : Vous avez peut-être remarqué que les valeurs 0 et 2⁸ - 1 sont laissées de côté. Si l'exposant est encodé comme zéro, alors le nombre représenté est soit ±∞ soit NaN. Si les bits de l'exposant sont tous à un (c'est-à-dire, 2⁸ - 1 = 255), alors le nombre représenté est un subnormal spécial (plus à ce sujet plus tard).

## Convention du bit de tête

Le chiffre le plus à gauche de tout nombre écrit en notation scientifique n'est jamais zéro (sauf si le nombre lui-même est exactement 0). Si vous vous retrouvez avec un 0 à gauche, vous devez diminuer votre exposant. Par exemple,

0.12 x 10² = 1.2 x 10¹

Puisque nous travaillons en base deux et que le chiffre de tête ne peut pas être zéro : cela signifie que le chiffre de tête doit être — 1 et seulement 1. Ce fait est exploité par l'IEEE 754 et le bit de tête est exclu de la mantisse encodée.

## Nombres subnormaux

L'IEEE 754 définit deux types de nombres : normaux et subnormaux. Les nombres normaux sont, en fait, normaux — ils peuvent être représentés dans le format _m_ x 2^e, où e est _emin_ ≤ _e_ ≤ _emax_. Cependant, si _e_ descend en dessous de _emin_, alors l'IEEE 754 les appelle subnormaux.

Puisque l'_e_ encodé ne peut pas descendre en dessous de 0, l'exposant réel pour les nombres subnormaux est toujours -127. Les exposants inférieurs peuvent être représentés en rompant la convention du bit de tête et en ajoutant des 0s à gauche de la mantisse. Cela provoque une perte de précision pour la mantisse (car les zéros de tête font tomber les bits les plus à droite).

```
undefined
```

// emin = -126, largeur de la mantisse = 24 bits
// 1. NOMBRE NORMAL, V = 2^-126
Encodé :  m = 00000000000000000000000, e = 1
Réel :  m = 100000000000000000000000, e = -126
V = 2^-126

// 2. NOMBRE SUBNORMAL, V = 2^-127
Encodé :  m = 10000000000000000000000, e = 0 (e doit être 0)
Réel :   m = 10000000000000000000000, e = -127
La convention du bit de tête ne fonctionne pas dans les nombres subnormaux, où e = 0. Cela signifie que la mantisse encodée est la mantisse réelle. La puissance e (réelle) est toujours -127.
Le bit de tête de la mantisse pourrait être 0. Voir l'exemple ci-dessous.

// 3. NOMBRE SUBNORMAL, V = 2^-129
Encodé :  m = 00100000000000000000000, e = 0 (subnormal)
Réel :  m =  00100000000000000000000, e = -127
V = 0.0100000000000000000000 x 2^-127 = 0.25 * 2^-127 = 2^-129

```
// emin = -126, largeur de la mantisse = 24 bits

// 1. NOMBRE NORMAL, V = 2^-126

Encodé :  m = 00000000000000000000000, e = 1
Réel :  m = 100000000000000000000000, e = -126

V = 2^-126

// 2. NOMBRE SUBNORMAL, V = 2^-127

Encodé :  m = 10000000000000000000000, e = 0 (e doit être 0)
Réel :   m = 10000000000000000000000, e = -127

La convention du bit de tête ne fonctionne pas dans les nombres subnormaux, où e = 0. Cela signifie que la mantisse encodée est la mantisse réelle. La puissance e (réelle) est toujours -127.

Le bit de tête de la mantisse pourrait être 0. Voir l'exemple ci-dessous.

// 3. NOMBRE SUBNORMAL, V = 2^-129

Encodé :  m = 00100000000000000000000, e = 0 (subnormal)
Réel :  m =  00100000000000000000000, e = -127

V = 0.0100000000000000000000 x 2^-127 = 0.25 * 2^-127 = 2^-129
```

## ±Infinité et NaN

L'exposant avait deux valeurs spéciales : 0 et 2⁸-1 (où ce 8 est en fait la largeur de l'exposant en binaire32). La première était pour les nombres subnormaux, tandis que la seconde est pour les valeurs "spéciales". 2⁸-1 est également la valeur lorsque tous les bits de l'exposant sont à un.

* Si la valeur de la mantisse est 0, alors le nombre représenté est l'infini positif ou négatif. Le signe est déterminé par le bit de signe.
* Si la valeur de la mantisse est non nulle, alors le nombre représenté est, en fait, "not a number" ou NaN. Il existe deux types de NaN — signalant et silencieux. Le type est déterminé par la valeur de la mantisse, et cet article ne couvre pas cela. Un NaN signalant est utilisé pour terminer toute opération numérique tandis qu'un NaN silencieux permet à l'opération de continuer. Selon mon expérience, vous n'aurez jamais besoin de distinguer ces NaN. Ils sont probablement inutiles pour vous.

## Le cas ±Zéro

Il est surprenant qu'il y ait deux zéros dans l'IEEE 754 — positif et négatif. Pour vous et moi, ils sont identiques. Toute opération avec +0 donnera le même résultat si -0 est utilisé à la place, ou est-ce vrai ? Non, ce n'est pas le cas.

1/∞ = 0, et aussi 1/-∞ = 0, alors 1/(1/∞) = 1/0 = ∞ et 1/(1/-∞) = ∞. Le signe n'est pas préservé si nous utilisons seulement un zéro positif dans les équations ci-dessus. Cela est résolu en utilisant ±0. 1/-∞ = -0, alors 1/(1/-∞)=-∞.

Encore une fois, si seulement 0 est utilisé : alors 4/∞=0 et -4/∞=0. Cependant, en utilisant ±0, cela donne : 4/∞=+0 et -4/∞=-0.

L'IEEE 754 exige, cependant, que toute comparaison entre +0 et -0 retourne un résultat positif. En d'autres termes, +0 == -0 est vrai.

La plupart des langages cacheraient +0 et -0, et vous ne pourriez pas les distinguer directement (vous pourriez si vous divisez par zéro et testez le résultat pour ±∞). Cependant, JavaScript est spécial et fournit la méthode `Object.is(arg1, arg2)` qui distinguerait +0 et -0.

```
Object.is(+0, -0);// false
```

## Exemples

J'ai promis que je clarifierais votre esprit de toute confusion avec mes exemples.

```
// Tous les exemples utilisent binary32 ici
// 1. Encoder 127872.12781278 en IEEE 754

Étape 1 : Écrire en notation binaire

127872.12781278 = 11111001110000000.0010000 (24 bits)

Étape 2 : Écrire en notation scientifique

1.11110011100000000010000 x 2^16

Étape 3 : Encoder

m(encodé) = 11110011100000000010000 (23 bits seulement)
e(encodé) = 16+127 = 143 = 10001111

(signe)(e)(m) = 0 10001111 11110011100000000010000 (32 bits)

// 2. Encoder (-1.25 x 2^-130) en IEEE 754

Étape 1 : Écrire en notation binaire (en excluant le signe ici)

1.25x2^-130 = 1.01 x 2^-130 (déplacer de 130 vers la droite pour supprimer l'échelle)

Étape 2 : Déjà fait !!!
Étape 3 : Encoder

Comme e < emin, ceci est un nombre subnormal
e = -127
V = 1.01 x 2^-130 = 0.00101 x 2^-127
m = 0.0010100000000000000000 (23 bits seulement, pas de convention de bit de tête)
signe = 1

(signe)(e)(m) = 1 00000000 00010100000000000000000 (32 bits)
```

## Enfin, est-ce qu'il flotte ?

Le titre promettait de répondre à cette question. Il le devait.

Le nom "virgule flottante" vient du fait que le point radix peut être placé n'importe où dans un nombre. Les types à virgule flottante peuvent encoder n'importe quel nombre avec au plus un nombre donné de chiffres (la mantisse limite la précision), où que soit placé le point radix (à part le fait qu'il peut y avoir une petite perte de précision).

Cela s'oppose aux types à virgule fixe où la représentation fixe les chiffres représentables à gauche et à droite du point radix.

Le type float en C++ vient également du système à virgule flottante.

## Informations supplémentaires : Types à virgule flottante décimale

(NOTE : Les types à virgule flottante décimale ne sont pas largement utilisés. Ils sont plus importants dans le commerce, en raison de l'importance de la précision dans les valeurs monétaires.)

En 2008, l'IEEE 754 a ajouté deux autres formats : decimal32 et decimal64. Dans les formats décimaux, la mantisse est mise à l'échelle par des puissances de 10 au lieu de 2. Cela préserve les chiffres significatifs décimaux de notre entrée et, surtout, ne perd pas de précision pour les nombres qui peuvent être représentés exactement en base 10.

Cependant, la mantisse est encodée en base 2 (l'exposant est également encodé en base 2, simplement la valeur réelle est calculée par _V_ = _m_ x _10^e_). Puisque la mantisse est en base 2, vous ne pouvez pas l'écrire en notation scientifique :

```
102 = 1.02 x 10^2 = 1.000001010001111010111000 x 10^2
202 = 2.02 x 10^2 = 10.00000101000111101011100 x 10^2
```

Par exemple, 202 a deux chiffres ('10') avant le point radix tandis que 101 n'a qu'un seul chiffre ('1') avant le point radix. Il n'y a pas de puissance intégrale de 10 qui puisse être utilisée pour représenter 202 en forme scientifique binaire (avec seulement un chiffre avant le point radix).

NOTE : Cet effet secondaire est dû au fait que la mantisse et le facteur d'échelle (10) ne sont pas dans la même base.

Pour surmonter cette limitation, l'IEEE 754 encode les nombres où la mantisse est un entier.

```
1234.31212 = 123431212 x 10^-5 = 111010110110110100100101100 x 10^-5

// La mantisse sera 111010110110110100100101100
// L'exposant sera -5.
```

Les formats décimaux définissent deux façons d'encoder la mantisse entière : entier binaire (comme montré dans l'exemple ci-dessus) et décimal densément compacté (DPD). Les formats décimaux ont également des astuces spéciales, qui sont hors du cadre de cet article. J'écrirai à leur sujet dans une autre histoire.

Pour aller plus loin avec Shukant Pal :

* [Aperçu complet du HTML Canvas](https://medium.com/@sukantk3.4/full-overview-of-the-html-canvas-6354216fba8d)
* [Supprimer les dépendances circulaires en JavaScript](https://medium.com/@sukantk3.4/circular-dependencies-in-javascript-34183fc2720) (ma proposition)
* [Comment synchroniser votre application de jeu sur plusieurs appareils](https://medium.freecodecamp.org/how-to-synchronize-your-game-app-across-multiple-devices-88794d4c95a9) (Android)
* [Comment utiliser Firebase pour créer des jeux Android](https://medium.freecodecamp.org/match-making-with-firebase-hashnode-de9161e2b6a7)

Je suis Shukant Pal — le créateur du noyau Silcos. Je connais beaucoup de choses sur le code C++ de bas niveau et un peu sur la structure interne du code du noyau Linux. J'aime les détails au niveau matériel ici et là. Suivez-moi sur mes profils de réseaux sociaux.