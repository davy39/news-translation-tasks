---
title: 'Component crafting: how to create a slider with a linked input'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-11T17:00:35.000Z'
originalURL: https://freecodecamp.org/news/component-crafting-how-to-create-a-slider-with-a-linked-input-600d3438a050
coverImage: https://cdn-media-1.freecodecamp.org/images/1*4xqdv8O0r3mXLL13R0Gk3A.jpeg
tags:
- name: forms
  slug: forms
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: UX
  slug: ux
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Robin Sandborg

  Here at Stacc, we’re huge fans of React and the render-props pattern. When it came
  time to create a slider input, we turned to one of our favorite resources — Jared
  Palmers awesome-react-render-props. Here we found react-compound-sl...'
---

By Robin Sandborg

Here at [Stacc](https://stacc.com/), we’re huge fans of React and the render-props pattern. When it came time to create a slider input, we turned to one of our favorite resources — Jared Palmers [awesome-react-render-props](https://github.com/jaredpalmer/awesome-react-render-props). Here we found [react-compound-slider](https://github.com/sghall/react-compound-slider).

Our challenge was to combine the slider with a linked input. The user could choose whether to input their data through the keyboard input or the slider.

The slider and input were like your typical siblings, constantly bickering. When the input requested a value outside the domain of the slider or one that didn’t fall exactly on one of the sliders steps, the stubborn slider not only refused to listen to the input — it would force the input to change its value. The result was a frustrating user experience.

I’ve searched but didn't find someone who’d solved this for me. So, in the spirit of sharing, here’s my solution. If you have any ideas or suggestions about how it could be even better, please share! I am, after all, more designer than developer.

### The goal

Looks pretty simple, right? So let’s think about what we need to do here.

1. Put the shared value where both the slider and the input have access to it. In this case, we’ll make a component that wraps them both, and put the values there.
2. Manage the values sent to both the input and the slider when something changes in either of them.
3. Avoid the strict rules of the slider’s domain (min and max) and steps from interfering with the users' ability to type a value into the input.

We’ll get back to the wrapping component later. First, let’s get our hands dirty with implementing the slider. Explanation below the example.

Here I’ve implemented _getDerivedStateFromProps._ The slider needs to update its internal state from the values supplied from the slider’s props. I’ve also added some props for onUpdate, onChange and onSlideStart. We can handle these events in our wrapper component. Except for these details, this is pretty close to the code used in the [react-compound-slider documentation](https://sghall.github.io/react-compound-slider/#/slider-demos/horizontal).

The part I struggled with was handling the linking of the input and the slider. When typing, the value often goes outside of the slider’s permitted min and max values. There is no guarantee the user would type in a value that exactly matches any of the allowed steps in the slider.

If we didn’t handle these cases, the user would never be allowed to empty the input. If she typed a value outside any of the steps, it would just set the value to the closest step. Basically, any change in our input would result in the slider moving to where it thinks it should be, and thus updating our state with its value, overriding the value the user just typed.

In order to handle these situations, I needed some logic. The best solution I could come up with was this:

1. When the input has focus, set the step prop for the slider to be 1 so that it can be set to whatever the user types
2. If the input’s value changes AND the new value lies in the allowed range, set the slider’s value. Otherwise, do nothing.
3. When the user starts dragging the slider, set the step prop to what it’s supposed to be again and update the value of the inputs.

You can see the entire implementation with more comments on [CodeSandbox](https://codesandbox.io/s/wj9wv6nyw).

Thank you for reading!

