---
title: How to Make a Database Read-Only in MySQL
subtitle: ''
author: Md. Fahim Bin Amin
co_authors: []
series: null
date: '2023-06-22T22:49:49.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-a-database-read-only-in-mysql
coverImage: https://www.freecodecamp.org/news/content/images/2023/06/altumcode-dMUt0X3f59Q-unsplash.jpg
tags:
- name: database
  slug: database
- name: MySQL
  slug: mysql
- name: SQL
  slug: sql
seo_title: null
seo_desc: "If you are learning MySQL, then you are likely enjoying executing different\
  \ commands and checking the results afterward. \nBut you may be working on a project\
  \ where you have modified your database to an acceptable state and you're worried\
  \ about alteri..."
---

If you are learning MySQL, then you are likely enjoying executing different commands and checking the results afterward. 

But you may be working on a project where you have modified your database to an acceptable state and you're worried about altering it by mistake. This could happen when you're working in the DB, or when others who have access to your computer get in there.

Well, fear not! In MySQL, you can restrict the database to ensure its safety. I assume you're a SQL beginner, so I am not going to bore you with the difficult stuff. The easiest thing is to make the database **READ ONLY**. After that, no one can modify the database in any way if they aren't familiar with certain MySQL commands.

### If you'd like to go through the process step-by-step in a video, here you go:

%[https://youtu.be/7kFzNo6tD-k]

## How to Make a Database READ ONLY

Let's assume that you're already in your SQL editor (from where you can execute your MySQL commands). Keep in mind that usually, when we create a database, it comes with read-write accessibility by default. 

So for now, let's assume that the default status of a newly created database is READ-WRITE enabled. 

To convert the database into a READ-ONLY state, use this command:

```sql
ALTER DATABASE database_name READ ONLY = 1;
```

Let me explain each part of the code for you now.

As you want to change something in the data, you are telling the database,   
"hey, I want to alter something". So you used the `ALTER` command. 

Then comes the part where you tell it which thing you want to alter, because there might be multiple tables or databases. So you need to tell it which thing you want to alter. So, you stated `DATABASE` to specify that you actually want to alter a database.

In your client (MySQL Workbench/XAMPP, and so on), there might be multiple databases. So wouldn't MySQL get confused about exactly which database you want to alter? You don't want to confuse it, right? This is why you need to specify the database name. 

After that, you tell it exactly which modification you want it to make. You want to change the `READ ONLY` status to `1`. This means that **READ ONLY** is on/enabled.

After this, nobody will be able to make any kind of alteration or changes (update/delete/addition) to that specific READ ONLY database anymore. Nobody will even be able to delete the database!

## How to Make a Database READ-WRITE

What if you need to revert the changes so you can make updates to the database? You need to change the **READ ONLY** status to 0 to state that you want the **READ ONLY** status to be disabled (or no in short).

Simply use the following command to do that:

```sql
ALTER DATABASE database_name READ ONLY = 0;
```

After this, anyone will be able to make changes to the database or even delete the database if they want.

## Conclusion

Isn't it a short but beautiful trick? Enjoy your coding journey!

Also, if you like programming-related content, then make sure to [subscribe to my YouTube channel](https://www.youtube.com/@FahimAmin?sub_confirmation=1) where I publish programming-related content regularly!

Also, you can follow me on [GitHub](https://github.com/FahimFBA) and [Twitter](https://twitter.com/Fahim_FBA). You can also check my website: [https://fahimbinamin.com/](https://fahimbinamin.com/)

If you want to endorse me for relevant skills, then do that using [LinkedIn](https://www.linkedin.com/in/fahimfba/).

Cover image: Photo by [AltumCode](https://unsplash.com/@altumcode?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/photos/dMUt0X3f59Q?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)


