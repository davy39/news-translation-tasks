---
title: Lambda Sorted in Python – How to Lambda Sort a List
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2023-03-16T19:37:09.000Z'
originalURL: https://freecodecamp.org/news/lambda-sort-list-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/lambdaSort.png
tags:
- name: lambda
  slug: lambda
- name: Python
  slug: python
seo_title: null
seo_desc: "The sort() method and the sorted() function let you sort iterable data\
  \ like lists and tuples in ascending or descending order. \nThey take parameters\
  \ with which you can modify how they perform the sorting. And one of those parameters\
  \ could be a functi..."
---

The `sort()` method and the `sorted()` function let you sort iterable data like lists and tuples in ascending or descending order. 

They take parameters with which you can modify how they perform the sorting. And one of those parameters could be a function or even a lambda function.

In this article, you’ll learn how to sort a list with the lambda function.


## What We'll Cover
- [How to Sort a List in Python](#heading-how-to-sort-a-list-in-python)
- [What is a Lambda Function?](#heading-what-is-a-lambda-function)
- [How to Sort a List with the Lambda Function](#heading-how-to-sort-a-list-with-the-lambda-function)
  - [How to Lambdasort with the `sort()` Method](#heading-how-to-lambdasort-with-the-sort-method)
  - [How to Lambdasort with the `sorted()` Function](#heading-how-to-lambdasort-with-the-sorted-function)
- [Conclusion](#heading-conclusion)


## How to Sort a List in Python
You can sort a list with the `sort()` method and `sorted()` function. 

The `sort()` method takes two parameters – `key` and `reverse`. You can use a function as the key, but the reverse parameter can only take a Boolean. 

If you specify the value of the reverse parameter as `True`, the `sort()` method will perform the sorting in descending order. And if you specify `false` as the value of the `reverse`, the sorting will be in ascending order. You don’t even need to specify false as the value because it’s the default.

But both parameters are optional, so the method still works fine without them:

```py
name_list = ['Zen Jack', 'Luigi Austin', 'Ben Benson', 'John Ann']
print("Original names:", name_list) # Original names: ['Zen Jack', 'Luigi Austin', 'Ben Benson', 'John Ann']


name_list.sort()
print("Sorted names:", name_list) # Sorted names: ['Ben Benson', 'John Ann', 'Luigi Austin', 'Zen Jack']


num_list = [34, 11, 35, 89, 37]
print("Original numbers:", num_list) # Original numbers: [34, 11, 35, 89, 37]


num_list.sort()
print("Sorted numbers:", num_list) # Sorted numbers: [11, 34, 35, 37, 89]
```

The `sorted()` function, on the other hand, also works like `sort()`. It takes the optional `key` and `reverse` parameters too, but it takes a compulsory parameter of the iterable you want to sort – making it ideal for sorting other iterables apart from a list.

Here’s how the `sorted()` function works:
```py
name_list = ['Zen Jack', 'Luigi Austin', 'Ben Benson', 'John Ann']
print("Original names:", name_list) # Original names: ['Zen Jack', 'Luigi Austin', 'Ben Benson', 'John Ann']


sorted(name_list)
print("Sorted names:", name_list) # Sorted names: ['Ben Benson', 'John Ann', 'Luigi Austin', 'Zen Jack']


num_list = [34, 11, 35, 89, 37]
print("Original numbers:", num_list) # Original numbers: [34, 11, 35, 89, 37]


sorted(num_list)
print("Sorted numbers:", num_list) # Sorted numbers: [11, 34, 35, 37, 89]
```

As I pointed out earlier, you can also sort other iterables with the `sorted()` function. This is how I sorted a tuple with the `sorted()` function:
```py
name_tuple = ('Zen Jack', 'Luigi Austin', 'Ben Benson', 'John Ann')
print("Original tuple:", name_tuple) # Original tuple: ('Zen Jack', 'Luigi Austin', 'Ben Benson', 'John Ann')


sorted(name_tuple)
print("Sorted tuple:", name_tuple) # Sorted tuple: ('Zen Jack', 'Luigi Austin', 'Ben Benson', 'John Ann')
```

Remember I also pointed out you can pass a function as the value for the key parameter of the `sort()` method and `sorted()` function. This function can help you be more decisive with the way you want to sort the iterable list or tuple.

For example, the `sorted()` function and `sort()` method would only sort by the first part of the string or number. But you can also sort by the second part by passing in a function as the key parameter. It is with this function that you will decide how you want to sort the list or other iterables.

A lambda function would be ideal to do this because it takes one expression. But before we dive into sorting with a lambda function, let me remind you what the lambda function is.


## What is a Lambda Function?
A lambda function is an anonymous function – a function you don’t write with the `def` keyword. A lambda function can take many arguments, but it can only have one expression.

Since you don’t define a lambda function with the `def` keyword, how do you call it? You can assign a lambda function to a variable, then call it by the name of that variable.

In the example below, the `addNum` lambda function has 3 arguments and adds them together:

```py
addNums = lambda a, b, c : a + b + c


res = addNums(4, 12, 4)
print(res) #20
``` 


## How to Sort a List with the Lambda Function
You can “lambda sort” a list with both the `sort()` method and the `sorted()` function. Let’s look at how to lambda sort with the `sort()` method first.


### How to Lambdasort with the `sort()` Method
Let’s take the names we sorted before and sort them by the second name. This lambda function would be ideal in sorting by the second name:

```py
lambda name: name.split()[1]
```
The lambda function splits a name and takes the second part of the name – the second name. The first part is the first name and it would be `[0]`.

You can pass in this lambda function as the key parameter – sorting the names by the second names:
```py
name_list = ['Zen Jack', 'Luigi Austin', 'Ben Benson', 'John Ann']
print("Original list", name_list) # Original list ['Zen Jack', 'Luigi Austin', 'Ben Benson', 'John Ann']


name_list.sort(key=lambda name: name.split()[1])
print("Sorted name list", name_list) # Sorted name list ['John Ann', 'Luigi Austin', 'Ben Benson', 'Zen Jack']
```

You can see the names got sorted by the alphabetical order of the second names. `John Ann` came first, and `Zen Jack` came last. Ann starts with A and Jack starts with J.

If you want, you can even pass in a function directly. What you need to do is to not call the function. You have to pass it in as an object.
```py
name_list = ['Zen Jack', 'Luigi Austin', 'Ben Benson', 'John Ann']
print("Original list", name_list) # Original list ['Zen Jack', 'Luigi Austin', 'Ben Benson', 'John Ann']


def sort_by_second_name(name):
    return name.split()[1]


name_list.sort(key=sort_by_second_name)
print("Sorted name list", name_list) # Sorted name list ['John Ann', 'Luigi Austin', 'Ben Benson', 'Zen Jack']
```

Now, let’s sort the numbers based on their last digits. In case you don’t know, if you use the remainder (`%`) operator on two numbers, it divides the two numbers and returns the remainder: 

```py
print(4 % 2) # returns 0
print(44 % 11) # returns 0
print(104 % 60) # returns 44
print(21 % 2) # returns 1
```

But if you “mod” a number with multiple digits with 10, it returns the last digit of the number:
```py
print (44 % 10) # returns 4
print (402 % 10) # returns 2
print (152 % 10) # returns 2
print (1596 % 10) # returns 6
```

That’s how you can get the second number and sort the numbers based on it.

Here’s how I sorted the numbers from the previous examples with a lambda function:
```py
num_list = [22, 34, 11, 35, 89, 37, 93, 56, 108]
print('Original Number:', num_list) # Original Number: [22, 34, 11, 35, 89, 37, 93, 56, 108]


num_list.sort(key=lambda num: num % 10)
print('Lambda sorted number:', num_list) # Lambda sorted number: [11, 22, 93, 34, 35, 56, 37, 108, 89]
```

As you can see, this lambda function, ` lambda num: num % 10` is responsible for sorting the numbers based on each of the second digits. I passed in the number to the lambda function and got the last digit with `% 10`. This lambda function runs through each of the numbers and gets their last digits.

If you want, you can even pass in a function directly as the key:
```py
num_list = [22, 34, 11, 35, 89, 37, 93, 56, 108]
print('Original Number:', num_list) # Original Number: [22, 34, 11, 35, 89, 37, 93, 56, 108]


def sort_by_second_num(num):
    return num % 10


num_list.sort(key=sort_by_second_num)
print('Lambda sorted number:', num_list) # Lambda sorted number: [11, 22, 93, 34, 35, 56, 37, 108, 89]
```


### How to Lambdasort with the `sorted()` Function
In this example, we are going to sort a list of tuples using the jersey numbers of some footballers.

The only difference between the `sort()` and `sorted()` method is that `sorted()` takes a compulsory iterable and `sort()` does not.

So, to lambda sort with the `sorted()` function, all you need to do is pass in the list as the iterable and your lambda function as the key:

```py
 footballers_and_nums = [("Fabregas", 4),("Beckham" ,10),("Yak", 9), ("Lampard", 8), ("Ronaldo", 7), ("Terry", 26), ("Van der Saar", 1), ("Yobo", 2)]


sorted_footballers_and_nums = sorted(footballers_and_nums, key=lambda index : index[1])


print("Original footballers and jersey numbers", footballers_and_nums) # Original footballers and jersey numbers [('Fabregas', 4), ('Beckham', 10), ('Yak', 9), ('Lampard', 8), ('Ronaldo', 7), ('Terry', 26), ('Van der Saar', 1), ('Yobo', 2)]


print("Sorted footballers by jersey numbers:", sorted_footballers_and_nums) # Sorted footballers by jersey numbers: [('Van der Saar', 1), ('Yobo', 2), ('Fabregas', 4), ('Ronaldo', 7), ('Lampard', 8), ('Yak', 9), ('Beckham', 10), ('Terry', 26)]
```

The lambda function that performed the sorting is this ` lambda index : index[1])`. The lambda went through all the tuples in the list, took the second index (`[1]`), and used those to do the sorting.


## Conclusion
This article showed you how to sort a list with the `sort()` method and `sorted()` function using a lambda function.

But that was not all. We looked at how both the `sort()` method and `sorted()` function work on their own without a lambda function. I also reminded you of what the lambda function is, so you could understand how I did the sorting with a lambda function.

Thank you for reading!


