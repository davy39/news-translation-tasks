---
title: How to monitor network changes using Redux Saga in React Native
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-05T23:29:20.000Z'
originalURL: https://freecodecamp.org/news/how-to-monitor-network-changes-using-redux-saga-in-react-native-b7b95635ef65
coverImage: https://cdn-media-1.freecodecamp.org/images/0*l5MxcXOJgo-EZ-ht
tags:
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: React Native
  slug: react-native
- name: Redux
  slug: redux
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Pritish Vaidya

  Why should I use Redux Saga to monitor Network Changes?


  _Image Credit — [ImgFlip](https://i.imgflip.com/2knj8b.jpg" rel="noopener" target="blank"
  title=")

  Redux Saga is an alternate side effect model for redux apps. It is easier to...'
---

By Pritish Vaidya

#### Why should I use Redux Saga to monitor Network Changes?

![Image](https://cdn-media-1.freecodecamp.org/images/icYVSeaXDsfe83z7SkYSyKE-AKKWjQF7XOE5)
_Image Credit — [ImgFlip](https://i.imgflip.com/2knj8b.jpg" rel="noopener" target="_blank" title=")_

Redux Saga is an _alternate_ _side effect_ model for redux apps. It is easier to manage, execute, test and catch errors.

Rather than implementing the logic to manage the _network state_ in your react component, the `side-effects` should be handled separately. Redux Saga provides us with _eventChannel_ as an out of the box solution for handling such cases.

### What is an Event Channel?

![Image](https://www.freecodecamp.org/news/content/images/2021/06/1OSYcBjFfR0OqQ1JNH20hEvGHZ1Xrbzzv2em.jpeg)
_Image Credit — [Unsplash](https://images.unsplash.com/photo-1538131688925-7e0eb2e7828b)_

Redux Saga consists of `eventChannels` to communicate between _external events_ and _sagas_ as a factory function. The events are from the event sources _other than the redux store_.

Here’s a basic example from the [docs](https://github.com/redux-saga/redux-saga/blob/master/docs/advanced/Channels.md#using-the-eventchannel-factory-to-connect-to-external-events):

```js
import { eventChannel } from 'redux-saga'

function countdown(secs) {
  return eventChannel(emitter => {
      const iv = setInterval(() => {
        secs -= 1
        if (secs > 0) {
          emitter(secs)
        } else {
          // this causes the channel to close
          emitter(END)
        }
      }, 1000);
      return () => {
        clearInterval(iv)
      }
    }
  )
}
```

Things to note:

* The first argument of the `eventChannel` is a listener function.
* The return method is the _unregister listener_ function.

Emitter _initializes the listener once_ after which all the events from the listener are _passed to the emitter function_ by invoking it.

#### How should I hook up Redux Saga’s Event Channel with React Native’s Network(NetInfo) API?

The React Native’s **NetInfo** `[isConnected](https://facebook.github.io/react-native/docs/netinfo#isconnected)` API asynchronously fetches a _boolean_ which determines whether the device is `online` or `offline`.

#### Dive into the code

![Image](https://www.freecodecamp.org/news/content/images/2021/06/1MwK-maPG4EYywcUFOeyEAZTUxleIx8DSSM0.jpeg)
_Image Credit — [Unsplash](https://unsplash.com/photos/pgSkeh0yl8o)_

**First, we need to create a start channel method.**

```js
import { NetInfo } from "react-native"
import { eventChannel} from "redux-saga"

function * startChannel() {
  const channel = eventChannel(listener => {
    const handleConnectivityChange = (isConnected) => {
      listener(isConnected);
    }
    
// Initialise the connectivity listener
    NetInfo.isConnected.addEventListener("connectionChange", handleConnectivityChange);
    
// Return the unregister event listener.
    return () =>
      NetInfo.isConnected.removeEventListener("connectionChange",    handleConnectivityChange);
  });
}
```

The next step is to **listen for the event changes** within the channel.

```js
...

while (true) {
  const connectionInfo = yield take(channel);
}

...
```

The final step is to **pass a custom action** to the channel so that the _value can be synced using your action_.

```js
...
function * startChannel(syncActionName) {

...
while (true) {
  const connectionInfo = yield take(channel);
  yield put({type: syncActionName, status: connectionInfo });
}
```

This **channel** can be used in our default exported generator by using the [_call_](https://github.com/redux-saga/redux-saga/tree/master/docs/api#callfn-args) operation.

```js
export default function* netInfoSaga() {
  try {
    yield call(startChannel, 'CONNECTION_STATUS');
  } catch (e) {
    console.log(e);
  }
}
```

The _exported generator_ can then be _imported_ and used as a _detached task_ using [spawn/fork](https://github.com/redux-saga/redux-saga/tree/master/docs/api#spawnfn-args) operation in our main saga.

### Usage

The above code has added it as a package `react-native-network-status-saga` to include some of the more useful and cool parameters.

Here are the links

* [GitHub](https://github.com/pritishvaidya/react-native-network-status-saga)
* [npm](https://www.npmjs.com/package/react-native-network-status-saga)

_Thanks for reading._ _If you liked this article, show your support by clapping this article to share with other people on Medium._

_More of the cool stuff can be found on my [StackOverflow](https://stackoverflow.com/users/6606831/pritish-vaidya) and [GitHub](https://github.com/pritishvaidya) profiles._

_Follow me on [LinkedIn](https://www.linkedin.com/in/pritish-vaidya-506686128/), [Medium](https://medium.com/@pritishvaidya94), [Twitter](https://twitter.com/PritishVaidya) for further update new articles._

