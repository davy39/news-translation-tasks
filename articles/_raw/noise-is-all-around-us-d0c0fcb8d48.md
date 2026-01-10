---
title: Noise is all around us.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-17T17:07:03.000Z'
originalURL: https://freecodecamp.org/news/noise-is-all-around-us-d0c0fcb8d48
coverImage: https://cdn-media-1.freecodecamp.org/images/1*K8x5vECRP6b6_Dc1y8PiqA.jpeg
tags:
- name: Design
  slug: design
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Donavon West

  Noise! Noise! Noise! It’s all around us. That person on the train playing a video
  game on their phone with the sound on with no headphones. The guy who think’s it’s
  perfectly within their right to hold a speakerphone call while in lin...'
---

By Donavon West

Noise! Noise! Noise! It’s all around us. That person on the train playing a video game on their phone with the sound on with no headphones. The guy who think’s it’s perfectly within their right to hold a speakerphone call while in line at Starbucks. Emergency vehicle sirens, and cars honking at a traffic jam (as if that will solve anything).

Noise can be seemingly as innocuous as someone not muting their laptop during a meeting — until, that is, everyone is forced to hear the Slack notifications that arrive every 3–4 minutes. Do you want to be that person who asks them to place their computer on mute? Or do you bite your tongue and try to ignore the “cla-clunks” as you try and concentrate to the presentation?

> noise /noiz/  
> a sound, especially one that is loud or unpleasant, or that causes disturbance

Noise is such a problem that it even has its own day — [International Noise Awareness Day](https://euracoustics.org/INAD2017/AboutNoise.html).

### Visual Noise

But noise isn’t just limited to sound. Our eyes can also be inundated with noise. Billboards, advertising on park benches, and flashing neon store signs all contribute to visual noise.

Many cities have ordinances limiting outdoor advertising and distracting architectural design. In Scottsdale, AZ for example, many buildings are a light tan color that blend into the natural surroundings. Contrast this with Time Square in New York City. Pass the aspirin please!

![Image](https://cdn-media-1.freecodecamp.org/images/nSZrzE16aOvUs0gapJBHWGJRiqgTHUgEEmAo)
_Image: [Wikipedia](https://creativecommons.org/licenses/by-sa/3.0" rel="noopener" target="_blank" title="">CC BY-SA 3.0</a> from <a href="https://en.wikipedia.org/wiki/Times_Square#/media/File:New_york_times_square-terabass.jpg" rel="noopener" target="_blank" title=")_

### Code Noise

I know what you’re thinking, “Donavon. I started following you because of your keen insight on technical issues. Is there a point to all this?” First of all, “Thank you.” And yes, I’m glad you asked!

The point is… Coding can be complex enough without adding extraneous noise, or what I like to call “visual clutter”.

Let’s look at a few examples.

#### Repeated Sections of Code

Code that’s unnecessarily repeated can be considered visual clutter. [Don’t repeat yourself](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself). Not only does writing DRY code reduce the chance for errors, but it is easier on the eye.

Take the following example. Look at all of the repeated code.

```
const Foo = () => (  <div>    <Bar className="fruit medium">      <span>Apple</span>    </Bar>    <Bar className="fruit medium">      <span>Orange</span>    </Bar>    <Bar className="fruit large">      <span>Watermelon</span>    </Bar>    <Bar className="fruit large">      <span>Jack Fruit</span>    </Bar>    </div>);
```

But we can DRY this up nicely by putting the repeated code into its own component and get it out of sight by placing it in its own file.

```
const Fruit = ({ size, type }) => (  <Bar className={`fruit ${size}`}>    <span>{type}</span>  </Bar>);Fruit.defaultProps = {  size: 'medium',};
```

Now `Foo` is as DRY as bone.

```
const Foo = () => (  <div>    <Fruit type="Apple" />    <Fruit type="Orange" />    <Fruit type="Watermelon" size="large" />    <Fruit type="Jack Fruit" size="large" />  </div>);
```

#### React Stateless Functional Components vs ES6 Class Components

Here we have a traditional React component written using an ES6 class.

```
Hello class extends Component {  render() {    return (      <div>Hello {this.name}</div>    );  }}
```

Notice that is doesn’t keep any state, and doesn’t use any lifecycle events. Why then aren’t we using a Stateless Functional Component (SFC)?

Here is the same component written as a SFC.

```
const Hello = ({ name }) => (  <div>Hello {name}</div>);
```

Notice that a SFC is basically just the `render` method of a traditional ES6 class component. Because it’s not an instance of a class, any `props` referenced don’t need to use `this`. And because all we are doing is returning a value, we can use the “single statement” form of the ES6 arrow function, which means we can also eliminate the `return` statement.

Using a SFC allows us to cut nearly half of the code. But please don’t think that this is a contest to write the fewest amount of lines (making your code too terse can also make too hard to understand). It’s about eliminating the unnecessary, the boilerplate, and it allows us to focus simply on the problem at hand.

> SFCs help to reduce the signal to noise ratio.

#### Self Commenting Code

Commenting your code _seems_ like a good idea, right? But many would argue that comments should be added only when you need to explain something that may not be obvious or to explain the problem. The code itself should be written in a matter that make it self-commenting.

> Comments should be used to state the problem. Your code shows the solution.

Take this following example.

```
// display a message if high risk and driver has too many accidentsif (driver.age < 25 || driver.age > 85 && driver.accidents > 2) {  doSomething();}
```

Not bad. We’re all used to reading code that look like this. But it’s complex. Now consider this example.

```
const { age, accidents } = driver;const isHighRiskAge = age < 25 || age > 85;const hasManyAccidents = accidents > 2;
```

```
if (isHighRiskAge && hasManyAccidents) {  doSomething();}
```

Notice that we didn’t eliminate lines of code — in fact the code size **increased** — but logic is spread out into bite-sized pieces which your brain can evaluate and set aside. And by using descriptive variable names (i.e. `isHighRiskAge` and `hasManyAccidents`) , the `if` statement is now self explanatory, eliminating the need for the comment.

Another big plus of eliminating comments is confusion. Today you write and comment your code as follows.

```
if (age > 75) { // do something if over 75
```

Tomorrow you find a bug and change the code.

```
if (age > 85) { // do something if over 75
```

But did you remember to update the comment to match? Maybe? Maybe not? Another programmer reading this code months from now might read the comments and be thrown off. Computer’s don’t execute comments.

> Don’t comment the obvious.

#### Small Reusable Components

Creating smaller, reusable components can also reduce visual clutter. Take the following example.

```
const Foo = () => (  <div>    <div      style={{        color: 'red',        width: '200px',        height: '200px'      }}    >Hello World</div>  </div>);
```

Not bad, but we can do better. What if we created a `RedBox` component that encapsulates the styling?

```
const Foo = () => (  <div>    <RedBox>Hello World</RedBox>  </div>);
```

The details are now hidden away out of sight. You only need to look at it’s implementation if there is a problem. Otherwise you should assume that `RedBox` is doing it’s job correctly.

Below is an implementation of `RedBox` that uses using [Styled Components](https://www.styled-components.com/) which allows to to reduce visual clutter even further. If you haven’t used it before, check it out!

```
const RedBox = styled.div`  color: red;  width: 200px;  height: 200px;`;
```

### Conclusion

Eliminating all forms of noise from your life can do wonders for you mental health. Take a walk in a quiet park, free from the chaos of the city streets. Enjoy the pleasant sounds of birds chirping and the natural beauty of the trees. Just stay clear of the playground! ?

![Image](https://cdn-media-1.freecodecamp.org/images/kvcMTFHg-XZALxBYFPznzJzu2FlHvuNiHrwy)
_Image: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:%C3%87ocuk_park%C4%B1.JPG" rel="noopener" target="_blank" title=")_

_I also write for the American Express Engineering Blog. Check out my other works and the works of my talented co-workers at [AmericanExpress.io](http://americanexpress.io/). You can also [follow me on Twitter](https://twitter.com/donavon)._

