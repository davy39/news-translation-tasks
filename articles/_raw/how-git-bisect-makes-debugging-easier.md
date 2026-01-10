---
title: How Git Bisect Makes Debugging Easier
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-23T00:06:25.000Z'
originalURL: https://freecodecamp.org/news/how-git-bisect-makes-debugging-easier
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c998e740569d1a4ca2065.jpg
tags:
- name: debugging
  slug: debugging
- name: Git
  slug: git
- name: Productivity
  slug: productivity
seo_title: null
seo_desc: 'By Periklis Gkolias

  Git bisect is a fantastic tool that can help make debugging a breeze. But very few
  people use it actively.

  In this quick article, I will showcase how git bisect can easily point out the where
  your bugs lie.

  But first, lets talk ab...'
---

By Periklis Gkolias

_Git bisect_ is a fantastic tool that can help make debugging a breeze. But very few people use it actively.

In this quick article, I will showcase how _git bisect_ can easily point out the where your bugs lie.

But first, lets talk about...

### Delta debugging

Delta debugging is the process of completing many debugging steps and in each one your goal is to eliminate half the "problem". You can think of it as the binary search of debugging. Or as [Andreas Zeller](https://andreas-zeller.info/) (who coined the term) said:

> Delta Debugging automates the scientific method of debugging. The basic idea of the scientific method is to establish a hypothesis on why something does not work. You test this hypothesis, and you refine or reject it depending on the test outcome. When debugging, people are doing this all the time. Manually. Delta Debugging automates this process.

_Git bisect_ is how we apply delta debugging with Git.

Let's assume we have a bug and we try to find the root cause. In every step of our investigation for a solution, we eliminate half the solution space. Configuration, code, input...anything. Here's an example to make it clearer.

### Git bisect example

First, we need to initialize a repository to track our work.

```
mkdir test_git_bisect && cd test_git_bisect && git init

```

Let's say we are going to make a script that gets an epoch and converts it to

```
datetime

```

We do that by using an input file (named epochs.txt) that _should_ contain only epochs.

Please note, that in order to run a _git bisect_ smoothly, we need to have quite a few commits.

The python script `parse_epochs.py` we will use here is nothing special.

```

from time import localtime, strftime

with open('epochs.txt', 'r') as handler:
    epochs = handler.readlines()
    for epoch in epochs:
        current_datetime = strftime('%Y-%m-%d %H:%M:%S', localtime(int(epoch)))
        print(current_datetime)


```

Let's commit the first change:

`git add . && git commit -m "Created epoch parser"`

then create the input:

`for i in {1..100}; do   sleep 3;   date +%s >> epochs.txt; done`

This is essentially all epochs from the time we started the script (plus 3 seconds) until five minutes later, with a 3 second step.

Again we commit the change:

`git add . && git commit -m "Generated the first version of input"`

If we now run the initial script, we get all inputs parsed to dates:

```
$ python3 parse_epochs.py
2020-07-21 16:08:39
2020-07-21 16:10:40
2020-07-21 16:10:43
2020-07-21 16:10:46
2020-07-21 16:10:49
2020-07-21 16:10:52
...

```

Let's amend the input now to make it faulty:

```
echo "random string" >> epochs.txt

```

and commit again:

```
git add . && git commit -m "Added faulty input"

```

For the sake of entropy, to make the example more complex, let's add more faulty inputs - commits.

```
echo "This is not an epoch" >> epochs.txt 
&& git add . && git commit -m "Added faulty input v2"

```

```
echo "Stop this, the script will break" >> epochs.txt
&& git add . && git commit -m "Added faulty input v3"

```

Here is the commit log we have created:

```
$ git log --pretty=format:"%h - %an, %ar : %s"
b811d35 - Periklis Gkolias, 2 minutes ago: Added faulty input v3
dbf75cd - Periklis Gkolias, 2 minutes ago: Added faulty input v2
cbfa2f5 - Periklis Gkolias, 8 minutes ago: Added faulty input
d02eae8 - Periklis Gkolias, 20 minutes ago: Generated first version of input
a969f3d - Periklis Gkolias, 26 minutes ago: Created epoch parser

```

If we run the script again, it will obviously fail with the following error:

```
Traceback (most recent call last):
  File "parse_epochs.py", line 6, in <module>
    current_datetime = strftime('%Y-%m-%d %H:%M:%S', localtime(int(epoch)))
ValueError: invalid literal for int() with base 10: 'random string\n'


```

Looks like we need _git bisect_ to fix this. To do so we need to start the investigation:

`git bisect start`

and mark one commit as bad (usually the last one) and one commit as good. This would be the second commit when we generated the input:

```
git bisect bad b811d35 && git bisect good d02eae8

```

After that, git bisect will split the history between the good and the bad commit in two. You can see that by doing `git bisect visualize` to see the commits that are considered the culprits, and

```
git show

```

to print the currently checked out one, in our case this one:

```
dbf75cd

```

If we run the script it will still fail. So we mark the current commit as bad:

`git bisect bad dbf75cd`

It is worth mentioning the output of Git in that case:

```
git bisect bad dbf75cd
Bisecting: 0 revisions left to test after this (roughly 0 steps)
[cbfa2f5f52b7e8a0c3a510a151ac7653377cfae1] Added faulty input

```

Git knows we are almost there. Yay!

If we run the script again, it of course fails. And if we mark it as bad, Git says:

```
git bisect bad cbfa2f5
cbfa2f5f52b7e8a0c3a510a151ac7653377cfae1 is the first bad commit

```

By then, you may either fix the bug or contact whomever committed the bad code/input/configuration. Here is how to get the details:

```
$ git show -s --format='%an, %ae' cbfa2f5
Periklis Gkolias, myemail@domain.com

```

## Conclusion

Thank you for reading this article. Feel free to share your thoughts on this great tool.

