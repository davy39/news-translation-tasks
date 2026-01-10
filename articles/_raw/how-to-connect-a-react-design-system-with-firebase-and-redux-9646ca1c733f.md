---
title: How to connect a React Design System with Firebase and Redux
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-02T20:41:58.000Z'
originalURL: https://freecodecamp.org/news/how-to-connect-a-react-design-system-with-firebase-and-redux-9646ca1c733f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*gILubZM4zMQnVf4CAm-NSA.jpeg
tags:
- name: Design Systems
  slug: design-systems
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

  After almost two years of working with ReactJS at Creative-Tim, years while I’ve
  been creating simple front-end ReactJS projects, front-end templates, I have started
  to learn more about React, and create some tutorials.

  After l...'
---

By Nazare Emanuel Ioan

After almost two years of working with [ReactJS](https://reactjs.org/) at [Creative-Tim](https://www.creative-tim.com/?ref=trrfadr-medium), years while I’ve been creating simple front-end ReactJS projects, front-end templates, I have started to learn more about React, and create some tutorials.

After long hours of watching and reading firebase tutorials, firebase & react tutorials, and reading the officials docs of firebase, I am ready to write myself a tutorial.

**What I am going to use in this little tutorial article:**

* [npm@6.4.1](https://www.npmjs.com/package/npm)
* [nodejs@10.15.3 (LTS version)](https://nodejs.org/en/)
* [Atom Editor version 1.35.0](https://atom.io/)
* [Reactstrap](https://reactstrap.github.io/)

We are going to use Redux and Firebase for Login, Register and to create some dynamic stat cards.

I will focus my attention on Firebase, and give explanations just about this. If you do not know Redux, it would be best to take a look at my other [tutorial about what Redux is, and what it does](https://medium.freecodecamp.org/how-to-use-redux-in-reactjs-with-real-life-examples-687ab4441b85). After that, you can easily return here.

### Getting started with a React Design System

Since we do not have time to walk through creating our own design system — this would require days, weeks or even months to do — we will take one I’ve already worked on.

To get this project you can do one of the following (I am going to use the first option):

* Clone from Github:

```
git clone https://github.com/creativetimofficial/argon-dashboard-react.git
```

* [Download from Github](https://github.com/creativetimofficial/argon-dashboard-react/archive/master.zip) (by pressing the link, it will automatically start the download)
* [Download from Creative-Tim](https://www.creative-tim.com/product/argon-dashboard-react) (you will need to have an account there)

After you’ve got the project, cd into it (in my case will be):

```
cd argon-dashboard-react
```

Let’s start the product and see how it looks like:

```
npm run install:clean
```

![Image](https://cdn-media-1.freecodecamp.org/images/4gzCHNeU-XA-EKgRe8fPoLAb5iSp1QqRmHzA)
_npm run install:clean — output_

### Adding Redux to this starter template

#### Actions, Reducers, and Store

Let’s go back into the terminal and run:

```
npm i -E redux redux-thunk react-redux
```

When I ran this command, on my machine the installed versions were as follows:

* redux@4.0.1
* redux-thunk@2.3.0
* react-redux@6.0.1

At the beginning of the tutorial, we’ve set our goal to make two things happen: login and register (auth) and to be able to add some dynamic cards from our database (simple add). This means we’ll have two reducers, one for authentication and one for the dynamic cards (also, we’ll need one root reducer that will combine these two). We’ll also have four actions, one for login, one for register, one for adding the cards to our database (you can think about these as to some todos) and one for getting from the database all these cards (which we’ll render in our app). And also, just a store.

So, this being said let's run the following commands:

1 — Linux/Mac commands

```
mkdir src/actionsmkdir src/reducerstouch src/actions/addStatCardAction.jstouch src/actions/getAllStatCardsAction.jstouch src/actions/loginAction.jstouch src/actions/registerAction.jstouch src/reducers/statCardReducer.jstouch src/reducers/authReducer.jstouch src/reducers/rootReducer.jstouch src/store.js
```

2 — Windows commands

```
mkdir src\actionsmkdir src\reducersecho "" > src\actions\addStatCardAction.jsecho "" > src\actions\getAllStatCardsAction.jsecho "" > src\actions\loginAction.jsecho "" > src\actions\registerAction.jsecho "" > src\reducers\statCardReducer.jsecho "" > src\reducers\authReducer.jsecho "" > src\reducers\rootReducer.jsecho "" > src\store.js
```

#### Actions

**src/actions/addStatCardAction.js**

The stat card that we want to dynamically create is one of these:

![Image](https://cdn-media-1.freecodecamp.org/images/FuY9TJygUIsa-6GQcaufpcbow6BGjgMuuTxJ)
_stat cards to dynamically create_

As we can see, they have a name, a stat, an icon (that varies in color), a footer icon and percentage (that once again, varies in color) and a footer text.

So, we’ll need to create the action that will accept all of the above, like so:

```
const addStatCardAction = (  statName,  statDescription,  statIcon,  statIconColor,  statFooterIcon,  statFooterIconState,  statFooterPercentage,  statFooterText) => async dispatch => {  // here we'll make a call to our database (firebase)  // to add our new stat card with the above details
```

```
  dispatch({    type: "addStatCard",    payload: {      statName: statName,      statDescription: statDescription,      statIcon: statIcon,      statIconColor: statIconColor,      statFooterIcon: statFooterIcon,      statFooterIconState: statFooterIconState,      statFooterPercentage: statFooterPercentage,      statFooterText: statFooterText    }  });};
```

```
export default addStatCardAction;
```

As we can see, we’re going to work with async action creators, since we are making calls to a database. After the call is done, we’ll need to send to our store the data that we’ve just added to our database in firebase.

**src/actions/getAllStatCardsAction.js**

This one will not require any params, since it only retrieves something from the database. So the code will look like this:

```
const getAllStatCardsAction = () => async dispatch => {  // here we'll make a call to our database (firebase)  // that will retrieve all of our stat cards
```

```
  dispatch({ type: "getAllStatCards" , payload: {}});};
```

```
export default getAllStatCardsAction;
```

**src/actions/loginAction.js**

For login, we’ll have an email and a password, so this is the code for this action (also our login form has an email and a password):

```
const loginAction = (email, password) => async dispatch => {  // at the moment, since we haven't yet connected to the database  // we are going to say that each time we try to login  // we should not be able to log in (that is why we send false)
```

```
  dispatch({ type: "login", payload: false });};
```

```
export default loginAction;
```

**src/actions/registerAction.js**

```
const registerAction = (name, email, password) => async dispatch => {  // at the moment, since we haven't yet connected to the database  // we are going to say that each time we try to register  // we should not be able to register (that is why we send false)
```

```
  dispatch({ type: "register", payload: false });};
```

```
export default registerAction;
```

#### Reducers

**src/reducers/statCardReducer.js**

Since we have two actions about the stat card, we’ll have two cases in this reducer:

```
export default (state = {}, action) => {  switch (action.type) {    case "addStatCard":      console.log("adding ", action.payload);      // since we will always fetch our stat cards      // from firebase, each time we add one new      // we will just return the state      return state;    case "getAllStatCards":      console.log("getting ", action.payload);      console.log(action.payload);      return {        // keep the old state        ...state,        // add all the cards from the database        // they will come in a json format,        // so we need to convert them to array        statCardState: Object.values(action.payload)      };    default:      return state;  }};
```

We’re also logging what we are adding and what we are trying to get from our firebase.

**src/reducers/authReducer.js**

```
export default (state = {}, action) => {  switch (action.type) {    // in both cases, we want to tell our app,    // if the user is logged in or not    // if the user registers, he will automatically be logged in
```

```
    case "register":      console.log("register is ",action.payload);      return {        // keep old state        ...state,        // add true/false if the user is or not logged in        loggedIn: action.payload      };    case "login":      console.log("login is ",action.payload);      return {        // keep old state        ...state,        // add true/false if the user is or not logged in        loggedIn: action.payload      };    default:      return state;  }};
```

When we register a new user, we’ll automatically log them in. We’ve also added some logs to see if the registration or the login is successful.

**src/reducers/rootReducer.js**

This is for combining the above reducers:

```
import { combineReducers } from "redux";
```

```
import authReducer from "reducers/authReducer";import statCardReducer from "reducers/statCardReducer";
```

```
export default combineReducers({  // the authReducer will work only with authState  authState: authReducer,  // the statCardReducer will work only with statCardState  statCardState: statCardReducer});
```

#### Store

**src/store.js**

Since we have async action creators, we’ll need a middleware that will allow us to use these actions creators, hence the usage of redux-thunk:

```
import { createStore, applyMiddleware } from "redux";import reduxThunk from "redux-thunk";
```

```
import rootReducer from "reducers/rootReducer";
```

```
function configureStore(  state = { authState: {}, statCardState: {} }) {  return createStore(rootReducer, state, applyMiddleware(reduxThunk));}
```

```
export default configureStore;
```

#### Connecting our app to our store

At the moment, if we were to start our app, nothing would happen, since all the actions and our store are not being rendered in our app. So this is what we are going to do now.

First, let’s add our store, for this, we need to fo inside **src/index.js**.

Before the **ReactDOM.render()** function we need to add the following imports:

```
import { Provider } from "react-redux";import configureStore from "store";
```

And after that, we’ll wrap the **BrowserRouter** from the **ReactDOM.render()** function inside the **Provider** tag as follows:

```
<Provider store={configureStore()}>  <BrowserRouter>    <Switch>      <Route path="/admin" render={          props => <AdminLayout {...props} />      } />      <Route path="/auth" render={          props => <AuthLayout {...props} />      } />      <Redirect from="/" to="/admin/index" />    </Switch>  </BrowserRouter></Provider>,
```

Our next concern is to make our users to be redirected to the login page if not authenticated and if they are authenticated to be redirected to the user page. Basically, if they are logged in, they will not be able to access the Auth layout (**src/layouts/Auth.jsx**), and if they are not, they won’t be able to access the Admin layout (**src/layouts/Admin.jsx**).

Let’s go inside **src/layouts/Auth.jsx** and after the **React** import, make the following imports:

```
import { connect } from "react-redux";import { Redirect } from "react-router-dom";
```

After that let’s change the export of this component as follows:

```
const mapStateToProps = state => ({  ...state});
```

```
export default connect(  mapStateToProps,  {})(Auth);
```

After this, we go inside the **render function** of this component, and before the **return**, add the following code:

```
if (this.props.authState.loggedIn) {  return <Redirect to="/admin/user-profile" />;}
```

So, if the user is authenticated, they will be redirected to their profile page.

Next, we go inside **src/layouts/Admin.jsx** and make the same changes as with the **Auth** layout. So add the following imports:

```
import { connect } from "react-redux";import { Redirect } from "react-router-dom";
```

Change it’s export to:

```
const mapStateToProps = state => ({  ...state});
```

```
export default connect(  mapStateToProps,  {})(Admin);
```

Once again, in the **render function**, before the **return** we add:

```
if (!this.props.authState.loggedIn) {  return <Redirect to="/auth/login" />;}
```

This time, we say **!this.props.authState.loggedIn**, since we want the user to be redirected to the login page if they are not authenticated.

Let us start again our project and see how, each time if we try to navigate to the **Dashboard** or **Profile,** we are not allowed since we are not logged in.

![Image](https://cdn-media-1.freecodecamp.org/images/i3yIhiqSEGtBulgXHfqhvGcYUVs9qQuB8zot)
_Project after adding the redirects_

Now, we need to go inside the **Login** and **Register** view-pages and add Redux to them as well.

#### Connecting our Login page to redux using loginAction

First, let's go inside **src/views/examples/Login.jsx** and after the **React** import, add these imports:

```
import { connect } from "react-redux";
```

```
import loginAction from "actions/loginAction";
```

Then, change the export at the end of the file with this:

```
const mapStateToProps = state => ({  ...state});
```

```
const mapDispatchToProps = dispatch => ({  loginAction:   (email, password) => dispatch(loginAction(email, password))});
```

```
export default connect(  mapStateToProps,  mapDispatchToProps)(Login);
```

Now, before the render function we write:

```
state = {  email: "",  password: ""};onChange = (stateName, value) => {  this.setState({    [stateName]: value  });};
```

We’ll need to keep a local **state** for the email and password and send these two to our firebase.

Then, we need to change _line 85_ from:

```
<Input placeholder="Email" type="email" />
```

To:

```
<Input  placeholder="Email"  type="email"  onChange={e => this.onChange("email", e.target.value)}/>
```

We’ll also change _line 99_ from:

```
<Input placeholder="Password" type="password" />
```

To:

```
<Input  placeholder="Password"  type="password"  onChange={e => this.onChange("password", e.target.value)}/>
```

We’re almost set for the login. Next we need to change the **Sign in** button so that, when we press it, it will call the **loginAction**. So change it from:

```
<Button className="my-4" color="primary" type="button">  Sign in</Button>
```

To:

```
<Button  className="my-4"  color="primary"  type="button"  onClick={() =>    this.props.loginAction(      this.state.email,      this.state.password    )  }>  Sign in</Button>
```

Now go back in your browser, and on the **Login** page, open your console, and try to log in. You should get an output of **login is _false_**. So we know that our **action** and our **reducer** work.

![Image](https://cdn-media-1.freecodecamp.org/images/ph56L3CSbnOONWONDMOIKWBTCCsIjzahNieS)
_**login is false**_

#### Connecting our Register page to redux using registerAction

Go inside **src/views/examples/Register.jsx** and do the same as the above. So first add the imports (this time with the **registerAction**):

```
import { connect } from "react-redux";
```

```
import registerAction from "actions/registerAction";
```

Then, the export to:

```
const mapStateToProps = state => ({  ...state});
```

```
const mapDispatchToProps = dispatch => ({  registerAction: (name, email, password) => dispatch(registerAction(name, email, password))});
```

```
export default connect(  mapStateToProps,  mapDispatchToProps)(Register);
```

Add the following before the **render function**:

```
state = {  name: "",  email: "",  password: ""};onChange = (stateName, value) => {  this.setState({    [stateName]: value  });};
```

Change:

```
<Input placeholder="Name" type="text" />
```

To:

```
<Input placeholder="Name" type="text" onChange={e => this.onChange("name", e.target.value)}/>
```

Then:

```
<Input placeholder="Email" type="email" />
```

To:

```
<Input placeholder="Email" type="email" onChange={e => this.onChange("email", e.target.value)}/>
```

And lastly, the password as well:

```
<Input placeholder="Password" type="password" />
```

To:

```
<Input placeholder="Password" type="password" onChange={e => this.onChange("password", e.target.value)}/>
```

One more thing — the button, we need to change it from:

```
<Button className="mt-4" color="primary" type="button">  Create account</Button>
```

To:

```
<Button className="mt-4" color="primary" type="button"   onClick={() =>  this.props.registerAction(    this.state.name,    this.state.email,    this.state.password  )}>  Create account</Button>
```

So, we are all set with Redux. Again, go to the Register page, type something inside the form, and then press the Create account button with the console opened. You should get a **register is _false_**.

![Image](https://cdn-media-1.freecodecamp.org/images/jjNR3gDDVOYzZndVi3TpdZa3Qx7BXWSiTkPB)
_**register is false**_

#### Connecting our Header component to redux using addStatCardAction and getAllStatCardsAction actions

Now we need to make our **Stat Cards** from the **Header** component (this component can be seen for example inside the **Dashboard** page) to be rendered from our **store/firebase**, and also, make them create dynamically — for example on a **button click**.

Go inside **src/components/Headers/Header.jsx** and add the following **imports** (after the **React import**):

```
import {connect} from "react-redux";
```

```
import addStatCardAction from "actions/addStatCardAction";import getAllStatCardsAction from "actions/getAllStatCardsAction";
```

```
import { Button } from "reactstrap";
```

Change the **default export** to:

```
const mapStateToProps = state => ({  ...state});const mapDispatchToProps = dispatch => ({  getAllStatCardsAction: () => dispatch(getAllStatCardsAction()),  addStatCardAction: (    statName,    statDescription,    statIcon,    statIconColor,    statFooterIcon,    statFooterIconState,    statFooterPercentage,    statFooterText  ) =>    dispatch(      addStatCardAction(        statName,        statDescription,        statIcon,        statIconColor,        statFooterIcon,        statFooterIconState,        statFooterPercentage,        statFooterText      )    )});
```

```
export default connect(  mapStateToProps,  mapDispatchToProps)(Header);
```

Then, let’s add a **componentDidMount** function right before the **render** one as follows:

```
componentDidMount(){  this.props.getAllStatCardsAction();}
```

And now, after the first **div** inside the **return** statement of the **render** function, we’ll add a **Button** that will add our stat cards inside our firebase:

```
<Container>  <Row>    <Col lg="6" xl="3">      <Button        color="primary"        onClick={() =>          this.props.addStatCardAction(            "Performance",            "49,65%",            "fas fa-percent",            "bg-info text-white rounded-circle shadow",            "fas fa-arrow-up",            "text-success",            " 12%",            "Since last month"          )        }      >        Add stat card      </Button>    </Col>  </Row></Container><br />
```

And, we now need to delete the whole contents of the **Row** tag (~_lines 48–165_ — from **<R**ow&g**t; to** </Row>), and replace it with the following:

```
{// we first verify if the statCardState is undefined  this.props.statCardState &&  // then verify if the statCardState.statCardState is  // populated with cards from our firebase  this.props.statCardState.statCardState &&  // and lastly, we render them using the map function  this.props.statCardState.statCardState.map((prop, key) => {    return (      <Col lg="6" xl="3" key={key}>        <Card className="card-stats mb-4 mb-xl-0">          <CardBody>            <Row>              <div className="col">                <CardTitle                  tag="h5"                  className="text-uppercase text-muted mb-0"                >                  {prop.statName}                </CardTitle>                <span className="h2 font-weight-bold mb-0">                  {prop.statDescription}                </span>              </div>              <Col className="col-auto">                <div                  className={                    "icon icon-shape " + prop.statIconColor                  }                >                  <i className={prop.statIcon} />                </div>              </Col>            </Row>            <p className="mt-3 mb-0 text-muted text-sm">              <span                className={"mr-2 " + prop.statFooterIconState}              >                <i className={prop.statFooterIcon} />{" "}                {prop.statFooterPercentage}              </span>{" "}              <span className="text-nowrap">                {prop.statFooterText}              </span>            </p>          </CardBody>        </Card>      </Col>    );  })}
```

### Adding Firebase

#### Setting Firebase Account

For this, you need to have a [Google Account](https://myaccount.google.com/). If you do not have one, Google offers you a fast (1 minute) [Guide](https://support.google.com/mail/answer/56256?hl=en).

After you’ve made your account, sign into it, or if you have one, sign into that one.

After that, navigate to [this page](https://firebase.google.com/) (this is the homepage of firebase) and press the **GO TO CONSOLE** button, or just navigate directly to [this link](https://console.firebase.google.com/u/0/).

After that press on the **Add project** button. You will be prompted with a modal, with an input for a **name** (you can type whatever name you would like). For me, it will be **react-redux-firebase-tutorial**. You can leave everything else as is. **Accept the terms** and then press the **Create Project** button. You’ll have to wait a bit until it creates the project (around 30 seconds).

After that press the **Continue** button. That will automatically redirect you to the new project page. In the left menu press the **Authentication** link. On that press the **Set up sign-in method**. You will have a table with **Provider** and **Status**. Press on the line **Email/Password**. And check the first **Switch** and then press the **Save** button.

Now, go to **Database** link, scroll down the page and press **Create database** button, under the **Realtime Database**. After this, on the modal prompt that opens, choose **Start in test mode** radio and then press **Enable** and wait a few seconds.

Next, you’ll need to get your config file (config file that we will add it to our project in the next section). For this press on **Project Overview** link in the left menu, and after that press on the **<**;/> (Web) button. Cop**y the** config variable an**d the firebase initiali**zation. We’ll paste this in a new file, in the next section.

We are done!

We won’t need to create any tables for our users, our users’ details, or our dynamic cards, since firebase will automatically create them — we’ll talk about this in the next section.

Here are the above steps, as images:

![Image](https://cdn-media-1.freecodecamp.org/images/4COJIxHnrVZNkWZsV2SEUy9nnGooi5DfVNru)

![Image](https://cdn-media-1.freecodecamp.org/images/-J4f7OkHSJHNX4Q16tnQqQwOQHEPtSY0CcPY)

![Image](https://cdn-media-1.freecodecamp.org/images/g31yzK-Pt3iwx1ATEL0sZ9LoYdJDtH9rdp1o)

![Image](https://cdn-media-1.freecodecamp.org/images/lTBqKAmZs34jLSgyVeXPIsXp4f-r4dFsF9T0)

![Image](https://cdn-media-1.freecodecamp.org/images/qExTP7hRuHk3F0aQv3RCK3U28patPZ5BdBFj)

![Image](https://cdn-media-1.freecodecamp.org/images/0HzPZhEt2cWYBO8beQSPTb5GWVARZ7M6tZRE)

![Image](https://cdn-media-1.freecodecamp.org/images/wAhTEBfWmsLgX66S-BUVlcKF-5nR3-Fkvb3z)

![Image](https://cdn-media-1.freecodecamp.org/images/nkxMOuEp9SUWVSwA36DAqX3EXXwXpu5J5kST)

![Image](https://cdn-media-1.freecodecamp.org/images/htFFlwaTuyNn6okH9urG1askjORredSC9Eob)

![Image](https://cdn-media-1.freecodecamp.org/images/eYC-jXvLpX3Mpu9EKcvEp0cJMtpydCw1TjsF)

![Image](https://cdn-media-1.freecodecamp.org/images/VG9txfaAPtpb5tjGLoTAJnSyqcDa0qYsAb5H)

![Image](https://cdn-media-1.freecodecamp.org/images/WoAZ5etvIEG9uJ8BaSYwrMMKxgIk8ADx3XL9)

![Image](https://cdn-media-1.freecodecamp.org/images/9MwpNj7l32x5CqxCsVjV7fgciMHcBqFug8r2)

![Image](https://cdn-media-1.freecodecamp.org/images/GygAEXlsQoQlvAoFOG9GAT0EGD3BTU6IoQcZ)
_**Setting up a firebase project**_

#### Adding Firebase to our project

Let’s install **firebase** in our app:

```
npm i -E firebase
```

After this, we need to create a file for configuring our firebase in our app, so:

1 — Linux/Mac commands

```
touch src/firebaseConfig.js
```

2 — Windows commands

```
echo "" > src\firebaseConfig.js
```

And let’s import **firebase** in this file, and then export firebase with the initialization (you need the code from the previous section — see the last image):

```
import * as firebase from "firebase";
```

```
// replace this variable, with your own config variable// from your firebase projectvar config = {  apiKey: "YOUR_KEY_HERE",  authDomain: "YOUR_DOMAIN_HERE",  databaseURL: "YOUR_URL_HERE",  projectId: "YOUR_ID_HERE",  storageBucket: "YOUR_BUCKET_HERE",  messagingSenderId: "YOUR_ID_HERE"};
```

```
let firebaseConfig = firebase.initializeApp(config);
```

```
export default firebaseConfig;
```

Now, we can import our **firebaseConfig** everywhere we need it.

#### Register

Let us first make our **registerAction** functional. So, we go inside **src/actions/registerAction.js** and at the beginning of the file we import our firebase config:

```
import firebase from "firebaseConfig";
```

After this, we may need for our users to keep stuff, like their name, their photos etc. so we are going to create a new table called user-details. If it doesn’t exist, add in it the name of our user.

Our form only has email, password, and name — firebase will automatically create a database table in which it will only put the credentials (email and password) of the account. So if we want to keep more details about our users, we’ll need to create a new table — my table will have the ID of the user, from the table with the credentials, and the user’s name.

So after the above import, we say:

```
// get me the firebase database
```

```
const databaseRef = firebase.database().ref();
```

```
// get me the table named user-details// if it does not exist, firebase will// automatically create it
```

```
const userDetailsRef = databaseRef.child("user-details");
```

After that, we’ll change our dispatch code from:

```
dispatch({ type: "register", payload: false });
```

To:

```
// firebase offers us this function createUserWithEmailAndPassword// which will automatically create the user for us// it only has two arguments, the email and the password
```

```
firebase.auth().createUserWithEmailAndPassword(email, password)
```

```
// then() function is used to know when the async call has ended// that way, we can notify our reducers that register was succesful
```

```
.then(function(user) {
```

```
  // we take the user id and it's name and we add it in our  // user-details table
```

```
  userDetailsRef.push().set({userId: user.user.uid, userName: name});
```

```
  // after that we dispatch to our reducers the fact that  // register was succesful by sending true
```

```
  dispatch({type:"register", payload: true});
```

```
// if the register was not succesful we can catch the erros here
```

```
}).catch(function(error) {
```

```
  // if we have any erros, we'll throw an allert with that error
```

```
  alert(error);
```

```
});
```

So in the end, our **registerAction** will look like this:

```
import firebase from "firebaseConfig";
```

```
const databaseRef = firebase.database().ref();const userDetailsRef = databaseRef.child("user-details");
```

```
const registerAction = (name, email, password) => async dispatch => {  firebase    .auth()    .createUserWithEmailAndPassword(email, password)    .then(function(user) {      userDetailsRef.push().set(        { userId: user.user.uid, userName: name }      );      dispatch({ type: "register", payload: true });    })    .catch(function(error) {      alert(error);    });};
```

```
export default registerAction;
```

Open the app again, and go to the register page. Type a name, a valid email and a password (something simple to remember — something like **qwerty**). After you press the **Create account** button you should be redirected to the **user-profile** page — this means that our registration was successful. We can now go back to our **firebase project** ([https://console.firebase.google.com/u/0/](https://console.firebase.google.com/u/0/) — press on your project), click the **Authentication** link, and we’ll see that email that we’ve just written. Also, if we go to the **Database** link, we’ll see our **user-details** table.

![Image](https://cdn-media-1.freecodecamp.org/images/Fcvn-A-fMjcOHvtni0hCQNwIm3UAEtIOulZh)
_**Register action is now working**_

#### **Login**

we go inside **src/actions/loginAction.js** and at the beginning of the file we import our firebase config:

```
import firebase from "firebaseConfig";
```

For this action, we won’t need anything else, so the next thing is to change our dispatch code from:

```
dispatch({ type: "login", payload: false });
```

To:

```
// firebase offers us this function signInWithEmailAndPassword// which will automatically create the user for us// it only has two arguments, the email and the password
```

```
firebase  .auth()  .signInWithEmailAndPassword(email, password)  // then() function is used to know when the async call has ended  // that way, we can notify our reducers that login was succesful    .then(function(user) {    // if the login was succesful, then     // we dispatch to our reducers the fact that    // login was succesful by sending true    dispatch({type:"login", payload: "true"});  })
```

```
// if the login was not succesful we can catch the erros here    .catch(function(error) {
```

```
// if we have any erros, we'll throw an allert with that error        alert(error);  });
```

So in the end, our **loginAction** should look like this:

```
import firebase from "firebaseConfig";
```

```
const loginAction = (email, password) => async dispatch => {  firebase    .auth()    .signInWithEmailAndPassword(email, password)    .then(function(user) {      dispatch({ type: "login", payload: "true" });    })    .catch(function(error) {      alert(error);    });};
```

```
export default loginAction;
```

If we open again our app (we should be redirected by default to **Login** page), and if we enter our email and password, we will be able to login to our new account.

![Image](https://cdn-media-1.freecodecamp.org/images/KiDtGPZVvtaeDG8QbYNQxgjUcZgn1dEpoCxK)
_**Login action working**_

#### Add stat cards and render them

Now, we need to make some changes to our actions regarding the stat cards.

Inside **src/actions/getAllStatCardsAction.js** we need to add the following **imports**:

```
import firebase from "firebaseConfig";
```

```
const databaseRef = firebase.database().ref();// this is to get the stat-cards table from firebaseconst statCardsRef = databaseRef.child("stat-cards");
```

Then we need to change the **dispatch** from:

```
dispatch({ type: "getAllStatCards", payload: {} });
```

To:

```
// this function will get all the entires of the// stat-cards table, in a json formatstatCardsRef.on("value", snapshot => {  dispatch({    type: "getAllStatCards",    // if the json returns null, i.e. the    // stat-cards table is blank - empty    // then we'll return an empty object    payload: snapshot.val() || {}  });});
```

This is how the action should now look:

```
import firebase from "firebaseConfig";
```

```
const databaseRef = firebase.database().ref();const statCardsRef = databaseRef.child("stat-cards");
```

```
const getAllStatCardsAction = () => async dispatch => {  statCardsRef.on("value", snapshot => {    dispatch({      type: "getAllStatCards",      payload: snapshot.val() || {}    });  });};
```

```
export default getAllStatCardsAction;
```

Next, is the **src/actions/addStatCardAction.js**. Like the previous one, we need some imports:

```
import firebase from "firebaseConfig";
```

```
const databaseRef = firebase.database().ref();const statCardsRef = databaseRef.child("stat-cards");
```

Now, instead of the simple dispatch, we’ll overwrite it from:

```
dispatch({  type: "addStatCard",  payload: {    statName: statName,    statDescription: statDescription,    statIcon: statIcon,    statIconColor: statIconColor,    statFooterIcon: statFooterIcon,    statFooterIconState: statFooterIconState,    statFooterPercentage: statFooterPercentage,    statFooterText: statFooterText  }});
```

To:

```
statCardsRef  // the push function will send to our firebase the new object  .push()  // and will set in a new row of the table stat-cards  // with the bellow object  .set({    statName: statName,    statDescription: statDescription,    statIcon: statIcon,    statIconColor: statIconColor,    statFooterIcon: statFooterIcon,    statFooterIconState: statFooterIconState,    statFooterPercentage: statFooterPercentage,    statFooterText: statFooterText  })  // when the push has terminated, we will dispatch to our  // reducer that we have successfully added a new row  .then(() => {    dispatch({      type: "addStatCard"    });  });
```

So, it now should look like:

```
import firebase from "firebaseConfig";
```

```
const databaseRef = firebase.database().ref();const statCardsRef = databaseRef.child("stat-cards");
```

```
const addStatCardAction = (  statName,  statDescription,  statIcon,  statIconColor,  statFooterIcon,  statFooterIconState,  statFooterPercentage,  statFooterText) => async dispatch => {  statCardsRef    .push()    .set({      statName: statName,      statDescription: statDescription,      statIcon: statIcon,      statIconColor: statIconColor,      statFooterIcon: statFooterIcon,      statFooterIconState: statFooterIconState,      statFooterPercentage: statFooterPercentage,      statFooterText: statFooterText    })    .then(() => {      dispatch({        type: "addStatCard"      });    });};
```

```
export default addStatCardAction;
```

And we are all set. Run again the app, login into your account, navigate on the **Dashboard** page, and then press the **Add stat card** button. Stats should now start adding to your **Header**.

![Image](https://cdn-media-1.freecodecamp.org/images/ghyjERjE8Jp6HG2yCIUM5aP7ddP8HTX6HfUT)
_**App is done**_

### Thanks for reading!

If you’ve enjoyed reading this tutorial give it a clap. I am very keen on hearing your thoughts about it. Just give this thread a comment and I’ll be more than happy to reply.

Useful links:

* Get the code for this tutorial from [Github](https://github.com/EINazare/react-redux-firebase-rds-tutorial)
* Read more about ReactJS on [their official website](https://reactjs.org/)
* Read more about [Redux here](https://redux.js.org/)
* Read more about [React-Redux](https://react-redux.js.org/)
* Read more about [Firebase](https://firebase.google.com/docs/)
* Check out our platform to see [what we are doing](https://www.creative-tim.com/) and [who we are](https://www.creative-tim.com/presentation)
* Read more about [Reactstrap](https://reactstrap.github.io/), the core of Argon Dashboard React
* Read my [Webpack tutorial](https://medium.freecodecamp.org/how-to-use-reactjs-with-webpack-4-babel-7-and-material-design-ff754586f618) and/or my [Redux tutorial](https://medium.freecodecamp.org/how-to-use-redux-in-reactjs-with-real-life-examples-687ab4441b85)

Find me on:

* Facebook: [https://www.facebook.com/NazareEmanuel](https://www.facebook.com/NazareEmanuel)
* Instagram: [https://www.instagram.com/manu.nazare/](https://www.instagram.com/manu.nazare/)
* Linkedin: [https://www.linkedin.com/in/nazare-emanuel-ioan-4298b5149/](https://www.linkedin.com/in/nazare-emanuel-ioan-4298b5149/)
* Email: [manu@creative-tim.com](mailto:manu@creative-tim.com)

