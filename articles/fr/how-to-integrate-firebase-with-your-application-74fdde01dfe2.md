---
title: Comment intégrer Firebase avec votre application
subtitle: ''
author: Tomer
co_authors: []
series: null
date: '2019-01-29T22:22:18.000Z'
originalURL: https://freecodecamp.org/news/how-to-integrate-firebase-with-your-application-74fdde01dfe2
coverImage: https://cdn-media-1.freecodecamp.org/images/0*aClI4EGtanpC5mqJ
tags:
- name: coding
  slug: coding
- name: Firebase
  slug: firebase
- name: Java
  slug: java
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment intégrer Firebase avec votre application
seo_desc: You’ve probably heard about Firebase, but may not know much about how it
  works and how it fits in with your application. Well, you’ve come to the right place.
  We’ll go over what Firebase is and how to integrate it with your Android project
  straight f...
---

Vous avez probablement entendu parler de Firebase, mais vous ne savez peut-être pas comment il fonctionne et comment il s'intègre à votre application. Eh bien, vous êtes au bon endroit. Nous allons passer en revue ce qu'est Firebase et comment l'intégrer à votre projet Android directement depuis Android Studio. **_Attachez vos ceintures_**.

#### Fire-quoi ?

Essentiellement, Firebase fait partie du groupe des [MBaaS](https://en.wikipedia.org/wiki/Mobile_backend_as_a_service), ce qui signifie **_Mobile Backend as a Service_**. Si vous êtes un développeur frontend, vous aurez besoin de divers services qui peuvent nécessiter des capacités backend. Pensez au stockage de fichiers, à la base de données, aux notifications push, à l'analytique, aux publicités et plus encore. Vous pouvez utiliser Firebase pour vous aider à connecter votre application à ces services. Pour en savoir plus, rendez-vous [ici](https://firebase.google.com/).

![Image](https://cdn-media-1.freecodecamp.org/images/1*-ZiPpoNKT33nBDCw2STgFg.jpeg)

### Suivez ces étapes

1. Après avoir ouvert votre projet dans Android Studio, cliquez sur l'onglet **_Outils_** et sélectionnez **_Firebase_**
2. Une nouvelle fenêtre s'ouvre à droite, l'onglet **_Assistant_**, avec tous les services que Firebase propose.

![Image](https://cdn-media-1.freecodecamp.org/images/1*NA34OHFxCyy1zjCYIbeUzg.jpeg)
_Assistant Firebase_

3. Sélectionnez le service que vous souhaitez ajouter à votre application en cliquant dessus. Nous sélectionnerons **_Cloud Messaging_** comme exemple.

4. Cliquez sur le lien qui apparaît, spécifiquement, **_Configurer Firebase Cloud Messaging._**

5. La fenêtre de l'Assistant se transformera en un nouveau menu :

![Image](https://cdn-media-1.freecodecamp.org/images/1*ckAHDd9hqpy8TuM30IQhHQ.jpeg)
_Suivez les étapes ci-dessus_

Suivez les étapes décrites dans l'Assistant, en faisant attention à tout code qui doit être ajouté (et où il doit être ajouté).

La première étape vous demandera toujours de connecter votre application à Firebase. Pour ce faire, vous devez créer un projet pour votre application dans la [**_Console Firebase_**](https://console.firebase.google.com).

Et la deuxième étape vous guidera pour ajouter le service spécifique que vous recherchez. Donc pour notre exemple, FCM signifie **F**irebase **C**loud **M**essaging.

Les choses suivantes que nous devons faire sont :

* Créer une nouvelle classe qui étend FirebaseMessagingService
* Redéfinir deux méthodes : **_onNewToken_** et **_onMessageReceived_**

* Déclarer le service dans votre manifest :

6. La dernière étape que vous rencontrerez s'appelle **_Étapes suivantes_**. Ici, vous serez invité à vous rendre sur la Console Firebase. Cela vous permettra d'interagir avec le service que vous venez d'ajouter.

![Image](https://cdn-media-1.freecodecamp.org/images/1*yb2p7q78i8bGy5TOOQAm1A.jpeg)

Vous possédez maintenant la capacité d'offrir à toute application que vous créez un puissant composant backend qui peut être opérationnel en quelques minutes. Cela réduira considérablement votre temps de développement et vous permettra de vous concentrer sur ce qui est important pour vous.

Des commentaires ? Des questions ? N'hésitez pas à demander.

_Si vous avez aimé cet article, applaudissez pour que d'autres puissent en profiter aussi ! ?_