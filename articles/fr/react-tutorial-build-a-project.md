---
title: Le tutoriel complet sur React pour 2021 – Apprenez les principaux concepts
  de React en construisant un projet
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2021-04-09T18:18:00.000Z'
originalURL: https://freecodecamp.org/news/react-tutorial-build-a-project
coverImage: https://www.freecodecamp.org/news/content/images/2021/04/the-complete-react-tutorial-2021.png
tags:
- name: JavaScript
  slug: javascript
- name: JSX
  slug: jsx
- name: React
  slug: react
- name: react hooks
  slug: react-hooks
- name: 'State Management '
  slug: state-management
seo_title: Le tutoriel complet sur React pour 2021 – Apprenez les principaux concepts
  de React en construisant un projet
seo_desc: 'Welcome to the complete React tutorial for 2021. This guide should help
  you become effective with React as quickly as possible as you build a complete application
  along the way.

  Compared to many tutorials you might have gone through before, this one ...'
---

Bienvenue dans le tutoriel complet sur React pour 2021. Ce guide devrait vous aider à devenir efficace avec React aussi rapidement que possible tout en construisant une application complète en cours de route.

Comparé à de nombreux tutoriels que vous avez peut-être suivis auparavant, celui-ci est conçu pour être entièrement pratique du début à la fin. 

Vous apprendrez comment créer une application React complète en environ 100 lignes de code, qui utilise de nombreux concepts fondamentaux de React : hooks, gestion d'état, formulaires, éléments JSX, composants, props, stylisation et conditionnels. 

Et surtout, vous apprendrez tous ces concepts en codant vous-même, de manière pratique. Commençons !

## Comment démarrer notre projet React

Nous allons créer notre application React en allant sur le site [react.new](https://react.new). 

Ce que cela va faire, c'est créer un nouveau bac à sable de code pour nous. Nous pouvons utiliser le bac à sable de code pour créer et développer des applications React complètes sans avoir à installer quoi que ce soit sur notre ordinateur. 

Une fois que vous visitez react.new, vous verrez votre éditeur de code et, sur le côté droit, nous voyons une version live de notre application à laquelle nous pouvons apporter des modifications :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/tutorial-1.png)

> Astuce rapide : assurez-vous d'appuyer sur commande/ctrl S. Cela va forker notre bac à sable et créer une URL spéciale que nous pourrons revisiter à l'avenir. 

Actuellement, nous regardons notre composant d'application, qui est le seul composant affiché dans notre application. Si nous regardons notre explorateur de fichiers à gauche, nous verrons que l'application est importée et rendue ici dans ce fichier index.js. 

```js
// src/index.js
import { StrictMode } from "react";
import ReactDOM from "react-dom";

import App from "./App";

const rootElement = document.getElementById("root");
ReactDOM.render(
  <StrictMode>
    <App />
  </StrictMode>,
  rootElement
);
```

Que fait tout ce code ?

Il "rend" ou affiche simplement notre application en l'injectant dans un fichier index.html, qui est ce que nous voyons sur le côté droit de la page. 

Le code trouve également et place notre application dans le soi-disant élément racine (un div avec l'id "root"). Si vous voulez voir où se trouve cet élément, vous pouvez le trouver dans notre dossier public, spécifiquement dans le fichier index.html. 

## Comment utiliser JSX

Maintenant que nous avons une application React fonctionnelle, commençons à la construire et à changer ce que nous voyons.

Commençons dans notre div en supprimant cet élément h2, et dans notre h1, appelons simplement notre application "Liste de tâches" : 

![Image](https://www.freecodecamp.org/news/content/images/2021/04/tutorial-2.png)

Ce avec quoi nous travaillons ici s'appelle **JSX**. Cela ressemble beaucoup à HTML, mais c'est en fait du JavaScript. Nous l'utilisons pour construire la structure de notre application, tout comme nous utiliserions HTML. 

> Nous pouvons utiliser n'importe quel élément HTML standard dans JSX : divs, n'importe quel élément d'en-tête, paragraphe, spans, boutons, et ainsi de suite. 

Il est important de noter qu'il existe quelques différences mineures entre JSX et HTML. 

Les attributs que nous utilisons sur JSX sont légèrement différents de ceux des éléments HTML normaux. Ils sont écrits en style camelCase, qui est une manière standard d'écrire des variables ou des propriétés en JavaScript. 

Par exemple, pour appliquer une classe sur un élément JSX, nous utilisons un attribut appelé `className`. Pour le HTML normal, cela s'appellerait simplement `class`. 

```js
// src/App.js
import "./styles.css";

export default function App() {
  return (
    <div className="App">
      <h1>Liste de tâches</h1>
    </div>
  );
}
```

Si nous utilisons `class` au lieu de `className` pour JSX, nous allons obtenir un avertissement disant que class est une propriété DOM invalide :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/tutorial-3.png)

## Comment créer une liste d'éléments Todo

Puisque nous créons une application de tâches, créons notre liste de tâches sous notre en-tête h1. 

Nous pourrions commencer par faire une liste non ordonnée avec quelques éléments de liste comme éléments enfants. Chaque tâche serait listée dans un élément `li` :

```js
// src/App.js
import "./styles.css";

export default function App() {
  return (
    <div className="App">
      <h1>Liste de tâches</h1>
      
      <ul>
      	<li>Élément de tâche</li>
      </ul>
    </div>
  );
}
```

Nous pouvons faire quelque chose de mieux en tant que développeurs React, cependant. Au lieu de cela, créons un composant dédié qui est responsable de l'affichage de nos tâches. 

## Comment créer de nouveaux composants React

Les **composants** sont l'épine dorsale de toute application React. 

Nous utilisons des composants pour séparer différentes parties de notre interface utilisateur. Cela les rend réutilisables partout où nous en avons besoin dans notre application, cela organise mieux notre code et cela facilite la compréhension de nos projets.

> Les composants remplissent un concept important en programmation qui s'appelle "séparation des préoccupations". Cela signifie qu'il est préférable que chaque partie de notre composant ait son propre rôle et ses propres responsabilités clairement définis, séparés de tout autre composant.

Tout comme nous avons un composant App, nous pouvons créer un composant à afficher dans App. Puisqu'il s'agit d'une liste de tâches, appelons-le "TodoList" :

```js
// src/App.js
import "./styles.css";

export default function App() {
  return (
    <div className="App">
      <h1>Liste de tâches</h1>
      
      <TodoList /> {/* composant avec une seule balise */}
    </div>
  );
}
```

## Règles des composants React

Chaque composant doit commencer par une lettre majuscule. Et une fois qu'un composant est déclaré, il peut être écrit et utilisé très similaire à un élément HTML. 

Un composant peut consister en une seule balise ou deux balises. S'il n'a rien entre les deux balises, qui sont appelées **enfants**, il doit n'avoir qu'une seule balise comme le code ci-dessus l'affiche : `<TodoList />`. 

De plus, si un composant ou un élément consiste en une seule balise, il doit être auto-fermant. Cela signifie qu'il doit se terminer par une barre oblique (comme `<TodoList />` et non `<TodoList>`).

Nous essayons d'afficher notre composant TodoList, mais nous ne l'avons pas encore créé. Pour cela, nous pouvons créer une autre fonction composant comme App, avec le nom TodoList. 

À ce stade, nous allons obtenir cette erreur disant que rien n'a été retourné par render :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/tutorial-4.png)

Nous devons retourner quelque chose, spécifiquement du JSX. Chaque composant que nous créons doit retourner des éléments et des composants JSX (qui doivent également, en fin de compte, être composés de JSX). 

Dans notre cas, nous voulons retourner notre liste de tâches. Prenons notre liste non ordonnée avec tous nos éléments de liste que nous voulons montrer. Nous n'avons pas vraiment de données pour l'instant, alors créons-en.

En particulier, créons un ensemble de données de tâches, que nous pouvons inclure dans un tableau. Ajoutons cela au composant App :

```js
// src/App.js
import "./styles.css";

export default function App() {
  const todos = [
    { id: 1, text: "Faire la vaisselle", done: false },
    { id: 2, text: "Faire la lessive", done: false },
    { id: 3, text: "Prendre une douche", done: false }
  ];

  return (
    <div>
      <h1>Liste de tâches</h1>
      <TodoList />
    </div>
  );
}

function TodoList() {}
```

## Comment passer des données aux composants avec les props

Maintenant, la question est – comment passons-nous toutes ces données à notre liste de tâches et les affichons-nous ?

Avec les composants React, nous pouvons le faire avec des propriétés spéciales que nous ajoutons au composant appelées props. 

Les **props** sont des attributs personnalisés que nous pouvons ajouter aux composants React pour passer des données à nos composants. Ils sont l'équivalent React des arguments en JavaScript. 

Puisque nos données s'appellent todos, nommons notre prop de la même manière : "todos". Nous utilisons l'opérateur d'égalité pour définir la valeur d'une prop ainsi qu'un ensemble d'accolades. Cela est dû au fait que notre tableau de todos est une variable (une valeur dynamique) :

```js
// src/App.js
import "./styles.css";

export default function App() {
  const todos = [
    { id: 1, text: "Faire la vaisselle", done: false },
    { id: 2, text: "Faire la lessive", done: false },
    { id: 3, text: "Prendre une douche", done: false }
  ];

  return (
    <div>
      <h1>Liste de tâches</h1>
      <TodoList todos={todos} />
    </div>
  );
}

function TodoList() {}
```

> Si nous voulions en faire une chaîne de caractères, par exemple, nous l'entourerions d'un ensemble de guillemets. Mais puisque cela est une valeur dynamique qui peut changer, nous voulons toujours l'inclure dans des accolades.

Dans le composant TodoList, où nos props vont-elles être reçues pour afficher finalement nos données de todos ? Elles vont être reçues exactement là où toute fonction recevrait ses arguments. 

Nous recevons nos données de props sur un objet que nous appelons généralement "props", mais nous pouvons lui donner le nom que nous voulons. 

Nous pouvons voir que nous passons ces données en utilisant `console.log(props)`. Si nous regardons notre onglet console, nous avons cette propriété sur notre objet props appelée "todos". 

Il a un tableau de trois éléments comme nous nous y attendions :

```js
// src/App.js
import "./styles.css";

export default function App() {
  const todos = [
    { id: 1, text: "Faire la vaisselle", done: false },
    { id: 2, text: "Faire la lessive", done: false },
    { id: 3, text: "Prendre une douche", done: false }
  ];

  return (
    <div>
      <h1>Liste de tâches</h1>
      <TodoList todos={todos} />
    </div>
  );
}

function TodoList(props) {
  console.log(props) // {todos: Array(3)}
}
```

## Comment mapper les éléments d'un tableau avec la fonction Map

Pour afficher chacun de ces éléments de liste, nous pouvons prendre le tableau qui est sur `props.todos`. 

En particulier, nous pouvons utiliser une fonction spéciale que React nous donne sur le tableau de todos appelée **map**. 

Puisque nous voulons afficher cela dans TodoList, nous devons à nouveau utiliser un ensemble d'accolades pour l'afficher dans notre JSX. En utilisant `props.todo.map`, nous allons mapper ce tableau comme nous le ferions pour un tableau JavaScript normal. 

> La fonction map de React est légèrement différente de la fonction map JavaScript normale car elle est conçue pour retourner et rendre des éléments JSX. 

`.map()` accepte une fonction interne et dans cette fonction, nous pouvons obtenir l'accès à chaque todo. En utilisant une fonction fléchée, nous pouvons retourner chaque todo dans son propre JSX. 

Enfin, nous pouvons immédiatement retourner ce JSX en l'entourant d'un ensemble de parenthèses :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/tutorial-5.gif)

Dans notre fonction interne, nous obtenons l'accès aux données de chaque todo. Pour afficher ces données, nous pouvons prendre chaque todo que nous savons être un objet. Nous pouvons utiliser un ensemble d'accolades pour sortir la valeur dynamique de ce qui se trouve sur `todo.text`. 

Lorsque nous faisons cela, nous pouvons voir nos trois todos :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/tutorial-6.png)

## Que sont les clés React (et pourquoi sont-elles importantes) ?

Si nous regardons l'onglet console en bas, nous verrons un avertissement disant que chaque enfant dans la liste devrait avoir une "propriété clé unique". 

La raison en est que React doit garder une trace de l'ordre de chacun des éléments de notre liste. Il le fait avec l'aide d'une propriété React spéciale appelée **clé**. 

> Pour une clé, vous voulez généralement utiliser un identifiant unique, une valeur unique qui n'est associée qu'à une seule donnée. Dans notre cas, pour identifier les données de chaque todo, nous utiliserons le numéro unique fourni sur `todo.id`.

Alors pourquoi les clés sont-elles importantes ? Il est important pour React de déterminer comment il doit mettre à jour notre interface utilisateur de manière appropriée. Si nous devions mettre à jour le texte d'un todo ou sa valeur done, la clé est ce qui indique à React quel élément de todo doit être mis à jour. 

Une fois que nous avons ajouté la prop clé à l'élément ou au composant sur lequel nous itérons, nous n'obtenons plus cet avertissement : 

![Image](https://www.freecodecamp.org/news/content/images/2021/04/tutorial-7.png)

## Comment obtenir des props individuelles avec la déstructuration

Notez qu'un raccourci supplémentaire est que, au lieu de référencer l'objet entier dans TodoList, nous pouvons référencer les propriétés individuelles de cet objet pour rendre notre code un peu plus court en utilisant la déstructuration d'objet. 

> La déstructuration d'objet n'est pas un concept React, mais une fonctionnalité JavaScript standard qui facilite l'accès aux propriétés d'objet en les déclarant immédiatement comme variables individuelles.

Pour l'instant, nous n'avons qu'une seule prop transmise à TodoList, alors déstructurons cette prop, `todos`, individuellement.

Pour ce faire, nous ajoutons un ensemble d'accolades dans les paramètres de notre fonction, et nous prenons simplement la propriété dont nous avons besoin de l'objet props. Cela signifie que nous pouvons changer `props.todos` en simplement `todos` :

```js
// src/App.js
import "./styles.css";

export default function App() {
  const todos = [
    { id: 1, text: "Faire la vaisselle", done: false },
    { id: 2, text: "Faire la lessive", done: false },
    { id: 3, text: "Prendre une douche", done: false }
  ];

  return (
    <div>
      <h1>Liste de tâches</h1>
      <TodoList todos={todos} />
    </div>
  );
}

// utilisation de la déstructuration d'objet sur l'objet props
function TodoList({ todos }) {
  return (
    <ul>
      {todos.map((todo) => (
        <li key={todo.id}>{todo.text}</li>
      ))}
    </ul>
  );
}
```

## Comment ajouter de nouveaux éléments à la liste de tâches

Maintenant, que faire pour ajouter de nouvelles tâches à notre liste ? 

Sous notre composant TodoList, ajoutons un nouveau composant qui est responsable de l'ajout de nouvelles tâches. Un nom logique pour cela serait "AddTodo". 

Nous pouvons créer cela sous notre composant de liste de tâches. Faisons en sorte que AddTodo retourne un élément de formulaire qui contient une entrée de texte de base et un bouton de soumission.

```js
// src/App.js
import "./styles.css";

export default function App() {
  const todos = [
    { id: 1, text: "Faire la vaisselle", done: false },
    { id: 2, text: "Faire la lessive", done: false },
    { id: 3, text: "Prendre une douche", done: false }
  ];

  return (
    <div>
      <h1>Liste de tâches</h1>
      <TodoList todos={todos} />
      <AddTodo />
    </div>
  );
}

function TodoList({ todos }) {
  return (
    <ul>
      {todos.map((todo) => (
        <li key={todo.id}>{todo.text}</li>
      ))}
    </ul>
  );
}

function AddTodo() {
  return (
    <form>
      <input placeholder="Ajouter une tâche" />
      <button type="submit">Soumettre</button>
    </form>
  );
}
```

> Notez que tout élément JSX qui consiste en une seule balise (comme notre entrée) doit se terminer par une barre oblique. Si nous ne l'incluons pas, nous allons obtenir une erreur de compilation disant "contenu JSX non terminé". 

Maintenant, la question est : comment tapons-nous dans notre entrée, soumettons notre formulaire et avons une nouvelle tâche ajoutée à notre tableau de tâches ?

## Comment gérer les soumissions de formulaire dans React

Pour prendre en charge la soumission de notre formulaire, nous devons commencer à travailler avec les événements dans React. 

Dans notre cas, nous voulons utiliser l'événement "submit" lorsque notre formulaire est soumis par notre utilisateur et que React gère cette soumission de formulaire en ajoutant une nouvelle tâche. 

React ajoute une prop spéciale à l'élément de formulaire appelée `onSubmit`. onSubmit accepte une fonction dans un ensemble d'accolades. Créons une nouvelle fonction, que nous appellerons `handleAddTodo`. 

> Notez que la plupart des fonctions qui gèrent les événements dans React sont préfixées par le mot "handle". Il vous appartient finalement de nommer vos fonctions comme vous le souhaitez, mais c'est une convention utile.

Il est important de noter que cette fonction doit être créée dans le composant lui-même (AddTodo), et non à l'extérieur. Lorsque `handleAddTodo` est passé à la prop `onSubmit`, il sera appelé lorsque notre formulaire est soumis :

```js
// src/App.js
import "./styles.css";

// ...

function AddTodo() {
  function handleAddTodo() {}

  return (
    <form onSubmit={handleAddTodo}>
      <input placeholder="Ajouter une tâche" />
      <button type="submit">Soumettre</button>
    </form>
  );
}
```

## Comment empêcher le comportement par défaut du formulaire

Lorsque nous cliquons sur le bouton de soumission ou appuyons sur la touche de retour, les données de l'événement de soumission sont passées automatiquement à notre fonction connectée à onSubmit. Nous recevons ces données d'événement dans les paramètres de `handleAddTodo`.

La première chose que nous voulons faire avec cet événement est d'appeler une méthode sur celui-ci appelée `.preventDefault()`. Cette méthode empêche l'action par défaut chaque fois que nous soumettons un formulaire :

```js
// src/App.js
import "./styles.css";

// ...

function AddTodo() {
  function handleAddTodo(event) {
    event.preventDefault();
  }

  return (
    <form onSubmit={handleAddTodo}>
      <input placeholder="Ajouter une tâche" />
      <button type="submit">Soumettre</button>
    </form>
  );
}
```

Chaque fois que nous soumettons un formulaire, par défaut, la page est actualisée. Nous ne voulons pas ce comportement avec React – nous voulons que JavaScript contrôle ce qui se passe ensuite. 

Après avoir empêché une actualisation, nous voulons obtenir l'accès à ce qui a été tapé dans l'entrée pour créer une nouvelle tâche avec celle-ci. Comment faisons-nous cela ? 

## Comment accéder aux données du formulaire lors de la soumission

La manière dont nous obtenons l'accès à tous les éléments de notre formulaire est avec l'aide de la propriété `event.target.elements`. 

Tout d'abord, cela nous donnera la cible de l'événement, qui est le formulaire lui-même. `elements` est une propriété qui nous donnera tous les éléments de ce formulaire, y compris notre entrée et notre bouton de soumission. 

Si nous devions console.log `event.target.elements` maintenant, soumettre notre formulaire et regarder notre console, nous voyons simplement un objet avec quelques propriétés, une appelée "0", et une appelée "1". 

Ce n'est pas très utile pour nous, bien que nous voyions qu'il s'agit de notre entrée et de notre bouton :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/tutorial-8.png)

Au lieu de cela, nous voulons obtenir ce qui a été tapé dans notre entrée. 

Pour ce faire, nous pouvons ajouter soit un attribut "id" soit un attribut "name" à notre entrée. Ajoutons l'attribut name avec une valeur de "addTodo". Lorsque nous cliquons à nouveau sur soumettre, cela nous donnera une nouvelle propriété sur l'objet elements également appelée `addTodo`. À partir de cette référence, nous pouvons très facilement obtenir ce qui a été tapé dedans. 

Cela nous permet d'utiliser `event.target.elements.addTodo.value` pour obtenir ce qui a été tapé dans le texte. Lorsque nous le faisons, lorsque nous tapons du texte dans notre entrée et cliquons sur soumettre, nous le voyons enregistré dans la console :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/tutorial-9.gif)

Maintenant que nous avons notre texte, nous allons le mettre dans une variable appelée "text". En utilisant cela, nous voulons créer une nouvelle tâche. 

Nous savons que chaque tâche est un objet et qu'elle doit consister en les propriétés id, text et done. Créons une variable `todo` et celle-ci sera égale à un nouvel objet où l'id sera 4, le texte sera égal au texte que nous obtenons de l'objet elements, et nous pouvons définir done à false. 

Par défaut, les nouvelles tâches qui sont ajoutées ne seront pas terminées :

```js
// src/App.js
import "./styles.css";

//...

function AddTodo() {
  function handleAddTodo(event) {
    event.preventDefault();
    const text = event.target.elements.addTodo.value;
    const todo = {
      id: 4,
      text,
      done: false
    };
  }

  return (
    <form onSubmit={handleAddTodo}>
      <input name="addTodo" placeholder="Ajouter une tâche" />
      <button type="submit">Soumettre</button>
    </form>
  );
}
```

Et enfin, la grande question est, comment ajoutons-nous cette tâche à notre tableau, `todos` ? 

## Introduction à l'état dans React 

C'est là que le concept d'état intervient. 

Pour l'instant, nous traitons avec des données statiques – il n'y a aucun moyen réel de mettre à jour ce tableau de tâches. Pour être clair, il y a bien un moyen de le faire en utilisant JavaScript, mais ce que nous ne sommes pas actuellement en mesure de faire, c'est dire à React, même si nous devions le mettre à jour, qu'il doit **re-rendre** cette liste. 

En d'autres termes, pour effectuer une mise à jour de nos données et ensuite nous montrer les données mises à jour dans notre vue. Donc, bien que nous puissions mettre à jour les données, nous avons également besoin que React montre à nos utilisateurs les données mises à jour. 

L'**état** est nécessaire pour résoudre notre problème. 

> L'état est un moyen de gérer les données de notre application et permet également à React de mettre à jour notre UI (interface utilisateur) en réponse aux changements de données. 

## Comment gérer l'état dans React avec le hook useState

Nous pouvons gérer l'état dans React en utilisant le hook `useState`. Pour utiliser le hook useState, la première chose que nous devons faire est d'importer React en haut, car useState provient de la bibliothèque principale React. 

Après cela, nous pouvons simplement appeler le hook useState en haut de notre composant d'application. Une fois que nous appelons useState comme une fonction normale, nous passerons tout notre tableau de tâches comme nos données initiales. Notre application va se casser pendant un moment puisque nous ne montrons plus nos tâches pour l'instant. 

useState retourne un tableau avec deux éléments :

1. La valeur initiale avec laquelle nous avons appelé useState (notre tableau de tâches) et cela devient notre variable d'état
2. Une fonction spéciale qui nous permet de mettre à jour ce qui est stocké dans la variable d'état 

Nous pouvons déstructurer les valeurs qui sont retournées par useState en ajoutant un ensemble de crochets de tableau pour obtenir immédiatement les valeurs qui sont retournées par celui-ci. D'abord l'état et ensuite, la fonction pour mettre à jour l'état :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/tutorial-10.gif)

Nous appellerons notre variable d'état `todos` et le setter pour gérer notre état `setTodos`. 

Tout ce que nous avons à faire pour mettre à jour notre état est de lui passer ce que nous voulons que le nouvel état soit. Cette fonction `setTodos` va être passée à notre composant AddTodo, alors ajoutons cela comme une prop du même nom. Nous allons également déstructurer `setTodos` de notre objet props dans AddTodo. 

Et enfin, nous pouvons appeler `setTodos` en bas de `handleAddTodo`. Ce qui est génial avec cette fonction, c'est qu'au lieu de devoir passer le tableau de tâches également, cette fonction peut nous donner l'état précédent avec l'aide d'une fonction que nous pouvons recevoir à l'intérieur de celle-ci :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/tutorial-11.gif)

Cela peut sembler étrange au début, mais dans `setTodos`, nous obtenons l'accès aux données de tâches précédentes. Si nous écrivons une fonction fléchée ou toute fonction d'ailleurs, nous pouvons simplement fournir ce que nous voulons que le nouvel état soit. 

> L'avantage de pouvoir accéder directement à la valeur de la variable d'état précédente dans la fonction de setter est que cela nous évite de devoir passer toute la variable d'état des tâches comme une prop supplémentaire à chaque composant dans lequel nous voulons mettre à jour sa valeur.

Si nous voulions vider notre état de tâches, nous pourrions simplement retourner un tableau vide ici. Si nous devions soumettre notre formulaire, nous verrions que toutes nos tâches ont été supprimées. 

Une fois que nous soumettons notre formulaire, l'état est mis à jour, et notre application est re-rendue en conséquence. 

## Re-rendus dans React

Notez que tout re-rendu dans un composant parent entraînera le re-rendu de tous les composants enfants. Cela signifie que chaque fois que nos données de tâches sont mises à jour, le composant TodoList (un enfant du composant App) est mis à jour avec ces nouvelles données. 

Si nous retournons à `handleAddTodo`, nous pouvons prendre nos tâches précédentes et utiliser la méthode `.concat()` pour ajouter cette nouvelle tâche à notre tableau dans l'état. Tout ce que nous avons à faire est de retourner cette expression. 

Ajoutons une nouvelle tâche, comme "Équilibrer le chéquier". Une fois que nous cliquons sur soumettre, nous la voyons immédiatement ajoutée à notre liste :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/tutorial-12.gif)

Maintenant, il y a un problème ici : nous ne vidons pas notre entrée après que notre formulaire a été soumis. 

Cela signifie que si nous voulions ajouter une autre tâche, nous devrions la vider manuellement. Comment prenons-nous la valeur de cette entrée et la vidons-nous ?

## Références React et useRef

Pour effectuer des actions courantes telles que vider la valeur d'une entrée ou focaliser notre entrée, nous pouvons utiliser ce qu'on appelle une **référence**. 

> Une référence est une fonctionnalité que React fournit pour référencer un élément DOM donné. 

Dans ce cas, nous voulons une référence à cet élément d'entrée avec le nom "addTodo". 

Tout comme notre état, nous pouvons travailler avec des références en appelant le hook React approprié. Pour créer une référence, nous devons simplement appeler `React.useRef()` en haut de AddTodo. Nous n'avons pas à lui passer une valeur initiale, mais nous pouvons lui donner une valeur par défaut si nous en avions besoin. 

Nous appellerons cette référence créée `inputRef`. En utilisant inputRef, nous pouvons créer une référence à notre élément d'entrée auquel nous pouvons accéder où nous le souhaitons en utilisant la prop ref intégrée en définissant `ref={inputRef}` :

```js
// src/App.js
import React from "react";
import "./styles.css";

//...

function AddTodo({ setTodos }) {
  const inputRef = React.useRef();

  function handleAddTodo(event) {
    event.preventDefault();
    const text = event.target.elements.addTodo.value;
    const todo = {
      id: 4,
      text,
      done: false
    };
    setTodos((prevTodos) => {
      return prevTodos.concat(todo);
    });
  }

  return (
    <form onSubmit={handleAddTodo}>
      <input name="addTodo" placeholder="Ajouter une tâche" ref={inputRef} />
      <button type="submit">Soumettre</button>
    </form>
  );
}
```

Que fait cela ? Cela nous permet, dans `handleAddTodo`, d'utiliser la propriété `inputRef.current`, qui contient l'élément d'entrée lui-même. Si nous devions logger `input.ref.current`, nous verrions notre élément d'entrée. 

Nous avons une référence directe à notre entrée, ce qui signifie que nous pouvons accéder à n'importe quelle propriété que nous souhaitons. Dans notre cas, nous voulons prendre la valeur de l'entrée sur la propriété value. Pour effacer la valeur de notre entrée, nous pouvons simplement muter inputRef directement en définissant la valeur sur une chaîne vide :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/tutorial-13.gif)

Chaque fois que nous cliquons sur soumettre, notre entrée est vidée sans que nous ayons à la vider manuellement nous-mêmes.

## Règles essentielles des hooks React

Puisque useRef est un autre hook React, nous commençons à voir certaines caractéristiques communes parmi les hooks React. Ils sont souvent préfixés par le mot "use". En fait, la plupart des hooks React ont ce préfixe pour indiquer qu'ils sont des hooks et doivent être utilisés comme tels. 

De plus, les hooks React sont appelés tout en haut des composants de fonction. Les hooks ne peuvent pas être utilisés dans les composants de classe. Et enfin, les hooks ne peuvent pas être conditionnels (c'est-à-dire utilisés dans une instruction if).

Mais comme vous pouvez le voir, il n'y a rien de trop spécial avec les hooks React. Ils fonctionnent beaucoup comme des fonctions JavaScript régulières. 

## Comment marquer les tâches comme terminées avec onClick

Après avoir créé des tâches, nous voulons les basculer comme terminées – pour les barrer si nous avons terminé une tâche donnée. Comment ajoutons-nous cette fonctionnalité ? 

Si nous retournons à notre élément de liste, dans TodoList, nous pouvons voir à quoi cela ressemblera en appliquant quelques styles en ligne. Nous avons vu comment ajouter des styles via des classes. Pour les styles que nous voulons appliquer en ligne à n'importe quel élément donné, nous ne pouvons pas utiliser la même syntaxe que nous utiliserions avec le HTML normal. 

Si nous essayions d'utiliser la syntaxe HTML, nous obtiendrions une erreur nous disant "la prop style attend des propriétés de style dans un objet, pas dans une chaîne" :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/tutorial-14.png)

Pour corriger cela, nous fournirons un objet. Nous devons fournir cet objet dans un autre ensemble d'accolades. Ensuite, nous fournirons n'importe quelle propriété comme nous le ferions dans un objet JavaScript normal pour appliquer ce style de barré. 

Pour chacun de nos éléments de liste, nous pouvons définir la propriété `textDecoration` sur "line-through" :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/tutorial-15.png)

Nous ne voulons pas que chaque élément soit barré, nous voulons que cela ne soit appliqué que si une tâche donnée est terminée. Comment faisons-nous cela ? 

Nous pouvons utiliser une conditionnelle JavaScript normale, en particulier une ternaire, pour dire que si la propriété done d'une tâche donnée est vraie, alors nous voulons appliquer la valeur de barré pour la décoration de texte, sinon non. 

Si nous changeons l'une de nos tâches du tableau pour avoir une valeur done de `true`, nous voyons que cette règle de style est appliquée :

```js
// src/App.js

//...

function TodoList({ todos }) {
  return (
    <ul>
      {todos.map((todo) => (
        <li
          style={{
            textDecoration: todo.done ? "line-through" : ""
          }}
          key={todo.id}
        >
          {todo.text}
        </li>
      ))}
    </ul>
  );
}

//...
```

Comment basculons-nous réellement cette tâche ? 

Nous pourrions vouloir que notre utilisateur clique ou double-clique sur notre tâche pour la barrer. Cela signifie que nous voulons voir comment enregistrer et gérer un nouveau type d'événement – un événement de clic. 

Pour gérer un événement de clic avec React, nous fournissons la prop `onClick` à un élément donné pour lequel nous voulons enregistrer cet événement. Dans ce cas, c'est l'élément `li`. 

Une fois de plus, nous devons le connecter à une fonction pour gérer notre événement de clic. Nous allons appeler cela `handleToggleTodo` et le créer dans notre composant TodoList. Dans ce cas, notre fonction que nous utilisons pour gérer l'événement n'a pas besoin de recevoir de données d'événement. Cette fonction gérera la mise à jour de l'état de notre tâche. 

Nous voulons que `handleToggleTodo` parcourt le tableau `todos` et voit si celui sur lequel l'utilisateur a cliqué existe dans notre tableau. Si c'est le cas, sa valeur done peut être basculée à la valeur booléenne opposée. 

Pour recevoir les données de tâche appropriées pour l'élément de liste approprié sur lequel on a cliqué, nous pouvons appeler `handleToggleTodo` comme une fonction fléchée en ligne et passer les données de tâche comme argument : 

```js
// src/App.js

//...

function TodoList({ todos }) {
  function handleToggleTodo(todo) {}
    
  return (
    <ul>
      {todos.map((todo) => (
        <li
          onClick={() => handleToggleTodo(todo)}
          style={{
            textDecoration: todo.done ? "line-through" : ""
          }}
          key={todo.id}
        >
          {todo.text}
        </li>
      ))}
    </ul>
  );
}

//...
```

Pour mettre à jour notre état de tâches, nous allons passer `setTodos` à notre composant TodoList. Nous allons passer `setTodos` comme une prop à TodoList, et le déstructurer de l'objet props. 

Une fois de plus, nous pouvons appeler `setTodos` et obtenir l'accès aux tâches précédentes en incluant une fonction interne. Tout d'abord, ce que nous pouvons faire est de prendre tout notre tableau de tâches et de mapper dessus avec la fonction de tableau `.map()`. 

Dans la fonction interne passée à map, nous vérifierons que l'id des tâches sur lequel nous mappons est égal à la tâche sur laquelle nous avons cliqué. Si c'est le cas, nous retournons un nouvel objet avec toutes les propriétés précédentes de la tâche, mais avec `done` basculé à sa valeur booléenne opposée :

```js
// src/App.js

//...

function TodoList({ todos, setTodos }) {
  function handleToggleTodo(todo) {
    // confus par ce code ? Voici ce qu'il dit :
      
    // si l'id d'une tâche est égal à celui sur lequel nous avons cliqué,
    // mettez simplement à jour la valeur done de cette tâche à son opposé,
    // sinon, ne faites rien (retournez-la)
      
    const updatedTodos = todos.map((t) =>
      t.id === todo.id
        ? {
            ...t,
            done: !t.done
          }
        : t
    );
  }

  return (
    <ul>
      {todos.map((todo) => (
        <li
          onDoubleClick={() => handleToggleTodo(todo)}
          style={{
            textDecoration: todo.done ? "line-through" : ""
          }}
          key={todo.id}
        >
          {todo.text}
          <DeleteTodo todo={todo} setTodos={setTodos} />
        </li>
      ))}
    </ul>
  );
}

//...
```

Sinon, si cette tâche sur laquelle nous itérons n'est pas celle sur laquelle nous avons cliqué, nous voulons simplement la retourner (sans la changer). Ce tableau mis à jour est ce que nous passerons à `setTodos` pour mettre à jour notre état. 

Si nous cliquons sur une tâche, nous la basculons comme terminée. Si nous cliquons à nouveau dessus, elle est basculée comme non terminée :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/tutorial-16.gif)

Pour que cela fonctionne correctement, pour voir qu'un id de tâche passé est égal à la tâche sur laquelle nous cliquons, nous devons nous assurer que chaque id de tâche est unique. 

Au lieu de définir chaque nouvelle tâche pour qu'elle ait un id de 4, nous pouvons simplement utiliser `Math.random()` pour créer une valeur semi-aléatoire et nous assurer qu'il n'y a pas d'éléments de liste avec le même id. 

Enfin, comme alternative à `onClick`, nous pouvons utiliser une autre prop d'événement, `onDoubleClick`, au cas où les utilisateurs cliqueraient accidentellement sur une tâche donnée. Maintenant, si un utilisateur double-clique sur un élément de liste, ce n'est qu'alors que nous le basculons comme terminé. 

## Comment gérer la suppression des tâches

La dernière partie de la fonctionnalité que nous recherchons est de pouvoir supprimer une tâche donnée. 

Nous pouvons ajouter cette fonctionnalité dans TodoList en ajoutant un autre composant imbriqué. Sous notre texte de tâche, nous ajouterons un nouveau composant : DeleteTodo. Déclarons ce nouveau composant au-dessus de l'endroit où nous avons déclaré AddTodo. 

De quoi ce composant sera-t-il constitué ? Dans celui-ci, nous retournerons un span, qui fonctionnera comme un bouton pour nous. Un utilisateur peut cliquer dessus et supprimer une tâche donnée. 

> Si vous voulez qu'un élément non-bouton fonctionne comme un bouton, nous devons définir sa propriété "role" sur "button". 

À notre span, ajoutons quelques règles de style – nous pouvons lui donner une couleur rouge, le rendre gras et le séparer du texte de la tâche en définissant `marginLeft: 10`. Ce qui est bien avec l'objet style, c'est que nous n'avons pas à dire 10 pixels comme une chaîne – nous pouvons utiliser la valeur 10 ou inclure n'importe quel entier que nous aimons.

Voici le code pour notre composant DeleteTodo jusqu'à présent :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/tutorial-17.png)

Pour supprimer une tâche, nous voulons pouvoir cliquer dessus et afficher une boîte de dialogue de confirmation. Si l'utilisateur confirme qu'il veut la supprimer, ce n'est qu'alors que la tâche est supprimée. 

Puisque nous mappons chaque élément de tâche, y compris DeleteTodo, nous pouvons passer une prop appelée simplement `todo` avec les données de chaque tâche. 

Dans DeleteTodo, sur notre élément span, nous voulons ajouter un `onClick` pour gérer la suppression de notre tâche. Pour gérer cela, nous appellerons une nouvelle fonction : `handleDeleteTodo`. 

En utilisant cette fonction, nous voulons d'abord afficher une boîte de dialogue de confirmation. Nous pouvons le faire en disant `window.confirm()` avec le message, "Voulez-vous supprimer cela ?" `window.confirm` va retourner une valeur de vrai ou faux en fonction de si l'utilisateur a confirmé la boîte de dialogue ou non. Nous mettrons le résultat de cette action dans une variable appelée `confirmed` :

```js
// src/App.js
// ...

function TodoList({ todos, setTodos }) {
  // ...

  return (
    <ul>
      {todos.map((todo) => (
        <li
          onDoubleClick={() => handleToggleTodo(todo)}
          style={{
            textDecoration: todo.done ? "line-through" : ""
          }}
          key={todo.id}
        >
          {todo.text}
          {/* passer les données de la tâche comme une prop à DeleteTodo */}
          <DeleteTodo todo={todo} />
        </li>
      ))}
    </ul>
  );
}

function DeleteTodo({ todo, setTodos }) {
  function handleDeleteTodo() {
    const confirmed = window.confirm("Voulez-vous supprimer cela ?");
    if (confirmed) {
      // s'occuper de la suppression de la tâche
    }
  }

  return (
    <span
      onClick={handleDeleteTodo}
      role="button"
      style={{
        color: "red",
        fontWeight: "bold",
        marginLeft: 10,
        cursor: "pointer"
      }}
    >
      x
    </span>
  );
}

//...
```

Si `confirmed` est vrai, alors seulement nous voulons supprimer la tâche.

Pour ce faire, nous devons utiliser `setTodos` une fois de plus. Nous allons le passer un niveau plus bas de TodoList au composant DeleteTodo et le déstructurer de l'objet props. 

Ensuite, dans `handleDeleteTodo`, nous pouvons l'appeler et utiliser la fonction interne pour obtenir les tâches précédentes. Pour supprimer la tâche sur laquelle un utilisateur a cliqué, nous pouvons filtrer ce tableau pour nous assurer que nous supprimons celle que l'utilisateur a sélectionnée. 

Pour ce faire, nous nous assurons que toutes les tâches de notre tableau n'ont pas un id égal à celui que nous tentons de supprimer :

```js
// src/App.js

// ...

function DeleteTodo({ todo, setTodos }) {
  function handleDeleteTodo() {
    const confirmed = window.confirm("Voulez-vous supprimer cela ?");
    if (confirmed) {
      setTodos((prevTodos) => {
        return prevTodos.filter((t) => t.id !== todo.id);
      });
    }
  }

  return (
    <span
      onClick={handleDeleteTodo}
      role="button"
      style={{
        color: "red",
        fontWeight: "bold",
        marginLeft: 10,
        cursor: "pointer"
      }}
    >
      x
    </span>
  );
}

// ...
```

Maintenant, si nous essayons de supprimer l'une de nos tâches, nous voyons notre boîte de dialogue de confirmation, nous cliquons sur "ok", et elle est immédiatement supprimée de notre liste. 

Si nous supprimons toutes nos tâches, nous ne voyons plus rien. Si nous voulons dire à notre utilisateur qu'il n'y a plus de tâches dans la liste lorsque le tableau est vide, dirigeons-nous vers notre composant TodoList. 

Si nous avons un tableau de tâches vide, nous pouvons ajouter une conditionnelle au-dessus de notre retour et vérifier si la longueur de notre tableau est égale à 0. Si c'est le cas, nous afficherons un élément de paragraphe avec le texte "Plus de tâches !" :

```js
// ...

function TodoList({ todos, setTodos }) {
  function handleToggleTodo(todo) {
    const updatedTodos = todos.map((t) =>
      t.id === todo.id
        ? {
            ...t,
            done: !t.done
          }
        : t
    );
    setTodos(updatedTodos);
  }

  if (!todos.length) {
    return <p>Plus de tâches !</p>;
  }

  return (
    <ul>
      {todos.map((todo) => (
        <li
          onDoubleClick={() => handleToggleTodo(todo)}
          style={{
            textDecoration: todo.done ? "line-through" : ""
          }}
          key={todo.id}
        >
          {todo.text}
          <DeleteTodo todo={todo} setTodos={setTodos} />
        </li>
      ))}
    </ul>
  );
}

// ...
```

## Félicitations ! 

Vous avez maintenant une application de tâches fonctionnelle qui a une fonctionnalité CRUD complète qui peut créer, lire, mettre à jour et supprimer des tâches.

Vous avez pu voir comment de nombreux concepts majeurs de React fonctionnent en première main et vous êtes maintenant dans une excellente position pour commencer à construire vos propres applications React.

Si vous souhaitez jeter un coup d'œil au code final de notre application, vous pouvez le voir [ici](https://codesandbox.io/s/late-firefly-ker6p).

## Devenez un développeur React professionnel

React est difficile. Vous ne devriez pas avoir à le comprendre par vous-même.

J'ai mis tout ce que je sais sur React dans un seul cours, pour vous aider à atteindre vos objectifs en un temps record :

[**Présentation : Le Bootcamp React**](https://www.thereactbootcamp.com)

**C'est le seul cours que j'aurais aimé avoir lorsque j'ai commencé à apprendre React.**

Cliquez ci-dessous pour essayer le Bootcamp React par vous-même :

[![Cliquez pour rejoindre le Bootcamp React](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Cliquez pour commencer*