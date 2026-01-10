---
title: React Components – How to Create a Search, Filter, and Pagination Component
  in React
subtitle: ''
author: Spruce Emmanuel
co_authors: []
series: null
date: '2022-06-07T23:37:17.000Z'
originalURL: https://freecodecamp.org/news/how-to-react-components
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/wirxeocmd6tpnn9c5oqc.jpg
tags:
- name: components
  slug: components
- name: React
  slug: react
seo_title: null
seo_desc: "I wrote the article \"How to Search and Filter Components in React\" exactly\
  \ one year ago.\nhttps://twitter.com/freeCodeCamp/status/1401192338073042954?s=20&t=LhPQBYEWz90YSd8lm_M6FA\n\
  \ \nSince then, a lot has changed. The API we used for the tutorial has s..."
---

I wrote the article "How to Search and Filter Components in React" exactly one year ago.

%[https://twitter.com/freeCodeCamp/status/1401192338073042954?s=20&t=LhPQBYEWz90YSd8lm_M6FA] 

Since then, a lot has changed. The API we used for the tutorial has stopped working, so in this article, we'll recreate our previous examples while also introducing pagination to our component.

This tutorial makes use of React.js, so you'll need a basic understanding of React and JavaScript to follow along. This tutorial also assumes that you've read the previous article, How to [Search and Filter Components in React](https://www.freecodecamp.org/news/search-and-filter-component-in-reactjs/).

## Getting Started

To get the country data for this tutorial, we will use the [CountryAPI](https://countryapi.io/) from CountryAPI.io.

We'll need an API key to use the API. To get your API key, go to [CountryAPI](https://countryapi.io/register) and create an account. Your API key should appear on your dashboard:

![Image](https://www.freecodecamp.org/news/content/images/2022/06/Web-capture_4-6-2022_184858_countryapi.io--1-.jpeg align="left")

Next we'll go create a new React app with [Create React App](https://create-react-app.dev/docs/getting-started/). To do that run the following in your terminal:

```js
# Run this to use npm
npx create-react-app search-app
# Or run this to use yarn
yarn create react-app search-app
cd my-app
npm start
# Or with yarn
yarn start
```

As usual, for live preview we are going to be using Codepen to display all our examples.

## How to Fetch the Data

To get our data, we must make a GET call to the [`https://countryapi.io/api/all`](https://countryapi.io/api/all) endpoint while supplying our API key. In the **src** &gt; **App.js** file of the React app that we created previously, delete all existing code and replace it with the following:

```js
import { useState, useEffect } from "react";
import "./App.css";

function App() {
  const [error, setError] = useState(null);
  const [loaded, setLoaded] = useState(false);
  const [items, setItems] = useState([]);
  
   useEffect(() => {
    const request_headers = new Headers();
    const api_key = "xxxxxxxxxxxxxxxxxxxxxxxxxxx";
    request_headers.append("Authorization", `Bearer ${api_key}`);
    request_headers.append("Content-Type", "application/json");

    const request_options = {
      method: "GET",
      headers: request_headers,
    };

    fetch("https://countryapi.io/api/all", request_options)
      .then((res) => res.json())
      .then(
        (result) => {
          setLoaded(true);
          setItems(result);
        },
        (error) => {
          setLoaded(true);
          setError(error);
        }
      );
  }, []);
  
  console.log(items)
  
  if (error) {
    return <>{error.message}</>;
  } else if (!loaded) {
    return <>loading...</>;
  } else {
     return (
     //
    );
  }
 }

export default App;
```

All we did above was use the JavaScript fetch API to make the GET request to our endpoint and then store the returned data in the `items` state using `setState(result)`.

### How to display the data

Next, we'll need to display the API data, which will be a list of all the countries returned by our API.

To make a list, we'll need to generate an array of objects from the values in our returned object. Open **src &gt; App.js** file and add the following code:

```js
import { useState, useEffect } from "react";
import "./App.css";

function App() {
  const [error, setError] = useState(null);
  const [loaded, setLoaded] = useState(false);
  const [items, setItems] = useState([]);

  useEffect(() => {
    // fetch data
  }, []);

  const data = Object.values(items);

  if (error) {
    return <>{error.message}</>;
  } else if (!loaded) {
    return <>loading...</>;
  } else {
    return (
      <div className="wrapper">
        <ul className="card-grid">
          {data.map((item) => (
            <li key={item.alpha3Code}>
              <article className="card">
                <div className="card-image">
                  <img src={item.flag.large} alt={item.name} />
                </div>
                <div className="card-content">
                  <h2 className="card-name">{item.name}</h2>
                  // other card content
              </article>
            </li>
          ))}
        </ul>
      </div>
    );
  }
}

export default App;
```

With some added CSS, the example above looks like the preview below:

%[https://codepen.io/Spruce_khalifa/pen/yLvqezJ?editors=0010] 

## How to Create the Search Component

First thing is to create an input field where users can enter their search query. Open **src** &gt; **App.js** and make the following edit:

```js
...

function App() {
 const [query, setQuery] = useState("");
 
  if (error) {
    return <>{error.message}</>;
  } else if (!loaded) {
    return <>loading...</>;
  } else {
    return (
      <div className="wrapper">
        <div className="search-wrapper">
          <label htmlFor="search-form">
            <input
              type="search"
              name="search-form"
              id="search-form"
              className="search-input"
              placeholder="Search for..."
              onChange={(e) => setQuery(e.target.value)}
            />
            <span className="sr-only">Search countries here</span>
          </label>
        </div>
        
        ...
      </div>
    );
  }
}

export default App;
```

Above we created an input field and, using the `onChange` event handler, anytime the value of the input field changes we set the value to `query` using the `useState` hook.

Next we'll need to use that `query` to filter the data returned from our API.

```js
const search_parameters = Object.keys(Object.assign({}, ...data));

 function search(data) {
    return items.filter(
      (item) =>
        search_parameters.some((parameter) =>
          item[parameter].toString().toLowerCase().includes(query)
        )
    );
  }
```

Let's break this down a bit. First we created a function `search()` which takes in our `data` as an argument. Combining the `Array.filter()` and `Array.some()` methods we checked if any of our Search Parameters include the value of our query `includes(query)`.

Of course we can hardcode our search parameters:

```js
const search_parameters = ["Capital", "Name", ...]
```

And while this is the fastest way, it is not future proof (data returned from an API may change) – I found this out the hard way. So instead of hardcoding we can get the search parameters from the `data` returned from the API.

```js
const search_parameters = Object.keys(Object.assign({}, ...data));
```

Lastly we need to use the new data returned from the `search(data)` function to build our country lists. Open the **App.js** file and edit the list we created earlier:

```js
...
{search(data).map((item) => (
 <li key={item.alpha3Code}>
  <article className="card">
   <div className="card-image">
    <img src={item.flag.large} alt={item.name} />
     </div>
   <div className="card-content">
    <h2 className="card-name">{item.name}</h2>
    ...           
   </div>
   </article>
 </li>
))}
```

With the search functionality added, the live preview now looks like this:

%[https://codepen.io/Spruce_khalifa/pen/vYdaBEq?editors=0010] 

## How to Create the Filter Component

A filter is often used to group data by a specific keyword. In this example, we want to group data by regions.

Again, instead of hardcoding this, we can get the regions from the data:

```js
const filter_items = [...new Set(data.map((item) => item.region))];
```

After the search input field we created, add the the filter UI – its an HTML `select` input field:

```js
...
const [filter, setFilter] = useState("");
...

<div className="select">
 <select
  onChange={(e) => setFilter(e.target.value)}
  className="custom-select"
  aria-label="Filter Countries By Region">
  <option value="">Filter By Region</option>
  {filter_items.map((item) => (
   <option value={item}>Filter By {item}</option>
  ))}
</select>
<span className="focus"></span>
</div>
```

To add the filter, we have to modify the `search(data)` function. So instead of returning only the data we searched for, we are now returning the data as our filter parameter:

```js
function search(items) {
    return items.filter(
      (item) =>
        item.region.includes(filter) &&
        search_parameters.some((parameter) =>
          item[parameter].toString().toLowerCase().includes(query)
        )
    );
  }
```

And there you have it – we can now filter our countries by region. The live preview and full code can be found on Codepen:

%[https://codepen.io/Spruce_khalifa/pen/ExQpYVp] 

## How to Create the Pagination Component

Pagination doesn't just reduce the lists of items displayed on a web page – it also increases the app's performance since users only have to download few resources when page is loading.

To create pagination for our countries data, we'll start by specifying the number of items we want to display in a `useState`:

```js
const [paginate, setpaginate] = useState(8);
```

Next let's use our `paginate` value to update our countries list:

```js
...
{search(data)
 .slice(0, paginate)
 .map((item) => (
 <li key={item.alpha3Code}>
  <article className="card">
   <div className="card-image">
    <img src={item.flag.large} alt={item.name} />
     </div>
   <div className="card-content">
    <h2 className="card-name">{item.name}</h2>
    ...           
   </div>
   </article>
 </li>
))}
```

Next we need to create a function where we update this state anytime we call it:

```js
const load_more = (event) => {
  setpaginate((prevValue) => prevValue + 8);
};
```

Lastly, let's create a button that will call the `load_more` function when clicked:

```js
<button onClick={load_more}>Load More</button>
```

Again the preview of the pagination can be found on CodePen:

%[https://codepen.io/Spruce_khalifa/pen/NWyBKxb] 

## Conclusion

In this article we looked at how to implement search, filter and pagination functionality in React by building a real world app using the [CountryAPI](https://countryapi.io/) from [CountryAPI.io](http://CountryAPI.io).

If you created something wonderful with this, please feel free to tweet about it and tag me [@sprucekhalifa](https://twitter.com/sprucekhalifa). And don't forget to hit the follow button.

Happy coding!
