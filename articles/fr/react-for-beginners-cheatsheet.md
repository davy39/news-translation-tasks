---
title: 'React pour débutants : l''antisèche React complète pour 2021'
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2021-05-14T20:17:37.000Z'
originalURL: https://freecodecamp.org/news/react-for-beginners-cheatsheet
coverImage: https://www.freecodecamp.org/news/content/images/2021/05/react-for-beginners-2021.png
tags:
- name: beginners guide
  slug: beginners-guide
- name: cheatsheet
  slug: cheatsheet
- name: hooks
  slug: hooks
- name: React
  slug: react
seo_title: 'React pour débutants : l''antisèche React complète pour 2021'
seo_desc: 'Welcome to the React for Beginners guide. It''s designed to teach you all
  the core React concepts that you need to know to start building React applications
  in 2021.

  I created this resource to give you the most complete and beginner-friendly path
  to l...'
---

Bienvenue dans le guide React pour débutants. Il est conçu pour vous enseigner tous les concepts fondamentaux de React que vous devez connaître pour commencer à créer des applications React en 2021.

J'ai créé cette ressource pour vous offrir le parcours le plus complet et le plus accessible aux débutants pour apprendre React de zéro.

À la fin, vous aurez une compréhension approfondie de nombreux concepts essentiels de React, notamment :

* Le Pourquoi, le Quoi et le Comment de React
* Comment créer facilement des applications React
* JSX et la syntaxe de base
* Les éléments JSX
* Les composants et les Props
* Les événements dans React
* Le State et la gestion d'état
* Les bases des Hooks React

### Vous voulez votre propre exemplaire ? 📄

**[Téléchargez l'antisèche au format PDF ici](https://reedbarger.com/resources/react-beginners-2021)** (cela prend 5 secondes).

Voici quelques avantages immédiats à récupérer la version téléchargeable :

* Un guide de référence rapide à consulter n'importe quand et n'importe où
* Des tonnes de snippets de code copiables pour une réutilisation facile
* Lisez ce guide massif là où cela vous convient le mieux. Dans le train, à votre bureau, en faisant la queue... n'importe où.

Il y a énormément de choses passionnantes à couvrir, alors commençons.

## Les bases de React

### Qu'est-ce que React, vraiment ?

React est officiellement défini comme une « bibliothèque JavaScript pour créer des interfaces utilisateur », mais qu'est-ce que cela signifie réellement ?

React est une bibliothèque, conçue en JavaScript et que nous codons en JavaScript, pour construire d'excellentes applications qui s'exécutent sur le web.

### Que dois-je savoir pour apprendre React ?

En d'autres termes, avez-vous besoin d'une compréhension de base de JavaScript pour devenir un solide programmeur React ?

Les concepts JavaScript les plus basiques avec lesquels vous devriez être familier sont les variables, les types de données de base, les conditionnelles, les méthodes de tableau, les fonctions et les modules ES.

Comment apprendre toutes ces compétences JavaScript ? [Consultez le guide complet](https://reactbootcamp.com/javascript-skills-for-react-2021/) pour apprendre tout le JavaScript dont vous avez besoin pour React.

### Si React a été conçu en JavaScript, pourquoi ne pas simplement utiliser JavaScript ?

React a été écrit en JavaScript, mais il a été bâti dès le départ dans le but exprès de construire des applications web et nous donne les outils pour le faire.

JavaScript est un langage vieux de plus de 20 ans qui a été créé pour ajouter de petits morceaux de comportement au navigateur via des scripts et n'a pas été conçu pour créer des applications complètes.

En d'autres termes, bien que JavaScript ait été utilisé pour créer React, ils ont été créés pour des objectifs très différents.

### Puis-je utiliser JavaScript dans les applications React ?

Oui ! Vous pouvez inclure n'importe quel code JavaScript valide dans vos applications React.

Vous pouvez utiliser n'importe quelle API du navigateur ou de l'objet window, comme la géolocalisation ou l'API fetch.

De plus, puisque React (lorsqu'il est compilé) s'exécute dans le navigateur, vous pouvez effectuer des actions JavaScript courantes comme le requêtage et la manipulation du DOM.

## Comment créer des applications React

### Trois façons différentes de créer une application React

1. Mettre React dans un fichier HTML avec des scripts externes
2. Utiliser un environnement React dans le navigateur comme CodeSandbox
3. Créer une application React sur votre ordinateur à l'aide d'un outil comme Create React App

### Quelle est la meilleure façon de créer une application React ?

Quelle est la meilleure approche pour vous ? La meilleure façon de créer votre application dépend de ce que vous voulez en faire.

Si vous voulez créer une application web complète que vous souhaitez finalement mettre en ligne, il est préférable de créer cette application React sur votre ordinateur à l'aide d'un outil comme Create React App.

Si vous souhaitez créer des applications React sur votre ordinateur, [consultez le guide complet sur l'utilisation de Create React App](https://reactbootcamp.com/create-react-app-10-steps/).

La façon la plus simple et la plus conviviale pour les débutants de créer et de construire des applications React pour l'apprentissage et le prototypage est d'utiliser un outil comme CodeSandbox. Vous pouvez créer une nouvelle application React en quelques secondes en allant sur [react.new](https://react.new) !

## Éléments JSX

### JSX est un outil puissant pour structurer les applications

**JSX** est destiné à faciliter la création d'interfaces utilisateur avec des applications JavaScript.

Il emprunte sa syntaxe au langage de programmation le plus largement utilisé : HTML. En conséquence, JSX est un outil puissant pour structurer nos applications.

L'exemple de code ci-dessous est l'exemple le plus basique d'un élément React qui affiche le texte « Hello World » :

```js
<div>Hello React!</div>
```

Notez que pour être affichés dans le navigateur, les éléments React doivent être **rendus** (en utilisant `ReactDOM.render()`).

### En quoi JSX est différent du HTML

Nous pouvons écrire des éléments HTML valides en JSX, mais ce qui diffère légèrement est la façon dont certains attributs sont écrits.

Les attributs qui se composent de plusieurs mots sont écrits en syntaxe camelCase (comme `className`) et ont des noms différents du HTML standard (`class`).

```js
<div id="header">
  <h1 className="title">Hello React!</h1>
</div>
```

JSX a cette façon différente d'écrire les attributs car il est en fait composé de fonctions JavaScript (plus d'informations à ce sujet plus tard).

### JSX doit avoir une barre oblique de fin s'il est composé d'une seule balise

Contrairement au HTML standard, les éléments comme `input`, `img` ou `br` doivent se fermer par une barre oblique de fin pour être du JSX valide.

```js
<input type="email" /> // <input type="email"> est une erreur de syntaxe
```

### Les éléments JSX avec deux balises doivent avoir une balise de fermeture

Les éléments qui doivent avoir deux balises, tels que `div`, `main` ou `button`, doivent avoir leur seconde balise de fermeture en JSX, sinon cela entraînera une erreur de syntaxe.

```js
<button>Click me</button> // <button> ou </button> est une erreur de syntaxe
```

### Comment les éléments JSX sont stylisés

Les styles en ligne (inline styles) sont également écrits différemment par rapport au HTML pur.

* Les styles en ligne ne doivent pas être inclus sous forme de chaîne de caractères, mais à l'intérieur d'un objet.
* Encore une fois, les propriétés de style que nous utilisons doivent être écrites en style camelCase.

```js
<h1 style={{ color: "blue", fontSize: 22, padding: "0.5em 1em" }}>
  Hello React!
</h1>;
```

Les propriétés de style qui acceptent des valeurs en pixels (comme width, height, padding, margin, etc.) peuvent utiliser des entiers au lieu de chaînes de caractères. Par exemple, `fontSize: 22` au lieu de `fontSize: "22px"`.

### Le JSX peut être affiché de manière conditionnelle

Les nouveaux développeurs React peuvent se demander en quoi il est bénéfique que React puisse utiliser du code JavaScript.

Un exemple simple est que pour masquer ou afficher conditionnellement du contenu JSX, nous pouvons utiliser n'importe quelle conditionnelle JavaScript valide, comme une instruction if ou une instruction switch.

```js
const isAuthUser = true;

if (isAuthUser) {
  return <div>Hello user!</div>   
} else {
  return <button>Login</button>
}
```

Où retournons-nous ce code ? À l'intérieur d'un composant React, que nous aborderons dans une section ultérieure.

### Le JSX ne peut pas être compris par le navigateur

Comme mentionné ci-dessus, le JSX n'est pas du HTML, mais est composé de fonctions JavaScript.

En fait, écrire `<div>Hello React</div>` en JSX est juste une façon plus pratique et compréhensible d'écrire un code comme le suivant :

```js
React.createElement("div", null, "Hello React!")
```

Les deux morceaux de code auront le même résultat : « Hello React ».

Pour écrire du JSX et que le navigateur comprenne cette syntaxe différente, nous devons utiliser un **transpileur** pour convertir le JSX en ces appels de fonction.

Le transpileur le plus courant s'appelle **Babel.**

## Composants React

### Que sont les composants React ?

Au lieu de simplement rendre un ensemble ou un autre d'éléments JSX, nous pouvons les inclure dans des **composants** React.

Les composants sont créés en utilisant ce qui ressemble à une fonction JavaScript normale, mais ils sont différents dans le sens où ils retournent des éléments JSX.

```js
function Greeting() {
  return <div>Hello React!</div>;   
}
```

### Pourquoi utiliser des composants React ?

Les composants React nous permettent de créer une logique et des structures plus complexes au sein de notre application React que nous ne le ferions avec des éléments JSX seuls.

Considérez les composants React comme nos propres éléments React personnalisés qui ont leur propre fonctionnalité.

Comme nous le savons, les fonctions nous permettent de créer notre propre fonctionnalité et de la réutiliser où nous le souhaitons dans notre application.

Les composants sont réutilisables partout dans notre application et autant de fois que nous le souhaitons.

### Les composants ne sont pas des fonctions JavaScript normales

Comment pourrions-nous rendre ou afficher le JSX retourné par le composant ci-dessus ?

```js
import React from 'react';
import ReactDOM from 'react-dom';

function Greeting() {
  return <div>Hello React!</div>;   
}

ReactDOM.render(<Greeting />, document.getElementById("root"));
```

Nous utilisons l'import `React` pour analyser le JSX et `ReactDOM` pour rendre notre composant dans un **élément racine** avec l'id « root ».

### Que peuvent retourner les composants React ?

Les composants peuvent retourner des éléments JSX valides, ainsi que des chaînes de caractères, des nombres, des booléens, la valeur `null`, ainsi que des tableaux et des fragments.

Pourquoi voudrions-nous retourner `null` ? Il est courant de retourner `null` si nous voulons qu'un composant n'affiche rien.

```js
function Greeting() {
  if (isAuthUser) {
    return "Hello again!";   
  } else {
    return null;
  }
}
```

Une autre règle est que les éléments JSX doivent être enveloppés dans un seul élément parent. Plusieurs éléments frères ne peuvent pas être retournés.

Si vous avez besoin de retourner plusieurs éléments, mais que vous n'avez pas besoin d'ajouter un autre élément au DOM (généralement pour une conditionnelle), vous pouvez utiliser un composant React spécial appelé un fragment.

Les fragments peuvent être écrits sous la forme `<></>` ou, lorsque vous importez React dans votre fichier, avec `<React.Fragment></React.Fragment>`.

```js
function Greeting() {
  const isAuthUser = true;  
    
  if (isAuthUser) {
    return (
      <>
        <h1>Hello again!</h1>
        <button>Logout</button>
      </>
    );
  } else {
    return null;
  }
}
```

Notez que lorsque vous essayez de retourner un certain nombre d'éléments JSX répartis sur plusieurs lignes, nous pouvons tout retourner en utilisant un jeu de parenthèses () comme vous le voyez dans l'exemple ci-dessus.

### Les composants peuvent retourner d'autres composants

La chose la plus importante que les composants peuvent retourner, ce sont d'autres composants.

Voici un exemple basique d'une application React contenue dans un composant appelé `App` qui retourne plusieurs composants :

```js
import React from 'react';
import ReactDOM from 'react-dom';

import Layout from './components/Layout';
import Navbar from './components/Navbar';
import Aside from './components/Aside';
import Main from './components/Main';
import Footer from './components/Footer';

function App() {
  return (
    <Layout>
      <Navbar />
      <Main />
      <Aside />
      <Footer />
    </Layout>
  );
}

ReactDOM.render(<App />, document.getElementById('root'));
```

C'est puissant parce que nous utilisons la personnalisation des composants pour décrire ce qu'ils sont (c'est-à-dire le Layout) et leur fonction dans notre application. Cela nous indique comment ils doivent être utilisés rien qu'en regardant leur nom.

De plus, nous utilisons la puissance du JSX pour composer ces composants. En d'autres termes, pour utiliser la syntaxe de type HTML du JSX afin de les structurer de manière immédiatement compréhensible (comme la Navbar en haut de l'application, le Footer en bas, et ainsi de suite).

### Le JavaScript peut être utilisé dans JSX à l'aide d'accolades

Tout comme nous pouvons utiliser des variables JavaScript dans nos composants, nous pouvons les utiliser directement dans notre JSX également.

Il existe cependant quelques règles de base pour utiliser des valeurs dynamiques dans JSX :

* JSX peut accepter toutes les valeurs primitives (chaînes, booléens, nombres), mais il n'acceptera pas les objets simples.
* JSX peut également inclure des expressions qui se résolvent en ces valeurs.

Par exemple, les conditionnelles peuvent être incluses dans JSX en utilisant l'opérateur ternaire, puisqu'il se résout en une valeur.

```js
function Greeting() {
  const isAuthUser = true;  
    
  return <div>{isAuthUser ? "Hello!" : null}</div>;
}
```

## Les Props dans React

### On peut passer des valeurs aux composants via les props

Les données passées aux composants en JavaScript sont appelées **props**.

Les props ressemblent exactement aux attributs des éléments JSX/HTML simples, mais vous pouvez accéder à leurs valeurs à l'intérieur du composant lui-même.

Les props sont disponibles dans les paramètres du composant auquel elles sont passées. Les props sont toujours incluses en tant que propriétés d'un objet.

```js
ReactDOM.render(
  <Greeting username="John!" />,
  document.getElementById("root")
);

function Greeting(props) {
  return <h1>Hello {props.username}</h1>;
}

```

### Les props ne peuvent pas être modifiées directement

Les props ne doivent jamais être modifiées directement à l'intérieur du composant enfant.

Une autre façon de dire cela est que les props ne doivent jamais être **mutées**, car les props sont un objet JavaScript simple.

```js
// Nous ne pouvons pas modifier l'objet props :
function Header(props) {
  props.username = "Doug";

  return <h1>Hello {props.username}</h1>;
}
```

Les composants sont considérés comme des fonctions pures. C'est-à-dire que pour chaque entrée, nous devrions pouvoir attendre la même sortie. Cela signifie que nous ne pouvons pas muter l'objet props, seulement le lire.

### Props spéciales : la prop children

La prop **children** est utile si nous voulons passer des éléments / composants en tant que props à d'autres composants.

La prop children est particulièrement utile lorsque vous voulez que le même composant (comme un composant Layout) enveloppe tous les autres composants.

```js
function Layout(props) {
  return <div className="container">{props.children}</div>;
}

function IndexPage() {
  return (
    <Layout>
      <Header />
      <Hero />
      <Footer />
    </Layout>
  );
}

function AboutPage() {
  return (
    <Layout>
      <About />
      <Footer />
    </Layout>
  );
}
```

L'avantage de ce modèle est que tous les styles appliqués au composant Layout seront partagés avec ses composants enfants.

## Listes et clés dans React

### Comment itérer sur des tableaux dans JSX en utilisant map

Comment affichons-nous des listes en JSX en utilisant des données de tableau ? Nous utilisons la fonction **`.map()`** pour convertir des listes de données (tableaux) en listes d'éléments.

```js
const people = ["John", "Bob", "Fred"];
const peopleList = people.map((person) => <p>{person}</p>);

```

Vous pouvez utiliser `.map()` pour des composants ainsi que pour des éléments JSX simples.

```js
function App() {
  const people = ["John", "Bob", "Fred"];

  return (
    <ul>
      {people.map((person) => (
        <Person name={person} />
      ))}
    </ul>
  );
}

function Person({ name }) {
  // nous accédons à la prop 'name' directement via la déstructuration d'objet
  return <p>Le nom de cette personne est : {name}</p>;
}
```

### L'importance des clés dans les listes

Chaque élément React au sein d'une liste d'éléments a besoin d'une **prop key** spéciale.

Les clés sont essentielles pour que React puisse suivre chaque élément sur lequel on itère avec la fonction `.map()`.

React utilise les clés pour mettre à jour de manière performante les éléments individuels lorsque leurs données changent (au lieu de restituer toute la liste).

Les clés doivent avoir des valeurs uniques pour pouvoir identifier chacune d'elles en fonction de leur valeur de clé.

```js
function App() {
  const people = [
    { id: "Ksy7py", name: "John" },
    { id: "6eAdl9", name: "Bob" },
    { id: "6eAdl9", name: "Fred" },
  ];

  return (
    <ul>
      {people.map((person) => (
        <Person key={person.id} name={person.name} />
      ))}
    </ul>
  );
}
```

## State et gestion des données dans React

### Qu'est-ce que le state dans React ?

Le **State** (état) est un concept qui fait référence à la façon dont les données de notre application changent au fil du temps.

L'importance du state dans React est que c'est une façon de parler de nos données séparément de l'interface utilisateur (ce que l'utilisateur voit).

Nous parlons de gestion d'état, car nous avons besoin d'un moyen efficace de suivre et de mettre à jour les données à travers nos composants au fur et à mesure que notre utilisateur interagit avec eux.

Pour transformer notre application d'éléments HTML statiques en une application dynamique avec laquelle l'utilisateur peut interagir, nous avons besoin du state.

### Exemples d'utilisation du state dans React

Nous devons souvent gérer le state lorsque notre utilisateur souhaite interagir avec notre application.

Lorsqu'un utilisateur tape dans un formulaire, nous suivons l'état du formulaire dans ce composant.

Lorsque nous récupérons des données d'une API pour les afficher à l'utilisateur (comme des articles dans un blog), nous devons enregistrer ces données dans le state.

Lorsque nous voulons modifier des données qu'un composant reçoit via des props, nous utilisons le state pour les modifier au lieu de muter l'objet props.

### Introduction aux hooks React avec useState

La façon de « créer » un state dans React au sein d'un composant particulier est d'utiliser le hook `useState`.

Qu'est-ce qu'un hook ? C'est un peu comme une fonction JavaScript, mais il ne peut être utilisé que dans un composant fonctionnel React, au sommet du composant.

Nous utilisons des hooks pour nous « brancher » (hook into) sur certaines fonctionnalités, et `useState` nous donne la possibilité de créer et de gérer un state.

`useState` est un exemple de hook React de base qui provient directement de la bibliothèque React : `React.useState`.

```js
import React from 'react';

function Greeting() {
  const state = React.useState("Hello React");  
    
  return <div>{state[0]}</div> // affiche "Hello React"
}
```

Comment fonctionne `useState` ? Comme une fonction normale, nous pouvons lui passer une valeur de départ (comme « Hello React »).

Ce qui est retourné par useState est un tableau. Pour accéder à la variable d'état et à sa valeur, nous pouvons utiliser la première valeur de ce tableau : `state[0]`.

Il existe cependant un moyen d'améliorer l'écriture de ceci. Nous pouvons utiliser la déstructuration de tableau pour obtenir un accès direct à cette variable d'état et l'appeler comme nous le souhaitons, par exemple `title`.

```js
import React from 'react';

function Greeting() {
  const [title] = React.useState("Hello React");  
    
  return <div>{title}</div> // affiche "Hello React"
}
```

Et si nous voulons permettre à notre utilisateur de mettre à jour le message d'accueil qu'il voit ? Si nous incluons un formulaire, un utilisateur peut taper une nouvelle valeur. Cependant, nous avons besoin d'un moyen de mettre à jour la valeur initiale de notre titre.

```js
import React from "react";

function Greeting() {
  const [title] = React.useState("Hello React");

  return (
    <div>
      <h1>{title}</h1>
      <input placeholder="Update title" />
    </div>
  );
}

```

Nous pouvons le faire à l'aide du deuxième élément du tableau retourné par useState. C'est une fonction de mise à jour (setter function), à laquelle nous pouvons passer n'importe quelle valeur que nous voulons pour le nouvel état.

Dans notre cas, nous voulons obtenir la valeur qui est tapée dans l'input lorsqu'un utilisateur est en train de taper. Nous pouvons l'obtenir à l'aide des événements React.

### Que sont les événements dans React ?

Les événements sont des moyens d'obtenir des données sur une certaine action qu'un utilisateur a effectuée dans notre application.

Les props les plus couramment utilisées pour gérer les événements sont `onClick` (pour les événements de clic), `onChange` (lorsqu'un utilisateur tape dans une entrée) et `onSubmit` (lorsqu'un formulaire est soumis).

Les données d'événement nous sont transmises en connectant une fonction à chacune de ces props répertoriées (il y en a beaucoup d'autres parmi lesquelles choisir).

Pour obtenir des données sur l'événement lorsque notre entrée est modifiée, nous pouvons ajouter `onChange` sur l'input et le connecter à une fonction qui gérera l'événement. Cette fonction s'appellera `handleInputChange` :

```js
import React from "react";

function Greeting() {
  const [title] = React.useState("Hello React");

  function handleInputChange(event) {
    console.log("entrée modifiée !", event);
  }

  return (
    <div>
      <h1>{title}</h1>
      <input placeholder="Update title" onChange={handleInputChange} />
    </div>
  );
}
```

Notez que dans le code ci-dessus, un nouvel événement sera enregistré dans la console du navigateur chaque fois que l'utilisateur tape dans l'entrée.

Les données d'événement nous sont fournies sous la forme d'un objet avec de nombreuses propriétés qui dépendent du type d'événement.

### Comment mettre à jour le state dans React avec useState

Pour mettre à jour le state avec useState, nous pouvons utiliser le deuxième élément que useState nous renvoie dans son tableau.

Cet élément est une fonction qui nous permettra de mettre à jour la valeur de la variable d'état (le premier élément). Tout ce que nous passons à cette fonction setter lorsque nous l'appelons sera placé dans le state.

```js
import React from "react";

function Greeting() {
  const [title, setTitle] = React.useState("Hello React");

  function handleInputChange(event) {
    setTitle(event.target.value);
  }

  return (
    <div>
      <h1>{title}</h1>
      <input placeholder="Update title" onChange={handleInputChange} />
    </div>
  );
}
```

En utilisant le code ci-dessus, tout ce que l'utilisateur tape dans l'entrée (le texte provient de `event.target.value`) sera mis dans le state à l'aide de `setTitle` et affiché dans l'élément `h1`.

Ce qui est spécial avec le state et pourquoi il doit être géré avec un hook dédié comme useState, c'est qu'une mise à jour d'état (comme lorsque nous appelons `setTitle`) provoque un re-rendu (re-render).

Un re-rendu se produit lorsqu'un certain composant s'affiche ou est affiché à nouveau en fonction des nouvelles données. Si nos composants n'étaient pas re-rendus lorsque les données changeaient, nous ne verrions jamais l'apparence de l'application changer !

## **Et après ?**

J'espère que vous avez tiré profit de ce guide.

Si vous voulez une copie de cette antisèche pour vos besoins d'apprentissage, vous pouvez [télécharger une version PDF complète de cette antisèche ici](https://reedbarger.com/resources/react-beginners-2021).

Une fois que vous aurez terminé ce guide, il y a beaucoup de choses que vous pouvez apprendre pour faire passer vos compétences au niveau supérieur, notamment :

* [Comment écrire des hooks React personnalisés](https://reactbootcamp.com/how-to-code-react-hooks/)
* [Le guide complet des props React](https://reactbootcamp.com/react-props-cheatsheet/)
* [Comment récupérer des données dans React de bout en bout](https://reactbootcamp.com/fetch-data-in-react/)
* [Comment créer des applications fullstack en React avec Node](https://reactbootcamp.com/react-app-node-backend/)
* [En savoir plus sur le state React](https://reactbootcamp.com/what-to-know-about-react-state/)
* [Comment ajouter le routage à votre application React avec React Router](https://reactbootcamp.com/react-router-cheatsheet/)
* [Apprenez chaque partie de React avec l'antisèche React avancée](https://reactbootcamp.com/react-cheatsheet-2021/)

## Devenez un développeur React professionnel

React est difficile. Vous ne devriez pas avoir à le découvrir par vous-même.

J'ai mis tout ce que je sais sur React dans un seul cours, pour vous aider à atteindre vos objectifs en un temps record :

[**Présentation : Le Bootcamp React**](https://www.thereactbootcamp.com)

**C’est le cours que j’aurais aimé avoir quand j’ai commencé à apprendre React.**

Cliquez ci-dessous pour essayer le Bootcamp React par vous-même :

[![Cliquez pour rejoindre le Bootcamp React](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Cliquez pour commencer*