---
title: Comment créer un minuteur à bascule dans React Native
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-02T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-flip-timer-in-react-native-e208e54baf58
coverImage: https://cdn-media-1.freecodecamp.org/images/0*273pYX1ym8bIxTou
tags:
- name: Apps
  slug: apps-tag
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: Comment créer un minuteur à bascule dans React Native
seo_desc: 'By Pritish Vaidya

  Introduction

  A Flip Timer is a digital time keeping device with the time indicated by numbers
  that are sequentially revealed by a split-flap display.

  This article will demonstrate the building of a Flip Timer in React Native using
  i...'
---

Par Pritish Vaidya

### Introduction

Un _minuteur à bascule_ est un dispositif numérique de mesure du temps où le temps est indiqué par des nombres qui sont révélés séquentiellement par un affichage à volets divisés.

Cet article démontrera la création d'un _minuteur à bascule_ dans React Native en utilisant ses APIs exposées et sans dépendances supplémentaires.

### Défis à surmonter

* Implémenter la propriété `transform-origin` en utilisant vos techniques de **_matrices de votre cours de mathématiques universitaires_** puisque elle n'est pas supportée dans React Native. La rotation autour de l'origine centrée (par défaut) est facile, mais nous devons translater l'origine et faire une rotation autour des bords.
* Implémentation du composant Flip Number.
* Surmonter le problème `overflow: hidden` sur Android puisqu'il ne fonctionne pas avec les éléments positionnés en absolu.

### Contenu

1. **Implémenter le composant Flip Number**
2. **Implémenter FoldView**

* Disposition de base
* Surmonter le défi
* Ajouter les transformations
* Ajouter les animations

3. **Mettre à jour le composant Timer**

4. **Résultat final**

5. **Liens**

### Implémenter le composant Flip Number

#### Disposition de base

La disposition de base se compose de deux cartes — supérieure et inférieure — jointes ensemble de sorte que la vue ressemble à un minuteur à bascule.

**Carte de nombre**

Il s'agit d'une disposition de base composée d'un wrapper et de deux cartes — _inférieure_, _supérieure_.

**Note** : La carte inférieure a le nombre précédent ajouté. Son utilité sera révélée une fois que nous atteindrons l'implémentation de _FoldView_.

![Image](https://cdn-media-1.freecodecamp.org/images/uzy-CsNuZji7eCwWTu6LYYOhygfzB4uP7v68)
_Crédit image : [GitHub](https://github.com/dawnlabs/carbon" rel="noopener" target="_blank" title="">Carbon</a>. | Code : <a href="https://github.com/pritishvaidya/react-native-flip-timer/blob/master/src/components/flip-number/number-card.js" rel="noopener" target="_blank" title=")_

**Carte**

Le wrapper de la carte a `overflow: hidden`, et nous traduisons ses éléments (nombre) en fonction du type de la carte (supérieure ou inférieure).

![Image](https://cdn-media-1.freecodecamp.org/images/-1JOq61At7-JFxeyTRsn5vgtzCZYTL9UkZ-M)
_Crédit image : [GitHub](https://github.com/dawnlabs/carbon" rel="noopener" target="_blank" title="">Carbon</a>. | Code : <a href="https://github.com/pritishvaidya/react-native-flip-timer/blob/master/src/components/flip-number/card.js" rel="noopener" target="_blank" title=")_

### Implémenter FoldView

#### Disposition de base

Pour construire FoldView, nous avons besoin de deux _FlipCards_ similaires aux _NumberCards_ mais avec un _positionnement absolu_ afin qu'elles soient au-dessus des _NumberCards_ lorsque les animations de bascule sont appliquées.

**Carte de nombre**

Ajout du composant _FlipCard_ au composant _NumberCard_.

![Image](https://cdn-media-1.freecodecamp.org/images/YrmnGEZBPPoxwsvskGYqHaYzPJ4VkB8viPO1)
_Crédit image : [GitHub](https://github.com/dawnlabs/carbon" rel="noopener" target="_blank" title="">Carbon</a>. | Code : <a href="https://github.com/pritishvaidya/react-native-flip-timer/blob/master/src/components/flip-number/number-card.js" rel="noopener" target="_blank" title=")_

**Flip Card**

Le composant FlipCard est un wrapper animé avec un positionnement absolu utilisé lors de l'application de l'animation de bascule.

**Défi (Partie 2 et Partie 3)** : `overflow: hidden` avec un positionnement absolu pose des problèmes majeurs sur _Android_. En utilisant ce [post StackOverflow](https://stackoverflow.com/a/21684490/6606831), il peut être résolu en utilisant un _conteneur de débordement_ à l'intérieur de l'élément positionné en absolu.

![Image](https://cdn-media-1.freecodecamp.org/images/KG-NyI8-vafcBiZGWoZaD1hpCpwW0V-3ff3a)
_Crédit image : [GitHub](https://github.com/dawnlabs/carbon" rel="noopener" target="_blank" title="">Carbon</a>. | Code : <a href="https://github.com/pritishvaidya/react-native-flip-timer/blob/master/src/components/flip-number/flip-card.js" rel="noopener" target="_blank" title=")_

#### Résultat final

![Image](https://cdn-media-1.freecodecamp.org/images/qCA0sQ1vuVxxPDWMqOirMoOXtPhRh2-Rwyrl)

#### Surmonter le défi

Maintenant vient la partie difficile. Nous devons plier le composant FlipCard le long des bords.

Puisque React Native ne supporte pas la propriété `transform-origin`, nous devons trouver un autre moyen de déplacer l'origine de la rotation sur le bord inférieur.

Heureusement, il existe un moyen de surmonter ce problème. Selon cet article génial [article](https://commitocracy.com/implementing-foldview-in-react-native-e970011f98b8) et en lisant la documentation [MDN](https://developer.mozilla.org/en-US/) pour la propriété [transform-origin](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin), elle peut être implémentée en utilisant des **matrices**.

**Utils**

React Native expose plusieurs opérations de matrice dans [MatrixMath.js](https://github.com/facebook/react-native/blob/master/Libraries/Utilities/MatrixMath.js). Les plus importantes dont nous avons besoin sont

* **Matrice identité** : Elle retourne une matrice identité 4 * 4 `[1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]`

![Image](https://cdn-media-1.freecodecamp.org/images/J7CO8Ge-QqrmmFwuphxEwbypurpEPgQFUqeQ)
_Crédit image : [GitHub](https://github.com/dawnlabs/carbon" rel="noopener" target="_blank" title="">Carbon</a>. | Code : <a href="https://github.com/pritishvaidya/react-native-flip-timer/blob/master/src/utils/index.js" rel="noopener" target="_blank" title=")_

* **Multiplier les matrices** : Cette méthode utilitaire génère une sortie basée sur la multiplication des matrices 4*4 `a` et `b` fournies en entrée.

![Image](https://cdn-media-1.freecodecamp.org/images/1xbhTbClhu47mEsGPa7p4T7wHsajXl3PAy0J)
_Crédit image : [GitHub](https://github.com/dawnlabs/carbon" rel="noopener" target="_blank" title="">Carbon</a>. | Code : <a href="https://github.com/pritishvaidya/react-native-flip-timer/blob/master/src/utils/index.js" rel="noopener" target="_blank" title=")_

* **Matrice de rotation** : Il s'agit d'une méthode utilitaire personnalisée qui prendra une matrice 4*4 et le degré auquel elle sera tournée, puis la multipliera à la matrice originale pour retourner le résultat généré.

![Image](https://cdn-media-1.freecodecamp.org/images/qa2oiTgiOehlLCu4Qqfcj6zhNofoKpfA-1XL)

![Image](https://cdn-media-1.freecodecamp.org/images/q2MBhiltQRvtPmHC8r28UGvBDGPYOSTyEriN)
_Crédit image : [GitHub](https://github.com/dawnlabs/carbon" rel="noopener" target="_blank" title="">Carbon</a>. | Code : <a href="https://github.com/pritishvaidya/react-native-flip-timer/blob/master/src/utils/index.js" rel="noopener" target="_blank" title=")_

* **Matrice de perspective** : Cette méthode utilitaire nous permettra d'utiliser le style de perspective dans React Native et de le multiplier à la matrice originale 4*4.

![Image](https://cdn-media-1.freecodecamp.org/images/0HmvXN1gu3-hGoK1ydxmf-8rBmxtIJEe3PNi)

![Image](https://cdn-media-1.freecodecamp.org/images/RjIzOwoDY1-1vvH1Y9lu7RC-opK8hpS1vSoL)
_Crédit image : [GitHub](https://github.com/dawnlabs/carbon" rel="noopener" target="_blank" title="">Carbon</a>. | Code : <a href="https://github.com/pritishvaidya/react-native-flip-timer/blob/master/src/utils/index.js" rel="noopener" target="_blank" title=")_

* **Matrice de translation** : Cette méthode utilitaire traduira l'origine et modifiera la matrice originale 4*4

![Image](https://cdn-media-1.freecodecamp.org/images/OwRIvTNQ6f4YHisOmGSU362njvxovBFJ8JVy)

![Image](https://cdn-media-1.freecodecamp.org/images/ThtIdQR5osqzP5GMmxFGvQB5oUbuUUHMMwRv)
_Crédit image : [GitHub](https://github.com/dawnlabs/carbon" rel="noopener" target="_blank" title="">Carbon</a>. | Code : <a href="https://github.com/pritishvaidya/react-native-flip-timer/blob/master/src/utils/index.js" rel="noopener" target="_blank" title=")_

* **Matrice de non-translation** : Cette méthode utilitaire annulera la translation de l'origine et modifiera la matrice originale 4*4

![Image](https://cdn-media-1.freecodecamp.org/images/P0Ct10em0E2zebJeY2UTdZKMW2JmWyM62xMJ)
_Crédit image : [GitHub](https://github.com/dawnlabs/carbon" rel="noopener" target="_blank" title="">Carbon</a>. | Code : <a href="https://github.com/pritishvaidya/react-native-flip-timer/blob/master/src/utils/index.js" rel="noopener" target="_blank" title=")_

#### Ajouter les transformations

`deg` est le degré à tourner et `y` est la hauteur du composant auquel il sera traduit.

**Défi (Partie 1)** : En combinant les utils ci-dessus, `transform-origin` est implémenté avec succès.

![Image](https://cdn-media-1.freecodecamp.org/images/e9M2yLlahuXIQJ03D3UdvbQSNxSLlY-Lppdk)

![Image](https://cdn-media-1.freecodecamp.org/images/2qvRlyie7oBWQUwfyOn1t7RAvnZQ-rALAyj9)
_Crédit image : [GitHub](https://github.com/dawnlabs/carbon" rel="noopener" target="_blank" title="">Carbon</a>. | Code : <a href="https://github.com/pritishvaidya/react-native-flip-timer/blob/master/src/components/timer.js" rel="noopener" target="_blank" title=")_

#### Ajouter les animations

![Image](https://cdn-media-1.freecodecamp.org/images/GBeUP2fLLmHCcbS6gpVdXBR1DwRMuULV2t2t)
_Crédit image : [GitHub](https://github.com/dawnlabs/carbon" rel="noopener" target="_blank" title="">Carbon</a>. | Code : <a href="https://github.com/pritishvaidya/react-native-flip-timer/blob/master/src/components/timer.js" rel="noopener" target="_blank" title=")_

### Mettre à jour le composant Timer

#### Ajouter Time Util

Cet utilitaire incrémentera le minuteur d'une seconde et ajustera les heures, les minutes et les secondes.

![Image](https://cdn-media-1.freecodecamp.org/images/3r0RZrCsJG4d0J3VNbjKaO4lPlySXO1Cxl0S)
_Crédit image : [GitHub](https://github.com/dawnlabs/carbon" rel="noopener" target="_blank" title="">Carbon</a>. | Code : <a href="https://github.com/pritishvaidya/react-native-flip-timer/blob/master/src/utils/index.js" rel="noopener" target="_blank" title=")_

#### Composant Timer

Le composant timer appellera **Time Util** et mettra à jour le composant en fonction des heures, des minutes et des secondes.

![Image](https://cdn-media-1.freecodecamp.org/images/ZcNz-7U5YSbU8UYyQwKijO8cfpEE2-CL1pN4)
_Crédit image : [GitHub](https://github.com/dawnlabs/carbon" rel="noopener" target="_blank" title="">Carbon</a>. | Code : <a href="https://github.com/pritishvaidya/react-native-flip-timer/blob/master/src/components/timer.js" rel="noopener" target="_blank" title=")_

#### Composant Flip Number

Ce composant divise simplement le nombre en deux parties en fonction de leur placement de chiffre et appelle le composant **NumberCard**.

![Image](https://cdn-media-1.freecodecamp.org/images/MPgjFf9b9pYxOTVO461fBB-Dqh-8O25D3z5b)
_Crédit image : [GitHub](https://github.com/dawnlabs/carbon" rel="noopener" target="_blank" title="">Carbon</a>. | Code : <a href="https://github.com/pritishvaidya/react-native-flip-timer/blob/master/src/components/flip-number/index.js" rel="noopener" target="_blank" title=")_

### Résultat final

![Image](https://cdn-media-1.freecodecamp.org/images/c93caflCfnyqBNcQed-BOGQITYP-QFngekZ8)

### Liens

J'ai publié un package pour cela qui contient plus de propriétés personnalisables.

* npm : [react-native-flip-timer](https://www.npmjs.com/package/react-native-flip-timer)
* GitHub : [react-native-flip-timer](https://github.com/pritishvaidya/react-native-flip-timer)

D'autres choses intéressantes peuvent être trouvées sur mes profils [**_StackOverflow_**](https://stackoverflow.com/users/6606831/pritish-vaidya) et [**_GitHub_**](https://github.com/pritishvaidya).

Suivez-moi sur [**_LinkedIn_**](https://www.linkedin.com/in/pritish-vaidya-506686128/), [**_Medium_**](https://medium.com/@pritishvaidya94), [**_Twitter_**](https://twitter.com/PritishVaidya) pour des mises à jour et de nouveaux articles.

**Un applaudissement, deux applaudissements, trois applaudissements, quarante ?**

![Image](https://cdn-media-1.freecodecamp.org/images/6nEX6G3ucbC8JOm8KkdqSWhrwBusRHDmmQkH)

_Publié à l'origine sur [blog.pritishvaidya.com](https://blog.pritishvaidya.com/posts/2019-03-02-building-a-flip-timer-in-react-native/) le 2 mars 2019._