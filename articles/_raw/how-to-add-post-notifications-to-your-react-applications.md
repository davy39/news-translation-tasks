---
title: How to Add Real-time Post Notifications to Your React Applications
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-07-26T14:22:14.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-post-notifications-to-your-react-applications
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/Depth-First-Search--1-.png
tags:
- name: Firebase
  slug: firebase
- name: React
  slug: react
seo_title: null
seo_desc: 'By Nishant Kumar

  Recently, I was working on an application.  That application was a Thread Clone,
  the newly launched social media platform.

  The tech stack I was using was React for the front end and Firebase for authentication,
  real-time database, an...'
---

By Nishant Kumar

Recently, I was working on an application.  That application was a Thread Clone, the newly launched social media platform.

The tech stack I was using was React for the front end and Firebase for authentication, real-time database, and for file uploads.

As I was building the app, I thought wouldn’t it be cool if I add a Real-time notifications feature in the app, that updates the user when someone likes or comments on your thread? 

And so I started writing the code.

## Prerequisites

You must know React and Firebase in order to proceed with the things explained below. 

However, this can also be implemented in different databases like SQL or NoSQL.

## How to Set Up the Project

Before implementing this notification feature, we need a few things ready. 

Since this is a social media application like Facebook, Twitter, or Linkedin, we need a few parameters ready.

Let’s talk about those parameters now.

Take this payload as an example:

```javascript
const notificationData = {
   userName: auth.currentUser.displayName,
   recipientUserId: recipientUserId,
   senderUserEmail: auth.currentUser.email,
   senderUserId: auth.currentUser.uid,
   type: "like",
   threadID: threadID,
   threadData: threadData,
   timestamp: moment().format(),
   isRead: false,
};
```

We have an object called `notificationData`. 

In that object, we have parameters like `username`, `recipientUserId`, `senderUserEmail`, `senderUserId`, and more. 

Let me explain these:

* `userName`: The Current Username of the person who has logged in.
* `recipientUserId`: The ID of the person who will receive notifications.
* `senderUserEmail`: The Current Username of the person who has logged in.
* `senderUserId`: The Current UserID of the person who has logged in.
* `type: "like"` : The type of Notification. It can be a like or a comment.
* `threadID`: The ID of the Thread, or a Post.
* `threadData`: The contents of the Thread, or a Post.
* `timestamp`: The current timestamp.
* `isRead: false`: The status of the notification, if it has been read or not.

The current `userName`, `senderUserEmail`, and `senderUserId` belong to the current user who has logged in. 

We need these inputs in order the show who interacted with your thread. 

If I have logged in, this data should be mine. We are getting these params from the auth from Firebase Auth.

You need the `recipientUserId` to notify the user that someone has liked or commented on your post. 

If I am liking a thread or adding a comment on one, we need the ID of the user who posted the thread so we can filter through the notifications when we have to display the data.

We also have `isRead`, which is a boolean value to check if our notification has been read or not. 

If we click a notification, we can mark it as read, just by changing the `isRead` to true.

The rest of the parameters are `threadID`, which is the ID of the thread and `threadData` is the contents of the thread.

Now, how to get these inputs is up to you. If you want to build a social media application, simply refer to the videos below.

## How to Add a Notification Collection in Firebase

First of all, we need to create a reference to Firebase. 

Let’s create it:

```javascript
let notificationCollection = collection(database, "notification");
```

Now, we must have a function for handling likes. If that function runs, we send a like to a respective thread. 

Take the below function as an example:

```javascript
export const likeThread = (
  userId,
  recipientUserId,
  threadData,
  threadID,
  liked
) => {
  try {
    let docToLike = doc(likeRef, `${userId}_${threadID}`);
    let docToNotify = doc(
      notificationCollection,
      `${recipientUserId}_${threadID}`
    );

    if (liked) {
      deleteDoc(docToLike);
      deleteDoc(docToNotify);
    } else {
      setDoc(docToLike, { userId, threadID });

      if (userId !== recipientUserId) {
        const notificationData = {
          userName: auth.currentUser.displayName,
          recipientUserId: recipientUserId,
          senderUserEmail: auth.currentUser.email,
          senderUserId: auth.currentUser.uid,
          type: "like",
          threadID: threadID,
          threadData: threadData,
          timestamp: moment().format(),
          isRead: false,
        };
        setDoc(docToNotify, notificationData);
      }
    }
  } catch (err) {
    console.log(err, "error");
  }
};
```

We have a `likeThread` function that takes some of the parameters I previously mentioned. We have the `userId` here as well, which denotes the ID of the current user.

We also have a `liked` property, which is a way to check for likes on a thread. When we like it, it will become true, otherwise it will be false.

```javascript
let docToNotify = doc(
  notificationCollection, `${recipientUserId}_${threadID}`
);
```

We have this `doc` function from Firebase Firestore, that combines the `recipientUserId` with the `threadID` as a unique string and that will be the ID of the notification for a Thread in the Firestore Database.

```javascript
if (liked) {
      deleteDoc(docToLike);
      deleteDoc(docToNotify);
    } else {
      setDoc(docToLike, { userId, threadID });

      if (userId !== recipientUserId) {
        const notificationData = {
          userName: auth.currentUser.displayName,
          recipientUserId: recipientUserId,
          senderUserEmail: auth.currentUser.email,
          senderUserId: auth.currentUser.uid,
          type: "like",
          threadID: threadID,
          threadData: threadData,
          timestamp: moment().format(),
          isRead: false,
        };
        setDoc(docToNotify, notificationData);
      }
    }
```

We have two if statements in the code block. 

The first one is that if the thread is already liked and we unlike it, we will delete the notification document for that thread from the database using `deleteDoc` while passing the collection reference, which is `docToNotify`**.**

The second one checks if the `userId`**,** which is our own ID, is not equal to the `recipientUserId` from the thread. 

It checks if we like or add a comment on our own post. In this scenario, we cannot send a notification to ourselves. 

But keep in mind that the `addDoc` function that sends likes will be outside the second `if statement`. This is because we can like our own threads, but cannot get notifications.

```javascript
setDoc(docToNotify, notificationData);
```

Then we add these data to Firebase Firestore using the `setDoc` function with the parameters `docToNotify`, which notifies users, and the payload which is `notificationData`**.**

As for the comments, we can do the same thing we did for likes. 

The only difference will be the type key is a comment if we are sending a notification for comments.

```javascript
export const postReplies = async (
  recipientUserId,
  threadData,
  userId,
  threadID,
  reply,
  timeStamp,
  currentUserName
) => {
  try {
    addDoc(repliesRef, {
      threadID,
      reply,
      timeStamp,
      name: currentUserName,
    });

    if (userId != recipientUserId) {
      const notificationData = {
        userName: auth.currentUser.displayName,
        recipientUserId: recipientUserId,
        senderUserEmail: auth.currentUser.email,
        senderUserId: auth.currentUser.uid,
        type: "comment",
        threadID: threadID,
        threadData: threadData,
        timestamp: moment().format(),
        isRead: false,
      };

      addDoc(notificationCollection, notificationData);
    }
  } catch (err) {
    console.log(err);
  }
};
```

## How to Get Notifications for a Particular User

To get notifications for a particular user, we need the `userId`, which is the current ID of the user who is logged in.

```javascript
export const getNotifications = async (userId) => {
  const getNotifQuery = query(
    notificationCollection,
    where("recipientUserId", "==", userId),
    orderBy("timestamp", "desc")
  );
  onSnapshot(getNotifQuery, (response) => {
    console.log(
      response.docs.map((doc) => {
        return { ...doc.data(), id: doc.id };
      })
    );
  });
};
```

We need to create a query to check if the `recipientUserId` is equal to the `userId`.

This means the thread is our own, and we should receive a notification for that thread if anyone interacts with it by liking or commenting on it. 

We also have `orderBy` to order the notifications in descending order. This will give us all the notifications for a current user who has logged in.

## How to Display Notifications in the UI

Displaying notifications in the interface is pretty simple:

```javascript
import React from "react";
import useFetchNotifications from "../Hooks/useNotifications";
import { useLocation } from "react-router-dom";
import Notifications from "../Components/Notifications";

export default function NotificationsPage() {
  let { notifications } = useFetchNotifications();
  return (
    <div>
      <ul className="notification-ul">
        {notifications.map((notification) => (
          <div key={notification.id}>
            <Notifications notification={notification} />
          </div>
        ))}
      </ul>
    </div>
  );
}
```

We can get notification data. 

Here, I have a custom React hook called `useFetchNotifications()`**,** from which I am destructuring the notifications array.

Then we map the notifications using the map function.

Our notification page will be like this:

![Image](https://www.freecodecamp.org/news/content/images/2023/07/Screenshot-2023-07-23-at-9.29.07-PM.png)
_Notification Page_

You can also design the way you want to add user profile images for the user who liked or commented on your thread.

When we click a notification, we have to make it invisible or inactive. This will mean that we have read it.

Let’s use a function for this operation:

```javascript
export const readNotifications = async (id) => {
  let docToUpdate = doc(notificationCollection, id);

  updateDoc(docToUpdate, { isRead: true });
};
```

This function will take the id of the notification and update that particular notification’s `isRead` property to true.

When we click the notification, it will disappear.

## How to Show the Number of Notifications

We can also show the number of notifications in the bottom menu bar:

![Image](https://www.freecodecamp.org/news/content/images/2023/07/Screenshot-2023-07-23-at-9.06.55-PM.png)
_The Footer bar_

To implement this notification number functionality, we need to filter through the notifications array and find out if the notification `isRead` property is false.

 If it is false, it means it has not been read yet. If it has not been read yet, it means we can show its count:

```javascript
let isRead = notifications
    .filter((item) => item.isRead === false)
    .map((notif) => notif.isRead);
```

Let’s have a count badge adjacent to the notification icon. 

Here, we should find the length of the `isRead` array to get the total count of  notifications:

```jsx
<div className="active-notifications">{isRead.length}</div>
```

We will only show the count if the length is more than zero. 

In that case, we can have a condition that checks for the length of the `isRead` array length:

```jsx
{isRead.length ? (
  <div className="active-notifications">{isRead.length}</div>
) : (
  <></>
)}
```

## Conclusion

This is how we handle a notification system for a Thread application or any social media application.

[Here is a video version of the article](https://youtu.be/03OvR8I3EXg) if you prefer video format.

You can also learn how to build a [Threads clone](https://youtu.be/_itNFs2cUnY) and a [LinkedIn clone](https://youtube.com/playlist?list=PLWgH1O_994O-vRmOAKtq8VIM6XIC6xwkb) using React and Firebase.

