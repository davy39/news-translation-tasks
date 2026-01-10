---
title: Python String Format – Python S Print Format Example
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2021-09-07T23:20:34.000Z'
originalURL: https://freecodecamp.org/news/python-string-format-python-s-print-format-example
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/federico-burgalassi-t2zKLI9MQnw-unsplash.jpg
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: "In Python, you have a few options to format your strings. In this article,\
  \ I will go over str.format(), formatted string literals, and template strings.\
  \ \nBut first, let's take a look at what is considered to be the \"old way\" of\
  \ formatting strings. \nW..."
---

In Python, you have a few options to format your strings. In this article, I will go over `str.format()`, formatted string literals, and template strings. 

But first, let's take a look at what is considered to be the "old way" of formatting strings. 

## What is % string formatting in Python? 

One of the older ways to format strings in Python was to use the `%` operator. 

Here is the basic syntax:

```py
"This is a string %s" % "string value goes here"
```

You can create strings and use `%s` inside that string which acts like a placeholder. Then you can write `%` followed be the actual string value you want to use. 

Here is a basic example using `%` string formatting.

```py
print("Hi, my name is %s" % "Jessica")
```

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-06-at-10.31.53-PM.png)

This method is often referred to as the "older" way because Python 3 introduced `str.format()` along with formatted string literals. 

## What is the `str.format()` method in Python?

Here is the basic syntax for the `str.format()` method:

```py
"template string {}".format(arguments)
```

Inside the template string, we can use `{}` which act as placeholders for the arguments. The arguments are values that will be displayed in the string. 

In this example, we want to print `"Hello, my name is Jessica. I am a musician turned programmer."` 

In the string, we are going to have a total of three `{}` which will act as placeholders for the values of Jessica, musician, and programmer. These are called format fields. 

```py
"Hello, my name is {}. I am a {} turned {}."
```

Inside these parenthesis for the `str.format()`, we will use the values of "Jessica", "musician", and "programmer". 

```py
.format("Jessica", "musician", "programmer")
```

Here is the complete code and printed sentence:

```py
print("Hello, my name is {}. I am a {} turned {}.".format("Jessica", "musician", "programmer"))
```

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-03-at-10.32.14-PM.png)

### Positional arguments 

You can access the value of these arguments using an index number inside the `{}`. 

In this example, we have two arguments of `"trumpet"` and `"drums"` inside the `.format()`. 

```py
.format("trumpet", "drums")
```

We can access those values inside the string by referring to the index numbers. `{0}` refers to the first argument of `"trumpet"` and `{1}` refers to the second argument of `"drums"`.

```py
"Steve plays {0} and {1}."
```

Here is the complete code and printed sentence:

```py
print("Steve plays {0} and {1}.".format("trumpet", "drums"))

```

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-03-at-11.04.33-PM.png)

We can modify this example and switch the index numbers in the string. You will notice that the sentence has changed and the placement of the arguments is switched. 

```py
print("Steve plays {1} and {0}.".format("trumpet", "drums"))

```

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-03-at-11.06.17-PM.png)

### Keyword arguments

These arguments consist of a `key` `value` pair. We can access the `value` of the argument by using the `key` inside the `{}`. 

In this example, we have two keys called `organization` and `adjective`. We are going to use those keys inside the string. 

```py
"{organization} is {adjective}!"
```

Inside the `.format()`, we have the `key` `value` pairs.

```py
.format(organization="freeCodeCamp", adjective="awesome")
```

Here is the complete code and printed sentence. 

```py
print("{organization} is {adjective}!".format(organization="freeCodeCamp", adjective="awesome"))

```

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-03-at-11.44.14-PM.png)

### How to Mix Keyword and Positional arguments

In the `str.format()` you can mix keyword and positional arguments. 

In this example, we are going to create a short story about going to Disneyland. 

We are first going to create a few variables for name, number, adjective and a Disneyland ride. 

```py
name = "Sam"
adjective = "amazing"
number = 200
disney_ride = "Space Mountain"
```

We then want to create our string using keyword and positional arguments. I am going to add the `\n` to tell the computer to create a new line after each sentence. 

```py
"I went to {0} with {name}.\nIt was {adjective}.\nWe waited for {hours} hours to ride {ride}."
```

Inside the parenthesis for the `str.format()`, we will assign our variables to the keys of `name`, `adjective`, `hours` and `disney_ride`. `{0}` will have the value of `"Disneyland"`. 

```py
.format("Disneyland", name=name, adjective=adjective, hours=number, ride=disney_ride)
```

Here is the complete code and printed sentence:

```py
name = "Sam"
adjective = "amazing"
number = 200
disney_ride = "Space Mountain"

print("I went to {0} with {name}.\nIt was {adjective}.\nWe waited for {hours} hours to ride {ride}."
      .format("Disneyland", name=name, adjective=adjective, hours=number, ride=disney_ride))
```

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-04-at-12.20.41-AM.png)

## What are formatted string literals? 

Formatted string literals (or f-strings) allow you to include expressions inside your strings. Just before the string you place an `f` or `F` which tells the computer you want to use an `f-string`. 

Here is the basic syntax:

```py
variable = "some value"
f"this is a string {variable}"
```

Here is a basic example that prints the sentence `Maria and Jessica have been friends since grade school.`

```py
name = "Jessica"
print(f"Maria and {name} have been friends since grade school.")
```

It works just the same if I use a capital `F` before the string.

```py
name = "Jessica"
print(F"Maria and {name} have been friends since grade school.")
```

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-06-at-6.21.48-PM.png)

You can also use an `f-string` to format data from a dictionary. 

In this example, we have a dictionary which represents the top rankings for men's college basketball teams and how many games they won out of 32. 

```py
rankings = {"Gonzaga": 31, "Baylor": 28, "Michigan": 25, "Illinois": 24, "Houston": 21}

```

We can use a `for loop` and the `items()` method to go through each of the `key value` pairs of the `rankings` dictionary. 

```py
for team, score in rankings.items():

```

Inside the `for loop`, we can use an `f-string` to format the printed results. 

The use of the `:` for  `{team:10}` and `{score:10d}` tells the computer to create a field that is 10 characters wide. This will create even columns for the data. 

The `d` inside here `{score:10d}` refers to a decimal integer. 

```py
 print(f"{team:10} ==> {score:10d}")
```

Here is the full code and the printed output:

```py
rankings = {"Gonzaga": 31, "Baylor": 28, "Michigan": 25, "Illinois": 24, "Houston": 21}

for team, score in rankings.items():
    print(f"{team:10} ==> {score:10d}")
```

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-06-at-9.48.53-PM.png)

## What are template strings?

Template strings are Python strings that use placeholders for the real values. 

Here is the basic syntax:

```py
Template("$placeholder").substitute(placeholder="real value")
```

Let's take a look at an example to better understand how it works. 

In this example, we want to print `I love to learn with freeCodeCamp!` using template strings. 

In order to use template strings, you will first have to import the `Template` class from the standard library. 

```py
from string import Template

```

You can then use the `Template` class and provide a string inside the parenthesis. We are going to place a `$` in front of `name` which will later be replaced by the real value.

```py
Template("I love to learn with $name!")
```

We then add `.substitute` to the template and assign the value of `freeCodeCamp` to `name`. 

```py
.substitute(name="freeCodeCamp")
```

Here is the full code and the printed output:

```py
from string import Template

print(Template("I love to learn with $name!").substitute(name="freeCodeCamp"))
```

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-06-at-10.11.27-PM.png)

## Conclusion

There are many ways to format your strings in Python. 

The older way of formatting your strings would be to use the `%` operator.

```py
"This is a string %s" % "string value goes here"

```

`%s` acts as a placeholder for the real value. You place the real value after the `%` operator. 

This method is often referred to as the "older" way because Python 3 introduced `str.format()` and formatted string literals (f-strings).

In the `str.format()` method, you use `{}` for placeholders and place the real values inside the parenthesis. This method can take in positional and keyword arguments. 

```py
"template string {}".format(arguments)
```

Formatted string literals (or f-strings) allow you to include expressions inside your strings. Just before the string you place an `f` or `F` which tells the computer you want to use an `f-string`. 

```py
variable = "some value"
f"this is a string {variable}"
```

You can also use Template strings by importing the `Template` class from the standard library. Template strings are Python strings that use placeholders for the real values. 

```py
Template("$placeholder").substitute(placeholder="real value")
```

I hope you found this article helpful and best of luck on your Python journey. 

