---
title: How to Write Regular Expressions in a JSON File
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2023-04-24T12:38:59.000Z'
originalURL: https://freecodecamp.org/news/how-to-write-regular-expression-in-json-file
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/start-graph--11-.png
tags:
- name: json
  slug: json
- name: Regex
  slug: regex
seo_title: null
seo_desc: 'JSON stands for JavaScript Object Notation. It is a text-based and lightweight
  data format for exchanging information between systems, for example, a web server
  and a web application.

  JSON files typically contain objects, arrays, strings, and numbers...'
---

JSON stands for JavaScript Object Notation. It is a text-based and lightweight data format for exchanging information between systems, for example, a web server and a web application.

JSON files typically contain objects, arrays, strings, and numbers. But you can also have regular expressions in a JSON file. And that’s what we are going to take a look at in this article.


## How to Write RegEx inside JSON
Remember each entry in a JSON file is a `key:value` pair surrounded by double quotes. So, if you want to write RegEx inside your JSON file, you need to specify the key and the value and surrounded both with double quotes. 

The key can just be an arbitrary name, and the value would be the regex itself. Here’s an example of a JSON file with regular expressions:

```js
// data.json file

{
  "nigeriaPhone": "^(\\+?234|0)[789]\\d{9}$",
  "email": "^([a-zA-Z0-9_\\-\\.]+)@([a-zA-Z0-9_\\-\\.]+)\\.([a-zA-Z]{2,5})$",
  "password": "^(?=.*[0-9])(?=.*[!@#\\$%^&*])[a-zA-Z0-9!@#\\$%^&*]{8,}$",
  "url": "^(http|https)://[a-zA-Z0-9-\\.]+\\.[a-zA-Z]{2,5}(/[a-zA-Z0-9-._~:/?#[\\]@!$&'()*+,;=]*)?$"
}
```


Writing RegEx inside a JSON file can be useful when you want to use many regular expressions. 

Instead of littering your JavaScript, Python file, or any other programming files with regular expressions, you can put all of them inside a JSON file. You can then import the file into your programming language file and use the regular expressions entries.

That takes us to how to use a JSON file inside a programming language. Specifically, we’ll look at how to do that in JavaScript.


## How to use a JSON RegEx in a JavaScript File
To use the RegEx from your JSON file inside a JavaScript file, you need to import it first. 

An ordinary `import something from somefile` won't work if you want to import JSON into a JS file. This is the correct way to do it:

```bash
import someName from 'location/file.json' assert { type: 'json' };
```

So, I'm going to import the JSON file like this:

```js
import validators from './data.json' assert { type: 'json' };
```

In this case, I’m importing all the entries from the `data.json` file and naming them `validators`. This name can be anything. 

The `assert { type:  'json'}` part ensures that what I’m bringing in is a JSON object.

You can then chain any of the keys from the JSON file to `validators` to see what any of the entries look like:

```js
import validators from './data.json' assert { type: 'json' };

console.log(validators.nigeriaPhone); // ^(\+?234|0)[789]\d{9}$
console.log(validators.email); // ^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$
console.log(validators.password); // ^(?=.*[0-9])(?=.*[!@#\$%^&*])[a-zA-Z0-9!@#\$%^&*]{8,}$
console.log(validators.url); // ^(http|https)://[a-zA-Z0-9-\.]+\.[a-zA-Z]{2,5}(/[a-zA-Z0-9-._~:/?#[\]@!$&'()*+,;=]*)?$
```

You can even take this further and test what the regular expressions validate. Here’s how I validated a correct Nigerian phone number:

```js
import validators from './data.json' assert { type: 'json' };

const naijaNUmber = '+2348123456789';

if (naijaNUmber.match(validators.nigeriaPhone)) {
  console.log("That's a valid Naija phone number"); // That's a valid Naija phone number
} else {
  console.log("That's not a valid Naija phone number");
}
```

And here’s how I used the `password` key to validate a password that is at least eight characters long and contains at least one number and at least one special character:

```js
import validators from './data.json' assert { type: 'json' };

const pword = 'JohnDoe';

if (pword.match(validators.password)) {
  console.log("That's Valid password");
} else {
  console.log(
    'Your password must be 8 characters long with at least 1 number and 1 special character'
  ); // Your password must be 8 characters long with at least 1 number and 1 special character
}
```

Unfortunately, in some situations, you get an error if you decide to use the JSON regex directly without creating a regex out of it. Here’s an example with `test()`:

```js
import validators from './data.json' assert { type: 'json' };

const naijaPhone = validators.nigeriaPhone;
console.log(naijaPhone); // Output: ^(\+?234|0)[789]\d{9}$

console.log(naijaPhone.test(83412343433));

/* output: dex.js:4 Uncaught TypeError: naijaPhone.test is not a function
    at index.js:4:24
*/
```

You can see that the output does not show it as a regular expression – it is not surrounded by forward slashes. This means you have to create a regex out of it with the regex constructor:

```js
import validators from './data.json' assert { type: 'json' };

const naijaPhone = validators.nigeriaPhone;
console.log(naijaPhone); // Output: ^(\+?234|0)[789]\d{9}$

// Create a regex out of validators.nigeriaPhone;
const naijaNumberRegex = new RegExp(naijaPhone);
console.log(naijaNumberRegex); // Output: /^(\+?234|0)[789]\d{9}$/
```

You can see it is now surrounded by forward slashes – that’s a way to identify and even create regex in JavaScript.

Here's how the chrome developer tools distinguishes the two:

![Screenshot-2023-04-24-at-12.22.56](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-24-at-12.22.56.png)

It is with that regex you created that you can test the number:
```js
import validators from './data.json' assert { type: 'json' };

const naijaPhone = validators.nigeriaPhone;
console.log(naijaPhone); // Output: ^(\+?234|0)[789]\d{9}$

// Create a regex out of validators.nigeriaPhone;
const naijaNumberRegex = new RegExp(naijaPhone);
console.log(naijaNumberRegex); // Output: /^(\+?234|0)[789]\d{9}$/

// test it out with the regex
console.log(naijaNumberRegex.test(83412343433)); // output: false
console.log(naijaNumberRegex.test(2348033333333)); // output: true
```


The reason why it worked with the `match()` method and didn’t work with `test()` is this:

* when you use the `match()` method, you can directly pass the regular expression string that you read from a JSON file as an argument to the method, and JavaScript will automatically create a regular expression from the string.

* when you use the `test()` method, you need to manually create a regular expression from the regular expression string using the `new RegExp()` constructor. This is because the `test()` method expects a regular expression object as its argument, not a string.


## Conclusion
You’ve seen that there’s no extra caveat involved in writing regular expressions in a JSON file – you still have to follow the same rules for writing JSON.

And when you import that JSON file into a JavaScript file, you don’t need to do anything extra to make it work, other than creating a regex out of it with the `new RegExp()` constructor in some cases.

Thank you for reading!


