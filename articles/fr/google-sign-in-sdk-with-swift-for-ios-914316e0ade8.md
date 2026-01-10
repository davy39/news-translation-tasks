---
title: Comment configurer le SDK Google Sign In avec Swift pour iOS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-07-08T07:34:35.000Z'
originalURL: https://freecodecamp.org/news/google-sign-in-sdk-with-swift-for-ios-914316e0ade8
coverImage: https://cdn-media-1.freecodecamp.org/images/1*5rAHwA7P4HkBR9S2Gc7e4w.png
tags:
- name: Google
  slug: google
- name: mobile app development
  slug: mobile-app-development
- name: software development
  slug: software-development
- name: Swift
  slug: swift
- name: 'tech '
  slug: tech
seo_title: Comment configurer le SDK Google Sign In avec Swift pour iOS
seo_desc: 'By Onur Tuna

  This post is a clearer explanation of the implementation presented in the Google
  Developer tutorial. The Google tutorial recommends you to use pod, however, I don’t
  like to use pod — I want more freedom. So, this tutorial installs and se...'
---

Par Onur Tuna

Cet article est une explication plus claire de la mise en œuvre présentée dans le [tutoriel Google Developer](https://developers.google.com/identity/sign-in/ios/start). Le tutoriel Google vous recommande d'utiliser pod, cependant, je n'aime pas utiliser pod — je veux plus de liberté. Donc, ce tutoriel installe et configure le SDK manuellement.

Le tutoriel Google a écrit leur projet d'exemple en Objective-C. À la fin de cet article, vous pouvez trouver un projet d'exemple écrit en Swift.

#### **Commençons**

Nous allons maintenant installer le dernier SDK depuis la page [Google Developers](https://developers.google.com/identity/sign-in/ios/sdk/). Dans ce tutoriel, la version du SDK est 4.0.1. Vous pouvez utiliser n'importe quelle version, mais je recommande d'utiliser la dernière.

Lorsque vous téléchargez le SDK, vous allez voir les fichiers et dossiers suivants :

* CHANGELOG.md
* GoogleAppUtilities.framework
* GoogleSignIn.bundle
* GoogleSignIn.framework
* GoogleSignInDependencies.framework
* GoogleSymbolUtilities.framework
* README.md
* Sample: Il s'agit d'un projet d'exemple écrit en Objective-C.

Créez maintenant un projet en utilisant Xcode. Nous allons lier tous les frameworks nécessaires à celui-ci. Placez les frameworks situés dans le dossier SDK où vous le souhaitez. Je préfère regrouper toutes les bibliothèques dans un dossier appelé _Library_ sous mon dossier principal _Projects_.

Ouvrez votre projet et allez dans _Build Settings_. Entrez le chemin où se trouvent vos frameworks.

![Image](https://cdn-media-1.freecodecamp.org/images/1*HH3_B3TbZkv1e11e9GvgkA.png)

Ensuite, copiez le fichier GoogleSignIn.bundle en le glissant-déposant dans le projet. Vous devez également glisser-déposer les frameworks, mais ne les copiez pas.

![Image](https://cdn-media-1.freecodecamp.org/images/1*d_l_eX7V4mZJDTbGtsGL1A.gif)

Nous avons besoin de deux frameworks supplémentaires : _Safari Services_ et _System Configuration_. Apple les fournit. Vous pouvez les lier dans _Build Phases > Link Binary with Libraries_.

![Image](https://cdn-media-1.freecodecamp.org/images/1*iTZekslyv8-UM04rmapsvw.jpeg)

La dernière chose que vous devez faire dans cette partie est d'ajouter un flag de liaison. Ajoutez le flag ci-dessous dans _Build Settings > Other Linker Flags_ :

> _$(OTHER_LDFLAGS) -ObjC_

#### **Fichier de configuration**

Il est temps d'obtenir un fichier de configuration pour votre projet. Vous devez créer une application sur la page Google Developer. Cependant, vous ne copierez pas le fichier de configuration. Au lieu de cela, gardez-le quelque part — certaines informations pourraient être nécessaires plus tard.

Accédez à la [page](https://developers.google.com/mobile/add?platform=ios&cntapi=signin&cnturl=https:%2F%2Fdevelopers.google.com%2Fidentity%2Fsign-in%2Fios%2Fsign-in%3Fconfigured%3Dtrue&cntlbl=Continue%20Adding%20Sign-In) pour créer un projet.

![Image](https://cdn-media-1.freecodecamp.org/images/1*mHBTHeMtK7FDdCuBATF_mQ.png)

Choisissez un nom d'application et donnez votre identifiant de bundle que vous pouvez trouver sous _General_ dans Xcode. Dans la page suivante, vous activerez la connexion pour votre application en cliquant sur le bouton _Enable Sign In_. Après tout cela, téléchargez le fichier _GoogleService-Info.plist_. Gardez-le où vous voulez.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Ajc6yD2HOS91ASPdndmMHg.png)

Retournez à votre projet Xcode. Trouvez votre identifiant client inversé dans le fichier plist que vous venez de télécharger. Collez-le dans _Info > URL Types_.

![Image](https://cdn-media-1.freecodecamp.org/images/1*34A0vm7Cf4k-YccveODqbQ.png)

#### **Ajouter la connexion Google à l'application**

Le SDK Google Sign In est une bibliothèque Objective-C, vous avez donc besoin d'un en-tête de pont pour le lier à votre projet Swift. Vous pouvez créer un en-tête de pont manuellement. Cependant, vous pouvez également laisser Xcode le faire automatiquement.

Créez un nouveau fichier .m avec un nom factice. Il vous demandera de créer un en-tête de pont — dites oui. Supprimez le fichier .m, vous n'en avez pas besoin. Importez Google Sign In dans votre en-tête de pont.

> #import "GoogleSignIn/GoogleSignIn.h"

Maintenant, allez dans votre fichier délégué d'application nommé _AppDelegate.swift_. Votre délégué d'application devrait ressembler à quelque chose comme ceci.

Cela semble être beaucoup de code. Cependant, la plupart est écrit par défaut lorsque vous créez un nouveau projet.

Permettez-moi d'expliquer les changements. Votre classe — AppDelegate — implémente maintenant le protocole _GIDSignInDelegate_. Afin de se conformer au délégué, nous avons implémenté certaines méthodes : _application:openURL:options:_ et _signIn:signIn:didSignInForUser:withError:_. Nous avons également configuré l'objet GIDSignIn dans la méthode _application:didFinishLaunchingWithOptions:_. Le reste n'est pas important.

Un problème significatif est que vous devez coller votre identifiant client dans la méthode _application:didFinishLaunchingWithOptions:_. Vous pouvez trouver votre identifiant client dans le fichier _plist_ que nous avons téléchargé.

#### **Bouton de connexion**

Nous pouvons ajouter un bouton et voir notre application fonctionner. Allez dans votre _ViewController.swift_. Le code final devrait ressembler à quelque chose comme ci-dessous :

Une seule ligne de code a été ajoutée. Cependant, faites attention à ce que notre classe implémente le protocole _GIDSignInUIDelegate_. Nous avons besoin d'un bouton pour faire cliquer l'utilisateur. Allez dans votre Storyboard et placez une vue dessus. Glissez-déposez un _UIView_. Définissez _GIDSignInButton_ comme classe de base et vous avez terminé.

Maintenant, exécutez l'application et connectez-vous. Vous avez terminé avec les bases. Vous pouvez utiliser Google Login dans vos applications à partir de maintenant. En cas de problème, n'hésitez pas à me contacter.

**Exemples de code**

[**onurtuna/Google-Signin-Example**](https://github.com/onurtuna/Google-Signin-Example)
[_Google-Signin-Example - Exemple de connexion Google utilisant Swift 3_github.com](https://github.com/onurtuna/Google-Signin-Example)