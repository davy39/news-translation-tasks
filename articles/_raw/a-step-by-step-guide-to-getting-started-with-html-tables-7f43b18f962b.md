---
title: A step-by-step guide to getting started with HTML tables
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-11T01:06:12.000Z'
originalURL: https://freecodecamp.org/news/a-step-by-step-guide-to-getting-started-with-html-tables-7f43b18f962b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*NmvyJ4xEENdOUXBvmbHgpg.png
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: HTML
  slug: html
- name: General Programming
  slug: programming
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Abhishek Jakhar

  Overview

  The web is filled with information like football scores, cricket scores, lists of
  employee names and email addresses. HTML tables enable you to display information
  in what is commonly known as tabular data.


  NOTE: I have a...'
---

By Abhishek Jakhar

#### Overview

The web is filled with information like football scores, cricket scores, lists of employee names and email addresses. HTML tables enable you to display information in what is commonly known as **tabular data**.

> **NOTE:** I have already added the Styling using CSS, so my elements will look different. But they will work in exactly the same way.  
> If you want to make your elements look like mine then, you can find my CSS file in the links given below:  
> **CSS:** [https://gist.github.com/abhishekjakhar/2ea51dfc0dcf6f6ed0d44ac0e72f9c54](https://gist.github.com/abhishekjakhar/2ea51dfc0dcf6f6ed0d44ac0e72f9c54)

#### Basic Table

We can create an HTML table using the table element. It has an opening and closing tag, and it wraps all the **table rows** and **table cells** inside of it.

```
<table></table>
```

Now, let’s type a table row. Tables are made up of rows of information that go across the page. A **<**tr> element is used to create a table row.

However, there is no element for the table column. **Table columns** depend on how many **table cells** are **inside each row**. A **<**td> element is used to create a table cell. So basically the numb**er o**f <td> elements you will add **ins**ide the <tr> element is the exact same number of columns you will get inside your table row.

To recap:

* **<table**>: The table element represents data in a series of rows and columns. Tables should only be used for displaying tabular data, and never for page layout.
* **<tr**>: The table row element defines a row of cells in a table. Table rows can be filled with table cells and table header cells.
* **<td**>: The table cell element contains data and represents a single table cell. Each table cell should be inside a table row.

![Image](https://cdn-media-1.freecodecamp.org/images/1*yOyJaEaHDXFPhiYsCAa_Pg.png)
_**table row (&lt;t**r&gt;**) and tabl**e **cell (**&lt;td&gt;) elements together to form a table_

> **Note:** <table> elements have no attributes. If you’ve worked with tables before, you may have used some attributes in the past. However, they are all now deprecated.

#### Table Header Element

We’ve created a basic table, but it’s not clear that our first row in the table is actually an attempt to label each of our columns. Right now, the first row simply looks like another row in our table.

We can use a **table header element** on each of these three columns to tell the browser, search engine crawlers, and screen readers that these are actually headers and not just regular data.

Now we will be changing table cells in the first row to a table headers cell. To do that we will replace **<**td&g**t; b**y <th>.

![Image](https://cdn-media-1.freecodecamp.org/images/1*w9jJlM8jiASJryGjS0Exaw.png)
_The text in the first row is bolder than the other rows because of the **&lt;**th&gt; element used inside the **firs**t &lt;tr&gt;_

#### Table Head & Body

Similar to the structure of our HTML document, where we have a head and a body, we can also add a head and a body to our table. We will definitely not use the same HTML elements because then the syntax will become invalid. For the table, we have **<the**ad> fo**r th**e hea**d and &l**t;tbody&**gt;** for the body.

* **<the**ad> — The table head element (not to be confused with the table header cell element) defines a set of rows that make up the header of a table.
* **<tbo**dy> — The table body element defines one or more rows that make up the primary contents (or “body”) of a table.

![Image](https://cdn-media-1.freecodecamp.org/images/1*j8s-VYH2HgcKHC7F5Ir4xA.png)
_**table head (&lt;thea**d&gt;**) and table body (&amp;l**t;tbody&gt;) elements_

#### Table Foot Element

We have a **table head** and a **table body** element. So of course, there’s a **table foot** element as well. But the question is what is the point of table footer element when we already have the table headers that label columns?

In general, a table footer element should **contain a summary of the table.** This might be some final cells containing sums, totals and averages for each column. It might also contain some meta information like copyright information or the source of data within a table.

Now, you would think that the table footer would go at the bottom of the table. However, it actually should go **right after** the **table head** element and **just before** the **table body** element.

* **<tfoot&**gt; — The table footer element defines a set of rows summarizing the columns of the table.

![Image](https://cdn-media-1.freecodecamp.org/images/1*gAmY0_Zv-Lo4LCeKLbgmgg.png)
_**table foot (&lt;tfoo**t&gt;) element_

#### Caption Element

This element is basically a title for the table, and it should come immediately after the opening table tag. This is nice to add because it quickly summarizes what a table might contain.

![Image](https://cdn-media-1.freecodecamp.org/images/1*uDdPUgPmOUt_nm1_XgUs0w.png)

Now we have covered the essentials of table elements in HTML.

You can learn more about the **tables** in the **links** given below.

[**HTML Table Basics**](https://developer.mozilla.org/en-US/docs/Learn/HTML/Tables/Basics)  
[_That just about wraps up the basics of HTML Tables._developer.mozilla.org](https://developer.mozilla.org/en-US/docs/Learn/HTML/Tables/Basics)[**HTML Table Advanced**](https://developer.mozilla.org/en-US/docs/Learn/HTML/Tables/Advanced)   
[_There are a few other things you could learn about HTML Tables._developer.mozilla.org](https://developer.mozilla.org/en-US/docs/Learn/HTML/Tables/Advanced)

I hope you’ve found this post informative and helpful. I would love to hear your feedback!

**Thank you for reading!**

