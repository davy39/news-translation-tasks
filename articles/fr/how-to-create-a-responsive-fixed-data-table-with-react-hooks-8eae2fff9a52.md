---
title: Comment créer un Fixed-Data-Table réactif avec React Hooks
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-12T17:15:15.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-responsive-fixed-data-table-with-react-hooks-8eae2fff9a52
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca76f740569d1a4ca772f.jpg
tags:
- name: Functional Programming
  slug: functional-programming
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment créer un Fixed-Data-Table réactif avec React Hooks
seo_desc: 'By Yazeed Bzadough

  One of my projects uses a library called Fixed-Data-Table-2 (FDT2), and it’s great
  for efficiently rendering tons of rows of data.

  Their documentation demonstrates a responsive table that resizes based on the browser’s
  width and he...'
---

Par Yazeed Bzadough

L'un de mes projets utilise une bibliothèque appelée [Fixed-Data-Table-2](https://schrodinger.github.io/fixed-data-table-2/) (FDT2), et elle est excellente pour rendre efficacement des tonnes de lignes de données.

Leur documentation [démontre un tableau réactif](https://schrodinger.github.io/fixed-data-table-2/example-responsive.html) qui redimensionne en fonction de la largeur et de la hauteur du navigateur.

![](https://cdn-media-1.freecodecamp.org/images/1*0fuT32J4E_8xiHjivI9q5A.png)

J'ai pensé qu'il serait intéressant de partager cet exemple en utilisant React Hooks.

### Qu'est-ce que React Hooks ?

Ce sont des fonctions qui vous donnent des fonctionnalités React comme l'état et les hooks de cycle de vie sans classes ES6.

Certains avantages sont :

- isoler la logique d'état, rendant plus facile les tests
- partager la logique d'état sans props de rendu ou composants d'ordre supérieur
- séparer les préoccupations de votre application en fonction de la logique, et non des hooks de cycle de vie
- éviter les classes ES6, car elles sont capricieuses, **pas réellement des classes**, et posent problème même pour les développeurs JavaScript expérimentés

Pour plus de détails, voir [l'introduction officielle des Hooks de React](https://reactjs.org/docs/hooks-intro.html).

#### ATTENTION : Ne pas utiliser en production !

Au moment de la rédaction de cet article, **les Hooks sont en alpha. Leur API peut changer à tout moment.**

Je vous recommande d'expérimenter, de vous amuser et d'utiliser les Hooks dans vos projets secondaires, mais pas dans le code de production jusqu'à ce qu'ils soient stables.

### L'objectif

![](https://cdn-media-1.freecodecamp.org/images/1*Eb3EXmna0JSVlnUfp4GIBg.png)

Nous allons construire un Fixed-Data-Table réactif. Il ne sera ni trop étroit ni trop large pour notre page, il s'adaptera parfaitement !

### Installation

Voici les liens [GitHub](https://github.com/yazeedb/Responsive-FDT2-Hooks/) et [CodeSandbox](https://codesandbox.io/s/1vpm1z193j).

```
git clone https://github.com/yazeedb/Responsive-FDT2-Hooks/
cd Responsive-FDT2-Hooks
npm install
```

La branche `master` contient le projet terminé, donc vérifiez la branche `start` si vous souhaitez suivre.

`git checkout start`

Et exécutez le projet.

`npm start`

L'application devrait s'exécuter sur `localhost:3000`. Commençons à coder.

#### Importation des styles de tableau

Tout d'abord, vous voudrez importer la feuille de style de FDT2 dans `index.js`, afin que votre tableau ne semble pas déformé.

![](https://cdn-media-1.freecodecamp.org/images/1*NeHwi_fxuf7Ojhd4edJ4cg.png)

#### Génération de fausses données

Notre tableau a besoin de données, n'est-ce pas ? Créez un fichier dans le dossier `src` appelé `getData.js`.

Nous utiliserons la bibliothèque géniale [faker.js](https://www.npmjs.com/package/faker) pour générer nos données. Elle est déjà venue avec votre `npm install`.

Voici la source si vous voulez copier/coller.

```js
import faker from 'faker';

const createFakeRowData = () => ({
  firstName: faker.name.firstName(),
  lastName: faker.name.lastName(),
  email: faker.internet.email(),
  city: faker.address.city(),
  salary: faker.random
    .number({
      min: 50000,
      max: 500000
    })
    .toLocaleString('en-US', {
      style: 'currency',
      currency: 'USD'
    })
});

export default () => Array.from({ length: 2000 }, createFakeRowData);
```

`createFakeRowData` retourne un objet avec un nom complet, un email, une ville et un salaire en dollars américains.

Notre fonction exportée en retourne 2000.

### Le tableau non réactif

Nous avons nos données, codons le tableau maintenant.

En haut de `index.js`, importons nos données et les composants FDT2.

```jsx
import { Table, Column, Cell } from 'fixed-data-table-2';
import getData from './getData';
```

Et utilisez-les comme suit.

```jsx
function App() {
  const data = getData();

  return (
    <div className="App">
      <Table
        rowHeight={50}
        rowsCount={data.length}
        headerHeight={50}
        width={1000}
        height={500}
      >
        <Column
          columnKey="firstName"
          header={<Cell>First Name</Cell>}
          width={130}
          cell={({ rowIndex, columnKey }) => {
            return <Cell>{data[rowIndex][columnKey]}</Cell>;
          }}
        />
        <Column
          columnKey="lastName"
          header={<Cell>Last Name</Cell>}
          width={130}
          cell={({ rowIndex, columnKey }) => {
            return <Cell>{data[rowIndex][columnKey]}</Cell>;
          }}
        />
        <Column
          columnKey="email"
          header={<Cell>Email</Cell>}
          width={320}
          cell={({ rowIndex, columnKey }) => {
            return <Cell>{data[rowIndex][columnKey]}</Cell>;
          }}
        />
        <Column
          columnKey="city"
          header={<Cell>City</Cell>}
          width={180}
          cell={({ rowIndex, columnKey }) => {
            return <Cell>{data[rowIndex][columnKey]}</Cell>;
          }}
        />
        <Column
          columnKey="salary"
          header={<Cell>Salary</Cell>}
          width={180}
          cell={({ rowIndex, columnKey }) => {
            return <Cell>{data[rowIndex][columnKey]}</Cell>;
          }}
        />
      </Table>
    </div>
  );
}
```

Nous configurons le tableau avec nos données et créons une `Column` pour chaque champ que nous voulons afficher.

Les objets `getData` contiennent un prénom/nom, un email, une ville et un salaire, donc nous avons besoin d'une colonne pour chacun.

Notre UI ressemble maintenant à ceci.

![](https://cdn-media-1.freecodecamp.org/images/1*s8ekNyjl6FPxzeZnlprF2g.png)

Essayez de redimensionner la fenêtre de votre navigateur, vous remarquerez qu'il n'est pas du tout réactif. Il est soit trop grand soit trop petit pour votre viewport et peut laisser un espace excessif.

### Échappée vers l'impur

Comme nous l'avons appris, la nature déclarative de React vous permet d'écrire votre UI en utilisant des fonctions pures, déterministes et facilement testables.

**La même entrée doit toujours retourner la même sortie.**

Cependant, nous devons parfois visiter le monde "impur", pour la manipulation du DOM, l'ajout d'événements tels que les écouteurs, les abonnements et les temporisateurs.

#### HOCS et render props

Les render props et les composants d'ordre supérieur (HOCS) sont la solution standard, mais ont certains compromis que les Hooks essaient maintenant de résoudre.

### Utilisation des Hooks

Les Hooks sont la nouvelle issue de secours pour utiliser du code impératif. Dans notre cas, obtenir la taille de la fenêtre est l'effet que nous recherchons.

Créez un nouveau fichier appelé `useWindowSize.js`.

Nous aurons besoin de deux choses pour y parvenir :

1. Écouter l'événement `resize` de la fenêtre, afin d'être informé lorsqu'elle change
2. Enregistrer la largeur/hauteur pour la partager avec notre tableau

Deux hooks peuvent aider :

1. `useEffect`
2. `useState`

#### useEffect

Cela remplacera probablement vos hooks de cycle de vie `componentDidMount`, `componentDidUpdate` et `componentWillUnmount` une fois qu'il sera stabilisé.

`useEffect` est parfait pour la plupart des logiques d'initialisation et de lecture du DOM.

C'est là que nous configurerons nos écouteurs d'événements de redimensionnement de la fenêtre.

Pour plus de détails, voir [la documentation officielle](https://reactjs.org/docs/hooks-reference.html#useeffect).

#### `useState`

Super simple, ce Hook retourne une valeur d'état et une fonction pour la mettre à jour. Une fois que nous avons capturé la largeur/hauteur de la fenêtre, nous ferons suivre `useState`.

### Écriture de notre Hook personnalisé

Selon [la documentation officielle](https://reactjs.org/docs/hooks-custom.html#extracting-a-custom-hook) :

> **Un Hook personnalisé est une fonction JavaScript dont le nom commence par "use" et qui peut appeler d'autres Hooks.**

Notre Hook personnalisé s'appellera `useWindowSize`, et il appellera les hooks `useState` et `useEffect`.

Ce Hook est principalement inspiré de `useWindowSize` de [Gabe Ragland](https://medium.com/@gabe_ragland) sur [useHooks.com](https://gist.github.com/gragland/4e3d9b1c934a18dc76f585350f97e321).

```jsx
// `useWindowSize.js`

import { useState, useEffect } from 'react';

export default () => {
  const getSize = () => {
    return {
      width: window.innerWidth,
      height: window.innerHeight
    };
  };

  const [windowSize, setWindowSize] = useState(getSize);

  useEffect(() => {
    const handleResize = () => {
      setWindowSize(getSize());
    };

    window.addEventListener('resize', handleResize);

    return () => {
      window.removeEventListener('resize', handleResize);
    };
  }, []);

  return windowSize;
};
```

Décomposons cela.

#### Obtention de la taille de la fenêtre

```js
const getSize = () => {
  return {
    width: window.innerWidth,
    height: window.innerHeight
  };
};
```

`getSize` retourne simplement la `innerWidth` et la `innerHeight` de la fenêtre.

#### Initialisation de useState

```js
const [windowSize, setWindowSize] = useState(getSize);
```

`useState` peut prendre une valeur initiale ou une fonction qui retourne une valeur.

Dans ce cas, nous voulons les dimensions de la fenêtre pour commencer, donc `getSize` est l'initialisateur parfait.

`useState` retourne ensuite un tableau, le premier index est la valeur et le second index est la fonction de mise à jour.

#### Configuration de useEffect

```js
useEffect(() => {
  const handleResize = () => {
    setWindowSize(getSize());
  };

  window.addEventListener('resize', handleResize);

  return () => {
    window.removeEventListener('resize', handleResize);
  };
}, []);
```

`useEffect` prend une fonction qui exécutera votre effet souhaité.

Chaque fois que la taille de la fenêtre change, `handleResize` définit l'état en donnant à `setWindowSize` la dernière largeur/hauteur.

**Logique de nettoyage**

Notre fonction d'effet retourne ensuite une **nouvelle fonction**, que `useEffect` reconnaît comme une logique de nettoyage.

```js
return () => {
  window.removeEventListener('resize', handleResize);
};
```

Lorsque nous quittons la page ou désinstallons d'une manière ou d'une autre notre composant, cette fonction de nettoyage s'exécute et supprime l'écouteur d'événement `resize`. Cela aide à prévenir les fuites de mémoire.

**Second argument de useEffect**

Le premier argument de `useEffect` est la fonction gérant notre logique, mais nous lui avons également donné un second argument : un tableau vide.

```js
useEffect(() => { ... }, []); // tableau vide
```

**Pourquoi un tableau vide ?**

Le second argument de `useEffect` est un tableau de valeurs à surveiller. Si l'une de ces valeurs change, `useEffect` s'exécute à nouveau.

Nous définissons/supprimons simplement des écouteurs d'événements, ce qui ne doit se produire qu'une seule fois.

Un tableau vide est la manière dont nous communiquons "exécuter une seule fois" à `useEffect`.

> Tableau vide = aucune valeur ne change jamais = exécuter une seule fois

#### Retourner windowSize

Maintenant que notre effet est configuré, retournez simplement `windowSize`. Au fur et à mesure que le navigateur est redimensionné, `windowSize` sera mis à jour.

![](https://cdn-media-1.freecodecamp.org/images/1*g-8DAewSVWqhldzO1uYguw.png)

### Utilisation de notre Hook personnalisé

Il est temps de lancer notre Hook sur Fixed-Data-Table2 !

De retour dans `index.js`, allez-y et importez `useWindowSize`.

![](https://cdn-media-1.freecodecamp.org/images/1*LlF4n8uG10zDXDLWP3ti4A.png)

Et utilisez-le comme suit.

![](https://cdn-media-1.freecodecamp.org/images/1*X8Fl8ZHN1RN9rIKnhng5Ug.png)

Pour le plaisir, vous pouvez `console.log(windowSize)` et le voir se mettre à jour en temps réel.

![](https://cdn-media-1.freecodecamp.org/images/1*lU6qV0tPmuM1zxrRjxT3gQ.gif)

Cool, nous obtenons un objet de la `width` et de la `height` de la fenêtre !

Au lieu de coder en dur la largeur et la hauteur de notre tableau, nous pouvons utiliser l'état exposé par notre Hook.

![](https://cdn-media-1.freecodecamp.org/images/1*ufGH_7yvDH8IvdZA3JuOyA.png)

Maintenant, votre tableau devrait s'ajuster aux dimensions de la fenêtre.

![](https://cdn-media-1.freecodecamp.org/images/1*jwBuYI8qvS6NZjeL8-8m9g.gif)

J'espère que vous avez apprécié ce tutoriel !