---
title: Une introduction aux Hooks React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-14T21:50:42.000Z'
originalURL: https://freecodecamp.org/news/an-introduction-to-react-hooks-12843fcd2fd9
coverImage: https://cdn-media-1.freecodecamp.org/images/1*lTaYmnmt1NdkNFh7u6zzkw.png
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: technology
  slug: technology
seo_title: Une introduction aux Hooks React
seo_desc: 'By Harsh Makadia

  As the ReactJs library gets new updates, there are a lot of things being added and
  a few that are deprecated too. ReactJs is becoming more powerful day by day due
  to such updates. As a developer, you need to keep yourself up to date ...'
---

Par Harsh Makadia

Alors que la bibliothèque ReactJs reçoit de nouvelles mises à jour, de nombreuses choses sont ajoutées et certaines sont dépréciées. ReactJs devient de plus en plus puissant jour après jour grâce à ces mises à jour. En tant que développeur, vous devez vous tenir au courant des nouvelles fonctionnalités de chaque version.

#### Avez-vous entendu parler des Hooks React ?

Eh bien, les Hooks React, une fonctionnalité disponible dans _React v16.7.0-alpha_, est quelque chose d'awesome que vous devriez connaître.

Voici un aperçu des Hooks React.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ap02eQb0KjTorrDDuq06UQ.png)
_React Hooks_

Dans le code ci-dessus, `useState` est le premier Hook.

Maintenant, plongeons dans le problème que les Hooks React vont résoudre.

Après tout, chaque nouvelle fonctionnalité est introduite pour résoudre un problème. Voici la liste des choses que le [site officiel de React](https://reactjs.org/docs/hooks-intro.html) a à dire sur les problèmes qui seront résolus.

#### Il est difficile de réutiliser la logique avec état entre les composants

Le comportement réutilisable ne peut pas être attaché au composant React. Un bon exemple pourrait être la connexion au store. Si vous avez une certaine expérience avec React, vous connaissez peut-être certains des motifs comme [render props](https://reactjs.org/docs/render-props.html) et [higher-order components](https://reactjs.org/docs/higher-order-components.html) qui peuvent être utiles pour résoudre de tels problèmes. En utilisant de tels motifs, les composants doivent être restructurés pour les utiliser, ce qui rend le code plus difficile à suivre et à maintenir.

Avec l'introduction des Hooks, la logique avec état peut être extraite du composant. Cela permet de la tester indépendamment et de la réutiliser.

> **_Avec les Hooks, vous pouvez réutiliser la logique avec état sans changer votre hiérarchie de composants._**

#### Les composants complexes deviennent difficiles à comprendre

Il arrive qu'un composant passe d'un état petit à un état ingérable de logique avec état.

Chaque méthode de cycle de vie contient parfois un mélange de logique non liée. Par exemple, un composant peut effectuer des appels d'API dans `componentDidMount` et `componentDidUpdate`. Cependant, la même méthode `componentDidMount` peut également contenir une partie de la logique non liée.

Cette logique configure des écouteurs d'événements avec un nettoyage effectué dans `componentWillUnmount`. Le code lié qui change ensemble est divisé. Le code non lié qui est combiné dans une seule méthode introduit des bugs et des incohérences.

Nous rencontrons souvent une situation où nous ne pouvons pas diviser un grand composant en plus petits en raison des valeurs avec état. De plus, il devient difficile de les tester.

Pour résoudre ce problème, **les Hooks vous permettent de diviser un composant en fonctions plus petites basées sur les pièces liées. Un bon exemple pourrait être la configuration d'un abonnement ou la récupération de données**, indépendamment de la division du code basée sur la méthode de cycle de vie.

> **_Avec les Hooks, plus de fonctionnalités de React peuvent être utilisées sans avoir besoin de classes._**

### Mais comment fonctionnent vraiment les Hooks ?

Voici l'extrait de code que nous avons vu ci-dessus :

[Lien vers CodeSandbox](https://codesandbox.io/s/lpokw8ox67)

L'utilisation de `useState` est le Hook dont nous parlons.

Nous l'appelons à l'intérieur d'un composant fonctionnel pour ajouter un état local. React préservera cet état entre tous les re-rendus. `useState` retourne une paire qui contient la valeur d'état _actuelle_ et une fonction qui vous permet de mettre à jour la valeur.

Vous pouvez appeler cette fonction à partir d'un gestionnaire d'événements ou d'ailleurs. C'est similaire à `this.setState` dans une classe React, mais il ne fusionne pas l'ancien et le nouvel état.

Il n'y a qu'un seul argument pour `useState` qui est l'état initial. Dans cet exemple donné ci-dessus, l'état initial est `0` parce que notre compteur commence à zéro. Notez que contrairement à `this.state`, l'état ici n'a pas nécessairement besoin d'être un objet — cependant, il peut être un objet si vous le souhaitez.

#### Déclarer plusieurs variables d'état

La syntaxe de [déstruction d'array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment#Array_destructuring) donne différents noms aux variables d'état que nous avons déclarées en appelant `useState`. Ces noms ne font pas partie de l'API `useState`. Au lieu de cela, React suppose que si vous appelez plusieurs fois, vous le faites dans le même ordre au moment de chaque rendu.

> **_Note:_** _Les Hooks sont des fonctions qui vous permettent de "vous accrocher" aux fonctionnalités d'état et de cycle de vie de React à partir de composants fonctionnels. **Les Hooks ne fonctionnent pas à l'intérieur des classes React** — ils vous permettent d'utiliser React sans classes._

### Hook d'effet

![Image](https://cdn-media-1.freecodecamp.org/images/1*jy77wO7iZp8OFCn8_WCMPw.png)

En travaillant avec React, vous avez peut-être déjà travaillé sur la récupération de données, les abonnements ou la modification manuelle du DOM à partir de composants React. Nous appelons ces opérations des "effets de bord" (ou "effets" en abrégé).

Le Hook d'effet, `useEffect`, ajoute la capacité d'effectuer les effets de bord à partir d'un composant fonctionnel. Il a le même but que `componentDidMount`, `componentDidUpdate` et `componentWillUnmount` dans les classes React, mais unifié dans une seule API.

Par exemple, le composant ci-dessous définit le titre du document après que React a mis à jour le DOM :

[Lien vers CodeSandbox](https://wn8q6741xl.codesandbox.io/)

Lorsque vous appelez `useEffect`, vous dites à React d'exécuter votre fonction "effet" après avoir appliqué les changements au DOM. Les effets sont déclarés à l'intérieur du composant et ont ainsi accès à ses props et à son état. Par défaut, React exécute les effets après chaque rendu — _y compris_ le premier rendu.

### Règles des Hooks

![Image](https://cdn-media-1.freecodecamp.org/images/1*f4sJzaPTgNR0g95mmVCI3g.png)
_Règles des Hooks_

Les Hooks sont des fonctions JavaScript, mais elles ont deux règles supplémentaires :

* N'appeler les Hooks **qu'au niveau supérieur**. N'essayez pas d'appeler les Hooks à l'intérieur de boucles, de conditions ou de fonctions imbriquées.
* N'appeler les Hooks **qu'à partir de composants fonctionnels React**. N'essayez pas d'appeler les Hooks à partir de fonctions JavaScript régulières.

Eh bien, voici un aperçu rapide des Hooks React. Pour une description plus détaillée, suivez le lien ci-dessous :

[**Hooks en un coup d'œil - React**](https://reactjs.org/docs/hooks-overview.html)
[_Une bibliothèque JavaScript pour construire des interfaces utilisateur_reactjs.org](https://reactjs.org/docs/hooks-overview.html)

Bon apprentissage ! 💡✨