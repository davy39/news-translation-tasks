---
title: How to Build a Full-Stack Authentication App With React, Express, MongoDB,
  Heroku, and Netlify
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-07-05T13:50:44.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-fullstack-authentication-system-with-react-express-mongodb-heroku-and-netlify
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/pexels-sora-shimazaki-5935794--1-.jpg
tags:
- name: authentication
  slug: authentication
- name: full stack
  slug: full-stack
- name: React
  slug: react
seo_title: null
seo_desc: 'By Njoku Samson Ebere

  It''s almost impossible to build an application without registration and login functionalities.
  But this can be a bit tricky for beginners.

  In this article, I will guide you through creating a full-stack authentication applicatio...'
---

By Njoku Samson Ebere

It's almost impossible to build an application without registration and login functionalities. But this can be a bit tricky for beginners.

In this article, I will guide you through creating a full-stack authentication application. You will start with the backend which will be built with Express and hosted on [Heroku](https://www.heroku.com/). Then you will finish with the frontend that will be created with React and hosted on [Netlify](https://www.netlify.com/).

By the end of this tutorial, you will have learned how to use tools such as Nodejs, Express, React, MongoDB, Heroku, Netlify, bcrypt, jsonwebtoken, and React-Bootstrap.

## Table of Contents 

1. [Section 1: How to Build the Backend](#heading-section-1-how-to-build-the-backend)

* [How to Setup the Database](#heading-how-to-setup-the-database)
* [How to Connect Node.js to MongoDB](#heading-how-to-connect-nodejs-to-mongodb)
* [How to Create the Users Model](#heading-how-to-create-the-users-model)
* [How to Create the Register Endpoint](#heading-how-to-create-the-register-endpoint)
* [How to Create the Login Endpoint](#heading-how-to-create-the-login-endpoint)
* [How to Protect the Endpoints](#heading-how-to-protect-the-endpoints)
* [How to Host the Backend](#heading-how-to-host-the-backend)
* [Let's Review](#heading-lets-review)

2.   [Section 2: How to Build the Frontend](#heading-section-2-how-to-build-the-frontend)

* [How to Build the User Interface](#heading-how-to-build-the-user-interface)
* [How to Register a User](#heading-how-to-register-a-user)
* [How to Login a User](#heading-how-to-login-a-user)
* [How to Protect the Routes](#heading-how-to-protect-the-routes)
* [How to Make API Calls Using the useEffect Hook](#heading-how-to-make-api-calls-using-the-useeffect-hook)
* [How to Build the Logout Function](#heading-how-to-build-the-logout-function)
* [How to Host the Frontend](#heading-how-to-host-the-frontend)
* [Let's Review](#heading-lets-review)

3.   [All Resources And Previews](#heading-all-resources-and-previews)

4.   [Conclusion](#heading-conclusion)

## Prerequisites

This tutorial assumes that you already know the basics of:

* Nodejs and Express. Check out this [tutorial](https://www.freecodecamp.org/news/build-a-secure-server-with-node-and-express/) otherwise.
* [Github](https://github.com/).
* [React](https://reactjs.org/).

## Starter Code

* Please clone the starter code [here](https://github.com/EBEREGIT/auth-backend/tree/starter-code).
* In the project directory, run `npm install` to install dependencies
* Run `nodemon index` to serve the project on port 3000. 
* Check `http://localhost:3000/` on your browser to confirm

```cmd

$ git clone -b starter-code https://github.com/EBEREGIT/auth-backend


```

# Section 1: How to Build the Backend

The backend represents all the functionality that the users don't see. This includes the database design and API endpoints. 

This section will guide you step by step on how to build the backend of an authentication system. 

We'll begin with setting up a database using MongoDB, then we'll create endpoints (**login** and **register**), and finish by hosting the endpoints on Heroku.

Let's get started!

## How to Setup the Database 

This part will cover the database setup using [mongoDB atlas](https://www.mongodb.com/cloud/atlas).

You can create a free account [here](https://account.mongodb.com/account/register).

### How to Create a New Database User

On your dashboard, click on the `Database Access` link on the left (this will prompt you to add a new database user).

![Database Access photo](https://dev-to-uploads.s3.amazonaws.com/i/j3jakvaahhes3hwifuyw.JPG)
_user dashboard_

Click on the "Add New Database User" button and a `Add New Database User` dialogue box will open.

![Add New Database User dialogue box](https://dev-to-uploads.s3.amazonaws.com/i/3y63tqp3ama824jyjagg.JPG)
_`Add New Database User` dialogue box_

Select `Password` as the Authentication Method, and type in a username of your choice.

Then type in a password or Autogenerate Secure Password. I recommend auto-generating a password and storing it somewhere. You will need it soon.

Click on `Add User` to complete the process.

![User Created](https://dev-to-uploads.s3.amazonaws.com/i/iv92tdfrqegxgnj1lwyz.JPG)

### How to Create a Cluster

On the side menu, click on `clusters`. This brings you to the cluster page with a button: `Build a Cluster`.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/s2mtfzhyrzkz79omckha.JPG)

Click the button, and another page will come up.

Choose the `free cluster`. The settings page will open up. You will not be making any changes on this page.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/zmitdioyw4io3vuuv7u2.JPG)

Click `Create Cluster`. Wait a while for the cluster to be created completely. Once it is done, your screen should look like this:

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/whgefzv95dnmy2qo91xn.JPG)

### How to Connect a User to the Cluster

Click on the `connect` button:

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/n92cm0ztfc55i66vwx8t.JPG)

In the `Connect to Cluster0` modal that comes up, select `Connect from Anywhere` and update the settings.

Click on the `Choose a connection method` button:

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/y42t9m2kzmkp3oon0bb7.JPG)

Click on `Connect Your Application`. In the page that opens, make sure that the `DRIVER` is `nodejs` and the `VERSION` is `3.6 or later`.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/9yrg7nknor2xhogwldoe.JPG)

Copy the connection string and store it somewhere. You will need it soon.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/jj816egjtx7jjsiixs1a.JPG)

It should be similar to:

```javascript

mongodb+srv://plenty:<password>@cluster0.z3yuu.mongodb.net/<dbname>?retryWrites=true&w=majority


```

Close the dialogue box.

### How to Create a Collection (Tables)

Back on the Cluster page, click on `COLLECTIONS`.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/gtk0xqwbcf7xgdef6d9p.JPG)

You should be on this page below. Click on the `Add My Own Data` button:

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/b3itcf0383pvcuk7f8g7.JPG)

In the dialogue box that comes up, enter a `database name` and a `collection name`. My Database Name is `authDB` and My Collection name is `users`.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/2bb2p5fm1kz3muma35ow.JPG)

Click the `Create` button.

Congratulations on creating that Database and collection (table)!

## How to Connect Node.js to MongoDB

Let's get back to the starter code.

Still remember the database name, connection string, and password you generated? You will put them to use in a moment.

Replace the `<password>` and `<dbname>` with the password you generated and the database name you created like so

```javascript

mongodb+srv://plenty:RvUsNHBHpETniC3l@cluster0.z3yuu.mongodb.net/authDB?retryWrites=true&w=majority


```

Create a file in the root folder and name it `.env`.

Create a variable `DB_URL` and assign the connection string to it:

```javascript

DB_URL=mongodb+srv://plenty:RvUsNHBHpETniC3l@cluster0.z3yuu.mongodb.net/authDB?retryWrites=true&w=majority


```

Create a folder and name it `db`.

Create a new file in it and name it `dbConnect.js`.

Next, we'll need to install [mongoose](https://www.npmjs.com/package/mongoose):

```javascript

npm i mongoose -s


```

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/lsyp8s6sk30ke7g8x0ym.JPG)

In the `dbConnect` file, require `mongoose` and `env` with the following code:

```javascript

// external imports
const mongoose = require("mongoose");
require('dotenv').config()


```

Create and export a function to house the connection:

```javascript

async function dbConnect() {

}

module.exports = dbConnect;


```

In the function, the connection to the database was created using the connection string from the `.evn` file:

```javascript

// use mongoose to connect this app to our database on mongoDB using the DB_URL (connection string)
  mongoose
    .connect(
        process.env.DB_URL,
      {
        //   these are options to ensure that the connection is done properly
        useNewUrlParser: true,
        useUnifiedTopology: true,
        useCreateIndex: true,
      }
    )


```

Use a `then...catch...` block to show if the connection was successful or not:

```javascript

.then(() => {
      console.log("Successfully connected to MongoDB Atlas!");
    })
    .catch((error) => {
      console.log("Unable to connect to MongoDB Atlas!");
      console.error(error);
    });


```

The `dbConnect` file should look like this:

```javascript

// external imports
const mongoose = require("mongoose");
require('dotenv').config()

async function dbConnect() {
  // use mongoose to connect this app to our database on mongoDB using the DB_URL (connection string)
  mongoose
    .connect(
        process.env.DB_URL,
      {
        //   these are options to ensure that the connection is done properly
        useNewUrlParser: true,
        useUnifiedTopology: true,
        useCreateIndex: true,
      }
    )
    .then(() => {
      console.log("Successfully connected to MongoDB Atlas!");
    })
    .catch((error) => {
      console.log("Unable to connect to MongoDB Atlas!");
      console.error(error);
    });
}

module.exports = dbConnect;


```

In the `app.js` file, require the `dbConnect` function and execute it:

```javascript

// require database connection 
const dbConnect = require("./db/dbConnect");

// execute database connection 
dbConnect();


```

Check your terminal. If you didn't miss any steps, you should have `"Successfully connected to MongoDB Atlas!"` printed:

![Terminal showing "Successfully connected to MongoDB Atlas!"](https://dev-to-uploads.s3.amazonaws.com/i/u36z3xyjtr6mpgyq6gty.JPG)

## How to Create the Users Model

The users model tells the database how to store data that a user passes. The following steps will show you how to create a model for users:

Create a file in the `db` folder and name it `userModel`.

Require `mongoose` in the `userModel` file:

```javascript

const mongoose = require("mongoose");


```

Create a constant (`UserSchema`) and assign it the mongoose schema:

```javascript

const UserSchema = new mongoose.Schema({})


```

In the schema, enter the 2 fields needed (`email` and `password`) and assign an empty object to them:

```javascript
const UserSchema = new mongoose.Schema({
  email: {},

  password: {},
})


```

Specify how the fields should work by adding some [mongoose option](https://mongoosejs.com/docs/guide.html):

```javascript

email: {
    type: String,
    required: [true, "Please provide an Email!"],
    unique: [true, "Email Exist"],
  },

  password: {
    type: String,
    required: [true, "Please provide a password!"],
    unique: false,
  },


```

Finally, export `UserSchema` with the following code:

```javascript

module.exports = mongoose.model.Users || mongoose.model("Users", UserSchema);


```

The code above is saying: _"create a user table or collection if there is no table with that name already"._

You have completed the model for the user. The `user` collection is now ready to receive the data that is to be passed to it.

## How to Create the Register Endpoint

In this section, you will create an endpoint that you'll use to add a user to the database. Follow these steps:

Install [bcrypt](https://www.npmjs.com/package/bcrypt). We'll use this to hash the password that is received from the users.

```javascript

npm install --save bcrypt


```

Require `bcrypt` at the top of the `app.js` file:

```javascript

const bcrypt = require("bcrypt");


```

Require the `userModel` just below the line where you required the database:

```javascript

const User = require("./db/userModel");


```

Create a `register` endpoint just before the `module.exports = app;` line:

```javascript

app.post("/register", (request, response) => {

});


```

Hash the password before saving the `email` and `password` into the database with the following code:

```javascript

bcrypt.hash(request.body.password, 10)
  .then()
  .catch()


```

The code above is telling `bcrypt` to hash the `password` received from `request body` 10 times or 10 salt rounds. 

If the hash is successful, continue in the `then` block and save the `email` and `hashed password` in the database, else return an error in the `catch` block.

In the `catch` block, return an error:

```javascript

   .catch((e) => {
      response.status(500).send({
        message: "Password was not hashed successfully",
        e,
      });
    });


```

In the `then` block, save the data you have now. Create a new instance of the `userModel` and collect the updated data:

```javascript

.then((hashedPassword) => {
      const user = new User({
        email: request.body.email,
        password: hashedPassword,
      });
});


```

Save the data with:

```javascript

user.save()


```

And that is it. If you stop at this point, it's all good. It saves but you get no feedback.

To get feedback, use a `then...catch...` block:

```javascript

     user.save().then((result) => {
        response.status(201).send({
          message: "User Created Successfully",
          result,
        });
      })
      .catch((error) => {
        response.status(500).send({
          message: "Error creating user",
          error,
        });
      });


```

Finally, the `register` endpoint looks like this:

```javascript

// register endpoint
app.post("/register", (request, response) => {
  // hash the password
  bcrypt
    .hash(request.body.password, 10)
    .then((hashedPassword) => {
      // create a new user instance and collect the data
      const user = new User({
        email: request.body.email,
        password: hashedPassword,
      });

      // save the new user
      user
        .save()
        // return success if the new user is added to the database successfully
        .then((result) => {
          response.status(201).send({
            message: "User Created Successfully",
            result,
          });
        })
        // catch error if the new user wasn't added successfully to the database
        .catch((error) => {
          response.status(500).send({
            message: "Error creating user",
            error,
          });
        });
    })
    // catch error if the password hash isn't successful
    .catch((e) => {
      response.status(500).send({
        message: "Password was not hashed successfully",
        e,
      });
    });
});


```

### How to Test the Register Endpoint

Start the server in the terminal if you have not done so:

![Start your terminal](https://dev-to-uploads.s3.amazonaws.com/i/oo9g5y5j9tiv1t8cn91y.JPG)

Go to Postman and test:

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/oe3ay8c5gz2c24cpw1cr.JPG)

Go to your MongoDB Atlas. 

Click on `Collections` and you should see the data that you just added:

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/4znw7bw783l1hx1i3rms.JPG)



## How to Create the Login Endpoint

This part will cover login with [`jasonwebtoken (JWT)`](https://www.npmjs.com/package/jsonwebtoken). By the end, you will have learned how to crosscheck users and match the `hashed password` to the `plain text password`.

These are the steps:

First, you need to install JWT:

```javascript

npm i jsonwebtoken -s


```

Import `JWT` just below the `const bcrypt = require("bcrypt");` line at the top of the `app.js` file:

```javascript

const jwt = require("jsonwebtoken");


```

Just below the `register` endpoint, enter the following function:

```javascript

app.post("/login", (request, response) => {
  
})


```

Check if the email that the user enters on login exists:

```javascript

  User.findOne({ email: request.body.email })


```

Use a `then...catch...` block to check if the email search above was successful or not. If it is unsuccessful, capture that in the `catch` block:

```javascript

User.findOne({ email: request.body.email })
    .then()
    .catch((e) => {
      response.status(404).send({
        message: "Email not found",
        e,
      });
    });


```

If successful, compare the password entered with the hashed password in the database. Do this in the `then...` block:

```javascript

   .then((user)=>{
      bcrypt.compare(request.body.password, user.password)
   })


```

Use a `then...catch...` block again to check if the comparison is successful or not. If the comparison is unsuccessful, return an error message in the `catch` block:

```javascript

    .then((user)=>{
      bcrypt.compare(request.body.password, user.password)
      .then()
      .catch((error) => {
        response.status(400).send({
          message: "Passwords does not match",
          error,
        });
      })
    })


```

Check whether the password is correct in the `then` block:

```javascript

      .then((passwordCheck) => {

          // check if password matches
          if(!passwordCheck) {
            return response.status(400).send({
              message: "Passwords does not match",
              error,
            });
          }
        })


```

If the password matches, then create a random token with the `jwt.sign()` function. It takes 3 parameters: `jwt.sign(payload, secretOrPrivateKey, [options, callback])`. You can read more [here](https://www.npmjs.com/package/jsonwebtoken#usage).

```javascript

bcrypt.compare(request.body.password, user.password)
      .then((passwordCheck) => {

          // check if password matches
          if(!passwordCheck) {
            return response.status(400).send({
              message: "Passwords does not match",
              error,
            });
          }

        //   create JWT token
        const token = jwt.sign(
          {
            userId: user._id,
            userEmail: user.email,
          },
          "RANDOM-TOKEN",
          { expiresIn: "24h" }
        );
      })


```

Finally, return a success message with the token created:

```javascript

.then((user)=>{
      bcrypt.compare(request.body.password, user.password)
      .then((passwordCheck) => {

          // check if password matches
          if(!passwordCheck) {
            return response.status(400).send({
              message: "Passwords does not match",
              error,
            });
          }

        //   create JWT token
        const token = jwt.sign(
          {
            userId: user._id,
            userEmail: user.email,
          },
          "RANDOM-TOKEN",
          { expiresIn: "24h" }
        );

         //   return success response
         response.status(200).send({
          message: "Login Successful",
          email: user.email,
          token,
        });
      })


```

The Login Endpoint now looks like this:

```javascript

// login endpoint
app.post("/login", (request, response) => {
  // check if email exists
  User.findOne({ email: request.body.email })

    // if email exists
    .then((user) => {
      // compare the password entered and the hashed password found
      bcrypt
        .compare(request.body.password, user.password)

        // if the passwords match
        .then((passwordCheck) => {

          // check if password matches
          if(!passwordCheck) {
            return response.status(400).send({
              message: "Passwords does not match",
              error,
            });
          }

          //   create JWT token
          const token = jwt.sign(
            {
              userId: user._id,
              userEmail: user.email,
            },
            "RANDOM-TOKEN",
            { expiresIn: "24h" }
          );

          //   return success response
          response.status(200).send({
            message: "Login Successful",
            email: user.email,
            token,
          });
        })
        // catch error if password does not match
        .catch((error) => {
          response.status(400).send({
            message: "Passwords does not match",
            error,
          });
        });
    })
    // catch error if email does not exist
    .catch((e) => {
      response.status(404).send({
        message: "Email not found",
        e,
      });
    });
});



```

### How to Test the Login Endpoint

Let's try to log in with the credentials that were registered in the last part. See the random `token` generated on a successful login:

![Login Success Image](https://dev-to-uploads.s3.amazonaws.com/i/krz1ikslqsilk1d8lvpr.JPG)

If `email` is incorrect or does not exist, here's what you get:

![Email incorrect or does not exist](https://dev-to-uploads.s3.amazonaws.com/i/xy9ka8we8n2nvdaeain4.JPG)

If the `password` is incorrect, here's what you see:

![Password incorrect](https://dev-to-uploads.s3.amazonaws.com/i/tvq3cvsoh3ff24zl9e5k.JPG)

## How to Protect the Endpoints

This part will teach you how to protect some endpoints from unauthenticated users.

### Create Two Endpoints

You need two endpoints to be able to see how it works. Copy the following endpoints and paste them into the `app.js` file just before the last line.

```javascript
// free endpoint
app.get("/free-endpoint", (request, response) => {
  response.json({ message: "You are free to access me anytime" });
});

// authentication endpoint
app.get("/auth-endpoint", (request, response) => {
  response.json({ message: "You are authorized to access me" });
});

```

### Create the Authentication Function

Next, you'll need to make a function to enable you to protect a particular endpoint from unauthenticated users.

Create a file in the root directory and name it `auth.js`.

Import `jasonwebtoken` at the top of the file:

```javascript

const jwt = require("jsonwebtoken");


```

Create and export an asynchronous function in which the authorisation code will live:

```javascript

module.exports = async (request, response, next) => {
    
}


```

In the function, use a `try...catch...` block to check if a user is logged in:

```javascript

    try {
        
    } catch (error) {
        response.status(401).json({
            error: new Error("Invalid request!"),
          });
    }


```

In the `try{}` block, get the authentication token from the `authorization header`:

```javascript

//   get the token from the authorization header
    const token = await request.headers.authorization.split(" ")[1];


```

Check if the token that was generated matches the token string (**RANDOM-TOKEN**) entered initially:

```javascript

//check if the token matches the supposed origin
    const decodedToken = await jwt.verify(
      token,
      "RANDOM-TOKEN"
    );


```

Pass in the details of the `decodedToken` to the `user` constant:

```javascript

// retrieve the user details of the logged in user
    const user = await decodedToken;


```

Pass the `user` to the endpoint:

```javascript

// pass the the user down to the endpoints here
    request.user = user;


```

Finally, open the way to the endpoint:

```javascript

// pass down functionality to the endpoint
    next();


```

The `auth.js` file now looks like this:

```javascript

const jwt = require("jsonwebtoken");

module.exports = async (request, response, next) => {
  try {
    //   get the token from the authorization header
    const token = await request.headers.authorization.split(" ")[1];

    //check if the token matches the supposed origin
    const decodedToken = await jwt.verify(token, "RANDOM-TOKEN");

    // retrieve the user details of the logged in user
    const user = await decodedToken;

    // pass the user down to the endpoints here
    request.user = user;

    // pass down functionality to the endpoint
    next();
    
  } catch (error) {
    response.status(401).json({
      error: new Error("Invalid request!"),
    });
  }
};


```

### How to Protect the Endpoint

This is the final and simplest step. Start by importing the authentication function to the `app.js` file like so:

```javascript

const auth = require("./auth");


```

Add `auth` as a second argument in the authentication endpoint in the `app.js` file:

```javascript

// authentication endpoint
app.get("/auth-endpoint", auth, (request, response) => {
  response.json({ message: "You are authorized to access me" });
});


```

And that's it. That is all you need to protect that route. Let's test it out.

### How to Test the Endpoint Protection

If the user is not logged in:

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/k9tlcam9ef4hjh93qeha.JPG)

If the user is logged in:

* Login like so:

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/has8qii5z8srvlu5nbp9.JPG)

Copy the token, and then open a new tab on `postman`.

Select `bearer token` in the authentication type.

Paste the token in the `token` field and send the request.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/s7evrpmfjy3mmfi5vtlb.JPG)

### How to Handle CORS Errors

One last thing! You need to handle CORS errors. This will allow the user in the frontend to consume the APIs that you have created without any problem.

To do this, navigate to the `app.js` file.

Add the following code just below the `dbConnect()` line:

```javascript

// Curb Cores Error by adding a header here
app.use((req, res, next) => {
  res.setHeader("Access-Control-Allow-Origin", "*");
  res.setHeader(
    "Access-Control-Allow-Headers",
    "Origin, X-Requested-With, Content, Accept, Content-Type, Authorization"
  );
  res.setHeader(
    "Access-Control-Allow-Methods",
    "GET, POST, PUT, DELETE, PATCH, OPTIONS"
  );
  next();
});


```

And with this, you are a Backend Authentication Champion!!

## How to Host the Backend

This part teaches you how to host the backend application on Heroku. By the end, it will be available to everyone on the internet. Follow the steps below:

Create an account on [Heroku](https://heroku.com/).

If you have created an account, you may have been prompted to create an app (that is, a folder where your app will be housed). Create it. Mine is named `nodejs-mongodb-auth-app`.

Go to your app's dashboard:

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/msnum8scqj031dw53j27.JPG)

Select the `GitHub` Deployment method:

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/5edwt90cpy75b3uyqgvy.JPG)

Search and select a repo.

Click on `connect`:

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/6rpr4heuqqa9gn4qy1rt.JPG)

Select the branch you want to deploy (in my case, it is the `master` branch):

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/4ka9c6781vft1gio7p0k.JPG)

Enable automatic deployment by clicking the `Enable automatic deployment` button as in the image above.

Click on the `Deploy` button in the manual deploy:

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/7ksrclnfyjzzvn2nr4gc.JPG)

You will not have to do all this for subsequent deployments.

Now you have a button telling you to "view site" after the build is completed. Click it. This will open your app in a new tab.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/pa4ohxetzg4o6a9ek53n.jpg)

**OHHH NOOOO!!!! A BUG? APPLICATION ERROR?**

Well, it is just a small issue. Something you should never forget to do while making deployments. Most hosting services will require it.

### How to Fix the Heroku Application Error

In the root directory of your project, create a file and name it `Procfile`. It has no extension.

In the file, enter the following:

```javascript
web: node index.js

```

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/k655prvq8m34jsbs3p37.JPG)

This directs Heroku to the server file (`index.js`) which is the entry point of the application. If your server is in a different file, go ahead and modify it as required.

Save the file, and push the new changes to GitHub.

Wait for 2 to 5 minutes for Heroku to automatically detect changes in your GitHub repo and reflect the changes on the app.

You can now refresh that error page and see your hard work paying off:

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/cfdmvfquj0jsoxf4npeg.JPG)

### How to Add MongoDB

You may have noticed that other routes are not functional. It is because you have not included the database.

Remember that the URL to the database is in the `.env` file. But the `.env` file is not included in the project on GitHub after you pushed it. So you have to directly add the MongoDB URL into the Heroku app.

Let's do that...

Navigate to the settings of your app: `https://dashboard.heroku.com/apps/<your_app_name>/settings`

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/ojmvtebcl4dg6hhbsme5.JPG)

Scroll down to the `Config Vars` section.

Add the key and value of your database:

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/jo0nlhdf81aeu5cw26n3.JPG)

That is all! Your App should be working fine now.

### How to Test the Endpoints After Hosting

The easiest way to test if it is working is to try the login endpoint.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/op98eomewsw8n96hibbe.JPG)

It worked!

## Let's Review

The aim of this section was to create a backend authentication application. As you developed the application, you learned about `bycrypt`, `jsonwebtoken`, `heroku`, `CORS`, `database`, `MongoDB`, `Clusters`, `collections`, and `models`.

You started by setting up a database on MongoDB Atlas. Then you proceeded to create two endpoints – register and login – to enable us to input a user into the database and crosscheck if the user exists. Next, you saw how you can protect endpoints and how to handle CORS errors. Finally, you learned how to host the application that you have built.

The code for this section can be found [here](https://github.com/EBEREGIT/auth-backend). It is live on Heroku [here](https://nodejs-mongodb-auth-app.herokuapp.com/).

The next section will help us make this application useful to end-users by building a frontend to bridge the gap between the users and the backend.

# Section 2: How to Build the Frontend 

The frontend represents what the user can see and interact with. You will build a user interface to enable the user to communicate with the backend by clicking buttons.

You will begin by building the UI using React-Bootstrap. Next, you will connect the UI to the endpoints using `axios`. You will then protect some routes against unauthorised users. Finally, you'll host the frontend on Netlify.

Let's get to work!

## How to Build the User Interface

This part will introduce you to React-Bootstrap and guide you in building the Register and Login forms.

[Bootstrap](https://getbootstrap.com/) has stolen the heart of many developers over the years. This is understandable because it helps you write shorter and cleaner code, it saves time, and it is sophisticated enough to handle a lot of developers' concerns especially if you don't like writing CSS.

There is also [React](https://reactjs.org/) which has become one of the most popular frontend JavaScript frameworks/libraries. It has a large community built up around it, too.

To ensure even easier and faster development with React, Bootstrap has gone ahead and developed a new codebase called [React-Bootstrap](https://react-bootstrap.netlify.app/).

React-Bootstrap is still Bootstrap but it has been designed to fit in properly to React. This ensures that there are few or no bugs while building your application.

### Why Use React-Bootstrap Instead of Bootstrap?

React-Bootstrap has been built and tailored specifically for React applications. This means that it is more compatible.

React-Bootstrap code is generally shorter than Bootstrap code. For example, if you want to create a three-grid column in one row, you can do it in the following ways:

Using Bootstrap:

```javascript

<div class="container">
  <div class="row">
    <div class="col-sm">
      One of three columns
    </div>
    <div class="col-sm">
      two of three columns
    </div>
    <div class="col-sm">
      three of three columns
    </div>
  </div>
</div>


```

Using React-Bootstrap:

```javascript

<Container>
  <Row>
    <Col>One of three columns</Col>
    <Col>two of three columns</Col>
    <Col>three of three columns</Col>
  </Row>
</Container>


```

### How to Use React-Bootstrap

The following steps will show you how to create a simple UI with React-Bootstrap:

#### How to Set Up the Project

Create a React project and name it `react-auth`. 

```javascript

npx create-react-app react-auth


```

Open the project in a terminal and navigate into the project folder. I will use VS Code.

```javascript

cd react-auth


```

Install React-Bootstrap:

```javascript

npm install react-bootstrap bootstrap


```

Import the Bootstrap CSS file in the `index.js` file:

```javascript

import 'bootstrap/dist/css/bootstrap.min.css';


```

### How to Create the Components

This part will show you how to use the already-made components to create a UI. You will create the Register and Login forms here.

Create a new file in the `src` folder. Name it: `Register.js`.

In the file, start with the following code:

```javascript

import React from 'react'

export default function Register() {
    return (
        <>
            
        </>
    )
}


```

Enter the following code in the `return` statement:

```javascript

      <h2>Register</h2>
      <Form>
        {/* email */}
        <Form.Group controlId="formBasicEmail">
          <Form.Label>Email address</Form.Label>
          <Form.Control type="email" placeholder="Enter email" />
        </Form.Group>

        {/* password */}
        <Form.Group controlId="formBasicPassword">
          <Form.Label>Password</Form.Label>
          <Form.Control type="password" placeholder="Password" />
        </Form.Group>

        {/* submit button */}
        <Button variant="primary" type="submit">
          Submit
        </Button>
      </Form>


```

Now, you have to inform Bootstrap that you want to use the `Form` and `Button` components. So import them at the top:

```javascript

import { Form, Button } from "react-bootstrap";


```

You can also choose to do it individually like so:

```javascript

import Form from 'react-bootstrap/Form'
import Button from 'react-bootstrap/Button'


```

Show the Register component on the page. First, replace the code in the `App.js` file with the following code:

```javascript

import { Container, Col, Row } from "react-bootstrap";
import "./App.css";

function App() {
  return (
    <Container>
      <Row>

      </Row>
    </Container>
  );
}

export default App;


```

In the `Row` component, enter the following:

```javascript

    <Col xs={12} sm={12} md={6} lg={6}></Col>
    <Col xs={12} sm={12} md={6} lg={6}></Col>


```

This will make sure that there are two columns in large and medium devices while there will be one column on each row on small and extra small devices.

In the first column, add the `Register` component you created and import it at the top of the file. The `App.js` file will look like this:

```javascript

import { Container, Col, Row } from "react-bootstrap";
import Register from "./Register";

function App() {
  return (
    <Container>
      <Row>
        <Col xs={12} sm={12} md={6} lg={6}>
          <Register />
        </Col>

        <Col xs={12} sm={12} md={6} lg={6}></Col>
      </Row>
    </Container>
  );
}

export default App;



```

Run `npm start` in the terminal and see the output on the browser.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/lml6u4qdyq936ld3w72j.JPG)

You will notice that only one column is taken. Now your job is to create a LOGIN component with the same code as in the REGISTER component. Then add it in the second column. Check out my output below:

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/pic57grbm1tjcz6fcrre.JPG)

Walah! You can now create React applications faster by leveraging React-Bootstrap.

Now, you will begin connecting these forms to the backend.

## How to Register a User

This part takes you through connecting the registration form to the `register` endpoint: `https://nodejs-mongodb-auth-app.herokuapp.com/register`.

Navigate into the `Register.js` file.

Set initial states for `email`, `password`, and `register`.

```javascript

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [register, setRegister] = useState(false);


```

Set a `name` and `value` attribute for the `email` and `password` input fields:

```javascript

{/* email */}
        <Form.Group controlId="formBasicEmail">
          <Form.Label>Email address</Form.Label>
          <Form.Control
            type="email"
            name="email"
            value={email}
            placeholder="Enter email"
          />
        </Form.Group>

        {/* password */}
        <Form.Group controlId="formBasicPassword">
          <Form.Label>Password</Form.Label>
          <Form.Control
            type="password"
            name="password"
            value={password}
            placeholder="Password"
          />
        </Form.Group>


```

At this point, you will notice that you can no longer type into the Register Form fields. This is because you have not set the field to update from the previous state to the current state. 

Let's do that...

Add `onChange={(e) => setEmail(e.target.value)}`  
and `onChange={(e) => setPassword(e.target.value)}` to the `email` and `password` input fields respectively:

```javascript

       {/* email */}
        <Form.Group controlId="formBasicEmail">
          <Form.Label>Email address</Form.Label>
          <Form.Control
            type="email"
            name="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            placeholder="Enter email"
          />
        </Form.Group>

        {/* password */}
        <Form.Group controlId="formBasicPassword">
          <Form.Label>Password</Form.Label>
          <Form.Control
            type="password"
            name="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            placeholder="Password"
          />
        </Form.Group>


```

Now you can type into the form fields because it is updating the state based on the content you type in.

Add `onSubmit={(e)=>handleSubmit(e)}` and `onClick={(e)=>handleSubmit(e)}` to the `form` and `button` elements, respectively. 

`onSubmit` enables form submission using the `Enter` key, while `onClick` enables form submission by clicking the button. Now the form looks like this:

```javascript

      <Form onSubmit={(e)=>handleSubmit(e)}>
        {/* email */}
        <Form.Group controlId="formBasicEmail">
          <Form.Label>Email address</Form.Label>
          <Form.Control
            type="email"
            name="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            placeholder="Enter email"
          />
        </Form.Group>

        {/* password */}
        <Form.Group controlId="formBasicPassword">
          <Form.Label>Password</Form.Label>
          <Form.Control
            type="password"
            name="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            placeholder="Password"
          />
        </Form.Group>

        {/* submit button */}
        <Button
          variant="primary"
          type="submit"
          onClick={(e) => handleSubmit(e)}
        >
          Register
        </Button>
      </Form>


```

To test if this is working, create the following function just before the `return` line:

```javascript

const handleSubmit = (e) => {
    // prevent the form from refreshing the whole page
    e.preventDefault();
    // make a popup alert showing the "submitted" text
    alert("Submited");
  }


```

If you click the button or hit the Enter Key, this should be your result:

![Testing the handleSubmit function](https://dev-to-uploads.s3.amazonaws.com/i/zryimfq0tsf20umz70oj.JPG)

### How to Build the `handleSubmit` Function

Now remove the `alert` statement from the `handleSubmit` function.

Install `axios`.  You'll use it to call the endpoint or connect the frontend to the backend as the case may be.

```javascript

npm i axios


```

Import `axios` at the top of the file:

```javascript

import axios from "axios";


```

In the handleSubmit function, build the configuration needed for `axios` to successfully connect the frontend to the backend.

```javascript

// set configurations
    const configuration = {
      method: "post",
      url: "https://nodejs-mongodb-auth-app.herokuapp.com/register",
      data: {
        email,
        password,
      },
    };


```

The `method` tells how the data will be processed, `url` is the endpoint being called, and `data` contains all the input or `request body` that the backend expects. 

Having the configurations set up, make the call. The API call is just a one-line statement:

```javascript

axios(configuration)


```

With that, the API call has been completed. However, you need to be sure that it succeeded. And maybe show the result to the users. 

To fix that, you will use a then...catch... block.

Now you have this:

```javascript

    // make the API call
    axios(configuration)
    .then((result) => {console.log(result);})
    .catch((error) => {console.log(error);})


```

Register a new user and check the console for the result. The result that you get should look like this:

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/p18oqn02fsqe0hx2qnlc.JPG)

Of course, you will not direct your users to the console to check for the result of their registration. You need a way to communicate with the user.

Replace that code with the following code:

```javascript

    // make the API call
    axios(configuration)
      .then((result) => {
        setRegister(true);
      })
      .catch((error) => {
        error = new Error();
      });


```

By setting `register` to `true`, you can now tell when the registration process is completed. Tell the user by using the following code in the `Form` element:

```javascript

      {/* display success message */}
        {register ? (
          <p className="text-success">You Are Registered Successfully</p>
        ) : (
          <p className="text-danger">You Are Not Registered</p>
        )}


```

The code is a conditional statement to display a success message when the `register` is `true`. Now give it a try!

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/mbavmdxdhuleb9259rf1.gif)

If you are getting the same result as above, then you did it!

You are awesome.

## How to Login a User

Now it's time to turn your attention to the `Login.js` file.

Set initial states for `email`, `password`, and `login` like this:

```javascript

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [login, setLogin] = useState(false);


```

Set a `name` and `value` attribute for the `email` and `password` input fields:

```javascript

{/* email */}
        <Form.Group controlId="formBasicEmail">
          <Form.Label>Email address</Form.Label>
          <Form.Control
            type="email"
            name="email"
            value={email}
            placeholder="Enter email"
          />
        </Form.Group>

        {/* password */}
        <Form.Group controlId="formBasicPassword">
          <Form.Label>Password</Form.Label>
          <Form.Control
            type="password"
            name="password"
            value={password}
            placeholder="Password"
          />
        </Form.Group>


```

Add `onChange={(e) => setEmail(e.target.value)}`  
and `onChange={(e) => setPassword(e.target.value)}` to the `email` and `password` input fields, respectively. This is mine:

```javascript

       {/* email */}
        <Form.Group controlId="formBasicEmail">
          <Form.Label>Email address</Form.Label>
          <Form.Control
            type="email"
            name="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            placeholder="Enter email"
          />
        </Form.Group>

        {/* password */}
        <Form.Group controlId="formBasicPassword">
          <Form.Label>Password</Form.Label>
          <Form.Control
            type="password"
            name="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            placeholder="Password"
          />
        </Form.Group>


```

You can now type into the form.

Add `onSubmit={(e)=>handleSubmit(e)}` and `onClick={(e)=>handleSubmit(e)}` to the `form` and `button` elements, respectively. 

The `onSubmit` enables form submission using the `Enter` key while the `onClick` enables form submission by clicking the button. 

Now the form looks like this:

```javascript

      <Form onSubmit={(e)=>handleSubmit(e)}>
        {/* email */}
        <Form.Group controlId="formBasicEmail">
          <Form.Label>Email address</Form.Label>
          <Form.Control
            type="email"
            name="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            placeholder="Enter email"
          />
        </Form.Group>

        {/* password */}
        <Form.Group controlId="formBasicPassword">
          <Form.Label>Password</Form.Label>
          <Form.Control
            type="password"
            name="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            placeholder="Password"
          />
        </Form.Group>

        {/* submit button */}
        <Button
          variant="primary"
          type="submit"
          onClick={(e) => handleSubmit(e)}
        >
          Login
        </Button>
      </Form>


```

To test if this is working, create the following function just before the `return` line:

```javascript

const handleSubmit = (e) => {
    // prevent the form from refreshing the whole page
    e.preventDefault();
    // make a popup alert showing the "submitted" text
    alert("Submited");
  }


```

If you click the button or hit the `Enter` Key, this should be your result:

![Testing the handleSubmit function](https://dev-to-uploads.s3.amazonaws.com/i/zryimfq0tsf20umz70oj.JPG)

### How to Build the `handleSubmit` Function

Now you need to remove the `alert` statement from the `handleSubmit` function.

Import `axios` at the top of the file:

```javascript

import axios from "axios";


```

In the `handleSubmit` function, build the configuration needed for `axios` to successfully connect the frontend to the backend.

```javascript

// set configurations
    const configuration = {
      method: "post",
      url: "https://nodejs-mongodb-auth-app.herokuapp.com/login",
      data: {
        email,
        password,
      },
    };


```

The `method` tells how data will be processed, `url` is the endpoint through which the API function is accessed, and `data` contains all the input or `request body` that the backend expects.

Having the configurations set up, make the call.

```javascript

    // make the API call
    axios(configuration)
    .then((result) => {console.log(result);})
    .catch((error) => {console.log(error);})


```

Try to log in a user and check the console for the result

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/82z97iv2ym4z9sbng7ib.JPG)

Replace that code with the following code:

```javascript

    // make the API call
    axios(configuration)
      .then((result) => {
        setLogin(true);
      })
      .catch((error) => {
        error = new Error();
      });


```

By setting `login` to `true`, you can now tell when the login process is completed. Do that with the following code in the `Form` element:

```javascript

      {/* display success message */}
        {login ? (
          <p className="text-success">You Are Logged in Successfully</p>
        ) : (
          <p className="text-danger">You Are Not Logged in</p>
        )}


```

The code is a conditional statement to display a success message when the `login` is `true`. Give it a try.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/ujiildu7dqscevjhai3z.gif)

If you are getting the same result as above, then you did it!

You are a rockstar!

## How to Protect the Routes

Authentication will be useless if any user can still access the application somehow. Maybe by typing the desired URL in the address bar. In this part, you will be able to guard every route that needs authentication to be accessed.

First, you will create two more components. Next, you will set up routes for these components. Finally, you will create a component to protect the routes and apply the component to the desired routes.

### First, Create Two Components

Create a new file in the `src` directory and name it `FreeComponent.js`

The file should have the following content:

```javascript

import React from "react";

export default function FreeComponent() {
  return (
    <div>
      <h1 className="text-center">Free Component</h1>
    </div>
  );
}


```

Create a file and name it `AuthComponent.js`. The file should have the following content:

```javascript

import React from "react";

export default function AuthComponent() {
  return (
    <div>
      <h1 className="text-center">Auth Component</h1>
    </div>
  );
}


```

### How to Set Up the Route

Install `react-router-dom`:

```javascript

npm install --save react-router-dom


```

Navigate to `index.js` file.

Import `BrowserRouter`:

```javascript

import { BrowserRouter } from "react-router-dom";


```

Wrap the `<App>` component with the `</BrowserRouter>` component. So `index.js` file now looks like this:

```javascript

import React from "react";
import ReactDOM from "react-dom";
import "./index.css";
import App from "./App";
import reportWebVitals from "./reportWebVitals";
import "bootstrap/dist/css/bootstrap.min.css";
import { BrowserRouter } from "react-router-dom";

ReactDOM.render(
  <React.StrictMode>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </React.StrictMode>,
  document.getElementById("root")
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();


```

Now navigate to the `App.js` file.

Import `Switch` and `Route` at the top of the file:

```javascript

import { Switch, Route } from "react-router-dom";


```

Replace the `Account` Component with the following code:

```javascript

     <Switch>
        <Route exact path="/" component={Account} />
        <Route exact path="/free" component={FreeComponent} />
        <Route exact path="/auth" component={AuthComponent} />
      </Switch>


```

You will notice that nothing has changed. This is because the Account component is still the default component when routing. But you now have access to multiple routes.

Add links for navigation purposes under the `React Authentication Tutorial` heading:

```javascript

     <Row>
        <Col className="text-center">
          <h1>React Authentication Tutorial</h1>

          <section id="navigation">
            <a href="/">Home</a>
            <a href="/free">Free Component</a>
            <a href="/auth">Auth Component</a>
          </section>
        </Col>
      </Row>


```

Navigate to `index.css` to add the following styling for aesthetic purposes:

```css

#navigation{
  margin-top: 5%;
  margin-bottom: 5%;
}

#navigation a{
  margin-right: 10%;
}

#navigation a:last-child{
  margin-right: 0;
}


```

### The Protected Route Component

Having successfully set up routes, you now want to protect one (that is, the `AuthComponent`). To do this, you need to create a new component that will help to check if a certain condition has been met before allowing a user to access that route.

The condition you will be using in this case is the token generated during `login`. So before you create this `ProtectedRoute` component, let's go get the token from the `Login` component and make it available in all parts of the application.

#### How to Get the Token

Install `universal-cookie`. This is a cookie package that helps us share a value or variable across the application:

```javascript

npm i universal-cookie -s


```

Navigate to the `Login.js` file.

Import `universal-cookie` at the top and initialise it:

```javascript

import Cookies from "universal-cookie";
const cookies = new Cookies();


```

Next, add the following code in the `then` block of the `axios` call:

```javascript

       // set the cookie
        cookies.set("TOKEN", result.data.token, {
          path: "/",
        });


```

This code above sets the cookie with `cookie.set()`. It takes three arguments: `Name` of the cookie (here it's `"TOKEN"`, but it can be anything that you choose), `Value` of the cookie (`result.data.token`), and on which page or route you want it to be available (setting the `path` to `"/"` makes the cookie available in all the pages). Hopefully, that makes sense.

Below the `cookie.set()`, add the following line of code to redirect the user to the `authComponent` after a successful login

```javascript

        // redirect user to the auth page
        window.location.href = "/auth";


```

#### How to Create the Protected Route Component

Since the token is now available across the whole application, you now have access to it on all the components or pages already created or yet to be created. Let's continue...

Create a file with this name: `ProtectedRoutes.js`.

Enter the following code into the file:

```javascript

import React from "react";
import { Route, Redirect } from "react-router-dom";
import Cookies from "universal-cookie";
const cookies = new Cookies();

// receives component and any other props represented by ...rest
export default function ProtectedRoutes({ component: Component, ...rest }) {
  return (

    // this route takes other routes assigned to it from the App.js and return the same route if condition is met
    <Route
      {...rest}
      render={(props) => {
        // get cookie from browser if logged in
        const token = cookies.get("TOKEN");

        // returns route if there is a valid token set in the cookie
        if (token) {
          return <Component {...props} />;
        } else {
          // returns the user to the landing page if there is no valid token set
          return (
            <Redirect
              to={{
                pathname: "/",
                state: {
                  // sets the location a user was about to access before being redirected to login
                  from: props.location,
                },
              }}
            />
          );
        }
      }}
    />
  );
}


```

Hold up! Hold up!! What is going on in the `ProtectedRoutes` component?

This is like a template. What changes is the condition on which the `ProtectedRoutes` component is based. In this case, it is based on the `token` received from the cookie upon login. So in another application, the condition may be different.

This is what is going on here: The `ProtectedRoutes` component receives a `component` and then decides if the component should be returned to the user or not. 

To make this decision, it checks if there is a valid `token` (token is set upon a successful login) coming from the cookie. If the token is `undefined`, then it redirects to the default `path` (the landing page in this case).

The comments in the code will also help you to understand what is going on in the component. Follow Patiently...

### How to Use the `ProtectedRoutes` Component

It is time to use the `ProtectedRoutes` component to guard the AuthComponent since it should be accessible only to authenticated users.

Navigate to the `App.js` file.

Import the `ProtectedRoutes` component:

```javascript

import ProtectedRoutes from "./ProtectedRoutes";


```

Replace `<Route exact path="/auth" component={AuthComponent} />` with `<ProtectedRoutes path="/auth" component={AuthComponent} />`.

The `App.js` at this point looks like this:

```javascript

import { Switch, Route } from "react-router-dom";
import { Container, Col, Row } from "react-bootstrap";
import Account from "./Account";
import FreeComponent from "./FreeComponent";
import AuthComponent from "./AuthComponent";
import ProtectedRoutes from "./ProtectedRoutes";

function App() {
  return (
    <Container>
      <Row>
        <Col className="text-center">
          <h1>React Authentication Tutorial</h1>

          <section id="navigation">
            <a href="/">Home</a>
            <a href="/free">Free Component</a>
            <a href="/auth">Auth Component</a>
          </section>
        </Col>
      </Row>

      {/* create routes here */}
      <Switch>
        <Route exact path="/" component={Account} />
        <Route exact path="/free" component={FreeComponent} />
        <ProtectedRoutes path="/auth" component={AuthComponent} />
      </Switch>
    </Container>
  );
}

export default App;


```

Try to access `http://localhost:3000/auth` without logging in and notice how it redirects you to the landing page.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/7wmf5t65c946kqsndg8f.gif)
_That is amazing. Right?_

## How to Make API Calls Using the `useEffect` Hook

> [React Hooks](https://reactjs.org/docs/hooks-overview.html#:~:text=Hooks%20are%20functions%20that%20let,if%20you'd%20like.)) are functions that let you “hook into” React state and lifecycle features from function components. Hooks don't work inside classes — they let you use React without classes. 

Examples of hooks include `useState`, `useEffect`, and `useRef`.

This part will show you how to make API calls using the `useEffect` hook. The `useEffect` hook does for React `functional component`s what `componentDidMount()` does for react `class component`s.

The following are the endpoints that you will call:

* **Free Endpoint:** `https://nodejs-mongodb-auth-app.herokuapp.com/free-endpoint`
* **Protected Endpoint:** `https://nodejs-mongodb-auth-app.herokuapp.com/auth-endpoint`

### How to Call the Free Endpoint

Follow the steps below to call `https://nodejs-mongodb-auth-app.herokuapp.com/free-endpoint`.

Navigate to the `FreeComponent.js` file.

Import `useEffect` and `useState` by adjusting your `react` import line with the following:

```javascript

import React, { useEffect, useState,  } from "react";


```

Import `axios`:

```javascript

import axios from "axios";


```

Set an initial state for `message`:

```javascript

const [message, setMessage] = useState("");


```

Just above the `return` statement, declare the `useEffect` function:

```javascript

  useEffect(() => {

  }, [])


```

The empty array (that is, `[]`) is important to avoid continuous execution after an API call has been completed.

In the function, set the following configurations:

```javascript

  useEffect(() => {
    // set configurations for the API call here
    const configuration = {
      method: "get",
      url: "https://nodejs-mongodb-auth-app.herokuapp.com/free-endpoint",
    };
  }, [])


```

Next, make the API call using `axios`:

```javascript

  // useEffect automatically executes once the page is fully loaded
  useEffect(() => {
    // set configurations for the API call here
    const configuration = {
      method: "get",
      url: "https://nodejs-mongodb-auth-app.herokuapp.com/free-endpoint",
    };

    // make the API call
    axios(configuration)
      .then((result) => {
        // assign the message in our result to the message we initialized above
        setMessage(result.data.message);
      })
      .catch((error) => {
        error = new Error();
      });
  }, [])


```

`setMessage(result.data.message);` assigns the message in the result (that is, result.data.message) to the message initialised above. Now you can display the `message` in your component.

To display the `message` that you got on the `FreeComponent` page, enter the following code below the `<h1 className="text-center">Free Component</h1>` line:

```javascript

<h3 className="text-center text-danger">{message}</h3>


```

React will read the `message` as a variable because of the curly brackets. If the `message` is without the curly brackets, React reads it as a string.

This is the `FreeComponent.js` file at this point:

```javascript

import React, { useEffect, useState } from "react";
import axios from "axios";

export default function FreeComponent() {
  // set an initial state for the message we will receive after the API call
  const [message, setMessage] = useState("");

  // useEffect automatically executes once the page is fully loaded
  useEffect(() => {
    // set configurations for the API call here
    const configuration = {
      method: "get",
      url: "https://nodejs-mongodb-auth-app.herokuapp.com/free-endpoint",
    };

    // make the API call
    axios(configuration)
      .then((result) => {
        // assign the message in our result to the message we initialized above
        setMessage(result.data.message);
      })
      .catch((error) => {
        error = new Error();
      });
  }, []);

  return (
    <div>
      <h1 className="text-center">Free Component</h1>

      {/* displaying our message from our API call */}
      <h3 className="text-center text-danger">{message}</h3>
    </div>
  );
}


```

Here's the `FreeComponent` page right now:

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/7ap2bd2okfjwsrzl9a67.JPG)

### How to Call the Protected Endpoint

It is time to call `https://nodejs-mongodb-auth-app.herokuapp.com/auth-endpoint`.

Navigate to the `AuthComponent.js` file.

Import `useEffect` and `useState` by adjusting your `react` import line with the following:

```javascript

import React, { useEffect, useState,  } from "react";


```

Import `axios`:

```javascript

import axios from "axios";


```

Import and initialise universal-cookie:

```javascript

import Cookies from "universal-cookie";
const cookies = new Cookies();


```

Get the token generated on login:

```javascript

const token = cookies.get("TOKEN");


```

Set an initial state for `message`:

```javascript

const [message, setMessage] = useState("");


```

Just above the `return` statement, declare the `useEffect` function:

```javascript

  useEffect(() => {

  }, [])


```

In the function, set the following configurations:

```javascript

  useEffect(() => {
    // set configurations for the API call here
    const configuration = {
      method: "get",
      url: "https://nodejs-mongodb-auth-app.herokuapp.com/auth-endpoint",
      headers: {
        Authorization: `Bearer ${token}`,
      },
    };
  }, [])


```

Notice that this configuration contains a `header`. That is the main difference from the `free-endpoint` configuration. 

This is the case because the `auth-endpoint` is a protected endpoint that is only accessible using an `Authorization token`. So it is in the header that you specify the `Authorization token`. Without this header, the API call will return a `403:Forbidden` error.

Make the API call:

```javascript

// useEffect automatically executes once the page is fully loaded
  useEffect(() => {
    // set configurations for the API call here
    const configuration = {
      method: "get",
      url: "https://nodejs-mongodb-auth-app.herokuapp.com/auth-endpoint",
      headers: {
        Authorization: `Bearer ${token}`,
      },
    };

    // make the API call
    axios(configuration)
      .then((result) => {
        // assign the message in our result to the message we initialized above
        setMessage(result.data.message);
      })
      .catch((error) => {
        error = new Error();
      });
  }, []);


```

To display the `message` that you got on the `AuthComponent` page, enter the following code below the `<h1 className="text-center">Auth Component</h1>` line:

```javascript

<h3 className="text-center text-danger">{message}</h3>


```

Here's the `AuthComponent` page right now:

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/qqud8uirnrepmfxd0mff.JPG)

## How to Build the Logout Function

If for any reason you share a device with someone else, it is still possible for them to have access to the `authComponent` page after you are logged in. 

To ensure that does not happen, you need to destroy your authorisation token each time that you are done. 

To do this, add a button on the `authComponent` page.

Import the `Button` component:

```javascript

import { Button } from "react-bootstrap";


```

Add the following code below the text:

```javascript

<Button type="submit" variant="danger">Logout</Button>


```

The logout function is to be triggered when the button is clicked. So add `onClick={() => logout()}` to the button options. The button will now look like this:

```javascript

{/* logout */}
<Button type="submit" variant="danger" onClick={() => logout()}>
   Logout
</Button>


```

Create the function. Enter the following code just above the return:

```javascript

  // logout
  const logout = () => {
    
  }


```

Add the following code to the logout function to remove or destroy the token generated during login:

```javascript

// logout
  const logout = () => {
    // destroy the cookie
    cookies.remove("TOKEN", { path: "/" });
  }


```

Redirect the user to the landing page with the following code:

```javascript

// logout
  const logout = () => {
    // destroy the cookie
    cookies.remove("TOKEN", { path: "/" });
    // redirect user to the landing page
    window.location.href = "/";
  }


```

Add `className="text-center"` to the parent `div` of the `AuthComponent`, just to centralise the whole page. You can now remove it from other places. The `AuthComponent.js` file now has the following content:

```javascript

import React, { useEffect, useState } from "react";
import { Button } from "react-bootstrap";
import axios from "axios";
import Cookies from "universal-cookie";
const cookies = new Cookies();

// get token generated on login
const token = cookies.get("TOKEN");

export default function AuthComponent() {
  // set an initial state for the message we will receive after the API call
  const [message, setMessage] = useState("");

  // useEffect automatically executes once the page is fully loaded
  useEffect(() => {
    // set configurations for the API call here
    const configuration = {
      method: "get",
      url: "https://nodejs-mongodb-auth-app.herokuapp.com/auth-endpoint",
      headers: {
        Authorization: `Bearer ${token}`,
      },
    };

    // make the API call
    axios(configuration)
      .then((result) => {
        // assign the message in our result to the message we initialized above
        setMessage(result.data.message);
      })
      .catch((error) => {
        error = new Error();
      });
  }, []);

  // logout
  const logout = () => {
    // destroy the cookie
    cookies.remove("TOKEN", { path: "/" });
    // redirect user to the landing page
    window.location.href = "/";
  }

  return (
    <div className="text-center">
      <h1>Auth Component</h1>

      {/* displaying our message from our API call */}
      <h3 className="text-danger">{message}</h3>

      {/* logout */}
      <Button type="submit" variant="danger" onClick={() => logout()}>
        Logout
      </Button>
    </div>
  );
}


```

You can see the working application below:

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/8b4g8m53ckqc7ns0tdo8.gif)

And that is it for React authentication!

Congratulations! You are now a React authentication pro :)

## How to Host the Frontend

The React application will be hosted on Netlify. This will just take you a few steps to set up, so follow along:

Navigate to [https://app.netlify.com/signup](https://app.netlify.com/signup) and sign up.

Follow the process until you arrive at your dashboard.

Scroll down a bit and you will get to this screen:

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/xehd8jio7ht4lsjqvb7p.JPG)

You can drag your project folder into the box and your hosting will be done! Or you can connect it to your remote repo. 

The advantage of connecting to a remote repo is for continuous deployment. You will not have to do these steps again in case you have a reason to make changes to your app in the future.

So click on the `New Site from Git` button.

Choose the Git platform you want and grant authorisation to sync it to your Netlify app.

Choose the repo you want to sync. 

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/5rxhv6iy5z5qo3ywgix4.JPG)

Click on the `Deploy Site` button on the page that you are redirected to.

Wait for your site to be published. That should take less than 2 minutes. After that you can now click on the link that you see to access your site.

Notice the URL of your site at the top of the page. It is a random URL given to you by Netlify.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/doakehth09usrxg6vv2f.JPG)

You can change it by clicking on the `Site Settings` button.

In the `Site details` section, click on the `change site name` button.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/449x0ag7kwwmzwpcisu3.JPG)

Change the Name and Click `Save`.  


![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/4w4yaioa0wl9mw5hrei2.JPG)

Notice that the site name has been changed. See mine below:

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/kkojgyc0waxjn2ybq588.JPG)

You are likely to face the issue of redirecting to another page after hosting. The error may look like the image below:

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/12hi8shcwxyenvy1igar.JPG)

### How to Fix the "Page Not Found" Error

Go into the public folder of your React project.

Create a file and name it `_redirects`, and enter the following content:

```

    /*  /index.html 200


```

Save and push back to the Git platform where your app is hosted.

Wait a while for the app to be automatically published and you should be all good.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/zuewuniqjhpa9u8mys3d.JPG)
_The error is gone_

Congratulations! You are now a full-stack engineer... :)

## Let's Review

This section helped you connect users to the backend by building a user interface. You were able to learn about `React-Bootstrap`, `axios`, `React Hooks`, and `react-router-dom`.

You began with a brief introduction to `React-Bootstrap` and in that part, you built the registration and login form. 

Next, you connected the forms to their respective endpoints and protected some routes against unauthorised users. Finally, you used Netlify to host the application. 

All code for this section can be found [here](https://github.com/EBEREGIT/react-auth). It is live on Netlify [here](https://react-auth-app.netlify.app/)

## All Resources And Previews

#### Backend

* [The Node.js code is here](https://github.com/EBEREGIT/auth-backend)
* [The backend is live here](https://nodejs-mongodb-auth-app.herokuapp.com/)

#### Frontend

* [The React.js code is here](https://github.com/EBEREGIT/react-auth)
* [The front-end is live here](https://react-auth-app.netlify.app/)

## Conclusion

This was a long tutorial but I hope it was filled with helpful gems at every point. And I hope you enjoyed going through it as much as I did preparing it. It is my earnest desire to lower the barrier for anyone getting into tech.

The main purpose of this tutorial is to teach anyone how to create authentication both on the backend and frontend. But beyond that, this tutorial is to help beginners and advanced developers who are looking to transition to full-stack developers. 

The hosting parts added to each section teaches beginners how to get their projects out to the public. When you have your projects publicly available for preview, recruiters can easily access what you can do. That gives you a better fighting chance during recruitment.

At this point, you are sure to keep winning if you keep building. Nothing can stop you anymore.


