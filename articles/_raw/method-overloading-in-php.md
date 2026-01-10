---
title: How Method Overloading Works in PHP
subtitle: ''
author: Zubair Idris Aweda
co_authors: []
series: null
date: '2023-05-15T17:11:35.000Z'
originalURL: https://freecodecamp.org/news/method-overloading-in-php
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/kisscc0-line-art-drawing-drum-cartoon-overload-5b74068a69e855.7493203415343305064338.png
tags:
- name: PHP
  slug: php
seo_title: null
seo_desc: "As software engineers, we sometimes have to perform certain tasks that\
  \ can be achieved with a variable number of inputs. \nTo solve this problem, you\
  \ can create multiple functions to solve for the different possible number of inputs.\
  \ Or we can write a..."
---

As software engineers, we sometimes have to perform certain tasks that can be achieved with a variable number of inputs. 

To solve this problem, you can create multiple functions to solve for the different possible number of inputs. Or we can write a large function to solve this problem. 

A better way to do this is to create different variations of a simple function to solve for the different scenarios you have.

In this tutorial you will learn how PHP lets you easily solve this problem using method overloading and how you can use these variations.

## What is Polymorphism?

Polymorphism is a Greek word that literally means many forms. In programming terms, it is defined as the ability of objects of different classes to respond differently based on the same message. 

Polymorphism is the concept that lets classes share the same interface and have different definitions for the same method. Polymorphism is one of the key concepts in Object Oriented Programming (OOP).

## What is Method Overloading?

Method overloading is a concept that allows you to have a method that can perform differently based on its number of parameters. It allows you have multiple definitions for a same method in the same class.  

This method will have the same name for all its uses, but might produce different output in different situations. Method overloading is a key concept under the umbrella of polymorphism.

### Traditional Overloading

For example, say you have an `add` method that you want to use to sum a couple of numbers in these ways:

```php
function add(int $a, int $b): int
{
	return $a + $b;
}

function add(int $a, int $b, int $c): int
{
	$sum = $a + $b + $c;
	return $sum > 10 ? 10 : $sum;
}
```

In the first definition, the method takes in two parameters and simply returns their sum. In the second definition, it takes three parameters and it returns the sum of these only when it's equal to 10 or less.

Now, unlike other programming languages, PHP doesn't really let you redefine a method multiple times like this:

```php
class SampleClass
{
	function add(int $a, int $b): int
	{
		return $a + $b;
	}

	function add(int $a, int $b, int $c): int
	{
		return $a + $b + $c > 10 ?? 10;
	}
}
```

You would get an error like this: `PHP Fatal error:  Cannot redeclare SampleClass::add()`. But PHP supports method overloading using a magic keyword, `__call`. 

### The `__call` keyword

This is a magic method that PHP calls when it tries to execute a method of a class and it doesn't find it. This magic keyword takes in two arguments: a function name and other arguments to be passed into the function. Its definition looks like this:

```php
function __call(string $function_name, array $arguments) {}
```

Using this magic method, you can create as many methods and as many variations of each of these methods as you like. 

For example, to achieve our intended goal with the `add` function, update the `__call` definition and your `SampleClass` to be like this:

```php
class SampleClass
{
	function __call($function_name, $arguments)
	{
		$count = count($arguments);

		// Check function name
		if ($function_name == 'add') {
			if ($count == 2) {
				return array_sum($arguments);
			} else if ($count == 3) {
				return array_sum($arguments) > 10 ? 10 : array_sum($arguments);
			}
		}
	}
}
```

The code is pretty self explanatory. Here's a step by step breakdown:

* Use the `count` method to know how many arguments are passed to your method. 
* Check the function name being passed in. This `__call` will house all the different methods you intend to create variations of, so the name should be unique and be used to group variations of the methods.
* Handle the logic as you like based on the different number of arguments. Here, we return the sum as is when we have two arguments. We return the sum if it's less than 10 when we have three arguments.
* When you call the `add` method, PHP checks for a method with the same name in the class, if it doesn't find it, it calls the `__call` method instead, and that is how the code is run.

To call the `add` method now, create a new instance of the `SampleClass` class and try it out.

```php
$sampleObject = new SampleClass;
echo $sampleObject->add(12, 12) . PHP_EOL; // Outputs 24 
echo $sampleObject->add(12, 2, 6) . PHP_EOL; // Outputs 10
```

The two variations work perfectly 🥳.

## Applications Of Method Overloading

* In sort functions: The method can be programmed to behave differently with no arguments, or with one argument, or with two depending on what you're trying to solve.
* Payment processing: The same method can be used to handle different payment processors. And these processors often need a different number of inputs to work well. So the method can figure which to use based on the number of arguments passed in and react accordingly.
* Database wrappers: A database class could have a "query" method that can handle different types of queries with the same method name. For example, the "query" method could take in a SELECT query, an INSERT query, or an UPDATE query as parameters and execute the appropriate query based on the parameter passed in.

## **Summary**

I hope you now understand what method overloading is in PHP, and how you can use it to write better PHP applications.

If you have any questions or relevant advice, please get in touch with me to share them.

To read more of my articles or follow my work, you can connect with me on [LinkedIn](https://www.linkedin.com/in/idris-aweda-zubair-5433121a3/), [Twitter](https://twitter.com/AwedaIdris), and [Github](https://github.com/Zubs). It’s quick, it’s easy, and it’s free!

