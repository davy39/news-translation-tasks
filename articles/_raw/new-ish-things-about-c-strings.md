---
title: Strings in C# – What's New, Explained with Code Examples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-05-26T13:49:06.000Z'
originalURL: https://freecodecamp.org/news/new-ish-things-about-c-strings
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/things-about-strings.png
tags:
- name: C
  slug: c
seo_title: null
seo_desc: 'By Deborah Kurata

  Much of what we work with in our code are strings. Let''s look at some of the newish
  things about C# strings ... including raw string literals and raw string interpolation
  that are new in C# 11.

  Raw string literals make it easy to bu...'
---

By Deborah Kurata

Much of what we work with in our code are strings. Let's look at some of the newish things about C# strings ... including raw string literals and raw string interpolation that are new in C# 11.

Raw string literals make it easy to build complex, multi-line strings, including JSON, in a simple and flexible way. And with no escaping necessary.

Watch the associated video here:

%[https://youtu.be/A5FRgglBkJ8]

Find the [sample code here](https://github.com/DeborahK/CSharp-Examples). 

In this article, we'll start with some of the current techniques we use to handle strings, problems we've faced using those techniques, and new C# 11 features that help with our string handling.

## **Quoted String Literal**

The primary way we've worked with strings in C# is using a quoted string literal. These have been available since the beginning of C#.

```csharp
string header = "<div class=\"card-header\">Vehicle Detail</div>"
```

But if we have quotes in our string, the string gets a bit messy. We escape those quotes with a backslash. That way the C# compiler can tell the difference between the outside quotes and any quotes within the string.

Standard quoted string literals are often best for single line strings with no characters that need to be escaped.

## **Verbatim String Literal**

For strings that span across multiple lines, we use a verbatim string literal. We define a verbatim string literal with an at sign in front of the first quotation mark. Verbatim means "as is", and is meant to define a multi-line string that displays "as is".

```csharp
string header = @"
   <div class=""card"">
     <div class=""card-header"">
       Vehicle Detail
   </div>
";
```

But once again, quotation marks are a challenge! Verbatim string literals require that we use double quotation marks to indicate a quotation mark within a string. This doesn't look horrible in this case ... but when creating a string with lots of quotation marks, like defining JSON, it can be quite messy.

Plus, indentation of verbatim string literals can be a problem.

```csharp
  foreach (var vehicle in vehicles)
  {
    if (goodCredit)
    {
      if (newVehicle)
      {
        message = @"
          Congratulations on your new vehicle!
          We hope you enjoy driving it as much as we enjoyed building it.
          ";
      }
     }
   }
```

Above we have a typical bit of code with multiple indentations. And we indent the message nicely within the if block. But then if we display the message, the indentations are included as shown in Figure 1. That may not be the desired result.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/verbatim-string.png)
_Figure 1. Verbatim string literal retains its indentation_

To fix it, we'd have to unindent the text to line up with the left margin.

```csharp
  foreach (var vehicle in vehicles)
  {
    if (goodCredit)
    {
      if (newVehicle)
      {
        message = @"
Congratulations on your new vehicle!
We hope you enjoy driving it as much as we enjoyed building it.
";
      }
    }
   }
```

The result is then better as shown in Figure 2. But the code looks a bit messy. And if some unsuspecting developer comes along to "clean up" the indentation, our result is not as we intended.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/indentation-not-saved.png)
_Figure 2. Verbatim string literal must be outdented in the code to appear with no indentation_

## **Raw String Literal (new in C#11)**

A new feature in C# 11, released in 2022, is a **raw string literal**. A raw string literal is a new format for string literals. They allow for whitespace, new lines, embedded quotes, other special characters, or whatever!

A raw string literal begins with at least 3 quotes. And ends with a matching set of quotes. Everything on the lines between the opening and closing quotes is the desired string.

```csharp
 string header = """
      <div class="card">
        <div class="card-header">
          Vehicle Detail
        </div>
      </div>
    """;
```

Notice that there is no need for doubling of the quotes or any escape characters. The string displays exactly as it is. This is a much better choice for multi-line strings over the original verbatim string literal.

Another important feature of raw string literals is that the resulting string aligns to the closing quotes. In the example below, we align the message with the beginning of the closing quote.

```csharp
  foreach (var vehicle in vehicles)
  {
    if (goodCredit)
    {
      if (newVehicle)
      {
        message = """
          Congratulations on your new vehicle!
          We hope you enjoy driving it as much as we enjoyed building it.
          """;
      }
     }
   }
```

When we display this string, it's aligned appropriately to the left margin as shown in Figure 3.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/indented-based-on-closing-quote.png)
_Figure 3. Raw string literal is indented based on the closing quote_

Recall that I said that raw string literals start with **at least** three quotes. The C# team wanted the feature to have a long life, so they made it configurable. If for some reason you need triple quotes within the string, you could use quad quotes to enclose the raw string literal. Just be sure that the string ends with the same number of quotes.

A single line raw string literal requires that the opening and closing quotes are on the same line. Here is a single line raw string literal. Notice the three quotation marks at the beginning and ending. Then the embedded quotes don't require any special characters.

```csharp
string text = """He said, "None shall Pass"."""
```

A multiple line raw string literal requires that the opening quotes are on the line above the raw string and the closing quotes are on their own line below the raw string. Here is a JSON string defined using a raw string literal. Notice that we can use normal quotation marks around the field names and string values. So our JSON looks like JSON.

```csharp
  string vehicleJSON = """
    {
      "id": 1,
      "name": "AT-AT",
      "price": 19416.13
    }
    """;
```

Since the indenting of the raw string literal is defined by the start of the closing quotes, the text must **not** be outdented from that closing set of quotes.

The example below has the ending curly brace to the left of the closing quotes. So this code generates a syntax error as shown in Figure 4.

```csharp
  string vehicleJSON = """
    {
      "id": 1,
      "name": "AT-AT",
      "price": 19416.13
  }
    """;
```

![Image](https://www.freecodecamp.org/news/content/images/2024/04/error-message.png)
_Figure 4. Error message when raw string literal is outdented beyond the closing quotes_

Use raw string literals instead of verbatim strings when working with multiple lines or strings with quotes or other special characters that require escape sequences.

With the power, flexibility, and clarity of the raw string literals, you may never use a verbatim string literal again!

## **String Interpolation**

We often want to include the value of a variable or expression within a string. That's the purpose of interpolation. String interpolation allows us to insert an expression into a string literal.

```csharp
string pageTitle = "Vehicle Detail";
string header = $"Header: {pageTitle}";
```

We identify an interpolated string with a dollar sign in front of the first quote. We add one or more expressions into the string using curly braces. The curly braces act as a placeholder. 

At runtime, the expression is evaluated and the appropriate value appears in the string in place of the curly braces and expression. This way we can embed the value of a variable or expression in a string literal.

Here are some examples. We can include a calculation or call a method. Any valid C# expression can be inserted within the curly braces.

```csharp
string answer = $"Answer: { 20 * 2 + 2 }";

string pageTitle = "Vehicle Detail";
string header = $"Header: {PrepareTitle(pageTitle)}";
```

### Constant String Interpolation (New in C# 10)

As of C# 10, we can define an interpolated string as a constant ... but only if the interpolated expression is a constant, like in this example.

```csharp
const string pageTitle = "Vehicle Detail";
const string header = $"Header: {pageTitle}";
```

Since the interpolated expression is a constant in this example, the interpolated string can be defined as a constant. This may not be a very common requirement, but it's nice to know the feature is available if you should need it.

## Newlines in Interpolation Expressions (New in C# 11)

New in C# 11, we can use multiline interpolated expressions. This can make code within the curly braces a bit easier to read. 

In this example, we're using the ternary conditional operator. If the page title variable is empty, we set "no title", otherwise we set the page title. Notice that we must enclose the ternary conditional operator in parentheses within the curly braces.

```csharp
    string pageTitle = "";

    string header = $"Header: {
      (pageTitle == ""
        ? "No title"
        : pageTitle)
    }";
```

Putting too much code inside of an interpolation expression makes that code hard to debug and test. So be careful how much code you write within the interpolated expression. In some cases, it may be better to put the code in a function and call that function from the interpolated expression

## **Verbatim String Interpolation**

We can combine string interpolation with verbatim strings using `@$` or `$@`. That way we can have multiple lines of text and optionally, multiple lines for our interpolation expression.

```csharp
    string pageTitle = "Vehicle Detail";
    string header = @$"
      <div class=""card"">
        <div class=""card-header"">
          {(pageTitle == ""
           ? "No title"
           : pageTitle)}
        </div>
      </div>
    ";
```

But since it is a verbatim string, we again need double quotes for any embedded quotes.

## **Raw String Interpolation (New in C# 11)**

A better option for string interpolation is raw string interpolation, available in C# 11. Here we add the dollar sign in front of our three sets of quotation marks. Then we can define multiple lines of text and multiple lines for our interpolation expression.

```csharp
 string pageTitle = "Vehicle Detail";
  string header = $"""
      <div class="card">
        <div class="card-header">
          {(pageTitle == ""
           ? "No title"
           : pageTitle)}
        </div>
      </div>
    """;
```

Let's look at another example, creating a JSON string. This is the string we want to create. But we want to use interpolation for the price instead of hardcoding it.

```csharp
   {
      "id": 1,
      "name": "AT-AT",
      "price": 19416.13
    }
```

Notice that JSON syntax requires curly braces around the object. But if we want to use an interpolated string, the interpolation needs curly braces. So are we going to need to escape those curly braces? Nope!

The C# team wanted a string interpolation solution that was configurable. So for raw string interpolation, we can optionally use **two** dollar signs. The **two** dollar signs means that we need **two** sets of curly braces for the interpolation. That way the single set of curly braces can be interpreted as part of the string literal.

```csharp
    decimal price = 19416.13M;
    string vehicleJSON = $$"""
      {
        "id": 1,
        "name": "AT-AT",
        "price": {{price}}
      }
      """;
```

Or we could use three dollar signs with three sets of curly braces, and so on. The number of dollar signs indicates the number of pairs of curly braces required for interpolation.

Very cool!

## **Wrapping Up**

This tutorial walked through options for defining string literals and for string interpolation.

The new raw string literal and raw string interpolation simplify string management, offering a flexible solution for working with strings.

Check out the video here:

%[https://youtu.be/A5FRgglBkJ8]

Or try out the [sample code here](https://github.com/DeborahK/CSharp-Examples). 

