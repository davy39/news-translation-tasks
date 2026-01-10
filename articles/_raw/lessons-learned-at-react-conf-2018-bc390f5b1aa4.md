---
title: Lessons Learned at React Conf 2018
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-14T16:29:01.000Z'
originalURL: https://freecodecamp.org/news/lessons-learned-at-react-conf-2018-bc390f5b1aa4
coverImage: https://cdn-media-1.freecodecamp.org/images/1*XxPm9SJhbJ_NHMdFRhbxeA.jpeg
tags:
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: startup
  slug: startup
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Yangshun Tay

  I was fortunate to have attended React Conf 2018 thanks to my managers — it was
  an awesome event. I have been watching past React Conf videos online and it was
  exciting to be able to attend the event and listen to some of the best peo...'
---

By Yangshun Tay

I was fortunate to have attended React Conf 2018 thanks to my managers — it was an awesome event. I have been watching past React Conf videos online and it was exciting to be able to attend the event and listen to some of the best people in the industry live!

React Conf is a two-day event with over 20 speakers on stage. Here’s a summary of the highlights, so that people who weren’t able to attend would learn from my experience and quickly decide if it’s worth their time to watch the full video, which can be found on [YouTube](https://www.youtube.com/watch?v=V-QO-KO90iQ&list=PLPxbbTqCLbGE5AihOSExAa4wUM-P42EIJ).

#### Add State to Functional Components and Reuse Lifecycle Logic with React Hooks

The conference kicked off with a keynote from Sophie Alpert, Engineering Manager of the React Team at Facebook (at that point in time) and Dan Abramov, core team member of React and creator of Redux. Sophie started the presentation with an interesting trivia that on Google trends, React is also more popular than renewable energy and orange juice!

She then reiterated that since React started in 2013, its mission was to make it easier to build great user interfaces. React tries to simplify things which are hard to do, such as simplifying component’s async data dependencies with suspense and better rendering performance with time slicing, which makes sure that React processes the most important renders in your app first.

Another thing that React does well is to have great developer experience and tooling while you develop and debug your app via the React Devtools extension, which recently added a profiler feature to help developers understand what is happening in the app.

Some things in React were still not ideal — reusing logic between multiple components has traditionally been done using Higher Order Components and render props. They solve the problem but it comes with a disadvantage to developers who have to restructure code. This could lead to Wrapper hell and makes data flow through the app hard to follow.

The second issue is that in giant components, the logic can sometimes be tangled and split across various life-cycle methods, such as subscribing to a store in `componentDidMount` and unsubscribing in `componentWillUnmount`.

Splitting up logic tends to lead to situations where you forget to clean up after mounting which could cause memory leaks. The last issue is classes. Function components often have to be converted to classes to use state and life-cycle methods and boilerplate would have to be added to support them. Usage of `this` and binding callbacks can also be confusing.

The React team has a proposal to the above three issues — React Hooks.

Dan Abramov then took the stage! React uses a Request for Comments, RFC, process whenever somebody wants to make substantial additions or changes to React and a proposal would have to be written, detailing the motivation and design of the change. The proposal for React Hooks can be found [here](https://github.com/reactjs/rfcs/pull/68). It should be noted that Hooks do not contain any breaking changes or deprecation and its usage is opt-in.

Dan gave a demo of how to convert a typical class component with state to use functional components using a few new React Hook APIs — `useState`, `useEffect` and `useContext` and the benefits are obvious. We are able to co-locate life-cycle logic within a `useEffect` hook and can reuse them across components. This sparked a movement of the community creating npm packages of useful hooks and they can be found [here](https://github.com/rehooks/awesome-react-hooks).

Using Hooks come with a [few caveats](https://reactjs.org/docs/hooks-rules.html) — you cannot call hooks within a conditions, they have to be at the top level of your functional component and there’s a linter plugin which warns you if you are not using hooks correctly.

This is because React relies on the order of execution of hooks to match the state values with the hooks. You can only use hooks within functional components or other custom hooks (which by convention should start with `use`).

Facebook has been using hooks in production for about four months now so behavior is relatively stable. Hooks can coexist with your existing code and you can start using them today and gradually migrate your non-hooks code to use hooks.

Ryan Florence, creator of React Router then gave a demo on how to refactor some real world use cases to use hooks. Ryan first talked about how render props give components a false sense of hierarchy in situations like a `<Med`ia> component that is used for querying responsive screen sizes then refactored a component usin`g two &`lt;Media> components with render pr`ops usin`g a useMedia hook he created on-the-spot.

The next demo was about refactoring/creating an accessible carousel with all the essential features — a play/stop button, forward/back button and a progress bar.

The `useEffect` hook was introduced in greater detail here and how they can be run only when certain state/props have changed, things you'd do in `componentDidUpdate`. `useEffect` can be used to achieve the same things as what you need `componentDidMount`, `componentDidUpdate` and `componentWillUnmount` for.

Lastly, Ryan also demonstrated how you could take a Flux/Redux-like uni-directional data approach in your app by using the `useReducer` hook. The `useReducer` hooks returns two variables, `state` and `dispatch`.

Like in Redux, the reduce function you provide to `useReducer` will take in the current state and an action as parameters and produce a new state depending on the action passed in.

I recommend that you check out his entertaining and enlightening video demo. The code for his live demo can also be found in his [GitHub repo](https://github.com/ryanflorence/react-conf-2018).

P.S. I also learnt that changing keys of a components reset its state, because changing keys will unmount and remount a component. Pretty handy tip!

#### Video Links

* [React Today and Tomorrow — Sophie Alpert & Dan Abramov](https://www.youtube.com/watch?v=V-QO-KO90iQ&list=PLPxbbTqCLbGE5AihOSExAa4wUM-P42EIJ)
* [90% Cleaner React using Hooks — Ryan Florence](https://www.youtube.com/watch?v=wXLf18DsV-I&index=2&list=PLPxbbTqCLbGE5AihOSExAa4wUM-P42EIJ)

#### Improve User Experience and Developer Happiness with Concurrent Rendering in React

Day 2 of the conference was kicked off by Andrew Clark and Brian Vaughn. When developing, it’s not unusual to degrade user experience in the process of making our app faster. Andrew gives an [example of Ads Manager](https://twitter.com/acdlite/status/991503599246098432) as one of such apps, because of the sheer number of spinners in the creation flow as a result of codesplitting of components or data fetching. These spinners also show up only for a split second because the data does not take long to load on a fast network.

Over the past year, the React team has been working on concurrent React, which aims to make it easy for developers to build high-performance apps by default with smooth non-janky user experience.

Concurrent React (previously called Async React) allows React to work on multiple things at once and switch between them according to their priority. Today, React still works synchronously. If a component requires a long time to update, the main thread will be blocked and the browser cannot respond to user inputs until the work is complete. With concurrent React, that work can be paused, and the main thread can respond to the user input, then resume work. This is also referred to as time slicing, the ability to split work into chunks and spread its execution over time.

Andrew then uses an app comprising of three tabs as an example. With `React.lazy`, it's easy to code split the app and load the component within each tab only when it's being rendered. React also comes with a `<Suspen`se> component to allow developers to render fallbacks when the component code isn't loaded yet.

These components can be placed anywhere in the component tree and if any part of the tree hasn't been loaded, the fallback of the nearest `<Suspen`se>component will be used. The above features work in synchronous mode and don't require any concurrent React features. One problem mentioned earlier is that if a resource loads fast, there's a flashing spinner. With concurrent React, these unnecessary flashing spinners can be avoided as you can configure the threshold that you are willing to wait before showing the fallback spinner.

One last thing Andrew showed was how easy it was to pre-load and pre-render the content in the other tabs during the idle time that the user spends reading the contents of the first tab after its loaded. Simply pass a `hidden` props to a HTML element and React will deprioritize all of its children to off-screen priority and only load them when there's nothing else to do on the page. When navigating to the other tabs, they appear instantly, because they have already been loaded during the idle time.

Brian Vaughn then demonstrated a new profiling tool built into the React Devtool (it’s already in your browser) and a new profiling API. The profile works in a similar way to the Chrome performance profile, you record some interactions and can view the rendering duration and flame graphs of which components were rendered.

This helps with debugging unnecessary re-renders and detecting components with slow renders. Performance information can also be attributed to events in the code by using the experimental scheduler’s trace API. Note that this API is not yet finalized, so use with caution. Find out more about React’s new interaction tracing feature [here](http://fb.me/react-interaction-tracing).

Jared Palmer, lead engineer at Palmer HQ, gave a demo on how he improved the user experience of his Spotify-clone (aptly name Suspensify) by using the new concurrent React features. React cache can not only be used to cache API response data, it can also be used to cache assets such as images, audio files, and scripts.

Jared showed how he leveraged on the `unstable_createResource` API and `<Suspense` /> to show a low resolution placeholder artist profile photo image as a placeholder while the higher resolution image is being downloaded in the background then displaying the higher resolution image after it's done downloading. Data loaded usin`g the unstable_createRe`source API also reads more easily because developers no longer have to explicitly handle and write code for loading states. Suspense brings the benefits of coordinating and loading states easily.

Lastly, it should be noted that code using `<Suspense` /> still works without concurrent React; the user experience wins are fewer but the developer experience wins remain.

#### Video Links

* [Concurrent Rendering in React — Andrew Clark and Brian Vaughn](https://www.youtube.com/watch?v=ByBPyMBTzM0&list=PLPxbbTqCLbGE5AihOSExAa4wUM-P42EIJ&index=15)
* [Moving To React Suspense — Jared Palmer](https://www.youtube.com/watch?v=SCQgE4mTnjU&list=PLPxbbTqCLbGE5AihOSExAa4wUM-P42EIJ&index=16)

#### React Native has problems but a solution is in the works

React Native is Facebook’s framework for building native mobile apps using JavaScript and React. James Long, creator of Prettier, talks about what sucks about React Native, in particular, animations. In his experience, when writing React Native code related to responding to user interactions and animations, the user experience is horrible because of laggy animations.

The reason is because user interactions are handled on the native thread but the interaction effects are processed by the JavaScript thread over an async bridge. One solution to this problem is to use the [React Native Gesture Handler](https://kmagiera.github.io/react-native-gesture-handler/) library, which provides a declarative API exposing the platform native touch and gesture system to React Native. For even more complicated interactions and animations, `[react-native-reanimated](https://github.com/kmagiera/react-native-reanimated)` (by the same author of React Native Gesture Handler) could be used to represent logic where declarative APIs cannot.

In the worst case scenario, developers could go even lower level and write native language code and APIs. In conclusion, block the main thread when dealing with animations and avoid Async where possible. Declarative APIs are great for many use cases, but imperative APIs would be useful as an escape hatch for complex use cases.

Parashuram, a Facebook engineer on the React Native team goes through a brief overview of React Native’s current architecture and problems with the current React Native, which is a reiteration of James’ point about interactions on React Native not giving quick responses to user interactions which people are used to in purely native applications and on the web because of the async bridge between native thread and the JavaScript thread.

The React Native team’s solution to this issue is a new interface for communicating between JavaScript and native land, called the JavaScript Interface (JSI). It’s basically a simple way for JavaScript to talk to Objective-C or Java (or any native language).

The JavaScript side gets access to a host object very similar to the HTML elements (on React Web) and then you can call can access methods and properties on it.

You can also use JSI to get native modules which returns a host object and you can call methods on them, similar to RPC calls. Another change that I’m looking forward to, is that React Native might be shifting some of the view manager and native modules outside of the core library into the community, which makes React Native more lightweight and makes upgrading it easy as long as you don’t depend on the external modules. Facebook uses React Native internally, as well as other big companies like Microsoft, Pinterest and Zynga.

Hence, Facebook is committed to improving React Native and moving forward with the community.

#### Video Links

* [Go Ahead, Block the Main Thread — James Long](https://www.youtube.com/watch?v=ZXqyaslyXUw&index=24&list=PLPxbbTqCLbGE5AihOSExAa4wUM-P42EIJ)
* [React Native’s New Architecture — Parashuram N](https://www.youtube.com/watch?v=UcqRXTriUVI&index=25&list=PLPxbbTqCLbGE5AihOSExAa4wUM-P42EIJ)

#### You can use (the best features of) GraphQL without GraphQL

Conor Hastings, an engineer at Netflix, went through the design principles of GraphQL and explains why GraphQL is appealing to engineers. He gave a good analogy of how traditional REST is akin to ordering pizza without being able to choose the toppings and ending up with 40 toppings vs using GraphQL where you are able to pick just the toppings you want — this eliminates the problem of over-fetching data. Other benefits of GraphQL include fetching hierarchical data with just one round trip and GraphQL’s awesome developer tooling (GraphiQL).

Not all software have a need for GraphQL.

It’s probably not worth your time to create a full GraphQL API if your application doesn’t need to be maintained, your users have high speed internet. However, you can still use parts of GraphQL in your app and leverage on some of the good parts of GraphQL — namely, the powerful query system that makes it easy to shape the data to meet the needs of your UI.

Conor then introduces [RouteQL](https://github.com/conorhastings/routeql), a library he built that aims to use tools from graphql-js (the GraphQL parser on the client) and other popular libraries from the GraphQL-ecosystem so that you can write GraphQL queries in the browser that talks to any back-end. By making some sacrifices and giving up some of the benefits of GraphQL, we can still leverage on the power of GraphQL without using GraphQL. GraphQL is a great fit for server-data driven apps without much client state.

#### Video Links

* [GraphQL without GraphQL — Conor Hastings](https://www.youtube.com/watch?v=YSEUAi1dAdk&list=PLPxbbTqCLbGE5AihOSExAa4wUM-P42EIJ&index=10)

#### React Helps Make User Interfaces Fancy

Matt Perry goes through how animation is achieved using existing imperative-style animation libraries such as [animated](https://github.com/animatedjs/animated) and [Popmotion](https://github.com/Popmotion/popmotion) and their shortcomings. We can simplify imperative APIs into declarative ones by identifying patterns from the imperative logic that we write. As a solution to the problem mentioned, Matt introduces his animation library [Pose](https://popmotion.io/pose/) which uses a declarative CSS-like approach for animating which makes writing common animations really simple.

In another talk by Elizabet Oliveira (or Miuki Miu on the web), she talks about what is SVG, the benefits of SVGs, the various ways we can use them on the web and in React. When SVG illustrations need to be animated and customizable, writing them as composable components with props is especially beneficial.

[React-kawaii](https://github.com/miukimiu/react-kawaii), is a library of cute illustrations built by Elizabet that are easily customisable. You can change the size, color, mood (contents) of complex SVG illustrations just by changing the props. Check out the [demo](https://react-kawaii.now.sh/) on its website.

#### Video Links

* [The Path To A Declaratively Animated Future — Matt Perry](https://www.youtube.com/watch?v=1e07uPWpvzI&list=PLPxbbTqCLbGE5AihOSExAa4wUM-P42EIJ&index=4)
* [SVG illustrations as React Components — Elizabet Oliveira](https://www.youtube.com/watch?v=1gG8rtm-rq4&list=PLPxbbTqCLbGE5AihOSExAa4wUM-P42EIJ&index=17)

#### What’s New in Create React App 2

Create React App (CRA) is a starter project which makes it easy to bootstrap new React apps or if you want to try out React. Joe Haddad, a maintainer of CRA introduced what’s new in CRA 2: PostCSS support, [Babel Macros](https://github.com/kentcdodds/babel-plugin-macros), Sass and CSS modules, TypeScript support. Read more on the [React blog](https://reactjs.org/blog/2018/10/01/create-react-app-v2.html).

#### Video Links

* [What’s New in Create React App — Joe Haddad](https://www.youtube.com/watch?v=He-m9gd6WyM&index=5&list=PLPxbbTqCLbGE5AihOSExAa4wUM-P42EIJ)

#### The Web is Great for Making Complex User Interfaces

GDevelop is a game editor built many years ago by Florian Rival, engineer at Facebook. He went through his journey on how he modernized the editor (originally written in C++) to the web by leveraging on React, Electron and WebAssembly. Florian used emscripten, which compiled his native bytecode to WebAssembly format and rewrote the UI in React leveraging on React’s vast ecosystem of component libraries and tooling. Florian heavily optimized the performance using virtualization, the new React profiler and `shouldComponentUpdate`. Game editors are extremely complex applications and it's impressive that Florian was able to port his native app into Electron in a year with the help of React and the other tools in the open source ecosystem.

#### Video Links

* [React, JavaScript and WebAssembly to port legacy native apps — Florian Rival](https://www.youtube.com/watch?v=6La7jSCnYyk&list=PLPxbbTqCLbGE5AihOSExAa4wUM-P42EIJ&index=13)

#### Final Thoughts

I initially found it weird that the React Hooks returned values in arrays to be destructured, but gradually got used to it after using it at work for over a month now. Besides the benefits of hooks mentioned above, there is another big win of build size [going](https://twitter.com/sebmck/status/1055695821641924609) [down](https://twitter.com/jamiebuilds/status/1056015484364087297) because a lot of class methods are removed. State variables, because they are just local variables within a component, and now be minified too.

Hooks are great, but they don’t come without drawbacks.

* `useEffect` run on every render. If we set state within the `useEffect` callbacks, we could cause infinite loops. An example can be detailing the pitfall can be found in this [Stack Overflow question I wrote here](https://stackoverflow.com/q/53243203/1751946). It is recommended that developers read the `useEffect` API carefully and understand it well before using it.
* The closures (or code within) `useEffect` and `useCallback` could be referencing outdated `state` and `props`. I also wrote about this pitfall in [this Stack Overflow question](https://stackoverflow.com/q/53024496/1751946). If you are unsure whether you are referencing old values, the state hook updater also has a [callback form](https://reactjs.org/docs/hooks-reference.html#functional-updates) where you can access the previous state value.

More drawbacks can be found in the RFC [here](https://github.com/reactjs/rfcs/blob/master/text/0068-react-hooks.md#drawbacks).

I’ve been using hooks at work and we implemented a small form input abstraction that helps to validate and track changed/dirty states of a form. My team likes it so far!

I haven’t got to play around with concurrent React, but from the demos, using it in production code seems so frictionless and easy. I believe concurrent React, Suspense and the profiler features are highly relevant to improving user experience and developer happiness.

Looking forward to more React goodness in the upcoming versions of React! ?

_If you enjoyed this article, please don’t forget to leave a ? . (Do you know that you can clap more than once? Try it and see for yourself!)_

You can also follow me on [GitHub](https://github.com/yangshun) and [Twitter](https://twitter.com/yangshunz).

