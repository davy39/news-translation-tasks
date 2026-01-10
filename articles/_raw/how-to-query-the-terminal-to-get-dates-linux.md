---
title: Linux Date Command – How to Query the Terminal to Get Dates
subtitle: ''
author: Arunachalam B
co_authors: []
series: null
date: '2022-11-19T19:06:26.000Z'
originalURL: https://freecodecamp.org/news/how-to-query-the-terminal-to-get-dates-linux
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/10.-Date-Command---Brief-1.png
tags:
- name: Linux
  slug: linux
- name: terminal
  slug: terminal
seo_title: null
seo_desc: "Linux has many utility tools that help you quickly find the answer to your\
  \ questions. But many devs aren't aware of them.\nIn this article, you will learn\
  \ a command that has exceptional benefits. \nFor example, say you want to take a\
  \ look at your calen..."
---

Linux has many utility tools that help you quickly find the answer to your questions. But many devs aren't aware of them.

In this article, you will learn a command that has exceptional benefits. 

For example, say you want to take a look at your calendar to plan a vacation. What are a few ways you can open the calendar? Well, there's Google/Outlook, your system desktop calendar, your mobile phone calendar, and more.

But did you know that you can get a calendar just by typing three letters? In this article, I'll teach you this helpful three-letter command and share some fun experiences of using `date` with my team. 

## How to Query Your Terminal for the Date

I remember I was busy working one day. I asked one of my colleagues sitting next to me, "Do you know the date of next week Friday?" Then I realized that he was wearing headphones and appeared to be deeply concentrating on his code. 

I didn't want to disturb him further, and I was about to ask my other colleague sitting right opposite me. 

"November 25", the colleague whom I thought couldn't hear me replied. 

I was amazed – how'd he know that fast? 

"Oh, man! I thought you were coding. How did you get the date?" I asked him, surprised. 

"I was querying the terminal to find the answer to the question you asked me", he replied, showing his terminal window. 

The terminal window had the following command:

```bash
dd "next week Friday"
```

I didn't understand what he'd done, so I as. 

"Well, Linux by default supports the date command to display today's date and to set the current date and time in our system. It also provides a way to find a date in the future and past as simply as we speak. `date` is the command to do all stuff related to date and time", he replied. 

I was more confused about the `dd` command and I asked him to clarify how it worked.

"But if `date` is the command, what's `dd`? Is that part of the `date` command?" 

He explained that `dd` is not associated with the `date` command. Rather, it was just a shortcut command (I'll be writing about this in my future tutorials) that he created. `dd` abbreviates to `date --date="<given_date>"`.

So, the actual command is this:

```bash
date --date="next week Friday"
```

I ran the same in my terminal and was amazed to see the output. 

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-69.png)
_Linux terminal command to find the date of the given day_

This was cool and I thanked him for his super helpful explanation. On further research, I found that this command was able to answer most of my queries. I felt like I was interacting with an AI system. 

I'm posting a few of my queries here:

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screenshot-from-2022-11-15-00-05-25.png)
_Query terminal for a future or past date_

## How to Get Specific Info About a Date in Linux

Up until now, we have been trying to find a particular day with our query. But, what if you want to find some info about a date? After a bit more research, I found that you can find the day of the week of a date using the same command. 

The following command displays the day of the week of August 1, 2015:

```bash
date --date="2015-08-01"
date --date="08/01/2015"
```

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-82.png)
_Terminal command to find the day of a date_

## How to Find Information About a List of Dates in Linux

My coworker had a list of dates. He needed a script that displayed each date with the day. He'd gotten stuck trying to figure it out, and asked for my help. 

He was clear on his problem. But he has gone wrong with the steps he took to achieve it. On further discussion, I found that he searched the following items sequentially in Google.

* How to open a file in read mode?
* How to read line by line? 
* How to parse the date in the file? 
* Finally, How to find the day of that date? 

In the middle of this discussion, I remembered that you can do this quickly with the super powerful `date` command. The fact is that the `date` command does all the above actions – our job is just to give the path of the file. 

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-83.png)
_Terminal command to parse dates from a file_

The fact that it can read and parse the date given in any format is an added advantage. From the above screenshot, you will be able to understand how simple it is to solve my coworker's problem. 

Remembering the quote from [Unfiltered: No Shame, No Regrets, Just Me](https://www.goodreads.com/work/quotes/53327688) by Lily Collins

> Asking for help is never a sign of weakness. It's one of the bravest things you can do. And it can save your life.

## How the Date Command Works with File Operations

If you've read my [previous tutorial on getting started with Linux](https://www.freecodecamp.org/news/how-to-learn-linux-terminal-as-a-beginner/), you may remember that with the `stat` command we can get some info about the file such as its size, date created, last date modified, and so on. 

Well, did you know you can find the last modified time of a file using the `date` command? 

Yes – by adding the `-r` flag with the `date` command and the file path, you can find the last modified time of the file. It looks like this:

```bash
date -r install_git.sh
```

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-84.png)
_Terminal command showing the last modified time of a file_

There is another place where this date command might be more familiar. You use it to create a file with a timestamp. For example, system administrators often use it to see system and server logs. I've also heard that people in stock trading also rely on creating files with timestamps. 

Here's a quick example of creating a file with date and time:

```bash
vi file-$(date "+%Y-%m-%d_%I:%M:%S").txt
```

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-85.png)
_Terminal command to create a file with date and time_

For first time users, it might be tough to understand the above command. 

Let's break this command down to understand it better:

* `vi` is my text editor
* `file-$(date "+%Y-%m-%d_%I:%M:%S").txt` is the name of the file

Let's bisect the `date` command in the file name further:

* `date "<some_format>"` prints the date in the specified format
* `%Y` is the current year
* `%m` is the current month
* `%d` is today's date
* `%I` is hours
* `%M` is minutes
* `%S` is seconds

## How to Find the Date and Time in a Different Time Zone

One of my other team members raised this interesting question. 

It's possible to find the date and time in another time zone with the `date` command. But, it's not so user-friendly. You need to remember the full name of the timezone to get the date and time. But, it works out of the box. 

I'm in India and we follow Indian Standard Time (IST). I can use the below command to find the time in New York. 

```bash
TZ='America/New_York' date
```

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-86.png)
_Terminal command showing New York time_

The below screenshot shows you the time comparison across different time zones such as Singapore, America, and India. 

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-87.png)
_Terminal command showing time across different timezone_

## What is the Three-Letter Command to Get Your Calendar?

Are you waiting to know the 3 letter command to view the terminal? 

It is the `cal` command. 

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-94.png)
_Terminal command to display the calendar_

Here's a **bonus** tip for you. 

You can view the calendar of any year by just adding the year next to the `cal` command. 

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-95.png)
_Terminal command showing 2022 calendar year_

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-96.png)
_Terminal command showing 2023 calendar year_

If you wish to learn more about the `cal` command you can reach out to me on social media. 

Note: `date` and `cal` come pre-installed in many Linux distributions. If you encounter the `date: command not found` error while running the `date` command, you just need to install the `coreutils` package by running the following command:

```bash
sudo apt install coreutils
```

## Conclusion

In this tutorial, I shared my experience of using the `date` command in Linux. I hope you enjoyed reading this article. 

To have more insightful blogs delivered to your inbox, subscribe to my newsletter [here](https://5minslearn.gogosoon.com/). 


