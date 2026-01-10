---
title: How to Add Authentication to a Vue App Using AWS Amplify
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-01-14T22:37:42.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-authentication-to-a-vue-app-using-aws-amplify
coverImage: https://www.freecodecamp.org/news/content/images/2021/01/0_QrOUXeTdCaxjv6o_-1.jpeg
tags:
- name: authentication
  slug: authentication
- name: AWS
  slug: aws
- name: vue
  slug: vue
seo_title: null
seo_desc: 'By Jennifer Bland

  In this article, we’re going to create a very simple Vue application using the Vue
  CLI. We’ll modify the default scaffolded application so it provides a form to register
  as a new user, a login page, and a dashboard page only shown t...'
---

By Jennifer Bland

In this article, we’re going to create a very simple Vue application using the Vue CLI. We’ll modify the default scaffolded application so it provides a form to register as a new user, a login page, and a dashboard page only shown to people that are logged in.

Users will be able to register using an email and password. Once they’ve registered and logged in, they’ll be presented with the dashboard page.

# How to Create Our Project

I’ll be using the Vue CLI to scaffold out a project for us to start with. To do that, you need to have the Vue CLI installed on your system. If you don’t have it installed, you can install it globally with this command:

```
npm install -g @vue/cli
```

Now we can use the Vue CLI to create our project. Create a new project using this command:

```
vue create vue-amplify-auth-tutorial
```

You’ll be asked to pick a preset. Choose “Manually select features,” and then select “babel,” “Router,” and “Linter / Formatter.”

You’ll be asked if you want to use the history mode for the router. Choose “Yes” (should be the default).

For a linter, I’m selecting “ESLint with error prevention only.”

After the Vue CLI is finished, it’ll give you the commands to change into the new directory that was just created and the command to start the server. Follow those directions. 

Once the server is started you can open your browser to `localhost:8080`. You should see this:

![Image](https://www.freecodecamp.org/news/content/images/2021/01/0_S9E-Jj_1zY76iZBj.png)

# What is AWS Amplify?

AWS Amplify is an open-source framework created by Amazon that contains a set of tools and services that can be used together or on their own. 

One of the tools is Amplify Auth. Amplify Auth lets you quickly set up secure authentication and control what users have access to in your application.

The Amplify framework uses Amazon Cognito as the main authentication provider. Amazon Cognito is a robust user-directory service that handles user registration, authentication, account recovery, and other operations.

# Create an AWS Account

To get started, you’ll need to create an AWS account here. If you don’t have an AWS account, [follow the directions here to create one](https://aws.amazon.com/premiumsupport/knowledge-center/create-and-activate-aws-account/).

# Install and Configure the Amplify CLI

The Amplify CLI is a unified toolchain to create AWS cloud services for your app. You can install it globally with this command:

```
npm install -g @aws-amplify/cli
```

Next, we need to configure Amplify by running the following command:

```
amplify configure
```

This command will open up a new browser window and ask you to sign into the AWS console. Once you’re signed in, return to your terminal, and press `Enter`.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/0_SBiQgDy2bw0OGeX3.png)

You’ll be asked to specify the AWS Region. Select the region closest to you.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/0_Wx3wr2Ohnd7_2RAG.png)

You’ll need to specify the username of the new IAM user. It’ll provide a default name you can use by hitting enter or you can specify your own name. I’m going to call my user `auth-demo`.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/0_z0qKKxKSjp_1K98H.png)

When you hit `Enter`, you’ll be taken back to your browser.

Click the Next: Permissions button.

Click the Next: Tags button.

Click the Next: Review button.

Click the Create User button.

Now go back to your terminal and press `Enter` to continue.

Type in the `accessKeyId` of the user you just created, and press `Enter`.

Type in the `secretAcessKey` of the user you just created, and press `Enter`.

You’ll be asked to enter a profile name. I’ll accept the supplied value (the default) by just pressing `Enter`.

When everything is finished, you should get a message in your terminal that the new user was successfully set up.

# Initialize a New Back End

Now that we have a running Vue app, it’s time to set up Amplify so we can create the necessary back-end services needed to support the app. From the root of your Vue application, run:

```
amplify init
```

# Create the Authentication Service

We need to add an authentication service to our Vue application. In the root directory of your Vue application, enter this command:

```
amplify add auth
```

When you initialize Amplify, you’ll be prompted for some information about your application. Enter a project name.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/0_0Q7RiIPnBCAo90Kf.png)

Set the back-end environment name to be `dev`.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/0_SMbI1iNM5XELFdfp.png)

Sometimes the CLI will prompt you to edit a file — it’ll use this editor to open those files. Select your preferred code-editor software.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/0_juPUaS2SIkR0UnxL.png)

Amplify will provide configuration files for your front-end application to connect to this back-end environment. Since Vue is based on JavaScript, we’ll select that here.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/0_enPauC_uAMYzoDFV.png)

We’re using Vue, so select that as our JavaScript framework.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/0_xOxbC5xEGdudv-ej.png)

The Vue CLI sets up the source files for your project under a `./src` folder. Select `src` for the Source Directory Path.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/0_iLN4pnHKGUGB3tCz.png)

When your project is ready to be hosted, Vue will generate your website, ready for public use, into a folder called `dist`. This is the default, so you can just press `Enter` to continue.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/0_u1tw63qKuNAsPJ9B.png)

Amplify’s automated deployment needs to know what steps are needed to build your application for publishing. Here, we’ll set that to be the Vue CLI’s default build script.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/0_SqFEoy03S2eingpb.png)

If Amplify needs to run the application in development mode, it needs to know how to start the development server. Again, we’ll use the Vue CLI’s default scripts.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/0_WR5XjxUw9TmYlTUv.png)

Finally, Amplify needs an AWS account to connect to so we can begin creating the back-end services. This is the profile you created with the `amplify configure` command earlier. Select “yes” by typing `y` and pressing `Enter`.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/0_oTD19eyWt9KdCb6J.png)

Proceed to select your profile from the list, and press `Enter`. Amplify will now begin deploying your back-end framework.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/0_fX2wHxziZZil6sJ3.png)

When you initialize a new Amplify project, a few things happen:

* It creates a top-level directory called `amplify` that stores your back-end definition. During the tutorial, you'll add capabilities such as authentication, the GraphQL API, storage, and the authorization rules for the API. As you add features, the `amplify` folder will grow with infrastructure-as-code templates that define your back-end stack. Infrastructure-as-code is a best-practice way to create a replicable back-end stack.
* It creates a file called `aws-exports.js` in the `src` directory that holds all of the configuration for the services you create with Amplify. This is how the Amplify client is able to get the necessary information about your back-end services.
* It modifies the `.gitignore` file, adding some generated files to the ignore list
* A cloud project is created for you in the AWS Amplify Console that can be accessed by running `amplify console`. The console provides a list of back-end environments, deep links to provisioned resources per Amplify category, the status of recent deployments, and instructions on how to promote, clone, pull, and delete back-end resources

To deploy the service, run the `push` command.

# Install Amplify Libraries

We need to install the Amplify dependencies in our Vue application. You can install them with this command:

```
npm install aws-amplify
```

# Configure Our Application

We need to add Amplify to our Vue application. Open up the `main.js` file, and add the following after the last import line:

```
import Amplify from 'aws-amplify';
import awsconfig from './aws-exports'; 
Amplify.configure(awsconfig);
```

The above code successfully configures Amplify. As you add or remove categories and make updates to your back-end configuration using the Amplify CLI, the configuration in `aws-exports.js` will update automatically.

# Create a Sign-Up Page

We need a page that’ll allow new users to register with our application. In the views folder, create a new file called `Register.vue`.

We need to add this new page to our routes and then display it in the navigation. Open up the `index.js` file in the `router` folder. Add this to the routes array.

```
{
    path: '/register',
    name: 'Register',
    component: () =>
        import(/* webpackChunkName: "register" */ '../views/Register.vue'),
},
```

Now add this to our navigation. Open up the `App.vue` file, and add an entry for `Register` in the nav. Your nav should look like this:

```
<div id="nav">
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link> |
    <router-link to="/register">Register</router-link>
</div>
```

Go back to your `Register.vue` file. This page will have a form for a user to put their email and a password to register as a new user. Here’s the code you need to put in the template section:

```
<div class="container">
    <form @submit.prevent="register">
        <h2>Register</h2>
        <input
            type="email"
            v-model="email"
            placeholder="Email address..."
        />
        <input
            type="password"
            v-model="password"
            placeholder="password..."
        />
        <button>Register</button>
    </form>
</div>
```

If you look at our form, the two input fields and the button are right next to each other.

Want to add some spacing between the three fields? I could add CSS to this page, but it’d only apply to this page. We’re going to use this form again on the login page we’ll be creating next. 

To get styles that work on both pages, let’s put the following CSS in the `App.vue` file. Open up the `App.vue` file, and add the following style:

```
:input {   
  margin-right: 10px; 
}
```

Go back to the `Register.vue` file. We’re capturing the values the user enters for their email and password, so we need to add them to the data object. Add them to the data object so it looks like this:

```
data() { 
  return { 
    email: '', 
    password: '', 
  }; 
},
```

When a user submits the form it calls the `register` method. Here’s the code for that method:

```
async register() {
    try {
        await Auth.signUp({
            username: this.email,
            password: this.password,
        });
        alert('User successfully registered. Please login');
    } catch (error) {
        alert(error.message);
    }
},
```

This method uses `Auth` from the `aws-amplify` package we installed. Add this import for it at the beginning of the script section.

```
import { Auth } from 'aws-amplify';
```

Now open up your application, and register a new user. If successful, you’ll get an alert saying the user was registered.

# Create a Login Page

Once a user has registered an account with our application, they need a page through which they can log in. In the `views` folder, create a new file called `Login.vue`.

We need to add this new page to our routes and then display it in the navigation. Open up the `index.js` file in the `router` folder. Add this to the routes array.

```
{
    path: '/login',
    name: 'Login',
    component: () =>
        import(/* webpackChunkName: "login" */ '../views/Login.vue'),
},
```

Now add this to our navigation. Open up the `App.vue` file, and add an entry for `Register` in the nav. Your nav should look like this:

```
<div id="nav">
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link> |
    <router-link to="/register">Register</router-link> |
    <router-link to="/login">Login</router-link> 
</div>
```

Go back to your `Login.vue` file. You can copy the HTML code in the template section of the `Register.vue` file and paste it into this new file. Change all references of `Register` to `Login`. Your template section should look like this:

```
<div class="container">
    <form @submit.prevent="login">
        <h2>Login</h2>
        <input type="email" v-model="email" placeholder="Email address..." />
        <input type="password" v-model="password" placeholder="password..." />
        <button>Login</button>
    </form>
</div>
```

In the script section, add the import for `Auth` and the data object for the email and password. Your script section should look like this:

```
<script>
import { Auth } from 'aws-amplify';
export default {
  name: 'Login',
  data() {
    return {
      email: '',
      password: ''
    }
  },
}
</script>
```

The last thing we need to implement is the login method. Here’s the code:

```
async login() {
    try {
        await Auth.signIn(this.email, this.password);
        alert('Successfully logged in');
    } catch (error) {
        alert(error.message);
    }
},
```

Now if you open up your application, you’ll be able to log in with the user you previously registered.

# Add a Logout Method

We need to add a button so users can log out of our application. Open up the `App.vue` file. Add a button to log out in the nav. Your nav should look like this:

```
<div id="nav">
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link> |
    <router-link to="/register">Register</router-link> |
    <router-link to="/login">Login</router-link> |
    <button @click="logout">Logout</button>
</div>
```

In the script section, add a `methods` object, and include the `logout` method. It should look like this:

```
methods: {
    async logout() {
        try {
            await Auth.signOut();
        } catch (error) {
            alert(error.message);
        }
    },
},
```

Congratulations, you’ve successfully added AWS Amplify authentication to your Vue application.

# Get the Code

I have the [complete code on my GitHub account here](https://github.com/ratracegrad/Vue-Amplify-Auth-Tutorial).

# Using Other Authentication Methods

I’ve written several follow up articles on adding authentication to your Vue application using other authentication methods.

* [Using Firebase for authentication](https://www.jenniferbland.com/how-to-add-authentication-to-a-vue-app-using-firebase/)
* [Using Auth0 for authentication](https://www.jenniferbland.com/how-to-add-authentication-to-a-vue-app-using-auth0/)

# Conclusion

AWS Amplify is a a great tool allowing you to add authentication to your application.

Hope you enjoyed this article. Thanks for reading.

_Originally published at_ [_https://www.jenniferbland.com_](https://www.jenniferbland.com/how-to-add-authentication-to-a-vue-app-using-auth0/) _on December 31, 2020._

