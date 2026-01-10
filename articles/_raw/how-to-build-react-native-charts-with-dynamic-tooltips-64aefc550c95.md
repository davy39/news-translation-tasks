---
title: How to build React Native charts with dynamic tooltips
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-22T19:00:51.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-react-native-charts-with-dynamic-tooltips-64aefc550c95
coverImage: https://cdn-media-1.freecodecamp.org/images/1*zjVWOfAZdFWrzyTHJsiobw.gif
tags:
- name: coding
  slug: coding
- name: Design
  slug: design
- name: General Programming
  slug: programming
- name: React Native
  slug: react-native
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Vikrant Negi

  Creating charts, be it on the web or on mobile apps, has always been an interesting
  and challenging task especially in React Native. It’s difficult to find a suitable
  library that can meet your functional and design needs at the same ...'
---

By Vikrant Negi

Creating charts, be it on the web or on mobile apps, has always been an interesting and challenging task especially in React Native. It’s difficult to find a suitable library that can meet your functional and design needs at the same time. You can try to make your own charts, but that often comes with the overhead of learning and implementing things from scratch.

If you are a beginner like I am, you probably want to use an existing charts library. And given how young the React Native community is, you have very few options available to you to implement and customize charts.

#### Problem Statement

Before starting our journey deep into the woods, I would like to introduce you to our problem statement.

In this tutorial, we are going to draw an area chart and add a circular marker at each of the data points which can further be tapped to show a tooltip containing x and y coordinate values.

To solve this problem, I did some research on some existing React Native libraries and narrowed it down two of them, [react-native-charts-wrapper](https://github.com/wuxudong/react-native-charts-wrapper), and [react-native-svg-charts](https://github.com/JesperLekland/react-native-svg-charts).

#### React Native Charts Wrapper

Our first contender, `[react-native-charts-wrapper](https://github.com/wuxudong/react-native-charts-wrapper)` is a React Native wrapper of popular Native charting library [MPAndroidChart](https://github.com/PhilJay/MPAndroidChart) and [Charts](https://github.com/danielgindi/Charts).

This library is highly configurable, and since it uses the native chart libraries it provides silky smooth transitions and touch support. It also has tons of examples of use cases on its Github repo.

In the beginning, it was my preferred choice given its performance and customization. It has a very long and specific [installation](https://github.com/wuxudong/react-native-charts-wrapper/blob/master/installation_guide/README.md) guide, following which I was able to install and run it on both iOS and Android devices.

Everything seems to be working smoothly on Android. However, when I tried to create an iOS build, it gave me an error. After countless hours of searching through GitHub issues and Google, I decided against it.

#### React Native SVG Charts

After giving up on `react-native-charts-wrapper` this was the next best solution available that I could find.

`[react-native-svg-charts](https://github.com/JesperLekland/react-native-svg-charts)` uses `[react-native-svg](https://github.com/react-native-community/react-native-svg)` under the hood to render charts. It also has tons of [examples](https://github.com/JesperLekland/react-native-svg-charts-examples) featuring many use cases.

Since it doesn’t use any native linking, installation and implementation was pretty simple and straightforward.

> If you just want to see the source code of the example project, find the project repo [here](https://github.com/vikrantnegi/react-native-tooltip-chart).

Now that’s done, let’s get this party rolling.

#### Getting Started

Create a React native project and install all the required dependencies.

```
~ react-native init ReactNativeTooltip
```

We’ll also need to install and link the `react-native-svg` library.

```
~ npm i react-native-svg
```

```
~ react-native link react-native-svg
```

If you face any problem linking the library automatically using the link command, follow the [manual](https://github.com/react-native-community/react-native-svg) steps mentioned in the official documentation.

Now, finally install the `react-native-svg-charts` .

```
~ npm install react-native-svg-charts
```

#### Getting the Dummy data

Before we dive any further we’ll need to have some data that we can use for rendering our `AreaChart`. We’ll be using a third-party service called [Mockaroo](https://www.mockaroo.com/) to generate some mock data for our area chart.

Ideally, we’ll be getting this data from an API that we’ll store it in the component state and then feed to our area component.

Here is how my dummy JSON data looks. See [here](https://github.com/vikrantnegi/react-native-tooltip-chart/blob/master/src/Data.js) for the full JSON data file.

```
export const DATA = [  {    id: 1,    date: ‘2019–01–26T22:37:01Z’,    score: 3,  },  {    id: 2,    date: ‘2019–01–06T06:03:09Z’,    score: 9,  },  {    id: 3,    date: ‘2019–01–28T14:10:00Z’,    score: 10,  },  {    id: 4,    date: ‘2019–01–03T02:07:38Z’,    score: 7,  },  ...]
```

#### Using React Native SVG charts

`react-native-svg-charts` has lots of components that we can use to create graphs. In this tutorial, we’ll use `AreaChart` component but you can use any one of the [available](https://github.com/JesperLekland/react-native-svg-charts#components) charts components. Here is how an `Areachart` chart component looks:

```
<AreaChart  style={{ height: '70%' }}  data={data}  yAccessor={({ item }) => item.score}  xAccessor={({ item }) => moment(item.date)}  contentInset={contentInset}  svg={{ fill: '#003F5A' }}  numberOfTicks={10}  yMin={0}  yMax={10}>
```

Let’s go through the important props that we are using in the `AreaChart`.

* `data` : This is a required field and must be an array.
* `yAccessor`: A function that takes each entry of `data` (named "item") as well as the index and returns the y-value of that entry.
* `xAccessor:` Same as `yAccessor` but returns the x-value of that entry.

You can read more about the other available props in the official [documentation](https://github.com/JesperLekland/react-native-svg-charts#common-props).

#### Adding Decorators

React native SVG charts was built to be as extensible as possible. All charts can be extended with “decorators”, a component that somehow styles or enhances your chart. Simply pass in a `react-native-svg` compliant component as a child to the graph and it will be called with all the necessary information to layout your decorator.

For this tutorial, we’ll need two decorators, one for the datapoint marker and another one for the tooltip.

> Make sure you place Decorators inside the `_AreaChart_` component. Otherwise they won’t render.

#### Adding Marker Data Points

Let’s create a decorator to be used as a marker at each data point in the chart.

```
const ChartPoints = ({ x, y, color }) =>  data.map((item, index) => (   <Circle     key={index}     cx={x(moment(item.date))}     cy={y(item.score)}     r={6}     stroke={color}     fill=”white”     onPress={() =>       this.setState({         tooltipX: moment(item.date),         tooltipY: item.score,         tooltipIndex: index,       })     }  />));
```

We need a circular marker for each item in the data array. And, for that, we are going to loop through each item in the data array and return `Circle` SVG component for each one of them.

Now, to position them on the chart, we’ll use the `cx` and `cy` props to position them horizontally and vertically, respectively. For `cx` we will use `date` key and for `cy` we will use the `score` key.

Apart from that, we’ll also pass `onPress` prop that will set three states, `tooltipX`, `tooltipY` and `tooltipIndex` when any of the data points are pressed. We’ll use then use these states to position the `Tooltip` decorator.

![Image](https://cdn-media-1.freecodecamp.org/images/7DDoNAP66bEyXcKvCeyxj8FbCaTMw4-nwtdq)
_Area charts with the markers_

#### Adding Tooltip

Now that we have necessary information like x-axis(tooltipX), the y-axis (tooltipY)and index(tooltipIndex) of the marker pressed, we can use them to place `Tooltip` on the `AreaChart`.

We’ll create a new [file](https://github.com/vikrantnegi/react-native-tooltip-chart/blob/master/src/Tooltip.js) for the `Tooltip` Decorator.

```
const Tooltip = ({ x, y, tooltipX, tooltipY, color, index, dataLength,}) => {
```

```
let xAxis = 4;  if (dataLength > 4) {    if (index < 2) {      xAxis = 35;    } else if (index > dataLength — 2) {      xAxis = -20;    } else {     xAxis = 4;    }  }
```

```
return (    <;G x={x(tooltipX) — 40} y={y(tooltipY)}>      <G y={tooltipY > 9 ? 20 : -29} x={xAxis}>        <Rect x={-2} y={0} height={22} width={70} stroke={color} fill=”white” ry={10} rx={10} />        <Rect x={-2} y={0} height={22} width={18} fill={color} ry={10} rx={10} />        <Rect x={10} y={0} height={22} width={tooltipY > 9 ? 12 : 10} fill={color} /&gt;        <Text x={6} y={14} stroke=”#fff”>          {tooltipY}        </Text>        <Text x={tooltipY > 9 ? 24 : 22} y={14}>          {moment(tooltipX).format(‘MMM DD’)}        </Text>      </G>    </G>  );};
```

Don’t get confused or intimidated by all the `React`, `G` and `Text` tags here, most of them are just for the styling of the tooltip.

Just focus on `tooltipX` and, `tooltipY` that we are using to position the `Tooltip` horizontally and vertically on the chart. These values are the same as `cx` and `cy` that we used for the marker, except that we are adding and subtracting some values to adjust them on the chart.

Apart from that, we are using `tooltipIndex` to offset the first and last Tooltip so that they don’t get cut off on the sides.

> [Here](https://github.com/vikrantnegi/react-native-tooltip-chart) is the full source code of a working example.

![Image](https://cdn-media-1.freecodecamp.org/images/Dfhg49lhgH6Q6oFeHteuXmc9jkRlMJaHioLo)
_Area chart with tappable tooltips_

#### Final Thoughts

That is all we need to do to create charts, markers, and tooltips. This is just a basic implementation of what can be achieved using the `react-native-svg-charts` library.

If you want to explore more, do check out their [examples](https://github.com/JesperLekland/react-native-svg-charts-examples) repo where they showcase tons of other use cases.

> For the sake of brevity I’ve skipped some boilerplate code which you can find on the Github repo.

Let me know if you find anything confusing. If you have worked on react native charts, do share what libraries and use cases you came across.

