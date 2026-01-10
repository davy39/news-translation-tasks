---
title: Le guide de référence React pour 2021 (+ exemples concrets)
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2021-01-09T16:36:00.000Z'
originalURL: https://freecodecamp.org/news/react-cheatsheet-with-real-world-examples
coverImage: https://www.freecodecamp.org/news/content/images/2021/01/the-react-cheatsheet-for-2021-1.png
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: Web Development
  slug: web-development
seo_title: Le guide de référence React pour 2021 (+ exemples concrets)
seo_desc: 'I have put together a comprehensive visual cheatsheet to help you master
  all the major concepts and features of the React library in 2021.

  I created this cheatsheet to help you optimize your React learning in the shortest
  amount of time.

  It includes ...'
---

J'ai rassemblé un guide visuel complet pour vous aider à maîtriser tous les concepts et fonctionnalités majeurs de la bibliothèque React en 2021.

**J'ai créé ce guide pour vous aider à optimiser votre apprentissage de React dans le laps de temps le plus court possible.**

Il inclut de nombreux exemples pratiques pour illustrer chaque fonctionnalité de la bibliothèque et son fonctionnement en utilisant des motifs que vous pouvez appliquer dans vos propres projets.

En plus de chaque extrait de code, j'ai ajouté de nombreux commentaires utiles. Si vous lisez ces commentaires, vous verrez ce que fait chaque ligne de code, comment différents concepts se rapportent les uns aux autres, et vous obtiendrez une compréhension plus complète de la manière dont React peut être utilisé.

Notez que les mots-clés particulièrement utiles pour vous en tant que développeur React sont mis en évidence en gras, alors surveillez ceux-ci.

### Vous voulez votre propre copie du guide ?

**[Téléchargez le guide au format PDF ici](https://reedbarger.com/resources/the-react-cheatsheet-for-2021)** (cela prend 5 secondes).

Voici quelques avantages rapides à obtenir la version téléchargeable :

* ✅ Guide de référence rapide à consulter comme vous le souhaitez et quand vous le souhaitez
* ✅ Des tonnes d'extraits de code copiables pour une réutilisation facile
* ✅ Lisez ce guide massif où cela vous convient le mieux. Dans le train, à votre bureau, en faisant la queue... n'importe où.

Il y a une tonne de choses géniales à couvrir, alors commençons.

> Vous voulez exécuter l'un des extraits de code ci-dessous ? Créez une nouvelle application React pour essayer l'un de ces exemples en utilisant l'outil en ligne (gratuit) CodeSandbox. Vous pouvez le faire instantanément en visitant [react.new](https://react.new).

## Table des matières

### Fondamentaux de React

* [Éléments JSX](#heading-jsx-elements)
* [Composants et Props](#heading-components-and-props)
* [Listes et Clés](#heading-lists-and-keys)
* [Écouteurs d'événements et Gestion des événements](#heading-event-listeners-and-handling-events)

### Hooks essentiels de React

* [État et useState](#heading-state-and-usestate)
* [Effets de bord et useEffect](#heading-side-effects-and-useeffect)
* [Refs et useRef](#heading-refs-and-useref)

### Hooks et Performance

* [Prévenir les re-rendus et React.memo](#heading-preventing-re-renders-and-reactmemo)
* [Fonctions de rappel et useCallback](#heading-callback-functions-and-usecallback)
* [Mémoisation et useMemo](#heading-memoization-and-usememo)

### Hooks avancés de React

* [Contexte et useContext](#heading-context-and-usecontext)
* [Réducteurs et useReducer](#heading-reducers-and-usereducer)
* [Écrire des hooks personnalisés](#heading-writing-custom-hooks)
* [Règles des hooks](#heading-rules-of-hooks)

## Fondamentaux de React

### Éléments JSX

Les applications React sont structurées en utilisant une syntaxe appelée **JSX**. Voici la syntaxe d'un élément **JSX** de base.

```js
/* 
  JSX nous permet d'écrire dans une syntaxe presque identique au HTML simple.
  Par conséquent, JSX est un outil puissant pour structurer nos applications.
  JSX utilise toutes les balises HTML valides (c'est-à-dire div/span, h1-h6, form/input, img, etc).
*/

<div>Bonjour React !</div>

/* 
  Note : ce JSX ne serait pas visible car il doit être rendu par notre application en utilisant ReactDOM.render() 
*/
```

JSX est le moyen le plus courant de structurer les applications React, mais il n'est pas requis pour React.

```js
/* JSX est une manière plus simple d'utiliser la fonction React.createElement()
En d'autres termes, les deux lignes suivantes dans React sont les mêmes : */

<div>Bonjour React !</div>  // Syntaxe JSX

React.createElement('div', null, 'Bonjour React !'); // Syntaxe createElement
```

JSX n'est pas compris par le navigateur. Il doit être compilé en JavaScript simple, que le navigateur peut comprendre.

Le compilateur le plus couramment utilisé pour JSX s'appelle Babel.

```js
/* 
  Lorsque notre projet est construit pour s'exécuter dans le navigateur, notre JSX sera converti par Babel en simples appels de fonction React.createElement(). 
  De ceci... 
*/
const greeting = <div>Bonjour React !</div>;

/* ...en ceci : */
"use strict";

const greeting = /*#__PURE__*/React.createElement("div", null, "Bonjour React !");
```

JSX diffère de HTML de plusieurs manières importantes :

```js
/* 
  Nous pouvons écrire JSX comme du HTML simple, mais il est en fait fait en utilisant des fonctions JavaScript.
  Parce que JSX est JavaScript, et non HTML, il y a quelques différences :

  1) Certains attributs JSX sont nommés différemment des attributs HTML. Pourquoi ? Parce que certains mots d'attribut sont des mots réservés en JavaScript, comme 'class'. Au lieu de class, JSX utilise 'className'.

  De plus, parce que JSX est JavaScript, les attributs qui consistent en plusieurs mots sont écrits en camelCase :
*/

<div id="header">
  <h1 className="title">Bonjour React !</h1>
</div>

/* 
  2) Les éléments JSX qui consistent en une seule balise (c'est-à-dire input, img, br) doivent être fermés avec une barre oblique de fin pour être valides (/): 
*/

<input type="email" /> // <input type="email"> est une erreur de syntaxe

/* 
  3) Les éléments JSX qui consistent en une balise d'ouverture et de fermeture (c'est-à-dire div, span, button), doivent avoir les deux ou être fermés avec une barre oblique de fin. Comme en 2), il est une erreur de syntaxe d'avoir un élément non terminé. 
*/

<button>Cliquez-moi</button> // <button> ou </button> est une erreur de syntaxe
<button /> // vide, mais aussi valide
```

Les styles en ligne peuvent être ajoutés aux éléments JSX en utilisant l'attribut style. Et les styles sont mis à jour dans un objet, et non dans une série de guillemets doubles, comme avec HTML.

Notez que les noms des propriétés de style doivent également être écrits en camelCase.

```js
/* 
  Les propriétés qui acceptent des valeurs en pixels (comme width, height, padding, margin, etc), peuvent utiliser des entiers au lieu de chaînes.
  Par exemple : fontSize: 22. Au lieu de : fontSize: "22px"
*/
<h1 style={{ color: 'blue', fontSize: 22, padding: '0.5em 1em' }}>
  Bonjour React !
</h1>
```

Les éléments JSX sont des expressions JavaScript et peuvent être utilisés comme telles. JSX nous donne toute la puissance de JavaScript directement dans notre interface utilisateur.

```js
/* 
  Les éléments JSX sont des expressions (résolvent à une valeur) et peuvent donc être assignés à des variables JavaScript simples... 
*/
const greeting = <div>Bonjour React !</div>;

const isNewToReact = true;

// ... ou peuvent être affichés conditionnellement
function sayGreeting() {
  if (isNewToReact) {
    // ... ou retournés par des fonctions, etc.
    return greeting; // affiche : Bonjour React !
  } else {
    return <div>Bonjour à nouveau, React</div>;
  }
}
```

JSX nous permet d'insérer (ou d'intégrer) des expressions JavaScript simples en utilisant la syntaxe des accolades :

```js
const year = 2021;

/* Nous pouvons insérer des valeurs JS primitives (c'est-à-dire des chaînes, des nombres, des booléens) dans des accolades : {} */
const greeting = <div>Bonjour React en {year}</div>;

/* Nous pouvons également insérer des expressions qui résolvent à une valeur primitive : */
const goodbye = <div>Au revoir l'année précédente : {year - 1}</div>

/* Les expressions peuvent également être utilisées pour les attributs des éléments */
const className = 'title';
const title = <h1 className={className}>Mon titre</h1>

/* Note : essayer d'insérer des valeurs d'objet (c'est-à-dire des objets, des tableaux, des maps) dans des accolades entraînera une erreur */
```

JSX nous permet d'imbriquer des éléments les uns dans les autres, comme nous le ferions avec HTML.

```js
/* 
  Pour écrire JSX sur plusieurs lignes, enveloppez-le dans des parenthèses : ()
  Les expressions JSX qui s'étendent sur plusieurs lignes sont appelées expressions multilignes
*/

const greeting = (
  // div est l'élément parent
  <div>
    {/* h1 et p sont des éléments enfants */}
    <h1>Bonjour !</h1>
    <p>Bienvenue à React</p>
  </div>
);
/* 'parents' et 'enfants' sont la manière dont nous décrivons les éléments JSX en relation
les uns avec les autres, comme nous parlerions des éléments HTML */
```

Les commentaires dans JSX sont écrits comme des commentaires JavaScript multilignes, écrits entre accolades, comme ceci :

```js
const greeting = (
  <div>
    {/* Ceci est un commentaire sur une seule ligne */}
  	<h1>Bonjour !</div>
	<p>Bienvenue à React</p>
    {/* Ceci est un 
      commentaire
      multiline */} 
  </div>
);
```

Toutes les applications React nécessitent trois choses :

1. `ReactDOM.render()` : utilisé pour rendre (afficher) notre application en la montant sur un élément HTML
2. Un élément JSX : appelé "nœud racine", car il est la racine de notre application. Cela signifie que le rendre rendra tous les enfants à l'intérieur
3. Un élément HTML (DOM) : Où l'application est insérée dans une page HTML. L'élément est généralement une div avec un id de "root", situé dans un fichier index.html.

```js
// Les packages peuvent être installés localement ou apportés via un lien CDN (ajouté à l'en-tête du document HTML) 
import React from "react";
import ReactDOM from "react-dom";

// le nœud racine (généralement un composant) est le plus souvent appelé "App"
const App = <h1>Bonjour React !</h1>;

// ReactDOM.render(nœud racine, élément HTML)
ReactDOM.render(App, document.getElementById("root"));
```

### Composants et Props

JSX peut être regroupé dans des fonctions individuelles appelées **composants**.

Il existe deux types de composants dans React : les **composants fonctionnels** et les **composants de classe**.

Les noms des composants, pour les composants fonctionnels ou de classe, sont en majuscules pour les distinguer des fonctions JavaScript simples qui ne retournent pas de JSX :

```js
import React from "react";

/* 	
  Composant fonctionnel
  Notez le nom de la fonction en majuscules : 'Header', pas 'header'
*/
function Header() {
  return <h1>Bonjour React</h1>;
}

// Les composants fonctionnels qui utilisent une syntaxe de fonction fléchée sont également valides
const Header = () => <h1>Bonjour React</h1>;

/* 
  Composant de classe
  Les composants de classe ont plus de code standard (notez le mot-clé 'extends' et la méthode 'render')
*/
class Header extends React.Component {
  render() {
    return <h1>Bonjour React</h1>;
  }
}
```

Les composants, malgré le fait qu'ils soient des fonctions, ne sont pas appelés comme des fonctions JavaScript ordinaires. Ils sont exécutés en les rendant comme nous le ferions avec JSX dans notre application.

```js
// Appelons-nous cette fonction composant comme une fonction normale ?

// Non, pour les exécuter et afficher le JSX qu'ils retournent...
const Header = () => <h1>Bonjour React</h1>;

// ...nous les utilisons comme des éléments JSX 'personnalisés'
ReactDOM.render(<Header />, document.getElementById("root"));
// rend : <h1>Bonjour React</h1>
```

L'énorme avantage des composants est leur capacité à être réutilisés dans nos applications, partout où nous en avons besoin.

Puisque les composants tirent parti de la puissance des fonctions JavaScript, nous pouvons logiquement leur passer des données, comme nous le ferions en leur passant un ou plusieurs arguments.

```js
/* 
  Les composants Header et Footer peuvent être réutilisés dans n'importe quelle page de notre application.
  Les composants éliminent le besoin de réécrire le même JSX plusieurs fois.
*/

// Composant IndexPage, visible sur la route '/' de notre application
function IndexPage() {
  return (
    <div>
      <Header />
      <Hero />
      <Footer />
    </div>
  );
}

// Composant AboutPage, visible sur la route '/about'
function AboutPage() {
  return (
    <div>
      <Header />
      <About />
      <Testimonials />
      <Footer />
    </div>
  );
}
```

Les données passées aux composants en JavaScript sont appelées **props**. Les props ressemblent à des attributs sur des éléments JSX/HTML simples, mais vous pouvez accéder à leurs valeurs au sein du composant lui-même.

Les props sont disponibles dans les paramètres du composant auquel elles sont passées. Les props sont toujours incluses comme propriétés d'un objet.

```js
/* 
  Que faire si nous voulons passer des données personnalisées à notre composant depuis un composant parent ?
  Par exemple, pour afficher le nom de l'utilisateur dans l'en-tête de notre application.
*/

const username = "John";

/* 
  Pour ce faire, nous ajoutons des attributs personnalisés à notre composant appelés props.
  Nous pouvons en ajouter autant que nous le souhaitons et nous leur donnons des noms qui conviennent aux données que nous passons.
  Pour passer le nom de l'utilisateur à l'en-tête, nous utilisons une prop que nous avons appelée de manière appropriée 'username'
*/
ReactDOM.render(
  <Header username={username} />,
  document.getElementById("root")
);
// Nous avons appelé cette prop 'username', mais nous pouvons utiliser n'importe quel identifiant valide que nous donnerions, par exemple, une variable JavaScript

// props est l'objet que chaque composant reçoit comme argument
function Header(props) {
  // les props que nous créons sur le composant (username)
  // deviennent des propriétés de l'objet props
  return <h1>Bonjour {props.username}</h1>;
}
```

Les props ne doivent jamais être directement modifiées au sein du composant enfant.

Une autre façon de dire cela est que les props ne doivent jamais être **mutées**, puisque les props sont un objet JavaScript simple.

```js
/* 
  Les composants doivent fonctionner comme des fonctions 'pures'.
  C'est-à-dire, pour chaque entrée, nous devons pouvoir nous attendre à la même sortie.
  Cela signifie que nous ne pouvons pas muter l'objet props, seulement le lire.
*/

// Nous ne pouvons pas modifier l'objet props :
function Header(props) {
  props.username = "Doug";

  return <h1>Bonjour {props.username}</h1>;
}
/* 
  Mais que faire si nous voulons modifier une valeur de prop qui est passée à notre composant ?
  C'est là que nous utiliserions l'état (voir la section useState).
*/
```

La prop **children** est utile si nous voulons passer des éléments / composants comme props à d'autres composants.

```js
// Pouvez-nous accepter des éléments React (ou des composants) comme props ?
// Oui, via une propriété spéciale sur l'objet props appelée 'children'

function Layout(props) {
  return <div className="container">{props.children}</div>;
}

// La prop children est très utile lorsque vous voulez que le même
// composant (comme un composant Layout) enveloppe tous les autres composants :
function IndexPage() {
  return (
    <Layout>
      <Header />
      <Hero />
      <Footer />
    </Layout>
  );
}

// page différente, mais utilise le même composant Layout (grâce à la prop children)
function AboutPage() {
  return (
    <Layout>
      <About />
      <Footer />
    </Layout>
  );
}
```

Encore une fois, puisque les composants sont des expressions JavaScript, nous pouvons les utiliser en combinaison avec des instructions if-else et des instructions switch pour afficher conditionnellement du contenu, comme ceci :

```js
function Header() {
  const isAuthenticated = checkAuth();
    
  /* si l'utilisateur est authentifié, afficher l'application authentifiée, sinon, l'application non authentifiée */
  if (isAuthenticated) {
    return <AuthenticatedApp />   
  } else {
    /* alternativement, nous pouvons supprimer la section else et fournir un retour simple, et le conditionnel fonctionnera de la même manière */
    return <UnAuthenticatedApp />   
  }
}
```

Pour utiliser des conditions dans le JSX retourné par un composant, vous pouvez utiliser l'opérateur ternaire ou le court-circuitage (opérateurs && et ||).

```js
function Header() {
  const isAuthenticated = checkAuth();

  return (
    <nav>
      {/* si isAuth est vrai, ne rien afficher. Si faux, afficher Logo  */}
      {isAuthenticated || <Logo />}
      {/* si isAuth est vrai, afficher AuthenticatedApp. Si faux, afficher Login  */}
      {isAuthenticated ? <AuthenticatedApp /> : <LoginScreen />}
      {/* si isAuth est vrai, afficher Footer. Si faux, ne rien afficher */}
      {isAuthenticated && <Footer />}
    </nav>
  );
}
```

Les **Fragments** sont des composants spéciaux pour afficher plusieurs composants sans ajouter d'élément supplémentaire au DOM. Ils sont idéaux pour la logique conditionnelle qui a plusieurs composants ou éléments adjacents.

```js
/*
  Nous pouvons améliorer la logique dans l'exemple précédent.
  Si isAuthenticated est vrai, comment affichons-nous à la fois les composants AuthenticatedApp et Footer ?
*/
function Header() {
  const isAuthenticated = checkAuth();

  return (
    <nav>
      <Logo />
      {/* 
        Nous pouvons rendre les deux composants avec un fragment. 
        Les fragments sont très concis : <> </>
      */}
      {isAuthenticated ? (
        <>
          <AuthenticatedApp />
          <Footer />
        </>
      ) : (
        <Login />
      )}
    </nav>
  );
}
/* 
  Note : Une syntaxe alternative pour les fragments est React.Fragment :
  <React.Fragment>
     <AuthenticatedApp />
     <Footer />
  </React.Fragment>
*/
```

### Listes et Clés

Utilisez la fonction **.map()** pour convertir des listes de données (tableaux) en listes d'éléments.

```js
const people = ["John", "Bob", "Fred"];
const peopleList = people.map(person => <p>{person}</p>);

```

`.map()` peut être utilisé pour des composants ainsi que pour des éléments JSX simples.

```js
function App() {
  const people = ['John', 'Bob', 'Fred'];
  // peut interpoler la liste retournée d'éléments dans {}
  return (
    <ul>
      {/* nous passons chaque élément de tableau comme props à Person */}
      {people.map(person => <Person name={person} />}
    </ul>
  );
}

function Person({ name }) {
  // nous accédons à la prop 'name' directement en utilisant la destructuration d'objet
  return <p>Le nom de cette personne est : {name}</p>;
}
```

Chaque élément React dans une liste d'éléments a besoin d'une prop spéciale **key**. Les clés sont essentielles pour que React puisse garder une trace de chaque élément qui est itéré avec la fonction `.map()`.

React utilise les clés pour mettre à jour efficacement les éléments individuels lorsque leurs données changent (au lieu de re-rendre toute la liste).

Les clés doivent avoir des valeurs uniques pour pouvoir identifier chacune d'elles selon leur valeur de clé.

```js
function App() {
  const people = [
    { id: 'Ksy7py', name: 'John' },
    { id: '6eAdl9', name: 'Bob' },
    { id: '6eAdl9', name: 'Fred' },
  ];

  return (
    <ul>
      {/* les clés doivent être des valeurs primitives, idéalement une chaîne unique, comme un id */}
      {people.map(person =>
         <Person key={person.id} name={person.name} />
      )}
    </ul>
  );
}

// Si vous n'avez pas d'ids avec votre ensemble de données qui sont uniques // et des valeurs primitives, utilisez le deuxième paramètre de .map() pour obtenir chaque // index d'élément

function App() {
  const people = ['John', 'Bob', 'Fred'];

  return (
    <ul>
      {/* utilisez l'index de l'élément du tableau pour la clé */}
      {people.map((person, i) => <Person key={i} name={person} />)}
    </ul>
  );
}
```

### Écouteurs d'événements et Gestion des événements

Écouter les événements sur les éléments JSX par rapport aux éléments HTML diffère de plusieurs manières importantes.

Tout d'abord, vous ne pouvez pas écouter les événements sur les composants React – seulement sur les éléments JSX. Ajouter une prop appelée `onClick`, par exemple, à un composant React serait simplement une autre propriété ajoutée à l'objet props.

```js
/* 
  La convention pour la plupart des fonctions de gestion d'événements est de les préfixer avec le mot 'handle' puis l'action qu'elles effectuent (par exemple, handleToggleTheme)
*/
function handleToggleTheme() {
  // code pour basculer le thème de l'application
}

/* En HTML, onclick est tout en minuscules, plus le gestionnaire d'événements inclut un ensemble de parenthèses après avoir été référencé */
<button onclick="handleToggleTheme()">
  Basculer le thème
</button>

/* 
  En JSX, onClick est en camelCase, comme les attributs / props.
  Nous passons également une référence à la fonction avec des accolades.
*/
<button onClick={handleToggleTheme}>
  Basculer le thème
</button>
```

Les événements React les plus essentiels à connaître sont `onClick`, `onChange` et `onSubmit`.

* `onClick` gère les événements de clic sur les éléments JSX (notamment sur les boutons)
* `onChange` gère les événements de clavier (notamment un utilisateur tapant dans une entrée ou une zone de texte)
* `onSubmit` gère les soumissions de formulaire de l'utilisateur

```js
function App() {
  function handleInputChange(event) {
    /* Lorsque vous passez la fonction à un gestionnaire d'événements, comme onChange, nous obtenons l'accès aux données sur l'événement (un objet) */
    const inputText = event.target.value; // texte tapé dans l'entrée
    const inputName = event.target.name; // 'email' de l'attribut name
  }

  function handleClick(event) {
    /* onClick n'a généralement pas besoin de données d'événement, mais il reçoit également des données d'événement que nous pouvons utiliser */
    console.log('cliqué !');
    const eventType = event.type; // "click"
    const eventTarget = event.target; // <button>Submit</button>
  }
    
  function handleSubmit(event) {
    /* 
     Lorsque nous appuyons sur le bouton de retour, le formulaire sera soumis, ainsi que lorsque nous cliquons sur un bouton avec type="submit".
     Nous appelons event.preventDefault() pour empêcher le comportement par défaut du formulaire de se produire, qui est d'envoyer une requête HTTP et de recharger la page.
    */
    event.preventDefault();
    const formElements = event.target.elements; // accéder à tous les éléments dans le formulaire
    const inputValue = event.target.elements.emailAddress.value; // accéder à la valeur de l'élément d'entrée avec l'id "emailAddress"
  }

  return (
    <form onSubmit={handleSubmit}>
      <input id="emailAddress" type="email" name="email" onChange={handleInputChange} />
      <button onClick={handleClick}>Submit</button>
    </form>
  );
}

```

## Hooks essentiels de React

### État et useState

Le hook `useState` nous donne un état dans un composant fonctionnel. **L'état** nous permet d'accéder et de mettre à jour certaines valeurs dans nos composants au fil du temps.

L'état local du composant est géré par le hook React `useState` qui nous donne à la fois une variable d'état et une fonction qui nous permet de la mettre à jour.

Lorsque nous appelons `useState`, nous pouvons donner à notre état une valeur par défaut en la fournissant comme premier argument lorsque nous appelons `useState`.

```js
import React from 'react';

/* 
  Comment créer une variable d'état ?
  Syntaxe : const [stateVariable] = React.useState(defaultValue);
*/
function App() {
  const [language] = React.useState('JavaScript');
  /* 
    Nous utilisons la destructuration de tableau pour déclarer la variable d'état.
    Comme toute variable, nous pouvons la nommer comme nous le souhaitons (dans ce cas, 'language').
  */

  return <div>J'apprends {language}</div>;
}
```

Note : Tout hook dans cette section provient de la bibliothèque principale React et peut être importé individuellement.

```js
import React, { useState } from "react";

function App() {
  const [language] = useState("javascript");

  return <div>J'apprends {language}</div>;
}
```

`useState` nous donne également une fonction 'setter' pour mettre à jour l'état après sa création.

```js
function App() {
  /* 
   La fonction setter est toujours la deuxième valeur destructurée.
   La convention de nommage pour la fonction setter est d'être préfixée par 'set'.
  */
  const [language, setLanguage] = React.useState("javascript");

  return (
    <div>
      <button onClick={() => setLanguage("python")}>
        Apprendre Python
      </button>
      {/*  
        Pourquoi utiliser une fonction fléchée en ligne ici au lieu de l'appeler immédiatement comme suit : onClick={setterFn()}? 
        Si tel est le cas, setLanguage serait appelé immédiatement et non lorsque le bouton est cliqué par l'utilisateur.
        */}
      <p>J'apprends maintenant {language}</p>
    </div>
  );
}

/* 
 Note : chaque fois que la fonction setter est appelée, l'état est mis à jour,
 et le composant App est re-rendu pour afficher le nouvel état.
 Chaque fois que l'état est mis à jour, le composant sera re-rendu
*/
```

`useState` peut être utilisé une ou plusieurs fois dans un seul composant. Et il peut accepter des valeurs primitives ou des objets pour gérer l'état.

```js
function App() {
  const [language, setLanguage] = React.useState("python");
  const [yearsExperience, setYearsExperience] = React.useState(0);

  return (
    <div>
      <button onClick={() => setLanguage("javascript")}>
        Changer de langage pour JS
      </button>
      <input
        type="number"
        value={yearsExperience}
        onChange={event => setYearsExperience(event.target.value)}
      />
      <p>J'apprends maintenant {language}</p>
      <p>J'ai {yearsExperience} années d'expérience</p>
    </div>
  );
}
```

Si le nouvel état dépend de l'état précédent, pour garantir que la mise à jour est effectuée de manière fiable, nous pouvons utiliser une fonction dans la fonction setter qui nous donne l'état précédent correct.

```js
/* Nous avons la possibilité d'organiser l'état en utilisant le type de données le plus approprié, selon les données que nous gérons */
function App() {
  const [developer, setDeveloper] = React.useState({
    language: "",
    yearsExperience: 0
  });

  function handleChangeYearsExperience(event) {
    const years = event.target.value;
    /* Nous devons passer l'objet d'état précédent que nous avions avec l'opérateur de propagation pour étendre toutes ses propriétés */
    setDeveloper({ ...developer, yearsExperience: years });
  }

  return (
    <div>
      {/* Pas besoin d'obtenir l'état précédent ici ; nous remplaçons l'objet entier */}
      <button
        onClick={() =>
          setDeveloper({
            language: "javascript",
            yearsExperience: 0
          })
        }
      >
        Changer de langage pour JS
      </button>
      {/* Nous pouvons également passer une référence à la fonction */}
      <input
        type="number"
        value={developer.yearsExperience}
        onChange={handleChangeYearsExperience}
      />
      <p>J'apprends maintenant {developer.language}</p>
      <p>J'ai {developer.yearsExperience} années d'expérience</p>
    </div>
  );
}
```

Si vous gérez plusieurs valeurs primitives, utiliser `useState` plusieurs fois est souvent mieux que de l'utiliser une fois avec un objet. Vous n'avez pas à vous soucier d'oublier de combiner l'ancien état avec le nouvel état.

```js
function App() {
  const [developer, setDeveloper] = React.useState({
    language: "",
    yearsExperience: 0,
    isEmployed: false
  });

  function handleToggleEmployment(event) {
    /* Nous obtenons la valeur de la variable d'état précédente dans les paramètres.
       Nous pouvons nommer 'prevState' comme nous le souhaitons.
    */
    setDeveloper(prevState => {
      return { ...prevState, isEmployed: !prevState.isEmployed };
      // Il est essentiel de retourner le nouvel état depuis cette fonction
    });
  }

  return (
    <button onClick={handleToggleEmployment}>Basculer le statut d'emploi</button>
  );
}

```

### Effets de bord et useEffect

`useEffect` nous permet d'effectuer des effets de bord dans les composants fonctionnels. Alors, qu'est-ce que les effets de bord ?

**Les effets de bord** sont là où nous devons atteindre le monde extérieur. Par exemple, récupérer des données depuis une API ou travailler avec le DOM.

Ce sont des actions qui peuvent changer l'état de notre composant de manière imprévisible (qui ont causé des 'effets de bord').

`useEffect` accepte une fonction de rappel (appelée la fonction 'effet'), qui s'exécutera par défaut à chaque fois qu'il y a un re-rendu.

Il s'exécute une fois que notre composant est monté, ce qui est le bon moment pour effectuer un effet de bord dans le cycle de vie du composant.

```js
/* Que fait notre code ? Choisit une couleur dans le tableau des couleurs et en fait la couleur de fond */
import React, { useState, useEffect } from 'react';

function App() {
  const [colorIndex, setColorIndex] = useState(0);
  const colors = ["blue", "green", "red", "orange"];

  /* 
    Nous effectuons un 'effet de bord' puisque nous travaillons avec une API.
    Nous travaillons avec le DOM, une API de navigateur en dehors de React.
  */
  useEffect(() => {
    document.body.style.backgroundColor = colors[colorIndex];
  });
  /* Chaque fois que l'état est mis à jour, App est re-rendu et useEffect s'exécute */

  function handleChangeColor() {
    /* Ce code peut sembler complexe, mais tout ce qu'il fait est d'aller à la couleur suivante dans le tableau 'colors', et s'il est sur la dernière couleur, il revient au début */
    const nextIndex = colorIndex + 1 === colors.length ? 0 : colorIndex + 1;
    setColorIndex(nextIndex);
  }

  return (
    <button onClick={handleChangeColor}>
      Changer la couleur de fond
    </button>
  );
}
```

Pour éviter d'exécuter la fonction de rappel de l'effet après chaque rendu, nous fournissons un deuxième argument, un tableau vide.

```js
function App() {
  ...
  /* 
    Avec un tableau vide, notre bouton ne fonctionne pas peu importe le nombre de fois où nous cliquons dessus... 
    La couleur de fond n'est définie qu'une seule fois, lorsque le composant est monté pour la première fois.
  */
  useEffect(() => {
    document.body.style.backgroundColor = colors[colorIndex];
  }, []);

  /* 
    Comment faire pour que la fonction d'effet ne s'exécute pas pour chaque mise à jour d'état, mais qu'elle fonctionne toujours lorsque le bouton est cliqué ? 
  */

  return (
    <button onClick={handleChangeIndex}>
      Changer la couleur de fond
    </button>
  );
}
```

`useEffect` nous permet d'effectuer des effets de manière conditionnelle avec le tableau des dépendances.

Le **tableau des dépendances** est le deuxième argument et si l'une des valeurs du tableau change, la fonction d'effet s'exécute à nouveau.

```js
function App() {
  const [colorIndex, setColorIndex] = React.useState(0);
  const colors = ["blue", "green", "red", "orange"];

  /* 
    Ajoutons colorIndex à notre tableau des dépendances
    Lorsque colorIndex change, useEffect exécutera à nouveau la fonction d'effet
  */
  useEffect(() => {
    document.body.style.backgroundColor = colors[colorIndex];
    /* 
      Lorsque nous utilisons useEffect, nous devons réfléchir aux valeurs d'état
      avec lesquelles nous voulons que notre effet de bord se synchronise
    */
  }, [colorIndex]);

  function handleChangeIndex() {
    const next = colorIndex + 1 === colors.length ? 0 : colorIndex + 1;
    setColorIndex(next);
  }

  return (
    <button onClick={handleChangeIndex}>
      Changer la couleur de fond
    </button>
  );
}
```

`useEffect` nous permet de nous désabonner de certains effets en retournant une fonction à la fin.

```js
function MouseTracker() {
  const [mousePosition, setMousePosition] = useState({ x: 0, y: 0 });

  React.useEffect(() => {
    // .addEventListener() configure un écouteur actif...
    window.addEventListener("mousemove", handleMouseMove);

    /* ...Donc lorsque nous naviguons loin de cette page, il doit être
       supprimé pour arrêter d'écouter. Sinon, il essaiera de définir
       l'état dans un composant qui n'existe pas (provoquant une erreur)

     Nous nous désabonnons de tous les abonnements / écouteurs avec cette 'fonction de nettoyage')
     */
    return () => {
      window.removeEventListener("mousemove", handleMouseMove);
    };
  }, []);

function handleMouseMove(event) {
   setMousePosition({
     x: event.pageX,
     y: event.pageY
   });
}

  return (
    <div>
      <h1>La position actuelle de la souris est :</h1>
      <p>
        X: {mousePosition.x}, Y: {mousePosition.y}
      </p>
    </div>
  );
}
```

`useEffect` est le hook à utiliser lorsque vous souhaitez faire une requête HTTP (notamment, une requête GET lorsque le composant est monté).

Notez que la gestion des promesses avec la syntaxe plus concise async/await nécessite la création d'une fonction séparée. (Pourquoi ? La fonction de rappel de l'effet ne peut pas être asynchrone.)

```js
const endpoint = "https://api.github.com/users/reedbarger";

// Utilisation des fonctions de rappel .then() pour résoudre la promesse
function App() {
  const [user, setUser] = React.useState(null);

  React.useEffect(() => {
    fetch(endpoint)
      .then(response => response.json())
      .then(data => setUser(data));
  }, []);
}

// Utilisation de la syntaxe async / await pour résoudre la promesse :
function App() {
  const [user, setUser] = React.useState(null);
  // ne peut pas rendre la fonction de rappel useEffect asynchrone
  React.useEffect(() => {
    getUser();
  }, []);

  // Nous devons appliquer le mot-clé async à une fonction séparée
  async function getUser() {
    const response = await fetch(endpoint);
    const data = await response.json();
    setUser(data);
  }
}

```

### Refs et useRef

**Les Refs** sont un attribut spécial disponible sur tous les composants React. Ils nous permettent de créer une référence à un élément/composant donné lorsque le composant est monté.

`useRef` nous permet d'utiliser facilement les refs React. Nous appelons useRef (en haut du composant) et attachons la valeur retournée à l'attribut ref de l'élément pour y faire référence.

Une fois que nous avons créé une référence, nous utilisons la propriété current pour modifier (muter) les propriétés de l'élément ou pouvons appeler toute méthode disponible sur cet élément (comme `.focus()` pour focaliser une entrée).

```js
function App() {
  const [query, setQuery] = React.useState("react hooks");
  /* Nous pouvons passer une valeur par défaut à useRef.
     Nous n'en avons pas besoin ici, donc nous passons null pour référencer un objet vide
  */
  const searchInput = useRef(null);

  function handleClearSearch() {
    /* 
      .current fait référence à l'élément input lors du montage
      useRef peut stocker pratiquement n'importe quelle valeur dans sa propriété .current
    */
    searchInput.current.value = "";
    searchInput.current.focus();
  }

  return (
    <form>
      <input
        type="text"
        onChange={event => setQuery(event.target.value)}
        ref={searchInput}
      />
      <button type="submit">Rechercher</button>
      <button type="button" onClick={handleClearSearch}>
        Effacer
      </button>
    </form>
  );
}

```

## Hooks et Performance

### Prévenir les re-rendus et React.memo

`React.memo` est une fonction qui nous permet d'optimiser la façon dont nos composants sont rendus.

En particulier, elle effectue un processus appelé **mémoisation** qui nous aide à empêcher nos composants de se re-rendre lorsqu'ils n'en ont pas besoin (voir React.useMemo pour une définition plus complète de la mémoisation).

`React.memo` aide principalement à empêcher les listes de composants d'être re-rendues lorsque leurs composants parents sont re-rendus.

```js
/* 
  Dans l'application suivante, nous suivons nos compétences en programmation. Nous pouvons créer de nouvelles compétences en utilisant une entrée, et elles sont ajoutées à la liste (affichée dans le composant SkillList). Si nous cliquons sur une compétence, elle est supprimée.
*/

function App() {
  const [skill, setSkill] = React.useState('')
  const [skills, setSkills] = React.useState([
    'HTML', 'CSS', 'JavaScript'
  ])

  function handleChangeInput(event) {
    setSkill(event.target.value);
  }

  function handleAddSkill() {
    setSkills(skills.concat(skill))
  }

  return (
    <>
      <input onChange={handleChangeInput} />
      <button onClick={handleAddSkill}>Ajouter une compétence</button>
      <SkillList skills={skills} />
    </>
  );
}

/* Mais le problème, si vous exécutez ce code vous-même, est que lorsque nous tapons dans l'entrée, parce que le composant parent de SkillList (App) se re-rend, en raison de la mise à jour de l'état à chaque frappe, le SkillList est constamment re-rendu (comme indiqué par le console.log) */

/* Cependant, une fois que nous enveloppons le composant SkillList dans React.memo (qui est une fonction d'ordre supérieur, ce qui signifie qu'elle accepte une fonction comme argument), il ne se re-rend plus inutilement lorsque notre composant parent le fait. */
const SkillList = React.memo(({ skills }) => {
  console.log('re-rendu');
  return (
    <ul>
    {skills.map((skill, i) => <li key={i}>{skill}</li>)}
    </ul>
  )
})

export default App
```

### Fonctions de rappel et useCallback

`useCallback` est un hook utilisé pour améliorer les performances de nos composants. Les **fonctions de rappel** sont le nom des fonctions qui sont "rappelées" dans un composant parent.

L'utilisation la plus courante est d'avoir un composant parent avec une variable d'état, mais vous voulez mettre à jour cet état à partir d'un composant enfant. Que faites-vous ? Vous passez une fonction de rappel de l'enfant au parent. Cela nous permet de mettre à jour l'état dans le composant parent.

`useCallback` fonctionne de manière similaire à `React.memo`. Il mémoïse les fonctions de rappel, donc elle n'est pas recréée à chaque re-rendu. Utiliser `useCallback` correctement peut améliorer les performances de notre application.

```js
/* Gardons exactement la même App que ci-dessus avec React.memo, mais ajoutons une petite fonctionnalité. Rendons possible la suppression d'une compétence lorsque nous cliquons dessus. Pour ce faire, nous devons filtrer le tableau des compétences selon la compétence sur laquelle nous cliquons. Pour cela, nous créons la fonction handleRemoveSkill dans App */

function App() {
  const [skill, setSkill] = React.useState('')
  const [skills, setSkills] = React.useState([
    'HTML', 'CSS', 'JavaScript'
  ])

  function handleChangeInput(event) {
    setSkill(event.target.value);
  }

  function handleAddSkill() {
    setSkills(skills.concat(skill))
  }

  function handleRemoveSkill(skill) {
    setSkills(skills.filter(s => s !== skill))
  }
    
  /* Ensuite, nous passons handleRemoveSkill comme une prop, ou puisque c'est une fonction, comme une fonction de rappel à utiliser dans SkillList */
  return (
    <>
      <input onChange={handleChangeInput} />
      <button onClick={handleAddSkill}>Ajouter une compétence</button>
      <SkillList skills={skills} handleRemoveSkill={handleRemoveSkill} />
    </>
  );
}

/* Lorsque nous essayons de taper à nouveau dans l'entrée, nous voyons un re-rendu dans la console à chaque fois que nous tapons. Notre mémoisation de React.memo est cassée ! 

Ce qui se passe, c'est que la fonction de rappel handleRemoveSkill est recréée chaque fois que App est re-rendu, ce qui entraîne le re-rendu de tous les enfants également. Nous devons envelopper handleRemoveSkill dans useCallback et ne le recréer que lorsque la valeur de la compétence change.

Pour corriger notre application, remplacez handleRemoveSkill par :

const handleRemoveSkill = React.useCallback((skill) => {
  setSkills(skills.filter(s => s !== skill))
}, [skills])

Essayez-le vous-même !
*/
const SkillList = React.memo(({ skills, handleRemoveSkill }) => {
  console.log('re-rendu');
  return (
    <ul>
    {skills.map(skill => <li key={skill} onClick={() => handleRemoveSkill(skill)}>{skill}</li>)}
    </ul>
  )
})


export default App
```

### Mémoisation et useMemo

`useMemo` est très similaire à `useCallback` et est utilisé pour améliorer les performances. Mais au lieu d'être pour les rappels, il est pour stocker les résultats de calculs coûteux.

`useMemo` nous permet de **mémoïser**, ou de nous souvenir du résultat de calculs coûteux lorsqu'ils ont déjà été faits pour certaines entrées.

La mémoisation signifie que si un calcul a déjà été fait avec une entrée donnée, il n'est pas nécessaire de le refaire, car nous avons déjà le résultat stocké de cette opération.

`useMemo` retourne une valeur du calcul, qui est ensuite stockée dans une variable.

```js
/* En nous basant sur notre application de compétences, ajoutons une fonctionnalité pour rechercher dans nos compétences disponibles via une entrée de recherche supplémentaire. Nous pouvons ajouter cela dans un composant appelé SearchSkills (affiché au-dessus de notre SkillList).
*/

function App() {
  const [skill, setSkill] = React.useState('')
  const [skills, setSkills] = React.useState([
    'HTML', 'CSS', 'JavaScript', ...thousands more items
  ])

  function handleChangeInput(event) {
    setSkill(event.target.value);
  }

  function handleAddSkill() {
    setSkills(skills.concat(skill))
  }

  const handleRemoveSkill = React.useCallback((skill) => {
    setSkills(skills.filter(s => s !== skill))
  }, [skills])
   
  return (
    <>
      <SearchSkills skills={skills} />
      <input onChange={handleChangeInput} />
      <button onClick={handleAddSkill}>Ajouter une compétence</button>
      <SkillList skills={skills} handleRemoveSkill={handleRemoveSkill} />
    </>
  );
}

/* Imaginons que nous avons une liste de milliers de compétences que nous voulons rechercher. Comment trouvons-nous et affichons-nous efficacement les compétences qui correspondent à notre terme de recherche lorsque l'utilisateur tape dans l'entrée ? */
function SearchSkills() {
  const [searchTerm, setSearchTerm] = React.useState('');  
      
  /* Nous utilisons React.useMemo pour mémoïser (se souvenir) la valeur retournée de notre opération de recherche et ne l'exécuter que lorsque le searchTerm change */
  const searchResults = React.useMemo(() => {
    return skills.filter((s) => s.includes(searchTerm);
  }), [searchTerm]);
    
  function handleSearchInput(event) {
    setSearchTerm(event.target.value);
  }
    
  return (
    <>
    <input onChange={handleSearchInput} />
    <ul>
      {searchResults.map((result, i) => <li key={i}>{result}</li>
    </ul>
    </>
  );
}


export default App
```

## Hooks avancés de React

### Contexte et useContext

Dans React, nous voulons éviter le problème suivant de création de plusieurs props pour passer des données sur deux niveaux ou plus depuis un composant parent.

```js
/* 
  React Context nous aide à éviter de créer plusieurs props en double.
  Ce motif est également appelé props drilling.
*/

/* Dans cette application, nous voulons passer les données de l'utilisateur au composant Header, mais elles doivent d'abord passer par un composant Main qui ne les utilise pas */
function App() {
  const [user] = React.useState({ name: "Fred" });

  return (
    // Première prop 'user'
    <Main user={user} />
  );
}

const Main = ({ user }) => (
  <>
    {/* Deuxième prop 'user' */}
    <Header user={user} />
    <div>Contenu principal de l'application...</div>
  </>
);

const Header = ({ user }) => <header>Bienvenue, {user.name} !</header>;
```

Le contexte est utile pour passer des props à travers plusieurs niveaux de composants enfants depuis un composant parent.

```js
/* 
  Voici l'exemple précédent réécrit avec Context.
  Tout d'abord, nous créons un contexte, où nous pouvons passer des valeurs par défaut
  Nous appelons cela 'UserContext' parce que nous passons des données utilisateur
*/
const UserContext = React.createContext();

function App() {
  const [user] = React.useState({ name: "Fred" });

  return (
    {/* 
      Nous enveloppons le composant parent avec la propriété Provider 
      Nous passons les données dans l'arborescence des composants sur la prop value
     */}
    <UserContext.Provider value={user}>
      <Main />
    </UserContext.Provider>
  );
}

const Main = () => (
  <>
    <Header />
    <div>Contenu principal de l'application</div>
  </>
);

/* 
  Nous ne pouvons pas supprimer les deux props 'user'. Au lieu de cela, nous pouvons simplement utiliser la propriété Consumer pour consommer les données là où nous en avons besoin
*/
const Header = () => (
    {/* Nous utilisons un motif appelé render props pour accéder aux données */}
    <UserContext.Consumer>
      {user => <header>Bienvenue, {user.name} !</header>}
    </UserContext.Consumer>
);
```

Le hook `useContext` nous permet de consommer le contexte dans n'importe quel composant fonctionnel qui est un enfant du Provider, au lieu d'utiliser le motif render props.

```js
function Header() {
  /* Nous passons l'objet contexte entier pour le consommer et nous pouvons supprimer les balises Consumer */
  const user = React.useContext(UserContext);
    
  return <header>Bienvenue, {user.name} !</header>;
};

```

### Réducteurs et useReducer

Les réducteurs sont des fonctions simples, prévisibles (pures) qui prennent un objet d'état précédent et un objet d'action et retournent un nouvel objet d'état.

```js
/* Ce réducteur gère l'état de l'utilisateur dans notre application : */

function userReducer(state, action) {
  /* Les réducteurs utilisent souvent une instruction switch pour mettre à jour l'état d'une manière ou d'une autre en fonction de la propriété type de l'action */
    
  switch (action.type) {
    /* Si action.type a la chaîne 'LOGIN' sur elle, nous obtenons des données de l'objet payload sur action */
    case "LOGIN":
      return { 
        username: action.payload.username, 
        email: action.payload.email
        isAuth: true 
      };
    case "SIGNOUT":
      return { 
        username: "",
        email: "",
        isAuth: false 
      };
    default:
      /* Si aucun cas ne correspond à l'action reçue, retourner l'état précédent */
      return state;
  }
}
```

Les réducteurs sont un motif puissant pour gérer l'état qui est utilisé dans la bibliothèque de gestion d'état populaire Redux (communément utilisée avec React).

Les réducteurs peuvent être utilisés dans React avec le hook `useReducer` afin de gérer l'état dans notre application, par rapport à useState (qui est pour l'état local du composant).

`useReducer` peut être associé à `useContext` pour gérer les données et les passer facilement entre les composants.

Ainsi, `useReducer` + `useContext` peuvent être un système complet de gestion d'état pour nos applications.

```js
const initialState = { username: "", isAuth: false };

function reducer(state, action) {
  switch (action.type) {
    case "LOGIN":
      return { username: action.payload.username, isAuth: true };
    case "SIGNOUT":
      // pourrait également étendre initialState ici
      return { username: "", isAuth: false };
    default:
      return state;
  }
}

function App() {
  // useReducer nécessite une fonction de réducteur à utiliser et un initialState
  const [state, dispatch] = useReducer(reducer, initialState);
  // nous obtenons le résultat actuel du réducteur sur 'state'

  // nous utilisons dispatch pour 'dispatcher' des actions, pour exécuter notre réducteur
  // avec les données dont il a besoin (l'objet action)
  function handleLogin() {
    dispatch({ type: "LOGIN", payload: { username: "Ted" } });
  }

  function handleSignout() {
    dispatch({ type: "SIGNOUT" });
  }

  return (
    <>
      Utilisateur actuel : {state.username}, estAuthentifié : {state.isAuth}
      <button onClick={handleLogin}>Connexion</button>
      <button onClick={handleSignout}>Déconnexion</button>
    </>
  );
}
```

### Écrire des hooks personnalisés

Les hooks ont été créés pour réutiliser facilement le comportement entre les composants, de manière similaire à la façon dont les composants ont été créés pour réutiliser la structure dans notre application.

Les hooks nous permettent d'ajouter des fonctionnalités personnalisées à nos applications qui répondent à nos besoins et peuvent être combinées avec tous les hooks existants que nous avons couverts.

Les hooks peuvent également être inclus dans des bibliothèques tierces pour le bien de tous les développeurs React. Il existe de nombreuses excellentes bibliothèques React qui fournissent des hooks personnalisés tels que `@apollo/client`, `react-query`, `swr` et bien d'autres.

```js
/* Voici un hook React personnalisé appelé useWindowSize que j'ai écrit afin de calculer la taille de la fenêtre (largeur et hauteur) de tout composant dans lequel il est utilisé */

import React from "react";

export default function useWindowSize() {
  const isSSR = typeof window !== "undefined";
  const [windowSize, setWindowSize] = React.useState({
    width: isSSR ? 1200 : window.innerWidth,
    height: isSSR ? 800 : window.innerHeight,
  });

  function changeWindowSize() {
    setWindowSize({ width: window.innerWidth, height: window.innerHeight });
  }

  React.useEffect(() => {
    window.addEventListener("resize", changeWindowSize);

    return () => {
      window.removeEventListener("resize", changeWindowSize);
    };
  }, []);

  return windowSize;
}

/* Pour utiliser le hook, nous devons simplement l'importer là où nous en avons besoin, l'appeler, et utiliser la largeur où nous voulons masquer ou afficher certains éléments, comme dans un composant Header. */

// components/Header.js

import React from "react";
import useWindowSize from "../utils/useWindowSize";

function Header() {
  const { width } = useWindowSize();

  return (
    <div>
      {/* visible uniquement lorsque la fenêtre est supérieure à 500px */}
      {width > 500 && (
        <>
         Supérieur à 500px !
        </>
      )}
      {/* visible à n'importe quelle taille de fenêtre */}
	  <p>Je suis toujours visible</p>
    </div>
  );
}
```

### Règles des hooks

Il existe deux règles essentielles pour utiliser les hooks React que nous ne pouvons pas violer pour qu'ils fonctionnent correctement :

* Les hooks ne peuvent être utilisés qu'au sein de composants fonctionnels (et non dans des fonctions JavaScript simples ou des composants de classe)
* Les hooks ne peuvent être appelés qu'au sommet des composants (ils ne peuvent pas être dans des conditionnels, des boucles ou des fonctions imbriquées)

## **Conclusion**

Il existe d'autres concepts valables que vous pouvez apprendre, mais si vous vous engagez à apprendre les concepts couverts dans ce guide, vous aurez une excellente compréhension des parties les plus importantes et puissantes de la bibliothèque React.

_Voulez-vous garder ce guide pour référence future ?_

**[Téléchargez une version PDF complète de ce guide ici.](https://reedbarger.com/resources/the-react-cheatsheet-for-2021)**

## Devenez un développeur React professionnel

React est difficile. Vous ne devriez pas avoir à le comprendre par vous-même.

J'ai mis tout ce que je sais sur React dans un seul cours, pour vous aider à atteindre vos objectifs en un temps record :

[**Présentation : Le React Bootcamp**](https://www.thereactbootcamp.com)

**C'est le seul cours que j'aurais aimé avoir lorsque j'ai commencé à apprendre React.**

Cliquez ci-dessous pour essayer le React Bootcamp par vous-même :

[![Cliquez pour rejoindre le React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Cliquez pour commencer*