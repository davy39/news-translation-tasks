---
title: How to Add Search Functionality to a Frontend Application
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-01-04T16:28:58.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-search-to-frontend-app
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/pexels-ketut-subiyanto-4126712.jpg
tags:
- name: Front-end Development
  slug: front-end-development
- name: frontend
  slug: frontend
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: search
  slug: search
seo_title: null
seo_desc: "By Njoku Samson Ebere\nAs a software developer, part of your job is to\
  \ deliver the best user experience possible to those using your site or product.\
  \ \nAnd building a helpful and efficient search function is one way you can do this.\
  \ So if you are looki..."
---

By Njoku Samson Ebere

As a software developer, part of your job is to deliver the best user experience possible to those using your site or product. 

And building a helpful and efficient search function is one way you can do this. So if you are looking for the right way to build out search functionality on the front end of your site, you're in the right place. 

Some time ago, I thought that search functionality had to be built in the back end and called from the front end. 

But as I continued building applications, I learned that sometimes, you might just have to search among the data retrieved from a public endpoint where there is no _search_ endpoint. Other times, frontend search might be necessary to improve a website’s speed and user experience in general.

This tutorial will first go through the "wrong way" of setting up search which many of us have adopted. And then we'll learn a much better way of doing it. So stick with me and let me take you on this ride.

### Prerequisites 

It will be easy to follow this tutorial if you have basic knowledge of:

* [JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_is_JavaScript)
* [React](https://reactjs.org/)

## Starter Project

I have cooked up a little application to give you a head-start if you want to code along with me. Just clone [this repository](https://github.com/EBEREGIT/search-tutorial/tree/starter-code). The branch of interest is the **starter-code** branch. 

Follow the instructions in the [ReadMe](https://github.com/EBEREGIT/search-tutorial/blob/starter-code/README.md) file to setup the project and you should have the following screen:

![Image](https://www.freecodecamp.org/news/content/images/2021/12/Screenshot-2021-12-29-at-20.17.12.png)
_Starter Project Screen_

In the project you now have, we are fetching COVID-19 updates for every country in the ``src/context/hatchways.js`` file courtesy of [coronatracker](https://api.coronatracker.com/). 

In our ``src/App.js`` file, we display the results we have gotten. A *search* input box is situated above the list of results. For each of these result, the ``src/components/Country.js`` file is rendered.

As a user types into the input box, the ``filterCountryByName`` function is called to search through the countries we collected earlier. This function is being built in the ``src/Helpers/HatchHelper.js`` file.

All styles are in the ``src/styles/App.scss`` file.

You should now be able to navigate around the project and find your way. Let's begin with how you shouldn't build out your search functionality.


## How NOT to Build Search Functionality

We will focus on the `src/Helpers/HatchHelper.js` file to build out the search function.

Already we have the following code:

```javascript
// search countries by name
const filterCountryByName = (name, countries, setResults) => {
  // clear search result if the search field is empty
  if (name === "") {
    setResults([]);
  }

  // discontinue if there is no search yet
  if (name === null || name === "" || countries === []) return;
};
```

Next, we need to empty the previous search array so that we don't add the new search result to it. This is just in case we already made a search and want to do another.

```javascript
    // empty the previous search array if any
    const searchResult = [];
```

Convert the _search string_ to lower case for consistency's sake. This will make the search case insensitive.

```javascript
const data = name.toLowerCase();
```

Now, loop through the **countries** like so:

```javascript
  // loop through all countries
  for (const country of countries) {

  }
```

Next, collect each country name and make it lower case to ensure that the search will be case insensitive like so:

```javascript
    const countryName = country.countryName.toLowerCase();
```

Below that, check if the search string matches one character in the country name (`[...countryName].includes(data)`), one word in the country name (`countryName.split(" ").includes(data)`) or the full country name (`countryName === data`) and collect the country details like so:

```javascript
    // check if the search word or character matches
    if (
      [...countryName].includes(data) ||
      countryName === data ||
      countryName.split(" ").includes(data)
    ) {
      searchResult.push(country);
    }
```

When the loop is done, update the search Result with the following line of code:

```javascript
setResults(searchResult);
```

The `filterCountryByName` function now looks like this:

```javascript
// search countries by name
const filterCountryByName = (name, countries, setResults) => {
  // clear search result if the search field is empty
  if (name === "") {
    setResults([]);
  }

  // discontinue if there is no search yet
  if (name === null || name === "" || countries === []) return;

  // empty the previous search array if any
  const searchResult = [];
  const data = name.toLowerCase();

  // loop through all countries
  for (const country of countries) {
    const countryName = country.countryName.toLowerCase();

    // check if the search word or character matches
    if (
      [...countryName].includes(data) ||
      countryName === data ||
      countryName.split(" ").includes(data)
    ) {
      searchResult.push(country);
    }
  }

  setResults(searchResult);
};
```

Replace the **main** element in the `src/App.js` file with the following code to ensure proper feedback during search:

```html
<main>
    {filterByNameResults && filterByNameResults.length
    ? filterByNameResults.map((country) => (
    <Country country={country} />
    ))
    : filterByName && !filterByNameResults.length
    ? "No Result Found!"
    : hatchLoading === "processing"
    ? "Fetching Data..."
    : hatchLoading === "found" && hatches && hatches.length
    ? hatches.map((country) => <Country country={country} />)
    : "No country Found! Check your Internet Connection!"}
</main>
```

### How to Test Your Search Function

Let's now make a search and see what we get:

![Image](https://www.freecodecamp.org/news/content/images/2021/12/ezgif.com-gif-maker.gif)
_Testing How to Make Frontend Search the Wrong Way_

Here's the code for the [wrong way to code a search function](https://github.com/EBEREGIT/search-tutorial/tree/wrong-way).

### What is the problem with the search method above?

You will notice that the search string must satisfy at least one of the 3 conditions that we specified for a result to be returned. 

So how about a user who isn't sure of the spelling but knows a couple of characters contained in the country name? 

Do you notice that the user will take more time to search certain words because the words must me typed completely to get a match?

**Think about this**: ITA- should be able to return ITALY, NIG- should be able to return NIGER and NIGERIA, and so on.

So while our search works, these issues make it difficult to use and negatively impact the user experience. This now takes us to the right way to make this search functionality.

## How to Build a Search Feature the Right Way

We need to create another search just below the current one. 

Start by setting 2 initial states to hold the **search string** and the **search results** for this new search like so:

```javascript
  const [searchString, setSearchString] = useState("");
  const [searchResult, setSearchResult] = useState([]);
```

Next, make another input box just below the first one like so:

```javascript
          {/* search by name the right way*/}
          <input
            name="searchString"
            value={searchString}
            placeholder="Search by name (Right Way)"
            onChange={(e) => setSearchString(e.target.value)}
            onKeyUp={(e) =>
              searchCountryByName(
                e.target.value,
                hatches,
                setSearchResult
              )
            }
          />
```

Go to the `src/Helpers/HatchHelper.js` file and create the **`searchCountryByName`** function below the **`filterCountryByName`** function:

```javascript
// search countries by name the right way
const searchCountryByName = (
  searchString,
  countries,
  setSearchResult
) => {

};
```

Include it in the export like this:

```javascript
export { filterCountryByName, searchCountryByName };
```

You can now import it in the `src/App.js` file like so:

```javascript
import { filterCountryByName, searchCountryByName } from "./Helpers/HatchHelper";
```

You should now have a second input box that doesn’t do anything just yet:

![Image](https://www.freecodecamp.org/news/content/images/2021/12/Screenshot-2021-12-30-at-07.38.27.png)
_Screen showing a second input box that doesn’t do anything just yet_

#### Fleshing out the function 

We will now build out the function to work as we desire. 

Begin by adding the following lines of code:

```javascript
    // clear search result if the search field is empty
    if (searchString === "") {
      setSearchResult([]);
    }
  
    // discontinue if there is no search yet
    if (searchString === null || searchString === "" || countries === []) return;
```

Next, empty the previous search array if any like this:

```javascript
// empty the previous search array if any
  setSearchResult([]);
```

Then create a variable that will hold our search results while searching:

```javascript
let results = [];
```

Create a regular expression pattern for the search string like so:

```javascript
  // create a regular expression pattern for the search string
  const pattern = new RegExp(searchString, "gi");
```

> In the code above, we are saying that we want to use this **searchString** for something. While using it, we want it to be case-insensitive and we want all possible results. You can learn more about [regular expressions here](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp).

Now loop through countries and collect each country name like so:

```javascript
  // loop through all countries
  for (const country of countries) {
    const countryName = country.countryName;
 
  }
```

Still in the loop, test if the regular expression pattern matches the **`countryName`** that we just collected. If it is **true**, then add the country details to the **results** array like so:

```javascript
// check if the search word or character matches
if (pattern.test(countryName)) {
    results.push(country);
}
```

Finish by updating the search result using the following code:

```javascript
setSearchResult(results)
```

The `searchCountryByName` function now looks like this:

```javascript
// search countries by name the right way
const searchCountryByName = (
  searchString,
  countries,
  setSearchResult
) => {
  // clear search result if the search field is empty
  if (searchString === "") {
    setSearchResult([]);
  }

  // discontinue if there is no search yet
  if (searchString === null || searchString === "" || countries === []) return;

  // empty the previous search array if any
  setSearchResult([]);
  let results = [];

  // create a regular expression pattern for the search string
  const pattern = new RegExp(searchString, "gi");

  // loop through all countries
  for (const country of countries) {
    const countryName = country.countryName;

    // check if the search word or character matches
    if (pattern.test(countryName)) {
      results.push(country);
    }
  }

  setSearchResult(results)
};
```

Return to the `src/App.js` file and replace the main element with the following code:

```html
        <main>
          {filterByNameResults && filterByNameResults.length
            ? filterByNameResults.map((country) => (
                <Country country={country} />
              ))
            : filterByName && !filterByNameResults.length
            ? "No Result Found!"
            : searchResult && searchResult.length
            ? searchResult.map((country) => <Country country={country} />)
            : searchString && !searchResult.length
            ? "No Result Found!"
            : hatchLoading === "processing"
            ? "Fetching Data..."
            : hatchLoading === "found" && hatches && hatches.length
            ? hatches.map((country) => <Country country={country} />)
            : "No country Found! Check your Internet Connection!"}
        </main>
```

Now, the results for the second search box are included above.

### Testing your search function (the right way)

![Image](https://www.freecodecamp.org/news/content/images/2021/12/ezgif.com-gif-maker--1-.gif)
_Testing How to Make Frontend Search the Right Way_

Walah! You just learned the right way to create a search on the front end. 😊

Here's the code for the [right way to build a search function](https://github.com/EBEREGIT/search-tutorial/tree/right-way).

## How to Optimize Your Search Functionality

We are actually done. So you can skip this if you are busy, but it will just take a moment if you want to improve your search function.

You will notice that when you make a search the wrong way and do not refresh the page, you will be stuck with the results of the wrong way. It would be better to get fresh results when the second search box is used for the right way. 

To achieve that, we will need to clear all search results for every search being made – whether it is the **Wrong** or **Right** Way. Let's do the following:

In the `src/App.js`, replace the _onkey_ event of the first search box with the following_:_

```javascript
            onKeyUp={(e) =>
              filterCountryByName(
                e.target.value,
                hatches,
                setFilterByNameResults,
                setSearchString,
                setSearchResult
              )
            }
```

Replace the _onkey_ event of the second search box with the following_:_

```javascript
            onKeyUp={(e) =>
              searchCountryByName(
                e.target.value,
                hatches,
                setSearchResult,
                setFilterByName,
                setFilterByNameResults
              )
            }
```

In the `src/Helpers/HatchHelper.js` file, add the 2 parameters we just passed into the **`filterCountryByName`** like so:

```javascript
// search countries by name
const filterCountryByName = (
  name,
  countries,
  setResults,
  setSearchString,
  setSearchResult
) => {...}
```

Next, just before clearing the initial search results, clear the other search field and results like so:

```javascript
  // clear the other search field and results if any
  setSearchString("");
  setSearchResult([]);
```

Now do the same for the **`searchCountryByName`** function.

#### When you are done, you should have the following result:

![Image](https://www.freecodecamp.org/news/content/images/2021/12/ezgif.com-gif-maker--2--1.gif)
_Our application after we have optimised the functionality_

Awesome! 👍🏾👍🏾👍🏾

Here's the [optimisation code](https://github.com/EBEREGIT/search-tutorial/tree/optimization).

## Conclusion 

It has been an awesome ride with you as we saw the mistakes many of us have made and how to correct them by creating a search function that offers the best experience to the user.

I believe the code can be improved even more. So I encourage to take a look at the code again and see how you can make it even better.

All the code is [here](https://github.com/EBEREGIT/search-tutorial). Thanks for reading!


