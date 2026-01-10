---
title: Why I now appreciate testing, and why you should, too.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-25T20:41:01.000Z'
originalURL: https://freecodecamp.org/news/why-i-now-appreciate-testing-and-why-you-should-too-74d48c67ab72
coverImage: https://cdn-media-1.freecodecamp.org/images/1*4zwBXAldsCYxTb9vySYwZw.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Testing
  slug: testing
seo_title: null
seo_desc: 'By Evelyn Chan

  There’s a common misconception that writing tests slows down development speed.
  While the benefits of testing may not be immediately noticeable sometimes, it’s
  been my experience thus far that testing allows me to work faster in the lo...'
---

By Evelyn Chan

There’s a common misconception that writing tests slows down development speed. While the benefits of testing may not be immediately noticeable sometimes, it’s been my experience thus far that testing allows me to work faster in the long run, even on a small team.

After implementing tests for a full-stack application, I’ve come to appreciate how useful it is to effectively test your apps and how it influences your coding ability.

### Quick intro to what a test stack looks like

**Jest** is a testing library developed by Facebook that comes prepackaged with a bunch of cool methods to make testing easier. On a recent project, my team and I chose Jest because of its ease of use and its wide range of built-in functions that help streamline your testing. It’s very simple to set up and uses the Expect library for assertions.

**Enzyme** is the de-facto way of testing your React app. It’s pretty magical in that it renders your React components within Jest, allowing you to test your front end JSX code effectively without manually transpiling it. You render your components using one of three methods: shallow, mount, or render.

**SuperTest** allows you to make API calls without actually making the call, by intercepting it. API calls can be expensive and/or slow for unit tests, so you won’t want to make the call and wait for the response. Otherwise, it’ll slow down your tests and take forever to run.

### Here’s what I’ve learned

#### Testing prevents regression

Adding new features frequently breaks existing code, and having tests can prevent this from happening. Testing helps ensure that your code works as you intend it to. As simple as it may sound, that makes a world of difference.

It may seem silly to hear that not all programmers can articulate the code they write, but it’s actually pretty common. How many times have you been asked to explain something you wrote on the fly under a strict deadline and found yourself stuttering to answer? Writing tests forces you to think clearly about what exactly your function is taking in as an argument and returning as an output.

Even if you do understand the purpose of each line of code, as time goes on, you’ll inevitably start to forget. Tests provide an important complement to documentation that helps you move back and forth between code bases quickly. Taking the time to write good, efficient tests allows you to refactor your code much more easily and develop with confidence.

#### Unit test with mocks and stubs.

In a unit test, you test a specific piece of code one at a time. In any application, your code probably will make calls to and depend on other classes or modules. As these relationships between classes increase in complexity, it’ll obfuscate the source of bugs.

In order to isolate and debug effectively, you can replace these dependencies with a mock or a stub to control the behavior or output you expect.

For example, let’s say you want to test the following method:

```
import database from 'Database';import cache from 'Cache';
```

```
const getData = (request) => { if (cache.check(request.id)) { // check if data exists in cache  return cache.get(request.id); // get from cache } return database.get(request.id); // get from database};
```

Stub:

```
test('should get from cache on cache miss', (done) => { const request = { id: 10 }; cache.check = jest.fn(() => false);
```

```
getData(request); expect(database.get).toHaveBeenCalledWith(request.id); done();});
```

Mock:

```
test('should check cache and return database data if cache data is not there', (done) => { let request = { id: 10 }; let dummyData = { id: 10, name: 'Foo' }  let cache = jest.mock('Cache'); let database = jest.mock('Database'); cache.check = jest.fn(() => false); database.get = jest.fn(() => dummyData);
```

```
expect(getData(request)).toBe(dummyData); expect(cache.check).toHaveBeenCalledWith(request.id); expect(database.get).toHaveBeenCalledWith(request.id); done();});
```

The main difference between the two lies in state vs behavioral manipulation.

When using mocks, you replace the entire module with a mock object. A stub is a forced output of a function no matter the given input. Mocks are used to test if a function is being called with the right arguments, and stubs are used to test how a function operates on a given response. Stubs are used to validate the state of a method, whereas mocks are used to evaluate the behavior.

Jest provides `jest.fn`, which has both basic mocking and stubbing functionality. A Jest mock can also stub method outputs, and in this case be both a mock and a stub.

The concept of mocks in testing and how they differ from stubs can get pretty complex, so for a deeper dive, check out the links at the end!

#### Know what you don’t need to test.

You’ll want to test every method you write. But keep in mind that depending on your code base, 100% test coverage is unlikely and most times not even necessary.

With Jest, you can easily track your test coverage by adding a`--coverage` tag to your test script on your CLI. While this is a useful measure, take this with a grain of salt — the way Jest measures test coverage is through tracing the call stack, so a higher test coverage doesn’t necessarily mean your tests are effective.

For example, in a previous project, I used a library to implement a carousel component. Within the component was a function to render a list based on an array. To increase test coverage, I wrote a test to count and compare the number of rendered items to the array. The carousel component modified the number of items being rendered on the DOM to be more than a 1:1 output, even though the implementation visually displayed the correct number of elements in the browser. I chose to forego the test coverage because it was essentially testing the carousel library instead of my code.

Let’s assume a `Listings` component with a method `renderCarousel` that renders a carousel from an external library:

**Ineffective test:**

```
test('should return the same number of elements as the array', (done) => {    // Full DOM render    let mountWrapper = mount(<Listings />);
```

```
    // State change to trigger re-render    mountWrapper.instance().setState({ listings: [listing, listing, listing] });
```

```
    // Updates the wrapper based on new state    mountWrapper.update();
```

```
    expect(mountWrapper.find('li').length).toBe(3);    done();  })
```

**Effective test:**

```
test('should call renderCarousel method when state is updated', (done) => {    // Mock function inside component to track calls    wrapper.instance().renderCarousel = jest.fn();
```

```
    // State change to trigger re-render    wrapper.instance().setState({ listings: [listing, listing, listing] });
```

```
    expect(wrapper.instance().renderCarousel).toHaveBeenCalled();    done();  });
```

The difference between the two lies in what the tests are actually testing.

The first example evaluates the renderCarousel function, which calls the external library. The second test evaluates whether the renderCarousel is simply being called. Since the external libraries are somewhat akin to a black box of magic and are being tested by their own developers, it’s not necessary to write a test that makes sure it’s working correctly.

In this scenario, we only need to test that the library is being called and have faith that the library’s developers are handling the testing.

Understanding what you do and don’t need to test lets you maximize your time to remove redundancies.

#### Well-designed tests lead to well-designed code.

Designing your code knowing you’ll have to write tests for it improves your code. This is known as test-driven development, which is supported by a wide margin of the coding community.

In order to appropriately unit test functions, you need to strip away logic and test one method at a time. This structure forces you to write modular code and abstract logic away from your components.

As you think about your code in terms of writing tests, you’ll start to develop the habit of decoupling your code. I’ve discovered that writing your code this way seems to produce a story-like structure that’s both easier to write and easier to follow.

Let’s consider a scenario where we’re calling an endpoint to fetch data from a database and formatting that data before we return it.

**Too much logic:**

```
// Define endpointapp.get('/project', (request, response) => {  let { id } = request.params;  let query = `SELECT * FROM database WHERE id = ${id}`;    database.query(query)    .then((result) => {      const results = [];      for (let index = 0; index < data.length; index++) {        let result = {};        result.newKey = data[index].oldKey;        results.push(result);      }      response.send(results);    })    .catch((error) => {      response.send(error);    })  })
```

**Easier to test:**

```
// Make call to database for dataconst getData = (request) => {  return new Promise((resolve, reject) => {    let { id } = request.params;    let query = `SELECT * FROM database WHERE id = ${id}`;    database.query(query)      .then(results => resolve(results))      .catch(error => reject(error));    };}
```

```
// Format data to send backconst formatData = (data) => {  const results = [];  for (let index = 0; index < data.length; index++) {    let result = {};    result.newKey = data[index].oldKey;    results.push(result);  }  return results;}
```

```
// Send back dataconst handleRequest = (request, response) => {  getData(request)  .then((result) => {    let formattedResults = formatData(result)    response.send(formattedResults);  .catch((error) => {    response.send(error);}
```

```
// Define endpointapp.get('/project', handleRequest);
```

While the second example is longer, it’s much easier to follow along. The logic is clearly abstracted and isolated, making it much easier to test.

If you’re just starting out with testing/coding, it can be hard to discern what makes a well-designed test. You can’t write effective tests if your code isn’t designed well, but you can’t figure out what makes code suitable for the tests you can’t write! Fortunately, this leads to my last tip…

#### Write tests as you code

The best way to incorporate testing is to write it alongside your code. Otherwise, it’ll feel overwhelming when you write them all at once and have to go back and forth between all your test and method files.

Many beginners make the mistake of treating tests as something you do after all your code is written. If you treat it as a task you do alongside your code, it not only improves your code but also makes writing them more achievable.

In a system with cleanly abstracted APIs, you can test each class before moving on so you know which part of the logic is broken. For instance, my ‘get’ endpoint calls getData to interact with the database. I would write tests for getData first and make sure those are green. That way, I know that if any of my controller tests fail, it probably has to do with the way I’m calling getData.

Hopefully this write-up has helped you understand why testing is so useful and has equipped you with some tips on how to get started. This only hits the tip of the iceberg with testing, though! Here are some resources if you want to learn more:

[https://martinfowler.com/articles/mocksArentStubs.html](https://martinfowler.com/articles/mocksArentStubs.html)

[https://medium.com/@rickhanlonii/understanding-jest-mocks-f0046c68e53c](https://medium.com/@rickhanlonii/understanding-jest-mocks-f0046c68e53c)

If you enjoyed this article, please click on the ?? and share to help others find it. Thanks for reading!

