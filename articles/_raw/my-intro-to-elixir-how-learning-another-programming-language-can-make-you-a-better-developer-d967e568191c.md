---
title: 'My intro to Elixir: how learning another programming language can make you
  a better developer'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-04T00:33:19.000Z'
originalURL: https://freecodecamp.org/news/my-intro-to-elixir-how-learning-another-programming-language-can-make-you-a-better-developer-d967e568191c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*-roj-FWdYdOaPvpF9qo-hw.jpeg
tags:
- name: Elixir
  slug: elixir
- name: learning
  slug: learning
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Nikolas O''Donnell

  I attended ElixirConf EU in Warsaw earlier this year. It was actually my first ever
  programming conference. My colleague was giving a talk about Elixir and Phoenix
  called ‘Phoenix and the World of Tomorrow’.

  Now, my background is...'
---

By Nikolas O'Donnell

I attended ElixirConf EU in Warsaw earlier this year. It was actually my first ever programming conference. My colleague was giving a talk about Elixir and Phoenix called ‘Phoenix and the World of Tomorrow’.

Now, my background is in JavaScript but my company is Elixir obsessed. Having taken a sip of the company kool-aid and seen what it can do — I’m pretty well converted.

JavaScript will always be my first language, and holds a special place in my heart. I’m still using, learning and very much part of the vibrant and growing JavaScript and React community.

Although I’ve been familiarizing myself with Elixir for work, I have come to see a great deal of value in learning another programming language.

It’s a similar experience with learning a new spoken language. You’re pushed outside of your comfort zone. Having to understand and reason in another way, even from another perspective.

Further, you often have to rebuild from first principles — which in turn can have the added benefits of breaking preconceived assumptions and limitations.

This is a healthy thing to do and ultimately we should be language, library, and framework agnostic.

Our job is not actually to write code, and certainly not to write a specific ‘language’ of code.

Rather, it is to solve problems for our companies, clients, and customers.

Having other languages, frameworks and coding paradigms at your disposal when solving a problem increases your chances of solving it in a better way. In addition, it makes you a more well-rounded programmer and valuable team member.

#### Exploring Elixir further

Elixir is a relatively new meta-programming language created by Jose Valim and launched in 2012.

The ‘meta’ part is not just me trying to be ‘hip’, ‘happening’ and ‘down with the cool kids’. It gives an extra piece of information to what Elixir is.

To explain more about Elixir, I guess I have to first talk a little bit about Erlang. This is because Elixir is built on top of Erlang (hence the “meta” part). It runs on the Erlang virtual machine, called the BEAM because of some acronym that I’d have to [DuckDuckGo](https://www.freecodecamp.org/news/my-intro-to-elixir-how-learning-another-programming-language-can-make-you-a-better-developer-d967e568191c/undefined) to find out.

Erlang was created by Joe Armstrong, Robert Virding, and Mike Williams, while they were working for Ericsson in the mid 1980’s.

Ericsson works within the telecommunications space. They had the problem of making software that was robust, fault tolerant, and asynchronous — so calls didn’t drop out!

Charged with this mission, these engineers created Erlang. The Danish engineer [Agner Krarup Erlang](https://en.wikipedia.org/wiki/Agner_Krarup_Erlang) is often cited as the namesake… though it’s also a pretty convenient choice for an **Er**icsson **Lang**uage (I’m on to you ಠ_ಠ).

Back to Elixir. Being a functional language, it is super nice to keep things all ordered, organized and readable.

This function does that specific task. This module does this set of functions. Neither really need to know what the other is doing. This modular design pattern makes it easier to keep a clean codebase.

It is actually considered a multi-paradigm language as it is functional, concurrent, distributed and process-orientated. Cool story — but what does any of that even mean?

* **Functional programming** uses functions (ideally ‘pure functions’ where the inputs and outputs are clearly declared) with no hidden values coming in or out to build the program. The goal is to remove side effects or unintended outputs from the code.
* **Concurrency** lets a program execute multiple computations at the same time. It doesn’t have to wait for one thing to finish before starting another. This is referred to as ‘blocking’ because the execution of the next item is blocked from running until the previous item is completed.
* **Distributed** describes how information is exchanged. In distributed systems, problems are broken down into smaller tasks. These are completed through exchanging messages. As these messages can be talking to each other across machines/networks, it is distributed.
* **Process-orientated** also reflects how problems are broken down into smaller tasks or processes and aims to keep separate the data structures from the processes that interact with them. The reason for wanting to do this is that it allows for programmers to be more assured of getting the result they expect.

This is what Elixir code looks like:

![Image](https://cdn-media-1.freecodecamp.org/images/1*I2Z7z9DnrvgDAf2gb1WY6w.gif)
_[https://marketplace.visualstudio.com/items?itemName=mjmcloug.vscode-elixir](https://marketplace.visualstudio.com/items?itemName=mjmcloug.vscode-elixir" rel="noopener" target="_blank" title=")_

Clean right, and quite readable — take note of the following pattern:

```elixir
defmodule <Module_name> do

 def <something> do
  
  <the things to do>
  |> {you can use the pipe operator (|>) to parse..}
  |> {the result from a function..}
  |> {as the fist argument to the next function..}
  |> {creating a 'pipeline' with a final output..} 
  |> {of the entire cross function calls!}
  
 end
 
end
```

#### But where is all the extra syntax?

Well, being a new language, it has the fortune gained from hind sight. The language borrows some of the best aspects of other languages. As mentioned, it is built on Erlang and is actually compatible — meaning you can use Erlang syntax in Elixir code.

It also leverages the clean syntax and code structure of Ruby — its creator having come from a Ruby background.

#### Phoenix

Phoenix is a web framework built for Elixir by Chris McCord. You can think of this as a way to bootstrap out a project. It is modular (thanks to Elixir). It is also super fast (thanks to Erlang), and ultimately very powerful.

You can use it as the API layer between your database and your front end. You can also easily use the HTML and CSS templates that come with Phoenix. You can use Brunch JS to inject these parts into your website/app.

Alternatively, you could also use a front-end framework like Ember or React to do the same — making it a ‘best of both worlds’ approach.

This is the talk my colleague Ley gave at ElixirConf EU that I mentioned earlier. It is well worth a watch, as it looks at the role Phoenix can play in the next billion users accessing the internet on < 3G devices:

So if you’re intrigued, why not take a sip of Elixir? I think you might just get hooked.

Though in any case, take a sip of something new. Move out of your programming comfort zone and challenge yourself to explore another language, perspective and way of thinking. What’s the worst that could happen...?

![Image](https://cdn-media-1.freecodecamp.org/images/1*x49mx2qULeZcmfooM7cCOA.gif)
_[https://gfycat.com/gifs/detail/fewalarmingcaiman](https://gfycat.com/gifs/detail/fewalarmingcaiman" rel="noopener" target="_blank" title=")_

