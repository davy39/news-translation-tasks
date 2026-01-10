---
title: How to Use Regular Expressions in YAML File – RegEx in YAML Tutorial
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2023-05-17T14:48:51.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-regular-expressions-in-yaml-file
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/yamlRe.png
tags:
- name: Regex
  slug: regex
- name: Regular Expressions
  slug: regular-expressions
- name: YAML
  slug: yaml
seo_title: null
seo_desc: 'YAML does not have built-in support for regular expressions. But you can
  still include regex patterns as part of a YAML file''s contents, access those patterns,
  and create a regex out of them.

  You can do this, for example, with the JavaScript RegExp c...'
---

YAML does not have built-in support for regular expressions. But you can still include regex patterns as part of a YAML file's contents, access those patterns, and create a regex out of them.

You can do this, for example, with the JavaScript `RegExp` constructor.

So, in YAML, regular expressions are typically represented as strings, using a specific syntax to define the pattern. For example, a YAML key-value pair that includes a regular expression pattern might look like this:

```bash
example:
pattern: ^[A-Za-z]+$
```

In this article, I'll show you how to write regular expressions inside a YAML file and access its entries in a JavaScript file. Let's take a look at what the YAML file is first.

## What We'll Cover

* [What is a YAML File?](#heading-what-is-a-yaml-file)
    
* [How to Write Regular Expressions in a YAML File](#heading-how-to-write-regular-expressions-in-a-yaml-file)
    
* [How to Import a YAML File in JavaScript and Use it](#heading-how-to-import-a-yaml-file-in-javascript-and-use-it)
    
* [Conclusion](#heading-conclusion)
    

## What is a YAML File?

YAML stands for YAML ain't markup language. It is a human and machine-readable data serialization file format. It is often used as configuration files, for data exchange, and for representing structured data in DevOps engineering.

YAML files use indentation and a concise syntax to define data structures such as lists, dictionaries (key-value pairs), and scalars (strings, numbers, booleans).

Each entry in a YAML file can be string, number, or Boolean, and other YAML-specific data types like scalars and lists. Here's a YAML file containing those data types:

```bash
# YAML Data Types Example
# -----------------------

# Scalars
null_example: null           # Null Scalar
bool_example: true           # Boolean Scalar
int_example: 42              # Integer Scalar
float_example: 3.14          # Float Scalar
str_example: "Hello, YAML!"  # String Scalar

# Sequences (Arrays)
seq_example:                 # Sequence (Array)
  - Apple
  - Orange
  - Banana

# Mappings (Dictionaries)
map_example:                 # Mapping (Dictionary)
  key1: value1
  key2: value2
  key3: value3

# List (Sequence of Mappings)
list_example:                # List of Mappings (Sequence of Dictionaries)
  - name: John
    age: 30
  - name: Jane
    age: 28
  - name: Bob
    age: 35
```

You can also put regular expressions right inside a YAML file. And that's what we'll look at next.

## How to Write Regular Expressions in a YAML File

You can represent specific values in a YAML file as regular expressions. Below are some validation regex patterns:

```bash
# validator.yaml file
password:
  pattern: ^(?!.*[\s])(?=.*[A-Z])(?=.*[a-z])(?=.*\d)[A-Za-z\d@$!%*#?&]{8,}$
  description: |
    - At least 8 characters
    - At least one uppercase letter
    - At least one lowercase letter
    - At least one digit
    - Allowed special characters: @$!%*#?&

nigerianPhoneNumber:
  pattern: ^(\+?234|0)[789]\d{9}$
  description: |
    - Nigerian phone number format
    - Starts with +234 or 0
    - Followed by 7, 8, or 9
    - Total of 11 digits

email:
  pattern: ^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$
  description: |
    - Valid email address format
    - Example: example@example.com

username:
  pattern: ^[a-zA-Z0-9_-]{3,16}$
  description: |
    - Allowed characters: letters (upper and lower case), numbers, underscore (_), and hyphen (-)
    - Minimum length: 3 characters
    - Maximum length: 16 characters
```

You can then import the YAML file into your JavaScript file and do what you want with it – for instance, create regular expressions out of those patterns and use them.

But that process is not straightforward. So that's the next thing you'll learn in this article.

## How to Import a YAML File in JavaScript and Use it

If you attempt to import any YAML file into a JavaScript file with the `import` syntax, like `import abc from file.yaml`, this is the kind of error you'll get:

![reYamlErr](https://www.freecodecamp.org/news/content/images/2023/05/reYamlErr.png align="left")

Instead of doing it that way, you should create a `package.json` in your project directory by running `npm init -y` and install the `js-yaml` package by running `npm install js-yaml`.

After that, import the `fs` module of Node.js and the `js-yaml` package this way:

```js
const fs = require('fs');
const yaml = require('js-yaml');
```

The next thing you should do is read the `validator.yaml` file with the `readFileSync` method of the `fs` module and parse the YAML file with the `load()` method:

```js
const yamlData = fs.readFileSync('validator.yaml', 'utf8');
const parsedData = yaml.load(yamlData);
```

All that's left to do is to access any of the patterns, create a RegEx out of it, and use it. This is how I used the password pattern:

```js
const passwordPattern = parsedData.password.pattern;
const pwordValidator = new RegExp(passwordPattern);

const myPassword = 'reallyStrongPassword21!';
console.log(pwordValidator.test(myPassword)); //true
```

Here's how I used the Nigerian phone number validator pattern:

```js
const phonePattern = parsedData.nigerianPhoneNumber.pattern;

phoneValidator = new RegExp(phonePattern);

const myPhoneNum = '08133333333';
console.log(phoneValidator.test(myPhoneNum)); //true;
```

Here's the full code:

```js
// import the fs module to be able to access the YAML file
const fs = require('fs');

// import the YAML package
const yaml = require('js-yaml');

// Read the validator.yaml file with the FS module
const yamlData = fs.readFileSync('test.yaml', 'utf8');

// parse the YAML file
const parsedData = yaml.load(yamlData);

// Access the password validator pattern from the YAML file
const passwordPattern = parsedData.password.pattern;

// Create a regex out of the password pattern
const pwordValidator = new RegExp(passwordPattern);

const myPassword = 'reallyStrongPassword21!';
console.log(pwordValidator.test(myPassword)); //true

// Access the nigeriaPhoneNumber validator pattern from the YAML file
const phonePattern = parsedData.nigerianPhoneNumber.pattern;

// Create a regex out of the phonePAttern
phoneValidator = new RegExp(phonePattern);

const myPhoneNum = '08133333333';
console.log(phoneValidator.test(myPhoneNum)); //true;

// Access the email validator pattern from the YAML file
const emailPattern = parsedData.email.pattern;

// Create a regex out of the phonePAttern
emailValidator = new RegExp(emailPattern);

const emailAddress = 'chris@gmail.com';
console.log(emailValidator.test(emailAddress)); //false;

// Access the username validator pattern from the YAML file
const usernamePattern = parsedData.username.pattern;

// Create a regex out of the phonePAttern
usernameValidator = new RegExp(usernamePattern);

const username = 'ksound22';
console.log(usernameValidator.test(username)); //false;
```

## Conclusion

This article showed you how to put regular expressions in a YAML file, import it into a JavaScript file with the `js-yaml` package, and access any of the values in it.

We also looked at how you can create regular expressions out of the patterns in the YAML file and test them with some strings.

Thanks for reading. If you find the article helpful, kindly share it with your friends and family.
