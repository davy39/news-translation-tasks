---
title: Une introduction au modèle de routage Redux-First
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-06-21T18:11:26.000Z'
originalURL: https://freecodecamp.org/news/an-introduction-to-the-redux-first-routing-model-98926ebf53cb
coverImage: https://cdn-media-1.freecodecamp.org/images/1*YjH6ffLqFDSht8owkh27Vg.png
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: react router
  slug: react-router
- name: Redux
  slug: redux
- name: Web Development
  slug: web-development
seo_title: Une introduction au modèle de routage Redux-First
seo_desc: 'By Michael Sargent

  A routing library is a key component of any complex, single-page application. If
  you develop web apps with React and Redux, you’ve probably used, or at least heard
  of React Router. It’s a well-known routing library for React, and a...'
---

Par Michael Sargent

Une bibliothèque de routage est un composant clé de toute application complexe à page unique. Si vous développez des applications web avec React et Redux, vous avez probablement utilisé, ou au moins entendu parler de [React Router](https://github.com/ReactTraining/react-router). C'est une bibliothèque de routage bien connue pour React, et une excellente solution pour de nombreux cas d'utilisation.

Mais React Router n'est pas la seule solution viable dans l'écosystème React/Redux. En fait, il existe de nombreuses solutions de routage construites [pour React](https://github.com/brillout/awesome-react-components#router) et [pour Redux](https://github.com/markerikson/redux-ecosystem-links/blob/master/routing.md), chacune avec différentes API, fonctionnalités et objectifs — et la liste ne fait que s'allonger. Il va sans dire que le routage côté client n'est pas près de disparaître, et il reste encore beaucoup d'espace pour la conception dans les bibliothèques de routage de demain.

Aujourd'hui, je veux attirer votre attention sur le sujet du routage dans Redux. Je vais présenter et défendre le **routage Redux-first** — un paradigme qui fait de Redux la _star_ du modèle de routage, et le fil conducteur parmi de nombreuses solutions de routage Redux. Je vais démontrer comment assembler l'API de base, indépendante du framework, en moins de 100 lignes de code, avant d'explorer les options pour une utilisation réelle avec React et d'autres frameworks front-end.

### Un peu d'histoire

![Image](https://cdn-media-1.freecodecamp.org/images/mp5i8J4GGt1XW0Df9y57Qf4Q61tHyxXLhxRu)

Dans le navigateur, le **location** (informations sur l'URL) et l'**historique de session** (une pile de locations visitées par l'onglet actuel du navigateur) sont stockés dans l'objet global `window`. Ils sont accessibles via :

* `window.location` ([Location API](https://developer.mozilla.org/en-US/docs/Web/API/Location))
* `window.history` ([History API](https://developer.mozilla.org/en-US/docs/Web/API/History)).

L'API History offre les **méthodes de navigation dans l'historique** suivantes, notables pour leur capacité à mettre à jour l'historique et la location du navigateur _sans nécessiter de rechargement de la page_ :

* `pushState(href)` — pousse une nouvelle location sur la pile d'historique
* `replaceState(href)` — écrase la location actuelle sur la pile
* `back()` — navigue vers la location précédente sur la pile
* `forward()` — navigue vers la location suivante sur la pile
* `go(index)` — navigue vers une location sur la pile, dans les deux sens.

Ensemble, les API History et Location permettent le paradigme de routage côté client moderne connu sous le nom de **routage pushState** — le premier protagoniste de notre histoire.

Maintenant, il est presque criminel de mentionner les API History et Location sans mentionner une bibliothèque **wrapper** moderne comme `[history](https://github.com/ReactTraining/history)`.

[**ReactTraining/history**](https://github.com/ReactTraining/history)  
[_Gérer l'historique de session avec JavaScript_github.com](https://github.com/ReactTraining/history)

`history` fournit une API simple mais puissante pour interagir avec l'historique du navigateur et la location, tout en couvrant les incohérences entre les différentes implémentations de navigateurs. Elle est utilisée comme dépendance pair ou interne dans de nombreuses bibliothèques de routage modernes, et je vais faire plusieurs références à celle-ci tout au long de cet article.

### Redux et le routage pushState

![Image](https://cdn-media-1.freecodecamp.org/images/xSdtvEGu7Q6eQPryNCLpBRJt2v4mLULCQ2B5)

Le deuxième protagoniste de notre histoire est **Redux**. Nous sommes en 2017, alors je vais vous épargner l'introduction et aller droit au but :

_En utilisant le routage pushState simple dans une application Redux, nous divisons l'état de l'application en deux domaines : l'historique du navigateur et le store Redux._

Voici à quoi cela ressemble avec React Router, qui [instancie et enveloppe](https://github.com/ReactTraining/react-router/blob/master/packages/react-router-dom/modules/BrowserRouter.js#L18-L21) `history` :

```
history → React Router ⇄                        vue                 Redux ⇆
```

Maintenant, nous savons que [toutes les données n'ont pas à résider dans le store](http://redux.js.org/docs/faq/OrganizingState.html#do-i-have-to-put-all-my-state-into-redux-should-i-ever-use-reacts-setstate). Par exemple, l'état local du composant est souvent un endroit approprié pour stocker des données spécifiques à un seul composant.

Mais les données de location ne sont pas triviales. C'est une partie dynamique et importante de l'état de l'application — le genre de données qui appartient au store. Les y stocker permet des luxes Redux comme le débogage par voyage dans le temps, et un accès facile depuis n'importe quel composant connecté au store.

**Alors, comment déplaçons-nous la location dans le store ?**

Il n'y a pas moyen de contourner le fait que le navigateur lit et stocke les informations d'historique et de location dans la `window`, mais ce que nous _pouvons_ faire, c'est garder une _copie_ des données de location dans le store, et la maintenir synchronisée avec le navigateur.

**N'est-ce pas ce que fait `[react-router-redux](https://github.com/reactjs/react-router-redux)` pour React Router ?**

Oui, mais seulement pour activer les capacités de voyage dans le temps des Redux DevTools. L'application dépend toujours des données de location détenues par React Router :

```
history → React Router ⇄                   ⇅    vue                 Redux ⇆
```

Utiliser `react-router-redux` pour lire les données de location depuis le store au lieu de React Router est [déconseillé](https://github.com/reactjs/react-router-redux#how-do-i-access-router-state-in-a-container-component) (en raison de sources de vérité potentiellement conflictuelles).

**Pouvons-nous faire mieux ?**

Pouvons-nous construire un modèle de routage alternatif — un qui est construit dès le départ pour bien fonctionner avec Redux, nous permettant de lire et de mettre à jour la location _à la manière Redux_ — avec `store.getState()` et `store.dispatch()` ?

Nous le pouvons absolument, et cela s'appelle le _routage Redux-first_.

### Routage Redux-First

![Image](https://cdn-media-1.freecodecamp.org/images/bdi9OKYROykNZgP1v4F-a0kFSvybq14wg8Ri)

Le routage Redux-first est une variation du routage pushState qui fait de Redux la star du modèle de routage.

**Une solution de routage Redux-first satisfait les critères suivants :**

* La location est stockée dans le store Redux.
* La location est modifiée en dispatchant des actions Redux.
* L'application lit les données de location uniquement depuis le store.
* Le store et l'historique du navigateur sont maintenus synchronisés en arrière-plan.

Voici une idée de base de ce à quoi cela ressemble :

```
history   ⇅ Redux → router → vue
```

**Attendez, n'y a-t-il pas encore deux sources de données de location ?**

Oui, mais si nous pouvons faire confiance à ce que l'historique du navigateur et le store Redux sont synchronisés, nous pouvons construire nos applications pour _ne lire les données de location que depuis le store_. Ensuite, du point de vue de l'application, il n'y a qu'une seule source de vérité — le store.

**Comment réalisons-nous le routage Redux-first ?**

Nous pouvons commencer par créer un modèle conceptuel, en fusionnant les éléments fondateurs des modèles de cycle de vie des données de routage côté client et de Redux.

### Revisiter le modèle de routage côté client

![Image](https://cdn-media-1.freecodecamp.org/images/5ZaWBXE1esnDQD1WVGLkTStNe0YGFi533CFW)

Le routage côté client est un processus en plusieurs étapes qui commence par la _navigation_ et se termine par le _rendu_ — le _routage_ lui-même n'est qu'une étape de ce processus ! Passons en revue les détails :

* **Navigation** — Tout commence par un changement de location. Il existe 2 types de navigation : _interne_ et _externe_. La navigation interne est accomplie depuis l'application (par exemple, via l'API History), tandis que la navigation externe se produit lorsque l'utilisateur interagit avec la barre de navigation du navigateur ou entre dans l'application depuis un site externe.
* **Répondre à la navigation** — Lorsque la location change, l'application répond en passant la nouvelle location au routeur. Les techniques de routage plus anciennes s'appuyaient sur le sondage de `window.location` pour accomplir cela, mais de nos jours, nous avons l'utilitaire pratique `[history.listen](https://github.com/ReactTraining/history#listening)`.
* **Routage** — Ensuite, la nouvelle location est associée à son contenu de page correspondant. Le code qui gère cette étape est appelé un _routeur_, et il prend généralement un paramètre d'entrée de routes et de pages correspondantes appelé une _configuration de route_.
* **Rendu** — Enfin, le contenu est rendu sur le client. Cette étape peut, bien sûr, être gérée par un framework/bibliothèque front-end comme React.

Notez que les bibliothèques de routage n'ont pas à gérer _chaque_ partie du modèle de routage.

Certaines bibliothèques, comme React Router et [Vue Router](https://github.com/vuejs/vue-router), le font — tandis que d'autres, comme [Universal Router](https://github.com/kriasoft/universal-router), ne s'occupent que d'un seul aspect (comme le _routage_), offrant ainsi de la flexibilité dans les autres aspects :

![Image](https://cdn-media-1.freecodecamp.org/images/QItDX8b-2ecVCPIro0kP-msPFq0uubaKn2VA)
_Les bibliothèques de routage peuvent avoir différentes portées de responsabilité. (Cliquez pour agrandir)_

### Revisiter le modèle de cycle de vie des données Redux

![Image](https://cdn-media-1.freecodecamp.org/images/CYoN5Bl8EfGhmh-6g2vOyRZodvosMkN34oX9)

Redux possède un modèle de flux de données/cycle de vie unidirectionnel qui ne nécessite probablement pas d'introduction — mais voici un bref aperçu pour faire bonne mesure :

* **Action** — Tout changement d'état commence par le dispatch d'une action Redux (un objet simple contenant un `type` et une charge utile optionnelle).
* **Middleware** — L'action passe à travers la chaîne de middlewares du store, où les actions peuvent être interceptées et un comportement supplémentaire peut être exécuté. Les middlewares sont couramment utilisés pour gérer les effets secondaires dans les applications Redux.
* **Reducer** — L'action atteint ensuite le reducer racine, qui calcule le prochain état du store comme une fonction pure de l'état précédent et de l'action reçue. Le reducer racine peut être composé de reducers individuels qui gèrent chacun une partie de l'état du store.
* **Nouvel état** — Le store sauvegarde le nouvel état retourné par le reducer, et notifie ses [abonnés](http://redux.js.org/docs/api/Store.html#subscribe) du changement (dans React, via `[connect](https://github.com/reactjs/react-redux/blob/master/docs/api.md#connectmapstatetoprops-mapdispatchtoprops-mergeprops-options)`).
* **Rendu** — Enfin, la vue connectée au store peut se re-rendre conformément au nouvel état.

### Construire un modèle de routage Redux-First

![Image](https://cdn-media-1.freecodecamp.org/images/4ZlAWoprj2NEkTPINS0xRNFBHROGxcbL8Jzs)

La nature unidirectionnelle des modèles de cycle de vie des données de routage côté client et de Redux se prêtent bien à un modèle fusionné qui satisfait les critères que nous avons établis pour le routage Redux-first.

Dans ce modèle, le routeur est abonné au store, la navigation est accomplie via des actions Redux, et les mises à jour de l'historique du navigateur sont gérées par un middleware personnalisé. Examinons les détails de ce modèle :

* **Navigation interne via des actions Redux** — Au lieu d'utiliser l'API History directement, la navigation interne est réalisée en dispatchant l'une des 5 _actions de navigation_ qui reflètent les méthodes de navigation de l'historique.
* **Mise à jour de l'historique du navigateur via le middleware** — Un middleware est utilisé pour intercepter les actions de navigation et gérer l'effet secondaire de la mise à jour de l'historique du navigateur. Comme la nouvelle location n'est pas nécessairement ou facilement connue sans d'abord consulter l'historique du navigateur (par exemple, dans le cas d'une action `go`), les actions de navigation sont empêchées d'atteindre le reducer.
* **Répondre à la navigation** — Le flux d'exécution se poursuit avec un écouteur `history` qui répond à la navigation (à la fois depuis le middleware _et_ la navigation externe) en dispatchant une _deuxième action_ qui _contient_ la nouvelle location.
* **Reducer de location** — L'action dispatchée par l'écouteur atteint ensuite le reducer de location, qui ajoute la location au store. Le reducer de location détermine également la _forme_ de l'état de la location.
* **Routage connecté** — Le routeur connecté au store peut alors déterminer de manière réactive le nouveau contenu de la page lorsqu'il est notifié d'un changement de location dans le store.
* **Rendu** — Enfin, la page peut être re-rendue avec le nouveau contenu.

Notez que ce n'est pas la _seule_ façon d'accomplir le routage Redux-first — certaines [variations](https://github.com/mksarge/redux-first-routing#credits) présentent l'utilisation d'un enhancer de store et/ou une logique supplémentaire dans le middleware — mais c'est un modèle simple qui couvre toutes les bases.

### Une implémentation de base

![Image](https://cdn-media-1.freecodecamp.org/images/w9oWkwA26S9gqvwWmSqSUtWWvaRs1opbw10U)

En suivant le modèle que nous venons d'examiner, implémentons l'API de base — les actions, le middleware, l'écouteur et le reducer.

Nous utiliserons le package `history` comme dépendance interne, et construirons la solution de manière incrémentielle. Si vous préférez suivre avec le résultat final, vous pouvez le consulter [ici](https://gist.github.com/mksarge/d02e8d14a5496dc98d4dde60dbebbf3c).

#### Actions

Nous commencerons par définir les 5 actions de navigation qui reflètent les méthodes de navigation de l'historique :

```
// constants.js
export const PUSH = 'ROUTER/PUSH';
export const REPLACE = 'ROUTER/REPLACE';
export const GO = 'ROUTER/GO';
export const GO_BACK = 'ROUTER/GO_BACK';
export const GO_FORWARD = 'ROUTER/GO_FORWARD';
```

```
// actions.js
export const push = (href) => ({
  type: PUSH,
  payload: href,
});
```

```
export const replace = (href) => ({
  type: REPLACE,
  payload: href,
});
```

```
export const go = (index) => ({
  type: GO,
  payload: index,
});
```

```
export const goBack = () => ({
  type: GO_BACK,
});
```

```
export const goForward = () => ({
  type: GO_FORWARD,
});
```

#### Middleware

Ensuite, définissons le middleware. Il doit intercepter les actions de navigation, appeler les méthodes de navigation `history` correspondantes, puis empêcher l'action d'atteindre le reducer — mais laisser toutes les autres actions intactes :

```
// middleware.js
export const routerMiddleware = (history) => () => (next) => (action) => {
  switch (action.type) {
    case PUSH:
      history.push(action.payload);
      break;
    case REPLACE:
      history.replace(action.payload);
      break;
    case GO:
      history.go(action.payload);
      break;
    case GO_BACK:
      history.goBack();
      break;
    case GO_FORWARD:
      history.goForward();
      break;
    default:
      return next(action);
  }
};
```

Si vous n'avez pas eu l'occasion d'écrire ou d'examiner les internes d'un middleware Redux auparavant, consultez [cette introduction](http://redux.js.org/docs/advanced/Middleware.html).

#### Écouteur d'historique

Ensuite, nous aurons besoin d'un écouteur `history` qui répond à la navigation en dispatchant une _nouvelle_ action contenant les nouvelles informations de location.

Tout d'abord, ajoutons le nouveau type et créateur d'action. Les parties intéressantes de la location sont le `pathname`, `search`, et `hash` — c'est donc ce que nous inclurons dans la charge utile :

```
// constants.js
export const LOCATION_CHANGE = 'ROUTER/LOCATION_CHANGE';
```

```
// actions.js
export const locationChange = ({ pathname, search, hash }) => ({
  type: LOCATION_CHANGE,
  payload: {
    pathname,
    search,
    hash,
  },
});
```

Ensuite, écrivons la fonction d'écouteur :

```
// listener.js
export function startListener(history, store) {
  history.listen((location) => {
    store.dispatch(locationChange({
      pathname: location.pathname,
      search: location.search,
      hash: location.hash,
    }));
  });
}
```

Nous ajouterons une petite addition — un dispatch initial `locationChange`, pour tenir compte de l'entrée initiale dans l'application (qui n'est pas captée par l'écouteur d'historique) :

```
// listener.js
export function startListener(history, store) {
  store.dispatch(locationChange({
    pathname: history.location.pathname,
    search: history.location.search,
    hash: history.location.hash,
  }));

  history.listen((location) => {
    store.dispatch(locationChange({
      pathname: location.pathname,
      search: location.search,
      hash: location.hash,
    }));
  });
}
```

#### Reducer

Ensuite, définissons le reducer de location. Nous utiliserons une forme d'état simple, et ferons un travail minimal dans le reducer :

```
// reducer.js
const initialState = {
  pathname: '/',
  search: '',
  hash: '',
};
```

```
export const routerReducer = (state = initialState, action) => {
  switch (action.type) {
    case LOCATION_CHANGE:
      return {
        ...state,
        ...action.payload,
      };
    default:
      return state;
  }
};
```

#### Code de l'application

Enfin, connectons notre API au code de l'application :

```
// index.js
import { combineReducers, applyMiddleware, createStore } from 'redux'
import { createBrowserHistory } from 'history'
import { routerReducer } from './reducer'
import { routerMiddleware } from './middleware'
import { startListener } from './listener'
import { push } from './actions'
```

```
// Créer l'objet history
const history = createBrowserHistory()
```

```
// Construire le reducer racine
const rootReducer = combineReducers({
  // ...otherReducers,
  router: routerReducer,
})
  // Construire le middleware
const middleware = routerMiddleware(history)
```

```
// Créer le store
const store = createStore(rootReducer, {}, applyMiddleware(middleware))
```

```
// Démarrer l'écouteur d'historique
startListener(history, store)
```

```
// Maintenant vous pouvez lire les données de location depuis le store !
let currentLocation = store.getState().router.pathname
```

```
// Vous pouvez également vous abonner aux changements de location !
let unsubscribe = store.subscribe(() => {
  let previousLocation = currentLocation
  currentLocation = store.getState().router.pathname
```

```
  if (previousLocation !== currentLocation) {
    // Vous pouvez rendre votre application de manière réactive ici !
  }
})
```

```
// Et vous pouvez dispatcher des actions de navigation depuis n'importe où !
store.dispatch(push('/about'))
```

Et c'est tout ! En utilisant notre petite API (moins de 100 lignes de code), nous avons satisfait tous les critères pour le routage Redux-first :

* La location est stockée dans le store Redux. ✓
* La location est modifiée en dispatchant des actions Redux. ✓
* L'application lit les données de location uniquement depuis le store. ✓
* Le store et l'historique du navigateur sont maintenus synchronisés en arrière-plan. ✓

[Voir tous les fichiers ensemble ici](https://gist.github.com/mksarge/d02e8d14a5496dc98d4dde60dbebbf3c) — n'hésitez pas à les importer dans votre projet, ou à les utiliser comme point de départ pour développer votre propre implémentation.

#### Le package redux-first-routing

J'ai également rassemblé l'API dans le package `[redux-first-routing](https://github.com/mksarge/redux-first-routing)`, que vous pouvez `npm install` et utiliser de la même manière.

[**mksarge/redux-first-routing**](https://github.com/mksarge/redux-first-routing)  
[_redux-first-routing — Une base minimale et indépendante du framework pour accomplir le routage Redux-first._github.com](https://github.com/mksarge/redux-first-routing)

Il inclut une implémentation similaire à celle que nous avons construite ici, mais avec l'ajout notable de l'analyse des requêtes via le package `[query-string](https://github.com/sindresorhus/query-string)`.

**Attendez — et le composant de routage réel ?**

Vous avez peut-être remarqué que `redux-first-routing` ne s'occupe que de l'aspect navigationnel du modèle de routage :

![Image](https://cdn-media-1.freecodecamp.org/images/0cx7C4aMZSVeA2h1mFAN6QUHtGe5Cq0FxiqG)

En découplant l'aspect navigationnel des autres aspects de notre modèle de routage, nous avons gagné en flexibilité — `redux-first-routing` est à la fois _agnostique du routeur_ et _agnostique du framework_.

Vous pouvez donc l'associer à une bibliothèque comme Universal Router pour créer une solution de routage Redux-first complète pour n'importe quel framework front-end :

![Image](https://cdn-media-1.freecodecamp.org/images/VKvhkkYLIv9d2J5UmrGfUybbPXFVe0ro-TMI)
_[Cliquez ici pour commencer avec redux-first-routing + universal-router](https://github.com/kriasoft/universal-router/issues/99" rel="noopener" target="_blank" title=")._

Ou, vous pourriez construire des liaisons opinionnées pour votre framework de choix — et c'est ce que nous ferons pour React dans la prochaine et dernière section de cet article.

### Utilisation avec React

![Image](https://cdn-media-1.freecodecamp.org/images/rjr7N0EYizdefCuxjk83Ladmo9UZv71yrRCK)

Terminons notre exploration en regardant comment nous pourrions construire des composants connectés au store pour la navigation et le routage déclaratifs dans React.

#### Navigation déclarative

Pour la navigation, nous pouvons utiliser un composant `<Link/>` connecté au store similaire à celui de [React Router](https://github.com/ReactTraining/react-router/blob/master/packages/react-router-dom/modules/Link.js) et d'autres solutions de routage React.

Il remplace simplement le comportement par défaut de l'élément d'ancrage `<a/>` et dispatch une action push lorsqu'il est cliqué :

```
// Link.js
import React from 'react';
import { connect } from 'react-redux';
import { push as pushAction, replace as replaceAction } from './actions';
```

```
const Link = (props) => {
  const { to, replace, children, dispatch, ...other } = props;
```

```
  const handleClick = (event) => {
    // Ignorer tout clic autre qu'un clic gauche
    if ((event.button && event.button !== 0)
      || event.metaKey
      || event.altKey
      || event.ctrlKey
      || event.shiftKey
      || event.defaultPrevented === true) {
      return;
    }
    // Empêcher le comportement par défaut (rechargement de la page, etc.)
    event.preventDefault();
```

```
    // Dispatch l'action de navigation appropriée
    if (replace) {
      dispatch(replaceAction(to));
    } else {
      dispatch(pushAction(to));
    }
  };
```

```
  return (
    <a href={to} onClick={handleClick} {...other}>
      {children}
    </a>);
};
```

```
export default connect()(Link);
```

Vous pouvez trouver une implémentation plus complète [ici](https://gist.github.com/mksarge/a22c809cdd5698aeb4f57c009a3a4933).

#### Routage déclaratif

Bien qu'il n'y ait pas grand-chose à un composant de navigation, il existe d'innombrables façons de concevoir un composant de routage — ce qui en fait la partie la plus intéressante de toute solution de routage.

**Qu'est-ce qu'un routeur, après tout ?**

Vous pouvez généralement voir un routeur comme une fonction ou une boîte noire avec deux entrées et une sortie :

```
configuration de route ⇄                      contenu correspondant
location actuelle  ⇅
```

Bien que le routage et le rendu ultérieur puissent se produire en étapes séparées, React facilite et rend intuitif le fait de les regrouper en une API de routage déclarative. Examinons deux stratégies pour y parvenir.

**Stratégie 1 : Un composant monolithique `<Router/>`**

Nous pouvons utiliser un composant monolithique `<Router/>` connecté au store qui :

* accepte un objet de configuration de route via les props
* lit les données de location depuis le store Redux
* calcule le nouveau contenu chaque fois que la location change
* rend/re-rend le contenu selon le cas.

La configuration de route peut être un objet JavaScript simple qui contient tous les chemins et pages correspondants (une configuration de route _centralisée_).

Voici à quoi cela pourrait ressembler :

```
const routes = [
  {
    path: '/',
    page: './pages/Home',
  },
  {
    path: '/about',
    page: './pages/About',
  },
  {
    path: '*',
    page: './pages/Error',
  },
]
```

```
React.render(
  <Provider store={store}>
    <Router routes={routes}>
  </Provider>,
  document.getElementById('app'))
```

Assez simple, n'est-ce pas ? Pas besoin de routes JSX imbriquées — juste un seul objet de configuration de route, et un seul composant routeur.

Si cette stratégie vous plaît, consultez mon implémentation plus complète dans la bibliothèque `[redux-json-router](https://github.com/mksarge/redux-json-router)`. Elle enveloppe `redux-first-routing` et fournit des liaisons React pour la navigation et le routage déclaratifs en utilisant les stratégies que nous avons examinées jusqu'à présent.

[**mksarge/redux-json-router**](https://github.com/mksarge/redux-json-router)  
[_redux-json-router - Routage déclaratif et Redux-first pour les applications navigateur React/Redux._github.com](https://github.com/mksarge/redux-json-router)

**Stratégie 2 : Composants `<Route/>` composables**

Bien qu'un composant monolithique puisse être un moyen _simple_ d'atteindre le routage déclaratif dans React, ce n'est définitivement pas le _seul_ moyen.

La nature composable de React permet une autre possibilité intéressante : utiliser JSX pour définir des routes de manière _décentralisée_. Bien sûr, l'exemple principal est l'API `<Route/>` de React Router :

```
React.render(
  <BrowserRouter>
    <Route path='/' component={Home}/>
    <Route path='/about component={About}/>
    ...
  </BrowserRouter>
```

[D'autres bibliothèques de routage](https://github.com/FormidableLabs/redux-little-router#fragment) explorent également cette idée. Bien que je n'aie pas eu l'occasion de le faire, je ne vois aucune raison pour laquelle une API similaire ne pourrait pas être implémentée sur le package `redux-first-routing`.

Au lieu de s'appuyer sur les données de location fournies par `<BrowserRouter/>`, le composant `<Route/>` pourrait simplement se connecter au store :

```
React.render(
  <Provider store={store}>
    <Route path='/' component={Home}/>
    <Route path='/about component={About}/>
    ...
  </Provider>
```

Si c'est quelque chose qui vous intéresse à construire ou à utiliser, faites-le moi savoir dans les commentaires ! Pour en savoir plus sur les différentes stratégies de configuration de route, consultez [cette](https://reacttraining.com/react-router/web/guides/philosophy) introduction sur le site web de React Router.

### Conclusion

J'espère que cette exploration a aidé à approfondir vos connaissances sur le routage côté client et vous a montré à quel point il est simple de l'accomplir à la manière Redux.

Si vous cherchez une solution de routage Redux complète, vous pouvez utiliser le package `[redux-first-routing](https://github.com/mksarge/redux-first-routing)` avec un routeur compatible listé dans le readme. Et si vous vous retrouvez à devoir développer une solution sur mesure, j'espère que cet article vous a donné un bon point de départ pour le faire.

Si vous souhaitez en savoir plus sur le routage côté client dans React et Redux, consultez les articles suivants — ils ont été instrumentaux pour m'aider à mieux comprendre les sujets que j'ai couverts ici :

* [**Laissez l'URL parler**](https://formidable.com/blog/2016/07/11/let-the-url-do-the-talking-part-1-the-pain-of-react-router-in-redux/) par Tyler Thompson
* [**Vous n'avez peut-être pas besoin de React Router**](https://medium.freecodecamp.com/you-might-not-need-react-router-38673620f3d) par Konstantin Tarkus
* [**Ai-je même besoin d'une bibliothèque de routage ?**](http://jamesknelson.com/even-need-routing-library/) par James K. Nelson
* et d'innombrables discussions informatives dans les [problèmes de `react-router-redux`](https://github.com/reactjs/react-router-redux).

Le routage côté client est un espace avec des possibilités de conception infinies, et je suis sûr que certains d'entre vous ont joué avec des idées similaires à celles que j'ai partagées ici. Si vous souhaitez poursuivre la conversation, je serai ravi de vous connecter dans les commentaires ou via [Twitter](https://twitter.com/michaelksarge). Merci d'avoir lu !

_Édition du 22/06/17 : Consultez également [cet article](https://medium.com/faceyspacey/pre-release-redux-first-router-a-step-beyond-redux-little-router-cd2716576aea) sur `redux-first-router`, un projet séparé qui utilise des types d'actions intelligents pour atteindre des capacités de routage puissantes._