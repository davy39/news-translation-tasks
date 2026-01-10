---
title: How to Build a Real-time Editable Datagrid In React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-28T16:27:13.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-real-time-editable-datagrid-in-react-c13a37b646ec
coverImage: https://cdn-media-1.freecodecamp.org/images/1*qguZN_QzVYcECU_UpG799A.gif
tags:
- name: data
  slug: data
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Peter Mbanugo

  A datagrid enables you to display and edit data. This is a vital feature in most
  data-driven applications.

  You may have implemented this in one of your React apps in the past. Maybe you used
  libraries like react-bootstrap-table, reac...'
---

By Peter Mbanugo

A datagrid enables you to display and edit data. This is a vital feature in most data-driven applications.

You may have implemented this in one of your React apps in the past. Maybe you used libraries like [react-bootstrap-table](https://react-bootstrap-table.github.io/react-bootstrap-table2/), [react-grid](https://github.com/eddyson-de/react-grid), or [react-table](https://react-table.js.org/). With those, you can add a Datagrid to your React app. But what if you want the changes to be done in real-time and updates synchronized across all connected devices and their browsers?

In this article, I will show you how to build a real-time datagrid in React using [react-table](https://react-table.js.org/) and [Hamoni Sync](https://www.hamoni.tech/).

react-table is a lightweight and fast library for rendering tables in React, and it supports pagination and many more features.

Hamoni Sync is a real-time state synchronization service which enables you to synchronize your application state in real-time. I will show you how to build a datagrid with people’s first and last names.

If you want to follow along, you should have some knowledge of React and have the following tools installed:

1. [NodeJS](https://dev.to/nodejs.org)
2. [npm](http://npmjs.com/) & [npx](https://github.com/zkat/npx). If you have installed npm version 5.2.0 or greater, it installs npx alongside npm.
3. [create-react-app](https://github.com/facebook/create-react-app)

### Create the React app

First we will create a new React project using create-react-app.

Open the command line and run `npx create-react-app realtime-react-datatable`. This will bootstrap a React application for us by creating a new directory `realtime-react-datatable` with the files needed to build a React application.

With the React app created, we need to install react-table and Hamoni Sync. Still on the command line, run `cd realtime-react-datatable` to switch to the directory for the app. Run `npm i react-table hamoni-sync` in the command line to install both packages.

### Render the Datagrid

To render the datagrid, we will use the react-table component. Open the file `src/App.js` and update it with the code below:

```
import React, { Component } from "react";import logo from "./logo.svg";import "./App.css";// Import React Tableimport ReactTable from "react-table";import "react-table/react-table.css";// Import Hamoni Syncimport Hamoni from "hamoni-sync";
```

```
class App extends Component {  constructor() {    super();    this.state = {      data: [],      firstName: "",      lastName: ""    };  }
```

```
  handleChange = event => {    if (event.target.name === "firstName")      this.setState({ firstName: event.target.value });    if (event.target.name === "lastName")      this.setState({ lastName: event.target.value });  };
```

```
  handleSubmit = event => {    event.preventDefault();  };
```

```
  renderEditable = cellInfo => {    return (      <div        style={{ backgroundColor: "#fafafa" }}        contentEditable        suppressContentEditableWarning        onBlur={e => {          const data = [...this.state.data];          data[cellInfo.index][cellInfo.column.id] = e.target.innerHTML;          this.setState({ data });        }}        dangerouslySetInnerHTML={{          __html: this.state.data[cellInfo.index][cellInfo.column.id]        }}      />    );  };
```

```
  render() {    const { data } = this.state;
```

```
    return (      <div className="App">        <header className="App-header">          <img src={logo} className="App-logo" alt="logo" />          <h1 className="App-title">Welcome to React</h1>        </header>        <p className="App-intro">          <form onSubmit={this.handleSubmit}>            <h3>Add new record</h3>            <label>              FirstName:              <input                type="text"                name="firstName"                value={this.state.firstName}                onChange={this.handleChange}              />            </label>{" "}            <label>              LastName:              <input                type="text"                name="lastName"                value={this.state.lastName}                onChange={this.handleChange}              />            </label> 
```

```
            <input type="submit" value="Add" />          </form>        </p>        <div>          <ReactTable            data={data}            columns={[              {                Header: "First Name",                accessor: "firstName",                Cell: this.renderEditable              },              {                Header: "Last Name",                accessor: "lastName",                Cell: this.renderEditable              },              {                Header: "Full Name",                id: "full",                accessor: d => (                  <div                    dangerouslySetInnerHTML={{                      __html: d.firstName + " " + d.lastName                    }}                  />                )              }            ]}            defaultPageSize={10}            className="-striped -highlight"          />        </div>      </div>    );  }}
```

```
export default App;
```

The code above renders a form and an editable react-table component. `<ReactTable` /> renders a component `wit`h `data, c`olumns`, and defaultPa`geSize props`. Th`e data props holds the data to display`, and c`olumns props for the column definition`. The ac`cessor proper`ty in c`olumns props indicates the property that holds the value to be displayed for that co`lumn. Cell: this.renderEd`itable proper`ty in c`olumns props tells react-table that the column is editable. The other funct`ions (handle`Sub`mit & handle`Change) allows getting new data entry from the form on the page.

### Add Hamoni Sync

The data for the datagrid will be retrieved and updated in real-time using Hamoni Sync. We already imported the Hamoni library on line 18 in `App.js`;

```
import Hamoni from "hamoni-sync";
```

We need to initialize it and connect to Hamoni server. To do this we need an account and application ID. Follow these steps to create an application in Hamoni.

1. Register and login to Hamoni [dashboard](https://dashboard.hamoni.tech/)
2. Enter your preferred application name in the text field and click the create button. This should create the app and display it in the application list section.
3. Click the button “Show AccountID” to see your account ID.

![Image](https://cdn-media-1.freecodecamp.org/images/JcOI2Oer-YfeEh3ITndyiaF98c1GIRrUQoeN)

Add the following code to `App.js` to initialise and connect to Hamoni Sync server.

```
componentDidMount() {    let hamoni = new Hamoni("ACCOUNT_ID", "APP_ID");
```

```
    hamoni      .connect()      .then(() =>; {
```

```
      })      .catch(console.log);  }
```

The code above will connect the client device or browser to Hamoni Sync server. Copy your account and application ID from the dashboard and replace them with the string placeholder respectively.

Add the following to the function in the `then()` block, to be executed when it successfully connects to the server:

```
hamoni    .get("datagrid")    .then(listPrimitive => {      this.listPrimitive = listPrimitive;
```

```
      this.setState({        data: [...listPrimitive.getAll()]      });
```

```
      listPrimitive.onItemAdded(item => {        this.setState({ data: [...this.state.data, item.value] });      });
```

```
      listPrimitive.onItemUpdated(item => {        let data = [        ...this.state.data.slice(0, item.index),        item.value,        ...this.state.data.slice(item.index + 1)        ];
```

```
        this.setState({ data: data });      });
```

```
      listPrimitive.onSync(data => {        this.setState({ data: data });      });    })    .catch(console.log);
```

The code above calls `hamoni.get("datagrid")` to get the data, with `datagrid` as the name of the application state on Hamoni Sync. Hamoni Sync allows you to store 3 kinds of state referred to as Sync primitives. They are:

1. **Value Primitive**: This kind of state holds simple information represented with datatypes like string, boolean or numbers. It is best suited for cases such as unread message count, toggles, etc.
2. **Object Primitive**: Object state represents states that can be modeled as a JavaScript object. An example usage could be storing the score of a game.
3. **List Primitive**: This holds a list of state objects. A state object is a JavaScript object. You can update an item based on its index in the list.

If the state is available it resolves and returns a promise with the state primitive object. This object gives us access to methods to update state and get state updates in real-time.

On line 36 we used the `getAll()` method to get data and set the state for the React component. Also, the methods `onItemAdded()` and `onItemUpdated()` are used to get updates when an item is added or updated. The `onSync()` method is useful in a scenario where a device or browser loses connection, and when it reconnects, it tries to get the latest state from the server and update the local state if there's any.

### Add & Update items

From the previous section, we are able to get the data for the datagrid and update the state when an item is added or update. Let’s add code to add new items and update an item when a column has been edited. Add the following code to the `handleSubmit` method:

```
handleSubmit = event => {    this.listPrimitive.push({        firstName: this.state.firstName,        lastName: this.state.lastName    });    this.setState({ firstName: "", lastName: "" });    event.preventDefault();};
```

This code gets the first and last name from the form and adds it to the list state primitive on Hamoni Sync by calling the `push()` method. This will trigger the `onItemAdded()` method.

In order to update items as they get edited in the datagrid, we will update the function passed to the `onBlur` props on line 84 as follows:

```
onBlur={e => {    let row = this.state.data[cellInfo.index];    row[cellInfo.column.id] = e.target.innerHTML;    this.listPrimitive.update(cellInfo.index, row);}}
```

This code updates the item at the index retrieved from the `cellInfo` object. To update a list state primitive in Hamoni Sync, you call the `update()`method with the index of the item and the value to update. The `renderEditable` method should now look like this after the last change:

```
renderEditable = cellInfo => {    return (      <div        style={{ backgroundColor: "#fafafa" }}        contentEditable        suppressContentEditableWarning        onBlur={e => {          let row = this.state.data[cellInfo.index];          row[cellInfo.column.id] = e.target.innerHTML;          this.listPrimitive.update(cellInfo.index, row);        }}        dangerouslySetInnerHTML={{          __html: this.state.data[cellInfo.index][cellInfo.column.id]        }}      />    );  };
```

At this point we have almost all that’s needed to run the app except the initial data that will be rendered on the datagrid.

We need to create the state and give it some data on Hamoni Sync. Add a new file **seed.js** at the root of your working directory and add to it the following code:

```
const Hamoni = require("hamoni-sync");
```

```
let hamoni = new Hamoni("AccountID", "APP_ID");
```

```
hamoni  .connect()  .then(response => {    hamoni      .createList("datagrid", [        { firstName: "James", lastName: "Darwin" },        { firstName: "Jimmy", lastName: "August" }      ])      .then(() => console.log("create success"))      .catch(console.log);  })  .catch(console.log);
```

This will create a list primitive state on Hamoni Sync, with a name of `datagrid`. Replace the `AccountID` and `APP_ID` string with your account and application ID. Open the command line and run `node seed.js`. This should succeed and print out `create success` message.

Now we can start the React app and see our app in action! Run the command `npm start` in the command line and it'll open the application in your default browser.

![Image](https://cdn-media-1.freecodecamp.org/images/gKCOU6o-Pi075R0WC-czpeuKbAyoOr7m7dCD)

Hooray! We have a real-time editable datagrid with pagination!

### Conclusion

We have built a real-time datagrid in React using [react-table](https://react-table.js.org/) and [Hamoni Sync](https://www.hamoni.tech/). With react-table powering the datagrid and Hamoni Sync handling the state for the datagrid. This was all achieved in few lines of code and less effort designing real-time state logic. You can get the finished app of what we built on [GitHub](https://github.com/pmbanugo/realtime-react-datatable). It’s possible to track which cell is being edited or lock the cells currently being edited by another user. I’ll leave that as a weekend hack for you.

Feel free to leave a comment if anything is not clear or encounter problems while trying to add lock or highlight cells being edited.

Happy coding ?

