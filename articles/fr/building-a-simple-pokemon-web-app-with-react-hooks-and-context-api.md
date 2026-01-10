---
title: Comment créer une application Web Pokémon simple avec React Hooks et l'API
  Context
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-04-24T16:50:01.000Z'
originalURL: https://freecodecamp.org/news/building-a-simple-pokemon-web-app-with-react-hooks-and-context-api
coverImage: https://www.freecodecamp.org/news/content/images/2020/04/ash.gif
tags:
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: react hooks
  slug: react-hooks
- name: Web Development
  slug: web-development
seo_title: Comment créer une application Web Pokémon simple avec React Hooks et l'API
  Context
seo_desc: 'By TK

  After seven years of full stack development using Ruby, Python, and vanilla JavaScript,
  these days I mostly work with JavaScript, Typescript, React, and Redux.

  The JavaScript community is great and moves really fast. Tons of things are created
  ...'
---

Par TK

Après sept années de développement full stack en utilisant Ruby, Python et JavaScript vanilla, ces jours-ci je travaille principalement avec JavaScript, TypeScript, React et Redux.

La communauté JavaScript est géniale et évolue très rapidement. Des tonnes de choses sont créées "du jour au lendemain", généralement de manière figurative, mais parfois littéralement. Tout cela rend difficile de rester à jour.

J'ai toujours l'impression d'arriver en retard à la fête JavaScript. Et je veux y être, même si je n'aime pas vraiment les fêtes.

Après seulement un an de travail avec React et Redux, j'ai senti que je devais apprendre de nouvelles choses comme les Hooks et l'API Context pour gérer l'état. Après avoir lu quelques articles à ce sujet, j'ai voulu essayer ces concepts, alors j'ai créé un projet simple comme laboratoire pour expérimenter ces choses.

Depuis que je suis petit garçon, je suis passionné par Pokémon. C'était toujours amusant de jouer aux jeux sur Game Boy et de conquérir toutes les Ligues. Maintenant, en tant que développeur, je veux jouer avec l'[API Pokémon](https://pokeapi.co/).

J'ai décidé de créer une simple page web où je pourrais partager des données entre différentes parties de la page. La page aurait trois sections principales :

* Une boîte avec une liste de tous les pokémons existants
* Une boîte avec une liste de tous les pokémons capturés
* Une boîte avec une entrée pour ajouter de nouveaux pokémons à la liste

Et chaque boîte aurait le comportement ou les actions suivants :

* Pour chaque pokemon dans la première boîte, je peux les capturer et les envoyer dans la deuxième boîte
* Pour chaque pokemon dans la deuxième boîte, je peux les libérer et les envoyer dans la première boîte
* En tant que dieu du jeu, je suis capable de créer des pokémons en remplissant l'entrée et en les envoyant dans la première boîte

Ainsi, toutes les fonctionnalités que je voulais implémenter étaient claires – listes et actions.

## Lister les Pokémon

La fonctionnalité de base que je voulais construire en premier était de lister les pokémons. Donc pour un tableau d'objets, je voulais lister et afficher l'attribut `name` de chaque objet.

J'ai commencé avec la première boîte : les pokémons existants.

Au début, j'ai pensé que je n'avais pas besoin de l'API Pokémon – je pourrais simplement simuler la liste et voir si cela fonctionne. Avec `useState`, je peux déclarer l'état de mon composant et l'utiliser.

Nous le définissons avec une valeur par défaut d'une liste de pokémons simulée, juste pour le tester :

```javascript
const [pokemons] = useState([
  { id: 1, name: 'Bulbasaur' },
  { id: 2, name: 'Charmander' },
  { id: 3, name: 'Squirtle' }
]);

```

Ici, nous avons une liste de trois objets pokémons. Le hook `useState` fournit une paire d'éléments : l'état actuel et une fonction pour vous permettre de mettre à jour cet état créé.

Maintenant, avec l'état des pokémons, nous pouvons le mapper et rendre le nom de chacun.

```javascript
{pokemons.map((pokemon) => <p>{pokemon.name}</p>)}

```

C'est juste un map qui retourne le nom de chaque pokemon dans une balise de paragraphe.

Voici le composant entier implémenté :

```javascript
import React, { useState } from 'react';

const PokemonsList = () => {
  const [pokemons] = useState([
    { id: 1, name: 'Bulbasaur' },
    { id: 2, name: 'Charmander' },
    { id: 3, name: 'Squirtle' }
  ]);

  return (
    <div className="pokemons-list">
      <h2>Liste de Pokémons</h2>
      
      {pokemons.map((pokemon) =>
        <div key={`${pokemon.id}-${pokemon.name}`}>
          <p>{pokemon.id}</p>
          <p>{pokemon.name}</p>
        </div>)}
    </div>
  )
}

export default PokemonsList;

```

Juste un petit ajustement ici :

* J'ai ajouté la `key` dans une combinaison de l'`id` et du `name` du pokemon
* Et j'ai également rendu un paragraphe pour l'attribut `id` (je testais simplement. Mais nous le supprimerons plus tard.)

Super ! Maintenant, nous avons la première liste opérationnelle.

Je veux faire cette même implémentation mais maintenant pour les pokémons capturés. Mais pour les pokémons capturés, je veux d'abord créer une liste vide car lorsque le "jeu" commence, je n'aurai aucun pokemon capturé, n'est-ce pas ? Exactement !

```javascript
const [pokemons] = useState([]);

```

C'est tout, vraiment simple !

Le composant entier ressemble à l'autre :

```javascript
import React, { useState } from 'react';

const CapturedPokemons = () => {
  const [pokemons] = useState([]);

  return (
    <div className="pokedex">
      <h2>Pokémons Capturés</h2>

      {pokemons.map((pokemon) =>
        <div key={`${pokemon.id}-${pokemon.name}`}>
          <p>{pokemon.id}</p>
          <p>{pokemon.name}</p>
        </div>)}
    </div>
  )
}

export default CapturedPokemons;

```

Ici, nous utilisons `map`, mais comme le tableau est vide, il ne rend rien.

Maintenant que j'ai les deux composants principaux, je peux les utiliser ensemble dans le composant `App` :

```javascript
import React from 'react';
import './App.css';

import PokemonsList from './PokemonsList';
import Pokedex from './Pokedex';

const App = () => (
  <div className="App">
    <PokemonsList />
    <Pokedex />
  </div>
);

export default App;

```

## Capturer et Libérer

C'est la deuxième partie de notre application où nous pouvons capturer et libérer des pokémons. Alors, passons en revue le comportement attendu.

Pour chaque pokemon dans la liste des pokémons disponibles, je veux activer une action pour les capturer. L'action de capture les supprimera de la liste où ils se trouvaient et les ajoutera à la liste des pokémons capturés.

L'action de libération aura un comportement similaire. Mais au lieu de passer de la liste disponible à la liste capturée, ce sera l'inverse. Nous les déplacerons de la liste capturée à la liste disponible.

Ainsi, les deux boîtes doivent partager des données pour pouvoir ajouter des pokémons à l'autre liste. Comment faire cela alors qu'ils sont des composants différents dans l'application ? Parlons de l'API Context de React.

L'API Context a été conçue pour créer des données globales pour un arbre défini de composants React. Comme les données sont globales, nous pouvons les partager entre les composants de cet arbre défini. Alors, utilisons-la pour partager nos simples données Pokémon entre les deux boîtes.

Note mentale : "Le contexte est principalement utilisé lorsque certaines données doivent être accessibles par de nombreux composants à différents niveaux de nidification." - Documentation React.

En utilisant l'API, nous créons simplement un nouveau contexte comme ceci :

```javascript
import { createContext } from 'react';

const PokemonContext = createContext();

```

Maintenant, avec le `PokemonContext`, nous pouvons utiliser son fournisseur. Il fonctionnera comme un enveloppeur de composant d'un arbre de composants. Il fournit des données globales à ces composants et leur permet de s'abonner à tout changement lié à ce contexte. Cela ressemble à ceci :

```javascript
<PokemonContext.Provider value={/* une certaine valeur */}>

```

La propriété `value` est simplement une valeur que ce contexte fournit aux composants enveloppés. Que devons-nous fournir aux listes disponibles et capturées ?

* `pokemons` : pour lister dans la liste disponible
* `capturedPokemons` : pour lister dans la liste capturée
* `setPokemons` : pour pouvoir mettre à jour la liste disponible
* `setCapturedPokemons` : pour pouvoir mettre à jour la liste capturée

Comme je l'ai mentionné précédemment dans la partie `useState`, ce hook fournit toujours une paire : l'état et une fonction pour mettre à jour cet état. Cette fonction gère et met à jour l'état du contexte. En d'autres termes, ce sont les `setPokemons` et `setCapturedPokemons`. Comment ?

```javascript
const [pokemons, setPokemons] = useState([
  { id: 1, name: 'Bulbasaur' },
  { id: 2, name: 'Charmander' },
  { id: 3, name: 'Squirtle' }
]);

```

Maintenant, nous avons le `setPokemons`.

```javascript
const [capturedPokemons, setCapturedPokemons] = useState([]);

```

Et maintenant, nous avons aussi le `setCapturedPokemons`.

Avec toutes ces valeurs en main, nous pouvons maintenant les passer à la propriété `value` du fournisseur.

```javascript
import React, { createContext, useState } from 'react';

export const PokemonContext = createContext();

export const PokemonProvider = (props) => {
  const [pokemons, setPokemons] = useState([
    { id: 1, name: 'Bulbasaur' },
    { id: 2, name: 'Charmander' },
    { id: 3, name: 'Squirtle' }
  ]);

  const [capturedPokemons, setCapturedPokemons] = useState([]);

  const providerValue = {
    pokemons,
    setPokemons,
    capturedPokemons,
    setCapturedPokemons
  };

  return (
    <PokemonContext.Provider value={providerValue}>
      {props.children}
    </PokemonContext.Provider>
  )
};

```

J'ai créé un `PokemonProvider` pour envelopper toutes ces données et les API pour créer le contexte et retourner le fournisseur de contexte avec la valeur définie.

Mais comment fournissons-nous toutes ces données et API au composant ? Nous devons faire deux choses principales :

* Envelopper les composants dans ce fournisseur de contexte
* Utiliser le contexte dans chaque composant

Enveloppons-les d'abord :

```javascript
const App = () => (
  <PokemonProvider>
    <div className="App">
      <PokemonsList />
      <Pokedex />
    </div>
  </PokemonProvider>
);

```

Et nous utilisons le contexte en utilisant le `useContext` et en passant le `PokemonContext` créé. Comme ceci :

```javascript
import { useContext } from 'react';
import { PokemonContext } from './PokemonContext';

useContext(PokemonContext); // retourne la valeur du fournisseur de contexte que nous avons créée

```

Nous voulons pouvoir attraper les pokémons disponibles, donc il serait utile d'avoir la fonction API `setCapturedPokemons` pour mettre à jour les pokémons capturés.

À mesure que chaque pokemon est capturé, nous devons le supprimer de la liste disponible. `setPokemons` est également nécessaire ici. Et pour mettre à jour chaque liste, nous avons besoin des données actuelles. Donc, essentiellement, nous avons besoin de tout ce qui provient du fournisseur de contexte.

Nous devons construire un bouton avec une action pour capturer le pokemon :

* Balise `<button>` avec un `onClick` appelant la fonction `capture` et passant le pokemon

```javascript
<button onClick={capture(pokemon)}>+</button>

```

* La fonction `capture` mettra à jour les listes `pokemons` et `capturedPokemons`

```javascript
const capture = (pokemon) => (event) => {
  // mettre à jour la liste des pokémons capturés
  // mettre à jour la liste des pokémons disponibles
};

```

Pour mettre à jour les `capturedPokemons`, nous pouvons simplement appeler la fonction `setCapturedPokemons` avec les `capturedPokemons` actuels et le pokemon à capturer.

```javascript
setCapturedPokemons([...capturedPokemons, pokemon]);

```

Et pour mettre à jour la liste `pokemons`, il suffit de filtrer le pokemon qui sera capturé.

```javascript
setPokemons(removePokemonFromList(pokemon));

```

`removePokemonFromList` est juste une simple fonction pour filtrer le pokemon en supprimant le pokemon capturé.

```javascript
const removePokemonFromList = (removedPokemon) =>
  pokemons.filter((pokemon) => pokemon !== removedPokemon)

```

À quoi ressemble le composant maintenant ?

```javascript
import React, { useContext } from 'react';
import { PokemonContext } from './PokemonContext';

export const PokemonsList = () => {
  const {
    pokemons,
    setPokemons,
    capturedPokemons,
    setCapturedPokemons
  } = useContext(PokemonContext);

  const removePokemonFromList = (removedPokemon) =>
    pokemons.filter(pokemon => pokemon !== removedPokemon);

  const capture = (pokemon) => () => {
    setCapturedPokemons([...capturedPokemons, pokemon]);
    setPokemons(removePokemonFromList(pokemon));
  };

  return (
    <div className="pokemons-list">
      <h2>Liste de Pokémons</h2>
      
      {pokemons.map((pokemon) =>
        <div key={`${pokemon.id}-${pokemon.name}`}>
          <div>
            <span>{pokemon.name}</span>
            <button onClick={capture(pokemon)}>+</button>
          </div>
        </div>)}
    </div>
  );
};

export default PokemonsList;

```

Il ressemblera beaucoup au composant des pokémons capturés. Au lieu de `capture`, ce sera une fonction `release` :

```javascript
import React, { useContext } from 'react';
import { PokemonContext } from './PokemonContext';

const CapturedPokemons = () => {
  const {
    pokemons,
    setPokemons,
    capturedPokemons,
    setCapturedPokemons,
  } = useContext(PokemonContext);

  const releasePokemon = (releasedPokemon) =>
    capturedPokemons.filter((pokemon) => pokemon !== releasedPokemon);

  const release = (pokemon) => () => {
    setCapturedPokemons(releasePokemon(pokemon));
    setPokemons([...pokemons, pokemon]);
  };

  return (
    <div className="captured-pokemons">
      <h2>Pokémons Capturés</h2>

      {capturedPokemons.map((pokemon) =>
        <div key={`${pokemon.id}-${pokemon.name}`}>
          <div>
            <span>{pokemon.name}</span>
            <button onClick={release(pokemon)}>-</button>
          </div>
        </div>)}
    </div>
  );
};

export default CapturedPokemons;

```

## Réduire la complexité

Maintenant, nous utilisons le hook `useState`, l'API Context et le fournisseur de contexte `useContext`. Et surtout, nous pouvons partager des données entre les boîtes de pokémons.

Une autre façon de gérer l'état est d'utiliser `useReducer` comme alternative à `useState`.

Le cycle de vie du réducteur fonctionne comme suit : `useReducer` fournit une fonction `dispatch`. Avec cette fonction, nous pouvons dispatcher une `action` à l'intérieur d'un composant. Le `reducer` reçoit l'action et l'état. Il comprend le type d'action, gère les données et retourne un nouvel état. Maintenant, le nouvel état peut être utilisé dans le composant.

En tant qu'exercice et pour avoir une meilleure compréhension de ce hook, j'ai essayé de remplacer `useState` par celui-ci.

`useState` était à l'intérieur du `PokemonProvider`. Nous pouvons redéfinir l'état initial pour les pokémons disponibles et capturés dans cette structure de données :

```javascript
const defaultState = {
  pokemons: [
    { id: 1, name: 'Bulbasaur' },
    { id: 2, name: 'Charmander' },
    { id: 3, name: 'Squirtle' }
  ],
  capturedPokemons: []
};

```

Et passer cette valeur à `useReducer` :

```javascript
const [state, dispatch] = useReducer(pokemonReducer, defaultState);

```

`useReducer` reçoit deux paramètres : le reducer et l'état initial. Construisons le `pokemonReducer` maintenant.

Le reducer reçoit l'état actuel et l'action qui a été dispatchée.

```javascript
const pokemonReducer = (state, action) => // retourne le nouvel état basé sur le type d'action

```

Ici, nous obtenons le type d'action et retournons un nouvel état. L'action est un objet. Cela ressemble à ceci :

```javascript
{ type: 'UN_TYPE_D_ACTION' }

```

Mais pourrait aussi être plus grand :

```javascript
{
  type: 'UN_TYPE_D_ACTION',
  pokemon: {
    name: 'Pikachu'
  }
}

```

Dans ce cas, nous passerons un pokemon à l'objet action. Faisons une pause d'une minute et réfléchissons à ce que nous voulons faire à l'intérieur du reducer.

Ici, nous mettons généralement à jour les données et gérons les actions. Les actions sont dispatchées, donc les actions sont des comportements. Et les comportements de notre application sont _capture_ et _release_ ! Ce sont les actions que nous devons gérer ici.

Voici à quoi ressemblera notre reducer :

```javascript
const pokemonReducer = (state, action) => {
  switch (action.type) {
    case 'CAPTURE':
      // gérer la capture et retourner le nouvel état
    case 'RELEASE':
      // gérer la libération et retourner le nouvel état
    default:
      return state;
  }
};

```

Si notre type d'action est `CAPTURE`, nous le gérons d'une certaine manière. Si notre type d'action est `RELEASE`, nous le gérons d'une autre manière. Si le type d'action ne correspond à aucun de ces types, retournez simplement l'état actuel.

Lorsque nous capturons le pokemon, nous devons mettre à jour les deux listes : supprimer le pokemon de la liste disponible et l'ajouter à la liste capturée. Cet état est ce que nous devons retourner depuis le reducer.

```javascript
const getPokemonsList = (pokemons, capturedPokemon) =>
  pokemons.filter(pokemon => pokemon !== capturedPokemon)

const capturePokemon = (pokemon, state) => ({
  pokemons: getPokemonsList(state.pokemons, pokemon),
  capturedPokemons: [...state.capturedPokemons, pokemon]
});

```

La fonction `capturePokemon` retourne simplement les listes mises à jour. La fonction `getPokemonsList` supprime le pokemon capturé de la liste disponible.

Et nous utilisons cette nouvelle fonction dans le reducer :

```javascript
const pokemonReducer = (state, action) => {
  switch (action.type) {
    case 'CAPTURE':
      return capturePokemon(action.pokemon, state);
    case 'RELEASE':
      // gérer la libération et retourner le nouvel état
    default:
      return state;
  }
};

```

Maintenant, la fonction `release` !

```javascript
const getCapturedPokemons = (capturedPokemons, releasedPokemon) =>
  capturedPokemons.filter(pokemon => pokemon !== releasedPokemon)

const releasePokemon = (releasedPokemon, state) => ({
  pokemons: [...state.pokemons, releasedPokemon],
  capturedPokemons: getCapturedPokemons(state.capturedPokemons, releasedPokemon)
});

```

La fonction `getCapturedPokemons` supprime le pokemon libéré de la liste capturée. La fonction `releasePokemon` retourne les listes mises à jour.

Notre reducer ressemble maintenant à ceci :

```javascript
const pokemonReducer = (state, action) => {
  switch (action.type) {
    case 'CAPTURE':
      return capturePokemon(action.pokemon, state);
    case 'RELEASE':
      return releasePokemon(action.pokemon, state);
    default:
      return state;
  }
};

```

Juste un petit refactoring : les types d'action ! Ce sont des chaînes de caractères et nous pouvons les extraire dans une constante et les fournir au dispatcher.

```javascript
export const CAPTURE = 'CAPTURE';
export const RELEASE = 'RELEASE';

```

Et le reducer :

```javascript
const pokemonReducer = (state, action) => {
  switch (action.type) {
    case CAPTURE:
      return capturePokemon(action.pokemon, state);
    case RELEASE:
      return releasePokemon(action.pokemon, state);
    default:
      return state;
  }
};

```

Le fichier reducer entier ressemble à ceci :

```javascript
export const CAPTURE = 'CAPTURE';
export const RELEASE = 'RELEASE';

const getCapturedPokemons = (capturedPokemons, releasedPokemon) =>
  capturedPokemons.filter(pokemon => pokemon !== releasedPokemon)

const releasePokemon = (releasedPokemon, state) => ({
  pokemons: [...state.pokemons, releasedPokemon],
  capturedPokemons: getCapturedPokemons(state.capturedPokemons, releasedPokemon)
});

const getPokemonsList = (pokemons, capturedPokemon) =>
  pokemons.filter(pokemon => pokemon !== capturedPokemon)

const capturePokemon = (pokemon, state) => ({
  pokemons: getPokemonsList(state.pokemons, pokemon),
  capturedPokemons: [...state.capturedPokemons, pokemon]
});

export const pokemonReducer = (state, action) => {
  switch (action.type) {
    case CAPTURE:
      return capturePokemon(action.pokemon, state);
    case RELEASE:
      return releasePokemon(action.pokemon, state);
    default:
      return state;
  }
};

```

Comme le reducer est maintenant implémenté, nous pouvons l'importer dans notre fournisseur et l'utiliser dans le hook `useReducer`.

```javascript
const [state, dispatch] = useReducer(pokemonReducer, defaultState);

```

Comme nous sommes à l'intérieur du `PokemonProvider`, nous voulons fournir une certaine valeur aux composants consommateurs : les actions de capture et de libération.

Ces fonctions doivent simplement dispatcher le type d'action correct et passer le pokemon au reducer.

* La fonction `capture` : elle reçoit le pokemon et retourne une nouvelle fonction qui dispatch une action avec le type `CAPTURE` et le pokemon capturé.

```javascript
const capture = (pokemon) => () => {
  dispatch({ type: CAPTURE, pokemon });
};

```

* La fonction `release` : elle reçoit le pokemon et retourne une nouvelle fonction qui dispatch une action avec le type `RELEASE` et le pokemon libéré.

```javascript
const release = (pokemon) => () => {
  dispatch({ type: RELEASE, pokemon });
};

```

Maintenant, avec l'état et les actions implémentés, nous pouvons fournir ces valeurs aux composants consommateurs. Il suffit de mettre à jour la propriété value du fournisseur.

```javascript
const { pokemons, capturedPokemons } = state;

const providerValue = {
  pokemons,
  capturedPokemons,
  release,
  capture
};

<PokemonContext.Provider value={providerValue}>
  {props.children}
</PokemonContext.Provider>

```

Super ! Maintenant, retournons au composant. Utilisons ces nouvelles actions. Toutes les logiques de capture et de libération sont encapsulées dans notre fournisseur et reducer. Notre composant est maintenant très propre. Le `useContext` ressemblera à ceci :

```javascript
const { pokemons, capture } = useContext(PokemonContext);

```

Et le composant entier :

```javascript
import React, { useContext } from 'react';
import { PokemonContext } from './PokemonContext';

const PokemonsList = () => {
  const { pokemons, capture } = useContext(PokemonContext);

  return (
    <div className="pokemons-list">
      <h2>Liste de Pokémons</h2>
      
      {pokemons.map((pokemon) =>
        <div key={`${pokemon.id}-${pokemon.name}`}>
          <span>{pokemon.name}</span>
          <button onClick={capture(pokemon)}>+</button>
        </div>)}
    </div>
  )
};

export default PokemonsList;

```

Pour le composant des pokémons capturés, il ressemblera beaucoup au `useContext` :

```javascript
const { capturedPokemons, release } = useContext(PokemonContext);

```

Et le composant entier :

```javascript
import React, { useContext } from 'react';
import { PokemonContext } from './PokemonContext';

const Pokedex = () => {
  const { capturedPokemons, release } = useContext(PokemonContext);

  return (
    <div className="pokedex">
      <h2>Pokedex</h2>

      {capturedPokemons.map((pokemon) =>
        <div key={`${pokemon.id}-${pokemon.name}`}>
          <span>{pokemon.name}</span>
          <button onClick={release(pokemon)}>-</button>
        </div>)}
    </div>
  )
};

export default Pokedex;

```

Aucune logique. Juste de l'UI. Très propre.

## Pokémon Dieu – Le Créateur

Maintenant que nous avons la communication entre les deux listes, je veux construire une troisième boîte. Cela montrera comment créer de nouveaux pokémons. Mais ce n'est qu'une simple entrée et un bouton de soumission.

Lorsque nous ajoutons le nom d'un pokemon dans l'entrée et que nous appuyons sur le bouton, il dispatchera une action pour ajouter ce pokemon à la liste disponible.

Comme nous devons accéder à la liste disponible pour la mettre à jour, nous devons partager l'état. Donc, notre composant sera enveloppé par notre `PokemonProvider` avec les autres composants.

```javascript
const App = () => (
  <PokemonProvider>
    <div className="main">
      <PokemonsList />
      <Pokedex />
    </div>
    <PokemonForm />
  </PokemonProvider>
);

```

Construisons maintenant le composant `PokemonForm`. Le formulaire est assez simple :

```javascript
<form onSubmit={handleFormSubmit}>
  <input type="text" placeholder="nom du pokemon" onChange={handleNameOnChange} />
  <input type="submit" value="Ajouter" />
</form>

```

Nous avons un formulaire, une entrée et un bouton. En résumé, nous avons également une fonction pour gérer la soumission du formulaire et une autre fonction pour gérer le changement de l'entrée.

La fonction `handleNameOnChange` sera appelée chaque fois que l'utilisateur tape ou supprime un caractère. Je voulais créer un état local, une représentation du nom du pokemon. Avec cet état, nous pouvons l'utiliser pour dispatcher lors de la soumission du formulaire.

Comme nous voulons essayer les hooks, nous utiliserons `useState` pour gérer cet état local.

```javascript
const [pokemonName, setPokemonName] = useState();

const handleNameOnChange = (e) => setPokemonName(e.target.value);

```

Nous utilisons `setPokemonName` pour mettre à jour `pokemonName` chaque fois que l'utilisateur interagit avec l'entrée.

Et `handleFormSubmit` est une fonction pour dispatcher le nouveau pokemon à ajouter à la liste disponible.

```javascript
const handleFormSubmit = (e) => {
  e.preventDefault();
  addPokemon({
    id: generateID(),
    name: pokemonName
  });
};

```

`addPokemon` est l'API que nous construirons plus tard. Elle reçoit l'id et le nom du pokemon. Le nom est l'état local que nous avons défini, `pokemonName`.

`generateID` est juste une simple fonction que j'ai construite pour générer un nombre aléatoire. Cela ressemble à ceci :

```javascript
export const generateID = () => {
  const a = Math
    .random()
    .toString(36)
    .substring(2, 15)

  const b = Math
    .random()
    .toString(36)
    .substring(2, 15)

  return a + b;
};

```

`addPokemon` sera fourni par l'API de contexte que nous construisons. De cette façon, cette fonction peut recevoir le nouveau pokemon et l'ajouter à la liste disponible. Cela ressemble à ceci :

```javascript
const addPokemon = (pokemon) => {
  dispatch({ type: ADD_POKEMON, pokemon });
};

```

Il dispatchera ce type d'action `ADD_POKEMON` et passera également le pokemon.

Dans notre reducer, nous ajoutons le cas pour `ADD_POKEMON` et gérons l'état pour ajouter le nouveau pokemon à l'état.

```javascript
const pokemonReducer = (state, action) => {
  switch (action.type) {
    case CAPTURE:
      return capturePokemon(action.pokemon, state);
    case RELEASE:
      return releasePokemon(action.pokemon, state);
    case ADD_POKEMON:
      return addPokemon(action.pokemon, state);
    default:
      return state;
  }
};

```

Et la fonction `addPokemon` sera :

```javascript
const addPokemon = (pokemon, state) => ({
  pokemons: [...state.pokemons, pokemon],
  capturedPokemons: state.capturedPokemons
});

```

Une autre approche consiste à déstructurer l'état et à changer uniquement l'attribut du pokemon, comme ceci :

```javascript
const addPokemon = (pokemon, state) => ({
  ...state,
  pokemons: [...state.pokemons, pokemon],
});

```

De retour à notre composant, nous devons simplement nous assurer que le `useContext` fournit l'API de dispatch `addPokemon` basée sur le `PokemonContext` :

```javascript
const { addPokemon } = useContext(PokemonContext);

```

Et le composant entier ressemble à ceci :

```javascript
import React, { useContext, useState } from 'react';
import { PokemonContext } from './PokemonContext';
import { generateID } from './utils';

const PokemonForm = () => {
  const [pokemonName, setPokemonName] = useState();
  const { addPokemon } = useContext(PokemonContext);

  const handleNameOnChange = (e) => setPokemonName(e.target.value);

  const handleFormSubmit = (e) => {
    e.preventDefault();
    addPokemon({
      id: generateID(),
      name: pokemonName
    });
  };

  return (
    <form onSubmit={handleFormSubmit}>
      <input type="text" placeholder="nom du pokemon" onChange={handleNameOnChange} />
      <input type="submit" value="Ajouter" />
    </form>
  );
};

export default PokemonForm;

```

Maintenant, nous avons la liste des pokémons disponibles, la liste des pokémons capturés et la troisième boîte pour créer de nouveaux pokémons.

## Effets Pokémon

Maintenant que notre application est presque complète, nous pouvons remplacer la liste simulée de pokémons par une liste de pokémons provenant de la PokéAPI.

Ainsi, à l'intérieur du composant de fonction, nous ne pouvons pas faire d'effets secondaires comme le journalisation ou les abonnements. C'est pourquoi le hook `useEffect` existe. Avec ce hook, nous pouvons récupérer des pokémons (un effet secondaire) et les ajouter à la liste.

La récupération depuis la PokéAPI ressemble à ceci :

```javascript
const url = "https://pokeapi.co/api/v2/pokemon";
const response = await fetch(url);
const data = await response.json();
data.results; // [{ name: 'bulbasaur', url: 'https://pokeapi.co/api/v2/pokemon/1/' }, ...]

```

L'attribut `results` est la liste des pokémons récupérés. Avec ces données, nous pourrons les ajouter à la liste des pokémons.

Obtenons le code de la requête à l'intérieur de `useEffect` :

```javascript
useEffect(() => {
  const fetchPokemons = async () => {
    const response = await fetch(url);
    const data = await response.json();
    data.results; // mettre à jour la liste des pokémons avec ces données
  };

  fetchPokemons();
}, []);

```

Pour pouvoir utiliser `async-await`, nous devons créer une fonction et l'appeler plus tard. Le tableau vide est un paramètre pour s'assurer que `useEffect` connaît les dépendances qu'il recherchera pour se réexécuter.

Le comportement par défaut est d'exécuter l'effet à chaque rendu terminé. Si nous ajoutons une dépendance à cette liste, `useEffect` ne se réexécutera que lorsque la dépendance changera, au lieu de s'exécuter à chaque rendu terminé.

Maintenant que nous avons récupéré les pokémons, nous devons mettre à jour la liste. C'est une action, un nouveau comportement. Nous devons utiliser le dispatch à nouveau, implémenter un nouveau type dans le reducer et mettre à jour l'état dans le fournisseur de contexte.

Dans `PokemonContext`, nous avons créé la fonction `addPokemons` pour fournir une API au composant consommateur qui l'utilise.

```javascript
const addPokemons = (pokemons) => {
  dispatch({ type: ADD_POKEMONS, pokemons });
};

```

Elle reçoit des pokémons et dispatch une nouvelle action : `ADD_POKEMONS`.

Dans le reducer, nous ajoutons ce nouveau type, nous attendons les pokémons et nous appelons une fonction pour ajouter les pokémons à l'état de la liste disponible.

```javascript
const pokemonReducer = (state, action) => {
  switch (action.type) {
    case CAPTURE:
      return capturePokemon(action.pokemon, state);
    case RELEASE:
      return releasePokemon(action.pokemon, state);
    case ADD_POKEMON:
      return addPokemon(action.pokemon, state);
    case ADD_POKEMONS:
      return addPokemons(action.pokemons, state);
    default:
      return state;
  }
};

```

La fonction `addPokemons` ajoute simplement les pokémons à la liste :

```javascript
const addPokemons = (pokemons, state) => ({
  pokemons: pokemons,
  capturedPokemons: state.capturedPokemons
});

```

Nous pouvons refactoriser cela en utilisant la déstructuration de l'état et la notation abrégée de la valeur de la propriété de l'objet :

```javascript
const addPokemons = (pokemons, state) => ({
  ...state,
  pokemons,
});

```

Comme nous fournissons cette fonction API au composant consommateur maintenant, nous pouvons utiliser le `useContext` pour l'obtenir.

```javascript
const { addPokemons } = useContext(PokemonContext);

```

Le composant entier ressemble à ceci :

```javascript
import React, { useContext, useEffect } from 'react';
import { PokemonContext } from './PokemonContext';

const url = "https://pokeapi.co/api/v2/pokemon";

export const PokemonsList = () => {
  const { state, capture, addPokemons } = useContext(PokemonContext);

  useEffect(() => {
    const fetchPokemons = async () => {
      const response = await fetch(url);
      const data = await response.json();
      addPokemons(data.results);
    };    

    fetchPokemons();
  }, [addPokemons]);

  return (
    <div className="pokemons-list">
      <h2>Liste de Pokémons</h2>

      {state.pokemons.map((pokemon) =>
        <div key={pokemon.name}>
          <div>
            <span>{pokemon.name}</span>
            <button onClick={capture(pokemon)}>+</button>
          </div>
        </div>)}
    </div>
  );
};

export default PokemonsList;

```

## Conclusion

C'était ma tentative de partager ce que j'ai appris en essayant d'utiliser les hooks dans un mini projet secondaire.

Nous avons appris comment gérer l'état local avec `useState`, construire un état global avec l'API Context, comment réécrire et remplacer `useState` avec `useReducer`, et comment faire des effets secondaires avec `useEffect`.

Avertissement : ceci n'était qu'un projet expérimental à des fins d'apprentissage. Je n'ai peut-être pas utilisé les meilleures pratiques pour les hooks ou les rendre évolutifs pour de grands projets.

J'espère que cela a été une bonne lecture ! Continuez à apprendre et à coder !

Vous pouvez trouver d'autres articles comme celui-ci [sur mon blog](https://leandrotk.github.io/tk/2020/03/closure-currying-and-cool-abstractions/index.html).

Mon [Twitter](https://twitter.com/leandrotk_) et [Github](https://github.com/leandrotk).

## Ressources

* [Documentation React : Context](https://reactjs.org/docs/context.html)
* [Documentation React : Hooks](https://reactjs.org/docs/hooks-reference.html)
* [Projet secondaire Pokemon Hooks : code source](https://github.com/leandrotk/pokehooks-labs)
* [Apprendre React en construisant une App](https://alterclass.io/?ref=5ec57f513c1321001703dcd2)