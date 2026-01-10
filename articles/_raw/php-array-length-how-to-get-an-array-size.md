---
title: PHP Array Length Tutorial – How to Get an Array Size
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-08-27T19:10:13.000Z'
originalURL: https://freecodecamp.org/news/php-array-length-how-to-get-an-array-size
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/count.jpg
tags:
- name: arrays
  slug: arrays
- name: PHP
  slug: php
seo_title: null
seo_desc: "By Jonathan Bossenger\nArrays are a powerful data type in PHP. And knowing\
  \ how to quickly determine the size of an array is a useful skill. \nIn this article\
  \ I'll give you a quick overview of how arrays work, and then I'll dive into how\
  \ to get the size..."
---

By Jonathan Bossenger

Arrays are a powerful data type in PHP. And knowing how to quickly determine the size of an array is a useful skill. 

In this article I'll give you a quick overview of how arrays work, and then I'll dive into how to get the size of PHP arrays.

If you already know what arrays are, you can jump straight ahead to the **[How to get an Array size?](#how-to-get-an-array-size)** section.

## What is an Array in PHP?

Before we dive into getting an array size, we need to make sure we understand what an array is. An [array in PHP](https://www.php.net/manual/en/language.types.array.php) is a variable type that allows you to store more than one piece of data. 

For example, if you were storing a simple string, you would use a PHP string type:

```php
$heading = 'PHP Array Length Tutorial';
```

However, if you wanted to store a few more pieces of separate data, you might consider using a couple of string variables.

```
$heading = 'PHP Array Length Tutorial';
$subheading = 'How to get an array size';
$author = 'Jonathan Bossenger'
```

That's all well and good, but what if you need to store more data, and quickly recall any of those items elsewhere in your code? That's where an array comes in handy. You can still store the individual pieces of data but using a single variable.

```php
$post_data = array(
    'PHP Array Length Tutorial',
    'How to get an array size',
    'Jonathan Bossenger'
);
```

Each item in that array can be referenced by its numeric key. So instead of needing to recall the single variables, you could reference a single array item by its numeric key.

```
echo $post_data[0];
```

For even more control, arrays also allow you to define your own array keys, using a string.

```
$post_data = array(
    'heading' => 'PHP Array Length Tutorial',
    'subheading' => 'How to get an array size',
    'author' => 'Jonathan Bossenger'
);
```

This allows you to also reference the array item by its string key.

```php
echo $post_data['heading'];
```

You can also define arrays using the new short array notation, which is similar to JavaScript:

```
$post_data = [
    'heading' => 'PHP Array Length Tutorial',
    'subheading' => 'How to get an array size',
    'author' => 'Jonathan Bossenger'
];
```

Arrays can also be nested, forming more complex array variables:

```
$post_data = [
    'heading' => 'PHP Array Length Tutorial',
    'subheading' => 'How to get an array size',
    'author' => [
        'name' => 'Jonathan Bossenger',
        'twitter' => 'jon_bossenger',
    ]
];

```

And, you can recall a specific array value using its nested key:

```php
echo $post_data['author']['name'];
```

However, if you find yourself regularly doing this, you might want to consider using [objects](https://www.php.net/manual/en/language.types.object.php) rather than arrays.

Arrays are useful if you need to quickly gather and then use different pieces of related data in a function, or pass that data to another function. 

By putting these pieces of data into an array, you have fewer variables defined, and it can make your code easier to read and understand later on. It's also a lot easier to pass a single array variable to another function than it is to pass multiple strings.

```
$post_data = [
    'heading' => 'PHP Array Length Tutorial',
    'subheading' => 'How to get an array size',
    'author' => [
        'name' => 'Jonathan Bossenger',
        'twitter' => 'jon_bossenger',
    ]
];

$filtered_post_data = filter_post_data($post_data)
```

## How to Get the Size of an Array in PHP

Usually when we talk about the size of an array, we're talking about how many elements exist in that array. There are two common ways to get the size of an array.

The most popular way is to use the PHP [count()](https://www.php.net/manual/en/function.count.php) function. As the function name says, `count()` will return a count of the elements of an array. But how we use the `count()` function depends on the array structure.

Let's look at the two example arrays we defined earlier.

```
$post_data = array(
	'heading' => 'PHP Array Length Tutorial',
	'subheading' => 'How to get an array size',
	'author' => 'Jonathan Bossenger'
);

echo count($post_data);
```

In this example, `count($post_data)` will result in 3. This is because there are 3 elements in that array: 'heading', 'subheading', and 'author'. But what about our second, nested array example?

```
$post_data = [
	'heading' => 'PHP Array Length Tutorial',
	'subheading' => 'How to get an array size',
	'author' => [
		'name' => 'Jonathan Bossenger',
		'twitter' => 'jon_bossenger',
	]
];
echo count($post_data);
```

Believe it or not, in this example, `count($post_data)` will also return 3. This is because by default the `count()` function only counts the top level array elements.

If you take a look at the [function definition](https://www.php.net/manual/en/function.count.php), you will see that it accepts two arguments – the array to be counted, and a `mode` integer. The default value for that mode is the predefined constant `COUNT_NORMAL`, which tells the function to only count the top level array elements.

If we pass the predefined constant `COUNT_RECURSIVE` instead, it will run through all levels of nesting, and count those instead.

```
$post_data = [
	'heading' => 'PHP Array Length Tutorial',
	'subheading' => 'How to get an array size',
	'author' => [
		'name' => 'Jonathan Bossenger',
		'twitter' => 'jon_bossenger',
	]
];
echo count($post_data, COUNT_RECURSIVE);
```

Now, the result of `count($post_data, COUNT_RECURSIVE)` will be, as expected, 5.

"But wait!", I hear you cry. "you mentioned there was another way?".

Well yes, the other function you can use is [sizeof()](https://www.php.net/manual/en/function.sizeof.php). However, `sizeof()` is just an alias of `count()`, and many folks assume (rightly so) that `sizeof()` would return the memory usage of an array. 

Therefore it's better to stick with `count()`, which is a much more suitable name for what you are doing – counting elements in an array.

Thanks for reading! I hope you now have a better understanding of how to find the size of an array in PHP.

