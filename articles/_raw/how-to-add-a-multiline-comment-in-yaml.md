---
title: YAML Commenting – How to Add a Multiline Comment in YAML
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2023-05-01T18:28:28.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-a-multiline-comment-in-yaml
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/vipul-jha-a4X1cdC1QAc-unsplash.jpg
tags:
- name: data
  slug: data
- name: YAML
  slug: yaml
seo_title: null
seo_desc: 'You can use a YAML file to store data in a format that can be easily read
  and understood by humans. It is a data serialization language that is often used
  for configuration files and data transfer between applications.

  YAML is similar to XML and JSON...'
---

You can use a YAML file to store data in a format that can be easily read and understood by humans. It is a [data serialization language](https://www.freecodecamp.org/news/what-is-yaml-the-yml-file-format/#intro:~:text=Serialization%20is%20a%20process%20where%20one%20application%20or%20service%20that%20has%20different%20data%20structures%20and%20is%20written%20in%20a%20different%20set%20of%20technologies%20can%20transfer%20data%20to%20another%20application%20using%20a%20standard%20format.) that is often used for configuration files and data transfer between applications.

YAML is similar to XML and JSON as they can all be used to store data in different formats. The main difference is their syntax. 

Here's what XML format looks like: 

```xml
<user>
  <name>John Doe</name>
  <phone>00223344</phone>
  <age>80</age>
</user>
```

Here's what JSON format looks like:

```json
{
  "user": {
    "name": "John Doe",
    "phone": "00223344",
    "age": 80
  }
}

```

Here's what YAML format looks like:

```yaml
user:
  name: John Doe
  phone: 00223344
  age: 80

```

Each of the formats above is used to store data about a user's name, phone number, and age.

You can read more about the features, basic rules, and syntax of YAML, and its differences from JSON and XML in [this article](https://www.freecodecamp.org/news/what-is-yaml-the-yml-file-format/).

In this article, you'll learn about multiline comments in YAML. 

## How to Add a Multiline Comment in YAML

You can use comments for various reasons like documenting your code, collaborating with others, stopping a block of code from running, and so on. 

You can use the `#` symbol to create comments in a YAML file. That is:

```yaml
# The object below represents a user

user:
  name: John Doe
  email: john.doe@example.com
  age: 30

```

Unlike some other languages, YAML doesn't have a different format for creating block or multiline comments. 

You'll have to use the `#` symbol on every line the comments spans into. Here's an example: 

```yaml
# The object below is an example that represents a 
# user's name, phone number and age

user:
  name: John Doe
  email: john.doe@example.com
  age: 30

```

If you remove the `#` symbol on the second line, the text may still appear as a comment but the YAML parser may interpret it as plain text which may lead to an error. 

To be on the safe side, use the `#` symbol at the start of each comment line. 

## Summary

In this article, we talked about YAML. It is mostly used to store and transfer data. 

We saw how to create inline and multiline comments. In YAML, the `#` symbol is used for both inline and multiline comments. 

Happy coding! Check out [my blog](https://ihechikara.com/) for more programming content.

