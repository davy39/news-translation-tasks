---
title: How to use React and React-Sentinel to make responsive, dumb components
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-20T20:34:10.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-react-and-react-sentinel-to-make-responsive-dumb-components-51a04c6279a3
coverImage: https://cdn-media-1.freecodecamp.org/images/0*-M7kIz-f-VmOfAy6.
tags:
- name: animation
  slug: animation
- name: CSS
  slug: css
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Ryan Yurkanin

  tldr; Media Queries aren’t always enough. Element Queries are amazing, and you can
  black box them with a combination of render props, and something observing your
  element!

  Dealing with Media Queries

  If you’ve had to recreate a Respon...'
---

By Ryan Yurkanin

**tldr; Media Queries aren’t always enough. Element Queries are amazing, and you can black box them with a combination of render props, and something observing your element!**

#### Dealing with Media Queries

If you’ve had to recreate a Responsive Design , then you know how awesome — but troublesome — [Media Queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Media_Queries/Using_media_queries) are.

Media Queries allow for CSS that only applies when size changes relative to viewport.

Unfortunately, if you want to make a reusable and responsive card component, Media Queries are less than ideal:

1. You need to figure out the relationship between the height and width of the responsive card and the height and width of the viewport.
2. If your card is in a more complex layout (such as a flex layout), then you need to figure out how the window size will change the flex layout, and then how that will affect the card. ?
3. There could be JavaScript that toggles a condition that programmatically changes the size of the card, so you would also have to factor that in and communicate that to the style sheets.

![Image](https://cdn-media-1.freecodecamp.org/images/1*vIDJ7ghnI_MUu0kfVUD9DA.gif)
_… and now we are in CSS calc() hell. ?_

At this point, I started questioning why I even got into developing in the first place

All I wanted was a way to style the card based on the height and width of that element. [A lot of people want the ability to do that](https://discourse.wicg.io/t/element-queries/26/33). One proposal is Element Queries, and [there are a few ways out there to have them in CSS right now!](https://elementqueries.com/) ?

If you’re like me, though, you want to be able to bring it into not only the JavaScript ecosystem, but the React ecosystem as well. Can we make an intelligent, black-boxed, responsive container, and a dumb visual component?

**Yes** we can.

#### The solution

The beauty of this component is that it doesn’t know why it’s the size that it is. That’s up to whomever is using it to decide, which means this component can be reused in a number of layouts. Our goal is to **keep it this way**, while simultaneously making it awesome.

Let’s see how we can do that by bringing in `react-sentinel`, and creating a smart responsive container with it! ?

So what is **actually** going on here?

`react-sentinel` works by taking a function, the `observe` prop, and calling it repeatedly in a performant `requestAnimationFrame` or `requestIdleCallback` loop.

`requestAnimationFrame` loops at a speed that is determined by the browser. If someone is browsing on an older phone, the loop will happen less often. This gives the browser finer control and leads to a smoother experience!

If you want to learn more about `requestAnimationFrame` , I suggest reading [**Gain Motion Superpowers with requestAnimationFrame**](https://medium.com/@bdc/gain-motion-superpowers-with-requestanimationframe-ecc6d5b0d9a4) by Benjamin De Cock! ?

`Sentinel` takes the return value from those functions, and if it’s different from the previous return value, sets it as the `Sentinel` component’s local state. If it’s not different, then we stop right there and don’t update so we aren’t constantly re-rerendering! ?

#### Using Render Props

Now at this point you may be asking what good is setting `Sentinel` ’s local state? How are we going to get that? ?

My preferred way to do this is using Render Props.

Most know that you can pass in children to a component, and access them using `this.props.children`, but you could also pass in a function!

```
<MightHaveSecrets>  {() => <WantsSecrets />}</MightHaveSecrets>
```

Alright, that’s a thing. Why would anyone want to do that? ?

Because now, **has secrets** can pass it’s internal secrets as an argument to that function! It has no idea how you are actually going to use those secrets, which makes it super encapsulated.

```
<MightHaveSecrets>  {secret => <WantsSecrets emoji={ secret ? ? : ? } />}</MightHaveSecrets>  
```

All the `<Sentinel` /> component cares about is polling infinitely looking to update itself. Render Props allow any chunk of UI to interpret those updates as they see fit. Also it’s a lot more obvious where those values are coming from. ?

If you want to learn more about Render Props, I suggest taking a look at the React Documentation or reading this article by the person [who first turned me onto them!](https://cdb.reacttraining.com/use-a-render-prop-50de598f11ce)

Now we have a smart component that translates the size of the element into simple props that `<DumbCard` />can digest. It’s super easy to refactor and swap values, and you don’t have to worry about what layout it lives in, or what’s going on outside of its scope.

#### Wrapping up

Imagine how difficult it would have been to write CSS for a card the user could resize. Now, we react to anything that changes the elements size.

The cool thing about `react-sentinel` is that it doesn’t just solve the element queries problem. I’ve also used it to create a Smart Animation component, since it uses `requestAnimationframe` under the hood ?

[Here](https://github.com/YurkaninRyan/react-sentinel) is where you can check out the code for `react-sentinel`, as well as some alternative solutions!

If you have any questions, or any topics that you’d like to see covered more in-depth feel free to hit me up! Thanks for reading and happy coding! ?

