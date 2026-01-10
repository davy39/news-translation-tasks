---
title: 'Concurrency Explained: How to Build a Multi-Threaded iOS App'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-28T01:24:39.000Z'
originalURL: https://freecodecamp.org/news/ios-concurrency
coverImage: https://www.freecodecamp.org/news/content/images/2020/03/onur-k-fHDVylCKLX0-unsplash-3.jpg
tags:
- name: concurrency
  slug: concurrency
- name: iOS
  slug: ios
seo_title: null
seo_desc: "By Besher Al Maleh\nConcurrency in iOS is a massive topic. So in this article\
  \ I want to zoom in on a sub-topic concerning queues and the Grand Central Dispatch\
  \ (GCD) framework. \nIn particular, I wish to explore the differences between serial\
  \ and concu..."
---

By Besher Al Maleh

Concurrency in iOS is a massive topic. So in this article I want to zoom in on a sub-topic concerning queues and the Grand Central Dispatch (GCD) framework. 

In particular, I wish to explore the differences between serial and concurrent queues, as well as the differences between synchronous and asynchronous execution.

If you've never used GCD before, this article is a great place to start. If you have some experience with GCD, but are still curious about the topics mentioned above, I think you will still find it useful. And I hope you will pick up one or two new things along the way. 

I created a SwiftUI companion app to visually demonstrate the concepts in this article. The app also has a fun short quiz that I encourage you to try before and after reading this article. [Download the source code here](https://github.com/almaleh/Dispatcher), or get the [public beta here](https://testflight.apple.com/join/2tC0CKMO).

I will begin with an introduction to GCD, followed by a detailed explanation on sync, async, serial and concurrent. Afterwards, I will cover some pitfalls when working with concurrency. Finally, I will end with a summary and some general advice.

## Introduction

Let’s start with a brief intro to GCD and dispatch queues. Feel free to skip to the **Sync vs Async** section if you are already familiar with the topic.

### Concurrency and Grand Central Dispatch

Concurrency lets you take advantage of the fact that your device has multiple CPU cores. To make use of these cores, you will need to use multiple threads. However, threads are a low-level tool, and managing threads manually in an efficient manner is extremely difficult.

[Grand Central Dispatch](https://developer.apple.com/documentation/DISPATCH) was created by Apple over 10 years ago as an abstraction to help developers write multi-threaded code without manually creating and managing the threads themselves.

With GCD, Apple took an [_asynchronous design approach_](https://developer.apple.com/library/archive/documentation/General/Conceptual/ConcurrencyProgrammingGuide/ConcurrencyandApplicationDesign/ConcurrencyandApplicationDesign.html#//apple_ref/doc/uid/TP40008091-CH100-SW8) to the problem. Instead of creating threads directly, you use GCD to schedule work tasks, and the system will perform these tasks for you by making the best use of its resources. GCD will handle creating the requisite threads and will schedule your tasks on those threads, shifting the burden of thread management from the developer to the system.

A big advantage of GCD is that you don’t have to worry about hardware resources as you write your concurrent code. GCD manages a thread pool for you, and it will scale from a single-core Apple Watch all the way up to a many-core MacBook Pro.

### Dispatch Queues

These are the main building blocks of GCD which let you execute arbitrary blocks of code using a set of parameters that you define. The tasks in dispatch queues are always started in a first-in, first-out (FIFO) fashion. Note that I said _started_, because the completion time of your tasks depends on several factors, and is not guaranteed to be FIFO (more on that later.)

Broadly speaking, there are three kinds of queues available to you:

* The Main dispatch queue (serial, pre-defined)
* Global queues (concurrent, pre-defined)
* Private queues (can be serial or concurrent, you create them)

Every app comes with a Main queue, which is a _serial_ queue that executes tasks on the main thread. This queue is responsible for drawing your application’s UI and responding to user interactions (touch, scroll, pan, etc.) If you block this queue for too long, your iOS app will appear to freeze, and your macOS app will display the infamous beach ball/spinning wheel.

When performing a long-running task (network call, computationally intensive work, etc), we avoid freezing the UI by performing this work on a background queue. Then we update the UI with the results on the main queue:

```swift
URLSession.shared.dataTask(with: url) { data, response, error in
    if let data = data {
        DispatchQueue.main.async { // UI work
            self.label.text = String(data: data, encoding: .utf8)
        }
    }
}
```

As a rule of thumb, all UI work must be executed on the Main queue. You can turn on the Main Thread Checker option in Xcode to receive warnings whenever UI work gets executed on a background thread.

![the main thread checker can be found in the scheme editor](https://www.freecodecamp.org/news/content/images/2020/01/1-HwivHHBJZKmFzhQfiJZ3nQ.png)

In addition to the main queue, every app comes with several pre-defined concurrent queues that have varying levels of [Quality of Service](https://developer.apple.com/library/archive/documentation/Performance/Conceptual/EnergyGuide-iOS/PrioritizeWorkWithQoS.html) (an abstract notion of priority in GCD.)

For example, here’s the code to submit work asynchronously to the _user interactive_ (highest priority) QoS queue:

```swift
DispatchQueue.global(qos: .userInteractive).async {
    print("We're on a global concurrent queue!") 
}
```

Alternatively, you can call the _default priority_ global queue by not specifying a QoS like this:

```swift
DispatchQueue.global().async {
    print("Generic global queue")
}
```

Additionally, you can create your own private queues using the following syntax:

```swift
let serial = DispatchQueue(label: "com.besher.serial-queue")
serial.async {
    print("Private serial queue")
}
```

When creating private queues, it helps to use a descriptive label (such as reverse DNS notation), as this will aid you while debugging in Xcode’s navigator, lldb, and Instruments:

![Image](https://www.freecodecamp.org/news/content/images/2020/01/1-vri5m4HJq2CBLeTUYg-RTQ-1.png)

![Image](https://www.freecodecamp.org/news/content/images/2020/01/1-zc_ZBGW9gVUF4h7TQA5Lgw.png)

By default, private queues are _serial_ (I’ll explain what this means shortly, promise!) If you want to create a private _concurrent_ queue, you can do so via the optional _attributes_ parameter:

```swift
let concurrent = DispatchQueue(label: "com.besher.serial-queue", attributes: .concurrent)
concurrent.sync {
    print("Private concurrent queue")
}
```

There is an optional QoS parameter as well. The private queues that you create will ultimately land in one of the global concurrent queues based on their given parameters.

### What’s in a task?

I mentioned dispatching tasks to queues. Tasks can refer to any block of code that you submit to a queue using the `sync` or `async` functions. They can be submitted in the form of an anonymous closure:

```swift
DispatchQueue.global().async {
    print("Anonymous closure")
}
```

Or inside a [dispatch work item](https://developer.apple.com/documentation/dispatch/dispatchworkitem) that gets performed later:

```swift
let item = DispatchWorkItem(qos: .utility) {
    print("Work item to be executed later")
}
```

Regardless of whether you dispatch synchronously or asynchronously, and whether you choose a serial or concurrent queue, all of the code inside a single task will execute line by line. Concurrency is only relevant when evaluating _multiple_ tasks.

For example, if you have 3 loops inside the **same** task, these loops will _always_ execute in order:

```swift
DispatchQueue.global().async {
    for i in 0..<10 {
        print(i)
    }

    for _ in 0..<10 {
        print("?")
    }

    for _ in 0..<10 {
        print("?")
    }
}
```

This code always prints out ten digits from 0 to 9, followed by ten blue circles, followed by ten broken hearts, regardless of how you dispatch that closure.

Individual tasks can also have their own QoS level as well (by default they use their queue’s priority.) This distinction between queue QoS and task QoS leads to some interesting behaviour that we will discuss in the priority inversion section.

By now you might be wondering what _serial_ and _concurrent_ are all about. You might also be wondering about the differences between `sync` and `async` when submitting your tasks. This brings us to the crux of this article, so let’s dive in!

## Sync vs Async

When you dispatch a task to a queue, you can choose to do so synchronously or asynchronously using the `sync` and `async` dispatch functions. Sync and async primarily affect the **source** of the submitted task, that is the queue where it is being submitted _from_.

When your code reaches a `sync` statement, it will block the current queue until that task completes. Once the task returns/completes, control is returned to the caller, and the code that follows the `sync` task will continue.

Think of `sync` as synonymous with ‘blocking’.

An `async` statement, on the other hand, will execute asynchronously with respect to the current queue, and immediately returns control back to the caller without waiting for the contents of the `async` closure to execute. There is no guarantee as to when exactly the code inside that async closure will execute.

### Current queue?

It may not be obvious what the source, or _current_, queue is, because it’s not always explicitly defined in the code. 

For example, if you call your `sync` statement inside viewDidLoad, your current queue will be the Main dispatch queue. If you call the same function inside a URLSession completion handler, your current queue will be a background queue.

Going back to sync vs async, let’s take this example:

```swift
DispatchQueue.global().sync {
    print("Inside")
}
print("Outside")
// Console output:
// Inside
// Outside
```

The above code will block the current queue, enter the closure and execute its code on the global queue by printing “Inside”, before proceeding to print “Outside”. This order is guaranteed.

Let’s see what happens if we try `async` instead:

```swift
DispatchQueue.global().async {
    print("Inside")
}
print("Outside")
// Potential console output (based on QoS): 
// Outside
// Inside
```

Our code now submits the closure to the global queue, then immediately proceeds to run the next line. It will _likely_ print “Outside” before “Inside”, but this order isn’t guaranteed. It depends on the QoS of the source and destination queues, as well as other factors that the system controls.

Threads are an implementation detail in GCD — we do not have direct control over them and can only deal with them using queue abstractions. Nevertheless, I think it can be useful to ‘peek under the covers’ at thread behaviour to understand some challenges we might encounter with GCD.

For instance, when you submit a task using `sync`, [GCD optimizes performance by executing that task on the current thread](https://developer.apple.com/documentation/dispatch/1452870-dispatch_sync?language=objc) (the caller.) 

There is one exception however, which is when you submit a sync task to the main queue —  doing so will always run the task on the main thread and not the caller. This behaviour can have some ramifications that we will explore in the priority inversion section.

![Image](https://www.freecodecamp.org/news/content/images/2020/01/Sync-400.gif)
_[From Dispatcher on Github](https://github.com/almaleh/Dispatcher" rel="noopener nofollow)_

### Which one to use?

When submitting work to a queue, [Apple recommends using asynchronous execution over synchronous execution](https://developer.apple.com/library/archive/documentation/General/Conceptual/ConcurrencyProgrammingGuide/OperationQueues/OperationQueues.html#//apple_ref/doc/uid/TP40008091-CH102-SW21). However, there are situations where `sync` might be the better choice, such as when dealing with race conditions, or when performing a very small task. I will cover these situations shortly.

One large consequence of performing work asynchronously inside a function is that the function can no longer directly return its values (if they depend on the async work that’s being done). It must instead use a closure/completion handler parameter to deliver the results.

To demonstrate this concept, let’s take a small function that accepts image data, performs some expensive computation to process the image, then returns the result:

```swift
func processImage(data: Data) -> UIImage? {
    guard let image = UIImage(data: data) else { return nil }
    // calling an expensive function
    let processedImage = upscaleAndFilter(image: image)
    return processedImage 
}
```

In this example, the function `upscaleAndFilter(image:)` might take several seconds, so we want to offload it into a separate queue to avoid freezing the UI. Let’s create a dedicated queue for image processing, and then dispatch the expensive function asynchronously:

```swift
let imageProcessingQueue = DispatchQueue(label: "com.besher.image-processing")

func processImageAsync(data: Data) -> UIImage? {
    guard let image = UIImage(data: data) else { return nil }
    
    imageProcessingQueue.async {
        let processedImage = upscaleAndFilter(image: image)
        return processedImage
    }
}
```

There are two issues with this code. First, the return statement is inside the async closure, so it is no longer returning a value to the `processImageAsync(data:)` function, and currently serves no purpose. 

But the bigger issue is that our `processImageAsync(data:)` function is no longer returning any value, because the function reaches the end of its body before it enters the `async` closure.

To fix this error, we will adjust the function so that it no longer directly returns a value. Instead, it will have a new completion handler parameter that we can call once our asynchronous function has completed its work:

```swift
let imageProcessingQueue = DispatchQueue(label: "com.besher.image-processing")

func processImageAsync(data: Data, completion: @escaping (UIImage?) -> Void) {
    guard let image = UIImage(data: data) else {
        completion(nil)
        return
    }

    imageProcessingQueue.async {
        let processedImage =  self.upscaleAndFilter(image: image)
        completion(processedImage)
    }
}
```

As evident in this example, the change to make the function asynchronous has propagated to its caller, who now has to pass in a closure and handle the results asynchronously as well. By introducing an asynchronous task, you can potentially end up modifying a chain of several functions.

Concurrency and asynchronous execution add complexity to your project as we just observed. This indirection also makes debugging more difficult. That’s why it really pays off to think about concurrency early in your design — it’s not something you want to tack on at the end of your design cycle.

Synchronous execution, by contrast, does not increase complexity. Rather, it allows you to continue using return statements as you did before. A function containing a `sync` task will not return until the code inside that task has completed. Therefore it does not require a completion handler.

If you are submitting a tiny task (for example, updating a value), consider doing it synchronously. Not only does that help you keep your code simple, it will also perform better — Async is believed to [incur an overhead](https://gist.github.com/tclementdev/6af616354912b0347cdf6db159c37057) that outweighs the benefit of doing the work asynchronously for tiny tasks that take under 1ms to complete.

If you are submitting a large task, however, like the image processing we performed above, then consider doing it asynchronously to avoid blocking the caller for too long.

### Dispatching on the same queue

While it is safe to dispatch a task asynchronously from a queue into itself (for example, you can use [.asyncAfter](https://developer.apple.com/documentation/dispatch/dispatchqueue/2300020-asyncafter) on the current queue), you can not dispatch a task _synchronously_ from a queue into the same queue. Doing so will result in a deadlock that immediately crashes the app!

This issue can manifest itself when performing a chain of synchronous calls that lead back to the original queue. That is, you `sync` a task onto another queue, and when the task completes, it syncs the results back into the original queue, leading to a deadlock. Use `async` to avoid such crashes.

### Blocking the main queue

Dispatching tasks synchronously _from_ the main queue will block that queue, thereby freezing the UI, until the task is completed. Thus it’s better to avoid dispatching work synchronously from the main queue unless you’re performing really light work.

![Image](https://www.freecodecamp.org/news/content/images/2020/01/Async-400.gif)
_[prefer to use async from the main queue](https://github.com/almaleh/Dispatcher" rel="noopener nofollow)_

## Serial vs Concurrent

_Serial_ and _concurrent_ affect the **destination** —  the queue in which your work has been submitted to run. This is in contrast to _sync_ and _async_, which affected the **source**.

A serial queue will not execute its work on more than one thread at a time, regardless of how many tasks you dispatch on that queue. Consequently, the tasks are guaranteed to not only start, but also terminate, in first-in, first-out order. 

Moreover, when you block a serial queue (using a `sync` call, semaphore, or some other tool), all work on that queue will halt until the block is over.

![Image](https://www.freecodecamp.org/news/content/images/2020/01/Serial-400.gif)
_[From Dispatcher on Github](https://github.com/almaleh/Dispatcher" rel="noopener nofollow)_

A concurrent queue can spawn multiple threads, and the system decides how many threads are created. Tasks always _start_ in FIFO order, but the queue does not wait for tasks to finish before starting the next task, therefore tasks on concurrent queues can finish in any order. 

When you perform a blocking command on a concurrent queue, it will not block the other threads on this queue. Additionally, when a concurrent queue gets blocked, it runs the risk of _thread explosion_. I will cover this in more detail later on.

![Image](https://www.freecodecamp.org/news/content/images/2020/01/Concurrent-400.gif)
_[From Dispatcher on Github](https://github.com/almaleh/Dispatcher" rel="noopener nofollow)_

The main queue in your app is serial. All the global pre-defined queues are concurrent. Any private dispatch queue you create is serial by default, but can be set to be concurrent using an optional attribute as discussed earlier.

It’s important to note here that the concept of _serial_ vs _concurrent_ is only relevant when discussing a specific queue. All queues are concurrent relative to _each other_. 

That is, if you dispatch work asynchronously from the main queue to a private _serial_ queue, that work will be completed _concurrently_ with respect to the main queue. And if you create two different serial queues, and then perform blocking work on one of them, the other queue is unaffected.

To demonstrate the concurrency of multiple serial queues, let’s take this example:

```swift
let serial1 = DispatchQueue(label: "com.besher.serial1")
let serial2 = DispatchQueue(label: "com.besher.serial2")

serial1.async {
    for _ in 0..<5 { print("?") }
}

serial2.async {
    for _ in 0..<5 { print("?") }
}
```

![Image](https://www.freecodecamp.org/news/content/images/2020/01/1-zJztLeessQUMvONpoLW0ZQ.png)

Both queues here are serial, but the results are jumbled up because they execute concurrently in relation to each other. The fact that they’re each serial (or concurrent) has no effect on this result. Their QoS level determines who will _generally_ finish first (order not guaranteed).

If we want to ensure that the first loop finishes first before starting the second loop, we can submit the first task synchronously from the caller:

```swift
let serial1 = DispatchQueue(label: "com.besher.serial1")
let serial2 = DispatchQueue(label: "com.besher.serial2")

serial1.sync { // <---- we changed this to 'sync'
    for _ in 0..<5 { print("?") }
}
// we don't get here until first loop terminates
serial2.async {
    for _ in 0..<5 { print("?") }
}
```

![Image](https://www.freecodecamp.org/news/content/images/2020/01/1-s1N-5HfXpcAtsKQ3tZ-DHQ-2.png)

This is not necessarily desirable, because we are now blocking the caller while the first loop is executing.

To avoid blocking the caller, we can submit both tasks asynchronously, but to the _same_ serial queue:

```swift
let serial = DispatchQueue(label: "com.besher.serial")

serial.async {
    for _ in 0..<5 { print("?") }
}

serial.async {
    for _ in 0..<5 { print("?") }
}	
```

![Image](https://www.freecodecamp.org/news/content/images/2020/01/1-s1N-5HfXpcAtsKQ3tZ-DHQ-2-1.png)

Now our tasks execute concurrently with respect to the _caller_, while also keeping their order intact.

Note that if we make our single queue concurrent via the optional parameter, we go back to the jumbled results, as expected:

```swift
let concurrent = DispatchQueue(label: "com.besher.concurrent", attributes: .concurrent)

concurrent.async {
    for _ in 0..<5 { print("?") }
}

concurrent.async {
    for _ in 0..<5 { print("?") }
}
```

![Image](https://www.freecodecamp.org/news/content/images/2020/01/1-zJztLeessQUMvONpoLW0ZQ-1.png)

Sometimes you might confuse synchronous execution with serial execution (at least I did), but they are very different things. For example, try changing the first dispatch on line 3 from our previous example to a `sync` call:

```swift
let concurrent = DispatchQueue(label: "com.besher.concurrent", attributes: .concurrent)

concurrent.sync {
    for _ in 0..<5 { print("?") }
}

concurrent.async {
    for _ in 0..<5 { print("?") }
}
```

![Image](https://www.freecodecamp.org/news/content/images/2020/01/1-s1N-5HfXpcAtsKQ3tZ-DHQ.png)

Suddenly, our results are back in perfect order. But this is a concurrent queue, so how could that happen? Did the `sync` statement somehow turn it into a serial queue?

The answer is **no!**

This is a bit sneaky. What happened is that we did not reach the `async` call until the first task had completed its execution. The queue is still very much concurrent, but inside this zoomed-in section of the code. it appears as if it were serial. This is because we are blocking the caller, and not proceeding to the next task, until the first one is finished.

If another queue somewhere else in your app tried submitting work to this same queue while it was still executing the `sync` statement, that work _will_ run concurrently with whatever we got running here, because it’s still a concurrent queue.

### Which one to use?

Serial queues take advantage of CPU optimizations and caching, and help reduce context switching. 

Apple recommends starting with one serial queue per subsystem in your app —  for example one for networking, one for file compression, etc. If the need arises, you can later expand to a [hierarchy of queues per subsystem](https://developer.apple.com/videos/play/wwdc2017/706/) using the [setTarget method](https://developer.apple.com/documentation/dispatch/dispatchobject/1452989-settarget) or the [optional target parameter](https://developer.apple.com/documentation/dispatch/dispatchqueue/2300059-init) when building queues.

If you run into a performance bottleneck, measure your app’s performance then see if a concurrent queue helps. If you do not see a measurable benefit, it’s better to stick to serial queues.

## Pitfalls

### Priority Inversion and Quality of Service

[Priority inversion](https://en.wikipedia.org/wiki/Priority_inversion) is when a high priority task is prevented from running by a lower priority task, effectively inverting their relative priorities.

This situation often occurs when a high QoS queue shares a resources with a low QoS queue, and the low QoS queue gets a lock on that resource. 

But I wish to cover a different scenario that is more relevant to our discussion —  it’s when you submit tasks to a low QoS serial queue, then submit a high QoS task to that same queue. This scenario also results in priority inversion, because the high QoS task has to wait on the lower QoS tasks to finish.

GCD resolves priority inversion by temporarily raising the QoS of the queue that contains the low priority tasks that are ‘ahead’ of, or blocking, your high priority task. 

It’s kind of like having cars stuck _in front_ _of_ an ambulance. Suddenly they’re allowed to cross the red light just so that the ambulance can move (in reality the cars move to the side, but imagine a narrow (serial) street or something, you get the point :-P)

To illustrate the inversion problem, let’s start with this code:

```swift

enum Color: String {
    case blue = "?"
    case white = "⚪️"
}

func output(color: Color, times: Int) {
    for _ in 1...times {
        print(color.rawValue)
    }
}

let starterQueue = DispatchQueue(label: "com.besher.starter", qos: .userInteractive)
let utilityQueue = DispatchQueue(label: "com.besher.utility", qos: .utility)
let backgroundQueue = DispatchQueue(label: "com.besher.background", qos: .background)
let count = 10

starterQueue.async {

    backgroundQueue.async {
        output(color: .white, times: count)
    }

    backgroundQueue.async {
        output(color: .white, times: count)
    }

    utilityQueue.async {
        output(color: .blue, times: count)
    }

    utilityQueue.async {
        output(color: .blue, times: count)
    }

    // next statement goes here
}
```

We create a starter queue (where we submit the tasks _from_), as well as two queues with different QoS. Then we dispatch tasks to each of these two queues, each task printing out an equal number of circles of a specific colour (_utility_ queue is blue, _background_ is white.)

Because these tasks are submitted asynchronously, every time you run the app, you’re going to see slightly different results. However, as you would expect, the queue with the lower QoS (background) almost always finishes last. In fact, the last 10–15 circles are usually all white.

![Image](https://www.freecodecamp.org/news/content/images/2020/01/1-woRLw218x4QZKFov0w1hDA.gif)
_no surprises here_

But watch what happens when we submit a **sync** task to the background queue after the last async statement. You don’t even need to print anything inside the `sync` statement, just adding this line is enough:

```swift
// add this after the last async statement, 
// still inside starterQueue.async
backgroundQueue.sync {}
```

![Image](https://www.freecodecamp.org/news/content/images/2020/01/1-yxMCgE4Vy8Ws2309CvYelA.gif)
_priority inversion_

The results in the console have flipped! Now, the higher priority queue (utility) always finishes last, and the last 10–15 circles are _blue._

To understand why that happens, we need to revisit the fact that synchronous work is executed on the caller thread (unless you’re submitting to the main queue.) 

In our example above, the caller (starterQueue) has the top QoS (userInteractive.) Therefore, that seemingly innocuous `sync` task is not only blocking the starter queue, but it’s also running on the starter’s high QoS thread. The task therefore runs with high QoS, but there are two other tasks ahead of it on the same background queue that have _background_ QoS. Priority inversion detected!

As expected, GCD resolves this inversion by raising the QoS of the entire queue to temporarily match the high QoS task. Consequently, all the tasks on the background queue end up running at _user interactive_ QoS, which is higher than the _utility_ QoS. And that’s why the utility tasks finish last!

Side-note: If you remove the starter queue from that example and submit from the main queue instead, you will get similar results, as the main queue also has _user interactive_ QoS.

To avoid priority inversion in this example, we need to avoid blocking the starter queue with the `sync` statement. Using `async` would solve that problem.

Although it’s not always ideal, you can minimize priority inversions by sticking to the default QoS when creating private queues or dispatching to the global concurrent queue.

### Thread explosion

When you use a concurrent queue, you run the risk of thread explosion if you’re not careful. This can happen when you try to submit tasks to a concurrent queue that is currently blocked (for example with a semaphore, sync, or some other way.) Your tasks _will_ run, but the system will likely end up spinning up new threads to accommodate these new tasks, and threads aren’t cheap.

This is likely why Apple suggests starting with a serial queue per subsystem in your app, as each serial queue can only use one thread. Remember that serial queues are concurrent in relation to _other_ queues, so you still get a performance benefit when you offload your work to a queue, even if it isn’t concurrent.

### Race conditions

Swift Arrays, Dictionaries, Structs, and other value types are not thread-safe by default. For example, when you have multiple threads trying to access and **modify** the same array, you will start running into trouble.

There are different solutions to [the readers-writers problem](https://en.wikipedia.org/wiki/Readers%E2%80%93writers_problem), such as using locks or semaphores. But the relevant solution I wish to discuss here is the use of an [isolation queue](http://khanlou.com/2016/04/the-GCD-handbook/).

Let’s say we have an array of integers, and we want to submit asynchronous work that references this array. As long as our work only _reads_ the array and does not modify it, we are safe. But as soon as we try to modify the array in one of our asynchronous tasks, we will introduce instability in our app.

It’s a tricky problem because your app can run 10 times without issues, and then it crashes on the 11th time. One very handy tool for this situation is the Thread Sanitizer in Xcode. Enabling this option will help you identify potential race conditions in your app.

![the thread sanitizer can be accessed in the scheme editor](https://www.freecodecamp.org/news/content/images/2020/01/1-SQpYE8quVN_ziJsg8bqrYQ.png)
_**t**his option is only available on the simulator****_

To demonstrate the problem, let’s take this (admittedly contrived) example:

```swift
class ViewController: UIViewController {
    
    let concurrent = DispatchQueue(label: "com.besher.concurrent", attributes: .concurrent)
    var array = [1,2,3,4,5]

    override func viewDidLoad() {
        for _ in 0...1 {
            race()
        }
    }

    func race() {

        concurrent.async {
            for i in self.array { // read access
                print(i)
            }
        }

        concurrent.async {
            for i in 0..<10 {
                self.array.append(i) // write access
            }
        }
    }
}
```

One of the `async` tasks is modifying the array by appending values. If you try running this on your simulator, you might not crash. But run it enough times (or increase the loop frequency on line 7), and you will eventually crash. If you enable the thread sanitizer, you will get a warning every time you run the app.

![Image](https://www.freecodecamp.org/news/content/images/2020/01/1-NNBN1ZKViVwYzqJfZenaeQ.png)

To deal with this race condition, we are going to add an isolation queue that uses the [barrier flag](https://developer.apple.com/documentation/dispatch/dispatchworkitemflags/1780674-barrier). This flag allows any outstanding tasks on the queue to finish, but blocks any further tasks from executing until the barrier task is completed.

Think of the barrier like a janitor cleaning a public restroom (shared resource.) There are multiple (concurrent) stalls inside the restroom that people can use. 

Upon arrival, the janitor places a cleaning sign (barrier) blocking any newcomers from entering until the cleaning is done, but the janitor does not start cleaning until all the people inside have finished their business. Once they all leave, the janitor proceeds to clean the public restroom in isolation. 

When finally done, the janitor removes the sign (barrier) so that the people who are queued up outside can finally enter.

Here’s what that looks like in code:

```swift
class ViewController: UIViewController {
    let concurrent = DispatchQueue(label: "com.besher.concurrent", attributes: .concurrent)
    let isolation = DispatchQueue(label: "com.besher.isolation", attributes: .concurrent)
    private var _array = [1,2,3,4,5]
    
    var threadSafeArray: [Int] {
        get {
            return isolation.sync {
                _array
            }
        }
        set {
            isolation.async(flags: .barrier) {
                self._array = newValue
            }
        }
    }
    
    override func viewDidLoad() {
        for _ in 0...15 {
            race()
        }
    }
    
    func race() {
        concurrent.async {
            for i in self.threadSafeArray {
                print(i)
            }
        }
        
        concurrent.async {
            for i in 0..<10 {
                self.threadSafeArray.append(i)
            }
        }
    }
}
```

We have added a new isolation queue, and restricted access to the private array using a getter and setter that will place a barrier when modifying the array.

The getter needs to be `sync` in order to directly return a value. The setter can be `async`, as we don’t need to block the caller while the write is taking place.

We could have used a serial queue without a barrier to solve the race condition, but then we would lose the advantage of having concurrent read access to the array. Perhaps that makes sense in your case, you get to decide.

## Conclusion

Thank you so much for reading this far! I hope you learned something new from this article. I will leave you with a summary and some general advice:

### Summary

* Queues always _start_ their tasks in FIFO order
* Queues are always concurrent relative to _other_ queues
* **Sync** vs **Async** concerns the source
* **Serial** vs **Concurrent** concerns the destination
* Sync is synonymous with ‘blocking’
* Async immediately returns control to caller
* Serial uses a single thread, and guarantees order of execution
* Concurrent uses multiple-threads, and risks thread explosion
* Think about concurrency early in your design cycle
* Synchronous code is easier to reason about and debug
* Avoid relying on global concurrent queues if possible
* Consider starting with a serial queue per subsystem
* Switch to concurrent queue only if you see a **measurable** performance benefit

I like the metaphor from the [Swift Concurrency Manifesto](https://gist.github.com/lattner/31ed37682ef1576b16bca1432ea9f782) of having an ‘island of serialization in a sea of concurrency’. This sentiment was also shared in this tweet by Matt Diephouse:

%[https://twitter.com/mdiep/status/1207112168224763905?s=20]

When you apply concurrency with that philosophy in mind, I think it will help you achieve concurrent code that can be reasoned about without getting lost in a mess of callbacks.

If you have any questions or comments, feel free to reach out to me on [Twitter](https://twitter.com/BesherMaleh)

[Besher Al Maleh](https://www.besher.ca)

_Cover photo by [Onur K](https://unsplash.com/@kodozani?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/s/photos/railway?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)_

### Download the companion app here: 

%[https://github.com/almaleh/Dispatcher]

#### Check out some of my other articles:

%[https://medium.com/flawless-app-stories/fireworks-a-visual-particles-editor-for-swift-618e76347798]

%[https://medium.com/flawless-app-stories/you-dont-always-need-weak-self-a778bec505ef]

#### Further reading:

%[https://developer.apple.com/library/archive/documentation/General/Conceptual/ConcurrencyProgrammingGuide/Introduction/Introduction.html]

%[https://www.objc.io/issues/2-concurrency/concurrency-apis-and-pitfalls/#grand-central-dispatch]

%[https://www.objc.io/issues/2-concurrency/low-level-concurrency-apis/]

[http://khanlou.com/2016/04/the-GCD-handbook/](http://khanlou.com/2016/04/the-GCD-handbook/)

%[https://stackoverflow.com/a/53582047]

#### WWDC Videos:

%[https://developer.apple.com/videos/play/wwdc2017/706/]

%[https://developer.apple.com/videos/play/wwdc2015/718/]


