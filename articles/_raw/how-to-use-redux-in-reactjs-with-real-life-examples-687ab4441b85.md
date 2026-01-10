---
title: How to use Redux in ReactJS with real-life examples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-10T22:59:16.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-redux-in-reactjs-with-real-life-examples-687ab4441b85
coverImage: https://cdn-media-1.freecodecamp.org/images/1*hOT8TIpiXVDCK02sQkvhDQ.jpeg
tags:
- name: learning to code
  slug: learning-to-code
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: Redux
  slug: redux
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Nazare Emanuel Ioan

  Since I started to work with ReactJS, at Creative-Tim, I’ve only used it to create
  simple react apps, or templates if you will. I have used ReactJS only with create-react-app
  and have never tried to integrate it with something ...'
---

By Nazare Emanuel Ioan

Since I started to work with [ReactJS](https://reactjs.org/), at [Creative-Tim](https://www.creative-tim.com/), I’ve only used it to create [simple react apps](https://www.creative-tim.com/bootstrap-themes/react-themes), or [templates](https://www.creative-tim.com/bootstrap-themes/react-themes) if you will. I have used ReactJS only with [create-react-app](https://github.com/facebook/create-react-app) and have never tried to integrate it with something more.

A lot of our users have asked me or my team if the templates created by me had [Redux](https://redux.js.org/) on them. Or if they were created in such manner that they could be used with Redux. And my answer was always something like: “I haven’t worked with Redux yet and I do not know what answer I should give you”.

So here I am now, writing an article about Redux and how it should be used in React. Later on, in this article, I am going to add Redux on top of one of the projects that I have worked over the last one and some years.

Good to know before we go ahead and wrestle with these two libraries:

* I am going to use [create-react-app@2.1.](https://github.com/facebook/create-react-app)1 (installed globally)
* I am using [npm@6.4.1](https://www.npmjs.com/package/npm)
* My [Node.js](https://nodejs.org/en/) version at the time of writing this post was 10.13.0 (LTS)
* If you want to use [Webpack](https://webpack.js.org/) instead, then you can read my [Webpack article](https://medium.freecodecamp.org/how-to-use-reactjs-with-webpack-4-babel-7-and-material-design-ff754586f618), and combine what I am showing you there with what I am going to show you here.

### Creating a new ReactJS based project and adding Redux to it

First things first let’s create a new react app, cd into it and start it.

```bash
create-react-app react-redux-tutorial
cd react-redux-tutorial
npm start
```

![Image](https://cdn-media-1.freecodecamp.org/images/nDaQRa3VplnG8gqJg08kGNkwpeSvlad2s30B)
_default **create-react-app** output of **npm start**_

As we can see, create-react-app gives us a very basic template with a paragraph, an anchor to the React website and the official ReactJS icon rotating.

I haven’t told you guys what we are going to use Redux for, or what are we doing here. And this is because I needed the above gif image.

To make this tutorial article light weight and easy to understand, we are not going to build something very complex. We are going to use Redux to make the above React image stop or start rotating.

So this being said, let’s go ahead and add the following **Redux** packages:

```bash
npm install --save redux react-redux
```

[redux v4.0.1](https://redux.js.org/)

* What Redux does in a very general sense, is that it creates a global state for the whole application, that can be accessed by any of your component
* It is a state management library
* You have only one state for your whole app, and not states for each of your components

[react-redux v5.1.1](https://www.npmjs.com/package/react-redux)

* This is used so we can access Redux’s data and modify it by sending actions to Redux — actually not Redux, but we’ll get there
* The official docs state: _It lets your React components read data from a Redux store, and dispatch actions to the store to update data_

**NOTE**: _If you have problems with the above command, try installing the packages separately_

When working with Redux, you will need three main things:

* [actions](https://redux.js.org/basics/actions): these are objects that should have two properties, one describing the **type** of action, and one describing what should be changed in the app state.
* [reducers](https://redux.js.org/basics/reducers): these are functions that implement the behavior of the actions. They change the state of the app, based on the action description and the state change description.
* [store](https://redux.js.org/basics/store): it brings the actions and reducers together, holding and changing the state for the whole app — there is only one store.

As I’ve said above, we are going to stop and start the React logo spinning. This means we are going to need two actions as follows:

1 — Linux / Mac commands

```bash
mkdir src/actions
touch src/actions/startAction.js
touch src/actions/stopAction.js
```

2 — Windows commands

```bash
mkdir src\actions
echo "" > src\actions\startAction.js
echo "" > src\actions\stopAction.js
```

Now let’s edit the **src/actions/startAction.js** as follows:

```js
export const startAction = {
  type: "rotate",
  payload: true
};
```

So, we are going to say to our reducer that the type of the action is about the _rotation_ (**rotate**) of the React logo. And the state for the rotate of the React logo should be changed to **true** — we want the logo to start rotating.

Now let’s edit the **src/actions/stopAction.js** as follows:

```js
export const stopAction = {
  type: "rotate",
  payload: false
};
```

So, we are going to say to our reducer that the type of the action is about the _rotation_ (**rotate**) of the React logo. And the state for the rotate of the React logo should be changed to **false** — we want the logo to stop rotating.

Let’s also create the reducer for our app:

1 — Linux / Mac commands

```bash
mkdir src/reducers
touch src/reducers/rotateReducer.js
```

2 — Windows commands

```bash
mkdir src\reducers
echo "" > src\reducers\rotateReducer.js
```

And, add the following code inside of it:

```js
export default (state, action) => {
  switch (action.type) {
    case "rotate":
      return {
        rotating: action.payload
      };
    default:
      return state;
  }
};
```

So, the reducer will receive both of our actions, both of which are of type **rotate,** and they both change the same state in the app — which is _state.rotating_. Based on the payload of these actions, _state.rotating_ will change into **true** or **false**.

I’ve added a **default** case, which will keep the state unaltered if the action type is not **rotate**. The default value is there in case we create an action and we forget to add a case for that action. This way we do not delete the whole app state — we simply do nothing, and keep what we had.

The last thing that we need to do is to create our store for the whole app. Since there is only one store / one state for the whole app, we are not going to create a new folder for the store. If you want, you can create a new folder for the store and add it there, but it’s not like with the actions, for example, where you can have multiple actions and it looks better to keep them inside a folder.

So this being said we are going to run this command:

1 — Linux / Mac command

```bash
touch src/store.js
```

2 — Windows command

```bash
echo "" > src\store.js
```

And also add the following code inside it:

```js
import { createStore } from "redux";
import rotateReducer from "reducers/rotateReducer";

function configureStore(state = { rotating: true }) {
  return createStore(rotateReducer,state);
}

export default configureStore;
```

So, we create a function named **configureStore** in which we send a default state, and we create our store using the created reducer and the default state.

I’m not sure if you’ve seen my imports, they use absolute paths, so you might have some errors due to this. The fix for this is one of the two:

Either

1 — Add a .env file into your app like so:

```bash
echo "NODE_PATH=./src" > .env
```

Or

2 — Install cross-env globally and change the start script from the package.json file like so:

```bash
npm install -g cross-env
```

And inside package.json

```json
"start": "NODE_PATH=./src react-scripts start",
```

Now that we have set up our store, our actions and our reducer we need to add a new class inside the **src/App.css** file. This class will pause the rotating animation of the logo.

So we are going to write the following inside **src/App.css**:

```css
.App-logo-paused {
  animation-play-state: paused;
}
```

So your **App.css** file should look something like this:

```css
.App {
  text-align: center;
}

.App-logo {
  animation: App-logo-spin infinite 20s linear;
  height: 40vmin;
}

/* new class here */
.App-logo-paused {
  animation-play-state: paused;
}

.App-header {
  background-color: #282c34;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-size: calc(10px + 2vmin);
  color: white;
}

.App-link {
  color: #61dafb;
}

@keyframes App-logo-spin {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}
```

Now, we only need to modify our **src/App.js** file so that it listens to our store state. And when clicking on the logo, it calls one of the start or stop actions.

First things first, we need to connect our component to our redux store so we import **connect** from **react-redux**.

```js
import { connect } from "react-redux";
```

After this, we’ll export our App component through the connect method like this:

```js
export default connect()(App);
```

To change the redux store state we’ll need the actions that we’ve done earlier so let’s import them as well:

```js
import { startAction } from "actions/startAction";
import { stopAction } from "actions/stopAction";
```

Now we need to retrieve the state from our store and to say that we want the start and stop actions to be used for changing the state.

This will be done using the connect function, which accepts two parameters:

* **mapStateToProps:** this is used to retrieve the store state
* **mapDispatchToProps:** this is used to retrieve the actions and dispatch them to the store

You can read more about them here: [react-redux connect function arguments](https://github.com/reduxjs/react-redux/blob/master/docs/api.md#arguments).

So let’s write inside our App.js (at the end of the file if you may):

```js
const mapStateToProps = state => ({
  ...state
});

const mapDispatchToProps = dispatch => ({
  startAction: () => dispatch(startAction),
  stopAction: () => dispatch(stopAction)
});
```

After this, let’s add them inside our connect function like so:

```js
export default connect(mapStateToProps, mapDispatchToProps)(App);
```

And right now, inside our App component, we can access the store state, the startAction and stopAction through props.

Let’s change the **img** tag to:

```jsx
<img 
  src={logo} 
  className={
    "App-logo" + 
    (this.props.rotating ? "":" App-logo-paused")
  } 
  alt="logo" 
  onClick={
    this.props.rotating ? 
      this.props.stopAction : this.props.startAction
  }
/>
```

So, what we are saying here is, if the store state of rotating (**this.props.rotating**) is true, then we want just the _App-logo_ **className** to be set to our **img**. If that is false, then we also want the _App-logo-paused_ class to be set in the **className**. This way we pause the animation.

Also, if **this.props.rotating** is **true**, then we want to send to our store for the **onClick** function and change it back to **false**, and vice-versa.

We are almost done, but we’ve forgot something.

We haven’t yet told our react app that we have a global state, or if you will, that we use redux state management.

For this, we go inside **src/index.js**, we import a **Provider** from **react-redux**, and the newly created store like so:

```js
import { Provider } from "react-redux";

import configureStore from "store";
```

* [Provider](https://react-redux.js.org/docs/api/provider): makes the Redux store available to any nested components that have been wrapped in the connect function

After this, instead of rendering our App component directly, we render it through our Provider using the store that we’ve created like so:

```js
ReactDOM.render(
  <Provider store={configureStore()}>
    <App />
  </Provider>,
  document.getElementById('root')
);
```

Here we could have used the **configureStore** function with some other state, for example **_configureStore({ rotating: false })_**.

So, your **index.js** should look like this:

```js
import React from 'react';
import ReactDOM from 'react-dom';
// new imports start
import { Provider } from "react-redux";

import configureStore from "store";
// new imports stop

import './index.css';

import App from './App';
import * as serviceWorker from './serviceWorker';

// changed the render
ReactDOM.render(
  <Provider store={configureStore()}>
    <App />
  </Provider>,
  document.getElementById('root')
);
// changed the render

serviceWorker.unregister();
```

Let’s go ahead and see if our redux app works:

![Image](https://cdn-media-1.freecodecamp.org/images/cOdx8xHzZjMmqEYSTgVkkPSXkG925Hwewoxj)
_**react** and **redux** in action_

### Using action creators

Optionally, instead of **actions**, we can use [action creators](https://redux.js.org/basics/actions#action-creators), which are functions that create actions.

This way, we can combine our two actions in just one function and reduce a bit our code.

So, let’s go ahead and create a new file:

1 — Linux / Mac command

```bash
touch src/actions/rotateAction.js
```

2 — Windows command

```bash
echo "" > src\actions\rotateAction.js
```

And add this code:

```jsx
const rotateAction = (payload) => {
  return {
    type: "rotate",
    payload
  }
}
export default rotateAction;
```

We are going to send an action of type rotate, with a payload that we are going to get in the App component.

Inside the src/App.js component, we need to import our new action creator:

```js
import rotateAction from "actions/rotateAction";
```

Add the new function to the mapDispatchToProps like so:

rotateAction: will receive a (payload) and will dispatch the rotateAction with the payload

Change the **onClick** function to:

```js
onClick={() => this.props.rotateAction(!this.props.rotating)}
```

And finally, add our new action creator to the **mapDispatchToProps** like this:

```js
rotateAction: (payload) => dispatch(rotateAction(payload))
```

We can also delete the old imports for the old actions, and delete them from the **mapDispatchToProps** as well.

This is how you new src/App.js should look like:

```jsx
import React, { Component } from 'react';
// new lines from here
import { connect } from "react-redux";
import rotateAction from "actions/rotateAction";

//// new lines to here

import logo from './logo.svg';
import './App.css';

class App extends Component {
  render() {
    console.log(this.props);
    return (
      <div className="App">
        <header className="App-header">
          <img
            src={logo}
            className={
              "App-logo" +
              (this.props.rotating ? "":" App-logo-paused")
            }
            alt="logo"
            onClick={
              () => this.props.rotateAction(!this.props.rotating)
            }
          />
          <p>
            Edit <code>src/App.js</code> and save to reload.
          </p>
          <a
            className="App-link"
            href="https://reactjs.org"
            target="_blank"
            rel="noopener noreferrer"
          >
            Learn React
          </a>
        </header>
      </div>
    );
  }
}

const mapStateToProps = state => ({
  ...state
});
const mapDispatchToProps = dispatch => ({
  rotateAction: (payload) => dispatch(rotateAction(payload))
});

export default connect(mapStateToProps, mapDispatchToProps)(App);
```

### A real-life example with [Paper Dashboard React](https://www.creative-tim.com/product/paper-dashboard-react)

![Image](https://cdn-media-1.freecodecamp.org/images/356UctzmEu8euFGJLpMVitFUDLy3LduQQTl4)
_**Paper Dashboard React** — Product Gif_

As you will see in the above gif image, I am using the right menu to change the colors of the menu on the left. This is achieved by using component states, and by passing that state from a parent component to the two menus and some functions to change that state.

![Image](https://cdn-media-1.freecodecamp.org/images/V3KhG508UOWnU1CA2FFtKEACx7vU3BRyDfyQ)
_small diagram on how the app works at the moment_

I thought it would be a nice example, to take this product and replace the component states with Redux.

You can get it in these 3 ways:

1. Download from [creative-tim.com](https://www.creative-tim.com/product/paper-dashboard-react)
2. Download from [Github](https://github.com/creativetimofficial/paper-dashboard-react)
3. Clone from Github:

```bash
git clone https://github.com/creativetimofficial/paper-dashboard-react.git
```

Now that we have this product, let’s cd into it and install again redux and react-redux:

```bash
npm install --save redux react-redux
```

After this, we need to create the actions. Since in the right menu we have 2 colors that set the background of the left menu, and 5 colors that change the color of the links, we need 7 actions, or 2 actions creators — and we are going with this second option since it is a bit less code to write:

1 — Linux / Mac commands

```bash
mkdir src/actions
touch src/actions/setBgAction.js
touch src/actions/setColorAction.js
```

2 — Windows commands

```bash
mkdir src\actions
echo "" > src\actions\setBgAction.js
echo "" > src\actions\setColorAction.js
```

After this, let’s create the actions code as follows:

— **src/actions/setBgAction.js**

```js
const setBgAction = (payload) => {
  return {
    type: "bgChange",
    payload
  }
}
export default setBgAction;
```

— **src/actions/setColorAction.js**

```js
const setColorAction = (payload) => {
  return {
    type: "colorChange",
    payload
  }
}
export default setColorAction;
```

Now, as in the first part, we need the reducer:

1 — Linux / Mac commands

```bash
mkdir src/reducers
touch src/reducers/rootReducer.js
```

2 — Windows commands

```bash
mkdir src\reducers
echo "" > src\reducers\rootReducer.js
```

And the code for the reducer:

```js
export default (state, action) => {
  switch (action.type) {
    case "bgChange":
      return {
        ...state,
        bgColor: action.payload
      };
    case "colorChange":
      return {
        ...state,
        activeColor: action.payload
      };
    default:
      return state;
  }
};
```

As you can see here, unlike our first example, we want to keep our old state and update its contents.

We also need the store:

1 — Linux / Mac command

```bash
touch src/store.js
```

2 — Windows command

```bash
echo "" > src\store.js
```

The code for it:

```js
import { createStore } from "redux";
import rootReducer from "reducers/rootReducer";

function configureStore(state = { bgColor: "black", activeColor: "info" }) {
  return createStore(rootReducer,state);
}
export default configureStore;
```

Inside the src/index.js we need:

```js
// new imports start
import { Provider } from "react-redux";

import configureStore from "store";
// new imports stop
```

And also, change the **render** function:

```js
ReactDOM.render(
  <Provider store={configureStore()}>
    <Router history={hist}>
      <Switch>
        {indexRoutes.map((prop, key) => {
          return <Route path={prop.path} key={key} component={prop.component} />;
        })}
      </Switch>
    </Router>
  </Provider>,
  document.getElementById("root")
);
```

So the **index.js** file should look like this:

```js
import React from "react";
import ReactDOM from "react-dom";
import { createBrowserHistory } from "history";
import { Router, Route, Switch } from "react-router-dom";
// new imports start
import { Provider } from "react-redux";

import configureStore from "store";
// new imports stop

import "bootstrap/dist/css/bootstrap.css";
import "assets/scss/paper-dashboard.scss";
import "assets/demo/demo.css";

import indexRoutes from "routes/index.jsx";

const hist = createBrowserHistory();

ReactDOM.render(
  <Provider store={configureStore()}>
    <Router history={hist}>
      <Switch>
        {indexRoutes.map((prop, key) => {
          return <Route path={prop.path} key={key} component={prop.component} />;
        })}
      </Switch>
    </Router>
  </Provider>,
  document.getElementById("root")
);
```

Now we need to make some changes inside **src/layouts/Dashboard/Dashboard.jsx**. We need to delete the state and the functions that change the state. So go ahead and **delete these bits of code:**

The constructor (between lines 16 and 22):

```jsx
constructor(props){
  super(props);
  this.state = {
    backgroundColor: "black",
    activeColor: "info",
  }
}
```

The state functions (between lines 41 and 46):

```jsx
handleActiveClick = (color) => {
    this.setState({ activeColor: color });
  }
handleBgClick = (color) => {
  this.setState({ backgroundColor: color });
}
```

The sidebar **bgColor** and **activeColor** props (lines 53 and 54):

```jsx
bgColor={this.state.backgroundColor}
activeColor={this.state.activeColor}
```

All of the FixedPlugin props (between lines 59–62):

```jsx
bgColor={this.state.backgroundColor}
activeColor={this.state.activeColor}
handleActiveClick={this.handleActiveClick}
handleBgClick={this.handleBgClick}
```

So, we remain with this code inside the Dashboard layout component:

```jsx
import React from "react";
// javascript plugin used to create scrollbars on windows
import PerfectScrollbar from "perfect-scrollbar";
import { Route, Switch, Redirect } from "react-router-dom";

import Header from "components/Header/Header.jsx";
import Footer from "components/Footer/Footer.jsx";
import Sidebar from "components/Sidebar/Sidebar.jsx";
import FixedPlugin from "components/FixedPlugin/FixedPlugin.jsx";

import dashboardRoutes from "routes/dashboard.jsx";

var ps;

class Dashboard extends React.Component {
  componentDidMount() {
    if (navigator.platform.indexOf("Win") > -1) {
      ps = new PerfectScrollbar(this.refs.mainPanel);
      document.body.classList.toggle("perfect-scrollbar-on");
    }
  }
  componentWillUnmount() {
    if (navigator.platform.indexOf("Win") > -1) {
      ps.destroy();
      document.body.classList.toggle("perfect-scrollbar-on");
    }
  }
  componentDidUpdate(e) {
    if (e.history.action === "PUSH") {
      this.refs.mainPanel.scrollTop = 0;
      document.scrollingElement.scrollTop = 0;
    }
  }
  render() {
    return (
      <div className="wrapper">
        <Sidebar
          {...this.props}
          routes={dashboardRoutes}
        />
        <div className="main-panel" ref="mainPanel">
          <Header {...this.props} />
          <Switch>
            {dashboardRoutes.map((prop, key) => {
              if (prop.pro) {
                return null;
              }
              if (prop.redirect) {
                return <Redirect from={prop.path} to={prop.pathTo} key={key} />;
              }
              return (
                <Route path={prop.path} component={prop.component} key={key} />
              );
            })}
          </Switch>
          <Footer fluid />
        </div>
        <FixedPlugin />
      </div>
    );
  }
}

export default Dashboard;
```

We need to connect the **Sidebar** and **FixedPlugin** components to to the store.

For **src/components/Sidebar/Sidebar.jsx**:

```jsx
import { connect } from "react-redux";
```

And change the export to:

```jsx
const mapStateToProps = state => ({
  ...state
});

export default connect(mapStateToProps)(Sidebar);
```

For the **src/components/FixedPlugin/FixedPlugin.jsx**:

```jsx
import { connect } from "react-redux";
import setBgAction from "actions/setBgAction";
import setColorAction from "actions/setColorAction";
```

And the export should now be:

```jsx
const mapStateToProps = state => ({
  ...state
});

const mapDispatchToProps = dispatch => ({
  setBgAction: (payload) => dispatch(setBgAction(payload)),
  setColorAction: (payload) => dispatch(setColorAction(payload))
});

export default connect(mapStateToProps, mapDispatchToProps)(FixedPlugin);
```

We are going to have these next changes:

* anywhere you find the word **handleBgClick**, you’ll need to change it to **setBgAction**
* anywhere you find the word **handleActiveClick**, you’ll need to change it to **setColorAction**

So, the FixedPlugin component should now look like this:

```jsx
import React, { Component } from "react";

import { connect } from "react-redux";
import setBgAction from "actions/setBgAction";
import setColorAction from "actions/setColorAction";

import Button from "components/CustomButton/CustomButton.jsx";

class FixedPlugin extends Component {
  constructor(props) {
    super(props);
    this.state = {
      classes: "dropdown show"
    };
    this.handleClick = this.handleClick.bind(this);
  }
  handleClick() {
    if (this.state.classes === "dropdown") {
      this.setState({ classes: "dropdown show" });
    } else {
      this.setState({ classes: "dropdown" });
    }
  }
  render() {
    return (
      <div className="fixed-plugin">
        <div className={this.state.classes}>
          <div onClick={this.handleClick}>
            <i className="fa fa-cog fa-2x" />
          </div>
          <ul className="dropdown-menu show">
            <li className="header-title">SIDEBAR BACKGROUND</li>
            <li className="adjustments-line">
              <div className="badge-colors text-center">
                <span
                  className={
                    this.props.bgColor === "black"
                      ? "badge filter badge-dark active"
                      : "badge filter badge-dark"
                  }
                  data-color="black"
                  onClick={() => {
                    this.props.setBgAction("black");
                  }}
                />
                <span
                  className={
                    this.props.bgColor === "white"
                      ? "badge filter badge-light active"
                      : "badge filter badge-light"
                  }
                  data-color="white"
                  onClick={() => {
                    this.props.setBgAction("white");
                  }}
                />
              </div>
            </li>
            <li className="header-title">SIDEBAR ACTIVE COLOR</li>
            <li className="adjustments-line">
              <div className="badge-colors text-center">
                <span
                  className={
                    this.props.activeColor === "primary"
                      ? "badge filter badge-primary active"
                      : "badge filter badge-primary"
                  }
                  data-color="primary"
                  onClick={() => {
                    this.props.setColorAction("primary");
                  }}
                />
                <span
                  className={
                    this.props.activeColor === "info"
                      ? "badge filter badge-info active"
                      : "badge filter badge-info"
                  }
                  data-color="info"
                  onClick={() => {
                    this.props.setColorAction("info");
                  }}
                />
                <span
                  className={
                    this.props.activeColor === "success"
                      ? "badge filter badge-success active"
                      : "badge filter badge-success"
                  }
                  data-color="success"
                  onClick={() => {
                    this.props.setColorAction("success");
                  }}
                />
                <span
                  className={
                    this.props.activeColor === "warning"
                      ? "badge filter badge-warning active"
                      : "badge filter badge-warning"
                  }
                  data-color="warning"
                  onClick={() => {
                    this.props.setColorAction("warning");
                  }}
                />
                <span
                  className={
                    this.props.activeColor === "danger"
                      ? "badge filter badge-danger active"
                      : "badge filter badge-danger"
                  }
                  data-color="danger"
                  onClick={() => {
                    this.props.setColorAction("danger");
                  }}
                />
              </div>
            </li>
            <li className="button-container">
              <Button
                href="https://www.creative-tim.com/product/paper-dashboard-react"
                color="primary"
                block
                round
              >
                Download now
              </Button>
            </li>
            <li className="button-container">
              <Button
                href="https://www.creative-tim.com/product/paper-dashboard-react/#/documentation/tutorial"
                color="default"
                block
                round
                outline
              >
                <i className="nc-icon nc-paper"></i> Documentation
              </Button>
            </li>
            <li className="header-title">Want more components?</li>
            <li className="button-container">
              <Button
                href="https://www.creative-tim.com/product/paper-dashboard-pro-react"
                color="danger"
                block
                round
                disabled
              >
                Get pro version
              </Button>
            </li>
          </ul>
        </div>
      </div>
    );
  }
}

const mapStateToProps = state => ({
  ...state
});

const mapDispatchToProps = dispatch => ({
  setBgAction: (payload) => dispatch(setBgAction(payload)),
  setColorAction: (payload) => dispatch(setColorAction(payload))
});

export default connect(mapStateToProps, mapDispatchToProps)(FixedPlugin);
```

And we are done, you can start the project and see how everything works fine:

![Image](https://cdn-media-1.freecodecamp.org/images/Pxtk6P8ssePiK2LaAmOuG4tvn8SCXwJPVKs3)

### Multiple reducers

As you can have multiple actions, you can have multiple reducers. The only thing is that you need to combine them — we’ll see this a bit further down.

Let’s go ahead and create two new reducers for our app, one for the **setBgAction** and one for the **setColorAction**:

1 — Linux / Mac commands

```bash
touch src/reducers/bgReducer.js
touch src/reducers/colorReducer.js
```

2 — Windows commands

```bash
echo "" > src\reducers\bgReducer.js
echo "" > src\reducers\colorReducer.js
```

After this, let’s create the reducers’ code as follows:

— **src/reducers/bgReducer.js**

```js
export default (state = {}, action) => {
  switch (action.type) {
    case "bgChange":
      return {
        ...state,
        bgColor: action.payload
      };
    default:
      return state;
  }
};
```

— **src/reducers/colorReducer.js**

```js
export default (state = {} , action) => {
  switch (action.type) {
    case "colorChange":
      return {
        ...state,
        activeColor: action.payload
      };
    default:
      return state;
  }
};
```

When working with combined reducers, you need to add a **default state** in each of your reducers that are going to be combined. In my case, I’ve chosen an empty object i.e. **state = {}**;

And now, our **rootReducer** will combine these two as follows:

— **src/reducers/rootReducer.js**

```js
import { combineReducers } from 'redux';

import bgReducer from 'reducers/bgReducer';
import colorReducer from 'reducers/colorReducer';

export default combineReducers({
  activeState: colorReducer,
  bgState: bgReducer
});
```

So, we say that we want the **colorReducer** to be referred by the **activeState** prop of the app state, and the **bgReducer** to be referred by the **bgState** prop of the app state.

This means that our state will no longer look like this:

```js
state = {
  activeColor: "color1",
  bgColor: "color2"
}
```

It will now look like this:

```js
state = {
  activeState: {
    activeColor: "color1"
  },
  bgState: {
    bgColor: "color2"
  }
}
```

Since we’ve changed our reducers, now we’ve now combined them together into just one, we need to change our **store.js** as well:

— **src/store.js**

```js
import { createStore } from "redux";
import rootReducer from "reducers/rootReducer";

// we need to pass the initial state with the new look
function configureStore(state = { bgState: {bgColor: "black"}, activeState: {activeColor: "info"} }) {
  return createStore(rootReducer,state);
}
export default configureStore;
```

Since we’ve changed the way the state looks, we now need to change the props inside the **Sidebar** and **FixedPlugin** components to the new state object:

— **src/components/Sidebar/Sidebar.jsx**:

Change **line 36** from

```jsx
<div className="sidebar" data-color={this.props.bgColor} data-active-color={this.props.activeColor}>
```

to

```jsx
<div className="sidebar" data-color={this.props.bgState.bgColor} data-active-color={this.props.activeState.activeColor}>
```

— **src/components/FixedPlugin/FixedPlugin.jsx**:

We need to change all the `**this.props.bgColor**` to `**this.props.bgState.bgColor**` . And all the `**this.props.activeColor**` to `**this.props.activeState.activeColor**` .

So the new code should look like this:

```jsx
import React, { Component } from "react";

import Button from "components/CustomButton/CustomButton.jsx";

import { connect } from "react-redux";
import setBgAction from "actions/setBgAction";
import setColorAction from "actions/setColorAction";

class FixedPlugin extends Component {
  constructor(props) {
    super(props);
    this.state = {
      classes: "dropdown show"
    };
    this.handleClick = this.handleClick.bind(this);
  }
  handleClick() {
    if (this.state.classes === "dropdown") {
      this.setState({ classes: "dropdown show" });
    } else {
      this.setState({ classes: "dropdown" });
    }
  }
  render() {
    return (
      <div className="fixed-plugin">
        <div className={this.state.classes}>
          <div onClick={this.handleClick}>
            <i className="fa fa-cog fa-2x" />
          </div>
          <ul className="dropdown-menu show">
            <li className="header-title">SIDEBAR BACKGROUND</li>
            <li className="adjustments-line">
              <div className="badge-colors text-center">
                <span
                  className={
                    this.props.bgState.bgColor === "black"
                      ? "badge filter badge-dark active"
                      : "badge filter badge-dark"
                  }
                  data-color="black"
                  onClick={() => {
                    this.props.setBgAction("black");
                  }}
                />
                <span
                  className={
                    this.props.bgState.bgColor === "white"
                      ? "badge filter badge-light active"
                      : "badge filter badge-light"
                  }
                  data-color="white"
                  onClick={() => {
                    this.props.setBgAction("white");
                  }}
                />
              </div>
            </li>
            <li className="header-title">SIDEBAR ACTIVE COLOR</li>
            <li className="adjustments-line">
              <div className="badge-colors text-center">
                <span
                  className={
                    this.props.activeState.activeColor === "primary"
                      ? "badge filter badge-primary active"
                      : "badge filter badge-primary"
                  }
                  data-color="primary"
                  onClick={() => {
                    this.props.setColorAction("primary");
                  }}
                />
                <span
                  className={
                    this.props.activeState.activeColor === "info"
                      ? "badge filter badge-info active"
                      : "badge filter badge-info"
                  }
                  data-color="info"
                  onClick={() => {
                    this.props.setColorAction("info");
                  }}
                />
                <span
                  className={
                    this.props.activeState.activeColor === "success"
                      ? "badge filter badge-success active"
                      : "badge filter badge-success"
                  }
                  data-color="success"
                  onClick={() => {
                    this.props.setColorAction("success");
                  }}
                />
                <span
                  className={
                    this.props.activeState.activeColor === "warning"
                      ? "badge filter badge-warning active"
                      : "badge filter badge-warning"
                  }
                  data-color="warning"
                  onClick={() => {
                    this.props.setColorAction("warning");
                  }}
                />
                <span
                  className={
                    this.props.activeState.activeColor === "danger"
                      ? "badge filter badge-danger active"
                      : "badge filter badge-danger"
                  }
                  data-color="danger"
                  onClick={() => {
                    this.props.setColorAction("danger");
                  }}
                />
              </div>
            </li>
            <li className="button-container">
              <Button
                href="https://www.creative-tim.com/product/paper-dashboard-react"
                color="primary"
                block
                round
              >
                Download now
              </Button>
            </li>
            <li className="button-container">
              <Button
                href="https://www.creative-tim.com/product/paper-dashboard-react/#/documentation/tutorial"
                color="default"
                block
                round
                outline
              >
                <i className="nc-icon nc-paper"></i> Documentation
              </Button>
            </li>
            <li className="header-title">Want more components?</li>
            <li className="button-container">
              <Button
                href="https://www.creative-tim.com/product/paper-dashboard-pro-react"
                color="danger"
                block
                round
                disabled
              >
                Get pro version
              </Button>
            </li>
          </ul>
        </div>
      </div>
    );
  }
}

const mapStateToProps = state => ({
  ...state
});

const mapDispatchToProps = dispatch => ({
  setBgAction: (payload) => dispatch(setBgAction(payload)),
  setColorAction: (payload) => dispatch(setColorAction(payload))
});

export default connect(mapStateToProps, mapDispatchToProps)(FixedPlugin);
```

Let’s open the project again with `npm start` and see how everything works. Ta da!

### Thanks for reading!

If you’ve enjoyed reading this tutorial please share it. I am very keen on hearing your thoughts about it. Just give this thread a comment and I’ll be more than happy to reply.

Special thanks should also go to [Esther Falayi](https://medium.com/@estherfalayi) for his [tutorial](https://medium.com/backticks-tildes/setting-up-a-redux-project-with-create-react-app-e363ab2329b8) which has given me some much needed understanding on **Redux**.

Useful links:

* Get the code for this tutorial from [Github](https://github.com/creativetimofficial/react-redux-tutorial)
* Read more about ReactJS on [their official website](https://reactjs.org/)
* Read more about [Redux here](https://redux.js.org/)
* Read more about [React-Redux](https://react-redux.js.org/)
* Check out our platform to see [what we are doing](https://www.creative-tim.com/) and [who we are](https://www.creative-tim.com/presentation)
* Get Paper Dashboard React from [www.creative-tim.com](https://www.creative-tim.com/product/paper-dashboard-react) or from [Github](https://github.com/creativetimofficial/paper-dashboard-react)
* Read more about [Reactstrap](https://reactstrap.github.io/), the core of Paper Dashboard React

Find me on:

* Email: [manu@creative-tim.com](mailto:manu@creative-tim.com)
* Facebook: [https://www.facebook.com/NazareEmanuel](https://www.facebook.com/NazareEmanuel)
* Instagram: [https://www.instagram.com/manu.nazare/](https://www.instagram.com/manu.nazare/)
* Linkedin: [https://www.linkedin.com/in/nazare-emanuel-ioan-4298b5149/](https://www.linkedin.com/in/nazare-emanuel-ioan-4298b5149/)

