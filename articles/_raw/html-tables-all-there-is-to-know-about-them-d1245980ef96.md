---
title: 'HTML Tables: All there is to know about them'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-30T16:21:36.000Z'
originalURL: https://freecodecamp.org/news/html-tables-all-there-is-to-know-about-them-d1245980ef96
coverImage: https://cdn-media-1.freecodecamp.org/images/1*UFIlBVRuLEGCGfliYgNwsA.jpeg
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: HTML
  slug: html
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Alexander Gilmanov

  Judging by the fact that we created wpDataTables, it’s no secret that we like tables.
  So much that we wrote this lengthy article about them to help out those of you who
  are beginners and want to learn about HTML tables.

  HTML tab...'
---

By Alexander Gilmanov

Judging by the fact that we created [wpDataTables](https://wpdatatables.com/), it’s no secret that we like tables. So much that we wrote this lengthy article about them to help out those of you who are beginners and want to learn about HTML tables.

HTML tables are used for displaying data that make sense in spreadsheet software. They consist of rows and columns and are often used on websites for the effective displaying of tabular data.

So how to make a table in HTML? When to use it and why? What are good HTML table examples? Today, we are going to answer these questions and more to help you understand everything there is to know about HTML tables.

### Table of contents

* Introduction to tables
* Table styling
* HTML tables frequently asked questions
* HTML table generator tools

### Introduction to tables

The HTML table is used for arranging data (such as text, images, links etc.) into the tabular design — basically, rows and columns.

#### When to Use Tables

A table in HTML makes a lot of sense when you want to organize data that would look best in a spreadsheet. An HTML table is a great way to display things such as financial data, calendars, pricing, feature comparison, the nutrition facts information panel, bowling scores, and many other tabular data.

There is a chance you have heard that the tables were unsemantic. However, that is not at all true. Tables semantically indicate tabular data and they are the best choice for displaying data of this kind.

#### When NOT to Use Tables

While some data looks great in tables, there are things that shouldn’t be arranged that way simply because it wouldn’t make any sense. There are also some other inappropriate CSS table uses that should be avoided if possible.

For example, **you should never use tables for layout**. The thing is that table elements semantically describe tabular data and using them for other purposes is a breach of semantic duty.

The general rule is that the websites should be accessible. One part of accessibility is screen readers which read tables from top to bottom, left to right. With the tables in HTML, the order of how the site is presented is determined by visual choices instead of the accessibility choices. In cases like that, screen readers don’t always work as you’d want them to.

### Table Elements

HTML tables usually come with a short description of their purpose. Sometimes, a more detailed description is provided via the summary attribute for the benefit of people using speech or Braille-based user agents.

Table rows may be grouped into a head, foot, and body sections, (via the **THEAD**, **TFOOT** and **TBODY** elements). User agents may exploit the head/body/foot division to support scrolling of body sections independently of the head and foot sections. When we print the long HTML tables, the head and foot information is usually displayed on each page containing the table.

If you want to provide more structural information, you can also group columns. In addition to that, column properties may be declared at the start of the table definition using the **COLGROUP** and **COL** elements.

Table cells contain the header information and/or data and they can span multiple columns and rows. When you label each cell with the HTML 4 table mode, the non-visual user agents can communicate the information to the user more easily. Not only is this useful for users with disabilities but it makes it possible for modal wireless browsers with limited display capabilities to handle HTML tables.

We mentioned already that tables HTML should not be used for layout. Instead, you should use style sheets whenever necessary to achieve better results and better accessibility.

#### Head and Body

Let’s take a look at a basic example of HTML table style:

Imagine looking at a row (horizontal) to see a single person and relevant information about them. When you look up and down a column (vertical), you will get a sense of the variety or pattern of data.

The first row is the header of the table and it contains no data — just the titles of the columns. You can semantically indicate that is the case with the **<the**ad> element, which would wrap the **firs**t <tr> (it could wrap as many rows as needed that are all header information).

When you use **<the**ad>, there must **be n**o <tr> that is a dire**ct chil**d of <table>. All rows must be **within** ei**ther th**e <**;thead&**gt;, <tbody>, or <tfoot>.

#### Table Footer

Along with **<the**ad>**; and &**lt;tbody>**;, ther**e is <tfoot> for wrapping table rows that indicate the footer o**f the t**able. Like <thead>, best for semantically indicating that these are not data rows but ancillary information.

The placement of **<tfo**ot> is unique in HTML as it comes **after &**lt;thead> **and be**fore <tbody>! So even though it might seem logical to find **it at** the end of <table>, it is actually not the case. Since the footer contains information necessary to understand the table, it is placed before the data in the source order for better accessibility.

Table footer can be used in long HTML tables to repeat the header, for example. However, it can be used for other purposes as well, for instance, with a layout where the position of elements jumps around from bottom to top depending on needs.

### Table Elements and their Attributes

#### <tfoot> HTML Tag

The **<tfo**ot> element identifies one or **mor**e <tr> elements as containing summary contents of a table’s c**olumns.** The <tfoot> element must be the direc**t desce**ndant of a <table> element.

In HTML5, **<tfo**ot> can be placed either before or **after &**lt;tb**ody&**gt; and <tr>elements, but must **appear a**ft**er any <**;capti**on>,** <colgroup>, and <thead> elements.

#### <tbody> HTML Tag

The **<tbo**dy> element must be a direct descendant **of a &**lt;table> element and is used **to i**dentify <tr> elements that comprise the body **of the** table. The <tbody> element sho**uld alw**ays come after a <thead> element a**nd may** come before or after a <tfoot> element.

#### <tr> HTML Tag

**Attributes**

* <tr align=””>
* <tr valign=””>
* <tr bgcolor=””>
* <tr background=””>
* <tr bordercolor=””>

The **<**tr> element is used to group tog**ethe**r &l**t;th**> or <td> values into a single row of table heading or **dat**a values. The <tr> element may **be a d**irect child of a <table> elem**ent or** ne**sted wi**thin **a paren**t <thead>, <tfoot>, or <tbody> element.

#### <thead> HTML Tag

**Attributes**

The **<capti**on> element is used to add a caption to an HTML tab**le. A <**;caption> must appear in an HTML document as the first descendant **of a pa**rent <table>, but it may be positioned visually at the bottom of the table with CSS.

#### col

**Attributes**

The **<c**ol> element, typically implemented as a child element of a p**arent <**colgroup>, can be used to target a column in an HTML table.

#### colgroup

**Attributes**

The **<colgro**up> element is used a parent container for one or **more** <col>elements which are used to target columns in an HTML table.

### Basic Styling

Distinguishing different parts of the table is easy if the table has different colors and lines. CSS table border is another common element. By default, all table cells are spaced out from one another by 2px. Between the first row and the rest, you will notice a slight extra gap caused by the default border-spacing being applied to the **<the**ad>**; and &l**t;tbody> pushing them apart a bit extra.

You can control the spacing:

`table {border-spacing: 0.5rem;}`

Or you can simply remove that space:

`table {border-collapse: collapse;}`

HTML table padding, HTML table heading, borders, and making <th> elements left-aligned is a simple yet effective way to style your HTML tables.

### Important Style Rules for Tables

CSS tables and their properties work great if you use them right. There are, however, some details to keep in mind. For example, if you apply a certain font-family to the table, but then a different one to the cell — the cell wins because it is the actual element with the text inside.

These properties are either unique to table elements or they behave uniquely on table elements.

#### vertical-align

**Possible values**: baseline, sub, super, text-top, text-bottom, middle, top, bottom, %, length

Aligns the content inside a cell. Works particularly well in tables, although only the top/bottom/middle make much sense in that context.

#### white-space

**Possible values:** normal, pre, nowrap, pre-wrap, pre-line

Controls how text wraps in a cell. Some data may need to be all on one line to make sense.

#### border-collapse

**Possible values:** collapse, separate

Applied to the table to determine if borders collapse into themselves (sort of like margin collapsing only bi-directional) or not. What if two borders that collapse into each other have conflicting styles (like color)? The styles applied to these types of elements will “win”, in order of “strength”: cell, row, row group, column, column group, table.

#### border-spacing

**Possible values:** length

If border-collapse is separate, you can specify how far cells should be spaced out from each other. The modern version of the cellspacing attribute. And speaking of that, padding is the modern version of the cellpadding attribute.

#### width

**Possible values:** length

Width works on table cells just about how you would think it does, except when there is some kind of conflict.

For instance, if you tell the table itself to be 400px wide then the first cell of a three-cell row to be 100px wide and leave the others alone, that first cell will be 100px wide and the other two will split up the remaining space.

But if you tell all three of them to be 20000px wide, the table will still be 400px and it will just give each of them a third of the space. That’s assuming white-space or elements like an image don’t come into play.

#### border

**Possible values:** length

Border works on any of the table elements and just about how you would expect. The quirks come in when you collapse the borders.

In this case, all table cells will have only one border width between them, rather than the two you would expect them to have (border-right on the first cell and border-left on the next cell).

In order to remove a border in a collapsed environment, both cells need to “agree” to remove it. Like this:

```
td:nth-child(2) { border-right: 0; } td:nth-child(3) { border-left: 0; }
```

Otherwise, source order/specificity wins which border is shown on which edge.

#### table-layout

**Possible values:** auto, fixed

auto is the default. The width of the table and its cells depends on the content inside.

If you change this to fixed, the table and column widths are set by the widths of table and col elements or by the width of the first row of cells.

Cells in subsequent rows do not affect column widths, which can speed up rendering. If the content in subsequent cells can’t fit, the overflow property determines what happens.

#### Table Border

Table border CSS makes it easier to see the table and it is also the best method for displaying borders. Add styles, within the <style></style> tags located in the head element, to show the border for the table, th and td elements within your HTML document.

#### Connecting Cells

To understand how connected cells work, we need to explain the two attributes that can go on any table cell element: HTML rowspan and HTML colspan. If a td has a colspan of 2 (i.e. <td colspan=”2″>) will take up the space of two cells in a row horizontally even though it would still be a single cell. The same goes for rowspan, but vertically.

Rowspan is a bit harder to grasp simply because columns are grouped differently than rows. For example, with colspan, you get the final value by simply adding up the values for each table cell in the row. With rowspan, on the other hand, the row below it gets +1 to its table cell count and needs one less table cell to complete the row.

#### Nesting Tables

“Nesting tables” simply means placing a table inside another table which is doable, but you need to include the complete structure with the <table> element. However, it might not be the best idea because of the confusing markup and worse accessibility.

However, there are situations when this is absolutely necessary and yes, it is doable. So, for example, if you need to import content from other sources, you can import a table and place it inside your table.

#### Zebra Striping Tables

Colors are very helpful for the users to easily spot what they are looking for in the table. You can either set a background color to the table cell elements or you can set them on the table rows themselves.

This is the most basic example:

`tbody tr:nth-child(odd) {background: #eee; }`

Using tbody is useful if you don’t want to stripe header and footer rows. If you don’t want to let what is underneath show through, you can set the even rows as well.

If you need to support browsers that don’t understand: nth-child() (pretty damn old) you could use jQuery to do it.

#### Highlighting Rows and Columns

Highlighting rows is pretty easy; all it takes is adding a class name to a row.

Highlighting columns, on the other hand, takes a bit more effort. You can use the **<c**ol> element, which will allow you to set styles for cells that appear in the selected column. For example, a table with 4 columns in each row would need to h**ave 4** <col> elements.

#### How to center an HTML Table

How to center a table in HTML? This question is pretty common among people designing their first HTML tables. The thing is that text-align:center doesn’t center a table as a whole — it just centers the text inside the cells.

Centering the whole table needs left and right margins set to _auto_, and top and bottom margins set to the values you need.

Say you want the top and bottom margins of your table to be one blank line (1em). The CSS code in the **<tab**le> tag is simply:

`<table style=”margin:1em auto`;”>

If you wish to wrap text next to a table, use _float:left_ to float the table to the left of the subsequent text. To put a little space between the table and the text, you can also put the right margin on the table, like this:

`<table style=”float:left; margin-right:10px`;”>

If you want the table to be to the right of the neighboring text, use _float:right_ instead. You can also set the left margin:

`<table style=”float:right; margin-left:10px`;”>

Something to keep in mind: Make sure you put the text that should be next to the table after the closing </table> tag for the table. Floats float next to subsequent content in the code, not content that precedes the float.

### HTML tables frequently asked questions

![Image](https://cdn-media-1.freecodecamp.org/images/1*IlTpsqI9LEC4vNclDhbuNQ.jpeg)

#### Can I nest tables within tables?

Yes, you can place an existing table inside the cell of another table. There is an example mentioned earlier in this article.

Keep in mind that the older browsers have problems with nested tables if you don’t explicitly close your **TR**, **TD**, and **TH** elements. To avoid these issues, include every **</**tr**>,** </**td>**;, and </th> tag, even though the HTML specifications don’t require them.

Also, try not to nest tables more than a few rows deep into the table because the older browser versions often have problems with that. You can use the **ROWSPAN** and **COLSPAN** attributes to minimize table nesting.

Finally, be especially sure to validate your markup whenever you use nested tables.

#### How can I use tables to structure forms?

Within a **TD** element within a table, there can be small forms placed if you want to position a form relative to the other content. However, if you want to position the form-related elements relative to each other, it doesn’t really help.

If you want to do that, the entire table must be within the form. You can’t start a form in one **TH** or **TD** element and end in another. You can’t place the form within the table without placing it inside a **TH** or **TD** element. You can put the table inside the form, and then use the table to position the **INPUT**, **TEXTAREA**, **SELECT**, and other form-related elements, as shown in the following example.

#### Can I use percentage values for <TD WIDTH=…>?

The HTML 3.2 and HTML 4.0 specifications allow only integer values (representing a number of pixels) for the WIDTH attribute of the TD element. The he HTML 4.0 DTD, on the other hand, allows non-integer values (such as percentages), so an HTML validator will not complain about <TD WIDTH=”xx%”>.

Keep in mind that Netscape and Microsoft’s browsers interpret percentage values for <TD WIDTH=…> differently. On the other hand, their interpretations (and those of other table-aware browsers) match when combined with <TABLE WIDTH=”100%”>. In cases like that, percentage values can be used safely, even though they are prohibited by the public specifications.

#### Why doesn’t <TABLE WIDTH=”100%”> use the full browser width?

The margin between the content and the edge of the display area is quite narrow with graphical browsers. Navigator always leaves room for a scrollbar on the right. However, when the document is not long enough to require scrolling, the scrollbar doesn’t appear and this leaves you with the margin on the right that can’t be removed.

#### Why is there extra space before or after my table?

An invalid HTML syntax can cause extra space before and after HTML tables. The most common cause is the loose content within the table (i.e., content that is not inside a **TD** or **TH** element).

When it comes to the loose content, there isn’t a standard way to handle it. Some browsers display it before or after the table. When the loose content contains only multiple line breaks or empty paragraphs, all this empty space will be displayed before or after the table itself.

The solution is to fix the HTML syntax errors. All content within a table must be within a **TD** or **TH** element.

#### Are there any problems with using tables for layout?

The short answer would be — **yes**.

In order for the browsers to display the table, the HTML table attributes, particularly the **HEIGHT** or **WIDTH** attributes need to be known. The thing is that the entire table has to be downloaded with the known dimensions before being rendered. If the above-mentioned attributes aren’t known, the rendering process can be delayed.

In addition to that, if any of the table’s content is too wide for the available display area, the table has to stretch to display the oversized content. The rest of the content then adjusts to fit the oversized table rather than fitting the available display area. As a result of that, the users need to scroll horizontally to be able to read the content. The printed versions can also end up being cropped.

If the content is viewed on a display narrower than anticipated, the fixed-width tables cause the same problems as other oversized tables. If the displays are wider than anticipated, much of the display is will be wasted with the extremely wide margins. If the readers require larger fonts, the content will be displayed with only a few words per line.

One of the most important things to keep in mind is the correct syntax. The browsers don’t do well with invalid syntax. Nested tables may not display correctly with correct syntax either in older versions of Netscape Navigator.

Then there are also some browsers that completely ignore tables which means they would also ignore the layout created with the HTML tables. In addition to that, search engines also ignore them. What you normally see in search results is usually the text at the beginning of a document. As a result of that, if a table is used for layout, instead of the actual content, navigation links appear in the search.

Some versions of Navigator have problems linking to named anchors when they are inside a table that uses the **ALIGN** attribute. They associate the named anchor with the top of the table, instead of the content of the anchor. If you don’t use **ALIGN** attribute on your tables, this problem can be entirely avoided.

All that being said, if you insist on using HTML tables for layout, careful markup can help you minimize the related issues. Avoid placing wide content inside tables such as wide images, **PRE** elements with long lines, long URLs, and similar.

Use several independent tables rather than a single full-page layout. For instance, you could use a table to lay out a navigation bar at the top or the bottom of the page, and leave the main content completely outside any layout tables.

#### How to add a caption to your table with <caption>?

You add a caption to your table by putting it inside a [<capti](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/caption)on> element and nesting it insid**e the &**lt;table> element. You should put it just below **the ope**ning <table> tag.

```
<table> <caption>Your caption should be here</caption> ... </table>
```

The purpose of the caption is to contain a description of the table content. This gives the readers a quick idea of whether the table contains the content they are searching for. However, it is particularly useful for the visually-impaired users who can avoid having the screen reader read a lot of the table content before realizing what the table is about.

A caption is placed directly beneath the **<tab**le> tag.

Note: The summary attribute can also be used on the **<tab**le> element to provide a description — this is also read out by screen readers. We’d recommend usin**g the <**;caption> element instead because the summary is deprecated by the HTML5 table spec, and doesn’t appear on the page.

### Best HTML Table Generator Tools

If you don’t want to deal with a bunch of HTML table code, using a good table generator tool could be really useful. Creating a table in HTML with a tool like this requires no knowledge of developing languages and it is pretty fast and simple.

In addition to that, the majority of the best tools of this sort are completely free of charge and everyone can use them. Basically, all you have to do is import the data, and customize the table (for example, HTML table border style, HTML table formatting, CSS table width, CSS table background color, cellspacing, cellpadding etc).

Once you are done with that, the generator will give you your table HTML code that you will simply copy and paste to your website. Easy-peasy.

#### Why Should You Use HTML Table Generator Tools

Designing a table from scratch is no easy task. Making it perfectly functional is an uphill battle and it takes a lot of time and effort — not to mention that the results often end up being less than perfect.

Instead of writing lines and lines of code with your notepad, you can save yourself a lot of time and trouble with the right HTML table generator tool. Not only is it easier but the results are often better than when you try to build the whole thing yourself. Not to mention how much time it will save you, and we all know time is money.

### HTML table generator tools

#### [Tables generator](http://www.tablesgenerator.com/html_tables)

![Image](https://cdn-media-1.freecodecamp.org/images/1*_EHfuyYjdmcl3NN4BkAcJQ.jpeg)

Very useful HTML table generator tool. Easy to use and it allows you to choose the theme you like best. You can learn more about it on the official website.

#### [Quackit](http://www.quackit.com/html/html_table_generator.cfm)

![Image](https://cdn-media-1.freecodecamp.org/images/1*GD-6r6smQraAI_El5jk58g.jpeg)

A simple and easy-to-use tool that also happens to be free of charge.

#### [Truben](http://truben.no/latex/table/)

![Image](https://cdn-media-1.freecodecamp.org/images/1*C4G_v1UPRcQCsY60avTwAg.jpeg)

Truben allows you to make all kinds of HTML tables quickly and easily.

#### [Html-tables](http://html-tables.com/)

![Image](https://cdn-media-1.freecodecamp.org/images/1*xk9W4CUlPP3aXKWwCz-Zwg.jpeg)

A handy tool that works similarly to word processors. It lets you create beautiful tables free of charge.

#### [CSS Table generator](http://www.csstablegenerator.com/)

![Image](https://cdn-media-1.freecodecamp.org/images/1*bwDVOj6xgPOOhsgeDdLHjA.jpeg)

Great tool for creating stylish tables without the use of images.

#### [Tablestyler](http://tablestyler.com/)

![Image](https://cdn-media-1.freecodecamp.org/images/1*Ke1T1TXqDO-0w67w2E4w6A.jpeg)

Use table CSS elements and create gorgeous HTML tables with this online tool.

#### [Textfixer](http://www.textfixer.com/html/html-table-generator.php)

![Image](https://cdn-media-1.freecodecamp.org/images/1*FBGbuZ-IHehw5esqSTKSwQ.jpeg)

A simple tool for creating your favorite table style.

#### [Accessify](http://accessify.com/tools-and-wizards/accessibility-tools/table-builder/)

![Image](https://cdn-media-1.freecodecamp.org/images/1*BYzMYV3bC9hwhTvwfsZsvA.jpeg)

One of the simplest tools; perfect for people with little technical knowledge and/or slow internet connection.

#### [RapidTables](https://www.rapidtables.com/)

![Image](https://cdn-media-1.freecodecamp.org/images/1*u0Iqq-tKoNWD9cow5kOrLg.jpeg)

This tool comes with a variety of generating options and creating great HTML tables is one of them.

#### [Tableizer](http://tableizer.journalistopia.com/)

![Image](https://cdn-media-1.freecodecamp.org/images/1*Zwb6_Tv214beAfvZs_vtIA.jpeg)

A useful generator for designing HTML tables out of spreadsheet data.

### Ending thoughts on learning about HTML Tables

Creating beautiful and functional HTML tables is no easy task. If you want to build them from scratch, you have to have a certain amount of coding knowledge and developing experience because there are many things to consider if you want the table display the content properly.

If, on the other hand, you are looking for a quick solution that requires no coding experience, you could always consider using one of many handy table generator tools. Not only will they save you a lot of time and trouble, but the results will also be amazing.

If you enjoyed reading this article about HTML tables, you should also read these:

* [CSS tables and their code that you can use](https://wpdatatables.com/css-tables/)
* [Building Responsive Tables with CSS & HTML or WordPress](https://wpdatatables.com/responsive-tables/)
* [jQuery Table Plugins You Should Check Out](https://wpdatatables.com/jquery-table-plugins/)

_Originally published at [wpdatatables.com](https://wpdatatables.com/html-tables/) on October 31, 2018._

