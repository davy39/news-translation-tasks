---
title: Microsoft Excel Tutorial – How to Create Formulas and Functions
subtitle: ''
author: Benny Ifeanyi Iheagwara
co_authors: []
series: null
date: '2022-09-08T15:17:10.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-microsoft-excel-formulas-and-functions
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/Green-Orange-and-Brown-Collage-Math-Quiz-Presentation.png
tags:
- name: excel
  slug: excel
- name: spreadsheets
  slug: spreadsheets
seo_title: null
seo_desc: "Spreadsheets aren't merely for arranging data into rows and columns. Most\
  \ of the time, you use them for data analysis as well. \nMicrosoft Excel is one\
  \ of the most widely used spreadsheet applications, especially in finance and accounting.\
  \ This is par..."
---

Spreadsheets aren't merely for arranging data into rows and columns. Most of the time, you use them for data analysis as well. 

Microsoft Excel is one of the most widely used spreadsheet applications, especially in finance and accounting. This is partly because of its easy UI and unmatched depth of functions.

In this article, you will learn:

* What Excel formulas are
* How to write a formula in Excel
* What Excel functions are
* How to work with an Excel function
* Lastly, we'll take a look at dynamic Excel functions.

# What do I need to install on my computer to follow this article?

To follow along, you will need to have Microsoft Excel installed on your computer. We’ll use a Windows computer for this article.

# How can I install Microsoft Excel on my computer?

Follow these steps to install Microsoft Excel on your Windows computer:

1. Sign in to [www.office.com](https://www.office.com/) if you’re not already signed in.
2. Sign in with the account associated with your [Microsoft 365](https://www.microsoft.com/en/microsoft-365?ocid=oo_support_mix_marvel_ups_support_railbanner_1000852&rtc=1) subscription. You can also try out [Office for free](https://signup.live.com/signup?mkt=en-US&uiflavor=web&lw=1&fl=easi2&client_id=4345a7b9-9a63-4910-a426-35363201d503&wreply=https%3A%2F%2Fwww.office.com%2F%3Fauth%3D1%26from%3DOdotComFreeSignup) as well.
3. Once signed in, select “Install Office” from the Office home page. This will automatically download Microsoft Office onto your Windows computer.
4. Run the installer to set up Microsoft Office and select "Close" once you're done.
5. Once done, select the “Start” button (located at the lower-left corner of your screen) and type “Microsoft Excel.”
6. Click on Microsoft Excel to open it.
7. Accept the license agreement, and let's get started.

# What are Excel Formulas?

An Excel formula is an expression that carries out an operation based on the value of a cell or range of cells. You can use an Excel formula to:

* Perform simple mathematical operations such as addition or subtraction.
* Perform a simple operation like joining categorical data.

It's important to understand two things: Excel formulas always begin with the equals "=" sign and they can return an error if not properly executed.

# What Operators Are Used in Excel Formulas?

There are four different types of operators in Excel—arithmetic, comparison, text concatenation, and reference. But for most formulas, you’ll typically use these three:

### Arithmetic operators

<table style="border:none;border-collapse:collapse;table-layout:fixed;width:468pt"><colgroup><col><col></colgroup><tbody><tr style="height:0pt"><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">+</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Addition</span></p></td></tr><tr style="height:0pt"><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">-</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Subtraction</span></p></td></tr><tr style="height:0pt"><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">/</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Division</span></p></td></tr><tr style="height:0pt"><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">*</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Multiplication</span></p></td></tr><tr style="height:0pt"><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">^</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Exponentiation</span></p></td></tr></tbody></table>

### Comparison operators

<table style="border:none;border-collapse:collapse;table-layout:fixed;width:468pt"><colgroup><col><col></colgroup><tbody><tr style="height:0pt"><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">=</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Equal to</span></p></td></tr><tr style="height:0pt"><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">&gt;</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Greater than</span></p></td></tr><tr style="height:0pt"><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">&lt;</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Less than</span></p></td></tr><tr style="height:0pt"><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">&gt;=</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Greater than or equal to</span></p></td></tr><tr style="height:0pt"><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">&lt;=</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Less than or equal to</span></p></td></tr><tr style="height:0pt"><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">&lt;&gt;</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Not equal to</span></p></td></tr></tbody></table>

### Text concatenation

Here you have just the ampersand “&” sign for joining text.

# How Can I Create an Excel Formula?

Let's take a simple scenario using one of the arithmetic operators.

In math, to add up two numbers, let's say 20 and 30, you will calculate this by writing: 20 + 30 = 

And this will give you 50.

In Excel, here is how it goes:

1. First, open a blank Excel worksheet.
2. In cell A1, type 20.
3. In cell A2, type 30.
4. To add it up, type in = 20 + 30 in cell A3.

![Image](https://lh5.googleusercontent.com/ahFv4-tCq-5p6B9wWJwrfv-0glehpnu9gMnAw34pwCUh9hUVyw3p5aOu5ejIAnCPBDtw6g_CTOOWaEtap1ph2XP5nL9TkxVb2E5iV80tp6Tm73968jE3kyCPKaMkrVYpw1Mn4rYBxXMSrU5CzEkSlxNhBp-KiZLfEtDAOagAzGHa6RWO5yLaZsyevQ)
_How can I create an Excel formula?_

5.  Then, press ENTER on your keyboard. Excel will instantly calculate this and return 50.

![Image](https://lh6.googleusercontent.com/XGXatK9hD_imhCrF3wQ-NuzlOzCgW0TCysQ0vwtk-Xz8Wu-W5ZxIKf65DBbc0i5H2_ubVC4rBoiyVauMcOWdapOwqGwhANyNKhwS_us0CTFMBP76q2wP3HGksmsWvb8ebB6cLG_3RzWSp2vie7woGbTZTuMmaPsnwa5oFoP8gFNf6RwbJa4O-hnVzQ)
_How can I create an Excel formula? Adding numbers in Excel_

I mentioned earlier that every formula begins with the equal "=" sign. That's what I meant. To write a formula, you type the equal to sign followed by the numeric values. This also applies to cases of subtraction, division, multiplication, and exponentiation. 

Let's take another simple scenario using one of the comparison operators. Assume we want to find out if 30 is greater than 40.

In Excel, here is how we would do it:

1. Type in =30>40
2. Press ENTER.

![Image](https://lh6.googleusercontent.com/j7NqF7FlQbtnSWU_QiE2pHtmsadofCUgJHkXKTEEp2miFXV24QjJMMyZrP-sVibNuM__jgW1szMEQjuFtz4gb9ZbOm6n5UtWtGNktWd3iOEcnbTFH4_4GftYs_FLySTkeWhA51MujOKvZGAkdYN96hzyGb86Na_dKhawPQFXRNtP7jI87Azo1FZ1qA)
_How can I create an Excel formula? Comparison operators_

  
3.  This will return a FALSE because 30 isn't greater than 40. Excel uses TRUE and FALSE for logical statements, the same way we human says yes and no.

![Image](https://lh5.googleusercontent.com/rmJNrTzMCS3Qg0nIk-1DqURQuqfO2qF-0eqiF4RyAsM9lPDGtVyDpzsJryzN-7BXrv3qGbIhRjw2NGNKHiMVaHlWwnqVWigvlu35dqTUgHaxGshud8n3bdsnwrJ9cXPMLASLQDMKoAJqRjivuqgA_WQpYZaUMDq4T41LMJzgivLeqd5LN2_zrsmTrA)
_How can I create an Excel formula? Comparison operators_

Lastly, let's take another simple scenario using the text concatenation operator – the ampersand “&” sign. This works with your string data types and you use it to join text.

Assume we have "Welcome", "To", and "FreeCodeCamp" all in different cells—A1, A2, and A3—of your worksheet. We would type =A1&” “&A2&” “&A3 to join them.

The space in quotes “ “ represents that we want a space between our words.

![Image](https://lh6.googleusercontent.com/_NuH8HoSTLRA4zTSGaCkcCwLKhjZVYy885wThXg_NgwYsyIDEk_6APoloy2wujJUNZUkXsBTFDr-dmO_x3B_4WU0XQUaBJGiNz6gTlPC3lqR2U5utRsK9S3R9yxoRi4U9N1zvH92LMW-F97cn5hx1_k09du0tYxFERxtg5w5Zl8M4Bw_HSyF8maq6w)
_How can I create an Excel formula using the ampersand “&amp;” sign_

Another tip: the formula bar shows the formula used to generate a value.

# What Are Excel Functions?

Excel functions are predefined inbuilt formulas that perform mathematical, statistical, and logical calculations and operations using your values and arguments.

For Excel functions, you should know that:

* They’re formulas, so yeah, they start with the equal "=" sign as well.
* The order is very important.

There are over 500 functions available. You can find all available Excel functions on the Formulas tab on the Ribbon.

![Image](https://lh5.googleusercontent.com/GL6J_F_ao0U-lmLQs8CCZHrjxGZz5l_zF9b7EAn6lirKVRx9YZ86PCw6UTrCFBFhPDaiEUBSpLA8fOZcj43CW7oDWYlcxjEHXMXe5cSphegI2HpdfjrJxoXaWcP8wCEK9gAV30rqE89Gd08y1pj5vI5JGSCfDgdUg8lxu2MT9S-KgnFahn5o-H2x7A)
_All available Excel formulas and functions_

But why use a function when you can just write a formula?

Here are some benefits of Excel functions.

* To improve productivity and effectiveness.
* To simplify complex calculations.
* To automate your work.
* To quickly visualize data.

## What Makes Up Excel Functions?

Unlike formulas, Excel functions are made up of a structure with arguments you need to pass.

Every function:

* Starts with the equals "=" sign
* Has a name. Some examples are VLOOKUP, SUM, UNIQUE, and XLOOKUP.
* Requires arguments which are separated by commas. You should know that semicolons are used as separators in countries like Spain, France, Italy, Netherlands, and Germany. You can, however, change this via the Excel setting.
* Argument with the square brackets [] are optional
* Has an opening and closing parenthesis.
* Has an argument tooltip which shows you what you should pass.

There are some exceptions. For example,

* The DATEDIF doesn't show in Excel because it is not a standard function and gives incorrect results in a few circumstances. However, here is the syntax: 

`DATEDIF(birthdate, TODAY(), "y")`

* Functions like PI(), RAND(), NOW(), TODAY() require no argument.

# How to Use Excel Functions

Let's look at a few functions:

### How to Use the `SUM()` Function in Excel

According to the documentation, the SUM function adds values. Here is the syntax:

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-315.png)
_Excel Sum Syntax_

Let's assume that we have a line of numbers from 1 to 10 and we want to add it up. To achieve this, we will just type =SUM(A1:A10). The A1:A10 simply returns an array of number that are situated on cell A1 to A10 which are A1, A2, and A3 up through A10.

![Image](https://lh3.googleusercontent.com/oj-2CwOiYRuzMhsH6oyy8zMFUCw9EpTPQWtLhkUbsbigzk-U6RG_dDG_aVeazYkgIQmuil80wG0N6_t3yk9oqF3EKjdSoREj8c-PqACBgOkZX763fMyM4oLKnGVharikQAFt0SNEvkxO1bnN67LQs3LLfQ-LW2R37IFVJGXz7KvJ1Wu_S7imz-0YsA)
_How to use Sum in Excel_

Since the second argument is optional, that means a sum(A10) will return a value. In our case, it will return just 10 since A10 has the value 10 in it. Give it a try.

If you were writing this using the addition operator, you would have written:

=1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 

or 

=A1 + A2 + A3 + A4 + A5 + A6 + A7 + A8 + A9 + A10 

This doesn't look very productive or efficient.

### How to Use the `TODAY()` Function in Excel

According to the documentation, the TODAY function displays the current date on your worksheet. It also requires no argument. Here is the syntax:

![Image](https://lh3.googleusercontent.com/o0zz_IZW5soeg7kcBLmaruiuCHlVhyR4C3_-D0lDhtXV0xDZU4JnapR9q_QbyXOdsSN_n8Ko0owSMITVXWbOjZml2GATMUBx4h9QcNpQsbz6B1BsDbxvoK2N-cuyw5I7OcwyyAJI8BbnPXiU2pVAYmQ26SnXHrWQt2DFsiWi5l6oo_U4dEo6cruImA)
_How to use Today() in Excel_

Excel displays the current date automatically according to your computer's date and time setting. The same goes for the NOW() function, which displays the current date and time.

### How to Use the `CONCATENATE()` Function in Excel

Let’s look at a text function. You use CONCATENATE to join two or more text strings into one string together.

Here is the syntax:

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-316.png)
_Excel CONCATENATE() Syntax_

Let's assume we want to join “This is” with “freeCodeCamp” – but in your cell, you have just "freeCodeCamp."

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-320.png)
_freeCodeCamp Excel_

If you’re going to write a string inside a formula, you must write it inside quotes like this “ “. 

Why?

This way, Excel wouldnt think you're trying to write another function.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-319.png)
_How to use Excel CONCATENATE function_

This will return the phrase “This is freeCodeCamp”

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-321.png)
_How to use CONCATENATE() in Excel_

### How to Use the `VLOOKUP()` Function in Excel

This is one of Excel’s most interesting and commonly used formulas or functions. You use it to find a value in a table or range by row.

Here is a scenario:

We have a simple table that shows various films along with their genre, lead studio, audience score %, profitability, rotten tomatoes %, worldwide gross and year. I would use just the first 10 rows of the sample data from this [GitHub Gist](https://gist.github.com/tiangechen/b68782efa49a16edaf07dc2cdaa855ea).

![Image](https://lh5.googleusercontent.com/T12acvhR4WeGpmxjG8Ye9-nif_k8r-trYb3Zacz9PZjxRDZJOQd1weeIx06Soa-QRsriVCuaGrJ2B_-6klJcxyuRKh7cmoIPre-cbHecnxvooo6AEYd5pgc_Dz2keINjCm-yF3Vw1HtcQTfzMK938gUK5Ybks72moTZEGuPmnHVHS2-yHv38hRvArg)
_Flim dataset_

I want that, whenever I type in a movie in the yellow cell, the year should get displayed in the green cell. Let's use VLOOKUP to find it.

This is the VLOOKUP syntax:

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-317.png)
_Excel Vlookup Syntax_

Besides writing your formulas in the cell, you can also write them using the Excel Insert Function (fx) button, which is close to the formula bar.

Let's try this.

1. Write `=Vlookup(` on the green cell.
2. Click on fx. A dialogue box will pop up showing all the arguments this formula needs.
3. Input the value for each argument.
4. Lookup_value (required argument): This is what you want to find. In our case, that is the movie “Youth in Revolt” which is in cell B1.
5. Table_array (required argument): This is just asking you for the table that contains the data. You give it the entire table, which in our case is A4:H13
6. Col_index_num (required argument): This is asking you for the column number of the table you gave. In our case, we want the year. This is in column 8.
7. Range_lookup (optional argument): Lastly, we pick if we want an approximate match (TRUE) or an exact match (FALSE). 

	- TRUE means approximate match, so it returns the closest or an estimate.

	-  FALSE means exact match, so it returns an error if it's not found.

8. We would go for the FALSE because we want the exact match.

![Image](https://lh6.googleusercontent.com/T-VtgAKve9lXEP8VA5FATji23YJveuZJfqWEnde330eLDw0gJj2hn1Qol5R1fVqs9aFYPoxFZ9Y5XLwth6MHWgYH55i0Llz-gS8m2_r7aEViaDD_3_Gpow5rWATdGtCBVlPTolM-9zZ2hono6lsBiN-l_DM7pVjLzk7oOZ-GYO8unxTQF7unpzA5MA)
_How to use VLOOKUP() in Excel_

9. Click on "OK." Excel will return 2010. 

However, you can write this in the cell by typing in `=VLOOKUP(B1,A4:H13,8,FALSE)` in your cell.

![Image](https://lh3.googleusercontent.com/fhQrWy2DvFXRtscCz_H-DbZE73claukadh-KwtU5XGuxmZWDwtDlo60aM7cqBS3iPpayxfB3DH6NeFFH2j19l2M3QXM7RCUlYrGHRUlxcFAmEUylwj4g1b8k00lYx_8FWrEQl4cJyxmhoUPLlxJuALoUtO5F06SQl1_0nWusaza0nWFwZmO4T-3qGA)
_How to use VLOOKUP() in Excel_

# Tips and Rules When Writing Excel Functions

When writing our function, Excel provides some formula tips.

1. The Argument tooltip doesn't leave until you close the last parenthesis.
2. The formula bar shows your formula.
3. The argument you are currently writing is always dark. Take a look at the lookup_value in the image below.
4. The square brackets [] tell you it is optional.
5. Lastly, the colour code – our B1 is in blue, and cell B1 is in blue to guide us on what cell or table was picked. The same thing will happen to A4:H13 when we pick it as our table_array argument.  


![Image](https://lh4.googleusercontent.com/DVOp6zoa3z8cC01iE0iW01CcMv3ceE3WId7qu-2peocY8HkJf3ltmXHfAgHjj9Sj-7w-NS0DugruBR8FTCTRW77AFLRmdwM_UY83pXcFv3M6FHZBHFpWXy6B02ocko1NtC15GpHenEzBjU2w13i5SorlHU_6FdfA12iycyevjQhgnu6Mr78_CwkRSw)
_Vlookup and Excel formula bar_

# How to Work with Nested Functions in Excel

A nested function is when you write a function within another function. For example, finding the average of the sum of values.

The first tip when writing a nested function will be to treat every function individually. So address the first function before addressing the second. A pro tip would be to look at the argument tooltip when writing it.

Let's take a simple scenario.

We have two arrays of numbers. Each has the scores of students in the class. I want to add the two arrays before I get the average. 

Let's get started.

1. Type in your = followed by the average.
2. The number one will be the sum of the scores from class one.
3. The number two will be the sum of the scores from class two. 

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-318.png)
_Nested Function: Excel AVERAGE and SUM syntax_

![Image](https://lh3.googleusercontent.com/SBV3QpbGiSsXkDoXBpRaRfbjVUjJckLV0crBJ2u5iptUb0C10poCJZIZltv0b13tTTXpABVQ9CvHoAC2S5gwCNMxhaTFX3Y1oyRgNehxFEHPRf_Sm9--HQmVh8ZsVWKsWs2EfQBAEdv6sSTqTP2tmr0JXPb44UmLOO82OzM3oERfntfhPyHQaf1b_w)
_Excel AVERAGE syntax_

Finally, don't forget the closing parenthesis. 

Thus, the formula will be `=AVERAGE(SUM(B3:B8),SUM(D3:D8))`.

# How to Work with Dynamic Array Functions in Excel

Dynamic array functions are formulas associated with spill array behaviour. 

Before now, you wrote a function and it returned just a single input. We call these kinds of functions legacy array formulas. 

Dynamic array functions, on the other hand, will return values that will enter the neighbouring cells. A few examples of dynamic array functions are:

* UNIQUE
* TEXTSPLIT
* FILTER
* SEQUENCE
* SORT
* SORTBY
* RANDARRAY

Let's look at the UNIQUE formula.

### How to Use the UNIQUE() Formula in Excel

The unique formula works by returning the unique value from an array or list. Let's use the movie sample data from this [GitHub Gist](https://gist.github.com/tiangechen/b68782efa49a16edaf07dc2cdaa855ea). This table contains 77 rows of film excluding the heading.

![Image](https://lh5.googleusercontent.com/cgULd4fUAfw1b4J5Q2utiNG_bPSaicGK6vEtuNKS6zCL2IFgoq8ivfZL_UMTTUcRUNc-nVDRxx8O6gQUCba1Eoko6U588n18CsiuBigsVS83V8W8bLZjtltBOqIkWUJRDhhamJzGzqz3FWn_sgVAB3oLJx5L7JOEike_iawhMd7fQHinqfSb_MoaxA)
_Flim data GitHub_

Let's try to get the unique years from our dataset – that is, years without duplicates. 

To do this:

1. Type `=UNIQUE(`
2. Select the entire array of values from the year column: =UNIQUE(H2:H78)

![Image](https://lh6.googleusercontent.com/mdX9zeClRBtGuzdHukis2gU-2RcH1K2rJvLrUHbSXN2ECokzYTn6SWSLuE2UOACXx3J2DrJQTauzLIb2u5Eqgq1LGvUJXVhpYAZD29CKZnWMBaId2O_6AFHtPJLFbz1FsG7dSIq8zMeRivRwG-qdpw74JG_Qglu4yrlgWIH-8ycQRMQ4cqp1ZNbSgQ)
_How to use Excel UNIQUE formula_

3. Close the parenthesis and press Enter.

Though the formula was written in a single cell, the returned value got spilled into the cells below it. That's the spilled array behaviour.

![Image](https://lh4.googleusercontent.com/BM4eUSa5hvjSJF4Md2eizx-N97bc2dOdV0LwGYKLErjP4acTf0oCYnjYLhuxs3JHcF7YHyONMWTbXH24Epmc0AT6kvmyL_cg6d0shcKjEmvVL9wN_YQXMpTIGKoh-1dgmfyqUg102K67JsjUGycCMogiCzsIK7E53e7rZ5qd_buCQfylmIH4jHPtaQ)
_Excel dynamic array formula_

# How to Create Your Own Functions in Excel

Microsoft Excel released a bunch of new functions to make user more productive. One of these function was the LAMBDA function.

The LAMBDA function lets you create custom functions without macros, VBA or JavaScript, and reuse them throughout a workbook. 

The best part? you can name it.

### How to Use the `LAMBDA()` Function in Excel

This LAMBDA function will increase productivity by eliminating the need to copy and paste this formula, which can be error-prone.

Here is the LAMBDA syntax:

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-322.png)
_Excel LAMBDA function_

Lets start with a simple use case using the movie sample data from this [GitHub Gist](https://gist.github.com/tiangechen/b68782efa49a16edaf07dc2cdaa855ea). 

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-323.png)
_The Movie dataset_

We had a column called "Worldwide Gross", lets try to find the Naira value.

1. Create a new column and call it "Worldwide Gross in Naira".
2. Right below our column name, Cell I2, type `=lAMBDA(`
3. LAMBDA requires a parameter and/or a calculation. 

The parameter means the value you want to pass, in our use case we want to change the gross value. Lets call it gross.

The calculation means the formula or function you want to execute. For us, that will be to multiply it with te exchange rate. At the moment, that's 670. so lets write gross * 670. 

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-328.png)
_How to use LAMBDA function in Excel_

4. Press Enter. This will return an error because, gross doesnt exist and you need to let excel know of these names.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-329.png)
_Using Excel LAMBDA_

5. To make use of the newly created function, you need to copy the syntax written.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-330.png)
_Writing function with Excel LAMBDA_

6. Go to the formula ribbon and open the name manager. 

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-332.png)
_Excel name manger using the LAMBDA function_

7. Define the name manger parameters:

* The name is simply what you want to call this function. I am going with NairaConvert.
* The scope should be workbook because you want to use this function in the workbook.
* The comments explains what your function does. It is acts as a documentation.
* In the **refer to**, you should paste the copied function syntax.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-333.png)
_Excel name manager_

8. Press Ok.

9. To use this new function, you call it with the name you defined it as—NairaConvert—and give it the gross which is our worldwise gross on G2.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-334.png)
_Custom function with LAMBDA_

10. Close the parenthesis and press Ok

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-336.png)
_Calculating with Excel LAMBDA_

# Where Can I Learn More about Excel?

There are a ton of resources for learning Microsoft Excel nowadays. So many that it is hard to figure out which ones are up-to-date and helpful.

The best thing you can do is find a helpful tutorial and follow it to completion, instead of attempting to take several at once. I would advise you to start with [freeCodeCamp's Microsoft Excel Tutorial for Beginners - Full Course](https://www.youtube.com/watch?v=Vl0H-qTclOg), which is available on YouTube. 

You should also join communities like the [Microsoft Excel and Data Analysis Learning Community](https://www.meetup.com/Microsoft-Excel-and-Data-Analysis-Learning-Community/). However, if you’re looking for a compilation of resources, check out [freeCodeCamp's publication Excel tags](https://www.freecodecamp.org/news/tag/excel/).

If you enjoyed reading this article and/or have any questions and want to connect, you can find me on [LinkedIn](https://www.linkedin.com/in/ifeanyi-iheagwara/) or [Twitter](https://twitter.com/Bennykillua). 

  


  


  

