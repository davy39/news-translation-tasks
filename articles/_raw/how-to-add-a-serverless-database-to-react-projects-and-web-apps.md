---
title: How to Add a Serverless Database to your React Projects
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-02-01T17:16:23.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-a-serverless-database-to-react-projects-and-web-apps
coverImage: https://cdn-media-2.freecodecamp.org/w1280/601084310a2838549dcb80e0.jpg
tags:
- name: React
  slug: react
- name: serverless
  slug: serverless
seo_title: null
seo_desc: 'By Michael Bagley

  React is still one of the most popular front end Javascript libraries around. According
  to the annual Stack Overflow Developer Survey, React is the most popular front end
  library for building interfaces and the second most popular w...'
---

By Michael Bagley

React is still one of the most popular front end Javascript libraries around. According to the annual Stack Overflow Developer Survey, [React is the most popular front end library for building interfaces and the second most popular web framework overall](https://insights.stackoverflow.com/survey/2020#technology-web-frameworks). 

Even more impressive is that its popularity _continues_ to grow year-over-year.

How come React continues to be so popular (and wanted) amongst developers when [so many competitors](https://www.slant.co/topics/3790/~best-react-js-alternatives) have tried to dethrone it over the past few years? 

The full answer to that question can get very technical, so I'll do my best to make it short and sweet. 

First, React's virtual DOM is fast and efficient. Second, the declarative JSX syntax is easy to learn and features programming patterns that developers find familiar.

These benefits make React ideal for a variety of application types. Furthermore, individuals and small teams continue to choose React for their web apps. 

A common requirement for modern web applications is a _backend database_ to serve and query real-time data. The traditional implementation of a backend database can often be quite precarious and cost-ineffective. 

Thankfully, over the past five years, serverless technology has come to the forefront of modern application development. 

In this context, _serverless_ means that the developer doesn't have to set up and administer an actual server to host their database and other backend services. Rather, they use a secure provider to host their backend and connect to it directly from the front end application code. No need to worry about scalability and systems. 

This application architecture is relatively new, but it's cost-effective and _dramatically_ increases productivity. These benefits play well to those using React to build modern, production applications. Plus, services like Easybase have created serverless libraries built specifically for stateful React components.

This article will demonstrate how easy it is to use the `[easybase-react](https://github.com/easybase/easybase-react)` library to implement a stateful, serverless database in a new React project. The below example will be a straightforward note-taking app, but serverless architecture has the potential to streamline all sorts of applications.

## Table of Contents:

* How to Initialize React Project & Components
* How to Set Up the Serverless Database
* Mutable Database array

## **How to Initialize React Project & Components**

To create a new React project, I'm going to use the popular `[create-react-app](https://github.com/facebook/create-react-app)` library ([make sure you have Node installed on your machine](https://www.npmjs.com/get-npm)). 

To those not familiar with manually setting up a React project, I suggest using this library as it will create a blank, properly-configured project. 

Execute the following command where you want your new project to be created:

```zsh
npx create-react-app serverless-database-app
```

After that completes, let's install the serverless library:

```zsh
cd serverless-database-app && npm install easybase-react
```

Finally, we can start the project:

```zsh
npm run start
```

Your application will automatically open in your default browser. The root component that you see is in `src/App.js` and this is where the main changes will be made. 

Before we get into the serverless provider, I'm going to simplify the code in `App.js`. We'll have two components: _App_ and _Cards_. `App.js` will now look like the following:

```jsx
import './App.css';

function App() {
  return (
    <div className="App" style={{ display: "flex", justifyContent: "center" }}>
      <Notes />
    </div>
  );
}

function Notes() {
  const backendData = [
    { title: "Grocery List", description: "Milk, Soup, Bread", createdat: "01-18-2021" },
    { title: "Math Homework", description: "Remember to finish question 8-10 before monday", createdat: "12-01-2020" },
    { title: "Call James", description: "Ask him about the company party.", createdat: "12-30-2020" }
  ]

  const noteRootStyle = {
    border: "2px #0af solid",
    borderRadius: 9,
    margin: 20,
    backgroundColor: "#efefef",
    padding: 6
  };

  return (
    <div style={{ width: 400 }}>
      {backendData.map(ele => 
        <div style={noteRootStyle}>
          <h3>{ele.title}</h3>
          <p>{ele.description}</p>
          <small>{ele.createdat}</small>
        </div>
      )}
    </div>
  )
}

export default App;

```

I added some **example data** called _backendData_, but we'll replace this with a real-time database in the next step. Here's a screenshot of my current implementation for reference:

![serverless React example before database](https://www.freecodecamp.org/news/content/images/2021/01/Screen-Shot-2021-01-26-at-6.19.02-PM.png)

For the sake of brevity, the styling of this application will be very rudimentary. But you should definitely give your own application a unique look and feel!

## **How to Set Up the Serverless Database**

There are many general serverless backend providers around ([AWS](https://aws.amazon.com/serverless/), [Google Cloud](https://cloud.google.com/), and so on). Variance exists between the _functionality_ of these providers. Some are better suited for, perhaps, mobile applications or parallel processing or machine learning, and so on. 

I'm going to use Easybase because their platform features a **React-specific library** that is [built for serverless applications](https://easybase.io/about/2021/01/30/What-Is-a-Serverless-Application/). We'll see below how quick and easy this package is set up in code. 

I've used this platform for multiple projects and by far the most valuable aspects of `easybase-react` are the _automatic session caching_ and _secure data fetching_. Implementing these modules manually is a major hassle and can be a whole project within itself.

To start, we are going to make two changes to `App.js`. First, let's use that `easybase-react` package that we installed earlier by adding an import line to the top of `App.js`. Bring in _EasybaseProvider_ and _useEasybase_. 

Second, Wrap the _Notes_ component in the _EasybaseProvider_ component. 

`App.js` should now look as follows. Note that I also brought in the _useEffect_ hook from React.

```jsx
import './App.css';
import { EasybaseProvider, useEasybase } from 'easybase-react';
import { useEffect } from 'react';

function App() {
  return (
    <div className="App" style={{ display: "flex", justifyContent: "center" }}>
      <EasybaseProvider>
        <Notes />
      </EasybaseProvider>
    </div>
  );
}

// ...
```

The _EasybaseProvider_ component will give all children components valid access to the _useEasybase_ hook, once we pass in the required configuration. 

_EasybaseProvider_ has a prop called `ebconfig` which is a single file that authenticates and secures all connections from within our React project.

Here's how we can get an `ebconfig` token associated with a custom data table:

* [Login to Easybase](https://easybase.io/) or [create a free account](https://app.easybase.io/?view=signup)
* Open the **Create Table** dialog via the '+' button in the bottom-left button group
* Give your table a name and make columns that correspond to those of the example array _(title, description, createdat)_

![Easybase React create table](https://www.freecodecamp.org/news/content/images/2021/01/Screen-Shot-2021-01-27-at-10.54.21-AM.png)

I'm going to manually add the example rows from the _backendData_ array for reference, <ins>but this step is not necessary.</ins>

![Easybase React adding row to Notes App](https://www.freecodecamp.org/news/content/images/2021/01/Screen-Shot-2021-01-27-at-11.02.27-AM.png)

* Navigate to **Integrate** tab and create a new **React** integration

![Easybase React add integration](https://www.freecodecamp.org/news/content/images/2021/01/Screen-Shot-2021-01-27-at-1.32.45-PM.png)

* In the right-hand drawer, **enable** _Active, Testing Mode,_ and read and write in _Permissions_. Then download the _React_ token and click **Save** in the top-right

![Easybase React integration edit 1](https://www.freecodecamp.org/news/content/images/2021/01/Screen-Shot-2021-01-27-at-6.37.13-PM.png)

![Easybase React integration edit 2](https://www.freecodecamp.org/news/content/images/2021/01/Screen-Shot-2021-01-27-at-6.37.16-PM.png)

* Place the newly downloaded _ebconfig.js_ file within the `src/` folder of your project

```
├── README.md
├── node_modules/
├── package.json
├── public/
└── src/
    ├── ebconfig.js   <---
    ├── App.css
    ├── App.js
    ├── index.css
    ├── index.js
    └── ...
```

* Finally, **import** this file into `App.js` and pass it as the `ebconfig` prop of _EasybaseProvider_ like so:

```jsx
import './App.css';
import { EasybaseProvider, useEasybase } from 'easybase-react';
import { useEffect } from 'react';
import ebconfig from './ebconfig';

function App() {
  return (
    <div className="App" style={{ display: "flex", justifyContent: "center" }}>
      <EasybaseProvider ebconfig={ebconfig}>
        <Notes />
      </EasybaseProvider>
    </div>
  );
}

// ...
```

Just like that, our project is configured for serverless functionality. All that's left to do is utilize the functions provided by the `useEasybase` hook, which we'll do in the next section. 

[Take a look at this walkthrough for more information on using React or React Native with serverless architecture](https://easybase.io/react/).

If your project is to handle individual users with secure login authentication, use the **Projects** tab rather than a simple **React** integration. 

[Information about React user authentication can be found at this freeCodeCamp article about the Easybase **Project** workflow](https://www.freecodecamp.org/news/build-react-native-app-user-authentication/).

## **Mutable Database Array**

Now that we have properly set up our backend, the child components of _EasybaseProvider_ can access the _useEasybase_ hook. This hook provides the essential functions needed to access our remote data. 

Let's start by bringing in three functions; _configureFrame_, _sync_, and _Frame_, in our _Notes_ component with `const { Frame, sync, configureFrame } = useEasybase();`. 

When our component first mounts we want to configure our _Frame_ to get the first 10 entries of our database, **NOTES APP**. _Frame_ acts as a **stateful database array** in which calling _sync_ will normalize any local changes with changes in the backend database.

```jsx
function Notes() {
  const { Frame, sync, configureFrame } = useEasybase();

  useEffect(() => {
    configureFrame({ tableName: "NOTES APP", limit: 10 });
    sync();
  }, []);

  const noteRootStyle = {
    border: "2px #0af solid",
    borderRadius: 9,
    margin: 20,
    backgroundColor: "#efefef",
    padding: 6
  };

  return (
    <div style={{ width: 400 }}>
      {Frame().map(ele => 
        <div style={noteRootStyle}>
          <h3>{ele.title}</h3>
          <p>{ele.description}</p>
          <small>{String(ele.createdat).slice(0, 10)}</small>
        </div>
      )}
    </div>
  )
}
```

_Sync_ will automatically handle the backend processes necessary. More importantly, it will re-render our component with the fresh data in _Frame_.

If we rebuild our application, the new notes displayed will be the same ones present in our data table. _Congrats, you're using a serverless database!_ 

Let's have some more fun by adding a button that will push a new note to Easybase and render your application accordingly.

Create a new component called _NewNoteButton_. Get the _sync_ and _Frame_ functions from the _useEasybase_ hook. 

I'm going to place this button in the top-left of the window using absolute positioning. When a user clicks this button, my component will get a new title and description from the user and post it to Easybase using _Frame_ and _sync_. 

Put this newly created component below the _Notes_ component within the _EasybaseProvider_.

```jsx

function App() {
  return (
    <div className="App" style={{ display: "flex", justifyContent: "center" }}>
      <EasybaseProvider ebconfig={ebconfig}>
        <Notes />
        <NewNoteButton />
      </EasybaseProvider>
    </div>
  );
}

// ...

function NewNoteButton() {
  const { Frame, sync } = useEasybase();

  const buttonStyle = {
    position: "absolute",
    left: 10,
    top: 10,
    fontSize: 21
  }

  const handleClick = () => {
    const newTitle = prompt("Please enter a title for your note");
    const newDescription = prompt("Please enter your description");
    
    Frame().push({
      title: newTitle,
      description: newDescription,
      createdat: new Date().toISOString()
    })
    
    sync();
  }

  return <button style={buttonStyle} onClick={handleClick}>📓 Add Note 📓</button>
}
```

My implementation gathers the user's desired title and description via the [native prompt function](https://www.w3schools.com/jsref/met_win_prompt.asp), but your production app will likely require a more robust input solution. This will work just fine for a demonstration, though.

![serverless React project add note](https://www.freecodecamp.org/news/content/images/2021/01/Screen-Shot-2021-01-27-at-8.20.09-PM.png)

Notice the new button in the top right corner of the screen. Clicking this will bring up two text boxes. After completion, the _Notes_ component re-renders after the _sync_ call which displays your new entry.

![serverless React project with added note](https://www.freecodecamp.org/news/content/images/2021/01/Screen-Shot-2021-01-27-at-8.22.01-PM.png)

These changes will be instantly visible in your Easybase table, so feel free to make changes there as well!

## Conclusion

[The numbers don't lie](https://github.com/facebook/react/graphs/contributors) – React is robust, mature, and loved by developers. The open-source community has really embraced the project, [with over 1500 contributors](https://github.com/facebook/react/graphs/contributors). 

This library has proven to be one of the best ways to create beautiful, high-performance interfaces. In fact, you can even [deploy your React project right to Github Pages](https://github.com/gitname/react-gh-pages).

Using React with serverless has become a no-brainer. The adoption of this scalable technology has grown greatly. Take a look at the Google Trends chart for the term "serverless" over the past 8 years.

![Google Trends for 'serverless'](https://www.freecodecamp.org/news/content/images/2021/01/Screen-Shot-2021-01-28-at-2.32.12-PM.png)
_Google Trends for 'serverless'_

This technology has empowered developers to deploy scalable, enterprise-level applications at a fraction of the cost and without the conventional overhead. By unlocking the tools traditionally available to those with abundant resources, _serverless technology_ continues to encourage developers to turn their ideas into a reality.

