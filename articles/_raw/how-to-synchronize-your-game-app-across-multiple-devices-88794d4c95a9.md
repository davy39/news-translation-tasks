---
title: How to synchronize your game app across multiple devices
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-08T17:16:57.000Z'
originalURL: https://freecodecamp.org/news/how-to-synchronize-your-game-app-across-multiple-devices-88794d4c95a9
coverImage: https://cdn-media-1.freecodecamp.org/images/0*vLBlhBeBsItUgjMR
tags:
- name: android app development
  slug: android-app-development
- name: communication
  slug: communication
- name: Firebase
  slug: firebase
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Shukant Pal

  If you’re having problems with online game synchronization, you’re in the right
  place!


  _Photo by [Unsplash](https://unsplash.com/@rawpixel?utm_source=medium&utm_medium=referral"
  rel="noopener" target="_blank" title="">rawpixel on <a h...'
---

By Shukant Pal

If you’re having problems with online game synchronization, you’re in the right place!

![Image](https://cdn-media-1.freecodecamp.org/images/0*vLBlhBeBsItUgjMR)
_Photo by [Unsplash](https://unsplash.com/@rawpixel?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">rawpixel</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

At their lowest level, typical games can be broken down into simple steps taken by each player — they are called turns, and in each turn a move occurs. It isn’t necessary that players get one turn at a time, or make only one move at a time. To synchronize your game app across multiple online devices, you need to be able to break your game into these little steps.

### Our Model

In this article, we take a simple generic two-player board game. Before doing anything, we need two players, right?

To set this up, you need to implement a feature called matchmaking, where you have a common node in your FirebaseDatabase where every player can post their challenge. The challenge posted contains the UID of the challenger and another reference to a moves-node where the moves will be published. If you haven’t done this or are having problems implementing it, read this article on [matchmaking](https://medium.com/@sukantk3.4/match-making-with-firebase-hashnode-de9161e2b6a7).

Once both players get hold of the moves node, one player must post their first move, then the second, then the first and so on. We will use Firebase’s `ChildEventListener` to receive moves posted by the opponent.

### Dive deeper into the code

Basically, we have two things to do: send a move and receive a move. Our `FirebaseGameSynchronizer` component will do just that, but **interpretation of the move will be done by the `Modulator` you implement.**

The **mover** sends their move using `sendMoveMsg` . You can encode your move in a variety of ways. For example, if a piece is moved from (a,b) to (c,d), then encode the move as the number `abcd`. I would definitely recommend this method if the size of your sample (or if it’s a board game, the board size) is less than 10.

`sendMoveMsg` basically uploads the move to the moves-node `mMovesRecordList` and expects the other player to be listening to it.

Once the move is published, both players receive the move. Wait a minute… You don’t want the mover to receive the move — because you may have already done the move on their end, and don’t want to do it twice.

So, I also added a cool feature (if you want both players to receive the move instead, just remove all references to `mSelfMoveSoph` ): the self-moves semaphore. Every time `sendMoveMsg` is called, it increments to `mSelfMoveSoph`. We know how many moves we’ve uploaded right now with this semaphore.

`onChildAdded` is called whenever a move is added by Firebase. It ignores the move if the semaphore has a value; otherwise, the `mMessageModulator` is called to interpret the move and show it to your user. `Modulator` is a functional interface that is the complement to your move-to-string encoder. It takes that string uploaded to Firebase and converts it into the move.

### **Wait, that won’t work if the user gets a call**

Yes, if the user gets a call and your application is killed… how will the user get back to playing?

Again, let’s make a `Modulator` like this:

```
public class GenericGameFragment implements FirebaseGameSynchronizer.Modulator {
```

```
    public void onMoveReceived(boolean isSyncingPast, String encodedMsg) {       // ... do move, show it on UI .....
```

```
    }
```

```
}
```

Now two bad things will happen:

1. If the user leaves, `FirebaseGameSynchronizer` will be left attached to the node listening to it. That’s a memory + CPU-usage leak.
2. `FirebaseGameSynchronizer` will have a reference to your fragment — just see it, Modulator must update the UI and has a reference to `GenericGameFragment` .

### Syncing and Unsyncing to the moves-node

I used a relatively simple solution to the problem. It’s a combination of two things:

1. **Sync flag:** When you set the sync property, `FirebaseGameSynchronizer` will call the modulator, otherwise, it will store the move in a buffer. On setting the sync flag again, it first releases the moves in its buffer.
2. **Attachment:** The modulator is removed whenever the fragment’s `onStop` method and set again on the fragment’s `onStart`.

Before using this “new” synchronizer, remember to call `startSync()`. On `onStop`, call `stopSync` and in `onResume` call `startSync` again. Now, you should call `detachModulator` and `flush` in `onDestroy`.

Check this link for the full implementation: [FirebaseGameSynchronization Gist](https://gist.github.com/SukantPal/bf90b4aa7b6859cf54b0133a0abd2594).

Further Reading:

* [Firebase Match Maker — How to use Firebase for building multiplayer Android games?](https://medium.freecodecamp.org/match-making-with-firebase-hashnode-de9161e2b6a7)
* [Custom layout for board games — BoardLayout!!!](https://medium.com/@sukantk3.4/custom-layout-for-board-games-in-android-ab6d1a321ff6)

