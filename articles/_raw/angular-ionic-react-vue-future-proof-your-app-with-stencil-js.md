---
title: Angular/Ionic, React, Vue? Future-proof your app with Stencil.js!
subtitle: ''
author: Lee Nathan
co_authors: []
series: null
date: '2019-05-31T20:51:20.000Z'
originalURL: https://freecodecamp.org/news/angular-ionic-react-vue-future-proof-your-app-with-stencil-js
coverImage: https://www.freecodecamp.org/news/content/images/2019/06/bridge.jpg
tags: []
seo_title: null
seo_desc: 'A Brief Intro:

  In this tutorial, I’m going to build a plain Stencil app with a working analog clock.
  I will throw in a little Ionic for convenience as well, but that’s not the focus
  here. This tutorial will cover some of the more important basics to ...'
---

## A Brief Intro:

In this tutorial, I’m going to build a plain Stencil app with a working analog clock. I will throw in a little Ionic for convenience as well, but that’s not the focus here. This tutorial will cover some of the more important basics to know about Stencil.

While this is a low-level intro to Stencil, I’m going to assume that you’ve at least scanned the Stencil docs and have a basic idea of what JSX and Stencil are all about. You should probably be familiar with Typescript or at least ES6 as well.

## A Longer Intro:

In a previous post, I said I’d be “migrating” toward React because it’s outstripped Ionic. That’s a daunting proposition after 3 years in the Ionic realm. And what if React gets taken over in another year? Fortunately, the folks at Ionic are completely aware of this reality. Which is why they built stencil.js.

Stencil uses Typescript and JSX as a super powerful, lightweight, non-framework. Stencil can be added to any other framework or used on its own to accomplish much of what someone would use Angular or React for.

It’s also quick and easy to learn compared to larger frameworks. So it’s a great way to get used to the JSX/Web Component way of thinking. And if you want to migrate to React from Angular, or vice versa, Stencil can smooth your path.

Going forward I’ll be using Stencil in my personal projects. And Ionic 4 Components are now built on Stencil. So it’s a logical choice to future-proof your apps, whether you stay with Ionic/Angular or move to another framework.

As a side note for the JSX beginners. I find it’s easiest to forget about making everything into perfect Components and just write HTML. Then when I see a bit of HTML I’m going to use more than once or that I want to do something special, I’ll move it into its own Component.

## Getting Started:

First off:

npm init stencil

Select `component` and use `analog-clock-components` as your project name, then:

cd analog-clock-components npm install --save @ionic/core npm start

If it all went to plan, you should see the default “Home” page pop up.

## Making the Clock:

I hate it when tutorials weigh you down with a bunch of information that isn’t critical to the core concepts. So that’s exactly what I’m going to do! I’ll be making the clock with SVG. But hey, it beats yet another fucking todo list example. And I promise to keep it simple.

**Watch out!** Your Stencil component tags MUST have 2 or more words or your app will enigmatically fail with something like `“clock” is not a valid custom element name`!

Add a clock-face folder in the `src/components` directory like so:`clock-face/clock-face.tsx` and add the following contents.

import { Component } from '@stencil/core';

@Component({ tag: 'clock-face' }) export class ClockFace {

render() { return ( ); } }

Then add `analog-clock/analog-clock.tsx`.

import { Component } from '@stencil/core';

@Component({ tag: 'analog-clock', }) export class AnalogClock { render() { return \[

\]; } }

And now replace the `my-component` tag in `index.html` with `<analog-clock\>`

You may have to restart the app, but you should now see this as your home page:

![Image](https://www.freecodecamp.org/news/content/images/2019/05/clock-1.png align="left")

*my stunning clock*

That bit of SVG was pretty painless, just a circle and a couple lines with a bit of style for aesthetics. The style can and should be applied with CSS in a non-trivial app.

Notice that I’ve used the `<svg>` tag as the root of this component. Neat! So far this clock is only right twice a day, so let’s add a few props to make it adjustable. I’m also going to add functions to convert time to degrees to rotate the hands. And I’m going to update the SVG to be able to rotate those hands.

import { Component, Prop } from '@stencil/core';

@Component({ tag: 'clock-face' }) export class ClockFace { @Prop() hour: number; @Prop() minute: number; @Prop() second: number;

hourToDegrees(): number { return Math.floor(this.minute / 2) + (this.hour \* 30); }

minuteToDegrees(): number { return Math.floor(this.second / 10) + (this.minute \* 6); }

secondToDegrees(): number { return this.second \* 6; }

render() {

return ( &lt;line id="hour-hand" transform={`rotate(${this.hourToDegrees()}, 100, 100)`} x1="100" y1="100" x2="100" y2="60" stroke="black" stroke-width="10" stroke-linecap="round"/&gt; &lt;line id="minute-hand" transform={`rotate(${this.minuteToDegrees()}, 100, 100)`} x1="100" y1="100" x2="100" y2="30" stroke="black" stroke-width="8" stroke-linecap="round"/&gt; &lt;line id="second-hand" transform={`rotate(${this.secondToDegrees()}, 100, 100)`} x1="100" y1="100" x2="100" y2="30" stroke="black" stroke-width="2" stroke-linecap="round"/&gt; ); } }

And there we go. My component can now accept incoming variables via the @Prop() decorator and change how it’s displayed based on those variables. Let’s see this in action by updating the clock-face tag to `<clock-face hour={12} minute={34} second={56}/>` I’ve wrapped the numbers in curly brackets so they’ll be passed in as numbers instead of strings.

![Image](https://www.freecodecamp.org/news/content/images/2019/05/clock-2.png align="left")

*my updated clock; still only right twice a day*

## Making the Clock Tick:

If you notice, the clock has no internal logic or time management abilities. It’s best to keep your components as simple as possible. Web Components are a bit like functional programming in that they should do just one thing. Stencil builds on the functional paradigm by making props immutable so that the component can’t affect anything outside of itself. They can fire off events, but that’s it.

Now I’m going to add getters to `analog-clock.ts` to get it to start ticking away.

import { Component } from '@stencil/core';

@Component({ tag: 'analog-clock', }) export class AnalogClock { get hour(): number { let h: any = new Date().getHours(); return h; }

get minute(): number { let m: any = new Date().getMinutes(); return m; }

get second(): number { let s: any = new Date().getSeconds(); return s; }

render() { return (

); } }

Wow! Look at that clock go… nowhere. The time is right, but it’s not ticking. If those of you following along at home are familiar with the Angular family, you may be expecting a ticking clock at this point. However, Stencil only re-renders upon certain conditions. This avoids the runaway train effect Angular developers know all too well. If you get a loop in your code or just have a lot of logic in a method that’s being called from HTML or a getter, your app can slow to a dead stop. It’s still possible for that to happen with Stencil, but it would almost have to be deliberate.

In order for Stencil to re-render, you have to use decorators like @Prop() or @State() to tell Stencil what data is important enough to cause the view to re-render. The state decorator is for managing internal variables, so I’m going to use that. I’m also going to tap into the Component lifecycle so that the timer doesn’t start until the component loads and so that it stops when the Component unloads.

import { Component, State } from '@stencil/core';

@Component({ tag: 'analog-clock', }) export class AnalogClock { timer: number;

@State() time: number = Date.now();

componentDidLoad() { this.timer = window.setInterval(() =&gt; { this.time = Date.now(); }, 250); }

componentDidUnload() { clearInterval(this.timer); }

get hour(): number { return new Date(this.time).getHours(); }

get minute(): number { return new Date(this.time).getMinutes(); }

get second(): number { return new Date(this.time).getSeconds(); }

render() { return ( ); } }

![Image](https://www.freecodecamp.org/news/content/images/2019/05/clock-3.gif align="left")

*And now my clock is ticking away merrily.*

## Changing the Timezone (sort of):

Next, I’m going to add a slider to allow me to pick a timezone. I’m not actually going to incorporate timezones though. It’s a complex feature that needs a whole other library ([like moment.js for timezones](https://momentjs.com/timezone/)) to manage properly. I’m just going to offset the hour by give-or-take 12 hours. It’s a kludgey fix, but it will illustrate how to get data back out of a component, which is a critical thing to know.

Now I’m going to add a time-zone-slider component just like I did with the analog clock, like so `time-zone-slider/time-zone-slider.tsx`.

import { Component, Prop, Event, EventEmitter } from '@stencil/core'; import '@ionic/core';

@Component({ tag: 'time-zone-slider' }) export class TimeZoneSlider { @Prop() offset: number; @Event() timeZoneChanged: EventEmitter;

positionChanged(event: CustomEvent) { this.timeZoneChanged.emit(event.detail.value) }

render() { return ( &lt;ion-range debounce={500} max={12} min={-12} pin={true} snaps={true} step={1} value={this.offset} onIonChange={event =&gt; this.positionChanged(event)} &gt; -1212 ); } }

Notice that I imported the `@ionic/core` library here. This may be overkill, especially in an app where you have no intention of using Ionic components. I just found this to be the easiest way to implement a slider so I could finish this tutorial before the end of the year.

This component also has no internal logic. It doesn’t even manage its own state. It receives the offset as a @Prop(). And when the slider moves, it emits an @Event() to the parent, letting it know about the new value. It is then the parent’s responsibility to manage the state and update the child when the offset changes. Or the parent may also be passing in a value managed by the state of one of **its** ancestors.

import { Component, State, Listen } from '@stencil/core';

@Component({ tag: 'analog-clock', }) export class AnalogClock { timer: number;

@State() time: number = Date.now(); @State() timeZone: number = 0; @Listen('timeZoneChanged') timeZoneChangedHandler(event: CustomEvent) { this.timeZone = event.detail; }

componentDidLoad() { this.timer = window.setInterval(() =&gt; { this.time = Date.now(); }, 250); }

componentDidUnload() { clearInterval(this.timer); }

get hour(): number { return new Date(this.time).getHours(); }

get minute(): number { return new Date(this.time).getMinutes(); }

get second(): number { return new Date(this.time).getSeconds(); }

render() { return (

&lt;clock-face hour={this.hour + this.timeZone} minute={this.minute} second={this.second}/&gt;

  
); } }

In analog-clock, I just added a timeZone state manager. I also added the @Listen() decorator to the `timeZoneChangedHandler` function. That function updates the timeZone state. I changed the `clock-face` element to offset the hour based on the timeZone. Finally, I added the slider element and passed in the current timeZone, completing the loop.

#### Summary:

I just touched on about 80% of what you need to know to get started using Stencil. We’ve covered creating and implementing Components and handling their lifecycles. We covered firing and listening for Events. We covered passing data to children Components with Props. And we covered handling internal Component State. That’s actually about half of the features listed in the Components section of the Stencil docs.
