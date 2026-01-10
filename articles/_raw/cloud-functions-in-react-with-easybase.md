---
title: How to Deploy Dynamic Cloud Functions in React and React Native with Easybase
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-04-13T18:37:52.000Z'
originalURL: https://freecodecamp.org/news/cloud-functions-in-react-with-easybase
coverImage: https://cdn-media-2.freecodecamp.org/w1280/606b5c58d5756f080ba94a3a.jpg
tags:
- name: Cloud Computing
  slug: cloud-computing
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: React Native
  slug: react-native
seo_title: null
seo_desc: "By Michael Bagley\nCloud functions are stateless, single-purpose code snippets\
  \ that can be invoked programmatically or through other event-driven processes.\
  \ \nThese code snippets are not built into your application, as a traditional function\
  \ would be. ..."
---

By Michael Bagley

Cloud functions are stateless, single-purpose code snippets that can be invoked programmatically or through other event-driven processes. 

These code snippets are not built into your application, as a traditional function would be. Rather, they are **stored in a cloud container** that is maintained by a provider. They can be edited live and hide business logic from the locally available front-end code.

React and React Native can greatly benefit from this method of application development due to their declarative programming style. Events in the UI can predictably call your function in a React-friendly manner. Let's try it!

## **Setup**

We'll start by creating a brand new React or React Native application. The easiest way to create one of these projects is to use `npx` which comes with a standard Node.js installation. If you don't have these modules installed, you can [install them here](https://nodejs.org/en/). 

From there we can create a fresh project like so:

React: `npx create-react-app my-cloud-app`

React Native: `npx create-react-native-app`

After that finishes installing, move into your new project directory and run `npm run start`. Here's what my starting React project looks like:

![Image](https://www.freecodecamp.org/news/content/images/2021/04/Screen-Shot-2021-04-12-at-11.03.51-AM.png)

## **Example React Project**

The example React project I will create is a **simple cryptocurrency price fetcher**. 

The UI will feature a text box and button where users can submit a cryptocurrency's symbol like 'BTC' or 'ETH'. From there, the front end will call a serverless function, hosted by Easybase. The cloud function will call an API and return the specified price in USD.

First, let's add these interface elements to our React elements. Open up `src/App.js` and clear out the component under the root `header` tag. To start, we'll need four elements:

1. A text box
2. A text element to tell the user to input a cryptocurrency symbol
3. A button to invoke the cloud function based on the text box input
4. Finally, we need another text element to display the outputted result

Your `App` function may now look like the following:

```jsx
function App() {
  return (
    <div className="App">
      <header className="App-header">
        <p>Enter Cryptocurrency symbol:</p>
        <input placeholder="BTC, ETH, etc." type="text" />
        <button>Go</button>
        <p>Result:</p>
      </header>
    </div>
  );
}
```

Save this file and your new app will look something like this:

![Image](https://www.freecodecamp.org/news/content/images/2021/04/Screen-Shot-2021-04-12-at-11.46.38-AM.png)

**Great!** Now we need to make our application stateful, such that we save user input and have a callback for our button. 

We will use React's `useState` hook to store and display user input. Also, create an asynchronous function called `buttonCallback` that gets triggered when a user clicks the 'Go' button. For now, this function will just print the text box input.

Here is my implementation of `src/App.js` for reference:

```jsx
import { useState } from 'react';
import './App.css';

function App() {
  const [inputVal, setInputVal] = useState("");

  async function buttonCallback() {
    console.log(inputVal);
  }

  return (
    <div className="App">
      <header className="App-header">
        <p>Enter Cryptocurrency symbol:</p>
        <input placeholder="BTC, ETH, etc." type="text" value={inputVal} onChange={e => setInputVal(e.target.value)} />
        <button onClick={buttonCallback}>Go</button>
        <p>Result:</p>
      </header>
    </div>
  );
}

export default App;
```

## **How to Deploy Your Cloud Function**

So far, **everything works as expected**. Time to deploy a code snippet in the cloud. [Make a free account at easybase.io](https://easybase.io/) and click the **'+'** button on the bottom-left of the view.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/Screen-Shot-2021-04-12-at-1.04.33-PM.png)

Select the _Hello World_ template and proceed through the stepper. This will bring up a function that simply returns whatever is passed in for the value of _message_ in the request body.

The [Monaco code editor](https://microsoft.github.io/monaco-editor/) is built right into the website, so we can code live in our web browser! 

We are going to want a package from npm that helps us make requests to external APIs. Open up `package.json` and add the module _[cross-fetch](https://www.npmjs.com/package/cross-fetch)_ with the appropriate version (when we save our function, this module will automatically be installed):

![Image](https://www.freecodecamp.org/news/content/images/2021/04/Screen-Shot-2021-04-12-at-1.12.00-PM.png)

Now reopen `handler.js` and bring in the newly installed module at the top of the file with `var fetch = require('cross-fetch');`.

When we make our request from the front end, we will pass an object with the key `cryptoSymbol` representing the input value of the text box. So, let's create a variable to save that. Remember, `event.body` will reference whatever is passed into the function via the request body.

```js
const cryptoSymbol = event.body.cryptoSymbol;
```

We are going to use the [Cryptonator API](https://www.cryptonator.com/api/) to retrieve current prices. The route for getting prices is `https://api.cryptonator.com/api/ticker/**_pair_name_**` where `**_pair_name_**` is the given symbol (three letters) followed by '-usd'. 

The reason we follow the pair name with '-usd' is because we want to get the price of the given cryptocurrency in dollars, but you could use another symbol for different asset price conversion. Let's make a variable for this URL:

```js
const nexchangeUrl = `https://api.cryptonator.com/api/ticker/${cryptoSymbol}-usd`;
```

Here's the **full template** for our new function:

```js
var fetch = require('cross-fetch');

module.exports = async (event, context) => {
  const cryptoSymbol = event.body.cryptoSymbol;
  const nexchangeUrl = `https://api.cryptonator.com/api/ticker/${cryptoSymbol}-usd`;

  const res = await fetch(nexchangeUrl);
  const resJson = await res.json();
  if (resJson.success) {
    return context.succeed(resJson.ticker.price);
  } else {
    return context.fail("Symbol does not exist");
  }
}
```

Note: `context.succeed` and `context.fail` both send whatever is passed to the requesting client.

Save the function:

![Image](https://www.freecodecamp.org/news/content/images/2021/04/Screen-Shot-2021-04-12-at-1.50.55-PM.png)

We can expand the **Deploy** row and test the function. Add `cryptoSymbol` to the input body with the value of some crypto symbol (BTC, ETH, etc).

![Image](https://www.freecodecamp.org/news/content/images/2021/04/Screen-Shot-2021-04-12-at-1.52.58-PM.png)

**Congrats, your cloud function is working!** The first time you call your function it may take a few seconds, as it is performing a _cold start_. Cold starts occur when your function has not been invoked recently, so it gets offloaded from the provider's back end. It will be responsive when being actively called.

Now let's head over to our React/React Native app. Head to your project directory and install the [`easybase-react`](https://github.com/easybase/easybase-react) library.

```bash
cd my-cloud-app
npm install easybase-react
```

Now in our `src/App.js` file, we can import a function called `[callFunction](https://easybase.io/docs/easybase-react/modules/_callfunction_.html#callfunction)` from this newly installed package with `import { callFunction } from 'easybase-react`.

This function takes two parameters:

1. The function route (available under **Deploy** --> Deploy)
2. Request body object, accessible in our cloud function's `event.body` (Optional)

Here's where you can find your function route:

![Image](https://www.freecodecamp.org/news/content/images/2021/04/Screen-Shot-2021-04-12-at-5.48.34-PM.png)

In our `buttonCallback` function, use the imported `callFunction` to invoke our cloud function as detailed. **Note that `callFunction` is asynchronous –** both programming methods will work:

```js
const result = await callFunction('YOUR-CUSTOM-ROUTE', { cryptoSymbol: "BTC" });
console.log(result);

// OR

callFunction('YOUR-CUSTOM-ROUTE', { cryptoSymbol: "BTC" }).then(result => console.log(result));
```

In our application, we want to display the result in the last `<p>` tag. We will do this with another `useState` instance, such that the tag will now look like `<p>Result: {resultVal}</p>`. The `resultVal` variable will be set within our `buttonCallback` function as follows:

```js
  async function buttonCallback() {
    const result = await callFunction('YOUR-CUSTOM-ROUTE', { cryptoSymbol: inputVal });
    setResultVal(`${inputVal} currently costs $${result}`);
  }
```

![Image](https://www.freecodecamp.org/news/content/images/2021/04/Screen-Shot-2021-04-12-at-6.03.36-PM.png)

Input a crypto symbol in the text box and click 'Go' _—_ it works! For reference, here's my entire implementation (feel free to take code this and give it some style for a unique look and feel):

```jsx
import { useState } from 'react';
import './App.css';
import { callFunction } from 'easybase-react';

function App() {
  const [inputVal, setInputVal] = useState("");
  const [resultVal, setResultVal] = useState("");

  async function buttonCallback() {
    const result = await callFunction('YOUR-CUSTOM-ROUTE', { cryptoSymbol: inputVal });
    setResultVal(`${inputVal} currently costs $${result}`);
  }

  return (
    <div className="App">
      <header className="App-header">
        <p>Enter Cryptocurrency symbol:</p>
        <input placeholder="BTC, ETH, etc." type="text" value={inputVal} onChange={e => setInputVal(e.target.value)} />
        <button onClick={buttonCallback}>Go</button>
        <p>Result: {resultVal}</p>
      </header>
    </div>
  );
}

export default App;

```

## **Conclusion**

I hope this brief walkthrough was helpful to those interested in cloud computing and serverless application development! [There are many different frameworks/libraries available for developing UIs and applications](https://easybase.io/best-javascript-framework-library-quiz/), but React and React Native have proven to be great, robust options with thriving communities.

For those interested, here's some [comprehensive information on using Easybase with React/React Native](https://easybase.io/react/). The [`easybase-react` package](https://github.com/easybase/easybase-react) can handle other application modules such as user authentication.

Your serverless function will stay idle in the cloud when there's no traffic, **avoiding any charges.** If your application experiences a surge in usage, the cloud provider will be there to _elastically_ deliver the required performance. 

[This infrastructure, known as serverless computing, puts the burden of management, scaling, and readiness on the host](https://easybase.io/about/2021/01/30/What-Is-a-Serverless-Application/). The best part is that there is no maintenance required on your end. Also, check out my other walkthrough on [freeCodeCamp about serverless databases for React & React Native](https://www.freecodecamp.org/news/how-to-add-a-serverless-database-to-react-projects-and-web-apps/). 

_Thanks for reading and happy coding!_




