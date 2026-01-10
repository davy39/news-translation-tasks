---
title: How to deploy a React application to Netlify that reads from a Google Sheet
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-22T19:39:47.000Z'
originalURL: https://freecodecamp.org/news/how-to-deploy-a-react-application-to-netlify-that-reads-from-a-google-sheet-97a015806c47
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9cad7b740569d1a4ca9fb9.jpg
tags:
- name: education
  slug: education
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: startup
  slug: startup
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Sergiy Dybskiy

  In this tutorial, we’re going to cover how to connect to a spreadsheet hosted on
  Google, display that information inside a React application, and deploy it to Netlify.

  Skip to “The Setup” if you don’t care where the data will be com...'
---

By Sergiy Dybskiy

In this tutorial, we’re going to cover how to connect to a spreadsheet hosted on Google, display that information inside a React application, and deploy it to Netlify.

Skip to “The Setup” if you don’t care where the data will be coming from or why I chose to build this. I won’t be mad, I promise.

Right now the final result looks like this, but I’ll be adding more features to it shortly.

![Image](https://cdn-media-1.freecodecamp.org/images/B0fW0hCrk6UNfnyhZz49Wyigj8BSLWe6H-yN)
_You can find it at [https://dougscore.netlify.com](https://dougscore.netlify.com" rel="noopener" target="_blank" title=")_

### The Why

I love cars ? ?️. If you’re even slightly interested in cars, you’ve probably at some point stumbled upon Do[ug Demuro’s Youtube channel.](https://www.youtube.com/channel/UCsqjHFMB_JYTaEnf_vmTNqg) He reviews a wide range of cars anywhere from a $3 [Million Ferrari Enzo t](https://www.youtube.com/watch?v=KhaLiiSUvAw)o a 3 [wheeled BMW Isetta.](https://www.youtube.com/watch?v=k0dEzY-xld8) Doug’s format is a little bit different than most user reviews. His roughly 20 minute videos have three main points:

* Interesting quirks and features: about 70% of the video is him taking about the car’s exterior and interior quirks. These can range from a paragraph in the owner’s manual to an interesting shape of the break lights.

![Image](https://cdn-media-1.freecodecamp.org/images/PRwgOYulrc9WjHVypGBsN84K-kMaZdTARG4W)
_Not actually Doug, but a happy doggo ?_

* Driving: about 20% of the video is Doug taking the car out on the road and making funny faces when he accelerates. He also talks about the interior noise, handling, speed, and so on.
* The DougScore: Doug created a spreadsheet with all the cars he’s ever reviewed (since creating the scoring system) and ranked all of them using his own system. It’s broken down into two categories:  
* Weekend Score: Essentially how much fun the car is.  
* Daily Score: Essentially how practical the car is.

![Image](https://cdn-media-1.freecodecamp.org/images/2pf1-UBRO1QVYtj6hntKdeHSHpr077skCXkB)
_I wonder if Doug reads all of these_

![Image](https://cdn-media-1.freecodecamp.org/images/6Mmm4aJZrLSRGzfI3fimEpDhy0BraT31sylA)
_Then he’ll find a typo on page 73_

That’s why, in my opinion, he can get over 1.5M views on a [25 minute video of a minivan](https://www.youtube.com/watch?v=oOZ_Q6qzXuw) ??‍. Since the videos are so quirky, and Doug himself is pretty quirky too, his following has come up with some creative comments. My favourite are the “Doug is the type of guy to…” remarks, like those above.

And now, to all of you who have stuck around after that intro that has nothing to do with building an app, Google Sheets API, or React, here’s what I am on about.

### The Setup

Doug keeps his [spreadsheet](https://docs.google.com/spreadsheets/d/1KTArYwDWrn52fnc7B12KvjRb6nmcEaU6gXYehWfsZSo/edit#gid=0) on Google Sheets, and anyone with a link can access it. To me, it was hard to navigate. So I decided to see if there was a way to extend it and add some additional functionality.

#### React Create App

[Facebook’s React boilerplate](https://github.com/facebook/create-react-app) will get us started fairly quickly without the need to configure any backends. In your Terminal of choice ([Hyper](https://hyper.is/) for me), go ahead and put in:

```
npx create-react-app doug-score
cd doug-score
yarn start
```

(Or `npm start`, whatever floats your boat but I'll be using yarn.)

Open up the folder in your editor of choice (VS Code for me) and head over to `App.js`. We’re going to create a separate component called `CarList` , putting it inside a `components` folder and adding it to `App` .

```js
import React, { Component } from "react";
import logo from "./logo.svg";
import "./App.css";
import CarList from "./components/CarList";
class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">Welcome to React</h1>
        </header>
        <CarList />
      </div>
    );
  }
}
export default App;
```

For now, this is what CarList component will look like:

```js
import React, { Component } from 'react';
class CarList extends Component {
  render() {
    return (
      <div>
        This will be the car list
      </div>
    );
  }
}
```

#### Google Sheets API

Let’s go ahead and [create a new project on Google](https://console.developers.google.com/projectcreate). I’ve called it `doug-score`. Once it’s been created, in the APIs box, click “Go to APIs overview.” Once you click “Enable APIs and Services” you’ll be presented with the API Library. We’ll go ahead and search for “Google Sheets API.” Once you click into it, click “Enable,” and after it’s processed you should see this page.

![Image](https://cdn-media-1.freecodecamp.org/images/XmCCcDJkZbQM7lLZLE1F6V25c2CwRtKvpEEt)
_Google APIs Dashboard_

In the sidebar, head over to “Credentials,” click the “Create credentials” button, and select “API Key.” Click the “Restrict Key” and set a name for it (I set it to “DougScore”). Under “Application Restrictions,” we’re going to set it to “HTTP referrers” and add `http://localhost:3000` for now. Under “API Restrictions” select the “Google Sheets API” and save. We should be good to go on this end.

#### The Connection

Now that we have an API key, head back over to the application code and create a new file called `config.js` . Input your API key and the spreadsheet ID into it.

```js
export default {
  apiKey: "YOUR_API_KEY",
  discoveryDocs: 
    ["https://sheets.googleapis.com/$discovery/rest?version=v4"],
  spreadsheetId: "1KTArYwDWrn52fnc7B12KvjRb6nmcEaU6gXYehWfsZSo"
};
```

Now, we’ll need the Google API library, so we’ll use our `index.html` file inside the `public` library after our `<div id="root">`</div>

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <!-- Stuff -->
  </head>
  <body>
    <noscript>
      You need to enable JavaScript to run this app.
    </noscript>
    <div id="root"></div>
    <script src="https://apis.google.com/js/api.js"></script>
    <!-- Stuff -->
  </body>
</html>
```

This will give us access to `window.gapi` which we’ll use to connect to the Sheets API. For more information on it, head over to [Google’s Docs](https://developers.google.com/sheets/api/quickstart/js).

### The Data

Now that we have access to the API, let’s establish the connection to it. The best place to do that would be inside the `componentDidMount` lifecycle of the `CarList` component we created earlier. Let’s head over there.

```js
componentDidMount() {
  // 1. Load the JavaScript client library.
  window.gapi.load("client", this.initClient);
}
```

`window.gapi.load` accepts a callback so our `initClient` function looks like this:

```js
initClient = () => {
  // 2. Initialize the JavaScript client library.
  window.gapi.client
    .init({
      apiKey: config.apiKey,
      // Your API key will be automatically added to the Discovery Document URLs.
      discoveryDocs: config.discoveryDocs
    })
    .then(() => {
    // 3. Initialize and make the API request.
    load(this.onLoad);
  });
};
```

A few things are introduced here. `config` is coming from the `config.js` file we created earlier, so don’t forget to do `import config from “../config”;` at the top of the `CarList.js` file.

`load` is a function that we’ll be creating now. It will be in charge of connecting to the right spreadsheet, formatting the data correctly, and returning it to the component within the `this.onLoad` callback (or returning an error if we messed something up).

I wanted to separate that logic from the component to keep the files small and fairly readable. Let’s create a new folder called `helpers` inside `src` and put a `spreadsheet.js` file in there.

```js
import config from "../config";
/**
 * Load the cars from the spreadsheet
 * Get the right values from it and assign.
 */
export function load(callback) {
  window.gapi.client.load("sheets", "v4", () => {
    window.gapi.client.sheets.spreadsheets.values
      .get({
        spreadsheetId: config.spreadsheetId,
        range: "Sheet1!A4:T"
      })
      .then(
        response => {
          const data = response.result.values;
const cars = data.map(car => ({
            year: car[0],
            make: car[1],
            model: car[2]
          })) || [];
callback({
            cars
          });
        },
        response => {
          callback(false, response.result.error);
        }
      );
  });
}
```

So here we’re invoking the sheets API and getting values from the spreadsheet by passing the `spreadsheetId` and the `range` . The promise returns two responses: one if there is data and one if there is an error. The response values are an array of arrays where each one is a row within the spreadsheet.

### The Display

Now that we have data back inside the `CarList` component, we can start setting up the display for it. Inside the `initClient` function, we had the `load(this.onLoad)` function, so let’s pick up there.

```js
onLoad = (data, error) => {
  if (data) {
    const cars = data.cars;
    this.setState({ cars });
  } else {
    this.setState({ error });
  }
};
```

If the `load` function within `spreadsheet.js` returns data, we set the `cars` state to that data. Otherwise we set an `error` state to show to our users that something went wrong.

#### Default state

Since data won’t be available instantly, we need to set up a default state for our component.

```js
state = {
  cars: [],
  error: null
}
```

#### Render

Now inside the `render` function we can display the state:

```js
render() {
  const { cars, error } = this.state;
  if (error) {
    return <div>{this.state.error}</div>;
  }
  return (
    <ul>
      {cars.map((car, i) => (
        <li key={i}>
          {car.year} {car.make} {car.model}
        </li>
      ))}
    </ul>
  );
}
```

Here we’re destructuring the state (ES6 FTW ??) and first checking if there is an error. If not, we’re mapping over the cars and displaying them in an unordered list.

![Image](https://cdn-media-1.freecodecamp.org/images/s4i4xPrmJ5iQs9yt7v2jNI4EcbTdZujHhtmb)

### Deployment

Now that we have our super beautiful list of cars Doug has reviewed, we can go ahead and share it with the world. Since it will be a static website, I am going to deploy it to [Netlify](https://blog.416serg.me/r/?url=https%3A%2F%2Fwww.netlify.com%2F) using their CLI. For that we’re going to stop our localhost and run the following commands:

```
yarn build
```

This will create a `build` folder within the application which will be production ready. Now all you have to do is:

```
npm install netlify-cli -g
netlify deploy
```

When it asks, make sure you put in `build` as the `Path to deploy? (current dir)` .

Netlify is going to do its thing and show you the final URL (mine is [https://laughing-yonath-118f58.netlify.com](https://laughing-yonath-118f58.netlify.com/) ?)

If you try to access the one you created, you’ll see an error in your console because your URL wasn’t added to the Google API console. Go ahead and add the URL you need, and after that everything should be working as expected.

### The End

I hope all of this made sense. You can now work your magic on adding features to that list such as sorting, filtering, pagination, search, comparison, and so on. And when Doug adds another car to that list, the app will be automatically updated with the new information.

If this tutorial made sense, give it a ?? and share it with a friend. If you want to tell me it sucked or you have any more questions, comment below or yell at me [on Twitter,](https://twitter.com/416serg) I really don’t mind. If Doug is reading this, hey Doug ??!

