---
title: Instant Search with Vanilla JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-06-25T02:14:28.000Z'
originalURL: https://freecodecamp.org/news/instant-search-with-vanilla-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2019/06/Week--15_-Instant-Search.png
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: instant search
  slug: instant-search
- name: JavaScript
  slug: javascript
- name: search
  slug: search
- name: WeeklyCodingChallenge
  slug: weeklycodingchallenge
seo_title: null
seo_desc: 'By Florin Pop

  Originally posted on www.florin-pop.com

  The theme for week #15 of the Weekly Coding Challenge is:

  Instant Search

  We live in a fast world and we want everything to be FAST, including search results,
  this is why instant search functionali...'
---

By Florin Pop

_Originally posted on [www.florin-pop.com](https://www.florin-pop.com/blog/2019/06/vanilla-javascript-instant-search/)_

The **theme** for week #15 of the [Weekly Coding Challenge](https://florin-pop.com/blog/2019/03/weekly-coding-challenge/) is:

## Instant Search

We live in a fast world and we want everything to be FAST, including search results, this is why instant search functionality became pretty much a "must have" feature instead of a "nice to have" feature.

In this article we're going to build this [feature](https://codepen.io/FlorinPop17/full/qzNxGa/), but only using Vanilla JavaScript :smiley:.

Below is the Live Preview of what we are going to build in this article. Let's search through the Countries of the world to see their Population and Flag:

%[https://codepen.io/FlorinPop17/pen/qzNxGa/]

**Note**: that you can use React, Vue, Angular or any other framework/library to create this functionality, although making it in Vanilla JavaScript is much more fun. ?

## The HTML

We'll need 2 things in our HTML:

1. A `search` field
2. A `results` div where we'll display the search results

```html
<input type="text" id="search" placeholder="Search for a Country" />
<div id="results"></div>
```

Usually we are going into the styling part next, but in this case considering that we don't yet have the entire markup (you'll see in a moment), we'll get to the JS part first. ?

## The JavaScript

Let's make a plan before we actually type any code. The things that we need to do are:

1. Gather a list of all the countries in the world
2. Display the list of countries
3. Update the results based on the search query

Pretty awesome, eh? ?

### Step one - getting the data

I found a nice API we can use to get the list of countries we need. It is: [RestCountries.eu](https://restcountries.eu/).

We're going to use the built in [Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API) in order to retrieve all the countries, and we're going to store them in a variable: `countries`.

```js
let countries;

const fetchCountries = async () => {
    countries = await fetch(
        'https://restcountries.eu/rest/v2/all?fields=name;population;flag'
    ).then(res => res.json());
};
```

As you can see, we created an async function; You can read more about this [here](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function).

Also, note that we only want 3 fields from the API (name, population and flag) so this is what we're going to get from the API by setting the `fields` query parameter.

### Step two - displaying the data

Now, we need to create the structure of our list in order to display the data and for that we're going to create all the elements that we need (`ul`, `li`, headings, etc) inside of a function and we'll insert them into the `results` div we declared in our HTML.

We're also going to call our `fetchCountries` function here because we want to loop over the countries in order to create the corresponding elements:

```js
const results = document.getElementById('results');

const showCountries = async () => {
    // getting the data
    await fetchCountries();

    const ul = document.createElement('ul');
    ul.classList.add('countries');

    countries.forEach(country => {
        // creating the structure
        const li = document.createElement('li');
        li.classList.add('country-item');

        const country_flag = document.createElement('img');
        // Setting the image source
        country_flag.src = country.flag;
        country_flag.classList.add('country-flag');

        const country_name = document.createElement('h3');
        country_name.innerText = country.name;
        country_name.classList.add('country-name');

        const country_info = document.createElement('div');
        country_info.classList.add('country-info');

        const country_population = document.createElement('h2');
        country_population.innerText = numberWithCommas(country.population);
        country_population.classList.add('country-population');

        const country_popupation_text = document.createElement('h5');
        country_popupation_text.innerText = 'Population';
        country_popupation_text.classList.add('country-population-text');

        country_info.appendChild(country_population);
        country_info.appendChild(country_popupation_text);

        li.appendChild(country_flag);
        li.appendChild(country_name);
        li.appendChild(country_info);

        ul.appendChild(li);
    });

    results.appendChild(ul);
};

// display initial countries
showCountries();

// From StackOverflow https://stackoverflow.com/questions/2901102/how-to-print-a-number-with-commas-as-thousands-separators-in-javascript
function numberWithCommas(x) {
    return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',');
}
```

There is a "little" bit of code above, so let's break it down. ?

First, we have our list (`ul`) with the `li`s that are created in the `forEach` loop.

All the `li`s have three children:

1. The flag - `img`
2. The name of the country heading - `h3`
3. A `div` which holds: (a) the `population` number - `h2` - and (b) The `'Population'` text - `h5`

We organized them in this manner because it'll be easier in the CSS to align everything using **flexbox**.

Alongside that, we added a `class` for each element because we want to style them individually in the CSS and then we used the `appendChild` to add these elements into the DOM at the end of the `forEach` function.

And lastly, we have a `numberWithComma` function from StackOverflow which will add a comma as a thousand separator for the `population` number.

### Step 3 - update the view based on the search query

In this final step we're going to get the search query from the `input` by attaching an `eventListener` on it, and we're going to modify our `showCountries` function so that it will `filter` out the values we don't want to be displayed. Let's see how we can do that:

```js
const search_input = document.getElementById('search');

let search_term = '';

search_input.addEventListener('input', e => {
    // saving the input value
    search_term = e.target.value;

    // re-displaying countries based on the new search_term
    showCountries();
});

const showCountries = async () => {
    // clear the results
    results.innerHTML = '';

    // see code above at Step 2.

    countries
        .filter(country =>
            country.name.toLowerCase().includes(search_term.toLowerCase())
        )
        .forEach(country => {
            // see code above at Step 2.
        });

    // see code above at Step 2.
};
```

As you can see we added two new things in the `showCountries` function:

1. We are clearing the previous `results` by setting the `innerHTML` to an empty string
2. We are filtering the `countries` by checking if the entered `search_term` is `included` in the `name` of the country, and we're also converting these two values `toLowerCase` as the user might type in upperCase letters and we still want to display the corresponding country

## The entire JS Code

Below you can find the entire JS code in case you want to copy it:

```js
const search_input = document.getElementById('search');
const results = document.getElementById('results');

let search_term = '';
let countries;

const fetchCountries = async () => {
    countries = await fetch(
        'https://restcountries.eu/rest/v2/all?fields=name;population;flag'
    ).then(res => res.json());
};

const showCountries = async () => {
    results.innerHTML = '';

    await fetchCountries();

    const ul = document.createElement('ul');
    ul.classList.add('countries');

    countries
        .filter(country =>
            country.name.toLowerCase().includes(search_term.toLowerCase())
        )
        .forEach(country => {
            const li = document.createElement('li');
            li.classList.add('country-item');

            const country_flag = document.createElement('img');
            country_flag.src = country.flag;
            country_flag.classList.add('country-flag');

            const country_name = document.createElement('h3');
            country_name.innerText = country.name;
            country_name.classList.add('country-name');

            const country_info = document.createElement('div');
            country_info.classList.add('country-info');

            const country_population = document.createElement('h2');
            country_population.innerText = numberWithCommas(country.population);
            country_population.classList.add('country-population');

            const country_popupation_text = document.createElement('h5');
            country_popupation_text.innerText = 'Population';
            country_popupation_text.classList.add('country-population-text');

            country_info.appendChild(country_population);
            country_info.appendChild(country_popupation_text);

            li.appendChild(country_flag);
            li.appendChild(country_name);
            li.appendChild(country_info);

            ul.appendChild(li);
        });

    results.appendChild(ul);
};

showCountries();

search_input.addEventListener('input', e => {
    search_term = e.target.value;
    showCountries();
});

// From StackOverflow https://stackoverflow.com/questions/2901102/how-to-print-a-number-with-commas-as-thousands-separators-in-javascript
function numberWithCommas(x) {
    return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',');
}
```

## The CSS

Finally, let's add some styling to our little app:

```css
@import url('https://fonts.googleapis.com/css?family=Roboto:300,500&display=swap');

* {
    box-sizing: border-box;
}

body {
    background-image: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    font-family: 'Roboto', sans-serif;

    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;

    min-height: 100vh;
}

.countries {
    padding: 0;
    list-style-type: none;
    width: 480px;
}

.country-item {
    background-color: #fff;
    border-radius: 3px;
    box-shadow: 0 2px 3px rgba(0, 0, 0, 0.3);
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 15px 10px;
    margin: 10px 0;
}

.country-item:hover {
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.4);
}

.country-flag {
    width: 40px;
}

.country-name {
    flex: 2;
    font-weight: normal;
    letter-spacing: 0.5px;
    margin: 0 5px;
    text-align: center;
}

.country-info {
    border-left: 1px solid #aaa;
    color: #777;
    padding: 0 15px;
    flex: 1;
}

.country-population {
    font-weight: 300;
    line-height: 24px;
    margin: 0;
    margin-bottom: 12px;
}

.country-population-text {
    font-weight: 300;
    letter-spacing: 1px;
    margin: 0;
    text-transform: uppercase;
}

input {
    font-family: 'Roboto', sans-serif;
    border-radius: 3px;
    border: 1px solid #ddd;
    padding: 15px;
    width: 480px;
}
```

Because it's nothing fancy I'm not going into details about the CSS, but if you have any questions regarding it feel free to contact me and I'll be happy to answer your questions! ?

## Conclusion

As mentioned above, this small app could probably be done much simpler with React, Vue or Angular, and you are free to do so if you want for your submission, but I wanted to play around with Vanilla JS and it was a fun experience for me! ?

As always, make sure you share what you're going to create!

Happy Coding! ?



