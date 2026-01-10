---
title: Google Sheets – How to Make a Dynamic Search Bar
subtitle: ''
author: Eamonn Cottrell
co_authors: []
series: null
date: '2023-06-02T13:31:11.000Z'
originalURL: https://freecodecamp.org/news/dynamic-search-bar-google-sheets
coverImage: https://www.freecodecamp.org/news/content/images/2023/06/Google-Sheets-Dynamic-Search-Bar-with-profile.png
tags:
- name: google sheets
  slug: google-sheets
- name: search
  slug: search
- name: spreadsheets
  slug: spreadsheets
seo_title: null
seo_desc: 'This tutorial is for when CTRL + F is not enough. 🔥

  I bet I''ve used the CTRL + F shortcut more than any other keyboard shortcut in
  my life. CTRL + Z probably comes close, but I use CTRL + F to find things...

  💥ALL 💥

  💥💥THE 💥💥

  💥💥💥TIME 💥💥💥


  ...'
---

This tutorial is for when CTRL + F is not enough. 🔥

I bet I've used the CTRL + F shortcut more than any other keyboard shortcut in my life. CTRL + Z probably comes close, but I use CTRL + F to find things...

💥**ALL 💥**

💥💥**THE** 💥💥

💥💥💥**TIME** 💥💥💥

![Image](https://www.freecodecamp.org/news/content/images/2023/06/more2.gif)
_gif of man saying we need more_

And yes, it'll work just fine in a Google Sheet to find information.

But sometimes I want to display a range of results based on a word I'm searching for. To do that, we'll create a dynamic search bar in our Google Sheet.

You can also follow along in this walkthrough video:

%[https://youtu.be/5xgwvokDhT0]

## The Search Bar

Our search bar is nothing more than a cell or range of cells. In the example below, it starts in J2.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/google-sheets-search-bar.png)
_Screenshot of a search bar on Google Sheets_

By adding a `=QUERY()` function in J5 we can look at whatever is typed into `J2` (the red circle) and display the search results below it (the blue rectangle).

In my example, I'm searching through a bunch of personal finance transactions (with randomized amounts😀) that are in columns `A:F`.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/google-sheets-finance-data.png)
_Screenshot of finance data on Google Sheets_

## The Query Function

The `=QUERY()` function looks in the Transactions range (which is that `A3:F` range where all the transactions live).

And it grabs all the info in either column B or column D that `CONTAINS` what we type in `J2`.

So it searches through all our transaction descriptions in column B and categories in column D for whatever we type in `J2`. The `LOWER` command turns the info in B and D into lowercase. This makes it easier to search because the `CONTAINS` command is case-sensitive.

```javascript
=QUERY(Transactions, 
       "SELECT A,B,C,D,E WHERE LOWER(B) CONTAINS '"&J2&"' OR LOWER(D) CONTAINS '"&J2&"'")
```

* the only caveat is that if you type in uppercase in the search bar, it won't work properly.

## The Filter Function

By using the `=FILTER()` function in combination with the `=SEARCH()` function, we can do the same thing in a little bit shorter formula and without having to worry about case sensitivity.

```xls
=IF(ISBLANK(J2),"",FILTER(Transactions,SEARCH(J2,B3:B225)))
```

The tradeoff here is that when we want to add multiple conditions like we did in the `=QUERY()` statement, it breaks down. Both `=FIND()` and `=SEARCH()` did not work properly when trying to use them more than once inside the `=FILTER()`.

I was able to find a work around by using the plus operator and constructing the formula in this way:

```xls
=IF(ISBLANK(J2),"",FILTER(Transactions,(B3:B225=J2)+(D3:D225=J2)))
```

Unfortunately when you filter in this way, partial matches are not included in the search results. 

In the case of Query, partial answers are always returned. 

So, when we enter "hom" all the lines with "home" in it would be returned. When using multiple conditions with filter, nothing would return unless you entered the whole word "home".

## What About XLOOKUP?

The issue with XLOOKUP is twofold. One, it doesn't handle partial matches well unless you add wildcard characters:

```xls
=XLOOKUP("*"&J2&"*",B3:B225,A3:F225,,2)
```

This increases complexity but still works. 

The more important difference is that it will only return one result so it's not going to work at all for us for this use case.

## The Winner is Query

Query takes the prize simply because it doesn't need further manipulation to add multiple conditions, and it will return all the values that meet our search criteria.

It may take you a minute to wrap your head around the syntax, but it's just as powerful and more versatile than Filter in the long haul.

The only thing to make sure to remember is case sensitivity. If you're using the `LOWER` command in your query, don't use any uppercase search letters. 

## Make it Neat

In the full formula, I've added an `=IF()` function at the start to handle the blank search bar. We want to return nothing in that case:

```xls
=IF(ISBLANK(J2),"", QUERY(Transactions "SELECT A,B,C,D,E WHERE LOWER(B) CONTAINS '"&J2&"' OR LOWER(D) CONTAINS '"&J2&"'")
```

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-30.png)
_Screenshot of a blank search bar in Google Sheets_

## Follow Along

Come [follow me over on YouTube](https://www.youtube.com/@eamonncottrell?sub_confirmation=1) as I make tutorials each week.

[Sign up here](https://got-sheet.beehiiv.com/subscribe) to get my newsletter in your email each week.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/Beehiivp.jpg)
_Eamonn's Sheets | Coding | Education logo_

