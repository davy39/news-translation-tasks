---
title: Excel Formulas – Basic Functions for Beginners
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-05-12T15:44:00.000Z'
originalURL: https://freecodecamp.org/news/excel-formulas-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/einstein-153422_1280.png
tags:
- name: excel
  slug: excel
- name: Productivity
  slug: productivity
seo_title: null
seo_desc: 'Microsoft Excel lets you use formulas and functions to perform basic and
  advanced numerical calculations. You can do addition, subtraction, multiplication,
  division, mean, worke with strings, and many others.

  In Excel, the difference between a formul...'
---

Microsoft Excel lets you use formulas and functions to perform basic and advanced numerical calculations. You can do addition, subtraction, multiplication, division, mean, worke with strings, and many others.

In Excel, the difference between a formula and a function is that a function is a predefined calculation while a formula is a user-defined calculation. 

For example, `SUM` is a function while `=SUM(E1:E9)` is a formula using the `SUM` function. 

In this article, I will show you Excel formulas and functions that will make life easier for you any time you’re working with Excel. You will also learn how to use each of the formulae. 
 
| Function      | Description | Usage |
| ----------- | ----------- |----------|
|**Excel Formulas for Working with Numbers**|
| SUM      | For adding numbers in a cell       | =SUM(D2:D10)   |
| AVERAGE   | For finding the average of certain numbers in a cell      |  =AVERAGE(E6:E8)  |
|MIN| For finding the minimum number within the numbers in cells| MIN(C1:C10)|
|MAX| For finding the maximum number within the numbers in cells | =MAX(C1:C10)|
|SUMIF| Adds all the numbers in certain cells that meet certain criteria| =SUMIF(B7:B9, “>2000”,E2:E6)|
|ISNUMBER| Returns true if a value is a number and false if its not a number| ISNUMBER(E7)|
|ISEVEN| Returns true if a number is an even number and false if it is not |ISEVEN(D3)|
|ISODD | Returns true if a number is an odd number and false if it is not |=ISODD(D10)|
| ISERROR | Returns true if a value is an error and false if it is not | =ISERROR(D9) |
|MEDIAN | Returns the number in the middle of certain numbers | =MEDIAN(D2:D10) | 
|PI | Returns the value of Pi to 15 digits | =Pi() |
| CODE | Returns a numeric code for the first character in a string in the character set used by your computer | =CODE(free) |
|RAND | Generates a random number between 0 and 1 | RAND()|
|POWER | Returns the result of a number raised to a power | =POWER(3,9)|
|ROUND | Rounds off a number to the specified number of decimal places | =ROUND(D10,3) | 
|ROMAN | Converts a number to Roman numerals | =ROMAN(2022) |
|MOD | Returns the remainder of a number when divided by another number | =MOD(123 ,3) |
|BASE | Converts a number into a text representation with the given base number | =BASE(2,32,1)|
|CEILING | Rounds up a number to the nearest integer or the nearest multiple of significance | =CEILING(D6, 2)|
|CELL | Returns information about a cell | =CELL(D9)|
|CHAR | Returns the character specified by the code number from the character set for your computer | =CHAR(D4)|
|COUNT | Counts how many numbers are in the list of certain arguments | =COUNT(D2:D10)| 
| DOLLAR | Converts a number to currency format to a specified number of decimal places | =DOLLAR(4000,4)|
| COS | Returns the cosine of an angle | =COS(60)|
| SIN | Returns the sine of an angle | =SIN(30)|
| TAN | Returns the tangent of an angle | =TAN(45)|
|**Excel Formulas for working with Dates**|
|TIME | Converts the hour, minute, and seconds to an Excel serial number in time format | =TIME(9,20,40|
|DATE | Returns the number that represents the day in Excel date-time code | =DATE(2022,5,12)|
|DAY | Converts a number to a date of the month | =DAY(243)|
|HOUR| Returns the number as an hour between 0 and 23| =HOUR(34)|
|MINUTE| Returns the minute, a number between 0 and 59 | =MINUTE(59)|
|SECOND| Returns the second, a number between 0 and 59 | =SECOND(48)|
|TODAY| Returns the current date formatted as a date | =TODAY()|
|WEEKDAY| Returns the weekday, a number between 1 and 7 | =WEEKDAY(12,4)|
| MONTH | Returns the month, a number between 1 and 12 |=MONTH(9)|
|YEAR | Returns the year, date between 1900 and 9999 |=YEAR(12) |
|**Excel Formulas for Working with Text and Strings**|
|Concatenate | Combines various texts together | =CONCATENATE("free","Code","Camp")|
|LEN| Returns the length of a string| =LEN(C1)|
|LEFT | Returns the number of specified strings from the left-hand side of a string | =LEFT(C6,5) |
| RIGHT | Returns the number of specified strings from the right-hand side of a string | =RIGHT(C6,5) |
|MID | Returns the number in the middle of string from a specified start and position and length| =MID(C7,3,5) |
|REPLACE | Replaces parts of a string with another specified string | =REPLACE(“Coding”,2,2,”og”)|
|FIND | Returns the starting position of one string with another string | =FIND(“od”,”Coding”,1) |
|ISTEXT| Returns true if a value is a string and false if it is not | =ISTEXT(D9)|
|LOWER | Converts text to lowercase | =LOWER("FREECODECAMP")|
|UPPER | converts text to uppercase | =UPPER("freecodecamp")|
|TRIM | Removes all spaces from a text except single spaces between words | =TRIM("free  code    camp")|
| EXACT | Returns true if two texts are equal and false if they are not| =EXACT("free","FREE"|
| PROPER | Converts the first letter of a word to a capital letter| =PROPER("javascript")|
| **Logical** |
|AND | Returns true if all arguments are true and false if they are not | =AND(12,34)|
|NOT| Changes false to true and true to false | =NOT(TRUE)|
|OR | Returns false only if all arguments are false | =OR(12,12)|

## Conclusion

Excel provides various functions that allow you to manipulate your data.

To check out more of these functions, click the Formula tab
![formulas](https://www.freecodecamp.org/news/content/images/2022/05/formulas.png)




