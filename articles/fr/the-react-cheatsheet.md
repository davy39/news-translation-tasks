---
title: Le guide de référence React pour 2022
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2022-02-14T17:02:30.000Z'
originalURL: https://freecodecamp.org/news/the-react-cheatsheet
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/mugshotbot.com_customize_theme-two_up-mode-light-color-pink-pattern-bubbles-image-9129875b-url-https___freecodecamp.org.png
tags:
- name: cheatsheet
  slug: cheatsheet
- name: JavaScript
  slug: javascript
- name: React
  slug: react
seo_title: Le guide de référence React pour 2022
seo_desc: 'Do you want to get up to speed with React as quickly as possible?

  I’ve put together a super helpful cheatsheet to give you a complete overview of
  all of the React concepts you need to know in 2022.

  Click here to download the cheatsheet in PDF format....'
---

Vous voulez vous mettre à niveau avec React aussi rapidement que possible ?

J'ai préparé un guide de référence super utile pour vous donner un aperçu complet de tous les concepts React que vous devez connaître en 2022.

[Cliquez ici pour télécharger le guide de référence au format PDF](https://reedbarger.com/resources/the-react-cheatsheet-for-2021).

Il inclut toutes les informations essentielles de cet article sous forme de guide PDF pratique.

Commençons !

## Table des matières

* [Éléments React](#heading-react-elements)
* [Attributs des éléments React](#heading-react-element-attributes)
* [Styles des éléments React](#heading-react-element-styles)
* [Fragments React](#heading-react-fragments)
* [Composants React](#heading-react-components)
* [Props React](#heading-react-props)
* [Props Children React](#heading-react-children-props)
* [Conditionnels React](#heading-react-conditionals)
* [Listes React](#heading-react-lists)
* [Contexte React](#heading-react-context)
* [Hooks React](#heading-react-hooks)
* [Hook useState de React](#heading-react-usestate-hook)
* [Hook useEffect de React](#heading-react-useeffect-hook)
* [Hook useRef de React](#heading-react-useref)
* [Hook useContext de React](#heading-react-usecontext)
* [Hook useCallback de React](#heading-react-usecallback)
* [Hook useMemo de React](#heading-react-usememo)

## Éléments React

Les éléments React s'écrivent exactement comme des éléments HTML réguliers. Vous pouvez écrire n'importe quel élément HTML valide dans React.

```js
<h1>Mon En-tête</h1>
<p>Mon paragraphe>
<button>Mon bouton</button>

```

Nous écrivons les éléments React en utilisant une fonctionnalité appelée _JSX_.

Cependant, parce que JSX est vraiment juste des fonctions JavaScript (et non HTML), la syntaxe est un peu différente.

Contrairement à HTML, les éléments à balise unique (comme l'élément img), doivent être auto-fermants. Ils doivent se terminer par une barre oblique `/` :

```js
<img src="my-image.png" />
<br />
<hr />
```

## Attributs des éléments React

De plus, JSX nécessite une syntaxe différente pour ses attributs.

Puisque JSX est vraiment du JavaScript et que JavaScript utilise une convention de nommage en camelCase (c'est-à-dire, "camelCase"), les attributs sont écrits différemment de HTML.

L'exemple le plus courant est l'attribut `class`, que nous écrivons comme `className`.

```js
<div className="container"></div>

```

## Styles des éléments React

Pour appliquer des styles en ligne, au lieu d'utiliser des guillemets doubles (" "), nous utilisons deux ensembles d'accolades.

Les styles en ligne ne sont pas écrits comme de simples chaînes de caractères, mais comme des propriétés sur des objets :

```js
<h1 style={{ fontSize: 24, margin: '0 auto', textAlign: 'center' }}>Mon en-tête</h1>

```

## Fragments React

React nous donne également un élément appelé un _fragment_.

React exige que tous les éléments retournés soient retournés dans un seul composant "parent".

Par exemple, nous ne pouvons pas retourner deux éléments frères, comme un h1 et un paragraphe depuis un composant :

```
// cette syntaxe est invalide
function MyComponent() {
  return (
    <h1>Mon en-tête</h1>
    </p>Mon paragraphe</p>
  );
} 

```

Si nous ne voulons pas envelopper nos éléments dans un élément conteneur comme une div, nous pouvons utiliser un fragment :

```
// syntaxe valide
function MyComponent() {
  return (
    <>
      <h1>Mon en-tête</h1>
      </p>Mon paragraphe</p>
    </>
  );
} 

```

Nous pouvons écrire des fragments en syntaxe régulière ou abrégée : <React.Fragment></React.Fragment> ou <></>.

## Composants React

Nous pouvons organiser des groupes d'éléments en composants React.

Un composant de fonction de base est écrit de manière similaire à une fonction JavaScript régulière avec quelques différences.

1. Les noms des composants doivent commencer par une lettre majuscule (c'est-à-dire MyComponent, au lieu de myComponent)
2. Les composants, contrairement aux fonctions JavaScript, doivent retourner du JSX.

Voici la syntaxe de base d'un composant de fonction React :

```
function App() {
  return (
     <div>Bonjour le monde !</div>
  );
} 

```

## Props React

Les composants React peuvent accepter des données qui leur sont passées appelées _props_.

Les props sont passées du composant parent à un composant enfant.

Ici, nous passons une prop `name` de App au composant User.

```
function App() {
  return <User name="John Doe" />
}

function User(props) {
  return <h1>Bonjour, {props.name}</h1>; // Bonjour, John Doe !
}

```

Props est un objet, donc nous pouvons sélectionner la prop `name` dans `User` pour obtenir sa valeur.

> Pour intégrer une valeur dynamique (c'est-à-dire une variable ou une expression) dans JSX, vous devez l'envelopper dans des accolades.

Puisque nous utilisons uniquement la propriété `name` sur l'objet props, nous pouvons simplifier notre code avec la déstructuration d'objet :

```
function App() {
  return <User name="John Doe" />
}

function User({ name }) {
  return <h1>Bonjour, {name} !</h1>; // Bonjour, John Doe !
}

```

N'importe quelle valeur JavaScript peut être passée en tant que prop, y compris d'autres éléments et composants.

## Props Children React

Les props peuvent également être passées en plaçant des données entre les balises d'ouverture et de fermeture d'un composant.

Les props qui sont passées de cette manière sont placées sur la propriété `children`.

```
function App() {
  return (
   <User>
     <h1>Bonjour, John Doe !</h1>
   </User>
  );
}

function User({ children }) {
  return children; // Bonjour, John Doe !
}

```

## Conditionnels React

Les composants et éléments React peuvent être affichés de manière conditionnelle.

Une approche consiste à créer un retour séparé avec une instruction if.

```
function App() {
	const isAuthUser = useAuth();

  if (isAuthUser) {
    // si notre utilisateur est authentifié, laissez-le utiliser l'application
    return <AuthApp />;
  }

  // si l'utilisateur n'est pas authentifié, afficher un écran différent
  return <UnAuthApp />;
}

```

Si vous voulez écrire une conditionnelle dans une instruction de retour, cependant, vous devez utiliser une conditionnelle qui se résout en une valeur.

Pour utiliser l'opérateur ternaire, enveloppez toute la conditionnelle dans des accolades.

```
function App() {
	const isAuthUser = useAuth();

  return (
    <>
      <h1>Mon App</h1>
      {isAuthUser ? <AuthApp /> : <UnAuthApp />}
    </>
  ) 
}

```

## Listes React

Les listes de composants React peuvent être générées en utilisant la fonction `.map()`.

`.map()` nous permet de parcourir des tableaux de données et de générer du JSX.

Ici, nous générons une liste de joueurs de football en utilisant le composant SoccerPlayer.

```
function SoccerPlayers() {
  const players = ["Messi", "Ronaldo", "Laspada"];

  return (
    <div>
      {players.map((playerName) => (
        <SoccerPlayer key={playerName} name={playerName} />
      ))}
    </div>
  );
}

```

Lorsque vous parcourez un tableau de données, vous devez inclure la prop _key_ sur l'élément ou le composant que vous parcourez.

De plus, cette prop key doit recevoir une valeur unique, et non simplement un index d'élément.

Dans l'exemple ci-dessus, nous utilisons une valeur que nous savons être unique, qui est le `playerName`.

## Contexte React

Le contexte React nous permet de passer des données à notre arbre de composants sans utiliser de props.

Le problème avec les props est que parfois nous les passons à travers des composants qui n'ont pas besoin de les recevoir. Ce problème est appelé _props drilling_.

Voici un exemple simplifié de passage de props à travers un composant `Body` qui n'en a pas besoin :

```
function App() {
  return (
    <Body name="John Doe" />
  );
} 

function Body({ name }) {
  return (
    <Greeting name={name} />
  );
} 

function Greeting({ name }) {
  return <h1>Bienvenue, {name}</h1>;
}

```

> Avant d'utiliser Context, il est préférable de voir si nos composants peuvent être mieux organisés pour éviter de passer des props à travers des composants qui n'en ont pas besoin.

Pour utiliser Context, nous utilisons la fonction `createContext` de React.

Nous pouvons l'appeler avec une valeur initiale à mettre sur le contexte.

Le contexte créé inclut une propriété `Provider` et une propriété `Consumer`, qui sont chacune des composants.

Nous enveloppons le Provider autour de l'arbre de composants auquel nous voulons passer la valeur donnée. Ensuite, nous plaçons le Consumer dans le composant où nous voulons consommer la valeur.

```js
import { createContext } from 'react';

const NameContext = createContext('');

function App() {
  return (
    <NameContext.Provider value="John Doe">
      <Body />
    <NameContext.Provider>
  );
} 

function Body() {
  return <Greeting />;
} 

function Greeting() {
  return (
    <NameContext.Consumer>
      {name => <h1>Bienvenue, {name}</h1>}
    </NameContext.Consumer>
  );
}

```

## Hooks React

Les hooks React ont été introduits dans la version 16.8 de React comme un moyen d'ajouter facilement une logique réutilisable et étatique aux composants de fonction React.

Les hooks nous permettent d'utiliser toutes les fonctionnalités qui étaient auparavant disponibles uniquement dans les composants de classe.

De plus, nous pouvons créer nos propres hooks personnalisés qui donnent à notre application des fonctionnalités personnalisées.

De nombreux hooks React ont également été ajoutés à la bibliothèque principale de React. Nous allons couvrir les 6 hooks essentiels que vous devez absolument connaître :

* useState
* useEffect
* useRef
* useContext
* useCallback
* useMemo

## Hook useState de React

`useState` fait exactement ce qu'il dit—il nous permet d'utiliser des valeurs étatiques dans les composants de fonction.

useState est utilisé au lieu d'une simple variable car lorsque l'état est mis à jour, notre composant est réaffiché, généralement pour afficher cette valeur mise à jour.

Comme tous les hooks, nous appelons `useState` en haut de notre composant et pouvons lui passer une valeur initiale à mettre sur sa variable d'état.

Nous utilisons la déstructuration de tableau sur la valeur retournée par `useState` pour accéder (1) à l'état stocké et (2) à une fonction pour mettre à jour cet état.

```
import { useState } from 'react';

function MyComponent() {
  const [stateValue, setStateValue] = useState(initialValue);
}

```

Un exemple de base de l'utilisation de `useState` est d'incrémenter un compteur.

Nous pouvons voir le compte actuel à partir de la variable `count` et pouvons incrémenter l'état en passant `count + 1` à la fonction `setCount`.

```
import { useState } from 'react';

function Counter() {
  const [count, setCount] = useState(0);

  function updateCount() {
    setCount(count + 1);
  }

  return <button onClick={updateCount}>Le compte est : {count}</button>;
}

```

## Hook useEffect de React

Si nous voulons interagir avec le "monde extérieur", comme utiliser une API, nous utilisons le hook `useEffect`.

useEffect est utilisé pour effectuer un effet secondaire, ce qui signifie effectuer une opération qui existe en dehors de notre application et qui n'a pas de résultat prévisible.

La syntaxe de base de useEffect nécessite une fonction comme premier argument et un tableau comme deuxième argument.

```
import { useEffect } from 'react';

function MyComponent() {
   useEffect(() => {
     // effectuer l'effet secondaire ici
   }, []);
}

```

Si nous voulons récupérer des données, nous utiliserions `useEffect`, comme dans la récupération et l'affichage d'une liste de publications :

```
import { useEffect } from 'react';

function PostList() {
	 const [posts, setPosts] = useState([]);

   useEffect(() => {
	   fetch('https://jsonplaceholder.typicode.com/posts')
       .then(response => response.json())
       .then(posts => setPosts(posts));
   }, []);

   return posts.map(post => <Post key={post.id} post={post} />
}

```

Si nous devons utiliser une valeur qui provient de l'extérieur de la fonction d'effet, elle doit être incluse dans le tableau des dépendances.

Si cette valeur change, la fonction d'effet sera réexécutée.

Par exemple, voici un peu de code qui ajoute ou supprime la classe "overflow-hidden" à l'élément body chaque fois que le menu mobile est ouvert ou fermé.

```
function Mobile({ open }) {
  useEffect(() => {
    const body = document.querySelector("#__next");

    if (open) {
      body.classList.add("overflow-hidden");
    } else {
      body.classList.remove("overflow-hidden");
    }
  }, [open]);
 
  // ...
}

```

## React useRef

`useRef` nous permet d'obtenir un accès direct à un élément JSX.

Pour utiliser `useRef`, appelez-le, obtenez la valeur retournée et placez-la sur la prop `ref` pour un élément React donné.

> Les refs n'ont pas de prop intégrée sur les composants, seulement sur les éléments React.

Voici la syntaxe de base pour `useRef` :

```
import { useRef } from 'react';

function MyComponent() {
  const ref = useRef();

  return <div ref={ref} />
}

```

Une fois qu'une ref est attachée à un élément donné, nous pouvons utiliser la valeur stockée sur `ref.current` pour accéder à l'élément lui-même.

Par exemple, si nous voulions écrire du code qui met en focus une entrée de recherche lorsque les utilisateurs utilisent la combinaison de touches Control + K.

```
import { useWindowEvent } from "@mantine/hooks";
import { useRef } from "react";

function Header() {
	const inputRef = useRef();

  useWindowEvent("keydown", (event) => {
    if (event.code === "KeyK" && event.ctrlKey) {
      event.preventDefault();
      inputRef.current.focus();
    }
  });
  
  return <input ref={inputRef} />
}

```

## React useContext

`useContext` fournit un moyen plus facile de consommer le contexte que d'utiliser le composant standard Context.Consumer.

La syntaxe implique de passer l'objet Context entier que nous voulons consommer dans `useContext`. La valeur retournée est la valeur passée au Context.

```
import { useContext } from 'react';

function MyComponent() {
  const value = useContext(Context);

  // ...
}

```

Pour réécrire notre exemple précédent, en utilisant le hook `useContext` :

```js
import { createContext, useContext } from 'react';

const NameContext = createContext('');

function App() {
  return (
    <NameContext.Provider value="John Doe">
      <Body />
    <NameContext.Provider>
  );
} 

function Body() {
  return <Greeting />;
} 

function Greeting() {
	const name = useContext(NameContext);

  return (
    <h1>Bienvenue, {name}</h1>
  );
}

```

## React useCallback

`useCallback` est un hook que nous utilisons pour aider à la performance de notre application.

Plus précisément, il empêche les fonctions d'être recréées chaque fois que notre composant est réaffiché, ce qui peut nuire à la performance de notre application.

Si nous revenons à notre exemple `PlayerList` précédent et ajoutons la capacité d'ajouter des joueurs à notre tableau, lorsque nous passons une fonction pour les supprimer (`handleRemovePlayer`) via les props, la fonction sera recréée chaque fois.

La façon de corriger cela est d'envelopper notre fonction de rappel dans `useCallback` et d'inclure son argument `player` dans le tableau des dépendances :

```
function App() {
  const [player, setPlayer] = React.useState("");
  const [players, setPlayers] = React.useState(["Messi", "Ronaldo", "Laspada"]);

  function handleChangeInput(event) {
    setPlayer(event.target.value);
  }
  function handleAddPlayer() {
    setPlayers(players.concat(player));
  }
  const handleRemovePlayer = useCallback(player => {
    setPlayers(players.filter((p) => p !== player));
  }, [players])

  return (
    <>
      <input onChange={handleChangeInput} />
      <button onClick={handleAddPlayer}>Ajouter un joueur</button>
      <PlayerList players={players} handleRemovePlayer={handleRemovePlayer} />
    </>
  );
}

function PlayerList({ players, handleRemovePlayer }) {
  return (
    <ul>
      {players.map((player) => (
        <li key={player} onClick={() => handleRemovePlayer(player)}>
          {player}
        </li>
      ))}
    </ul>
  );
}

```

## React useMemo

`useMemo` est un autre hook de performance qui nous permet de "mémoïser" une opération donnée.

La mémoïsation permet de se souvenir du résultat de calculs coûteux lorsqu'ils ont déjà été effectués afin de ne pas avoir à les refaire.

Comme `useEffect` et `useCallback`, `useMemo` accepte une fonction de rappel et un tableau de dépendances.

Contrairement à ces deux fonctions, cependant, `useMemo` est destiné à retourner une valeur.

> Vous devez retourner la valeur soit explicitement avec le mot-clé `return`, soit implicitement en utilisant la syntaxe abrégée de la fonction fléchée (comme vu ci-dessous).

Un exemple concret de `useMemo` provient de la documentation de mdx-bundler. `mdx-bundler` est une bibliothèque pour convertir des fichiers .mdx en composants React.

Ici, il utilise `useMemo` pour convertir une chaîne de code brute en un composant React.

```js
import * as React from 'react'
import {getMDXComponent} from 'mdx-bundler/client'

function Post({code, frontmatter}) {
  const Component = React.useMemo(() => getMDXComponent(code), [code]);

  return (
    <>
      <header>
        <h1>{frontmatter.title}</h1>
        <p>{frontmatter.description}</p>
      </header>
      <main>
        <Component />
      </main>
    </>
  )
}

```

La raison de le faire est d'empêcher la valeur `Component` d'être recréée inutilement lorsque le composant est réaffiché.

`useMemo` n'exécutera donc sa fonction de rappel que si la dépendance `code` change.

## Devenez un développeur React professionnel

React est difficile. Vous ne devriez pas avoir à le comprendre par vous-même.

J'ai mis tout ce que je sais sur React dans un seul cours, pour vous aider à atteindre vos objectifs en un temps record :

[**Présentation : Le React Bootcamp**](https://www.thereactbootcamp.com)

**C'est le cours que j'aurais aimé avoir lorsque j'ai commencé à apprendre React.**

Cliquez ci-dessous pour essayer le React Bootcamp par vous-même :

[![Cliquez pour rejoindre le React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Cliquez pour commencer*