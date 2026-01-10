---
title: How to Create a Real-time Chat Application with Nuxt
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-08-10T19:39:17.000Z'
originalURL: https://freecodecamp.org/news/create-a-real-time-chat-application-with-nuxt
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/chat-app-with-nuxt-image.png
tags:
- name: application
  slug: application
- name: Chat
  slug: chat
- name: JavaScript
  slug: javascript
- name: Nuxt.js
  slug: nuxtjs
seo_title: null
seo_desc: "By Idorenyin Udoh\nIn a real-time chat application, the recipient can view\
  \ the sender’s message almost immediately. This can either be in a one-on-one conversation\
  \ between two parties or a group conversation. \nAnd that's what we're going to\
  \ build in t..."
---

By Idorenyin Udoh

In a real-time chat application, the recipient can view the sender’s message almost immediately. This can either be in a one-on-one conversation between two parties or a group conversation. 

And that's what we're going to build in this tutorial. For this application, we will be using [Nuxt](https://nuxtjs.org/), the intuitive Vue framework.

Now that we know what we’re going to be building and the technology we’ll be using, let’s go over the chat API we’ll be using.

For this article, we’ll be going with [Robin](https://robinapp.io/) because of its minimal UI and how easy it is to integrate into our app. With that out of the way, let’s get started.

# Step 1 – Create the Nuxt App

First, we need to create the Nuxt app with any of the following commands:

```
yarn create nuxt-app nuxt-chat-app
// OR
npx create-nuxt-app nuxt-chat-app
// OR
npm init nuxt-app nuxt-chat-app
```

# Step 2 – Create a Robin Account

Now that our app is ready, we need to have a Robin account before we can use it. Head over to [Robin’s signup page](https://dashboard.robinapp.co/signup) to create a 30-day free trial account. 

Robin notifies you 7 days after you've created the account and you can remove your card before the billing date. 

After filling out the signup form, you’ll be redirected to a billing page to fill in your card information. On the next page where it redirects you, Robin requests the name of the app you want to create and its authentication type. Feel free to use any name of your choice and either of the auth options.

![Image](https://paper-attachments.dropbox.com/s_8728EF96CF25BE6F7A46E3619EB658CA92CDD4D1E377FEC5C8707FC59B5068A6_1658071816533_Screenshot+2022-07-17+at+16.29.23.png)

# Step 3 – Get Your Robin Credentials

Now that we have created an app on our Robin dashboard, there is something you should take note of. There are a couple of credentials you need when using Robin in your Nuxt app:

* API key,
* User token,
* User name,
* Users, and
* Keys

Let’s go over each of them individually.

* API key: Robin automatically creates the API key when you create an app. You can retrieve it from either the getting started or the API config page on your dashboard. It is unique for every application.
* User token: The user token is a unique identifier for every user of your Robin app. The token that should be passed to this property is yours since you’re the one using the app on your site. However, it is to be created by you, the user, typically on the server, and then used on the client side.
* User name: The User name is the name of the current user of your Robin app. In this case, it will be your name. If you wanted someone else to include your Robin chat on their site or web app (i.e another user of your Robin app), it should be their name.
* Users: Users is a list of the users on your Robin app. It usually contains their user tokens, profile images, and user names.
* Keys: This fundamentally exists to help us be flexible in describing the user tokens, profile images, and user names in our users list. Here’s an example. If our keys object looks like this:

```javascript
keys: {
  userToken: 'user_token',
  profileImage: 'profile_image',
  userName: 'user_name'
}
```

Then our `users` array should describe the users’ tokens, profile images, and names with the values in the `keys` object.

Regardless of the users that would be using your Robin App, Robin requires a `userToken`, `profileImage` and a `userName` from them. Robin requires this for the display name and to identify each message sender and receiver uniquely on the platform.

```js
users: [
  {
    'user_token': 'ABCDEF098765GH',
    'profile_image': 'https://url-to-image',
    'user_name': 'Article Reader'
  }
]
```

# Step 4 – Install Robin in Your Nuxt App

Since we have everything we’ll need, we can go ahead and install Robin.

```
npm i robin-vue
// OR
yarn add robin-vue
```

# Step 5 – Setup the Robin Plugin

In your `plugins` directory, create a `robin.js` file with the plugin setup:

```javascript
import Vue from 'vue'
import RobinChat from 'robin-vue'
import 'robin-vue/dist/style.css'

Vue.use(RobinChat)
```

Note that we import the CSS because the `RobinChat` component does not include any CSS itself.

# Step 6 – Register the Plugin

The `plugins` property in the `nuxt.config.js` file is to let our Nuxt app know about the plugins that it should use. So if we don’t include our Robin plugin there, it won’t be available in our app.

```javascript
export default {
  // ...
  plugins: [
    { src: '~/plugins/robin.js', mode: 'client' }
  ]
}
```

# Step 7 – Use the Plugin

Now what’s left is for us to include the `RobinChat` component anywhere in our app and pass those credentials we discussed earlier as props. 

Once again, the credentials are:

* API key,
* User token,
* User name,
* Users, and
* Keys

In this list, what we currently don’t have is our user token and the tokens of the users on our app. 

Recall that these tokens are usually created on the server. But we don’t have the luxury of that. So we can go ahead and create them with the help of [Robin’s JavaScript SDK](https://www.npmjs.com/package/robin.io-js). The Vue SDK we previously installed depends on this JavaScript SDK. So we don’t need to install it since it already exists in our app.

## How to Create the User Tokens

We can go ahead and create the tokens in the page we're going to include the chat UI. Because it’s for learning purposes, we can go ahead and create tokens for 5 users, ourselves included. We need to come up with usernames for each of them.

```javascript
<template>
  <!-- ... -->
</template>


<script>
export default {
  data () {
    return {
      users: [
        {
          user_token: '',
          profile_image: '',
          user_name: 'idorenyin'
        },
        {
          user_token: '',
          profile_image: '',
          user_name: 'ayo'
        },
        {
          user_token: '',
          profile_image: '',
          user_name: 'elvis'
        },
        {
          user_token: '',
          profile_image: '',
          user_name: 'favour'
        },
        {
          user_token: '',
          profile_image: '',
          user_name: 'enoch'
        }
      ],
    }
  }
}
</script>
```

Note that the keys in every user object in the `users` array have to be defined in the `keys` object that we’ll be passing as a prop to the Robin component.

```javascript
keys: {
  userToken: 'user_token',
  profileImage: 'profile_image',
  userName: 'user_name'
},
```

Next, we use the SDK’s `createUserToken()` function to create the tokens after creating a Robin instance, as it says in [Robin’s docs](https://docs.robinapp.co/frontend-sdks/javascript/getting-started).

```javascript
<template>
  <!-- ... -->
</template>

<script>
import { Robin } from 'robin.io-js'

export default {
  data () {
    return {
      keys: {
        userToken: 'user_token',
        profileImage: 'profile_image',
        userName: 'user_name'
      },
      users: [
        // ...
      ]
    }
  },
  created () {
    this.createTokens()
  },
  methods: {
    async createTokens () {
      const robin = new Robin('API_KEY', true)
      for (let i = 0; i < this.users.length; i++) {
        await robin.createUserToken({
          meta_data: {
            username: this.users[i].user_name
          }
        }).then((res) => {
          this.users[i].user_token = res.data.user_token
        })
      }
    }
  }
}
</script>
```

## How to Use Credentials on the RobinChat Component

We now have everything we need to display the Robin chat UI on our app. Whew!  
We can now go ahead and use the tokens and the other credentials.

```javascript
<template>
  <!-- ... -->
  <RobinChat
    v-if="tokensAreAvailable"
    :api-key="apiKey"
    :user-token="users[0].user_token"
    user-name="Idorenyin Udoh"
    :keys="keys"
    :users="users"
  />
</template>

<script>
import { Robin } from 'robin.io-js'

export default {
  data () {
    return {
      tokensAreAvailable: false,
      apiKey: 'API_KEY',
      keys: {
        userToken: 'user_token',
        profileImage: 'profile_image',
        userName: 'user_name'
      },
      users: [
        {
          user_token: '',
          profile_image: '',
          user_name: 'idorenyin'
        },
        {
          user_token: '',
          profile_image: '',
          user_name: 'ayo'
        },
        {
          user_token: '',
          profile_image: '',
          user_name: 'elvis'
        },
        {
          user_token: '',
          profile_image: '',
          user_name: 'favour'
        },
        {
          user_token: '',
          profile_image: '',
          user_name: 'enoch'
        }
      ]
    }
  },
  created () {
    this.createTokens()
  },
  methods: {
    async createTokens () {
      const robin = new Robin(this.apiKey, true)
      for (let i = 0; i < this.users.length; i++) {
        await robin.createUserToken({
          meta_data: {
            username: this.users[i].user_name
          }
        }).then((res) => {
          this.users[i].user_token = res.data.user_token
        })
      }
      this.tokensAreAvailable = true
    }
  }
}
</script>
```

Note that we only display the `RobinChat` component when all the users’ tokens are available to avoid errors.

This is what the result looks like:

![Image](https://paper-attachments.dropbox.com/s_8728EF96CF25BE6F7A46E3619EB658CA92CDD4D1E377FEC5C8707FC59B5068A6_1658311851926_Screenshot+2022-07-20+at+11.10.45.png)

The app is available [here](https://nuxt-chat-lmqlbq79p-idorenyinudoh.vercel.app/).

Note that I used previously-created user tokens for this app because you wouldn’t be able to view messages if tokens are created every time the app loads. Permanent tokens are what make the messages on Robin persist.

Also, I created [another app](https://nuxt-chat-app-git-ayo-idorenyinudoh.vercel.app/) for the user Ayo. You can check it out too. This way, you can test the real-time communication between Idorenyin and Ayo.

# Conclusion

You just learned how to implement real-time communication on a Nuxt application with Robin. 

The ease of integration makes it super fast to implement a chat system in your app and focus on building/maintaining it. 

If you make sure to create your users’ tokens on the server, then implementing the integration on the frontend wouldn't be too hard.

Happy building!

