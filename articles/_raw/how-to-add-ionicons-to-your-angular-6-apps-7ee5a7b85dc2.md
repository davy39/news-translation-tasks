---
title: How to add Ionicons to your Angular 6 apps
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-06T00:26:20.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-ionicons-to-your-angular-6-apps-7ee5a7b85dc2
coverImage: https://cdn-media-1.freecodecamp.org/images/1*I_tQfo1PrAT_kum--QcNGw.jpeg
tags:
- name: Ionicons
  slug: ionicons
- name: Angular
  slug: angular
- name: JavaScript
  slug: javascript
- name: 'tech '
  slug: tech
- name: Tutorial
  slug: tutorial
seo_title: null
seo_desc: 'By Adedoja Adedamola

  I have had to work on a lot of Angular apps recently and Font Awesome has literally
  tired me out. So I decided to use Ionicons off the popular Ionic framework.

  This post shows how to set up Ionicons on your Angular project. We wi...'
---

By Adedoja Adedamola

I have had to work on a lot of [**Angular**](https://angular.io/) apps recently and Font Awesome has literally tired me out. So I decided to use [**Ionicons**](http://ionicons.com/) off the popular Ionic framework.

This post shows how to set up [**Ionicons**](http://ionicons.com/) on your Angular project. We will take the following steps:

* Install Angular CLI v6
* Create a new Angular v6 app
* Install Ionicons
* Setup Ionicons for use on your Angular v6 app

#### Install Angular CLI v6

This is pretty simple — you just install the latest Angular version via npm.

```
npm install -g @angular/cli@latest
```

After that has been done, you then run a `ng --version` to check for the version of Angular you have installed. Make sure it is Angular CLI version of 6.0.0 and above, like below.

![Image](https://cdn-media-1.freecodecamp.org/images/1*se1AfRueItoiUcswhitMEg.png)
_Angular version check using ng — version_

#### Create a new Angular v6 app

At this point, you have installed the Angular CLI globally on your PC. Now you get to create a new Angular app. We use the `ng new name-of-my-incredible-app` command, it allows us to create an Angular application.

```
ng new my-ionicons-angular-app --style=scss
```

The SCSS bit is there to allow us to use SCSS. This takes a bit. When it is done, we then navigate to the newly created app.

```
cd my-ionicons-angular-app
```

As soon as we are in the project directory, we can then start the development server.

```
ng serve
```

This returns the following:

```
** Angular Live Development Server is listening on localhost:4200, open your browser on http://localhost:4200/ **
```

Running the URL [http://localhost:4200/](http://localhost:4200/) shows you your brand new app. If you see the screen below. You are good to go.

![Image](https://cdn-media-1.freecodecamp.org/images/1*bNZu4fH_Yc3vevGy_SoZ0Q.png)
_Default Angular Homepage_

#### Install Ionicons

Like we did earlier, we use npm again to install Ionicons.

```
npm install ionicons
```

#### Setup Ionicons for use on your Angular v6 app

As soon as it installs, we need to tell angular where and how to load it. Best way to do it is inside our styles.scss file and you do this by adding the following lines:

```
$ionicons-font-path: "~ionicons/dist/fonts";@import "~ionicons/dist/scss/ionicons.scss";
```

It should be set up correctly at this point. You can edit your homepage file — app.component.html and using the font icon to add a new icon there like this: `<i class="icon ion-md-heart"&g`t;</i> . You can also have a [**look at**](https://ionicons.com/) the Ionicons page for a list of icons there. Below is what my homepage looks like along with my app.component.html file.

![Image](https://cdn-media-1.freecodecamp.org/images/1*STno4LND04VK8Ft1DLDClw.png)
_Angular 6 homepage with an Ionicon_

#### That’s that!!

Pretty easy. I hope you made it to the end. If you have any questions or you see something wrong or something that can be done better, please leave a comment below or you can message me on twitter [**@TrussDamola**](https://twitter.com/TrussDamola)**.**

Cheers!

