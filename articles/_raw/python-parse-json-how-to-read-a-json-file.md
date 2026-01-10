---
title: Python Parse JSON – How to Read a JSON File
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2022-02-07T17:03:18.000Z'
originalURL: https://freecodecamp.org/news/python-parse-json-how-to-read-a-json-file
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/pexels-mike-1181776.jpg
tags:
- name: json
  slug: json
- name: Python
  slug: python
seo_title: null
seo_desc: 'JSON (JavaScript Object Notation) is a popular way to structure data. It''s
  used to exchange information between a web application and the server. But how do
  you read a JSON file in Python?

  In this article, I will show you how to use the json.loads() ...'
---

JSON (JavaScript Object Notation) is a popular way to structure data. It's used to exchange information between a web application and the server. But how do you read a JSON file in Python?

In this article, I will show you how to use the `json.loads()` and `json.load()` methods to parse and read JSON files and strings. 

## JSON syntax

Before we get into parsing and reading a JSON file, we first need to understand the basic syntax. The JSON syntax looks like a JavaScript object literal with key-value pairs.

This is an example of JSON data for [freeCodeCamp](https://www.freecodecamp.org/):

```json
{
  "organization": "freeCodeCamp",
  "website": "https://www.freecodecamp.org/",
  "formed": 2014,
  "founder": "Quincy Larson",
  "certifications": [
    {
      "name": "Responsive Web Design",
      "courses": [
        "HTML",
        "CSS"
      ]
    },
    {
      "name": "JavaScript Algorithms and Data Structures",
      "courses": [
        "JavaScript"
      ]
    },
    {
      "name": "Front End Development Libraries",
      "courses": [
        "Bootstrap",
        "jQuery",
        "Sass",
        "React",
        "Redux"
      ]
    },
    {
      "name": "Data Visualization",
      "courses": [
        "D3"
      ]
    },
    {
      "name": "Relational Database Course",
      "courses": [
        "Linux",
        "SQL",
        "PostgreSQL",
        "Bash Scripting",
        "Git and GitHub",
        "Nano"
      ]
    },
    {
      "name": "Back End Development and APIs",
      "courses": [
        "MongoDB",
        "Express",
        "Node",
        "NPM"
      ]
    },
    {
      "name": "Quality Assurance",
      "courses": [
        "Testing with Chai",
        "Express",
        "Node"
      ]
    },
    {
      "name": "Scientific Computing with Python",
      "courses": [
        "Python"
      ]
    },
    {
      "name": "Data Analysis with Python",
      "courses": [
        "Numpy",
        "Pandas",
        "Matplotlib",
        "Seaborn"
      ]
    },
    {
      "name": "Information Security",
      "courses": [
        "HelmetJS"
      ]
    },
    {
      "name": "Machine Learning with Python",
      "courses": [
        "Machine Learning",
        "TensorFlow"
      ]
    }
  ]
}
```

## How to parse a JSON string in Python

Python has a built in module that allows you to work with JSON data. At the top of your file, you will need to import the `json` module. 

```py
import json

```

If you need to parse a JSON string that returns a dictionary, then you can use the `json.loads()` method. 

```py
import json

# assigns a JSON string to a variable called jess 
jess = '{"name": "Jessica Wilkins", "hobbies": ["music", "watching TV", "hanging out with friends"]}'

# parses the data and assigns it to a variable called jess_dict
jess_dict = json.loads(jess)

# Printed output: {"name": "Jessica Wilkins", "hobbies": ["music", "watching TV", "hanging out with friends"]}
print(jess_dict)
```

## How to parse and read a JSON file in Python

In this example, we have a JSON file called `fcc.json` which holds the same data from earlier concerning the courses offered by freeCodeCamp. 

If we want to read that file, we first need to use Python's built in `open()` function with the mode of read. We are using the `with` keyword to make sure that the file is properly closed. 

```py
with open('fcc.json', 'r') as fcc_file:

```

If the file cannot be opened, then we will receive an OSError. This is an example of a "FileNotFoundError" if I misspell the `fcc.json` file name. 

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screen-Shot-2022-02-07-at-4.47.15-AM.png)

We can then parse the file using the `json.load()` method and assign it to a variable called `fcc_data`. 

```py
 fcc_data = json.load(fcc_file)
```

The final step would be to print the results.

```py
print(fcc_data)

```

This is what the entire code would look like:

```py
import json

with open('fcc.json', 'r') as fcc_file:
    fcc_data = json.load(fcc_file)
    print(fcc_data)
```

## How to Pretty Print JSON data in Python

If we examine the printed data, then we should see that the JSON data prints all on one line.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screen-Shot-2022-02-07-at-5.09.05-AM.png)

But that can be hard to read. To fix that, we can use the `json.dumps()` method with the parameter of `indent`.

In this example, we are going to have an indent of 4 spaces and print the data in an easier to read format.

```py
 print(json.dumps(fcc_data, indent=4))

```

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screen-Shot-2022-02-07-at-5.13.13-AM.png)

We can also sort the keys in alphabetical order using the `sort_keys` parameter and setting that to `True`. 

```py
print(json.dumps(fcc_data, indent=4, sort_keys=True))

```

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screen-Shot-2022-02-07-at-5.18.47-AM.png)

## Conclusion

JSON (JavaScript Object Notation) is a popular way to structure data and is used to exchange information between a web application and the server. 

If you need to parse a JSON string that returns a dictionary, then you can use the `json.loads()` method. 

If you need to parse a JSON file that returns a dictionary, then you can use the `json.load()` method. 

