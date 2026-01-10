---
title: 'Permutation and Combination: The Difference Explained with Formula Examples'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-04-23T17:34:42.000Z'
originalURL: https://freecodecamp.org/news/permutation-and-combination-the-difference-explained-with-formula-examples
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9b7e740569d1a4ca2c26.jpg
tags:
- name: Mathematics
  slug: mathematics
- name: General Programming
  slug: programming
seo_title: null
seo_desc: 'By Alexander Arobelidze

  Permutations and Combinations are super useful in so many applications – from Computer
  Programming to Probability Theory to Genetics.

  I''m going to introduce you to these two concepts side-by-side, so you can see how
  useful the...'
---

By Alexander Arobelidze

Permutations and Combinations are super useful in so many applications – from Computer Programming to Probability Theory to Genetics.

I'm going to introduce you to these two concepts side-by-side, so you can see how useful they are.

The key difference between these two concepts is ordering. With **Permutations**, you focus on **lists** of elements where their order matters.

For example, I was born in **1977**. That's number **1** followed by number **9**, followed by number **7**, followed by number **7**. In that particular order.

If I change the order to **7917** instead, that would be a completely different year. Thus, the order **matters**.

With **Combinations** on the other hand, the focus is on **groups** of elements where the order does **not** matter.

Like my cup of coffee is a combination of **coffee**, **sugar** and **water**. It doesn't matter which order I add these ingredients are in. There may as well be **water**, **sugar** and **coffee**, it's still the same cup of coffee. Thus, the order does **not** matter.

Now let's take a closer look at these concepts.

## Part 1: Permutations

### Permutations Where Repetition is Allowed

Imagine you got a new phone. As you start using this new phone, at some point you will be asked to set up a password. 

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-173.png)
_Image of a smartphone screen_

The password must consist of **4** digits. Any 4 digits. And they may be repeated.

There are **10** digits in total to begin with. Those are: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9. So for the first digit of your password, you have **10** choices. 

Since you may use the same digit again, the number of choices for the second digit of our password will be **10** again! Thus, choosing two of the password digits so far, the permutations are **10 times 10,** or **10 x 10 = 100** or **10<sup>2</sup>**. 

The same thinking goes for the third digit of your password. You get to choose from the same 10 choices again. This time you will have **10 times 10 times 10**, or **10 x 10 x 10 = 1,000** or **10<sup>3</sup>** permutations. 

At last, for the fourth digit of the password and the same 10 digits to choose from, we end up with **10 times 10 times 10 times 10**, or **10 x 10 x 10 x 10 = 10,000** or **10<sup>4</sup>** permutations. 

As you probably noticed, you had 4 choices to make and you multiplied 10 **four** times (10 x 10 x 10 x 10) to arrive at a total number of permutations (10,000). If you had to choose **3** digits for your password, you would multiply 10 **three** times. If **7**, you would do it **seven** times, and so on.

But life isn't all about passwords with digits to choose from. What if you have a birthday party and need to choose **5** colored balloons from **20** different colors available? 

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-175.png)
_image of colored balloons_

Since you have 20 different colors to choose from and may choose the same color again, for each balloon you have **20** choices. The first balloon is **20**, the second balloon is **20 times 20**, or **20 x 20 = 400** etc. For the fifth balloon you get **20 x 20 x 20 x 20 x 20 = 3,200,000** or **20<sup>5</sup>** permutations. 

Let's summarize with the general rule: when order matters and repetition is allowed, if **n** is the number of things to choose from (balloons, digits etc), and you choose **r** of them (5 balloons for the party, 4 digits for the password, etc.), the number of permutations will equal **P = n<sup>r</sup>**.

### Permutations Where Repetition Isn't Allowed

Next, let's consider the case where **repetition is not allowed**. As an example, we will look at the planets of our solar system. 

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-174.png)
_image of solar system planets_

How many different ways can you arrange these **8** planets? The planets are: **Mercury**, **Venus**, **Earth**, **Mars**, **Jupiter**, **Saturn**, **Uranus** and **Neptune**. After choosing, say, Mercury you can't choose it again. Thus, you have to reduce the number of available choices each time the planet is chosen. 

The first choice will have **8** possibilities. The second choice will have **8 minus 1 equals 7** possibilities, then **6**, followed by **5**, followed by **4,** until we have **1** planet left in the list.

Following the logic from the previous scenario, the total number of permutations is: **P = 8 x 7 x 6 x 5 x 4 x 3 x 2 x 1 = 40,320**.

In other words, this is a product of integer 8 and all the positive integers below it. This product is called **Factorial** and is denoted with an exclamation point, like this: **8!**

The number of permutations equals **P = 8!** or more generally **P = n!**

What if you only need to arrange, say, **5** out of these **8** planets instead of all of them? Then you only take the **first 5** steps in our method. Namely, **P = 8 x 7 x 6 x 5 x 4 = 6,720** will be how many ways you can arrange **5** planets out of **8**. 

But why stop here? Why not apply our logic to come up with a more general formula? To make the above notation easy to remember for any numbers of objects, we will use a trick. In a fraction, multiplying both numerator and denominator by the same number (except zero), does not affect that fraction. Thus: 

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Permutations1.png)
_P(n, r) = n! / (n - r)!_

Number of planets to choose from **n = 8**, you choose **r = 5** of them. Substituting the numbers into above formula gives us **P = 8! / (8 - 5)! = 8! / 3!**. Same as **8 x 7 x 6 x 5 x 4 = 6,720**. 

From here, the result from earlier example can be derived. There, you arranged all **8** out of **8** available planets. Using the new formula, **P = 8! / (8 - 8)! = 8! / 0!**. Since, factorial of **zero** is agreed to **equal 1**, **P = 8! / 1 = 8!.** Or more generally:

**P = n! / (n - n)! = n! / 0! = n!**.  

One short and convenient notation often used is: **P(n, r) = n! / (n - r)!** 

Remembering formulas is important. But what's more important for solving real life problems is to know which formulas to use in each situation. Practice helps.

Pop quiz:

<!-- Code for Multiple Choice questions and evaluating answers
 Editor does not support template string, so functionalily had to be hard  coded. Since each question-answer block is still a part of a single HTML code  instance, element IDs and function names had to be indexed.

Displays a question with for possible clickable answers -->
<div style='transform: scale(0.65); position: relative; top: -100px;'>
<h3>The tournament is on and six teams are competing. First place gets gold and second place gets silver medals. How many distinct ways can medals be awarded to these teams?</h3>	
    <p>Choose 1 answer</p>
    <hr/>
   
    <div id='block-11' style='padding: 10px;'>
   <label for='option-11' style=' padding: 5px; font-size: 2.5rem;'>
        <input type='radio' name='option' value='6/24' id='option-11' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 
        30</label>
        <span id='result-11'></span>
    </div>
    <hr/>
    
    <div id='block-12' style='padding: 10px;'>
    <label for='option-12' style=' padding: 5px; font-size: 2.5rem;'>
        <input type='radio' name='option' value='6' id='option-12' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 				
        360</label>
        <span id='result-12'></span>
    </div>	
    <hr/>
     
    <div id='block-13' style='padding: 10px;'>
    <label for='option-13' style=' padding: 5px; font-size: 2.5rem;'>
        <input type='radio' name='option' value='1/3' id='option-13' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 				
        720</label>
        <span id='result-13'></span>
    </div>
    <hr/>
     
    <div id='block-14' style='padding: 10px;'>
        <label for='option-14' style=' padding: 5px; font-size: 2.5rem;'>
         <input type='radio' name='option' value='1/6' id='option-14' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 				
         15</label>
        <span id='result-14'></span>
    </div>
    <hr/>
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

Explanation: you have **6** teams to choose from. Thus **n = 6**. Gold and silver together give you **2** medals to award. Thus **r = 2**. Substituting these numbers into your formula gives us **P(6, 2) = 6! / (6 - 2)! = 6! / 4! = 6 x 5 = 30**. 

## Part 2. Combinations

### Combinations Without Repetition

To make the comparison more vivid, let's revisit our planet selection example. What if you want to know just which planets are chosen and **not** their order of appearance? 

There you had 6,720 distinct ways of arranging 5 out of 8 planets. But since the order of appearance does **not** matter now, many of these ways are **redundant**. They are the same to us.

A **group** of Venus, Earth, Mars, Jupiter, Saturn is the same **group** as Mars, Jupiter, Venus, Earth, Saturn and the **group** as Saturn, Mars, Earth, Jupiter, Venus. These are just different sequences of the same 5 planets.

How many groups do you have that are the same? If you choose **r** planets per group, you get **r!** groups. For **r = 5**, you get **r! = 5! = 120** groups.

Thus, to eliminate the unnecessary groups that are the same, you divide the number of original **6,720** Permutations by **5!**. The result is 6,720 / 120 = **56**. 

To generalize, in order to arrive at the number of **Combinations**, you need to figure out all the **Permutations** and divide by all the **Redundancies**.

Using short and convenient notation: **C(n, r) = P(n, r) / r! = n! / (r!(n - r)!)**

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Permutations2.png)
_C(n, r) = n! / (r!(n - r)!)_

And this assumes that order does **not** matter and there are **no** repetitions (that is – there is only one Jupiter to choose from).

Let's revisit the tournament example:

<!-- Code for Multiple Choice questions and evaluating answers
 Editor does not support template string, so functionalily had to be hard  coded. Since each question-answer block is still a part of a single HTML code  instance, element IDs and function names had to be indexed.

Displays a question with for possible clickable answers -->
<div style='transform: scale(0.65); position: relative; top: -100px;'>
<h3>The tournament is on and six teams are competing. First place gets gold and second place gets silver medals. How many groups of medal winners are possible? Order of teams doesn't matter</h3>	
    <p>Choose 1 answer</p>
    <hr/>
   
    <div id='block-21' style='padding: 10px;'>
   <label for='option-21' style=' padding: 5px; font-size: 2.5rem;'>
        <input type='radio' name='option' value='6/24' id='option-21' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 
        360</label>
        <span id='result-21'></span>
    </div>
    <hr/>
    
    <div id='block-22' style='padding: 10px;'>
    <label for='option-22' style=' padding: 5px; font-size: 2.5rem;'>
        <input type='radio' name='option' value='6' id='option-22' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 				
        15</label>
        <span id='result-22'></span>
    </div>	
    <hr/>
     
    <div id='block-23' style='padding: 10px;'>
    <label for='option-23' style=' padding: 5px; font-size: 2.5rem;'>
        <input type='radio' name='option' value='1/3' id='option-23' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 				
        30</label>
        <span id='result-23'></span>
    </div>
    <hr/>
     
    <div id='block-24' style='padding: 10px;'>
        <label for='option-24' style=' padding: 5px; font-size: 2.5rem;'>
         <input type='radio' name='option' value='1/6' id='option-24' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 				
         720</label>
        <span id='result-24'></span>
    </div>
    <hr/>
    <button type='button' onclick='displayAnswer2()' style='width: 100px; height: 40px; border-radius: 3px; background-color: lightblue; font-weight: 700;'>Submit</button>
</div>
<a id='showanswer2'></a>
<script>
    
 //    The function evaluates the answer and displays result
	function displayAnswer2() {
    	if (document.getElementById('option-22').checked) {
      
        document.getElementById('block-22').style.border = '3px solid limegreen'
        document.getElementById('result-22').style.color = 'limegreen'
		document.getElementById('result-22').innerHTML = 'Correct!'
        
        } 
        if (document.getElementById('option-21').checked) {
        document.getElementById('block-21').style.border = '3px solid red'
        document.getElementById('result-21').style.color = 'red'
		document.getElementById('result-21').innerHTML = 'Incorrect!'
        showCorrectAnswer2()
 		}
        if (document.getElementById('option-23').checked) {
        document.getElementById('block-23').style.border = '3px solid red'
        document.getElementById('result-23').style.color = 'red'
		document.getElementById('result-23').innerHTML = 'Incorrect!'
        showCorrectAnswer2()	
        }
        if (document.getElementById('option-24').checked) {
        document.getElementById('block-24').style.border = '3px solid red'
        document.getElementById('result-24').style.color = 'red'
		document.getElementById('result-24').innerHTML = 'Incorrect!'
        showCorrectAnswer2() 	
        }
     }
    // the functon displays the link to the correct answer
    function showCorrectAnswer2() {
        	 let showAnswer2 = document.createElement('p')
             showAnswer2.innerHTML = 'Show Corrent Answer'
        showAnswer2.style.position = 'relative'
        showAnswer2.style.top = '-180px'
        showAnswer2.style.fontSize = '1.75rem'
             document.getElementById('showanswer2').appendChild(showAnswer2)
             showAnswer2.addEventListener('click', () => {
        	 document.getElementById('block-22').style.border = '3px solid limegreen'
        document.getElementById('result-22').style.color = 'limegreen'
		document.getElementById('result-22').innerHTML = 'Correct!'
        document.getElementById('showanswer2').removeChild(showAnswer2)    
         
        })
        }
</script>

As before, you have **6** teams. Thus, **n = 6**. There are two medals awarded, so **r = 2**. However, this time it **doesn't** matter who wins gold and who wins silver. Team gold and team silver is the same as team silver and team gold. Substituting these numbers into your formula gives us **C(6, 2) = 6! / (2!(6 - 2)!) = 6! / 2! 4! = 15**.

### Combinations with Repetition

To complete this article, there is one case that requires special attention. So far in our Combinations we assumed there was no repetition. No two items were the same. 

What if we **can** have repetitions? What if, as in our earlier example, we can choose more than one balloon of the same color? If the number of balloons to choose from is **n** and we choose **r** of them while **allowing** for same colors and **disregarding** the order of arrangement, we will end up with **(n + r - 1)! / (r!(n - 1)!) Combinations**.

So wrapping up, here is a table you can use to reference these concepts and their formulas.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Permutations3.png)
_Table of formulas for Permutations and Combinations_

 I hope this article has helped you better understand these two important mathematical concepts. Thanks for reading.

