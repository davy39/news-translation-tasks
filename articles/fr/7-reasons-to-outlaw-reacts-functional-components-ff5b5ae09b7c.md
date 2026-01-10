---
title: 7 raisons d'interdire les composants fonctionnels de React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-10-10T14:07:29.000Z'
originalURL: https://freecodecamp.org/news/7-reasons-to-outlaw-reacts-functional-components-ff5b5ae09b7c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*nywxB5PdmQq8zmB_TnMTbQ.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: React Native
  slug: react-native
- name: Web Development
  slug: web-development
seo_title: 7 raisons d'interdire les composants fonctionnels de React
seo_desc: 'By Cory House

  Are React’s Functional Components Worth The Cost?

  Update 5/31/19: React 16.8 added Hooks, which mean you can use functional components
  for nearly everything! ? Function components are the future of React. So bottom-line,
  use functional ...'
---

Par Cory House

**Les composants fonctionnels de React valent-ils le coût ?**

**Mise à jour 31/05/19** : React 16.8 a ajouté les [Hooks](https://reactjs.org/docs/hooks-intro.html), ce qui signifie que vous pouvez utiliser des composants fonctionnels pour presque tout ! ? Les composants fonctionnels sont l'avenir de React. Donc, en résumé, utilisez des composants fonctionnels pour les développements futurs. Cela dit, les compromis ci-dessous s'appliquent aux anciens codebases où les Hooks ne sont pas une option. Bon codage !

Je passe la semaine à conseiller une équipe à Seattle pour aider à [accélérer leur transition vers React](http://reactjsconsulting.com). Aujourd'hui, nous avons discuté des [8 décisions clés à prendre pour standardiser le développement React](https://medium.freecodecamp.org/8-key-react-component-decisions-cc965db11594).

J'ai partagé [9 raisons pour lesquelles je suis un fan des composants fonctionnels](https://hackernoon.com/react-stateless-functional-components-nine-wins-you-might-have-overlooked-997b0d933dbc). Une réponse m'a surpris :

> « Interdisons l'utilisation des composants fonctionnels. »

Woah, vraiment ? Nous avons discuté du problème en longueur. Voici pourquoi.

## 1. Tracas de conversion

Les composants fonctionnels ne supportent pas l'état, les refs, ou les méthodes de cycle de vie. Ils ne peuvent pas non plus étendre PureComponent. Parfois, vous créerez un composant fonctionnel seulement pour réaliser que vous avez besoin d'une de ces fonctionnalités réservées aux classes plus tard. Dans ces situations, il est fastidieux de convertir manuellement une fonction en classe.

**Édition** : Au lieu de convertir en classe, vous pouvez améliorer les composants fonctionnels existants avec des méthodes de cycle de vie, un état, et plus via [recompose](https://github.com/acdlite/recompose).

## 2. Diffs désordonnés

Une fois que vous avez terminé la conversion, le diff est bruyant. Même un changement trivial d'une ligne entraîne une révision de code multi-lignes.

Voici un exemple de conversion d'un composant fonctionnel en classe afin qu'il puisse être déclaré comme un PureComponent.

![Image](https://cdn-media-1.freecodecamp.org/images/kr8yw-al2gMvnamZWpuMG00mWGmIm21JDvEi)

Si ce composant avait été déclaré comme une classe dès le départ, l'intention réelle du commit aurait été cristalline — il aurait nécessité un changement de 4 caractères :

![Image](https://cdn-media-1.freecodecamp.org/images/BWwVp-yUaTzkyCFeeePwUz7hyic9wBl5k2nC)

La conversion obscurcit l'historique du composant en créant l'illusion que le composant a été largement réécrit alors qu'en fait vous avez peut-être fait un changement très trivial. La personne qui effectue la conversion sera « blâmée » pour avoir écrit de nombreuses lignes qu'elle a simplement modifiées pour des raisons de conversion.

## 3. Différences mineures de signal à bruit

Comparez une classe minimale à une fonction, et les différences sont mineures. Souvenez-vous, les constructeurs sont optionnels sans état.

![Image](https://cdn-media-1.freecodecamp.org/images/ulQNa8UZO1XBVhrV-uCOiWvSBfxx2r9DHVWf)
_Une classe sans props par défaut n'est que 3 lignes plus longue (en raison du render explicite et de la destructuration sur une ligne séparée). Sans destructuration, une classe n'est que 2 lignes plus longue._

**Correction** : Oups ! J'ai oublié que le style fonctionnel peut être une ligne avec une simple fonction fléchée :

```jsx
const Hello = ({greeting, firstName}) => <div>{greeting} {firstName}</div>
```

## 4. Incohérence

Les composants fonctionnels et les composants classe ont des apparences différentes. Cette incohérence peut ralentir les développeurs lorsqu'ils passent d'un style à l'autre.

* Dans les classes, vous dites **this.props**, dans les fonctions, vous dites **props**.
* Dans les classes, vous déclarez une fonction render. Dans les fonctions, vous ne le faites pas.
* Dans les classes, vous destructurez en haut de render. Dans les fonctions, vous destructurez dans la liste d'arguments de la fonction.
* Dans les classes, vous déclarez les props par défaut en dessous du composant (ou via les propriétés de classe si vous êtes prêt à utiliser une [fonctionnalité de stage-3](https://tc39.github.io/proposal-class-fields/)). Dans les fonctions, vous déclarez les props par défaut en utilisant les arguments par défaut.

Ces différences subtiles ajoutent de la friction pour les nouveaux développeurs, et le changement de contexte conduit également à des erreurs pour les développeurs expérimentés.

## 5. Les classes sont familières aux développeurs OO

Oui, les classes de JavaScript sont certainement différentes des classes Java et C#. Mais toute personne travaillant en OO-land sur le serveur est susceptible de trouver cette règle simple facile à comprendre :

« Un composant React est une classe qui étend React.Component. »

Ajouter une conversation nuancée sur la manière et le moment d'utiliser des fonctions simples ajoute de la confusion pour les développeurs OO qui sont déjà habitués à être obligés d'utiliser des classes pour tout. Maintenant, je ne dis pas que cet état d'esprit est sain — la communauté React favorise davantage un état d'esprit fonctionnel. Mais, il faut reconnaître que les composants fonctionnels créent une friction de modèle mental pour les développeurs OO.

## 6. Aucun avantage de performance, pour l'instant

Bien que l'équipe React ait fait allusion à la possibilité que les composants fonctionnels soient plus rapides ou plus efficaces à l'avenir, ce n'est pas encore le cas. On pourrait donc soutenir que les composants fonctionnels sont actuellement une optimisation prématurée.

Et puisque les composants fonctionnels nécessitent une conversion en classe pour implémenter les optimisations de performance d'aujourd'hui comme shouldComponentUpdate et PureComponent, ils sont en fait plus fastidieux à optimiser pour la performance aujourd'hui.

**Mise à jour** : Avec React 16.6+, vous pouvez déclarer des composants fonctionnels « purs » via [React.memo](https://reactjs.org/docs/react-api.html#reactmemo).

## 7. Encore une autre décision

Enfin, les développeurs JavaScript ont déjà un [nombre ridicule de décisions à prendre](https://medium.freecodecamp.org/you-need-a-javascript-starter-kit-ff12d90ed8c5). Interdire les composants fonctionnels élimine une décision : Toujours créer une classe.

# Résumé

[Je suis toujours un fan des composants fonctionnels](https://medium.freecodecamp.org/8-key-react-component-decisions-cc965db11594). Mais maintenant, je reconnais qu'ils ne sont pas nécessairement une évidence pour tout le monde. Donc, comme d'habitude, considérez les compromis. ?

Voyez-vous d'autres inconvénients ou avantages ? Faites-nous en part ci-dessous.

# Vous cherchez plus d'informations sur React ? ⚒️

J'ai écrit [plusieurs cours sur React et JavaScript](http://bit.ly/psauthorpageimmutablepost) sur Pluralsight ([essai gratuit](http://bit.ly/pstrialimmutablepost)).

![Image](https://cdn-media-1.freecodecamp.org/images/SuC9EgNC2ufSr9E2uhTHLfy1tMv-kego4GJd)

[Cory House](https://twitter.com/housecor) est l'auteur de [plusieurs cours sur JavaScript, React, le code propre, .NET, et plus encore sur Pluralsight](http://pluralsight.com/author/cory-house). Il est consultant principal chez [reactjsconsulting.com](http://www.reactjsconsulting.com), Architecte Logiciel chez VinSolutions, un Microsoft MVP, et forme des développeurs logiciels à l'international sur des pratiques logicielles comme le développement front-end et le code propre. Cory tweete sur JavaScript et le développement front-end sur Twitter en tant que [@housecor](http://www.twitter.com/housecor).