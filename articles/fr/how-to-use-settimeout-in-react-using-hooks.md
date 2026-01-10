---
title: Comment utiliser setTimeout dans React avec les Hooks
subtitle: ''
author: Joan Ayebola
co_authors: []
series: null
date: '2023-12-06T23:37:13.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-settimeout-in-react-using-hooks
coverImage: https://www.freecodecamp.org/news/content/images/2023/12/Blue
seo_title: Comment utiliser setTimeout dans React avec les Hooks
---

white-company-profile-presentation--1-.png
étiquettes:
- nom: React
  slug: react
- nom: react hooks
  slug: react-hooks
seo_title: null
seo_desc: "React s'est imposé comme une bibliothèque JavaScript puissante et largement utilisée pour\
  \ construire des interfaces utilisateur. Son architecture basée sur les composants permet aux développeurs de\
  \ créer un code modulaire et réutilisable, facilitant la gestion et la maintenance des applications complexes. \nSur..."
---

React s'est imposé comme une bibliothèque JavaScript puissante et largement utilisée pour construire des interfaces utilisateur. Son architecture basée sur les composants permet aux développeurs de créer un code modulaire et réutilisable, facilitant la gestion et la maintenance des applications complexes. 

Une exigence courante dans les projets de développement web est la capacité de retarder l'exécution de certaines tâches. C'est là que `setTimeout` entre en jeu. 

Considérez des scénarios où vous souhaitez créer des transitions fluides, afficher des indicateurs de chargement ou implémenter des animations. Dans ces cas, retarder l'exécution d'actions spécifiques vous permet de contrôler le timing des éléments visuels, offrant une interface plus polie et conviviale.

Dans cet article, nous explorerons comment utiliser `setTimeout` dans React, spécifiquement avec les React Hooks. Les React Hooks sont des fonctions qui vous permettent d'utiliser l'état et d'autres fonctionnalités de React dans des composants fonctionnels. Si vous êtes nouveau dans les React Hooks ou si vous souhaitez simplement en apprendre davantage sur l'utilisation efficace de `setTimeout`, vous êtes au bon endroit.

Voici ce que nous allons couvrir:

1. [Comment fonctionne `setTimeout` ?](#heading-comment-fonctionne-settimeout)
2. [Configurer un projet React](#heading-installation-dun-projet-react)
3. [Comment utiliser `setTimeout` dans les composants fonctionnels](#heading-comment-utiliser-settimeout-dans-les-composants-fonctionnels)
4. [Comment gérer les interactions utilisateur avec `setTimeout`](#heading-comment-gerer-les-interactions-utilisateur-avec-settimeout)
5. [Comment gérer les retards dynamiques avec `setTimeout`](#heading-comment-gerer-les-retards-dynamiques-avec-settimeout)
6. [Comment gérer plusieurs `setTimeout` en séquence](#heading-comment-gerer-plusieurs-settimeout-en-sequence)
7. [Comment gérer plusieurs `setTimeout` dans les opérations asynchrones](#heading-comment-gerer-plusieurs-settimeout-dans-les-operations-asynchrones)
8. [Comment annuler les fonctions `setTimeout`](#heading-comment-annuler-les-fonctions-settimeout)
9. [Comment utiliser `setTimeout` avec les Promesses](#heading-comment-utiliser-settimeout-avec-les-promesses)
10. [Comment utiliser `setTimeout` avec `async/await`](#heading-comment-utiliser-settimeout-avec-asyncawait)
11. [Conclusion](#heading-conclusion)

## Comment fonctionne `setTimeout` ?

Avant de plonger dans l'utilisation de `setTimeout` dans une application React, comprenons brièvement ce qu'est `setTimeout` et comment il fonctionne en JavaScript.

`setTimeout` est une fonction JavaScript intégrée qui vous permet de planifier l'exécution d'une fonction après une durée spécifiée. Sa syntaxe de base ressemble à ceci:

```javascript
setTimeout(callback, delay);

```

* `callback`: Une fonction à exécuter après le délai spécifié.
* `delay`: Le temps (en millisecondes) à attendre avant d'exécuter la fonction de rappel.

Par exemple, le fragment de code suivant affichera "Bonjour le monde!" dans la console après un délai de 2000 millisecondes (2 secondes):

```javascript
setTimeout(() => {
  console.log("Bonjour le monde!");
}, 2000);

```

Maintenant que nous avons une compréhension de base de `setTimeout`, voyons comment nous pouvons l'intégrer avec React en utilisant les Hooks.

## Installation d'un projet React

Pour suivre les exemples de cet article, vous aurez besoin d'une compréhension de base de React et de Node.js installé sur votre machine. 

Pour ceux qui sont déjà familiers avec la configuration d'un projet React, vous pouvez sauter les étapes suivantes. Sinon, vous pouvez créer un nouveau projet React en utilisant Create React App avec les commandes suivantes (ou utiliser l'outil de construction de votre choix):

```bash
npx create-react-app mon-application-react
cd mon-application-react
npm start


```

Remplacez "mon-application-react" par le nom de projet de votre choix. La commande `npm start` lance le serveur de développement, et vous pouvez accéder à votre application React à l'adresse `http://localhost:3000`.

## Comment utiliser `setTimeout` dans les composants fonctionnels

Dans React, les composants fonctionnels sont un moyen léger de définir des composants d'interface utilisateur. Avec l'introduction des Hooks dans React 16.8, les composants fonctionnels peuvent maintenant utiliser l'état et d'autres fonctionnalités qui étaient auparavant exclusives aux composants de classe. 

Commençons par créer un composant fonctionnel simple et utiliser `setTimeout` à l'intérieur.

Ouvrez le fichier `src/App.js` et remplacez son contenu par le code suivant:

```jsx
import React, { useState, useEffect } from 'react';

const MessageRetarde = () => {
  const [message, setMessage] = useState('');

  useEffect(() => {
    // Utilisez setTimeout pour mettre à jour le message après 2000 millisecondes (2 secondes)
    const timeoutId = setTimeout(() => {
      setMessage('Message retardé après 2 secondes!');
    }, 2000);

    // Fonction de nettoyage pour effacer le timeout si le composant est démonté
    return () => clearTimeout(timeoutId);
  }, []); // Tableau de dépendances vide garantit que l'effet ne s'exécute qu'une seule fois

  return (
    <div>
      <h1>{message}</h1>
    </div>
  );
};

function App() {
  return (
    <div className="App">
      <MessageRetarde />
    </div>
  );
}

export default App;

```

Dans cet exemple, nous avons créé un composant fonctionnel appelé `MessageRetarde`. À l'intérieur de ce composant, nous utilisons le hook `useState` pour gérer l'état de la variable `message`. Le hook `useEffect` est utilisé pour gérer les effets secondaires, tels que les opérations asynchrones, dans les composants fonctionnels.

À l'intérieur du hook `useEffect`, nous utilisons `setTimeout` pour mettre à jour l'état `message` après un délai de 2000 millisecondes. Nous fournissons également une fonction de nettoyage utilisant `clearTimeout` pour nous assurer que le timeout est effacé si le composant est démonté avant la fin du timeout.

Maintenant, lorsque vous exécutez votre application React (`npm start`), vous devriez voir le message "Message retardé après 2 secondes!" affiché à l'écran après un bref délai.

## Comment gérer les interactions utilisateur avec `setTimeout`

Dans l'exemple précédent, nous avons exploré un scénario où `setTimeout` était utilisé pour simuler une action retardée déclenchée par un clic sur un bouton. Bien que cela démontre l'utilisation de base de `setTimeout` en réponse à une interaction utilisateur, il est essentiel de souligner l'importance de la validation des entrées utilisateur dans les applications réelles.

```jsx
import React, { useState } from 'react';

const ActionRetardee = () => {
  const [statutAction, setStatutAction] = useState('Inactif');
  const [dureeRetard, setDureeRetard] = useState(3000);

  const gererClicBouton = () => {
    setStatutAction('Action en cours...');

    // Utilisez setTimeout pour simuler une action retardée
    setTimeout(() => {
      setStatutAction('Action terminée!');
    }, dureeRetard);
  };

  return (
    <div>
      <p>Statut: {statutAction}</p>
      <button onClick={gererClicBouton}>Déclencher l'action retardée</button>
      <input
        type="number"
        value={dureeRetard}
        onChange={(e) => setDureeRetard(parseInt(e.target.value, 10))}
      />
    </div>
  );
};

export default ActionRetardee;

```

### Importance de la validation des entrées utilisateur

Dans les scénarios où l'entrée utilisateur influence directement le comportement de `setTimeout` ou d'autres opérations liées au temps, la validation de cette entrée devient cruciale. Ne pas valider l'entrée utilisateur peut entraîner un comportement inattendu, des erreurs potentielles ou même des vulnérabilités de sécurité.

Dans le fragment de code ci-dessus, nous avons un champ de saisie qui permet aux utilisateurs de spécifier la durée du retard en millisecondes. Il est essentiel de noter que la fonction `setDureeRetard` est enveloppée avec `parseInt` pour s'assurer que l'entrée est convertie en un entier valide. Cette étape aide à prévenir les problèmes découlant de valeurs d'entrée non numériques ou négatives.

```jsx
<input
  type="number"
  value={dureeRetard}
  onChange={(e) => setDureeRetard(parseInt(e.target.value, 10))}
/>

```

En validant l'entrée utilisateur, vous pouvez vous assurer que la durée du retard reste dans les limites attendues, atténuant le risque de comportement inattendu. 

Incorporer des pratiques de validation des entrées est un aspect fondamental de la construction d'applications React robustes et sécurisées, en particulier lorsqu'il s'agit d'opérations asynchrones liées aux actions des utilisateurs.

## Comment gérer les retards dynamiques avec `setTimeout`

Dans certains cas, vous pouvez vouloir définir dynamiquement la durée du retard en fonction de certaines conditions ou de l'entrée utilisateur. Modifions l'exemple précédent pour permettre aux utilisateurs de saisir la durée du retard via un champ de texte.

Mettez à jour le fichier `src/App.js` avec le code suivant:

```jsx
import React, { useState } from 'react';

const ActionRetardDynamique = () => {
  const [statutAction, setStatutAction] = useState('Inactif');
  const [dureeRetard, setDureeRetard] = useState(3000);

  const gererClicBouton = () => {
    setStatutAction('Action en cours...');

    // Utilisez setTimeout avec une durée de retard définie dynamiquement
    setTimeout(() => {
      setStatutAction('Action terminée!');
    }, dureeRetard);
  };

  const gererChangementSaisie = (e) => {
    const valeur = parseInt(e.target.value, 10);
    setDureeRetard(isNaN(valeur) ? 0 : valeur); // Définir dureeRetard à 0 si NaN
  };

  return (
    <div>
      <h2>Statut de l'action: {statutAction}</h2>
      <label>
        Durée du retard (millisecondes):
        <input type="text" value={dureeRetard} onChange={gererChangementSaisie} />
      </label>
      <button onClick={gererClicBouton}>Déclencher l'action retardée</button>
    </div>
  );
};

function App() {
  return (
    <div className="App">
      <ActionRetardDynamique />
    </div>
  );
}

export default

 App;

```

Dans cet exemple, nous avons introduit un champ de texte pour permettre aux utilisateurs de saisir la durée du retard en millisecondes. La variable d'état `dureeRetard` est mise à jour en fonction de l'entrée utilisateur, et la fonction `gererChangementSaisie` garantit que l'entrée est un entier valide.

La fonction `gererClicBouton` utilise ensuite `setTimeout` avec la durée de retard définie dynamiquement. Les utilisateurs peuvent maintenant spécifier la durée du retard via le champ de texte, leur donnant le contrôle sur le moment où l'action sera terminée.

**Note:** Bien que l'utilisation de `setTimeout` avec des retards définis dynamiquement offre de la flexibilité, il est essentiel d'être conscient des implications potentielles sur les performances. Lorsque les retards sont fréquemment mis à jour en fonction de l'entrée utilisateur ou d'autres facteurs dynamiques, cela peut entraîner une fréquence plus élevée de création et de destruction de temporisateurs.

La création et l'effacement excessifs de temporisateurs peuvent avoir un impact sur les performances globales de votre application, surtout si les retards sont très courts. Envisagez d'optimiser votre code ou d'explorer des approches alternatives, telles que le débogage de l'entrée utilisateur ou l'utilisation d'un mécanisme de planification plus sophistiqué, si vous rencontrez des problèmes de performance.

## Comment gérer plusieurs `setTimeout` en séquence

Dans certains scénarios, vous pourriez avoir besoin d'exécuter plusieurs fonctions `setTimeout` en séquence, créant une chaîne d'actions retardées. Explorons comment y parvenir en créant un composant qui affiche un compte à rebours avec plusieurs étapes.

Mettez à jour le fichier `src/App.js` avec le code suivant:

```jsx
import React, { useState, useEffect } from 'react';

const CompteARebours = () => {
  const [compteARebours, setCompteARebours] = useState(5);

  useEffect(() => {
    const intervalCompteARebours = setInterval(() => {
      // Diminuer la valeur du compte à rebours chaque seconde
      setCompteARebours((prevCompteARebours) => prevCompteARebours - 1);
    }, 1000);

    // Fonction de nettoyage pour effacer l'intervalle lorsque le composant est démonté
    return () => clearInterval(intervalCompteARebours);
  }, []); // Tableau de dépendances vide garantit que l'effet ne s'exécute qu'une seule fois

  useEffect(() => {
    // Utilisez setTimeout pour réinitialiser le compte à rebours lorsqu'il atteint 0
    if (compteARebours === 0) {
      setTimeout(() => {
        setCompteARebours(5); // Réinitialiser le compte à rebours à 5 secondes
      }, 2000); // Délai avant la réinitialisation (2 secondes)
    }
  }, [compteARebours]); // L'effet est réexécuté chaque fois que compteARebours change

  return (
    <div>
      <h2>Compte à rebours: {compteARebours}</h2>
    </div>
  );
};

function App() {
  return (
    <div className="App">
      <CompteARebours />
    </div>
  );
}

export default App;

```

Dans cet exemple, nous avons créé un composant `CompteARebours` qui affiche une valeur de compte à rebours. Le compte à rebours commence à 5 et diminue de 1 chaque seconde en utilisant `setInterval`. Lorsque le compte à rebours atteint 0, une fonction `setTimeout` est utilisée pour réinitialiser le compte à rebours à 5 après un délai de 2000 millisecondes (2 secondes).

Le point clé ici est l'utilisation de plusieurs hooks `useEffect`. Le premier `useEffect` initialise l'intervalle de compte à rebours, et la fonction de nettoyage garantit que l'intervalle est effacé lorsque le composant est démonté. Le deuxième `useEffect` surveille l'état `compteARebours` et déclenche la réinitialisation du compte à rebours lorsqu'il atteint 0.

En exécutant l'application, vous observerez le compte à rebours se réinitialiser à 5 après avoir atteint 0, créant une séquence cyclique d'actions retardées.

## Comment gérer plusieurs `setTimeout` dans les opérations asynchrones

L'utilisation de plusieurs hooks `useEffect` est cruciale pour gérer les actions asynchrones de manière contrôlée. Chaque hook `useEffect` sert un objectif spécifique.

**Initialisation du compte à rebours**: Le premier `useEffect` initialise l'intervalle de compte à rebours en utilisant `setInterval`. En ayant un `useEffect` dédié à cette initialisation, nous nous assurons que l'intervalle est configuré une seule fois lorsque le composant est monté. La fonction de nettoyage associée à ce `useEffect` efface l'intervalle lorsque le composant est démonté, empêchant les fuites de mémoire.

**Réinitialisation du compte à rebours**: Le deuxième `useEffect` surveille l'état `compteARebours` et déclenche la réinitialisation du compte à rebours lorsqu'il atteint 0. Cette séparation des préoccupations améliore la lisibilité et la maintenabilité du code. Si les deux fonctionnalités étaient combinées dans un seul `useEffect`, cela pourrait conduire à une structure de code moins organisée et plus difficile à comprendre.

L'utilisation de plusieurs hooks `useEffect` avec des responsabilités ciblées favorise une meilleure organisation du code et facilite la compréhension du comportement asynchrone dans votre composant. 

Considérez un composant de diaporama où chaque image est affichée pendant une durée spécifique avant de passer à la suivante. En enchaînant plusieurs fonctions `setTimeout`, vous pouvez créer une expérience de diaporama fluide et automatisée pour les utilisateurs.

```jsx
const demarrerDiaporama = () => {
  setTimeout(() => {
    // Afficher la première image
  }, 0);

  setTimeout(() => {
    // Afficher la deuxième image après un délai
  }, 3000);

  setTimeout(() => {
    // Afficher la troisième image après un délai
  }, 6000);
  // ...
};

```

Ce modèle d'exécution séquentielle vous permet d'orchestrer le timing de différentes actions, offrant une expérience utilisateur plus contrôlée et organisée.

## Comment annuler les fonctions `setTimeout`

Annuler une fonction `setTimeout` est essentiel pour prévenir les comportements non intentionnels, surtout lorsqu'il s'agit de retards dynamiques ou de démontage de composants. La fonction `clearTimeout` peut être utilisée pour annuler un timeout planifié.

Considérez l'exemple suivant où un timeout est défini pour mettre à jour un message après un délai:

```jsx
import React, { useState, useEffect } from 'react';

const MessageRetarde = () => {
  const [message, setMessage] = useState('');

  useEffect(() => {
    const timeoutId = setTimeout(() => {
      setMessage('Message retardé après 2 secondes!');
    }, 2000);

    // Fonction de nettoyage pour effacer le timeout si le composant est démonté
    return () => clearTimeout(timeoutId);
  }, []); // Tableau de dépendances vide garantit que l'effet ne s'exécute qu'une seule fois

  return (
    <div>
      <h1>{message}</h1>
    </div>
  );
};

export default MessageRetarde;

```

Dans cet exemple, la fonction `clearTimeout` est utilisée dans la fonction de nettoyage du hook `useEffect`. Si le composant est démonté avant la fin du timeout, la fonction de nettoyage garantit que le timeout est effacé, empêchant la mise à jour de l'état sur un composant démonté.

## Comment utiliser `setTimeout` avec les Promesses

La fonction `setTimeout` de JavaScript peut être combinée avec les Promesses pour créer un code asynchrone plus lisible et flexible. La fonction `setTimeout` elle-même ne retourne pas une Promesse, mais nous pouvons l'envelopper dans une Promesse pour utiliser la syntaxe `async/await`.

Considérez l'exemple suivant:

```jsx
const delai = (millisecondes) => new Promise(resolve => setTimeout(resolve, millisecondes));

const fonctionExemple = async () => {
  console.log('Début');
  await delai(2000);
  console.log('Après 2 secondes');
};

fonctionExemple();

```

Dans cet exemple, la fonction `delai` retourne une Promesse qui se résout après le nombre de millisecondes spécifié. La fonction `fonctionExemple` utilise `async/await` pour attendre que le délai soit terminé avant de passer à l'étape suivante. Ce modèle est particulièrement utile lorsqu'il s'agit d'opérations asynchrones impliquant des timeouts.

## Comment utiliser `setTimeout` avec `async/await`

Combiner `setTimeout` avec `async/await` permet d'écrire un code asynchrone plus propre et plus lisible. Bien que `setTimeout` lui-même ne retourne pas directement une Promesse, nous pouvons l'envelopper dans une Promesse pour attendre le délai.

Considérez l'exemple suivant:

```jsx
const delai = (millisecondes) => new Promise(resolve => setTimeout(resolve, millisecondes));

const fonctionExemple = async () => {
  console.log('Début');
  await delai(2000);
  console.log('Après 2 secondes');
};

fonctionExemple();

```

Dans cet exemple, la fonction `delai` retourne une Promesse qui se résout après le nombre de millisecondes spécifié. La fonction `fonctionExemple` utilise `async/await` pour attendre que le délai soit terminé avant de passer à l'étape suivante. 

Ce modèle est particulièrement utile lorsqu'il s'agit d'opérations asynchrones impliquant des timeouts.

## Conclusion

Dans ce guide, nous avons couvert les bases de l'utilisation de `setTimeout` dans une application React en utilisant des composants fonctionnels et les React Hooks. 

Nous avons commencé par un exemple simple d'affichage d'un message retardé et avons progressivement exploré des scénarios plus complexes, y compris la gestion des interactions utilisateur, la définition dynamique des durées de retard et l'enchaînement de plusieurs fonctions `setTimeout` en séquence.

Comprendre comment utiliser `setTimeout` efficacement dans React peut améliorer votre capacité à créer des interfaces utilisateur réactives et interactives. En combinant la puissance des React Hooks avec `setTimeout`, vous pouvez implémenter divers comportements asynchrones de manière propre et maintenable.

Alors que vous continuez votre parcours dans le développement React, envisagez d'explorer d'autres React Hooks et des concepts JavaScript supplémentaires pour élargir vos compétences. Bon codage!