---
title: You Don’t Need a Regex for That
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-25T20:02:30.000Z'
originalURL: https://freecodecamp.org/news/you-dont-need-a-regex-for-that-57c771c4fab0
coverImage: https://cdn-media-1.freecodecamp.org/images/1*QCpHG1qtGQoztknxNo9d4Q.jpeg
tags:
- name: Poetry
  slug: poetry
- name: Regex
  slug: regex
- name: software development
  slug: software-development
- name: Software Engineering
  slug: software-engineering
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Rina Artstain

  I once had a web siteon which one could searchfor all sorts of things(as long as
  they’re strings)

  The items had titlesand content and moreso the search used a regexto help you explore

  We had an ideawe gave it a trylet’s help you find...'
---

By Rina Artstain

I once had a web site  
on which one could search  
for all sorts of things  
(as long as they’re strings)

The items had titles  
and content and more  
so the search used a regex  
to help you explore

We had an idea  
we gave it a try  
let’s help you find more  
we’ll add synonyms galore

We tacked on those words  
to the end of the regex  
and straight to production  
(we didn’t have stress tests)

And lo and behold  
the site all but crashed  
so many timeouts  
we all were abashed

The change was reverted  
and there we sat hurted  
trying to think  
what brought us to this brink

We researched those regexes  
and guess what we found:  
you should compile them first  
if you want them around

So try that we did  
and it didn’t work  
the site was still slow  
we hoped it’s a quirk

We tried many things  
we were all stressing  
until we decided  
it’s time to start testing!

We drew up some schemes  
for searching multiple words  
and what a surprise  
we saw with our eyes

String.Find()  
was 1000 times faster  
than all of those regexes  
which caused the disaster

We learned our lesson  
I hope you did too  
regexes are evil  
except for a few

If your regex is simple  
just put it away  
you’re probably wasting  
your time anyway

All of us know  
the truth’s where it’s at  
in most of the cases  
YOU DON’T NEED A REGEX FOR THAT

P.S.  
Please excuse my bad rhymes and rhythm, I get paid to write software. Not poetry.

