---
title: React shouldComponentUpdate demystified
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-07-30T21:15:20.000Z'
originalURL: https://freecodecamp.org/news/react-shouldcomponentupdate-demystified-c5d323099ef6
coverImage: https://cdn-media-1.freecodecamp.org/images/1*_4NojzFjpzBM4vGMiAoYPw.jpeg
tags:
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Jean-Paul Delimat

  While developing in React have you ever wondered when and why a component’s render()
  method is run? Or when to use less obvious lifecycle methods shouldComponentUpdate()?

  If the answer is yes your app might have performance issue...'
---

By Jean-Paul Delimat

While developing in React have you ever wondered when and why a component’s [render](https://facebook.github.io/react/docs/react-component.html#render)() method is run? Or when to use less obvious lifecycle methods [shouldComponentUpdate](https://facebook.github.io/react/docs/react-component.html#shouldcomponentupdate)()?

If the answer is yes your app might have performance issues. Read through and you will be able to fix them easily.

It all comes down to how React works under the hood. React’s big promise is that it is blazing fast at rendering elements on a page.

To do this React keeps in memory two versions of the DOM:

* the version of the DOM currently displayed
* the next version of the DOM to be displayed

It compares the two and updates the displayed DOM with only the parts that have changed. This process is called [tree reconciliation](https://facebook.github.io/react/docs/reconciliation.html). The root of the tree evaluated for reconciliation is a component which [props](https://facebook.github.io/react/docs/components-and-props.html) have changed.

Great. Now whether you planned for it or not, your web app follows the container/presentational components split to some extent. See [here](https://medium.com/@dan_abramov/smart-and-dumb-components-7ca2f9a7c7d0) and [here](https://medium.com/@learnreact/container-components-c0e67432e005) for definitions. This means that each complex view in your app is made of a container component that holds the logic and has a lot of [display only components](https://www.fullstackreact.com/30-days-of-react/day-11/) as children.

This is a very good pattern. If you look closer though it means that any user interaction on the view will affect the container itself and trigger a render of it and all its children. Say you have a list of elements with a fancy display of text, image and an “Add to favourites” yellow star like button. The minimal model for a list element could be:

```js
product = { 
    imageUrl: '...', 
    title: '...', 
    isFavourite: false
}
```

The list of favourites could come from another source of data. Regardless, your components organisation probably looks something like this:

```js
<Container>
    <ListOfElements
        elements={this.props.elements} 
        onElementChanged={this.props.onElementChanged} 
    />
</Container>
```

The handler is called upon user click and saves the info server side (or persist in a store or whatever) and triggers a change in this.props.elements.

The result of a single click triggers the render of the container and of all the rows in the list just to update one checkbox.

This is where shouldComponentUpdate() comes into play. You can tell React not to render rows that do not need to be using this method.

```js
class ListItem extends Component {
    shouldComponentUpdate(nextProps, nextState) {
        return nextProps.isFavourite != this.props.isFavourite;
    }
    ...
}
```

Here is a concrete case: on a marketplace app project we had a products management view for the sellers. The list had a “load more as the user scrolls down” pattern and an inline item actions “show/hide” to set visibility of each product. Everything was fine when sellers where managing <100 products in their dashboard. Then a given seller started to enter and advertise more than 300 products …

There was a lag of ~600ms before the UI updated after a user clicked the “enable/disable” icon. The lag was definitely visible by the end user. Using the [Chrome profiler](https://developers.google.com/web/tools/chrome-devtools/rendering-tools/) we saw that it took React ~2ms to render a single row. Times 300 … we got up to 600ms. We added the shouldComponentUpdate() checks for the proper conditions. The render time after user click got under 10ms …

**I have put together a small project that allows reproducing this case [here](https://github.com/jpdelima/react-should-component-update-demystified). Run it and read the code comments to see the magic happen.**

### Warning for Redux users

The problem described above may happen more often if you are using [Redux](https://github.com/reactjs/react-redux) and [reselect](https://github.com/reactjs/reselect) (or similar “store based” action pipelines libraries).

With Redux and reselect you push actions to the store and you plug listeners to store changes, a.k.a. selectors. Selectors are globally available in the application and on a large application, it is pretty easy for many components to map to the same selectors. Changes to the store may trigger props changes and thus renders that are completely irrelevant for some components.

Here is the confusing advice: **do not use** shouldComponentUpdate() to prevent renders in such cases. The logic inside shouldComponentUpdate should only look at what is relevant to the component. It should never anticipate the contexts the component is used in. The reason is just that your code would quickly become unmaintainable.

If you have this kind of problems it means your store structure is wrong or selectors are not specific enough. You need to get to a new modelling round.

I recommend [this awesome boilerplate](https://github.com/react-boilerplate/react-boilerplate) guidelines. It promotes store encapsulation per high-level container with a global area for the key data structures that span across the whole application. This is a pretty safe approach to avoid store modelling mistakes.

**Thanks for reading! If you liked it please hit the clap button below. It helps other people see the story.**

