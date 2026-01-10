---
title: How to Solve a System of Linear Equations
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-04-10T12:48:46.000Z'
originalURL: https://freecodecamp.org/news/how-to-solve-a-system-of-linear-equations
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9baf740569d1a4ca2d4b.jpg
tags:
- name: Math
  slug: math
- name: Mathematics
  slug: mathematics
seo_title: null
seo_desc: "By Alexander Arobelidze\nA linear equation is an equation that graphs a\
  \ line. A system of linear equations is when there are two or more linear equations\
  \ grouped together. \nTo simplify the illustration, we will consider systems of\
  \ two equations. As th..."
---

By Alexander Arobelidze

A linear equation is an equation that graphs a line. A system of linear equations is when there are two or more linear equations grouped together. 

To simplify the illustration, we will consider systems of two equations. As the name suggests, there are two unknown variables. Often they are designated by the letters **x** and **y**. If equations describe some process, the letters can be chosen by the roles they play. For example, **d** can stand for distance, and **t** for time. 

In this article we will learn how to solve systems of linear equations using two fun methods. But before we start, let's see how we end up with a particular system by looking at a real life example.

## Deriving a system

A boy gets on his bicycle and starts riding to school. He rides **200** yards every minute. 

**6** minutes later, his mother realizes her son forgot his lunch. She gets on her own bicycle and starts following the boy. She rides **500** yards every minute (She is an Olympian and a gold medalist). 

We want to figure out how long it takes the mother to catch up to the boy, and how far she needs to ride to do so.

Since the boy covers 200 yards every minute, in **t** minutes he will cover **200** times **t** yards, or **200t** yards. 

His mother starts bicycling **6** minutes later, so she rides for **(t - 6)** minutes. Since she covers 500 yards every minute, in (t - 6) minutes she covers **500** times **(t - 6)** yards, or **500(t - 6)** yards. 

By the time she catches up to him, they both have covered the same distance. Let's say for now that distance is **d**. 

For the boy we have  **d = 200t** and for his mother we have **d = 500(t - 6)**. We now have our system of two equations.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/system1.png)
_A system of two equations d=200t and d=500(t - 6)_

A curly brace is often added to indicate that equations form a system.

Now let's see how we can solve this system.

## Solving by substitution

The first method we will consider uses **substitution**. 

We have two unknowns here, **d** and **t**. The idea is to get rid of one variable by expressing it using the other variable. 

The top equation tells us that **d = 200t**, so let's plug in **200t** for the **d** in the bottom equation. As a result, we have an equation with just the **t** variable.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/system2.png)
_An equation with a single variable 200t = 500(t - 6)_

First we expand the right side: 500(t -6) = 500t - 500*6 = **500t - 3000**. 

Then we simplify by moving the unknown members to one side and the known members to the other. The result is: **500t - 200t = 3000**.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/system3.png)
_Solving of equation 300t = 3000 results in t = 10_

Solving for **t** gives us **t = 10**, or since we measure time in minutes, **t = 10 minutes**. In other words, the mother will catch up to her son in 10 minutes. 

The second part of our problem is to find out how far she had to cycle to catch up with him. 

To answer that question, we need to find **d**. Substituting t = 10 in either equation will give us that answer. 

To make it easier, let use the top equation, **d = 200t = 200 * 10 = 2000**. Since we measure distance in yards, **d = 2000 yards**. 

Let's test your understanding so far – try to solve the next system on your own:

<!-- Code for Multiple Choice questions and evaluating answers
 Editor does not support template string, so functionalily had to be hard  coded. Since each question-answer block is still a part of a single HTML code  instance, element IDs and function names had to be indexed.

Displays a question with for possible clickable answers -->
<div style='transform: scale(0.65); position: relative; top: -100px;'>
  <div style='display: flex;'>
    <div style='transform: scale(4.3); margin-top: 52px;'>&#123;</div>
    <div style='margin-left: 20px;'>
      <h3>y = 2x</h3>
      <h3>y = 3(x - 1)</h3>
    </div>  
  </div>  
    
    <p>Choose 1 answer</p>
    <hr/>
   
    <div id='block-11' style='padding: 10px;'>
   <label for='option-11' style=' padding: 5px; font-size: 2.5rem;'>
        <input type='radio' name='option' value='1' id='option-11' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 
        x = 3 and y = 6</label>
        <span id='result-11'></span>
    </div>
    <hr/>
    
    <div id='block-12' style='padding: 10px;'>
    <label for='option-12' style=' padding: 5px; font-size: 2.5rem;'>
        <input type='radio' name='option' value='0' id='option-12' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 				
        x = 1 and y = 2</label>
        <span id='result-12'></span>
    </div>	
    <hr/>
     
    <div id='block-13' style='padding: 10px;'>
    <label for='option-13' style=' padding: 5px; font-size: 2.5rem;'>
        <input type='radio' name='option' value='0' id='option-13' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 				
        x = 6 and y = 3</label>
        <span id='result-13'></span>
    </div>
    <hr/>
     
    <div id='block-14' style='padding: 10px;'>
        <label for='option-14' style=' padding: 5px; font-size: 2.5rem;'>
         <input type='radio' name='option' value='0' id='option-14' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 				
         x = 1/2 and y = 2/3</label>
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

In the system above, the unknown variables are **x** and **y**. 

From the top equation we know that **y = 2x**. Substituting that to the bottom equation gives us **2(2x) = 3(x + 1)**. 

Once we expand and simplify, we get **4x = 3x + 3**. Or **x = 3**. Therefore, **y = 2 * 3 = 6**.

## Solving by graphing

The second method we will consider uses **graphing**, where we find the solution to a system of equations by graphing them out.

For example, take this system: **y = 2x + 3** and **y = 9 - x**. 

A graph of each equation will be a line. The first one for **y = 2x + 3** looks like this:  

![Image](https://www.freecodecamp.org/news/content/images/2020/04/graph1-1.png)
_A graph of y = 2x + 3_

Next, we can graph a line for **y = 9 - x**:  

![Image](https://www.freecodecamp.org/news/content/images/2020/04/graph2.png)
_Graphs of y = 2x + 3 and y = 9 - x_

These two lines **intersect** at exactly one point. This point is the only solution to both equations: 

![Image](https://www.freecodecamp.org/news/content/images/2020/04/graph3-1.png)
_Graphs of y = 2x + 3 and y = 9 - x intersect at (2, 7) point_

The ordered pair **(2, 7)** gives us the coordinates of our point of intersection. This pair is the solution to the system. Substituting **x = 2** and **y = 7** will let us verify this. 

What if the graphs are parallel and do not intersect at all? For example:

![Image](https://www.freecodecamp.org/news/content/images/2020/04/graph4.png)
_Graphs of y = x - 1 and y = x - 3_

When graphs of the equations do not intersect, that means our system has no solution. Trying to solve by substitution will prove that. 

The result of **x - 1** **= x - 3** will be **0 = -2**, which is **always** **false**.

But what if two graphs are the same and are directly on top of each other? 

![Image](https://www.freecodecamp.org/news/content/images/2020/04/graph5.png)
_Graphs of y = x - 2 and y = x - 2_

In such cases there are an infinite number of points of intersection. That means our system has an infinite number of solutions. Using the substitution method will prove that. 

The result of **x - 2 = x - 2** is **0 = 0**, which is **always true**. 

## More practice

Try using both the substitution and graphing methods to solve the following systems. These methods complement each other and will help you solidify your knowledge.

<!-- Code for Multiple Choice questions and evaluating answers
 Editor does not support template string, so functionalily had to be hard  coded. Since each question-answer block is still a part of a single HTML code  instance, element IDs and function names had to be indexed.

Displays a question with for possible clickable answers -->
<div style='transform: scale(0.65); position: relative; top: -100px;'>
  <div style='display: flex;'>
    <div style='transform: scale(4.3); margin-top: 52px;'>&#123;</div>
    <div style='margin-left: 20px;'>
      <h3>y = 2</h3>
      <h3>3y - 2x = 4</h3>
    </div>  
  </div>  
    
    <p>Choose 1 answer</p>
    <hr/>
   
    <div id='block-21' style='padding: 10px;'>
   <label for='option-21' style=' padding: 5px; font-size: 2.5rem;'>
        <input type='radio' name='option' value='1' id='option-21' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 
        System has no solution</label>
        <span id='result-21'></span>
    </div>
    <hr/>
    
    <div id='block-22' style='padding: 10px;'>
    <label for='option-22' style=' padding: 5px; font-size: 2.5rem;'>
        <input type='radio' name='option' value='0' id='option-22' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 				
        x = 1/2 and y = 1</label>
        <span id='result-22'></span>
    </div>	
    <hr/>
     
    <div id='block-23' style='padding: 10px;'>
    <label for='option-23' style=' padding: 5px; font-size: 2.5rem;'>
        <input type='radio' name='option' value='0' id='option-23' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 				
        x = 1 and y = 2</label>
        <span id='result-23'></span>
    </div>
    <hr/>
     
    <div id='block-24' style='padding: 10px;'>
        <label for='option-24' style=' padding: 5px; font-size: 2.5rem;'>
         <input type='radio' name='option' value='0' id='option-24' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 				
         x = 0 and y = 2</label>
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

Choosing a particular variable to use in substitution should make finding a solution easier.

Try expressing **x** with two other members in the top equation, then substitute the result into the bottom equation. That way you'll avoid dealing with fractions.

<!-- Code for Multiple Choice questions and evaluating answers
 Editor does not support template string, so functionalily had to be hard  coded. Since each question-answer block is still a part of a single HTML code  instance, element IDs and function names had to be indexed.

Displays a question with for possible clickable answers -->
<div style='transform: scale(0.65); position: relative; top: -100px;'>
  <div style='display: flex;'>
    <div style='transform: scale(4.3); margin-top: 52px;'>&#123;</div>
    <div style='margin-left: 20px;'>
      <h3>x + 5y = 7</h3>
      <h3>3x - 2y = 4</h3>
    </div>  
  </div>  
    
    <p>Choose 1 answer</p>
    <hr/>
   
    <div id='block-31' style='padding: 10px;'>
   <label for='option-31' style=' padding: 5px; font-size: 2.5rem;'>
        <input type='radio' name='option' value='1' id='option-31' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 
        x = 5 and y = 5/2</label>
        <span id='result-31'></span>
    </div>
    <hr/>
    
    <div id='block-32' style='padding: 10px;'>
    <label for='option-32' style=' padding: 5px; font-size: 2.5rem;'>
        <input type='radio' name='option' value='0' id='option-32' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 				
        x = 1 and y = 2</label>
        <span id='result-32'></span>
    </div>	
    <hr/>
     
    <div id='block-33' style='padding: 10px;'>
    <label for='option-33' style=' padding: 5px; font-size: 2.5rem;'>
        <input type='radio' name='option' value='0' id='option-33' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 				
        x = 1 and y = 1</label>
        <span id='result-33'></span>
    </div>
    <hr/>
     
    <div id='block-34' style='padding: 10px;'>
        <label for='option-34' style=' padding: 5px; font-size: 2.5rem;'>
         <input type='radio' name='option' value='0' id='option-34' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 				
         x = 2 and y = 1</label>
        <span id='result-34'></span>
    </div>
    <hr/>
    <button type='button' onclick='displayAnswer3()' style='width: 100px; height: 40px; border-radius: 3px; background-color: lightblue; font-weight: 700;'>Submit</button>
</div>
<a id='showanswer3'></a>
<script>
    
 //    The function evaluates the answer and displays result
	function displayAnswer3() {
    	if (document.getElementById('option-34').checked) {
      
        document.getElementById('block-34').style.border = '3px solid limegreen'
        document.getElementById('result-34').style.color = 'limegreen'
		document.getElementById('result-34').innerHTML = 'Correct!'
        
        } 
        if (document.getElementById('option-31').checked) {
        document.getElementById('block-31').style.border = '3px solid red'
        document.getElementById('result-31').style.color = 'red'
		document.getElementById('result-31').innerHTML = 'Incorrect!'
        showCorrectAnswer3()
 		}
        if (document.getElementById('option-32').checked) {
        document.getElementById('block-32').style.border = '3px solid red'
        document.getElementById('result-32').style.color = 'red'
		document.getElementById('result-32').innerHTML = 'Incorrect!'
        showCorrectAnswer3()	
        }
        if (document.getElementById('option-33').checked) {
        document.getElementById('block-33').style.border = '3px solid red'
        document.getElementById('result-33').style.color = 'red'
		document.getElementById('result-33').innerHTML = 'Incorrect!'
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
        	 document.getElementById('block-34').style.border = '3px solid limegreen'
        document.getElementById('result-34').style.color = 'limegreen'
		document.getElementById('result-34').innerHTML = 'Correct!'
        document.getElementById('showanswer3').removeChild(showAnswer3)    
         
        })
        }
</script>

Let's do one more challenge:

<!-- Code for Multiple Choice questions and evaluating answers
 Editor does not support template string, so functionalily had to be hard  coded. Since each question-answer block is still a part of a single HTML code  instance, element IDs and function names had to be indexed.

Displays a question with for possible clickable answers -->
<div style='transform: scale(0.65); position: relative; top: -100px;'>
  <div style='display: flex;'>
    <div style='transform: scale(4.3); margin-top: 52px;'>&#123;</div>
    <div style='margin-left: 20px;'>
      <h3>-6x - 8y = 4</h3>
      <h3>y = -x - 1</h3>
    </div>  
  </div>  
    
    <p>Choose 1 answer</p>
    <hr/>
   
    <div id='block-41' style='padding: 10px;'>
   <label for='option-41' style=' padding: 5px; font-size: 2.5rem;'>
        <input type='radio' name='option' value='1' id='option-41' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 
        x = -2 and y = 1</label>
        <span id='result-41'></span>
    </div>
    <hr/>
    
    <div id='block-42' style='padding: 10px;'>
    <label for='option-42' style=' padding: 5px; font-size: 2.5rem;'>
        <input type='radio' name='option' value='0' id='option-42' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 				
        Infinite number of solutions</label>
        <span id='result-42'></span>
    </div>	
    <hr/>
     
    <div id='block-43' style='padding: 10px;'>
    <label for='option-43' style=' padding: 5px; font-size: 2.5rem;'>
        <input type='radio' name='option' value='0' id='option-43' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 				
        x = 2 and y = -1</label>
        <span id='result-43'></span>
    </div>
    <hr/>
     
    <div id='block-44' style='padding: 10px;'>
        <label for='option-44' style=' padding: 5px; font-size: 2.5rem;'>
         <input type='radio' name='option' value='0' id='option-44' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 				
         x = -1/6 and y = 6</label>
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

Now that you know enough about substitution and graphing, get out there and solve more linear equations.

