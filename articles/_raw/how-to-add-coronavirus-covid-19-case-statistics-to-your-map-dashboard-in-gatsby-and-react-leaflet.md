---
title: How to add Coronavirus (COVID-19) case statistics to your React map dashboard
  with Gatsby
subtitle: ''
author: Colby Fayock
co_authors: []
series: null
date: '2020-04-22T14:45:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-coronavirus-covid-19-case-statistics-to-your-map-dashboard-in-gatsby-and-react-leaflet
coverImage: https://www.freecodecamp.org/news/content/images/2020/04/coronavirus-mapping-app-2600x1000.jpg
tags:
- name: coronavirus
  slug: coronavirus
- name: Covid-19
  slug: covid-19
- name: data analytics
  slug: data-analytics
- name: front end
  slug: front-end
- name: Front-end Development
  slug: front-end-development
- name: frontend
  slug: frontend
- name: Gatsby
  slug: gatsby
- name: GatsbyJS
  slug: gatsbyjs
- name: JavaScript
  slug: javascript
- name: leaflet
  slug: leaflet
- name: Mapping
  slug: mapping
- name: maps
  slug: maps
- name: React
  slug: react
- name: react-leaflet
  slug: react-leaflet
- name: React
  slug: reactjs
seo_title: null
seo_desc: 'Previously, we walked through creating a map that shows an interactive
  look at Coronavirus (COVID-19) cases per country. How can we extend this with some
  case statistics to show recent data about the impacts on our world?

  Author''s note: Similar to be...'
---

Previously, we walked through creating a map that shows an interactive look at Coronavirus (COVID-19) cases per country. How can we extend this with some case statistics to show recent data about the impacts on our world?

_Author's note: Similar to before, this dashboard is meant to be a demo and proof of concept for using real world data to build a dashboard. While this data should be accurate per the NovelCOVID API, I would recommend using tools like the [Johns Hopkins University dashboard](https://www.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6) for complete and accurate analysis. Stay home and be safe! ❤️_

* [What are we going to build?](#heading-what-are-we-going-to-build)
* [What do we need before we get started?](#heading-what-do-we-need-before-we-get-started)
* [Step 1: Update how we fetch our data and fetch the statistics](#heading-step-1-update-how-we-fetch-our-data-and-fetch-the-statistics)
* [Step 2: Adding statistics to our dashboard](#heading-step-2-adding-statistics-to-our-dashboard)
* [Step 3: Make the data human friendly](#heading-step-3-make-the-data-human-friendly)
* [Step 4: Add the Last Updated date](#heading-step-4-add-the-last-updated-date)
* [What can I do next?](#heading-what-can-i-do-next)

%[https://www.youtube.com/watch?v=9bfxeod27fU]

## What are we going to build?

We're going to be extending our [original map demo](https://www.colbyfayock.com/2020/03/how-to-create-a-coronavirus-covid-19-dashboard-map-app-with-gatsby-and-leaflet) with some basic statistics that we can retrieve from the [NovelCOVID API](https://github.com/NovelCOVID/API). To get an idea, here's [my demo](https://coronavirus-map-dashboard.netlify.app/) I'm basing this off of.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/coronavirus-covid-19-dashboard-map-stats.jpg)
_Coronavirus (COVID-19) map demo with dashboard statistics_

While you're not required to have completed [Part 1](https://www.colbyfayock.com/2020/03/how-to-create-a-coronavirus-covid-19-dashboard-map-app-with-gatsby-and-leaflet/) to apply these concepts, it definitely helps, and it lets you set up a map for your dashboard. If you'd like to start there, which I recommend, check out [How to create a Coronavirus (COVID-19) Dashboard & Map App with Gatsby and Leaflet](https://www.colbyfayock.com/2020/03/how-to-create-a-coronavirus-covid-19-dashboard-map-app-with-gatsby-and-leaflet/) first.

## Woah, a mapping app?

Yup. If you haven't played with maps before, don't be discouraged! It's not as bad as you probably think. If you'd rather start with mapping basics, you can  [read more about how mapping works](https://www.freecodecamp.org/news/easily-spin-up-a-mapping-app-in-react-with-leaflet/)  first.

## What do we need before we get started?

For this walkthrough, you pretty much need a React app in some form. I'll be working with the dashboard we previously built in my last walkthrough that includes a [map of the cases of the Coronavirus (COVID-19) per country](https://www.colbyfayock.com/2020/03/how-to-create-a-coronavirus-covid-19-dashboard-map-app-with-gatsby-and-leaflet/).

![Image](https://www.freecodecamp.org/news/content/images/2020/04/coronavirus-map-tutorial-country-markers.jpg)
_Coronavirus (COVID-19) map dashboard_

I recommend starting with the previous tutorial, but if you want to skip the map and start fresh, the easiest way would probably be to use [Create React App](https://github.com/facebook/create-react-app), [Gatsby](https://www.gatsbyjs.org/), or [Next.js](https://nextjs.org/).

## Step 1: Update how we fetch our data and fetch the statistics

To get started with our statistics dashboard, we're going to do a little prep work by changing how we're fetching the data. The goal here, is we're going to wrap our request logic in a reusable way so that we can use it for both our countries data and our new statistics data.

### Creating a new React hook to fetch data

Diving in, the first we'll do is create a new [React hook](https://reactjs.org/docs/hooks-reference.html) that will serve as how we fetch the data. To get started, create a new file in your hooks directory called `useTracker.js`  and add a line inside of `hooks/index.js` to export it:

```js
// New file src/hooks/useTracker.js
// This will be empty for now
```

```js
// Inside hooks/index.js
export { default as useTracker } from './useTracker';

```

Inside of our `useTracker.js` file, we're going to set up our request logic. This is a long file, so make sure you copy and paste the entire thing before we walk through what it does:

```js
import { useEffect, useState } from 'react';
import axios from 'axios';

const API_HOST = 'https://corona.lmao.ninja/v2';

const ENDPOINTS = [
  {
    id: 'all',
    path: '/all',
    isDefault: true
  },
  {
    id: 'countries',
    path: '/countries'
  }
]

const defaultState = {
  data: null,
  state: 'ready'
}

const useTracker = ({ api = 'all' }) => {

  const [tracker = {}, updateTracker] = useState(defaultState)

  async function fetchTracker() {
    let route = ENDPOINTS.find(({ id } = {}) => id === api);

    if ( !route ) {
      route = ENDPOINTS.find(({ isDefault } = {}) => !!isDefault);
    }

    let response;

    try {
      updateTracker((prev) => {
        return {
          ...prev,
          state: 'loading'
        }
      });
      response = await axios.get(`${API_HOST}${route.path}`);
    } catch(e) {
      updateTracker((prev) => {
        return {
          ...prev,
          state: 'error',
          error: e
        }
      });
      return;
    }

    const { data } = response;

    updateTracker((prev) => {
      return {
        ...prev,
        state: 'ready',
        data
      }
    });

  }

  useEffect(() => {
    fetchTracker()
  }, [api])

  return {
    fetchTracker,
    ...tracker
  }
};

export default useTracker;


```

Starting from the top:

* We import our dependencies: we're going to use Reacts `useEffect`  and `useState` hooks to manage our requests
* We define default constants: we have a base API endpoint for our data, a list of the available endpoints we'll use, and a state object that will store our data
* We define our `useTracker` hook:  our hook includes one argument `api`  that will allow us to specify which endpoint we'll use to make our request
* We set up a state instance: we'll want to keep track of our fetched data, so we create a `tracker` state instance that we'll be able to update
* We created an asynchronous `fetchTracker` function: we'll use this to make our actual request
* Inside our function: we first find the API route and create our URL, update our state instance to a "loading" state, try to make our request, catch any errors if there are any, and finally if the request is successful, we update our state with that data
* We trigger our function: using a `useEffect` hook, we trigger our `fetchTracker` function to make the request. We only have one dependency of `api`. This means the function will only fire the first time and any time the `api` value we pass in changes. We won't be changing that value, but it may be helpful in other instances if you're dynamically changing the API used
* We return our tracker: the returned object includes both our `tracker` data as well as our `fetchTracker` function that we could use to refetch the data if we'd like

And with all of that, we have a brand new hook that will fetch data from the NovelCOVID API.

### Using our new tracker hook

To make use of this hook, let's jump over to `src/pages/index.js`, remove our `axios` import if it's there, and instead import our hook:

```js
import { useTracker } from 'hooks';

```

With our hook, let's replace our original country data request.  First, add the following to the top of the `IndexPage` component:

```js
const { data: countries = [] } = useTracker({
  api: 'countries'
});

const hasCountries = Array.isArray(countries) && countries.length > 0;

```

This will let us fetch our country data and let us know if we have any results. Next, let's replace our original request.

Inside of our `mapEffect` function, let's remove the `axios` request in addition to the response, the destructured data object, and the `hasData` constant.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/code-diff-map-effect-countries-data.jpg)
_Code diff showing update to map effect_

Then, replace `hasData` with `hasCountries`:

```js
if ( !hasCountries ) return;

```

And replace `data` with `countries` in the `geoJson` object where we map our features:

```js
features: countries.map((country = {}) => {

```

At this point, if you hit save and refresh, you shouldn't notice any difference to what you previously had.

### Add a request for our stats

Now that we are using our `useTracker` hook to fetch our country data, let's also use that to fetch our stats.

Right next to where we set up our `useTracker` hook before, let's add another request:

```js
const { data: stats = {} } = useTracker({
  api: 'all'
});

```

And if we add a `console.log` statement under to see what's inside `stats`:

```js
console.log('stats', stats);

```

We should see our `stats` data object logged out!

![Image](https://www.freecodecamp.org/news/content/images/2020/04/console-log-coronavirus-stats-1.jpg)
_Using console.log to show Coronavirus (COVID-19) statistics_

[Follow along with the commit!](https://github.com/colbyfayock/my-coronavirus-map/commit/fe9d85e57f7474a86d38213676bf62df4b6168a4)

## Step 2: Adding statistics to our dashboard

Now that we have our data available to use, let's use it!

To get started adding our statistics to the dashboard, let's create a data structure that will allow us to easily configure the data we want to use.

To do this, let's first create a new array called `dashboardStats` below `hasCountries` at the top of the page component:

```js
const dashboardStats = [];

```

Inside this array, let's add some new objects that specify our data that we're pulling from the `stats` object we requested. To start, let's try to add:

```js
const dashboardStats = [
  {
    primary: {
      label: 'Total Cases',
      value: stats?.cases
    },
    secondary: {
      label: 'Per 1 Million',
      value: stats?.casesPerOneMillion
    }
  },
  {
    primary: {
      label: 'Total Deaths',
      value: stats?.deaths
    },
    secondary: {
      label: 'Per 1 Million',
      value: stats?.deathsPerOneMillion
    }
  },
  {
    primary: {
      label: 'Total Tests',
      value: stats?.tests
    },
    secondary: {
      label: 'Per 1 Million',
      value: stats?.testsPerOneMillion
    }
  }
]

```

The reason we're splitting this up into `primary` and `secondary` keys, is we're going to use that to differentiate between logically similar stats that we want to style a little bit differently.

_Note: if you're not familiar with the `?.` syntax, it's called [Optional Chaining](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Optional_chaining). This allows us to chain our properties without worrying about if the objects exist. If `stats` is undefined, it will simply return undefined instead of throwing an error._

With our stats data, let's add the tracker to our map. Let's remove our current `<Map>` component and include it nested inside our tracker div in the following:

```jsx
<div className="tracker">
  <Map {...mapSettings} />
  <div className="tracker-stats">
    <ul>
      { dashboardStats.map(({ primary = {}, secondary = {} }, i) => {
        return (
          <li key={`Stat-${i}`} className="tracker-stat">
            { primary.value && (
              <p className="tracker-stat-primary">
                { primary.value }
                <strong>{ primary.label }</strong>
              </p>
            )}
            { secondary.value && (
              <p className="tracker-stat-secondary">
                { secondary.value }
                <strong>{ secondary.label }</strong>
              </p>
            )}
          </li>
        );
      })}
    </ul>
  </div>
</div>

```

This code should be immediately following the `<Helmet>` component if you're following along.

To explain what we're doing:

* We're creating a "tracker" div that will organize our stats
* We move our `<Map` component inside of this tracker
* We create a separate section called "tracker-stats"
* Inside of this, we create an unordered list (`ul`)
* Inside of our list, we loop through all of our stats inside `dashboardStats`
* For each stat, we create a new list element (`li`) and include 2 optional paragraphs that includes our primary stat data and our secondary stat data

Once we reload our page, we should now see a few stats:

![Image](https://www.freecodecamp.org/news/content/images/2020/04/adding-coronavirus-stats-to-page.jpg)
_Adding the first statistics to the page_

Now that we have our stats on our page, let's make them look like they're in a dashboard.

Let's create a new file called `_tracker.scss` inside of our `src/assets/stylesheets/components` directory. Once that file is created, additionally add it to the `src/assets/stylesheets/components/__components.scss` file:

```scss
@import "tracker";

```

With our new component style file ready to go, let's add some styles into `_tracker.scss`:

```scss
.tracker-stats {

  color: white;
  background-color: $blue-grey-900;
  border-top: solid 1px darken($blue-grey-900, 5);

  ul {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    list-style: none;
    padding: 0;
    margin: 0;
  }

}

.tracker-stat {

  font-size: 2em;
  text-align: center;
  padding: .5em;
  border-right: solid 1px darken($blue-grey-900, 5);
  border-bottom: solid 1px darken($blue-grey-900, 5);

  strong {
    font-weight: normal;
    color: $blue-grey-300;
  }

}

.tracker-stat-primary {

  margin: 0;

  strong {
    display: block;
    font-size: .5em;
  }

}

.tracker-stat-secondary {

  font-size: .5em;
  margin: .8em 0 0;

  strong {
    font-size: .8em;
    margin-left: .4em;
  }

}

```

Above – we're adding colors and organizational effects, such as using [CSS Grid](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Grid_Layout), to allow our data to be organized in an easy to read way and to look good! We're also making use of some pre-existing colors variables that are used within the project to keep the color use consistent.

Once you save those styles and reload the page, it should look much better:

![Image](https://www.freecodecamp.org/news/content/images/2020/04/adding-coronavirus-case-statistics-to-map-dashboard.jpg)
_Adding case statistics to the dashboard_

From here, feel free to add more stats or adjust them to your liking. In the demo I created, I added the stats for active cases, critical cases, and recovered cases. If you'd like to do the same, you can [check out the commit](https://github.com/colbyfayock/my-coronavirus-map/commit/eb8a28c9e46dc2327ada0df21b250422e55d304c).

[Follow along with the commit!](https://github.com/colbyfayock/my-coronavirus-map/commit/eb8a28c9e46dc2327ada0df21b250422e55d304c)

## Step 3: Make the data human friendly

Now the rest of this walkthrough could be considered optional, but ultimately we want people to be able to read these statistics, right? So let's make the numbers a little more easy to read.

First, let's open our `src/lib/util.js` file and add this function:

```js
/**
 * commafy
 * @description Applies appropriate commas to large numbers
 */

export function commafy(value) {
  let numberString = `${value}`;

  numberString = numberString.split('');

  numberString.reverse();

  numberString = numberString.reduce((prev, current, index) => {
    const shouldComma = (index + 1) % 3 === 0 && index + 1 < numberString.length;
    let updatedValue = `${prev}${current}`;
    if ( shouldComma ) {
      updatedValue = `${updatedValue},`;
    }
    return updatedValue;
  }, '');

  numberString = numberString.split('');
  numberString.reverse()
  numberString = numberString.join('');

  return numberString;
}

```

This function will take a number and turn it into a string with commas. To walk through what it does:

* Takes in a value as an argument. For our use, this value will most likely be a number.
* It converts the value into a string. We'll use this to work with adding commas to our number.
* We split that string into an array and reverse it. We want to reverse it because it makes it easier to add our commas depending on the index.
* We use the javascript `reduce` function to recreate our number-string. After every 3 numbers, we want to add a comma.
* Once we have our new value with the commas, we want to re-reverse it. So we split it again, reverse the array of characters, and re-join it, which is what we return

And now that we have our `commafy` function, let's use it. Back inside `src/pages/index.js`, let's import our function at the top of the page:

```js
import { commafy } from 'lib/util';

```

Then, in our `dashboardStats` array, let's replace every number value with a ternary expression and function that will convert our number if it's available:

```js
value: stats ? commafy(stats?.cases) : '-'

```

This line checks to see if `stats` exists. If it does, we `commafy` the `cases` value. If it doesn't exist, we return a `-` to show it's unavailable.

Once we repeat that process for all of our numbers, we can save, reload the page, and see our human friendly numbers!

![Image](https://www.freecodecamp.org/news/content/images/2020/04/coronavirus-dashboard-stats-with-readable-stats.jpg)
_Formatting the statistics to be human readable_

[Follow along with the commit!](https://github.com/colbyfayock/my-coronavirus-map/commit/90f266c17815239d9d3356d9b9d660915fdc26c2)

## Step 4: Add the Last Updated date

Finally, we want to make sure people are staying informed and understand the last time this data was updated. Luckily, our API provides a Last Updated date for us, so let's use it!

At the bottom of our "tracker" `div` under `tracker-stats`, let's add the following:

```jsx
<div className="tracker-last-updated">
  <p>
    Last Updated: { stats?.updated }
  </p>
</div>

```

This creates a new section where we simply include the `updated` property from our stats. And if we save and reload the page, we can see the last updated date!

![Image](https://www.freecodecamp.org/news/content/images/2020/04/coronvirus-dashboard-last-updated.jpg)
_Adding last updated to the dashboard_

But how could we even understand what that number is, unless you're the computer crawling this blog post? So let's change it to a human readable format like we did with our numbers.

Inside of our `src/lib/util.js` file, let's add another function:

```js
/**
 * friendlyDate
 * @description Takes in a date value and returns a friendly version
 */

export function friendlyDate(value) {
  const date = new Date(value);
  return new Intl.DateTimeFormat('en', {
    year: 'numeric',
    month: 'short',
    day: '2-digit',
    hour: 'numeric',
    minute: 'numeric'
  }).format(date);
}

```

This function creates a new `Date` object, then uses the javascript [International DateTimeFormat API](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DateTimeFormat) to convert it into a friendly readable format!

Once that's saved, let's import it next to our `commafy` function at the top of `src/pages/index.js`:

```js
import { commafy, friendlyDate } from 'lib/util';

```

Then we can update our code similar to how we updated our numbers:

```jsx
Last Updated: { stats ? friendlyDate(stats?.updated) : '-' }

```

And if we save and reload, we see it in a human readable way!

![Image](https://www.freecodecamp.org/news/content/images/2020/04/coronvirus-dashboard-last-updated-formatted-1.jpg)
_Formatting the last updated date_

Finally for our "last updated" should look like it fits in with the rest of the dashboard, so let's add a few more styles. Inside of our `_tracker.scss` file we were working with earlier:

```scss
.tracker-last-updated {

  color: white;
  background-color: $blue-grey-900;
  padding: .8em 0;

  p {
    color: $blue-grey-300;
    font-size: .8em;
    text-align: center;
    margin: 0;
  }

}

```

And once we hit save and refresh the browser, we have our dashboard statistics with the last updated time! ?

![Image](https://www.freecodecamp.org/news/content/images/2020/04/coronavirus-dashboard-formatted-styled.jpg)
_Final dashboard with formatted lasted updated date_

[Follow along with the commit!](https://github.com/colbyfayock/my-coronavirus-map/commit/408286aecb32223c8782eb1539f5563135c75dfb)

## What can I do next?

### Make the marker tooltip data human friendly

Now that we have our handy `commafy` and `friendlyDate` functions, we can reuse those functions to clean up the data in our country marker popups!

### Use the fetchTracker function to poll for updates

Inside of the `useTracker` hook we created, we exported a function called `fetchTracker`. This allows us to force a request to the API to fetch new data. To make sure our map stays current even when somebody doesn't refresh the page, we can create a [timer](https://developer.mozilla.org/en-US/docs/Web/API/WindowOrWorkerGlobalScope/setTimeout) in javascript to regularly invoke that function to update our dashboard data.

### Clear the map layers before re-adding the new ones

One thing we're currently not doing is cleaning up old layers before adding a new one. The way the map is set up, it just keeps layering them on top. What we can do is before we add all of our new layers, we can clear out the old ones. [Check out this commit](https://github.com/colbyfayock/my-coronavirus-map/commit/cad3b5a6e31a6ae090549c12e40a08fee4db4aa5) to get started!

## Want to learn more about maps?

You can check out a few of my other resources to get started:

* [How to create a Coronavirus (COVID-19) Dashboard & Map App in React with Gatsby and Leaflet](https://www.colbyfayock.com/2020/03/how-to-create-a-coronavirus-covid-19-dashboard-map-app-with-gatsby-and-leaflet) (Part 1 of this post)
* [How to set up a custom Mapbox basemap style with React Leaflet and Leaflet Gatsby Starter](https://www.colbyfayock.com/2020/04/how-to-set-up-a-custom-mapbox-basemap-style-with-react-leaflet-and-leaflet-gatsby-starter/)
* [Anyone Can Map! Inspiration and an introduction to the world of mapping](https://www.colbyfayock.com/2020/03/anyone-can-map-inspiration-and-an-introduction-to-the-world-of-mapping)
* [How to Create a Summer Road Trip Mapping App with Gatsby and Leaflet](https://www.colbyfayock.com/2020/03/how-to-create-a-summer-road-trip-mapping-app-with-gatsby-and-leaflet)
* [How to Create your own Santa Tracker with Gatsby and React Leaflet](https://www.colbyfayock.com/2019/12/create-your-own-santa-tracker-with-gatsby-and-react-leaflet/)
* [How to build a mapping app in React the easy way with Leaflet](https://www.freecodecamp.org/news/easily-spin-up-a-mapping-app-in-react-with-leaflet/)

<div id="colbyfayock-author-card">
  <p style="margin: 0;">
    <a href="https://twitter.com/colbyfayock" style="display: block;">
      <img src="https://res.cloudinary.com/fay/image/upload/w_2000,h_400,c_fill,q_auto,f_auto/w_1020,c_fit,co_rgb:007079,g_north_west,x_635,y_70,l_text:Source%20Sans%20Pro_64_line_spacing_-10_bold:Colby%20Fayock/w_1020,c_fit,co_rgb:383f43,g_west,x_635,y_6,l_text:Source%20Sans%20Pro_44_line_spacing_0_normal:Follow%20me%20for%20more%20JavaScript%252c%20UX%252c%20and%20other%20interesting%20things!/w_1020,c_fit,co_rgb:007079,g_south_west,x_635,y_70,l_text:Source%20Sans%20Pro_40_line_spacing_-10_semibold:colbyfayock.com/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_68,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_145,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_222,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_295,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/v1/social-footer-card" alt="Follow me for more Javascript, UX, and other interesting things!" style="width:100%;display: block;margin: 0;">
    </a>
  </p>
  <ul style="display:flex;justify-content:center;list-style:none;padding:0;margin: .5em 0 0;font-size: .8em;">
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://twitter.com/colbyfayock" style="text-decoration: none;">? Follow Me On Twitter</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://youtube.com/colbyfayock" style="text-decoration: none;">?️ Subscribe To My Youtube</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://www.colbyfayock.com/newsletter/" style="text-decoration: none;">✉️ Sign Up For My Newsletter</a>
    </li>
  </ul>
</div>

