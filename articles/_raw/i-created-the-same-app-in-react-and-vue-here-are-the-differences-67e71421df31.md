---
title: I created the same app in React and Vue. Here are the differences.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-27T17:09:58.000Z'
originalURL: https://freecodecamp.org/news/i-created-the-same-app-in-react-and-vue-here-are-the-differences-67e71421df31
coverImage: https://cdn-media-1.freecodecamp.org/images/1*mJ-qdNqldpgae2U5oS0qDg.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: Vue.js
  slug: vuejs
seo_title: null
seo_desc: 'By Sunil Sandhu

  Having used Vue at my current workplace, I had a fairly solid understanding of how
  it all worked. I was, however, curious to know what the grass was like on the other
  side of the fence — the grass in this scenario being React.

  I’d rea...'
---

By Sunil Sandhu

Having used **Vue** at my current workplace, I had a fairly solid understanding of how it all worked. I was, however, curious to know what the grass was like on the other side of the fence — the grass in this scenario being React.

I’d read the React docs and watched a few tutorial videos and, while they were great and all, what I really wanted to know was how different **React** was from **Vue**.

By “different”, I didn’t mean things such as whether they both had **virtual DOMS** or how they went about rendering pages. I wanted someone to take the time to explain the code and to tell me what was going on! I wanted to find an article that took the time to explain these differences so that someone new to either **Vue** or **React** (or Web Development as a whole) could gain a better understanding of the differences between the two.

But I couldn’t find anything that tackled this. So I came to the realisation that I’d have to go ahead and build this myself in order to see the similarities and differences. In doing so, I thought I’d document the whole process so that an article on this would finally exist.

![Image](https://cdn-media-1.freecodecamp.org/images/gxU7ZAu4Ey12iGnSlpGwYH6i83ncsHcmIEDj)
_Who wore it better?_

I decided to try and build a fairly standard To Do App that allows a user to add and delete items from the list. Both apps were built using the default **CLIs** (**create-react-app** for **React**, and **vue-cli** for **Vue**). _CLI stands for Command Line Interface by the way_. ?

#### Anyway, this intro is already longer than I’d anticipated. So let’s start by having a quick look at how the two apps look:

![Image](https://cdn-media-1.freecodecamp.org/images/V9NdEyLFZvFCGDQ731P892-lTF3lcXP9laP1)
_Vue vs React: The Irresistible Force meets The Immovable Object_

The CSS code for both apps is exactly the same, but there are differences in where these are located. With that in mind, let’s next have a look at the file structure of both apps:

![Image](https://cdn-media-1.freecodecamp.org/images/GV3G8hb9X8mA-vnRcfRpboA59nVO46ZTIknR)
_Who wore it better?_

You’ll see that their structures are almost identical as well. The only difference here is that the React app has three CSS files, whereas the Vue app doesn’t have any. This is because, in create-react-app, **a React component will have an accompanying file to hold its styles, whereas the Vue CLI adopts an all-encompassing approach where the styles are declared inside the actual component file**.

Ultimately, they both achieve the same thing, and there is nothing to say that you can’t go ahead and structure your CSS differently in React or Vue. It really comes down to personal preference — you’ll hear plenty of discussion from the dev community over how CSS should be structured. For now, we’ll just follow the structure laid out in both CLIs.

But before we go any further, let’s take a quick look at what a typical Vue component and React component look like:

![Image](https://cdn-media-1.freecodecamp.org/images/OYJ9J1mD7ENdqSy0d66zRGSRivznwiHyi1HH)
_Vue on the left. React on the right_

Now that’s out of the way, let’s get into the nitty gritty detail!

### How do we mutate data?

But first, what do we even mean by “mutate data”? Sounds a bit technical, doesn’t it? It basically just means changing the data that we have stored. So if we wanted to change the value of a person’s name from John to Mark, we would be ‘mutating the data’.

This is where a key difference between React and Vue lies. **While Vue essentially creates a data object, where data can freely be updated, React creates a state object, where a little more legwork is required to carry out updates**.

Now React implements the extra legwork with good reason, and we’ll get into that in a little bit. But first, let’s take a look at the **data** object from Vue and the **state** object from React:

![Image](https://cdn-media-1.freecodecamp.org/images/sZzmUCmi9Frf20OgPlXeFxeYutk5nVpYLyIo)

![Image](https://cdn-media-1.freecodecamp.org/images/pMzlry1q9FfWOoMj6TnLJoRBmfobAzf3MIuE)
_Vue data object on the left. React state object on the right._

So you can see that we have passed the same data into both, but they’re simply labelled differently. So passing initial data into our components is very, very similar. But as we’ve mentioned, how we go about changing this data differs between the frameworks.

Let’s say that we have a data element called `**name: ‘Sunil’**`.

In Vue, we reference this by calling `this.name`. We can also go about updating this by calling `**this.name** **= ‘John’**`. This would change my name to John. I’m not sure how I feel about being called John, but hey ho, things happen! ?

In React, we would reference the same piece of data by calling `**this.state.name**`. Now the key difference here is that we cannot simply write `**this.state.name** = ‘John’`, because React has restrictions in place to prevent this kind of easy, care-free mutation-making. So in React, we would write something along the lines of `**this.setState({name: ‘John’})**`.

While this essentially does the same thing as we achieved in Vue, the extra bit of writing is there because Vue essentially combines its own version of setState by default whenever a piece of data gets updated.

So in short, **React requires setState and then the updated data inside of it, whereas Vue makes an assumption that you’d want to do this if you were updating values inside the data object**.

Why does React even bother with this, and why is setState even needed? Let’s hand this over to [Revanth Kumar](https://medium.com/@revanth0212) for an explanation:

> “This is because React wants to re-run certain life cycle hooks, [such as] componentWillReceiveProps, shouldComponentUpdate, componentWillUpdate, render, componentDidUpdate, whenever state changes. It would know that the state has changed when you call the setState function. If you directly mutated state, React would have to do a lot more work to keep track of changes and what lifecycle hooks to run etc. So to make it simple React uses setState.”

![Image](https://cdn-media-1.freecodecamp.org/images/BjPx0SKGGAUNqBoLjDJRUwtctgPimca0DtjG)
_Bean knew best_

Now that we have mutations out of the way, let’s get into the nitty gritty by looking at how we would go about adding new items to both of our To Do Apps.

### How do we create new To Do Items?

#### React:

```jsx
createNewToDoItem = () => {
    this.setState( ({ list, todo }) => ({
      list: [
          ...list,
        {
          todo
        }
      ],
      todo: ''
    })
  );
};
```

#### How did React do that?

In React, our input field has a attribute on it called **value.** This value gets automatically updated through the use of a couple of functions that tie together to create something that closely resembles **two-way binding** (if you’ve never heard of this before, there’s a more detailed explanation in the _How did Vue do that_ section after this). We create this form of two-way binding by having an additional **onChange event listener** attached to the **input** field.

Let’s quickly take a look at the **input** field so that you can see what is going on:

```jsx
<input type="text" 
       value={this.state.todo} 
       onChange={this.handleInput}/>
```

The handleInput function is run whenever the value of the input field changes. It updates the **todo** that sits inside the state object by setting it to whatever is in the input field. This function looks as such:

```jsx
handleInput = e => {
  this.setState({
    todo: e.target.value
  });
};
```

Now, whenever a user presses the **+** button on the page to add a new item, the `**createNewToDoItem**` function essentially runs this.setState and passes it a function.

This function takes two parameters, the first being the entire `**list**` array from the state object, the second being the `**todo**` (which gets updated by the `**handleInput**` function). The function then returns a new object, which contains the entire `**list**` from before and then adds `**todo**` at the end of it. The entire list is added through the use of a spread operator (Google this if you’ve not seen this before — it’s ES6 syntax).

Finally, we set `**todo**` to an empty string, which automatically updates the **value** inside the **input** field.

#### Vue:

```js
createNewToDoItem() {
    this.list.push(
        {
            'todo': this.todo
        }
    );
    this.todo = '';
}
```

#### How did Vue do that?

In Vue, our **input** field has a handle on it called **v-model**. This allows us to do something known as **two-way binding**. Let’s just quickly look at our input field, then we’ll explain what is going on:

```js
<input type="text" v-model="todo"/>
```

V-Model ties the input of this field to a key we have in our data object called toDoItem. When the page loads, we have `**toDoItem**` set to an empty string, as such: `**todo: ‘’**`. If this had some data already in there, such as `**todo: ‘add some text here’**`, our input field would load with _add some text here_ already inside the input field.

Anyway, going back to having it as an empty string, whatever text we type inside the input field gets bound to the value for `**todo**`. This is effectively two-way binding (the input field can update the data object and the data object can update the input field).

So looking back at the `**createNewToDoItem()**` code block from earlier, we see that we push the contents of `**todo**` into the `**list**` array and then update `**todo**` to an empty string.

### How do we delete from the list?

#### React:

```jsx
deleteItem = indexToDelete => {
    this.setState(({ list }) => ({
      list: list.filter((toDo, index) => index !== indexToDelete)
    }));
};
```

#### How did React do that?

So whilst the deleteItem function is located inside **ToDo.js**, I was very easily able to make reference to it inside **ToDoItem.js** by firstly passing the `**deleteItem()**` function as a prop on `**<ToDoIte**`m/> as such:

```jsx
<ToDoItem deleteItem={this.deleteItem.bind(this, key)}/>
```

This passes the function down to make it accessible to the child. You’ll see here that we’re also binding `**this**` as well as passing the key parameter, as the key is what the function is going to use to differentiate between which **ToDoItem** we’re attempting to delete when clicked. Then, inside the **ToDoItem** component, we do the following:

```jsx
<div className=”ToDoItem-Delete” onClick={this.props.deleteItem}>-</div>
```

All I had to do to reference a function that sat inside the parent component was to reference `**this.props.deleteItem**`.

#### Vue:

```js
onDeleteItem(todo){
  this.list = this.list.filter(item => item !== todo);
}
```

#### How did Vue do that?

A slightly different approach is required in Vue. We essentially have to do three things here:

Firstly, on the element we want to call the function:

```js
<div class=”ToDoItem-Delete” @click=”deleteItem(todo)”>-</div>
```

Then we have to create an emit function as a method inside the child component (in this case, **ToDoItem.vue**), which looks like this:

```js
deleteItem(todo) {
    this.$emit('delete', todo)
}
```

Along with this, you’ll notice that we actually reference a **function** when we add **ToDoItem.vue** inside of **ToDo.vue**:

```js
<ToDoItem v-for="todo in list" 
          :todo="todo" 
          @delete="onDeleteItem" // <-- this :)
          :key="todo.id" />
```

This is what is known as a **custom event-listener**. It listens out for any occasion where an emit is triggered with the string of `‘delete’`. If it hears this, it triggers a function called `**onDeleteItem**`. This function sits inside of **ToDo.vue,** rather than **ToDoItem.vue**. As we discussed earlier, it simply filters the `**todo**` **array** inside the `**data**` **object** to remove the item that was clicked on.

It’s also worth noting here that in the Vue example, I could have simply written the `**$emit**` part inside of the `**@click**` listener, as such:

```js
<div class=”ToDoItem-Delete” @click=”$emit(‘delete’, todo)”>-</div>
```

This would have reduced the number of steps down from 3 to 2, and this is simply down to personal preference.

In short, **child components in React will have access to parent functions via** `**this.props**` (providing you are passing props down, which is fairly standard practice — you’ll come across this loads of times in other React examples). In Vue, on the other hand, **you have to emit events from the child that will usually be collected inside the parent component**.

### How do we pass event listeners?

#### React:

Event listeners for simple things such as click events are straightforward. Here is an example of how we created a click event for a button that creates a new ToDo item:

```jsx
<div className=”ToDo-Add” onClick={this.createNewToDoItem}>+</div>.
```

Super easy here, and pretty much looks like how we would handle an in-line `onClick` with vanilla JS. As mentioned in the Vue section, it took a little bit longer to set up an event listener to handle whenever the enter button was pressed. This essentially required an `onKeyPress` event to be handled by the input tag, as such:

```jsx
<input type=”text” onKeyPress={this.handleKeyPress}/>.
```

This function essentially triggered the `**createNewToDoItem**` function whenever it recognised that the ‘enter’ key had been pressed, as such:

```
handleKeyPress = (e) => {
  if (e.key === ‘Enter’) {
    this.createNewToDoItem();
  }
};
```

#### Vue:

In Vue it is super straight-forward. We simply use the **@** symbol, and then the type of event-listener we want to do. So for example, to add a click event listener, we could write the following:

```js
<div class=”ToDo-Add” @click=”createNewToDoItem()”>+</div>
```

Note: `**@click**` is actually shorthand for writing `**v-on:click**`. The cool thing with Vue event listeners is that there are also a bunch of things that you can chain on to them, such as `.once`, which prevents the event listener from being triggered more than once. There are also a bunch of shortcuts when it comes to writing specific event listeners for handling key strokes.

I found that it took quite a bit longer to create an event listener in React to create new ToDo items whenever the enter button was pressed. In Vue, I was able to simply write:

```js
<input type=”text” v-on:keyup.enter=”createNewToDoItem”/>
```

#### How do we pass data through to a child component?

#### React:

In React, we pass props onto the child component at the point where it is created. Such as:

```jsx
<ToDoItem key={key} item={todo} />
```

Here we see two props passed to the **ToDoItem** component. From this point on, we can now reference them in the child component via `**this.props**`. So to access the `**item.todo**` prop, we simply call `**this.props.item**`.

#### Vue:

In Vue, we pass props onto the child component at the point where it is created. Such as:

```js
<ToDoItem v-for="todo in list" 
            :todo="todo"
            :key="todo.id"
            @delete="onDeleteItem" />
```

Once this is done, we then pass them into the props array in the child component, as such: `**props: [ ‘todo’ ]**`. These can then be referenced in the child by their name — so in our case, `**‘todo**’`.

### How do we emit data back to a parent component?

#### React:

We firstly pass the function down to the child component by referencing it as a prop in the place where we call the child component. We then add the call to function on the child by whatever means, such as an `**onClick**`, by referencing `**this.props.whateverTheFunctionIsCalled**`. This will then trigger the function that sits in the parent component.

We can see an example of this entire process in the section _‘How do we delete from the list’._

#### Vue:

In our child component, we simply write a function that emits a value back to the parent function. In our parent component, we write a function that listens for when that value is emitted, which can then trigger a function call. We can see an example of this entire process in the section _‘How do we delete from the list’._

### And there we have it! ?

We’ve looked at how we add, remove and change data, pass data in the form of props from parent to child, and send data from the child to the parent in the form of event listeners.

There are, of course, lots of other little differences and quirks between React and Vue, but hopefully the contents of this article has helped to serve as a bit of a foundation for understanding how both frameworks handle stuff ?

If you found this useful, please share on social media and comment!

#### Github links to both apps:

Vue ToDo: [https://github.com/sunil-sandhu/vue-todo](https://github.com/sunil-sandhu/vue-todo)

React ToDo: [https://github.com/sunil-sandhu/react-todo](https://github.com/sunil-sandhu/react-todo)

**This is a syndicated repost for freeCodeCamp in collaboration with [Javascript In Plain English](https://medium.com/javascript-in-plain-english). The original version of this article can be found [here](https://medium.com/javascript-in-plain-english/i-created-the-exact-same-app-in-react-and-vue-here-are-the-differences-e9a1ae8077fd).**

