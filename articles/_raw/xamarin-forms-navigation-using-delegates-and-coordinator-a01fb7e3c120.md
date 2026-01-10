---
title: How to implement Xamarin.Forms navigation using delegates and coordinators
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-20T17:36:13.000Z'
originalURL: https://freecodecamp.org/news/xamarin-forms-navigation-using-delegates-and-coordinator-a01fb7e3c120
coverImage: https://cdn-media-1.freecodecamp.org/images/1*jQnSCD-sqgoSDH9ucrFRKA.jpeg
tags:
- name: mobile app development
  slug: mobile-app-development
- name: General Programming
  slug: programming
- name: software architecture
  slug: software-architecture
- name: software development
  slug: software-development
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Rafael Fiol

  Recently I have been thinking a lot about how to best implement page navigation
  within a Xamarin.Forms mobile app. My deep-dive into this topic started when a colleague
  sent me an article entitled The Coordinator, written by Soroush Kh...'
---

By Rafael Fiol

Recently I have been thinking a lot about how to best implement page navigation within a Xamarin.Forms mobile app. My deep-dive into this topic started when a colleague sent me an article entitled [The Coordinator](http://khanlou.com/2015/10/coordinators-redux/), written by [Soroush Khanlou](http://khanlou.com/). Initially, I was a very happy passenger on the Coordinator bandwagon. I guess I still am. It’s a wonderful way to think about and implement [separation of concerns](https://en.wikipedia.org/wiki/Separation_of_concerns) with respect to UI/UX and general navigation.

The following notes represent my thoughts on the subject, learnings with regard to an implementation in Xamarin.Forms, and how **delegates** in C# can help.

### Why Coordinators?

Soroush’s solution focuses primarily on the problems with overstuffed view controllers (citing the iOS UIViewController as a primary example), and suggests that a Coordinator’s primary responsibility should be to take over navigation and model mutation. He states that:

> When we take those tasks out of a view controller, we end up with a view controller that’s _inert_. It can be presented, it can fetch data, transform it for presentation, display it, but it crucially can’t alter it.

This is good. This is what we want. It means that we can reuse our view controllers as participants in multiple workflows, with purpose-built Coordinators for each workflow. Our Pages and View Models — in our MVVM applications — will no longer have messy navigation concerns.

Consider this common scenario. Let’s imagine that your app includes a login page. After a user completes the login page, your app then displays a dashboard page. Then, in a later design incarnation of your app, you decide that not all pages require a login. What if you want to reuse that login page elsewhere, and go to a different post-login page depending on the workflow that triggers the login?

The obvious (and ugly) solution is to start littering your Pages or View Models with conditional logic — normally in the form of IF/THEN statements. That never scales, and in large applications you end up with very brittle code.

### **Coordinators to the Rescue.**

When I began my experiments to implement Coordinators in Xamarin.Forms, I had several design goals in mind.

First, this is not about MVVM. I have no desire to implement yet another MVVM framework for Xamarin. Further, navigation is not an MVVM concern. I assert that View Models (and for that matter, Pages) should not be aware of other View Models (and pages) within an application.

Second, Coordinators should not know anything about the underlying View Model that supports a page. My desire is for a Coordinator to simply launch pages, and respond to **hooks** exposed by those pages. This is somewhat analogous to the idea of [webhooks](https://en.wikipedia.org/wiki/Webhook) (more on this in a bit).

Third, I wanted the implementation to be straightforward, without a lot of coercing of objects, and without diminishing any of the features that make RAD with Xamarin.Forms so amazing.

### Delegates to the Rescue.

Before getting into building Coordinators, we have to first address a fundamental issue that comes up with every MVVM project. Specifically, how does a View Model, which is handling UI interactions, signal to the workflow that it has completed its intended task?

Using the login example I cited earlier, how does the View Model signal that the user logged in successfully (or unsuccessfully), and pass the generated access token and user information to the workflow that instantiated the page? And more importantly, how does the View Model publish that information? Is there a contract that can be inspected without having to dig through reams of code?

For me, the solution was to use [delegates](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/delegate). In C#, a **delegate** is a reference type variable that holds a reference to a method. Delegates are similar to function pointers in C++. However, delegates are type-safe and secure. Using delegates, I create **hooks**, that the caller can use to participate in and influence the workflow.

For example, in my LoginViewModel, I declare a delegate definition, as:

I added this in the namespace, just above the actual declaration of my LoginViewModel class. This defines the pattern for the delegate, not the actual implementation. It tells a programmer that this View Model will perform a callback when the login is completed, and defines what parameters will be passed. In my LoginViewModel, I expose a property of this type. Users of this View Model can _attach_ to it, to get a callback when the login completes.

In the LoginViewModel, there is no implementation of this delegate. Instead, the View Model’s caller will implement the method — usually as an anonymous method or lambda — creating a sort of callback (or **webhook**) pattern.

Also in the LoginViewModel is an implementation of an **ICommand** which is invoked when the login button is pressed. It is in this command, after the login is successful, that we invoke the delegate. Below is a snippet of the command implementation. I’ve omitted much of the boilerplate code related to exception handling, etc.

Notice the last line, which invokes the delegate. Also notice the [null conditional](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/operators/null-conditional-operators). The delegate is only invoked if it exists. So let’s see how we can use this.

### Threading the Hook.

We’re not quite ready to create our Coordinators yet. But we have solved for a major design goal. We’ve defined a strategy for our View Models to expose important lifecycle events to anyone who cares. Continuing with the LoginViewModel example, we can hook into this as follows:

Simple. The above demonstrates how we can create an anonymous method that will be invoked by our View Model. The method will receive the access token and user object, so that we can _do something important_ with it, such as storing that data and navigating to the next page, for example. This is where our Coordinators come in. They will use these hooks to do something important.

### What About the Code-behind Pages?

Earlier I said that w_e’ve defined a strategy for our View Models to expose important lifecycle events to anyone who cares_. The question is: exactly who cares when the login completes? Well, our _as-of-yet-undefined_ Coordinates will care. But, recall that my second design goal stated:

> Coordinators should not know anything about the underlying View Model that supports a page.

I’ve made a decision that this is to be a hard-and-fast rule. My Coordinators know about the pages that make up a workflow, but do not know or interact with the View Models of those pages. In fact, my code-behind pages create their View Models as _protected_ properties. So, to keep the contracts clean, my code-behind pages simply relay delegate invocations. For example, my LoginPage code-behind looks like this:

Notice that the code-behind page registers itself as the object interested in a callback from the View Model (line 12), and then — because the code-behind does not concern itself in matters of navigation — it simply relays the callback to its own delegate (line 13).

This might seem redundant, but it has practical applications. First, it means that the View Model can expose delegate methods that are private to the code-behind page. Second, it means that there is very loose coupling between the Coordinators and pages.

### A Xamarin Coordinator Implementation

With this, and my third design goal in mind, which is…

> I wanted the implementation to be straightforward, without a lot of coercing of objects, and without diminishing any of the features that make RAD with Xamarin.Forms so amazing.

…I decided that pages can live on their own, or they can have attached Coordinators. It took me a while to arrive at this decision. I actually first started with a Coordinator-first design approach, whereby everything was driven by a Coordinator. I quickly found that this was terribly limiting and super complicated. It required a complex push/pop pseudo-navigation manager, and it limited my ability to easily use TabbedPages, MasterDetailPages, and modals. I also found myself pushing navigation logic into View Models. I didn’t like it.

So instead, I opted for a Page-first approach, whereby Pages can have a Coordinator attached to them. This solves a big issue related to [garbage collection](https://docs.microsoft.com/en-us/dotnet/standard/garbage-collection/fundamentals), since the Xamarin.Forms framework already handles retaining and disposing of Pages based on visibility lifecycles. Had I gone down the Coordinator-first approach, I would have had to add a bunch of ugly logic to manage the stack myself.

With the Page-first approach, you can create a Page as you normally do, and you can pass (attach) a coordinator via the page constructor. So for the login page, it looks something like this:

The nice thing about this approach is that I can also inject a Coordinator in XAML. This is especially useful in MasterDetailPage or TabbedPage situations, wherein you don’t normally create the instances in code. Such as:

Before we get into the mechanics, let’s take a look the implementation of LoginCoordinator. Specifically, we’ll focus on what responsibilities this coordinator takes on, which is all encapsulated within the Coordinator’s Start() method. This is where all of the magic — navigation logic — happens.

Before we go further, let me briefly explain a portion of the [business logic](https://en.wikipedia.org/wiki/Business_logic) of the app. In this app (built for musicians), each user can belong to one or more bands. So after authenticating (logging in), the user is presented with a list of their bands. The user then selects one, and the app then completes the login workflow, and shows the post-login master detail page.

So, this LoginCoordinator actually orchestrates the presentation of two separate pages — the LoginPage and the BandPickerPage. Each of the pages can be used independently or as part of other workflows.

For example, the BandPicker page is used in another part of the app when the user wants to switch between their active bands, without having to login again. The BandPicker page is completely unaware of how it is being used. It just has to focus on doing what it does — pick bands.

### The Framework Stuff

The implementation of the Coordinator itself is pretty easy. In my approach, there is one interface (called ICoordinator) and an abstract base class that partially implements that interface. The interface looks like this:

Each coordinator has to only implement the Start() method. The other two methods — AttachToPage() and DetachFromPage() — are implemented in the abstract base class. Here’s what that looks like:

The application’s coordinators simply need to extend this base class and override the Start() method. That’s pretty much it. There’s only one other piece to the **framework**, which is a simple base class for ContentPage subclasses. It does nothing more than call the AttachToPage() and DetatchFromPage() methods of the Coordinators passed in to the constructor. That’s it.

### Summary

Many thanks to Soroush Khanlou for the inspiration. I’d love to hear about how you’re using Coordinators in your own Xamarin projects, and any ideas you might have to improve upon the implementation I’ve presented here.

You can [download my sample](https://github.com/raf66/CoordinatorExampleApp) app from GitHub.

