---
title: How to Build a Custom Dashboard with WordPress APIs and React
subtitle: ''
author: Marco Venturi
co_authors: []
series: null
date: '2022-02-18T15:59:20.000Z'
originalURL: https://freecodecamp.org/news/build-a-custom-dashboard-with-wordpress-apis-and-react
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/stephen-dawson-qwtCeJ5cLYs-unsplash.jpg
tags:
- name: React
  slug: react
- name: WordPress
  slug: wordpress
seo_title: null
seo_desc: "When you manage websites, it is all about data: views, response time, users,\
  \ bounce rate, and so on. And, if you manage websites, you've likely had to deal\
  \ with a WordPress instance at least once. \nThere are hundreds – or maybe thousands\
  \ – of WordPre..."
---

When you manage websites, it is all about data: views, response time, users, bounce rate, and so on. And, if you manage websites, you've likely had to deal with a WordPress instance at least once. 

There are hundreds – or maybe thousands – of WordPress plugins to retrieve and show data. But WordPress APIs can give us a hand if we want to build a custom dashboard with some specific information we want to get. 

That's why today I want to share with you how to build a service that retrieves data from our WordPress instance and shows them on a table. To be more specific, I want to know the number the plugins I'm using and what plugins I've installed previously that I'm not using anymore. 

## Why should I know what WordPress plugins I'm using?

I always found this information to be very important. Especially at the beginning of your journey with WordPress, you might be tempted to install a plugin for every single functionality you want your websites to have. 

Well, plugins may be easy to install but they also have some potential drawbacks:

* If not updated often, they can expose your website to attacks and vulnerabilities
* They can make the loading time of your website much longer than it should be
* Some of the plugins might conflict with each other

I'm not saying you shouldn't use or trust plugins. But it is something you have to pay attention to. So let's see how we can have some useful information about our plugins at our fingertips.

### What tools I'll be using

* WordPress APIs – I'll work with the "plugins" endpoint.
* React – I'll create a component to display data. 
* Axios – I'll use it to call APIs easily.
* React-Bootstrap – I chose this library just to get a nice and easy-to-use table component quickly.
* Postman – This is the tool I always use to test APIs.
* Npm – I'll use it to create a React app and install packages.

## WordPress APIs

As I said at the beginning of this article, I want to call a specific endpoint to get JSON with the information about the plugins I've installed on my instance. Precisely, I want to count the plugins I currently use ("active") and the plugins I don't use ("inactive"). 

The [documentation](https://developer.wordpress.org/rest-api/) about the APIs is very detailed and full of useful information and concepts. So I hit "Endpoint reference" on the sidebar and scroll to click on "Plugins". 

Let's focus now on the "Schema" section. Here I find all the fields that exist in a plugin record. The list is quite long, but I need just one of these fields: "status". The documentation says it returns me a string with two possible values: "inactive" or "active". 

So this is the API I'll call to retrieve the necessary data:

```
https://<BASE_URL>/wp-json/wp/v2/plugins
```

So far so good. There's one more thing we need to take into consideration. Some endpoints require basic authentication to return data. Our endpoint is one of those. Starting version 5.6, you can pass a username and an application password to call this endpoint. 

If you want to know more about application passwords and how to generate them, I recommend you to check this [article](https://make.wordpress.org/core/2020/11/05/application-passwords-integration-guide/) written by the WordPress community.

### Time to Test the API

Once I know what endpoint I need to call and I generate my application password, I'm ready to test my API call with Postman. This is what I get:

![Image](https://www.freecodecamp.org/news/content/images/2022/02/postman.png)

As you can see, I get a JSON with the information I'm looking for: the "status" key. Now we are ready to create our React app!

## Let's Code the React App

It's now time to create the front-end of our application. As I said before, I'll use React because of its flexibility, Axios to call APIs easily, and React-Bootstrap to get ready-to-use components with a nice design. 

Before I start writing code, let's recap what I want to achieve: I want my front-end application to retrieve data from my WordPress instance about the status – active or inactive – of the plugins installed by calling the "Plugins" endpoint. 

To do so, I want my script to perform the following actions:

1. Create variables to store the count of active and inactive plugins
2. Call the endpoint by an API call
3. Iterate through the JSON – the API call returns with the following logic: If the object key "status" equals "active" increase the related count by one, otherwise increase the count related to the inactive plugins by 1. Update the related states - previously defined in the constructor - accordingly
4. Render the table by using the "Table" component from React-Bootstrap and pass the states into the table component where I want data to be displayed with the count of active and inactive plugins

Enough talking. Time to code! :)

First things first, I create my React app like this:

```
npx create-react-app report
```

Then I install Axios and React-Bootstrap:

```
npm install axios
npm install react-bootstrap bootstrap@5.1.3
```

All set. Now, in my React app, I move to the /src directory and I create a new directory called "components":

```
/src/components
```

Then I move to the components folder and I create a "Report.jsx" file. This is how the file looks now:

```jsx
import React from 'react';
import axios from 'axios';
import Table from 'react-bootstrap/Table'

class Report extends React.Component { 
  constructor(props) { 
      super(props); 
      this.state = { countActiveState: 0, countInactiveState: 0, };
  } 

  componentDidMount() {
  let countActive  = 0;
  let countInactive = 0;
  
  axios.get("https://<BASE_URL>/wp-json/wp/v2/plugins", {
    auth: {
      username: process.env.REACT_APP_USERNAME,
      password: process.env.REACT_APP_CLIENT_SECRET
    }
  })
  .then(res => {
      const plugins = res.data;
      for(let key in plugins) {
        if(plugins[key].status === "active") {
          countActive++;
          this.setState({countActiveState: countActive}); 
        }
        else{
          countInactive++;
          this.setState({countInactiveState: countInactive}); 
        }
    }
    })
    .catch(error => {
      alert("Something went wrong. Try again later.");
      console.log(error);
   })
  }

  render() { 
      return ( 
          <Table striped bordered hover >
              <thead>
                  <tr>
                  <th>Status</th>
                  <th>Plugin Amount</th>
                  </tr>
              </thead>
              <tbody>
                  <tr>
                  <th>Active</th>
                  <td>{this.state.countActiveState}</td>
                  </tr>
                  <tr>
                  <th>Inactive</th>
                  <td>{this.state.countInactiveState}</td>
                  </tr>
              </tbody>
          </Table>
      ); 
  } 
} 

export default Report;
```

Let's break it into smaller pieces and see what is going on:

```
import React from 'react';
import axios from 'axios';
import Table from 'react-bootstrap/Table'
```

I import Axios and the component "Table" from the React-bootstrap library.

```
constructor(props) { 
      super(props); 
      this.state = { countActiveState: 0, countInactiveState: 0, };
  } 
```

In the constructor I define two states: countActiveState and countInactiveState. I set both of them to 0.

```jsx
componentDidMount() {
    let countActive  = 0;
    let countInactive = 0;
```

I declare two variables and set them equal to 0: `countActive` to store the active plugin count and `countInactive` to store the inactive plugin count.

```jsx
axios.get("https://<BASE_URL>/wp-json/wp/v2/plugins", {
      auth: {
        username: process.env.REACT_APP_USERNAME,
        password: process.env.REACT_APP_CLIENT_SECRET
      }
    })
```

I use Axios to perform a GET call to the "Plugins" endpoint. I also pass the credentials for the basic auth.

```jsx
.then(res => {
      const plugins = res.data;
      for(let key in plugins) {
        if(plugins[key].status === "active") {
          countActive++;
          this.setState({countActiveState: countActive}); 
        }
        else{
          countInactive++;
          this.setState({countInactiveState: countInactive}); 
        }
    }
    })
    .catch(error => {
      alert("Something went wrong. Try again later.");
      console.log(error);
   })
  }
```

Then, after storing the response data in a variable called "plugins", I iterate through the JSON and say: "for each JSON object, check if the key "status" is equal to "active". If so, increase the countActive variable by 1 and set the countActiveState equal to countActive, else increase the countInactive variable by 1 and set the countInactiveState equal to countInactive".

```jsx
render() { 
      return ( 
          <Table striped bordered hover >
              <thead>
                  <tr>
                  <th>Status</th>
                  <th>Plugin Amount</th>
                  </tr>
              </thead>
              <tbody>
                  <tr>
                  <th>Active</th>
                  <td>{this.state.countActiveState}</td>
                  </tr>
                  <tr>
                  <th>Inactive</th>
                  <td>{this.state.countInactiveState}</td>
                  </tr>
              </tbody>
          </Table>
      ); 
  } 
} 

export default Report;
```

Then I render the Table component and I pass the countActiveState and countInactiveState where I want data to be displayed.

Lastly, I go to the App.js file and I add the Report component:

```jsx
import './App.css';
import Report from './components/Report';

function App() {

  return (
    <div className="App">
      <h1>WordPress Stats Dashboard</h1>
      <Report/>
    </div>
  );
}

export default App;
```

I start the app:

```
npm start
```

And the magic happens! :)

![Image](https://www.freecodecamp.org/news/content/images/2022/02/frontend.png)

### And there you have it!

So, this is just a quick example of how you can easily build your custom dashboard to retrieve and visualize data from your WordPress instance. 

You can use any type of graphical data representation, such as bar or pie chart. It's all up to you! 

Don't forget to have a look at my [repo](https://github.com/mventuri/react-dashboard-wordpress-api) on GitHub. Feel free to share this article and your feedback. :)

