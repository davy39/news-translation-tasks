---
title: What is a JSON File? Example JavaScript Code
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2021-08-25T20:04:19.000Z'
originalURL: https://freecodecamp.org/news/what-is-a-json-file-example-javascript-code
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/json.png
tags:
- name: api
  slug: api
- name: JavaScript
  slug: javascript
- name: json
  slug: json
seo_title: null
seo_desc: "JSON stands for JavaScript Object Notation. A JSON file has .json as its\
  \ extension and the data inside are represented in a key:value pair, just like a\
  \ traditional JavaScript object. \nJSON and objects aren't exactly the same, though.\
  \ The core differe..."
---

JSON stands for JavaScript Object Notation. A JSON file has .json as its extension and the data inside are represented in a key:value pair, just like a traditional JavaScript object. 

JSON and objects aren't exactly the same, though. The core difference is that the key in JSON must be in double-quotes, and the values apart from the number and null types must be in double-quotes, too.

If you have worked with APIs during your programming journey, you likely know what JSON is, because a lot of API data now comes in JSON format. 

If you have not worked with APIs before and you're an absolute beginner, you're not alone. 

In this article, I'm going to walk you through what JSON is all about and how you can make the best use of it.

## Basic JSON Syntax

```js
{
  "key1": "value1",
  "key2": "value2",
  "key3": "value3",
  "key4": 7,
  "key5": null,
  "favFriends": ["Kolade", "Nithya", "Dammy", "Jack"],
  "favPlayers": {"one": "Kante", "two": "Hazard", "three": "Didier"}
}
```

## Accepted JSON Data Types

JSON can be defined in an object or an array, which might take in several objects. So, objects and arrays are automatically acceptable data types in JSON. Other data types that it supports are boolean, null, and string. 

Data types such as undefined, function, and date are not supported by JSON.

In addition, JSON can also be extended into other data formats which might accept extra data types that raw JSON does not accept. 

Examples of such extensions are GeoJSON and BSON. GeoJSON is used to represent Geographical data while BSON is used by the popular database service provider MongoDB.

BSON, for example, accepts regular expressions, dates, and timestamps as data types, which JSON does not accept.

## JSON Syntax Rules

JSON is very strict when it comes to its supported data types. If you have a linter installed in your code editor, it immediately lets you know there's an error any time you input an unsupported data type or go against the syntax rules.

### JSON syntax rules to know:

- All the data in the file must be surrounded by curly braces if you're representing it as an object, and in square brackets if it is an array.
- Single quotes are not allowed
- The key in each JSON must be unique and must be in double quotes
- Numbers must not be enclosed in double-quotes, otherwise they will be treated as strings.
- The null data type must not be enclosed in double-quotes.
- Boolean values can only be true or false.
- Each key:value pair must be terminated with a comma except for the last item
- A particular object inside an array must be terminated by a comma, too.

## How JSON Data is Sent to the Client (Browser)

JSON was created out of the need to send data from the server (a database, for example) to the client (browsers) in real-time. 

But JSON data can't be transmitted to the browser in its raw key:value pair form, so programming languages have methods for manipulating JSON data. 

In JavaScript, for example, `JSON.parse()` converts JSON data to objects and `JSON.stringify()` converts an object's key:value pair to JSON data. 

Python provides methods such as `json.loads()` for converting an existing string to JSON, and `json.dumps()` to convert an object to a JSON string.

You can send the data in the basic JSON syntax to the browser by using the two methods JavaScript provides. 

### How to Send JSON Data to the Client (Browser) with JavaScript

The `JSON.stringify()` method returns a JSON string that is exactly the same as a JavaScript object. You can use it in combination with DOM manipulation methods to display JSON data in the browser, as I have done in the code snippets below:

```html
<h2>Here is the Data from the JSON:</h2> 
<div id="json"></div>
```

```js
 const JSONData = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
    "key4": 7,
    "key5": null,
    "favFriends": ["Kolade", "Nithya", "Dammy", "Jack"],
    "favPlayers": {"one": "Kante", "two": "Hazard", "three": "Didier"}
}

const JSONString = JSON.stringify(JSONData)
const JSONDisplay = document.querySelector("#json")
JSONDisplay.innerHTML = JSONString
```

In the JavaScript code, we declared the JSON data as an object literal with the identifier (name) `JSONData`. We used JavaScript’s `JSON.stringify()` method to turn it into a string, and the DOM’s query selector method to get the empty div in the HTML. This makes it possible to populate the JSON data in it with the `innerHTML` DOM manipulation method.

![json-stringify-method](https://www.freecodecamp.org/news/content/images/2021/08/json-stringify-method.png)

We can use the `JSON.parse()` method to turn a JSON data to an object – and here it is in action:

```html
<h2>Here is the Data from the JSON:</h2>
<div id="json"></div>
```

```js
const JSONData =
     '{"name": "Kolade", "favFriends": ["Kolade", "Nithya", "Rocco", "Jack"], "from": "Africa"}';

   try {
     const JSONString = JSON.parse(JSONData);
     const JSONDisplay = document.querySelector("#json");
     JSONDisplay.innerHTML = JSONString.name + ", [" + JSONString.favFriends + "], " + JSONString.from;
   } catch (error) {
     console.log("Cannot parse the JSON Data");
   }
```

The resulting output in the browser looks like this: 
![json-parse-method](https://www.freecodecamp.org/news/content/images/2021/08/json-parse-method.png)

## Conclusion

As a programmer, you can't do without JSON. Most APIs are now written in JSON instead of XML. 

JSON was initially intended for JavaScript, but a lot of other programming languages now support it thanks to its language-independent nature. As a result, many languages have libraries for working with it.

I hope this tutorial has given you the insights you need to work with JSON so you can put it into proper use any time you encounter it.

Thank you for reading, and keep coding.



