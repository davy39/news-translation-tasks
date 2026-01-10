---
title: Comment créer des tableaux avec la bibliothèque React-Data-Table-Component
  dans React & TypeScript
subtitle: ''
author: Losalini Rokocakau
co_authors: []
series: null
date: '2024-03-27T15:40:38.000Z'
originalURL: https://freecodecamp.org/news/create-tables-using-the-react-datatable-component-library
coverImage: https://www.freecodecamp.org/news/content/images/2024/03/cover-image-21.png
tags:
- name: Front-end Development
  slug: front-end-development
- name: React
  slug: react
- name: TypeScript
  slug: typescript
- name: user experience
  slug: user-experience
- name: User Interface
  slug: user-interface
seo_title: Comment créer des tableaux avec la bibliothèque React-Data-Table-Component
  dans React & TypeScript
seo_desc: "In this tutorial, I'll teach you how to use the react-data-table-component\
  \ library in your React projects. You'll learn how to render a table that has features\
  \ such as pagination, searching/filtering, and sorting. \nI'll walk you through\
  \ each step, fr..."
---

Dans ce tutoriel, je vais vous apprendre à utiliser la bibliothèque _react-data-table-component_ dans vos projets React. Vous apprendrez à rendre un tableau avec des fonctionnalités telles que la pagination, la recherche/le filtrage et le tri. 

Je vais vous guider à travers chaque étape, depuis la configuration d'un projet React et TypeScript avec Vite jusqu'à l'utilisation de la bibliothèque _react-data-table-component_ pour rendre un tableau.

Pour suivre ce tutoriel, voici quelques prérequis :

1. Une compréhension de base de React et TypeScript
2. Des connaissances de base en Bootstrap, que nous utiliserons pour le style
3. Pour les utilisateurs de Windows OS, savoir utiliser le terminal PowerShell (car vous aurez besoin d'un terminal interactif pour créer le projet avec Vite)
4. Node v20.11.1 installé
5. npm v10.2.4 installé
6. Un éditeur de code tel que Visual Studio Code (VS Code) ou Atom

Commençons à créer le projet !

### Ce que nous allons construire

À la fin de ce tutoriel, vous aurez construit un tableau qui affiche l'ID, le nom, la taille et la couleur des yeux d'une personne.

Le tableau aura également une barre de recherche où les utilisateurs pourront rechercher une personne en fonction de la valeur de l'une des quatre propriétés mentionnées ci-dessus.

Chaque ligne du tableau sera sélectionnable et chaque colonne sera triable lorsque l'en-tête de la colonne est cliqué par un utilisateur.

## 1. Créer un projet React et TypeScript

Dans la ligne de commande, créez le projet avec la commande suivante :

```
npm create vite@latest
```

Nommez le projet `react-data-table-tutorial`.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/fig-1-0-1.png)
_**Figure 1.0** Création du projet React & TypeScript avec Vite sur la ligne de commande PowerShell. Nommer le projet react-data-table-tutorial._

Naviguez jusqu'à React avec les touches haut et bas pour sélectionner React. Choisissez React comme bibliothèque que vous allez utiliser.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/fig-1-1-1.png)
_**Figure 1.1** Sélection de React comme notre framework en naviguant jusqu'à lui dans la liste avec les touches fléchées haut et bas du clavier._

De manière similaire à l'étape ci-dessus, naviguez jusqu'à TypeScript et choisissez-le comme langage à utiliser.

L'étape suivante consiste à changer de répertoire pour entrer dans le dossier du projet. Une fois que vous avez fait cela, ouvrez le projet dans votre éditeur de code comme le montre la Figure 1.2 ci-dessous. J'utiliserai l'éditeur VS Code dans ce tutoriel.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/fig-1-2-2.png)
_**Figure 1.2** Changement du dossier dans le répertoire react-data-table-tutorial et ouverture du contenu du dossier dans un éditeur de code._

## 2. Supprimer le code par défaut défini par React

Cette étape consiste simplement à supprimer tout code et style par défaut dans les fichiers trouvés dans le dossier _src_. 

Tout d'abord, supprimez tous les styles par défaut dans le fichier _App.css_ et remplacez-les par les styles ci-dessous.

```css
body {
    background-color: white;
    padding: 160px 500px;
}
```

Ensuite, supprimez les éléments suivants du fichier _App.tsx_ :

* les instructions importées du hook `useState`, `reactLogo`, et `viteLogo`_._
* Le tableau déstructuré et le hook `useState` pour la variable count et la fonction `setCount`.
* Le JSX retourné enveloppé dans le fragment du composant `App`.

Le composant `App` devrait ressembler au bloc de code ci-dessous après toutes ces modifications :

```javascript
import './App.css';

function App(){
	return <></>;
}

export default App;
```

## 3. Installer les bibliothèques dont nous aurons besoin

Dans le projet, vous devrez installer quelques bibliothèques :

1. _styled-components_ v3.23+
2. _react-data-table-component_ v16.8.0+
3. _Bootstrap_ v5.3.3

Vous devrez installer la bibliothèque _styled-components_ pour l'utiliser avec la bibliothèque _react-data-table-component_.

Dans la ligne de commande, installez toutes ces bibliothèques en utilisant les commandes ci-dessous :

```
npm install styled-components

```

```
npm install react-data-table-components

```

```
npm install bootstrap@5.3.3

```

![Image](https://www.freecodecamp.org/news/content/images/2024/03/fig-3-0.png)
_**Figure 3.0** Installation des bibliothèques sur le terminal intégré de Visual Studio Code._

Les bibliothèques installées sont listées sous les dépendances dans le fichier _package.json_.

```json
{
   // reste du code dans le fichier
    "dependencies": {
        "boostrap": "^5.3.3",
        "react": "^18.2.0",
        "react-data-table-component": "^7.6.2",
        "react-dom": "^18.2.0",
        "styled-components": "^6.1.8",
    }
    // reste du code dans le fichier
}
```

## 4. Importer Bootstrap dans le composant App

Dans le fichier _App.tsx_, importez la bibliothèque Bootstrap en haut du fichier.

Cela nous permettra d'utiliser les styles Bootstrap dans tout le projet.

```javascript
import "./App.css";
import "bootstrap/dist/js/bootstrap.bundle.min.js";

function App(){
   return <></>;
}

export default App;
```

## 5. Créer un composant Table

Dans le dossier _src_, créez un sous-dossier et nommez-le _components_. Par convention, cela servira à contenir tous les composants du projet.

Dans le dossier _components_, créez un fichier appelé _Table.tsx_. Cela servira pour notre composant `Table`.

Créez un composant fonctionnel appelé `Table`.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/fig-4-0.png)
_**Figure 5.0** Créer le composant Table dans le sous-dossier components dans le dossier src._

## 6. Importer la bibliothèque react-data-table-component pour commencer à l'utiliser

Importez la bibliothèque _react-data-table-component_ dans le composant `Table`.

```javascript
import DataTable from "react-data-table-component";

function Table(){
	return <></>;
}

export default Table;
```

## 7. Créer le tableau dans le composant Table

Créez un conteneur `<div>` dans le fragment et ajoutez le style Bootstrap `container` et `my-5` pour placer le tableau au centre de la page.

Ajoutez le composant `DataTable` comme enfant du conteneur `<div>`.

```javascript
import DataTable from 'react-data-table-component';

function Table(){
	return (
    	<>
        	<div className="container my-5">
            	<DataTable />
            </div>
        </>
    );
}
```

Passez les colonnes et les lignes du tableau comme props au composant `DataTable`.

Les en-têtes de colonne du tableau sont des objets qui seront stockés dans un tableau. Les lignes du tableau seront également stockées de manière similaire. Le tableau d'objets pour les deux aura ces structures :

```javascript
const columns = [
    {
        name: "ID",
        selector: row => row.id
    },
    {
        name: "Full Name",
        selector: row => row.fullName
    },
    {
        name: "Height",
        selector: row => row.height
    },
    {
        name: "Weight",
        selector: row => row.weight
    },
];

```

```javascript
const rows = [
    {
    	id: 1,
        fullName: "John Doe",
        height: "1.75m",
        weight: "89kg",
    },
    {
    	id: 2,
        fullName: "Jane Doe",
        height: "1.64m",
        weight: "55kg",
    },
    {
    	id: 3,
        fullName: "Sheera Maine",
        height: "1.69m",
        weight: "74kg",
    },
];

```

Ces constantes sont ensuite passées dans le composant `DataTable` comme suit :

```jsx
<DataTable columns={columns} data={rows} />
```

Créez une constante `columns` qui est un tableau d'objets avec quatre en-têtes de colonne pour `personID`, `fullName`, `height`, et `eyeColor`.

Créez une constante `rows` qui est un tableau d'objets avec 15 objets équivalents aux données de 15 personnes.

Passez les deux constantes dans leurs props respectives dans le composant `DataTable` comme le montre le bloc de code suivant.

```javascript
function Table(){
	const columns = [
    	{
            name: "ID",
            selector: (row) => row.personID,
        },
        {
            name: "Full Name",
            selector: (row) => row.fullName,
        },
        {
            name: "Height",
            selector: (row) => row.height,
        },
        {
            name: "eyeColor",
            selector: (row) => row.eyeColor,
        },
    ];
    
    const rows = [
    	{
           personID: 1,
           fullName: "Kate Shein",
           height: "1.79m",
           eyeColor: "blue",
        },
        //....objets restants pour la 2ème à la 14ème personne
        {
           personID: 15,
           fullName: "Isabella Thompson",
           height: "1.79m",
           eyeColor: "blue",
        },
    ];
}
```

Vous ajouterez également la prop `fixedHeader` au composant `DataTable` pour garder l'en-tête de colonne fixe lorsque l'utilisateur fait défiler le tableau qui contient plus de 10 enregistrements.

Donnez un titre au tableau en passant la prop `title` au composant et sa valeur est ce que vous souhaitez appeler votre tableau.

```javascript
<div class="container">
    <DataTable 
        columns={columns} 
        data={rows} 
        fixedHeader
        title="Tutoriel React-Data-Table-Component."
     />
</div>

```

De retour dans le composant `App`, importez le composant `Table` et placez-le dans le fragment.

```javascript
import "./App.css";
import "bootstrap/dist/js/bootstrap.bundle.min.js";
import Table from "./components/Table";

function App(){
    return (
    	<>
           <Table />
        </>
    );
}

export default App;
```

## 8. Ajouter la pagination et le tri, et rendre chaque ligne sélectionnable

### Pagination et `selectableRows`

Ajoutez les props `pagination` et `selectableRows` au composant `DataTable`.

Par défaut, la première page contient les 10 premiers enregistrements. Si des appels API doivent être effectués côté serveur pour une pagination personnalisée, vous pouvez utiliser la propriété `paginationServer` ainsi que les propriétés `paginationTotalRows`, `onChangeRowsPerPage` et `onChangePage` qui fonctionnent en conjonction avec quelques autres éléments.

Mais pour l'instant, restons avec la propriété `pagination`.

```jsx
//...reste du code dans le composant fonctionnel
<div className="container d-flex justify-content-center my-5">
   <DataTable
    	columns={columns}
        data={rows}
        fixedHeader
        title="Tutoriel React-Data-Table-Component"
        pagination
        selectableRows
    />
</div>
//...reste du code dans le composant fonctionnel
```

### Tri

Dans le composant `DataTable`, ajoutez la propriété `sortable` à chaque objet dans la constante `columns`. Donnez-lui une valeur booléenne `true` pour que le tri soit appliqué à chaque colonne lorsque l'utilisateur clique sur les en-têtes de colonne.

```typescript
//...reste du code dans le composant fonctionnel
const columns = [
    {
        name: 'ID',
        selector: (row) => row.personID,
        sortable: true,
    },
    {
        name: 'Full Name',
        selector: (row) => row.fullName,
        sortable: true,
    },
    {
        name: 'Height',
        selector: (row) => row.height,
        sortable: true,
    },
    {
        name: 'Eye Color',
        selector: (row) => row.eyeColor,
        sortable: true,
    },
];
//...reste du code dans le composant fonctionnel

```

## 9. Ajouter la recherche et le filtrage

Ajoutez un conteneur `<div>` au-dessus du composant `DataTable` dans le JSX retourné. Ajoutez également la classe Bootstrap `input-group` au `<div>`.

L'élément enfant de ce nouveau conteneur sera l'`<input />` de type `search` et nous utiliserons les styles de Bootstrap pour celui-ci. Utilisez le code ci-dessous :

```jsx
<input
    type="search"
    className="form-control-sm border ps-3"
    placeholder="Rechercher"
/>
```

Une étape facultative consiste à ajouter une icône de recherche ou à utiliser le [style par défaut de Bootstrap](https://getbootstrap.com/docs/5.3/forms/input-group/) pour une barre de recherche. Cependant, nous allons le laisser de côté pour l'instant afin de nous concentrer uniquement sur la fonctionnalité de recherche.

Maintenant, importons le hook `useState` dans le fichier _Table.tsx_.

Utilisez le hook et passez la constante `rows` comme valeur par défaut de notre variable d'état. Dans le tableau déstructuré se trouvera notre variable d'état appelée `data` et la fonction de définition appelée `setData`.

```typescript
const [data, setData] = useState(rows);


```

Créez une fonction appelée `handleSearch` qui sera appelée lorsque l'écouteur d'événement `onChange` est utilisé sur la barre de recherche. 

Passez l'objet événement, `e`, comme argument. En utilisant l'annotation de type, définissez le type de l'objet événement sur `React.ChangeEvent<HTMLInputElement>`.

```typescript
const handleSearch = (e: React.ChangeEvent<HTMLInputElement>) => {
   // le reste du code sera défini ici
};
```

Déclarez 5 variables de type Boolean comme indiqué ci-dessous :

```typescript
const handleSearch = (e: React.ChangeEvent<HTMLInputElement>) => {
   let searchValue: Boolean;
   let personIDValue: Boolean;
   let fullNameValue: Boolean;
   let heightValue: Boolean;
   let eyeColorValue: Boolean;
};
```

Déclarez une nouvelle constante locale appelée `newRows`. Dans cette constante, filtrez et retournez les lignes/données dans la constante _rows_ où la valeur de l'entrée de recherche est la même que la valeur de la propriété `fullName` ou `height` ou `eyeColor` des lignes.

```typescript
const newRows = rows.filter((row) => {
      personIDValue = row.personID
        .toString()
        .toLowerCase()
        .includes(e.target.value.toLowerCase());
      fullNameValue = row.fullName
        .toLowerCase()
        .includes(e.target.value.toLowerCase());
      heightValue = row.height
        .toLowerCase()
        .includes(e.target.value.toLowerCase());
      eyeColorValue = row.eyeColor
        .toLowerCase()
        .includes(e.target.value.toLowerCase());

      if (personIDValue) {
        searchValue = personIDValue;
      } else if (fullNameValue) {
        searchValue = fullNameValue;
      } else if (heightValue) {
        searchValue = heightValue;
      } else {
        searchValue = eyeColorValue;
      }

      return searchValue;
});
```

Passez `newRows` dans la fonction de définition, `setData`.

```typescript
setData(newRows);
```

```typescript
// définition de la constante columns

// définition de la constante rows

const [data, setData] = useState(rows);

// Gérer la recherche
const handleSearch = (e: React.ChangeEvent<HTMLInputElement>) => {
    let searchValue: Boolean;
    let personIDValue: Boolean;
    let fullNameValue: Boolean;
    let heightValue: Boolean;
    let eyeColorValue: Boolean;
   
    const newRows = rows.filter((row) => {
      personIDValue = row.personID
        .toString()
        .toLowerCase()
        .includes(e.target.value.toLowerCase());
      fullNameValue = row.fullName
        .toLowerCase()
        .includes(e.target.value.toLowerCase());
      heightValue = row.height
        .toLowerCase()
        .includes(e.target.value.toLowerCase());
      eyeColorValue = row.eyeColor
        .toLowerCase()
        .includes(e.target.value.toLowerCase());

      if (personIDValue) {
        searchValue = personIDValue;
      } else if (fullNameValue) {
        searchValue = fullNameValue;
      } else if (heightValue) {
        searchValue = heightValue;
      } else {
        searchValue = eyeColorValue;
      }

      return searchValue;
    });
	
    setData(newRows);
};

```

L'étape suivante consiste à passer (sans appeler la fonction) la fonction `handleSearch` à l'écouteur d'événement `onChange`. 

```jsx
<input
   type="search"
   className="form-control-sm border ps-3"
   placeholder="Rechercher"
   onChange={handleSearch}
/>
```

La valeur de la propriété data dans le composant `DataTable` sera maintenant la variable d'état, `data` au lieu de `rows` qui était initialement passée.

```jsx
<DataTable
    columns={columns}
    data={data}
    fixedHeader
    title="Tutoriel React-Data-Table-Component."
    pagination
    selectableRows
/>
```

## 10. Voir le tableau

Exécutez le projet dans la ligne de commande et visualisez le tableau dans un navigateur :

```command line
npm run dev
```

Le tableau devrait ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2024/03/final-result-table.png)
_**Figure 11.0** Aperçu du tableau résultant créé._

Vous pouvez lire la [documentation](https://react-data-table-component.netlify.app/?path=/docs/getting-started-intro--docs) pour _react-data-table-component_ car elle couvre plus en détail l'utilisation de la bibliothèque, ce qui dépasse le cadre de cet article. 

Ne vous inquiétez pas s'il y a une différence entre votre tableau et le résultat attendu. Le code source dans [ce dépôt](https://github.com/chelmerrox/react-data-table-tutorial) vous guidera.

Bon codage et que votre code s'exécute sans accroc !