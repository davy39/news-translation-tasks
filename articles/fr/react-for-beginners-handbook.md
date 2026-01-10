---
title: Apprendre React – Un Guide pour Débutants
subtitle: ''
author: Nathan Sebhastian
co_authors: []
series: null
date: '2024-03-01T00:34:46.000Z'
originalURL: https://freecodecamp.org/news/react-for-beginners-handbook
coverImage: https://www.freecodecamp.org/news/content/images/2024/03/Learn-React-Cover.png
tags:
- name: beginner
  slug: beginner
- name: handbook
  slug: handbook
- name: React
  slug: react
seo_title: Apprendre React – Un Guide pour Débutants
seo_desc: 'The goal of this handbook is to provide gentle step-by-step instructions
  that will help you learn the key concepts of React.

  Instead of covering all the theories and concepts of React in their entirety, I''ll
  be teaching you important building blocks ...'
---

L'objectif de ce guide est de fournir des instructions étape par étape qui vous aideront à apprendre les concepts clés de React.

Au lieu de couvrir toutes les théories et concepts de React dans leur intégralité, je vais vous enseigner les éléments de base importants de la bibliothèque. Vous apprendrez à propos de JSX, des composants, des props, des états, des gestionnaires d'événements, de la création de formulaires et de l'exécution de requêtes réseau.

## Table des Matières

- [Exigences](#heading-exigences)
- [Chapitre 1 : Introduction](#heading-chapitre-1-introduction)
  - [Installation de l'Ordinateur](#heading-installation-de-lordinateur)
  - [Votre Première Application React](#heading-votre-premiere-application-react)
  - [Explication du Code Source](#heading-explication-du-code-source)
- [Chapitre 2 : Comment Créer des Composants React](#heading-chapitre-2-comment-creer-des-composants-react)
  - [Comment Retourner Plusieurs Éléments avec des Fragments](#heading-comment-retourner-plusieurs-elements-avec-des-fragments)
  - [Comment Rendre à l'Écran](#heading-comment-rendre-a-lecran)
  - [Comment Écrire des Commentaires dans React](#heading-comment-ecrire-des-commentaires-dans-react)
  - [Comment Composer Plusieurs Composants en Un](#heading-comment-composer-plusieurs-composants-en-un)
- [Chapitre 3 : Comprendre JSX](#heading-chapitre-3-comprendre-jsx)
  - [Comment Rendre une Liste en Utilisant JSX](#heading-comment-rendre-une-liste-en-utilisant-jsx)
  - [Comment Ajouter l'Attribut Class](#heading-comment-ajouter-lattribut-class)
- [Chapitre 4 : Props et États](#heading-chapitre-4-props-et-etats)
  - [Comment Passer Plusieurs Props](#heading-comment-passer-plusieurs-props)
  - [Les Props sont Immuables](#heading-les-props-sont-immuables)
  - [État dans React](#heading-etat-dans-react)
  - [Comment Passer l'État à un Composant Enfant](#heading-comment-passer-letat-a-un-composant-enfant)
  - [Comment Utiliser React DevTools pour Inspecter les États et les Props](#heading-comment-utiliser-react-devtools-pour-inspecter-les-etats-et-les-props)
- [Chapitre 5 : Rendu Conditionnel dans React](#heading-chapitre-5-rendu-conditionnel-dans-react)
  - [Rendu Partiel avec une Variable Régulière](#heading-rendu-partiel-avec-une-variable-reguliere)
  - [Rendu Inline avec l'Opérateur &&](#heading-rendu-inline-avec-loperateur-et)
  - [Rendu Inline avec l'Opérateur Conditionnel (Ternaire)](#heading-rendu-inline-avec-loperateur-conditionnel-ternaire)
- [Chapitre 6 : Comment Gérer les Événements Utilisateur](#heading-chapitre-6-comment-gerer-les-evenements-utilisateur)
  - [Comment Changer l'UI en Gérant les Événements](#heading-comment-changer-lui-en-gerant-les-evenements)
- [Chapitre 7 : CSS dans React](#heading-chapitre-7-css-dans-react)
  - [Style Inline React](#heading-style-inline-react)
  - [Fichiers CSS](#heading-fichiers-css)
  - [Modules CSS](#heading-modules-css)
  - [Tailwind CSS](#heading-tailwind-css)
  - [Lequel Devez-Vous Utiliser ?](#heading-lequel-devez-vous-utiliser)
- [Chapitre 8 : Comment Construire des Formulaires dans React](#heading-chapitre-8-comment-construire-des-formulaires-dans-react)
  - [Comment Gérer l'Entrée de Formulaire](#heading-comment-gerer-lentree-de-formulaire)
  - [Comment Gérer la Soumission de Formulaire](#heading-comment-gerer-la-soumission-de-formulaire)
  - [Comment Gérer la Validation de Formulaire](#heading-comment-gerer-la-validation-de-formulaire)
- [Chapitre 9 : Requêtes Réseau dans React](#heading-chapitre-9-requetes-reseau-dans-react)
  - [Le Hook useEffect](#heading-le-hook-useeffect)
- [Conclusion](#heading-conclusion)

En couvrant ces concepts, vous serez équipé pour plonger plus profondément dans les sujets avancés de React.

## Exigences

Pour tirer pleinement parti de ce guide, vous devez avoir des connaissances de base en HTML, CSS et JavaScript. Aucune connaissance préalable de React n'est nécessaire, car nous commencerons par les bases.

Si vous avez besoin d'un rappel sur JavaScript, vous pouvez [obtenir mon livre sur JavaScript ici](https://codewithnathan.com/beginning-modern-javascript).

## Chapitre 1 : Introduction

React est une bibliothèque front-end JavaScript très populaire. Elle a reçu beaucoup d'amour de la part des développeurs du monde entier pour sa **simplicité** et ses **performances rapides**.

React a été initialement développé par Facebook comme solution aux problèmes front-end auxquels ils étaient confrontés :

* La manipulation du DOM est une opération coûteuse et doit être minimisée
* Aucune bibliothèque spécialisée dans le développement front-end à l'époque (il y a Angular, mais c'est un FRAMEWORK ENTIER.)
* L'utilisation de beaucoup de JavaScript vanilla peut transformer une application web en un désordre difficile à maintenir.

Pourquoi les développeurs aiment-ils React ? En tant que développeur logiciel moi-même, je peux penser à quelques raisons pour lesquelles je l'aime :

* **Il est minimaliste**. React ne s'occupe que d'UNE seule chose : l'interface utilisateur et comment elle change en fonction des données que vous lui fournissez. React rend votre interface dynamique avec un code minimal.
* **Il a une courbe d'apprentissage faible**. Les concepts de base de React sont relativement faciles à apprendre, et vous n'avez pas besoin de mois ou de 40 heures de cours vidéo pour apprendre les bases.
* **Il est non opinionné**. React peut être intégré avec de nombreuses technologies différentes. Sur le front-end, vous pouvez utiliser différentes bibliothèques pour gérer les appels Ajax (Axios, Superagent, ou simplement Fetch). Sur le back-end, vous pouvez utiliser PHP/Ruby/Go/Python ou tout autre langage que vous préférez.
* **Il bénéficie d'un fort soutien communautaire**. Pour améliorer les capacités de React, les contributeurs open source ont construit un écosystème incroyable de bibliothèques qui vous permettent de créer des applications encore plus puissantes. Mais la plupart des bibliothèques open source pour React sont optionnelles. Vous n'avez pas besoin de les apprendre jusqu'à ce que vous ayez maîtrisé les fondamentaux de React.

En résumé, avec une courbe d'apprentissage faible, React vous donne un pouvoir incroyable pour rendre votre UI flexible, réutilisable et sans spaghetti.

Apprendre React ouvre des opportunités considérables si vous souhaitez travailler en tant que développeur web.

### Installation de l'Ordinateur

Pour commencer à programmer avec React, vous aurez besoin de trois choses :

1. Un navigateur web
2. Un éditeur de code
3. Node.js

Nous allons utiliser le navigateur Chrome pour exécuter notre code JavaScript, donc si vous ne l'avez pas, [vous pouvez le télécharger ici](https://www.google.com/chrome/).

Le navigateur est disponible pour tous les systèmes d'exploitation majeurs. Une fois le téléchargement terminé, installez le navigateur sur votre ordinateur.

Ensuite, vous devrez installer un éditeur de code si vous n'en avez pas déjà un. Il existe plusieurs éditeurs de code gratuits disponibles sur Internet, tels que Sublime Text, Visual Studio Code et Notepad++.

Parmi ces éditeurs, mon préféré est Visual Studio Code, car il est rapide et facile à utiliser.

#### Comment installer Visual Studio Code

Visual Studio Code, ou VSCode en abrégé, est une application créée dans le but d'écrire du code. En plus d'être gratuit, VSCode est rapide et disponible sur tous les systèmes d'exploitation majeurs.

Vous pouvez [télécharger Visual Studio Code ici](https://code.visualstudio.com/).

Lorsque vous ouvrez le lien ci-dessus, il devrait y avoir un bouton montrant la version compatible avec votre système d'exploitation comme indiqué ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2024/02/1-installvscode-2.png)
_Téléchargement de Visual Studio Code_

Cliquez sur le bouton pour télécharger VSCode, et installez-le sur votre ordinateur.

Maintenant que vous avez un éditeur de code installé, l'étape suivante est d'installer Node.js

#### Comment installer Node.js

Node.js est une application d'exécution JavaScript qui vous permet d'exécuter JavaScript en dehors du navigateur. Vous devez installer cette application sur votre ordinateur pour installer les packages requis dans le développement React.

Vous pouvez télécharger et installer Node.js depuis [https://nodejs.org](https://nodejs.org/). Choisissez la version LTS recommandée car elle bénéficie d'un support à long terme. Le processus d'installation est assez simple.

Pour vérifier si Node a été correctement installé, tapez la commande suivante sur votre ligne de commande (Invite de commandes sur Windows ou Terminal sur Mac) :

```sh
node -v

```

La ligne de commande devrait répondre avec la version de Node.js que vous avez sur votre ordinateur.

### Votre Première Application React

Il est temps d'exécuter votre première application React. Tout d'abord, créez un dossier sur votre ordinateur qui sera utilisé pour stocker tous les fichiers liés à ce livre. Vous pouvez nommer le dossier 'beginning_react'.

L'étape suivante consiste à ouvrir votre terminal et à exécuter la commande npm pour créer une nouvelle application React en utilisant Vite.

Vite (prononcé 'veet') est un outil de construction que vous pouvez utiliser pour démarrer un nouveau projet React. Dans le dossier 'beginning_react', vous devez exécuter la commande suivante pour créer un nouveau projet React avec Vite :

```sh
npm create vite@5.1.0 my-react-app -- --template react

```

Vous devriez voir npm demander à installer un nouveau package (create-vite) comme indiqué ci-dessous. Procédez en tapant 'y' et en appuyant sur Entrée :

```txt
Need to install the following packages:
  create-vite@5.1.0
Ok to proceed? (y) y

```

Ensuite, Vite créera un nouveau projet React nommé 'my-react-app' comme suit :

```txt
Scaffolding project in /dev/beginning_react/my-react-app...

Done. Now run:

  cd my-react-app
  npm install
  npm run dev

```

Lorsque vous avez terminé, suivez les étapes suivantes que vous voyez dans la sortie ci-dessus. Utilisez la commande `cd` pour changer le répertoire de travail vers l'application que vous venez de créer, puis exécutez `npm install` pour installer les packages requis par l'application.

Ensuite, vous devez exécuter la commande `npm run dev` pour démarrer votre application :

```txt
$ npm run dev

> my-react-app@0.0.0 dev
> vite


  VITE v5.0.10  ready in 509 ms

  ➜  Local:   http://localhost:5173/
  ➜  Network: use --host to expose
  ➜  press h + enter to show help

```

Maintenant, vous pouvez voir l'application en cours d'exécution depuis le navigateur, à l'adresse localhost désignée :

![Image](https://www.freecodecamp.org/news/content/images/2024/02/1-vite-react-demo.png)
_Page d'Accueil Vite-React_

Cela signifie que vous avez créé avec succès votre première application React. Félicitations !

### Explication du Code Source

Maintenant que vous avez exécuté avec succès une application React, examinons le code source généré par Vite pour comprendre comment les choses fonctionnent.

Exécutez Visual Studio Code que vous avez installé dans la section précédente, et ouvrez le dossier 'my-react-app' dans VSCode.

Ici, vous devriez voir plusieurs dossiers et fichiers qui composent l'application React comme suit :

![Image](https://www.freecodecamp.org/news/content/images/2024/02/1-vite-react-app.png)
_Structure de l'Application Vite-React_

Le fichier `vite.config.js` est un fichier de configuration qui indique à Vite comment exécuter l'application. Comme nous avons une application React, vous verrez le plugin React importé à l'intérieur :

```js
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
})

```

Lorsque vous exécutez la commande `npm run dev`, Vite recherchera ce fichier pour savoir comment exécuter le programme.

Le fichier `package.json` stocke les informations sur le projet, y compris les packages requis pour exécuter le projet sans aucun problème. Le fichier `package-lock.json` suit les versions des packages installés.

Le fichier `.eslintrc.cjs` contient les règles ESLint. ESLint est un outil d'analyse de code qui peut identifier le code problématique dans votre projet sans avoir besoin d'exécuter le projet. Il signalera toute erreur et avertissement dans VSCode.

Le fichier `index.html` est un document HTML statique qui sera utilisé lors de l'exécution de l'application React, et le fichier `README.md` contient une introduction au projet.

Vous n'avez pas besoin de modifier l'un de ces fichiers. Au lieu de cela, allons dans le dossier `src/` où le code de l'application React est écrit.

```txt
src
├── App.css
├── App.jsx
├── assets
│   └── react.svg
├── index.css
└── main.jsx

```

Tout d'abord, le fichier `App.css` contient les règles CSS appliquées au fichier `App.jsx`, qui est le code principal de l'application React.

Le dossier `assets/` contient les ressources nécessaires pour ce projet. Dans ce cas, il s'agit de l'icône React, que vous avez vue dans le navigateur.

Le fichier `index.css` est le fichier CSS racine appliqué globalement à l'application, et le fichier `main.jsx` est le fichier racine qui accède au fichier `index.html` pour rendre l'application React. Voici le contenu du fichier `main.jsx` :

```jsx
import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import './index.css'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)

```

Ici, vous pouvez voir que la bibliothèque ReactDOM crée une racine à l'élément `<div>` qui contient l'ID `root`, puis rend toute l'application React à cet élément.

Vous pouvez ouvrir le fichier `App.jsx` pour voir le code React :

```jsx
import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <div>
        <a href="https://vitejs.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Vite + React</h1>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
        <p>
          Edit <code>src/App.jsx</code> and save to test HMR
        </p>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </>
  )
}

export default App

```

Dans ce fichier, un seul composant nommé `App` est défini. Les logos Vite et React sont rendus avec un lien vers la bibliothèque respective, et il y a un bouton de compteur qui incrémentera le compteur de 1 lorsque vous cliquerez dessus.

Ce fichier est celui où nous explorerons les fondamentaux de React. Supprimons tout dans ce fichier, et écrivons un simple composant `App` qui rend un élément `<h1>` :

```jsx
function App() {
  return <h1>Hello World</h1>
}

export default App

```

Ensuite, supprimez le fichier `index.css`, `app.css`, et le dossier `assets/`. Vous devez également supprimer l'instruction `import './index.css'` dans votre fichier `main.jsx`.

Si vous ouvrez à nouveau le navigateur, vous devriez voir un seul en-tête rendu comme suit :

![Image](https://www.freecodecamp.org/news/content/images/2024/02/1-react-hello-world.png)
_Sortie React des Modifications de Code_

D'accord ! Maintenant, vous êtes prêt à apprendre les fondamentaux de React. Nous commencerons votre première leçon dans le chapitre suivant.

## Chapitre 2 : Comment Créer des Composants React

Dans React, un composant est une unité indépendante unique d'une interface utilisateur (UI). Ce que vous écrivez à l'intérieur d'un composant déterminera ce qui doit apparaître à l'écran du navigateur à un moment donné.

Dans le chapitre précédent, nous avons créé un composant `App` qui retourne un élément d'en-tête :

```jsx
function App() {
  return <h1>Hello World</h1>
}

export default App

```

Un composant est composé d'une fonction qui retourne un seul élément d'UI.

Lorsque vous voulez qu'un composant ne rende rien, vous pouvez retourner un `null` ou `false` au lieu d'un élément.

```jsx
function App() {
  return null
}

```

Tous les composants React sont enregistrés sous l'extension de fichier `.jsx`. Comme vous pouvez le voir dans ce projet, vous avez `main.jsx` et `App.jsx`.

Qu'est-ce que JSX ? C'est une extension de JavaScript qui produit des éléments HTML alimentés par JavaScript. Nous allons en apprendre davantage plus tard.

### Comment Retourner Plusieurs Éléments avec des Fragments

Un composant doit toujours retourner un seul élément. Lorsque vous devez retourner plusieurs éléments, vous devez les envelopper tous dans un seul élément comme un `<div>` :

```jsx
function App() {
  return (
    <div>
      <h1>Hello World!</h1>
      <h2>Learning to code with React</h2>
    </div>
  )
}

export default App

```

Mais cela fera en sorte que votre application rende un élément `<div>` supplémentaire dans le navigateur. Pour éviter d'encombrer votre application, vous pouvez rendre une balise vide `<>` comme ceci :

```jsx
function App() {
  return (
    <>
      <h1>Hello World!</h1>
      <h2>Learning to code with React</h2>
    </>
  )
}

export default App

```

La balise vide ci-dessus est une fonctionnalité React appelée un Fragment. En utilisant un Fragment, votre composant ne rendra pas d'élément supplémentaire à l'écran.

Vous pouvez également importer le module `Fragment` depuis React pour le rendre explicite comme suit :

```jsx
import { Fragment } from 'react';

function App() {
  return (
    <Fragment>
      <h1>Hello World!</h1>
      <h2>Learning to code with React</h2>
    </Fragment>
  )
}

export default App

```

Mais vous n'avez pas besoin de déclarer explicitement la balise `Fragment`. Utiliser une balise vide `<>` est suffisant.

### Comment Rendre à l'Écran

Pour rendre un composant React dans le navigateur, vous devez créer un composant racine React en utilisant la bibliothèque ReactDOM, que vous avez vue précédemment lors de la visualisation du fichier `main.jsx`.

Vous devez avoir un fichier HTML comme source à partir duquel votre composant React est rendu.

Habituellement, un document HTML très basique avec un `<div>` est suffisant, comme vous pouvez le voir dans le fichier `index.html` :

```html
<body>
  <div id="root"></div>
  <script type="module" src="/src/main.jsx"></script>
</body>

```

Ensuite, vous rendez le composant dans l'élément `<div>`.

Remarquez comment ReactDOM est importé depuis le package `react-dom`, et comment `document.getElementById('root')` est utilisé pour sélectionner l'élément `<div>` ci-dessous :

```jsx
import React from 'react'
import ReactDOM from 'react-dom/client'

function App() {
  return <h1>Hello World!</h1>
}

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)

```

Ici, vous pouvez voir que le composant `App` est placé dans le même fichier que la bibliothèque ReactDOM. Vous pouvez faire cela si vous voulez supprimer le fichier `App.jsx`, afin d'avoir uniquement un seul fichier `main.jsx` comme source pour votre application React.

Mais il est confus d'avoir plusieurs composants dans un seul fichier, alors ne faisons pas cela.

### Comment Écrire des Commentaires dans React

Écrire des commentaires dans les composants React est similaire à la façon dont vous commentez dans le code JavaScript régulier. Vous pouvez utiliser la syntaxe double barre oblique `//` pour commenter tout code.

L'exemple suivant montre comment commenter l'instruction `export` :

```jsx
function App() {
  return (
    <>
      <h1>Hello World!</h1>
      <h2>Learning to code with React</h2>
    </>
  )
}

// export default App

```

Lorsque vous voulez commenter le code à l'intérieur de l'instruction `return`, vous devez utiliser le format avec des accolades, une barre oblique et un astérisque `{/* comment here */}` comme montré ci-dessous :

```jsx
function App() {
  return (
    <>
      <h1>Hello World!</h1>
      {/* <h2>Learning to code with React</h2> */}
    </>
  )
}

```

Il peut sembler très ennuyeux que vous deviez vous souvenir de deux façons différentes de commenter lors de l'écriture d'applications React. Mais ne vous inquiétez pas, car un outil moderne comme VSCode sait comment générer la bonne syntaxe de commentaire.

Vous n'avez besoin que de presser le raccourci de commentaire, qui est `CTRL + /` pour Windows/Linux ou `Command + /` pour macOS.

### Comment Composer Plusieurs Composants en Un

Jusqu'à présent, vous n'avez rendu qu'un seul composant `App` dans le navigateur. Mais les applications construites avec React peuvent être composées de dizaines ou de centaines de composants.

**Composer des composants** est le processus de formation de l'interface utilisateur en utilisant des composants faiblement couplés. C'est un peu comme construire une maison avec des blocs Lego, comme je vais vous le montrer dans l'exemple suivant :

```jsx
export default function ParentComponent() {
  return (
    <>
      <UserComponent />
      <ProfileComponent />
      <FeedComponent />
    </>
  );
}

function UserComponent() {
  return <h1> User Component </h1>;
}

function ProfileComponent() {
  return <h1> Profile Component </h1>;
}

function FeedComponent() {
  return <h1> Feed Component</h1>;
}

```

Dans l'exemple ci-dessus, vous pouvez voir comment le `<ParentComponent>` rend trois composants enfants :

* `<UserComponent>`
* `<ProfileComponent>`
* `<FeedComponent>`

La composition de plusieurs composants formera un seul arbre de composants React dans une approche de haut en bas.

L'arbre sera ensuite rendu dans le DOM via la méthode `ReactDOM.render()` :

![Image](https://www.freecodecamp.org/news/content/images/2024/02/2-react-tree.png)
_Arbre de Composants React Illustré_

En composant plusieurs composants, vous pouvez diviser l'interface utilisateur en pièces indépendantes et réutilisables, et développer chaque pièce en isolation.

## Chapitre 3 : Comprendre JSX

Dans le chapitre précédent, vous avez appris qu'un composant doit toujours avoir une instruction `return` qui contient des éléments à rendre à l'écran :

```jsx
function App() {
  return <h1>Hello World</h1>
}

```

La balise `<h1>` ressemble à une balise HTML régulière, mais il s'agit en réalité d'un langage de modèle spécial inclus dans React appelé JSX.

JSX est une extension de syntaxe qui produit des éléments HTML alimentés par JavaScript. Il peut être assigné à des variables JavaScript et peut être retourné par des appels de fonction. Par exemple :

```jsx
function App() {
  const myElement = <h1>Hello World</h1>
  return myElement
}

```

Grâce à JSX, vous pouvez également intégrer des expressions JavaScript à l'intérieur d'un élément en utilisant des accolades `{}` :

```jsx
const lowercaseClass = 'text-lowercase';
const text = 'Hello World!';
const App = <h1 className={lowercaseClass}>{text}</h1>;

```

C'est ce qui rend les éléments React différents des éléments HTML. Vous ne pouvez pas intégrer JavaScript directement en utilisant des accolades en HTML.

Au lieu de créer un tout nouveau langage de modélisation, vous devez simplement utiliser des fonctions JavaScript pour contrôler ce qui est affiché à l'écran.

### Comment Rendre une Liste en Utilisant JSX

Par exemple, supposons que vous avez un tableau d'utilisateurs que vous souhaitez afficher :

```jsx
const users = [
  { id: 1, name: 'Nathan', role: 'Web Developer' },
  { id: 2, name: 'John', role: 'Web Designer' },
  { id: 3, name: 'Jane', role: 'Team Leader' },
]

```

Vous pouvez utiliser la fonction `map()` pour parcourir le tableau :

```jsx
function App() {
  const users = [
    { id: 1, name: 'Nathan', role: 'Web Developer' },
    { id: 2, name: 'John', role: 'Web Designer' },
    { id: 3, name: 'Jane', role: 'Team Leader' },
  ]

  return (
    <>
      <p>The currently active users list:</p>
      <ul>
      {
        users.map(function(user){
          // returns Nathan, then John, then Jane
          return (
            <li> {user.name} as the {user.role} </li>
          )
        })
      }
      </ul>
    </>
  )
}

```

Dans React, vous n'avez pas besoin de stocker la valeur de retour de la fonction `map()` dans une variable. L'exemple ci-dessus retournera un élément `<li>` pour chaque valeur de tableau dans le composant.

Bien que le code ci-dessus soit déjà complet, React déclenchera une erreur dans la console, indiquant que vous devez mettre une "clé" prop dans chaque enfant d'une liste (l'élément que vous retournez depuis la fonction `map()`) :

![Image](https://www.freecodecamp.org/news/content/images/2024/02/3-react-array-warning.png)
_Avertissement 'key' de React sur la Console du Navigateur_

Une prop (abréviation de propriété) est une entrée que vous pouvez passer à un composant lors du rendu de ce composant. La prop `key` est une prop spéciale que React utilisera pour déterminer quel élément enfant a été changé, ajouté ou supprimé de la liste.

Vous ne l'utiliserez pas activement dans aucune partie de votre code de rendu de tableau, mais React en demandera une lorsque vous rendrez une liste.

Il est recommandé de mettre l'identifiant unique de vos données comme valeur de clé. Dans l'exemple ci-dessus, vous pouvez utiliser les données `user.id`. Voici comment vous passez une prop `key` pour chaque élément `<li>` :

```jsx
return (
  <li key={user.id}> 
    {user.name} as the {user.role} 
  </li>
)

```

Lorsque vous n'avez aucun identifiant unique pour votre liste, vous pouvez utiliser la valeur d'`index` du tableau comme dernier recours :

```jsx
users.map(function(user, index){
  return (
    <li key={index}>
      {user.name} as the {user.role}
    </li>
  )
})

```

Les props sont l'un des ingrédients qui rendent un composant React puissant. Vous allez en apprendre davantage à leur sujet dans le chapitre suivant.

### Comment Ajouter l'Attribut Class

Vous pouvez ajouter l'attribut `class` à vos éléments en utilisant le mot-clé `className` :

```jsx
function App() {
  return <h1 className='text-lowercase'>Hello World!</h1>
}

```

Le mot-clé `class` est réservé pour les classes JavaScript, vous devez donc utiliser `className` à la place.

## Chapitre 4 : Props et États

Les props et les états sont utilisés pour passer des données à l'intérieur des composants React. Les props (ou propriétés) sont des entrées transmises d'un composant parent à son composant enfant.

D'autre part, les états sont des variables définies et gérées à l'intérieur des composants.

Commençons par comprendre les props. Supposons que vous avez un `ParentComponent` qui rend un `ChildComponent` comme ceci :

```jsx
function ParentComponent() {
  return <ChildComponent />
}

```

Vous pouvez passer une prop de `ParentComponent` à `ChildComponent` en ajoutant un nouvel attribut après le nom du composant.

Dans le code ci-dessous, la prop `name` avec la valeur 'John' est passée au `ChildComponent` :

```jsx
function ParentComponent() {
  return <ChildComponent name='John' />
}

```

Lorsque le composant est rendu dans le navigateur, le `ChildComponent` recevra la prop name dans le composant.

Vous pouvez accéder à l'objet `props` en le définissant dans l'argument de la fonction composant :

```jsx
function ChildComponent(props){
  return <p>Hello World! my name is {props.name}</p>
}

```

Le paramètre `props` sera toujours un objet, et toute prop que vous définissez lors du rendu du composant sera passée en tant que propriété à l'objet.

### Comment Passer Plusieurs Props

Vous pouvez passer autant de props que vous le souhaitez dans un seul composant enfant. Il suffit d'ajouter les props lors de l'utilisation du composant comme montré ci-dessous :

```jsx
function ParentComponent() {
  return (
    <ChildComponent
      name="John"
      age={29}
      hobbies={["read books", "drink coffee"]}
      occupation="Software Engineer"
    />
  )
}

```

Toutes les props ci-dessus seront passées au paramètre `props` du ChildComponent.

Vous pouvez même passer une fonction dans les props comme ceci :

```jsx
function ParentComponent() {
  function greetings() {
    return 'Hello World'
  }

  return <ChildComponent greetings={greetings} />
}

```

Dans le composant enfant, vous pouvez appeler la fonction comme suit :

```jsx
function ChildComponent(props) {
  return <p>{props.greetings()}</p>
}

```

Notez que si vous passez autre chose qu'une chaîne de caractères comme valeur de prop, vous devez mettre la valeur entre accolades (nombres, fonctions, tableaux, objets, etc.)

C'est parce que les expressions JavaScript ne peuvent pas être traitées par JSX à moins que vous ne mettiez l'expression entre accolades.

### Les Props sont Immuables

Immuable signifie qu'une valeur de prop ne peut pas être changée quoi qu'il arrive.

Dans le code ci-dessous, le `ChildComponent` essaie de changer la valeur de la propriété `props.name` :

```jsx
function ChildComponent(props){
  props.name = 'Mark';
  return <p>Hello World! my name is {props.name}</p>
}

function ParentComponent() {
  return <ChildComponent name='John'/>
}

export default ParentComponent

```

Mais vous obtiendrez une erreur dans la console comme suit :

```txt
Uncaught TypeError: Cannot assign to read only property 'name' of object '#<Object>'

```

Comme vous pouvez le voir, les props de React ne peuvent pas être changées une fois que vous les avez déclarées. Mais que faire si vos données doivent changer lorsque l'utilisateur interagit avec votre application ? C'est là que l'état vient à la rescousse.

### État dans React

Dans React, les états sont des données arbitraires que vous pouvez déclarer et gérer dans vos composants. Pour créer un état dans React, vous devez appeler le hook `useState` comme montré ci-dessous :

```jsx
import { useState } from 'react'

function ParentComponent() {
  const [name, setName] = useState('John')

}

export default ParentComponent

```

Dans React, les hooks sont des fonctions qui vous permettent de tirer parti des fonctionnalités fournies par React. Le hook `useState` est une fonction qui vous permet de mettre une valeur dans le mécanisme d'état.

Lorsque vous appelez la fonction `useState()`, vous pouvez passer un argument qui servira de valeur initiale de l'état. La fonction retourne ensuite un tableau avec deux éléments.

Le premier élément contient la valeur de l'état, et le second élément est une fonction qui vous permet de changer la valeur de l'état. Vous devez utiliser la syntaxe de tableau de déstructuration pour recevoir les deux éléments comme montré ci-dessus

Vous pouvez donner n'importe quels noms aux variables retournées par `useState`, mais il est recommandé d'utiliser `[something, setSomething]`.

Pour rendre la valeur de l'état, vous pouvez l'intégrer dans JSX comme suit :

```jsx
function ParentComponent() {
  const [name, setName] = useState('John')

  return <h1>Hello {name}</h1>
}

```

Si vous voulez changer la valeur de la variable `name`, vous devez utiliser la fonction `setName()` fournie.

Mais vous ne pouvez pas appeler `setName()` dans le corps du composant, car React se rafraîchira chaque fois que vous changerez la valeur de l'état.

Au lieu de cela, vous pouvez créer un bouton qui changera la valeur de name lorsque vous cliquerez dessus :

```jsx
function ParentComponent() {
  const [name, setName] = useState('John')

  return (
    <>
      <h1>Hello {name}</h1>
      <button onClick={() => setName('Mark')}>Change Name</button>
    </>
  )
}

```

Dans le code ci-dessus, nous créons un élément `<button>` et ajoutons la prop `onClick`, qui s'exécute chaque fois que nous cliquons sur le bouton.

À l'intérieur de la prop, nous passons une fonction qui appelle simplement la fonction `setName()`, changeant la valeur de l'état.

### Comment Passer l'État à un Composant Enfant

Vous pouvez passer l'état à n'importe quel composant enfant. Lorsque vous devez mettre à jour l'état depuis un composant enfant, vous devez passer la fonction `setSomething` reçue du hook `useState`.

Voici un exemple de passage d'un état de `ParentComponent` à `ChildComponent` :

```jsx
function ParentComponent() {
  const [name, setName] = useState('John')

  return <ChildComponent name={name} setName={setName} />
}

```

Dans le `ChildComponent`, vous pouvez appeler la fonction `setName()` depuis `props` comme ceci :

```jsx
function ChildComponent(props) {
  return (
    <>
      <h1>Hello {props.name}</h1>
      <button onClick={() => props.setName('Mark')}>Change Name</button>
    </>
  )
}

```

Lorsque le bouton du `ChildComponent` est cliqué, la valeur de l'état `name` changera. En interne, React rafraîchira l'application et reflétera les changements dans l'interface utilisateur.

### Comment Utiliser React DevTools pour Inspecter les États et les Props

Pour faciliter votre développement, vous pouvez installer les React Developer Tools (DevTools en abrégé) pour inspecter l'état actuel et les valeurs des props de vos composants.

Vous pouvez [installer React DevTool pour Chrome ici](https://chromewebstore.google.com/detail/react-developer-tools/fmkadmapgofadopljbjfkapdkoienihi).

Une fois installé, ouvrez l'outil de développement et vous devriez avoir deux onglets supplémentaires appelés _Components_ et _Profiler_ comme montré ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2024/02/4-react-devtool-chrome.png)
_Ouverture de React DevTool_

De la même manière que vous pouvez inspecter les règles CSS appliquées aux éléments HTML, vous pouvez inspecter l'état et les props des composants React en utilisant les outils de développement. Cliquez sur l'onglet _Components_, et inspectez l'un des deux composants que nous avons créés précédemment.

Ci-dessous, vous pouvez voir les props et l'état du `ParentComponent`, ainsi que d'autres détails :

![Image](https://www.freecodecamp.org/news/content/images/2024/02/4-react-devtool-inspect.png)
_Inspection des Composants avec React DevTool_

Lorsque vous cliquez sur le bouton, la valeur de l'état changera en conséquence. Vous pouvez inspecter le `ChildComponent` pour voir ses détails. Ces DevTools seront très utiles lorsque vous développerez des applications React.

## Chapitre 5 : Rendu Conditionnel dans React

Vous pouvez contrôler ce qui est rendu par un composant en implémentant un rendu conditionnel dans votre code JSX.

Par exemple, supposons que vous souhaitez basculer entre le rendu des boutons de connexion et de déconnexion, en fonction de la disponibilité de l'état `user` :

```jsx
function App(props) {
  const { user } = props

  if (user) {
    return <button>Logout</button>
  }
  return <button>Login</button>
}

export default App

```

Vous n'avez pas besoin d'ajouter une instruction `else` dans le composant car React arrêtera les processus supplémentaires une fois qu'il atteindra une instruction `return`.

Dans l'exemple ci-dessus, React rendra le bouton de déconnexion lorsque la valeur `user` est vraie, et le bouton de connexion lorsque `user` est faux.

### Rendu Partiel avec une Variable Régulière

Lors du développement avec React, il y aura des cas où vous souhaitez rendre une partie de votre UI dynamiquement dans un composant.

Dans l'exemple ci-dessous, l'élément JSX est stocké dans une variable appelée `button`, et cette variable est utilisée à nouveau dans l'instruction `return` :

```jsx
function App(props) {
  const { user } = props

  let button = <button>Login</button>

  if (user) {
    button = <button>Logout</button>
  }

  return (
    <>
      <h1>Hello there!</h1>
      {button}
    </>
  )
}

```

Au lieu d'écrire deux instructions return, vous stockez l'élément UI dynamique à l'intérieur d'une variable et utilisez cette variable dans l'instruction `return`.

De cette façon, vous pouvez avoir un composant qui a des éléments statiques et dynamiques.

### Rendu Inline avec l'Opérateur `&&`

Il est possible de rendre un composant uniquement si une certaine condition est remplie et de rendre null sinon.

Par exemple, supposons que vous souhaitez afficher un message dynamique pour les utilisateurs lorsqu'ils ont de nouveaux e-mails dans leur boîte de réception :

```jsx
function App() {
  const newEmails = 2

  return (
    <>
      <h1>Hello there!</h1>
      {newEmails > 0 &&
        <h2>
          You have {newEmails} new emails in your inbox.
        </h2>
      }
    </>
  )
}

```

Dans cet exemple, l'élément `<h2>` n'est rendu que lorsque le nombre de `newEmails` est supérieur à 0.

### Rendu Inline avec l'Opérateur Conditionnel (Ternaire)

Il est également possible d'utiliser un opérateur ternaire afin de rendre l'UI dynamiquement.

Jetez un œil à l'exemple suivant :

```jsx
function App(props) {
  const { user } = props

  return (
    <>
      <h1>Hello there!</h1>
      { user? <button>Logout</button> : <button>Login</button> }
    </>
  )
}

```

Au lieu d'utiliser une variable pour contenir l'élément `<button>`, vous pouvez simplement utiliser l'opérateur ternaire sur la valeur `user` et rendre le bouton 'Logout' ou 'Login' selon la valeur de la variable.

## Chapitre 6 : Comment Gérer les Événements Utilisateur

Sous le capot, React dispose d'un gestionnaire d'événements interne qui se connecte à l'événement DOM natif.

C'est pourquoi nous pouvons ajouter la prop `onClick` aux boutons dans les chapitres précédents, qui s'exécute en réponse à un événement de clic.

Lorsque vous appelez une fonction en réponse à des événements, l'objet `event` sera passé à la fonction de rappel comme suit :

```jsx
function App() {
  const handleClick = (event) => {
    console.log("Hello World!");
    console.log(event);
  }
  return (
    <button onClick={handleClick}>
      Click me
    </button>
  )
}

```

Lorsque vous cliquez sur le bouton ci-dessus, la variable `event` sera enregistrée en tant qu'objet `SyntheticBaseEvent` dans votre console :

![Image](https://www.freecodecamp.org/news/content/images/2024/02/8-react-synthetic-event.png)
_Journal SyntheticBaseEvent de React_

L'objet `SyntheticBaseEvent` est un objet intégré de React utilisé pour interagir avec les événements DOM natifs. Différents navigateurs ont différentes implémentations de l'objet événement DOM, donc le `SyntheticBaseEvent` rend React compatible avec ces navigateurs.

Chaque fois qu'un événement DOM est déclenché, cet événement synthétique sera géré par React afin que vous puissiez décider quoi faire avec cet événement.

Le cas d'utilisation de cet événement synthétique est le même que celui de l'événement DOM natif. Trois des gestionnaires d'événements les plus courants que vous allez utiliser sont :

* `onChange`
* `onClick`
* `onSubmit`

Vous pouvez répondre aux interactions de l'utilisateur comme le clic, le survol, la mise au point ou la saisie dans un champ de formulaire, la soumission d'un formulaire, etc.

### Comment Changer l'UI en Gérant les Événements

Dans le chapitre précédent, vous avez vu comment la logique conditionnelle peut être utilisée pour rendre différentes sorties.

En combinant la logique conditionnelle avec l'état, les props et les gestionnaires d'événements, vous pouvez créer un composant dynamique qui rend différentes sorties en fonction des données qu'il contient actuellement.

Par exemple, supposons que vous souhaitez afficher ou masquer un élément `<div>` avec un clic sur un bouton. Voici comment faire :

```jsx
import { useState } from 'react';

function App() {
  // État pour contenir le statut de visibilité du paragraphe
  const [isParagraphVisible, setIsParagraphVisible] = useState(true);

  // Fonction pour basculer le statut de visibilité du paragraphe
  const toggleStatus = () => {
    setIsParagraphVisible(!isParagraphVisible);
  };

  return (
    <>
      <h1>Change UI based on click</h1>
      {isParagraphVisible && (
        <p>This paragraph will be shown/hidden on click</p>
      )}
      <button onClick={toggleStatus}>
        {isParagraphVisible ? 'Hide' : 'Show'} Paragraph
      </button>
    </>
  );
}

export default App;

```

Tout d'abord, vous créez un état pour contenir le statut de visibilité du paragraphe en utilisant le hook `useState`. La valeur par défaut de l'état est `true`.

Ensuite, une fonction nommée `toogleStatus()` est définie. Cette fonction changera la valeur `status` de `true` à `false` et vice versa.

Enfin, une instruction `return` est ajoutée pour rendre les éléments à l'écran. Lorsque le bouton est cliqué, la fonction `toogleStatus()` sera exécutée. Cela affichera ou masquera le paragraphe en fonction du statut actuel.

En utilisant les états, les props et les gestionnaires d'événements, le code que vous écrivez devient une description de ce à quoi l'interface utilisateur devrait ressembler. React prend ensuite cette description et la rend dans le navigateur.

## Chapitre 7 : CSS dans React

Il existe 4 façons courantes d'ajouter du CSS dans une application React :

1. Style inline
2. Fichiers CSS
3. Modules CSS
4. Tailwind CSS

Ce chapitre explorera ces 4 différentes façons d'écrire du CSS dans les composants React, et celle que vous devriez utiliser lorsque vous commencez une application React.

### Style Inline React

Les composants React sont composés d'éléments JSX. Mais simplement parce que vous n'écrivez pas d'éléments HTML réguliers ne signifie pas que vous ne pouvez pas utiliser l'ancienne méthode de style inline.

La seule différence avec JSX est que les styles inline doivent être écrits sous forme d'objet au lieu d'une chaîne. Voir l'exemple ci-dessous :

```jsx
function App() {
  return (
    <h1 style={{ color: 'red' }}>Hello World</h1>
  );
}

```

Dans l'attribut style ci-dessus, le premier ensemble d'accolades est utilisé pour écrire des expressions JavaScript. Le second ensemble d'accolades initialise un objet JavaScript.

Les noms de propriétés de style qui ont plus d'un mot sont écrits en camelCase au lieu d'utiliser le style traditionnel avec des traits d'union. Par exemple, la propriété habituelle `text-align` est écrite `textAlign` en JSX :

```jsx
function App() {
  return (
    <h1 style={{ textAlign: 'center' }}>Hello World</h1>
  );
}

```

Parce que l'attribut style est un objet, vous pouvez également séparer le style en l'écrivant comme une constante. De cette façon, vous pouvez réutiliser le style dans d'autres éléments selon les besoins :

```jsx
const pStyle = {
  fontSize: '16px',
  color: 'blue'
}

export default function App() {
  return (
    <>
      <p style={pStyle}>Hello World!</p>
      <p style={pStyle}>The weather is sunny today.</p>
    </>
  )
}

```

Si vous devez étendre votre style de paragraphe plus loin, vous pouvez utiliser l'opérateur de propagation.

Cela vous permettra d'ajouter des styles inline à votre objet de style déjà déclaré. Voir l'élément `<p>` ci-dessous :

```jsx
const pStyle = {
  fontSize: '16px',
  color: 'blue'
}

export default function App() {
  return (
    <p style={{ ...pStyle, color: 'green', textAlign: 'right' }}>
      When you go to work, bring your umbrella with you!
    </p>
  )
}

```

Les styles inline JSX vous permettent d'écrire du CSS directement dans votre composant.

L'un des avantages de l'utilisation de l'approche de style inline est que vous aurez une technique de style simple et centrée sur les composants. Lorsque vous utilisez un objet pour le style, vous pouvez étendre votre style en propageant l'objet.

Mais dans un projet grand et complexe où vous avez des centaines de composants React à gérer, cela pourrait ne pas être le meilleur choix pour vous.

Vous ne pouvez pas spécifier de pseudo-classes en utilisant des styles inline. Cela signifie que vous ne pouvez pas définir de règles comme `:hover`, `:focus`, `:active`, etc.

De plus, vous ne pouvez pas spécifier de requêtes média pour le style réactif. Considérons une autre façon de styliser votre application React.

### Fichiers CSS

Une autre façon d'ajouter du CSS dans React est d'utiliser des fichiers `.css`. Vite sait déjà comment gérer un fichier `.css`, donc tout ce que vous avez à faire est d'importer le fichier CSS dans votre fichier JSX et d'ajouter la bonne prop `className` à votre composant.

Créons un fichier `style.css` dans votre dossier de projet avec le contenu suivant :

```css
/* style.css */
.paragraph-text {
  font-size: 16px;
  color: #ff0000;
}

```

Maintenant, importons le fichier CSS dans le fichier `App.jsx` et ajoutons la prop class au composant :

```jsx
import './style.css';

function App() {
  return (
      <p className="paragraph-text">
        The weather is sunny today.
      </p>
  );
}

```

De cette façon, le CSS sera séparé de vos fichiers JavaScript, et vous pourrez simplement écrire la syntaxe CSS comme d'habitude.

Vous pouvez même inclure un framework CSS tel que Bootstrap dans React avec cette approche. Tout ce que vous avez à faire est d'importer le fichier CSS dans votre composant racine.

Cette méthode vous permettra d'utiliser toutes les fonctionnalités CSS, y compris les pseudo-classes et les requêtes média.

### Modules CSS

Un module CSS est un fichier CSS régulier avec tous ses noms de classes et d'animations portées localement par défaut.

Lorsque vous appliquez cette méthode, chaque composant React aura son propre fichier CSS, et vous devez importer ce fichier CSS dans votre composant.

Pour indiquer à React que vous utilisez des modules CSS, nommez votre fichier CSS en utilisant la convention `[name].module.css`.

Voici un exemple :

```css
/* App.module.css */
.BlueParagraph {
  color: blue;
  text-align: left;
}
.GreenParagraph {
  color: green;
  text-align: right;
}

```

Ensuite, importez-le dans votre fichier de composant :

```jsx
import styles from "./App.module.css";

function App() {
  return (
    <>
      <p className={styles.BlueParagraph}>
        The weather is sunny today.
      </p>
      <p className={styles.GreenParagraph}>
        Still, don't forget to bring your umbrella!
      </p>
    </>
  )
} 

```

Lorsque vous construisez votre application, Vite recherchera automatiquement les fichiers CSS qui ont le nom `.module.css` et traitera les noms de classes en un nouveau nom localisé.

L'utilisation de modules CSS garantit que vos classes CSS sont portées localement, empêchant les règles CSS d'entrer en conflit les unes avec les autres.

Un autre avantage de l'utilisation des modules CSS est que vous pouvez composer une nouvelle classe en héritant d'autres classes que vous avez écrites. De cette façon, vous pourrez réutiliser le code CSS que vous avez écrit précédemment, comme ceci :

```css
.MediumParagraph {
  font-size: 20px;
}
.BlueParagraph {
  composes: MediumParagraph;
  color: blue;
  text-align: left;
}
.GreenParagraph {
  composes: MediumParagraph;
  color: green;
  text-align: right;
}

```

Mais nous n'allons pas explorer chaque fonctionnalité des modules CSS ici, seulement assez pour vous familiariser avec eux.

### Tailwind CSS

Tailwind CSS est un framework CSS moderne basé sur les utilitaires qui vous permet de styliser des éléments en combinant un ensemble de classes.

Les frameworks CSS comme Bootstrap et Bulma vous fournissent des composants de haut niveau que vous pouvez immédiatement utiliser dans votre projet. Lorsque vous devez styliser un bouton, vous devez simplement appliquer les classes qui contiennent les propriétés CSS souhaitées :

```html
<button className="btn btn-primary">Subscribe</button>

```

Lorsque vous utilisez Bootstrap, la classe `btn` fournit une combinaison de propriétés CSS telles que le remplissage, la couleur, l'opacité, le poids de la police, etc.

D'autre part, Tailwind vous donne des classes utilitaires où chaque classe n'a qu'une ou deux propriétés :

```html
<button className='px-5 py-2 text-white bg-blue-500 border-2'>
  Subscribe
</button>

```

Dans l'exemple ci-dessus, `px-5` est l'abréviation de `padding-left` et `padding-right`, tandis que 5 est une taille spécifique pour les rembourrages. `text-white` applique `color: white`, `bg-blue-500` applique la propriété `background-color`, et `border` applique `border-width`.

### Lequel Devez-Vous Utiliser ?

Cela dépend de la méthode avec laquelle vous vous sentez le plus à l'aise. Si vous travaillez avec une équipe, vous devez discuter et convenir de la méthode que vous souhaitez appliquer, car mélanger les styles rend le développement et la maintenance de l'application difficiles.

Rappelez-vous : Utilisez toujours une seule façon de styliser les composants React dans un projet spécifique pour éviter la confusion.

## Chapitre 8 : Comment Construire des Formulaires dans React

L'une des interfaces les plus courantes que vous allez construire en tant que développeur web est un formulaire. Dans React, vous pouvez créer un formulaire en utilisant l'état comme source unique des données de ce formulaire.

Dans ce chapitre, je vais vous montrer comment gérer l'entrée de formulaire, la soumission de formulaire et la validation de formulaire en utilisant React.

### Comment Gérer l'Entrée de Formulaire

Par exemple, supposons que vous souhaitez créer un formulaire avec une seule entrée de texte et un bouton.

Vous pouvez d'abord configurer l'état qui servira de valeur d'entrée :

```js
import { useState } from 'react';

function Form() {
  const [username, setUsername] = useState();
}

```

Ensuite, ajoutez l'instruction `return` et définissez le formulaire. Sur l'élément `<input>`, attribuez l'état `username` comme prop `value` :

```jsx
import { useState } from 'react';

function Form() {
  const [username, setUsername] = useState();
  return (
    <form>
      Username:
      <input type='text' name='username' value={username} />
    </form>
  );
}

```

Ensuite, ajoutez la prop `onChange` à l'élément `<input>`. Dans cette prop, attribuez la `value` de l'entrée de texte comme valeur de l'état `username` :

```jsx
import { useState } from 'react';

function Form() {
  const [username, setUsername] = useState();
  return (
    <form>
      Username:
      <input
        type='text'
        value={username}
        onChange={e => setUsername(e.target.value)}
      />
    </form>
  );
}

```

L'objet `e` ou `event` est passé par la prop `onChange` à la fonction de rappel. À partir de cet objet, nous pouvons obtenir la valeur de l'entrée de texte à la propriété `event.target.value`.

Maintenant, chaque fois que la valeur de l'entrée change, l'état sera mis à jour pour refléter les changements.

### Comment Gérer la Soumission de Formulaire

L'étape suivante consiste à soumettre le formulaire. Créons une fonction qui gère l'événement de soumission appelée `handleSubmit()` comme suit :

```jsx
import { useState } from 'react';

function Form() {
  const [username, setUsername] = useState();

  const handleSubmit = (e) => {
    e.preventDefault();
    alert(username);
  }

  return (
    <form onSubmit={handleSubmit}>
      Username:
      <input
        type='text'
        value={username}
        onChange={(e) => setUsername(e.target.value)}
      />
      <button>Submit</button>
    </form>
  );
}

```

Ici, la fonction `handleSubmit()` arrêtera le comportement par défaut de soumission du formulaire, qui déclenchera un rafraîchissement, puis créera une boîte d'alerte pour afficher la valeur `username`.

La fonction est ensuite passée à la prop `onSubmit` de l'élément `<form>`. Un `<button>` est également ajouté afin que l'utilisateur puisse soumettre le formulaire.

### Comment Gérer la Validation de Formulaire

Pour gérer la validation de formulaire, vous devez créer un autre état qui stockera le message d'erreur. Vous pouvez nommer cet état `usernameError` comme suit :

```jsx
const [usernameError, setUsernameError] = useState();

```

Ensuite, créez une fonction `handleUsername()` qui s'exécutera lorsque l'entrée `username` changera.

À l'intérieur de cette fonction, vous pouvez appeler la fonction `setUsername()` pour mettre à jour l'état, puis écrire la logique pour valider la valeur d'entrée.

Par exemple, supposons que la longueur de `username` doit être supérieure à 6. Voici comment faire :

```jsx
const handleUsername = e => {
  const { value } = e.target;
  setUsername(value);

  // Valider la valeur du nom d'utilisateur :
  if (value.length <= 6) {
    setUsernameError('La longueur du nom d\'utilisateur doit être supérieure à 6 caractères');
  } else {
    setUsernameError();
  }
};

```

Maintenant que vous avez une logique de validation, vous devez définir la fonction `handleUsername()` comme gestionnaire de la prop `onChange`.

Ajoutez également un paragraphe sous l'élément `<input>` qui affichera le message d'erreur comme suit :

```jsx
return (
  <form onSubmit={handleSubmit}>
    Username:
    <input type='text' value={username} onChange={handleUsername} />
    <p>{usernameError}</p>
    <button>Submit</button>
  </form>
);

```

À l'intérieur de la fonction `handleSubmit()`, vous pouvez vérifier s'il y a une erreur dans le formulaire en vérifiant l'état `usernameError`, puis empêcher le formulaire d'être soumis lorsqu'il y a une erreur :

```jsx
const handleSubmit = (e) => {
  e.preventDefault();
  if(usernameError){
    alert('Impossible de soumettre : Le formulaire contient des erreurs');
  } else {
    alert(username);
  }
}

```

De cette façon, le formulaire ne sera pas soumis tant que l'erreur n'est pas corrigée.

Voici le code source complet du formulaire si vous souhaitez l'essayer :

```jsx
import { useState } from 'react';

function App() {
  const [username, setUsername] = useState();
  const [usernameError, setUsernameError] = useState();

  const handleSubmit = (e) => {
    e.preventDefault();
    if(usernameError){
      alert('Impossible de soumettre : Le formulaire contient des erreurs');
    } else {
      alert(username);
    }
  }

  const handleUsername = e => {
    const { value } = e.target;
    setUsername(value);
  
    // Valider la valeur du nom d'utilisateur :
    if (value.length <= 6) {
      setUsernameError('La longueur du nom d\'utilisateur doit être supérieure à 6 caractères');
    } else {
      setUsernameError();
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      Username:
      <input
        type='text'
        value={username}
        onChange={handleUsername}
      />
      <p>{usernameError}</p>
      <button>Submit</button>
    </form>
  );
}

export default App;

```

Un formulaire peut être aussi complexe ou aussi simple que nécessaire, mais vous utiliserez le modèle que vous voyez ici quel que soit le formulaire que vous construisez :

* Les valeurs d'état sont utilisées comme source des données et de la validation du formulaire
* La prop `onChange` comme moyen de mettre à jour l'état
* Les validations sont déclenchées par les entrées de l'utilisateur
* Une fonction `handleSubmit()` est exécutée lorsque le formulaire est soumis

En utilisant ces éléments de base, vous pouvez construire n'importe quel formulaire requis par votre application.

## Chapitre 9 : Requêtes Réseau dans React

Les applications web modernes tendent à avoir une architecture modulaire, où le back-end est séparé du front-end. L'application front-end devra envoyer une requête réseau HTTP à un point de terminaison distant.

React ne vous dit pas comment vous devriez envoyer des requêtes réseau. La bibliothèque se concentre uniquement sur le rendu de l'UI avec la gestion des données en utilisant les props et les états.

Pour récupérer des données en utilisant React, vous pouvez utiliser n'importe quelle bibliothèque JavaScript valide comme Axios, Superagent, et même l'API Fetch native.

Dans ce chapitre, nous allons voir comment effectuer des requêtes réseau en utilisant Fetch dans React.

### Le Hook useEffect

Lorsque vous créez une application React qui doit se synchroniser avec un système externe à React, vous devez utiliser le hook `useEffect`.

Ce hook vous permet d'exécuter du code après le rendu afin que vous puissiez synchroniser votre composant avec un système externe à React.

Lorsque le hook a terminé l'exécution de la requête de données, vous pouvez définir la réponse dans les états de votre composant et rendre les composants appropriés en fonction des valeurs d'état.

Pour vous montrer un exemple, récupérons des données depuis [https://jsonplaceholder.typicode.com/todos/1](https://jsonplaceholder.typicode.com/todos/1) qui est un point de terminaison factice :

```jsx
function App() {
  const [title, setTitle] = useState('');

  useEffect(() => {
    getData();
  }, []);

  const getData = async () => {
    const response = await fetch('https://jsonplaceholder.typicode.com/todos/1');
    const task = await response.json();
    console.log(task)
    setTitle(task.title);
  };

  return <h1>{title}</h1>;
}

```

Dans le code ci-dessus, nous créons un composant `App` qui a un état appelé `title`, et nous exécutons l'API Fetch pour obtenir une tâche todo depuis l'API.

Lorsque une réponse est reçue, nous analysons la chaîne JSON en un objet JavaScript, nous enregistrons l'objet, puis nous définissons l'état `title` sur la valeur de la propriété `task.title`.

La réponse est la suivante :

![Image](https://www.freecodecamp.org/news/content/images/2024/02/9-useeffect-log.png)
_Journal useEffect de React_

Ici, vous pouvez voir que le `console.log()` est appelé deux fois. Cela est dû au fait que l'enveloppe `<React.StrictMode>` exécute toujours un hook `useEffect` deux fois pour vous aider dans le développement.

Si vous supprimez l'enveloppe `<React.StrictMode>` dans `main.jsx`, le hook `useEffect` ne s'exécutera qu'une seule fois.

Le hook `useEffect` lui-même est une fonction qui accepte deux arguments :

* Une fonction de rappel à exécuter à chaque rendu
* Un tableau de variables d'état à surveiller pour les changements. `useEffect` sera ignoré si aucune des variables n'est mise à jour.

Lorsque vous souhaitez exécuter `useEffect` une seule fois, vous pouvez passer un tableau vide comme second argument à la fonction, comme montré dans l'exemple ci-dessus.

En utilisant le hook `useEffect`, React peut envoyer des requêtes HTTP et récupérer des données depuis n'importe quel système externe, puis stocker ces données dans l'état du composant.

## Conclusion

Félicitations pour avoir terminé ce guide ! J'espère que vous l'avez trouvé utile et que vous sentez maintenant que l'apprentissage de React n'est pas impossible ou confus. Tout ce dont vous avez besoin est un guide étape par étape qui révèle les concepts clés de React un par un.

Si vous êtes impatient d'approfondir React et d'élargir vos compétences, je vous encourage à consulter mon nouveau livre intitulé _Beginning React_ ici :

[![Beginning React Book](https://www.freecodecamp.org/news/content/images/2024/02/beginning-react-promo.png)](https://codewithnathan.com/beginning-react)

Le but de ce livre est de vous aider à voir comment construire une application en utilisant React. Il y a deux projets inclus dans ce livre qui vous donneront l'"expérience" de la construction d'une application web en utilisant React.

Vous verrez comment les concepts de React comme les composants, JSX, les props, les états, les hooks et l'API Context sont utilisés pour créer une application front-end dynamique.

Voici ma promesse : _Vous vous sentirez réellement confiant dans la construction d'applications web à partir de zéro en utilisant React._

Merci d'avoir lu !