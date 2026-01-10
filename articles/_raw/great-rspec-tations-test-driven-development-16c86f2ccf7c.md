---
title: 'Great RSpec-tations: why I love test-driven development'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-23T23:57:01.000Z'
originalURL: https://freecodecamp.org/news/great-rspec-tations-test-driven-development-16c86f2ccf7c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*OvF5QBJTAjMURU4G2BSWNA.jpeg
tags:
- name: General Programming
  slug: programming
- name: Ruby on Rails
  slug: ruby-on-rails
- name: technology
  slug: technology
- name: test driven development
  slug: test-driven-development
- name: women in tech
  slug: women-in-tech
seo_title: null
seo_desc: 'By Arit Amana

  When I first wrote about Test-Driven Development, I thought I was in love with the
  concept… but that was just the flirting stage. Now I’ve fallen head-over-Louboutins,
  girlfriend! ?

  The efficiency gains from not needing to fire my app u...'
---

By Arit Amana

When I first [wrote about Test-Driven Development](https://code.likeagirl.io/what-done-looks-like-test-driven-development-e9b0eaa38836), I thought I was in love with the concept… but that was just the flirting stage. Now I’ve fallen head-over-Louboutins, girlfriend! ?

The efficiency gains from not needing to fire my app up for testing are just the beginning. Developing my apps with [RSpec](http://rspec.info/) forces me to really think about how I’m defining and structuring my code. Furthermore, every time my tests fail, they faithfully supply tips and clues that help me troubleshoot what’s missing, broken or redundant. Now that’s a metaphor for life in general… but I digress. ?

I’m creating an online chess app [as part of an agile development team](https://code.likeagirl.io/no-longer-the-lone-coding-wolf-4fb52360b808), and this week, I was tasked with building the **move_to!(x,y)** method. This should move a chess piece (called **pawn** from now on) to the chessboard square at location **(x,y)**.

If an opponent’s piece (called **king** from now on) occupies (x,y), pawn should capture it. If pawn’s brother-in-arms occupies (x,y), the method should raise an error message and pawn should go nowhere.

Note: move_to!(x,y) doesn’t consider whether the moves or captures are valid. Other methods will do this.

I configured [FactoryBot](https://github.com/thoughtbot/factory_bot) to generate instances of a chess game. Each chess piece has the following relevant attributes: **:location_x**, **:location_y**, **:white** (a boolean; **true** = white color), **:game_id**, and **:notcaptured** (a boolean; **false** = the piece has been captured). My first test determined if pawn (currently on 0,0) moved to an empty square (7,7):

Next, I began writing the **move_to!(x,y)** method, then ran my test:

```
arit (master) chessapp $ rspec spec/models/piece_spec.rb
```

```
.
```

```
Finished in 0.43495 seconds (files took 15.68 seconds to load)
```

```
1 example, 0 failures
```

Yes! No errors. ?? Next, I wrote a test to determine whether pawn stayed put if its destination was occupied by a friendly piece (we’ll call it ro**ok):**

Why aren’t I testing the values of **rook.notcaptured**, **rook.location_x** and **rook.location_y**? Well, the rook IS the friendly-piece in question, but what we’re actually testing is whatever piece (if any) is **found by and saved in the _destination_ variable**. Now to flesh out the method:

My tests passed again! ?? Feeling very confident, I moved on to the third test: to determine if the opponent’s king was captured and whether pawn took its place:

I also completed the method:

But when I ran my tests, I received the following error:

```
arit (master *) chessapp $ rspec spec/models/piece_spec.rb
```

```
..F
```

```
Failures:
```

```
1) Piece captures opponent's piece on destination, then assumes that position
```

```
Failure/Error: expect(destination.notcaptured).to be false
```

```
expected false
```

```
got true
```

```
# ./spec/models/piece_spec.rb:104:in `block (2 levels) in <top (required)>'
```

```
Finished in 0.21787 seconds (files took 4.83 seconds to load)
```

```
1 example, 1 failure
```

```
Failed examples:
```

```
rspec ./spec/models/piece_spec.rb:95 # Piece captures opponent's piece on destination, then assumes that position
```

Wha??? **destination.notcaptured** was not updated? Why? I re-read my method over and over. Nothing seemed to be missing or broken (and, really, just how much could I get wrong in 11 lines of code?).

After deciding to make like a ? and review my rspec test sloooowwly, it occurred to me that the d**estination** variable was expected to change. The move_to!(x,y) method had updated its l**ocation_x, location_y** and n**otcaptured** attributes.

Then it hit me — I needed to RELOAD **destination** from the database back into RSpec. Then my three tests passed beautifully:

Test-Driven Development has permanently impacted my coding practice, and I relished the opportunity to turn the rest of my teammates unto it. TDD is lightweight, efficient, safe, revealing, and it helps me produce higher-quality code the first … well, okay… in as little time as possible! ?

