---
title: Comment convertir des classes React-Redux en React Hooks, la manière facile
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-05-15T15:47:20.000Z'
originalURL: https://freecodecamp.org/news/how-to-convert-from-react-redux-classes-to-react-hooks-the-easy-way-eca2233e0e7a
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca26b740569d1a4ca5488.jpg
tags:
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment convertir des classes React-Redux en React Hooks, la manière facile
seo_desc: 'By Mohammad Iqbal

  Hello everyone! With the recent release of create-react-app v3 and React hooks,
  I decided to write a tutorial on how to refactor a class component to a functional
  hooks component.

  In this tutorial, I will share how I did it. I refer...'
---

Par Mohammad Iqbal

Bonjour à tous ! Avec la récente sortie de create-react-app v3 et des hooks React, j'ai décidé d'écrire un tutoriel sur la façon de refactoriser un composant de classe en un composant fonctionnel avec hooks.

Dans ce tutoriel, je vais partager comment j'ai fait cela. Je me réfère à cela comme la "manière facile" puisque cela ne nécessite pas de changer votre code Redux du tout. Les reducers et les actions peuvent être virtuellement laissés tels quels.

Si vous voulez une introduction plus basique à l'intégration des React Hooks, consultez mon [tutoriel précédent](https://medium.freecodecamp.org/how-to-integrate-react-hooks-into-your-project-without-changing-your-redux-code-974e6f70f0b0).

Vous pouvez trouver le code du projet [ici](https://github.com/iqbal125/react_hooks_with_react_redux).

Vous pouvez également me suivre sur Twitter pour plus de tutoriels à l'avenir : [ici](https://twitter.com/iqbal125sf)

Ce projet utilise à la fois Redux et les hooks React, ce qui vous permettra de voir le code et les différences côte à côte. Ouvrez les fichiers `hooks_container1.js` et `container1.js` dans votre éditeur de texte pour voir les différences. J'ai fait de mon mieux pour faire correspondre les lignes de la classe React et des hooks React, ce qui facilite la visualisation des différences. Cependant, cela n'a pas fonctionné parfaitement car il y a quelques différences majeures entre les hooks React et les classes React. J'ai essayé de garder la fonctionnalité des deux composants identique pour qu'il soit plus facile pour vous de repérer les différences de syntaxe.

#### **Table des matières**

1. Version TLDR
2. useReducer et Context
3. Quand utiliser l'état local ou global et useState et useReducer
4. Comment fonctionne Context
5. Structure du répertoire
6. L'objet Context
7. Reducers et Actions
8. Lecture et mise à jour de l'état dans React Redux vs. React Hooks
9. Fusion de l'ancien état dans React Hooks
10. Lecture et mise à jour de l'état avec useReducer et Redux Reducers
11. Lecture de l'état et dispatch des actions
12. Context avec useState
13. Context avec useReducer

### **La manière facile — TL;DR**

**Étape 1 :** Pour vos reducers, exportez à la fois l'initialState et le reducer. Ne faites pas d'`export default` du reducer.

**Étape 2 :** Les actions peuvent être laissées telles quelles depuis React-Redux

**Étape 3 :** Importez tous vos reducers et leurs initialState dans le fichier App.js racine. Importez les actions normalement.

**Étape 4 :** Passez chaque reducer et son initialState à un hook `useReducer()` séparé dans le fichier App.js.

**Étape 5 :** Importez la fonction `React.createContext()` dans App.js après l'avoir initialisée dans son propre fichier. Enveloppez tous les composants enfants avec `<Context.Provider />`

**Étape 6 :** Ensuite, il suffit de couper et coller les propriétés définies dans vos fonctions `mapStateToProps()` et `mapDispatchToProps()` de React-Redux dans la prop `value` de `<Context.Provider />`

**Étape 7 :** Changez le mot-clé dispatch dans vos propriétés de la fonction `mapDispatchToProps()` par le nom de la fonction d'actions de dispatch (2ème élément dans la destructuration du tableau) dans le hook `useReducer()`. Puisque chaque reducer aura son propre hook useReducer, vous devrez faire correspondre les dispatchs d'actions appropriés avec le bon reducer.

**Étape 8 :** Faites la même chose pour la fonction `mapStateToProps()`. Changez le nom de la propriété pour qu'il corresponde au hook useReducer. La valeur de l'état pour le hook `useReducer()` (1er élément dans la destructuration du tableau) contient tout l'état initial du reducer. Vous devrez accéder à chaque propriété de l'état avec la notation par points, puis la passer dans une propriété de la prop "value".

**Étape 9 :** Enfin, pour utiliser réellement l'état global Context dans un composant enfant, vous importez d'abord l'objet Context original dans le composant enfant. Ensuite, vous passez l'objet Context importé au hook `useContext()`. Enregistrez le résultat des hooks useContext dans une variable. Maintenant, vous avez accès à toutes les propriétés que nous avons définies dans la prop `value` de `<Context.Provider />` dans le fichier App.js racine.

Accéder aux valeurs d'état dans un composant enfant avec context : `context.stateprop1`

Dispatch des actions dans un composant enfant avec context : `() => context.action1()`

Voici un exemple d'un conteneur de classe React Redux et d'un composant fonctionnel React Hooks avec une fonctionnalité similaire côte à côte.

```javascript
 class Container1 extends Component {
    constructor(props) {
      super(props)

      this.state = {
        local_state_prop1: true,
        local_state_prop2: 0,
        cDM_value: ''
      }
    }

 ...
 
    inc_local = () => {
      this.setState({local_state_prop2: this.state.local_state_prop2 + 1})
    }

    dec_local = () => {
      this.setState({local_state_prop2: this.state.local_state_prop2 - 1})
    }
 
  ...
    <button onClick={() => this.inc_local()}> INC Local State  </button>
    <button onClick={() => this.dec_local()}> DEC Local State  </button>
    <br />
    <br />
      {this.state.local_state_prop2}
    <br />
 ...
    
```

```javascript

const HooksContainer1 = () => {
    const [value, setValue] = useState({local_state_prop1: true,
                                        local_state_prop2: 0
                                       })
  
...    
    const incrementValue_uS = () => {
      setValue({...value, local_state_prop2: value.local_state_prop2 + 1} )
    }

    const decrementValue_uS = () => {
      setValue({...value, local_state_prop2: value.local_state_prop2 - 1} )
    }
    
...

      <button onClick={() => incrementValue_uS()}> Add Local Value uS </button>
      <button onClick={() => decrementValue_uS()}> Dec Local Value uS</button>
      <br />
      <p>Local useState Value: {value.local_state_prop2}</p>
      <br />
 ...
```

Avant de commencer, j'aimerais clarifier quelques points qui m'ont confus lorsque j'ai commencé à travailler avec les React Hooks.

#### **useReducer et Context**

J'étais un peu confus au début par useReducer. Je pensais qu'en utilisant simplement useReducer, j'aurais automatiquement imité la fonctionnalité Redux et aurais un état global. Ce n'est pas le cas. C'est Context qui rend notre état global. Context peut être utilisé avec useReducer et useState.

> **état global** : signifie que l'état persiste d'un composant à un autre. Si vous avez changé l'état dans un composant et que vous êtes passé à un autre composant, l'état serait sauvegardé s'il est global. Si l'état est local et que vous êtes passé à un autre composant, l'état ne serait pas sauvegardé.

#### **Quand utiliser l'état local ou global et useState et useReducer**

À des fins pédagogiques, je vais vous montrer les quatre combinaisons possibles d'état local et global avec useState et useReducer. Dans une vraie application, j'utiliserais le hook useReducer pour les états globaux complexes, tels que l'authentification et le stockage des données d'un serveur. J'utiliserais le hook useState pour les états locaux plus simples, comme l'ouverture et la fermeture d'une modale.

#### **Comment fonctionne Context**

![Image](https://cdn-media-1.freecodecamp.org/images/vKxyeIoOimtSIC3gy9nk7N-BdBtTHySC2t2J)

Context précède les hooks React et est un moyen de transmettre des props à des composants enfants profondément imbriqués. Sans context, les props devraient être transmises à chaque composant intermédiaire pour atteindre le composant enfant visé.

Context a résolu ce problème en permettant de passer une prop au composant parent. Ensuite, elle serait disponible pour tous les composants enfants automatiquement. Vous n'aviez pas à la transmettre à travers des composants intermédiaires. Et c'est essentiellement comment nous avons un état global. En utilisant le Context dans le composant racine, notre état est disponible pour tous les composants enfants. Puisque App.js est le composant racine, et que tous les autres composants sont des composants enfants, l'état que nous avons défini dans App.js est disponible pour tous les composants.

Il est important de garder à l'esprit que tout l'état est contenu, initialisé et mis à jour dans le fichier App.js. Vous pouvez appeler une fonction pour changer l'état depuis un composant enfant, mais il est finalement mis à jour dans le fichier App.js.

### **Structure du répertoire et introduction**

Au lieu de me concentrer sur la façon de construire cette application étape par étape, je vais plutôt me concentrer davantage sur les différences entre la classe React-Redux et les hooks React.

Voici quelques acronymes que j'utilise et leur signification

**uS** = useState signifie lorsqu'une chose utilise le hook useState

**uR** = useReducer signifie lorsqu'une chose utilise le hook useReducer

![Image](https://cdn-media-1.freecodecamp.org/images/730bBk8D8F5zEDgkhYE0X5XP6ZXCvrK7droc)

Voici la structure du répertoire. Il s'agit d'une application très basique qui contient :

* 1 classe React-Redux
* 1 composant fonctionnel React qui utilise les hooks useState, useReducer et useContext
* Actions et types d'actions
* Reducers à utiliser avec les hooks React
* Reducers à utiliser avec React-Redux
* un fichier Context
* Le fichier racine App.js

#### **L'objet Context**

J'aime avoir le context dans son propre fichier puisque vous devez l'importer dans chaque composant enfant que vous utilisez avec le hook `useContext()`. Nous n'avons pas besoin de faire autre chose pour configurer l'objet Context, nous avons juste besoin de cette fonction.

```javascript

import React from 'react';

const Context = React.createContext()

export default Context;
```

Remarquez également que nous ne passons aucune valeur d'état à l'objet Context. Vous pouvez voir d'autres tutoriels qui passent des valeurs à la fonction `createContext()`. Cela est inutile car nous allons remplacer ces valeurs lorsque nous configurerons le `<Context.Provider />` et passerons l'état à la prop `value`.

#### **Reducers et Actions**

Maintenant, je vais montrer un reducer pour une utilisation avec les hooks React et un autre pour une utilisation avec React Redux.

Reducer pour une utilisation avec les hooks React :

```javascript

import * as ACTION_TYPES from '../actions/action_types'

export const initialState = {
  hooks_stateprop1: false,
}

export const Reducer1 = (state = initialState, action) => {
    switch(action.type) {
      case ACTION_TYPES.SUCCESS:
        return {
          ...state,
          hooks_stateprop1: true,
        }
      case ACTION_TYPES.FAILURE:
        return {
          ...state,
          hooks_stateprop1: false,
        }
      default:
        throw new Error();
    }
}
```

Reducer pour React Redux :

```javascript
import * as ACTION_TYPES from '../actions/action_types'

const initialState = {
  stateprop1: false
}

const Reducer1 = (state = initialState, action) => {
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

export default Reducer1;
```

Remarquez que dans le reducer des hooks React, nous exportons à la fois l'initialState et le reducer. Nous n'utilisons pas `export default` à la fin. Dans le reducer React Redux, nous faisons un `export default` du reducer.

Ensuite, nous avons nos actions et types d'actions :

```javacript
export const SUCCESS = "SUCCESS"

export const FAILURE = "FAILURE"

...
```

```javascript

import * as ACTION_TYPES from './action_types'

export const SUCCESS = {
  type: ACTION_TYPES.SUCCESS
}

export const FAILURE = {
  type: ACTION_TYPES.FAILURE
}

export const success = () => {
  return {
    type: ACTION_TYPES.SUCCESS
  }
}

export const failure = () => {
  return {
    type: ACTION_TYPES.FAILURE
  }
}
...
```

Les actions et les créateurs d'actions ne nécessitent aucun changement depuis React Redux.

#### **Lecture et mise à jour de l'état dans React Redux vs React Hooks**

Avec les informations préliminaires écartées, nous pouvons maintenant regarder les fichiers `hooks_container1.js` et `container1.js` et voir les différences entre React Hooks et React Redux dans le code.

Commençons par regarder l'état local pour chacun et voyons comment vous implémenteriez un simple compteur.

**React-Redux**

```javascript
class Container1 extends Component {
    constructor(props) {
      super(props)

      this.state = {
        local_state_prop1: true,
        local_state_prop2: 0,
        cDM_value: ''
      }
    }

 ...
 
    inc_local = () => {
      this.setState({local_state_prop2: this.state.local_state_prop2 + 1})
    }

    dec_local = () => {
      this.setState({local_state_prop2: this.state.local_state_prop2 - 1})
    }
 
  ...
    <button onClick={() => this.inc_local()}> INC Local State  </button>
    <button onClick={() => this.dec_local()}> DEC Local State  </button>
    <br />
    <br />
      {this.state.local_state_prop2}
    <br />
 ...
    
 
```

**React Hooks**

```javascript


const HooksContainer1 = () => {
    const [value, setValue] = useState({local_state_prop1: true,
                                        local_state_prop2: 0
                                       })
  
...    
    const incrementValue_uS = () => {
      setValue({...value, local_state_prop2: value.local_state_prop2 + 1} )
    }

    const decrementValue_uS = () => {
      setValue({...value, local_state_prop2: value.local_state_prop2 - 1} )
    }
    
...

      <button onClick={() => incrementValue_uS()}> Add Local Value uS </button>
      <button onClick={() => decrementValue_uS()}> Dec Local Value uS</button>
      <br />
      <p>Local useState Value: {value.local_state_prop2}</p>
      <br />
 ...
```

La première chose à noter est que nous passons d'un composant de classe dans React Redux à un composant fonctionnel dans React Hooks. C'est pourquoi nous n'avons pas le mot-clé "this" dans notre code React Hooks. Puisque nous ne sommes pas dans une classe, nous pouvons référencer les noms de variables et de fonctions directement.

Dans React Redux, nous initialisons l'état dans le constructeur et avons une fonction `setState()` dédiée. "state" et "setState()" sont des noms réservés.

Ce n'est pas le cas dans les hooks React. Dans les hooks React, nous créons notre propre mot-clé "state" et notre propre fonction setState() avec le hook useState(). Dans l'exemple ci-dessus, vous pouvez considérer `value` comme l'équivalent de `this.state` dans un composant de classe. Et similaire à `this.state`, nous utilisons la notation par points pour accéder à chaque propriété individuelle de l'état, donc la syntaxe que nous utiliserons sera :

```
 value.name_of_property
```

Lorsque j'ai commencé à apprendre les hooks, je confondais souvent le hook `useState()` avec la fonction `setState()` de React Redux. Ce n'est pas le cas. La fonction `setState()` de React Redux est équivalente au deuxième élément dans la destructuration du tableau. Dans l'exemple ci-dessus, il s'agit de `setValue()`. Cette fonction `setValue()` est la façon dont nous mettons à jour notre état avec les hooks. `useState()` est alors simplement une façon d'initialiser la capacité de lire et de mettre à jour l'état dans un composant fonctionnel. Cela était auparavant uniquement disponible pour les composants de classe.

#### **Fusion de l'ancien état dans React Hooks**

Une autre chose importante à remarquer dans l'exemple React Hooks est que j'utilise `...value` avant de mettre à jour l'état dans les fonctions d'incrémentation et de décrémentation. Il s'agit de l'opérateur de propagation, qui passe tout l'état précédent aplati à la fonction setState().

Je n'ai pas eu besoin de passer l'état précédent dans l'exemple React Redux. Lorsque nous mettons à jour une propriété d'état dans React Redux, la nouvelle propriété d'état est automatiquement fusionnée avec les anciennes propriétés d'état.

Cela **ne se produit pas** dans React Hooks. Lorsque vous mettez à jour l'état dans React Hooks, un nouvel état est créé. Vous voyez dans l'exemple React Hooks que nous avons 2 propriétés d'état : `local_state_prop1` et `local_state_prop2`. Si nous mettons à jour l'état avec seulement `local_state_prop2` et que nous ne passons pas `...value`, alors un nouvel état sera créé qui n'a que `local_state_prop2`. Cela signifie que notre `local_state_prop1` sera simplement supprimé.

Ainsi, lors de la conversion de l'état de React Redux vers React Hooks, vous devrez passer tout l'état précédent avec l'opérateur de propagation lors de la mise à jour d'une seule propriété d'état.

#### **Lecture et mise à jour de l'état avec useReducers et Redux Reducers**

Nous pouvons maintenant comparer la lecture et la mise à jour de l'état avec useReducer et Reducers.

Nous utilisons le même reducer que dans l'exemple précédent. Un reducer avec des types d'actions `SUCCESS` et `FAILURE` qui change `stateprop1` de vrai à faux et vice versa.

useReducer Hook

```javascript
import * as Reducer1 from '../store/hooks_reducers/reducer1_hooks';

...
const HooksContainer1 = () => {
      const [stateLocal1, dispatchLocal1] = useReducer(Reducer1.Reducer1,
                                                     Reducer1.initialState)
    
...

    const action1 = () => {
      //    dispatchLocal1({type: "SUCCESS"})
      //  dispatchLocal1(ACTIONS.success())
          dispatchLocal1(ACTIONS.SUCCESS)

    }

    const action2 = () => {
      //   dispatchLocal1({type: "FAILURE"})
      //   dispatchLocal1(ACTIONS.failure())
           dispatchLocal1(ACTIONS.FAILURE)

    }
 ...
 
    <button onClick={() => action1()}>Dispatch Action 1  </button>
    <button onClick={() => action2()}>Dispatch Action 2 </button>
      <br />
      {stateLocal1.stateprop1
        ? <p> stateprop1 is true </p>
        : <p> stateprop1 is false </p>
      }
      <br />
...
```

React Redux

```javascript
...

function mapStateToProps(state) {
  return {
    stateprop1: state.reducer1.stateprop1,
  }
}

function mapDispatchToProps(dispatch) {
  return {
    // action_creator1: () => dispatch(ACTIONS.success()),
    // action_creator2: () => dispatch(ACTIONS.failure()),
    // action_type1: () => dispatch({type: "SUCCESS"}),
    // action_type2: () => dispatch({type: "FAILURE}),
    action1: () => dispatch(ACTIONS.SUCCESS),
    action2: () => dispatch(ACTIONS.FAILURE),
  }
}

...

  <button onClick={() => this.props.action1()}> Dispatch Action 1 </button>
  <button onClick={() => this.props.action2()}>Dispatch Action 2 </button>
  <br />
  {this.props.stateprop1
    ? <p> stateprop1 is true </p>
    : <p> stateprop1 is false </p>
  }
  <br />
...
```

Comme mentionné dans l'introduction, même si nous utilisons `useReducer()` dans le composant fonctionnel, nous ne mettons toujours à jour que l'état local du composant. Je vais vous montrer comment imiter la fonctionnalité Redux avec Context et avoir un état global dans la section suivante. Il est important de garder à l'esprit que nous ne mettons toujours à jour que l'état local ici dans notre conteneur de hooks, même si nous utilisons des actions et des reducers.

D'autre part, dans notre composant de classe React, nous mettons à jour l'état global puisque nous utilisons Redux.

La première différence que vous remarquerez avec useReducer est que nous devons importer notre reducer et notre état initial et les passer dans le hook useReducer, ce que nous ne faisons pas avec React Redux. Dans React Redux, nous utilisons simplement la fonction `connect()`.

#### **Lecture de l'état et dispatch des actions**

Ensuite, pour dispatcher des actions dans React Hooks, nous utilisons une fonction fléchée puis nous dispatchons nos actions dans le corps de la fonction. Vous pouvez dispatcher des actions directement dans l'événement `onClick()`, mais avoir le dispatch dans une fonction rendra votre code plus lisible.

Dans React Redux, nous définissons des propriétés dans la fonction `mapDispatchToProps()`, puis chaque propriété est une fonction fléchée qui dispatch des actions.

Vous remarquerez que nous passons les actions et les créateurs d'actions de la même manière à la fonction dispatch dans React Hooks et React Redux. Il n'y a littéralement aucune différence, c'est pourquoi nous n'avons pas eu besoin de changer nos actions du tout. J'ai inclus toutes les façons de dispatcher des actions en commentaire.

La seule différence entre React Hooks et React Redux est que le nom de la fonction "dispatch" est réservé dans React Redux. Dans React Hooks, nous créons notre propre nom de fonction "dispatch" via le hook useReducer.

Pour appeler la fonction dispatch dans React Redux, nous utilisons la syntaxe `this.props` puis le nom de la propriété dans la fonction `mapDispatchToProps()`. Dans React Hooks, nous appelons simplement le nom de la fonction dispatch directement.

Pour lire l'état dans React Redux, nous faisons `this.props` puis le nom de la propriété dans la fonction `mapStateToProps()`. Le nom de la propriété contient la valeur pour une propriété spécifique dans un reducer spécifique. Dans React Hooks, nous faisons simplement le nom de la valeur de l'état. Il s'agit du premier élément dans la destructuration du tableau dans l'appel du hook useReducer. Ensuite, le nom de la propriété que nous avons définie dans l'initialState dans le reducer.

#### **Context avec useState**

Maintenant, je vais passer en revue Context, qui est la façon dont nous configurons un état global. Il est important de noter que Context ne fait pas partie des React Hooks. `useContext()` est un hook React, mais Context lui-même ne fait pas partie des React Hooks. Context est simplement un moyen de transmettre des props d'un composant parent à un composant enfant profondément imbriqué. Voir la section "Comment fonctionne Context" au début de ce tutoriel pour une explication complète.

De plus, je ne ferai pas de comparaisons entre React Redux et Context car Context n'a pas d'opposé dans React Redux. Je vais vous montrer comment implémenter un état global avec Context en utilisant à la fois le hook `useReducer()` et `useState()`.

Nous allons d'abord commencer par utiliser le hook `useState()` pour configurer un état global.

Nous allons commencer à configurer notre état global dans le fichier racine App.js. Nous allons d'abord importer l'objet Context que nous avons configuré dans le fichier `context.js`. Nous aurons également besoin d'importer notre composant fonctionnel Hooks.

```javascript

import Context from '../utils/context';
import HooksContainer1 from './hooks/hooks_container1';
...

const App = () => {
    const [valueGlobal_uS, setValueGlobal_uS] = useState(0)
    
    const incrementValueGlobal_uS = () => {
      setValueGlobal_uS(valueGlobal_uS + 1 )
    }

    const decrementValueGlobal_uS = () => {
      setValueGlobal_uS(valueGlobal_uS - 1 )
    }
    
...    
    
    <div>
     <Context.Provider
          value={{
            //global state with useState
            valueGlobalState_uS: valueGlobal_uS,
            addGlobalValue_uS: () => incrementValueGlobal_uS(),
            decGlobalValue_uS: () => decrementValueGlobal_uS(),
          }}>
        <HooksContainer1 />
      </Context.Provider>
     </div>
...
```

Nous pouvons simplement configurer un simple compteur pour l'instant. Notre hook `useState()` est configuré comme d'habitude. Dans notre JSX, nous enveloppons notre `<HooksContainer1 />` avec l'élément `<Context.Provider />`. C'est ce qui nous permet de passer l'état de App.js aux composants enfants. Nous avons également 3 propriétés fournies à notre prop `value`. 1 pour contenir la valeur de l'état et 2 propriétés pour changer l'état. Remarquez que nous n'utilisons pas le hook `useContext()` dans App.js. Le hook `useContext()` sera en fait utilisé dans les composants enfants pour lire et mettre à jour l'état.

Vous pouvez essentiellement penser à la prop `value` comme étant à la fois les fonctions `mapStateToProps()` et `mapDispatchToProps()` combinées en une seule, car la prop `value` contient des propriétés qui vous permettent de lire et de mettre à jour l'état qui peuvent être appelées et accessibles par le composant enfant, ce qui est exactement ce que font les fonctions `mapStateToProps()` et `mapDispatchToProps()`.

Maintenant, regardons comment nous utiliserions cet objet Context dans un composant enfant.

```javascript

import Context from '../utils/context';

...
const HooksContainer1 = () => {
  
...
    const context = useContext(Context)


    <p>Global useState Value: {context.valueGlobalState_uS}</p>

    <button onClick={() => context.addGlobalValue_uS()}> Add Global Value uS </button>
    <button onClick={() => context.decGlobalValue_uS()}> Dec Global Value uS </button>

...
```

Nous devons d'abord importer notre objet Context en haut. Il s'agit de l'objet Context original que nous avons créé avec la fonction `createContext()`, et non le `<Context.Provider />` que nous venons de configurer. Ensuite, nous passons simplement cet objet Context au hook `useContext()` et l'enregistrons dans une variable. Cette variable context a maintenant toutes les propriétés que nous venons de définir dans la prop `value` du `<Context.Provider />`.

Pour accéder aux propriétés de la prop `value`, nous pouvons simplement utiliser la notation par points. Par exemple, pour accéder à la valeur de l'état ici dans notre composant enfant, nous utilisons la syntaxe `context.valueGlobalstate_uS`.

Notez que `valueGlobalState` est le nom de la _propriété_ que nous avons définie dans le fichier App.js dans la prop value. `valueGlobalState` est la propriété qui contient la valeur de l'état que nous avons définie dans App.js comme `valueGlobal_uS`. De même, pour changer l'état, nous appelons le nom de la propriété et non le nom de la fonction que nous avons définie dans App.js.

J'ai intentionnellement gardé les noms des propriétés et des fonctions différents pour qu'il soit plus facile de voir comment Context fonctionne dans le composant enfant.

C'est tout pour l'utilisation de Context avec useState. Je vais maintenant démontrer avec useReducer.

#### **Context avec useReducer**

L'utilisation de Context avec useReducer est essentiellement la façon dont nous obtenons la fonctionnalité Redux.

Afin d'éviter la confusion, je vais configurer un nouveau reducer et des actions pour cela.

```javascript

export const CONTEXT_INC = "CONTEXT_INC"

export const CONTEXT_DEC = "CONTEXT_DEC"
```

```javascript
export const CONTEXT_INC = {
  type: ACTION_TYPES.CONTEXT_INC
}

export const CONTEXT_DEC = {
  type: ACTION_TYPES.CONTEXT_DEC
}
```

```javascript
import * as ACTION_TYPES from '../actions/action_types'

export const initialState = {
  context_prop1: 0,
}

export const ContextReducer = (state = initialState, action) => {
    switch(action.type) {
      case ACTION_TYPES.CONTEXT_INC:
        return {
          ...state,
          context_prop1: state.context_prop1 + 1
        }
      case ACTION_TYPES.CONTEXT_DEC:
        return {
          ...state,
          context_prop1: state.context_prop1 - 1
        }
      default:
        throw new Error();
    }
}
```

Nous avons donc un simple reducer qui fonctionne comme un compteur. Maintenant, nous pouvons configurer le hook useReducer dans notre fichier App.js et nous allons le configurer de la même manière que nous avons configuré useReducer dans notre conteneur de hooks. Nous importons le ContextReducer et son état initial et les passons dans le hook useReducer dans App.js. Parce que nous utilisons maintenant Context, nous n'importerons pas notre Context Reducer dans les composants enfants. L'état sera changé ici dans notre fichier App.js et sera simplement transmis comme props.

```javascript
import * as ACTIONS from './store/actions/actions';
import * as ContextReducer from './store/reducers/context_reducer';

...

const App = () => {

...

    const [contextState, contextDispatch] = useReducer(ContextReducer.ContextReducer,
                                                       ContextReducer.initialState)
                                                       
    const dispatchContextInc = () => {
      contextDispatch(ACTIONS.CONTEXT_INC)
    }

    const dispatchContextDec = () => {
      contextDispatch(ACTIONS.CONTEXT_DEC)
    }
 ...
 
 
       <div>
      <Context.Provider
          value={{
            //global state with useState
            valueGlobalState_uS: valueGlobal_uS,
            addGlobalValue_uS: () => incrementValueGlobal_uS(),
            decGlobalValue_uS: () => decrementValueGlobal_uS(),

            //global state with useReducer
            valueGlobalState_uR: contextState,
            addGlobalValue_uR: () => dispatchContextInc(),
            decGlobalValue_uR: () => dispatchContextDec()
          }}>
              <HooksContainer1 />
          </Context.Provider>
        </div>
...
```

Nous avons configuré nos propriétés dans la prop `value` de la même manière que lorsque nous avons utilisé Context avec le hook `useState()`. Les actions sont également dispatchées de la même manière que nous l'avons vu précédemment.

Maintenant, pour notre composant enfant :

```javascript
...

const HooksContainer1 = () => {
  
 const context = useContext(Context)
 
...

 <button onClick={() => context.addGlobalValue_uR()}> Add Global Value uR </button>
 <button onClick={() => context.decGlobalValue_uR()}> Dec Global Value uR </button>

 <p>Global useReducer Value: {context.valueGlobalState_uR.context_prop1}</p>
```

Comme vous pouvez le voir, la lecture et la mise à jour de l'état avec le hook `useReducer()` sont très similaires à l'exemple `useState()`. Nous pouvons même utiliser la même variable context que nous avons utilisée pour `useState()`, nous n'avons pas à en initialiser une autre. Pour mettre à jour l'état, nous appelons simplement le nom de la propriété que nous avons définie dans la prop `value` du provider. Cela met à jour l'état dans App.js. Parce que nous mettons à jour notre état dans App.js, nous n'avons pas à importer le ContextReducer ici dans notre composant enfant et à le passer dans le hook `useReducer()`.

La lecture de l'état est un peu différente. Puisque `valueGlobalState_uR` contient tout notre état, nous devons spécifier une seule propriété de l'état qui, dans ce cas, est `context_prop1`.

Et c'est tout ! Après cela, vous pouvez lire et mettre à jour l'état dans n'importe quel composant de votre application en utilisant ce même modèle, ce qui vous permet d'imiter essentiellement la fonctionnalité Redux.

Pour une version vidéo 100% gratuite de ce tutoriel et un contenu plus approfondi sur les React Hooks, consultez mon cours Udemy ou ma playlist YouTube :

[https://www.udemy.com/react-hooks-with-react-redux-migration](https://www.udemy.com/react-hooks-with-react-redux-migration)

[https://www.youtube.com/watch?v=l8ODM-KoDpA&list=PLMc67XEAt-ywplHhDpoj5vakceZNr8S0B](https://www.youtube.com/watch?v=l8ODM-KoDpA&list=PLMc67XEAt-ywplHhDpoj5vakceZNr8S0B)