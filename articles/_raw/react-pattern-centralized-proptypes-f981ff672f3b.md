---
title: 'React Pattern: Centralized PropTypes'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-11-14T16:39:43.000Z'
originalURL: https://freecodecamp.org/news/react-pattern-centralized-proptypes-f981ff672f3b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*fjBw8m5BiLqjW9BHfmySfg.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Cory House

  Avoid repeating yourself by centralizing PropTypes

  There are three popular ways to handle types in React: PropTypes, TypeScript and
  Flow. This post is about PropTypes, which are currently the most popular.

  https://twitter.com/housecor/s...'
---

By Cory House

#### Avoid repeating yourself by centralizing PropTypes

There are three popular ways to handle types in React: [PropTypes](https://reactjs.org/docs/typechecking-with-proptypes.html), [TypeScript](http://typescriptlang.org) and [Flow](http://flowtype.org/). This post is about PropTypes, which are currently the most popular.

%[https://twitter.com/housecor/status/911673327240073216?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed&ref_url=https%3A%2F%2Fcdn.embedly.com%2Fwidgets%2Fmedia.html%3Ftype%3Dtext%252Fhtml%26key%3Da19fcc184b9711e1b4764040d3dc5c07%26schema%3Dtwitter%26url%3Dhttps%253A%2F%2Ftwitter.com%2Fhousecor%2Fstatus%2F911673327240073216%26image%3Dhttps%253A%2F%2Fi.embed.ly%2F1%2Fimage%253Furl%253Dhttps%25253A%25252F%25252Fpbs.twimg.com%25252Fprofile_images%25252F650743198348808192%25252FLT6SeOJr_400x400.jpg%2526key%253Da19fcc184b9711e1b4764040d3dc5c07]

Since PropTypes provide type warnings at runtime, it’s helpful to be as specific as possible.

* Component accepts an object? Declare the object’s shape.
* Prop only accepts a specific list of values? Use oneOf.
* Array should contain numbers? Use arrayOf.
* You can even declare your own types. [AirBnB offers many additional PropTypes](https://github.com/airbnb/prop-types).

Here’s a PropType example:

```js
UserDetails.propTypes = {
 user: PropTypes.shape({
   id: PropTypes.number.isRequired,
   firstName: PropTypes.string.isRequired,
   lastName: PropTypes.string.isRequired,
   role: PropTypes.oneOf(['user','admin'])
};
```

In real apps with large objects, this quickly leads to a lot of code. That’s a problem, because **in React, you’ll often pass the same object to multiple components**. Repeating these details in multiple component files breaks the [DRY principle](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) (don’t repeat yourself). Repeating yourself creates a maintenance problem.

The solution? **Centralize your PropTypes**.

#### Here’s How to Centralize PropTypes

I prefer centralizing PropTypes in /types/index.js.

I’m using named imports on line 2 to shorten the declarations. ?

And here’s how I use the PropType I declared above:

```js
// types/index.js
import { shape, number, string, oneOf } from 'prop-types';

export const userType = shape({
  id: number,
  firstName: string.isRequired,
  lastName: string.isRequired,
  company: string,
  role: oneOf(['user', 'author']),
  address: shape({
    id: number.isRequired,
    street: string.isRequired,
    street2: string,
    city: string.isRequired,
    state: string.isRequired,
    postal: number.isRequired
  });
});
```

I use a named import to get a reference to the exported PropType declaration on line 2. And I put it to use on line 13.

**Benefits**:

1. The centralized PropType radically simplifies the component’s PropType declaration. Line 13 just references the centralized PropType, so it’s easy to read.
2. The centralized type only declares the shape, so you can still mark the prop as required as needed.
3. No more copy/paste. If the object shape changes later, you have a single place to update. ?

Here’s a [working example on CodeSandbox](https://codesandbox.io/s/3vw24xnlqm).

%[https://codesandbox.io/s/3vw24xnlqm]

#### Extra Credit: Generate Your PropTypes

Finally, consider writing some custom code to generate your PropType declarations from your server-side code. For example, if your API is written using a strongly typed language like C# or Java, consider generating your PropType declarations as part of your server-side API build process by reading the shape of your server-side classes. This way you don’t have to worry about keeping your client-side PropTypes and your server-side API code in sync. ?

**Side-note**: If you know of a project that does this for any server-side languages, please reply in the comments and I’ll add a link here.

**Edit**: You can convert JSON into PropTypes using [transform.now.sh](https://transform.now.sh/). ?

### Summary

1. Declare your PropTypes as explicitly as possible, so you know when you’ve made a mistake.
2. Centralize your PropTypes to avoid repeating yourself.
3. If you’re working in a strongly typed language on the server, consider generating your PropTypes by reading your server-side code. This assures your PropTypes match your server-side types.

### Looking for More on React? ⚛️

I’ve authored [multiple React and JavaScript courses](http://bit.ly/psauthorpageimmutablepost) on Pluralsight ([free trial](http://bit.ly/pstrialimmutablepost)).

![Image](https://cdn-media-1.freecodecamp.org/images/1*BkPc3o2d2bz0YEO7z5C2JQ.png)

[Cory House](https://twitter.com/housecor) is the author of [multiple courses on JavaScript, React, clean code, .NET, and more on Pluralsight](http://pluralsight.com/author/cory-house). He is principal consultant at [reactjsconsulting.com](http://www.reactjsconsulting.com), a Software Architect at VinSolutions, a Microsoft MVP, and trains software developers internationally on software practices like front-end development and clean coding. Cory tweets about JavaScript and front-end development on Twitter as [@housecor](http://www.twitter.com/housecor).

