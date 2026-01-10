---
title: How to get a grip on the four constructs of an RxJava routine
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-09T23:17:10.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-a-grip-on-the-four-constructs-of-an-rxjava-routine-32addd16349e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*EqESoVsAoU6eWUMYIA4wxA.png
tags:
- name: Android
  slug: android
- name: Java
  slug: java
- name: mobile app development
  slug: mobile-app-development
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Ayusch Jain


  This article was originally posted here.


  RxJava has become the single most important weapon in the android development arsenal.
  Every developer in 2019 must start using it in their apps if they haven’t already.
  According to the offic...'
---

By Ayusch Jain

> [_This article was originally posted here_](https://www.ayusch.com/understanding-rxjava-basics)_._

RxJava has become the single most important weapon in the android development arsenal. Every developer in 2019 must start using it in their apps if they haven’t already. According to the official definition of RxJava:

> _“RxJava is a Java VM implementation of [Reactive Extensions](http://reactivex.io/): a library for composing asynchronous and event-based programs by using observable sequences.”_

This definition can sound intimidating with all the technical terms such as Java VM, Reactive Extensions, Asynchronous event-based, observable sequences etc. But guess what? You’ve been using all these things in your day to day android development tasks unknowingly.

> _Note: I’m assuming that if you’re looking to dive deep into RxJava then you have a good knowledge of Java programming language. If not, you can find various [online schools](https://www.microverse.org/) which can help you with this._

### Getting Started

Let’s start with the **Java VM (or JVM).** Ever wondered how your code written using the English alphabet gets translated to pixels on the screen? How your color changes in code translate to color changes on the screen? Well, it’s all done by the JVM.

First, your source code is compiled into Bytecode by the compiler. Now comes in the JVM that takes that Bytecode and converts it into something that the machine can understand. In other [languages](https://www.ayusch.com/understanding-rxjava-basics), the compiler converts the code for a particular system, but Java’s compiler converts the source code to Bytecode which can be run on any machine with JVM.

Now, do you understand why Kotlin can be used to write Android applications? If not, then be on the lookout for my next post.

### **Reactive Extensions**

Reactive Extensions or ReactiveX has been around for a long time. It is nothing but an API that makes reactive programming easy.

Unknowingly we have been writing reactive code all along. For example, when a button click happens, it triggers a certain block of code in your source file. This is reactive programming! A piece of code has reacted to an event (button click in this case).

[Reactive Extensions](https://www.ayusch.com/understanding-rxjava-basics) is not specific to any programming language but more of a methodology which has been implemented in languages such as Java (RxJava), JavaScript (RxJS), C# (Rx.NET), Scala (RxScala) and many others! So, you see, ReactiveX is not language specific but is more of a design pattern that can be implemented in any language.

### Constructs of RxJava

RxJava basically has 4 constructs:

* Observable
* Scheduler
* Observer
* Subscriber

These 4 components are present in all the RxJava routines. Although these are not necessary, I’d recommend that you stick to them as a beginner. Once you get comfortable with RxJava, you can throw the rules out the window and start playing around. But before you get to that level, just stick to the basics.

So let’s look at each one of these constructs in more detail.

#### **Observable**

An Observable is exactly what it sounds like: something that can be observed. An observable (button) in RxJava is watched upon by an Observer (code that runs on a button click) which reacts to any events emitted (button click event) by the observable. This pattern facilitates concurrent operations as the main thread need not be blocked while waiting for the observable to emit events. The observer is always ready to react as soon as the observable emits.

RxJava follows the observer pattern in which an Observer (explained later) subscribes to an Observable which emits events/data and then reacts accordingly. The concepts in RxJava are best explained with the help of Marble diagrams. So here is one for you:

![Image](https://cdn-media-1.freecodecamp.org/images/qhMY4gqVCAcxjxD-bn35bEFAABTt9PDiNAtG)

In ReactiveX, many instructions may execute in parallel and their results are later captured, in arbitrary order, by “**observers**.” Rather than calling a method, you define a mechanism for retrieving and transforming the data, in the form of an “**Observable.**” Then you subscribe an observer to it, at which point the previously-defined mechanism fires into action with the observer standing sentry to capture and respond to its emissions whenever they are ready.

An advantage of this approach is that when you have a bunch of tasks that are not dependent on each other, you can start them all at the same time rather than waiting for each one to finish before starting the next one. That way, your entire bundle of tasks only takes as long to complete as the longest task in the bundle.

#### [**Schedulers _(important)_**](https://www.ayusch.com/understanding-rxjava-basics)

One of the super cool features of RxJava is that it provides for instant concurrency. **Concurrency** is really difficult to understand. Even today it is one of the most complex topics in computer science and is really hard to implement.

The geniuses who wrote RxJava have abstracted all of these complexities away for us, giving us relatively simpler APIs to work with. RxJava handles concurrency with the help of Schedulers. In the RxJava routine, we have an operator named

```
subscribeOn()
```

> **_It basically says:_** Here is an observable and an observer, take them and establish their connection on this particular thread.

All of this can be achieved with pure Java using Threads, Handlers, Executors etc, but Schedulers are just an elegant way of handling it.

Generally, most of the operations are delegated to the IO thread. But there are many other scheduler types. Here are some of the most commonly used:

* **Schedulers.io():** used for non-computational IO tasks such as File Management, making network calls, database management etc. This thread pool is intended to be used for asynchronous tasks.
* **Schedulers.computation():** As the name suggests, it is intended to be used for computation-heavy tasks such as image processing, dataset processing etc. It has as many numbers of threads as the number of available processors. But you should be careful while using it as it can lead to degradation in performance due to context switching in threads.
* **Schedulers.from(Executor ex):** creates and returns a custom scheduler backed by a specific executor.
* **Schedulers.mainThread():** Hey, I haven’t forgotten about you Android Devs ? This is provided by RxAndroid library and provides us with the main thread. Be careful not to perform long running tasks on this thread as it is synchronous and can lead to ANRs.

There is also an operator named

```
observeOn()
```

As we saw above, **subscribeOn()** instructs the source Observable which thread to emit items on — this thread will push the emissions all the way to our Observer. However, if it encounters an observeOn() anywhere in the chain, it will switch and pass emissions using that Scheduler for the remaining (downstream) operations.

### **Observer/Subscriber**

As an artist needs an audience, the observable also needs someone to observe it while it emits items. There can be emissions without an observer (google hot and cold observables), but that’s a story for some other time.

An **observer** subscribes to the observable with the help of the subscribe() method. As soon as the observer subscribes, it is ready to receive notifications from the observable.

It provides three methods to handle the notifications:

* **onNext():** In this method, the notification is delivered to the subscriber without any errors.
* **onError():** A throwable is sent to the subscriber in onError outlining the error.
* **onComplete():** This is called at the end when the source has finished emitting.

Depending upon whether you were observing on the main thread or a separate thread, you’ll be getting the emissions in the onNext in the main thread or a new thread.

When a Subscriber subscribes to a Publisher then in RxJava2, a Disposable instance is returned which can be used to cancel/dispose a Subscriber externally via Disposable::dispose().

Here is a diagram to help you understand this relationship better:

[caption id=”attachment_1032" align=”aligncenter” width=”1340"]

![Image](https://cdn-media-1.freecodecamp.org/images/pElm1-RWq8hbX1KQU-eFlfpxQud0esO0k1Xf)

Image Source [[Mindorks](https://mindorks.com/course/learn-rxjava/public/chapter/id/2/page/id/7)][/caption]

### Should I even use RxJava?

Instead of making my case verbally, I’ll leave it up to you to decide. Just go through the code below.

#### Java

```
List<Integer> temp = Arrays.asList(5,8,9,20,30,40);List<Integer> javaList = new ArrayList<>();
```

```
for(Integer i: temp){    if(i>10)        javaList.add(i);}
```

#### RxJava

```
List<Integer> rxlist = Stream.of(5, 8, 9, 20, 30, 40).filter(x -> x > 10).        collect(Collectors.toList());
```

#### Java

```
TPExecutor.execute(() -> api.getUserDetails(userId))        .runOnUIAfterBoth(TPExecutor.execute(() -> api.getUserPhoto(userId)), p -> {            // Do your task        });
```

#### RxJava

```
Observable.zip(api.getUserDetails2(userId), api.getUserPhoto2(userId), (details, photo) -> Pair.of(details, photo))        .subscribe(p -> {            // Do your task.        });
```

#### **AsyncTask**

```
private class MyTask extends AsyncTask<String, Integer, Boolean>{    @Override    protected Boolean doInBackground(String... paths)    {        for (int index = 0; index < paths.length; index++)        {            boolean result = copyFileToExternal(paths[index]);
```

```
            if (result == true)            {                // update UI                publishProgress(index);            }            else            {                // stop the background process                return false;            }        }
```

```
        return true;    }
```

```
    @Override    protected void onProgressUpdate(Integer... values)    {        super.onProgressUpdate(values);        int count = values[0];        // this will update my textview to show the number of files copied        myTextView.setText("Total files: " + count);    }
```

```
    @Override    protected void onPostExecute(Boolean result)    {        super.onPostExecute(result);        if (result)        {            // display a success dialog            ShowSuccessAlertDialog();        }        else        {            // display a fail dialog            ShowFailAlertDialog();        }    }}
```

#### **RxJava**

```
Observable.fromArray(getPaths())        .map(path -> copyFileToExternal(path))        .subscribeOn(Schedulers.io())        .observeOn(AndroidSchedulers.mainThread())        .subscribe(aInteger -> Log.i("test", "update UI"),                throwable -> ShowFailAlertDialog),        () -> ShowSuccessAlertDialog());
```

You can see that the RxJava code is much more readable and concise (lambda expressions can get a little daunting if you are unfamiliar with them, but once you start using them, this code would feel like second nature to you). And there are many more examples where RxJava operators unleash their power over traditional Java programming.

### Disadvantages

I have not found any disadvantage in using RxJava up to this point — just that it has a really **steep learning** curve. If you aren’t already familiar with Observer pattern, **Java 8** (not mandatory but really useful), lambdas etc, you’ll find RxJava code really intimidating.

But as you start patching your code with RxJava you’ll slowly start getting the hang of it and will realize that most of the constructs in RxJava remain the same.

[This post has a complete list of resources to get you started.](https://blog.mindorks.com/a-complete-guide-to-learn-rxjava-b55c0cea3631)

_Like what you read? Don’t forget to share this post on [**Facebook**](https://www.facebook.com/AndroidVille), **Whatsapp**, and **LinkedIn**._

_You can follow me on [LinkedIn](https://www.linkedin.com/in/ayuschjain), [Quora](https://www.quora.com/profile/Ayusch-Jain), [Twitter](https://twitter.com/ayuschjain), and [Instagram](https://www.instagram.com/androidville/) where I answer questions related to **Mobile Development, especially Android and Flutter**._

![Image](https://cdn-media-1.freecodecamp.org/images/NNWIaau9-uWSJFA1fHCjrcfMrOQo-fMAWAZm)

