---
title: Unified Architecture – A Simpler Way to Build Full-Stack Apps
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-09T23:42:36.000Z'
originalURL: https://freecodecamp.org/news/full-stack-unified-architecture
coverImage: https://www.freecodecamp.org/news/content/images/2019/12/unified-architecture-2.jpg
tags:
- name: architecture
  slug: architecture
- name: full stack
  slug: full-stack
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Manuel Vila

  Modern full-stack apps – like single-page apps or mobile apps – usually have six
  layers


  data access

  backend model

  API server

  API client

  frontend model

  and user interface.


  By architecting in this way, you can achieve some characterist...'
---

By Manuel Vila

Modern full-stack apps – like single-page apps or mobile apps – usually have six layers
- data access
- backend model
- API server
- API client
- frontend model
- and user interface.

By architecting in this way, you can achieve some characteristics of a well-designed application, such as [separation of concerns](https://en.wikipedia.org/wiki/Separation_of_concerns) or [loose coupling](https://en.wikipedia.org/wiki/Loose_coupling).

But this does not come without drawbacks. It usually comes at the cost of other important characteristics, like simplicity, [cohesion](<https://en.wikipedia.org/wiki/Cohesion_(computer_science)>), and agility.

It seems we can't have it all. We have to compromise.

The problem is that developers usually build each layer as a completely different world on its own.

Even if you implement the layers with the same language, they cannot communicate with one another very easily.

You would need a lot of [glue code](https://en.wikipedia.org/wiki/Glue_code) to connect them all, and the [domain model](https://en.wikipedia.org/wiki/Domain_model) gets duplicated across the stack. As a result, your development agility suffers dramatically.

For example, adding a simple field to a model often requires modifying all the layers of the stack. This can feel a bit ridiculous.

Well, I've been thinking a lot about this problem recently. And I believe I've found a way out.

Here's the trick: for sure, the layers of an application must be "physically" separated. But they don't need to be "logically" separated.

## The Unified Architecture
<p>
	<img src="https://liaison-blog.s3.dualstack.us-west-2.amazonaws.com/images/traditional-vs-unified-architecture.svg" alt="Traditional vs unified architecture" style="width: 100%; margin-top: 1.5rem">
</p>

In object-oriented programming, when we use inheritance, we get some classes that can be seen in two ways: physical and logical. What do I mean by that?

Let's imagine we have a class `B` that inherits from a class `A`. Then, `A` and `B` can be seen as two physical classes. But logically, they are not separated, and `B` can be seen as a logical class that composes the properties of `A` with its own properties.

For example, when we call a method in a class, we don't have to worry if the method is implemented in this class or a parent class. From the caller perspective, there is only one class to worry about. Parent and child are unified into a single logical class.

How about applying the same approach to the layers of an application? Wouldn't it be great if, for example, the frontend could somehow inherit from the backend?

Doing so, frontend and backend would be unified into a single logical layer. And that would remove all communication and sharing issues. Indeed, backend classes, attributes, and methods would be directly accessible from the frontend.

Of course, we don't usually want to expose the whole backend to the frontend. But the same goes for class inheritance, and there is an elegant solution that is called "private properties". Similarly, the backend could selectively expose some attributes and methods.

Being able to grasp all the layers of an application from one single unified world is not a small deal. It changes the game completely. It is like going from a 3D world to a 2D world. Everything gets a lot easier.

[Inheritance is not evil](https://liaison.dev/blog/articles/Do-We-Really-Need-to-Separate-the-Model-from-the-UI-9wogqr#composition-over-inheritance). Yes, it can be misused, and in some languages, it can be pretty rigid. But when properly used, it is an invaluable mechanism in our toolbox.

We have a problem, though. As far as I know, there is no language allowing us to inherit classes across multiple execution environments. But we are programmers, aren't we? We can build everything we want, and we can extend the language to provide new capabilities.

But before we get to that, let's break down the stack to see how each layer can fit in a unified architecture.

### Data Access

For a majority of applications, the database can be abstracted using some sort of ORM. So, from the developer perspective, there is no data access layer to worry about.

For more ambitious applications, we might have to optimize database schemas and requests. But we don't want to clutter the backend model with these concerns, and this is where an additional layer may be appropriate.

We build a data access layer to implement the optimization concerns, and this usually happens late in the development cycle, if it ever happens.

Anyway, if we need such a layer, we can build it later. With cross-layer inheritance, we can add a data access layer on top of the backend model layer with almost no changes to the existing code.

### Backend Model

Typically, a backend model layer handles the following responsibilities:

- Shaping the domain model.
- Implementing business logic.
- Handling the authorization mechanisms.

For most backends, it's fine to implement them all in a single layer. But, if we want to handle some concerns separately, for example, we want to separate the authorization from the business logic, we can implement them in two layers that inherit from each other.

### API Layers

To connect the frontend and the backend, we usually build a web API (REST, GraphQL, etc.), and that complicates everything.

The web API must be implemented on both sides: an API client in the frontend and an API server in the backend. That's two extra layers to worry about, and it usually leads to duplicate the whole domain model.

A web API is nothing more than glue code, and it is a pain in the ass to build. So, if we can avoid it, that's a massive improvement.

Fortunately, we can take advantage of cross-layer inheritance again. In a unified architecture, there is no web API to build. All we have to do is to inherit the frontend model from the backend model, and we are done.

However, there are still some good use cases for building a web API. That's when we need to expose a backend to some third-party developers, or when we need to integrate with some legacy systems.

But let's be honest, most applications don't have such a requirement. And when they do, it is easy to handle it afterward. We can simply implement the web API into a new layer that inherits from the backend model layer.

Further information on this topic can be found in [this article](https://liaison.dev/blog/articles/How-about-interoperability-oy3ugk).

### Frontend Model

Since the backend is the source of truth, it should implement all the business logic, and the frontend should not implement any. So, the frontend model is simply inherited from the backend model, with almost no additions.

### User Interface

We usually implement the frontend model and the UI in two separate layers. But as I showed in [this article](https://liaison.dev/blog/articles/Do-We-Really-Need-to-Separate-the-Model-from-the-UI-9wogqr), it is not mandatory.

When the frontend model is made of classes, it is possible to encapsulate the views as simple methods. Don't worry if you don't see what I mean right now, it will become clearer in the example later on.

Since the frontend model is basically empty (see above), it is fine to implement the UI directly into it, so there is no user interface layer _per se_.

Implementing the UI in a separate layer is still needed when we want to support multiple platforms (e.g., a web app and a mobile app). But, since it is just a matter of inheriting a layer, that can come later in the development roadmap.

### Putting Everything Together

The unified architecture allowed us to unify six physical layers into one single logical layer:

- In a minimal implementation, data access is encapsulated into the backend model, and the same goes for UI that is encapsulated into the frontend model.
- The frontend model inherits from the backend model.
- The API layers are not required anymore.

Again, here's what the resulting implementation looks like:

<p>
	<img src="https://liaison-blog.s3.dualstack.us-west-2.amazonaws.com/images/traditional-vs-unified-architecture.svg" alt="Traditional vs unified architecture" style="width: 100%; margin-top: .5rem">
</p>

That's pretty spectacular, don't you think?

## Liaison

To implement a unified architecture, all we need is cross-layer inheritance, and I started building [Liaison](https://liaison.dev) to achieve exactly that.

You can see Liaison as a framework if you wish, but I prefer to describe it as a language extension because all its features lie at the lowest possible level — the programming language level.

So, Liaison does not lock you into a predefined framework, and a whole universe can be created on top of it. You can read more on this topic in [this article](https://liaison.dev/blog/articles/Getting-the-Right-Level-of-Generalization-7xpk37).

Behind the scene, Liaison relies on an [RPC](https://en.wikipedia.org/wiki/Remote_procedure_call) mechanism. So, superficially, it can be seen as something like [CORBA](https://en.wikipedia.org/wiki/Common_Object_Request_Broker_Architecture), [Java RMI](https://en.wikipedia.org/wiki/Java_remote_method_invocation), or [.NET CWF](https://en.wikipedia.org/wiki/Windows_Communication_Foundation).

But Liaison is radically different:

- It is not a [distributed object system](https://en.wikipedia.org/wiki/Distributed_object). Indeed, a Liaison backend is stateless, so there are no shared objects across layers.
- It is implemented at the language-level (see above).
- Its design is straightforward and it exposes a minimal API.
- It doesn't involve any boilerplate code, generated code, configuration files, or artifacts.
- It uses a simple but powerful serialization protocol ([Deepr](https://deepr.io)) that enables unique features, such as chained invocation, automatic batching, or partial execution.

Liaison starts its journey in JavaScript, but the problem it tackles is universal, and it could be ported to any object-oriented language without too much trouble.

### Hello Counter

Let's illustrate how Liaison works by implementing the classic "Counter" example as a single-page application.

First, we need some shared code between the frontend and the backend:

```js
// shared.js

import {Model, field} from '@liaison/liaison';

export class Counter extends Model {
  // The shared class defines a field to keep track of the counter's value
  @field('number') value = 0;
}
```

Then, let's build the backend to implement the business logic:

```js
// backend.js

import {Layer, expose} from '@liaison/liaison';

import {Counter as BaseCounter} from './shared';

class Counter extends BaseCounter {
  // We expose the `value` field to the frontend
  @expose({get: true, set: true}) value;

  // And we expose the `increment()` method as well
  @expose({call: true}) increment() {
    this.value++;
  }
}

// We register the backend class into an exported layer
export const backendLayer = new Layer({Counter});
```

Finally, let's build the frontend:

```js
// frontend.js

import {Layer} from '@liaison/liaison';

import {Counter as BaseCounter} from './shared';
import {backendLayer} from './backend';

class Counter extends BaseCounter {
  // For now, the frontend class is just inheriting the shared class
}

// We register the frontend class into a layer that inherits from the backend layer
const frontendLayer = new Layer({Counter}, {parent: backendLayer});

// Lastly, we can instantiate a counter
const counter = new frontendLayer.Counter();

// And play with it
await counter.increment();
console.log(counter.value); // => 1
```

What's going on? By invoking `counter.increment()`, we got the counter's value incremented. Notice that the `increment()` method is neither implemented in the frontend class nor in the shared class. It only exists in the backend.

So, how is it possible that we could call it from the frontend? This is because the frontend class is registered in a layer that inherits from the backend layer. So, when a method is missing in the frontend class, and a method with the same name is exposed in the backend class, it is automatically invoked.

From the frontend point of view, the operation is transparent. It doesn't need to know that a method is invoked remotely. It just works.

The current state of an instance (i.e., `counter`'s attributes) is automatically transported back and forth. When a method is executed in the backend, the attributes that have been modified in the frontend are sent. And inversely, when some attributes change in the backend, they are reflected in the frontend.

> Note that in this simple example, the backend is not exactly remote. Both the frontend and the backend run in the same JavaScript runtime. To make the backend truly remote, we can easily expose it through HTTP. See an [example here](https://github.com/liaisonjs/liaison/tree/master/examples/counter-via-http/src).

How about passing/returning values to/from a remotely invoked method? It is possible to pass/return anything that is serializable, including class instances. As long as a class is registered with the same name in both the frontend and the backend, its instances can be automatically transported.

How about overriding a method across the frontend and the backend? It is no different than with regular JavaScript – we can use `super`. For example, we can override the `increment()` method to run additional code in the context of the frontend:

```js
// frontend.js

class Counter extends BaseCounter {
  async increment() {
    await super.increment(); // Backend's `increment()` method is invoked
    console.log(this.value); // Additional code is executed in the frontend
  }
}
```

Now, let's build a user interface with [React](https://reactjs.org/) and the encapsulated approach shown earlier:

```js
// frontend.js

import React from 'react';
import {view} from '@liaison/react-integration';

class Counter extends BaseCounter {
  // We use the `@view()` decorator to observe the model and re-render the view when needed
  @view() View() {
    return (
      <div>
        {this.value} <button onClick={() => this.increment()}>+</button>
      </div>
    );
  }
}
```

Finally, to display the counter, all we need is:

```js
<counter.View />
```

Voilà! We built a single-page application with two unified layers and an encapsulated UI.

### Proof of Concept

To experiment with the unified architecture, I built a [RealWorld example app](https://github.com/liaisonjs/react-liaison-realworld-example-app) with Liaison.

I might be biased, but the outcome looks pretty amazing to me: simple implementation, high code cohesion, 100% [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself), and no glue code.

In terms of the amount of code, my implementation is significantly lighter than any other one I have examined. Check out the [results here](https://github.com/liaisonjs/react-liaison-realworld-example-app/blob/master/docs/comparison.md).

Certainly, the RealWorld example is a small application, but since it covers the most important concepts that are common to all applications, I'm confident that a unified architecture can scale up to more ambitious applications.

## Conclusion

Separation of concerns, loose coupling, simplicity, cohesion, and agility.

It seems we get it all, finally.

If you are an experienced developer, I guess you feel a bit skeptical at this point, and this is totally fine. It is hard to leave behind years of established practices.

If object-oriented programming is not your cup of tea, you will not want to use Liaison, and this is totally fine as well.

But if you are into OOP, please keep a little window open in your mind, and the next time you have to build a full-stack application, try to see how it would fit in a unified architecture.

[Liaison](https://liaison.dev/) is still at an early stage, but I am actively working on it, and I expect to release the first beta version in early 2020.

If you are interested, please star the [repository](https://github.com/liaisonjs/liaison) and stay updated by following the [blog](https://liaison.dev/blog) or subscribing to the [newsletter](https://liaison.dev/#newsletter).

_Discuss this article on [Changelog News](https://changelog.com/news/how-to-simplify-fullstack-development-with-a-unified-architecture-XVOM)_.


