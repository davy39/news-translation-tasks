---
title: Comment gérer les événements dans React – Expliqué avec des exemples de code
subtitle: ''
author: Matéu.sh
co_authors: []
series: null
date: '2024-05-13T09:26:31.000Z'
originalURL: https://freecodecamp.org/news/how-to-handle-events-in-react-19
coverImage: https://www.freecodecamp.org/news/content/images/2024/05/React-logo.png
tags:
- name: events
  slug: events
- name: React
  slug: react
seo_title: Comment gérer les événements dans React – Expliqué avec des exemples de
  code
seo_desc: "Event handling is fundamental to understanding how React processes browser\
  \ events and updates the DOM. As a React developer, it's a critical skill to have,\
  \ as it enables efficient management of user interactions within web apps.  \nThis\
  \ article covers..."
---

La gestion des événements est fondamentale pour comprendre comment React traite les événements du navigateur et met à jour le DOM. En tant que développeur React, c'est une compétence critique à avoir, car elle permet une gestion efficace des interactions utilisateur au sein des applications web.  
  
Cet article couvre la configuration des gestionnaires d'événements et aborde des techniques plus élégantes pour la gestion des événements. Vous apprendrez à créer des événements dans les composants React, à passer des arguments aux gestionnaires et à empêcher les comportements par défaut.  
  
Nous aborderons également les modèles courants de gestion des événements et les meilleures pratiques pour garantir que vos applications sont performantes et faciles à maintenir.

## Principes de base de la gestion des événements dans React

La gestion des événements dans React est guidée par quelques principes de base qui s'alignent avec son architecture basée sur les composants. Ces principes incluent :

* Système d'événements synthétiques
* Conventions de nommage
* Passage des gestionnaires d'événements en tant que props
* Fonctions en ligne et méthodes de composant

React utilise un système d'événements synthétiques qui garantit que les événements se comportent de manière cohérente sur différents navigateurs. Cela enveloppe le système d'événements natif des navigateurs, fournissant une API unifiée quel que soit le navigateur dans lequel React est exécuté.

Les conventions de nommage tournent autour d'un ensemble de noms cohérents que les développeurs utilisent pour identifier les événements et les fonctions de gestionnaire d'un seul coup d'œil. Chaque événement utilise une convention de nommage `camelCase`, et la fonction de gestionnaire qu'ils exécutent est préfixée par "handle", suivie du nom de l'événement. Par exemple, un événement `onClick` exécutant une fonction `handleClick`.

Les gestionnaires d'événements sont les fonctions qui s'exécutent lorsque l'événement est déclenché. Ils sont généralement définis avant le rendu, juste au-dessus de l'instruction return. À de nombreuses occasions, ils sont également passés en tant que `props` aux composants. Cela s'aligne avec l'architecture basée sur les composants de React, permettant d'intégrer la logique des événements dans les composants qui les utilisent.

Dans les composants React, les événements exécutent généralement des fonctions en ligne ou des fonctions autonomes au sein du composant lorsqu'ils sont déclenchés. Avec cela, vous pouvez utiliser des hooks comme `useState` pour l'état et `useCallback` pour mémoriser les fonctions de gestionnaire. Cela aide à gérer les changements d'état et à optimiser les performances.

## Comment créer des gestionnaires d'événements dans les composants React

Créer un événement dans React commence par attacher le nom de l'événement à l'élément qui va le déclencher, avec la fonction de gestionnaire référencée dedans :

```jsx
<button onClick={handleClick}>
  Cliquez-moi
</button>
```

Ce qui suit est de définir cette fonction de gestionnaire, car c'est la fonction qui s'exécutera lorsque l'événement sera déclenché :

```js
const handleClick = () => {
   alert('Vous avez cliqué sur moi');
};
```

Voici le code complet qui a été importé dans le fichier `page.jsx` d'un starter Next.js :

```jsx
'use client';

const Counter = () => {
 const handleClick = () => {
   alert('Vous avez cliqué sur moi !');
 };

 return (
   <div className="p-10 flex items-center">
     <button
       onClick={handleClick}
       className="bg-green-400 px-4 py-2 rounded mx-auto"
     >
       Cliquez-moi
     </button>
   </div>
 );
};

export default Counter;
```

Et voici ce qui s'affiche dans le navigateur lorsque le bouton est cliqué :

![Image](https://www.freecodecamp.org/news/content/images/2024/05/onclick-event.png)
_Application Next.js affichant une fenêtre d'alerte_

Vous pouvez également déclencher l'événement sans fonction séparée. Vous pouvez le faire en définissant la fonction à exécuter en tant que fonction anonyme à l'intérieur de l'événement :

```jsx
<button onClick={() => alert('Vous avez cliqué sur moi !')}>
  Cliquez-moi
</button>
```

Si vous souhaitez mettre à jour l'état du composant en fonction d'un événement, vous pourriez avoir besoin du hook `useState`. Voici un exemple qui montre cela en utilisant une simple application de compteur :

```jsx
'use client';

import { useState } from 'react';

const Counter = () => {
 const [count, setCount] = useState(0);

 return (
   <div className="flex items-center justify-center space-x-8 p-10">
     <button
       onClick={() => setCount(count - 1)}
       className="bg-red-500 hover:bg-red-600 text-white font-bold px-4 py-2 rounded "
     >
       Décrémenter
     </button>
     <p className="text-4xl font-semibold text-gray-800">{count}</p>
     <button
       onClick={() => setCount(count + 1)}
       className="bg-green-500 hover:bg-green-600 text-white font-bold px-4 py-2 rounded "
     >
       Incrémenter
     </button>
   </div>
 );
};

export default Counter;
```

![Image](https://www.freecodecamp.org/news/content/images/2024/05/counter-app.gif)
_Application de compteur dans Next.js (GIF animé)_

`onChange` et `onSubmit` sont d'autres événements populaires dans React. `onChange` est utilisé sur les éléments `input` et `onSubmit` est utilisé sur un élément `form`.

Voici un exemple d'un événement `onChange` :

```jsx
'use client';

import { useState } from 'react';

const MyInput = () => {
 const [inputValue, setInputValue] = useState('');

 const handleChange = (e) => {
   setInputValue(e.target.value);
 };

 return (
   <div>
     <input
       type="text"
       value={inputValue}
       onChange={handleChange}
       className="border border-green-400 p-2 rounded shadow"
       placeholder="Tapez quelque chose..."
     />
     <p className="mt-4 text-green-400">Vous avez tapé : {inputValue}</p>
   </div>
 );
};

export default MyInput;
```

![Image](https://www.freecodecamp.org/news/content/images/2024/05/onchange-event.gif)
_Gestion des changements d'entrée dans React_

Nous examinerons un exemple d'un événement `onSubmit` dans la section sur la façon d'empêcher le comportement par défaut du navigateur lors de la soumission d'un formulaire.

D'autres exemples d'événements incluent les événements de clavier comme `onKeyDown`, `onKeyPress`, et `onKeyUp`, les événements de souris comme `onMouseUp`, `onMouseDown`, `onMouseEnter`, `onDrag`, et plus encore. Tout événement populaire en JavaScript est disponible dans React. La seule différence est que les événements sont écrits en `camelCase` dans React.

## Comment passer des arguments aux gestionnaires d'événements

Passer des arguments aux gestionnaires d'événements dans React est une exigence courante lorsque vous devez effectuer des actions sur des données spécifiques associées à un événement. Par exemple, supprimer ou modifier une ressource.

Pour ce faire, la fonction de gestionnaire doit prendre un paramètre :

```jsx
const handleClick = (item) => {
   console.log('Clic sur le bouton pour :', item);
};
```

Vous passez ensuite un argument correspondant à ce paramètre dans la fonction anonyme de l'événement :

```jsx
<button onClick={() => handleClick(item)}>Cliquez-moi</button>

```

Voici un exemple de gestion de la suppression de tâches dans un composant `TaskManager` :

```jsx
'use client';

import { useState } from 'react';

const TaskManager = () => {
 const [tasks, setTasks] = useState([
   { id: 1, text: 'Lire un article' },
   { id: 2, text: 'Lire un livre' },
   { id: 3, text: 'Écrire un article' },
   { id: 4, text: 'Coder' },
 ]);

 // La fonction prend un paramètre taskId
 const deleteTask = (taskId) => {
   setTasks((currentTasks) =>
     currentTasks.filter((task) => task.id !== taskId)
   );
   console.log('Tâche supprimée avec l\'ID :', taskId);
 };

 return (
   <div className="p-5 max-w-md mx-auto bg-gray-100 rounded-lg shadow">
     <ul className="list-none space-y-2">
       {tasks.map((task) => (
         <li
           key={task.id}
           className="flex justify-between items-center bg-white p-3 rounded shadow-sm"
         >
           {task.text}
           <button
             // L'événement onClick prend un argument task.id pour tenir compte du paramètre taskId de la fonction
             onClick={() => deleteTask(task.id)}
             className="bg-red-500 hover:bg-red-700 text-white font-bold py-1 px-3 rounded"
           >
             Supprimer
           </button>
         </li>
       ))}
     </ul>
   </div>
 );
};


export default TaskManager;
```

![Image](https://www.freecodecamp.org/news/content/images/2024/05/task-deletion.gif)
_La suppression d'un élément est un excellent exemple de gestionnaire d'événements paramétré_

## Modèles courants de gestion des événements dans React

Les modèles de gestion des événements font référence aux techniques de gestion des interactions utilisateur au sein des composants React.

Ces modèles incluent, sans s'y limiter :

* Liaison des gestionnaires d'événements avec `useCallback` pour mémoriser le gestionnaire
* Gestionnaires d'événements avec paramètres (vous avez vu cela dans la section sur la façon de passer des arguments aux gestionnaires d'événements)
* Gestion conditionnelle des événements
* Délégation d'événements
* Remontée d'événements
* Gestion optimisée pour les listes
* Fonctions fléchées en ligne (fonctions anonymes que vous passez aux gestionnaires d'événements)

Voici un exemple utilisant `useCallback` pour éviter de créer une nouvelle fonction à chaque rendu :

```jsx
'use client';

import { useCallback } from 'react';

function HandlerComponent() {
 const handleClick = useCallback(() => {
   console.log('Bouton cliqué');
 }, []);

 return (
   <button onClick={handleClick}>
     Cliquez-moi
   </button>
 );
}

export default HandlerComponent;
```

Et voici un exemple de gestion conditionnelle des événements :

```jsx
'use client';

import { useState } from 'react';

function CheckLogin() {
 const [isLoggedIn, setLoggedIn] = useState(false);

 const toggleLogin = () => {
   setLoggedIn(!isLoggedIn);
 };

 const handleLogin = () => {
   if (isLoggedIn) {
     console.log('L\'utilisateur est connecté');
   } else {
     console.log('L\'utilisateur est déconnecté');
   }
 };

 return (
   <div>
     <h2 className="text-3xl text-center mb-4">
       {isLoggedIn ? 'L\'utilisateur est connecté' : 'L\'utilisateur n\'est pas connecté'}
     </h2>
     <button
       onClick={handleLogin}
       className="bg-green-400 hover:bg-green-500 px-2 py-3 rounded mr-3"
     >
       Vérifier la connexion
     </button>
     <button
       onClick={toggleLogin}
       className="bg-green-400 hover:bg-green-500 px-2 py-3 rounded"
     >
       {isLoggedIn ? 'Se déconnecter' : 'Se connecter'}
     </button>
   </div>
 );
}

export default CheckLogin;
```

![Image](https://www.freecodecamp.org/news/content/images/2024/05/conditional-event.gif)
_L'application Next.js vérifie si l'utilisateur est connecté_

## Comment empêcher le comportement par défaut du navigateur dans les gestionnaires d'événements

Le comportement par défaut du navigateur est l'action automatique que le navigateur effectue lorsqu'un événement spécifique est déclenché. En gestion des événements, le comportement par défaut du navigateur le plus courant est qu'il actualise la page lorsqu'un formulaire est soumis. 

Pour empêcher le navigateur d'actualiser la page lorsqu'un formulaire est soumis, ou pour empêcher tout autre comportement par défaut, passez le paramètre `event` dans la fonction gérant l'événement `onSubmit`, puis utilisez cet `event` pour appeler une fonction `preventDefault`.

```jsx
const handleSubmit = (event) => {
 // empêcher le comportement par défaut
 event.preventDefault();
};

return (
 // référencez la fonction dans onSubmit
 <form onSubmit={handleSubmit}>
   <input
     type="text"
     value={inputValue}
     onChange={handleInputChange}
     placeholder="Entrez quelque chose..."
   />
   <button type="submit">Soumettre</button>
 </form>
);
```

## Bonnes pratiques pour une gestion efficace des événements dans React

Voici les règles les plus importantes pour la gestion des événements dans React :

### Éviter d'utiliser des fonctions fléchées anonymes à l'intérieur des événements

Il semble pratique d'utiliser des fonctions fléchées directement dans les événements, comme `onClick={() => console.log('bouton cliqué')})`. L'inconvénient est que cela peut entraîner des problèmes de performance car une nouvelle fonction est créée à chaque rendu.

Définissez toujours la fonction de gestionnaire à exécuter lorsque l'événement est déclenché en dehors de la méthode de rendu pour éviter ces problèmes de performance.

### Mémoriser les événements avec le hook useCallback

Pour les composants qui se re-rendent souvent, la mémorisation des gestionnaires avec le hook `useCallback` peut prévenir les re-rendus inutiles. Cela est utile lorsque vous passez des événements en tant que props à des composants enfants qui pourraient se re-rendre inutilement.

### Utiliser la délégation d'événements

Pour plusieurs éléments similaires, comme des éléments dans une liste, envisagez d'utiliser la délégation d'événements. Attachez un seul écouteur d'événement à l'élément parent et utilisez la cible de l'événement pour gérer l'interaction utilisateur avec les éléments enfants. Cela réduit le nombre d'écouteurs d'événements et peut améliorer les performances.

### Prévenir le comportement par défaut lorsque nécessaire

Utilisez `event.preventDefault()` dans vos gestionnaires d'événements lorsque vous devez empêcher le navigateur d'effectuer des actions par défaut, comme la soumission d'un formulaire. Cependant, vous devez utiliser cette méthode avec prudence pour éviter de bloquer les comportements du navigateur inutilement.

### Nettoyer les écouteurs d'événements

Si vous configurez vos écouteurs d'événements dans `useEffect`, retournez toujours une fonction de nettoyage pour supprimer l'écouteur d'événement. Sinon, cela provoquera des fuites de mémoire.

### Tester les gestionnaires d'événements

Assurez-vous que vos gestionnaires d'événements sont couverts par vos tests unitaires et d'intégration. Des frameworks de test comme Jest combinés avec React Testing Library peuvent aider à vérifier que vos gestionnaires d'événements fonctionnent comme prévu.

## Conclusion

Dans cet article, vous avez appris les fondamentaux de la gestion des événements dans React, en vous concentrant sur l'utilisation du système d'événements synthétiques de React pour créer des événements dans les applications web React.

Nous avons exploré la définition des gestionnaires d'événements, le passage d'arguments et la prévention des comportements par défaut du navigateur pour améliorer les expériences utilisateur.

De plus, vous avez appris les avantages de l'utilisation de `useCallback` pour optimiser les gestionnaires d'événements pour des performances efficaces sous diverses interactions utilisateur.

Avec ces informations, vous devriez être en mesure de mettre en œuvre la gestion des événements dans vos projets, afin d'améliorer à la fois la fonctionnalité et l'engagement des utilisateurs.

## Faites passer vos compétences React au niveau supérieur

Souhaitez-vous en savoir plus sur la gestion des événements ou d'autres concepts React ? Alors rejoignez mon cours React sur Udemy. Je vous montrerai comment devenir un meilleur développeur React en construisant un jeu 2048. Construire des jeux rend l'apprentissage plus amusant et agréable.

[![Cours accéléré Next.js sur Udemy](https://assets.mateu.sh/assets/fcc-events-in-react)](https://assets.mateu.sh/r/fcc-events-in-react)


 Rejoignez maintenant et commencez votre voyage pour maîtriser React !