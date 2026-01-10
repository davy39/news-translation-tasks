---
title: How to Build your Own Uber-for-X App
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-10-22T06:20:09.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-your-own-uber-for-x-app-33237955e253
coverImage: https://cdn-media-1.freecodecamp.org/images/1*WcHHixgDq7o5lN3biKIu9Q.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Ashwin Hariharan

  Featured in Mybridge’s Top Ten NodeJS articles from October 2016 and Top Ten NodeJS
  articles of the year (v.2017)



  Update: Check-out the latest version on my tech blog!

  This article is now a few years old - and due to JavaScript''...'
---

By Ashwin Hariharan

Featured in [Mybridge](https://medium.mybridge.co/)’s [Top Ten NodeJS articles from October 2016](https://medium.mybridge.co/node-js-top-ten-articles-from-october-fbde1ebe7785#.fnr9w51pr) and [Top Ten NodeJS articles of the year (v.2017)](https://medium.mybridge.co/node-js-top-10-articles-of-the-year-v-2017-79df8269d0f3#.f82p1dork)

*****
> **Update: Check-out the latest version on my [tech blog](https://ashwinhariharan.tech/blog/how-to-build-your-own-uber-for-x-app/)!**
> This article is now a few years old - and due to JavaScript's rapidly changing ecosystem, the article has become slightly outdated. Click on the above link for the updated version of this article and the project.
*****

Uber (if you haven’t heard of it) is a handy app that allows you to catch a cab without walking around to look for one. And most importantly, it solves the problems of demand and supply that exists among cab drivers and cab seekers.

Today, there are a variety of startups focused around **_Uber-for-X_** apps. The thinking goes that, what Uber did for cabs, they can surely do for other supply/demand problems.

So during a hackathon, me and my [friend](https://github.com/akdeboss) decided to build a citizen-cop app. We figured it would be cool to build something that can help your friends in times of trouble!

After some thinking, these were the following features that we agreed upon:

1. Civilians will be able to request the nearest police officer in their neighborhood at the press of a button. It’ll raise a ‘distress signal’ and alert nearby cops.
2. Any police in the vicinity will immediately receive the user’s location and can choose to accept the request and solve the issue.
3. A rating system
4. Data collected from locations, crime cases solved, etc. can be visualized on a map, or graphed with some other cool user interface widgets

![Image](https://cdn-media-1.freecodecamp.org/images/1*MW1nUkwxgGuUN8lbIFCfDg.png)

In this tutorial, I’ll walk you through how we built it step-by-step, so that you’ll be able to build your own **_Uber-for-X_** app.

![Image](https://cdn-media-1.freecodecamp.org/images/1*438j5EzvsD_q2cjBrKe-Tg.png)

Before you begin, it would help to keep the following points in mind —

* This tutorial will not focus on how to build the app for scale. Or for performance. It’s basically designed so that you can have fun while building it, and how you can create something that mimics Uber. Think of this as though building a Minimum Viable Product to demonstrate your idea or startup, for a proof-of-concept.
* Since I’ve not worked on Android or iPhone apps much, I’ll be building this to work inside a browser.

Now, every app that you build has few important pieces:

* a client-facing app (that you see in a browser or on your phone screens)
* on the back end, a web-server to handle incoming requests from the client and to route information
* and a database to store and query information.

On the back end, you’ll use MongoDB as your database. it’s easier to learn, and offers a lot of querying techniques to handle geospatial information, which you’ll need for your app.

You’ll use NodeJS for your back end logic. Because it’s the same language for both front-end and back-end you wouldn’t have to worry about learning a new language or syntax.

On the front end, you’ll use HTML5, CSS3, JavaScript, and also the Google Maps and Places APIs.

I’m assuming that you already have a working knowledge of JavaScript, and that you have at least a theoretical understanding of how NodeJS and MongoDB work.

Here are the contents of this tutorial :

**Part 1 (what you’re reading right now)**:

* MongoDB Schema design
* Using the Mongo Shell to query information
* Connecting your database with your Node-Express server and writing RESTful APIs

**Part 2**:

* Using Socket.IO to enable the cop and civilian devices talk to each other
* Using Google Maps API to show civilians and cops on a map

### Let’s get started!

Developers have used MongoDB to build applications for quite some time now. It has a shallow learning curve, and its versatility allows developers to rapidly build applications with ease.

I personally like MongoDB because it allows me to quickly build prototypes for an idea to demonstrate proof-of-concept.

Before you begin, do make sure that you have MongoDB and NodeJS installed. At the time of writing this article, the current version of MongoDB is **3.2**.

### **Designing the Schema**

Since you’re using MongoDB, everything that you save in it is a collection of documents.

Let’s create a collection called _citizensData_ for storing citizen information, and another collection called _policeData_ for storing cops info. So go ahead, open up your terminal and type _mongo_ to fire up the mongo shell. Once it opens up, you can show existing databases in MongoDB by typing:

```
show dbs
```

You need a new database to store your app data. Let’s call it _myUberApp._ To create a new database, you can type:

```
use myUberApp
```

The _use_ command has the effect of creating a new database if it doesn’t exist. If it does, it tells Mongo to apply all following commands to this database.

Mongo stores documents in _collections_. Collections are like tables. To see existing collections, type:

```
show collections
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*F7W7VRj4bSehrwmItGo8Ww.jpeg)

For the cop, the username could be the badge-id too. You might add in a field for email address and one for password too (which won’t be revealed) for authentication purposes.

Go to this [link](https://raw.githubusercontent.com/booleanhunter/code-samples/master/blog-posts/how-to-build-your-own-uber-for-x-app/cops.json), and save the JSON data-set for cop related information.

To import data from this JSON file, type this in your terminal :

```
mongoimport --db myUberApp --collection policeData --drop --file ./path/to/jsonfile.json
```

Now, before you start querying your database, you need to learn a little on how _indexes_ in MongoDB (or any database for that matter) work.

An index is a special arrangement of data or data structure that allows you to query for information very efficiently. That way you can quickly retrieve results without having to scan across the entire database.

For example — let’s say you stored student related information in ascending order of their name in a book, which means that you have an index on the name field. That way, if you had to fetch information of a person named _Tyrion_, you can quickly locate his information without going through the rest of the students first.

But if you saved the same information in ascending order of their height, then querying information for a person using their name would become difficult. It could take lot of time, because now the students are not saved in order of their names, so you might have to scan and search across multiple rows.

But other kind of queries become possible. For example, fetch information of students whose heights lie between 4 and 5 feet. In which case _Tyrion’s_ info could be retrieved quickly, because:

![Image](https://cdn-media-1.freecodecamp.org/images/1*0YhfgYNBAXv4aLHuovNd3g.png)

Different databases support different types of indexes. You could read on the complete list of indexes that supports MongoDB [here](https://docs.mongodb.com/v3.2/indexes/).

So, now if you type this command:

```
 db.policeData.find().pretty()
```

which will return you all the documents that exist inside the _policeData_ collection — which is the entire list of cops. (The _pretty_ function makes the output easier to read).

If you want to fetch information about a particular cop whose _userId_ is _01_, you can type out `db.policeData.find({userId: “01”}).pretty()`

```javascript
{
    "_id" : ObjectId("57e75af5eb1b8edc94406943"),
    "userId" : "01",
    "displayName" : "Cop 1",
    "phone" : "01",
    "email" : "cop01@gmail.com",
    "earnedRatings" : 21,
    "totalRatings" : 25,
    "location" : {
        "type" : "Point",
        "address" : "Kalyan Nagar, Bengaluru, Karnataka 560043, India",
        "coordinates" : [
            77.63997110000003,
            13.0280047
        ]
    }
}
```

#### **Using MongoDB geospatial indexes**

Geospatial indexes allow you to store [GeoJSON](http://geojson.org/) objects within documents.

GeoJSON objects can be of different [types](https://docs.mongodb.com/manual/reference/geojson/#overview), such as _Point, LineString_ and _Polygon._

If you observe the output of your _.find()_ command, you’ll notice that every _location_ is an object which has the _type_ field and the _coordinates_ field within it. This is important, because if you store your GeoJSON object as a _Point_ type, you can use the [$near](https://docs.mongodb.com/manual/reference/operator/query/near/) command to query for points within certain proximity for a given longitude and latitude.

To use this, you need to create a [_2dsphere_](https://docs.mongodb.com/v3.2/core/2dsphere/) index (which is a geospatial index) on the _location_ field, and have a _type_ field within it. The _2dsphere_ index supports queries that calculate geometries on an earth-like sphere. This includes MongoDB geospatial queries: queries for inclusion, intersection and proximity.

So type this in your mongo shell:

```
db.policeData.createIndex({"location": "2dsphere"})
```

Now, to fetch documents from nearest to furthest from a given pair of co-ordinates, you need to issue a command with this syntax :

```javascript
db.<collectionName>.find({
    <fieldName>: {
        $near: {
            $geometry: {
                type: "Point",
                coordinates: [<longitude>, <latitude>]
            },
            $minDistance: <distance in metres>,
            $maxDistance: <distance in metres>
        }
    }
}).pretty()
```

$minDistance and $maxDistance are optional fields. Now, to get all cops that are located within 2 kilometers from _latitude 12.9718915_ and _longitude 77.64115449999997,_ run this :

```javascript
db.policeData.find({
    location: {
        $near: {
            $geometry: {
                type: "Point",
                coordinates: [77.64115449999997, 12.9718915]
            },
            $maxDistance: 2000
        }
    }
}).pretty()
```

And that’s it — you’ll find a list of documents returned in the output!

Perfect! Now let’s try doing the same with a web server. Download this [package.json](https://github.com/booleanhunter/code-samples/blob/master/blog-posts/how-to-build-your-own-uber-for-x-app/package.json) file and save it in the root of your project folder (make sure you named it _package.json_), and then in your terminal, _cd_ to the directory that contains the file and run

```
sudo npm install
```

A brief explanation about some of the packages that you’re going to use :

* [Express](https://expressjs.com/) is a web framework for NodeJS. It has lots of APIs, utilities and middlewares in its ecosystem to help you build your application.
* [body-parser](https://github.com/expressjs/body-parser) parses incoming request bodies in a middleware before your handlers, available under the _req.body_ property. You need this so you can handle POST requests.
* [underscore](http://underscorejs.org/) makes writing JavaScript simpler. Feel free to use another library if you prefer.
* [socket.io](http://socket.io) lets you use web sockets within your Node application.
* [mongodb](https://www.npmjs.com/package/mongodb) is the official NodeJS driver for MongoDB. It helps your Node app talk to your database.

The package.json file contains other modules as well. You’ll need them while building a complete app, but I’ll focus on how to use the _mongodb_ driver in your express app to execute queries. Here’s what some of the other modules do :

* [async](https://www.npmjs.com/package/async) is a utility for dealing with asynchronous code in NodeJS. It helps you avoid callback hell.
* [debug](https://www.npmjs.com/package/debug) is a debugging library. This handy tool helps debug your programs without the use of ugly _console.log_ statement outputs.
* [redis](https://www.npmjs.com/package/redis) is similar to the _mongodb_ driver. It lets your NodeJS app talk to your Redis database.
* [connect-redis](https://www.npmjs.com/package/connect-redis) is a session store that uses Redis to manage sessions. You’ll need this later when you decide to have user accounts.

Before you write code, it’ll be helpful to organize it first. For now, you can use two files:

* A file for writing your API endpoints
* A file that uses database drivers for database related operations. The route-handler would decide which function to call from the database file. Once a query is performed, the results are returned back to your route-handler with the help of a callback function.

Let’s see how this looks like when you write your code:

```javascript
var http = require("http");
var express = require("express");
var consolidate = require("consolidate");//1
var _ = require("underscore");
var bodyParser = require('body-parser');

var routes = require('./routes'); //File that contains our endpoints
var mongoClient = require("mongodb").MongoClient;

var app = express();
app.use(bodyParser.urlencoded({
   extended: true,
}));
             
app.use(bodyParser.json({limit: '5mb'}));

app.set('views', 'views'); //Set the folder-name from where you serve the html page. 
app.use(express.static('./public')); //setting the folder name (public) where all the static files like css, js, images etc are made available

app.set('view engine','html');
app.engine('html',consolidate.underscore);
var portNumber = 8000; //for locahost:8000

http.createServer(app).listen(portNumber, function(){ //creating the server which is listening to the port number:8000, and calls a function within in which calls the initialize(app) function in the router module
	console.log('Server listening at port '+ portNumber);
	
	var url = 'mongodb://localhost:27017/myUberApp';
	mongoClient.connect(url, function(err, db) { //a connection with the mongodb is established here.
		console.log("Connected to Database");
		routes.initialize(app, db); //function defined in routes.js which is exported to be accessed by other modules
	});
});

/* 1. Not all the template engines work uniformly with express, hence this library in js, (consolidate), is used to make the template engines work uniformly. Altough it doesn't have any 
modules of its own and any template engine to be used should be seprately installed!*/

```

In this example, you create a new instance of the _MongoClient_ object from the _mongodb_ module. Once the web server begins, you connect to your MongoDB database using the _connect_ function that’s exposed by your _MongoClient_ instance. After it initializes the connection, it returns a _Db_ instance in the callback.

You can now pass both the _app_ and _db_ instances to the _initialize_ function of your _routes.js_ file.

Next, you need to create a new file called _routes.js_, and add this code:

```js
function initialize(app, db) { 
    //A GET request to /cops should return back the nearest cops in the vicinity.
    app.get('/cops', function(req, res){
    /*extract the latitude and longitude info from the request. Then, fetch the nearest cops using MongoDB's geospatial queries and return it back to the client.
    */
    });
}
exports.initialize = initialize;
```

For this to work, you’ll have to pass the coordinates as query strings in your request. You’ll also write your database operations in another file. So go ahead and create a new file _db-operations.js,_ and write this:

```javascript
function fetchNearestCops(db, coordinates, callback) {
    db.collection('policeData').createIndex({
        "location": "2dsphere"
    }, function() {
        db.collection("policeData").find({
            location: {
                $near: {
                    $geometry: {
                        type: "Point",
                        coordinates: coordinates
                    },
                    $maxDistance: 2000
                }
            }
        }).toArray(function(err, results) {
            if(err) {
                console.log(err)
            }else {
                callback(results);
            }
        });
    });
}
exports.fetchNearestCops = fetchNearestCops;
```

This function accepts three arguments: an instance of _db_, an array that contains co-ordinates in the order [<longitude>,<latitude>], and a callback function, to which it returns the results of your query.

The _createIndex_ ensures that an index is created on the specified field if it doesn’t exist, so you may want to skip that if you have already created an index prior to querying.

Now, all that’s left to do is to call this function inside your handler. So modify your _routes.js_ code to this:

```javascript
var dbOperations = require('./db-operations');
function initialize(app, db) {
    // '/cops?lat=12.9718915&&lng=77.64115449999997'
    app.get('/cops', function(req, res){
        //Convert the query strings into Numbers
        var latitude = Number(req.query.lat);
        var longitude = Number(req.query.lng);
        dbOperations.fetchNearestCops(db, [longitude,latitude], function(results){
        //return the results back to the client in the form of JSON
            res.json({
                cops: results
            });
        });  
    });
}
exports.initialize = initialize;
```

And that’s it! Run

```
node app.js 
```

from your terminal, then open your browser and hit [http://localhost:8000/cops?lat=12.9718915&&lng=77.64115449999997](http://localhost:8000/cops?lat=12.9718915&&lng=77.64115449999997)

Depending on the query strings that you passed, you should either get a JSON response containing an empty array or an array containing cop data!

This is the end of Part 1. In [Part 2](https://medium.freecodecamp.com/how-to-build-your-own-uber-for-x-app-part-2-8ba6ffa2573d), you’ll take it up a notch and try to send a distress signal to nearby cops. Then you’ll figure out how a cop could respond back to the signal using socket.io. You’ll also see how to display the location of the citizen on a map.

In the meantime do have a look at the [source code](https://github.com/booleanhunter/how-to-build-your-own-uber-for-x-app) on GitHub!

![Image](https://cdn-media-1.freecodecamp.org/images/1*aoUgLA_yDneLrALRQHYqUw.png)

If you liked this article, please consider supporting me on Patreon.

<a href="https://www.patreon.com/bePatron?u=20804433" data-patreon-widget-type="become-patron-button">Become a Patron!</a><script async src="https://c6.patreon.com/becomePatronButton.bundle.js"></script>

You should totally [subscribe](https://www.freecodecamp.org/news/how-to-build-your-own-uber-for-x-app-33237955e253/forum.booleanhunter.com). I won't waste your time.

**Many thanks to [Quincy Larson](https://medium.com/@quincylarson) for helping me make this article better.**

> Featured in [Mybridge](https://medium.mybridge.co/)’s [Top Ten NodeJS articles from October 2016](https://medium.mybridge.co/node-js-top-ten-articles-from-october-fbde1ebe7785#.fnr9w51pr) and [Top Ten NodeJS articles of the year (v.2017)](https://medium.mybridge.co/node-js-top-10-articles-of-the-year-v-2017-79df8269d0f3#.f82p1dork)

