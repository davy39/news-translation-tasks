---
title: Rendu conditionnel React – Expliqué avec des exemples de BBC Sports
subtitle: ''
author: Rufai Mustapha
co_authors: []
series: null
date: '2023-04-04T00:23:29.000Z'
originalURL: https://freecodecamp.org/news/react-conditional-rendering
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/poster--1-.jpg
tags:
- name: React
  slug: react
seo_title: Rendu conditionnel React – Expliqué avec des exemples de BBC Sports
seo_desc: "Conditional rendering is a powerful tool for creating dynamic and engaging\
  \ user interfaces in React applications. \nYou can use it to control what content\
  \ is rendered and when, and it improves user experience, simplifies your code, and\
  \ helps you creat..."
---

Le rendu conditionnel est un outil puissant pour créer des interfaces utilisateur dynamiques et engageantes dans les applications React.

Vous pouvez l'utiliser pour contrôler le contenu rendu et quand, ce qui améliore l'expérience utilisateur, simplifie votre code et vous aide à créer des composants plus flexibles et adaptables.

### Exemple de code

* Le code de cet article peut être trouvé [ici](https://github.com/rufai/bbcquiz/tree/master/src).
* Les exemples utilisés dans cet article sont inspirés de [The 100 Premier League Goals Quiz](https://bbc.com/sport/football/61202500) sur la BBC.

### Prérequis

Avant d'apprendre le rendu des composants React, il est important d'avoir une compréhension de base de HTML, CSS et JavaScript.

* Vous devez également avoir une compréhension de base de React lui-même, y compris ses concepts fondamentaux tels que l'état, les props et les méthodes de cycle de vie.
* De plus, il est important de comprendre le concept de DOM virtuel et son fonctionnement dans React, car il est étroitement lié au rendu des composants.

### Ce que vous apprendrez dans cet article

* Comment retourner différents JSX en fonction d'une condition.
* Comment inclure ou exclure conditionnellement un morceau de JSX.
* Raccourcis de syntaxe conditionnelle courants que vous rencontrerez dans le code React.

### À propos des démonstrations

Dans chaque démonstration que vous verrez ci-dessous :

* Je montre la vidéo de démonstration de ce que je vais vous montrer comment créer,
* puis je montre le code qui réalise ce qui est dans la vidéo,
* et enfin, j'explique le code.

## Table des matières

1. [Qu'est-ce que le rendu conditionnel React](#heading-quest-ce-que-le-rendu-conditionnel-react) ?

* Définir le rendu conditionnel React et comment il fonctionne
* Pourquoi le rendu conditionnel est nécessaire dans les applications React

2. [Comment implémenter le rendu conditionnel React](#heading-comment-implementer-le-rendu-conditionnel-react)

* L'opérateur ternaire et l'opérateur `&&`
* Exemples de code pour chaque méthode

3. [Comment gérer l'état de l'application pour le rendu conditionnel](#heading-comment-gerer-letat-de-lapplication-pour-le-rendu-conditionnel)

* Comment l'état de l'application peut être utilisé pour contrôler quand le contenu est rendu.
* Comment utiliser le hook `useState` pour gérer l'état pour le rendu conditionnel.
* Démo 1 - Connexion Déconnexion
* Démo 2 - Bouton Comment Jouer

4. [Avancé : Comment utiliser les props pour provoquer le rendu conditionnel React](#heading-avance-comment-utiliser-les-props-pour-provoquer-le-rendu-conditionnel-react)

* Rendu des composants en fonction des props
* Démo 3 - Composant ABC
* Démo 4 - Démarrer le Quiz

5. [Lectures complémentaires](#heading-lectures-complementaires)

## Qu'est-ce que le rendu conditionnel React ?

Dans React, le rendu conditionnel est le processus d'affichage de différents contenus en fonction de certaines conditions ou états. Il vous permet de créer des interfaces utilisateur dynamiques qui peuvent s'adapter aux changements de données et aux interactions utilisateur.

Dans ce processus, vous pouvez utiliser des instructions conditionnelles pour décider quel contenu doit être rendu.

### Pourquoi le rendu conditionnel est nécessaire dans les applications React

Il y a plusieurs raisons pour lesquelles vous pourriez vouloir utiliser le rendu conditionnel dans vos applications React :

1. Expérience utilisateur améliorée : Le rendu conditionnel vous permet de créer des interfaces utilisateur dynamiques qui s'adaptent aux changements de données et aux interactions utilisateur. En affichant et masquant le contenu en fonction des actions de l'utilisateur ou de l'état de l'application, vous pouvez créer une expérience utilisateur plus intuitive et engageante.
2. Performance améliorée : En rendant conditionnellement le contenu, vous pouvez éviter de rendre des composants inutiles et améliorer les performances de votre application. Cela est particulièrement important dans les applications plus grandes où le rendu inutile peut entraîner des problèmes de performance.
3. Code simplifié : Le rendu conditionnel peut vous aider à simplifier votre code et à le rendre plus lisible. En utilisant des instructions conditionnelles pour décider quel contenu doit être rendu, vous pouvez éviter de dupliquer le code et créer des composants plus modulaires.
4. Flexibilité : Le rendu conditionnel vous permet de créer des composants plus flexibles et personnalisables. En rendant différents contenus en fonction de l'état de l'application, vous pouvez créer des composants qui peuvent être utilisés dans différents contextes et s'adapter à différentes interactions utilisateur.

## Comment implémenter le rendu conditionnel React

Dans React, il existe différentes façons de rendre conditionnellement le contenu en fonction de l'état d'un composant ou d'autres conditions. Deux méthodes courantes sont l'utilisation de l'opérateur ternaire et de l'opérateur `&&`.

```js
function Greeting(props) {
  const isLoggedIn = props.isLoggedIn;
  return (
    <div>
      {isLoggedIn ? (
        <h1>Bienvenue !</h1>
      ) : (
        <h1>Veuillez vous inscrire.</h1>
      )}
    </div>
  );
}
```

Dans le code ci-dessus, nous avons utilisé l'opérateur ternaire `isLoggedIn ? ... : ...` pour rendre conditionnellement le message en fonction de si l'utilisateur est connecté ou non.

```js
function Greeting(props) {
  const isLoggedIn = props.isLoggedIn;
  return (
    <div>
      {isLoggedIn && <h1>Bienvenue !</h1>}
    </div>
  );
}

```

Dans le code ci-dessus, nous avons utilisé l'opérateur `&&` pour rendre conditionnellement le message si `isLoggedIn` est `true`.

Ces deux méthodes sont efficaces pour rendre conditionnellement le contenu dans React. Celle à utiliser dépend souvent de la préférence personnelle ou du cas d'utilisation spécifique.

L'opérateur ternaire peut être plus utile lorsqu'il y a plusieurs conditions à vérifier, tandis que l'opérateur `&&` peut être plus simple et plus concis lorsqu'il n'y a qu'une seule condition.

## Comment gérer l'état de l'application pour le rendu conditionnel

Dans React, l'état de l'application peut être utilisé pour contrôler quand et comment le contenu est rendu. L'état de l'application est un dépôt central de données utilisé par l'application pour rendre l'interface utilisateur. Lorsque l'état de l'application change, React ré-affiche les composants qui dépendent de cet état.

Une façon d'utiliser l'état de l'application pour contrôler le rendu est de rendre conditionnellement les composants en fonction de l'état. Par exemple, si vous avez un composant qui ne doit être affiché que lorsqu'une certaine condition est remplie, vous pouvez utiliser l'état de l'application pour contrôler quand le composant est rendu.

Une autre façon d'utiliser l'état de l'application pour contrôler le rendu est de passer des variables d'état aux composants enfants sous forme de props. Cela permet aux composants enfants de rendre le contenu en fonction de l'état du composant parent.

Voici un exemple de la façon dont vous pouvez utiliser l'état de l'application pour contrôler le rendu dans React :

### Démo 1 - Connexion Déconnexion

%[https://youtu.be/y0Dpte_sDKU]

```js
import React, { useState } from "react";

const App = () => {
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  const handleLogin = () => {
    setIsLoggedIn(true);
  };

  const handleLogout = () => {
    setIsLoggedIn(false);
  };

  return (
    <div>
      {isLoggedIn ? (
        <div>
          <h1>Bienvenue !</h1>
          <button onClick={handleLogout}>Déconnexion</button>
        </div>
      ) : (
        <div>
          <h1>Veuillez vous connecter</h1>
          <button onClick={handleLogin}>Connexion</button>
        </div>
      )}
    </div>
  );
};

export default App;

```

Dans cet exemple, nous avons un composant `App` qui rend différents contenus en fonction de l'état isLoggedIn. Initialement, `isLoggedIn` est défini sur false en utilisant le hook useState.

Lorsque l'utilisateur clique sur le bouton "Connexion", la fonction `handleLogin` est appelée, ce qui définit l'état `isLoggedIn` sur `true`. De même, lorsque l'utilisateur clique sur le bouton "Déconnexion", la fonction `handleLogout` est appelée, ce qui définit l'état `isLoggedIn` sur `false`.

L'instruction `return` du composant `App` utilise un opérateur ternaire pour rendre différents contenus en fonction de la valeur de `isLoggedIn`. Si `isLoggedIn` est `true`, il rend un message de bienvenue et un bouton "Déconnexion". Si `isLoggedIn` est `false`, il rend un message demandant à l'utilisateur de se connecter ainsi qu'un bouton "Connexion".

Cet exemple démontre comment vous pouvez utiliser le rendu conditionnel pour créer des interfaces utilisateur dynamiques qui peuvent s'adapter aux changements de l'état de l'application.

En utilisant le hook `useState` pour gérer l'état `isLoggedIn` et des instructions conditionnelles pour décider quel contenu doit être rendu, nous pouvons créer un système de connexion/déconnexion simple qui change le contenu de la page en fonction du statut d'authentification de l'utilisateur.

### Démo 2 - Construire un bouton Comment Jouer

%[https://youtu.be/0dGhpmNAb8A]



![Image](https://www.freecodecamp.org/news/content/images/2023/04/toplay.JPG)
_Structure de dossier pour le composant Comment Jouer_

```js
import React, { useState } from "react";

import "./style.css";

const HowToPlay = () => {
  const [showRules, setShowRules] = useState(false);

  const toggleRules = () => {
    setShowRules(!showRules);
  };

  return (
    <div>
      <button className="flat-black-button" onClick={toggleRules}>
        Comment Jouer
      </button>
      {showRules ? (
        <div>
          <p className="flat-black-button-content">
            Pour commencer, cliquez sur 'Démarrer'. Une fois que vous avez commencé le quiz,
            tapez une réponse dans la boîte et appuyez sur entrée ou cliquez sur le bouton soumettre.
            Si vous avez raison, il remplira la case correcte dans le tableau.
            Continuez à entrer plus de réponses jusqu'à ce que vous ayez réussi à compléter le quiz
            ou que le temps soit écoulé. Si vous ne voulez plus jouer, cliquez simplement sur le bouton 'Abandonner !'.
            Vous pouvez ensuite révéler les réponses que vous avez manquées ou réessayer.
          </p>
        </div>
      ) : null}
    </div>
  );
};

export default HowToPlay;

```

Ce composant affiche un bouton "Comment Jouer" et montre les instructions du jeu lorsque le bouton est cliqué.

Décomposons le code :

* Nous utilisons le hook `useState` pour créer une variable d'état `showRules` et sa fonction de définition `setShowRules`, initialisée à `false`. Cet état bascule l'affichage des instructions du jeu lorsque le bouton est cliqué.
* La fonction `toggleRules` est appelée lorsque le bouton "Comment Jouer" est cliqué, ce qui bascule l'état `showRules` en utilisant `setShowRules`.
* L'instruction `return` affiche le bouton "Comment Jouer" en utilisant un élément bouton, qui a un nom de classe "flat-black-button". Il affiche également conditionnellement les instructions du jeu si `showRules` est `true`.
* Nous affichons les instructions du jeu en utilisant un élément paragraphe, qui a un nom de classe "flat-black-button-content".
* Enfin, nous exportons le composant `HowToPlay` comme exportation par défaut du module.

Vous pouvez utiliser ce composant dans d'autres parties de l'application où le bouton "Comment Jouer" est nécessaire. Lorsque le bouton est cliqué, les instructions du jeu seront affichées ou masquées en fonction de l'état actuel de `showRules`.

## Avancé : Comment utiliser les props pour provoquer le rendu conditionnel React


![Image](https://www.freecodecamp.org/news/content/images/2023/04/Group-8.jpg)
_Les composants A, B et C sont des enfants de App_

Le diagramme ci-dessus montre comment un composant parent nommé "App" communique, indiqué par une ligne noire, avec ses composants enfants, A, B et C.

Le composant A doit communiquer avec les composants B et C, il envoie donc un message, indiqué par la ligne rouge, à App en utilisant "props". App transmet ensuite ce message à B et C en utilisant leurs propres "props".

### Démo 3 - Composant ABC

%[https://youtu.be/nAv0ksWYfls]

```js
import "./App.css";

import React, { useState } from "react";

function App() {
  return (
    <div>
      <A />
    </div>
  );
}

function A() {
  const [showB, setShowB] = useState(false);
  const [showC, setShowC] = useState(false);
  const [text, setText] = useState("");

  const handleInputChange = (event) => {
    setText(event.target.value);
    setShowB(true);
    setShowC(true);
  };

  return (
    <div className="App">
      <input type="text" onChange={handleInputChange} />
      {showB && <B text={text} />}
      {showC && <C text={text} />}
    </div>
  );
}

function B(props) {
  const { text } = props;
  return <h1>Composant B - {text.toUpperCase()}</h1>;
}

function C(props) {
  const { text } = props;
  return <h1>Composant C - {text.toLowerCase()}</h1>;
}

export default App;

```

Dans cet exemple, le composant `A` a trois variables d'état : `showB`, `showC` et `text`. Lorsque la valeur du champ de saisie change, la fonction `handleInputChange` est appelée et, en fonction de la valeur du champ de saisie, la variable d'état `text` est mise à jour et les variables d'état `showB` et `showC` sont définies sur `true`.

Les composants `B` et `C` sont des composants fonctionnels qui reçoivent la prop `text` en entrée et rendent le texte de différentes manières – le composant `B` rend le texte en majuscules, tandis que le composant `C` rend le texte en minuscules.

L'opérateur `&&` est utilisé pour rendre conditionnellement les composants en fonction de leurs variables d'état respectives.

Voyons comment ce concept est utilisé dans une application produit.

### Démo 4 - Démarrer le Quiz

La Démo 4 est une autre version du dernier exemple.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Group-9.jpg)
_Cliquer sur le bouton StartQuiz déclenchera le Timer et remplira le PlayerNameTable_

Lorsque l'utilisateur clique sur le bouton "StartQuiz", un Timer commence à compter à rebours, et un signal est envoyé pour remplir le PlayerNameTable.

%[https://youtu.be/QM9b69PfVjE]

### Composant Timer

```js
import React, { useEffect } from "react";
import { useTimer } from "react-timer-hook";

const Timer = ({ expiryTimestamp, shouldTimerStart }) => {
  const { seconds, minutes, start, reset } = useTimer({
    expiryTimestamp,
    autoStart: false,
  });
  useEffect(() => {
    if (shouldTimerStart) {
      start();
    }
  }, [shouldTimerStart]);

  return (
    <div>
      {minutes}:{seconds < 10 ? `0${seconds}` : seconds}
    </div>
  );
};

export default Timer;

```

Ceci est un composant React qui utilise le hook `useTimer` de la bibliothèque `react-timer-hook` pour créer un compte à rebours. Décomposons-le :

1. Importer les dépendances nécessaires : `React` et `useTimer` de la bibliothèque `react-timer-hook`.
2. Définir le composant `Timer`, qui prend deux props : `expiryTimestamp` et `shouldTimerStart`.
3. Déstructurer les propriétés `seconds`, `minutes`, `start` et `reset` du hook `useTimer`. Le hook `useTimer` prend un objet d'options avec une propriété `expiryTimestamp` qui spécifie le moment où le timer doit expirer, et une propriété `autoStart` qui spécifie si le timer doit démarrer automatiquement lorsque le composant est monté.
4. Utiliser le hook `useEffect` pour démarrer le timer lorsque `shouldTimerStart` change. Le hook `useEffect` prend une fonction de rappel qui s'exécute après chaque rendu, et un tableau de dépendances qui détermine quand la fonction de rappel doit s'exécuter. Dans ce cas, la fonction de rappel s'exécute chaque fois que `shouldTimerStart` change.
5. Rendre le timer en utilisant les propriétés `minutes` et `seconds`, avec une instruction conditionnelle qui ajoute un zéro initial aux secondes lorsqu'elles sont inférieures à 10.
6. Exporter le composant Timer comme exportation par défaut du module.

### PlayerNameTable

```js
import React, { useState, useEffect } from "react";

import "./style.css";

const PlayerNameTable = ({ trigger }) => {
  const data = require("../data/League100.json");
  console.log(data);

  const [shouldShowData, updateShouldShowData] = useState(false);

  useEffect(() => {
    if (trigger) {
      updateShouldShowData(trigger);
    }
  }, [trigger]);

  return (
    <table>
      <thead>
        <tr>
          <th>Rang</th>
          <th>Buts</th>
          <th>Clubs</th>
          <th>Joueur</th>
        </tr>
      </thead>
      <tbody>
        {shouldShowData ? (
          data.sort().map((player, index) => (
            <tr key={index}>
              <td>{index + 1}</td>
              <td>{player.goals}</td>
              <td>{player.clubs}</td>
              {/* <td>{player.name || player.player}</td> */}
            </tr>
          ))
        ) : (
          <tr>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
          </tr>
        )}
      </tbody>
    </table>
  );
};

export default PlayerNameTable;

```

Ceci est un composant React qui rend un tableau de la Premier League. Décomposons-le :

1. Importer les dépendances nécessaires : `React`, `useState` et `useEffect`.
2. Importer le fichier `style.css`, qui contient probablement des styles CSS pour le tableau.
3. Définir le composant `PlayerNameTable`, qui prend une prop : `trigger`.
4. Charger les données pour le tableau de la Premier League à partir d'un fichier JSON en utilisant `require`. Les données JSON contiennent des informations sur les joueurs, y compris leur rang, le nombre de buts, le club et le nom.
5. Utiliser le hook `useState` pour définir une variable d'état `shouldShowData`, qui détermine si les données doivent être affichées dans le tableau ou non. Par défaut, elle est définie sur `false`.
6. Utiliser le hook `useEffect` pour mettre à jour la variable d'état `shouldShowData` chaque fois que la prop `trigger` change. Cela permet au composant parent de contrôler quand les données sont affichées dans le tableau.
7. Rendre le tableau en utilisant les éléments HTML `table`, `thead`, `tbody` et `tr`, ainsi que les éléments `th` et `td` pour les en-têtes et les cellules de données du tableau.
8. Utiliser une instruction conditionnelle pour déterminer si les données ou un tableau vide doivent être affichés. Si `shouldShowData` est `true`, trier le tableau `data` par rang et mapper dessus pour rendre les données de chaque joueur sous forme de ligne de tableau. Si `shouldShowData` est `false`, rendre une ligne de tableau vide.
9. Exporter le composant `PlayerNameTable` comme exportation par défaut du module.

### StartQuiz

```js
import React, { useState } from "react";
import "./style.css";

function Quiz({ trigger }) {
  const [isStarted, setIsStarted] = useState(false);
  const [answer, setAnswer] = useState("");

  const handleStartClick = () => {
    setIsStarted(true);
    trigger(true);
  };

  const handleResetClick = () => {
    setIsStarted(false);
    trigger(false);
  };

  const handleSubmitClick = () => {
    // Faire quelque chose avec la réponse, par exemple la valider
  };

  return (
    <div>
      {isStarted ? (
        <div>
          <input
            type="text"
            value={answer}
            onChange={(e) => setAnswer(e.target.value)}
          />
          <button className="submit-button" onClick={handleSubmitClick}>
            Soumettre
          </button>
          <button className="reset-button" onClick={handleResetClick}>
            Réinitialiser
          </button>
        </div>
      ) : (
        <button className="start-button" onClick={handleStartClick}>
          Démarrer le Quiz
        </button>
      )}
    </div>
  );
}

export default Quiz;

```

Ceci est un composant React qui représente un quiz simple. Voici ce qu'il fait :

1. Importer les dépendances nécessaires : `React` et `useState`.
2. Importer le fichier `style.css`, qui contient probablement des styles CSS pour le quiz.
3. Définir le composant `Quiz`, qui prend une prop : `trigger`.
4. Utiliser le hook `useState` pour définir deux variables d'état : `isStarted`, qui détermine si le quiz a été démarré ou non, et `answer`, qui stocke la réponse de l'utilisateur à la question du quiz.
5. Définir trois fonctions pour gérer les événements utilisateur : `handleStartClick`, `handleResetClick` et `handleSubmitClick`.
6. Dans la fonction `handleStartClick`, définir la variable d'état `isStarted` sur `true` et déclencher la prop `trigger` pour informer le composant parent que le quiz a démarré.
7. Dans la fonction `handleResetClick`, définir la variable d'état `isStarted` sur `false` et déclencher la prop `trigger` pour informer le composant parent que le quiz a été réinitialisé.
8. Dans la fonction `handleSubmitClick`, faire quelque chose avec la réponse de l'utilisateur, comme la valider par rapport à la bonne réponse.
9. Dans l'instruction `return`, rendre le quiz en fonction de s'il a été démarré ou non. Si `isStarted` est `true`, rendre un champ de saisie pour la réponse de l'utilisateur, ainsi qu'un bouton "Soumettre" et un bouton "Réinitialiser". Si `isStarted` est `false`, rendre un bouton "Démarrer le Quiz".
10. Exporter le composant `Quiz` comme exportation par défaut du module.

### Composant Parent App

```js
import "./App.css";

import HowToPlay from "./HowToPlay";
import ScoreCounter from "./ScoreCounter";
import Timer from "./Timer";
import Table from "./Rank";
import PremierLeagueTable from "./Rank/index2";
import Quiz from "./Quiz";

import { useState, useEffect } from "react";

function App() {
  const [hasQuizStarted, updateHasQuizStarted] = useState(null);

  function startTimer(status) {
    updateHasQuizStarted(status);
  }

  const time = new Date();
  time.setSeconds(time.getSeconds() + 300);
  return (
    <div className="App">
      <h1>Pouvez-vous nommer les joueurs avec 100 buts en Premier League ?</h1>
      <HowToPlay></HowToPlay>
      <div className="place_edges">
        <ScoreCounter></ScoreCounter>
        <Timer expiryTimestamp={time} shouldTimerStart={hasQuizStarted}></Timer>
      </div>
      <Quiz trigger={startTimer}></Quiz>
      <PremierLeagueTable trigger={hasQuizStarted}></PremierLeagueTable>
    </div>
  );
}

export default App;

```

Application React qui rend un quiz pour les joueurs de Premier League avec 100 buts. L'application inclut des composants pour afficher les instructions, suivre le score et le temps, et rendre le quiz et le tableau des joueurs de Premier League.

La fonction startTimer est passée en tant que prop au composant Quiz, qui est appelée lorsque l'utilisateur démarre le quiz. Cela met à jour l'état de la variable hasQuizStarted, qui est ensuite passée aux composants Timer et PremierLeagueTable pour démarrer le timer et rendre le tableau des joueurs.

## Lectures complémentaires

Le rendu conditionnel est un concept important dans React qui vous permet de rendre différents contenus en fonction d'une certaine condition. Voici quelques ressources qui peuvent vous aider à mieux comprendre le rendu conditionnel dans React :

1. Documentation officielle de React sur le rendu conditionnel : [https://react.dev/learn/conditional-rendering](https://react.dev/learn/conditional-rendering)
2. "Conditional Rendering in React" par Robin Wieruch : [https://www.robinwieruch.de/conditional-rendering-react](https://www.robinwieruch.de/conditional-rendering-react)