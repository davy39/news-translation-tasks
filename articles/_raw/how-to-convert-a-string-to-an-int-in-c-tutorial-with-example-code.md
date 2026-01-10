---
title: How to Convert a String to an Int in C# – Tutorial with Example Code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-03-29T20:03:18.000Z'
originalURL: https://freecodecamp.org/news/how-to-convert-a-string-to-an-int-in-c-tutorial-with-example-code
coverImage: https://www.freecodecamp.org/news/content/images/2021/03/youtube-cover.jpg
tags:
- name: C
  slug: c
- name: Tutorial
  slug: tutorial
seo_title: null
seo_desc: 'By Ondrej Polesny

  Converting a string to an integer is common practice when you''re dealing with user
  input, JSON data, API responses, or regular expressions. But what''s the right way
  to do it for each scenario?

  In this article, I''ll explain three way...'
---

By Ondrej Polesny

Converting a string to an integer is common practice when you're dealing with user input, JSON data, API responses, or regular expressions. But what's the right way to do it for each scenario?

In this article, I'll explain three ways to convert a string into a number in C# and I'll show you how to choose the right method for your scenario.

## Determine the source of your data

First of all, let's see where your data is coming from. It's easy to convert the string "123" into an integer, but in the real world, it's never that simple. 

The "number string" can come from a database, text file, an API, or a user of your app. So how confident are you it's really a number?

| Data source | Confidence | What can happen |
| ------------- |:-------------:| ----- |
| User input | 🙁 | "1.23"<br/>"hello" |
| JSON data | 😐 | "123.1"<br/>"" |
| API response | 😐 | "11,7"<br/>"" |
| Regular expression match | 🙂 | invalid expression allowing not only numbers |

## How big can your number get?

You also need to know how big your target number can be. In the scope of this article, we're talking about Int. That is usually considered `Int32` (`int`), but you can also use `Int16` (`short`) and `Int64` (`long`) depending on how large the numbers are that you expect.

| Type | Largest number |
| ------------- | ------------- |
| `Int16` (`short`) | 32767 (`Int16.MaxValue`) |
| `Int32` (`int`) | 2,147,483,647 (`Int32.MaxValue`) |
| `Int64` (`long`) | 9,223,372,036,854,775,807 (`Int64.MaxValue`) |

## int.Parse(String) – input confidence: high 🙂

Use `int.Parse` when you are sure the input is really a number. It can also parse numbers in culture-specific or other widely-known formats, but you need to know the exact format:

| Signature | Output |
| ---- | ---- |
| `int.Parse("123")` | 123 |
| `int.Parse("")` | throws `FormatException` |
| `int.Parse(null)` | throws `ArgumentNullException` |
| `int.Parse("123,000")` | throws `FormatException` |
| `int.Parse("123,000",`<br/>`  System.Globalization.NumberStyles.AllowThousands,`<br/>`  new System.Globalization.CultureInfo("en-US"))` | 123000 |

## Convert.ToInt32(String) – input confidence: medium 😑

`Convert` is very similar to `int.Parse` with one exception: `null` is converted to 0 and does not throw an exception. It can also handle other input data types (not just strings):

| Signature | Output |
| ---- | ---- |
| `Convert.ToInt32("123")` | 123 |
| `Convert.ToInt32("")` | throws `FormatException` |
| `Convert.ToInt32(null)` | 0 |
| `Convert.ToInt32("123,000")` | throws `FormatException` |
| `Convert.ToInt32("1.23")` | throws `FormatException` |
| `Convert.ToInt32(1.23)` | 1 |

_Note: You can use_ `_Convert.ToInt32_` _to remove number precision behind a decimal point. However, to ensure good code readability, you should use_ `_Math.Floor_` _to achieve this task._

## Int*.TryParse(String, Int32) - input confidence: low 🙁

Use `TryParse` whenever you don't trust your data source. For example, when you're getting user input or parsing and validating data from submitted forms:

| Signature | Output |
| ---- | ---- |
| `int number;`<br/>`bool convertible = Int32.TryParse("123", out number)` | number = 123<br/>convertible = True |
| `int number;`<br/>`bool convertible = Int32.TryParse("hello", out number)` | number = 0<br/>convertible = False |
| `int number;`<br/>`bool convertible = Int32.TryParse("", out number)` | number = 0<br/>convertible = False |

_Note: You can also move the number definition to the `TryParse` method call by typing `out int number`._

The most typical example is with `Console.ReadLine`:

```csharp
while (!Int32.TryParse(Console.ReadLine(), out int number))
{
	Console.WriteLine("Please input number");
}
Console.WriteLine(number);
```

## Conclusion

In this article, I showed you three ways to convert a number to a string in C# and explained how to decide which method to use based on the source of your data and the confidence you have in it.

If you don't want to miss my new articles, follow me on [Twitter](https://twitter.com/ondrabus).

