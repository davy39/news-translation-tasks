---
title: How to create a Countdown component using React & MomentJS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-05-16T16:41:47.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-countdown-component-using-react-momentjs-4717edc4ac3
coverImage: https://cdn-media-1.freecodecamp.org/images/0*uxd3eEv1EyIUdvNi.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Florin Pop

  Recently I had to create a Countdown for one of my other projects, and I thought
  that it could also make a good tutorial. So in this post we’re going to create this
  component using React and a little bit of SVG. ?

  You can find the final...'
---

By Florin Pop

Recently I had to create a Countdown for one of my other projects, and I thought that it could also make a good tutorial. So in this post we’re going to create this component using React and a little bit of `SVG`. ?

You can find the final result in this [Codepen example](https://codepen.io/FlorinPop17/pen/YbpwyG):

%[https://codepen.io/FlorinPop17/pen/YbpwyG]

First we will create the countdown functionality and then we will look into how to create the animated arc using `SVG` with some fancy functions. ?

### Creating the Countdown functionality

For this we’re going to use [MomentJS](https://momentjs.com/) library which will help us _parse, validate, manipulate,_ and _display_ dates and times.

Basically what we’re going to need is to have 2 dates:

* the current date or `now`
* the final date or `then`

When we have these 2 dates, we can subtract `now` from `then` using `moment` and we'll get the remaining time (or the `countdown` value).

For the `then` date, we'll need to pass 2 strings:

* one, the `timeTillDate` string containing the final date until which we want to count (e.g: **05 26 2019, 6:00 am**)
* two, the `timeFormat` string that is used by `moment` in order to validate the time format (in our example would be: **MM DD YYYY, h:mm a**)

You can find out more about parsing strings and formatting them in the [documentation](https://momentjs.com/docs/#/parsing/string/).

Let’s see how this looks in code:

```javascript
import moment from 'moment';

const then = moment(timeTillDate, timeFormat);
const now = moment();
const countdown = moment(then - now);
```

**Note**: the `timeTillDate`, `timeFormat` values will be provided inside the React component. For now we're using them as examples.

From the `countdown` object we can get all the values that we want to display in our component - `days`, `hours`, `minutes` and `seconds` left until we reach the `then` time.

```javascript
import moment from 'moment';

const then = moment(timeTillDate, timeFormat);
const now = moment();
const countdown = moment(then - now);
const days = countdown.format('D');
const hours = countdown.format('HH');
const minutes = countdown.format('mm');
const seconds = countdown.format('ss');
```

Later we’ll add this code in a JS `interval` that would be called every second, but before that let's set up the react component for it.

### The Countdown Component

For this we’re going to create a _class_ based component, as we need access to the `state` of the component because we'll save these 4 values (`days`, `hours`, `minutes`, `seconds`) in it. By default these values are `undefined`.

```javascript
import React from 'react';

class Countdown extends React.Component {
    state = {
        days: undefined,
        hours: undefined,
        minutes: undefined,
        seconds: undefined
    };

    render() {
        const { days, hours, minutes, seconds } = this.state;
      
        return (
            <div>
                <h1>Countdown</h1>
                <div className="countdown-wrapper">
                    <div className="countdown-item">
                        {days}
                        <span>days</span>
                    </div>
                    <div className="countdown-item">
                        {hours}
                        <span>hours</span>
                    </div>
                    <div className="countdown-item">
                        {minutes}
                        <span>minutes</span>
                    </div>
                    <div className="countdown-item">
                        {seconds}
                        <span>seconds</span>
                    </div>
                </div>
            </div>
        );
    }
}
```

Next, let’s create the `interval` that runs every second and saves the values in the `state` of the component. We'll do this `interval` inside the `componentDidMount` lifecycle method. We are going to `clear` the interval in the `componentWillUnmount` lifecycle method, as we don't want to keep it running after the component is removed from the DOM.

```javascript
import React from 'react';
import moment from 'moment';

class Countdown extends React.Component {
    state = {
        days: undefined,
        hours: undefined,
        minutes: undefined,
        seconds: undefined
    };

    componentDidMount() {
        this.interval = setInterval(() => {
            const { timeTillDate, timeFormat } = this.props;
            const then = moment(timeTillDate, timeFormat);
            const now = moment();
            const countdown = moment(then - now);
            const days = countdown.format('D');
            const hours = countdown.format('HH');
            const minutes = countdown.format('mm');
            const seconds = countdown.format('ss');
            this.setState({ days, hours, minutes, seconds });
        }, 1000);
    }

    componentWillUnmount() {
        if (this.interval) {
            clearInterval(this.interval);
        }
    }

    render() {
        const { days, hours, minutes, seconds } = this.state;
      
        return (
            <div>
                <h1>Countdown</h1>
                <div className="countdown-wrapper">
                    <div className="countdown-item">
                        {days}
                        <span>days</span>
                    </div>
                    <div className="countdown-item">
                        {hours}
                        <span>hours</span>
                    </div>
                    <div className="countdown-item">
                        {minutes}
                        <span>minutes</span>
                    </div>
                    <div className="countdown-item">
                        {seconds}
                        <span>seconds</span>
                    </div>
                </div>
            </div>
        );
    }
}
```

### The CSS

We have the countdown functionality all up and running now, so let’s style it a little bit:

```javascript
@import url('https://fonts.googleapis.com/css?family=Lato');

* {
    box-sizing: border-box;
}

body {
    font-family: 'Lato', sans-serif;
}

h1 {
    letter-spacing: 2px;
    text-align: center;
    text-transform: uppercase;
}

.countdown-wrapper {
    display: flex;
    align-items: center;
    justify-content: center;
    flex-wrap: wrap;
}

.countdown-item {
    color: #111;
    font-size: 40px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    line-height: 30px;
    margin: 10px;
    padding-top: 10px;
    position: relative;
    width: 100px;
    height: 100px;
}

.countdown-item span {
    color: #333;
    font-size: 12px;
    font-weight: 600;
    text-transform: uppercase;
}
```

Nothing fancy in the CSS; we’re using `flexbox` to position the items within the wrapper.

Lastly, let’s create the `SVG` arc that will be surrounding each item in our countdown.

### The SVGCircle Component

Before we do that, there are a couple of functions that we need in order to create the customizable `SVG` arc. I found these on [StackOverflow](https://stackoverflow.com/questions/5736398/how-to-calculate-the-svg-path-for-an-arc-of-a-circle). For more information you should go there and read the detailed explanation of the functions.

```javascript
function polarToCartesian(centerX, centerY, radius, angleInDegrees) {
    var angleInRadians = ((angleInDegrees - 90) * Math.PI) / 180.0;
  
    return {
        x: centerX + radius * Math.cos(angleInRadians),
        y: centerY + radius * Math.sin(angleInRadians)
    };
}

function describeArc(x, y, radius, startAngle, endAngle) {
    var start = polarToCartesian(x, y, radius, endAngle);
    var end = polarToCartesian(x, y, radius, startAngle);
    var largeArcFlag = endAngle - startAngle <= 180 ? '0' : '1';
    var d = [
        'M',
        start.x,
        start.y,
        'A',
        radius,
        radius,
        0,
        largeArcFlag,
        0,
        end.x,
        end.y
    ].join(' ');
  
    return d;
}
```

Basically the above function calculates how the arc should be drawn by providing a set of values as: the start and ending points, the radius and the angles.

Back to our React Component: we’re going to create the `svg` and we'll have a `path` tag within it which will draw the arc (the `d` prop) by giving it a `radius` property. The other 4 values within the `describeArc` function are fixed, as we don't want to modify it and we are customizing it to look good for our example.

```javascript
const SVGCircle = ({ radius }) => (
    <svg className="countdown-svg">
        <path
            fill="none"
            stroke="#333"
            stroke-width="4"
            d={describeArc(50, 50, 48, 0, radius)}
        />
    </svg>
);
```

And we also need a little bit of CSS to position it inside the `.countdown-item` (See where this component goes in the final result section):

```css
.countdown-svg {
    position: absolute;
    top: 0;
    left: 0;
    width: 100px;
    height: 100px;
}
```

Before adding this component inside the `Countdown` component, we need to convert the values that we have (`days`, `hours`, `minutes` and `seconds`) to their corresponding radius values.

For this we’ll need another simple function that will map a number within a range (in our case the date values) to another range of numbers (in our case, the radius). This function is also from [StackOverflow](https://stackoverflow.com/questions/10756313/javascript-jquery-map-a-range-of-numbers-to-another-range-of-numbers):

```javascript
function mapNumber(number, in_min, in_max, out_min, out_max) {
    return (
        ((number - in_min) * (out_max - out_min)) / (in_max - in_min) + out_min
    );
}
```

### The final result

Finally, let’s add the new `SVGCircle` component inside each of the `.countdown-item`s and put everything together:

```js
import React from 'react';
import moment from 'moment';

class Countdown extends React.Component {
    state = {
        days: undefined,
        hours: undefined,
        minutes: undefined,
        seconds: undefined
    };
    
    componentDidMount() {
        this.interval = setInterval(() => {
            const { timeTillDate, timeFormat } = this.props;
            const then = moment(timeTillDate, timeFormat);
            const now = moment();
            const countdown = moment(then - now);
            const days = countdown.format('D');
            const hours = countdown.format('HH');
            const minutes = countdown.format('mm');
            const seconds = countdown.format('ss');
            this.setState({ days, hours, minutes, seconds });
        }, 1000);
    }
    
    componentWillUnmount() {
        if (this.interval) {
            clearInterval(this.interval);
        }
    }
    
    render() {
        const { days, hours, minutes, seconds } = this.state;
        
        // Mapping the date values to radius values
        const daysRadius = mapNumber(days, 30, 0, 0, 360);
        const hoursRadius = mapNumber(hours, 24, 0, 0, 360);
        const minutesRadius = mapNumber(minutes, 60, 0, 0, 360);
        const secondsRadius = mapNumber(seconds, 60, 0, 0, 360);
        
        if (!seconds) {
            return null;
        }
        
        return (
            <div>
                <h1>Countdown</h1>
                <div className="countdown-wrapper">
                    {days && (
                        <div className="countdown-item">
                            <SVGCircle radius={daysRadius} />
                            {days}
                            <span>days</span>
                        </div>
                    )}
                    {hours && (
                        <div className="countdown-item">
                            <SVGCircle radius={hoursRadius} />
                            {hours}
                            <span>hours</span>
                        </div>
                    )}
                    {minutes && (
                        <div className="countdown-item">
                            <SVGCircle radius={minutesRadius} />
                            {minutes}
                            <span>minutes</span>
                        </div>
                    )}
                    {seconds && (
                        <div className="countdown-item">
                            <SVGCircle radius={secondsRadius} />
                            {seconds}
                            <span>seconds</span>
                        </div>
                    )}
                </div>
            </div>
        );
    }
}

const SVGCircle = ({ radius }) => (
    <svg className="countdown-svg">
        <path
            fill="none"
            stroke="#333"
            stroke-width="4"
            d={describeArc(50, 50, 48, 0, radius)}
        />
    </svg>
);

// From StackOverflow: https://stackoverflow.com/questions/5736398/how-to-calculate-the-svg-path-for-an-arc-of-a-circle

function polarToCartesian(centerX, centerY, radius, angleInDegrees) {
    var angleInRadians = ((angleInDegrees - 90) * Math.PI) / 180.0;
    
    return {
        x: centerX + radius * Math.cos(angleInRadians),
        y: centerY + radius * Math.sin(angleInRadians)
    };
}

function describeArc(x, y, radius, startAngle, endAngle) {
    var start = polarToCartesian(x, y, radius, endAngle);
    var end = polarToCartesian(x, y, radius, startAngle);
    var largeArcFlag = endAngle - startAngle <= 180 ? '0' : '1';
    var d = [
        'M',
        start.x,
        start.y,
        'A',
        radius,
        radius,
        0,
        largeArcFlag,
        0,
        end.x,
        end.y
    ].join(' ');
    
    return d;
}

// From StackOverflow: https://stackoverflow.com/questions/10756313/javascript-jquery-map-a-range-of-numbers-to-another-range-of-numbers

function mapNumber(number, in_min, in_max, out_min, out_max) {
    return (
        ((number - in_min) * (out_max - out_min)) / (in_max - in_min) + out_min
    );
}
```

All you have to do now to use the `Countdown` component is to pass it the two props (`timeTillDate` and `timeFormat`) and you're golden ?:

```javascript
<Countdown 
    timeTillDate="05 26 2019, 6:00 am" 
    timeFormat="MM DD YYYY, h:mm a" 
/>
```

### Conclusion

It was a fun little project with React, wasn’t it? ?

When I built this I learned a little bit more about how to work with the `momentjs` library and also with `svg`s to draw an arc.

Let me know if you have any questions regarding this tutorial.

Happy Coding! ?

_Originally posted on [www.florin-pop.com](https://www.florin-pop.com/blog/2019/05/countdown-built-with-react/)_

