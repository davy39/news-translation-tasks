---
title: How the “Golden Rule” of React components can help you write better code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-26T21:23:23.000Z'
originalURL: https://freecodecamp.org/news/how-the-golden-rule-of-react-components-can-help-you-write-better-code-127046b478eb
coverImage: https://cdn-media-1.freecodecamp.org/images/1*KzKoXW7PovSAUUn8htYbnw@2x.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Rico Kahler

  And how hooks come into play

  Recently I’ve adopted a new philosophy that changes the way I make components. It’s
  not necessarily a new idea but rather a subtle new way of thinking.

  The Golden Rule of Components


  Create and define compo...'
---

By Rico Kahler

#### And how hooks come into play

Recently I’ve adopted a new philosophy that changes the way I make components. It’s not necessarily a new idea but rather a subtle new way of thinking.

#### The Golden Rule of Components

> Create and define components in the most natural way, solely considering what they need to function.

Again, it’s a subtle statement and you may think you already follow it but it’s easy to go against this.

For example, let’s say you have the following component:

![Image](https://cdn-media-1.freecodecamp.org/images/1*nF_5kuYHigZuwdq99vRJ8g.png)
_PersonCard_

If you were defining this component “naturally” then you’d probably write it with the following API:

```js
PersonCard.propTypes = {
  name: PropTypes.string.isRequired,
  jobTitle: PropTypes.string.isRequired,
  pictureUrl: PropTypes.string.isRequired,
};
```

Which is pretty straightforward — solely looking at what it needs to function, you just need a name, job title, and picture URL.

But let’s say you have a requirement to show an “official” picture depending on user settings. You might be tempted to write an API like so:

```js
PersonCard.propTypes = {
  name: PropTypes.string.isRequired,
  jobTitle: PropTypes.string.isRequired,
  officialPictureUrl: PropTypes.string.isRequired,
  pictureUrl: PropTypes.string.isRequired,
  preferOfficial: PropTypes.boolean.isRequired,
};
```

It may seem like the component needs those extra props to function, but in actuality, the component doesn’t look any different and doesn’t need those extra props to function. What these extra props do is couple this `preferOfficial` setting with your component and makes any use of the component outside that context feel really unnatural.

### Bridging the gap

So if the logic for switching the picture URL doesn’t belong in the component itself, where does it belong?

How about an `index` file?

We’ve adopted a folder structure where every component goes into a self-titled folder where the `index` file is responsible for bridging the gap between your “natural” component and the outside world. We call this file the “container” (inspired from [React Redux’s concept of “container” components](https://redux.js.org/basics/usage-with-react#presentational-and-container-components)).

```
/PersonCard
  -PersonCard.js ------ the "natural" component
  -index.js ----------- the "container"
```

We define **containers** as the piece of code that bridges that gap between your natural component and the outside world. For this reason, we also sometimes call these things “injectors”.

Your **natural component** is the code you’d create if you were only shown a picture of what you were required make (without the details of how’d you’d get data or where it’d be placed in the app — all you know is that it should function).

The **outside world** is a keyword we’ll use to refer to any resource your app has (e.g. the Redux store) that can be transformed to satisfy your natural component’s props.

**Goal for this article:** How can we keep components “natural” without polluting them with junk from the outside world? Why is that better?

> **_Note:_** _Though inspired by [Dan’s Abramov](https://medium.com/@dan_abramov/smart-and-dumb-components-7ca2f9a7c7d0) and [React Redux’s](https://redux.js.org/basics/usage-with-react#presentational-and-container-components) terminology, our definition of “containers” goes slightly beyond that and is subtly different._

> _The only difference between [Dan Abramov’s container](https://medium.com/@dan_abramov/smart-and-dumb-components-7ca2f9a7c7d0) and ours is only at the conceptual level. Dan’s says there are two kinds of components: presentational components and container components. We take this a step further and say there are components and then containers._

> _Even though we implement containers with components, we don’t think of containers as components on a conceptual level. That’s why we recommend putting your container in the `index` file — because it’s a bridge between your natural component and the outside world and doesn’t stand on its own._

Though this article is focused on components, containers take up the bulk of this article.

Why?

Making natural components — Easy, fun even.  
Connecting your components to the outside world — A bit harder.

The way I see it, there are three major reasons you’d pollute your natural component with junk from the outside world:

1. Weird data structures
2. Requirements outside of the scope of the component (like the example above)
3. Firing events on updates or on mount

The next few sections will try to cover these situations with examples with different types of container implementations.

### Working with weird data structures

Sometimes in order to render the required information, you need to link together data and transform it into something that’s more sensible. For lack of a better word, “weird” data structures are simply data structures that are unnatural for your component to use.

It’s very tempting to pass weird data structures directly into a component and do the transforming inside the component itself, but this leads to confusing and often hard to test components.

I caught myself falling into this trap recently when I was tasked to create a component that got its data from a particular data structure we use to support a particular type of form.

![Image](https://cdn-media-1.freecodecamp.org/images/1*hFOPWOxkedUEb851jdAXjA.gif)
_The component itself_

```js
ChipField.propTypes = {
  field: PropTypes.object.isRequired,      // <-- the "weird" data structure
  onEditField: PropTypes.func.isRequired,  // <-- and a weird event too
};
```

The component took in this weird `field` data structure as a prop. In practicality, this might’ve been fine if we never had to touch the thing again, but it became a real issue when we were asked to use it again in a different spot unrelated to this data structure.

Since the component required this data structure, it was impossible to reuse it and it was confusing to refactor. The tests we originally wrote also were confusing because they mocked this weird data structure. We had trouble understanding the tests and trouble re-writing them when we eventually refactored.

Unfortunately, weird data structures are unavoidable, but using containers is a great way to deal with them. One takeaway here is that architecting your components in this way gives you the _option_ of extracting and graduating the component into a reusable one. If you pass a weird data structure into a component, you lose that option.

> **_Note:_** _I’m not suggesting that all components you make should be generic from the beginning. The suggestion is to think about what your component does on a fundamental level and then bridge the gap. As a consequence, you’re more likely to have the_ option _to graduate your component into a reusable one with minimal work._

#### Implementing containers using function components

If you’re strictly mapping props, a simple implementation option is to use another function component:

```js
import React from 'react';
import PropTypes from 'prop-types';

import getValuesFromField from './helpers/getValuesFromField';
import transformValuesToField from './helpers/transformValuesToField';

import ChipField from './ChipField';

export default function ChipFieldContainer({ field, onEditField }) {
  const values = getValuesFromField(field);
  
  function handleOnChange(values) {
    onEditField(transformValuesToField(values));
  }
  
  return <ChipField values={values} onChange={handleOnChange} />;
}

// external props
ChipFieldContainer.propTypes = {
  field: PropTypes.object.isRequired,
  onEditField: PropTypes.func.isRequired,
};
```

And the folder structure for a component like this looks something like:

```
/ChipField
  -ChipField.js ------------------ the "natural" chip field
  -ChipField.test.js
  -index.js ---------------------- the "container"
  -index.test.js
  /helpers ----------------------- a folder for the helpers/utils
    -getValuesFromField.js
    -getValuesFromField.test.js
    -transformValuesToField.js
    -transformValuesToField.test.js
```

You might be thinking “that’s too much work” — and if you are then I get it. It may seem like there is more work to do here since there are more files and a bit of indirection, but here’s the part you’re missing:

```js
import { connect } from 'react-redux';

import getPictureUrl from './helpers/getPictureUrl';

import PersonCard from './PersonCard';

const mapStateToProps = (state, ownProps) => {
  const { person } = ownProps;
  const { name, jobTitle, customPictureUrl, officialPictureUrl } = person;
  const { preferOfficial } = state.settings;
  
  const pictureUrl = getPictureUrl(preferOfficial, customPictureUrl, officialPictureUrl);
  
  return { name, jobTitle, pictureUrl };
};

const mapDispatchToProps = null;

export default connect(
  mapStateToProps,
  mapDispatchToProps,
)(PersonCard);
```

It’s still the same amount of work regardless if you transformed data outside of the component or inside the component. The difference is, when you transform data outside of the component, you’re giving yourself a more explicit spot to test that your transformations are correct while also separating concerns.

### Fulfilling requirements outside of the scope of the component

Like the Person Card example above, it’s very likely that when you adopt this “golden rule” of thinking, you’ll realize that certain requirements are outside the scope of the actual component. So how do you fulfill those?

You guessed it: Containers ?

You can create containers that do a little bit of extra work to keep your component natural. When you do this, you end up with a more focused component that is much simpler and a container that is better tested.

Let’s implement a PersonCard container to illustrate the example.

#### Implementing containers using higher order components

React Redux uses [higher order components](https://reactjs.org/docs/higher-order-components.html) to implement containers that push and map props from the Redux store. Since we got this terminology from React Redux, it comes with no surprise that [React Redux’s `connect` is a container](https://redux.js.org/basics/usage-with-react#implementing-container-components).

Regardless if you’re using a function component to map props, or if you’re using higher order components to connect to the Redux store, the golden rule and the job of the container are still the same. First, write your natural component and then use the higher order component to bridge the gap.

Folder structure for above:

```
/PersonCard
  -PersonCard.js ----------------- natural component
  -PersonCard.test.js
  -index.js ---------------------- container
  -index.test.js
  /helpers
    -getPictureUrl.js ------------ helper
    -getPictureUrl.test.js
```

> **_Note:_** _In this case, it wouldn’t be too practical to have a helper for `getPictureUrl`. This logic was separated simply to show that you can. You also might’ve noticed that there is no difference in folder structure regardless of container implementation._

If you’ve used Redux before, the example above is something you’re probably already familiar with. Again, this golden rule isn’t necessarily a new idea but a subtle new way of thinking.

Additionally, when you implement containers with higher order components, you also have the ability to functionally compose higher order components together — passing props from one higher order component to the next. Historically, we’ve chained multiple higher order components together to implement a single container.

> **_2019 Note:_** _The React community seems to be moving away from higher order components as a pattern._

> _I would also recommend the same. My experience when working with these is that they can be confusing for team members who aren’t familiar with functional composition and they can cause what is known as “wrapper hell” where components are wrapped too many times causing significant performance issues._

> _Here are some related articles and resources on this: [Hooks talk](https://youtu.be/dpw9EHDh2bM?t=710) (2018) [Recompose talk](https://youtu.be/zD_judE-bXk?t=1101) (2016) , [Use a Render Prop!](https://cdb.reacttraining.com/use-a-render-prop-50de598f11ce) (2017), [When to NOT use Render Props](https://blog.kentcdodds.com/when-to-not-use-render-props-5397bbeff746) (2018)._

### You promised me hooks

#### Implementing containers using hooks

Why are hooks featured in this article? Because implementing containers becomes a lot easier with hooks.

If you’re not familiar with React hooks, then I would recommend watching [Dan Abramov’s and Ryan Florence’s talks introducing the concept during React Conf 2018](https://youtu.be/dpw9EHDh2bM).

The gist is that hooks are the React team’s response to the issues with [higher order components](https://reactjs.org/docs/higher-order-components.html) and [similar patterns](https://reactjs.org/docs/render-props.html). React hooks are intended to be a superior replacement pattern for both in most cases.

This means that implementing containers can be done with a function component and hooks ?

In the example below, we’re using the hooks `useRoute` and `useRedux` to represent the “outside world” and we’re using the helper `getValues` to map the outside world into `props` usable by your natural component. We’re also using the helper `transformValues` to transform your component’s output to the outside world represented by `dispatch`.

```js
import React from 'react';
import PropTypes from 'prop-types';

import { useRouter } from 'react-router';
import { useRedux } from 'react-redux';

import actionCreator from 'your-redux-stuff';

import getValues from './helpers/getVaules';
import transformValues from './helpers/transformValues';

import FooComponent from './FooComponent';

export default function FooComponentContainer(props) {
  // hooks
  const { match } = useRouter({ path: /* ... */ });
  // NOTE: `useRedux` does not exist yet and probably won't look like this
  const { state, dispatch } = useRedux();

  // mapping
  const props = getValues(state, match);
  
  function handleChange(e) {
    const transformed = transformValues(e);
    dispatch(actionCreator(transformed));
  }
  
  // natural component
  return <FooComponent {...props} onChange={handleChange} />;
}

FooComponentContainer.propTypes = { /* ... */ };
```

And here’s the reference folder structure:

```
/FooComponent ----------- the whole component for others to import
  -FooComponent.js ------ the "natural" part of the component
  -FooComponent.test.js
  -index.js ------------- the "container" that bridges the gap
  -index.js.test.js         and provides dependencies
  /helpers -------------- isolated helpers that you can test easily
    -getValues.js
    -getValues.test.js
    -transformValues.js
    -transformValues.test.js
```

### Firing events in containers

The last type of scenario where I find myself diverging from a natural component is when I need to fire events related to changing props or mounting components.

For example, let’s say you’re tasked with making a dashboard. The design team hands you a mockup of the dashboard and you transform that into a React component. You’re now at the point where you have to populate this dashboard with data.

You notice that you need to call a function (e.g. `dispatch(fetchAction)`) when your component mount in order for that to happen.

In scenarios like this, I found myself adding `componentDidMount` and `componentDidUpdate` lifecycle methods and adding `onMount` or `onDashboardIdChanged` props because I needed some event to fire in order to link my component to the outside world.

Following the golden rule, these `onMount` and `onDashboardIdChanged` props are unnatural and therefore should live in the container.

The nice thing about hooks is that it makes dispatching events `onMount` or on prop change much simpler!

**Firing events on mount:**

To fire an event on mount, call `useEffect` with an empty array.

```js
import React, { useEffect } from 'react';
import PropTypes from 'prop-types';
import { useRedux } from 'react-redux';

import fetchSomething_reduxAction from 'your-redux-stuff';
import getValues from './helpers/getVaules';
import FooComponent from './FooComponent';

export default function FooComponentContainer(props) {
  // hooks
  // NOTE: `useRedux` does not exist yet and probably won't look like this
  const { state, dispatch } = useRedux();
  
  // dispatch action onMount
  useEffect(() => {
    dispatch(fetchSomething_reduxAction);
  }, []); // the empty array tells react to only fire on mount
  // https://reactjs.org/docs/hooks-effect.html#tip-optimizing-performance-by-skipping-effects

  // mapping
  const props = getValues(state, match);
  
  // natural component
  return <FooComponent {...props} />;
}

FooComponentContainer.propTypes = { /* ... */ };

```

**Firing events on prop changes:**

`useEffect` has the ability to watch your property between re-renders and calls the function you give it when the property changes.

Before `useEffect` I found myself adding unnatural lifecycle methods and `onPropertyChanged` props because I didn’t have a way to do the property diffing outside the component:

```js
import React from 'react';
import PropTypes from 'prop-types';

/**
 * Before `useEffect`, I found myself adding "unnatural" props
 * to my components that only fired events when the props diffed.
 *
 * I'd find that the component's `render` didn't even use `id`
 * most of the time
 */
export default class BeforeUseEffect extends React.Component {
  static propTypes = {
    id: PropTypes.string.isRequired,
    onIdChange: PropTypes.func.isRequired,
  };

  componentDidMount() {
    this.props.onIdChange(this.props.id);
  }

  componentDidUpdate(prevProps) {
    if (prevProps.id !== this.props.id) {
      this.props.onIdChange(this.props.id);
    }
  }

  render() {
    return // ...
  }
}
```

Now with `useEffect` there is a very lightweight way to fire on prop changes and our actual component doesn’t have to add props that are unnecessary to its function.

```js
import React, { useEffect } from 'react';
import PropTypes from 'prop-types';
import { useRedux } from 'react-redux';

import fetchSomething_reduxAction from 'your-redux-stuff';
import getValues from './helpers/getVaules';
import FooComponent from './FooComponent';

export default function FooComponentContainer({ id }) {
  // hooks
  // NOTE: `useRedux` does not exist yet and probably won't look like this
  const { state, dispatch } = useRedux();
  
  // dispatch action onMount
  useEffect(() => {
    dispatch(fetchSomething_reduxAction);
  }, [id]); // `useEffect` will watch this `id` prop and fire the effect when it differs
  // https://reactjs.org/docs/hooks-effect.html#tip-optimizing-performance-by-skipping-effects

  // mapping
  const props = getValues(state, match);
  
  // natural component
  return <FooComponent {...props} />;
}

FooComponentContainer.propTypes = {
  id: PropTypes.string.isRequired,
};

```

> **_Disclaimer:_** _before `useEffect` there were ways of doing prop diffing inside a container using other higher order components (like [recompose’s lifecycle](https://github.com/acdlite/recompose/blob/3db12ce7121a050b533476958ff3d66ded1c4bb8/docs/API.md#lifecycle)) or creating a lifecycle component like [react router does internally](https://github.com/ReactTraining/react-router/blob/89a72d58ac55b2d8640c25e86d1f1496e4ba8d6c/packages/react-router/modules/Lifecycle.js), but these ways were either confusing to the team or were unconventional._

### What are the benefits here?

#### Components stay fun

For me, creating components is the most fun and satisfying part of front-end development. You get to turn your team’s ideas and dreams into real experiences and that’s a good feeling I think we all relate to and share.

There will never be a scenario where your component’s API and experience is ruined by the “outside world”. Your component gets to be what you imagined it without extra props — that’s my favorite benefit of this golden rule.

#### More opportunities to test and reuse

When you adopt an architecture like this, you’re essentially bringing a new data-y layer to the surface. In this “layer” you can switch gears where you’re more concerned about the correctness of data going into your component vs. how your component works.

Whether you’re aware of it or not, this layer already exists in your app but it may be coupled with presentational logic. What I’ve found is that when I surface this layer, I can make a lot of code optimizations and reuse a lot of logic that I would’ve otherwise rewritten without knowing the commonalities.

I think this will become even more obvious with the addition of [custom hooks](https://reactjs.org/docs/hooks-custom.html). Custom hooks gives us a much simpler way to extract logic and subscribe to external changes — something that a helper function could not do.

#### Maximize team throughput

When working on a team, you can separate the development of containers and components. If you agree on APIs beforehand, you can concurrently work on:

1. Web API (i.e. back-end)
2. Fetching data from the web API (or similar) and transforming the data to the component’s APIs
3. The components

### Are there any exceptions?

Much like the real Golden Rule, this golden rule is also a golden rule of thumb. There are some scenarios where it makes sense to write a seemingly unnatural component API to reduce the complexity of some transformations.

A simple example would the names of props. It would make things more complicated if engineers renamed data keys under the argument that it’s more “natural”.

It’s definitely possible to take this idea too far where you end up overgeneralizing too soon, and that can also be a trap.

### The bottom line

More or less, this “golden rule” is simply re-hashing the existing idea of presentational components vs. container components in a new light. If you evaluate what your component needs on a fundamental level then you’ll probably end up with simpler and more readable parts.

Thank you!

