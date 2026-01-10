---
title: How to write a simple toy database in Python within minutes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-12T23:33:06.000Z'
originalURL: https://freecodecamp.org/news/how-to-write-a-simple-toy-database-in-python-within-minutes-51ff49f47f1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*yp-GUhlz1nZTRbkW-ye2HA.jpeg
tags:
- name: database
  slug: database
- name: json
  slug: json
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Palash Bauri

  MySQL, PostgreSQL, Oracle, Redis, and many more, you just name it — databases are
  a really important piece of technology in the progress of human civilization. Today
  we can see how valuable data are, and so keeping them safe and stabl...'
---

By Palash Bauri

MySQL, PostgreSQL, Oracle, Redis, and many more, you just name it — databases are a really important piece of technology in the progress of human civilization. Today we can see how valuable **data** are, and so keeping them safe and stable is where the database comes in!

So we can see how important databases are as well. For a quite some time I was thinking of creating My Own Toy Database just to understand, play around, and experiment with it. As [**Richard Feynman**](https://en.wikipedia.org/wiki/Richard_Feynman) said:

> **_“What I cannot create, I do not understand.”_**

So without any further talking let’s jump into the fun part: coding.

### Let’s Start Coding…

For this Toy Database, we’ll use **Python** (my favorite ❤️). I named this database **FooBarDB** (I couldn’t find any other name ?), but you can call it whatever you want!

So first let’s import some necessary Python libraries which are already available in Python Standard Library:

```python
import json
import os
```

Yes, we only need these two libraries! We need `json` as our database will be based on JSON, and `os` for some path related stuff.

Now let’s define the main class `FoobarDB` with some pretty basic functions, which I'll explain below.

```python
class FoobarDB(object):
    def __init__(self , location):
        self.location = os.path.expanduser(location)
        self.load(self.location)

    def load(self , location):
        if os.path.exists(location):
            self._load()
        else:
            self.db = {}
        return True

    def _load(self):
        self.db = json.load(open(self.location , "r"))

    def dumpdb(self):
        try:
            json.dump(self.db , open(self.location, "w+"))
            return True
        except:
            return False
```

Here we defined our main class with an `__init__` function. Whenever creating a Foobar Database we only need to pass the location of the database. In the first `__init__` function we take the location parameter and replace `~` or `~user` with user’s home directory to make it work intended way. And finally, put it in `self.location` variable to access it later on the same class functions. In the end, we are calling the `load` function passing `self.location` as an argument.

```python
. . . .
    def load(self , location):
        if os.path.exists(location):
            self._load()
        else:
            self.db = {}
        return True
. . . .
```

In the next `load` function we take the location of the database as a param. Then check if the database exists or not. If it exists, we load it with the `_load()` function (explained below). Otherwise, we create an empty in-memory JSON object. And finally, return true on success.

```python
. . . . 

    def _load(self):
        self.db = json.load(open(self.location , "r"))
. . . .
```

In the `_load` function, we just simply open the database file from the location stored in `self.location`. Then we transform it into a JSON object and load it into `self.db` variable.

```py
. . . .
    def dumpdb(self):
        try:
            json.dump(self.db , open(self.location, "w+"))
            return True
        except:
            return False

. . . .
```

And finally, the `dumpdb` function: its name says what it does. It takes the in-memory database (actually a JSON object) from the `self.db` variable and saves it in the database file! It returns **True** if saved successfully, otherwise returns **False.**

### Make It a Little More Usable… ?

Wait a minute! ? A database is useless if it can’t store and retrieve data, isn’t it? Let’s go and add them also…?

```py
. . . .
    def set(self , key , value):
        try:
            self.db[str(key)] = value
            self.dumpdb()
            return True
        except Exception as e:
            print("[X] Error Saving Values to Database : " + str(e))
            return False

    def get(self , key):
        try:
            return self.db[key]
        except KeyError:
            print("No Value Can Be Found for " + str(key))  
            return False

    def delete(self , key):
        if not key in self.db:
            return False
        del self.db[key]
        self.dumpdb()
        return True
. . . .
```

The `set` function is to add data to the database. As our database is a simple key-value based database, we’ll only take a `key` and `value` as an argument.

First, we’ll try to add the key and value to the database and then save the database. If everything goes right it will return True. Otherwise, it will print an error message and return False. (We don’t want it to crash and erase our data every time an error occurs ?).

```py
. . . .
    def get(self, key):
        try:
            return self.db[key]
        except KeyError:
            return False
. . . .
```

`get` is a simple function, we take `key` as an argument and try to return the value linked to the key from the database. Otherwise False is returned with a message.

```py
. . . .
    def delete(self , key):
        if not key in self.db:
            return False
        del self.db[key]
        self.dumpdb()
        return True

. . . .
```

`delete` function is to delete a key as well as its value from the database. First, we make sure the key is present in the database. If not we return False. Otherwise, we delete the key with the built-in `del` which automatically deletes the value of the key. Next, we save the database and it returns false.

Now you might think, what if I’ve created a large database and want to reset it? In theory, we can use `delete` — but it's not practical, and it’s also very time-consuming! ⏳ So we can create a function to do this task...

```py
. . . . 

    def resetdb(self):
        self.db={}
        self.dumpdb()
        return True
. . . .
```

Here’s the function to reset the database, `resetdb`! It's so simple: first, what we do is re-assign our in-memory database with an empty JSON object and it just saves it! And that's it! Our Database is now again clean shaven.

### Finally… ?

That’s it friends! We have created our own **Toy Database** ! ?? Actually, Fo**obarDB i**s just a simple demo of a database. It’s like a cheap DIY toy: you can improve it any way you want. You can also add many other functions according to your needs.

Full Source is Here ? [bauripalash/foobardb](https://github.com/bauripalash/foobardb)

I hope, you enjoyed it! Let me know your suggestions, ideas or mistakes I’ve made in the comments below! ?

Follow/ping me on socials ? F[acebook,](https://facebook.com/bauripalash) T[witter,](https://twitter.com/bauripalash) I[nstagram](https://instagram.com/bauripalash)

Thank you! See you soon!

---
If You Like My Work (My Articles, Stories, Softwares, Researches and many more) Consider [Buying Me A Coffee ☕](https://www.buymeacoffee.com/palash) ?


