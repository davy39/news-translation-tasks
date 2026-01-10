---
title: The world’s easiest introduction to WebAssembly?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-28T15:28:38.000Z'
originalURL: https://freecodecamp.org/news/webassembly-with-golang-is-fun-b243c0e34f02
coverImage: https://cdn-media-1.freecodecamp.org/images/1*XLrgliUgUebeFCVrZ--o2g.jpeg
tags:
- name: Front-end Development
  slug: front-end-development
- name: golang
  slug: golang
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Martin Olsansky (olso)

  WASM in Golang for JavaScript developers.


  An interactive <canvas> laser game for cats ? on your phone ?written completely
  in Golang. Being inspected by Matsu ?


  Do you think that WebAssembly (WASM) is only used for image ma...'
---

By Martin Olsansky (olso)

#### WASM in Golang for JavaScript developers.

![Image](https://cdn-media-1.freecodecamp.org/images/1*XLrgliUgUebeFCVrZ--o2g.jpeg)
_An interactive &lt;canvas&gt; laser game for cats ? on your phone ?written completely in Golang. Being inspected by Matsu ?_

* Do you think that WebAssembly (WASM) is only used for image manipulation, hard math, or other niche use cases on the web?
* Are you still confusing WASM with `Web Workers` and `Service Workers`?
* Not interested because you think that JavaScript web apps being developed today will still need to be maintained for the next 10+ years?
* Do you want to do frontend web development in non-JS languages?

_For the skimmers, here are the links to [**demo**](https://olso.space/go-wasm-cat-game-on-canvas/index.html) or **/[src](https://github.com/olso/go-wasm-cat-game-on-canvas-with-docker)**_ ?. _“[Reading/writing is a transaction”,](http://www.perell.com/blog/coolest-things-2018#block-yui_3_17_2_1_1546345205921_226865) I’ll try not to waste your time. There are g`ists` with explanatory comments in the code._

### Storyline ?

Our goal is to create a simple game for cats ?: moving a red laser on mobile with some ? audio effects and vibrations. We will implement everything in Go[lang (](https://golang.org)Go), including DOM manipulation, logic, and state.

_Aaaaaand since, cats cannot use a mouse, we’ll need touch interaction for those cat paws ?._

#### Intro explained!

Think of WASM as the [Universal Virtual Machine](https://webassembly.org/docs/use-cases/) (sandbox), where you write ANY code once, and it runs everywhere.

WASM is a compile target, not a language. As if you were to compile for Windows, Mac OS, and Linux at once!

I don’t think that WASM is about dethroning JS, it’s about having alternatives without any sacrifices.

Imagine all the people that are developing in _Go, Swift, Rust, Ruby, C++, OCaml or others_. Now, they can use their preferred language to create an interactive, networked, fast, offline-capable websites and web apps.

Have you ever been part of a discussion about whether your project will be a mono-repo or a multi-repo?

**You’re now also going to have a discussion about whether your project is a mono-language or a multi-language.**

When people can work with the same tech stack, everything becomes easier. Especially communication between teams.

You can still use React, Vue but now you’re not forced to use JS anymore.

#### How is WASM different from the Service and Web Workers?

`Service & Web Workers` allow you to run background, offline & caching processes. They mimic threading, don’t have access to DOM and can’t share the data (only through messaging) and are running in a separate context. Heck, you could even run WASM instead of JS in them. To me, they only provide some abstraction layer with special privileges, nobody said that these layers have to execute JS.

> `_Service & Web Workers_` are a browser feature, they are not some exclusive JS feature.

### Setup the dev env ?

We’re going to use WASM, Go, JS and (optionally) Docker ?.

If you don’t know Go but know JS, [learn Go](https://nemethgergely.com/learning-go-as-a-nodejs-developer/) and then come back here. Let’s start by going to the [Go WASM wiki](https://github.com/golang/go/wiki/WebAssembly).

Use your local `go`, I’m using `golang:1.12-rc` Docker image. Just set two WASM flags for the `go` compiler here. Create a simple [hello world](https://gobyexample.com/hello-world) within `main.go` to test it.

```
$ GOOS=js GOARCH=wasm go build -o game.wasm main.go
```

Now, grab the `[wasm_exec.js](https://github.com/golang/go/blob/master/misc/wasm/wasm_exec.js)` glue provided by the Go team. This `Go` global abstracts WASM initiation. We don’t have to craft any DOM abstraction from scratch ?. Finally, f`etch` the .`wasm` file and run our game.

All in all, it should look like this:

### Show me the Go code already!

To render our simple game, `<canv`as> should be sufficient. We can create the DOM structure and elements right from the Go code! `[That sysc](https://github.com/golang/go/tree/master/src/syscall/js)`all/js (included as a standard Go package) handle`s t`he DOM interaction for us.

#### main()

I bet you haven’t seen `main()` in a long time ?.

Looks pretty similar to JS, doesn’t it?

Yes, that’s all you need to interact with the `DOM`! Just a few `Get` and `Call` functions for now.

![Image](https://cdn-media-1.freecodecamp.org/images/1*QBGaRFL9RDLQ-y2BnY5iDg.png)
_Oh mama ? It’s there!_

At this point, I was asking myself. I’m still kind of writing JS in some way… how is this an upgrade? Because we don’t have direct access to the DOM yet, we have to resort to calling the DOM (via JS) in order to do anything. Imagine how you could abstract this away with let’s say, JSX/React. _Actually, you already can, but let’s leave that for my next article_ ?.__

#### “Rendering” and the event handling

Directly using the `syscall/js` lib reveals some ES5-like callbacks. We are able to listen for the DOM events. Looks very clean with those static types!

#### Logging, Audio and “async”

In Go, there is a convention to write all the `func` in a sync way. It’s up to the caller to decide whether `func` is async. Making a `func` run asynchronously is really easy. Just prefix it with `go` and there you go! It creates a thread with its own context. You can still bind the parent context to it, don’t worry.

#### Running our game forever! ♾

That code creates an unbuffered channel, and attempts to receive from it. And since no-one ever sends anything on it, it’s essentially a blocking forever operation, allowing us to run our program forever.

#### Updating the game state and moving the red laser

No state management to see here, just a simple typed `struct`, that doesn’t allow you to pass any incorrect values inside.

### Conclusion

The fact that WASM is still considered an [MVP](https://hacks.mozilla.org/2018/10/webassemblys-post-mvp-future/) (MAP) and that you can create a game like this, without writing a single line of JS, is amazing! [CanIUse](https://caniuse.com/#feat=wasm) is already fully green, there is nothing stopping you from building WASM powered websites and apps.

Look, you can combine all the languages you want, event JS -> WASM. In the end, they’ll all compile down to the WASM bytecode. If you need to share anything between them, you can, because they can share a raw memory.

What I’m afraid of is, in recent news, we learned that [Microsoft is building a Chromium browser](https://news.ycombinator.com/item?id=18595069) and [Firefox market share is below 9%](https://news.ycombinator.com/item?id=18595025). This gives Google a kill switch power over WASM. If they don’t go with it, masses may never know.

![Image](https://cdn-media-1.freecodecamp.org/images/1*UGmDc4xve13Yws3WEe8Hrg.gif)
_Gameplay ?_

#### Who is using WASM already?

Agreed, my example just draws a full-page `canvas` . Here are more advanced examples that focus on the semantic web [awesome-wasm#web-frameworks-libraries](https://github.com/mbasso/awesome-wasm#web-frameworks-libraries).

Quite a few projects have jumped on the WASM train already. Some of the more interesting to me are Spotify, Twitch, [Figma](https://www.figma.com/blog/webassembly-cut-figmas-load-time-by-3x/) & [EWASM](https://github.com/ewasm).

#### WASM in the Web3 era

Nowadays, if you want to use some Ethereum wallet on the mobile web, you have to download a mobile wallet like Status.im from some centralized App Store and trust all the parties.

How about a Progressive Web App that would run `geth` (Go Ethereum client) with light sync over WebRTC? It could use `Service Worker` to update its WASM code and run in it the background, could be hosted on IPFS/Dat.

### Useful WASM articles, resources & goodies ?

* [WebAssembly is more than the web](https://words.steveklabnik.com/webassembly-is-more-than-just-the-web)
* [WebAssembly and Go: A look at the future](https://www.brianketelsen.com/web-assembly-and-go-a-look-to-the-future/) and the [HN comments](https://news.ycombinator.com/item?id=17381816)
* posts by [Mozilla Hacks](https://hacks.mozilla.org/category/webassembly) & [Hacker News](https://hn.algolia.com/?query=wasm&sort=byDate&prefix&page=0&dateRange=all&type=story)
* [WebAssembly architecture for Go](https://docs.google.com/document/d/131vjr4DH6JFnb-blm_uRdaC0_Nv3OUwjEY5qVCxCup4/edit)

[**awesome-wasm**](https://github.com/mbasso/awesome-wasm), [awesome-wasm-langs](https://github.com/appcypher/awesome-wasm-langs), [gowasm-experiments](https://github.com/stdiopt/gowasm-experiments), [**WasmWeekly**](https://twitter.com/wasmweekly), [WasmRocks](http://www.wasmrocks.com/), [SPA with C++](https://github.com/mbasso/asm-dom#examples), [better DOM bindings for Go](https://github.com/dennwc/dom)

Thanks to [https://github.com/twifkak](https://github.com/twifkak) for optimizing Go on the Chrome for Android!

### Next article? ✍️

We will take a look at interoperability with JS modules & React. Stay tuned!

_If you liked it and would like to see more content, don’t forget to follow and keep pressing that clap button_ ?.

### About me ⚡️

Hi, I’m **Martin Olsansky** _(olso)_. If you have any questions/suggestions, feel free to contact me at [**https://olso.space**](https://olso.space) or @[olso_uznebolo](https://twitter.com/olso_uznebolo)

I’m also interested in [DIYBio](http://sphere.diybio.org), [Tech-augmented ecosystems/plants](https://terra0.org/), [Open Patient Data & Digital Health](https://events.ccc.de/congress/2018/wiki/index.php/Session:Digital_Health_and_Patient_Data), Cryptocurrencies, Web3, P2P.

