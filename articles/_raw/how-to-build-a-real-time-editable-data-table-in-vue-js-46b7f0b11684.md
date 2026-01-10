---
title: How to build a real-time editable data table in Vue.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-22T19:56:01.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-real-time-editable-data-table-in-vue-js-46b7f0b11684
coverImage: https://cdn-media-1.freecodecamp.org/images/1*1LI9TzwDU1l6IyJFBRcULw.jpeg
tags:
- name: data
  slug: data
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Vue.js
  slug: vuejs
seo_title: null
seo_desc: 'By Peter Mbanugo

  In data-driven applications, a data table is used to display data in a tabular format
  with the ability to edit and delete records in place. When you’re working with Vue,
  there are different open-sourced components that can be used to...'
---

By Peter Mbanugo

In data-driven applications, a data table is used to display data in a tabular format with the ability to edit and delete records in place. When you’re working with [Vue](https://vuejs.org/), there are [different open-sourced components](https://github.com/vuejs/awesome-vue#table) that can be used to easily add a data table to your application.

Many applications today have real-time features, and you may wonder how you can synchronize editing and deleting data in real-time. There are three options for this:

1. Use [WebSocket API](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API). This is not a good option if some of your users are using browsers that don’t yet support WebSocket.
2. Use a library that abstracts away these cross-browser differences with a fallback mechanism, such as [Socket.IO](https://socket.io/), [SignalR](http://www.asp.net/signalr), and [SockJS](https://github.com/sockjs/sockjs-client). With this option, you’d have to manage the server that handles a large number of open connections and deal with scaling.
3. Use a service that provides a library that does the same thing as the previous option, but manages the server and scales appropriately. This is a preferable option for companies and teams that are adopting (or have adopted) the serverless approach.

I’ll show you how to build a real-time editable data table in Vue.js using [Hamoni Sync](https://www.hamoni.tech/) as the real-time state synchronisation service. The picture below shows what we’ll build:

![Image](https://cdn-media-1.freecodecamp.org/images/JKuAr28AYFl1z-bZJR2jNTO3l8e1glrYOqc0)

To follow along, you’ll need to have some basic knowledge of Vue. If you have no knowledge of Vue, you can read my [previous post](https://dev.to/pmbanugo/from-vanillajs-to-vuejs-a-guide-to-vue-essentials-5gii) to get up to speed with Vue.js. You’ll also need the following tools:

1. [Node.js & npm](https://nodejs.org/en/download/) (follow the link to download an installer for your OS)
2. [Vue CLI](https://www.npmjs.com/package/vue-cli) to scaffold a new Vue project. If you don’t have this, run `npm install -g vue-cli@2.9.6` from the command line to install it.

### Set up the project

We’ll set up the project using the Vue CLI and a [template](https://github.com/vuetifyjs/simple) from [Vuetify](https://vuetifyjs.com/en/). Open the command line and run the command `vue init vuetifyjs/simple realtime-datatable-vue`. You'll get asked for a name and an author, so accept the default value by hitting enter for each prompt. This will scaffold a new Vue project with a single `index.html` file.

This file contains script references to Vue and Vuetify. Vuetify is a [Material Design](https://material.io/) Component for Vue.js. It has a `v-data-table` component with features for sorting, searching, pagination, inline-editing, header tooltips, and row selection.

### Add the data table component

Open the file `index.html` with your text editor (or IDE). Replace the content on line **50** with the following:

```
<div>    <v-dialog v-model="dialog" max-width="500px">    <v-btn slot="activator" color="primary" dark class="mb-2">New Item</v-btn>    <v-card>        <v-card-title>        <span class="headline">{{ formTitle }}</span>        </v-card-title>        <v-card-text>        <v-container grid-list-md>            <v-layout wrap>            <v-flex xs12 sm6 md4>                <v-text-field v-model="editedItem.name" label="Dessert name"></v-text-field>            </v-flex>            <v-flex xs12 sm6 md4>                <v-text-field v-model="editedItem.calories" label="Calories"></v-text-field>            </v-flex>            <v-flex xs12 sm6 md4>                <v-text-field v-model="editedItem.fat" label="Fat (g)"></v-text-field>            </v-flex>            <v-flex xs12 sm6 md4>                <v-text-field v-model="editedItem.carbs" label="Carbs (g)"></v-text-field>            </v-flex>            <v-flex xs12 sm6 md4>                <v-text-field v-model="editedItem.protein" label="Protein (g)"></v-text-field>            </v-flex>            </v-layout>        </v-container>        </v-card-text>        <v-card-actions>        <v-spacer></v-spacer>        <v-btn color="blue darken-1" flat @click.native="close">Cancel</v-btn>        <v-btn color="blue darken-1" flat @click.native="save">Save</v-btn>        </v-card-actions>    </v-card>    </v-dialog>    <v-data-table :headers="headers" :items="desserts" hide-actions class="elevation-1">    <template slot="items" slot-scope="props">        <td>{{ props.item.name }}</td>        <td class="text-xs-right">{{ props.item.calories }}</td>        <td class="text-xs-right">{{ props.item.fat }}</td>        <td class="text-xs-right">{{ props.item.carbs }}</td>        <td class="text-xs-right">{{ props.item.protein }}</td>        <td class="justify-center layout px-0">        <v-btn icon class="mx-0" @click="editItem(props.item)">            <v-icon color="teal">edit</v-icon>        </v-btn>        <v-btn icon class="mx-0" @click="deleteItem(props.item)">            <v-icon color="pink">delete</v-icon>        </v-btn>        </td>    </template>    </v-data-table></div>
```

The code above adds a `v-dialog` component for displaying a dialog to collect data for new records or edit an existing record. Also, it adds the `v-data-table` which renders the table. We need to define the data and methods used by these components. After line **126**, add the following code to the data properties:

```
dialog: false,headers: [    {        text: 'Dessert (100g serving)',        align: 'left',        sortable: false,        value: 'name'    },    { text: 'Calories', value: 'calories' },    { text: 'Fat (g)', value: 'fat' },    { text: 'Carbs (g)', value: 'carbs' },    { text: 'Protein (g)', value: 'protein' },    { text: 'Actions', value: 'name', sortable: false }],desserts: [],editedIndex: -1,editedItem: {    name: '',    calories: 0,    fat: 0,    carbs: 0,    protein: 0},defaultItem: {    name: '',    calories: 0,    fat: 0,    carbs: 0,    protein: 0},listPrimitive: null
```

The `desserts` data property will hold the data to be displayed in the table. The `editedItem` property will hold values for the record being edited, and the `editedIndex` will hold the index of the record being edited.

Add the following properties after the `data` property definition, after line **189**:

```
computed: {    formTitle() {        return this.editedIndex === -1 ? 'New Item' : 'Edit Item'    }},
```

```
watch: {    dialog(val) {        val || this.close()    }},
```

We added a `computed` and `watch` property. The `computed` property defines `formTitle` which gives the dialog component a title based on the value of `editedIndex`. The `watch` property watches `dialog` for when its value changes. If the value changes to false, it calls the function `close()` which will be defined later.

### Add Hamoni Sync

At this junction we need to add Hamoni Sync. It is used to synchronise the application state, and handles conflict resolution to avoid one user overriding another user’s data. To use Hamoni Sync, you’ll have to sign up for an account and application ID. Follow these steps to create an application in Hamoni.

1. Register and login to the Hamoni [dashboard](https://dashboard.hamoni.tech/).
2. Enter your preferred application name in the text field and click the create button. This should create the app and display it in the application list section.
3. Click the button “Show Account ID” to see your account ID.

![Image](https://cdn-media-1.freecodecamp.org/images/xuqPh053ZqsE3kInM55NSiY41ZG05f7VWED4)

Below the script reference to Vuetify on line **139**, add a reference to Hamoni Sync:

```
<script src="https://unpkg.com/hamoni-sync@0.4.0/hamoni.dev.js"><;/script>
```

Then we need to initialise Hamoni Sync once the Vue component is mounted. Add a `mounted` property below the `watch` property:

```
mounted: function () {    let hamoni = new Hamoni("ACCOUNT_ID", "APP_ID");
```

```
    hamoni.connect().then(() => {        hamoni          .get("vue-table")          .then(primitive => {            this.listPrimitive = primitive            this.desserts = [...primitive.getAll()]            this.subscribeToUpdate()          }).catch(error => {              if (error === "Error getting state from server") {                this.initialise(hamoni);              }              else {                 alert(error);              }          })    }).catch(alert)},
```

From the code above, we initialize Hamoni Sync with an account and application ID. Replace the string placeholders with the account and application ID from the dashboard. Then it is connected to the Hamoni server by calling `hamoni.connect()` which returns a promise.

Once connected, we call `hamoni.get()` with the name of the state stored in Hamoni. In order to retrieve a state from Hamoni, it needs to have been created, otherwise it'll return an error. What I've done here is handle this error within the catch block, such that it calls another function to initialize the state in Hamoni Sync.

If the call to get an application state succeeds, it returns an object which will be used to modify data contained in that state. This object is referred to as a Sync primitive. There are three types of Sync primitives:

1. [Value Primitive](https://docs.hamoni.tech/value-primitive.html): This kind of state holds simple information represented with datatypes like string, boolean or numbers. It is best suited for cases such as unread message count, toggles, etc.
2. [Object Primitive](https://docs.hamoni.tech/object-primitive.html): Object state represents states that can be modelled as a JavaScript object. An example usage could be storing the score of a game.
3. [List Primitive](https://docs.hamoni.tech/list-primitive.html): This holds a list of state objects. A state object is a JavaScript object. You can update an item based on its index in the list.

We’ve used a list primitive for this example. We call `primitive.getAll()` to get the state and pass it to `desserts`. After that, it calls the function `subscribeToUpdate()`. This function will be used to subscribe to state change events from Hamoni Sync.

Add the following code after the `mounted` property on line **215**:

```
methods: {  initialise(hamoni) {    hamoni.createList("vue-table", [      {        name: 'Frozen Yogurt',        calories: 159,        fat: 6.0,        carbs: 24,        protein: 4.0      },      {        name: 'Ice cream sandwich',        calories: 237,        fat: 9.0,        carbs: 37,        protein: 4.3      },      {        name: 'Eclair',        calories: 262,        fat: 16.0,        carbs: 23,        protein: 6.0      }    ]).then(primitive => {      this.listPrimitive = primitive      this.desserts = this.listPrimitive.getAll()      this.subscribeToUpdate();    }).catch(alert)  },
```

```
  subscribeToUpdate() {    this.listPrimitive.onItemAdded(item => {      this.desserts.push(item.value)    })
```

```
    this.listPrimitive.onItemUpdated(item => {      //update the item at item.index      this.desserts.splice(item.index, 1, item.value);    })
```

```
    this.listPrimitive.onItemDeleted(item => {      //remove the item at item.index      this.desserts.splice(item.index, 1);    })  },
```

```
  editItem(item) {    this.editedIndex = this.desserts.indexOf(item)    this.editedItem = Object.assign({}, item)    this.dialog = true  },
```

```
  deleteItem(item) {    const index = this.desserts.indexOf(item)    confirm('Are you sure you want to delete this item?') && this.listPrimitive.delete(index)  },
```

```
  close() {    this.dialog = false    setTimeout(() => {      this.editedItem = Object.assign({}, this.defaultItem)      this.editedIndex = -1    }, 300)  },
```

```
  save() {    if (this.editedIndex > -1) {      this.listPrimitive.update(this.editedIndex, this.editedItem)    } else {      this.listPrimitive.push(this.editedItem)    }
```

```
    this.close()  }}
```

The code above defines the functions we’ve been referencing thus far.

The `initialise()` function creates the list primitive with name as `vue-table`.

The `subscribeToUpdate()` functions contain code to handle when an item is added, updated, or deleted from the list primitive.

The `deleteItem()`function removes an item from the list primitive by calling `listPrimitive.delete(index)` with the index of the item to delete.

The `save()` function calls `listPrimitive.push(editedItem)` to add a new item to the list primitive, and calls `listPrimitive.update(editedIndex, editedItem)` to update the record at a certain index.

This is all the code that’s needed to achieve our objective of a real-time editable data table. Open the `index.html` file in your browser and the application is ready to use!

![Image](https://cdn-media-1.freecodecamp.org/images/FObytUBfPksl2aGCLfy0dQSUOv10LjBJ68ok)

### That’s A Wrap!

We’ve built a real-time editable data table in Vue.js. [Hamoni Sync](https://dev.to/pmbanugo/hamoni.tech) makes it easy to add real-time functionality. Both [Vuetify](https://vuetifyjs.com/en/) and [Hamoni Sync](https://www.npmjs.com/package/hamoni-sync) have npm packages if you’re working with a build system and using single file components. You can find the source code on [GitHub](https://github.com/pmbanugo/realtime-datatable-vue).

### Resources

* [Hamoni Sync](https://www.hamoni.tech/) ([docs](https://dev.to/pmbanugo/docs.hamoni.tech))
* [Vuetify](https://vuetifyjs.com/en/)
* [Vue CLI](https://www.npmjs.com/package/vue-cli)
* [Introduction to Vue.js essentials](https://dev.to/pmbanugo/from-vanillajs-to-vuejs-a-guide-to-vue-essentials-5gii)

