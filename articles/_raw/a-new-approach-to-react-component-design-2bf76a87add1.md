---
title: A New Approach to React Component Design
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-10T22:39:24.000Z'
originalURL: https://freecodecamp.org/news/a-new-approach-to-react-component-design-2bf76a87add1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*nFP5vJPVTEaimO8n4jPKgA.gif
tags:
- name: Design
  slug: design
- name: design patterns
  slug: design-patterns
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Austin Malerba

  In 2015, Dan Abramov wrote an article, Presentational and Container Components,
  that some React new-comers misconstrued as commandments. In fact, I myself stumbled
  upon the article and many others echoing its teachings and I thought...'
---

By Austin Malerba

In 2015, Dan Abramov wrote an article, [Presentational and Container Components](https://medium.com/@dan_abramov/smart-and-dumb-components-7ca2f9a7c7d0), that some React new-comers misconstrued as commandments. In fact, I myself stumbled upon the article and many others echoing its teachings and I thought, _this must be the best way to separate concerns amongst components_.

But, Dan Abramov himself later addressed the community for clinging to the design patterns he outlined.

![Image](https://cdn-media-1.freecodecamp.org/images/1*5TKk6it2JOAomEj-IwKgCg.png)

In working with React for over a year now, I’ve stumbled into my own design patterns and here I will try to formalize them. Take these ideas with a grain of salt, they’re just my own observations that I have found constructive.

### Escaping the Dichotomy

For a long time, components have been broadly classified as either smart or dumb, container or presentational, stateful or stateless, pure or impure. There’s a lot of terminology, but they all mean about the same thing. Smart components know how to tie together your application and dumb components just take in data to present to the end user. This is a useful distinction, but it’s really not how I find myself thinking while designing components.

The problem with the Container vs Presentational mindset is that it tries too hard to define component responsibilities in terms of state, logic, and other aspects of a component’s inner-workings.

Component design is better approached by deferring the implementation details and thinking in terms of **component interfaces**. It’s particularly important to think about what kind of **customizations** a component should allow and what kind of **implicit and explicit dependencies** a component should include.

### Introducing the Trichotomy

Trichotomy? Is that even a word? I don’t know, but you get the idea. I’ve come to think of React components as falling into one of three bins.

#### Universal Components

These are components that can be used **many times in any application**.

These components:

* Should be **reusable**
* Should be **highly customizable**
* Should **not be aware of application-specific code** including models, stores, services, etc.
* Should **minimize dependencies** on third party libraries
* Should rarely be used directly in your application
* Should be used as **building blocks for Global components**
* May end with the “Base” suffix (eg. ButtonBase, ImageBase)

These are foundational components that are application-agnostic and aren’t necessarily to be used directly in your View components because they are often too customizable. To use them directly in your View components would mean a lot of copying and pasting of the same boiler plate. You’d also risk developers abusing the components’ highly customizable nature in ways that create an inconsistent experience across your application.

#### Global Components

These are components that can be used **many times in one application**.

These components:

* Should be **reusable**
* Should be **minimally customizable**
* May use **application-specific code**
* Should **implement Universal components**, restricting their customizability
* Should be used as **building blocks for View components**
* Often tie one-to-one with model instances (eg. DogListItem, CatCard)

These components are reusable within your application but are not easily transferred to other applications because they depend on application logic. These are the building blocks for View components and other Global components.

They should be minimally customizable to ensure consistency across your application. Applications shouldn’t have thirty different button variations, but rather should have a handful of different button variations. This should be enforced by taking a highly customizable Universal ButtonBase component and baking into it styles and functionality in the form of a Global Button component. Global components often take another form as representations of domain model data.

#### View Components

These are components that are used **only once in your application**.

These components:

* Should **not** be concerned about reusability
* Are likely to **manage state**
* Receive **minimal props**
* Should tie together Global components (and possibly Universal components)
* Often **resolve application routes**
* Often maintain a dedicated plot of viewport real estate
* Often have a high number of dependencies
* Should be **building blocks for your application**

These are the highest level components of your application that glue together reusable components and even other Views. These will often be the components that resolve routes and may show in the form of page-level components. They are heavy in state and light in props. These are what Dan Abramov would consider container components.

#### The PromiseButton

Let’s take a look at the Universal and Global implementations of a promise button and see how they compare. A promise button acts like an ordinary button unless the onClick handler returns a promise. In the case of a returned promise, the button can conditionally render content based on the promise state.

<script src="https://gist.github.com/malerba118/86465f12da532d57f32d607e90f9d72b.js"></script>

<script src="https://gist.github.com/malerba118/ce2eccea26a307ac852bf0f47dd696be.js"></script>

Notice how the PromiseButtonBase allows us to control what to render at any point in the promise life-cycle, but the PromiseButton bakes in the teal PulseLoader during the pending state. Now any time we use the PromiseButton, we’re guaranteed a teal loading animation and we don’t have to worry about duplicating that code or providing an inconsistent loading experience by including multiple loading animations of multiple colors across our application. The PromiseButtonBase is customizable, but the PromiseButton is restrictive.

#### Directory Structure

The following illustrates how we might organize components following this pattern.

```
App/
  App.js
  Views/
    DogListView/
  Global/
    Models/
      Dog/
        DogListItem/
    Image/
    PromiseButton/
Universal/
  ImageBase/
  PromiseButtonBase/
```

#### Component Dependencies

Below illustrates how the above components depend on one another.

```javascript
/* App.js */
import { DogListView } from './Views'

/* DogListView.js */
import { DogListItem } from 'App/Global/Models/Dog'

/* DogListItem.js */
import Image from '../../Image',
import PromiseButton from '../../PromiseButton'

/* Image.js */
import { ImageBase } from 'Universal'

/* PromiseButton.js */
import { PromiseButtonBase } from 'Universal'
```

Our View component depends on a Global component and our Global components depend on other Global components as well as Universal components. This dependency flow will be pretty common. Notice also the use of absolute and relative imports. It’s nice to use relative imports when pulling in dependencies that reside within the same module. Also, it’s nice to use absolute imports when pulling in dependencies across modules or when your directory structure is deeply nested or frequently changing.

The problem with the Container vs Presentational model is that it tries too hard to define component responsibilities in terms of component inner-workings. The key takeaway is to view component design in terms of **component interfaces**. What matters less is the implementation that allows the component to satisfy its contract. It’s important to think about what kind of **customizations** a component should allow and what kind of **implicit and explicit dependencies** a component should include.

If you’ve found these thoughts helpful and would like to see more of my ideas, feel free to check out this [repo](https://github.com/malerba118/react-redux-template) which I use to maintain my thoughts and best practices for writing React/Redux apps.

