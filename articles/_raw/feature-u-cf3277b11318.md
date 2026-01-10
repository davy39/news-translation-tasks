---
title: feature-u (Feature Based Project Organization for React)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-12T06:38:54.000Z'
originalURL: https://freecodecamp.org/news/feature-u-cf3277b11318
coverImage: https://cdn-media-1.freecodecamp.org/images/1*D9PDIbwiUfWLB8zd7xPawQ.jpeg
tags:
- name: features
  slug: features
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: Redux
  slug: redux
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Kevin Bridges

  This article is an introduction to feature-u — a library that facilitates feature-based
  project organization in your react project. This utility assists in organizing your
  project by individual features.

  Most developers would agree t...'
---

By Kevin Bridges

This article is an introduction to [feature-u](https://feature-u.js.org/) — a library that facilitates **feature-based project organization** in your [react](https://reactjs.org/) project. This utility assists in organizing your project by individual features.

Most developers would agree that organizing your project by features is much preferred over type-based patterns. Because **application domains grow** in the real world, project **organization by type** simply doesn’t scale, it just becomes unmanageable!

There are many good articles on this topic with insights on feature-based design and structure (see: [References](#15dd) below).

This article outlines my excursion into feature-based composition. In working through the details, I realized there was an opportunity for a library to help manage and streamline some of the hurdles incurred in this process. The result: **feature-u** (check out the [full docs](https://feature-u.js.org/), [GitHub source](https://github.com/KevinAst/feature-u), and [NPM package](https://www.npmjs.com/package/feature-u)).

> **_Update_**: On 8/14/2018 [feature-u V1](https://feature-u.js.org/1.0.0/history.html#v1_0_0) was released, that re-designed Cross [Feature Communication `new`](https://feature-u.js.org/1.0.0/crossCommunication.html) to include [UI Composition `new`](https://feature-u.js.org/1.0.0/crossCommunication.html#ui-composition) as a core offering. **A new article can be found [here](http://bit.ly/feature-u-V1)** that takes a comprehensive approach in introducing you to all of **feature-u** (including **V1**). We are very excited about this update, because it **_promotes one solution for all feature collaboration_**! While upgrading to V1 requires some client code mods (see [V1 Migration Notes](https://feature-u.js.org/1.0.0/migration.1.0.0.html)), it is well worth it. This article is based on [feature-u V0](https://feature-u.js.org/0.1.3/history.html#v0_1_3), and is using some antiquated APIs (mostly `Feature.publicFace`, and the `app` object). Still, this is a good resource to get your feet wet with feature-u.

#### **_At a Glance_**

[Backdrop](#e4bb) — why feature-u was created

[feature-u Basics](#b996) — introduce high-level feature-u concepts

[eatery-nod App](#077e) — the sample app used to demonstrate feature-u

[Before & After](#688e) — **eatery-nod** project structure before and after features

[feature-u In Action](#ecd3) — explore feature-u aspects through concrete examples

[feature-u Benefits](#3ef6) — in summary

[References](#15dd) — feature-based articles

### [Backdrop](#e80d)

Let’s start by chronicling my journey in this process

#### **out of the Starting Gate …**

_Sooo … I had decided to restructure my project by features_. From a design perspective, there were a number of considerations in determining the feature boundaries. I had read all the articles, and applied my design to a **new feature-based directory structure.**

In general, I was feeling good about my progress. I was starting to see concrete benefits … **feature segregation was going to result in code that is much more manageable!**

#### **the Hurdles …**

However, there were a number of hurdles yet to be resolved …

How can I encapsulate and isolate my features, while still allowing them to collaborate with one another?

How can selected features introduce start-up initialization (even injecting utility at the root DOM), without relying on some external startup process?

How can I promote feature-based UI components in an isolated and autonomous way?

How can I configure my chosen frameworks now that my code is so spread out?

How can I enable/disable selected features which are either optional, or require a license upgrade?

In short, how can I pull it all together so that my individual features operate as one application?

#### **the Goal _(what now?)_**

The **overriding goal** of feature-u is two-fold:

1. Allow features to **Plug-and-Play!** This encompasses many things, such as: encapsulation, cross communication, enablement, initialization, and so on. We will build on these concepts throughout this article.
2. **Automate the startup of your application!!** You have the features. Allow them to promote their characteristics, so a central utility can **automatically** configure the frameworks used in your app, thereby launching your application. This task must be accomplished in an extendable way, because not everyone uses the same set of frameworks.

### [feature-u Basics](#e80d)

The basic process of **feature-u** is that each feature promotes a [Feature](https://feature-u.js.org/0.1.3/api.html#Feature) object that contains various aspects of that feature — things like the feature's name, its Public API, whether it is enabled, initialization constructs, and resources used to configure its slice of the frameworks in use.

In turn, these Feature objects are supplied to [launchApp()](https://feature-u.js.org/0.1.3/api.html#launchApp), which configures and starts your application running. In addition, the returned [App](https://feature-u.js.org/0.1.3/api.html#App) object is exported, in order to promote the public API of each feature.

#### aspects

In feature-u, “aspect” is a generalized term used to refer to the various ingredients that (when combined) constitute your application.

Aspects can take on many different forms:

* UI Components and Routes
* State Management (actions, reducers, selectors)
* Business Logic
* Startup Initialization Code
* And so on…

Not all aspects are of interest to feature-u — only those that are needed to setup and launch the app — all others are considered an internal implementation detail of the feature.

As an example, consider the redux state manager. While it uses actions, reducers, and selectors … only reducers are needed to setup and configure redux.

#### framework integration

A fundamental goal of feature-u is to **automatically configure the framework**(s) used in your run-time-stack (by accumulating the necessary resources across all your features). Because not everyone uses the same frameworks, feature-u accomplishes this through **Extendable Aspects** (you can find them in external NPM packages, or you can create your own).

It is important to understand that the interface to your chosen frameworks is not altered in any way. You use them the same way you always have (just within your feature boundary).

feature-u merely provides a well defined organizational layer, where the frameworks are automatically setup and configured by accumulating the necessary resources across all your features.

### [eatery-nod App](#e80d)

[**eatery-nod**](https://github.com/KevinAst/eatery-nod/tree/after-features) is the application where feature-u was conceived. It is a [react-native](https://facebook.github.io/react-native/) [expo](https://expo.io/) mobile app, and is one of my sandbox applications that I use to test frameworks. I like to develop apps that I can use, but have enough real-world requirements to make it interesting.

eatery-nod randomly selects a “date night” restaurant from a pool of favorites. My wife and I have a steady “date night”, and we are always indecisive on which of our favorite restaurants to frequent :-) So eatery-nod provides the spinning wheel!

Take a look at the eatery-nod [README](https://github.com/KevinAst/eatery-nod/blob/after-features/README.md) to get a feel for the application. Screen flows are available, so it really helps in your orientation to the project.

![Image](https://cdn-media-1.freecodecamp.org/images/1*DDrt1xRlOmM8jywM4ABSCg.png)
_**eatery-nod’s** primary screen flow_

In addition, [README files](https://github.com/KevinAst/eatery-nod/blob/after-features/src/feature/README.md) are found in each feature, describing what each feature accomplishes. Take some time now and skim through these resources:

* [**device**](https://github.com/KevinAst/eatery-nod/blob/after-features/src/feature/device/README.md) — initializes the device for use by the app, and promotes a device API abstraction
* [**auth**](https://github.com/KevinAst/eatery-nod/blob/after-features/src/feature/auth/README.md) — promotes complete user authentication
* [**leftNav**](https://github.com/KevinAst/eatery-nod/blob/after-features/src/feature/leftNav/README.md) — promotes the app-specific Drawer/SideBar on the app’s left side
* [**currentView**](https://github.com/KevinAst/eatery-nod/blob/after-features/src/feature/currentView/README.md) — maintains the currentView with get/set cross-feature communication bindings
* [**eateries**](https://github.com/KevinAst/eatery-nod/blob/after-features/src/feature/eateries/README.md) — manages and promotes the eateries view
* [**discovery**](https://github.com/KevinAst/eatery-nod/blob/after-features/src/feature/discovery/README.md) — manages and promotes the discovery view
* [**firebase**](https://github.com/KevinAst/eatery-nod/blob/after-features/src/feature/firebase/README.md) — initializes the Google Firebase service
* [**logActions**](https://github.com/KevinAst/eatery-nod/blob/after-features/src/feature/logActions/README.md) — logs all dispatched actions and resulting state
* [**sandbox**](https://github.com/KevinAst/eatery-nod/blob/after-features/src/feature/sandbox/README.md) — promotes a variety of interactive tests, used in development, that can easily be disabled

### [Before & After](#e80d)

Anyone who knows me will tell you that I have an appreciation for a good before/after analysis. Whether it is a home remodel or a software refactor, it helps to chronicle where you have been, so as to quantify concrete achievements, and gives you a sense of accomplishment.

![Image](https://cdn-media-1.freecodecamp.org/images/0*dIpbZMgqHN5DrE6S.jpg)

Let’s take a look at eatery-nod’s directory structure (before/after).

For illustration purposes, I have only expanded a few directories, but I think you get the idea.

**Before**: here is my project's [before features](https://github.com/KevinAst/eatery-nod/tree/before-features/src) …

```
eatery-nod src BEFORE featuressrc/├──actions/        ... redux actions│     auth.js│     discovery.js│     eateries.js│     ... snip snip├──api/            ... various abstract APIs│     device.js│     discovery.js│     ... snip snip├──app/            ... mainline startup **1**│  │  ScreenRouter.js│  │  SideBar.js│  │  index.js│  └──startup/│     │  createAppStore.js│     │  platformSetup.android.js│     │  platformSetup.ios.js│     └──firebase/│           firebaseAppConfig.js│           initFireBase.js├──appState/       ... redux reducers│     auth.js│     discovery.js│     eateries.js│     ... snip snip├──comp/           ... UI Component Screens│     DiscoveryListScreen.js│     EateriesListScreen.js│     ... snip snip├──logic/          ... redux-logic modules│     auth.js│     discovery.js│     eateries.js│     ... snip snip└──util/           ... common utilities
```

**After**: and here is the same project's [after features](https://github.com/KevinAst/eatery-nod/tree/after-features/src) …

```
eatery-nod src AFTER featuressrc/│  app.js          ... launches app via launchApp() **2**├──feature/│  │  index.js     ... accumulate/promote all app Feature objects│  ├──auth/        ... the app's authorization feature│  │  │  actions.js│  │  │  featureName.js│  │  │  index.js│  │  │  logic.js│  │  │  publicFace.js│  │  │  route.js│  │  │  signInFormMeta.js│  │  │  state.js│  │  └──comp/│  │        SignInScreen.js│  │        SignInVerifyScreen.js│  ├──currentView/ ... other features│  ├──device/      ... feature to initialize the device│  │  │  actions.js│  │  │  api.js│  │  │  appDidStart.js│  │  │  appWillStart.js│  │  │  featureName.js│  │  │  index.js│  │  │  logic.js│  │  │  publicFace.js│  │  │  route.js│  │  │  state.js│  │  └──init/│  │        platformSetup.android.js│  │        platformSetup.ios.js│  ├──discovery/   ... more features│  ├──eateries/│  ├──firebase/│  ├──leftNav/│  ├──logActions/│  └──sandbox/└──util/           ... common utilities used across all features
```

As expected, the difference in project organization is dramatic!

* **Before features —** you find constructs for a given feature spread over numerous typed directories.
* **After features**: all aspects of a given feature are contained in its own isolated directory.
* A notable difference is the **dramatic reduction in complexity of the application startup process!** The “before features” contained an entire `app\` directory of startup code (see `[**1**](#226c)` above), while the "after features" simply contains a single `app.js` startup file (see `[**2**](#f98f)` above). **Where did all the complexity go?** ... stay tuned!

### [feature-u In Action](#e80d)

To better understand feature-u, let’s take a closer look at some eatery-nod examples in action.

![Image](https://cdn-media-1.freecodecamp.org/images/0*1OHVaxVpTBYvW_ZT.jpg)

Each of the following sections briefly introduce a new feature-u topic, correlating sample code from eatery-nod. Additional information is provided through links, both to the feature-u docs, and eatery-nod source code. In some cases the in-lined sample code has been streamlined (to emphasize a focal point), however the caption link will take you to the actual code (hosted on GitHub).

Here are our topics …

1. [Simplified App Startup](#5974)
2. [React Platforms](#af00)
3. [Feature Object](#6db0)
4. [Feature Initialization](#c1a5)
5. [Feature Collaboration](#1895)
6. [Framework Integration](#cfeb)
7. [Feature Enablement](#e557)
8. [Managed Code Expansion](#5fab)
9. [UI Component Promotion](#2666)
10. [Single Source of Truth](#c174)

### [1. Simplified App Startup](#6561)

After breaking your application up into pieces (as with features), how do you pull them all back together, and actually start your app running? At first glance, this may seem like a daunting task. As it turns out, however, because of the structure promoted by feature-u, it actually is a very simple process.

To solve this, feature-u provides the `[launchApp()](https://feature-u.js.org/0.1.3/api.html#launchApp)` function (see: [Launching Your Application](https://feature-u.js.org/0.1.3/detail.html#launching-your-application)).

Here is eatery-nod’s mainline …

The first thing to note is just how simple and generic the mainline startup process is. There is no real app-specific code in it … not even any global initialization!

That is because feature-u provides various hooks that allow your features to inject their own app-specific constructs.

The mainline merely accumulates the Aspects and Features, and starts the app by invoking `launchApp()`.

Here are some important points of interest (match the numbers to `*n*` in the code above):

1. `([*1*](#a002))` the supplied Aspects (pulled from separate NPM packages) reflect the frameworks of our run-time stack (in our example `[redux](http://redux.js.org/)`, `[redux-logic](https://github.com/jeffbski/redux-logic)`, and `[feature-router](https://github.com/KevinAst/feature-router)`) and extend the acceptable Feature properties — `Feature.reducer`, `Feature.logic`, and `Feature.route` respectively. (See [Extendable aspects](https://feature-u.js.org/0.1.3/detail.html#extendable-aspects)).
2. `([*2*](#a002))`all app features are accumulated from our `feature/` directory
3. `([*3*](#a002))`as a preview to [Feature Collaboration](#1895), the exported return value of `launchApp()` is an `App` object, which promotes the accumulated Public API of all features.

### [2. React Platforms](#6561)

In the example above (see `[*4*](#a002)`), you see that `launchApp()` uses a `[registerRootAppElm()](https://feature-u.js.org/0.1.3/api.html#registerRootAppElmCB)` callback hook to register the supplied `rootAppElm` to the specific React platform in use. Because this registration is accomplished by app-specific code, feature-u can operate in any of the React platforms (see [React Registration](https://feature-u.js.org/0.1.3/detail.html#react-registration)).

Here are some `[registerRootAppElm()](https://feature-u.js.org/0.1.3/api.html#registerRootAppElmCB)` variations:

[react web](https://reactjs.org/):

[react-native](https://facebook.github.io/react-native/):

[expo](https://expo.io/):

### [3. Feature Object](#6561)

Each feature is located in its own directory, and promotes aspect content through a `Feature` object (using `[createFeature()](https://feature-u.js.org/0.1.3/api.html#createFeature)`).

Here is an example from eatery-nod’s [device](https://github.com/KevinAst/eatery-nod/blob/after-features/src/feature/device/README.md) feature.

As you can see, the `Feature` object is merely a container that holds aspect content of interest to feature-u. The sole purpose of the `Feature` object is to communicate this aspect information to `launchApp()`.

We will fill in more detail a bit later, but for now notice that the feature is conveying reducers, logic modules, routes, and does some type of initialization (`appWillStart`/`appDidStart`). It also promotes a `publicFace` that can be used by other features (such as the feature’s Public API).

For more information, please refer to [Feature & aspect content](https://feature-u.js.org/0.1.3/detail.html#feature-object-relaying-aspect-content).

### [4. Feature Initialization](#6561)

Any given feature should not have to rely on an external startup process to perform the initialization that it needs. Rather, the feature should be able to spawn initialization that it depends on.

This could be any number of things, such as:

* initialize some service API
* inject a utility react component at the App root
* dispatch an action that kicks off a startup process
* And more...

To solve this, feature-u introduces two [Application Life Cycle Hooks](https://feature-u.js.org/0.1.3/appLifeCycle.html), injected through the following Feature aspects:

1. `[Feature.appWillStart({app, curRootAppElm}): rootAppElm || falsy](https://feature-u.js.org/0.1.3/appLifeCycle.html#appwillstart)` Invoked one time, just before the app starts up. This can do any type of initialization, including supplementing the app's top-level root element (such as the React `component` instance).
2. `[Feature.appDidStart({app, appState, dispatch}): void](https://feature-u.js.org/0.1.3/appLifeCycle.html#appDidStart)`   
Invoked one time immediately after the app has started. A typical usage for this hook is to dispatch some type of `bootstrap action`.

Here are some examples from eatery-nod:

FireBase Initialization:

Bootstrap Action:

Inject DOM Root Elm:

### [5. Feature Collaboration](#6561)

Even though a feature’s implementation is encapsulated, it still needs to interact with its surroundings. To complicate matters, one feature should never import resources from another feature, because it should strive to be plug-and-play. As a result, we need a well-defined feature-based Public API.

To solve this, feature-u promotes a [Cross Feature Communication](https://feature-u.js.org/0.1.3/crossCommunication.html). This is accomplished through the `Feature.publicFace`[Built-In aspect](https://feature-u.js.org/0.1.3/detail.html#built-in-aspects) property. A feature can expose whatever it deems necessary through its `publicFace`. There are no real constraints on this resource. It is truly open.

Typically this involves promoting selected:

* actions
* selectors
* APIs
* And so on

The `publicFace` of all features are accumulated and exposed through the `App` object (emitted from `launchApp()`).

It contains named feature nodes, as follows:

```
App.{featureName}.{publicFace}
```

Here is an example from eatery-nod’s [auth](https://github.com/KevinAst/eatery-nod/blob/after-features/src/feature/auth/README.md) feature.

Out of all the items found in the `auth` feature, only two actions and one selector are public.

Here is what the `App` object would look like for this example:

```
app: {  auth: {    actions: {      userProfileChanged(userProfile),      signOut(),    },    sel: {      getUserPool(appState),    },  },  currentView: {   // other features    ... snip snip  },}
```

As a result, the `auth` feature's public API can be accessed as follows:

```
app.auth.actions.userProfileChanged(userProfile)app.auth.actions.signOut()app.auth.sel.getUserPool(appState)
```

### [6. Framework Integration](#6561)

Most likely your application employs one or more frameworks (such as `redux` or `[redux-logic](https://github.com/jeffbski/redux-logic)`). How are the resources needed by these frameworks accumulated and configured across the many features of your app?

To solve this, feature-u introduces [Extendable aspects](https://feature-u.js.org/0.1.3/detail.html#extendable-aspects). **feature-u** is [extendable](https://feature-u.js.org/0.1.3/extending.html). It provides integration points between your features and your chosen frameworks.

Extendable Aspects are packaged separately from feature-u, so as to not introduce unwanted dependencies (because not everyone uses the same frameworks). You pick and choose them based on the framework(s) used in your project (matching your project’s run-time stack). They are created with feature-u’s extendable API, using [createAspect()](https://feature-u.js.org/0.1.3/api.html#createAspect). You can define your own Aspect, if the one you need doesn't already exist.

Let’s take a look at a redux example from eatery-nod.

The `device` feature maintains its own slice of the state tree.

It promotes its reducer through the `Feature.reducer` aspect:

Because `Feature.reducer` is an extended aspect (verses a built-in aspect), it is only available because we registered the [feature-redux](https://github.com/KevinAst/feature-redux) `reducerAspect` to `launchApp()` (please refer to [Simplified App Startup](#5974) above).

The key thing to understand is that feature-u (through the feature-redux extension) will automatically configure redux by accumulating all feature reducers into one overall appState.

Here is the reducer code …

A feature-based reducer is simply a normal reducer that manages the feature’s slice of the the overall appState. The only difference is it must be embellished with `[slicedReducer()](https://github.com/KevinAst/feature-redux#slicedreducer)`, which provides instructions on where to insert it in the overall top-level appState.

As a result, the `device` reducer only maintains the state relevant to the `device` feature (like its little slice of the world) — a status, a fontsLoaded indicator, and the device location.

**SideBar**: We are using the [astx-redux-util](https://astx-redux-util.js.org/) utility’s `[reducerHash()](https://astx-redux-util.js.org/1.0.0/api.html#reducerHash)` function to concisely implement the feature's reducer (providing an alternative to the common switch statement). I have found that in using a utility like this, for most cases it is feasible to implement all the reducers of a feature in one file (due in part to the smaller boundary of a feature). astx-redux-util also promotes other [Higher-Order Reducer](https://medium.com/@mange_vibration/reducer-composition-with-higher-order-reducers-35c3977ed08f)s. You may want to check this out.

### [7. Feature Enablement](#6561)

Some of your features may need to be dynamically enabled or disabled. As an example, certain features may only be enabled with a license upgrade, or other features may only be used for diagnostic purposes.

To solve this, feature-u introduces [Feature Enablement](https://feature-u.js.org/0.1.3/enablement.html). Using the `Feature.enabled` Built-In aspect (a boolean property), you can enable or disable your feature.

Here is an example from eatery-nod’s [sandbox](https://github.com/KevinAst/eatery-nod/blob/after-features/src/feature/sandbox/README.md) feature:

The sandbox feature promotes a variety of interactive tests, used in development, that can easily be disabled.

Typically this indicator is based on a dynamic expression, but in this case it is simply hard-coded (to be set by a developer).

**SideBar**: When other features interact with a feature that can be disabled, you can use the `App` object to determine if a feature is present or not (see: [Feature Enablement](https://feature-u.js.org/cur/enablement.html) for more information).

### [8. Managed Code Expansion](#6561)

In general, accessing **imported resources** during in-line code expansion can be problematic, due to the order in which these resources are expanded. The feature-u `App` object is such a critical resource (because it promotes the Public API of all features), **it must be available even during code expansion**. In other words, we cannot rely on an "imported app" being resolved during code expansion time.

To solve this, feature-u introduces [Managed Code Expansion](https://feature-u.js.org/0.1.3/crossCommunication.html#managed-code-expansion).

When aspect content definitions require the `App` object at code expansion time, you simply wrap the definition in a `[managedExpansion()](https://feature-u.js.org/0.1.3/api.html#managedExpansion)` function. In other words, your aspect content can either be the actual content itself (such as a reducer), or a function that returns the content.

When this is done, feature-u will expand it by invoking it in a controlled way, passing the fully resolved `App` object as a parameter.

Here is a logic module from eatery-nod’s [auth](https://github.com/KevinAst/eatery-nod/blob/after-features/src/feature/auth/README.md) feature:

You can see that the auth feature is using an action from the [device](https://github.com/KevinAst/eatery-nod/blob/after-features/src/feature/device/README.md) feature, requiring access to the `app` object (see `[*2*](#8030)`). Because the `app` object is needed during code expansion, we use the `managedExpansion()` function (see `[*1*](#8030)`), allowing feature-u to expand it in a controlled way, passing the fully resolved `app` object as a parameter.

### [9. UI Component Promotion](#6561)

Features that maintain their own UI Components need a way to promote them in the overall app’s GUI. Because features are encapsulated, how is this accomplished in an autonomous way?

To address this, feature-u recommends considering [Feature Based Routes](https://feature-u.js.org/0.1.3/featureRouter.html) via the [feature-router](https://github.com/KevinAst/feature-router) extendable Aspect (packaged separately). This approach can even be used in conjunction with other navigational solutions.

Feature Routes are based on a very simple concept: allow the application state to drive the routes! It operates through a series of feature-based routing functions that reason about the appState, and either return a rendered component, or null to allow downstream routes the same opportunity.

Here is a simple example from the [device](https://github.com/KevinAst/eatery-nod/blob/after-features/src/feature/device/README.md) feature.

This route analyzes the current appState, and displays a SplashScreen until the system is ready:

In feature based routing, you will not find the typical “route path to component” mapping catalog, where (for example) some pseudo `route('device')` directive causes the Device screen to display, which in turn causes the system to accommodate the request by adjusting its state appropriately.

Rather, the appState is analyzed, and if the device is NOT ready, no other screens are given the option to even render ... Easy Peasy!

Depending on your perspective, this approach can be more natural, but more importantly, it allows features to promote their own screens in an encapsulated and autonomous way.

### [10. Single Source of Truth](#6561)

Feature implementations (like all coding constructs) should strive to follow the **single-source-of-truth** principle. In doing this, a single line modification can propagate to many areas of your implementation.

What are some **Best Practices** for single-source-of-truth as it relates to features, and how can feature-u help?

The [Best Practices](https://feature-u.js.org/0.1.3/bestPractices.html) section highlights a number of feature-based single-source-of-truth items of interest. These are guidelines, because you must implement them in your application code (feature-u is not in control of this).

Here is an example from the [eateries](https://github.com/KevinAst/eatery-nod/blob/after-features/src/feature/eateries/README.md) feature:

The `featureName` is used to specify the top-level state location of this feature (see `[*1*](#d59b)`). feature-u guarantees the feature name is unique. As a result, it can be used to qualify the identity of several feature aspects.

For example:

* prefix action types with featureName, guaranteeing their uniqueness app-wide (see: [feature-redux](https://github.com/KevinAst/feature-redux#action-uniqueness-single-source-of-truth) docs)
* prefix logic module names with featureName, identifying where that module lives (see: [feature-redux-logic](https://github.com/KevinAst/feature-redux-logic#single-source-of-truth) docs)
* depending on the context, the featureName can be used as the root of your feature state’s shape (see: [feature-redux](https://github.com/KevinAst/feature-redux#state-root-single-source-of-truth) docs)

Because feature-u relies on `[slicedReducer()](https://github.com/KevinAst/feature-redux#slicedreducer)` (in the feature-redux package), a best practice is to use the reducer's embellished selector to qualify your feature state root in all your selector definitions. As a result the slice definition is maintained in one spot (see `[*2*](#d59b)`).

### [feature-u Benefits](#e80d)

In summary, the benefits of using feature-u include:

* **Feature Encapsulation** — isolating feature implementations improves code manageability
* **Cross Feature Communication** — a feature’s public API is promoted through a well-defined standard
* **Feature Enablement** — enable/disable features through a run-time switch
* **Application Life Cycle Hooks** — features can initialize themselves without relying on an external process
* **Single Source of Truth** — is facilitated in a number of ways within a feature’s implementation
* **Framework Integration** — configure the framework(s) of your choice (matching your run-time-stack) using feature-u’s extendable API
* **UI Component Promotion** — through Feature Routes
* **Minimize Feature Order Dependency Issues** — even in code that is expanded in-line
* **Plug-and-Play** — features can be added/removed easily
* **Simplified Mainline** — `launcApp()` starts the app running by configuring the frameworks in use, all driven by a simple set of features.
* **Operates in any React Platform** (including React Web, React Native and Expo)

Hopefully this article gives you a feel for how feature-u can improve your project. Please refer to the [full documentation](https://feature-u.js.org/) for more details.

feature-u allows you to focus your attention on the “business end” of your features! Go forth and compute!!

### [References](#e80d)

* [A feature based approach to React development](http://ryanlanciaux.com/blog/2017/08/20/a-feature-based-approach-to-react-development/) … Ryan Lanciaux
* [How to better organize your React applications?](https://medium.com/@alexmngn/how-to-better-organize-your-react-applications-2fd3ea1920f1) … Alexis Mangin
* [How to use Redux on highly scalable javascript applications?](https://medium.com/@alexmngn/how-to-use-redux-on-highly-scalable-javascript-applications-4e4b8cb5ef38) … Alexis Mangin
* [The 100% correct way to structure a React app (or why there’s no such thing)](https://hackernoon.com/the-100-correct-way-to-structure-a-react-app-or-why-theres-no-such-thing-3ede534ef1ed) … David Gilbertson
* [Redux for state management in large web apps](https://blog.mapbox.com/redux-for-state-management-in-large-web-apps-c7f3fab3ce9b) … David Clark

