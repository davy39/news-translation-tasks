---
title: Jeu de Mémoire en Vanilla JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-28T14:31:49.000Z'
originalURL: https://freecodecamp.org/news/vanilla-javascript-tutorial-build-a-memory-game-in-30-minutes-e542c4447eae
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ikkvZ9ToN2kCtpUSP6702w.gif
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: Web Development
  slug: web-development
seo_title: Jeu de Mémoire en Vanilla JavaScript
seo_desc: 'By Marina Ferreira

  Learn JS, CSS and HTML by building a memory game in 30 minutes!

  This tutorial explains some basic HTML5, CSS3 and JavaScript concepts. We will discuss
  data attribute, positioning, perspective, transitions, flexbox, event handling,
  ...'
---

Par Marina Ferreira

#### Apprenez JS, CSS et HTML en créant un jeu de mémoire en 30 minutes !

Ce tutoriel explique quelques concepts de base de HTML5, CSS3 et JavaScript. Nous aborderons les attributs de données, le positionnement, la perspective, les transitions, flexbox, la gestion des événements, les timeouts et les opérateurs ternaires. Vous n'êtes pas censé avoir beaucoup de connaissances préalables en programmation. Si vous savez à quoi servent HTML, CSS et JS, c'est plus que suffisant !

* ?Demo: [Projet de Jeu de Mémoire](https://marina-ferreira.github.io/memory-game/)

### Structure des Fichiers

Commençons par créer les fichiers dans le terminal :

```
? mkdir memory-game ? cd memory-game ? touch index.html styles.css scripts.js ? mkdir img  
```

### `HTML`

`Le modèle initial reliant les fichiers `css` et `js`.`

`Le jeu comporte 12 cartes. Chaque carte se compose d'un conteneur `div` nommé `.memory-card`, qui contient deux éléments `img`. Le premier représente la face avant de la carte et le second sa face arrière.`

![Image](https://cdn-media-1.freecodecamp.org/images/0*LXwjdEFd1dhLuME-.jpg)

`Vous pouvez télécharger les ressources pour ce projet à l'adresse suivante : [Dépôt du Jeu de Mémoire](https://github.com/code-sketch/memory-game).`

`L'ensemble des cartes sera enveloppé dans un élément conteneur `section`. Le résultat final :`

### `CSS`

`Nous utiliserons une réinitialisation simple mais très utile, appliquée à tous les éléments :`

`La propriété `box-sizing: border-box` inclut les valeurs de padding et de bordure dans la largeur et la hauteur totales de l'élément, ce qui nous permet de sauter les calculs.`

`En définissant [display: flex](https://marina-ferreira.github.io/tutorials/css/flexbox/#introduction) pour le `body` et `margin: auto` pour le conteneur `.memory-game`, il sera centré à la fois verticalement et horizontalement.`

`.memory-game` sera également un `flex-container`. Par défaut, les éléments sont définis pour réduire leur largeur afin de s'adapter au conteneur. En définissant [flex-wrap](https://marina-ferreira.github.io/tutorials/css/flexbox/#flex-wrap) sur `wrap`, les `flex-items` s'enroulent sur plusieurs lignes, en fonction de leur taille.

`La `width` et la `height` de chaque carte sont calculées avec la fonction CSS [calc()](https://developer.mozilla.org/en-US/docs/Web/CSS/calc). Faisons trois rangées, quatre cartes chacune en définissant `width` à `25%` et `height` à `33.333%` moins `10px` de `margin`.`

`Pour positionner les enfants de `.memory-card`, ajoutons `position: relative` afin de pouvoir positionner les enfants de manière absolue, par rapport à celui-ci.`

`La propriété `position: absolute` définie à la fois pour `front-face` et `back-face` supprimera les éléments de leur position d'origine et les empilera les uns sur les autres.`

`Le modèle devrait ressembler à ceci :`

![Image](https://cdn-media-1.freecodecamp.org/images/0*XCqaVtrSiWnr7Ucp.jpg)

`Ajoutons également un effet de clic. La pseudo-classe `:active` sera déclenchée chaque fois que l'élément est cliqué. Elle appliquera une transition de .2s à sa taille :`

![Image](https://cdn-media-1.freecodecamp.org/images/0*NediqPWKuwU_g0i8.gif)

### `Retourner la Carte`

`Pour retourner la carte lorsqu'elle est cliquée, une classe `flip` est ajoutée à l'élément. Pour cela, sélectionnons tous les éléments `memory-card` avec `document.querySelectorAll`. Ensuite, parcourons-les avec `forEach` et attachons un écouteur d'événement. Chaque fois qu'une carte est cliquée, la fonction `flipCard` sera déclenchée. La variable `this` représente la carte qui a été cliquée. La fonction accède à la `classList` de l'élément et bascule la classe `flip` :`

`Dans le CSS, la classe `flip` fait tourner la carte de 180deg :`

`Pour produire l'effet de retournement 3D, nous ajouterons la propriété [perspective](https://developer.mozilla.org/en-US/docs/Web/CSS/perspective) à `.memory-game`. Cette propriété définit à quelle distance dans le plan `z` l'objet se trouve de l'utilisateur. Plus la valeur est faible, plus l'effet de perspective est grand. Pour un effet subtil, appliquons `1000px` :`

`Aux éléments `.memory-card`, ajoutons `transform-style: preserve-3d`, pour les positionner dans l'espace 3D créé dans le parent, au lieu de les aplatir dans le plan `z = 0` ([transform-style](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-style)).`

`Maintenant, une transition doit être appliquée à la propriété `transform` pour produire l'effet de mouvement :`

`Donc, nous avons réussi à faire un retournement 3D de la carte, youpi ! Mais pourquoi la face de la carte ne s'affiche-t-elle pas ? Actuellement, `.front-face` et `.back-face` sont empilés l'un sur l'autre, car ils sont positionnés de manière absolue. Chaque élément a une `face arrière`, qui est une image miroir de sa `face avant`. La propriété [backface-visibility](https://developer.mozilla.org/en-US/docs/Web/CSS/backface-visibility) est par défaut `visible`, donc lorsque nous retournons la carte, ce que nous obtenons est la face arrière du badge JS.`

![Image](https://cdn-media-1.freecodecamp.org/images/0*k2MPONGEHyHGYvyl.gif)

`Pour révéler l'image en dessous, appliquons `backface-visibility: hidden` à `.front-face` et `.back-face`.`

`Si nous actualisons la page et retournons une carte, elle a disparu !`

![Image](https://cdn-media-1.freecodecamp.org/images/0*YCMzdW-z0yruzOPf.gif)

`Puisque nous avons masqué la face arrière des deux images, il n'y a rien de l'autre côté. Nous devons donc tourner `.front-face` de 180 degrés :`

`Et maintenant, nous avons l'effet de retournement souhaité !`

![Image](https://cdn-media-1.freecodecamp.org/images/0*QQAnvvQeYs7iFSAo.gif)

### `Correspondance des Cartes`

`Maintenant que nous avons des cartes qui se retournent, gérons la logique de correspondance.`

`Lorsque nous cliquons sur la première carte, elle doit attendre qu'une autre carte soit retournée. Les variables `hasFlippedCard` et `flippedCard` géreront l'état de retournement. Si aucune carte n'est retournée, `hasFlippedCard` est définie sur `true` et `flippedCard` est définie sur la carte cliquée. Changeons également la méthode `toggle` en `add` :`

`Ainsi, lorsque l'utilisateur clique sur la deuxième carte, nous entrerons dans le bloc else de notre condition. Nous vérifierons s'il y a une correspondance. Pour ce faire, identifions chaque carte.`

`Chaque fois que nous souhaitons ajouter des informations supplémentaires aux éléments HTML, nous pouvons utiliser les [attributs de données](https://developer.mozilla.org/en-US/docs/Learn/HTML/Howto/Use_data_attributes). En utilisant la syntaxe suivante : `data-*`, où `*` peut être n'importe quel mot, cet attribut sera inséré dans la propriété dataset de l'élément. Ajoutons donc un `data-framework` à chaque carte :`

`Maintenant, nous pouvons vérifier s'il y a une correspondance en accédant aux datasets des deux cartes. Extrayons la logique de correspondance dans sa propre méthode `checkForMatch()` et définissons également `hasFlippedCard` sur false. En cas de correspondance, `disableCards()` est invoquée et les écouteurs d'événements sur les deux cartes sont détachés, pour empêcher tout retournement supplémentaire. Sinon, `unflipCards()` retournera les deux cartes après un timeout de 1500ms qui supprime la classe `.flip` :`

`En mettant tout ensemble :`

`Une manière plus élégante d'écrire la condition de correspondance est d'utiliser un [opérateur ternaire](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_Operator). Il est composé de trois blocs. Le premier bloc est la condition à évaluer. Le deuxième bloc est exécuté si la condition retourne true, sinon le bloc exécuté est le troisième :`

### `Verrouiller le Plateau`

`Maintenant que nous avons couvert la logique de correspondance, nous devons verrouiller le plateau. Nous verrouillons le plateau pour éviter que deux ensembles de cartes ne soient retournés en même temps, sinon le retournement échouera.`

![Image](https://cdn-media-1.freecodecamp.org/images/0*z1gY24eYgqu2cjvw.gif)

`Déclarons une variable `lockBoard`. Lorsque le joueur clique sur la deuxième carte, `lockBoard` sera définie sur `true` et la condition `if (lockBoard) return;` empêchera tout retournement de carte avant que les cartes ne soient cachées ou correspondantes :`

### `Clic sur la Même Carte`

`Il reste encore le cas où le joueur peut cliquer deux fois sur la même carte. La condition de correspondance évaluerait à true, supprimant l'écouteur d'événement de cette carte.`

![Image](https://cdn-media-1.freecodecamp.org/images/0*WuPO5Ra7nRNJkZIO.gif)

`Pour éviter cela, vérifions si la carte cliquée actuellement est égale à la `firstCard` et retournons si c'est positif.`

`Les variables `firstCard` et `secondCard` doivent être réinitialisées après chaque tour, donc extrayons cela dans une nouvelle méthode `resetBoard()`. Placions également `hasFlippedCard = false;` et `lockBoard = false` là-bas. L'[affectation par déstructuration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment) es6 `[var1, var2] = ['value1', 'value2']`, nous permet de garder le code super court :`

`La nouvelle méthode sera appelée à la fois depuis `disableCards()` et `unflipCards()` :`

### `Mélange`

`Notre jeu a l'air assez bien, mais ce n'est pas amusant si les cartes ne sont pas mélangées, alors occupons-nous de cela maintenant.`

`Lorsque `display: flex` est déclaré sur le conteneur, les `flex-items` sont disposés selon la hiérarchie suivante : _groupe_ et _ordre source_. Chaque groupe est défini par la propriété [order](https://marina-ferreira.github.io/tutorials/css/flexbox/#order), qui contient un entier positif ou négatif. Par défaut, chaque `flex-item` a sa propriété `order` définie sur `0`, ce qui signifie qu'ils appartiennent tous au même groupe et seront disposés par ordre source. S'il y a plus d'un groupe, les éléments sont d'abord disposés par ordre de groupe croissant.`

`Il y a 12 cartes dans le jeu, donc nous allons itérer à travers elles, générer un nombre aléatoire entre 0 et 12 et l'assigner à la propriété `order` du flex-item :`

`Pour invoquer la fonction `shuffle`, faisons-en une [Expression de Fonction Invocable Immédiatement (IIFE)](https://developer.mozilla.org/en-US/docs/Glossary/IIFE), ce qui signifie qu'elle s'exécutera elle-même immédiatement après sa déclaration. Les scripts devraient ressembler à ceci :`

`Et c'est tout, les amis !`

`Vous pouvez également trouver une explication vidéo sur ? [Chaîne Code Sketch](https://www.youtube.com/watch?v=eMhiMsEC9Uk&list=PLLX1I3KXZ-YH-woTgiCfONMya39-Ty8qw).`

### `Références`

* `[Marina Ferreira — Fondamentaux de Flexbox](https://marina-ferreira.github.io/tutorials/css/flexbox/)`
* `[MDN Web Docs — Axe Principal](https://developer.mozilla.org/en-US/docs/Glossary/Main_Axis)`
* `[MDN Web Docs — Axe Transversal](https://developer.mozilla.org/en-US/docs/Glossary/Cross_Axis)`
* `[MDN Web Docs — calc](https://developer.mozilla.org/en-US/docs/Web/CSS/calc)`
* `[MDN Web Docs — perspective](https://developer.mozilla.org/en-US/docs/Web/CSS/perspective)`
* `[MDN Web Docs — transform-style](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-style)`
* `[MDN Web Docs — backface-visibility](https://developer.mozilla.org/en-US/docs/Web/CSS/backface-visibility)`
* `[MDN Web Docs — Utilisation des attributs de données](https://developer.mozilla.org/en-US/docs/Learn/HTML/Howto/Use_data_attributes)`
* `[MDN Web Docs — order](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout/Ordering_Flex_Items)`
* `[MDN Web Docs — IIFE](https://developer.mozilla.org/en-US/docs/Glossary/IIFE)`
* `[MDN Web Docs — opérateur ternaire](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_Operator)`
* `[MDN Web Docs — affectation par déstructuration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment)`

`_Publié à l'origine sur [marina-ferreira.github.io](https://marina-ferreira.github.io/tutorials/js/memory-game/).`