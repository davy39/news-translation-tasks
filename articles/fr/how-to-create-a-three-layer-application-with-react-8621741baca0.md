---
title: Comment créer une application à trois couches avec React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-23T19:04:14.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-three-layer-application-with-react-8621741baca0
coverImage: https://cdn-media-1.freecodecamp.org/images/1*R1_hBuSvlzK6TlDt3aJM8A.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Comment créer une application à trois couches avec React
seo_desc: 'By Cristian Salcescu

  Discover Functional JavaScript was named one of the best new Functional Programming
  books by BookAuthority!

  Splitting a Single Page Application into layers has a set of advantages:


  a better separation of concerns

  the layer imple...'
---

Par Cristian Salcescu

[**Découvrez Functional JavaScript**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE) a été nommé l'un des [**meilleurs nouveaux livres sur la programmation fonctionnelle par BookAuthority**](https://bookauthority.org/books/new-functional-programming-books?t=7p46zt&s=award&book=1095338781) !

Diviser une application monopage en couches présente un ensemble d'avantages :

* une meilleure séparation des préoccupations
* l'implémentation de la couche peut être remplacée
* la couche UI peut être difficile à tester. En déplaçant la logique vers d'autres couches, elle devient plus facile à tester.

Ci-dessous, nous pouvons voir le diagramme d'une application divisée en trois couches principales :

* UI (aka Présentation, Vue)
* Domaine (aka Métier)
* Accès aux données

![Image](https://cdn-media-1.freecodecamp.org/images/R9TvA7YLrnFcjcKJML6qZQ1Ovuv19SSqeYSZ)
_Couches de l'application_

### La démonstration

Je vais prendre le cas d'une application gérant une liste de tâches. L'utilisateur peut voir et rechercher des tâches.

#### Voir l'implémentation complète sur [git-hub](https://github.com/cristi-salcescu/todo-search-react).

![Image](https://cdn-media-1.freecodecamp.org/images/IZH5sOtfQIydXXvMK0Cv0B1gD4-esCk6ztSe)

### Couche UI

La couche UI est responsable de l'affichage des données sur la page et de la gestion des interactions utilisateur. La couche UI est composée de composants.

J'ai divisé la page en les composants suivants :

* `TodoContainer` gère la communication entre `TodoSearch`, `TodoList` et d'autres objets externes
* `TodoSearchForm` est le formulaire pour rechercher des tâches
* `TodoList` affiche la liste des tâches
* `TodoListItem` affiche une seule tâche dans la liste

![Image](https://cdn-media-1.freecodecamp.org/images/NzfTbD-ZNPr8WPjOBJ40Mv2ATkO7iipike3f)
_Arbre des composants_

#### TodoSearch

Le composant utilise le gestionnaire `handleChange` pour lire la valeur de l'entrée à chaque changement. `TodoSearch` expose une nouvelle propriété : `onSearch`. Elle peut être utilisée par le composant parent pour gérer le clic de recherche.

Le composant ne communique avec aucun autre objet externe, sauf son parent. `TodoSearch` est un composant de présentation.

```
export default class TodoSearch extends React.Component { 
  constructor(props){
    super(props);
    this.search = this.search.bind(this);
    this.handleChange = this.handleChange.bind(this);

    this.state = { text: "" };
  }
  
  search(){
    const query = Object.freeze({ text: this.state.text });
    if(this.props.onSearch)
      this.props.onSearch(query);
  }
  
  handleChange(event) {
    this.setState({text: event.target.value});
  }
  
  render() {
    return <form>
      <input onChange={this.handleChange} value={this.state.text} />
      <button onClick={this.search} type="button">Rechercher</button>
    </form>;
  }
}
```

#### TodoList

`TodoList` obtient la liste des `todos` à rendre à l'aide d'une propriété. Il envoie les `todos`, un par un, à `TodoListItem`.

`TodoList` est un composant fonctionnel sans état.

```
export default function TodoList(props) {
  function renderTodoItem(todo){
    return <TodoListItem todo={todo} key={todo.id}></TodoListItem>;
  }

  return <div className="todo-list">
      <ul>
        { props.todos.map(renderTodoItem) }
      </ul>
    </div>;
}
```

#### TodoListItem

`TodoListItem` affiche le `todo` reçu en tant que paramètre. Il est implémenté en tant que composant fonctionnel sans état.

```
export default function TodoListItem(props){
  return       <li>
    <div>{ props.todo.title}</div>
    <div>{ props.todo.userName }</div>
  </li>;
}
```

Lisez [**Architecture fonctionnelle avec React et Redux**](https://read.amazon.com/kp/embed?asin=B0846NRJYR&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_o.hlEbDD02JB2) et apprenez à construire des applications en style fonctionnel.

[**Découvrez Functional JavaScript**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE&source=post_page---------------------------) a été nommé l'un des [**meilleurs nouveaux livres sur la programmation fonctionnelle par BookAuthority**](https://bookauthority.org/books/new-functional-programming-books?t=7p46zt&s=award&book=1095338781&source=post_page---------------------------) !

**Pour en savoir plus sur l'application des techniques de programmation fonctionnelle dans React, consultez** [**Functional React**](https://read.amazon.com/kp/embed?asin=B07S1NLFTS&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_Pko5CbA30383Y&source=post_page---------------------------).

Vous pouvez me trouver sur [Medium](https://medium.com/@cristiansalcescu) et [Twitter](https://twitter.com/cristi_salcescu).