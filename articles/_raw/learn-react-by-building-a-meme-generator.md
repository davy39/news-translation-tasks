---
title: Learn React by Building a Meme Generator
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-10-23T18:29:43.000Z'
originalURL: https://freecodecamp.org/news/learn-react-by-building-a-meme-generator
coverImage: https://www.freecodecamp.org/news/content/images/2019/10/o60oxupyz8cfce0cknvz.png
tags:
- name: projects
  slug: projects
- name: React
  slug: reactjs
- name: Tutorial
  slug: tutorial
seo_title: null
seo_desc: 'By Bob Ziroll

  Memes are great - they''re such a fun way of describing ideas and opinions. So it''s
  no coincidence that I picked a meme generator app as the capstone project in my
  free React course on Scrimba. The app works by pulling a random meme imag...'
---

By Bob Ziroll

Memes are great - they're such a fun way of describing ideas and opinions. So it's no coincidence that I picked a meme generator app as the capstone project in my [free React course](https://scrimba.com/g/glearnreact) on Scrimba. The app works by pulling a random meme image from an API and placing your text over the top of it to create your very own, personalized meme. 

So in this article, I'll give you a step-by-step guide to creating the app. If you ever get confused, you can also follow these steps in the Scrimba course, starting at [this lecture.](https://scrimba.com/p/p7P5Hd/c6K77um) 

And then if you like my teaching style and are in the mood for a tougher challenge after you complete this tutorial, please check out [my upcoming advanced course](https://scrimba.com/g/greact) on Scrimba.

> Note: You should already be fairly familiar with some of the fundamental concepts of React, like components, state, props, and lifecycle methods. Also, this tutorial doesn't use Hooks, but in my upcoming course we'll cover Hooks in depth and get tons of practice using them.

## 1. Creating the boilerplate and rendering an App component

![Creating the boilerplate task](https://miro.medium.com/max/1396/1*Sigh_tXDKPjQpBlWsvj1lQ.png)

The first thing we need to do is to create the boilerplate code for the app. To do this, we import `React` and `ReactDOM` and use `ReactDOM` to render a component called `App`, which we will create later. We then put the `App` component at the 'root'. We also import `App` from its file `"./App"`, which we will create shortly.

```js
// index.js
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';

ReactDOM.render(<App />, document.getElementById('root'));
```

We then create our `App.js` file. In it, we create a functional component called `App` which, for now, returns a simple `<h1>`. We then export it. The `<h1>` allows us to check that the app is displaying correctly to the screen.

```js
import React from 'react';
function App() {
  return <h1>Hello world!</h1>;
}
export default App;
```

The resulting output is this:
![Rendered Hello World](https://miro.medium.com/max/1686/1*nQjf71dDnfwHqoT3Pw4tag.png)

## 2. Creating the Header and MemeGenerator components

![Creating the Header and MemeGenerator task](https://miro.medium.com/max/1196/1*QZ7p26lRlGRepBrT4i8r3Q.png)

Next up, we create the Header and MemeGenerator components. The Header will only display elements, while MemeGenerator will call to the API and retain the data in state.

Let's start by creating the `Header.js` file. Since Header is a component which is only used to display, it should be a functional component. For now, the component should return a simple `<h1>`. After creating it, we then export Header.

```js
import React from 'react';
function Header() {
  return <h1>HEADER</h1>;
}
export default Header;
```

Next, we create the `MemeGenerator.js` file. As the `MemeGenerator` component will be holding data and making calls to an API, it needs to be a class component. We still need to import React, and since it is going to be a class component, we'll import `Component` as well (which is a [named import](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import#Import_a_single_export_from_a_module)).

MemeGenerator needs a `constructor()` which calls `super()` and as it will be holding state, we add some empty state to it now. Like in the Header component, we render a simple `<h1>` to start with. We then export MemeGenerator.

```js
import React, { Component } from 'react';
class MemeGenerator extends Component {
  constructor() {
    super();
    this.state = {}; //empty state
  }
  render() {
    return <h1>MEME GENERATOR SECTION</h1>;
  }
}
export default MemeGenerator;
```

Now, we import both Header and MemeGenerator into `App.js` and create an instance of each one in our App component. In order to display the components correctly, we wrap them in a `<div>`.

```js
import React from 'react';
import Header from './Header';
import MemeGenerator from './MemeGenerator';
function App() {
  return (
    <div>
      <Header />
      <MemeGenerator />
    </div>
  );
}
export default App;
```

## 3. Completing the Header component.

To complete the `<Header>` component, we add a trollface image by inserting an `<img>` tag and setting the src to the image's URL. We then add a `<p>` tag with the name of our app and wrap them both in the semantic HTML5 `<header>` tag.

```js
function Header() {
  return (
    <header>
      <img
        src='http://www.pngall.com/wp-content/uploads/2016/05/Trollface.png'
        alt='Problem?'
      />
      <p>Meme Generator</p>
    </header>
  );
}
```

As styling is outside the scope of this course, the CSS styles have already been created and applied to the `<header>` tag. The result is this:

![Rendered Header](https://miro.medium.com/max/1142/1*tQ0B2usG9sXABiSHaSeXOQ.png)

That said, learners can always play around with the styling and hone their CSS skills by themselves. With the `<Header/>` now complete, the rest of the challenge will take place in `<MemeGenerator/>`

## 4. Initializing state

![Initializing state task](https://miro.medium.com/max/1394/1*-rcc61OqQ7n3qtCS8gcjLg.png)

We now have to initialize state so that it saves a top text, a bottom text and a random image, which is already supplied.

To do this, we build up the empty object we placed in the `<MemeGenerator/>` when we originally built it. We initialize `topText` and `bottomText` as empty strings and `randomImg` as the provided URL.

```js
class MemeGenerator extends Component {
  constructor() {
    super();
    this.state = {
      topText: '',
      bottomText: '',
      randomImg: 'http://i.imgflip.com/1bij.jpg'
    };
  }
}
```

## 5. Making the API call

![Making the API call task](https://miro.medium.com/max/1448/1*1fSA7JfSJxQ0RnnreAH1ww.png)

Next, we make an API call to the provided URL and save the data returned (which is an array found in `response.data.memes`) to a new state property called `allMemeImgs`.
When we need to load data from an endpoint to use in our component, a good place to make the request is the `componentDidMount()` lifecycle method. As soon as the component mounts, we use the native `fetch()` function to call to the provided URL.

```js
componentDidMount() {
  fetch("https://api.imgflip.com/get_memes")
}
```

This returns a promise which we turn into a Javascript object with the `.json()` method.

```js
componentDidMount() {
  fetch("https://api.imgflip.com/get_memes")
    .then(response => response.json())
}
```

Then we get the response which is useful to us by pulling the memes array from `response.data`.

```js
componentDidMount() {
fetch("https://api.imgflip.com/get_memes")
  .then(response => response.json())
  .then(response => {
  const { memes } = response.data
  })
}
```

Now, we save the results to a new state property called `allMemeImgs`. To do this, we initialize `allMemeImgs` as an empty array.

```js
this.state = {
  topText: '',
  bottomText: '',
  randomImg: 'http://i.imgflip.com/1bij.jpg',
  allMemeImgs: []
};
```

Now, back in `componentDidMount()`, we set state. As we are not interested in what the previous state was, we set `allMemeImgs` to memes.

```js
componentDidMount() {
  fetch("https://api.imgflip.com/get_memes")
    .then(response => response.json())
    .then(response => {
  const { memes } = response.data
  this.setState({ allMemeImgs: memes })
  })
}
```

To ensure that it works, we `console.log` the first item, which looks something like this:

![console.log output](https://miro.medium.com/max/1844/1*_Pn6VWqZsUFKMhbjVsAx-A.png)

Here's an overview of the entire `componentDidMount()` function.

```js
componentDidMount() { //ensure that data is fetched at the beginning
  fetch("https://api.imgflip.com/get_memes") //call to URL
    .then(response => response.json()) //turn promise into JS object
    .then(response => {
  const { memes } = response.data //pull memes array from response.data
  console.log(memes[0]) // check data is present
  this.setState({ allMemeImgs: memes }) // set allMemeImgs state
})
}
```

## 6. Creating the input form

We now want to create a form which will eventually allow the user to input the top and bottom texts. We do this with an HTML `<form>` tag and a simple `<button>` which says 'Gen'. We style it with the pre-provided CSS.

```js
render() {
  return (
    <div>
      <form className="meme-form">
        <button>Gen</button>
      </form>
    </div>
  )
}
```

![Rendered Gen button](https://miro.medium.com/max/1008/1*ruWrn2bd-PiHLu4T3sYMBg.png)

## 7. Adding input fields to the form

![Adding input fields task](https://miro.medium.com/max/1672/1*hJOUoYcmSIv6bV-eHH5m_w.png)

Next, it is up to us to add the two input fields (one for the top text and one for the bottom text). The form should be a controlled form, so we will need to add all the attributes needed in order for that to work. We will create the `onChange` handler later.

We create two input fields which both have the type `text` and appropriate name attributes (`topText` and `bottomText`). Rather than using labels, we use placeholders: 'Top Text' and 'Bottom Text'.

Lastly, in order to make this a [controlled form](https://reactjs.org/docs/forms.html#controlled-components), we set the value as equal to the current value in `state` with `{this.state.topText}` and `{this.state.bottomText}`.

```js
render() {
  return (
    <div>
      <form className="meme-form">
        <input
          type="text"
          name="topText"
          placeholder="Top Text"
          value={this.state.topText}
        />
        <input
          type="text"
          name="bottomText"
          placeholder="Bottom Text"
          value={this.state.bottomText}
        />
        <button>Gen</button>
      </form>
    </div>
  )
}
```

## 8. Creating the onChange handler.

![Creating the onChange handler task](https://miro.medium.com/max/1430/1*AO9cOxV8fnVCXxTyjQCPvw.png)

Now, we create the onChange handler, which will update the corresponding state on every change of the input field.

First, we create a `handleChange()` function which receives an event.

```js
handleChange(event) {

}
```

Now, we set the `onChange` of both input fields to equal `handleChange`.

```js
<form className='meme-form'>
  <input
    type='text'
    name='topText'
    placeholder='Top Text'
    value={this.state.topText}
    onChange={this.handleChange}
  />
  <input
    type='text'
    name='bottomText'
    placeholder='Bottom Text'
    value={this.state.bottomText}
    onChange={this.handleChange}
  />
  <button>Gen</button>
</form>
```

We need to remember to bind the method in the constructor — a common gotcha for React developers.

```js
constructor() {
  super()
  this.state = {
    topText: "",
    bottomText: "",
    randomImg: "http://i.imgflip.com/1bij.jpg",
    allMemeImgs: []
  }
  this.handleChange = this.handleChange.bind(this)
}
```

To test the new `handleChange()` function, we add a simple `console.log`:

```js
handleChange(event) {
  console.log("Working!")
}
```

If it is correctly firing, you'll see something like this:
![Rendered console.log("Working!")](https://miro.medium.com/max/308/1*wGS5bSipqBwpoqKqeC6dVg.png)

Now to fill in the `handleChange()` function. To do this, we want to pull the name and value properties from event.target so that we can get the name of the state we are supposed to update (`topText` or `bottomText`) and the value which is typed into the box.

```js
handleChange(event) {
  const { name, value } = event.target
}
```

We will now use these to update state. As we are not interested in what the previous state was, we can just provide an object in which we set the `[name]` to the value typed into the input field.

```js
handleChange(event) {
const {name, value} = event.target
this.setState({ [name]: value })
}
```

## 9. Displaying a meme image alongside the top and bottom text

We now want the app to display a meme image alongside the top and bottom text. We insert an `<img>` tag underneath the `<form>` and set the `randomImg` which we initialized as its source by using `src={this.state.randomImg}`. We then add two `<h2>` tags which display the corresponding text which is also saved in state. All of this is wrapped in a `div` and styled with the pre-provided `meme` class.

```js
<div className='meme'>
  <img src={this.state.randomImg} alt='' />
  <h2 className='top'>{this.state.topText}</h2>
  <h2 className='bottom'>{this.state.bottomText}</h2>
</div>
```

We can now test the app by typing into the text boxes. As state is being correctly set on every keystroke, the text displayed on the image changes each time we type.

![Rendered example of progress so far](https://miro.medium.com/max/1014/1*avFJ4IjRQZhrN4gdrZHa8g.png)

## 10. Displaying a random meme image alongside the Top and Bottom text

![Displaying a random meme image task](https://miro.medium.com/max/1570/1*xTuNOCWGvQV1sVuw0tgpzQ.png)

Now, we need to create a method which displays a meme image which it randomly chooses from our `allMemeImgs` array when the `Gen` button is clicked. The property on the chosen image in the array is `.url`.
We can break this task down into smaller parts.

Firstly, we set the form's `onSubmit` to equal the name of our new method, which we will call `handleSubmit()`.

`<form className="meme-form" onSubmit={this.handleSubmit}>`

We now create the `handleSubmit()` function above the `render()` function. We need to preventDefault on the event, otherwise, the method will try to refresh the page.

```js
handleSubmit(event) {
  event.preventDefault()
}
```

We also need to bind `handleSubmit()` in our `constructor()`.

```js
constructor() {
  super()
  this.state = {
    topText: "",
    bottomText: "",
    randomImg: "http://i.imgflip.com/1bij.jpg",
    allMemeImgs: []
  }
  this.handleChange = this.handleChange.bind(this)
  this.handleSubmit = this.handleSubmit.bind(this)
}
```

Now, we need to get a random number, get the meme from that index and set `randomImg` to the `.url` of the random item.

```js
handleSubmit(event) {
  event.preventDefault()
  // get a random int (index in the array)
  // get the meme from that index
  // set `randomImg` to the `.url` of the random item I grabbed
}
```

To get a random number, we use `Math.floor(Math.random)`. To make sure that it is one of the indices in our `allMemeImgs` array, we multiply by the length of the array.

```js
const randNum = Math.floor(Math.random() * this.state.allMemeImgs.length);
```

We now set `randMemeImg` to equal `allMemeImgs`, with the index of `allMemeImgs` as the `randNum` we just got. We then add `.url` to the end of it.

```js
const randMemeImg = this.state.allMemeImgs[randNum].url;
```

Now, all we need to do is update the state by updating the randomImg property with `randMemeImg`.

```js
this.setState({ randomImg: randMemeImg });
```

Our completed `handleSubmit()` function looks like this:

```js
handleSubmit(event) {
  event.preventDefault()
  const randNum = Math.floor(Math.random() * this.state.allMemeImgs.length)
  const randMemeImg = this.state.allMemeImgs[randNum].url
  this.setState({ randomImg: randMemeImg })
}
```

## Completed Meme Generator

![Working App](https://miro.medium.com/max/1008/1*ysbU1jxRIcNYCeZmhBdN6g.png)

We now have completed the meme generator app, and get a different image every time we hit the `Gen` button, which is then overlaid with the text we input.

To further our learning, we could play with code and see whether we can improve it, or try to get images from a different API. For some really heavy-duty practice, we could even delete all the code and try building it again from scratch.

Congratulations on following through the tutorial and learning all the skills used in this project.

And if you're ready for it, do check out my upcoming [advanced course](https://scrimba.com/g/greact), as it'll take you to a professional level in React!


