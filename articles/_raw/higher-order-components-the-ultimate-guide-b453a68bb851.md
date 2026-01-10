---
title: 'Higher-Order Components: The Ultimate Guide'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-28T15:42:02.000Z'
originalURL: https://freecodecamp.org/news/higher-order-components-the-ultimate-guide-b453a68bb851
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ocK9Z4_zq2X0Y1uqvhWMEg.jpeg
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: software
  slug: software
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By David Kopal

  The maintainable component structure is a crucial prerequisite for a stable React
  application. You can achieve this by writing your code in a functional way using
  higher-order components (HoCs). If you stick to this pattern, you’ll end...'
---

By David Kopal

The maintainable component structure is a crucial prerequisite for a stable React application. You can achieve this by writing your code in a functional way using higher-order components (HoCs). If you stick to this pattern, you’ll end up with reusable components that are both readable and easy to test as each component is only responsible for a single task.

In this article I’d love to share my experience, so you can easily utilize this approach in your own applications. Not only will you learn how to enhance your presentational components using one or several HoCs, but you’ll also understand the principles behind this pattern.

### Why is this post so long?

When I started learning HoCs myself, I had no problem finding resources dealing with this topic. However, many of them assumed certain previous knowledge of complex topics, such as functional programming (FP) principles. As a result, it was challenging for me to understand what was going on under the hood and how the composition of several HoCs works.

It was this experience that motivated me to write this article in a broader and more beginner-friendly way. So, it covers not only HoCs, but also the principles of FP and the core ideas that one must understand to be able to unleash the power of higher-order components.

This article is also based on [my first tech conference talk](https://www.codinglawyer.io/posts/my-first-tech-talk) I gave at the International JavaScript Conference (iJS) 2017 in Munich. You can find all the source code on [Github](https://github.com/codinglawyer/international-javascript-conference-2017).

### Getting started

Let’s get started by looking at some code:

```
const starWarsChars = [   { name:'Luke', side:'light' },   { name:'Darth Vader', side:'dark' },   { name:'Obi-wan Kenobi', side:'light'},   { name:'Palpatine', side:'dark'},]
```

```
class FilteredList extends React.Component {   constructor(props) {      super(props)      this.state = { value: this.props.defaultState }   }   updateState(value) {      this.setState({ value })   }   render() {      const otherSide = this.state.value === 'dark' ? 'light' : 'dark'      const transformedProps = this.props.list.filter(char =&gt; char.side === this.state.value)      return (         <div>            <button onClick={() => this.updateState(otherSide)}>Switch</button>            {transformedProps.map(char =&gt;               <div key={char.name}>                  <div>Character: {char.name}</div>                  <div>Side: {char.side}</div>               </div>            )}         </div>      )   }}
```

```
ReactDOM.render (   <FilteredList defaultState='dark' list={starWarsChars} />,   document.getElementById('app'))
```

`FilteredList` is a huge component that does so many things. It maintains the state and filters the `list` of the Star Wars characters according to their side. Moreover, it renders the character list with a button to the screen.

It takes care of all the logic and presentation, and because of that, it’s hardly ever reusable.

If you decide to reuse this component elsewhere, you’ll always need to use all the component’s logic and UI. You can’t just cherry pick the functionality you really need for a particular scenario. Instead, you’ll be forced to rewrite an already existing piece of behavior as a different component.

![Image](https://cdn-media-1.freecodecamp.org/images/pjwdpoNQlgtziUpuadP7bbgc-l8oFK73vay9)

As a result, such repeated code would be difficult to maintain, especially in a larger application.

At the end of this article, we’ll be able to write a fully reusable version of this code using the principles of functional programming (FP).

Stay tuned.

### Taste the principles of functional programming

To show you why you should stick to the principles of FP in a React application, I need to talk a little bit about the core principles of FP themselves.

The idea is to decompose a program into simple **reusable functions**.

So, it’s all about functions. To be more precise, it’s all about **simple functions**. This means that each function should only be responsible for a single task. The simpler the function, the more reusable it is.

#### Higher-order functions

In JavaScript, you can use a function like any other value. It can be passed as an argument to a function or it can be returned by it. A function that **returns or creates a new function** is called a higher-order function.

```
const numbers = [1, 5, 8, 10, 21]const createAddingFunction = number =&gt; arr => arr.map(num =&gt; num + number)const numbersPlusOne = createAddingFunction(1)console.log(numbersPlusOne(numbers))  // [2, 6, 9, 11, 22]
```

`createAddingFunctions` is a higher-order function. It takes a `number` and creates a new function waiting for the array to be passed. In the example, we pass it `1` and get back a new function waiting for an array. We store it as `numbersPlusOne`. Then we pass the `numbers` array to it. The function then iterates over the array’s elements and increases each by one.

As you can see, we’re telling the JavaScript engine **what** we want to do — we want to map over the array’s elements. This code is self-explanatory. You just see the code and you immediately know what’s going on. Such code is called **declarative**. Functional programming is all about declarative code.

![Image](https://cdn-media-1.freecodecamp.org/images/wSxQZsAuLdO-eZ1CMEyYXxYdn6MzAUVNI8WO)

#### Avoid side effects

As a functional programmer, you want to avoid side effects in your functions as much as possible. In other words, a function shouldn’t be changing anything that’s not local to the function itself. You can reuse such a function easily, anywhere in your application. Functions without side effects are called **pure.** They always return the same output, given the same arguments.

If you want to write pure functions, you should also avoid mutating your values. This is called the principle of **immutability**. However, this doesn’t mean you don’t change your values. It means that when you want to change a value, you create a new one rather than mutating the original one.

However, in JavaScript, values such as objects and arrays are mutable. In order to respect the principle of immutability, we can treat the values as immutable.

For example, adhering to this principle, you won’t be able to accidentally mutate an object that was passed to a function as its parameter.

```
// pure functionconst numbers = [1, 5, 8, 10, 21]const createAddingFunction = number =&gt; arr => arr.map(num =&gt; num + number)const numbersPlusOne = createAddingFunction(1)console.log(numbersPlusOne(numbers))  //[2, 6, 9, 11, 22]console.log(numbers)  // [1, 5, 8, 10, 21]
```

```
// impure functionconst numbers = [1, 5, 8, 10, 21]const numbersPlusOne = numbers =&gt; {   for(let i = 0; i < numbers.length; i++) {      numbers[i] = numbers[i] + 1   }   return numbers}numbersPlusOne(numbers) // [2, 6, 9, 11, 22]console.log(numbers) // [2, 6, 9, 11, 22]
```

Here we have an example of a pure (same as in a previous example) and impure function. In the first case, the fact that we passed an array to the pure function didn’t affect the `numbers` array in any way.

However, in the second scenario, the array was mutated inside the impure function. Such behavior can make your code pretty unpredictable. And especially in the functional programming realm, we want to avoid that.

#### Composition

By now, we know we should be creating simple pure functions. However, what if we need behavior that is so complex that it can’t be stored in a single function? We could achieve this by combining several functions into a new compound function using composition.

```
const number = 15const increment = num =&gt; num + 5const decrement = num =>; num - 3const multiply = num =&gt; num * 2
```

```
const operation = increment(decrement(multiply(number)))console.log(operation)  //32
```

Composition means that we pass the output of the first function call as the input to the second function call, its output to the third function and so on. As a result, we get a compound function.

In our example, we have a `number` and three functions. We wrap them all inside each other, and we get a compound function waiting for the `number` argument. By using composition, we don’t need to create variables for storing the result of the single functions.

#### Combined

To really see the benefits of all these FP principles, you need to combine them together.

Ideally, your application should be composed of **pure functions** whose data are treated as **immutable.** That means they’re not modifying their upper scope and so you’re free to reuse them in any part of your program. Each function should be responsible for a single task and should be separated from the other ones. You can use them as they are or you can **compose** them together to achieve more complex behavior.

By sticking to FP principles, you’ll end up with simple reusable functions that can be composed together.

![Image](https://cdn-media-1.freecodecamp.org/images/e3godfqlWfBBv2VvlpjzA4LfUVmnMPOl-sTX)

### Functional programming and React

Now that we are familiar with the basic principles of FP, we can take a look at how to use them to our advantage in React.

React applications are composed of components. But what exactly is a component?

```
// Class-based componentclass Button extends React.Component {   render(){      return <button>{this.props.title}</button>   }}
```

```
// Functional componentconst Button = (props) =>   <button>{props.title}</button>
```

Since the class is just syntactic sugar over functions and the functional component is basically a function, **components are just functions**. It’s a function that takes input data (props) and returns a tree of React elements (UI) which is rendered to the screen. However, it doesn’t need to return UI all the time. It can return a component as well as we’re going to see later.

So React UI is just a **composition of functions**. That sounds awfully like FP, right?

#### Smart and presentational components

A component is typically composed of logic and presentation. However, if we decide to write all our components as such, we would end up with dozens of components having only a single purpose. On the other hand, if we try to [separate these concerns](https://en.wikipedia.org/wiki/Separation_of_concerns), we’ll be able to create simple reusable components. Following this idea, we should prefer defining our components as smart (logic) and presentational (UI).

![Image](https://cdn-media-1.freecodecamp.org/images/ZY1YlmlV6sbafDF3tYlxfAsmpef81Qj3bPtF)

The **presentational** component takes care of all the UI. It will typically have the form of a **functional** component, which is just a render method. You can think of them as functions.

The component containing mostly logic is called **smart**. It typically handles data manipulations, API calls, and event handlers. It will often be defined as a **class** since it provides us with more functionality (such as internal state and lifecycle).

Each component should be responsible for a single task and written so generally that it can be reused throughout the application. Such a task should be either logic (smart component) or presentation (presentational component). The combination of both in a single component should be minimized.

* **smart class component**

```
class DisplayList extends Component {   constructor(props) {      super(props)      this.state = {         starWarsChars: [            { name:'Luke Skywalker', side:'light' },            { name:'Darth Vader', side:'dark' },            { name:'Obi-wan Kenobi', side:'light' },            { name:'Palpatine', side:'dark' },         ]      }   }   render() {      return (         <div>            {this.state.starWarsChars.map(char =>               <div key={char.name}>                  <div>Character: {char.name}</div>                  <div>Side: {char.side}</div>               </div>            )}         </div>      )   }}
```

```
ReactDOM.render(   <DisplayList />,   document.getElementById('app'))
```

* **presentational functional component**

```
const starWarsChars = [   { name:'Luke', side:'light' },   { name:'Darth Vader', side:'dark' },   { name:'Obi-wan Kenobi', side:'light'},   { name:'Palpatine', side:'dark'},]
```

```
const DisplayList = ({ list }) =>   <div>      {list.map(char =&gt;         <div key={char.name}>            <div>Character: {char.name}</div>            <div>Side: {char.side}</div>         </div>      )}   </div>
```

```
ReactDOM.render (   <DisplayList list={starWarsChars} />,   document.getElementById('app'))
```

Let’s take a look at the functional component. It’s pretty reusable since it only takes care of the UI. So, if you want to display a list of Star Wars characters elsewhere in your application, you can easily reuse this component. It also doesn’t have any side effects since it doesn’t affect its outer scope in any way.

You can see that the functional component is just a **pure function** that takes props object and returns the same UI given the same props.

Not only is that React application a composition of functions in general, but it can also be a **composition of pure functions**.

As we’ve already learned, pure functions are the basic building blocks of FP. So if we prefer using functional components, we’ll be able to **apply various FP techniques** such as the higher-order components in our code.

![Image](https://cdn-media-1.freecodecamp.org/images/akA76VKyKkf2fR6ELKTOTK5S74uV92gPRP-p)

#### Adding more logic

Let’s take a look at our functional component again. It takes a list of Star Wars characters as a prop and renders them to the screen. It’s pretty reusable since it doesn’t contain any logic.

Now, what if we wanted to display only characters belonging to the dark side? The simplest solution will be to filter the `list` prop inside the component.

```
const FilteredList = ({ list, side }) =&gt; {   const filteredList = list.filter(char => char.side === side)   return (      <div>         {filteredList.map(char =&gt;            <div key={char.name}>               <div>Character: {char.name}</div>               <div>Side: {char.side}</div>            </div>         )}      </div>   )}
```

```
ReactDOM.render (   <FilteredList side='dark' list={starWarsChars}/>,   document.getElementById('app'))
```

This will do the trick. We renamed `DisplayList` to `FilteredList` since it now contains filtering functionality. We are also now passing the `side` prop according to which list will be filtered.

However, is this the ideal solution? As you can see, the `FilteredList` component isn’t reusable anymore. Because of the filter function buried inside of it, this component can hardly ever be reused.

If we wanted to display characters elsewhere in our application without any filtering, we would need to create another component. Furthermore, if we wanted to use the filter function in other components, we would have to duplicate this behavior as well.

Fortunately, there’s a **more elegant and declarative solution** that lets us keep our presentational component reusable. We are able to filter the characters list before it’s passed as the prop to the `DisplayList` component.

```
const withFilterProps = BaseComponent =&gt; ({ list, side }) => {   const transformedProps = list.filter(char => char.side === side)   return <BaseComponent list={transformedProps} />}
```

```
const renderDisplayList = ({ list }) =>   <div>      {list.map(char =&gt;         <div key={char.name}>            <div>Character: {char.name}</div>            <div>Side: {char.side}</div>         </div>      )}   </div>
```

```
const FilteredList = withFilterProps(renderDisplayList)
```

```
ReactDOM.render (   <FilteredList side='dark' list={starWarsChars} />,   document.getElementById('app'))
```

We renamed our functional component `renderDisplayList` to make it obvious that it’s responsible only for the UI rendering.

First, let’s take a look at the `FilteredList` component. This component gets created by passing our functional component `renderDisplayList` to the `withFilterProps` higher-order function. When this happens, we get back a functional component and store it as `FilteterdList` waiting for the props object to be passed.

We render the `FilteredList` component at the end of the example by passing the props. It filters the character list from the props according to the `side` prop. The filtered list is then passed as the props to the `renderDisplayList,` which subsequently renders the list of characters to the screen.

### Introducing higher-order components

![Image](https://cdn-media-1.freecodecamp.org/images/BZQLvTD70AGyVbm5WxLfeoJfyMIm4RaMUjrU)

Let’s now talk about the nature of the higher-order function `withFilterProps`. In React’s vocabulary, such a function is called a higher-order component (HoC). Just as the higher-order function creates a new function, the HoC creates a new component.

HoC is a **function** that **accepts** **a component** and **returns a new component that renders the passed one**. This new component is enhanced with an additional functionality.

```
const HoC = BaseComponent => EnhancedComponent
```

In our example, the `withFilterProps` HoC takes the `renderDisplayList` component and returns a new functional component that renders the `renderDisplayList`. The `renderDisplayList` component is enhanced with the filtering props logic.

Because we abstracted all the logic to the HoC, our base functional component only takes care of the UI rendering and is reusable again.

![Image](https://cdn-media-1.freecodecamp.org/images/zwq70rgYR7Ne9yoFWhFPgutiaSx-LztiBCDM)

The HoC is a special type of a function that wraps the presentational component and enhances it with an advanced functionality. Think of them as the **wrappers for your functional components.**

Thanks to the HoC pattern, you can enhance your simple functional components with whatever logic you want. This is the power of the HoC pattern. You can edit/update/transform props, maintain internal state, or affect the component rendering outside of your presentational component.

Sticking to this pattern will enable you to use only functional components as your base components throughout your application and get rid of all the class components.

If we again consider the distinction between smart and presentational components, the base component will always be the presentational one (since it’s just a pure function). On the other hand, the HoC will take the role of a **smart** component since it deals only with the logic, which is then passed down to the presentational component. However, if you don’t need the class-specific behavior, you can also define HoC as a functional component (as you’ve just seen).

Since you made it this far, let’s slow down a little bit and talk about food :)

#### Meatloaf or Pancake

At the beginning of this article, we saw this hard-to-reuse component that takes care of all the logic and presentation.

```
class FilteredList extends React.Component {   constructor(props) {      super(props)      this.state = { value: this.props.defaultState }   }   updateState(value) {      this.setState({ value })   }   render() {      const otherSide = this.state.value === 'dark' ? 'light' : 'dark'      const transformedProps = this.props.list.filter(char =&gt; char.side === this.state.value)      return (         <div>            <button onClick={() => this.updateState(otherSide)}>Switch</button>            {transformedProps.map(char =&gt;               <div key={char.name}>                  <div>Character: {char.name}</div>                  <div>Side: {char.side}</div>               </div>            )}         </div>      )   }}
```

```
ReactDOM.render (   <FilteredList defaultState='dark' list={starWarsChars} />,   document.getElementById('app'))
```

You can think of this component as **meatloaf**.

![Image](https://cdn-media-1.freecodecamp.org/images/kLsEptFbZS0hA6sgb1wfhSwQDGFdZiUHzxQK)

When preparing meatloaf, you take the meat, breadcrumbs, garlic, onion, and eggs, mix them together, put the raw meatloaf into the oven, and wait until it’s cooked. There’s no way that you can take the eggs or the onion from the meatloaf, since everything is irrevocably combined together.

This is the same as a component that is a mixture of logic and UI. You just can’t take something from it. **You need to use it as is or not at all.**

Try to think of the presentational components as **pancakes**.

![Image](https://cdn-media-1.freecodecamp.org/images/nokhg0VKb67G3lVvbA5Mv4wfCGAJ4iUtpsxG)

However, simple pancakes without any decoration are pretty boring, and no one eats them like this anyway. So you want to decorate them. You can pour maple syrup on them or put some berries or chocolate on top of them. So many possible decorating layers for you to use!

![Image](https://cdn-media-1.freecodecamp.org/images/D9QHuPyjOO7sbx4xWIOSAkL4SFiEsyZfDKIE)

In the React application, these decorating layers are represented by the HoCs. So, just as you decorate a pancake according to your taste, you also decorate the presentational component using HoC with the functionality you want. As a result, **you can reuse a particular presentational component in different places of your application** and decorate it with the HoC you want for a particular case.

However, you can’t do that with the component that is responsible for all the logic and presentation, since everything is irrevocably combined together.

I hope that this metaphor gave you a better understanding of the HoC pattern. If not, at least I made you hungry :).

### Make all the components reusable again

Now, that we know how to create a HoC, we’ll take a look at how to make it reusable.

Making components reusable means to **decouple them from the data**. This means that they shouldn’t be dependent on a particular props structure. Sticking to reusable components helps you to avoid unnecessary duplication. You just pass a different set of props each time.

By using the HoC pattern in the previous example, we moved all the logic to the HoC, and just let the base component render the UI. As a result, our **presentational component became reusable** since it just receives data as props and renders it to the screen.

But it would be pretty difficult to reuse our HoC as well since it’s too specific.

```
const withFilterProps = BaseComponent =&gt; ({ list, side }) => {   const transformedProps = list.filter(char => char.side === side)   return <BaseComponent list={transformedProps} />}
```

It can be applied only in the cases where the `list` and `side` props are present. You don’t want this kind of specificity in your application since you want reusable HoCs that can be used in various scenarios.

Let’s make the HoC reusable.

![Image](https://cdn-media-1.freecodecamp.org/images/-j5TCVnvuAmfoAfTmPX2WrVTRabraGpWDaRs)

```
const withTransformProps = transformFunc =&gt; {   const ConfiguredComponent = BaseComponent => {      return baseProps => {         const transformedProps = transformFunc(baseProps)         return <BaseComponent {...transformedProps} />      }   }   return ConfiguredComponent}
```

```
const renderDisplayList = ({ list }) =>   <div>      {list.map(char =&gt;         <div key={char.name}>            <div>Character: {char.name}</div>            <div>Side: {char.side}</div>         </div>      )}   </div>
```

```
const FilteredList = withTransformProps(   ({ list, side }) =&gt; ({      list: list.filter(FilteredListchar =>         char.side === side)   }))(renderDisplayList)
```

```
ReactDOM.render (   <FilteredList      side='dark'      list={starWarsChars}   />,   document.getElementById('app'))
```

This code still does the same thing as the previous HoC example. We filter the props using the HoC component and then pass them to the base component. However, the old name would be misleading, since the HoC is no longer limited only to the filtering logic, so we renamed it `withTransformProps`.

We also no longer care about the props structure. We are newly passing a `transformFunc` as a **configuration function** to the `withTransformProps`. This function is responsible for the props transformation.

Let’s take a look at the `FilteredList` enhanced component. It gets created when we pass the configuration function (responsible for the props transformation) to the `withTransformProps`. We get back a specialized HoC with the transformation function stored inside the closure. We store it as the `ConfiguredComponent`. It expects the `BaseComponent` to be passed. When the `renderDisplayList` is passed to it, we get back a functional component that is waiting for the props to be passed. We store this enhanced component as the `FilteredList`.

The props get passed when we render the `FilteredList` component. Then, the transforming function we passed earlier takes the props and filters the characters according the side. The returned value is then passed as the props to the `renderDisplayList` base component which renders filtered Start Wars characters to the screen.

However, our HoC syntax is pretty verbose. We don’t need to store the specialized HoC as the `ConfiguredComponent` inside a variable.

```
const withTransformProps = mapperFunc =>   BaseComponent => baseProps => {      const transformedProps = mapperFunc(baseProps)      return <BaseComponent {...transformedProps} />   }
```

This solution is much cleaner.

The idea behind this approach is to **have a reusable HoC that can be configured for any scenario** in which we want to do something with the props before they get passed to the base component. That’s a powerful abstraction, isn’t it?

In our example, we passed a custom filtering function that could be different for every use case. And if we later decide that we want to change some of the HoC’s behavior, we just need to change it in a single reusable component and not in many different places of our application.

```
const HoC = config => BaseComponent => EnhancedComponent
```

The HoC and the base component are both **reusable** and **independent** of each other. The HoC doesn’t know where its data goes and the presentational component has no idea where its data is coming from.

Writing reusable HoCs and presentational components will help you to avoid unnecessary repetition and force you to write simpler components. **As a result, you’ll be writing cleaner, maintainable, and readable code.**

![Image](https://cdn-media-1.freecodecamp.org/images/HzHa3iKWnGZHjcNm7c0aTQTANWUUkIEqQDFy)

Congratulations! By now you should be able to write reusable higher-order components yourself.

In the following sections, you’ll learn the difference between class HoC and the functional one. We’ll also spend a good amount of time understanding how the composition of several higher-order components works. All of this will allow us to enhance our base components with even more behavior that can be easily reused throughout our application.

### Functional or class-based HoCs?

![Image](https://cdn-media-1.freecodecamp.org/images/bfxSr1qSfYN01qO-eUZjwJmJyDhuFuytOmOr)

Let’s talk a little bit about the difference between functional HoCs and class-based ones. When is it more convenient to stick to the former and when should you go for the latter?

Since we want to follow the principles of FP, we should be using **functional components** as much as possible. We’re already doing this with presentational components as we’ve seen above. And we should do this with HoCs as well.

#### Functional HoC

A functional HoC just wraps the base component, injects it with new props along with the original ones, and returns a new component. It doesn’t change the original component by modifying its prototype as the classes do. We saw such an HoC above. Here’s a quick reminder:

```
const withTransformProps = mapperFunc =>   BaseComponent => baseProps => {      const transformedProps = mapperFunc(baseProps)      return <BaseComponent {...transformedProps} />   }
```

This HoC doesn’t have any side effects. It doesn’t mutate anything. It’s a pure function.

When creating an HoC, we should define it as a functional component if possible.

#### Class-based HoCs

However, sooner or later, you’ll need to access the internal state or lifecycle methods in your component. You can’t achieve this without classes since this behavior is inherited from the [React.Component](https://facebook.github.io/react/docs/react-component.html), which can’t be accessed within the functional component. So, let’s define a class-based HoC.

```
const withSimpleState = defaultState =&gt; BaseComponent => {   return class WithSimpleState extends React.Component {      constructor(props) {         super(props)         this.state = { value: defaultState }         this.updateState = this.updateState.bind(this)      }      updateState(value) {         this.setState({ value })      }      render() {         return (            <BaseComponent               {...this.props}               stateValue={this.state.value}               stateHandler={this.updateState}            />         )      }   }}
```

```
const renderDisplayList = ({ list, stateValue, stateHandler })=&gt; {   const filteredList = list.filter(char => char.side === stateValue)   const otherSide = stateValue === 'dark' ? 'light' : 'dark'   return (      <div>         <;button onClick={() => stateHandler(otherSide)}>Switch</button>         {filteredList.map(char =>            <div key={char.name}>               <div>Character: {char.name}</div>               <div>Side: {char.side}</div>            </div>         )}      </div>   )}
```

```
const FilteredList = withSimpleState('dark')(renderDisplayList)
```

```
ReactDOM.render (   <FilteredList list={starWarsChars} />,   document.getElementById('app'))
```

Our new class-based HoC `withSimpleState` expects a configuration parameter `defaultState` which is pretty self-explanatory. It also maintains a state named `value` and defines an event handler `updateState` that can set the value of the state. Finally, it passes the state utilities along with the original props to the base component.

`renderDisplayList` now contains filtering logic that was previously stored inside the `withTransformProps` HoC, so it’s not reusable anymore.

Let’s take a look at the `FilteredList` component. First, we pass the configuration string `dark` to the `withSimpleState` and get back a specialized HoC waiting for the base component. So, we pass it the `renderDisplayList` component and get back a class component waiting for the props to be passed. We store this component as the `FilteredList`.

At the end of the example, we render the component by passing the props to it. When this happens, the class component sets the state `value` to `dark` and passes the state and its handler to the `renderDisplayList` component along with the `list` prop.

`renderDisplayList` then filters the `list` prop according to the passed state value and sets the `otherSide` variable. Finally, it renders the filtered list to the screen along with the button with the attached state handler. When the button is clicked, the state is set to the `otherSide` variable.

#### Does it matter?

![Image](https://cdn-media-1.freecodecamp.org/images/7SyB4ye4uAKg6cBt-EwR-3Oyu0nmQzJp3S2k)

As you’ve just seen, our new HoC `withSimpleState` returns a class, instead of a functional component. You might say it doesn’t look like a **pure function** since it contains impure class-specific behavior (state). However, let’s take a closer look.

`withSimpleState` doesn’t have any side effects. It doesn’t mutate anything. It just takes the base component and returns a new one. Although it contains the impure class-related code, the HoC itself is still a pure function since “the purity of a function is judged from the outside, [regardless of what goes on inside](https://github.com/getify/Functional-Light-JS/blob/master/manuscript/ch5.md#containing-effects).” We are basically hiding the class-specific impure code inside the HoC pure function.

The HoC (pure function) enables us to encapsulate the impure class-related code inside of it.

If you find yourself in a situation where you simply can’t write a functional component because you need a class-related behavior, wrap the impure code inside the HoC, which is the pure function instead, just as we did in the example.

#### What’s next?

If you check our example again, you’ll see that we have a new problem. The `renderDisplayList` component is no longer reusable since we moved the filtering logic inside it.

To make it reusable again, we need to move the logic back to the `withTransformProps` HoC. To achieve this, we need to figure out how to use the `withTransformProps` and `withSimpleState` HoCs with the base component at the same time and allow the `renderDisplayList` to only be responsible for the presentation again. We can achieve this behavior using composition.

### Composition

![Image](https://cdn-media-1.freecodecamp.org/images/gC0gCeSTZ7mCgox08iZAMbPCLKJ9if38K1mg)

We’ve already talked about the composition principle at the beginning. It enables us to combine several functions into a new compound function. Here’s a quick reminder:

```
const number = 15const increment = num => num + 5const decrement = num => num - 3const multiply = num => num * 2
```

```
const operation = increment(decrement(multiply(number)))console.log(operation)  //32
```

We have a number and three functions. We wrap them all inside each other, and we get a compound function to which we pass the number.

This works fine. However, the readability might get worse, if we wanted to compose even more functions. Fortunately, we can define a functional programming `compose` function to help us out. Keep in mind that it composes functions from **right to left**.

```
const compose = (...funcs) =&gt; value =&gt;   funcs.reduceRight((acc, func) => func(acc)      , value)
```

```
const number = 15const increment = num =&gt; num + 5const decrement = num =>; num - 3const multiply = num =&gt; num * 2
```

```
const funcComposition = compose(   increment,   decrement,   multiply)
```

```
const result = funcComposition(number)console.log(result)  //32
```

We no longer need to explicitly wrap the functions inside each other. Instead, we pass them all as the arguments to the `compose` function. When we do that, we get back a new compound function waiting for the `value` argument to be passed. We store it as a `funcComposition`.

Finally, we pass the `number` as the `value` to the `funcComposition` function. When this happens, the `compose` passes the `value` to the `multiply` (rightmost) function. The returned value is then passed as an input to the `decrement` function and so on until all the functions in the composition have been called. We store the final value as a `result`.

#### Composition of HoCs

![Image](https://cdn-media-1.freecodecamp.org/images/b5c02CoroaWSkzvTh9sXCjy5A09qbP3lxdof)

Let’s take a look at how we could `compose` several HoCs. We’ve already learned that our reusable HoCs should only be responsible for a single task. However, what if we needed to implement complex logic that can’t be stored in a single HoC? To achieve this, we want to be able to **combine several HoCs together and wrap them around the base component.**

First, let’s take a look at the HoC composition without a `compose` helper since it’s easier to understand what’s going on.

```
const withTransformProps = mapperFunc =>   BaseComponent => baseProps => {      const transformedProps = mapperFunc(baseProps)      return <BaseComponent {...transformedProps} />   }
```

```
const withSimpleState = defaultState =&gt; BaseComponent => {   return class WithSimpleState extends React.Component {      constructor(props) {         super(props)         this.state = { value: defaultState }         this.updateState = this.updateState.bind(this)      }      updateState(value) {         this.setState({ value })      }      render() {         return (            <BaseComponent               {...this.props}               stateValue={this.state.value}               stateHandler={this.updateState}            />         )      }   }}
```

```
const renderDisplayList = ({ list, stateHandler, otherSide }) =&gt; (   <div>      <button onClick={() => stateHandler(otherSide)}>Switch</button&gt;      {list.map(char =>         <div key={char.name}>            <div>Character: {char.name}</div>            <div>Side: {char.side}</div>         </div>      )}   </div>)
```

```
const FilteredList = withTransformProps(({ list, stateValue, stateHandler }) =&gt; {   const otherSide = stateValue === 'dark' ? 'light' : 'dark'   return {      stateHandler,      otherSide,      list: list.filter(char => char.side === stateValue),   }})(renderDisplayList)
```

```
const ToggleableFilteredList = withSimpleState('dark')(FilteredList)
```

```
ReactDOM.render (   <ToggleableFilteredList list={starWarsChars} />,   document.getElementById('app'))
```

Nothing new here. We’ve seen all this code before. The new thing is that we are composing two HoCs — `withSimpleState` which provides us with the state utilities and `withTransformProps` which gives us the props transformation functionality.

We have two enhanced components here: `FilteredList` and `ToggleableFilteredList`.

First, we enhance the `renderDisplayList` component with the `withTransformProps` HoC and store it as the `FilteredList`. Secondly, we enhance the new `FilteredList` component using the `withSimpleState` HoC and store it as the `ToggleableFilteredList`.

`ToggleableFilteredList` is a component enhanced by two HoCs that have been composed together.

Here’s a detailed description of the HoC composition:

1. We pass a props transformation function to the `withTransformProps` HoC and get back a specialized HoC waiting for the base component to be passed.
2. We pass it the `renderDisplayList` presentational component and get back a new functional component expecting the props argument.
3. We store this enhanced component as the `FilteredList`.
4. We pass the `dark` string to the `withSimpleState` HoC and get back a specialized HoC waiting for the base component to be passed.
5. We pass it our enhanced `FilteredList` component as the base component and we get back a class component waiting for the props.
6. We store this **higher-order component composition** as the `ToggleableFilteredList`.
7. We render the `ToggleableFilteredList` component by passing the `list` props to it.
8. `ToggleableFilteredList` is the `FilteredList` component enhanced by the `withSimpleState` HoC. So, the props are first passed to the class component that was returned by this HoC. Inside it, the props get enhanced with a state and its handler. These props along with the original ones are then passed to the `FilteredList` as the base component.
9. `FilteredList` is a `renderDisplayList` component enhanced by the `withTransformProps` HoC. So, the props are first passed to the functional component that was returned by this HoC. Inside it, the passed `list` prop is filtered using the transformation function. These props along with the other props are then passed to the base component `renderDisplayList`.
10. Finally, the `renderDisplayList` component renders the list of the characters with the switch button to the screen.

The composition lets us enhance our base component with the functionality aggregated from several HoCs.

In our example, we passed the new behavior from the `withSimpleState` and `withTransformProps` HoCs to the `renderDisplayList` base component.

As you’ve just seen, the **props are the only language that HoCs use to talk to each other inside a composition**. Each HoC performs a specific action which results in an enhancement or a modification of the props object.

![Image](https://cdn-media-1.freecodecamp.org/images/WYe3UGjzTTBQqd-jPngl3i5fQeNOhFF2oMES)

#### Refactor

Although our HoC composition works, the syntax itself is pretty verbose. We can make it simpler by getting rid of the `ToggleableFilteredList` variable and just wrap the HoCs inside each other.

```
const FilteredList = withSimpleState('dark')(   withTransformProps(({ list, stateValue, stateHandler }) =&gt; {      const otherSide = stateValue === 'dark' ? 'light' : 'dark'      return {         stateHandler,         otherSide,         list: list.filter(char => char.side === stateValue),      }   })(renderDisplayList))
```

This code is a little bit better. However, we are still manually wrapping all the components. Imagine that you wanted to add even more HoCs to this composition. In such a case, our composition will become difficult to read and understand. Just imagine all those parentheses!

#### Using compose

Since this talk is about FP principles, let’s use the `compose` helper.

```
const compose = (...hocs) =&gt; BaseComponent =&gt;   hocs.reduceRight((acc, hoc) => hoc(acc)      , BaseComponent)
```

```
const enhance = compose(   withSimpleState('dark'),   withTransformProps(({ list, stateValue, stateHandler }) =&gt; {      const otherSide = stateValue === 'dark' ? 'light' : 'dark'      return {         stateHandler,         otherSide,         list: list.filter(char => char.side === stateValue),      }   }))
```

```
const FilteredList = enhance(renderDisplayList)
```

We no longer need to explicitly wrap the HoCs inside each other. Instead, we pass them all as the arguments to the `compose` function. When we do that, we get back a new compound function waiting for the `BaseComponent` argument to be passed. We store this function as `enhance`. Then, we just pass the `renderDisplayList` as the base component to it, and `compose` will do all the component wrapping for us.

#### Pancakes again

I’d like to come back to our **pancake** analogy. Before, we were decorating our pancakes with only a single flavorful layer. But as we all know, pancakes taste much better when you combine more flavors together. How about a pancake with melted chocolate and banana or with cream and caramel? You know what I’m talking about…

Just as you can decorate your pancake using one or several decorating layers depending on your tastes, you can decorate your presentational component with one or several HoCs to get the combination of logic you want for your particular use case.

![Image](https://cdn-media-1.freecodecamp.org/images/2kpZubt4-blpyzuNxiiuNYSJlTqG914ojayU)

If you need a complex logic for your presentational component, you don’t need to store it all inside a single component or in a single HoC. Instead, you just compose several simple HoCs together and enhance your presentational component with them.

### Recompose

So far, you’ve seen some simple HoCs. However, this pattern is so powerful that it has been used in many React-based libraries (such as React-Redux, React router, Recompose).

I’d like to talk more about the [Recompose library](https://github.com/acdlite/recompose), which provides us with dozens of HoCs. It uses HoCs for everything from state and lifecycle to conditional rendering and props manipulation.

Let’s rewrite our HoC composition example using the predefined HoCs from Recompose.

```
import { withState, mapProps, compose } from 'recompose';
```

```
const enhance = compose(   withState('stateValue', 'stateHandler', 'dark'),   mapProps(({ list, stateValue, stateHandler }) =&gt; {      const otherSide = stateValue === 'dark' ? 'light' : 'dark'      return {         stateHandler,         otherSide,         list: list.filter(char => char.side === stateValue),      }   }),)
```

```
const FilteredList = enhance(renderDisplayList)
```

```
ReactDOM.render (   <FilteredList list={starWarsChars} />,   document.getElementById('app'))
```

Our two custom HoCs `withSimpleState` and `withTransformProps` are already predefined in Recompose as `withState` and `mapProps`. Moreover, the library also provides us with a predefined `compose` function. So, it’s really easy just to use these existing implementations, rather than defining our own.

The Recompose version of the HoC composition isn’t that different from ours. Just the `withState` HoC is now more reusable since it takes three arguments, where you can set the default value of the state, the state name, and the name of its handler as well. `mapProps` works the same way as our implementation. We only need to pass the configuration function.

As a result, we don’t need to define HoCs, which provide us with a general behavior.

#### More improvements

We can improve our composition using Recompose even more since there’s still one issue we haven’t addressed yet.

```
const renderDisplayList = ({ list, stateHandler, otherSide }) =&gt; (   <div>      <button onClick={() => stateHandler(otherSide)}>Switch</button&gt;      {list.map(char =>         <div key={char.name}>            <div>Character: {char.name}</div>            <div>Side: {char.side}</div>         </div>      )}   </div>)
```

If we check the `renderDisplayList` component again, we can see that it’s click handler function gets recreated each time the component re-renders. And we want to prevent any unnecessary recreation since it might hinder the performance of our application. Fortunately, we can add the `withHandlers` HoC to our composition to address this issue.

```
import { withState, mapProps, withHandlers, compose } from 'recompose';
```

```
const renderDisplayList = ({ list, handleSetState }) =&gt; (   <div>      <button onClick={handleSetState}>Switch</button>      {list.map(char =>         <div key={char.name}>            <div>Character: {char.name}</div>            <div>Side: {char.side}</div>         </div>      )}   </div>)
```

```
const enhance = compose(   withState('stateValue', 'stateHandler', 'dark'),   mapProps(({ list, stateValue, stateHandler }) =&gt; {      const otherSide = stateValue === 'dark' ? 'light' : 'dark'      return {         stateHandler,         otherSide,         list: list.filter(char => char.side === stateValue),      }   }),   withHandlers({      handleSetState: ({ stateHandler, otherSide }) =&gt; () => stateHandler(otherSide)   }))
```

```
const FilteredList = enhance(renderDisplayList)
```

```
ReactDOM.render (   <FilteredList list={starWarsChars} />,   document.getElementById('app'))
```

`withHandlers` HoC takes an object of functions as a configuration argument. In our example, we pass an object with a single function `handleSetState`. When this happens, we get back an HoC expecting the base component and the props to be passed. When we pass them, the outer function in every key of the passed object receives the props object as an argument.

In our case `handleSetState` function receives `stateHandler` and `otherSide` props. We get back a new function that is then injected to the props and is passed down to the `renderDisplayList` component.

The `handleSetState` then gets attached to the button in a way that doesn’t require its recreation during every component's re-render since the `withHandlers` makes sure that the identity of its handlers are preserved across renders. As a result, the handlers get recreated **only** when the props passed to the `withHandlers` change.

Of course, the possible recreation of our simple click handler function doesn’t hinder the performance much. `withHandlers` is much more useful when you need to optimize a higher number of complex handlers.

This also means that it’s a good place for storing all the handlers used inside your presentational component. This way, it’s immediately obvious for anyone who looks at your component, which handlers are being used inside it. As a result, it’s pretty simple for a developer to add or remove a particular handler. This is much better than searching for all the handlers inside a component manually.

By providing us with many reusable HoCs, Recompose makes HoC composition and the usage of HoCs in general much easier, since we don’t need to write all the HoCs ourselves.

In real-world applications, you’ll be using these predefined HoCs quite often since they cover most typical use cases. And in the case you need a specific logic that needs to be shared across several components, you’ll define an HoC yourself.

![Image](https://cdn-media-1.freecodecamp.org/images/NR5prIzyMKBd0LMf14ciCMvy0mIcfKpvRhKh)

### Conclusion

Thanks to the principles of functional programming we were able to transform this not reusable huge component from the beginning…

```
class FilteredList extends React.Component {   constructor(props) {      super(props)      this.state = { value: this.props.defaultState }   }   updateState(value) {      this.setState({ value })   }   render() {      const otherSide = this.state.value === 'dark' ? 'light' : 'dark'      const transformedProps = this.props.list.filter(char =&gt; char.side === this.state.value)      return (         <div>            <button onClick={() => this.updateState(otherSide)}>Switch</button>            {transformedProps.map(char =&gt;               <div key={char.name}>                  <div>Character: {char.name}</div>                  <div>Side: {char.side}</div>               </div>            )}         </div>      )   }}
```

```
ReactDOM.render (   <FilteredList defaultState='dark' list={starWarsChars} />,   document.getElementById('app'))
```

…into this reusable, readable, and maintainable component composition.

```
import { withState, mapProps, withHandlers, compose } from 'recompose';
```

```
const renderDisplayList = ({ list, handleSetState }) =&gt; (   <div>      <button onClick={handleSetState}>Switch</button>      {list.map(char =>         <div key={char.name}>            <div>Character: {char.name}</div>            <div>Side: {char.side}</div>         </div>      )}   </div>)
```

```
const enhance = compose(   withState('stateValue', 'stateHandler', 'dark'),   mapProps(({ list, stateValue, stateHandler }) =&gt; {      const otherSide = stateValue === 'dark' ? 'light' : 'dark'      return {         stateHandler,         otherSide,         list: list.filter(char => char.side === stateValue),      }   }),   withHandlers({      handleSetState: ({ stateHandler, otherSide }) =&gt; () => stateHandler(otherSide)   }))
```

```
const FilteredList = enhance(renderDisplayList)
```

```
ReactDOM.render (   <FilteredList list={starWarsChars} />,   document.getElementById('app'))
```

We use these principles during application development quite often. Our aim is to use simple reusable components as much as possible. The HoC pattern helps us to achieve this since its idea is to move the logic to the HoC and let the presentational functional component take care of the UI rendering. As a result, we don’t need to use classes for our presentational components anymore, only for the HoCs if we need a class-specific behavior.

As a result, our application is composed of a bunch of presentational components that we can reuse throughout our application, and we can enhance them using one or several reusable HoCs to get a logic we need for a particular scenario (such as a dedicated HoC for data fetching).

A cool feature about our approach is that, if you take a look at a particular HoC composition, you immediately know what kind of logic it uses. You just need to check the `compose` function where you can see all the logic contained in the HoCs. If you decide to add more logic, you just insert a new HoC into the `compose` function. Furthermore, if you wanted to see what handlers the component uses, you just need to check the `withHandlers` HoC.

Another cool thing about HoCs is that they’re not tied to React. This means you can use them in your other applications that haven’t been written in React.

![Image](https://cdn-media-1.freecodecamp.org/images/1AAlmR3SlqLaDv3vQYJuqayzeRcdOlZi7Sn4)

Congratulations! You made it.

If you liked this article, give it a few claps**.** I would greatly appreciate it and more people will be able to see this post as well.

This post was [originally published on my blog](https://www.codinglawyer.io/).

If you have any questions, criticism, observations, or tips for improvement, feel free to write a comment below or reach me via [Twitter](https://twitter.com/coding_lawyer).

[**David Kopal (@coding_lawyer) | Twitter**](https://twitter.com/coding_lawyer)  
[_The latest Tweets from David Kopal (@coding_lawyer). passionate programmer, speaker, former lawyer, love to learn new…_twitter.com](https://twitter.com/coding_lawyer)

