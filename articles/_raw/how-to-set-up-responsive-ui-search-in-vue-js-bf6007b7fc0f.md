---
title: How to set up responsive UI search in Vue.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-14T16:55:04.000Z'
originalURL: https://freecodecamp.org/news/how-to-set-up-responsive-ui-search-in-vue-js-bf6007b7fc0f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*557yKFY9udPu1QV2_bW9Kw.jpeg
tags:
- name: Front-end Development
  slug: front-end-development
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: vue
  slug: vue
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Honey Thakuria

  Are you thinking of building something awesome with one of the popular modern frameworks
  out there right now, but don’t know how to get started?

  If yes, then this post will help you get a kick started and build something awesome.


  W...'
---

By Honey Thakuria

Are you thinking of building something awesome with one of the popular modern frameworks out there right now, but don’t know how to get started?

If yes, then this post will help you get a kick started and build something awesome.

> **What are we going to build?**

We will be building a responsive client side search of the 7 wonders of the world with the following features:

1. **Text Search** & **Filters** based on Ratings and Likes.
2. 2 items per row for **Tablet** and **Desktop**, 1 item per row for **Mobile**.
3. Fetching data asynchronously from external API on client side.
4. Responsive view as shown below:

![Image](https://cdn-media-1.freecodecamp.org/images/NAceF0rPfr0FHFAl-m0NW-BDBQrR-6YNcDG-)

![Image](https://cdn-media-1.freecodecamp.org/images/3bxyozgrAJ45A1n9pRysRELj3cweirUBIdTu)
_Left is Dektop / Tablet view and right is the Mobile view_

**Live Demo**: [https://vue-responsive-search.herokuapp.com](https://vue-responsive-search.herokuapp.com/)

**Source Code**: [https://github.com/honey93/VueSearchExample](https://github.com/honey93/VueSearchExample)

#### **Tech Architecture**

We will be working with the following technologies:

1. [**Vue.js**](https://vuejs.org/)**:** The Progressive JavaScript Framework
2. [**BootstrapVue**](https://bootstrap-vue.js.org/)**:** It provides one of the most comprehensive implementations of Bootstrap V4 components and grid system available for Vue.js 2.5+, complete with extensive and automated WAI-ARIA accessibility markup.
3. [**Vue Cli 3**](https://cli.vuejs.org/)**:** Standard Tooling for Vue.js Development

#### **Project Structure**

To get started with our Vue project, we need to setup many things like Vue, Bootstrap, Vue Router, Vuex, etc.

Vue Cli provides us the command to create the project with most of the needed configurations.

```
npm install -g @vue/cli
vue create project-name
```

For the remaining things like BootstrapVue, vue-star-rating, etc, we can use the npm install command.

The default project created using vuecli has the following structure:

```
/Root Folder 
 
 Public/

 src/
  
  assets/  /* Static assets like images goes here */
  components/ /* Small part of a view */
  views/  /* View represents a page composed of several components*/
  App.vue /* The main view inside which the routing logic goes */
  main.js  /* App initialisation happens here  */
  router.js /* Router logic is defined here */
  store.js /* Optional state management library Vuex */

 package.json /* It consist of all the dependencies of the project. */
 ......
```

The above things are there to explain the project architecture to you and the way to initialise it.

We can get started by cloning the [**repository**](https://github.com/honey93/VueSearchExample) and writing the following commands:

```
npm install 
npm run serve 
```

Some important components explained:

**components/Header.vue**

The header has been created in the form of a single independent component so that it can be reused across pages, avoiding duplication of the code.

```
/* Vue style of writing component: template, script and style*/
<template>
  <div class="pad-15-hor pad-15-ver header">
    <div>
      <img src="@/assets/logo.png" width="25px"> Responsive Search
    </div>
    <div>
      <i class="fas fa-bars"></i>
    </div>
  </div>
</template>
<script>
export default {
  name: "Header"
};
</script>
<style scoped>
.header {
  display: flex;
  flex-flow: row wrap;
  justify-content: space-between;
}
</style>
```

**components/Main.vue**

This component consist of the entire logic of search / filters and display of results fetched from the API.

This component is using the above Header by importing it in the script.

```
<template>
  <div>
    <Header/>
    <div class="pad-15-hor pad-15-ver search-parent">
      <div class="search-bar">
        <b-form-input
          @input="search_text()"
          v-model="search.text"
          type="text"
          placeholder="Search by Name"
        ></b-form-input>
        <span class="search-icon">
          <i class="fas fa-search"></i>
        </span>
      </div>
      <div>
        <span class="bold">Total Likes:</span>
        {{likes.count}}
        <span class="bold">Hits:</span>
        {{likes.hit}}
      </div>
      <div>
        <b-form-select @input="sort()" v-model="search.filter" :options="options"/>
      </div>
    </div>
<div class="container-fluid">
      <div class="row">
        <div class="col-md-6 pad-15-ver" v-for="wonder in wonders_data" :key="wonder.id">
          <div
            class="card-inner"
            @mouseover="show_hover(true,wonder.id)"
            @mouseout="show_hover(false,0)"
          >
            <img class="card-img" :src="wonder.imageURL">
<div class="card-bottom pad-15-hor" v-show="!hover_flag || active_id != wonder.id">
              <div class="min-width-160">
                <span class="bold">Ratings:</span>
                <star-rating
                  :rating="wonder.ratings"
                  :show-rating="false"
                  :inline="true"
                  :star-size="15"
                ></star-rating>
              </div>
              <div class="max-width-160">
                <span class="bold">{{wonder.place}}</span>
              </div>
            </div>
<div :class="{'card-hover':1}" v-show="hover_flag && active_id == wonder.id">
              <span
                @click="make_active(wonder.id)"
                :class="{'fas':1, 'fa-heart':1, 'absolute-star':1, 'green':check_active(wonder.id)}"
              >{{wonder.likes}}</span>
              <h5>{{wonder.place}}</h5>
              <p>{{wonder.description}}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
/* Importing Header to use in this component */ 
import Header from "@/components/Header.vue";
/* Importing axios for async REST calls */
import axios from "axios";
export default {
  name: "Main",
/* mounted gets called when the component gets mounted. AJAX calls are preferred in mounted lifecycle method */
  mounted() {
    this.hover_flag = false;
var inside = this;
axios
      .get("https://www.mocky.io/v2/5c7b98562f0000c013e59f07")
      .then(function(response) {
        //console.log(response);
inside.wonders_data_actual = response.data.data;
response.data.data.map(function(wonder) {
          inside.likes.count += wonder.likes;
        });
inside.wonders_data_actual = inside.wonders_data_actual.map(function(
          wonder
        ) {
          wonder.active_like = false;
          return wonder;
        });
        inside.wonders_data = response.data.data;
      })
      .catch(function(error) {
        // console.log(error);
      });
  },
/* All the data variable declaration are done here:  */
  data() {
    return {
      hover_flag: false,
      wonders_data_actual: [],
      wonders_data: [],
      active_id: 0,
      options: [
        { value: null, text: "Sort By" },
        { value: "a", text: "Ratings" },
        { value: "b", text: "Likes" }
      ],
      search: { filter: null, text: "" },
      likes: { count: 0, hit: 0 }
    };
  },
/* Methods are defined here */
  methods: {
    show_hover(flag, active_id) {
      this.hover_flag = flag;
      this.active_id = active_id;
    },
    sort() {
      //console.log(this.search.filter);
      this.search.filter == "b"
        ? this.wonders_data.sort(function(a, b) {
            return b.likes - a.likes;
          })
        : this.wonders_data.sort(function(a, b) {
            return b.ratings - a.ratings;
          });
    },
    search_text() {
      //console.log(this.search.text);
var inside = this;
this.wonders_data = this.wonders_data_actual.filter(function(wonder) {
        if (
          wonder.place
            .toLowerCase()
            .indexOf(inside.search.text.toLowerCase()) != "-1"
        ) {
          return wonder;
        }
      });
    },
    check_active(id) {
      var flag = false;
      this.wonders_data_actual.map(function(wonder) {
        if (wonder.id == id) {
          flag = wonder.active_like;
        }
      });
      return flag;
    },
    make_active(id) {
      this.likes.hit++;
      this.wonders_data_actual = this.wonders_data_actual.map(function(wonder) {
        if (wonder.id == id) {
          wonder.active_like = !wonder.active_like;
          wonder.active_like ? wonder.likes++ : wonder.likes--;
        }
return wonder;
      });
      var inside = this;
inside.likes.count = 0;
      this.wonders_data_actual.map(function(wonder) {
        inside.likes.count += wonder.likes;
      });
    }
  },
  components: {
    Header
  }
};
</script>
<style scoped> /* Styles are scoped to this component only.*/
/* Style for Desktop/Tablet  */
.search-parent {
  display: flex;
  flex-flow: row wrap;
  justify-content: space-between;
  background-color: lightgray;
}
.card-inner {
  position: relative;
  overflow: hidden;
  box-shadow: 2px 2px 8px grey;
}
.card-img {
  width: 100%;
}
.card-bottom {
  position: absolute;
  bottom: 0;
  left: 0;
  height: 30px;
  width: 100%;
  background-color: white;
  opacity: 0.7;
  display: flex;
  justify-content: space-between;
}
.card-hover {
  position: absolute;
  right: 15px;
  left: 15px;
  top: 15px;
  bottom: 15px;
  background-color: white;
  opacity: 0.7;
  display: flex;
  flex-flow: column wrap;
  justify-content: center;
  align-items: center;
}
.absolute-star {
  position: absolute;
  top: 10px;
  right: 10px;
}
.card-hover p {
  font-size: 10px;
  text-align: center;
}
.bold {
  font-weight: 500;
}
.rating-div {
  width: 200px;
}
.search-bar {
  position: relative;
}
.search-bar input {
  padding-left: 30px;
}
.search-icon {
  position: absolute;
  top: 8px;
  left: 8px;
}
/* For Mobile Device, we will be going with column wrap approach */
@media screen and (max-width: 550px) {
  .search-parent {
    display: flex;
    flex-flow: column wrap;
    justify-content: center;
    align-items: center;
    background-color: lightgray;
  }
.search-parent div {
    width: 100%;
    text-align: center;
  }
}
</style>
```

I hope you have a better understanding of how to get started with Vue and create something awesome.

If you found this helpful, **clap** below, give **stars** to the project [**repo**](https://github.com/honey93/VueSearchExample) and share with your friends too.

