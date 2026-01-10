---
title: How to test a Socket.io-client app using Jest and the react-testing-library
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-13T12:33:33.000Z'
originalURL: https://freecodecamp.org/news/testing-socket-io-client-app-using-jest-and-react-testing-library-9cae93c070a3
coverImage: https://cdn-media-1.freecodecamp.org/images/0*hO-7lLXvx8RG6CAQ
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: Testing
  slug: testing
seo_title: null
seo_desc: 'By Justice Mba

  Testing the quality of real-time Socket.io-client integration seems to have sunk
  into oblivion, maybe because the UIs had a long history of testability issues. Let’s
  fix this!

  Quickly google “testing socket.io app”.

  The first two resul...'
---

By Justice Mba

Testing the quality of real-time Socket.io-client integration seems to have sunk into oblivion, maybe because the UIs had a long history of testability issues. Let’s fix this!

Quickly google “testing socket.io app”.

The first two result pages (just don’t bother opening the rest of the pages) are all examples and tutorials focusing on testing the server-side socket.io integration. No one is talking about the quality of socket.io-client integration on the front-end, how the User Interface will look when it receives certain events, and if the front-end code is actually emitting the right events.

But why? Does this just mean that people don’t really care about the quality of their real-time apps on the front-end — the meat of the software? I don’t think so. My guess is: Testing UIs _was_ **just too hard!**

User Interfaces have had a long history of testability issues. UIs are never stable. The testing tools we have had available to us easily lead to writing very brittle UI tests. Thus, people tend to focus their time and energy on testing their socket.io apps only on the server-side.

But that doesn’t feel right. It is **only** the UI that makes our user confident that they’re actually accomplishing the purpose of using our app. But then, unto us a UI testing tool has been born!

### react-testing-library

It was a few months ago that my friend and mentor [Kent C. Dodds](https://www.freecodecamp.org/news/testing-socket-io-client-app-using-jest-and-react-testing-library-9cae93c070a3/undefined) [released this beautiful tool](https://blog.kentcdodds.com/introducing-the-react-testing-library-e3a274307e65) for testing react apps. Ever since then, I no longer just love the **idea** of testing UIs, but actually love testing them. I have literally dug out and tested all the UI code I gave up on testing because of its complexity :).

In my experience-based opinion, the react-testing-library is the panacea for all UI test issues. It is not just a testing tool, it is a testing approach.

Note: If your’re not a React person, there is [vue-testing-library](https://www.npmjs.com/package/vue-testing-library), [ng-testing-library](https://www.npmjs.com/package/ng-testing-library) and [others](https://www.npmjs.com/browse/depended/dom-testing-library), all built on top of the [dom-testing-library](https://www.npmjs.com/package/dom-testing-library).

The best feature of the react-testing-library is probably its support of UI TDD. According to the docs, it’s [primary guiding principle](https://twitter.com/kentcdodds/status/977018512689455106) is:

> _The more your tests resemble the way your software is used, the more confidence they can give you._

This is the “approach” I’m talking about. Test your UIs just as your non-techie friend would. Your user probably neither knows nor cares what your code looks like. And nor should your test. That gives us the power to use TDD on our UIs.

This is how we’re going to write our socket.io-client test — test everything without thinking about the code. Now let’s do it!

### Testing out the Telegram app

From our very talented Telegram UI designer, bellow are the designs of the Telegram app we’ll be testing.

![Image](https://cdn-media-1.freecodecamp.org/images/1*-DkSudIVU8WGeLQTWeZf8g@2x.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*5s82AK1rmhshHVic0XCpXA@2x.jpeg)
_telegram chat screenshots_

Looking at the design, I see a couple of real-time features our user would want to make sure the app performs, otherwise they’ll close the tab. Here are some of them:

* App should get messages
* App should tell when/if a message is sent or not
* App should tell when/if a message is delivered or not
* App should tell when a friend comes online/goes offline
* App should tell when a friend is typing

Okay, the list goes on…but let’s work on these first.

#### Receiving messages

Let’s look at how a user would know if they received a message as an example. First, create a test file, then import the chat.js file and its mocked dependencies. If you’re new to mocking or stuff like that, then [Kent C. Dodds](https://www.freecodecamp.org/news/testing-socket-io-client-app-using-jest-and-react-testing-library-9cae93c070a3/undefined) should really be your friend. He’s got everything covered on JavaScript testing, so just follow him on here, Twitter, and everywhere else.

Now as I was writing this line, I was thinking he should just write a book on JS testing so I tweeted:

And hopefully, he will eventually :)

Back to our test file:

```
// chat.test.jsimport React from 'react';import io from 'socket.io-client';
```

```
import Chat from './chat';
```

Because, we’re only doing integration testing here, we don’t really want to emit socket.io events to the server. So we need to mock out socket.io-client. For more information on mocking, see Kent’s article “[But really, what is a JavaScript mock?](https://blog.kentcdodds.com/but-really-what-is-a-javascript-mock-10d060966f7d)” as well as this section from the Jest docs on [Jest’s Mock Functions](https://facebook.github.io/jest/docs/en/mock-functions.html#using-a-mock-function).

Once you understand how to mock, the next thing is understanding what your module is doing, and then fake the implementation.

```
// socket.io-client.js
```

```
let EVENTS = {};
```

```
function emit(event, ...args) { EVENTS[event].forEach(func => func(...args));}
```

```
const socket = { on(event, func) {  if (EVENTS[event]) {   return EVENTS[event].push(func);  }  EVENTS[event] = [func]; }, emit};
```

```
export const io = { connect() {  return socket; }};
```

```
// Additional helpers, not included in the real socket.io-client,just for out test.
```

```
// to emulate server emit.export const serverSocket = { emit }; // cleanup helperexport function cleanup() { EVENTS = {}}
```

```
export default io;
```

With that, we have a good-enough socket.io-client mock for our test. Let’s use it.

```
// chat.test.jsimport React from 'react';import mockio, {serverSocket, cleanUp } from 'socket.io-client';
```

```
import Chat from './chat';
```

Now let’s write our first test. The traditional TDD approach says we’ll write a test for a feature, see it fail, then go implement the feature to satisfy our test. For brevity, we’re not going to do _exactly_ that, as this article focuses on testing.

Following the react-testing-library approach, the first thing you do before you write any test is to ask yourself: “How will a user test this feature?” For the first test in our list above, you ask yourself, “how will a user know that they’re getting the messages their friend is sending?”. To test it, they’ll probably tell the person next to them to send them a message.

Usually, how that will work is that the user’s friend sends a message to the server, with the user’s address, then the server emits the message to the user. Now, since we’re not testing if the user can send a message at this time, but whether the user can **receive** a message, let’s have`socket.io server` directly send the user a message.

```
// chat.test.jsimport React from 'react';import mock-io, {serverSocket, cleanUp } from 'socket.io-client';import {render} from 'react-testing-library';
```

```
import Chat from './chat';
```

```
test('App should get messages', () => {  // first render the app  const utils = render(<Chat />)    // then send a message  serverSocket.emit('message', 'Hey Wizy!');})
```

Above we imported the `render` method from the react-testing-library, which is just a wrapper around `ReactDom.render`. In our text, we use it to render our Chat app. The render method returns a test utility object that contains query methods we can use to query the `container` of our app — the DOM node `render` rendered our app into — for DOM nodes our test is interested in. Next in the text, use our mock socket.io server to send a message to the user.

Now that we’ve sent a message to the user, think again: how will the user know they’ve gotten the message? From the design above, they’ll definitely have to look at the screen to see the message appear. So to test that, we have to query the container of our app to see if it has any node that contains the message we sent, ‘Hey Wizy!’ To do that, the utility object returned from `render` has a query method called `getByText`, so we could simply do:

`expect(utils.getByText('Hey Wizy!')).toBeTruthy();`

While that might work, unfortunately, we can’t do that. Here’s why: All query methods returned from `render` will search the entire container for the specified query. That means that `getByText`, as used above, will search the entire container for the text ‘Hey Wizy!’, then returns the first node that has that text.

But that’s not how our user will look for the text. Instead, our user will only look **within** the ‘messages-section’, the section that contains all the messages. Only if messages appear in that section will they know they’ve got a message. So to make sure our test resembles how the user is using our app, we’ll need to search for the text ‘Hey Wizy!’ **only within** the messages-section, just as the user would do.

For that, the react-testing-library provides us with a unique query method call, `within`, which helps us focus our query **within** a particular section of the rendered document. Let’s use it!

Note: `within` is a new API that was inspired by this article, so make sure you have the very latest version of the react-testing-library.

```
// chat.test.jsimport React from 'react';import mock-io, {serverSocket, cleanUp } from 'socket.io-client';import {render, within} from 'react-testing-library';
```

```
import Chat from './chat';
```

```
test('App should get messages', () => {  // first render the app  const utils = render(<Chat />)    // then send a message  serverSocket.emit('message', 'Hey Wizy!');    // the message must appear in the message-section  const messageSection = utils.getByTestId('message-section');  // check withing messageSection to find the received message  const message = within(messageSection).getByText('Hey Wizy!');})
```

First, we grabbed the message section with a query method `getByTestId`. To use `getByTestId` in your test, you have to hard-code it in the DOM. Like so:

`<div data-testid=”message-section”` />

Because `getByTestId` does not closely resemble how users locate sections of your app, you should use it only on spacial cases and only when you’re certain there is no better alternative.

Still, our test is not relying on the DOM structure. Even if someone changes the `div` to a `section` tag or wraps it 10 levels deep in the DOM, our test doesn’t just care about the code — it just cares about the test-id.

Lastly, we use the `within` method as described earlier to get the received message. If the text is not found, `getByText` will throw and fail our test.

And that’s how we assert that the App can get messages.

#### Writing more tests

Let’s see some more query methods that the react-test-library gives us. We’ll see how we can further combine the APIs we’ve already learned to perform more complex queries without relying on the UI code.

So now, let’s write the second test: the App should tell the user when/if a message has been sent or not. Also, I think this test is basically doing the same thing as the next one in the list, so let’s merge both into one example.

Again, the first question we ask is…? I know you got it: “how will our user test this feature?” Okay, how you phrase your question might be different, but you get the idea :). So to test the sending message feature, the steps will look like this:

* The user locates the input to enter their message. Then they enter their message. Finally, they click the send button.
* The message should appear on the message-section
* The server will tell if the message got to the server, which means sent
* The UI should mark the message as sent
* The server then tells when the message is delivered
* The UI should, in turn, update the message as delivered

How does the user locate the input to enter their message? From the UI design we’re working with, they’ve gotta look and find the input with the placeholder ‘message’. (Well, that’s actually the only input on the screen, but even if there are more, the user will identify the input to enter their message by the placeholder or label.)

The react-testing-library has us covered again with a query method called `getByPlaceholderText`

```
// chat.test.jsimport React from 'react';import mock-io, {serverSocket, cleanUp } from 'socket.io-client';import {render, renderIntoDocument, within, cleanup} from 'react-testing-library';
```

```
import Chat from './chat';
```

```
afterEach(cleanup);
```

```
test('App should get messages', () => {  // ...})
```

```
test('App should tell when message is sent and delivered', () => {  // first render the app  const utils= renderIntoDocument(<Chat />)    // enter and send a message  utils.getByPlaceholderText('message').value = 'Hello';  utils.getByTestId('send-btn').click()})
```

So we introduced a couple of new APIs here. The first one is the `renderIntoDocument` method. We should fire real DOM events, not simulate them, in our test, as that more closely resembles how users use our app.

The drawback is that the `render` method creates and renders our app to an arbitrary DOM node, called `container`, on the fly. But React handles events via event delegation — attaching a single event for all event types on the `document`, and then delegating the event to the appropriate DOM node that triggered the event.

So, to fire real DOM events, we need to actually render our app into `document.body`. That’s what `renderIntoDocument` does for us.

Because we render into the document, we want to always make sure that the document is cleaned up after each test. You guessed right, the **cleanup** helper function does that for us.

In the test, after we enter the value, we click the send button to send our message. If you noticed, looking at the design, there is no send button. But if you pull out your Telegram or WhatsApp right now, you’ll notice that the send button only appears when you’ve actually entered some text in the message input. Our test has just accidentally covered that feature. :)

Now that we’ve clicked the send button, let’s make some assertions.

```
// chat.test.jsimport React from 'react';import mock-io, {serverSocket, cleanUp } from 'socket.io-client';import {render, renderIntoDocument, within, cleanup} from 'react-testing-library';
```

```
import Chat from './chat';
```

```
afterEach(cleanup);
```

```
test('App should get messages', () => {  // ...})
```

```
test('App should tell when message is sent/delivered', () => {  // first render the app  const utils = renderIntoDocument(<Chat />)    // enter and send a message  utils.getByPlaceholderText('message').value = 'Hello';  utils.getByTestId('send-btn').click();    // the message should appear on the message section  const messageSection = uitils.getByTestId('message-section');  expect(within(messageSection).getByText('Hello')).toBeTruthy();    // server tells us message is sent  serverSocket.emit('message-sent');
```

```
  // Now the UI should mark the message as sent  const message = within(messageSection).getByText('Hello');  expect(within(message).getByTestId('sentIcon')).toBeTruthy();
```

```
  // server tells us it's delivered  serverSocket.emit('message-delivered');
```

```
  // UI should mark the message as delivered  expect(within(message).getByTestId('deliveredIcon')).toBeTruthy();})
```

And that’s it. Just exactly as the user would expect, our test expects to see the sent/delivered icon appear next to the message when it’s sent/delivered.

So far, we’ve seen how easy testing a real-time socket.io-client app can be with the react-testing-library. No matter what you are testing, when you follow this approach, you gain more confidence that your app is working as it should. And what is more, we still have **zero idea** what the implementation of the app will look like. Just as the user, **our test just doesn’t care about the implementation!**

### Finishing up

Lastly, I’ll leave it to you to think about how to write the last two remaining tests on our list:

* App should tell when a friend comes online/goes offline
* App should tell when a friend is typing

Tip: You should have the server socket.io emit the event, then you assert what the UI will look like. Think about how **exactly** the user will know when a friend is typing, online, offline.

If you feel like I’ve done a nice job, and that others deserve a chance to see this, kindly applaud this article to help spread a better approach of testing real-time socket.io-client apps.

If you have a question that hasn’t been answered or feel differently about some of the points here, feel free to drop in some comments here or via [Twitter](https://twitter.com/Daajust).

You might also want to follow me here and/or on Twitter for more awesome articles coming up. And you might like to check out my previous articles:

* [Do you want a better understanding of Buffer in Node.js? Check this out](https://medium.freecodecamp.org/do-you-want-a-better-understanding-of-buffer-in-node-js-check-this-out-2e29de2968e8?source=user_profile---------2-------------------)
* [Functional setState is the future of React](https://medium.freecodecamp.org/functional-setstate-is-the-future-of-react-374f30401b6b)

