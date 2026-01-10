---
title: Adding to a Dict in Python – How to Add to a Dictionary
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-12-22T18:04:49.000Z'
originalURL: https://freecodecamp.org/news/adding-to-a-dict-in-python-how-to-add-to-a-dictionary
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/addToDict.png
tags:
- name: dictionary
  slug: dictionary
- name: Python
  slug: python
seo_title: null
seo_desc: "A Python dictionary is like a JavaScript object – it’s a sequence of key:value\
  \ pairs. So, you can create them like this:\nstack_dict = {\n    \"frontend\": \"\
  JavaScript\",\n    \"backend\": \"Node JS\",\n    \"markup\": \"HTML and JSX\",\n\
  }\n\nTo access the value in th..."
---

A Python dictionary is like a JavaScript object – it’s a sequence of `key:value` pairs. So, you can create them like this:

```py
stack_dict = {
    "frontend": "JavaScript",
    "backend": "Node JS",
    "markup": "HTML and JSX",
}
```

To access the value in the dictionary, you can do it this way: `dict[key]`. For example, if I want to access what the `frontend` key holds, I can do it like this:

```py
print(stack_dict["frontend"])
# JavaScript
```

But what if you want to add another entry to the dictionary without going back to the dictionary to put it there? That's what we are going to look at in this article. And I'm going to show you how to do it in 3 different ways.

## What We'll Cover
- [How to Add to a Dictionary in Python](#heading-how-to-add-to-a-dictionary-in-python)
- [How to Add to a Dictionary by Mapping a key to the Dictionary](#howtoaddtoadictionarybymappingakeytothedictionary)
- [How to Add to a Dictionary by Using the `update()` Method](#howtoaddtoadictionarybyusingtheupdatemethod)
- [How to Add to a Dictionary by Using the `if` Statement](#howtoaddtoadictionarybyusingtheifstatement)
- [Conclusion](#heading-conclusion)


## How to Add to a Dictionary in Python
You can add to a dictionary in three different ways:
- map a key to the dictionary 
- use the `update()` method
- use an if statement

### How to Add to a Dictionary in Python by Mapping a key to the Dictionary
If you want to add to a dictionary with this method, you'll need to add the value with the assignment operator.

```py
dict["key"] = "value"`
```

This would also override the value of an existing key.

In the stack dictionary I defined earlier, there's no styling there:

```py
stack_dict = {
    "frontend": "JavaScript",
    "backend": "Node JS",
    "markup": "HTML and JSX",
}
```

So let's add a `styling` key and `CSS` value to the dictionary by mapping a new key to the dictionary:

```py
stack_dict["styling"] = "CSS"

print(stack_dict)
# Output: {'frontend': 'JavaScript', 'backend': 'Node JS', 'markup': 'HTML and JSX', 'styling': 'CSS'}
```

You can see that a new key of `styling` and a value of `CSS` has been added to the dictionary.

If the key already exists, the value gets overwritten:

```py
stack_dict["markup"] = "HTML only"
print(stack_dict)

# {'frontend': 'JavaScript', 'backend': 'Node JS', 'markup': 'HTML only'}
```

### How to Add to a Dictionary in Python Using the `update()` Method

The stack is still missing a JavaScript library, so let's add it with the `update()` method. You can do that this way:

```py
dict.update({"key": "value"})`.
```

So, to add the JavaScript framework/library, I did it like this:

```py
stack_dict.update({"JS Framework": "React/Next"})

print(stack_dict)
# {'frontend': 'JavaScript', 'backend': 'Node JS', 'markup': 'HTML and JSX', 'styling': 'CSS', 'JS Framework': 'React/Next'}
```

The `update()` also overwrites an existing value if it's different:

```py
stack_dict.update({"backend": "Django"})

print(stack_dict)
# {'frontend': 'JavaScript', 'backend': 'Django', 'markup': 'HTML and JSX'}
```

### How to Add to a Dictionary in Python Using the `if` Statement

If you don't want an entry to be overwritten even if it already exists, you can use an `if` statement. You can do it with this syntax:

```py
if "value" not it dict.keys():
    dict["key"] = "value"
```

I want to add a "CSS Framework" key with a value of "Tailwind CSS" to the stack dictionary, so I'm going to do that with the help of this syntax:

```py
if "Tailwind CSS" not in stack_dict.keys():
    stack_dict["CSS Framework"] = "Tailwind CSS"

print(stack_dict)
# {'frontend': 'JavaScript', 'backend': 'Node JS', 'markup': 'HTML and JSX', 'styling': 'CSS', 'JS Framework': 'React/Next', 'CSS Framework': 'Tailwind CSS'}
```

If the entry is already in the dictionary, it won't be added in there:

```py
if "HTML and JSX" not in stack_dict.keys():
    stack_dict["markup"] = "HTML and JSX"

print(stack_dict)
# {'frontend': 'JavaScript', 'backend': 'Node JS', 'markup': 'HTML and JSX', 'styling': 'CSS', 'JS Framework': 'React/Next'}
```

If you don't feel like using an `if` statement to add to the dictionary, you can do the same thing with `try…except…`:

```py
try:
  stack_dict["Deployment"] = "Anywhere possible"
except:
  print("An exception occurred")

print(stack_dict)
# {'frontend': 'JavaScript', 'backend': 'Node JS', 'markup': 'HTML and JSX', 'styling': 'CSS', 'JS Framework': 'React/Next', 'Deployment': 'Anywhere possible'}
```

## Conclusion
This article took you through three different ways to add to a dictionary in Python:
- mapping a key to the dictionary 
- using the update() method
- using an if statement 

We even looked at how you can add to a dictionary with the `try…except…` expression.

Thank you for reading.



