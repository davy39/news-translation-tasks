---
title: Méthodes de cycle de vie de React et Hooks – un guide pour débutants
subtitle: ''
author: Casmir Onyekani
co_authors: []
series: null
date: '2023-10-02T17:22:49.000Z'
originalURL: https://freecodecamp.org/news/react-lifecycle-methods-and-hooks-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2023/10/lifecycle.jpg
tags:
- name: hooks
  slug: hooks
- name: lifecycle methods
  slug: lifecycle-methods
- name: React
  slug: react
- name: react hooks
  slug: react-hooks
seo_title: Méthodes de cycle de vie de React et Hooks – un guide pour débutants
seo_desc: 'React is all about building user interfaces. And to do that effectively,
  React provides ways for components to manage their lifecycles.

  This means that components can perform specific tasks at different stages of their
  existence, from the moment they...'
---

[React](https://www.freecodecamp.org/news/react-beginner-handbook/#howmuchjavascriptyouneedtoknowtousereact) est entièrement dédié à la construction d'interfaces utilisateur. Pour ce faire efficacement, React fournit des moyens pour que les composants gèrent leurs cycles de vie.

Cela signifie que les composants peuvent effectuer des tâches spécifiques à différentes étapes de leur existence, depuis le moment où ils sont créés jusqu'à leur suppression de l'interface utilisateur.

Les méthodes de cycle de vie ont été une partie fondamentale de React pendant de nombreuses années. Mais avec l'introduction des hooks, l'approche de React pour gérer l'état et les effets secondaires dans les composants fonctionnels est devenue plus intuitive et flexible.

Juste une petite note : bien que les hooks remplacent généralement les composants de classe, il n'est pas prévu de supprimer les classes de React.

### Pourquoi ce guide ?

Dans ce tutoriel, vous apprendrez les méthodes de cycle de vie des composants de classe telles que `componentDidMount`, `componentDidUpdate`, `componentWillUnmount` et `shouldComponentUpdate`.

Vous explorerez également les hooks React comme `useState`, `useEffect` et `useContext`, et comprendrez pourquoi ils ont été introduits. Cela rendra votre parcours avec React plus fluide et plus agréable.

Que vous débutiez avec React ou que vous cherchiez à approfondir vos connaissances, ce guide vous fournira les connaissances nécessaires pour construire des applications web réactives et interactives en utilisant les outils puissants de React.

Plongeons dans le vif du sujet et découvrons la magie des méthodes de cycle de vie et des hooks de React.

## Comment fonctionne le cycle de vie des composants

Dans React, les composants passent par un cycle de vie composé de différentes étapes. Chacune de ces étapes offre des méthodes spécifiques que vous pouvez personnaliser pour exécuter du code à divers moments pendant l'existence d'un composant.

Ces méthodes vous aident à effectuer des tâches telles que l'initialisation des données, la gestion des mises à jour et le nettoyage des ressources selon les besoins.

### Méthodes de cycle de vie des composants de classe

Commençons par examiner les méthodes de cycle de vie des composants de classe. Celles-ci étaient le moyen principal de gérer le cycle de vie des composants avant l'introduction des hooks.

#### Comment utiliser `componentDidMount` :

Cette méthode est appelée après qu'un composant a été inséré dans le DOM. C'est un endroit idéal pour effectuer des tâches d'initialisation, comme la récupération de données depuis une API ou la configuration d'écouteurs d'événements.

Exemple de code :

```jsx

import React, { Component } from 'react';

class MyComponent extends React.Component {
  constructor() {
    super();
    this.state = {
      data: null,
    };
  }

  componentDidMount() {
    // C'est ici que vous pouvez effectuer l'initialisation.
    
    // Dans cet exemple, nous simulons la récupération de données depuis une API après que le composant a été monté.
    // Nous utilisons un setTimeout pour imiter une opération asynchrone.
    setTimeout(() => {
      const fetchedData = 'Ces données ont été récupérées après le montage.';
      this.setState({ data: fetchedData });
    }, 2000); // Simuler un délai de 2 secondes
  }

  render() {
    return (
      <div>
        <h1>Exemple de componentDidMount</h1>
        {this.state.data ? (
          <p>Données : {this.state.data}</p>
        ) : (
          <p>Chargement des données...</p>
        )}
      </div>
    );
  }
}

export default MyComponent;
```

Dans cet exemple, nous avons créé un composant de classe appelé `MyComponent`. Dans le constructeur, l'état du composant est initialisé avec data défini à null, et nous l'utilisons pour stocker les données récupérées.

Dans la méthode `componentDidMount`, nous simulons la récupération de données depuis une API en utilisant `setTimeout` pour imiter une opération asynchrone. Après 2 secondes (2000 millisecondes), l'état du composant est mis à jour avec les données récupérées.

Dans la méthode render, le contenu est rendu de manière conditionnelle en fonction de l'état des données. Si data est null, un message `Chargement des données...` est affiché. Sinon, les données récupérées sont affichées.

Lorsque vous utilisez ce composant dans votre application, vous remarquerez que le message Chargement des données... s'affiche initialement, et après 2 secondes, les données récupérées sont affichées. Cela démontre comment `componentDidMount` est utile pour effectuer des tâches après qu'un composant a été ajouté au DOM.

#### Comment utiliser `componentDidUpdate` :

Cette méthode est appelée après qu'un composant a été réaffiché en raison de changements dans son état ou ses props. C'est un endroit idéal pour gérer les effets secondaires ou effectuer des actions supplémentaires basées sur ces changements.

Exemple de code :

```jsx
import React, { Component } from 'react';

class Counter extends React.Component {
  constructor() {
    super();
    this.state = {
      count: 0,
    };
  }

  // Cette méthode sera appelée lorsque le bouton "Incrémenter" est cliqué
  handleIncrement = () => {
    this.setState({ count: this.state.count + 1 });
  };

  // componentDidUpdate est appelé après la mise à jour du composant
  componentDidUpdate(prevProps, prevState) {
    // Vous pouvez accéder aux props et à l'état précédents ici
    console.log('Composant mis à jour');
    console.log('État précédent :', prevState);
    console.log('État actuel :', this.state);
  }

  render() {
    return (
      <div>
        <h1>Compteur</h1>
        <p>Compte : {this.state.count}</p>
        <button onClick={this.handleIncrement}>Incrémenter</button>
      </div>
    );
  }
}

export default Counter;
```

Dans cet exemple de code, nous créons un composant de classe `Counter` avec un constructeur qui initialise l'état `count` à 0. La méthode `handleIncrement` met à jour l'état count lorsque le bouton *Incrémenter* est cliqué.

À l'intérieur de la méthode de cycle de vie `componentDidUpdate`, nous enregistrons un message (Composant mis à jour) dans la console. Nous enregistrons également l'état précédent (prevState) et l'état actuel (this.state). Cela démontre comment vous pouvez accéder aux valeurs précédentes et actuelles pendant une mise à jour. La méthode render affiche le compte actuel et un bouton pour l'incrémenter.

Maintenant, lorsque vous utilisez ce composant `Counter` dans votre application, ouvrez la console du navigateur. Chaque fois que vous cliquez sur le bouton *Incrémenter*, vous verrez des messages dans la console indiquant que le composant a été mis à jour, ainsi que les valeurs de l'état précédent et actuel.

Vous pouvez utiliser `componentDidUpdate` pour diverses raisons, telles que faire des requêtes réseau lorsque les props ou l'état changent, mettre à jour le DOM en fonction des changements d'état, ou interagir avec des bibliothèques tierces après une mise à jour. Cela fournit un moyen d'effectuer des actions qui doivent se produire spécifiquement après qu'un composant a été réaffiché.

#### Comment utiliser `componentWillUnmount`

Cette méthode est appelée juste avant qu'un composant soit retiré du DOM. C'est un endroit crucial pour effectuer des tâches de nettoyage, telles que l'effacement des temporisateurs, le désabonnement des événements ou la libération des ressources pour prévenir les \[fuites de mémoire\](https://en.wikipedia.org/wiki/Memory\_leak#:~:text=In computer science%2C a memory,longer needed is not released.).

Illustrons un simple composant React qui configure un temporisateur lorsqu'il est monté, en utilisant la méthode `componentDidMount`, et efface ce temporisateur lorsqu'il est démonté en utilisant la méthode `componentWillUnmount`.

Exemple de code :

```jsx
import React, { Component } from 'react';

class TimerComponent extends React.Component {
  constructor() {
    super();
    this.state = {
      seconds: 0,
    };
    this.timer = null; // Initialiser le temporisateur
  }

  // Lorsque le composant est monté, démarrer le temporisateur
  componentDidMount() {
    this.timer = setInterval(() => {
      this.setState({ seconds: this.state.seconds + 1 });
    }, 1000); // Mettre à jour toutes les 1 seconde (1000 millisecondes)
  }

  // Lorsque le composant est démonté, effacer le temporisateur pour prévenir les fuites de mémoire
  componentWillUnmount() {
    clearInterval(this.timer);
  }

  render() {
    return (
      <div>
        <h1>Composant Temporisateur</h1>
        <p>Temps écoulé : {this.state.seconds} secondes</p>
      </div>
    );
  }
}

export default TimerComponent;
```

Dans cet exemple, nous avons créé la classe `TimerComponent`. À l'intérieur du constructeur, l'état du composant est initialisé avec une propriété seconds, que nous utiliserons pour suivre le temps écoulé. La variable timer est également définie à null.

Dans la méthode de cycle de vie `componentDidMount`, le temporisateur est démarré en utilisant `setInterval`. Ce temporisateur incrémente la propriété d'état seconds toutes les secondes.

Dans la méthode de cycle de vie `componentWillUnmount`, le temporisateur est effacé en utilisant `clearInterval` pour s'assurer qu'il ne continue pas à fonctionner après que le composant a été retiré du DOM.

Dans la méthode render, le temps écoulé est affiché en fonction de la propriété d'état seconds.

Lorsque vous utilisez ce `TimerComponent` dans votre application et que vous le rendez, vous remarquerez que le temporisateur commence lorsque le composant est monté et s'arrête lorsque le composant est démonté. Cela est grâce au nettoyage effectué dans la méthode `componentWillUnmount`. Cela prévient les fuites de ressources et assure que le temporisateur est correctement géré tout au long du cycle de vie du composant.

#### Comment utiliser `shouldComponentUpdate`

Nous utilisons cette méthode de cycle de vie pour contrôler si un composant doit être réaffiché lorsque son état ou ses props changent. Elle est particulièrement utile pour optimiser les performances en empêchant les rendus inutiles.

Créons un simple composant de classe React et utilisons la méthode `shouldComponentUpdate` pour décider si le composant doit être réaffiché en fonction des changements de son état.

Exemple de code :

```jsx
import React, { Component } from 'react';

class Counter extends React.Component {
  constructor() {
    super();
    this.state = {
      count: 0,
    };
  }

  shouldComponentUpdate(nextProps, nextState) {
    // Permettre au composant de se réafficher uniquement si le compte est pair
    if (nextState.count % 2 === 0) {
      return true; // Réafficher
    }
    return false; // Ne pas réafficher
  }

  incrementCount = () => {
    this.setState((prevState) => ({ count: prevState.count + 1 }));
  };

  render() {
    return (
      <div>
        <h1>Exemple de Compteur</h1>
        <p>Compte : {this.state.count}</p>
        <button onClick={this.incrementCount}>Incrémenter</button>
      </div>
    );
  }
}

export default Counter;
```

Dans cet exemple, nous avons créé le composant de classe `Counter` qui maintient un état count, qui commence à 0. Dans la méthode `shouldComponentUpdate`, nous vérifions si le compte de l'état suivant est pair. Si c'est le cas, nous permettons au composant de se réafficher. Sinon, nous empêchons le réaffichage.

La méthode `incrementCount` est appelée lorsque le bouton *Incrémenter* est cliqué. Elle met à jour l'état count en l'incrémentant.

Dans la méthode render, le compte actuel et un bouton pour l'incrémenter sont affichés.

Si vous cliquez sur le bouton *Incrémenter* et que le compte devient un nombre impair, le composant ne se réaffichera pas. Ce comportement démontre comment `shouldComponentUpdate` peut être utilisé pour optimiser le rendu dans des situations où tous les changements d'état ne doivent pas déclencher un réaffichage.

## Introduction aux Hooks React

React a introduit les hooks dans la version 16.8. Ils ont permis aux composants fonctionnels d'accéder à l'état et à diverses fonctionnalités de React sans écrire de composants de classe.

Par conséquent, les composants de classe sont devenus largement inutiles. Les hooks simplifient la logique des composants et la rendent plus réutilisable.

### Pourquoi utiliser les Hooks ?

Les hooks ont été introduits pour résoudre plusieurs problèmes et rendre le code React plus facile à comprendre et à maintenir :

* Complexité – les composants de classe peuvent devenir complexes lors de la gestion de l'état et des effets secondaires.
  
* Réutilisabilité – la logique dans les composants de classe n'est pas facilement partageable entre les composants.
  
* Courbe d'apprentissage – les composants de classe introduisent une courbe d'apprentissage plus raide pour les nouveaux venus dans React.
  
### Hooks React couramment utilisés

#### Le hook `useState`

`useState` vous permet d'ajouter un état aux composants fonctionnels. Il retourne un tableau avec la valeur actuelle de l'état et une fonction pour le mettre à jour.

Exemple de code :

```jsx
import React, { useState } from 'react';

function Counter() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>Compte : {count}</p>
      <button onClick={() => setCount(count + 1)}>Incrémenter</button>
    </div>
  );
}
```

Dans cet exemple, nous avons utilisé le hook `useState` pour gérer l'état d'un compteur. Lorsque le bouton Incrémenter est cliqué, `setCount` met à jour l'état count, provoquant le réaffichage du composant avec la valeur mise à jour.

#### Le hook `useEffect`

`useEffect` est utilisé pour les effets secondaires dans les composants fonctionnels, similaire à `componentDidMount` et `componentDidUpdate`. Il s'exécute après le rendu et peut être contrôlé en spécifiant des dépendances.

Exemple de code :

```jsx
import React, { useState, useEffect } from 'react';

function Example() {
  const [data, setData] = useState(null);

  useEffect(() => {
    // Récupérer des données depuis une API
    fetch('https://api.example.com/data')
      .then(response => response.json())
      .then(data => setData(data));
  }, []); // Tableau de dépendances vide, s'exécute une seule fois

  return <div>{data ? data.message : 'Chargement...'}</div>;
}
```

Dans cet exemple, `useEffect` est utilisé pour récupérer des données depuis une API lorsque le composant est monté. Le tableau de dépendances vide `[]` garantit que l'effet ne s'exécute qu'une seule fois. Lorsque les données sont récupérées, `setData` met à jour l'état des données, provoquant un réaffichage avec les informations récupérées.

#### Le hook `useContext`

`useContext` permet aux composants fonctionnels d'accéder aux valeurs de contexte. C'est un moyen de transmettre des données dans l'arborescence des composants sans passer explicitement des props.

Exemple de code :

```jsx

import React, { useContext } from 'react';

// Créer un contexte
const MyContext = React.createContext();

function MyComponent() {
  const value = useContext(MyContext);

  return <div>Valeur du Contexte : {value}</div>;
}
```

Dans cet exemple, nous créons un contexte appelé `MyContext`. Le hook `useContext` permet à `MyComponent` d'accéder à la valeur stockée dans ce contexte. C'est un outil puissant pour gérer l'état global dans votre application.

### Avantages des hooks personnalisés

Les hooks personnalisés sont des fonctions qui utilisent des hooks en interne et peuvent être réutilisées dans plusieurs composants. Ils aident à encapsuler et à partager une logique complexe.

Voici un exemple de hook personnalisé appelé `useLocalStorage` qui simplifie le stockage et la récupération de données dans le stockage local du navigateur :

```jsx
import { useState } from 'react';

function useLocalStorage(key, initialValue) {
  // Récupérer la valeur stockée depuis le stockage local
  const storedValue = localStorage.getItem(key);

  // Initialiser l'état avec la valeur stockée ou la valeur initiale
  const [value, setValue] = useState(storedValue || initialValue);

  // Mettre à jour le stockage local chaque fois que l'état change
  const setStoredValue = (newValue) => {
    setValue(newValue);
    localStorage.setItem(key, newValue);
  };

  return [value, setStoredValue];
}

export default useLocalStorage;
```

Dans ce hook personnalisé, nous importons `useState` de React car nous allons l'utiliser pour gérer l'état. La fonction `useLocalStorage` prend deux paramètres :

* **key** : une chaîne représentant la clé sous laquelle les données seront stockées dans le stockage local.
  
* **initialValue** : la valeur initiale pour l'état.
  

À l'intérieur du hook, nous avons d'abord tenté de récupérer la valeur stockée depuis le stockage local en utilisant `localStorage.getItem(key)`. Ensuite, nous avons initialisé la variable d'état value en utilisant `useState`, en utilisant la `storedValue` si elle existe ou la `initialValue` sinon.

Ensuite, nous avons défini une fonction `setStoredValue` qui met à jour à la fois l'état et le stockage local lorsqu'elle est appelée. Elle définit la nouvelle valeur dans le stockage local en utilisant `localStorage.setItem(key, newValue)`.

Enfin, nous avons retourné un tableau `[value, setStoredValue]` comme valeur de retour du hook, permettant aux composants d'accéder à la valeur stockée et de la mettre à jour selon les besoins.

Voici un exemple de la façon dont vous pouvez utiliser le hook `useLocalStorage` dans un composant :

```jsx
import React from 'react';
import useLocalStorage from './useLocalStorage'; // Importer le hook personnalisé

function App() {
  // Utiliser le hook personnalisé pour gérer un "username" stocké dans le stockage local
  const [username, setUsername] = useLocalStorage('username', 'Invité');

  const handleInputChange = (e) => {
    setUsername(e.target.value);
  };

  return (
    <div>
      <h1>Bonjour, {username} !</h1>
      <input
        type="text"
        placeholder="Entrez votre nom d'utilisateur"
        value={username}
        onChange={handleInputChange}
      />
    </div>
  );
}

export default App;
```

Dans cet exemple, nous importons le hook personnalisé `useLocalStorage` et l'utilisons pour gérer une valeur username dans le stockage local. Le composant initialise l'état username en utilisant le hook et le met à jour lorsque le champ de saisie change.

La valeur est stockée et récupérée depuis le stockage local, ce qui lui permet de persister à travers les rechargements de page.

Les hooks personnalisés sont un moyen puissant d'encapsuler et de réutiliser une logique complexe dans les applications React, rendant votre code plus modulaire et maintenable.

## Conclusion

React fournit aux développeurs des outils puissants pour gérer les cycles de vie de leurs composants. Ces cycles de vie permettent aux composants d'effectuer des tâches spécifiques à différentes étapes de leur existence, de la création à la suppression.

Dans ce guide, nous avons exploré les méthodes de cycle de vie des composants de classe de React. Ces méthodes ont été une partie fondamentale de React pendant de nombreuses années et continuent d'être pertinentes dans certains scénarios.

Vous avez également été introduit aux Hooks React. Ceux-ci sont devenus le moyen préféré de gérer l'état et les effets secondaires dans les applications React. Ils offrent une approche plus intuitive et flexible pour construire des composants.

Bien que les hooks aient gagné en popularité et remplacent généralement le besoin de composants de classe, il est important de noter qu'il n'est pas prévu de supprimer les composants de classe de React. Les bases de code existantes et les bibliothèques tierces peuvent encore utiliser des composants de classe, donc comprendre à la fois les cycles de vie des composants de classe et les hooks est précieux pour les développeurs React.

En résumé, les méthodes de cycle de vie et les hooks de React sont cruciaux pour construire des applications dynamiques et efficaces, et ils offrent aux développeurs une gamme d'options pour gérer le comportement et l'état des composants. Alors que vous continuez à explorer et à travailler avec React, vous trouverez qu'avoir une solide compréhension des cycles de vie et des hooks fera de vous un développeur React plus polyvalent et capable.

Si vous avez trouvé ce guide utile et agréable, n'hésitez pas à le liker. Pour plus de tutoriels instructifs, suivez-moi sur [X](https://twitter.com/casweb_dev) pour les mises à jour 🙏.

Bonne programmation !