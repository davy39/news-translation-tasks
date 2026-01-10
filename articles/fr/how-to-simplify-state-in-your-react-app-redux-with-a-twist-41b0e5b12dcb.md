---
title: Comment simplifier l'état dans votre application React — Redux avec une touche
  spéciale
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-05T21:46:48.000Z'
originalURL: https://freecodecamp.org/news/how-to-simplify-state-in-your-react-app-redux-with-a-twist-41b0e5b12dcb
coverImage: https://cdn-media-1.freecodecamp.org/images/1*SdI7uKKyAnA3i6jhyn5oyw.png
tags:
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: Redux
  slug: redux
- name: 'tech '
  slug: tech
seo_title: Comment simplifier l'état dans votre application React — Redux avec une
  touche spéciale
seo_desc: 'By Arnel Enero

  New, much easier syntax and semantics for good old Redux

  The words “simple” and “Redux” rarely appear together in the same sentence. And
  yet, much of the React community has come to embrace Redux as one of the best solutions
  for implem...'
---

Par Arnel Enero

#### Nouvelle syntaxe et sémantique, bien plus simples, pour le bon vieux Redux

Les mots « simple » et « Redux » apparaissent rarement ensemble dans la même phrase. Pourtant, une grande partie de la communauté React a adopté Redux comme l'une des meilleures solutions pour implémenter l'état de l'application.

Il existe désormais un moyen d'utiliser Redux même si vous n'écrivez pas une seule ligne de code boilerplate Redux. Vous n'avez même pas besoin de connaître ou d'apprendre Redux. Tant que vous êtes convaincu que Redux est le meilleur choix pour les besoins d'état de votre application, vous voudrez lire ceci.

Dans cet article, nous aborderons les sujets suivants :

* Gestion des changements d'état simples de l'application
* Travail avec des opérations asynchrones (par exemple, récupération de données)
* Fractionnement de code et état d'application chargé de manière paresseuse

### La bibliothèque Reactor

J'ai initialement écrit la bibliothèque Reactor pour minimiser le code boilerplate nécessaire dans mes projets personnels utilisant React. L'une de ses fonctionnalités est la gestion d'état d'application ultra-simple que je vais partager avec vous ici.

J'ai depuis décidé de rendre la bibliothèque disponible à tous ceux qui cherchent à simplifier leur code React/Redux. N'hésitez pas à l'utiliser ; elle est à vous autant qu'à moi.

Pour installer :

```
npm install @reactorlib/core
```

### Les 3 choses clés

Pour écrire notre gestion d'état d'application en utilisant la bibliothèque Reactor, il y a 3 choses clés que nous devons connaître :

* **Store** : C'est l'endroit unique où l'ensemble de l'état de notre application est conservé.
* **Entités** : Ce sont des morceaux de l'état de l'application, chacun représentant une zone spécifique de préoccupation ou de fonctionnalité.
* **Actions** : Ce sont des fonctions que nos composants peuvent invoquer pour déclencher un changement dans l'état de l'application. Celles-ci résident également dans le store.

### Étape 1 : Création des entités

Lorsque nous définissons une entité, nous réfléchissons à la manière dont l'entité réagirait à certaines _actions_. Nous appelons cela ses _réactions_. Chaque réaction comprend des changements d'état qui se produisent au sein de l'entité (rappelons que chaque entité n'est qu'une partie de notre état d'application).

La bibliothèque Reactor fournit une fonction appelée `createEntity` que nous utiliserons pour définir nos entités. Elle accepte deux arguments, les réactions de l'entité ainsi que son état initial :

```
createEntity(reactions: Object, initialState: any)
```

Commençons par la partie la plus facile. L'`initialState` doit essentiellement définir la structure de données de notre entité en lui attribuant une valeur par défaut.

L'argument `reactions` est un mappage des noms d'actions contre les réactions correspondantes. **Notez que le mappage n'est pas destiné à définir les fonctions d'action réelles.**

Dans sa forme la plus simple, une réaction ressemble à ceci :

```
action: (state, payload) => newState
```

où `action` correspond au nom d'une action, tandis que `payload` (optionnel) est un argument unique que l'entité attend que vous passiez à l'action. Tout cela signifie vraiment que, lorsque `action(payload)` est invoquée, l'entité applique une certaine logique pour changer son état de `state` à `newState`.

![Image](https://cdn-media-1.freecodecamp.org/images/rPTIu9N-LqknB7MH8hODj7CMFxQt2Jklcfx5)

Voici un exemple simple de définition d'entité :

```
const initialState = { value: 0 };
```

```
const counter = createEntity(  {    increment: (state, by) => (      { ...state, value: state.value + by }    ),    reset: state => ({ ...state, value: 0 })  },  initialState);
```

**IMPORTANT :** En définissant les réactions d'une entité, gardez à l'esprit que la règle d'or de React de ne pas muter l'état du composant s'applique également à l'état de l'application. Donc, si l'état de votre entité est de type objet ou tableau, assurez-vous toujours de retourner un nouvel objet ou tableau.

Jusqu'à présent, c'est facile, n'est-ce pas ? Continuons...

### Étape 2 : Configuration du Store

J'ai dit « _le_ store » car il ne peut y avoir qu'un **seul** store dans toute notre application. Pour rendre ce store disponible à tous nos composants, nous devons l'injecter dans un composant de haut niveau, généralement `<App>`.

La bibliothèque Reactor inclut le HOC `withStore` qui crée le store, y place les entités et désigne son composant cible comme le fournisseur/propriétaire du store.

```
withStore(entities: Object) (Component)
```

Ici, l'argument `entities` est un mappage des noms d'entités contre les objets d'entités réels créés en utilisant `createEntity()`. Ce mappage est important car nous accédons aux entités du store en utilisant les noms assignés ici.

Prenons l'entité `counter` de notre exemple précédent, et créons notre store puis plaçons l'entité dedans :

```
import counter from './store/counter';
```

```
const _App = () => (  <Router>    <Shell />  </Router>);
```

```
const App = withStore({ counter })(_App);
```

C'est aussi simple que cela. Notre store est maintenant prêt.

### Étape 3 : Importation des Props depuis le Store

Maintenant, la dernière étape restante est de rendre l'état de l'application accessible à nos composants. Il y a 2 règles simples :

* Les composants peuvent _lire_ l'état de l'application en important les _entités_ depuis le store.
* Ils peuvent également _changer_ l'état de l'application, en important les _actions_ depuis le store.

Nous utilisons le HOC `getPropsFromStore` de la bibliothèque Reactor pour faire l'un ou l'autre, ou les deux, et les injecter dans notre composant en tant que props.

```
getPropsFromStore(  entities?: Array<string>,   actions?: Array<string>) (Component)
```

Ici, `entities` est une liste de noms d'entités, et `actions` est une liste de noms d'actions.

Les entités importées sont injectées en tant que _props d'état_. Cela signifie que chaque fois que l'une de ces entités change, le composant se re-rendra.

Les actions importées sont injectées en tant que props de fonction que nous pouvons invoquer directement dans notre composant.

Vous vous demandez peut-être, où définissons-nous ces fonctions d'action ? Eh bien, nous ne le faisons pas. Le store les crée pour nous, sur la base de tous les noms d'actions que nous avons mappés aux _réactions_ lors de la création de nos entités avec `createEntity`.

En continuant nos exemples précédents, nous importons l'entité `counter` depuis le store comme suit :

```
const _ClickCount = ({ counter, increment, reset }) => (  <>    Vous avez cliqué {counter.value} fois.    <button onClick={() => increment(1)}>Cliquez-moi</button>    <button onClick={reset}>Réinitialiser le compteur</button>  </>);
```

```
const ClickCount = getPropsFromStore(  ['counter'],   ['increment', 'reset'])(_ClickCount);
```

**C'est tout !** En 3 étapes faciles, nous avons connecté notre composant à l'état de l'application.

### Travailler avec des Actions Asynchrones

Une _action asynchrone_ est essentiellement une action qui nécessite une sorte d'opération non bloquante et asynchrone, telle que la récupération de données, un minuteur, une tâche intensive en calcul, ou toute autre chose qui ne peut pas compléter immédiatement son exécution.

Avec la forme simple de réaction, le calcul du nouvel état est effectué _immédiatement_. Mais lorsque nous traitons des actions asynchrones, l'entité doit effectuer une opération asynchrone et attendre qu'elle se termine avant de pouvoir calculer le changement d'état. Pour cela, nous avons besoin d'une forme différente de réaction, appelée à juste titre une _réaction asynchrone_.

#### Définition des Réactions Asynchrones

La fonction `createEntity` de la bibliothèque Reactor nous permet de définir facilement des réactions asynchrones, _de manière déclarative_, sous la forme suivante :

```
action: [  (state, payload) => newState,  async (payload, next) => {     const result = await doSomethingAsync();    next(result);   },  (state, result) => newState]
```

Il s'agit d'un tableau composé des **3 étapes** de notre réaction asynchrone :

1. L'_étape de démarrage_ où tout changement d'état préparatoire peut être effectué, par exemple, définir un indicateur « loading » ou « wait ».
2. L'_étape asynchrone_ où l'entité effectue l'opération asynchrone. Elle attend que l'opération asynchrone se termine avant d'appeler l'étape suivante.
3. L'_étape de completion_ où le changement d'état final est effectué, normalement basé sur le résultat de l'étape asynchrone précédente.

Ce diagramme illustre comment les données circulent tout au long des 3 étapes de la réaction asynchrone :

![Image](https://cdn-media-1.freecodecamp.org/images/zGdu2r0KHgKfGdPEIUaZikIXcmuYKniMpxLs)

La première étape (démarrage) est en fait _optionnelle_, car il arrive que vous n'ayez pas vraiment besoin d'un changement d'état préparatoire.

#### Exemple d'Utilisation

Voici un exemple d'une entité complète avec des réactions simples et asynchrones. Vous pouvez toujours revenir à l'illustration ci-dessus si le flux de données et les changements d'état semblent encore quelque peu flous.

```
const initialState = { auth: null, waiting: false };
```

```
const session = createEntity(  {    login: [      state => ({ ...state, waiting: true }),      async ({ username, password }, next) => {        const response = await login(username, password);        next(response);      },      (state, { auth }) => ({ ...state, auth, waiting: false }),    ],    logout: state => ({ ...state, auth: null }),  },  initialState);
```

Une fois que vous vous êtes habitué à ce format en 3 étapes, vous serez en mesure de créer des entités rapidement car vous n'aurez besoin de vous concentrer que sur la logique de changement d'état et le flux de données, sans vous soucier d'écrire un code boilerplate complexe.

**C'est tout !** N'est-ce pas trop facile ?

### Chargement Paresseux de l'État de l'Application

Si vous faites du code splitting, vous voudrez également fractionner l'état de votre application. Un module chargé de manière paresseuse peut avoir son propre _feature store_ contenant des entités spécifiques à la fonctionnalité.

Puisqu'il ne peut y avoir qu'un seul store dans l'application, la bibliothèque Reactor fournit un moyen simple de fusionner dynamiquement les feature stores chargés de manière paresseuse dans le store principal. Cela se fait en utilisant le HOC `withFeatureStore`, qui a la signature suivante :

```
withFeatureStore(entities: Object) (Component)
```

Comme vous pouvez le remarquer, cela a exactement le même format que le HOC `withStore` dont nous avons parlé précédemment. Il spécifie les `entities` qui sont chargées de manière paresseuse avec vos modules de fonctionnalité, pour permettre à la bibliothèque Reactor de savoir que ces entités doivent être fusionnées dynamiquement dans le store une fois les modules de fonctionnalité chargés.

#### Exemple d'Utilisation

Prenons, par exemple, une fonctionnalité de minuteur chargée de manière paresseuse qui a un composant `TimerPage` comme point d'entrée, et une entité `timer` pour gérer son état.

```
import timer from './store/timer';
```

```
const _TimerPage = () => (  <Countdown />);
```

```
const TimerPage = withFeatureStore({ timer })(_TimerPage);
```

**C'est tout !** Encore une fois, rapide et facile.

### Informations Complémentaires

Pour en savoir plus sur la bibliothèque Reactor que nous avons utilisée dans cet article, vous pouvez trouver sa documentation officielle à l'adresse [https://github.com/arnelenero/reactorlib](https://github.com/arnelenero/reactorlib).

Merci d'avoir lu.