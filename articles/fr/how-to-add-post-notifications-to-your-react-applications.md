---
title: Comment ajouter des notifications de publication en temps réel à vos applications
  React
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
seo_title: Comment ajouter des notifications de publication en temps réel à vos applications
  React
seo_desc: 'By Nishant Kumar

  Recently, I was working on an application.  That application was a Thread Clone,
  the newly launched social media platform.

  The tech stack I was using was React for the front end and Firebase for authentication,
  real-time database, an...'
---

Par Nishant Kumar

Récemment, je travaillais sur une application. Cette application était un clone de Thread, la nouvelle plateforme de médias sociaux lancée.

La stack technique que j'utilisais était React pour le front-end et Firebase pour l'authentification, la base de données en temps réel et pour les téléchargements de fichiers.

En construisant l'application, je me suis dit que ce serait cool d'ajouter une fonctionnalité de notifications en temps réel dans l'application, qui met à jour l'utilisateur lorsqu'une personne aime ou commente son thread ?

Et donc, j'ai commencé à écrire le code.

## Prérequis

Vous devez connaître React et Firebase pour suivre les choses expliquées ci-dessous.

Cependant, cela peut également être implémenté dans différentes bases de données comme SQL ou NoSQL.

## Comment configurer le projet

Avant d'implémenter cette fonctionnalité de notification, nous avons besoin de quelques éléments prêts.

Puisque c'est une application de médias sociaux comme Facebook, Twitter ou LinkedIn, nous avons besoin de quelques paramètres prêts.

Parlons de ces paramètres maintenant.

Prenons cette charge utile comme exemple :

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

Nous avons un objet appelé `notificationData`.

Dans cet objet, nous avons des paramètres comme `username`, `recipientUserId`, `senderUserEmail`, `senderUserId`, et plus encore.

Permettez-moi de les expliquer :

* `userName` : Le nom d'utilisateur actuel de la personne qui s'est connectée.
* `recipientUserId` : L'ID de la personne qui recevra les notifications.
* `senderUserEmail` : L'e-mail de l'utilisateur actuel de la personne qui s'est connectée.
* `senderUserId` : L'ID utilisateur actuel de la personne qui s'est connectée.
* `type: "like"` : Le type de notification. Il peut s'agir d'un like ou d'un commentaire.
* `threadID` : L'ID du thread, ou d'une publication.
* `threadData` : Le contenu du thread, ou d'une publication.
* `timestamp` : L'horodatage actuel.
* `isRead: false` : Le statut de la notification, si elle a été lue ou non.

Le `userName`, `senderUserEmail` et `senderUserId` actuels appartiennent à l'utilisateur actuel qui s'est connecté.

Nous avons besoin de ces entrées pour montrer qui a interagi avec votre thread.

Si je suis connecté, ces données doivent être les miennes. Nous obtenons ces paramètres à partir de l'authentification Firebase Auth.

Vous avez besoin du `recipientUserId` pour notifier l'utilisateur qu'une personne a aimé ou commenté sa publication.

Si j'aime un thread ou que j'ajoute un commentaire, nous avons besoin de l'ID de l'utilisateur qui a posté le thread afin de filtrer les notifications lorsque nous devons afficher les données.

Nous avons également `isRead`, qui est une valeur booléenne pour vérifier si notre notification a été lue ou non.

Si nous cliquons sur une notification, nous pouvons la marquer comme lue, simplement en changeant `isRead` en true.

Les autres paramètres sont `threadID`, qui est l'ID du thread, et `threadData` est le contenu du thread.

Maintenant, comment obtenir ces entrées vous appartient. Si vous souhaitez créer une application de médias sociaux, référez-vous simplement aux vidéos ci-dessous.

## Comment ajouter une collection de notifications dans Firebase

Tout d'abord, nous devons créer une référence à Firebase.

Créons-la :

```javascript
let notificationCollection = collection(database, "notification");
```

Maintenant, nous devons avoir une fonction pour gérer les likes. Si cette fonction s'exécute, nous envoyons un like à un thread respectif.

Prenons la fonction ci-dessous comme exemple :

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

Nous avons une fonction `likeThread` qui prend certains des paramètres que j'ai mentionnés précédemment. Nous avons également `userId` ici, qui désigne l'ID de l'utilisateur actuel.

Nous avons également une propriété `liked`, qui est un moyen de vérifier les likes sur un thread. Lorsque nous l'aimons, il deviendra vrai, sinon il sera faux.

```javascript
let docToNotify = doc(
  notificationCollection, `${recipientUserId}_${threadID}`
);
```

Nous avons cette fonction `doc` de Firebase Firestore, qui combine `recipientUserId` avec `threadID` en une chaîne unique et cela sera l'ID de la notification pour un thread dans la base de données Firestore.

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

Nous avons deux instructions if dans le bloc de code.

La première est que si le thread est déjà aimé et que nous ne l'aimons plus, nous supprimerons le document de notification pour ce thread de la base de données en utilisant `deleteDoc` tout en passant la référence de la collection, qui est `docToNotify`.

La seconde vérifie si `userId`, qui est notre propre ID, n'est pas égal à `recipientUserId` du thread.

Elle vérifie si nous aimons ou ajoutons un commentaire sur notre propre publication. Dans ce scénario, nous ne pouvons pas nous envoyer une notification à nous-mêmes.

Mais gardez à l'esprit que la fonction `addDoc` qui envoie les likes sera en dehors de la seconde instruction `if`. Cela est dû au fait que nous pouvons aimer nos propres threads, mais ne pouvons pas recevoir de notifications.

```javascript
setDoc(docToNotify, notificationData);
```

Ensuite, nous ajoutons ces données à Firebase Firestore en utilisant la fonction `setDoc` avec les paramètres `docToNotify`, qui notifie les utilisateurs, et la charge utile qui est `notificationData`.

En ce qui concerne les commentaires, nous pouvons faire la même chose que nous avons faite pour les likes.

La seule différence sera que la clé de type est un commentaire si nous envoyons une notification pour les commentaires.

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

## Comment obtenir des notifications pour un utilisateur particulier

Pour obtenir des notifications pour un utilisateur particulier, nous avons besoin de `userId`, qui est l'ID actuel de l'utilisateur qui est connecté.

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

Nous devons créer une requête pour vérifier si `recipientUserId` est égal à `userId`.

Cela signifie que le thread est le nôtre, et nous devrions recevoir une notification pour ce thread si quelqu'un interagit avec lui en l'aimant ou en commentant.

Nous avons également `orderBy` pour trier les notifications par ordre décroissant. Cela nous donnera toutes les notifications pour un utilisateur actuel qui s'est connecté.

## Comment afficher les notifications dans l'interface utilisateur

Afficher les notifications dans l'interface est assez simple :

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

Nous pouvons obtenir les données de notification.

Ici, j'ai un hook React personnalisé appelé `useFetchNotifications()`, à partir duquel je déstructure le tableau des notifications.

Ensuite, nous mappons les notifications en utilisant la fonction map.

Notre page de notification sera comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/07/Screenshot-2023-07-23-at-9.29.07-PM.png)
_Page de notification_

Vous pouvez également concevoir la manière dont vous souhaitez ajouter des images de profil d'utilisateur pour l'utilisateur qui a aimé ou commenté votre thread.

Lorsque nous cliquons sur une notification, nous devons la rendre invisible ou inactive. Cela signifiera que nous l'avons lue.

Utilisons une fonction pour cette opération :

```javascript
export const readNotifications = async (id) => {
  let docToUpdate = doc(notificationCollection, id);

  updateDoc(docToUpdate, { isRead: true });
};
```

Cette fonction prendra l'ID de la notification et mettra à jour la propriété `isRead` de cette notification particulière à true.

Lorsque nous cliquons sur la notification, elle disparaîtra.

## Comment afficher le nombre de notifications

Nous pouvons également afficher le nombre de notifications dans la barre de menu inférieure :

![Image](https://www.freecodecamp.org/news/content/images/2023/07/Screenshot-2023-07-23-at-9.06.55-PM.png)
_La barre de pied de page_

Pour implémenter cette fonctionnalité de nombre de notifications, nous devons filtrer le tableau des notifications et découvrir si la propriété `isRead` de la notification est false.

Si elle est false, cela signifie qu'elle n'a pas encore été lue. Si elle n'a pas encore été lue, cela signifie que nous pouvons afficher son compte :

```javascript
let isRead = notifications
    .filter((item) => item.isRead === false)
    .map((notif) => notif.isRead);
```

Avoir un badge de compte adjacent à l'icône de notification.

Ici, nous devons trouver la longueur du tableau `isRead` pour obtenir le nombre total de notifications :

```jsx
<div className="active-notifications">{isRead.length}</div>
```

Nous n'afficherons le compte que si la longueur est supérieure à zéro.

Dans ce cas, nous pouvons avoir une condition qui vérifie la longueur du tableau `isRead` :

```jsx
{isRead.length ? (
  <div className="active-notifications">{isRead.length}</div>
) : (
  <></>
)}
```

## Conclusion

C'est ainsi que nous gérons un système de notification pour une application Thread ou toute application de médias sociaux.

[Voici une version vidéo de l'article](https://youtu.be/03OvR8I3EXg) si vous préférez le format vidéo.

Vous pouvez également apprendre à créer un [clone de Threads](https://youtu.be/_itNFs2cUnY) et un [clone de LinkedIn](https://youtube.com/playlist?list=PLWgH1O_994O-vRmOAKtq8VIM6XIC6xwkb) en utilisant React et Firebase.