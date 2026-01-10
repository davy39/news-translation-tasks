---
title: Functional setState est l'avenir de React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-03-03T07:00:16.000Z'
originalURL: https://freecodecamp.org/news/functional-setstate-is-the-future-of-react-374f30401b6b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*K8A3aXts5rTCHYRcdHIR6g.jpeg
tags:
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: software development
  slug: software-development
- name: Web Development
  slug: web-development
seo_title: Functional setState est l'avenir de React
seo_desc: 'By Justice Mba

  Update: I gave a follow up talk on this topic at React Rally. While this post is
  more about the “functional setState” pattern, the talk is more about understanding
  setState deeply

  React has popularized functional programming in JavaScr...'
---

Par Justice Mba

Mise à jour : J'ai donné une conférence de suivi sur ce sujet à React Rally. Alors que cet article parle davantage du modèle "functional setState", la conférence porte davantage sur la compréhension approfondie de setState.

React a popularisé la programmation fonctionnelle en JavaScript. Cela a conduit à l'adoption par de grands frameworks du modèle d'UI basé sur les composants que React utilise. Et maintenant, la fièvre fonctionnelle se répand dans l'écosystème du développement web en général.

Mais l'équipe React est loin de s'arrêter. Ils continuent de creuser plus profond, découvrant encore plus de pépites fonctionnelles cachées dans la bibliothèque légendaire.

Alors aujourd'hui, je vous révèle un nouvel or fonctionnel enterré dans React, le meilleur secret de React — **Functional setState !**

D'accord, je viens d'inventer ce nom… et ce n'est pas entièrement nouveau ou un secret. Non, pas exactement. Voyez-vous, c'est un modèle intégré à React, connu seulement par quelques développeurs qui ont vraiment creusé profondément. Et il n'avait jamais de nom. Mais maintenant, il en a un — **Functional setState !**

Selon les mots de [Dan Abramov](https://www.freecodecamp.org/news/functional-setstate-is-the-future-of-react-374f30401b6b/undefined) pour décrire ce modèle, **Functional setState** est un modèle où vous

> « Déclarez les changements d'état séparément des classes de composants. »

Hein ?

### D'accord… ce que vous savez déjà

React est une bibliothèque d'UI basée sur les composants. Un composant est essentiellement une fonction qui accepte certaines propriétés et retourne un élément d'UI.

```jsx
function User(props) {
  return <div>Un joli utilisateur</div>;
}

```

Un composant peut avoir besoin d'avoir et de gérer son état. Dans ce cas, vous écrivez généralement le composant sous forme de classe. Ensuite, son état vit dans la fonction `constructor` de la classe :

```jsx
class User {
  constructor() {
    this.state = { score: 0 };
  }
  render() {
    return <div>Cet utilisateur a marqué {this.state.score}</div>;
  }
}
```

Pour gérer l'état, React fournit une méthode spéciale appelée `setState()`. Vous l'utilisez comme ceci :

```jsx
class User {
  ...
  increaseScore() {
    this.setState({ score: this.state.score + 1 });
  }
  ...
}

```

Notez comment `setState()` fonctionne. Vous lui passez **un objet** contenant une ou plusieurs parties de l'état que vous souhaitez mettre à jour. En d'autres termes, l'objet que vous passez aurait des clés correspondant aux clés de l'état du composant, puis `setState()` met à jour ou _définit_ l'état en fusionnant l'objet avec l'état. Ainsi, "set-State".

### Ce que vous ne saviez probablement pas

Vous souvenez-vous de la façon dont nous avons dit que `setState()` fonctionne ? Eh bien, que diriez-vous si je vous disais que, au lieu de passer un objet, vous pourriez passer **une fonction** ?

Oui. `setState()` accepte également une fonction. La fonction accepte l'état _précédent_ et les props _courantes_ du composant qu'elle utilise pour calculer et retourner l'état suivant. Voyez cela ci-dessous :

```js
this.setState(function (state, props) {
  return { score: state.score - 1 };
});

```

Notez que `setState()` est une fonction, et nous lui passons une autre fonction (programmation fonctionnelle… **functional setState**). À première vue, cela peut sembler laid, trop d'étapes juste pour définir l'état. Pourquoi voudriez-vous jamais faire cela ?

### Pourquoi passer une fonction à `setState ?`

Le problème est que [les mises à jour d'état peuvent être asynchrones](https://facebook.github.io/react/docs/state-and-lifecycle.html#state-updates-may-be-asynchronous).

Pensez à [ce qui se passe lorsque `setState`](https://facebook.github.io/react/docs/reconciliation.html)`()` [est appelé](https://facebook.github.io/react/docs/reconciliation.html). React va d'abord fusionner l'objet que vous avez passé à `setState()` dans l'état actuel. Ensuite, il va commencer ce processus de _réconciliation_. Il va créer un nouvel arbre d'éléments React (une représentation objet de votre UI), comparer le nouvel arbre avec l'ancien arbre, déterminer ce qui a changé en fonction de l'objet que vous avez passé à `setState()`, puis enfin mettre à jour le DOM.

Ouf ! Tant de travail ! En fait, ceci est même un résumé trop simplifié. Mais faites confiance à React !

> React ne "définit" pas simplement l'état.

En raison de la quantité de travail impliquée, l'appel à `setState()` peut ne pas mettre à jour votre état _immédiatement_.

> React peut regrouper plusieurs appels à `setState()` en une seule mise à jour pour des raisons de performance.

Que veut dire React par là ?

Tout d'abord, "_plusieurs appels à `setState()`_" pourrait signifier appeler `setState()` à l'intérieur d'une seule fonction plus d'une fois, comme ceci :

```js
state = { score: 0 };
// plusieurs appels à setState()
function increaseScoreBy3() {
  this.setState({ score: this.state.score + 1 });
  this.setState({ score: this.state.score + 1 });
  this.setState({ score: this.state.score + 1 });
}

```

Maintenant, lorsque React rencontre "_plusieurs appels à `setState()`_", au lieu de faire ce "set-state" **trois fois de suite**, React évitera cette énorme quantité de travail que j'ai décrite ci-dessus et dira intelligemment : "Non ! Je ne vais pas gravir cette montagne trois fois, en transportant et en mettant à jour une partie de l'état à chaque voyage. Non, je préfère prendre un conteneur, emballer toutes ces parties ensemble, et faire cette mise à jour une seule fois." Et cela, mes amis, est le **batching** !

Rappelez-vous que ce que vous passez à `setState()` est un objet simple. Maintenant, supposons que chaque fois que React rencontre "_plusieurs appels à `setState()`_", il fait le batching en extrayant tous les objets passés à chaque appel `setState()`, les fusionne ensemble pour former un seul objet, puis utilise cet objet unique pour faire `setState()`.

En JavaScript, la fusion d'objets pourrait ressembler à ceci :

```js
const singleObject = Object.assign(
  {},
  objectFromSetState1,
  objectFromSetState2,
  objectFromSetState3
);

```

Ce modèle est connu sous le nom de **composition d'objets**.

En JavaScript, la façon dont la "fusion" ou la **composition** des objets fonctionne est : si les trois objets ont les mêmes clés, la valeur de la clé du _dernier objet_ passé à `Object.assign()` l'emporte. Par exemple :

```js
const me = { name: "Justice" },
  you = { name: "Votre nom" },
  we = Object.assign({}, me, you);
we.name === "Votre nom"; //true
console.log(we); // {name : "Votre nom"}
```

Parce que `you` est le dernier objet fusionné dans `we`, la valeur de `name` dans l'objet `you` — "Votre nom" — remplace la valeur de `name` dans l'objet `me`. Donc "Votre nom" est dans l'objet `we`… `you` gagnez ! :)

Ainsi, si vous appelez `setState()` avec un objet plusieurs fois — en passant un objet à chaque fois — React va **fusionner**. Ou en d'autres termes, il va **composer** un nouvel objet à partir des multiples objets que nous lui avons passés. Et si l'un des objets contient la même clé, la valeur de la clé du _dernier_ objet avec la même clé est stockée. N'est-ce pas ?

Cela signifie que, étant donné notre fonction `increaseScoreBy3` ci-dessus, le résultat final de la fonction sera simplement 1 au lieu de 3, parce que React n'a pas mis à jour l'état _immédiatement_ dans l'ordre où nous avons appelé `setState()`. Mais d'abord, React a composé tous les objets ensemble, ce qui donne ceci : `{score : this.state.score + 1}`, puis n'a fait "set-state" qu'une seule fois — avec le nouvel objet composé. Quelque chose comme ceci : `User.setState({score : this.state.score + 1}`.

Pour être super clair, passer un objet à `setState()` n'est pas le problème ici. Le vrai problème est de passer un objet à `setState()` lorsque vous voulez calculer l'état suivant à partir de l'état précédent. Donc arrêtez de faire cela. Ce n'est pas sûr !

> Parce que `_this.props_` et `_this.state_` peuvent être mis à jour de manière asynchrone, vous ne devriez pas vous fier à leurs valeurs pour calculer l'état suivant.

Voici un exemple de [Sophia Shoemaker](https://www.freecodecamp.org/news/functional-setstate-is-the-future-of-react-374f30401b6b/undefined) qui démontre ce problème. Jouez avec, et faites attention aux mauvaises et aux bonnes solutions dans cet exemple :

### Functional setState à la rescousse

Si vous n'avez pas passé de temps à jouer avec l'exemple ci-dessus, je vous recommande fortement de le faire, car cela vous aidera à saisir le concept central de cet article.

Pendant que vous jouiez avec l'exemple ci-dessus, vous avez sans doute vu que **functional setState** a résolu notre problème. Mais comment, exactement ?

Consultons l'Oprah de React — Dan.

Notez la réponse qu'il a donnée. Lorsque vous utilisez functional setState…

> Les mises à jour seront mises en file d'attente et exécutées plus tard dans l'ordre où elles ont été appelées.

Ainsi, lorsque React rencontre "_plusieurs appels à `functional setState()`_", au lieu de fusionner les objets ensemble (bien sûr, il n'y a pas d'objets à fusionner), React met en file d'attente les fonctions "dans l'ordre où elles ont été appelées".

Après cela, React continue à mettre à jour l'état en appelant chaque fonction dans la "file d'attente", en leur passant l'état _précédent_ — c'est-à-dire l'état tel qu'il était _avant_ le premier appel `setState()` fonctionnel (s'il s'agit du premier functional setState() en cours d'exécution) ou l'état avec la mise à jour la plus récente de l'appel `setState()` fonctionnel _précédent_ dans la file d'attente.

Encore une fois, je pense que voir un peu de code serait bien. Cette fois-ci, nous allons tout simuler. Sachez que ce n'est pas la vraie chose, mais c'est juste ici pour vous donner une _idée_ de ce que React fait.

De plus, pour le rendre moins verbeux, nous allons utiliser ES6. Vous pouvez toujours écrire la version ES5 plus tard si vous le souhaitez.

Tout d'abord, créons une classe de composant. Ensuite, à l'intérieur, nous allons créer une méthode `setState()` _fausse_. De plus, notre composant aurait une méthode `increaseScoreBy3()`, qui effectuera un multiple functional setState. Enfin, nous allons instancier la classe, comme React le ferait.

```js
class User {
  state = { score: 0 };
  // simulons setState
  setState(state, callback) {
    this.state = Object.assign({}, this.state, state);
    if (callback) callback();
  }
  // multiple functional setState call
  increaseScoreBy3() {
    this.setState((state) => ({ score: state.score + 1 })),
      this.setState((state) => ({ score: state.score + 1 })),
      this.setState((state) => ({ score: state.score + 1 }));
  }
}
const Justice = new User();

```

Notez que setState accepte également un deuxième paramètre optionnel — une fonction de rappel. Si elle est présente, React l'appelle après avoir mis à jour l'état.

Maintenant, lorsqu'un utilisateur déclenche `increaseScoreBy3()`, React met en file d'attente le multiple functional setState. Nous ne allons pas simuler cette logique ici, car notre focus est sur **ce qui rend functional setState sûr**. Mais vous pouvez imaginer le résultat de ce processus de "mise en file d'attente" comme un tableau de fonctions, comme ceci :

```js
const updateQueue = [
  (state) => ({ score: state.score + 1 }),
  (state) => ({ score: state.score + 1 }),
  (state) => ({ score: state.score + 1 }),
];

```

Enfin, simulons le processus de mise à jour :

```js
// mettre à jour l'état dans l'ordre
function updateState(component, updateQueue) {
  if (updateQueue.length === 1) {
    return component.setState(updateQueue[0](component.state));
  }
  return component.setState(updateQueue[0](component.state), () =>
    updateState(component, updateQueue.slice(1))
  );
}
updateState(Justice, updateQueue);

```

Vrai, ce code n'est pas si sexy. Je suis sûr que vous pourriez faire mieux. Mais le point clé ici est que chaque fois que React exécute les fonctions de votre **functional setState**, React met à jour votre état en lui passant une copie _fraîche_ de l'état mis à jour. Cela permet à **functional setState** de **définir l'état en fonction de l'état précédent**.

Ici, j'ai fait un bin avec le code complet. Jouez avec (peut-être le rendre plus sexy), juste pour mieux le comprendre.

[**FunctionalSetStateInAction**](http://jsbin.com/najewe/edit?js,console)  
[_Amusez-vous avec le code dans ce bin. Souvenez-vous ! nous simulons simplement React pour avoir une idée..._jsbin.com](http://jsbin.com/najewe/edit?js,console)

Jouez avec pour le comprendre pleinement. Lorsque vous reviendrez, nous allons voir ce qui rend functional setState vraiment précieux.

### Le meilleur secret de React

Jusqu'à présent, nous avons profondément exploré pourquoi il est sûr de faire plusieurs functional setStates dans React. Mais nous n'avons pas encore rempli la définition _complète_ de functional setState : "Déclarez les changements d'état séparément des classes de composants."

Au fil des ans, la logique de définition de l'état — c'est-à-dire les fonctions ou objets que nous passons à `setState()` — a toujours vécu _à l'intérieur_ des classes de composants. Cela est plus impératif que déclaratif.

Eh bien, aujourd'hui, je vous présente un trésor nouvellement découvert — le **meilleur secret de React** :

Merci à [Dan Abramov](https://www.freecodecamp.org/news/functional-setstate-is-the-future-of-react-374f30401b6b/undefined) !

C'est le pouvoir de functional setState. Déclarez votre logique de mise à jour d'état _à l'extérieur_ de votre classe de composant. Ensuite, appelez-la _à l'intérieur_ de votre classe de composant.

```jsx
// à l'extérieur de votre classe de composant
function increaseScore(state, props) {
  return { score: state.score + 1 };
}
class User {
  ...
  // à l'intérieur de votre classe de composant
  handleIncreaseScore() {
    this.setState(increaseScore);
  }
  ...
}

```

C'est déclaratif ! Votre classe de composant ne se soucie plus de _comment_ les mises à jour d'état se font. Elle déclare simplement le _type_ de mise à jour qu'elle désire.

Pour apprécier profondément cela, pensez à ces composants complexes qui auraient généralement de nombreuses parties d'état, mettant à jour chaque partie sur différentes actions. Et parfois, chaque fonction de mise à jour nécessiterait de nombreuses lignes de code. Toute cette logique vivrait _à l'intérieur_ de votre composant. Mais plus maintenant !

De plus, si vous êtes comme moi, j'aime garder chaque module aussi court que possible, mais maintenant vous avez l'impression que votre module devient trop long. Maintenant, vous avez le pouvoir d'extraire toute votre logique de changement d'état dans un module différent, puis de l'importer et de l'utiliser dans votre composant.

```jsx
import { increaseScore } from "../stateChanges";
class User {
  ...
  // à l'intérieur de votre classe de composant
  handleIncreaseScore() {
    this.setState(increaseScore);
  }
  ...
}

```

Maintenant, vous pouvez même réutiliser la fonction increaseScore dans un composant _différent_. Il suffit de l'importer.

Que pouvez-vous faire d'autre avec functional setState ?

Rendre les tests faciles !

Vous pouvez également passer des arguments **supplémentaires** pour calculer l'état suivant (celui-ci m'a soufflé l'esprit… #funfunFunction).

Attendez-vous à encore plus dans…

### [L'avenir de React](https://github.com/reactjs/react-future/tree/master/07%20-%20Returning%20State)

![Image](https://cdn-media-1.freecodecamp.org/images/0*uInBa_PPwz5aLo0j.jpg)

Depuis des années, l'équipe React expérimente la meilleure façon d'implémenter des [fonctions stateful](https://github.com/reactjs/react-future/blob/master/07%20-%20Returning%20State/01%20-%20Stateful%20Functions.js).

Functional setState semble être la bonne réponse à cela (probablement).

Hé, Dan ! Des derniers mots ?

Si vous êtes arrivé jusqu'ici, vous êtes probablement aussi excité que moi. Commencez à expérimenter avec ce **functional setState** dès aujourd'hui !

Si vous pensez que j'ai fait un bon travail, ou que d'autres méritent une chance de voir cela, cliquez sur le cœur vert ci-dessous pour aider à répandre une meilleure compréhension de React dans notre communauté.

Si vous avez une question qui n'a pas été répondue ou si vous n'êtes pas d'accord avec certains des points ici, n'hésitez pas à laisser des commentaires ici ou via [Twitter](https://twitter.com/Daajust).

Bon codage !