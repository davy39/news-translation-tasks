---
title: Want to Learn Svelte? Here's a Free 16-Part Course by Noah Kaufman
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-14T22:09:51.000Z'
originalURL: https://freecodecamp.org/news/want-to-learn-svelte-heres-our-free-15-part-course-by-noah-kaufman
coverImage: https://www.freecodecamp.org/news/content/images/2020/04/jm6s35gtdtf5rijq0uqm.png
tags:
- name: Scrimba
  slug: scrimba
- name: Svelte
  slug: svelte
seo_title: null
seo_desc: 'By Per Harald Borgen

  If you''re looking to learn a new Javascript framework which allows you to write
  less code, use no virtual DOM, and create truly reactive apps, then Svelte is for
  you.

  What is Svelte?

  Svelte is a Javascript framework, a compiler, ...'
---

By Per Harald Borgen

If you're looking to learn a new Javascript framework which allows you to write less code, use no virtual DOM, and create truly reactive apps, then Svelte is for you.

## What is Svelte?

Svelte is a Javascript framework, a compiler, and a language. Unlike other Frameworks such as React and Vue which do much of their work in the browser, Svelte does its work in the compile step. This results in highly efficient code and a potentially faster run-time on the client-side.

Svelte offers faster development, faster web pages, and a better developer experience - the creators of Svelte created it with other developers in mind). 

On top of this, knowing Svelte will help you stand out to potential employers and shows that you're interested in newer technologies.

## Great! Tell me about Svelte.

This article takes you through Scrimba's brand-new [16-part Svelte course](https://scrimba.com/playlist/pG6X6UG?utm_source=fcc&utm_medium=referral&utm_campaign=glearnsvelte_launch_article) which covers the following essential topics to put you well on your way to becoming a Svelte master:

- Components
- Importing/exporting
- Slots
- Template
- Event Handling
- Event Dispatching
- Buttons
- Reactivity
- Binding

The course is delivered through a series of interactive screencasts, allowing you to practice your new skills and truly embed your learning.

Finishing up with an in-depth Final Project which consolidates all the skills learned along the way, the course helps you build the muscle memory needed to become an effective Svelte developer. 

It is led by is Noah Kaufman, a Senior Frontend Developer from San Francisco, California with an M.S in Computational Linguistics.

If this sounds right up your street, [head on over to the course](https://scrimba.com/g/glearnsvelte?utm_source=fcc&utm_medium=referral&utm_campaign=glearnsvelte_launch_article) on Scrimba and read on to find out more.

## Components

In Svelte, everything exists inside a component, and the first cast shows what the anatomy of these components looks like. 

The component has three optional parts; `<script>`, which contains Javascript, `<style>` which contains CSS, and finally some HTML, which is able to use the JS from the `<script>` tag.

```js
<script>
    let say = 'hi';
</script>

<style>
    div {
        color: red;
    }
</style>

<div>
    Say: {say}
</div>
```

## Importing and Exporting

Here, we take a quick look at how to import and export components so they can be used elsewhere in our app.

Components are imported with the `import` keyword:

```js
import Face from "./Face.svelte";
```

While the `export` keyword allows other components to change components on import:

```js
<script>
    export let size;
</script>

<div style="font-size: {size}em">=)</div>
```

## Challenge 1

In this cast, Noah challenges us to put our new Svelte skills to the test. No spoilers here, so [click through to the course](https://scrimba.com/p/pG6X6UG/cvdpNRU8?utm_source=fcc&utm_medium=referral&utm_campaign=glearnsvelte_launch_article) to give the challenge a try and check the solution.

## Slots

Slots allow us to place elements inside components. For example, inserting a `<slot>` into a `<div>` with the class `Container` allows us to place as many elements as we want into the `<Container>` component:

```js
<div class="Container">
  <slot></slot>
</div>
```

The newly-placed elements are children of the component:

```js
<Container>
  <div>Say: {say}</div>

  <Face index={0} />
  <Face />
  <Face index={2} />
</Container>
```

## Templating

The Svelte templating syntax allows us to add if statements and for loops to our HTML. That's right, to our HTML!

An if statement looks like this:

```js
<Container>
    {#if say}
        <div>
            Hi!
        </div>

    {/if}
</Container>
```

While a for loop looks like this:

```js
{#each [2,1,0] as faceIndex}
        <Face index={faceIndex} />
    {/each}
```

## Making Header - Challenge 2

In this challenge, we use what we've just learned about Svelte templating to add a Header to our app. [Check out the course](https://scrimba.com/p/pG6X6UG/cGmeLzsR?utm_source=fcc&utm_medium=referral&utm_campaign=glearnsvelte_launch_article) to try it out for yourself and check your answer.

## Event Handling

Next up, Noah shows us a simple inline event handler, which allows the user to show the app's header at the click of a button.

```js
<button
  on:click={() => {
    showHeader = true;
  }}
>
  show
</button>
```

However, if we use a `<Button>` component rather than a native HTML button, this kind of `on:click` handler won't work. We can fix this with **event forwarding**, i.e. adding a plain `on:click` to the native `<button>` in the component file:

```js
<button on:click>
  <slot></slot>
</button>
```

## Event Dispatching

Event dispatching allows a component to emit more than one type of event, for example, the same `<Button>` component can be used both to show an element and to hide it.

We create an event dispatcher like this:

```js
<script>
  import {createEventDispatcher} from 'svelte'; const dispatch =
  createEventDispatcher();
</script>
```

We then add it to native HTML `<button>` like this:

```js
<button on:click={() => dispatch('show')}>
    Show
</button>
<button on:click={() => dispatch('hide')}>
    Hide
</button>
```

Finally we define the `<Button>`'s functionality options in the `App.svelte` file like this:

```js
<Buttons
  on:show={() => {
    showHeader = true;
  }}
  on:hide={() => {
    showHeader = false;
  }}
/>
```

The same outcome can also be achieved by passing values (in this case `true` and `false`) up through the dispatch. The values can then be accessed through the event variable `e`.

```
<button on:click={() => dispatch('click', true)}>
    Show
</button>
<button on:click={() => dispatch('click', false)}>
    Hide
</button>
```

```js
<Container>
  <Buttons
    on:click={(e) => {
      showHeader = e.detail;
    }}
  />
</Container>
```

## Buttons - Challenge 3

Our third challenge is more involved than the previous two and puts our new knowledge of event dispatchers to the test. To help us along, Noah breaks the challenge down into bitesize chunks:

```js
<!-- Challenge 3 -
1. add a prop in Buttons.svelte called buttons which is a list of objects like:
[{value: '', text: ''}, ...etc]
2. use #each to turn all the objects into buttons that:
    a. have innerHTML equal to the .text of the object.
    b. dispatch a click event that passes the .value of the object.
3. Handle the event in App.svelte to update the score.
-->
```

[Head over to the course](https://scrimba.com/p/pG6X6UG/cp342mTV?utm_source=fcc&utm_medium=referral&utm_campaign=glearnsvelte_launch_article) now to give it a try and see the solution.

## Reactivity

Reactive statements are a unique feature of Svelte which tell a piece of code to re-run each time a variable within that code is updated. 

For example, the code below will run each time the score variable is changed (note that we declare a reactive statement with `$:`).

```js
let score = 0;
$: smileySays = "Hi there, your score is: " + score;
```

We can also run if statements inside reactive statements:

```js
let score = 0;
$: smileySays = "Hi there, your score is: " + score;
$: if (score < -4) smileySays = "Wow your score is low!";
```

## Reactive Challenge - Challenge 4

We can now test our new skills by completing the Reactive Challenge, which brings us one step closer to being ready for the final project.

Once again, Noah splits the challenge into smaller parts to help us on our way:

```js
<!-- Challenge 4 -
1. add happyScore and storyIndex (both equal 0)
2. smileySays and buttons get updated whenever storyIndex changes
3. add clickHandler function that increments storyIndex and adds e.detail.value to the happyScore -->
```

[Click through to the course](https://scrimba.com/p/pG6X6UG/cgKqRDt9?utm_source=fcc&utm_medium=referral&utm_campaign=glearnsvelte_launch_article) to try it out and check your answer.

## A Bit More Reactivity

Next up, Noah gives us another example of using Reactive Statements, an emoji face which changes according the current `happyScore` variable:

```js
const faceList = [
  "?",
  "?",
  "?",
  "?",
  "?",
  "?",
  "?",
  "?",
  "?",
  "?",
  "?",
];
$: index = happyScore + 5;
```

Similarly to the previous examples, the code runs each time the 'happyScore' variable changes, so a Reactive Statement is just the right tool for the job.

## Binding

Binding allows a user to update a variable (in this case called `name`) by entering a value into an `<input>` field. As binding is a two-way process, changing the variable also updates the `<input>`'s value:

We bind values like this:

```js
<script>
    import Face from './Face.svelte';
    import Container from './Container.svelte';
    import story from './story';

    let showHeader = false;
    let storyIndex = 0;
    $: smileySays = story[storyIndex].smileySays;
    //variable name below:
    let name = '';
</script>

<Container>
    //binding declared below:
    <input type="text" bind:value={name}>
    <h1>{name}, {smileySays}</h1>
</Container>
```

As well as binding variables, it's also possible to bind values from objects, lists or components.

## Final Project

[![Final Project](https://dev-to-uploads.s3.amazonaws.com/i/mzg89uwkqt4yd0t4ghdz.png)](https://scrimba.com/p/pG6X6UG/cgKK4yhG?utm_source=fcc&utm_medium=referral&utm_campaign=glearnsvelte_launch_article)
_Click the image to access the final project._

Well done for making it through the course! We wrap things up with a final project which ties together all the skills we've learned along the way. 

Once again Noah breaks it down into smaller chunks to help us through:

```js
<!-- Final Challenge
1. The header appears if the user chooses Svelte answer
(HINT: happyScore will be greater than 0 if they answer Svelte)
2. Display final message depending on happyScore
3. Implement the Reset functionality
-->
```

[Check out the cast](https://scrimba.com/p/pG6X6UG/cgKK4yhG?utm_source=fcc&utm_medium=referral&utm_campaign=glearnsvelte_launch_article) to test out your news Svelte skills and see the solution.

## Outro

That brings us to the end of the course. Great job for finishing it! And if you're eager to learn more Svelte, do check out the official docs at [svelte.dev](https://svelte.dev/) for topics like: `Context`, `Stores`, `Lifecycle methods`, `Actions`, `Sapper` and more.

You can also follow my [SvelteMaster Youtube Channel](https://www.youtube.com/channel/UCg6SQd5jnWo5Y70rZD9SQFA) and do sign up for the [Scrimba Svelte Bootcamp](https://rebrand.ly/sveltebootcamp) to be the first to know about the launch and any discounts.

I hope you've found it useful and can put your brand-new knowledge to good use very soon.

In the meantime, why not [head over to Scrimba](https://scrimba.com/?utm_source=fcc&utm_medium=referral&utm_campaign=glearnsvelte_launch_article) to see what other courses are on offer to help you reach your coding goals?

If you also want to hang out with your fellow learners or chat with more experienced folks and the creators of Scrimba courses, do join our [Scrimba Discord server](https://discord.gg/mF6PcNU).

Happy learning :)


%[https://www.youtube.com/watch?v=SU25upz4WCI]


