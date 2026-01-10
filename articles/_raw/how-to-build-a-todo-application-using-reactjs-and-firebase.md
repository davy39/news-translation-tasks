---
title: How to Build a TodoApp using ReactJS and Firebase
subtitle: ''
author: Sharvin Shah
co_authors: []
series: null
date: '2020-04-15T00:01:20.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-todo-application-using-reactjs-and-firebase
coverImage: https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-11-at-5.10.03-PM.png
tags:
- name: Apps
  slug: apps-tag
- name: Firebase
  slug: firebase
- name: React
  slug: reactjs
seo_title: null
seo_desc: 'Hello folks, welcome to this tutorial. Before we begin you should be familiar
  with basic ReactJS concepts. If you''re not, I would recommend that you go through
  the ReactJS documentation.

  We will use the following components in this application:


  Reac...'
---

Hello folks, welcome to this tutorial. Before we begin you should be familiar with basic ReactJS concepts. If you're not, I would recommend that you go through the [ReactJS documentation](https://reactjs.org/docs/getting-started.html).

We will use the following components in this application:

1. [**ReactJS**](https://reactjs.org/)
    
2. [**Material UI**](https://material-ui.com/)
    
3. [**Firebase**](https://firebase.google.com/)
    
4. [**ExpressJS**](https://expressjs.com/)
    
5. [**Postman**](https://www.postman.com/)
    

## How our application is going to look:

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Account-1.gif align="left")

*Account creation*

![Image](https://www.freecodecamp.org/news/content/images/2020/04/ezgif.com-optimize.gif align="left")

*TodoApp Dashboard*

---

## Application Architecture:

![Image](https://www.freecodecamp.org/news/content/images/2020/04/TodoApp-1.png align="left")

*Application Architecture*

## Understanding our components:

You may be wondering why we are using firebase in this application. Well, it provides secure **Authentication**, a **Real-time database**, a **Serverless Component,** and a **Storage bucket**.

We are using Express here so that we don't need to handle HTTP Exceptions. We are going to use all the firebase packages in our functions component. This is because we don't want to make our client application too big, which tends to slow the loading process of the UI.

**Note:** I am going to divide this tutorial into four separate sections. At the start of every section, you will find a git commit that has the code developed in that section. Also If you want to see the complete code then it is available in this [repository](https://github.com/Sharvin26/TodoApp).

## Section 1: Developing Todo APIs

In this section\*\*,\*\* we are going to develop these elements:

1. **Configure the firebase functions.**
    
2. **Install the Express framework and build Todo APIs.**
    
3. **Configuring firestore as database.**
    

The **Todo API code** implemented in this section can be found at this [commit](https://github.com/Sharvin26/TodoApp/tree/256e69f5d53646b648347b6f1fbdb965ad184763).

### Configure Firebase Functions:

Go to the [Firebase console](https://firebase.google.com/).

![Image](https://www.freecodecamp.org/news/content/images/2020/04/FirebaseFunctions.png align="left")

*Firebase Console*

Select the **Add Project** option. After that follow the gif down below step by step to configure the firebase project.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/FirebaseConfigure.gif align="left")

*Firebase Configuration*

Go to the functions tab and click on the **Get Started** button:

![Image](https://www.freecodecamp.org/news/content/images/2020/04/FirebaseFunctionConfig1.png align="left")

*Functions Dashboard*

You will see a dialogue box which has instructions on **How to set up the Firebase Functions**. Go to your local environment. Open a command-line tool. To install the firebase tools in your machine use the command below:

```shell
 npm install -g firebase-tools
```

Once that is done then use the command `firebase init` to configure the firebase functions in your local environment. Select the following options when initialising the firebase function in the local environment:

1. Which Firebase CLI features do you want to set up for this folder? Press Space to select features, then Enter to confirm your choices =&gt; *Functions: Configure and deploy Cloud Functions*
    
2. First, let’s associate this project directory with a Firebase project …. *\=&gt; Use an existing project*
    
3. Select a default Firebase project for this directory =&gt; *application\_name*
    
4. What language would you like to use to write Cloud Functions? =&gt; *JavaScript*
    
5. Do you want to use ESLint to catch probable bugs and enforce style? =&gt; *N*
    
6. Do you want to install dependencies with npm now? (Y/n) =&gt; *Y*
    

After the configuration is done you will get the following message:

```shell
✔ Firebase initialization complete!
```

This will be our directory structure once the initialization is completed:

```shell
+-- firebase.json 
+-- functions
|   +-- index.js
|   +-- node_modules
|   +-- package-lock.json
|   +-- package.json
```

Now open the `index.js` under functions directory and copy-paste the following code:

```js
const functions = require('firebase-functions');

exports.helloWorld = functions.https.onRequest((request, response) => {
     response.send("Hello from Firebase!");
});
```

Deploy the code to firebase functions using the following command:

```shell
firebase deploy
```

Once the deployment is done you will get the following logline at the end of your command line:

```shell
> ✔  Deploy complete!
> Project Console: https://console.firebase.google.com/project/todoapp-<id>/overview
```

Go to the **Project Console &gt; Functions** and there you will find the URL of the API. The URL will look like this:

```shell
https://<hosting-region>-todoapp-<id>.cloudfunctions.net/helloWorld
```

Copy this URL and paste it in the browser. You will get the following response:

```shell
Hello from Firebase!
```

This confirms that our Firebase function has been configured properly.

### Install the Express Framework:

Now let’s install the `Express` framework in our project using the following command:

```shell
npm i express
```

Now let's create an **APIs** directory inside the **functions** directory. Inside that directory, we will create a file named `todos.js`. Remove everything from the `index.js` and then copy-paste the following code:

```js
//index.js

const functions = require('firebase-functions');
const app = require('express')();

const {
    getAllTodos
} = require('./APIs/todos')

app.get('/todos', getAllTodos);
exports.api = functions.https.onRequest(app);
```

We have assigned the getAllTodos function to the **/todos** route. So all the API calls on this route will execute via the getAllTodos function. Now go to the `todos.js` file under APIs directory and here we will write the getAllTodos function.

```js
//todos.js

exports.getAllTodos = (request, response) => {
    todos = [
        {
            'id': '1',
            'title': 'greeting',
            'body': 'Hello world from sharvin shah' 
        },
        {
            'id': '2',
            'title': 'greeting2',
            'body': 'Hello2 world2 from sharvin shah' 
        }
    ]
    return response.json(todos);
}
```

Here we have declared a sample JSON object. Later we will derive that from the Firestore. But for the time being we will return this. Now deploy this to your firebase function using the command `firebase deploy`. It will ask for permission to delete the module **helloworld** – just enter **y**.

```shell
The following functions are found in your project but do not exist in your local source code: helloWorld

Would you like to proceed with deletion? Selecting no will continue the rest of the deployments. (y/N) y
```

Once this is done go to the **Project Console &gt; Functions** and there you will find the URL of the API. The API will look like this:

```shell
https://<hosting-region>-todoapp-<id>.cloudfunctions.net/api
```

Now go to the browser and copy-paste the URL and add **/todos** at the end of this URL. You will get the following output:

```json
[
        {
            'id': '1',
            'title': 'greeting',
            'body': 'Hello world from sharvin shah' 
        },
        {
            'id': '2',
            'title': 'greeting2',
            'body': 'Hello2 world2 from sharvin shah' 
        }
]
```

### Firebase Firestore:

We will use a firebase firestore as a real-time database for our application. Now go to the **Console &gt; Database** in Firebase Console. To configure firestore follow the gif below:

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Firestore.gif align="left")

*Configuring Firestore*

Once the configuration is done then click on the **Start Collection** button and set **Collection ID** as **todos**. Click Next and you will get the following popup:

![Image](https://www.freecodecamp.org/news/content/images/2020/04/FireStore-collection.png align="left")

*Creating Database Manually*

Ignore the DocumentID key. For the **field, type, and value**, refer to the JSON down below. Update the value accordingly:

```json
{
    Field: title,
    Type: String,
    Value: Hello World
},
{
    Field: body,
    Type: String,
    Value: Hello folks I hope you are staying home...
},
{
    Field: createtAt,
    type: timestamp,
    value: Add the current date and time here
}
```

Press the save button. You will see that the collection and the document is created. Go back to the local environment. We need to install `firebase-admin` which has the firestore package that we need. Use this command to install it:

```shell
npm i firebase-admin
```

Create a directory named **util** under the **functions** directory. Go to this directory and create a file name `admin.js`. In this file we will import the firebase admin package and initialize the firestore database object. We will export this so that other **modules** can use it.

```js
//admin.js

const admin = require('firebase-admin');

admin.initializeApp();

const db = admin.firestore();

module.exports = { admin, db };
```

Now let’s write an API to fetch this data. Go to the `todos.js` under the **functions &gt; APIs** directory. Remove the old code and copy-paste the code below:

```js
//todos.js

const { db } = require('../util/admin');

exports.getAllTodos = (request, response) => {
	db
		.collection('todos')
		.orderBy('createdAt', 'desc')
		.get()
		.then((data) => {
			let todos = [];
			data.forEach((doc) => {
				todos.push({
                    todoId: doc.id,
                    title: doc.data().title,
					body: doc.data().body,
					createdAt: doc.data().createdAt,
				});
			});
			return response.json(todos);
		})
		.catch((err) => {
			console.error(err);
			return response.status(500).json({ error: err.code});
		});
};
```

Here we are fetching all the todos from the database and forwarding them to the client in a list.

You can also run the application locally using `firebase serve` command instead of deploying it every time. When you run that command you may get an error regarding credentials. To fix it, follow the steps mentioned below:

1. Go to the **Project Settings** (Settings icon at the top left-hand side)
    
2. Go to the **service accounts tab**
    
3. Down there will be the option of **Generating a new key**. Click on that option and it will download a file with a JSON extension.
    
4. We need to export these credentials to our command line session. Use the command below to do that:
    

```shell
export GOOGLE_APPLICATION_CREDENTIALS="/home/user/Downloads/[FILE_NAME].json"
```

After that run firebase serve command. If you still get the error then use the following command: `firebase login --reauth`. It will open the Google sign-in page in a browser. Once sign-in is done then it will work without any error.

You will find a URL in the logs of your command-line tool when you run a firebase serve command. Open this URL in browser and append `/todos` after it.

```shell
✔ functions[api]: http function initialized (http://localhost:5000/todoapp-<project-id>/<region-name>/api).
```

You will get the following JSON output in your browser:

```json
[
    {
        "todoId":"W67t1kSMO0lqvjCIGiuI",
        "title":"Hello World",
        "body":"Hello folks I hope you are staying home...",
        "createdAt":{"_seconds":1585420200,"_nanoseconds":0 }
    }
]
```

### Writing Other APIs:

It's time to write all the other todo APIs that we are going to require for our application.

1. **Create Todo item:** Go to the `index.js` under the functions directory. Import postOneTodo method under the existing getAllTodos. Also, assign the POST route to that method.
    

```js
//index.js

const {
    ..,
    postOneTodo
} = require('./APIs/todos')

app.post('/todo', postOneTodo);
```

Go to the `todos.js` inside the functions directory and add a new method `postOneTodo` under the existing `getAllTodos` method.

```js
//todos.js

exports.postOneTodo = (request, response) => {
	if (request.body.body.trim() === '') {
		return response.status(400).json({ body: 'Must not be empty' });
    }
    
    if(request.body.title.trim() === '') {
        return response.status(400).json({ title: 'Must not be empty' });
    }
    
    const newTodoItem = {
        title: request.body.title,
        body: request.body.body,
        createdAt: new Date().toISOString()
    }
    db
        .collection('todos')
        .add(newTodoItem)
        .then((doc)=>{
            const responseTodoItem = newTodoItem;
            responseTodoItem.id = doc.id;
            return response.json(responseTodoItem);
        })
        .catch((err) => {
			response.status(500).json({ error: 'Something went wrong' });
			console.error(err);
		});
};
```

In this method, we are adding a new Todo to our database. If the elements of our body are empty then we will return a response of 400 or else we will add the data.

Run the firebase serve command and open the postman application. Create a new request and select the method type as **POST**. Add the URL and a body of type JSON.

```shell
URL: http://localhost:5000/todoapp-<app-id>/<region-name>/api/todo

METHOD: POST

Body: {
   "title":"Hello World",
   "body": "We are writing this awesome API"
}
```

Press the send button and you will get the following response:

```json
{
     "title": "Hello World",
     "body": "We are writing this awesome API",
     "createdAt": "2020-03-29T12:30:48.809Z",
     "id": "nh41IgARCj8LPWBYzjU0"
}
```

2. **Delete Todo item:** Go to the `index.js` under the functions directory. Import the deleteTodo method under the existing postOneTodo. Also, assign the DELETE route to that method.
    

```js
//index.js

const {
    ..,
    deleteTodo
} = require('./APIs/todos')

app.delete('/todo/:todoId', deleteTodo);
```

Go to the `todos.js` and add a new method `deleteTodo` under the existing `postOneTodo` method.

```js
//todos.js

exports.deleteTodo = (request, response) => {
    const document = db.doc(`/todos/${request.params.todoId}`);
    document
        .get()
        .then((doc) => {
            if (!doc.exists) {
                return response.status(404).json({ error: 'Todo not found' })
            }
            return document.delete();
        })
        .then(() => {
            response.json({ message: 'Delete successfull' });
        })
        .catch((err) => {
            console.error(err);
            return response.status(500).json({ error: err.code });
        });
};
```

In this method, we are deleting a Todo from our database. Run the firebase serve command and go to the postman. Create a new request, select the method type as **DELETE** and add the URL.

```shell
URL: http://localhost:5000/todoapp-<app-id>/<region-name>/api/todo/<todo-id>

METHOD: DELETE
```

Press the send button and you will get the following response:

```json
{
   "message": "Delete successfull"
}
```

3. **Edit Todo item:** Go to the `index.js` under the functions directory. Import the editTodo method under the existing deleteTodo. Also, assign the PUT route to that method.
    

```js
//index.js

const {
    ..,
    editTodo
} = require('./APIs/todos')

app.put('/todo/:todoId', editTodo);
```

Go to the `todos.js` and add a new method `editTodo` under the existing `deleteTodo` method.

```js
//todos.js

exports.editTodo = ( request, response ) => { 
    if(request.body.todoId || request.body.createdAt){
        response.status(403).json({message: 'Not allowed to edit'});
    }
    let document = db.collection('todos').doc(`${request.params.todoId}`);
    document.update(request.body)
    .then(()=> {
        response.json({message: 'Updated successfully'});
    })
    .catch((err) => {
        console.error(err);
        return response.status(500).json({ 
                error: err.code 
        });
    });
};
```

In this method, we are editing a Todo from our database. Remember here we are not allowing the user to edit the todoId or createdAt fields. Run the firebase serve command and go to the postman. Create a new request, select the method type as **PUT,** and add the URL.

```shell
URL: http://localhost:5000/todoapp-<app-id>/<region-name>/api/todo/<todo-id>

METHOD: PUT
```

Press the send button and you will get the following response:

```json
{  
   "message": "Updated successfully"
}
```

**Directory structure till now:**

```shell
+-- firebase.json 
+-- functions
|   +-- API
|   +-- +-- todos.js
|   +-- util
|   +-- +-- admin.js
|   +-- index.js
|   +-- node_modules
|   +-- package-lock.json
|   +-- package.json
|   +-- .gitignore
```

With this, we have completed the first section of the application. You can go ahead have some coffee, take a break, and after that we will work on developing the User APIs.

## Section 2: Developing User APIs

In this section\*\*,\*\* we are going to develop these components:

1. **User Authentication ( Login and Signup ) API.**
    
2. **GET and Update user details API.**
    
3. **Update the user profile picture API.**
    
4. **Securing the existing Todo API.**
    

The User API code implemented in this section can be found at this [commit](https://github.com/Sharvin26/TodoApp/tree/951a8605d988b8e17bd1623eac5c46e449786d1b).

So let’s start building the User Authentication API. Go to the **Firebase console &gt; Authentication.**

![Image](https://www.freecodecamp.org/news/content/images/2020/04/FirebaseAuthentication.png align="left")

*Firebase Authentication Page*

Click on the **Set up** **sign-in-method** button. We will use email and password for user validation. Enable the **Email/Password** option.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/FirebaseAuth1.png align="left")

*Firebase Set up Sign up page*

Right now we will manually create our user. First, we will build the Login API. After that we will build the Sign-Up API.

Go to the Users Tab under Authentication, fill in the User details, and click on the **Add User** button.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Login.png align="left")

*Adding user manually*

### 1\. User Login API:

First, we need to install the `firebase` package, which consists of the **Firebase Authentication library,** using the following command:

```shell
npm i firebase
```

Once the installation is done go to the **functions &gt; APIs** directory. Here we will create a `users.js` file. Now Inside `index.js` we import a loginUser method and assign the POST route to it.

```js
//index.js

const {
    loginUser
} = require('./APIs/users')

// Users
app.post('/login', loginUser);
```

Go to the **Project Settings &gt; General** and there you will find the following card:

![Image](https://www.freecodecamp.org/news/content/images/2020/04/app.png align="left")

*Getting Firebase configuration*

Select the Web Icon and then follow the gif down below:

![Image](https://www.freecodecamp.org/news/content/images/2020/04/project.gif align="left")

Select the **continue to console** option. Once this is done you will see a JSON with firebase config. Go to the **functions &gt; util** directory and create a `config.js` file. Copy-paste the following code in this file:

```js
// config.js

module.exports = {
    apiKey: "............",
    authDomain: "........",
    databaseURL: "........",
    projectId: ".......",
    storageBucket: ".......",
    messagingSenderId: "........",
    appId: "..........",
    measurementId: "......."
};
```

Replace `............` with the values that you get under **Firebase console &gt; Project settings &gt;** **General &gt; your apps &gt; Firebase SD snippet &gt; config**.

Copy-paste the following code in the `users.js` file:

```js
// users.js

const { admin, db } = require('../util/admin');
const config = require('../util/config');

const firebase = require('firebase');

firebase.initializeApp(config);

const { validateLoginData, validateSignUpData } = require('../util/validators');

// Login
exports.loginUser = (request, response) => {
    const user = {
        email: request.body.email,
        password: request.body.password
    }

    const { valid, errors } = validateLoginData(user);
	if (!valid) return response.status(400).json(errors);

    firebase
        .auth()
        .signInWithEmailAndPassword(user.email, user.password)
        .then((data) => {
            return data.user.getIdToken();
        })
        .then((token) => {
            return response.json({ token });
        })
        .catch((error) => {
            console.error(error);
            return response.status(403).json({ general: 'wrong credentials, please try again'});
        })
};
```

Here we are using a firebase **signInWithEmailAndPassword** module to check if the user-submitted credentials are right. If they are right then we send the token of that user or else a 403 status with a "wrong credentials" message.

Now let’s create `validators.js` under the **functions &gt; util** directory. Copy-paste the following code in this file:

```js
// validators.js

const isEmpty = (string) => {
	if (string.trim() === '') return true;
	else return false;
};

exports.validateLoginData = (data) => {
   let errors = {};
   if (isEmpty(data.email)) errors.email = 'Must not be empty';
   if (isEmpty(data.password)) errors.password = 'Must not be  empty';
   return {
       errors,
       valid: Object.keys(errors).length === 0 ? true : false
    };
};
```

With this our **LoginAPI** is completed. Run the `firebase serve` command and go to the postman. Create a new request, select the method type as **POST**, and add the URL and body.

```shell
URL: http://localhost:5000/todoapp-<app-id>/<region-name>/api/login

METHOD: POST

Body: {   
    "email":"Add email that is assigned for user in console", 
    "password": "Add password that is assigned for user in console"
}
```

Hit the send request button in postman and you will get the following output:

```json
{   
    "token": ".........."
}
```

We will use this token in an upcoming part to **get the user details**. Remember this token expires in **60 minutes**. To generate a new token use this API again.

### 2\. User Sign-up API:

The default authentication mechanism of firebase only allows you to store information like email, password, etc. But we need more information to identify if this user owns that todo so that they can perform read, update and delete operations on it.

To achieve this goal we are going to create a new collection called **users**. Under this collection, we will store the user’s data which will be mapped to the todo based on the username. Each username will be unique for all the users on the platform.

Go to the `index.js`. We import a signUpUser method and assign the POST route to it.

```js
//index.js

const {
    ..,
    signUpUser
} = require('./APIs/users')

app.post('/signup', signUpUser);
```

Now go to the `validators.js` and add the following code below the `validateLoginData` method.

```js
// validators.js

const isEmail = (email) => {
	const emailRegEx = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
	if (email.match(emailRegEx)) return true;
	else return false;
};

exports.validateSignUpData = (data) => {
	let errors = {};

	if (isEmpty(data.email)) {
		errors.email = 'Must not be empty';
	} else if (!isEmail(data.email)) {
		errors.email = 'Must be valid email address';
	}

	if (isEmpty(data.firstName)) errors.firstName = 'Must not be empty';
	if (isEmpty(data.lastName)) errors.lastName = 'Must not be empty';
	if (isEmpty(data.phoneNumber)) errors.phoneNumber = 'Must not be empty';
	if (isEmpty(data.country)) errors.country = 'Must not be empty';

	if (isEmpty(data.password)) errors.password = 'Must not be empty';
	if (data.password !== data.confirmPassword) errors.confirmPassword = 'Passowrds must be the same';
	if (isEmpty(data.username)) errors.username = 'Must not be empty';

	return {
		errors,
		valid: Object.keys(errors).length === 0 ? true : false
	};
};
```

Now go to the `users.js` and add the following code below the `loginUser` module.

```js
// users.js

exports.signUpUser = (request, response) => {
    const newUser = {
        firstName: request.body.firstName,
        lastName: request.body.lastName,
        email: request.body.email,
        phoneNumber: request.body.phoneNumber,
        country: request.body.country,
		password: request.body.password,
		confirmPassword: request.body.confirmPassword,
		username: request.body.username
    };

    const { valid, errors } = validateSignUpData(newUser);

	if (!valid) return response.status(400).json(errors);

    let token, userId;
    db
        .doc(`/users/${newUser.username}`)
        .get()
        .then((doc) => {
            if (doc.exists) {
                return response.status(400).json({ username: 'this username is already taken' });
            } else {
                return firebase
                        .auth()
                        .createUserWithEmailAndPassword(
                            newUser.email, 
                            newUser.password
                    );
            }
        })
        .then((data) => {
            userId = data.user.uid;
            return data.user.getIdToken();
        })
        .then((idtoken) => {
            token = idtoken;
            const userCredentials = {
                firstName: newUser.firstName,
                lastName: newUser.lastName,
                username: newUser.username,
                phoneNumber: newUser.phoneNumber,
                country: newUser.country,
                email: newUser.email,
                createdAt: new Date().toISOString(),
                userId
            };
            return db
                    .doc(`/users/${newUser.username}`)
                    .set(userCredentials);
        })
        .then(()=>{
            return response.status(201).json({ token });
        })
        .catch((err) => {
			console.error(err);
			if (err.code === 'auth/email-already-in-use') {
				return response.status(400).json({ email: 'Email already in use' });
			} else {
				return response.status(500).json({ general: 'Something went wrong, please try again' });
			}
		});
}
```

We validate our user data, and after that we send an email and password to the firebase **createUserWithEmailAndPassword** module to create the user. Once the user is created successfully we save the user credentials in the database.

With this our **SignUp API** is completed. Run the `firebase serve` command and go to the postman. Create a new request, select the method type as **POST**. Add the URL and body.

```shell
URL: http://localhost:5000/todoapp-<app-id>/<region-name>/api/signup

METHOD: POST

Body: {
   "firstName": "Add a firstName here",
   "lastName": "Add a lastName here",
   "email":"Add a email here",
   "phoneNumber": "Add a phone number here",
   "country": "Add a country here",
   "password": "Add a password here",
   "confirmPassword": "Add same password here",
   "username": "Add unique username here"
}
```

Hit the send request button in postman and you will get the following Output:

```json
{   
    "token": ".........."
}
```

Now go to the **Firebase console &gt; Database** and there you will see the following output:

![Image](https://www.freecodecamp.org/news/content/images/2020/04/database.png align="left")

As you can see our user’s collection is successfully created with one document in it.

### 3\. Upload User Profile Picture:

Our users will be able to upload their profile picture. To achieve this we will be using Storage bucket. Go to the **Firebase console &gt; Storage** and click on the **Get started** button. Follow the GIF below for the configuration:

![Image](https://www.freecodecamp.org/news/content/images/2020/04/storage.gif align="left")

Now go to the **Rules** tab under Storage and update the permission for the bucket access as per the image below:

![Image](https://www.freecodecamp.org/news/content/images/2020/04/storageRule.png align="left")

To upload the profile picture we will be using the package named `busboy`. To install this package, use the following command:

```shell
npm i busboy
```

Go to `index.js`. Import the uploadProfilePhoto method below the existing signUpUser method. Also assign the POST route to that method.

```js
//index.js

const auth = require('./util/auth');

const {
    ..,
    uploadProfilePhoto
} = require('./APIs/users')

app.post('/user/image', auth, uploadProfilePhoto);
```

Here we have added an authentication layer so that only a user associated with that account can upload the image. Now create a file named `auth.js` in **functions &gt; utils** directory. Copy-paste the following code in that file:

```js
// auth.js

const { admin, db } = require('./admin');

module.exports = (request, response, next) => {
	let idToken;
	if (request.headers.authorization && request.headers.authorization.startsWith('Bearer ')) {
		idToken = request.headers.authorization.split('Bearer ')[1];
	} else {
		console.error('No token found');
		return response.status(403).json({ error: 'Unauthorized' });
	}
	admin
		.auth()
		.verifyIdToken(idToken)
		.then((decodedToken) => {
			request.user = decodedToken;
			return db.collection('users').where('userId', '==', request.user.uid).limit(1).get();
		})
		.then((data) => {
			request.user.username = data.docs[0].data().username;
			request.user.imageUrl = data.docs[0].data().imageUrl;
			return next();
		})
		.catch((err) => {
			console.error('Error while verifying token', err);
			return response.status(403).json(err);
		});
};
```

Here we are using the firebase **verifyIdToken** module to verify the token. After that we are decoding the user details and passing them in the existing request.

Go to the `users.js` and add the following code below the `signup` method:

```js
// users.js

deleteImage = (imageName) => {
    const bucket = admin.storage().bucket();
    const path = `${imageName}`
    return bucket.file(path).delete()
    .then(() => {
        return
    })
    .catch((error) => {
        return
    })
}

// Upload profile picture
exports.uploadProfilePhoto = (request, response) => {
    const BusBoy = require('busboy');
	const path = require('path');
	const os = require('os');
	const fs = require('fs');
	const busboy = new BusBoy({ headers: request.headers });

	let imageFileName;
	let imageToBeUploaded = {};

	busboy.on('file', (fieldname, file, filename, encoding, mimetype) => {
		if (mimetype !== 'image/png' && mimetype !== 'image/jpeg') {
			return response.status(400).json({ error: 'Wrong file type submited' });
		}
		const imageExtension = filename.split('.')[filename.split('.').length - 1];
        imageFileName = `${request.user.username}.${imageExtension}`;
		const filePath = path.join(os.tmpdir(), imageFileName);
		imageToBeUploaded = { filePath, mimetype };
		file.pipe(fs.createWriteStream(filePath));
    });
    deleteImage(imageFileName);
	busboy.on('finish', () => {
		admin
			.storage()
			.bucket()
			.upload(imageToBeUploaded.filePath, {
				resumable: false,
				metadata: {
					metadata: {
						contentType: imageToBeUploaded.mimetype
					}
				}
			})
			.then(() => {
				const imageUrl = `https://firebasestorage.googleapis.com/v0/b/${config.storageBucket}/o/${imageFileName}?alt=media`;
				return db.doc(`/users/${request.user.username}`).update({
					imageUrl
				});
			})
			.then(() => {
				return response.json({ message: 'Image uploaded successfully' });
			})
			.catch((error) => {
				console.error(error);
				return response.status(500).json({ error: error.code });
			});
	});
	busboy.end(request.rawBody);
};
```

With this our **Upload Profile Picture API** is completed. Run the `firebase serve` command and go to the postman. Create a new request, select the method type as **POST**, add the URL, and in the body section select type as form-data.

The request is protected so you’ll need to send the **bearer token** also. To send the bearer token, log in again if the token has expired. After that in **Postman App &gt; Authorization tab &gt; Type &gt; Bearer Token** and in the token section paste the token.

```shell
URL: http://localhost:5000/todoapp-<app-id>/<region-name>/api/user/image

METHOD: GET

Body: { REFER THE IMAGE down below }
```

![Image](https://www.freecodecamp.org/news/content/images/2020/04/cover.png align="left")

Hit the send request button in postman and you will get the following Output:

```json
{        
    "message": "Image uploaded successfully"
}
```

### 4\. Get User Details:

Here we are fetching the data of our user from the database. Go to the `index.js` and import the getUserDetail method and assign GET route to it.

```js
// index.js

const {
    ..,
    getUserDetail
} = require('./APIs/users')

app.get('/user', auth, getUserDetail);
```

Now go to the `users.js` and add the following code after the `uploadProfilePhoto` module:

```js
// users.js

exports.getUserDetail = (request, response) => {
    let userData = {};
	db
		.doc(`/users/${request.user.username}`)
		.get()
		.then((doc) => {
			if (doc.exists) {
                userData.userCredentials = doc.data();
                return response.json(userData);
			}	
		})
		.catch((error) => {
			console.error(error);
			return response.status(500).json({ error: error.code });
		});
}
```

We are using the firebase **doc().get()** module to derive the user details. With this our **GET User Details API** is completed. Run the `firebase serve` command and go to the postman. Create a new request, select the method type: **GET**, and add the URL and body.

The request is protected so you’ll need to send the **bearer token** also. To send the bearer token, log in again if the token has expired.

```shell
URL: http://localhost:5000/todoapp-<app-id>/<region-name>/api/user
METHOD: GET
```

Hit the send request button in postman and you will get the following Output:

```json
{
   "userCredentials": {
       "phoneNumber": "........",
       "email": "........",
       "country": "........",
       "userId": "........",
       "username": "........",
       "createdAt": "........",
       "lastName": "........",
       "firstName": "........"
    }
}
```

### 5\. Update user details:

Now let’s add the functionality to update the user details. Go to the `index.js` and copy-paste the following code:

```js
// index.js

const {
    ..,
    updateUserDetails
} = require('./APIs/users')

app.post('/user', auth, updateUserDetails);
```

Now go to the `users.js` and add the `updateUserDetails` module below the existing `getUserDetails` :

```js
// users.js

exports.updateUserDetails = (request, response) => {
    let document = db.collection('users').doc(`${request.user.username}`);
    document.update(request.body)
    .then(()=> {
        response.json({message: 'Updated successfully'});
    })
    .catch((error) => {
        console.error(error);
        return response.status(500).json({ 
            message: "Cannot Update the value"
        });
    });
}
```

Here we are using the firebase **update** method. With this our **Update User Details API** is completed. Follow the same procedure for a request as with the Get User Details API above with one change. Add body in the request here and method as POST.

```shell
URL: http://localhost:5000/todoapp-<app-id>/<region-name>/api/user

METHOD: POST

Body : {
    // You can edit First Name, last Name and country
    // We will disable other Form Tags from our UI
}
```

Hit the send request button in postman and you will get the following Output:

```json
{
    "message": "Updated successfully"
}
```

### 6\. Securing Todo APIs:

To secure the Todo API so that only the chosen user can access it, we will make a few changes in our existing code. Firstly, we will update our `index.js` as follows:

```js
// index.js

// Todos
app.get('/todos', auth, getAllTodos);
app.get('/todo/:todoId', auth, getOneTodo);
app.post('/todo',auth, postOneTodo);
app.delete('/todo/:todoId',auth, deleteTodo);
app.put('/todo/:todoId',auth, editTodo);
```

We have updated all the **Todo routes** by adding `auth` so that all the API calls will require a token and can only be accessed by the particular user.

After that go to the `todos.js` under the **functions &gt; APIs** directory.

1. **Create Todo API:** Open the `todos.js` and under the **postOneTodo** method add the username key as follows:
    

```js
const newTodoItem = {
     ..,
     username: request.user.username,
     ..
}
```

2. **GET All Todos API:** Open the `todos.js` and under the **getAllTodos** method add the where clause as follows:
    

```js
db
.collection('todos')
.where('username', '==', request.user.username)
.orderBy('createdAt', 'desc')
```

Run the firebase serve and test our GET API. **Don’t forget to send the bearer token.** Here you will get a response error as follows:

```json
{   
    "error": 9
}
```

Go to the command line and you will see the following lines logged:

```shell
i  functions: Beginning execution of "api">  Error: 9 FAILED_PRECONDITION: The query requires an index. You can create it here: <URL>>      at callErrorFromStatus
```

Open this in the browser and click on create index.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/index.png align="left")

Once the index is built send the request again and you will get the following output:

```json
[
   {
      "todoId": "......",
      "title": "......",
      "username": "......",
      "body": "......",
      "createdAt": "2020-03-30T13:01:58.478Z"
   }
]
```

3. **Delete Todo API:** Open the `todos.js` and under the **deleteTodo** method add the following condition. Add this condition inside the **document.get().then()** query below the **!doc.exists** condition.
    

```js
..
if(doc.data().username !== request.user.username){
     return response.status(403).json({error:"UnAuthorized"})
}
```

### Directory structure up to now:

```shell
+-- firebase.json 
+-- functions
|   +-- API
|   +-- +-- todos.js 
|   +-- +-- users.js
|   +-- util
|   +-- +-- admin.js
|   +-- +-- auth.js
|   +-- +-- validators.js
|   +-- index.js
|   +-- node_modules
|   +-- package-lock.json
|   +-- package.json
|   +-- .gitignore
```

With this we have completed our API backend. Take a break, have a coffee, and after that we will start building the front end of our application

## Section 3: User Dashboard

In this section\*\*,\*\* we are going to develop these components:

1. **Configure ReactJS and Material UI.**
    
2. **Building Login and SignUp Form.**
    
3. **Building Account Section.**
    

The User Dashboard code implemented in this section can be found at this [commit](https://github.com/Sharvin26/TodoApp/tree/2b207786651167c1ed5327c2c8583e97080abb54/view).

### 1\. Configure ReactJS and Material UI:

We will use the create-react-app template. It gives us a fundamental structure for developing the application. To install it, use the following command:

```shell
npm install -g create-react-app
```

Go to the root folder of the project where the functions directory is present. Initialize our front end application using the following command:

```shell
create-react-app view
```

Remember to use version **v16.13.1** of the ReactJS library\_.\_

Once the installation is completed then you'll see the following in your command line logs:

```shell
cd view
  npm start
Happy hacking!
```

With this, we have configured our React application. You’ll get the following directory structure:

```shell
+-- firebase.json 
+-- functions { This Directory consists our API logic }
+-- view { This Directory consists our FrontEnd Compoenents }
+-- .firebaserc
+-- .gitignore
```

Now run the application using the command `npm start` . Go to the browser on `[http://localhost:3000/](http://localhost:3000/)` and you’ll see the following output:

![Image](https://www.freecodecamp.org/news/content/images/2020/04/React1.png align="left")

Now we will remove all the unnecessary components. Go to the view directory and then remove all the files which have **\[ Remove \]** in front of them. **For this, refer to the directory tree structure below.**

```shell
+-- README.md [ Remove ]
+-- package-lock.json
+-- package.json
+-- node_modules
+-- .gitignore
+-- public
|   +-- favicon.ico [ Remove ]
|   +-- index.html
|   +-- logo192.png [ Remove ]
|   +-- logo512.png [ Remove ]
|   +-- manifest.json
|   +-- robots.txt
+-- src
|   +-- App.css
|   +-- App.test.js
|   +-- index.js
|   +-- serviceWorker.js
|   +-- App.js
|   +-- index.css [ Remove ]
|   +-- logo.svg [ Remove ]
|   +-- setupTests.js
```

Go to `index.html` under the public directory and remove the following lines:

```html
<link rel="icon" href="%PUBLIC_URL%/favicon.ico" />
<link rel="apple-touch-icon" href="%PUBLIC_URL%/logo192.png" />
<link rel="manifest" href="%PUBLIC_URL%/manifest.json" />
```

Now go to the `App.js` under the src directory and replace the old code with the following code:

```js
import React from 'react';
function App() {
  return (
    <div>
    </div>
  );
}
export default App;
```

Go to the `index.js` and remove the following import:

```python
import './index.css'
```

I have not deleted the `App.css` nor I am using it in this application. But if you want to delete or use it you are free to do that.

Go to the browser on `[http://localhost:3000/](http://localhost:3000/)` and you’ll get a blank screen output.

To install Material UI go to the view directory and copy-paste this command in the terminal:

```shell
npm install @material-ui/core
```

Remember to use version **v4.9.8** of the Material UI library.

### 2\. Login Form:

To develop the login form go to `App.js`. At the top of `App.js` add the following imports:

```js
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import login from './pages/login';
```

We are using **Switch** and **Route** to assign routes for our TodoApp. Right now we will add only the **/login** route and assign a login component to it.

```html
// App.js

<Router>
    <div>
       <Switch>
           <Route exact path="/login" component={login}/>
       </Switch>
    </div>
</Router>
```

Create a **pages** directory under the existing **view** directory and a file named `login.js` under the **pages** directory.

We will import Material UI components and the Axios package in the `login.js`:

```js
// login.js

// Material UI components
import React, { Component } from 'react';
import Avatar from '@material-ui/core/Avatar';
import Button from '@material-ui/core/Button';
import CssBaseline from '@material-ui/core/CssBaseline';
import TextField from '@material-ui/core/TextField';
import Link from '@material-ui/core/Link';
import Grid from '@material-ui/core/Grid';
import LockOutlinedIcon from '@material-ui/icons/LockOutlined';
import Typography from '@material-ui/core/Typography';
import withStyles from '@material-ui/core/styles/withStyles';
import Container from '@material-ui/core/Container';
import CircularProgress from '@material-ui/core/CircularProgress';

import axios from 'axios';
```

We will add the following styles to our login page:

```js
// login.js

const styles = (theme) => ({
	paper: {
		marginTop: theme.spacing(8),
		display: 'flex',
		flexDirection: 'column',
		alignItems: 'center'
	},
	avatar: {
		margin: theme.spacing(1),
		backgroundColor: theme.palette.secondary.main
	},
	form: {
		width: '100%',
		marginTop: theme.spacing(1)
	},
	submit: {
		margin: theme.spacing(3, 0, 2)
	},
	customError: {
		color: 'red',
		fontSize: '0.8rem',
		marginTop: 10
	},
	progess: {
		position: 'absolute'
	}
});
```

We will create a class named login which has a form and submit handler inside it.

```js
// login.js

class login extends Component {
	constructor(props) {
		super(props);

		this.state = {
			email: '',
			password: '',
			errors: [],
			loading: false
		};
	}

	componentWillReceiveProps(nextProps) {
		if (nextProps.UI.errors) {
			this.setState({
				errors: nextProps.UI.errors
			});
		}
	}

	handleChange = (event) => {
		this.setState({
			[event.target.name]: event.target.value
		});
	};

	handleSubmit = (event) => {
		event.preventDefault();
		this.setState({ loading: true });
		const userData = {
			email: this.state.email,
			password: this.state.password
		};
		axios
			.post('/login', userData)
			.then((response) => {
				localStorage.setItem('AuthToken', `Bearer ${response.data.token}`);
				this.setState({ 
					loading: false,
				});		
				this.props.history.push('/');
			})
			.catch((error) => {				
				this.setState({
					errors: error.response.data,
					loading: false
				});
			});
	};

	render() {
		const { classes } = this.props;
		const { errors, loading } = this.state;
		return (
			<Container component="main" maxWidth="xs">
				<CssBaseline />
				<div className={classes.paper}>
					<Avatar className={classes.avatar}>
						<LockOutlinedIcon />
					</Avatar>
					<Typography component="h1" variant="h5">
						Login
					</Typography>
					<form className={classes.form} noValidate>
						<TextField
							variant="outlined"
							margin="normal"
							required
							fullWidth
							id="email"
							label="Email Address"
							name="email"
							autoComplete="email"
							autoFocus
							helperText={errors.email}
							error={errors.email ? true : false}
							onChange={this.handleChange}
						/>
						<TextField
							variant="outlined"
							margin="normal"
							required
							fullWidth
							name="password"
							label="Password"
							type="password"
							id="password"
							autoComplete="current-password"
							helperText={errors.password}
							error={errors.password ? true : false}
							onChange={this.handleChange}
						/>
						<Button
							type="submit"
							fullWidth
							variant="contained"
							color="primary"
							className={classes.submit}
							onClick={this.handleSubmit}
							disabled={loading || !this.state.email || !this.state.password}
						>
							Sign In
							{loading && <CircularProgress size={30} className={classes.progess} />}
						</Button>
						<Grid container>
							<Grid item>
								<Link href="signup" variant="body2">
									{"Don't have an account? Sign Up"}
								</Link>
							</Grid>
						</Grid>
						{errors.general && (
							<Typography variant="body2" className={classes.customError}>
								{errors.general}
							</Typography>
						)}
					</form>
				</div>
			</Container>
		);
	}
}
```

At the end of this file add the following export:

```js
export default withStyles(styles)(login);
```

Add our firebase functions URL to **view &gt; package.json** as follows:

> Remember: Add a key named **proxy** below the existing browserslist JSON object

```json
"proxy": "https://<region-name>-todoapp-<id>.cloudfunctions.net/api"
```

Install the **Axios** and **material icon** package using the following commands:

```shell
// Axios command:
npm i axios
// Material Icons:
npm install @material-ui/icons
```

We have added a login route in `App.js`. In the `login.js` we have created a class component that handles the state, sends the post request to the login API using the Axios package. If the request is successful then we store the token. If we get errors in the response we simply render them on the UI.

Go to the browser at `[http://localhost:3000/login](http://localhost:3000/login)` and you’ll see the following Login UI.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/LoginPage.png align="left")

*Login Page*

Try filling wrong credentials or sending an empty request and you will get the errors. Send a valid request. Go to the **Developer console &gt; Application**. You will see that users token is store in the Local storage. Once the Login is successful we will be routed back to the Home page.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/loginDev.png align="left")

*Google Chrome Developer Console*

### 3\. Signup Form:

To develop the Signup form go to `App.js` and update the existing `Route` component with the line below:

```js
// App.js

<Route exact path="/signup" component={signup}/>
```

Don’t forget to import:

```js
// App.js

import signup from './pages/signup';
```

Create a file named `signup.js` under the **pages directory**.

Inside the signup.js we will import the Material UI and Axios package:

```js
// signup.js

import React, { Component } from 'react';
import Avatar from '@material-ui/core/Avatar';
import Button from '@material-ui/core/Button';
import CssBaseline from '@material-ui/core/CssBaseline';
import TextField from '@material-ui/core/TextField';
import Link from '@material-ui/core/Link';
import Grid from '@material-ui/core/Grid';
import LockOutlinedIcon from '@material-ui/icons/LockOutlined';
import Typography from '@material-ui/core/Typography';
import Container from '@material-ui/core/Container';
import withStyles from '@material-ui/core/styles/withStyles';
import CircularProgress from '@material-ui/core/CircularProgress';

import axios from 'axios';
```

We will add the following styles to our signup page:

```js
// signup.js


const styles = (theme) => ({
	paper: {
		marginTop: theme.spacing(8),
		display: 'flex',
		flexDirection: 'column',
		alignItems: 'center'
	},
	avatar: {
		margin: theme.spacing(1),
		backgroundColor: theme.palette.secondary.main
	},
	form: {
		width: '100%', // Fix IE 11 issue.
		marginTop: theme.spacing(3)
	},
	submit: {
		margin: theme.spacing(3, 0, 2)
	},
	progess: {
		position: 'absolute'
	}
});
```

We will create a class named signup which has a form and submit handler inside it.

```js
// signup.js

class signup extends Component {
	constructor(props) {
		super(props);

		this.state = {
			firstName: '',
			lastName: '',
			phoneNumber: '',
			country: '',
			username: '',
			email: '',
			password: '',
			confirmPassword: '',
			errors: [],
			loading: false
		};
	}

	componentWillReceiveProps(nextProps) {
		if (nextProps.UI.errors) {
			this.setState({
				errors: nextProps.UI.errors
			});
		}
	}

	handleChange = (event) => {
		this.setState({
			[event.target.name]: event.target.value
		});
	};

	handleSubmit = (event) => {
		event.preventDefault();
		this.setState({ loading: true });
		const newUserData = {
			firstName: this.state.firstName,
			lastName: this.state.lastName,
			phoneNumber: this.state.phoneNumber,
			country: this.state.country,
			username: this.state.username,
			email: this.state.email,
			password: this.state.password,
			confirmPassword: this.state.confirmPassword
		};
		axios
			.post('/signup', newUserData)
			.then((response) => {
				localStorage.setItem('AuthToken', `${response.data.token}`);
				this.setState({ 
					loading: false,
				});	
				this.props.history.push('/');
			})
			.catch((error) => {
				this.setState({
					errors: error.response.data,
					loading: false
				});
			});
	};

	render() {
		const { classes } = this.props;
		const { errors, loading } = this.state;
		return (
			<Container component="main" maxWidth="xs">
				<CssBaseline />
				<div className={classes.paper}>
					<Avatar className={classes.avatar}>
						<LockOutlinedIcon />
					</Avatar>
					<Typography component="h1" variant="h5">
						Sign up
					</Typography>
					<form className={classes.form} noValidate>
						<Grid container spacing={2}>
							<Grid item xs={12} sm={6}>
								<TextField
									variant="outlined"
									required
									fullWidth
									id="firstName"
									label="First Name"
									name="firstName"
									autoComplete="firstName"
									helperText={errors.firstName}
									error={errors.firstName ? true : false}
									onChange={this.handleChange}
								/>
							</Grid>
							<Grid item xs={12} sm={6}>
								<TextField
									variant="outlined"
									required
									fullWidth
									id="lastName"
									label="Last Name"
									name="lastName"
									autoComplete="lastName"
									helperText={errors.lastName}
									error={errors.lastName ? true : false}
									onChange={this.handleChange}
								/>
							</Grid>

							<Grid item xs={12} sm={6}>
								<TextField
									variant="outlined"
									required
									fullWidth
									id="username"
									label="User Name"
									name="username"
									autoComplete="username"
									helperText={errors.username}
									error={errors.username ? true : false}
									onChange={this.handleChange}
								/>
							</Grid>

							<Grid item xs={12} sm={6}>
								<TextField
									variant="outlined"
									required
									fullWidth
									id="phoneNumber"
									label="Phone Number"
									name="phoneNumber"
									autoComplete="phoneNumber"
									pattern="[7-9]{1}[0-9]{9}"
									helperText={errors.phoneNumber}
									error={errors.phoneNumber ? true : false}
									onChange={this.handleChange}
								/>
							</Grid>

							<Grid item xs={12}>
								<TextField
									variant="outlined"
									required
									fullWidth
									id="email"
									label="Email Address"
									name="email"
									autoComplete="email"
									helperText={errors.email}
									error={errors.email ? true : false}
									onChange={this.handleChange}
								/>
							</Grid>

							<Grid item xs={12}>
								<TextField
									variant="outlined"
									required
									fullWidth
									id="country"
									label="Country"
									name="country"
									autoComplete="country"
									helperText={errors.country}
									error={errors.country ? true : false}
									onChange={this.handleChange}
								/>
							</Grid>

							<Grid item xs={12}>
								<TextField
									variant="outlined"
									required
									fullWidth
									name="password"
									label="Password"
									type="password"
									id="password"
									autoComplete="current-password"
									helperText={errors.password}
									error={errors.password ? true : false}
									onChange={this.handleChange}
								/>
							</Grid>
							<Grid item xs={12}>
								<TextField
									variant="outlined"
									required
									fullWidth
									name="confirmPassword"
									label="Confirm Password"
									type="password"
									id="confirmPassword"
									autoComplete="current-password"
									onChange={this.handleChange}
								/>
							</Grid>
						</Grid>
						<Button
							type="submit"
							fullWidth
							variant="contained"
							color="primary"
							className={classes.submit}
							onClick={this.handleSubmit}
                            disabled={loading || 
                                !this.state.email || 
                                !this.state.password ||
                                !this.state.firstName || 
                                !this.state.lastName ||
                                !this.state.country || 
                                !this.state.username || 
                                !this.state.phoneNumber}
						>
							Sign Up
							{loading && <CircularProgress size={30} className={classes.progess} />}
						</Button>
						<Grid container justify="flex-end">
							<Grid item>
								<Link href="login" variant="body2">
									Already have an account? Sign in
								</Link>
							</Grid>
						</Grid>
					</form>
				</div>
			</Container>
		);
	}
}
```

At the end of this file add the following export:

```js
export default withStyles(styles)(signup);
```

The logic for the Signup component is the same as the login component. Go to the browser at `[http://localhost:3000/signup](http://localhost:3000/signup)` and you’ll see the following Signup UI. Once the Signup is successful we will be routed back to the Home page.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/SignupPage.png align="left")

*Sign up Form*

Try filling wrong credentials or sending an empty request and you will get the errors. Send a valid request. Go to the **Developer console &gt; Application**. You will see that users token is store in the Local storage.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/DevConsoleSignup.png align="left")

*Chrome Developer Console*

### 4\. Account Section:

To build the account page we will need to first create our **Home page** from where we will load the **account section**. Go to the `App.js` and update the following route:

```js
// App.js

<Route exact path="/" component={home}/>
```

Don't forget the import:

```js
// App.js

import home from './pages/home';
```

Create a new file named `home.js` . This file will be the index of our application. The Account and Todo sections both load on this page based on the button click.

Import the Material UI packages, Axios package, our custom Account, todo components, and auth middleware.

```js
// home.js

import React, { Component } from 'react';
import axios from 'axios';

import Account from '../components/account';
import Todo from '../components/todo';

import Drawer from '@material-ui/core/Drawer';
import AppBar from '@material-ui/core/AppBar';
import CssBaseline from '@material-ui/core/CssBaseline';
import Toolbar from '@material-ui/core/Toolbar';
import List from '@material-ui/core/List';
import Typography from '@material-ui/core/Typography';
import Divider from '@material-ui/core/Divider';
import ListItem from '@material-ui/core/ListItem';
import ListItemIcon from '@material-ui/core/ListItemIcon';
import ListItemText from '@material-ui/core/ListItemText';
import withStyles from '@material-ui/core/styles/withStyles';
import AccountBoxIcon from '@material-ui/icons/AccountBox';
import NotesIcon from '@material-ui/icons/Notes';
import Avatar from '@material-ui/core/avatar';
import ExitToAppIcon from '@material-ui/icons/ExitToApp';
import CircularProgress from '@material-ui/core/CircularProgress';

import { authMiddleWare } from '../util/auth'
```

We will set our drawerWidth as follows:

```js
const drawerWidth = 240;
```

We will add the following style to our Home page:

```js
const styles = (theme) => ({
	root: {
		display: 'flex'
	},
	appBar: {
		zIndex: theme.zIndex.drawer + 1
	},
	drawer: {
		width: drawerWidth,
		flexShrink: 0
	},
	drawerPaper: {
		width: drawerWidth
	},
	content: {
		flexGrow: 1,
		padding: theme.spacing(3)
	},
	avatar: {
		height: 110,
		width: 100,
		flexShrink: 0,
		flexGrow: 0,
		marginTop: 20
	},
	uiProgess: {
		position: 'fixed',
		zIndex: '1000',
		height: '31px',
		width: '31px',
		left: '50%',
		top: '35%'
	},
	toolbar: theme.mixins.toolbar
});
```

We will create a class named home. This class will have an API call to get the User's profile picture, First name and Last name. Also it will have logic to choose which component to display, either Todo or Account:

```js
class home extends Component {
	state = {
		render: false
	};

	loadAccountPage = (event) => {
		this.setState({ render: true });
	};

	loadTodoPage = (event) => {
		this.setState({ render: false });
	};

	logoutHandler = (event) => {
		localStorage.removeItem('AuthToken');
		this.props.history.push('/login');
	};

	constructor(props) {
		super(props);

		this.state = {
			firstName: '',
			lastName: '',
			profilePicture: '',
			uiLoading: true,
			imageLoading: false
		};
	}

	componentWillMount = () => {
		authMiddleWare(this.props.history);
		const authToken = localStorage.getItem('AuthToken');
		axios.defaults.headers.common = { Authorization: `${authToken}` };
		axios
			.get('/user')
			.then((response) => {
				console.log(response.data);
				this.setState({
					firstName: response.data.userCredentials.firstName,
					lastName: response.data.userCredentials.lastName,
					email: response.data.userCredentials.email,
					phoneNumber: response.data.userCredentials.phoneNumber,
					country: response.data.userCredentials.country,
					username: response.data.userCredentials.username,
					uiLoading: false,
					profilePicture: response.data.userCredentials.imageUrl
				});
			})
			.catch((error) => {
				if(error.response.status === 403) {
					this.props.history.push('/login')
				}
				console.log(error);
				this.setState({ errorMsg: 'Error in retrieving the data' });
			});
	};

	render() {
		const { classes } = this.props;		
		if (this.state.uiLoading === true) {
			return (
				<div className={classes.root}>
					{this.state.uiLoading && <CircularProgress size={150} className={classes.uiProgess} />}
				</div>
			);
		} else {
			return (
				<div className={classes.root}>
					<CssBaseline />
					<AppBar position="fixed" className={classes.appBar}>
						<Toolbar>
							<Typography variant="h6" noWrap>
								TodoApp
							</Typography>
						</Toolbar>
					</AppBar>
					<Drawer
						className={classes.drawer}
						variant="permanent"
						classes={{
							paper: classes.drawerPaper
						}}
					>
						<div className={classes.toolbar} />
						<Divider />
						<center>
							<Avatar src={this.state.profilePicture} className={classes.avatar} />
							<p>
								{' '}
								{this.state.firstName} {this.state.lastName}
							</p>
						</center>
						<Divider />
						<List>
							<ListItem button key="Todo" onClick={this.loadTodoPage}>
								<ListItemIcon>
									{' '}
									<NotesIcon />{' '}
								</ListItemIcon>
								<ListItemText primary="Todo" />
							</ListItem>

							<ListItem button key="Account" onClick={this.loadAccountPage}>
								<ListItemIcon>
									{' '}
									<AccountBoxIcon />{' '}
								</ListItemIcon>
								<ListItemText primary="Account" />
							</ListItem>

							<ListItem button key="Logout" onClick={this.logoutHandler}>
								<ListItemIcon>
									{' '}
									<ExitToAppIcon />{' '}
								</ListItemIcon>
								<ListItemText primary="Logout" />
							</ListItem>
						</List>
					</Drawer>

					<div>{this.state.render ? <Account /> : <Todo />}</div>
				</div>
			);
		}
	}
}
```

Here in the code, you will see that `authMiddleWare(this.props.history);` is used. This middleware checks if the authToken is null. If yes then it will push the user back to the `login.js`. This is added so that our user cannot access the `/` route without Signup or log in. At the end of this file add the following export:

```js
export default withStyles(styles)(home);
```

Now are you wondering what this code from `home.js` does?

```python
<div>{this.state.render ? <Account /> : <Todo />}</div>
```

It is checking the render state which we are setting on the button click. Let's create the component directory, and under that directory create two files: `account.js` and `todo.js`.

Let’s create a directory named **util** and file named `auth.js` under that directory. Copy-paste the following code under `auth.js` :

```js
export const authMiddleWare = (history) => {
    const authToken = localStorage.getItem('AuthToken');
    if(authToken === null){
        history.push('/login')
    }
}
```

For time being inside the `todo.js` file we will just write a class which renders the text **Hello I am todo**. We will be working on our todos in the next section:

```js
import React, { Component } from 'react'

import withStyles from '@material-ui/core/styles/withStyles';
import Typography from '@material-ui/core/Typography';

const styles = ((theme) => ({
    content: {
        flexGrow: 1,
        padding: theme.spacing(3),
    },
    toolbar: theme.mixins.toolbar,
    })
);

class todo extends Component {
    render() {
        const { classes } = this.props;
        return (
            <main className={classes.content}>
            <div className={classes.toolbar} />
            <Typography paragraph>
                Hello I am todo
            </Typography>
            </main>
        )
    }
}

export default (withStyles(styles)(todo));
```

Now it's time for the account section. Import the Material UI, clsx, axios and authmiddleWare utility in our `account.js`.

```js
// account.js

import React, { Component } from 'react';

import withStyles from '@material-ui/core/styles/withStyles';
import Typography from '@material-ui/core/Typography';
import CircularProgress from '@material-ui/core/CircularProgress';
import CloudUploadIcon from '@material-ui/icons/CloudUpload';
import { Card, CardActions, CardContent, Divider, Button, Grid, TextField } from '@material-ui/core';

import clsx from 'clsx';

import axios from 'axios';
import { authMiddleWare } from '../util/auth';
```

We will add the following styling to our Account page:

```js
// account.js

const styles = (theme) => ({
	content: {
		flexGrow: 1,
		padding: theme.spacing(3)
	},
	toolbar: theme.mixins.toolbar,
	root: {},
	details: {
		display: 'flex'
	},
	avatar: {
		height: 110,
		width: 100,
		flexShrink: 0,
		flexGrow: 0
	},
	locationText: {
		paddingLeft: '15px'
	},
	buttonProperty: {
		position: 'absolute',
		top: '50%'
	},
	uiProgess: {
		position: 'fixed',
		zIndex: '1000',
		height: '31px',
		width: '31px',
		left: '50%',
		top: '35%'
	},
	progess: {
		position: 'absolute'
	},
	uploadButton: {
		marginLeft: '8px',
		margin: theme.spacing(1)
	},
	customError: {
		color: 'red',
		fontSize: '0.8rem',
		marginTop: 10
	},
	submitButton: {
		marginTop: '10px'
	}
});
```

We will create a class component named account. For the time being just copy-paste the following code:

```js
// account.js

class account extends Component {
	constructor(props) {
		super(props);

		this.state = {
			firstName: '',
			lastName: '',
			email: '',
			phoneNumber: '',
			username: '',
			country: '',
			profilePicture: '',
			uiLoading: true,
			buttonLoading: false,
			imageError: ''
		};
	}

	componentWillMount = () => {
		authMiddleWare(this.props.history);
		const authToken = localStorage.getItem('AuthToken');
		axios.defaults.headers.common = { Authorization: `${authToken}` };
		axios
			.get('/user')
			.then((response) => {
				console.log(response.data);
				this.setState({
					firstName: response.data.userCredentials.firstName,
					lastName: response.data.userCredentials.lastName,
					email: response.data.userCredentials.email,
					phoneNumber: response.data.userCredentials.phoneNumber,
					country: response.data.userCredentials.country,
					username: response.data.userCredentials.username,
					uiLoading: false
				});
			})
			.catch((error) => {
				if (error.response.status === 403) {
					this.props.history.push('/login');
				}
				console.log(error);
				this.setState({ errorMsg: 'Error in retrieving the data' });
			});
	};

	handleChange = (event) => {
		this.setState({
			[event.target.name]: event.target.value
		});
	};

	handleImageChange = (event) => {
		this.setState({
			image: event.target.files[0]
		});
	};

	profilePictureHandler = (event) => {
		event.preventDefault();
		this.setState({
			uiLoading: true
		});
		authMiddleWare(this.props.history);
		const authToken = localStorage.getItem('AuthToken');
		let form_data = new FormData();
		form_data.append('image', this.state.image);
		form_data.append('content', this.state.content);
		axios.defaults.headers.common = { Authorization: `${authToken}` };
		axios
			.post('/user/image', form_data, {
				headers: {
					'content-type': 'multipart/form-data'
				}
			})
			.then(() => {
				window.location.reload();
			})
			.catch((error) => {
				if (error.response.status === 403) {
					this.props.history.push('/login');
				}
				console.log(error);
				this.setState({
					uiLoading: false,
					imageError: 'Error in posting the data'
				});
			});
	};

	updateFormValues = (event) => {
		event.preventDefault();
		this.setState({ buttonLoading: true });
		authMiddleWare(this.props.history);
		const authToken = localStorage.getItem('AuthToken');
		axios.defaults.headers.common = { Authorization: `${authToken}` };
		const formRequest = {
			firstName: this.state.firstName,
			lastName: this.state.lastName,
			country: this.state.country
		};
		axios
			.post('/user', formRequest)
			.then(() => {
				this.setState({ buttonLoading: false });
			})
			.catch((error) => {
				if (error.response.status === 403) {
					this.props.history.push('/login');
				}
				console.log(error);
				this.setState({
					buttonLoading: false
				});
			});
	};

	render() {
		const { classes, ...rest } = this.props;
		if (this.state.uiLoading === true) {
			return (
				<main className={classes.content}>
					<div className={classes.toolbar} />
					{this.state.uiLoading && <CircularProgress size={150} className={classes.uiProgess} />}
				</main>
			);
		} else {
			return (
				<main className={classes.content}>
					<div className={classes.toolbar} />
					<Card {...rest} className={clsx(classes.root, classes)}>
						<CardContent>
							<div className={classes.details}>
								<div>
									<Typography className={classes.locationText} gutterBottom variant="h4">
										{this.state.firstName} {this.state.lastName}
									</Typography>
									<Button
										variant="outlined"
										color="primary"
										type="submit"
										size="small"
										startIcon={<CloudUploadIcon />}
										className={classes.uploadButton}
										onClick={this.profilePictureHandler}
									>
										Upload Photo
									</Button>
									<input type="file" onChange={this.handleImageChange} />

									{this.state.imageError ? (
										<div className={classes.customError}>
											{' '}
											Wrong Image Format || Supported Format are PNG and JPG
										</div>
									) : (
										false
									)}
								</div>
							</div>
							<div className={classes.progress} />
						</CardContent>
						<Divider />
					</Card>

					<br />
					<Card {...rest} className={clsx(classes.root, classes)}>
						<form autoComplete="off" noValidate>
							<Divider />
							<CardContent>
								<Grid container spacing={3}>
									<Grid item md={6} xs={12}>
										<TextField
											fullWidth
											label="First name"
											margin="dense"
											name="firstName"
											variant="outlined"
											value={this.state.firstName}
											onChange={this.handleChange}
										/>
									</Grid>
									<Grid item md={6} xs={12}>
										<TextField
											fullWidth
											label="Last name"
											margin="dense"
											name="lastName"
											variant="outlined"
											value={this.state.lastName}
											onChange={this.handleChange}
										/>
									</Grid>
									<Grid item md={6} xs={12}>
										<TextField
											fullWidth
											label="Email"
											margin="dense"
											name="email"
											variant="outlined"
											disabled={true}
											value={this.state.email}
											onChange={this.handleChange}
										/>
									</Grid>
									<Grid item md={6} xs={12}>
										<TextField
											fullWidth
											label="Phone Number"
											margin="dense"
											name="phone"
											type="number"
											variant="outlined"
											disabled={true}
											value={this.state.phoneNumber}
											onChange={this.handleChange}
										/>
									</Grid>
									<Grid item md={6} xs={12}>
										<TextField
											fullWidth
											label="User Name"
											margin="dense"
											name="userHandle"
											disabled={true}
											variant="outlined"
											value={this.state.username}
											onChange={this.handleChange}
										/>
									</Grid>
									<Grid item md={6} xs={12}>
										<TextField
											fullWidth
											label="Country"
											margin="dense"
											name="country"
											variant="outlined"
											value={this.state.country}
											onChange={this.handleChange}
										/>
									</Grid>
								</Grid>
							</CardContent>
							<Divider />
							<CardActions />
						</form>
					</Card>
					<Button
						color="primary"
						variant="contained"
						type="submit"
						className={classes.submitButton}
						onClick={this.updateFormValues}
						disabled={
							this.state.buttonLoading ||
							!this.state.firstName ||
							!this.state.lastName ||
							!this.state.country
						}
					>
						Save details
						{this.state.buttonLoading && <CircularProgress size={30} className={classes.progess} />}
					</Button>
				</main>
			);
		}
	}
}
```

At the end of this file add the following export:

```js
export default withStyles(styles)(account);
```

In `account.js` there are lot of components used. First let's see how our application looks. After that I'll explain all the components that are used and why they are used.

Go to the browser, and if your token is expired it will redirect you to the `login` page. Add your details and log in again. Once you've done that, go to the Account tab and you will find the following UI:

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-88.png align="left")

*Account Section*

There are 3 handlers in the Account Section:

1. **componentWillMount**: This is React's inbuilt lifecycle method. We are using it to load the data before the render lifecycle and update our state values.
    
2. **ProfilePictureUpdate:** This is our custom handler that we are using so that when our user clicks on the Upload Photo button then it will send the data to a server and reload the page to show the user's new Profile Picture.
    
3. **updateFormValues:** This is also our custom handler to update the User's details. Here, the user can update their first name, last name, and country. We are not allowing email and username updates because our backend logic depends on those keys.
    

Other than these 3 handlers it is a form page with styling on top of it. Here is the directory structure up to this point inside the view folder:

```shell
+-- public 
+-- src
|   +-- components
|   +-- +-- todo.js
|   +-- +-- account.js
|   +-- pages
|   +-- +-- home.js
|   +-- +-- login.js
|   +-- +-- signup.js
|   +-- util
|   +-- +-- auth.js 
|   +-- README.md
|   +-- package-lock.json
|   +-- package.json
|   +-- .gitignore
```

With this we have completed our Account Dashboard. Now go have a coffee, take a break and in the next section, we will build the Todo Dashboard.

## Section 4: Todo Dashboard

In this section\*\*,\*\* we are going to develop the UI for these features of the Todos Dashboard:

1. **Add a Todo:**
    
2. **Get all todos:**
    
3. **Delete a todo**
    
4. **Edit a todo**
    
5. **Get a todo**
    
6. **Applying Theme**
    

The Todo Dashboard code implemented in this section can be found at this [commit](https://github.com/Sharvin26/TodoApp/tree/3799980aa13eeb8d313e17d83aa3032748aedb00/view).

Go to `todos.js` under the **components** directory. Add the following imports to the existing imports:

```js
import Button from '@material-ui/core/Button';
import Dialog from '@material-ui/core/Dialog';
import AddCircleIcon from '@material-ui/icons/AddCircle';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import IconButton from '@material-ui/core/IconButton';
import CloseIcon from '@material-ui/icons/Close';
import Slide from '@material-ui/core/Slide';
import TextField from '@material-ui/core/TextField';
import Grid from '@material-ui/core/Grid';
import Card from '@material-ui/core/Card';
import CardActions from '@material-ui/core/CardActions';
import CircularProgress from '@material-ui/core/CircularProgress';
import CardContent from '@material-ui/core/CardContent';
import MuiDialogTitle from '@material-ui/core/DialogTitle';
import MuiDialogContent from '@material-ui/core/DialogContent';

import axios from 'axios';
import dayjs from 'dayjs';
import relativeTime from 'dayjs/plugin/relativeTime';
import { authMiddleWare } from '../util/auth';
```

We also need to add the following CSS elements in the existing style components:

```js
const styles = (theme) => ({
	.., // Existing CSS elements
	title: {
		marginLeft: theme.spacing(2),
		flex: 1
	},
	submitButton: {
		display: 'block',
		color: 'white',
		textAlign: 'center',
		position: 'absolute',
		top: 14,
		right: 10
	},
	floatingButton: {
		position: 'fixed',
		bottom: 0,
		right: 0
	},
	form: {
		width: '98%',
		marginLeft: 13,
		marginTop: theme.spacing(3)
	},
	toolbar: theme.mixins.toolbar,
	root: {
		minWidth: 470
	},
	bullet: {
		display: 'inline-block',
		margin: '0 2px',
		transform: 'scale(0.8)'
	},
	pos: {
		marginBottom: 12
	},
	uiProgess: {
		position: 'fixed',
		zIndex: '1000',
		height: '31px',
		width: '31px',
		left: '50%',
		top: '35%'
	},
	dialogeStyle: {
		maxWidth: '50%'
	},
	viewRoot: {
		margin: 0,
		padding: theme.spacing(2)
	},
	closeButton: {
		position: 'absolute',
		right: theme.spacing(1),
		top: theme.spacing(1),
		color: theme.palette.grey[500]
	}
});
```

We will add the transition for the pop up dialogue box:

```js
const Transition = React.forwardRef(function Transition(props, ref) {
	return <Slide direction="up" ref={ref} {...props} />;
});
```

Remove the existing todo class and copy-paste the following class:

```js
class todo extends Component {
	constructor(props) {
		super(props);

		this.state = {
			todos: '',
			title: '',
			body: '',
			todoId: '',
			errors: [],
			open: false,
			uiLoading: true,
			buttonType: '',
			viewOpen: false
		};

		this.deleteTodoHandler = this.deleteTodoHandler.bind(this);
		this.handleEditClickOpen = this.handleEditClickOpen.bind(this);
		this.handleViewOpen = this.handleViewOpen.bind(this);
	}

	handleChange = (event) => {
		this.setState({
			[event.target.name]: event.target.value
		});
	};

	componentWillMount = () => {
		authMiddleWare(this.props.history);
		const authToken = localStorage.getItem('AuthToken');
		axios.defaults.headers.common = { Authorization: `${authToken}` };
		axios
			.get('/todos')
			.then((response) => {
				this.setState({
					todos: response.data,
					uiLoading: false
				});
			})
			.catch((err) => {
				console.log(err);
			});
	};

	deleteTodoHandler(data) {
		authMiddleWare(this.props.history);
		const authToken = localStorage.getItem('AuthToken');
		axios.defaults.headers.common = { Authorization: `${authToken}` };
		let todoId = data.todo.todoId;
		axios
			.delete(`todo/${todoId}`)
			.then(() => {
				window.location.reload();
			})
			.catch((err) => {
				console.log(err);
			});
	}

	handleEditClickOpen(data) {
		this.setState({
			title: data.todo.title,
			body: data.todo.body,
			todoId: data.todo.todoId,
			buttonType: 'Edit',
			open: true
		});
	}

	handleViewOpen(data) {
		this.setState({
			title: data.todo.title,
			body: data.todo.body,
			viewOpen: true
		});
	}

	render() {
		const DialogTitle = withStyles(styles)((props) => {
			const { children, classes, onClose, ...other } = props;
			return (
				<MuiDialogTitle disableTypography className={classes.root} {...other}>
					<Typography variant="h6">{children}</Typography>
					{onClose ? (
						<IconButton aria-label="close" className={classes.closeButton} onClick={onClose}>
							<CloseIcon />
						</IconButton>
					) : null}
				</MuiDialogTitle>
			);
		});

		const DialogContent = withStyles((theme) => ({
			viewRoot: {
				padding: theme.spacing(2)
			}
		}))(MuiDialogContent);

		dayjs.extend(relativeTime);
		const { classes } = this.props;
		const { open, errors, viewOpen } = this.state;

		const handleClickOpen = () => {
			this.setState({
				todoId: '',
				title: '',
				body: '',
				buttonType: '',
				open: true
			});
		};

		const handleSubmit = (event) => {
			authMiddleWare(this.props.history);
			event.preventDefault();
			const userTodo = {
				title: this.state.title,
				body: this.state.body
			};
			let options = {};
			if (this.state.buttonType === 'Edit') {
				options = {
					url: `/todo/${this.state.todoId}`,
					method: 'put',
					data: userTodo
				};
			} else {
				options = {
					url: '/todo',
					method: 'post',
					data: userTodo
				};
			}
			const authToken = localStorage.getItem('AuthToken');
			axios.defaults.headers.common = { Authorization: `${authToken}` };
			axios(options)
				.then(() => {
					this.setState({ open: false });
					window.location.reload();
				})
				.catch((error) => {
					this.setState({ open: true, errors: error.response.data });
					console.log(error);
				});
		};

		const handleViewClose = () => {
			this.setState({ viewOpen: false });
		};

		const handleClose = (event) => {
			this.setState({ open: false });
		};

		if (this.state.uiLoading === true) {
			return (
				<main className={classes.content}>
					<div className={classes.toolbar} />
					{this.state.uiLoading && <CircularProgress size={150} className={classes.uiProgess} />}
				</main>
			);
		} else {
			return (
				<main className={classes.content}>
					<div className={classes.toolbar} />

					<IconButton
						className={classes.floatingButton}
						color="primary"
						aria-label="Add Todo"
						onClick={handleClickOpen}
					>
						<AddCircleIcon style={{ fontSize: 60 }} />
					</IconButton>
					<Dialog fullScreen open={open} onClose={handleClose} TransitionComponent={Transition}>
						<AppBar className={classes.appBar}>
							<Toolbar>
								<IconButton edge="start" color="inherit" onClick={handleClose} aria-label="close">
									<CloseIcon />
								</IconButton>
								<Typography variant="h6" className={classes.title}>
									{this.state.buttonType === 'Edit' ? 'Edit Todo' : 'Create a new Todo'}
								</Typography>
								<Button
									autoFocus
									color="inherit"
									onClick={handleSubmit}
									className={classes.submitButton}
								>
									{this.state.buttonType === 'Edit' ? 'Save' : 'Submit'}
								</Button>
							</Toolbar>
						</AppBar>

						<form className={classes.form} noValidate>
							<Grid container spacing={2}>
								<Grid item xs={12}>
									<TextField
										variant="outlined"
										required
										fullWidth
										id="todoTitle"
										label="Todo Title"
										name="title"
										autoComplete="todoTitle"
										helperText={errors.title}
										value={this.state.title}
										error={errors.title ? true : false}
										onChange={this.handleChange}
									/>
								</Grid>
								<Grid item xs={12}>
									<TextField
										variant="outlined"
										required
										fullWidth
										id="todoDetails"
										label="Todo Details"
										name="body"
										autoComplete="todoDetails"
										multiline
										rows={25}
										rowsMax={25}
										helperText={errors.body}
										error={errors.body ? true : false}
										onChange={this.handleChange}
										value={this.state.body}
									/>
								</Grid>
							</Grid>
						</form>
					</Dialog>

					<Grid container spacing={2}>
						{this.state.todos.map((todo) => (
							<Grid item xs={12} sm={6}>
								<Card className={classes.root} variant="outlined">
									<CardContent>
										<Typography variant="h5" component="h2">
											{todo.title}
										</Typography>
										<Typography className={classes.pos} color="textSecondary">
											{dayjs(todo.createdAt).fromNow()}
										</Typography>
										<Typography variant="body2" component="p">
											{`${todo.body.substring(0, 65)}`}
										</Typography>
									</CardContent>
									<CardActions>
										<Button size="small" color="primary" onClick={() => this.handleViewOpen({ todo })}>
											{' '}
											View{' '}
										</Button>
										<Button size="small" color="primary" onClick={() => this.handleEditClickOpen({ todo })}>
											Edit
										</Button>
										<Button size="small" color="primary" onClick={() => this.deleteTodoHandler({ todo })}>
											Delete
										</Button>
									</CardActions>
								</Card>
							</Grid>
						))}
					</Grid>

					<Dialog
						onClose={handleViewClose}
						aria-labelledby="customized-dialog-title"
						open={viewOpen}
						fullWidth
						classes={{ paperFullWidth: classes.dialogeStyle }}
					>
						<DialogTitle id="customized-dialog-title" onClose={handleViewClose}>
							{this.state.title}
						</DialogTitle>
						<DialogContent dividers>
							<TextField
								fullWidth
								id="todoDetails"
								name="body"
								multiline
								readonly
								rows={1}
								rowsMax={25}
								value={this.state.body}
								InputProps={{
									disableUnderline: true
								}}
							/>
						</DialogContent>
					</Dialog>
				</main>
			);
		}
	}
}
```

At the end of this file add the following export:

```js
export default withStyles(styles)(todo);
```

First we will understand how our UI works and after that we will understand the code. Go to the browser and you'll get the following UI:

![Image](https://www.freecodecamp.org/news/content/images/2020/04/TodoDashboard.png align="left")

*Todo Dashboard*

Click on the Add button at the bottom right corner and you’ll get the following screen:

![Image](https://www.freecodecamp.org/news/content/images/2020/04/AddTodo.png align="left")

*Add Todo*

Add the Todo title and details and press the submit button. You’ll get the following screen:

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Added-Todo.png align="left")

*Todo Dashboard*

After this click on the view button and you’ll be able to see the full details of the Todo:

![Image](https://www.freecodecamp.org/news/content/images/2020/04/View-Todo.png align="left")

*View Single Todo*

Click on the Edit button and you’ll be able to edit the todo:

![Image](https://www.freecodecamp.org/news/content/images/2020/04/EditTodo.png align="left")

*Edit Todo*

Click the delete button and you’ll be able to delete the Todo. Now as we are aware of how Dashboard works, we will understand the components used in it.

**1\. Add Todo:** For implementing the add todo we will use the [Dialogue component](https://material-ui.com/components/dialogs/#full-screen-dialogs) of Material UI. This component implements a hook functionality. We are using the classes so we will remove that functionality.

```js
// This sets the state to open and buttonType flag to add:
const handleClickOpen = () => {
      this.setState({
           todoId: '',
           title: '',
           body: '',
           buttonType: '',
           open: true
     });
};

// This sets the state to close:
const handleClose = (event) => {
      this.setState({ open: false });
};
```

Other than this we will also change the placement of the Add Todo Button.

```js
// Position our button
floatingButton: {
    position: 'fixed',
    bottom: 0,
    right: 0
},

<IconButton className={classes.floatingButton} ... >
```

Now we will replace the list tag with a form inside this Dialogue. It will help us in adding the new todo.

```js
// Show Edit or Save depending on buttonType state
{this.state.buttonType === 'Edit' ? 'Save' : 'Submit'}

// Our Form to add a todo
<form className={classes.form} noValidate>
	<Grid container spacing={2}>
		<Grid item xs={12}>
        // TextField here
        </Grid>
        <Grid item xs={12}>
        // TextField here
        </Grid>
    </Grid>
</form>
```

The handleSubmit consists of logic to read the `buttonType` state. If the state is an empty string `(“”)` then it will post on the Add Todo API. If the state is an `Edit` then in that scenario it will update the Edit Todo.

**2\. Get Todos:** To display the todos we will use the `Grid container` and inside it, we place the `Grid item` . Inside that, we will use a `Card` component to display the data.

```js
<Grid container spacing={2}>
    {this.state.todos.map((todo) => (
	<Grid item xs={12} sm={6}>
	<Card className={classes.root} variant="outlined">
	    <CardContent>
        // Here will show Todo with view, edit and delete button
        </CardContent>
    </Card>
    </Grid>))}
</Grid>
```

We use the map to display the todo item as the API sends them in a list. We will use the componentWillMount lifecycle to get and set the state before the render is executed. There are 3 buttons ( **view, edit, and delete** ) so we will need 3 Handlers to handle the operation when the button is clicked. We will learn about these buttons in their respective subsections.

**3\. Edit Todo:** For the edit todo, we are reusing the dialogue pop up code that is used in add todo. To differentiate between the button clicks we are using a `buttonType` state. For Add Todo the `buttonType` state is `(“”)` while for edit todo it is `Edit`.

```js
handleEditClickOpen(data) {
	this.setState({
		..,
		buttonType: 'Edit',
		..
	});
}
```

In the `handleSubmit` method we read the `buttonType` state and then send the request accordingly.

**4\. Delete Todo:** When this button is clicked we send the todo object to our deleteTodoHandler and then it sends the request further to the backend.

```js
<Button size="small" onClick={() => this.deleteTodoHandler({ todo })}>Delete</Button>
```

**5\. View Todo:** When showing the data we have truncated it so that the user will get a glimpse of what the todo is about. But if a user wants to know more about it then they need to click on the view button.

For this, we will use the [Customised dialogue](https://material-ui.com/components/dialogs/#customized-dialogs). Inside that, we use DialogTitle and DialogContent. It displays our title and content. In DialougeContent we will use the form to display the content that the user has posted. (This is one solution that I found there are many and you are free to try other.)

```js
// This is used to remove the underline of the Form
InputProps={{
       disableUnderline: true
}}

// This is used so that user cannot edit the data
readonly
```

**6\. Applying Theme:** This is the last step of our application. We will apply a theme on our application. For this we are using `createMuiTheme` and `ThemeProvider` from material UI. Copy-paste the following code in `App.js`:

```js
import { ThemeProvider as MuiThemeProvider } from '@material-ui/core/styles';
import createMuiTheme from '@material-ui/core/styles/createMuiTheme';

const theme = createMuiTheme({
	palette: {
		primary: {
			light: '#33c9dc',
			main: '#FF5722',
			dark: '#d50000',
			contrastText: '#fff'
		}
	}
});

function App() {
	return (
        <MuiThemeProvider theme={theme}>
        // Router and switch will be here.
        </MuiThemeProvider>
    );
}
```

We missed applying a theme to our button in `todo.js` in the `CardActions` . Add the color tag for the view, edit, and delete button.

```js
<Button size="small" color="primary" ...>
```

Go to the browser and you will find that everything is the same except that the app is a different color.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/FinalTodo.png align="left")

*TodoApp after applying theme*

And we're done! We have built a TodoApp using ReactJS and Firebase. If you have built it all the way to this point then a very big congratulations to you on this achievement.

> Feel free to connect with me on [Twitter](https://twitter.com/sharvinshah26) and [Github](https://github.com/Sharvin26).
