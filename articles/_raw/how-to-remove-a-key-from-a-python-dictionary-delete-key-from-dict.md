---
title: How to Remove a Key from a Python Dictionary – Delete Key from Dict
subtitle: ''
author: Zaira Hira
co_authors: []
series: null
date: '2022-02-18T20:32:40.000Z'
originalURL: https://freecodecamp.org/news/how-to-remove-a-key-from-a-python-dictionary-delete-key-from-dict
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/remove-key-val.png
tags:
- name: dictionary
  slug: dictionary
- name: Python
  slug: python
seo_title: null
seo_desc: "A dictionary is a very powerful data collection in Python. Dictionaries\
  \ help make database operations faster. \nYou can append items to an existing dictionary\
  \ and remove them as well.\nIn this blog post, we will learn how to delete \"keys\"\
  \ using two met..."
---

A dictionary is a very powerful data collection in Python. Dictionaries help make database operations faster. 

You can append items to an existing dictionary and remove them as well.

In this blog post, we will learn how to delete "keys" using two methods:

1. Deleting `key:value` pairs using `del`.
2. Deleting `key:value` pairs using `pop()`.

## What is a Dictionary in Python?

A dictionary is an unordered collection of items. The items are defined using key-value pairs. Keys map to their corresponding item in the list. Whenever an item needs to be queried, we can do this using its key.

For example, `"city":"Seoul"` is a key value pair where "city" is the key, and "Seoul" is its value.

Here's the syntax for declaring a dictionary in Python:

```python
my_dict = {
    <key>: <value>,
    <key>: <value>,
      .
      .
      .
    <key>: <value>
}
```

In our examples, we will use the below dictionary:

```python
>>> # Declare a dictionary
>>> my_dict = {"Fruit":"Pear", "Vegetable":"Carrot", "Pet":"Cat", "Book":"Moby dick", "Crystal":"Amethyst"}
```

![Image](https://www.freecodecamp.org/news/content/images/2022/02/image-61.png)

## How to Remove Keys from a Dictionary in Python

### Remove a key using `del`.

You can remove a key using the `del` keyword. Here's the syntax for that:

```python
del dict["Key"]
```

Let's delete a key in our dictionary `my_dict`. We'll be deleting the key: "Fruit".

```python
# Delete a key - Fruit
del my_dict["Fruit"]
```

![Image](https://www.freecodecamp.org/news/content/images/2022/02/image-62.png)

After we delete that key, we can see that the key `Fruit` is no longer present in the dictionary.

But, what happens if you try to delete a key that does not exist?

Let's try to delete the key `Fruit` again.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/image-63.png)
_Delete a key that does not exist._

We received a traceback error. This is valid as the key does not exist. 

One drawback of `del` is that it throws an exception when `key` is not found. The exception needs to be handled explicitly in a try catch block. 

However, we can handle this exception using the second method.

### Remove a key using `pop()`

The second way to remove a key is using the `pop()` method. Here's its syntax_:_

```python
data.pop("Key", None)
```

 Where,

* `key` is the key to be removed.
* `None` specifies that if the key is found, then delete it. Else, do nothing.
* We can also specify a custom message in place of 'None' for cases where key is not found.

Now, if we try to delete `Fruit` again, there is no exception thrown.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/image-65.png)

Now, let's try to delete an existing key with `pop()`.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/image-64.png)

Here, the key:Book is successfully deleted.

One advantage of `pop()` over `del` is that it allows us to handle exceptions. It provides a mechanism to return a custom message when exception occurs.

### How to set a custom message:

Let's try to delete 'Book' again. We are expecting an error, so let's set a return message.

Here, `Key does not exist` is the return message in case the key does not exist.

```python
my_dict.pop("Book", 'Key does not exist')
```

![Image](https://www.freecodecamp.org/news/content/images/2022/02/image-68.png)
_As "Book" was already deleted, we are getting the error message_

Another advantage is that it also returns the value of the key in addition to performing a delete operation. If you need to know the value of a deleted key, then `pop()` is the suitable option.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/image-67.png)

## Conclusion

In this tutorial, we learned how to create a dictionary in Python. We also focused on how to delete key:value pairs in a dictionary. 

I hope you found this tutorial helpful.

Let's connect on [Twitter](https://twitter.com/hira_zaira)!

Read my other posts [here](https://www.freecodecamp.org/news/author/zaira/).

Let's [chat on Discord.](https://discordapp.com/users/Zaira_H#2603)

