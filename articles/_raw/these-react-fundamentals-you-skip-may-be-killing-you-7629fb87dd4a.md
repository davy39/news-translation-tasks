---
title: These React Fundamentals You Skip may be Killing You
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-05T19:03:56.000Z'
originalURL: https://freecodecamp.org/news/these-react-fundamentals-you-skip-may-be-killing-you-7629fb87dd4a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*sVjlf2VlXRhi6zglSUyVoQ.png
tags:
- name: Apps
  slug: apps-tag
- name: development
  slug: development
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Emmanuel Ohans

  Often times, the inability to debug a certain error stems from not understanding
  some foundational concept.

  You can say the same thing if you don’t understand some more advanced concepts because
  you lack the knowledge of certain fun...'
---

By Emmanuel Ohans

Often times, the inability to debug a certain error stems from not understanding some foundational concept.

You can say the same thing if you don’t understand some more advanced concepts because you lack the knowledge of certain fundamentals.

In this article, I hope to explain what I consider some of the most important foundational React concepts you need to understand.

These concepts aren’t particularly technical. There are lots of other articles that cover those — things like `props`, `state`, `context`, `setState` , and so on.

However, in this article I’ll focus on some more conceptual knowledge that forms the basis of most technical things you’ll do in React.

Ready?

### How React works under the hood

One of the first things everyone learns in React is how to build components. I’m pretty sure you learned that too.

For example:

```
// functional component function MyComponent() {  return <div> My Functional Component </div> }// class based component class MyComponent extends React.Component {  render() {     return <div> My Class Component </div>   }}
```

Most components you write will return some elements:

```
function MyComponent() {  return <span> My Functional Component &lt;/span> //span element}class MyComponent extends React.Component {  render() {     return <div> My Class Component &lt;/div> //div element  }}
```

Under the hood, most components return a tree of elements.

![Image](https://cdn-media-1.freecodecamp.org/images/tQn1uuZsujd4JU-cIxVrjn8-3Giy1CRAqjCD)
_Components, when evaluated internally, often times return a tree of elements._

Now, you must also remember that components are like functions that return values based on their `props` and `state` values.

![Image](https://cdn-media-1.freecodecamp.org/images/7NCegDIGXAs8OGYEP733SK7L-uOpMI4vZwSR)
_Components are like functions with “props” and “state” parameters._

Consequently, whenever the `props` or `state` values of a component change, a new tree of elements is rendered.

![Image](https://cdn-media-1.freecodecamp.org/images/jqur2fLzWkWzsXgcm0bDIVRRJWSfnN0v6DSN)
_If the props or state values change, the tree of elements is re-rendered. This results in a new tree._

If the component is a class-based component, the `render` function is invoked to return the tree of elements.

```
class MyComponent extends React.Component {    render() {    //this function is invoked to return the tree of elements  }}
```

If the component is a functional component, its return value yields the tree of elements.

```
function MyComponent() {     // the return value yields the tree of elements   return <div>
```

```
   </div>}
```

Why is this important?

Consider a component, `<MyComponent` /> which takes `in` a prop as shown below:

```
<MyComponent name='Ohans'/>
```

When this component is rendered, a tree of elements is returned.

![Image](https://cdn-media-1.freecodecamp.org/images/3DsSWux3GMF8nLy8KyWXqaciojsvhKaIcts8)
_A tree of elements returned from rendering &lt;MyComponent /&gt;_

What happens when the value of `name` changes?

```
<MyComponent name='Quincy'/>
```

Well, a new tree of elements is returned!

![Image](https://cdn-media-1.freecodecamp.org/images/OQ1FFA7FNaRpmkrMH43CpbHJCV2opTEBNMqe)
_A NEW tree of elements returned from rendering &lt;MyComponent /&gt; with different props_

Okay.

Now, React has in its custody two different trees — the former and the current element tree.

At this point, React then compares both trees to find what exactly has changed.

![Image](https://cdn-media-1.freecodecamp.org/images/cO44K8IzUSeTPwvnGm5nJwYhfn0AvC5lnyGX)
_Two different trees. What’s really changed in both trees?_

Most times the entire tree hasn’t changed. Just some updates here and there.

Upon comparing these two trees of elements, the actual DOM is then updated with the change in the new element tree.

Easy, huh?

This process of comparing two trees for changes is called “reconciliation”. It’s a [technical process](https://reactjs.org/docs/reconciliation.html#motivation), but this conceptual overview is just great for understanding what goes on under the hood.

### React Only Updates What’s Necessary. True?

When you get started with React, everyone’s told how awesome React is — particularly how it just updates the essential part of the DOM being updated.

![Image](https://cdn-media-1.freecodecamp.org/images/o83thhmBUVqoiatZw56dEY6yGNMJn5jxemhw)
_From the [React Docs](https://reactjs.org/docs/rendering-elements.html#react-only-updates-whats-necessary" rel="noopener" target="_blank" title="): DOM inspector showing granular updates._

Is this completely true?

Yes it is.

However, before React gets to updating the DOM, remember that under the hood — it had first constructed the element tree for the various components and did the essential “diffing” before updating the DOM. In other words, it had compared the changes between the previous and current element trees.

The reason I re-iterate this is, if you’re new to React you may be blind to the performance ditches dug in your app because you think React just updates the DOM with what’s necessary.

While that is true, the performance concerns in most React apps begin with the process before the DOM is updated!

### Wasted Renders vs. Visual Updates

No matter how small, rendering a component element tree takes some time (no matter how minute). The time for rendering gets larger as the component element tree increases.

The implication of this is that in your app you do not want React re-rendering your component element tree if it is NOT important.

Let me show you a quick example.

Consider an app with a component structure as shown below:

![Image](https://cdn-media-1.freecodecamp.org/images/sN9IozHOb0YjHvIPzCleBcjPZsTR8nPNZn3y)
_An app with a parent component A and child components B,C and D._

The overall container component, `A` receives a certain prop. However, the sole reason for this is to pass the props down to component `D`.

![Image](https://cdn-media-1.freecodecamp.org/images/5xX0JPX-o-Gej4yKA3iJ8mv4EQpLEaWkvQgH)
_The parent component `A` receives some props and passes them down to the child component D._

Now, whenever the prop value in `A` changes, the entire children elements of `A` are re-rendered to compute a new element tree.

![Image](https://cdn-media-1.freecodecamp.org/images/74D67kRq4cnFHlKfw86OUkdCO1nMYgT9E-rN)

![Image](https://cdn-media-1.freecodecamp.org/images/iAEokbsFD2IW1AOG7DSnhfRFTp0VztjXf5YA)
_When the parent component receives new Props, every child element is re-rendered and a new tree returned._

By implication, the components `B` and `C` are also re-rendered even though they haven’t changed at all! They have not received any new props!

This needless re-rendering is what is termed a “wasted” render.

In this example, `B` and `C` need not re-render, but React doesn’t know this.

There are many ways to deal with such issue, and I cover that in my recent article, [How to Eliminate React Performance Issues](https://medium.com/@ohansemmanuel/how-to-eliminate-react-performance-issues-a16a250c0f27).

Moving forward, consider the application below:

![Image](https://cdn-media-1.freecodecamp.org/images/eSvpbb0SILVtzIf8G7peS9DfJOK2gS1bIc1s)
_Cardey in Action :)_

I call this app [Cardey](http://cardie-performace.surge.sh/).

When I click the button to change the user’s profession, I can choose to highlight updates to the DOM as shown below:

![Image](https://cdn-media-1.freecodecamp.org/images/QnX-5eQrP7GkCVyxl5Xkfu78uhxN-9JhJMMJ)
_Enable the visual updates (Paint Flashing) via Chrome Devtools_

And now I see what’s been updated in the DOM.

This is a representation of the visual updates to the DOM. Note the green flash around the “I am a Librarian” text.

This is great, but I am concerned about React’s initial rendering of the component element tree.

So, I could choose the check that as well.

![Image](https://cdn-media-1.freecodecamp.org/images/xDeyGJE6fL42FrSmU15nm5she0xfO6mtC42G)
_Enable the highlight update toggle in React Devtools_

Upon doing this, I see what components are actually re-rendered when I hit that button.

![Image](https://cdn-media-1.freecodecamp.org/images/zduYcMxUoMrKLzHbLABBf3d2zkVa0gkv9Stc)
_Note the green flash around the user card._

Do you see how the visual updates to the DOM and react’s render updates are different?

The large user card was re-rendered but just the small text region was updated.

This is important.

### Conclusion

I believe you now have a more intuitive understanding how what happens under the hood in your React components.

Actually, a lot more happens than I have discussed here. However, this is a good start.

Go build great apps!

Are you learning React/Redux at the moment? If yes, I have a really great [book series on Redux](https://thereduxjsbooks.com). Some say it’s [one of the best](https://twitter.com/Kaafu4u/status/1041495744803491840) tech books they [ever read](https://twitter.com/LedZeck/status/1044888661664378880)!

