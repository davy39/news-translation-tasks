---
title: The best data visualization and web reporting tools for your BI solution
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-08T20:59:04.000Z'
originalURL: https://freecodecamp.org/news/4-data-visualization-and-web-reporting-tools-for-your-bi-solution-35503cc8b7e3
coverImage: https://cdn-media-1.freecodecamp.org/images/1*VcPbsz04dol7sFWB77rOKg.jpeg
tags:
- name: Apps
  slug: apps-tag
- name: 'BUSINESS INTELLIGENCE '
  slug: business-intelligence
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Veronika Rovnik

  Making the complex simple with smart data analysis

  It is hard to overestimate the value of insightful analytics nowadays. All business
  processes have become data-driven: marketing, accounting, human resources, customer
  service, fin...'
---

By Veronika Rovnik

### **Making the complex simple with smart data analysis**

It is hard to overestimate the value of insightful analytics nowadays. All business processes have become data-driven: marketing, accounting, human resources, customer service, finance.

And to convince the decision makers, you need to properly convey the meaning of the data. One possible technique is composing an analytical web report. Another essential part of it is high-powered data visualization which helps you understand the business trends of your company.

I’ve done some research, and I’ll now give you a comprehensive overview of **four popular tools for web reporting and data analysis.** The first two of them are free, the following two are more advanced. These tools will be useful for both the **developers** and **data analysts**.

### **Free tools**

The following options provide opportunities for basic web reporting.

#### **PivotTable.js**

![Image](https://cdn-media-1.freecodecamp.org/images/d7yt-vm9gz47Z7ROTSUyrmlhTYAxG70ZpUZs)

[PivotTable.js](https://pivottable.js.org/?r=m4) is an open-source JavaScript Pivot Table. It aims to provide the functionality for data analysis, and requires a good knowledge of JavaScript to reach its full potential.

1. Built-in web reporting features:

* Support of **.csv** and **JSON** data sources
* **Aggregation**, **filtering**, **sorting**, and **grouping** are available. There are **22 functions** which include functions for statistical research.
* You can move the fields from columns to rows, and vice versa, with the help of **drag & drop** functionality.
* Custom **cell formatting**
* **TSV renderer** for exporting to TSV format
* Ability to define **multiple aggregators**
* A **heat map** rendering option

2. View customization features:

* Mobile-enabled renderers for touch devices are available.
* Cells of the grid can be **colored.**
* There is an Excel-like layout available: each hierarchy is displayed in a separate column or row.
* [Custom formatting](https://pivottable.js.org/examples/montreal_2014.html) is possible as well as making a custom heat map color-scale.
* **Language localization**: the pivot table is available in **English** and **French**, and it’s possible to write your own “language pack” in JavaScript.

3. Integration and compatibility:

* There is a [React version](https://react-pivottable.js.org/) with integrated Plotly charts.
* It is compatible with Python/Jupyter and R/RStudio.

4. Limits:

* Handles up to 100K rows
* Unfortunately, subtotals can be rendered only via an additional plugin.
* Built-in renderers for export to CSV and Excel are not available.
* To save the configuration of the report, you need to implement this functionality yourself. **PivotTable.js** provides a freedom in customization, though.

5. Creating charts:

You can use the renderers for integration with **C3 Charts**, **D3.js**, **Plotly**, and **Google Charts**. It is possible to use **Highcharts** along with the pivot table with the help of a third-party plugin.

**Learn more:**

* [Download from GitHub](https://github.com/nicolaskruchten/pivottable)

**Demos on JSFiddle:**

* [Main demo](https://jsfiddle.net/nicolaskruchten/kn381h7s/)
* [Analysis of R datasets](https://pivottable.js.org/examples/rcsvs.html)

#### WebDataRocks

![Image](https://cdn-media-1.freecodecamp.org/images/OlytnwmNiaw1j3dFI3FPZID2H2CMSgJRyQ5b)

[**WebDataRocks**](https://www.webdatarocks.com/?r=m4) is an embeddable **web pivot table** written in JavaScript. It is a lightweight component. You can use it in a web application and build an interactive report based on your data. It can be viewed on mobile devices and desktop clients. It is suitable for less technical end-users, but offers advanced customization options for developers.

1. Built-in web reporting features:

* Support of **local and remote** **JSON** and **.csv** data sources
* The main functionality is accessible via the special extra-part of the pivot table — the **Toolbar.**
* **Aggregation, multiple filtering, sorting**, and **grouping** are easy with the UI. There are 13 aggregation functions and the ability to create a custom calculated value.
* Configuring fields via the **Field List** and moving them from columns to rows and vice versa with the help of **drag and drop** functionality
* Creation of **multi-level hierarchies**
* Each cell of the grid can be drilled through.
* Sharing your results with colleagues: you can save the report and export it to **PDF, Excel,** and **HTML** formats, or **print** it.

2. View customization features:

* The look and feel of the reporting tool can be changed. There are [four predefined themes](https://www.webdatarocks.com/doc/changing-report-themes/?r=m4) that may be to your taste, and the possibility to **create your own theme.**
* You can use a **conditional formatting** feature to **highlight** the most important cells of the pivot table based on particular values.
* Number formatting
* If you need to **change the layout**, you can choose a classic, compact, or flat form of the pivot table. For me, the compact form has the most laconic and neat style.
* **Language localization** — you can choose among available languages, or translate your pivot table into the needed language using a simple template JSON file.

3. Integration and compatibility:

* WebDataRocks can be embedded into AngularJS, Angular and React applications.

4. Limits:

* Maximum data size is 1Mb.

5. Creating charts:

It is easy to integrate WebDataRocks with Google Charts, Highcharts or any other charting library. There are tutorials available in the documentation.

**Learn more:**

* [Quick start](https://www.webdatarocks.com/doc/how-to-start-online-reporting/?r=m4)
* [3 installation options](https://www.webdatarocks.com/doc/download/?r=m4)

**CodePen demos:**

* [Multi-level hierarchy with types](https://codepen.io/webdatarocks/pen/jvJKoY)
* [A dashboard with HighCharts](https://codepen.io/webdatarocks/pen/dqdvmg)

### **Advanced solutions**

Let’s move on to tools that are more high-powered **embedded BI tools** and provide a more advanced web reporting experience.

A free 30-day trial is available for testing both tools.

#### **Flexmonster**

![Image](https://cdn-media-1.freecodecamp.org/images/uOEIpPBuDbg92agHsO9iG9xSTc9AXTnZuYLz)

[**Flexmonster Pivot Table & Charts**](https://www.flexmonster.com/?r=m4) is a JavaScript pivot table component. It is well-suited for deep analysis of tabular and multidimensional data, and building visual reports based on these. The main differences from the free options are OLAP cube support and more integration options.

1. Built-in web reporting features:

* Supported data formats are **CSV, JSON**, data from **SQL** and **NoSQL** databases, and **OLAP cubes** — such as Microsoft Analysis Services and Pentaho Mondrian cubes).
* You can use **multiple aggregations** to summarize numerical data. There are **16 aggregation functions** available and the ability to create a calculated value.
* **Sorting** and **grouping** of the data
* **Filtering** can be performed **by values** — to display Top/Bottom N records — **member names** and/or applied to the whole **report.**
* You can add interactivity to your pivot table by using **event handlers.**
* The final report can be saved in a **JSON file** with all the configurations and formatting applied. You can load it later for further work.
* Export the report **to HMTL, Image, CSV, Excel** or **PDF** formats without the need to connect any third-party plugins.

2. View customization features

* It is possible to choose one of the **five** **theme styles** or create a custom one.
* [Grid customization](https://www.flexmonster.com/blog/grid-customization-and-styling-beyond-css/?r=m4) functionality allows the creation of **heat map** visualizations.
* **Conditional formatting** of cells
* **Number formatting**
* **Date** values can be displayed in user-defined formatting.
* Component **localization** includes seven languages. You can translate the pivot table by yourself with the help of a template JSON file.
* A mobile-friendly design

3. Integration and compatibility

* Flexmonster can be included in the simple web page or integrated into **AngularJS, Angular,** or **React** applications. There are also tutorials on the official website on integrating with **jQuery** and **Webpack.**
* **MongoDB data analysis** is of special interest for those who have huge amounts of data stored in documents. Connection to MongoDB is supported via Node.js.

4. Limits:

Handles up to 1 million rows so there is no problem with big datasets.

5. Creating charts:

**Flexmonster** has [**pivot charts**](https://www.flexmonster.com/demos/pivot-charts/?r=m4) as a part of the component. To get access to other charts, you can use guides on integration with Google Charts, Highcharts, FusionCharts, or any other third party charting libraries. All these approaches help to create interactive dashboards.

**Learn more:**

* [Quick start](https://www.flexmonster.com/doc/how-to-create-js-pivottable/?r=m4)
* [Download options](https://www.flexmonster.com/download-page/?r=m4)

**Demos:**

* [Main demo](https://www.flexmonster.com/demos/pivot-table-js/?r=m4)
* [Heat Map](https://www.flexmonster.com/demos/heatmap/?r=m4)

#### **DhtmlxPivot**

![Image](https://cdn-media-1.freecodecamp.org/images/90yYMjiNRq3m6VUj5AkAB0Ri4wX3VjkUEO7J)

[**DhtmlxPivot**](https://dhtmlx.com/docs/products/dhtmlxPivot/) is a JavaScript Pivot Grid for analytical reports creation. It is a part of the dhtmlxSuite, but can be purchased separately from the bundle. It offers a modern UI and integration with different server-side technologies.

1. Built-in web reporting features:

* Supports connection to **JSON**, **.csv**, and **XML** data sources. Data can be loaded from JavaScript array and HTML table.
* There are only four inbuilt aggregation functions — max, min, sum and count. Custom ones can be created.
* **Grouping**, **searching**, and **sorting** of the data
* **Filtering** using UI or pre-defined string, number, and dates filters. Also, you can define global filters and set the number of rows to display per page on the grid.
* **Drag and drop** functionality
* Cells can be edited and filled with the custom content
* Built-in module for exporting the report to an Excel file with all the configurations saved

2. View customization features:

* The layout can be adjusted. For example, you can change the width of columns, left margin, turn on a “read-only” mode for the pivot table.
* **Conditional formatting** and **custom CSS** of the cells
* Mobile-friendly design as well
* Localization of the interface is possible via the special method.

3. Integration and compatibility:

* Supports integration with multiple technologies, such as PHP, Java, .NET, Node.js, Ruby on Rails, ASP.NET, ColdFusion, and Typescript and other technologies.

4. Limits:

There is no information about a data size on the official website. Testing showed that the pivot table renders up to 10K rows.

5. Creating charts:

To use charts in your web reports, the best option is to use dhtmlxChart. If you purchased the **dhtmlxSuite**, they are already included in the bundle. However, you can purchase it separately.

**Learn more:**

* [Samples](https://docs.dhtmlx.com/pivot/samples/)
* [Download packages](https://dhtmlx.com/docs/download.shtml)

### **Summary**

To my mind, a perfect tool contains a bundle of built-in features such as:

* Loading of CSV, JSON and multidimensional data
* Support of aggregation pipeline via UI
* The ability to display the data in charts and integrate with any server-side and front-end technology
* Exporting should be easy as well, without the need to include any third party modules.

Furthermore, the tools should always evolve to meet the new demands of end-users. It is up to you which one to choose for your project, and I hope it will help improve the way you work with the data.

