---
title: How to Start Testing Your React Apps Using the React Testing Library and Jest
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-03-12T17:39:01.000Z'
originalURL: https://freecodecamp.org/news/8-simple-steps-to-start-testing-react-apps-using-react-testing-library-and-jest
coverImage: https://www.freecodecamp.org/news/content/images/2020/03/cover-3.png
tags:
- name: React
  slug: react
- name: Testing
  slug: testing
seo_title: null
seo_desc: 'By Ibrahima Ndaw

  Testing is often seen as a tedious process. It''s extra code you have to write,
  and in some cases, to be honest, it''s not needed. But every developer should know
  at least the basics of testing. It increases confidence in the products ...'
---

By Ibrahima Ndaw

Testing is often seen as a tedious process. It's extra code you have to write, and in some cases, to be honest, it's not needed. But every developer should know at least the basics of testing. It increases confidence in the products they build, and for most companies, it's a requirement.

In the React world, there is an amazing library called the `react-testing-library` which helps you test your React Apps more efficiently. You use it with Jest.

In this article, we will see the 8 simple steps you can take to start testing your React Apps like a boss.

* [Prerequisites](#heading-prerequisites)
* [Basics](#heading-basics)
* [What is React Testing Library?](#what-is-react-testing-library)
* [1. How to create a test snapshot?](#heading-1-how-to-create-a-test-snapshot)
* [2. Testing DOM elements](#heading-2-testing-dom-elements)
* [3. Testing events](#heading-3-testing-events)
* [4. Testing asynchronous actions](#heading-4-testing-asynchronous-actions)
* [5. Testing React Redux](#heading-5-testing-react-redux)
* [6. Testing React Context](#heading-6-testing-react-context)
* [7. Testing React Router](#heading-7-testing-react-router)
* [8. Testing HTTP Request](#heading-8-testing-http-request)
* [Final Thoughts](#heading-final-thoughts)
* [Next Steps](#heading-next-steps)

## Prerequisites

This tutorial assumes that you have at least a basic understanding of React. I will focus only on the testing part.

And to follow along, you have to clone the project by running in your terminal:

```shell
  git clone https://github.com/ibrahima92/prep-react-testing-library-guide

```

Next, run:

```shell
  yarn

```

Or, if you use NPM:

```shell
npm install

```

And that's it! Now let's dive into some basics.

## Basics

Some key things will be used a lot in this article, and understanding their role can help you with your understanding.

`it or test`: describes the test itself. It takes as parameters the name of the test and a function that holds the tests.

`expect`: the condition that the test needs to pass. It will compare the received parameter to a matcher.

`a matcher`: a function that is applied to the expected condition.

`render`: the method used to render a given component.

```jsx
import React from 'react'
import {render} from '@testing-library/react'
import App from './App'
 
 it('should take a snapshot', () => {
    const { asFragment } = render(<App />)
    
    expect(asFragment(<App />)).toMatchSnapshot()
   })
});

```

As you can see, we describe the test with `it`, then, use `render` to display the App component and expect that `asFragment(<App />)` matches `toMatchSnapshot()` (the matcher provided by [jest-dom](https://github.com/testing-library/jest-dom)). 

By the way, the `render` method returns several methods we can use to test our features. We also used destructuring to get the method.

That being said, let's move on and learn more about the React Testing Library in the next section.

## What is the React Testing Library?

The React Testing Library is a very light-weight package created by [Kent C. Dodds](https://twitter.com/kentcdodds). It's a replacement for [Enzyme](https://enzymejs.github.io/enzyme/) and provides light utility functions on top of `react-dom` and `react-dom/test-utils`. 

The React Testing Library is a DOM testing library, which means that instead of dealing with instances of rendered React components, it handles DOM elements and how they behave in front of real users. 

It's a great library, it's (relatively) easy to start using, and it encourages good testing practices. Note – you can also use it without Jest.

"The more your tests resemble the way your software is used, the more confidence they can give you."

So, let's start using it in the next section. By the way, you don't need to install any packages, since `create-react-app` comes with the library and its dependencies.

## 1. How to create a test snapshot

A snapshot, as the name suggests, allows us to save the snapshot of a given component. It helps a lot when you update or do some refactoring, and want to get or compare the changes.

Now, let's take a snapshot of the `App.js` file.

* `App.test.js`

```jsx
import React from 'react'
import {render, cleanup} from '@testing-library/react'
import App from './App'

 afterEach(cleanup)
 
 it('should take a snapshot', () => {
    const { asFragment } = render(<App />)
    
    expect(asFragment(<App />)).toMatchSnapshot()
   })
});

```

To take a snapshot, we first have to import `render` and `cleanup`. These two methods will be used a lot throughout this article. 

`render`, as you might guess, helps to render a React component. And `cleanup` is passed as a parameter to `afterEach` to just clean up everything after each test to avoid memory leaks.

Next, we can render the App component with `render` and get back `asFragment` as a returned value from the method. And finally, make sure that the fragment of the App component matches the snapshot.

Now, to run the test, open your terminal and navigate to the root of the project and run the following command:

```shell
  yarn test

```

Or, if you use npm:

```shell
  npm test

```

As a result, it will create a new folder `__snapshots__` and a file `App.test.js.snap` in the `src` which will look like this:

* `App.test.js.snap`

```jsx
// Jest Snapshot v1, https://goo.gl/fbAQLP

exports[`Take a snapshot should take a snapshot 1`] = `
<DocumentFragment>
  <div class="App">
    <h1>Testing</h1>
  </div>
</DocumentFragment>
`;

```

And if you make another change in `App.js`, the test will fail, because the snapshot will no longer match the condition. To make it passes, just press `u` to update it. And you'll have the updated snapshot in `App.test.js.snap`.

Now, let's move on and start testing our elements.

## 2. Testing DOM elements

To test our DOM elements, we first have to look at the `TestElements.js` file.

* `TestElements.js`

```jsx
import React from 'react'

const TestElements = () => {
 const [counter, setCounter] = React.useState(0)
  
 return (
  <>
    <h1 data-testid="counter">{ counter }</h1>
    <button data-testid="button-up" onClick={() => setCounter(counter + 1)}> Up</button>
    <button disabled data-testid="button-down" onClick={() => setCounter(counter - 1)}>Down</button>
 </>
    )
  }
  
export default TestElements

```

Here, the only thing you have to retain is `data-testid`. It will be used to select these elements from the test file. Now, let's write the unit test:

Test if the counter is equal to 0:

`TestElements.test.js`

```jsx
import React from 'react';
import { render, cleanup } from '@testing-library/react';
import TestElements from './TestElements'

afterEach(cleanup);

  it('should equal to 0', () => {
    const { getByTestId } = render(<TestElements />); 
    expect(getByTestId('counter')).toHaveTextContent(0)
   });

```

As you can see, the syntax is quite similar to the previous test. The only difference is that we use `getByTestId` to select the necessary elements (remember the `data-testid`) and check if it passed the test. In others words, we check if the text content `<h1 data-testid="counter">{ counter }</h1>` is equal to 0.

Test if the buttons are enabled or disabled:

`TestElements.test.js` (add the following code block to the file)

```jsx
   it('should be enabled', () => {
    const { getByTestId } = render(<TestElements />);
    expect(getByTestId('button-up')).not.toHaveAttribute('disabled')
  });

  it('should be disabled', () => {
    const { getByTestId } = render(<TestElements />); 
    expect(getByTestId('button-down')).toBeDisabled()
  });

```

Here, as usual, we use `getByTestId` to select elements and check for the first test if the button has a `disabled` attribute. And for the second, if the button is disabled or not.

And if you save the file or run again in your terminal `yarn test`, the test will pass.

_Congrats! Your first test has passed!_

![congrats](https://media.giphy.com/media/3o6fJ1BM7R2EBRDnxK/source.gif)

Now, let's learn how to test an event in the next section.

## 3. Testing events

Before writing our unit tests, let's first check what the `TestEvents.js` looks like.

* `TestEvents.js`

```jsx
import React from 'react'

const TestEvents = () => {
  const [counter, setCounter] = React.useState(0)
  
return (
  <>
    <h1 data-testid="counter">{ counter }</h1>
    <button data-testid="button-up" onClick={() => setCounter(counter + 1)}> Up</button>
    <button data-testid="button-down" onClick={() => setCounter(counter - 1)}>Down</button>
 </>
    )
  }
  
  export default TestEvents

```

Now, let's write the tests.

Test if the counter increments and decrements correctly when we click on buttons:

`TestEvents.test.js`

```jsx
import React from 'react';
import { render, cleanup, fireEvent } from '@testing-library/react';
import TestEvents from './TestEvents'

  afterEach(cleanup);
  
  it('increments counter', () => {
    const { getByTestId } = render(<TestEvents />); 
    
    fireEvent.click(getByTestId('button-up'))

    expect(getByTestId('counter')).toHaveTextContent('1')
  });

  it('decrements counter', () => {
    const { getByTestId } = render(<TestEvents />); 
    
    fireEvent.click(getByTestId('button-down'))

    expect(getByTestId('counter')).toHaveTextContent('-1')
  });


```

As you can see, these two tests are very similar except the expected text content.

The first test fires a click event with `fireEvent.click()` to check if the counter increments to 1 when the button is clicked.

And the second one checks if the counter decrements to -1 when the button is clicked.

`fireEvent` has several methods you can use to test events, so feel free to dive into the documentation to learn more.

Now that we know how to test events, let's move on and learn in the next section how to deal with asynchronous actions.

## 4. Testing asynchronous actions

An asynchronous action is something that can take time to complete. It can be an HTTP request, a timer, and so on.

Now, let's check the `TestAsync.js` file.

* `TestAsync.js`

```jsx
import React from 'react'

const TestAsync = () => {
  const [counter, setCounter] = React.useState(0)

  const delayCount = () => (
    setTimeout(() => {
      setCounter(counter + 1)
    }, 500)
  )
  
return (
  <>
    <h1 data-testid="counter">{ counter }</h1>
    <button data-testid="button-up" onClick={delayCount}> Up</button>
    <button data-testid="button-down" onClick={() => setCounter(counter - 1)}>Down</button>
 </>
    )
  }
  
  export default TestAsync

```

Here, we use `setTimeout()` to delay the incrementing event by 0.5s.

Test if the counter is incremented after 0.5s:

`TestAsync.test.js`

```jsx
import React from 'react';
import { render, cleanup, fireEvent, waitForElement } from '@testing-library/react';
import TestAsync from './TestAsync'

afterEach(cleanup);
  
  it('increments counter after 0.5s', async () => {
    const { getByTestId, getByText } = render(<TestAsync />); 

    fireEvent.click(getByTestId('button-up'))

    const counter = await waitForElement(() => getByText('1')) 

    expect(counter).toHaveTextContent('1')
  });

```

To test the incrementing event, we first have to use async/await to handle the action because, as I said earlier, it takes time to complete.

Next, we use a new helper method `getByText()`. This is similar to `getByTestId()`, except that `getByText()` selects the text content instead of id or data-testid.

Now, after clicking to the button, we wait for the counter to be incremented with `waitForElement(() => getByText('1'))`. And once the counter incremented to 1, we can now move to the condition and check if the counter is effectively equal to 1.

That being said, let's now move to more complex test cases.

_Are you ready?_

![ready](https://media.giphy.com/media/Y3MbPtRn74uR3Ziq4P/source.gif)

## 5. Testing React Redux

If you're new to React Redux, [this article](https://www.ibrahima-ndaw.com/blog/7-steps-to-understand-react-redux/) might help you. Otherwise, let's check what the `TestRedux.js` looks like.

* `TestRedux.js`

```jsx
import React from 'react'
import { connect } from 'react-redux'

const TestRedux = ({counter, dispatch}) => {

 const increment = () => dispatch({ type: 'INCREMENT' })
 const decrement = () => dispatch({ type: 'DECREMENT' })
  
 return (
  <>
    <h1 data-testid="counter">{ counter }</h1>
    <button data-testid="button-up" onClick={increment}>Up</button>
    <button data-testid="button-down" onClick={decrement}>Down</button>
 </>
    )
  }
  
export default connect(state => ({ counter: state.count }))(TestRedux)

```

And for the reducer:

* `store/reducer.js`

```jsx
export const initialState = {
    count: 0,
  }
  
  export function reducer(state = initialState, action) {
    switch (action.type) {
      case 'INCREMENT':
        return {
          count: state.count + 1,
        }
      case 'DECREMENT':
        return {
          count: state.count - 1,
        }
      default:
        return state
    }
  }

```

As you can see, there is nothing fancy – it's just a basic Counter Component handled by React Redux.

Now, let's write the unit tests.

Test if the initial state is equal to 0:

`TestRedux.test.js`

```jsx
import React from 'react'
import { createStore } from 'redux'
import { Provider } from 'react-redux'
import { render, cleanup, fireEvent } from '@testing-library/react';
import { initialState, reducer } from '../store/reducer'
import TestRedux from './TestRedux'

const renderWithRedux = (
  component,
  { initialState, store = createStore(reducer, initialState) } = {}
) => {
  return {
    ...render(<Provider store={store}>{component}</Provider>),
    store,
  }
}

 afterEach(cleanup);

it('checks initial state is equal to 0', () => {
    const { getByTestId } = renderWithRedux(<TestRedux />)
    expect(getByTestId('counter')).toHaveTextContent('0')
  })

```

There are a couple of things we need to import to test React Redux. And here, we create our own helper function `renderWithRedux()` to render the component since it will be used several times.

`renderWithRedux()` receives as parameters the component to render, the initial state, and the store. If there is no store, it will create a new one, and if it doesn't receive an initial state or a store, it returns an empty object.

Next, we use `render()` to render the component and pass the store to the Provider.

That being said, we can now pass the component `TestRedux` to `renderWithRedux()` to test if the counter is equal to `0`.

Test if the counter increments and decrements correctly:

`TestRedux.test.js` (add the following code block to the file)

```jsx
it('increments the counter through redux', () => {
  const { getByTestId } = renderWithRedux(<TestRedux />, 
    {initialState: {count: 5}
})
  fireEvent.click(getByTestId('button-up'))
  expect(getByTestId('counter')).toHaveTextContent('6')
})

it('decrements the counter through redux', () => {
  const { getByTestId} = renderWithRedux(<TestRedux />, {
    initialState: { count: 100 },
  })
  fireEvent.click(getByTestId('button-down'))
  expect(getByTestId('counter')).toHaveTextContent('99')
})

```

To test the incrementing and decrementing events, we pass an initial state as a second argument to `renderWithRedux()`. Now, we can click on the buttons and test if the expected result matches the condition or not.

Now, let's move to the next section and introduce React Context.

_React Router and Axios will come next – are you still with me?_

![of-course](https://media.giphy.com/media/l41YfdYdptDB9RHIA/source.gif)

## 6. Testing React Context

If you're new to React Context, check out [this article](https://www.ibrahima-ndaw.com/blog/redux-vs-react-context-which-one-should-you-choose/) first. Otherwise, let's check the `TextContext.js` file.

* `TextContext.js`

```jsx
import React from "react"

export const CounterContext = React.createContext()

const CounterProvider = () => {
  const [counter, setCounter] = React.useState(0)
  const increment = () => setCounter(counter + 1)
  const decrement = () => setCounter(counter - 1)

  return (
    <CounterContext.Provider value={{ counter, increment, decrement }}>
      <Counter />
    </CounterContext.Provider>
  )
}

export const Counter = () => {  
    const { counter, increment, decrement } = React.useContext(CounterContext)   
    return (
     <>
       <h1 data-testid="counter">{ counter }</h1>
       <button data-testid="button-up" onClick={increment}> Up</button>
       <button data-testid="button-down" onClick={decrement}>Down</button>
    </>
       )
}

export default CounterProvider

```

Now, the counter state is managed through React Context. Let's write the unit test to check if it behaves as expected.

Test if the initial state is equal to 0:

`TextContext.test.js`

```jsx
import React from 'react'
import { render, cleanup,  fireEvent } from '@testing-library/react'
import CounterProvider, { CounterContext, Counter } from './TestContext'

const renderWithContext = (
  component) => {
  return {
    ...render(
        <CounterProvider value={CounterContext}>
            {component}
        </CounterProvider>)
  }
}

afterEach(cleanup);

it('checks if initial state is equal to 0', () => {
    const { getByTestId } = renderWithContext(<Counter />)
    expect(getByTestId('counter')).toHaveTextContent('0')
})

```

As in the previous section with React Redux, here we use the same approach, by creating a helper function `renderWithContext()` to render the component. But this time, it receives only the component as a parameter. And to create a new context, we pass `CounterContext` to the Provider.

Now, we can test if the counter is initially equal to 0 or not.

Test if the counter increments and decrements correctly:

`TextContext.test.js` (add the following code block to the file)

```jsx
  it('increments the counter', () => {
    const { getByTestId } = renderWithContext(<Counter />)

    fireEvent.click(getByTestId('button-up'))
    expect(getByTestId('counter')).toHaveTextContent('1')
  })

  it('decrements the counter', () => {
    const { getByTestId} = renderWithContext(<Counter />)

    fireEvent.click(getByTestId('button-down'))
    expect(getByTestId('counter')).toHaveTextContent('-1')
  })

```

As you can see, here we fire a click event to test if the counter increments correctly to 1 and decrements to -1.

That being said, we can now move to the next section and introduce React Router.

## 7. Testing React Router

If you want to dive into React Router, [this article](https://www.ibrahima-ndaw.com/blog/the-complete-guide-to-react-router/) might help you. Otherwise, let's check the `TestRouter.js` file.

* `TestRouter.js`

```jsx
import React from 'react'
import { Link, Route, Switch,  useParams } from 'react-router-dom'

const About = () => <h1>About page</h1>

const Home = () => <h1>Home page</h1>

const Contact = () => {
  const { name } = useParams()
  return <h1 data-testid="contact-name">{name}</h1>
}

const TestRouter = () => {
    const name = 'John Doe'
    return (
    <>
    <nav data-testid="navbar">
      <Link data-testid="home-link" to="/">Home</Link>
      <Link data-testid="about-link" to="/about">About</Link>
      <Link data-testid="contact-link" to={`/contact/${name}`}>Contact</Link>
    </nav>
    
      <Switch>
        <Route exact path="/" component={Home} />
        <Route path="/about" component={About} />
        <Route path="/about:name" component={Contact} />
      </Switch>
    </>
  )
}

export default TestRouter

```

Here, we have some components to render when navigating the Home page.

Now, let's write the tests:

* `TestRouter.test.js`

```jsx
import React from 'react'
import { Router } from 'react-router-dom'
import { render, fireEvent } from '@testing-library/react'
import { createMemoryHistory } from 'history'
import TestRouter from './TestRouter'


const renderWithRouter = (component) => {
    const history = createMemoryHistory()
    return { 
    ...render (
    <Router history={history}>
        {component}
    </Router>
    )
  }
}

it('should render the home page', () => {

  const { container, getByTestId } = renderWithRouter(<TestRouter />) 
  const navbar = getByTestId('navbar')
  const link = getByTestId('home-link')

  expect(container.innerHTML).toMatch('Home page')
  expect(navbar).toContainElement(link)
})

```

To test React Router, we have to first have a navigation history to start with. Therefore we use `createMemoryHistory()` to well as the name guessed to create a navigation history.

Next, we use our helper function `renderWithRouter()` to render the component and pass `history` to the `Router` component. With that, we can now test if the page loaded at the start is the Home page or not. And if the navigation bar is loaded with the expected links.

Test if it navigates to other pages with the parameters when we click on links:

`TestRouter.test.js` (add the following code block to the file)

```jsx
it('should navigate to the about page', ()=> {
  const { container, getByTestId } = renderWithRouter(<TestRouter />) 

  fireEvent.click(getByTestId('about-link'))

  expect(container.innerHTML).toMatch('About page')
})

it('should navigate to the contact page with the params', ()=> {
  const { container, getByTestId } = renderWithRouter(<TestRouter />) 
   
  fireEvent.click(getByTestId('contact-link'))
   
  expect(container.innerHTML).toMatch('John Doe')
})

```

Now, to check if the navigation works, we have to fire a click event on the navigation links.

For the first test, we check if the content is equal to the text in the About Page, and for the second, we test the routing params and check if it passed correctly.

We can now move to the final section and learn how to test an Axios request.

_We're almost done!_

![still-here](https://media.giphy.com/media/h3inb3B7bEAq43iui9/source.gif)

## 8. Testing HTTP Request

As usual, let's first see what the `TextAxios.js` file looks like.

* `TextAxios.js`

```jsx
import React from 'react'
import axios from 'axios'

const TestAxios = ({ url }) => {
  const [data, setData] = React.useState()

  const fetchData = async () => {
    const response = await axios.get(url)
    setData(response.data.greeting)    
 }     
 
 return (
  <>
    <button onClick={fetchData} data-testid="fetch-data">Load Data</button>
    { 
    data ?
    <div data-testid="show-data">{data}</div>:
    <h1 data-testid="loading">Loading...</h1>
    }
  </>
     )
}

export default TestAxios

```

As you can see here, we have a simple component that has a button to make a request. And if the data is not available, it will display a loading message.

Now, let's write the tests.

Test if the data are fetched and displayed correctly:

`TextAxios.test.js`

```jsx
import React from 'react'
import { render, waitForElement, fireEvent } from '@testing-library/react'
import axiosMock from 'axios'
import TestAxios from './TestAxios'

jest.mock('axios')

it('should display a loading text', () => {

 const { getByTestId } = render(<TestAxios />)

  expect(getByTestId('loading')).toHaveTextContent('Loading...')
})

it('should load and display the data', async () => {
  const url = '/greeting'
  const { getByTestId } = render(<TestAxios url={url} />)

  axiosMock.get.mockResolvedValueOnce({
    data: { greeting: 'hello there' },
  })

  fireEvent.click(getByTestId('fetch-data'))

  const greetingData = await waitForElement(() => getByTestId('show-data'))

  expect(axiosMock.get).toHaveBeenCalledTimes(1)
  expect(axiosMock.get).toHaveBeenCalledWith(url)
  expect(greetingData).toHaveTextContent('hello there')
})

```

This test case is a bit different because we have to deal with an HTTP request. And to do that, we have to mock an axios request with the help of `jest.mock('axios')`.

Now, we can use `axiosMock` and apply a `get()` method to it. Finally we will use the Jest function `mockResolvedValueOnce()` to pass the mocked data as a parameter.

With that, now for the second test we can click to the button to fetch the data and use async/await to resolve it. And now we have to test 3 things:

1. If the HTTP request has been done correctly
2. If the HTTP request has been done with the `url`
3. If the data fetched matches the expectation.

And for the first test, we just check if the loading message is displayed when we have no data to show.

That being said, we're now done with the 8 simple steps to start testing your React Apps.

_Don't be scared to test anymore._

![not-scared](https://media.giphy.com/media/xUA7beT9PDJoDNAmgU/200w_d.gif)

## Final Thoughts

The React Testing Library is a great package for testing React Apps. It gives us access to `jest-dom` matchers we can use to test our components more efficiently and with good practices. Hopefully this article was useful, and it will help you build robust React apps in the future.

You can find the finished project [here](https://github.com/ibrahima92/react-testing-library-guide)

Thanks for reading it!

[Read more articles](https://www.ibrahima-ndaw.com/)  -  [Subscribe to my newsletter](https://ibrahima-ndaw.us5.list-manage.com/subscribe?u=8dedf5d07c7326802dd81a866&id=5d7bcd5b75)   -   [Follow me on twitter](https://twitter.com/ibrahima92_)

You can read other articles like this on [my blog](https://www.ibrahima-ndaw.com/blog/react-testing-library-guide/).

## Next Steps

[React Testing Library docs](https://testing-library.com/docs/react-testing-library/intro)

[React Testing Library Cheatsheet](https://testing-library.com/docs/react-testing-library/cheatsheet)

[Jest DOM matchers cheatsheet](https://github.com/testing-library/jest-dom)

[Jest Docs](https://jestjs.io/docs/en/getting-started.html)

