---
title: How to build a range slider component in React from scratch using only &lt;div&gt;
  and &lt;span&gt;
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-08T21:41:33.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-range-slider-component-in-react-from-scratch-using-only-div-and-span-d53e1a62c4a3
coverImage: https://cdn-media-1.freecodecamp.org/images/1*iSkeoPHBQubtAL4fV4h9xQ.png
tags:
- name: components
  slug: components
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Rajesh Pillai

  In this article we will build a React range slider component step by step using
  only . We will enable it with touch support.

  What can you do with a piece of about 50 ?

  Build a slider control from scratch. If this sounds interesting, ...'
---

By Rajesh Pillai

In this article we will build a React range slider component step by step using only <div>. We will enable it with touch support.

What can you do with a piece of about 50 <div’s>?

Build a slider control from scratch. If this sounds interesting, then follow along.

![Image](https://cdn-media-1.freecodecamp.org/images/QEwCv3lfVNUfQ1OBmNv06P0gCVvRiDwoyb2A)

The final output will look like the below animation.

![Image](https://cdn-media-1.freecodecamp.org/images/3doGzBVGEKKvAJHv-dl3PXsZ62GZ-wg3hlx7)

Please do note that I have developed this component as a teaching exercise for my students of [ReactJS — Beyond the Basics course on Udemy](https://www.udemy.com/reactjs-beyond-the-basics/?couponCode=MEDIUM_500), so it may have some edge cases (which I will fix as and when encountered).

You could use an HTML5 range control and customize it. But I wanted to take a different approach and build something from scratch. And the result is what you see here.

Our slider component will be composed of the below three elements:

* A slider range
* The actual slider controls
* The current selection range

### Defining the state for our component

Let us begin by defining our state. I am only showing you the important part of the code. For the full source code, please refer to the link at the end of the article.

```
state = {      slots: 24,      start: 0,      end: 10,      labelMode: "mid",   // mid, long}
```

The state contains the following properties.

* slots: Total slots to be drawn (in this case I am using it as a time selector, so it will have 24 hour slots)
* start: The start value of the selection
* end: The end value of the selection
* labelMode: Currently unused. But can be used to customize the scale label rendering.

### The return part of the render method

Let us now take a look at the return part of the render method. The render() method will be slowly composed of small pieces of functionality.

```
return (        <div>          <h2>React Slider</h2>          <div className="example-1">            <div className="slider-container">             <div className="slider-scale">                 {scale}              </div>              <div className="slider">                  {slider}              </div>              <div className="slider-selected-scale">                  {currentScale}              </div>            </div>          </div>        </div>);
```

For those reading on mobile, the below image may be handy, as sometimes Medium breaks the code formatting.

![Image](https://cdn-media-1.freecodecamp.org/images/fmu5JvCqMDyJ8VDtwyeNScNlgydLc7MZdqWV)

If you take a look at the code, there are only three important pieces:

* scale variable
* slider variable
* currentScale variable

The three variables above will be responsible for rendering the correct parts of the overall slider.

### Dissecting the render () method

Let us initialize some variables. The `scale`, `slider` and `currentScale` JSX will be created within the for loop defined below.

```
render () { let scale = []; let slider=[]; let currentScale = []; let minThumb = null; let maxThumb = null
```

```
..... // rest of the code }
```

#### Create the JSX for the ‘scale’ variable

Creating the JSX for the scale variable is quite simple. We just loop through the slots value in the state and push a <div> to the scale array with the required CSS class for styling.

The if condition ensures that we are only printing the label for i = 0, i = 12, or i = 24 (kind of mid range). Please feel free to customize this.

```
for (let i = 0; i <= this.state.slots;i++) {        let label = "";                if (i == 0 || i == 12 || i == 24) {          label = i;        }                scale.push(          <div             key={i}             className="slot-scale">            {label}          </div>        );
```

Here’s the code in image format:

![Image](https://cdn-media-1.freecodecamp.org/images/ya7pdynXtp7ethqBzlALLU8zx57PghfpjfG7)

#### Create the JSX for the ‘currentScale’ variable

Let us now continue with the same for loop and create the ‘currentScale’ JSX. We are still within the same for loop, so about 24 divs will be created as per the value in this.state.slots value.

The currentScale has a class of ‘slot-scale-selected’.

```
let currentLabel = "";        if (i === this.state.start || i === this.state.end) {   currentLabel = i;}        currentScale.push(   <div       key={i}       className="slot-scale-selected">            {currentLabel}    </div> );
```

![Image](https://cdn-media-1.freecodecamp.org/images/K8tMqK3APpa7vyi186bmW3Pze0ebX-9laxfv)

The code is pretty similar to the ‘scale’ JSX that we created.

#### Create the JSX for the ‘slider’ variable

Let us write a function to render the ‘slider’ jsx. The slider needs two thumbs, one for min, and one for max.

Let us first initialize the thumb variable depending on the ‘i’ value. If ‘i’ is the same as this.state.start, then we set the minThumb variable. Else if the value of ‘i’ is the same as this.state.end, then we initialize the maxThumb variable.

```
if (i === this.state.start) {   minThumb = <this.MinSlider />} else if (i === this.state.end) {   maxThumb = <this.MaxSlider />} else {   minThumb = null;   maxThumb = null;}
```

![Image](https://cdn-media-1.freecodecamp.org/images/dvDNWJiBE0qleprPJYPC6yQBhedxr0KRq8TY)

#### Create the JSX for the ‘slider’

The important code piece here is the dragover event. This is required for the HTML drop to work correctly.

```
let lineClass = "line";        if (i >= this.state.start && i < this.state.end) {   lineClass += " line-selected";}slider.push(   <div         data-slot={i}        onDragOver={this.onDragOver}         onTouchMove = {this.onDragOver}        onTouchEnd = {this.onDrop}        onDrop = {this.onDrop}        key={i}         className="slot">           <div  data-slot={i} className={lineClass}/>           <span className="scale-mark"></span>           {minThumb}           {maxThumb}    </div> );
```

![Image](https://cdn-media-1.freecodecamp.org/images/xOUMWRHUNkJZLc1HVq7ihuhjI4O32BLCsyeA)

The slider variable needs two additional pieces of features to represent the min and the max thumb on the slider.

The slider JSX has additional event handlers to deal with handling the drop event/touchend event. We will take a look at the event handlers shortly.

The ‘lineClass’ styles/renders the line on the slider, and the ‘line-selected’ class styles the currently selected range.

Let us now write the MinSlider and MaxSlider function outside the render method.

#### The MinSlider () function to render the min thumb

Let’s take a look at the code. The important props are the events related to drag and the draggable attribute. The draggable attribute will make this element draggable.

We are also adding the touch event handler. Refer to the link at the bottom of the article to add touch support polyfill for the HTML5 API.

```
MinSlider=()=> {  return (     <div data-slider="min"            onDragStart={this.onDragStart}            onTouchStart={this.onDragStart}           draggable className="slider-thumb slider-thumb-min">     </div>  );}
```

#### The MaxSlider () function to render the min thumb

The MaxSlider is almost the same as the MinSlider except for the data and the className.

```
MaxSlider=()=> {  return (      <div data-slider="max"          onDragStart={this.onDragStart}           onTouchStart={this.onDragStart}        draggable className="slider-thumb slider-thumb-max">              </div>   );}
```

The code image is given below for reference.

![Image](https://cdn-media-1.freecodecamp.org/images/4vI2mOLaFiwUgpnUVe3zXD0vx3w4jbeOJB0o)

### Event Handling

Let us now look at the drag/touch event handlers defined within our <div> to control the movement of the slider element.

#### dragover:

The dragover event is required to support the drop zone when using the HTML5 drag/drop API. The only thing we need to do here is to invoke the preventDefault on the event object.

```
onDragOver = (e) => {    e.preventDefault();}
```

#### dragstart:

The dragstart enables us to store which slider is being dragged. Please note that I am not using the dataTransfer object here, but simply using an instance variable to store this.

```
onDragStart = (e) => {   let slider  = e.target.dataset.slider;   this.sliderType = slider;}
```

The value of e.target.dataset.slider is either “min” or “max,” indicating which slider is being dragged.

#### ondrop:

The ondrop event captures where the thumb is being dropped (on which scale).

This is the important flow in the ondrop event:

* Grab the source (whether min/max thumb)
* Get the slot (where the drop happens)
* Validations
* Update the slot (in the state)
* Reset the sliderType.

```
onDrop = (e, target) => {      let source = this.sliderType;      let slot = Number(e.target.dataset.slot);           if (isNaN(slot)) return;            if (source === "min") {        if (slot >= this.state.end) return;        this.setState({          start: slot        },()=>{          console.log(this.state);        })      } else if (source === "max") {        if (slot <= this.state.start) return;        this.setState({          end: slot        },()=>{          console.log(this.state);        })      }     this.sliderType = null;}
```

![Image](https://cdn-media-1.freecodecamp.org/images/13wMILHS9heXZUOf5pegbiq34G2o6Gom1onc)

#### The complete source code/and demo can be seen here [http://jsbin.com/remodat/edit?output](https://jsbin.com/remodat/edit?js,console)

Since I am using HTML5 drag and drop features to add touch, support please add this polyfill reference to your html file.

[**Bernardo-Castilho/dragdroptouch**](https://github.com/Bernardo-Castilho/dragdroptouch/blob/master/DragDropTouch.js)  
[_dragdroptouch - Polyfill that enables HTML5 drag drop support on mobile (touch) devices._github.com](https://github.com/Bernardo-Castilho/dragdroptouch/blob/master/DragDropTouch.js)

### Todos

* Extract the logic to a separate Component class
* Test it and and add customization.

### History

* 21-May-2018 — First release

P.S: This component is a result of a very quick coding attempt. This will be refactored.

**Promotion**: If you would like to support our open source curriculum [Mastering Full Stack Engineering in 12 to 20 weeks](https://codeburst.io/mastering-front-end-engineering-in-12-to-20-weeks-for-beginners-and-experienced-alike-6dc5172e3295) then here is a special 10$ coupon for medium readers for my upcoming live [ReactJS-Beyond the basics](https://www.udemy.com/reactjs-beyond-the-basics/?couponCode=MEDIUM_500) course on udemy (MEDIUM_500 is the coupon code, which is already tagged in the above URL)

