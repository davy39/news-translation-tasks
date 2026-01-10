---
title: Infinite Pagination in Flutter with Firebase, Riverpod, and Freeze
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-04-14T23:46:42.000Z'
originalURL: https://freecodecamp.org/news/infinite-pagination-in-flutter-with-riverpod
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/Firebase-Security-Rules-Introduction--1-.png
tags:
- name: app development
  slug: app-development
- name: Flutter
  slug: flutter
seo_title: null
seo_desc: "By Rutvik Tak\nWhen you're developing an app, you'll have to decide how\
  \ you want to load data. And this will typically bring up the issue of infinite\
  \ pagination. \nYou likely won't be showing all of the available items in your DB\
  \ to your users. You may..."
---

By Rutvik Tak

When you're developing an app, you'll have to decide how you want to load data. And this will typically bring up the issue of infinite pagination. 

You likely won't be showing all of the available items in your DB to your users. You may fetch the first 10-20 items and load the next ones as the user scrolls. 

This not only saves you unnecessary reads on your database, but also improves performance as you're loading items on demand.  
  
Getting this right is crucial if you're trying to build high-quality apps. I had the chance to work on a B2B application for one of my clients, and having a nice pagination experience was critical to our application – both in terms of fetch operations and user experience.

In this tutorial, I'll walk you through the approach I took so you can build this feature in your own apps.  
  
This article is focused toward readers who already have a basic understanding of Flutter Slivers, Firebase, Riverpod, and Freezed and who want to use them to build something cool. 

This is less like a tutorial and is rather something I wanted to share which I think is an interesting take on pagination implementation with these packages. 

Once you understand the reasons behind these implementations, then you may be able to replicate this with other state management and DB solutions of your choice. 

Also, I've tried to make things as clear as possible while staying within the scope of the article and have added links for supporting articles/documentation to follow up with.

## What we'll cover here:

1. Overview of tools/packages we are using
2. Feature Breakdown
3. How to fetch and limit items
4. How to fetch data as we scroll
5. How to cache or store fetched items
6. How to manage OnGoingStates
7. Some improvements you can make

## Here are the tools and packages we'll be using:

* **[Cloud Firestore](https://firebase.google.com/docs/firestore):** NoSQL database solution from Firebase.
* **[Riverpod](https://riverpod.dev/):** a state management library from the author of Provider.
* **[Freezed](https://pub.dev/packages/freezed):** a code generator for unions/pattern-matching/copy. Commonly used for generating class models with from and to json methods. 

And here's the source code if you'd like to have a look: [Infinite pagination in Flutter with Riverpod, Freezed, Firebase](https://github.com/rutvik110/infinite_pagination).

## Feature Breakdown

To make things easier to understand and work with, I always try to break them down into their different states. This way, you'll get the abstract idea of what's going on and we can handle each task one by one so we don't get overwhelmed.  
  
Our Pagination feature has the following different states:

### Initial fetch states

Here are what the Loading, Data, and Error states should look like:

![Image](https://www.freecodecamp.org/news/content/images/2024/08/loadingState-1.gif)
_Initial loading_

![Image](https://www.freecodecamp.org/news/content/images/2024/08/dataState-1.gif)
_Data loaded_

![Image](https://www.freecodecamp.org/news/content/images/2024/08/errorState-1.gif)
_Error state_

###   
After first fetch states (OnGoingStates)

Here are what the OnGoingLoading, OnGoingData, and OnGoingError states should look like:

![Image](https://www.freecodecamp.org/news/content/images/2024/08/onGoingLoadingState-3.gif)
_OnGoingLoading state_

![Image](https://www.freecodecamp.org/news/content/images/2024/08/onGoingDataState-2.gif)
_OnGoingData state_

![Image](https://www.freecodecamp.org/news/content/images/2024/08/onGoingErrorState-2.gif)
_OnGoingError state_

Alright now that we've seen what our different states will look like, let's dive in.

## How to Fetch and Limit Data 

I got a sample application running – it does nothing special except fetching the data as it is from Firebase. 

We are using [Slivers for scrolling](https://docs.flutter.dev/development/ui/advanced/slivers) behaviour and we are using [Consumer from Riverpod](https://riverpod.dev/docs/concepts/reading/#consumer-and-hookconsumer-widgets) to load the data through a future provider that's fetching items from Firebase. I've already added some data in Firebase (*Firestore), so we'll just be using that.

Loading the items through Consumer:

![Image](https://www.freecodecamp.org/news/content/images/2022/04/initial_paginatedview-1.png)
_Loading initial items through a consumer using Slivers_

  
Declaring Providers:

![Image](https://www.freecodecamp.org/news/content/images/2022/04/init_providers.png)
_Declaring database class provider and the futureProvider that returns the items from the database._

  
MyDatabase class:

![Image](https://www.freecodecamp.org/news/content/images/2022/04/MyDatabase_initiali.png)
_Database class with a method called fetchItems() which fetches the items from a Firestore collection called "items" and returns them._

Here's a preview of what this will look like:

![Image](https://www.freecodecamp.org/news/content/images/2022/03/fetching_all_items-1.gif)
_Loading items from Firebase into the app. Showing initial loading, ondata states._

As you can see, we are fetching everything that's available, which is not very good! We want to limit the number of items we fetch. 

We can do that by using **`.limit(n)`** on our Firebase query. We'll set that limit to 20 items and order our items by **createdAt** field in descending order. 

![Image](https://www.freecodecamp.org/news/content/images/2022/02/limiting_items.png)
_Limiting the number of items fetched with the help of .limit(n) and ordering items based on "createdAt" value._

Now, we only fetch the most recent 20 items from our database. 🙌   
  
Ordering items with respect to some field that is unique and which can be used to sort is important here. This is one of the ways to paginate items. This is also called cursor-based pagination.

### How to Add the Mechanism for Scrolling Callback 

To get the information on the scrolling, we'll create a ScrollController and pass it to our CustomScrollView.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/adding_scroll_controller-1.png)
_Added ScrollListener and listening to scroll events to make a call when scroll position is near the end of the items list._

* **maxScroll**: Maximum amount of distance the user can scroll in the scrolling axis.
* **currentScroll**: Current position of the user in the scrolling view.
* **delta**: Amount of space from the bottom.

We'll listen to scrolling events, and when the difference between **maxScroll** and **currentScroll** gets less than the **delta**, we make the call to fetch the next batch of items.

## How to Store and Fetch the Next Batch

This will be interesting. Let's see what we have to manage here:

1. How to store already-fetched items.
2. How to build up logic to fetch the next batch of items based on what we fetched previously.

To manage these two functionalities, we'll use [StateNotifiersProvider](https://riverpod.dev/docs/providers/state_notifier_provider/) in Riverpod. Using them will help us separate our core implementation logic from the UI layer and give us more flexibility in handling different states of fetching and building up logic for the fetch calls.

This is also Riverpod's recommended solution for managing state which may change in reaction to user interaction.

Here's the updated itemsProvider:

![Image](https://www.freecodecamp.org/news/content/images/2022/04/itemsProvider.png)
_Updated itemsProvider to StateNotifierProvider which creates a PaginationNotifier with initial items count and fetchNextItems call back._

Here's PaginationStateNotifier:

![Image](https://www.freecodecamp.org/news/content/images/2022/04/paginated_state_notifier-1.png)
_PaginationNotifier that will hold fetched items and handle all the logic related to different pagination states and fetch callbacks._

In this code, we created our **PaginationNotifier** by extending it to the StateNotifier class. We made it generic representing the type with **T** to make it reusable. 

So, let me go through things in here:

* **_items**: All the fetched items are added to this list.
* **itemsPerBatch**: Max number of items in a batch. Same as the number we set in the limit on the firebase query in the backend.
* **fetchItems (T? item)**: This function will be the one actually making the call to fetch the items, and it accepts a nullable item. This **item** is the last item from the **_items** list. If it's the first time we are fetching items or **_items** is empty, then it'll be **null**. 
* **fetchFirstBatch()**: Will fetch the first batch of items and update the state.
* **fetchNextBatch()**: Will fetch the next batch of items and update the state. The implementation is almost the same as the **fetchFirstBatch** right now except for two important things:  
– At first, we are updating the state to **.data(_items)**. This is because we still want to show the previously fetched items while the next batch is loading.  
– Second, we pass the last item in the **_items** list when making the call to fetch items. This section will improve in the next section where we'll add OnGoingStates to handle this better.
* **init()**: Called when the notifier is initialized. We just make the call to fetch the first batch here if the items are empty.

Now, let's see what we have to update in the backend logic:

![Image](https://www.freecodecamp.org/news/content/images/2022/04/MyDatabase_final-1.png)
_Database class fetchItems method updated for fetching next 20 items based on the last item fetched._

So we are accepting an item here now. If the item is null, we fetch the first 20 items. If it's not, then we are using a **.startAfter()** filter on our query, which basically says, "Hey! I want the items that start after the item that matches this value that I'm sending along. Cool!"

A bit more professional answer here: 😅

> [startAfter()](https://firebase.google.com/docs/firestore/query-data/query-cursors): Takes a list of [values], creates and returns a new [Query] that starts after the provided fields relative to the order of the query. (From the Firebase docs)

On the UI side, we won't have to change anything. Let's run this and see what we get!

![Image](https://www.freecodecamp.org/news/content/images/2022/02/ezgif.com-gif-maker.gif)
_Loading next items on demand as user scrolls towards end of the items list._



Nice! We are loading up the next batches as we scroll toward the end of the list. Isn't that cool? 😁

Now we want to work on the display. We want to show an ongoing loading or error indicator at the bottom of our list which will represent OnGoingStates.

## How to Manage OnGoing States

So how do we manage these OnGoingStates and represent them to the user?  
  
Well, this doesn't have a single answer. One approach is to create some variable within StateNotifier that represents these states in enum form and updates them to indicate the OnGoingStates. This is what I did in my first iteration, and it turned out not to be a very good approach. 

So instead, let's jump to the thing that worked for me.  
  
As we have more than three states to handle here, why don't we create our own version of AsyncValue that will include two more additional states called OnGoingLoading and OnGoingError state? AsyncValue is just a union that maps to different states. We could create something similar.

We can do this by using [Freezed](https://pub.dev/packages/freezed), which is a code generation library for creating unions and a lot more. 

![Image](https://www.freecodecamp.org/news/content/images/2022/02/pagination_state.png)
_Creating our custom PaginationState union with Freezed._

  
The first three states here are self-explanatory – they're the regular ones that you interact with when using AsyncValue.  
  
As our OnGoingLoading and OnGoingError states occur after our first call, we also want to display the previously fetched items in this state so we have the items parameter. And an additional error and stack trace parameter for the OnGoingError state.

I believe this way we are more declarative on what we are doing on both the UI and business logic sides. Also, the representation to the user gets pretty easy and clean with this.  
  
Now, let's update our StateNotifier to use this new PaginationState object instead of AsyncValue.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/adding_ongoing_states-2.png)
_Updated PaginationNotifier to use PaginationState instead of AsyncValue._

In the **fetchNextBatch** function, we'll update our state to **.onGoingLoading** and **.onGoingError** states replacing the **.data()** and **.error()** states.

On the UI side, you'll see some compilation errors. We'll also need to handle these two new states in our Consumer.

Updated PaginatedListView :

![Image](https://www.freecodecamp.org/news/content/images/2022/04/paginatedlistview-5.png)
_Updated UI code for PaginatedListView_

ItemsList: So, I extracted my logic for loading items in its separate widget.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/itemslist.png)
_Updated UI code for ItemsList now handling both initial and OnGoing states._

ItemsListBuilder: And the logic for building out items list or SliverList is extracted into its own widget as well which makes it reusable across different pagination states.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/itemslistbbuilder.png)
_Builder that builds sliver list of items._

  
The final step that remains is adding that loading/error indicator at the bottom of the **ItemsList.** 

For this, we'll just add another consumer that will handle only the **OnGoingLoading** and **OnGoingError** states.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/adding_ongoing_bottom_widget.png)
_Adding OnGoingBottomWidget below our items list which shows appropriate message based on OnGoing state._

There we go! That looks much better.

Let's see it in action in an iOS simulator showing the handing of different ongoing pagination states: 🚀

![Image](https://www.freecodecamp.org/news/content/images/2024/08/onGoingLoadingState-4.gif)

![Image](https://www.freecodecamp.org/news/content/images/2024/08/onGoingDataState-3.gif)

![Image](https://www.freecodecamp.org/news/content/images/2024/08/onGoingErrorState-3.gif)

## Some Improvements You Can Make

Now that we have a working application with pagination, the next steps are to improve upon what we have done so far. 

That includes things related to limiting our calls to fetch when there's already a fetch call going on, debouncing calls within a certain duration, and letting the user know if they've reached the end of the list and there are no more items to display.

Also, who doesn't want a scroll to the top button 😅.

### How to reject concurrent requests

First, we'll reject any concurrent requests that happen in a certain duration after a request is made. We can do this by creating a timer and checking if that timer is active on each request. If it is, we reject the request or else proceed and again instantiate the timer. 

Second, we can also check for our state – if we are already processing the previous request then we reject the incoming request. For this, we can just check if our state is equal to the loading state and handle that.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/adding_timer_with_state_check.png)
_Added timer and state check to debounce any immediate calls after a call is made or when state is loading._

### Has reached end of list (no more items to fetch)

We can maintain a boolean that indicates this. Every time we get our results, we can check if the results are less than our **itemsPerBatch** count. 

On the UI side, we can present a proper message based on that. Here's the updated pagination notifier:

![Image](https://www.freecodecamp.org/news/content/images/2022/03/nomoreitems_addition.png)
_Declaring a noMoreItems bool to know when there are no more items to fetch._

And the updated UI code: 

![Image](https://www.freecodecamp.org/news/content/images/2022/03/noMoreItems.png)
_Showing a proper message based on status of noMoreItems bool._

![No More Items Found condition!](https://www.freecodecamp.org/news/content/images/2022/03/nomoreitems.gif)
_No More Items Found demo._

### How to add a scroll to top button

These buttons are useful and save the user from a whole bunch of scrolling. Here's how we can implement one in our app: 

![Image](https://www.freecodecamp.org/news/content/images/2022/03/scroll_to_top_button_addition.dart.png)
_Adding a ScrollToTopButton_

We are using AnimatedBuilder to listen for scrolling updates. AnimatedBuilder accepts a listenable object and as our ScrollController is actually a ChangeNotifier that implements Listenable, we can pass it here.

If the **scroll offset** is greater than a certain value, then we show the **ScrollToTop** button. When tapped, we animate the scrolling to the top.  


![Image](https://www.freecodecamp.org/news/content/images/2022/03/scroll_to_top.gif)
_Demo showing usage of ScrollToTopButton added above._

## Summary

That wraps it up! Here are some of the things you learned about in this article:

* How to handle the different states of pagination effectively with Riverpod and Freezed.
* How to use the cursor-based pagination technique with Firebase. The same can be applied to whatever DB you're using with only changes in the backend fetch function. Other implementations remains the same. 

**Again, here's the source code:** [Infinite pagination in Flutter with Riverpod, Freezed, Firebase](https://github.com/rutvik110/infinite_pagination)

Hope you enjoyed the article. ☺️ This was my first article here on freeCodeCamp and I really enjoyed writing this. It took a 😅 lot more time to write than I had imagined but finally, it's here for you to read!🙌 

I hope to write more such articles here 🙇‍♂️ along with some Flutter design 🧑‍🎨 challenges as I myself explore app development as a growing developer and bring interesting stuff to you! 😁

I'm also active on Twitter [@TakRutvik](https://twitter.com/TakRutvik) 💙 sharing my creations and things that I've been working on. Feel free to reach out ☺️.

