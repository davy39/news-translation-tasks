---
title: How to show in-app messages using Material-UI in a React web app
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-27T23:33:12.000Z'
originalURL: https://freecodecamp.org/news/how-to-show-informational-messages-using-material-ui-in-a-react-web-app-5b108178608
coverImage: https://cdn-media-1.freecodecamp.org/images/1*awO-09f5MGtVvnkbVLoBDA.png
tags:
- name: Material Design
  slug: material-design
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: Tutorial
  slug: tutorial
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Kelly Burke

  In some situations, your web app needs to show an informational message to tell
  users whether an event was successful or not. For example, a “Success” message after
  a user clicks a button and successfully completes some action.

  In this...'
---

By Kelly Burke

In some situations, your web app needs to show an informational message to tell users whether an event was successful or not. For example, a “Success” message after a user clicks a button and successfully completes some action.

In this tutorial, I’ll show you how to create a simple component for informational, in-app messages with React and Material-UI. We’ll call it a `Notifier` component.

Here are the main sections of this tutorial:

* Getting started
* Notifier component
* Import Notifier component to Index page
* Testing

If you find this article useful, consider starring our [Github repo](https://github.com/builderbook/builderbook) and checking out our [book](https://builderbook.org/book) where we cover this and many other topics in detail.

### **Getting started**

For this tutorial, I’ve created a simple web app for you to follow. We’ll use code located in the [tutorials/4-start](https://github.com/builderbook/builderbook/tree/master/tutorials/4-start) folder of our [builderbook repo](https://github.com/builderbook/builderbook).

If you don’t have time to run the app locally, I deployed this example app [here](https://notifier.builderbook.org).

To run the app locally:

* Clone the builderbook repo to your local machine with:

```
git clone git@github.com:builderbook/builderbook.git
```

* Inside the `4-start` folder, run `yarn` or `npm install` to install all packages listed in `package.json`.
* Run `yarn dev` to start the app.

#### Index page

On your browser, go to [http://localhost:3000](http://localhost:3000). This is our `Index` page, which has the `/` route. Next.js provides automatic routing for pages located in a `/pages` folder. The name of each page file becomes that page’s route.

Our `Index` page is a simple page component that renders a form, an input, and a button (more explanation below).

![Image](https://cdn-media-1.freecodecamp.org/images/1*I50gTzdSn6aPSI3JYk9Hqw.png)

Here’s the code for our `Index` page at `pages/index.js`:

A few notes:

* We could have defined this page as a stateless functional component, since it has no state, lifecycle hooks, or refs ([read more](https://www.jstwister.com/post/react-stateless-functional-components-best-practices/) about when to use stateless functional components versus React ES6 classes). You’ll see this Eslint warning: `Component should be written as a pure function`. However, the **final** `Index` page that we write in this tutorial will have ref. Hence, we wrote this **initial** `Index` page as a child of [ES6 class](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes) using [extends](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/extends).
* We imported [Head](https://github.com/zeit/next.js/#populating-head) from Next.js in order to customize the `<He`ad> element of the page. I`nside` <Head>, we a`dded a` page `<t`itle> and<meta> description for proper indexing by search engine bots (good fo`r SEO).` The text inside <title> displays on your browser tab:

![Image](https://cdn-media-1.freecodecamp.org/images/1*QtsMfsiewcSAb5AOE8LvsA.png)

* We used Material-UI’s [TextField](https://material-ui-next.com/api/text-field/#textfield) and [Button](https://material-ui-next.com/demos/buttons/#buttons) components, which render into `<inp`ut>`; and &l`t;button> HTML elements, respectively.
* We wrapped our page with a `withLayout` higher-order component. Our app uses Next.js, and `withLayout` ensures that server-side rendering works properly for Material-UI inside our React-Next app. `withLayout` also adds our `Header` component (located at `components/Header.js`) to each page that `withLayout` wraps. Server-side rendering is not necessary for Material-UI or React, but it is a main feature of Next.js. We discussed [server-side vs. client-side rendering](https://hackernoon.com/server-side-vs-client-side-rendering-in-react-apps-443efd6f2e87) in React apps in another tutorial.

We are done describing our initial `Index` page. Now let’s discuss the `Notifier` component that we will later import into the `Index` page to show informational messages to our web app users.

### Notifier component

Let’s start by defining the `Notifier` component. We define `Notifier` as a `React.Component` instead of a stateless function, because `Notifier` will have state, one lifecycle method, and a few event handling functions.

For our informational messages, we will use Material-UI’s [Snackbar](https://material-ui-next.com/demos/snackbars/#snackbars). Check out [examples](https://material-ui-next.com/demos/snackbars/#snackbars) of using Snackbar on the official Material-UI site.

Here’s a high-level outline of our `Notifier` component:

Create a `Notifier.js` file inside the `/components` folder of `4-start`. Add the above high-level outline to this file. Below, we will replace the numbered comments with code.

1. We will use the `open` and `message` props of Material-UI’s Snackbar for the state of our `Notifier`. Check the [full list of props](https://material-ui-next.com/api/snackbar/#props) for Snackbar.

Initially, our `Notifier` should be in a closed state with an empty string as a message. We define the `Notifier`'s initial state as:

2. Now let’s write a function that updates the state of the Notifier component. The function will change the value of the `open` prop to `true` and set the value of the `message` prop to a non-empty string. Let’s call this function `openSnackbar()`.

Before we can execute `openSnackbar()`, our `Notifier` component needs to be mounted in the DOM. Thus, we put the `openSnackbar()` function into a `componentDidMount` lifecycle method that executes right after the `Notifier` component mounts in the DOM.

In order to access the `openSnackbar()` function **anywhere** in our app, we have to set its value to another function that is available outside of the `Notifier` component. Hence, we write `let openSnackbarFn` above `class Notifier extends React.Component`.

Putting these pieces together:

Now let’s define the `openSnackbar()` function. This function will update the `open` and `message` properties of our `Notifier`’s state. Once the state is updated, the `Notifier` component will get re-rendered to show a message (`open:true` displays the Snackbar, and `message:message` sets the message).

Inside `this.setState`, we could have written `message` as `message:message`. Instead, we used ES6 [shorthand syntax](https://eslint.org/docs/rules/object-shorthand) (enforced by Eslint) to make the code more concise.

3. When a user clicks outside of the Snackbar area, the Snackbar should close. The Snackbar prop `onClose` is responsible for this behavior. Let’s write a function called `handleSnackbarClose()` that sets `open` to `false` and `message` to an empty string.

4. Finally, let’s write code for our `Notifier` component to render the Snackbar component with all necessary props.

In addition to the `message`, `onClose`, and `open` props described above, we’ll add the following props to our Snackbar component:

* `anchorOrigin`: specifies the Snackbar location
* `autoHideDuration`: specifies the Snackbar duration in milliseconds
* `SnackbarContentProps`: binds the Snackbar to an element inside the DOM that contains `message`; in our case, the element has the id `snackbar-message-id`, and the Snackbar will display text from this element.

Here is the `render()` method of our `Notifier` component:

In the `<sp`an> element, we could have wr`itten message={this.state.me`ssage}, but instead we `wrote dangerouslySetInnerHTML={{ __html: this.state.mess`age }} . This allows us to add HTML code to the Snack`bar’s m`essage prop. For instance, you may want to show a hyperlink to u[sers. Rea](https://reactjs.org/docs/dom-elements.html#dangerouslysetinnerhtml)d more about using dangerouslySetInnerHTML in React.

After putting the code from steps 1–4 together, here’s our final `Notifier` component:

Important note: notice how we exported our `openSnackbar()` function in addition to `Notifier` component. We will import **both** `openSnackbar()` and `Notifier` into our `Index` page.

### Import Notifier component to Index page

Let’s go back to our `Index` page, where we will import our `Notifier` component and `openSnackbar()` function.

Without triggering the `openSnackbar()` function, our `Notifier` component will always stay in its initial closed state with an empty string as a message. We need to execute `openSnackbar()` after a user submits the form by clicking the button on our `Index` page. Let’s define a `showNotifier()` function that does exactly that.

#### showNotifier Function

We will call `showNotifier()` inside the `<fo`rm> element. We’ll `make showNoti`fier() execute when a user enters a number on the form and clicks the “Submit” button.

Here’s the current `<fo`rm> o`n our` Index page:

Let’s make two modifications:

1. To call `showNotifier()` when the form is submitted, we use JavaScript’s [onsubmit Event](https://www.w3schools.com/jsref/event_onsubmit.asp):

2. A user will enter a number inside `TextField`. In order for our `showNotifier()` function to access the value of `TextField`, we add React’s [ref attribute](https://reactjs.org/docs/refs-and-the-dom.html#adding-a-ref-to-a-dom-element) to `TextField`.

There are two ways to get the value of `TextField`: with `this.state` and with `ref`. We chose `ref`, since `this.state` is more concise. Here’s an [explanation](https://stackoverflow.com/questions/36683770/react-how-to-get-the-value-of-an-input-field?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa) of writing with `this.state`, and here’s [more info](https://reactjs.org/docs/refs-and-the-dom.html#callback-refs) about using `ref` in React.

Now let’s define the `showNotifier()` function. Here’s the high-level outline for `showNotifier()`:

Below, we’ll write code for each of the three comments above.

1. We define `answer` as:

This line of code says that IF `answerInput` exists (meaning the `<inp`ut> element is added to the DOM), `THEN` answer equals the val`ue of answe`rInput, which is accessed `with answerInput`.value.

IF `answerInput` does not exist, THEN the entire condition in parentheses is false and `answer` equals `null`.

2. If a user does not enter an answer on our form but clicks the “Submit” button, we will show this message: `Empty field. Enter a number.`

3. If a user enters 4 and clicks the “Submit” button, then our `openSnackbar()` function will run and show this message: `Correct answer!`. Otherwise, it will show `Incorrect answer.`

We use `parseInt(answer, 10)` to parse `answer`, which is a string, and return an integer. The parameter `10` specifies that the integer is in decimal format.

Let’s put together the code from steps 1–3 above for our `showNotifier` function. We’ll place the code right under the line `class Index extends React.Component`:

You’ll notice that we added a line `event.preventDefault();`. This will prevent our `<fo`rm> element from its default behavi[or of sending form data to a](https://developer.mozilla.org/en-US/docs/Learn/HTML/Forms/Sending_and_retrieving_form_data) server.

Now we have all the code for our final `Index` page:

### Testing

Let’s test that our `Notifier` works as expected. Run the app locally with `yarn dev` and navigate to [http://localhost:3000](http://localhost:3000). If you aren’t running the app, go to the one I deployed: [https://notifier.builderbook.org](https://notifier.builderbook.org).

First, click “Submit” without adding anything in the text field.

![Image](https://cdn-media-1.freecodecamp.org/images/1*tFZ2EbE513_ACJqNMPiHYw.png)

Next, add the number 4 and click “Submit”.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ov1Nt7TI_VcHWOgn-zb9WQ.png)

Now add any other number and click “Submit”.

![Image](https://cdn-media-1.freecodecamp.org/images/1*61lDH0rzRRsReG4X36GV8A.png)

Remember that we wrote code to close the Snackbar when a user clicks away from it (we wrote a `handleSnackbarClose()` function and passed it to the `onClose` prop of the Snackbar). After seeing the Snackbar, click anywhere besides the Snackbar itself on your screen. The Snackbar should close immediately.

A nice feature of Material-UI is mobile optimization. We don’t have to write extra code for our informational message to look good on mobile devices. See for yourself by going to Chrome’s DevTools and changing the view from desktop to mobile. Our message appears across the top of the screen:

![Image](https://cdn-media-1.freecodecamp.org/images/1*3t4ur9VU3LOw2ytbKHrvAQ.png)

Woohoo! You’ve successfully added an informational, in-app message to a React web app! Your final code should match the code in the [tutorials/4-end](https://github.com/builderbook/builderbook/tree/master/tutorials/4-end) folder of our [builderbook repo](https://github.com/builderbook/builderbook).

#### Customize Notifier component

Now that you have a working `Notifier` component, let’s see how we can modify the UX by changing props of Material-UI’s SnackBar component. Here’s the [full list](https://material-ui-next.com/api/snackbar/#props) of props you can use.

First, let’s change the duration of the Snackbar. Insider your `Notifier` component, find the `autoHideDuration` prop. Change its value from `3000` to `1000` and compare. You’ll see that at `1000`, the Snackbar closes more quickly.

Second, let’s change the position of the Snackbar. Find the `anchorOrigin` prop and change its values from `top` and `right` to `bottom` and `left`, respectively. Check where the Snackbar appears now:

![Image](https://cdn-media-1.freecodecamp.org/images/1*9ANw1zxyhHSQBOECUR_G2Q.png)

Finally, let’s make the Snackbar `message` include a hyperlink. Recall that we added `dangerouslySetInnerHTML={{ __html: this.state.message }}` to our `message` prop in the Snackbar so that we can write HTML inside of it.

Change the code for our `Correct answer!` and `Incorrect answer.` messages like this:

Now users will see the messages below. Notice the dark blue hyperlinks for text inside the `<`;a> tags.

![Image](https://cdn-media-1.freecodecamp.org/images/1*fGzjKrwd2noPg34wQUOTCw.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*lYm3vmPuDAx4klVt33BwWw.png)

If you’re learning how to build web apps with JavaScript, check out our [Github repo](https://github.com/builderbook/builderbook) and our [book](https://builderbook.org/book), where we cover this and many other topics in detail.

To get email updates about our tutorials, subscribe [here](https://builderbook.org/tutorials).

