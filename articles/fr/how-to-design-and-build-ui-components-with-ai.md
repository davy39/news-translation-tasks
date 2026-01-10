---
title: 'Du Concept au Code : Comment Utiliser des Outils d''IA pour Concevoir et Construire
  des Composants d''Interface Utilisateur'
subtitle: ''
author: Ekemini Samuel
co_authors: []
series: null
date: '2024-10-14T19:50:16.406Z'
originalURL: https://freecodecamp.org/news/how-to-design-and-build-ui-components-with-ai
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1727885187463/f41f59b0-1ec0-4dbf-9d2a-437738584310.png
tags:
- name: AI
  slug: ai
- name: UI
  slug: ui
- name: Web Development
  slug: web-development
- name: coding
  slug: coding
seo_title: 'Du Concept au Code : Comment Utiliser des Outils d''IA pour Concevoir
  et Construire des Composants d''Interface Utilisateur'
seo_desc: 'How should a website look? What size should the buttons be? What layout
  should you use? Do your users need an OTP to reset their passwords? These are all
  questions that proper user interface and user experience (UI/UX) design answer.

  Design prototypi...'
---

À quoi devrait ressembler un site web ? Quelle taille les boutons devraient-ils avoir ? Quel agencement devriez-vous utiliser ? Vos utilisateurs ont-ils besoin d'un OTP pour réinitialiser leurs mots de passe ? Ce sont toutes des questions auxquelles une conception appropriée de l'interface utilisateur et de l'expérience utilisateur (UI/UX) répond.

Le prototypage et les tests de conception sont des étapes critiques pour optimiser la fonctionnalité UX d'un site web. Une [étude](https://www.forrester.com/report/The-Six-Steps-For-Justifying-Better-UX/RES117708) a rapporté qu'une amélioration de la [conception UX](https://www.hotjar.com/ux-design) a conduit à une augmentation de 400 % des conversions sur le site web.

Pour une tâche aussi importante, nous avons besoin des meilleurs outils et ressources possibles. Et récemment, j'ai pris plaisir à utiliser [Cody de Sourcegraph](https://sourcegraph.com/cody). Cody est un outil d'IA qui accélère le codage en vous aidant à comprendre, écrire et corriger du code. Il accède aux informations de l'ensemble de votre base de code et référence également les pages de documentation pour fournir un contexte sur les fonctions et les variables, aider à créer un nouveau code et améliorer votre système de conception.

Lorsque vous le combinez avec Tailwind CSS, qui est un framework CSS utilitaire, vous pouvez rapidement construire des composants d'interface utilisateur à la fois fonctionnels et visuellement attrayants.

Dans ce tutoriel, je vais vous apprendre à construire des interfaces utilisateur plus rapidement avec Cody et Tailwind CSS afin que vous puissiez utiliser l'IA pour rationaliser votre flux de travail.

### Prérequis

* Compréhension de base de JavaScript et du développement front-end.

* Familiarité avec Tailwind CSS.

* [Node.js](https://nodejs.org/en) installé sur votre système.

* Un éditeur de code comme Visual Studio Code (VS Code).

* Cody. [Inscrivez-vous sur Sourcegraph](https://sourcegraph.com/cody) pour obtenir un accès (c'est gratuit).

### Table des Matières

* [Que allons-nous construire ?](#heading-quest-ce-que-nous-allons-construire)

* [Comment configurer votre environnement](#heading-comment-configurer-votre-environnement)

* [Comment créer des composants d'interface utilisateur avec l'IA](#heading-comment-creer-des-composants-dinterface-utilisateur-avec-lia)

* [Interfaces utilisateur plus complexes](#heading-interfaces-utilisateur-plus-complexes)

* [Comment améliorer et gérer des bases de code existantes avec Cody](#heading-comment-ameliorer-et-gerer-des-bases-de-code-existantes-avec-cody)

* [Prochaines étapes](#heading-prochaines-etapes)

## Que allons-nous construire ?

Construisons encore une autre application Todo, mais avec une touche spéciale. Chaque élément de la liste de tâches aura un minuteur qui peut être démarré, mis en pause et réinitialisé. Cela pourrait être utile pour suivre le temps que vous passez à travailler sur des tâches spécifiques.

D'après la [documentation de Cody](https://sourcegraph.com/docs/cody/capabilities/chat#selecting-context), le chat de Cody vous permet d'ajouter des fichiers et des symboles comme contexte dans vos messages.

* Tapez `@` puis un nom de fichier pour inclure un fichier comme contexte.

* Tapez `@#` puis un nom de symbole pour inclure la définition du symbole comme contexte. Les fonctions, méthodes, classes, types, etc., sont tous des symboles.

Même si Cody fera la majeure partie du travail, il est bon d'avoir un plan de la façon dont nous voulons que l'interface utilisateur soit. Voici les wireframes que j'ai créés avec [wireframe.cc](https://wireframe.cc/) :

![Wireframe du composant de tâche - état général et état détaillé](https://cdn.hashnode.com/res/hashnode/image/upload/v1726667247231/ada73031-20ac-4e07-8203-abe7d85a4d55.png align="center")

![Wireframe de l'en-tête et du pied de page](https://cdn.hashnode.com/res/hashnode/image/upload/v1726667377001/5ac6b7ce-e2a8-41d6-8378-e5ba36bb546d.png align="center")

D'accord ! Commençons.

## Comment configurer votre environnement

Ce tutoriel utilise Visual Studio Code, mais le processus de développement est similaire dans d'autres éditeurs de code. Si vous n'avez pas encore configuré d'éditeur, choisissez celui qui convient à vos préférences et [installez Node.js](https://nodejs.org/en/learn/getting-started/how-to-install-nodejs).

Au moment de la rédaction de cet article, Sourcegraph Cody est disponible sur [Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=sourcegraph.cody-ai), [Neovim](https://github.com/sourcegraph/sg.nvim#setup), [Cody CLI](https://sourcegraph.com/github.com/sourcegraph/cody@main/-/blob/cli/README.md), [Emacs](https://github.com/sourcegraph/emacs-cody), et [tous les IDE JetBrains](https://plugins.jetbrains.com/plugin/9682-cody-ai-coding-assistant-with-autocomplete--chat)

### Comment ajouter Cody à votre éditeur de code

Tout d'abord, rendez-vous sur la [page d'accueil de Cody](https://sourcegraph.com/cody/), cliquez sur **Obtenez Cody gratuitement**, et suivez les instructions pour vous inscrire à un compte [Sourcegraph](https://sourcegraph.com/) en utilisant votre méthode d'authentification préférée—GitHub, GitLab, ou Google.

Choisissez l'option appropriée pour votre éditeur de code. Si vous utilisez Visual Studio Code, ce serait **Installer Cody dans VS Code**.

![Tableau de bord de Cody](https://cdn.hashnode.com/res/hashnode/image/upload/v1726667454887/bccde86e-ac68-4425-a5d8-ffbc7febfd83.png align="center")

L'ouverture de l'extension dans votre éditeur de code vous invite à vous connecter :

![Connexion à Cody avec votre méthode préférée.](https://cdn.hashnode.com/res/hashnode/image/upload/v1726667554900/d956efbb-9712-4096-a968-69854d3b98c0.png align="center")

Après vous être connecté, nous sommes prêts à commencer.

![Le chat de Cody sur VS Code](https://cdn.hashnode.com/res/hashnode/image/upload/v1726667586141/428a2eac-f383-4d7f-a63e-5fdd5638f227.jpeg align="center")

### **Comment configurer le projet**

Nous travaillerons avec un projet Vite + React + TailwindCSS, mais ces idées peuvent facilement être appliquées à tout autre framework (pensez à Vue, Astro, Svelte, ou même du JavaScript Vanilla) ou bibliothèque de style (comme Bootstrap, Bulma, Foundation CSS, ou tout ce que vous préférez).

Exécutez la commande suivante pour créer un nouveau projet React, **abc-planning-todo-app** :

```bash
npm create vite@latest abc-planning-todo-app -- --template react
```

Ensuite, installez Tailwind CSS :

```bash
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
```

Ensuite, mettez à jour `tailwind.config.js` avec ce code pour configurer Tailwind CSS pour le projet :

```javascript

/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

Supprimez tout dans `./src/index.css` et ajoutez les directives Tailwind CSS suivantes :

```javascript

@tailwind base;
@tailwind components;
@tailwind utilities;
```

## Comment créer des composants d'interface utilisateur avec l'IA

Pour la cohérence, choisissons une palette de couleurs que nous utiliserons pour notre application de liste de tâches.

![Palettes de couleurs pour l'interface utilisateur TODO](https://cdn.hashnode.com/res/hashnode/image/upload/v1726667638883/06819a4e-d7fd-4a24-b9b6-6ef8cda38b08.png align="center")

Pour utiliser ces couleurs dans notre thème Tailwind, nous devons d'abord leur donner des noms descriptifs. Demandons de l'aide à Cody !

Pour le reste de cet article, toutes les citations représentent un seul message d'invite utilisé lors de la discussion avec Cody.

> *Quels seraient de bons noms pour les couleurs hexadécimales suivantes ?*
> 
> * *2B2D42*
> 
> * *8D99AE*
> 
> * *EDF2F4*
> 
> * *EF233C*
> 
> * *D90429*
> 

Puis,

> *Mettre à jour* ***@tailwind.config.js*** *pour inclure ces 5 couleurs hexadécimales ci-dessus :*

```javascript

/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'bleu-nuit': '#2B2D42',
        'ciel-nuageux': '#8D99AE',
        'blanc-glace': '#EDF2F4',
        'rouge-vif': '#EF233C',
        'rouge-ruby': '#D90429',
      },
    },
  },
  plugins: [],
}
```

### **Comment créer des composants d'interface utilisateur de base**

Tout d'abord, nous créons le composant Header. Avec des modèles pour des composants relativement simples (par exemple, des champs de texte, des en-têtes, des boutons et des menus déroulants), c'est aussi simple que de fournir un nom pour le composant et le contenu qu'il doit contenir.

> *Créer un composant React Header simple avec uniquement le nom de l'entreprise à gauche et la devise de l'entreprise à droite. Utiliser le thème Tailwind* ***@tailwind.config.js***

![Ajout de l'invite à Cody](https://cdn.hashnode.com/res/hashnode/image/upload/v1726667685164/728a496e-c018-4f09-ac4a-1926f322b3f1.png align="center")

Cody générera un composant Header, que vous pourrez ensuite copier et coller dans `./src/components/Header.jsx`.

Vous pouvez également enregistrer le code dans un nouveau fichier dans votre projet directement depuis le chat de Cody.

```javascript

// ./src/components/Header.jsx
import React from 'react';
const Header = () => {
  return (
    <header className="bg-bleu-nuit text-blanc-glace p-4 flex justify-between items-center">
      <div className="text-2xl font-bold">
        Entreprise
      </div>
      <div className="text-ciel-nuageux italic">
        Innover. Créer. Inspirer.
      </div>
    </header>
  );
};
export default Header;
```

Ensuite, créez le composant Footer avec cette invite :

> *Créer un composant React Footer simple avec le contenu Copyright C ABC Planning. Utiliser le thème Tailwind* ***@tailwind.config.js***\*. Assurez-vous que le pied de page est toujours en bas de la fenêtre\*

```javascript

// ./src/components/Footer.jsx
import React from 'react';
const Footer = () => {
  return (
    <footer className="bg-bleu-nuit text-blanc-glace p-4 text-center fixed bottom-0 w-full">
      <p>&copy; {new Date().getFullYear()} ABC Planning</p>
    </footer>
  );
};
export default Footer;
```

Jetons un coup d'œil à ce que nous avons jusqu'à présent.

![L'en-tête et le pied de page générés](https://cdn.hashnode.com/res/hashnode/image/upload/v1726667795664/bb16ff44-1403-499f-9441-9dcc804ea06b.png align="center")

## **Interfaces utilisateur plus complexes**

Ensuite, nous aurons besoin d'un conteneur qui contiendra toutes nos tâches. Demandons à Cody de créer un composant de conteneur de tâches.

> *Créer un composant React TodoContainer qui servira de conteneur pour les éléments Todo. Utiliser le thème Tailwind* ***@tailwind.config.js***\*. Il doit être réactif pour les mobiles\*.

Nous disons à Cody :

* Ce que nous voulons (un composant React)

* Une brève description de la manière dont ce composant se comporte/ce qu'il fait (conteneur pour les tâches)

* Tout contexte supplémentaire - feuilles de style, préférences, conventions, ou autre chose.

```javascript

// ./src/components/TodoContainer.jsx
import React from 'react';
const TodoContainer = ({ children }) => {
  return (
    <div className="bg-blanc-glace min-h-screen p-4 sm:p-6 md:p-8">
      <div className="max-w-4xl mx-auto">
        <h1 className="text-bleu-nuit text-3xl font-bold mb-6">Liste de tâches</h1>
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
          {children}
        </div>
      </div>
    </div>
  );
};
export default TodoContainer;
```

Une bonne stratégie de [programmation orientée chat](https://sourcegraph.com/blog/chat-oriented-programming-in-action) (CHOP) consiste à séparer la création de la structure de la création du contenu. Cela simplifie le processus d'invite.

Cody peut [g](https://sourcegraph.com/blog/chat-oriented-programming-in-action)énérer les deux très bien, mais essayer d'ajuster une seule invite pour les deux tâches pourrait être difficile. Chaque invite doit avoir un objectif clair et spécifique pour obtenir les meilleurs résultats.

Concentrons-nous maintenant sur le composant `TodoItem` et divisons-le en sections :

* Il y a un **en-tête de tâche** qui consiste en un titre avec une bordure.

* Il y a un bouton **Voir les détails**.

* Il y a un minuteur montrant depuis combien de temps la tâche a été démarrée.

* Il y a des boutons de contrôle (qui reflètent l'état de la tâche)

> *Créer un composant React TodoItem.*
> 
> *Il se compose de :*
> 
> *1. Titre de la tâche. Un texte d'en-tête avec une bordure autour.*
> 
> *2. Un lien/bouton simplifié "Voir les détails" sous la boîte d'en-tête de la tâche.*
> 
> *3. Un minuteur numérique qui montre les heures, les minutes et les secondes au format 00:00:00.*
> 
> *4. Actions de la tâche - "Démarrer", "Pause", "Réinitialiser". Utiliser des couleurs pertinentes pour chacune. Le minuteur doit pouvoir être démarré, mis en pause et réinitialisé lorsque le bouton correspondant est pressé.*
> 
> *Il doit ressembler à une carte (haute et non large) sur un bureau.*
> 
> *Il sera utilisé avec* ***@TodoContainer.jsx***
> 
> *Utiliser le thème* ***@tailwind.config.js***

```javascript
// ./src/components/TodoItem.jsx
import React, { useState, useEffect } from 'react';
const TodoItem = ({ title }) => {
  const [time, setTime] = useState(0);
  const [isRunning, setIsRunning] = useState(false);
  useEffect(() => {
    let interval;
    if (isRunning) {
      interval = setInterval(() => {
        setTime((prevTime) => prevTime + 1);
      }, 1000);
    }
    return () => clearInterval(interval);
  }, [isRunning]);
  const formatTime = (seconds) => {
    const hours = Math.floor(seconds / 3600);
    const minutes = Math.floor((seconds % 3600) / 60);
    const secs = seconds % 60;
    return [hours, minutes, secs].map(v => v.toString().padStart(2, '0')).join(':');
  };
  const handleStart = () => setIsRunning(true);
  const handlePause = () => setIsRunning(false);
  const handleReset = () => {
    setIsRunning(false);
    setTime(0);
  };
  return (
    <div className="bg-blanc-glace rounded-lg shadow-md p-4 flex flex-col space-y-4 h-full">
      <h2 className="text-xl font-bold text-bleu-nuit border-2 border-bleu-nuit rounded p-2 text-center">
        {title}
      </h2>
      <button className="text-ciel-nuageux hover:text-bleu-nuit transition-colors">
        Voir les détails
      </button>
      <div className="text-3xl font-mono text-bleu-nuit text-center">
        {formatTime(time)}
      </div>
      <div className="flex justify-between mt-auto">
        <button 
          onClick={handleStart} 
          className="bg-rouge-vif text-blanc-glace px-4 py-2 rounded hover:bg-rouge-ruby transition-colors"
        >
          Démarrer
        </button>
        <button 
          onClick={handlePause} 
          className="bg-ciel-nuageux text-bleu-nuit px-4 py-2 rounded hover:bg-blanc-glace transition-colors"
        >
          Pause
        </button>
        <button 
          onClick={handleReset} 
          className="bg-bleu-nuit text-blanc-glace px-4 py-2 rounded hover:bg-ciel-nuageux transition-colors"
        >
          Réinitialiser
        </button>
      </div>
    </div>
  );
};
export default TodoItem;
```

D'après nos wireframes, chaque tâche aura un état détaillé lorsque sa description est visible et peut être mise à jour. Nous allons dire à Cody de mettre à jour le fichier `TodoItem.jsx` existant :

> *Mettre à jour* ***@TodoItem.jsx*** *pour avoir un deuxième état, lorsque le bouton de vue détaillée est pressé. Dans cet état, le TodoItem est composé des éléments suivants uniquement :*
> 
> *1. En-tête de la tâche avec le titre de la tâche, comme avant*
> 
> *2. Une zone de texte avec une description de la tâche*
> 
> *3. Un bouton de sauvegarde, qui émet un événement updateTask, et ramène le composant à son état par défaut.*
> 
> *Inclure des animations entre la transition pour créer une sensation et une expérience fluides*

```javascript

// ./src/components/TodoItem.jsx
import React, { useState, useEffect } from 'react';
const TodoItem = ({ title, description = '', onUpdateTask }) => {
  const [time, setTime] = useState(0);
  const [isRunning, setIsRunning] = useState(false);
  const [isDetailView, setIsDetailView] = useState(false);
  const [taskDescription, setTaskDescription] = useState(description);
  useEffect(() => {
    let interval;
    if (isRunning) {
      interval = setInterval(() => {
        setTime((prevTime) => prevTime + 1);
      }, 1000);
    }
    return () => clearInterval(interval);
  }, [isRunning]);
  const formatTime = (seconds) => {
    const hours = Math.floor(seconds / 3600);
    const minutes = Math.floor((seconds % 3600) / 60);
    const secs = seconds % 60;
    return [hours, minutes, secs].map(v => v.toString().padStart(2, '0')).join(':');
  };
  const handleStart = () => setIsRunning(true);
  const handlePause = () => setIsRunning(false);
  const handleReset = () => {
    setIsRunning(false);
    setTime(0);
  };
  const handleViewDetails = () => setIsDetailView(true);
  const handleSave = () => {
    onUpdateTask({ title, description: taskDescription });
    setIsDetailView(false);
  };
  return (
    <div className="bg-blanc-glace rounded-lg shadow-md p-4 flex flex-col space-y-4 h-full transition-all duration-300 ease-in-out">
      <h2 className="text-xl font-bold text-bleu-nuit border-2 border-bleu-nuit rounded p-2 text-center">
        {title}
      </h2>
      {isDetailView ? (
        <>
          <textarea
            className="flex-grow p-2 border-2 border-ciel-nuageux rounded resize-none transition-all duration-300 ease-in-out"
            value={taskDescription}
            onChange={(e) => setTaskDescription(e.target.value)}
            placeholder="Entrez la description de la tâche..."
          />
          <button 
            onClick={handleSave}
            className="bg-rouge-vif text-blanc-glace px-4 py-2 rounded hover:bg-rouge-ruby transition-colors"
          >
            Sauvegarder
          </button>
        </>
      ) : (
        <>
          <button 
            onClick={handleViewDetails}
            className="text-ciel-nuageux hover:text-bleu-nuit transition-colors"
          >
            Voir les détails
          </button>
          <div className="text-3xl font-mono text-bleu-nuit text-center">
            {formatTime(time)}
          </div>
          <div className="flex justify-between mt-auto">
            <button 
              onClick={handleStart} 
              className="bg-rouge-vif text-blanc-glace px-4 py-2 rounded hover:bg-rouge-ruby transition-colors"
            >
              Démarrer
            </button>
            <button 
              onClick={handlePause} 
              className="bg-ciel-nuageux text-bleu-nuit px-4 py-2 rounded hover:bg-blanc-glace transition-colors"
            >
              Pause
            </button>
            <button 
              onClick={handleReset} 
              className="bg-bleu-nuit text-blanc-glace px-4 py-2 rounded hover:bg-ciel-nuageux transition-colors"
            >
              Réinitialiser
            </button>
          </div>
        </>
      )}
    </div>
  );
};
export default TodoItem;
```

Maintenant, créons un nouveau composant racine qui utilise nos composants :

> *Générer un App.jsx qui utilise* ***@Header.jsx***\*,\* ***@TodoItem.jsx***\*,\* ***@TodoContainer.jsx***\*, et\* ***@Footer.jsx*** *de manière appropriée. Utiliser des variables JavaScript simples comme données d'état et implémenter toutes les fonctions pertinentes. Avoir un minimum de 5 éléments de tâche.*

```javascript

// ./src/App.jsx
import React, { useState } from 'react';
import Header from './components/Header';
import TodoContainer from './components/TodoContainer';
import TodoItem from './components/TodoItem';
import Footer from './components/Footer';
const App = () => {
  const [todos, setTodos] = useState([
    { id: 1, title: 'Terminer la proposition de projet', description: 'Rédiger et finaliser la proposition de projet pour la réunion avec le client.' },
    { id: 2, title: 'Revoir les modifications de code', description: 'Passer en revue les demandes de tirage et fournir des commentaires sur les modifications de code.' },
    { id: 3, title: 'Préparer la présentation', description: 'Créer des diapositives pour la prochaine présentation de réunion d'équipe.' },
    { id: 4, title: 'Mettre à jour la documentation', description: 'Revoir et mettre à jour la documentation du projet avec les changements récents.' },
    { id: 5, title: 'Réunion d'équipe', description: 'Assister à la synchronisation hebdomadaire de l'équipe et discuter de l'avancement du projet.' },
  ]);
  const handleUpdateTask = (updatedTask) => {
    setTodos(todos.map(todo => 
      todo.id === updatedTask.id ? { ...todo, ...updatedTask } : todo
    ));
  };
  return (
    <div className="flex flex-col min-h-screen">
      <Header />
      <main className="flex-grow">
        <TodoContainer>
          {todos.map(todo => (
            <TodoItem 
              key={todo.id}
              title={todo.title}
              description={todo.description}
              onUpdateTask={(updatedTask) => handleUpdateTask({ id: todo.id, ...updatedTask })}
            />
          ))}
        </TodoContainer>
      </main>
      <Footer />
    </div>
  );
};
export default App;
```

Voici ce que nous avons maintenant :

![Capture d'écran de l'application web avec les composants TodoList et TodoItem](https://cdn.hashnode.com/res/hashnode/image/upload/v1726667940335/69911f3c-063b-40cc-80d6-27fd7b5aaa76.png align="center")

## Comment améliorer et gérer des bases de code existantes avec Cody

Pour augmenter encore votre productivité, Cody offre des [invites](https://sourcegraph.com/docs/cody/capabilities/commands#prompts) et des [commandes](https://sourcegraph.com/docs/cody/capabilities/commands#commands).

Vous pouvez enregistrer les invites fréquemment utilisées pour une utilisation future et les partager avec d'autres membres de votre organisation. Les commandes offrent des raccourcis prêts à l'emploi pour des tâches de codage courantes comme l'écriture, la description, la correction et l'identification des problèmes de code.

### **Ajoutons de la documentation à notre code !**

Tout d'abord, sélectionnez le code pour lequel vous souhaitez générer de la documentation, nous utiliserons `TodoItem.jsx` pour cet exemple. Exécutez la commande **Documenter le code**, et nous obtenons une chaîne de documentation JSDoc pour la classe du composant Footer.

![Ajout de documentation au code](https://cdn.hashnode.com/res/hashnode/image/upload/v1726668014952/8c65682a-d931-46df-bf49-df447df74443.png align="center")

### **Rendons nos composants plus accessibles et inclusifs**

Nous pouvons enregistrer nos invites de chat préférées et fréquemment utilisées dans la [**Bibliothèque d'invites**](https://sourcegraph.com/prompts/new) via l'interface Web de Sourcegraph.

Créons une nouvelle invite pour améliorer l'accessibilité de notre application web et nous assurer qu'elle respecte la [norme WCAG](https://www.w3.org/WAI/standards-guidelines/wcag/).

![Création d'une nouvelle invite dans la Bibliothèque d'invites](https://cdn.hashnode.com/res/hashnode/image/upload/v1726668303154/a83398cb-90b7-4d28-9c8b-a15b4751366c.png align="center")

Nous pouvons maintenant utiliser cette invite dans VS Code.

![Utilisation de notre nouvelle invite dans VS Code](https://cdn.hashnode.com/res/hashnode/image/upload/v1726668369322/5279315d-283f-4d24-9a8d-62316f7ec3b4.png align="center")

Ci-dessus, vous pouvez voir les résultats de notre invite d'accessibilité.

### Comment utiliser l'IA de manière responsable pour la génération de code

Les outils d'IA peuvent considérablement accélérer votre flux de travail, mais il est essentiel de se rappeler que l'IA est encore en développement. Aussi puissants que ces outils puissent être, ils peuvent également faire des erreurs ou "halluciner", produisant du code qui semble correct mais qui ne fonctionne pas réellement dans votre contexte spécifique.

Pour utiliser l'IA de manière responsable pour le codage, il est crucial de l'aborder avec une compréhension de ce qui doit être fait. Avant de vous appuyer sur l'IA, assurez-vous d'avoir une bonne compréhension de la tâche à accomplir. L'IA fonctionne mieux lorsqu'elle est utilisée comme un booster de productivité plutôt que comme un remplacement de votre expertise.

Voici quelques points clés à garder à l'esprit lorsque vous travaillez avec du code généré par l'IA :

* **Vérifiez le code** : Exécutez et testez toujours le code généré par l'IA. Même s'il semble correct à première vue, il pourrait y avoir des erreurs subtiles ou des inefficacités. C'est votre responsabilité de vous assurer que le code est fonctionnel et répond aux exigences de votre projet.

* **Comprenez le résultat** : Avant d'utiliser un code suggéré par l'IA, prenez le temps de comprendre comment il fonctionne. Cela vous permettra d'identifier rapidement les erreurs et d'intégrer le code efficacement avec le reste de votre projet.

Lorsque l'IA est utilisée de manière réfléchie et prudente, elle peut rendre votre processus de développement plus efficace et vous aider à vous concentrer sur des tâches de niveau supérieur. Cependant, il est essentiel d'équilibrer son utilisation avec une supervision humaine pour garantir la qualité et l'exactitude du code que vous construisez.

## Prochaines étapes

Créer des interfaces utilisateur conviviales a traditionnellement été chronophage et difficile à gérer. Mais en utilisant Cody, nous avons créé une interface utilisateur interactive et attrayante avec un effort minimal. Cody nous a soutenus tout au long du processus de développement.

Voici quelques améliorations potentielles que vous pouvez apporter :

* Nous ne pouvons pas créer ou supprimer de tâches. Essayez de corriger cela.

* Développez un composant pour afficher le nombre total de tâches et les heures accumulées.

* Ajoutez des cas de test pour chaque composant. Nous pouvons le faire rapidement en utilisant la commande **Générer des tests unitaires**.

Si vous avez apprécié apprendre à connaître Cody, vous pouvez essayer plus de ses fonctionnalités et applications. [Inscrivez-vous pour un compte gratuit](https://sourcegraph.com/cody) et boostez votre productivité en concevant, créant, documentant et gérant des applications.

### Lectures complémentaires

Si vous souhaitez en savoir plus, vous pouvez lire cet article sur la programmation orientée chat (CHOP) et comment utiliser Cody pour cela : [Programmation orientée chat (CHOP) en action](https://sourcegraph.com/blog/chat-oriented-programming-in-action).