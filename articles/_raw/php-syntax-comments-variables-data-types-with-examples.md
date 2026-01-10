---
title: Learn PHP Syntax, Comments, Variables and Data Types – with Examples
subtitle: ''
author: Okoro Emmanuel Nzube
co_authors: []
series: null
date: '2022-06-10T20:18:35.000Z'
originalURL: https://freecodecamp.org/news/php-syntax-comments-variables-data-types-with-examples
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/PHP--SYNTAX--COMMENTS-1.png
tags:
- name: PHP
  slug: php
seo_title: null
seo_desc: 'Welcome to today''s tutorial, everyone. In my last article, I walked you
  through what PHP is and how to get it set up along with XAMPP.

  And today, we''ll review those introductory PHP concepts and then dive into the
  language a bit more in depth. We''ll ...'
---

Welcome to today's tutorial, everyone. [In my last article](https://www.freecodecamp.org/news/how-to-get-started-with-php/), I walked you through what PHP is and how to get it set up along with XAMPP.

And today, we'll review those introductory PHP concepts and then dive into the language a bit more in depth. We'll look at PHP syntax, comments, data types, and variables, among other things.

## PHP Setup

Here's a quick rundown of how to get PHP up and running in your project.

Go to the [PHP website](https://www.php.net/), click on download in the navigation bar at the top, scroll down to where you see Windows Downloads, and click on it.

When you click on Windows Download, a new page should show up. Just scroll down until you see VS16 x64 Thread Safe (2022-Jun-07 22:31:20), then click on the zip file to download PHP.

When the download is finished, go to the downloads folder in your computer, extract the PHP folder from the zip file, open the extracted PHP folder, right-click php.exe, and choose run as administrator.

[You can read more here](https://www.freecodecamp.org/news/how-to-get-started-with-php/) for a detailed description of how to set up PHP for your code.

## PHP Syntax

You can embed PHP code anywhere in a document. It starts with an opening tag of `<?php (the PHP code goes in here)` and ends with a closing tag `?>`.

All PHP statements end with a semicolon `;`. A PHP file is always named with the file extension of `.php` – for example, `index.php` or `home.php`.

PHP code usually contains HTML code inside, for example:

```php
<?php
	echo “ <h1> GOOD BYE WORLD, SEE YOU NEXT TIME </h1>”;
	echo “<p> This is me leaving the website at this point in the day </p>”;
?>
```

From the code above, it we can see that our PHP code contains two lines of HTML code in it – the `h1` tag and the `p` tag. The `h1` tag (heading 1) will be displayed in a very big and bold format, while the `p` tag (paragraphs) will be displayed in the browser normally. Note that all the code above ended with a semi-colon `;`.

## Comments in PHP

As a developer, comments are crucial. Adding comments to your code makes it easier to read and understand.

In some cases, you may need to return to code that you wrote previously, but you'll struggle to solve the problem if you didn't explain what you were doing with comments.

When you comment something out, it won't show up in the web browser. In PHP, you can write single line comments and multiple line comments.

### How to Write Single-Line Comments in PHP

Just as the name states, a single line comment just comments out everything in one line. You can use the forward slash (`/`) or hash symbol (`#`) in PHP to denote a single line comment. For example:

```php
<?php
//This is a PHP Heading 1 
echo"<h1> PHP Heading 1</h1>";

#This is a PHP Heading 2
echo"<h1> PHP Heading 2</h1>";
?>
```

The code above shows the two ways to execute a single line comment in PHP.

### How to Write Multiple-Line Comments in PHP

This comments everything in multiple lines. You can use the symbol `/* (the comment goes in-between) */` to include a multi-line comment.

When you comment out multiple lines of code, it will not be displayed in the web browser. For example:

```php
<?php
	/*This is a PHP Heading
	the h1 tag displays text very bold and big, and the p tag below is the paragraph tag and will be displayed below the heading.
	*/
	echo"<h1> PHP Heading</h1>";
	echo "<p> This is the paragraph </p>";
?>
```

The multiple line comment that you can see in the code above can be said to have two tags: one is the opening tag which is `/*` and the other is the closing tag `*/`. Your comment text/code goes in-between the two tags.

## Variables in PHP

A variable is a container that stores or houses data or values. In PHP, you create a variable with the dollar symbol `$` followed by the variable name.

For a variable to be assigned to a value, we use the `=` symbol. Here are a few important things to note about PHP variables:

* A variable is declared/executed with a dollar symbol `$` then the variable name.
    
* Variable names are case sensitive. For example `$Derek` is very different from `$DEREK`.
    
* A variable name should not and cannot start with a number, but rather a letter (Aa – Zz) or an underscore (\_).
    

Here are some examples of naming variables in PHP:

```php
<?php
	$color = "red";
	echo "$color"; //THIS CODE OUTPUTS THE COLOR RED TO THE WEB BROWSER
	echo "</br>";

	$COLOR = "Blue";
	echo "$COLOR"; //THIS CODE OUTPUTS THE COLOR BLUE TO THE WEB BROWSER
	echo "</br>";

	$_price = "1000";
	echo "$_price"; //THIS CODE OUTPUTS THE PRICE 1000 TO THE WEB BROWSER
	echo "</br>";

	$_PRICE = "900";
	echo "$_PRICE"; //THIS CODE OUTPUTS THE PRICE 900 TO THE WEB BROWSER
?>
```

The code above shows the different ways of naming variables in PHP.

## Data Types in PHP

Variables in PHP store values of different data types. Now let's discuss some data types that work with PHP:

* `String`
    
* `Integer`
    
* `Float`
    
* `Boolean`
    

### String data type

A string is a data type which is represented with some text inside double quotes `" "`. A string can also hold numbers and special characters but they should be enclosed in the quotes. For example:

```php
<?php
	$name = "Derek Emmmanel";
	echo "$name";
    
    echo "<br>";
    
	$price = “1234567”;
	Echo “$price”;
?>
```

From the code above, the variable values `“Derek Emmanuel”;` and `"1234567"` are of the `string` data type because they are enclosed in quotes.

We can use another method to run the above code in our web browser. For example:

```php
<?php
$name = "Derek Emmmanel";
var_dump($name);
?>
```

In the code above, I used the `var_dump` keyword to execute my PHP code. `Var_dump` not only displays your code to your web browser, but also helps you identify what data type you are working with and how many values it contains.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/localhost_Demo_test.php---Google-Chrome-6_8_2022-7_49_26-AM.png align="left")

*var\_dump keyword*

### Integer data type

Integers are whole numbers that have no decimal point. Integers can either be negative numbers (-34567) or positive numbers (34567). For example:

```php
<?php
	$ad = 12345;
	var_dump($ad);
?>
```

The code above is an example of the integer data type.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/localhost_Demo_test.php---Google-Chrome-6_8_2022-8_36_54-AM.png align="left")

### Float data type

Floats are not whole numbers, but rather they are numbers with decimal points. Floats can also be negative decimal numbers (-34.567) or positive decimal numbers (34.567). For example:

```python
<?php
	$fl = 34.567;
	var_dump($fl);
?>
```

### Boolean data type

Boolean is a data type that represents two possible outcome, `true` or `false`. Booleans are used mostly when we are working with conditional statements like `if`, `else`, `elseif`, and `swtich`. For example:

```php
$house = true;
$city = false;
```

## Conclusion

I hope you've learned a lot from today's tutorial. Stay tuned for our next topic.

Happy Coding!
