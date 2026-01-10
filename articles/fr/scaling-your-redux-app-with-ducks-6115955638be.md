---
title: Mise à l'échelle de votre application Redux avec ducks
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-01-23T06:48:21.000Z'
originalURL: https://freecodecamp.org/news/scaling-your-redux-app-with-ducks-6115955638be
coverImage: https://cdn-media-1.freecodecamp.org/images/1*uceu9f-p_A2H2-2xD-6MiQ.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: Redux
  slug: redux
- name: Web Development
  slug: web-development
seo_title: Mise à l'échelle de votre application Redux avec ducks
seo_desc: 'By Alex Moldovan

  How does your front-end application scale? How do you make sure that the code you’re
  writing is maintainable 6 months from now?

  Redux took the world of front-end development by storm in 2015 and established itself
  as a standard — eve...'
---

Par Alex Moldovan

Comment votre application front-end évolue-t-elle ? Comment vous assurez-vous que le code que vous écrivez sera maintenable dans 6 mois ?

[Redux](http://redux.js.org/) a conquis le monde du développement front-end en 2015 et s'est établi comme une norme — même au-delà du cadre de React.

Dans l'entreprise où je travaille, nous avons récemment terminé la refactorisation d'une base de code React assez grande, en ajoutant Redux au lieu de [reflux](https://github.com/reflux/refluxjs).

Nous l'avons fait parce que continuer aurait été impossible sans une application bien structurée et un bon ensemble de règles.

La base de code a plus de deux ans, et _reflux_ était là depuis le début. Nous avons dû modifier du code qui n'avait pas été touché depuis plus d'un an et qui était assez emmêlé avec les composants React.

Sur la base du travail que nous avons effectué sur le projet, j'ai créé [ce dépôt](https://github.com/alexnm/re-ducks), expliquant notre approche pour organiser notre code Redux.

Lorsque vous apprenez Redux et les rôles des actions et des reducers, vous commencez par des exemples très simples. La plupart des tutoriels disponibles aujourd'hui ne vont pas au niveau suivant. Mais si vous construisez quelque chose avec Redux qui est plus compliqué qu'une liste de tâches, vous aurez besoin d'une manière plus intelligente de faire évoluer votre base de code au fil du temps.

Quelqu'un a dit un jour que _nommer les choses_ est l'un des travaux les plus difficiles en informatique. Je ne pourrais pas être plus d'accord. Mais structurer les dossiers et organiser les fichiers est une tâche tout aussi difficile.

Explorons comment nous avons abordé l'organisation du code par le passé.

### Fonction vs Fonctionnalité

Il existe deux approches établies pour structurer les applications : _fonction-d'abord_ et _fonctionnalité-d'abord_.

À gauche ci-dessous, vous pouvez voir une structure de dossiers basée sur les fonctions. À droite, vous pouvez voir une approche basée sur les fonctionnalités.

![Image](https://cdn-media-1.freecodecamp.org/images/1*HM8M2Agd_TBfU4Zm1_lEJA.png)

L'approche fonction-d'abord signifie que vos répertoires de premier niveau sont nommés selon la finalité des fichiers qu'ils contiennent. Vous avez donc : _containers_, _components_, _actions_, _reducers_, etc.

Cela ne se met pas du tout à l'échelle. À mesure que votre application grandit et que vous ajoutez plus de fonctionnalités, vous ajoutez des fichiers dans les mêmes dossiers. Vous finissez donc par devoir faire défiler un seul dossier pour trouver votre fichier.

Le problème est également lié au couplage des dossiers ensemble. Un seul flux à travers votre application nécessitera probablement des fichiers de tous les dossiers.

Un avantage de cette approche est qu'elle isole — dans notre cas — React de Redux. Donc, si vous voulez changer la bibliothèque de gestion d'état, vous savez quels dossiers vous devez modifier. Si vous changez la bibliothèque de vue, vous pouvez garder vos dossiers Redux intacts.

L'approche fonctionnalité-d'abord signifie que les répertoires de premier niveau sont nommés selon les principales fonctionnalités de l'application : _product_, _cart_, _session_.

Cette approche se met beaucoup mieux à l'échelle, car chaque nouvelle fonctionnalité vient avec un nouveau dossier. Mais, vous n'avez aucune séparation entre les composants React et Redux. Changer l'un d'eux à long terme est une tâche très délicate.

De plus, vous avez des fichiers qui n'appartiennent à aucune fonctionnalité. Vous finissez par avoir un dossier _common_ ou _shared_, parce que vous voulez réutiliser du code à travers de nombreuses fonctionnalités dans votre application.

### Le meilleur des deux mondes

Bien que cela ne soit pas dans le cadre de cet article, je veux aborder cette idée : **séparez toujours les fichiers de gestion d'état des fichiers d'interface utilisateur.**

Pensez à votre application à long terme. Imaginez ce qui arrive à la base de code lorsque vous passez de _React_ à une autre bibliothèque. Ou imaginez comment votre base de code utiliserait _ReactNative_ en parallèle avec la version web.

[Notre approche](https://github.com/FortechRomania/react-redux-complete-example) part du besoin d'isoler le code React dans un seul dossier — appelé views — et le code Redux dans un dossier séparé — appelé redux.

Cette première division nous donne la flexibilité d'organiser les deux parties séparées de l'application de manière complètement différente.

Dans le dossier views, nous préférons une approche fonction-d'abord pour structurer les fichiers. Cela semble très naturel dans le contexte de React : _pages_, _layouts_, _components_, _enhancers_, etc.

Pour ne pas devenir fou avec le nombre de fichiers dans un dossier, nous pouvons avoir une division basée sur les fonctionnalités à l'intérieur de chacun de ces dossiers.

Ensuite, à l'intérieur du dossier redux...

### Voici re-ducks

Chaque fonctionnalité de l'application doit correspondre à des actions et des reducers séparés, il est donc logique d'opter pour une approche fonctionnalité-d'abord.

L'approche modulaire originale [ducks](https://github.com/erikras/ducks-modular-redux) est une simplification agréable pour Redux et offre une manière structurée d'ajouter chaque nouvelle fonctionnalité dans votre application.

Pourtant, nous voulions explorer un peu ce qui se passe lorsque l'application se met à l'échelle. Nous avons réalisé qu'un seul fichier pour une fonctionnalité devient trop encombré et difficile à maintenir à long terme.

C'est ainsi que [_re-ducks_ est né](https://github.com/alexnm/re-ducks). La solution était de diviser chaque fonctionnalité en un dossier _duck_.

```
duck/
├── actions.js
├── index.js
├── operations.js
├── reducers.js
├── selectors.js
├── tests.js
├── types.js
└── utils.js
```

Un dossier duck DOIT :

* contenir toute la logique pour gérer uniquement UN concept dans votre application, ex : _product_, _cart_, _session_, etc.
* avoir un fichier `index.js` qui exporte selon les règles originales des ducks.
* garder le code avec un but similaire dans le même fichier, tel que _reducers_, _selectors_, et _actions_
* contenir les _tests_ liés au duck.

Pour cet exemple, nous n'avons utilisé aucune abstraction construite sur Redux. Lorsque vous construisez un logiciel, il est important de commencer avec le moins d'abstractions possible. De cette manière, vous vous assurez que le coût de vos abstractions ne dépasse pas les bénéfices.

Si vous devez vous convaincre que les abstractions peuvent être mauvaises, regardez cette [superbe conférence de Cheng Lou](https://www.youtube.com/watch?v=mVVNJKv9esE).

Voyons ce qui va dans chaque fichier.

#### Types

Le fichier _types_ contient les noms des actions que vous envoyez dans votre application. En tant que bonne pratique, vous devriez essayer de définir les noms en fonction de la fonctionnalité à laquelle ils appartiennent. Cela aide lors du débogage d'applications plus complexes.

```javascript
const QUACK = "app/duck/QUACK";
const SWIM = "app/duck/SWIM";

export default {
    QUACK,
    SWIM
};
```

#### Actions

Ce fichier contient toutes les fonctions de création d'actions.

```javascript
import types from "./types";

const quack = ( ) => ( {
    type: types.QUACK
} );

const swim = ( distance ) => ( {
    type: types.SWIM,
    payload: {
        distance
    }
} );

export default {
    swim,
    quack
};
```

Remarquez comment toutes les actions sont représentées par des fonctions, même si elles ne sont pas paramétrées. Une approche cohérente est plus que nécessaire dans une grande base de code.

#### Operations

Pour représenter des opérations enchaînées, vous avez besoin d'un _middleware_ Redux pour améliorer la fonction de dispatch. Certains exemples populaires sont : [redux-thunk](https://github.com/gaearon/redux-thunk), [redux-saga](https://github.com/redux-saga/redux-saga) ou [redux-observable](https://github.com/redux-observable/redux-observable).

Dans notre cas, nous utilisons _redux-thunk_. Nous voulons séparer les thunks des créateurs d'actions, même avec le coût d'écrire du code supplémentaire. Nous définissons donc une opération comme un wrapper sur les actions.

Si l'opération ne dispatch qu'une seule action — n'utilise pas réellement redux-thunk — nous transférons la fonction de création d'action. Si l'opération utilise un thunk, elle peut dispatcher de nombreuses actions et les enchaîner avec des promesses.

```javascript
import actions from "./actions";

// Ceci est un lien vers une action définie dans actions.js.
const simpleQuack = actions.quack;

// Ceci est un thunk qui dispatch plusieurs actions de actions.js
const complexQuack = ( distance ) => ( dispatch ) => {
    dispatch( actions.quack( ) ).then( ( ) => {
        dispatch( actions.swim( distance ) );
        dispatch( /* any action */ );
    } );
}

export default {
    simpleQuack,
    complexQuack
};
```

Appelez-les opérations, thunks, sagas, epics, c'est votre choix. Trouvez simplement une convention de nommage et tenez-vous-y.

À la fin, lorsque nous discuterons de l'_index_, nous verrons que les opérations font partie de l'interface publique du duck. Les actions sont encapsulées, les opérations sont exposées.

#### Reducers

Si une fonctionnalité a plusieurs facettes, vous devriez définitivement utiliser plusieurs reducers pour gérer différentes parties de la forme de l'état. De plus, n'ayez pas peur d'utiliser _combineReducers_ autant que nécessaire. Cela vous donne beaucoup de flexibilité lorsque vous travaillez avec une forme d'état complexe.

```javascript
import { combineReducers } from "redux";
import types from "./types";

/* State Shape
{
    quacking: bool,
    distance: number
}
*/

const quackReducer = ( state = false, action ) => {
    switch( action.type ) {
        case types.QUACK: return true;
        /* ... */
        default: return state;
    }
}

const distanceReducer = ( state = 0, action ) => {
    switch( action.type ) {
        case types.SWIM: return state + action.payload.distance;
        /* ... */
        default: return state;
    }
}

const reducer = combineReducers( {
    quacking: quackReducer,
    distance: distanceReducer
} );

export default reducer;
```

Dans une application à grande échelle, votre arbre d'état aura au moins 3 niveaux de profondeur. Les fonctions de reducer doivent être aussi petites que possible et gérer uniquement des structures de données simples. La fonction utilitaire _combineReducers_ est tout ce dont vous avez besoin pour construire une forme d'état flexible et maintenable.

Consultez le [projet d'exemple complet](https://github.com/FortechRomania/react-redux-complete-example) et voyez comment _combineReducers_ est utilisé. Une fois dans les fichiers _reducers.js_ et ensuite dans le fichier _store.js_, où nous assemblons tout l'arbre d'état.

#### Selectors

Avec les opérations, les selectors font partie de l'interface publique d'un duck. La séparation entre les opérations et les selectors ressemble au [modèle CQRS](https://martinfowler.com/bliki/CQRS.html).

Les fonctions de selector prennent une partie de l'état de l'application et retournent certaines données basées sur celui-ci. Elles n'introduisent jamais de changements dans l'état de l'application.

```javascript
function checkIfDuckIsInRange( duck ) {
    return duck.distance > 1000;
}

export default {
    checkIfDuckIsInRange
};
```

#### Index

Ce fichier spécifie ce qui est exporté du dossier duck. Il va :

* exporter par défaut la fonction de reducer du duck.
* exporter comme exports nommés les selectors et les opérations.
* exporter les types s'ils sont nécessaires dans d'autres ducks.

```javascript
import reducer from "./reducers";

export { default as duckSelectors } from "./selectors";
export { default as duckOperations } from "./operations";
export { default as duckTypes } from "./types";

export default reducer;
```

#### Tests

Un avantage de l'utilisation de Redux et de la structure des ducks est que vous pouvez écrire vos tests à côté du code que vous testez.

Tester votre code Redux est assez simple :

```javascript
import expect from "expect.js";
import reducer from "./reducers";
import actions from "./actions";

describe( "duck reducer", function( ) {
    describe( "quack", function( ) {
        const quack = actions.quack( );
        const initialState = false;

        const result = reducer( initialState, quack );

        it( "should quack", function( ) {
            expect( result ).to.be( true ) ;
        } );
    } );
} );
```

Dans ce fichier, vous pouvez écrire des tests pour les reducers, les opérations, les selectors, etc.

Je pourrais écrire un article complètement différent sur les avantages de tester votre code, il y en a tant. Faites-le simplement !

### Donc, voilà

La partie intéressante à propos de re-ducks est que vous obtenez à utiliser le même modèle pour tout votre code Redux.

La division basée sur les fonctionnalités pour le code Redux est beaucoup plus flexible et évolutive à mesure que la base de code de votre application grandit. Et la division basée sur les fonctions pour les vues fonctionne lorsque vous construisez de petits composants qui sont partagés à travers l'application.

Vous pouvez consulter une base de code complète react-redux-example [ici](https://github.com/FortechRomania/react-redux-complete-example). Gardez simplement à l'esprit que le dépôt est encore en développement actif.

Comment structurez-vous vos applications Redux ? J'ai hâte d'avoir des retours sur cette approche que j'ai présentée.

Si vous avez trouvé cet article utile, cliquez sur le cœur vert ci-dessous et je saurai que mes efforts ne sont pas vains.