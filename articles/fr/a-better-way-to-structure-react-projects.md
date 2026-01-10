---
title: Une meilleure façon de structurer les projets React
subtitle: ''
author: Akash Joshi
co_authors: []
series: null
date: '2021-02-02T22:54:52.000Z'
originalURL: https://freecodecamp.org/news/a-better-way-to-structure-react-projects
coverImage: https://www.freecodecamp.org/news/content/images/2021/02/z02wxvp94dwg84c4ifhj.jpeg
tags:
- name: Code Quality
  slug: code-quality
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: React
  slug: react
seo_title: Une meilleure façon de structurer les projets React
seo_desc: 'Hello, everyone! A lot of e-ink has already been spilt on the relatively
  easier pickings of “Doing X in React” or “Using React with technology X”.

  So instead, I want to talk about the experiences I''ve had building frontends from
  scratch at DelightCha...'
---

Bonjour à tous ! Beaucoup d'encre électronique a déjà été versée sur les sujets relativement plus faciles comme "Faire X dans React" ou "Utiliser React avec la technologie X".

Je souhaite donc plutôt parler des expériences que j'ai eues en construisant des frontends à partir de zéro chez [DelightChat](https://delightchat.io/) et dans mes précédentes entreprises.

Ces projets nécessitent une compréhension plus approfondie de React et une utilisation étendue dans un environnement de production.

Si vous souhaitez regarder une version vidéo de ce tutoriel pour compléter votre lecture, [vous pouvez le faire ici](https://www.youtube.com/watch?v=lViIdphWTwY).

%[https://www.youtube.com/watch?v=lViIdphWTwY]

## Introduction

En résumé, un projet React complexe devrait être structuré comme suit. Bien que j'utilise NextJS en production, cette structure de fichiers devrait être assez utile dans n'importe quel environnement React.

```javascript
src
|---adapters
|---contexts
|---components
|---styles
|---pages
```

*Note : Dans la structure de fichiers ci-dessus, les assets ou fichiers statiques doivent être placés dans le dossier* `public` *ou son équivalent pour votre framework.*

Pour chacun des dossiers ci-dessus, discutons-les dans l'ordre de précédence.

## 1. Adapters

Les `Adapters` sont les connecteurs de votre application avec le monde extérieur. Toute forme d'appel API ou d'interaction websocket qui doit se produire, pour partager des données avec un service externe ou un client, doit se faire dans l'adapter lui-même.

Il existe des cas où certaines données sont toujours partagées entre tous les adapters – par exemple, le partage de cookies, d'URL de base et d'en-têtes entre vos adapters AJAX (XHR). Ceux-ci peuvent être initialisés dans le dossier xhr, puis importés à l'intérieur de vos autres adapters pour être utilisés plus loin.

Cette structure ressemblera à ceci :

```javascript
adapters
|---xhr
|---page1Adapter
|---page2Adapter
```

Dans le cas d'axios, vous pouvez utiliser `axios.create` pour créer un adapter de base, et soit exporter cette instance initialisée, soit créer différentes fonctions pour get, post, patch et delete pour l'abstraire davantage. Cela ressemblerait à ceci :

```javascript
// adapters/xhr/index.tsx

import Axios from "axios";

function returnAxiosInstance() {
  return Axios.create(initializers);
}

export function get(url){
  const axios = returnAxiosInstance();
  return axios.get(url);
}

export function post(url, requestData){
  const axios = returnAxiosInstance();
  return axios.post(url, requestData);
}

... et ainsi de suite ...
```

Après avoir préparé votre fichier de base (ou vos fichiers), créez un fichier d'adapter séparé pour chaque page, ou chaque ensemble de fonctionnalités, selon la complexité de votre application. Une fonction bien nommée facilite grandement la compréhension de ce que chaque appel API fait et de ce qu'il doit accomplir.

```javascript
// adapters/page1Adapter/index.tsx

import { get, post } from "adapters/xhr";
import socket from "socketio";

// fonctions bien nommées
export function getData(){
  return get(someUrl);
}

export function setData(requestData){
  return post(someUrl, requestData);
}

... et ainsi de suite ...
```

Mais comment ces adapters seront-ils utiles ? Découvrons-le dans la section suivante.

## 2. Components

Bien que dans cette section nous devrions parler des contextes, je souhaite d'abord parler des composants. Cela permet de comprendre pourquoi le contexte est nécessaire (et requis) dans les applications complexes.

Les `Components` sont le cœur de votre application. Ils contiendront l'interface utilisateur de votre application et peuvent parfois contenir la logique métier ainsi que tout état qui doit être maintenu.

Dans le cas où un composant devient trop complexe pour exprimer la logique métier avec votre interface utilisateur, il est bon de pouvoir le diviser en un fichier bl.tsx séparé, avec votre fichier index.tsx racine important toutes les fonctions et gestionnaires de celui-ci.

Cette structure ressemblerait à ceci :

```javascript
components
|---page1Components
        |--Component1
        |--Component2
|---page2Component
        |--Component1
               |---index.tsx
               |---bl.tsx
```

Dans cette structure, chaque page obtient son propre dossier à l'intérieur des composants, afin qu'il soit facile de déterminer quel composant affecte quoi.

Il est également important de limiter la portée d'un composant. Par conséquent, un composant ne doit utiliser que les `adapters` pour la récupération de données, avoir un fichier séparé pour la logique métier complexe et se concentrer uniquement sur la partie interface utilisateur.

```javascript
// components/page1Components/Component1/index.tsx

import businessLogic from "./bl.tsx";

export default function Component2() {

  const { state and functions } = businessLogic();

  return {
    // JSX
  }
}
```

Tandis que le fichier BL n'importe que les données et les retourne :

```javascript
// components/page1Components/Component1/bl.tsx

import React, {useState, useEffect} from "react";
import { adapters } from "adapters/path_to_adapter";

export default function Component1Bl(){
  const [state, setState] = useState(initialState);

  useEffect(() => {
    fetchDataFromAdapter().then(updateState);
  }, [])
}
```

Cependant, il existe un problème courant à toutes les applications complexes : la gestion d'état et la manière de partager l'état entre des composants distants. Par exemple, considérons la structure de fichiers suivante :

```javascript
components
|---page1Components
        |--Component1
               |---ComponentA
|---page2Component
        |--ComponentB
```

Si un certain état doit être partagé entre les composants A et B dans l'exemple ci-dessus, il devra être passé à travers tous les composants intermédiaires, et également à tout autre composant qui souhaite interagir avec l'état.

Pour résoudre ce problème, plusieurs solutions peuvent être utilisées comme Redux, Easy-Peasy et React Context, chacune ayant ses propres avantages et inconvénients. Généralement, React Context devrait être "suffisant" pour résoudre ce problème. Nous stockons tous les fichiers liés au contexte dans `contexts`.

## 3. Contexts

Le dossier `contexts` est un dossier minimal contenant uniquement l'état qui doit être partagé entre ces composants. Chaque page peut avoir plusieurs contextes imbriqués, chaque contexte ne transmettant les données que dans une direction descendante. Mais pour éviter la complexité, il est préférable de n'avoir qu'un seul fichier de contexte. Cette structure ressemblera à ceci :

```javascript
contexts
|---page1Context
        |---index.tsx (Exporte les consommateurs, les fournisseurs, ...)
        |---Context1.tsx (Contient une partie de l'état)
        |---Context2.tsx (Contient une partie de l'état)
|---page2Context
        |---index.tsx (Assez simple pour contenir également l'état)
```

Dans le cas ci-dessus, comme `page1` peut être un peu plus complexe, nous permettons un certain contexte imbriqué en passant le contexte enfant comme enfant du parent. Cependant, généralement un seul fichier `index.tsx` contenant l'état et exportant les fichiers pertinents devrait suffire.

Je ne vais pas entrer dans la partie implémentation des bibliothèques de gestion d'état React, car chacune d'entre elles est un monde à part et a ses propres avantages et inconvénients. Je recommande donc de suivre le tutoriel de ce que vous décidez d'utiliser pour apprendre leurs meilleures pratiques.

Le contexte est autorisé à importer depuis `adapters` pour récupérer et réagir aux effets externes. Dans le cas de React Context, les fournisseurs sont importés à l'intérieur des pages pour partager l'état entre tous les composants, et quelque chose comme `useContext` est utilisé à l'intérieur de ces `components` pour pouvoir utiliser ces données.

Passons à la dernière pièce majeure du puzzle, `pages`.

## 4. Pages

Je souhaite éviter d'être biaisé envers un framework pour cette partie, mais en général, avoir un dossier spécifique pour les composants de niveau route est une bonne pratique.

Gatsby et NextJS imposent d'avoir toutes les routes dans un dossier nommé `pages`. C'est une manière assez lisible de définir les composants de niveau route, et imiter cela dans votre application générée par CRA entraînerait également une meilleure lisibilité du code.

Un emplacement centralisé pour les routes vous aide également à utiliser la fonctionnalité "Aller au fichier" de la plupart des IDE en sautant à un fichier en utilisant (Cmd ou Ctrl) + Clic sur une importation.

Cela vous aide à naviguer dans le code rapidement et avec clarté sur ce qui appartient où. Cela établit également une hiérarchie claire de différenciation entre `pages` et `components`, où une page peut importer un composant pour l'afficher et ne rien faire d'autre, pas même de la logique métier.

Cependant, il est possible d'importer des fournisseurs de contexte à l'intérieur de votre page afin que les composants enfants puissent les consommer. Ou, dans le cas de NextJS, écrire du code côté serveur qui peut passer des données à vos composants en utilisant getServerSideProps ou getStaticProps.

## 5. Styles

Enfin, nous arrivons aux styles. Bien que ma méthode préférée soit d'intégrer les styles directement dans l'interface utilisateur en utilisant une solution CSS-in-JS comme Styled-Components, il est parfois utile d'avoir un ensemble global de styles dans un fichier CSS.

Un bon vieux fichier CSS est plus partageable entre les projets et peut également affecter le CSS des composants que styled-components ne peut pas atteindre (par exemple, les composants tiers).

Vous pouvez donc stocker tous ces fichiers CSS à l'intérieur du dossier `styles` et les importer ou les lier librement depuis n'importe où.

Ce sont mes réflexions. N'hésitez pas à m'envoyer un e-mail si vous souhaitez discuter de quelque chose ou si vous avez d'autres suggestions sur la manière d'améliorer cela !

Pour des mises à jour ou des discussions supplémentaires, vous pouvez me suivre sur Twitter [ici](https://twitter.com/thewritingdev).

Mon dernier article sur freeCodeCamp portait sur la manière de commencer avec Deno en construisant un raccourcisseur d'URL, que [vous pouvez lire ici](https://www.freecodecamp.org/news/build-a-url-shortener-in-deno/).