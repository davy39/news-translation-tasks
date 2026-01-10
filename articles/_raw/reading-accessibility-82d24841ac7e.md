---
title: If you want to talk about Accessibility, then we need to talk about Readability
  issues.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-08T14:14:17.000Z'
originalURL: https://freecodecamp.org/news/reading-accessibility-82d24841ac7e
coverImage: https://cdn-media-1.freecodecamp.org/images/0*XasHqwgzIbn-rNW4
tags:
- name: Accessibility
  slug: accessibility
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: writing
  slug: writing
seo_title: null
seo_desc: 'By Code Girl

  Before I became a web developer, I was a college professor, and my major during
  my doctoral program was language and literacy acquisition. That’s a technical way
  of saying I studied how we learn to read and write. I worked with strugglin...'
---

By Code Girl

Before I became a web developer, I was a college professor, and my major during my doctoral program was language and literacy acquisition. That’s a technical way of saying I studied how we learn to read and write. I worked with struggling readers of all ages, specifically in middle school but adults as well.

Did you know that the average reading level of adults living in the United States is between 7th and 8th grade, middle school level? It’s a sad fact. Further, people prefer to read about two grade levels below their reading level because it’s more comfortable.

When it comes to technical content, a person’s reading level dramatically lowers. They just can’t comprehend the unfamiliar technical vocabulary, complex sentence structure, and buzzwords that have no context to them.

This is of critical importance for the content of whatever websites you are building. Your **About** section, **FAQ**s, and **Directions** are generally written by members of a team that have a strong educational background, have a reading level between a high school and college level, and have substantial writing skills. In other words, what you are writing might not be comprehendible by your audience.

When it comes to accessibility, you simply must be checking the readability of everything you want your audience to read and comprehend. And this is important to keep in mind for both native English speakers and non-native English speakers alike.

To illustrate this problem, I want to share with you an experience I had in the spring of this year. I volunteered to help a fabulous nonprofit organization, [Bank on Atlanta](http://bankonatlanta.org/), build their website (working on Phase 2 now). Their goal is to help low-income, low-literacy citizens learn about financial literacy, predatory lending, and safely securing their money.

The website’s goal is to display key information since participants would be working directly with trained counselors. This is a link to [Phase 1](https://fwallacephd.github.io/BOAClone/) of the website where the organization is described (embedded below). Take a minute and read this description. As you read, make a guess at the grade level of this passage.

![Image](https://cdn-media-1.freecodecamp.org/images/CK-AWdp0ljnfhrm7z8saAUnBcFNQPQ8T91Pp)
_Phase 1 Description_

### The Flesch Reading Ease Score and Flesch-Kincaid Grade Level

While there are many algorithms out there to assess readability, there are two main measures used to define readability: The Flesch Reading Ease Score and the Flesch-Kincaid Grade Level.

The U.S. Department of Defense uses the Flesch Reading Ease Score for documents and forms. Florida uses it to evaluate insurance policies. The Armed forces uses the Flesch-Kincaid Grade Level to assess technical manuals.

These algorithms (embedded below) measure readability by examining the average length of sentences (measured by the number of words) and the average number of syllables per word (words with syllables of 3 or more are extremely difficult for struggling readers).

A higher score on the Flesch Reading Ease Score indicates ease of reading, so a score of 100 is ideal. This type of text gets to the point with short sentences, no words with more than 2 syllables, and no buzzwords. A score of 60–70 is considered an average score.

The Flesch-Kincaid Grade Level is used extensively in the field of education and uses the same measures as the Flesch Reading Ease Score. The difference is that instead of presenting a numerical score, a U.S. grade level is assigned to the passage which makes it easier for educators, parents, librarians and others to understand and address the student’s ability.

![Image](https://cdn-media-1.freecodecamp.org/images/rcAHP9BCBFquAKA8i7-LHkq9o2lgKB-uwahj)
_from [Readable.io](https://readable.io/blog/the-flesch-reading-ease-and-flesch-kincaid-grade-level/" rel="noopener" target="_blank" title=")_

What grade level did you guess for the Bank on Atlanta about passage?

The passage on the Bank on Atlanta site earned a score of 30.7 on the Flesch Reading Ease Score, meaning difficult to read. On the Flesch-Kincaid Grade Level, the passage earned a 14.2 level, meaning college level.

As stated before, adults in this country have an average reading level between 7th and 8th grade, and the reading level of non-native English speakers varies greatly.

The diagram below clearly illustrates these results:

![Image](https://cdn-media-1.freecodecamp.org/images/38LeDRDDoIe7-sVvrPBWZFW4SgKmiE2JJ5hK)
_The orange circle indicates the score from our passage._

### Two Key Problems

To give you a picture of why this passage is so difficult, I will focus on two key issues.

The first problem is sentence length. The longer the sentence is, the more complexity you add to the sentence. Complex sentences may have multiple subjects, verbs, objects, not to mention embedded clauses and phrases, and tenses that may shift. When the reader struggles with word analysis and vocabulary skills, complicated sentence structures cause the reader frustration which may force them to stop reading.

At a 7th or 8th-grade reading level, a comfortable number of words per sentence would be 13–16, but our passage’s average was between 20–22 (see diagram).

![Image](https://cdn-media-1.freecodecamp.org/images/v0052YuH8JATK5Ij4HsDk3zQZAYLmECVMVBi)

Polysyllabic words are words that have 3 or more syllables. These words tax the reader to decode (or sound out) the word as well as make meaning of the word at the same time. Understanding bases/roots and prefix/suffixes is an advanced skill, but the more syllables a word has, the more of these components are included.

Take, for example, a keyword from our passage “underbanked” — a 4 syllable word with three meaningful word parts: “under” (2 syllables), “bank”, and the ending “ed”. Worse, this is also a buzzword. It has no context for the reader.

The average percent of 3-syllable words for U.S. high school and adult readers is between 12–14%. The percent of 3-syllable words in this text is between 26–29%. This is extremely high (see diagram).

![Image](https://cdn-media-1.freecodecamp.org/images/7-duAyMUtL3FSY2w0Wa7J1uSaouDVTIA6AxW)

### Revisions

Luckily, it’s easy to determine the reading level of a passage and analyze why it is difficult. It’s more challenging to revise a passage to lower the reading level rather than start when you are writing by paying attention to sentence length, polysyllabic words, and even buzzwords.

Thankfully, Bank on Atlanta is committed to creating a website where all of their readers can comprehend the necessary information with ease.

By simply writing shorter but more sentences, eliminating polysyllabic words, and limiting buzzwords, their second draft was far more successful:

![Image](https://cdn-media-1.freecodecamp.org/images/kbU3MxqMGq7TFAB1ZC4Y2wTZ3icDyr1QD94k)
_Revised Description_

The first draft on the Bank on Atlanta site earned a score of 30.7 on the Flesch Reading Ease Score, which is difficult to read. On the Flesch-Kincaid Grade Level, the first draft earned a 14.2 level, meaning college level.

This second draft earned a 64.5, which is considered average, on the Flesch Reading Ease Scale, and a grade level of 8.4 on the Flesch-Kincaid Grade Level. This revision was a huge success!

Because our target audience are struggling readers, we have more revisions to make. At best, our passages should be at a 5th-grade reading level. But the point is that the team made readability a priority and we are making progress.

To determine the readability of passages on your websites, use this [free tool](https://www.online-utility.org/english/readability_test_and_improve.jsp). It will provide you with scores for both the Flesch Reading Ease Score and the Flesch-Kincaid Grade Level, and hopefully, you will make revisions based on your scores.

