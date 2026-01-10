---
title: How to create a three layer application with React
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
seo_title: null
seo_desc: 'By Cristian Salcescu

  Discover Functional JavaScript was named one of the best new Functional Programming
  books by BookAuthority!

  Splitting a Single Page Application into layers has a set of advantages:


  a better separation of concerns

  the layer imple...'
---

By Cristian Salcescu

[**Discover Functional JavaScript**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE) was named one of the [**best new Functional Programming books by BookAuthority**](https://bookauthority.org/books/new-functional-programming-books?t=7p46zt&s=award&book=1095338781)**!**

Splitting a Single Page Application into layers has a set of advantages:

* a better separation of concerns
* the layer implementation can be replaced
* the UI layer can be hard to test. By moving the logic to other layers, it becomes easier to test.

Below we can see the diagram of an application split in the three main layers:

* UI (aka Presentation, View)
* Domain (aka Business)
* Data Access

![Image](https://cdn-media-1.freecodecamp.org/images/R9TvA7YLrnFcjcKJML6qZQ1Ovuv19SSqeYSZ)
_Application Layers_

### The showcase

I’ll take the case of an application managing a list of to-dos. The user is able to see and search for to-dos.

#### Check the full [implementation on git-hub](https://github.com/cristi-salcescu/todo-search-react).

![Image](https://cdn-media-1.freecodecamp.org/images/IZH5sOtfQIydXXvMK0Cv0B1gD4-esCk6ztSe)

### UI Layer

The UI layer is responsible for displaying data on the page, and for handling user interactions. The UI Layer is made up of components.

I split the page in the following components:

* `TodoContainer` manages the communication between `TodoSearch`, `TodoList` and other external objects
* `TodoSearchForm` is the form for searching to-dos
* `TodoList` displays the list of to-dos
* `TodoListItem:` displays a single to-do in the list

![Image](https://cdn-media-1.freecodecamp.org/images/NzfTbD-ZNPr8WPjOBJ40Mv2ATkO7iipike3f)
_Components Tree_

#### TodoSearch

The component uses the `handleChange` handler to read the input value on any change. `TodoSearch` exposes a new property: `onSearch` . It can be used by the parent component to handle the search click.

The component doesn't communicate with any other external objects, except its parent. `TodoSearch` is a presentation component.

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
      <button onClick={this.search} type="button">Search</button>
    </form>;
  }
}
```

#### TodoList

`TodoList` gets the list of `todos` to render using a property. It sends the `todos`, one by one, to the `TodoListItem`.

`TodoList` is a stateless functional component.

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

`TodoListItem` displays the `todo` received as a parameter. It is implemented as a stateless functional component.

```
export default function TodoListItem(props){
  return       <li>
    <div>{ props.todo.title}</div>
    <div>{ props.todo.userName }</div>
  </li>;
}
```

Read [**Functional Architecture with React and Redux**](https://read.amazon.com/kp/embed?asin=B0846NRJYR&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_o.hlEbDD02JB2) and learn how to build apps in function style.

[**Discover Functional JavaScript**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE&source=post_page---------------------------) was named one of the [**best new Functional Programming books by BookAuthority**](https://bookauthority.org/books/new-functional-programming-books?t=7p46zt&s=award&book=1095338781&source=post_page---------------------------)**!**

**For more on applying functional programming techniques in React take a look at** [**Functional React**](https://read.amazon.com/kp/embed?asin=B07S1NLFTS&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_Pko5CbA30383Y&source=post_page---------------------------)**.**

You can find me on [Medium](https://medium.com/@cristiansalcescu) and [Twitter](https://twitter.com/cristi_salcescu).

