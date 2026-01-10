---
title: Up & Going with Nuxt.js, Bulma and  Sass
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-06-15T11:09:27.000Z'
originalURL: https://freecodecamp.org/news/up-goind-with-nuxt-js-bulma-and-sass
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca202740569d1a4ca51f3.jpg
tags:
- name: 100DaysOfCode
  slug: 100daysofcode
- name: Bulma
  slug: bulma
- name: freeCodeCamp.org
  slug: freecodecamp
- name: JavaScript
  slug: javascript
- name: Nuxt.js
  slug: nuxtjs
- name: General Programming
  slug: programming
- name: Sass
  slug: sass
- name: vue
  slug: vue
seo_title: null
seo_desc: 'By Eduardo Vedes

  TL;DR: Overcome Nuxt.js, Bulma and Sass shenanigans with this quick article to help
  you start developing your next App in less than 10 minutes.

  Hi everyone ❤️! Few days ago I found myself struggling a bit to put Nuxt.js, Bulma
  and Sa...'
---

By Eduardo Vedes

**TL;DR: Overcome Nuxt.js, Bulma and Sass shenanigans with this quick article to help you start developing your next App in less than 10 minutes.**

Hi everyone ❤️! Few days ago I found myself struggling a bit to put **Nuxt.js**, **Bulma** and **Sass** to work correctly and the info I found on google didn't help too much. 

Most of the configurations I found were not working, because they were outdated or didn't explain quite well how to do it. So I deep dived a little bit on this subject and decided to write an article to help you do the same in less than 10 minutes.

Let's have some fun and get our hands dirty while grokking a few concepts needed to do this.

## 1. Scaffolding Nuxt.js



Nowadays, to get started quickly with Nuxt.js we use a scaffolding tool called **[create-nuxt-app](https://github.com/nuxt/create-nuxt-app)**. Please make sure you have **[npx](https://www.npmjs.com/package/npx)** installed on your machine.

Let's open a terminal and do: `npx create-nuxt-app nuxt-bulma-sass`, where `nuxt-bulma-sass` is the name of the project we're scaffolding for the purpose of this article.

**create-nuxt-app** will ask you some questions before creating the scaffold. For the purpose of this article I've chosen the following setup:

![Image](https://www.freecodecamp.org/news/content/images/2019/06/bulma2.png)
_create-nuxt-app init questions_

So, the next step will be to change directory into our project folder:

`cd nuxt-bulma-sass`

and launch the project with: `yarn run dev`. (you can also use npm if you like it)

At this point we have our project running:

![Image](https://www.freecodecamp.org/news/content/images/2019/06/bulma3.png)

And if we open our browser on localhost:3000 we'll be getting this screen:

![Image](https://www.freecodecamp.org/news/content/images/2019/06/Screen-Shot-2019-06-14-at-09.29.05.png)
_localhost:3000 pages/index.vue_

So at this point we have the pages/index.vue on the screen, which is the first page to be rendered in your project by default.

Let's replace the content of this file by the following one:

![Image](https://www.freecodecamp.org/news/content/images/2019/06/carbon1.png)

If we inspect our page in the browser we see we got **bulma** installed because section is formatted according to it.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/Screen-Shot-2019-06-14-at-09.45.03.png)

Easy peasy lemon squeezy.

Let's add a class and choose some colors:

![Image](https://www.freecodecamp.org/news/content/images/2019/06/carbon-2.png)

![Image](https://www.freecodecamp.org/news/content/images/2019/06/Screen-Shot-2019-06-14-at-09.47.55.png)

What if we want to nest ._hello-nuxt_ inside ._edo-theme_? We're going to need SASS to be able to do it.

## 2. Adding Sass



So, to add Sass to our project we'll need to stop our running app (Ctrl+c) and do the following:

`yarn add node-sass sass-loader --dev`

These are the two packages needed as dev-dependencies to be able to have Sass in our boilerplate.

Note that we're adding it as a dev dependency because we only need it while developing and at build time. After that **Sass** is transformed into **CSS** and we don't need it anymore.

Let's sneak peek my package.json for you to check it:

![Image](https://www.freecodecamp.org/news/content/images/2019/06/Screen-Shot-2019-06-14-at-09.57.38.png)
_package.json with sass added to the project_

Okay everyone ❤️, at this point we're able to nest the classes we wanted to.

Let's run our boilerplate again: `yarn run dev` and do the tweaks needed ?

![Image](https://www.freecodecamp.org/news/content/images/2019/06/carbon--1-.png)

![Image](https://www.freecodecamp.org/news/content/images/2019/06/Screen-Shot-2019-06-14-at-10.05.23.png)

Noice! We already did a lot today! Go grab a coffee ☕, I'll wait for you here ?

Okay, let's abstract things a bit and create this file _~/assets/scss/main.scss_ and put there some classes and variables:

![Image](https://www.freecodecamp.org/news/content/images/2019/06/carbon-1.png)
_new ~/assets/scss/main.scss_

![Image](https://www.freecodecamp.org/news/content/images/2019/06/carbon--1--1.png)

Nice! It's working!

Now we have two problems: 

1. We need to import main.scss into each one of our pages/components, which is not nice. We want to import it only once and have it available in all our <style> "bags"
2. We can't use bulma sass variables (try to change the **background-color** from the .edo-theme class from **$edo** to **$primary**. We want to have bulma sass variables in order to override them and create new themes from there.

So... what if we want to use [bulma sass variables](https://bulma.io/documentation/overview/colors/)? 

![Image](https://www.freecodecamp.org/news/content/images/2019/06/Screen-Shot-2019-06-14-at-10.13.31.png)
_bulma sass variables (colors doc)_

## 3. Here comes the hard part which took me some time to understand.



Bulma is being imported in the create-nuxt-app scaffold. When you do `yarn run dev` there's this hidden .**nuxt** folder into your **nuxt-bulma-sass** folder.

If you take a look at App.js there:

![Image](https://www.freecodecamp.org/news/content/images/2019/06/nuxt2.png)

You'll see that bulma is being imported from the node-modules when you launch dev environment.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/nuxt-bulma.png)
_.nuxt/App.js_

So, importing bulma while launching nuxt.js scaffold is not okay if we want to override bulma sass variables.

Don't despair, you don't have to throw your project away. Show must go on ?

## 4. Using Bulma the right way ?



How do we get bulma into our boilerplate the way we need? 

Let's start by commenting out @nuxtjs/bulma from the **nuxt.config.js** modules section (keep it on the package.json because what it does there is install bulma, it would be the same, AFAIK, as doing `yarn add bulma`).

Stop your running environment and do `yarn run dev` again.

If you take a look into _./nuxt/App_ you'll see that it's not importing bulma anymore.

So now what we have to do is to go to our main.scss file and import it in the last line of the file.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/carbon--4-.png)

_I've also imported bulma/sass/utilities/_all.sass_ for us to have the sass variables with the colors there.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/Screen-Shot-2019-06-14-at-11.12.24.png)
_/bulma/sass/utilities folder_

Of course later you can improve it by only importing exactly what you need. But that's another story for another article ?

Well well, check your browser and see it working.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/Screen-Shot-2019-06-14-at-11.19.16.png)

## 5. Yeah! It's working baby!



**Now the last problem!** We don't want to import it into our <style> scaffold each time we want to use it. We want it to be available as a global anywhere in the boilerplate.

The solution for this is to import a package called **[@nuxtjs/style-resources](https://www.npmjs.com/package/@nuxtjs/style-resources).** 

This package allows you to share variables, mixins, function across all files. No more imports needed on your <style> tag of each component or page.

Just stop  your dev environment and do:

`yarn add @nuxjs/style-resources`  Note: don't try to install it as a dev-dependency because it won't work correctly.

Also, open your nuxt.config.js file and add '@nuxtjs/style-resources' to your modules key/value.

You also need to add _styleResources._ Check how mine is after that ?

![Image](https://www.freecodecamp.org/news/content/images/2019/06/carbon--5-.png)

Do `yarn run dev` again and... no errors... but...

**CSS classes not being imported anymore.**

**FML** ??‍?☠️

## 6. Last tweak



**What's happening here?** 

So, from the point you import and use _@nuxt/style-resources_ you can't import actual styles from the main.scss anymore just because they won't exist in the actual build.

So, to solve this problem:

Stop your running the boilerplate again and open your nuxt.config.js:

Add the main.scss path to the global css array, like this:

![Image](https://www.freecodecamp.org/news/content/images/2019/06/carbon--6-.png)

This way we make sure that global css styles are also imported into the scope of our templates.

From this point on of course you can establish an architectural pattern for your css files, create independent variable, functions and mixins files and compose stuff with some extra @imports.

In the styleResources object you have the option to include more files as you need them in your boilerplate.

Again, that's beyond the scope of this article which was to show you how to unblock from this tiny complexities that nuxt and its ecosystems introduce in our App's flow.

## Hope you have enjoyed it! ❤️

## Be Strong and Code On ?



## 7. Last but not least



You can clone my repo and play around with it.

[https://github.com/evedes/nuxt-bulma-sass](https://github.com/evedes/nuxt-bulma-sass)

Thank you very much [@ruiposse](https://twitter.com/ruiposse) for reviewing this article and for mentoring me into the vue ecosystem. ❤️

## 8. Bibliography



01. [Nuxtjs.org](https://nuxtjs.org/)

02. [Nuxt Style Resources](https://github.com/nuxt-community/style-resources-module)

03. [Bulma.io](https://bulma.io/)

04. Some hours around google getting frustrated and seeing people also frustrated with this ?

---

Hey! I'm Edo, a frontend engineer dedicated to the JavaScript stack. Nowadays I work mostly with React, Vue and all the ecosystem around. 

If you liked this article you can read more [here](https://www.freecodecamp.org/news/author/evedes/).







 

