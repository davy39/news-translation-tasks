---
title: How to build native desktop apps with JavaScript (Proton Native)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-08T22:17:48.000Z'
originalURL: https://freecodecamp.org/news/build-native-desktop-apps-with-javascript-a49ede90d8e9
coverImage: https://cdn-media-1.freecodecamp.org/images/1*XyeRix8Z-yOcpRlpubtyuA.png
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Mohammed Salman

  When I was writing this article, Atwood’s Law came to mind:


  Any application that can be written in JavaScript, will eventually be written in
  JavaScript. - Jeff Atwood



  don’t worry about it

  Originally posted on my blog!

  Today we a...'
---

By Mohammed Salman

When I was writing this article, Atwood’s Law came to mind:

> Any application that can be written in JavaScript, will eventually be written in JavaScript. - [Jeff Atwood](https://en.wikipedia.org/wiki/Jeff_Atwood)

![Image](https://cdn-media-1.freecodecamp.org/images/1*XyeRix8Z-yOcpRlpubtyuA.png)
_don’t worry about it_

[Originally posted on my blog!](https://code.nimrey.me/how-to-build-native-desktop-apps-with-js/)

Today we are going to take a look at [Proton Native](https://proton-native.js.org), and make a simple app with it.

Unlike **Electron** apps, apps built with **Proton Native** are actually **native** (hence the name) and not web-based on chromium.

**Proton Native** is like **React Native** but for desktop. It compiles to native platform code, so it looks and performs like a native app.

So let’s get started.

#### Windows

Install the build tools by running:

```
npm install --global --production windows-build-tools
```

#### Linux

You’ll need these libraries:

* libgtk-3-dev
* build-essential

#### Mac

You don’t need anything.

Now run the following:

```
npm install -g create-proton-app
```

and

```
create-proton-app my-app
```

to make a new project.

Open the project directory with your favorite code editor. The directory should look like this:

```
 └───node_modules
 ├───.babelrc
 ├───index.js
 ├───package.json
 └───package-lock.json
```

`index.js` should look like this:

![Image](https://cdn-media-1.freecodecamp.org/images/1*BUgjpvWtCCZNPJ__qrQxig.png)
_As you can see it look like React/React Native File_

Just like any React or React Native Project, we import the react library and make a class component.

The `App` element is just a container that holds the `Window` and `Menu`, and the `Window` has three props: `title` (the window title), `size` (takes an object that contains the width and height of the window), and `menuBar` (set to false because we don’t want a menu bar).

Before we start coding, let’s install `crypto` using `npm`:

```
npm i crypto
```

We will use `crypto` to hash the text with the MD5 algorithm.

### index.js

```js
import React, { Component } from "react";
import { render, Window, App, Box, Text, TextInput } from "proton-native";
import crypto from "crypto";

class Example extends Component {
  state = { text: "", md5: "" };

  hash = text => {
    this.setState({ text });
    
    let md5 = crypto
      .createHash("md5")
      .update(text, "utf8")
      .digest("hex");

    this.setState({ md5 });
  };
  render() {
    return (
      <App>
        <Window
          title="Proton Native Rocks!"
          size={{ w: 300, h: 300 }}
          menuBar={false}
        >
          <Box>
            <TextInput onChange={text => this.hash(text)} />
            <Text>{this.state.md5}</Text>
          </Box>
        </Window>
      </App>
    );
  }
}

render(<Example />);
```

I first imported `Text` and `TextInput` so I could use them later. Then in the `class` after setting the `text` and `md5` to empty strings in the `state` object, I created a function `hash` that takes a `text` argument.

In the `hash` function, we set the state to `text` and declare `md5` to store the encrypted text (as below)

```js
this.setState({ text });
let md5 = crypto.createHash("md5")
  .update(text, "utf8").digest("hex");
```

and set the state object to the updated `md5`.

```js
this.setState({ md5 });
```

The `render` method returns some `jsx` element. The `Box` element is just like `div` in React, or `View` in React Native, which holds the `TextInput` and `Text` . This is because the parent window element doesn’t allow having more than one child.

`TextInput` has an `onChange` prop that will be called every time the text changes. Therefore, we set it to a fat arrow function that takes a `text` argument and returns the `hash` function we declared earlier.

So now every time the text changes, `text` is hashed and set to `md5`.

Now if we run it with

```
npm run start
```

this window should pop up:

![Image](https://cdn-media-1.freecodecamp.org/images/1*D_fBTxyGSpUbIVPcyt3Kzw.png)

And if we enter some text, it gets hashed to md5 like this:

![Image](https://cdn-media-1.freecodecamp.org/images/1*azNLC0SBkJs85SK-fj15fw.png)

You might say “It looks ugly — let’s add some styling to it.” Well, at the time of writing this article, Proton Native is still at it’s infancy. It’s very buggy and it doesn’t support styling (yet), but it’s a fun project to play with.

If you want to contribute to the project, check out the [repo](https://github.com/kusti8/proton-native).

If you have any questions or suggestions, feel free to comment or reach me on Twitter [@4msal4](https://twitter.com/4msal4) and don’t forget to hit that clap button :)

👇Check out my previous story👇

[How to build a news app with React Native](https://medium.freecodecamp.org/create-a-news-app-using-react-native-ced249263627).

