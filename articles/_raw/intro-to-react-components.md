---
title: Why You Should Use React Components Instead of HTML
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2021-03-17T15:34:07.000Z'
originalURL: https://freecodecamp.org/news/intro-to-react-components
coverImage: https://www.freecodecamp.org/news/content/images/2021/03/still-using-html-start-using-react-components.png
tags:
- name: components
  slug: components
- name: JavaScript
  slug: javascript
- name: JSX
  slug: jsx
- name: React
  slug: react
seo_title: null
seo_desc: 'HTML is the language of the web, but creating entire websites with HTML
  alone can be repetitive and hard to manage.

  In this article, we''re going to see how to use the JavaScript library React as
  a way to add convenience and reusability to our website...'
---

HTML is the language of the web, but creating entire websites with HTML alone can be repetitive and hard to manage.

In this article, we're going to see how to use the JavaScript library React as a way to add convenience and reusability to our websites.

React is a powerful tool for any developer who knows HTML and wants to build more organized and dynamic websites, faster.

Let's get started!

## Why should I use React instead of HTML?

React arrived in 2013 as a better way to build web apps with JavaScript. It's often referred to as a library for building UIs, short for "user interfaces". 

What makes React such a desirable library to learn is that _it doesn't replace HTML._

It takes advantage of HTML's popularity and strength as the most popular programming language, by letting you use a very similar syntax to HTML to build interfaces and add dynamic features to it using JavaScript.

## How to build a user interface with HTML

In light of React's versatility, we can recreate any site or user interface that we see on the web.

For this lesson, let's remake part of an app that you likely use every day—Google Search.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/image-1-1.png)

This may seem ambitious if you are brand new to React, but it requires a knowledge of only two simple concepts: HTML and basic JavaScript functions.

What's the way to build out a user interface without knowing React or even JavaScript?

By using HTML elements as part of a simple HTML document.

Here's how we would show the first three results that come up when you search for "reactjs" in Google.

```html
<!DOCTYPE html>
<html>
  <head>
    <title>reactjs Search Results</title>
  </head>

  <body>
    <section>
      <div>
        <a href="https://reactjs.org"
          >React - A JavaScript Library for Building User Interfaces</a
        >
        <div>
          <h3>reactjs.org</h3>
        </div>
        <div>
          React makes it painless to create interactive UIs.
        </div>
      </div>
      <div>
        <a href="https://en.wikipedia.org/wiki/React_(web_framework)"
          >React (web framework) - Wikipedia</a
        >
        <div>
          <h3>https://en.wikipedia.org › wiki › React_(web_framework)</h3>
        </div>
        <div>
          React is a JavaScript library for building user interfaces.
        </div>
      </div>
      <div>
        <a href="https://twitter.com/reactjs?lang=en"
          >React (@reactjs) | Twitter</a
        >
        <div>
          <h3>https://twitter.com › reactjs</h3>
        </div>
        <div>
          The latest Tweets from React (@reactjs).
        </div>
      </div>
    </section>
  </body>
</html>

```

Using static HTML alone would be fine if we only needed to show a few links.

But how could we display 100s or 1000s of links this way, all with different data, as a search engine might need to do?

What's a better, that is, a simpler and more extensible way of writing this?

HTML alone is not going to be the answer. We'll need a way of making our site more dynamic to display as many links as we need.

When it comes to adding behavior to a site, we need JavaScript. And since our goal is to build great apps with JavaScript, we know to use React.

## How to upgrade any HTML site to a React app

Let's turn our static HTML into a dynamic React app.

Sounds difficult? It's simpler than you think.

We can build a React app out of a single HTML document. All we have to do is bring React in with the following external scripts.*

```html
<script src="https://unpkg.com/react@16/umd/react.development.js"></script>
<script src="https://unpkg.com/react-dom@16/umd/react-dom.development.js"></script>
<script src="https://unpkg.com/babel-standalone@6.26.0/babel.js"></script>

```

The first is for building our React app, and the second is for displaying, or rendering the React app in the browser.

The first is **React**, the second **ReactDOM**.

The third script is to bring in a tool called **Babel**. We'll touch on what that does in a bit.

Here's what our code looks like at this point:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>reactjs Search Results</title>
    <script src="https://unpkg.com/react@16/umd/react.development.js"></script>
    <script src="https://unpkg.com/react-dom@16/umd/react-dom.development.js"></script>
    <script src="https://unpkg.com/babel-standalone@6.26.0/babel.js"></script>
  </head>

  <body>
    <!-- our script must have type="text/babel" for Babel to work -->
    <script type="text/babel">
      // React code will go here
    </script>
  </body>
</html>

```

... and it's almost a React app.

Note that we have a script where we can write our React code, but no HTML.

Let's fix that.

## How to create and render our React app

Every React app must have what's known as an entry point.

The **entry point** is an HTML element where we insert our React application into the page.

The conventional entry point is a div with the id of root (`<div id="root"></div>`).

We'll add that, then use the `render()` function from ReactDOM to do the work of rendering the app.

The first is the app itself, meaning our HTML from before, and the second must reference our entry point. We can create that reference by saying `document.getElementById('root')`.

So now we have everything we need to run our React app:

```html
<!DOCTYPE html>
<html>

  <head>
    <title>reactjs Search Results</title>
    <script src="https://unpkg.com/react@16/umd/react.development.js"></script>
    <script src="https://unpkg.com/react-dom@16/umd/react-dom.development.js"></script>
    <script src="https://unpkg.com/babel-standalone@6.26.0/babel.js"></script>
  </head>

  <body>
    <div id="root">

    </div>
    <!-- our script must have type="text/babel" for Babel to work -->
    <script type="text/babel">
      ReactDOM.render(
      <section>
      <div>
        <a href="https://reactjs.org"
          >React - A JavaScript Library for Building User Interfaces</a
        >
        <div>
          <h3>reactjs.org</h3>
        </div>
        <div>
          React makes it painless to create interactive UIs.
        </div>
      </div>
      <div>
        <a href="https://en.wikipedia.org/wiki/React_(web_framework)">React (web framework) - Wikipedia</a>
        <div>
          <h3>https://en.wikipedia.org › wiki › React_(web_framework)</h3>
        </div>
        <div>
          React is a JavaScript library for building user interfaces.
        </div>
      </div>
      <div>
        <a href="https://twitter.com/reactjs?lang=en">React (@reactjs) | Twitter</a>
        <div>
          <h3>https://twitter.com › reactjs</h3>
        </div>
        <div>
          The latest Tweets from React (@reactjs).
        </div>
      </div>
    </section>, document.getElementById('root'))
    </script>
  </body>

</html>
```

And if we look at our result, it works like before. Perfect!

![Image](https://www.freecodecamp.org/news/content/images/2023/09/image-2-1.png)

Now let's use React to improve our site by dynamically displaying our links.

## How to make HTML reusable with React components

If we examine our HTML structure, each link consists of the same parts. Each has a URL, a title, a shorter URL, and an excerpt. For each link, we have to repeat the same HTML elements again and again.

In programming, if you're having to repeat yourself a great deal, it's likely a sign that your code can be simplified and shortened in some way. As programmers, we always strive to repeat ourselves as little as possible.

We try to write code that is DRY, where you "don't repeat yourself."

React is, at core, JavaScript plus some features to help us build apps.

And since we're working with JavaScript, what is a JavaScript feature that allows us to create or output something as many times as we like?

A function. 

Let's create one here, and we'll call it Link.

```js
function Link() {
  // create link HTML output
}

```

The reason being that we want this function to return or output a link's HTML every time we call it.

To do that, let's return our first link's HTML:

```js
function Link() {
  return (
    <div>
      <a href="https://reactjs.org">
        React - A JavaScript Library for Building User Interfaces
      </a>
      <div>
        <h3>reactjs.org</h3>
      </div>
      <div>React makes it painless to create interactive UIs.</div>
    </div>
  );
}

```

So now let's use it to display each link it returns.

To do so, instead of calling it like `Link()`, in React, we can write it like it was an HTML element `<Link />`.

If you've seen this for the first time it might bend your brain a little bit.

Here we are using HTML syntax, but we are calling a JavaScript function! You'll get comfortable with it as you see this more often.

(Also, did you notice that we didn't have to use an opening and closing tag, like it was a normal HTML element? More about that in a minute.)

**How does React convert HTML-looking syntax into JavaScript?**

It does so with the help of a special tool called Babel, the third script we added. You can see how it works in action here:

![Babel gif](https://dev-to-uploads.s3.amazonaws.com/i/p3550r6dthfd6onee5eg.gif)

What's happening?

Babel, a JavaScript tool called a compiler, converts ("compiles") this code that looks like HTML into valid JavaScript.

## What is this HTML-like syntax? JSX

This HTML, which is in fact JavaScript, is called **JSX**, which stands for "JavaScript XML."

XML, if you're not familiar, is a slightly stricter way of writing HTML.

Stricter means that we need to use a closing forward slash for elements with one tag. For example: `<input>` in HTML as valid JSX is `<input />`.

So to reiterate, JSX is _not_ valid JavaScript code.

Meaning, you couldn't put JSX in a browser and expect it to work. We need both a compiler, like Babel, to convert it into valid JavaScript, and then React to use that created JavaScript.

So now to use our custom Link element, we remove all three of the links' HTML and replace them with three Links, like so:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>reactjs Search Results</title>

    <script src="https://unpkg.com/react@16/umd/react.development.js"></script>
    <script src="https://unpkg.com/react-dom@16/umd/react-dom.development.js"></script>
    <script src="https://unpkg.com/babel-standalone@6.26.0/babel.js"></script>
  </head>

  <body>
    <div id="root"></div>

    <script type="text/babel">
      ReactDOM.render(
        <section>
          <Link />
          <Link />
          <Link />
        </section>,
        document.getElementById("root")
      );
    </script>
  </body>
</html>

```

And if we look at our result, we do indeed have three links.

This is the power of React: it takes the reusability of JavaScript functions, but allows us to use them like they were HTML.

We refer to these custom elements made with JavaScript as **components**.

So we've gained a great deal of readability here by using components. We don't have any confusion about what we're looking at if we've named our components well. No need to read through a ton of HTML elements to see what the app displays.

We see immediately that we have three custom links.

## The anatomy of a function component

Now that we know how components operate, let's take a second look at our Link function component:

Our code may look pretty straightforward, but there are a few subtle things you should take note of here:

```js
function Link() {
  return (
    <div>
      <a href="https://reactjs.org">
        React - A JavaScript Library for Building User Interfaces
      </a>
      <div>
        <h3>reactjs.org</h3>
      </div>
      <div>React makes it painless to create interactive UIs.</div>
    </div>
  );
}

```

The function component name is capitalized: Link instead of link. This is a required naming convention for React components. We use a capitalized name to distinguish components from normal functions. Note that functions which return JSX are not the same as normal JavaScript functions.

Notice how the JSX we are returning has a set of parentheses around it. As you are first writing your React code, it's easy to forget these parentheses, which will result in an error. Wrap your JSX in parentheses if it span more than one line.

Finally, our Link function returns some JSX. Every React component must return either JSX elements or other React components. And yes, React components can return other components.

So since React components can return other React components, we can make an App component.

This App component will contain our entire set or **tree of components** and will show of what our app consists.

And with an App component, this makes our render method much easier to read:

```html
<!DOCTYPE html>
<html>

  <head>
   ...
  </head>

  <body>
    <div id="root"></div>

    <script type="text/babel">
      function Link() {
        return (
          <div>
            <a href="https://reactjs.org">
              React - A JavaScript Library for Building User Interfaces
            </a>
            <div>
              <h3>reactjs.org</h3>
            </div>
            <div>React makes it painless to create interactive UIs.</div>
          </div>
        );
      }

      function App() {
        return (
          <section>
            <Link />
            <Link />
            <Link />
          </section>
        );
      }

      ReactDOM.render(<App />, document.getElementById("root"));
    </script>
  </body>

</html>
```

We see from this code that React components have a hierarchy or order like HTML elements. As a result, we can refer to different parts of our component tree as either **parents** or **children**.

In this case, for example, to each rendered Link component, App is the parent. To App, all three Links are its children.

Note that whenever we render or return JSX, there can only be one parent component. But a parent component can have as many child components (as well as elements) as needed.

When we look at the output of our code, you've likely noticed the following problem:

We have three instances of the same link! That's because we are using the same data for each link we create. Yet we know each link has different data—a different title, URL, short URL, and excerpt.

So how do we pass in unique data to our components?

## How to pass dynamic data to components: Props

If we wanted to pass some title text to a normal JavaScript function we would do so like this:

```js
Link("Our link title here");

```

But how to we do pass data to **function components**?

Normal HTML elements accept data in the form of attributes. But unlike HTML attributes, attributes aren't recognized on React components. The data doesn't stay on the component itself. Where do they go?

As arguments to the function component. Again, this is something we're familiar with since we know the basics of functions.

We know that functions output data using `return` and accept data with _arguments_.

If we had an HTML element, say a div with an attribute called "title", this code would be invalid. HTML doesn't have a title attributes for any of its elements:

```html
<div title="Our link title here"></div>

```

But if we created this title "attribute" on our Link component:

```html
<link title="Our link title here" />

```

This is valid. And since we wrote title like an attribute on our component, it is passed to the Link function as an argument called "title".

In code we can think of it like this:

```js
const linkData = { title: "Our link title here" };

Link(linkData);

```

Notice that the linkData argument is an object.

React collects and organizes the data passed to a given component as a single object.

The name for data passed to a component, such as title, is **props**.

All prop values exist within the function component itself on a props object.

And since our goal is to use our title prop within our Link component, we can write the following:

```js
function Link(props) {
  return <a>{props.title}</a>;
}

```

We use the curly braces `{}` syntax to insert the title prop from props.title wherever we want. And the same applies to any other prop passed down to a component.

These curly braces allow us to insert or interpolate dynamic values wherever we need.

Now we have everything we need to fix our links. For each of the Link components, we need to pass down their title, URL, short URL, and excerpt as individual props:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>reactjs Search Results</title>

    <script src="https://unpkg.com/react@16/umd/react.development.js"></script>
    <script src="https://unpkg.com/react-dom@16/umd/react-dom.development.js"></script>
    <script src="https://unpkg.com/babel-standalone@6.26.0/babel.js"></script>
  </head>

  <body>
    <div id="root"></div>

    <script type="text/babel">
      function Link(props) {
        return (
          <div>
            <a href={props.url}>{props.title}</a>
            <div>
              <h3>{props.shortUrl}</h3>
            </div>
            <div>{props.excerpt}</div>
          </div>
        );
      }

      function App() {
        return (
          <section>
            <Link
              title="React - A JavaScript Library for Building User Interfaces"
              url="https://reactjs.org"
              // props consisting of two or more words must be written in camelcase
              shortUrl="reactjs.org"
              excerpt="React makes it painless to create interactive UIs."
            />
            <Link
              title="React (web framework) - Wikipedia"
              url="https://en.wikipedia.org/wiki/React_(web_framework)"
              shortUrl="en.wikipedia.org › wiki › React_(web_framework)"
              excerpt="React is a JavaScript library for building user interfaces."
            />
            <Link
              title="React (@reactjs) | Twitter"
              url="https://twitter.com/reactjs"
              shortUrl="twitter.com › reactjs"
              excerpt="The latest Tweets from React (@reactjs)."
            />
          </section>
        );
      }

      ReactDOM.render(<App />, document.getElementById("root"));
    </script>
  </body>
</html>

```

Looking at our output, we still get the same result.

But there was a bit of a trade-off here. Through props, we were able to make our Link component much more readable.

Now we can make any Link based off of whatever (valid) prop data we give it.

But now you can see that our App component got a lot bigger by providing the prop values immediately on each Link.

_Isn't there a way that we can move all this data somewhere else?_

## How to separate the data from the interface

Let's move our data out of the component tree and put it somewhere more convenient, but still use the data as needed.

To do that we'll make an array of objects with the link data to pass down to the Link components through props.

This allows us to put our data wherever we want, in another JavaScript file even. The benefit is that it doesn't clutter up our components anymore.

```html
<!DOCTYPE html>
<html>
  <head>
    ...
  </head>

  <body>
    <div id="root"></div>

    <script type="text/babel">
      const linkData = [
        {
          title: "React - A JavaScript Library for Building User Interfaces",
          url: "https://reactjs.org",
          shortUrl: "reactjs.org",
          excerpt: "React makes it painless to create interactive UIs."
        },
        {
          title: "React (web framework) - Wikipedia",
          url: "https://en.wikipedia.org/wiki/React_(web_framework)",
          shortUrl: "en.wikipedia.org › wiki › React_(web_framework)",
          excerpt: "React is a JavaScript library for building user interfaces."
        },
        {
          title: "React (@reactjs) | Twitter",
          url: "https://twitter.com/reactjs",
          shortUrl: "twitter.com › reactjs",
          excerpt: "The latest Tweets from React (@reactjs)."
        }
      ];

      function Link(props) {
        return (
          <div>
            <a href={props.url}>{props.title}</a>
            <div>
              <h3>{props.shortUrl}</h3>
            </div>
            <div>{props.excerpt}</div>
          </div>
        );
      }

      function App() {
        return (
          <section>
            <Link title="" url="" shortUrl="" excerpt="" />
            <Link title="" url="" shortUrl="" excerpt="" />
            <Link title="" url="" shortUrl="" excerpt="" />
          </section>
        );
      }

      ReactDOM.render(<App />, document.getElementById("root"));
    </script>
  </body>
</html>

```

Now how do we display each Link with its data using the linkData array?

If you've worked with arrays before, to get each element we loop or iterate over the array. Here, for each loop, we can pass the props data down to the Link component again.

This pattern is a very common one in React. So much so that there is a special array method that we can use to perform this iteration, called .map(). It is not the same as the map method in regular JavaScript—it is for working with JSX and components alone.

```html
<!DOCTYPE html>
<html>

  <head>
    ...
  </head>

  <body>
    <div id="root"></div>

    <script type="text/babel">
      const linkData = [
        {
          title: "React - A JavaScript Library for Building User Interfaces",
          url: "https://reactjs.org",
          shortUrl: "reactjs.org",
          excerpt: "React makes it painless to create interactive UIs."
        },
        {
          title: "React (web framework) - Wikipedia",
          url: "https://en.wikipedia.org/wiki/React_(web_framework)",
          shortUrl: "en.wikipedia.org › wiki › React_(web_framework)",
          excerpt: "React is a JavaScript library for building user interfaces."
        },
        {
          title: "React (@reactjs) | Twitter",
          url: "https://twitter.com/reactjs",
          shortUrl: "twitter.com › reactjs",
          excerpt: "The latest Tweets from React (@reactjs)."
        }
      ];

      function Link(props) {
        return (
          <div>
            <a href={props.url}>{props.title}</a>
            <div>
              <h3>{props.shortUrl}</h3>
            </div>
            <div>{props.excerpt}</div>
          </div>
        );
      }

      function App() {
        return (
          <section>
            {linkData.map(function(link) {
              return (
                <Link
                  key={link.url}
                  title={link.title}
                  url={link.url}
                  shortUrl={link.shortUrl}
                  excerpt={link.excerpt}
                />
              );
            })}
          </section>
        );
      }

      ReactDOM.render(<App />, document.getElementById("root"));
    </script>
  </body>

</html>
```

By moving our data out of the UI and displaying each link using .map(), we have a far simpler React app that can accept as many links as we choose.

Finally, note in our code that where we are mapping over our linkData, the entire expression is surrounded by our curly braces. Be aware that JSX allows us to insert any valid JavaScript expression between curly braces.

## How to build apps the "React" way

What was the point of covering these various patterns?

Not only to cover the basics of JSX and how React combines HTML and JavaScript, but also to show you how React developers think.

How do you think like a React developer? By knowing how to break down your UI into reusable components.

When a React developer plans out an application they want to make, they start by identifying all individual parts of the app and seeing what parts can be made into reusable components. 

We do that by seeing if each part has the same visual (HTML) structures and accept the same or very similar sets of data (through props).

Now to come full circle, let's take a new look at the starting UI that we wanted to recreate at the beginning. 

If we were to look at this like a React developer, it might look something like this:

![Image](https://www.freecodecamp.org/news/content/images/2023/09/image-3-1.png)

The better you get with using components, the faster you'll be able to build your own websites and applications with ease.

## Become a Professional React Developer

React is hard. You shouldn't have to figure it out yourself.

I've put everything I know about React into a single course, to help you reach your goals in record time:

[**Introducing: The React Bootcamp**](https://www.reactbootcamp.com)

**It’s the one course I wish I had when I started learning React.**

Click below to try the React Bootcamp for yourself:

[![Click to join the React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.reactbootcamp.com)
*Click to get started*


