---
title: Learn Vuex in 5 minutes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-28T20:37:58.000Z'
originalURL: https://freecodecamp.org/news/learn-vuex-in-5-minutes
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/learn-vuex.png
tags:
- name: vue
  slug: vue
- name: Vuex
  slug: vuex
seo_title: null
seo_desc: 'By Per Harald Borgen

  This tutorial will give you a basic understanding of Vuex by building a plan-making
  application. A user can type in activities and then vote how much they like/dislike
  them.

  Once you''ve read this tutorial, you can check out our f...'
---

By Per Harald Borgen

This tutorial will give you a basic understanding of Vuex by building a plan-making application. A user can type in activities and then vote how much they like/dislike them.

Once you've read this tutorial, you can check out our [free Vuex course on Scrimba](https://scrimba.com/g/gvuex), if you're interested in learning more.

What is Vuex? From [Vue's official documentation](https://vuex.vuejs.org)

```
Vuex is a state management pattern + library for Vue.js applications.
It serves as a centralized store for all the components in an application, with rules ensuring that the state can only be mutated in a predictable fashion.

```

This course assumes that you're somewhat familiar with Vue and we will briefly touch on features like `props`, components and bindings, but will not review them in great detail. If you'd like to have a quick primer on Vue, feel free to [check out this course on Scrimba](https://scrimba.com/p/pXKqta).

# The setup

At Scrimba, complicated setups are something we just don't do.  
For this tutorial, we've created a simple HTML file where everything can be written. Feel free to write your own CSS or just copy it from [this playground](https://scrimba.com/c/c66qG4uG)

Vue and Vuex libraries are imported via CDN using `<script>` tags:

```html
<!DOCTYPE html>
<html lang="en">
  <head>

    <title>Activity Voter</title>

    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/vuex/dist/vuex.js"></script>
    <style>
      /*
        ADD CSS HERE
      */
    </style>
  </head>
  <body>
    <div id="app"></div>
  </body>

  <script>
    /*
      ADD VUE CODE HERE
    */
  </script>
</html>

```

Alternatively, you can also experiment with the code in [this Vue Scrimba playground](https://scrimba.com/c/cqRNMEcG) Just remember to **relink the playground to your own account.**

# App plan

We're going to build a voting app, that works especially well when you're in a group of friends not knowing what to do and you have to consider all the options.

The functionality will consist of a user being able to type in an activity and then each activity will have a vote up and down button to count up the totals.

# Getting started

First, let's quickly mock our app up in HTML. We will use this layout to then extract into a separate component and we will add functionality for the layout to come to life.

```html
<div id="app">
  <h1>Activity voter</h1>
  <form>
    <input type="text" placeholder="Add Activity" />
    <button id="button">Add Activity</button>
  </form>
  <ul>
    <li>
      <span>
Go Snowboarding</span>
<span>?</span>
        <button>?</button>
        5
        <button>?</button>
      </span>
    </li>
  </ul>
</div>

```

![Image](https://thepracticaldev.s3.amazonaws.com/i/42ixhwdzkncbibp1m210.png)

# Add Vuex store with some basic data

Vuex starts with the store. The store is where we keep (store) our state.

```html
<script>
  Vue.use(Vuex);

  const store = new Vuex.Store({

  });

  new Vue({
    el: "#app",
    store
  });
</script>


```

Let's also add some hard-coded data to the store, that will include one activity and an array with one emoji to display our feelings towards the activity.

```html
<script>
  Vue.use(Vuex);

  const store = new Vuex.Store({
    state: {
      activities: [{ name: "go snowboarding", rating: 5 }],
      emojis: ["?"]
    }
  });

  new Vue({
    el: "#app",
    store
  });
</script>


```

To allow our state to change reactively, we can use Vuex `mapState` to handle computed state properties for us.

```js
  new Vue({
    el: "#app",
    store,
    computed: Vuex.mapState(["activities", "emojis"])
  });


```

# Add component

Now we have activities inside our state. Let's render a separate component for each of those activities. Each one will need `activity` and `emojis` props.

```js
Vue.component("activity-item", {
  props: ["activity", "emojis"],
  template: `
    <li>
      <span>{{ activity.name }}
        <span>{{ emojis[0] }}</span>
        <button>?</button>
        {{activity.rating}}
        <button>?</button>
      </span>
    </li>
    `
});

```

Inside `app` we can now use our newly created component with all the appropriate bindings for `activity` and emojis. As a quick reminder, if we want to loop over an array and display a component for each item in an array, in Vue, we can use `v-for` binding.

```html
<div id="app">
  <h1>Activity voter</h1>
  <form>
    <input type="text" placeholder="Add Activity" />
    <button id="button">Add Activity</button>
  </form>
  <ul>
    <activity-item
      v-for="item in activities"
      v-bind:activity="item"
      v-bind:emojis="emojis"
      v-bind:key="item.name">
</activity-item>

</ul>
</div>

```

![Image](https://thepracticaldev.s3.amazonaws.com/i/42ixhwdzkncbibp1m210.png)

# Add mutations to store

If we want to update the store in Vuex, we can use mutations. At the moment we will just `console.log` that a mutation happened and we will implement it afterwards.

```js
const store = new Vuex.Store({
  state: {
    activities: [
      { name: "go snowboarding", rating: 5 },
    ],
    emojis: ["?"]
  },
  mutations: {
    increment(state, activityName) {
      console.log('increment');
    },
    decrement(state, activityName) {
      console.log('decrement');
    },
  }
});

```

How do we trigger a mutation? We call a `commit` function on `$store` with the name of mutations we want to be executed. Any arguments after the name of a mutation are treated as arguments to a committed mutation.

```js
new Vue({
  el: "#app",
  store,
  data() {
    return {
      activityName: ""
    };
  },
  computed: Vuex.mapState(["activities", "emojis"]),
  methods: {
    increment(activityName) {
      this.$store.commit("increment", activityName);
    },
    decrement(activityName) {
      this.$store.commit("decrement", activityName);
    }
  }
});

```

# Add functionality to component

Each `activity-item` has voting buttons that need to `increment` and `decrement` on click of a button. We can pass these functions as props. Let's now bind our methods to props.

```html
<activity-item
  v-for="item in activities"
  v-bind:increment="increment"
  v-bind:decrement="decrement"
  v-bind:activity="item"
  v-bind:emojis="emojis"
  v-bind:key="item.name">
</activity-item>


```

Let's also not forget to provide `activity.name` as an argument to both.

```js
Vue.component("activity-item", {
  props: ["activity", "emojis", "increment", "decrement"],
  template: `
    <li>
      <span>{{ activity.name }}
          <span>{{ emojis[0] }}</span>
          <button @click="decrement(activity.name)">?</button>
          {{activity.rating}}
          <button @click="increment(activity.name)">?</button>
      </span>
    </li>
    `
});

```

And there we go! The flow is working. We can see the `console.log` statement in the console.  


![Image](https://thepracticaldev.s3.amazonaws.com/i/2spr4ea73npem7pyv05h.png)

# Implement counter

Let's implement the counter. First, we need to find an activity by its name, and then update its rating.

```js
  mutations: {
    increment(state, activityName) {
      state.activities
        .filter(activity => activity.name === `${activityName}`)
        .map(activity => activity.rating++);
    },
    decrement(state, activityName) {
      state.activities
        .filter(activity => activity.name === `${activityName}`)
        .map(activity => activity.rating--);
    }
  }

```

Perfect, we can now vote on activities.  


![Image](https://thepracticaldev.s3.amazonaws.com/i/eh23lvlqaszxq0rxmkel.png)

# Use form input to add activity

But of course, we need to be able to add activities too.

Let's create a mutation to the store, that would add an activity to the list of existing activities, with a name that we will later get from the input and a default rating of 0.

```js
 mutations: {
    ...
    addActivity(state, name) {
      state.activities.push({ name, rating: 0 });
    }
  }

```

Inside methods, we can commit a new activity to the store.

```js
methods: {
    ...
    addActivity(activityName) {
      this.$store.commit("addActivity", activityName);
    }
  }

```

# Implement form submission

Let's wire up the submit function to our HTML form.

```html
<form @submit="onSubmit">
  <input type="text" placeholder="Add Activity" v-model="activityName" />
  <button id="button">Add Activity</button>
</form>

```

We can now add our submit function to methods. Inside, we're going to use our existing `addActivity` method and in the end, reset `activityName` in the input field to an empty string.

```js
methods: {
    ...
    onSubmit(e) {
      e.preventDefault();
      this.addActivity(this.activityName);
      this.activityName = "";
    }
  }

```

We call `e.preventDefault()` to avoid the form from reloading on each addition of a new activity.

![Image](https://thepracticaldev.s3.amazonaws.com/i/qsnc185pcchj71c6878i.png)

All the counters now work and the field gets updated. It does look a bit strange, that we have only one emotion for all the activities, no matter what their rating is.

Let's rewrite emojis into an object with some description of what moods they are meant to reflect and clean up existing state, so we start from no activities.

```js
state: {
    activities: [],
    emojis: { yay: "?", nice: "?", meh: "?", argh: "?", hateIt: "?"}
},
...

```

And as a finishing touch, we can display different emojis depending on the rating an activity has.

```js
Vue.component("activity-item", {
  props: ["activity", "emojis", "increment", "decrement"],
  template: `
    <li>
      <span>{{ activity.name }}
        <span v-if="activity.rating <= -5">{{ emojis.hateIt }}</span>
        <span v-else-if="activity.rating <= -3">{{ emojis.argh }}</span>
        <span v-else-if="activity.rating < 3">{{ emojis.meh }}</span>
        <span v-else-if="activity.rating < 5">{{ emojis.nice }}</span>
        <span v-else>{{ emojis.yay }}</span>
        <button @click="decrement(activity.name)">?</button>
          {{activity.rating}}
        <button @click="increment(activity.name)">?</button>
      </span>
    </li>
    `
});

```

We start with a blank app, which is what we wanted.  


![Image](https://thepracticaldev.s3.amazonaws.com/i/7izt1gxbmnje90fiv9gq.png)

And now if we add back the two activities we used to have in the app, vote on the ratings we have emojis that reflect how we feel about the activities!  


![Image](https://thepracticaldev.s3.amazonaws.com/i/hclj6218rr3pxe5pnv19.png)

You can check out the full code [here.](https://gist.github.com/perborgen/ce11d4f36cfb97f2ddb15ae73bfa10dd)

