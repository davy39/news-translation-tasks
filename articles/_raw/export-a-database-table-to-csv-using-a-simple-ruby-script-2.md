---
title: How to Export a Database Table to CSV Using a Simple Ruby Script
subtitle: ''
author: Fatos Morina
co_authors: []
series: null
date: '2019-08-19T05:28:00.000Z'
originalURL: https://freecodecamp.org/news/export-a-database-table-to-csv-using-a-simple-ruby-script-2
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca0cc740569d1a4ca4ada.jpg
tags:
- name: Ruby
  slug: ruby
seo_title: null
seo_desc: If you have a Rails project and want to export a table as a CSV, without
  having to go to all the trouble of finding a gem, installing and using it, then
  uninstalling it when it’s no longer needed, I have some good news. Here’s an easy
  and quick way t...
---

If you have a Rails project and want to export a table as a CSV, without having to go to all the trouble of finding a gem, installing and using it, then uninstalling it when it’s no longer needed, I have some good news. Here’s an easy and quick way to export a particular table from your database as a CSV file.

This is the [code](https://gist.github.com/foxumon/fdb30349545944eee58c7858e6bab23c) that you need to run. You can put it as a rake task and run it, or run it another way.

As you can see, first we import `CSV`— we need it to do the writing of the CSV file with the data from the database. We then choose the location and the name for the file that we want to export it to, which in our case will be a file called *data.csv* included under repository *public*.

Then we set the table that we want to export and start writing. We could also change the attributes that we want to export — we don’t have to include them all as they are in the database.

That’s it! It’s that simple and yet very helpful.

*This article was originally published on* [*Medium*](https://medium.com/better-programming/export-a-database-table-to-csv-using-a-simple-ruby-script-5577a0914eb0?source=friends_link&sk=6debc0a92a8679247534b2e60a42f516)
