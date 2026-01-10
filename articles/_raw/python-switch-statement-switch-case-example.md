---
title: Python Switch Statement – Switch Case Example
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-08-05T15:27:56.000Z'
originalURL: https://freecodecamp.org/news/python-switch-statement-switch-case-example
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/switchCase.png
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: 'Until version 3.10, Python never had a feature that implemented what the
  switch statement does in other programming languages.

  So, if you wanted to execute multiple conditional statements, you would''ve had
  to use the elif keyword like this:

  age = 120...'
---

Until version 3.10, Python never had a feature that implemented what the switch statement does in other programming languages.

So, if you wanted to execute multiple conditional statements, you would've had to use the `elif` keyword like this:

```python
age = 120

if age > 90:
    print("You are too old to party, granny.")
elif age < 0:
    print("You're yet to be born")
elif age >= 18:
    print("You are allowed to party")
else: 
    "You're too young to party"

# Output: You are too old to party, granny.
```

From version 3.10 upwards, Python has implemented a switch case feature called “structural pattern matching”. You can implement this feature with the `match` and `case` keywords.

Some people debate whether or not the `match` and `case` are keywords in Python. This is because you can use both of them as variable and function names. But that’s another story for another day. 

You can refer to both keywords as "soft keywords" if you like.

In this article, I will show you how to write a switch statement in Python using the `match` and `case` keywords. 

But before that, I have to show you how Python programmers used to simulate a switch statement back in the day.

## How Python Programmers Used to Simulate Switch Case

There were multiple ways Pythonistas simulated switch statements back in the day. 

Using a function and the `elif` keyword was one of them and you can do it this way:

```python
def switch(lang):
    if lang == "JavaScript":
        return "You can become a web developer."
    elif lang == "PHP":
        return "You can become a backend developer."
    elif lang == "Python":
        return "You can become a Data Scientist"
    elif lang == "Solidity":
        return "You can become a Blockchain developer."
    elif lang == "Java":
        return "You can become a mobile app developer"

print(switch("JavaScript"))   
print(switch("PHP"))   
print(switch("Java"))  

"""
Output: 
You can become a web developer.
You can become a backend developer.
You can become a mobile app developer
"""
```  

## How to Implement Switch Statements with the `match` and `case` Keywords in Python 3.10 

To write switch statements with the structural pattern matching feature, you can use the syntax below:

```python
match term:
    case pattern-1:
         action-1
    case pattern-2:
         action-2
    case pattern-3:
         action-3
    case _:
        action-default
```

Note that the underscore symbol is what you use to define a default case for the switch statement in Python.

An example of a switch statement written with the match case syntax is shown below. It is a program that prints what you can become when you learn various programming languages:

```python
lang = input("What's the programming language you want to learn? ")

match lang:
    case "JavaScript":
        print("You can become a web developer.")

    case "Python":
        print("You can become a Data Scientist")

    case "PHP":
        print("You can become a backend developer")
    
    case "Solidity":
        print("You can become a Blockchain developer")

    case "Java":
        print("You can become a mobile app developer")
    case _:
        print("The language doesn't matter, what matters is solving problems.")
```

That’s a much cleaner syntax than multiple `elif` statements and simulating the switch statement with a function.

You probably noticed I did not add a break keyword to each of the cases, as it is done in other programming languages. That’s the advantage Python’s native switch statement has over those of other languages. The break keyword's functionality is done for you behind the scenes.


## Conclusion

This article showed you how to write switch statements with the “match” and “case” keywords. You also learned how Python programmers used to write it before version 3.10.

The Python match and case statements were implemented to provide the functionality that the switch statement feature in other programming languages such as JavaScript, PHP, C++, and others give us.

Thank you for reading.


