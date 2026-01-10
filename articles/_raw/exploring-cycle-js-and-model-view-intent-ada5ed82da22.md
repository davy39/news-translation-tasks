---
title: Let’s explore the benefits of Cycle.js and Model-View-Intent
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-05-14T18:50:02.000Z'
originalURL: https://freecodecamp.org/news/exploring-cycle-js-and-model-view-intent-ada5ed82da22
coverImage: https://cdn-media-1.freecodecamp.org/images/1*r980RzYbz7ShlZEYsd089A.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Fabio Hiroki

  In the current software development ecosystem, it''s not surprising that Model-View-Controller
  (MVC) architecture doesn’t have a great reputation. Common alternatives have been
  gaining popularity, such as Model-View-Presenter (MVP) and...'
---

By Fabio Hiroki

In the current software development ecosystem, it's not surprising that Model-View-Controller (MVC) architecture doesn’t have a great reputation. Common alternatives have been gaining popularity, such as Model-View-Presenter (MVP) and Model-View-ViewModel (MVVM).

As a mobile developer, I tried the MVP architecture. And in fact, I had a better experience because of the separation of concerns and improved testability provided by this architecture. But it doesn't propose a pattern for data flow (like Flux or Redux), and I felt somehow dissatisfied by this. I wondered if there’s a way to minimize the bugs and provide a better developer experience.

### Model-View-Intent (MVI)

The first concept that caught my attention was the Model-View-Intent (MVI) implementation on Android proposed by the [Mosby](https://github.com/sockeqwe/mosby) library. I decided to read its code and try to understand its principles.

Mosby looked like a great library, especially because its creator thoroughly documented its motivation and published examples on his [blog](http://hannesdorfmann.com/mosby/). But unfortunately Mosby seemed too complex. It had a steep learning curve and wasn’t exactly what I was trying to find — and represented only a small incremental improvement from MVP.

The MVI concept wasn’t first introduced by Mosby, but rather by a web framework called [Cycle.js](https://cycle.js.org/). So I decided to learn the basics. To my surprise, Cycle.js made me like the MVI idea and want to give it a try. Mostly because the framework is very small and simple.

These are the basic principles of MVI, and why they have great value:

* **Purely reactive:** this makes it much easier to coordinate asynchronous tasks, and brings all the [benefits](https://tylermcginnis.com/imperative-vs-declarative-programming/) from declarative programming. In the case of Cycle.js, it makes your **view** testable. As we're going to see below, the view becomes just a common **observable**_._
* **Unidirectional data flow:** in MVI, the data follows a straight path of **intent**, **model**, and **view**. I will discuss this in detail in the next section. But for now, this means that you as a developer must learn how to organize your code to use this pattern. Once you overcome the learning curve, your application becomes easier to understand. Every feature on your app follows the same recipe.
* **The** view layer is represented by a single object, the model: the entire **view** state is represented by an unique source of truth, including the **loading** and **error** states. This means that you have to look at and manipulate one place in order to display the view correctly.

More details about MVI design and advantages are described in [this article](http://futurice.com/blog/reactive-mvc-and-the-virtual-dom) by Cycle.js’ creator and also in [this article](https://medium.com/@fkrautwald/plug-and-play-all-your-observable-streams-with-cycle-js-e543fc287872). I recommend that you read both to have a better understanding even if you don’t have a background in web development.

### MVI in a real application

![Image](https://cdn-media-1.freecodecamp.org/images/f6tnoMKQNH7s3ekf1IPZob1FoilxvGTYEkjn)
_The application I've built using Cycle.js_

After I gained a brief understanding of MVI, I decided to build an application using Cycle.js to verify its benefits in a practical way. The app I built provides an initial list of characters and then performs search requests on [Star Wars API](https://swapi.co/) when you type something in the input text. You can see the code in this [repository](https://github.com/fabiothiroki/cyclejs-starwars).

The main structure of a Cycle.js application is an abstraction of the concept of a human-computer interaction. This is represented by a single function where any external interaction is passed as a function parameter (usually called "sources"), and the "human" output is the object returned by the function (usually called "sinks").

In our application, this is represented by the "App" method in the "app.js" file. The code placed between the input and the output will transform the "sources" into an **intent observable**_,_ which is transformed into a **model** **observable.** The latter is then transformed into a **view observable** which is returned inside the "sinks" object.

```
export function App (sources) {
```

```
  // ...
```

```
  return sinks;}
```

We will build each layer incrementally in the same order as the data should flow.

### Intent

The intent object contains **observables** generated from the "sources" object. It represents the user’s intent when interacting with the application. In our application, a user can do two things:

* Enter a search term by typing on the input text
* Receive characters’ data from the API

```
const intents = {  receiveCharacterList: sources.HTTP.select(‘api’).flatten(),
```

```
  changeSearchTerm: sources.DOM.select(‘#search.form-control’)    .events(“input”)    .map(ev => ev.target.value)    .startWith(‘’)}
```

You don't need to worry if you don’t understand the receiveCharacterList property of the **intents** object. For now, to understand the MVI concept, you just need to understand this: the changeSearchTerm receives a new **observable** whenever the user types something in the input that has an id of "search.form-control." By default it started with an empty string.

### Model

The **model**, as I've mentioned above, is the representation of the current **view** state. It depends only on the **intents** object.

```
const model = Observable.combineLatest(  intents.receiveCharacterList,   intents.changeSearchTerm)  .map((combined) => {
```

```
    const [response, searchTerm] = combined
```

```
    return {      characters: response.body.results,      searchTerm: searchTerm    }; }) .startWith({   characters: [{name: ‘Loading…’}],   searchTerm: ‘’ });
```

Here we are combining the observable containing the API response with the observable containing the **string** typed. The result is a new observable containing the list of characters and the search term.

### View

The **view** in Cycle.js isn't represented by HTML or by a controller layer, as we commonly see in mobile applications. The default Cycle.js configuration uses a library called [Cycle DOM](https://cycle.js.org/api/dom.html), which can generate an observable from a Virtual DOM [abstraction](https://github.com/snabbdom/snabbdom).

```
const view = model.map((state) => {
```

```
  const list = state.characters.map( character => {    return tr(td(character.name));  });
```

```
  return div(“.card”, [    div(‘.card-header’, [      h4(‘.title’, ‘Star Wars Character Search’),      input(‘#search.form-control’, {props: {type: “text”, placeholder: “Type to search”, value: state.searchTerm}})    ]),    div(‘.card-content .table-responsive’,[      table(‘.table’, [        thead(tr(th(h5(‘Name’)))),        tbody(list)      ])    ])  ]);});
```

As I mentioned above, view depends only on **model.** It generates an HTML table for listing the characters and it fills the **input** with the typed string.

At the end of our “App” function, the view is part of the returned “sinks” object. The “sinks” should also contain the configuration of the HTTP request to the API:

```
return {  DOM: view,  HTTP: intents.changeSearchTerm.map( searchTerm => {    return {      url: ‘https://swapi.co/api/people/?search=' + searchTerm,      category: ‘api’,    }  })};
```

### Unit testing the view

Given that the view representation is just a function of the model_,_ we can easily write unit tests for it. First, I’ve extracted the view creation into method and moved it to a separate file. This allowed me to use it in the application and in the tests. Then I’ve used the [chai-virtual-dom](https://github.com/staltz/chai-virtual-dom) package to compare two views_._

The tests I’ve implemented follow this basic structure:

1. Create a **mock** model of the state we want to test.
2. Use the **view** function passing the created mock to generate its view.
3. Assert if the created view is equal to the expected view.

In this application I’ve created two simple test cases:

* When the application is loading the API data, the view should display a **loading** state:

```
const model = Observable.of({ characters: [{name: ‘Loading…’}], searchTerm: ‘’});
```

```
const view = view(model);
```

```
const expected = div(".card", [  div('.card-header', [    h4('.title', 'Star Wars Character Search'),    input('#search.form-control', {props: {type: "text", placeholder: "Type to search"}})  ]),  div('.card-content .table-responsive',[    table('.table', [      thead(tr(th(h5('Name')))),        tbody([          tr(td('Darth Vader')),          tr(td('Darth Maul')),        ])      ])    ])  ]);
```

```
expect(view).to.look.exactly.like(expected);
```

* When the application has received the characters’ data from the API, the view should display it:

```
const model = Observable.of({  characters: [{name: 'Darth Vader'}, {name: 'Darth Maul'}],  searchTerm: 'darth'});
```

```
const view = view(model);
```

```
const expected$ = div(".card", [  div('.card-header', [    h4('.title', 'Star Wars Character Search'),    input('#search.form-control', {props: {type: "text", placeholder: "Type to search"}})  ]),  div('.card-content .table-responsive',[    table('.table', [      thead(tr(th(h5('Name')))),        tbody([          tr(td('Darth Vader')),          tr(td('Darth Maul')),        ])      ])    ])  ]);
```

```
expect(view).to.look.exactly.like(expected);
```

### Conclusion

I got a great first impression of the Model-View-Intent architecture. Code looks more organized and is easier to understand, so it provides a nicer developer experience. The communication between an object and its responsibilities are already predefined, so you don’t have to make too many decisions when programming.

In the end, MVI doesn’t take a lot of effort to learn and seems to be a better choice when comparing it to MVP.

What about Cycle.js? I’m not yet 100% confident that I can start building a production application using Cycle.js. I think I need to explore the framework further to assess its real capabilities, like creating routes or an authentication system.

Did you enjoy this article? If so, please give me some claps so more people see it. Thank you!

