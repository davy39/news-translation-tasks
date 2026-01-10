---
title: SQL Delete Row Statement - How to Remove Data From a Table With Example Queries
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-12-07T18:11:32.000Z'
originalURL: https://freecodecamp.org/news/sql-delete-row-statement-examples
coverImage: https://www.freecodecamp.org/news/content/images/2020/11/u-j-e-s-h-7ySd00IGyx4-unsplash.jpg
tags:
- name: database
  slug: database
- name: SQL
  slug: sql
seo_title: null
seo_desc: "By Jonathan Sexton\nI make no qualms about how much I enjoy working with\
  \ SQL both in my professional and personal projects. \nIts straightforwardness and\
  \ simplicity appeal to my desire to have well-defined boundaries in terms of what\
  \ the language will ..."
---

By Jonathan Sexton

I make no qualms about how much I enjoy working with SQL both in my professional and personal projects. 

Its straightforwardness and simplicity appeal to my desire to have well-defined boundaries in terms of what the language will and will not let me "get away with" regarding syntax.  

SQL is structured with a clear and concise manner of operation in which the user's input dictates the data returned. Hence my comment about having well-defined boundaries on syntax.

While I celebrate its resiliency (SQL was created in 1974 with an initial release of 1986) within the development community, I also know that when working with data it can feel like even the fundamentals are stressful and frightening.

I'm here to (hopefully) shed some light on one of those fundamentals of working with data: deleting an entire row of data. 

Although we're not going to go over the process for [establishing a table in SQL](https://www.freecodecamp.org/news/sql-create-table-statement-with-example-syntax/) or [populating that table with data/updating that data](https://www.freecodecamp.org/news/sql-update-statement-example-queries-for-updating-table-values/), I've linked those other articles in case you'd like to learn more or just need a refresher.

Alright, now the fun part - let's start deleting data from a table!

## SQL Delete Row Overview

Here is the table, aptly named _Cute_Doggos_, that we'll be using as our example to start removing data from:

 <table>
            <th>
              <tr style="font-weight: bold">
                <td>Name</td>
                <td>Color</td>
                <td>Breed</td>
                <td>Age</td>
                <td>Weight</td>
                <td>Height</td>
                <td>Fav_Food</td>
                <td>Fav_Toy</td>
                <td>Dislikes</td>
                <td>Allergies</td>
              </tr>
            </th>
            <tbody>
              <tr>
                <td>daisy</td>
                <td>red</td>
                <td>standard dachshund</td>
                <td>1 yr</td>
                <td>14</td>
                <td>6</td>
                <td>salmon flavored kibble</td>
                <td>squeeky ball</td>
                <td>birds flying over the yard</td>
                <td>cats, baths, cleanliness</td>
              </tr>
                <tr style="background-color: lightgrey">
                <td>winston</td>
                <td>black/tan</td>
                <td>rottweiler</td>
                <td>3 yrs</td>
                <td>41</td>
                <td>17</td>
                <td>literally anything</td>
                <td>rope tug</td>
                <td>staying off the couch</td>
                <td>listening, behaving, not slobbering on everything</td>
              </tr>
              <tr>
                <td>sammie</td>
                <td>light honey</td>
                <td>golden retriever</td>
                <td>9 yrs</td>
                <td>46</td>
                <td>19</td>
                <td>beef flavored kibble</td>
                <td>her bed</td>
                <td>rambutcious puppies</td>
                <td>none known</td>
              </tr>
              <tr style="background-color: lightgrey">
                <td>penelope</td>
                <td>gray and white</td>
                <td>husky</td>
                <td>9 months</td>
                <td>16</td>
                <td>12</td>
                <td>old shoes</td>
                <td>outside</td>
                <td>kennel</td>
                <td>none known</td>
              </tr>
            </tbody>
 </table>

As you may have guessed, this is fictitious data from a table I've concocted out of thin air :)  However, I hope it illustrates the data well enough for our purposes.

As with most aspects of technical nature, it never hurts to check the official documentation as well. If you wish to do that, Microsoft has some great in-depth [information on the SQL Delete statement](https://docs.microsoft.com/en-us/sql/t-sql/statements/delete-transact-sql?view=sql-server-ver15).

Onto the core of this article - deleting data.  The action is as simple as the name itself and here is the base syntax:

<code>DELETE FROM <em>name_of_table</em></code>

### ***With this syntax you will delete all rows of data within the entire table.*** 



So for our example table above, the query would look like the following:

<code>DELETE FROM Cute_Doggos</code>

That may be your intended purpose and the longer you write SQL the more cases you'll find to use the delete statement in this capacity. 

I have used this statement many times to clear a table after it was filled with test data. This approach allows us to keep the column names, data types, indexes, and overall table structure in tact without deleting the actual table.

_As a side note, if your intended purpose is to delete all of the rows within a table, the faster approach would be to use the [TRUNCATE TABLE](https://docs.microsoft.com/en-us/sql/t-sql/statements/truncate-table-transact-sql?view=sql-server-ver15) statement as it uses far fewer system resources._

## Example Delete Queries

The vast majority of the time when you use the delete functionality you'll want to be a bit more targeted with your approach. For that, we'll add a condition and the syntax will look like so:

<code>DELETE FROM <em>name_of_table</em> WHERE <em>conditions_exist</em></code>

Using our table above of dogs, our query would look like this:

<code>DELETE FROM Cute_Doggos WHERE dbo.Cute_Doggos.Height > 18</code>

This would remove all entries from our table that match our condition of the _Height being greater than 18_. And if you're using Microsoft SQL Server Manager, you'll get a return statement like so: 

<code>(1 row affected)</code>

If you'd like to see the rows of data that were deleted (for logging purposes, visual indications to users, and so on), we can use the OUTPUT statement to do just that.

Our table would now look like this:

 <table>
            <th>
              <tr style="font-weight: bold">
                <td>Name</td>
                <td>Color</td>
                <td>Breed</td>
                <td>Age</td>
                <td>Weight</td>
                <td>Height</td>
                <td>Fav_Food</td>
                <td>Fav_Toy</td>
                <td>Dislikes</td>
                <td>Allergies</td>
              </tr>
            </th>
            <tbody>
              <tr>
                <td>daisy</td>
                <td>red</td>
                <td>standard dachshund</td>
                <td>1 yr</td>
                <td>14</td>
                <td>6</td>
                <td>salmon flavored kibble</td>
                <td>squeeky ball</td>
                <td>birds flying over the yard</td>
                <td>cats, baths, cleanliness</td>
              </tr>
                <tr style="background-color: lightgrey">
                <td>winston</td>
                <td>black/tan</td>
                <td>rottweiler</td>
                <td>3 yrs</td>
                <td>41</td>
                <td>17</td>
                <td>literally anything</td>
                <td>rope tug</td>
                <td>staying off the couch</td>
                <td>listening, behaving, not slobbering on everything</td>
              </tr>
              <tr>
                <td>penelope</td>
                <td>gray and white</td>
                <td>husky</td>
                <td>9 months</td>
                <td>16</td>
                <td>12</td>
                <td>old shoes</td>
                <td>outside</td>
                <td>kennel</td>
                <td>none known</td>
              </tr>
            </tbody>
 </table>



The condition we set is wholly our choice, and if that's too narrow for your needs there are other options.

Let's say you don't care about the specific records you remove, only that you need to remove a certain number of records in the table.

<code>DELETE TOP 2 FROM Cute_Doggos</code>

You might be thinking that this query would remove the very first two records in your table – and you're not too far off. The only problem is because SQL stores records in a random order, this syntax will remove 2 **<ins>RANDOM</ins>** records from the table.

If you're looking to remove a percentage of the records, SQL can do that as well:

<code>DELETE TOP 25 PERCENT FROM Cute_Doggos</code>

Again, this query will delete **<ins>RANDOM</ins>** records. In our example, since we have 4 records, this query would delete 1 random record (4 * 0.25 = 1).

As a final side note, when using the TOP keyword, we cannot use an [ORDER BY](https://docs.microsoft.com/en-us/sql/t-sql/queries/select-order-by-clause-transact-sql?view=sql-server-ver15) clause because of the randomness of record storage.

## Wrapping up

Now that you've seen the DELETE statement in action, you're ready to go out into the wild and cull all of the data from all of the tables! Maybe don't do this as it will make for a long weekend of restoring off of backups :)

At any rate, now you're ready to start putting it to good use.

If you found this article helpful check out my [blog](https://jonathansexton.me/blog) (I'm currently rebuilding it in Gatsby/WordPress so stay tuned for an article about that) where I frequently post articles about web development, life, and learning.

While you're there why not sign up for my newsletter? You can do that at the top right of the main blog page. I like to send out interesting articles (mine and others), resources, and tools for developers every now and then.

If you have questions about this article or just in general let me know – come say hi on [Twitter](https://twitter.com/jj_goose) or any of my other social media accounts which you can find below the newsletter sign up on the main page of my blog or on my profile here at freeCodeCamp :)

Have an awesome day! Happy learning and happy coding, friend.

