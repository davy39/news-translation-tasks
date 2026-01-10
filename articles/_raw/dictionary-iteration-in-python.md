---
title: Dictionary Iteration in Python – How to Iterate Over a Dict with a For Loop
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2023-01-06T23:16:43.000Z'
originalURL: https://freecodecamp.org/news/dictionary-iteration-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/pexels-stas-knop-1194723.jpg
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: "In Python, a dictionary is one of the built-in data structures (the others\
  \ are tuples, lists, and sets). A dictionary is a collection of key:value pairs\
  \ and you can use them to solve various programming problems. \nDictionaries are\
  \ very flexible to wo..."
---

In Python, a dictionary is one of the built-in data structures (the others are tuples, lists, and sets). A dictionary is a collection of key:value pairs and you can use them to solve various programming problems. 

Dictionaries are very flexible to work with. You can get the keys and values separately, or even together.

This article is about looping over a dictionary with the `for` loop, but you can also loop through a dictionary with three methods:

- the `key()` method: gets you the keys in a dictionary 
- the `values()` method: gets you the values in a dictionary 
- the `items()` method: gets you both the keys and values in a dictionary 

In the example below, I use those 3 methods to get the keys, values, and items of the dictionary.

```py
states_tz_dict = {
    'Florida': 'EST and CST',
    'Hawaii': 'HST',
    'Arizona': 'DST',
    'Colorado': 'MST',
    'Idaho': 'MST and PST',
    'Texas': 'CST and MST',
    'Washington': 'PST',
    'Wisconsin': 'CST'
}

# Keys
states_keys = states_tz_dict.keys()
print(states_keys) # dict_keys(['Florida', 'Hawaii', 'Arizona', 'Colorado', 'Idaho', 'Texas', 'Washington', 'Wisconsin'])

#  Values
tz_values = states_tz_dict.values()
print(tz_values) # dict_values(['EST and CST', 'HST', 'DST', 'MST', 'MST and PST', 'CST and MST', 'PST', 'CST']) 

# Keys and values
states_tz_dict_items = states_tz_dict.items()
print(states_tz_dict_items) # dict_items([('Florida', 'EST and CST'), ('Hawaii', 'HST'), ('Arizona', 'DST'), ('Colorado', 'MST'), ('Idaho', 'MST and PST'), ('Texas', 'CST and MST'), ('Washington', 'PST'), ('Wisconsin', 'CST')])
```

That's some iterations we did. But you can also loop through a dictionary with a `for` loop. That's what we are going to look at in this tutorial.

## What We'll Cover
- [How to Iterate through a Dictionary with a `for` Loop](#heading-how-to-iterate-through-a-dictionary-with-a-for-loop)
- [How to Iterate through Dictionary Keys with a `for` Loop](#heading-how-to-iterate-through-dictionary-keys-with-a-for-loop)
  - [How to Iterate through Dictionary Values with a `for` Loop](#heading-how-to-iterate-through-dictionary-values-with-a-for-loop)
  - [How to Iterate through Dictionary Items with a `for` Loop](#heading-how-to-iterate-through-dictionary-items-with-a-for-loop)
- [How to Loop through a Dictionary and Convert it to a List of Tuples](#heading-how-to-loop-through-a-dictionary-and-convert-it-to-a-list-of-tuples)
- [Conclusion](#heading-conclusion)

## How to Iterate through a Dictionary with a `for` Loop

With the Python `for` loop, you can loop through dictionary keys, values, or items. You can also loop through the dictionary and put the key:value pair in a list of tuples. We are going to look at them one by one.

### How to Iterate through Dictionary Keys with a `for` Loop
Remember how I got the keys of the dictionary with the `keys()` method in the first part of this article? You can use the same method in a `for` loop and assign each of the keys to a variable we can call `k`:

```py
states_tz_dict = {
    'Florida': 'EST and CST',
    'Hawaii': 'HST',
    'Arizona': 'DST',
    'Colorado': 'MST',
    'Idaho': 'MST and PST',
    'Texas': 'CST and MST',
    'Washington': 'PST',
    'Wisconsin': 'CST'
}

for k in states_tz_dict.keys():
    print(k)

# Result:
# Florida   
# Hawaii    
# Arizona   
# Colorado  
# Idaho     
# Texas     
# Washington
# Wisconsin
```

### How to Iterate through Dictionary Values with a `for` Loop
You can use the `values()` method in a `for` loop too, and assign the values to a variable you can call `v`:

```py
states_tz_dict = {
    'Florida': 'EST and CST',
    'Hawaii': 'HST',
    'Arizona': 'DST',
    'Colorado': 'MST',
    'Idaho': 'MST and PST',
    'Texas': 'CST and MST',
    'Washington': 'PST',
    'Wisconsin': 'CST'
}

for v in states_tz_dict.values():
    print(v)
    
# Result:
# EST and CST
# HST        
# DST        
# MST        
# MST and PST
# CST and MST
# PST        
# CST
```

### How to Iterate through Dictionary Items with a `for` Loop
The `items()` method comes in handy in getting the keys and values inside a `for` loop. This time around, you have to assign two variables instead of one:

```py
states_tz_dict = {
    'Florida': 'EST and CST',
    'Hawaii': 'HST',
    'Arizona': 'DST',
    'Colorado': 'MST',
    'Idaho': 'MST and PST',
    'Texas': 'CST and MST',
    'Washington': 'PST',
    'Wisconsin': 'CST'
}

for k, v in states_tz_dict.items():
    print(k,"--->", v)

# Result:
# Florida ---> EST and CST
# Hawaii ---> HST
# Arizona ---> DST        
# Colorado ---> MST       
# Idaho ---> MST and PST  
# Texas ---> CST and MST  
# Washington ---> PST     
# Wisconsin ---> CST 
```

**Note**: You can use any letter for the variable(s) in a `for` loop. It doesn't have to be k or v, or k, v. 


### How to Loop through a Dictionary and Convert it to a List of Tuples
To convert a dictionary to a list of tuples in Python, you still have to use the `items()` method inside a `for` loop. 

But this time around, you have to surround the loop with square brackets. You also have to assign the loop to a separate variable and wrap the variable for both keys and values in brackets: 
```py
states_tz_dict = {
    'Florida': 'EST and CST',
    'Hawaii': 'HST',
    'Arizona': 'DST',
    'Colorado': 'MST',
    'Idaho': 'MST and PST',
    'Texas': 'CST and MST',
    'Washington': 'PST',
    'Wisconsin': 'CST'
}

list_of_tuples = [(k, v) for k, v in states_tz_dict.items()]
print(list_of_tuples)

# Result: [('Florida', 'EST and CST'), ('Hawaii', 'HST'), ('Arizona', 'DST'), ('Colorado', 'MST'), ('Idaho', 'MST and PST'), ('Texas', 'CST 
# and MST'), ('Washington', 'PST'), ('Wisconsin', 'CST')]
```


## Conclusion
In this tutorial, we looked at how to iterate through a dictionary with the `for` loop. 

If you don’t want to use a `for` loop, you can also use any of the `keys()`, `values()`, or `items()` methods directly like I did in the first part of this article.

If you find this article helpful, don’t hesitate to share it on social media.


