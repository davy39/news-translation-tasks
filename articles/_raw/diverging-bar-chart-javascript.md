---
title: How to Create a Diverging Bar Chart with a JavaScript Charting Library
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-02-24T17:09:07.000Z'
originalURL: https://freecodecamp.org/news/diverging-bar-chart-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2021/02/diverging-bar-chart-javascript-1500.png
tags:
- name: charts
  slug: charts
- name: data analysis
  slug: data-analysis
- name: data visualization
  slug: data-visualization
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'By Shachee Swadia

  This article is a step-by-step guide that''ll show you how to build an interactive
  JavaScript range chart that visualizes 20 years of the LA Lakers’ performance with
  Kobe Bryant.

  The year 2020 was pretty poignant for obvious reasons....'
---

By Shachee Swadia

This article is a step-by-step guide that'll show you how to build an interactive JavaScript range chart that visualizes 20 years of the LA Lakers’ performance with Kobe Bryant.

The year 2020 was pretty poignant for obvious reasons. But even before the pandemic, the year started on a sad note with the death of basketball legend [Kobe Bryant](https://en.wikipedia.org/wiki/Kobe_Bryant). He was a star NBA athlete who had played for 20 years with one and only one team — the Los Angeles Lakers. 

Remembering Kobe one year after that horrible crash, I wondered how the Lakers had performed in his two-decade era. So, I visualized that in an interactive Diverging Bar Chart with the help of pure JavaScript. 

Thinking that this project might be helpful for those new to web charting, I also logged the entire process and made a tutorial. Check it out!

## What Is a Diverging Bar Chart?

First things first, I will give you a brief explanation about what diverging bar charts are and then we'll dive into the tutorial.  

A diverging bar chart shows two or more measures that are plotted from a middle baseline, extending either to the right and left (horizontal range bars) or top and bottom (vertical range columns). 

The key point of data visualization in such diverging charts is to facilitate the comparison of multiple categories by means of displaying them against a bifurcating midpoint.

In this tutorial, I use the diverging bar chart technique to showcase the wins and losses of the LA Lakers through the 20 years of Kobe Bryant’s career.

Here's a sneak peek at the final chart to get you ready for the start of the game! Follow along with me to learn how I create this beautiful range bar chart with JavaScript.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/js-diverging-bar-chart.gif)

## How to Build a JavaScript Diverging Bar Chart in 4 Basic Steps

There are [multiple](https://en.wikipedia.org/wiki/Comparison_of_JavaScript_charting_libraries) JavaScript libraries out there providing pre-written JS code for commonly needed functions that can make the interactive data visualization process quite quick and straightforward. 

I picked one called [AnyChart](https://www.anychart.com) to create this diverging bar chart. This JS charting library appeared to support (particularly useful in this case) range charts out of the box and was also flexible enough to do what I wanted. 

Also, it is quite easy to get started with AnyChart even for beginners because there are many ready-to-use examples and it has intensive [documentation](https://docs.anychart.com).

Of course, having good HTML and JavaScript skills gives you an edge when visualizing data on the web. But anyway, the best part about making use of good charting libraries is that they make it quite uncomplicated to create interactive charts even without much experience.

The entire process of creating literally any JS chart, including a diverging bar chart like this one, can be broken down into four fundamental steps:

1. Create an HTML page.
2. Reference the necessary JS files.
3. Set the data.
4. Write the JS code for the chart.

Let's go through each step in detail now.

### 1. Create a basic HTML page

The first thing we need to do is create a basic HTML page. Let’s give it a title and create an HTML block element to hold the chart. To identify this `<div>` later in the code, we should also give it an id attribute (let it be “container”).

```html
<html>
  <head>
    <title>JavaScript Diverging Bar Chart</title>
    <style type="text/css">      
        html, body, #container { 
            width: 100%; height: 100%; margin: 0; padding: 0; 
        } 
    </style>
  </head>
  <body>
    <div id="container"></div>
  </body>
</html>
```

Note that it is possible to specify the width and height parameters inside the `<style>` block to modify the space that your chart will occupy. I have put 100% in both parameters so the chart fills the whole page.

### 2. Include the necessary JavaScript files

Next, we need to add the charting library scripts that will help create the data visualization. Since we are working with the AnyChart library here, let’s include the corresponding files from its [CDN](https://www.anychart.com/download/cdn/). (Keep in mind that you can always download the scripts if you want.)

For the diverging bar chart, we need the [base module script](https://docs.anychart.com/Quick_Start/Modules#base) which is to be added to the `<head>` section of the HTML page.

```js
<html>
  <head>
    <title>JavaScript Diverging Bar Chart</title>
    <script src="https://cdn.anychart.com/releases/8.9.0/js/anychart-base.min.js" type="text/javascript"></script>
    <style type="text/css">
      html,
      body,
      #container {
        width: 100%;
        height: 100%;
        margin: 0;
        padding: 0;
      }
    </style>
  </head>
  <body>  
    <div id="container"></div>
    <script>
      // All the code for the JS diverging bar chart will come here
    </script>
  </body>
</html>

```

### 3. Add the data

I wanted to visualize the number of wins and losses of the LA Lakers team across all seasons from 1996 to 2016. So, I got the data from the [NBA website](https://www.nba.com/lakers/history/seasonbyseason/) and created an array with the year, wins, and losses.

Since the amount of data is not huge, we can add it just like that:

```
var winlossData = [
  [65, 17, "2015-16"],
  [61, 21, "2014-15"],
  [55, 27, "2013-14"],
  [37, 45, "2012-13"],
  [25, 41, "2011-12"],
  [25, 57, "2010-11"],
  [25, 57, "2009-10"],
  [17, 65, "2008-09"],
  [25, 57, "2007-08"],
  [40, 42, "2006-07"],
  [37, 45, "2005-06"],
  [48, 34, "2004-05"],
  [26, 56, "2003-04"],
  [32, 50, "2002-03"],
  [24, 58, "2001-02"],
  [26, 56, "2000-01"],
  [15, 67, "1999-00"],
  [19, 31, "1998-99"],
  [21, 61, "1997-98"],
  [26, 56, "1996-97"]
];
```

Now that the stage is set, let’s start playing around by adding the JavaScript code that will create the interactive Diverging Bar Chart!

### 4. Write the JavaScript code for your chart

Before anything else, we need to add a function enclosing all the JS code, which makes sure that the entire code inside of it will only execute once the page is loaded.

```js
<script>
  anychart.onDocumentReady(function() {
    // The place for the JS diverging bar chart code
  });
</script>
```

In general, a JS diverging bar chart is pretty simple to create and I will walk you through each action. So get ready to wiggle, block, and shoot!

Firstly, we create a bar chart and enter the data, all inside the enclosing `anychart.onDocumentReady()` function.

```js
// create a bar chart
var chart = anychart.bar();

// data
var winlossData = [
  [65, 17, "2015-16"],
  [61, 21, "2014-15"],
  [55, 27, "2013-14"],
  [37, 45, "2012-13"],
  [25, 41, "2011-12"],
  [25, 57, "2010-11"],
  [25, 57, "2009-10"],
  [17, 65, "2008-09"],
  [25, 57, "2007-08"],
  [40, 42, "2006-07"],
  [37, 45, "2005-06"],
  [48, 34, "2004-05"],
  [26, 56, "2003-04"],
  [32, 50, "2002-03"],
  [24, 58, "2001-02"],
  [26, 56, "2000-01"],
  [15, 67, "1999-00"],
  [19, 31, "1998-99"],
  [21, 61, "1997-98"],
  [26, 56, "1996-97"]
];
```

Next, we create a function that accepts two parameters — a column number and a name. The column number indicates the column in the dataset and the name indicates the series. In our case, we have two series — one for the number of wins and one for the number of losses. 

Since we want a diverging bar chart, let’s take the center and plot the bars for wins to the right and bars for losses to the left. Then, we should prepare the dataset by adding all the required values through a 'for' loop.

Don’t worry if this sounds a bit complicated. It is just about making our data ready to be plotted, and when you look into the code below, you’ll likely see that it's all completely logical.

There are two more things we need to include in the function. We define a series with the rangeBar function and add a line to indicate the names of the series and a separator line between the left and right bars.

```js
var createSeries = function (columnNumber, name) {
  var data = [];
  for (var i = 0; i < winlossData.length; i++) {
    var value = winlossData[i][columnNumber];
    var center = 0;
    if (name === "Wins") {
      data.push({
        x: winlossData[i][2],
        low: center,
        high: center + value,
        value: value
      });
    } else {
      data.push({
        x: winlossData[i][2],
        low: -center,
        high: -center - value,
        value: value
      });
    }
  }
    
  var series = chart.rangeBar(data);
  series.name(name);
};

```

Now, we create the two series with the desired arguments using the function just defined.

```js
createSeries(0, "Losses");
createSeries(1, "Wins");
```

It’s halftime and the most complicated parts are over! Now we just have the setup of the chart.

Add the title to the diverging bar chart:

```js
chart
  .title()
  .enabled(true)
  .text("20 Years of LA Lakers Win-Loss Record with Kobe Bryant (1996-2016)");
```

And enable the chart’s legend:

```js
chart
  .legend()
  .enabled(true);
```

To make the wins and losses for each year show up adjacent to each other, we should convert the multi-series bar chart into a stacked bar chart. Next, to emphasize divergence, let’s add a line marker at 0. Finally, we assign the container div and draw the chart:

```js
// create a stacked bar chart from the multi-series bar chart
chart.yScale().stackMode("value");

// set a container id for the chart
chart.container("container");
  
// initiate chart drawing
chart.draw();

```

That’s the whistle and there you have it — a very basic, yet fully functional interactive diverging bar chart built with JavaScript!

![Image](https://www.freecodecamp.org/news/content/images/2021/02/initial-chart-default-colors-1.PNG)

Although Kobe may have been spectacular in the final games of his career in the NBA, we can see that the Lakers struggled during his last few years with more losses than wins. But the overall record is definitely many more triumphs than losses.

**Take a look at this initial version of the diverging bar chart with the full JS/CSS/HTML code [on CodePen](https://codepen.io/shacheeswadia/pen/jOVrqLQ).**

```js
<html>
  <head>
    <title>JavaScript Diverging Bar Chart</title>
    <script src="https://cdn.anychart.com/releases/8.9.0/js/anychart-base.min.js" type="text/javascript"></script>
    <style type="text/css">
      html,
      body,
      #container {
        width: 100%;
        height: 100%;
        margin: 0;
        padding: 0;
      }
    </style>
  </head>
  <body>  
    <div id="container"></div>
    <script>

    anychart.onDocumentReady(function () {
  
      // create a bar chart
      var chart = anychart.bar();

      // data
      var winlossData = [
        [65, 17, "2015-16"],
        [61, 21, "2014-15"],
        [55, 27, "2013-14"],
        [37, 45, "2012-13"],
        [25, 41, "2011-12"],
        [25, 57, "2010-11"],
        [25, 57, "2009-10"],
        [17, 65, "2008-09"],
        [25, 57, "2007-08"],
        [40, 42, "2006-07"],
        [37, 45, "2005-06"],
        [48, 34, "2004-05"],
        [26, 56, "2003-04"],
        [32, 50, "2002-03"],
        [24, 58, "2001-02"],
        [26, 56, "2000-01"],
        [15, 67, "1999-00"],
        [19, 31, "1998-99"],
        [21, 61, "1997-98"],
        [26, 56, "1996-97"]
      ];

      // configure a function to create series
      var createSeries = function (columnNumber, name) {
        var data = [];
        for (var i = 0; i < winlossData.length; i++) {
          var value = winlossData[i][columnNumber];
          var center = 0;
          if (name === "Wins") {
            data.push({
              x: winlossData[i][2],
              low: center,
              high: center + value,
              value: value
            });
          } else {
            data.push({
              x: winlossData[i][2],
              low: -center,
              high: -center - value,
              value: value
            });
          }
        }
    
        var series = chart.rangeBar(data);
        series.name(name);
      };

      // create series
      createSeries(0, "Losses");
      createSeries(1, "Wins");

      // set the chart title
     chart
        .title()
        .enabled(true)
        .text("20 Years of LA Lakers Win-Loss Record with Kobe Bryant (1996-2016)");

      // enable the chart legend
      chart
        .legend()
        .enabled(true);
  
      // create a stacked bar chart from the multi-series bar chart
      chart.yScale().stackMode("value");

      // set a container id for the chart
      chart.container("container");
  
      // initiate chart drawing
      chart.draw();

    });

    </script>
  </body>
</html>

```

## How to Customize Our JavaScript Diverging Bar Chart

A slam dunk thing about interactive data visualization with JavaScript is the freedom we have to customize it so that our data tells better stories. I will show you how to push some quick changes to the basic JS-based diverging bar chart to make it more engaging and informative.

Now I'll throw a 3-pointer and customize the chart to improve some of its functionalities and aesthetics.

### 1. Basic styling and axes settings

To start with, let’s change some basic styling and settings for the X and Y axes to make things more readable. 

Just remember that in AnyChart, a [range bar chart](https://docs.anychart.com/Basic_Charts/Range_Bar_Chart) is the vertical version of a [range column chart](https://docs.anychart.com/Basic_Charts/Range_Column_Chart). Consequently, in our diverging bar chart, the horizontal axis is the Y-axis, and the vertical axis is called the X-axis.

So, let’s get rid of ticks, configure the axis title, and customize the labels on the vertical axis. We'll also set 80 as the maximum and remove the minus sign from the labels on the horizontal axis:

```js
chart
  .xAxis()
  .ticks(false);
chart
  .xAxis()
  .title()
  .enabled(true)
  .text("Years")
  .padding([0, 0, 10, 0]);
chart
  .xAxis()
  .labels()
  .fontSize(11)
  .fontColor("#474747")
  .padding([0, 10, 0, 0]);
chart.yScale().maximum(80);
chart
  .yAxis(0)
  .labels()
  .format(function () {
    return Math.abs(this.value);
  });

```

Next, to emphasize divergence, it would be great to add a white stroke between the two series and a line marker at 0.

```js
// add the stroke by setting it in this line
series.name(name).stroke("3 #fff 1");

...

// create a line marker at 0
chart
  .lineMarker()
  .value(0)
  .stroke("#CECECE");

```

![Image](https://www.freecodecamp.org/news/content/images/2021/02/intermediate-chart-1-1.PNG)

Ah, doesn’t the chart look more polished and easier to read now?

**Check out the code for this version of the diverging bar chart [on CodePen](https://codepen.io/shacheeswadia/pen/zYoEMEd).**

Before we make more customizations, there is one small digression I want to make. I also thought of making the horizontal axis display the wins and losses for every season in percentages rather than absolute values. It’s pretty easy but the result did not offer any extra insights. 

Also, the absolute values do represent when the Lakers played more or fewer games through the year. That’s ultimately why I decided to keep the absolute values. But you are welcome to check out the version with percentages [on CodePen](https://codepen.io/shacheeswadia/pen/jOVrqKd). 

Well, let's move on from that missed shot and back into focus mode.

### 2. Tooltip customization

Next, I customized the tooltip to make it more informative and interesting.

Here, I also got the idea of showcasing the previously calculated percentage values (see the example from the digression just above) as an extra bit of information in the tooltip of our diverging bar chart.

So, the first step is to implement the calculation of percentage values:

```js
// calculate percentages for the tooltip
var val = winlossData[i][columnNumber] * 100;
if (columnNumber == 0) {
  var percentValue =
    val / (winlossData[i][columnNumber] + winlossData[i][columnNumber + 1]);
} else {
  var percentValue =
    val / (winlossData[i][columnNumber] + winlossData[i][columnNumber - 1]);
}
percentValue = percentValue.toFixed(2);

```

The percentage calculation goes as part of the series configuration function — look at how it is included there:

```js
// configure a function to create series
var createSeries = function (columnNumber, name) {
  var data = [];
  for (var i = 0; i < winlossData.length; i++) {

    // calculate percentages for the tooltip
    var val = winlossData[i][columnNumber] * 100;
    if (columnNumber == 0) {
      var percentValue =
        val / (winlossData[i][columnNumber] + winlossData[i][columnNumber + 1]);
    } else {
      var percentValue =
        val / (winlossData[i][columnNumber] + winlossData[i][columnNumber - 1]);
    }
    percentValue = percentValue.toFixed(2);     
      
    var value = winlossData[i][columnNumber];
    var center = 0;
    if (name === "Wins") {
      data.push({
        x: winlossData[i][2],
        low: center,
        high: center + value,
        value: value,
        // add the calculated percentage value
        percentValue: percentValue
      });
    } else {
      data.push({
        x: winlossData[i][2],
        low: -center,
        high: -center - value,
        value: value,
        // add the calculated percentage value
        percentValue: percentValue
      });
    }
  }

```

Then we have additional tooltip formatting to make it all look neat and beautiful:

```js
// customize the tooltip
chart
  .tooltip()
  .useHtml(true)
  .fontSize(12)
  .titleFormat(function () {
    return this.getData("x") + " " + this.seriesName;
  })
  .format(function () {
    return (
      "<h6 style='font-size:12px; font-weight:400; margin: 0.25rem 0;'>Total games: " +
      "<b>" +
      this.getData("value") +
      "</b></h6>" +
      "<h6 style='font-size:12px; font-weight:400; margin: 0.25rem 0;'>Percentage games: " +
      "<b>" +
      this.getData("percentValue") +
      " %</b></h6>"
    );
  });

```

### 3. Color palette change

Well, this last customization is definitely a dagger — the shot that is going to make the chart look completely awesome and win the game! It is simply changing the color palette to match the LA Lakers' jersey colors. So simple:

```js
chart.palette(
  anychart.palettes.distinctColors().items(["#FDB827", "#542583"])
);
```

![Image](https://www.freecodecamp.org/news/content/images/2021/02/final-chart-without-tooltip-2.PNG)

You see, at the very last second, I also turned off the selection mode by adding the corresponding command to this line:

```js
series.name(name).stroke("3 #fff 1").selectionMode("none");
```

**Okay! This final interactive JavaScript diverging range bar chart is available [on CodePen](https://codepen.io/shacheeswadia/pen/NWbrpYj).**

Just in case, the full code for the HTML page is right here:

```js
<html>
  <head>
    <title>JavaScript Diverging Bar Chart</title>
    <script src="https://cdn.anychart.com/releases/8.9.0/js/anychart-base.min.js" type="text/javascript"></script>
    <style type="text/css">
      html,
      body,
      #container {
        width: 100%;
        height: 100%;
        margin: 0;
        padding: 0;
      }
    </style>
  </head>
  <body>  
    <div id="container"></div>
    <script>

    anychart.onDocumentReady(function () {
  
      // create a bar chart
      var chart = anychart.bar();

      // data
      var winlossData = [
        [65, 17, "2015-16"],
        [61, 21, "2014-15"],
        [55, 27, "2013-14"],
        [37, 45, "2012-13"],
        [25, 41, "2011-12"],
        [25, 57, "2010-11"],
        [25, 57, "2009-10"],
        [17, 65, "2008-09"],
        [25, 57, "2007-08"],
        [40, 42, "2006-07"],
        [37, 45, "2005-06"],
        [48, 34, "2004-05"],
        [26, 56, "2003-04"],
        [32, 50, "2002-03"],
        [24, 58, "2001-02"],
        [26, 56, "2000-01"],
        [15, 67, "1999-00"],
        [19, 31, "1998-99"],
        [21, 61, "1997-98"],
        [26, 56, "1996-97"]
      ];

      // configure a function to create series
      var createSeries = function (columnNumber, name) {
        var data = [];
        for (var i = 0; i < winlossData.length; i++) {

          // calculate percentages for the tooltip
          var val = winlossData[i][columnNumber] * 100;
          if (columnNumber == 0) {
            var percentValue =
              val / (winlossData[i][columnNumber] + winlossData[i][columnNumber + 1]);
         } else {
            var percentValue =
              val / (winlossData[i][columnNumber] + winlossData[i][columnNumber - 1]);
          }
          percentValue = percentValue.toFixed(2);     
      
          var value = winlossData[i][columnNumber];
          var center = 0;
          if (name === "Wins") {
            data.push({
              x: winlossData[i][2],
              low: center,
              high: center + value,
              value: value,
              // add the calculated percentage value
              percentValue: percentValue
            });
          } else {
            data.push({
              x: winlossData[i][2],
              low: -center,
              high: -center - value,
              value: value,
              // add the calculated percentage value
              percentValue: percentValue
            });
          }
        }
    
        var series = chart.rangeBar(data);
        series.name(name).stroke("3 #fff 1").selectionMode("none");
      };

      // create series
      createSeries(0, "Losses");
      createSeries(1, "Wins");

      // set the chart title
      chart
        .title()
        .enabled(true)
        .text("20 Years of LA Lakers Win-Loss Record with Kobe Bryant (1996-2016)");

      // enable the chart legend
      chart
        .legend()
        .enabled(true);
  
      // create a stacked bar chart from the multi-series bar chart
      chart.yScale().stackMode("value");
  
      // customize the settings of the axes
      chart
        .xAxis()
        .ticks(false);
      chart
        .xAxis()
        .title()
        .enabled(true)
        .text("Years")
        .padding([0, 0, 10, 0]);
      chart
        .xAxis()
        .labels()
        .fontSize(11)
        .fontColor("#474747")
        .padding([0, 10, 0, 0]);
      chart.yScale().maximum(80);
      chart
        .yAxis(0)
        .labels()
        .format(function () {
          return Math.abs(this.value);
        });

      // create a line marker at 0
      chart
        .lineMarker()
        .value(0)
        .stroke("#CECECE");
  
      // customize the tooltip
      chart
        .tooltip()
        .useHtml(true)
        .fontSize(12)
        .titleFormat(function () {
          return this.getData("x") + " " + this.seriesName;
        })
        .format(function () {
          return (
            "<h6 style='font-size:12px; font-weight:400; margin: 0.25rem 0;'>Total games: " +
            "<b>" +
            this.getData("value") +
            "</b></h6>" +
            "<h6 style='font-size:12px; font-weight:400; margin: 0.25rem 0;'>Percentage games: " +
            "<b>" +
            this.getData("percentValue") +
            " %</b></h6>"
          );
        });
  
      // set a custom color palette
      chart.palette(
        anychart.palettes.distinctColors().items(["#FDB827", "#542583"])
      );

      // set a container id for the chart
      chart.container("container");
  
      // initiate chart drawing
      chart.draw();

    });

    </script>
  </body>
</html>

```

## Conclusion

In this tutorial, I have shown you how fast and easy it is to get a diverging bar chart up and running using JavaScript. We've also seen how a little bit of effort makes the graphic look really cool and lets you get more out of the underlying data. Please let me know if you have any questions.

If you are feeling motivated to work more with interactive JS-based data visualization, go ahead and play around with the diverging bar charts on CodePen (I added links throughout the tutorial), check out [other chart options](https://www.anychart.com/chartopedia/), or try [other JavaScript libraries](https://en.wikipedia.org/wiki/Comparison_of_JavaScript_charting_libraries).

Also, as we fondly look back at the statistics of the basketball legend’s team here, remember to do more sports and create more visualizations!

  

