---
title: 'How to Test React Components: the Complete Guide'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-11T21:18:12.000Z'
originalURL: https://freecodecamp.org/news/testing-react-hooks
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/photo-1562679817-2aac4f5581ec.jpg
tags:
- name: Jest
  slug: jest
- name: React
  slug: react
- name: react testing library
  slug: react-testing-library
- name: Software Testing
  slug: software-testing
seo_title: null
seo_desc: 'By Mohammad Iqbal

  When I first started learning to test my apps back in the day, I would get very
  frustrated with the different types, styles and technologies used for testing, along
  with the disbanded array of blog posts, tutorials and articles. I f...'
---

By Mohammad Iqbal

When I first started learning to test my apps back in the day, I would get very frustrated with the different types, styles and technologies used for testing, along with the disbanded array of blog posts, tutorials and articles. I found this to be true as well for React testing. 

So I decided to just write a complete React testing guide in one article. 

Complete Guide, huh, are you going to cover every possible testing scenario? Of course not. However, it will be a complete foundational guide to testing and will be enough to build off of for most other edge cases.

Also I have curated an extensive collection of blog posts, articles and tutorials in the further reading section at the end that should give you enough knowledge to be in the top 10% of developers in terms of testing.

You can find the completed project here:

[https://github.com/iqbal125/react-hooks-testing-complete](https://github.com/iqbal125/react-hooks-testing-complete)  


## Table of Contents

	 **Theory**

*  What is Testing?   
*  Why Test? 
*  What to Test? 
*  What Not to Test? 
*  How I test
*  Shallow vs Mount
*  unit vs integration vs e to e

	**Preliminary Info**

* a few odds and ends

	**Enzyme**

* Enyme Setup
* react-test-renderer
* snapshot testing
* testing implementation details

	**React Testing Library**

* useState and props 
* useReducer()
* useContext()
* Controlled component Forms
* useEffect() and Axios API requests

	**Cypress** 

* A complete end to end test

	**Continuous Integration**

* Travis.yml
* Code Coverage with coveralls 

## Theory

### What is testing?

Let's start at the beginning and discuss what testing is. Testing is a 3 step process that looks like this:

![Image](https://www.freecodecamp.org/news/content/images/2019/07/image-12.png)

Arrange, your app is in a certain original state. Act, then something happens (click event, input, etc.). Then you assert, or make a hypothesis, of the new state of your app. The tests will pass if your hypothesis is correct and fail if it is wrong. 

Unlike your react components, your tests are not executed in the browser. Jest is the test runner and testing framework used by React. Jest is the environment where all your tests are actually executed. This is why you do not need to import `expect` and `describe` into this file. These functions are already available globally in the jest environment. 

Your tests syntax will look something like this:

```javascript
describe('Testing sum', () => {
    function sum(a, b) {
       return a + b;
    }

    it('should equal 4',()=>{
       expect(sum(2,2)).toBe(4);
      })

    test('also should equal 4', () => {
        expect(sum(2,2)).toBe(4);
      }) 
});
```

`describe` wraps our `it` or `test` blocks, and is a way to group our tests. Both `it` and `test` are keywords and can be used interchangeably. The string will be something that should happen with your tests and will be printed to the console. `toBe()` is a matcher that works with expect to allow you to make assertions. There are many more matchers and global variables offered by jest, see the links below for a complete list. 

[https://jestjs.io/docs/en/using-matchers](https://jestjs.io/docs/en/using-matchers)

[https://jestjs.io/docs/en/api](https://jestjs.io/docs/en/api)

###   
  
Why test?

Testing is done to ensure that your app will work as intended for your end users. Having tests will make your app more robust and less error prone. It is a way to verify that the code is doing what the developers intended. 

Potential Drawbacks:

* Writing tests is time consuming and difficult. 
* In certain scenarios executing tests in CI can cost actual money. 
* If done incorrectly, it can give you false positives. Your tests pass, but your app doesn’t function as intended. 
* Or false negatives. Your tests fail but your app is functioning as intended.



### What to test?

To build upon the previous point, Your tests should test the functionality of the app, that mimic how it will be used by your end users. This will give you confidence that your app will function as intended in your production environment.  We will of course go into much more detail through out this article but this is the basic gist of it. 

### What not to test?

I like to use Kent C dodds philosophy here that you shouldn’t test implementation details. 

Implementation details meaning testing things that are not end user functionality. We will see an example of this in the Enzyme section below. 

It seems that you are testing functionality there but you are actually not. You are testing the name of the function. Because you can change the name of the function and your tests will break but your app will still work giving you a false negative. 

Constantly having to worry about function and variable names is a headache, and having to rewrite tests every time you change them is tedious, I will show you a better approach. 

**Const variables:** these are unchanging variables, no need to test them.    

**Third party libraries:** It is not your job to test these libraries. It is up to the creators of these libraries to test it. If you are not sure if a library is tested you should not use it. Or you can read the source code to see if the author included tests. You can download the source code and run these tests yourself. You can also ask the author if their library is production ready or not.     


### My personal philosophy on testing

A lot of my testing philosophy is based on Kent C dodds teachings so you will see a lot of his sentiments echoed here, but I some of my own thoughts as well.

Many integration tests. No snapshot tests. Few unit tests. Few e to e tests. 

Unit testing is step above snapshot testing but its not ideal. It is however much easier to understand and maintain then snapshot testing. 

Write mostly integration tests. Unit tests are good but they don't really resemble the way your end user interacts with your app. It is very easy to test implementation details with unit tests, especially with shallow render.  

Integration tests should mock as little as possible

Do not test implementation details such as names of functions and variables. 

For example if we are testing a button and change the name of the function in the onClick method from increment() to handleClick() our tests would break but our component will still function. This is bad practice because we are basically just testing the name of the function which is an implementation detail, which our end user does not care about.



### Shallow vs mount

Mount actually executes the html, css and js code like a browser would, but does so in a simulated way. It is “headless” for example, meaning it doesn’t render or paint anything to a UI, but acts as a simulated web browser and executes the code in the background. 

Not spending time painting anything to the UI makes your tests much faster. However mount tests are still much slower than shallow tests. 

This is why you unmount or cleanup  the component after each test, because it’s almost a live app and one test will affect another test. 

Mount/render is typically used for integration testing and shallow is used for unit testing.

shallow rendering only renders the single component we are testing. It does not render child components. This allows us to test our component in isolation. 

For example consider this child and parent component.

```javascript
import React from 'react';

const App = () => {
  return (
    <div> 
      <ChildComponent /> 
    </div> 
  )
}

const ChildComponent = () => {
  return (
    <div>
     <p> Child components</p>
    </div>
  )
}
```

If we used shallow rendering of `App.js` we would get something like this, notice none of the DOM nodes for the child component are present, hence the term shallow render. 

```
<App>
  <div> 
    <ChildComponent /> 
  </div>
</App> 
```

Now we can compare this to mounting the component: 

```
<App>
  <div> 
    <ChildComponent> 
      <div>
       <p> Child components</p>
      </div>
    </ChildComponent>
   </div>
</App> 
```

What we have above is much closer to what our app will look like in the browser, hence the superiority of mount/render. 

### unit vs integration vs end to end

**unit testing**: testing an isolated part of your app, usually done in combination with shallow rendering. example: a component renders with the default props.

**integration testing:** testing if different parts work or integrate with each other. Usually done with mounting or rendering a component. example: test if a child component can update context state in a parent. 

**e to e testing**: Stands for end to end. Usually a multi step test combining multiple unit and integration tests into one big test. Usually very little is mocked or stubbed. Tests are done in a simulated browser, there may or may not be a UI while the test is running. example: testing an entire authentication flow.



## Preliminary Info

**react-testing-library:** I personally like to use react-testing-library but the common way is to use Enzyme. I will show you one example of Enzyme because it is important to be aware of Enzyme at a basic level and the rest of the examples with react-testing-library. 

**Examples Outline:** Our examples will follow a pattern. I will first show you the React component and then the tests for it, with detailed explanations of each. You can also follow along with the repo linked at the beginning. 

**Configuration:** I will also assume you are using create-react-app with the default testing setup with jest so I will skip manual configurations.

**Sinon, mocha, chai:** A lot of the functionality offered by sinon is available by default with jest so you dont need sinon. Mocha and chai are a replacement for jest. Jest comes pre configured out of the box to work with your app, so it doesnt make sense to use Mocha and chai.

**Components Naming scheme:** My naming scheme for the components is `<TestSomething />` but that does not mean they are fake components in any way. They are regular React components, this is just the naming scheme.

**npm test and jest watch mode**: `yarn test`   worked for me. `npm test` did not work correctly with jest watch mode.

**testing a single file:** `yarn test` name of file

**React Hooks vs Classes:** I use React Hooks components for most of the examples but due to the power of react-testing-library all these tests will directly work with class components as well. 

With the preliminary background info out of the way we can go over some code.



## Enzyme

### Enzyme Setup

Our third party libraries

`npm install enzyme enzyme-to-json  enzyme-adapter-react-16`

Lets first start with our imports

```javascript
import React from 'react';
import ReactDOM from 'react-dom';
import Basic from '../basic_test';

import Enzyme, { shallow, render, mount } from 'enzyme';
import toJson from 'enzyme-to-json';
import Adapter from 'enzyme-adapter-react-16';

Enzyme.configure({ adapter: new Adapter() })
```

We will start with our basic imports Our first 3 imports are for react and our component. 

After this we import Enzyme. Then we import the toJson function from the 'enzyme-to-json' library. We will need this to convert our shallow rendered component into JSON which can be saved to the snapshot file. 

Finally we import our Adapter to make enzyme work with react 16 and initialize it as shown above. 

  
react-test-renderer

React actually comes with its own test renderer you can use instead of enzyme and the syntax will look like this. 

```javascript
// import TestRenderer from 'react-test-renderer';
// import ShallowRenderer from 'react-test-renderer/shallow';


// Basic Test with React-test-renderer
// it('renders correctly react-test-renderer', () => {
//   const renderer = new ShallowRenderer();
//   renderer.render(<Basic />);
//   const result = renderer.getRenderOutput();
//
//   expect(result).toMatchSnapshot();
// });
```

But even the react-test-render docs suggest using enzyme instead because it has a slightly nicer syntax and does the same thing. Just something to be aware of.   


### SnapShot Testing

Now our first test which is a snapshot test

```javascript
it('renders correctly enzyme', () => {
  const wrapper = shallow(<Basic />)

  expect(toJson(wrapper)).toMatchSnapshot();
});
```

If you have not ran this command before, a __snapshots__ folder and test.js.snap file will be created for you automatically. On every subsequent test the new snapshot will be compared to the existing snapshot file. The test will pass if the snapshot has not changed and fail if it has changed.

So essentially snapshot testing allows you to see how your component has changed since the last test, line for line. The lines of code that have changed is known as the diff.

Here is our basic component we are snapshot testing: 

```
import React from 'react';


const Basic = () => {
  return (
    <div >
      <h1> Basic Test</h1>
         <p> This is a basic Test Component</p>
    </div>
  );
}

export default Basic;
```

  
Running the above test will generate a file that will look like this. This is essentially our tree of React DOM nodes. 

```
// Jest Snapshot v1, https://goo.gl/fbAQLP

exports[`renders correctly enzyme 1`] = `
<div>
  <h1>
     Basic Test
  </h1>
  <p>
     This is a basic Test Component
  </p>
</div>
`;
```

And will produce a folder structure that will look like this: 

![Image](https://www.freecodecamp.org/news/content/images/2019/07/image-6.png)

  
Your terminal output will look like this:

![Image](https://www.freecodecamp.org/news/content/images/2019/07/image-7.png)

However what happens if we changed our basic component to this

```
import React from 'react';


const Basic = () => {
  return (
    <div >
      <h1> Basic Test</h1>

    </div>
  );
}

export default Basic;
```

Our snapshots will now fail   


![Image](https://www.freecodecamp.org/news/content/images/2019/07/image-8.png)

And will also give us the diff

![Image](https://www.freecodecamp.org/news/content/images/2019/07/image-9.png)

Just like in git the " - " before each line means it was removed. 

We just need to press "w" to activate watch mode then press "u" to update the snapshot. 

our snap shot file will be automatically updated with the new snapshot and will pass our tests 

```
// Jest Snapshot v1, https://goo.gl/fbAQLP

exports[`renders correctly enzyme 1`] = `
<div>
  <h1>
     Basic Test
  </h1>
</div>
`;
```

  
This is it for snapshot testing but if you read my personal thoughts section you know I dont snapshot test. I included it here because like Enzyme it is very common and something you should be aware of, but below I'll try to explain why I dont use it.  

Let's go over again what snapshot testing is. It essentially allows you to see how your component has changed since the last test. What are the benefits of this. 

* Its very quick and easy to implement and sometimes requires only a few lines of code. 
* You can see if our component is rendering correctly. You can see the DOM nodes clearly with the .debug() function.  
  


**Cons, Arguments against snapshot testing:**

* The only thing a snapshot test does is tell you whether the syntax of your code has changed since the last test. 
* So what is it really testing? Some would argue not much.
* Also basic rendering of the app correctly is React’s job so you're going a little into testing a third party library territory. 
* Also comparing diffs can be done with git version control. This should not be the job of snapshot testing.
* A failed test doesn’t mean your app isn’t working as intended, only that your code has changed since the last time you ran the test. This can lead to a lot of false negatives and a lack of trust in the test. This can also lead to people just updating the test without looking too closely at it. 
* Snapshot testing also tells you if your JSX is syntactically correct, but again this can be easily done in the dev environment. Running a snapshot test just to check syntax errors doesnt make any sense. 
* It can become hard to understand what’s happening in a Snapshot test, since most people use snapshot testing with shallow rendering, which doesnt render child components so it doesnt give the developer any insights at all.    


See the further reading section for more info



### Testing Implementation details with Enzyme

Here I will give an example on why not to test implementation details. Say we have simple counter component like so: 

```javascript
import React, { Component } from 'react';


class Counter extends Component {
  constructor(props) {
    super(props)

    this.state = {
      count: 0
    }
  }

  increment = () => {
    this.setState({count: this.state.count + 1})
  }

  //This incorrect code will still cause tests to pass
  // <button onClick={this.incremen}>
  //   Clicked: {this.state.count}
  // </button>

  render() {
    return (
      <div>
        <button className="counter-button" onClick={this.incremen}>
          Clicked: {this.state.count}
        </button>
      </div>
  )}
}

export default Counter;
```

You will notice I have a comment suggesting that a non-working app will still cause the tests to pass, for example by misspelling the name of the function in the onClick event. 

And let's see the tests which will make it clear why. 

```javascript
import React from 'react';
import ReactDOM from 'react-dom';
import Counter from '../counter';

import Enzyme, { shallow, render, mount } from 'enzyme';
import toJson from 'enzyme-to-json';
import Adapter from 'enzyme-adapter-react-16';

Enzyme.configure({ adapter: new Adapter() })

// incorrect function assignment in the onClick method
// will still pass the tests.

test('the increment method increments count', () => {
  const wrapper = mount(<Counter />)

  expect(wrapper.instance().state.count).toBe(0)

  // wrapper.find('button.counter-button').simulate('click')
  // wrapper.setState({count: 1})
  wrapper.instance().increment()
  expect(wrapper.instance().state.count).toBe(1)
})

```

Running the above code will pass the tests. So will using `wrapper.setState()`. So we have passing tests with a non functional app. I dont know about you but this doesnt give me confidence that our app will function as intended for our end users. 

Simulating click on the button will not pass the tests but it might give us the opposite problem, a false negative. Say we want to change the styling on the button by declaring a new CSS class for it, a very common situation. Our tests will now fail because we cant find our button anymore but our app will still be working, giving us a false negative. This is also true whenever we change the names of our functions or state variables.  

Every time we want to change our function and CSS class names we have to rewrite our tests, a very inefficient and tedious process. 

So what can we do instead? 

## React-testing-library

### useState

From the react-testing-library docs we see that the main guiding principle is 

> The more your tests resemble the way your software is used the more confidence they can give you. 

We will keep this guiding principle in mind as we explore further with our tests. 

Let's start with a basic React Hooks component and test the state and props. 

```javascript
import React, { useState } from 'react';


const TestHook = (props) => {
  const [state, setState] = useState("Initial State")

  const changeState = () => {
    setState("Initial State Changed")
  }

  const changeNameToSteve = () => {
    props.changeName()
  }

  return (
  <div>
    <button onClick={changeState}>
      State Change Button
    </button>
    <p>{state}</p>
    <button onClick={changeNameToSteve}>
       Change Name
    </button>
    <p>{props.name}</p>
  </div>
  )
}


export default TestHook;
```

Our props are coming from the root parent component

```javascript
  const App = () => {
      const [state, setState] = useState("Some Text")
      const [name, setName] = useState("Moe")
  ...
      const changeName = () => {
        setName("Steve")
      }

      return (
        <div className="App">
         <Basic />
        <h1> Counter </h1>
         <Counter />
        <h1> Basic Hook useState </h1>
         <TestHook name={name} changeName={changeName}/>
    ...     
```

So keeping our guiding principle in mind, what will our tests look like? 

The way our end user will use this app will be to: see some text on the UI, see the text in the button, then click on it, finally see some new text on UI. 

This is how we will write our tests using the React testing library. 

Use this command to install react testing library. 

`npm install @testing-library/react`

**not** 

`npm install react-testing-library`

Now for our tests

```javascript
import React from 'react';
import ReactDOM from 'react-dom';
import TestHook from '../test_hook.js';
import {render, fireEvent, cleanup} from '@testing-library/react';
import App from '../../../App'

afterEach(cleanup)

it('Text in state is changed when button clicked', () => {
    const { getByText } = render(<TestHook />);

    expect(getByText(/Initial/i).textContent).toBe("Initial State")

    fireEvent.click(getByText("State Change Button"))

    expect(getByText(/Initial/i).textContent).toBe("Initial State Changed")
 })


it('button click changes props', () => {
  const { getByText } = render(<App>
                                <TestHook />
                               </App>)

  expect(getByText(/Moe/i).textContent).toBe("Moe")

  fireEvent.click(getByText("Change Name"))

  expect(getByText(/Steve/i).textContent).toBe("Steve")
})
```

We first start with our usual imports.

Next we have the `afterEach(cleanup)` function. Since we are not using shallow render we have to unmount or cleanup after every test. And this is exactly what this function is doing. 

`getByText` is the query method we get by using object destructuring on the value of the render function. There are several more query methods but this is the one you will want to use most of the time.

To test our state notice we are not using any function names or the names of our state variables. We are keeping with our guiding principle and not testing implementation details. Since a user will see the text on the UI, this is how we will query the DOM nodes. We will also query the button this way and click it. Finally we will query the final state based on the text as well. 

`(/Initial/i)` is a regex expression that returns the first node that at least contains the text "Initial".  

We can do the same exact thing with props as well. Since the **props** are going to be changed in `App.js` we will need to render it along with our component. Like the previous example we are not using function and variable names. We are testing the same way a user would use our app and that is through the text they will see. 

Hopefully this gives you a good idea of how to test with the `react-testing-library` and the guiding principle, you generally want to use `getByText` most of the time. There are a few exceptions we will see as we continue further. 



### useReducer

Now we can test a component with the useReducer hook. We will of course need actions and reducers to work with our component so let's set them up like so: 

Our reducer

```javascript
import * as ACTIONS from './actions'

export const initialState = {
    stateprop1: false,
}

export const Reducer1 = (state = initialState, action) => {
  switch(action.type) {
    case "SUCCESS":
      return {
        ...state,
        stateprop1: true,
      }
    case "FAILURE":
      return {
        ...state,
        stateprop1: false,
      }
    default:
      return state
  }
}
```

And the actions: 

```



export const SUCCESS = {
  type: 'SUCCESS'
}

export const FAILURE = {
  type: 'FAILURE'
}


```

we will keep things simple and use actions instead of action creators. 

And finally the component that will use these actions and reducers: 

```javascript
import React, { useReducer } from 'react';
import * as ACTIONS from '../store/actions'
import * as Reducer from '../store/reducer'


const TestHookReducer = () => {
  const [reducerState, dispatch] = useReducer(Reducer.Reducer1, Reducer.initialState)

  const dispatchActionSuccess = () => {
    dispatch(ACTIONS.SUCCESS)
  }

  const dispatchActionFailure = () => {
    dispatch(ACTIONS.FAILURE)
  }


  return (
    <div>
       <div>
        {reducerState.stateprop1
           ? <p>stateprop1 is true</p>
           : <p>stateprop1 is false</p>}
       </div>
       <button onClick={dispatchActionSuccess}>
         Dispatch Success
       </button>
    </div>
  )
}


export default TestHookReducer;

```

This is a simple component that will change `stateprop1` from false to true by dispatching a `SUCCESS` action.

And now for our test. 

```javascript
import React from 'react';
import ReactDOM from 'react-dom';
import TestHookReducer from '../test_hook_reducer.js';
import {render, fireEvent, cleanup} from '@testing-library/react';
import * as Reducer from '../../store/reducer';
import * as ACTIONS from '../../store/actions';


afterEach(cleanup)

describe('test the reducer and actions', () => {
  it('should return the initial state', () => {
    expect(Reducer.initialState).toEqual({ stateprop1: false })
  })

  it('should change stateprop1 from false to true', () => {
    expect(Reducer.Reducer1(Reducer.initialState, ACTIONS.SUCCESS ))
      .toEqual({ stateprop1: true  })
  })
})

it('Reducer changes stateprop1 from false to true', () => {
   const { container, getByText } = render(<TestHookReducer />);

   expect(getByText(/stateprop1 is/i).textContent).toBe("stateprop1 is false")

   fireEvent.click(getByText("Dispatch Success"))

   expect(getByText(/stateprop1 is/i).textContent).toBe("stateprop1 is true")
})
```

We first start off by testing our reducer. And we can wrap the tests for the reducer in the `describe` block. These are fairly basic tests we are using to make sure the **initial state** is what we want and the actions produce the output we want. 

You can make an argument that testing the reducer is testing implementation details, but I found in practice that testing actions and reducers is one unit test that is always necessary. 

This is a simple example so it doesn't seem like its a big deal but in larger more complex apps not testing reducers and actions can prove disastrous. So actions and reducers would be one exception to the testing implementation details rule.

Next we have our tests for the actual component. Notice again here we are not testing implementation details. We use the same pattern from the previous useState example we are getting our DOM nodes by the text and also finding and clicking the button with the text as well. 

### useContext

Let's now move on and test if a child component can update the context state in a parent component. This may seem complex but it is rather simple and straight forward. 

We will first need our context object that we can initialize in its own file. 

```javascript
import React from 'react';

const Context = React.createContext()

export default Context

```

We also need our parent app component which will hold the Context provider. The value passed down to the `Provider` will be the state value and the `setState` function of the `App.js` component. 

```javascript
import React, { useState } from 'react';
import TestHookContext from './components/react-testing-lib/test_hook_context';


import Context from './components/store/context';


const App = () => {
  const [state, setState] = useState("Some Text")
  

  const changeText = () => {
    setState("Some Other Text")
  }


  return (
    <div className="App">
    <h1> Basic Hook useContext</h1>
     <Context.Provider value={{changeTextProp: changeText,
                               stateProp: state
                                 }} >
        <TestHookContext />
     </Context.Provider>
    </div>
  );
}

export default App;
```

And for our component

```javascript
import React, { useContext } from 'react';

import Context from '../store/context';

const TestHookContext = () => {
  const context = useContext(Context)

  return (
    <div>
    <button onClick={context.changeTextProp}>
        Change Text
    </button>
      <p>{context.stateProp}</p>
    </div>
  )
}


export default TestHookContext;
```

We have a simple component that displays the text we initialized in `App.js` and also we pass the `setState` function to the `onClick` method. 

**Note:** The state is changed, initialized and contained in our `App.js` component. We have simply passed down the state value and `setState` function to our child component through context, but ultimately the state is handled in the `App.js` component. This will be important to understanding our test. 

And our test: 

```javascript
import React from 'react';
import ReactDOM from 'react-dom';
import TestHookContext from '../test_hook_context.js';
import {act, render, fireEvent, cleanup} from '@testing-library/react';
import App from '../../../App'

import Context from '../../store/context';

afterEach(cleanup)

it('Context value is updated by child component', () => {

   const { container, getByText } = render(<App>
                                            <Context.Provider>
                                             <TestHookContext />
                                            </Context.Provider>
                                           </App>);

   expect(getByText(/Some/i).textContent).toBe("Some Text")

   fireEvent.click(getByText("Change Text"))

   expect(getByText(/Some/i).textContent).toBe("Some Other Text")
})

```

Even for context you can see we don't break our pattern of tests, we still find and simulate our events with the text. 

I have included the `<Context.Provider/>` and `<TestHookContext />`  components in the render function because it makes the code easier to read but we actually dont need either of them. Our test will still work if we passed only the `<App />` component to the render function. 

```
const { container, getByText } = render(<App/>) 
```

Why is this the case? 

Let's think back to what we know about context. All the context state is handled in `App.js`, for this reason this is the main component we are actually testing, even though it seems like we are testing the child component that uses the **useContext** Hook. This code also works because of **mount/render**. As we know in shallow render the child components are **not rendered**, but in mount/render they are. Since `<Context.Provider />` and `<TestHookContext />` are both child components of `<App />` they are rendered automatically.  



### Controlled component Forms

A controlled component form essentially means the form will work through the React state instead of the form maintaining its own state. Meaning the `onChange` handler will save the input text to the React state on every keystroke. 

Testing the form will be a little bit different than what we have seen so far, but we will try to still keep our guiding principle in mind. 

```javascript
import React, { useState } from 'react';

const HooksForm1 = () => {
  const [valueChange, setValueChange] = useState('')
  const [valueSubmit, setValueSubmit] = useState('')

  const handleChange = (event) => (
    setValueChange(event.target.value)
  );

  const handleSubmit = (event) => {
    event.preventDefault();
    setValueSubmit(event.target.text1.value)
  };

    return (
      <div>
       <h1> React Hooks Form </h1>
        <form data-testid="form" onSubmit={handleSubmit}>
          <label htmlFor="text1">Input Text:</label>
          <input id="text1" onChange={handleChange} type="text" />
          <button type="submit">Submit</button>
        </form>
        <h3>React State:</h3>
          <p>Change: {valueChange}</p>
          <p>Submit Value: {valueSubmit}</p>
        <br />
      </div>
    )
}


export default HooksForm1;
```

This is a basic form we have here and we also display the value of the change and submit value in our JSX. We have the `data-testid="form"`  attribute which we will use in our test to the query for the form. 

And our tests: 

```javascript
import React from 'react';
import ReactDOM from 'react-dom';
import HooksForm1 from '../test_hook_form.js';
import {render, fireEvent, cleanup} from '@testing-library/react';

afterEach(cleanup)

//testing a controlled component form.
it('Inputing text updates the state', () => {
    const { getByText, getByLabelText } = render(<HooksForm1 />);

    expect(getByText(/Change/i).textContent).toBe("Change: ")

    fireEvent.change(getByLabelText("Input Text:"), {target: {value: 'Text' } } )

    expect(getByText(/Change/i).textContent).not.toBe("Change: ")
 })


 it('submiting a form works correctly', () => {
     const { getByTestId, getByText } = render(<HooksForm1 />);

     expect(getByText(/Submit Value/i).textContent).toBe("Submit Value: ")

     fireEvent.submit(getByTestId("form"), {target: {text1: {value: 'Text' } } })

     expect(getByText(/Submit Value/i).textContent).not.toBe("Submit Value: ")
  })
```

Since an empty input element does not have text, we will use a `getByLabelText()` function to get the input node. This will still be keeping with our guiding principle, since the label text is what the user will read before inputting text. 

Notice we will fire the `.change()` event instead of the usual `.click()` event. We also pass in dummy data in the form of: 

`{ target: { value: "Text" } }` 

Since the value from the form will be accessed in the form of `event.target.value`, this is what we pass to the simulated event. 

Since we will generally not know what the text is the user will submit, we can just use a `.not` keyword to make sure the text has changed in our render method. 

We can test the submitting of the form in a similar way.  The only difference is we use the `.submit()` event and pass in dummy data in this way: 

`{ target: { text1: { value: 'Text' } } }` 

This is how to access form data from the synthetic event when a user submits a form. where `text1` is the id of our input element. We will have to break our pattern a little bit here, and use the `data-testid="form"`   attribute to query for the form since there is really no other way to get the form.  

And thats it for the form. It isnt that different from our other examples. If you think you got it, let's move onto something a little more complex. 

### 

### useEffect and API requests with axios

Let's now see how we would test the **useEffect hook** and API requests. This will be fairly different than what we have seen so far. 

Say we have a url passed down to a child component from the root parent. 

```javascript

...

     <TestAxios url='https://jsonplaceholder.typicode.com/posts/1' />
     
 ... 
```

And the component itself. 

```javascript
import React, { useState, useEffect } from 'react';
import axios from 'axios';


const TestAxios = (props) => {
  const [state, setState] = useState()

  useEffect(() => {
    axios.get(props.url)
      .then(res => setState(res.data))
  }, [])


  return (
    <div>
    <h1> Axios Test </h1>
        {state
          ? <p data-testid="title">{state.title}</p>
          : <p>...Loading</p>}
    </div>
  )
}


export default TestAxios;
```

We simply make an API request and save the results in the local state. We also use a ternary expression in our render method to wait until the request is complete to display the title data from json placeholder. 

You will notice we will again out of necessity have to make use of the `data-testid` attribute, and again it is an implementation detail since a user will not see or interact with this attribute in any way, but this is more realistic, since we will generally not know the text from a API request beforehand. 

We will also be using mocks in this test. 

A **mock** is way to simulate behavior we dont actually want to do in our tests. For example we mock API requests because we dont want to make real requests in our tests. 

We dont want to make real API requests in our tests for various reasons: it will make our tests much slower, might give us a false negative, the API request will cost us money, or we will mess up our database with test data. 

```
import React from 'react';
import ReactDOM from 'react-dom';
import TestAxios from '../test_axios.js';
import {act, render, fireEvent, cleanup, waitForElement} from '@testing-library/react';

import axiosMock from "axios";


```

We have our usual imports but you will notice something peculiar. We are importing `axiosMock` from the `axios` library. We are not importing a mock axios object from the `axios` library. We are actually mocking the `axios` library _itself_. 

How? 

By using the mocking functionality offered by jest. 

We first will make a `__mocks__` folder adjacent to our test folder, so something like this. 

![Image](https://www.freecodecamp.org/news/content/images/2019/07/image-13.png)



And inside the mocks folder we have an `axios.js` file and this is our fake **axios** library. And inside our fake **axios** library we have our **jest mock function**. 

Mock functions allow us to use functions in our jest environment without having to implement the actual logic of the function. 

So basically we are not going to implement the actual logic behind an axios get request. We will just use this mock function instead. 

```javascript
export default {
  get: jest.fn(() => Promise.resolve({ data: {} }) )
};

```

Here we have our fake get function. It is a simple function that is actually a JS object. `get` is our key and the value is the **mock function**. Like an **axios** API request, we resolve a promise. We wont pass in any data here, we will do that in our testing setup. 

Now our testing setup

```javascript
//imports
...

afterEach(cleanup)

it('Async axios request works', async () => {
  axiosMock.get.mockResolvedValue({data: { title: 'some title' } })

  const url = 'https://jsonplaceholder.typicode.com/posts/1'
  const { getByText, getByTestId, rerender } = render(<TestAxios url={url} />);

  expect(getByText(/...Loading/i).textContent).toBe("...Loading")

  const resolvedEl = await waitForElement(() => getByTestId("title"));

  expect((resolvedEl).textContent).toBe("some title")

  expect(axiosMock.get).toHaveBeenCalledTimes(1);
  expect(axiosMock.get).toHaveBeenCalledWith(url);
 })
```

The first thing we do in our test is call our fake **axios get request**, and mock the resolved value with ironically the `mockResolvedValue` function offered by jest. This function does exactly what its name says, it resolves a promise with the data we pass in, which simulates what axios does. 

This function has to be called before our `render()` function otherwise the test wont work. Because remember we are mocking the **axios library** itself. When our component runs the `import axios from 'axios';` command it will be **importing our fake axios library** instead of the real one and this fake axios will be substituted in our component wherever we used axios. 

Next we get our "...Loading" text node since this is what will be displayed before the promise resolves. After this we a function we havent seen before the `waitForElement()`  function, which will wait until the promise resolves before going to the next assertion. 

Also notice the **await** and **async** keywords, these are used in the exact same way as they are used in a non testing environment. 

Once resolved the DOM node will have the text of "some title" which is the data we passed to our fake mock axios library. 

Next we make sure the request was only called once and with the right url. Even though we are testing the url we didnt make an API request with this url. 

And this is it for API requests with axios. In the next section we will look at e to e tests with cypress. 

## Cypress

Lets now go over cypress which I believe is the best framework to run e to e tests. We are now longer in jest land, we will now be working solely with cypress which has its own testing environment and syntax.

Cypress is pretty amazing and powerful. So amazing and powerful in fact that we can run every test we just went over in one test block and watch cypress run these tests in real time in a simulated browser. 

Pretty cool, huh? 

I think so. Anyway, before we can do that we need to setup cypress. Surprisingly Cypress can be installed as a regular npm module. 

`npm install cypress`

To run cypress you will need to use this command. 

`node_modules/.bin/cypress open`

If that seems cumbersome to write every time you want open cypress so you can add it to your package.json. 

```javascript
...

  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject",
    "cypress": "node_modules/.bin/cypress open", 
    
   ...
```

this will allow you to open up cypress with just the `npm run cypress` command. 

Opening up cypress will give you a GUI that looks like this.

![Image](https://www.freecodecamp.org/news/content/images/2019/07/image-14.png)

To actually run the cypress tests, your app will have to be running at the same time, which we will see in a second. 

Running the `cypress open` command will give you a basic configuration of cypress and create some files and folders for your automatically. A cypress folder will be created in the project root. We will write our code in the integration folder. 

We can begin by deleting the examples folder. Unlike jest, cypress files take a `.spec.js` extension.  Because this is a e to e test we will run it on our main `App.js` file. So you should have a directory structure that now looks like this. 

![Image](https://www.freecodecamp.org/news/content/images/2019/07/image-21.png)



We can also set a Base url in the cypress.json file. Just like this: 

`{ "baseUrl": "[http://localhost:3000](http://localhost:3000)" }`

Now for our large monolithic test 

```javascript
import React from 'react';

describe ('complete e to e test', () => {
  it('e to e test', () => {
    cy.visit('/')
    //counter test
    cy.contains("Clicked: 0")
      .click()
    cy.contains("Clicked: 1")
    // basic hooks test
    cy.contains("Initial State")
    cy.contains("State Change Button")
      .click()
    cy.contains("Initial State Changed")
    cy.contains("Moe")
    cy.contains("Change Name")
      .click()
    cy.contains("Steve")
    //useReducer test
    cy.contains('stateprop1 is false')
    cy.contains('Dispatch Success')
      .click()
    cy.contains('stateprop1 is true')
    //useContext test
    cy.contains("Some Text")
    cy.contains('Change Text')
      .click()
    cy.contains("Some Other Text")
    //form test
    cy.get('#text1')
      .type('New Text {enter}')
    cy.contains("Change: New Text")
    cy.contains("Submit Value: New Text")
    //axios test
    cy.request('https://jsonplaceholder.typicode.com/posts/1')
      .should(res => {
          expect(res.body).not.to.be.null
          cy.contains(res.body.title)
        })
  });
});
```

As mentioned we are running every single test we just went over in one test block. I have separated each section with a comment so it will easier to see. 

Our test may look intimidating at first but most of the individual tests will follow a basic arrange-act-assert pattern.  

```javascript

cy.contains(Some innerHTML text of DOM node)

cy.contains (text of button)
.click()

cy.contains(Updated innerHTML text of DOM node)

```

Since this is a e to e test you will find no mocking at all. Our app will be running in its full development version in a simulated browser with a UI. This will be as close to testing our app in realistic way as we can get.   

Unlike unit and integration tests we do not need to explicitly assert some things. This is because some Cypress commands have built in default assertions. **Default assertions** are exactly what they sound like, they are asserted by default so no need to add a matcher.  

 [Cypress default assertions](https://docs.cypress.io/guides/core-concepts/introduction-to-cypress.html#Default-Assertions) 

Commands are chained together so order is important and one command will wait until a previous command is completed before running. 

Even when testing with cypress we will stick to our philosophy of not testing implementation details. In practice this is going to mean that we will not use html/css classes, ids or properties as selectors if we can help it. The only time we will need to use id is to get our form input element.  

We will make use of the `cy.contains()` command which will return a DOM node with matching text. Seeing and Interacting with text on the UI is what our end user will do, so testing this way will be in line with our guiding principle. 

Since we are not stubbing or mocking anything you will notice our tests will look very simplistic. This is good since this is a live running app, our tests will not have any artificial values. 

In our axios test we will make a real http request to our endpoint. Making a real http request in an e to e test is common. Then we will check to see if that value is not null. Then make sure that the data of the response appears in our UI. 

If done correctly you should see that cypress successfully ran the tests in chromium.   


![Image](https://www.freecodecamp.org/news/content/images/2019/07/image-22.png)



## Continuous Integration

Keeping track and Running all these tests manually can become tedious. So we have Continuous Integration, A way to automatically run our tests continuously.

### Travis CI

To keep things simple we'll just use Travis CI for our Continuous integration. You should know though that there are much more complex CI setups using Docker and Jenkins.

You will need to sign up for a Travis and Github account, both of these are luckily free. 

I would suggest just using the "Sign Up with Github" option on Travis CI. 

Once there you can just go on your profile icon and click the slider button next to the repository you want CI on.

![Image](https://www.freecodecamp.org/news/content/images/2019/07/image-15.png)

So that Travis CI knows what to do we will need to configure a .travis.yml file in our project root. 

```yaml
language: node_js

node_js: 
  - stable
  
  
install:
  - npm install

script:
  - npm run test
  - npm run coveralls
```

This essentially tells Travis that we are using node_js, download the stable version, install the dependencies and run the npm run test and npm run coveralls command.  

And this is it. You can know go on the dashboard and start the build. Travis will run the tests automatically and give you an output like this.  If your tests pass you are good to go. If they fail, your build will fail and you will need to fix your code and restart the build. 

![Image](https://www.freecodecamp.org/news/content/images/2019/07/image-16.png)



### Coveralls

coverall gives us a coverage report that essentially tells us how much of our code is being tested. 

You will need to sign up to coveralls and sync with your github account. Similar to Travis CI, just go to the add repos tab and turn on the repo that you also activated on Travis CI. 

![Image](https://www.freecodecamp.org/news/content/images/2019/07/image-17.png)

Next go to your package.json file and add this line of code 

```
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test --coverage",
    "eject": "react-scripts eject",
    "cypress": "node_modules/.bin/cypress open", 
    "coveralls": "cat ./coverage/lcov.info | node node_modules/.bin/coveralls"
  },
```

Be sure to add the `--coverage`  flag to the `react-scripts test` command. This is what will generate the coverage data that coveralls will use to generate a coverage report. 

And you can actually see this coverage data on the Travis CI console after your tests have ran.  

![Image](https://www.freecodecamp.org/news/content/images/2019/07/image-18.png)

Since we are not dealing with a private repo or Travis CI pro, we dont need to worry about repo tokens. 

Once your done you can add a badge to your repo README by copying the provided link on the dashboard. 

![Image](https://www.freecodecamp.org/news/content/images/2019/07/image-19.png)



It will look like this. 

![Image](https://www.freecodecamp.org/news/content/images/2019/07/image-20.png)





## Conclusion 

Count yourself among the top 20% of developers in terms of React testing skill if you made it through the entire tutorial. 

Thanks for reading. cheers. 

> You can follow me on twitter for more tutorials in the future: [https://twitter.com/iqbal125sf?lang=en](https://twitter.com/iqbal125sf?lang=en)



### Further Reading  


**Blog Posts:**

[https://djangostars.com/blog/what-and-how-to-test-with-enzyme-and-jest-full-instruction-on-react-component-testing/](https://djangostars.com/blog/what-and-how-to-test-with-enzyme-and-jest-full-instruction-on-react-component-testing/#utm_source=medium&utm_medium=blog.bitsrc.io&utm_campaign=react%20components%20testing&utm_content=continue%20reading%20the%20original%20article%20on%20our%C2%A0blog)

[https://engineering.ezcater.com/the-case-against-react-snapshot-testing](https://engineering.ezcater.com/the-case-against-react-snapshot-testing)

[https://medium.com/@tomgold_48918/why-i-stopped-using-snapshot-testing-with-jest-3279fe41ffb2](https://medium.com/@tomgold_48918/why-i-stopped-using-snapshot-testing-with-jest-3279fe41ffb2)

[https://circleci.com/blog/continuously-testing-react-applications-with-jest-and-enzyme/](https://circleci.com/blog/continuously-testing-react-applications-with-jest-and-enzyme/)

[https://testing.googleblog.com/2015/04/just-say-no-to-more-end-to-end-tests.html](https://testing.googleblog.com/2015/04/just-say-no-to-more-end-to-end-tests.html)

[https://willowtreeapps.com/ideas/best-practices-for-unit-testing-with-a-react-redux-approach](https://willowtreeapps.com/ideas/best-practices-for-unit-testing-with-a-react-redux-approach)

[https://blog.pragmatists.com/genuine-guide-to-testing-react-redux-applications-6f3265c11f63](https://blog.pragmatists.com/genuine-guide-to-testing-react-redux-applications-6f3265c11f63)

[https://hacks.mozilla.org/2018/04/testing-strategies-for-react-and-redux/](https://hacks.mozilla.org/2018/04/testing-strategies-for-react-and-redux/)

[https://codeburst.io/deliberate-practice-what-i-learned-from-reading-redux-mock-store-8d2d79a4b24d](https://codeburst.io/deliberate-practice-what-i-learned-from-reading-redux-mock-store-8d2d79a4b24d)

[https://www.robinwieruch.de/react-testing-tutorial/](https://www.robinwieruch.de/react-testing-tutorial/)

[https://medium.com/@ryandrewjohnson/unit-testing-components-using-reacts-new-context-api-4a5219f4b3fe](https://medium.com/@ryandrewjohnson/unit-testing-components-using-reacts-new-context-api-4a5219f4b3fe)  
  
  


**Kent C dodds Posts on Testing**

[https://kentcdodds.com/blog/introducing-the-react-testing-library](https://kentcdodds.com/blog/introducing-the-react-testing-library)

[https://kentcdodds.com/blog/unit-vs-integration-vs-e2e-tests](https://kentcdodds.com/blog/unit-vs-integration-vs-e2e-tests)

[https://kentcdodds.com/blog/why-i-never-use-shallow-rendering](https://kentcdodds.com/blog/why-i-never-use-shallow-rendering)

[https://kentcdodds.com/blog/demystifying-testing](https://kentcdodds.com/blog/demystifying-testing)

[https://kentcdodds.com/blog/effective-snapshot-testing](https://kentcdodds.com/blog/effective-snapshot-testing)

[https://kentcdodds.com/blog/testing-implementation-details](https://kentcdodds.com/blog/testing-implementation-details)

[https://kentcdodds.com/blog/common-testing-mistakes](https://kentcdodds.com/blog/common-testing-mistakes)

[https://kentcdodds.com/blog/ui-testing-myths](https://kentcdodds.com/blog/ui-testing-myths)

[https://kentcdodds.com/blog/why-youve-been-bad-about-testing](https://kentcdodds.com/blog/why-youve-been-bad-about-testing)

[https://kentcdodds.com/blog/the-merits-of-mocking](https://kentcdodds.com/blog/the-merits-of-mocking)

[https://kentcdodds.com/blog/how-to-know-what-to-test](https://kentcdodds.com/blog/how-to-know-what-to-test)

[https://kentcdodds.com/blog/avoid-the-test-user](https://kentcdodds.com/blog/avoid-the-test-user)  
  


**Cheat Sheets / github threads**

[https://devhints.io/enzyme](https://devhints.io/enzyme)

[https://devhints.io](https://devhints.io/enzyme)/jest 

[https://github.com/ReactTraining/react-router/tree/master/packages/react-router/modules/__tests__](https://github.com/ReactTraining/react-router/tree/master/packages/react-router/modules/__tests__)

[https://github.com/airbnb/enzyme/issues/1938](https://github.com/airbnb/enzyme/issues/1938) 

[https://gist.github.com/fokusferit/e4558d384e4e9cab95d04e5f35d4f913](https://gist.github.com/fokusferit/e4558d384e4e9cab95d04e5f35d4f913)

[https://airbnb.io/enzyme/docs/api/selector.html](https://airbnb.io/enzyme/docs/api/selector.html)  
  


**Docs**

[https://docs.cypress.io](https://docs.cypress.io/)

[https://airbnb.io/enzyme/](https://airbnb.io/enzyme/)

[https://github.com/dmitry-zaets/redux-mock-store](https://github.com/dmitry-zaets/redux-mock-store)

[https://jestjs.io/docs/en](https://jestjs.io/docs/en)

[https://testing-library.com/docs/learning](https://testing-library.com/docs/learning)

[https://sinonjs.org/releases/v7.3.2/](https://sinonjs.org/releases/v7.3.2/)

[https://redux.js.org/recipes/writing-tests](https://redux.js.org/recipes/writing-tests)

[https://jestjs.io/docs/en/using-matchers](https://jestjs.io/docs/en/using-matchers)

[https://jestjs.io/docs/en/api](https://jestjs.io/docs/en/api)  



