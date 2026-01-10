---
title: Le guide pratique React pour 2020 (+ exemples concrets)
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2020-01-21T13:00:00.000Z'
originalURL: https://freecodecamp.org/news/the-react-cheatsheet-for-2020
coverImage: https://www.freecodecamp.org/news/content/images/2020/01/react-cheatsheet-bg.png
tags:
- name: React
  slug: react
- name: react hooks
  slug: react-hooks
seo_title: Le guide pratique React pour 2020 (+ exemples concrets)
seo_desc: 'I''ve put together for you an entire visual cheatsheet of all of the concepts
  and skills you need to master React in 2020.

  But don''t let the label ''cheatsheet'' fool you. This is more than a mere summary
  of React''s features.

  My aim here was to clearly ...'
---

J'ai préparé pour vous un guide visuel complet de tous les concepts et compétences nécessaires pour maîtriser React en 2020.

Mais ne vous laissez pas tromper par le terme 'guide pratique'. Cela va bien au-delà d'un simple résumé des fonctionnalités de React.

Mon objectif ici était de présenter clairement et concisément les connaissances et les modèles que j'ai acquis en travaillant avec React en tant que développeur professionnel.

Chaque partie est conçue pour être extrêmement utile en vous montrant des exemples pratiques et concrets avec des commentaires significatifs pour vous guider tout au long.

### Vous voulez votre propre copie ? ?

Téléchargez le guide PDF **[ici](https://reedbarger.com/resources/react-cheatsheet-2020/)** (cela prend 5 secondes).

Voici quelques avantages à télécharger la version PDF :

*  Guide de référence rapide à consulter comme vous le souhaitez et quand vous le souhaitez
*  Des tonnes de snippets de code copiables pour une réutilisation facile
*  Lisez ce guide complet où que vous soyez. Dans le train, à votre bureau, en faisant la queue... n'importe où.

> Remarque : Ce guide pratique couvre peu les composants de classe. Les composants de classe restent utiles pour les projets React existants, mais depuis l'arrivée des Hooks en 2018, nous pouvons créer nos applications avec des composants fonctionnels uniquement. J'ai souhaité offrir une approche 'Hooks-first' de React aux débutants et aux développeurs expérimentés.

Il y a énormément de choses à couvrir, alors commençons.

## Table des matières

### Concepts de base

* Éléments et JSX
* Composants et Props
* Listes et Clés
* Événements et Gestionnaires d'événements

### Hooks React

* État et useState
* Effets de bord et useEffect
* Performance et useCallback
* Mémoisation et useMemo
* Refs et useRef

### Hooks avancés

* Contexte et useContext
* Réducteurs et useReducer
* Écrire des hooks personnalisés
* Règles des hooks

## Concepts de base

### Éléments et JSX

Voici la syntaxe de base pour un élément React :

```js
// En résumé, JSX nous permet d'écrire du HTML dans notre JS
// JSX peut utiliser n'importe quelle balise HTML valide (i.e. div/span, h1-h6, form/input, etc)
<div>Bonjour React</div> 
```

Les éléments JSX sont des expressions :

```js
// en tant qu'expression, JSX peut être assigné à des variables...
const greeting = <div>Bonjour React</div>;

const isNewToReact = true;

// ... ou peut être affiché conditionnellement
function sayGreeting() {
  if (isNewToReact) {
    // ... ou retourné par des fonctions, etc.
    return greeting; // affiche : Bonjour React
  } else {
    return <div>Bonjour à nouveau, React</div>;
  }
}

```

JSX nous permet d'imbriquer des expressions :

```js
const year = 2020;
// nous pouvons insérer des valeurs JS primitives dans des accolades : {}
const greeting = <div>Bonjour React en {year}</div>;
// essayer d'insérer des objets entraînera une erreur

```

JSX nous permet d'imbriquer des éléments :

```js
// pour écrire JSX sur plusieurs lignes, enveloppez-le dans des parenthèses : ()
const greeting = (
  // div est l'élément parent
  <div>
    {/* h1 et p sont des éléments enfants */}
    <h1>Bonjour !</h1>
    <p>Bienvenue dans React</p>
  </div>
);
// 'parents' et 'enfants' sont les termes utilisés pour décrire les éléments JSX en relation
// les uns avec les autres, comme nous parlerions des éléments HTML

```

HTML et JSX ont une syntaxe légèrement différente :

```js
// Div vide n'est pas <div></div> (HTML), mais <div/> (JSX)
<div/>

// Un élément à balise unique comme input n'est pas <input> (HTML), mais <input/> (JSX)
<input name="email" />

// Les attributs sont écrits en camelCase pour JSX (comme les variables JS
<button className="submit-button">Soumettre</button> // pas 'class' (HTML)

```

L'application React la plus basique nécessite trois choses :

* ReactDOM.render() pour rendre notre application
* Un élément JSX (appelé nœud racine dans ce contexte)
* Un élément DOM dans lequel monter l'application (généralement une div avec un id de root dans un fichier index.html)

```js
// imports nécessaires si vous utilisez le package NPM ; pas si vous utilisez des liens CDN
import React from "react";
import ReactDOM from "react-dom";

const greeting = <h1>Bonjour React</h1>;

// ReactDOM.render(nœud racine, point de montage)
ReactDOM.render(greeting, document.getElementById("root"));

```

### Composants et Props

Voici la syntaxe pour un composant React de base :

```js
import React from "react";

// 1er type de composant : composant fonctionnel
function Header() {
  // les composants fonctionnels doivent être en majuscule contrairement aux fonctions JS normales
  // notez le nom en majuscule ici : 'Header'
  return <h1>Bonjour React</h1>;
}

// les composants fonctionnels avec des fonctions fléchées sont également valides
const Header = () => <h1>Bonjour React</h1>;

// 2ème type de composant : composant de classe
// (les classes sont un autre type de fonction)
class Header extends React.Component {
  // les composants de classe ont plus de code standard (avec extends et la méthode render)
  render() {
    return <h1>Bonjour React</h1>;
  }
}

```

Voici comment les composants sont utilisés :

```js
// appelons-nous ces composants fonctionnels comme des fonctions normales ?

// Non, pour les exécuter et afficher le JSX qu'ils retournent...
const Header = () => <h1>Bonjour React</h1>;

// ... nous les utilisons comme des éléments JSX 'personnalisés'
ReactDOM.render(<Header />, document.getElementById("root"));
// rend : <h1>Bonjour React</h1>

```

Les composants peuvent être réutilisés dans notre application :

```js
// par exemple, ce composant Header peut être réutilisé dans n'importe quelle page de l'application

// ce composant est affiché pour la route '/'
function IndexPage() {
  return (
    <div>
      <Header />
      <Hero />
      <Footer />
    </div>
  );
}

// affiché pour la route '/about'
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

Les données peuvent être passées dynamiquement aux composants avec des props :

```js
// Que faire si nous voulons passer des données à notre composant depuis un parent ?
// Par exemple, pour passer le nom d'un utilisateur à afficher dans notre Header ?

const username = "John";

// nous ajoutons des 'attributs' personnalisés appelés props
ReactDOM.render(
  <Header username={username} />,
  document.getElementById("root")
);
// nous avons appelé cette prop 'username', mais nous pouvons utiliser n'importe quel identifiant JS valide

// props est l'objet que chaque composant reçoit en tant qu'argument
function Header(props) {
  // les props que nous créons sur le composant (par exemple, username)
  // deviennent des propriétés de l'objet props
  return <h1>Bonjour {props.username}</h1>;
}

```

Les props ne doivent jamais être modifiées directement (mutées) :

```js
// Les composants doivent idéalement être des fonctions 'pures'.
// C'est-à-dire que pour chaque entrée, nous devons pouvoir nous attendre à la même sortie

// nous ne pouvons pas faire ce qui suit avec les props :
function Header(props) {
  // nous ne pouvons pas muter l'objet props, nous ne pouvons que le lire
  props.username = "Doug";

  return <h1>Bonjour {props.username}</h1>;
}
// Mais que faire si nous voulons modifier une valeur de prop qui arrive ?
// C'est là que nous utiliserions l'état (voir la section useState)

```

Les props enfants sont utiles si nous voulons passer des éléments / composants en tant que props à d'autres composants.

```js
// Pouvez-nous accepter des éléments React (ou des composants) en tant que props ?
// Oui, via une propriété spéciale de l'objet props appelée 'children'

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

Affichage conditionnel des composants avec des ternaires et des courts-circuits :

```js
// les instructions if sont bien pour afficher conditionnellement, cependant...
// ... seules les ternaires (vues ci-dessous) nous permettent d'insérer ces conditionnelles
// dans JSX, cependant
function Header() {
  const isAuthenticated = checkAuth();

  return (
    <nav>
      <Logo />
      {/* si isAuth est vrai, affiche AuthLinks. Si faux, Login  */}
      {isAuthenticated ? <AuthLinks /> : <Login />}
      {/* si isAuth est vrai, affiche Greeting. Si faux, rien. */}
      {isAuthenticated && <Greeting />}
    </nav>
  );
}

```

Les Fragments sont des composants spéciaux pour afficher plusieurs composants sans ajouter un élément supplémentaire au DOM.

Les Fragments sont idéaux pour la logique conditionnelle :

```js
// nous pouvons améliorer la logique dans l'exemple précédent
// si isAuthenticated est vrai, comment afficher à la fois AuthLinks et Greeting ?
function Header() {
  const isAuthenticated = checkAuth();

  return (
    <nav>
      <Logo />
      {/* nous pouvons rendre les deux composants avec un fragment */}
      {/* les fragments sont très concis : <> </> */}
      {isAuthenticated ? (
        <>
          <AuthLinks />
          <Greeting />
        </>
      ) : (
        <Login />
      )}
    </nav>
  );
}

```

### Listes et Clés

Utilisez .map() pour convertir des listes de données (tableaux) en listes d'éléments :

```js
const people = ["John", "Bob", "Fred"];
const peopleList = people.map(person => <p>{person}</p>);

```

.map() est également utilisé pour les composants ainsi que pour les éléments :

```js
function App() {
  const people = ['John', 'Bob', 'Fred'];
  // peut interpoler la liste retournée d'éléments dans {}
  return (
    <ul>
      {/* nous passons chaque élément de tableau comme props */}
      {people.map(person => <Person name={person} />}
    </ul>
  );
}

function Person({ name }) {
  // obtient la prop 'name' en utilisant la destructuration d'objet
  return <p>le nom de cette personne est : {name}</p>;
}

```

Chaque élément React itéré a besoin d'une prop spéciale 'key'. Les clés sont essentielles pour que React puisse suivre chaque élément qui est itéré avec map

Sans clés, il est plus difficile pour React de déterminer comment les éléments doivent être mis à jour lorsque les données changent.

Les clés doivent être des valeurs uniques pour représenter le fait que ces éléments sont séparés les uns des autres.

```js
function App() {
  const people = ['John', 'Bob', 'Fred'];

  return (
    <ul>
      {/* les clés doivent être des valeurs primitives, idéalement un id généré */}
      {people.map(person => <Person key={person} name={person} />)}
    </ul>
  );
}

// Si vous n'avez pas d'ids avec votre ensemble de données ou de valeurs primitives uniques,
// vous pouvez utiliser le deuxième paramètre de .map() pour obtenir l'index de chaque élément
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

### Événements et Gestionnaires d'événements

Les événements dans React et HTML sont légèrement différents.

```js
// Note : la plupart des fonctions de gestion d'événements commencent par 'handle'
function handleToggleTheme() {
  // code pour basculer le thème de l'application
}

// en html, onclick est en minuscules
<button onclick="handleToggleTheme()">
  Soumettre
</button>

// en JSX, onClick est en camelCase, comme les attributs / props
// nous passons également une référence à la fonction avec des accolades
<button onClick={handleToggleTheme}>
  Soumettre
</button>

```

Les événements React les plus essentiels à connaître sont onClick et onChange.

* onClick gère les événements de clic sur les éléments JSX (notamment les boutons)
* onChange gère les événements de clavier (notamment les entrées)

```js
function App() {
  function handleChange(event) {
    // lorsque nous passons la fonction à un gestionnaire d'événements, comme onChange
    // nous obtenons accès aux données sur l'événement (un objet)
    const inputText = event.target.value;
    const inputName = event.target.name; // myInput
    // nous obtenons le texte tapé et d'autres données à partir de event.target
  }

  function handleSubmit() {
    // on click n'a généralement pas besoin des données de l'événement
  }

  return (
    <div>
      <input type="text" name="myInput" onChange={handleChange} />
      <button onClick={handleSubmit}>Soumettre</button>
    </div>
  );
}

```

## React Hooks

### État et useState

useState nous donne un état local dans un composant fonctionnel :

```js
import React from 'react';

// créer une variable d'état
// syntaxe : const [stateVariable] = React.useState(defaultValue);
function App() {
  const [language] = React.useState('javascript');
  // nous utilisons la destructuration de tableau pour déclarer la variable d'état

  return <div>J'apprends {language}</div>;
}

```

Note : Tout hook dans cette section provient du package React et peut être importé individuellement.

```js
import React, { useState } from "react";

function App() {
  const [language] = useState("javascript");

  return <div>J'apprends {language}</div>;
}

```

useState nous donne également une fonction 'setter' pour mettre à jour l'état qu'il crée :

```js
function App() {
  // la fonction setter est toujours la deuxième valeur destructurée
  const [language, setLanguage] = React.useState("python");
  // la convention pour le nom du setter est 'setStateVariable'

  return (
    <div>
      {/*  pourquoi utiliser une fonction fléchée ici au lieu de onClick={setterFn()} ? */}
      <button onClick={() => setLanguage("javascript")}>
        Changer la langue en JS
      </button>
      {/*  sinon, setLanguage serait appelé immédiatement et non au clic */}
      <p>J'apprends maintenant {language}</p>
    </div>
  );
}

// notez que chaque fois que la fonction setter est appelée, l'état est mis à jour,
// et le composant App est ré-exécuté pour afficher le nouvel état

```

useState peut être utilisé une ou plusieurs fois dans un seul composant :

```js
function App() {
  const [language, setLanguage] = React.useState("python");
  const [yearsExperience, setYearsExperience] = React.useState(0);

  return (
    <div>
      <button onClick={() => setLanguage("javascript")}>
        Changer la langue en JS
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

useState peut accepter des valeurs primitives ou des objets pour gérer l'état :

```js
// nous avons la possibilité d'organiser l'état en utilisant le type de données
// le plus approprié, selon les données que nous suivons
function App() {
  const [developer, setDeveloper] = React.useState({
    language: "",
    yearsExperience: 0
  });

  function handleChangeYearsExperience(event) {
    const years = event.target.value;
    // nous devons passer l'objet d'état précédent que nous avions avec l'opérateur de propagation
    setDeveloper({ ...developer, yearsExperience: years });
  }

  return (
    <div>
      {/* pas besoin d'obtenir l'état précédent ici ; nous remplaçons l'objet entier */}
      <button
        onClick={() =>
          setDeveloper({
            language: "javascript",
            yearsExperience: 0
          })
        }
      >
        Changer la langue en JS
      </button>
      {/* nous pouvons également passer une référence à la fonction */}
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

Si le nouvel état dépend de l'état précédent, pour garantir que la mise à jour est effectuée de manière fiable, nous pouvons utiliser une fonction dans la fonction setter qui nous donne le bon état précédent.

```js
function App() {
  const [developer, setDeveloper] = React.useState({
    language: "",
    yearsExperience: 0,
    isEmployed: false
  });

  function handleToggleEmployment(event) {
    // nous obtenons la valeur de la variable d'état précédente dans les paramètres
    // nous pouvons nommer 'prevState' comme nous le souhaitons
    setDeveloper(prevState => {
      return { ...prevState, isEmployed: !prevState.isEmployed };
      // il est essentiel de retourner le nouvel état à partir de cette fonction
    });
  }

  return (
    <button onClick={handleToggleEmployment}>Basculer le statut d'emploi</button>
  );
}

```

### Effets de bord et useEffect

useEffect nous permet d'effectuer des effets de bord dans les composants fonctionnels. Alors, qu'est-ce que les effets de bord ?

* Les effets de bord sont là où nous devons atteindre le monde extérieur. Par exemple, récupérer des données à partir d'une API ou travailler avec le DOM.
* Les effets de bord sont des actions qui peuvent changer l'état de notre composant de manière imprévisible (qui ont causé des 'effets de bord').

useEffect accepte une fonction de rappel (appelée la fonction 'effet'), qui, par défaut, s'exécutera chaque fois qu'il y a un ré-affichage. Il s'exécute une fois que notre composant est monté, ce qui est le bon moment pour effectuer un effet de bord dans le cycle de vie du composant.

```js
// que fait notre code ? Choisit une couleur dans le tableau des couleurs
// et en fait la couleur de fond
function App() {
  const [colorIndex, setColorIndex] = React.useState(0);
  const colors = ["blue", "green", "red", "orange"];

  // nous effectuons un 'effet de bord' puisque nous travaillons avec une API
  // nous travaillons avec le DOM, une API de navigateur en dehors de React
  useEffect(() => {
    document.body.style.backgroundColor = colors[colorIndex];
  });
  // chaque fois que l'état est mis à jour, App est ré-exécuté et useEffect s'exécute

  function handleChangeIndex() {
    const next = colorIndex + 1 === colors.length ? 0 : colorIndex + 1;
    setColorIndex(next);
  }

  return <button onClick={handleChangeIndex}>Changer la couleur de fond</button>;
}

```

Pour éviter d'exécuter la fonction de rappel de l'effet après chaque rendu, nous fournissons un deuxième argument, un tableau vide :

```js
function App() {
  ...
  // maintenant notre bouton ne fonctionne plus, peu importe le nombre de fois où nous cliquons dessus...
  useEffect(() => {
    document.body.style.backgroundColor = colors[colorIndex];
  }, []);
  // la couleur de fond n'est définie qu'une seule fois, lors du montage

  // comment faire pour que la fonction d'effet ne s'exécute pas à chaque mise à jour d'état...
  // mais qu'elle fonctionne toujours lorsque le bouton est cliqué ?

  return (
    <button onClick={handleChangeIndex}>
      Changer la couleur de fond
    </button>
  );
}

```

useEffect nous permet d'effectuer des effets de manière conditionnelle avec le tableau des dépendances.

Le tableau des dépendances est le deuxième argument, et si l'une des valeurs du tableau change, la fonction d'effet s'exécute à nouveau.

```js
function App() {
  const [colorIndex, setColorIndex] = React.useState(0);
  const colors = ["blue", "green", "red", "orange"];

  // nous ajoutons colorIndex à notre tableau des dépendances
  // lorsque colorIndex change, useEffect exécutera la fonction d'effet à nouveau
  useEffect(() => {
    document.body.style.backgroundColor = colors[colorIndex];
    // lorsque nous utilisons useEffect, nous devons penser aux valeurs d'état
    // avec lesquelles nous voulons que notre effet de bord se synchronise
  }, [colorIndex]);

  function handleChangeIndex() {
    const next = colorIndex + 1 === colors.length ? 0 : colorIndex + 1;
    setColorIndex(next);
  }

  return <button onClick={handleChangeIndex}>Changer la couleur de fond</button>;
}

```

useEffect nous permet de nous désabonner de certains effets en retournant une fonction à la fin :

```js
function MouseTracker() {
  const [mousePosition, setMousePosition] = useState({ x: 0, y: 0 });

  React.useEffect(() => {
    // .addEventListener() configure un écouteur actif...
    window.addEventListener("mousemove", event => {
      const { pageX, pageY } = event;
      setMousePosition({ x: pageX, y: pageY });
    });

    // ... donc lorsque nous naviguons loin de cette page, il doit être
    // supprimé pour arrêter d'écouter. Sinon, il essaiera de définir
    // l'état dans un composant qui n'existe pas (provoquant une erreur)

    // Nous nous désabonnons de toute subscription / écouteur avec cette 'fonction de nettoyage'
    return () => {
      window.removeEventListener("mousemove", event => {
        const { pageX, pageY } = event;
        setMousePosition({ x: pageX, y: pageY });
      });
    };
  }, []);

  return (
    <div>
      <h1>La position actuelle de la souris est :</h1>
      <p>
        X: {mousePosition.x}, Y: {mousePosition.y}
      </p>
    </div>
  );
}

// Note : nous pourrions extraire la logique réutilisée dans les rappels à
// leur propre fonction, mais je pense que cela est plus lisible

```

* Récupération de données avec useEffect

Notez que la gestion des promesses avec la syntaxe plus concise async/await nécessite la création d'une fonction séparée. (Pourquoi ? La fonction de rappel de l'effet ne peut pas être asynchrone.)

```js
const endpoint = "https://api.github.com/users/codeartistryio";

// avec les promesses :
function App() {
  const [user, setUser] = React.useState(null);

  React.useEffect(() => {
    // les promesses fonctionnent dans le rappel
    fetch(endpoint)
      .then(response => response.json())
      .then(data => setUser(data));
  }, []);
}

// avec la syntaxe async / await pour la promesse :
function App() {
  const [user, setUser] = React.useState(null);
  // ne peut pas rendre la fonction de rappel de useEffect asynchrone
  React.useEffect(() => {
    getUser();
  }, []);

  // au lieu de cela, utilisez async / await dans une fonction séparée, puis appelez
  // la fonction dans useEffect
  async function getUser() {
    const response = await fetch("https://api.github.com/codeartistryio");
    const data = await response.json();
    setUser(data);
  }
}

```

### Performance et useCallback

useCallback est un hook qui est utilisé pour améliorer les performances de notre composant.

Si vous avez un composant qui est ré-exécuté fréquemment, useCallback empêche les fonctions de rappel à l'intérieur du composant d'être recréées à chaque fois que le composant est ré-exécuté (ce qui signifie que la fonction composant est ré-exécutée).

useCallback est ré-exécuté uniquement lorsque l'une de ses dépendances change.

```js
// dans Timer, nous calculons la date et la mettons dans l'état beaucoup de fois
// cela entraîne un ré-affichage pour chaque mise à jour d'état

// nous avions une fonction handleIncrementCount pour incrémenter l'état 'count'...
function Timer() {
  const [time, setTime] = React.useState();
  const [count, setCount] = React.useState(0);

  // ... mais à moins de l'envelopper dans useCallback, la fonction est
  // recréée pour chaque ré-affichage (mauvaise performance)
  // le hook useCallback retourne un rappel qui n'est pas recréé à chaque fois
  const inc = React.useCallback(
    function handleIncrementCount() {
      setCount(prevCount => prevCount + 1);
    },
    // useCallback accepte un deuxième argument de tableau de dépendances comme useEffect
    // useCallback ne s'exécutera que si une dépendance change (ici c'est 'setCount')
    [setCount]
  );

  React.useEffect(() => {
    const timeout = setTimeout(() => {
      const currentTime = JSON.stringify(new Date(Date.now()));
      setTime(currentTime);
    }, 300);

    return () => {
      clearTimeout(timeout);
    };
  }, [time]);

  return (
    <div>
      <p>L'heure actuelle est : {time}</p>
      <p>Compte : {count}</p>
      <button onClick={inc}>+</button>
    </div>
  );
}

```

### Mémoisation et useMemo

useMemo est très similaire à useCallback et est utilisé pour améliorer les performances. Mais au lieu d'être pour les rappels, il est pour stocker les résultats de calculs coûteux.

useMemo nous permet de 'mémoïser', ou de nous souvenir du résultat de calculs coûteux lorsqu'ils ont déjà été faits pour certaines entrées (nous l'avons déjà fait une fois pour ces valeurs, donc ce n'est rien de nouveau de le refaire).

useMemo retourne une valeur à partir du calcul, pas une fonction de rappel (mais peut être une fonction).

```js
// useMemo est utile lorsque nous avons besoin de beaucoup de ressources de calcul
// pour effectuer une opération, mais que nous ne voulons pas la répéter à chaque ré-affichage

function App() {
  // état pour sélectionner un mot dans le tableau 'words' ci-dessous
  const [wordIndex, setWordIndex] = useState(0);
  // état pour le compteur
  const [count, setCount] = useState(0);

  // mots que nous utiliserons pour calculer le nombre de lettres
  const words = ["i", "am", "learning", "react"];
  const word = words[wordIndex];

  function getLetterCount(word) {
    // nous imitions un calcul coûteux avec une boucle très longue (inutile)
    let i = 0;
    while (i < 1000000) i++;
    return word.length;
  }

  // Mémoïser la fonction coûteuse pour retourner la valeur précédente si l'entrée était la même
  // effectuer le calcul uniquement si un nouveau mot sans valeur mise en cache
  const letterCount = React.useMemo(() => getLetterCount(word), [word]);

  // si le calcul était fait sans useMemo, comme ceci :

  // const letterCount = getLetterCount(word);

  // il y aurait un délai dans la mise à jour du compteur
  // nous devrions attendre que la fonction coûteuse se termine

  function handleChangeIndex() {
    // passer d'un mot dans le tableau au suivant
    const next = wordIndex + 1 === words.length ? 0 : wordIndex + 1;
    setWordIndex(next);
  }

  return (
    <div>
      <p>
        {word} a {letterCount} lettres
      </p>
      <button onClick={handleChangeIndex}>Mot suivant</button>
      <p>Compteur : {count}</p>
      <button onClick={() => setCount(count + 1)}>+</button>
    </div>
  );
}

```

### Refs et useRef

Les Refs sont un attribut spécial disponible sur tous les composants React. Ils nous permettent de créer une référence à un élément / composant donné lorsque le composant est monté.

useRef nous permet d'utiliser facilement les refs React. Nous appelons useRef (en haut du composant) et attachons la valeur retournée à l'attribut ref de l'élément pour y faire référence.

Une fois que nous avons créé une référence, nous utilisons la propriété current pour modifier (muter) les propriétés de l'élément. Ou nous pouvons appeler n'importe quelle méthode disponible sur cet élément (comme .focus() pour focaliser une entrée).

```js
function App() {
  const [query, setQuery] = React.useState("react hooks");
  // nous pouvons passer une valeur par défaut à useRef
  // nous n'en avons pas besoin ici, donc nous passons null pour référer un objet vide
  const searchInput = useRef(null);

  function handleClearSearch() {
    // current référence l'entrée de texte une fois que App est monté
    searchInput.current.value = "";
    // useRef peut stocker pratiquement n'importe quelle valeur dans sa propriété .current
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

## Hooks avancés

### Contexte et useContext

Dans React, nous voulons éviter le problème suivant de création de plusieurs props pour passer des données sur deux niveaux ou plus depuis un composant parent :

```js
// Le Contexte nous aide à éviter de créer plusieurs props en double
// Ce modèle est également appelé props drilling :
function App() {
  // nous voulons passer les données utilisateur à Header
  const [user] = React.useState({ name: "Fred" });

  return (
   {/* première prop 'user' */}
    <Main user={user} />
  );
}

const Main = ({ user }) => (
  <>
    {/* deuxième prop 'user' */}
    <Header user={user} />
    <div>Contenu principal de l'application...</div>
  </>
);

const Header = ({ user }) => <header>Bienvenue, {user.name} !</header>;

```

Le Contexte est utile pour passer des props sur plusieurs niveaux de composants enfants depuis un composant parent.

```js
// Voici l'exemple précédent réécrit avec le Contexte
// D'abord nous créons le contexte, où nous pouvons passer des valeurs par défaut
const UserContext = React.createContext();
// nous appelons cela 'UserContext' car c'est le type de données que nous passons

function App() {
  // nous voulons passer les données utilisateur à Header
  const [user] = React.useState({ name: "Fred" });

  return (
    {/* nous enveloppons le composant parent avec la propriété provider */}
    {/* nous passons les données dans l'arbre du composant avec la prop value */}
    <UserContext.Provider value={user}>
      <Main />
    </UserContext.Provider>
  );
}

const Main = () => (
  <>
    <Header />
    <div>Contenu principal de l'application...</div>
  </>
);

// nous pouvons supprimer les deux props 'user', nous pouvons simplement utiliser consumer
// pour consommer les données où nous en avons besoin
const Header = () => (
  {/* nous utilisons ce modèle appelé render props pour accéder aux données */}
  <UserContext.Consumer>
    {user => <header>Bienvenue, {user.name} !</header>}
  </UserContext.Consumer>
);

```

Le hook useContext peut supprimer ce modèle de render props qui semble inhabituel, cependant, pour pouvoir consommer le contexte dans n'importe quel composant fonctionnel que nous aimons :

```js
const Header = () => {
  // nous passons l'objet de contexte entier pour le consommer
  const user = React.useContext(UserContext);
  // et nous pouvons supprimer les balises Consumer
  return <header>Bienvenue, {user.name} !</header>;
};

```

### Réducteurs et useReducer

Les réducteurs sont des fonctions simples et prévisibles (pures) qui prennent un objet d'état précédent et un objet d'action et retournent un nouvel objet d'état. Par exemple :

```js
// disons que ce réducteur gère l'état de l'utilisateur dans notre application :
function reducer(state, action) {
  // les réducteurs utilisent souvent une instruction switch pour mettre à jour l'état
  // d'une manière ou d'une autre en fonction de la propriété type de l'action
  switch (action.type) {
    // si action.type a la chaîne 'LOGIN' dessus
    case "LOGIN":
      // nous obtenons les données de l'objet payload sur action
      return { username: action.payload.username, isAuth: true };
    case "SIGNOUT":
      return { username: "", isAuth: false };
    default:
      // si aucun cas ne correspond, retourner l'état précédent
      return state;
  }
}

```

Les réducteurs sont un modèle puissant pour gérer l'état qui est utilisé dans la bibliothèque populaire de gestion d'état Redux (communément utilisée avec React).

Les réducteurs peuvent être utilisés dans React avec le hook useReducer afin de gérer l'état dans notre application, contrairement à useState (qui est pour l'état local du composant).

useReducer peut être associé à useContext pour gérer les données et les passer facilement entre les composants.

Ainsi, useReducer + useContext peut être un système complet de gestion d'état pour nos applications.

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

Les hooks ont été créés pour réutiliser facilement le comportement entre les composants.

Ils sont un modèle plus compréhensible que les précédents pour les composants de classe, tels que les composants d'ordre supérieur ou les render props.

Ce qui est génial, c'est que nous pouvons créer nos propres hooks selon les besoins de nos propres projets, en plus de ceux que nous avons couverts et que React fournit :

```js
// voici un hook personnalisé qui est utilisé pour récupérer des données à partir d'une API
function useAPI(endpoint) {
  const [value, setValue] = React.useState([]);

  React.useEffect(() => {
    getData();
  }, []);

  async function getData() {
    const response = await fetch(endpoint);
    const data = await response.json();
    setValue(data);
  };

  return value;
};

// ceci est un exemple fonctionnel ! essayez-le vous-même (par exemple, dans codesandbox.io)
function App() {
  const todos = useAPI("https://todos-dsequjaojf.now.sh/todos");

  return (
    <ul>
      {todos.map(todo => <li key={todo.id}>{todo.text}</li>}
    </ul>
  );
}

```

### Règles des hooks

Il y a deux règles principales pour utiliser les hooks React que nous ne pouvons pas violer pour qu'ils fonctionnent correctement :

1. Les hooks ne peuvent être appelés qu'au sommet des composants (ils ne peuvent pas être dans des conditionnelles, des boucles ou des fonctions imbriquées)
2. Les hooks ne peuvent être utilisés qu'à l'intérieur des composants fonctionnels (ils ne peuvent pas être dans des fonctions JavaScript normales ou des composants de classe)

```js
function checkAuth() {
  // Règle 2 Violée ! Les hooks ne peuvent pas être utilisés dans des fonctions normales, seulement dans des composants
  React.useEffect(() => {
    getUser();
  }, []);
}

function App() {
  // ceci est le seul hook valablement exécuté dans ce composant
  const [user, setUser] = React.useState(null);

  // Règle 1 violée ! Les hooks ne peuvent pas être utilisés dans des conditionnelles (ou des boucles)
  if (!user) {
    React.useEffect(() => {
      setUser({ isAuth: false });
      // si vous voulez exécuter un effet de manière conditionnelle, utilisez le
      // tableau des dépendances pour useEffect
    }, []);
  }

  checkAuth();

  // Règle 1 violée ! Les hooks ne peuvent pas être utilisés dans des fonctions imbriquées
  return <div onClick={() => React.useMemo(() => doStuff(), [])}>Notre application</div>;
}

```

## Qu'est-ce qui suit

Il y a beaucoup d'autres concepts React à apprendre, mais ce sont ceux que je crois que vous devez connaître avant tout autre pour vous mettre sur la voie de la maîtrise de React en 2020.

Vous voulez une référence rapide de tous ces concepts ?

Téléchargez un guide PDF complet de toutes ces informations [ici](https://reedbarger.com/resources/react-cheatsheet-2020/).

Continuez à coder et je vous retrouverai dans le prochain article !

## Devenez un développeur React professionnel

React est difficile. Vous ne devriez pas avoir à le comprendre par vous-même.

J'ai mis tout ce que je sais sur React dans un seul cours, pour vous aider à atteindre vos objectifs en un temps record :

[**Présentation : Le React Bootcamp**](https://www.thereactbootcamp.com)

**C'est le seul cours que j'aurais aimé avoir lorsque j'ai commencé à apprendre React.**

Cliquez ci-dessous pour essayer le React Bootcamp par vous-même :

[![Cliquez pour rejoindre le React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Cliquez pour commencer*