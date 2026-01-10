---
title: Learn React in 1 Hour by Building a Movie Search App
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-06T14:17:15.000Z'
originalURL: https://freecodecamp.org/news/learn-react-in-1-hour-by-building-a-movie-search-app
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/Screenshot-2020-06-01-at-17.18.11.png
tags:
- name: React
  slug: react
seo_title: null
seo_desc: "By Per Harald Borgen\nIf you've been meaning to learn React but are unsure\
  \ of where to start, Scrimba's brand new Build a Movie Search App course is perfect\
  \ for you! \nIn this course, you'll be guided through the app's creation from start\
  \ to finish in ..."
---

By Per Harald Borgen

If you've been meaning to learn React but are unsure of where to start, Scrimba's brand new [Build a Movie Search App](https://scrimba.com/course/greactmovie?utm_source=dev.to&utm_medium=referral&utm_campaign=greactmovie_launch_article) course is perfect for you! 

In this course, you'll be guided through the app's creation from start to finish in just one hour. And you'll work through interactive challenges along the way that help you gain the muscle memory you need to become an effective React developer.

## Why learn React?

React is the world's most popular front-end framework. As [the docs](https://reactjs.org/) state, React makes it painless to create interactive UIs and more predictable code which is easier to debug. With React, you can produce complex UIs through constructing reusable components that manage their own state.

## What does this course do?

[![Styled movie cards](https://dev-to-uploads.s3.amazonaws.com/i/mspewise511f3ub7eyn9.png)](https://scrimba.com/course/greactmovie?utm_source=dev.to&utm_medium=referral&utm_campaign=greactmovie_launch_article)

This learning journey takes you through 11 interactive screencasts, showing you the following core concepts of modern React:

- How to get an API key
- Adding base styles
- Creating and styling components
- Creating functions
- Managing state using hooks
- Displaying information
- Creating and styling cards

## Intro to the teacher

This tutorial is led by James Q. Quick, a full-stack Web Developer who regularly speaks at community events and participates in Hackathons. He also runs a YouTube channel teaching web development. His motto 'Learn. Build. Teach.' makes him the perfect teacher for this practical course.

## Prerequisites

To study this course effectively, you should have basic knowledge of HTML, CSS, and JavaScript. You'll also find it useful to have seen some React code before, but it's not a must-have. 

If you need a bit more background knowledge, take a look at these fantastic free Scrimba courses:

- [HTML and CSS](https://scrimba.com/course/ghtmlcss?utm_source=dev.to&utm_medium=referral&utm_campaign=greactmovie_launch_article)
- [Javascript](https://scrimba.com/course/gintrotojavascript?utm_source=dev.to&utm_medium=referral&utm_campaign=greactmovie_launch_article)

If you're ready to hit the ground running with React, let's get started!

## Course Introduction

[![Build a Movie Search App Course front title slide](https://dev-to-uploads.s3.amazonaws.com/i/n0xmel3r6k0qiazx8v0p.png)](https://scrimba.com/p/pZaznUL/cdVKdrtr?utm_source=dev.to&utm_medium=referral&utm_campaign=greactmovie_launch_article)

In [the first scrim](https://scrimba.com/p/pZaznUL/cdVKdrtr?utm_source=dev.to&utm_medium=referral&utm_campaign=greactmovie_launch_article), James runs us through a few of the key features of the app we'll be building and gives us a quick rundown of how the app works. Lastly, James introduces us to the API we'll use - [themoviedb.org](https://www.themoviedb.org/).

## How to Get Your Movie DB API Key

[![Generating a MovieDB API key](https://dev-to-uploads.s3.amazonaws.com/i/xe8kqht68qhkbpn6bvo5.png)](https://scrimba.com/p/pZaznUL/cdVKdLSk?utm_source=dev.to&utm_medium=referral&utm_campaign=greactmovie_launch_article)

In [this short cast](https://scrimba.com/p/pZaznUL/cdVKdLSk?utm_source=dev.to&utm_medium=referral&utm_campaign=greactmovie_launch_article), James gives us the lowdown on how to get a Movie DB API Key by signing up with a free account. This is super straightforward and takes just a few minutes. Click the image above to access the course.

## Add Base Styles to Your App

[Next up](https://scrimba.com/p/pZaznUL/cNDyQvc2?utm_source=dev.to&utm_medium=referral&utm_campaign=greactmovie_launch_article), James shows us the basic React application he has instantiated for us:

```js
import React from "react";
import ReactDOM from "react-dom";

class Main extends React.Component {
	render() {
		return <h1>Hello world!</h1>;
	}
}

ReactDOM.render(<Main />, document.getElementById("root"));
```

We then add some base styles to our `style.css` file including margins and padding, title styles and, the Holy Grail of CSS - centering the app's contents. [Click here](https://scrimba.com/p/pZaznUL/cNDyQvc2?utm_source=dev.to&utm_medium=referral&utm_campaign=greactmovie_launch_article) to check out the styles for yourself.

## Create Your First Component

[![Our first React app in action](https://dev-to-uploads.s3.amazonaws.com/i/avats2r0wi0mz89mivbr.png)](https://scrimba.com/p/pZaznUL/caZvgqTk?utm_source=dev.to&utm_medium=referral&utm_campaign=greactmovie_launch_article)

[In this scrim](https://scrimba.com/p/pZaznUL/caZvgqTk?utm_source=dev.to&utm_medium=referral&utm_campaign=greactmovie_launch_article), we have our first challenge - to create a React component. James uses a `test.js` file to give us a brief preview of what's needed before breaking down the task into manageable chunks:

```html
//to create the SearchMovies component //form with a class of form //label with
htmlFor="query" and a class of Label //input of type text with a name of "query"
and a placeholder //button class of button and a type of submit
```

Click through to the link or image above to get your hands dirty and give the challenge a try.

## Style the Search Movies Component

[![Our first React app with styles added](https://dev-to-uploads.s3.amazonaws.com/i/752w2eczfd6vo21o1b1j.png)](https://scrimba.com/p/pZaznUL/c6WdV7Ap?utm_source=dev.to&utm_medium=referral&utm_campaign=greactmovie_launch_article)

[Next up](https://scrimba.com/p/pZaznUL/c6WdV7Ap?utm_source=dev.to&utm_medium=referral&utm_campaign=greactmovie_launch_article), it's time to style our new app. James suggests some styles for our `<form>`, `<label>`, `<input>` and `<button>` and adds a media query to adjust the styles on larger screens:

```css
@media (min-width: 786px) {
	.form {
		grid-template-columns: auto 1fr auto;
		grid-gap: 1rem;
		align-items: center;
	}

	.input {
		margin-bottom: 0;
	}
}
```

Don't forget that Scrimba is fully interactive, so you can be as creative as you like with the styles - these ideas are just some possibilities.

## Create the Search Movies Function

```js
export default function SearchMovies(){

    const searchMovies = async (e) => {
        e.preventDefault();

        const query = "Jurassic Park";

        const url = `https://api.themoviedb.org/3/search/movie?api_key=5dcf7f28a88be0edc01bbbde06f024ab&language=en-US&query=${query}&page=1&include_adult=false`;

        try {
            const res = await fetch(url);
            const data  = await res.json();
            console.log(data);
        }catch(err){
            console.error(err);
        }
    }
```

In [this screencast](https://scrimba.com/p/pZaznUL/cdVQEGh9?utm_source=dev.to&utm_medium=referral&utm_campaign=greactmovie_launch_article), we create an async function that will use the Fetch API to retrieve the movie information from the Movie DB API. Hit the link to see how it's done.

## Manage State with React useState Hook

In [this scrim](https://scrimba.com/p/pZaznUL/c73GVeS4?utm_source=dev.to&utm_medium=referral&utm_campaign=greactmovie_launch_article), James shows us how to use state to track the user's query with the `useState` hook:

```js
const [query, setQuery] = useState("");
```

Next, we set the `onChange` on our `<input>` to bind it to that state:

```js
<input
	className="input"
	type="text"
	name="query"
	placeholder="i.e. Jurassic Park"
	value={query}
	onChange={(e) => setQuery(e.target.value)}
/>
```

Then it's time for our second challenge - to create the state for movie information and update that state as appropriate. Hop on over to the tutorial to try it out.

## Display Movie Information

[![App displaying movie info](https://dev-to-uploads.s3.amazonaws.com/i/wv0o08oujgigzbi3h8jz.png)](https://scrimba.com/p/pZaznUL/cgKVEEf4?utm_source=dev.to&utm_medium=referral&utm_campaign=greactmovie_launch_article)

Now that we can search for our movies, it's time to [display the information](https://scrimba.com/p/pZaznUL/cgKVEEf4?utm_source=dev.to&utm_medium=referral&utm_campaign=greactmovie_launch_article) to the user. Click the link or image to see how it's done!

## Style the Movie Cards

[![Styled movie cards](https://dev-to-uploads.s3.amazonaws.com/i/mspewise511f3ub7eyn9.png)](https://scrimba.com/p/pZaznUL/c9qaG6sD?utm_source=dev.to&utm_medium=referral&utm_campaign=greactmovie_launch_article)

[Next up](https://scrimba.com/p/pZaznUL/c9qaG6sD?utm_source=dev.to&utm_medium=referral&utm_campaign=greactmovie_launch_article), James shows us how to style our movie cards to create an attractive, user-friendly app. We start with our card container `<div>` :

```js
.card {
    padding: 2rem 4rem;
    border-radius: 10px;
    box-shadow: 1px 1px 5px rgba(0,0,0,0.25);
    margin-bottom: 2rem;
    background-color: white;
}
```

With that done, we move onto our titles and images. Click the link or image above to get the lowdown.

## Create the Movie Card Component (Challenge)

Our [final task](https://scrimba.com/p/pZaznUL/cE9N3nsw?utm_source=dev.to&utm_medium=referral&utm_campaign=greactmovie_launch_article) is to create a separate component to display the movie card. This ensures maintainability should our project grow, and is a good habit to get into in preparation for bigger projects.

In true Scrimba style, James presents this challenge and then walks us through his solution. Head over to the cast now to try for yourself. **Note:** Props are needed for this, but James gives a quick how-to in the task explanation.

## Wrap up

Congratulations on completing the Movie Search app! You now know how to build a fully functional app using core React concepts including functional components, hooks, fetch requests, styling, and reusable components.

I hope that you gained a lot from this course and feel inspired to continue your learning journey. To find out more about React, head over to Scrimba's free, six-hour [Learn React for Free](https://scrimba.com/course/glearnreact?utm_source=dev.to&utm_medium=referral&utm_campaign=greactmovie_launch_article) course.

After that, why not check out all the other great courses available over on [Scrimba](https://scrimba.com/?utm_source=dev.to&utm_medium=referral&utm_campaign=greactmovie_launch_article) to see where you'll go next?

Wherever your journey takes you, happy coding :)


%[https://www.youtube.com/watch?v=UKmsNUk7RxM]


