---
title: Want to Learn Vuetify? Here's Our Free 15-Part Course by Gwen Faraday
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-23T16:02:00.000Z'
originalURL: https://freecodecamp.org/news/want-to-learn-vuetify-heres-our-free-15-part-course-by-gwen-faraday
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-23-at-17.06.55.png
tags:
- name: Scrimba
  slug: scrimba
- name: vue
  slug: vue
- name: Vuetify
  slug: vuetify
seo_title: null
seo_desc: 'By Per Harald Borgen

  If you love building apps in Vue.js but struggle to know where to start with UI
  design, look no further than Vuetify. It''s a UI library containing handcrafted
  material components which give apps a beautiful finish and professiona...'
---

By Per Harald Borgen

If you love building apps in Vue.js but struggle to know where to start with UI design, look no further than Vuetify. It's a UI library containing handcrafted material components which give apps a beautiful finish and professional feel.

## Why learn Vuetify?

Vuetify is the most popular component library for Vue.js, enabling you to create great-looking, accessible apps even if UI design isn't your area. 

While the library has over 80 elements ready to use straight out the box, it also allows you to create custom elements, giving your apps a clean yet bespoke feel.

This article takes you through Scrimba's free [two-hour Vuetify course](https://scrimba.com/course/gvuetify?utm_source=dev.to&utm_medium=referral&utm_campaign=gvuetify_launch_article) by Gwen Faraday. The course teaches you all the core skills needed to get started with Vuetify, including:

- Typography
- Spacing
- Buttons
- Navigation
- Grid
- Card

In the first half, Gwen introduces all the Vuetify elements needed to build a great app. As with all Scrimba courses, you can pause the scrims and explore the code.

The second half lets you get your hands dirty by building a webshop. This puts your new skills to good use and lets you apply your newfound knowledge.

By the end, you'll be fully versed in building professionally-styled apps with Vuetify.

## Intro to the Instructor

Gwen Faraday is a software engineer, author, speaker, and & content creator who also runs a Youtube channel, [the Faraday Academy](https://www.youtube.com/channel/UCxA99Yr6P_tZF9_BgtMGAWA/featured), where she teaches a wide range of subjects including Vue.js and Vuetify. This makes her the perfect teacher to take you through this learning journey and bring your Vuetify skills to the next level.

## Prerequisites

To learn the most from this tutorial, you'll need a decent understanding of HTML, CSS, Javascript and Vue.js. If you're not there yet, check out Scrimba's great free courses to get you up to speed:

- [HTML and CSS](https://scrimba.com/course/ghtmlcss?utm_source=dev.to&utm_medium=referral&utm_campaign=gvuetify_launch_article)
- [Javascript](https://scrimba.com/course/gintrotojavascript?utm_source=dev.to&utm_medium=referral&utm_campaign=gvuetify_launch_article)
- [Vue.js](https://scrimba.com/course/glearnvue?utm_source=dev.to&utm_medium=referral&utm_campaign=gvuetify_launch_article)

If you’re ready to hit the ground running with Vuetify, let’s get into it!

## Intro to Vuetify

[In the first cast](https://scrimba.com/p/pP4xZu3/cEKyEkuB?utm_source=dev.to&utm_medium=referral&utm_campaign=gvuetify_launch_article), Gwen introduces us to Vuetify and shares the two Github repositories where she has stored all the code, [basic-components](https://github.com/gwenf/vuetify-basic-components) and [vuetify-responsive](https://github.com/gwenf/vuetify-responsive). This allows us to download the code and try it out for ourselves.

## What is Material Design?

[Next up](https://scrimba.com/p/pP4xZu3/c4PDDZtg?utm_source=dev.to&utm_medium=referral&utm_campaign=gvuetify_launch_article), we learn about Material Design, a standard developed by Google for implementing accessible, user-friendly interfaces.

The Material Standard provides a set of rules for the most common elements found on web pages including buttons, text, navigation and more advanced features such as movement and elevation.

Vuetify takes the hard work out of implementing this standard by providing a bunch of ready-made compliant UI elements which we can add to our Vue.js application straight out the box.

## First Look at Vuetify Code

[In the next cast](https://scrimba.com/p/pP4xZu3/ckPbepSM?utm_source=dev.to&utm_medium=referral&utm_campaign=gvuetify_launch_article), Gwen gives us our first look at Vuetify code by instantiating a Vue application, adding a Vuetify property and creating a new Vuetify object:

```js
new Vue({
	el: "#app",
	vuetify: new Vuetify({}),
	data: {
		message: "Using Single File Components",
	},
});
```

Next, Gwen shows us the `<v-app>` element, which is the root component of all Vuetify elements (Vuetify components must fall within `<v-app>`):

```vue
<v-app>
     <v-content>
          <playground></playground>
     </v-content>
</v-app>
```

## Typography

[![Vuetify typography](https://dev-to-uploads.s3.amazonaws.com/i/lrmuhh5orzx32c4jdlsd.png)](https://scrimba.com/p/pP4xZu3/cMqPmeTG?utm_source=dev.to&utm_medium=referral&utm_campaign=gvuetify_launch_article)
_Click the image to access the course._

In [the next scrim](https://scrimba.com/p/pP4xZu3/cMqPmeTG?utm_source=dev.to&utm_medium=referral&utm_campaign=gvuetify_launch_article), we see some of the options Vuetify offers to handle typography, including headings, titles, subtitles and body text. We also see how to change text color and background color.

```vue
<v-card-text>
     <h1 class="display-4 purple yellow--text">Heading 1</h1>
     <h2 class="display-3">Heading 2</h2>
     <h3 class="display-2">Heading 3</h3>
     <h4 class="title">Title</h4>
     <h5 class="subtitle-1">Subtitle</h5>
     <p class="body-1">Body</p>
</v-card-text>
```

Finally, we see how to use Vuetify classes to adjust font weight and style:

```vue
<h1 class="font-italic font-weight-light">Heading 1</h1>
```

**Note:** Vuetify classes override any other styles that the browser applies to HTML tags.

## Spacing

[Next up](https://scrimba.com/p/pP4xZu3/cD7pnzSw?utm_source=dev.to&utm_medium=referral&utm_campaign=gvuetify_launch_article), we explore some of the spacing classes in Vuetify, which allow us to add margins and padding. We also see how to change spacing size.

```vue
<h3 class="ml-5">Spacing</h3>
```

Best of all, Gwen also shows us how Vuetify classes can help with that holy grail of app styling - centering an element! Click through to the course to find out more.

## Buttons

[![Vuetify buttons](https://dev-to-uploads.s3.amazonaws.com/i/ollkzqisck44bqdnc1r9.png)](https://scrimba.com/p/pP4xZu3/crmrBwtP?utm_source=dev.to&utm_medium=referral&utm_campaign=gvuetify_launch_article)
_Click the image to access the course._

In the [next scrim](https://scrimba.com/p/pP4xZu3/crmrBwtP?utm_source=dev.to&utm_medium=referral&utm_campaign=gvuetify_launch_article), we look at some of the options available with Vuetify's button component, including buttons with text, icons or both.

```vue
<v-btn large block>Submit</v-btn>
```

Lastly, we look at how to build custom buttons using classes from earlier.

```vue
<button v-ripple class="elevation-2 py-2 px-4">
     Submit
</button>
```

## Navigation

[![Vuetify navigation](https://dev-to-uploads.s3.amazonaws.com/i/je40l0odaw1l68pi8a71.png)](https://scrimba.com/p/pP4xZu3/czkwwQCw?utm_source=dev.to&utm_medium=referral&utm_campaign=gvuetify_launch_article)
_Click the image to access the course._

[Next up](https://scrimba.com/p/pP4xZu3/czkwwQCw?utm_source=dev.to&utm_medium=referral&utm_campaign=gvuetify_launch_article), we look at the two main navigation options available in Vuetify,`<v-app-bar>` and `<v-toolbar>`. Both navigation elements provide automatic button and icon sizing, navigation icons and the ability to handle list dropdowns.

```vue
<v-toolbar color="deep-purple accent-4" dense dark>
    <v-app-bar-nav-icon></v-app-bar-nav-icon>
<v-toolbar-title>App Title</v-toolbar-title></v-toolbar>
```

[Click through](https://scrimba.com/p/pP4xZu3/czkwwQCw?utm_source=dev.to&utm_medium=referral&utm_campaign=gvuetify_launch_article) to see all this in action!

## Grid

[![Vuetify grid](https://dev-to-uploads.s3.amazonaws.com/i/hddtxtqh91j6z9gjb1up.png)](https://scrimba.com/p/pP4xZu3/cWKBnPSV?utm_source=dev.to&utm_medium=referral&utm_campaign=gvuetify_launch_article)
_Click the image to access the course._

In [the next scrim](https://scrimba.com/p/pP4xZu3/cWKBnPSV?utm_source=dev.to&utm_medium=referral&utm_campaign=gvuetify_launch_article), Gwen takes us through Vuetify's grid system, which is split into 12 columns, with five built-in media breakpoints for handling different screen sizes.

```vue
<v-row>
    <v-col cols="12" sm="6">
        <v-card
        class="pa-2"
        outlined
        tile
        >
        Column
        </v-card>
    </v-col>
</v-row>
```

## Card

[![Vuetify card](https://dev-to-uploads.s3.amazonaws.com/i/dbh0863c4we6t4sncpf2.png)](https://scrimba.com/p/pP4xZu3/cdNW42t8?utm_source=dev.to&utm_medium=referral&utm_campaign=gvuetify_launch_article)
_Click the image to access the course._

In [this cast](https://scrimba.com/p/pP4xZu3/cdNW42t8?utm_source=dev.to&utm_medium=referral&utm_campaign=gvuetify_launch_article), Gwen explains that Vuetify uses a `<v-card>` component as the wrapper for any UI card. This component can take props, classes and slots and has custom events, allowing for neat, well-aligned cards in any use case.

```vue
 <v-card-title>
    <v-icon
        large
        left
    >
        mdi-twitter
    </v-icon>
    </v-card-title>

    <v-card-text class="headline font-weight-bold">
    "Vue Rocks!"
    </v-card-text>

</v-card>
```

Gwen also introduces us to the `<v-spacer>` element, which lets us easily add whitespace between elements.

Finally, we check out the `Playground.vue` file - a space for us to explore the features of Vuetify Gwen has shown us so far. Head over [to the course](https://scrimba.com/p/pP4xZu3/cdNW42t8?utm_source=dev.to&utm_medium=referral&utm_campaign=gvuetify_launch_article) to try it out for yourself and see what Vuetify can do.

## Store Navigation

[![Vuetify web store navigation](https://dev-to-uploads.s3.amazonaws.com/i/tc2s63qss1f3tc7vyyhu.png)](https://scrimba.com/p/pP4xZu3/cMZMQbu9?utm_source=dev.to&utm_medium=referral&utm_campaign=gvuetify_launch_article)
_Click the image to access the course._

[Next](https://scrimba.com/p/pP4xZu3/cMZMQbu9?utm_source=dev.to&utm_medium=referral&utm_campaign=gvuetify_launch_article), it's time to start building our store application. Gwen starts us off by adding a navigation bar including responsiveness and a drawer menu. We also run through some options for styling, including icons and a dense menu.

## Home Page

[Next up](https://scrimba.com/p/pP4xZu3/c33vv6fz?utm_source=dev.to&utm_medium=referral&utm_campaign=gvuetify_launch_article), it's time to add a home page. Gwen adds the header and a footer and then sets us the challenge of coding the mid-section using the mock-ups provided. Head over [to the screencast](https://scrimba.com/p/pP4xZu3/c33vv6fz?utm_source=dev.to&utm_medium=referral&utm_campaign=gvuetify_launch_article) to test out your new Vuetify skills and compare your work to Gwen's solution.

To finish off, Gwen shows us the `<v-snackbar>` element, which can be used to notify a user when a product has been added to the cart.

```vue
<v-snackbar
	v-model="$store.state.snackbar.show"
	:multi-line="true"
	:right="true"
	:top="true"
	:timeout="6000"
	:color="$store.state.snackbar.variant"
>
    {{ $store.state.snackbar.message }}
    <v-btn
    dark
    text
    @click="$store.commit('updateSnackbar', { show: false })"
    >
    Close
    </v-btn>
</v-snackbar>
```

## Store Page

[![Vuetify web store page](https://dev-to-uploads.s3.amazonaws.com/i/m1d909j9guwo0q1da9jj.png)](https://scrimba.com/p/pP4xZu3/cvdrn6Ar?utm_source=dev.to&utm_medium=referral&utm_campaign=gvuetify_launch_article)
_Click the image to access the course._

[In the next Scrim](https://scrimba.com/p/pP4xZu3/cvdrn6Ar?utm_source=dev.to&utm_medium=referral&utm_campaign=gvuetify_launch_article) we build out our store page using Vuetify grid elements. First up, we add product cards by reusing the cards we built for our home page. Next, Gwen challenges us to build out a sidebar with the `<v-sheet>` and `<v-expansion-panels>` elements.

Head over [to the cast](https://scrimba.com/p/pP4xZu3/cvdrn6Ar?utm_source=dev.to&utm_medium=referral&utm_campaign=gvuetify_launch_article) to give the challenge a try.

## Cart Page

[![Vuetify cart page](https://dev-to-uploads.s3.amazonaws.com/i/drbsnxpy6p95kzj3aph5.png)](https://scrimba.com/p/pP4xZu3/caZyp7um?utm_source=dev.to&utm_medium=referral&utm_campaign=gvuetify_launch_article)
_Click the image to access the course._

[Next up](https://scrimba.com/p/pP4xZu3/caZyp7um?utm_source=dev.to&utm_medium=referral&utm_campaign=gvuetify_launch_article), we add a cart page to our app. Once again, Gwen sets us the challenge of coding out the page as per her mock-ups, which is great practice for real-world coding and flexes the muscle memory needed to become a Vuetify wizard.

Click through to give the challenge your best shot before comparing your work with Gwen's final code. Don't forget, you can always look back at the previous scrims or check out the Vuetify docs if you're having trouble.

## Checkout Screen

In the final code scrim, we build a simple checkout flow using the `<v-stepper>` element.

```vue
<v-stepper-header>
    <v-stepper-step
        step="1"
        :complete="step > 1"
    />
    <v-divider />
    <v-stepper-step
        step="2"
        :complete="step > 2"
    />
    <v-divider />
    <v-stepper-step
        step="3"
    />
    </v-stepper-header>
```

To finish the course, Gwen points out that there are a few features in the mockups which we haven't covered and encourages us to have a go at coding them ourselves using Scrimba's interactive interface.

## Conclusion

A huge well done for completing the course! I hope you've found it useful and now have the confidence to build stunning apps using Vuetify. Why not continue your learning journey by checking out the huge range of other topics available over at [Scrimba](https://scrimba.com/?utm_source=dev.to&utm_medium=referral&utm_campaign=gvuetify_launch_article)?

Wherever you go next, happy coding :)


%[https://www.youtube.com/watch?v=rJIRv-_oYnA]


