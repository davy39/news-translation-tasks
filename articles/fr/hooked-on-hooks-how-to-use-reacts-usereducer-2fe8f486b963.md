---
title: 'Accro aux hooks : comment utiliser useReducer() de React'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-16T16:29:04.000Z'
originalURL: https://freecodecamp.org/news/hooked-on-hooks-how-to-use-reacts-usereducer-2fe8f486b963
coverImage: https://cdn-media-1.freecodecamp.org/images/1*YxApEKMTlenh-lDQ-uWvJw.jpeg
tags:
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: 'Accro aux hooks : comment utiliser useReducer() de React'
seo_desc: 'By Adeel Imran


  _Photo by [Unsplash](https://unsplash.com/@sebastian_unrau?utm_source=ghost&utm_medium=referral&utm_campaign=api-credit">Sebastian
  Unrau / <a href="https://unsplash.com/?utm_source=ghost&utm_medium=referral&utmcampaign=api-credit)

  So ...'
---

Par Adeel Imran

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-248.png)
_Photo par [Unsplash](https://unsplash.com/@sebastian_unrau?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Sebastian Unrau</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

La conférence React vient de se terminer et, comme toujours, quelque chose de nouveau s'est produit. *Les hooks sont arrivés !* L'équipe React a parlé de suspense, de chargement paresseux, de rendu concurrent et de **_hooks_** :D.

%[https://www.youtube.com/watch?v=V-QO-KO90iQ]

Maintenant, je vais parler de mon hook préféré `useReducer` et de la manière de l'utiliser.

```
import React, { useReducer } from 'react';

const initialState = {
  loading: false,
  count: 0,
};

const reducer = (state, action) => {
  switch (action.type) {
    case 'increment': {
      return { ...state, count: state.count + 1, loading: false };
    }
    case 'decrement': {
      return { ...state, count: state.count - 1, loading: false };
    }
    case 'loading': {
      return { ...state, loading: true };
    }
    default: {
      return state;
    }
  }
};

const delay = (time = 1500) => {
  return new Promise(resolve => {
    setTimeout(() => {
      resolve(true);
    }, time);
  });
};

function PokemonInfo() {
  const [{ count, loading }, dispatch] = useReducer(reducer, initialState);
  const onHandleIncrement = async () => {
    dispatch({ type: 'loading' });
    await delay(500);
    dispatch({ type: 'increment' });
  };
  const onHandleDecrement = async () => {
    dispatch({ type: 'loading' });
    await delay(500);
    dispatch({ type: 'decrement' });
  };
  return (
    <div>
      <p>Compte {loading ? 'chargement..' : count}</p>
      <button type="button" onClick={onHandleIncrement}>
        +
      </button>
      <button type="button" onClick={onHandleDecrement}>
        -
      </button>
    </div>
  );
}

export default PokemonInfo;
```

Dans mon composant `PokemonInfo`, j'ai :

```
const [{ count, loading }, dispatch] = useReducer(reducer, initialState);
```

Ce qui est équivalent à :

```
const [state, dispatch] = useReducer(reducer, initialState);
const { count, loading } = state;
```

Alors, qu'est-ce que `const [state, dispatch] = useReducer(param1, param2)` ? Parlons d'abord de la **destructuration de tableau** qui se produit ci-dessous.

```
const [state, dispatch] = useReducer(initialState);
```

Voici un exemple de destructuration de tableau :

```
let myHeroes = ['Ant man', 'Batman']; // Mélange de DC & Marvel :D
let [marvelHero, dcHero] = myHeroes; // destructuration de tableau
/**
* myHeroes[0] == marvelHero => est 'Ant man'
* myHeroes[1] == dcHero => est 'Batman'
*/
```

Ainsi, la méthode `useReducer` a deux éléments dans son tableau `state` et `dispatch`. De plus, `useReducer` prend deux paramètres : l'un est `reducer` et l'autre est `initial-state`.

Dans le paramètre `reducer` de `useReducer`, je passe :

```
const reducer = (state, action) => {
  switch (action.type) {
    case 'increment': {
      return { ...state, count: state.count + 1, loading: false };
    }
    case 'decrement': {
      return { ...state, count: state.count - 1, loading: false };
    }
    case 'loading': {
      return { ...state, loading: true };
    }
    default: {
      return state;
    }
  }
};
```

Ce que cela fait, c'est qu'il prend deux arguments. L'un est l'état actuel du reducer et l'autre est l'action. Le `action.type` décide comment il va mettre à jour le reducer et retourner un nouvel état.

Donc, si `action.type === increment`

```
case 'increment': {      
  return { ...state, count: state.count + 1, loading: false };    
}
```

...il retournera l'état, qui aura son compte mis à jour à **+1** et loading défini à **false**. De plus, là où il est écrit `state.count + 1`, le `state` est en fait l'état précédent.

Dans le paramètre `initialState` de `useReducer`, je passe :

```
const initialState = {  
  loading: false,  
  count: 0
};
```

Donc, si c'est l'état initial, la méthode `useReducer` retourne deux éléments de son tableau, `state` et `dispatch`. La méthode `state` est un objet qui a deux clés `count & loading` que je destructure dans mon tableau destructuré.

Ainsi, je destructure un tableau, et à l'intérieur du tableau, je destructure un objet au premier index du tableau comme ci-dessous.

```
const [{ count, loading }, dispatch] = useReducer(reducer, initialState);
```

J'ai également une méthode appelée `delay`

```
// retourne true après 1500ms si l'argument time est passé.
const delay = (time = 1500) => {  
  return new Promise(resolve => {    
      setTimeout(() => {      
         resolve(true);    
      }, time);  
   });
};
```

Maintenant, dans ma méthode de rendu, lorsque je clique sur le bouton `+`

```
<button type="button" onClick={onHandleIncrement}>+</button>
```

la fonction `onHandleIncrement` est exécutée, ce qui fait ce qui suit :

```
const onHandleIncrement = async () => {    
   dispatch({ type: 'loading' });    
   await delay(500);    
   dispatch({ type: 'increment' });  
};
```

Elle définit initialement `loading` à true, ajoute un délai de `500ms` puis incrémente le compteur. Je sais que ce n'est pas un exemple de cas réel, mais cela explique comment fonctionne un reducer.

Dernière chose :

```
<p>Compte {loading ? 'chargement..' : count}</p>
```

Si `loading` est vrai, j'affiche `Compte chargement..` sinon j'affiche `Compte {value}`.

Voici à quoi cela ressemble dans l'UI :

![Image](https://cdn-media-1.freecodecamp.org/images/1*HFN4x5wAuyE6vYNkV6_tcA.gif)
_Exemple de compte utilisant le hook useReducer_

J'ai essayé de reproduire le code de [Dan Abramov](https://twitter.com/dan_abramov) qu'il a présenté à la React Conference 2018. Voici le lien vers le [**dépôt de code**](https://github.com/adeelibr/react-hooks-demo). Amusez-vous bien. :)

> Veuillez noter que les hooks sont dans une version alpha de React et ne sont en aucun cas conseillés pour une utilisation en production. Mais il est fort probable qu'ils deviennent une partie importante de l'écosystème à l'avenir. Vous devriez donc commencer à jouer avec les hooks React maintenant.