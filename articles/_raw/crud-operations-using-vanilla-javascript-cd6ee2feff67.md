---
title: How to perform CRUD operations using vanilla JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-13T20:16:53.000Z'
originalURL: https://freecodecamp.org/news/crud-operations-using-vanilla-javascript-cd6ee2feff67
coverImage: https://cdn-media-1.freecodecamp.org/images/1*xn7U354KKc64AeCSZWLdcw.jpeg
tags:
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Zafar Saleem

  Nowadays there are a number of JavaScript frameworks around such as React, Angular,
  Vue and so on. They all offer a simple and easy approach towards the development
  of web applications, especially SPAs.

  However, many JavaScript learne...'
---

By Zafar Saleem

Nowadays there are a number of JavaScript frameworks around such as React, Angular, Vue and so on. They all offer a simple and easy approach towards the development of web applications, especially SPAs.

However, many JavaScript learners tend to begin learning these frameworks and know little about how to develop similar apps in vanilla JavaScript.

One of the most basic operations in any application is CRUD (stands for Create, Read, Update, Delete). This is something we are going to achieve today. We will take a basic and good old example: a Todo app.

Even though vanilla JavaScript will be used for this tutorial, we’ll use ES6 syntax instead of plain old JavaScript syntax. In order to accomplish that, we’ll use the babel transpiler to convert ES6/ES7 to ES5, and we’ll use webpack as a build tool.

I am assuming that you already have the latest version of node.js on your computer. Setting up our environment is going to take some extra time, so no need to go into these details. Simply clone my boilerplate code from here ([https://github.com/zafar-saleem/hut](https://github.com/zafar-saleem/hut)) and run “npm install” to install all the dependencies.

The new files will go into the `/src` folder. So create a new file called `Todo.js` inside the `/src/scripts/` folder and add the code below to that file:

```js
class Todo {
  constructor() {}
}

export default Todo;

```

As you can see in the above code, we are creating a class `Todo`, and inside that class we are writing a constructor function. Even though JavaScript does not have classes by default, ES6 has classes (which is, in reality, syntactic sugar on top of the JavaScript prototype).

Now when we create a new instance of this class using the `new` keyword, the constructor function is automatically called. That is where we will add some attributes to the `Todo` class which we will be able to access in this entire class using the keyword `this`.

Now that we have above code, go ahead and import the above file in the `src/index.js` file and make a new instance of this class:

```js
import Todo from './scripts/Todo';

let todo = new Todo();

```

Now we have some basic code in `Todo.js`. We also need some basic HTML code. Add the code below to a file named `index.html` in the root folder:

```html
<div class="edit-popup">
  <input type="text" name="" class="edit-item" />
  <button class="btn-update">Update</button>
</div>
<div class="container">
  <div class="sections">
    <input type="text" name="" class="item" />
    <button class="btn-add-item">Add</button>
    <ul>
      <li><a href="#">All</a></li>
      <li><a href="#">Today</a></li>
      <li><a href="#">Tomorrow</a></li>
    </ul>
  </div>
  <div class="items">
    <ul class="list-items"></ul>
  </div>
</div>

```

Now that we have the basic HTML code, let’s go back to `Todo.js` and get the reference to our `.list-item` container. Add your new code inside the constructor:

```js
class Todo {
  constructor() {
    this.list = document.querySelector('.list-items');
    this.render();
  }
}

export default Todo;

```

After getting the reference to the `.list-item` element, I am calling the render function to render a list of items on the screen. This function does not exist yet so we are going to write it next.

But before writing the render function, we need some mock data that we are going to render. So for the purpose of this tutorial, we are going to use an array of objects. Add your mock data at the top of the `Todo.js` file:

```js
let mockData = [
  {
    id: '1',
    title: 'This is title',
    done: false,
    date: new Date(),
  },
  {
    id: '2',
    title: 'This is second title',
    done: false,
    date: new Date(),
  },
  {
    id: '3',
    title: 'This is third title',
    done: false,
    date: new Date(),
  },
  {
    id: '4',
    title: 'This is forth title',
    done: false,
    date: new Date(),
  },
];

class Todo {
  constructor() {
    this.list = document.querySelector('.list-items');
    this.render();
  }
}

export default Todo;

```

Now back to the render function, which is completed below:

```js
class Todo {
  constructor() {
    this.list = document.querySelector('.list-items');
    this.render();
  }

  // render function
  render() {
    this.list.innerHTML = '';

    mockData.forEach((item) => {
      this.createDomElements(item.id);
      this.li.insertAdjacentHTML('afterbegin', item.title);

      if (item.done) {
        this.li.classList.add('done');
      }

      this.list.appendChild(this.li);
    });
  }
}

export default Todo;

```

In this function we are making sure that the `this.list` container is empty. That is, we do not want any item to be appended to existing items. The first line simply makes the container empty before appending new items.

Next we are looping through the `mockData` array that we created at the top of the `Todo.js` file using the `forEach` function. Inside the `forEach` callback function, we are first creating some DOM elements by calling the `createDomElements(item.id)` function, and we are passing the current item’s id to that function. I will write this function next, but before getting there let’s finish writing this function.

Once it creates the new DOM element (the `li` element) with child elements (buttons in this case), it adds that `li` element into the `Todo` class as an attribute using the `this` keyword. Now we can access that `li` element throughout the `Todo` class, so I am accessing that `li` element and adding the title using the `insertAdjacentHTML()` function.

Next I am checking if the current item is completed or done. If it is, then I add a class to the current `li` element which adds a line-through style on the item.

And finally I append that `li` element to `this.list`.

Now let’s write the `createDomElements()` function:

```js
class Todo {
  constructor() {
    this.list = document.querySelector('.list-items');
    this.render();
  }

  render() {
    this.list.innerHTML = '';

    mockData.forEach((item) => {
      this.createDomElements(item.id);
      this.li.insertAdjacentHTML('afterbegin', item.title);

      if (item.done) {
        this.li.classList.add('done');
      }

      this.list.appendChild(this.li);
    });
  }

  // Create DOM Elements step
  createDomElements(id) {
    this.li = document.createElement('li');
    this.edit = document.createElement('button');
    this.delete = document.createElement('button');
    this.complete = document.createElement('button');

    this.edit.classList.add('btn-edit');
    this.delete.classList.add('btn-delete');
    this.complete.classList.add('btn-complete');

    this.delete.setAttribute('data-id', id);
    this.edit.setAttribute('data-id', id);
    this.complete.setAttribute('data-id', id);

    this.edit.innerHTML = 'Edit';
    this.delete.innerHTML = 'Delete';
    this.complete.innerHTML = 'Complete';

    this.li.appendChild(this.delete);
    this.li.appendChild(this.edit);
    this.li.appendChild(this.complete);
  }
}

export default Todo;

```

This function has a lot of code, but it is simple to understand. I simply create `li` elements, delete, edit and complete buttons. Then I add some classes to all of these buttons and set the `data-id` attribute and assign the current item’s id that we passed as an argument from the render function. Then I put text on these buttons (Edit, Delete and Complete) using `innerHTML`.

Finally, I append these buttons to the `li` element which I later access in the render function to perform further operations.

Now that we have the basic structure, if you run `npm run dev` and go to http://localhost:2770 in the browser, you should have the below items, an input field and button, and four items with their respective buttons.

Until now you should have the “R” part of CRUD — I am reading all the elements from `mockData` and placing them on the screen.

Now that the Read part is done, it is time begin working on the C part of CRUD. For that, we'll write a function named `create`:

```js
class Todo {
  constructor() {
    this.list = document.querySelector('.list-items');
    this.render();
  }

  render() {
    this.list.innerHTML = '';

    mockData.forEach((item) => {
      this.createDomElements(item.id);
      this.li.insertAdjacentHTML('afterbegin', item.title);

      if (item.done) {
        this.li.classList.add('done');
      }

      this.list.appendChild(this.li);
    });
  }

  createDomElements(id) {
    this.li = document.createElement('li');
    this.edit = document.createElement('button');
    this.delete = document.createElement('button');
    this.complete = document.createElement('button');

    this.edit.classList.add('btn-edit');
    this.delete.classList.add('btn-delete');
    this.complete.classList.add('btn-complete');

    this.delete.setAttribute('data-id', id);
    this.edit.setAttribute('data-id', id);
    this.complete.setAttribute('data-id', id);

    this.edit.innerHTML = 'Edit';
    this.delete.innerHTML = 'Delete';
    this.complete.innerHTML = 'Complete';

    this.li.appendChild(this.delete);
    this.li.appendChild(this.edit);
    this.li.appendChild(this.complete);
  }

  // Creating new item step
  create() {
    let todoItem = document.querySelector('.item').value;

    let newItem = {
      id: Date.now().toString(),
      title: todoItem,
      done: false,
      date: new Date(),
    };

    mockData.push(newItem);

    document.querySelector('.item').value = '';
    this.render();
  }
}

export default Todo;

```

The `create` function is pretty self explanatory: all it does is get the value from the text field. It creates a `newItem` object with the attributes `id`, `title`, `done`, and `date`.

Finally, it pushes that `newItem` into the `mockData` array, empties the `textfield` and calls the `render` function to render all the items with the newly created item.

Now go ahead try this in your browser. Put some text in the text field. Press the add button — but you do not see any change. That is expected, because there is still one last part to this. Simply add an event listener to the “add” button inside the constructor and call the `create` function as below:

```js
class Todo {
  constructor() {
    this.list = document.querySelector('.list-items');
    this.render();

    // event listener to add new item step
    document
      .querySelector('.btn-add-item')
      .addEventListener('click', this.create.bind(this));
  }

  render() {
    this.list.innerHTML = '';

    mockData.forEach((item) => {
      this.createDomElements(item.id);
      this.li.insertAdjacentHTML('afterbegin', item.title);

      if (item.done) {
        this.li.classList.add('done');
      }

      this.list.appendChild(this.li);
    });
  }

  createDomElements(id) {
    this.li = document.createElement('li');
    this.edit = document.createElement('button');
    this.delete = document.createElement('button');
    this.complete = document.createElement('button');

    this.edit.classList.add('btn-edit');
    this.delete.classList.add('btn-delete');
    this.complete.classList.add('btn-complete');

    this.delete.setAttribute('data-id', id);
    this.edit.setAttribute('data-id', id);
    this.complete.setAttribute('data-id', id);

    this.edit.innerHTML = 'Edit';
    this.delete.innerHTML = 'Delete';
    this.complete.innerHTML = 'Complete';

    this.li.appendChild(this.delete);
    this.li.appendChild(this.edit);
    this.li.appendChild(this.complete);
  }

  create() {
    let todoItem = document.querySelector('.item').value;

    let newItem = {
      id: Date.now().toString(),
      title: todoItem,
      done: false,
      date: new Date(),
    };

    mockData.push(newItem);

    document.querySelector('.item').value = '';
    this.render();
  }
}

export default Todo;

```

Now try it in your browser and voilà. You have the new item at the bottom of the list.

Two parts of the CRUD operations are completed. The next is the D part which is Delete.

For deleting an item, let’s write a `remove` function (`delete` is a reserved keyword in JavaScript and for that reason I named it `remove`):

```js
class Todo {
  constructor() {
    this.list = document.querySelector('.list-items');
    this.render();

    document
      .querySelector('.btn-add-item')
      .addEventListener('click', this.create.bind(this));
  }

  render() {
    this.list.innerHTML = '';

    mockData.forEach((item) => {
      this.createDomElements(item.id);
      this.li.insertAdjacentHTML('afterbegin', item.title);

      if (item.done) {
        this.li.classList.add('done');
      }

      this.list.appendChild(this.li);
    });
  }

  createDomElements(id) {
    this.li = document.createElement('li');
    this.edit = document.createElement('button');
    this.delete = document.createElement('button');
    this.complete = document.createElement('button');

    this.edit.classList.add('btn-edit');
    this.delete.classList.add('btn-delete');
    this.complete.classList.add('btn-complete');

    this.delete.setAttribute('data-id', id);
    this.edit.setAttribute('data-id', id);
    this.complete.setAttribute('data-id', id);

    this.edit.innerHTML = 'Edit';
    this.delete.innerHTML = 'Delete';
    this.complete.innerHTML = 'Complete';

    this.li.appendChild(this.delete);
    this.li.appendChild(this.edit);
    this.li.appendChild(this.complete);
  }

  create() {
    let todoItem = document.querySelector('.item').value;

    let newItem = {
      id: Date.now().toString(),
      title: todoItem,
      done: false,
      date: new Date(),
    };

    mockData.push(newItem);

    document.querySelector('.item').value = '';
    this.render();
  }

  // Delete item step
  remove(event) {
    let id = event.target.getAttribute('data-id');

    mockData = mockData.filter((item) => {
      if (item.id !== id) {
        return item;
      }
    });

    this.render();
  }
}

export default Todo;

```

This function is also quite simple: first it gets the `id` from the delete button element, which was added in the `createDomElements` function using the `data-id` attribute. It filters through `mockData` and places a check on the current item’s id with the delete button’s id. This check simply returns all items except the item this check returns `true`.

After this operation, it re-renders all the items by calling the `render` function at the bottom.

Things are looking good, but hold on a minute: this function needs to be triggered by calling the delete button. As you might recall, this button was added dynamically in the `createDomElements` function. Adding events to such elements are a little tricky. Since these items were not present when the DOM was loaded and were added later, adding the event listener directly to the delete, update and complete buttons is not going to work.

To make this happen, add the event listener to the document object and find the particular button (delete in this case) to perform the delete or remove operation.

```js
class Todo {
  constructor() {
    let self = this; // referencing this keyword

    this.list = document.querySelector('.list-items');
    this.render();

    document
      .querySelector('.btn-add-item')
      .addEventListener('click', this.create.bind(this));

    // step for adding Click Event listener to delete button
    document.addEventListener('click', (event) => {
      if (event.target.classList.contains('btn-delete')) {
        self.remove(event);
      }
    });
  }

  render() {
    this.list.innerHTML = '';

    mockData.forEach((item) => {
      this.createDomElements(item.id);
      this.li.insertAdjacentHTML('afterbegin', item.title);

      if (item.done) {
        this.li.classList.add('done');
      }

      this.list.appendChild(this.li);
    });
  }

  createDomElements(id) {
    this.li = document.createElement('li');
    this.edit = document.createElement('button');
    this.delete = document.createElement('button');
    this.complete = document.createElement('button');

    this.edit.classList.add('btn-edit');
    this.delete.classList.add('btn-delete');
    this.complete.classList.add('btn-complete');

    this.delete.setAttribute('data-id', id);
    this.edit.setAttribute('data-id', id);
    this.complete.setAttribute('data-id', id);

    this.edit.innerHTML = 'Edit';
    this.delete.innerHTML = 'Delete';
    this.complete.innerHTML = 'Complete';

    this.li.appendChild(this.delete);
    this.li.appendChild(this.edit);
    this.li.appendChild(this.complete);
  }

  create() {
    let todoItem = document.querySelector('.item').value;

    let newItem = {
      id: Date.now().toString(),
      title: todoItem,
      done: false,
      date: new Date(),
    };

    mockData.push(newItem);

    document.querySelector('.item').value = '';
    this.render();
  }

  remove(event) {
    let id = event.target.getAttribute('data-id');

    mockData = mockData.filter((item) => {
      if (item.id !== id) {
        return item;
      }
    });

    this.render();
  }
}

export default Todo;

```

To call remove, the word `self` is used. Inside the callback function, the `this` keyword loses its reference to the `Todo` class. For that reason, create a new variable called `self` and assign the `this` keyword to it at the top of the construction.

Inside the callback function, I check if the click element has a class `btn-delete` — that is, is it a delete button? Then simply trigger the `remove` function and pass the event as a parameter. I use this inside of the `remove` function to get the id of the current clicked element to perform the delete operation.

The Update part is slightly complicated. It consists of two functions. The first is to render the edit form, which has a text field and update button. The second is to update the function that performs the update operation:

```js
class Todo {
  constructor() {
    let self = this;

    this.list = document.querySelector('.list-items');
    this.render();

    document
      .querySelector('.btn-add-item')
      .addEventListener('click', this.create.bind(this));

    document.addEventListener('click', (event) => {
      if (event.target.classList.contains('btn-delete')) {
        self.remove(event);
      }
    });
  }

  // step to render edit form
  renderEditForm(event) {
    let id = event.target.getAttribute('data-id');

    document.querySelector('.edit-popup').classList.remove('hide');
    document.querySelector('.edit-popup').classList.add('show');
    document.querySelector('.btn-update').setAttribute('data-id', id);

    mockData.forEach((item) => {
      if (item.id === id) {
        document.querySelector('.edit-item').value = item.title;
      }
    });
  }

  render() {
    this.list.innerHTML = '';

    mockData.forEach((item) => {
      this.createDomElements(item.id);
      this.li.insertAdjacentHTML('afterbegin', item.title);

      if (item.done) {
        this.li.classList.add('done');
      }

      this.list.appendChild(this.li);
    });
  }

  createDomElements(id) {
    this.li = document.createElement('li');
    this.edit = document.createElement('button');
    this.delete = document.createElement('button');
    this.complete = document.createElement('button');

    this.edit.classList.add('btn-edit');
    this.delete.classList.add('btn-delete');
    this.complete.classList.add('btn-complete');

    this.delete.setAttribute('data-id', id);
    this.edit.setAttribute('data-id', id);
    this.complete.setAttribute('data-id', id);

    this.edit.innerHTML = 'Edit';
    this.delete.innerHTML = 'Delete';
    this.complete.innerHTML = 'Complete';

    this.li.appendChild(this.delete);
    this.li.appendChild(this.edit);
    this.li.appendChild(this.complete);
  }

  create() {
    let todoItem = document.querySelector('.item').value;

    let newItem = {
      id: Date.now().toString(),
      title: todoItem,
      done: false,
      date: new Date(),
    };

    mockData.push(newItem);

    document.querySelector('.item').value = '';
    this.render();
  }

  remove(event) {
    let id = event.target.getAttribute('data-id');

    mockData = mockData.filter((item) => {
      if (item.id !== id) {
        return item;
      }
    });

    this.render();
  }
}

export default Todo;

```

All the above code does is to add and remove CSS classes to show and hide the edit form which is already in the DOM with the edit-popup class. Get the id from the edit button and place it on the update button. Iterate through `mockData` and check for the current item using its id. Put the title of the item from mockData into the textfield to edit it.

To trigger this function, follow the same logic for delete to add an event listener, like this:

```js
class Todo {
  constructor() {
    let self = this;

    this.list = document.querySelector('.list-items');
    this.render();

    document
      .querySelector('.btn-add-item')
      .addEventListener('click', this.create.bind(this));

    document.addEventListener('click', (event) => {
      if (event.target.classList.contains('btn-delete')) {
        self.remove(event);
      }
      // step to add click event to show edit form
      if (event.target.classList.contains('btn-edit')) {
        self.renderEditForm(event);
      }
    });
  }

  renderEditForm(event) {
    let id = event.target.getAttribute('data-id');

    document.querySelector('.edit-popup').classList.remove('hide');
    document.querySelector('.edit-popup').classList.add('show');
    document.querySelector('.btn-update').setAttribute('data-id', id);

    mockData.forEach((item) => {
      if (item.id === id) {
        document.querySelector('.edit-item').value = item.title;
      }
    });
  }

  render() {
    this.list.innerHTML = '';

    mockData.forEach((item) => {
      this.createDomElements(item.id);
      this.li.insertAdjacentHTML('afterbegin', item.title);

      if (item.done) {
        this.li.classList.add('done');
      }

      this.list.appendChild(this.li);
    });
  }

  createDomElements(id) {
    this.li = document.createElement('li');
    this.edit = document.createElement('button');
    this.delete = document.createElement('button');
    this.complete = document.createElement('button');

    this.edit.classList.add('btn-edit');
    this.delete.classList.add('btn-delete');
    this.complete.classList.add('btn-complete');

    this.delete.setAttribute('data-id', id);
    this.edit.setAttribute('data-id', id);
    this.complete.setAttribute('data-id', id);

    this.edit.innerHTML = 'Edit';
    this.delete.innerHTML = 'Delete';
    this.complete.innerHTML = 'Complete';

    this.li.appendChild(this.delete);
    this.li.appendChild(this.edit);
    this.li.appendChild(this.complete);
  }

  create() {
    let todoItem = document.querySelector('.item').value;

    let newItem = {
      id: Date.now().toString(),
      title: todoItem,
      done: false,
      date: new Date(),
    };

    mockData.push(newItem);

    document.querySelector('.item').value = '';
    this.render();
  }

  remove(event) {
    let id = event.target.getAttribute('data-id');

    mockData = mockData.filter((item) => {
      if (item.id !== id) {
        return item;
      }
    });

    this.render();
  }
}

export default Todo;

```

Now it’s time to write the update operation. Follow the code below:

```js
class Todo {
  constructor() {
    let self = this;

    this.list = document.querySelector('.list-items');
    this.render();

    document
      .querySelector('.btn-add-item')
      .addEventListener('click', this.create.bind(this));

    document.addEventListener('click', (event) => {
      if (event.target.classList.contains('btn-delete')) {
        self.remove(event);
      }

      if (event.target.classList.contains('btn-edit')) {
        self.renderEditForm(event);
      }
    });
  }

  renderEditForm(event) {
    let id = event.target.getAttribute('data-id');

    document.querySelector('.edit-popup').classList.remove('hide');
    document.querySelector('.edit-popup').classList.add('show');
    document.querySelector('.btn-update').setAttribute('data-id', id);

    mockData.forEach((item) => {
      if (item.id === id) {
        document.querySelector('.edit-item').value = item.title;
      }
    });
  }

  render() {
    this.list.innerHTML = '';

    mockData.forEach((item) => {
      this.createDomElements(item.id);
      this.li.insertAdjacentHTML('afterbegin', item.title);

      if (item.done) {
        this.li.classList.add('done');
      }

      this.list.appendChild(this.li);
    });
  }

  createDomElements(id) {
    this.li = document.createElement('li');
    this.edit = document.createElement('button');
    this.delete = document.createElement('button');
    this.complete = document.createElement('button');

    this.edit.classList.add('btn-edit');
    this.delete.classList.add('btn-delete');
    this.complete.classList.add('btn-complete');

    this.delete.setAttribute('data-id', id);
    this.edit.setAttribute('data-id', id);
    this.complete.setAttribute('data-id', id);

    this.edit.innerHTML = 'Edit';
    this.delete.innerHTML = 'Delete';
    this.complete.innerHTML = 'Complete';

    this.li.appendChild(this.delete);
    this.li.appendChild(this.edit);
    this.li.appendChild(this.complete);
  }

  create() {
    let todoItem = document.querySelector('.item').value;

    let newItem = {
      id: Date.now().toString(),
      title: todoItem,
      done: false,
      date: new Date(),
    };

    mockData.push(newItem);

    document.querySelector('.item').value = '';
    this.render();
  }

  remove(event) {
    let id = event.target.getAttribute('data-id');

    mockData = mockData.filter((item) => {
      if (item.id !== id) {
        return item;
      }
    });

    this.render();
  }

  // step to update item
  update(event) {
    let id = event.target.getAttribute('data-id');
    let itemTobeUpdated = document.querySelector('.edit-item').value;

    mockData = mockData.map((item) => {
      if (item.id === id) {
        item['title'] = itemTobeUpdated;
      }

      return item;
    });

    document.querySelector('.edit-popup').classList.remove('show');
    document.querySelector('.edit-popup').classList.add('hide');

    this.render();
  }
}

export default Todo;

```

The first 2 lines of this function are to get the id of the item and value from the text field and put them in their respective variables. Then map through `mockData`, and place a check to find the item that needs to be updated based on the id. Once that item is found, replace the title with a new `itemTobeUpdate` title. Finally `return` that updated item from the map.

Once that operation is done, hide the edit-popup form by adding and removing the respective CSS classes. Then re-render `mockData` by calling the render function.

To trigger this function, add the code below to the constructor:

```js
class Todo {

  constructor() {
    let self = this;

    this.list = document.querySelector('.list-items');
    this.render();

    document.querySelector('.btn-add-item').addEventListener('click', this.create.bind(this));
    // step to add event listener to update item.
    document.querySelector('.btn-update').addEventListener('click', this.update.bind(this));

    document.addEventListener('click', event => {
      if (event.target.classList.contains('btn-delete')) {
        self.remove(event);
      }
      
      if (event.target.classList.contains('btn-edit')) {
        self.renderEditForm(event);
      }
    });
  }
  
  renderEditForm(event) {
    let id = event.target.getAttribute('data-id');

    document.querySelector('.edit-popup').classList.remove('hide');
    document.querySelector('.edit-popup').classList.add('show');
    document.querySelector('.btn-update').setAttribute('data-id', id);

    mockData.forEach(item => {
      if (item.id === id) {
        document.querySelector('.edit-item').value = item.title;
      }
    });
  }

  render() {
    this.list.innerHTML = '';

    mockData.forEach(item => {
      this.createDomElements(item.id);
      this.li.insertAdjacentHTML('afterbegin', item.title);

      if (item.done) {
        this.li.classList.add('done');
      }

      this.list.appendChild(this.li);
    });
  }

  createDomElements(id) {
    this.li = document.createElement('li');
    this.edit = document.createElement('button');
    this.delete = document.createElement('button');
    this.complete = document.createElement('button');

    this.edit.classList.add('btn-edit');
    this.delete.classList.add('btn-delete');
    this.complete.classList.add('btn-complete');

    this.delete.setAttribute('data-id', id);
    this.edit.setAttribute('data-id', id);
    this.complete.setAttribute('data-id', id);

    this.edit.innerHTML = 'Edit';
    this.delete.innerHTML = 'Delete';
    this.complete.innerHTML = 'Complete';

    this.li.appendChild(this.delete);
    this.li.appendChild(this.edit);
    this.li.appendChild(this.complete);
  }

  create() {
    let todoItem = document.querySelector('.item').value;

    let newItem = {
      id: Date.now().toString(),
      title: todoItem,
      done: false,
      date: new Date()
    };

    mockData.push(newItem);

    document.querySelector('.item').value = '';
    this.render();
  }

  remove(event) {
    let id = event.target.getAttribute('data-id');

    mockData = mockData.filter(item => {
      if (item.id !== id) {
        return item;
      }
    });

    this.render();
  }
  
  update(event) {
    let id = event.target.getAttribute('data-id');
    let itemTobeUpdated = document.querySelector('.edit-item').value;

    mockData = mockData.map(item => {
      if (item.id === id) {
        item['title'] = itemTobeUpdated;
      }

      return item;
    });

    document.querySelector('.edit-popup').classList.remove('show');
    document.querySelector('.edit-popup').classList.add('hide');

    this.render();
  }
}

export default Todo;
```

Now all CRUD operations have been completed. There is one last step which is not part of CRUD but is part of the Todo app. That is to mark items as completed. The function below will achieve this:

```js
class Todo {
  constructor() {
    let self = this;

    this.list = document.querySelector('.list-items');
    this.render();

    document
      .querySelector('.btn-add-item')
      .addEventListener('click', this.create.bind(this));
    document
      .querySelector('.btn-update')
      .addEventListener('click', this.update.bind(this));

    document.addEventListener('click', (event) => {
      if (event.target.classList.contains('btn-delete')) {
        self.remove(event);
      }

      if (event.target.classList.contains('btn-edit')) {
        self.renderEditForm(event);
      }
    });
  }

  renderEditForm(event) {
    let id = event.target.getAttribute('data-id');

    document.querySelector('.edit-popup').classList.remove('hide');
    document.querySelector('.edit-popup').classList.add('show');
    document.querySelector('.btn-update').setAttribute('data-id', id);

    mockData.forEach((item) => {
      if (item.id === id) {
        document.querySelector('.edit-item').value = item.title;
      }
    });
  }

  render() {
    this.list.innerHTML = '';

    mockData.forEach((item) => {
      this.createDomElements(item.id);
      this.li.insertAdjacentHTML('afterbegin', item.title);

      if (item.done) {
        this.li.classList.add('done');
      }

      this.list.appendChild(this.li);
    });
  }

  createDomElements(id) {
    this.li = document.createElement('li');
    this.edit = document.createElement('button');
    this.delete = document.createElement('button');
    this.complete = document.createElement('button');

    this.edit.classList.add('btn-edit');
    this.delete.classList.add('btn-delete');
    this.complete.classList.add('btn-complete');

    this.delete.setAttribute('data-id', id);
    this.edit.setAttribute('data-id', id);
    this.complete.setAttribute('data-id', id);

    this.edit.innerHTML = 'Edit';
    this.delete.innerHTML = 'Delete';
    this.complete.innerHTML = 'Complete';

    this.li.appendChild(this.delete);
    this.li.appendChild(this.edit);
    this.li.appendChild(this.complete);
  }

  create() {
    let todoItem = document.querySelector('.item').value;

    let newItem = {
      id: Date.now().toString(),
      title: todoItem,
      done: false,
      date: new Date(),
    };

    mockData.push(newItem);

    document.querySelector('.item').value = '';
    this.render();
  }

  remove(event) {
    let id = event.target.getAttribute('data-id');

    mockData = mockData.filter((item) => {
      if (item.id !== id) {
        return item;
      }
    });

    this.render();
  }

  update(event) {
    let id = event.target.getAttribute('data-id');
    let itemTobeUpdated = document.querySelector('.edit-item').value;

    mockData = mockData.map((item) => {
      if (item.id === id) {
        item['title'] = itemTobeUpdated;
      }

      return item;
    });

    document.querySelector('.edit-popup').classList.remove('show');
    document.querySelector('.edit-popup').classList.add('hide');

    this.render();
  }

  // step to set task as complete
  setTaskComplete(event) {
    let id = event.target.getAttribute('data-id');

    mockData = mockData.map((item) => {
      if (item.id === id) {
        item['done'] = true;
      }

      return item;
    });

    this.render();
  }
}

export default Todo;

```

Again, follow the same pattern as the rest of the functions:

* get the id from the button’s `data-id` attribute
* map through `mockData` and find the relevant item and set its `done` property to `true` and `return` that item
* finally, re-render `mockData` by calling the `render` function.

Again, use the same logic to trigger the `delete` function, and add the code below to the constructor to set tasks as completed:

```js
class Todo {
  constructor() {
    let self = this;

    this.list = document.querySelector('.list-items');
    this.render();

    document
      .querySelector('.btn-add-item')
      .addEventListener('click', this.create.bind(this));
    document
      .querySelector('.btn-update')
      .addEventListener('click', this.update.bind(this));

    document.addEventListener('click', (event) => {
      if (event.target.classList.contains('btn-delete')) {
        self.remove(event);
      }

      if (event.target.classList.contains('btn-edit')) {
        self.renderEditForm(event);
      }
      // step to add event listener to complete button
      if (event.target.classList.contains('btn-complete')) {
        self.setTaskComplete(event);
      }
    });
  }

  renderEditForm(event) {
    let id = event.target.getAttribute('data-id');

    document.querySelector('.edit-popup').classList.remove('hide');
    document.querySelector('.edit-popup').classList.add('show');
    document.querySelector('.btn-update').setAttribute('data-id', id);

    mockData.forEach((item) => {
      if (item.id === id) {
        document.querySelector('.edit-item').value = item.title;
      }
    });
  }

  render() {
    this.list.innerHTML = '';

    mockData.forEach((item) => {
      this.createDomElements(item.id);
      this.li.insertAdjacentHTML('afterbegin', item.title);

      if (item.done) {
        this.li.classList.add('done');
      }

      this.list.appendChild(this.li);
    });
  }

  createDomElements(id) {
    this.li = document.createElement('li');
    this.edit = document.createElement('button');
    this.delete = document.createElement('button');
    this.complete = document.createElement('button');

    this.edit.classList.add('btn-edit');
    this.delete.classList.add('btn-delete');
    this.complete.classList.add('btn-complete');

    this.delete.setAttribute('data-id', id);
    this.edit.setAttribute('data-id', id);
    this.complete.setAttribute('data-id', id);

    this.edit.innerHTML = 'Edit';
    this.delete.innerHTML = 'Delete';
    this.complete.innerHTML = 'Complete';

    this.li.appendChild(this.delete);
    this.li.appendChild(this.edit);
    this.li.appendChild(this.complete);
  }

  create() {
    let todoItem = document.querySelector('.item').value;

    let newItem = {
      id: Date.now().toString(),
      title: todoItem,
      done: false,
      date: new Date(),
    };

    mockData.push(newItem);

    document.querySelector('.item').value = '';
    this.render();
  }

  remove(event) {
    let id = event.target.getAttribute('data-id');

    mockData = mockData.filter((item) => {
      if (item.id !== id) {
        return item;
      }
    });

    this.render();
  }

  update(event) {
    let id = event.target.getAttribute('data-id');
    let itemTobeUpdated = document.querySelector('.edit-item').value;

    mockData = mockData.map((item) => {
      if (item.id === id) {
        item['title'] = itemTobeUpdated;
      }

      return item;
    });

    document.querySelector('.edit-popup').classList.remove('show');
    document.querySelector('.edit-popup').classList.add('hide');

    this.render();
  }

  setTaskComplete(event) {
    let id = event.target.getAttribute('data-id');

    mockData = mockData.map((item) => {
      if (item.id === id) {
        item['done'] = true;
      }

      return item;
    });

    this.render();
  }
}

export default Todo;

```

Here is some basic CSS that I used for this tutorial — nothing fancy:

```css
.show {
  display: block;
}

.hide {
  display: none;
}

.done {
  text-decoration: line-through;
}

```

That is it for vanilla JavaScript CRUD operations! The next step is to covert this into an Angular and React app to see the difference and find out how convenient such frameworks are.

To get the code and the complete project, clone the repository below:

[https://github.com/zafar-saleem/todo](https://github.com/zafar-saleem/todo)

