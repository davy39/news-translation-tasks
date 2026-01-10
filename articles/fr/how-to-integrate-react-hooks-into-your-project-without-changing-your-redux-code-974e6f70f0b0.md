---
title: Comment intégrer React Hooks dans votre projet sans modifier votre code Redux
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-22T18:29:24.000Z'
originalURL: https://freecodecamp.org/news/how-to-integrate-react-hooks-into-your-project-without-changing-your-redux-code-974e6f70f0b0
coverImage: https://cdn-media-1.freecodecamp.org/images/1*RijhIwu_gn98_W_QnYcGAA.jpeg
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
seo_title: Comment intégrer React Hooks dans votre projet sans modifier votre code
  Redux
seo_desc: 'By Mohammad Iqbal

  In this tutorial we will be going over how to integrate React Hooks into a React
  Redux project without changing the Redux code (reducers and actions) at all.

  To save time, we can start with with a basic React Redux app instead of bu...'
---

Par Mohammad Iqbal

Dans ce tutoriel, nous allons voir comment intégrer React Hooks dans un projet React Redux sans modifier le code Redux (réducteurs et actions) du tout.

Pour gagner du temps, nous pouvons commencer avec une application React Redux de base au lieu d'en construire une à partir de zéro. Cela vous permettra de voir le code avant et après côte à côte et de faciliter l'intégration pour votre application.

Vous pouvez également me suivre sur Twitter pour plus de tutoriels à l'avenir : [ici](https://twitter.com/iqbal125sf)

**Code de démarrage :**

[**iqbal125/modern-react-app-sample**](https://github.com/iqbal125/modern-react-app-sample)
[_Contribuez au développement de iqbal125/modern-react-app-sample en créant un compte sur GitHub._github.com](https://github.com/iqbal125/modern-react-app-sample)

#### Utilisation de la bonne version de React

La toute première chose que nous devons faire est de nous assurer que nous avons la bonne version de React. Au moment de la rédaction de cet article, create-react-app ne vous donne pas la bonne version. Vous pouvez donc utiliser create-react-app, puis aller dans votre fichier package.json et taper la bonne version. Il suffit de changer React et React-dom en version 16.8. Enregistrez le fichier et supprimez votre dossier node modules. Exécutez npm install et vous êtes prêt à partir.

```javascript
{
  "name": "app2",
  "version": "0.1.0",
  "private": true,
  "dependencies": {
    "auth0-js": "^9.8.2",
    "history": "^4.7.2",
    "react": "^16.8.0",
    "react-dom": "^16.8.0",
    "react-redux": "^6.0.0",
    "react-router": "^4.3.1",
    "react-router-dom": "^4.3.1",
    "react-scripts": "2.1.1",
    "redux": "^4.0.1"
  },
```

#### Refactorisation d'une classe React en un Hook React

La première chose que nous allons faire est de refactoriser un composant de classe React en un Hook React. Ouvrons notre fichier App.js et transformons-le en un Hook, donc refactorisez votre App.js comme suit :

```javascript
import React, { Component } from 'react';
import Routes from './routes';



const App = () => {

    return(
      <div>
      React
      <Routes />
      </div>
    )
}


export default App;
```

Donc, il suffit de transformer la classe en une fonction fléchée et de supprimer la méthode render. Et voilà, vous avez créé un Hook React !

#### Configuration d'un autre Hook

De la même manière, nous pouvons configurer un autre Hook, que nous allons configurer dans un dossier appelé Hooks.

Créez donc un fichier hooks_container.js dans le répertoire hooks et configurez-le comme suit :

```javascript
import React, { useState } from 'react';




const HooksContainer = () => {

    return(
      <div>

      </div>
    )
}


export default HooksContainer;
```

#### Le Hook useState()

Nous allons maintenant commencer à configurer un état de composant non global de base avec le hook useState().

Le hook useState() est similaire à la fonction setState() de React. Il est configuré avec une destructuration de tableau, où le premier élément du tableau est la valeur de l'état et le second élément est une fonction pour changer l'état.

Créons simplement des boutons d'incrémentation et de décrémentation de base pour voir comment fonctionne la fonction useState.

Configurez les boutons comme suit :

```javascript
import React, { useState } from 'react';




const HooksContainer = () => {

  const [value, setValue] = useState(0)

  const incrementValue = () => {
    setValue(value + 1 )
  }

  const decrementValue = () => {
    setValue(value - 1 )
  }

    return(
      <div>
        <button onClick={() => incrementValue()}> Ajouter une valeur locale </button>
        <button onClick={() => decrementValue()}> Décrémenter la valeur locale </button>
        <br />
        <div>
          État local React : {value}
        </div>
      </div>
    )
}


export default HooksContainer;
```

Remarquez que nous n'avons pas à utiliser les mots-clés "props" ou "state" n'importe où, nous pouvons simplement utiliser le nom de la variable et de la fonction directement. C'est l'une des choses qui rendent les Hooks React si faciles à utiliser.

Votre application devrait ressembler à ceci.

![Image](https://cdn-media-1.freecodecamp.org/images/0*CscqAv6uPi86BjMB)

Et vous devriez pouvoir augmenter ou diminuer le nombre librement.

Maintenant que nous avons une idée de base de comment fonctionne useState(), nous pouvons passer à quelque chose d'un peu plus complexe.

#### Le Hook useReducer()

Nous pouvons maintenant commencer à configurer le hook useReducer().

Avant de pouvoir utiliser le hook useReducer(), nous devons d'abord configurer le réducteur. Les actions peuvent en fait être laissées telles quelles. Et le changement que nous devons apporter au réducteur est très minimal. Tout ce que nous avons à faire est de changer les déclarations d'exportation au lieu d'exporter par défaut. Nous devons exporter à la fois le réducteur et l'état initial.

Pour gagner du temps, créez simplement un nouveau réducteur appelé hooks_reducer.js dans le fichier réducteur et copiez le code de Reducer1. Vous devriez avoir quelque chose qui ressemble à ceci :

```javascript

import * as ACTION_TYPES from '../actions/action_types'

export const initialState = {
  stateprop1: false,
}

export const HooksReducer1 = (state = initialState, action) => {
    switch(action.type) {
      case ACTION_TYPES.SUCCESS:
        return {
          ...state,
          stateprop1: true
        }
      case ACTION_TYPES.FAILURE:
        return {
          ...state,
          stateprop1: false
        }
      default:
        return state
    }
}
```

Maintenant, importez simplement ce réducteur et son état initial dans hooks_container.js. Et passez-les tous les deux dans le hook useReducer().

```javascript

import * as HooksReducer1 from '../store/reducers/hooks_reducer';

...

const [state, dispatch] = useReducer(HooksReducer1.HooksReducer1, HooksReducer1.initialState)
```

Créons également 2 boutons pour changer stateprop1 de false à true et vice versa. Et nous pouvons également créer une expression ternaire pour afficher du texte en fonction de si stateprop1 est vrai ou faux. N'oubliez pas que stateprop1 est le même que celui que nous avons configuré dans HookReducer1, mais nous le mettons à jour ici dans notre conteneur.

Et nous utilisons les mêmes actions préexistantes pour mettre à jour le réducteur. Remarquez dans les commentaires que j'ai laissé deux méthodes alternatives pour dispatcher les actions. Elles font toutes la même chose. Retourner un objet javascript avec un type de chaîne de SUCCESS.

Donc votre code devrait ressembler à ceci :

```javascript
import React, { useState } from 'react';
import * as ACTIONS from '../store/actions/actions';
import * as HooksReducer1 from '../store/hooks_state/reducer1_hooks';



const HooksContainer = () => {

  const [state, dispatch] = useReducer(HooksReducer1.HooksReducer1, HooksReducer1.initialState)
  const [value, setValue] = useState(0)

  const incrementValue = () => {
    setValue(value + 1 )
  }

  const decrementValue = () => {
    setValue(value - 1 )
  }
  
  const handleDispatchTrue = () => {
    //    dispatch(type: "SUCCESS")
    //    dispatch(ACTIONS.SUCCESS)
    dispatch(ACTIONS.success())
  }

  const handleDispatchFalse = () => {
    //     dispatch(type: "FAILURE")
    //    dispatch(ACTIONS.FAILURE)
    dispatch(ACTIONS.failure())
  }

    return(
      <div>
        <button onClick={() => incrementValue()}> Ajouter une valeur locale </button>
        <button onClick={() => decrementValue()}> Décrémenter la valeur locale </button>
        <button onClick={() => handleDispatchTrue()}>Dispatcher Vrai </button>
        <button onClick={() => handleDispatchFalse()}>Dispatcher Faux </button>
        <br />
        <br />
        <div>
          État local React : {value}
        </div>
        <div>
        {state.stateprop1
          ? <p> stateprop1 est vrai </p>
          : <p> stateprop1 est faux </p>
        }
        </div>
      </div>
    )
}


export default HooksContainer;
```

Votre application devrait ressembler à ceci et vous devriez pouvoir changer stateprop1 à partir du conteneur de hooks :

![Image](https://cdn-media-1.freecodecamp.org/images/0*YhL5unbUcK0MFbQD)

Vous remarquerez un problème lorsque nous allons à un autre composant : l'état n'est pas sauvegardé. Cela est dû au fait que même si nous utilisons des actions et des réducteurs, l'état est toujours un état de composant local et n'est pas disponible globalement. Pour rendre l'état disponible globalement, nous devons en fait utiliser le Contexte React, que nous allons configurer dans les prochaines sections.

#### Configuration des Actions et du Réducteur

Avant de configurer le Contexte, configurons les Actions et le Réducteur que nous allons utiliser avec lui. Ajoutons donc une deuxième propriété à HooksReducer1 appelée stateprop2 et définissons-la à 0.

Nous devons maintenant configurer les actions et les types d'actions pour travailler avec ce nouvel état.

Créons d'abord 2 types d'actions pour stateprop2 :

```javascript

export const INC_GLOBAL_STATE = "INC_GLOBAL_STATE"

export const DEC_GLOBAL_STATE = "DEC_GLOBAL_STATE"
```

Ensuite, nous pouvons aller dans notre fichier d'actions et créer 2 créateurs d'actions pour gérer ces types d'actions.

```javascript


export const inc_global_state = () => {
  return {
  type: ACTION_TYPES.INC_GLOBAL_STATE
  }
}

export const dec_global_state = () => {
  return {
  type: ACTION_TYPES.DEC_GLOBAL_STATE
  }
}
```

Enfin, nous devons configurer notre réducteur qui devrait ressembler à ceci :

```javascript
import * as ACTION_TYPES from '../actions/action_types'

export const initialState = {
  stateprop1: false,
  stateprop2: 0
}

export const HooksReducer1 = (state = initialState, action) => {
    switch(action.type) {
      case ACTION_TYPES.SUCCESS:
        return {
          ...state,
          stateprop1: true
        }
      case ACTION_TYPES.FAILURE:
        return {
          ...state,
          stateprop1: false
        }
      case ACTION_TYPES.INC_GLOBAL_STATE:
        return {
          ...state,
          stateprop2: state.stateprop2 + 1
        }
      case ACTION_TYPES.DEC_GLOBAL_STATE:
        return {
          ...state,
          stateprop2: state.stateprop2 - 1 
        }
      default:
        return state
    }
}
```

#### Contexte React

Ensuite, nous devons configurer l'objet de contexte. Créez simplement un autre fichier context.js et configurez-le comme suit :

```javascript
import React from 'react';

const Context = React.createContext({
  prop1: false
})

export default Context;
```

Notez que prop1 ici est sans importance. Nous allons le remplacer dans notre fichier App.js. Nous avons simplement fourni prop1 pour initialiser l'objet Context. Tout le code pour mettre à jour et lire notre état sera fait dans le fichier App.js.

Ensuite, importons cet objet de contexte dans notre fichier App.js. Importez également HooksReducer1 et les Actions puisque nous allons les utiliser ici.

Configurons également useReducer de la même manière que précédemment.

```javascript
import React, { useReducer } from 'react';
import Routes from './routes';
import Context from './utils/context';
import * as ACTIONS from './store/actions/actions';
import * as HooksReducer1 from './store/reducers/hooks_reducer';



const App = () => {
  const [valueGlobal, dispatchActionsGlobal] = useReducer(HooksReducer1.HooksReducer1, HooksReducer1.initialState)

...
```

Ensuite, nous devons créer 2 fonctions pour dispatcher nos créateurs d'actions que nous venons de créer. Ces fonctions vont incrémenter et décrémenter stateprop2.

Nous devons également envelopper nos routes avec un composant <Context.Provider />. C'est ce qui nous permet d'avoir un état global. Le composant <Context.Provider /> transmet tout l'état aux composants enfants. Puisque App.js est le composant racine, l'état est transmis à chaque composant de l'application, ce qui rend l'état global.

L'état lui-même est contenu dans une propriété appelée "value". Tout cela est similaire au composant <Provider /> et à la propriété "store" vue dans React-Redux.

Nous devons ensuite passer l'état et les dispatches d'actions en tant que propriétés à la propriété value. Nous aurons besoin de 3 propriétés ici : une pour une fonction pour incrémenter notre valeur d'état, une pour une fonction pour décrémenter notre valeur d'état et une pour contenir la valeur réelle de l'état.

Ensemble, votre fichier App.js ressemblera à ceci :

```javascript
import React, { useReducer } from 'react';
import Routes from './routes';
import Context from './utils/context';
import * as ACTIONS from './store/actions/actions';
import * as HooksReducer1 from './store/reducers/hooks_reducer';



const App = () => {
  const [valueGlobal, dispatchActionsGlobal] = useReducer(HooksReducer1.HooksReducer1, HooksReducer1.initialState)

    const incrementGlobalValue = () => {
      dispatchActionsGlobal(ACTIONS.inc_global_state() )
    }

    const decrementGlobalValue = () => {
      dispatchActionsGlobal(ACTIONS.dec_global_state() )
    }

    return(
      <div>
        React
        <Context.Provider
                  value={{
                    valueGlobalState: valueGlobal,
                    addGlobalValue: () => incrementGlobalValue(),
                    decGlobalValue: () => decrementGlobalValue()
                  }}>
            <Routes />
          </Context.Provider>
      </div>
    )
}


export default App;
```

J'ai intentionnellement gardé tous les noms de fonctions et de propriétés différents pour qu'il soit plus facile de voir d'où tout vient lorsque nous utilisons Context dans le composant enfant.

Donc maintenant, toutes ces propriétés définies dans la propriété value peuvent être accessibles par tous les composants enfants, et nous avons donc un état global !

#### Utilisation du Contexte dans un composant enfant avec le hook useContext().

Retournons à notre conteneur de hooks et utilisons ces fonctions et cet état que nous venons de configurer.

Pour utiliser le Contexte dans notre conteneur de hooks, nous devons d'abord l'importer et passer l'objet Context entier dans les hooks useContext. Comme ceci :

```javascript

...

import Context from '../utils/context';


const HooksContainer = () => {
  const context = useContext(Context)
  
...
```

Ensuite, nous pouvons accéder directement aux propriétés que nous avons définies dans la propriété value directement via la variable context.

```javascript
...    

<button onClick={() => context.addGlobalValue()}> Ajouter une valeur globale </button>
<button onClick={() => context.decGlobalValue()}> Décrémenter la valeur globale </button>

...
```

Rappelez-vous que addGlobalValue() est le nom de la propriété que nous avons fournie à la propriété value dans App.js. Ce n'est pas le nom de la fonction pour dispatcher les actions ou le nom de la fonction que nous avons définie dans le hook useReducer() dans App.js.

L'accès à la valeur de l'état via Context se fait de la manière suivante :

```javascript
...

<p>Valeur globale : {context.valueGlobalState.stateprop2}</p>

...
```

Et similaire au dispatching des actions, valueGlobalState est le nom de la propriété fournie à la propriété value. Et nous devons accéder à stateprop2 avec la notation par points à partir de la propriété valueGlobalState, puisque valueGlobalState contient tout l'initialState de HooksReducer1, y compris stateprop1.

Et si vous testez maintenant, vous verrez que l'état se met à jour et persiste même après être passé à un autre composant, vous permettant de répliquer la fonctionnalité Redux et d'avoir un état global.

Vous pouvez utiliser ce modèle pour essentiellement l'évoluer pour tout votre code Redux.

**Code final :**

[**iqbal125/react-hooks-basic**](https://github.com/iqbal125/react-hooks-basic)
[_Contribuez au développement de iqbal125/react-hooks-basic en créant un compte sur GitHub._github.com](https://github.com/iqbal125/react-hooks-basic)

#### Résumé

Voici donc un résumé conceptuel de la manière de procéder (nécessite des connaissances de base sur les hooks React) :

Les actions n'ont pas besoin d'être modifiées du tout. Les réducteurs n'ont pas besoin d'être modifiés non plus. Il suffit d'exporter à la fois l'état initial et le réducteur au lieu de simplement exporter le réducteur. N'utilisez pas "export default" en bas du fichier du réducteur.

Importez le réducteur et son état initial dans le fichier App.js racine. Appelez le hook useReducer() dans le fichier App.js racine et enregistrez-le dans une variable. Similaire au hook useState, le premier élément dans la destructuration du tableau est la valeur de l'état et le second élément est la fonction pour changer l'état. Puis passez à la fois le réducteur et initialState que vous avez importés au hook useReducer(). Importez autant de réducteurs que vous le souhaitez et passez chacun d'eux dans un hook useReducer() séparé.

Importez les actions dans App.js comme d'habitude. Le dispatching des actions est également exactement le même. Au lieu d'utiliser la fonction mapDispatchToProps(), vous allez dispatcher les actions à partir de la fonction de changement d'état (second élément dans la destructuration du tableau) de l'appel du hook useReducer().

Configurez et initialisez la fonction React.CreateContext() dans un autre fichier et importez-la dans App.js. Ensuite, enveloppez votre <Routes /> avec <Context.Provider>. Vous aurez généralement besoin de 3 propriétés pour chaque partie de l'état pour la propriété value dans le provider. 1 propriété pour définir l'état à une nouvelle valeur, 1 pour passer la valeur réelle de l'état, et 1 pour remettre l'état à la valeur par défaut.

Ensuite, pour utiliser l'état dans les composants, vous importez d'abord l'objet Context de context.js, puis vous le passez simplement dans le hook useContext() et vous enregistrez cela dans une variable appelée "context" ou ce que vous voulez. Ensuite, pour accéder à la propriété de l'état, il suffit de faire le nom de la variable "context" "." puis le nom de la propriété définie dans la propriété value, suivi du nom de la propriété définie dans l'initialState du réducteur. Pour dispatcher les actions, il suffit de faire "context" "." puis d'appeler le nom de la propriété.

Une fois cela fait, votre état de contexte est disponible globalement et fonctionnera avec votre code React Redux existant.

Pour une version vidéo 100% gratuite de ce tutoriel et plus de contenu approfondi sur les hooks React, veuillez consulter mon cours Udemy ou ma playlist YouTube :

[https://www.udemy.com/react-hooks-with-react-redux-migration](https://www.udemy.com/react-hooks-with-react-redux-migration)

[https://www.youtube.com/watch?v=l8ODM-KoDpA&list=PLMc67XEAt-ywplHhDpoj5vakceZNr8S0B](https://www.youtube.com/watch?v=l8ODM-KoDpA&list=PLMc67XEAt-ywplHhDpoj5vakceZNr8S0B)