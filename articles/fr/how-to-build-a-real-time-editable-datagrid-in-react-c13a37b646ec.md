---
title: Comment construire une grille de données éditable en temps réel dans React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-28T16:27:13.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-real-time-editable-datagrid-in-react-c13a37b646ec
coverImage: https://cdn-media-1.freecodecamp.org/images/1*qguZN_QzVYcECU_UpG799A.gif
tags:
- name: data
  slug: data
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: Web Development
  slug: web-development
seo_title: Comment construire une grille de données éditable en temps réel dans React
seo_desc: 'By Peter Mbanugo

  A datagrid enables you to display and edit data. This is a vital feature in most
  data-driven applications.

  You may have implemented this in one of your React apps in the past. Maybe you used
  libraries like react-bootstrap-table, reac...'
---

Par Peter Mbanugo

Une grille de données vous permet d'afficher et de modifier des données. Il s'agit d'une fonctionnalité vitale dans la plupart des applications basées sur les données.

Vous avez peut-être déjà implémenté cela dans l'une de vos applications React par le passé. Peut-être avez-vous utilisé des bibliothèques comme [react-bootstrap-table](https://react-bootstrap-table.github.io/react-bootstrap-table2/), [react-grid](https://github.com/eddyson-de/react-grid), ou [react-table](https://react-table.js.org/). Avec celles-ci, vous pouvez ajouter une grille de données à votre application React. Mais que faire si vous souhaitez que les modifications soient effectuées en temps réel et que les mises à jour soient synchronisées sur tous les appareils connectés et leurs navigateurs ?

Dans cet article, je vais vous montrer comment construire une grille de données en temps réel dans React en utilisant [react-table](https://react-table.js.org/) et [Hamoni Sync](https://www.hamoni.tech/).

react-table est une bibliothèque légère et rapide pour rendre des tableaux dans React, et elle prend en charge la pagination et bien d'autres fonctionnalités.

Hamoni Sync est un service de synchronisation d'état en temps réel qui vous permet de synchroniser l'état de votre application en temps réel. Je vais vous montrer comment construire une grille de données avec les prénoms et noms de famille des personnes.

Si vous souhaitez suivre, vous devriez avoir quelques connaissances de React et avoir les outils suivants installés :

1. [NodeJS](https://dev.to/nodejs.org)
2. [npm](http://npmjs.com/) & [npx](https://github.com/zkat/npx). Si vous avez installé npm version 5.2.0 ou supérieure, il installe npx avec npm.
3. [create-react-app](https://github.com/facebook/create-react-app)

### Créer l'application React

Tout d'abord, nous allons créer un nouveau projet React en utilisant create-react-app.

Ouvrez la ligne de commande et exécutez `npx create-react-app realtime-react-datatable`. Cela initialisera une application React pour nous en créant un nouveau répertoire `realtime-react-datatable` avec les fichiers nécessaires pour construire une application React.

Avec l'application React créée, nous devons installer react-table et Hamoni Sync. Toujours sur la ligne de commande, exécutez `cd realtime-react-datatable` pour passer au répertoire de l'application. Exécutez `npm i react-table hamoni-sync` dans la ligne de commande pour installer les deux packages.

### Rendre la grille de données

Pour rendre la grille de données, nous allons utiliser le composant react-table. Ouvrez le fichier `src/App.js` et mettez-le à jour avec le code ci-dessous :

```
import React, { Component } from "react";import logo from "./logo.svg";import "./App.css";// Import React Tableimport ReactTable from "react-table";import "react-table/react-table.css";// Import Hamoni Syncimport Hamoni from "hamoni-sync";
```

```
class App extends Component {  constructor() {    super();    this.state = {      data: [],      firstName: "",      lastName: ""    };  }
```

```
  handleChange = event => {    if (event.target.name === "firstName")      this.setState({ firstName: event.target.value });    if (event.target.name === "lastName")      this.setState({ lastName: event.target.value });  };
```

```
  handleSubmit = event => {    event.preventDefault();  };
```

```
  renderEditable = cellInfo => {    return (      <div        style={{ backgroundColor: "#fafafa" }}        contentEditable        suppressContentEditableWarning        onBlur={e => {          const data = [...this.state.data];          data[cellInfo.index][cellInfo.column.id] = e.target.innerHTML;          this.setState({ data });        }}        dangerouslySetInnerHTML={{          __html: this.state.data[cellInfo.index][cellInfo.column.id]        }}      />    );  };
```

```
  render() {    const { data } = this.state;
```

```
    return (      <div className="App">        <header className="App-header">          <img src={logo} className="App-logo" alt="logo" />          <h1 className="App-title">Bienvenue dans React</h1>        </header>        <p className="App-intro">          <form onSubmit={this.handleSubmit}>            <h3>Ajouter un nouvel enregistrement</h3>            <label>              Prénom :              <input                type="text"                name="firstName"                value={this.state.firstName}                onChange={this.handleChange}              />            </label>{" "}            <label>              Nom :              <input                type="text"                name="lastName"                value={this.state.lastName}                onChange={this.handleChange}              />            </label> 
```

```
            <input type="submit" value="Ajouter" />          </form>        </p>        <div>          <ReactTable            data={data}            columns={[              {                Header: "Prénom",                accessor: "firstName",                Cell: this.renderEditable              },              {                Header: "Nom",                accessor: "lastName",                Cell: this.renderEditable              },              {                Header: "Nom complet",                id: "full",                accessor: d => (                  <div                    dangerouslySetInnerHTML={{                      __html: d.firstName + " " + d.lastName                    }}                  />                )              }            ]}            defaultPageSize={10}            className="-striped -highlight"          />        </div>      </div>    );  }}
```

```
export default App;
```

Le code ci-dessus rend un formulaire et un composant react-table éditable. `<ReactTable` /> rend un composant `avec` des props `data, columns`, et `defaultPageSize`. La prop `data` contient les données à afficher, et la prop `columns` pour la définition des colonnes. La propriété `accessor` dans les props `columns` indique la propriété qui contient la valeur à afficher pour cette colonne. La propriété `Cell: this.renderEditable` dans les props `columns` indique à react-table que la colonne est éditable. Les autres fonctions (`handleSubmit` & `handleChange`) permettent d'obtenir de nouvelles entrées de données à partir du formulaire sur la page.

### Ajouter Hamoni Sync

Les données pour la grille de données seront récupérées et mises à jour en temps réel en utilisant Hamoni Sync. Nous avons déjà importé la bibliothèque Hamoni à la ligne 18 dans `App.js`;

```
import Hamoni from "hamoni-sync";
```

Nous devons l'initialiser et nous connecter au serveur Hamoni. Pour cela, nous avons besoin d'un compte et d'un identifiant d'application. Suivez ces étapes pour créer une application dans Hamoni.

1. Inscrivez-vous et connectez-vous au tableau de bord Hamoni [dashboard](https://dashboard.hamoni.tech/)
2. Entrez le nom de votre application préféré dans le champ de texte et cliquez sur le bouton créer. Cela devrait créer l'application et l'afficher dans la section de la liste des applications.
3. Cliquez sur le bouton « Afficher l'ID du compte » pour voir votre identifiant de compte.

![Image](https://cdn-media-1.freecodecamp.org/images/JcOI2Oer-YfeEh3ITndyiaF98c1GIRrUQoeN)

Ajoutez le code suivant à `App.js` pour initialiser et vous connecter au serveur Hamoni Sync.

```
componentDidMount() {    let hamoni = new Hamoni("ACCOUNT_ID", "APP_ID");
```

```
    hamoni      .connect()      .then(() =>; {
```

```
      })      .catch(console.log);  }
```

Le code ci-dessus connectera l'appareil client ou le navigateur au serveur Hamoni Sync. Copiez votre identifiant de compte et d'application depuis le tableau de bord et remplacez-les par les placeholders de chaîne respectivement.

Ajoutez ce qui suit à la fonction dans le bloc `then()`, à exécuter lorsqu'il se connecte avec succès au serveur :

```
hamoni    .get("datagrid")    .then(listPrimitive => {      this.listPrimitive = listPrimitive;
```

```
      this.setState({        data: [...listPrimitive.getAll()]      });
```

```
      listPrimitive.onItemAdded(item => {        this.setState({ data: [...this.state.data, item.value] });      });
```

```
      listPrimitive.onItemUpdated(item => {        let data = [        ...this.state.data.slice(0, item.index),        item.value,        ...this.state.data.slice(item.index + 1)        ];
```

```
        this.setState({ data: data });      });
```

```
      listPrimitive.onSync(data => {        this.setState({ data: data });      });    })    .catch(console.log);
```

Le code ci-dessus appelle `hamoni.get("datagrid")` pour obtenir les données, avec `datagrid` comme nom de l'état de l'application sur Hamoni Sync. Hamoni Sync vous permet de stocker 3 types d'états appelés primitives de synchronisation. Ils sont :

1. **Value Primitive** : Ce type d'état contient des informations simples représentées avec des types de données comme chaîne, booléen ou nombres. Il est idéal pour des cas tels que le compteur de messages non lus, les bascules, etc.
2. **Object Primitive** : L'état d'objet représente des états qui peuvent être modélisés comme un objet JavaScript. Un exemple d'utilisation pourrait être le stockage du score d'un jeu.
3. **List Primitive** : Cela contient une liste d'objets d'état. Un objet d'état est un objet JavaScript. Vous pouvez mettre à jour un élément en fonction de son index dans la liste.

Si l'état est disponible, il résout et retourne une promesse avec l'objet primitif d'état. Cet objet nous donne accès à des méthodes pour mettre à jour l'état et obtenir des mises à jour d'état en temps réel.

À la ligne 36, nous avons utilisé la méthode `getAll()` pour obtenir des données et définir l'état pour le composant React. De plus, les méthodes `onItemAdded()` et `onItemUpdated()` sont utilisées pour obtenir des mises à jour lorsqu'un élément est ajouté ou mis à jour. La méthode `onSync()` est utile dans un scénario où un appareil ou un navigateur perd la connexion, et lorsqu'il se reconnecte, il essaie d'obtenir le dernier état du serveur et de mettre à jour l'état local s'il y en a un.

### Ajouter et mettre à jour des éléments

Dans la section précédente, nous sommes en mesure d'obtenir les données de la grille de données et de mettre à jour l'état lorsqu'un élément est ajouté ou mis à jour. Ajoutons du code pour ajouter de nouveaux éléments et mettre à jour un élément lorsqu'une colonne a été modifiée. Ajoutez le code suivant à la méthode `handleSubmit` :

```
handleSubmit = event => {    this.listPrimitive.push({        firstName: this.state.firstName,        lastName: this.state.lastName    });    this.setState({ firstName: "", lastName: "" });    event.preventDefault();};
```

Ce code obtient le prénom et le nom de famille à partir du formulaire et l'ajoute à la primitive d'état de liste sur Hamoni Sync en appelant la méthode `push()`. Cela déclenchera la méthode `onItemAdded()`.

Afin de mettre à jour les éléments lorsqu'ils sont modifiés dans la grille de données, nous allons mettre à jour la fonction passée à la prop `onBlur` à la ligne 84 comme suit :

```
onBlur={e => {    let row = this.state.data[cellInfo.index];    row[cellInfo.column.id] = e.target.innerHTML;    this.listPrimitive.update(cellInfo.index, row);}}
```

Ce code met à jour l'élément à l'index récupéré depuis l'objet `cellInfo`. Pour mettre à jour une primitive d'état de liste dans Hamoni Sync, vous appelez la méthode `update()` avec l'index de l'élément et la valeur à mettre à jour. La méthode `renderEditable` devrait maintenant ressembler à ceci après le dernier changement :

```
renderEditable = cellInfo => {    return (      <div        style={{ backgroundColor: "#fafafa" }}        contentEditable        suppressContentEditableWarning        onBlur={e => {          let row = this.state.data[cellInfo.index];          row[cellInfo.column.id] = e.target.innerHTML;          this.listPrimitive.update(cellInfo.index, row);        }}        dangerouslySetInnerHTML={{          __html: this.state.data[cellInfo.index][cellInfo.column.id]        }}      />    );  };
```

À ce stade, nous avons presque tout ce dont nous avons besoin pour exécuter l'application, à l'exception des données initiales qui seront rendues sur la grille de données.

Nous devons créer l'état et lui donner des données sur Hamoni Sync. Ajoutez un nouveau fichier **seed.js** à la racine de votre répertoire de travail et ajoutez-y le code suivant :

```
const Hamoni = require("hamoni-sync");
```

```
let hamoni = new Hamoni("AccountID", "APP_ID");
```

```
hamoni  .connect()  .then(response => {    hamoni      .createList("datagrid", [        { firstName: "James", lastName: "Darwin" },        { firstName: "Jimmy", lastName: "August" }      ])      .then(() => console.log("create success"))      .catch(console.log);  })  .catch(console.log);
```

Cela créera un état de primitive de liste sur Hamoni Sync, avec un nom de `datagrid`. Remplacez les chaînes `AccountID` et `APP_ID` par votre identifiant de compte et d'application. Ouvrez la ligne de commande et exécutez `node seed.js`. Cela devrait réussir et afficher le message `create success`.

Maintenant, nous pouvons démarrer l'application React et voir notre application en action ! Exécutez la commande `npm start` dans la ligne de commande et elle ouvrira l'application dans votre navigateur par défaut.

![Image](https://cdn-media-1.freecodecamp.org/images/gKCOU6o-Pi075R0WC-czpeuKbAyoOr7m7dCD)

Hourra ! Nous avons une grille de données éditable en temps réel avec pagination !

### Conclusion

Nous avons construit une grille de données en temps réel dans React en utilisant [react-table](https://react-table.js.org/) et [Hamoni Sync](https://www.hamoni.tech/). Avec react-table alimentant la grille de données et Hamoni Sync gérant l'état de la grille de données. Tout cela a été réalisé en quelques lignes de code et avec moins d'efforts pour concevoir la logique d'état en temps réel. Vous pouvez obtenir l'application finale de ce que nous avons construit sur [GitHub](https://github.com/pmbanugo/realtime-react-datatable). Il est possible de suivre quelle cellule est en cours d'édition ou de verrouiller les cellules actuellement éditées par un autre utilisateur. Je vous laisse cela comme un hack de week-end.

N'hésitez pas à laisser un commentaire si quelque chose n'est pas clair ou si vous rencontrez des problèmes en essayant d'ajouter un verrou ou de mettre en surbrillance les cellules en cours d'édition.

Bon codage 😊