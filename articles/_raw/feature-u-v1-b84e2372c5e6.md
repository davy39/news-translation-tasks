---
title: Unleash the Power of Feature Based JS Development — with feature-u V1
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-22T00:31:55.000Z'
originalURL: https://freecodecamp.org/news/feature-u-v1-b84e2372c5e6
coverImage: https://cdn-media-1.freecodecamp.org/images/1*79altp9cNA9V31OonG_pSA.jpeg
tags:
- name: features
  slug: features
- name: JavaScript
  slug: javascript
- name: Libraries
  slug: libraries
- name: React
  slug: react
- name: Utilities
  slug: utilities
seo_title: null
seo_desc: 'By Kevin Bridges

  This article is an introduction to a new JS library called feature-u, that facilitates
  feature-based development in your React project.


  Note_: On 8/14/2018 feature-u V1 was released, that re-designed Cross Feature Communication
  to i...'
---

By Kevin Bridges

This article is an introduction to a new JS library called [feature-u](https://feature-u.js.org/), that _facilitates feature-based development in your [React](https://reactjs.org/) project_.

> **_Note_**_: On 8/14/2018 [**feature-u V1**](https://feature-u.js.org/1.0.0/history.html#v1_0_0) was released, that re-designed [Cross Feature Communication](https://feature-u.js.org/1.0.1/crossCommunication.html) to include [UI Composition](https://feature-u.js.org/1.0.1/crossCommunication.html#ui-composition) as a core offering. This article covers the V1 release. The first article, based on [feature-u V0](https://feature-u.js.org/0.1.3/history.html#v0_1_3), can be found [here](http://bit.ly/feature-u). We are very excited about this update because it **promotes one solution for all feature collaboration**!_

Most developers would agree that organizing your project by feature is much preferred over type-based patterns. Because **application domains grow** in the real world, project **organization by type simply doesn’t scale**, _it just becomes unmanageable_!

There are a number of good articles that discuss this topic with insight on feature-based design and structure (see: [References](#8e25) below). However when it comes to the implementation, you are pretty much left to fend for yourself.

[**feature-u**](https://feature-u.js.org/) is a utility library that manages and streamlines this process. It automates the mundane details of managing features and helps to promote features that are truly **plug-and-play**.

This article provides a foundation of [**feature-u**](https://feature-u.js.org/) concepts and terminology, building insight into how you can promote individual **plug-and-play** features within your project. It makes the case for why **feature-u** was developed and gives you a better understanding of it’s benefits.

Check out the [full docs](https://feature-u.js.org/), [source](https://github.com/KevinAst/feature-u), and [npm package](https://www.npmjs.com/package/feature-u).

[**feature-u**](https://feature-u.js.org/) opens new doors into the exciting world of feature-based development. It frees you up to **focus your attention on the “business end” of your features**!

### At a Glance

For your convenience, this **Table of Contents** (TOC) links directly to **each section. Also note that each section title links back to the TOC**.

```
Feature Based Development  Segregating Features  Feature Goals    Feature Runtime Consolidation    Feature CollaborationThe feature-u Solution  launchApp()  Feature Object  aspects  Running the App    App Initialization    Framework Configuration    Launching Your Application  Cross Feature Communication  Feature Based UI Composition    Resource Contracts  Feature EnablementIn SummaryBenefitsReferences
```

> _Please **help me get the word** **out** on **feature-u**. Your claps determine the distribution/promotion of this article. If you think **feature-u** has potential, please give this article multiple claps :-)_

### [Feature Based Development](#e98c)

At a 30,000 ft view, feature-based development (as in most software) is all about dissecting hard problems into smaller pieces. Even when I started my career _(back in the 70's)_, this was a prominent quote:

> “All problems in computer science can be solved by another level of indirection.” **David Wheeler**

By breaking up your application into features, each feature can focus on a more specific and isolated set of tasks. **In some ways you can think of a feature as a “mini application”**!

![Image](https://cdn-media-1.freecodecamp.org/images/1*50bxcswJEzugLESSDiFW7w.jpeg)

There are many design considerations in defining your feature boundaries. You can find several articles on this topic that provide insight on feature-based design.

For the most part, these considerations are part of the design of each individual project. While **feature-u** does not dictate overall design considerations, it does facilitate good feature-based principles (such as encapsulation). _This will be the focus of this article_.

### [Segregating Features](#e98c)

If you are like me, when you think about feature-based development, the first thing that comes to mind is to isolate your code into feature directories.

![Image](https://cdn-media-1.freecodecamp.org/images/1*8GHt18xe1e1tG9VQOXTMRQ.png)

In doing this your code is organized by what it accomplishes (i.e. features), rather than what it is (i.e. components, routes, logic, actions, reducers, selectors, etc.).

By segregating your features into individual directories, there is a semblance of isolation.

### [Feature Goals](#e98c)

Our goal is to **encapsulate each feature** in such a way as to make them truly **plug-and-play**. _But how is this accomplished_?

The directory structure is just a start. There are **several hurdles** that must be overcome to realize our goal …

* How do we encapsulate and isolate our features, while still allowing them to collaborate with one another?
* How can selected features introduce start-up initialization (even injecting utility at the root DOM), without relying on some external startup process?
* How can feature-based UI Composition be accomplished in an isolated and autonomous way?
* How do we configure our chosen frameworks now that our code is so spread out?
* How do we enable/disable selected features which are either optional, or require a license upgrade?

**In short**, how do we achieve a running application from these isolated features?

When you boil it all down, there are **two overriding characteristics** that must be accomplished to achieve our goals:

1. `[**Feature Runtime Consolidation**](#c8d1)`: _pulling our features back together into one running application_
2. `[**Feature Collaboration**](#abbc)`: _provide a mechanism by which our features can interact with one another_

As it turns out, _everything else is a byproduct of these two artifacts_. Let’s take a closer look at each of these items.

### [Feature Runtime Consolidation](#e98c)

Now that we have isolated our features into separate entities, how do we bring them back together so they run as **one application**? We must be able to pull and configure various aspects of our individual features, and “launch” them as a single homogeneous running application.

![Image](https://cdn-media-1.freecodecamp.org/images/0*k1La5g-6jXlOCIP-.png)

This concern can be further divided into two sub-concerns:

* `[App Initialization](#d44a)`  
Some features may require certain startup initialization. As an example, a feature that encapsulates some DB abstraction will rely on a run-time setup of a DB service.  
Certainly we don’t want to rely on some global app logic to accomplish this _(once again, we want our features to be encapsulated and self-sufficient)_.
* `[Framework Configuration](#c339)`  
If your application relies on other frameworks, chances are there are resources contained within each feature that must be accumulated and fed into the framework configuration process.  
How is this accomplished?

### [Feature Collaboration](#e98c)

The second characteristic (mentioned above) is **Feature Collaboration** — _providing a mechanism by which our features can interact with one another_.

A **best practice** of feature-based development _(to the extent possible)_ is to **treat each feature as an isolated implementation**. Most aspects of a feature are internal to that feature’s implementation _(for example, actions are typically created and consumed exclusively by logic/reducers/components that are internal to that feature)_.

From this perspective, you can think of each feature as its **own isolated mini application**.

With that said, however, we know that _“_**no man is an island**_”_! Any given feature ultimately exists as part of a larger application. There are cases where a feature needs to promote a limited subset of its aspects to other features. For example, a feature may need to:

* be knowledgeable of some external state (via a selector)
* emit or monitor actions of other features
* consolidate component resources from other features — as in **UI Composition**
* invoke the API of other features
* etc. etc. etc.

These items form the basis of why `[**Cross Feature Communication**](#5369)` and `[**Feature Based UI Composition**](#a480)` are needed.

![Image](https://cdn-media-1.freecodecamp.org/images/0*S6DWAwYUVlWsTR5Q.png)

To complicate matters, as a general rule, **JS imports should NOT cross feature boundaries**. The reason being that this cross-communication should be **limited to public access points** — helping to **facilitate true plug-and-play**.

![Image](https://cdn-media-1.freecodecamp.org/images/0*rUqXNI_dmUnyaPQn.png)

Given all this then, **how is Cross Feature Communication achieved** _in a way that doesn’t break encapsulation_?

Features need a way to promote their **Public Interface** to other features, and consume other feature’s **Public Assets**.

### [The feature-u Solution](#e98c)

Let’s take a look at the solution **feature-u** provides for all of these goals. The following sections will build **feature-u** concepts incrementally.

![Image](https://cdn-media-1.freecodecamp.org/images/1*GBSlbLZegIq6vN-6tPY02A.jpeg)

### [launchApp()](#e98c)

`[launchApp()](https://feature-u.js.org/1.0.1/api.html#launchApp)` is an essential utility in **feature-u**. It is an agent, working on your behalf, which provides the foundation that **accomplishes all the goals** of **feature-u**! It facilitates both `[**Feature Runtime Consolidation**](#c8d1)` and `[**Feature Collaboration**](#abbc)`.

With this utility, **your mainline startup process is extremely simple** … it merely invokes `[launchApp()](https://feature-u.js.org/1.0.1/api.html#launchApp)`, and you are done!

![Image](https://cdn-media-1.freecodecamp.org/images/0*73_25clr2UP2Vbqb.png)

The `[launchApp()](https://feature-u.js.org/1.0.1/api.html#launchApp)` function actually starts your application running, employing various hooks that drive BOTH **App Initialization** and **Framework Configuration**!

You can find `[launchApp()](https://feature-u.js.org/1.0.1/api.html#launchApp)` examples in the `[Usage](https://feature-u.js.org/1.0.1/usage.html#launchapp)` section, and `[Launching Your Application](https://feature-u.js.org/1.0.1/detail.html#launching-your-application)`.

**How does this work? What are the bindings to `[launchApp()](https://feature-u.js.org/1.0.1/api.html#launchApp)`**? ... _let's delve a bit deeper…_

### [Feature Object](#e98c)

To accomplish this, each feature promotes a `[Feature](https://feature-u.js.org/1.0.1/api.html#Feature)` object _(using `[createFeature()](https://feature-u.js.org/1.0.1/api.html#createFeature)`)_, that catalogs aspects of interest to **feature-u**.

This is the primary input to `[launchApp()](https://feature-u.js.org/1.0.1/api.html#launchApp)`.

![Image](https://cdn-media-1.freecodecamp.org/images/0*5vyM9ekRX_AYaaXw.png)

### [aspects](#e98c)

In **feature-u**, “aspect” _(little “a”)_ is a generalized term used to refer to the various ingredients that (when combined) constitute your application. Aspects can take on many different forms: **UI Components** • **Routes** • **State Management**_(actions, reducers, selectors)_ • **Business Logic** • **Startup Initialization Code** • _etc. etc. etc._

**Not all aspects are of interest to feature-u** … _only those that are needed to setup and launch the application_ … all others are considered an internal implementation detail of the feature. As an example, consider the Redux state manager: while it uses actions, reducers, and selectors … only reducers are needed to setup and configure Redux.

![Image](https://cdn-media-1.freecodecamp.org/images/0*fCOFHW2dFyYYSrd-.png)

The `[Feature](https://feature-u.js.org/1.0.1/api.html#Feature)` object is merely a lightweight container that holds aspects of interest to **feature-u**. These aspects can either be `[Built-In aspects](https://feature-u.js.org/1.0.1/detail.html#built-in-aspects)` _(from core **feature-u**)_, or `[Extendable aspects](https://feature-u.js.org/1.0.1/detail.html#extendable-aspects)` _(from plugin extensions)_.

### [Running the App](#e98c)

Let’s see how `[launchApp()](https://feature-u.js.org/1.0.1/api.html#launchApp)` accommodates the two sub-goals of running the app:

* `[App Initialization](#d44a)`
* `[Framework Configuration](#c339)`

### [App Initialization](#e98c)

Because `[launchApp()](https://feature-u.js.org/1.0.1/api.html#launchApp)` is in control of starting the app, it can introduce `[Application Life Cycle Hooks](https://feature-u.js.org/1.0.1/appLifeCycle.html)`.

This allows each feature to perform app-specific initialization, and even inject components into the root of the app.

There are two hooks:

1. `[Feature.appWillStart()](https://feature-u.js.org/1.0.1/appLifeCycle.html#appwillstart)` - invoked one time at app startup time
2. `[Feature.appDidStart()](https://feature-u.js.org/1.0.1/appLifeCycle.html#appdidstart)` - invoked one time immediately after app has started

![Image](https://cdn-media-1.freecodecamp.org/images/0*9EzmrTLQ-pglIoek.png)

`[Application Life Cycle Hooks](https://feature-u.js.org/1.0.1/appLifeCycle.html)` **greatly simplify your app's mainline startup process**, because _initialization specific to a given feature can be encapsulated in that feature_.

### [Framework Configuration](#e98c)

A fundamental goal of **feature-u** is to **automatically configure the framework(s)** used in your run-time-stack _(by accumulating the necessary resources across all your features)_. This greatly reduces the boilerplate code within your app.

How can this be accomplished when there are so many frameworks out there … and every project uses a different mix?

**feature-u** is extendable! It operates in an open plugable architecture where **Extendable Aspects** integrate **feature-u** to other frameworks, matching your specific run-time stack. **This is good,** _because not everyone uses the same frameworks_!

**Extendable Aspects** can be found in external NPM packages _(the normal case)_, or you can create your own using `[createAspect()](https://feature-u.js.org/1.0.1/api.html#createAspect)` _(a more advanced topic)_.

![Image](https://cdn-media-1.freecodecamp.org/images/0*be_uSLWT5KxyCiTD.png)

The `[Aspect](https://feature-u.js.org/1.0.1/api.html#Aspect)` object contains a series of `[Aspect Life Cycle Hooks](https://feature-u.js.org/1.0.1/extending.html#aspect-life-cycle-methods)` that are invoked under the control of **feature-u**(`[launchApp()](https://feature-u.js.org/1.0.1/api.html#launchApp)`). In general, an Aspect's responsibility is to:

* accumulate `[AspectContent](https://feature-u.js.org/1.0.1/api.html#AspectContent)` across all features
* perform some desired setup and configuration
* expose it’s functionality in some way (typically a framework integration)

An `[Aspect](https://feature-u.js.org/1.0.1/api.html#Aspect)` automatically extends the `[Feature](https://feature-u.js.org/1.0.1/api.html#Feature)` object by allowing it's `[AspectContent](https://feature-u.js.org/1.0.1/api.html#AspectContent)` to be **"cataloged"** in the `Feature` using `Aspect.name` as it's key. In the diagram above, you can see that

* the `reducerAspect` (`Aspect.name: 'reducer'`) permits a `Feature.reducer: reducerContent` construct
* and the `logicAspect` (`Aspect.name: 'logic'`) permits a `Feature.logic: logicContent` construct

It is important to understand that the interface to your chosen frameworks is not altered in any way. You use them the same way you always have _(just within your feature boundary)_. **feature-u** merely provides a well-defined organizational layer, where the frameworks are automatically setup and configured by accumulating the necessary resources across all your features.

### [Launching Your Application](#e98c)

In **feature-u,** the application mainline is very simple and generic. There is no real app-specific code in it … **not even any global initialization**! That is because **each feature can inject their own app-specific constructs**!! The mainline merely accumulates the `[Aspects](https://feature-u.js.org/1.0.1/api.html#Aspect)` and `[Features](https://feature-u.js.org/1.0.1/api.html#Feature)`, and starts the app by invoking `[launchApp()](https://feature-u.js.org/1.0.1/api.html#launchApp)`:

Here are some **important points of interest** _(match the numbers to `*n*` in the code above)_:

1. the supplied `[Aspects](https://feature-u.js.org/1.0.1/api.html#Aspect)` _(pulled from separate npm packages)_ reflect the frameworks of our run-time stack _(in our example `[redux](http://redux.js.org/)`, `[redux-logic](https://github.com/jeffbski/redux-logic)`, and `[feature-router](https://github.com/KevinAst/feature-router)`)_ and extend the acceptable Feature properties _(`Feature.reducer`, `Feature.logic`, and `Feature.route` respectively)_ ... **_see:_** `[Extendable aspects](https://feature-u.js.org/1.0.1/detail.html#extendable-aspects)`
2. all of our app features are supplied (accumulated from the `features/` directory)
3. a `[registerRootAppElm()](https://feature-u.js.org/1.0.1/api.html#registerRootAppElmCB)` callback is used to catalog the supplied `rootAppElm` to the specific React platform in use. Because this registration is accomplished by your app-specific code, **feature-u** can operate in any of the React platforms, such as: `[react-web](https://reactjs.org/)`, `[react-native](https://facebook.github.io/react-native/)`, and `[expo](https://expo.io/)` ... **_see:_** `[React Registration](https://feature-u.js.org/1.0.1/detail.html#react-registration)`
4. _as a bit of a preview_, the return value of `[launchApp()](https://feature-u.js.org/1.0.1/api.html#launchApp)` is a `[Fassets object](https://feature-u.js.org/1.0.1/api.html#Fassets)`, which promotes the accumulated Public Face of all features, and is exported to provide `[Cross Feature Communication](https://feature-u.js.org/1.0.1/crossCommunication.html)`.

### [Cross Feature Communication](#e98c)

In support of **Feature Collaboration** _that doesn’t break encapsulation_, **feature-u** promotes feature-based resources through something called `fassets` (feature assets). This is how all **Cross Feature Communication** is accomplished. You can think of this as the **Public Face** of a feature.

**SideBar**: The term `fassets` is a play on words. While it is pronounced "facet" _and is loosely related to this term_, it is spelled fassets (i.e. feature assets).

A feature can expose whatever it deems necessary through the built-in `[Feature.fassets aspect](https://feature-u.js.org/1.0.1/api.html#fassets)`). There is no real constraint on this resource. It is truly open.

![Image](https://cdn-media-1.freecodecamp.org/images/0*TbIrHeN2HxFwFzhY.png)

The `[fassets aspect](https://feature-u.js.org/1.0.1/api.html#fassets)` has a `define` directive where resources are cataloged.

Here is a simple example of how `fassets` are defined:

**feature-u** accumulates `fassets` from all active features, and promotes them through the `[Fassets object](https://feature-u.js.org/1.0.1/api.html#Fassets)` _(emitted from `[launchApp()](https://feature-u.js.org/1.0.1/api.html#launchApp)`)_.

**SideBar**: There are several ways to obtain access the `Fassets object` _(see `[Obtaining fassets object](https://feature-u.js.org/1.0.1/crossCommunication.html#obtaining-fassets-object)`)_.

To reference a `fassets` resource, simply dereference it as any other object reference. There is also a `[Fassets.get()](https://feature-u.js.org/1.0.1/api.html#Fassets_get)`method that can be supplied `[Wildcards](https://feature-u.js.org/1.0.1/crossCommunication.html#wildcards-adding-dynamics)`, returning an array of resources.

This is an example of a **push** philosophy. Here the supplier is is simply publicly promoting a resource for other features to use **(take it or leave it)**. The supplier is merely saying: _“this is my Public Face”_.

You can find more information about this topic in `[Cross Feature Communication](https://feature-u.js.org/1.0.1/crossCommunication.html)`.

### [Feature Based UI Composition](#e98c)

It is common for a UI component to be an accumulation of sub-components that span several features. As a result, **UI Composition is a very important part of Cross Feature Communication**.

In support of this, **feature-u** introduces the `[withFassets()](https://feature-u.js.org/1.0.1/api.html#withFassets)` Higher-order Component (HoC) that auto-wires fasset properties into a component. This is a common pattern popularized by Redux `connect()` _(simplifying component access to application state)_.

Here is how a component would access a `company.logo` _(defined by another feature)_:

The `[withFassets()](https://feature-u.js.org/1.0.1/api.html#withFassets)` HoC auto-wires named feature assets as component properties through the `[mapFassetsToPropsStruct](https://feature-u.js.org/1.0.1/api.html#mapFassetsToPropsStruct)` hook. In this example, because the `Logo` property is a component, `MyComponent` can simply reference it using JSX.

You can find more information about this topic in `[UI Composition](https://feature-u.js.org/1.0.1/crossCommunication.html#ui-composition)`.

### [Resource Contracts](#e98c)

It is common for UI Composition to be represented as a contract, where a component in one feature has a series of injection needs that are to be supplied by other features.

The `[fassets aspect](https://feature-u.js.org/1.0.1/api.html#fassets)` has additional constructs to facilitate this contractual arrangement, allowing **feature-u** to provide more validation in the process.

Rather than just defining resources in one feature and using them in another:

* A given feature can specify a series of injection needs using the `fassets.use` directive. This identifies a set of **injection keys** that uniquely identify these resources.
* Other features will supply this content using the `fassets.defineUse` directive, by referencing these same **injection keys**.

This represents more of a **pull** philosophy. It gives **feature-u** more knowledge of the process, allowing it to verify that supplied resources are correct.

Wildcards (`*`) can be used to add additional dynamics to the process, allowing features to inject their content autonomously.

Here is a `main` feature that is pulling in a series of sub-components _(links and bodies)_ from other features:

**main feature:**

Because our specification includes wildcards, a series of definitions will match!

Here is the `MainPage` component that fulfills the usage contract:

When `[withFassets()](https://feature-u.js.org/1.0.1/api.html#withFassets)` encounters wildcards (`*`), it merely accumulates all matching definitions, and promotes them as arrays.

Through this implementation, **any feature may dynamically inject itself in the process autonomously**! In addition, this dynamic implicitly handles the case where a feature is dynamically disabled **(very kool indeed)**!!

The following snippets are taken from other features that supply the definitions for the content to inject:

**cart feature**

**search feature**

Two external features (**cart** and **search**) define the content that is requested by the **main** feature.

The `fassets.defineUse` directive requires that the resource keys match a `fassets.use` feature request. This is the contract that provides **feature-u** insight when enforcing it's validation.

**SideBar**: Because we are also dealing with navigation, we introduce `[react-router](https://reacttraining.com/react-router/)` into the mix (with the `Link` and `Route` components). Because of RR's V4 design, our routes are also handled through component composition _(see `[Feature Based Routes](https://feature-u.js.org/1.0.1/featureRouter.html)` for more information)_.

You can find more information about this topic in `[UI Composition](https://feature-u.js.org/1.0.1/crossCommunication.html#ui-composition)`.

### [Feature Enablement](#e98c)

Features can be dynamically disabled by setting the `Feature.enabled` boolean property _(part of the `[Built-In aspects](https://feature-u.js.org/1.0.1/detail.html#built-in-aspects)`)_:

In this example, it is just as though the `sandbox` feature doesn't exist. In other words **it has been logically removed**.

Typically, this indicator is based on some run-time expression, allowing packaged code to be dynamically enabled/disabled during the application’s start-up process:

This dynamic is useful in a number of different situations. For example:

* some features may require a license upgrade
* other features may only be used for diagnostic purposes, and are disabled by default

You can find more information about this topic in `[Feature Enablement](https://feature-u.js.org/1.0.1/enablement.html)`.

### [In Summary](#e98c)

The following diagram summarizes **feature-u**’s Basic Concepts _(as discussed above)_:

![Image](https://cdn-media-1.freecodecamp.org/images/1*qsohsNr9SgLca22xW6r1eQ.png)

### [Benefits](#e98c)

There are many benefits in using **feature-u**!

![Image](https://cdn-media-1.freecodecamp.org/images/1*SJ-3bETYSjbchI28hEXlUw.jpeg)

The two fundamental artifacts from which most benefits are derived are:

* A formal means by which features can collaborate with one another _(`[Cross Feature Communication](http://localhost:4000/crossCommunication.html)`)_, making them truly **plug-and-play**  
This includes the ability for `[UI Composition](http://localhost:4000/crossCommunication.html#ui-composition)` to cross feature boundaries. It even allows UI Content to be injected autonomously. This is something that has to be seen ... it shows off **feature-u** very well.
* A significant reduction in boilerplate code through:  
Auto configuration of the frameworks in-use _(via plugin extensions — `[Extendable aspects](http://localhost:4000/detail.html#extendable-aspects)`)_  
Startup initialization that is encapsulated within features _(via `[Application Life Cycle Hooks](http://localhost:4000/appLifeCycle.html)`)_

The following list of benefits can be directly correlated to the considerations that formed the basis of why **feature-u** was developed _(see: `[Why feature-u?](http://localhost:4000/why.html)`)_.

1. **Feature Encapsulation:** _isolating feature boundaries improves code manageability_
2. **Feature Collaboration:** _promote **Cross Feature Communication** through a well-defined feature-based Public Interface_
3. **Feature Based UI Composition:** _facilitate seamless **cross-feature component composition**_
4. **Application Life Cycle Hooks:** _features can initialize themselves without relying on an external process_
5. **Feature Enablement:** _enable/disable features through a run-time switch_
6. **Minimize Feature Order Dependency Issues** _during in-line code expansion_
7. **Framework Integration:** _automatically configure used framework(s) (matching the app’s run-time-stack) by accumulating all feature aspects (employing an extendable API)_
8. **UI Component Promotion:** _features can autonomously promote their UI components through Feature Based Route Management_
9. **Single Source of Truth:** _is facilitated in a number of ways within a feature’s implementation_
10. **Simplified App Startup:** _launching an app can be accomplished through a single line of executable code!_
11. **Operates in any React Platform** _React Web, React Native, Expo, etc._
12. **Plug-and-Play:** _features can be more easily added or removed_

**feature-u** allows you to **focus your attention on the “business end” of your features!**

_Go forth and compute!!_

### [References](#e98c)

* [A feature based approach to React development](http://ryanlanciaux.com/blog/2017/08/20/a-feature-based-approach-to-react-development/) _… Ryan Lanciaux_
* [How to better organize your React applications?](https://medium.com/@alexmngn/how-to-better-organize-your-react-applications-2fd3ea1920f1) _… Alexis Mangin_
* [How to use Redux on highly scalable javascript applications?](https://medium.com/@alexmngn/how-to-use-redux-on-highly-scalable-javascript-applications-4e4b8cb5ef38) _… Alexis Mangin_
* [The 100% correct way to structure a React app (or why there’s no such thing)](https://hackernoon.com/the-100-correct-way-to-structure-a-react-app-or-why-theres-no-such-thing-3ede534ef1ed) _… David Gilbertson_
* [Redux for state management in large web apps](https://blog.mapbox.com/redux-for-state-management-in-large-web-apps-c7f3fab3ce9b) _… David Clark_

