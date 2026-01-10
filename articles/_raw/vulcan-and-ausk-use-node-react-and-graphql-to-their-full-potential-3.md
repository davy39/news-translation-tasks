---
title: 'A comparison between Vulcan and AUSK: how to use Node, React and GraphQL to
  their full potential'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-10-02T14:58:50.000Z'
originalURL: https://freecodecamp.org/news/vulcan-and-ausk-use-node-react-and-graphql-to-their-full-potential-3
coverImage: https://www.freecodecamp.org/news/content/images/2019/10/sayan_ausk_vulcan_banner_1600.png
tags:
- name: Vulcan.js
  slug: vulcan-js
- name: Apollo GraphQL
  slug: apollo
- name: GraphQL
  slug: graphql
- name: JavaScript
  slug: javascript
- name: React
  slug: reactjs
seo_title: null
seo_desc: 'By Eric Burel

  The NRG stack for faster development

  You''ve probably never heard of either Vulcan.js or Apollo Universal Starter Kit –
  at least not yet.

  But I am pretty sure you''ve heard about React, Node.js and GraphQL. Okay, that’s
  what we call an un...'
---

By Eric Burel

## The NRG stack for faster development

You've probably never heard of either Vulcan.js or Apollo Universal Starter Kit – at least not yet.

But I am pretty sure you've heard about React, Node.js and GraphQL. Okay, that’s what we call an understatement: you’ve likely seen millions of tweets, blog articles, meetups and podcasts about those three and their magical powers.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/tweet.png)
_Sums up 2017-2020 in one tweet_

There are a lot of good reasons why those technologies are praised by web developers. Yet, if you ever tried to write a modern full-stack JavaScript application from scratch, you may have noticed the amount of boilerplate it can produce.

This is especially annoying with generic features: setting up authentication, setting up the database, setting up the main App component, setting up the settings…

Both Vulcan.js and AUSK aim to make you a fast and efficient full-stack JavaScript developer. Both rely on a modular architecture, with React for the UI, Node for the backend, and Apollo graphQL for the client/server communication layer. Both provide tons of pre-coded modules so you can focus on valuable features.

However, they each take very different approaches to the problem, so I thought you might enjoy a comparison.

First of all let’s introduce the competitors.

_Disclaimer: I am a contributor of Vulcan.js, however I used both of those technologies for my client’s projects so I’ll stay as objective as can be._

## Apollo UNIVERSAL Starter Kit

![Image](https://www.freecodecamp.org/news/content/images/2019/10/ausk_400.png)

Okay, when they say universal, they mean UNIVERSAL. Have you ever seen a JavaScript boilerplate that includes a Scala server for big work? And a full React Native setup with Expo? They even close the eternal (and annoying) Angular versus React debate by supporting both.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/ausk-stack.png)
_Technologies included in AUSK: Node, Scala, React, Angular and React Native, all tied by GraphQL. Kind of the Oscar ceremony of modern web development._

I don’t have much else to say. I mean, look again at this stack, that’s a web developer’s wildest dream! 

I actually have something to add: it also includes Bootstrap and Ant Design as styling frameworks, Knex to connect to SQL database (MongoDB connection is not included but easily doable), and it’s written in TypeScript. All core features of a JS/GraphQL application are provided in the boilerplate (menu, auth, etc.)+ a few higher level modules that serve as examples.

Link: [https://github.com/sysgears/apollo-universal-starter-kit](https://github.com/sysgears/apollo-universal-starter-kit)

## Vulcan: beyond universal, isomorphic

![Image](https://www.freecodecamp.org/news/content/images/2019/10/vulcan.png)

Remember Meteor and Telescope? I know the JS ecosystem moves fast, but this golden era was like only 2 or 3 years ago.

Meteor was the first framework to fully exploit the combination of server-side and client-side JavaScript, by allowing to write isomorphic code that runs on both environment. Telescope was a Meteor boilerplate app meant to fully enjoy its package-oriented architecture.

Though still used in many professional apps and known by a whole lot of developers, Meteor is crippled by some technical limitations that prevents a wider usage: its webpack-incompatible build system, its package manager that is now surpassed by NPM, or its RAM-consuming real-time data exchange protocol.

And I am yet to discover a framework that makes devs half as productive as Meteor. But don’t worry, there’s now a serious contender. You get it : Vulcan !

The use of Apollo GraphQL and a rational package-oriented architecture allow Vulcan to overcome Meteor's limitations while enjoying the same advantages: fully modular architecture, declarative programming, isomorphism and so on.

Vulcan is meant to be the Rails of the JavaScript ecosystem. Easy to get started with but complete enough to write any app.

[Check my previous article for a more complete description of Vulcan patterns targeting development speed](http://:%20https://medium.com/dailyjs/write-less-code-ship-more-apps-how-vulcan-js-makes-me-an-efficient-developer-71c829c76417).

Link: [http://vulcanjs.org/](http://vulcanjs.org/)

## #1: Framework VS Boilerplate

First major difference between these tools: AUSK is a boilerplate, while Vulcan is a framework. Where does the distinction lie, you may wonder?

### Vulcan, a framework

A framework is meant to make you a more efficient developer on a daily basis by providing a specific set of functions and helpers. It is usually designed to stay separate from your app. You can update your app from time-to-time whenever a new version of the framework is published.

We usually distinguish frameworks and librairies based on the level of specialization. A framework usually allows delivering business-level features, while a library is a more specialized technical tool. But both mostly works the same.

The limitation with frameworks or libs is that you may feel lost when they abandon you. What do you do when the bug is not in your app, but in React or Apollo?

My rule of thumb is that when using a framework, you should be ready to contribute to its development, at least by opening issues whenever you encounter a bug.

### AUSK, a boilerplate

A boilerplate is a well written piece of code with a fully working development environment. That’s all. With a boilerplate it’s harder to keep up with updates because the boilerplate code is not clearly separated from your app. Kind of like Create React App after you eject.

It usually provides only few custom methods. You will feel faster in the first month and you will benefit from a battle-tested architecture, but your cruise speed will end up being mostly the same than without a boilerplate.

A boilerplate is far more freedom than a framework but also less impact on your efficiency.

## #2 Learning Curve

### Vulcan: GraphQL made easy

Vulcan can be a good way to get a first grasp of GraphQL because… you don’t need to actually write GraphQL. The framework generates the GraphQL schema and resolvers for you based on your data model. Using developer tools like GraphiQL or GraphQL Voyager, you can visualize and play around with the schema to get a grasp of how your features translate into GraphQL.

The second step is to understand the logic of Vulcan itself. A live tutorial is included in the “Vulcan Starter” app to help you in the process.

### AUSK: for purists

AUSK architecture is far closer to what Express developers are used to. Think of your canonical Express app, but with GraphQL installed and a package-based architecture. No surprises.

This also means that you’ll need to grasp the basics of GraphQL to use AUSK, in addition of course to Node, Express and React and whatever database you use (but the same goes for Vulcan). Luckily, it provides a few examples to help you in the process, including creating and listing data and even uploading files.

### Conclusion: Full-stack devs have a lot to master

The JavaScript ecosystem is maturing more and more, which also means it is harder to learn and understand for beginners.

To fully enjoy those technologies, you’ll need at least some knowledge of modern JavaScript and React development.

Don’t expect to be fully productive at day one. That said, there are pleeenty of courses, free or paid, to learn modern full-stack JavaScript development. Studying AUSK and Vulcan can be an incredible source of inspiration.

## #3 Development speed

### Vulcan: automate all the things

When well used, [Vulcan is just incredibly fast at delivering features](https://www.freecodecamp.org/news/how-i-built-an-app-with-vulcan-js-in-four-days-6368814077b1/). This is because it relies on automated generation a lot, so it can produces the most relevant parts of an app in a matter of hours as long as your data model is correctly defined.

This pattern is called declarative programming: you “declare” how your app works and let the framework do the job. It’s difficult to implement but can be extremely powerful.

### AUSK: more freedom

Since AUSK is boilerplate-focused, it’s a bit tougher to add basic features as it’s a multi-step process:

* write your GraphQL schema
* same for resolvers, mutations
* same for your database model (using Knex or Mongoose)
* same for your React components
* …

However, if you need to write a custom feature, it’s gonna be easier with AUSK than with Vulcan. So if you have very few data models but complex features, AUSK will be more efficient than Vulcan.

Hopefully there are ongoing work to make AUSK more declarative, through an innovative Domain Driven Design inspired schema system, [domain-schema](https://github.com/sysgears/domain-schema).

### Conclusion: select the right tool for the right use case

There’s no magical universal technology for full-stack JS development. The development speed with each framework depends a lot on the underlying use case. I tend to prefer Vulcan for data-oriented platforms and professional tools, and AUSK for B2C SaaS platforms that require more custom features.

## #4 Community, support and maturity

### Vulcan: heir of Meteor

Vulcan is a framework from Sacha Greif, who is a long time Meteor developer and very invested in the JavaScript community ([State of JS](https://stateofjs.com/) and [State of CSS](https://stateofcss.com/) among other things).

There is an active Slack where beginners and other enthusiasts can quickly find answers to their questions.

### AUSK: an actively maintained project

AUSK is maintained by [SysGears](https://sysgears.com/), in particular by Victor Vlasenko, the founder of the company.

The project is associated with Gitter. During my latest freelance mission with AUSK, Victor responded very quickly to my issues and questions. He even merged the Storybook support after I gave it a shot.

### Conclusion: small but rich communities

Both technologies are used in production in multiple projects, so they are already safe to use. The communities are growing actively and beginner-friendly.

If you need to build a team, don’t expect to find freelancers that precisely know those technologies, they are too specific. Instead focus on finding full-stack JavaScript developers who will be able to quickly learn them. Alternatively, you can go to the source and find true specialists among the [Vulcan](http://slack.vulcanjs.org/) or [AUSK](https://gitter.im/sysgears/apollo-fullstack-starter-kit) communities.

## #5 Deployment

Not much to compare, both frameworks allow deployment on platforms offering free services like Zeit Now and Heroku as well as deployment on your own custom server.

## #6 Code scalability and modular patterns

### Vulcan: share efforts

One advantage of a framework is effort sharing. End usage is clearer, and thus allows us to integrate various optimizations within the framework itself.

Vulcan provides patterns like callbacks/hooks, enhancement and central registration to fully benefit from its package-oriented architecture. For example, we are able to add Material UI to an app, including SSR, without changing a single line of code in the Vulcan Core module.

More precisely, Vulcan provides different `register` methods for each data structure, like `registerComponent` , and also callbacks, like `router.wrapper` that allow to wrap the root `App` React component. You only need to import your file once at the package entry level ( `main` files).

### AUSK: start on the right track, finish by yourself

The modular architecture limits the temptation of writing spaghetti code. It favors code reuse across applications. Each package possesses an `index.ts` file that declares relevant middlewares, startup functions, graphQL functions shared with other modules.

The well-named `module` module provides classes for each environment to register a new module, like `ServerModule` and `ClientModule` . That’s the only module that is actually used directly at the app level.

<pre>
<code>
export default new ServerModule({
    onAppCreate: [ callback1, callback2]
})
</code>
</pre>

Internally all modules will be merged into one big module, that will eventually be used to create the app. For example, all `onAppCreate` callbacks will be run one after the other.

That’s a relatively clean pattern and a very smart architecture. I mean, even the module manager is a module, isn’t that beautiful?

But the rest is up to you. Nice, you’ll be able to optimize everything! So, are you going to loose couple your GraphQL resolvers and your Mongo database? Using which tools? How do you convert your GraphQL schema into Mongo projections? Are you going to write connectors, use DataLoader?

Here’s the point: writing a scalable app is hard. Very hard. If you want to learn, then good for you. I am very glad to use AUSK for this very reason, doing things by yourself is the best way to learn.

### Conclusion: are you risk-averse?

For both AUSK and Vulcan, code scalability means a modular architecture. Whenever code becomes too complex or unreadable, the solution is easy: cut it into smaller, simpler pieces.

Vulcan architecture is bolder, everything can be modular. This ambition comes at a risk, it may sometimes be difficult to get who registered what and when.

AUSK modular patterns are easier to read, but also a bit less powerful. It may for example be difficult to add complex global features without touching the core package code. Yet they are definitely sufficient for most use cases, you don’t have to be a modularity purist to write good apps.

## #6 Mobile

### Vulcan: with Cordova

Meteor, which Vulcan is based on, embeds Cordova. So your web app can be bundled as a mobile application with a single command line.

However Vulcan does not provide tools for native apps. Of course you can still create an independent React Native app and plug it to Vulcan. Improvements on the auth system (currently the last piece of Vulcan really relying on Meteor) are planned in the months to come to facilitate such connections.

### AUSK: with React Native

Combining both a setup for “vanilla” React and React Native is one of the best features of AUSK. After all, it’s a Universal starter kit! I don’t do much mobile myself but it’s reassuring to be able to quickly create a native mobile app sharing the same server as my web interface.

### Conclusion: AUSK is better at mobile-first

AUSK will be more suited if you specifically need to write a mobile app. Nonetheless Vulcan allows to build a mobile app from your code in just one command-line, which is okay if the mobile version is more secondary to you.

## #7 Change the UI: a tough issue

Creating a fullstack framework that allows instantaneous UI library change is a dream only achieved during the era of CSS. Remember those websites that allowed to switch  theme by clicking on a single button?

![Image](https://www.freecodecamp.org/news/content/images/2019/10/fire.png)
_“What logo can we pick for our nice CSS-in-JS lib?” “I don’t know, kind of a badass warrior woman?” “Yeah it makes total sense” — creators of [Emotion](https://github.com/emotion-js/emotion), probably_

Then the JS nations attacked. Using React components, it is very difficult to provide such a feature (except for trivial color changes), because style and design is now very tied to the underlying React/Angular/Vue components.

Each React UI lib has its own way to define a button, without even speaking about theming. That’s a problem for full-stack technologies like AUSK and Vulcan, because picking a styling framework is a matter of taste. They can’t just propose a definitive choice and force you to stick to it. Bootstrap is no longer at monopoly and each developer has their own favorite lib.

To tackle this issue, both have a similar approach. They wrote a canonical set of components with Bootstrap, then tried to allow the replacement of those components with another lib like Ant Design or Material UI.

It makes the code weird. For example, AUSK Button will take a `color` prop, because it is how Bootstrap work. If you switch to Ant Design, you will also need to use the color prop, even if Ant Design uses a `type` prop instead.

Since UI framework selection usually happens only once, being obligated to use a non-canonical set of props during all the developments seems a very high price for multiple UI framework support.

During development, I’d suggest to avoid using those pre-coded components for custom UI as much as possible. They are cool to build the example and generic features provided by the boilerplate/framework, but not that much when it comes to write the custom parts of your app.

Instead use the underlying components provided by Ant Design or Bootstrap or Material UI depending on your choice, and try to write your own UI lib. You could checkout Storybook to help you in the process, as it is included in both AUSK and Vulcan.

## #8 FREE FIGHT

If I were to retain differentiating features specific to each of these technologies, they would be these.

### Vulcan

The schema system. To my best knowledge,  no framework is able to generate the database structure, the server entry points, the client/server communication layer, and a production-ready frontend (forms, lists etc.) from a single JSON schema.

Vulcan.js can do that while using the latest JS technologies.

### AUSK

I did not manage to pick only one, so my loved features of AUSK would be TypeScript and React Native.

There has been debates for a few years around the benefits of statically typed JavaScript, whether to prefer Flow or TypeScript… And TypeScript definitely won the fight. Working with TypeScript is possible in Vulcan but, due to the use of Meteor, is currently feels unnatural and compilation is slow. AUSK uses TypeScript as a default and that’s awesome.

And React Native… well, there are also debates whether using React to write mobile apps is relevant. You may choose to stick to a responsive web app, but at least you know everything is setup for you, given that configuring a dev env for React Native is not always an easy task.

---

## So, have you made your choice?

There are so many points that should be taken into consideration like performance, security, DevOps, auth management… Picking the right tool to build your JavaScript app is certainly not an easy choice. I hope that this article gave you valuable insights to help you in this decision.

If you still feel hesitant, reach me out on Vulcan's Slack, I’d be glad to answer them :)

You can also direct any question on AUSK to Victor Vlasenko and his team at [SysGears](https://sysgears.com/), and join [Vulcan’s dedicated Slack](http://slack.telescopeapp.org/) to access the Vulcan community.

My last advice will be that simple: give both Vulcan and AUSK a shot, they are worth your time!

_Thanks to Sacha Greif and Victor Vlasenko for reviewing this article._

<a href="https://twitter.com/lbke_fr">
<img src="https://www.freecodecamp.org/news/content/images/2019/10/Medium-follow-2019.png" alt="LBKE banner twitter" />
</a>

---

I am the co-founder of the French company Lebrun Burel Knowledge Engineering (LBKE) —  [https://www.lbke.fr](https://www.lbke.fr)

_Always happy to talk about code, machine learning, innovation and entrepreneurship!_

