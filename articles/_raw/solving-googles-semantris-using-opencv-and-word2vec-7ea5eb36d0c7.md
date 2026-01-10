---
title: How to solve Google’s Semantris game using OpenCV and Word2Vec
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-24T22:30:58.000Z'
originalURL: https://freecodecamp.org/news/solving-googles-semantris-using-opencv-and-word2vec-7ea5eb36d0c7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*FYMv5pI8NInQAp1jQK6EIg.jpeg
tags:
- name: Computer Vision
  slug: computer-vision
- name: Data Science
  slug: data-science
- name: nlp
  slug: nlp
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Pravendra Singh

  Writing a program to play Google Semantris



  Automation is good, so long as you know exactly where to put the machine. — Eliyahu
  Goldratt

  Semantris is a set of word association games by Google that use semantic search
  to predict a ...'
---

By Pravendra Singh

#### Writing a program to play Google Semantris

![Image](https://cdn-media-1.freecodecamp.org/images/1*FYMv5pI8NInQAp1jQK6EIg.jpeg)

> Automation is good, so long as you know exactly where to put the machine. — Eliyahu Goldratt

> [Semantris](https://research.google.com/semantris/) is a set of word association games by Google that use semantic search to predict a relevant word in the game based on the player’s input.

There are 2 modes available in the game.

**ARCADE**

Arcade mode requires the player to come up with associated words for certain words. You are supposed to think and enter as fast as you can before an increasing list of words fills your screen.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ASVWg8hkhtBHdtdpJMiqLQ.gif)
_Semantris ARCADE mode_

**BLOCKS**

Blocks is a turn-based game mode. You can take your time to come up with different types of clues and see which ones the game understands best.

![Image](https://cdn-media-1.freecodecamp.org/images/1*-CEfzr_8hsgBC3dGNBSFhQ.gif)
_Semantris BLOCKS mode_

After playing for a while, I realized both the game modes are using [pattern recognition as the main game-play mechanism](http://www.peachpit.com/articles/article.aspx?p=98123&seqNum=2). That’s when I started wondering if it could be automated.

### Turns out, it can be

Semantris-Solver uses the following procedure to play the game:

* **Capture the current game state using computer vision techniques**
* **Identify the word to enter for higher-reward/longer-gameplay**
* **Find the associated word using word-embeddings**

In the following sections, we are going to dive into the working of Semantris-Solver for both the game modes.

### ARCADE

A human player will use the following moves to play the arcade mode:

* Find one or more highlighted words in the game
* Get these words in the highlighted area by entering the associated word for them
* Keep doing this before you run out of space on your screen for new words

> _Also, there are three types of theme colors in arcade mode._

![Image](https://cdn-media-1.freecodecamp.org/images/1*FYMv5pI8NInQAp1jQK6EIg.jpeg)
_Semantris ARCADE theme colors_

You will realize that the theme color isn’t playing any role here — the game playing mechanism will remain the same if we change the theme color. What changes is the definition of the highlighted word.

> _A word is **highlighted** if it has a pointer shape left of it, (‎▶ **Ship**) in this case._

#### Color space conversion

ARCADE mode of Semantris-Solver starts with capturing a screenshot of the laptop screen and converting it into a gray-scale image, agnostic of the actual color.

![Image](https://cdn-media-1.freecodecamp.org/images/1*gP7jPgkVTBZz21TG5yu-7w.png)
_Semantris ARCADE mode (gray-scale)_

#### Template matching

Our next step will be to find the highlighted word in the captured image. OpenCV provides a method called [Template Matching](https://docs.opencv.org/3.3.0/d4/dc6/tutorial_py_template_matching.html) for searching and finding the location of a template image in a larger image.

We will use a cropped version of the pointer shape (▶) as a template image, to find its location in the captured screen.

![Image](https://cdn-media-1.freecodecamp.org/images/1*zEAmRMZ4gbh392Yq_rlZpQ.png)
_Semantris ARCADE highlighted word selection_

#### Optical character recognition (OCR)

![Image](https://cdn-media-1.freecodecamp.org/images/1*DzR7dHo936cLxjeCdPNqRw.png)
_Highlighted word image_

Based on the pointer’s location, a section is cropped right next to it, with the highlighted word.

The cropped image is converted into text using [Tesseract OCR](https://github.com/tesseract-ocr/tesseract); in this case, it will give us **Ship**.

> In case of more than one highlighted words, they are entered one after another to keep the game moving.

#### Associated word selection (Using Word Embeddings)

[Word2Vec pre-trained on Google News corpus](https://github.com/mmihaltz/word2vec-GoogleNews-vectors) is used as a word embedding model to find the [most similar](https://radimrehurek.com/gensim/models/word2vec.html#gensim.models.word2vec.Word2Vec.most_similar) words (associated) for a given word.

In this case, it will return “**vessel”** to enter as an associated word for “**ship”** (_after removing morphologically similar words_).

> _The program will enter this associated word and capture the updated game screen to continue._

### BLOCKS

In this mode, there are word-blocks with four possible colors for a given theme. The word-blocks might or might not contain a word in them.

Entering the associated word for a word-block will remove the same colored blocks connected to it, like the good old **Tetris**.

A human player will use the following moves to play the arcade mode:

* Enter the associated word for a word-block, connected with most same colored word-blocks (if possible)
* Keep doing this before you run out of space on your screen for new words

![Image](https://cdn-media-1.freecodecamp.org/images/1*3zS9PmEJFX47g2q4hfdDhg.png)
_Semantris BLOCKS mode captured screen_

You will realize that the color of a word-block is playing a significant role this time. You will have to enter the associated word for a word-block connected with more same colored blocks to score higher points.

> _On top of this, there are three types of theme colors in blocks mode._

![Image](https://cdn-media-1.freecodecamp.org/images/1*jHXOeWmDiepucJyO9eP-OQ.jpeg)
_Semantris BLOCKS theme colors_

#### Color palette generation

This time we can’t convert the captured image into its gray-scale version. We need to know the color attributes to be able to distinguish between different word-blocks.

Running **K-mean clustering** on the pixels of the captured screen will give us all the prominent colors in the image after excluding background colors such as white (text-color), black (background-color), and gray (text-input).

![Image](https://cdn-media-1.freecodecamp.org/images/1*I4GFZLlX2n1wLWM0UJgw4Q.png)
_Semantris BLOCKS theme color palette_

#### Contour detection

Now that we have all the four colors in the current theme, we need to know which word-block to choose to get maximum points.

In other words, if we calculate the area of every connected-word-block-group (_word-blocks of the same color connected to each other_) and select the one with the maximum area, we will get the desired connected-word-block-group.

> [_Contour_](https://docs.opencv.org/3.4/d4/d73/tutorial_py_contours_begin.html) _is a curve joining all the continuous points along a boundary, having same color or intensity._

A word-block group can be considered a contour of that color; if it’s connected to more blocks with the same color, the contour’s area will be the sum of the connected word-blocks.

![Image](https://cdn-media-1.freecodecamp.org/images/1*POkYHfLEMRfRwMVKV0KnVQ.png)
_Semantris BLOCKS mode with maximum area contour highlighted_

Contours are calculated (using OpenCV’s [findCountours](https://docs.opencv.org/3.3.1/d3/dc0/group__imgproc__shape.html#ga17ed9f5d79ae97bd4c7cf18403e1689a) function) for all the word-block colors separately and the one with the maximum area is selected.

We can select the maximum area contour by doing a bitwise-and operation between the captured screen and the contour mask.

![Image](https://cdn-media-1.freecodecamp.org/images/1*S5XyET4u8aBTd64IU5m-aw.png)
_Maximum area contour_

#### Word detection (Using Tesseract and Word2Vec)

The contour image is converted into text using [Tesseract OCR](https://github.com/tesseract-ocr/tesseract); in this case, it will give us **Garden**.

Similar to the arcade mode, we will use Word2Vec to find the most similar word to it, which will be **Flower beds** this time.

### Improvements

![Image](https://cdn-media-1.freecodecamp.org/images/1*tIgIoMSbvcmKj2yTXDuk1g.png)
_Contour with failing OCR_

In certain scenarios, the current OCR process doesn’t recognize the word properly.

For example, it would return “**Eloctrlclty”** for this contour instead of “**Electricity”**.

Given that it’s an invalid word suggestion, the Word2Vec model will not return any similar word for it. In that case, the suggested word itself is entered as an associated word, just to keep the game moving.

> A spelling correction model can help here, correcting **Eloctrlclty** to **Electricity.**

> _I have created an [issue](https://github.com/pravj/semantris-solver/issues/7) on the GitHub repository for the same, feel free to contribute if you like. ?_

### Source code

#### [Semantris-Solver](https://github.com/pravj/semantris-solver) (GitHub)

It’s implemented as a CLI tool that allows you to switch between the game modes. You can check the **IPython notebooks** implementing both the modes.

* [ARCADE mode](https://github.com/pravj/semantris-solver/blob/master/notebooks/Semantris%20Arcade%20Mode.ipynb)
* [BLOCKS mode](https://github.com/pravj/semantris-solver/blob/master/notebooks/Semantris%20Block%20Mode.ipynb)

#### Dependencies

It wasn’t possible to build Semantris-Solver without the following software tools.

* OpenCV
* Word2Vec (gensim)
* pyautogui (taking the screenshot and entering associated words)
* Tesseract (OCR)

Hope you liked my weekend hack story. Feel free to provide your feedback.

Follow me on Twitter [Pravendra Singh](https://www.freecodecamp.org/news/solving-googles-semantris-using-opencv-and-word2vec-7ea5eb36d0c7/undefined) or check my personal website [hackpravj.com](https://hackpravj.com).

