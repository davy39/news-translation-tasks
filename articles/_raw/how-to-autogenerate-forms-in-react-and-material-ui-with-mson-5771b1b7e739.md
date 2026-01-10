---
title: How to autogenerate forms in React and Material-UI with MSON
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-22T20:34:18.000Z'
originalURL: https://freecodecamp.org/news/how-to-autogenerate-forms-in-react-and-material-ui-with-mson-5771b1b7e739
coverImage: https://cdn-media-1.freecodecamp.org/images/0*WKoVhYdsFzzh3_21.png
tags:
- name: Design
  slug: design
- name: forms
  slug: forms
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Geoff Cox

  Implementing great forms can be a real time-waster. With just a few lines of JSON,
  you can use MSON to generate forms that perform real-time validation and have a
  consistent layout. And, MSON comes with a bunch of cool stuff like date pi...'
---

By Geoff Cox

Implementing great forms can be a real time-waster. With just a few lines of JSON, you can use [MSON](https://github.com/redgeoff/mson) to generate forms that perform real-time validation and have a consistent layout. And, [MSON](https://github.com/redgeoff/mson) comes with a bunch of cool stuff like date pickers, masked fields and field collections.

**Disclaimer**: this post is geared towards those wishing to use Material-UI with React. Future versions of MSON will support other rendering layers.

#### What the heck is MSON?

[MSON](https://github.com/redgeoff/mson) is a declarative language that has the capabilities of an object-oriented language. The MSON compiler allows you to generate apps from JSON. The ultimate goal of MSON is to allow anyone to develop software visually. You can also use pieces of MSON to turbo charge your form development.

### A Basic Form Generated with MSON

Simply declare your form in JSON. Then let the MSON compiler and UI-rendering layer autogenerate your UI:

Did you try submitting the form without filling in any values? Did you notice how real-time validation is automatically baked in?

Now, let’s take a closer look at what is happening. The first block of code contains a JSON definition that describes the fields in the form:

This code adds the following fields to your form:

1. The _Text_ component displays some [markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
2. The _PersonNameField_ is used to capture a person’s first and last names
3. The _DateField_ allows a user to choose a date using a slick date picker
4. The _PhoneField_ uses an input mask and country codes to guide the user when entering a phone number
5. The _SubmitField_ contains a _Send_ icon and allows the user to submit the form via a click or by pressing enter

Now, let’s take a look at the code that renders the component and handles the submit event:

That’s it!? Yup! The [mson-react](https://github.com/redgeoff/mson-react) layer **automatically** knows how to render the form component. It uses [pub/sub](https://en.wikipedia.org/wiki/Publish%E2%80%93subscribe_pattern) and [Pure Components](https://reactjs.org/docs/react-api.html#reactpurecomponent) to keep the rendering up-to-date.

When there is no validation error and the user clicks the submit button, an event with the name equal to the button’s name is emitted. In our case, this event is called _submit._ Therefore, we can define a handler using the _onSubmit_ property. To keep things simple, we just alert the user of the entered values. Typically you want to do something like contact an API, redirect, etc…

### Basic Form 2

Now, let’s go a bit deeper into the CRUD with a different example:

The first thing you may notice are the [validators](https://github.com/redgeoff/mson#validators) in the definition:

Each field has a default set of [validators](https://github.com/redgeoff/mson#validators), e.g. the _EmailField_ ensures that email addresses are in a valid format. You can also extend these validators for a particular field or even for an entire form. For example, you can prevent the user from entering [_nope@example.com_](mailto:nope@example.com)_._

Next, let’s take a look at the code that loads the initial values when the component is mounted:

This code could just as easily be replaced by code that retrieves the values from some API asynchronously.

Finally, we use a more sophisticated event listener to handle the submit action. In a real-world app, you’d probably want to send a request to an API to save the data. You would receive a response from this API. If you receive an error, e.g. the email address is already in use, you can present this error to the user:

### [Live Demo](https://redgeoff.github.io/mson-react/)

This post only touches on a small piece of what you can do using [MSON](https://github.com/redgeoff/mson). Because [MSON](https://github.com/redgeoff/mson) is a full-featured language, you can declare all types of cool components. If you are interested in seeing more live examples, check out the [live demo](https://redgeoff.github.io/mson-react).

![Image](https://cdn-media-1.freecodecamp.org/images/0*WKoVhYdsFzzh3_21.png)
_[https://redgeoff.github.io/mson-react](https://redgeoff.github.io/mson-react/" rel="noopener" target="_blank" title=")_

### Wrap It Up!

If you are using React and Material-UI, you can speed up your app development by autogenerating your forms from JSON. This can be particularly useful if you need to bootstrap an app quickly and don’t want to have to worry about building a UI from scratch.

If you liked this post, please give it a clap or two. Happy [autogenerating](https://github.com/redgeoff/mson)!

### About the Author

Geoff Cox is the creator of [MSON](https://github.com/redgeoff/mson), a new declarative programming language that will allow anyone to develop software visually. He’s been self-employed for the greater part of the last 15 years. He loves taking on ambitious, yet wife-maddening, projects like [creating a database](https://github.com/delta-db/deltadb) and [distributed data syncing system](https://github.com/redgeoff/spiegel). You can reach him [@redgeoff7](https://twitter.com/redgeoff7) or at [github](https://github.com/redgeoff).

