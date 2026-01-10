---
title: Bash Sleep – How to Make a Shell Script Wait N Seconds (Example Command)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-09-13T14:29:40.000Z'
originalURL: https://freecodecamp.org/news/bash-sleep-how-to-make-a-shell-script-wait-n-seconds-example-command
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/pexels-----------------------1560424.jpg
tags:
- name: Bash
  slug: bash
- name: shell script
  slug: shell-script
seo_title: null
seo_desc: "By Veronica Stork\nWhen you're writing a shell script, you may find that\
  \ you need it to wait a certain number of seconds before proceeding. For example,\
  \ you might want the script to wait while a process completes or before retrying\
  \ a failed command. \n..."
---

By Veronica Stork

When you're writing a shell script, you may find that you need it to wait a certain number of seconds before proceeding. For example, you might want the script to wait while a process completes or before retrying a failed command. 

To do this, you can use the very straightforward `sleep` command. 

## How to Use the Bash Sleep Command

`Sleep`  is a very versatile command with a very simple syntax. It is as easy as typing `sleep N`. This will pause your script for `N` seconds, with `N` being either a positive integer or a floating point number. 

Consider this basic example:

```
echo "Hello there!"
sleep 2
echo "Oops! I fell asleep for a couple seconds!"
```

The result of this script will look like this:

![gif of script running](https://www.freecodecamp.org/news/content/images/2021/09/2021-09-10-22.33.49.gif)

Similarly, you could use a floating point number to represent fractions of seconds. For example, `sleep .8` will pause your script for .8 seconds. 

That's it for the basic usage of the `sleep` command! 

## What to Keep in Mind When Using the Sleep Command

`Sleep`'s default unit of time is **seconds**, which is why we don't have to specify a unit in the examples above. 

On some types of machines (namely BSD systems and MacOS,) the _only_ unit of time supported is seconds. Other Unix-like operating systems will likely support the following units of time:

* `s`: seconds
* `m`: minutes
* `h`: hours
* `d`: days

It is also possible to use more than one argument with the `sleep` command. If there are two or more numbers included, the system will wait for the amount of time equivalent to the sum of those numbers.

For example, `sleep 2m 30s` will create a pause of 2 and a half minutes. Note that to achieve the same result on a MacOS or BSD machine, you would run the equivalent command `sleep 150`, as 2 minutes and 30 seconds is equal to 150 seconds. 

## Conclusion

The `sleep` command is a useful way to add pauses in your Bash script. Used in conjunction with other commands, `sleep` can help you create a timed alarm, run operations in the correct order, space out attempts to connect to a website, and more. So put this simple yet powerful tool in your Bash toolbox and code on!

