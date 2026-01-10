---
title: How to run tests in RxSwift
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-19T04:15:05.000Z'
originalURL: https://freecodecamp.org/news/testing-in-rxswift-2b6eeaeaf432
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ASJBAG5pLUIdEpVU4_RM2A.png
tags:
- name: coding
  slug: coding
- name: iOS
  slug: ios
- name: Reactive Programming
  slug: reactive-programming
- name: RxSwift
  slug: rxswift
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Navdeep Singh

  RxTest and RxBlocking are part of the RxSwift repository. They are made available
  via separate pods, however, and so require separate imports.

  RxTest provides useful additions for testing Rx code. It includes TestScheduler,
  which is ...'
---

By Navdeep Singh

**RxTest** and **RxBlocking** are part of the RxSwift repository. They are made available via separate pods, however, and so require separate imports.

**RxTest** provides useful additions for testing Rx code. It includes **TestScheduler**, which is a virtual time scheduler, and provides methods for adding events at precise time intervals.

**RxBlocking**, on the other hand, enables you to convert a regular Observable sequence to a blocking observable, which blocks the thread it’s running on until the observable sequence completes or a specified timeout is reached. This makes testing asynchronous operations much easier.

Let’s look at each one now.

### RxTest

As described above, **RxTest** is part of the same repository as **RxSwift.** There is one more thing to know about **RxTest** before we dive into some RxTesting: RxTest exposes two types of Observables for testing purposes.

* HotObservables
* ColdObservables

HotObservables replay events at specified times using a test scheduler, regardless of whether there are any subscribers.

ColdObservables work more like regular Observables, replaying their elements to their new subscribers upon subscription.

### RxBlocking

If you are familiar with expectations in **XCTest**, you will know that it’s another way to test asynchronous operations. Using RxBlocking just happens to be way easier. Let’s start with a small implementation so we can see how to take advantage of this library while testing asynchronous operations.

### Testing with RxBlocking

We will start a new test and create an Observable of 10, 20, and 30, as follows:

```
func testBlocking(){        let observableToTest = Observable.of(10, 20, 30)    }
```

Now we will define the result as equal to calling toBlocking() on the observable we created:

```
let result = observableToTest.toBlocking()
```

**toBlocking()** returns a blocking Observable to a straight array, as you can see here:

![Image](https://cdn-media-1.freecodecamp.org/images/1F4TF7RZ2FlBgcynP9tWUi9UqQBtLCCy6YSg)

We will need to use the first method if we want to discover which is a throwing method. So we will wrap it in a do catch statement, and then we will add an **AssertEquals** statement if it is successful, as follows:

```
func testBlocking(){        let observableToTest = Observable.of(10, 20, 30)        do{            let result = try observableToTest.toBlocking().first()            XCTAssertEqual(result, 10)        } catch {        }    }
```

Alternatively, an Assert fails if it’s not this:

```
do{            let result = try observableToTest.toBlocking().first()            XCTAssertEqual(result, 10)        } catch {            XCTFail(error.localizedDescription)        }
```

That’s it! Let’s run the test, and you will see that the test passes. We can simplify this test with just two lines of code by forcing the try.

Again, this is more acceptable on test than production code. We will comment out the do catch statement and then write the assert equals in a single line, as follows:

```
XCTAssertEqual(try! observableToTest.toBlocking().first(), 10)
```

Rerun the test, and you will see that the test passes once again. The overall code with comments looks like this:

```
func testBlocking(){        let observableToTest = Observable.of(10, 20, 30)//        do{//            let result = try observableToTest.toBlocking().first()//            XCTAssertEqual(result, 10)//        } catch {//            XCTFail(error.localizedDescription)//        }        XCTAssertEqual(try! observableToTest.toBlocking().first(), 10)    }
```

**How’s that for succinct?** Truth be told, that Observable sequence would actually be synchronous already if we printed emitted elements in a subscription to it followed by a marker. The marker will be printed after the subscription’s completed event.

To test an actual asynchronous operation, we will write one more test. This time, we will use a concurrent scheduler on a background thread, as follows:

```
func testAsynchronousToArry(){        let scheduler = ConcurrentDispatchQueueScheduler(qos: .background)    }
```

Now, we will create an Observable of the simple sequence of integers. We will use map to double each value, as follows:

```
let intObservbale = Observable.of(10, 20, 30)            .map{ $0 * 2 }
```

Then, we will subscribe on the scheduler:

```
let intObservbale = Observable.of(10, 20, 30)            .map{ $0 * 2 }            .subscribeOn(scheduler)
```

Now we will write a do catch statement that is similar to the last test and calls toBlocking on the Observable, which should be observed on the main scheduler, as follows:

```
do{   let result = try intObservbale.observeOn(MainScheduler.instance).toBlocking().toArray()   } catch {   }
```

Then, we will add the same assertions as the previous example:

```
do{   let result = try intObservbale.observeOn(MainScheduler.instance).toBlocking().toArray()            XCTAssertEqual(result, [20, 40, 60])        } catch {            XCTFail(error.localizedDescription)        }
```

Now we will run the test, and you will note that it passes with the green check mark in the gutter.

Note that the marker is printed before the emitted elements in the console, as shown:

![Image](https://cdn-media-1.freecodecamp.org/images/699d2sSCtcHgNblX68UK9VKzUBF-f1aTW8r0)

This is because these operations were executed asynchronously.

For other updates you can follow me on Twitter on my twitter handle @NavRudraSambyal

To work with examples of hot and cold observables, you can find the link to my book [Reactive programming in Swift 4](https://www.amazon.com/Reactive-Programming-Swift-easy-maintain-ebook/dp/B078MHNSL1/ref=asap_bc?ie=UTF8)

Thanks for reading, please share it if you found it useful :)

