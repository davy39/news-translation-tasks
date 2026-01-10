---
title: Top Python Concepts to Know Before Learning Data Science
subtitle: ''
author: Ibrahim Ogunbiyi
co_authors: []
series: null
date: '2022-08-24T17:53:30.000Z'
originalURL: https://freecodecamp.org/news/top-python-concepts-for-data-science
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/python-data-science-concepts.jpeg
tags:
- name: Data Science
  slug: data-science
- name: Python
  slug: python
seo_title: null
seo_desc: 'If you''re interested in learning data science, you''ve likely heard the
  buzzword "Python,". It''s a popular programming language often used in data science.

  But Python is a general-purpose programming language. This means that it''s not
  limited to data ...'
---

If you're interested in learning data science, you've likely heard the buzzword **"Python,"**. It's a popular programming language often used in data science.

But Python is a general-purpose programming language. This means that it's not limited to data science alone. You can use it to develop web and mobile applications too, among other things.

So, when learning Python for data science, one of the most common mistakes beginners make is learning it "incorrectly" — that is, not learning Python in preparation for Data Science. This can result in a loss of time and effort.

In this article, we'll go through the top Python concepts you should know before delving into data science. Now relax and follow along because this will be an exciting journey.

To have a quick overview of what the journey is going to be all about, here's what we'll cover:

* [Integers and Floating-Point Numbers in Python](#heading-integers-and-floating-point-numbers-in-python)
    
* [Strings in Python](#heading-strings-in-python)
    
* [Boolean values in Python](#heading-boolean-values-in-python)
    
* [Arithmetic operators in Python](#heading-arithmetic-operators-in-python)
    
* [Comparison Operator in Python](#heading-comparison-operator-in-python)
    
* [Logical Operators in Python](#heading-logical-operators-in-python)
    
* [Membership Operator in Python](#heading-membership-operator-in-python)
    
* [F-string formatting in Python](#heading-f-string-formatting-in-python)
    
* [Lists in Python](#heading-lists-in-python)
    
* [Tuples in Python](#heading-tuples-in-python)
    
* [Dictionaries in Python](#heading-dictionaries-in-python)
    
* [`Zip()` Function in Python](#heading-zip-function-in-python)
    
* [`Enumerate()` Function in Python](#heading-enumerate-function-in-python)
    
* [`Counter()` Function in Python](#heading-counter-function-in-python)
    
* [If-else Statements in Python](#heading-if-else-statements-in-python)
    
* [`Range()` Function in Python](#heading-range-function-in-python)
    
* [List Comprehension in Python](#heading-list-comprehension-in-python)
    
* [User Defined Functions in Python](#heading-user-defined-functions-in-python)
    

## Top Python Concepts to Know for Data Science

### Why these concepts are important to Know

To put it bluntly, these concepts are what you will need to kickstart your data science journey when you want to use Python as your language for data science. You will be working with them in your day-to-day work as a data scientist, so it's good to have a firm grip on how they work.

### Integers and Floating-Point Numbers in Python

Numbers are one of the most fundamental concepts in data science. And Python contains representations (data types) for the various types of numbers that can exist. These are mostly classified into:

* Integers: these are whole numbers that are either positive or negative in Python. Examples include 200, -100, 67, and so forth.
    
* Floating-point numbers: these are decimal values that are either positive or negative. Examples include 200.65, -14.34, 53.0002, and so on.
    

### Strings in Python

In Python, strings contain alphanumeric values that are usually enclosed in single or double quotation marks.

An example includes `"FreeCodeCamp has a lot of rich resources"`.

Python has a lot of methods that you can use to manipulate strings. For example if you wish to convert a string from uppercase to lowercase, you can use the `.lower()` method in Python as shown below.

```python
string = "FREECODECAMP IS COOL"
print(string.lower())
>>> 'freecodecamp is cool'
```

You often work with strings in Data Science to create or manipulate any textual data in your dataset.

To learn more about strings and their methods, [check out this helpful handbook](https://www.freecodecamp.org/news/python-string-manipulation-handbook/).

### Boolean values in Python

Boolean values are also known as binary values. They are values represented by two numbers. `True and False`, or `0 and 1`.

### Arithmetic operators in Python

You use arithmetic operators to perform mathematical operations on two numerical operands or values. They include the following:

* The plus symbol `+` represents addition.
    
* The dash symbol `-` represents subtraction
    
* The asterisk symbol `*` represents multiplication.
    
* The slash symbol `/` represents division.
    
* The percentage symbol `%` is [used to express the modulus](https://www.freecodecamp.org/news/the-python-modulo-operator-what-does-the-symbol-mean-in-python-solved/)
    
* The double asterisk symbol `**` represents an exponent.
    
* The double slash symbol `//` represents floor division.
    

The first four operators are quite straightforward because we deal with them on a daily basis. However, the following require a bit more explanation:

#### What is the modulus operator?

The modulus operator (`%`) returns the remainder when performed on two separate numbers. For example, 8 % 3 will return 2 since 3 can only go in 8 twice, leaving a remainder of 2.

#### What is the exponential operator?

You use the exponential operator `**` to raise a number to the power of another. For example, `2**3` equals 8, because 2 is raised (or multiplied by itself) three times: `2*2*2 = 8`

#### What is the floor division operator?

You use the floor division `/` operator to divide. But unlike the other division operators which produce a decimal number, floor division returns the whole number portion of the division.

For example, `5//2` will result in 2 (because 2 goes into 5 two times evenly). The floor division does not approximate as well.

#### How to perform arithmetic operations on a string

Also, you can also perform arithmetic operations on a string. Addition and multiplication are two arithmetic operations that you can perform on a string.

* Addition operator `+`: you use the addition operator to concatenate two strings operands together (that is, you join two strings together). For example:
    

```python
"Folks" + "connect" 
>>> "Folksconnect"
```

* Multiplication operator `*`: you use the multiplication operator to repeat a string (but note that one of the operands must be a number). For example:
    

```python
2 * "Folks" 
>>> "FolksFolks"
```

### Comparison Operator in Python

You use comparison operators to compare two operands. When the comparison operators are performed on two operands they return a boolean value of either true or false. The comparison operators include:

* Greater than sign `>`
    
* Less than sign `<`
    
* Equality sign `==`
    
* Not equal sign `!=`
    
* Greater than or equals to `>=`
    
* Less than or equals to `<=`
    

Here are some examples: `2==2` will result in `True`. Also `5>= 5` will result in `True` since 5 is also equal to 5.

### Logical Operators in Python

You use logical operators to combine conditional statements. They include `and` `or` and `not`.

For example `4<5` and `3>2` will return `True`, because `4 <5` is a condition which is True and `3 > 2` is also another condition which is True. So `True` and `True` according to the logic gate will result to true.

Before we move on, I want to define a term that I will be using mostly in the rest of the article – iterables. An iterable is basically something that consists of a sequence of values, for example characters, numbers and so on. Iterables include strings, lists, dictionaries, ranges, tuples, and so on in Python.

### Membership Operator in Python

You use the membership operation to determine whether a value belongs in a sequence/iterable. A sequence can be a string of characters, a list of numbers, or anything else.

Membership operator includes the `in` operator and the `not in` operator.

For example let's say I want to check if the character `b` is in the string `"What a time to be alive"` – I can do that by typing the following statement and the result from it will be a Boolean value.

```python
"b" in "what a time to be alive"


>>> True
```

To learn more about the operators in Python check out [these](https://www.freecodecamp.org/news/basic-operators-in-python-with-examples/) [articles](https://www.freecodecamp.org/news/operators-in-python-how-to-use-logical-operators-in-python/).

### F-string formatting in Python

In some cases, you may want to insert a variable value within a string. Assume you don't know the value ahead of time but want it to be within a string. String formatting can help you achieve this.

There are several ways to format strings in Python, but we will focus on one of them: the f-literal format.

Let's look at an example: I have two variables, name and age, and I want to include them in a string and then print out the entire string.

```python
age = 10
name = "Eagle"

string = f"There are some birds of prey such as {name} that are older than {age} years."

print(string)

>>> There are some birds of prey such as Eagle that are older than 10 years.
```

So the first thing to do is you must had an f to the front of the string you wish to format using the f-literal. Also, the variable you wish to format must be inside curly braces.

To learn more about string formatting using f-literals, check out this article from [Bala Priya that explains it](https://www.freecodecamp.org/news/python-f-strings-tutorial-how-to-use-f-strings-for-string-formatting/). Also, you can learn more about other types of string formatting [here](https://www.geeksforgeeks.org/string-formatting-in-python/).

### Lists in Python

You use lists to store or organize data in a sequential order. This data can be a string, numbers, or iterables like a list.

A list is also mutable, which means that it can expand and change after you declare it (you add new elements to it).

In Python, you can create a list with square brackets and then save it to a variable. For instance:

```python
lst_of_num = [2, 3, 4, 2].
```

As we can see, the preceding is a list of numbers. The beauty of a list is that it allows you to have duplicate values in the list. As previously stated, you can create a list of different data types, such as a list of numbers, strings, and lists.

```python
diverse_lst = [4, "Folks", ["2", 4, 6, 7]]
```

To get to a list item or element, you use indexing. In Python, the first element of any iterable is always at the zero-th index position. In other words, a list's position begins with 0. As an example, the `lst_of_number` variable elements in the following index or position.

```python
lst_of_num = [2, 3, 4, 2]. 

2 -- index or position 0
3 -- index or position 1
4 -- index or position 2
2 -- index or position 3
```

You can access a list element using the following approach:

`name_of_list[index or position]`

For our case, if you want to access the element in the 3rd position you can do that by typing:

```python
print(lst_of_num[3])
>> 2
```

Lists are your friend that you'll use a lot in data science. You will need them when you wish to have a sequence of values in a container.

To learn how to add, remove, or update a list, check out this helpful tutorial by Ihechikara Vincent Abba on [how to make a list in Python](https://www.freecodecamp.org/news/how-to-make-a-list-in-python-declare-lists-in-python-example/).

### Tuples in Python

A tuple is another data collection type in Python. You also use it to store and organize data in the form of a list.

The only difference is that it is immutable, which means it cannot expand (you can't add new elements to it) like a list.

In Python, you can make a tuple by using parentheses.

```python
my_tuple = (2, 3, 5) # This is a tuple of number.

Also a tuple can contain different data types:

diverse_tuple = (2, "Golang", [4, 5, 2], ("day", "night"))
```

To access elements in a tuple, you do the same thing as with a list:

```python
my_tuple[2]
>>> 5
```

When you need a Python collection that you don't need to add a new elements to once it is created, tuples come in handy.

If you want to know more about tuples check out this [article](https://www.w3schools.com/python/python_tuples.asp). Also if you want to know more about the differences between lists and tuples, check out [this helpful article by Dionysia Lemonaki that explains it](https://www.freecodecamp.org/news/python-tuple-vs-list-what-is-the-difference/).

### Dictionaries in Python

A dictionary is a Python collection that stores data as key-value pairs. You can create a dictionary using curly braces. Also dictionaries are mutable. For example:

```python
my_dict = {"names":["Grace", "Dave", "Jack"], "scores":[45, 56, 70]}
```

The value before the column is referred to as the key and can only contain immutable datatype such as strings, integers, or tuples. The value after the column is just called a value and can contain mutable and immutable datatypes like lists, dictionaries, and so on.

You can access a dictionary's values through keys. For example, say I want to get the name of a student from the above dictionary. I can just do that easily through the use of keys, like this:

```python
print(my_dict["names"])
>>> ["Grace", "Dave", "Jack"]
```

You will often need dictionaries for key-value pairs-related tasks or when you wish to transform something into a series/dataframe in Pandas (a library you will work with mostly for data manipulation).

To learn more about dictionaries and how to add, update, or delete from a dictionary, check out [this helpful tutorial by Dionysia Lemonaki that explains them](https://www.freecodecamp.org/news/create-a-dictionary-in-python-python-dict-methods/). Here's also a [helpful article from Kolade Chris about dictionaries](https://www.freecodecamp.org/news/python-dictionary-methods-dictionaries-in-python/).

### `Zip()` Function in Python

You use the zip function to zip (combine) two iterables such as a list, tuple, dictionary, and so on. And each element of each iterable is paired together.

To put it another way, the first element of the first iterable is paired with the first element of the second iterable. You typically use the zip function to merge two lists or tuples into a dictionary. Let's see how that goes.

Let's say I have a list that contains the name of a student and another list that contains the score of each student. Now If I want to map the name of each student to their respective score, I can do that using the zip function.

```python
name = ["Dave", "Jerry", "Sasha"]
score = [43, 56, 78]
result = zip(name, score)
```

Now we are finished – but if you print the result from the above code, it's always an Iterator object. The last thing we will need to do is to make use of a dict function – which you use to convert an iterable into a dictionary.

```python
print(dict(result)
>>> {"Dave":43, "Jerry":56, "Sasha":78}
```

You will often use the `zip()` function to join list into a dictionary in Data Science.

To learn more about `zip()` function check out this helpful tutorial by Ihechikara Vincent Abba [here.](https://www.freecodecamp.org/news/python-zip-zip-function-in-python/)

### `Enumerate()` Function in Python

In Python, you use the enumerate function to assign or pair index or position values to the values in an iterable (remember, index values start at 0).

Once those index values are paired to the iterable values, you can decide to turn it into a dictionary where the index values will now serve as a key for the values in the iterable.

Let's look at an example to see how it works.

```python
lst = ["Free", "Code", "Camp"]
result = dict(enumerate(s))
print(result)
>>> {0: 'Free', 1: 'Code', 2: 'Camp', 3: 'Code'}
```

You will often use the `Enumerate()` function to assign an index to a list and then turn it to a dictionary.

### `Counter()` Function in Python

The counter function, as the name implies, lets you count the number of times the values in an iterable occurs.

The counter function produces a counter object in the form of a dictionary. To use the counter() we will need to import it from the collection module. Let's see how that works.

```python
from collections import Counter
lst = ["Free", "Code", "Camp", "Code", "Free"]
print(Counter(lst))
>>> Counter({'Free': 2, 'Code': 2, 'Camp': 1})
```

You will often use the `Counter` function when performing natural language processing in data science.

### If-else Statements in Python

You use if-else statements when you want to execute a task based on a certain condition. In real life, for example, if you pass your exam, you will be promoted. But if you fail, you will have to take it again in order to be promoted.

This type of expression, it turns out, can also be executed in Python using the if-else statement. This is how you write an if else statement:

```python
if condition:
	execute statement
else:
	execute statement
```

In our exam example, the condition for the above expression is whether you pass or not, and the executable statement is whether you pass or not.

Now what the above expression does is if the condition is evaluated to true, the executable statement inside the if block gets executed. If the condition is not true, the executable statement inside the else block gets executed.

Let's go over an example so we can grok what we just talked about.

Assume I have a list of numbers like `[4, 5, 6, 8, 10]`, and I have a variable `i` with the value `6`. Now I need to write an if-else statement that will print whether or not the `i` is in the list.

As you might expect, our condition will be whether or not `i` is in the list, and our executable statement will be to print a message to us. You can do this using the code provided above like this:

```python
lst = [4, 5, 6, 8, 10]
i = 6

if i in lst:
	print("Yes 6 is present in the list")
else:
	print("No 6 is not present in the list")
    
>>> "Yes 6 is present in the list"
```

The `i in lst` is the conditional statement that evaluates to `True` or `False`. If `i` was not present in the list then the executable statement in the else block gets printed.

You will often need if-else statements to perform conditional operations in Data science.

To learn more about if-else statements, check out this article written by Dionysia Lemonaki that [explains Python if-else statements simply](https://www.freecodecamp.org/news/python-else-if-statement-example/).

### `Range()` Function in Python

The range function, as the name implies, provides a sequence of values within a specific range when needed. It basically works like this: (start, end-1). That is, it will not include the last value.

So, let's say I want a list of numbers ranging from 2 to 10. So I can easily do that with the range function and then convert the result to a list instead of creating a list and then typing out those items. For example:

```python
# rememeber it's end-1 so it will display values from 2 to 10
no_range = range(2, 11)
print(list(no_range))
>>> [2, 3, 4, 5, 6, 7, 8, 9, 10]
```

You will often need the `range()` function when you need to get a list of numbers with a long range in data science.

To learn more about range function check out this helpful tutorial from Bala Priya [here](https://www.freecodecamp.org/news/python-range-function-explained-with-code-examples/).

### For-Loops in Python

The for loop statement allows you to repeat a task a predefined number of times. The syntax for a for-loop basically looks like this:

```python
for i in iterable:
	execute statement
    
   
where i is a variable (you can change its name to anything you prefer) which stands as a place holder to access all the items in the iterable (for example dictionary, list, string, etc.)
```

Assume I have a list containing the names of thousands of students and I want to print those names. Now instead of doing it the manual way (where I access the names in the list through indexing like `print(names[10])` up to the `1000th` element), I can easily employ a for-loop since I want to perform the same task repeatedly.

For example:

```python
lst  = ["Free", "Code", "Camp", "is", "the", "best", "place", "to", "learn"]
for i in lst:
	print(i)
```

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-123.png align="left")

You will often need for loops in Data Science to iterate through an iterable and perform some certain task.

We can see that the `i` variable serves as a placeholder to access each item in the list. To learn more about for-loops and all their applications check out this helpful tutorial by Kolade Chris [here](https://www.freecodecamp.org/news/python-for-loop-example-how-to-write-loops-in-python/).

### List Comprehension in Python

A list comprehension is a simple method of generating a new list from another iterable using specific operations.

Assume I have a tuple with some values and want to make a new list from it that only contains values from the tuple that can be divided by 3.

One method is to create an empty list and then use a for loop to iterate through all of the elements in the tuple. You also create an if-else statement to match the condition you want and then append the values that match that condition to the empty list you initialized. Here's what that looks like in code:

```python
my_tuple = (2, 3, 4, 6, 10, 12)
my_new_lst = []
for i in my_tuple:
	if i % 3 == 0:
    	my_new_lst.append(i)
print(my_new_lst)
>>> [3, 6, 12]
```

I can also do that using list comprehension in just one line of code. Let's see how that's done:

```python
my_tuple = (2, 3, 4, 6, 10, 12)

my_new_lst = [i for i in my_tuple if i % 3 == 0]
print(my_new_lst)

>>>[3, 6, 12]
```

So far, we've seen that the list comprehension resembles the above line of code.

To begin, we use the for-loop to iterate through the tuple, with `i` acting as a placeholder for each item in the tuple. Now `i` will be evaluated to see if the condition is met (that is for each element `i` represents in the tuple). So if `i` condition evaluates to true, `i` will be added to the newly created list.

You will often need list comprehension in Data Science when you need a simple way to create a new list from an existing list.

To learn more about list comprehension check out this helpful tutorial by Dionysia Lemonaki [here](https://www.freecodecamp.org/news/list-comprehension-in-python-with-code-examples/).

### User Defined Functions in Python

User defined means functions you create yourself from scratch.

You use functions to modularize or group a large amount of code into smaller pieces. Functions are useful when you need to execute a set of code repeatedly. Instead of typing out that code again and again whenever you need it, you can easily modularize it into a function and then call the function (which is just a one-line statement) whenever you need it.

In Python, you create a function in the following manner.

```python
def function_name(parameter1, parameter2, ....):
	
    //execute statement
    
    return value
```

* `Parameter` in the function serves as a placeholder to hold any value you want to pass inside the function executable statement. You can have more than one parameter depending on what you wish to achieve.
    
* `Execute statement` means the code that you wish to execute any time you call the function.
    
* `return` is a keyword. It's not compulsory for a function to return a value. You might decide not to return anything.
    

Let's look at an example of how to write a function. For example, suppose you want to run some Python code that asks for a person's name and age. You also want to create a conditional statement that prints a message based on the person's age.

Now you wish to execute this code over and over again because you want to try it out on different people. You can easily write a function that will group this code into a piece, which you can then call whenever you need it.

```python
def print_func(person_name, person_age):
    if person_age > 10:
        print(f"Hi {person_name} you are more than your denary age and your name contains {len(person_name)} characters.")
    else:
         print(f"Hi {person_name} you are still in your denary age and your name contains {len(person_name)} characters.")
```

Now let's go over what we have above. We created a function named `print_func` which requires two parameters that we want to pass into it: they are `person_name` and `person_age`.

Also the executable statement is the if -else statement we created inside it which will print out a message if a person's age is greater than 10 and another message if it is not.

You can see that we make use of string formatting to print the person's name and the length of the person's name. Also we decided not to return anything since we just want to print a value to the console.

Now if you wish to call this function, you will call it with its name and the parameters it requires. In our case it requires name and age.

```python
name = "Ibrahim"
age = 12
print_func(name, age)

>>> Hi Ibrahim you are more than your denary age and your name contains 7 characters.
```

You will often need functions to modularize your code in Data Science.

To learn more about how to create function check out this helpful tutorial on functions for beginners from Bala Priya [here](https://www.freecodecamp.org/news/functions-in-python-a-beginners-guide/). Also check this one from Dionysia Lemonaki on how to declare and invoke functions with params [here](https://www.freecodecamp.org/news/python-function-examples-how-to-declare-and-invoke-with-parameters-2/).

## Conclusion

We've come to the end of this long journey. You may be wondering whether you should learn advanced topics like object-oriented programming (OOP), which includes concepts like classes, before learning data science.

To answer your question directly, it's not necessary. The majority of your data science work will revolve around these concepts we discussed in this tutorial, and you will primarily use functions to modularize your code.

Still, as your knowledge grows, it's useful to learn OOP in case you need to contribute to an open source project.

Thank you for taking the time to read this article. I hope you learned a thing or two.
