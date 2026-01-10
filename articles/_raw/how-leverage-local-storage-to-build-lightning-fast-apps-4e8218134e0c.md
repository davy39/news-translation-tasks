---
title: How to leverage Local Storage to build lightning-fast apps
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-04-25T18:44:13.000Z'
originalURL: https://freecodecamp.org/news/how-leverage-local-storage-to-build-lightning-fast-apps-4e8218134e0c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*f0xRT52dcYqbK3JN_6fMgA.jpeg
tags:
- name: Android
  slug: android
- name: mobile app development
  slug: mobile-app-development
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Nikita Kozlov

  Users love fast, responsive apps. They don’t want to hear about how API calls take
  time. They just want to see updates immediately. Right now. And we as a developers
  should strive to provide that. So how can we?

  The solution: storing...'
---

By Nikita Kozlov

Users love fast, responsive apps. They don’t want to hear about how API calls take time. They just want to see updates immediately. Right _now._ And we as a developers should strive to provide that. So how can we?

The solution: storing those changes locally, then synchronizing them with your servers from time to time. But this gets way more complex when things like connection latency is taken into account.

Let’s take Medium for example. Medium users can recommend an article to their followers by tapping a little green heart (there’s one on this page, too ?). By tapping the heart a second time, the user can stop recommending it.

### The functionality is simple, but the edge cases cause lots of problems

I don’t know exactly what happens inside Medium’s app, but for simplicity, lets imagine that the first tap adds an item to the recommendation list, and the second one removes it.

Let’s see what kinds of problems this could cause for us if we decided to add similar functionality to our app:

1. We should take into account that user can start tapping like crazy. This behavior could lead to a stream of events.
2. Internet isn’t always fast. On a bad network connection, even simplest API calls could take several seconds to finish. During this time, the user could leave the current screen, then return.
3. From time to time, API calls can fail, and our system needs to be able to recover from such situations.
4. Users can have multiple devices with the same app, or they can use both the mobile app version and the corresponding website in tandem. In either case, we should have a policy for synchronizing data with our back end to update its state.

This isn’t a full list of the challenges we face, but these are the ones this article will focus on addressing.

### Defining the problem

![Image](https://cdn-media-1.freecodecamp.org/images/Hjb48bUy1QlA3xfQFwB96yKGdr8O7PlH-Iy8)

Before we start discussing implementation, lets define our acceptance criteria. The task is to develop a feature that allows the user to add and remove items from a certain list. The list is stored on our back end.

Implementation must fulfill the following requirements:

1. **The user interface reacts immediately to the user’s actions.** The user wants to see the results of their actions immediately. If later we can’t synchronize those changes, we should notify our user, and roll back to the previous state.
2. **Interaction from multiple devices is supported.** This doesn’t mean that we need to support changes in real time, but we do need to fetch the whole collection from time to time. Plus, our back end provides us with API endpoints for additions and removals, which we must use to support better synchronization.
3. **Integrity of the data is guaranteed.** Whenever a synchronization call fails, our app should recover gracefully from errors.

Luckily, we don’t need to implement the whole feature, but rather develop a storage mechanism that will allow us to implement it. Let’s investigate different ways to meet these requirements.

### The straight-forward approach

![Image](https://cdn-media-1.freecodecamp.org/images/oLDGe3QJgeliWCKWuLDgQQCdjPlubHuDZK91)

The first solution that comes to mind is to store a local copy of the list, then update it when the user makes a change.

Most of the problems with this approach are related to race conditions or API call failures, for example:

1. **Collisions between fetching and changing the list.** Lets imagine that we started fetching items from our back end to update our local storage, and the user made a change before that operation finished. This would lead to a merge conflict between fetched list and the local one. So we need to distinguish, for example, between an item that wasn’t added yet and an item that was already removed from the web or another device.
2. **API call failure.** Users can make lots of changes quickly, and they can also revert them quickly. For example, users can add an item to a list, then remove them, then add them back. If the first addition fails, then we should recover from it. In this case, we need to remove the item from the list. But that would ruin the integrity of our data, because the item should actually be on the list, since the last call we made was an addition and it wasn’t finished yet.

Even though there could be a way to make this approach work, I would argue that local storage should keep more information than just the final expected result. This will allow us to recover from all problems we may encounter.

### Let’s keep history of everything the user does

![Image](https://cdn-media-1.freecodecamp.org/images/lMQoXy6k3uoNG9h23dxkNilJYjvn390W2iEt)

Here’s a different approach: let’s keep the list we fetched from the API, as well as record everything the user has done. Every record would match an API call (“add” and “remove” respectively).

Once our API call finishes, we can update our local copy and remove the record from our history. When we want to synchronize the user’s browser with our back end, we just fetch the version of that list and replace our copy.

We no longer have any problems with API call failure, because we know the exact state before the call, and can just drop that record from the history without losing data integrity.

The main problem with this is performance. Every time we want to check whether a particular item is in the list, we need to go through all the records to calculate what our user should expect to see.

Of course, performance depends on the amount of interactions our user can do within a certain timeframe, and the way the data is stored. Plus keep in mind that **premature optimization is the root of all evil**, so if you don’t have this problem, then probably this is a way to go.

I think that this approach is great when user creates the content in the app, because it exposes lots of ways for handling synchronization issues. But our problem is simpler than that, so we should be able to make some optimizations and further increase performance.

### The middle ground

![Image](https://cdn-media-1.freecodecamp.org/images/uk9K56dmC1IhVJgyo0opNtr6nenHfsAThhrO)

It’s possible to have just _enough_ information to recover from negative cases. Having two extra lists — one for ongoing additions, and one for ongoing removals — should be enough. To ensure data integrity, you would just need to apply a few rules:

1. **Lists with additions and removals have priority over the main list.** For example, let’s say an item is in both the removals list and in the main list. When the browser checks to see whether the item is in the list, it should return false.
2. **One item can’t be in both lists at once.** If the user made multiple actions on a single item, the latest change should have priority. For example, if the user added and then removed the item, as a result it should be in the list for removals. It doesn’t matter whether the item is in the main list or not.
3. **Only after the last API call for a certain item has finished can it be removed from the corresponding list.** For example, the user could have added the item, removed it, then added it again before the first call is finished. In this case, the item would be in the list for additions. But it should be removed from there only after the second addition is finished. This can be achieved by assigning an ID to each entry in those lists. Later, after API call is finished, the entry would be removed using this ID.
4. **After every API call, the main list should be updated.** The main list should reflect the actual state of the backend to the best of our knowledge. So in the case of consecutive addition and removal, even though from app side it would looks like item was not in the list, after the first call we should add it to the main list.

### A few words about API call failures

There are different reasons why an API call can fail. Some of them temporary, some of them not. Some of them are fatal, and some of them are possible to recover from. Regardless of the solution, even failed requests should return some information about the cause of the problem.

I think that HTTP status codes are perfect for this. For example, if the status code is _504 Gateway Timeout,_ then retrying could be a good idea, but if it is _400 Bad Request,_ then most likely some client logic is wrong and simple retry logic won’t help. Some of them, like _401 Unauthorized,_ could require some user actions. _410 Gone_ or _404 Not Found_ during the removal call could mean that the user removed this item from a different device and most likely we can even tell user that the operation was successful, since user’s intention is fulfilled.

If for some reason your API doesn’t use proper HTTP status codes (I don’t even want to know why), it still should provide information regarding the cause of an issue. Otherwise, you could run into a weird issues. For example, if the call for removal failed because item **is not** in the list anymore, but we won’t have information about the cause, then the application would think that item **is** in the list until the next round of fetching the whole list.

### Conclusion

The first solution was a simple list. It was fast, but handling negative cases was difficult.

In the second approach, we created a data structure that acts like a list, but persisted the records of all the changes made. This could handle negative cases, but it was much slower.

Our middle ground was a solution that — from outside — still acts like a list. But it allows us to balance performance and easily recovery from errors.

The issues mentioned in this article are only one side of the problem. The other is the amount of API calls made. If the user performs a lot of similar interactions, we can try to minimize the amount of API calls made. This optimization affects the structure of our local storage as well.

I will discuss this and propose additional solution to these issues in my next articles.

Thank you for you time reading this article. If you like it, don’t forget to click the ? below. You can also f[ollow me on Twitter.](https://twitter.com/Nikita_E_Kozlov)

