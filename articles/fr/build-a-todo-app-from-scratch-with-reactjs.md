---
title: Comment créer une application TODO à partir de zéro avec React.js
subtitle: ''
author: Spruce Emmanuel
co_authors: []
series: null
date: '2024-04-12T16:23:13.000Z'
originalURL: https://freecodecamp.org/news/build-a-todo-app-from-scratch-with-reactjs
coverImage: https://www.freecodecamp.org/news/content/images/2024/04/Screenshot-2024-04-10-at-7.27.44-AM.png
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
seo_title: Comment créer une application TODO à partir de zéro avec React.js
seo_desc: 'If you''re new to React.js and you''re eager to dive into application development,
  then you''ve come to the right place!

  Join me in this tutorial as I walk you through building a basic TODO app from the
  ground up.

  The Importance of a TODO App for Beginn...'
---

Si vous êtes nouveau dans React.js et que vous êtes impatient de vous lancer dans le développement d'applications, alors vous êtes au bon endroit !

Rejoignez-moi dans ce tutoriel alors que je vous guide à travers la création d'une application TODO basique à partir de zéro.

## L'importance d'une application TODO pour les débutants

Une application TODO sert de projet idéal pour les débutants afin de saisir rapidement les fondamentaux d'un nouveau langage de programmation ou d'un framework. Elle fournit un contexte pratique pour apprendre des concepts essentiels tout en travaillant vers un résultat tangible.

Si vous commencez votre voyage avec React.js, construire une application TODO avec ce tutoriel pourrait être le point de départ parfait.

## Prérequis

Avant de commencer, assurez-vous d'avoir des connaissances de base en React.js et d'avoir Node.js et npm installés sur votre ordinateur. Si ce n'est pas déjà fait, [prenez un moment pour configurer votre environnement de développement.](https://www.freecodecamp.org/news/how-to-install-react-a-step-by-step-guide/)

## Notre objectif

Notre objectif est de créer une application TODO simple avec des fonctionnalités. Voici ce que nous allons viser :

* Ajouter de nouvelles TODOs : Permettre aux utilisateurs d'ajouter de nouvelles tâches à la liste.
    
* Modifier et supprimer des TODOs : Fournir une fonctionnalité pour modifier ou supprimer des tâches existantes.
    
* Marquer les TODOs comme terminées : Permettre aux utilisateurs d'indiquer quand les tâches sont terminées.
    
* Suivre les TODOs terminées : Implémenter une fonctionnalité pour garder une trace de toutes les tâches terminées.
    

N'hésitez pas à étendre cette liste avec des fonctionnalités supplémentaires si vous le souhaitez. Dans le cadre de ce tutoriel, nous nous concentrerons sur ces fonctionnalités principales.

Voici un exemple de l'application TODO que nous allons construire :

![Image](https://lh7-us.googleusercontent.com/c6jXW1lvtqwDfabL0JRlt4C136nqXe-S5PRJKMywRKzuErt9sFnaXTbKl3tKFe2ZWEK2kIMSk1eDAEN5HtyFKbmsRo2nuXabVD-w8h1WNJnInEn5Gc3elHLGd0xOMonokRFA0tqiS8fxr64is1pFOwg align="left")

*Un aperçu de notre application todo*

## Table des matières :

1. [Comment configurer votre application React](#heading-installation)
    
2. [Comment construire les composants](#heading-construction-des-composants)
    
    * [Le composant Header](#heading-le-composant-header)
        
    * [Le composant TODOHero](#heading-le-composant-todohero)
        
    * [Le composant Form](#heading-le-composant-form)
        
    * [Le composant TODOList](#heading-le-composant-todolist)
        
3. [Tout assembler](#heading-tout-assembler)
    
    * [Le style](#heading-le-style)
        
4. [Construire la fonctionnalité : Comment ajouter des todos](#heading-construction-de-la-fonctionnalite-comment-ajouter-des-todos)
    
    * [Une façon de stocker les données Todo](#heading-une-facon-de-stocker-les-donnees-todo)
        
    * [Quel type de données voulons-nous stocker ?](#heading-quel-type-de-donnees-voulons-nous-stocker)
        
    * [Comment passer les données Todo à nos composants](#heading-comment-passer-les-donnees-todo-a-nos-composants)
        
    * [Ajouter plus de données Todo à notre état](#heading-ajouter-plus-de-donnees-todo-a-notre-etat)
        
5. [Comment construire la fonctionnalité de l'application TODO](#heading-comment-construire-la-fonctionnalite-de-lapplication-todo)
    
    * [Comment marquer les todos comme terminées](#heading-comment-marquer-les-todos-comme-terminees)
        
    * [Comment modifier les todos](#heading-comment-modifier-les-todos)
        
    * [Comment supprimer les todos](#heading-comment-supprimer-les-todos)
        
6. [Comment persister nos données Todo](#heading-comment-persister-nos-donnees-todo)
    
    * [Comment persister les données Todo dans localStorage](#heading-comment-persister-les-donnees-todo-dans-localstorage)
        
    * [Comment lire les données Todo depuis localStorage](#heading-comment-lire-les-donnees-todo-depuis-localstorage)
        
7. [Et nous l'avons fait.](#summary)
    

## Comment configurer votre application React

En 2024, utiliser un framework comme Next.js ou Remix est une approche recommandée pour initier un projet React. L'un ou l'autre framework suffira – choisissez simplement celui avec lequel vous êtes le plus à l'aise. Pour ce tutoriel, nous utiliserons Next.js.

Pour créer une application React avec Next.js, naviguez vers votre répertoire préféré et exécutez la commande suivante :

```bash
npx create-next-app@latest
```

Note : Nous n'utiliserons pas TypeScript et TailwindCSS pour ce projet, vous pouvez donc procéder avec les paramètres par défaut.

Une fois l'installation terminée, naviguez dans votre nouveau répertoire d'application (j'ai nommé le mien 'todo') et démarrez le serveur de développement en exécutant :

```bash
cd todo
npm run dev
## ou avec yarn
cd todo
yarn run dev
```

Avec votre serveur de développement en cours d'exécution, nous sommes prêts à commencer à créer notre application TODO !

## Comment construire les composants

Dans React, nous construisons des interfaces utilisateur à partir de composants. L'interface utilisateur de notre application TODO se compose de plusieurs parties. Décomposons-les :

### Le composant Header

Le composant Header sert à afficher le titre de notre application. Plutôt que d'intégrer directement du HTML, nous allons construire cette fonctionnalité dans un composant React.

Commencez par créer un répertoire pour nos composants :

```bash
# Dans le répertoire racine de votre projet, créez un nouveau répertoire
mkdir src/components
# Naviguez dans le répertoire
cd src/components
# Créez un nouveau fichier pour le composant Header
touch Header.jsx
```

Les composants dans React sont essentiellement des fonctions JavaScript qui retournent du HTML. Dans notre fichier Header.jsx, définissez une fonction qui retourne le contenu HTML pour notre composant Header :

```jsx
// src/components/Header.jsx
function Header() {
  return (
    <>
      <svg>
        <path d="" /> 
      </svg>
      <h1>TODO</h1>
    </>
  );
}

export default Header;
```

Nous exportons la fonction Header afin de pouvoir l'utiliser dans tout notre projet.

### Le composant TODOHero

Le composant TODOHero joue un rôle pivot dans notre application. Il sert de section où nous fournissons un aperçu du nombre total de todos et du nombre de tâches terminées.

![Image](https://lh7-us.googleusercontent.com/BEGn3mOpp0K5yZyALAFqwNASN8UDcJJwc1JYugAKgRECnsOAsv2la6O7nPtSJXmOffXc-dre7Ftu6aJFUrWgfV9AychKvECOTspY6vGdiMtQZ2O5uufi8e4UaC2I1JgchsHvN4LlegRG9K6cteGu1jA align="left")

*Une image montrant le* `TODOHero` component

Contrairement au composant d'en-tête, qui reste statique tout au long de l'utilisation de notre application, le composant `TODOHero` est dynamique. Il se met à jour en continu en fonction du nombre de todos terminées et du nombre total de todos.

Lors de la construction de composants, il est important d'identifier les parties dynamiques dès le début. Dans React, nous y parvenons en passant des arguments, appelés props, à nos composants.

Créons le composant `TODOHero`. Tout d'abord, assurez-vous d'être dans le répertoire src/components :

```bash
cd src/components
```

Maintenant, créez un nouveau fichier pour le composant `TODOHero` :

```bash
touch TODOHero.jsx
```

Dans TODOHero.jsx, définissez une fonction qui prend les props comme arguments :

```jsx
// src/components/TODOHero.jsx
function TODOHero({ todos_completed, total_todos }) {
  return (
    <section>
      <div>
        <p>Tâches terminées</p>
        <p>Continuez comme ça</p>
      </div>
      <div>
        {todos_completed}/{total_todos}
      </div>
    </section>
  );
}
export default TODOHero;
```

Cette fonction retourne le contenu HTML pour notre composant TODOHero. Nous utilisons les props pour mettre à jour dynamiquement le nombre de todos terminées et le nombre total de todos.

### Le composant Form

Notre composant Form sera un simple champ de saisie avec un bouton de soumission, alors créez un nouveau composant

```bash
touch src/components/Form.jsx
```

Comme je l'ai dit, ce sera un formulaire très simple : juste un champ de saisie avec un bouton de soumission. Le label est pour l'accessibilité.

```jsx
// src/components/Form.jsx

function Form() {
  const handleSubmit = (event) => {
    event.preventDefault();
    // réinitialiser le formulaire
    event.target.reset();
  };
  return (
    <form className="form" onSubmit={handleSubmit}>
      <label htmlFor="todo">
        <input
          type="text"
          name="todo"
          id="todo"
          placeholder="Écrivez votre prochaine tâche"
        />
      </label>
      <button>
        <span className="visually-hidden">Soumettre</span>
        <svg>
          <path d="" />
        </svg>
      </button>
    </form>
  );
}
export default Form;
```

Nous avons ajouté un événement `onSubmit` au formulaire avec un gestionnaire d'événements `handleSubmit`. Le `event.preventDefault()` empêche le formulaire de se soumettre et de recharger toute l'application. Enfin, nous réinitialisons le formulaire avec `event.target.reset()`.

### Le composant TODOList

Enfin, créons le composant List. Commencez par créer un nouveau fichier de composant nommé TODOList.jsx :

```bash
touch src/components/TODOList.jsx
```

La liste elle-même est une liste ordonnée simple :

```jsx
// src/components/TODOList.jsx

function TODOList() {
  return <ol className="todo_list">{/* <li> la liste va ici */}</ol>;
}
export default TODOList;
```

Les éléments de la liste seront générés dynamiquement à partir des données todo. Mais avant de continuer, créons un composant séparé pour l'élément de la liste.

Dans React, presque tout est un composant, donc nous créerons le composant `Item` avec le composant `TODOList` :

```jsx
// src/components/TODOList.jsx

function Item({ item }) {
  return (
    <li id={item?.id} className="todo_item">
      <button className="todo_items_left">
        <svg>
          <circle cx="11.998" cy="11.998" fillRule="nonzero" r="9.998" />
        </svg>
        <p>{item?.title}</p>
      </button>
      <div className="todo_items_right">
        <button>
          <span className="visually-hidden">Modifier</span>
          <svg>
            <path d="" />
          </svg>
        </button>
        <button>
          <span className="visually-hidden">Supprimer</span>
          <svg>
            <path d="" />
          </svg>
        </button>
      </div>
    </li>
  );
}
```

L'élément de la liste lui-même est simplement un élément `<li>` avec des boutons pour modifier et supprimer les tâches. Nous avons veillé à ce que le `<li>` lui-même ne soit pas cliquable, suivant le principe que "tout ce qui est cliquable sur le web doit être soit un bouton, soit un lien".

Maintenant, nous pouvons utiliser le composant `Item` dans notre liste :

```jsx
// src/components/TODOList.jsx

function TODOList({ todos }) {
  return (
    <ol className="todo_list">
      {todos && todos.length > 0 ? (
        todos?.map((item, index) => <Item key={index} item={item} />)
      ) : (
        <p>Il semble solitaire ici, que faites-vous ?</p>
      )}
    </ol>
  );
}
export default TODOList;
```

Avec ces composants en place, l'interface utilisateur de notre application TODO est entièrement construite.

## Tout assembler

Jusqu'à présent, nous avons créé quatre composants distincts, chacun ne faisant pas grand-chose par lui-même. Maintenant, nous devons rendre ces composants dans notre page d'index.

Dans Next.js, les pages sont situées à l'intérieur du répertoire src/app, et la page d'index est généralement nommée page.js.

Tout d'abord, vidons le contenu du fichier car nous n'aurons pas besoin de quoi que ce soit à l'intérieur :

```bash
echo -n > src/app/page.js
```

Ensuite, importons tous les composants que nous avons créés et utilisons-les dans le fichier page.js comme montré ci-dessous :

```jsx
// src/app/page.js

import React from "react";
import Form from "@/components/Form";
import Header from "@/components/Header";
import TODOHero from "@/components/TODOHero";
import TODOList from "@/components/TODOList";
function Home() {
  return (
    <div className="wrapper">
      <Header />
      <TODOHero todos_completed={0} total_todos={0} />
      <Form />
      <TODOList todos={[]} />
    </div>
  );
}
export default Home;
```

En visualisant la sortie dans votre navigateur, cela devrait ressembler à quelque chose comme ceci :

![Image](https://lh7-us.googleusercontent.com/iarew4c0BX773LQXr_pmwOpUK7YFQt-shtsuYPVfqKI9_Z6JsBMj90A3BvE_WFKK37jxoAyG038xHeuvsJsAhhky6D-tH_VzVKqfvjlT1TkYv_v52VDNEl7IbrgjL_c439Ws8JsMO887a6ipk3H_4Pk align="left")

*Un aperçu de notre application sans CSS*

### Le style

Pour le style, nous allons utiliser le bon vieux CSS. Créons un fichier styles.css pour contenir nos styles :

```bash
touch src/app/styles.css
```

Supprimez également tous les fichiers CSS qui sont venus avec l'installation de Next.js car nous n'en aurons pas besoin :

```bash
rm src/app/page.module.css && src/app/globals.css
```

Maintenant, vous pouvez ajouter vos règles CSS dans le fichier styles.css. Bien que ce ne soit pas parfait, le CSS suivant devrait suffire pour notre exemple simple :

```css
*,
*::after,
*::before {
  padding: 0;
  margin: 0;
  font-family: inherit;
  box-sizing: border-box;
}
html,
body {
  font-family: sans-serif;
  background-color: #0d0d0d;
  color: #fff;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100vw;
}
button {
  cursor: pointer;
}
.visually-hidden {
  position: absolute !important;
  clip: rect(1px, 1px, 1px, 1px);
  padding: 0 !important;
  border: 0 !important;
  height: 1px !important;
  width: 1px !important;
  overflow: hidden;
  white-space: nowrap;
}
.text_large {
  font-size: 32px;
}
.text_small {
  font-size: 24px;
}
.wrapper {
  display: flex;
  flex-direction: column;
  width: 70%;
}
@media (max-width: 510px) {
  .wrapper {
    width: 100%;
  }
  header {
    justify-content: center;
  }
}
header {
  display: flex;
  align-items: center;
  justify-content: flex-start;
  gap: 12px;
  padding: 42px;
}
.todohero_section {
  border: 1px solid #c2b39a;
  display: flex;
  align-items: center;
  justify-content: space-around;
  align-self: center;
  width: 90%;
  max-width: 455px;
  padding: 12px;
  border-radius: 11px;
}
.todohero_section div:last-child {
  background-color: #88ab33;
  width: 150px;
  height: 150px;
  border-radius: 75px;
  font-size: 48px;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
}
.form {
  align-self: center;
  width: 97%;
  max-width: 455px;
  display: flex;
  align-items: center;
  gap: 12px;
  margin-top: 38px;
}
.form label {
  width: 90%;
}
.form input {
  background-color: #1f2937;
  color: #fff;
  width: 100%;
  height: 50px;
  outline: none;
  border: none;
  border-radius: 11px;
  padding: 12px;
}
.form button {
  width: 10%;
  height: 50px;
  border-radius: 11px;
  background-color: #88ab33;
  border: none;
}
.todo_list {
  align-self: center;
  width: 97%;
  max-width: 455px;
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 27px;
  margin-bottom: 27px;
  gap: 27px;
}
.todo_item,
.edit-form input {
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 70px;
  width: 100%;
  max-width: 455px;
  border: 1px solid #c2b39a;
  font-size: 16px;
  background-color: #0d0d0d;
  color: #fff;
  padding: 12px;
}
.edit-form input {
  outline: transparent;
  width: calc(100% - 14px);
  height: calc(100% - 12px);
  border: transparent;
}
.todo_items_left,
.todo_items_right {
  display: flex;
  align-items: center;
}
.todo_items_left {
  background-color: transparent;
  border: none;
  color: #fff;
  gap: 12px;
  font-size: 16px;
}
.todo_items_right {
  gap: 4px;
}
.todo_items_right button {
  background-color: transparent;
  color: #fff;
  border: none;
}
.todo_items_right button svg {
  fill: #c2b39a;
}
```

Enfin, nous devons importer le fichier CSS dans notre layout. Ouvrez le fichier layout.js situé à côté du fichier page.js et importez le fichier CSS comme démontré ci-dessous :

![Image](https://lh7-us.googleusercontent.com/BMQnzUwBP_ksPvXvMdG2WgpsLZCA4xrucsHmuAg16JCmciXLh8CREGOIbCmrGPKtR_uEJYG50bL0SUw7Yb_oj2fnRsgAfnSIwKWTyOtIhSje_p7HPe818ZvXFbey54EOlNibmABCOkmkTiaF-zzFptY align="left")

*Une image montrant comment importer le fichier styles.css dans notre composant*

Lors de l'aperçu de l'application à nouveau, elle devrait maintenant refléter les styles appliqués :

![Image](https://lh7-us.googleusercontent.com/kJ9zqWtpAHFcR0zxgQr9HOVOlQiCUXRFDoyMRn4_erG9DTGOTZ3x1lS3BvhhyY3h3rhuvIuLvQ2v5IQshQsc7rDl6Kjsqjspi4EdhoWKgxjejerJ9WRoJXvU78eDnjTB90WIMky31lUemGB1KlMQqXw align="left")

*Une image montrant l'aperçu de notre application après l'ajout de CSS*

## Construire la fonctionnalité : Comment ajouter des todos

À ce stade, nous avons créé une application todo visuellement attrayante, mais elle manque de fonctionnalité. Changeons cela dans cette section.

### Une façon de stocker les données Todo

Tout d'abord, nous avons besoin d'une méthode pour stocker nos données todo. Dans React, cela est accompli en utilisant l'état—un objet JavaScript qui contient des informations sur l'état d'un composant.

React fournit un hook appelé `useState()`, qui nous permet de gérer l'état dans nos applications React. Mais dans Next.js, avant d'utiliser `useState`, vous devez spécifier que le composant est un composant client.

Ajoutez le code suivant en haut de votre fichier src/app/page.js :

```js
"use client";
```

Comme illustré dans l'image ci-dessous :

![Image](https://lh7-us.googleusercontent.com/-K5nq04GCngiUGJEbtSQhNprJ0eTPPzapT8MjCcEYSRyEXq5Tz8zT4hgqwSd5wcwgZNgnkVA_fpraJhxJog3aZiynE9CdvzO0VGF-wHTpodvilFYNW7uICnAD9zdqvuxVbbZQ3pMizcbiPoD78kb0Zw align="left")

*Une image montrant comment ajouter "use client" en haut de notre page.js*

Maintenant, nous pouvons utiliser le hook `useState` pour créer un état pour nos données todo :

```jsx
// src/app/page.js

"use client";
import React from "react";
import Form from "@/components/Form";
// Ajoutez les imports pour les autres composants
function Home() {
  const [todos, setTodos] = React.useState([]);
  return (
    <Header />
    // Ajoutez d'autres composants ici
  );
}
export default Home;
```

Dans l'extrait de code ci-dessus, vous remarquerez que `useState` contient initialement un tableau vide. Il est important de comprendre que `useState` retourne deux valeurs : `todos` et `setTodos` (vous pouvez nommer celles-ci comme vous le préférez).

La première valeur, `todos`, contient la valeur actuelle de l'état, tandis que `setTodos` (la deuxième valeur) est une fonction utilisée pour mettre à jour l'état. C'est clair jusqu'à présent ?

### Quel type de données voulons-nous stocker ?

Maintenant que nous avons un moyen de stocker nos données, définissons le type de données que nous avons l'intention de stocker. Essentiellement, ce sera un tableau d'objets, où chaque objet contient les informations nécessaires pour rendre notre liste de todos :

```js
const [todos, setTodos] = React.useState([
{ /* Object */ },
{ /* Object */ },
{ /* Object */ },
]);
```

Chaque objet dans le tableau aura la structure suivante :

```js
{
title: "Some task",  // string
id: self.crypto.randomUUID(), // string
is_completed: false // boolean
}
```

Ici, `self.crypto.randomUUID()` est une méthode qui permet au navigateur de générer des identifiants uniques pour chaque élément todo. Si vous consultez la console, vous observerez que les identifiants générés sont effectivement uniques.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/Screenshot-2024-04-04-at-9.47.22-PM.png align="left")

*console.log de nos données todo*

Cette structure garantit que chaque élément todo a un titre, un identifiant unique (id) et une valeur booléenne indiquant si la tâche est terminée (`is_completed`).

### Comment passer les données Todo à nos composants

Dans React, il existe un concept appelé partage d'état, qui permet aux composants enfants d'accéder à l'état de leurs composants parents. Cela signifie que l'état todo que nous avons créé précédemment peut être partagé entre tous nos composants.

Le premier endroit où nous avons besoin des données de l'état est dans notre composant List. Passons l'état au composant List :

```jsx
// src/app/page.js

"use client";
import React from "react";
// importer d'autres composants
import TODOList from "@/components/TODOList";

function Home() {
  const [todos, setTodos] = React.useState([
    { title: "Some task", id: self.crypto.randomUUID(), is_completed: false },
    {
      title: "Some other task",
      id: self.crypto.randomUUID(),
      is_completed: true,
    },
    { title: "last task", id: self.crypto.randomUUID(), is_completed: false },
  ]);
  return (
    <div className="wrapper">
      ...
      <TODOList todos={todos} />
    </div>
  );
}
export default Home;
```

Nous avons déjà fait des provisions dans notre composant List pour recevoir une prop `todos` :

```jsx
// src/components/TODOList.jsx

function TODOList({ todos }) {
  return (
    <ol className="todo_list">
      {todos && todos.length > 0 ? (
        todos?.map((item, index) => (
          <Item key={index} item={item} setTodos={setTodos} />
        ))
      ) : (
        <p>Il semble solitaire ici, que faites-vous ?</p>
      )}
    </ol>
  );
}
```

Maintenant, la prop todos sera peuplée par les données de notre état, et sans plus tarder, cela fonctionnera. Voici une image montrant la liste créée à partir de nos données todos :

![Image](https://lh7-us.googleusercontent.com/oqqO8NpZ3Mzdl2Ydc9MYlzYZPtvNstvVdB8hrjhF4hra41cwpSYNN0QwbsPCAi1cUDBGAR-lcPpso8sMdiAgzvU-JjHEV-Cn3FqvNkxqekulirAAGbrpDeGMwtSJyQGcqnydhvOqDSbjPgV3NpQYmM0 align="left")

*Une image montrant une liste de nos todos*

L'autre endroit où nous avons besoin des données est dans notre composant `TODOHero`. Nous n'avons pas besoin de toutes les données dans ce composant – nous avons juste besoin de compter le nombre total de todos et le nombre de todos terminées :

```jsx
// src/app/page.js

"use client";
import React from "react";
// importer d'autres composants
import TODOHero from "@/components/TODOHero";
import TODOList from "@/components/TODOList";
function Home() {
  const [todos, setTodos] = React.useState([
    { title: "Some task", id: self.crypto.randomUUID(), is_completed: false },
    // ajouter d'autres données factices
  ]);
  const todos_completed = todos.filter(
    (todo) => todo.is_completed === true
  ).length;
  const total_todos = todos.length;
  return (
    <div className="wrapper">
      <Header />
      <TODOHero todos_completed={todos_completed} total_todos={total_todos} />
      <Form />
      <TODOList todos={todos} />
    </div>
  );
}
export default Home;
```

Ici, la méthode JavaScript filter est utilisée pour filtrer toutes les todos avec `is_completed` défini sur true, puis nous obtenons la longueur. Le `total_todos` est simplement la longueur de l'ensemble du tableau.

Voici une image montrant le composant `TODOHero` avec des valeurs mises à jour :

![Image](https://lh7-us.googleusercontent.com/zDgqM8GZi9Wrr80GIWPFyq9D1kSOFXqZ4zDkKUTtWzayHnABJ7LYgvQi9xrukNEdJg2jbg7_Co07LfZJr7bsVFw1cytBN1INq5uv4AM87iHrn5B5KYtuY2wn2HRh0bMRu2PBLcNEoS8p1H_F5oS2kko align="left")

*Une image montrant le composant TODOHero mis à jour*

### Ajouter plus de données Todo à notre état

Actuellement, notre application todo affiche les todos à partir de nos données factices :

```js
const [todos, setTodos] = React.useState([
  { title: "Some task", id: self.crypto.randomUUID(), is_completed: false },
  {
    title: "Some other task",
    id: self.crypto.randomUUID(),
    is_completed: true,
  },
  { title: "last task", id: self.crypto.randomUUID(), is_completed: false },
]);
```

Mais le but de créer un composant Form était de nous permettre de créer de nouvelles todos nous-mêmes, et non de dépendre de données factices.

La bonne nouvelle est que, tout comme nous avons accès aux données d'état des todos, nous pouvons également mettre à jour l'état d'un parent à partir d'un composant enfant. Cela signifie que nous pouvons passer la fonction utilisée pour mettre à jour l'état, `setTodos`, à notre composant Form :

```js
// src/app/page.js

"use client";
import React from "react";
import Form from "@/components/Form";
// importer d'autres composants

function Home() {
  const [todos, setTodos] = React.useState([
    { title: "Some task", id: self.crypto.randomUUID(), is_completed: false },
    // ajouter d'autres données factices
  ]);

  ...
  return (
    <div className="wrapper">
      ...
      <Form setTodos={setTodos} />
      <TODOList todos={todos} />
    </div>
  );
}
export default Home;
```

Avec l'accès à la fonction `setTodos` dans notre composant Form, nous pouvons maintenant ajouter de nouvelles todos à notre état lorsque nous soumettons le formulaire :

```jsx
// src/components/Form.jsx

function Form({ setTodos }) {
  const handleSubmit = (event) => {
    event.preventDefault();
    const value = event.target.todo.value;
    setTodos((prevTodos) => [
      ...prevTodos,
      { title: value, id: self.crypto.randomUUID(), is_completed: false },
    ]);
    event.target.reset();
  };
  return (
    <form className="form" onSubmit={handleSubmit}>
      
    </form>
  );
}
export default Form;
```

L'extrait de code ci-dessous est là où la magie opère :

```js
setTodos((prevTodos) => [
  ...prevTodos,
  { title: value, id: self.crypto.randomUUID(), is_completed: false },
]);
```

Cela équivaut à faire ce qui suit en JavaScript simple :

```js
let prevTodos = [];

prevTodos.push({
  title: value,
  id: self.crypto.randomUUID(),
  is_completed: false,
});
```

Maintenant que nous pouvons ajouter de nouvelles todos à notre état nous-mêmes, nous pouvons nous débarrasser des données factices. Nous n'en avons plus besoin. Revenons à utiliser un tableau vide :

```js
const [todos, setTodos] = React.useState([]);
```

Maintenant que nous avons terminé avec la première partie, nous pouvons ajouter des todos comme nous le souhaitons. Voici une vidéo le démontrant :

%[https://youtu.be/bUqtCC8qBwI] 

## Comment construire la fonctionnalité de l'application TODO

### Comment marquer les todos comme terminées

Dans notre composant List, nous avons construit un élément `<li>` avec des boutons. Maintenant, nous allons attacher un gestionnaire d'événements `onClick` au premier bouton.

```jsx
// src/components/TODOList.jsx

function Item({ item }) {
  const completeTodo = () => {
    // effectuer une action
  };
  return (
    <li id={item?.id} className="todo_item" onClick={completeTodo}>
      <button className="todo_items_left">
        <svg>
          <circle cx="11.998" cy="11.998" fillRule="nonzero" r="9.998" />
        </svg>
        <p>{item?.title}</p>
      </button>
      <div className="todo_items_right">
        <button>...</button>
        <button>...</button>
      </div>
    </li>
  );
}
```

Lorsque nous cliquons sur ce bouton et que le gestionnaire completeTodo est invoqué, notre objectif est de :

* Filtrer les données pour trouver le todo qui a été cliqué.
    
* Modifier les données et définir la valeur `is_completed` sur true.
    

Avant de pouvoir procéder à la modification des données, nous avons besoin d'accès à la fonction `setTodo` dans notre composant `<Item />`. Heureusement, React permet à l'état d'être passé aux composants petits-enfants.

Cela signifie que nous pouvons passer la fonction `setTodo` du composant `<List />` à notre composant `<Item />` :

```jsx
// src/app/page.js

"use client";
import React from "react";
// importer d'autres composants
import TODOList from "@/components/TODOList";

function Home() {
  const [todos, setTodos] = React.useState([]);

...

  return (
    <div className="wrapper">
      ...
      <TODOList todos={todos} setTodos={setTodos} />
    </div>
  );
}
export default Home;
```

Ensuite, dans notre composant `<List />`, nous passons la fonction `setTodo` à notre composant `<Item />` :

```jsx
// src/components/TODOList.jsx

function TODOList({ todos, setTodos }) {
  return (
    <ol className="todo_list">
      {todos && todos.length > 0 ? (
        todos?.map((item, index) => (
          <Item key={index} item={item} setTodos={setTodos} />
        ))
      ) : (
        <p>Il semble solitaire ici, que faites-vous ?</p>
      )}
    </ol>
  );
}
```

Maintenant, dans notre composant `<Item />`, nous pouvons utiliser la fonction `setTodos` pour mettre à jour le statut `is_completed` du todo lorsque le bouton est cliqué :

```jsx
// src/components/TODOList.jsx

function Item({ item, setTodos }) {
  const completeTodo = () => {
    setTodos((prevTodos) =>
      prevTodos.map((todo) =>
        todo.id === item.id
          ? { ...todo, is_completed: !todo.is_completed }
          : todo
      )
    );
  };
  return (
    <li id={item?.id} className="todo_item">
      <button className="todo_items_left" onClick={completeTodo}>
        ...
      </button>
      <div className="todo_items_right">
        <button>...</button>
        <button>...</button>
      </div>
    </li>
  );
}
```

Maintenant, cliquer sur le premier bouton dans l'élément todo basculera son statut de complétion, modifiant effectivement les données todo.

Lorsque qu'un todo est marqué comme terminé, nous voulons améliorer sa représentation visuelle. Cela inclut l'ajout d'un remplissage au cercle SVG à côté du titre du todo, créant l'illusion que le todo est terminé. De plus, nous voulons ajouter un barré au texte pour signifier la complétion.

```js
<button className="todo_items_left" onClick={completeTodo}>
  <svg fill={item.is_completed ? "#22C55E" : "#0d0d0d"}>
    <circle cx="11.998" cy="11.998" fillRule="nonzero" r="9.998" />
  </svg>
  <p style={item.is_completed ? { textDecoration: "line-through" } : {}}>
    {item?.title}
  </p>
</button>;
```

Dans l'extrait de code ci-dessus, la couleur du bouton change en fonction de l'état de complétion de l'élément todo. Si l'élément est terminé (`is_completed` est vrai), le cercle SVG se remplit d'une couleur verte – sinon, il se remplit d'une couleur sombre. De plus, le texte du titre du todo reçoit un style de barré si le todo est terminé, indiquant visuellement sa complétion.

Et maintenant tout fonctionne parfaitement :

%[https://youtu.be/MJ57XGaOimI] 

### Comment modifier les todos

Lorsque nous modifions les todos, nous voulons avoir un formulaire dans lequel nous pouvons modifier le titre du todo. Lorsque le bouton de modification est cliqué, nous voulons remplacer tout le contenu dans le `<li>` et avoir un formulaire à la place :

```jsx
// src/components/TODOList.jsx

function Item({ item, setTodos }) {
  const [editing, setEditing] = React.useState(false);
  const inputRef = React.useRef(null);
  const completeTodo = () => {
    // marquer le todo comme terminé
  };
  const handleEdit = () => {
    setEditing(true);
  };
  React.useEffect(() => {
    if (editing && inputRef.current) {
      inputRef.current.focus();
      // positionner le curseur à la fin du texte
      inputRef.current.setSelectionRange(
        inputRef.current.value.length,
        inputRef.current.value.length
      );
    }
  }, [editing]);
  const handleInpuSubmit = (event) => {
    event.preventDefault();
    setEditing(false);
  };
  const handleInputBlur = () => {
    setEditing(false);
  };
  return (
    <li id={item?.id} className="todo_item">
      {editing ? (
        <form className="edit-form" onSubmit={handleInpuSubmit}>
          <label htmlFor="edit-todo">
            <input
              ref={inputRef}
              type="text"
              name="edit-todo"
              id="edit-todo"
              defaultValue={item?.title}
              onBlur={handleInputBlur}
              onChange={handleInputChange}
            />
          </label>
        </form>
      ) : (
        <>
          <button className="todo_items_left" onClick={completeTodo}>
            ...
          </button>
          <div className="todo_items_right">
            <button onClick={handleEdit}>...</button>
            <button>...</button>
          </div>
        </>
      )}
    </li>
  );
}
```

Je sais que le code ci-dessus est assez complexe. Eh bien, c'est parce que nous faisons beaucoup ici – mais la première chose que nous avons faite a été de créer un état :

```js
const [editing, setEditing] = React.useState(false);
```

Lorsque le bouton de modification est cliqué, nous définissons la valeur de notre état d'édition sur true, ce qui rendra notre formulaire :

```js
const handleEdit = () => {
  setEditing(true);
};
```

Maintenant, lorsque nous soumettons le formulaire de modification de todo en appuyant sur entrer, nous voulons également définir la variable sur false pour retrouver notre liste :

```js
const handleInpuSubmit = (event) => {
  event.preventDefault();
  setEditing(false);
};
```

Lorsque nous sortons du formulaire de modification avec la souris, nous voulons également définir l'état sur false :

```js
const handleInputBlur = () => {
  setEditing(false);
};
```

Une autre chose que nous voulons faire est de mettre le focus sur l'entrée une fois que l'édition est définie sur true :

```jsx
React.useEffect(() => {
  if (editing && inputRef.current) {
    inputRef.current.focus();
    // positionner le curseur à la fin du texte
    inputRef.current.setSelectionRange(
      inputRef.current.value.length,
      inputRef.current.value.length
    );
  }
}, [editing]);
```

Le formulaire de modification du todo lui-même a un seul champ de saisie avec un événement `onChange`. Lorsque nous modifions le titre dans le champ de saisie, nous voulons modifier le todo actuel avec le titre mis à jour :

```js
const handleInputChange = (e) => {
  setTodos((prevTodos) =>
    prevTodos.map((todo) =>
      todo.id === item.id ? { ...todo, title: e.target.value } : todo
    )
  );
};
```

La méthode JavaScript `array.map()` est parfaite pour cela car elle retourne un nouveau tableau avec le même nombre d'éléments après avoir modifié le titre.

Voici une vidéo de son fonctionnement sans accroc :

%[https://youtu.be/YRGq0SV7K_c] 

### Comment supprimer les todos

Supprimer des todos est un processus simple. Lorsque le bouton de suppression est cliqué, nous filtrons le todo qui a déclenché l'événement de suppression de la liste des todos.

```jsx
// src/components/TODOList.jsx

const handleDelete = () => {
  setTodos((prevTodos) => prevTodos.filter((todo) => todo.id !== item.id));
};
```

N'oubliez pas d'ajouter un événement onClick au bouton de suppression :

```jsx
// src/components/TODOList.jsx

function Item({ item, setTodos }) {
  ...
    const handleDelete = () => {
    setTodos((prevTodos) => prevTodos.filter((todo) => todo.id !== item.id));
  };
  return (
    <li id={item?.id} className="todo_item">
      {editing ? (
        <form className="edit-form" onSubmit={handleInpuSubmit}>
          ...
        </form>
      ) : (
        <>
          
          <div className="todo_items_right">
            
            <button onClick={handleDelete}>
              <span className="visually-hidden">Supprimer</span>
              <svg>
                <path d="" />
              </svg>
            </button>
          </div>
        </>
      )}
    </li>
  );
}
```

Et voilà ! Cela fonctionne comme un charme :

%[https://youtu.be/YMEmxMr1KEY] 

## Comment persister nos données Todo

Jusqu'à présent, nos données todo ont été stockées uniquement dans l'état de l'application :

```js
const [todos, setTodos] = React.useState([]);
```

Bien que cette approche fonctionne, elle présente un défi : lorsque l'application est rechargée, toutes les données todo sont perdues.

En ce qui concerne la persistance des données, nous pensons généralement aux bases de données. Stocker nos données todo dans une base de données offre plusieurs avantages, tels qu'un accès facile depuis n'importe quel appareil. Mais il existe une alternative : localStorage.

LocalStorage est un système de stockage basé sur le navigateur. Il a certaines limitations, comme une limite de stockage de 5 Mo et l'accessibilité des données restreinte au navigateur où elles sont stockées. Malgré ces inconvénients, nous utiliserons localStorage dans ce tutoriel pour des raisons de simplicité.

### Comment persister les données Todo dans localStorage

Actuellement, lorsque nous ajoutons un nouveau todo, nous mettons uniquement à jour l'état des todos dans notre composant Form :

```js
// src/components/Form.jsx

const handleSubmit = (event) => {
  event.preventDefault();
  const value = event.target.todo.value;
  setTodos((prevTodos) => [
    ...prevTodos,
    { title: value, id: self.crypto.randomUUID(), is_completed: false },
  ]);
  event.target.reset();
};
```

Nous voulons toujours garder cela, mais en même temps, nous voulons ajouter les mêmes données à localStorage, donc nous allons modifier le code ci-dessus pour qu'il ressemble à ceci :

```js
// src/components/Form.jsx 

const handleSubmit = (event) => {
  event.preventDefault();
  const value = event.target.todo.value;
  const newTodo = {
    title: value,
    id: self.crypto.randomUUID(),
    is_completed: false,
  };
  // Mettre à jour l'état des todos
  setTodos((prevTodos) => [...prevTodos, newTodo]);
  // Stocker la liste des todos mise à jour dans le stockage local
  const updatedTodoList = JSON.stringify([...todos, newTodo]);
  localStorage.setItem("todos", updatedTodoList);
  event.target.reset();
};
```

Ai-je mentionné que vous ne pouvez stocker que des chaînes de caractères dans localStorage ? Nous ne pouvons pas stocker un tableau ou un objet dans localStorage. C'est pourquoi nous convertissons d'abord notre tableau de données todo en une chaîne de caractères :

```js
const updatedTodoList = JSON.stringify([...prevTodos, newTodo]);
```

Et enfin, nous persistons les données dans localStorage avec ce code :

```js
localStorage.setItem('todos', updatedTodoList);
```

Vous remarquerez que nous avons utilisé nos données d'état `todos` dans notre composant `<Form />` :

```js
const updatedTodoList = JSON.stringify([...todos, newTodo]);
```

Alors n'oubliez pas de passer l'état des todos au composant :

```js
// src/app/page.js

<Form todos={todos} setTodos={setTodos} />
```

De plus, puisque nous pouvons modifier et supprimer des todos dans notre application, nous devons mettre à jour les données dans localStorage en conséquence. Tout d'abord, passez les données todos à notre composant `<Item />` :

```jsx
// src/components/TODOList.jsx

function TODOList({ todos, setTodos }) {
  return (
    <ol className="todo_list">
      {todos && todos.length > 0 ? (
        todos?.map((item, index) => (
        // passer les todos à <Item />
          <Item key={index} item={item} todos={todos} setTodos={setTodos} />
        ))
      ) : (
        <p>Il semble solitaire ici, que faites-vous ?</p>
      )}
    </ol>
  );
}
```

Maintenant que nous avons accès aux données todo dans notre composant `<Item />`, nous pouvons persister les données dans localStorage après avoir marqué le todo comme terminé :

```js
// src/components/TODOList.jsx

const completeTodo = () => {
  setTodos((prevTodos) =>
    prevTodos.map((todo) =>
      todo.id === item.id ? { ...todo, is_completed: !todo.is_completed } : todo
    )
  );

  // Mettre à jour localStorage après avoir marqué le todo comme terminé
  const updatedTodos = JSON.stringify(todos);
  localStorage.setItem("todos", updatedTodos);
};
```

Nous voulons également persister les données dans localStorage après avoir modifié un todo :

```js
// src/components/TODOList.jsx

const handleInpuSubmit = (event) => {
  event.preventDefault();

  // Mettre à jour localStorage après avoir modifié le todo
  const updatedTodos = JSON.stringify(todos);
  localStorage.setItem("todos", updatedTodos);
  setEditing(false);
};

const handleInputBlur = () => {
  // Mettre à jour localStorage après avoir modifié le todo
  const updatedTodos = JSON.stringify(todos);
  localStorage.setItem("todos", updatedTodos);

  setEditing(false);
};
```

Enfin, nous voulons également persister les données dans localStorage après avoir supprimé un todo :

```js
// src/components/TODOList.jsx

const handleDelete = () => {
  setTodos((prevTodos) => prevTodos.filter((todo) => todo.id !== item.id));
  // Mettre à jour localStorage après avoir supprimé le todo
  const updatedTodos = JSON.stringify(
    todos.filter((todo) => todo.id !== item.id)
  );
  localStorage.setItem("todos", updatedTodos);
};
```

Et c'est tout ce dont vous avez besoin – assez facile, non ? Maintenant, lorsque nous créons de nouveaux todos, ils seront persistés dans localStorage même après avoir rechargé notre application.

### Comment lire les données Todo depuis localStorage

Même si nous avons réussi à persister nos données dans localStorage, les données de notre application sont toujours effacées lorsque nous rechargeons notre application ou le navigateur. C'est parce que nous n'utilisons pas encore les données stockées dans localStorage.

Pour remédier à cela, lorsque notre application est montée (chargée), nous voulons récupérer les données de localStorage et les passer à notre état.

Dans notre fichier src/app/page.js, nous allons lire les données de localStorage et les stocker dans notre état todos.

```jsx
// src/app/page.js

"use client";
import React from "react";
import Form from "@/components/Form";
import Header from "@/components/Header";
import TODOHero from "@/components/TODOHero";
import TODOList from "@/components/TODOList";

function Home() {
  const [todos, setTodos] = React.useState([]);

  // Récupérer les données de localStorage lorsque le composant est monté
  React.useEffect(() => {
    const storedTodos = localStorage.getItem("todos");
    if (storedTodos) {
      setTodos(JSON.parse(storedTodos));
    }
  }, []);

  const todos_completed = todos.filter(
    (todo) => todo.is_completed == true
  ).length;
  const total_todos = todos.length;

  return (
    <div className="wrapper">
      <Header />
      <TODOHero todos_completed={todos_completed} total_todos={total_todos} />
      <Form todos={todos} setTodos={setTodos} />
      <TODOList todos={todos} setTodos={setTodos} />
    </div>
  );
}

export default Home;
```

Le code à l'intérieur du hook `useEffect()` que nous exécutons une fois que le composant est monté.

C'est la partie qui lit les données de localStorage :

```js
const storedTodos = localStorage.getItem("todos");
```

Puisque les données stockées dans localStorage sont une chaîne de caractères, nous devons les convertir en notre tableau d'objets avant de pouvoir les utiliser :

```js
JSON.parse(storedTodos)
```

Et c'est tout ce dont vous avez besoin pour que cela fonctionne. Maintenant, même lorsque nous rechargeons l'application, les données sont persistées comme vous pouvez le voir dans cette vidéo :

%[https://youtu.be/008u_QJZBAs] 

## Et nous l'avons fait.

Félicitations ! Après un voyage rempli de codage et de persévérance, nous avons réussi à construire une application todo simple mais fonctionnelle à partir de zéro. Le voyage a peut-être été long, mais le résultat en vaut la peine.

Vous pouvez explorer le code source complet de l'application [ici](https://github.com/iamspruce/create-a-todo-app-with-React). N'hésitez pas à plonger dans le code et à voir comment tout s'assemble.

Mais attendez, il y a plus ! Si vous êtes impatient d'essayer l'application vous-même, j'ai une version hébergée disponible [ici](https://create-a-todo-app-with-react.vercel.app/). Allez-y et essayez-la pour vivre l'expérience de l'application en direct.

Merci de m'avoir accompagné dans cette aventure de codage. J'espère que vous avez acquis des connaissances précieuses sur la construction d'applications React et la persistance des données avec localStorage.

Si vous avez des questions, n'hésitez pas à m'envoyer un message sur Twitter à [@sprucekhalifa](https://twitter.com/sprucekhalifa), et n'oubliez pas de me suivre pour plus d'informations et de mises à jour. Bon codage !