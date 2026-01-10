---
title: 'Google Interview Question Guide: Delete Reoccurring Characters with Python'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-31T16:42:33.000Z'
originalURL: https://freecodecamp.org/news/solving-a-google-interview-question-python-2-code-included-eddefcaeffb2
coverImage: https://cdn-media-1.freecodecamp.org/images/1*e56V2AE2vxE7FgYBWb80_g.jpeg
tags:
- name: Google
  slug: google
- name: Job Interview
  slug: job-interview
- name: General Programming
  slug: programming
- name: Software Engineering
  slug: software-engineering
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Anthony Sistilli

  Nowadays, Google interviews are all the rage. But sometimes, interviews can get
  the best of us. Especially if it’s for a position we really want.

  I’ve had the pleasure of interviewing at multiple top companies as a student, and
  la...'
---

By Anthony Sistilli

Nowadays, Google interviews are all the rage. But sometimes, interviews can get the best of us. Especially if it’s for a position we **really** want.

I’ve had the pleasure of interviewing at multiple top companies as a student, and landing a job in Silicon Valley as a Software Engineer.

My goal is to help **you** get that dream job you’ve always wanted!

We’re going to go over a classic question that could show up on your next Google Interview.

**Warning: if you’re a coding veteran, you probably already know how to solve this question!**

If you’re trying to get an **Internship** or a **Full-Time** job next year, then you’ll definitely benefit from this article. ???

### QUESTION: Given a string as your input, delete any reoccurring character, and return the new string.

If you would prefer a video to explain the question, [I made one here](https://www.youtube.com/watch?v=EaNX2PG6PEM).

![Image](https://cdn-media-1.freecodecamp.org/images/vv17teBZkBcz1N9YYWbuSuDrjToPBRKECOs9)

As we can see from the example above, the output is “abc” because we delete the second ‘a’, ‘b’, and ‘c’.

First things first, let’s set up our function in Python 2.7.

```
def deleteReoccurringCharacters(string):
```

To tackle this question, we’re going to use a specific data structure called a HashSet.

![Image](https://cdn-media-1.freecodecamp.org/images/LcEjXtDtuirkkf-VWJ5VNDes95irHF-8K89D)
_A Set_

You can think of a set as being similar to an array, with two main exceptions.

1. **It’s completely unordered**
2. **It can’t contain duplicates**

Because it’s unordered, we’ll also need an empty string to store the characters we’ve added to the set in order. This will be the string we return.

Let’s set both of those things up.

```
def deleteReoccurringCharacters(string):    seenCharacters = set()    outputString = ''
```

Now that we’ve set up the data structures we need, let’s talk about our algorithm.

Because of the way a set works in memory, it has a lookup time complexity of 0(1).

This means we can use it to check whether or not we’ve already visited a character!

### Our algorithm

**Loop through all the characters in the initial string and do the following:**

> Step 1: Check if the character is in our set already

> Step 2: If it’s not in the set, add it to the set and append it to the string

Let’s see what that would look like in code ???

```
for char in string:    if char not in seenCharacters:        seenCharacters.add(char)        outputString += char
```

We don’t have to worry about an “else” case, because we don’t do anything with the reoccurring character itself.

Now all that’s left to do is return the outputString.

**Here’s what the finished code looks like:**

```
def deleteReoccurringCharacters(string):    seenCharacters = set()    outputString = ''    for char in string:        if char not in seenCharacters:            seenCharacters.add(char)            outputString += char    return outputString
```

And there you have it!

Now if this was an interview, your recruiter would ask you about the time and space complexity.

Let’s do a little analysis.

### Time Complexity

Iterating through the entire input string has a time complexity of O(n), since there are _n_ characters in the string itself.

For each of those characters, we have to check whether or not we’ve seen the… However, since a HashSet has a lookup time of O(1), our time complexity isn’t impacted.

Leaving us with a final time complexity of **O(n).**

### Space Complexity

Worst case scenario, we get a string with all unique characters. For example, “abcdef”.

In that case, we would store all _n_ elements in our string and our set.

However, we’re also limited to size of the english alphabet.

This is a good chance to ask our interviewer what type of characters count as unique in the string (uppercase / lowercase / numbers / symbols).

Assuming that the initial string will contain lowercase letters from the alphabet, since the alphabet is finite, our set and output string can never be bigger than 26 characters.

Leaving us with a worst case scenario space complexity of **O(1).**

### You now know how to solve a Google interview question!

This question is likely to come up in the early stages of the interview due to it’s straightforwardness… Like the online test, or the first phone call.

If you’re a visual learner like I am, [check out this video I made explaining the solution further.](https://www.youtube.com/watch?v=EaNX2PG6PEM) **I create a new tutorial video everyday revolving around starting your career in software.**

I’ve also posted the finished code on Github [here](https://github.com/AtotheY/YoutubeTutorials/blob/master/InterviewPrep/deleteReoccuringCharacters.py).

Thanks for watching, and good luck!

.a #33

