---
title: JSON for Beginners – JavaScript Object Notation Explained in Plain English
subtitle: ''
author: Tapas Adhikary
co_authors: []
series: null
date: '2021-11-29T19:16:16.000Z'
originalURL: https://freecodecamp.org/news/what-is-json-a-json-file-example
coverImage: https://www.freecodecamp.org/news/content/images/2021/11/freeCodeCamp-Cover-1.png
tags:
- name: beginners guide
  slug: beginners-guide
- name: JavaScript
  slug: javascript
- name: json
  slug: json
seo_title: null
seo_desc: "Many software applications need to exchange data between a client and server.\
  \ \nFor a long time, XML was the preferred data format when it came to information\
  \ exchange between the two points. Then in early 2000, JSON was introduced as an\
  \ alternate dat..."
---

Many software applications need to exchange data between a client and server. 

For a long time, XML was the preferred data format when it came to information exchange between the two points. Then in early 2000, JSON was introduced as an alternate data format for information exchange.

In this article, you will learn all about JSON. You'll understand what it is, how to use it, and we'll clarify a few misconceptions. So, without any further delay, let's get to know JSON.

## What is JSON?

JSON (**J**ava**S**cript **O**bject **N**otation) is a `text-based` data exchange format. It is a collection of key-value pairs where the key must be a string type, and the value can be of any of the following types:

* Number
* String
* Boolean
* Array
* Object
* null

A couple of important rules to note:

* In the JSON data format, the keys must be enclosed in double quotes.
* The key and value must be separated by a colon (:) symbol.
* There can be multiple key-value pairs. Two key-value pairs must be separated by a comma (,) symbol.
* No comments (// or /* */) are allowed in JSON data. (But you can [get around that](https://www.freecodecamp.org/news/json-comment-example-how-to-comment-in-json-files/), if you're curious.)

Here is how some simple JSON data looks:

```js
{
    "name": "Alex C",
    "age": 2,
    "city": "Houston"
}
```

Valid JSON data can be in two different formats:

* A collection of key-value pairs enclosed by a pair of curly braces `{...}`. You saw this as an example above.
* A collection of an ordered list of key-value pairs separated by comma (,) and enclosed by a pair of square brackets `[...]`. See the example below:

```js
[
	{
        "name": "Alex C",
        "age": 2,
        "city": "Houston"
	},
    {
        "name": "John G",
        "age": 40,
        "city": "Washington"
	},
    {
        "name": "Bala T",
        "age": 22,
        "city": "Bangalore"
	}
]
```

Suppose you are coming from a JavaScript developer background. In that case, you may feel like the JSON format and JavaScript objects (and array of objects) are very similar. But they are not. We will see the differences in detail soon.

The structure of the JSON format was derived from the JavaScript object syntax. That's the only relationship between the JSON data format and JavaScript objects.

JSON is a programming language-independent format. We can use the JSON data format in Python, Java, PHP, and many other programming languages.

## JSON Data Format Examples 

You can save JSON data in a file with the extension of `.json`. Let's create an `employee.json` file with attributes (represented by keys and values) of an employee.

```js
{
	"name": "Aleix Melon",
	"id": "E00245",
	"role": ["Dev", "DBA"],
	"age": 23,
	"doj": "11-12-2019",
	"married": false,
	"address": {
		"street": "32, Laham St.",
		"city": "Innsbruck",
		"country": "Austria"
	},
	"referred-by": "E0012"
}
```

The above JSON data shows the attributes of an employee. The attributes are:

* `name`: the name of the employee. The value is of `String` type. So, it is enclosed with double quotes.
* `id`: a unique identifier of an employee. It is a `String` type again.
* `role`: the roles an employee plays in the organization. There could be multiple roles played by an employee. So `Array` is the preferred data type.
* `age`: the current age of the employee. It is a `Number`.
* `doj`: the date the employee joined the company. As it is a date, it must be enclosed within double-quotes and treated like a `String`.
* `married`: is the employee married? If so, true or false. So the value is of `Boolean` type.
* `address`: the address of the employee. An address can have multiple parts like street, city, country, zip, and many more. So, we can treat the address value as an `Object` representation (with key-value pairs).
* `referred-by`: the id of an employee who referred this employee in the organization. If this employee joined using a referral, this attribute would have value. Otherwise, it will have `null` as a value.

Now let's create a collection of employees as JSON data. To do that, we need to keep multiple employee records inside the square brackets [...].

```js
[
	{
        "name": "Aleix Melon",
        "id": "E00245",
        "role": ["Dev", "DBA"],
        "age": 23,
        "doj": "11-12-2019",
        "married": false,
        "address": {
            "street": "32, Laham St.",
            "city": "Innsbruck",
            "country": "Austria"
            },
        "referred-by": "E0012"
	},
    {
        "name": "Bob Washington",
        "id": "E01245",
        "role": ["HR"],
        "age": 43,
        "doj": "10-06-2010",
        "married": true,
        "address": {
            "street": "45, Abraham Lane.",
            "city": "Washington",
            "country": "USA"
            },
        "referred-by": null
	}
]
```

Did you notice the `referred-by` attribute value for the second employee, Bob Washington? It is `null`. It means he was not referred by any of the employees.

## How to Use JSON Data as a String Value

We have seen how to format JSON data inside a JSON file. Alternatively, we can use JSON data as a string value and assign it to a variable. As JSON is a text-based format, it is possible to handle as a string in most programming languages. 

Let's take an example to understand how we can do it in JavaScript. You can enclose the entire JSON data as a string within a single quote `'...'`.

```js
const user = '{"name": "Alex C", "age": 2, "city": "Houston"}';
```

If you want to keep the JSON formatting intact, you can create the JSON data with the help of template literals.

```js
const user = `{
    "name": "Alex C",
    "age": 2,
    "city": "Houston"
}`;

```

It is also useful when you want to build JSON data using dynamic values.

```js
const age = 2;

const user = `{
    "name": "Alex C",
    "age": ${age},
    "city": "Houston"
}`;

console.log(user);

// Output
{
    "name": "Alex C",
    "age": 2,
    "city": "Houston"
}
```

## JavaScript Objects and JSON are NOT the Same

The JSON data format is derived from the JavaScript object structure. But the similarity ends there. 

Objects in JavaScript:

* Can have methods, and JSON can't.
* The keys can be without quotes.
* Comments are allowed.
* Are JavaScript's own entity.

Here's a Twitter thread that explains the differences with a few examples.

%[https://twitter.com/tapasadhikary/status/1463493300225204225]

## How to Convert JSON to a JavaScript Object, and vice-versa

JavaScript has two built-in methods to convert JSON data into a JavaScript object and vice-versa.

### How to Convert JSON Data to a JavaScript Object

To convert JSON data into a JavaScript object, use the `JSON.parse()` method. It parses a valid JSON string into a JavaScript object.

```js

const userJSONData = `{
    "name": "Alex C",
    "age": 2,
    "city": "Houston"
}`;

const userObj = JSON.parse(userJSONData);
console.log(userObj);
```

Output:

![Image](https://www.freecodecamp.org/news/content/images/2021/12/first.png)
_The output_

### How to Convert a JavaScript Object to JSON Data

To convert a JavaScript object into JSON data, use the `JSON.stringify()` method.

```js
const userObj = {
    name: 'Alex C', 
    age: 2, 
    city: 'Houston'
}

const userJSONData = JSON.stringify(userObj);
console.log(userJSONData);
```

Output:

![Image](https://www.freecodecamp.org/news/content/images/2021/12/second.png)
_The output_

  
Did you notice the `JSON` term we used to invoke the `parse()` and `stringify()` methods above? That's a built-in JavaScript object named `JSON` (could have been named JSONUtil as well) but it's not related to the JSON data format we've discussed so far. So, please don't get confused.

## How to Handle JSON Errors like "Unexpected token u in JSON at position 1"?

While handling JSON, it is very normal to get an error like this while parsing the JSON data into a JavaScript object:

![Image](https://www.freecodecamp.org/news/content/images/2021/11/image-127.png)
_JSON Syntax Error_

Whenever you encounter this error, please question the validity of your JSON data format. You probably made a trivial error and that is causing it. You can validate the format of your JSON data using a [JSON Linter](https://jsonlint.com/).

## Before We End...

I hope you found the article insightful and informative. My DMs are open on Twitter if you want to discuss further. 

Recently I have published a few helpful tips for beginners to web development. You may want to have a look:

%[https://blog.greenroots.info/5-tips-for-beginners-to-web-development]

Let's connect. I share my learnings on JavaScript, Web Development, and Blogging on these platforms as well:

* [Follow me on Twitter](https://twitter.com/tapasadhikary)
* [Subscribe to my YouTube Channel](https://www.youtube.com/tapasadhikary?sub_confirmation=1)
* [Side projects on GitHub](https://github.com/atapas)

