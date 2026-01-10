---
title: Les compétences JavaScript dont vous avez besoin pour React (+ exemples pratiques)
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2021-01-16T16:49:15.000Z'
originalURL: https://freecodecamp.org/news/javascript-skills-you-need-for-react-practical-examples
coverImage: https://www.freecodecamp.org/news/content/images/2021/01/7-js-skills-for-react.png
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
seo_title: Les compétences JavaScript dont vous avez besoin pour React (+ exemples
  pratiques)
seo_desc: 'One of the most important things to understand about React is that it is
  fundamentally JavaScript. This means that the better you are at JavaScript, the
  more successful you will be with React.

  Let''s break down the 7 essential concepts that you should...'
---

L'une des choses les plus importantes à comprendre à propos de React est qu'il est fondamentalement du JavaScript. Cela signifie que plus vous maîtrisez JavaScript, plus vous réussirez avec React.

**Décomposons les 7 concepts essentiels que vous devez connaître en JavaScript pour maîtriser React.**

Et lorsque je dis que ces concepts sont essentiels, je veux dire qu'ils sont utilisés dans chaque application qu'un développeur React crée, avec peu ou pas d'exceptions.

Apprendre ces concepts est l'une des choses les plus précieuses que vous puissiez faire pour accélérer votre capacité à créer des projets React et devenir un développeur React compétent, alors commençons.

## Vous voulez votre propre copie de ce guide ?

**[Téléchargez l'aide-mémoire au format PDF ici](https://reedbarger.com/resources/7-javascript-skills-for-react)** (cela prend 5 secondes).

## 1. Déclarations de fonctions et fonctions fléchées

La base de toute application React est le **composant**. Dans React, les composants sont définis avec des fonctions et des classes JavaScript.

Mais contrairement aux fonctions JavaScript, les composants React retournent des éléments JSX qui sont utilisés pour structurer l'interface de notre application.

```js
// Fonction JavaScript : retourne n'importe quel type JavaScript valide
function javascriptFunction() {
  return "Hello world";
}

// Composant de fonction React : retourne JSX
function ReactComponent(props) {
  return <h1>{props.content}</h1>;
}

```

Notez la différence de casse entre les noms des fonctions JavaScript et des composants de fonction React. Les fonctions JavaScript sont nommées en camel case, tandis que les composants de fonction React sont écrits en pascal case (dans lequel tous les mots sont capitalisés).

Il existe deux façons différentes d'écrire une fonction en JavaScript : la manière traditionnelle, en utilisant le mot-clé `function`, appelée **déclaration de fonction**, et en tant que **fonction fléchée**, qui a été introduite dans ES6.

Les déclarations de fonctions et les fonctions fléchées peuvent être utilisées pour écrire des composants de fonction dans React.

L'avantage principal des fonctions fléchées est leur concision. Nous pouvons utiliser plusieurs raccourcis afin d'écrire nos fonctions pour supprimer le code inutile, de sorte que nous pouvons même tout écrire sur une seule ligne.

```js
// Syntaxe de déclaration de fonction
function MyComponent(props) {
  return <div>{props.content}</div>;
}

// Syntaxe de fonction fléchée
const MyComponent = (props) => {
  return <div>{props.content}</div>;
};

// Syntaxe de fonction fléchée (raccourcie)
const MyComponent = (props) => <div>{props.content}</div>;

/*
Dans le dernier exemple, nous utilisons plusieurs raccourcis que les fonctions fléchées permettent :

1. Pas de parenthèses autour d'un seul paramètre
2. Retour implicite (par rapport à l'utilisation du mot-clé "return")
3. Pas d'accolades pour le corps de la fonction
*/

```

Un petit avantage de l'utilisation des déclarations de fonctions par rapport aux fonctions fléchées est que vous n'avez pas à vous soucier des problèmes de **hoisting**.

En raison du comportement de hoisting de JavaScript, vous pouvez utiliser plusieurs composants de fonction créés avec des déclarations de fonction dans un seul fichier dans l'ordre que vous souhaitez.

Les composants de fonction créés avec des fonctions fléchées, cependant, ne peuvent pas être ordonnés de la manière que vous souhaitez. Parce que les variables JavaScript sont hoistées, les composants de fonction fléchée doivent être déclarés avant d'être utilisés :

```js
function App() {
  return (
    <>
      {/* Valide ! FunctionDeclaration est hoistée */}
      <FunctionDeclaration />
      {/* Invalide ! ArrowFunction n'est PAS hoistée. Par conséquent, elle doit être déclarée avant d'être utilisée */}
      <ArrowFunction />
    </>
  );
}

function FunctionDeclaration() {
  return <div>Hello React !</div>;
}

function ArrowFunction() {
  return <div>Hello React, encore !</div>;
}

```

Une autre petite différence dans l'utilisation de la syntaxe de déclaration de fonction est que vous pouvez immédiatement exporter un composant depuis un fichier en utilisant `export default` ou `export` avant que la fonction ne soit déclarée. Vous ne pouvez utiliser le mot-clé `export` qu'avant les fonctions fléchées (les exports par défaut doivent être placés sur une ligne en dessous du composant).

```js
// La syntaxe de déclaration de fonction peut être immédiatement exportée avec export default ou export
export default function App() {
  return <div>Hello React</div>;
}

// La syntaxe de fonction fléchée doit utiliser uniquement export
export const App = () => {
  return <div>Hello React</div>;
};

```

## 2. Littéraux de gabarit

JavaScript a une histoire maladroite de travail avec les chaînes de caractères, en particulier si vous voulez **concaténer** ou connecter plusieurs chaînes ensemble. Avant l'arrivée de ES6, pour ajouter des chaînes ensemble, vous deviez utiliser l'opérateur `+` pour ajouter chaque segment de chaîne à un autre.

Avec l'ajout de ES6, nous avons reçu une nouvelle forme de chaîne appelée **littéral de gabarit**, qui consiste en deux backticks ```` au lieu de guillemets simples ou doubles.

Au lieu d'avoir à utiliser l'opérateur `+`, nous pouvons connecter des chaînes en plaçant une expression JavaScript (comme une variable) dans une syntaxe spéciale `${}` :

```js
/*
Concaténation de chaînes avant ES6.
Remarquez l'espace maladroit après le mot Hello ?
*/
function sayHello(text) {
  return "Hello " + text + "!";
}

sayHello("React"); // Hello React!

/*
Concaténation de chaînes en utilisant des littéraux de gabarit.
Voyez à quel point ce code est plus lisible et prévisible ?
*/
function sayHelloAgain(text) {
  return `Hello again, ${text}!`;
}

sayHelloAgain("React"); // Hello again, React!

```

Ce qui est puissant avec les littéraux de gabarit, c'est leur capacité à utiliser n'importe quelle expression JavaScript (c'est-à-dire tout ce qui en JavaScript se résout en une valeur) dans la syntaxe `${}`.

Nous pouvons même inclure une logique conditionnelle en utilisant l'opérateur ternaire, ce qui est parfait pour ajouter ou supprimer conditionnellement une classe ou une règle de style à un élément JSX donné :

```js
/* Allez sur react.new et collez ce code pour le voir fonctionner ! */
import React from "react";

function App() {
  const [isRedColor, setRedColor] = React.useState(false);

  const toggleColor = () => setRedColor((prev) => !prev);

  return (
    <button
      onClick={toggleColor}
      style={{
        background: isRedColor ? "red" : "black",
        color: "white",
      }}
    >
      Button is {isRedColor ? "red" : "not red"}
    </button>
  );
}

export default App;

```

En bref, les littéraux de gabarit sont parfaits pour React chaque fois que nous devons créer dynamiquement des chaînes. Par exemple, lorsque nous utilisons des valeurs de chaîne qui peuvent changer dans nos éléments head ou body de notre site :

```js
import React from "react";
import Head from "./Head";

function Layout(props) {
  // Affiche le nom du site (c'est-à-dire Reed Barger) à la fin du titre de la page
  const title = `${props.title} | Reed Barger`;

  return (
    <>
      <Head>
        <title>{title}</title>
      </Head>
      <main>{props.children}</main>
    </>
  );
}

```

## 3. Conditionnels courts : &&, ||, Opérateur ternaire

Considérant que React est simplement du JavaScript, il est très facile d'afficher (ou de masquer) conditionnellement des éléments JSX en utilisant des instructions if simples et parfois des instructions switch.

```js
import React from "react";

function App() {
  const isLoggedIn = true;

  if (isLoggedIn) {
    // Affiche : Welcome back!
    return <div>Welcome back!</div>;
  }

  return <div>Who are you?</div>;
}

export default App;

```

Avec l'aide de certains opérateurs JavaScript essentiels, nous réduisons la répétition et rendons notre code plus concis.

Nous pouvons transformer l'instruction if ci-dessus en ce qui suit, en utilisant l'**opérateur ternaire**. L'opérateur ternaire fonctionne exactement de la même manière qu'une instruction if, mais il est plus court, c'est une expression (pas une instruction), et peut être inséré dans JSX :

```js
import React from "react";

function App() {
  const isLoggedIn = true;

  // Affiche : Welcome back!
  return isLoggedIn ? <div>Welcome back!</div> : <div>Who are you?</div>;
}

export default App;

```

Les opérateurs ternaires peuvent également être utilisés à l'intérieur des accolades (encore une fois, puisque c'est une expression) :

```js
import React from "react";

function App() {
  const isLoggedIn = true;

  // Affiche : Welcome back!
  return <div>{isLoggedIn ? "Welcome back!" : "Who are you?"}</div>;
}

export default App;

```

Si nous devions changer l'exemple ci-dessus et ne vouloir afficher du texte que si l'utilisateur est connecté (si `isLoggedIn` est vrai), ce serait un excellent cas d'utilisation pour l'opérateur `&&` (et).

Si la première valeur (**opérande**) dans le conditionnel est vraie, l'opérateur `&&` affiche le deuxième opérande. Sinon, il retourne le premier opérande. Et puisque c'est **falsy** (est une valeur automatiquement convertie en booléen `false` par JavaScript), il n'est pas rendu par JSX :

```js
import React from "react";

function App() {
  const isLoggedIn = true;

  // Si vrai : Welcome back!, si faux : rien
  return <div>{isLoggedIn && "Welcome back!"}</div>;
}

export default App;

```

Supposons que nous voulons l'inverse de ce que nous faisons maintenant : ne dire "Who are you?" que si `isLoggedIn` est faux. Si c'est vrai, nous n'afficherons rien.

Pour cette logique, nous pouvons utiliser l'opérateur `||` (ou). Il fonctionne essentiellement à l'opposé de l'opérateur `&&`. Si le premier opérande est vrai, le premier opérande (falsy) est retourné. Si le premier opérande est faux, le deuxième opérande est retourné.

```js
import React from "react";

function App() {
  const isLoggedIn = true;

  // Si vrai : rien, si faux : Who are you?
  return <div>{isLoggedIn || "Who are you?"}</div>;
}

export default App;

```

## 4. Trois méthodes de tableau : .map(), .filter(), .reduce()

Insérer des valeurs primitives dans des éléments JSX est facile – il suffit d'utiliser des accolades.

Nous pouvons insérer n'importe quelle expression valide, y compris des variables qui contiennent des valeurs primitives (chaînes, nombres, booléens, etc.) ainsi que des propriétés d'objet qui contiennent des valeurs primitives.

```js
import React from "react";

function App() {
  const name = "Reed";
  const bio = {
    age: 28,
    isEnglishSpeaker: true,
  };

  return (
    <>
      <h1>{name}</h1>
      <h2>I am {bio.age} years old</h2>
      <p>Speaks English: {bio.isEnglishSpeaker}</p>
    </>
  );
}

export default App;

```

Et si nous avons un tableau et que nous voulons itérer sur ce tableau pour afficher chaque élément de tableau dans un élément JSX individuel ?

Pour cela, nous pouvons utiliser la méthode `**.map()**`. Elle nous permet de transformer chaque élément de notre tableau de la manière que nous spécifions avec la fonction interne.

Notez qu'elle est particulièrement concise lorsqu'elle est utilisée en combinaison avec une fonction fléchée.

```js
/* Notez que ceci n'est pas exactement la même chose que la méthode JavaScript .map() normale, mais est très similaire. */
import React from "react";

function App() {
  const programmers = ["Reed", "John", "Jane"];

  return (
    <ul>
      {programmers.map((programmer) => (
        <li>{programmer}</li>
      ))}
    </ul>
  );
}

export default App;

```

Il existe d'autres variantes de la méthode .map() qui effectuent des tâches connexes et sont importantes à connaître car elles peuvent être enchaînées en combinaison les unes avec les autres.

Pourquoi ? Parce que `.map()`, comme de nombreuses méthodes de tableau, retourne une copie superficielle du tableau sur lequel il a itéré. Cela permet à son tableau retourné d'être passé à la méthode suivante dans la chaîne.

`**.filter()**`, comme son nom l'indique, nous permet de filtrer certains éléments de notre tableau. Par exemple, si nous voulions supprimer tous les noms de programmeurs qui commencent par "J", nous pourrions le faire avec `.filter()` :

```js
import React from "react";

function App() {
  const programmers = ["Reed", "John", "Jane"];

  return (
    <ul>
      {/* Retourne 'Reed' */}
      {programmers
        .filter((programmer) => !programmer.startsWith("J"))
        .map((programmer) => (
          <li>{programmer}</li>
        ))}
    </ul>
  );
}

export default App;

```

Il est important de comprendre que `.map()` et `.filter()` ne sont que différentes variations de la méthode de tableau `**.reduce()**`, qui est capable de transformer les valeurs de tableau en pratiquement n'importe quel type de données, même des valeurs non-tableau.

Voici `.reduce()` effectuant la même opération que notre méthode `.filter()` ci-dessus :

```js
import React from "react";

function App() {
  const programmers = ["Reed", "John", "Jane"];

  return (
    <ul>
      {/* Retourne 'Reed' */}
      {programmers
        .reduce((acc, programmer) => {
          if (!programmer.startsWith("J")) {
            return acc.concat(programmer);
          } else {
            return acc;
          }
        }, [])
        .map((programmer) => (
          <li>{programmer}</li>
        ))}
    </ul>
  );
}

export default App;

```

## 5. Astuces avec les objets : Raccourci de propriété, Déstructuration, Opérateur de propagation

Comme les tableaux, les objets sont une structure de données avec laquelle vous devez être à l'aise lorsque vous utilisez React.

Puisque les objets existent pour le stockage organisé de paires clé-valeur, contrairement aux tableaux, vous allez devoir être très à l'aise avec l'accès et la manipulation des propriétés d'objet.

Pour ajouter des propriétés à un objet au moment de sa création, vous nommez la propriété et sa valeur correspondante. Un raccourci très simple à retenir est que si le nom de la propriété est le même que la valeur, vous n'avez qu'à lister le nom de la propriété.

C'est le **raccourci de propriété d'objet** :

```js
const name = "Reed";

const user = {
  // au lieu de name: name, nous pouvons utiliser...
  name,
};

console.log(user.name); // Reed

```

La manière standard d'accéder aux propriétés d'un objet est d'utiliser la notation par point. Une approche encore plus pratique, cependant, est la **déstructuration d'objet**. Elle nous permet d'extraire des propriétés en tant que variables individuelles du même nom à partir d'un objet donné.

Cela ressemble un peu à l'écriture d'un objet à l'envers, ce qui rend le processus intuitif. C'est beaucoup plus agréable à utiliser que d'avoir à utiliser le nom de l'objet plusieurs fois pour accéder à chaque fois que vous voulez obtenir une valeur de celui-ci.

```js
const user = {
  name: "Reed",
  age: 28,
  isEnglishSpeaker: true,
};

// Accès aux propriétés par point
const name = user.name;
const age = user.age;

// Déstructuration d'objet
const { age, name, isEnglishSpeaker: knowsEnglish } = user;
// Utilisez ':' pour renommer une valeur lors de la déstructuration

console.log(knowsEnglish); // true

```

Maintenant, si vous voulez créer des objets à partir d'objets existants, vous pourriez lister les propriétés une par une, mais cela peut devenir très répétitif.

Au lieu de copier les propriétés manuellement, vous pouvez propager toutes les propriétés d'un objet dans un autre objet (au moment de sa création) en utilisant l'opérateur de propagation d'objet :

```js
const user = {
  name: "Reed",
  age: 28,
  isEnglishSpeaker: true,
};

const firstUser = {
  name: user.name,
  age: user.age,
  isEnglishSpeaker: user.isEnglishSpeaker,
};

// Copie toutes les propriétés de user dans secondUser
const secondUser = {
  ...user,
};

```

Ce qui est génial avec la propagation d'objet, c'est que vous pouvez propager autant d'objets que vous le souhaitez dans un nouvel objet, et vous pouvez les ordonner comme des propriétés. Mais soyez conscient que les propriétés qui viennent plus tard avec le même nom écraseront les propriétés précédentes :

```js
const user = {
  name: "Reed",
  age: 28,
};

const moreUserInfo = {
  age: 70,
  country: "USA",
};

// Copie toutes les propriétés de user dans secondUser
const secondUser = {
  ...user,
  ...moreUserInfo,
  computer: "MacBook Pro",
};

console.log(secondUser);
// { name: "Reed", age: 70, country: "USA", computer: "Macbook Pro" }

```

## 6 : Promesses + Syntaxe Async/Await

Presque toutes les applications React consistent en du **code asynchrone** – du code qui prend un temps indéfini pour être exécuté. Particulièrement si vous devez obtenir ou changer des données depuis une API externe en utilisant des fonctionnalités de navigateur comme l'**API Fetch** ou la bibliothèque tierce **axios**.

Les promesses sont utilisées pour résoudre le code asynchrone afin de le faire résoudre comme du code normal, synchrone, que nous pouvons lire de haut en bas.

Les promesses utilisent traditionnellement des rappels pour résoudre notre code asynchrone. Nous utilisons le rappel `.then()` pour résoudre les promesses qui se sont résolues avec succès, tandis que nous utilisons le rappel `.catch()` pour résoudre les promesses qui répondent avec une erreur.

Voici un exemple réel d'utilisation de React pour récupérer des données depuis mon API GitHub en utilisant l'API Fetch pour afficher mon image de profil. Les données sont résolues en utilisant des promesses :

```js
/* Allez sur react.new et collez ce code pour le voir fonctionner ! */
import React from "react";

const App = () => {
  const [avatar, setAvatar] = React.useState("");

  React.useEffect(() => {
    /*
      Le premier .then() nous permet d'obtenir les données JSON de la réponse.
      Le deuxième .then() obtient l'url de mon avatar et la place dans l'état.
    */
    fetch("https://api.github.com/users/reedbarger")
      .then((response) => response.json())
      .then((data) => setAvatar(data.avatar_url))
      .catch((error) => console.error("Error fetching data: ", error));
  }, []);

  return <img src={avatar} alt="Reed Barger" />;
};

export default App;

```

Au lieu de toujours devoir utiliser des rappels pour résoudre nos données depuis une promesse, nous pouvons utiliser une syntaxe nettoyée qui ressemble à du code synchrone, appelée la **syntaxe async/await**.

Les mots-clés async et await ne sont utilisés qu'avec des fonctions (fonctions JavaScript normales, pas des composants de fonction React).

Pour les utiliser, nous devons nous assurer que notre code asynchrone est dans une fonction précédée du mot-clé `async`. La valeur de toute promesse peut ensuite être résolue en plaçant le mot-clé `await` avant celle-ci.

```js
/* Allez sur react.new et collez ce code pour le voir fonctionner ! */
import React from "react";

const App = () => {
  const [avatar, setAvatar] = React.useState("");

  React.useEffect(() => {
    /*
	  Notez que parce que la fonction passée à useEffect ne peut pas être async, nous devons créer une fonction séparée pour que notre promesse soit résolue (fetchAvatar)
    */
    async function fetchAvatar() {
      const response = await fetch("https://api.github.com/users/reedbarger");
      const data = await response.json();
      setAvatar(data.avatar_url);
    }

    fetchAvatar();
  }, []);

  return <img src={avatar} alt="Reed Barger" />;
};

export default App;

```

Nous utilisons le rappel `.catch()` pour gérer les erreurs dans les promesses traditionnelles, mais comment attraper les erreurs avec async/await ?

Nous utilisons toujours `.catch()` et lorsque nous rencontrons une erreur, comme lorsque nous avons une réponse de notre API qui est dans la plage de statut 200 ou 300 :

```js
/* Allez sur react.new et collez ce code pour le voir fonctionner ! */
import React from "react";

const App = () => {
  const [avatar, setAvatar] = React.useState("");

  React.useEffect(() => {
    async function fetchAvatar() {
      /* Utilisation d'un utilisateur invalide pour créer une erreur 404 (non trouvé) */
      const response = await fetch("https://api.github.com/users/reedbarge");
      if (!response.ok) {
        const message = `An error has occured: ${response.status}`;
        /* En développement, vous verrez ce message d'erreur affiché sur votre écran */
        throw new Error(message);
      }
      const data = await response.json();

      setAvatar(data.avatar_url);
    }

    fetchAvatar();
  }, []);

  return <img src={avatar} alt="Reed Barger" />;
};

export default App;

```

## 7. Modules ES + Syntaxe Import / Export

ES6 nous a donné la capacité de partager facilement du code entre nos propres fichiers JavaScript ainsi qu'avec des bibliothèques tierces en utilisant des **modules ES**.

De plus, lorsque nous utilisons des outils comme Webpack, nous pouvons importer des actifs comme des images et des svgs, ainsi que des fichiers CSS et les utiliser comme valeurs dynamiques dans notre code.

```js
/* Nous importons dans notre fichier une bibliothèque (React), une image png et des styles CSS */
import React from "react";
import logo from "../img/site-logo.png";
import "../styles/app.css";

function App() {
  return (
    <div>
      Welcome!
      <img src={logo} alt="Site logo" />
    </div>
  );
}

export default App;

```

L'idée derrière les modules ES est de pouvoir diviser notre code JavaScript en différents fichiers, pour le rendre modulaire ou réutilisable dans notre application.

En ce qui concerne le code JavaScript, nous pouvons importer et exporter des variables et des fonctions. Il existe deux façons d'importer et d'exporter, en tant qu'**importations/exportations nommées** et en tant qu'**importations/exportations par défaut**.

Il ne peut y avoir qu'une seule chose que nous faisons une importation ou une exportation par défaut par fichier et nous pouvons faire autant d'importations/exportations nommées que nous le souhaitons. Par exemple :

```js
// constants.js
export const name = "Reed";

export const age = 28;

export default function getName() {
  return name;
}

// app.js
// Remarquez que les exportations nommées sont importées entre accolades
import getName, { name, age } from "../constants.js";

console.log(name, age, getName());

```

Nous pouvons également écrire toutes les exportations à la fin du fichier au lieu de les placer à côté de chaque variable ou fonction :

```js
// constants.js
const name = "Reed";

const age = 28;

function getName() {
  return name;
}

export { name, age };
export default getName;

// app.js
import getName, { name, age } from "../constants.js";

console.log(name, age, getName());

```

Vous pouvez également aliaser ou renommer ce que vous importez en utilisant le mot-clé `as` pour les importations nommées. L'avantage des exportations par défaut est qu'elles peuvent être nommées comme vous le souhaitez.

```js
// constants.js
const name = "Reed";

const age = 28;

function getName() {
  return name;
}

export { name, age };
export default getName;

// app.js
import getMyName, { name as myName, age as myAge } from "../constants.js";

console.log(myName, myAge, getMyName());

```

## Devenez un développeur React professionnel

React est difficile. Vous ne devriez pas avoir à le comprendre par vous-même.

J'ai mis tout ce que je sais sur React dans un seul cours, pour vous aider à atteindre vos objectifs en un temps record :

[**Présentation : Le React Bootcamp**](https://www.thereactbootcamp.com)

**C'est le seul cours que j'aurais aimé avoir lorsque j'ai commencé à apprendre React.**

Cliquez ci-dessous pour essayer le React Bootcamp par vous-même :

[![Cliquez pour rejoindre le React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Cliquez pour commencer*