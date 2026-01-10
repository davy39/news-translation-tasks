---
title: Comment créer une application React Native et l'intégrer avec Firebase
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-01T10:00:00.000Z'
originalURL: https://freecodecamp.org/news/react-native-firebase-tutorial
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/react-native-firebase.png
tags:
- name: Firebase
  slug: firebase
- name: React Native
  slug: react-native
seo_title: Comment créer une application React Native et l'intégrer avec Firebase
seo_desc: "By Florian Marcu\nIn this tutorial, we are going to build a React Native\
  \ app that is integrated with a Firebase backend. The app will support both the\
  \ React Native CLI as well as Expo CLI. \nThis React Native Firebase tutorial will\
  \ cover the main featu..."
---

Par Florian Marcu

Dans ce tutoriel, nous allons créer une application React Native intégrée à un backend Firebase. L'application prendra en charge à la fois React Native CLI et Expo CLI.

Ce tutoriel **React Native Firebase** couvrira les principales fonctionnalités telles que l'authentification, l'inscription et les opérations CRUD de la base de données (Firestore).

Vous pouvez également [télécharger le code source complet](https://github.com/instamobile/react-native-firebase) depuis GitHub si vous souhaitez passer directement au code.

Ce tutoriel vous guidera à travers les détails des sections suivantes :

1. **Création d'un projet Firebase**
2. **Création et configuration d'une nouvelle application React Native**
3. **Configuration de la structure des dossiers, des routes et de la navigation**
4. **Implémentation de l'UI pour les écrans de connexion, d'inscription et d'accueil**
5. **Inscription avec Firebase Auth**
6. **Connexion avec Firebase Auth**
7. **Identifiants de connexion persistants**
8. **Écriture et lecture de données depuis Firebase Firestore**

Sans plus attendre, commençons à construire le projet React Native Firebase. L'application mobile finale ressemblera à ceci :

![react native firebase](https://www.freecodecamp.org/news/content/images/2020/05/react-native-firebase-1.png)

## 1. Créer un projet Firebase

Rendez-vous sur [Firebase.com](https://firebase.google.com/) et créez un nouveau compte. Une fois connecté, vous pourrez créer un nouveau projet dans la [Console Firebase](https://console.firebase.google.com/u/0/).

* Créez un nouveau compte sur [Firebase.com](https://firebase.google.com/)
* Créez un nouveau projet dans la [Console Firebase](https://console.firebase.google.com/)
* Activez la méthode d'authentification par email et mot de passe dans _Console Firebase_ -> _Authentification_ -> _Méthode de connexion_

![Image](https://www.freecodecamp.org/news/content/images/2020/05/1__J2bqHTUxhs_sTxwRdbvAg.png)

* Créez une nouvelle application iOS, avec l'ID d'application _com.reactnativefirebase_

![Image](https://www.freecodecamp.org/news/content/images/2020/05/1_RFyy5eHgUlZIEQtaCj5ddA.png)

* (Facultatif) Créez une nouvelle application Android avec le nom de package _com.reactnativefirebase_
* Téléchargez le fichier de configuration généré à l'étape suivante sur votre ordinateur (_GoogleService-Info.plist_ pour iOS, et _google-services.json_ pour Android)

Firebase vous permet de créer des applications _sans backend_. C'est un produit qui s'exécute sur Google Cloud et permet aux développeurs de créer des applications web et mobiles sans avoir besoin de leurs propres serveurs.

Cela permet de gagner beaucoup de temps, car vous n'avez pas besoin d'écrire de code backend. C'est également très scalable, étant soutenu par l'infrastructure Google.

Dans Firebase, vous pourrez stocker tout ce dont votre application a besoin : utilisateurs, données, fichiers, jetons de notification push, etc. Toutes ces informations sont mises à disposition des clients mobiles via les SDK Firebase, qui sont compatibles avec React Native. Cela signifie que toutes les interactions avec le backend sont abstraites et encapsulées dans le SDK, de sorte que les développeurs mobiles n'ont pas à se soucier des appels API, de l'analyse des données, de la gestion des sockets, etc.

## **2. Créer et configurer une nouvelle application React Native**

Nous allons rendre notre application React Native Firebase compatible avec Expo CLI et React Native CLI.

Nous allons utiliser Expo pour l'instant, car cela facilite la prévisualisation des applications pour les nouveaux venus. Mais nous n'utiliserons aucune bibliothèque spécifique à Expo, donc le code _src_ peut être simplement utilisé dans n'importe quelle application React Native, quel que soit son échafaudage.

Nous allons utiliser le [Firebase Web SDK](https://firebase.google.com/docs/reference/js), qui est compatible avec Expo et React Native CLI, et est directement soutenu par Google.

Si vous souhaitez utiliser [react-native-firebase](https://rnfirebase.io/) à la place, n'hésitez pas à l'installer et à le configurer (le code restera le même). Mais gardez à l'esprit que nous ne le recommandons pas pour quelques raisons :

* il n'est pas directement soutenu par Google, donc sa maintenance sera beaucoup plus difficile étant donné qu'il s'agit d'une couche supplémentaire qui peut causer des bugs, et
* il ne fonctionne pas non plus avec Expo, ce qui peut être un critère d'exclusion pour de nombreux développeurs.

Les étapes ci-dessous sont également couvertes dans la documentation officielle de React Native sur [comment configurer votre environnement de développement](https://reactnative.dev/docs/environment-setup).

* Installer Expo CLI

Dans votre Terminal, exécutez simplement

```
npm install -g expo-cli
```

* Créez une nouvelle application React Native en exécutant

```
expo init react-native-firebase

```

Pour le modèle, choisissez _Managed Workflow_ — _Blank_

* Démarrez l'application en exécutant

```
yarn ios
// ou
yarn android

```

Cela vous présentera également un code QR que vous pouvez scanner en utilisant l'application Appareil photo sur iOS, ou l'application Expo sur Android.

C'est génial. Nous avons maintenant une nouvelle application React Native, fonctionnant sur iOS et Android. Commençons à la connecter à votre backend Firebase.

* Ajoutez le SDK Firebase au projet React Native

```
yarn add firebase

```

* Ajoutez la bibliothèque de navigation React Native en exécutant

```
yarn add @react-navigation/native && yarn add @react-navigation/stack && expo install react-native-gesture-handler react-native-reanimated react-native-screens react-native-safe-area-context @react-native-community/masked-view
```

* Ajoutez divers composants UI et packages à utiliser dans le projet

```
yarn add react-native-keyboard-aware-scroll-view base-64

```

Créez un fichier de configuration Firebase

```
mkdir src src/firebase && touch src/firebase/config.js
```

Ajoutez votre configuration Firebase dans _src/firebase/config.js_ :

<script src="https://gist.github.com/mrcflorian/f6e52d359d09b27745f27950ba601ac1.js"></script>

Vous pouvez obtenir toutes ces informations depuis [Console Firebase](https://console.firebase.google.com/) -> Paramètres du projet

![Image](https://www.freecodecamp.org/news/content/images/2020/05/1_RU6D6YeIhpIprROu8lmOOw.png)

## 3. Créer la structure des dossiers et configurer les routes et la navigation

* Créez la structure des dossiers en exécutant

```
mkdir src/screens src/screens/LoginScreen src/screens/RegistrationScreen src/screens/HomeScreen
```

* Créez la structure des fichiers en exécutant

```
touch src/screens/index.js src/screens/LoginScreen/LoginScreen.js src/screens/LoginScreen/styles.js src/screens/RegistrationScreen/RegistrationScreen.js src/screens/styles.js src/screens/HomeScreen/HomeScreen.js src/screens/HomeScreen/styles.js
```

* Ajoutez ce code à _src/screens/index.js_

```
export { default as LoginScreen } from './LoginScreen/LoginScreen'

export { default as HomeScreen } from './HomeScreen/HomeScreen'

export { default as RegistrationScreen } from './RegistrationScreen/RegistrationScreen'

```

Ne vous inquiétez pas si le projet est cassé ! Tout aura du sens dans un petit moment.

* Configurez les routes et les navigateurs

Remplacez le fichier _App.js_ par le code suivant :

<script src="https://gist.github.com/mrcflorian/411d266eaf5c081535692eaf0cf6f4b0.js"></script>

## 4. Implémenter l'UI

Maintenant que nous avons l'échafaudage de l'application, passons à l'implémentation des composants UI de tous les écrans. Nous n'allons pas entrer dans les détails de la disposition flex et du style React Native, car cela est hors du cadre de ce tutoriel. Nous allons nous concentrer principalement sur l'intégration de React Native Firebase.

Remplacez simplement les fichiers comme suit :

* src/LoginScreen/LoginScreen.js

<script src="https://gist.github.com/mrcflorian/1d94b6907d3b6521d698512aa55ebeb7.js"></script>

* src/LoginScreen/styles.js

<script src="https://gist.github.com/mrcflorian/499dcf5064d03673ee9f76af2abd1e3f.js"></script>

* src/RegistrationScreen/RegistrationScreen.js

<script src="https://gist.github.com/mrcflorian/1d6924cca7ccda5e9da4f84d3208fc94.js"></script>

* src/RegistrationScreen/styles.js

<script src="https://gist.github.com/mrcflorian/499dcf5064d03673ee9f76af2abd1e3f.js"></script>

* src/HomeScreen/HomeScreen.js

<script src="https://gist.github.com/mrcflorian/bbd57208348528de759f7797936210d1.js"></script>

* src/HomeScreen/styles.js

<script src="https://gist.github.com/mrcflorian/36c027ce741269d387b261c1fa6ea6aa.js"></script>

À ce stade, votre application devrait fonctionner correctement et afficher les écrans suivants (UI uniquement) :

![react native firebase auth](https://www.freecodecamp.org/news/content/images/2020/05/1_rwQyQ3ZCE7rgHukTAeLliw.png)

Vous pouvez basculer entre les deux écrans en appuyant sur les boutons de liens dans le pied de page.

Maintenant que nous avons une belle UI pour la connexion et l'inscription, voyons comment nous pouvons intégrer notre application React Native (et Expo) avec Firebase.

## 5. React Native Firebase — Inscription

Commençons par créer un nouveau compte avec Firebase Auth, puisque naturellement la connexion vient après. Pour cela, nous allons ajouter la logique Firebase pour créer un nouveau compte avec email et mot de passe dans _RegistrationScreen.js_, en implémentant la méthode _onRegisterPress_ comme suit :

<script src="https://gist.github.com/mrcflorian/427ae7cdc5d6ece1461046b91bcb1112.js"></script>

Dans le flux de création de compte ci-dessus, nous faisons quelques choses importantes :

* Nous appelons l'API createUserWithEmailAndPassword de Firebase Auth (ligne 13), qui crée un nouveau compte qui apparaîtra dans la table Authentication de la Console Firebase.
* Si l'inscription du compte a réussi, nous stockons également les données de l'utilisateur dans Firebase Firestore (ligne 24). Cela est nécessaire pour stocker des informations supplémentaires sur l'utilisateur, telles que le nom complet, l'URL de la photo de profil, etc., qui ne peuvent pas être stockées dans la table Authentication.
* Si l'inscription a réussi, nous naviguons vers l'écran d'accueil, en passant également les données de l'objet utilisateur.
* Si une erreur se produit, nous affichons simplement une alerte avec celle-ci. Les erreurs peuvent être des choses telles qu'aucune connexion réseau, mot de passe trop court, email invalide, etc.

Rechargez votre application et testez l'inscription. Si vous avez créé un compte avec succès, vérifiez qu'il apparaît dans _Console Firebase_ -> _Authentification_ :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/1_qy_k5wsgw4MAALmIeBxYpg.png)

## 6. React Native Firebase — Connexion

Maintenant que nous sommes capables de créer de nouveaux comptes, implémentons la fonctionnalité de connexion. Le SDK Firebase prend en charge toutes les étapes d'autorisation et d'authentification nécessaires pour une connexion sécurisée.

Ouvrez _LoginScreen.js_, importez firebase et complétez la méthode _onLoginPress_ :

<script src="https://gist.github.com/mrcflorian/99d7b46ae8323f103213e331c1f1d7ff.js"></script>

Rechargez votre application et connectez-vous avec un compte existant. L'application devrait vous emmener à l'écran d'accueil si les identifiants étaient corrects, ou elle vous alertera avec une erreur si quelque chose a mal tourné.

## 7. Persister les identifiants de connexion

Vous remarquerez que si vous quittez l'application et l'ouvrez à nouveau, elle affichera à nouveau l'écran de connexion. Pour une bonne expérience utilisateur, nous voudrions que tous les utilisateurs connectés arrivent sur l'écran d'accueil. Personne ne veut saisir ses identifiants de connexion chaque fois qu'il veut utiliser une application.

Cela est également connu sous le nom de connexion persistante. Heureusement, le SDK Firebase s'en charge pour nous, en traitant toutes les préoccupations de sécurité. La connexion persistante est activée par défaut dans Firebase, donc tout ce que nous avons à faire est de récupérer l'utilisateur actuellement connecté.

Ouvrez _App.js_ et implémentons la fonctionnalité de connexion persistante :

<script src="https://gist.github.com/mrcflorian/b93251517dd6239848f8a66ec6160a39.js"></script>

_onAuthStateChanged_ retourne l'utilisateur actuellement connecté. Nous récupérons ensuite toutes les données supplémentaires de l'utilisateur que nous avons stockées dans Firestore, et les définissons sur l'état du composant actuel. Cela réaffichera le composant de l'application, qui affichera l'écran d'accueil.

Remarquez comment nous appelons cela la première fois que l'application se charge en utilisant le hook [useEffect](https://reactjs.org/docs/hooks-effect.html).

## 8. Écriture et lecture de données depuis Firebase Firestore

Nous avons déjà utilisé Firestore ci-dessus, pour sauvegarder des informations supplémentaires sur nos utilisateurs (le nom complet). Dans cette section dédiée, nous allons voir comment nous pouvons écrire des données dans Firestore, et comment nous pouvons les interroger.

Nous allons également couvrir comment observer (écouter) les changements dans la collection Firestore et les refléter sur l'écran, en temps réel. Cela peut être très utile dans les applications en temps réel, telles qu'un [React Native Chat](https://www.instamobile.io/app-templates/video-chat-app-in-react-native/).

Pour simplifier, nous allons sauvegarder certains éléments de texte dans une collection Firestore nommée « entities ». Pensez à ceux-ci comme des tâches, des publications, des tweets, tout ce que vous voulez. Nous allons créer un fichier simple qui ajoute une nouvelle entité et nous allons également lister toutes les entités qui appartiennent à l'utilisateur actuellement connecté. De plus, la liste sera mise à jour en temps réel.

* Implémentez _HomeScreen.js_ en le réécrivant avec le code ci-dessous

<script src="https://gist.github.com/mrcflorian/d196fd9a0a77188240ab73b66ec46f3c.js"></script>

* Stylez l'écran d'accueil, en remplaçant _HomeScreen/styles.js_ par :

<script src="https://gist.github.com/mrcflorian/997aad06bec46618697c293fb2446623.js"></script>

* Rechargez l'application et observez le nouvel écran d'accueil. Saisissez du texte et appuyez sur le bouton _Ajouter_
* Rien ne s'est passé.
* Créez un index sur la collection Firestore des entités

Vous remarquerez que la liste des entités n'est pas rendue. Si vous consultez les logs, vous verrez un avertissement concernant « La requête nécessite un index », suivi d'une longue URL :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/1_bfOrtReOOo9B_pDR4_Zm9w.png)

Cela nous informe que nous ne pouvons pas interroger la table des entités par _authorID_ et trier les données par _createdAt_ par ordre décroissant, sauf si nous créons un index. Créer un index est en fait très facile — cliquez simplement sur cette URL puis sur le bouton :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/1_72kARyPWnDypbCko7e4U1Q.png)

* Rechargez l'application à nouveau

Maintenant, tout fonctionne comme prévu :

* L'application liste toutes les entités dans la collection des entités, par ordre de création décroissant
* L'ajout d'une nouvelle entité fonctionne bien
* La liste est mise à jour en temps réel (essayez de supprimer une entrée directement dans la base de données, ou d'en ajouter une nouvelle directement depuis l'application)

Voici à quoi ressemble votre base de données Firestore maintenant :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/1_zPT7lLNr6kvtdazgN50eKg.png)

C'est ainsi que vous lisez et écrivez depuis Firestore dans React Native. Passons à la dernière section.

Jouez avec l'application en ajoutant de nouvelles entités. Voici le projet final :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/react-native-firebase-2.png)

## **Conclusion**

Firebase facilite grandement l'ajout d'authentification et de support de base de données à toute application React Native. Le SDK Firebase est extrêmement puissant, prenant en charge de nombreux modèles courants de lecture et d'écriture de base de données.

En plus de React Native, le SDK Firebase offre un support pour de nombreux autres langages, tels que [Swift](https://www.iosapptemplates.com/blog/swift-programming/firebase-swift-tutorial-login-registration-ios), [Kotlin](https://www.instakotlin.com/templates/android-starter-kit-with-firebase/) ou [Flutter](https://www.instaflutter.com/app-templates/flutter-login-screen/). Consultez ces liens pour des kits de démarrage Firebase similaires dans divers langages.

Nous avons présenté les fonctionnalités les plus basiques dans ce tutoriel React Native Firebase. Dans la prochaine série, nous couvrirons des fonctionnalités plus avancées, telles que Firebase Storage (téléchargement de fichiers) et les notifications push.

Si vous avez aimé ce tutoriel, veuillez me donner une étoile sur le [dépôt Github](https://github.com/instamobile/react-native-firebase) et partagez cela avec votre communauté. Vous pouvez consulter encore plus de [projets React Native gratuits](https://www.instamobile.io/mobile-templates/react-native-templates-free/) sur Instamobile. Santé !