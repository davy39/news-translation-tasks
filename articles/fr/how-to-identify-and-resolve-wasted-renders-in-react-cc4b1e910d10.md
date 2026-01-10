---
title: Comment identifier et résoudre les rendus inutiles dans React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-22T15:17:08.000Z'
originalURL: https://freecodecamp.org/news/how-to-identify-and-resolve-wasted-renders-in-react-cc4b1e910d10
coverImage: https://cdn-media-1.freecodecamp.org/images/1*PAy2dYBC4-B2JY9l4u4v4g.png
tags:
- name: optimization
  slug: optimization
- name: performance
  slug: performance
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: Comment identifier et résoudre les rendus inutiles dans React
seo_desc: 'By Nayeem Reza

  So, recently I was thinking about performance profiling of a react app that I was
  working on, and suddenly thought to set a few performance metrics. And I did come
  across that the first thing I need to tackle is wasted renders I’m doin...'
---

Par Nayeem Reza

Récemment, je réfléchissais au profilage des performances d'une application React sur laquelle je travaillais, et j'ai soudainement pensé à définir quelques métriques de performance. Et je me suis rendu compte que la première chose que je dois aborder est les _rendus inutiles_ que je fais sur chacune des pages web. Vous vous demandez peut-être ce que sont les rendus inutiles ? Plongeons-nous dans le sujet.

Dès le début, React a changé toute la philosophie de la construction d'applications web et, par conséquent, la façon dont les développeurs front-end pensent. Avec son introduction du _Virtual DOM_, React rend les mises à jour de l'UI aussi efficaces qu'elles peuvent l'être. Cela rend l'expérience de l'application web fluide. Vous êtes-vous déjà demandé comment rendre vos applications React plus rapides ? Pourquoi les applications web React de taille modérée ont-elles encore tendance à performer médiocrement ? Les problèmes résident dans la manière dont nous utilisons réellement React !

### Comment React fonctionne

Une bibliothèque front-end moderne comme [React](https://facebook.github.io/react/) ne rend pas notre application plus rapide de manière magique. Tout d'abord, nous, les développeurs, devons comprendre comment React fonctionne. Comment les composants vivent-ils à travers les cycles de vie des composants dans la durée de vie des applications ? Donc, avant de plonger dans toute technique d'optimisation, nous devons avoir une meilleure compréhension de la manière dont React fonctionne sous le capot.

Au cœur de React, nous avons la syntaxe JSX et la puissante capacité de React à construire et comparer des [virtual DOMs](http://reactkungfu.com/2015/10/the-difference-between-virtual-dom-and-dom/). Depuis sa sortie, React a influencé de nombreuses autres bibliothèques front-end. Par exemple, Vue.js repose également sur l'idée des virtual DOMs.

Chaque application React commence avec un composant racine. Nous pouvons penser à l'ensemble de l'application comme à une formation en arbre où chaque nœud est un composant. Les composants dans React sont des 'fonctions' qui rendent l'UI en fonction des données. Cela signifie les _props_ et l'_état_ qu'ils reçoivent ; disons que c'est `CF`

```
UI = CF(data)
```

Les utilisateurs interagissent avec l'UI et provoquent le changement des données. Les interactions sont tout ce qu'un utilisateur peut faire dans notre application. Par exemple, cliquer sur un bouton, faire défiler des images, déplacer des éléments de liste, et les requêtes AJAX invoquant des APIs. Toutes ces interactions ne changent que les données. Elles ne provoquent aucun changement dans l'UI.

Ici, les données sont tout ce qui définit l'_état_ d'une application. Pas seulement ce que nous avons stocké dans notre base de données. Même différents états front-end comme quel onglet est actuellement sélectionné ou si une case à cocher est actuellement cochée ou non font partie de ces données. Chaque fois qu'il y a un changement dans les données, React utilise les fonctions de composant pour re-rendre l'UI, mais seulement virtuellement :

```
UI1 = CF(data1)
UI2 = CF(data2)
```

React calcule les différences entre l'UI actuelle et la nouvelle UI en appliquant un [algorithme de comparaison](https://reactjs.org/docs/reconciliation.html#the-diffing-algorithm) sur les deux versions de son virtual DOM.

```
Changes = Difference(UI1, UI2)
```

React procède ensuite à l'application uniquement des changements d'UI à l'UI réelle dans le navigateur. Lorsque les données associées à un composant changent, React détermine si une mise à jour réelle du DOM est nécessaire. Cela permet à React d'éviter des opérations de manipulation du DOM potentiellement coûteuses dans le navigateur. Des exemples tels que la création de nœuds DOM et l'accès à des nœuds existants au-delà de la nécessité.

Cette différenciation et ce rendu répétés des composants peuvent être l'une des principales sources de problèmes de performance de React dans toute application React. Construire une application React où l'algorithme de différenciation échoue à [réconcilier](https://reactjs.org/docs/reconciliation.html) efficacement, provoquant le rendu de l'ensemble de l'application de manière répétée, ce qui cause en réalité des rendus inutiles et peut entraîner une expérience frustramment lente.

Pendant le processus de rendu initial, React construit un arbre DOM comme ceci —

![Image](https://cdn-media-1.freecodecamp.org/images/y4qB7PH40s9RK02BE5njs2w-lPMJVrKtqqor)

Supposons qu'une partie des données change. Ce que nous voulons que React fasse, c'est de re-rendre uniquement les composants qui sont directement affectés par ce changement spécifique. Possiblement sauter même le processus de différenciation pour le reste des composants. Disons que certaines données changent dans le Composant `2` dans l'image ci-dessus, et que ces données ont été passées de `R` à `B` puis à `2`. Si R se re-rend, alors il re-rendra chacun de ses enfants, c'est-à-dire A, B, C, D, et par ce processus, ce que React fait réellement, c'est ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/2X1HZDWVjVFi0fib0I9qUEEyeFIWLnBDcolg)

Dans l'image ci-dessus, tous les nœuds jaunes sont rendus et différenciés. Cela entraîne une perte de temps/ressources de calcul. C'est là que nous mettrons principalement nos efforts d'optimisation. Configurer chaque composant pour qu'il ne se rende et ne se différencie que lorsqu'il est nécessaire. Cela nous permettra de récupérer ces cycles CPU gaspillés. Tout d'abord, nous allons examiner la manière dont nous pouvons identifier les rendus inutiles de notre application.

### Identifier les rendus inutiles

Il existe plusieurs façons de procéder. La méthode la plus simple consiste à activer l'option _mettre en surbrillance les mises à jour_ dans les préférences des outils de développement React.

![Image](https://cdn-media-1.freecodecamp.org/images/Rjxm5xSv-yo4igzgz4OhGUsyRobsIjnJMCTq)

Lors de l'interaction avec l'application, les mises à jour sont mises en surbrillance à l'écran avec des bordures colorées. Grâce à ce processus, vous devriez voir les composants qui ont été re-rendus. Cela nous permet de repérer les re-rendus qui n'étaient pas nécessaires.

Suivons cet exemple.

![Image](https://cdn-media-1.freecodecamp.org/images/sEbzC97cYGA21Sap7VGKTlwNZ5OEBCDZwzD5)

Notez que lorsque nous entrons une deuxième tâche, la première 'tâche' clignote également à l'écran à chaque frappe. Cela signifie qu'elle est re-rendue par React en même temps que l'entrée. C'est ce que nous appelons un rendu 'inutile'. Nous savons qu'il est inutile parce que le contenu de la première tâche n'a pas changé, mais React ne le sait pas.

Même si React ne met à jour que les nœuds DOM modifiés, le re-rendu prend tout de même un certain temps. Dans de nombreux cas, ce n'est pas un problème, mais si le ralentissement est perceptible, nous devrions envisager quelques solutions pour arrêter ces rendus redondants.

### Utilisation de la méthode shouldComponentUpdate

Par défaut, React rendra le virtual DOM et comparera la différence pour chaque composant de l'arbre pour tout changement dans ses props ou son état. Mais cela n'est évidemment pas raisonnable. À mesure que notre application grandit, tenter de re-rendre et de comparer l'ensemble du virtual DOM à chaque action finira par ralentir tout le système.

React fournit une méthode de cycle de vie simple pour indiquer si un composant a besoin d'être re-rendu, et c'est `shouldComponentUpdate`, qui est déclenchée avant le début du processus de re-rendu. L'implémentation par défaut de cette fonction retourne `true`.

![Image](https://cdn-media-1.freecodecamp.org/images/M8-a8KtHWAtoicHp8-mmVkEd-FX-gqwZw6Co)

Lorsque cette fonction retourne vrai pour un composant, elle permet au processus de différenciation de rendu d'être déclenché. Cela nous donne le pouvoir de contrôler le processus de différenciation de rendu. Supposons que nous devons empêcher un composant d'être re-rendu, nous devons simplement retourner `false` depuis cette fonction. Comme nous pouvons le voir à partir de l'implémentation de la méthode, nous pouvons comparer les props et l'état actuels et suivants pour déterminer si un re-rendu est nécessaire :

![Image](https://cdn-media-1.freecodecamp.org/images/5ERuL7iT4wDYhPCj9mmhSwp-cCch6ydPdNMJ)

### Utilisation de composants purs

En travaillant sur React, vous connaissez définitivement `React.Component`, mais quel est l'intérêt de `React.PureComponent` ? Nous avons déjà discuté de la méthode de cycle de vie shouldComponentUpdate, dans les composants purs, il y a déjà une implémentation par défaut de `shouldComponentUpdate()` avec une comparaison superficielle des props et de l'état. Donc, un composant pur est un composant qui ne se re-rend que si `props/state` est différent des _props_ et _state_ précédents.

![Image](https://cdn-media-1.freecodecamp.org/images/jQnYm0ejA57POOcjmOJ1fauWWC7kB0q-y7Dr)

> Dans la comparaison superficielle, les types de données primitifs comme string, boolean, number sont comparés par valeur et les types de données complexes comme array, object, function sont comparés par référence

Mais, que faire si nous avons un composant stateless fonctionnel dans lequel nous devons implémenter cette méthode de comparaison avant chaque re-rendu ? React a un Higher Order Component `React.memo`. C'est comme `React.PureComponent` mais pour les composants fonctionnels au lieu des classes.

![Image](https://cdn-media-1.freecodecamp.org/images/A1MmnhyMmXvz-kwKx6619gJVx7IfUwMJGSKR)

Par défaut, il fait la même chose que shouldComponentUpdate() qui ne compare que superficiellement l'objet props. Mais, si nous voulons avoir le contrôle sur cette comparaison ? Nous pouvons également fournir une fonction de comparaison personnalisée comme second argument.

![Image](https://cdn-media-1.freecodecamp.org/images/38vWplvDxFSEpjSeL72vcNaLRs7XzBYwa1xI)

### Rendre les données immuables

Et si nous pouvions utiliser un `React.PureComponent` mais avoir tout de même un moyen efficace de savoir quand des props ou états complexes comme un tableau, un objet, etc., ont changé automatiquement ? C'est là que la structure de données immuable facilite la vie.

L'idée derrière l'utilisation de structures de données immuables est simple. Comme nous l'avons discuté précédemment, pour les types de données complexes, la comparaison est effectuée sur leur référence. Chaque fois qu'un objet contenant des données complexes change, au lieu de faire les changements dans cet objet, nous pouvons créer une copie de cet objet avec les changements qui créeront une nouvelle référence.

ES6 a un opérateur de propagation d'objet pour faire cela.

![Image](https://cdn-media-1.freecodecamp.org/images/CbPn9o3eE53eh784JIzXPwaS7oqOefb-wW-O)

Nous pouvons faire de même pour les tableaux :

![Image](https://cdn-media-1.freecodecamp.org/images/n73IBFev-5etKfGYTOAH-qAs8R3E6EICcaSv)

### Éviter de passer une nouvelle référence pour les mêmes anciennes données

Nous savons que chaque fois que les `props` d'un composant changent, un re-rendu se produit. Mais parfois les `props` n'ont pas changé. Nous écrivons du code de manière à ce que React pense qu'ils ont changé, et cela provoquera également un re-rendu, mais cette fois, c'est un rendu inutile. Donc, en gros, nous devons nous assurer que nous passons une référence différente en tant que props pour des données différentes. De plus, nous devons éviter de passer une nouvelle référence pour les mêmes données. Maintenant, nous allons examiner quelques cas où nous créons ce problème. Regardons ce code.

![Image](https://cdn-media-1.freecodecamp.org/images/qDjrVvrQAPlavtw0rQGE05jPWXFvP8unpt9n)

Voici le contenu du composant `BookInfo` où nous rendons deux composants, `BookDescription` et `BookReview`. Ce code est correct et fonctionne bien, mais il y a un problème. `BookDescription` se re-rendra chaque fois que nous recevrons de nouvelles données de critiques en tant que props. Pourquoi ? Dès que le composant `BookInfo` reçoit de nouvelles props, la fonction `render` est appelée pour créer son arbre d'éléments. La fonction render crée une nouvelle constante `book`, ce qui signifie qu'une nouvelle référence est créée. Donc, `BookDescription` recevra ce `book` comme une nouvelle référence, ce qui provoquera le re-rendu de `BookDescription`. Donc, nous pouvons refactoriser ce morceau de code en ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/ushbIP1Vt8uV63TFX6DGyQAQZpIoNiW7BzPg)

Maintenant, la référence est toujours la même, `this.book`, et un nouvel objet n'est pas créé au moment du rendu. Cette philosophie de re-rendu s'applique à chaque `prop`, y compris les gestionnaires d'événements, comme :

![Image](https://cdn-media-1.freecodecamp.org/images/xmUdrbVqtYaa37e1Ds4ykJRiZRzpsQweDUVz)

Ici, nous avons utilisé deux méthodes différentes (liaison de méthodes et utilisation de fonctions fléchées dans le rendu) pour invoquer les méthodes de gestion d'événements, mais les deux créeront une nouvelle fonction chaque fois que le composant se re-rendra. Donc, pour corriger ces problèmes, nous pouvons lier la méthode dans le `constructeur` et utiliser les propriétés de classe, qui est encore expérimentale et non standardisée, mais tant de développeurs utilisent déjà cette méthode pour passer des fonctions à d'autres composants dans des applications prêtes pour la production :

![Image](https://cdn-media-1.freecodecamp.org/images/wTadfqSaGeRy7nH-jSt2-285fbZGi2Zoy9rH)

### Conclusion

En interne, React utilise plusieurs techniques astucieuses pour minimiser le nombre d'opérations DOM coûteuses nécessaires à la mise à jour de l'UI. Pour de nombreuses applications, l'utilisation de React conduira à une interface utilisateur rapide sans avoir à faire beaucoup de travail pour optimiser spécifiquement les performances. Néanmoins, si nous pouvons suivre les techniques que j'ai mentionnées ci-dessus pour résoudre les rendus inutiles, alors pour les grandes applications, nous obtiendrons également une expérience très fluide en termes de performance.