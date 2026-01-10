---
title: Tips to Enhance the Performance of Your React App
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-08-27T13:46:33.000Z'
originalURL: https://freecodecamp.org/news/tips-to-enhance-the-performance-of-your-react-app
coverImage: https://www.freecodecamp.org/news/content/images/2019/08/react.jpg
tags:
- name: create-react-app
  slug: create-react-app
- name: React
  slug: react
- name: React context
  slug: react-context
- name: react testing library
  slug: react-testing-library
- name: Reactive Programming
  slug: reactive-programming
- name: React
  slug: reactjs
seo_title: null
seo_desc: 'By Shifa Martin

  ReactJS is an open-source framework that facilitates the development of UI interfaces
  for web and mobile applications. Developers globally use the framework to build
  state-of-the-art applications which subsequently generate revenues a...'
---

By Shifa Martin

ReactJS is an open-source framework that facilitates the development of UI interfaces for web and mobile applications. Developers globally use the framework to build state-of-the-art applications which subsequently generate revenues as well as expand the audience for businesses.  


However, building a great UI with React isn’t enough, You’ve got to add that extra glitter to make the app more polished, functional and remarkably better than the competition. 

This is exactly what I’m going to help you with as I describe some key methods to increase performance in React apps.

### 1. Making good use of Identities

When building mobile apps with React,  it is possible to wrap functions and variables with React.useMemo. Doing so provides the ability to memoize them so they remain identical for renders in the future.  


When functions and variables are not memoized, any references to them might vanish from future renders. Memoizing helps in negating wasteful processes and operations in every situation where you’d leverage functions and variables.

_**Example:**_ 

Say, we’re preparing a custom hook for a list of urls as arguments. Using the hook, we can collect them into an array of promise objects and resolve them with Promise.all. The results of this accumulation will enter the state and be passed the app component once done. The list of promises now map over the urls array from where it fetches the urls.

```react
import React from 'react'
import axios from 'axios'

export const useApp = ({ urls }) => {
  const [results, setResults] = React.useState(null)

  const promises = urls.map(axios.get)

  React.useEffect(() => {
    Promise.all(promises).then(setResults)
  }, [])

  return { results }
}

const App = () => {
  const urls = [
    'https://clinicaltables.nlm.nih.gov/api/icd10cm/v3/search?terms=a',
    'https://clinicaltables.nlm.nih.gov/api/icd10cm/v3/search?terms=b',
    'https://clinicaltables.nlm.nih.gov/api/icd10cm/v3/search?terms=c',
  ]

  useApp({ urls })

  return null
}

export default App

```

Since we want to obtain data from 3 urls here, only 3 requests are supposed to be sent out, one for each url. However,  when looking at it through the inspect element feature on Google Chrome, we find that 6 requests are sent instead of the supposed 3.   
This happens because the urls argument did not retain its previous identity. When the app is re-rendered, it’s instantiating a new array each time, as React treats it as a different value.  


![Image](https://lh5.googleusercontent.com/XE6rCdOL110eYARSgVTgcwiecF2qNAT96yBYn_-FbQ2_ffjdRAplLqRxu4eQh-NniyF0doEPRtsT3X0lYxeHcSu35UN0giiteCsIJTrVP9tw1mITk5-P5hH3PmdWd2ss5R0E2pb3)

To fix this problem, we can use React.useMemo as previously mentioned. When using React.useMemo, the array of promise objects won’t recompute in each new render unless the array with the list of urls changes. As long as it stays the same, the identities remain.

**Here’s what happens when applying React.useMemo to this example:**

```react
const useApp = ({ urls }) => {
  const [results, setResults] = React.useState(null)

  const promises = urls.map((url) => axios.get(url))

  React.useEffect(() => {
    Promise.all(promises).then(setResults)
  }, [])

  return { results }
}

const App = () => {
  const urls = React.useMemo(() => {
    return [
      'https://clinicaltables.nlm.nih.gov/api/icd10cm/v3/search?terms=a',
      'https://clinicaltables.nlm.nih.gov/api/icd10cm/v3/search?terms=b',
    ]
  }, [])

  const { results } = useApp({ urls })

  return null
}
```

It will send 6 requests even now since we’ve only memoized the urls array. The promises variables are also instantiating when running the hook. So in order to send only 3  requests, we also have to memorize the promises variables as well.

```react
const promises = React.useMemo(() => {
  return urls.map((url) => axios.get(url))
}, [urls])
```

> After memoizing both the urls array and the promises variables, this is what we get: 

![Image](https://lh4.googleusercontent.com/P-8qvsq_Nu229Eod2_FIlqLtY1_lAxkPXZfw3a9D7P25VIyGrw--kTnOuTF4rmXPsA3vxGRifwprsI_VGGDU9pFIafOAsfPKiQE3L3Zv1MHXzPH25e2g39MaCikn2AActzgJlftr)

### 2. Merging Props to Children

At times, developers get into situations where they prefer merging a prop with children before rendering. To facilitate the same, React allows viewing the props to all react elements including others, and also allows exposing their key.

So developers can choose to wrap the children element with a newer one, and insert new props there or they can simply merge the props with React.

Say, we have an app component that uses a useModal and offers the ability to manage modals by using controls such as open, close, opened and activated. Before merging props to children, we can pass them to a VisbilityControl component which provides some additional functionality.

```react
import React from 'react'

const UserContext = React.createContext({
  user: {
    firstName: 'Kelly',
    email: 'frogLover123@gmail.com',
  },
  activated: true,
})

const VisibilityControl = ({ children, opened, close }) => {
  const ctx = React.useContext(UserContext)
  return React.cloneElement(children, {
    opened: ctx.activated ? opened : false,
    onClick: close,
  })
}

export const useModal = ({ urls } = {}) => {
  const [opened, setOpened] = React.useState(false)
  const open = () => setOpened(true)
  const close = () => setOpened(false)

  return {
    opened,
    open,
    close,
  }
}

const App = ({ children }) => {
  const modal = useModal()

  return (
    <div>
      <button type="button" onClick={modal.opened ? modal.close : modal.open}>
        {modal.opened ? 'Close' : 'Open'} the Modal
      </button>
      <VisibilityControl {...modal}>{children}</VisibilityControl>
    </div>
  )
}

const Window = ({ opened }) => {
  if (!opened) return null
  return (
    <div style={{ border: '1px solid teal', padding: 12 }}>
      <h2>I am a window</h2>
    </div>
  )
}

export default () => (
  <App>
    <Window />
  </App>
)
```

Using Visibility control allows developers to ascertain whether the control activated is true before allowing the control opened to be used by children. In case the Visibility Control feature is used via a secret route, there’s an option to prevent unactivated users from accessing the content.  


### 3. Making a larger reducer

It is possible to combine to or more reducer to make a single, much larger reducer that can help boost a react app.

Say, you think of building a large app that provides access to a wide variety of small services. How would you go about the development of such an app? 

**There are two options:**

1. We can give each microservice within the app a separate part of its own from where its state and context can be managed directly.  


2. Or we can combine all states into a single large state and manage all of them within the same environment.  


> The first approach seems to highly tedious, so obviously, the second one is the way to go.  
> 

**Now we have three reducers to combine -** 

frogsreducer.js, authreducer.js and finally, ownersreducer.js.  


**Let's start with authReducer.js**

```react
const authReducer = (state, action) => {
  switch (action.type) {
    case 'set-authenticated':
      return { ...state, authenticated: action.authenticated }
    default:
      return state
  }
}

export default authReducer

ownersReducer.js
```

**ownersReducer.js**

```react
const ownersReducer = (state, action) => {
  switch (action.type) {
    case 'add-owner':
      return {
        ...state,
        profiles: [...state.profiles, action.owner],
      }
    case 'add-owner-id':
      return { ...state, ids: [...state.ids, action.id] }
    default:
      return state
  }
}

export default ownersReducer
```

**frogsReducer.js**

```react
const frogsReducer = (state, action) => {
  switch (action.type) {
    case 'add-frog':
      return {
        ...state,
        profiles: [...state.profiles, action.frog],
      }
    case 'add-frog-id':
      return { ...state, ids: [...state.ids, action.id] }
    default:
      return state
  }
}

export default frogsReducer
```

> Now we can put all three into the main app file and define their state:  
> 

**App.js**

```react
import React from 'react'
import authReducer from './authReducer'
import ownersReducer from './ownersReducer'
import frogsReducer from './frogsReducer'

const initialState = {
  auth: {
    authenticated: false,
  },
  owners: {
    profiles: [],
    ids: [],
  },
  frogs: {
    profiles: [],
    ids: [],
  },
}

function rootReducer(state, action) {
  return {
    auth: authReducer(state.auth, action),
    owners: ownersReducer(state.owners, action),
    frogs: frogsReducer(state.frogs, action),
  }
}

const useApp = () => {
  const [state, dispatch] = React.useReducer(rootReducer, initialState)

  const addFrog = (frog) => {
    dispatch({ type: 'add-frog', frog })
    dispatch({ type: 'add-frog-id', id: frog.id })
  }

  const addOwner = (owner) => {
    dispatch({ type: 'add-owner', owner })
    dispatch({ type: 'add-owner-id', id: owner.id })
  }

  React.useEffect(() => {
    console.log(state)
  }, [state])

  return {
    ...state,
    addFrog,
    addOwner,
  }
}

const App = () => {
  const { addFrog, addOwner } = useApp()

  const onAddFrog = () => {
    addFrog({
      name: 'giant_frog123',
      id: 'jakn39eaz01',
    })
  }

  const onAddOwner = () => {
    addOwner({
      name: 'bob_the_frog_lover',
      id: 'oaopskd2103z',
    })
  }

  return (
    <>
      <div>
        <button type="button" onClick={onAddFrog}>
          add frog
        </button>
        <button type="button" onClick={onAddOwner}>
          add owner
        </button>
      </div>
    </>
  )
}
export default () => <App />

This is what it looks like combining all three reducers into one large reducer, along with rootReducer

function rootReducer(state, action) {
  return {
    auth: authReducer(state.auth, action),
    owners: ownersReducer(state.owners, action),
    frogs: frogsReducer(state.frogs, action),
  }
```

This is what it looks like combining all three reducers into one large reducer, along with rootReducer.

### Using Sentry for Analyzing Errors

![Image](https://lh5.googleusercontent.com/ySh7MjcCdU2XUVc1GASq8HBz0ym9Yn3mQt8xP0fygcYWqf-UoSkOAV1gOxUSgOQ3o79FJb7R3P9iwIYngWY8MtNB6uAqHBh-UXY5gf_G-C9kN_Nuxx73iYllkPSqKKOSjDTXWvmb)

Any mobile app development project can benefit greatly from [Sentry.](https://sentry.io/welcome/) It provides everything a developer needs to handle errors and exceptions when building apps with React. Sentry identifies all errors and displays them at one central location so they can be accessed and analyzed all at once.

Getting started with Sentry on React is easy. Just use npm install @sentry/browser and set it up. Once done, developers can log in at sentry.io and analyze all error reports of a project on a single dashboard.

The error reports from sentry are incredibly detailed. They provide all sorts of important information which include the user’s device information, browser, URL, stack trace, how the error was handled, source code, IP address, breadcrumbs to trace the source of error, the error function name and much more.  


### 5. Using Axios for HTTP requests

Though [Axios](https://github.com/axios/axios) is commonly used for HTTP requests. I felt it is important to mention this point because it's actually not common for developers to use other request libraries such as fetch for React apps.  


Windows.fetch provides no support for Internet Explorer 11 (most don’t really care though). But for what it's worth, Axios does work there as well and offers the ability to cancel requests in mid-flight.  


### Final Words

The 5 mentioned methods can greatly help speed up your React app. It helps developers, the business you’re in and of course, those who’d be using it eventually. But honestly, the success of your React App mostly depends on those who work on them. 

As a consumer, you’d want better performance from your app, so it is what denotes success. As a developer, these methods could make your app easier to develop, and efficiency is key to being more productive. 

**ValueCoders is an expert [IT outsourcing company](https://www.valuecoders.com/) for software development. If you are looking for offshore React programmers or [hire Android developers](https://www.valuecoders.com/hire-developers/hire-android-developers), feel free to get in touch.** 

Also, I hope this post helps you learn new things and get a deeper insight into what goes into making the perfect react application. 

  

