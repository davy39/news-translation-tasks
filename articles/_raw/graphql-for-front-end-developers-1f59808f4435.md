---
title: A guide to GraphQL for front-end developers
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-17T21:20:07.000Z'
originalURL: https://freecodecamp.org/news/graphql-for-front-end-developers-1f59808f4435
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ATRODaaXUt35esV1CCFvwg.png
tags:
- name: Front-end Development
  slug: front-end-development
- name: GraphQL
  slug: graphql
- name: JavaScript
  slug: javascript
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Schalk Venter

  10 months ago, Artsy Engineering Lead, Alan Johnson proclaimed that ‘I have seen
  the future, and it looks a lot like GraphQL’.

  Fast-forward to exactly 13 days before I started this article, and Wired Magazine
  publishes a story title ...'
---

By Schalk Venter

**10 months ago, [Artsy](https://www.artsy.net/) Engineering Lead, [Alan Johnson](http://artsy.github.io/author/alan/) proclaimed that [‘I have seen the future, and it looks a lot like GraphQL](http://artsy.github.io/blog/2018/05/08/is-graphql-the-future/)’.**

**Fast-forward to exactly 13 days before I started this article, and [Wired Magazine](https://www.wired.com) publishes a story title [_How Facebook has changed computing_](https://www.wired.com/story/how-facebook-has-changed-computing/), highlighting [GraphQL](https://graphql.org/) as one of the technologies that ‘_played a tremendous role in shifting not only in the way we build our servers but also how we write code_’.**

These are bold claims! I am by no means qualified to counter nor concur them. However, for me, the above is indicative of how astronomically fast the GraphQL eco-system has grown over the past two years - regardless of whether we think this is for better or [for worse](https://news.ycombinator.com/item?id=13480049).

This growth is also reflected in my day-to-day experience as a developer. Internally at [OpenUp](https://openup.org.za), our team has been steadily adopting GraphQL in more and more of our products, due to it solving a lot of [pain-points usually associated with the REST API endpoints](https://www.howtographql.com/basics/1-graphql-is-the-better-rest/). Furthermore, we are not alone. GraphQL is widely used by a range of international tech teams from [Pinterest](https://pinterest.com), [Twitter](https://twitter.com/), [Yelp](https://www.yelp.com/developers/graphql/guides/intro), [New York Times](https://www.nytimes.com/), [Paypal](https://www.paypal.com), [Atlassian](https://www.atlassian.com/), [Facebook](https://code.fb.com/core-data/graphql-a-data-query-language/), [Github](https://developer.github.com/v4/) ([amongst others](https://graphql.org/users/)); and fellow South African startups like [GetTruck](https://gettruck.co.za), [Bettr](https://bettr.finance) and [Dine4Six](https://dine4six.com).

After reading the above Wired article I reflected on my own (sometimes turbulent) journey through GraphQL, and I thought that it might be of value to compile a (hopefully!) easy guide for other front-end developers interested in getting started (and avoiding common pitfalls) learning GraphQL.

I’ve broken the below into the following broad topics, so feel free to skip ahead if you are only interested in a specific aspect of GraphQL:

* [My own journey learning GraphQL](#9a35)
* [So what exactly is GraphQL?](#20c2)
* [What problem is GraphQL trying to solve?](#e61e)
* [The GraphQL equivalent of ‘Hello World!’](#156a)
* [In what order should I learn GraphQL concepts?](#fbef)
* [What about the back-end?](#35cc)

### My own journey learning GraphQL

**When I first heard about GraphQL I’ve been playing around with this thing called [React](https://reactjs.org/) for a while. I’ve used a bit of [Backbone](http://backbonejs.org/) and [AngularJS](https://angularjs.org/) before, but neither really stuck with me.**

However, I was extremely excited by React’s [functional approach](https://en.wikipedia.org/wiki/Functional_programming) to state management and the usage of a [Virtual DOM](https://reactjs.org/docs/faq-internals.html) to reduce the performance footprint of intensive DOM manipulations. By this time I’ve essential hand-rolled my own [HyperScript](https://github.com/hyperhype/hyperscript)-esque helper function to do the above and was looking forward to getting rid of the latter abomination in favour of `React.createClass()` and `React.createElement()` .

Before giving the above a spin in a production environment I thought it wise to ask a senior team member what he thinks of this React thing. Yet, no good (or perhaps prudent) deed goes unpunished: I was berated with the usual disdain held by a lot of back-end developers at that point (and for some even still today) towards JavaScript frameworks. However (and perhaps as a gesture of goodwill), he did mention that this GraphQL thing (that the team behind React is working on) looks really promising.

Which lead me to the following:

* **Googling GraphQL.**
* **Reading a couple of overviews.**
* **Still having no idea what GraphQL is.**
* **Assuming that it’s probably aimed at web developers with at least one (or multiple) computer science degrees (I guess the way I still feel about [Web Assembly](https://webassembly.org/) and [Houdini](https://github.com/w3c/css-houdini-drafts))**
* **Going on with my life.**

A couple of years later, after being sucked in by the gravitational pull of the front-end supernova that has become the React ecosystem, I started playing around with another tool called [Gatsby](https://www.gatsbyjs.org/). I’ve been struggling to get [React Helmet](https://www.npmjs.com/package/react-helmet) to play nice with my own Frankenstein React static site generator built on top of [static-site-generator-webpack-plugin](https://github.com/markdalgleish/static-site-generator-webpack-plugin).

I actually found a message in the `#react` [Slack](https://slack.com/) channel on [ZA Tech](https://zatech.github.io/) that nicely encapsulates the frustration I felt at that time:

> **September 14th, 2017**

> Schalk Venter 4:02 PM  
> I might be missing something obvious here _?_

> Schalk Venter 4:38 PM  
> However, either I’m misunderstanding the documentation or server-side rendering is not as easy as they make it out in the docs. _?_

So this Gatsby-thing seemed to give me what I was trying to hack together by other means. However, I was met with further frustration as I came to realise that Gatsby is in cahoots with my previous nemesis, GraphQL (as a means to query front-matter and textual content from [Markdown](https://en.wikipedia.org/wiki/Markdown) files). However, going back to my Frankenstein-mess really didn’t seem to be compelling either.

_Turns out I really didn’t have a choice but to learn GraphQL at this point._

This meant that I needed to find answers to the following:

* [So what exactly is GraphQL?](#20c2)
* [What problem is GraphQL trying to solve?](#e61e)
* [The GraphQL equivalent of ‘Hello World!’](#156a)
* [In what order should I learn GraphQL concepts?](#fbef)
* [What about the back-end?](#35cc)

### So what exactly is GraphQL?

> “I have seen the future, and it looks a lot like GraphQL. Mark my words: in 5 years, newly minted full-stack app developers won’t be debating _RESTfulness_ anymore, because REST API design will be obsolete. […] It lets you model the resources and processes provided by a server as a domain-specific language (DSL). Clients can use it to send scripts written in your DSL to the server to process and respond to as a batch.”

> — [Alan Johnson](http://artsy.github.io/author/alan/) ([Is GraphQL The Future?](http://artsy.github.io/blog/2018/05/08/is-graphql-the-future/))

**_Yikes,_ that probably wasn’t the answer that I (nor you, dear reader) were looking for!**

#### Domain-what-a-thing?

However, as scary as the above definition seems, it is important to unpack it a bit if we want to get to the root of what exactly GraphQL is.

_Let’s start with the term ‘domain-specific language’_:

1. **First and foremost,** a domain-specific language (also called a _mini-language_) is a programming language created to express a very specific and predefined type of digital information (a domain). Whereas a [general purpose language](https://en.wikipedia.org/wiki/General-purpose_programming_language) like [JavaScript](https://en.wikipedia.org/wiki/JavaScript) can (similar to a Swiss army knife) be used to express a range of digital information ([and in some cases, even information that its creators didn’t anticipate at inception](http://www.jsfuck.com/)). This includes everything from low-level primitives like [objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object), [functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function), [strings](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String), [symbols](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol) to general programming patterns like [HTTP requests](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods), [DOM](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model) manipulations and/or [online data storage](https://developer.mozilla.org/en-US/docs/Web/API/Web_Storage_API)). Domain-specific languages tend to be more limited (and intentionally so) in what they are able to express when compared to general-purpose programming languages.
2. **Secondly,** DSL’s are often plugged into other DSL’s or general purpose languages to piggyback on existing functionality (due to their limited scope). However, this does not mean that DSL’s are tied to specific languages (GraphQL being an example of this). For example, the (more or less defunct now) [XForms](https://en.wikipedia.org/wiki/XForms) DSL can be used inside [HTML](https://en.wikipedia.org/wiki/HTML) (which itself is a DSL on top of another DSL called [SGML](https://en.wikipedia.org/wiki/Standard_Generalized_Markup_Language)), while at the same time it can also be used in a general purpose language like [Java](https://en.wikipedia.org/wiki/Java_(programming_language)).

**_Is this getting a bit too nerdy?_**

Right, let’s bring it back! You probably have more experience with DSL’s than you realise (and not only through HTML!), but one or more of the following:

* [_CSS_](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
* [_JSON_](https://en.wikipedia.org/wiki/JSON)
* [YAML](https://en.wikipedia.org/wiki/YAML)
* [_XML_](https://en.wikipedia.org/wiki/XML)

Furthermore, you probably already have first-hand experience of their narrow scope. Most people will roll their eyes if I attempt to manage a database by means of HTML or [control a spacesuit](https://foundation.nodejs.org/wp-content/uploads/sites/50/2017/09/Node_CaseStudy_Nasa_FNL.pdf) via CSS.

#### The real value of DSL’s

**However, because of their very narrow scope, DSL’s tend to be extremely expressive (in other words, easy to read and write) compared to general purpose languages.**

_As an exampl_e:

A friend (and ex-colleague) of mine, [Greg Kempe](https://www.freecodecamp.org/news/graphql-for-front-end-developers-1f59808f4435/undefined) uses a DSL called [Akoma Ntoso](http://www.akomantoso.org/) (built on [XML](https://en.wikipedia.org/wiki/XML)) in his non-profit project called [Open By-laws](https://openbylaws.org.za). Akoma Ntoso (meaning ‘_linked hearts_’ in [Akan](https://en.wikipedia.org/wiki/Akan_language)) is a DSL built exclusively to express parliamentary, legislative and judiciary documents in a digital manner.

For example, see below a section of [the city of Cape Town’s outdoor signage by-law](https://openbylaws.org.za/za-cpt/act/by-law/2001/outdoor-advertising-signage/eng/) (expressed in Akoma Ntoso):

#### Bringing this back to front-end development

To illustrate the above in the context of front-end development we can look at a common example where we update our website’s [Document Object Model](https://en.wikipedia.org/wiki/Document_Object_Model) (DOM) via [JavaScript](https://en.wikipedia.org/wiki/JavaScript) (in order to show a specific message when a user is logged in):

You can see it in action inside the following Codepen example:

As powerful as JavaScript (even with the above ES6 syntax is), it isn’t very expressive when working with the DOM. Fortunately, there is a DSL specifically designed to better express browser DOM nodes. You might know it as HTML (or by the full name: Hypertext Markup Language).

This means that we can use the `innerHTML` property (only added to JavaScript back with [_Internet Explorer 4_](https://en.wikipedia.org/wiki/Internet_Explorer_4)) to re-write the above. The `innerHTML` property accepts a string written in HTML DSL:

As you can see we still get the exact same behaviour:

#### One last thing

Lastly, before we get into the GraphQL DSL itself, it might be of value to draw a distinction between DSL’s and [superset](https://en.wikipedia.org/wiki/Subset) languages like [TypeScript](https://en.wikipedia.org/wiki/TypeScript) or [Sass](https://en.wikipedia.org/wiki/Sass_(stylesheet_language)). While a superset language is meant to extend an existing language’s grammar, a DSL does not need to adhere to any underlying language or environment. For example, [JSX](https://en.wikipedia.org/wiki/React_(JavaScript_library)#JSX) (built on top of [XML](https://en.wikipedia.org/wiki/XML)) can be used to either interface directly with the browser DOM or a [mobile operating system](https://en.wikipedia.org/wiki/Mobile_operating_system) in the form of a [mobile app](https://en.wikipedia.org/wiki/Mobile_app) (by means of [React Native](https://facebook.github.io/react-native/)).

_Stop before you type that angry reply! I’m aware that the above distinction between DSLs/general purpose languages and DSLs/superset languages is fuzzy in a lot of cases, and (much like the disputed difference between websites and webapps) is subject to the [Sorites paradox](http://Sorites paradox). However, as is true with all cases of the Sorites paradox, fuzzy distinctions exist (in spite of their lack of scientific rigour) specifically because of the value they provide when explaining the nature of day-to-day experiences. So let’s merely call the above definition this article’s [working definition](https://en.wiktionary.org/wiki/working_definition) of DSLs._

### What problem is GraphQL trying to solve?

Similar to the above, GraphQL was created internally by the [tech team behind Facebook](https://github.com/facebook) in 2012 as a DSL to write more expressive (and powerful) data queries in the Facebook mobile app (to a remote data API).

![Image](https://cdn-media-1.freecodecamp.org/images/1*ikw1LeJXVlyPGxA7C0_svQ.png)

**The problem: Common [REST (or Representational State Transfer) API](https://en.wikipedia.org/wiki/Representational_state_transfer) approaches mostly rely on fixed data structures. This means that after enough iteration, most REST API’s end up requiring a [Lernaean Hydra](https://en.wikipedia.org/wiki/Lernaean_Hydra) of queries to get a specific piece of data.**

In short (as noted by [Chimezie Enyinnaya](https://blog.pusher.com/author/mezie/), a Nigerian content creator for [Pusher](https://pusher.com/) — a service that manages remote pub/sub messaging):

> “With REST, we might have a `/authors/:id` endpoint to fetch an author, then another `/authors/:id/posts` endpoint to fetch the post of that particular author. Lastly, we could have a `/authors/:id/posts/:id/comments` endpoint that fetches the comments on the posts. […] It is easy to fetch more than the data you need with REST, because each endpoint in a REST API has a fixed data structure which it is meant to return whenever it is hit.”

> — [Chimezie Enyinnaya](https://blog.pusher.com/author/mezie/) ([REST versus GraphQL](https://blog.pusher.com/rest-versus-graphql/))

In fact, this is so common that GraphQL is just one of several solutions that were conjured up to solve this problem:

> “Interestingly, other companies like Netflix or Coursera were working on comparable ideas to make API interactions more efficient. Coursera envisioned a similar technology to let a client specify its data requirements and Netflix even open-sourced their solution called Falcor.”

> — [How to GraphQL](https://www.howtographql.com) ([GraphQL fundamentals: Introduction](https://www.howtographql.com/basics/0-introduction/))

However, contrary to some of the above, GraphQL was released three years later under the [MIT license](https://en.wikipedia.org/wiki/MIT_License) and today forms the backbone behind open-source services like [Apollo](https://www.apollographql.com/) (using GraphQL to read and/or change both local and remote app state) or even [Gatsby](https://www.gatsbyjs.org/) (using GraphQL to query front-matter and textual content from markdown files).

**So without further ado, let’s get to the meat of this section: A real-world working example that actually illustrates how GraphQL solves the above problem.**

For argument's sake, let’s say that I want to know the [number of users following me on Github](https://github.com/schalkventer?tab=followers). We can easily retrieve the data via the native JavaScript fetch method (from the [Github REST API](https://developer.github.com/v3/)), and then display a list of usernames in the DOM via an unordered list (by means of the `innerHTML` example illustrated above):

**Surprisingly straightforward right?**

However, getting a list of followers doesn’t really tell us much. We want to get a sense of how prominent these users are on Github (since a follow from [Dan Abramov](https://twitter.com/dan_abramov) should be weighed differently than a follow from Johnny the team intern). In order to accomplish this, I will be using the extremely unscientific concept, which I henceforth deem _Github Equity_™ (similar to the search engine concept of [Link Equity](https://moz.com/learn/seo/what-is-link-equity)). _Github Equity_™ will be calculated by means of the total repositories maintained by a user and their own amount of followers.

In short:

`Total Repositories * Total Followers`

**Pretty easy! However, getting the data required to perform this calculation is a bit trickier since it would require several asynchronous requests REST queries (requiring some orchestration by means of [native JavaScript Promises](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)):**

As data queries go the above is still well within the bounds of what would be considered reasonable. However, all the required REST API calls (running in parallel!) make the code extremely hard to read and modify. This means that even if we only get the needed information from the first 10 followers, it would amount to a total of 31 REST API calls. Meaning that we quickly run into the [default Github API rate limit](https://developer.github.com/apps/building-github-apps/understanding-rate-limits-for-github-apps/) (a limit on the amount of request the API accepts from a specific IP in the span of an hour)

You can see this happening in the below [Codepen](https://codepen.io/schalkventer/pen/ef4598c518037d83bb006529a2d7ad30), where it should output the following error to the DOM if run a couple of times in a single hour (click the `rerun` button in the bottom right corner a couple of times) : `TypeError: response.map is not a function`. In other words, the API did not return the required array (since `.map()` can only be run on [iterables in JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols)):

Lucky for us (in addition to the above REST API) Github also [exposes a GraphQL endpoint](https://developer.github.com/v4/) by means of the following: `[https://api.github/graphql](https://api.github/graphql.)`[.](https://api.github/graphql.) This means that we can re-write the above as follows in the GraphQL DSL:

If you haven’t encountered GraphQL before the above might look a bit bewildering. However, we’ll unpack the syntax a bit in the upcoming section.

_As an aside, we are doing a very low-level/hand-rolled implementation of GraphQL for illustrative purposes. When encountering GraphQL in the wild you will most probably encounter it by means of [Apollo](https://www.apollographql.com/) (developed by the team behind [Meteor](https://www.meteor.com/)) or [Relay](https://facebook.github.io/relay/) (developed by the team behind [Facebook](https://www.facebook.com/)). These libraries are essentially just tooling that makes it easier to work with GraphQL on the client-side._

### The GraphQL equivalent of ‘Hello World!’

**Queries and Subscriptions and Mutations, Oh my!**

Personally for me, when I’m just starting out with a new programming language (even if it’s a DSL like GraphQL) there is often (what seems like) an impossible amount of information to take in. In order to make this process a bit more manageable, I (without fail) always start with the same question: What is to the ‘Hello World!’ equivalent of this language (often followed by what is the To-do app equivalent of this language).

In short:

> A “Hello, World!” program generally is a computer program that outputs or displays the message “Hello, World!”. Because it is very simple in most programming languages, it is often used to illustrate the basic syntax of a programming language and is often the first program that those learning to code write.

> A “Hello, World!” program is traditionally used to introduce novice programmers to a programming language.

> — [Wikipedia](https://en.wikipedia.org) (["Hello, World!” program](https://en.wikipedia.org/wiki/%22Hello,_World!%22_program))

**So what is the ‘Hello World!’ equivalent in GraphQL?**

According to Julian Mayorga in his book, [Fullstack GraphQL](https://www.graphql.college/fullstack-graphql/), ‘_In its simplest form, GraphQL is all about asking for specific fields of objects_’. Something called c_lient‐specified queries in_ the [original 2015 GraphQL spec](https://facebook.github.io/graphql/July2015/):

> These queries are specified at field‐level granularity. In the majority of client‐server applications written without GraphQL, the server determines the data returned in its various scripted endpoints. A GraphQL query, on the other hand, returns exactly what a client asks for and no more.

> — [GraphQL Working Draft (July 2015](https://facebook.github.io/graphql/July2015/))

However, what separates a GraphQL ‘Hello World!’ from (for example) a JavaScript `console.log('Hello World!')` is that we need to connect our query to something that is queryable.

Luckily there are [several public GraphQL endpoint](https://github.com/APIs-guru/graphql-apis)s available on the internet. From a Stanford University endpoint that allows one [to query HIV drug resistance data](https://hivdb.stanford.edu/page/graphiql/) to an endpoint that houses a collection of [public demographic information arranged by country](https://countries.trevorblades.com/).

However, let us direct our gaze on the pinnacle of human technological achievement: a [Pokéapi](https://graphql-pokemon.now.sh) that supplies _‘ all the Pokémon data you’ll ever need’._

As a warm-up exercise lets create the following query ([you can follow along if you want](https://graphql-pokemon.now.sh/?query=%7B%0A%20%20pokemons%20(first%3A%2020)%20%7B%0A%20%20%20%20name%0A%20%20%7D%0A%7D)):

```
{  pokemons (first: 20) {    name  }}
```

**_Meh!_** That was quite underwhelming: a list of 20 Pokemon from the [Pokedex](https://pokedex.org/). However, let’s turn it up a notch and find something more specific (which if you remember correctly is where GraphQL really shines!).

To make it interesting let’s say that we want to determine the average weight of [Pikachu](https://pokedex.org/#/pokemon/25)’s final evolution (spoiler: it’s [Raichu](https://pokedex.org/#/pokemon/26)). We can use the following query ([link to live example](https://graphql-pokemon.now.sh/?query=%7B%0A%20%20pokemon(name%3A%20%22Pikachu%22)%20%7B%0A%20%20%20%20evolutions%20%7B%0A%20%20%20%20%20%20name%0A%20%20%20%20%20%20weight%20%7B%0A%20%20%20%20%20%20%20%20minimum%0A%20%20%20%20%20%20%20%20maximum%0A%20%20%20%20%20%20%7D%0A%20%20%20%20%7D%0A%20%20%7D%0A%7D)):

It is important to note that the above query is essentially shorthand for the following:

```
query GetPikachuEvolutionWeight {  pokemon(name: "Pikachu") {    evolutions {      weight {        minimum        maximum      }    }  }}
```

The fact that GraphQL assumes you will be doing a query even when you don’t specify an action shows how central queries are to GraphQL.

Regardless, no matter which of the above we use, we will get the following JSON response from the endpoint:

This means that we can just run our `parse()` function (from the above example) on this JSON response, and output the result (29.5) to the DOM.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ATRODaaXUt35esV1CCFvwg.png)

**In short, it can be said that queries are little maps in the form of Strings ([no, not this kind](https://www.lovelyetc.com/diy-map-string-art/)!) used by GraphQL to navigate a data-structure to find all requested items in a single journey.**

This means that we can (for the fun of it) write a similar set of real-world instructions in the GraphQL DSL:

### In what order should I learn GraphQL concepts?

Thus far we’ve only touched on queries. However (and perhaps surprisingly), you can get pretty far with GraphQL by just understanding the above. However, there are several additional concepts that you might want to look into if you want to use GraphQL to its full potential:

Additional tooling/concepts used by GraphQL queries:

1. [**Fields**](https://www.apollographql.com/docs/resources/graphql-glossary.html#field): This is the items in a query that at face-value resemble keys in a JavaScript object. For example `paper` , `post_office` and `travel` in the above example.
2. [**Arguments**](https://www.apollographql.com/docs/resources/graphql-glossary.html#argument): Optional information we can pass to fields. For example `type: drive` and `amount: 12` in our example above.
3. [**Aliases**](https://www.apollographql.com/docs/resources/graphql-glossary.html#alias): A custom name that should be used for the JavaScript key to which a field resolves. By default, the object key is the same name as the field. For example in the above `post_office` will resolve to `{ post_office: { ... } }` . However, we can alias it as follows: `postOffice: post_office` , which will return `{ postOffice: { ... } }` . Not only is this useful if we want to make the key more semantic or change the casing, but this is also useful when we are using the same field twice (to prevent the default key of the second `post_office` from overriding the first `post_office` value.
4. [**Variables**](https://www.apollographql.com/docs/resources/graphql-glossary.html#variable)**:** When I first started using GraphQL, I did what any reasonable developer would do. I just used dynamic interpolation in the query (expressed through a [template literal](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals)). In other words, I would do the following for our Pokemon example above: `pokemon (name: "${dynamicValue)")`. Much to the shock of fellow GraphQL developers (since I’m essentially creating side-effects all over the place)! Turns out that GraphQL has built-in functionality to pass external values into a query. By declaring the variable at the query root. For example with `query GetPokemonEvolutionWeight($name: string)` and `pokemon (name: $name)` we can simply pass an object of variables to the query when it gets called (i.e. `{ name: 'Pikachu' }` . Note that you need to assign one of the [core GraphQL scalar types](https://www.apollographql.com/docs/apollo-server/schemas/types.html) to a variable (for example we used `string` above). It is possible to create your own custom types, but this is outside of the scope of this article.

Furthermore, you might also be interested in venturing past queries only (covered in this article) into more advanced GraphQL features:

* [**Mutations**](https://graphql.org/graphql-js/mutations-and-input-types/): Thus far we’ve only been fetching data via GraphQL. However, it is also possible to send data via GraphQL. This is done via Mutations, which are the GraphQL equivalent of [POST](https://en.wikipedia.org/wiki/POST_(HTTP)) in traditional REST API endpoints.
* [**Subscriptions**](https://www.graph.cool/docs/reference/graphql-api/subscription-api-aip7oojeiv/): This is essentially traditional GraphQL queries in reverse. Instead of sending a request to the server to retrieve data we tell the server to let us know when data changes and to send the updated data to us as defined in the subscription.

### What about the back-end?

In short, when I initially asked myself this question 3 years ago the answer was a resounding:

**Don’t even worry about it.**

Furthermore, I’m not sure whether my response has changed since. I still have no idea what Gatsby does behind the scenes to convert my markdown (via [gatsby-transformer-remark](https://www.gatsbyjs.org/packages/gatsby-transformer-remark/)) and JSON (via [gatsby-transformer-json](https://www.gatsbyjs.org/packages/gatsby-transformer-json/)) content into a GraphQL endpoint.

This is not due to apathy, quite the contrary in fact! I’m a big fan of Gatsby and busy working on a [pull request to trigger prefetching of pages programmatically](https://github.com/gatsbyjs/gatsby/issues/8122). Given how self-documenting GraphQL is, I have yet to have a need to peek under the hood in terms of how Gatsby handles GraphQL — regardless of how complex my query or data gets. Furthermore, there are several other GraphQL services that I use (for example, [Hygraph](https://hygraph.com/), formerly GraphCMS) where I can say the exact same.

**Does this mean that there is no value in learning how to configure a GraphQL server?**

Certainly not!

As with anything understanding how something works under the surface (whether it be JavaScript, CSS or even the browser itself) makes it easier to debug things when they do go wrong. However, the fact that I’ve only started digging into the back-end side of GraphQL recently goes to show how far you can get without knowing anything about how the endpoint gets created behind the scenes.

However, if you are interested in learning how to set up a custom GraphQL server you can have a look at [GraphQL for Back-end Developers](https://medium.com/@naidooshailen648/graphql-for-back-end-developers-b4f809417a99) by my good friend [Shailen Naidoo](https://www.freecodecamp.org/news/graphql-for-front-end-developers-1f59808f4435/undefined). He is a phenomenal developer and the reason why I’m even looking at the back-end side of GraphQL in the first place.

### Final Word

First and foremost, well done if you’ve read this entire wall of text from top to bottom. It’s quite lengthy! I started writing it mostly in response to the lack of front-end specific introductions to GraphQL. This meant that there was quite a bit of ground to cover.

Secondly, I am by no means an expert on GraphQL so if there are resources/references that I missed or you feel would help front-end developers get started on GraphQL, then please let me know in the comments. I’m more than happy to add it.

Lastly, if there are any inaccuracies also feel free to call me out in the comments!

If you’re interested in learning more about GraphQL check out the following resources:

* [Fullstack GraphQL](https://www.graphql.college/fullstack-graphql/) _(book)_
* [How To GraphQL](https://www.howtographql.com/) (website)
* [Official GraphQL documentation](https://graphql.org/learn/) _(website)_

Lastly, thanks for the feedback and input provided by [Shailen Naidoo](https://www.freecodecamp.org/news/graphql-for-front-end-developers-1f59808f4435/undefined) and [Zeeshaan Maudarbocus](https://www.freecodecamp.org/news/graphql-for-front-end-developers-1f59808f4435/undefined).

[**Follow me on Github**](https://github.com/schalkventer)**, I’m always curious as to what everyone in the tech field is working on — so I’ll probably follow you back! ?**

[**schalkventer - Overview**](https://github.com/schalkventer)  
[_? Front-end Development / ? UI Design / ? Social Good / ❤️ Destigmatising Mental Illness - schalkventergit_hub.com](https://github.com/schalkventer)

