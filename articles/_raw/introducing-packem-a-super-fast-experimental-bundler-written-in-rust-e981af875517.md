---
title: 'Introducing Packem: a super fast experimental bundler written in Rust'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-05-15T16:36:27.000Z'
originalURL: https://freecodecamp.org/news/introducing-packem-a-super-fast-experimental-bundler-written-in-rust-e981af875517
coverImage: https://cdn-media-1.freecodecamp.org/images/1*AP72bMDkd2rDgR4txJreIQ.png
tags:
- name: Bundler
  slug: bundler
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: Rust
  slug: rust
- name: TypeScript
  slug: typescript
seo_title: null
seo_desc: 'By Bukhari Muhammad

  Packem is an experimental precompiled JavaScript module bundler primarily implemented
  in Rust. It can also handle a variety of other file types like YAML/TOML, fragment
  shader files and a lot more. Checkout the website or the GitH...'
---

By Bukhari Muhammad

Packem is an experimental precompiled JavaScript module bundler primarily implemented in Rust. It can also handle a variety of other file types like YAML/TOML, fragment shader files and a lot more. Checkout the [website](https://packem.github.io/) or the [GitHub page](https://github.com/packem/packem) to quickly get started.

![Image](https://cdn-media-1.freecodecamp.org/images/qAPcGMSL2YG2dAXsQL0rzSN7vytigBv8HQd6)
_Packem’s logo. Always soothes me._

Packem resolves a module’s dependencies and rehydrates them into a module graph, a flat list containing module interfaces which are essentially **references to in-memory heap-based mutable data structures** containing special metadata of a module in the module graph.

Most of the business logic is abstracted into Rust using FFI bindings to enable low level interactions between both ends. The Rusty binaries are available as precompiled Node C/C++ addons in [Packem’s repo](https://github.com/packem/packem/tree/master/bin). A cloud-based CI is used to run a few scripts with pre-gyp installations, yielding OS-specific binaries with support for later Node versions (8, 9, 10).

This layer of Packem’s core is what is referred to as the **Logical Context (LC)**. All the other operations that are not _explicitly prioritized_ are regressed into Node’s general runtime, which in Packem’s terms is the **Runtime Context (RC)**. Read more on contexts [here](https://packem.github.io/docs/execution-contexts.html).

Theoretically, the module graph is kept flat to avoid common pitfalls that would lead to unnecessary traversals if a tree was used in place. This allows the RC to keep track of cases such as deep circular dependencies or heavily nested dynamic imports (code splitting), amongst others, appropriately with minimum performance implications or side effects as possible.

![Image](https://cdn-media-1.freecodecamp.org/images/Ig7Fy4kGltI7JTU9IqMpMBH7Gvq-ctV2z44f)
_An overview of the bundling cycle from contexts._

> More details can be found at Packem’s [README.md](https://github.com/packem/packem).

I’ve been having this idea in mind but never planned to execute it until I _joined forces_ with [Saddam M](https://www.freecodecamp.org/news/introducing-packem-a-super-fast-experimental-bundler-written-in-rust-e981af875517/undefined). It has really been in my interest to see module bundling as a concept safe for anyone to learn, understand and implement. Having people struggle with configurations, documentation and plugins was extremely horrendous and I’d like to take the chance to change that. With you. With Packem.

### Quick history

I took some time to exhaust most of the bundlers written in a non-JavaScript environment. I found out that most of them _forgot_ that they’re supposed to be a bundler and not a C/C++ library from the dark ‘ol 19s.

What I wanted was a bundler that does most of the heavy-lifting in a _close-to-the-metal_ language for the user without requiring any interaction with its internals. Then I found Rust. A smart and concise systems language that shows off some laudable features like a fearless concurrency model, type safety, and more! I would expect as much from using C/C++ but I’d rather stick with Rust since it’s pretty straightforward when it comes to memory management.

### Why another bundler?

So what’s the take here? Why do we need another build tool since we already have amazing ones like webpack, Parcel, Rollup, etc? I’ll take you along with a few reasons why. Perhaps you might have your own interests in having your development and production build times reduced heavily.

#### It’s 2019, we don’t need slow tools no more

Even though Packem is faster than webpack 4, **it is more than twice as fast as Parcel (with multicore compilation)**. In a benchmark test, we bundled [Lodash v4.17.1](https://lodash.com/docs/4.17.11) with both Packem and Parcel and this was the result:

> Never take any benches at face value. You can test it out for yourself [here](https://github.com/bukharim96/packem-lodash-test).

The reason why I didn’t bother benchmarking Parcel against webpack was because webpack 4 is profoundly faster than Parcel. I proved this fact by using [Sean T. Larkin](https://www.freecodecamp.org/news/introducing-packem-a-super-fast-experimental-bundler-written-in-rust-e981af875517/undefined)’s own benches and a thread to it on Twitter [can be found here](https://twitter.com/bukharim96/status/1099049693290680321?s=20).

#### Because we can. Anyone can, right?

Of course, what will make the most sense, is because _we can_. We had the idea of having faster bundle times with a Rusty interface either with FFI or WASM (was still unsure by then). FFI was more reasonable as far as speed and DX was concerned, so we went with having Packem implemented in Rust FFI bindings.

We experienced a few thread-related issues so we didn’t make much use of the available resources. As a result we used multiple node child processes (with [_node-worker-farm_](https://github.com/rvagg/node-worker-farm)_)_, the same technique Parcel uses for multicore compilation, but for larger module graphs since it adds a significant startup time on top of Node’s uptime when used with smaller module graphs.

### Configuration style

This was a tricky part. There were a lot of questions that needed a good answer to make up to picking the right configuration style. Static or dynamic? JSON/YAML/TOML? Our choice was based entirely on whether we **needed** Packem to:

1. Have a neater configuration style, and
2. Be agnostic of other custom user configurations like _.babelrc_ or _package.json_.

Bottomline, we proceeded with a static configuration style since we found it to be exactly what we needed. Something that could _declaratively tell Packem how to manage the bundle cycle_. All the limits to having a static configuration were made clear.

Another aspect of interest was the type of file we should use for the configuration. JSON that is more common to an overwhelming majority of JavaScript developers or YAML/TOML/XML-style which are less common but have their own advantage(s). A suggestion was still made for JSON support ([#5](https://github.com/packem/packem/issues/5)).

JSON just didn’t cut out because of all the unnecessary string quotes, curly & block braces, which makes sense since it’s a **data interchanging format**. An XML-ish approach deserves no respect with regards to being used as a configuration format since it makes things worse than JSON as far as unnecessary characters are concerned. TOML introduced a lot of new lines, and debugging nested options didn’t appear to be eye-appealing since we knew that Packem plugins could get really nesty.

The final winner was YAML! It was able to pass through all aspects of being a proper configuration format (for Packem at least). It:

1. Makes configuration painless.
2. Uses an elegant approach.
3. Is still familiar to the JavaScript eye
4. Was designed specifically for this use-case (configurations)_._

Here’s an example of a typical Packem configuration (_packem.config.yml)_. Check for yourself and think about writing the same content in a JSON/TOML/XML-ish style.

FYI, only the first two options are necessary! ?

#### Extending Packem

> This feature is not yet implemented.

Sometimes we might need to use a feature that **doesn’t yet exist**, **might not be implemented in Packem** or is **very specific to our project**. For that case, you’d have two ways of solving your needs:

1. [Create a Packem plugin](https://packem.github.io/docs/plugin-system.html) for your use case (which is the recommended option).
2. Build a custom RC on top of Packem’s binaries.

Using Rust gives us the chance to reform the LC into other binary formats, such as WebAssembly, which will enable Packem to exhibit multiple compile targets:

1. A NAPI-based C/C++ addon with platform-specific binaries required by Packem’s default RC.
2. A WebAssembly-based binary that is cross-platform and injected into the RC.
3. Packem’s default standalone which uses WebAssembly with a browser-compatible implementation of the RC.

> The last two are not yet on the radar since internal refactorings are still being sorted out.

The advanced guide is soon expected to show you how to **build a custom build tool using Packem’s binaries** to fit your own needs in case you need to use Packem outside the browser and Node environments. These binaries complete the entire graph generation, and duplicate filtering and other graph-related aspects. This means you can use your custom serializer, file watcher, plugin system, etc. It is much like how you can build your custom renderer over OpenGL.

1. You can still embrace [Packem’s plugin system](https://packem.github.io/docs/plugin-system.html) since it will allow you to integrate Packem’s ecosystem of plugins with your custom bundler.
2. If you’re uncertain whether or not you would need to build a custom bundler, know that you wouldn’t always need to. Please try filing an issue first.
3. It is a guarantee that these binaries will speed up your workflow depending on your specific use case(s).

#### Current state

* ✂ [Code Splitting](https://packem.github.io/docs/code-splitting.html) for development and production modes.
* ? Improved CLI (` — verbose`) for better information on bundling cycle.
* ? M[odule Interfaces](https://packem.github.io/docs/advanced-plugin-apis.html#module-interfaces) to allow easy manipulation of the module graph.
* ✔ Proper priority. Native functionalities fit perfectly into the LC. This means there is greater chances of speedy builds.
* ? Export N`ativeUtils` for external usage of native functionalities including g`enerateModuleGraph` which reruns the process of generating a module graph. It is heavy but still useful in cases where you’d need a clone of the current active module graph. Using it means doubling the build time, so use it with care.

#### What’s next?

These are the features we’re hoping to have soon in the upcoming releases. With your efforts we could **get bundling done the right way**. When Packem is at _1.0_, we’re expecting to have full support for all the features listed below and the others mentioned in [Packem’s roadmap](https://packem.github.io/docs/roadmap.html).

* A browser-compatible standalone of Packem with the LC in WebAssembly for closer integration with the underlying system. [Axel Rauschmayer](https://www.freecodecamp.org/news/introducing-packem-a-super-fast-experimental-bundler-written-in-rust-e981af875517/undefined) already [made a feature request](https://github.com/packem/packem/issues/1) to have a Node-compatible version in WASM. For the record, we’ll be working on both soon.
* Treeshaking, but advanced. Resolving named/unnamed imports and stripping dead code should be a breeze. This means you can use libraries like _lodash_ instead of _lodash-es_ without worrying whether your code will be **elided** or not.
* Auto Config. Like Zero Config, but defaults-oriented for extra flexibility.
* Advanced CLI options to make development with Packem a second nature.
* Better error reporting.
* More environment targets. Packem can only bundle for the browser as of now. Eventually, we expect to support Node CJS and other formats as well.
* More plugins. We need more plugins! Packem has a set of common plugins to get you started quicker. But to grow a community, we’ll need a great ecosystem of plugins. Check the [common plugins](https://packem.github.io/docs/common-plugins.html) available or the [plugins section](https://packem.github.io/docs/plugin-system.html) on the site to start developing a plugin right away.
* And much more…

#### Resources

* [Packem on GitHub](https://github.com/packem/packem/)
* [Roadmap and Feature Requests](https://packem.github.io/docs/roadmap.html)
* [Packem’s Official Site](https://packem.github.io/)
* [Creating Plugins with Packem](https://packem.github.io/docs/plugin-system.html)
* [Code Splitting with Packem](https://packem.github.io/docs/code-splitting.html)
* [The Module Graph](https://packem.github.io/docs/the-module-graph.html)

**Packem hasn’t reach _1.0_ yet**. If you have found Packem to be interesting at all to you, try contributing to Packem itself by creating plugins, updating the documentation, supporting us financially, representing Packem at conferences or any other means. We appreciate your efforts!

Happy bundling! ???

