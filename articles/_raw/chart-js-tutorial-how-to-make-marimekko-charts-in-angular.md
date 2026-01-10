---
title: Chart.js Tutorial – How to Make Marimekko Charts in Angular
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-03-21T17:51:26.000Z'
originalURL: https://freecodecamp.org/news/chart-js-tutorial-how-to-make-marimekko-charts-in-angular
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/austin-distel-DfjJMVhwH_8-unsplash.jpg
tags:
- name: Angular
  slug: angular
- name: chartjs
  slug: chartjs
- name: charts
  slug: charts
- name: data visualization
  slug: data-visualization
seo_title: null
seo_desc: "By Swatej Patil\nData visualization is an essential part of data analysis.\
  \ And charts are one of the most effective ways to present data in a clear and concise\
  \ manner. \nMarimekko charts are an excellent choice for displaying complex data\
  \ sets in a com..."
---

By Swatej Patil

Data visualization is an essential part of data analysis. And charts are one of the most effective ways to present data in a clear and concise manner. 

Marimekko charts are an excellent choice for displaying complex data sets in a compact and visually appealing format. 

A Marimekko chart, also known as a mosaic chart or mekko chart, is a combination of a stacked bar chart and a 100% stacked bar chart. The width of each bar represents the total value of the corresponding category, and the height of each bar represents the relative contribution of each sub-category to that total. 

In this tutorial, we will explore how to create a Marimekko chart using Chart.js, a powerful charting library. We'll delve into the details of how to structure the data for Marimekko charts, as well as how to customize the chart's appearance and behavior using Chart.js options and APIs.

# **Getting Started**

I am assuming that you already have familiarity with creating simple line and bar charts using Chart.js in an Angular application. In this guide, there are certain concepts that will be easier to comprehend if you have prior knowledge.

Don't worry if you don't – I've got you covered. You can follow my [Chart.js Tutorial – How to Make Bar and Line Charts in Angular](https://www.freecodecamp.org/news/how-to-make-bar-and-line-charts-using-chartjs-in-angular/) to get started.

## How to Structure Data for Marimekko Charts

Let's discuss the data structure required for Marimekko charts before creating the chart. 

Marimekko charts need an array of objects, with each object representing a category. Each object must have a label and a sub-array of objects, where each sub-object represents a sub-category. 

Each sub-object must have a label and a value. The value represents the proportion of the sub-category in relation to the total of its category.

Here's an example of how to structure data for a Marimekko chart:

```jsx
data: [
  {
    label: 'Category 1',
    subcategories: [
      { label: 'Subcategory 1', value: 10 },
      { label: 'Subcategory 2', value: 20 },
      { label: 'Subcategory 3', value: 30 }
    ]
  },
  {
    label: 'Category 2',
    subcategories: [
      { label: 'Subcategory 1', value: 40 },
      { label: 'Subcategory 2', value: 50 },
      { label: 'Subcategory 3', value: 60 }
    ]
  }
]

```

In this example, we have two categories: Category 1 and Category 2, with three subcategories each. The values for the subcategories represent the proportion of the subcategory in relation to the total of its category. For example, in Category 1, Subcategory 1 represents 10 out of 60, or 16.7% of the total.

## How to Create a Marimekko Chart with Chart.js

Now that we have our data structured correctly, let's move on to creating our Marimekko chart using Chart.js. 

First, we need to create a canvas element in our HTML code to hold the chart:

```jsx
<canvas id="marimekkoChart"></canvas>

```

Next, we'll need to install Chart.js and import it into our Angular component:

```jsx
npm install chart.js

```

```jsx
import Chart from 'chart.js/auto';

```

In our component class, we can then create a new Chart object and pass in our data and options:

```jsx
ngAfterViewInit() {
  const canvas = document.getElementById('marimekkoChart') as HTMLCanvasElement;
  const ctx = canvas.getContext('2d') as CanvasRenderingContext2D;

  const data = {
    labels: ['Category 1', 'Category 2'],
    datasets: [
      {
        label: 'Subcategory 1',
        data: [10, 40],
        backgroundColor: 'rgba(255, 99, 132, 0.7)',
        borderWidth: 1
      },
      {
        label: 'Subcategory 2',
        data: [20, 50],
        backgroundColor: 'rgba(54, 162, 235, 0.7)',
        borderWidth: 1
      },
      {
        label: 'Subcategory 3',
        data: [30, 60],
        backgroundColor: 'rgba(255, 206, 86, 0.7)',
        borderWidth: 1
      }
    ]
  };

  const options = {
    indexAxis: 'y',
    plugins: {
      legend: {
        position: 'bottom'
      }
    }
  };

  const marimekkoChart = new Chart(ctx, {
    type: 'bar',
    data: data,
  });
}

```

In this example, we're creating a Marimekko chart with three subcategories for two categories. We've set the type of chart to 'bar', and we're passing in our data and options. The 'indexAxis' option is set to 'y' to make the chart horizontal, and the 'legend' option is set to position the legend at the bottom of the chart.

Congratulations! If you have followed along carefully then you shouldn’t run into any errors and your output may look like the following:

![Image](https://www.freecodecamp.org/news/content/images/2023/03/Mekkochart.png)

And that's it! With this code, we can create a Marimekko chart in Chart.js in Angular. 

You can further customize your chart using various Chart.js options and APIs, such as adjusting the colors, labels, and tooltip behaviors, to make it even more informative and engaging.

# C**onclusion**

Chart.js is a very useful and powerful library. In this quick tutorial, we've covered how to create a Marimekko chart in Chart.js in Angular. If you want to include any type of chart in your Angular application, then it is very easy to make them with Chart.js.

The full code for this Angular application is hosted on my [GitHub Repo](https://github.com/SwatejPatil/Chart.js-Tutorial-How-to-Make-a-Marimekko-Chart-in-Angular).

I hope you found this tutorial helpful and informative. If you have any questions or feedback, feel free to to contact me on [LinkedIn](http://www.linkedin.com/in/swatejpatil/)!

### **Related Articles I've Written about Chart.js:**

* [How to Make Bar and Line Charts using Chart.js in Angular](https://www.freecodecamp.org/news/chart-js-zooom-plugin/)
* [Chart.js Tutorial – How to Make Pie and Doughnut Charts in Angular](https://www.freecodecamp.org/news/how-to-make-pie-and-doughnut-charts-using-chartjs-in-angular/)
* [How to Add the Chart.js Zoom Plugin to an Angular App](https://www.freecodecamp.org/news/chart-js-zooom-plugin/)

Photo by [Austin Distel](https://unsplash.com/@austindistel?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/photos/DfjJMVhwH_8?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText).

