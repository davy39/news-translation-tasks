---
title: How to Build a Podcast Player with Transcriptions using Vue and Supabase
subtitle: ''
author: Brian Barrow
co_authors: []
series: null
date: '2022-02-28T23:05:43.000Z'
originalURL: https://freecodecamp.org/news/build-a-podcast-player-with-transcriptions-using-vue-supabase
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/Build-Podcast-Player-app-w-transcriptions-using-Vue-Supabase@2x.jpg
tags:
- name: audio
  slug: audio
- name: projects
  slug: projects
- name: supabase
  slug: supabase
- name: vue
  slug: vue
seo_title: null
seo_desc: "In this post we will walk through setting up a Podcast Player app using\
  \ Supabase and Vue 3, including getting transcriptions for the podcasts. \nThis\
  \ is a continuation of my previous post on setting up Authentication using Supabase.\
  \ If you aren't fami..."
---

In this post we will walk through setting up a Podcast Player app using Supabase and Vue 3, including getting transcriptions for the podcasts. 

This is a continuation of my previous post on [setting up Authentication using Supabase](https://www.freecodecamp.org/news/add-supabase-authentication-to-vue/). If you aren't familiar with getting Supabase set up in your project, I highly recommend going through that post. 

## The Starting Code Repo

Here is the repo from my previous post that will get you to where this post will be starting. You'll just need to set up Supabase and add your credentials/API key to a `.env.local` file to get up and running. This repo also has styling applied to it that was not included in the previous post.

%[https://github.com/briancbarrow/vue-supabase-auth]

## Prerequisites

You should be familiar with JavaScript, have had some experience with Vue 3, and you should have Node.js and NPM installed on your machine. 

If you've gone through the previous post about Supabase Authentication or this other post on [Getting Started with Supabase](https://developers.deepgram.com/blog/2021/11/getting-started-with-supabase/) you'll be good to go.

You will also need a [free API key from Deepgram](https://console.deepgram.com/signup) for when we get to the transcription section. 

## Getting Started

Once you have downloaded the [repo from above](https://github.com/briancbarrow/vue-supabase-auth) run `npm install` to get the packages installed for the project. 

Add your `VITE_SUPABASE_URL` and `VITE_SUPABASE_ANON_KEY` environment variables from your the dashboard of your own Supabase project.

Run `npm run dev` to get the local dev server started.

Sign in to the app using either the Sign In form or the Magic Link form. Once you get signed in, you should see the HelloWorld component/page with a sign out button at the top. 

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screen-Shot-2022-02-18-at-2.20.26-PM.png)
_Hello World component_

## How to Fetch a Podcast RSS Feed

The first thing we need to do is add functionality to get a podcast feed into our app. Create a new component in the components folder called `PodcastFeed.vue`. 

Most podcasts have a public RSS feed that we can use to get the information we need with a simple fetch request. 

Inside the of the `PodcastFeed.vue` component create the following form that takes in a RSS feed URL, and hooks up to a button that triggers the fetch request.

Note: I've tried to add comments in the code to help you understand what each part is doing.

```js
<template>
  <div class="podcast-input-feed">
    <label for="email">Podcast RSS Feed URL</label>
    <div class="">
      <!-- binding the url input field to the 'url' data property -->
      <input
        type="url"
        name="url"
        id="url"
        v-model="url"
        placeholder="https://rss.your-org.org/feed/"
        aria-describedby="rss-url"
      />
    </div>
    <!-- hooking the button click to the 'getRssFeed' method -->
    <button @click="getRssFeed()" type="button" class="">Get Feed</button>
  </div>
</template>

<script>
import { ref } from "vue";
import { supabase } from "../supabase";
import { store } from "../store";
export default {
  setup() {
    // I am initializing the url to a url I know works, so that I don't need to keep inputing a url as I'm developing.
    // feel free to change this to a url of your own choosing
    const url = ref("https://anchor.fm/s/3e9db190/podcast/rss");
    // initializing the podcast state to an empty object
    const podcast = ref({});

    function getRssFeed() {
      const feedUrl = url.value;
      return (
        fetch(feedUrl)
          // this returns a promise so we need to convert it to a string
          .then((response) => response.text())
          // this next line is to parse the xml response
          .then((str) =>
            new window.DOMParser().parseFromString(str, "text/xml")
          )
          // parsing the data from the xml response and setting it into the podcast state
          .then((data) => {
            console.log("Data: ", data);
            podcast.value.image_url = data
              .querySelector("image")
              .querySelector("url").innerHTML;
            podcast.value.title = data.querySelector("title").textContent;
            podcast.value.description =
              data.querySelector("description").textContent;
            podcast.value.rss_url = feedUrl;
          })
          .catch((err) => {
            console.log("ERROR: ", err);
          })
      );
    }
    return {
      url,
      podcast,
      store,

      getRssFeed,
    };
  },
};
</script>

```

With that set up, replace the HelloWorld component in the `App.vue` file with this new `PodcastFeed.vue` component:

```js
<template>
  <button v-if="store.state.user" class="signout-button" @click="signOut">Sign Out</button>
  <!-- Check if user is available in the store, if not show auth compoenent -->
  <Auth v-if="!store.state.user" />
  <!-- If user is available, show the app -->
  <div v-else class="app">
    <PodcastFeed />
  </div>
</template>

<script>
import Auth from "./components/Auth.vue";
import PodcastFeed from "./components/PodcastFeed.vue";

import { store } from "./store";
import { supabase } from "./supabase";

export default {
  components: {
    PodcastFeed,
    Auth,
  },
  setup() {
    // we initially verify if a user is logged in with Supabase
    store.state.user = supabase.auth.user();
    // we then set up a listener to update the store when the user changes either by logging in or out
    supabase.auth.onAuthStateChange((event, session) => {
      if (event == "SIGNED_OUT") {
        store.state.user = null;
      } else {
        store.state.user = session.user;
      }
    });

    async function signOut() {
      const { error } = await supabase.auth.signOut();
    }

    return {
      store,

      signOut,
    };
  },
};
</script>

<style></style>

```

So now the app should look like this:

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screen-Shot-2022-02-18-at-2.38.40-PM.png)
_App after adding PodcastFeed.vue_

When you click the button, the data that comes back from the fetch request will show up in the console. 

![Image](https://www.freecodecamp.org/news/content/images/2022/02/xml-data-from-rss.png)
_Parsed XML Data_

In the `getRssFeed` method we parse that data and then take the information we need and add it to the `podcast` state data. We need to display that data so that the user can know the request was successful. We also want to add better error messaging in case the request fails. 

Create a new component called `PodcastInfo.vue` and add the following code:

```js
<template>
  <div class="podcast-info">
    <div class="image-container">
      <img :src="podcast.image_url" alt="" class="" />
    </div>
    <div class="podcast-text">
      <div class="title-desc">
        <p class="title">
          {{ podcast.title }}
        </p>
        <p class="desc">
          {{ podcast.description }}
        </p>
      </div>
    </div>
  </div>
</template>

<script>
import { store } from "../store";
import { supabase } from "../supabase";

export default {
  props: {
    podcast: {
      type: Object,
      required: true,
    },
  },
  computed: {},
  methods: {},
  setup() {},
};
</script>

<style scoped></style>

```

```js
<template>
  <div class="info-error">
    <h3 class="">There was an error with your request</h3>
    <p class="">Check your RSS feed URL and try again.</p>
  </div>
</template>

<script>
export default {};
</script>

```

Then update the  `PodcastFeed.vue` to the following in order to bring in the component:

```js
<template>
  <div class="podcast-input-feed">
    <label for="email">Podcast RSS Feed URL</label>
    <div class="">
      <!-- binding the url input field to the 'url' data property -->
      <input
        type="url"
        name="url"
        id="url"
        v-model="url"
        placeholder="https://rss.your-org.org/feed/"
        aria-describedby="rss-url"
      />
    </div>
    <!-- hooking the button click to the 'getRssFeed' method -->
    <button @click="getRssFeed()" type="button" class="">Get Feed</button>
	<!-- Adding in these two new components -->
    <podcast-info v-if="podcast.title && !requestError" :podcast="podcast" />
  </div>
</template>

<script>
import { ref } from "vue";
import { supabase } from "../supabase";
import { store } from "../store";

import PodcastInfo from "./PodcastInfo.vue";

export default {
  components: {
    PodcastInfo,
  },

  setup() {
    // I am initializing the url to a url I know works, so that I don't need to keep inputing a url as I'm developing.
    // feel free to change this to a url of your own choosing
    const url = ref("https://anchor.fm/s/3e9db190/podcast/rss");
    // initializing the podcast state to an empty object
    const podcast = ref({});
    const requestError = ref(false);

    function getRssFeed() {
      const feedUrl = url.value;
      return (
        fetch(feedUrl)
          // this returns a promise so we need to convert it to a string
          .then((response) => response.text())
          // this next line is to parse the xml response
          .then((str) =>
            new window.DOMParser().parseFromString(str, "text/xml")
          )
          // parsing the data from the xml response and setting it into the podcast state
          .then((data) => {
            console.log("Data: ", data);
            podcast.value.image_url = data
              .querySelector("image")
              .querySelector("url").innerHTML;
            podcast.value.title = data.querySelector("title").textContent;
            podcast.value.description =
              data.querySelector("description").textContent;
            podcast.value.rss_url = feedUrl;
          })
          .catch((err) => {
            requestError.value = true;
          })
      );
    }
    return {
      url,
      podcast,
      store,
      requestError,

      getRssFeed,
    };
  },
};
</script>

```

Now when you click the "Get Feed" button, you should see the following:

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screen-Shot-2022-02-18-at-3.05.15-PM.png)

Now that we can get the info displayed, we can wire up the app to save the info to Supabase. 

## How to Add a Table to the Supabase DB

The first thing we need to do is add a table to our Supabase DB. In the Dashboard for your project on Supabase, select the Table Editor and click the `New table` button. I name the new table `podcasts`. Enable the Row Level Security (this makes our DB more secure) and add the following columns:

* id (this column should be filled in for you when you create a new table)
* created_at
* name
* image_url
* description
* rss_url
* user_id (for this one, we want to link it via foreign key to our users table created by the Auth service. Click the chain-link icon to get that set up and link it to the `users` table on the `id` column.)

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screen-Shot-2022-01-19-at-9.08.50-AM.png)
_podcasts table setup_

Because we enabled the Row Level Security, the table won't let anything get inserted until we update the policies for it. 

Under the Authentication tab there is a section called 'Policies'. There you should see the `podcasts` table and a button to create a new policy. When you click on it, it will give you the option to create a policy from a template. Choose the template called 'Enable insert access for authenticated users only'. Now, only users that are authenticated have access to insert anything into the table. 

When Supabase runs the `insert` command, it will automatically run a `select` command and return the newly inserted row. Because of this, we also have to add a policy to the table allowing the user `SELECT` access. 

Create a new policy with the name `Enable select based on userid` and then in the `USING expression` section put `(uid() = user_id)`. That will prevent users from reading other users' information, while still giving them access to their own podcasts in the table.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/select-user-policy.png)
_Select based on userid policy_

## How to Link Up the UI to the DB So the User Can Save Podcasts

To add a podcast to our DB, we will first add a button to the `PodcastInfo` component. Add this code to the bottom of the `<div class="podcast-info">`:

```html
<button @click="addPodcast">Add to My Podcasts</button>
```

Now add a method called `addPodcast` to the setup function of the component like this. Don't forget to add the `props` to the argument of the setup function.

```js
setup(props) {
    function addPodcast() {
      // Setting up the podcast object to send to supabase
      const podcast = {
        name: props.podcast.title,
        image_url: props.podcast.image_url,
        description: props.podcast.description,
        rss_url: props.podcast.rss_url,
        user_id: store.state.user.id,
      };
      // calling supabase method to insert into the db
      supabase
        .from("podcasts")
        .insert(podcast)
        .then(({ body }) => {
          store.addPodcastToStore(body[0]);
        })
        .catch((err) => {
          console.log(err);
        });
    }

    return {
      addPodcast,
    };
  },
```

You can see in the `.then` statement we call a method from the global store. Update the `store.js` file to the following:

```js
import { reactive } from "vue";

export const store = {
  state: reactive({
    user: {},
    // adding podcasts array to global store
    podcasts: [],
  }),

  // adding addPodcastToStore method to store object
  addPodcastToStore(podcast) {
    this.state.podcasts.push(podcast);
  },
};
```

Now when we click the "Add To My Podcasts" button, the app makes a call to Supabase and then takes the result of that call and adds it to the podcasts array in the global store. (If you are getting a 403 error, make sure you set up the policies correctly. Maybe try restarting the dev server too.)

If a podcast is already in a user's list of podcasts, we don't want to let them click the add button again. To prevent this we need to first call Supabase to get all of the user's podcasts, and then check if the podcast they are looking at is in that list.

This method will not be specific to any one component so we want to create it inside of the global store. That way, any component has access to it. Add this method to the `store.js` file underneath the `addPodcastToStore` method:

```js
getPodcastsFromDB() {
    supabase
        .from("podcasts")
        .select("*")
        .then(({ body }) => {
            this.state.podcasts = body;
        });
},
```

Then we want to update the method to be called whenever a user signs in. Inside of `App.vue` change the `onAuthStateChange` handler to this:

```js
supabase.auth.onAuthStateChange((event, session) => {
    if (event == "SIGNED_OUT") {
        store.state.user = null;
    } else {
        // make call to supabase to get Podcasts for the user
        store.getPodcastsFromDB();
        store.state.user = session.user;
    }
});
```

Now update the `PodcastInfo.vue` file to this in order to display to the user if a podcast is already in their library.

```js
<template>
  <div class="podcast-info">
    <div class="image-container">
      <img :src="podcast.image_url" alt="" class="" />
    </div>
    <div class="podcast-text">
      <div class="title-desc">
        <p class="title">
          {{ podcast.title }}
        </p>
        <p class="desc">
          {{ podcast.description }}
        </p>
      </div>
    </div>
    <!-- Add check in markup to remove the button if the podcast already exists in the user's list -->
    <div v-if="isInUserPodcasts" class="in-podcasts">In Your Podcasts</div>
    <button v-else class="" @click="addPodcast">Add to My Podcasts</button>
  </div>
</template>

<script>
// importing computed
import { ref, computed } from "vue";
import { store } from "../store";
import { supabase } from "../supabase";

export default {
  props: {
    podcast: {
      type: Object,
      required: true,
    },
  },
  setup(props) {
    // add computed property checking if podcast is in user's podcasts
    const isInUserPodcasts = computed(() => {
      return store.state.podcasts.some(
        (podcast) => podcast.rss_url === props.podcast.rss_url
      );
    });

    function addPodcast() {
      // check if podcast is already in user's podcasts
      if (isInUserPodcasts.value) {
        alert("You already have this podcast in your list!");
      } else {
        const podcast = {
          name: props.podcast.title,
          image_url: props.podcast.image_url,
          description: props.podcast.description,
          rss_url: props.podcast.rss_url,
          user_id: store.state.user.id,
        };
        supabase
          .from("podcasts")
          .insert(podcast)
          .then(({ body }) => {
            store.addPodcastToStore(body[0]);
          })
          .catch((err) => {
            console.log(err);
          });
      }
    }

    return {
      // exposing the isInUserPodcasts computed property
      isInUserPodcasts,
      addPodcast,
    };
  },
};
</script>

<style scoped></style>

```

Next, we want to display a list of podcasts that the user has added to their library. We have the list in the global store, so we just need to loop through them to display the needed info. 

Add the following to the bottom of the `PodcastFeed.vue` template:

```html
<!-- Loop through podcasts and display them -->
  <div class="feeds">
    <h2 class="">Your Podcast Feeds</h2>
    <ul class="">
      <li v-for="pod in store.state.podcasts" :key="pod.id" class="">
        <a :href="`/podcast/${pod.id}`" class="">
          <img :src="pod.image_url" :alt="`logo for ${pod.name}`" class="" />
          <p class="">{{ pod.name }}</p>
        </a>
      </li>
    </ul>
  </div>
```

## How to Set Up the Other Pages for Our Podcast App

Now that we have the list of podcasts being displayed in the app, we need a way to navigate to an individual podcast. We have the markup set to link to a path like `/podcast/{podcast_id}`. Now we need to update our app to handle routes like this. 

First, install vue-router using `npm i vue-router`.

Then create a file called `router.js` with the following code:

```js
// Import Vue Router
import * as VueRouter from "vue-router";

// Import the components that will show on the different routes
import PodcastFeed from "./components/PodcastFeed.vue";
import PodcastDetail from "./components/PodcastDetail.vue";

// Set up the routes
const routes = [
  { path: "/", component: PodcastFeed },
  { path: "/podcast/:id", component: PodcastDetail },
];

// Initialize the router
const router = VueRouter.createRouter({
  history: VueRouter.createWebHistory(),
  routes,
});

// Export the router
export default router;

```

Update `main.js` to use the router in the Vue app:

```js
import { createApp } from "vue";
import router from "./router";
import App from "./App.vue";
import "./index.css";

const app = createApp(App);
app.use(router);
app.mount("#app");
```

Update `App.vue` to show the `router-view` component provided by Vue Router:

```html
<template>
  <button v-if="store.state.user" class="signout-button" @click="signOut">Sign Out</button>
  <!-- Check if user is available in the store, if not show auth compoenent -->
  <Auth v-if="!store.state.user" />
  <!-- If user is available, show the app -->
  <div v-else class="app">
    <router-view></router-view>
  </div>
</template>
```

Now create a `PodcastDetail.vue` file that will display the episode info for the podcast:

```js
<template>
  <nav class="">
    <a href="/" class="">Home</a>
  </nav>
  <!-- Basic layout for showing podcast info -->
  <div class="podcast-detail">
    <img :src="podcast.image_url" :alt="podcast.name" class="" />
    <h1 class="">{{ podcast.name }}</h1>
    <p>{{ podcast.description }}</p>
    <h2 class="">Episodes</h2>
    <!-- Looping through each episode of a podcast and displaying episode info -->
    <ul class="">
      <li
        v-for="episode in episodes"
        :key="episode.guid || episode.link"
        class=""
      >
        <div class="info">
          <h3>{{ episode.title }}</h3>
          <audio class="" controls>
            <source :src="episode.url" type="audio/mpeg" />
            Display
          </audio>          
        </div>        
      </li>
    </ul>
  </div>
</template>

<script>
// Importing necessary methods
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";
import { supabase } from "../supabase";

export default {
  setup() {
    const route = useRoute();
    const podcast = ref({});
    const episodes = ref([]);

    // Getting podcast info from the database
    async function getPodcastData() {
      const {
        data: [podcastinfo],
      } = await supabase.from("podcasts").select().eq("id", route.params.id);
      podcast.value = podcastinfo;

      // Making call to episode url to get episode info
      getEpisodes(podcastinfo.rss_url);
    }

    function getEpisodes(url) {
      fetch(url)
        .then((response) => response.text())
        .then((str) => new window.DOMParser().parseFromString(str, "text/xml"))
        .then((data) => {
          // Finding all the "item" tags in the xml response which will contain the episode info
          const items = data.querySelectorAll("item");
          // Looping through each item and getting the episode info and pushing it to the 'episodes' array
          items.forEach((item) => {
            let url;

            // Not every podcast episode is going to have the `enclosure` tag, so we need to check if it exists
            try {
              url = item.querySelector("enclosure").getAttribute("url");
            } catch (e) {
              console.log("error", e);
              url = item.querySelector("link").innerHTML;
            }

            episodes.value.push({
              // this `title` and the `guid` properties looks a little different because the title contains CDATA tags which need to be grabbed with the 'childNodes' property
              title: item.querySelector("title").childNodes[0].textContent,
              link: url,
              url: url,
              description: item.querySelector("description").innerHTML,
              pubDate: item.querySelector("pubDate").innerHTML,
              guid: item.querySelector("guid").childNodes[0].textContent,
            });
          });
        })
        .catch((err) => {
          alert("Couldn't get episodes", err);
        });
    }

    onMounted(() => {
      // Getting podcast info from the database once the component is mounted
      getPodcastData();
    });

    return {
      podcast,
      episodes,
    };
  },
};
</script>

<style scoped></style>

```

With those changes, we can now see the individual episodes of the podcast and can play them using the `<audio>` html tag. 

## How to Get the Transcriptions of the Podcasts

The last step is to get transcriptions for the podcasts, and then save them to our database.

If you haven't yet, you'll need to get a [free API key from Deepgram](https://console.deepgram.com/signup) in order to process the audio and get the transcriptions. 

Once you get the API key, add it to your `.env.local` file as `VITE_DEEPGRAM_KEY`. Make sure you restart your dev server here, otherwise you'll probably get a 403 Forbidden error when we finally call the API.

Then add this code to a deepgram.js file in the `src` folder.

```js
const deepgramKey = import.meta.env.VITE_DEEPGRAM_KEY;

async function deepgram(url) {
  const response = await fetch(
    "https://api.deepgram.com/v1/listen?punctuate=true&diarize=true&utterances=true",
    {
      method: "POST",
      headers: {
        Authorization: `Token ${deepgramKey}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        url: url,
      }),
    }
  );
  const json = await response.json();
  return json.results;
}

export default deepgram;

```

This gives us a utility function we can import into our app in other files to call the Deepgram API in order to get the transcriptions. We added the punctuate, diarize, and utterances to the URL as parameters to get a cleaner transcription that is easier to read. 

Now that we have that, we need to add some functionality to the `PodcastDetail.vue` file. I'll walk through the changes and then later will put up the final code for the file.

First we need to have some state to keep track of the transcriptions we get, and also to have some loading state once we click a button to get a transcription. So we'll add these two lines to our setup function:

```js
let transcriptions = ref({});
const episodeTranscriptionLoading = ref([]);
```

Don't forget to add them to the return object of the `setup` function.

Then add this function to make the request to Deepgram, and then add the transcription to the local `transcriptions` object.

```js
// Function to get a transcription from Deepgram, passing in the episode url
async function getTranscription(episode) {
    // setting the loading state to true for the episode
    episodeTranscriptionLoading.value.push(episode.guid);
    const transcription = await deepgram(episode.url);
    // setting a unique id for the episode transcription
    transcriptions.value[`${podcast.value.id}---${episode.guid}`] =
        transcription;
    // removing the loading state for the episode
    episodeTranscriptionLoading.value.splice(
        episodeTranscriptionLoading.value.indexOf(episode.guid),
        1
    );
}
```

Make sure you import the deepgram function from `deepgram.js` at the top of the script tag.

Then update the template to this:

```html
<template>
  <nav class="">
    <a href="/" class="">Home</a>
  </nav>
  <!-- Basic layout for showing podcast info -->
  <div class="podcast-detail">
    <img :src="podcast.image_url" :alt="podcast.name" class="" />
    <h1 class="">{{ podcast.name }}</h1>
    <p>{{ podcast.description }}</p>
    <h2 class="">Episodes</h2>
    <!-- Looping through each episode of a podcast and displaying episode info -->
    <ul class="">
      <li
        v-for="episode in episodes"
        :key="episode.guid || episode.link"
        class=""
      >
        <div class="info">
          <h3>{{ episode.title }}</h3>
          <audio class="" controls>
            <source :src="episode.url" type="audio/mpeg" />
            Display
          </audio>
            <!-- button to get transcriptions -->
          <button
            v-if="!transcriptions[`${podcast.id}---${episode.guid}`]"
            @click.prevent="getTranscription(episode)"
            class=""
          >
            {{
              episodeTranscriptionLoading.includes(episode.guid)
                ? "Loading..."
                : "Get Transcription"
            }}
          </button>
        </div>
          <!-- box to display the transcription -->
        <div
          v-if="transcriptions[`${podcast.id}---${episode.guid}`]"
          class="transcription"
        >
          <p>
            {{
              transcriptions[`${podcast.id}---${episode.guid}`].channels[0]
                .alternatives[0].transcript
            }}
          </p>
        </div> 
      </li>
    </ul>
  </div>
</template>
```

## How to Save the Transcriptions

Now that we can get the transcriptions, we need to add the functionality to save them to Supabase. 

First, go create a table in Supabase like we did above, but this time name the table `transcriptions`. You'll want the following as the columns:

* **id** – varchar (primary) Also remove the "Is Identity" check mark in the settings for this column
* **podcast_id** – int8
* **episode_guid** – varchar
* **transcript** – text
* **user_id** – uuid (You'll need to link this to the user table by clicking on the link icon)
* **created_at** – timestamptz

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screen-Shot-2022-02-22-at-4.40.52-PM.png)
_columns for transcriptions table_

Once that table is set up, we can add a reactive property called `savedTranscriptions` to the component and then add the following code to save the transcriptions to Supabase. Then we'll store them in the object `savedTranscriptions`.

```js
function saveTranscription(podcastId, episodeGuid) {
    supabase
        .from("transcriptions")
        .insert({
        id: `${podcastId}---${episodeGuid}`,
        podcast_id: podcastId,
        episode_guid: episodeGuid,
        transcript:
        transcriptions.value[`${podcastId}---${episodeGuid}`].channels[0]
        .alternatives[0].transcript,
        user_id: store.state.user.id,
    })
        .then(({ data: [transcriptObject] }) => {
        savedTranscriptions.value[transcriptObject.id] =
            transcriptObject.transcript;
    });
}
```

Once a user has a transcription saved, we need to display it whenever they re-visit a page. Add this function to get that data from Supabase:

```js
async function getTranscriptions() {
    const { data: transcriptions } = await supabase
    .from("transcriptions")
    .select()
    .eq("podcast_id", podcast.value.id);
    console.log("Transcriptions", transcriptions);
    transcriptions.forEach((transcript) => {
        console.log("id", transcript.id);
        savedTranscriptions.value[transcript.id] = transcript.transcript;
    });
}
```

We will want this called whenever a user hits this page, but not until we get the podcast information. Add a call to `getTranscriptions` to the bottom of the `getPodcastData` function to do that.

The last thing to do is to update the template to include the save buttons and to display transcriptions if they are in the saved objects. The final code for the `PodcastDetail.vue` should then look like this:

```js
<template>
  <nav class="">
    <a href="/" class="">Home</a>
  </nav>
  <!-- Basic layout for showing podcast info -->
  <div class="podcast-detail">
    <img :src="podcast.image_url" :alt="podcast.name" class="" />
    <h1 class="">{{ podcast.name }}</h1>
    <p>{{ podcast.description }}</p>
    <h2 class="">Episodes</h2>
    <!-- Looping through each episode of a podcast and displaying episode info -->
    <ul class="">
      <li
        v-for="episode in episodes"
        :key="episode.guid || episode.link"
        class=""
      >
        <div class="info">
          <h3>{{ episode.title }}</h3>
          <audio class="" controls>
            <source :src="episode.url" type="audio/mpeg" />
            Display
          </audio>
          <button
            v-if="savedTranscriptions[`${podcast.id}---${episode.guid}`]"
            disabled
          >
            Transcription Saved
          </button>
          <button
            v-else-if="
              !transcriptions[`${podcast.id}---${episode.guid}`] &&
              !savedTranscriptions[`${podcast.id}---${episode.guid}`]
            "
            @click.prevent="getTranscription(episode)"
            class=""
          >
            {{
              episodeTranscriptionLoading.includes(episode.guid)
                ? "Loading..."
                : "Get Transcription"
            }}
          </button>
          <button
            v-if="
              transcriptions[`${podcast.id}---${episode.guid}`] &&
              !savedTranscriptions[`${podcast.id}---${episode.guid}`]
            "
            class="save"
            @click.prevent="saveTranscription(podcast.id, episode.guid)"
          >
            Save Transcription
          </button>
        </div>
        <div
          v-if="savedTranscriptions[`${podcast.id}---${episode.guid}`]"
          class="transcription"
        >
          <p>
            {{ savedTranscriptions[`${podcast.id}---${episode.guid}`] }}
          </p>
        </div>
        <div
          v-else-if="transcriptions[`${podcast.id}---${episode.guid}`]"
          class="transcription"
        >
          <p>
            {{
              transcriptions[`${podcast.id}---${episode.guid}`].channels[0]
                .alternatives[0].transcript
            }}
          </p>
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
// Importing necessary methods
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";
import { supabase } from "../supabase";
import { store } from "../store";
import deepgram from "../deepgram";

export default {
  setup() {
    const route = useRoute();
    const podcast = ref({});
    const episodes = ref([]);
    let transcriptions = ref({});
    let savedTranscriptions = ref({});
    const episodeTranscriptionLoading = ref([]);

    // Getting podcast info from the database
    async function getPodcastData() {
      const {
        data: [podcastinfo],
      } = await supabase.from("podcasts").select().eq("id", route.params.id);
      podcast.value = podcastinfo;

      // Making call to episode url to get episode info
      getEpisodes(podcastinfo.rss_url);
      await getTranscriptions();
    }

    function getEpisodes(url) {
      fetch(url)
        .then((response) => response.text())
        .then((str) => new window.DOMParser().parseFromString(str, "text/xml"))
        .then((data) => {
          // Finding all the "item" tags in the xml response which will contain the episode info
          const items = data.querySelectorAll("item");
          // Looping through each item and getting the episode info and pushing it to the 'episodes' array
          items.forEach((item) => {
            let url;

            // Not every podcast episode is going to have the `enclosure` tag, so we need to check if it exists
            try {
              url = item.querySelector("enclosure").getAttribute("url");
            } catch (e) {
              console.log("error", e);
              url = item.querySelector("link").innerHTML;
            }

            episodes.value.push({
              // this `title` and the `guid` properties looks a little different because the title contains CDATA tags which need to be grabbed with the 'childNodes' property
              title: item.querySelector("title").childNodes[0].textContent,
              link: url,
              url: url,
              description: item.querySelector("description").innerHTML,
              pubDate: item.querySelector("pubDate").innerHTML,
              guid: item.querySelector("guid").childNodes[0].textContent,
            });
          });
        })
        .catch((err) => {
          alert("Couldn't get episodes", err);
        });
    }

    // Function to get a transcription from Deepgram, passing in the episode url
    async function getTranscription(episode) {
      // setting the loading state to true for the episode
      episodeTranscriptionLoading.value.push(episode.guid);
      const transcription = await deepgram(episode.url);
      // setting a unique id for the episode transcription
      transcriptions.value[`${podcast.value.id}---${episode.guid}`] =
        transcription;
      // removing the loading state for the episode
      episodeTranscriptionLoading.value.splice(
        episodeTranscriptionLoading.value.indexOf(episode.guid),
        1
      );
    }

    function saveTranscription(podcastId, episodeGuid) {
      console.log(
        "saving transcription",
        transcriptions.value[`${podcastId}---${episodeGuid}`]
      );
      supabase
        .from("transcriptions")
        .insert({
          id: `${podcastId}---${episodeGuid}`,
          podcast_id: podcastId,
          episode_guid: episodeGuid,
          transcript:
            transcriptions.value[`${podcastId}---${episodeGuid}`].channels[0]
              .alternatives[0].transcript,
          user_id: store.state.user.id,
        })
        .then(({ data: [transcriptObject] }) => {
          console.log("saved", transcriptObject);
          savedTranscriptions.value[transcriptObject.id] =
            transcriptObject.transcript;
        });
    }

    async function getTranscriptions() {
      const { data: transcriptions } = await supabase
        .from("transcriptions")
        .select()
        .eq("podcast_id", podcast.value.id);
      console.log("Transcriptions", transcriptions);
      transcriptions.forEach((transcript) => {
        console.log("id", transcript.id);
        savedTranscriptions.value[transcript.id] = transcript.transcript;
      });
    }

    onMounted(() => {
      // Getting podcast info from the database once the component is mounted
      getPodcastData();
    });

    return {
      podcast,
      episodes,
      transcriptions,
      savedTranscriptions,
      episodeTranscriptionLoading,

      getTranscription,
      saveTranscription,
    };
  },
};
</script>

<style scoped></style>

```

## Conclusion

If you've followed the steps above, you should have a working app. [Here is the final code](https://github.com/briancbarrow/vue-supabase-auth/tree/final-podcast-feed-transcriptions) if you want to double check against what I have written.

I know I enjoyed making the app. Supabase makes it really easy to get a database/backend up and running. Please reach out to me on [Twitter](https://twitter.com/the_BrianB) if you have any questions!

