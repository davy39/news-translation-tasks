---
title: The Rabin-Karp Algorithm Explained
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/the-rabin-karp-algorithm-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d0b740569d1a4ca3596.jpg
tags:
- name: algorithms
  slug: algorithms
- name: toothbrush
  slug: toothbrush
seo_title: null
seo_desc: 'The Rabin-Karp algorithm is a string matching/searching algorithm developed
  by Michael O. Rabin and Richard M. Karp. It uses hashing technique and brute force
  for comparison, and is a good candidate for plagiarism detection.

  Important terms


  pattern ...'
---

The Rabin-Karp algorithm is a string matching/searching algorithm developed by Michael O. Rabin and Richard M. Karp. It uses **_hashing_** technique and **_brute force_** for comparison, and is a good candidate for plagiarism detection.

## Important terms

* **_pattern_** is the string to be searched. Consider length of pattern as **_M_** characters.
* **_text_** is the whole text from which the pattern is to be searched. Consider length of text as **_N_** characters.

## What is brute force comparison?

In brute force comparison each character of pattern is compared with each character of text until characters that don't match are found.

## How the Rabin-Karp Algorithm Works

1. Calculate hash value of _pattern_
2. Calculate hash value of first _M_ characters of _text_
3. Compare both hash values
4. If they are unequal, calculate hash value for next _M_ characters of _text_ and compare again.
5. If they are equal, perform a brute force comparison.

```text
hash_p = hash value of pattern
hash_t = hash value of first M letters in body of text
do
	if (hash_p == hash_t) 
		brute force comparison of pattern and selected section of text
	hash_t= hash value of next section of text, one character over
while (end of text or brute force comparison == true)
```

## Advantage over Naive String Matching Algorithm

This technique results in only one comparison per text sub-sequence and brute force is only required when the hash values match.

