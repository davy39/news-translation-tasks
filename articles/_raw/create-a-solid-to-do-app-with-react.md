---
title: How to Build a Solid To-Do App with React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-03-02T16:37:00.000Z'
originalURL: https://freecodecamp.org/news/create-a-solid-to-do-app-with-react
coverImage: https://cdn-media-2.freecodecamp.org/w1280/603a6472a675540a229246bc.jpg
tags:
- name: create-react-app
  slug: create-react-app
- name: React
  slug: react
- name: Web Applications
  slug: web-applications
seo_title: null
seo_desc: "By Virginia Balseiro\nIn this tutorial you will learn how to create a basic\
  \ Solid to-do app. But what is Solid – not to be confused with SOLID? Well, it's\
  \ a set of conventions and tools used to build decentralized apps.  \nSo what do\
  \ I mean by decentra..."
---

By Virginia Balseiro

In this tutorial you will learn how to create a basic [Solid](https://solidproject.org/about) to-do app. But what is Solid – not to be confused with [SOLID](https://www.freecodecamp.org/news/solid-principles-explained-in-plain-english/)? Well, it's a set of conventions and tools used to build decentralized apps.  
  
So what do I mean by decentralized? Currently, all our data is centralized in a few web platforms: Facebook, Google, and others. This has various consequences for privacy that we're all aware of, but it also endangers the principle of universality of the web: the web must be accessible to everyone.   
  
Let me illustrate this with an example: if my German teacher decides to create a Facebook group to share class materials, I need to have a Facebook account to access it. Likewise, if the teacher decides to quit Facebook, she needs to move the students to another app along with the data.   
  
With Solid, the data and the app are decoupled. The data lives in one place and the app reads and write to that place. The user controls where that data is, and with which people or apps they want to share it with. Users can decide which apps to use based on which ones suit their needs better, and they have full control of their data. 

This has many advantages for developers as well, because competition is then based on the quality of an app, as opposed to how much user data you control.

And for frontend developers there's the added bonus of not having to worry about setting up a database if you want to save user data.

This tutorial will help you become familiar with some of the tools available to write Solid applications. We will use the following libraries:

* [solid-client](https://docs.inrupt.com/developer-tools/javascript/client-libraries/tutorial/read-write-data/): Library to read and write data in Solid Pods
* [solid-ui-react](https://docs.inrupt.com/developer-tools/javascript/react-sdk/): Library of UI components that make it easier to interact with the data.

## Prerequisites

This tutorial assumes a basic knowledge of React.

You will also need to [have your own Pod](https://solidproject.org/users/get-a-pod). You can create it beforehand, or as part of the login process when we add authentication to the to-do app, by registering instead of logging in.

Here's a link to the repository where you can find the code: [https://github.com/VirginiaBalseiro/solid-todo-tutorial](https://github.com/VirginiaBalseiro/solid-todo-tutorial)

And here's a link to CodeSandbox: [https://codesandbox.io/s/solid-todo-tutorial-7uz4j](https://codesandbox.io/s/solid-todo-tutorial-7uz4j). If you want to test the app on CodeSandbox, just make sure to open it on a separate tab.

# Getting started

We will start by creating a React app using [create-react-app.](https://create-react-app.dev/) This will create a new directory with your app's name within the directory you run it from. So navigate to the directory where you keep you projects and run:

```jsx
npx create-react-app solid-todo-tutorial

```

This creates a new directory named `solid-todo-tutorial`. Go to that directory and install the two Solid libraries I mentioned before:

```jsx
cd solid-todo-tutorial
npm install @inrupt/solid-client @inrupt/solid-ui-react

```

Now we're ready to start coding.

# How to Authenticate a User

I left the class names in these snippets in case you would like to use the stylesheets available in the repository.

### How to Use the LoginButton Component to Log Users In

The first thing we need to do in order to be able to write to our Pod is to authenticate as a user with write permissions (so that we have the permissions to do so). Luckily this is very straightforward using the [login button](https://solid-ui-react.docs.inrupt.com/?path=/story/authentication-login-button--with-children) from `solid-ui-react`.

We need to import `LoginButton` from `solid-ui-react`. This component accepts two required props: `oidcIssuer`, the Pod provider, and a `redirectUrl` which is the URL we want to be redirected to after we login.

We will get the Pod provider as a string from the user through a text input box, and we will also provide some Pod provider options.

The `LoginButton` also takes an optional `authOptions` prop, which is an object with the `clientName` property. This is useful because we want to display our app's name to the user when they authenticate. 

If we don't pass the `clientName`, a random string will be generated which is confusing for the user when they're granting our app permission to do things.

In `App.js` let's get rid of all the boilerplate that comes with our React app and use the `LoginButton`:

```jsx
// App.js

import React from "react";
import { LoginButton } from "@inrupt/solid-ui-react";

const authOptions = {
    clientName: "Solid Todo App",
  };

function App() {
const [oidcIssuer, setOidcIssuer] = useState("");

  const handleChange = (event) => {
    setOidcIssuer(event.target.value);
  };

  return (
    <div className="app-container">
	 <span>
            Log in with:
            <input
              className="oidc-issuer-input "
              type="text"
              name="oidcIssuer"
              list="providers"
              value={oidcIssuer}
              onChange={handleChange}
            />
          <datalist id="providers">
            <option value="https://broker.pod.inrupt.com/" />
            <option value="https://inrupt.net/" />
          </datalist>
          </span>
		  <LoginButton
		     oidcIssuer={oidcIssuer}
		     redirectUrl={window.location.href}
		     authOptions={authOptions}
		   />
    </div>
  );
}

export default App;

```

In the `index.js` file, let's wrap our App component with the `SessionProvider` component. Now, we can use the `useSession` hook throughout the entire app, which returns session info that allows us to make authenticated requests.

Replace the boilerplate in `index.js` with the following:

```jsx
// index.js

import ReactDOM from "react-dom";
import App from "./App";
import { SessionProvider } from "@inrupt/solid-ui-react";

ReactDOM.render(
  <SessionProvider>
    <App />
  </SessionProvider>,
  document.getElementById("root")
);

```

Once that is done, you can test it! Run your app with `npm start` and click on the Login button. It should take you to a page where you can either log in or register. If you don't have an account, you can click on "Sign up" to create one. 

Once you log in, you will be redirected to the main page. As you can see, our main page only has the login button. We are logged in, but we don't do anything with that information. Let's change that!

### How to Use Profile Data

We're going to change our code so our app shows the login button if we're logged out, and our name if we're logged in.

For this we're going to use `CombinedDatasetProvider` and `Text` from `solid-ui-react`. `CombinedDatasetProvider` needs two props: `datasetUrl` and `thingUrl` which, in this case, can both be set to the user's WebID.

A **WebID** is an HTTP URI which refers to an agent (for example, a person), that, when looked up, resolves to a profile document.

`CombinedDatasetProvider` fetches the dataset and Thing for us so we can pass it straight on to the children.

The child in our app will be the `Text` component

The `Text` component takes a prop, either `property` or `properties`, that specifies the value to retrieve and display from the fetched dataset/thing. 

In our case, we want the Text component to retrieve and display the name of the user from the user's profile. `property` or `properties` is the URL or URLs we have chosen for the **predicate** for which we want to fetch the data.

In our case we want to get the name of the user.

A user's profile data is stored as [Resource Description Framework (RDF)](https://www.w3.org/RDF/) data. RDF is a standard model for data interchange on the Web. RDF data is stored in **triples**, which are composed of a **subject**, a **predicate** and an **object**. 

So, for instance, if I want to write a social networking app and I want to store Bob's acquaintances, I could add one like so: `<http://example.org/bob#me> <http://xmlns.com/foaf/0.1/knows> <http://example.org/alice#me> .`

In this case, `<http://example.org/bob#me>` is the subject, `<http://xmlns.com/foaf/0.1/knows>`  is the predicate, and `<http://example.org/alice#me>` is the object.

To specify that we want to retrieve the name, we use a name identifier. In our example, we use a name identifier from an existing Vocabulary.

Vocabularies are collections of identifiers (URIs) with a clearly-defined meaning. An example of a popular vocabulary is **[FOAF (Friend Of A Friend)](http://xmlns.com/foaf/spec/)**, which defines URIs to describe people and their relationships. 

You can find more information about vocabularies in [the Solid Project website](https://solidproject.org/developers/vocabularies).

The name of the logged in user, in most cases, will be stored in the profile document under "[http://www.w3.org/2006/vcard/ns#fn](http://www.w3.org/2006/vcard/ns#fn)" or "[http://xmlns.com/foaf/0.1/name](http://xmlns.com/foaf/0.1/name)". `fn` stands for formatted name. In RDF, that looks like this:

```jsx
:me <http://www.w3.org/2006/vcard/ns#fn> "Virginia Balseiro" .

```

or

```jsx
:me <[<http://xmlns.com/foaf/0.1/name>](<http://xmlns.com/foaf/0.1/name>)> "Virginia Balseiro" 

```

But in our case we want it to check under [`http://www.w3.org/2006/vcard/ns#fn`](http://www.w3.org/2006/vcard/ns#fn) and if it cannot find anything, check under [`http://xmlns.com/foaf/0.1/name`](http://xmlns.com/foaf/0.1/name). We can use `properties`, which is an array of properties to attempt to read from, in our `Text` component.

```jsx
// App.js

import React from "react";
import {
  LoginButton,
  Text,
  useSession,
  CombinedDataProvider,
} from "@inrupt/solid-ui-react";

const authOptions = {
    clientName: "Solid Todo App",
  };

function App() {
  const { session } = useSession();
  const [oidcIssuer, setOidcIssuer] = useState("");

  const handleChange = (event) => {
    setOidcIssuer(event.target.value);
  };
  return (
    <div className="app-container">
      {session.info.isLoggedIn ? (
        <CombinedDataProvider
          datasetUrl={session.info.webId}
          thingUrl={session.info.webId}
        >
          <div className="message logged-in">
            <span>You are logged in as: </span>
            <Text properties={[
                "http://www.w3.org/2006/vcard/ns#fn",
                "http://xmlns.com/foaf/0.1/name",
              ]} />
          </div>
        </CombinedDataProvider>
      ) : (
        <div className="message">
          <span>You are not logged in. </span>
          <span>
            Log in with:
            <input
              className="oidc-issuer-input "
              type="text"
              name="oidcIssuer"
              list="providers"
              value={oidcIssuer}
              onChange={handleChange}
            />
           <datalist id="providers">
             <option value="https://broker.pod.inrupt.com/" />
             <option value="https://inrupt.net/" />
           </datalist>
          </span>
          <LoginButton
            oidcIssuer={oidcIssuer}
            redirectUrl={window.location.href}
            authOptions={authOptions}
          />
        </div>
      )}
    </div>
  );
}

export default App;

```

We can now log in and display info from our Pod in our app.

### How to Log Users Out

Let's now add a [logout button](https://solid-ui-react.vercel.app/?path=/story/authentication-logout-button--with-children) so we can log out whenever we want to. This is easy: we just need to import the `LogoutButton` from `solid-ui-react` and display it underneath the Text with the user name:

```jsx
// App.js

import {
  LoginButton,
  LogoutButton,
  Text,
  useSession,
  CombinedDataProvider,
} from "@inrupt/solid-ui-react";

function App() {
  const { session } = useSession();

	// ...
	
	<div className="message logged-in">
	  <span>You are logged in as: </span>
	  <Text properties={[
	     "http://xmlns.com/foaf/0.1/name",
	     "http://www.w3.org/2006/vcard/ns#fn",
	   ]} />    
	   <LogoutButton />
	 </div>

	// ...

}

```

# How to Create a To-Do

### How to Add an "Add Todo" button

To create a to-do item we are going to need a button that triggers a function which adds a to-do item to our to-do list. Let's put all of the logic and UI to add a to-do into a separate component in `src/components/AddTodo/index.js`:

```jsx
// components/AddTodo/index.js

import React from "react";

function AddTodo() {
  return <button className="add-button">Add Todo</button>;
}

export default AddTodo;

```

In our App, we are going to display this `AddTodo` button to logged-in users only:

```jsx
// App.js

import AddTodo from "../src/components/AddTodo";

function App() {
// ...
      {session.info.isLoggedIn ? (
        <CombinedDataProvider
          datasetUrl={session.info.webId}
          thingUrl={session.info.webId}
        >
          <div className="message logged-in">
            <span>You are logged in as: </span>
            <Text
              properties={[
                "http://xmlns.com/foaf/0.1/name",
                "http://www.w3.org/2006/vcard/ns#fn",
              ]} />
            <LogoutButton />
          </div>
          <section>
            <AddTodo />
          </section>
        </CombinedDataProvider>
      ) : 
// ...
}

```

For now this button doesn't do anything. Let's change that.

### How to Initialize the To-Dos Dataset

In formal terms, each of our to-do items will be structured as **things** that are grouped inside a **dataset.** So first we need to check if the dataset already exists, and if not, we must create it. 

Let's write a function that does this, assuming our structured data will be stored in a folder called "todos" in the root of our pod.

The proper way to do this would be to check the profile (that is, the data at the user's WebID), look for a URL for a known predicate (for example `myVocab:todolistContainer`), and then follow that link to get to this folder. 

Only if no such link exists would the app initialize its own folder - and after initialization, it would link back to that from the user's WebID. 

For that we would need to create a new vocab, and for simplicity's sake that is not included in this tutorial.

Let's put this function in `src/utils/index.js` because we might use it again in the future somewhere aside from our `AddTodo` component.

```jsx
// utils/index.js

import {
  createSolidDataset,
  getSolidDataset,
  saveSolidDatasetAt,
} from "@inrupt/solid-client";

export async function getOrCreateTodoList(containerUri, fetch) {
  const indexUrl = `${containerUri}index.ttl`;
  try {
    const todoList = await getSolidDataset(indexUrl, { fetch });
    return todoList;
  } catch (error) {
    if (error.statusCode === 404) {
      const todoList = await saveSolidDatasetAt(
        indexUrl,
        createSolidDataset(),
        {
          fetch,
        }
      );
      return todoList;
    }
  }
}

```

We are using three functions from `solid-client` here to read and write data in our Pods:

* `getSolidDataset`: takes the URI of the dataset we want to get, plus an `options` object where we pass the `fetch` function. This is a function we get from the session, and it's used to make authenticated requests.
* `createSolidDataset`: initializes a new dataset in memory.
* `saveSolidDatasetAt`: takes a URI as first param (which is where our dataset will be saved), the dataset in question as second param (in this case a new, empty dataset), and the fetch function.

If the to-do list `index` file is found, our getOrCreateTodoList function will return it. If not (if there is a 404 error), it will create the file at the location given.

Now we can use this function in our `AddTodo` component. We need to pass it a container URI, which we make by concatenating the Pod URI with the folder name we have chosen to store our to-do list. So first we need to:

* Fetch the profile dataset using the WebID for the current session (the current user's WebID).
* Extract the profile `Thing` from the profile dataset with the same URL (the user's WebID).
* Get the URLs for the user's Pods. For this we use `getUrlAll`, which returns an array with all the URLs stored under the predicate `http://www.w3.org/ns/pim/space#storage`. We will assume that the first item in the array is the Pod we want to use.

Once we have the container URL, we can now check if the to-do list dataset exists. If it doesn't we can create it, and use it anywhere in the component:

```jsx
// components/AddTodo/index.js

import { getSolidDataset, getThing, getUrlAll } from "@inrupt/solid-client";
import { useSession } from "@inrupt/solid-ui-react";
import React, { useEffect, useState } from "react";
import { getOrCreateTodoList } from "../../utils";

function AddTodo() {
  const { session } = useSession();
  const [todoList, setTodoList] = useState();

  useEffect(() => {
    if (!session) return;
    (async () => {
      const profileDataset = await getSolidDataset(session.info.webId, {
        fetch: session.fetch,
      });
      const profileThing = getThing(profileDataset, session.info.webId);
      const podsUrls = getUrlAll(
        profileThing,
        "http://www.w3.org/ns/pim/space#storage"
      );
      const pod = podsUrls[0];
      const containerUri = `${pod}todos/`;
      const list = await getOrCreateTodoList(containerUri, session.fetch);
      setTodoList(list);
    })();
  }, [session]);

  return <button className="add-button">Add Todo</button>;
}

export default AddTodo;

```

To check if it worked, go to [PodBrowser](https://podbrowser.inrupt.com/login), log in by selecting your Pod Provider from the dropdown, enter your username and password, and check that the "todos" folder was created in your Pod.

![Files view in PodBrowser showing the newly created "todos" folder](https://www.freecodecamp.org/news/content/images/2021/02/image-171.png)

If you go into the "todos" container, there should be an `index.ttl` file in it.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/image-173.png)
_Files view in PodBrowser showing the newly created "index.tll" file_

If you click on the `index.ttl` a drawer will open up to the right with a "Download" link. Click on it to download the file, which you can open with any text editor, such as Notepad. The contents of the file should look like this:

```jsx
@prefix as:    <https://www.w3.org/ns/activitystreams#> .
@prefix rdf:   <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix xsd:   <http://www.w3.org/2001/XMLSchema#> .
@prefix ldp:   <http://www.w3.org/ns/ldp#> .
@prefix skos:  <http://www.w3.org/2004/02/skos/core#> .
@prefix rdfs:  <http://www.w3.org/2000/01/rdf-schema#> .
@prefix acl:   <http://www.w3.org/ns/auth/acl#> .
@prefix vcard: <http://www.w3.org/2006/vcard/ns#> .
@prefix foaf:  <http://xmlns.com/foaf/0.1/> .
@prefix dc:    <http://purl.org/dc/terms/> .
@prefix acp:   <http://www.w3.org/ns/solid/acp#> .

<https://pod.inrupt.com/virginiabalseiro/todos/index.ttl>
        rdf:type  ldp:RDFSource .

```

This is the file where we are going to be adding our to-dos.

If at any point you mess up your to-do list by testing out the app as you code along, you can delete this file and then the folder that contains it ("todos") on PodBrowser by clicking on the "Delete" button in the details drawer. 

Then next time you refresh your app, the folder and file will be created again so you can start over.

# How to Add an Item to the Dataset

Ok, now we can finally add a to-do! Adding a to-do is essentially adding an item, or `[Thing](https://docs.inrupt.com/developer-tools/javascript/client-libraries/reference/glossary/)`, to the to-do list dataset we just created. Our to-dos will have three properties:

* `text` - the content of the to-do. It will be stored under the predicate: [http://schema.org/text](http://schema.org/text)
* `created` - the date when this to-do was created, stored under [http://www.w3.org/2002/12/cal/ical#created](http://www.w3.org/2002/12/cal/ical#created)
* `type` - the type of the todo, which among other things will help us filter later on. This is stored under [http://www.w3.org/2002/12/cal/ical#Vtodo](http://www.w3.org/2002/12/cal/ical#Vtodo)

We are hardcoding the predicate strings here, but there are libraries that make this easier, such as [rdf-namespaces](https://www.npmjs.com/package/rdf-namespaces).

The date will help us sort them later. So we need to create a thing and add these to it. We will use:

* `addStringNoLocale` to add the text string
* `addDatetime` to add the created at date

Let's write a function that does that so we can trigger it by clicking the button.

```jsx
// components/AddTodo/index.js
import {
  addDatetime,
  addStringNoLocale,
  createThing,
  getSolidDataset,
  getSourceUrl,
  getThing,
  getUrlAll,
  saveSolidDatasetAt,
  setThing,
} from "@inrupt/solid-client";

function AddTodo() { 
const { session } = useSession();
// ...
  const addTodo = async (text) => {
    const indexUrl = getSourceUrl(todoList);
    const todoWithText = addStringNoLocale(
      createThing(),
      "http://schema.org/text",
      text
    );
    const todoWithDate = addDatetime(
      todoWithText,
      "http://www.w3.org/2002/12/cal/ical#created",
      new Date()
    );
    const todoWithType = addUrl(todoWithDate, "http://www.w3.org/1999/02/22-rdf-syntax-ns#type", "http://www.w3.org/2002/12/cal/ical#Vtodo");
    const updatedTodoList = setThing(todoList, todoWithType);
    const updatedDataset = await saveSolidDatasetAt(indexUrl, updatedTodoList, {
      fetch: session.fetch,
    });
    setTodoList(updatedDataset);
  };
// ...
}

```

We create the `Thing` first, add a string and a date, then set the thing in the dataset (`todoList`). We need to overwrite the `todoList` by saving it in its URL, which we get by using `getSourceUrl`. 

Now we need to modify our component so we can get the input text from the user. Let's put those predicates in constants to keep our code tidy and avoid bugs due to typos:

```jsx
// components/AddTodo/index.js

import {
  addDatetime,
  addStringNoLocale,
  createThing,
  getSolidDataset,
  getSourceUrl,
  getUrlAll,
  saveSolidDatasetAt,
  setThing,
  getThing,
} from "@inrupt/solid-client";
import { useSession } from "@inrupt/solid-ui-react";
import React, { useEffect, useState } from "react";
import { getOrCreateTodoList } from "../../utils";

const STORAGE_PREDICATE = "http://www.w3.org/ns/pim/space#storage";
const TEXT_PREDICATE = "http://schema.org/text";
const CREATED_PREDICATE = "http://www.w3.org/2002/12/cal/ical#created";
const TODO_CLASS = "http://www.w3.org/2002/12/cal/ical#Vtodo";
const TYPE_PREDICATE = "http://www.w3.org/1999/02/22-rdf-syntax-ns#type";

function AddTodo() {
  const { session } = useSession();
  const [todoList, setTodoList] = useState();
  const [todoText, setTodoText] = useState("");

  useEffect(() => {
    if (!session) return;
    (async () => {
      const profileDataset = await getSolidDataset(session.info.webId, {
        fetch: session.fetch,
      });
      const profileThing = getThing(profileDataset, session.info.webId);
      const podsUrls = getUrlAll(profileThing, STORAGE_PREDICATE);
      const pod = podsUrls[0];
      const containerUri = `${pod}todos/`;
      const list = await getOrCreateTodoList(containerUri, session.fetch);
      setTodoList(list);
    })();
  }, [session]);

  const addTodo = async (text) => {
    const indexUrl = getSourceUrl(todoList);
    const todoWithText = addStringNoLocale(createThing(), TEXT_PREDICATE, text);
    const todoWithDate = addDatetime(
      todoWithText,
      CREATED_PREDICATE,
      new Date()
    );
    const todoWithType = addUrl(todoWithDate, TYPE_PREDICATE, TODO_CLASS);
    const updatedTodoList = setThing(todoList, todoWithType);
    const updatedDataset = await saveSolidDatasetAt(indexUrl, updatedTodoList, {
      fetch: session.fetch,
    });
    setTodoList(updatedDataset);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    addTodo(todoText);
  };

  const handleChange = (e) => {
    e.preventDefault();
    setTodoText(e.target.value);
  };

  return (
    <>
      <form onSubmit={handleSubmit} className="todo-form">
        <label htmlFor="todo-input">
          <input
            id="todo-input"
            type="text"
            value={todoText}
            onChange={handleChange}
          />
        </label>
        <button type="submit" className="add-button">
          Add Todo
        </button>
      </form>
    </>
  );
}

export default AddTodo;

```

Now if we write some text and click `AddTodo`, our to-do will be added! But we cannot see our to-dos yet. 

So in order to check if it worked, on [PodBrowser](https://podbrowser.inrupt.com/) navigate to your "todos" folder, download the `index.ttl` file again, and see if there are changes. If everything went well, you should see something like this:

```jsx
<https://pod.inrupt.com/virginiabalseiro/todos/index.ttl#16141957896165236259077375411>
        <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2002/12/cal/ical#Vtodo> ;
        <http://www.w3.org/2002/12/cal/ical#created>  "2021-02-24T19:43:09.616Z"^^xsd:dateTime ;
        <http://schema.org/text>  "Finish the Solid Todo App tutorial" .

```

You can see that a random id has been generated for our to-do. This happens when we create a thing without passing a URL or a name string for the subject, which is fine for this case. Next we will see how we can fetch our to-dos so we can display them.

# How to Display the To-Dos

To display the to-dos we are going to use two additional components from `solid-ui-react`: the `Table` and `TableColumn` components.

The Table component has a required prop `things`, which is an array of objects containing each thing in the dataset and the dataset they belong to. It should look like this:

```jsx
[{ dataset: myDataset, thing: thing1 }, { dataset: myDataset, thing: thing2 } ];

```

In our case, we already have the dataset (our to-do list), but now we need to extract the things from it and map them to obtain an array that looks like the above.

The place where we are fetching our to-dos is in the `AddTodo` component. But we are going to create a component called `TodoList` to display our table, so we are going to need to use the list there too. 

Let's move the `useEffect` to the `App` component, so we can pass `todoList` and `setTodoList` to the components that need them. We are adding a check to see if the user is logged out, in which case we exit the `useEffect`.

```jsx
// App.js

import React, { useEffect, useState } from "react";
import {
  LoginButton,
  LogoutButton,
  Text,
  useSession,
  CombinedDataProvider,
} from "@inrupt/solid-ui-react";
import { getSolidDataset, getUrlAll, getThing } from "@inrupt/solid-client";
import AddTodo from "./components/AddTodo";
import TodoList from "./components/TodoList";
import { getOrCreateTodoList } from "./utils";

const STORAGE_PREDICATE = "http://www.w3.org/ns/pim/space#storage";

const authOptions = {
  clientName: "Solid Todo App",
};

function App() {
  const { session } = useSession();
  const [todoList, setTodoList] = useState();
  const [oidcIssuer, setOidcIssuer] = useState("");

  const handleChange = (event) => {
    setOidcIssuer(event.target.value);
  };

  useEffect(() => {
    if (!session || !session.info.isLoggedIn) return; 
    (async () => {
      const profileDataset = await getSolidDataset(session.info.webId, {
        fetch: session.fetch,
      });
      const profileThing = getThing(profileDataset, session.info.webId);
      const podsUrls = getUrlAll(profileThing, STORAGE_PREDICATE);
      const pod = podsUrls[0];
      const containerUri = `${pod}todos/`;
      const list = await getOrCreateTodoList(containerUri, session.fetch);
      setTodoList(list);
    })();
  }, [session, session.info.isLoggedIn]);

  return (
    <div className="app-container">
      {session.info.isLoggedIn ? (
        <CombinedDataProvider
          datasetUrl={session.info.webId}
          thingUrl={session.info.webId}
        >
          <div className="message logged-in">
            <span>You are logged in as: </span>
            <Text
              properties={[
                "http://xmlns.com/foaf/0.1/name",
                "http://www.w3.org/2006/vcard/ns#fn",
              ]}
            />
            <LogoutButton />
          </div>
          <section>
            <AddTodo todoList={todoList} setTodoList={setTodoList} />
            <TodoList todoList={todoList} setTodoList={setTodoList} />
          </section>
        </CombinedDataProvider>
      ) : (
        <div className="message">
          <span>You are not logged in. </span>
          <span>
            Log in with:
            <input
              className="oidc-issuer-input "
              type="text"
              name="oidcIssuer"
              list="providers"
              value={oidcIssuer}
              onChange={handleChange}
            />
           <datalist id="providers">
            <option value="https://broker.pod.inrupt.com/" />
            <option value="https://inrupt.net/" />
           </datalist>
          </span>
          <LoginButton
            oidcIssuer={oidcIssuer}
            redirectUrl={window.location.href}
            authOptions={authOptions}
          />
        </div>
      )}
    </div>
  );
}

export default App;

```

And our AddTodo component will now look like this:

```jsx
// components/AddTodo/index.jsx

import {
  addDatetime,
  addStringNoLocale,
  createThing,
  getSourceUrl,
  saveSolidDatasetAt,
  setThing,
} from "@inrupt/solid-client";
import { useSession } from "@inrupt/solid-ui-react";
import React, { useState } from "react";

const TEXT_PREDICATE = "http://schema.org/text";
const CREATED_PREDICATE = "http://www.w3.org/2002/12/cal/ical#created";
const TODO_CLASS = "http://www.w3.org/2002/12/cal/ical#Vtodo";
const TYPE_PREDICATE = "http://www.w3.org/1999/02/22-rdf-syntax-ns#type";

function AddTodo({ todoList, setTodoList }) {
  const { session } = useSession();
  const [todoText, setTodoText] = useState("");

  const addTodo = async (text) => {
    const indexUrl = getSourceUrl(todoList);
    const todoWithText = addStringNoLocale(createThing(), TEXT_PREDICATE, text);
    const todoWithDate = addDatetime(
      todoWithText,
      CREATED_PREDICATE,
      new Date()
    );
    const todoWithType = addUrl(todoWithDate, TYPE_PREDICATE, TODO_CLASS);
    const updatedTodoList = setThing(todoList, todoWithType);
    const updatedDataset = await saveSolidDatasetAt(indexUrl, updatedTodoList, {
      fetch: session.fetch,
    });
    setTodoList(updatedDataset);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    addTodo(todoText);
    setTodoText("");
  };

  const handleChange = (e) => {
    e.preventDefault();
    setTodoText(e.target.value);
  };

  return (
      <form className="todo-form" onSubmit={handleSubmit}>
        <label htmlFor="todo-input">
          <input
            id="todo-input"
            type="text"
            value={todoText}
            onChange={handleChange}
          />
        </label>
        <button className="add-button" type="submit">Add Todo</button>
      </form>
  );
}

export default AddTodo;

```

Notice that we added a line in `handleSubmit` to set the text to an empty string after we have added the to-do, so that the input box content is cleared.

For our `TodoList` component, we are going to need the `Table` and `TableColumn` components from `solid-ui-react`. We're also going to use `getThingAll` from solid-client to extract the things from our dataset so we can create the array we need for the Table. 

For now let's just display the number of things our dataset contains:

```jsx
// components/TodoList/index.jsx

import { getThingAll } from "@inrupt/solid-client";
import { Table, TableColumn } from "@inrupt/solid-ui-react";
import React, { useEffect, useState } from "react";

function TodoList({ todoList }) {
	const todoThings = todoList ? getThingAll(todoList) : [];

  return <div>Your to-do list has {todoThings.length} items</div>;
}

export default TodoList;

```

Once you add the `TodoList` component, you might need to stop and start your app again with `npm start` if you see any errors. 

To see if it works, try adding to-dos and see if the number of items changes. You will notice the length of the array indicates one item more than the number of to-dos you have created. This is because there is another item in the to-dos dataset that is not a to-do. We will fix that later.

To use the `Table` component, we need to create the array with the objects we need and pass it to the table:

```jsx
// components/TodoList/index.jsx

function TodoList({ todoList }) {
// ...
const thingsArray = todoThings.map((t) => {
    return { dataset: todoList, thing: t };
  });
// ...
}

```

But to actually display anything we need to use the `TableColumn` component inside the `Table`. The `TableColumn` component needs a required prop `property`, which is the property we want to display. This means the predicate under which the data we want to show is stored. 

In the case of our to-dos, we have two properties: the `text` and the `date` in which the to-do was created, stored under [http://schema.org/text](http://schema.org/text) and [http://www.w3.org/2002/12/cal/ical#created](http://www.w3.org/2002/12/cal/ical#created), respectively:

```jsx
// ./components/TodoList/index.jsx

const TEXT_PREDICATE = "http://schema.org/text";
const CREATED_PREDICATE = "http://www.w3.org/2002/12/cal/ical#created";

function TodoList({ todoList }) {
// ...
<div>
  Your to-do list has {todoThings.length} items
  <Table things={thingsArray}>
    <TableColumn property={TEXT_PREDICATE} />
    <TableColumn property={CREATED_PREDICATE} />
   </Table>
 </div>
// ...
}

```

You will notice two things: first, the headers. The `TableColumn` accepts an optional prop `header`, with which we can set the header of the column. If we don't pass this prop, the header will be the URL of the predicate for that property. You can also pass an empty string if you don't want headers. Let's do that for the text of our to-do, and pass "Created" for the date.

Second, there is nothing displayed for the created at column. This is because `TableColumn` also accepts an optional prop `dataType`, which defaults to 'string' if not set, but the data we have is not a string but a datetime, so we need to set it:

```jsx
// components/TodoList/index.jsx

const TEXT_PREDICATE = "http://schema.org/text";
const CREATED_PREDICATE = "http://www.w3.org/2002/12/cal/ical#created";

function TodoList({ todoList }) {
// ...
	<div className="table-container">
		<span className="tasks-message">
		  Your to-do list has {todoThings.length} items
		</span>
	  <Table className="table" things={thingsArray}>
	    <TableColumn property={TEXT_PREDICATE} header="" />
	     <TableColumn
	       property={CREATED_PREDICATE}
	       dataType="datetime"
	       header="Created At"
	      />
	   </Table>
	 </div>
// ...
}

```

Finally, it would be nice if we could format the date so it could look like this: `Sat Dec 26 2020`, instead of a such a longer string. 

The body prop allows us to pass a custom body to the column, where we can format the value we get for each cell. This prop is super useful when we want to pass a custom component the cell, for instance a link, instead of the value as it comes from the dataset.

Before we do this, though, we need to filter out the non-todo things we have in our dataset. If you look at the `index.ttl` file you will notice a line that looks like this:

```jsx
<https://pod.inrupt.com/virginiabalseiro/todos/index.ttl>
        rdf:type  ldp:RDFSource .

```

That is automatically added by the server to identify what type of resource we're dealing with, but it will throw an error when we try to format the date, because it won't have a `created` property. This is also why we had an extra item in our to-dos count. 

So we need to filter out all the things containing a property `type` with the value `RDFSource`.

We will also switch from `todoThing` to `thingsArray` in the message displaying the number of items, since otherwise we are counting the `type` as well.

Our `TodoList` component now looks like this:

```jsx
// ./components/TodoList/index.jsx

import React from "react";
import { getThingAll, getUrl } from "@inrupt/solid-client";
import { Table, TableColumn } from "@inrupt/solid-ui-react";

function TodoList({ todoList }) {
  const todoThings = todoList ? getThingAll(todoList) : [];

  const TEXT_PREDICATE = "http://schema.org/text";
  const CREATED_PREDICATE = "http://www.w3.org/2002/12/cal/ical#created";
  const TODO_CLASS = "http://www.w3.org/2002/12/cal/ical#Vtodo";
  const TYPE_PREDICATE = "http://www.w3.org/1999/02/22-rdf-syntax-ns#type";

  const thingsArray = todoThings.filter((t) => getUrl(t, TYPE_PREDICATE) === TODO_CLASS).map((t) => {
    return { dataset: todoList, thing: t };
  });

  if (!thingsArray.length) return null;

  return (
    <div className="table-container">
      <span className="tasks-message">
        Your to-do list has {thingsArray.length} items
      </span>
      <Table className="table" things={thingsArray}>
        <TableColumn property={TEXT_PREDICATE} header="" />
        <TableColumn
          property={CREATED_PREDICATE}
          dataType="datetime"
		      header="Created At"
          body={({ value }) => value.toDateString()}
        />
      </Table>
    </div>
  );
}

export default TodoList;

```

# How to Mark a To-Do as Done

Now that we can display our to-dos, we need a way to mark them as done. We will store this "done" state under "[http://www.w3.org/2002/12/cal/ical#completed"](http://www.w3.org/2002/12/cal/ical#completed%22%5D(http://www.w3.org/2002/12/cal/ical#completed%22), with a date time as the object. 

Let's add a new column to our table:

```jsx
// components/TodoList/index.jsx

const COMPLETED_PREDICATE = "http://www.w3.org/2002/12/cal/ical#completed";
// ...
<TableColumn
  property={COMPLETED_PREDICATE}
  dataType="datetime"
  header="Done"
  body={({ value }) => (
     <label>
       <input type="checkbox" />
      </label>
     )}
 />
// ...

```

For now this check box doesn't do anything. We need to add this property with a datetime value to our to-do thing when we click the checkbox. For that, we are going to need the URL for our to-do, so we can find it and add properties to it.

For this we are going to use the `useThing` hook from `solid-ui-react`.

We need to write a function that handles the adding of a `completed` property to our to-do thing. This function will take the to-do thing as an argument, add a `completed` property with a `datetime` value to it, set it in the dataset, and save the updated dataset.

```jsx
// components/TodoList/index.jsx
import {
  addDatetime,
  getSourceUrl,
  saveSolidDatasetAt,
  setThing,
} from "@inrupt/solid-client";
import {
  Table,
  TableColumn,
  useSession,
} from "@inrupt/solid-ui-react";

function TodoList({ todoList, setTodoList }) {
  const { fetch } = useSession();
  // ...
  const handleCheck = async (todo) => {
	    const todosUrl = getSourceUrl(todoList);
	    const date = new Date();
	    const doneTodo = addDatetime(
	      todo,
	      "http://www.w3.org/2002/12/cal/ical#completed",
	      date
	    );
	    const updatedTodos = setThing(todoList, doneTodo, { fetch });
	    await saveSolidDatasetAt(todosUrl, updatedTodos, {
	      fetch,
	    });
	  };
  // ...
}

```

To access the to-do thing, we first need to create a custom body component for our `TableColumn`. It needs to be a proper component so that we can use the `useThing` hook, so let's put it outside the `TodoList` component but in the same file. We will also pass it a `checked` prop that we will use to set the `checked` property in the checkbox, and our `handleCheck` function.

```jsx
// components/TodoList/index.jsx
import {
  Table,
  TableColumn,
  useThing,
  useSession,
} from "@inrupt/solid-ui-react";

function CompletedBody({ checked, handleCheck }) {
    const { thing } = useThing();
    return (
      <label>
        <input
          type="checkbox"
          checked={checked}
          onChange={() => handleCheck(thing)}
        />
      </label>
    );
  }

```

Now we can use this component in the `body` of our column:

```jsx
// components/TodoList/index.jsx

<TableColumn
  property={COMPLETED_PREDICATE}
  dataType="datetime"
  header="Done"
  body={({ value }) => <CompletedBody checked={Boolean(value)} handleCheck={handleCheck} />}
 />

```

Now if you click on the checkbox, a property is added to the to-do. If you check the `index.ttl` file, you will see something like this:

```jsx
<https://pod.inrupt.com/virginiabalseiro/todos/index.ttl#16089989748796144560745441174>
        <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2002/12/cal/ical#Vtodo> ;        
        <http://www.w3.org/2002/12/cal/ical#created>  "2020-12-26T16:09:34.880Z"^^xsd:dateTime ;
        <http://schema.org/text>  "Walk the dog" ;
        <http://www.w3.org/2002/12/cal/ical#completed>  "2020-12-26T16:09:39.853Z"^^xsd:dateTime .

```

We will also want to mark to-dos as "undone", so essentially removing this property from the to-do. For that we will need to modify our `handleCheck` function so that it removes the to-do if it was marked as done at the moment of clicking the checkbox, or add it if it was undone:

```jsx
// components/TodoList/index.jsx
import {
  addDatetime,
  getDatetime,
  getSourceUrl,
  getThingAll,
  getUrl, 
  removeDatetime,
  saveSolidDatasetAt,
  setThing,
} from "@inrupt/solid-client";

const COMPLETED_PREDICATE = "http://www.w3.org/2002/12/cal/ical#completed";

function TodoList({ todoList, setTodoList }) {
const { fetch } = useSession();
// ...

const handleCheck = async (todo, checked) => {
    const todosUrl = getSourceUrl(todoList);
    let updatedTodos;
    let date;
    if (!checked) {
      date = new Date();
      const doneTodo = addDatetime(todo, COMPLETED_PREDICATE, date);
      updatedTodos = setThing(todoList, doneTodo, { fetch });
    } else {
      date = getDatetime(todo, COMPLETED_PREDICATE);
      const undoneTodo = removeDatetime(todo, COMPLETED_PREDICATE, date);
      updatedTodos = setThing(todoList, undoneTodo, { fetch });
    }
    const updatedList = await saveSolidDatasetAt(todosUrl, updatedTodos, {
      fetch,
    });
    setTodoList(updatedList);
  };
// ...
}

```

And we need to update the `CompletedBody` component as well:

```jsx
// components/TodoList/index.jsx

function CompletedBody({ checked, handleCheck }) {
    const { thing } = useThing();
    return (
      <label>
        <input
          type="checkbox"
          checked={checked}
          onChange={() => handleCheck(thing, checked)}
        />
      </label>
    );
  }

```

Notice we need to use `setTodoList` here to update the to-do list, which we are getting from the `App` component.

There is one little bug though: each time we check a to-do, our list gets rearranged.

To fix this, we can sort the things array after we extract the things from the to-do list dataset. We want them sorted by the date they were created:

```jsx
// components/TodoList/index.jsx

const todoThings = todoList ? getThingAll(todoList) : [];
  todoThings.sort((a, b) => {
    return (
      getDatetime(a, CREATED_PREDICATE) - getDatetime(b, CREATED_PREDICATE)
    );
  });

```

In addition, with the `TableColumn` component we can sort items by property. If we pass a `sortable` prop to one of our columns, we can arrange our to-dos based on that property, so let's use the "Created At" column and the to-do content column to see how it works. Let's also add a "To do" header to the content column so we can see what criteria we are sorting by. 

Our (almost) finished `TodoList` component now looks like this:

```jsx
// components/TodoList/index.jsx

import {
  addDatetime,
  getDatetime,
  getSourceUrl,
  getThingAll,
  getUrl,
  removeDatetime,
  saveSolidDatasetAt,
  setThing,
} from "@inrupt/solid-client";
import {
  Table,
  TableColumn,
  useThing,
  useSession,
} from "@inrupt/solid-ui-react";
import React from "react";

const TEXT_PREDICATE = "http://schema.org/text";
const CREATED_PREDICATE = "http://www.w3.org/2002/12/cal/ical#created";
const COMPLETED_PREDICATE = "http://www.w3.org/2002/12/cal/ical#completed";

function CompletedBody({ checked, handleCheck }) {
    const { thing } = useThing();
    return (
      <label>
        <input
          type="checkbox"
          checked={checked}
          onChange={() => handleCheck(thing, checked)}
        />
      </label>
    );
  }

function TodoList({ todoList, setTodoList }) {
  const todoThings = todoList ? getThingAll(todoList) : [];
  todoThings.sort((a, b) => {
    return (
      getDatetime(a, CREATED_PREDICATE) - getDatetime(b, CREATED_PREDICATE)
    );
  });

  const { fetch } = useSession();

  const handleCheck = async (todo, checked) => {
    const todosUrl = getSourceUrl(todoList);
    let updatedTodos;
    if (!checked) {
      const date = new Date();
      const doneTodo = addDatetime(todo, COMPLETED_PREDICATE, date);
      updatedTodos = setThing(todoList, doneTodo, { fetch });
    } else {
      const date = getDatetime(todo, COMPLETED_PREDICATE);
      const undoneTodo = removeDatetime(todo, COMPLETED_PREDICATE, date);
      updatedTodos = setThing(todoList, undoneTodo, { fetch });
    }
    const updatedList = await saveSolidDatasetAt(todosUrl, updatedTodos, {
      fetch,
    });
    setTodoList(updatedList);
  };

  const thingsArray = todoThings
    .filter((t) => getUrl(t, TYPE_PREDICATE) === TODO_CLASS)
    .map((t) => {
      return { dataset: todoList, thing: t };
    });
  if (!thingsArray.length) return null;

  return (
    <div className="table-container">
      <span className="tasks-message">
        Your to-do list has {thingsArray.length} items
      </span>
      <Table className="table" things={thingsArray}>
        <TableColumn property={TEXT_PREDICATE} header="To Do" sortable />
        <TableColumn
          property={CREATED_PREDICATE}
          dataType="datetime"
          header="Created At"
          body={({ value }) => value.toDateString()}
          sortable
        />
        <TableColumn
          property={COMPLETED_PREDICATE}
          dataType="datetime"
          header="Done"
          body={({ value }) => <CompletedBody checked={Boolean(value)} handleCheck={handleCheck} />}
        />
      </Table>
    </div>
  );
}

export default TodoList;

```

# How to Delete a To-Do 

To delete a to-do, we will need a new column to add a delete button.

We will also need to write a function that takes the to-do `Thing` and deletes it on click:

```jsx
// components/TodoList/index.jsx

import {
  addDatetime,
  getDatetime,
  getSourceUrl,
  getThingAll,
  getUrl,
  removeDatetime,
	removeThing,
  saveSolidDatasetAt,
  setThing,
} from "@inrupt/solid-client";

function TodoList({ todoList, setTodoList }) {
// ...
	const deleteTodo = async (todo) => {
	    const todosUrl = getSourceUrl(todoList);
	    const updatedTodos = removeThing(todoList, todo);
	    const updatedDataset = await saveSolidDatasetAt(todosUrl, updatedTodos, {
	      fetch,
	    });
	    setTodoList(updatedDataset);
	  };
// ...
}

```

We can get the to-do `Thing` using the `useThing` hook (like we did before with the `CompleteBody` component to mark to-dos as done), so it doesn't really matter which property we use. But because `property` is not optional in the `TableColumn` component, we'll use the to-do text.

Since we need to use a hook, we have to write a proper React component for the custom body outside the `TodoList` component:

```jsx
// components/TodoList/index.jsx

function DeleteButton({ deleteTodo }) {
    const { thing } = useThing();
    return (
      <button className="delete-button" onClick={() => deleteTodo(thing)}>
        Delete
      </button>
    );
  }

```

And add the column to the table, after the last column:

```jsx
// components/TodoList/index.jsx

<TableColumn
          property={TEXT_PREDICATE}
          header=""
          body={() => <DeleteButton deleteTodo={deleteTodo} />}
        />

```

That's it! Now if we click the delete button, we can delete the to-do.

# Conclusion

### Where to go from here

You have completed the tutorial! You now know the basics of how to create your own Solid app. Now you can go and build your own app from scratch, experiment, and learn more. Here are some resources to help you:

* [Solid UI React Docs](https://solid-ui-react.docs.inrupt.com/?path=/story/intro--page)
* [Solid Client Libraries Docs](https://docs.inrupt.com/developer-tools/javascript/client-libraries/)
* [Solid apps you can test and play around with](https://inrupt.com/solidApps/solid-app-listing)
* [The Solid Community Forum, where you can ask questions and see what people are talking about](https://forum.solidproject.org/)

