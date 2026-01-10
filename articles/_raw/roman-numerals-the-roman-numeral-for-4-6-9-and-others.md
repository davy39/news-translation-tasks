---
title: Roman Numerals – the Roman Numeral for 4, 6, 9, and Others
subtitle: ''
author: Kristofer Koishigawa
co_authors: []
series: null
date: '2022-03-28T17:41:16.000Z'
originalURL: https://freecodecamp.org/news/roman-numerals-the-roman-numeral-for-4-6-9-and-others
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/thomas-bormans-JsTmUnHdVYQ-unsplash.jpg
tags:
- name: Math
  slug: math
- name: Mathematics
  slug: mathematics
seo_title: null
seo_desc: 'Roman numerals are a numerical system that originated in ancient Rome.
  They are used to represent numbers in the decimal system, but they are not used
  for mathematical operations.

  In this system, symbols are used to represent different numbers, with ...'
---

Roman numerals are a numerical system that originated in ancient Rome. They are used to represent numbers in the decimal system, but they are not used for mathematical operations.

In this system, symbols are used to represent different numbers, with I representing 1, V representing 5, X representing 10, L representing 50, C representing 100, D representing 500, and M representing 1,000.

Here is a table of the symbols used in the Roman numeral system:

<table>
  <thead>
    <tr>
      <th style="text-align: center">1</th>
      <th style="text-align: center">5</th>
      <th style="text-align: center">10</th>
      <th style="text-align: center">50</th>
      <th style="text-align: center">100</th>
      <th style="text-align: center">500</th>
      <th style="text-align: center">1,000</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align: center">I</td>
      <td style="text-align: center">V</td>
      <td style="text-align: center">X</td>
      <td style="text-align: center">L</td>
      <td style="text-align: center">C</td>
      <td style="text-align: center">D</td>
      <td style="text-align: center">M</td>
    </tr>
  </tbody>
</table>

The value of a numeral is determined by its position in relation to other symbols. When a symbol of equal or lesser value is placed after another symbol, their values are added. But when certain symbols of lesser value are placed before another symbol, their values are subtracted.

For example, the numeral VI, or 6, would be read as "five plus one" (5 + 1), and XI, or 11, is "ten plus one" (10 + 1).

But the methods for representing 4 and 9 are special. The Roman numeral IV, or 4, would be read as "one less than 5" (5 - 1). Also, the numeral IX, or 9, would be read as "one less than 10" (10 - 1).

Here is a table of numbers and their Roman numeral equivalent, followed by more in-depth explanations about how to perform the conversions. Just scroll through the table or use Ctrl/Cmd + f to find the value you're looking for:

| Number | Roman numeral |
|--------|---------------|
| 1      | I             |
| 2      | II            |
| 3      | III           |
| 4      | IV            |
| 5      | V             |
| 6      | VI            |
| 7      | VII           |
| 8      | VIII          |
| 9      | IX            |
| 10     | X             |
| 11     | XI            |
| 12     | XII           |
| 13     | XIII          |
| 14     | XIV           |
| 15     | XV            |
| 16     | XVI           |
| 17     | XVII          |
| 18     | XVIII         |
| 19     | XIX           |
| 20     | XX            |
| 21     | XXI           |
| 22     | XXII          |
| 23     | XXIII         |
| 24     | XXIV          |
| 25     | XXV           |
| 30     | XXX           |
| 40     | XL            |
| 50     | L             |
| 60     | LX            |
| 70     | LXX           |
| 80     | LXXX          |
| 90     | XC            |
| 100    | C             |
| 101    | CI            |
| 102    | CII           |
| 103    | CIII          |
| 104    | CIV           |
| 105    | CV            |
| 200    | CC            |
| 300    | CCC           |
| 400    | CD            |
| 500    | D             |
| 600    | DC            |
| 700    | DCC           |
| 800    | DCCC          |
| 900    | CM            |
| 1,000  | M             |
| 1,001  | MI            |
| 1,002  | MII           |
| 1,003  | MIII          |
| 1,004  | MIV           |
| 1,005  | MV            |
| 1,900  | MCM           |
| 2,000  | MM            |
| 3,000  | MMM           |
| 3,999  | MMMCMXCIX     |

## How to Convert a Number into Roman Numerals

Because Roman numerals are often ordered from largest to smallest, break the number you're converting up into groups of thousands, hundreds, tens, and ones, and perform the conversion on each group.

For example, if you want to convert the number 2,014 (the year freeCodeCamp was founded) into Roman numerals, break the number up as follows:

```
2,014 = 2,000 + 10 + 4
```

Then perform the conversion on each group and combine them to get the Roman numeral equivalent:

```
* 2,000 = MM
* 10 = X
* 4 = IV

2,014 = 2,000 + 10 + 4 = MMXIV

```

## How to Represent Large Numbers in Roman Numerals

You might have noticed that the chart above only goes from 1 to 3,999.

This is due to the special methods for representing 4 and 9 mentioned above. If you check the table above, you'll see that whenever a 4 or 9 appears (including 40, 90, 400, 900) that the Roman numerals are ordered in a particular way so the lesser symbol is subtracted from the one of greater value immediate afterwards.

Since Roman numerals were never fully standardized, you might see the number 4,000 represented as MMMM.

This works, but many see this as invalid since 4 (and 9) have special representations in lower numbers.

Instead, one of the most common ways to represent larger Roman numerals is with a [vinculum](https://en.wikipedia.org/wiki/Roman_numerals#Vinculum), or a straight horizontal line above one or more symbols.

If you see a Roman numeral symbol with a horizontal line over it, that just means to multiply that symbol by 1,000.

Here are the Roman numeral symbols with the vinculum applied:

<table>
  <thead>
    <tr>
      <th style="text-align: center">1,000</th>
      <th style="text-align: center">5,000</th>
      <th style="text-align: center">10,000</th>
      <th style="text-align: center">50,000</th>
      <th style="text-align: center">100,000</th>
      <th style="text-align: center">500,000</th>
      <th style="text-align: center">1,000,000</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align: center;">M or <span style="text-decoration: overline;">I</span></td>
      <td style="text-align: center; text-decoration: overline;">V</td>
      <td style="text-align: center; text-decoration: overline;">X</td>
      <td style="text-align: center; text-decoration: overline;">L</td>
      <td style="text-align: center; text-decoration: overline">C</td>
      <td style="text-align: center; text-decoration: overline;">D</td>
      <td style="text-align: center; text-decoration: overline;">M</td>
    </tr>
  </tbody>
</table>

With this extended set of Roman numeral symbols, 4,000 would be represented as the following:

<p><span style="text-decoration: overline;">IV</span></p>

And here's a table of larger numbers and their Roman numeral representations to get you started:

<table>
  <thead>
    <tr>
      <th>Number</th>
      <th>Roman numeral</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>4,000</td>
      <td><span style="text-decoration: overline;">IV</span></td>
    </tr>
    <tr>
      <td>4,001</td>
      <td><span style="text-decoration: overline;">IV</span>I</td>
    </tr>
    <tr>
      <td>4,002</td>
      <td><span style="text-decoration: overline;">IV</span>II</td>
    </tr>
    <tr>
      <td>4,003</td>
      <td><span style="text-decoration: overline;">IV</span>III</td>
    </tr>
    <tr>
      <td>5,000</td>
      <td><span style="text-decoration: overline;">V</span></td>
    </tr>
    <tr>
      <td>6,000</td>
      <td><span style="text-decoration: overline;">VI</span></td>
    </tr>
    <tr>
      <td>7,000</td>
      <td><span style="text-decoration: overline;">VII</span></td>
    </tr>
    <tr>
      <td>8,000</td>
      <td><span style="text-decoration: overline;">VIII</span></td>
    </tr>
    <tr>
      <td>9,000</td>
      <td><span style="text-decoration: overline;">IX</span></td>
    </tr>
    <tr>
      <td>10,000</td>
      <td><span style="text-decoration: overline;">X</span></td>
    </tr>
    <tr>
      <td>40,000</td>
      <td><span style="text-decoration: overline;">XL</span></td>
    </tr>
    <tr>
      <td>90,000</td>
      <td><span style="text-decoration: overline;">XC</span></td>
    </tr>
    <tr>
      <td>400,000</td>
      <td><span style="text-decoration: overline;">CD</span></td>
    </tr>
    <tr>
      <td>900,000</td>
      <td><span style="text-decoration: overline;">CM</span></td>
    </tr>
    <tr>
      <td>1,000,000</td>
      <td><span style="text-decoration: overline;">M</span></td>
    </tr>
  </tbody>
</table>

## How to Add a Vinculum or Horizontal Line Over Roman Numerals With HTML and CSS

For you devs out there, the easiest way to add a vinculum to Roman numerals online is to wrap the symbols in an element and use a bit of CSS.

For example, to add a horizontal line over the symbols IV in IVIII, you can wrap them in a `span` element and set its `text-decoration` property to `overline`:

```html
<p><span style="text-decoration: overline;">IV</span>III</p>
```

Which will render the following:

<p><span style="text-decoration: overline;">IV</span>III</p>

## **Thanks for Reading**

If you found this breakdown of Roman numerals helpful, please share it with your friends so more people can benefit from it.

Also, feel free to reach out on [Twitter](https://twitter.com/kriskoishigawa) and let me know what you think.

