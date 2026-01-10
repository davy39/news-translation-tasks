---
title: Comment modéliser le comportement des applications Redux à l'aide de statecharts
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-05T17:40:33.000Z'
originalURL: https://freecodecamp.org/news/how-to-model-the-behavior-of-redux-apps-using-statecharts-5e342aad8f66
coverImage: https://cdn-media-1.freecodecamp.org/images/1*_vb_56pz-h3xAB1E5uooqA.jpeg
tags:
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: Redux
  slug: redux
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment modéliser le comportement des applications Redux à l'aide de statecharts
seo_desc: 'By Luca Matteis

  Our app, whether we like it or not, will be in a particular state at any given point
  in time. As we code User Interfaces (UI), we describe these states using data (a
  Redux store for instance), but we never give each state a formal nam...'
---

Par Luca Matteis

Notre application, que nous le voulions ou non, sera dans un état particulier à tout moment. Lorsque nous codons des interfaces utilisateur (UI), nous décrivons ces états à l'aide de données (un store Redux par exemple), mais nous ne donnons jamais à chaque état un nom formel.

Plus important encore, il existe des événements qui ne devraient pas être déclenchés dans un état particulier.

Il s'avère que cette idée de décrire les états et les événements qui font la transition d'un état à un autre est un concept bien étudié. Les [statecharts](http://www.inf.ed.ac.uk/teaching/courses/seoc/2005_2006/resources/statecharts.pdf), par exemple, fournissent un formalisme visuel pour décrire le comportement des applications réactives, telles que les interfaces utilisateur.

Dans cet article, je vais discuter de la manière dont le comportement des applications Redux peut être découplé des composants, conteneurs ou middlewares — endroits où nous gardons généralement une telle logique — et peut être contenu et décrit entièrement à l'aide d'un statechart. Cela permet des refactorisations et des visualisations beaucoup plus faciles du comportement de notre application.

### Redux et statecharts

[Redux](https://redux.js.org/) est assez simple. Nous avons un composant UI qui déclenche un événement. Nous envoyons ensuite (`dispatch`) une action lorsque cet événement se produit. Un reducer utilise cette action pour mettre à jour le store. Enfin, notre composant se nourrit directement des mises à jour du store :

```
// notre composant UI
function Counter({ currentCount, onPlusClick }) {
  return <>
    <button onClick={onPlusClick}>plus</button>
    {currentCount}
  <>
}
```

```
// connectons le composant à redux
connect(
  state => ({ currentCount: state.currentCount }),
  dispatch => ({
    onPlusClick: () => dispatch({ type: INCREMENT })
  })
)(Counter)
```

```
// gérer la mise à jour INCREMENT à l'aide d'un reducer
function currentCountReducer(state = 0, action) {
  switch(action.type) {
    case INCREMENT:
      return state + 1;
    default:
      return state;
  }
}
```

C'est à peu près tout ce qu'il y a à savoir sur Redux.

![Image](https://cdn-media-1.freecodecamp.org/images/j8cLfILp7OZ9z99gm6-JM6m5FGciCZD3bBJh)

Pour introduire les statecharts, au lieu de mapper directement notre événement à l'action de mise à jour, nous le mappons à une action générique qui ne met à jour aucune donnée (aucun reducer ne la gère) :

```
// actuellement, nous mappons notre événement à la mise à jour :
// onPlusClick -> INCREMENT
// au lieu de cela, nous envoyons un événement générique qui n'est pas une mise à jour :
// onPlusClick -> CLICKED_PLUS
// de cette manière, nous découplons notre conteneur de la connaissance
// de la mise à jour qui va se produire.
// le statechart se chargera de déclencher la bonne mise à jour.
```

```
connect(
  state => ({ currentCount: state.currentCount }),
  dispatch => ({
    onPlusClick: () => dispatch({ type: CLICKED_PLUS })
  })
)(Counter)
```

Aucun reducer ne gère `CLICKED_PLUS`, donc nous laissons plutôt un statechart le gérer :

```
const statechart = {
  initial: 'Init',
  states: {
    Init: {
      on: { CLICKED_PLUS: 'Increment' }
    },
    Increment: {
      onEntry: INCREMENT, // <- mise à jour lorsque nous entrons dans cet état
      on: { CLICKED_PLUS: 'Increment' }
    }
  }
}
```

Le statechart gérera les événements qu'il reçoit de manière similaire à un reducer, mais seulement s'il est dans un état qui permet à un tel événement de se produire. **Les événements dans ce contexte sont des actions Redux qui ne mettent pas à jour le store**.

Dans l'exemple mentionné ci-dessus, nous commençons par être dans l'état `Init`. Lorsque l'événement `CLICKED_PLUS` se produit, nous passons à l'état `Increment` qui a un champ `onEntry`. Cela fait que le statechart envoie une action `INCREMENT` — cette fois gérée par un reducer, qui met à jour le store.

Vous pourriez vous demander, pourquoi avons-nous découplé le conteneur de la connaissance de la mise à jour ? Nous l'avons fait pour que tout le comportement concernant le moment où la mise à jour doit se produire soit contenu dans la structure JSON du statechart. Ce qui signifie qu'il peut également être visualisé :

![Image](https://cdn-media-1.freecodecamp.org/images/f20MvpyzWylXFxR739RS4UVAxLVG1pKslHL8)

Cela peut conduire à des améliorations dans le comportement de notre application en changeant simplement la description JSON du statechart. Améliorons notre design en regroupant les deux transitions `CLICKED_PLUS` en une seule, en utilisant le concept de [états hiérarchiques](https://statecharts.github.io/glossary/compound-state.html) :

![Image](https://cdn-media-1.freecodecamp.org/images/0XUooK1P2XVwPZHIXAq0AdctW5wcBzCg6PMx)

Pour que cela se produise, nous n'avons dû changer que notre définition de statechart. Nos composants UI et reducers restent intacts.

```
{
  initial: 'Init',
  states: {
    Init: {
      on: { CLICKED_PLUS: 'Init.Increment' },
      states: {
        Increment: {
          onEntry: INCREMENT
        }
      }
    }
  }
}
```

### Effets secondaires asynchrones

Imaginons que lorsque l'on clique sur un `<FetchDataButton />`, nous voulons démarrer une requête HTTP. Voici comment nous le ferions actuellement dans Redux sans statecharts :

```
connect(
  null,
  dispatch => ({
    onFetchDataClick: () => dispatch({ type: FETCH_DATA_CLICKED })
  })
)(FetchDataButton)
```

Ensuite, nous aurions probablement un epic pour gérer une telle action. Ci-dessous, nous utilisons [redux-observable](https://redux-observable.js.org/), mais redux-saga ou redux-thunk peuvent également être utilisés :

```
function handleFetchDataClicked(action$, store) {
  return action$.ofType('FETCH_DATA_CLICKED')
    .mergeMap(action =>
      ajax('http://foo.bar')
        .mapTo({ type: 'FETCH_DATA_SUCCESS' })
        .takeUntil(action$.ofType('FETCH_DATA_CANCEL'))
    )
}
```

Même si nous avons découplé le conteneur de l'effet secondaire (le conteneur se contente de dire à l'epic « hey, le bouton de récupération de données a été cliqué »), nous avons toujours le problème que la requête HTTP est déclenchée quel que soit l'état dans lequel nous nous trouvons.

Et si nous sommes dans un état où `FETCH_DATA_CLICKED` ne devrait pas déclencher une requête HTTP ?

Ce cas peut facilement être géré par les statecharts. Lorsque `FETCH_DATA_CLICKED` se produit, nous passons à un état `FetchingData`. Ce n'est qu'en entrant dans cet état (`onEntry`) que l'action `FETCH_DATA_REQUEST` est envoyée :

```
{
  initial: 'Init',
  states: {
    Init: {
      on: {
        FETCH_DATA_CLICKED: 'FetchingData',
      },
      initial: 'NoData',
      states: {
        ShowData: {},
        Error: {},
        NoData: {}
      }
    },
    FetchingData: {
      on: {
        FETCH_DATA_SUCCESS: 'Init.ShowData',
        FETCH_DATA_FAILURE: 'Init.Error',
        CLICKED_CANCEL: 'Init.NoData',
      },
      onEntry: 'FETCH_DATA_REQUEST',
      onExit: 'FETCH_DATA_CANCEL',
    },
  }
}
```

Ensuite, nous modifions notre epic pour réagir en fonction de la nouvelle action `FETCH_DATA_REQUEST` ajoutée :

```
function handleFetchDataRequest(action$, store) {
  // gérer FETCH_DATA_REQUEST plutôt que FETCH_DATA_CLICKED
  return action$.ofType('FETCH_DATA_REQUEST')
    .mergeMap(action =>
      ajax('http://foo.bar')
        .mapTo({ type: 'FETCH_DATA_SUCCESS' })
        .takeUntil(action$.ofType('FETCH_DATA_CANCEL'))
    )
}
```

De cette manière, la requête ne sera déclenchée que lorsque nous serons dans l'état `FetchingData`.

Encore une fois, en faisant cela, nous avons poussé tout le comportement à l'intérieur de la structure JSON du statechart, rendant le refactoring facile et nous permettant de visualiser quelque chose qui serait autrement resté caché dans le code :

![Image](https://cdn-media-1.freecodecamp.org/images/VQAnmHywghmtUrY0I241qgxsOPqyowmMesY5)

Une propriété intéressante de cette conception particulière est que lorsque nous quittons l'état `FetchingData`, l'action `FETCH_DATA_CANCEL` est envoyée. Nous pouvons envoyer des actions non seulement lorsque nous entrons dans des états, mais aussi lorsque nous en sortons. Comme défini dans notre epic, cela provoquera l'abandon de la requête HTTP.

Il est important de noter que j'ai ajouté ce comportement particulier d'abandon de HTTP seulement après avoir regardé la visualisation résultante du statechart. En jetant simplement un coup d'œil au diagramme, il était évident que la requête HTTP aurait dû être nettoyée lors de la sortie de `FetchingData`. Cela n'aurait peut-être pas été si apparent sans une telle représentation visuelle.

À ce stade, nous pouvons rassembler l'intuition que les statecharts contrôlent nos mises à jour de store. Nous apprenons quels effets secondaires doivent se produire et quand ils doivent se produire, en fonction de l'état actuel dans lequel nous nous trouvons.

**L'idée principale ici est que nos reducers et epics réagiront toujours en fonction des actions de sortie de notre statechart, plutôt que de notre UI.**

En fait, un statechart peut être implémenté comme un émetteur d'événements avec état : vous lui dites ce qui s'est passé (déclencher un événement), et, en vous souvenant du dernier état dans lequel vous étiez, il vous dit quoi faire (actions).

![Image](https://cdn-media-1.freecodecamp.org/images/tTa5yNmBDRIpuTDoyuFprSRWvA1ZnJUngIH8)

### Problèmes que les statecharts aident à résoudre

En tant que développeurs UI, notre travail est de donner vie à des images statiques. Ce processus pose plusieurs problèmes :

* **Lorsque nous convertissons des images statiques en code, nous perdons la compréhension de haut niveau de notre application** — à mesure que notre application grandit, comprendre quelle section de code est responsable de chaque image devient de plus en plus difficile.
* **Toutes les questions ne peuvent pas être répondus à l'aide d'un ensemble d'images** — Que se passe-t-il lorsque l'utilisateur clique plusieurs fois sur le bouton ? Que se passe-t-il si l'utilisateur souhaite annuler la requête alors qu'elle est en cours ?
* **Les événements sont dispersés dans notre code et ont des effets imprévisibles** — Lorsque l'utilisateur clique sur un bouton, que se passe-t-il exactement ? Nous avons besoin d'une meilleure abstraction qui nous aide à comprendre les répercussions du déclenchement d'événements.
* **Beaucoup de variables `isFetching`, `isShowing`, `isDisabled`** — Nous devons garder une trace de tout ce qui change dans notre UI.

Les statecharts aident à résoudre ces problèmes en fournissant un **formalisme visuel** strict du comportement de notre application. Dessiner un statechart nous permet d'avoir une compréhension de haut niveau de notre application, ce qui nous permet de répondre à des questions à l'aide d'indices visuels.

![Image](https://cdn-media-1.freecodecamp.org/images/6WmId-UGRupVjl2O5T923hsdkBIvf7Af2KZj)

Tous les états d'une application sont explorés lors de ce processus et les événements sont explicitement étiquetés, ce qui nous permet de prédire ce qui va se passer après un événement donné.

De plus, un statechart peut être construit directement à partir des maquettes des designers, permettant aux non-ingénieurs de comprendre également ce qui se passe sans avoir à creuser dans le code réel.

### En savoir plus

En tant qu'exemple concret de cela, j'ai construit [redux-statecharts](https://github.com/lmatteis/redux-statecharts), un middleware Redux qui peut être utilisé comme montré dans les exemples précédents. Il utilise la bibliothèque [xstate](https://github.com/davidkpiano/xstate) — une fonction pure pour la transition d'un statechart.

Si vous souhaitez en savoir plus sur les statecharts, voici une excellente ressource : [https://statecharts.github.io/](https://statecharts.github.io/)

Consultez également ma présentation sur le sujet : [Les statecharts sont-ils le prochain grand paradigme UI ?](https://www.slideshare.net/lmatteis/are-statecharts-the-next-big-ui-paradigm)