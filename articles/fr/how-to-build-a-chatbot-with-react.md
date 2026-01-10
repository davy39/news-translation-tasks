---
title: Comment construire un chatbot avec React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-12T08:05:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-chatbot-with-react
coverImage: https://www.freecodecamp.org/news/content/images/2020/07/wooden-robot-6069-1.jpg
tags:
- name: '#chatbots'
  slug: chatbots
- name: React
  slug: react
seo_title: Comment construire un chatbot avec React
seo_desc: 'By Fredrik Strand Oseberg

  My philosophy is simple. To become good at something, you need to do it a lot.

  It''s not enough to do it once. You need to do it again, and again and again. It
  will never end. I used the same philosophy to get good at program...'
---

Par Fredrik Strand Oseberg

Ma philosophie est simple. Pour devenir bon dans quelque chose, il faut le faire souvent.

Une seule fois ne suffit pas. Il faut le faire encore et encore. Cela ne s'arrêtera jamais. J'ai utilisé la même philosophie pour devenir bon en programmation.

Une chose que j'ai remarquée durant ce parcours, c'est que c'est bien plus amusant de construire des choses intéressantes et qui ont l'air bien. Des choses que vous pouvez montrer à vos amis et dont vous pouvez être fier. Quelque chose qui vous donne envie de commencer lorsque vous vous asseyez devant votre clavier.

C'est pourquoi j'ai construit un chatbot. 

Qui s'est transformé en un [package npm](https://www.npmjs.com/package/react-chatbot-kit).

Alors construisons-en un ensemble. Si vous voulez relever ce défi par vous-même, vous pouvez aller directement à la [documentation (qui est en fait un chatbot)](https://fredrikoseberg.github.io/react-chatbot-kit-docs/). Ou, si vous êtes un apprenant visuel, [j'ai créé un tutoriel sur YouTube](https://youtu.be/vTpk-PKZwTs).

Sinon, c'est parti. Je vais supposer que vous avez Node installé et accès à la commande npx. Si ce n'est pas le cas, [allez le télécharger ici](https://nodejs.org/).

## Installation initiale

```
// Exécutez ces commandes depuis votre ligne de commande
npx create-react-app chatbot
cd chatbot
yarn add react-chatbot-kit
yarn start
```

Cela devrait installer le package npm et ouvrir le serveur de développement sur localhost:3000.

Ensuite, rendez-vous dans `App.js` et apportez ces modifications :

```jsx
import Chatbot from 'react-chatbot-kit'

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <Chatbot />
      </header>
    </div>
  );
}
```

Bon travail. Nous y sommes presque. Vous devriez voir ceci dans votre serveur de développement maintenant : 

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Screenshot-2020-06-10-at-16.03.51.png)

Le chatbot prend trois props qui doivent être incluses pour qu'il fonctionne. Tout d'abord, il a besoin d'une configuration qui doit inclure une propriété `initialMessages` avec des objets de messages du chatbot. 

Deuxièmement, il a besoin d'une classe `MessageParser` qui doit implémenter une méthode parse.

Troisièmement, il a besoin d'une classe `ActionProvider` qui implémentera des actions que nous voulons prendre en fonction de l'analyse du message. 

Nous approfondirons cela plus tard. Pour l'instant, [allez ici pour obtenir le code de base pour commencer](https://gist.github.com/FredrikOseberg/c1e8ec83ade6e89ca84882e33caf599c).

* Placez le code `MessageParser` dans un fichier appelé `MessageParser.js`
* Placez le code `ActionProvider` dans un fichier appelé `ActionProvider.js`
* Placez le code de configuration dans un fichier appelé `config.js`

Lorsque c'est fait, retournez à votre fichier `App.js` et ajoutez ce code :

```jsx
import React from 'react';
import Chatbot from 'react-chatbot-kit'
import './App.css';

import ActionProvider from './ActionProvider';
import MessageParser from './MessageParser';
import config from './config';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <Chatbot config={config} actionProvider={ActionProvider} 	    messageParser={MessageParser} />
      </header>
    </div>
  );
}
```

Vous devriez maintenant voir ceci sur localhost:3000 : 

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Screenshot-2020-06-10-at-16.16.57.png)

Super. Maintenant nous avons le chatbot rendu à l'écran et nous pouvons écrire dans le champ de saisie et l'envoyer pour envoyer un message au chat. Mais lorsque nous essayons cela, rien ne se passe.

## Comprendre comment fonctionne le chatbot

Ici, nous devons faire une pause et examiner comment le `MessageParser` et le `ActionProvider` interagissent pour faire agir notre bot.

Lorsque le bot est initialisé, la propriété `initialMessages` de la configuration est placée dans l'état interne du chatbot dans une propriété appelée `messages`, qui est utilisée pour rendre les messages à l'écran. 

De plus, lorsque nous écrivons et appuyons sur le bouton d'envoi dans le champ de chat, notre `MessageParser` (que nous avons passé en tant que props au chatbot) appelle sa méthode `parse`. C'est pourquoi cette méthode doit être implémentée. 

Examinons de plus près le code de démarrage du `MessageParser` :

```jsx
class MessageParser {
  constructor(actionProvider) {
    this.actionProvider = actionProvider;
  }

  parse(message) {
    ... parse logic
  }
}
```

Si nous regardons de près, cette méthode est construite avec un `actionProvider`. C'est la même classe `ActionProvider` que nous passons en tant que props au chatbot. Cela signifie que nous contrôlons deux choses - comment le message est analysé et quelle action prendre en fonction de cette analyse.

Utilisons ces informations pour créer une réponse simple de chatbot. Modifiez d'abord le `MessageParser` comme ceci :

```
class MessageParser {
  constructor(actionProvider) {
    this.actionProvider = actionProvider;
  }

  parse(message) {
    const lowerCaseMessage = message.toLowerCase()
    
    if (lowerCaseMessage.includes("hello")) {
      this.actionProvider.greet()
    }
  }
}

export default MessageParser
```

Maintenant, notre `MessageParser` reçoit le message de l'utilisateur, vérifie s'il inclut le mot "hello". Si c'est le cas, il appelle la méthode `greet` sur le `actionProvider`. 

Actuellement, cela provoquerait une erreur, car nous n'avons pas implémenté la méthode `greet`. Faisons cela ensuite. Rendez-vous dans `ActionProvider.js` :

```
class ActionProvider {
  constructor(createChatBotMessage, setStateFunc) {
    this.createChatBotMessage = createChatBotMessage;
    this.setState = setStateFunc;
  }
  
  greet() {
    const greetingMessage = this.createChatBotMessage("Hi, friend.")
    this.updateChatbotState(greetingMessage)
  }
  
  updateChatbotState(message) {
 // NOTE: This function is set in the constructor, and is passed in      // from the top level Chatbot component. The setState function here     // actually manipulates the top level state of the Chatbot, so it's     // important that we make sure that we preserve the previous state.
 
    
   this.setState(prevState => ({
    	...prevState, messages: [...prevState.messages, message]
    }))
  }
}

export default ActionProvider
```

Bien. Maintenant, si nous tapons "hello" dans le champ de chat, nous obtenons ceci en retour :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Screenshot-2020-06-10-at-16.39.48.png)

Fantastique. Maintenant que nous pouvons contrôler l'analyse du message et répondre avec une action, essayons de faire quelque chose de plus compliqué. Essayons de faire un bot qui vous fournit des ressources d'apprentissage pour le langage de programmation que vous demandez.

## Créer un bot d'apprentissage

Tout d'abord, retournons à notre fichier `config.js` et apportons quelques modifications :

```
import { createChatBotMessage } from 'react-chatbot-kit';

const config = { 
  botName: "LearningBot",
  initialMessages: [createChatBotMessage("Hi, I'm here to help. What do you want to learn?")],
  customStyles: {
    botMessageBox: {
      backgroundColor: "#376B7E",
    },
    chatButton: {
      backgroundColor: "#376B7E",
    },
  },
}

export default config
```

D'accord, nous avons ajouté quelques propriétés ici et changé notre message initial. Plus particulièrement, nous avons donné un nom au bot et changé la couleur des composants `messagebox` et `chatbutton`.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Screenshot-2020-06-22-at-09.44.33.png)

Très bien. Maintenant, nous arrivons à la bonne partie.

Non seulement nous pouvons analyser les messages et répondre à l'utilisateur avec un message de chatbot, mais nous pouvons également définir des composants React personnalisés que nous voulons rendre avec le message. Ces composants peuvent être tout ce que nous voulons - ce sont simplement de vieux composants React.

Essayons cela en créant un composant d'options qui guidera l'utilisateur vers les options possibles.

Tout d'abord, nous définissons le composant des options d'apprentissage :

```jsx
// in src/components/LearningOptions/LearningOptions.jsx

import React from "react";

import "./LearningOptions.css";

const LearningOptions = (props) => {
  const options = [
    { text: "Javascript", handler: () => {}, id: 1 },
    { text: "Data visualization", handler: () => {}, id: 2 },
    { text: "APIs", handler: () => {}, id: 3 },
    { text: "Security", handler: () => {}, id: 4 },
    { text: "Interview prep", handler: () => {}, id: 5 },
  ];

  const optionsMarkup = options.map((option) => (
    <button
      className="learning-option-button"
      key={option.id}
      onClick={option.handler}
    >
      {option.text}
    </button>
  ));

  return <div className="learning-options-container">{optionsMarkup}</div>;
};

export default LearningOptions;

// in src/components/LearningOptions/LearningOptions.css

.learning-options-container {
  display: flex;
  align-items: flex-start;
  flex-wrap: wrap;
}

.learning-option-button {
  padding: 0.5rem;
  border-radius: 25px;
  background: transparent;
  border: 1px solid green;
  margin: 3px;
}
```

Maintenant que nous avons notre composant, nous devons l'enregistrer avec notre chatbot. Rendez-vous dans `config.js` et ajoutez ce qui suit : 

```jsx
import React from "react";
import { createChatBotMessage } from "react-chatbot-kit";

import LearningOptions from "./components/LearningOptions/LearningOptions";

const config = {
initialMessages: [
    createChatBotMessage("Hi, I'm here to help. What do you want to 		learn?", {
      widget: "learningOptions",
    }),
  ],
 ...,
 widgets: [
     {
     	widgetName: "learningOptions",
    	widgetFunc: (props) => <LearningOptions {...props} />,
     },
 ],
}
```

### Comprendre les widgets

D'accord. Prenons une pause et explorons ce que nous avons fait.

1. Nous avons créé le composant `LearningOptions`.
2. Nous avons enregistré le composant sous `widgets` dans notre configuration.
3. Nous avons donné à la fonction `createChatbotMessage` un objet d'options spécifiant quel widget rendre avec ce message.

Le résultat : 

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Screenshot-2020-06-22-at-10.41.49.png)

Fantastique, mais pourquoi avons-nous dû enregistrer notre composant dans la configuration en tant que fonction de widget ? 

En lui donnant une fonction, nous contrôlons quand nous effectuons l'invocation. Cela nous laisse de la place pour décorer le widget avec des propriétés importantes à l'intérieur du chatbot. 

Le widget que nous définissons recevra un certain nombre de propriétés du chatbot (certaines peuvent être contrôlées par les propriétés de configuration) :

1. `actionProvider` - nous donnons le `actionProvider` au widget afin d'exécuter des actions si nécessaire.
2. `setState` - nous donnons la fonction `setState` de niveau supérieur du chatbot au widget au cas où nous aurions besoin de manipuler l'état.
3. `scrollIntoView` - fonction utilitaire pour faire défiler jusqu'au bas de la fenêtre de chat, si nous devons ajuster la vue.
4. `props` - si nous définissons des props dans la configuration du widget, celles-ci seront transmises au widget sous le nom de propriété `configProps`.
5. `state` - si nous définissons un état personnalisé dans la configuration, nous pouvons le mapper au widget en utilisant la propriété `mapStateToProps`

Si vous vous souvenez, nous avons défini certaines options dans le composant `LearningOptions` : 

```
  const options = [
    { text: "Javascript", handler: () => {}, id: 1 },
    { text: "Data visualization", handler: () => {}, id: 2 },
    { text: "APIs", handler: () => {}, id: 3 },
    { text: "Security", handler: () => {}, id: 4 },
    { text: "Interview prep", handler: () => {}, id: 5 },
  ];
```

Actuellement, ceux-ci ont un gestionnaire vide. Ce que nous voulons faire maintenant, c'est remplacer ce gestionnaire par un appel au `actionProvider`. 

Alors, que voulons-nous qu'il se passe lorsque nous exécutons ces fonctions ? Idéalement, nous aurions un message de chatbot, et un widget accompagnateur qui affiche une liste de liens vers des ressources utiles pour chaque sujet. Alors voyons comment nous pouvons implémenter cela.

Tout d'abord, nous devons créer le composant de liste de liens :

```jsx
// in src/components/LinkList/LinkList.jsx

import React from "react";

import "./LinkList.css";

const LinkList = (props) => {
  const linkMarkup = props.options.map((link) => (
    <li key={link.id} className="link-list-item">
      <a
        href={link.url}
        target="_blank"
        rel="noopener noreferrer"
        className="link-list-item-url"
      >
        {link.text}
      </a>
    </li>
  ));

  return <ul className="link-list">{linkMarkup}</ul>;
};

export default LinkList;

// in src/components/LinkList/LinkList.css

.link-list {
  padding: 0;
}

.link-list-item {
  text-align: left;
  font-size: 0.9rem;
}

.link-list-item-url {
  text-decoration: none;
  margin: 6px;
  display: block;
  color: #1d1d1d;
  background-color: #f1f1f1;
  padding: 8px;
  border-radius: 3px;
  box-shadow: 2px 2px 4px rgba(150, 149, 149, 0.4);
}
```

Super. Nous avons maintenant un composant qui peut afficher une liste de liens. Maintenant, nous devons l'enregistrer dans la section widget de la configuration :

```jsx
import React from "react";
import { createChatBotMessage } from "react-chatbot-kit";

import LearningOptions from "./components/LearningOptions/LearningOptions";
import LinkList from "./components/LinkList/LinkList";

const config = {
  ...
  widgets: [
    {
      widgetName: "learningOptions",
      widgetFunc: (props) => <LearningOptions {...props} />,
    },
    {
      widgetName: "javascriptLinks",
      widgetFunc: (props) => <LinkList {...props} />,
    },
  ],
};

export default config;

```

Jusqu'à présent, tout va bien, mais nous voulons passer dynamiquement des props à ce composant afin de pouvoir le réutiliser pour les autres options également. Cela signifie que nous devons ajouter une autre propriété à l'objet widget dans la configuration :

```jsx
import React from "react";
import { createChatBotMessage } from "react-chatbot-kit";

import LearningOptions from "./components/LearningOptions/LearningOptions";
import LinkList from "./components/LinkList/LinkList";

const config = {
  ...,
  widgets: [
    ...,
    {
      widgetName: "javascriptLinks",
      widgetFunc: (props) => <LinkList {...props} />,
      props: {
        options: [
          {
            text: "Introduction to JS",
            url:
              "https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/basic-javascript/",
            id: 1,
          },
          {
            text: "Mozilla JS Guide",
            url:
              "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide",
            id: 2,
          },
          {
            text: "Frontend Masters",
            url: "https://frontendmasters.com",
            id: 3,
          },
        ],
      },
    },
  ],
};

export default config;

```

Maintenant, ces props seront passées au composant `LinkList` en tant que props.

Maintenant, nous devons faire deux choses de plus. 

1. Nous devons ajouter une méthode à l'`actionProvider`

```jsx
class ActionProvider {
  constructor(createChatBotMessage, setStateFunc) {
    this.createChatBotMessage = createChatBotMessage;
    this.setState = setStateFunc;
  }

  handleJavascriptList = () => {
    const message = this.createChatBotMessage(
      "Fantastic, I've got the following resources for you on Javascript:",
      {
        widget: "javascriptLinks",
      }
    );

    this.updateChatbotState(message);
  };

  updateChatbotState(message) {
    // NOTICE: This function is set in the constructor, and is passed in from the top level Chatbot component. The setState function here actually manipulates the top level state of the Chatbot, so it's important that we make sure that we preserve the previous state.

    this.setState((prevState) => ({
      ...prevState,
      messages: [...prevState.messages, message],
    }));
  }
}

export default ActionProvider;

```

2.  Nous devons ajouter cette méthode en tant que gestionnaire dans le composant `LearningOptions` :

```jsx
import React from "react";

import "./LearningOptions.css";

const LearningOptions = (props) => {
  const options = [
    {
      text: "Javascript",
      handler: props.actionProvider.handleJavascriptList,
      id: 1,
    },
    { text: "Data visualization", handler: () => {}, id: 2 },
    { text: "APIs", handler: () => {}, id: 3 },
    { text: "Security", handler: () => {}, id: 4 },
    { text: "Interview prep", handler: () => {}, id: 5 },
  ];

  const optionsMarkup = options.map((option) => (
    <button
      className="learning-option-button"
      key={option.id}
      onClick={option.handler}
    >
      {option.text}
    </button>
  ));

  return <div className="learning-options-container">{optionsMarkup}</div>;
};

export default LearningOptions;

```

D'accord ! C'était beaucoup d'informations. Mais si nous essayons maintenant de cliquer sur l'option JavaScript dans le chatbot, nous obtenons ce résultat : 

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Screenshot-2020-06-22-at-17.35.27.png)

Parfait. Mais nous ne voulons pas nous arrêter là, c'est un chatbot après tout. Nous voulons pouvoir répondre aux utilisateurs qui veulent utiliser le champ de saisie également. Nous devons donc créer une nouvelle règle dans `MessageParser`.

Mettons à jour notre fichier `MessageParser.js` pour qu'il ressemble à ceci :

```jsx
class MessageParser {
  constructor(actionProvider) {
    this.actionProvider = actionProvider;
  }

  parse(message) {
    const lowerCaseMessage = message.toLowerCase();

    if (lowerCaseMessage.includes("hello")) {
      this.actionProvider.greet();
    }

    if (lowerCaseMessage.includes("javascript")) {
      this.actionProvider.handleJavascriptList();
    }
  }
}

export default MessageParser;

```

Maintenant, essayez de taper "javascript" dans le champ de saisie et envoyez le message. Vous devriez obtenir la même liste en réponse du chatbot.

Alors voilà. Nous avons mis en place un chatbot qui affiche une liste d'options possibles et répond à l'entrée de l'utilisateur. 

Pour l'instant, nous avons seulement configuré le bot pour gérer lorsque quelqu'un clique ou tape JavaScript, mais vous pouvez essayer d'étendre les autres options par vous-même. [Voici un lien vers le dépôt](https://github.com/FredrikOseberg/fcc-chatbot-example).

Tout le code est sur GitHub, alors n'hésitez pas à plonger dans [le code ou la documentation de react-chatbot-kit](https://github.com/FredrikOseberg/react-chatbot-kit).

## Conclusion

Construire des choses est amusant et une excellente façon d'élargir vos compétences. Il n'y a pas de limites à ce que vous pourriez faire ensuite. 

Peut-être pourriez-vous faire un chatbot qui trouve le produit idéal dans une boutique en ligne en fonction de quelques questions simples (en utilisant le routage dans l'application), ou peut-être pourriez-vous en faire un pour votre entreprise qui s'occupe des demandes les plus courantes des clients. 

N'hésitez pas à développer, à avoir de nouvelles idées et à les tester. Et si vous voyez quelque chose qui peut être amélioré, envoyez une pull request.

Si vous voulez vous améliorer en tant que développeur, je vous encourage à continuer à construire. C'est vraiment le seul chemin à suivre. Si vous avez aimé cet article et que vous aimeriez savoir quand je publie plus de contenu, vous pouvez [me suivre sur Twitter](https://twitter.com/foseberg).