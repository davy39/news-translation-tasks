---
title: 'Fraction Math: How to Do Fractions for Beginners'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-03-11T18:57:45.000Z'
originalURL: https://freecodecamp.org/news/fraction-math-how-to-do-fractions-for-beginners
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9c2f740569d1a4ca3077.jpg
tags:
- name: fractions
  slug: fractions
- name: Math
  slug: math
seo_title: null
seo_desc: 'By Alexander Arobelidze

  We deal with fractions every day. But what exactly is a fraction? How do we get
  to know them better? In this tutorial we will explore the basics and practice together,
  so fractions can become valuable helpers in everyday life ...'
---

By Alexander Arobelidze

We deal with fractions every day. But what exactly is a fraction? How do we get to know them better? In this tutorial we will explore the basics and practice together, so fractions can become valuable helpers in everyday life and beyond. 

## Part 1. Fraction as a share

Let's imagine a whole pie divided into 4 equal parts. One part is shaded red.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/fraction1.png)
_image of a circle with one quarter shaded red_

**One** red part out of **four** equal parts means **1/4** of a whole is shaded. If we think of equal parts of a whole as shares, one share of a pie here is shaded red. 

![Image](https://www.freecodecamp.org/news/content/images/2020/03/fraction2.png)
_drawing of a fraction 1/4. 1 is a Numerator, 4 is a Denominator_

The number 1 **above** the line is called a **Numerator**. It shows how many shares are shaded. The number 4 **below** the line is called a **Denominator**. It shows how many **equal** shares a whole is divided into. Let's look at another example.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/fractions3.png)
_image of a circle with three sixths shaded red_

The new pie above is divided into **6** equal shares. Therefore, the denominator will equal 6. Out of these 6 equal shares **3** are shaded red. Therefore, the numerator will equal 3. In other words, **3/6** of the pie is shaded. 

Now let's test what we have learned so far. As you know, there are 24 hours in a whole day. If you spent 6 hours studying, what fraction of the day did you spend studying? 

<!-- Code for Multiple Choice questions and evaluating answers
 Editor does not support template string, so functionalily had to be hard  coded. Since each question-answer block is still a part of a single HTML code  instance, element IDs and function names had to be indexed.

Displays a question with for possible clickable answers -->
<div style='transform: scale(0.65); position: relative; top: -100px;'>
<h3>What fraction of a day is 6 hours?</h3>	
    <p>Choose 1 answer</p>
    <hr/>
   
    <div id='block-11' style='padding: 10px;'>
   <label for='option-11' style=' padding: 5px; font-size: 2.5rem;'>
        <input type='radio' name='option' value='6/24' id='option-11' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 
        6/24</label>
        <span id='result-11'></span>
    </div>
    <hr/>
    
    <div id='block-12' style='padding: 10px;'>
    <label for='option-12' style=' padding: 5px; font-size: 2.5rem;'>
        <input type='radio' name='option' value='6' id='option-12' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 				
        6</label>
        <span id='result-12'></span>
    </div>	
    <hr/>
     
    <div id='block-13' style='padding: 10px;'>
    <label for='option-13' style=' padding: 5px; font-size: 2.5rem;'>
        <input type='radio' name='option' value='1/3' id='option-13' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 				
        1/3</label>
        <span id='result-13'></span>
    </div>
    <hr/>
     
    <div id='block-14' style='padding: 10px;'>
        <label for='option-14' style=' padding: 5px; font-size: 2.5rem;'>
         <input type='radio' name='option' value='1/6' id='option-14' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 				
         1/6</label>
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

A day is divided into **24** equal shares called hours. So the Denominator will be 24. Think of the 6 hours spent studying as **6** shaded shares of the pie. That will make the Numerator equal 6. The fraction we are looking for is **6/24**.

## Part 2. Simplifying fractions

Remember the pie from previous example? It had 3/6 of it shaded red. Let's add two new pies and look at them together.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/fractions4.png)
_image of 3 circles with half of each painted red_

The first pie is divided into 4 shares and two are shaded red. But as we can see that's half the pie. The second pie is divided into 6 shares and three are shaded red. Half of the pie again. Finally, the third pie is divided into two halves and one half is shaded red. 

Since it's **half** a pie that's shaded in either case, we can conclude that the fractions are equal: **2/4 = 3/6 = 1/2**. 

![Image](https://www.freecodecamp.org/news/content/images/2020/03/fraction5.png)
_image of 3 circles with half of each painted red. 2/4 = 3/6 = 1/2_

Finally, by multiplying or dividing both the numerator and denominator by the **same** number, the fraction will stay the same (except the case when division is by zero, which is outside of the scope of this article and will not be considered here). 

This rule helps simplify fractions and makes using them easier. As an example, let's consider 4/12. Dividing numerator and denominator by 4 gives us (4 : **4**) / (12 : **4**) = 1 / 3. It's time to test your knowledge.

<!-- Code for Multiple Choice questions and evaluating answers
 Editor does not support template string, so functionalily had to be hard  coded. Since each question-answer block is still a part of a single HTML code  instance, element IDs and function names had to be indexed.

Displays a question with for possible clickable answers -->
<div style='transform: scale(0.65); position: relative; top: -100px;'>
<h3>What fraction is the same as 2/5?</h3>	
    <p>Choose 1 answer</p>
    <hr/>
   
    <div id='block-21' style='padding: 10px;'>
   <label for='option-21' style=' padding: 5px; font-size: 2.5rem;'>
        <input type='radio' name='option' value='6/24' id='option-21' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 
        4/25</label>
        <span id='result-21'></span>
    </div>
    <hr/>
    
    <div id='block-22' style='padding: 10px;'>
    <label for='option-22' style=' padding: 5px; font-size: 2.5rem;'>
        <input type='radio' name='option' value='6' id='option-22' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 				
        5/2</label>
        <span id='result-22'></span>
    </div>	
    <hr/>
     
    <div id='block-23' style='padding: 10px;'>
    <label for='option-23' style=' padding: 5px; font-size: 2.5rem;'>
        <input type='radio' name='option' value='1/3' id='option-23' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 				
        8/20</label>
        <span id='result-23'></span>
    </div>
    <hr/>
     
    <div id='block-24' style='padding: 10px;'>
        <label for='option-24' style=' padding: 5px; font-size: 2.5rem;'>
         <input type='radio' name='option' value='1/6' id='option-24' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 				
         6/10</label>
        <span id='result-24'></span>
    </div>
    <hr/>
    <button type='button' onclick='displayAnswer2()' style='width: 100px; height: 40px; border-radius: 3px; background-color: lightblue; font-weight: 700;'>Submit</button>
</div>
<a id='showanswer2'></a>
<script>
    
 //    The function evaluates the answer and displays result
	function displayAnswer2() {
    	if (document.getElementById('option-23').checked) {
      
        document.getElementById('block-23').style.border = '3px solid limegreen'
        document.getElementById('result-23').style.color = 'limegreen'
		document.getElementById('result-23').innerHTML = 'Correct!'
        
        } 
        if (document.getElementById('option-21').checked) {
        document.getElementById('block-21').style.border = '3px solid red'
        document.getElementById('result-21').style.color = 'red'
		document.getElementById('result-21').innerHTML = 'Incorrect!'
        showCorrectAnswer2()
 		}
        if (document.getElementById('option-22').checked) {
        document.getElementById('block-22').style.border = '3px solid red'
        document.getElementById('result-22').style.color = 'red'
		document.getElementById('result-22').innerHTML = 'Incorrect!'
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
        	 document.getElementById('block-23').style.border = '3px solid limegreen'
        document.getElementById('result-23').style.color = 'limegreen'
		document.getElementById('result-23').innerHTML = 'Correct!'
        document.getElementById('showanswer2').removeChild(showAnswer2)    
         
        })
        }
</script>

## Part 3. Comparing fractions

When we see two pieces of a pie, we can usually tell which one is larger. Similarly with fractions, there is a simple way of comparing them to each other. 

Say we need to compare 1/3 and 2/7. Since they have different denominators, they have a different number of parts. So the **First step** must be to find the **common ground**. We do it by finding a **common denominator**. 

One of the methods for finding a common denominator of two or more fractions is to multiply the denominators with each other. **3** times **7** = **21**. 

Now that we found the common denominator, we need to replace each fraction's own denominator with the common denominator. 

![Image](https://www.freecodecamp.org/news/content/images/2020/03/fraction6.png)
_bringing 1/3 and 2/7 to the common denominator_

The first fraction is 1/3, so we divide 21 by 3 and resulting **7** gets multiplied by that fractions numerator. Since the numerator equals 1, we get **7 times 1 = 7**. 

The second fraction is 2/7, so 21 divided by 7 results in 3. Multiplying 3 times this fractions numerator, gives us **3 times 2 = 6**.  

Now that the fractions have the same denominator, we can finally compare them. 7 shares is more than 6 shares, therefore 7/21 is greater than 6/21. 

The mathematical symbol denoting our result is the **>** sign. **7/21 > 6/21**. It is read as  "**greater-than**." The symbol denoting **lesser-than** looks like this: **<**. We can rewrite our result like this: **6/21 < 7/21**. 

<!-- Code for Multiple Choice questions and evaluating answers
 Editor does not support template string, so functionalily had to be hard  coded. Since each question-answer block is still a part of a single HTML code  instance, element IDs and function names had to be indexed.

Displays a question with for possible clickable answers -->
<div style='transform: scale(0.65); position: relative; top: -100px;'>
<h3>Compare 3/4 and 5/7</h3>	
    <p>Choose 1 answer</p>
    <hr/>
   
    <div id='block-31' style='padding: 10px;'>
   <label for='option-31' style=' padding: 5px; font-size: 2.5rem;'>
        <input type='radio' name='option' value='5/7' id='option-31' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 
        3/4 is less than 5/7</label>
        <span id='result-31'></span>
    </div>
    <hr/>
    
    <div id='block-32' style='padding: 10px;'>
    <label for='option-32' style=' padding: 5px; font-size: 2.5rem;'>
        <input type='radio' name='option' value='3/4' id='option-32' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 				
        3/4 is greater than 5/7</label>
        <span id='result-32'></span>
    </div>	
    <hr/>
     
    <div id='block-33' style='padding: 10px;'>
    <label for='option-33' style=' padding: 5px; font-size: 2.5rem;'>
        <input type='radio' name='option' value='1' id='option-33' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 				
        3/4 equals 5/7</label>
        <span id='result-33'></span>
    </div>
    <hr/>
     
    <div id='block-34' style='padding: 10px;'>
        <label for='option-34' style=' padding: 5px; font-size: 2.5rem;'>
         <input type='radio' name='option' value='0' id='option-34' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 				
         They Cannot be compared</label>
        <span id='result-34'></span>
    </div>
    <hr/>
    <button type='button' onclick='displayAnswer3()' style='width: 100px; height: 40px; border-radius: 3px; background-color: lightblue; font-weight: 700;'>Submit</button>
</div>
<a id='showanswer3'></a>
<script>
    
 //    The function evaluates the answer and displays result
	function displayAnswer3() {
    	if (document.getElementById('option-32').checked) {
      
        document.getElementById('block-32').style.border = '3px solid limegreen'
        document.getElementById('result-32').style.color = 'limegreen'
		document.getElementById('result-32').innerHTML = 'Correct!'
        
        } 
        if (document.getElementById('option-31').checked) {
        document.getElementById('block-31').style.border = '3px solid red'
        document.getElementById('result-31').style.color = 'red'
		document.getElementById('result-31').innerHTML = 'Incorrect!'
        showCorrectAnswer3()
 		}
        if (document.getElementById('option-33').checked) {
        document.getElementById('block-33').style.border = '3px solid red'
        document.getElementById('result-33').style.color = 'red'
		document.getElementById('result-33').innerHTML = 'Incorrect!'
        showCorrectAnswer3()	
        }
        if (document.getElementById('option-34').checked) {
        document.getElementById('block-34').style.border = '3px solid red'
        document.getElementById('result-34').style.color = 'red'
		document.getElementById('result-34').innerHTML = 'Incorrect!'
        showCorrectAnswer3() 	
        }
     }
    // the functon displays the link to the correct answer
    function showCorrectAnswer3() {
        	 let showAnswer3 = document.createElement('p')
             showAnswer3.innerHTML = 'Show Corrent Answer'
        showAnswer3.style.position = 'relative'
        showAnswer3.style.top = '-180px'
        showAnswer3.style.fontSize = '1.75rem'
             document.getElementById('showanswer3').appendChild(showAnswer3)
             showAnswer3.addEventListener('click', () => {
        	 document.getElementById('block-32').style.border = '3px solid limegreen'
        document.getElementById('result-32').style.color = 'limegreen'
		document.getElementById('result-32').innerHTML = 'Correct!'
        document.getElementById('showanswer3').removeChild(showAnswer3)    
         
        })
        }
</script>

## Part 4. Adding fractions

To add fractions, we again need to find a common denominator. Let's look at the following example. 

We need to add **2/7** and **3/9**. The common denominator is **7 times 9 = 63**. The next step would be to replace each fraction's own denominator with the common one. 

For the first fraction, **63 divided by 7 = 9** and **9 times 2 = 18**. The result is **18/63**. For the second one, **63 divided by 9 = 7** and **7 times 3 = 21**. The result is **21/63**. 

Next, we add the numerators. **18 plus 21 = 39,** which leaves us with the sum of **39/63**. 

As a useful habit, always check if the resulting fraction can be further simplified. 

We know that 39 is evenly divisible by 3. 63 is also evenly divisible by 3. Since both numerator and denominator are divided by the same number, the fraction will remain the same. **39 divided by 3 = 13** and **63 divided by 3 = 21**. Our final result is **13/21**.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/fraction7.png)
_Fraction addition calculation 2/7 + 3/9 = 39/63 = 13/21_

What if we need to add mixed numbers? To add mixed numbers, we first add the whole numbers together and then the fractions. 

For example, to add **1 and a half** to **2 and a half**, add **1 and 2 = 3**, then add **1/2 and 1/2 = 1**. Finally, **add 3 and 1 = 4**. Let's have some practice and remember how to simplify results. 

<!-- Code for Multiple Choice questions and evaluating answers
 Editor does not support template string, so functionalily had to be hard  coded. Since each question-answer block is still a part of a single HTML code  instance, element IDs and function names had to be indexed.

Displays a question with for possible clickable answers -->
<div style='transform: scale(0.65); position: relative; top: -100px;'>
<h3>What is the result of 4/6 + 2/9?</h3>	
    <p>Choose 1 answer</p>
    <hr/>
   
    <div id='block-41' style='padding: 10px;'>
   <label for='option-41' style=' padding: 5px; font-size: 2.5rem;'>
        <input type='radio' name='option' value='8/9' id='option-41' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 
        8/9</label>
        <span id='result-41'></span>
    </div>
    <hr/>
    
    <div id='block-42' style='padding: 10px;'>
    <label for='option-42' style=' padding: 5px; font-size: 2.5rem;'>
        <input type='radio' name='option' value='9/8' id='option-42' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 				
        9/8</label>
        <span id='result-42'></span>
    </div>	
    <hr/>
     
    <div id='block-43' style='padding: 10px;'>
    <label for='option-43' style=' padding: 5px; font-size: 2.5rem;'>
        <input type='radio' name='option' value='1/2' id='option-43' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 				
        1/2</label>
        <span id='result-43'></span>
    </div>
    <hr/>
     
    <div id='block-44' style='padding: 10px;'>
        <label for='option-44' style=' padding: 5px; font-size: 2.5rem;'>
         <input type='radio' name='option' value='7/18' id='option-44' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 				
         7/18</label>
        <span id='result-44'></span>
    </div>
    <hr/>
    <button type='button' onclick='displayAnswer4()' style='width: 100px; height: 40px; border-radius: 3px; background-color: lightblue; font-weight: 700;'>Submit</button>
</div>
<a id='showanswer4'></a>
<script>
    
 //    The function evaluates the answer and displays result
	function displayAnswer4() {
    	if (document.getElementById('option-41').checked) {
      
        document.getElementById('block-41').style.border = '3px solid limegreen'
        document.getElementById('result-41').style.color = 'limegreen'
		document.getElementById('result-41').innerHTML = 'Correct!'
        
        } 
        if (document.getElementById('option-42').checked) {
        document.getElementById('block-42').style.border = '3px solid red'
        document.getElementById('result-42').style.color = 'red'
		document.getElementById('result-42').innerHTML = 'Incorrect!'
        showCorrectAnswer4()
 		}
        if (document.getElementById('option-43').checked) {
        document.getElementById('block-43').style.border = '3px solid red'
        document.getElementById('result-43').style.color = 'red'
		document.getElementById('result-43').innerHTML = 'Incorrect!'
        showCorrectAnswer4()	
        }
        if (document.getElementById('option-44').checked) {
        document.getElementById('block-44').style.border = '3px solid red'
        document.getElementById('result-44').style.color = 'red'
		document.getElementById('result-44').innerHTML = 'Incorrect!'
        showCorrectAnswer4() 	
        }
     }
    // the functon displays the link to the correct answer
    function showCorrectAnswer4() {
        	 let showAnswer4 = document.createElement('p')
             showAnswer4.innerHTML = 'Show Corrent Answer'
        showAnswer4.style.position = 'relative'
        showAnswer4.style.top = '-180px'
        showAnswer4.style.fontSize = '1.75rem'
             document.getElementById('showanswer4').appendChild(showAnswer4)
             showAnswer4.addEventListener('click', () => {
        	 document.getElementById('block-41').style.border = '3px solid limegreen'
        document.getElementById('result-41').style.color = 'limegreen'
		document.getElementById('result-41').innerHTML = 'Correct!'
        document.getElementById('showanswer4').removeChild(showAnswer4)    
         
        })
        }
</script>

## Part 5. Subtracting fractions

We'll start with two simple fractions. Subtract 1/3 from 3/5. As in the case of addition, we need to find a common denominator. So if we multiply our denominators, that **equals 3 times 5 = 15**. 

Next, we replace old denominators with the common one.  

![Image](https://www.freecodecamp.org/news/content/images/2020/03/fraction8.png)
_image of 3/5 - 1/3 = 4/15_

Then we need to find our numerators. For the first fraction, **15 divided by 5 = 3** and **3 times 3 = 9**. The result is **9/15**. For the second one, **15 divided by 3 = 5** and **5 times 1 = 5**. The result is **5/15**. 

The last step is to subtract the adjusted numerators: **9 minus 5 = 4.** The resulting fraction equals **4/15**.  

Let's now look at the case when we need to subtract a fraction from **a whole** number. Let's begin with **1 - 2/7**. 

You remember from previous sections that a whole number is like a pie that is completely shaded. Thus, if a pie is divided into **3** parts, **all 3** parts are shaded. If it is divided into **7** parts, then **7** parts will be shaded. So, **1 = 3/3 = 7/7** etc. 

Since we need to subtract **2/7**, we'll turn **1 whole** into **7/7** to make our task easy. **7/7 minus 2/7 = 5/7**. If the whole number is other than **1**, we write it as a mixed number and follow the steps from the last example. 

So let's subtract **2/7 from 3**. 

![Image](https://www.freecodecamp.org/news/content/images/2020/03/fraction9.png)
_image of 3 - 2/7 = 19/7_

Often, as a result of calculations, we may end up with a fraction where the numerator is greater than or equal to the denominator. Such fractions are called improper fractions. For example **5/3** (five thirds), **7/2** (seven halves) and so on. They can be converted to mixed numbers and vice versa. 

![Image](https://www.freecodecamp.org/news/content/images/2020/03/fraction10.png)
_Converting improper fractions to mixed numbers and vice versa_

All the rules covered so far apply to improper fractions as well. 

<!-- Code for Multiple Choice questions and evaluating answers
 Editor does not support template string, so functionalily had to be hard  coded. Since each question-answer block is still a part of a single HTML code  instance, element IDs and function names had to be indexed.
 Displays a question with for possible clickable answers --> 

<div style='transform: scale(0.65); position: relative; top: -100px;'>
<h3>What is the result of 9/11 - 3/4?</h3>	
    <p>Choose 1 answer</p>
    <hr/>
   
    <div id='block-51' style='padding: 10px;'>
   <label for='option-51' style=' padding: 5px; font-size: 2.5rem;'>
        <input type='radio' name='option' value='6/7' id='option-51' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 
        6/7</label>
        <span id='result-51'></span>
    </div>
    <hr/>
    
    <div id='block-52' style='padding: 10px;'>
    <label for='option-52' style=' padding: 5px; font-size: 2.5rem;'>
        <input type='radio' name='option' value='6/44' id='option-52' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 				
        6/44</label>
        <span id='result-52'></span>
    </div>	
    <hr/>
     
    <div id='block-53' style='padding: 10px;'>
    <label for='option-53' style=' padding: 5px; font-size: 2.5rem;'>
        <input type='radio' name='option' value='3/44' id='option-53' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 				
        3/44</label>
        <span id='result-53'></span>
    </div>
    <hr/>
     
    <div id='block-54' style='padding: 10px;'>
        <label for='option-54' style=' padding: 5px; font-size: 2.5rem;'>
         <input type='radio' name='option' value='6/11' id='option-54' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 				
         6/11</label>
        <span id='result-54'></span>
    </div>
    <hr/>
    <button type='button' onclick='displayAnswer5()' style='width: 100px; height: 40px; border-radius: 3px; background-color: lightblue; font-weight: 700;'>Submit</button>
</div>
<a id='showanswer5'></a>
<script>
    
 //    The function evaluates the answer and displays result
	function displayAnswer5() {
    	if (document.getElementById('option-53').checked) {
      
        document.getElementById('block-53').style.border = '3px solid limegreen'
        document.getElementById('result-53').style.color = 'limegreen'
		document.getElementById('result-53').innerHTML = 'Correct!'
        
        } 
        if (document.getElementById('option-51').checked) {
        document.getElementById('block-51').style.border = '3px solid red'
        document.getElementById('result-51').style.color = 'red'
		document.getElementById('result-51').innerHTML = 'Incorrect!'
        showCorrectAnswer5()
 		}
        if (document.getElementById('option-52').checked) {
        document.getElementById('block-52').style.border = '3px solid red'
        document.getElementById('result-52').style.color = 'red'
		document.getElementById('result-52').innerHTML = 'Incorrect!'
        showCorrectAnswer5()	
        }
        if (document.getElementById('option-54').checked) {
        document.getElementById('block-54').style.border = '3px solid red'
        document.getElementById('result-54').style.color = 'red'
		document.getElementById('result-54').innerHTML = 'Incorrect!'
        showCorrectAnswer5() 	
        }
     }
    // the functon displays the link to the correct answer
    function showCorrectAnswer5() {
        	 let showAnswer5 = document.createElement('p')
             showAnswer5.innerHTML = 'Show Corrent Answer'
        showAnswer5.style.position = 'relative'
        showAnswer5.style.top = '-180px'
        showAnswer5.style.fontSize = '1.75rem'
             document.getElementById('showanswer5').appendChild(showAnswer5)
             showAnswer5.addEventListener('click', () => {
        	 document.getElementById('block-53').style.border = '3px solid limegreen'
        document.getElementById('result-53').style.color = 'limegreen'
		document.getElementById('result-53').innerHTML = 'Correct!'
        document.getElementById('showanswer5').removeChild(showAnswer5)    
         
        })
        }
</script>

## Part 6. Multiplying fractions

Suppose we need to multiply two fractions, **2/5 times 3/7**. The **numerator** of the product will be the **product of the numerators** of these fractions: **2 times 3 = 6.** The **denominator** of the product will be the **product of denominators** of these fractions: **5 times 7 = 35**. Thus, **2/5 times 3/7 = 6/35**. 

If we need to multiply a **fraction** by a **whole number**, the **numerator** of the product will be the **product of the numerator of the fraction and that whole number**. The **denominator** of the product will remain the same as the **denominator of the fraction**. 

For example, **3/10 times 5 = 15/10**. To simplify, we divide the numerator and denominator by **5** and get **3/2.** 

Finally, if we need to multiply mixed numbers, first we convert them to improper fractions, then multiply them as we did above. The example below shows the steps. 

![Image](https://www.freecodecamp.org/news/content/images/2020/03/fraction11.png)
_image of 3/2 times 11/5 equals 33/10_

## Part 7. Dividing fractions

To divide fractions, flip the divisor so its numerator becomes the **new denominator** and denominator becomes the **new numerator**. Then just multiply the fractions like we did before. 

For example, divide 3/7 by 2/5. After flipping, **2/5** becomes **5/2** and we end up multiplying **3/7 times 5/2 = 15/14**. 

To divide fraction by a **whole** number, we invert that number and it becomes **1 divided by that number**. 

For instance, **2 becomes 1/2**, **9 becomes 1/9** etc. Next, we multiply as above. As you probably guessed already, dividing mixed numbers works the same way. Let's look at the example below.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/fraction12.png)
_dividing 11/6 by 17/8 = 44/51_

Let's test your knowledge.

<!-- Code for Multiple Choice questions and evaluating answers
 Editor does not support template string, so functionalily had to be hard  coded. Since each question-answer block is still a part of a single HTML code  instance, element IDs and function names had to be indexed.
 Displays a question with for possible clickable answers --> 

<div style='transform: scale(0.65); position: relative; top: -100px;'>
<h3>What is the result of 11/3 divided by 11/7?</h3>	
    <p>Choose 1 answer</p>
    <hr/>
   
    <div id='block-71' style='padding: 10px;'>
   <label for='option-71' style=' padding: 5px; font-size: 2.5rem;'>
        <input type='radio' name='option' value='3/7' id='option-71' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 
        3/7</label>
        <span id='result-71'></span>
    </div>
    <hr/>
    
    <div id='block-72' style='padding: 10px;'>
    <label for='option-72' style=' padding: 5px; font-size: 2.5rem;'>
        <input type='radio' name='option' value='3' id='option-72' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 				
        3</label>
        <span id='result-72'></span>
    </div>	
    <hr/>
     
    <div id='block-73' style='padding: 10px;'>
    <label for='option-73' style=' padding: 5px; font-size: 2.5rem;'>
        <input type='radio' name='option' value='7' id='option-73' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 				
        7</label>
        <span id='result-73'></span>
    </div>
    <hr/>
     
    <div id='block-74' style='padding: 10px;'>
        <label for='option-74' style=' padding: 5px; font-size: 2.5rem;'>
         <input type='radio' name='option' value='7/3' id='option-74' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 				
         7/3</label>
        <span id='result-74'></span>
    </div>
    <hr/>
    <button type='button' onclick='displayAnswer7()' style='width: 100px; height: 40px; border-radius: 3px; background-color: lightblue; font-weight: 700;'>Submit</button>
</div>
<a id='showanswer7'></a>
<script>
    
 //    The function evaluates the answer and displays result
	function displayAnswer7() {
    	if (document.getElementById('option-74').checked) {
      
        document.getElementById('block-74').style.border = '3px solid limegreen'
        document.getElementById('result-74').style.color = 'limegreen'
		document.getElementById('result-74').innerHTML = 'Correct!'
        
        } 
        if (document.getElementById('option-71').checked) {
        document.getElementById('block-71').style.border = '3px solid red'
        document.getElementById('result-71').style.color = 'red'
		document.getElementById('result-71').innerHTML = 'Incorrect!'
        showCorrectAnswer7()
 		}
        if (document.getElementById('option-72').checked) {
        document.getElementById('block-72').style.border = '3px solid red'
        document.getElementById('result-72').style.color = 'red'
		document.getElementById('result-72').innerHTML = 'Incorrect!'
        showCorrectAnswer7()	
        }
        if (document.getElementById('option-73').checked) {
        document.getElementById('block-73').style.border = '3px solid red'
        document.getElementById('result-73').style.color = 'red'
		document.getElementById('result-73').innerHTML = 'Incorrect!'
        showCorrectAnswer7() 	
        }
     }
    // the functon displays the link to the correct answer
    function showCorrectAnswer7() {
        	 let showAnswer7 = document.createElement('p')
             showAnswer7.innerHTML = 'Show Corrent Answer'
        showAnswer7.style.position = 'relative'
        showAnswer7.style.top = '-180px'
        showAnswer7.style.fontSize = '1.75rem'
             document.getElementById('showanswer7').appendChild(showAnswer7)
             showAnswer7.addEventListener('click', () => {
        	 document.getElementById('block-74').style.border = '3px solid limegreen'
        document.getElementById('result-74').style.color = 'limegreen'
		document.getElementById('result-74').innerHTML = 'Correct!'
        document.getElementById('showanswer7').removeChild(showAnswer7)    
         
        })
        }
</script>

## Part 8. Some practical examples

In order to find a fraction of some number, we need to **multiply** the given **number** by that **fraction**. 

Imagine, your school textbook has 200 pages. If you read 3/5 of the textbook, how many pages have you read? We are given the number which equals 200. To find 3/5 of 200, we multiply **200 times 3/5** and get  **120** pages. 

Solve the next question on your own. My birthday cake had 12 pieces. A few friends came by and enjoyed 2/3 of the cake. How many pieces did my friends have?

<!-- Code for Multiple Choice questions and evaluating answers
 Editor does not support template string, so functionalily had to be hard  coded. Since each question-answer block is still a part of a single HTML code  instance, element IDs and function names had to be indexed.
 Displays a question with for possible clickable answers --> 

<div style='transform: scale(0.65); position: relative; top: -100px;'>
<h3>How many pieces did my friends have?</h3>	
    <p>Choose 1 answer</p>
    <hr/>
   
    <div id='block-81' style='padding: 10px;'>
   <label for='option-81' style=' padding: 5px; font-size: 2.5rem;'>
        <input type='radio' name='option' value='2/3' id='option-81' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 
        2/3</label>
        <span id='result-81'></span>
    </div>
    <hr/>
    
    <div id='block-82' style='padding: 10px;'>
    <label for='option-82' style=' padding: 5px; font-size: 2.5rem;'>
        <input type='radio' name='option' value='4' id='option-82' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 				
        4</label>
        <span id='result-82'></span>
    </div>	
    <hr/>
     
    <div id='block-83' style='padding: 10px;'>
    <label for='option-83' style=' padding: 5px; font-size: 2.5rem;'>
        <input type='radio' name='option' value='9' id='option-83' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 				
        9</label>
        <span id='result-83'></span>
    </div>
    <hr/>
     
    <div id='block-84' style='padding: 10px;'>
        <label for='option-84' style=' padding: 5px; font-size: 2.5rem;'>
         <input type='radio' name='option' value='8' id='option-84' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 				
         8</label>
        <span id='result-84'></span>
    </div>
    <hr/>
    <button type='button' onclick='displayAnswer8()' style='width: 100px; height: 40px; border-radius: 3px; background-color: lightblue; font-weight: 700;'>Submit</button>
</div>
<a id='showanswer8'></a>
<script>
    
 //    The function evaluates the answer and displays result
	function displayAnswer8() {
    	if (document.getElementById('option-84').checked) {
      
        document.getElementById('block-84').style.border = '3px solid limegreen'
        document.getElementById('result-84').style.color = 'limegreen'
		document.getElementById('result-84').innerHTML = 'Correct!'
        
        } 
        if (document.getElementById('option-81').checked) {
        document.getElementById('block-81').style.border = '3px solid red'
        document.getElementById('result-81').style.color = 'red'
		document.getElementById('result-81').innerHTML = 'Incorrect!'
        showCorrectAnswer8()
 		}
        if (document.getElementById('option-82').checked) {
        document.getElementById('block-82').style.border = '3px solid red'
        document.getElementById('result-82').style.color = 'red'
		document.getElementById('result-82').innerHTML = 'Incorrect!'
        showCorrectAnswer8()	
        }
        if (document.getElementById('option-83').checked) {
        document.getElementById('block-83').style.border = '3px solid red'
        document.getElementById('result-83').style.color = 'red'
		document.getElementById('result-83').innerHTML = 'Incorrect!'
        showCorrectAnswer8() 	
        }
     }
    // the functon displays the link to the correct answer
    function showCorrectAnswer8() {
        	 let showAnswer8 = document.createElement('p')
             showAnswer8.innerHTML = 'Show Corrent Answer'
        showAnswer8.style.position = 'relative'
        showAnswer8.style.top = '-180px'
        showAnswer8.style.fontSize = '1.75rem'
             document.getElementById('showanswer8').appendChild(showAnswer8)
             showAnswer8.addEventListener('click', () => {
        	 document.getElementById('block-84').style.border = '3px solid limegreen'
        document.getElementById('result-84').style.color = 'limegreen'
		document.getElementById('result-84').innerHTML = 'Correct!'
        document.getElementById('showanswer8').removeChild(showAnswer8)    
         
        })
        }
</script>

Finally, there is one more case I want to explore. What if we know what a given fraction of some number equals and we need to find that number? 

For example, we know my friends had **8** pieces of the birthday cake and that was **2/3** of the **whole cake**. How many pieces did the cake have in the beginning? In order to find that **whole number**, we need to **divide 8 by 2/3**, which is **12**. 

Solve the next question on your own. A race car drove 900 meters on a track, which is 3/5 of the whole distance. What's the length of the race track?  

<!-- Code for Multiple Choice questions and evaluating answers
 Editor does not support template string, so functionalily had to be hard  coded. Since each question-answer block is still a part of a single HTML code  instance, element IDs and function names had to be indexed.
 Displays a question with for possible clickable answers --> 

<div style='transform: scale(0.65); position: relative; top: -100px;'>
<h3>What is the length of the race track?</h3>	
    <p>Choose 1 answer</p>
    <hr/>
   
    <div id='block-91' style='padding: 10px;'>
   <label for='option-91' style='padding: 5px; font-size: 2.5rem;'>
        <input type='radio' name='option' value='1200' id='option-91' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 
        1200 meters</label>
        <span id='result-91'></span>
    </div>
    <hr/>
    
    <div id='block-92' style='padding: 10px;'>
    <label for='option-92' style=' padding: 5px; font-size: 2.5rem;'>
        <input type='radio' name='option' value='1500' id='option-92' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 				
        1500 meters</label>
        <span id='result-92'></span>
    </div>	
    <hr/>
     
    <div id='block-93' style='padding: 10px;'>
    <label for='option-93' style=' padding: 5px; font-size: 2.5rem;'>
        <input type='radio' name='option' value='2700' id='option-93' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 				
        2700 meters</label>
        <span id='result-93'></span>
    </div>
    <hr/>
     
    <div id='block-94' style='padding: 10px;'>
        <label for='option-94' style=' padding: 5px; font-size: 2.5rem;'>
         <input type='radio' name='option' value='540' id='option-94' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 
        540 meters</label>
        <span id='result-94'></span>
    </div>
    <hr/>
    <button type='button' onclick='displayAnswer9()' style='width: 100px; height: 40px; border-radius: 3px; background-color: lightblue; font-weight: 700;'>Submit</button>
</div>
<a id='showanswer9'></a>
<script>
    
 //    The function evaluates the answer and displays result
	function displayAnswer9() {
    	if (document.getElementById('option-92').checked) {
      
        document.getElementById('block-92').style.border = '3px solid limegreen'
        document.getElementById('result-92').style.color = 'limegreen'
		document.getElementById('result-92').innerHTML = 'Correct!'
        
        } 
        if (document.getElementById('option-91').checked) {
        document.getElementById('block-91').style.border = '3px solid red'
        document.getElementById('result-91').style.color = 'red'
		document.getElementById('result-91').innerHTML = 'Incorrect!'
        showCorrectAnswer9()
 		}
        if (document.getElementById('option-93').checked) {
        document.getElementById('block-93').style.border = '3px solid red'
        document.getElementById('result-93').style.color = 'red'
		document.getElementById('result-93').innerHTML = 'Incorrect!'
        showCorrectAnswer9()	
        }
        if (document.getElementById('option-94').checked) {
        document.getElementById('block-94').style.border = '3px solid red'
        document.getElementById('result-94').style.color = 'red'
		document.getElementById('result-94').innerHTML = 'Incorrect!'
        showCorrectAnswer9() 	
        }
     }
    // the functon displays the link to the correct answer
    function showCorrectAnswer9() {
        	 let showAnswer9 = document.createElement('p')
             showAnswer9.innerHTML = 'Show Corrent Answer'
        showAnswer9.style.position = 'relative'
        showAnswer9.style.top = '-180px'
        showAnswer9.style.fontSize = '1.75rem'
             document.getElementById('showanswer9').appendChild(showAnswer9)
             showAnswer9.addEventListener('click', () => {
        	 document.getElementById('block-92').style.border = '3px solid limegreen'
        document.getElementById('result-92').style.color = 'limegreen'
		document.getElementById('result-92').innerHTML = 'Correct!'
        document.getElementById('showanswer9').removeChild(showAnswer9)    
         
        })
        }
</script>


