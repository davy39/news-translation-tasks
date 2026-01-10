---
title: Comment effectuer des opérations CRUD avec React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-28T17:47:12.000Z'
originalURL: https://freecodecamp.org/news/crud-using-react-41d047224e26
coverImage: https://cdn-media-1.freecodecamp.org/images/1*EntHChgUyirgbZ9A3zTxkA.png
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: Comment effectuer des opérations CRUD avec React
seo_desc: 'By Zafar Saleem

  In my previous articles, we have already written the same Todo application using
  Vanilla JavaScript and Angular. Now it’s time to take this same example a little
  further and use an even more popular framework: React. This example assu...'
---

Par Zafar Saleem

Dans mes articles précédents, nous avons déjà écrit la même application Todo en utilisant [Vanilla JavaScript](https://medium.com/@zafarsaleem/crud-operations-using-vanilla-javascript-cd6ee2feff67) et [Angular](https://medium.com/@zafarsaleem/crud-operations-in-angular-536e1c03a715). Maintenant, il est temps de prendre cet exemple un peu plus loin et d'utiliser un framework encore plus populaire : React. Cet exemple suppose que vous avez déjà installé [_node_](https://nodejs.org/en/%5C) et [_create-react-app_](https://github.com/facebook/create-react-app) sur votre système.

Tout d'abord, créons une nouvelle application React avec cette commande.

```
create-react-app todo
```

Donnez-lui quelques secondes et vous devriez avoir un dossier todo dans votre système de fichiers. Accédez à ce dossier.

La première chose qui est créée est un nouveau fichier appelé _Todo.js_ à l'intérieur du dossier _src/_. Voici le code dans ce fichier :

```
import React, { Component } from 'react';
```

```
class Todo extends Component {     render() {        return(<h1>Ce message provient du composant Todo</h1>)     }  }
```

```
export default Todo;
```

Tout d'abord, nous importons _React_ et _Component_ depuis le cœur de React.

Ensuite, nous créons un _composant Todo_ qui étend _Component_.

Le composant todo a une méthode _render_ qui rend JSX avec un élément _h1_ et le texte « Ce message provient du composant Todo ».

Enfin, nous exportons ce composant pour l'utiliser dans le reste de notre projet.

Ouvrez maintenant le fichier _src/App.js_. Nous devons importer notre composant Todo nouvellement créé après l'import du fichier _App.css_.

Une fois là, utilisez ce composant à l'intérieur de la méthode render du composant App.

```
import React, { Component } from 'react';import logo from './logo.svg';import './App.css';
```

```
// importer le composant Todo iciimport Todo from './Todo';
```

```
class App extends Component {
```

```
constructor(props) {    super(props);
```

```
this.state = {      show: false    };  }
```

```
render() {    // utiliser le composant Todo à l'intérieur de la méthode render.    return (      <div className="App">        <Todo />      </div>    );  }}
```

```
export default App;
```

Maintenant que nous avons le fichier de composant Todo de base et que nous l'avons importé dans le composant App et utilisé, il est temps d'ajouter des _mockData_. Cette fois, nous allons utiliser les _états React_ pour travailler avec nos données. Cela facilite les opérations CRUD et met à jour la vue en conséquence. Ajoutez ce code au composant Todo :

```
class Todo extends Component {  state = {    edit: false,    id: null,    mockData: [{      id: '1',      title: 'Acheter du lait',      done: false,      date: new Date()    }, {      id: '2',      title: 'Réunion avec Ali',      done: false,      date: new Date()    }, {      id: '3',      title: 'Pause café',      done: false,      date: new Date()    }, {      id: '4',      title: 'Aller courir.',      done: false,      date: new Date()    }]  }}
```

> L'état est comme un magasin de données pour le composant ReactJS. Il est principalement utilisé pour mettre à jour le composant lorsqu'un utilisateur effectue une action comme `cliquer sur un bouton`, `saisir du texte`, `appuyer sur une touche`, etc.

L'état ci-dessus peut également être placé à l'intérieur du constructeur. Choisissez la méthode que vous préférez.

Comme vous pouvez le voir, l'_état_ dans React est simplement un objet JavaScript avec des propriétés telles que _edit_, _id_ et _mockData_. La propriété _edit_ est un booléen. Elle sera utilisée pour afficher et masquer le formulaire d'édition afin d'éditer un élément particulier dans _mockData_. La propriété _id_ est utilisée pour définir l'id de l'élément actuel dans mockData afin d'effectuer l'opération de mise à jour.

Maintenant que nous avons ajouté mockData à l'état, qui est également appelé _état initial_, il est temps d'ajouter JSX. Si vous souhaitez en savoir plus sur JSX, rendez-vous [ici](https://reactjs.org/docs/introducing-jsx.html) pour plus de détails. Il s'agit d'une extension de syntaxe à JavaScript qui produit des éléments React pour rendre les données sur les pages.

JSX liste tous les éléments dans mockData, c'est-à-dire qu'il effectue l'opération « R » de CRUD. Pour ce faire, rendez ce code à la classe.

```
render() {  return (    <div>      <form onSubmit={this.onSubmitHandle.bind(this)}>        <input type="text" name="item" className="item" />        <button className="btn-add-item">Ajouter</button>      </form>      <ul>        {this.state.mockData.map(item => (          <li key={item.id}>            {item.title}            <button onClick={this.onDeleteHandle.bind(this, item.id)}>Supprimer</button>            <button onClick={this.onEditHandle.bind(this, item.id, item.title)}>Éditer</button>            <button onClick={this.onCompleteHandle}>Terminer</button>          </li>        ))}      </ul>    </div>  );}
```

La méthode _Render_ est simple. Tout d'abord, elle a le formulaire qui est utilisé pour ajouter un nouvel élément dans la liste de tâches. Ce formulaire a un événement _onSubmit_ et il appelle la méthode _onSubmitHandle_ que nous écrirons plus tard dans ce composant.

Ensuite, nous avons _ul_ et nous parcourons simplement tous les éléments à l'intérieur de mockData et présentons le titre et ajoutons les mêmes boutons que dans nos exemples précédents (Supprimer, Éditer et Terminer). Maintenant, si vous exécutez votre application en utilisant la commande « npm start », vous devriez voir quelque chose comme ceci.

![Image](https://cdn-media-1.freecodecamp.org/images/TMDfLfRAjiocbmKBBCZcTy-YwOcSGKHv9n59)

Maintenant que l'opération R est terminée, il est temps d'ajouter une opération de _création_ qui est le C dans CRUD. Ajoutez la méthode _onSubmitHandle_ au composant Todo comme ci-dessous.

```
onSubmitHandle(event) {  event.preventDefault();
```

```
  this.setState({    mockData: [...this.state.mockData, {        id: Date.now(),        title: event.target.item.value,        done: false,        date: new Date()    }]  });
```

```
  event.target.item.value = '';}
```

La méthode _onSubmitHandle_ est appelée lorsque le bouton Ajouter est cliqué. Ici, nous utilisons la méthode setState sur l'état de Todo qui est :

> `setState()` planifie une mise à jour de l'objet `state` d'un composant. Lorsque l'état change, le composant répond en se rendant à nouveau.

Ici, la méthode setState est appelée pour réinitialiser l'état du composant Todo qui a mockData. Il ajoute simplement le nouvel élément pris depuis le champ de saisie. Enfin, définissez la valeur du champ de saisie à vide.

![Image](https://cdn-media-1.freecodecamp.org/images/3gWNcPz0Lh38lx2p9iQBemRoZtnyKXY0Ofaw)

Allez-y et actualisez l'application dans votre navigateur et tapez « Temps de randonnée » ou ce que vous voulez et appuyez sur le bouton AJOUTER. Vous devriez pouvoir voir le nouvel élément en bas de la liste comme ci-dessus.

Maintenant que le C est fait, il est temps pour le D qui est Supprimer. Ajoutez simplement la méthode _onDeleteHandle_ au composant Todo comme ci-dessous.

```
onDeleteHandle() {  let id = arguments[0];
```

```
  this.setState({    mockData: this.state.mockData.filter(item => {      if (item.id !== id) {        return item;      }    })  });}
```

Cette méthode est déclenchée lorsque le bouton de suppression est cliqué. Comme vous pouvez le voir, nous liaisons this et item.id à _onDeleteHandle_. Le mot-clé _this_ est nécessaire afin que nous ayons accès à la portée actuelle pour accéder à l'état du composant Todo avec le mot-clé _this_, tandis que la partie id est utilisée pour supprimer cet élément particulier.

Afin d'accéder à item.id, nous allons utiliser l'objet arguments[0]. Une fois que nous avons l'id, définissez l'état et filtrez à travers mockData. Trouvez l'élément qui doit être supprimé et retournez tous les éléments sauf celui qui doit être supprimé.

Allez-y et actualisez votre navigateur et appuyez sur supprimer sur le premier élément et vous devriez voir qu'il est supprimé, comme dans la capture d'écran ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/JbMIsm7x2PzYNJISa6aJcI67EqVBpokCAZQX)

C'est tout pour la partie suppression. La partie Mise à jour, comme d'habitude, se compose de 2 parties. Tout d'abord, affichez le formulaire d'édition lorsque le bouton d'édition est pressé, puis effectuez l'opération de mise à jour.

Pour afficher et masquer le formulaire d'édition, nous allons utiliser la propriété edit que nous avons ajoutée à l'état. Ajoutez donc la méthode _renderEditForm_ ci-dessous au composant.

```
renderEditForm() {    if (this.state.edit) {      return <form onSubmit={this.onUpdateHandle.bind(this)}>        <input type="text" name="updatedItem" className="item" defaultValue={this.state.title} />        <button className="update-add-item">Mettre à jour</button>      </form>    }  }
```

Il vérifie l'état d'édition, et en fonction de cela, il retourne editForm qui est la syntaxe JSX du formulaire.

Maintenant, appelez la méthode ci-dessus dans la méthode render à l'intérieur du mot-clé return juste au-dessus du formulaire actuel, comme ci-dessous :

```
{this.renderEditForm()}
```

Maintenant que cette partie est hors de notre chemin, il est temps de manipuler la propriété edit. Ajoutez la méthode _onEditHandle_ ci-dessous au composant Todo :

```
onEditHandle(event) {  this.setState({    edit: true,    id: arguments[0],    title: arguments[1]  });}
```

Cette méthode est déclenchée lorsque le bouton Éditer est pressé. Nous liaisons trois paramètres : _this_, _id_ et _title_. Le mot-clé _this_ est utilisé pour référencer le composant actuel. Il définit la propriété _id_ à l'id de l'élément actuel en cours d'édition. Il définit _edit_ à _true_ et ajoute une propriété title à l'état, que nous accéderons plus tard dans ce composant.

Maintenant que nous avons ce code dans notre composant, allez dans le navigateur, actualisez et cliquez sur le bouton d'édition pour le premier élément qui affichera le formulaire d'édition comme ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/SwS8OfTwPytVo9o0j4tiSfGP4ps6-ZeRRFjF)

Ce formulaire a un champ de saisie et un bouton de mise à jour. Maintenant, il est temps de gérer la partie U de CRUD. Lorsque le bouton _MISE À JOUR_, dans le formulaire d'édition montré ci-dessus, est pressé, la méthode ci-dessous sera déclenchée :

```
onUpdateHandle(event) {  event.preventDefault();
```

```
  this.setState({      mockData: this.state.mockData.map(item => {        if (item.id === this.state.id) {          item['title'] = event.target.updatedItem.value;          return item;        }
```

```
        return item;      })   });
```

```
   this.setState({      edit: false   });}
```

Ajoutez la méthode ci-dessus à votre composant Todo. Cela définit l'état du composant, parcourt mockData à l'intérieur de l'état, et trouve l'élément qui doit être mis à jour et définit son titre avec le nouveau titre. Enfin, définissez la propriété edit de l'état à false pour masquer le formulaire. C'est tout.

Maintenant, exécutez votre code dans votre navigateur et essayez de mettre à jour le premier élément. Vous devriez pouvoir voir le titre mis à jour.

![Image](https://cdn-media-1.freecodecamp.org/images/E5urORe5I0fXViTeBI2BQqBxxAG57ihjoQXY)

La méthode finale est utilisée pour définir l'élément à un état terminé. Ajoutez la méthode ci-dessous qui fait exactement cela.

```
onCompleteHandle() {    let id = arguments[0];
```

```
    this.setState({      mockData: this.state.mockData.map(item => {        if (item.id === id) {          item['done'] = true;          return item;        }
```

```
      return item;    })  });}
```

La méthode ci-dessus définit la propriété de l'élément dans mockData à true. Cela est pratiquement identique à nos deux exemples précédents en Vanilla JavaScript et Angular.

Maintenant, pour que cela fonctionne, ajoutez le code ci-dessous à « li » pour définir sa classe en fonction de l'état de la propriété « done » dans mockData.

```
className={ item.done ? 'done' : 'hidden' }
```

Maintenant, actualisez votre navigateur et appuyez sur le bouton terminer. Vous devriez pouvoir voir les changements ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/x7vO3rwHdzZvgJtGhV16YbT0olSN5amxYgQd)

Voici le CSS de base qui doit être ajouté au fichier _index.css_ afin d'afficher les éléments terminés à l'écran.

```
.done {  text-decoration: line-through;}
```

C'est tout. Comme vous pouvez le voir, Reactjs est une solution encore plus centrée sur les composants pour les applications JavaScript modernes. La prochaine tâche pour vous serait de diviser l'élément de formulaire en ses propres composants afin que nous n'ayons pas besoin d'utiliser deux éléments de formulaire pour les opérations de mise à jour et d'ajout. Cela devrait être une tâche simple et amusante pour tout le monde.

Pour obtenir le code complet, veuillez cloner le dépôt ci-dessous.

[**zafar-saleem/react-todo**](https://github.com/zafar-saleem/react-todo)  
[_Contribute to zafar-saleem/react-todo development by creating an account on GitHub._github.com](https://github.com/zafar-saleem/react-todo)