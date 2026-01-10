---
title: A quick intro to setState in React.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-18T04:04:07.000Z'
originalURL: https://freecodecamp.org/news/understanding-setstate-in-react-ea8982168b49
coverImage: https://cdn-media-1.freecodecamp.org/images/0*OhUk2Ct_kQ78DO1M.
tags:
- name: education
  slug: education
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Rajesh Pillai

  How to use setState effectively and what pitfalls to avoid


  State management shouldn’t be like solving Rubik Cube :)

  TL;DR — In case you are a visual learner, head over to the video I made: ReactJS
  — How setState works

  Or watch it he...'
---

By Rajesh Pillai

#### How to use setState effectively and what pitfalls to avoid

![Image](https://cdn-media-1.freecodecamp.org/images/0*OhUk2Ct_kQ78DO1M.)
_State management shouldn’t be like solving Rubik Cube :)_

**TL;DR** — In case you are a visual learner, head over to the video I made: [ReactJS — How setState works](https://www.youtube.com/watch?v=hwvnCnQ1mRg)

Or watch it here:

### An introduction to setState

The first thing to be aware of is the fact that the setState function in React works in an asynchronous fashion. That might trip some developers up, as the state values are not immediately available after the update.

There are two variations of using setState: the object-based approach and the functional approach.

Let’s see both in action. We’ll get to understand the issue with object based setState in the process.

Let’s create a simple application.

```
class App extends React.Component {   constructor() {     super();     this.state = {       value: 0,       message: 'default click state'     }   }     onClick = () => {     this.setState({       value: this.state.value + 1     });          this.setState({       message: `click-state ${this.state.value}`     });   }         render(){     return(        <div>         <div>render->state={this.state.value} -              {this.state.message}         </div>         <button onClick={this.onClick}>Click-setState</button>               </div>     );   }}
```

Now we’ll mount this application to our root DOM node.

```
ReactDOM.render(  <App />,   document.getElementById("root"));
```

The above code, when executed, renders the value and message from the state object and also renders a button.

If you take a look at the click handler, we have two consecutive setState functions that access the this.state value.

The behavior we are expecting is that when the button is clicked, the correct state value should be rendered in the below div (extracted for reference):

```
<div>render->state={this.state.value} -      {this.state.message}</div>
```

The `this.state.message` contains values from `this.state.value`

We are expecting that both state values should be the same when the button is clicked.

Let’s see the output of this.

The initial output is shown below, as the value is 0 to start with.

![Image](https://cdn-media-1.freecodecamp.org/images/1*XJSgTpbY1uJmdKJDWYxHKQ.png)

After the first click, we expect the below output:

```
render->state=1 -click-state 1
```

but we are getting this instead:

![Image](https://cdn-media-1.freecodecamp.org/images/1*gwTie8l4onwKgloeOCXItA.png)
_mismatch in state value_

On the second click, the output still mismatches as shown below.

![Image](https://cdn-media-1.freecodecamp.org/images/1*WPzoGxDaOgd91EEnNwPH-Q.png)

By now you might be snoozing or scratching your head :)

![Image](https://cdn-media-1.freecodecamp.org/images/0*finEoFAqAty_kvoo.)
_Photo by [Unsplash](https://unsplash.com/@jackmanchiu?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Jackman Chiu</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

### The onClick() function

So let’s take a look at the onClick() function to understand the issue.

![Image](https://cdn-media-1.freecodecamp.org/images/1*GHPR2qbIGr-EoWoxg5Jo4w.png)

Since the setState call is asynchronous before the first setState execution may be completed, the reference to the second setState may point to the previous value and not the first current updated one.

We’ll fix this by using the functional aspect of setState.

To demonstrate the fix, let’s create one more button:

```
<button onClick={this.onClickfn}>Click-setState fn</button>
```

And add a new click handler onClickfn() as shown below

![Image](https://cdn-media-1.freecodecamp.org/images/1*crfPkk3iZn0LWjQ48cyaMA.png)
_setState(fn)_

The above method uses the functional parameter in setState.

This can be an arrow function as shown above or the normal ES5 function.

This function takes two parameters as arguments: the first is the prevState, and the second is the props (in case you need props as well, which is passed from the parent component). Here we are only looking into the prevState.

The prevState above relates to the setState function as it is the last updated state. This will always point to the correct value.

Let’s see the output after couple of clicks. You will find that the values are always in sync when you click the second button.

![Image](https://cdn-media-1.freecodecamp.org/images/1*JJxtwtGrlULXMplQVL643A.png)

In the above example, you can see that using the functional setState parameter correctly batches the previous state, and you get predictable state values.

One more caveat we need to be aware of: setState() takes one more callback function, which is executed once the state values are successfully updated.

This is very handy in a situation where you have to do some operation once setState successfully updates.

Let’s see a final example.

Assume we want to log the state value after the update, and we write the code as below. I will use the onClickfn() handler for this.

![Image](https://cdn-media-1.freecodecamp.org/images/1*UyMTLi70kI2pMzpQKq8qAQ.png)

But lets see the `console.log` and verify whether the value is correct or not. After three clicks, you get this status:

![Image](https://cdn-media-1.freecodecamp.org/images/1*91u86QfsxY6Kx5HmNWbf2A.png)

You will observe that the logged value is not the last updated value. Let’s fix this and see the output.

![Image](https://cdn-media-1.freecodecamp.org/images/1*-RUif3etCRJuK6oeoCj3JA.png)

In the above example, we are using the setState() second callback parameter. This callback will be executed once the setState() has completed its operation.

Let’s see the final output with the above modified code.

![Image](https://cdn-media-1.freecodecamp.org/images/1*P48JwStPYtR_fZiOxSF0Dg.png)

### Wrapping up

I hope this small article clears up some misconceptions about setState.

The complete source code is available at [jsbin](http://jsbin.com/mekiwog/1/edit).

Happy coding!

Learn with me @Learner + Fullstack Coach (@rajeshpillai): [https://twitter.com/rajeshpillai](https://twitter.com/rajeshpillai)

Promotion: Special $10 coupon for medium readers for my upcoming live [ReactJS-Beyond the basics](https://www.udemy.com/reactjs-beyond-the-basics/?couponCode=MEDIUM_500) course on udemy in case you wish to support our open source curriculum [Mastering frontend engineering in 12 to 20 weeks](https://codeburst.io/mastering-front-end-engineering-in-12-to-20-weeks-for-beginners-and-experienced-alike-6dc5172e3295)

