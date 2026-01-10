---
title: These are the best JavaScript chart libraries for 2019
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-05-15T21:37:15.000Z'
originalURL: https://freecodecamp.org/news/these-are-the-best-javascript-chart-libraries-for-2019-29782f5e1dc2
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Aom0Yz2zVQZdBiiByborCA.png
tags:
- name: Data Science
  slug: data-science
- name: data visualization
  slug: data-visualization
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Arthur Puszynski

  First, a brief history:

  With data collection and use continuing to increase exponentially, the need to visualize
  this data is becoming more important. Developers seek to consolidate millions of
  database records into beautiful char...'
---

By Arthur Puszynski

First, a brief history:

With data collection and use continuing to increase exponentially, the need to visualize this data is becoming more important. Developers seek to consolidate millions of database records into beautiful charts and dashboards that humans can quickly and intuitively interpret.

Data visualization technology has continued to improve over the past decade and many advanced chart libraries are now available to consumers. In the early 2000s, chart generation was dominated by server side image bitmap charts. Plugins such as Flash and Silverlight offered a more interactive charting experience but with a heavy toll on download speed, battery life and system resources.

With the explosion of mobile and tablet usage, plugins were no longer supported on major platforms and developers had to shift to open client side technologies that could run everywhere. At the same time, the advent of very high resolution screens and more common zooming through touch gestures brought resolution independent vector charts to the forefront.

Enter the current era of data visualization dominated by JavaScript and SVG (Scalable Vector Graphics). Charts now run on all browsers, without special plugins, support interactivity and animations and look sharp even on the highest resolution devices. Reviewing over 50 visualization libraries, these 9 products stood out:

#### [**D3.js**](https://d3js.org/)

![Image](https://cdn-media-1.freecodecamp.org/images/S6EaFX5GX8yUIDvllrXDeYc2fONsQL-8jMUL)

D3.js is a very extensive and powerful graphics JavaScript library. It allows you to bind arbitrary data to a Document Object Model (DOM), and then apply data-driven transformations to the document.

D3 goes well beyond typical charting libraries, including many other smaller technical modules such as axes, colors, hierarchies, contours, easing, polygons, and more. All this makes for a steep learning curve.

Trying to create a simple chart can be complicated. All elements including the axes, and other chart items need to be defined explicitly. Many samples show how CSS can be used to style chart elements. No charting-based features apply automatically. If you want to get into the weeds and use creativity to fully control every element, it is the best choice. Working against the clock to meet data visualization project requirements it may not be the best choice starting from scratch.

D3.js can be a building block for a charting library. Developers have used D3 to make it easier to use chart solutions that consume it, such as NVD3.

D3.js is open source and free to use.

#### [**JSCharting**](https://jscharting.com/)

![Image](https://cdn-media-1.freecodecamp.org/images/hTX6DIAPWYObB4LCQ--zfJIRrW1q85peGy3A)

JSCharting chart library supports a large number of chart types including maps, gantt, stock and others that often require separate libraries to use. It includes built-in maps of all world countries, and a library of SVG icons. A suite of standalone micro charts can render in any chart labels or in any div element on a page. UI controls (UiItems) are also included allowing for richer interactive charts. To control data or visualization variables in real-time is easy and charts can be exported to SVG, PNG, PDF, and JPG formats.

The gallery is divided into chart type and feature samples. The chart styling is polished and yields some clean looking charts. The overall visuals provide a clean and professional charting experience.

Included samples use a configuration object to customize charts. The settings to create and control chart types are very simple to use. Few property settings are needed to specify more complex chart types and JSCharting has strong and dynamic defaults meaning it attempts to choose the best settings for the scenarios automatically.

The documentation includes many tutorials and thorough API property descriptions. Many properties include example usage and sample links.

JSCharting is free for non commercial and personal use and also offers commercial license options that includes all chart types and products for a single fee.

#### [**Highcharts**](https://www.highcharts.com/)

![Image](https://cdn-media-1.freecodecamp.org/images/2syqkeQ3kQi2mhDSFfsqV57jiG810QWR7b7G)

Highcharts is a popular JavaScript charting library used by many of the world’s largest companies. Charts are generated using SVG and fallback to VML for backward compatibility all the way to IE6/IE8. The demo charts demonstrate a fairly rich feature set but don’t wow visually. General documentation includes tutorials for many relevant topics and the API documentation is thorough.

The chart uses configuration options to create charts and the API is easy to use.

Highcharts is free for non-commercial and personal use. Commercial licensing is required for other usage and stock, map and gantt charts are licensed separately.

#### [**amCharts**](https://www.amcharts.com/)

![Image](https://cdn-media-1.freecodecamp.org/images/g5AOK1ltx8xdH2JFXp3iw7fcZAYJ5pthfFdG)

amCharts has recently released their version 4 which adds a strong SVG animation engine that allows creating movie-like scenes.

The demo charts look very nice. Most demos offer a number of palettes and a slider UI to adjust chart variables in real-time. Documentation includes many tutorials and full API property descriptions.

Creating a chart feels slightly different from the configuration-based approach, and instead uses a more declarative API. It requires slightly more code to configure charts but gives a better code completion experience.

amCharts offers a free license with branded charts and paid licenses for other usage.

#### [**Google Charts**](https://developers.google.com/chart/)

![Image](https://cdn-media-1.freecodecamp.org/images/fPisdLR3HjGBrfbCAzc75uXc5IO9wsf2wj-f)

Google charts are powerful and easy to use.

The sample charts look clean and are easy on the eyes. The gallery and extended gallery shows many chart types, but pressing the hamburger menu reveals more types (like calendar) that are not shown in these gallery lists.

Each chart type has a dedicated tutorial with live examples. The tutorials include code for the related features and API listings. This is a pleasant experience getting started with a new chart library.

Charts are customized using the configuration options object. Data sets are populated using a DataTable class which can be consumed by all charts. Each chart type has unique options listed in the type specific tutorials. Property naming is standardized and many options work across all types.

Google charts is free, but there is a caveat. It is a web service and cannot be hosted locally. In the past Google has retired API’s so if your usage is mission critical you may want to pick another option.

#### [**ZingChart**](https://www.zingchart.com/)

![Image](https://cdn-media-1.freecodecamp.org/images/7UxG9uthgcsC-fYPf0GEXgJY6A3X6C187ggy)

ZingChart offers many chart types and integrates with angular, react, and other frameworks. It has a strong feature set with many customization options.

The demo charts show a range of styling themes, some of which look better than others, but the options to style them as needed are there. Demos don’t demonstrate all the available chart types.

Documentation includes tutorials for all the available types, a good number of features, and full API listing.

ZingChart uses configuration options to customize charts. Samples include many property settings such as font styling. These can get in the way of understanding what settings are required for a given chart.

ZingChart can be used for free with branding. Paid licensing is available for non-branded usage.

#### [**FusionCharts**](https://www.fusioncharts.com/)

![Image](https://cdn-media-1.freecodecamp.org/images/b7k3uk0H59ImJz2wBVa6zBRCx8J6euicz1ZW)

FusionCharts has been around for many years starting as a Flash-based chart plugin. It is a robust chart visualization library. It supports many data formats including XML, JSON, and JavaScript, works in modern browsers and is backwards compatible back to IE6. Many JavaScript frameworks and server-side programming languages are also supported.

The chart gallery includes a large number of examples and they have a clean visual appearance.

Documentation includes good API descriptions, and examples of each chart type. The configuration properties are grouped by tasks and chart features.

Charts are created using configuration based options and is relatively easy to use. The list of properties can be lengthy when digging deeper into the API. All configuration properties are shallow such as {chartLeftMargin, showAlternateHGridColor }. It seems like an attempt to improve code completion.

FusionCharts is free for personal use with chart branding. Paid licensing is available for unbranded and commercial use.

#### [**KOOLCHART**](https://www.koolchart.com/)

![Image](https://cdn-media-1.freecodecamp.org/images/3iWJw51bCnMDw4QKpjP-0k-lZsoX0DUNnzL5)

KoolChart is an HTML 5 canvas-based JavaScript charting library. A mapping and grid product is also available.

Their new v5 release includes a more interactive feature set and updated styling. The visuals are clean and modern. The use of canvas offers better performance at the expense of being raster based.

The samples use a string based XML to apply chart options which seems less practical than other approaches. These options look like HTML5 but are set through a JavaScript string.

The API is well documented with example charts for each property. A 173 page PDF manual is also available.

A two month trial period is available for evaluation. Licensing is required after the trial period expires.

#### [**Chart.js**](https://www.chartjs.org/)

![Image](https://cdn-media-1.freecodecamp.org/images/ewHuQvOha7Jgzn2rLM8jzoz5caFNhU7IuQCw)

Chart.js is an open source JavaScript library supporting 8 chart types. It is a small js library at just 60kb. Types include line charts, bar charts, area charts, radar, pie charts, bubble, scatter plots, and mixed. A time series is also supported. It uses canvas element for rendering and is responsive on window resize to maintain scale granularity. It is backwards compatible to IE9. Polyfills are available to work with IE7 as well.

The sample visuals are fairly modern looking and include initial animations when drawing for the first time. It animates smoothly when adding series or data points in real-time. Chart options can be modified after and calling an update() function redraws the chart.

Sample source code is not shown the website gallery but is available in the GitHub repo. Configuration options are used to create and modify charts. The options API is clean and intuitive.

The documentation is thorough and includes tutorials with property API and code snippets.

Chart.js is an open source library and free to use for personal and commercial use which is a plus. The limited number of types can be an issue for more advanced dashboard requirements.

#### **Conclusion**

The ecosystem of JavaScript charting libraries has evolved considerably over the last decade. Today, there are a large number of charting products that meet very diverse requirements, serving a wide range of projects though hundreds of chart types. Most libraries provide a free trial or branded version enabling you to evaluate the chart effectiveness with your own data, loading and project complexity.

It is easy for most chart libraries to deal with simple curated data sets and static visualizations. However, charts may not always handle things smoothly when real-world, dynamic data is visualized. More work may be required to adjust and arrange elements so that charts appear correct and this manual tweaking can break as new dynamic data is visualized.

To select the best JS chart solution for your unique needs, I recommend testing your own data against a couple of the libraries listed above to ensure an ideal fit for your current and future projects.

