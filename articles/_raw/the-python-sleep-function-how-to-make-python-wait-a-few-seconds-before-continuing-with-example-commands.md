---
title: The Python Sleep Function – How to Make Python Wait A Few Seconds Before Continuing,
  With Example Commands
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-08-24T16:24:24.000Z'
originalURL: https://freecodecamp.org/news/the-python-sleep-function-how-to-make-python-wait-a-few-seconds-before-continuing-with-example-commands
coverImage: https://www.freecodecamp.org/news/content/images/2020/08/pexels-pixabay-280254.jpg
tags:
- name: Productivity
  slug: productivity
- name: Python
  slug: python
seo_title: null
seo_desc: "By Amy Haddad\nYou can use Python’s sleep() function to add a time delay\
  \ to your code. \nThis function is handy if you want to pause your code between\
  \ API calls, for example. Or enhance the user’s experience by adding pauses between\
  \ words or graphics.\n..."
---

By Amy Haddad

You can use Python’s `sleep()` function to add a time delay to your code. 

This function is handy if you want to pause your code between API calls, for example. Or enhance the user’s experience by adding pauses between words or graphics.

```python
from time import sleep
sleep(2)   
print("hello world")
```

When I run the above code, there’s about a two-second delay before "hello world" prints. 

I experience a delay because `sleep()` stops the “[execution of the calling thread](https://docs.python.org/3/library/time.html#time.sleep)” for a provided number of seconds (though the exact time is approximate). So the execution of the program is paused for about two seconds in the above example.

In this article, you’ll learn how to put your Python code to sleep.

# The Details of Sleep

Python’s [time module](https://docs.python.org/3/library/time.html#time) contains many time-related functions, one of which is `sleep()`. In order to use sleep(), you need to import it.

```python
from time import sleep
```

sleep() takes one argument: seconds. This is the amount of time (in seconds) that you want to delay your code.

```python
seconds = 2
sleep(seconds)
```

## Sleep in Action

Now let’s use `sleep()` in a few different ways. 

After I import the sleep from the `time` module, two lines of text will print. However, there will be an approximate two-second delay between the printing of each line.  

```python
from time import sleep
 
print("Hello")
sleep(2)  
print("World")
```

This is what happened when I ran the code:

**`"Hello"`** This line printed right away.

Then, there was approximately a two-second delay.

**`"World"`** This line printed about two seconds after the first.

### You Can Be Precise

Make your time delay specific by passing a floating point number to `sleep()`.

```python
from time import sleep
 
print("Prints immediately.")
sleep(0.50)
print("Prints after a slight delay.")
```

This is what happened when I ran the code:

**`"Prints immediately."`** This line printed immediately.

Then, there was a delay of approximately 0.5 seconds.

**`"Prints after a slight delay."`** This line printed about 0.5 seconds after the first.

## Create a Timestamp

Here’s another example to consider.

In the code below, I create five timestamps. I use `sleep()` to add a delay of approximately one second between each timestamp.

```python
import time
 
for i in range(5):
   current_time = time.localtime()
   timestamp = time.strftime("%I:%m:%S", current_time)
   time.sleep(1)
   print(timestamp)
```

Here, I import the entire time module so I can access multiple functions from it, including sleep().

```python
import time
```

Then, I create a for loop that will iterate five times.

```python
for i in range(5):
...
```

On each iteration, I get the current time.

```python
current_time = time.localtime()
```

I get a timestamp using another function in the time module, `strftime()`.

```python
timestamp = time.strftime("%I:%m:%S", current_time)
```

The sleep() function is next, which will cause a delay on each iteration of the loop.

```python
time.sleep(1)
```

When I run the program I wait about a second before the first timestamp prints out. Then, I wait about a second for the next timestamp to print, and so on until the loop terminates.

The output looks like this:

```python
04:08:37
04:08:38
04:08:39
04:08:40
04:08:41
```

### sleep() and the User Experience

Another way to use `sleep()` is to enhance the user’s experience by creating some suspense. 

```python
from time import sleep
 
story_intro = ["It", "was", "a", "dark", "and", "stormy", "night", "..."]
for word in story_intro:
   print(word)
   sleep(1)
```

Here, I iterate through the list of words in **`story_intro`**. To add suspense, I use the sleep() function to delay by about a second after each word is printed.

```python
time.sleep(1)
```

Although execution speed is often at the forefront of our minds, sometimes it’s worth slowing down and adding a pause in our code. When those occasions arise, you know what to reach for and how it works.

_I write about learning to program, and the best ways to go about it on [amymhaddad.com](http://amymhaddad.com/)._ I tweet about programming, learning, and productivity: [@amymhaddad](https://twitter.com/amymhaddad).

