---
title: How to create a custom fetch API from XMLHttpRequest
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-24T08:18:41.000Z'
originalURL: https://freecodecamp.org/news/create-a-custom-fetch-api-from-xmlhttprequest-2cad1b84f07c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*XXsfkhk3zt2Y70p2FFeutQ.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: Software Engineering
  slug: software-engineering
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Samuel Omole

  What is your worst nightmare?

  That sounded dark, but it’s not a rhetorical question. I really want to know because
  I am about to tell you mine. Along the way, we will learn some things like how the
  fetch API works and also how functio...'
---

By Samuel Omole

What is your worst nightmare?

That sounded dark, but it’s not a rhetorical question. I really want to know because I am about to tell you mine. Along the way, we will learn some things like how the fetch API works and also how function constructors work.

Sorry I digress, back to my worst nightmare. If you had asked me that question last week it would be the below list in no particular order:

* Writing Pre-ES6 syntax
* No fetch API
* No Transpiler (Babel/Typescript)
* [Uncle Bob](https://en.wikipedia.org/wiki/Robert_C._Martin) said that I’m a disappointment (Kidding)

If your list matches mine then I have to say that you are a very weird person. As luck would have it I was called to work on a project that brought to life my nightmare list (excluding the last one). I was to add a new feature to the application. It was a legacy codebase that used purely pre-es6 syntax and XMLHttpRequest (the horror) for its AJAX requests.

So in a bid to make the experience palatable, I decided to create a function that abstracts all the AJAX requests I would be making and expose APIs that mimics the new [fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API) (well not really). This is also after I watched the [Javascript: The new hard parts](https://frontendmasters.com/courses/javascript-new-hard-parts/) video on frontend masters where an amazing explanation of how the fetch API works under the hood was given. Let’s begin.

First, I had to look up how [XMLHttpRequest](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest) works. Then I started writing the function. My first iteration looked like this:

```javascript
"use strict";


function fetch() {
  var url = arguments.length > 0 && arguments[0] !== undefined ? arguments[0] : '';
  var options = arguments.length > 1 && arguments[1] !== undefined ? arguments[1] : {};

var xhr = new XMLHttpRequest();
  var onFufillment = [];
  var onError = [];
  var onCompletion = [];
  var method = "GET" || options.method;
  xhr.onreadystatechange = function () {
    var _data = this;
    if (this.readyState == 4 && this.status == 200) {
      // Action to be performed when the document is read;
      onFufillment.forEach(function (callback) {
          callback(_data);
      });
     onCompletion.forEach(function (callback) {
        callback(_data);
      });
    } else if (this.readyState == 4 && this.status !== 200) {
      onError.forEach(function (callback) {
        callback(_data);
      });
      onCompletion.forEach(function (callback) {
        callback(_data);
      });
    }
  };
  xhr.open(method, url, true);
  xhr.send();


return {
    then: function then(fufillmentFunction) {
      onFufillment.push(fufillmentFunction);
    },
    catch: function _catch(errorFunction) {
      onError.push(errorFunction);
    },
    finally: function _finally(completionFunction) {
      onCompletion.push(completionFunction);
    }
  };
}
```

Let me work through what the function does:

* We are checking if the `url` argument is passed into the function. Defaulting to an empty string if nothing is passed
* We are also doing the same thing for the `options` argument. Defaulting to an empty object if nothing is passed
* Then we create a new instance of the XMLHttpRequest
* We create 4 variables `onFufillment, onError, onCompletion and method`
* `onFufillment` is an array that stores all the functions passed into the `then` method
* `onError` is an array that stores all the functions passed into the `catch` method
* `onCompletion` is an array that stores all the functions passed into the `finally` method
* `method` is used to store the HTTP method that will be used, it defaults to `GET`
* We then pass a function into the `onreadystatechange` method of `xhr` which will be called when the state of the request changes
* In the function, we save `this` into a `_data` variable so that it can be passed into the forEach functions without losing its context (I know `this` is annoying)
* We then check if the request is completed (`readyState == 4` ) and if the request is successful, then we loop through `onFufillment and onCompletion` arrays, calling each function and passing `_data` into it
* If the request fails we do the same thing with the `onCompletion and onError` arrays
* Then we send off the request with the passed in parameters
* After that, we return an object containing three functions, then. `catch and finally` which have the same names as the fetch API.
* `catch` pushes the function that is passed as an argument into the `onError` array
* `then` does the same thing with the `onFufillment` array
* `finally` does the same with the `onCompletion` array

The usage of this API will look like this:

```javascript
var futureData = fetch('https://jsonplaceholder.typicode.com/todos/2');
futureData.then(function(data){
  console.log(data)
})

futureData.finally(function(response){
  console.log(response);
});

futureData.catch(function(error){
  console.log(error);
})
```

It works!!! But not nearly as the real fetch implementation. Can we do better than this? Of course, we can. We can still add more features to the function. We could make it chainable, that is, we can give it the ability to chain methods together.

On the second iteration, this is how it looks:

```javascript
"use strict";

function fetch() {
  var url = arguments.length > 0 && arguments[0] !== undefined ? arguments[0] : '';
  var options = arguments.length > 1 && arguments[1] !== undefined ? arguments[1] : {};
var xhr = new XMLHttpRequest();
  var onFufillment = [];
  var onError = [];
  var onCompletion = [];
  var method = "GET" || options.method;
  xhr.onreadystatechange = function () {
    var _data = this;
    if (this.readyState == 4 && this.status == 200) {
      // Action to be performed when the document is read;
      onFufillment.forEach(function (callback) {
          callback(_data);
      });
     onCompletion.forEach(function (callback) {
        callback(_data);
      });
    } else if (this.readyState == 4 && this.status !== 200) {
      onError.forEach(function (callback) {
        callback(_data);
      });
      onCompletion.forEach(function (callback) {
        callback(_data);
      });
    }
  };
  xhr.open(method, url, true);
  xhr.send();


	return {
    	then: function then(fufillmentFunction) {
          onFufillment.push(fufillmentFunction);
          return this;
   		},
    	catch: function _catch(errorFunction) {
      	  onError.push(errorFunction);
      	  return this;
      },
        finally: function _finally(completionFunction) {
         onCompletion.push(completionFunction);
         return this;
    }
  };
}
```

The usage of the API will look like this:

```javascript
var futureData = fetch('https://jsonplaceholder.typicode.com/todos/2');


futureData.then(function(data){
  console.log(data)
}).then(function(response){
  console.log(response);
}).catch(function(error){
  console.log(error);
});
```

What did it do? The only difference in the second iteration was in the `then, catch and finally` where I just returned `this` which means each function returns itself basically enabling it to be chained (partially).

Better right? But can we do better than this? Of course, we can. The returned object can be put in the function's prototype so that we can save memory in a situation where the function is used multiple times.

This is how it looks on the third iteration:

```javascript
"use strict";
function fetch() {
  var fetchMethod = Object.create(fetch.prototype);
  var url = arguments.length > 0 && arguments[0] !== undefined ? arguments[0] : '';
  var options = arguments.length > 1 && arguments[1] !== undefined ? arguments[1] : {};
var xhr = new XMLHttpRequest();
  fetchMethod.onFufillment = [];
  fetchMethod.onError = [];
  fetchMethod.onCompletion = [];
  var method = "GET" || options.method;
  xhr.onreadystatechange = function () {
    var _data = this;
    if (this.readyState == 4 && this.status == 200) {
      // Action to be performed when the document is read;
      fetchMethod.onFufillment.forEach(function (callback) {
          callback(_data);
      });
     fetchMethod.onCompletion.forEach(function (callback) {
        callback(_data);
      });
    } else if (this.readyState == 4 && this.status !== 200) {
      fetchMethod.onError.forEach(function (callback) {
        callback(_data);
      });
      fetchMethod.onCompletion.forEach(function (callback) {
        callback(_data);
      });
    }
  };
  xhr.open(method, url, true);
  xhr.send();
  return fetchMethod;
};
fetch.prototype.then = function(fufillmentFunction) {
      this.onFufillment.push(fufillmentFunction);
      return this;
};
fetch.prototype.catch = function(errorFunction) {
      this.onError.push(errorFunction);
      return this;
};
fetch.prototype.finally = function(completionFunction) {
      this.onCompletion.push(completionFunction);
      return this;
};
```

So this version basically moves the returned function into the fetch’s prototype. If you don’t understand the statement then I recommend checking out this article about [Javascript’s prototype](https://dev.to/tylermcginnis/a-beginners-guide-to-javascripts-prototype-5kk) (Thanks, Tyler McGinnis).

Is this an improvement? Yes!!! Can we do better? Of course, we can. We can use the `new` keyword to our advantage here and remove the explicit return statement.

The next iteration will look like this:

```javascript
"use strict";
function Fetch() {
  var url = arguments.length > 0 && arguments[0] !== undefined ? arguments[0] : '';
  var options = arguments.length > 1 && arguments[1] !== undefined ? arguments[1] : {};
  var xhr = new XMLHttpRequest();
  this.onFufillment = [];
  this.onError = [];
  this.onCompletion = [];
  var method = "GET" || options.method;
  var internalFetchContext = this;
  xhr.onreadystatechange = function () {
    var _data = this;
    if (this.readyState == 4 && this.status == 200) {
      // Action to be performed when the document is read;
      internalFetchContext.onFufillment.forEach(function (callback) {
          callback(_data);
      });
     internalFetchContext.onCompletion.forEach(function (callback) {
        callback(_data);
      });
    } else if (this.readyState == 4 && this.status !== 200) {
      internalFetchContext.onError.forEach(function (callback) {
        callback(_data);
      });
      internalFetchContext.onCompletion.forEach(function (callback) {
        callback(_data);
      });
    }
  };
  xhr.open(method, url, true);
  xhr.send();
};
Fetch.prototype.then = function(fufillmentFunction) {
      this.onFufillment.push(fufillmentFunction);
      return this;
};
Fetch.prototype.catch = function(errorFunction) {
      this.onError.push(errorFunction);
      return this;
};
Fetch.prototype.finally = function(completionFunction) {
      this.onCompletion.push(completionFunction);
      return this;
};
```

Let me explain the changes:

* Changed the name of the function from fetch to Fetch, it’s just a convention when using the `new` keyword
* Since I am using the `new` keyword I can then save the various arrays created to the `this` context.
* Because the function passed into `onreadystatechange` has its own context I had to save the original `this` into its own variable to enable me to call it in the function (I know, `this` can be annoying)
* Converted the prototype functions to the new function name.

The usage will look like this:

```javascript
var futureData = new 

Fetch('https://jsonplaceholder.typicode.com/todos/1');
futureData.then(function(data){
  console.log(data)
}).then(function(response){
  console.log(response);
}).catch(function(error){
  console.log(error);
})
```

Voilà! That was really fun. But can we do better? Of course, we can.

But I will leave that to you. I would love to see your own implementation of the API in the comments below.

If you liked the article (and even if you didn’t), I would appreciate a clap (or 50) from you. Thank you.

