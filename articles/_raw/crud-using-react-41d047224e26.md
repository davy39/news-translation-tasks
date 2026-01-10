---
title: How to perform CRUD operations using React
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
seo_title: null
seo_desc: 'By Zafar Saleem

  In my previous articles, we have already written the same Todo application using
  Vanilla JavaScript and Angular. Now it’s time to take this same example a little
  further and use an even more popular framework: React. This example assu...'
---

By Zafar Saleem

In my previous articles, we have already written the same Todo application using [Vanilla JavaScript](https://medium.com/@zafarsaleem/crud-operations-using-vanilla-javascript-cd6ee2feff67) and [Angular](https://medium.com/@zafarsaleem/crud-operations-in-angular-536e1c03a715). Now it’s time to take this same example a little further and use an even more popular framework: React. This example assumes that you’ve already installed [_node_](https://nodejs.org/en/%5C) and [_create-react-app_](https://github.com/facebook/create-react-app) on your system.

First of all, let's create a new React app with this command.

```
create-react-app todo
```

Give it a few seconds and then you should have a todo folder in your file system. CD into that folder.

First thing that is created is a new file called _Todo.js_ inside the _src/_ folder. Here is the code in that file:

```
import React, { Component } from 'react';
```

```
class Todo extends Component {     render() {        return(<h1>This message is from Todo component</h1>)     }  }
```

```
export default Todo;
```

First, we are importing _React_ and _Component_ from the React core.

Then we are creating a _Todo component_ which extends from _Component_.

The todo component has a _render_ method which renders JSX with an _h1_ element and the text “This message is from Todo component”.

Finally, we are exporting this component to use it in the rest of our project.

Now open _src/App.js_ file. We need to import our newly created Todo component after the import of the _App.css_ file.

Once there, now use this component inside the render method of the App component.

```
import React, { Component } from 'react';import logo from './logo.svg';import './App.css';
```

```
// import Todo component hereimport Todo from './Todo';
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
render() {    // use Todo component inside render method.    return (      <div className="App">        <Todo />      </div>    );  }}
```

```
export default App;
```

Now that we have the basic Todo Component file and have imported it in the App component and used it, it’s time to add some _mockData_. This time we are going to use _React states_ to work with our data. This makes things easier in order to perform CRUD operations and update the view accordingly. Add this code to the Todo component:

```
class Todo extends Component {  state = {    edit: false,    id: null,    mockData: [{      id: '1',      title: 'Buy Milk',      done: false,      date: new Date()    }, {      id: '2',      title: 'Meeting with Ali',      done: false,      date: new Date()    }, {      id: '3',      title: 'Tea break',      done: false,      date: new Date()    }, {      id: '4',      title: 'Go for a run.',      done: false,      date: new Date()    }]  }}
```

> State is like a data store to the ReactJS component. It is mostly used to update the component when a user performs some action like `clicking button`, `typing some text`, `pressing some key`, etc.

The above state can also be placed inside the constructor. Choose whichever method you like.

As you can see, _state_ in React is simply a javascript object with properties such as _edit_, _id,_ and _mockData_. The _edit_ property is a boolean. It will be used to show and hide the edit form to edit a particular item in _mockData_. The _id_ property is used to set the id of the current item inside mockData to perform the update operation.

Now that we have the mockData added to the state which is also called _initial state_, it’s time to add JSX. If you would like to know more about JSX, then head over [here](https://reactjs.org/docs/introducing-jsx.html) for more details. It is a syntax extension to JavaScript which produces React elements to render data on pages.

JSX lists all the items in mockData, that is it performs the “R” operation of CRUD. To do that, render this code to the class.

```
render() {  return (    <div>      <form onSubmit={this.onSubmitHandle.bind(this)}>        <input type="text" name="item" className="item" />        <button className="btn-add-item">Add</button>      </form>      <ul>        {this.state.mockData.map(item => (          <li key={item.id}>            {item.title}            <button onClick={this.onDeleteHandle.bind(this, item.id)}>Delete</button>            <button onClick={this.onEditHandle.bind(this, item.id, item.title)}>Edit</button>            <button onClick={this.onCompleteHandle}>Complete</button>          </li>        ))}      </ul>    </div>  );}
```

The _Render_ method is simple. First, it has the form which is used to add a new item into the todo list. This form has an _onSubmit_ event and it calls the _onSubmitHandle_ method which we will write later in this component.

Then we have _ul_ and simply map through all the items inside mockData and present the title and add same buttons as in our previous examples (Delete, Edit and Complete). Now if you run your application using the “npm start” command you should see something like this.

![Image](https://cdn-media-1.freecodecamp.org/images/TMDfLfRAjiocbmKBBCZcTy-YwOcSGKHv9n59)

Now that R operation is completed, it is time to add a _create_ operation which is the C in CRUD. Add the _onSubmitHandle_ method to the Todo Component like below.

```
onSubmitHandle(event) {  event.preventDefault();
```

```
  this.setState({    mockData: [...this.state.mockData, {        id: Date.now(),        title: event.target.item.value,        done: false,        date: new Date()    }]  });
```

```
  event.target.item.value = '';}
```

The _onSubmitHandle_ method is called when the Add button is clicked. Here we use the setState method on Todo’s state which is:

> `setState()` schedules an update to a component’s `state` object. When state changes, the component responds by re-rendering.

Here, the setState method is called to reset the state of the Todo Component which has mockData. It simply appends the new item taken from the input field. Finally, set the value of the input field to empty.

![Image](https://cdn-media-1.freecodecamp.org/images/3gWNcPz0Lh38lx2p9iQBemRoZtnyKXY0Ofaw)

Go ahead and refresh the app in your browser and type “Hike time” or anything you want and press the ADD button. You should be able to see the new item at the bottom of the list like above.

Now that the C is done, it’s time for D which is Delete. Simple add the _onDeleteHandle_ method to the Todo component like below.

```
onDeleteHandle() {  let id = arguments[0];
```

```
  this.setState({    mockData: this.state.mockData.filter(item => {      if (item.id !== id) {        return item;      }    })  });}
```

This method is triggered when the delete button is clicked. As you can see, we are binding this and item.id to _onDeleteHandle_. The _this_ keyword is necessary so that we have access to the current scope to access the state of the Todo Component with the _this_ keyword, whereas the id part is used to delete that particular item.

In order to access the item.id, we are going to use the arguments[0] object. Once we have the id, then set the state and filter through mockData. Find the item that needs to be deleted and return all the items except the one that needs to be deleted.

Go ahead and refresh your browser and press delete on the first item and you should see that it is deleted, like in the below screenshot.

![Image](https://cdn-media-1.freecodecamp.org/images/JbMIsm7x2PzYNJISa6aJcI67EqVBpokCAZQX)

That’s all for the delete part. The Update part, as usual, consists of 2 parts. First, show the edit form when the edit button is pressed, then perform the update operation.

To show and hide the edit form, we are going to use the edit property we added to state. So add the below _renderEditForm_ method to the component.

```
renderEditForm() {    if (this.state.edit) {      return <form onSubmit={this.onUpdateHandle.bind(this)}>        <input type="text" name="updatedItem" className="item" defaultValue={this.state.title} />        <button className="update-add-item">Update</button>      </form>    }  }
```

It checks the edit state, and based on that it returns editForm which is the JSX syntax of the form.

Now call the above method in the render method inside the return keyword just above the current form, like below:

```
{this.renderEditForm()}
```

Now that this part is out of our way, it’s time to manipulate the edit property. Add the below _onEditHandle_ method to the Todo Component:

```
onEditHandle(event) {  this.setState({    edit: true,    id: arguments[0],    title: arguments[1]  });}
```

This method is triggered when the Edit button is pressed. We are binding three parameters: _this_, _id_, and _title_. The _this_ keyword is used to reference the current component. It sets the _id_ property to the id of the current item being edited. It sets _edit_ to _true_ and adds a title property to the state, which we will access later in this component.

Now that we have this code in our component, go to the browser, refresh, and click on the edit button for the first item which will show the edit form like below:

![Image](https://cdn-media-1.freecodecamp.org/images/SwS8OfTwPytVo9o0j4tiSfGP4ps6-ZeRRFjF)

This form has an input field and an update button. Now it’s time to handle the U part of CRUD. When the _UPDATE_ button, in the edit form shown above, is pressed, the below method will be triggered:

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

Add the above method to your Todo Component. This sets the state of the component, maps through mockData inside the state, and finds the item that needs to be updated and set its title with the new title. Finally, set the edit property of the state to false to hide the form. That is it.

Now run your code in your browser and try to update the first item. You should be able to see the updated title.

![Image](https://cdn-media-1.freecodecamp.org/images/E5urORe5I0fXViTeBI2BQqBxxAG57ihjoQXY)

The final method is used to set the item to a completed state. Add the below method which does exactly that.

```
onCompleteHandle() {    let id = arguments[0];
```

```
    this.setState({      mockData: this.state.mockData.map(item => {        if (item.id === id) {          item['done'] = true;          return item;        }
```

```
      return item;    })  });}
```

The above method sets he property of the item in mockData to true. This is pretty much the same as in our previous two examples in Vanilla JavaScript and Angular.

Now to make this work, add the below code to “li” to set its class based on the “done” property state in mockData.

```
className={ item.done ? 'done' : 'hidden' }
```

Now refresh your browser and press the complete button. You should be able to see the below changes.

![Image](https://cdn-media-1.freecodecamp.org/images/x7vO3rwHdzZvgJtGhV16YbT0olSN5amxYgQd)

Below is the basic CSS that needs to be added to _index.css_ file on order to display done items on the screen.

```
.done {  text-decoration: line-through;}
```

That is it. As you can see, Reactjs is an even more component-centric solution to modern JavaScript apps. The next task for you would be to split the form element into its own components so that we do not need to use two form elements for the update and add operations. That should be a simple and fun task for everyone.

To get the complete code, please clone the below repository.

[**zafar-saleem/react-todo**](https://github.com/zafar-saleem/react-todo)  
[_Contribute to zafar-saleem/react-todo development by creating an account on GitHub._github.com](https://github.com/zafar-saleem/react-todo)

