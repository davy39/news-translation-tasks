---
title: Web Animation Techniques – CSS vs JavaScript
subtitle: ''
author: Joan Ayebola
co_authors: []
series: null
date: '2023-10-19T14:54:50.000Z'
originalURL: https://freecodecamp.org/news/web-animation-css-vs-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/10/Addition-and-Subtraction-Word-Problems-Math-Presentation-Orange-in-Pink-and-Purple-Groovy-Style.png
tags:
- name: animations
  slug: animations
- name: CSS
  slug: css
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: "Animations play a vital role in enhancing user experience on web pages.\
  \ They add interactivity, visual appeal, and engagement to websites and web applications.\
  \ \nTwo popular methods for creating web animations are Cascading Style Sheets (CSS)\
  \ and Java..."
---

Animations play a vital role in enhancing user experience on web pages. They add interactivity, visual appeal, and engagement to websites and web applications. 

Two popular methods for creating web animations are Cascading Style Sheets (CSS) and JavaScript. Each of these techniques has its strengths and use cases, and understanding when to use one over the other is crucial for web developers. 

In this article, we will explore the key differences between CSS and JavaScript animations, provide code examples, and guide you on when to choose one over the other.

## CSS Animations

CSS (Cascading Style Sheets) is commonly used for styling web pages. But it also provides a powerful and straightforward way to create animations. 

CSS animations are primarily used for simple, declarative animations like transitions, keyframes, and transformations.

### CSS Transition Example

First, let's look at an example of a simple CSS transition:

```css
.button {
  transition: background-color 0.3s ease;
}

.button:hover {
  background-color: #3498db;
}

```

<html>
<head>
  <style> 
      .button {
  transition: background-color 0.3s ease;
}

.button:hover {
  background-color: #3498db;
}
    </style>
</head>
<body>
  <button class="button">Hover me</button>
</body>
</html>


In the above example, the background color of the button will smoothly transition to a new color when a user hovers over it. This is achieved using the `transition` property. 

Let's learn a bit more about how the `transition` property works:

* `background-color`: This is the CSS property being animated. In this case, it's the background color of the button.
* `0.3s`: This is the duration of the animation. It specifies how long the transition takes to complete (0.3 seconds in this example).
* `ease-in-out`: This is the timing function that controls the animation's speed curve. It starts slow, speeds up in the middle, and slows down at the end.
* `0s`: This is the delay before the animation starts (in this case, there is no delay).

### Keyframes Example

Keyframes are another type of CSS animation you can use to style your elements. Here's an example of one in action:

```css
@keyframes pulse {
            0% {
                transform: scale(1);
            }
            50% {
                transform: scale(1.1);
            }
            100% {
                transform: scale(1);
            }
        }

        .element {
            width: 100px;
            height: 100px;
            background-color: #3498db;
            animation: pulse 2s ease-in-out infinite;
        }
```

Result:

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pulse Animation</title>
    <style>
        @keyframes pulse {
            0% {
                transform: scale(1);
            }
            50% {
                transform: scale(1.1);
            }
            100% {
                transform: scale(1);
            }
        }

        .element {
            width: 100px;
            height: 100px;
            background-color: #3498db;
            animation: pulse 2s ease-in-out infinite;
        }
    </style>
</head>
<body>
    <div class="element"></div>
</body>
</html>


In this example:

* We define a `@keyframes` rule named "pulse" that specifies three keyframes at 0%, 50%, and 100% of the animation duration. It uses the `transform` property to scale the element.
* The `.element` CSS class sets the initial background color, and it applies the "pulse" animation with a 2-second duration, "ease-in-out" timing function, and the "infinite" value, which means the animation will loop indefinitely.
* Inside the `<body>`, there's a `<div>` element with the class "element" that will undergo the "pulse" animation when the page loads.

When you open this HTML file in a web browser, the element will pulse or "breathe" by smoothly scaling up and down in size, creating a simple but eye-catching animation.

### Other CSS Animation Techniques:

There are other CSS animation techniques, including:

* **Transformations:** CSS can be used to perform 2D and 3D transformations like scaling, rotating, and translating elements.
* **Keyframes:** As shown in the above example, keyframes allow you to create more complex animations by specifying multiple steps or keyframes in an animation sequence.
* **Other types of CSS Transitions:** Besides property-based transitions, you can also use transitions for multiple properties, allowing you to create more intricate animations.

### Advantages of CSS Animations

* **Easy to Use**: CSS animations are relatively simple to implement, especially for basic animations like transitions and fades.
* **Performance**: They are hardware-accelerated and generally perform well, providing a smooth user experience.
* **Responsive Design**: CSS animations are inherently responsive and adapt to different screen sizes and devices.
* **Low JavaScript Overhead**: Using CSS for animations can reduce the load on JavaScript, making your web application more efficient.
* **Browser Compatibility**: CSS animations are widely supported in modern browsers. But it's important to note that there can be compatibility issues with older versions of Internet Explorer (IE) and some mobile browsers. In such cases, it may be necessary to provide graceful degradation or alternative designs for users on older browsers.

## JavaScript Animations

JavaScript is a versatile programming language used for a wide range of tasks, including creating complex animations. JavaScript animations are typically more flexible and capable of handling intricate, data-driven animations.

### JS Animations using the `requestAnimationFrame` method

```javascript
     const box = document.getElementById('animated-box');
        let isAnimating = false;

        box.addEventListener('click', () => {
            if (!isAnimating) {
                isAnimating = true;
                box.style.transform = 'translateX(200px)';
                
                setTimeout(() => {
                    isAnimating = false;
                    box.style.transform = 'translateX(0)';
                }, 1000);
            }
        });
```

Result:

<!DOCTYPE html>
<html>
<head>
    <style>
        #animated-box {
            width: 100px;
            height: 100px;
            background-color: #FF5733;
            position: relative;
            transition: transform 1s ease;
        }
    </style>
</head>
<body>
    <div id="animated-box">Click Me</div>

    <script>
        const box = document.getElementById('animated-box');
        let isAnimating = false;

        box.addEventListener('click', () => {
            if (!isAnimating) {
                isAnimating = true;
                box.style.transform = 'translateX(200px)';
                
                setTimeout(() => {
                    isAnimating = false;
                    box.style.transform = 'translateX(0)';
                }, 1000);
            }
        });
    </script>
</body>
</html>


In the JavaScript animation example, the `requestAnimationFrame` method is used to create a simple animation where a box moves horizontally when clicked. This method is often used for smoother, more complex animations.

In this example,

* We use `document.getElementById('animated-box')` to select the HTML element with the ID "animated-box" and assign it to the `box` variable.
* We also declare a boolean variable `isAnimating` to keep track of whether an animation is currently in progress.
* We add an event listener to the `box` element that listens for a click event.
* When the box is clicked, the event listener triggers an anonymous function that checks if an animation is already in progress (`isAnimating`). If not, it sets `isAnimating` to `true`.
* It then changes the `transform` property of the box to `translateX(200px)`. This shifts the box 200 pixels to the right, creating a horizontal animation effect.
* After a 1-second delay (specified by `setTimeout`), it sets `isAnimating` back to `false` and resets the `transform` property to its original state (`translateX(0)`), moving the box back to its initial position.

This code creates a simple animation where clicking the box moves it horizontally to the right and then back to its original position, all within the duration of 1 second. The CSS `transition` property ensures that the movement is smooth and visually appealing.

### Other common JavaScript animation methods

* **jQuery:** jQuery is a popular JavaScript library that simplifies animation tasks, making it easier to create animations with less code.
* **GreenSock Animation Platform (GSAP):** GSAP is a robust animation library for JavaScript that provides advanced animation capabilities and precise control over animations.
* **Canvas Animation:** HTML5 canvas can be used to create custom animations, especially for games and visualizations.
* **Web Animation API:** This native browser API provides a JavaScript interface for controlling animations on web pages, allowing for greater control over animations compared to CSS.
* **SVG Animations:** You can create complex animations within Scalable Vector Graphics (SVG) using JavaScript to manipulate SVG elements.

### Advantages of JavaScript Animations

* **Complex Animations**: JavaScript offers greater flexibility, making it suitable for complex animations with dynamic behavior.
* **Interactivity**: You can easily add user interactions, such as drag-and-drop functionality, through JavaScript animations.
* **Data-Driven Animations**: JavaScript allows you to create animations based on data, making it ideal for visualizing dynamic content.
* **Real-Time Updates**: JavaScript animations can be used for real-time updates and synchronized animations with other parts of the web application.
* **Performance Implications**: JavaScript animations can sometimes be resource-intensive, especially on mobile devices or less powerful hardware. Developers should be cautious when implementing complex JavaScript animations on these platforms to ensure a smooth user experience.

## When to Use CSS vs JavaScript for Animations

### When to Use CSS for Animations: 

CSS if often the best choice for basic animations like hover effects, transitions, and small, non-interactive animations.

CSS animations are generally smoother and more efficient, making them ideal for performance-critical scenarios.

And when you're designing responsive websites, CSS animations adapt to different screen sizes seamlessly.

### When to Use JavaScript for Animations:

On the other hand, when you need to create intricate animations with dynamic elements, JavaScript provides the necessary flexibility and control.

Also, if your animations need to respond to user interactions, JavaScript animations should be your go-to option.

JavaScript is also essential for creating interactive charts and graphs for data-driven animations.

And finally, when you require real-time updates or synchronized animations, JavaScript is the best choice for dynamic content.

## How to Combine CSS and JavaScript Animations

In some scenarios, a hybrid approach using both CSS and JavaScript animations can offer the best of both worlds. 

For instance, you might use CSS for initial animations and transitions that occur when a page loads and then employ JavaScript for user interactions, real-time updates, or data-driven animations. This combination can provide the efficiency and performance benefits of CSS with the interactivity and dynamic capabilities of JavaScript. 

Check out the following Codepen for an example: 

%[https://codepen.io/joanayebola/pen/wvRLKbQ]

## Conclusion

Web animations are a crucial element of modern web development, enhancing user experience and engagement. 

The choice between CSS and JavaScript for animations depends on the complexity of your project, the level of interactivity required, and your performance needs. 

For simple and performance-critical animations, CSS is often the best choice, while JavaScript is the go-to option for complex, interactive, and data-driven animations.

Remember that in many cases, a combination of both CSS and JavaScript can be the most effective approach. By understanding the strengths of each technique and when to apply them, you can create web animations that captivate your audience and elevate your web development projects.


