---
title: How to Build a Voice-Based Todo App using React, Firebase, and Alan AI
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-11-16T15:32:00.000Z'
originalURL: https://freecodecamp.org/news/build-a-voice-based-weather-application-using-react-and-alan-ai
coverImage: https://www.freecodecamp.org/news/content/images/2021/11/How-to-Build-a-Weather-Application-using-React--36-.png
tags:
- name: Apps
  slug: apps-tag
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Firebase
  slug: firebase
- name: React
  slug: react
seo_title: null
seo_desc: 'By Nishant Kumar

  React Todo applications are generally very basic – in fact, they''re a great exercise
  if you''re a React beginner and want to work on building up your skills.

  But have you ever built a Todo application where a user can add todos using ...'
---

By Nishant Kumar

React Todo applications are generally very basic – in fact, they're a great exercise if you're a React beginner and want to work on building up your skills.

But have you ever built a Todo application where a user can add todos using voice commands? This makes it a bit more complex and exciting.

So that's what we're going to do in this tutorial. And to build this voice-based Todo app, we will be using three main tools:

1. React – for the user interface.
2. Firebase – for the database.
3. Alan AI – for implementing voice commands.

So, let's get started.

## How to Create the Todo App UI using React

Let's create our React app first. Simply type in the following command:

```
npx create-react-app react-todo-alan-firebase
```

It will initialize and create our React Application like this. Then, we'll navigate into that folder and start the application using npm start.

Now let's create a folder called components. It will contain our main component, called Todo.js. Create the Todo.js file as well.

```
import React from 'react'

export default function Todo() {
    return (
        <div>
            
        </div>
    )
}

```

Give the application a header (or name), something like Voice-based Todo Application, or anything of your choice.

```
import React from 'react'

export default function Todo() {
    return (
        <div>
            <h2>Voice-based Todo Application</h2>
        </div>
    )
}

```

Then, import this component into your App.js file.

```
import './App.css';
import Todo from './components/Todo';

function App() {
  return (
    <div>
      <Todo />
    </div>
  );
}

export default App;

```

You will see the Header on the output screen.

Let's make the header appear in the center. So, give the `h2` a classname of header in the Todo.js component.

```
import React from 'react'

export default function Todo() {
    return (
        <div>
            <h2 className="header">Voice-based Todo Application</h2>
        </div>
    )
}

```

And then we'll add some styling in App.css file so the header is centered.

```
.header{
  text-align: center;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-2021-11-15-215217.png)

You will see the above output on the screen, with the centered header.

Now, let's create a card that will contain our todo items.

```
import React from 'react'

export default function Todo() {
    return (
        <div className="todo-main">
            <h2 className="header">Voice-based Todo Application</h2>

            <div className="todo-card">

            </div>
        </div>
    )
}

```

Create a div and make the `className` be `todo-card`. You will see the main parent div has the `className` of `todo-main`. This is because we need everything in the center.

```
.todo-main {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}

.header {
  text-align: center;
}

.todo-card {
  border: 1px dashed #1f133d;
  height: 50vh;
  width: 50vh;
  border-radius: 20px;
}

```

And add the above styles to App.css. It'll look like this now:

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-2021-11-15-220125.png)

Let's add the lists now. 

```
import React from 'react'

export default function Todo() {
    return (
        <div className="todo-main">
            <h2 className="header">Voice-based Todo Application</h2>

            <div className="todo-card">
                <div className="todo-list">
                    <h3>
                        Wash the Clothes
                    </h3>
                </div>
                <div className="todo-list">
                    <h3>
                        Cook the Dinner
                    </h3>
                </div>
                <div className="todo-list">
                    <h3>
                        Code some software
                    </h3>
                </div>
            </div>
        </div>
    )
}

```

So, I have created a div, and it contains the items in `h3` tags. These texts are static for now, but we will soon create dynamic texts too, coming from the Firebase Database.

And here are our updated styles:

```
.todo-main {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}

.header {
  text-align: center;
}

.todo-card {
  border: 1px dashed #1f133d;
  height: 50vh;
  width: 50vh;
  border-radius: 20px;
}

.todo-list{
  text-align: center;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-2021-11-15-220710.png)

So that's the output now, with three items on our list.

Now, let's add a close icon, that will remove each item after we are done with it.

And to add icons, we need an icon package. So, let's install React Icons with this command:

```
npm install react-icons --save
```

After the installation, choose any icon package from the left sidebar.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-2021-11-15-220805.png)

I am using Feather Icons, so I will import it.

First, let's import that package using this command:

```
import { FiX } from "react-icons/fi";
```

Then, call it after the h3 tag.

```
import React from 'react'
import { FiX } from "react-icons/fi";
export default function Todo() {
    return (
        <div className="todo-main">
            <h2 className="header">Voice-based Todo Application</h2>

            <div className="todo-card">
                <div className="todo-list">
                    <h3>
                        Wash the Clothes
                    </h3>
                    <FiX />
                </div>
                <div className="todo-list">
                    <h3>
                        Cook the Dinner
                    </h3>
                    <FiX />
                </div>
                <div className="todo-list">
                    <h3>
                        Code some software
                    </h3>
                    <FiX />
                </div>
            </div>
        </div>
    )
}

```

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-2021-11-15-221145.png)

Above, this is what our application looks like now. But we want the close icon and the todo item to be in the same row.

Give the Icon a className of `close-icon`.

```
 <FiX className="close-icon" />
```

And in the App.css, add the following styles:

```
.todo-list {
  display: flex;
  align-items: center;
  justify-content: center;
}

.close-icon {
  margin-left: 10px;
}

```

Our Todo.js component will have the following final code up to this point:

```
import React from 'react'
import { FiX } from "react-icons/fi";
export default function Todo() {
    return (
        <div className="todo-main">
            <h2 className="header">Voice-based Todo Application</h2>

            <div className="todo-card">
                <div className="todo-list">
                    <h3>
                        Wash the Clothes
                    </h3>
                    <FiX className="close-icon" />
                </div>
                <div className="todo-list">
                    <h3>
                        Cook the Dinner
                    </h3>
                    <FiX className="close-icon" />
                </div>
                <div className="todo-list">
                    <h3>
                        Code some software
                    </h3>
                    <FiX className="close-icon" />
                </div>
            </div>
        </div>
    )
}

```

And our App.css looks like this:

```
.todo-main {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}

.header {
  text-align: center;
}

.todo-card {
  border: 1px dashed #1f133d;
  height: 50vh;
  width: 50vh;
  border-radius: 20px;
}

.todo-list {
  display: flex;
  align-items: center;
  justify-content: center;
}

.close-icon {
  margin-left: 10px;
}

```

Now this is how our UI will look:

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-2021-11-15-221826.png)

## How to Add Alan AI to our React Project

Head over to [https://alan.app/](https://alan.app/) and create your account.

After signing in, you can create a project. Just click the plus button.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-2021-11-15-222106.png)

But before we can use it, we need to install the Alan AI package first. So, head over to [https://alan.app/docs/client-api/web/react](https://alan.app/docs/client-api/web/react) for the React documentation.

Install Alan Al using the following command:

```
npm install @alan-ai/alan-sdk-web --save
```

Now, let's import Alan in our main App.js file.

```
import alanBtn from "@alan-ai/alan-sdk-web";
```

Then, we need to create a useEffect Hook. It will start our Alan service whenever our component is mounted or loaded.

```
useEffect(() => {
    alanBtn({
        key: 'YOUR_KEY_FROM_ALAN_STUDIO_HERE',
        onCommand: (commandData) => {
            if (commandData.command === 'go:back') {
                // Call the client code that will react to the received command
            }
        }
    });
}, []);
```

This `alanBtn` requires a key which we'll need to get. So, in the project that you created in Alan, you should see an "Integrations" button in the top bar. Click that button.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-2021-11-15-222645.png)

And there you will get your key.

Paste that key in your `alanBtn` in your React app, like this:

```
import './App.css';
import Todo from './components/Todo';
import alanBtn from "@alan-ai/alan-sdk-web";
import { useEffect } from 'react'
function App() {
  useEffect(() => {
    alanBtn({
      key: '86e866fbe49666abd385ee5c9f9cbf5c2e956eca572e1d8b807a3e2338fdd0dc/stage',
      onCommand: (commandData) => {

      }
    });
  }, []);
  return (
    <div>
      <Todo />
    </div>
  );
}

export default App;

```

Now, check the output, and you will see a microphone button.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-2021-11-15-222913.png)

Now, we need to create an Intent in our Alan App. It will start with the Add command, like add Washing Clothes, add Write Some Code, and so on. So, let's write the code for that:

```
intent('Add $(item* (.*))', (p) => {
    if(p.item.value){
        p.play({ command: 'todoApp', data: p.item.value });
        p.play(`${p.item.value} added`);
    }
    else{
        p.play(`Cannot add Empty Item`);
    }
})
```

It will also return the item back to us, which we can see in our React Application. Here, we also have a check that stops us from adding any empty item. If we try, it will reply with "Cannot add Empty Item".

Now, we want to receive the spoken item back to our React application. 

```
import './App.css';
import Todo from './components/Todo';
import alanBtn from "@alan-ai/alan-sdk-web";
import { useEffect } from 'react'
function App() {
  useEffect(() => {
    alanBtn({
      key: '86e866fbe49666abd385ee5c9f9cbf5c2e956eca572e1d8b807a3e2338fdd0dc/stage',
      onCommand: (commandData) => {
        console.log(commandData)
      }
    });
  }, []);
  return (
    <div>
      <Todo />
    </div>
  );
}

export default App;

```

Simply console.log the commandData, and you'll get the following result. Don't forget to click the microphone button and say something. You'll see what you said in the console.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-2021-11-15-223428.png)

Alright great, our Alan AI is now all set.

## How to Use Firebase to Send Data to the Firestore Database.

We will now send this data to Firebase.

But first, we need to install it. Head over to [https://firebase.google.com/](https://firebase.google.com/) and create a project there as well.

To install Firebase, simply type `npm install firebase`.

Then, create an application in the project, like this:

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-2021-11-15-223909.png)

It will give us some configuration data. Just create a file in the src folder, name it `firebase-config.js`, and add those configuration data.

```
// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";

// Your web app's Firebase configuration
const firebaseConfig = {
    apiKey: "AIzaSyCP8qL8z9BorGF3NZJsGb4vSaWHYyCVfc8",
    authDomain: "todo-firebase-alan.firebaseapp.com",
    projectId: "todo-firebase-alan",
    storageBucket: "todo-firebase-alan.appspot.com",
    messagingSenderId: "892581913000",
    appId: "1:892581913000:web:dbe08ac753c3adaab87d9d"
};

// Initialize Firebase
export const app = initializeApp(firebaseConfig);
```

Don't forget to export the const app.

Next, we need to access Firestore as well. So, let's import it here in our firebase-config.js file.

```
import { getFirestore } from 'firebase/firestore'
```

```
export const database = getFirestore(app);
```

And export it too at the bottom.

```
// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getFirestore } from 'firebase/firestore'

// Your web app's Firebase configuration
const firebaseConfig = {
    apiKey: "AIzaSyCP8qL8z9BorGF3NZJsGb4vSaWHYyCVfc8",
    authDomain: "todo-firebase-alan.firebaseapp.com",
    projectId: "todo-firebase-alan",
    storageBucket: "todo-firebase-alan.appspot.com",
    messagingSenderId: "892581913000",
    appId: "1:892581913000:web:dbe08ac753c3adaab87d9d"
};

// Initialize Firebase
export const app = initializeApp(firebaseConfig);
export const database = getFirestore(app);
```

This is the whole firebase-config code.

Now, in App.js, we need to import this app and database.

```
import { app, database } from './firebase-config';
```

Next, we need to create a connection to our Firebase Firestore. For that, we need the collection property from Firebase Firestore. Also, we'll import addDoc which we'll use to add data to Firestore.

```
import { collection, addDoc } from 'firebase/firestore';
```

Now, let's create the connection to our database.

Create a variable, and put in the database that we imported from the firebase-config file along with the name we want to give to our collection. Since we want the collection to be todo-list, we can add the following:

```
const databaseRef = collection(database, 'todo-list');
```

To add data, we need that addDoc property.

The addDoc property will take two parameters. The first is the connection we created, the databaseRef. The second is the data we want to add, as an object.

Put the addDoc in the useEffect Hook like this:

```
useEffect(() => {
    alanBtn({
      key: '86e866fbe49666abd385ee5c9f9cbf5c2e956eca572e1d8b807a3e2338fdd0dc/stage',
      onCommand: (commandData) => {
        addDoc(databaseRef, { item: commandData.data })
      }
    });
  }, []);
```

Currently, our Firestore is empty.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-2021-11-15-225805.png)

Now, let's try this out. Speak something into the microphone starting with add command, and it will be visible in the Firebase Firestore.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-2021-11-15-225922.png)

You see, what we said is now getting added in Firebase.

Now, let's try to read and display this data.

Pass the `databaseRef` to the Todo Component as a prop.

```
<Todo databaseRef={databaseRef}/>
```

And then receive it in the Todo Component.

```
export default function Todo({databaseRef})
```

Create a useEffect hook in the Todo.js component, and inside the useEffect Hook create the function `getData`.

```
useEffect(() => {
        const getData = async () => {
            
        }
        getData()
    }, [])
```

We will use getDocs property to read data from the Firebase Firestore. And we also need that connection databaseRef, that we passed as a prop previously.

```
let data = await getDocs(databaseRef);
```

```
const getData = async () => {
  let data = await getDocs(databaseRef);
  console.log(data.docs.map((item) => ({ ...item.data(), id: item.id })));
}
```

We map the incoming data to make it more readable. We also add the unique id of the item that the app will use to delete that item later.

Let's check our console now:

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-2021-11-15-231500.png)

You see, we are getting it.

Now, let's store this data in a state to display in the React Application.

Import the useState Hook, then create an array state like this:

```
 const [todoList, setTodoList] = useState([]);
```

And set the data using the `setTodoList` function:

```
setTodoList(data.docs.map((item) => ({ ...item.data(), id: item.id })));
```

Now, let's map the todoList array.

```
<div className="todo-main">
            <h2 className="header">Voice-based Todo Application</h2>

            <div className="todo-card">
                {todoList.map((todo) => {
                    return (
                        <div className="todo-list">
                            <h3>
                                {todo.item}
                            </h3>
                            <FiX className="close-icon" />
                        </div>
                    )
                })}
            </div>
        </div>
```

We will see our data in our React UI and it looks like this:

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-2021-11-15-231945.png)

Now, let's update this so that each Todo starts with a capital letter.

Give h3 as the `className` of `todo-items`.

```
<h3 className="todo-item">
 {todo.item}
</h3>
```

And in App.css, add this styling:

```
.todo-item{
  text-transform: capitalize;
}
```

And you will see that each Todo is capitalized now.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-2021-11-15-232149.png)

Now, if we add anything by speech command, our list in React should update. So, let's configure our useEffect to run every time we speak something into the app.

In the App.js file, create one state. It will be a boolean, with the initial state of false.

```
const [update, setUpdate] = useState(false)
```

This state will change to true when we say something, or when the useEffect in App.js runs.

```
useEffect(() => {
    alanBtn({
      key: '86e866fbe49666abd385ee5c9f9cbf5c2e956eca572e1d8b807a3e2338fdd0dc/stage',
      onCommand: (commandData) => {
        addDoc(databaseRef, { item: commandData.data })
        .then(() => {
          setUpdate(true);
        })
      }
    });
  }, []);
```

Then, we will pass the update state and the function to update state in Todo.js. 

```
<Todo databaseRef={databaseRef} update={update} setUpdate={setUpdate}/>
```

And receive these two in the Todo component.

```
export default function Todo({ databaseRef, update, setUpdate })
```

Then, in the useEffect of Todo.js, once it's fetched our data from Firebase Firestore, set the update to false using the setUpdate function. Then put the update state in the dependency array. 

```
useEffect(() => {
        const getData = async () => {
            let data = await getDocs(databaseRef);
            setTodoList(data.docs.map((item) => ({ ...item.data(), id: item.id })));
        }
        getData()
        setUpdate(false)
    }, [update])
```

This might be a bit confusing, but let me explain.

When we speak, the update state is changed from false to true. Then, when the data fetching from Firestore is done, it is being changed to false from true. That way, the state is constantly changing. So the useEffect gets updated every time the update state changes.

Let's try it out now. Say something and the list will be dynamically updated.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-2021-11-15-233617.png)

Now, let's add the delete function to delete items from Firebase Firestore and our React application.

Create a function called `deleteItems`.

```
const deleteItems = () => {
        
}
```

And bind this function to the `close` icon like this:

```
<FiX className="close-icon" onClick={() => deleteItems()}/>
```

When we click a particular close icon, we need to pass the id of that item to the function, which will be used to delete that item.

```
<FiX className="close-icon" onClick={() => deleteItems(todo.id)}/>
```

And in the function, receive it.

Let's try to console.log our id:

```
const deleteItems = (id) => {
  console.log(id)
}
```

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-2021-11-15-234631.png)

We will get that particular id in the console.

Now, before deleting any todo item, we need to specify which todo to delete. So, we will create a reference using this id. We will use the doc property from Firestore.

So, first import doc from Firestore with this command:

```
import { getDocs, doc } from 'firebase/firestore';
```

Then, in the function 1deleteItems1, add the following code:

```
const data = doc(database, 'todo-list', id)
```

This doc takes three parameters – the database, the collection name, and the id. We have all the three things.

The database has been imported from firebase-config. The todo-list is the name of the Firestore collection. And the id we got from the close button click.

To delete an item, we need another property called deleteDoc from Firestore.

```
import { getDocs, doc, deleteDoc } from 'firebase/firestore';
```

Then, simply add the following:

```
const deleteItems = (id) => {
   const data = doc(database, 'todo-list', id);
   deleteDoc(data)
}
```

Try it now – click the close icon, then check Firestore. That item will be deleted.

But we have the same problem we had during the add and read actions: the React application is not getting updated after we delete an item.

So, the first thing to do is move the getData function outside the useEffect Hook. Don't worry, it will still work.

```
const getData = async () => {
   let data = await getDocs(databaseRef);
   setTodoList(data.docs.map((item) => ({ ...item.data(), id: item.id })));
}

useEffect(() => {   
   getData()
   setUpdate(false)
}, [update])
```

And in the deleteDoc function, we need to call the getData function again, to fetch the updated data after the user deletes an item.

```
const deleteItems = (id) => {
    const data = doc(database, 'todo-list', id);
    deleteDoc(data)
    .then(() => {
       getData()
    })
}
```

Here is the whole Todo.js code:

```
import React, { useEffect, useState } from 'react'
import { FiX } from "react-icons/fi";
import { database } from '../firebase-config';
import { getDocs, doc, deleteDoc } from 'firebase/firestore';
export default function Todo({ databaseRef, update, setUpdate }) {
    const [todoList, setTodoList] = useState([]);
    const getData = async () => {
        let data = await getDocs(databaseRef);
        setTodoList(data.docs.map((item) => ({ ...item.data(), id: item.id })));
    }
    useEffect(() => {
        getData()
        setUpdate(false)
    }, [update])

    const deleteItems = (id) => {
        const data = doc(database, 'todo-list', id);
        deleteDoc(data)
            .then(() => {
                getData()
            })
    }

    return (
        <div className="todo-main">
            <h2 className="header">Voice-based Todo Application</h2>

            <div className="todo-card">
                {todoList.map((todo) => {
                    return (
                        <div className="todo-list">
                            <h3 className="todo-item">
                                {todo.item}
                            </h3>
                            <FiX className="close-icon" onClick={() => deleteItems(todo.id)} />
                        </div>
                    )
                })}
            </div>
        </div>
    )
}

```

And the App.js code as well:

```
import './App.css';
import Todo from './components/Todo';
import alanBtn from "@alan-ai/alan-sdk-web";
import { useEffect, useState } from 'react';
import { app, database } from './firebase-config';
import { addDoc, collection } from '@firebase/firestore';
function App() {
  const databaseRef = collection(database, 'todo-list');
  const [update, setUpdate] = useState(false)
  useEffect(() => {
    alanBtn({
      key: '86e866fbe49666abd385ee5c9f9cbf5c2e956eca572e1d8b807a3e2338fdd0dc/stage',
      onCommand: (commandData) => {
        addDoc(databaseRef, { item: commandData.data })
          .then(() => {
            setUpdate(true);
          })
      }
    });
  }, []);
  return (
    <div>
      <Todo databaseRef={databaseRef} update={update} setUpdate={setUpdate} />
    </div>
  );
}

export default App;

```

Now, we can add items using voice commands, and it will be stored in our Firebase Database. It will also show up in our React Application.

Ther's one last thing to do. In our App.css file, we need to set the height of the card to auto, to prevent the text from overflowing.

```
.todo-card {
  border: 1px dashed #1f133d;
  height: auto;
  width: 50vh;
  border-radius: 20px;
}
```

And this is just a simple UI design. You can use your own designs if you want. Go ahead, build this awesome application.

Thanks for reading!

You can check out my video on the same topic at [Let's build a Voice-Based Todo Application using React, Firebase, and Alan AI](https://youtu.be/BzHbI2AAXGs), which is on my YouTube channel.

> Happy Learning.

