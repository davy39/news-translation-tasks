---
title: This is why the HyperLogLog algorithm is my new favorite
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-05T12:31:00.000Z'
originalURL: https://freecodecamp.org/news/my-favorite-algorithm-and-data-structure-hyperloglog-6583a25c8a4f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ij4OThN8DISD0zwH-7UlWQ.jpeg
tags:
- name: Data Science
  slug: data-science
- name: data structures
  slug: data-structures
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Alex Nadalin

  Every now and then I bump into a concept that’s so simple and powerful that I’m
  wish I’d discovered such an incredible and beautiful idea.

  I discovered HyperLogLog (HLL) a couple of years ago, and fell in love with it right
  after read...'
---

By Alex Nadalin

Every now and then I bump into a concept that’s so simple and powerful that I’m wish I’d discovered such an incredible and beautiful idea.

I discovered [HyperLogLog](https://en.wikipedia.org/wiki/HyperLogLog) (HLL) a couple of years ago, and fell in love with it right after reading how [redis decided to add a HLL data structure](http://antirez.com/news/75).

The idea behind HLL is devastatingly simple but extremely powerful. This is what makes it such a widespread algorithm, used by giants of the internet such as Google and Reddit.

#### Collecting phone numbers

My friend Tommy and I planned to go to a conference. While heading to its location, we decided to wager on who would meet the most new people. Once we reached the place, we’d start conversing around and keep a counter of how many people we talked to.

![Image](https://cdn-media-1.freecodecamp.org/images/0*oIVPnmV6cE4mAbaK.png)

At the end of the event, Tommy comes to me with his figure — say, 17 — and I tell him that I had a word with 46 people.

Clearly, I am the winner, but Tommy’s frustrated as he thinks I’ve counted the same people multiple times. He believes he only saw me talking to maybe 15–20 people in total.

So, the wager’s off. We decide that for our next event, we’ll be taking down names instead, to be sure we’re counting unique people, and not just the total number of conversations.

At the end of the following conference, we meet each other with a very long list of names and — guess what? Tommy had a couple more encounters than I did! We laugh it off, and while discussing our approach to counting uniques, Tommy comes up with a great idea:

_“Alex, you know what? We can’t go around with pen and paper and track down a list of names, it’s really impractical! Today I spoke to 65 different people and counting their names on this paper was a real pain. I lost count 3 times and had to start from scratch!”_

_“Yeah, I know, but do we even have an alternative?”_

_“What if, for our next conference, instead of asking for names, we ask people the last 5 digits of their phone number? Instead of winning by counting their names, the winner will be the one who spoke to someone with the longest sequence of leading zeroes in those digits.”_

_“Wait Tommy, you’re going too fast! Slow down a second and give me an example…”_

_“Sure, just ask each person for those last 5 digits, ok? Let’s suppose they reply ‘54701’. There’s no leading zero, so the longest sequence of leading zeroes is 0. The next person you talk to says ‘02561’ — that’s a leading zero! So your longest sequence is now 1.”_

_“You’re starting to make sense to me…”_

_“Yeah, so if we speak to only a couple of people, chances are that are longest zero-sequence will be 0. But if we talk to maybe 10 people, we have more chances of it being 1.”_

_“Now, imagine you tell me your longest zero-sequence is 5 — you must have spoken to thousands of people to find someone with 00000 in their phone number!”_

_“Dude, you’re a damn genius!”_

#### And that, my friends, is how HyperLogLog fundamentally works.

It allows us to estimate unique items within a large dataset by recording the longest sequence of zeroes within that set.

This ends up creating an incredible advantage over keeping track of each and every element in the set. It is an incredibly efficient way to count unique values, with relatively high accuracy.

> _“The HyperLogLog algorithm can estimate cardinalities well beyond 10⁹ with a relative accuracy (standard error) of 2% while only using 1.5kb of memory”_

> **_Fangjin Yang —_** _[Fast, Cheap, and 98% Right: Cardinality Estimation for Big Data](http://druid.io/blog/2012/05/04/fast-cheap-and-98-right-cardinality-estimation-for-big-data.html)_

Since I may be oversimplifying, let’s have a look at some more details of HLL.

### More HLL details

HLL is part of a family of algorithms that aim to address [cardinality estimation](https://en.wikipedia.org/wiki/Count-distinct_problem) — otherwise known as the “count-distinct problem.” How can we efficiently count the number of unique objects in a data set?

This is extremely useful for lots of today’s web applications. For example, when you want to count how many unique views an article on your site has generated.

When HLL runs, it takes your input data and hashes it, turning it into a bit sequence:

```
IP address of the viewer: 54.134.45.789
```

```
HLL hash: 010010101010101010111010...
```

Now, an important part of HLL is to make sure that your hashing function distributes bits as evenly as possible. You don’t want to use a weak function such as:

A HLL using this hashing function would return biased results if, for example, the [distribution of your visitors is tied to a specific geographic region](https://stackoverflow.com/a/277537/934439).

The [original paper](http://algo.inria.fr/flajolet/Publications/FlFuGaMe07.pdf) has a few more details on what a good hashing function means for HLL:

> _“All known efficient cardinality estimators rely on randomization, which is ensured by the use of hash functions._

> _The elements to be counted belonging to a certain data domain D, we assume given a hash function, h : D → {0, 1}∞; that is, we assimilate hashed values to infinite binary strings of {0, 1}∞, or equivalently to real numbers of the unit interval._

> _[…]_

> _We postulate that the hash function has been designed in such a way that the hashed values closely resemble a uniform model of randomness, namely, bits of hashed values are assumed to be independent and to have each probability [0.5] of occurring.”_

> **_Philippe Flajolet —_** _[HyperLogLog: The Analysis of a Near-optimal Cardinality Estimation Algorithm](http://algo.inria.fr/flajolet/Publications/FlFuGaMe07.pdf)_

Now, after we’ve picked a suitable hash function, we need to address another pitfall: [variance](https://en.wikipedia.org/wiki/Variance).

Going back to our example, imagine that the first person you talk to at the conference tells you their number ends with `00004` — jackpot!

You might have won a wager against Tommy, but if you use this method in real life, chances are that specific data in your set will negatively influence the estimation.

Fear no more, as this is a problem HLL was born to solve.

Not many are aware that [Philippe Flajolet](https://en.wikipedia.org/wiki/Philippe_Flajolet), one of the brains behind HLL, has been involved in cardinality-estimation problems for a long time. Long enough to have come up with the [Flajolet-Martin algorithm in 1984](https://en.wikipedia.org/wiki/Flajolet%E2%80%93Martin_algorithm#Improving_accuracy) and [(super-)LogLog in 2003](http://algo.inria.fr/flajolet/Publications/DuFl03-LNCS.pdf).

These algorithms already addressed some of the problems with outlying hashed values, by dividing measurements into buckets, and (somewhat) averaging values across buckets.

If you got lost here, let me go back to our original example.

Instead of just taking the last 5 digits of a phone number, we take 6 of them. Now, we store the longest sequence of leading zeroes together with the first digit (the ‘bucket’).

This means that our data will look like:

```
Input:708942 --> in the 7th bucket, the longest sequence of 0s is 1518942 --> in the 5th bucket, the longest sequence of 0s is 0500973 --> in the 5th bucket, the longest sequence of 0s is now 2900000 --> in the 9th bucket, the longest sequence of 0s is 5900672 --> in the 9th bucket, the longest sequence of 0s stays 5
```

```
Buckets:0: 01: 02: 03: 04: 05: 26: 07: 18: 09: 5
```

```
Output:avg(buckets) = 0.8
```

As you can see, if we weren’t employing buckets, we would instead use 5 as the longest sequence of zeroes. This would negatively impact our estimation.

Although I simplified the math behind buckets (it’s not just a simple average), you can totally see how this approach makes sense.

It’s interesting to see how Flajolet addresses variance throughout his works:

> _“While we’ve got an estimate that’s already pretty good, it’s possible to get a lot better. Durand and Flajolet make the observation that outlying values do a lot to decrease the accuracy of the estimate; by throwing out the largest values before averaging, accuracy can be improved._

> _Specifically, by throwing out the 30% of buckets with the largest values, and averaging only 70% of buckets with the smaller values, accuracy can be improved from 1.30/sqrt(m) to only 1.05/sqrt(m)! That means that our earlier example, with 640 bytes of state and an average error of 4% now has an average error of about 3.2%, with no additional increase in space required._

> _Finally, the major contribution of Flajolet et al in the HyperLogLog paper is to use a different type of averaging, taking the harmonic mean instead of the geometric mean we just applied. By doing this, they’re able to edge down the error to 1.04/sqrt(m), again with no increase in state required”_

> **_Nick Johnson_** _— [Improving Accuracy: SuperLogLog and HyperLogLog](http://blog.notdot.net/2012/09/Dam-Cool-Algorithms-Cardinality-Estimation)_

### HLL in the wild

So, where can we find the application of HLLs? Two great web-scale examples are:

* [BigQuery](https://cloud.google.com/blog/big-data/2017/07/counting-uniques-faster-in-bigquery-with-hyperloglog), to efficiently count uniques in a table (`APPROX_COUNT_DISTINCT()`)
* [Reddit](https://redditblog.com/2017/05/24/view-counting-at-reddit/), where it’s used to calculate how many unique views a post has gathered

In particular, see how HLL impacts queries on BigQuery:

```
SELECT COUNT(DISTINCT actor.login) exact_cntFROM `githubarchive.year.2016`6,610,026 (4.1s elapsed, 3.39 GB processed, 320,825,029 rows scanned)
```

```
SELECT APPROX_COUNT_DISTINCT(actor.login) approx_cntFROM `githubarchive.year.2016`6,643,627 (2.6s elapsed, 3.39 GB processed, 320,825,029 rows scanned)
```

The second result is an approximation (with an error rate of ~0.5%), but takes a fraction of the time.

Long story short: **HyperLogLog is amazing!**

Now you know what it is and when it can be used, so go out and do incredible stuff with it!

### Further reading

* [HyperLogLog on Wikipedia](https://en.wikipedia.org/wiki/HyperLogLog)
* the [original paper](http://algo.inria.fr/flajolet/Publications/FlFuGaMe07.pdf)
* [HyperLogLog++, Google’s improved implementation of HLL](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/40671.pdf)
* [Redis new data structure: the HyperLogLog](http://antirez.com/news/75)
* [Damn Cool Algorithms: Cardinality Estimation](http://blog.notdot.net/2012/09/Dam-Cool-Algorithms-Cardinality-Estimation)
* [HLL data types in Riak](https://github.com/basho/riak_kv/blob/develop/docs/hll/hll.pdf)
* [HyperLogLog and MinHash](http://tech.adroll.com/blog/data/2013/07/10/hll-minhash.html)

_Originally published at [odino.org](http://odino.org/my-favorite-data-structure-hyperloglog/) (13th Jan 2018)._

