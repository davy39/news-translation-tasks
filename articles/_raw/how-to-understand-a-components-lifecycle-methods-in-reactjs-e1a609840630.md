---
title: How to understand a component’s lifecycle methods in ReactJS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-18T16:48:15.000Z'
originalURL: https://freecodecamp.org/news/how-to-understand-a-components-lifecycle-methods-in-reactjs-e1a609840630
coverImage: https://cdn-media-1.freecodecamp.org/images/1*_drMYY_IEgboMS4RhvC-lQ.png
tags:
- name: JavaScript
  slug: javascript
- name: lifecycle methods
  slug: lifecycle-methods
- name: General Programming
  slug: programming
- name: React
  slug: reactjs
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Anchal Nigam

  In this article, we are going to explore the lifecycle methods of ReactJS. But,
  before moving ahead to React’s different lifecycle methods, we should understand
  what it is.

  As we know, everything in this world follows a cycle (say hum...'
---

By Anchal Nigam

In this article, we are going to explore the lifecycle methods of ReactJS. But, before moving ahead to React’s different lifecycle methods, we should understand what it is.

As we know, everything in this world follows a cycle (say humans or trees). We are born, grow, and then die. Almost everything follows this cycle in its life, and React components do as well. Components are created (mounted on the DOM), grow by updating, and then die (unmount on DOM). This is referred to as **a component lifecycle.**

There are different lifecycle methods that React provides at different phases of a component’s life. React automatically calls the responsible method according to the phase in which the component is. These methods give us better control over our component and we can manipulate them using these methods.

At present, we know what lifecycle methods are and why they are important. So what are these different methods? Let’s have a look into them.

### Lifecycle Methods

A component’s lifecycle is broadly classified into four parts:

* **initialization**
* **mounting**
* **updating, and**
* **unmounting**.

Let’s discuss the different lifecycle methods that are available at these different phases (i.e., initialization, mounting, updating & unmounting).

#### **Initialization**

This is the phase in which the component is going to start its journey by setting up the state (see below) and the props. This is usually done inside the constructor method (see below to understand the initialization phase better).

```
class Initialize extends React.Component {
    constructor(props)
    {
    // Calling the constructor of
    // Parent Class React.Component
    super(props);
    // initialization process
    this.state = {
       date : new Date(),
       clickedStatus: false
     };
}
```

#### **Mounting**

The name is self-explanatory. Mounting is the phase in which our React component mounts on the DOM (i.e., is created and inserted into the DOM).

This phase comes onto the scene after the initialization phase is completed. In this phase, our component renders the first time. The methods that are available in this phase are:

**1. componentWillMount()**

This method is called just before a component mounts on the DOM or the render method is called. After this method, the component gets mounted.

Note: You should not make API calls or any data changes using this.setstate in this method because it is called before the render method. So, nothing can be done with the DOM (i.e. updating the data with API response) as it has not been mounted. Hence, we can’t update the state with the API response.

**2. componentDidMount()**

This method is called after the component gets mounted on the DOM. Like componentWillMount, it is called once in a lifecycle. Before the execution of this method, the render method is called (i.e., we can access the DOM). We can make API calls and update the state with the API response.

Have a look to understand these mounting methods:

```
class LifeCycle extends React.Component {
  componentWillMount() {
      console.log('Component will mount!')
   }
  componentDidMount() {
      console.log('Component did mount!')
      this.getList();
   }
  getList=()=>{
   /*** method to make api call***
  }
  render() {
      return (
         <div>
            <h3>Hello mounting methods!</h3>
         </div>
      );
   }
}
```

#### **Updating**

This is the third phase through which our component passes. After the mounting phase where the component has been created, the update phase comes into the scene. This is where component’s state changes and hence, re-rendering takes place.

In this phase, the data of the component (state & props) updates in response to user events like clicking, typing and so on. This results in the re-rendering of the component. The methods that are available in this phase are:

1. **shouldComponentUpdate()**

This method determines whether the component should be updated or not. By default, it returns true. But at some point, if you want to re-render the component on some condition, then shouldComponentUpdate method is the right place.

Suppose, for example, you want to only re-render your component when there is a change in prop — then utilize the power of this method. It receives arguments like nextProps and nextState which help us decide whether to re-render by doing a comparison with the current prop value.

**2. componentWillUpdate()**

Like other methods, its name is also self-explanatory. It is called before the re-rendering of the component takes place. It is called once after the ‘**shouldComponentUpdate**’ method. If you want to perform some calculation before re-rendering of the component and after updating the state and prop, then this is the best place to do it. Like the ‘shouldComponentUpdate’ method, it also receives arguments like nextProps and nextState.

**3. ComponentDidUpdate()**

This method is called just after the re-rendering of the component. After the new (updated) component gets updated on the DOM, the ‘**componentDidUpdate**’ method is executed. This method receives arguments like prevProps and prevState.

Have a look to understand the updating methods better:

```
class LifeCycle extends React.Component {
      constructor(props)
      {
        super(props);
         this.state = {
           date : new Date(),
           clickedStatus: false,
           list:[]
         };
      }
      componentWillMount() {
          console.log('Component will mount!')
       }
      componentDidMount() {
          console.log('Component did mount!')
          this.getList();
       }
      getList=()=>{
       /*** method to make api call***
       fetch('https://api.mydomain.com')
          .then(response => response.json())
          .then(data => this.setState({ list:data }));
      }
       shouldComponentUpdate(nextProps, nextState){
         return this.state.list!==nextState.list
        }
       componentWillUpdate(nextProps, nextState) {
          console.log('Component will update!');
       }
       componentDidUpdate(prevProps, prevState) {
          console.log('Component did update!')
       }
      render() {
          return (
             <div>
                <h3>Hello Mounting Lifecycle Methods!</h3>
             </div>
          );
       }
}
```

#### **Unmounting**

This is the last phase in the component’s lifecycle. As the name clearly suggests, the component gets unmounted from the DOM in this phase. The method that is available in this phase is:

**1. componentWillUnmount()**

This method is called before the unmounting of the component takes place. Before the removal of the component from the DOM, ‘**componentWillUnMount’** executes. This method denotes the end of the component’s lifecycle.

Here is a flowchart representation of lifecycle methods:

![Image](https://cdn-media-1.freecodecamp.org/images/NpWCjYyzfnJkn7rXwDmyWwK2DqInFJu6-g1O)

That’s all about this important part of the React world — lifecycle methods. I hope you enjoyed reading it.

Thanks!

