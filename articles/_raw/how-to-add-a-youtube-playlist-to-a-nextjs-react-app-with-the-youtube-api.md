---
title: How to Add a YouTube Playlist to a Next.js React App with the YouTube API
subtitle: ''
author: Colby Fayock
co_authors: []
series: null
date: '2020-08-06T21:11:50.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-a-youtube-playlist-to-a-nextjs-react-app-with-the-youtube-api
coverImage: https://www.freecodecamp.org/news/content/images/2020/08/youtube-api.jpg
tags:
- name: api
  slug: api
- name: Next.js
  slug: nextjs
- name: React
  slug: react
seo_title: null
seo_desc: "YouTube gives content creators a ton of tools to add their work for everyone\
  \ to see. But those tools only help you manage the experience on YouTube. \nHow\
  \ can we utilize the YouTube API to bring our video content to our own website?\n\
  \nYouTube has an AP..."
---

YouTube gives content creators a ton of tools to add their work for everyone to see. But those tools only help you manage the experience on YouTube. 

How can we utilize the YouTube API to bring our video content to our own website?

* [YouTube has an API?](#heading-youtube-has-an-api)
* [What are we going to build?](#heading-what-are-we-going-to-build)
* [Step 0: Getting started with Next.js](#heading-step-0-getting-started-with-nextjs)
* [Step 1: Creating a Google Developer project](#heading-step-1-creating-a-google-developer-project)
* [Step 2: Requesting playlist items from the YouTube API](#heading-step-2-requesting-playlist-items-from-the-youtube-api)
* [Step 3: Showing YouTube playlist videos on the page](#heading-step-3-showing-youtube-playlist-videos-on-the-page)

%[https://www.youtube.com/watch?v=8YWrmZoUYGs]

## YouTube has an API?

Yup! YouTube, along with a lot of other Google services, [has an API](https://developers.google.com/youtube) that we can use to take advantage of our content in ways outside of YouTube. And the API is pretty extensive.

With YouTube’s API, you can do things like manage your videos, access analytics, and manage playback. But we’re going to use it for grabbing videos from a playlist so that we can add them to a page.

## What are we going to build?

We’re going to put together a [Next.js](https://nextjs.org/) app that uses the YouTube API To fetch videos from a playlist.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/youtube-playlist-app-demo.jpg)
_[Demo Playlist Gallery](https://demo-youtube-playlist.vercel.app/)_

We’ll take those videos and we’ll display their thumbnails on a page that links to the video.

## Step 0: Getting started with Next.js

To spin up an app, we’re going to use Next.js. Using yarn or npm, we can easily create a new app that will let us dive right into the code.

So to get started, navigate to where you want to create your project and run:

```
yarn create next-app
# or
npx create-next-app

```

That script will prompt you for a project name. I’m going to use “my-youtube-playlist”, and it will install all of the dependencies needed to get started.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/command-line-new-nextjs-project.jpg)
_Successfully created a new app with Next.js_

Then navigate to that directory and run `yarn dev` to start your development server and we’re ready to go.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/new-nextjs-app.jpg)
_Next.js default page_

[Follow along with the commit!](https://github.com/colbyfayock/my-youtube-playlist/commit/f062c01111aa064c43111dad6a23812637ce1f92)

## Step 1: Creating a Google Developer project

To use the API, we’re going to need a new project in the Google Developer console that will allow us to generate an API key to use the service.

First, head over to: [https://console.developers.google.com/](https://console.developers.google.com/).

Once there and logged in with your Google account, we’ll want to create a new project.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/google-developer-console-new-project.jpg)
_Creating a new project in Google Developer Console_

At this point, you can name your project whatever you’d like. I’m going with “My YouTube Playlist”. Then click Create.

By default, Google won’t drop you into the new project. It kicks off a job to create that project, but once it finishes, you can open back up the project selector and select your new project.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/google-developer-console-select-project.jpg)
_Selecting your project_

Next, we want to create an API key. Navigate to Credentials, click Create Credentials, and then select API key.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/google-api-create-api-key.jpg)
_Creating an API Key credential_

This will create a new API key that you’ll want to copy and save for later.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/google-developer-api-key.jpg)
_Copying your new API key_

_Note: This API key should be kept secret. If you expose this or add it somewhere available to the public like GitHub, others can abuse it and leave you with a bill to pay._

Finally, we need to add the YouTube API as a service. Navigate to **Library** in the sidebar, search for “YouTube”, and then select **YouTube Data API v3**.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/google-api-youtube-data-api.jpg)
_Searching for YouTube API in the Google API Library_

Finally after that page loads, click Enable, which will bring you to a new dashboard page and you’ll be ready to go.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/google-api-enable-youtube-data-api.jpg)
_Enabling YouTube Data API v3_

## Step 2: Requesting playlist items from the YouTube API

To request our data, we’re going to use the [getServerSideProps](https://nextjs.org/docs/basic-features/data-fetching#getserversideprops-server-side-rendering) function.

First, open up the `pages/index.js` file and add the following above the `Home` component.

```js
const YOUTUBE_PLAYLIST_ITEMS_API = 'https://www.googleapis.com/youtube/v3/playlistItems';

export async function getServerSideProps() {
  const res = await fetch(`${YOUTUBE_PLAYLIST_ITEMS_API}`)
  const data = await res.json();
  return {
    props: {
      data
    }
  }
}

```

Here’s what we’re doing:

* We’re creating a new constant that stores our API endpoint
* We’re creating and exporting a new `getServerSideProps`  function
* Inside that function, we fetch our endpoint
* We then transform that to JSON
* Finally, we return the data as props in our object

Now, if we destructure the `data` prop from `Home` and console log out that data like the following:

```js
export default function Home({ data }) {
  console.log('data', data);

```

We can now see that we get an error:

![Image](https://www.freecodecamp.org/news/content/images/2020/08/google-api-invalid-key.jpg)
_Request error requiring API key_

We’re not using our API key, so let’s use that.

Create a new file in the root of the project called `.env.local` and add the following content:

```
YOUTUBE_API_KEY="[API Key]"

```

Make sure to replace `[API Key]` with your API key from Step 1.

At this point, you’ll want to restart your server so Next.js can see the new variable.

Now, update the `getServerSideProps` function to add your key to the API request:

```js
export async function getServerSideProps() {
  const res = await fetch(`${YOUTUBE_PLAYLIST_ITEMS_API}?key=${process.env.YOUTUBE_API_KEY}`)

```

And if we reload the page, again, we get an error:

![Image](https://www.freecodecamp.org/news/content/images/2020/08/google-api-missing-parameters.jpg)
_Request error requiring API parameters_

Now, we’re missing the playlist ID and the filters we want to grab our data.

Using the parameters from the [playlist items API](https://developers.google.com/youtube/v3/docs/playlistItems/list#request), let’s update our API endpoint again:

```js
const res = await fetch(`${YOUTUBE_PLAYLIST_ITEMS_API}?part=snippet&maxResults=50&playlistId=[Playlist ID]&key=${process.env.YOUTUBE_API_KEY}`)

```

Here, we’re adding:

* `part=snippet`: this tells the API we want the snippet
* `maxResults=50`: this sets the maximum number of playlist items that get returned to 50
* `playlistId=[Playlist ID]`: this adds the parameter to configure the playlist ID. Here, you should update that value to the playlist ID of your choice.

Note: you can find the playlist ID in the URL of the playlist you want to use.

And finally, when we reload the page, we have our data:

![Image](https://www.freecodecamp.org/news/content/images/2020/08/google-api-youtube-playlist-data.jpg)
_Successfully requested playlist items_

[Follow along with the commit!](https://github.com/colbyfayock/my-youtube-playlist/commit/7ca0de9005303950fd1aac4442b8fba7b4b179a7)

## Step 3: Showing YouTube playlist videos on the page

Now that we have our data, we want to display it.

To make use of what we already have from Next.js, we can transform the existing grid into a grid of YouTube thumbnails.

Let’s replace the entire `<div>` with the `className` of `styles.grid` to:

```jsx
<ul className={styles.grid}>
  {data.items.map(({ id, snippet = {} }) => {
    const { title, thumbnails = {}, resourceId = {} } = snippet;
    const { medium } = thumbnails;
    return (
      <li key={id} className={styles.card}>
        <a href={`https://www.youtube.com/watch?v=${resourceId.videoId}`}>
          <p>
            <img width={medium.width} height={medium.height} src={medium.url} alt="" />
          </p>
          <h3>{ title }</h3>
        </a>
      </li>
    )
  })}
</ul>

```

Here’s what we’re doing:

* We’re changing the `<div>` to a `<ul>` so it’s more semantic
* We create a map through the items of our playlist to dynamically create new items
* We’re destructuring our data grabbing the id, title, thumbnail, and video ID
* Using the ID, we add a key to our `<li>`
* We also move the `className` of `styles.card`  from the `<a>` to the `<li>`
* For our link, we use the YouTube video ID to create the video URL
* We add our thumbnail image
* We use our `title` for the `<h3>`

And if we reload the page, we can see that our videos are there, but the styles are a bit off.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/playlist-videos.jpg)
_Displaying playlist items on the page_

To fix this, we can start by adding the following styles to `.grid` inside of the `Home.module.css` file:

```css
list-style: none;
padding: 0;
margin-left: 0;

```

We can also change

```css
align-items: center;

```

to

```css
align-items: flex-start;

```

which will help fix the alignment of our videos.

But we’ll notice we still don’t have two columns like the original Next.js layout.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/playlist-videos-fixed-list.jpg)
_Removing default HTML list styles_

Under our `.grid` class that we just updated, add the following:

```css
.grid img {
  max-width: 100%;
}

```

This makes sure all of our images don’t exceed the container. This will prevent the overflow and will let our images settle in to two columns.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/playlist-videos-fixed-columns.jpg)
_Fixing column sizes_

And that gives us our playlist videos.

[Follow along with the commit!](https://github.com/colbyfayock/my-youtube-playlist/commit/5bc2d374ea706d3ad920a8568097e3dd6e30f568)

## What else can we do?

### Embed a player and show that video on click

YouTube also gives controls for their own player. So using some JavaScript, we can take advantage and when someone clicks one of our video thumbnails, we can show an embedded player and play that video.

[YouTube Player API Reference for iframe Embeds](https://developers.google.com/youtube/iframe_api_reference)

### Get analytics data

While YouTube provides some analytics in its dashboard, maybe you want something more advanced.

You can use the Analytics and Reporting APIs to get more insight into your channel and videos.

[YouTube Analytics and Reporting APIs](https://developers.google.com/youtube/analytics)

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

