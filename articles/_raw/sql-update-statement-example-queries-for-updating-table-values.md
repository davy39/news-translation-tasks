---
title: SQL Update Statement — Example Queries for Updating Table Values
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-04-26T16:20:52.000Z'
originalURL: https://freecodecamp.org/news/sql-update-statement-example-queries-for-updating-table-values
coverImage: https://www.freecodecamp.org/news/content/images/2020/04/markus-winkler-cxoR55-bels-unsplash.jpg
tags:
- name: SQL
  slug: sql
seo_title: null
seo_desc: 'By Jonathan Sexton

  SQL (pronounced Seequel) stands for Structured Query Language. It is a strongly
  typed, static (types are checked before runtime) querying language that first appeared
  in 1974 (woah, 46 years old!), but was not initially released un...'
---

By Jonathan Sexton

SQL (pronounced Seequel) stands for Structured Query Language. It is a [strongly typed](https://en.wikipedia.org/wiki/Strong_and_weak_typing), static (types are checked before runtime) querying language that first appeared in 1974 (woah, 46 years old!), but was not initially released until 1986.  

You might be thinking to yourself that such an "old" tool has its best days behind it, but you'd be far from correct. In 2019, through the Scale Grid [DeveloperWeek survey](https://scalegrid.io/blog/2019-database-trends-sql-vs-nosql-top-databases-single-vs-multiple-database-use/), SQL was used by 60.5% of respondents, while [NoSQL](https://en.wikipedia.org/wiki/NoSQL) was used by only 39.5 % of respondents.

To be clear, the SQL category was broken down into several subcategories that included [MySQL](https://en.wikipedia.org/wiki/MySQL), [PostgreSQL](https://en.wikipedia.org/wiki/PostgreSQL), [SQL Server](https://en.wikipedia.org/wiki/Microsoft_SQL_Server), and so on, while the NoSQL category was broken apart into subcategories that contained [MongoDB](https://en.wikipedia.org/wiki/MongoDB), [Cassandra](https://en.wikipedia.org/wiki/Apache_Cassandra), etc.

Even in 2017, according to the [Stack Overflow Developer's Survey](https://insights.stackoverflow.com/survey/2017), the second most popular language used was SQL (right behind JavaScript) with 50% of the 64,000 respondents saying they still use SQL in some form.

It's popularity is due, at least in part, to the simplicity of the language, the fact that it was built with relational data in mind, and because it's proven itself as reliable for searching, joining, and filtering data.

Suffice it to say, SQL is not only alive and kicking, but thriving among today's development community.

Now let's see why!

<h2>The Fun Parts</h2>	

SQL Server is the preferred flavor of SQL that I use in my day to day activities at work, so the examples below will conform to those standards.  

One thing I find myself doing a great deal of is updating multiple records within a table. Now I could do this one record at a time but SQL gives us the ability to update multiple (thousands upon thousands if need be) records at once through the `UPDATE` statement.

The `UPDATE` statement can be used to update a single column, a larger set of records (through the use of conditions), and/or the entire table in a database. The condition(s) can be a boolean, a string check, or mathematical sequence that resolves to a boolean (greater than, less than, etc.).

While it may vary slightly from flavor to flavor, the general syntax is as follows:

<code><strong>UPDATE</strong> <em>table-name</em><br />
<strong>SET</strong> <em>column-name = value[, column-name=value]</em><br />
[<strong>WHERE</strong> <em>condition</em>]</code>

The brackets ( [] ) above denote optional additions to the query.  

**<ins>***It is very important to note that without a `WHERE` condition, ALL records in the table will be updated as soon as you execute the query.***</ins>**

<h2 id="simple_query">Example Queries</h2>

As our dataset, I'll be using this table named _**Work_Tickets**_:

<table>
        <th>
          <tr>
            <td><strong>SalesOrderNum</strong></td>
            <td><strong>WorkTicketNum</strong></td>
            <td><strong>Customer_Code</strong></td>
              <td><strong>Customer_Contact</strong></td>
            <td><strong>UnitCost</strong></td>
            <td><strong>Billed</strong></td>
            <td><strong>ParentLineKey</strong></td>
            <td><strong>Qty_Ordered</strong></td>
            <td><strong>Qty_Shipped</strong></td>
          </tr>
        </th>
        <tbody>
          <tr>
            <td>00061356</td>
            <td>000931</td>
            <td>1250</td> 
              <td>sales@wayneindustries.com</td>
            <td>0.00</td>
            <td>False</td>
            <td>079777</td>
            <td>12.0</td>
            <td>0</td>
          </tr>
          <tr>
            <td>00061357</td>
            <td>000932</td>
              <td>1251</td>  
              <td>contact@starkindustries.com</td>
            <td>0.00</td>
            <td>False</td>
            <td>085695</td>
            <td>196.5</td>
            <td>0</td>
          </tr>
          <tr>
            <td>00061358</td>
            <td>000933</td>
              <td>1252</td>
              <td>animation@acmetoons.com</td>
            <td>0.00</td>
            <td>False</td>
            <td>085569</td>
            <td>17.5</td>
            <td>0</td>
          </tr>
        </tbody>
      </table>

<h4>Simple Query Without Conditions</h4>

Here is a very simple update query that will change all of the `UnitCost` fields to the number `131.6152`:

`UPDATE Work_Tickets`   
`SET UnitCost = 131.6152`   


Note there is no `WHERE` clause, so every line in the table will be updated and our dataset will now look like this:

    <table>
        <th>
          <tr>
            <td><strong>SalesOrderNum</strong></td>
            <td><strong>WorkTicketNum</strong></td>
              <td><strong>Customer_Code</strong></td>
              <td><strong>Customer_Contact</strong></td>
            <td><strong>UnitCost</strong></td>
            <td><strong>Billed</strong></td>
            <td><strong>ParentLineKey</strong></td>
            <td><strong>Qty_Ordered</strong></td>
            <td><strong>Qty_Shipped</strong></td>
          </tr>
        </th>
        <tbody>
          <tr>
            <td>00061356</td>
            <td>000931</td>
              <td>1250</td>
              <td>sales@wayneindustires.com</td>
            <td>131.6152</td>
            <td>False</td>
            <td>079777</td>
            <td>12.0</td>
            <td>0</td>
          </tr>
          <tr>
            <td>00061357</td>
            <td>000932</td>
              <td>1251</td>
              <td>contact@starkindustries.com</td>
            <td>131.6152</td>
            <td>False</td>
            <td>085695</td>
            <td>196.5</td>
            <td>0</td>
          </tr>
          <tr>
            <td>00061358</td>
            <td>000933</td>
              <td>1252</td>
              <td>animation@acmetoons.com</td>
            <td>131.6152</td>
            <td>False</td>
            <td>085569</td>
            <td>17.5</td>
            <td>0</td>
          </tr>
        </tbody>
      </table>

<h4 id="simple_query_condition">Simple Queries With Condition(s)</h4>

Here is a simple query with one condition statement:

<code>UPDATE Work_Tickets<br />SET Billed = true<br />WHERE UnitCost <> 0.00</code>


This query will update the `Billed` field to be _true_ on every line that matches the condition of the `UnitCost` not equaling 0. After we run our query, the dataset will look like this:

   <table>
        <th>
          <tr>
            <td><strong>SalesOrderNum</strong></td>
            <td><strong>WorkTicketNum</strong></td>
              <td><strong>Customer_Code</strong></td>
              <td><strong>Customer_Contact</strong></td>
            <td><strong>UnitCost</strong></td>
            <td><strong>Billed</strong></td>
            <td><strong>ParentLineKey</strong></td>
            <td><strong>Qty_Ordered</strong></td>
            <td><strong>Qty_Shipped</strong></td>
          </tr>
        </th>
        <tbody>
          <tr>
            <td>00061356</td>
            <td>000931</td>
              <td>1250</td>
              <td>sales@wayneindustires.com</td>
            <td>131.6152</td>
            <td>True</td>
            <td>079777</td>
            <td>12.0</td>
            <td>0</td>
          </tr>
          <tr>
            <td>00061357</td>
            <td>000932</td>
              <td>1251</td>
              <td>contact@starkindustries.com</td>
            <td>131.6152</td>
            <td>True</td>
            <td>085695</td>
            <td>196.5</td>
            <td>0</td>
          </tr>
          <tr>
            <td>00061358</td>
            <td>000933</td>
              <td>1252</td>
              <td>animation@acmetoons.com</td>
            <td>131.6152</td>
            <td>True</td>
            <td>085569</td>
            <td>17.5</td>
            <td>0</td>
          </tr>
        </tbody>
      </table>

Below is a query where we change the `ParentLineKey` to the string `000134` where the `SalesOrderNum` and the `WorkTicketNum` both match the given strings.

<code>UPDATE Work_Tickets <br />SET ParentLineKey = 000134 <br />WHERE SalesOrderNum = 00061358 and WorkTicketNumber = 000933</code>

So, the 085569 in the `ParentLineKey` field will be replaced with `000134` and our dataset now looks like this:

   <table>
        <th>
          <tr>
            <td><strong>SalesOrderNum</strong></td>
            <td><strong>WorkTicketNum</strong></td>
              <td><strong>Customer_Code</strong></td>
              <td><strong>Customer_Contact</strong></td>
            <td><strong>UnitCost</strong></td>
            <td><strong>Billed</strong></td>
            <td><strong>ParentLineKey</strong></td>
            <td><strong>Qty_Ordered</strong></td>
            <td><strong>Qty_Shipped</strong></td>
          </tr>
        </th>
        <tbody>
          <tr>
            <td>00061356</td>
            <td>000931</td>
              <td>1250</td>
            <td>sales@wayneindustires.com</td>
            <td>131.6152</td>
            <td>True</td>
            <td>079777</td>
            <td>12.0</td>
            <td>0</td>
          </tr>
          <tr>
            <td>00061357</td>
            <td>000932</td>
              <td>1251</td>
              <td>contact@starkindustries.com</td>
            <td>131.6152</td>
            <td>True</td>
            <td>085695</td>
            <td>196.5</td>
            <td>0</td>
          </tr>
          <tr>
            <td>00061358</td>
            <td>000933</td>
              <td>1252</td>
              <td>animation@acmetoons.com</td>
            <td>131.6152</td>
            <td>True</td>
            <td>000134</td>
            <td>17.5</td>
            <td>0</td>
          </tr>
        </tbody>
      </table>

<h4>Updating Multiple Fields</h4>

Let's say you have a much larger dataset than the one we are currently using and you have several fields to update.  

It would be tedious and mind-numbing to update them with different update statements. Luckily for us it's also possible to update several fields at once with an update statement, as long as we separate the column names with a comma: 

<code>UPDATE Work_Tickets <br />SET UnitCost = 129.8511, Qty_Ordered = 72, Qty_Shipped = 72 <br />WHERE SalesOrderNum = 00061358</code>

And here is the result with the updated fields after running the query:

   <table>
        <th>
          <tr>
            <td><strong>SalesOrderNum</strong></td>
            <td><strong>WorkTicketNum</strong></td>
              <td><strong>Customer_Code</strong></td>
              <td><strong>Customer_Contact</strong></td>
            <td><strong>UnitCost</strong></td>
            <td><strong>Billed</strong></td>
            <td><strong>ParentLineKey</strong></td>
            <td><strong>Qty_Ordered</strong></td>
            <td><strong>Qty_Shipped</strong></td>
          </tr>
        </th>
        <tbody>
          <tr>
            <td>00061356</td>
            <td>000931</td>
              <td>1250</td>
              <td>sales@wayneindustires.com</td>
            <td>131.6152</td>
            <td>True</td>
            <td>079777</td>
            <td>12.0</td>
            <td>0</td>
          </tr>
          <tr>
            <td>00061357</td>
            <td>000932</td>
              <td>1251</td>
              <td>contact@starkindustries.com</td>
            <td>131.6152</td>
            <td>True</td>
            <td>085695</td>
            <td>196.5</td>
            <td>0</td>
          </tr>
          <tr>
            <td>00061358</td>
            <td>000933</td>
              <td>1252</td>
              <td>animation@acmetoons.com</td>
            <td>129.8511</td>
            <td>True</td>
            <td>000134</td>
            <td>72</td>
            <td>72</td>
          </tr>
        </tbody>
      </table>

<h4>Using Update in a Subquery</h4>

The above examples are perfect if you are working with one data source. However, most of your data will not be stored in a single table. That's where using _UPDATE_ with multiple data sources comes in handy.

The syntax for updating a column/table changes a little if we want to bring in data from another table:

<code><strong>UPDATE</strong> <em>table-name</em><br />
<strong>SET</strong> <em>column-name = (SELECT column name(s) <br />  FROM table2-name<br />  WHERE condition(s))</em><br />
[<strong>WHERE</strong> <em>condition</em>]</code>

And here are the two tables we'll be using for this query - the **_Work_Tickets table:_**

   <table>
        <th>
          <tr>
            <td><strong>SalesOrderNum</strong></td>
            <td><strong>WorkTicketNum</strong></td>
              <td><strong>Customer_Code</strong></td>
              <td><strong>Customer_Contact</strong></td>
            <td><strong>UnitCost</strong></td>
            <td><strong>Billed</strong></td>
            <td><strong>ParentLineKey</strong></td>
            <td><strong>Qty_Ordered</strong></td>
            <td><strong>Qty_Shipped</strong></td>
          </tr>
        </th>
        <tbody>
          <tr>
            <td>00061356</td>
            <td>000931</td>
              <td>1250</td>
              <td>sales@wayneindustires.com</td>
            <td>131.6152</td>
            <td>True</td>
            <td>079777</td>
            <td>12.0</td>
            <td>0</td>
          </tr>
          <tr>
            <td>00061357</td>
            <td>000932</td>
              <td>1251</td>
              <td>contact@starkindustries.com</td>
            <td>131.6152</td>
            <td>True</td>
            <td>085695</td>
            <td>196.5</td>
            <td>0</td>
          </tr>
          <tr>
            <td>00061358</td>
            <td>000933</td>
              <td>1252</td>
              <td>animation@acmetoons.com</td>
            <td>129.8511</td>
            <td>True</td>
            <td>000134</td>
            <td>72</td>
            <td>72</td>
          </tr>
        </tbody>
      </table>

and the **_Customer_Info table :_**

<table>
        <th>
          <tr>
            <td><strong>Name</strong></td>
            <td><strong>Industry</strong></td>
            <td><strong>Code</strong></td>
            <td><strong>Address</strong></td>
              <td><strong>City</strong></td>
            <td><strong>Discount</strong></td>
            <td><strong>PhoneNumber</strong></td>
            <td><strong>Email</strong></td>
          </tr>
        </th>
        <tbody>
          <tr>
            <td>Wayne Enterprises</td>
            <td>Defense,weaponry,aerospace,enginerring</td>
            <td>NULL</td>
            <td>1631 Dark Knight Way</td>
            <td>Gotham</td>
            <td>19.75</td>
            <td>5556614000</td>
              <td>sales@wayneindustires.com</td>
          </tr>
          <tr>
            <td>Stark Industries</td>
            <td>Defense,weaponry,protection</td>
              <td>1251</td>
            <td>5641 Iron Dr</td>
            <td>Undisclosed</td>
            <td>19.73</td>
            <td>9993126156</td>
            <td>contact@starkindustries.com</td>
          </tr>
          <tr>
            <td>Acme Corp</td>
            <td>Comedy,laughter,animation</td>
            <td>1252</td>
            <td>24569 Smiling St</td>
            <td>Toon Town</td>
            <td>17.53</td>
            <td>3216549877</td>
              <td>animation@acmetoons.com
          </tr>
        </tbody>
      </table>

The `UPDATE` statement with a [subquery](https://docs.microsoft.com/en-us/sql/relational-databases/performance/subqueries?view=sql-server-ver15) looks like this:

<code>UPDATE Customer_Info<br />SET Code = (SELECT Customer_Code<br />  FROM Work_Tickets<br />  WHERE Work_Tickets.Customer_Contact = Customer_Info.Email)  <br />FROM Work_Tickets<br />WHERE Code IS NULL</code>

This example will update the _Code_ field on the _Customer_Info_ table where the email address match from both tables. And this is what our _Customer_Info_ table looks like now:

<table>
        <th>
          <tr>
            <td><strong>Name</strong></td>
            <td><strong>Industry</strong></td>
            <td><strong>Code</strong></td>
            <td><strong>Address</strong></td>
              <td><strong>City</strong></td>
            <td><strong>Discount</strong></td>
            <td><strong>PhoneNumber</strong></td>
            <td><strong>Email</strong></td>
          </tr>
        </th>
        <tbody>
          <tr>
            <td>Wayne Enterprises</td>
            <td>Defense,weaponry,aerospace,enginerring</td>
            <td>1250</td>
            <td>1631 Dark Knight Way</td>
            <td>Gotham</td>
            <td>19.75</td>
            <td>5556614000</td>
              <td>sales@wayneindustires.com</td>
          </tr>
          <tr>
            <td>Stark Industries</td>
            <td>Defense,weaponry,protection</td>
              <td>1251</td>
            <td>5641 Iron Dr</td>
            <td>Undisclosed</td>
            <td>19.73</td>
            <td>9993126156</td>
            <td>contact@starkindustries.com</td>
          </tr>
          <tr>
            <td>Acme Corp</td>
            <td>Comedy,laughter,animation</td>
            <td>1252</td>
            <td>24569 Smiling St</td>
            <td>Toon Town</td>
            <td>17.53</td>
            <td>3216549877</td>
              <td>animation@acmetoons.com
          </tr>
        </tbody>
      </table>

## Wrapping up

I hope this article has been helpful to you in understanding how the _UPDATE_ statement works in SQL.

You're now ready to write your own SQL _UPDATE_ statements like a champ! After you do, I'd love for you to share them with me on social media!

Don't forget to check out my [blog](https://jonathansexton.me/blog) where I frequently post articles about web development.

While you're there why not sign up for my newsletter? You can do that at the top right of the main blog page. I like to send out interesting articles (mine and others), resources, and tools for  developers every now and then.

If you have questions about this article or just in general my DMs are open – come say hi on [Twitter](https://twitter.com/jj_goose) or any of my other social media accounts which you can find below the newsletter sign up on the main page of my blog or on my profile here at fCC :)

Have an awesome day and happy coding, friend!

