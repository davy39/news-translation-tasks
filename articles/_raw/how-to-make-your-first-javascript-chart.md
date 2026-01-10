---
title: How to make your first JavaScript chart with JSCharting
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-08T14:45:15.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-your-first-javascript-chart
coverImage: https://www.freecodecamp.org/news/content/images/2020/01/first-javascript-chart-using-csv-jscharting-fit.jpg
tags:
- name: charts
  slug: charts
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'By Arthur Puszynski

  When you''re starting out as a beginner JavaScript developer, I think it is important
  to pursue interesting projects. That way you can make sure you have fun as you learn,
  and you''ll likely find an area of specialization that you e...'
---

By Arthur Puszynski

When you're starting out as a beginner JavaScript developer, I think it is important to pursue interesting projects. That way you can make sure you have fun as you learn, and you'll likely find an area of specialization that you enjoy. 

As they say, _"If you love what you do, you'll never work a day in your life"_. 

![Image](https://www.freecodecamp.org/news/content/images/2019/12/not-suited-for-work.gif)
_Source: giphy.com_

In this article, I will introduce you to front-end data visualization, which is my personal passion. Perhaps it will become your passion as well!

The most rewarding moments for me as a developer are when I can see or experience the results of what I've made. It’s highly satisfying to create a chart that reveals interesting insights about its data, or an interactive experience that helps explore details of a unique data set. The more significant the result, the more rewarding it feels. 

However, I have realized that the amount of work you put into a project does not necessarily correlate with the sense of accomplishment – sometimes it feels great even when it was relatively easy. 

Over time, you will find tools that will help make you more efficient, and sometimes you will move mountains with little effort. There are many chart libraries and tools available in the data visualization field. With the right tools, you will create new charts with little effort, regardless of the type of chart you need. Personally, I think that datavis yields a great reward on your investment of time and effort.

In this tutorial you will use a number of tools to get data over the internet, process it, and draw a beautiful chart that can be viewed in any modern browser. You can click the links below to download example code for each step individually, view them all on **[GitHub](https://github.com/arthurPuszynski/first-chart-article)**, or download all steps at once here: **[all-steps.zip](https://github.com/arthurPuszynski/first-chart-article/raw/master/zips/all-steps.zip).**

## The Result

By the end of this tutorial you will create this interactive data-driven chart. You will learn how to get data over the internet, process it, and make a chart with that data. You will also be able to make your own charts from scratch.

![Interactive JavaScript line chart](https://www.freecodecamp.org/news/content/images/2019/12/javascript-line-chart.png)
_Interactive JavaScript line chart_

After processing the data and charting it, you will also learn how to make adjustments to the chart including modifying the default legend, enabling x axis crosshairs with tooltips, and applying text annotations to add context and other information to the chart.

## The Tools

To get started, use an internet browser like the one you're probably using to read this article. I recommend Chrome as it offers a great experience and built in tools for developers.

Next you will need a text editor. Something as simple as notepad will work. But, I suggest using a more advanced code editor such as VS Code, as this is an environment you will spend a lot of time with. It will give you a more convenient and pleasant coding experience, and it makes writing HTML5, CSS, and JavaScript easier on the eyes. Most important, if you forget a quote or comma somewhere, a code editor can help you find the error.

This article can help you [choose the best JavaScript code editor for web development](https://www.freecodecamp.org/news/how-to-choose-a-javascript-code-editor/).

You will use the JSCharting chart library to automatically draw and add interactive functionality for this chart. No other JavaScript libraries such as jQuery, or front-end platforms including React and Angular (commonly used for website projects) will be required.

### Why JSCharting?

[JSCharting](https://jscharting.com/) is a JavaScript charting library that can draw many different types of charts using SVG. It is easy to use and get started with, so it's a good fit for this tutorial. The API (Application Programming Interface, aka the options and settings necessary to create charts) makes difficult things simpler and it is a good option when experimenting with data visualizations. 

You can use JSCharting for free for personal and commercial use with the included branding.

You can create responsive charts with JSCharting through a couple simple steps:

- Define a `<div>` tag in the HTML file with a unique id.
- Provide this id,  data, and any other options when calling `JSC.Chart()` in the JavaScript file.

That's it. JSC will draw a professional looking chart populating this div tag with SVG element visuals. The chart will be responsive and interactive without any extra effort.

## The Data

You will use a data file provided by the NCHS (National Center for Health Statistics) listing historical life expectancy of males and females in the US.

You can find it here: [https://data.cdc.gov/resource/w9j2-ggv5.csv](https://data.cdc.gov/resource/w9j2-ggv5.csv). 

This CSV file contains data that categorizes the life expectancies by year, race, and sex. You will use some of this data to draw a simple male/female trend line over the last 100 years.

CSV (Comma Separated Values) is a great format for transmitting data over the internet. It is compact, human readable and you can open it directly excel, which is also nice.

So without further ado, let's get started.

![Image](https://www.freecodecamp.org/news/content/images/2019/12/readycat.gif)
_Source: giphy.com_

## Step 1 - Add a blank chart

The first zip file contains a blank starting point you can fill in as we go. If you get lost or confused, or want to skip ahead, the zip file at the end or throughout each section will bring you up to speed.  

If you wish to download all the files at once, see **[all-steps.zip](https://github.com/arthurPuszynski/first-chart-article/raw/master/zips/all-steps.zip)** instead_._

### [step1-a.zip](https://github.com/arthurPuszynski/first-chart-article/raw/master/zips/step1-a.zip)

This zip file contains the following files.
- `index.html`
- `js/index.js`

The `.html` file is empty except for some standard code that makes it a valid file and the `.js` file is completely blank.

The first step is to add some scripts to the HTML web page file. Normally people suggest adding `<script>` tags inside the `<head>` tags. However, for scripts that affect the HTML content it is often better to add them after the closing `</body>` tag. 

This technique loads all the HTML into the DOM before executing any JavaScript. The chart needs the HTML loaded before it can draw in it. The DOM (Document Object Model) is a representation of your HTML code in the browser memory. Once HTML is loaded into the DOM the browser can display it and JavaScript can interact with it.

Start by adding the JSCharting library to the HTML file. Open the `index.html` file in your editor of choice. Then add a script tag to include JSCharting after the closing `</body>` tag. The resulting code at the bottom of the file should look like this:

```html
</body>
<script src="https://code.jscharting.com/2.9.0/jscharting.js"></script>
</html>
```

This library URL points to a CDN (Content Delivery Network). It hosts the chart code and makes it convenient to quickly add the library to any HTML page for prototyping charts and experimenting. You can also [download](https://jscharting.com/download/) and use the library locally or use the npm package in your project, but the CDN does not require any extra steps.

Next, using the same technique, add another script tag referencing your blank JavaScript file. Add this script after the `jscharting.js` script so it looks like this:

```html
</body>
<script src="https://code.jscharting.com/2.9.0/jscharting.js"></script>
<script src="js/index.js"></script>
</html>
```

Great. We are almost ready to draw a blank chart. The last thing you need to do is add a `<div>` placeholder inside the HTML file to define where we want this chart to draw.

Add this HTML code inside the `<body>` tags.

```html
<body>
    <div id="chartDiv" style="width:50%; height:300px; margin:0 auto;"></div>
</body>
```

The div must have an id so you can tell the chart which div to draw in. In this case the id is `chartDiv`. 

You may notice the style attribute of the `<div>` tag. It makes the div 50% of the window width, and 300 pixels tall. The margin style `margin:0 auto;` centers the div on the page. The chart will fill whatever size the div is, so changing the div size is a good way to control the chart size.

You're all set with the HTML file. Open the `index.js` file and add a blank chart to this page by writing the following code which includes the div id `chartDiv`:

```javascript
JSC.Chart('chartDiv', {});
```

Open the `index.html` file in a browser (drag and drop the file into a web browser like chrome).

Not much to see yet, but you might notice a small JSC logo on this page. That indicates a chart is wired up and drawing.

![JSCharting logo shows the chart is working](https://www.freecodecamp.org/news/content/images/2019/12/jscharting-brand.png)
_JSCharting logo shows the chart is working_

**[step1-b.zip](https://github.com/arthurPuszynski/first-chart-article/raw/master/zips/step1-b.zip)**

## Step 2 - Play with the chart a little bit

Ok, as a test, let's add a couple values for the chart to visualize to see how it works.

Going back to the `index.js` file, replace the content with the following code which adds more options to the chart.

```javascript
JSC.Chart('chartDiv', {
   type: 'horizontal column',
   series: [
      {
         points: [
            {x: 'Apples', y: 50},
            {x: 'Oranges', y: 42}
         ]
      }
   ]
});
```

Now refresh (F5) the browser window where the `index.html` page is loaded.

![Horizontal column chart with one series and two points](https://www.freecodecamp.org/news/content/images/2019/12/horizontal-column-chart.png)
_Horizontal column chart with one series and two points_

Nice! You just made your first chart using JavaScript.

![Image](https://www.freecodecamp.org/news/content/images/2019/12/yeah-1.gif)
_Source: giphy.com_

You made a bar chart by setting the chart type option to `'horizontal column'`. If you prefer a vertical column, set the value to `'column'`. You also added a series with two points to the chart for Apples and Oranges.

All chart data is made up of series and points. A series is simply a group of data points. Charts can contain one or more data series. Data points consist of values that map to the x and y axes. Points can also include many other descriptive variables and values.

The example above contains only one series. Now let's look at the options for a chart with two series. Replace the content of the JavaScript file with this code.

```javascript
JSC.Chart('chartDiv', {
   type: 'horizontal column',
   series: [
      {
         name:'Andy',
         points: [
            {x: 'Apples', y: 50},
            {x: 'Oranges', y: 32}
         ]
      },{
         name:'Anna',
         points: [
            {x: 'Apples', y: 30},
            {x: 'Oranges', y: 22}
         ]
      }
   ]
});
```

Refreshing the browser window will show this chart.

![Horizontal column chart with two series](https://www.freecodecamp.org/news/content/images/2019/12/horizontal-column-cluster.png)
_Horizontal column chart with two series_

The chart options look similar. Still a bar chart, but this time there is an extra object in the series array.  We also added name properties for each series so the chart can identify them in the legend.

If you are interested in making different charts like radar charts, area charts, pie charts, gantt charts, or even calendar heatmap charts, take a look at the [JSCharting examples gallery](https://jscharting.com/examples/chart-types/) and the source code (chart options) used to create those charts. You can quickly learn how to use other chart features by copying the available examples.

**[step2.zip](https://github.com/arthurPuszynski/first-chart-article/raw/master/zips/step2.zip)**

## Step 3 - Prepare the data

![Image](https://www.freecodecamp.org/news/content/images/2019/12/data.gif)
_Source: giphy.com_

The CSV data format is exactly that – Comma Separated Values. The file contains rows (lines) and each row represents a record or entry. Normally the first row of values contains the names of each comma separated value (column). Subsequent rows contain the values themselves. 

```
name,age
chris,26
mike,34
```

CSV is human readable, but there are variations of this format. Sometimes if values contain commas (e.g. mailing addresses) the format doesn't work as-is so each value is also wrapped in quotes. That way the commas inside quotes are ignored and the format can still work by using only the commas outside of quotes to separate the values. 

```
"name","age","parents"
"Chris","26","Gregory, Mary"
"Mike","34","David, Sarah"
```

Values can also be separated using a different character like tabs in place of commas.

But let's not get bogged down in minutia. JSCharting provides a number of tools that help with this process and we will use one of them to skip worrying about the CSV file format and convert it to JSON (JavaScript Object Notation). The result will be an array of objects. Each object represents a row with named properties. The first row in the CSV file is used to define the names of those properties.

This is the url of the data we are interested in: [https://data.cdc.gov/resource/w9j2-ggv5.csv](https://data.cdc.gov/resource/w9j2-ggv5.csv).

You can click to download and open it in excel.

![Image](https://www.freecodecamp.org/news/content/images/2019/12/image-28.png)
_CSV file opened in Excel_

However, you will download and access this CSV data in real-time using JavaScript code. The code below may be slightly confusing at first, but it's short and you can reuse it to get any CSV, text, or JSON files over the internet programmatically. It is similar to the older AJAX technology but much simpler to use.

Once again, replace the content of the `index.js` file with the following:

```javascript
fetch('https://data.cdc.gov/resource/w9j2-ggv5.csv')
   .then(function (response) {
      return response.text();
   })
   .then(function (text) {
	csvToSeries(text);
   })
   .catch(function (error) {
      //Something went wrong
      console.log(error);
   });

function csvToSeries(text) {
   console.log(text);
}
```

Why so complicated? It is because when you request a file, it does not immediately become available. There is a delay and you have to wait for the file to arrive. So first you request the file from another website using `fetch()`.

```javascript
fetch('https://data.cdc.gov/resource/w9j2-ggv5.csv')
```

Then the code inside the `then(...)` argument function gets called with the response when it arrives. This function converts the response into text and returns it, which passes the result to the following `then()` argument function.

```javascript
.then(function (response) {
	return response.text();
})
```

The next `then(...)` argument function calls the `csvToSeries()` function, and passes the text as an argument.

```javascript
.then(function (text) {
	csvToSeries(text);
})
```

In the `catch()` function, you can specify what to do if anything goes wrong. For example maybe the internet is down, or the URL is not correct.

```javascript
.catch(function (error) {
	//Something went wrong
	console.log(error);
});
```

In this case, the error is sent to the console.

In the `csvToSeries()` function we pass this text to the console for inspection.

```javascript
function csvToSeries(text) {
   console.log(text);
}
```

? **Note:** The native `fetch()` function is not supported in Internet Explorer 11. If you want to support this browser as well, you can use the `JSC.fetch()` function which comes with JSCharting. It provides the same functionality, but adds additional support for IE11.

Drag the `index.html` file into a browser window (or refresh the page if already open) and press F12. This will open the DevTools window of the chrome browser. By default, the bottom half of the DevTools window will show the console output. This is where the text is sent when you run code like:

```javascript
console.log(text);
```

![Image](https://lh4.googleusercontent.com/C9pr4DISX6SwVwUdrSUz8s54gIuNgseApHISaR-C0HXkU-8OKaup09xhIeWjn7MvzWraT4uIEYPJU63ZVopGAHSshqxE64a6m8mHQlPiTVZUV0mAh4_p_3vBvSxWnqM0B9Vt3kLP)
_Console window output_

You can also paste or write code into this console window to execute it. Try pasting the entire code snippet above into the console window (next to the > character) and press enter. You will notice you get the same result in the console window output. This can be useful for testing a line of code and experimenting.

**[step3-a.zip](https://github.com/arthurPuszynski/first-chart-article/raw/master/zips/step3-a.zip)**

At this point you have retrieved the text of the CSV file over the internet and sent it to the console to prove that it works. Now we can start to work with it.

Let's take a look at this data file to get an idea of what's inside: [https://data.cdc.gov/resource/w9j2-ggv5.csv](https://data.cdc.gov/resource/w9j2-ggv5.csv)

I used excel to sort the rows by the year column to analyze the rows of data for a single year. 

![Image](https://www.freecodecamp.org/news/content/images/2019/12/image-27.png)
_The CSV data sorted by year._

Each year contains 9 rows with data based on race and sex. We are only interested in the highlighted male and female values of all races for each year. You will create two series based on the highlighted rows. A series for female and one for male values. 

Now that you have an idea of what needs to happen, let's get started.

First, let's use the `JSC.csv2Json()` function to convert the text into JSON format and pass it to the console to see what it does. 

Update the `csvToSeries()` function with the following code:


```javascript
function csvToSeries(text) {
   let dataAsJson = JSC.csv2Json(text);
   console.log(dataAsJson)
}
```

Refresh the browser to see the updated console output.   


![Image](https://www.freecodecamp.org/news/content/images/2019/12/image-29.png)
_CSV data converted to JSON using JSC.csv2Json() utility function_

The console shows an array of 1062 records. And this is one of these records:

```json
{year: 1900, race: "All Races", sex: "Both Sexes", average_life_expectancy: 47.3, mortality: 2518}
```

? **Note:** The console can display arrays, and objects for inspection and you can expand and collapse sections in the console to explore details.

The property name `average_life_expectancy` is a little long, but you will need to use it. To avoid typing it more than once, define a constant variable to store this name.  When you need to use this property, you can just write the variable name `lifeExp`. It will look like this `row[lifeExp]` instead of `row.average_life_expectancy`.

Add this line at the top of the `csvToSeries()` function.

```javascript
function csvToSeries(text) {
	const lifeExp = 'average_life_expectancy';
	...
```

You can process this data using simple vanilla JavaScript. The end result we want is two series with data points that include a year and life expectancy for each point.

Update the `csvToSeries()` with the following code:


```javascript
function csvToSeries(text) {
	const lifeExp = 'average_life_expectancy';
	let dataAsJson = JSC.csv2Json(text);
	let male = [], female = [];
	dataAsJson.forEach(function (row) {
		 //add either to male, female, or discard.
		console.log(row);
	});
}
```

It defines arrays for male and female data points. Then it calls the array `dataAsJson.forEach()` function passing a callback `function(row){...}` function as the argument. The `forEach()` function will execute the callback function for each item in the `dataAsJson` array. For now we will just call `console.log(row)` on each row that the callback function encounters.

Refresh the browser and inspect the console output. 

![Image](https://www.freecodecamp.org/news/content/images/2019/12/image-30.png)
_Each row object the callback function encountered_

Let's add some logic to filter the data we want and log the result in the console window. Replace the `csvToSeries()` function with this code.


```javascript
function csvToSeries(text) {
	const lifeExp = 'average_life_expectancy';
	let dataAsJson = JSC.csv2Json(text);
	let male = [], female = [];
	dataAsJson.forEach(function (row) {
		 //add either to male, female, or discard.
		if (row.race === 'All Races') {
			if (row.sex === 'Male') {
				male.push({x: row.year, y: row[lifeExp]});
			} else if (row.sex === 'Female') {
				female.push({x: row.year, y: row[lifeExp]});
			}
		}
	});
    console.log([male, female]);
}
```

Inside the callback function you decide whether the row is of interest and use it or if not then discard it. 

```javascript
if (row.race === 'All Races') {
	if (row.sex === 'Male') {
		//add data to male array
		male.push({x: row.year, y: row[lifeExp]});
	} else if (row.sex === 'Female') {
		//add data to female array
		female.push({x: row.year, y: row[lifeExp]});
	}
}
```

The logic checks to see if the `row.race` value equals 'All Races'. If so, then it checks to see if the `row.sex` property equals either 'Male' or 'Female'. If the row equals either, it adds the data to either the `male` or `female` arrays as a `{x, y}` point object. Notice the use of the `lifeExp` variable defined above which helps shorten this code.


At the end, you used `console.log([male, female])` to pass the male and female variables to the console for inspection and to make sure your code worked as expected.

After refreshing the browser, the console shows the result which is two arrays, each with 118 data points spanning the years 1900 to 2017.

![Image](https://lh6.googleusercontent.com/V3yi_ZyqpoOMvn8jr1Tb31obS1WPHbgJ8p1LkPirFMLu8rjmzUs5-CgVCvtsLLnXscGO7HxR8_IM02_Q1twFPRNa1ll5JCCOoQbuK_S0hxqA7IZNoAqskksO62nXXRoSedjwUmzg)
_The male and female point arrays_

Lastly, instead of passing the result to the console, wrap these data points within an array of two series that the chart can use directly and return them.

Add this code at the end of the `csvToSeries()` function:


```javascript
return [
   {name: 'Male', points: male},
   {name: 'Female', points: female}
];
```

If the returned value was sent to the console, it would produce this result.  


![Image](https://lh6.googleusercontent.com/_xlnsylk8kbv1u9-Fw4K0dnmJ7J_UBzhbhrWT8j48S4xtr04gYezHIITd_cNWQ5ZvJvi4MPdqi_IIat-JSfmRiOZT7jDzco5JYSstOzec67OxAQ-LCB7zuyqm20gxV8FYEm1XL0d)
_Two series objects the chart can consume directly_

As you can see, the logic for filtering rows is fairly simple and you can adjust it to get other details from this data set. 

To learn more about handling CSV files using JSCharting utilities, see this [tutorial](https://jscharting.com/tutorials/js-chart-data/client-side/fetch-csv-and-json/). When you are ready for more advanced data handling, the [JSC.nest() utility](https://jscharting.com/tutorials/js-chart-data/client-side/data-nesting/) can be used to create series and points from JSON data with with very little code. 

[**step3-b.zip**](https://github.com/arthurPuszynski/first-chart-article/raw/master/zips/step3-b.zip)

## Step 4 - Putting it all together

The data handling section was the most difficult step, but that alone will enable you to manipulate and extract data of interest from any CSV file. This is where it all comes together and where you will feel a sense of accomplishment. 

Start by adding a `renderChart()` function to the end of the `index.js` file. You will pass the series data to this function as an argument. 


```javascript
function renderChart(series){
   JSC.Chart('chartDiv', {
      series: series
   });
}
```

In the `then()` argument function that calls `csvToSeries()`, pass the series result to the `renderChart()` function to see what it draws in the browser.

```javascript
.then(function (text) {
	let series = csvToSeries(text);
	renderChart(series);
})
```

**[step4-a.zip](https://github.com/arthurPuszynski/first-chart-article/raw/master/zips/step4-a.zip)**

Now, refresh the browser. You should see this chart that uses the CSV data you processed in the previous section. Sweet! ?

![Line chart showing filtered CSV data](https://www.freecodecamp.org/news/content/images/2019/12/csv-line-chart.png)
_Line chart showing filtered CSV data_

Whoa, what happened in 1918? Life expectancy dropped significantly there. According to Wikipedia there was a [flu pandemic](https://en.wikipedia.org/wiki/Spanish_flu) involving H1N1 virus that wiped out a portion of the world population. This unfortunate event shows how visualizing data provides insights you would not normally get from just looking at the numbers.

You created a chart using the default line series type and it looks good, but you can make a few adjustments and tweaks to further improve it.

First, add a title at the top to explain what the viewer is looking at and an annotation at the bottom of the chart to credit the data source. Update the `JSC.Chart()` constructor function to pass the following options:


```javascript
function renderChart(series){
	JSC.Chart('chartDiv', {
		title_label_text: 'Life Expectancy in the United States',
		annotations: [{
			label_text: 'Source: National Center for Health Statistics',
			position: 'bottom left'
		}],
		series: series
	});
}

```

When you refresh the browser you can see the updated chart.

![Line chart with title and annotation for attribution](https://www.freecodecamp.org/news/content/images/2019/12/line-chart-annotations.png)
_Line chart with title and annotation for attribution_

You added an annotation with label text, and a position setting. We can use another annotation for the title as well, but it was easier to use the title label in this example. 

It is easy to control the annotation position using values such as `'top right'` or `'inside bottom right'`. The `'inside'` value means the annotation is placed inside the chart area where data is drawn. This [box positions chart example](https://jscharting.com/examples/chart-features/annotation/box-positions/) demonstrates all the position setting options.

The legend shows the sum of point values for each series, but the sum is not important for this data set. You can reduce the legend columns to only show the icon and series name by using this setting:

```javascript
legend_template: '%icon,%name'
```

But you don't really need to use a legend at all. It will be cleaner to simply label the lines themselves. You can disable the legend, and tell the chart to write the series name on the last point of each line series with these chart options:

```javascript
legend_visible: false,
defaultSeries_lastPoint_label_text: '<b>%seriesName</b>',

```

![Line chart using point labels instead of a legend](https://www.freecodecamp.org/news/content/images/2019/12/csv-line-chart-labels.png)
_Line chart using point labels instead of a legend_

The `'%seriesname'` token is one of many [point related tokens](https://jscharting.com/tutorials/js-chart-labels/token-reference/#point-tokens) that can be used in any point label text to show point details and calculations. 

Finally, let’s enable the x axis crosshair combined tooltip to show the male and female life expectancy for any given year. On mobile devices, you can tap the chart to see the crosshair tooltip. When using a PC, tooltips display when hovering over the chart with your mouse pointer.

```javascript
xAxis_crosshair_enabled: true,
```

You may be wondering, what's with all those underscores in property names? This is not the actual property name. It's a shorthand way to write:

```javascript
xAxis: {crosshair: {enabled: true}},
```

You may find it more convenient to specify a setting with underscores and JSCharting will understand what you mean. 


The default tooltip text is clear, but let's customize it slightly to make it our own. 

![Image](https://www.freecodecamp.org/news/content/images/2019/12/image-60.png)
_Default combined tooltip_

Since the crosshair tooltip shows information about each point it crosses, the tooltip text is defined within the point options. The `defaultPoint` property defines point options that all points will inherit automatically.

```javascript
defaultPoint_tooltip: '%seriesName <b>%yValue</b> years',
```

![Image](https://www.freecodecamp.org/news/content/images/2019/12/image-61.png)
_Customized combined tooltip_

For more information about this feature, check out the [crosshair and combined tooltip tutorial](https://jscharting.com/tutorials/js-chart-interactivity/crosshair-combined-tooltip/).

When you apply all these options, your code will look similar to the following snippet. Replace the entire `renderChart()` function with this code.


```javascript
function renderChart(series){
	JSC.Chart('chartDiv', {
		title_label_text: 'Life Expectancy in the United States',
		annotations: [{
			label_text: 'Source: National Center for Health Statistics',
			position: 'bottom left'
		}],
        legend_visible: false,
		defaultSeries_lastPoint_label_text: '<b>%seriesName</b>',
		defaultPoint_tooltip: '%seriesName <b>%yValue</b> years',
		xAxis_crosshair_enabled: true,
		series: series
	});
}

```

Refresh the browser window once more.

![Line chart with crosshairs and customized combined tooltips](https://www.freecodecamp.org/news/content/images/2019/12/csv-line-chart-tooltips.png)
_Line chart with crosshairs and customized combined tooltips_

You did it! 

![Image](https://www.freecodecamp.org/news/content/images/2019/12/congratulations.gif)
_Source: giphy.com_

First you fetched CSV data using native JavaScript. You then converted it into JSON format and filtered the data into two series. With those series you created a beautiful interactive line chart using JSCharting and configured it to look professional. 

You can customize and adjusted the charts further to meet your specific needs. Visit the JSCharting [tutorials](https://jscharting.com/tutorials/) section to learn more about a specific topic, or find charts similar to what you want to make in the [examples gallery](https://jscharting.com/examples/chart-types/) and copy them to continue your data visualization journey.

If you run into problems working with JSCharting, feel free to [contact](https://jscharting.com/support.htm) the support team. They will be happy to guide you or help resolve any issues you may encounter.

**[step4-b.zip](https://github.com/arthurPuszynski/first-chart-article/raw/master/zips/step4-b.zip)**

## Bonus Challenge

We did not use all the data available in in that CSV file. Let's experiment with it for fun and practice.

Create this chart using what you have learned.

![Challenge: Replicate this chart on your own](https://www.freecodecamp.org/news/content/images/2019/12/bonus-trend-line-chart.png)
_Challenge: Replicate this chart on your own_

This zip file contains the answer:

**[step5-bonus.zip](https://github.com/arthurPuszynski/first-chart-article/raw/master/zips/step5-bonus.zip)**

Can you think of other charts you can make with this data? Keep experimenting and enjoy every minute of it!

