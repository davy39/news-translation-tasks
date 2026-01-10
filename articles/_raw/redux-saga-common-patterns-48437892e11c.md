---
title: This collection of common Redux-saga patterns will make your life easier.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-08-24T21:53:45.000Z'
originalURL: https://freecodecamp.org/news/redux-saga-common-patterns-48437892e11c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*2o7NrAj_0G63BKySac_XuA.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Andrés Mijares

  This is a 2-part series — feel free to check out the first part here.

  I’ve been a redux-saga user for a year now, and I still remember when I was introduced
  to the library. I remember how amazed I was (that ‘Eureka’ moment!) when I ...'
---

By Andrés Mijares

**This is a 2-part series — feel free to check out the first part [here](https://medium.freecodecamp.org/async-operations-using-redux-saga-2ba02ae077b3).**

I’ve been a redux-saga user for a year now, and I still remember when I was introduced to the library. I remember how amazed I was (that ‘Eureka’ moment!) when I solved a few problems in matter of hours.

It was so good that I needed to share all this awesomeness with other people — so I sat down and wrote a [post](https://medium.freecodecamp.org/async-operations-using-redux-saga-2ba02ae077b3) about it. From that day on, due to the [curse of knowledge](https://en.wikipedia.org/wiki/Curse_of_knowledge), I couldn’t imagine my life without it.

It was so good that now I also use it as an orchestration layer to manage all the asynchronous operations at work at [Shiftgig](http://www.shiftgig.com). So yes, these lines of code help to support the daily operations of several million VC companies — a big part of our application architecture relies on it.

If you are interested in that, [this other](https://medium.com/shiftgig-blog/agile-front-end-architectures-with-react-redux-and-vanilla-js-23f4e5626e01) post can point you in that direction.

**A side note:** If your company happens to rely heavily on this or any open source project, I highly encourage you (and your employer) to become a [backer of the project](https://opencollective.com/redux-saga#contributors). This small donation can make a big difference, and it’s a nice way to make good karma. ??.

### Enough with the emotive introduction — let’s see the patterns.

This post assumes that you have a basic understanding of the library. If you need more information about how to register a saga, or even how to configure, please refer to the first part of the series [here](https://medium.freecodecamp.org/async-operations-using-redux-saga-2ba02ae077b3).

After a year of working with the library and solving problems, we have identified a few patterns that we have repeated over and over. Let’s see them one by one with a possible use case for each.

Disclaimer: I used the names I know for these. But if you happen to know them by some sort of official names, please comment below.

### Take and Fork

By definition, the most common on my list. Do you remember the old way when you used to put a listener and watchers everywhere on your angular 1 application? Well, I kind of do…?.

This pattern is mostly used to trigger a process after an action is dispatched — yeah! Like a listener:

```
/* this is the saga you are going to register */export function* aListenerOnlySaga() {  const somePossibleData = yield take('SOME_ACTION')  yield fork(someOtherSagaProcess)}
```

```
function* someOtherSagaProcess() {    /* Any process calculation you need to do */}
```

#### The use case

There are many…but let’s keep it real. In our application, we need to support different branches/states that are required to display information and take action based on the current selection.

If I’m Martha, a 45 year old secretary who doesn’t like technology, I need to be able to select a branch from a dropdown and, by magic, query the information related to it.

```
/* Some ugly react component*/class CompanyDropDown extends React.Component {   state = {      company: null,       branches: [],   }   componentDidUpdate ({company, branches}) {     this.setState(({company}) => ({company, branches}))   }   onChangeCompany (company) {      this.props.dispatch('company_change', company)   }   render () { /* omitted for convenience */}}
```

```
const mapStateToProps = ({company, branches}) => ({company, branches})
```

```
export connect(mapStateToProps)(CompanyDropDown)
```

Some details, like the render method and the reducers, will be omitted to go directly to the point.

```
/* somewhere in your code... */export function* listenForChangeCompany() {   /* this variable holds the argument passed */   const company = yield take('company_change')   yield fork(changeCompanySaga, company)}
```

```
function* changeCompanySaga(company) {   const branchesPerCompany = yield call(getBranchesByCompany, company)   yield put({     type: 'company_change_success',     payload: branchesPerCompany,   })}
```

Now our UI is separate from out business logic, and we are happy. We will add more complexity to this later.

The main benefit of this is that you can create a process catalog (more about this later) that isolates that specific functionality and exposes it to your team at your discretion.

But there is a little problem with that pattern. If you noticed, **this will work only once.** After you exec the process, it won’t work anymore. That’s where the next pattern comes in handy.

### Watch and Fork

One of the problems with the Take and Fork pattern is that we limit the amount of executions to only one. As you can see, that previous use case probably doesn’t match the use for the pattern. I made it on purpose, so that this way we can keep enhancing and powering it is as much as we need, step by step.

A better fit-for-purpose case would probably be a login or logout process, where you know that you only need them once.

Moving on with the case, we need to make sure that our friend Martha can change between companies as much as she needs to, not only once. We can solve this with a small tweak. Let’s see the watch and fork pattern in place, and let’s bring our listener saga to the game again.

```
export function* listenForChangeCompany() {   while (true) {      const company = yield take('company_change')      yield fork(changeCompanySaga, company)   } } /* eh viola! */
```

Pretty neat, eh? If you are not used to function generators, having a while/true around probably looks weird. But it fits the purpose. Still, there is a even better way to do it: we can iterate more over this using another library helper shortcut.

```
/* Where you register the sagas */function* rootSagas () {   yield [    takeEvery('company_change', changeCompanySaga)   ]}
```

Behind the scenes, the company argument is passed to the changeCompanySaga saga. I really like this pattern, especially if you need to handle a big application with hundreds of processes. You just know that it responds to a single dispatched action.

### Put and Take

This pattern is very useful. As I mentioned before, you organize your process operations into different sagas. You then create a services catalog that you can share across all the teams/people/units you name. This means that each of your services has a finite functionally that will change your state. Sometimes that is enough, while other times you want to extend the capability of a single service. Let’s see a use case.

Imagine that one of the teams in your company tells you that they’ve created this very complex service that you can re-use. It’s called...`fetchDataOverFiveDifferentLocations` . This is a lot of imperative stuff, but at the end you will have all the information you need parsed and ready to be consumed. Awesome!

You and your team agreed on some naming conventions that go as follows: {service_name}_{microservice}_{status}. So let’s say:

* **fetchSomeData_events** This will start the saga.
* **fetchSomeData_events_start** This action is dispatched by the service as soon as it starts.
* **fetchSomeData_events_success** This action is dispatched by the service when it finishes.
* **fetchSomeData_events_error** This action is dispatched if there is an error during the process.

This means our services library exposes a saga which looks like this:

```
export function* fetchDataOverFiveDifferentLocations() {    while (true) {        yield put({type: 'fetchSomeData_events_start'})       /*         computing stuff...       */       yield put({type: 'fetchSomeData_events_success'})     }}
```

On your application, you can consume the service like this:

```
function* rootSagas () {   yield [    takeEvery('fetchSomeData_events', fetchDataOverFiveDifferentLocations)   ]}
```

What if we need to extend that functionality?

```
/* We create a manager saga */function* fetchDataManager () {   /* we need to start the service/saga */   yield put({type: 'fetchSomeData_events'})   /* we need to wait/listen when it ends...*/   yield take('fetchSomeData_events_success')   /*      fork another process,     query info from the state,     do imperative stuff,     whatever you need to do when the previous saga finishes, the sky is the limit...    */}
```

```
/* We create an orchestrator saga */function* orchestratorSaga () {   while (true) {    yield fork(fetchDataManager)   }}
```

```
/* your root saga then looks like this */function* rootSagas () {   yield [    takeEvery('other_action_trigger', orchestratorSaga),   ]}
```

Probably some of you are thinking… what about the error handling? Hold your thoughts, I will come back to that later.

### For/of Collection

This one is picky, because most of the time we do not solve the problem this way by default. But when you need it, you need it.

Let’s say that we fetch a collection from any source. We receive 100 objects and we need to apply an operation/service to each. In other words, we need to dispatch one or multiple actions per each element. Normally, this is something you can manage in a reducer, but let’s keep the spirit of the service catalog.

The problem is that when you are in a saga, you cannot do something like:

```
function* someSagaName() {   /* code omitted for convenience */   const events = yield call(fetchEvents)   events.map((event) => {      /* this is syntactically invalid */      yield put({type: 'some_action', payload: event})   })}
```

This is when the for/of loop comes to the rescue. Let’s solve this problem before we start breaking our architectural services rules ??.

```
function* someSagaName() {   /* code omitted for convenience */   const events = yield call(fetchEvents)   for (event of events) {     yield put({type: 'some_action', payload: event}) /* ?? */     /* or maybe something like: */     yield fork(someOtherSagaOrService, event) /* ?? */   }}  
```

How the for/of loop works is beyond the scope of this post, but you can find out more [here](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Statements/for...of). Also, it’s possible to do it using a regular for loop and iterate over the array — it’s your call.

### Error Handling

Oh yes! Javascript is not Elixir, so we still need to do defensive programming and protect against errors. ??‍? Based on this catalog structure, how do we ensure that we don’t swallow the errors? Or how can each error be managed correctly? A 500 is not the same as a 401, so we still need a flexible way to communicate to the user in a friendly way that something went wrong.

The rules of thumb we use are simple:

* **All** errors are handled inside the sagas.
* **The saga that manages** the process is in charge of handling the error.

Let’s go back to our event manager service:

1. This service is generic.
2. If the service handles the error, we cannot make a custom error. We are just coupled to the conventional error.
3. If we need to make a custom handler, we need to create a service that handles for the error.

```
/* Case 1, service that manage the error */export function* fetchDataOverFiveDifferentLocations() {    try {      while (true) {          yield put({type: 'fetchSomeData_events_start'})         /*           computing stuff...         */         yield put({type: 'fetchSomeData_events_success'})       }    } catch (error) {      yield put({type: 'fetchSomeData_events_error', error})    }}
```

In this case, we are coupled to the service error, so we need to create a service that listens for that action:

```
function* rootSagas () {  yield [   takeEvery('fetchSomeData_events_error', yourErrorHandlerService),   /* ... */,     ]}
```

The only con for this that I’ve found so far is how verbose it is to handle a single error. But it also gives you a lot of flexibility, since you decide on your reducers if you want to react to this error or not. The important part is that it was caught and that your application is being notified.

```
/* Case 2, manager takes care of the error */function* fetchDataOverFiveDifferentLocations() {  while (true) {     yield put({type: 'fetchSomeData_events_start'})         /*           computing stuff...         */    yield put({type: 'fetchSomeData_events_success'})   }}
```

```
function* fetchDataManager () {  try {     yield put('fetchSomeData_events')     /*...*/     yield take('fetchSomeData_success')  } catch (error) {    yield put('some_custom_error_action', error)  }}
```

You can then handle the error, for example, via a reducer. It’s probably a boolean. It’s up to you based on what you need — both ways work really well. It will depend on your cases and you agreements with the team. Remember: **convention over configuration** is the key.

### Conclusion

As you might see, this library comes in really handy when you need a solid way to share architectural practices across teams, or maybe when you need to create a very descriptive service layer. Most important of all, it is really easy to extend to others.

Do you use any other patterns? I’m always happy to learn what others are doing out there and how we can learn from each other. Please let me know!

Finally feel free to check my open source projects at the moment:

* [**React Calendar Multiday**](https://github.com/andresmijares/react-calendar-multiday)

[**the mediocre engineer**](https://www.youtube.com/channel/UCSBzbeNuDamKpX6N4Q5SaHA)  
[_For more content like this, please, consider subscribe to my channel_www.youtube.com](https://www.youtube.com/channel/UCSBzbeNuDamKpX6N4Q5SaHA)

