---
title: Comment utiliser React Context dans votre projet – Guide pour débutants
subtitle: ''
author: Benedicta Onyebuchi
co_authors: []
series: null
date: '2024-01-05T20:06:06.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-react-context
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/Learn-With-Benedicta.png
tags:
- name: React
  slug: react
- name: React context
  slug: react-context
- name: 'State Management '
  slug: state-management
seo_title: Comment utiliser React Context dans votre projet – Guide pour débutants
seo_desc: "As beginners, managing state in React applications can be challenging,\
  \ especially when passing and utilizing props in deeply nested components. \nThe\
  \ usual way of passing information from a main component to its smaller parts —\
  \ like a parent passing d..."
---

En tant que débutants, la gestion de l'état dans les applications React peut être difficile, surtout lors du passage et de l'utilisation de props dans des composants profondément imbriqués. 

La manière habituelle de transmettre des informations d'un composant principal à ses parties plus petites — comme un parent transmettant des données à un enfant, puis à un petit-enfant — peut devenir compliquée et fastidieuse, surtout lorsque nous devons accéder à quelque chose profondément dans la hiérarchie.

Dans cet article, nous allons explorer comment fonctionne l'API React Context, ses cas d'utilisation et un projet exemple utilisant ce concept.

## Qu'est-ce que React Context ?

React Context nous fournit un moyen de transmettre des données à travers l'arborescence des composants jusqu'à l'endroit où nous en avons besoin, sans avoir à passer manuellement des props à chaque niveau.

Il agit comme un espace de stockage global pour tous vos composants dans votre projet.

## En quoi React Context est-il différent du passage de props ?

Dans le **passage de props**, les données sont transmises du composant parent au composant enfant. Si un enfant de ce composant a besoin de la même prop, elle est transmise jusqu'à ce que le composant requis obtienne les données. 

Bien que simple, cela peut devenir complexe lors de la traversée de structures profondément imbriquées, ce qui entraîne le "prop drilling".

![Image](https://www.freecodecamp.org/news/content/images/2024/01/context-1.png)
_Une représentation picturale du passage de props_

En revanche, React Context permet de transmettre des données du composant parent à n'importe quel composant imbriqué qui en a besoin, simplifiant ainsi le processus. 

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-02-114317.png)
_Une représentation de React Context._

## Qu'est-ce que le Prop Drilling ?

Le Prop Drilling fait référence à une situation où ce passage de props devient compliqué en raison de la nécessité de les transmettre à travers plusieurs couches de composants. 

Lorsque les données sont transmises à travers de nombreuses couches, chaque composant intermédiaire doit recevoir et transmettre les données, même s'il ne les utilise pas lui-même.

Voici un exemple :

```javascript
// App.js

import React, { useState } from 'react';

const GrandchildComponent = ({ dataFromChild }) => {
  return (
    <div>
      <p>Nom d'utilisateur dans le petit-enfant : {dataFromChild.username}</p>
    </div>
  );
};

const ChildComponent = ({ dataFromParent }) => {
  return (
    <div>
      <p>Votre email : {dataFromParent.email}</p>
      <GrandchildComponent dataFromChild={dataFromParent} />
    </div>
  );
};

const ParentComponent = () => {
  const [userData, setUserData] = useState({
    username: 'benny_dicta',
    email: 'benedictaonyebuchi@gmail.com',
  });

  return (
    <div>
      <h1>Bienvenue, {userData.username} !</h1>
      <ChildComponent dataFromParent={userData} />
    </div>
  );
};

const App = () => {
  return <ParentComponent />;
};

export default App;

```

Le code ci-dessus montre un cas typique de prop drilling où les données sont transmises du `ParentComponent` au composant `GrandChild` même lorsqu'elles ne sont pas nécessaires par ce composant.

* `ParentComponent` est le composant de niveau supérieur qui contient certaines données (`userData`).
* `ChildComponent` est un enfant de `ParentComponent` et reçoit `dataFromParent` en tant que prop. Il rend également un `GrandChildComponent`, transmettant la prop reçue plus loin.
* `GrandChildComponent` est profondément imbriqué et reçoit la prop `dataFromChild`. Il rend les données dans son interface utilisateur.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-02-115808.png)
_Une représentation d'une structure de projet simple_



## Quand choisir React Context

* Pour des projets simples et directs, le passage de props serait adéquat.
* Pour des projets complexes nécessitant que les données traversent plusieurs couches imbriquées, React Context offre une solution plus propre.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-02-120902.png)
_Une représentation d'une application profondément imbriquée_



La différence picturale entre les deux approches peut être vue ici. 

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-02-124809.png)
_Une représentation picturale de la différence entre React Context et le prop drilling._



## Quels sont les cas d'utilisation de l'API React Context ?

Voici quelques cas d'utilisation de React Context :

1. Lorsque le prop drilling devient compliqué : Imaginez devoir transmettre une prop à travers plusieurs couches de composants juste pour atteindre celui qui en a besoin. L'API Context élimine ce casse-tête de prop drilling.
2. Besoin de données globales : Lorsque plusieurs composants ont besoin d'accéder aux mêmes données (par exemple : statut d'authentification de l'utilisateur, préférences de thème, etc.), l'utilisation du contexte les rend accessibles sans transmission redondante de props.
3. Composants thématiques : Si votre application nécessite de changer de thèmes, comme les modes clair et sombre, et que vous souhaitez que les composants profondément dans l'arborescence s'adaptent dynamiquement aux changements de thème, l'API Context rend cela transparent.
4. Imbrication multi-niveaux : Dans les arborescences de composants profondément imbriqués, la transmission de props à travers la hiérarchie devient impraticable. Le contexte offre une solution plus propre pour partager des données à travers divers niveaux.

## Comment utiliser l'API React Context

#### Étape #1 - Créer un Contexte

```javascript
import { createContext } from 'react';

const MyContext = createContext();
export default MyContext;

```

#### Étape #2 - Envelopper votre App avec le Fournisseur de Contexte

```javascript
import React from 'react';
import MyContext from './MyContext';

const App = () => {
  const sharedValue = 'Ceci est une valeur partagée';

  return (
    <MyContext.Provider value={sharedValue}>
      {/* Vos composants vont ici */}
    </MyContext.Provider>
  );
};

export default App;

```

#### Étape #3 - Consommer le Contexte dans les Composants

```javascript
import React, { useContext } from 'react';
import MyContext from './MyContext';

const MyComponent = () => {
  const sharedValue = useContext(MyContext);

  return <p>{sharedValue}</p>;
};

export default MyComponent;

```

## Les trois parties importantes de l'API React Context.

Dans cette section, nous allons parler des trois parties importantes de l'API React Context : Provider, Context et Consumer.

### Provider

Il s'agit d'un composant utilisé pour envelopper des composants afin d'accéder à la valeur du contexte. C'est ici que vous passez les valeurs que vous souhaitez partager dans toute l'arborescence des composants en utilisant la prop `value`. 

```javascript
import React from 'react';
import MyContext from './MyContext';

const App = () => {
  const sharedValue = 'Ceci est une valeur partagée';

  return (
    <MyContext.Provider value={sharedValue}>
     {children} {/*tous les composants dans son sous-arbre*/}
    </MyContext.Provider>
  );
};

export default App;
```


Dans le code ci-dessus, le contexte est importé et le `.Provider` est ajouté au contexte, `MyContext`. Cela rend la prop passée au Provider disponible pour tous ses enfants. C'est-à-dire, les composants dans son sous-arbre.

### Context

Cela agit comme l'espace de stockage où les données sont stockées. Il se compose de deux parties :

* `createContext()` — Cela crée l'objet global et crée le contexte.
* `useContext()` — Cela consomme les informations mises à disposition par le fournisseur.

```javascript
/*MyComponent.js*/

import React, { createContext, useContext } from 'react';

export const MyContext = createContext();

const MyComponent = () => {
  const sharedValue = useContext(MyContext);

  return <p>{sharedValue}</p>;
};

export default MyComponent;

```

Dans le code ci-dessus, le Contexte est créé en assignant le hook `useContext` importé à la fonction `MyComponent`.

### Consumer

Le composant Consumer est utilisé pour consommer les données partagées dans un composant. Il permet aux composants de s'abonner aux changements de contexte et d'accéder à la valeur partagée. Nous ne verrons peut-être pas le consommateur en tant que tel, mais il utilisera les informations rendues par le fournisseur. 

Il doit toujours être imbriqué à l'intérieur du Provider car le Provider sera rendu en premier pour transmettre les données aux composants qui les consomment. En d'autres termes, il doit exister avant de pouvoir le consommer.

```javascript
import React, { useContext } from 'react';
import MyContext from './MyComponent';

const MyComponent = () => {
  const sharedValue = useContext(MyContext);

  return <p>{sharedValue}</p>;
};

export default MyComponent;

```

Dans le code, le composant `MyComponent` utilise le contexte `MyContext` créé précédemment en utilisant `useContext`.

## Comment créer une application de changement de thème en utilisant React Context.

Implémentons une application simple de changement de thème en utilisant l'API React Context.

#### Étape #1

Dans le dossier **src**, créez un dossier **context**. Ensuite, créez un nouveau fichier appelé `ThemeContext.js`. 

```javascript
import React, { createContext, useContext, useState } from 'react';

const ThemeContext = createContext();

const ThemeProvider = ({ children }) => {
  const [theme, setTheme] = useState('light');

  const toggleTheme = () => {
    setTheme((prevTheme) => (prevTheme === 'light' ? 'dark' : 'light'));
  };

  return (
    <ThemeContext.Provider value={{ theme, toggleTheme }}>
      {children}
    </ThemeContext.Provider>
  );
};

const useTheme = () => {
  return useContext(ThemeContext);
};

export { ThemeProvider, useTheme };
```


##### Explication :

* Nous avons commencé par créer un contexte (`createContext()`) et assigner une variable `ThemeContext` à celui-ci, qui servira de stockage pour les données de thème.
* Dans le composant `ThemeProvider`, nous avons utilisé le hook `useState` pour gérer le thème actuel et également créer un basculement qui aidera à passer du mode clair au mode sombre.
* Le `<ThemeContext.Provider>` enveloppe les enfants, rendant les props qui lui sont passées disponibles pour chaque composant dans son sous-arbre.
* Le composant `useTheme` est un hook personnalisé qui utilise `useContext()` pour consommer le contexte `ThemeContext`.

#### Étape #2

Dans votre dossier **src**, créez un fichier `ThemedComponent.js`. Copiez et collez le code ci-dessous dans le fichier :

```javscript
import React from 'react';
import { useTheme } from './context/ThemeContext';

const ThemedComponent = () => {
  const { theme, toggleTheme } = useTheme();

  return (
    <div style={{ background: theme === 'light' ? '#fff' : '#333', color: theme === 'light' ? '#333' : '#fff' }}>
      <h2>Composant thématique</h2>
      <p>Thème actuel : {theme}</p>
      <button onClick={toggleTheme}>Changer de thème</button>
    </div>
  );
};

export default ThemedComponent;
```


##### Explication :

* En utilisant le hook `useTheme()`, vous pouvez accéder et consommer le contexte de thème. Souvenez-vous que nous avons passé `theme` et la fonction `toggleTheme` au `ThemeContext.Provider`.
* Le style du composant change dynamiquement en fonction du thème actuel. Cela montre comment les composants peuvent s'adapter aux changements d'état global gérés par le contexte.
* Le bouton déclenche la fonction `toggleTheme` pour basculer entre le mode clair et le mode sombre.

#### Étape #3

Dans votre fichier `App.js`, copiez et collez le code ci-dessous :

```javascript
import React from 'react';
import { ThemeProvider } from './context/ThemeContext';
import ThemedComponent from './ThemedComponent.js';

const App = () => {
  return (
    <ThemeProvider>
      <div>
        <h1>Application thématique</h1>
        <ThemedComponent />
      </div>
    </ThemeProvider>
  );
};

export default App;
```


##### Explication :

* `<App />` est le composant principal de l'application où le `ThemeProvider` est utilisé pour envelopper toute l'application et donner accès au contexte de thème à tous les composants dans le `ThemeProvider`.
* Le `ThemedComponent` est rendu, montrant le résultat des composants ayant accès au contexte.

Après une implémentation réussie du contexte, le résultat devrait être comme suit :

![Image](https://www.freecodecamp.org/news/content/images/2024/01/ezgif.com-video-to-gif-converter.gif)
_Un simple changement de thème utilisant React Context._

Cela devrait vous aider à implémenter l'API React Context dans votre projet.

## Conclusion

Dans cet article, vous avez appris ce qu'est le contexte, le fournisseur de contexte, le consommateur de contexte, et comment créer un wrapper de fournisseur React qui gère la valeur d'un contexte à travers l'état du composant. 

Vous avez également appris ce qu'est le passage de props, le prop drilling et ses inconvénients par rapport à React Context. 

Enfin, vous avez appris comment récupérer des valeurs d'un contexte en utilisant le hook `useContext` en construisant un simple commutateur de thème.

## Ressources

* [Documentation officielle de React sur l'API Context](https://react.dev/reference/react/createContext)
* [React Context et Hooks - Tutoriel Vidéo](https://www.youtube.com/watch?v=6RhOzQciVwI)

Merci d'avoir lu !