---
title: Comment utiliser le Hook useReducer dans React
subtitle: ''
author: Timothy Olanrewaju
co_authors: []
series: null
date: '2024-05-03T17:48:03.000Z'
originalURL: https://freecodecamp.org/news/react-usereducer-hook
coverImage: https://www.freecodecamp.org/news/content/images/2024/05/Introduction-to-useReducer-Hook.png
tags:
- name: React
  slug: react
- name: react hooks
  slug: react-hooks
seo_title: Comment utiliser le Hook useReducer dans React
seo_desc: In this article, we'll take a deep look at the useReducer hook in React.
  It can look confusing, especially if you are coming across the hook for the first
  time. This article breaks down the useReducer hook concept into understandable bits
  with both c...
---

Dans cet article, nous allons examiner en profondeur le hook `useReducer` dans React. Il peut sembler déroutant, surtout si vous le découvrez pour la première fois. Cet article décompose le concept du hook `useReducer` en parties compréhensibles avec des exemples de code et des exemples concrets pour vous permettre de saisir son fonctionnement.

Si vous avez du mal à comprendre ce qu'est `useReducer` et comment il fonctionne, cet article est fait pour vous. Cependant, une bonne connaissance du fonctionnement des états est essentielle pour comprendre ce qui sera couvert dans cet article. Vous pouvez lire à propos des états React ici : [State Management In React](https://www.freecodecamp.org/news/react-state-management/#:~:text=State%20management%20is%20a%20crucial,placed%20in%20your%20applications). Vous pourrez ensuite nous rejoindre dans l'exploration du monde de `useReducer` une fois que vous aurez terminé. Si vous êtes déjà familier avec les états, c'est parti !

Avant d'aller plus loin, il est important de noter que les hooks `useState` et `useReducer` sont similaires à certains égards.

## Comment `useReducer` se compare-t-il au hook `useState` ?

* Ils impliquent tous deux une valeur d'état actuelle, et ont une fonction qui déclenche une mise à jour de l'état et une valeur d'état initiale passée en argument.
* `useReducer` est une alternative au hook `useState` pour gérer l'état dans les composants fonctionnels. Le hook `useReducer` est mieux adapté pour gérer une logique d'état complexe tandis que `useState` est idéal pour des changements d'état simples.

Lorsque la logique d'état devient trop compliquée ou lorsque vous devez gérer les changements d'état de manière plus prévisible et gérable, le hook `useReducer` est votre meilleur choix.

## Qu'est-ce que `useReducer` ?

`useReducer` est un hook dans React qui vous permet d'ajouter un `reducer` à votre composant. Il prend en arguments la fonction reducer et un `initialState`. `useReducer` retourne également un tableau contenant l'état actuel (`state`) et une fonction `dispatch`.

```js
const [state, dispatch] = useReducer(reducer, initialState);
```

Familiarisons-nous avec la signification des paramètres :

* `state` : représente la valeur actuelle et est défini à la valeur `initialState` lors du rendu initial.
* `dispatch` : est une fonction qui met à jour la valeur de l'état et déclenche toujours un nouveau rendu, tout comme la fonction de mise à jour dans `useState`.
* `reducer` : est une fonction qui contient toute la logique de la manière dont l'état est mis à jour. Elle prend l'état et l'action comme arguments et retourne le nouvel état.
* `initialState` : contient la valeur initiale et peut être de n'importe quel type.

## Plongeons dans `useReducer`

Ayant vu les parties qui composent un hook useReducer, il est temps de regarder de plus près comment il fonctionne.

Pour utiliser useReducer dans votre application React, appelez-le au niveau supérieur de votre composant.

```js
import { useReducer } from "react";
```

Nous pouvons maintenant utiliser le hook useReducer dans notre composant.

```js
export default function App() {
  const [state, dispatch] = useReducer(reducer, initialState);
  
  return(
  )
 }
```

Pour voir notre hook `useReducer` en action, nous allons construire une application de compteur très simple qui s'incrémente de 1 lorsqu'un bouton d'incrémentation est cliqué et se décrémente de 1 lorsqu'un bouton de décrémentation est cliqué.

Tout d'abord, examinons de plus près la fonction `reducer` importante. Cette fonction détermine comment l'état est mis à jour et contient toute la logique par laquelle le nouvel état sera calculé.

En gros, les reducers contiennent la logique qui est généralement placée à l'intérieur d'un gestionnaire d'événements lors de l'utilisation de `useState`. Cela facilite la lecture et le débogage lorsque vous n'obtenez pas les résultats souhaités. Un rapide coup d'œil à la fonction reducer peut vous éviter du stress.

La fonction reducer est toujours déclarée en dehors de votre composant et prend en arguments un état actuel (`state`) et une `action`.

```js
function reducer(state, action) {
}
```

Une `action` est un objet qui a généralement une propriété `type` qui identifie une action spécifique. Les actions décrivent ce qui se passe et contiennent les informations nécessaires pour que le reducer mette à jour l'état.

Des instructions conditionnelles sont utilisées pour vérifier les types d'action et effectuer une opération spécifiée qui retournera une nouvelle valeur d'état. Des instructions conditionnelles comme `if` et `switch` peuvent être utilisées dans les reducers.

### Fonction Dispatch

Il s'agit d'une fonction retournée par le hook `useReducer` et responsable de la mise à jour de l'état vers une nouvelle valeur. La fonction dispatch prend l'action comme seul argument.

Nous pouvons placer la fonction dispatch à l'intérieur d'une fonction de gestionnaire d'événements. N'oubliez pas que les actions viennent avec une propriété de type, nous devons donc la spécifier lorsque nous appelons la fonction dispatch. Pour notre application de compteur, nous avons deux gestionnaires d'événements qui augmentent et diminuent le compte.

```js
function handleIncrement() {
    dispatch({ type: "increment" });
  }
  
  function handleDecrement() {
    dispatch({ type: "decrement" });
  }
```

Maintenant, nous allons revenir à notre fonction reducer et utiliser la condition `switch` pour évaluer l'expression `action.type`.

```js
function reducer(state, action) {
  switch (action.type) {
    case "increment":
      return { ...state, count: state.count + 1 };
    case "decrement":
      return { ...state, count: state.count - 1 };
    default:
      return "Commande non reconnue";
  }
}
```

Dans le code ci-dessus,

* La fonction `reducer` prend à la fois l'état et l'action comme argument.
* Nous vérifions conditionnellement un cas spécifique de la chaîne d'expression `action.type`.
* Si vrai, une copie superficielle de l'état est prise par l'utilisation de l'opérateur de propagation et la valeur de compte dans l'état est évaluée.
* Un nouvel état est retourné après que l'évaluation a été terminée.
* Le `default` sert de solution de repli lorsqu'aucun cas correspondant n'est trouvé.

Toute la logique de notre application de compteur a été faite. Nous pouvons maintenant retourner notre JSX avec l'état de `count` à afficher sur l'interface utilisateur et les fonctions de gestionnaire passées au gestionnaire d'événements `onClick` pour les boutons.

```js
return (
    <>
      <h1>Compte:{state.count}</h1>
      <button onClick={handleIncrement}>Incrémenter</button>
      <button onClick={handleDecrement}>Décrémenter</button>
    </>
  );
```

Notre application de compteur est prête et l'état `count` sera mis à jour en conséquence lorsque les boutons seront cliqués.

## Que se passe-t-il derrière le capot ?

L'action de cliquer sur le bouton déclenche une fonction `dispatch` qui envoie une information de `type` à la fonction reducer. Le dispatching (cliquer sur le bouton) provoque un nouveau rendu du composant. La fonction reducer fait correspondre conditionnellement le cas avec le type de l'objet d'action et met à jour l'état en conséquence après que l'évaluation a eu lieu.

**NOTE** : Au moment du dispatch, la fonction reducer conserve toujours l'ancienne valeur. Cela signifie que la fonction dispatch met uniquement à jour la variable d'état pour le prochain rendu. Pour vérifier cela, nous pouvons logger les arguments `state` et `action` dans la console avant l'instruction switch :

```js
function reducer(state, action) {
  console.log(state, action);
  
  switch (action.type) {
    case "increment":
      return { ...state, count: state.count + 1 };
    case "decrement":
      return { ...state, count: state.count - 1 };
    default:
      return "Commande non reconnue";
  }
  }
```

Après avoir cliqué sur le bouton d'incrémentation pour augmenter le compte deux fois, voici ce qui est loggé dans la console :

![Image](https://www.freecodecamp.org/news/content/images/2024/05/Capture.PNG)
_state et type d'action loggés dans la console_

L'image ci-dessus montre que, lors du premier clic, il y a eu un type d'action `increment` et la valeur initiale de l'état était 0. Lors du deuxième clic, la valeur de l'état a été mise à jour à 1, et a été affichée comme l'état actuel du compte. J'espère que vous comprenez maintenant.

Assez de jargon de code, regardons un exemple concret de la fonction reducer.

## Exemple concret de Reducer

Imaginez un dispatch qui travaille pour une entreprise de commerce en ligne se rendant dans un entrepôt pour récupérer les marchandises/articles qu'ils distribueront plus tard aux personnes qui les ont commandés.

Le dispatch s'identifie et effectue une action de réclamation des marchandises destinées à l'expédition auprès du responsable de l'entrepôt. Le responsable se rend à une boîte contenant les commandes expédiées et localise les marchandises destinées à être remises au dispatch. Le responsable se connecte également au système d'inventaire et effectue les évaluations avant de remettre les marchandises au dispatch.

Ce scénario peut également être traduit comme suit :

* Le dispatch fait une demande de mise à jour ou déclenche un processus comme la fonction `dispatch`.
* Le dispatch effectue une action de 'réclamation de marchandises' comme l'action `dispatch` avec une propriété `type`.
* Le responsable de l'entrepôt effectue le tri et la mise à jour nécessaires, tout comme la fonction `reducer`.
* La boîte qui contient toutes les marchandises est mise à jour en fonction du nombre de marchandises libérées pour l'expédition. Cela agit comme la mise à jour de l'`state`.

J'espère que ce scénario concret rend l'ensemble du processus plus clair pour vous.

Jetez un coup d'œil au code complet une fois de plus et digérez le processus.

```js
import { useReducer } from "react";

function reducer(state, action) {
  console.log(state, action);
  switch (action.type) {
    case "increment":
      return { ...state, count: state.count + 1 };
    case "decrement":
      return { ...state, count: state.count - 1 };
    default:
      return "Commande non reconnue";
  }
}
const initialState = { count: 0 };
export default function App() {
  const [state, dispatch] = useReducer(reducer, initialState);

  function handleIncrement() {
    dispatch({ type: "increment" });
  }
  function handleDecrement() {
    dispatch({ type: "decrement" });
  }
  return (
    <>
      <h1>Compte:{state.count}</h1>
      <button onClick={handleIncrement}>Incrémenter</button>
      <button onClick={handleDecrement}>Décrémenter</button>
    </>
  );
}

```

## Avantages de l'utilisation du hook `useReducer`

* Aide à centraliser la logique d'état.
* Rend les transitions d'état prévisibles.
* Convient pour la gestion d'état complexe.
* Optimise les performances.

## Conclusion

Nous avons couvert ce qu'est le hook `useReducer`, comment il se compare à `useState` - similitudes et différences, le processus du reducer et les avantages de l'utilisation de `useReducer`.

Si vous avez trouvé cet article utile, vous pouvez [m'offrir un café](https://buymeacoffee.com/timothyolanrewaju).

Vous pouvez également me contacter sur [LinkedIn](http://linkedin.com/in/timothy-olanrewaju750).

À la prochaine !