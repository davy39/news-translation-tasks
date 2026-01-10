---
title: Vue vs React – How to Go from One Framework to the Other
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-10-22T21:59:39.000Z'
originalURL: https://freecodecamp.org/news/vue-vs-react-comparison-of-frameworks
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/pexels-ryutaro-tsukata-5472355.jpg
tags:
- name: framework
  slug: framework
- name: React
  slug: react
- name: vue
  slug: vue
seo_title: null
seo_desc: "By Yiğit Kemal Erinç\nThese days, a new trending front-end framework is\
  \ released every now and then. But React and Vue.js still stand as the most popular\
  \ among all the other alternatives. \nAnd although both are performant, elegant,\
  \ and arguably easy t..."
---

By Yiğit Kemal Erinç

These days, a new trending front-end framework is released every now and then. But React and Vue.js still stand as the most popular among all the other alternatives. 

And although both are performant, elegant, and arguably easy to learn, they have some different opinions on how certain things should be done, and different ways of achieving the same end result.

I believe getting comfortable and efficient with a frontend framework is mostly about learning the patterns of doing regular stuff.

You know, how to listen to changes of a parameter/data and perform some action on that. And how to bind an event listener or data to an action object (button, checkbox, etc) and so on. 

While I was working on a side-project with React, I noticed that my mind was like: "Yeah, I could do it like this in Vue, I would emit an event from the child, then listen for it in the parent and update this data". And then I was Googling how to do something like that in React.

In this article, I am going to show you how to apply some common patterns in both React and Vue that you'll come across in your daily front-end work. Then you can use these recipes to easily transition from one framework to the other one.

This will be helpful whether you are an experienced Vue developer who needs to work on a React project or the other way around. I will be using modern React with hooks and the Vue Options API (Vue 2). 

I suggest cloning the [repository](https://github.com/yigiterinc/VueVsReact) that contains all the code I use in this article and rendering the respective components in each section and playing with them to really understand how they work. 

After cloning, you need to run **npm install** in the React and Vue folders. Then you can start the React project with **npm start** and the Vue project with **npm run serve**.

```
https://github.com/yigiterinc/VueVsReact
```

### Table of Contents

* [Component Structure in React vs Vue](#heading-component-structure)
* [How to use State in React and Vue](#heading-how-to-use-state)
* [How to Use Props in Vue and React](#heading-how-to-use-props)
* [How to Create Methods/Functions in Vue and React](#heading-how-to-create-methodsfunctions)
* [Styling Options](#heading-styling-options)
* [How to Bind Form Input to Data (State)](#heading-how-to-bind-form-input-to-data-state)
* [How to Handle Events (User Input)](#heading-handling-events-user-input)
* [Conditional Styling](#heading-conditional-styling)
* [Conditional Rendering](#heading-conditional-rendering)
* [Rendering Arrays (Lists)](#heading-rendering-arrays-lists)
* [Child to Parent Communication](#heading-child-to-parent-communication)
* [Reacting to Data/State Changes](#heading-reacting-to-datastate-changes)
* [Computed Properties vs useMemo](#heading-computed-properties-vs-usememo)
* [Vue Slots vs Render Props](#heading-vue-slots-vs-render-props)

<h2 id=1>Component Structure</h2>

Let's take a bird's eye look into some very basic components in both frameworks. We will extend this in the following sections.

In Vue, a Single File Component contains 3 parts: the template, script and style.

The template is the part that will be rendered. It contains the HTML of the component and has access to the data (and methods) in the scripts and the styles.

You can find everything about a component inside these sections in Vue.

```javascript
<template>
  <div id="structure">
    <h1>Hello from Vue</h1>
  </div>
</template>

<script>
export default {}
</script>

<!-- Use preprocessors via the lang attribute! e.g. <style lang="scss"> -->
<style>
#structure {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>

```

To get this component rendered without a router or other complicated things, you can add it to **App.vue.** I suggest you render every component as you follow along so you can see them in action:

```js
<template>
  <div id="app">
    <structure />
  </div>
</template>

<script>
import Structure from './Structure/Structure.vue'

export default {
  name: 'App',
  components: { Structure },
}
</script>

```

You will be changing the import component inside the **components** section and the tag name in the **template** section.

In React, a functional component is a function that returns [JSX](https://reactjs.org/docs/introducing-jsx.html) (an extension of JavaScript that allows you to use HTML tags inside JS code). You can think as if it is returning HTML to simplify things. The part that will be rendered used to be written inside the `render()` function in class-based React, if you are more familiar with that. 

As you progress in this tutorial, in each section you can put the respective components inside App.js to get them rendered like this:

```js
import React from 'react'

function Structure() {
  return <div>Render me App</div>
}

export default Structure

```

```js
import './App.css'

import Structure from './Structure/Structure'

function App() {
  return (
    <div className="App">
      <Structure />
    </div>
  )
}

export default App

```

So you will change the import and the component inside the div.

<h2 id=2>How to Use State</h2>

In Vue, we learned that the script tag contains the data and methods related to the component. The Vue Options API has special keywords (options) such as _data, methods, props, computed, watch,_ and _mixins_ that we can use, as well as lifecycle methods such as _created_ and _mounted_. 

We will use the `data` option to use state in our component. The data should be defined as a function which returns an object that contains our states. 

To access the state inside our HTML (template), we have to use double curly braces and write the name of our variable. Keep in mind that any change to data variables will result in a render if that variable is used (referenced) in the HTML.

```javascript
<template>
  <div>
    <h1>Hello {{ currentFramework }}</h1>
  </div>
</template>

<script>
export default {
  data() {
    return {
      currentFramework: ' Vue!',
      alternative: ' React!',
    }
  },
}
</script>

<!-- Use preprocessors via the lang attribute! e.g. <style lang="scss"> -->
<style></style>

```

In React, functional components used to be stateless. But thanks to hooks, we now have the `useState` hook to store state inside our component. To use the useState hook we have to import it, and the syntax is:

```javascript
import React, { useState } from 'react';


function App() {
    const [stateName, setStateName] = useState('default value'); 
}
```

We define the name of the state variable and name of its setter function inside the brackets, then we pass the default value of our variable to the useState hook. 

You can imagine the hook like this to understand the syntax better: It is like a function that creates a variable, sets its value to the passed value, then returns an array which contains the variable and its setter function. 

Note that you should use a single pair of curly parenthesis to switch to JavaScript scope and print a variable inside your JSX, instead of double parenthesis, which was the case with Vue.

```javascript
import { React, useState } from 'react'

function TestUseState() {
  const [frameworkName, setFrameworkName] = useState('React')

  return (
    <div>
      <h1>useState API</h1>
      <p>Current Framework: {frameworkName}</p>
    </div>
  )
}

export default TestUseState

```

<h2 id=3>How to Use Props</h2>

In Vue, we define props by adding the props option inside the object we export inside the script field like we did with the data option. It is a best practice to define the props as objects so we get more control over how they are used. 

For example, specify their types, default values, and make them required if necessary. Vue will show a warning if you use the component wrong, like calling it without passing a required prop. 

Let's say we have an Address child component that will be called from the `UserInfo` parent component.

```javascript
<template>
  <div class="address">
    <p>City: {{ city }}</p>
    <p>Street: {{ street }}</p>
    <p>House No: {{ houseNumber }}</p>
    <p>Postal Code: {{ postalCode }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {}
  },
  props: {
    city: {
      type: String,
      default: 'Munich',
    },
    street: {
      type: String,
      required: true,
    },
    houseNumber: {
      type: Number,
      required: true,
    },
    postalCode: {
      type: Number,
      required: true,
    },
  },
}
</script>

<style></style>

```

We can access our props just like our data variables – using the double parenthesis inside the template. And we can pass the props from the parent like this:

```javascript
<template>
  <div class="address">
    <p>Name: Yigit</p>
    <Address
      street="randomStrasse"
      :postalCode="80999"
      :houseNumber="32"
    ></Address>
  </div>
</template>

<script>
import Address from '@/components/Address.vue'

export default {
  data() {
    return {}
  },
  components: {
    Address,
  },
}
</script>

<style></style>

```

Notice how we use the v-bind shorthand `:` and write `:postalCode` and `:houseNumber` to indicate that these are not strings but Number type objects. We have to use this syntax whenever we need to pass anything other than a string (array, object, number, and so on). 

This might confuse you if you are coming from React, so you might want to read more about [v-bind](https://vuejs.org/v2/guide/class-and-style.html) to get a better understanding of how it works.

In React, we do not need to explicitly define what props will be passed in the child component. We can either use object destructuring to assign props to variables or access them using the props object. We access our props inside JSX, just like how we access the state.

```javascript
import React from 'react'

function Address({ city, street, postalCode, houseNumber }) {
  return (
    <div>
      <p>City: {city}</p>
      <p>Street: {street}</p>
      <p>Postal Code: {postalCode}</p>
      <p>House Number: {houseNumber}</p>
    </div>
  )
}

export default Address

```

And we can pass the props from the parent like this:

```javascript
import React from 'react'

function UserInfo() {
  return (
    <div>
      <p>Name: Yigit</p>
      <Address
        city="Istanbul"
        street="Ataturk Cad."
        postalCode="34840"
        houseNumber="92"
      ></Address>
    </div>
  )
}

export default UserInfo
```

<h2 id=4>How to Create Methods/Functions</h2>

In Vue, we define methods similarly to data – we can just put a methods option under the data and define the method. We can call these methods from the template and methods can access/modify our data.

```javascript
<template>
  <div>
    {{ sayHello() }}
  </div>
</template>

<script>
export default {
  data() {
    return {
      to: 'Methods',
    }
  },
  methods: {
    sayHello() {
      return 'Hello ' + this.to
    },
  },
}
</script>

<style></style>

```

Be careful when trying to access component methods or data properties from inside the exported object (code inside script tag). If you don't include the `this` keyword, Vue will show an error saying it does not know where that property/method is.

In React, things are a bit more simple. It is just the regular JS function definition, with ES6 syntax, if you'd like.

```javascript
import React from 'react'

function HelloFunctions() {
  const to = 'Functions'

  function sayHello() {
    return 'Hello ' + to
  }

  const sayHelloModern = () => 'Hello ' + to

  return (
    <div>
      {sayHello()}
      <br />
      {sayHelloModern()}
    </div>
  )
}

export default HelloFunctions

```

<h2 id=5>Styling Options</h2>

Styling Vue components is really simple. We just need to write our plain old CSS classes and selectors inside the `style` tag. 

Vue also supports scoped CSS by using the `scoped` keyword. It helps to avoid visual bugs caused by assigning the same class name inside different components. For example, you could name the main container in all your components `main-container` and only the styles in that component file would be applied to each main-container. 

```javascript
<template>
  <div class="main-container">
    <h3 class="label">I am a styled label</h3>
  </div>
</template>

<script>
export default {
  data() {
    return {}
  },
}
</script>

<style scoped>
.main-container {
  position: absolute;
  left: 50%;
  top: 45%;
  margin: 0;
  transform: translate(-50%, -50%);
  text-align: center;
}

.label {
  font-size: 30px;
  font-weight: 300;
  letter-spacing: 0.5rem;
  text-transform: uppercase;
}
</style>

```

In React, though, we have more options in terms of styling and it's basically up to your personal preference since there are multiple ways to style your components. I will suggest a few good options here.

### 1) Writing regular CSS in a .css file and importing it

This is probably the most basic and straightforward approach for applying styles to your React components. It does not mean it is a bad approach, as it allows you to write plain old CSS. It is a good method if you are a CSS guru who is just getting started with React. 

```javascript
import React from 'react'
import './styles.css'

function Styled() {
  return (
    <div>
      <h3 class="title">I am red</h3>
    </div>
  )
}

export default Styled

```

```css
.title {
  color: red;
  font-size: 30px;
}

```

### 2) Using Material UI (useStyles/makeStyles)

Material UI is a CSS framework that has so many reusable components. It also provides a way to style your components, which uses CSS in JS and therefore has its advantages such as scoped CSS. 

The `makeStyles` hook receives a list of classes in an object, then you can use those classes by assigning them to objects. 

```javascript
import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Button from '@material-ui/core/Button';

const useStyles = makeStyles({
  root: {
    background: 'linear-gradient(45deg, #FE6B8B 30%, #FF8E53 90%)',
    border: 0,
    borderRadius: 3,
    boxShadow: '0 3px 5px 2px rgba(255, 105, 135, .3)',
    color: 'white',
    height: 48,
    padding: '0 30px',
  },
});

export default function Hook() {
  const classes = useStyles();
  return <Button className={classes.root}>Hook</Button>;
}

```

### 3) Using Styled Components (CSS in JS)

[Styled components](https://styled-components.com/) are modern and easy to use and it allows you to take advantage of all the features of plain CSS as well. 

In my opinion, it is easier to use and more powerful than MaterialUI (you can also style MaterialUI components with this, instead of using `makeStyles`). It's also better than importing a CSS file since it is scoped and styled components are reusable.

```javascript
import React from 'react'
import styled, { css } from 'styled-components'

// Use Title and Wrapper like any other React component – except they're styled!
const Title = styled.h1`
  font-size: 2em;
  text-align: center;
  color: palevioletred;
`

// Create a Wrapper component that'll render a <section> tag with some styles
const Wrapper = styled.section`
  padding: 4em;
  background: papayawhip;
  height: 100vh;
`

function StyledComponent() {
  return (
    <Wrapper>
      <Title>Hello World!</Title>
    </Wrapper>
  )
}

export default StyledComponent

```

<h2 id=6>How to Bind Form Input to Data (State)</h2>
    

We have learned how to have state inside our components but we also need a way to bind user inputs to that state. For example in login forms, we will probably need to store the user's username and password input in the component state. React and Vue have different ways of keeping user inputs in sync with state.

In Vue we have a special directive for this operation called [v-model](https://vuejs.org/v2/guide/forms.html). To use this, you need to create a state by using the `data` property as we have learned before. Then you add the v-model keyword to your input and specify which data variable is responsible for storing this input (this is applicable to form input, textarea and select elements). 

This is a high-level and clean way to connect data, removing the need to create additional lambda functions or handlers. 

```javascript
<template>
  <div>
    <input v-model="inputState" type="text" />
    <br />
    {{ inputState }}
    <br />
    <button @click="changeInputState()">Click to say goodbye</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      inputState: 'Hello',
    }
  },
  methods: {
    changeInputState: function () {
      this.inputState = 'Goodbye'
    },
  },
}
</script>

<style></style>

```

Here is a small example: we have a text input, and we connect it to the `inputState` variable by using the v-model keyword. So whenever the user inputs text, the `inputState` variable will reflect the changes automatically. 

However, there is one special thing that you need to know: v-model implements **2-way data binding** in contrast to **1-way binding** in React. 

This means that, not only when you change the input does the data change, but also, if you change the data, the input value changes as well. 

To demonstrate this, I have created a button and connected it to a method. Don't worry about the event handling yet, we will see that in next section. When the button is clicked, the value of inputState variable is changed and the input also changes when that happens. 

I encourage you to try it yourself by running the code. Also, notice that the initial value of your input box is 'Hello' – it is not initialized to empty string or null because we set the `inputState` variable to 'Hello'.

Now let's see it in React:

```javascript
import { React, useState } from 'react'

function FormInputBinding() {
  const [userInput, setUserInput] = useState('Hello')

  return (
    <div>
      <input type="text" onChange={(e) => setUserInput(e.target.value)} />
      <button onClick={() => setUserInput('Goodbye')}>
        Click to say goodbye
      </button>
      {userInput}
    </div>
  )
}

export default FormInputBinding

```

This topic overlaps with handling user events so if you do not understand something, wait until you complete the next section. Here, we handle the `onChange` event manually and call the `setUserInput` function to set the state to the event's value. 

As we mentioned earlier, React uses a **1-way binding** model. This means that changing the userInput state will not affect the value we see inside the text input – we won't see Hello inside the input box initially. Also when we click the button, it will update the state but the input inside the box will maintain its value.

<h2 id=7>Handling Events (User Input)</h2>

Let's see another form that is closer to real-life cases in Vue and React:

```javascript
<template>
  <div>
    <input
      v-model="username"
      id="outlined-basic"
      label="Username"
      variant="outlined"
    />
    <input
      v-model="password"
      id="outlined-basic"
      type="password"
      label="Password"
      variant="outlined"
    />

    <input
      v-model="termsAccepted"
      id="outlined-basic"
      type="checkbox"
      label="Password"
      variant="outlined"
    />

    <Button variant="contained" color="primary" @click="submitForm">
      Submit
    </Button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: '',
      password: '',
      termsAccepted: false,
    }
  },
  methods: {
    submitForm: function () {
      console.log(this.username, this.password, this.termsAccepted)
    },
  },
}
</script>

<style></style>

```

As you can see, we are using the v-model property that we just learned about to connect all our inputs to data properties (state). So, whenever the inputs change, Vue automatically updates the corresponding variable. 

To see how we handle a click event on button, check the submit Button. We use the [v-on](https://vuejs.org/v2/guide/events.html) keyword to handle click event. `@click` is just a shorthand for `v-on:click`.

Whenever a click event happens it simply calls the `submitForm` method. You can familiarize yourself with the list of possible events by going through the linked docs.

In React, we can have a form like this:

```javascript
import { React, useState } from 'react'

import {
  TextField,
  Checkbox,
  FormControlLabel,
  Button,
} from '@material-ui/core'

function EventHandling() {
  let [username, setUsername] = useState('')
  let [password, setPassword] = useState('')
  let [termsAccepted, setTermsAccepted] = useState(false)

  const submitForm = () => {
    console.log(username, password, termsAccepted)
  }

  const formContainer = {
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    gap: '20px',
  }

  return (
    <div style={formContainer}>
      <TextField
        onInput={(e) => setUsername(e.target.value)}
        id="outlined-basic"
        label="Username"
        variant="outlined"
      />
      <TextField
        onInput={(e) => setPassword(e.target.value)}
        id="outlined-basic"
        type="password"
        label="Password"
        variant="outlined"
      />

      <FormControlLabel
        control={
          <Checkbox
            type="checkbox"
            checked={termsAccepted}
            onChange={(e) => setTermsAccepted(e.target.checked)}
          />
        }
        label="Accept terms and conditions"
      />

      <Button variant="contained" color="primary" onClick={() => submitForm()}>
        Submit
      </Button>
    </div>
  )
}

export default EventHandling
```

We create our state variables for each input. We can then listen to events on inputs and the event will be accessible inside the handler function. We call the state setters to update our state as a response to these events. 

<h2 id=8>Conditional Styling</h2>

Conditional Styling means binding a class or style to an element if a condition is true. 

In Vue it can be achieved like this:

```javascript
<template>
  <div>
    <button @click="toggleApplyStyles"></button>
    <p :class="{ textStyle: stylesApplied }">
      Click the button to {{ stylesApplied ? 'unstyle' : 'style' }} me
    </p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      stylesApplied: false,
    }
  },
  methods: {
    toggleApplyStyles: function () {
      this.stylesApplied = !this.stylesApplied
    },
  },
}
</script>

<style>
.textStyle {
  font-size: 25px;
  color: red;
  letter-spacing: 120%;
}
</style>

```

We create a paragraph and want to apply the `textStyle` class only when the `stylesApplied` data property's value is true. We can use v-bind to achieve this. The colon is the shorthand for v-bind so `:class` is same as `v-bind:class`. 

We use v-bind object syntax to bind classes. We pass an object to the class property: {textStyle: stylesApplied}, which means apply the `textStyle` class if `stylesApplied` is true. 

It is a bit complicated at the start but it helps us avoid multiple chained if statements to determine which class will be applied and handles style bindings in a clean way: class names on the left (object keys), conditions on the right (object values).

In React we have to do things more primitively.

```javascript
import { React, useState } from 'react'
import './styles.css'

function ConditionalStyling() {
  let [stylesApplied, setStylesApplied] = useState(false)

  return (
    <div>
      <button onClick={() => setStylesApplied(!stylesApplied)}>Click me</button>
      <p style={{ color: stylesApplied ? 'red' : 'green' }}>Red or Green</p>
      <p className={stylesApplied ? 'styleClass' : ''}>Red with class</p>
    </div>
  )
}

export default ConditionalStyling

```

Here we use plain JavaScript to bind either a styles object or a class name to the element. I think this complicates the code a bit, and I'm not a huge fan of this syntax.

<h2 id=9>Conditional Rendering</h2>

Sometimes, we want to render a component after some operation – such as fetching data from an API – is completed. Or maybe we want to display an error message if there is an error or success message if not. 

For such situations, we use conditional rendering to change the HTML to be rendered programmatically. 

In Vue, there are [special directives](https://vuejs.org/v2/guide/conditional.html) for that as well. We can use the `v-if` and `v-else` or even `v-else-if` for rendering templates based on conditions.

```javascript
<template>
  <div>
    <h2 v-if="condition1">condition1 is true</h2>
    <h2 v-else-if="condition2">condition2 is true</h2>
    <h2 v-else>all conditions are false</h2>
  </div>
</template>

<script>
export default {
  data() {
    return {
      condition1: false,
      condition2: false,
    }
  },
}
</script>

<style></style>
```

This syntax allows us to create complex chains of conditional rendering without complicating our template code with if else statements.

Here is one of the ways to accomplish the same output with React:

```javascript
import React from 'react'

function ConditionalRendering() {
  const condition1 = false
  const condition2 = false

  function getMessage() {
    let message = ''

    if (condition1) {
      message = 'condition1 is true'
    } else if (condition2) {
      message = 'condition2 is true'
    } else {
      message = 'all conditions are false'
    }

    return <h1>{message}</h1>
  }

  return <>{getMessage()}</>
}

export default ConditionalRendering

```

This is just plain JS and JSX, no magic here.

<h2 id=10>Rendering Arrays (Lists)</h2>

Now let's see how we can render list data. In Vue, there is `v-for` keyword for doing this. The syntax **name in names** means the name variable will always hold the current name. As the index changes, if index is 0, it is `names[0]` and so on. We can also access the index as specifying it inside the parentheses. The **v-for** directive also requires a key.

```javascript
<template>
  <div>
    <h1>Names</h1>
    <ul>
      <li v-for="(person, index) in people" :key="index">{{ person.name }}</li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      people: [
        {
          id: 0,
          name: 'Yigit',
        },
        {
          id: 1,
          name: 'Gulbike',
        },
        {
          id: 2,
          name: 'Mete',
        },
        {
          id: 3,
          name: 'Jason',
        },
        {
          id: 4,
          name: 'Matt',
        },
        {
          id: 5,
          name: 'Corey',
        },
      ],
    }
  },
}
</script>
```

Note that we can also use the **v-for** directive for iterating over properties of an object. Remember that, in JS, arrays are just a special subset of objects with number keys. 

In React, we will use the `Arrays.map` function to iterate over the array and return a JSX tag for each element.

```javascript
import React from 'react'

function RenderingLists() {
  const cities = [
    'Istanbul',
    'München',
    'Los Angeles',
    'London',
    'San Francisco',
  ]

  return (
    <div>
      <h1>Cities</h1>
      {cities.map((city, index) => (
        <h4 key={index}>{city}</h4>
      ))}
    </div>
  )
}

export default RenderingLists

```

<h2 id=11>Child to Parent Communication</h2>

Imagine you have a form component and a button sub-component inside it. And you want to perform some action when that button is clicked, like calling an API to submit data – but you do not have access to the form data in the button component since it is stored in the parent. What do you do?

Well, if you are in Vue, you want to emit a custom event from the child and act on that in the parent. In React, you would create the function that will be executed (when button is clicked) in the parent, where the function has access to form data and pass it to the button component so that it can call the parent's function. 

Let's see an example in Vue:

```javascript
<template>
  <div>
    <button @click="buttonClicked">Submit</button>
  </div>
</template>

<script>
export default {
  methods: {
    buttonClicked: function () {
      this.$emit('buttonClicked') // Emits a buttonClicked event to parent
    },
  },
}
</script>

<style></style>

```

In our child component, we have the button and on click we emit a `buttonClicked` event. We could also send data in this call. For example if this was a text input box instead of a button and had its own data, we could send that data to the parent with emit. 

In the parent component, we need to listen for the custom `buttonClicked` event that we just created.

```javascript
<template>
  <form action="#">
    <input v-model="username" type="text" />
    <child @buttonClicked="handleButtonClicked" />
  </form>
</template>

<script>
import Child from './Child.vue'

export default {
  components: { Child },
  data() {
    return {
      username: '',
    }
  },
  methods: {
    handleButtonClicked: function () {
      console.log(this.username)
    },
  },
}
</script>

<style></style>

```

We just added a `@buttonClicked` event to our child component call to handle this custom event. 

In React, we could achieve the same results by passing a handler function to the child component. The concept was a bit complicated to me first but the syntax is easier than the Vue example and there is no magic.

```javascript
import React from 'react'

function Child({ handleButtonClicked }) {
  return (
    <div>
      <button onClick={() => handleButtonClicked()}>Submit</button>
    </div>
  )
}

export default Child

```

We access the `handleButtonClicked` prop and call it when the button is clicked.

```javascript
import { React, useState } from 'react'

import Child from './Child.js'

function Parent() {
  const [username, setUsername] = useState('')

  const submitForm = () => {
    console.log(username)
    // Post form data to api...
  }

  return (
    <div>
      <input onChange={(e) => setUsername(e.target.value)} type="text" />
      <Child handleButtonClicked={submitForm} />
    </div>
  )
}

export default Parent

```

In the parent, we pass the `submitForm` function as the `handleButtonClicked` prop which will do the job.

<h2 id=12>Reacting to Data/State Changes</h2>

In some cases, we need to react to data changes. For example, when you want to perform asynchronous or expensive operations in response to a change in data.

 In Vue, we have `watch` properties or watchers for that. If you are familiar with `useEffect` in React, this is closest thing you can find in Vue and their use cases are more or less the same.

Let's see an example:

```javascript
<template>
  <div>
    <input v-model="number1" type="number" name="number 1" />
    <input v-model="number2" type="number" name="number 2" />
    {{ sum }}
  </div>
</template>

<script>
export default {
  data() {
    return {
      number1: 0,
      number2: 0,
      sum: 0,
    }
  },
  watch: {
    number1: function (val) {
      this.sum = parseInt(val) + parseInt(this.number2)
    },
    number2: function (val) {
      this.sum = parseInt(this.number1) + parseInt(val)
    },
  },
}
</script>

<style></style>

```

Here, we have `number1` and `number2` defined in our data properties. We have 2 respective inputs and we are printing the sum of those numbers and we want sum to update when any of the inputs change. 

Inside the `watch` property, we write the name of the variable we want to **watch**. In this case, we want to watch both number1 and number2. If the user enters an input, `v-model` will change the corresponding data variable and when that happens, the **watch** function for that variable will be triggered and the value of sum will be recalculated.

Note that, in a real application, you wouldn't need to use watch for this simple thing and you would just put sum inside `computed` instead. This is a made-up example to demonstrate how `watch` works. 

Before using `watch` with more complicated things like objects, arrays, and nested structures, I suggest reading [this article](https://michaelnthiessen.com/how-to-watch-nested-data-vue/) because you will probably need to learn some `watch` options like `deep` and `immediate`.

In React, we use the built-in `useEffect` hook to watch for changes.

```javascript
import { React, useState, useEffect } from 'react'

function ReactToDataChanges() {
  const [number1, setNumber1] = useState(0)
  const [number2, setNumber2] = useState(0)
  const [sum, setSum] = useState(0)

  useEffect(() => {
    console.log('I am here!')
    setSum(parseInt(number1) + parseInt(number2))
  }, [number1, number2])

  return (
    <div>
      <input
        onChange={(e) => setNumber1(e.target.value)}
        type="number"
        name="number 1"
      />
      <input
        onChange={(e) => setNumber2(e.target.value)}
        type="number"
        name="number 2"
      />
      {sum}
    </div>
  )
}

export default ReactToDataChanges

```

`useEffect` expects a function to run when a dependency changes as the first argument and a list of dependencies as the second argument. 

Keep in mind that this is also a made-up example to demonstrate `useEffect` (we could achieve the same without `useEffect` by taking the sum variable out of state).

I want to show a very common use case for this hook: fetching data from an API after the component loads:

```javascript
useEffect(() => {
    fetchUserData()
}, [])

const fetchUserData = async () => {
    const url = '';
    const response = await axios.get(url);
    const user = response.data;
    setUser(user);
}
```

We can specify empty array to run the `useEffect` once when the component renders. In Vue, we would do the same operation inside a lifecycle hook, such as `created` or `mounted`.

<h2 id=13>Computed Properties vs useMemo</h2>

Vue has a concept called computed properties, which serve the purpose of caching rather complex computations and re-evaluating their values whenever one of the dependencies change (similar to `watch`). 

It is also useful in keeping our templates clean and concise by moving the logic to **JavaScript**. In this case, they act like regular variables which we don't want to be a state.

```javascript
<template>
  <div>
    <h3>Yigit's Favorite Cities are:</h3>
    <p v-for="city in favCities" :key="city">{{ city }}</p>
    <h3>Yigit's Favorite Cities in US are:</h3>
    <p v-for="town in favCitiesInUS" :key="town">{{ town }}</p>
    <button @click="addBostonToFavCities">
      Why is Boston not in there? Click to add
    </button>
  </div>
</template>

<script>
export default {
  computed: {
    favCitiesInUS: function () {
      return this.favCities.filter((city) => this.usCities.includes(city))
    },
  },
  data() {
    return {
      favCities: [
        'Istanbul',
        'München',
        'Los Angeles',
        'Rome',
        'Florence',
        'London',
        'San Francisco',
      ],
      usCities: [
        'New York',
        'Los Angeles',
        'Chicago',
        'Houston',
        'Phoenix',
        'Arizona',
        'San Francisco',
        'Boston',
      ],
    }
  },
  methods: {
    addBostonToFavCities() {
      if (this.favCities.includes('Boston')) return
      
      this.favCities.push('Boston')
    },
  },
}
</script>

<style></style>

```

Here, we do not want to put the `favCitiesInUS` function inside our template because it is too much logic. 

Think of it like a function where the output will be cached. The function will be re-evaluated only if `favCities` or `usCities` (its dependencies) changes. To try that, you can click the button and see how the template changes. Keep in mind that computed functions do not receive any arguments.

We can use the `useMemo` hook to achieve the same result in React. We wrap the function in the useMemo hook and provide the list of dependencies in the second argument. Whenever one of those dependencies changes, React will run the function again.

```java
import { React, useMemo, useState } from 'react'

function UseMemoTest() {
  const [favCities, setFavCities] = useState([
      'Istanbul',
      'München',
      'Los Angeles',
      'Rome',
      'Florence',
      'London',
      'San Francisco',
    ]),
    [usCities, setUsCities] = useState([
      'New York',
      'Los Angeles',
      'Chicago',
      'Houston',
      'Phoenix',
      'Arizona',
      'San Francisco',
      'Boston',
    ])

  const favCitiesInUs = useMemo(() => {
    return favCities.filter((city) => usCities.includes(city))
  }, [favCities, usCities])

  return (
    <div>
      <h3>Yigit's Favorite Cities are:</h3>
      {favCities.map((city) => (
        <p key={city}>{city}</p>
      ))}
      <h3>Yigit's Favorite Cities in US are:</h3>
      {favCitiesInUs.map((town) => (
        <p key={town}>{town}</p>
      ))}
      <button onClick={() => setFavCities([...favCities, 'Boston'])}>
        Click me to add
      </button>
    </div>
  )
}

export default UseMemoTest

```

<h2 id=14>Vue Slots vs Render Props</h2>

We sometimes want to create generic components that can display other components inside of them, such as a grid component that displays any type of item inside it.

For that purpose, Vue has a mechanism called [slots](https://twitter.com/caglarcilara/status/1448905192045531143?s=20). The logic behind slots is really simple: you open a slot in the component which should receive another component to render (let's call it consumer, because it consumes the elements that are provided). 

In the producer, you pass the components that consumer should render inside its tags – you can think of them as filling the slots you opened in the consumer. The first element will be rendered in the first slot, the second in the second slot, and so on. 

If there is more than one slot, you have to set the names as well. Let's see an example:

```javascript
<template>
  <div>
    <h3>Component in slot 1:</h3>
    <slot name="slot1"></slot>
    <h3>Hello slot1</h3>
    <slot name="slot2"></slot>
    <h3>Component in slot 3:</h3>
    <slot name="slot3"></slot>
  </div>
</template>

<script>
export default {}
</script>

<style></style>

```

Here is our consumer component. It may be creating a layout or some composition from multiple components. We create the slots and give them distinct names.

```javascript
<template>
  <div>
    <consumer>
      <custom-button
        text="I am a button in slot 1"
        slot="slot1"
      ></custom-button>
      <h1 slot="slot2">I am in slot 2, yayyy</h1>
      <custom-button text="I am in slot 3" slot="slot3"></custom-button>
    </consumer>
  </div>
</template>

<script>
import CustomButton from './CustomButton.vue'
import Consumer from './Consumer.vue'

export default {
  components: {
    CustomButton,
    Consumer,
  },
}
</script>

<style></style>

```

And here is the producer passing the components to the slots of consumer by specifying their slot name as an attribute.

And here is the simple `CustomButton` component if you are interested in that:

```javascript
<template>
  <button>{{ text }}</button>
</template>

<script>
export default {
  props: {
    text: {
      type: String,
      default: 'I am a button component',
    },
  },
}
</script>

<style></style>

```

Can you guess the output without running the code? That might be a good exercise to make sure you understand slots.

In React, it is much simpler. I think the slots overcomplicate things a lot. As React uses JSX, we can just get away with passing the component to be rendered as a prop.

```js
import React from 'react'
import Child from './Child'

function Parent() {
  const compToBeRendered = (
    <div>
      <h1>Hello</h1>
      <button>Im button</button>
    </div>
  )

  return (
    <div>
      <Child compToBeRendered={compToBeRendered}></Child>
    </div>
  )
}

export default Parent

```

```js
import React from 'react'

function Child({ compToBeRendered }) {
  return (
    <div>
      <h1>In child:</h1>
      {compToBeRendered}
    </div>
  )
}

export default Child

```

## Final Thoughts

In this last section of the article, I would like to share my two cents on these frameworks. 

As we have seen through the article, Vue usually has its own way of doing things and has different constructs for most things. Sometimes this makes it a bit harder to get started with in my opinion. 

On the other hand, React is like pure JS, blended with JSX: not much magic and not many special keywords to learn. 

Although it may be not be the most beginner-friendly framework, I believe that the abstractions/keywords Vue provides (such as v-for, v-if and the Options API) allow you to write code at a higher level of abstraction (think of adding a simple statement to iterate over components versus a low level, multi-line map function).

These features also make your Vue code more structured and clean because the framework is opinionated. So it has its own ways of doing things, and if you do things that way, you will end up with code that is easy to read and understand.

React, on the other hand, is not very opinionated about things and provides developers with a lot of freedom to decide the structure of their project themselves.

But this freedom comes with a cost: if you are a beginner who is not aware of best practices, it is easy to end up with messy code and a poorly structured project. 

Another important difference in my opinion is this: if you are going to build a non-fundamental project with React, you will need to use a lot of external libraries to develop at a normal speed, which means you will need to learn how those things work as well.

## Conclusion

Thank you for reading and I hope this comparison was useful. If you would like to connect, ask questions, or discuss further, feel free to send me a message on [LinkedIn](https://www.linkedin.com/in/yigit-erinc/). 

