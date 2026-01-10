---
title: Apprenez les React Hooks – Les Hooks courants expliqués avec des exemples de
  code
subtitle: ''
author: Prankur Pandey
co_authors: []
series: null
date: '2024-09-25T16:04:35.573Z'
originalURL: https://freecodecamp.org/news/learn-react-hooks-with-example-code
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1727212733982/7c9b8ae3-e8ac-4e20-b154-7edc60a6985a.avif
tags:
- name: React
  slug: reactjs
- name: ReactHooks
  slug: reacthooks
- name: JavaScript
  slug: javascript
seo_title: Apprenez les React Hooks – Les Hooks courants expliqués avec des exemples
  de code
seo_desc: 'Web development is a popular field in the tech industry. It involves building
  web software using HTML, CSS, and JavaScript – sometimes with the help of various
  frameworks and libraries.

  Using libraries and frameworks allows developers to focus more o...'
---

Le développement Web est un domaine populaire dans l'industrie technologique. Il consiste à créer des logiciels Web à l'aide de HTML, CSS et JavaScript – parfois à l'aide de divers frameworks et bibliothèques.

L'utilisation de bibliothèques et de frameworks permet aux développeurs de se concentrer davantage sur le développement, tandis que les outils s'occupent de certaines fonctionnalités en arrière-plan. Et React.js est une bibliothèque JavaScript populaire pour la création d'applications front-end.

Dans cet article, vous découvrirez la colonne vertébrale de React, à savoir les **Hooks**, et comment ils peuvent vous faciliter la vie en tant que développeur.

## Ce que nous allons aborder :

* [Prérequis :](#heading-prerequis)
    
* [Pour commencer](#heading-pour-commencer)
    
* [Que sont les Hooks ?](#heading-que-sont-les-hooks)
    
* [Types de React Hooks](#heading-types-de-react-hooks)
    
    * [Hooks de gestion d'état](#heading-hooks-de-gestion-detat)
        
    * [Hooks d'effet](#heading-hooks-deffet)
        
    * [Hook de référence](#heading-hook-de-reference)
        
    * [Hooks de performance](#heading-hooks-de-performance)
        
    * [Hook de contexte](#heading-hook-de-contexte)
        
    * [Hook de transition](#heading-hook-de-transition)
        
    * [Quelques autres Hooks](#heading-quelques-autres-hooks)
        
* [Conclusion](#heading-conclusion)
    

## Prérequis :

* Vous devez connaître les bases de JavaScript.
    
* Vous devez également connaître les bases de React, comme la configuration d'une application, sa mise à jour et l'utilisation de l'état (state).
    

## Pour commencer

Vous avez donc décidé de créer une application React — félicitations ! 🎉 Mais en plongeant dans le monde des React Hooks, vous pourriez vous sentir submergé. Avec une pléthore de hooks disponibles, déterminer lesquels utiliser et à quel moment peut être un peu intimidant.

Eh bien, ne vous inquiétez pas – dans ce guide, je vais détailler chaque hook majeur afin que vous puissiez voir comment ils s'imbriquent les uns dans les autres. Nous verrons également lesquels vous utiliserez le plus fréquemment par rapport à ceux plus rares.

À la fin de cet article, vous aurez une carte complète des React Hooks et de leurs applications pratiques.

## **Que sont les Hooks ?**

En JavaScript, nous utilisons des variables pour stocker des données et effectuer ensuite des opérations sur ces données.

Les Hooks dans React fonctionnent de manière similaire, mais ils sont conçus pour gérer l'état dans les **composants fonctionnels**. Au lieu de déclarer manuellement une seule variable, des hooks comme `useState` nous permettent de déclarer des valeurs d'état accompagnées d'une fonction de mise à jour pour modifier cet état.

Voici un exemple simple :

```javascript
import React, { useState } from 'react';

function Counter() {
  const [count, setCount] = useState(0);  // Initialise l'état et la fonction de mise à jour

  return (
    <div>
      <p>Vous avez cliqué {count} fois</p>
      <button onClick={() => setCount(count + 1)}>Cliquez ici</button>
    </div>
  );
}
```

Dans ce code, j'utilise le hook `useState` pour déclarer une donnée d'état appelée `count` et définir sa valeur initiale à 0. La fonction `setCount` nous permet de mettre à jour cet état. Chaque fois que l'on clique sur le bouton, nous utilisons `setCount` pour augmenter `count` de 1. Lorsque l'état est mis à jour, React restitue (re-render) le composant pour refléter le changement.

Contrairement à la déclaration `let count = 0`, l'utilisation de `useState` permet à React de se souvenir de l'état entre les rendus et garantit que l'interface utilisateur (UI) se mette à jour correctement.

## Types de React Hooks

Pour faciliter les choses, vous pouvez considérer que les React Hooks se répartissent en huit catégories majeures :

* **Hooks de gestion d'état** – Pour manipuler l'état.
    
* **Hooks d'effet** – Pour les effets de bord.
    
* **Hooks de référence** – Pour référencer des valeurs JavaScript ou des éléments du DOM.
    
* **Hooks de performance** – Pour optimiser les performances.
    
* **Hooks de contexte** – Pour accéder au contexte React.
    
* **Hooks de transition** – Pour des expériences utilisateur plus fluides.
    
* **Quelques autres Hooks** – Des hooks à usage spécifique.
    
* **Nouveaux Hooks (React 19)** – Des outils de pointe introduits dans la dernière version de React.
    

Dans React, vous pouvez également créer des hooks personnalisés pour différents cas d'utilisation. Chaque hook commence par le mot-clé `use` – même les hooks personnalisés commencent par cette structure. Ce mot-clé est réservé aux Hooks dans React.

Explorons ces hooks en détail.

### **Hooks de gestion d'état**

#### **1.** `useState`

Le hook `useState` est le cœur de React. C'est le hook le plus couramment utilisé, et il est essentiel pour gérer l'état dans les composants fonctionnels. Avec `useState`, vous pouvez capturer les saisies utilisateur, afficher ou masquer des composants, et gérer des nombres, comme dans une application de commerce électronique avec un panier d'achat.

`useState` est polyvalent et simple : vous l'initialisez avec une valeur, et il renvoie une variable d'état et une fonction de mise à jour.

```jsx
import React, { useState } from 'react';

function Counter() {
  const [count, setCount] = useState(0);  // Initialise l'état et la fonction de mise à jour

  return (
    <div>
      <p>Vous avez cliqué {count} fois</p>
      <button onClick={() => setCount(count + 1)}>Cliquez ici</button>
    </div>
  );
}
```

**Explication du code** : `useState` initialise l'état (count) et fournit une fonction (`setCount`) pour mettre à jour cet état.

#### **2.** `useReducer`

Quand `useState` ne suffit plus, `useReducer` entre en jeu. Ce hook est parfait pour gérer une logique d'état complexe.

Il utilise une fonction reducer pour simplifier les mises à jour d'état et est particulièrement utile lorsque plusieurs variables d'état sont interdépendantes ou lorsque des actions doivent être déclenchées (dispatched).

Considérez-le comme une version supérieure pour gérer des scénarios d'état plus compliqués. Voici un exemple :

```jsx
import React, { useReducer } from 'react';

const initialState = { count: 0 };

function reducer(state, action) {
  switch (action.type) {
    case 'increment':
      return { count: state.count + 1 };
    case 'decrement':
      return { count: state.count - 1 };
    default:
      return state;
  }
}

function Counter() {
  const [state, dispatch] = useReducer(reducer, initialState);

  return (
    <div>
      <p>Compteur : {state.count}</p>
      <button onClick={() => dispatch({ type: 'increment' })}>+</button>
      <button onClick={() => dispatch({ type: 'decrement' })}>-</button>
    </div>
  );
}
```

**Explication du code** : `useReducer` est utile pour gérer des mises à jour d'état complexes, comme le traitement de plusieurs actions liées.

**3.** `useSyncExternalStore`  
`useSyncExternalStore` est un hook permettant d'intégrer des magasins d'état (stores) externes à React dans vos composants React.

Bien qu'il ne soit pas couramment utilisé, il est crucial si vous construisez votre propre bibliothèque de gestion d'état à partir de zéro.

```jsx
import React, { useSyncExternalStore } from 'react';

const externalStore = {
  subscribe: (callback) => {
    const interval = setInterval(callback, 1000);
    return () => clearInterval(interval);
  },
  getSnapshot: () => new Date().toLocaleTimeString(),
};

function Clock() {
  const time = useSyncExternalStore(externalStore.subscribe, externalStore.getSnapshot);
  return <div>{time}</div>;
}
```

**Explication du code** : `useSyncExternalStore` vous permet de connecter votre composant React à des sources de données non-React, comme des stores globaux.

### **Hooks d'effet**

**1.** `useEffect`  
Le hook `useEffect` exécute des effets de bord dans vos composants. Que vous interagissiez avec le DOM ou que vous récupériez des données, `useEffect` est votre outil privilégié. Il s'exécute par défaut après chaque rendu, mais vous pouvez personnaliser son comportement à l'aide d'un tableau de dépendances.

Cependant, vous devriez envisager d'utiliser des outils plus spécialisés ou des bibliothèques comme React Query pour les effets de bord basés sur des événements ou sur le rendu.

```jsx
import React, { useState, useEffect } from 'react';

function DataFetcher() {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetch('https://api.example.com/data')
      .then((response) => response.json())
      .then((data) => setData(data));
  }, []);  // Un tableau de dépendances vide signifie qu'il s'exécute une seule fois au montage

  return <div>{data ? JSON.stringify(data) : 'Chargement...'}</div>;
}
```

**Explication du code** : Le hook `useEffect` récupère des données lors du montage du composant. L'effet ne s'exécutera qu'une seule fois lorsque le tableau est vide.

**2.** `useLayoutEffect`  
`useLayoutEffect` fonctionne de manière similaire à `useEffect` mais s'exécute de façon synchrone juste après que le DOM a été mis à jour. Il est utilisé pour les opérations qui doivent se produire avant que le navigateur n'affiche l'interface utilisateur, comme la mesure d'éléments.

Utilisez-le avec parcimonie, car il s'exécute moins fréquemment que `useEffect`. Voici un exemple :

```jsx
import React, { useLayoutEffect, useRef } from 'react';

function Measure() {
  const divRef = useRef();

  useLayoutEffect(() => {
    console.log(divRef.current.getBoundingClientRect());
  }, []);

  return <div ref={divRef}>Mesurez-moi !</div>;
}
```

**Explication du code** : `useLayoutEffect` mesure les éléments du DOM avant que le navigateur ne redessine l'écran.

**3.** `useInsertionEffect`  
Exclusivement destiné aux développeurs de bibliothèques CSS-in-JS, `useInsertionEffect` s'exécute avant `useEffect` et `useLayoutEffect` pour garantir que les styles CSS sont insérés correctement. C'est une niche, mais c'est crucial pour maintenir l'intégrité du style dans des applications complexes.

```jsx
import React, { useInsertionEffect, useState } from 'react';

function StyledComponent() {
  const [text, setText] = useState('Survolez-moi !');

  useInsertionEffect(() => {
    const style = document.createElement('style');
    style.textContent = `
      .hovered {
        color: red;
        font-size: 24px;
        transition: color 0.3s ease;
      }
    `;
    document.head.appendChild(style);

    return () => {
      document.head.removeChild(style);
    };
  }, []);

  return (
    <div
      className="hovered"
      onMouseEnter={() => setText('Vous m\'avez survolé !')}
      onMouseLeave={() => setText('Survolez-moi !')}
    >
      {text}
    </div>
  );
}
```

**Explication du code** : Le hook `useInsertionEffect` est utilisé pour injecter des styles dans le DOM au moment de l'exécution, rendant le style du composant dynamique et limité à ce seul composant.

### **Hook de référence**

1. `useRef`  
`useRef` vous permet de faire persister des valeurs entre les rendus sans provoquer de nouveau rendu. C'est parfait pour stocker des valeurs mutables ou référencer des éléments du DOM. Que vous gériez des intervalles, stockiez un nœud DOM ou gardiez une trace de l'état précédent, `useRef` répond à vos besoins.

```jsx
import React, { useRef } from 'react';

function FocusInput() {
  const inputRef = useRef(null);

  const handleFocus = () => {
    inputRef.current.focus();
  };

  return (
    <div>
      <input ref={inputRef} type="text" />
      <button onClick={handleFocus}>Mettre le focus sur l'input</button>
    </div>
  );
}
```

**Explication du code :** Ce code React utilise `useRef` pour créer une référence à un élément d'entrée (input). Lorsque le bouton est cliqué, la fonction `handleFocus` déclenche la prise de focus du champ de saisie à l'aide de `inputRef.current.focus()`.

### **Hooks de performance**

**1.** `useMemo`  
Pour optimiser les performances, `useMemo` est votre allié. Il met en cache les résultats de calculs coûteux et ne les recalcule que lorsque les dépendances changent. Cela peut considérablement améliorer les performances, en particulier dans les scénarios impliquant des calculs lourds.

```jsx
import React, { useState, useMemo } from 'react';

function ExpensiveCalculation() {
  const [count, setCount] = useState(0);

  const expensiveComputation = useMemo(() => {
    return count * 100;
  }, [count]);

  return (
    <div>
      <p>Calcul coûteux : {expensiveComputation}</p>
      <button onClick={() => setCount(count + 1)}>Augmenter le compteur</button>
    </div>
  );
}
```

**Explication du code :** Ce code React utilise `useMemo` pour optimiser un calcul coûteux (`count * 100`). Le calcul n'est relancé que lorsque `count` change. Le bouton incrémente `count`, déclenchant une mise à jour de l'interface utilisateur avec le nouveau résultat.

**2.** `useCallback`  
`useCallback` est similaire à `useMemo`, mais il se concentre sur la mémorisation des fonctions de rappel (callback functions). C'est utile pour éviter les rendus inutiles des composants enfants en gardant les fonctions stables d'un rendu à l'autre.

```jsx
import React, { useState, useCallback } from 'react';

function Child({ onClick }) {
  return <button onClick={onClick}>Cliquez-moi</button>;
}

function Parent() {
  const [count, setCount] = useState(0);

  const handleClick = useCallback(() => {
    console.log('Cliqué');
  }, []);

  return (
    <div>
      <Child onClick={handleClick} />
      <p>Compteur : {count}</p>
      <button onClick={() => setCount(count + 1)}>Augmenter le compteur</button>
    </div>
  );
}
```

**Explication du code :** Ce code React utilise `useCallback` pour mémoriser la fonction `handleClick`, empêchant sa recréation à chaque rendu. Le composant `Child` utilise cette fonction pour son bouton. Le parent met à jour `count` indépendamment.

### **Hook de contexte**

1. `useContext`  
Le hook `useContext` simplifie l'accès aux valeurs de contexte. Il lit la valeur du fournisseur de contexte le plus proche et fonctionne de manière transparente à travers les composants imbriqués. Cela facilite la gestion des états globaux ou des thèmes.

```jsx
import React, { useContext, createContext } from 'react';

const ThemeContext = createContext('light');

function ThemedButton() {
  const theme = useContext(ThemeContext);
  return <button>{theme}</button>;
}

function App() {
  return (
    <ThemeContext.Provider value="dark">
      <ThemedButton />
    </ThemeContext.Provider>
  );
}
```

**Explication du code** : Ce code React utilise `createContext` pour créer un `ThemeContext`. `useContext` accède à la valeur du contexte, l'affichant dans le bouton. Le composant `App` fournit "dark" comme thème à `ThemedButton`.

### **Hook de transition**

1. `useTransition`  
`useTransition` vous permet de marquer des mises à jour d'état spécifiques comme étant de faible priorité, améliorant ainsi l'expérience utilisateur en maintenant l'application plus réactive pendant des calculs ou des transitions intensifs. Cela améliore l'expérience utilisateur en rendant l'application plus fluide.

```jsx
import React, { useState, useTransition } from 'react';

function TransitionComponent() {
  const [count, setCount] = useState(0);
  const [isPending, startTransition] = useTransition();

  const handleClick = () => {
    startTransition(() => {
      setCount((prevCount) => prevCount + 1);
    });
  };

  return (
    <div>
      <button onClick={handleClick}>Augmenter le compteur</button>
      {isPending ? <p>Chargement...</p> : <p>Compteur : {count}</p>}
    </div>
  );
}
```

**Explication du code :** Ce code utilise `useTransition` pour incrémenter `count` sans bloquer l'interface utilisateur. Pendant la mise à jour de l'état, `isPending` affiche "Chargement...". Cliquer sur le bouton déclenche une transition d'état fluide et non bloquante.

### **Quelques autres Hooks**

**1.** `useDeferredValue`  
Semblable à `useTransition`, `useDeferredValue` aide à différer les mises à jour d'état pour maintenir la réactivité de l'application. Il planifie les mises à jour pour qu'elles se produisent au moment optimal, améliorant l'expérience utilisateur sans intervention manuelle.

```jsx
import React, { useState, useDeferredValue } from 'react';

function DeferredComponent() {
  const [value, setValue] = useState('');
  const deferredValue = useDeferredValue(value);

  return (
    <div>
      <input value={value} onChange={(e) => setValue(e.target.value)} />
      <p>Valeur différée : {deferredValue}</p>
    </div>
  );
}
```

**Explication du code** : `useDeferredValue` retarde la mise à jour de `deferredValue` pour garantir que l'interface utilisateur reste réactive.

**2.** `useDebugValue`  
`useDebugValue` est un hook principalement destiné au débogage. Il vous permet d'étiqueter les hooks personnalisés dans les React DevTools, facilitant ainsi le suivi et le débogage de vos hooks.

```jsx

import React, { useDebugValue, useState } from 'react';

function useCustomHook(value) {
  useDebugValue(value ? "A une valeur" : "Aucune valeur"); return value; }
function DebugComponent() { const [value, setValue] = useState(''); const customValue = useCustomHook(value);

return (
 <input value={value} onChange={(e) => setValue(e.target.value)} />
Valeur : {customValue}
); }
```

**Explication du code :** Ce code utilise `useDebugValue` pour afficher "A une valeur" ou "Aucune valeur" dans les React DevTools en fonction de `value`. `useCustomHook` est utilisé dans `DebugComponent` pour suivre l'état de l'entrée et l'afficher dynamiquement.

**3.** `useId`  
`useId` génère des identifiants uniques pour les éléments, garantissant que les entrées de formulaire et les étiquettes (labels) sont correctement liées sans conflits. C'est particulièrement utile lorsqu'on traite des éléments répétés dynamiquement.

```javascript

import React, { useId } from 'react';

function FormComponent() {
  const id = useId();

  return (
    <div>
      <label htmlFor={id}>Nom : </label>
      <input id={id} type="text" />
    </div>
  );
}
```

**Explication du code** : `useId` garantit que les éléments de formulaire ont des identifiants uniques, évitant ainsi les conflits potentiels.

## Conclusion

Les React Hooks peuvent sembler intimidants au début, mais avec ce guide, vous êtes bien équipé pour les manipuler. Maîtriser ces hooks améliore vos compétences en React et rend votre processus de développement plus fluide et efficace.

Pour approfondir vos connaissances et pratiquer concrètement, consultez mon React Bootcamp complet, où vous trouverez des défis interactifs, des vidéos et des fiches récapitulatives pour renforcer votre savoir.