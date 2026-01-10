---
title: How to Create a Travel Bucket List Map with Gatsby, React Leaflet, & Hygraph
subtitle: ''
author: Colby Fayock
co_authors: []
series: null
date: '2020-06-23T14:45:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-travel-bucket-list-map-with-gatsby-react-leaflet-graphcms
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/travel-bucket-list.jpg
tags:
- name: beginners guide
  slug: beginners-guide
- name: cms
  slug: cms
- name: Gatsby
  slug: gatsby
- name: GatsbyJS
  slug: gatsbyjs
- name: graphcms
  slug: graphcms
- name: headless cms
  slug: headless-cms
- name: JavaScript
  slug: javascript
- name: leaflet
  slug: leaflet
- name: Mapping
  slug: mapping
- name: maps
  slug: maps
- name: react-leaflet
  slug: react-leaflet
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Travel
  slug: travel
- name: Tutorial
  slug: tutorial
seo_title: null
seo_desc: Traveling is fun and we all have a lot of places we want to visit, but rarely
  do we have time to do it all at once. That’s what bucket lists are for! How can
  we create a custom mapping app that we can show all of our the destinations on our
  bucket li...
---

Traveling is fun and we all have a lot of places we want to visit, but rarely do we have time to do it all at once. That’s what bucket lists are for! How can we create a custom mapping app that we can show all of our the destinations on our bucket list?

Note: As of July 2022, GraphCMS is now [Hygraph](https://hygraph.com/).

* [What are we going to build?](#heading-what-are-we-going-to-build)
* [Step 1: Creating a new app with Gatsby Starter Leaflet](#heading-step-1-creating-a-new-app-with-gatsby-starter-leaflet)
* [Step 2: Creating and managing a list of travel locations with GraphCMS](#heading-step-2-creating-and-managing-a-list-of-travel-locations-with-graphcms)
* [Step 3: Querying our GraphCMS location data with Gatsby and GraphQL](#heading-step-3-querying-our-graphcms-location-data-with-gatsby-and-graphql)
* [Step 4: Creating a bucket list of destinations and adding them to the map](#heading-step-4-creating-a-bucket-list-of-destinations-and-adding-them-to-the-map)
* [What else other features can we add to our app?](#heading-what-else-other-features-can-we-add-to-our-app)
* [Want to learn more about maps?](#heading-want-to-learn-more-about-maps)

%[https://www.youtube.com/watch?v=isbr52VKjb0]

## What are we going to build?

We’re going to build a mapping app with [Gatsby](https://www.gatsbyjs.org/) managed by a CMS that will both display markers on a map and show our locations in a simple text-based list for our bucket list locations.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/travel-bucket-list-demo.jpg)
_Demo of a Travel Bucket List mapping app_

We’ll spin up the app with a [Gatsby Starter for Leaflet](https://github.com/colbyfayock/gatsby-starter-leaflet) and then we’ll use [GraphCMS](https://graphcms.com/) to create and manage the list of locations for our map!

## Woah, a mapping app?

Yup. If you haven't played with maps before, don't be discouraged! It's not as bad as you probably think. If you'd rather start with mapping basics, you can  [read more about how mapping works](https://www.freecodecamp.org/news/easily-spin-up-a-mapping-app-in-react-with-leaflet/)  first.

## Step 1: Creating a new app with Gatsby Starter Leaflet

We’ll start off with Gatsby Starter Leaflet. This is going to give us a basic React application with our mapping tools already built in.

### Creating a new Gatsby app with Gatsby Starter Leaflet

To get started, navigate to where you want to create your new app and run:

```shell
gatsby new my-travel-bucket-list https://github.com/colbyfayock/gatsby-starter-leaflet

```

_Note: you can replace `my-travel-bucket-list` with whatever you want. This will be used to create the new folder for the app._

Once you run that, Gatsby will pull down the Starter and install the dependencies. After it’s complete, navigate to that directory and run the development command:

```shell
cd my-travel-bucket-list
yarn develop
# or
npm run develop

```

Once it’s finished location, your app should be ready to go!

### Cleaning our some demo code

Because we’re using a Starter, it has a little bit of demo code. Let’s clean that out to avoid any confusion.

Open up the `src/pages/index.js` file.

First, remove everything inside of `mapEffect` except the first line and set up an alias for `leafletElement` to `map`:

```js
async function mapEffect({ leafletElement: map } = {}) {
  if ( !map ) return;
}

```

With that gone, we can remove the `markerRef` definition at the top of the `IndexPage` component, remove the `ref={markerRef}` prop from our `<Marker>` component, and the `useRef` import next to React.

Now, we can remove all of the variables that start with `popup` and `time`, including:

* timeToZoom
* timeToOpenPopupAfterZoom
* timeToUpdatePopupAfterZoom
* popupContentHello
* popupContentGatsby

Lastly, you can remove all of the following lines:

```js
import L from 'leaflet';
...
import { promiseToFlyTo, getCurrentLocation } from 'lib/map';
...
import gatsby_astronaut from 'assets/images/gatsby-astronaut.jpg';
...
const ZOOM = 10;

```

Once done, we should be ready to go with a basic app with a map!

![Image](https://www.freecodecamp.org/news/content/images/2020/06/new-app-gatsby-starter-leaflet.jpg)
_New app with Gatsby Starter Leaflet_

[Follow along with the commit!](https://github.com/colbyfayock/my-travel-bucket-list/commit/63eed5a7a208ede6f8eeec44e0c08b594b407360)

## Step 2: Creating and managing a list of travel locations with GraphCMS

### Creating a GraphCMS account

To get started with GraphCMS, you’ll need an account. I’m not going to walk you through this part, but the good news is they have a generous free tier that makes it easy to sign up for us to use for our demo!

[Sign up for GraphCMS](https://app.graphcms.com/signup)

Alternatively, if you already have an account, you can make sure you’re logged in.

### Creating a new GraphCMS project

Once logged in, we’ll want to create a new project. We’re going to create one manually, so once at the [GraphCMS Dashboard](https://app.graphcms.com/), select **Create new project**:

![Image](https://www.freecodecamp.org/news/content/images/2020/06/graphcms-create-new-project.jpg)
_Creating a new project in GraphCMS_

Here, you can enter whatever you’d like for the **Name** and **Description** such as:

* Name: My Travel Bucket List
* Description: The locations that I want to travel to some day!

Below that you’ll see a map where you’ll select a **Region**. This is where your database data will live, so while it probably doesn’t matter too much for our purposes, you can choose the one that’s closest to you.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/graphcms-configure-new-project.jpg)
_Configuring a new project in GraphCMS_

After you select your options, go ahead and click **Create Project**.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/graphcms-select-plan.jpg)
_Selecting the Personal plan in GraphCMS_

Next, you’ll be presented with billing options. Since we’re just creating a demo, under **Personal** select **Continue** at which point we’ll be dropped into our new GraphCMS project dashboard.

### Creating a new Content Model Schema with GraphCMS

In GraphCMS, a Content Model refers to a specific type of data that has specific properties associated with it. In our case, our Model will be a Destination, which will be defined by a Name and a Location.

First, navigate to the **Schema** section of GraphCMS in the left sidebar and select **Create Model**.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/graphcms-create-new-schema-model.jpg)
_Creating a new Schema Model in GraphCMS_

Once selected, you’ll see a popup that asks for a bit more information. Here, you can type in “Destination” as the **Display Name**, which will also fill in most of the other fields. We’ll leave those as is.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/graphcms-configure-new-content-model.jpg)
_Configuring a new Model in GraphCMS_

Feel free to add a description if you’d like, but it’s not required. Then select **Create model**.

Now that we have our Model, we need our properties.

First, select **Single line text** in the right list of fields and add a **Display Name** of “Name”. This will also fill out **App Id** which you can leave as is. Then click **Create**.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/graphcms-configure-text-field.jpg)
_Adding and configuring a new text field in GraphCMS_

Next, scroll down in the field options on the right and under **Location** select **Map**. Add “Location” as the **Display Name**, which will set the **App Id** as “location” which you can leave as is. Then same as before, click **Create**.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/graphcms-configure-new-map-field.jpg)
_Adding and configuring a new map field in GraphCMS_

Now we have a Content Model which we’ll use to create our locations!

![Image](https://www.freecodecamp.org/news/content/images/2020/06/graphcms-destination-content-model.jpg)
_Destination content Model in GraphCMS_

### Creating our locations

Finally, let’s create our locations. Navigate over to **Content** in the GraphCMS dashboard, make sure you’ve selected **Destination** under **System** (should be the only one), and select **Create New**.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/graphcms-add-new-content.jpg)
_Create new Destination Content in GraphCMS_

Now we can start adding all of our locations! First, add the name of your location in the **Name** field, then you can use the **Search** box under **Location** to find that location on the map.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/graphcms-create-new-destination-content-item.jpg)
_Adding a new Destination Content item in GraphCMS_

Once you’re good, hit **Save and publish**. This will create your first location!

Follow those same steps and create as many locations as you want.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/graphcms-destination-content-items.jpg)
_List of Destination Content items in GraphCMS_

We’ll use these for our map and bucket list.

## Step 3: Querying our GraphCMS location data with Gatsby and GraphQL

Now that we have our locations, let’s use them!

### Adding a plugin to Gatsby to query our GraphQL data

First, we need to [add a new plugin](https://www.gatsbyjs.org/packages/gatsby-source-graphql/) to our Gatsby project to query our GraphQL data. In your terminal make sure your development server isn’t running and run:

```shell
yarn add gatsby-source-graphql
# or
npm install gatsby-source-graphql

```

Next, open up your `gatsby-config.js` file in the root of your project and add the following to your plugins:

```json
{
  resolve: 'gatsby-source-graphql',
  options: {
    typeName: 'GCMS',
    fieldName: 'gcms',
    url: '[API ENDPOINT]',
  }
}

```

This will be what sources our data from GraphCMS, but we need an endpoint.

### Finding our API endpoint for GraphCMS

Open back up your browser and head over to your GraphCMS project. After selecting **Settings** in the left navigation, select **API Access**.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/graphcms-api-access.jpg)
_API Access in GraphCMS_

Before we copy our API Endpoint, first we need to update our permissions so we can query our API. Under **Public API Permissions**, check the box next to **Content from stage Published** and click **Save**.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/graphcms-configure-api-access.jpg)
_Configuring API permissions in GraphCMS_

Next, copy the URL under **Endpoints**:

![Image](https://www.freecodecamp.org/news/content/images/2020/06/graphcms-copy-api-access-endpoint.jpg)
_Copying API Endpoint in GraphCMS_

And paste that in to your `gatsby-config.js` file that we modified above:

```json
{
  resolve: 'gatsby-source-graphql',
  options: {
    typeName: 'GCMS',
    fieldName: 'gcms',
    url: 'https://[region-id].graphcms.com/v2/[project-id]/master',
  },
},

```

_Note: your URL will have actual values inside of `[region-id]` and `[project-id]`._

Save your `gatsby-config.js` file and start your development server backup (`yarn develop`) and we’re ready to go!

### Querying our locations via GraphQL

Finally, let’s actually query our data so that we’ll be able to use it in our app.

We’re going to create a new [React Hook](https://reactjs.org/docs/hooks-reference.html) that we’ll be able to use to grab our locations anywhere within our app.

Under `src/hooks/index.js`, add the following line to the existing list:

```js
export { default as useDestinations } from './useDestinations';

```

This will allow us to more conveniently import our hook which we’ll create next.

Under `src/hooks`, create a new file `useDestinations.js` and paste in this code:

```js
import { graphql, useStaticQuery } from 'gatsby';

export default function useDestinations() {
  const { gcms = {} } = useStaticQuery( graphql`
    query {
      gcms {
        destinations {
          id
          name
          location {
            latitude
            longitude
          }
        }
      }
    }
  ` );

  let { destinations } = gcms;

  return {
    destinations,
  };
}

```

Here, we’re:

* Importing the `graphql` and `useStaticQuery` utilities from Gatsby
* We’re creating a new function (or hook) that is exported by default
* In that function, we’re using `useStaticQuery` to create a new GraphQL query which asks GraphCMS to return the data structure we defined.
* That query returns a value which we destructure immediately to grab the `gmcs` object
* We destructure `destinations` from `gmcs` and return it as part of a new object from our hook

With this, we can now use our hook anywhere in our app!

Head over to your `src/pages/index.js` file, first import our new hook:

```js
import { useDestinations } from 'hooks';

```

And at the top of the `IndexPage` component, query our data:

```js
const { destinations } = useDestinations();

```

This puts all of our locations into the `destinations` variable. We can test that this works by console logging it out:

```js
console.log('destinations', destinations);

```

And once we open up our browser and look in our web developer tools console, we can see our location data!

![Image](https://www.freecodecamp.org/news/content/images/2020/06/gatsby-starter-leaflet-logging-graphcms-destinations.jpg)
_Logging destinations data to the web console_

## Step 4: Creating a bucket list of destinations and adding them to the map

We’re going to start with creating a simple text list of our destinations. This will let us see all of our destinations in an easy to read format.

### Creating a text list of our destinations

Inside of our `IndexPage` and above “Still Getting Started?”, let’s add the following code:

```jsx
<h2>My Destinations</h2>
<ul>
  { destinations.map(destination => {
    const { id, name } = destination;
    return <li key={id}>{ name }</li>
  })}
</ul>

```

This code:

* Adds a new header for our list
* Creates a new unordered list
* Loops through our `destinations` and creates a new list item for each destination that include’s the location’s name

Once we hit save and reload, we should see our list under our map!

![Image](https://www.freecodecamp.org/news/content/images/2020/06/app-adding-list-of-destinations.jpg)
_New basic list of destinations in the app_

The list looks a little odd though right? We probably want to format it a little better to fit into the page.

Open up `src/assets/stylesheets/pages/_home.scss` and inside of the `.home-start` class, add:

```scss
.home-start {

  ...

  ul {
    list-style: none;
    padding: 0;
    margin: 1.2em 0;
  }

```

Let’s also modify the `h2` to space things out a little better:

```scss
.home-start {

  ...

  h2 {

    margin-top: 2em;

    &:first-child {
      margin-top: 0;
    }

  }

```

Once you hit save and reload, it should look a little better.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/app-fixing-styles-list-of-destinations.jpg)
_Destinations in the app with cleaned up styles_

Feel free to make additional changes, but we’ll leave it there for now.

### Adding our destinations to the map

Now we can finally add our destinations to the map!

Inside of our `<Map>` component, we already have a `<Marker>`. This allows us to easily add a marker to the map given a position. We’ll take this concept and combine it with our text list to add our locations to the map.

Let’s update our `<Map>` code to match the following:

```jsx
<Map {...mapSettings}>
  { destinations.map(destination => {
    const { id, name, location } = destination;
    const position = [location.latitude, location.longitude];
    return <Marker key={id} position={position} />
  })}
</Map>

```

Here we:

* Loop through our `destinations` to dynamically create a new list of components inside our `<Map>`
* Inside each loop instance, we destructure our date from `destination`
* We create a new `position` array with the latitude and longitude
* Create a new `Marker` where we use our position to add it to the map

This gives us our markers on the map!

![Image](https://www.freecodecamp.org/news/content/images/2020/06/mapping-app-with-destination-markers.jpg)
_Markers for each destination in the mapping app_

But we want to know what each of those locations are, so let’s also add a popup to each marker that will show the name.

First, we need to import `Popup` from `react-leaflet`:

```js
import { Marker, Popup } from 'react-leaflet';

```

Then, let’s update our `<Marker>` component to return:

```jsx
return (
  <Marker key={id} position={position}>
    <Popup>{ name }</Popup>
  </Marker>
);

```

And once we save and open back up our map, you can now click on each marker and see our destinations name!

![Image](https://www.freecodecamp.org/news/content/images/2020/06/mapping-app-with-destination-marker-popup.jpg)
_Popup for each destination marker in the mapping app_

### Before we’re done, center the map

Previously, our demo map centered on Washington, DC. Let’s update that to the center of the world since our map doesn’t focus on the United States.

Update the `LOCATION` variable to:

```js
const LOCATION = {
  lat: 0,
  lng: 0,
};

```

And with that, we have our map!

![Image](https://www.freecodecamp.org/news/content/images/2020/06/mapping-app-with-travel-bucket-list-markers.jpg)
_Final mapping app with markers and popups for each destination_

[Follow along with the commit!](https://github.com/colbyfayock/my-travel-bucket-list/commit/56dbadb74cea2770174eb8ea7c039be27ca18971)

## What else other features can we add to our app?

### Add a way to check off each location

Inside GraphCMS, you can add a new field to your Destination content model that allows you to select whether you visited each location or not.

With this value, we can add it to our query and update our map with some kind of indicator like a checkmark to show that we’ve checked it off our bucket list!

### Customize your map background styles

We’re using a public version of [OpenStreetMap](https://www.openstreetmap.org/#map=5/38.007/-95.844) which is open source, but [Mapbox](https://www.mapbox.com/) offers some cool maps we can use to make it look a little more impressive.

If you want to get started changing your map styles, you can [check out this other walkthrough](https://www.freecodecamp.org/news/how-to-set-up-a-custom-mapbox-basemap-with-gatsby-and-react-leaflet/) of mine to learn how to use Mapbox.

[Check out the blog post](https://www.colbyfayock.com/2020/04/how-to-set-up-a-custom-mapbox-basemap-style-with-react-leaflet-and-leaflet-gatsby-starter) or [watch the video](https://www.youtube.com/watch?v=KcPJr1b_rv0)!

### Style the map markers with a custom image

You can check out my video walk through on how to change the markers to a custom image.

Take that a step further and use the feature above to dynamically show a different marker image when you’ve checked off a location.

[Check out the video on Egghead.io!](https://egghead.io/lessons/react-customize-geojson-data-markers-with-a-react-leaflet-icon-image?pl=mapping-with-react-leaflet-e0e0&af=atzgap)

## Want to learn more about maps?

Check out some of my other tutorials and videos:

* [Mapping with React Leaflet](https://egghead.io/playlists/mapping-with-react-leaflet-e0e0?af=atzgap) ([egghead.io](https://egghead.io/?af=atzgap))
* [Mapping Apps with React, Gatsby, & Leaflet](https://www.youtube.com/playlist?list=PLFsfg2xP7cbJTnTFH3OGXEAt9O1mpoqpR) ([youtube.com](https://www.youtube.com/channel/UC7Wpv0Aft4NPNhHWW_JC4GQ))
* [How to create a Coronavirus (COVID-19) Dashboard & Map App with Gatsby and Leaflet](https://www.colbyfayock.com/2020/03/how-to-create-a-coronavirus-covid-19-dashboard-map-app-with-gatsby-and-leaflet) (colbyfayock.com)
* [How to Create a Summer Road Trip Mapping App with Gatsby and Leaflet](https://www.colbyfayock.com/2020/03/how-to-create-a-summer-road-trip-mapping-app-with-gatsby-and-leaflet) (colbyfayock.com)
* [How to build a mapping app in React the easy way with Leaflet](https://www.freecodecamp.org/news/easily-spin-up-a-mapping-app-in-react-with-leaflet/) (colbyfayock.com)
* [Anyone Can Map! Inspiration and an introduction to the world of mapping](https://www.colbyfayock.com/2020/03/anyone-can-map-inspiration-and-an-introduction-to-the-world-of-mapping) (colbyfayock.com)

## What’s on your travel bucket list?

[Let me know on Twitter!](https://twitter.com/colbyfayock)

%[https://twitter.com/colbyfayock/status/1275441134144110595]

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

