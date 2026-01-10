---
title: How to convert an AngularJS 1.x app to a React app — one component at a time.
subtitle: ''
author: Shruti Kapoor
co_authors: []
series: null
date: '2018-01-24T18:57:40.000Z'
originalURL: https://freecodecamp.org/news/how-to-convert-an-angular-app-to-a-react-app-one-component-at-a-time-ba985eaae66e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*yq7TPrTheULIcxwfTD96SA.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: Angular and React are both great frameworks/libraries. Angular provides
  a defined structure of MVC (Model, View, Controller). React provides a lightweight
  rendering mechanism based on state change. Often times, developers will have an
  application wit...
---

Angular and React are both great frameworks/libraries. Angular provides a defined structure of MVC (Model, View, Controller). React provides a lightweight rendering mechanism based on state change. Often times, developers will have an application with legacy code in AngularJS but they’ll want to build new features in ReactJS.

Although it is possible to retire an AngularJS application and build a ReactJS application from scratch, it isn’t a workable solution for large scale applications. In such situations, it is easier to build a React component in isolation and import it into Angular.

In this post, I will help you create a React component in an Angular app using `react2angular`.

### Plan out the app

Here is what we are going to do —

**Given**: An Angular app that renders name of a city and its top sights.

**Goal**: Add a React component to the Angular app. The React component will display a featured image of a sight.

**Plan**: We are going to create a React component, pass in `imageUrl` through `props`, and display the image as a React component.

Let’s get started!

### Step 0: Have an Angular app

For the purpose of this article, let’s keep the complexity of the Angular app simple. I am planning a Euro trip in 2018, hence my Angular app is essentially a bucket-list of places I would like to visit.

Here is what our dataset `bucketlist` looks like:

```js
const bucketlist = [{
  city: 'Venice',
  position: 3,
  sites: ['Grand Canal', 'Bridge of Sighs', 'Piazza San Marco'],
  img: 'https://unsplash.com/photos/ryC3SVUeRgY',
}, {
  city: 'Paris',
  position: 2,
  sites: ['Eiffel Tower', 'The Louvre', 'Notre-Dame de Paris'],
  img: 'https://unsplash.com/photos/R5scocnOOdM',
}, {
  city: 'Santorini',
  position: 1,
  sites: ['Imerovigli', 'Akrotiri', 'Santorini Arts Factory'],
  img: 'https://unsplash.com/photos/hmXtDtmM5r0',
}];
```

This is what `angularComponent.js` looks like:

```js
function AngularComponentCtrl() {
  var ctrl = this;
  ctrl.bucketlist = bucketlist; 
};

angular.module(’demoApp’).component(’angularComponent’, {
  templateUrl: 'angularComponent.html’,
  controller: AngularComponentCtrl
});
```

and this is `angularComponent.html`:

```html
<div ng-repeat="item in $ctrl.bucketlist" ng-sort="item.position">
  <h2>{{item.city}}</h2>
  <p> I want to see <span ng-repeat="sight in item.sights">{{sight}}                 </p></span>
</div>
```

Super simple! Could go to Santorini right now though…

![Image](https://cdn-media-1.freecodecamp.org/images/p83cdbYPyyvGn1IrTNnzC-XDpcWuSm7-1VBu)
_That moment when you come back from vacation and cannot wait for next vacation. Photo by [Unsplash](https://unsplash.com/photos/aapSemzfsOk?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Alexandre Chambon</a> on <a href="https://unsplash.com/search/photos/santorini?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

### Step 1: Install dependencies

Moving from Angular to React world can be a huge pain in the butt if your editor is not configured. Let’s do that first. We are going to install setup linting first.

```bash
npm install --save eslint babel-eslint
```

Next, let’s install `react2angular` . If you have never installed React, you will need to install `react`, `react-dom` and `prop-types` as well.

```bash
npm install --save react2angular react react-dom prop-types
```

### Step 2: Create a React component

Now, we already have an Angular component that renders the name of a city. Next, we need to render the featured image. Let’s assume for now that the image is available to us via `props` (and we will get to how `props` works in just a minute). Our React component looks like this:

```js
import {Component} from 'react';

class RenderImage extends Component {

  render() {
    const imageUrl = this.props.imageUrl;
    return (
      <div>
        <img src={imageUrl} alt=""/>
      </div>
      );
  }
}
```

### Step 3: Pass in props

Remember in `Step 2` we assumed we have an image available via `props`. We are going to populate `props` now. You can pass in dependencies to a React component using `props`. Keep in mind that none of your Angular dependencies are available to the React component. Think of it this way — the React component is like a container connected to the Angular app. If you need the container to inherit information from parent, you will need to explicitly wire it in through `props`.

So, to pass in dependencies, we will add a component `renderImage` in angular and pass in `imageUrl` as a parameter:

```js
 angular.module(’demoApp’, [])
.component(’renderImage’, react2angular(RenderImage,[’imageUrl’]));
```

### Step 4: Include in angular template

Now you can simply import this component in the Angular app like any other component:

```html
<div ng-repeat="item in $ctrl.bucketlist">
  <h2>{{item.city}}</h2>
  <p> I want to see <span ng-repeat="site in item.sites">{{site}}</span>
  <render-image image-url={{item.img}}></render-image>
</div>
```

Ta Da! It’s magic! Not really. It’s hard work and sweat. And coffee. Lots of it.

![Image](https://cdn-media-1.freecodecamp.org/images/-L8XanmrOrxeb9YzUIjafJ21x2KRbuSbmaCy)
_Coffee Coffee Coffee. Photo by [Unsplash](https://unsplash.com/photos/02MLReRp3I8?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Christiana Rivers</a> on <a href="https://unsplash.com/search/photos/new-york?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

> Now go build some React components, you brave warrior!

Special shout out to [David Gee](https://twitter.com/dvdgee) for introducing me to `react2angular` and helping me see the light at the end of the tunnel when I was knee deep in the Angular world.

Resources:

1. [This article](https://medium.com/@panagiotisvrs/angularjs-migration-to-react-redux-2d3bb3a7cc84) helped me a lot.
2. [Official documentation of react2angular](https://github.com/coatue-oss/react2angular)

**If this article helped you, please click the ? button so it reaches other developers.**

