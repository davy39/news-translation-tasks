---
title: Stop writing extra code — you can do it in SQL instead
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-03T22:13:24.000Z'
originalURL: https://freecodecamp.org/news/stop-writing-extra-code-you-can-do-it-in-sql-instead-61883bfcf16d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*a0b9O6_F9pLl_BpkjiBPrA.jpeg
tags:
- name: software development
  slug: software-development
- name: Software Engineering
  slug: software-engineering
- name: SQL
  slug: sql
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Geshan Manandhar


  “SQL, Lisp, and Haskell are the only programming languages that I’ve seen where
  one spends more time thinking than typing.“ — Philip Greenspun


  Even with thinking more than typing SQL (Structured Query Language) we software
  engin...'
---

By Geshan Manandhar

> **“SQL, Lisp, and Haskell are the only programming languages that I’ve seen where one spends more time thinking than typing.“** — Philip Greenspun

Even with thinking more than typing SQL (Structured Query Language) we software engineers use it as a way to only pull the data.

> _We usually don’t leverage SQL’s power of data manipulation to do the necessary changes in our code._

This is quite common among software engineers who work in web applications. Another thing we miss is, if we do the manipulation in SQL directly, the pulled data will be the same format for any programming language. This post aims to enlighten you about the powers of SQL you might know but generally don’t use.

![Image](https://cdn-media-1.freecodecamp.org/images/DbqkDm6MXNYDaK6uYMfg0JO-8v4ZwikjhB7f)
_Tea Lights image from [Pixabay](https://pixabay.com/en/tea-lights-candles-light-prayer-2223898/" rel="noopener" target="_blank" title=")_

### TL;DR

Here are the highlights:

* Use SQL to do math like sum, average etc.
* Utilize it for grouping one to many relational values like getting categories of products.
* Leverage SQL for string manipulation like using CONCAT_WS for concating first name and last name.
* Exploit SQL to sort by a custom priority formula.

Examples below…

### Some Assumptions

Below are some assumptions made for this post:

1. Just because you can do it in SQL, doesn’t mean you need to do it in SQL and use the database resources. Always profile your solution and then decide where is it best to use it. There have been suggestions that it is more difficult and costly to scale a database than application code.
2. Use SQL wisely and optimally. Always think of the necessary resources like processor and memory. `EXPLAIN` is your friend for query optimization.
3. This post does not advocate putting all logic in the database like in the form of triggers, stored procedures, or views. The code in the database generally cannot be put into a version control system and testing database code is difficult.
4. SQL is generally case insensitive, so be careful when performing operations like `CONCAT` or any other string manipulation.
5. In distributed systems, it is a balance of trade-offs. Same applies for deciding to do something in SQL or the programming language. Evaluate your options and choose the best one depending on the use case.
6. The example below uses MYSQL, so syntax and implementation for other flavors of SQL will differ.

### The Example

It will be easier to explain the superpowers of SQL by putting it in action in an example. Below is a basic schema with 2 tables in MYSQL for a refund microservice:

![Image](https://cdn-media-1.freecodecamp.org/images/ri57whhXR9n9RTApP5SsN4vx-fPKYl-RBRYH)

There are 2 refunds and 7 related payments as example [data](http://sqlfiddle.com/#!9/b242d/5).

### Some assumptions

For the refund microservice example schema and applications, the following assumptions are made:

1. Refund microservice and data structure store the fk_item (the id of the ordered/delivered item), but it is not a hard foreign key.
2. Item can be refunded in either cash or credit for the amount paid for the same.
3. Items can be refunded many times as long as the remaining balance can cover the requested refund amount for each cash and credit. For example, let’s say the item was paid 50 in cash and 50 in credit. 2 refunds of 20 cash and 20 credit can be done. So after these transactions the balance will be 10 cash and 10 credit for that item (50–20–20).
4. Each refund can have multiple items for payment. Each payment can be of type either cash or credit.
5. All amounts are stored in cents so they are integers.

Now let’s use some SQL powers. You can find the example with the related queries running on this [SQL Fiddle](http://sqlfiddle.com/#!9/b242d/5).

### Do the math in SQL

As software engineers, let’s say if we need to find the total cash and credit amount refunded for an item, what would we do? We would run something like:

`SELECT fk_item, fk_refund, amount, is_cash FROM payment WHERE fk_item=2001;`

With the current data, it will give 3 rows like below:

![Image](https://cdn-media-1.freecodecamp.org/images/47KGYhwpcPnlyHSDJuZmZscjtnCYz8Qz9JfR)

With these 3 rows, we would loop over them. If it is cash, accumulate it to cashBalance variable, if not sum it up to creditBalace variable. But instead of that, it would be a lot easier (and probably faster) to do in SQL like this:

`SELECT fk_item, SUM(amount) AS total_paid, IF(is_cash = 1, 'cash', 'credit') as type FROM payment WHERE fk_item = 2001 GROUP BY fk_item, is_cash;`

Resulting in this:

![Image](https://cdn-media-1.freecodecamp.org/images/8S45Vi1zHw1k2zTRdKiryUwehMrUv5czFUiy)

The result is achieved easily now. If you need the total refund for the item, just change the GROUP BY to be on fk_item and it’s done. For 2 and 3 records it won’t feel significant. If there were say 20 refunds for that item, the first solution with a loop is writing more code with no gain. Like sum, other SQL functions can be used too. Simple math operations like [sum](https://www.w3schools.com/sql/func_mysql_sum.asp), multiply, [average](https://www.w3schools.com/sql/func_mysql_avg.asp) etc can be easy with SQL. This means no more loops.

### Use GROUP_CONCAT to fetch related 1:m relation values

[Group concat](http://www.mysqltutorial.org/mysql-group_concat/) is a robust operation in SQL databases. It is instrumental when you need to get data from a one to many relationship.

For instance, say you want to get all tags for a blog post or you want to get all categories of a product. Concerning this refund example, one item can be refunded multiple times. So we will get all the refunds associated with the item id. To get this we will run only 1 query and get it without any loops in the code, like below:

`SELECT fk_item, GROUP_CONCAT(DISTINCT fk_refund) refund_ids FROM payment WHERE fk_item = 2001;`

This results in:

![Image](https://cdn-media-1.freecodecamp.org/images/GWnoZNm5uqdxV6fLvd094ozvv8tGcw47vHNl)

Now we know that item 2001 has been refunded twice for 2 refunds. It will be easy to explode the refund Ids with `,` and proceed with any related operation. Be aware of that GROUP_CONCAT max length in MYSQL is 1024 characters.

### String manipulation

Many [string manipulation](https://dev.mysql.com/doc/refman/8.0/en/string-functions.html) tasks like substring, concatenation, change case, and string compare can be done in SQL. With this example, I am going to show the usage of `CONCAT_WS`. It is concat with a separator. It can also be used to select, for instance, a first_name and last_name with a space in between.

> _In the case of having an optional middle name, `COALESCE` can be used with `CONCAT_WS`. That is something for you to explore :)._

In this example, I will select refund_nr with its related reason:

`SELECT CONCAT_WS("-", refund_nr, reason) AS refund_nr_with_reason FROM refund;`

Resulting in:

![Image](https://cdn-media-1.freecodecamp.org/images/h8hVeGa8wznSHn5bRrAc9HorrwPFq7Ysowm8)

If this needs to be shown on the credit note document, for example, no extra code is needed to join the values again. SQL makes it one step easier again. Beware again that SQL is a case-insensitive language.

### Sorting with a custom formula

All software engineers know you can sort based on a column. But if you are given a custom priority formula to sort, what would you do? Probably again resort back to code and loop to sort. So let’s set the priority formula rules for above example:

1. Premium customer refunds get the highest priority (we hack it with a priority of 9999999999)
2. Other than premium customers, cash refunds get a priority of amount * 25, and for credit it is amount * 20.

As per the above rules, it is decided that premium customers and priority above 50000 (in cents) will be processed first. Then other refunds will be processed. Let’s get the priority refunds as below:

`SELECT r.refund_nr, r.reason, p.fk_item, p.amount, p.is_cash, IF(p.premium_customer = 1, 9999999999, p.amount * (IF(is_cash = 1, 25, 20))) AS priority FROM refund AS r INNER JOIN payment AS p ON r.id = p.fk_refund HAVING priority > 50000 ORDER BY priority D`ESC

The results are below:

![Image](https://cdn-media-1.freecodecamp.org/images/8JRjCiq9YxzYGrv81MxUzPeWBdrZ3prQ5OMp)

With the proper use of IF in SQL, sorting by a custom priority formula is a lot easier than trying to do it with loops in code. Notice that even smaller amounts like 7.5 (750 cents) and 9.0 (900 cents) came to the highest priority as these refund payment amounts were associated with premium customers.

> _Use the superpowers of SQL to make your life as a software engineer easier._

You can play with the example and run your queries on [SQL fiddle](http://sqlfiddle.com/#!9/b242d/5).

### Conclusion

There are other tricks of SQL that can help you as a software engineer. Like, `UPDATE` with `INSERT` using `ON DUPLICATE KEY UPDATE`. Whenever you have an itch for doing some manipulation on data pulled in from a database in code with loops, think again. Like any other language or tool, SQL is powerful but use it wisely. The main takeaway from this story is:

> _Exploit the power of SQL **optimally and wisely** to write less code because “the best code is the code that was never written”. If it is not written there is no need to maintain it._

_You can read more of my blog posts at [geshan.com.np](https://geshan.com.np/blog/2018/12/you-can-do-it-in-sql/)._

