---
title: How to Convert a String to an Integer in C# – with Code Examples
subtitle: ''
author: Israel Chidera
co_authors: []
series: null
date: '2023-02-23T23:22:15.000Z'
originalURL: https://freecodecamp.org/news/how-to-convert-a-string-to-an-integer-in-c-sharp
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/luca-bravo-XJXWbfSo2f0-unsplash.jpg
tags:
- name: C
  slug: c
seo_title: null
seo_desc: 'There are various situations where you need to convert a string to a number.
  Whether you are working with user input or data from an external source, converting
  a string to a number is a common task for developers.

  This article will explore some of t...'
---

There are various situations where you need to convert a string to a number. Whether you are working with user input or data from an external source, converting a string to a number is a common task for developers.

This article will explore some of the most common methods to convert a string to an integer in C# using the **`int.Parse()`**, **`int.TryParse()`**, and **`Convert.ToInt32()`** methods. 

This article will also provide examples to help you understand the syntax of each method. Whether you are a beginner or an experienced programmer, this guide will provide a user-friendly introduction to the topic.

The **`Int`** keyword is an alias for the **`System.Int32`** type, and it is utilized for declaring variables that can hold 32-bit signed integers within the range of -2,147,483,648 to 2,147,483,647. **`Int32`** is a built-in value type that represents a 32-bit signed integer. You can convert a string to an Int using the following method.

## How to Convert a String to an Int Using `Int32.Parse()`

`Int32.Parse()` is the easiest way to convert a string to an integer. It takes a string as a parameter. Here is an example:

```cs
string numberString = “8”;
int i = int.Parse(numberString); 
Console.WriteLine("Value of i: {0}", i);
```

The above code shows how to convert a string to an Integer using the **`int.Parse()`** method. The method takes a string variable called **`numberString`** and converts it to an int. 

The downside of using the **`int.Parse()`** method is that an exception will be thrown if it cannot be successfully parsed to an integer. To avoid this issue, you can use a try-catch block while using **`int.Parse()`**. Here is how to do this:

```cs
string numString = "12"; 
try
{
    int num = int.Parse(numString);              
}
catch(FormatException ex)
{
    Console.WriteLine(ex.Message);                
}
```

Another possible solution is using **`TryParse()`**, which we'll discuss below.

## How to Convert a String to an Int Using `Convert.ToInt32()`

`Convert.ToInt32()` is a static method provided by C# to convert a string to a 32-bit signed integer. This method takes a string variable as input and returns an integer. Here is an example:

```cs
string numString = "123";
int num = Convert.ToInt32(numString);
```

In the code block above, we have declared a string variable, **`numString`**, and assigned it a value. We then use the **`Convert.ToInt32()`** method to convert this string to an integer and assign it to a variable named **`num`**. 

The `Convert.ToInt32()` method has two exceptions, **`FormatException`** and **`OverflowException`** and is able to convert a null variable to 0 without throwing an exception.

## How to Convert a String to an Int Using `Int32.TryParse()`

Compared to the **`int.Parse()`** method, **`int.TryParse()`** is a safer way to convert a string to a 32-bit signed integer. 

This method takes in a string variable and an **`out`** parameter and returns a **`bool`** of value `true` if the parsing is successful. The result of the parsing is stored in an **`out`** parameter. 

This is the safest way of converting a string variable to an Integer. Here is an example:

```cs
string numString = "12";

if (int.TryParse(numString, out int num))
{
	// Conversion successful, do something with num.
    Console.WriteLine("Successful");
    Console.WriteLine(num);
}
else
{
	// Conversion failed, handle the error.
    Console.WriteLine("Unsuccessful..");
}
```

In the above code, we tried to parse a string variable called **`numString`** to an integer using the **`int.TryParse()`** method. The result is stored in the **`num`** variable if the conversion is successful. If the conversion fails, the success variable is set to false and the num variable is assigned its default value.

## Conclusion

Converting a string to a number is a common task in programming, and C# provides various ways to accomplish this task. 

In this article, we saw some of the methods to convert a string to an integer in C# using the `Parse()`, `TryParse()`, and `Convert()` methods. I hope this article helped you learn more about converting strings to ints in C#.  
  
Happy coding!  

