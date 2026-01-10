---
title: PHP Array – How to Use Arrays in Your PHP Projects
subtitle: ''
author: Okoro Emmanuel Nzube
co_authors: []
series: null
date: '2022-06-22T17:30:59.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-arrays-in-php
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/Arrays-in-PHP-final.png
tags:
- name: arrays
  slug: arrays
- name: PHP
  slug: php
seo_title: null
seo_desc: 'An array is a special variable that we use to store or hold more than one
  value in a single variable without having to create more variables to store those
  values.

  To create an array in PHP, we use the array function array( ).

  By default, an array of...'
---

An array is a special variable that we use to store or hold more than one value in a single variable without having to create more variables to store those values.

To create an array in PHP, we use the array function `array( )`.

By default, an array of any variable starts with the `0` index. So whenever you want to call the first value of an array you start with `0` then the next is `1`...and so on.

There are different types of arrays in PHP. They are:

* Numeric/Indexed Arrays
    
* Associative Arrays
    
* Multidimensional Arrays
    

Let's look at how each one works in more detail.

## What are Numerical or Indexed Arrays?

A numerical array is a type of array which can store strings, numbers, and objects. Here's an example of a numeric array:

```php
<?php
// Numeric/ index arrays
$cars = array('Mecedes Benz', 'Hilux', 'Highlander', 'Hummer', 'Limozien');
var_dump($cars);
?>
```

From the code above I have a variable of `$cars` which stores an array of 5 elements. The `var_dump($cars)` keyword above will show us the total number of elements we have in the array, the index number of each array, and also the length of each element in the array.

You can also chose to use the `echo( )` keyword, but in my case I prefer to use `var_dump( )` because it gives a more detailed explanation of the results we get.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/localhost_CODE_Arrays_arrays.php---Google-Chrome-6_15_2022-8_44_07-PM.png align="left")

You can also choose to display only one element/item of an array in the web browser by doing this:

```php
<?php
$numbers = array('8', '20', '40', '58', '88', '200', '400', '500');
var_dump ($numbers [4]);
?>
```

The code above follows the same pattern as our definition of an array, which states that it counts from zero. We want to display the element with the index of `4`. Counting from `0 to 4`, we can see that `88` falls under index `4`, indicating that `88` is the number we're seeking and that will be displayed to the browser.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/localhost_CODE_Arrays_arrays.php---Google-Chrome-6_17_2022-8_17_58-PM.png align="left")

## What are Associative Arrays?

An associative array is a type of array where the key has its own value. In an associative array, we make use of `key` and `value`.

`Key`s are descriptive captions of the array element used to access the value of the array. And `value` is the value assigned to the array element.

There are situations where you shouldn't use the numeric/indexed array, such as:

* When you want to store the age of different students along with their names.
    
* When you want to record the salaries of your employees.
    
* When you want to store the score of a student in different subjects
    

and so on.

Suppose we want to assign ages to a group of high school students with their names.

We can use the Associative array method to get it done. For example:

```php
<?php
$student_age = array (
'Scott_Mcall' => 17,
'Stalenski' => 18,
'Lydia' => 16,
'Allision' => 17,
);

echo $student_age ['Scott_Mcall']; //this code will display the age of Scot_Mcall as 17
echo $student_age ['Stalenski']; //this code will display the age of stalenski as 18
echo $student_age ['Lydia']; //this code will display the age of Lydia as 16
echo $student_age ['Allision']; //this code will display the age of Allision as 17
?>
```

The code above is an example of an associative array. The `key`s of the array are `scott_Mcall`, `Stalenski`, `Lydia`, `Allision`, and we used them to assign the age to each student. The `value`s of the array are `17`, `18`, `16`, and `17`.

## What are Multidimensional Arrays?

You can think of a multidimensional array as an array of arrays. This means that every element in the array holds a sub-array within it. In general, multidimensional arrays allow you to store multiple arrays in a single variable.

Suppose we want to store the Names, Registration Numbers, and Emails of some of the staff working in a particular company. We can use multidimensional arrays to archive this.

For example:

```php
<?php
$Staffs = [
	[
		'Name' => 'Derek Emmanuel',
		'Reg_No' => 'FE/30304',
		'Email' => 'derekemmanuel@gmail.com'
	],
	[
		'Name' => 'Rubecca Michealson',
		'Reg_No' => 'FE/20003',
		'Email' => 'rmichealsongmail.com'
	],
	[
		'Name' => 'Frank Castle',
		'Reg_No' => 'FE/10002',
		'Email' => 'fcastle86@gmail.com'
	]
];
echo $Staffs [2] ['Email']; // This displays the email of the last staff which is fcastle86@gmail.com

echo $staffs [0] ['Name']; //This displays the Name of the staff in the first array (index 0) which is Derek Emmanuel 

// you can access the information of any staff you wish to by using echo $(variable name) [index number] ['array element key'].


?>
```

Remember, an array starts counting from index `0`. The code above is an example of a multidimensional array because it contains more than one array (an array of arrays) with one single variable of `$staff`.

The `echo $staff [2] [‘Email’]` displays the email of the staff that falls into the index of `2`. In our case it will display [`fcastle86@gmail.com`](mailto:fcastle86@gmail.com).

If I want to access the Email of the staff in the first array, we'll do the following:

`echo $staff [0] ['Email'];`

Using the method above, you can access and display any information in the array from the code above.

## Conclusion

At this point you should be able to use the three different types of arrays when working on a PHP project.

Thank you for reading.

Have fun coding!
