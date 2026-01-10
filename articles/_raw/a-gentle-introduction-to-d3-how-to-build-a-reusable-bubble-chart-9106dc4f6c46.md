---
title: 'A gentle introduction to D3: how to build a reusable bubble chart'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-03-11T19:20:44.000Z'
originalURL: https://freecodecamp.org/news/a-gentle-introduction-to-d3-how-to-build-a-reusable-bubble-chart-9106dc4f6c46
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Ywul1VdNkWbdFz3x5iVYCA.jpeg
tags:
- name: D3
  slug: d3
- name: Data Science
  slug: data-science
- name: data visualization
  slug: data-visualization
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Déborah Mesquita

  Getting Started with D3


  When I started to learn D3, nothing made sense to me. Things only became more clear
  when I started to learn about reusable charts.

  In this article, I’ll show you how to create a reusable bubble chart and g...'
---

By Déborah Mesquita

#### Getting Started with D3

![Image](https://cdn-media-1.freecodecamp.org/images/b1f4Gb2hEkCUMp9X0hyUcsXKVAMuRPFHYuvk)

When I started to learn D3, nothing made sense to me. Things only became more clear when I started to learn about reusable charts.

In this article, I’ll show you how to create a reusable bubble chart and give you a gentle introduction to D3 along the way. The dataset we’ll use is composed of [stories published in the freeCodeCamp in January 2017](https://github.com/dmesquita/reusable_bubble_chart/blob/master/medium_january.csv).

![Image](https://cdn-media-1.freecodecamp.org/images/ST0umvE7-OejTYSovrDQQZQzVPbXqKGhtUnL)
_This is the chart you’re going to build_

### About D3

[D3](https://d3js.org/) is a JavaScript library for data visualization. It brings data to life using HTML, SVG and CSS.

We often need to reuse a chart in another project, or event share the chart with others. For this, Mike Bostock (the creator of D3) proposed a model called [reusable charts](https://bost.ocks.org/mike/chart/). We’ll use his approach with some small modifications, as presented by Pablo Navarro Castillo in the book [Mastering D3.js](http://pnavarrc.github.io/book/).

We are using D3 version **4.6.0** here.

### ?Reusable charts

Graphs following the reusable chart pattern have two characteristics:

* **Configurability.** We want to modify the appearance and behavior of the graph without having to modify the code itself.
* **Ability to be built in an independent way.** We want every graph element associated with a data point of our dataset independently. This has to do with the way D3 associates data instances with DOM elements. This will become more clear in a minute.

> “To sum up: implement charts as **closures with getter-setter methods.” —** [Mike Bostock](https://bost.ocks.org/mike/chart/)

### The bubble chart

You first need to define which elements of the chart can be customized:

* The size of the chart
* The input dataset

#### Defining the size of the chart

Let's start by creating a function to encapsulate all variables of the graph and set the default values. This structure is called a closure.

```
// bubble_graph.js
```

```
var bubbleChart = function () {    var width = 600,    height = 400;    function chart(selection){        // you gonna get here    }    return chart;}
```

You want to create charts of different sizes without having to change the code. For this you will create charts as follows:

```
// bubble_graph.html
```

```
var chart = bubbleChart().width(300).height(200);
```

To do that, now you will define accessors for the width and height variables.

```
// bubble_graph.js
```

```
var bubbleChart = function () {    var width = 600    height = 400;
```

```
    function chart(selection){        // we gonna get here    }    chart.width = function(value) {        if (!arguments.length) { return width; }        width = value;        return chart;    }
```

```
    chart.height = function(value) {        if (!arguments.length) { return height; }        height = value;        return chart;    }    return chart;}
```

If you call `bubbleChart()` (without width or height attributes) the graph is created with the default width and heights values you defined inside the closure. If called without arguments, the method returns the variable value.

```
// bubble_graph.html
```

```
var chart = bubbleChart();bubbleChart().width(); // returns 600
```

You may be wondering why the methods return the chart function. This is a JavaScript pattern used to simplify the code. It's called method chaining. With this pattern you can create new objects like this:

```
// bubble_graph.html
```

```
var chart = bubbleChart().width(600).height(400);
```

instead of:

```
// bubble_graph.html
```

```
var chart = bubbleChart(); chart.setWidth(600); chart.setHeight(400);
```

#### Joining data with our chart

Now let’s learn how to join data with chart elements. Here’s how the chart is structured: the div with the graph has an SVG element, and each data point corresponds to a circle in the chart.

![Image](https://cdn-media-1.freecodecamp.org/images/KDQtSripZjkfZlWAGwt1RMOhoOEtuZy6BvbV)

```
// bubble_graph.html, after the bubbleChart() function is called
```

```
<svg width="600" height="400">;    <circle></circle> // a story from data    <circle></circle&gt; // another story from data    ...</svg>
```

#### ? d3.data()

The `d3.selection.**data**([data[,key]])` function returns a new selection that represents an element successfully bound to data. To do that, you first need to load the data from the .csv file. You will use the `d3.**csv**(_url_[[, _row_], _callback_])` function.

```
// bubble_graph.html
```

```
d3.csv('file.csv', function(error, our_data) {    var data = our_data; //here you can do what you want with the data}
```

```
// medium_january.csv|                title                 |   category   | hearts ||--------------------------------------|--------------|--------|| Nobody wants to use software         | Development  |  2700  |  | Lossless Web Navigation with Trails  |    Design    |  688   |   | The Rise of the Data Engineer        | Data Science |  862   |
```

#### ? d3-selection

You will use the **d3-select()** and the **data()** functions to pass our data to the chart.

> Selections allow powerful data-driven transformation of the document object model (DOM): set [attributes](https://github.com/d3/d3-selection/blob/master/README.md#selection_attr), [styles](https://github.com/d3/d3-selection/blob/master/README.md#selection_style), [properties](https://github.com/d3/d3-selection/blob/master/README.md#selection_property), [HTML](https://github.com/d3/d3-selection/blob/master/README.md#selection_html) or [text](https://github.com/d3/d3-selection/blob/master/README.md#selection_text) content, and more. — [D3 documentation](https://github.com/d3/d3-selection/)

```
// bubble_graph.html
```

```
<div class="chart-example" id="chart"><svg></svg></div>
```

```
d3.csv('medium_january.csv', function(error, our_data) {    if (error) {        console.error('Error getting or parsing the data.');        throw error;    }
```

```
    var chart = bubbleChart().width(600).height(400);    d3.select('#chart').data(our_data).call(chart);
```

```
 });
```

Another important selector is **d3.selectAll()**. Let's say you have the following structure:

```
<body>    <div></div>    <div></div>    <div></div></body>
```

`d3.select("body").selectAll("div")` selects all those divs for us.

#### ?? d3.enter()

And now you’re going to learn about an important D3 function: **d3.enter()**. Let's say you have an empty body tag and an array with data. You want to go through each element of the array and create a new div for each element. You can do this with the following code:

```
<!-- before --><body> //empty</body>
```

```
----// js script
```

```
var our_data = [1, 2, 3]var div = d3.select("body") .selectAll("div") .data(our_data) .enter() .append("div");---
```

```
<!-- after --><body>    <div></div>    <div></div>    <div></div></body>
```

Why do you need `selectAll("div")` if the the divs don't even exist yet? Because in D3 instead of telling **how** to do something, we tell **what** we want.

In this case, you want to associate each div with a element of the array. That's what you are saying with the `selectAll("div")`.

```
var div = d3.select("body") .selectAll("div") // here you are saying 'hey d3, each data element      of the array that comes next will be bound to a div' .data(our_data) .enter().append("div");
```

The `enter()` returns the selection with the data bound to the element of the array. You then finally add this selection to the DOM with the `.append("div")`

#### ?d3.forceSimulation()

You need something to simulate the physics of the circles. For this you will use `d3.forceSimulation([nodes])`. You also need to tell what kind of force will change the position or the velocity of the nodes.

In our case, we’ll use the `d3.forceManyBody()`.

```
// bubble_chart.js
```

```
var simulation = d3.forceSimulation(data) .force("charge", d3.forceManyBody().strength([-50])) .force("x", d3.forceX()) .force("y", d3.forceY()) .on("tick", ticked);
```

A positive strength value causes the nodes to attract each other, while a negative strength value causes them to repel each other.

![Image](https://cdn-media-1.freecodecamp.org/images/wMJSa903Hk1t5odK27XEEl0vhpYS8eq6odq5)
_The strength() effect_

We don't want the nodes spreading out through the whole SVG space, though, so we use `d3.forceX(0)` and`d3.forceY(0)`. This "drags" the circles to the 0 position. Go ahead and try removing this from the code to see what happens.

When you refresh the page, you can see that the circles adjust until they finally stabilize. The `ticked()` function updates the positions of the circles. The `d3.forceManyBody()` keeps updating the x and y position of each node, and the the `ticked()` function updates the DOM with these values (the cx and cy attributes).

```
// bubble_graph.js
```

```
function ticked(e) {    node.attr("cx", function(d) { return d.x; })        .attr("cy", function(d) { return d.y; });    // 'node' is each circle of the bubble chart
```

```
 }
```

Here's the code with everything together:

```
var simulation = d3.forceSimulation(data)     .force("charge", d3.forceManyBody().strength([-50]))     .force("x", d3.forceX())     .force("y", d3.forceY())     .on("tick", ticked); 
```

```
function ticked(e) {     node.attr("cx", function(d) { return d.x; })         .attr("cy", function(d) { return d.y; }); }
```

To sum up, all this simulation does is give each circle an x and y position.

#### ? d3.scales

Here comes the most exciting part: actually adding the circles. Remember the **enter()** function? You will use it now. In our chart the radius of each circle is proportional to the number of recommendations of each story. To do that you will use a linear scale: **d3.scaleLinear()**

To use scales you need to define two things:

* **Domain**: the minimum and maximum values of the input data (in our case, the minimum and maximum number of recommendations). To get the minimum and maximum values, you’ll use the **d3.min()** and **d3.max()** functions.
* **Range**: the minimum and maximum output values of the scale. In our case, we want the smallest radius of size 5 and the biggest radius of size 18.

```
// bubble_graph.js
```

```
var scaleRadius = d3.scaleLinear()            .domain([d3.min(data, function(d) { return +d.views; }),                     d3.max(data, function(d) { return +d.views; })])            .range([5,18]);
```

And then you finally create the circles:

```
// bubble_graph.js
```

```
var node = svg.selectAll("circle")   .data(data)   .enter()   .append("circle")   .attr('r', function(d) { return scaleRadius(d.views)})});
```

To color the circles, you’ll use a categorical scale: **d3.scaleOrdinal()**. This scale returns discrete values.

Our dataset has 3 categories: Design, Development and Data Science. You will map each of these categories to a color. `d3.schemeCategory10` gives us a list of 10 colors, which is enough for us.

```
// bubble_graph.js
```

```
var colorCircles = d3.scaleOrdinal(d3.schemeCategory10);var node = svg.selectAll("circle")    .data(data)    .enter()    .append("circle")    .attr('r', function(d) { return scaleRadius(d.views)})    .style("fill", function(d) { return colorCircles(d.category)});
```

You want the circles drawn in the middle of the SVG, so you’ll move each circle to the middle (half the width and half the height). Go ahead and remove this from the code to see what happens.

```
// bubble_graph.js
```

```
var node = svg.selectAll("circle") .data(data) .enter() .append("circle") .attr('r', function(d) { return scaleRadius(d.views)}) .style("fill", function(d) {return colorCircles(d.category)}) .attr('transform', 'translate(' + [width / 2, height / 2] + ')');
```

Now you’ll add tooltips to the chart. They need to appear whenever we place the mouse over the circles.

```
var tooltip = selection .append("div") .style("position", "absolute") .style("visibility", "hidden") .style("color", "white") .style("padding", "8px") .style("background-color", "#626D71") .style("border-radius", "6px") .style("text-align", "center") .style("font-family", "monospace") .style("width", "400px") .text("");
```

```
var node = svg.selectAll("circle") .data(data) .enter() .append("circle") .attr('r', function(d) { return scaleRadius(d.views)}) .style("fill", function(d) {return colorCircles(d.category)}) .attr('transform', 'translate(' + [width / 2, height / 2] + ')') .on("mouseover", function(d){     tooltip.html(d.category +"<br>"+ d.title+"<br>"+d.views);      return tooltip.style("visibility", "visible");}) .on("mousemove", function(){   return tooltip.style("top", (d3.event.pageY-       10)+"px").style("left",(d3.event.pageX+10)+"px");}) .on("mouseout", function(){return tooltip.style("visibility", "hidden");});
```

The `mousemove` follows the cursor when the mouse is moving. `d3.event.pageX` and `d3.event.pageY` return the mouse coordinates.

And that's it! You can see the final code [here](https://github.com/dmesquita/reusable_bubble_chart).

You can play with the bubble chart [here](https://bl.ocks.org/dmesquita/37d8efdb3d854db8469af4679b8f984a).

Did you found this article helpful? I try my best to write a deep dive article each month, you can [receive an email when I publish a new one](https://goo.gl/forms/SLrJDrGtxgAoILkt1).

Any questions or suggestions? Leave them in the comments. Thanks for reading! ?

_Special thanks to [John Carmichael](https://www.freecodecamp.org/news/a-gentle-introduction-to-d3-how-to-build-a-reusable-bubble-chart-9106dc4f6c46/undefined) and [Alexandre Cisneiros](https://www.freecodecamp.org/news/a-gentle-introduction-to-d3-how-to-build-a-reusable-bubble-chart-9106dc4f6c46/undefined)._

