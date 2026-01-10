---
title: Voici les concepts que vous devriez connaître dans React.js (après avoir appris
  les bases)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-12T17:49:59.000Z'
originalURL: https://freecodecamp.org/news/these-are-the-concepts-you-should-know-in-react-js-after-you-learn-the-basics-ee1d2f4b8030
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Wjs9dJlrtDyYtTYb073_Vg.jpeg
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
seo_title: Voici les concepts que vous devriez connaître dans React.js (après avoir
  appris les bases)
seo_desc: 'By Chris Chuck

  You’ve followed your first React.js tutorial and you’re feeling great. Now what?
  In the following article, I’m going to discuss 5 concepts that will bring your React
  skills and knowledge to the next level.

  If you’re completely new to R...'
---

Par Chris Chuck

Vous avez suivi votre premier tutoriel React.js et vous vous sentez bien. Maintenant quoi ? Dans l'article suivant, je vais discuter de 5 concepts qui feront passer vos compétences et connaissances en React au niveau supérieur.

Si vous êtes complètement nouveau dans React, prenez le temps de compléter [ce tutoriel](https://reactjs.org/tutorial/tutorial.html) et revenez après !

### 1. [Le Cycle de Vie des Composants](https://reactjs.org/docs/react-component.html#static-getderivedstatefromprops)

De loin le concept le plus important de cette liste est de comprendre le cycle de vie des composants. Le cycle de vie des composants est exactement ce à quoi il ressemble : il détaille la vie d'un composant. Comme nous, les composants naissent, font certaines choses pendant leur temps ici sur terre, et puis ils meurent ☹️

Mais contrairement à nous, les étapes de la vie d'un composant sont un peu différentes. Voici à quoi cela ressemble :

![Image](https://cdn-media-1.freecodecamp.org/images/1*U13Mlxz_ktcajaeJCyYkwg.png)
_Image de [ici !](http://projects.wojtekmaj.pl/react-lifecycle-methods-diagram/" rel="noopener" target="_blank" title=")_

Décomposons cette image. Chaque rectangle horizontal coloré représente une méthode de cycle de vie (sauf pour « React met à jour le DOM et les refs »). Les colonnes représentent différentes _étapes_ de la vie des composants.

Un composant ne peut être que dans une étape à la fois. Il commence par le montage et passe à la mise à jour. Il reste en mise à jour perpétuellement jusqu'à ce qu'il soit retiré du DOM virtuel. Ensuite, il passe à la phase de démontage et est retiré du DOM.

Les méthodes de cycle de vie nous permettent d'exécuter du code à des points spécifiques de la vie du composant ou en réponse aux changements dans la vie du composant.

Passons en revue chaque étape du composant et les méthodes associées.

#### **Montage**

Puisque les composants basés sur des classes sont des classes, d'où le nom, la première méthode qui s'exécute est la méthode `constructor`. Typiquement, le `constructor` est l'endroit où vous initialiseriez l'état du composant.

Ensuite, le composant exécute `getDerivedStateFromProps`. Je vais sauter cette méthode car elle a une utilisation limitée.

Nous arrivons maintenant à la méthode `render` qui retourne votre JSX. Maintenant React « monte » sur le DOM.

Enfin, la méthode `componentDidMount` s'exécute. C'est ici que vous feriez des appels asynchrones à des bases de données ou manipuleriez directement le DOM si nécessaire. Comme ça, notre composant est né.

#### Mise à jour

Cette phase est déclenchée chaque fois que l'état ou les props changent. Comme dans le montage, `getDerivedStateFromProps` est appelé (mais pas de `constructor` cette fois !).

Ensuite, `shouldComponentUpdate` s'exécute. Ici, vous pouvez comparer les anciens props/état avec le nouvel ensemble de props/état. Vous pouvez déterminer si votre composant doit se re-rendre ou non en retournant vrai ou faux. Cela peut rendre votre application web plus efficace en réduisant les re-rendus supplémentaires. Si `shouldComponentUpdate` retourne faux, ce cycle de mise à jour se termine.

Sinon, React se re-rend et `getSnapshotBeforeUpdate` s'exécute ensuite. Cette méthode a également une utilisation limitée. React exécute ensuite `componentDidUpdate`. Comme `componentDidMount`, vous pouvez l'utiliser pour faire des appels asynchrones ou manipuler le DOM.

#### Démontage

Notre composant a vécu une bonne vie, mais toutes les bonnes choses ont une fin. La phase de démontage est la dernière étape du cycle de vie du composant. Lorsque vous retirez un composant du DOM, React exécute `componentWillUnmount` juste avant qu'il ne soit retiré. Vous devriez utiliser cette méthode pour nettoyer toute connexion ouverte telle que les WebSockets ou les intervalles.

#### Autres Méthodes de Cycle de Vie

Avant de passer au sujet suivant, parlons brièvement de `forceUpdate` et `getDerivedStateFromError`.

`forceUpdate` est une méthode qui provoque directement un re-rendu. Bien qu'il puisse y avoir quelques cas d'utilisation pour celle-ci, elle doit généralement être évitée.

`getDerivedStateFromError`, en revanche, est une méthode de cycle de vie qui ne fait pas directement partie du cycle de vie du composant. En cas d'erreur dans un composant, `getDerivedStateFromError` s'exécute et vous pouvez mettre à jour l'état pour refléter qu'une erreur s'est produite. Utilisez cette méthode abondamment.

Le fragment de code [**CodePen**](https://codepen.io/chrischuck/pen/EdrBxW) suivant montre les étapes de la phase de montage :

![Image](https://cdn-media-1.freecodecamp.org/images/1*f6eAmkAEw-wFCNkkICOVXA.png)
_Méthodes de cycle de vie de montage dans l'ordre_

Comprendre le cycle de vie des composants et les méthodes de React vous permettra de maintenir un flux de données approprié et de gérer les événements dans votre application.

### 2. [Composants d'Ordre Supérieur](https://reactjs.org/docs/higher-order-components.html)

Vous avez peut-être déjà utilisé des composants d'ordre supérieur, ou HOC. La fonction `connect` de Redux, par exemple, est une fonction qui retourne un HOC. Mais qu'est-ce qu'un HOC exactement ?

D'après la documentation React :

> Un composant d'ordre supérieur est une fonction qui prend un composant et retourne un nouveau composant.

En revenant à la fonction connect de Redux, nous pouvons regarder le fragment de code suivant :

```
const hoc = connect(state => state)
const WrappedComponent = hoc(SomeComponent)
```

Lorsque nous appelons `connect`, nous obtenons un HOC que nous pouvons utiliser pour envelopper un composant. À partir de là, nous passons simplement notre composant au HOC et commençons à utiliser le composant que notre HOC retourne.

Ce que les HOC nous permettent de faire, c'est d'abstraire la logique partagée entre les composants dans un seul composant global.

Un bon cas d'utilisation pour un HOC est l'autorisation. Vous pourriez écrire votre code d'authentification dans chaque composant qui en a besoin. Cela gonflerait rapidement et inutilement votre code.

Voyons comment vous pourriez faire l'authentification pour les composants sans HOC :

En utilisant les HOC, vous pourriez faire quelque chose comme ceci :

Voici un fragment de code [**CodePen**](https://codepen.io/chrischuck/pen/yRwMeo) fonctionnel pour le code ci-dessus.

En regardant le code ci-dessus, vous pouvez voir que nous sommes capables de garder nos composants réguliers très simples et « stupides » tout en fournissant toujours une authentification pour eux. Le composant `AuthWrapper` élève toute la logique d'authentification dans un composant unificateur. Tout ce qu'il fait, c'est prendre une prop appelée `isLoggedIn` et retourne le `WrappedComponent` ou une balise de paragraphe en fonction de si cette prop est vraie ou fausse.

Comme vous pouvez le voir, les HOC sont extrêmement utiles car ils nous permettent de réutiliser du code et de supprimer le gonflement. Nous aurons plus de pratique avec ceux-ci bientôt !

### 3. [État de React et setState()](https://reactjs.org/docs/state-and-lifecycle.html)

La plupart d'entre vous ont probablement utilisé l'état de React, nous l'avons même utilisé dans notre exemple de HOC. Mais il est important de comprendre que lorsqu'il y a un changement d'état, React déclenchera un re-rendu sur ce composant (sauf si vous spécifiez dans `shouldComponentUpdate` de dire le contraire).

Maintenant, parlons de la façon dont nous changeons l'état. La seule façon dont vous devriez changer l'état est via la méthode `setState`. Cette méthode prend un objet et le fusionne dans l'état actuel. En plus de cela, il y a quelques choses que vous devriez également savoir à ce sujet.

Tout d'abord, `setState` est asynchrone. Cela signifie que l'état ne se mettra pas à jour exactement après que vous ayez appelé `setState` et cela peut conduire à un comportement aggravant que nous espérons maintenant pouvoir éviter !

![Image](https://cdn-media-1.freecodecamp.org/images/1*qle8858T8Amobp6-WCrLZA.png)
_comportement asynchrone de setState_

En regardant l'image ci-dessus, vous pouvez voir que nous appelons `setState` puis `console.log` l'état juste après. Notre nouvelle variable de compteur _devrait_ être 1, mais elle est en fait 0. Alors, que faire si nous voulons accéder au nouvel état après que `setState` ait réellement mis à jour l'état ?

Cela nous amène à la prochaine pièce de connaissance que nous devrions savoir sur `setState` et c'est qu'il peut prendre une fonction de rappel. Réparons notre code !

![Image](https://cdn-media-1.freecodecamp.org/images/1*typSaWY-BfT4fMUaAP_jJg.png)
_Ça marche !_

Super, ça marche, maintenant nous avons terminé, n'est-ce pas ? Pas exactement. Nous n'utilisons pas correctement `setState` dans ce cas. Au lieu de passer un objet à `setState`, nous allons lui donner une fonction. Ce modèle est typiquement utilisé lorsque vous utilisez l'état actuel pour définir le nouvel état, comme dans notre exemple ci-dessus. Si vous ne faites pas cela, n'hésitez pas à continuer à passer un objet à `setState`. Mettons à jour notre code à nouveau !

![Image](https://cdn-media-1.freecodecamp.org/images/1*jWrcTSN4rr3f1rEYNiFcxQ.png)
_Maintenant nous parlons._

Voici le [**CodePen**](https://codepen.io/chrischuck/pen/wYYxrd) pour le code `setState` ci-dessus.

Quel est l'intérêt de passer une fonction au lieu d'un objet ? Parce que `setState` est asynchrone, compter sur lui pour créer notre nouvelle valeur aura quelques pièges. Par exemple, au moment où `setState` s'exécute, un autre `setState` pourrait avoir muté l'état. Passer une fonction à `setState` nous donne deux avantages. Le premier est qu'il nous permet de prendre une copie statique de notre état qui ne changera jamais d'elle-même. Le second est qu'il mettra en file d'attente les appels `setState` pour qu'ils s'exécutent dans l'ordre.

Jetez un coup d'œil à l'exemple suivant où nous essayons d'incrémenter le compteur de 2 en utilisant deux appels `setState` consécutifs :

![Image](https://cdn-media-1.freecodecamp.org/images/1*iuNhuy16nNN8BeSWvdRqkg.png)
_Comportement asynchrone typique vu précédemment_

Ce qui précède est ce que nous avons vu plus tôt alors que nous avons la correction ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/1*UaRuXtcBpVGrHHNknBAKTw.png)
_La correction pour obtenir notre comportement attendu_

[**CodePen**](https://codepen.io/chrischuck/pen/GYemvM) pour le code ci-dessus.

Dans la première image, les deux fonctions `setState` utilisent directement `this.state.counter` et comme nous l'avons appris plus tôt, `this.state.counter` sera toujours zéro après le premier appel de `setState`. Ainsi, nous obtenons 1 au lieu de 2 parce que les deux fonctions `setState` définissent `counter` à 1.

Dans la deuxième image, nous passons une fonction à `setState` qui garantira que les deux fonctions `setState` s'exécutent dans l'ordre. En plus de cela, elle prend un instantané de l'état, plutôt que d'utiliser l'état actuel, non mis à jour. Maintenant, nous obtenons notre résultat attendu de 2.

Et c'est tout ce que vous devez savoir sur l'état de React !

### 4. [Contexte React](https://reactjs.org/docs/context.html)

Cela nous amène maintenant au contexte React qui est simplement un état global pour les composants.

L'API de contexte React vous permet de créer des objets de contexte globaux qui peuvent être donnés à n'importe quel composant que vous créez. Cela vous permet de partager des données sans avoir à passer des props à travers tout l'arbre DOM.

Alors, comment utilisons-nous le contexte ?

Tout d'abord, créez un objet de contexte :

`const ContextObject = React.createContext({ foo: "bar" })`

La documentation React décrit la définition du contexte dans un composant comme suit :

`MyClass.contextType = MyContext;`

Cependant, dans CodePen (React 16.4.2), cela n'a pas fonctionné. Au lieu de cela, nous allons utiliser un HOC pour consommer le contexte de manière similaire à ce que Dan Abramov [recommande](https://github.com/facebook/react/issues/12397#issuecomment-375501574).

Ce que nous faisons, c'est envelopper notre composant avec le composant `Context.Consumer` et passer le contexte en tant que prop.

Maintenant, nous pouvons écrire quelque chose comme ce qui suit :

Et nous aurons accès à `foo` à partir de notre objet de contexte dans les props.

Comment changeons-nous le contexte, pourriez-vous demander. Malheureusement, c'est un peu plus compliqué, mais nous pouvons utiliser un HOC à nouveau et cela pourrait ressembler à ceci :

Passons en revue cela. Tout d'abord, nous prenons l'état initial du contexte, l'objet que nous avons passé à `React.createContext()` et nous le définissons comme l'état de notre composant d'enveloppement. Ensuite, nous définissons les méthodes que nous allons utiliser pour changer notre état. Enfin, nous enveloppons notre composant dans le composant `Context.Provider`. Nous passons notre état et notre fonction à la prop de valeur. Maintenant, tous les enfants recevront ceux-ci dans le contexte lorsqu'ils seront enveloppés avec le composant `Context.Consumer`.

En mettant tout ensemble (HOC omis pour plus de brièveté) :

Maintenant, notre composant enfant a accès au contexte global. Il a la capacité de changer l'attribut `foo` dans l'état en `baz`.

Voici un lien vers le [**CodePen**](https://codepen.io/chrischuck/pen/jeJLZG?editors=0011) complet pour le code de contexte.

### 5. [Restez à jour avec React !](https://reactjs.org/blog/2018/10/23/react-v-16-6.html)

Ce dernier concept est probablement le plus facile à comprendre. Il s'agit simplement de suivre les dernières versions de React. React a apporté des changements sérieux récemment et il ne va continuer qu'à grandir et se développer.

Par exemple, dans React 16.3, certaines [méthodes de cycle de vie](https://reactjs.org/blog/2018/03/29/react-v-16-3.html#component-lifecycle-changes) ont été dépréciées, dans React 16.6 nous avons maintenant des [composants asynchrones](https://reactjs.org/docs/code-splitting.html#reactlazy), et dans la version 16.7 nous avons des [hooks](https://reactjs.org/docs/hooks-intro.html) qui visent à remplacer entièrement les composants de classe.

### Conclusion

Merci d'avoir lu ! J'espère que vous avez apprécié et appris beaucoup de choses sur React. Bien que j'espère que vous avez appris beaucoup simplement en lisant, je vous encourage à essayer toutes ces fonctionnalités/particularités par vous-même. Lire est une chose, mais la seule façon de le maîtriser est de le faire vous-même !

Enfin, continuez simplement à coder. Apprendre une nouvelle technologie peut sembler décourageant, mais avant que vous ne le sachiez, vous serez un expert en React.

Si vous avez des commentaires, des questions, ou pensez que j'ai manqué quelque chose, n'hésitez pas à les laisser ci-dessous.

_Merci encore d'avoir lu ! Veuillez partager, laissez un_ ? (_ou deux), _et bon codage._