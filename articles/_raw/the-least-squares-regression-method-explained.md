---
title: The Least Squares Regression Method – How to Find the Line of Best Fit
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-09-08T18:59:02.000Z'
originalURL: https://freecodecamp.org/news/the-least-squares-regression-method-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c98d1740569d1a4ca1c34.jpg
tags:
- name: Advanced Mathematics
  slug: advanced-mathematics
- name: Math
  slug: math
- name: Mathematics
  slug: mathematics
- name: '#Regression'
  slug: regression
seo_title: null
seo_desc: 'By Diogo Spínola

  Would you like to know how to predict the future with a simple formula and some
  data?

  There are multiple ways to tackle the problem of attempting to predict the future.
  But we''re going to look into the theory of how we could do it wi...'
---

By Diogo Spínola

Would you like to know how to predict the future with a simple formula and some data?

There are multiple ways to tackle the problem of attempting to predict the future. But we're going to look into the theory of how we could do it with the formula **Y = a + b * X**.

After we cover the theory we're going to be creating a JavaScript project. This will help us more easily visualize the formula in action using [Chart.js](https://www.chartjs.org/) to represent the data.

## What is the Least Squares Regression method and why use it?

Least squares is a method to apply linear regression. It helps us predict results based on an existing set of data as well as clear anomalies in our data. Anomalies are values that are too good, or bad, to be true or that represent rare cases.

For example, say we have a list of how many topics future engineers here at freeCodeCamp can solve if they invest 1, 2, or 3 hours continuously. Then we can predict how many topics will be covered after 4 hours of continuous study even without that data being available to us.

This method is used by a multitude of professionals, for example statisticians, accountants, managers, and engineers (like in machine learning problems).

## Setting up an example

Before we jump into the formula and code, let's define the data we're going to use.

To do that let's expand on the example mentioned earlier. 

Let's assume that our objective is to figure out how many topics are covered by a student per hour of learning. 

Each pair (X, Y) will represent a student. Since we all have different rates of learning, the number of topics solved can be higher or lower for the same time invested.

| Hours (X) 	| Topics Solved (Y) 	|
|:---------:	|:-----------------:	|
| 1       	    | 1.5               	|
| 1.2         	| 2                 	|
| 1.5       	| 3                 	|
| 2         	| 1.8               	|
| 2.3       	| 2.7               	|
| 2.5       	| 4.7               	|
| 2.7       	| 7.1               	|
| 3         	| 10                	|
| 3.1       	| 6                 	|
| 3.2       	| 5                 	|
| 3.6       	| 8.9               	|

You can read it like this: "Someone spent 1 hour and solved 2 topics" or "One student after 3 hours solved 10 topics".

In a graph these points look like this:

![Image](https://www.freecodecamp.org/news/content/images/2020/09/image-8.png)
_Each point is a student (X, Y) and how long it took that specific student to complete a certain number of topics_

**Disclaimer:** This data is fictional and was made by hitting random keys. I have no idea of the actual values.

## The formula

> **Y = a + bX**

The formula, for those unfamiliar with it, probably looks underwhelming – even more so given the fact that we already have the values for **Y** and **X** in our example.

Having said that, and now that we're not scared by the formula, we just need to figure out the **a** and **b** values.

To give some context as to what they mean:

* **a** is the intercept, in other words the value that we expect, on average, from a student that practices for one hour. One hour is the least amount of time we're going to accept into our example data set.
* **b** is the slope or coefficient, in other words the number of topics solved in a specific hour (**X)**. As we increase in hours (**X**) spent studying, **b** increases more and more.

## Calculating "b"

![Image](https://www.freecodecamp.org/news/content/images/2020/08/image-50.png)
_Looks scarier than it is_

**X** and **Y** are our positions from our earlier table. When they have a **-** (macron) above them, it means we should use the average which we obtain by summing them all up and dividing by the total amount:

**͞x** -> 1+1.2+1.5+2+2.3+2.5+2.7+3+3.1+3.2+3.6 = **2.37**

**͞y** -> 1,5+2+3+1,8+2,7+4,7+7,1+10+6+5+8,9 / 11 = **4.79**

Now that we have the average we can expand our table to include the new results:

| Hours (X) 	| Topics Solved (Y) 	| (X - ͞x) 	| (y - ͞y) 	| (X - ͞x)*(y - ͞y) 	| (x - ͞x)² 	|
|:---------:	|:-----------------:	|:-------:	|:-------:	|:---------------:	|:--------:	|
|     1     	|        1.5        	|   -1.37 	|  -3.29  	|            4.51 	|     1.88 	|
|    1.2    	|         2         	|   -1.17 	|  -2.79  	|            3.26 	|     1.37 	|
|    1.5    	|         3         	|   -0.87 	|  -1.79  	|            1.56 	|     0.76 	|
|     2     	|        1.8        	|   -0.37 	|  -2.99  	|            1.11 	|     0.14 	|
|    2.3    	|        2.7        	|   -0.07 	|  -2.09  	|            0.15 	|     0.00 	|
|    2.5    	|        4.7        	|    0.13 	|  -0.09  	|           -0.01 	|     0.02 	|
|    2.7    	|        7.1        	|    0.33 	|   2.31  	|            0.76 	|     0.11 	|
|     3     	|         10        	|    0.63 	|   5.21  	|            3.28 	|     0.40 	|
|    3.1    	|         6         	|    0.73 	|   1.21  	|            0.88 	|     0.53 	|
|    3.2    	|         5         	|    0.83 	|   0.21  	|            0.17 	|     0.69 	|
|    3.6    	|        8.9        	|    1.23 	|   4.11  	|            5.06 	|     1.51 	|

The weird symbol sigma (**∑**) tells us to sum everything up:

**∑(x - ͞x)*(y - ͞y)** -> 4.51+3.26+1.56+1.11+0.15+-0.01+0.76+3.28+0.88+0.17+5.06 = **20.73**

**∑(x - ͞x)²** -> 1.88+1.37+0.76+0.14+0.00+0.02+0.11+0.40+0.53+0.69+1.51 = **7.41**

And finally we do **20.73 / 7.41** and we get **b = 2.8**

**Note:** When using an expression input calculator, like the one that's available in Ubuntu, -2² returns -4 instead of 4. To avoid that input (-2)².

## Calculating "a"

All that is left is **a**, for which the formula is **͞͞͞y = a +** **b ͞x.** We've already obtained all those other values, so we can substitute them and we get:

* 4.79 = **a** + 2.8*2.37
* 4.79 = **a** + 6.64
* **a** = -6.64+4.79
* **a = -1.85**

## The result

Our final formula becomes:

> **Y = -1.85 + 2.8*X**

Now we replace the **X** in our formula with each value that we have:

| Hours (X) 	| -1.85 + 2.8 * X 	|
|:---------:	|:---------------:	|
|     1     	|       0.95      	|
|    1.2    	|       1.51      	|
|    1.5    	|       2.35      	|
|     2     	|       3.75      	|
|    2.3    	|       4.59      	|
|    2.5    	|       5.15      	|
|    2.7    	|       5.71      	|
|     3     	|       6.55      	|
|    3.1    	|       6.83      	|
|    3.2    	|       7.11      	|
|    3.6    	|       8.23      	|

Which is a graph that looks something like this:

![Image](https://www.freecodecamp.org/news/content/images/2020/09/image-9.png)
_We now have a line that represents how many topics we expect to be solved for each hour of study_

If we want to predict how many topics we expect a student to solve with 8 hours of study, we replace it in our formula:

* **Y = -1.85 + 2.8*8**
* **Y = 20.55**

An in a graph we can see:

![Image](https://www.freecodecamp.org/news/content/images/2020/09/image-10.png)
_The further it is in the future the least accuracy we should expect_

## Limitations

Always bear in mind the limitations of a method. This will hopefully help you avoid incorrect results.

And this method, like any other, has its limitations. Here are a couple:

* It doesn't take into account the complexity of the topics solved. A topic covered at the start of the "[Responsive Web Design Certification](https://www.freecodecamp.org/learn/responsive-web-design/basic-html-and-html5/)" will most likely take less time to learn and solve than doing one of the final projects. So if the data we have is from different starting points of a course, the predictions won't be accurate
* It's impossible for someone to study 240 hours continuously or to solve more topics than those available. Regardless, the method allows us to predict those values. At that point the method is no longer accurately giving results since it's an impossibility.

## Example JavaScript Project

Doing this by hand is not necessary. We can create our project where we input the X and Y values, it draws a graph with those points, and applies the linear regression formula.

The project folder will have the following contents:

```
src/
  |-public // folder with the content that we will feed to the browser
    |-index.html
    |-style.css
    |-least-squares.js
  package.json
  server.js // our Node.js server
```

And **package.json**:

```json
{
  "name": "least-squares-regression",
  "version": "1.0.0",
  "description": "Visualize linear least squares",
  "main": "server.js",
  "scripts": {
    "start": "node server.js",
    "server-debug": "nodemon --inspect server.js"
  },
  "author": "daspinola",
  "license": "MIT",
  "devDependencies": {
    "nodemon": "2.0.4"
  },
  "dependencies": {
    "express": "4.17.1"
  }
}

```

Once we have the package.json and we run _npm install_ we will have Express and nodemon available. You can switch them out for others as you prefer, but I use these out of convenience.

In **server.js**:

```js
const express = require('express')
const path = require('path')

const app = express()

app.use(express.static(path.join(__dirname, 'public')))

app.get('/', function(req, res) {
  res.sendFile(path.join(__dirname, 'public/index.html'))
})

app.listen(5000, function () {
  console.log(`Listening on port ${5000}!`)
})
```

This tiny server is made so we can access our page when we write in the browser _localhost:5000._ Before we run it let's create the remaining files:

**public/index.html**

```html
<html>
  <head>
    <title>Least Squares Regression</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js@2.9.3/dist/Chart.min.js"></script>
    <link rel="stylesheet" href="style.css">
  </head>
  <body>
    <div class="container">
      <div class="left-half">
        <div>
          <input type="number" class="input-x" placeholder="X">
          <input type="number" class="input-y" placeholder="Y">

          <button class="btn-update-graph">Add</button> 
        </div>
        <div>
          <span class="span-formula"></span>
        </div>
        <div>
          <table class="table-pairs">
            <thead>
              <th>
                X
              </th>
              <th>
                Y
              </th>
            </thead>
            <tbody></tbody>
          </table>
        </div>
      </div>
      <div class="right-half">
        <canvas id="myChart"></canvas>
      </div>
    </div>
    <script src="/js/least-squares.js"></script>
  </body>
</html>
```

We create our elements:

* Two inputs for our pairs, one for X and one for Y
* A button to add those values to a table
* A span to show the current formula as values are added
* A table to show the pairs we've been adding
* And a canvas for our chart

We also import the [Chart.js](https://www.chartjs.org/) library with a CDN and add our CSS and JavaScript files.

**public/style.css**

```css
.container {
  display: grid; 
}

.left-half {
  grid-column: 1;
}

.right-half {
  grid-column: 2;
}
```

We add some rules so we have our inputs and table to the left and our graph to the right. This takes advantage of CSS grid.

**public/least-squares.js**

```js
document.addEventListener('DOMContentLoaded', init, false);

function init() {
  const currentData = {
    pairs: [],
    slope: 0,
    coeficient: 0,
    line: [],
  };

  const chart = initChart();
}
 
function initChart() {
  const ctx = document.getElementById('myChart').getContext('2d');

  return new Chart(ctx, {
    type: 'scatter',
    data: {
      datasets: [{
        label: 'Scatter Dataset',
        backgroundColor: 'rgb(125,67,120)',
        data: [],
      }, {
        label: 'Line Dataset',
        fill: false,
        data: [],
        type: 'line',
      }],
    },
    options: {
      scales: {
        xAxes: [{
          type: 'linear',
          position: 'bottom',
          display: true,
          scaleLabel: {
            display: true,
            labelString: '(X)',
          },
        }],
        yAxes: [{
          type: 'linear',
          position: 'bottom',
          display: true,
          scaleLabel: {
            display: true,
            labelString: '(Y)',
          },
        }],
      },
    },
  });
}
```

And finally, we initialize our graph. At the start, it should be empty since we haven't added any data to it just yet.

Now if we run _npm run server-debug_ and open our browser on localhost:5000 we should see something like this:

![Image](https://www.freecodecamp.org/news/content/images/2020/09/image-12.png)
_Our inputs to the left with an add button, or table with just the headers X and Y, to the right an empty graph_

## Adding functionality

The next step is to make the "Add" button do something. In our case we want to achieve:

* Add the X and Y values to the table
* Update the formula when we add more than one pair (we need at least 2 pairs to create a line)
* Update the graph with the points and the line
* Clean the inputs, just so it's easier to keep introducing data

### Add the values to the table

**public/least-squares.js**

```js
document.addEventListener('DOMContentLoaded', init, false);

function init() {
  const currentData = {
    pairs: [],
    slope: 0,
    coeficient: 0,
    line: [],
  };
  const btnUpdateGraph = document.querySelector('.btn-update-graph');
  const tablePairs = document.querySelector('.table-pairs');
  const spanFormula = document.querySelector('.span-formula');

  const inputX = document.querySelector('.input-x');
  const inputY = document.querySelector('.input-y');

  const chart = initChart();

  btnUpdateGraph.addEventListener('click', () => {
    const x = parseFloat(inputX.value);
    const y = parseFloat(inputY.value);

    updateTable(x, y);
  });
  
  function updateTable(x, y) {
    const tr = document.createElement('tr');
    const tdX = document.createElement('td');
    const tdY = document.createElement('td');

    tdX.innerHTML = x;
    tdY.innerHTML = y;

    tr.appendChild(tdX);
    tr.appendChild(tdY);

    tablePairs.querySelector('tbody').appendChild(tr);
  }
}

// ... rest of the code as it was
```

We get all of the elements we will use shortly and add an event on the "Add" button. That event will grab the current values and update our table visually.

We need to parse the amount since we get a string. It will be important for the next step when we have to apply the formula.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/image-13.png)
_When we press add we should see the pairs on the table_

### Make the calculations

All the math we were talking about earlier (getting the average of **X** and **Y**, calculating **b**, and calculating **a**) should now be turned into code. We will also display the **a** and **b** values so we see them changing as we add values.

**public/least-squares.js**

```js
// ... rest of the code as it was

btnUpdateGraph.addEventListener('click', () => {
  const x = parseFloat(inputX.value);
  const y = parseFloat(inputY.value);

  updateTable(x, y);
  updateFormula(x, y);
});

function updateFormula(x, y) {
  currentData.pairs.push({ x, y });
  const pairsAmount = currentData.pairs.length;

  const sum = currentData.pairs.reduce((acc, pair) => ({
    x: acc.x + pair.x,
    y: acc.y + pair.y,
  }), { x: 0, y: 0 });

  const average = {
    x: sum.x / pairsAmount,
    y: sum.y / pairsAmount,
  };

  const slopeDividend = currentData.pairs
    .reduce((acc, pair) => parseFloat(acc + ((pair.x - average.x) * (pair.y - average.y))), 0);
  const slopeDivisor = currentData.pairs
    .reduce((acc, pair) => parseFloat(acc + (pair.x - average.x) ** 2), 0);

  const slope = slopeDivisor !== 0
    ? parseFloat((slopeDividend / slopeDivisor).toFixed(2))
    : 0;

  const coeficient = parseFloat(
    (-(slope * average.x) + average.y).toFixed(2),
  );

  currentData.line = currentData.pairs
    .map((pair) => ({
      x: pair.x,
      y: parseFloat((coeficient + (slope * pair.x)).toFixed(2)),
    }));

  spanFormula.innerHTML = `Formula: Y = ${coeficient} + ${slope} * X`;
}

// ... rest of the code as it was
```

There isn't much to be said about the code here since it's all the theory that we've been through earlier. We loop through the values to get sums, averages, and all the other values we need to obtain the coefficient (**a**) and the slope (**b**).

![Image](https://www.freecodecamp.org/news/content/images/2020/09/image-15.png)
_The span so we can display the formula and see it change as we add values_

We have the _pairs_ and _line_ in the _current_ variable so we use them in the next step to update our chart.

### Update the graph and clean inputs

**public/least-squares.js**

```js
// ... rest of the code as it was

btnUpdateGraph.addEventListener('click', () => {
  const x = parseFloat(inputX.value);
  const y = parseFloat(inputY.value);

  updateTable(x, y);
  updateFormula(x, y);
  
  updateChart();
  
  clearInputs();
});

function updateChart() {
  chart.data.datasets[0].data = currentData.pairs;
  chart.data.datasets[1].data = currentData.line;

  chart.update();
}
  
function clearInputs() {
  inputX.value = '';
  inputY.value = '';
}

// ... rest of the code as it was
```

Updating the chart and cleaning the inputs of **X** and **Y** is very straightforward. We have two datasets, the first one (position zero) is for our pairs, so we show the dot on the graph. The second one (position one) is for our regression line.

We have to grab our instance of the chart and call _update_ so we see the new values being taken into account.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/image-16.png)
_At least three values are needed so we can take any kind of information our of the graph_

## Adding some style

We can change our layout a bit so it's more manageable. Nothing major, it just serves as a reminder that we can update the UI at any point 

**public/style.css**

```css
.container {
  display: grid; 
}

.left-half {
  grid-column: 1;
}

.right-half {
  grid-column: 2;
}

.pairs-style input[type="number"],
.pairs-style button {
  margin: 5px 0px;
}

.table-pairs {
  border-collapse: collapse;
  width: 100%;
}

.table-pairs td {
  text-align: center;
}

.table-pairs,
.table-pairs th,
.table-pairs td {
  margin: 10px 0px;
  border: 1px solid black;
}
```

**public/index.html**

```html
<html>
  <head>
    <title>Least Squares Regression</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js@2.9.3/dist/Chart.min.js"></script>
    <link rel="stylesheet" href="style.css">
  </head>
  <body>
    <div class="container">
      <div class="left-half">
        <div class="pairs-style">
          <div>
            <input type="number" class="input-x" placeholder="X">
          </div>
          <div>
            <input type="number" class="input-y" placeholder="Y">
          </div>
          <button class="btn-update-graph">Add</button> 
        </div>
        <div>
          <span class="span-formula">Formula: Y = a + b * X</span>
        </div>
        <div>
          <table class="table-pairs">
            <thead>
              <th>
                X
              </th>
              <th>
                Y
              </th>
            </thead>
            <tbody></tbody>
          </table>
        </div>
      </div>
      <div class="right-half">
        <canvas id="myChart"></canvas>
      </div>
    </div>
    <script src="/js/least-squares.js"></script>
  </body>
</html>
```

![Image](https://www.freecodecamp.org/news/content/images/2020/09/image-17.png)
_Not a big change, but at least the elements are a bit better aligned_

## Proof of Concept

![Image](https://www.freecodecamp.org/news/content/images/2020/09/image-18.png)
_We add the same values as earlier in the theory and obtain the same graph and formula! :D_

## Final remarks

For brevity's sake, I cut out a lot that can be taken as an exercise to vastly improve the project. For example:

* Add checks for empty values and the like
* Make it so we can remove data that we wrongly inserted
* Add an input for X or Y and apply the current data formula to "predict the future", similar to the last example of the theory

Regardless, predicting the future is a fun concept even if, in reality, the most we can hope to predict is an approximation based on past data points. 

It's a powerful formula and if you build any project using it I would love to see it.

I hope this article was helpful to serve as an introduction to this concept. The code used in the article can be found in my GitHub **[here](https://github.com/daspinola/least-squares-regression)**_._

See you in the next one, in the meantime, go code something!

