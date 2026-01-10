---
title: Test-Driven Development with React and Redux, using Redux TDD
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-09-29T12:16:32.000Z'
originalURL: https://freecodecamp.org/news/test-driven-development-with-react-and-redux-using-redux-tdd-3fd3be299918
coverImage: https://cdn-media-1.freecodecamp.org/images/1*0ern_Rqaw5d5tTuYRs78IQ.jpeg
tags:
- name: Functional Programming
  slug: functional-programming
- name: React
  slug: react
- name: Redux
  slug: redux
- name: Testing
  slug: testing
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Luca Matteis

  React and Redux have introduced a lot of functional programming concepts to the
  development of User Interfaces (UIs). This allows us to test our UIs in a simpler
  manner: they are pure functions of state.

  Redux has broken down state ma...'
---

By Luca Matteis

[React](https://facebook.github.io/react/) and [Redux](http://redux.js.org/) have introduced a lot of functional programming concepts to the development of User Interfaces (UIs). This allows us to test our UIs in a simpler manner: they are pure functions of state.

Redux has broken down state management using unidirectional data-flow, where the view — or the outside world — generates an **action** that is passed to a **reducer**, which creates a new **state**, and passes this new state back to the **view**:

![Image](https://cdn-media-1.freecodecamp.org/images/1*Wd0Tu0P9S-KuGiB_ZW77Cw.png)
_Redux’s unidirectional data-flow_

What’s important is that each of the steps illustrated above with the yellow arrows is a **pure function**.

This means that we can unit test each of these steps individually. This allows us to test complex UIs by asserting that functions return specific data.

Here’s an example of how we would test each of these steps in a simple `<Counter />` component using [**jest**](https://facebook.github.io/jest/) and [**enzyme**](https://github.com/airbnb/enzyme)**:**

```js
// Counter.test.js
it('should test the arrows going in and out of the VIEW', () => {
  // input to the view
  wrapper = shallow(<Counter counter={1} />);
  expect(wrapper.contains(<span>1</span>)).toBeTruthy();
  
  // output of the view
  wrapper = shallow(<Counter onClick={incrementAction} />);
  wrapper.find(button).simulate('click');
  expect(incrementAction).toHaveBeenCalled();
})

// reducers.test.js
it('should test the arrows going in and out of the REDUCER', () => {
  // input to the reducer
  const newState = reducer({ count: 0 }, incrementAction())
  
  // output of the reducer
  expect(newState).toEqual({ count: 1 });
})

// actions.test.js
it('should test the arrows going in and out of the ACTION', () => {
  expect(incrementAction()).toMatchObject({ type: 'INCREMENT' });
})
```

But, when it comes to doing TDD (test-driven development), you usually want to test things in succession. Such as when a certain click triggers a certain state-change which then triggers a UI change.

The tests above should be streamlined. There should be an easy way to plug them together naturally instead of having to write separate unit tests.

In this article I’ll explain [**Redux TDD.**](https://github.com/lmatteis/redux-tdd) It is a set of simple helper functions designed to help you streamline your tests by composing each part of the Redux data-flow together.

I’ll also discuss other concepts of TDD and BDD (behavior-driven development) in the context of Redux’s data-flow. And we’ll explore what the future of testing user-interfaces might look like.

![Image](https://cdn-media-1.freecodecamp.org/images/1*uOlxCoXq1faNmKA-3ie2Bg.jpeg)
_([Image source](https://unsplash.com/search/photos/jenga?photo=geNNFqfvw48" rel="noopener" target="_blank" title="))_

### Redux TDD

Let’s dive immediately into what Redux TDD looks like:

```jsx
ReduxTdd({ count: 9 }, state => shallow(
  <Counter 
    onIncrement={incrementActionMock} 
    onReset={resetActionMock} 
    count={state.count} />
))      
.simulate(wrapper => wrapper.find('button').simulate('click'))      .action(incrementActionMock).toMatchAction({ type: 'INCREMENT' })      .reducer(reducer).toMatchState({ count: 10 })      .view().contains(<span>10</span>)      
.simulate(wrapper => wrapper.find('button').simulate('click'))      .action(resetActionMock).toMatchAction({ type: 'RESET' })      .reducer(reducer).toMatchState({ count: 0 })
.view().contains(<span>0</span>)
```

There’s a lot of dot-chaining in this code, but there’s a reason for that. Since Redux’s data-flow is unidirectional, testing its behavior fits perfectly with a pipeline model. Which means chaining.

Each operator of the pipeline is in fact a simple unit-test.

The insight is that each output of a Redux unidirectional data-flow step should feed into the next step. This allows a more TDD-friendly development.

#### Let’s look at each step

1. Initialize the flow with a state and a view  
Other operators in the pipeline need this make assertions about current state and view:

```jsx
ReduxTdd({ count: 9 }, state => shallow(
  <Counter 
    onIncrement={incrementActionMock} 
    onReset={resetActionMock} 
    count={state.count} />
))
```

2. Simulate an actual click  
We have the enzyme wrapper from the earlier operator, so we can simulate actions:

```
.simulate(wrapper => wrapper.find('button').simulate('click'))
```

3. Here is where the fun starts  
We are unit-testing that `incrementActionMock` is called from the previous step and that it returns the `{ type: ‘INCREMENT’ } object:`

```js
.action(incrementActionMock).toMatchAction({ type: 'INCREMENT' })
```

4. We are passing in a `myReducer` function  
This will take the current state of the pipeline and the action returned from the earlier composed action.

It will assert that `myReducer({ count: 9 }, { type: ‘INCREMENT’ })` returns `{ count: 10 }`:

```js
.reducer(myReducer).toMatchState({ count: 10 })
```

5. We test that view  
Given the current state, modified by the earlier reducer, it will show the output that we want.

```js
.view().contains(<span>10</span>)
```

This dot-chaining model forces you to test the Redux unidirectional flow. It forces you to unit-test each step with the inputs from the earlier step.

![Image](https://cdn-media-1.freecodecamp.org/images/1*4n6RkGZdWcPvmsizsezKgg.png)
_How data flows through the pipeline_

We’re not introducing any Redux store, we’re not dispatching actions, and we’re not calling any of the Redux APIs. We’re only testing that pure functions return specific data.

#### Asyncronous actions

![Image](https://cdn-media-1.freecodecamp.org/images/1*av3MfP7tEC72pkPKkLAfeQ.jpeg)
_([Image source](https://unsplash.com/search/photos/time?photo=p3Pj7jOYvnM" rel="noopener" target="_blank" title="))_

So far we have described how to test the synchronous part of the redux data-flow. Yet, many of the things we do in our UIs involve asynchronous actions.

In Redux, this is handled by things called **middlewares**. I won’t go much into detail on how they work. I will cover examples showing how these tests can be pipelined against [redux-observable](https://github.com/redux-observable/redux-observable) and [redux-thunk](https://github.com/gaearon/redux-thunk). These are two famous middlewares used to handle asynchronous stuff and side-effects in Redux.

#### Redux-observable

```js
ReduxTdd({ count: 9 }, state => shallow(
  <Counter 
    onClick={incrementAsyncAction} 
    counter={state.count} />
))  
.simulate(wrapper => wrapper.find(button).simulate('click'))
.action(incrementAsyncAction).toMatchAction({ type: 'INCREMENT_ASYNC' })

.epic(handleIncrementAsyncEpic, { getJSON: () => 
  Observable.of({ foo: 'bar' })
})

// now since we mocked the epic, 
// we can continue normal action->reducer->view testing
.action(incrementSuccessAction).toMatchAction(
  { type: 'INCREMENT_SUCCESS' }
)
.reducer(reducer).toMatchState({ count: 10 })
.view().contains(<span>10</span>)
                 
.epic(handleIncrementAsyncEpic, { getJSON: () => 
  // let's throw this time 
  Observable.throw({ error: true })
})
                 
// since the epic threw an error, 
// we expect it to call the incrementFailureAction function
.action(incrementFailureAction).toMatchAction(
  { type: 'INCREMENT_FAILURE' }
)
// it will not increase it to 11
.reducer(reducer).toMatchState({ count: 10 })
.view().contains(<span>10</span>)
```

In the above example the important part of the pipeline is the `.epic()` operator.

We are testing that:  
The epic `handleIncrementAsyncEpic` will be executed with an observable emitting an action. This is returned by the earlier `.action` operator (`{ type: 'INCREMENT_ASYNC' }`) and the mocked `getJSON` observable. We will force the observable to emit a successful response.

This is plugged into the Redux flow. We’re literally visualizing each part of the Redux data-flow diagram using code.

The epic will execute immediately and the resulting action `{ type: 'INCREMENT_SUCCESS' }` will be passed to the next operator in the flow.

#### Redux-thunk

Thunks can also be plugged in the pipeline. But they are harder to test because they’re not pure functions:

```js
.thunk(incrementAsyncThunk, () => 
  Promise.resolve({ type: 'INCREMENT_SUCCESS' })
)
.toMatchActions([ 
  { type: 'INCREMENT_ASYNC' }, { type: 'INCREMENT_SUCCESS' } 
])
```

We are forcing the thunk’s `promise` to resolve to success. And we’re asserting that the actions are dispatched in the same order as the `toMatchActions` array.

### Behavior-driven development

![Image](https://cdn-media-1.freecodecamp.org/images/1*woIWXYmagRL9ejINlwRHnw.png)

The main benefit of composing tests in this manner is that it works great when doing [BDD](https://en.wikipedia.org/wiki/Behavior-driven_development).

In BDD you start by writing small tests that simulate users’ behavior. You implement your code until the tests pass, and you’re back into your test file writing new tests that break.

With the chaining model this works more naturally because we’re **forcing control flow**. You’re somewhat persuaded to write `.action()`, `.reduce()` and `.view()` — in that order. And you don’t have to create inputs for each of these steps because they’re passed along the flow behind the scenes.

### Example

![Image](https://cdn-media-1.freecodecamp.org/images/1*H0NItfukULQ4qOLFsc_tLQ.jpeg)
_([Image source](https://www.pexels.com/photo/paper-boats-on-solid-surface-194094/" rel="noopener" target="_blank" title="))_

Let’s take Redux TDD for a spin and try to implement a `<GithubTrending` /> component in a TDD way. This component is going to showcase the trending projects of the week. It’s going to h**ave a r**efresh button **and a lo**ading message that appears when requests are made.

In the spirit of true TDD we’re going to start imagining the shape of our state and the props our view will take.

And we’ll make the test fail:

```jsx
ReduxTdd({ projects: [], loading: false }, state => shallow(
  <GithubTrending 
    projects={state.projects} 
    loading={state.loading} 
    onRefresh={refreshAction} />
))
```

Let’s immediately test if our view looks OK. We’re extending the chaining from the above example:

```js
.view()
 .contains(<div class="loading" />, false) // shouldn't show loading
 .contains(<div class="projects">No projects</div>)
 .contains(<button class="refresh">refresh</button>)
```

Before implementing the component, we can simulate a `refresh` and check that the correct action is called:

```js
.simulate(wrapper => wrapper.find('.refresh').simulate('click'))
.action(refreshAction).toMatchAction({ type: 'REFRESH' })
```

Then we make sure that our state is changed correctly. In this step we are passing the earlier action to `githubReducer`. We should expect it to set the `loading` attribute to `true`:

```js
.reducer(githubReducer).toMatchState({ loading: true })
```

At this point we’re in the state where the projects are being loaded from the server so our `.view` should look something like this:

```js
.view().contains(<div class="loading" />)
```

Again, we haven’t written a single piece of implementation code yet.

Let’s continue the flow by going in the state where we’ve received data from the server and display the response. Here the `.epic` will call `handleRefreshEpic` with the earliest executed `.action` in the pipeline — in this case `refreshAction`. As its output to the next operator, we’re forcing its `getJSON` dependency to output a response. In case an epic emits multiple actions, we can call `action->reducer` multiple times to handle them.

```js
.epic(handleRefreshEpic, { getJSON: () => 
  Observable.of([
    { name: 'redux-tdd' }, { name: 'redux-cycles' }
  ])
}) 
.action(refreshDoneAction).toMatchAction({ 
  type: 'REFRESH_DONE',
  payload: [{ name: 'redux-tdd' }, { name: 'redux-cycles' }],
})
.reducer(githubReducer).toMatchState({
  loading: false,
  projects: [{ name: 'redux-tdd' }, { name: 'redux-cycles' }]
})
```

I’m being verbose to show what’s going on. You’d obviously want to put the mocked response in a variable and pass that along the tests.

Next, let’s make sure the `.view` looks as intended after the earlier changes of state:

```js
.view()
 .contains(<div class="loading" />, false) // shouldn't show loading
 .contains(<div class="projects">
   <div>redux-tdd</div>
   <div>redux-cycles</div>
 </div>)
```

And we’re done!

We can now start writing the actual implementation code to try to make each of our tests pass.

Let’s start by making the first test operator pass, hence the view:

```jsx
function GithubTrending({ projects, loading, onRefresh }) {
  return <div>
    { loading && <div class="loading" /> }
    <div class="projects">
      { !projects.length && 'No projects' }
      { projects.map(p => <div>{p.name}</div>) }
    </div>
    <button class="refresh" onClick={onRefresh}>refresh</button>
  </div>
}
```

Next let’s make our `.action`s pass:

```js
function refreshAction() {
  return { type: 'REFRESH' };
}

function refreshDoneAction(payload) {
  return { type: 'REFRESH_DONE', payload };
}
```

Next is our reducer:

```js
const initialState = { projects: [], loading: false };

function githubReducer(state = initialState, action) {
  switch (action.type) {
    case 'REFRESH':
      return { ...state, loading: true };
    case 'REFRESH_DONE':
      return { ...state, loading: false, projects: action.payload };
    default:
      return state;
  }
}
```

And our epic:

```js
function handleRefreshEpic(action$, store, { getJSON }) {
  return action$.ofType('REFRESH')
    .mergeMap(() =>
      getJSON('http://foo.bar')
        .map(response => refreshDoneAction(response))
    );
}
```

We can see from this example that writing the implementation code is actually the easy part. What’s hard is making sure we have correct test flows that follow the specs of our UIs.

One advantage of writing composable unit-tests this way compared to having separate tests in various files is that we generate inputs to units driven by actual user-behavior.

For instance, the test that checks whether `refreshDoneAction` was called with the actual mocked response might have never been written if we had not thought of the data-flow of Redux in this way.

On the other hand, Redux TDD drives you to think about — and test — how the data flows in your app.

Here’s a video showcasing the iterative process of writing these test using a watcher to constantly inform us about what needs to be implemented:

<iframe width="560" height="315" src="https://www.youtube.com/embed/lW1ytOEZx3Y" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Interaction between multiple components

So far we have seen how a component action triggers a state change which is fed to the component itself:

![Image](https://cdn-media-1.freecodecamp.org/images/1*RRokGbGhSvWc97PeEqVS3g.png)

Most component actions trigger changes that feed to other components as well:

![Image](https://cdn-media-1.freecodecamp.org/images/1*j2dDce96Vw0YM9HlVqEXRw.png)

To express this sort of behavior in Redux TDD we can render multiple components:

```js
ReduxTdd({ count: 0, show: false }, state => ([
  shallow(
    <Counter 
      onIncrement={incrementAction} 
      counter={state.count} />
  ),
  shallow(
    <Modal
      show={state.show} />
  )
]))
```

We can simulate things just like before and we get the wrappers as an array.

We want to show the `<Modal />` when the count state variable is odd:

```js
.simulate(([ counterWrapper, modalWrapper ]) =>
  counterWrapper.props.onIncrement() // simulate a click
)
.action(incrementAction).toMatchAction({ type: 'INCREMENT' })
.reducer(myReducer).toMatchState({ count: 1, show: true })
.view().contains(([ counter, modal ]) =>
  counter.contains(<span>1</span) &&
  modal.contains(<div class="showModal" />)
)
```

Although we could test each of these components individually, we have to think about the fact that our components are not yet implemented. Combining interactions among multiple components allows us to imagine what props our components will take in a true TDD fashion.

### Integration tests

![Image](https://cdn-media-1.freecodecamp.org/images/1*lnWj3S8D6P699LB98d9_oQ.gif)

You might be wondering whether the pipelines of unit-tests we’ve defined so far are considered integration tests.

There’s no stringent definition to what integration tests mean. Yet I’d argue that, compared to unit-tests, they require extra overhead:

1. They are computationally more expensive to execute. For instance, they require full DOM rendering.
2. They require complex setups of things like Redux stores, mocking of external libraries, and extra configuration.

On the other hand, the Redux TDD pipeline is only testing pure functions. There’s literally no external state and configuration required since each step of the chain is taking as input the output of the earlier step.

### Imperative vs declarative

![Image](https://cdn-media-1.freecodecamp.org/images/1*FZdafW2he_we_WOy_0MvWw.jpeg)
_([Image source](https://www.pexels.com/photo/pile-of-books-in-shallow-focus-photography-264635/" rel="noopener" target="_blank" title="))_

The dot-chain syntax we introduced, although simple and composable, is still imperative. This means that at every step of the chain we have a side-effect. This could be running `expect()`or simulating mouse clicks.

What if we could still have a way to think about the Redux flow using a more declarative style of programming?

An idea would be to use [function composition](https://medium.com/making-internets/why-using-chain-is-a-mistake-9bc1f80d51ba) with currying functions rather than dot chaining or [point-free programming](http://lucasmreis.github.io/blog/pointfree-javascript/):

```js
const myTest = flow(
  action(incrementActionMock)({ type: 'INCREMENT' }),
  reducer(reducer)({ count: 1 }),
  view(<div>{1}</div>)
)(ReduxTdd({ count: 0 }, state => 
  <Counter 
    onIncrement={incrementActionMock} 
    count={state.count} />
))

run(myTest)
```

The main advantage of this approach is that we are describing our test flows using `[_.flow](https://lodash.com/docs/4.17.4#flow),`rather than executing them. The `run` function call at the end is what’s actually going to execute our `expect()s`.

This declarative style can obviously be achieved with dot-chain syntax as well. But point-free function composition offers other benefits.

For instance it allows us to extend parts of the flow with our own implementations, instead of being tied to the [functions exposed by the library](https://medium.com/making-internets/why-using-chain-is-a-mistake-9bc1f80d51ba):

```js
const myIncrementAction = flow(
  action(incrementAction), 
  action => { // transform action in some way }
)
```

Here’s a great [article](https://simonsmith.io/dipping-a-toe-into-functional-js-with-lodash-fp/) that goes more in depth on these function composition concepts.

In terms of how we can use them, it remains an open question whether this declarative style of defining tests is actually better than its imperative counterpart.

### Trees of tests

![Image](https://cdn-media-1.freecodecamp.org/images/1*zqwlsft8_kItlJnKUS5ojQ.jpeg)
_([Image source](https://www.pexels.com/photo/green-pine-tree-leaves-192136/" rel="noopener" target="_blank" title="))_

You might be thinking that you could implement these composable Redux tests without the need of a library such as Redux TDD.

Redux TDD is a combination of helper functions showcasing the more important idea. Redux’s data-flow can be tested by composing unit-tests together.

Taking a hint of the functional composition from earlier, one can imagine having **trees of tests** rather than the common `describe()` and `it()` blocks of code.

We can represent these flows as trees. Instead of building from the earliest step, we can branch out into other states.

With functional composition, describing these trees can be fun:

```js
flow(
  flow(
    action(increment),
    reducer(githubReducer),
    view(<div>1</div>)
  ), // this branch has state { count: 1 }
  flow(
    action(decrement),
    reducer(githubReducer),
    view(<div>-1</div>),
    flow(
      action(increment),  
      reducer(githubReducer),
      view(<div>0</div>),
    )
  )({ count: 0 }) // don't get state from earlier branch
)({ count: 0 })
```

Again I’m being verbose. But we’re dealing with pure functions. For example, we can define a `simulateClick(increment)` to avoid some of the duplicate code.

I’d argue that having these kind of function trees describing your test flows, rather than a bunch of `it(‘should do this’)` blocks, is an interesting approach that should be studied more.

We can test states of our UIs that read more like specifications of what the user has done.

If a new combination comes to mind we can add it to the tree:

```js
flow(
  branch(
    clickButton, shouldShowModal, clickCloseModal, shouldCloseModal
  ),
  branch(
    clickCloseModal, 
    nothingShouldHappen,
    branch(clickButton, shouldShowModal)
    clickButton,
    shouldShowSpinner
  )
)
```

The above example are just ideas. Nothing of this is yet implemented in Redux TDD. We can compose the earlier primitive functions to read as if something were happening.

Branching is useful when we don’t want to modify the state of the parent branch. For instance, the `**clickButton**` in the earliest example will not know that the branch above it clicked the same button.

These kind of tests are similar to the [Gherkin language](https://github.com/cucumber/cucumber/wiki/Gherkin). We describe software’s behavior without detailing how that behavior is implemented.

### The future of UI testing in fantasy land

![Image](https://cdn-media-1.freecodecamp.org/images/1*TcWD4gZHNRFeRSUQN5xggg.jpeg)
_([Image source](https://www.pexels.com/photo/close-up-of-leaf-326055/" rel="noopener" target="_blank" title="))_

Although most of these concepts already exist in the context of BDD, they haven’t been explored much in the Redux world.

Describing these flows as trees is only practical because of Redux’s pureness.

I don’t personally know whether such tests can be described in this way using other state-management paradigms that aren’t pure and unidirectional.

Pureness is a critical concept that allows us to construct such descriptive trees.

⚠️ WARNING: bold and biased statements in the next few paragraphs.

One can imagine the bulk of future UI development being nothing other than writing test trees. Everything else is just an implementation detail.

I know this is a bold statement, but I’m ready to bet that Front-end developers of the future will spend most of their time writing **test trees**.

How the actual components, reducers, actions and side-effects will be written will depend entirely on such tests. These:  
(i) can be automated if enough combinations are covered by tests  
(ii) can be easily outsourced  
(iii) can be found as libraries.

### Conclusion

In this article I tried to shed some light on the fact that TDD can be fun.

Defining our tests as if we were interacting with the component makes it easier to understand what needs to be tested. Your unit-tests inputs are generated via actual users’ behavior.

We dove into the [crazy fantasy land](https://github.com/fantasyland/fantasy-land) of functional programming and discussed how some of these concepts can be useful for writing tests.

The number of interactions a user performs on a component can be described using a tree. We also looked at function trees and how we can combine curried functions together to build them.

I introduced Redux TDD as a concrete example to some of these concepts. Its functions are meant to help you streamline your Redux unit tests.

In the future I hope to showcase a more functional approach closer to the idea of function trees we discussed here.

You can try out redux-tdd by downloading it from [GitHub](https://github.com/lmatteis/redux-tdd).

Please share on social media if you enjoyed this article.

