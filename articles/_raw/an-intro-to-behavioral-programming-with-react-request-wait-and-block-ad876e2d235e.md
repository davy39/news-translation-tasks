---
title: 'An intro to Behavioral Programming with React: request, wait, and block'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-23T21:18:26.000Z'
originalURL: https://freecodecamp.org/news/an-intro-to-behavioral-programming-with-react-request-wait-and-block-ad876e2d235e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*vFUyNVhV5JOKn76HfMJYXw.jpeg
tags:
- name: Behavioral Programming
  slug: behavioral-programming
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Luca Matteis

  Behavioral Programming (BP) is a paradigm coined in the 2012 article by David Harel,
  Assaf Marron, and Gera Weiss.

  Directly from the abstract:


  Behavioral programming simplifies the task of dealing with underspecification and
  conflict...'
---

By Luca Matteis

Behavioral Programming (BP) is a paradigm coined in the [2012 article](http://www.wisdom.weizmann.ac.il/~amarron/BP%20-%20CACM%20-%20Author%20version.pdf) by David Harel, Assaf Marron, and Gera Weiss.

Directly from the abstract:

> Behavioral programming simplifies the task of dealing with underspecification and conflicting requirements by enabling the addition of software modules that can not only add to but also **modify existing behaviors**.

### High-level concepts

I’ll first explain the high-level concepts using an example of two React components `MoviesList` and `MoviesCount`. One displays a list of movies, the other a number of how many movies there are. Then I will dive into how exactly behavioral programming works.

Both components fetch data from the same HTTP URL. They were developed by two different teams in a large organization. When we render both components on a page, we have a problem as they perform the same request:

```
<>  <MoviesList />  <MoviesCount /></>
```

Little did we know that these are **behavioral components**. This means that we can do something quite clever to avoid both requests firing:

```
const MoviesCountFromList = withBehavior([  function* () {    // block FETCH_COUNT from happening    yield { block: ['FETCH_COUNT'] }  },  function* () {    // wait for FETCH_LIST, requested by the other    // MoviesList component, and derive the count    const response = yield { wait: ['FETCH_LIST'] }    this.setState({      count: response.length    })  }])(MoviesCount)
```

In the above example, we stepped inside the `MoviesCount` component. We **waited** and **requested** for something to happen. And, more uniquely to behavioral programming, we also **blocked** something from happening.

Because we were trying to avoid both requests from firing, we blocked the `FETCH_COUNT` event from being triggered (since the same data was already acquired by the `FETCH_LIST` event).

```
<>  <MoviesList />  <MoviesCountFromList /></>
```

Adding functionality to existing components without modifying their code is the novelty of the behavioral programming paradigm.

Intuitively, this can allow the creation of more reusable components.

In the rest of the article, I’ll go more in depth into how behavioral programing (BP) works, specifically in the context of **React**.

### Rethinking programming flow

To achieve the above functionality, we need to think about programming behaviors a bit differently. Specifically, **events** play a crucial role in orchestrating the synchronization between the various behaviors we define for our components.

```
const addHotThreeTimes = behavior(  function* () {    yield { request: ['ADD_HOT'] }    yield { request: ['ADD_HOT'] }    yield { request: ['ADD_HOT'] }  })
```

```
const addColdThreeTimes = behavior(  function* () {    yield { request: ['ADD_COLD'] }    yield { request: ['ADD_COLD'] }    yield { request: ['ADD_COLD'] }  })
```

```
run(  addHotThreeTimes,  addColdThreeTimes)
```

When we run the above code, we get back a list of requested events:

```
ADD_HOTADD_HOTADD_HOTADD_COLDADD_COLDADD_COLD
```

As expected, the first behavior executes. Once it’s done, the second behavior continues. However, new specifications for our component require us to change the order in which both events are triggered. Rather than triggering `ADD_HOT` three times, and then `ADD_COLD` three times, we want them to interleave and trigger `ADD_COLD` right after a `ADD_HOT` . This will keep the temperature somewhat stable.

```
...
```

```
const interleave = behavior(  function* () {    while (true) {      // wait for ADD_HOT while blocking ADD_COLD      yield { wait: ['ADD_HOT'], block: ['ADD_COLD'] }
```

```
      // wait for ADD_COLD while blocking ADD_HOT      yield { wait: ['ADD_COLD'], block: ['ADD_HOT'] }    }  })
```

```
run(  addHotThreeTimes,  addColdThreeTimes,  interleave)
```

In the above example, we introduce a new interleave behavior which does exactly what we need.

```
ADD_HOTADD_COLDADD_HOTADD_COLDADD_HOTADD_COLD
```

We changed the **order** of when things get executed, without having to modify the code of already-written behaviors.

The process is summarized in the graphic below.

![Image](https://cdn-media-1.freecodecamp.org/images/elehAKVL-hHtde0-NJJ4qaxh5-tUIhFvZfmP)

The key concepts of this way of programming are the **request**, **wait,** and **block** operators. The semantics for these operators are:

* **Requesting** an event: proposing that the event be considered for triggering, and asking to be notified when it is triggered
* **Waiting for** an event: without proposing its triggering, asking to be notified when the event is triggered
* **Blocking** an event: forbidding the triggering of the event, vetoing requests of other b-threads.

Each b-thread (behavioral thread) lives on its own and is unaware of other threads. But they’re all interwoven at runtime, which allows them to interact with each-other in a very novel way.

**The generator syntax is essential to the functioning of a behavioral program. We need to control when to proceed to the next yield statement.**

### Back to React

How can these BP concepts be used in the context of React?

Turns out that through high-order components (HOCs), you can add this behavioral idiom to existing components in a very intuitive fashion:

```
class CommentsCount extends React.Component {  render() {    return <div>{this.state.commentsCount}</div>  }}
```

```
const FetchCommentsCount = withBehavior([  function* () {    yield { request: ['FETCH_COMMENTS_COUNT']}    const comments = yield fetchComments()    yield { request: ['FETCH_COMMENTS_COUNT_SUCCESS']}    this.setState({ commentsCount: comments.length })  },])(CommentsCount)
```

Here we are using `withBehavior`, from the [b-thread](https://github.com/lmatteis/b-thread) library, to make `CommentsCount` a behavioral component. Specifically, we are making it fetch the comments and display the data once the data is ready.

For simple components, this might not be such a game-changer. But let’s imagine more complex components, with lots of logic and other components inside of them.

We might imagine the entire Netflix website as a `<Netflix` /> component:

![Image](https://cdn-media-1.freecodecamp.org/images/uPWqKfgGgH0PCYqKsvEyybAcWY5rHQwgG1Ax)
_Screenshot of Netflix’s website_

When we use this component in our app, we’d like to interact with it. Specifically, when a movie is clicked, we don’t want to start the movie immediately, but instead we want to make an HTTP request, show other data about the movie, and then start the movie.

Without changing code inside the `<Netflix` /> component, I’d argue that this would be impossible to achieve without it being a behavioral component.

Instead let’s imagine that `<Netflix` /> was developed using behavioral programming:

```
const NetflixWithMovieInfo = withBehavior([  function* () {    // First, block the MOVIE_START from happening     // within <Netflix /> until a new     // FETCH_MOVIE_INFO_SUCCESS event has been requested.    // The yield statement below can be read as:    // wait for FETCH_MOVIE_INFO_SUCCESS while blocking MOVIE_START    yield {       wait: ['FETCH_MOVIE_INFO_SUCCESS'],       block: ['MOVIE_START']     }  },  function* () {    // Here we wait for MOVIE_CLICKED, which is    // triggered within <Netflix />, and we fetch our    // movie info. Once that's done we request a new event    // which the earlier behavior is waiting upon    const movie = yield { wait: ['MOVIE_CLICKED'] }    const movieInfo = yield fetchMovieInfo(movie)    yield {       request: ['FETCH_MOVIE_INFO_SUCCESS'],       payload: movieInfo     }  }])(Netflix)
```

Above we’ve created a new `NetflixWithMovieInfo` component which modifies the behavior of the `<Netflix` /> component (again, without changing its source code). The addition of the above behaviors makes it so `that MOVIE_C`LICKED will not tr`igger MOVIE`_START immediately.

Instead, it uses a combination of “waiting while blocking”: a **wait** and a **block** can be defined within a single yield statement.

![Image](https://cdn-media-1.freecodecamp.org/images/KFzI-ryqH4Y8RJSMj9sQbhlgOewuCahAjVPJ)

The picture above describes, more in detail, what is happening within our behavioral components. Each little box within the components is a yield statement. Each vertical dashed arrow represents a behavior (aka b-thread).

Internally, the behavioral implementation will start by looking at all the yield statements of all b-threads at the current synchronization point, depicted using an horizontal yellow line. It will only continue to the next yield statement within a b-thread if no events in other b-threads are blocking it.

Since nothing is blocking `MOVIE_CLICKED` , it will be requested. We can then continue to the next yield statement for the Netflix behavior. At the next synch point, the b-thread on the far right, which is waiting for `MOVIE_CLICKED`, will proceed to its next yield statement.

The middle behavior that is waiting-and-blocking does not proceed. `FETCH_MOVIE_INFO_SUCCESS` was not requested by other b-threads, so it still waits-and-blocks. The next synchronization point will look something like this:

![Image](https://cdn-media-1.freecodecamp.org/images/q1eZUSHheMd3CdPZLyaaMx2EwdScwta7qHeW)

As before, we will look at all the yield statement at this synchronization point. This time, however, we cannot request `MOVIE_START` because there’s another b-thread that is blocking it (the black yield statement). The Netflix component will therefore not start the movie.

`FETCH_MOVIE_INFO_SUCCESS` on the far right, however, is free to be requested. This will unblock `MOVIE_START` at the next synch point.

All this in practice allowed us to change the order of things happening within other components, without directly modifying their code. We were able to block certain events from firing until other conditions were met in other components.

**This changes the way we might think of programming:** not necessarily a set of statements executed in order, but **rather an interleaving of yield statements all synchronized through specific event semantics.**

Here’s a simple animation depicting the way b-threads are executed and interwoven at runtime.

![Image](https://cdn-media-1.freecodecamp.org/images/vgOkR26vCmjVgmF6-gJpO5Cetiku9SsaqxFE)
_Order of execution of different threads_

### Programming without changing old code

There is another way we can understand this programming idiom. We can compare the way we currently program as specifications change, versus how it would be done with behavioral programming.

![Image](https://cdn-media-1.freecodecamp.org/images/uH6c2Q8UiiNHTtir3GipE69BK9ld6ZTY0NYe)
_Each added behavior is depicted using a different colored rectangle_

In the above caption, we imagine how behavior may be added to a non-behavioral program. We start with a program described only using three black rectangles (on the left).

As specifications change, we realize we need to modify the program and add new behavior in various sections of the program, depicted as newly added colored rectangles. We continue doing this as requirements for our software change.

Every addition of behavior requires us to change code that was written, which possibly litters the old behavior with bugs. Furthermore, if the program we are changing is part of various other modules used by different people, we might be introducing unwanted behavior to their software. Finally, it may not be possible to change specific programs as they might be distributed as libraries with licensed source code.

![Image](https://cdn-media-1.freecodecamp.org/images/rtjBXCCf8ftal6Utzyt0wX6EIOmvq9k1Qk0n)
_Each column on the left is a b-thread_

In the above figure, we see how the same program-modifications can be achieved using behavioral programming idioms. We still start with our three rectangles on the left as we did before. But as new specifications arise, we don’t modify them. Instead we add new b-threads, represented as columns.

The resulting program is the same, although constructed in a very different way. One of the advantages of the behavioral approach is that we don’t have to modify old code as requirements change.

You can also imagine developing each b-thread in parallel, possibly by different people in a large organization, since they do not directly depend on each other.

The benefit of this approach also seems to be with packaging: we can change the behavior of a library without needing to access or modify its source-code.

### APIs not only as props, but as events

Currently, the only way for a React component to communicate with the outside world is via props (apart from the Context API).

By making a component behavioral, instead of using props, we tell the outside world about when things happen within the component by yielding events.

To allow other developers to interact with the behavior of a component, we must therefore document the events that it **requests**, the events it **waits for,** and finally the events it **blocks**.

**Events become the new API.**

For instance, in a non-behavioral `Counter` component, we tell the outside world when the counter is incremented and what the current count is, using an `onIncrement` prop:

```
class Counter extends React.Component {  state = { currentCount: 0 }  handleClick = () => {    this.setState(prevState => ({      currentCount: prevState.currentCount + 1    }), () => {      this.props.onIncrement(this.state.currentCount)    })  }  render() {    {this.state.currentCount}    <button onClick={this.handleClick}>+</button>  }}
```

```
<Counter   onIncrement={(currentCount) =>     console.log(currentCount)  }/>
```

What if we want to do something else before the counter’s state gets incremented? Indeed we could add a new prop such as `onBeforeIncrement`, but the point is that we don’t want to add props and refactor code every time a new specific arises.

If we transform it into a behavioral component we can avoid refactoring when new specifications emerge:

```
class Counter extends React.Component {  state = { currentCount: 0 }  handleClick = () => {    bp.event('CLICKED_INCREMENT')  }  render() {    {this.state.currentCount}    <button onClick={this.handleClick}>+</button>  }}
```

```
const BehavioralCounter = withBehavior([  function* () {    yield { wait: ['CLICKED_INCREMENT'] }    yield { request: ['UPDATE_CURRENT_COUNT'] }
```

```
    this.setState(prevState => ({      currentCount: prevState.currentCount + 1    }), () => {      this.props.onIncrement(this.state.currentCount)    })  }])(Counter)
```

Notice how we moved the logic for when the state is updated inside a b-thread. Furthermore, before the update actually takes place, a new event `UPDATE_CURRENT_COUNT` is requested.

This effectively allows other b-threads to block the update from happening.

Components can also be encapsulated and shared as different packages, and users can add behavior as they see fit.

```
// package-name: movies-listexport const function MoviesList() {  ...}
```

```
// package-name: movies-list-with-paginationexport const MoviesListWithPagination = pipe(  withBehavior(addPagination))(MoviesList)
```

```
// package-name: movies-list-with-pagination-logicexport const MoviesListWithDifferentPaginationLogic = pipe(  withBehavior(changePaginationLogic))(MoviesListWithPagination)
```

Again this is different from simply enhancing a component, as a regular HOC would do. We can block certain things from happening in the components we extend from, effectively modifying their behavior.

### Conclusion

This new programming idiom might feel uncomfortable at first, but it seems to alleviate a prominent issue we have when using UI components: **it is hard to reuse components, because they don’t blend with the environment they were put into.**

In the future, perhaps using these behavioral concepts, we will be able to add new behavior to apps by simply mounting new components. Stuff like this will be possible:

```
<Environment>  <Netflix />  <Twitter />  <WaitForTwitterBeforeNetflix />  <OnTwitterClickShowLoader /></Environment>
```

Additionally, events don’t need to pollute the whole app and can be broadcast only within a specific environment.

Thanks for reading! If you’re interested in an actual implementation of behavioral programming, please see my current work in progress library that works with React: [https://github.com/lmatteis/b-thread](https://github.com/lmatteis/b-thread). The [Behavioral Programming homepage](http://www.wisdom.weizmann.ac.il/~bprogram/) also contains various implementations.

For more information on this exciting new concept, I suggest you read the [scientific papers on Behavioral Programming](https://scholar.google.ca/scholar?hl=en&as_sdt=0%2C5&q=behavioral+programming+harel&btnG=) or check some of [my other articles](https://medium.com/@lmatteis/on-user-interface-development-appending-to-the-event-log-8d8ca966795d) [on the subject](https://medium.com/@lmatteis/statecharts-updating-ui-state-767052b6b129).

