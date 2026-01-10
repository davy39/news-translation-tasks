---
title: How To Embed Multiple Choice Quiz Questions into Your Article
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-04-06T08:30:53.000Z'
originalURL: https://freecodecamp.org/news/multiple-choice-quiz-template
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9bc5740569d1a4ca2dcf.jpg
tags:
- name: blog
  slug: blog
- name: Blogging
  slug: blogging
seo_title: null
seo_desc: 'By Alexander Arobelidze

  In my experience, supplementing study with practical exercises greatly improves
  my understanding of a topic. This is especially true when I can test my knowledge
  as I go and receive instant feedback for each question.

  The mult...'
---

By Alexander Arobelidze

In my experience, supplementing study with practical exercises greatly improves my understanding of a topic. This is especially true when I can test my knowledge as I go and receive instant feedback for each question.

The multiple choice quiz format is perfect for this. I developed a method to embed multiple choice questions in the math articles I write for freeCodeCamp, and I want to show other authors how to do the same.

## How to add code to your article

The Ghost editor allows you to embed blocks of code throughout an article. The code editor can be accessed by clicking the round button with a plus sign **(+)** used for adding images, YouTube videos, and so on:

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-25.png)

Click on the "HTML" button to add an editor to the article. The editor supports HTML, CSS, and even JavaScript.

Once you start adding code, click anywhere outside the editor frame to render the code and view your progress. Double click on the rendered output to reopen the editor window:

![Image](https://www.freecodecamp.org/news/content/images/2020/04/editor.gif)

To test the functionality of your code, save the article by pressing Ctrl/⌘ + S, then click on the "View Preview" button that appears in the bottom left corner:

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-26.png)

Your article will open in a separate tab where you can see how your code will be rendered once your article is published. Take some time to check on the styling and functionality of your multiple choice quiz.

Boilerplate code for the multiple choice quiz is available in the next section. All you need to do is paste it into your own article and change the question and answers.

## How the multiple choice quiz works

You can add as many different questions as you want. However, while your article might have multiple quizzes, they're all contained within a **single HTML body** behind the scenes. Each question element starts with the following code:

```html
<div style='transform: scale(0.65); position: relative; top: -100px;'>
  <h3>WRITE YOUR QUESTION HERE</h3>
  <p>Choose 1 answer</p>
  <hr />
```

Each of the following `div` elements contains a possible answer:

```html
  ...
  <div id='block-11' style='padding: 10px;'>
    <label for='option-11' style=' padding: 5px; font-size: 2.5rem;'>
      <input type='radio' name='option' value='6/24' id='option-11' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' />
      ANSWER 1</label>
    <span id='result-11'></span>
  </div>
  <hr />

  <div id='block-12' style='padding: 10px;'>
    <label for='option-12' style=' padding: 5px; font-size: 2.5rem;'>
      <input type='radio' name='option' value='6' id='option-12' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' />
      ANSWER 2</label>
    <span id='result-12'></span>
  </div>
  <hr />
  ...
```

At the time of writing, Ghost's embedded code editor does not support template literals, so some things have to be hard coded. 

Remember that all the questions are essentially loaded together behind the scenes, so the two digit numbers in each `id` represent the following:

* The **first** digit indicates the order of the multiple choice question in the article (1 is question one, 2 is question two, and so on)
* The **second** digit indicates the order of each possible answer within its question block (1 is answer choice one, 2 is answer choice two, etc.)

For example, `block-12` represents **question** **1/answer choice 2**, while `block-43` is **question 4/answer choice 3**.

This indexing convention is necessary for different question blocks to function independently from each other.

Similar logic applies to the function names responsible for interactivity. The code that handles user interaction is placed within `<script>` tags and consists of two parts. First part is the function that evaluates answers and displays results: 

```js
function displayAnswer1() {
    if (document.getElementById('option-11').checked) {
      document.getElementById('block-11').style.border = '3px solid limegreen'
      document.getElementById('result-11').style.color = 'limegreen'
      document.getElementById('result-11').innerHTML = 'Correct!'
    }
    if (document.getElementById('option-12').checked) {
      document.getElementById('block-12').style.border = '3px solid red'
      document.getElementById('result-12').style.color = 'red'
      document.getElementById('result-12').innerHTML = 'Incorrect!'
      showCorrectAnswer1()
    }
    if (document.getElementById('option-13').checked) {
      document.getElementById('block-13').style.border = '3px solid red'
      document.getElementById('result-13').style.color = 'red'
      document.getElementById('result-13').innerHTML = 'Incorrect!'
      showCorrectAnswer1()
    }
    if (document.getElementById('option-14').checked) {
      document.getElementById('block-14').style.border = '3px solid red'
      document.getElementById('result-14').style.color = 'red'
      document.getElementById('result-14').innerHTML = 'Incorrect!'
      showCorrectAnswer1()
    }
  }
```

Like the name suggests, the `displayAnswer1` function handles the first question within an article. If there's a third question in your article, `displayAnswer3` will handle it.

In the example above, `option-11` is the correct answer, and the styling in the first `if` block is updated to show the right answer was selected. If any of the other incorrect answers are selected, the styling is updated to reflect that.

Feel free to play with the `displayAnswer_` functions in your own article. Just remember to attach the appropriate styling to the correct and incorrect answers.

Here's the second part of the code that handles user interaction:

```js
function showCorrectAnswer1() {
    let showAnswer1 = document.createElement('p')
    showAnswer1.innerHTML = 'Show Corrent Answer'
    showAnswer1.style.position = 'relative'
    showAnswer1.style.top = '-180px'
    showAnswer1.style.fontSize = '1.75rem'
    document.getElementById('showanswer1').appendChild(showAnswer1)
    showAnswer1.addEventListener('click', () => {
      document.getElementById('block-11').style.border = '3px solid limegreen'
      document.getElementById('result-11').style.color = 'limegreen'
      document.getElementById('result-11').innerHTML = 'Correct!'
      document.getElementById('showanswer1').removeChild(showAnswer1)
    })
  }
```

This function is called `showCorrectAnswer1` because it handles the first multiple choice question in the article. You'll have to add `showCorrectAnswer2`, `showCorrectAnswer3`, and more if your article has more than one question.

Please play around with the styling and dimensions used throughout the code, and customize it to your taste. Also, I'm sure there are other ways to implement multiple choice quizzes, but this is mine, and I'm happy to share it with you.

Here's the full code and a working example:

```html
<div style='transform: scale(0.65); position: relative; top: -100px;'>
  <h3>What fraction of a day is 6 hours?</h3>
  <p>Choose 1 answer</p>
  <hr />

  <div id='block-11' style='padding: 10px;'>
    <label for='option-11' style=' padding: 5px; font-size: 2.5rem;'>
      <input type='radio' name='option' value='6/24' id='option-11' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' />
      6/24</label>
    <span id='result-11'></span>
  </div>
  <hr />

  <div id='block-12' style='padding: 10px;'>
    <label for='option-12' style=' padding: 5px; font-size: 2.5rem;'>
      <input type='radio' name='option' value='6' id='option-12' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' />
      6</label>
    <span id='result-12'></span>
  </div>
  <hr />

  <div id='block-13' style='padding: 10px;'>
    <label for='option-13' style=' padding: 5px; font-size: 2.5rem;'>
      <input type='radio' name='option' value='1/3' id='option-13' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' />
      1/3</label>
    <span id='result-13'></span>
  </div>
  <hr />

  <div id='block-14' style='padding: 10px;'>
    <label for='option-14' style=' padding: 5px; font-size: 2.5rem;'>
      <input type='radio' name='option' value='1/6' id='option-14' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' />
      1/6</label>
    <span id='result-14'></span>
  </div>
  <hr />
  <button type='button' onclick='displayAnswer1()' style='width: 100px; height: 40px; border-radius: 3px; background-color: lightblue; font-weight: 700;'>Submit</button>
</div>
<a id='showanswer1'></a>
<script>
  //    The function evaluates the answer and displays result
  function displayAnswer1() {
    if (document.getElementById('option-11').checked) {
      document.getElementById('block-11').style.border = '3px solid limegreen'
      document.getElementById('result-11').style.color = 'limegreen'
      document.getElementById('result-11').innerHTML = 'Correct!'
    }
    if (document.getElementById('option-12').checked) {
      document.getElementById('block-12').style.border = '3px solid red'
      document.getElementById('result-12').style.color = 'red'
      document.getElementById('result-12').innerHTML = 'Incorrect!'
      showCorrectAnswer1()
    }
    if (document.getElementById('option-13').checked) {
      document.getElementById('block-13').style.border = '3px solid red'
      document.getElementById('result-13').style.color = 'red'
      document.getElementById('result-13').innerHTML = 'Incorrect!'
      showCorrectAnswer1()
    }
    if (document.getElementById('option-14').checked) {
      document.getElementById('block-14').style.border = '3px solid red'
      document.getElementById('result-14').style.color = 'red'
      document.getElementById('result-14').innerHTML = 'Incorrect!'
      showCorrectAnswer1()
    }
  }
  // the functon displays the link to the correct answer
  function showCorrectAnswer1() {
    let showAnswer1 = document.createElement('p')
    showAnswer1.innerHTML = 'Show Corrent Answer'
    showAnswer1.style.position = 'relative'
    showAnswer1.style.top = '-180px'
    showAnswer1.style.fontSize = '1.75rem'
    document.getElementById('showanswer1').appendChild(showAnswer1)
    showAnswer1.addEventListener('click', () => {
      document.getElementById('block-11').style.border = '3px solid limegreen'
      document.getElementById('result-11').style.color = 'limegreen'
      document.getElementById('result-11').innerHTML = 'Correct!'
      document.getElementById('showanswer1').removeChild(showAnswer1)
    })
  }
</script>
```

<div style='transform: scale(0.65); position: relative; top: -100px;'>
  <h3>What fraction of a day is 6 hours?</h3>
  <p>Choose 1 answer</p>
  <hr />

  <div id='block-11' style='padding: 10px;'>
    <label for='option-11' style=' padding: 5px; font-size: 2.5rem;'>
      <input type='radio' name='option' value='6/24' id='option-11' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' />
      6/24</label>
    <span id='result-11'></span>
  </div>
  <hr />

  <div id='block-12' style='padding: 10px;'>
    <label for='option-12' style=' padding: 5px; font-size: 2.5rem;'>
      <input type='radio' name='option' value='6' id='option-12' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' />
      6</label>
    <span id='result-12'></span>
  </div>
  <hr />

  <div id='block-13' style='padding: 10px;'>
    <label for='option-13' style=' padding: 5px; font-size: 2.5rem;'>
      <input type='radio' name='option' value='1/3' id='option-13' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' />
      1/3</label>
    <span id='result-13'></span>
  </div>
  <hr />

  <div id='block-14' style='padding: 10px;'>
    <label for='option-14' style=' padding: 5px; font-size: 2.5rem;'>
      <input type='radio' name='option' value='1/6' id='option-14' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' />
      1/6</label>
    <span id='result-14'></span>
  </div>
  <hr />
  <button type='button' onclick='displayAnswer1()' style='width: 100px; height: 40px; border-radius: 3px; background-color: lightblue; font-weight: 700;'>Submit</button>
</div>
<a id='showanswer1'></a>
<script>
  //    The function evaluates the answer and displays result
  function displayAnswer1() {
    if (document.getElementById('option-11').checked) {
      document.getElementById('block-11').style.border = '3px solid limegreen'
      document.getElementById('result-11').style.color = 'limegreen'
      document.getElementById('result-11').innerHTML = 'Correct!'
    }
    if (document.getElementById('option-12').checked) {
      document.getElementById('block-12').style.border = '3px solid red'
      document.getElementById('result-12').style.color = 'red'
      document.getElementById('result-12').innerHTML = 'Incorrect!'
      showCorrectAnswer1()
    }
    if (document.getElementById('option-13').checked) {
      document.getElementById('block-13').style.border = '3px solid red'
      document.getElementById('result-13').style.color = 'red'
      document.getElementById('result-13').innerHTML = 'Incorrect!'
      showCorrectAnswer1()
    }
    if (document.getElementById('option-14').checked) {
      document.getElementById('block-14').style.border = '3px solid red'
      document.getElementById('result-14').style.color = 'red'
      document.getElementById('result-14').innerHTML = 'Incorrect!'
      showCorrectAnswer1()
    }
  }
  // the functon displays the link to the correct answer
  function showCorrectAnswer1() {
    let showAnswer1 = document.createElement('p')
    showAnswer1.innerHTML = 'Show Corrent Answer'
    showAnswer1.style.position = 'relative'
    showAnswer1.style.top = '-180px'
    showAnswer1.style.fontSize = '1.75rem'
    document.getElementById('showanswer1').appendChild(showAnswer1)
    showAnswer1.addEventListener('click', () => {
      document.getElementById('block-11').style.border = '3px solid limegreen'
      document.getElementById('result-11').style.color = 'limegreen'
      document.getElementById('result-11').innerHTML = 'Correct!'
      document.getElementById('showanswer1').removeChild(showAnswer1)
    })
  }
</script>

You can also find the complete boilerplate code [here on GitHub](https://github.com/sandroarobeli/quiz-template/blob/master/testTemplateHTML.txt).

