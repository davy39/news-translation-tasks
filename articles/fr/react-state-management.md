---
title: Gestion d'état dans React – Quand et où utiliser l'état
subtitle: ''
author: Timothy Olanrewaju
co_authors: []
series: null
date: '2024-02-05T21:06:27.000Z'
originalURL: https://freecodecamp.org/news/react-state-management
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/rahul-mishra-XXMA-8fBB-g-unsplash.jpg
tags:
- name: React
  slug: react
- name: 'State Management '
  slug: state-management
seo_title: Gestion d'état dans React – Quand et où utiliser l'état
seo_desc: "State management is a crucial concept in React, which is one of the most\
  \ popular JavaScript libraries in the world for building dynamic user interfaces.\
  \ \nDue to its importance in handling data, it is essential know how to manage state,\
  \ when you need ..."
---

La gestion d'état est un concept crucial dans React, qui est l'une des bibliothèques JavaScript les plus populaires au monde pour construire des interfaces utilisateur dynamiques. 

En raison de son importance dans la gestion des données, il est essentiel de savoir comment gérer l'état, quand vous en avez besoin et où il peut être placé dans les composants de vos applications. 

Cet article plonge dans le monde de la gestion d'état dans React, offrant un guide complet pour vous aider à gérer l'état efficacement. Cet article s'adresse aux développeurs React débutants et intermédiaires qui souhaitent comprendre comment fonctionnent les états.

## Qu'est-ce que l'état ?

L'état peut être défini comme un objet qui contient des données qui changent au fil du temps dans une application. En d'autres termes, l'état est un stockage de données dynamique qui fournit un mécanisme permettant aux composants de gérer, de suivre les données changeantes et de déclencher un nouveau rendu lorsqu'il est mis à jour. 

Grâce à la modularisation dans React, l'état sert de conteneur qui encapsule les données pertinentes, la logique et le comportement au sein d'un composant. 

Maintenant que vous savez ce que signifie l'état, vous pouvez visualiser une application même avant de la construire et avoir une idée des données qui seraient stockées dans différents états. Cela nous amène à un point que j'aime appeler : « Penser en React ». 

Cette terminologie inventée peut être décrite comme l'image mentale qu'un développeur React a sur la manière de construire une application de la « manière React ». En appliquant les connaissances sur le maintien des composants purs, le passage des props des composants parents aux composants enfants, le flux de données unidirectionnel, la remontée des états, et bien d'autres aspects intégraux de React.

## Quand utiliser l'état

Lors de la construction d'une application, les données jouent un rôle intégral dans ce qui est affiché ou stocké. Il en va de même pour la construction d'applications web dans React, où les composants affichent ou opèrent sur des données — qui peuvent être des entrées utilisateur, des données récupérées depuis des API, ou tout autre contenu dynamique. Lorsqu'il est nécessaire d'obtenir des données qui doivent être mises à jour à l'intérieur d'un composant, nous utilisons l'état.

Pour mieux comprendre cela, examinons un exemple d'une application simple de liste de tâches qui accepte principalement des éléments saisis qui seront éventuellement ajoutés à une liste affichée. 

Les noms des éléments seront définis via une entrée de texte avant d'être ajoutés dynamiquement à un tableau d'éléments. 

Nous avons donc identifié deux aspects impliquant des données qui changeraient lorsqu'ils sont déclenchés. Toute mise à jour des données entraînera un nouveau rendu du composant. Ces deux aspects nécessitent le hook `useState` pour mettre à jour leurs données et exécuter la logique respective qui leur est attachée.

```react
const [name, setName] = useState(" ")
const [items, setItems] = useState([]);

```

Ci-dessus, voici la représentation des fonctions de hook `useState` qui permettent aux composants d'avoir des variables d'état. En ce qui concerne notre exemple de l'application de liste de tâches, nous avons initialisé notre fonction `useState` avec une chaîne vide (" ") pour les noms des éléments et un tableau vide (`[ ]`) pour les éléments. 

Les fonctions `useState` consistent en une affectation par déstructuration qui extrait les valeurs d'un tableau ou les propriétés d'un objet. Dans ce cas, nous extrayons deux valeurs retournées par les fonctions `useState`. 

`name` et `items` contiennent la valeur actuelle de la variable d'état. Tandis que `setName` et `setItems` sont les fonctions utilisées pour mettre à jour la valeur des variables d'état. 

Nous pouvons ajouter les composants `Header`, `Nav`, `ListArea` et `Footer` au JSX du composant `App`. Notre composant racine devrait ressembler à ceci :

```react
import { useState } from "react";

export default function App() {
  	const [items, setItems] = useState([]);
	const [name, setName] = useState(" ")
  return (
    <div>
      <Header />
      <Nav />
      <ListArea />
      <Footer />
    </div>
  );
}
```

Les composants individuels avec leurs JSX devraient ressembler à ceci :

```react
function Header() {
  return <h2>Liste de tâches</h2>;
}

function Nav() {
  return (
    <>
      <input type="text"/>
      <button>Ajouter</button>
    </>
  );
}

function ListArea() {
  return (
    <>
      <ul>
        <li></li>
      </ul>
    </>
  );
}

function Footer() {
  return (
    <>
      <p>Vous avez des éléments dans votre panier</p>
    </>
  );
}
```

![Image](https://www.freecodecamp.org/news/content/images/2024/02/image-33.png)
_Comment nos JSX de composants apparaissent dans le navigateur_

Ceci est une représentation simple de notre liste de tâches. Ensuite, nous ajouterons une logique et ferons en sorte que les états prennent vie. Pour l'instant, les états résident dans le composant `App`.

## Où utiliser l'état

Lors de l'utilisation de l'état, il est important de noter qu'il existe deux types d'états dans le développement React :

### État global

Ce sont des états accessibles à chaque composant de l'application. Ils sont toujours déclarés et situés dans le composant racine de votre application avant que le JSX ne soit retourné.

Un état peut être considéré comme un état global s'il s'agit d'une donnée accessible parmi plusieurs composants, aidant ainsi la communication entre les composants de l'application.

### État local

Les états locaux font référence aux données internes maintenues par un composant. Les états locaux sont situés dans les composants parents d'une application. Ils ne sont nécessaires et ne peuvent être accessibles que dans le composant. 

En utilisant l'état local, les composants peuvent indépendamment changer et gérer leurs données, ce qui conduit à un partitionnement au sein de l'application.

En regardant nos états déclarés dans l'application de liste de tâches, nous pouvons dire que `name` est un état local et `items` est un état global.

Les raisons sont :

* Deux composants ou plus auront besoin d'accéder à l'état `items`.
* L'état `name` n'est nécessaire que pour saisir les noms des éléments dans la liste `items`.

Voici la structure de notre application de liste de tâches avec les états positionnés selon leurs besoins et la logique d'ajout des noms d'éléments à la liste des éléments :

```javascript
import { useState } from "react";

export default function App() {

//État global
  const [items, setItems] = useState([]);

//fonction de gestion qui prend un élément comme paramètre
  function handleAddItems(item) {
  
  //fonction de mise à jour qui retourne un nouveau tableau avec les éléments de l'état actuel et un nouvel élément  
    setItems((items) => [...items, item]);
  }

  return (
    <div>
      <Header />
      <Nav handleAddItems={handleAddItems} /> //passage de handleAddItems en tant que props
      <ListArea items={items} /> //passage de items en tant que props
      <Footer items={items} />	//passage de items en tant que props
    </div>
  );
}
function Header() {
  return <h2>Liste de tâches</h2>;
}

function Nav({ handleAddItems }) {
  //Fonction d'état local
  const [name, setName] = useState("");
  
  //créer une fonction de gestion qui est déclenchée par le bouton Ajouter
  const handleAddButtonClick = () => {
    //création d'un objet newItem avec les propriétés name et id
    const newItem = { name, id: Date.now() };

    //passage de l'objet newItem dans la fonction de gestion en tant qu'argument
    handleAddItems(newItem);
    // Réinitialiser le champ de saisie après l'ajout de l'élément
    setName("");
  };
  return (
    <>
      <input
        type="text"
        value={name}
        onChange={(e) => setName(e.target.value)}
      />
      <button onClick={handleAddButtonClick}>Ajouter</button>
    </>
  );
}

//Composant ListArea recevant les éléments en tant que props de l'état global

function ListArea({ items }) {
  return (
    <>
      <ul>
      //mappage du tableau items pour obtenir chaque élément en tant qu'élément de liste
        {items.map((item) => (
          <li key={item.id}>{item.name}</li>
        ))}
      </ul>
    </>
  );
}

//Composant Footer recevant les éléments en tant que props de l'état global

function Footer({ items }) {
  return (
    <>
      {items.length !== 0 ? (
        <p>Vous avez {items.length} éléments dans votre panier</p>
      ) : (
        <p>Vous pouvez commencer à ajouter des éléments à votre liste</p>
      )}
    </>
  );
}

```

Les composants `Footer` et `ListArea` ont maintenant accès aux éléments passés via les props. 

L'acte de positionner un état dans le composant racine afin qu'il puisse être accessible globalement dans une application React est connu sous le nom de "Remonter l'état" - ce que nous avons fait avec l'état `items`.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/image-34.png)
_La liste de tâches après que des éléments ont été ajoutés à la liste_

Voici une représentation de l'ensemble du processus :

![Image](https://www.freecodecamp.org/news/content/images/2024/02/image-37.png)

## Conclusion

Dans cet article, nous avons exploré la gestion d'état dans React, quand vous en avez besoin et où placer l'état dans les composants de nos applications. 

Nous avons également décomposé comment "penser en React", pour faire interagir nos composants React entre eux et obtenir le résultat souhaité. 

React est une bibliothèque d'interface utilisateur intéressante, mais peut parfois être déroutante si vous ne connaissez pas les bases. Vous pouvez maintenant utiliser les connaissances acquises dans cet article pour coder vos projets.