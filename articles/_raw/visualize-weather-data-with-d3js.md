---
title: How to Visualize Weather Data with D3.js
subtitle: ''
author: Spruce Emmanuel
co_authors: []
series: null
date: '2022-01-17T16:59:10.000Z'
originalURL: https://freecodecamp.org/news/visualize-weather-data-with-d3js
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/reza-shayestehpour-Nw_D8v79PM4-unsplash.jpg
tags:
- name: D3.js
  slug: d3js
- name: data visualization
  slug: data-visualization
seo_title: null
seo_desc: 'What plans would you make if you knew it was going to rain tomorrow?

  This can be a crucial question to ask yourself when it comes to planning your personal
  and day-to-day business activities.

  For example, I have a friend who runs an app-based laundry...'
---

What plans would you make if you knew it was going to rain tomorrow?

This can be a crucial question to ask yourself when it comes to planning your personal and day-to-day business activities.

For example, I have a friend who runs an app-based laundry business in Lagos, Nigeria. He relies heavily on sunshine, and sometimes it rains, or there's just no sunshine. On those days, business is very bad.

But what if he knew it was going to rain the next day or in 6 hours? That would help him plan things well in advance and prevent delays in orders. But where can he get such information?

That's where the Tomorrow.io [weather API](https://www.tomorrow.io/weather-api/) comes in. The weather API provides us with accurate and fast weather data in real time, like precipitation probability, amount of rainfall, temperature, wind speed, and more.

Such information is very useful to businesses across various industries like transportation, agriculture, and, in my friend's case, laundry shops.

Also, the weather data from this API can be easily integrated into your project or any program you are working with. The best part – the free version of the API is extremely powerful on its own, so that's what we'll use today.

In this article, we'll use the Tomorrow.io weather API and [D3.js](https://d3js.org/) to forecast and visualize the precipitation probability of a particular location on a line chart. A service like this would allow my friend to tell on which days of the week it is likely to rain.

## Project Requirements

What do you need to continue in this tutorial? Basic knowledge of JavaScript and D3.js is required.

I suggest reading a [beginner's guide to D3.js](https://www.freecodecamp.org/news/d3js-tutorial-data-visualization-for-beginners/) if you want to refresh your memory before going further.

## Getting Started

First, create an HTML file, and add the latest library of `d3.js` to the HTML file. Also, create an empty `svg` element, like so:

```xml
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Tomorrow.io Rainfall probability</title>
    <script src="https://d3js.org/d3.v7.min.js"></script>
  </head>
  <body>
    <svg></svg>
  </body>
  <script src="index.js"></script>
</html>
```

## How to Set Up the Margins

At some point, our visualizations will need some space (margins). It is a convention in `d3.js` to set up the **margin convention**.

For this, you need to define the margins for the four sides, create an `index.js` file, and add the following:

`const margin = { left: 120, right: 30, top: 60, bottom: 30 }`

Now, let's set the width and viewBox of our SVG element. This will help make it responsive.

```js
const width = document.querySelector("body").clientWidth,
  height = 500;

const svg = d3.select("svg").attr("viewBox", [0, 0, width, height]);
```

## How to Define the Scales

The d3.scale function takes in data as input and returns a visual value in pixels. d3.scale needs to be set with a **domain** and a **range.** The domain sets a LIMIT for the data we are trying to represent visually.

As seen above, we need to set the range of the scales. We'll set the `domain` once we fetch our data:

```js
const x_scale = d3.scaleTime().range([margin.left, width - margin.right]);
const y_scale = d3.scaleLinear().range([height - margin.bottom - margin.top, margin.top]);
```

## How to Add a Title and Labels

Next, we need to add a title and labels to our visualizations. This is useful for explaining our graph to our users.

Edit your `script.js` and add the following code:

```js
// labels
const x_label = "Time";
const y_label = "Rainfall Probability";
const location_name = "Lagos Nigeria";

// add title
svg
  .append("text")
  .attr("class", "svg_title")
  .attr("x", (width - margin.right + margin.left) / 2)
  .attr("y", margin.top / 2)
  .attr("text-anchor", "middle")
  .style("font-size", "22px")
  .text(`${y_label} of ${location_name}`);
// add y label
svg
  .append("text")
  .attr("text-ancho", "middle")
  .attr(
    "transform",
    `translate(${margin.left - 70}, ${
      (height - margin.top - margin.bottom + 180) / 2
    }) rotate(-90)`
  )
  .style("font-size", "26px")
  .text(y_label);
// add x label
svg
  .append("text")
  .attr("class", "svg_title")
  .attr("x", (width - margin.right + margin.left) / 2)
  .attr("y", height - margin.bottom - margin.top + 60)
  .attr("text-anchor", "middle")
  .style("font-size", "26px")
  .text(x_label);
```

With the above-added title and labels, the preview looks like this:

![Added titles and labels to our visualization](https://paper-attachments.dropbox.com/s_80A2ED9660649A0944547FE32AE888AF070E268C15D560C813DD3420036CDBBE_1638557381465_tomorrow.io-demo1.png align="left")

## How to Create the Line Chart

Here, the first thing we'll need to do is to generate the [path](https://sharkcoder.com/data-visualization/d3-line-chart) for our chart. D3.js provides a `.line()` method that pretty much generates the line path for you. Let's add the line generator:

```js
const start_time = (d) => new Date(d.startTime);
const temperature = (d) => +d.values.precipitationProbability;

const line_generator = d3.line()
  .x((d) => x_scale(start_time(d)))
  .y((d) => y_scale(temperature(d)))
  .curve(d3.curveBasis);
```

Now that we have defined our line generator, let's go ahead and fetch our data.

## How to Fetch Data from the [Tomorrow.io](http://Tomorrow.io) Weather API

D3 provides us with a `.json()` method to fetch JSON data from an API or a local file.

Before you can fetch data using the [Tomorrow.io](http://Tomorrow.io) weather API, you'll need a secret access token. To get this token, all you need to do is create an account with [Tomorrow.io](http://Tomorrow.io). Yes, it's that easy.

Once you have created your account, go ahead and log in. Then, on your [dashboard](https://app.tomorrow.io/development/keys), you should see your API secret token:

![Image](https://paper-attachments.dropbox.com/s_80A2ED9660649A0944547FE32AE888AF070E268C15D560C813DD3420036CDBBE_1638566467761_tomorrow.io-demo2.png.png align="left")

Add the following code to fetch the data:

```js
const lat = 6.465422; // latitude of Lagos, Nigeria
const long = 3.406448; // Longitude of Lagos, Nigeria

const api_key = "your-api-key-here";

const url = `https://api.tomorrow.io/v4/timelines?location=${lat},${long}&fields=snowAccumulation,precipitationProbability,precipitationType&timesteps=1h&units=metric&apikey=${api_key}`;

d3.json(url).then(({ data }) => {
  const d = data.timelines[0].intervals;
  console.log(d)
});
```

Here is an example of the JSON data returned from that fetch:

```json
{
  "data": {
    "timelines": [
      {
        "timestep": "1h",
        "startTime": "2021-12-03T13:00:00Z",
        "endTime": "2021-12-08T01:00:00Z",
        "intervals": [
          {
            "startTime": "2021-12-03T13:00:00Z",
            "values": {
              "snowAccumulation": 0,
              "precipitationProbability": 0,
              "precipitationType": 0
            }
          },
          // 108 more data
        ]
      }
    ]
  }
}
```

Now that we've fetched our data, let's generate our line chart:

```js
d3.json(url).then(({ data }) => {
  const d = data.timelines[0].intervals;
  
// set the domain 
  x_scale.domain(d3.extent(d, start_time)).nice(ticks);
  y_scale.domain(d3.extent(d, temperature)).nice(ticks);
  // add the line path
  svg
    .append("path")
    .attr("fill", "none")
    .attr("stroke", "steelblue")
    .attr("stroke-width", 4)
    .attr("d", line_generator(d)); // generate the path
});
```

The above code gives us a basic chart:

![Image](https://paper-attachments.dropbox.com/s_80A2ED9660649A0944547FE32AE888AF070E268C15D560C813DD3420036CDBBE_1638560607910_tomorrow.io-demo3.png align="left")

## How to Add the Axes

Even with the above line chart, you will have a hard time knowing exactly which day or hour has the highest possibility of rainfall.

We can resolve this by adding the time and rainfall probability (in %) axes.

First, define the axes just below your scales:

```js
const ticks = 10;
const x_axis = d3.axisBottom()
  .scale(x_scale)
  .tickPadding(10)
  .ticks(ticks)
  .tickSize(-height + margin.top * 2 + margin.bottom);
const y_axis = d3.axisLeft()
  .scale(y_scale)
  .tickPadding(5)
  .ticks(ticks, ".1")
  .tickSize(-width + margin.left + margin.right);

// format our ticks to get accurate %
y_axis.tickFormat((d) => {
  if (!Number.isInteger(d)) {
    d = decimalFormatter(d);
  }
  return d + "%";
});
```

Finally, let's add our axis on the SVG element:

```js
// append x axis
  svg
    .append("g")
    .attr("transform", `translate(0,${height - margin.bottom - margin.top})`)
    .call(x_axis);

  // add y axis
  svg
    .append("g")
    .attr("transform", `translate(${margin.left},0)`)
    .call(y_axis);
```

With the axis added, our line chart now looks like this:

![Tomorrow.io precipitation probality of lagos, Nigeria. December 03, 2021](https://paper-attachments.dropbox.com/s_80A2ED9660649A0944547FE32AE888AF070E268C15D560C813DD3420036CDBBE_1638561615864_tomorrow.io-demo4.png align="left")

That's much better! You can now tell which day and hour has the highest probability of rainfall.

The full code and demo for this example is hosted on Codepen:

%[https://codepen.io/Spruce_khalifa/pen/vYeNKRg] 

## Conclusion

With the power of D3.js combined with the [Tomorrow.io](http://Tomorrow.io) weather API, we can create visualizations that help users solve weather-related issues affecting their businesses.

I hope you found this tutorial helpful.

Happy Coding!

Cover photo by [Reza Shayestehpour](https://unsplash.com/@r_shayesrehpour) on Unsplash
