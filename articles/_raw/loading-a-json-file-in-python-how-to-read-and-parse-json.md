---
title: Loading a JSON File in Python – How to Read and Parse JSON
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-07-25T14:06:45.000Z'
originalURL: https://freecodecamp.org/news/loading-a-json-file-in-python-how-to-read-and-parse-json
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/read-parse-json-files.png
tags:
- name: json
  slug: json
- name: Python
  slug: python
seo_title: null
seo_desc: 'By Dillion Megida

  In this article, you''ll learn how to read and parse JSON in Python.

  What is JSON?

  JSON is short for JavaScript Object Notation. It''s a simple syntax for storing
  data in name-value pairs. Values can be different data types as long as...'
---

By Dillion Megida

In this article, you'll learn how to read and parse JSON in Python.

## What is JSON?

JSON is short for JavaScript Object Notation. It's a simple syntax for storing data in name-value pairs. Values can be different data types as long as they are valid. Non-acceptable types for JSON include functions, dates, and `undefined`.

JSON files are stored with the `.json` extension with a valid JSON structure.

Here's what the structure of a JSON file looks like:

```json
{
  "name": "John",
  "age": 50,
  "is_married": false,
  "profession": null,
  "hobbies": ["traveling", "photography"]
}
```

You'll often use JSON to send and receive data from a server in web applications.

When the data is received, the program reads and parses the JSON to extract specific data. Different languages have their own methods for doing this. We'll look at how to do these in Python here.

## How to Read JSON Files

Let's say the JSON in the code block above is stored in a `user.json` file. Using the `open()` inbuilt function in Python, we can read that file and assign the content to a variable. Here's how:

```python
with open('user.json') as user_file:
  file_contents = user_file.read()
  
print(file_contents)
# {
#   "name": "John",
#   "age": 50,
#   "is_married": false,
#   "profession": null,
#   "hobbies": ["travelling", "photography"]
# }
```

You pass the file path to the `open` method which opens the file and assigns the stream data from the file to the `user_file` variable. Using the `read` method, you can pass the text contents of the file to the `file_contents` variable.

I used `with` at the beginning of the expression so that after reading the contents of the file, Python can close the file.

`file_contents` now contains a stringified version of the JSON. As a next step, you can now parse the JSON.

## How to Parse JSON

Python has in-built modules for various operations. For managing JSON files, Python has the `json` module.

This module comes with many methods. One of which is the `loads()` method for parsing JSON strings. Then, you can assign the parsed data to a variable like this:

```js
import json

with open('user.json') as user_file:
  file_contents = user_file.read()
  
print(file_contents)

parsed_json = json.loads(file_contents)
# {
#   'name': 'John',
#   'age': 50,
#   'is_married': False,
#   'profession': None,
#   'hobbies': ['travelling', 'photography']
# }
```

Using the `loads()` method, you can see that the `parsed_json` variable now has a valid dictionary. From this dictionary, you can access the keys and values in it.

Also notice how `null` from the JSON is converted to `None` in python. This is because `null` is not valid in `Python`.

## How to Use `json.load()` to Read and Parse JSON Files

The `json` module also has the `load` method which you can use to read a file object and parse it at the same time. Using this method, you can update the previous code to this:

```python
import json

with open('user.json') as user_file:
  parsed_json = json.load(user_file)

print(parsed_json)
# {
#   'name': 'John',
#   'age': 50,
#   'is_married': False,
#   'profession': None,
#   'hobbies': ['travelling', 'photography']
# }
```

Instead of using the `read` method of the file object and using the `loads` method of the `json` module, you can directly use the `load` method which reads and parses the file object.

## Wrapping Up

JSON data is commonly known for its simple structure and is popular (a standard in most cases) for information exchange between servers and clients.

Different languages and technologies can read and parse JSON files in different ways. In this article, we've learned how to read JSON files and parse such files using the `read` method of file objects, and the `loads` and `load` methods of the `json` module.


