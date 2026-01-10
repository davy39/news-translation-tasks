---
title: Comment intégrer le Data Grid de Material UI dans React en utilisant des données
  d'une API REST
subtitle: ''
author: deji adesoga
co_authors: []
series: null
date: '2022-01-06T16:30:56.000Z'
originalURL: https://freecodecamp.org/news/how-to-integrate-material-ui-data-grid-in-react-using-data-from-a-rest-api
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/datagrid.png
tags:
- name: data
  slug: data
- name: Datatables
  slug: datatables
- name: React
  slug: react
- name: REST API
  slug: rest-api
seo_title: Comment intégrer le Data Grid de Material UI dans React en utilisant des
  données d'une API REST
seo_desc: 'Material UI''s Data Grid is a powerful and flexible data table. It makes
  it easy for you to display data and perform out of the box functionalities such
  as editing, sorting, filtering, pagination and more.

  In this article, we''ll discuss why you should...'
---

Le Data Grid de Material UI est un tableau de données puissant et flexible. Il facilite l'affichage des données et permet des fonctionnalités prêtes à l'emploi telles que l'édition, le tri, le filtrage, la pagination et bien plus encore.

Dans cet article, nous discuterons des raisons pour lesquelles vous devriez utiliser le **Data Grid** dans **Material UI** dans votre projet. Ensuite, nous verrons comment installer et configurer le Data Grid, consommer et intégrer une API RESTful, et activer la pagination ainsi que le tri et le filtrage.

## Table des matières

* [Introduction au Data Grid](#heading-introduction-au-data-grid)
  
* [Pourquoi utiliser le Data Grid de Material UI](#heading-pourquoi-utiliser-le-data-grid-de-material-ui)
  
* [Installation et configuration de React et du Data Grid de Material UI](#heading-installation-et-configuration-de-react-et-du-data-grid-de-material-ui)
  
* [Intégration et consommation de l'API](#heading-integration-et-consommation-de-lapi)
  
* [Affichage des résultats de l'API dans le Data Grid de Material UI](#heading-comment-afficher-les-resultats-de-lapi-dans-le-data-grid-de-material-ui)
  
* [Conclusion](#heading-conclusion)
  

Regardez la version vidéo de cet article ci-dessous, ou sur ma [chaîne YouTube](https://www.youtube.com/watch?v=S_mgSHCWCmA&t=15s) :

%[https://www.youtube.com/watch?v=S_mgSHCWCmA&t=15s]

## Introduction au Data Grid

Selon la documentation de Material UI, le **Data Grid** est un

> "*tableau de données React rapide et extensible et une grille de données React. C'est un composant riche en fonctionnalités disponible en versions MIT ou Commerciales*".

En gros, le Data Grid dans Material UI vient avec certaines fonctionnalités comme l'édition, le tri, le filtrage, la mise à jour, la pagination, les exports et bien plus encore par défaut.

L'équipe a également des plans futurs pour implémenter des fonctionnalités supplémentaires comme l'export Excel, la sélection de plage, le regroupement, le pivot, l'agrégation.

Pour les besoins de ce tutoriel, nous allons implémenter certaines des fonctionnalités du Data Grid avec une API REST publique appelée **JSONPlaceholder**

## Pourquoi utiliser le Data Grid de Material UI

Il y a plusieurs raisons importantes pour lesquelles vous pourriez vouloir utiliser le Data Grid de Material UI :

* Accessibilité
  
* Interaction utilisateur
  
* Présentation des données
  

#### Accessibilité

Le Data Grid offre des fonctionnalités d'accessibilité telles que la mise en surbrillance des cellules. C'est-à-dire que chaque cellule est accessible à l'aide du clavier.

Il fournit également des fonctionnalités supplémentaires telles que la navigation au clavier en utilisant certaines touches du clavier pour changer le focus des cellules du tableau, ainsi que des propriétés de densité pour déterminer la hauteur des lignes et des colonnes dans le tableau.

#### Interaction utilisateur

En termes d'interaction, le Data Grid fournit une fonctionnalité intégrée telle que la sélection de lignes par défaut. Cela permet à l'utilisateur de sélectionner certaines lignes avec un clic de souris ou en utilisant certains raccourcis clavier.

Le Data Grid dans Material UI supporte la sélection de lignes uniques et multiples, la capacité de désactiver la sélection de certaines lignes ou de toutes les lignes, la sélection par case à cocher et bien plus encore.

#### Présentation des données

Le Data Grid fournit une fonctionnalité intégrée qui permet d'exporter les données au format CSV.

De plus, les données peuvent être manipulées en cliquant sur un en-tête de colonne. Cela déclenchera les fonctionnalités de tri et de filtrage.

Une autre fonctionnalité de base qui vient par défaut est le défilement, ce qui ne se produit pas dans un tableau normal par défaut.

## Installation et configuration de React et du Data Grid de Material UI

Pour créer un nouveau projet dans React, vous devez avoir [Node.js](https://nodejs.org/en/download/) installé. Cela nous donnera accès à npm dans notre terminal. Nous pouvons ensuite installer et utiliser Create React App en utilisant npm pour créer notre projet, en exécutant la commande suivante :

```javascript
npm i create-react-app
```

L'étape suivante consiste à créer un nouveau projet React à partir du terminal en exécutant la commande suivante :

```javascript
npx create-react-app data-grid 
cd data-grid 
npm start
```

Ci-dessus, nous avons créé un nouveau projet appelé `data-grid`. Ensuite, nous avons navigué dans le répertoire du projet nouvellement créé et démarré le projet avec *npm*.

Par défaut, notre projet s'exécutera sur localhost:3000 dans le navigateur.

Enfin, nous devons installer deux packages qui sont **Material UI** et le **Data Grid** en utilisant la commande suivante :

```javascript
npm install @mui/x-data-grid @mui/material
```

## Intégration et consommation de l'API

Pour intégrer notre API, nous devons créer un nouveau fichier et un nouveau dossier dans notre répertoire src qui est créé pour nous lorsque nous avons généré notre projet avec Create-React-App. Nous appellerons ce nouveau dossier **Table** et le fichier sera appelé **DataGrid.js**.

À la fin, notre structure de dossiers devrait ressembler à ceci :

```javascript
> src 
    > Table 
        > DataGrid.js 
.gitignore 
package-lock.json 
package.json 
README
```

Dans le fichier DataGrid.js, nous utiliserons un composant fonctionnel. Dans ce composant fonctionnel, nous implémenterons certaines des fonctionnalités par défaut suivantes dans React :

* le hook useState
  
* le hook useEffect
  
* l'API Fetch
  

#### Le hook useState

Le hook **useState** dans React est une fonction intégrée qui nous aide à suivre l'état dans un composant fonctionnel.

#### Le hook useEffect

Le hook **useEffect** nous permet de gérer les effets secondaires dans notre composant fonctionnel. Certains de ces effets secondaires pourraient inclure des choses comme la mise à jour du DOM, la récupération de données à partir d'une API RESTful, les événements de temporisation, et ainsi de suite.

#### L'API Fetch

L'**API Fetch** en JavaScript permet aux navigateurs web de faire des requêtes HTTP aux serveurs web. La requête peut être de n'importe quelle API qui envoie et reçoit des données au format JSON ou XML.

Maintenant que nous avons exploré le concept des hooks et de l'API Fetch, créons un composant fonctionnel de base dans notre fichier DataGrid.js :

```jsx
import React from 'react'

const DataGrid = () => {
  return (
    <div>
      
    </div>
  )
}

export default DataGrid
```

L'étape suivante consiste à consommer l'API REST de [JSON placeholder](https://jsonplaceholder.typicode.com/posts).

Pour ce faire, la première chose à faire est d'importer les hooks useState et useEffect :

```jsx
import React, { useState, useEffect } from 'react'
```

Ensuite, nous créons une variable en utilisant le hook useState :

```jsx
const [tableData, setTableData] = useState([])
```

Le **tableData** ci-dessus sert de getter, tandis que le **setTableData** sert de setter.

Enfin, pour accéder à nos données, nous utiliserons le hook useEffect et l'API Fetch :

```jsx
useEffect(() => {
  fetch("https://jsonplaceholder.typicode.com/posts")
    .then((data) => data.json())
    .then((data) => setTableData(data))
}, [])
 console.log(tableData)
```

Ci-dessus, nous pouvons voir que dans le hook useEffect, nous avons fait trois choses :

* Tout d'abord, dans le hook useEffect, nous avons utilisé Fetch pour consommer l'API REST de JSON placeholder
  
* Ensuite, nous avons converti la réponse que nous avons obtenue au format JSON
  
* Enfin, nous avons passé les données de notre réponse au setter que nous avons créé précédemment appelé setTableData
  

Pour être sûr d'avoir obtenu la bonne réponse, nous avons enregistré les données que nous avons obtenues dans la console. Pour voir les résultats dans la console, nous devons importer notre **DataGrid.js** dans notre fichier **App.js** :

```jsx
import './App.css';
import DataGrid from './Table/DataGrid';

function App() {
  return (
    <div className="App">
      <DataGrid />
    </div>
  );
}

export default App;
```

Ensuite, nous obtenons le résultat ci-dessous, qui consiste en une liste de 100 objets dans un tableau :

![Image](https://www.freecodecamp.org/news/content/images/2022/01/console.png align="left")

*Données JSON dans la console*

## Comment afficher les résultats de l'API dans le Data Grid de Material UI

Pour afficher les résultats de notre API dans le Data Grid de Material UI, nous devons importer le package Data Grid dans notre fichier DataGrid.js :

```jsx
import { DataGrid } from '@mui/x-data-grid'
```

Nous configurons ensuite la section d'en-tête de notre tableau Data Grid :

```jsx
const columns = [
  { field: 'id', headerName: 'ID' },
  { field: 'title', headerName: 'Titre', width: 300 },
  { field: 'body', headerName: 'Corps', width: 600 }
]
```

Comme vous pouvez le voir ci-dessus, c'est un tableau d'objets et il contient un **id**, un **titre** et un **corps**, ce qui est conforme aux résultats que nous avons obtenus de notre API REST.

Enfin, nous intégrons le composant DataGrid dans notre instruction return :

```jsx
<div style={{ height: 700, width: '100%' }}>
     <DataGrid
       rows={tableData}
       columns={columns}
       pageSize={12}
     />
   </div>
```

Ci-dessus, nous avons trois propriétés dans le composant DataGrid :

* La première est la propriété **rows**. Ce que nous avons fait avec la propriété row, c'est passer les résultats que nous avons obtenus de notre API REST, qui sont contenus dans le getter appelé tableData
  
* La deuxième propriété s'appelle **columns**. Il s'agit du tableau d'objets qui contient l'en-tête de notre DataGrid, y compris l'id, le titre et le corps.
  
* La dernière propriété est pageSize. Cela nous aide à définir une limite à la quantité de données qui peuvent être affichées à la fois. Comme vous pouvez le voir, nous l'avons définie à 12 - le reste du résultat est ensuite paginé par défaut.
  

À la fin, notre fichier DataGrid.js devrait ressembler à ceci :

```jsx
import React, { useState, useEffect } from 'react'
import { DataGrid } from '@mui/x-data-grid'

const columns = [
  { field: 'id', headerName: 'ID' },
  { field: 'title', headerName: 'Titre', width: 300 },
  { field: 'body', headerName: 'Corps', width: 600 }
]

const DataGrid = () => {

  const [tableData, setTableData] = useState([])

  useEffect(() => {
    fetch("https://jsonplaceholder.typicode.com/posts")
      .then((data) => data.json())
      .then((data) => setTableData(data))

  }, [])

  console.log(tableData)

  return (
    <div style={{ height: 700, width: '100%' }}>
      <DataGrid
        rows={tableData}
        columns={columns}
        pageSize={12}
      />
    </div>
  )
}

export default DataGrid
```

Les résultats dans le navigateur devraient également ressembler à l'image que nous avons ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2022/01/grid.png align="left")

*Résultat du tableau Data Grid*

Une chose géniale à noter dans le résultat de notre image ci-dessus est que nous avons une fonctionnalité de tri et de filtrage prête à l'emploi lorsque nous cliquons sur la section d'en-tête (*id, titre, corps*) de notre tableau de données.

## Conclusion

Dans cet article, nous avons appris à connaître le DataGrid dans Material UI, les hooks React, la consommation d'API REST et bien plus encore.

De plus, le lien vers le code de cet article peut être trouvé sur [GitHub](https://github.com/desoga10/data-grid).

Si vous avez apprécié cet article, montrez votre soutien en vous abonnant à ma [chaîne YouTube](https://www.youtube.com/TheCodeAngle) où je crée des tutoriels géniaux sur les technologies de développement web comme JavaScript, React, Angular, Node.js, et bien plus encore.

Si vous avez des commentaires ou des questions sur cet article ou d'autres questions liées à la programmation, vous pouvez me trouver sur Twitter [@thecodeangle](https://twitter.com/thecodeangle).