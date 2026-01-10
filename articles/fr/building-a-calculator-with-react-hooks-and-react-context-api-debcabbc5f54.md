---
title: Comment construire une calculatrice avec React Hooks et l'API Context de React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-14T17:24:25.000Z'
originalURL: https://freecodecamp.org/news/building-a-calculator-with-react-hooks-and-react-context-api-debcabbc5f54
coverImage: https://cdn-media-1.freecodecamp.org/images/0*rqZDBlph5lAF0kSO
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment construire une calculatrice avec React Hooks et l'API Context de
  React
seo_desc: 'By Theran Brigowatz

  If you are like me, when you first heard of React Hooks you were maybe a little
  bit ambivalent or confused by what all the hype was about. What’s the big deal if
  I don’t have to write out class components anymore? However, once I ...'
---

Par Theran Brigowatz

Si vous êtes comme moi, lorsque vous avez entendu parler pour la première fois des React Hooks, vous étiez peut-être un peu ambivalent ou confus quant à tout ce battage médiatique. Quel est l'intérêt si je n'ai plus à écrire des composants de classe ? Cependant, une fois que je m'y suis plongé et que je les ai utilisés, je ne pouvais plus vraiment me voir revenir à mes jours d'avant les Hooks. Dans les mots immortels de Blues Traveller, « The hook brings you back. I ain't tellin' you no lie. »

Pendant un moment, j'ai cherché un guide sur la façon d'utiliser les Hooks en connexion avec l'API Context. Après avoir trouvé seulement quelques exemples qui expliquaient pleinement le concept, j'ai décidé de faire ce que tout bon développeur devrait faire : me plonger dans les docs et construire quelque chose moi-même. Lutter à travers et l'apprendre par soi-même est l'une des meilleures façons d'absorber les connaissances. Ce guide explique comment construire le même projet que j'ai fait avec l'utilisation des Hooks et du Context.

#### Aperçu

Ce projet va être une application de calculatrice de base similaire à la calculatrice de l'iPhone. Puisque ce n'est qu'une simple application de bureau, j'ai remplacé le bouton % par un bouton de retour. Bien que je ne l'utiliserais pas pour passer les SAT, vous pourriez certainement additionner le nombre d'orteils que vous avez dessus.

Il y a une version déployée fonctionnelle du projet, ou vous pouvez consulter tout le code sur [GitHub](https://github.com/theranbrig/calculator).

![Image](https://cdn-media-1.freecodecamp.org/images/1*0XzsNDAyjANtW7Q7dqCkQA.png)
_Notre disposition de l'application. Rien de trop fantaisiste ici._

### Le Projet

#### Installation

Pour commencer, nous allons simplement utiliser `create-react-app`. Vous pouvez commencer en exécutant ce qui suit :

```
npx create-react-app calculatorcd calculatornpm start
```

#### Structure des fichiers et CSS

La structure des fichiers de l'application devrait ressembler à ce qui suit. Dans le dossier `src`, créez les fichiers suivants ou laissez simplement `App.js` et `index.js`.

```
src├── App.js├── index.js└── components    ├── BackButton.js    ├── Calculator.js    ├── ClearButton.js    ├── Display.js        ├── EqualButton.js    ├── FunctionButton.js    ├── NegativeButton.js    ├── NumberButton.js    ├── NumberProvider.js    └── styles        └── Styles.js
```

Si vous souhaitez suivre exactement, vous pouvez également installer Styled Components pour le CSS.

`npm -i styled-components`

Vous pouvez ensuite ajouter le CSS Styled depuis [ce lien](https://gist.github.com/theranbrig/dbf478ac4c961d6c8a193de582420ce1) au fichier `Styles.js` ou ajouter le vôtre.

#### Structure principale de l'application

Le fichier `Calculator.js` doit configurer l'affichage et le pavé numérique. Il doit contenir tous les types de boutons.

Vous remarquerez que tous les composants de boutons sont ajoutés ici ainsi que l'affichage des nombres. Chacun des composants de boutons est essentiellement le même. Ils doivent tous suivre la même structure de base. Le `zero-button` obtient un `div` séparé puisque nous utilisons CSS Grid pour la disposition et il doit s'étendre sur deux colonnes. (PS — Si vous voulez en savoir plus sur CSS Grid, j'ai fait un [petit article](https://medium.com/@theran.brigowatz/gettin-griddy-with-it-build-your-own-css-grid-and-drop-the-frameworks-7d8c498c8b1b) sur les bases.)

Vous remarquerez peut-être que la propriété `buttonValue` n'est nécessaire que pour les composants `NumberButton` et `FunctionButton`. Chacun des boutons doit suivre la même structure de base avec un nom unique. Vous pouvez vous référer à la structure des fichiers ci-dessus pour voir quels boutons sont nécessaires. Les boutons doivent avoir le symbole écrit dans le composant de bouton s'ils ne reçoivent pas de `buttonValue` via les props. Créez l'un de ceux-ci pour chacun des types de boutons dans votre structure de fichiers.

Après cela, vous devriez avoir la structure de base d'une calculatrice. Nous allons revenir à l'affichage dans un instant. Maintenant, nous allons nous pencher sur le fonctionnement interne de l'application et voir comment nous pouvons utiliser nos Hooks et Context.

#### Construction du fournisseur de l'API Context

Nous allons maintenant créer le `NumberProvider.js`. C'est le cœur de votre application et c'est là que nos fonctions vont résider. Si vous n'avez jamais utilisé l'API Context de React, c'est un excellent outil pour aider à passer des données d'un composant à un autre.

Pensez à quand vous avez des composants qui sont imbriqués les uns dans les autres. Dans le passé, vous deviez « prop driller ». C'est lorsque vous passez les données ou la fonction en tant que props dans des composants imbriqués. Ce n'est guère idéal, surtout lorsque vous commencez à aller plusieurs niveaux plus profond.

Cependant, avec ce composant fournisseur, il vous permet de passer des données à n'importe quel composant imbriqué, peu importe la profondeur. Ce fournisseur de nombres va envelopper notre composant `App`. Maintenant, chaque fois que nous voulons obtenir des données, ou utiliser une fonction qui réside dans le fournisseur, elle est globalement disponible. Cela nous évite d'avoir à « prop driller » à travers des composants imbriqués. Vous maintenez la source unique de vérité qui est l'essence de React. Pour commencer, vous devez créer le fournisseur. Il devrait ressembler à ce qui suit :

Le fournisseur de base est créé et toute valeur qui est passée est maintenant disponible pour tous les composants imbriqués. Afin de rendre cela disponible, nous allons envelopper notre composant `App` pour qu'il soit globalement disponible. Notre `App` aura ce code.

#### Utilisation du fournisseur de contexte

Maintenant, nous pouvons ajouter le code pour notre affichage. Nous pouvons afficher la valeur en passant la fonction `useContext` de la nouvelle API React Hooks. Nous n'avons plus à passer les props à travers des composants imbriqués. L'affichage devrait ressembler à :

Le nombre que vous avez passé trois niveaux plus haut dans le `NumberProvider` est immédiatement disponible pour le composant `Display` en appelant `useContext` et en passant notre `NumberContext` créé. Votre affichage de nombre est maintenant opérationnel car il affiche `number` que nous avons défini à zéro.

Maintenant, bien sûr, notre calculatrice affiche un seul zéro. C'est génial si vous comptez le nombre d'heures de sommeil que je fais avec un fils nouveau-né, mais pas si génial si vous essayez d'additionner autre chose, alors utilisons quelques hooks pour faire calculer cette calculatrice.

#### Premiers pas avec les Hooks

Si vous n'avez jamais utilisé de hook auparavant, il vous permet essentiellement de vous débarrasser de la syntaxe de classe et d'avoir un état au sein des composants fonctionnels. Ici, nous pouvons ajouter ce qui suit à notre fichier `NumberProvider.js` afin de créer notre premier hook.

Il peut y avoir une syntaxe que vous n'avez pas vue. Plutôt que d'écrire notre classe avec un état, nous divisons chaque partie de l'état en sa propre variable `number` plus petite. Il y a aussi `setNumber` qui agit de la même manière que la fonction `setState`, mais qui fonctionne maintenant pour une variable spécifique et peut être appelée lorsque nécessaire. `useState` nous permet de définir une valeur initiale.

Nous sommes maintenant en mesure d'utiliser tout cela dans notre fonction pour passer les valeurs des boutons de nombre dans l'affichage. Dans cette application, la calculatrice utilise des chaînes de caractères pour obtenir l'entrée. Il y a des vérifications pour s'assurer que vous ne pouvez pas avoir plusieurs `.` dans votre nombre et que vous n'avez pas de séries de zéros pour commencer votre nombre.

#### Construction des composants de boutons

Maintenant, vous pouvez appeler cette fonction en utilisant l'API Context dans l'un des composants imbriqués.

Maintenant, vous avez un générateur de chaînes de nombres fonctionnel. Vous pouvez voir comment vous pouvez commencer à injecter les valeurs que vous avez définies dans le `NumberProvider` dans les autres composants de l'application via la fonction `useContext`. L'état et les fonctions qui l'affectent sont conservés dans le `NumberProvider`. Vous devez simplement appeler le contexte spécifique que vous souhaitez.

Vous pouvez commencer à voir comment cela serait génial lorsque vous commencez à ajouter plus de complexité à votre application. Supposons que vous voulez un composant utilisateur pour vérifier que vous êtes connecté pour utiliser des fonctionnalités spéciales. Vous pouvez créer un fournisseur séparé qui contient les données utilisateur et les rend disponibles à tout composant imbriqué.

Nous pouvons continuer à ajouter des fonctions à notre calculatrice et les passer au composant approprié via la fonction `useContext` intégrée.

#### Fonctions du fournisseur complétées

Le `NumberProvider` complété se trouve ci-dessous et contient les fonctions suivantes qui sont utilisées avec les hooks.

* `handleSetDisplayValue` définit la valeur que vous tapez dans l'affichage. Nous vérifions qu'il n'y a qu'un seul décimal dans la chaîne de nombres et nous limitons la longueur du nombre à 8 caractères. Pensez à cela comme une calculatrice de pourboire plutôt que comme une calculatrice pour vous aider à passer votre examen de calcul. Elle prend la propriété `buttonValue` dans `NumberButton.js`.
* `handleSetStoredValue` prend notre chaîne d'affichage et la stocke afin que nous puissions entrer un autre nombre. C'est notre valeur stockée. Elle sera utilisée comme fonction auxiliaire.
* `handleClearValue` réinitialise tout à 0. C'est votre fonction de réinitialisation. Elle sera passée à `ClearButton.js`.
* `handleBackButton` vous permet de supprimer vos caractères précédemment entrés un par un jusqu'à ce que vous reveniez à 0. Cela appartient au fichier `BackButton.js`.
* `handleSetCalcFunction` est l'endroit où vous obtenez votre fonction mathématique. Elle définit si vous ajoutez, soustrayez, divisez ou multipliez. Elle est passée dans le fichier `FunctionButton.js` et prend la propriété `buttonValue`.
* `handleToggleNegative` fait exactement ce que le nom implique. Elle vous permet de le faire soit pour la valeur d'affichage, soit pour une valeur stockée après un calcul. Cela va bien sûr dans `NegativeButton.js`.
* `doMath` fait les maths. Enfin. Puisque ce n'est qu'une simple calculatrice à quatre fonctions, elle utilise simplement une fonction switch simple selon le `functionType` que nous avons dans l'état. Nous utilisons `parseInt` puisque nous passons notre nombre en chaînes de caractères. De plus, nous arrondissons à seulement trois décimales, pour nous assurer que nous n'avons pas de nombres trop longs.

#### L'affichage finalisé

Vous aurez également besoin d'un affichage. Dans ce cas, il affichera le `number` et le `storedNumber` ainsi que votre `functionType`. Il y a quelques vérifications telles que l'affichage d'un 0 lorsque vous avez une chaîne vide comme nombre.

Pour des raisons de brièveté, je ne vais pas inclure toutes les fonctions de boutons puisqu'elles sont à peu près les mêmes que le fichier `NumberButton.js` ci-dessus. Assurez-vous simplement de passer une propriété `buttonValue` lorsque cela est nécessaire, et que vous passez la fonction correcte de la liste ci-dessus.

#### Voir tout le code

Si vous souhaitez voir tout le code de ce projet, il peut être trouvé sur :

[Dépôt GitHub](https://github.com/theranbrig/calculator.)

[Déploiement Calc-U-Later](https://calc-u-later.netlify.com/)

### Conclusion

J'espère que cela clarifie un peu comment les React Hooks et l'API Context peuvent être utilisés ensemble. L'utilisation de ces fonctionnalités intégrées de React offre plusieurs avantages.

* Syntaxe simple à comprendre et se débarrasse de l'encombrement des composants de classe. Plus de super et de constructeurs. Juste quelques variables propres.
* Plus facile à définir et à utiliser l'état au sein et à travers les composants. Plus de prop drilling désordonné à travers plusieurs composants.
* Élimine le besoin de Redux dans les petits projets, où vous n'avez pas besoin de conserver trop de choses dans un état complexe. Vous ne allez probablement pas recréer Facebook avec cela, mais cela fera le travail sur des applications à petite échelle.

Veuillez me faire savoir vos pensées ou si vous rencontrez des problèmes dans le code. J'espère que cela a jeté un peu de lumière sur quelque chose que vous n'auriez peut-être pas connu auparavant. Les React Hooks et Context sont d'excellents moyens de simplifier vos applications React et d'écrire un code plus propre.

Consultez plus de mon travail et d'autres projets sur [https://theran.co](https://theran.co).