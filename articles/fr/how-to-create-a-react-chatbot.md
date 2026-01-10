---
title: Comment créer un chatbot React – un guide étape par étape
subtitle: ''
author: Tan Jin
co_authors: []
series: null
date: '2024-05-10T22:27:30.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-react-chatbot
coverImage: https://www.freecodecamp.org/news/content/images/2024/05/rcb-logo-large
seo_title: Comment créer un chatbot React – un guide étape par étape
---

Copy.png
tags:
- name: '#chatbots'
  slug: chatbots
- name: React
  slug: react
seo_title: null
seo_desc: "Dans le domaine en constante évolution des technologies web, l'intégration de chatbots alimentés par l'IA est devenue une tendance marquante en 2024. \nAvec les avancées rapides des grands modèles de langage (LLMs), les chatbots sont devenus des outils pivots adoptés sur de nombreux sites web et services. Des bots FAQ à l'assistance en direct, ils peuvent fournir aux utilisateurs des informations et de l'aide.\n"
---

Dans le domaine en constante évolution des technologies web, l'intégration de chatbots alimentés par l'IA est devenue une tendance marquante en 2024. 

Avec les avancées rapides des grands modèles de langage (LLMs), les chatbots sont devenus des outils pivots adoptés sur de nombreux sites web et services. Des bots FAQ à l'assistance en direct, ils peuvent fournir aux utilisateurs des informations et de l'aide.

Si vous avez un site web, une interface de chatbot élégante peut offrir du support à vos utilisateurs. Et vous voudrez présenter un chatbot moderne qui peut captiver vos utilisateurs et laisser une impression. 

React est l'un des outils les plus populaires pour développer des sites web, et les sites et applications alimentés par React sont de bons candidats pour les chatbots. Dans ce court guide, vous verrez à quel point il peut être facile d'intégrer un chatbot dans votre site web React.

## Prérequis

Avant de commencer à configurer notre chatbot, notez que ce guide suppose une connaissance des éléments suivants :

* [React](https://www.freecodecamp.org/news/react-for-beginners-handbook/)
* [Node.js/npm](https://www.freecodecamp.org/news/free-8-hour-node-express-course/)
* [Commandes Linux](https://www.freecodecamp.org/news/helpful-linux-commands-you-should-know/)

Une compréhension de base des éléments ci-dessus est suffisante, et vous devriez être en mesure de configurer votre propre projet React. Si vous n'êtes pas du tout familier avec les éléments ci-dessus, vous pouvez consulter les tutoriels liés (ainsi que toute autre ressource utile que vous trouvez) pour eux d'abord. Sinon, commençons !

## Étape 1 : Créer un projet

Avant de pouvoir configurer notre chatbot, créons un nouveau projet React vide. Rendez-vous dans un dossier de projet de votre choix et exécutez les commandes suivantes dans votre terminal :

```bash
npm create vite@latest
```

Vous serez invité à entrer un nom de projet, un framework et une variante. Pour les besoins de ce tutoriel, nous opterons pour les sélections suivantes :

* Nom du projet : MyChatBot
* Framework : React
* Variante : JavaScript

Une fois votre configuration terminée, rendez-vous dans votre dossier de projet et exécutez les commandes suivantes :

```bash
npm install && npm run dev
```

Si vous visitez _http://localhost:5173_ sur votre navigateur, vous devriez être accueilli avec l'écran suivant :

![Image](https://www.freecodecamp.org/news/content/images/2024/05/image-16.png)
_Application React configurée_

## Étape 2 : Installer React ChatBotify

Maintenant que nous avons notre projet configuré, il est temps d'installer [React ChatBotify](https://react-chatbotify.tjtanjin.com/). React ChatBotify est une bibliothèque React hautement personnalisable qui simplifie le processus d'intégration d'un chatbot dans votre application. Nous allons l'utiliser pour inclure un chatbot, alors installez-le avec la commande suivante :

```bash
npm install react-chatbotify
```

Une fois l'installation terminée, nous pouvons procéder à l'importation de la bibliothèque et à son rendu. Dans votre dossier `src`, ouvrez votre fichier `App.jsx` avec un éditeur de votre choix. Le fichier par défaut devrait ressembler à ceci :

```app.jsx
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

Ensuite, avec seulement deux lignes de code, nous verrons le chatbot rendu dans notre application. En haut de votre fichier, ajoutez la ligne :

* `import ChatBot from 'react-chatbotify'`

Au-dessus de votre élément `<div>` dans l'instruction `return`, ajoutez la ligne suivante :

* `<ChatBot/>`

Votre fichier modifié devrait ressembler à ceci :

```app.jsx
import ChatBot from 'react-chatbotify'
import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <ChatBot/>
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

Essayez de relancer votre application et vous serez accueilli avec un chatbot dans le coin inférieur droit comme montré dans la capture d'écran ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2024/05/image-17.png)
_Chatbot dans l'application React_

Plutôt sympa, n'est-ce pas ?

## Étape 3 : Créez votre message "Hello World"

C'est bien d'avoir le chatbot configuré facilement, mais ce n'est pas génial de n'avoir que le message de bienvenue par défaut. Ajoutons rapidement un message **hello world** à nous.

Le composant `<ChatBot/>` prend une prop `flow` pour définir les conversations. Par défaut, le point d'entrée d'une conversation est toujours nommé le bloc `start` comme montré dans cet exemple ci-dessous :

```
const flow = {
  "start": {
    "message": "Hello world!"
  }
}
```

Nous allons passer le flux ci-dessus dans notre chatbot :

```
import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import ChatBot from "react-chatbotify"
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  const flow = {
    "start": {
      "message": "Hello world!"
    }
  }
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
      <ChatBot flow={flow}/>
    </>
  )
}

export default App
```

Lorsque vous regardez à nouveau votre application, vous remarquerez que le message par défaut a disparu et est remplacé par `Hello world!` à la place. Pas trop difficile, n'est-ce pas ? 

## Conclusion

Dans ce guide, vous avez vu à quel point il peut être facile de configurer un chatbot React moderne. 

Bien que l'exemple ci-dessus soit simple, il existe de nombreuses autres propriétés dans un `flow` qui peuvent vous aider à construire vos conversations. Celles-ci sont documentées sur le [site web de la bibliothèque](https://react-chatbotify.tjtanjin.com/docs/introduction/quickstart) qui comprend également des [exemples de playground en direct](https://react-chatbotify.tjtanjin.com/docs/examples/basic_form) pour que vous puissiez explorer et en savoir plus.