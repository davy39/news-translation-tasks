---
title: RegEx for Date Formats – Regular Expressions for Matching Dates
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2023-05-18T12:41:17.000Z'
originalURL: https://freecodecamp.org/news/regex-for-date-formats-what-is-the-regular-expression-for-matching-dates
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/dateRegEx.png
tags:
- name: Regex
  slug: regex
seo_title: null
seo_desc: 'Regular expressions let you match any string, be it in the form of various
  user inputs such as username, password, URL, and even different date formats.

  In this article, I’ll show you several ways you can match a date with regular expressions.

  In the...'
---

Regular expressions let you match any string, be it in the form of various user inputs such as username, password, URL, and even different date formats.

In this article, I’ll show you several ways you can match a date with regular expressions.

In the programming world, there are always multiple ways of doing the same thing. So, how I’ll show you how to match date formats with regex might be different from how you’ll see it elsewhere.


## What We'll Cover
- [How to Match Dates with Regular Expressions](#heading-how-to-match-dates-with-regular-expressions)
  - [How to Match Dates with Regular Expressions – Example 1](#heading-how-to-match-dates-with-regular-expressions-example-1)
  - [How to Match Dates with Regular Expressions – Example 2](#heading-how-to-match-dates-with-regular-expressions-example-2)
  - [How to Match Dates with Regular Expressions – Example 3](#heading-how-to-match-dates-with-regular-expressions-example-3)
- [Conclusion](#heading-conclusion)


## How to Match Dates with Regular Expressions
Dates are usually numbers unless you format them with some programming tools. So, the characters I will use to match dates will be digit characters.


### How to Match Dates with Regular Expressions – Example 1
Let’s start with something less complex first. Assuming the date format is in `DD/MM/YYYY` or `MM/DD/YYYY`, this would work:

```bash
\d{1,2}\/\d{1,2}\/\d{2,4}
```
In the regex above:

* `\d{1,2}` matches 1 or 2 digits
* `\/` matches a slash (the separator). You can also make a hyphen (-) the separator
* \d{2,4} matches 2 or 4 digits

Indeed, the pattern matches a date:

![Screenshot-2023-05-18-at-11.08.02](https://www.freecodecamp.org/news/content/images/2023/05/Screenshot-2023-05-18-at-11.08.02.png) 

But that pattern is too generic because we don’t know which is which between the date and the month. The year can also be 2 or 4 digits. 

In short, anything that is not a valid date would go:

![Screenshot-2023-05-18-at-11.11.10](https://www.freecodecamp.org/news/content/images/2023/05/Screenshot-2023-05-18-at-11.11.10.png) 


That’s not how you want to match a date. I’ll show you a better pattern next.


### How to Match Dates with Regular Expressions – Example 2
Here’s another pattern that can match a date:

```bash
(0[1-9]|[12][0-9]|3[01])\/(0[1-9]|1[0,1,2])\/(19|20)\d{2}
```

In the pattern above: 

* `(0[1-9]|[12][0-9]|3[01])` is the first group of the pattern and it lets you specify the date only between `01` and `31`
* `\/` is the separator
* `(0[1-9]|1[0,1,2])` represents the month and it lets you specify it between `01` and `12`
* `\/` is another separator
* `(19|20)\d{2}` represents the year which can be between 1900 and any 2000 year

![Screenshot-2023-05-18-at-11.37.38](https://www.freecodecamp.org/news/content/images/2023/05/Screenshot-2023-05-18-at-11.37.38.png) 

You can replace the separator with any hyphen this way:

```bash
(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[1,2])-(19|20)\d{2}
```

And you can accept both forward slash and hyphen as a separator:

```bash
(0[1-9]|[12][0-9]|3[01])(\/|-)(0[1-9]|1[1,2])(\/|-)(19|20)\d{2}
```

![Screenshot-2023-05-18-at-11.41.32](https://www.freecodecamp.org/news/content/images/2023/05/Screenshot-2023-05-18-at-11.41.32.png)

You can also rearrange the pattern to be in the `MM/DD/YYYY` format this way:

```bash
(0[1-9]|1[1,2])(\/|-)(0[1-9]|[12][0-9]|3[01])(\/|-)(19|20)\d{2}
```

![Screenshot-2023-05-18-at-11.46.46](https://www.freecodecamp.org/news/content/images/2023/05/Screenshot-2023-05-18-at-11.46.46.png)


### How to Match Dates with Regular Expressions – Example 3
Many times, you’ll be accepting just one date in your input. In that case, you have to specify the start and end of a string with caret (`^`) and dollar sign (`$`).

This is how I came with that pattern:

```bash
^(3[01]|[12][0-9]|0?[1-9])(\/|-)(1[0-2]|0?[1-9])\2([0-9]{2})?[0-9]{2}$
```

And here’s what the pattern does:

- `^` denotes the start of the string
- `(3[01]|[12][0-9]|0?[1-9])` represents the day
    - `3[01]` matches numbers from `30` to `31`
    - `[12][0-9]` matches numbers from `10` to `29`
    - `0?[1-9]` matches numbers from `1` to `9`, with an optional leading zero
- `(\/|-)` matches either a forward slash (`/`) or a hyphen (`-`)
- `(1[0-2]|0?[1-9])` represents the month part
   - `1[0-2]` matches numbers from `10` to `12`
   - `0?[1-9]` matches numbers from `1` to `9`, with an optional leading zero
- `\2` is a backreference that matches the same delimiter captured in the second capturing group `(\/|-)`. This ensures that the delimiter between day and month is consistent
- `([0-9]{2})?` matches the two-digit year part optionally
- `([0-9]{2})` matches any two digits representing a year
- `[0-9]{2}` matches the last two digits of the year
- `$` denotes the end of the string


## Conclusion
This article took you through how to match a date with regular expressions with three examples.

The first example is a bit generic and won’t do well in matching a date, but the second can match valid dates in an input. The third does it better as it is tailored for a valid and single date – which would likely be what you want to do.


