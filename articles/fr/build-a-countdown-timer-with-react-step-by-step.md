---
title: Comment créer un compte à rebours avec React – Un guide étape par étape
subtitle: ''
author: Franklin Ohaegbulam
co_authors: []
series: null
date: '2024-10-14T13:38:55.761Z'
originalURL: https://freecodecamp.org/news/build-a-countdown-timer-with-react-step-by-step
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1724788718279/35a8ba3c-db35-49b6-ae41-14bcda547795.png
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: reactjs
- name: Web Development
  slug: web-development
- name: Tutorial
  slug: tutorial
- name: ReactHooks
  slug: reacthooks
seo_title: Comment créer un compte à rebours avec React – Un guide étape par étape
seo_desc: 'In this tutorial, you will learn how to build a custom countdown timer
  to track events using React.js.

  A countdown timer is a simple way to measure the time until an event happens. It
  counts down that time in reverse – like 5, 4, 3, 2, 1. It helps yo...'
---

Dans ce tutoriel, vous apprendrez à créer un compte à rebours personnalisé pour suivre des événements en utilisant React.js.

Un compte à rebours est un moyen simple de mesurer le temps jusqu'à ce qu'un événement se produise. Il compte à rebours ce temps à l'envers – comme 5, 4, 3, 2, 1. Il vous aide à gérer le temps précédant les événements à venir, les lancements de produits ou les offres, et vous permet d'informer les utilisateurs de ce calendrier.

### Table des matières

* [1\. Configurer votre application React](#heading-1-installation-de-votre-application-react)
    
* [2\. Créer le composant Count Down](#heading-2-creer-le-composant-count-down)
    
* [3\. Implémenter la gestion de l'état du temps et la fonctionnalité](#heading-3-implementer-la-gestion-de-letat-du-temps-et-la-fonctionnalite)
    
* [4\. Créer un formulaire de compte à rebours](#heading-4-creer-un-formulaire-de-compte-a-rebours)
    
* [5\. Gérer le démarrage, l'arrêt et la réinitialisation du compte à rebours](#heading-5-gerer-le-demarrage-larret-et-la-reinitialisation-du-compte-a-rebours)
    
* [6\. Formater la date et l'heure de l'événement](#heading-6-formater-la-date-et-lheure-de-levenement)
    
* [7\. Afficher le compte à rebours](#heading-7-afficher-le-compte-a-rebours)
    
* [8\. Styliser le composant du compte à rebours](#heading-8-styliser-le-composant-du-compte-a-rebours)
    
* [Conclusion](#heading-conclusion)
    

### Prérequis

Vous devez avoir une bonne connaissance de HTML, CSS et JavaScript pour tirer le meilleur parti de cet article.

Commençons.

## 1\. Configurer votre application React

Tout d'abord, vous devrez [créer une application React](https://www.freecodecamp.org/news/how-to-build-a-react-app-different-ways/#heading-what-is-vite) si vous n'en avez pas déjà une prête à l'emploi. Dans ce tutoriel, j'utilise Vite. Ensuite, changez le répertoire du nouveau projet en exécutant les commandes suivantes dans votre éditeur de code :

```bash
npm create vite countdown-timer

cd countdown-timer
```

Exécutez cette commande pour démarrer l'application sur le serveur local :

```bash
npm run dev
```

Maintenant, vous devriez voir le projet dans votre navigateur sur `https://localhost/3000`.

## 2\. Créer le composant Count Down

Dans le dossier `src` de votre application React, créez un répertoire `components`, et à l'intérieur, créez un fichier `CountDown.jsx`.

```javascript
/* components/CountDown.jsx */

import React from "react";

const CountdownTimer = () => {

  return (
    <div className="countdown-timer-container">
    </div>
  );
};

export default CountdownTimer;
```

## 3\. Implémenter la gestion de l'état du temps et la fonctionnalité

Définissez les variables d'état en utilisant le hook useState. Mettez à jour le fichier `CountDown.jsx` avec le code suivant :

```javascript
/* components/CountDown.jsx */

import React, { useState, useEffect } from "react";

const CountdownTimer = () => {
  const [eventName, setEventName] = useState("");
  const [eventDate, setEventDate] = useState("");
  const [countdownStarted, setCountdownStarted] = useState(false);
  const [timeRemaining, setTimeRemaining] = useState(0);

 return (
    <div className="countdown-timer-container">
    </div>
  );
};

export default CountdownTimer;
```

Voici un bref aperçu de `useState` :

* `eventName` : stocke le nom de l'événement pour le compte à rebours.
    
* `eventDate` : stocke la date de l'événement pour le compte à rebours.
    
* `countdownStarted` : suit si le compte à rebours a commencé.
    
* `timeRemaining` : stocke le temps restant en millisecondes pour le compte à rebours.
    

Maintenant, nous allons implémenter la fonctionnalité du compte à rebours en utilisant le hook useEffect :

```javascript
/* components/CountDown.jsx */

import React, { useState, useEffect } from "react";

const CountdownTimer = () => {
  
    // ...

  useEffect(() => {
    if (countdownStarted && eventDate) {
      const countdownInterval = setInterval(() => {
        const currentTime = new Date().getTime();
        const eventTime = new Date(eventDate).getTime();
        let remainingTime = eventTime - currentTime;

        if (remainingTime <= 0) {
          remainingTime = 0;
          clearInterval(countdownInterval);
          alert("Compte à rebours terminé !");
        }

        setTimeRemaining(remainingTime);
      }, 1000);

      return () => clearInterval(countdownInterval);
    }
  }, [countdownStarted, eventDate, timeRemaining]);

 return (
    <div className="countdown-timer-container">
    </div>
  );
};

export default CountdownTimer;
```

Le hook `useEffect` s'exécute chaque fois que `countdownStarted` ou `eventDate` change. Il configure un intervalle qui met à jour `timeRemaining` chaque seconde en fonction de l'heure actuelle et de l'heure de l'événement. Si le temps restant devient inférieur ou égal à 0, il arrête l'intervalle et déclenche la notification "Compte à rebours terminé !".

```javascript
/* components/CountDown.jsx */

import React, { useState, useEffect } from "react";

const CountdownTimer = () => {
 
  // ...
  
  useEffect(() => {
    if (countdownStarted) {
      document.title = eventName;
    }
  }, [countdownStarted, eventName]);

 return (
    <div className="countdown-timer-container">
    </div>
  );
};

export default CountdownTimer;
```

Ici, le hook `useEffect` s'exécute chaque fois que `countdownStarted` ou `eventName` change. Il met à jour le titre du compte à rebours pour afficher le `eventName` lorsque le compte à rebours est démarré.

## 4\. Créer un formulaire de compte à rebours

Pour avoir le contrôle sur le compte à rebours, vous devrez créer un formulaire avec deux champs de saisie pour le nom et la date de l'événement. Ensuite, ajoutez le code suivant :

```javascript
/* components/CountDown.jsx */

import React from "react";

 // ...
 
   const handleSetCountdown = () => {
    setCountdownStarted(true);
  };

 return (
 <div className="countdown-timer-container">
      <h2 className="countdown-name">
        {countdownStarted ? eventName : "Compte à rebours"}
      </h2>

      {!countdownStarted ? (
        <form className="countdown-form">
          <label htmlFor="title">Nom de l'événement</label>
          <input
            name="title"
            type="text"
            placeholder="Entrez le nom de l'événement"
            value={eventName}
            onChange={(e) => setEventName(e.target.value)}
          />

          <label htmlFor="date-picker">Date de l'événement</label>
          <input
            name="date-picker"
            type="date"
            value={eventDate}
            onChange={(e) => setEventDate(e.target.value)}
            onClick={(e) => (e.target.type = "date")}
          />
          <button onClick={handleSetCountdown}>Démarrer le compte à rebours</button>
        </form>
      }
    </div>
  );
};

export default CountdownTimer;
```

Voici un bref aperçu de `useState` :

* `eventName` : stocke le nom de l'événement pour le compte à rebours.
    
* `countdown-name` : affiche "Compte à rebours" par défaut ou se met à jour avec le `eventName` saisi une fois le compte à rebours démarré.
    

Le formulaire inclut :

* Le champ de saisie avec le nom `title` et l'étiquette `Nom de l'événement` met à jour la valeur de l'état `eventName`.
    
* Le champ de saisie avec le nom `date-picker` permet aux utilisateurs de sélectionner une date et de contrôler la valeur de l'état `eventDate`.
    
* Le bouton `Démarrer le compte à rebours` déclenche la fonction `handleSetCountdown` lorsqu'il est cliqué pour initier le compte à rebours.
    

## 5\. Gérer le démarrage, l'arrêt et la réinitialisation du compte à rebours

Ensuite, mettez à jour la fonction `handleSetCountdown` pour stocker le nom et la date de l'événement dans le stockage local en utilisant `localStorage.setItem`. localStorage est une API web qui permet aux utilisateurs de stocker des données sous forme de paires clé-valeur de manière persistante, même lorsque le navigateur est fermé ou actualisé.

Le code est le suivant :

```javascript
/* components/CountDown.jsx */

import React from "react";

 // ...
 
    const handleSetCountdown = () => {
    setCountdownStarted(true);
    localStorage.setItem("eventDate", eventDate);
    localStorage.setItem("eventName", eventName);
  };

 return (
 <div className="countdown-timer-container">
       // ...
 </div>
  );
};

export default CountdownTimer;
```

Maintenant, créez les fonctions `handleStopCountdown` et `handleResetCountdown` pour arrêter le compte à rebours en mettant à jour l'état `countdownStarted` à `false`.

```javascript
/* components/CountDown.jsx */

import React from "react";

 // ...

  const handleStopCountdown = () => {
    setCountdownStarted(false);
    setTimeRemaining(0);
  };

  const handleResetCountdown = () => {
    setCountdownStarted(false);
    setEventDate("");
    setEventName("");
    setTimeRemaining(0);
    localStorage.removeItem("eventDate");
    localStorage.removeItem("eventName");
  };

 return (
 <div className="countdown-timer-container">
       // ...
       <div className="control-buttons">
            <button onClick={handleStopCountdown}>Arrêter</button>
            <button onClick={handleResetCountdown}>Réinitialiser</button>
        </div>
 </div>
  );
};

export default CountdownTimer;
```

Ici :

* `handleStopCountdown` : réinitialise l'état `timeRemaining` à zéro.
    
* `handleResetCountdown` : réinitialise le compte à rebours à son état initial. Il efface les états de temps restant et supprime la date de l'événement et le nom de l'événement du stockage local en utilisant `localStorage.removeItem()`.
    

## 6\. Formater la date et l'heure de l'événement

Convertissons les données de date et d'heure en un format lisible.

```javascript
/* components/CountDown.jsx */

import React from "react";

 // ...
 
  const formatDate = (date) => {
    const options = { month: "long", day: "numeric", year: "numeric" };
    return new Date(date).toLocaleDateString("fr-FR", options);
  };

  const formatTime = (time) => {
    const seconds = Math.floor((time / 1000) % 60);
    const minutes = Math.floor((time / (1000 * 60)) % 60);
    const hours = Math.floor((time / (1000 * 60 * 60)) % 24);
    const days = Math.floor(time / (1000 * 60 * 60 * 24));

    return (
      <div className="countdown-display">
        <div className="countdown-value">
          {days.toString().padStart(2, "0")} <span>jours</span>
        </div>
        <div className="countdown-value">
          {hours.toString().padStart(2, "0")} <span> heures</span>
        </div>
        <div className="countdown-value">
          {minutes.toString().padStart(2, "0")} <span>minutes</span>
        </div>
        <div className="countdown-value">
          {seconds.toString().padStart(2, "0")} <span>secondes</span>
        </div>
      </div>
    );
  };

 return (
 <div className="countdown-timer-container">
       // ...
 </div>
  );
};

export default CountdownTimer;
```

Voici un bref aperçu des fonctions :

* `formatDate` : formate la date d'entrée en une chaîne de date lisible par l'homme.
    
* `formatTime` : prend un temps en millisecondes en entrée et calcule les jours, heures, minutes et secondes du compte à rebours. La méthode `.toString().padStart(2, "0")` retourne le temps formaté en deux caractères en ajoutant un 0 au début du temps uniquement si la longueur du nombre est inférieure à 2.
    

Voici le contenu complet du fichier `CountDown.jsx` :

```javascript
 /* components/CountDown.jsx */

import React, { useState, useEffect } from "react";

const CountdownTimer = () => {
  const [eventName, setEventName] = useState("");
  const [eventDate, setEventDate] = useState("");
  const [countdownStarted, setCountdownStarted] = useState(false);
  const [timeRemaining, setTimeRemaining] = useState(0);

  useEffect(() => {
    if (countdownStarted && eventDate) {
      const countdownInterval = setInterval(() => {
        const currentTime = new Date().getTime();
        const eventTime = new Date(eventDate).getTime();
        let remainingTime = eventTime - currentTime;

        if (remainingTime <= 0) {
          remainingTime = 0;
          clearInterval(countdownInterval);
          alert("Compte à rebours terminé !");
        }

        setTimeRemaining(remainingTime);
      }, 1000);

      return () => clearInterval(countdownInterval);
    }
  }, [countdownStarted, eventDate, timeRemaining]);

  useEffect(() => {
    if (countdownStarted) {
      document.title = eventName;
    }
  }, [countdownStarted, eventName]);

  const handleSetCountdown = () => {
    setCountdownStarted(true);
    localStorage.setItem("eventDate", eventDate);
    localStorage.setItem("eventName", eventName);
  };

  const handleStopCountdown = () => {
    setCountdownStarted(false);
    setTimeRemaining(0);
  };

  const handleResetCountdown = () => {
    setCountdownStarted(false);
    setEventDate("");
    setEventName("");
    setTimeRemaining(0);
    localStorage.removeItem("eventDate");
    localStorage.removeItem("eventName");
  };

  const formatDate = (date) => {
    const options = { month: "long", day: "numeric", year: "numeric" };
    return new Date(date).toLocaleDateString("fr-FR", options);
  };

  const formatTime = (time) => {
    const seconds = Math.floor((time / 1000) % 60);
    const minutes = Math.floor((time / (1000 * 60)) % 60);
    const hours = Math.floor((time / (1000 * 60 * 60)) % 24);
    const days = Math.floor(time / (1000 * 60 * 60 * 24));

    return (
      <div className="countdown-display">
        <div className="countdown-value">
          {days.toString().padStart(2, "0")} <span>jours</span>
        </div>
        <div className="countdown-value">
          {hours.toString().padStart(2, "0")} <span> heures</span>
        </div>
        <div className="countdown-value">
          {minutes.toString().padStart(2, "0")} <span>minutes</span>
        </div>
        <div className="countdown-value">
          {seconds.toString().padStart(2, "0")} <span>secondes</span>
        </div>
      </div>
    );
  };

  return (
    <div className="countdown-timer-container">
      <h2 className="countdown-name">
        {countdownStarted ? eventName : "Compte à rebours"}
      </h2>
      <p className="countdown-date">
        {countdownStarted && formatDate(eventDate)}
      </p>

      {!countdownStarted ? (
        <form className="countdown-form">
          <label htmlFor="title">Nom de l'événement</label>
          <input
            name="title"
            type="text"
            placeholder="Entrez le nom de l'événement"
            value={eventName}
            onChange={(e) => setEventName(e.target.value)}
          />

          <label htmlFor="date-picker">Date de l'événement</label>
          <input
            name="date-picker"
            type="date"
            value={eventDate}
            onChange={(e) => setEventDate(e.target.value)}
            onClick={(e) => (e.target.type = "date")}
          />
          <button onClick={handleSetCountdown}>Démarrer le compte à rebours</button>
        </form>
      ) : (
        <>
          {formatTime(timeRemaining)}
          <div className="control-buttons">
            <button onClick={handleStopCountdown}>Arrêter</button>
            <button onClick={handleResetCountdown}>Réinitialiser</button>
          </div>
        </>
      )}
    </div>
  );
};

export default CountdownTimer;
```

## 7\. Afficher le compte à rebours

Importez `CountDownTimer` dans `App.jsx`, en remplaçant le code par défaut par ceci :

```javascript
 /* App.jsx */

import React from "react";
import CountdownTimer from "./components/CountDown";

function App() {
  return (
    <div className="App">
      <CountdownTimer />
    </div>
  );
}

export default App;
```

Et c'est tout ! Votre application de compte à rebours devrait être rendue sur `localhost:3000` dans le navigateur.

## 8\. Styliser le composant du compte à rebours

Enfin, mettez à jour le fichier `index.css` dans le même répertoire de votre projet en ajoutant les styles suivants :

```css
@import url("https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=Open+Sans:wght@400;500;700&display=swap");

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  background: url("./img/bg-img.jpg") top center;
  background-size: cover;
  background-repeat: no-repeat;
  background-attachment: fixed;
  font-family: "Inter", sans-serif;
  font-size: 1rem;
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  padding: 1rem;
}

.countdown-form {
  background-color: #f6f6f6;
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 1.5rem;
  width: 100%;
  max-width: 400px;
  border-radius: 12px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

label {
  font-weight: 600;
  margin-bottom: 0.5rem;
  color: #333;
}

input {
  background-color: #d1f1ee;
  border: 1px solid #dfdfdf;
  border-radius: 6px;
  outline: none;
  margin-bottom: 1rem;
  padding: 0.75rem;
  width: 100%;
  font-size: 1rem;
  transition: border-color 0.2s ease;
}

input:focus {
  border-color: #038a7f;
}

button {
  background-color: #038a7f;
  border: none;
  border-radius: 6px;
  color: #fff;
  cursor: pointer;
  outline: none;
  margin-top: 1rem;
  text-transform: uppercase;
  width: 100%;
  height: 2.75rem;
  font-weight: 600;
  letter-spacing: 0.5px;
  transition: background-color 0.2s ease;
}

button:hover {
  background-color: #005a53;
}

.countdown-message {
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: clamp(1.25rem, 4vw, 1.5rem);
  margin: 1rem 0;
}

.countdown-name {
  color: #fff;
  font-size: clamp(1.5rem, 5vw, 2rem);
  margin-bottom: 1rem;
  text-align: center;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
}

.countdown-date {
  color: #eafbfa;
  margin: 0 0 1.5rem;
  text-align: center;
  font-size: clamp(1rem, 3vw, 1.25rem);
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
}

.countdown-display {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(80px, 1fr));
  gap: 1rem;
  justify-content: center;
  padding: 0.5rem;
  max-width: 600px;
  margin: 0 auto;
}

.countdown-value {
  background-color: #2f5d6f;
  border-radius: 50%;
  color: #03d5c0;
  aspect-ratio: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 1rem;
  font-size: clamp(1.5rem, 5vw, 2.5rem);
  font-weight: 700;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
  transition: transform 0.2s ease;
}

.countdown-value:hover {
  transform: scale(1.05);
}

.countdown-value > span {
  color: #fff;
  font-size: clamp(0.75rem, 2vw, 0.875rem);
  letter-spacing: 1px;
  text-transform: uppercase;
  margin-top: 0.2rem;
  font-weight: 500;
}

.control-buttons {
  margin-top: 2rem;
  display: flex;
  justify-content: center;
  gap: 1rem;
  flex-wrap: wrap;
}

.control-buttons > button {
  background-color: #03b4a2;
  border-radius: 50%;
  width: clamp(45px, 8vw, 50px);
  height: clamp(45px, 8vw, 50px);
  margin: 0;
  padding: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: clamp(0.65rem, 2vw, 0.775rem);
}

.control-buttons button:hover {
  background-color: #0b7c71;
  transform: scale(1.1);
}

@media (max-width: 480px) {
  .countdown-display {
    grid-template-columns: repeat(2, 1fr);
    gap: 0.75rem;
  }

  .countdown-value {
    font-size: clamp(1.25rem, 4vw, 1.75rem);
  }

  .countdown-value > span {
    font-size: 0.75rem;
  }

  .control-buttons {
    margin-top: 1.5rem;
  }
}

@media (max-width: 360px) {
  body {
    padding: 0.75rem;
  }

  .countdown-form {
    padding: 1rem;
  }

  .countdown-name {
    font-size: 1.25rem;
  }

  .countdown-date {
    font-size: 1rem;
  }

  .control-buttons > button {
    width: 40px;
    height: 40px;
  }
}
```

Félicitations, vous avez terminé la création de votre application de compte à rebours !

## Conclusion

Dans cet article, vous avez appris à créer une application de compte à rebours basique avec React et à travailler avec le stockage local du navigateur.

Le code implémenté dans cet article est accessible dans ce [dépôt GitHub](https://github.com/frankiefab100/countdown-timer). Pour en savoir plus sur le développement web et la technologie, consultez mon [blog](https://frankiefab.hashnode.dev/) ou connectez-vous avec moi sur [X(Twitter)](https://twitter.com/frankiefab100) et [LinkedIn](https://linkedin.com/in/frankiefab100/).

Merci d'avoir lu cet article.