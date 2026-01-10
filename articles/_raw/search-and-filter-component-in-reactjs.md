---
title: How to Search and Filter Components in React
subtitle: ''
author: Spruce Emmanuel
co_authors: []
series: null
date: '2021-06-04T21:34:33.000Z'
originalURL: https://freecodecamp.org/news/search-and-filter-component-in-reactjs
coverImage: https://www.freecodecamp.org/news/content/images/2021/05/wirxeocmd6tpnn9c5oqc.jpg
tags:
- name: create-react-app
  slug: create-react-app
- name: React
  slug: react
seo_title: null
seo_desc: 'If you''re building a React app, you want your users to be able to search
  and get exact results. And if you are getting tons of items from an API, then you
  need to create a way for users to be able to find various items easily.

  For this tutorial we ar...'
---

If you're building a React app, you want your users to be able to search and get exact results. And if you are getting tons of items from an API, then you need to create a way for users to be able to find various items easily.

For this tutorial we are going to be using one of [Frontend Mentor's free advanced API projects](https://www.frontendmentor.io/challenges/rest-countries-api-with-color-theme-switcher-5cacc469fec04111f7b848ca) as an example.

## Table Of Contents

1. Getting Started
    
2. How to Set Up React
    
3. How to Fetch the Data
    
4. How to Search for Items in the API
    
5. How to Filter Items Based on Region
    

# Getting Started

For this tutorial we will be using the free [REST COUNTRIES API](https://restcountries.eu/) provided by [Apilayer](https://apilayer.com/).

Basically we will fetch the data from our API endpoint `https://restcountries.eu/rest/v2/all` and display the data in a user readable form.

Then we'll provide a way for users to easily search for specific countries by their names and capitals.‌‌ Here is an example of the response for a particular country:

```json
[
  {
    "name": "Colombia",
    "topLevelDomain": [
      ".co"
    ],
    "alpha2Code": "CO",
    "alpha3Code": "COL",
    "callingCodes": [
      "57"
    ],
    "capital": "Bogotá",
    "altSpellings": [
      "CO",
      "Republic of Colombia",
      "República de Colombia"
    ],
    "region": "Americas",
    "subregion": "South America",
    "population": 48759958,
    "latlng": [
      4,
      -72
    ],
    "demonym": "Colombian",
    "area": 1141748,
    "gini": 55.9,
    "timezones": [
      "UTC-05:00"
    ],
    "borders": [
      "BRA",
      "ECU",
      "PAN",
      "PER",
      "VEN"
    ],
    "nativeName": "Colombia",
    "numericCode": "170",
    "currencies": [
      {
        "code": "COP",
        "name": "Colombian peso",
        "symbol": "$"
      }
    ],
    "languages": [
      {
        "iso639_1": "es",
        "iso639_2": "spa",
        "name": "Spanish",
        "nativeName": "Español"
      }
    ],
    "translations": {
      "de": "Kolumbien",
      "es": "Colombia",
      "fr": "Colombie",
      "ja": "コロンビア",
      "it": "Colombia",
      "br": "Colômbia",
      "pt": "Colômbia"
    },
    "flag": "https://restcountries.eu/data/col.svg",
    "regionalBlocs": [
      {
        "acronym": "PA",
        "name": "Pacific Alliance",
        "otherAcronyms": [],
        "otherNames": [
          "Alianza del Pacífico"
        ]
      },
      {
        "acronym": "USAN",
        "name": "Union of South American Nations",
        "otherAcronyms": [
          "UNASUR",
          "UNASUL",
          "UZAN"
        ],
        "otherNames": [
          "Unión de Naciones Suramericanas",
          "União de Nações Sul-Americanas",
          "Unie van Zuid-Amerikaanse Naties",
          "South American Union"
        ]
      }
    ],
    "cioc": "COL"
  }
]
```

‌‌By the end of this tutorial hopefully you will learn how to search through an API and return only the queried results with React.

# How to Set Up React

We'll use `create-react-app` to set up our project because it offers a modern build setup with no configuration at all.‌‌

To set up React, launch your terminal (either the one provided by your operating system or you can use an editor like VS Code) and run the following commands:

```bash
npx create-react-app my-app 
cd my-app 
npm start
```

If you are unsure how to properly setup a `create-react-app` project you can refer to the official guide here at [create-react-app-dev](https://create-react-app.dev/docs/getting-started/).‌‌

For our case and to display live results in this tutorial, we'll use [Codepen](https://codepen.io/) to setup our project. You can do this by using a Codepen template by [Lathryx](https://codepen.io/MrMaster):

%[https://codepen.io/MrMaster/pen/oNYWNjr] 

‌‌and there you have it – we have React set up in Codepen.

## How to Fetch the Data from Our API Endpoint

Now that we have successfully setup our React project, it is time to fetch the data from our API. There are many ways to fetch data in React, but the two most popular are **Axios** (a promise-based HTTP client) and the **Fetch API** (a browser in-built web API).‌‌

We’ll use the `Fetch API` provided by the browser and Ajax to fetch our data from our API Endpoint.‌‌ Here is an example using hooks from [Ajax and APIs by React](https://reactjs.org/docs/faq-ajax.html):

```js
function MyComponent() {
      const [error, setError] = useState(null);
      const [isLoaded, setIsLoaded] = useState(false);
      const [items, setItems] = useState([]);

      // Note: the empty deps array [] means
      // this useEffect will run once
      // similar to componentDidMount()
      useEffect(() => {
        fetch("https://api.example.com/items")
          .then(res => res.json())
          .then(
            (result) => {
              setIsLoaded(true);
              setItems(result);
            },
            // Note: it's important to handle errors here
            // instead of a catch() block so that we don't swallow
            // exceptions from actual bugs in components.
            (error) => {
              setIsLoaded(true);
              setError(error);
            }
          )
      }, [])

      if (error) {
        return <div>Error: {error.message}</div>;
      } else if (!isLoaded) {
        return <div>Loading...</div>;
      } else {
        return (
          <ul>
            {items.map(item => (
              <li key={item.id}>
                {item.name} {item.price}
              </li>
            ))}
          </ul>
        );
      }
    }
```

This fetches data from our endpoint in `line 10` and then uses `setState` to update our component when it gets the data.

From `line 27` we display an error message if getting data from our API fails. If it doesn't fail we display the data as a list.

If you are unfamiliar with React lists I suggest you take a look at this guide to [React Lists And Keys](https://reactjs.org/docs/lists-and-keys.html).

Now let's use this code to fetch and display data from our REST COUNTRIES API.

From the example code above, we want to `import useState from React` and then change `line 10` to:

`fetch("`[`https://restcountries.eu/rest/v2/all")`‌](https://restcountries.eu/rest/v2/all"\)‌)

When we put it all together we have:

```js
import { useState, useEffect } from "https://cdn.skypack.dev/react";

    // Note: the empty deps array [] means
    // this useEffect will run once
    function App() {
        const [error, setError] = useState(null);
        const [isLoaded, setIsLoaded] = useState(false);
        const [items, setItems] = useState([]);

        useEffect(() => {
            fetch("https://restcountries.eu/rest/v2/all")
                .then((res) => res.json())
                .then(
                    (result) => {
                        setIsLoaded(true);
                        setItems(result);
                    },
                    // Note: it's important to handle errors here
                    // instead of a catch() block so that we don't swallow
                    // exceptions from actual bugs in components.
                    (error) => {
                        setIsLoaded(true);
                        setError(error);
                    }
                );
        }, []);
```

**Note:** we are importing `useState` and `useEffect` from `"`[`https://cdn.skypack.dev/react`](https://cdn.skypack.dev/react)`";`. This is because we are using a CDN to import React in Codepen. If you set up React Locally then you should use `import { useState, useEffect } from "react";`.

Then we want to display our received data as a list of Countries. The final code to do this looks like this:

```js

    // Note: the empty deps array [] means
    // this useEffect will run once
    function App() {
        const [error, setError] = useState(null);
        const [isLoaded, setIsLoaded] = useState(false);
        const [items, setItems] = useState([]);

        useEffect(() => {
            fetch("https://restcountries.eu/rest/v2/all")
                .then((res) => res.json())
                .then(
                    (result) => {
                        setIsLoaded(true);
                        setItems(result);
                    },
                    // Note: it's important to handle errors here
                    // instead of a catch() block so that we don't swallow
                    // exceptions from actual bugs in components.
                    (error) => {
                        setIsLoaded(true);
                        setError(error);
                    }
                );
        }, []);

        if (error) {
            return <>{error.message}</>;
        } else if (!isLoaded) {
            return <>loading...</>;
        } else {
            return (
                /* here we map over the element and display each item as a card  */
                <div className="wrapper">
                    <ul className="card-grid">
                        {items.map((item) => (
                            <li>
                                <article className="card" key={item.callingCodes}>
                                    <div className="card-image">
                                        <img src={item.flag} alt={item.name} />
                                    </div>
                                    <div className="card-content">
                                        <h2 className="card-name">{item.name}</h2>
                                        <ol className="card-list">
                                            <li>
                                                population:{" "}
                                                <span>{item.population}</span>
                                            </li>
                                            <li>
                                                Region: <span>{item.region}</span>
                                            </li>
                                            <li>
                                                Capital: <span>{item.capital}</span>
                                            </li>
                                        </ol>
                                    </div>
                                </article>
                            </li>
                        ))}
                    </ul>
                </div>
            );
        }
    }

    ReactDOM.render(<App />, document.getElementById("root"));
```

Here is the live preview of this in Codepen:

%[https://codepen.io/Spruce_khalifa/pen/ZELeWoN] 

Now that we have successfully fetched and displayed the data from our REST COUNTRIES API, we can now concentrate on searching through the countries that are being displayed.

But before we do that let's style the above example with CSS (because it looks ugly when displayed like this).

When we add CSS to the above example we have something that looks like the example below:

%[https://codepen.io/Spruce_khalifa/pen/zYNZBBB] 

Though the CSS we've added is not perfect, it displays the countries in a neater way than the former, I hope you agree?

## How to Build the Search Component

Inside our APP function we use the `useState()` hooks to set the query `q` to an empty string. We also have the `setQ` which we’ll use to bind the value from our search form.‌‌

On `line 13` we use the `useState` to define an array of defaults value we want to be able to search from the API. This means that we want to be able to search any Country by its `Capital` and its `name` only. You can always make this array longer depending on your preference.

```js
        const [error, setError] = useState(null);
        const [isLoaded, setIsLoaded] = useState(false);
        const [items, setItems] = useState([]);

        //     set search query to empty string
        const [q, setQ] = useState("");
        //     set search parameters
        //     we only what to search countries by capital and name
        //     this list can be longer if you want
        //     you can search countries even by their population
        // just add it to this array
        const [searchParam] = useState(["capital", "name"]);

        useEffect(() => {
            // our fetch codes
        }, []);

     }
```

Inside our return function we'll create the search form and our code now looks like this:

```js
            return <>{error.message}</>;
        } else if (!isLoaded) {
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
                                value={q}
                                /*
                                // set the value of our useState q
                                //  anytime the user types in the search box
                                */
                                onChange={(e) => setQ(e.target.value)}
                            />
                            <span className="sr-only">Search countries here</span>
                        </label>
                    </div>
                    <ul className="card-grid">
                        {items.map((item) => (
                            <li>
                                <article className="card" key={item.callingCodes}>
                                    <div className="card-image">
                                        <img src={item.flag} alt={item.name} />
                                    </div>
                                    <div className="card-content">
                                        <h2 className="card-name">{item.name}</h2>
                                        <ol className="card-list">
                                            <li>
                                                population:{" "}
                                                <span>{item.population}</span>
                                            </li>
                                            <li>
                                                Region: <span>{item.region}</span>
                                            </li>
                                            <li>
                                                Capital: <span>{item.capital}</span>
                                            </li>
                                        </ol>
                                    </div>
                                </article>
                            </li>
                        ))}
                    </ul>
                </div>
            );
        }
    }

    ReactDOM.render(<App />, document.getElementById("root"));
```

Now we’ll create a function to handle our Search and place it above our return (the code above).

```js
            return items.filter((item) => {
                return searchParam.some((newItem) => {
                    return (
                        item[newItem]
                            .toString()
                            .toLowerCase()
                            .indexOf(q.toLowerCase()) > -1
                    );
                });
            });
        }
```

This function takes in our fetched items and returns all the items that match anything in our `searchParam` array if the `indexOF()` is `> -1`.

Now that the function is set up, to use it we'll wrap the returned data with our search function.

`{serach(items).map((item) => ( <li> // card goes here </li> ))}`‌

Now the data stored in our `useState()` is going to be filtered in our search function before it gets passed to the list items, thereby only returning items that match our query.

Here is the code when put together and the live preview on Codepen. Try using the search form below to search for any country by it’s name or capital.

%[https://codepen.io/Spruce_khalifa/pen/wvgJWdO?editors=0010] 

## How to Filter Countries by Region

Now we can take this further by filtering the countries by their region. Say we don't want to display all the countries, we just want to display and be able to search for countries only in `Africa` or `Asia`. You can achieve this by using the `useState()` hook in React.

### Regions:

1. Africa
    
2. America
    
3. Asia
    
4. Europe
    
5. Oceania
    

Now that we know our regions, let's create our filter component. First we set the `useState` of the filter like this:

`const [filterParam, setFilterParam] = useState(["All"]);`‌

Notice that we set the useState default to `ALL` on purpose, as we want to be able to display and search all countries if no region is specified.

```js
       <select
    /*
    // here we create a basic select input
    // we set the value to the selected value
    // and update the setFilterParam() state every time onChange is called
    */
      onChange={(e) => {
      setFilterParam(e.target.value);
       }}
       className="custom-select"
       aria-label="Filter Countries By Region">
        <option value="All">Filter By Region</option>
        <option value="Africa">Africa</option>
        <option value="Americas">America</option>
        <option value="Asia">Asia</option>
        <option value="Europe">Europe</option>
        <option value="Oceania">Oceania</option>
        </select>
        <span className="focus"></span>
        </div>
```

Now that we have created our filter, all that is left is to modify the `search function`. Basically we check the region entered and only return the countries that have that region:

```js
function search(items) {
       return items.filter((item) => {
    /*
    // in here we check if our region is equal to our c state
    // if it's equal to then only return the items that match
    // if not return All the countries
    */
       if (item.region == filterParam) {
           return searchParam.some((newItem) => {
             return (
               item[newItem]
                   .toString()
                   .toLowerCase()
                   .indexOf(q.toLowerCase()) > -1
                        );
                    });
                } else if (filterParam == "All") {
                    return searchParam.some((newItem) => {
                        return (
                            item[newItem]
                                .toString()
                                .toLowerCase()
                                .indexOf(q.toLowerCase()) > -1
                        );
                    });
                }
            });
        }
```

You can find the full code and live preview on Codepen. Try to filter the countries and watch the results.

%[https://codepen.io/Spruce_khalifa/pen/BapWzPe?editors=0010‌‌] 

Once we add some CSS we can now view the final preview of our React app.

%[https://codepen.io/Spruce_khalifa/pen/GRrWjmR?editors=0010] 

# Wrapping Up

When you're dealing with large set of data that you need to display to a user, search and filter functions help that user navigate and find important info quickly.

If you have any questions, you can get in touch with me and I'll be happy to chat.

You can find the full preview of this project here at [earthly vercel app](https://earthly.vercel.app). You can follow me on [Twitter @sprucekhalifa](https://twitter.com/sprucekhalifa).
