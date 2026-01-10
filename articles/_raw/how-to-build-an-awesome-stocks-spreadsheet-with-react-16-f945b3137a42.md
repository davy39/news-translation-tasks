---
title: How to build an awesome stocks spreadsheet with React 16
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-11-14T19:47:07.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-an-awesome-stocks-spreadsheet-with-react-16-f945b3137a42
coverImage: https://cdn-media-1.freecodecamp.org/images/1*AK6DfcdIDmYnEyEAZ9-Ijg.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Sandeep Adwankar

  React 16 is the first version of React built on top of React’s new core architecture,
  codenamed “Fiber”. React 16 is designed from the ground up to support asynchronous
  rendering. This allows processing large component trees witho...'
---

By Sandeep Adwankar

React 16 is the first version of React built on top of React’s new core architecture, codenamed “Fiber”. React 16 is designed from the ground up to support asynchronous rendering. This allows processing large component trees without blocking the main execution thread.

React 16 is popular because it supports a number of key features, such as catching exceptions using error boundaries, returning multiple components from render, reduced file size, and its support for MIT license.

For building a data-driven web application like a Stocks spreadsheet, you’ll need a spreadsheet-like interface to display data for your users.

![Image](https://cdn-media-1.freecodecamp.org/images/sOsMwULzRp-OYDAE4tMHSEbF9Dg8xKpKcBeO)
_Stocks Spreadsheet_

Your users will expect the spreadsheet in your application to be capable of:

* Scrolling with a fixed header
* Sorting by clicking on a column header
* Showing and hiding specific columns
* Paging, grouping, and summarization
* Editing data in cells
* Exporting to Excel
* Drilling down/row expansion

A spreadsheet or grid, however, can be one of the trickiest and most complex UI components to build in React. This is because many of the necessary features require both significant React expertise, as well as the willingness and ability to dig down into the DOM.

If you want to code a grid using an HTML table or another third-party component, you will have to implement several common features. These features include clicking on a grid column header to sort or clicking on a divider between a column header to resize, or sliding a pager and doing a fetch for the next page of data.

For quickly building this app, we will use Sencha’s ExtReact components. Sencha’s ExtReact is a component set of 115+ pre-built UI components that you can easily integrate with React 16 apps. One of the key components in ExtReact is Grid. It provides spreadsheet like functionality required to build a stocks spreadsheet app quickly. We will make use of ExtReact Grid to show information about Stocks and equities companies.

Let’s get started with building a stocks application using Sencha’s ExtReact Grid.

### Scaffolding Stocks Spreadsheet App

For creating application scaffolding, please follow the steps below:

* **Make sure you have a Node environment set up**

First, make sure you have Node 8.11+ and NPM 6+ set up on your system. You can download the latest Node version from the [Node web site](https://nodejs.org/en/download/). If you’ve already installed Node, you can easily check the Node and npm versions by using these commands: _node -v_ and _npm -v_

* **Get your login credentials for the ExtReact NPM repo**

ExtReact NPM packages are hosted on Sencha’s private NPM repo. You log in to that repo once to get access to all ExtReact packages. To get login credentials, go to the [ExtReact 30-Day Free Trial](https://www.sencha.com/products/extreact/evaluate/?utm_source=freecodecamp&utm_medium=advertising&utm_campaign=sncextreact&utm_content=180914-ft-sncextreact) page and fill out the form. We’ll send you an email with login details as well as some links to resources such as the docs and sample projects.

* **Login to ExtReact NPM repo and get App generator**

The next step is to log in to Sencha’s private npm repo, which hosts the ExtReact packages. Use your npm login (provided in the ExtReact trial email) to associate the npm repo with the @sencha scope, and enter the credentials when prompted:

```
npm login — registry=http://npm.sencha.com — scope=@sencha
```

The next step is to install ExtReact generator package.

```
npm install -g @sencha/ext-react-gen
```

* **Create your first React App**

Run the ExtReact app generator to create your first ExtReact app:

```
ext-react-gen app your-app-name-here -i
```

The app generator will ask you a few questions — such as the name for your app. By default the app uses Material theme (based on [Google’s Material design guidelines](https://material.io/guidelines/)) and is a good choice as a starting theme.

Select “Generate an Empty App” in one of the prompts. The generator will also prompt you to create a new directory for your project. The generator will then download and create your sample application, including relevant dependencies.

* **Run your React App**

In the generator output, you will find steps to run your application. Change to your new application directory and run the application using:

```
npm start
```

This will fire up the app, and your empty React app will just show up with the title of the app. The main component (e.g. StocksGrid) in the application has one container at the root. This is marked as full screen, layout is set to fit, which means it will stretch its child to fill it.

[See the code up to this step](https://github.com/adwankar/react16-stocks-grid/tree/empty-extreact-app) on GitHub.

### Adding Stocks Grid to the application

#### **Add Stocks Data**

We’ll be adding an example data set of 10,000 rows, called stocks.json to the application. Each data row contains the name of the company, ticker symbol, sector, and industries they are in. The row also contains an array of _ticks_ which are the last 5 sales of that stock.

This is the data we’re going to display in our grid. In this tutorial, we’re going to load data statically from stocks.json, but you can also build a back-end rest API to get the same data.

#### **Creating a Basic Grid**

In the StockGrid React component, in the render method we’re going to return a grid with columns.

To add columns in our grid, we use a Column component. The Column component takes a data index that is the same as the name field of the stocks data. The Column takes a text prop that is the column header text. We can also give the Column a width, like a fixed width or a flex or a combination of flex and minimum or maximum as well. We’ll add column components for the company name, symbol, ticks, sector, and industry. This will create a new StocksGrid class with Grid as shown below

```
<Grid >       <Column dataIndex="name" text="Name" width={300} />       <Column dataIndex="symbol" text="Symbol" />       <Column dataIndex="ticks" text="Trend" />       <Column dataIndex="sector" text="Sector" width={200} />       <Column dataIndex="industry" text="Industry" width={350} /></Grid>
```

Your app will return StockGrid as part of render as below:

```
export default class App extends Component {
```

```
   render() {        return (            <ExtReact>                <StocksGrid />            </ExtReact>            )    }}
```

[See the code up to this step](https://github.com/adwankar/react16-stocks-grid/tree/adding-stocks-grid-component-6.6) on GitHub.

On running, you will be able to see web application with empty Grid on _npm start_

### Binding Stock Data with Grid

An ExtReact grid is a spreadsheet-like table that pulls in and renders data from a data store. In ExtReact, Store is a data structure that allows you to sort and filter data in a grid.

We can now start by loading the stocks data and creating a store. Grids will grab their data from the Store. Interactions with the Grid will trigger events on the Store, like reloading or sorting or paging.

The concept of ExtReact data Store is a bit different from the Flux Store. What makes the Grid and the Store a little different from the standard React approach is that the two are tightly integrated. Typically, you can pass data directly to a Store, or a Store can pull data on its own from a back-end using a Proxy. The ExtReact Grid provides interactive functionality like filtering, sorting, paging, grouping, and summarization without any additional code.

For this example, we’re passing the data directly to the store from the Stocks data file. Alternatively, you can create a store with a proxy config — having a proxy allows us to do all sorts of great things like remote paging, filtering, and sorting. For this app, we set autoload to true, so it automatically loads data into the grid. The raw data isn’t particularly sorted by any criteria, so we’re going to have it sort on the client-side by specifying the name property.

```
this.store =        new Ext.data.Store({            data: stocks,            autoLoad: true,            sorters: [{                property: 'name'            }],            listeners: {                update: this.onRecordUpdated            }})
```

In the Grid, assign the store config to the store that we created.

```
<Grid store={this.store}>
```

```
       ...</Grid>
```

Now running _npm start_, our app has a grid with all the data as shown below:

![Image](https://cdn-media-1.freecodecamp.org/images/tKgjkb2j9G5QRJgARyZgagZBCdI1nJLZGdoP)
_Basic Grid with data_

With this simple React code, you get a lot of features for free. These features include sorting, which allows you to click on any column header and it automatically sorts on the client side. If we implemented a real back-end API, we could configure the Store Proxy to do remote sorting on the back-end and use an “order by” clause in the database to do a sort. ExtReact Grid also provides resizable columns for free. So the user can drag the column from side to side.

ExtReact Grid also provides a nice grouping feature. Your app user can group by industry, and the application will group all of the data by the industry. The ExtReact Grid will give you a pinned header as you scroll down for each of the groupings.

![Image](https://cdn-media-1.freecodecamp.org/images/XmuNfIYeVCiAAnMmZypdGekVKLOJohV7ZPR9)
_Grouping by Industry_

As you run your app, you’ll notice that this data is rendering pretty quickly for 10,000 records. The reason it renders so quickly is because it’s using what we call _Buffered Rendering_. With _buffered rendering_, on initial loading, Grid renders data that is a little bit more than what you actually see in terms of the “view port height.” As you scroll down, it’s actually replacing the content of the Grid cells with the newer records as you page down in the store. So the Grid is actually conserving the DOM elements as much as possible. By keeping the DOM small, it keeps memory consumption small and ensures high application performance.

[See the code up to this step](https://github.com/adwankar/react16-stocks-grid/tree/adding-stocks-store-6.6) on GitHub.

### **Styling your Stocks Grid**

You want to style the Grid, so that the data is easier to analyze.

#### **Using Grid Cell prop**

Let’s take a look at controlling the styling of grid cells. We want to make the name bold — the best way to do that is by using the cell prop. The grid cell takes a number of configs that controls what the cell looks like. We’ll throw a style config on there, and then we’ll say fontWeight equals bold.

```
cell={ { style: {fontWeight:'bold'}}}
```

#### **Adding a Button in a Row**

Now, let’s say we want to have a button that we can click to buy one of these stocks. To do that, we can add a column with a button. This time we’re not going to add a data index because it doesn’t correspond to any field in the Store. We are going to add a WidgetCell with a Button. We’ll do some styling — we’re going to put action round UI on it, so the button will have a round action look as below:

```
<Column >    <WidgetCell>        <Button ui ="round action"                 handler = {this.buyHandler}                  text = "Buy"/>    </WidgetCell></Column>
```

The buy handler that we’re going to use is very simple. When you click the buy button, we’re just going to show a little message that says the symbol of the stock that you’re buying. When you click it, it’s going to call this function:

```
buyHandler = (button) => {      let gridrow = button.up('gridrow'),      record = gridrow.getRecord();      Ext.toast(`Buy ${record.get('name')}`)}
```

![Image](https://cdn-media-1.freecodecamp.org/images/2xNENu00B48uW-DSzPjjcsrOlG-ryTuembWZ)
_Adding button in a grid_

As you can see from this example that you can basically embed any ExtReact component inside an ExtReact Grid cell, and it’s fully interactive.

[See the code up to this step](https://github.com/adwankar/react16-stocks-grid/tree/adding-stocks-grid-component-6.6) on GitHub

### Adding a Trends Sparkline Chart to Stocks Grid

In Stocks Data, we have an array of ticks on the last five stock sales. Let’s embed that as a Sparkline chart inside the grid. Again, we’re going to use Widgetcell to render the ExtReact component inside a grid cell.

```
<Column dataIndex="ticks"         text="Trend"         sortable={false}         cell = { {                xtype: 'widgetcell',               forceWidth: true,               widget: {                        xtype: 'sparklineline',                        tipTpl:                        'Price: {y:number("0.00")}'               }        } }/>
```

As you run your app with _npm start_, use your mouse to hover over different points in the sparkline chart, it will display the Y value formatted with two decimal points.

![Image](https://cdn-media-1.freecodecamp.org/images/YryHE9CDxi45TvsePo3BddZMCxxS-A2aWo3B)
_Trends chart in a grid_

[See the code up to this step](https://github.com/adwankar/react16-stocks-grid/tree/adding-sparkline-chart-6.6) on GitHub.

### Exporting Stocks Data to Excel

As with any data-intensive application, we want the capability to export the data to Excel. To add that capability, we will add gridexporter to plugins prop to a grid as shown:

```
<Grid      ..      plugins={{            gridexporter: true,      }}>
```

We’ll add a few more components to the app to make it easy to call the export functionality. We’ll add titlebar and dock titlebar at the top of the grid and put a menu inside. When you click on the “export” button, you will have the option to export either to Excel or CSV.

```
<TitleBar docked="top" title="Stocks">           <Button align="right" text="Export">                    <Menu indented={false}>                           <MenuItem text="Excel"                                 handler=                               {this.export.bind(this, 'excel07')}/>                            <MenuItem text="CSV"                                  handler=                                  {this.export.bind(this, 'csv')}/>                     </Menu&gt;            </Button></TitleBar>
```

The export handler will pass along the type of the export and extension of the filename as shown:

```
export = (type) => {            this.grid.cmp.saveDocumentAs(           { type, title: 'Stocks' });}
```

You will need to pass the exporter in the package.json dependencies as shown:

```
"@sencha/ext-exporter": "~6.6.0"
```

You will need install the dependency with _npm install_ and then _npm star_t to run the app.

![Image](https://cdn-media-1.freecodecamp.org/images/2P5JfBKrfGAjSiYK2fcWAh5q-mrKjVAY9Pdd)
_Exporting grid data_

The Exporter plugin enables data export to various file formats. It supports native XSLX, Excel XML as well as HTML and CSV/TSV (comma/tab separated value) formats.

[See the code up to this step](https://github.com/adwankar/react16-stocks-grid/tree/adding-exporter-6.6) on GitHub.

### Adding an Editing Capability to a Stocks Grid

The spreadsheet requires the capability to edit the data. To add that capability, we’ll need to add another Grid plugin called gridcellediting. By adding this plugin and marking columns as editable, you now have a spreadsheet that can be edited by double-clicking on any grid cell. You can continue to edit the grid by tabbing through the grid cells.

Add grid cell editing plugin with _gridcellediting: true_ and making “Name” editable in the Grid column as shown:

```
<Column        dataIndex="name"        text="Name"        width={300}        cell={ { style: {fontWeight:'bold'}}}        editable/>
```

As you run your app with _npm start_, you will now able to edit grid cells.

![Image](https://cdn-media-1.freecodecamp.org/images/5l9b0vUDDMx6spxsIIVHQRryUU89eFsJ4EaQ)
_Edit capability in a Grid_

#### **Handling Edit Events**

After editing the grid cell, you will need to listen to that event on the store for the data changes. You do that by adding a listener config and a listener for “update event”. The update event will pass a number of parameters including store, updated record, the object that describes the operation that happened, and then passes an array of changed field names. You will add that in the handler.

In this app, we’re just showing a toast message. In the real-world application, you would actually apply business logic such as persisting change in the database.

```
...
```

```
listeners: {            update: this.onRecordUpdated }
```

```
...
```

```
onRecordUpdated = (store, record, operation, modifiedFieldNames) => {      const field = modifiedFieldNames[0];      Ext.toast(`${record.get('name')}                  ${field} updated to  ${record.get(field)}`) }
```

#### **Adding a Select Option to a Grid Cell**

If you want to add a “Select” option to a Grid cell, you can do that using another ExtReact component called SelectField. You just add the SelectField ExtReact component in the required Column.

```
<Column dataIndex="sector" text="Sector" width={200} editable>         <SelectField options={sectors}/&gt;</Column
```

As you run your app with _npm start_, you will now able to see select options as shown:

![Image](https://cdn-media-1.freecodecamp.org/images/ttfWeJagFIacxsRk63TrcVdiecmSSlxRHAp9)
_Adding select option to grid_

[See the code up to this step](https://github.com/adwankar/react16-stocks-grid/tree/adding-grid-editing-6.6) on GitHub.

### Optimizing Stocks Spreadsheet for Mobile Experience

This application works well for the desktop experience, but you may want to provide an optimized experience when using the same app on the mobile phone browser. For this app, the cell editing may not be the best experience for small screen mobile phone editing. For small screen devices, you may want to choose a different editing style.

The ExtReact _platformconfig_ option allows you to specify behavior for desktop or mobile. You can set any prop to a different value based on _platformConfig_ and here we’re setting the plugin based on the platform. In this example, we’ll use _gridcellediting_ when the application is on the desktop. When the application is on mobile, we’ll use _grideditable_ which provides a better way to edit data on mobile devices as shown:

```
platformConfig= {{                desktop: {                        plugins: {                            gridexporter: true,                            gridcellediting: true                        }                },                '!desktop': {                        plugins: {                            gridexporter: true,                            grideditable: true                        }                }}}
```

As you run your app with _npm start_, you will now able to see the mobile view as shown:

![Image](https://cdn-media-1.freecodecamp.org/images/6oo5ww0cXrXu-scyA5PQok1jEKQNnMvCjgDG)
_Stocks app on a mobile device_

[See the code up to this step](https://github.com/adwankar/react16-stocks-grid) on GitHub.

### Summary

This Stocks spreadsheet app shows how easy it is to create spreadsheet-like interface easily in your data-driven web application using React 16 and Sencha ExtReact. You can view the completed running app in [Sencha Fiddle](https://fiddle.sencha.com/?extreact#view/editor&fiddle/2l0s).

