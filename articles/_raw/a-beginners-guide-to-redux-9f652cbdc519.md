---
title: A beginner’s guide to Redux
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-27T16:35:18.000Z'
originalURL: https://freecodecamp.org/news/a-beginners-guide-to-redux-9f652cbdc519
coverImage: https://cdn-media-1.freecodecamp.org/images/1*BpaqVMW2RjQAg9cFHcX1pw.png
tags:
- name: beginner
  slug: beginner
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: Redux
  slug: redux
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Safeer Hayat

  Understanding Redux as a beginner can be quite confusing. Redux has an abundance
  of new terms and concepts which are often pretty unintuitive. This guide presents
  a very simplified example of a Redux implementation. I will define each...'
---

By Safeer Hayat

Understanding Redux as a beginner can be quite confusing. Redux has an abundance of new terms and concepts which are often pretty unintuitive. This guide presents a very simplified example of a Redux implementation. I will define each of the steps and terms in a way that makes sense to a complete beginner.

This is intended to be a guide to demystify Redux elements. It does not contain the most technically accurate definitions. It does not have the best ever practices. It does have definitions that will help develop an understanding for someone with no prior knowledge of these concepts. There is a simple implementation as to not confuse with unnecessary details.

The example we will run through in this guide will be a simple todo app. The app allows a user to add or remove todo items and see them displayed on the page.

I will run through step by step each element of Redux, explaining what that element is and how to implement it with code examples. Scroll to the bottom to see the full code example which will show how it all fits together as a complete React app.

### Steps Summary

1. Write the reducer function
2. Instantiate the store in the root component
3. Wrap the components with the <Provider> component, passing in the store as a prop
4. Write the component
5. Define the actions
6. Define the dispatch, attach these to where the dispatches will be triggered (ie event listeners etc)
7. Define the mapStateToProps function
8. Export the connect function, passing in mapStateToProps and null as the 2 arguments and passing the component name in the second pair of brackets

### Steps

#### 1. Write the reducer function

The reducer function is a function which tells the store how to respond to actions. The function returns the new and updated state whenever an action is dispatched. State is immutable (can’t be changed) so the reducer always returns a new state. The reducer usually uses the spread operator to insert the current state into a new object/array and appending to it. Common practice is to use a switch/case statement and check the type property of the action passed in. Then write the code that updates the state for each case.

We write our reducer function first because we will need to pass this when we instantiate our store. To understand what’s happening though requires some knowledge of actions and dispatch. We will cover this further on in this guide.

For now know that our todo app will need to interact with the store in 2 ways: to add a new todo item to the state and to remove a todo item from the state. Therefore we write our function so that it responds to 2 cases of the action type. It uses the action value to either add or remove a todo item from the state.

The reducer is passed 2 parameters: state (this is the entire state currently in the store, and we give it a default value if state does not exist yet) and the action. We return the state in the default case.

![Image](https://cdn-media-1.freecodecamp.org/images/1*_HcMGsHCcl89CIbW5vBvxw.png)
_Reducer function with 2 cases_

#### 2. Instantiate the store in the root component

The store is the thing which actually contains the state in it. It’s a bit magical and you don’t really need to know the ins and outs of it. All you need to know is that you don’t access it directly like you would a normal React state. You access it and make changes to it using reducers, actions and dispatch.

The other important thing to know about the store is that it contains some useful and important methods. The main method is the dispatch function. It also contains a getState method (for viewing the state) and subscribe method (runs a callback every time an action is dispatched).

The store is typically instantiated at the root of your app (e.g. App.js). It is stored as a variable and has the reducer passed in as a parameter. The store is then passed in as a prop to the Provider component.

We instantiate our store object passing in the reducer we just created.

![Image](https://cdn-media-1.freecodecamp.org/images/1*z9nl7lgc1dTcLozE6HGjFA.png)
_Store instantiated with reducer we created in the previous step_

#### 3. Wrap the components with the <Provider> component, passing in the store as a prop

The Provider is a component created to make it easier to pass the store to all your components. The Provider component wraps around all your components (e.g. render your components as children of Provider). You pass the store in as a prop to the Provider only. This means you don’t need to pass in the store as a prop to every component as each component gets it from the Provider. However, this doesn’t mean the components have access to the state yet. You still need to use the mapStateToProps (we will cover this later) to have the state accessible in your component.

We wrap the Todo component we are going to make with our Provider component. We pass in the store we created in the previous step.

![Image](https://cdn-media-1.freecodecamp.org/images/1*oc_ahULWaWmVo5l0SdmlAg.png)
_Components are wrapped with the Provider component with the store passed in_

#### 4. Write the component

Next, we begin to write the Todo component which will render the todo items and interact with the Redux store.

The component is a stateful component containing one state element to keep track of what the user has typed into the input. We have a function called handleChange. This function updates the state every time the user types anything into the input. So far this is all we will write. We need to understand more about Redux before we can write the logic. The logic will add new todos to the state and retrieve current ones from the state to render on the page.

![Image](https://cdn-media-1.freecodecamp.org/images/1*QQYkjyrBinJy7Jiq4WjwLg.png)
_The beginning of the Todo component which allows a user to input new todo items_

#### 5. Define the actions

An action is a simple object containing a property called ‘type’. This object is passed into the dispatch function. It is used to tell the store what event has just occurred (by reading the actions type property). It also tells what update it should make to the state in response (through the reducer function). The action can also contain other properties for any other data you want to pass into the reducer. Data can only be passed through here so any data needed will need to be passed in here.

We will use action creators to define our actions. Action creators are a function which returns the action object. Its purpose is to make the action more portable and testable. It doesn’t change the behavior of how anything works. It’s another method of writing and passing the action. It also allows you to pass in parameters if you want to send data with the action which we will be doing. So we require to use action creators here.

If you remember our reducer responded to 2 action types — “ADD_TODO” and “REMOVE_TODO”. We will define those actions with our action creators. In our add_todo action will return “ADD_TODO” as the type and the todo item we want to add to the store as the value (we need the store to add this todo item to the state so it gets passed in here). In the remove_todo we return “REMOVE_TODO” as the type and the index of the todo item in the store as the value. We’ll need this to remove it from the list of todos.

![Image](https://cdn-media-1.freecodecamp.org/images/1*nTgkcNwagEXQUytjG6-Bdg.png)
_We define our 2 actions here in action creators. These are what our reducer reads when it is triggered to update the state._

If you return to our reducer function definition hopefully it now makes more sense. By reading the action.type the reducer knows whether it needs to add a todo to the state or remove one from it. It has the todo item passed in the add_todo. It appends to the current state using the spread operator. In the remove_todo it uses the spread operator to create a new array appending the current state sliced twice, once with all the elements before the one to remove and second with all the elements after the one to remove, thus creating our new state object with the todo item removed.

![Image](https://cdn-media-1.freecodecamp.org/images/1*_HcMGsHCcl89CIbW5vBvxw.png)
_The reducer function that we defined earlier on_

However, this still isn’t a complete picture. We have not yet covered how the reducer gets called and passed in the right action. For that, we will need to move on to define our dispatch function.

#### 6. Define the dispatch, attach these to where the dispatches will be triggered (ie event listeners etc)

The dispatch function is a method of the store which is used to trigger a change in the state. Any event or anything which needs to update the state must call the dispatch method to do so. This is the only way to trigger a change/update to the state. Dispatch is called and the action object is passed in (or the action creator if that was used). Once a dispatch is triggered the store then calls the reducer function and passes in the action that the dispatch provided which updates the state, as we’ve seen earlier.

Below we define the bottom half of our Components render method. We create our buttons which will contain our event handlers. Inside those, we will define our dispatch functions.

The first button is a simple add button. This button will dispatch the add_todo action to the store. It will pass in the current user input as the value (this is the todo item that the reducer appends to the new state). Note we call dispatch as `this.props.dispatch`. It’s a bit out of the scope of this guide to understand how and why this gets passed as a prop to the component. So just know that it does and we can call it like this.

The second event handler is written as an onClick on our rendered todo item. By clicking on any todo item on the page it triggers an event handler. The event handler searches the list of todos and finds the index of that todo in the list. It then dispatches the remove_todo action and passes in the index.

![Image](https://cdn-media-1.freecodecamp.org/images/1*5kkjqmwSjk5tbTs3mWKz0Q.png)
_The bottom half of our component definition including our event handlers which call the dispatch function_

The cycle for how to update the state in the Redux store is now fully defined. We know that any time we want to change the state we need to call the dispatch method, pass in the appropriate action, and ensure our reducer handles those actions and returns the new state using any values we passed in via the action.

The only puzzle piece missing now is how do we get the state from the Redux store. You’ve probably noticed that I’ve mapped over a list called `this.props.todos` in the previous example. You may be wondering where that came from. You may also recall at the beginning of this guide I mentioned that passing store into the Provider component is not enough to gain access to the state in the store. This is all addressed in the next 2 steps as we define our mapStateToProps function and pass that into the connect function.

#### 7. Define the mapStateToProps function

When you want your component to have access to the state you have to explicitly specify what in the state the component will get access to. Your component will not have access to state without this.

mapStateToProps is a function which simply returns an object that defines what state should be passed into the component by assigning values in the state to properties you define in this object. Essentially, the object you return in the mapStateToProps is what your props will be in your component. The mapStateToProps function is passed into the connect method as the first argument.

The mapStateToProps takes the entire state as a parameter and you take only what you need from it. Here though as our state only contains the list of todos. We need that list in our ToDo component, we will return the entire state as a property called todos.

![Image](https://cdn-media-1.freecodecamp.org/images/1*EI0ei8et6carOyDGwKzMew.png)
_Our mapStateToProps definition which simply assigns the entire state to a prop called todos_

As you can see now, we have access to our entire todos list in our props as `this.props.todos`. This is how we were able to render all our todos in the previous example by mapping over it.

Finally we need to pass this function into our connect method to connect everything together.

#### 8. Export the connect function, passing in mapStateToProps and null as the 2 arguments and passing the component name in the second pair of brackets

Connect is a method that hooks up mapStateToProps and mapDispatchToProps (see below) functions to your component so that the store can read those functions and ensure what you defined in there gets passed into the component as props. This method has a special syntax which looks like this:

`connect(mapStateToProps, MapDispatchToProps)(YourComponent)`

You pass in the 2 `map...ToProps` functions to the connect and then the name of your component inside the second pair of brackets. A typical pattern is to export the connect method instead of your component when you are exporting your component at the end of your file. For example:

`export default connect(mapStateToProps, MapDispatchToProps)(YourComponent)`

This then acts in the same way as exporting normally except the state and dispatches will be passed in as props. mapStateToProps and mapDispatchToProps are actually optional params to connect. If you don’t want to pass one or either, put null in their place instead.

You may be wondering where this mapDispatchToProps function has come from and why we haven’t mentioned it anywhere before here. Well, as this guide is the most simplified example of a Redux store and mapDispatchToProps isn’t strictly mandatory, I haven’t included it in our example. If you don’t pass mapDispatchToProps and pass null instead then you can still access the dispatch function in your component as we have earlier as `this.props.dispatch`.

So to finish off our example app, all we have to do is export our component wrapping it with the connect function and passing in the mapStateToProps we just defined.

![Image](https://cdn-media-1.freecodecamp.org/images/1*gfbjcvHkDGt1J5jN2zV9eQ.png)
_We export our component by wrapping it with the connect method and passing in our mapStateToProps function_

And that’s it! That’s a complete implementation of a Redux store. See below for the working example of what we implemented.

### Full Annotated Code Example

> **App.js**

![Image](https://cdn-media-1.freecodecamp.org/images/1*8Jn_9Tix-ErbBeCGaJSsGQ.png)
_Full code for the App.js file_

> **Todo.js**

![Image](https://cdn-media-1.freecodecamp.org/images/1*-cjCZtjQ4o_GYdd93fgxFw.png)
_Full code for the Todo.js file_

I hope that this guide can simplify some of the strange and sometimes confusing details of Redux. It’s not a complete guide of Redux, as there are definitely more elements and patterns to understand. But if you can understand this guide then you are well on your way to being able to work with and install Redux in your apps.

