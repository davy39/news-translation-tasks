---
title: Unit Circle Chart and Trig Calculator – Cos 0, Sin 0, Tan 0, Radians and More
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-09-08T16:06:31.000Z'
originalURL: https://freecodecamp.org/news/unit-circle-chart-and-trig-calculator
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c98d8740569d1a4ca1c60.jpg
tags:
- name: Advanced Mathematics
  slug: advanced-mathematics
- name: calculus
  slug: calculus
- name: Math
  slug: math
- name: Mathematics
  slug: mathematics
seo_title: null
seo_desc: "By Alexander Arobelidze\nThe unit circle is a useful visualization tool\
  \ for learning about trigonometric functions. \nThe key to its usefulness is its\
  \ simplicity. It removes the need for memorizing different values and allows the\
  \ user to simply derive ..."
---

By Alexander Arobelidze

The **unit circle** is a useful visualization tool for learning about trigonometric functions. 

The key to its usefulness is its simplicity. It removes the need for memorizing different values and allows the user to simply derive different results for different cases. 

Let's learn more about it and test our understanding with a handy trigonometric calculator I created at the end of the article.

## Part 1. What is the Unit Circle and how is it used?

The unit circle is a circle with a radius of **one** unit with its center placed at the origin. In other words, the center is put on a graph where the **X** and **Y** axes cross. 

![Image](https://www.freecodecamp.org/news/content/images/2020/08/unitCircle1-1.png)
_**Fig 1**. The graph of the unit circle with radius = 1 and points of intersection with X and Y axes_

Having a radius equal 1 unit will allow us to create **reference triangles** with hypotenuse equal to 1 unit. 

As we will see shortly, that allows us to measure **sine**, **cosine** and **tangent** directly. The triangle below reminds us how we define sine and cosine for some angle **alpha**. 

![Image](https://www.freecodecamp.org/news/content/images/2020/08/unitCircle2.png)
_**Fig 2**. Geometric definition of sine and cosine for an angle with hypotenuse equal 1_

Since the hypotenuse equals 1 and anything divided by 1 equals itself, sin of alpha equals the length of BC. Or **sin(α) = BC/1 = BC**. 

Similarly, cosine will equal the length of AC. Or **cos(α) = AC/1 = AC**. 

Next, let's move this triangle into our Unit Circle, so the radius of the circle can serve as the hypotenuse.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/unitCircle3.png)
_**Fig 3**. Reference triangle inside Unit Circle. x coordinate = cos(α) and y coordinate = sin(α)_

As a result, the **y** coordinate of the point where the triangle touches the circle equals sin(α), or **y = sin(α)**. Similarly, the **x** coordinate will equal cos(α), or **x = cos(α)**. 

Thus, by moving around the circle and changing the angle, we can measure sine and cosine of that angle by measuring the y and x coordinates accordingly. 

The angles can be measured in **degrees** and/or **radians**. The point with coordinates (1, 0) corresponds with **0** degrees (see Fig 1). The measure increases in a counterclockwise direction, so the point with coordinates (0, 1) will correspond with **90** degrees. A complete circle – **360** degrees. 

## Part 2. Important angles and their corresponding sine, cosine and tangent values

Since it makes sense to start at 0 degrees, our circle will look like this:

![Image](https://www.freecodecamp.org/news/content/images/2020/08/unitCircle4.png)
_**Fig 4**. Unit circle showing cos(0) = 1 and sin(0) = 0_

 Because **tangent** equals sine divided by cosine, **tan(0) = sin(0) / cos(0) = 0 / 1 = 0**. 

Next let's see what happens at 90 degrees. The coordinates of the corresponding point are (0, 1). Thus, sin(90) = y = 1 and cos(90) = x = 0. The circle will look like this:

![Image](https://www.freecodecamp.org/news/content/images/2020/08/unitCircle5.png)
_**Fig 5**. Unit circle showing cos(90) = 0 and sin(90) = 1_

What about tangent(90)? As the cosine measure approaches 0, and it happens to be a denominator in a fraction, the value of that fraction increases to infinity. Therefore **tan(90) is said to be undefined**. 

Now the question you might ask: as sin goes from 0 to 1 while cosine goes from 1 to 0, do they ever equal each other? The answer is yes, and that happens exactly half way at 45 degrees! The circle looks like this:

![Image](https://www.freecodecamp.org/news/content/images/2020/08/unitCircle6.png)
_**Fig 6**. Unit circle showing sin(45) = cos(45) = 1 / √2_

As a result of the numerator being the same as the denominator, **tan(45) = 1**.

Finally, the general reference Unit Circle. It reflects both positive and negative values for X and Y axes and shows important values you should remember

![Image](https://www.freecodecamp.org/news/content/images/2020/08/unitCircle7.png)
_**Fig 7**. Unit circle showing important sine and cosine values to remember_

As a final note for this section, it always helps to remember the following trigonometric identity based on the [Pythagorean theorem](https://en.wikipedia.org/wiki/Pythagorean_theorem): sin<sup>2</sup>(α) + cos<sup>2</sup>(α) = 1. 

## Part 3. Trigonometric Calculator

As a useful practice tool, I have added a simple trigonometric calculator. It takes inputs for angle measures and outputs corresponding values for **sine**, **cosine** and **tangent** functions. 

You can choose **degrees** or **radians** as a measure of angle. They each have their advantages and disadvantages. For quantitative relationships, since **π** radians **=** 180°, **1 radian** would be 180°/**π** or roughly **57°**. It can be calculated with any desired accuracy.   

The code for the calculator contains some basic interactivity and error handling within constraints of the editor. Its building blocks are marked and commented so anyone with the desire to modify it can easily do so. 

For example, new functions such as **ctg**, **sec** and so on can be added as well as different color schemes and much more. The complete source code can be accessed by [clicking here](https://github.com/sandroarobeli/TrigCalculator/blob/master/TrigCalculator.txt).

<!-- HTML elements -->
<div 
     class='flex-container' 
     style='margin: 0; 
            display: flex;
            flex-direction: column;
            justify-content: space-around; 
            align-items: center;'
     >
    <div 
         class='row' 
         style='margin: 0 auto;
                width: 100%;
                height: 60px;
                display: flex; 
                justify-content: space-around;
                align-items: center;'
         >
    	<h3 
            style='color: #1c96b5;
                   text-align: center;'
         >
            Input degree or radian measure and click Submit
        </h3>
    </div>
    <div 
         class='row' 
         style='margin: 0 auto; 
                width: 100%; 
                height: 60px; 
                display: flex;
                justify-content: space-around; 
                align-items: center;'
         >
    	<div 
             style='width: 250px;
                    height: 60px;'
             >
            <input style='margin: 0 auto;
                      	  border: 2px solid #eee;
                          box-shadow:0 0 15px 4px rgba(0,0,0,0.06);
                          border-radius:5px;
                          font-size: 2.3rem;
                          background: #fff;
                          width: 250px;
                          height: 60px;
                          margin: 0 auto;
                          color: #1c96b5;'
               	   type='number' 
               	   name='' 
                   id='currentMeasure' 
                   placeholder='Input measure here' 
         	/>
        </div>
    	<div 
             style='width: 250px; 
                    height: 60px;'
         >
             <div
                  style='display: flex;
                		 justify-content: space-around; 
                		 align-items: center;
                         background:#fff; 
                   	     font-size: 2.3rem;
                         height: 60px;
                         line-height: 60px;
                         margin: 0 auto;
                         color: #1c96b5;
                         border-radius:5px;
                         border: 2px solid #eee;
                         box-shadow:0 0 15px 4px rgba(0,0,0,0.06);'
                  >
             		<div>
  						<input 
                               type="radio" 
                               id="degree" 
                               name="measure" 	                             								value="degree" 
                               checked='checked'
                               style='transform: scale(1.5); 
                                      margin-right: 3px; 
                                      vertical-align: middle;'
                         />
  						<label for="degree">
                            Degree
                        </label>
					</div>
					<div>
  						<input 
                               type="radio" 
                               id="radian" 
                               name="measure" 															   value="radian" 
                               style='transform: scale(1.5); 
                                      margin-right: 3px; 
                                      vertical-align: middle;'
                         />
  						 <label for="radian">
                             Radian
                         </label>
					</div>
             </div>
         </div>
         <div 
              style='width: 250px; 
                     height: 60px;'
              >
         	<button 
                    style='background: #1c96b5; 
                           font-size: 3rem;
                           width: 250px;
                           height: 58px;
                           line-height: 56px;
                           margin: 0;
                           font-weight: 600;
                           border-radius:5px;
                           color:#fff;'
                	type='button'
                	id='submit'
                	onclick='handleSubmit()'
        	>
                Submit
                	<audio 
                      id='submitSound' 			                                                   src='https://www.fesliyanstudios.com/play-mp3/6683'
                    />
            </button>
         </div>
    </div>
    <div 
         class='row' 
         style='margin: 0 auto; 
                width: 100%; 
                height: 60px; 
                display: flex; 
                justify-content: space-around; 
                align-items: center;'
         >
    	<div 
             style='width: 250px; 
                    height: 60px;'
             >
        	<h3 
                style='background:#fff; 
                       font-size: 3rem;
                       height: 60px;
                       line-height: 60px;
                       margin: 0;
                       text-align: start;
                       padding-left: 30px;
                       color: #1c96b5;
                       border-radius:5px;
                       border: 2px solid #1c96b5;
                       box-shadow:0 0 15px 4px rgba(0,0,0,0.06);'
            	id=''
           >
                SIN: 
                	<span 
                          id='sin'
                    ></span>
            </h3>
        </div>
        <div 
             style='width: 250px; 
                    height: 60px;'
        >
        	<h3 
                style='background:#fff; 
                       font-size: 3rem;
                       height: 60px;
                       line-height: 60px;
                       margin: 0;
                       text-align: start;
                       padding-left: 30px;
                       color: #1c96b5;
                       border-radius:5px;
                       border: 2px solid #1c96b5;
                       box-shadow:0 0 15px 4px rgba(0,0,0,0.06);'
                id=''
         >
                COS: 
                	<span 
                          id='cos'
                    ></span>
            </h3>
        </div>
        <div 
             style='width: 250px;
                    height: 60px;'
         >
        	<h3 
                style='background:#fff; 
                       font-size: 3rem;
                       height: 60px;
                       line-height: 60px;
                       margin: 0;
                       text-align: start;
                       padding-left: 30px;
                       color: #1c96b5;
                       border-radius:5px;
                       border: 2px solid #1c96b5;
                       box-shadow:0 0 15px 4px rgba(0,0,0,0.06);'
                       id=''
         	>
                TAN: 
                	<span 
                          id='tan'
                    ></span>
            </h3>
        </div>
    </div>
    <div 
          class='row' 
          style='margin: 0 auto; 
                 width: 100%; 
                 height: 60px; 
                 display: flex; 
                 justify-content: space-around;
                 align-items: center;'
    >
    	<h3 
            style='background:#fff; 
                   font-size: 3rem;
                   height: 60px;
                   line-height: 60px;
                   margin: 0;
                   text-align: center;
                   color: #1c96b5;
                   border-radius:5px;
                   border: 2px solid #eee;
                   box-shadow:0 0 15px 4px rgba(0,0,0,0.06)'
        	id='prompter'
         ></h3>
    </div>
 </div>

<!--   CSS   -->
<!-- media accomodates two additional viewport sizes -->
<style>
    
    /* Mobile phones */
    @media screen and (max-width: 767px){
       .flex-container {
          transform: scale(0.60);
         }
     }
    /* Tablets and iPads */
    @media screen and (min-width: 768px) and (max-width: 1023px){
       .flex-container {
          transform: scale(0.8);
       }
    }
</style>

<!--   JS   --->
<script>
    // Element declaration
    const submitButton = document.getElementById('submit');
    const submitSound = document.getElementById('submitSound');
    const currentMeasure = document.getElementById('currentMeasure');
    const prompter = document.getElementById('prompter');
    const degreeInput = document.getElementById('degree')
    const radianInput = document.getElementById('radian')
    const sinValue = document.getElementById('sin')
    const cosValue = document.getElementById('cos')
    const tanValue = document.getElementById('tan')
	
	
   // Animation handling
    const handleActive = (button) => {
        submitSound.currentTime = 0
        submitSound.play()
    	button.style.backgroundColor = '#18809a'
        button.style.transform = 'scale(0.95)'
        setTimeout(() => {
			button.style.backgroundColor = '#1c96b5'
        	button.style.transform = 'scale(1.0)'
        	}, 100)
    }
    
  // Reset handling
   	const handleRestart = () => {
         if (currentMeasure.value === '' || !/^(\d*\.)?\d+$/.test(currentMeasure.value.toString())) {
         	currentMeasure.style.background = '#f99996'
            prompter.style.color = 'red' 
         } else {
         	currentMeasure.value = ''  
            currentMeasure.style.background = 'white'
          	prompter.textContent = ''  
         }
   };
  
  
  // Calculators for sin, cosine and tan
   const calculateSin = (degree, measure) => {
  	 if (degree) {
        return measure % 180 === 0 ? '0.000' : Math.sin(measure * (Math.PI / 180)).toPrecision(4)
        } else {
    	return Math.sin(measure).toPrecision(4)
    }
  }
  
  const calculateCos = (degree, measure) => {
  	if (degree) {
       return measure % 180 !== 0 && measure % 90 === 0 ? '0.000' : Math.cos(measure * (Math.PI / 180)).toPrecision(4)
     } else {
    	return Math.cos(measure).toPrecision(4)
     }
  }
  
  const calculateTan = (degree, measure) => {
	if (degree) {
    	if (measure % 180 !== 0 && measure % 90 === 0) {
        	return 'Infinity'
        } else {
        	return (calculateSin(true, measure) / calculateCos(true, measure)).toPrecision(4)
        }
    } else {
       if (measure % Math.PI !== 0 && measure % (Math.PI / 2) === 0) {
       		return 'Infinity'
       } else {
       		return (calculateSin(false, measure) / calculateCos(false, measure)).toPrecision(4)
       }
    }
}
  
  
  // Output handling
    const handleSubmit = () => {
    	handleActive(submitButton)
        if (currentMeasure.value === '' || !/^(\d*\.)?\d+$/.test(currentMeasure.value.toString())) {
            sinValue.innerText = ''
            cosValue.innerText = ''
            tanValue.innerText = ''
			prompter.textContent = 'Please input angle measure and press 				Submit';
        } else {
     		if (degreeInput.checked) {
            	sinValue.innerText = calculateSin(true, currentMeasure.value)
                cosValue.innerText = calculateCos(true, currentMeasure.value) 
                tanValue.innerText = calculateTan(true, currentMeasure.value)
            	} else {
            		sinValue.innerText = calculateSin(false, currentMeasure.value)
                	cosValue.innerText = calculateCos(false, currentMeasure.value)
                	tanValue.innerText = calculateTan(false, currentMeasure.value)
               }
   		}
        handleRestart()
   }
</script>

I hope the article, along with the calculator source code, will benefit you. Looking forward to seeing its modifications soon.

