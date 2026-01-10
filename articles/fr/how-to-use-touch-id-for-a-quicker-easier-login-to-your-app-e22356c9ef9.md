---
title: Comment utiliser Touch ID pour une connexion plus rapide et plus facile à votre
  application
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-11T09:37:32.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-touch-id-for-a-quicker-easier-login-to-your-app-e22356c9ef9
coverImage: https://cdn-media-1.freecodecamp.org/images/1*iHa_tmMWld0abbhzTUJcEQ.jpeg
tags:
- name: iOS
  slug: ios
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: Swift
  slug: swift
- name: 'tech '
  slug: tech
seo_title: Comment utiliser Touch ID pour une connexion plus rapide et plus facile
  à votre application
seo_desc: 'By Akul Tomar

  It is a common observation that users drop off a little on your login screen. This
  is how I tackle my facebook addiction? . This tutorial teaches you how to utilize
  Touch ID for a faster and easier login. I’ll take you through the steps...'
---

Par Akul Tomar

Il est courant d'observer que les utilisateurs abandonnent un peu sur votre écran de connexion. C'est ainsi que je lutte contre mon addiction à Facebook ?. Ce tutoriel vous apprend à utiliser **Touch ID** pour une connexion plus rapide et plus facile. Je vais vous guider à travers les étapes bientôt, laissez-moi juste vous donner un bref aperçu.

La plupart des applications utilisent Touch ID comme une authentification de second degré. Ce tutoriel ne traite PAS de la fourniture d'une authentification de second degré (bien que vous puissiez le faire aussi si vous lisez cet article). Il s'agit d'utiliser Touch ID pour effectuer cet appel serveur afin de connecter l'utilisateur.

Maintenant, comment obtenir les identifiants de l'utilisateur à partir de leur empreinte digitale pour effectuer cet appel serveur ??. C'est là que le service **Keychain** intervient. Lorsque l'utilisateur s'inscrit ou se connecte à votre application pour la première fois, enregistrez les identifiants dans le trousseau de votre application. La prochaine fois, lorsque l'utilisateur se déconnecte puis revient sur l'écran de connexion, affichez une popup leur demandant de se connecter en utilisant Touch ID. Lorsque l'utilisateur fournit un Touch ID valide, récupérez ces identifiants d'utilisateur que vous avez enregistrés précédemment dans le trousseau, effectuez votre appel API, et Boom !?.

Il y a donc deux étapes impliquées ici :

* Tout d'abord, vous devez enregistrer les identifiants de l'utilisateur dans le trousseau. Vous pouvez le faire lorsque l'utilisateur s'inscrit ou lorsqu'il se connecte à votre application pour la première fois.
* Ensuite, utilisez Touch ID pour vérifier l'utilisateur, puis récupérez leurs identifiants à partir du service Keychain.

J'utilise **KeychainPasswordItem**, un wrapper pratique pour Keychain disponible sur developer.apple.com [ici](https://developer.apple.com/library/content/samplecode/GenericKeychain/Listings/GenericKeychain_KeychainPasswordItem_swift.html#//apple_ref/doc/uid/DTS40007797-GenericKeychain_KeychainPasswordItem_swift-DontLinkElementID_7). Ils ont un exemple très bon et détaillé sur la façon d'utiliser ce trousseau générique. Allez y jeter un coup d'œil.

Dans le cadre de la première étape, utilisez la méthode d'appel ci-dessous avec l'email de l'utilisateur comme compte et mot de passe lorsque l'utilisateur s'inscrit et se connecte.

Nous stockons l'email de l'utilisateur dans **UserDefaults** pour une utilisation ultérieure. Il serait préférable de faire apparaître une popup pour demander la permission de l'utilisateur d'utiliser cette fonctionnalité. Je saute cette partie pour ce tutoriel ?.

#### Utiliser Touch ID pour accéder au trousseau

Pour utiliser Touch ID, vous devez d'abord ajouter le framework LocalAuthentication à vos binaires de projet. Vous pouvez le faire en allant dans Projet > Phases de construction > Lier le binaire avec les bibliothèques :

![Image](https://cdn-media-1.freecodecamp.org/images/1*1jVJSkOY95UDo9i0FZiXNg.png)

Ensuite, importez le framework LocalAuthentication dans votre contrôleur de vue de connexion.

```
import LocalAuthentication
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*luSj-qKPFtV5PjvAEZZQrQ.png)

Nous avons rempli notre champ de texte userName avec l'email du compte utilisateur que nous avons enregistré précédemment dans **UserDefaults.**

Ensuite, nous devons vérifier si l'authentification est possible sur l'appareil actuel. Consultez le code suivant :

Nous invoquons **authenticateUserUsingTouchId**() dans **viewDidAppear**(). LAContext est une sous-classe de NSObject et représente notre contexte d'authentification actuel. Maintenant, si l'authentification est possible, validez l'authenticité de Touch ID en appelant evaluatePolicy()

![Image](https://cdn-media-1.freecodecamp.org/images/1*vU1Q2tyhAB0yoTVoEa_a7Q.png)

**context.evaluatePolicy()** nous donne la popup Touch ID avec notre dernier nom d'utilisateur accessible, que nous avons donné comme notre localizedReason dans la **méthode evaluatePolicy()**.

Cela complète la partie 1 de l'étape 2 : faire authentifier l'utilisateur en utilisant Touch ID. Ensuite, utilisez Touch ID pour accéder au trousseau où nous sauvegardons ou récupérons les identifiants de l'utilisateur pour la connexion.

Lorsque l'utilisateur fournit un Touch ID valide, nous devons charger le mot de passe à partir du trousseau et effectuer notre appel POST pour connecter l'utilisateur.

```
if authSuccessful {             self.loadPasswordFromKeychainAndAuthenticateUser(lastAccessedUserName)}
```

C'est tout ! Vous pouvez mettre à niveau votre framework d'authentification pour prendre en charge plusieurs comptes. Après avoir vérifié l'authenticité de Touch ID, affichez une popup et demandez à l'utilisateur de sélectionner le compte avec lequel il souhaite se connecter. Ensuite, récupérez les identifiants de l'utilisateur correspondant à ce compte à partir du trousseau. Merci d'avoir lu !