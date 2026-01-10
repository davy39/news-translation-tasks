---
title: Functional vs Class Components in React Native
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-17T19:46:00.000Z'
originalURL: https://freecodecamp.org/news/functional-vs-class-components-react-native
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9dcf740569d1a4ca39c4.jpg
tags:
- name: class
  slug: class
- name: components
  slug: components
- name: React Native
  slug: react-native
seo_title: null
seo_desc: 'In React Native, there are two main types of components that make up an
  application: functional components and class components. These are structured the
  same as they would be in a regular React app for the web.

  Class Components

  Class components are ...'
---

In React Native, there are two main types of components that make up an application: **functional components** and **class components**. These are structured the same as they would be in a regular React app for the web.

## Class Components

Class components are JavaScript ES2015 classes that extend a base class from React called `Component`.

```js
class App extends Component {
    render () {
        return (
            <Text>Hello World!</Text>
        )
    }
}
```

This gives the class `App` access to the React lifecycle methods like `render` as well as state/props functionality from the parent.

## Functional Components

Functional components are simpler. They don’t manage their own state or have access to the lifecycle methods provided by React Native. They are literally plain old JavaScript functions, and are sometimes called stateless components.

```js
const PageOne = () => {
    return (
        <h1>Page One</h1>
    );
}
```

## Summary

Class components are used as container components to handle state management and wrap child components. 

Functional components generally are just used for display purposes - these components call functions from parent components to handle user interactions or state updates.

## More info about component state

### Component State

In `Class` components, there is a way to store and manage state built in to React Native.

```javascript
class App extends Component {
  constructor () {
    super();
    this.state = {
      counter: 0
    };
  }
  incrementCount () {
    this.setState({
      counter: this.state.counter + 1
    });
  }
  decrementCount () {
    this.setState({
      counter: this.state.counter - 1
    });
  }
  render () {
    return (
      <View>
        <Text>Count: {this.state.counter}</Text>
        <Button onPress={this.decrementCount.bind(this)}>-</Button>
        <Button onPress={this.incrementCount.bind(this)}>+</Button>
      </View>
    );
  }
}
```

State is similar to props, but it is private and fully controlled by the component. Here, the `constructor()` method is calling the parent class’ constructor with `super();` - **`Component`** is the parent class of `App` because we are using the `extends` keyword. The `constructor()` method also initializes the component’s state object:

```text
this.state = {
  counter: 0
};
```

The state can be displayed within the component:

```js
{this.state.counter}
```

Or updated by calling:

```js
this.setState({});
```

**Note:** Aside from its initial creation in your component’s `constructor()` method, you should never directly modify the component’s state with `this.state =`. You must use `this.setState` as can be seen in the `incrementCount` and `decrementCount` functions above.

The count is incremented and decremented by calling the functions passed to the `onPress` handlers just like they would be if you called a click handler from JavaScript on the web.

_ASIDE: In the first example, `<Button>` is a custom component; it’s a combination of `<TouchableOpacity>` and `<Text>` from the React Native API:_

```js
const Button = ({ onPress, children, buttonProps, textProps }) => {
  const { buttonStyle, textStyle } = styles;
  return (
    <TouchableOpacity onPress={onPress} style={[buttonStyle, buttonProps]}>
      <Text style={[textStyle, textProps]}>
        {children}
      </Text>
    </TouchableOpacity>
  );
};
```

## More info on React Native:

* [React Native Guide](https://www.freecodecamp.org/news/react-native-guide/)

