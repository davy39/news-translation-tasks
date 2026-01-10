---
title: The Best PHP Examples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-01T18:11:00.000Z'
originalURL: https://freecodecamp.org/news/the-best-php-examples
coverImage: https://www.freecodecamp.org/news/content/images/2020/01/php-examples.jpeg
tags:
- name: PHP
  slug: php
seo_title: null
seo_desc: 'PHP is a server-side scripting language created in 1995 by Rasmus Lerdorf.

  PHP is a widely-used open source general-purpose scripting language that is especially
  suited for web development and can be embedded into HTML.

  What is PHP used for?

  As of Oc...'
---

PHP is a server-side scripting language created in 1995 by Rasmus Lerdorf.

PHP is a widely-used open source general-purpose scripting language that is especially suited for web development and can be embedded into HTML.

### What is PHP used for?

As of October 2018, PHP is used on [80% of websites whose server-side language is known](https://w3techs.com/technologies/overview/programming_language/all). It is typically used on websites to generate web page content dynamically. Use-cases include:

* Websites and web applications (server-side scripting)
* Command line scripting
* Desktop (GUI) applications

Typically, it is used in the first form to generate web page content dynamically. For example, if you have a blog website, you might write some PHP scripts to retrieve your blog posts from a database and display them. Other uses for PHP scripts include:

* Processing and saving user input from form data
* Setting and working with website cookies
* Restricting access to certain pages of your website

The largest Social Networking Platform, [Facebook](https://www.facebook.com/) is written using PHP

### How does PHP work?

All PHP code is executed on a web server only, not on your local computer. For example, if you complete a form on a website and submit it, or click a link to a web page written in PHP, no actual PHP code runs on your computer. Instead, the form data or request for the web page gets sent to a web server to be processed by the PHP scripts. The web server then sends the processed HTML back to you (which is where 'Hypertext Preprocessor' in the name comes from), and your web browser displays the results. For this reason, you cannot see the PHP code of a website, only the resulting HTML that the PHP scripts have produced.

This is illustrated below:

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-283.png)

![Image](https://www.freecodecamp.org/news/content/images/2020/02/PHP-server-model.png)
_Source: https://github.com/xeroxism/_

PHP is an interpreted language. This means that when you make changes to your source code you can immediately test these changes, without first needing to compile your source code into binary form. Skipping the compilation step makes the development process much faster.

PHP code is enclosed between the `<?php` and `?>` tags and can then be embedded into HTML.

## Installation

PHP can be installed with or without a web server.

### GNU/Linux

On Debian based GNU/Linux distros, you can install by :

```bash
sudo apt install php
```

On Centos 6 or 7 you can install by :

```bash
sudo yum install php
```

After installing you can run any PHP files by simply doing this in terminal :

```text
php file.php
```

You can also install a localhost server to run PHP websites. For installing Apache Web Server :

```text
sudo apt install apache2 libapache2-mod-php
```

Or you can also install PHP, MySQL & Web-server all by installing

[XAMPP](https://www.apachefriends.org/download.html) (free and open-source cross-platform web server solution stack package) or similar packages like [WAMP](http://www.wampserver.com/en/)

## PHP Frameworks

Since writing the whole code for a website is not really practical/feasible for most projects, most developers tend to use frameworks for the web development. The advantage of using a framework is that

* You don't have to reinvent the wheel every time you create a project, a lot of the nuances are already taken care for you
* They are usually well-structured so that it helps in the separation of concerns
* Most frameworks tend the follow the best practices of the language
* A lot of them follow the MVC (Model-View-Controller) pattern so that it separates the presentation layer from logic

### Popular frameworks

* [CodeIgniter](https://codeigniter.com/)
* [Laravel](https://laravel.com/)
* [Symfony](https://symfony.com/)
* [Zend](http://www.zend.com/)
* [CakePHP](https://cakephp.org/)
* [FuelPHP](https://fuelphp.com/)
* [Slim](https://www.slimframework.com/)
* [Yii 2](https://www.yiiframework.com/)

## Basic Syntax

PHP scripts can be placed anywhere in a document, and always start with `<?php` and end with `?>`. Also, PHP statements end with a semicolon (;).

Here's a simple script that uses the built-in `echo` function to output the text "The Best PHP Examples" to the page:

```
<!DOCTYPE html>
<html>
<body>

<h1>Developer News</h1>

<?php echo "The Best PHP Examples"; ?>

</body>
</html> 
```

The output of that would be:

```text
Developer News

The Best PHP Examples
```

### Comments

PHP supports several ways of commenting:

* Single-line comments:
* Multi-line comments:

```
<?php
  // This is a single-line comment
  
  # You can also make single-line comments like this
?>
```

```
<?php
/*
This comment block spans
over multiple 
lines
*/
?>
```

### Case Sensitivity

All keywords, classes, and functions are NOT case sensitive.

In the example below, all three echo statements are valid:

```text
<?php
ECHO "Hello!<br>";
echo "Welcome to Developer News<br>";
EcHo "Enjoy all of the ad-free articles<br>";
?>
```

However, all variable names are case sensitive. In the example below, only the first statement is valid and will display the value of the `$name` variable. `$NAME` and `$NaMe` are both treated as different variables:

```text
<?php
$name = "Quincy";
echo "Hi! My name is " . $name . "<br>";
echo "Hi! My name is " . $NAME . "<br>";
echo "Hi! My name is " . $NaMe . "<br>";
?>
```

## Variables

Variables are the main way to store information in a PHP program.

All variables in PHP start with a leading dollar sign like `$variable_name`. To assign a variable, use the `=` operator, with the name of the variable on the left and the expression to be evaluated on the right.

**Syntax:**

```php
<?php
// Assign the value "Hello!" to the variable "greeting"
$greeting = "Hello!";
// Assign the value 8 to the variable "month"
$month = 8;
// Assign the value 2019 to the variable "year"
$year = 2019;
?>
```

### Rules for PHP variables

* Variable declarations starts with `$`, followed by the name of the variable
* Variable names can only start with an upper or lowercase letter or an underscore (`_`)
* Variable names can only contain letters, numbers, or underscores (A-z, 0-9, and `_`). Other special characters like `+ - % ( ) . &` are invalid
* Variable names are case sensitive

**Some examples of allowed variable names:**

* $my_variable
* $anotherVariable
* $the2ndVariable

### Predefined Variables

PHP has several special keywords that, while they are "valid" variable names, cannot be used for your variables. The reason for this is that the language itself has already defined those variables and they have are used for special purposes. Several examples are listed below, for a complete list see the [PHP documentation site](https://secure.php.net/manual/en/language.variables.predefined.php).

* `$this`
* `$_GET`
* `$_POST`
* `$_SERVER`
* `$_FILES`

## PHP Data Types

Variables can store data of different types such as:

* String ("Hello")
* Integer (5)
* Float (also called double) (1.0)
* Boolean ( 1 or 0 )
* Array ( array("I", "am", "an", "array") )
* Object
* NULL
* Resource

### Strings

A string is a sequence of characters. It can be any text inside quotes (single or double):

```php
$x = "Hello!";
$y = 'Hello!';
```

### Integers

An integer data type is a non-decimal number between -2,147,483,648 and 2,147,483,647.

**Rules for integers:**

* Integers must have at least one digit
* Integers must not have a decimal point
* Integers can be either positive or negative

`$x = 5;`

### Floats

A float, or floating point number, is a number with a decimal point.

`$x = 5.01;`

### Booleans

A Boolean represents two possible states: TRUE or FALSE. Booleans are often used in conditional testing.

```php
$x = true;
$y = false;
```

### Arrays

An array stores multiple values in one single variable.

`$colors = array("Magenta", "Yellow", "Cyan");`

### NULL

Null is a special data type that can only have the value `null`. Variables can be declared with no value or emptied by setting the value to `null`. Also, if a variable is created without being assigned a value, it is automatically assigned `null`.

```php
<?php
// Assign the value "Hello!" to greeting
$greeting = "Hello!";

// Empty the value greeting by setting it to null
$greeting = null;
?>
```

### Classes and Objects

A class is a data structure useful for modeling things in the real world, and can contain properties and methods. Objects are instances a class, and are a convenient way to package values and functions specific to a class.

```php
<?php
class Car {
    function Car() {
        $this->model = "Tesla";
    }
}

// create an object
$Lightning = new Car();

// show object properties
echo $Lightning->model;
?>
```

### PHP Resource

A resource is a special variable, holding a reference to an external resource. Resources are created and used by special functions. You can use [get_resource_type()](http://php.net/manual/en/function.get-resource-type.php) function to see resource type.

```php
<?php
// prints: mysql link
$c = mysql_connect();
echo get_resource_type($c) . "\n";

// prints: stream
$fp = fopen("foo", "w");
echo get_resource_type($fp) . "\n";

// prints: domxml document
$doc = new_xmldoc("1.0");
echo get_resource_type($doc->doc) . "\n";
```

## Strings

A string is series of characters. These can be used to store any textual information in your application.

There are a number of different ways to create strings in PHP.

### Single Quotes

Simple strings can be created using single quotes.

```php
$name = 'Joe';
```

To include a single quote in the string, use a backslash to escape it.

```php
$last_name = 'O\'Brian';
```

### Double Quotes

You can also create strings using double quotes.

```php
$name = "Joe";
```

To include a double quote, use a backslash to escape it.

```php
$quote = "Mary said, \"I want some toast,\" and then ran away.";
```

Double quoted strings also allow escape sequences. These are special codes that put characters in your string that represent typically invisible characters. Examples include newlines `\n`, tabs `\t`, and actual backslashes `\\`.

You can also embed PHP variables in double quoted strings to have their values added to the string.

```php
$name = 'Joe';
$greeting = "Hello $name"; // now contains the string "Hello Joe"
```

### String Functions

#### Find the length of a string

The `strlen()` function returns the length of a string.

```text
<?php
echo strlen("Developer News"); // outputs 14
?>
```

**Find the number of words in a string**  
The `str_word_count()` function returns the number of words in a string:

```text
<?php
echo str_word_count("Developer News"); // outputs 2
?>
```

#### **Reverse a String**

The `strrev()` function reverses a string:

```text
<?php
echo strrev("Developer News"); // outputs sweN repoleveD
?>
```

#### Search for text within a string

The `strpos()` function searches for text in a string:

```text
<?php
echo strpos("Developer News", "News"); // outputs 10
?>
```

#### Replace Text Within a String

The `str_replace()` function replaces text in a string:

```text
<?php
echo str_replace("freeCodeCamp", "Developer", "freeCodeCamp News"); // outputs Developer News
?>
```

## Constants

Constants are a type of variable in PHP. The `define()` function to set a constant takes three arguments - the key name, the key's value, and a Boolean (true or false) which determines whether the key's name is case-insensitive (false by default). A constant's value cannot be altered once it is set. It is used for values which rarely change (for example a database password OR API key).

### Scope

It is important to know that unlike variables, constants ALWAYS have a global scope and can be accessed from any function in the script.

```php
<?php
define("freeCodeCamp", "Learn to code and help nonprofits", false);
echo freeCodeCamp;
>?

// Output: Learn to code and help nonprofits
```

Also, when you are creating classes, you can declare your own constants.

```php
class Human {
  const TYPE_MALE = 'm';
  const TYPE_FEMALE = 'f';
  const TYPE_UNKNOWN = 'u'; // When user didn't select his gender
  
  .............
}
```

**Note:** If you want to use those constants inside the `Human` class, you can refer them as `self::CONSTANT_NAME`. If you want to use them outside the class, you need to refer them as `Human::CONSTANT_NAME`.

## Operators

PHP contains all the normal operators one would expect to find in a programming language.

A single “=” is used as the assignment operator and a double “==” or triple “===” is used for comparison.

The usual “<” and “>” can also be used for comparison and “+=” can be used to add a value and assign it at the same time.

Most notable is the use of the “.” to concatenate strings and “.=” to append one string to the end of another.

New to PHP 7.0.X is the Spaceship operator (<=>). The spaceship operator returns -1, 0 or 1 when $a is less than, equal to, or greater than $b.

```php
<?php

echo 1 <=> 1; // 0
echo 1 <=> 2; // -1
echo 2 <=> 1; // 1
```

## If / Else / Elseif Statements

If / Else is a conditional statement where depending on the truthiness of a condition, different actions will be performed.

**Note:** The `{}` brackets are only needed if the condition has more than one action statement; however, it is best practice to include them regardless.

### If Statement

```text
<?php

  if (condition) {
    statement1;
    statement2;
  }
```

**Note:** You can nest as many statements in an "if" block as you'd like; you are not limited to the amount in the examples.

### If/Else Statement

```text
<?php

  if (condition) {
    statement1;
    statement2;
  } else {
    statement3;
    statement4;
  }
```

**Note:** The `else` statement is optional.

### If/Elseif/Else Statement

```text
<?php

  if (condition1) {
    statement1;
    statement2;
  } elseif (condition2) {
    statement3;
    statement4;
  } else {
    statement5;
  }
```

**Note:** `elseif` should always be written as one word.

### Nested If/Else Statement

```text
<?php

  if (condition1) {
      if (condition2) {
        statement1;
        statement2;
      } else {
        statement3;
        statement4;
      }
  } else {
      if (condition3) {
        statement5;
        statement6;
      } else {
        statement7;
        statement8;
      }
  }
```

### Multiple Conditions

Multiple conditions can be used at once with the "or" (||), "xor", and "and" (&&) logical operators.

For instance:

```text
<?php

  if (condition1 && condition2) {
    echo 'Both conditions are true!';
  } elseif (condition1 || condition2) {
    echo 'One condition is true!';
  } else (condition1 xor condition2) {
    echo 'One condition is true, and one condition is false!';
  }
```

**Note:** It's a good practice to wrap individual conditions in parens when you have more than one (it can improve readability).

### Alternative If/Else Syntax

There is also an alternative syntax for control structures

```php
  if (condition1):
    statement1;
  else:
    statement5;
  endif;
```

### Ternary Operators

Ternary operators are basically single line if / else statements.

Suppose you need to display "Hello (user name)" if a user is logged in, and "Hello guest" if they're not logged in.

**If / Else statement**:

```text
if($user == !NULL {
  $message = 'Hello '. $user; 
} else {
  $message = 'Hello guest';
}
```

**Ternary operator**:

```text
$message = 'Hello '.($user == !NULL ? $user : 'Guest');
```

## Switch

In PHP, the `Switch` statement is very similar to the JavaScript `Switch` statement (See this [JavaScript switch statement guide](https://www.freecodecamp.org/news/javascript-switch-case-js-switch-statement-example/) to compare and contrast). It allows rapid case testing with a lot of different possible conditions, the code is also more readable.

```php
<?php
	// Switch Statement Example
	switch ($i) {
    	case "free":
    	    echo "i is free";
    	    break;
    	case "code":
    	    echo "i is code";
    	    break;
    	case "camp":
    	    echo "i is camp";
    	    break;
    	default:
    	    echo "i is freecodecamp";
            break;
	}
```

### Break

The `break;` statement exits the switch and goes on to run the rest of the application's code. If you do not use the `break;` statement you may end up running multiple cases and statements, sometimes this may be desired in which case you should not include the `break;` statement.

An example of this behavior can be seen below:

```text
<?php
    $j = 0;

    switch ($i) {
        case '2':
            $j++;
        case '1':
            $j++;
            break;
        default:
            break;
    }
```

If $i = 1, the value of $j would be:

```text
1
```

If $i = 2, the value of $j would be:

```text
2
```

While break can be omitted without causing fall-through in some instances (see below), it is generally best practice to include it for legibility and safety (see below):

```text
<?php
    switch ($i) {
        case '1':
            return 1;
        case '2':
            return 2;
        default:
            break;
     }
```

```text
<?php
    switch ($i) {
        case '1':
            return 1;
            break;
        case '2':
            return 2;
            break;
        default:
            break;
     }
```

### Example

```php
<?php
//initialize with a random integer within range
$diceNumber = mt_rand(1, 6);

//initialize
$numText = "";

//calling switch statement
  switch($diceNumber) 
  {
  case 1:
    $numText = "One";
    break;
  case 2:
    $numText = "Two";
    break;
  case 3:
  case 4:
    // case 3 and 4 will go to this line
    $numText = "Three or Four";
    break;
  case 5:
    $numText = "Five";
    echo $numText;
    // break; //without specify break or return it will continue execute to next case.
  case 6:
    $numText = "Six";
    echo $numText;
    break;
  default:
    $numText = "unknown";
  }
  
  //display result
  echo 'Dice show number '.$numText.'.';

?>
```

### Output

```text
if case is 1
> Dice show number One.

if case is 2
> Dice show number Two.

if case is 3
> Dice show number Three or Four.

if case is 4
> Dice show number Three or Four.

if case is 5
> FiveSixDice show number Six.

if case is 6
> SixDice show number Six.

if none of the above
> Dice show number unknown.
```

## Loops

When you need to repeat a task multiple times, you can use a loop instead of adding the same code over and over again.

Using a `break` within the loop can stop the loop execution.

### For loop

Loop through a block of code a specific number of times.

```php
<?php
for($index = 0; $index < 5; $index ++)
{
    echo "Current loop counter ".$index.".\n";
}
?>

/*
Output:

Current loop counter 0.
Current loop counter 1.
Current loop counter 2.
Current loop counter 3.
Current loop counter 4.
*/
```

### While loop

Loop through a block of code if a condition is true.

```php
<?php
$index = 10;
while ($index >= 0)
{
    echo "The index is ".$index.".\n";
    $index--;
}
?>

/*
Output:

The index is 10.
The index is 9.
The index is 8.
The index is 7.
The index is 6.
The index is 5.
The index is 4.
The index is 3.
The index is 2.
The index is 1.
The index is 0.
*/
```

### Do...While loop

Loop through a block of code once and continue to loop if the condition is true.

```php
<?php
$index = 3;
do
{
    // execute this at least 1 time
    echo "Index: ".$index.".\n"; 
    $index --;
}
while ($index > 0);
?>

/*
Output:

Index: 3.
Index: 2.
Index: 1.
*/
```

### Foreach loop

Loop through a block of code for each value within an array.

## Functions

A function is a block of statements that can be used repeatedly in a program.

### Simple Function + Call

```php
function say_hello() {
  return "Hello!";
}

echo say_hello();
```

### Simple Function + Parameter + Call

```php
function say_hello($friend) {
  return "Hello " . $friend . "!";
}

echo say_hello('Tommy');
```

### strtoupper - Makes all Chars BIGGER AND BIGGER!

```php
function makeItBIG($a_lot_of_names) {
  foreach($a_lot_of_names as $the_simpsons) {
    $BIG[] = strtoupper($the_simpsons);
  }
  return $BIG;
}

$a_lot_of_names = ['Homer', 'Marge', 'Bart', 'Maggy', 'Lisa'];
var_dump(makeItBIG($a_lot_of_names));
```

## Arrays

Arrays are like regular variables, but hold multiple values in an ordered list. This can be useful if you have multiple values that are all related to each other, like a list of student names or a list of capital cities.

### Types Of Arrays

In PHP, there are two types of arrays: Indexed arrays and Associative arrays. Each has their own use and we'll look at how to create these arrays.

### Indexed Array

An indexed array is a list of ordered values. Each of these values in the array is assigned an index number. Indexes for arrays always start at `0` for the first value and then increase by one from there.

```php
<?php
$shopping_list = array("eggs", "milk", "cheese");
?>
```

`$shopping_list[0]` would return `"eggs"`, `$shopping_list[1]` would return `"milk"`, and `$shopping_list[2]` would return `"cheese"`.

### Associative Array

An associative array is a list of values that are accessed via a key instead of index numbers. The key can be any value but it must be unique to the array.

```php
<?php
$student_scores = array("Joe" => 83, "Frank" => "93", "Benji" => "90");
?>
```

`$student_scores['Joe']` would return `83`, `$student_scores['Frank']` would return `93`, `$student_scores['Benji']` would return `90`.

### Multidimensional Array

A multidimensional array is an array that contains other arrays. This lets you create complex data structures that can model a very complex group of data.

```php
<?php
$students = 
  array(
    array("first_name" => "Joe", "score" => 83, "last_name" => "Smith"),
    array("first_name" => "Frank", "score" => 92, "last_name" => "Barbson"),
    array("first_name" => "Benji", "score" => 90, "last_name" => "Warner")   
  );
?>
```

Now you can get the first student's `first_name` with:

```php
$students[0]['first_name']
```

### Get The Length of an Array - The count() Function

The `count()` function is used to return the length (the number of elements) of an array:

```php
<?php
$cars = array("Volvo", "BMW", "Toyota");
echo count($cars);
?>
```

## Sorting Arrays

PHP offers several functions to sort arrays. This page describes the different functions and includes examples.

### sort()

The `sort()` function sorts the values of an array in ascending alphabetical/numerical order (E.g. A, B, C, D, E... 1, 2, 3, 4, 5...)

```php
<?php
$freecodecamp = array("free", "code", "camp");
sort($freecodecamp);
print_r($freecodecamp);
?>
```

**Output**:

```text
Array
(
    [0] => camp
    [1] => code
    [2] => free
)
```

### rsort()

The `rsort()` functions sort the values of an array in descending alphabetical/numerical order (E.g. Z, Y, X, W, V... 5, 4, 3, 2, 1...)

```php
<?php
$freecodecamp = array("free", "code", "camp");
rsort($freecodecamp);
print_r($freecodecamp);
?>
```

**Output:**

```text
Array
(
    [0] => free
    [1] => code
    [2] => camp
)
```

### asort()

The `asort()` function sorts an associative array, by its values, in ascending alphabetical/numerical order (E.g. A, B, C, D, E... 1, 2, 3, 4, 5...)

```php
<?php
$freecodecamp = array("zero"=>"free", "one"=>"code", "two"=>"camp");
asort($freecodecamp);
print_r($freecodecamp);
?>
```

**Output:**

```text
Array
(
    [two] => camp
    [one] => code
    [zero] => free
)
```

### ksort()

The `ksort()` function sorts an associative array, by its keys, in ascending alphabetical/numerical order (E.g. A, B, C, D, E... 1, 2, 3, 4, 5...)

```php
<?php
$freecodecamp = array("zero"=>"free", "one"=>"code", "two"=>"camp");
ksort($freecodecamp);
print_r($freecodecamp);
?>
```

**Output:**

```text
Array
(
    [one] => code
    [two] => camp
    [zero] => free
)
```

### arsort()

The `arsort()` function sorts an associative array, by its values, in descending alphabetical/numerical order (E.g. Z, Y, X, W, V... 5, 4, 3, 2, 1...)

```php
<?php
$freecodecamp = array("zero"=>"free", "one"=>"code", "two"=>"camp");
arsort($freecodecamp);
print_r($freecodecamp);
?>
```

**Output:**

```text
Array
(
    [zero] => free
    [one] => code
    [two] => camp
)
```

### krsort()

The `krsort()` function sorts an associative array, by its keys in descending alphabetical/numerical order (E.g. Z, Y, X, W, V... 5, 4, 3, 2, 1...)

```php
<?php
$freecodecamp = array("zero"=>"free", "one"=>"code", "two"=>"camp");
krsort($freecodecamp);
print_r($freecodecamp);
?>
```

**Output:**

```text
Array
(
    [zero] => free
    [two] => camp
    [one] => code
)
```

## Forms

Forms are a way for users to enter data or select data from the webpage. Forms can store data as well as allow the information to be retrieved for later use.

To make a form to work in languages like PHP you need some basic attributes in html. In most cases PHP uses 'post' and 'get' super global variables to get the data from form.

```html
<html>
<body>
  <form method="get" action="target_proccessor.php">
      <input type="search" name="search" /><br />
      <input type="submit" name="submit" value="Search" /><br />
  </form>
<body>
</html>
```

The 'method' attribute here tell the form the way to send the form data. Then the 'action' attribute tell where to send form data to process. Now the 'name' attribute is very important and it should be unique because in PHP the value of the name work as the identity of that input field.

## Checking Required Inputs

PHP has a few functions to check if the required inputs have been met. Those functions are `isset`, `empty`, and `is_numeric`.

### Checking form to make sure its set

The `isset` checks to see if the field has been set and isn't null. Example:

```php
$firstName = $_GET['firstName']

if(isset($firstName)){
  echo "firstName field is set". "<br>";
}
else{
  echo "The field is not set."."<br>";
}
```

## Handling Form Input

One can get form inputs with global variables $_POST and $_GET.

```text
$_POST["firstname"] or $_GET['lastname']
```

