---
title: How to create a realtime app using Socket.io, React, Node & MongoDB
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-29T21:43:18.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-realtime-app-using-socket-io-react-node-mongodb-a10c4a1ab676
coverImage: https://cdn-media-1.freecodecamp.org/images/1*j_kShofJmfZ_-bEpt1IS8Q.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Honey Thakuria

  Ever wondered how real time apps are built? Ever noticed the importance and use
  cases of real time applications?

  If you are curious about the above questions and need an answer, then this blog
  post is for you.

  First, let’s identify ...'
---

By Honey Thakuria

Ever wondered how real time apps are built? Ever noticed the importance and use cases of real time applications?

If you are curious about the above questions and need an answer, then this blog post is for you.

First, let’s identify a few use cases needing real time applications:

1. Getting location updates for your cab on a map of a cab booking application.
2. Getting new messages instantly on your favourite chatting application.
3. Food order info update to the kitchen of your favourite restaurant.

These all are the common scenarios of our day to day lives where we can’t tolerate a delay in the updating of information and hence need real time communication.

**Technologies** which can be used for **realtime communication** are:

1. **Short Polling**: AJAX, creates heavy traffic.
2. **Long Polling**: Like AJAX, but the server holds on the response until it has an update. After receiving it, the client sends another request, and needs additional header to be traversed back and forth causing additional overhead.
3. **Web Sockets**: make it possible to open interactive communication between the client and server. One can send a request to the server and receive event driven responses without Polling the server for a reply, making web sockets a **best choice** for our use case.

More in-depth info about the above three technologies can be read [here](https://stackoverflow.com/questions/12555043/my-understanding-of-http-polling-long-polling-http-streaming-and-websockets).

We will be learning to create a real time application by covering the following scenario.

Imagine you are sitting at your favourite restaurant and have a digital menu. You place the order and the kitchen gets updated regarding your order in real time. When the kitchen is done with the order, they update it in real time too.

Features in detail:

1. **Place Order**: Interface to select the quantity and place the order for a selected food item to the kitchen.
2. **Kitchen**: Interface which can be opened across multiple kitchens and updates in real time the chefs and cooks regarding the total orders created and predicted quantity of food items, giving them the flexibility to update it. Also has a functionality to download the report in the form of an excel sheet.
3. **Change Predicted**: Interface to update the predicted quantity of food items.

![Image](https://cdn-media-1.freecodecamp.org/images/6EyW3Wo0cKhjTFMskVgaWeTAaVS-3m26bhzL)

**A live demo** of this scenario can be found [here](https://faasos-honey.herokuapp.com/).

For better understanding, open it in different tabs/devices at the same time to see the data change in real time.

**The source code** is [here](https://github.com/honey93/OrderKitchen). Feel free to make something innovative/useful on top of it.

So let’s get started.

### Technology Stack:

**Frontend**: React.js, Reactstrap, Socket.io

**Backend**: Node.js (Express), MongoDB, Socket.io

### Folder Structure:

```
/*
Go to the root directory in the source code and find out the below-mentioned files. This architecture helps in creating a big modular App.
*/
backend-my-app/ /* Backend code of the app */
 server.js       /* Socket and backend code resides here*/
 build/      /* Optional for deployment of Frontend Build */ 
 package.json /* Backend dependency */
 ...
public/
src/  /*      Frontend Sourcecode      */
 global/      /*   Components getting used everywhere   */
  header.css
  header.js     
 main/           
  Kitchen.js
  PlaceOrder.js
  UpdatePredicted.js
 App.js   /* Routing logic and component assembly part */
package.json /* Frontend dependency */ 
 ............
```

### Explanation of source code:

#### Frontend:

```
git clone https://github.com/honey93/OrderKitchen.git
cd OrderKitchen
npm install
npm start
```

Packages used:

1. [Reactstrap](https://reactstrap.github.io/): Easy to use bootstrap4 components
2. [Socket.io](https://socket.io/docs/): Socket.io is a library that enables real-time, bidirectional and event-based communication between the browser and the server.
3. [react-html-table-to-excel](https://www.npmjs.com/package/react-html-table-to-excel): Provides a client side generation of Excel (.xls) file from HTML table element.
4. [react-router-dom](https://www.npmjs.com/package/react-router-dom): DOM bindings for react router. It consists of many important components like BrowserRouter used when there is a server to handle dynamic request, Switch, Route, etc.

#### **App Component**

**Path**: src/App.js

This component contains the main routing logic of the Frontend. This file is used in src/index.js inside the Browser Router Module. The below code demonstrates one of the approaches to keep your app modular.

```javascript
import React, { Component } from "react";
import "./App.css";
import { Header } from "./global/header";
import { Switch, Route } from "react-router-dom";
import PlaceOrder from "./main/PlaceOrder";
import UpdatePredicted from "./main/UpdatePredicted";
import Kitchen from "./main/Kitchen";
/*The <Route> component is the main part of React Router. Anywhere that you want to only render content based on the location’s pathname, you should use a <Route> element. */
/* The Route component expects a path prop, which is a string that describes the pathname that the route matches */
/* The <Switch> will iterate over routes and only render the first one that matches the current pathname */
class App extends Component {
  render() {
    return (
      <div className="App">
        <Header />
        <Switch>
          <Route exact path="/" component={PlaceOrder} />
          <Route path="/updatepredicted" component={UpdatePredicted} />
          <Route path="/kitchen" component={Kitchen} />
        </Switch>
      </div>
    );
  }
}
export default App;
```

#### **Header Component**

**Path**: src/global/header.js

This component will be common and used across the sections like Place Order, Change Predicted, Kitchen. This approach helps avoid code duplication and keeps the application modular.

```js
import React, { Component } from "react";
import { NavLink } from "react-router-dom";
import socketIOClient from "socket.io-client";
import "./header.css";
// The Header creates links that can be used to navigate
// between routes.
var socket;
class Header extends Component {
/* Creating a Socket client and exporting it at the end to be used across the Place Order, Kitchen, etc components*/
  constructor() {
    super();
    this.state = {
      endpoint: 'http://localhost:3001/'
    };
socket = socketIOClient(this.state.endpoint);
  }
render() {
    return (
      <header>
        <nav>
          <ul className="NavClass">
            <li>
              <NavLink exact to="/">
                Place Order
              </NavLink>
            </li>
            <li>
              <NavLink to="/updatepredicted">Change Predicted </NavLink>
            </li>
            <li>
              <NavLink to="/kitchen"> Kitchen </NavLink>
            </li  >
          </ul>
        </nav>
      </header>
    );
  }
}
export { Header, socket };
```

#### **Kitchen Component**

**Path**: src/main/Kitchen.js

The Kitchen Screen UI logic and html code resides in this component:

```js
import React, { Component } from "react";
import { Button, Table, Container } from "reactstrap";
import { socket } from "../global/header";
import ReactHTMLTableToExcel from "react-html-table-to-excel";
class Kitchen extends Component {
  constructor() {
    super();
    this.state = {
      food_data: []
      // this is where we are connecting to with sockets,
    };
  }
getData = foodItems => {
    console.log(foodItems);
    this.setState({ food_data: foodItems });
  };
changeData = () => socket.emit("initial_data");
/*As soon as the component gets mounted ie in componentDidMount method, firing the initial_data event to get the data to initialize the Kitchen Dashboard */
/* Adding change_data listener for listening to any changes made by Place Order and Predicted Order components*/ 
componentDidMount() {
    var state_current = this;
    socket.emit("initial_data");
    socket.on("get_data", this.getData);
    socket.on("change_data", this.changeData);
  }

/* Removing the listener before unmounting the component in order to avoid addition of multiple listener at the time revisit*/
componentWillUnmount() {
    socket.off("get_data");
    socket.off("change_data");
  }
/* When Done gets clicked, this function is called and mark_done event gets emitted which gets listened on the backend explained later on*/
markDone = id => {
    // console.log(predicted_details);
    socket.emit("mark_done", id);
  };
getFoodData() {
    return this.state.food_data.map(food => {
      return (
        <tr key={food._id}>
          <td> {food.name} </td>
          <td> {food.ordQty} </td>
          <td> {food.prodQty} </td>
          <td> {food.predQty} </td>
          <td>
            <button onClick={() => this.markDone(food._id)}>Done</button>
          </td>
        </tr>
      );
    });
  }
render() {
    return (
      <Container>
        <h2 className="h2Class">Kitchen Area</h2>
        <ReactHTMLTableToExcel
          id="test-table-xls-button"
          className="download-table-xls-button"
          table="table-to-xls"
          filename="tablexls"
          sheet="tablexls"
          buttonText="Download as XLS"
        />
<Table striped id="table-to-xls">
          <thead>
            <tr>
              <th>Name</th>
              <th>Quantity</th>
              <th>Created Till Now</th>
              <th>Predicted</th>
              <th>Status</th>
            </tr>
          </thead>
          <tbody>{this.getFoodData()}</tbody>
        </Table>
      </Container>
    );
  }
}
export default Kitchen;
```

#### **Place Order Component**

**Path**: src/main/PlaceOrder.js

```js
import React, { Component } from "react";
import { Button, Table, Container } from "reactstrap";
import { socket } from "../global/header";
class PlaceOrder extends Component {
  constructor() {
    super();
    this.state = {
      food_data: []
      // this is where we are connecting to with sockets,
    };
  }
getData = foodItems => {
    console.log(foodItems);
    foodItems = foodItems.map(food => {
      food.order = 0;
return food;
    });
    this.setState({ food_data: foodItems });
  };
componentDidMount() {
    socket.emit("initial_data");
    var state_current = this;
    socket.on("get_data", state_current.getData);
  }
componentWillUnmount() {
    socket.off("get_data", this.getData);
  }
//Function to place the order.
sendOrder = id => {
    var order_details;
    this.state.food_data.map(food => {
      if (food._id == id) {
        order_details = food;
      }
      return food;
    });
    console.log(order_details);
    socket.emit("putOrder", order_details);
    var new_array = this.state.food_data.map(food => {
      food.order = 0;
      return food;
    });
    this.setState({ food_data: new_array });
  };
// Changing the quantity in the state which is emitted to the backend at the time of placing the order.
changeQuantity = (event, foodid) => {
    if (parseInt(event.target.value) < 0) {
      event.target.value = 0;
    }
    var new_array = this.state.food_data.map(food => {
      if (food._id == foodid) {
        food.order = parseInt(event.target.value);
      }
      return food;
    });
    this.setState({ food_data: new_array });
  };
// To get the initial data
getFoodData() {
    return this.state.food_data.map(food => {
      return (
        <tr key={food._id}>
          <td> {food.name} </td>
          <td>
            <input
              onChange={e => this.changeQuantity(e, food._id)}
              value={food.order}
              type="number"
              placeholder="Quantity"
            />
          </td>
          <td>
            <button onClick={() => this.sendOrder(food._id)}>Order</button>
          </td>
        </tr>
      );
    });
  }
render() {
    return (
      <Container>
        <h2 className="h2Class">Order Menu</h2>
        <Table striped>
          <thead>
            <tr>
              <th>Product</th>
              <th>Quantity</th>
              <th>Order</th>
            </tr>
          </thead>
          <tbody>{this.getFoodData()}</tbody>
        </Table>
      </Container>
    );
  }
}
export default PlaceOrder;
```

One more section called Update Predicted Path: src/main/UpdatePredicted.js similar to above section is there in the code repository.

### Backend

Starting the Backend:

```
cd backend-my-app
npm install
node server.js
```

Packages used:

1. [**Monk**](https://www.npmjs.com/package/monk): A tiny layer that provides simple yet substantial usability improvements for MongoDB usage within Node.JS.
2. [**Socket.io**](https://socket.io/docs/): Socket.io is a library that enables real-time, bidirectional and event-based communication between the browser and the server.

3. [**Express**](https://www.npmjs.com/package/express): Fast, minimalist web framework for [node](http://nodejs.org/).

#### **Main Code**

**Path**: backend-my-app/server.js

```js
const express = require("express");
const http = require("http");
const socketIO = require("socket.io");
// Connection string of MongoDb database hosted on Mlab or locally
var connection_string = "**********";
// Collection name should be "FoodItems", only one collection as of now.
// Document format should be as mentioned below, at least one such document:
// {
//     "_id": {
//         "$oid": "5c0a1bdfe7179a6ca0844567"
//     },
//     "name": "Veg Roll",
//     "predQty": 100,
//     "prodQty": 295,
//     "ordQty": 1
// }
const db = require("monk")(connection_string);
const collection_foodItems = db.get("FoodItems");
// our localhost port
const port = process.env.PORT || 3000;
const app = express();
// our server instance
const server = http.createServer(app);
// This creates our socket using the instance of the server
const io = socketIO(server);
io.on("connection", socket => {
//  console.log("New client connected" + socket.id);
  //console.log(socket);
// Returning the initial data of food menu from FoodItems collection
  socket.on("initial_data", () => {
    collection_foodItems.find({}).then(docs => {
      io.sockets.emit("get_data", docs);
    });
  });
// Placing the order, gets called from /src/main/PlaceOrder.js of Frontend
  socket.on("putOrder", order => {
    collection_foodItems
      .update({ _id: order._id }, { $inc: { ordQty: order.order } })
      .then(updatedDoc => {
        // Emitting event to update the Kitchen opened across the devices with the realtime order values
        io.sockets.emit("change_data");
      });
  });
// Order completion, gets called from /src/main/Kitchen.js
  socket.on("mark_done", id => {
    collection_foodItems
      .update({ _id: id }, { $inc: { ordQty: -1, prodQty: 1 } })
      .then(updatedDoc => {
        //Updating the different Kitchen area with the current Status.
        io.sockets.emit("change_data");
      });
  });

// Functionality to change the predicted quantity value, called from /src/main/UpdatePredicted.js
  socket.on("ChangePred", predicted_data => {
    collection_foodItems
      .update(
        { _id: predicted_data._id },
        { $set: { predQty: predicted_data.predQty } }
      )
      .then(updatedDoc => {
        // Socket event to update the Predicted quantity across the Kitchen
        io.sockets.emit("change_data");
      });
  });

// disconnect is fired when a client leaves the server
  socket.on("disconnect", () => {
    console.log("user disconnected");
  });
});
/* Below mentioned steps are performed to return the Frontend build of create-react-app from build folder of backend Comment it out if running locally*/
app.use(express.static("build"));
app.use("/kitchen", express.static("build"));
app.use("/updatepredicted", express.static("build"));
server.listen(port, () => console.log(`Listening on port ${port}`));
```

**Database**: MongoDB

[**Mlab**](https://mlab.com/): Database as a service for MongoDB

**Collection Name**: FoodItems

**Document format**: At least one document is needed in the FoodItems collection with the below mentioned format.

```js
{
"name": "Veg Roll",  // Food Name
"predQty": 100,  // Predicted Quantity
"prodQty": 295,  // Produced Quantity
"ordQty": 1   // Total Order Quantity
}
```

Hope you got the understanding of how to create a modular real time app using the trending MERN stack. If you found it helpful **clap** below, give **stars** to the project [repo](https://github.com/honey93/OrderKitchen) and share with your friends too.

