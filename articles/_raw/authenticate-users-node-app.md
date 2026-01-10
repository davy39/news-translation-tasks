---
title: How to Authenticate Users in Your Node App with Cookies, Sessions, and Passport.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-11-05T13:08:00.000Z'
originalURL: https://freecodecamp.org/news/authenticate-users-node-app
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5fa294a749c47664ed81a292.jpg
tags:
- name: Application Security
  slug: application-security
- name: authentication
  slug: authentication
- name: node
  slug: node
seo_title: null
seo_desc: "By Suchandra Datta\nLearning how to authenticate users into an app is one\
  \ of the first things you learn in any course focused on backend technologies. \n\
  And it’s one of the first steps you take when building a social media app, an app\
  \ for learning from..."
---

By Suchandra Datta

Learning how to authenticate users into an app is one of the first things you learn in any course focused on backend technologies. 

And it’s one of the first steps you take when building a social media app, an app for learning from online courses, and so on. 

In this article, we'll look at basic authentication concepts in a beginner-friendly way.

## How to Authenticate a User with Cookies

First off, let’s build a simple app that authenticates users using the classic username and password method – we wont worry about database connections right now. 

Whenever we try to load a page, the browser sends a request to the server, which responds accordingly. 

Initially when a user accesses the site, they are prompted for their registered username and password. Once given, they make themselves known to the server so subsequent requests to the server do not involve re-asserting their identity. 

But how will the server keep track of which users are already authenticated and which aren’t? Here’s where cookies come in. 

According to w3.org, cookies are defined as:

> “bits of text stored on the client machine and sent with the HTTP request to the Web site for which they were created.” 

Cookies are created and stored after a user logs in, and they're consulted before satisfying successive requests. Then they expire according to a specified time limit.

```
let express=require('express')
let cookie_parser=require('cookie-parser')
let app=express()
app.use(cookie_parser('1234'))
```

First, we set up our Express app and include the `cookie-parser` middleware. It parses the cookie header of the request, and adds it to `req.cookies` or `req.signedCookies` (if secret keys are being used) for further processing. 

`cookie-parser` takes a secret key as an argument, which will be used to create an HMAC of the current cookie's value. If the value is tampered with later on, it is detected since the signature made at time of creation doesn’t match the current signature. 

Next, when the user visits the appropriate URL (like /login or something similar), we need to perform some checks. Suppose the user logs in for the first time.

```
let cookie_Stuff=req.signedCookies.user
//But the user is logging in for the first time so there won't be any appropriate signed cookie for usage.
if(!cookie_Stuff)//True for our case
    {
        let auth_Stuff=req.headers.authorization
        if(!auth_Stuff)//No authentication info given
        {
            res.setHeader("WWW-Authenticate", "Basic")
            res.sendStatus(401)
        }
```

We use the WWW-Authenticate response header to define the authentication method that should be used to gain access to a resource (the "Basic" method).

The response from the client consists of the username and password separated by a colon. It is base64 encoded and is attached to the Authorization header of the request. 

The user is prompted for authentication information, which is extracted and checked. We actually we need to check from a database, but we do a naïve check for simplicity's sake right now. 

If the correct values are given, we set up an appropriate cookie. If not, then we prompt the user again. The next code snippet performs these steps:

```
else
        {
            step1=new Buffer.from(auth_Stuff.split(" ")[1], 'base64')
 //Extracting username:password from the encoding Authorization: Basic username:password
            step2=step1.toString().split(":")
//Extracting the username and password in an array
            if(step2[0]=='admin' && step2[1]=='admin')
            {
//Correct username and password given
                console.log("WELCOME ADMIN")
//Store a cookie with name=user and value=username
                res.cookie('user', 'admin', {signed: true})
                res.send("Signed in the first time")
            }
            else
            {
 //Wrong authentication info, retry
                res.setHeader("WWW-Authenticate", "Basic")
                res.sendStatus(401)
            }
        }
    }
```

What about the next time our user makes a request? From that time onwards until the cookie is cleared or expires, we check the value of the cookie for authentication.

```
else
    {//Signed cookie already stored
        if(req.signedCookies.user=='admin')
        {
            res.send("HELLO GENUINE USER")
        }
        else
        {
     //Wrong info, user asked to authenticate again
            res.setHeader("WWW-Authenticate", "Basic")
            res.sendStatus(401)
        }
    }
})
```

Now you know how to authenticate a user with cookies! 

You can check the cookie that's stored by navigating to the Storage section of your browser developer tools and going to the Cookies tab. The cookie value and parsed values are shown separately in two sections (in Firefox, for instance).

## How to Authenticate a User with Sessions

Let’s look at an analogy to help us understand sessions as compared to cookies. Imagine you’re an absent-minded person who keeps forgetting your friends' names. 

One solution is to give each friend a card with their name and image on it. Every time you meet them, simply ask to see the card that you gave them to refresh your memory. 

The problem is that your friends may lose this card. Or two of them may switch cards and play a prank on you. Or maybe your friend doesn't have enough space to store another card. 

In either case, the authentication mechanism shows signs of weakness. But this is essentially what cookies do – they are stored on the client-side and every time the client makes a request to their site, the cookie is accessed for authentication. They eat up some space or they maybe tampered with.

Instead of using cookies, let’s say you make a card for each friend and keep it with you. When you see them, you assign a way of matching the card with the person for easy identification. This way, the information does not reside with the client and is hence more secure. 

This scenario shows us how sessions work. The information about a newly authenticated user resides on the server, and only minimal information is passed back to the client. This way the client can be mapped to the stored piece of information.

`express-session` creates a session middleware that lets you easily set up sessions and manipulate them. 

The default storage server-side is MemoryStore. To store session information as JSON files, you need session-file-store. The below code does the following:

* It sets up the Express app
* It tells the middleware to request authentication if none is specified, and otherwise check if the username and password match. 
* If not, it again needs to make the same request for authentication, otherwise the session is established. 
* Then it adds the username as the user attribute and subsequently checks it. 

Again, this is just a simple example – the information that needs to be checked against the given data should at the very least be stored in a database.

```
let app=express()
app.use(session({
  store: new File_Store,
  secret: 'hello world',
  resave: true,
  saveUninitialized: true
}))
app.use('/', (req,res,next)=>{
  if(!req.session.user)
  {
    console.log("Session not set-up yet")
    if(!req.headers.authorization)
    {
      console.log("No auth headers")
      res.setHeader("WWW-Authenticate", "Basic")
      res.sendStatus(401)
    }
    else
    {
      auth_stuff=new Buffer.from(req.headers.authorization.split(" ")[1], 'base64')
      step1=auth_stuff.toString().split(":")
      console.log("Step1: ", step1)
      if(step1[0]=='admin' && step1[1]=='admin')
      {
        console.log('GENUINE USER')
        req.session.user='admin'
        res.send("GENUINE USER")
      }
      else
      {
        res.setHeader("WWW-Authenticate", "Basic")
        res.sendStatus(401)
      }
    }
  }
```

## How to Authenticate Users with Passport.js Middleware

So far, we've seen how to authenticate users with cookies and sessions. Now we'll see a third method of authentication.

Passport.js is an authentication middleware for Node that allows you to authenticate users using sessions and OAuth. It also lets you create custom strategies and a lot more.

```
let passport=require('passport')
let bcrypt=require('bcrypt-nodejs')
let User_Obj=require('./Set_Up_Database_Stuffs')
const local_strategy=require('passport-local').Strategy
```

This code sets up all the required modules for defining a suitable local strategy. The `passport-local` strategy allows authentication with a username and password alone. 

Make sure that the name of the form input element for username is “username” and for password is “password”. Although this sounds very intuitive, it caused me a lot of trouble as I had overlooked this part. Now it’s one of those things I’m not likely to overlook again (at least for the near future). 

You can also change the default names of the fields by passing JSON before the callback function in the call to `local_strategy`, where the JSON structure is `usernameField`: "Some new name for this field", and `passwordField`: "Some new name for this field".

```
passport.use(new local_strategy(
    async (username, password, done)=>{
        console.log("Here inside local_strategy" ,username, password)
    
    try
    {
        let row1=await User_Obj.findOne({username: username})
        console.log(row1)
        //row1 should be the tuple from database where the username field matches the username supplied.
        if(row1==null)
        {
            console.log("NO RECORDS FOUND")
            return done(null, false)
        }
        else
        {
            console.log("Record found")
            console.log(row1)
            if(bcrypt.compareSync(password, row1.password))//Compare plaintext password with the hash
            {
                console.log("The passwords match")
                console.log("Finished authenticate local")
                return done(null, row1)
            }
            else
                {
                    console.log("The passwords don't match")
                    return done(null, false)
                }
        }
        
    }
    catch(err){
        console.log("Some error here")
        return done(err)}
    }
  ));
```

The above lines are a simplistic implementation of `local-strategy` where the data is checked from a database with username as a field.

```javascript
app.post('/auth', passport.authenticate('local', {successRedirect: 'articles', failureRedirect: '/failurepage'}))
//Triggers the local strategy. If successful, redirect to articles page else show failure page
app.post('/donesignup', objForUrlencoded, async (req,res)=>{
    console.log(req.body)
    try
    {
        let row1=await User_Obj.findOne({username: req.body.username})
        console.log(row1)
        if(row1!=null)
        {
            console.log("That username already exists")
            res.render('signup')
        }
        else
        {
            console.log(bcrypt.hashSync(req.body.password[0], bcrypt.genSaltSync(8), null))//Get the hash of the password to store it in the database
            let save_this=User_Obj({username: req.body.username, password: bcrypt.hashSync(req.body.password[0], bcrypt.genSaltSync(8), null)})
            console.log(save_this)
            save_this.save()
            console.log("SAVED IT")//Save it to database
        }
    }
    catch(err){}
})
```

Whenever the user accesses the /auth route, it triggers the local strategy which executes as specified. If there is a failure during authentication, it redirects to a failure page. Otherwise, it redirects to an articles page (or whatever page you need). 

On a post request to /donesignup it checks if the username already exists. If not, then it adds it as a tuple to the database, where the fields are the username and a hash of the given password.

## Wrapping Up

So this wraps up my summary of different authentication methods in Node. 

The code used here is far from ideal, but I hope it helps someone out there who just started learning about authentication and was feeling overwhelmed. 

If you’ve read this far, thank you so much and please correct any bugs that may have crept in, despite my best efforts. Thank you once again and happy coding.

  

