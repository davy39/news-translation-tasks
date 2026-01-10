---
title: JSON Comment Example — How to Comment in JSON Files
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-04-26T14:56:30.000Z'
originalURL: https://freecodecamp.org/news/json-comment-example-how-to-comment-in-json-files
coverImage: https://www.freecodecamp.org/news/content/images/2020/04/abstract-art-blur-bright-373543.jpg
tags:
- name: data
  slug: data
- name: json
  slug: json
- name: learn to code
  slug: learn-to-code
- name: General Programming
  slug: programming
seo_title: null
seo_desc: 'By Amy Haddad

  If you’re having trouble adding comments to your JSON file, there’s a good reason:
  JSON doesn’t support comments.

  “I removed comments from JSON because I saw people were using them to hold parsing
  directives, a practice which would have...'
---

By Amy Haddad

If you’re having trouble adding comments to your JSON file, there’s a good reason: JSON doesn’t support comments.

“I removed comments from JSON because I saw people were using them to hold parsing directives, a practice which would have destroyed interoperability,” writes [Douglas Crockford](https://web.archive.org/web/20150105080225if_/https://plus.google.com/+DouglasCrockfordEsq/posts/RK8qyGVaGSr), who popularized the text-based data format.

However, there’s a workaround. And that’s what this article is about: how to add comments to your JSON file.

## Add Data as Comments

A way to skirt around the comments issue is to add data to your JSON file that function as comments.

Let’s go through an example, starting with this information in our JSON file:

```json
{
   "sport": "basketball",
   "coach": "Joe Smith",
   "wins": 15,
   "losses": 5
}
```


  
Now let’s add another key-value pair to serve as our comment, which you can see in the first line in the code below:

```json
{
   "_comment1": "this is my comment",
   "sport": "basketball",
   "coach": "Joe Smith",
   "wins": 15,
   "losses": 5
}
```

Here’s another example. This time, we use two underscores at the start and end of the key:

```json
 "__comment2__": "this is another comment",
```

The underscores help to differentiate the comment from the rest of the data in our file.

### A Word of Caution

There’s an important detail to keep in mind.

The comments we added to our JSON file are included in the JSON object. In other words, the comments are treated as data.

Here’s what we mean.

This is the code in our file, **`data.json`**:

```json
{
   "_comment1": "this is my comment",
   "sport": "basketball",
   "coach": "Joe Smith",
   "wins": 15,
   "losses": 5
}
```

Now we’re going to read that data from the file, `read_comments.py`:

```python
import json
with open("data.json", mode="r") as j_object:
   data = json.load(j_object)
print(data)
```

The result includes our comment:

```json
{'_comment1': 'this is my comment', 'sport': 'basketball', 'coach': 'Joe Smith', 'wins': 15, 'losses': 5}
```

We can even extract the comment's value from the JSON object: `this is my comment`:

```python
import json
 
with open("data.json", mode="r") as j_object:
   data = json.load(j_object)
   print(data["_comment1"])
```

Keep in mind that the comment is only a comment in the eyes of the developer—not the computer.

### A Different Type of Comment

This JSON commenting practice is different from comments in programming languages, like Python, which are typically ignored when the program runs.

```python
# Here's my comment
word = "house"
for letter in word:
   print(letter)
```

When we run the Python program above, we get the letters in the word, “house.” But we don’t see the comment. It’s ignored.

## Commenting Options

[JSMin](https://www.crockford.com/jsmin.html) is another option to consider.

It’s a tool that removes extra whitespace and comments from JavaScript files. But it also works on JSON files. JSMin removes comments from JSON files before they're parsed.

So there are options when it comes to commenting in JSON files. Although they're not perfect solutions, at least there are ways to include the documentation you need when you need it.

_I write about learning to program and the best ways to go about it (_[amymhaddad.com](https://amymhaddad.com/)).  


  




  



