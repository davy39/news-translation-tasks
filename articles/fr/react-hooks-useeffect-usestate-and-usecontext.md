---
title: Comment utiliser les Hooks React – useEffect, useState et useContext avec des
  exemples de code
subtitle: ''
author: Joan Ayebola
co_authors: []
series: null
date: '2023-12-04T18:38:16.000Z'
originalURL: https://freecodecamp.org/news/react-hooks-useeffect-usestate-and-usecontext
coverImage: https://www.freecodecamp.org/news/content/images/2023/11/Orange-and-Yellow-Retro-Flower-Power-Daily-Class-Agenda-Template.png
tags:
- name: React
  slug: react
- name: react hooks
  slug: react-hooks
seo_title: Comment utiliser les Hooks React – useEffect, useState et useContext avec
  des exemples de code
seo_desc: "React is a powerful JavaScript library for building user interfaces. And\
  \ it has undergone significant changes over the years. \nOne of the most noteworthy\
  \ additions is the introduction of hooks, which revolutionized the way developers\
  \ manage state and..."
---

React est une puissante bibliothèque JavaScript pour construire des interfaces utilisateur. Et elle a subi des changements significatifs au fil des ans.

L'une des ajouts les plus notables est l'introduction des hooks, qui ont révolutionné la manière dont les développeurs gèrent l'état et les effets secondaires dans les composants fonctionnels.

Dans ce guide, nous explorerons trois hooks fondamentaux pour les débutants : `useState`, `useEffect` et `useContext`.

## Introduction aux Hooks React

Avant les hooks, la logique d'état dans React était principalement gérée en utilisant des composants de classe.

Avec l'avènement des composants fonctionnels et des hooks, les développeurs ont gagné une manière plus concise et expressive de gérer l'état et les méthodes de cycle de vie. Les hooks permettent d'utiliser l'état et d'autres fonctionnalités de React sans écrire une classe.

### Qu'est-ce que les Hooks React ?

Les hooks React sont des fonctions qui permettent aux composants fonctionnels d'utiliser l'état et les fonctionnalités de cycle de vie qui étaient auparavant uniquement disponibles dans les composants de classe. Ils ont été introduits dans React 16.8 pour fournir une manière plus cohérente de gérer la logique d'état dans les composants fonctionnels.

## Comment utiliser le Hook `useState`

Le hook `useState` est peut-être le hook le plus basique et essentiel dans React. Il permet d'ajouter un état à vos composants fonctionnels, leur permettant de suivre des données qui changent au fil du temps. Plongeons dans le fonctionnement de `useState` avec un exemple simple.

### Utilisation de base de `useState`

```jsx
import React, { useState } from 'react';

const Counter = () => {
  // Déclare une variable d'état nommée 'count' avec une valeur initiale de 0
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>Compteur : {count}</p>
      <button onClick={() => setCount(count + 1)}>Incrémenter</button>
    </div>
  );
};

export default Counter;
```

Dans cet exemple, nous importons le hook `useState` de la bibliothèque 'react'. La fonction `useState` retourne un tableau avec deux éléments : la valeur actuelle de l'état (`count`) et une fonction (`setCount`) pour la mettre à jour. Nous initialisons `count` à 0, et cliquer sur le bouton "Incrémenter" augmente sa valeur.

### Comment utiliser plusieurs Hooks `useState`

Vous pouvez utiliser le hook `useState` plusieurs fois dans un seul composant pour gérer différentes parties de l'état de manière indépendante. Modifions notre composant `Counter` pour inclure une deuxième partie de l'état.

```jsx
import React, { useState } from 'react';

const Counter = () => {
  const [count, setCount] = useState(0);
  const [isEven, setIsEven] = useState(false);

  return (
    <div>
      <p>Compteur : {count}</p>
      <p>{isEven ? 'Pair' : 'Impair'}</p>
      <button onClick={() => setCount(count + 1)}>Incrémenter</button>
      <button onClick={() => setIsEven(!isEven)}>Basculer Pair/Impair</button>
    </div>
  );
};

export default Counter;
```

Maintenant, notre composant `Counter` a deux parties d'état indépendantes : `count` et `isEven`. Cliquer sur le bouton "Basculer Pair/Impair" changera la valeur de `isEven`.

## Comment utiliser le Hook `useEffect`

Le hook `useEffect` est utilisé pour effectuer des effets secondaires dans vos composants fonctionnels, tels que la récupération de données, l'abonnement à des événements externes ou la modification manuelle du DOM. Il combine les fonctionnalités de `componentDidMount`, `componentDidUpdate` et `componentWillUnmount` dans les composants de classe.

### Utilisation de base de `useEffect`

```jsx
import React, { useState, useEffect } from 'react';

const DataFetcher = () => {
  const [data, setData] = useState(null);

  useEffect(() => {
    // Récupérer des données depuis une API
    fetch('https://api.example.com/data')
      .then((response) => response.json())
      .then((result) => setData(result))
      .catch((error) => console.error('Erreur lors de la récupération des données :', error));
  }, []); // Un tableau de dépendances vide signifie que cet effet s'exécute une fois après le rendu initial

  return (
    <div>
      {data ? (
        <ul>
          {data.map((item) => (
            <li key={item.id}>{item.name}</li>
          ))}
        </ul>
      ) : (
        <p>Chargement des données...</p>
      )}
    </div>
  );
};

export default DataFetcher;
```

Dans cet exemple, le hook `useEffect` est utilisé pour récupérer des données depuis une API lorsque le composant est monté. Le deuxième argument de `useEffect` est un tableau de dépendances. Si les dépendances changent entre les rendus, l'effet s'exécutera à nouveau. Un tableau vide signifie que l'effet s'exécute une fois après le rendu initial.

### Nettoyage dans `useEffect`

Parfois, les effets secondaires doivent être nettoyés, surtout lorsqu'on traite avec des abonnements ou des temporisateurs pour prévenir les fuites de mémoire. Le hook `useEffect` peut retourner une fonction de nettoyage qui sera exécutée lorsque le composant sera démonté.

```jsx
import React, { useState, useEffect } from 'react';

const Timer = () => {
  const [seconds, setSeconds] = useState(0);

  useEffect(() => {
    const intervalId = setInterval(() => {
      setSeconds((prevSeconds) => prevSeconds + 1);
    }, 1000);

    // Fonction de nettoyage pour effacer l'intervalle lorsque le composant est démonté
    return () => clearInterval(intervalId);
  }, []); // Tableau de dépendances vide pour la configuration initiale uniquement

  return <p>Secondes : {seconds}</p>;
};

export default Timer;
```

Dans cet exemple, la fonction `setInterval` est utilisée pour mettre à jour l'état `seconds` chaque seconde. La fonction de nettoyage retournée par `useEffect` efface l'intervalle lorsque le composant est démonté.

## Comment utiliser le Hook `useContext`

Le hook `useContext` est utilisé pour consommer des valeurs depuis un contexte React. Le contexte fournit un moyen de passer des données à travers l'arbre des composants sans avoir à passer des props manuellement à chaque niveau. Explorons comment `useContext` fonctionne avec un exemple simple.

### Comment créer un Contexte

Tout d'abord, créons un contexte pour contenir le statut d'authentification d'un utilisateur.

```jsx
import React, { createContext, useContext, useState } from 'react';

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  const login = () => {
    setIsAuthenticated(true);
  };

  const logout = () => {
    setIsAuthenticated(false);
  };

  return (
    <AuthContext.Provider value={{ isAuthenticated, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  return useContext(AuthContext);
};
```

Dans cet exemple, nous créons un `AuthContext` en utilisant `createContext` et fournissons un composant `AuthProvider`. Le composant `AuthProvider` enveloppe ses enfants avec le fournisseur de contexte et inclut des fonctions pour se connecter et se déconnecter.

### Comment utiliser `useContext`

Maintenant, utilisons le hook `useContext` dans un composant pour accéder au statut d'authentification.

```jsx
import React from 'react';
import { useAuth } from './AuthContext';

const AuthStatus = () => {
  const { isAuthenticated, login, logout } = useAuth();

  return (
    <div>
      <p>L'utilisateur est {isAuthenticated ? 'connecté' : 'déconnecté'}</p>
      <button onClick={login}>Connexion</button>
      <button onClick={logout}>Déconnexion</button>
    </div>
  );
};

export default AuthStatus;
```

Ici, le hook `useAuth` est utilisé pour accéder aux valeurs fournies par le `AuthContext`. Le composant `AuthStatus` affiche le statut de connexion de l'utilisateur et fournit des boutons pour se connecter et se déconnecter.

## Mettre le tout ensemble

Créons un exemple plus complexe qui combine `useState`, `useEffect` et `useContext` dans un seul composant. Supposons que nous avons un composant qui récupère les données utilisateur depuis une API et les affiche, en tenant compte du statut d'authentification de l'utilisateur.

```jsx
import React, { useState, useEffect } from 'react';
import { useAuth } from './AuthContext';

const UserProfile = () => {
  const { isAuthenticated } = useAuth();
  const [userData, setUserData] = useState(null);

  useEffect(() => {
    if (isAuthenticated) {
      // Récupérer les données utilisateur lorsque l'utilisateur est authentifié
      fetch('https://api.example.com/user')
        .then((response) => response.json())
        .then((result) => setUserData(result))
        .catch((error) => console.error('Erreur lors de la récupération des données utilisateur :', error));
    }
  }, [isAuthenticated]); // Exécuter l'effet lorsque isAuthenticated change

  return (
    <div>
      {isAuthenticated ? (
        <div>
          <h2>Bienvenue, {userData ? userData.name : 'Utilisateur'} !</h2>
          <p>Email : {userData ? userData.email : 'Chargement...'}</p>
        </div>
      ) : (
        <p>Veuillez vous connecter pour voir votre profil.</p>
      )}
    </div>
  );
};

export default UserProfile;
```

Dans cet exemple, le composant `UserProfile` utilise le hook `useAuth` pour vérifier le statut d'authentification de l'utilisateur. Si l'utilisateur est authentifié, il récupère les données utilisateur et affiche un message de bienvenue personnalisé. Si l'utilisateur n'est pas authentifié, il invite l'utilisateur à se connecter.

## Conclusion

Les hooks React, y compris `useState`, `useEffect` et `useContext`, ont transformé la manière dont les développeurs écrivent des composants en fournissant une approche plus intuitive et flexible pour gérer l'état et les effets secondaires.

Alors que vous continuez votre parcours avec React, la maîtrise de ces hooks vous permettra de construire des applications plus efficaces et maintenables.

Rappelez-vous, la pratique est la clé pour devenir compétent avec les hooks React. Expérimentez avec différents scénarios, explorez des hooks supplémentaires comme `useReducer` et `useCallback`, et restez à jour avec la documentation React pour toute nouvelle fonctionnalité ou meilleure pratique. Bon codage !