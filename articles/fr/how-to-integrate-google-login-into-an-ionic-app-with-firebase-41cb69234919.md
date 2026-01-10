---
title: Comment intégrer la connexion Google dans une application Ionic avec Firebase
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-28T19:27:23.000Z'
originalURL: https://freecodecamp.org/news/how-to-integrate-google-login-into-an-ionic-app-with-firebase-41cb69234919
coverImage: https://cdn-media-1.freecodecamp.org/images/1*aE75t1iZ3Sbr9l-I6QHf6A.png
tags:
- name: authentication
  slug: authentication
- name: Firebase
  slug: firebase
- name: Google
  slug: google
- name: Security
  slug: security
- name: technology
  slug: technology
seo_title: Comment intégrer la connexion Google dans une application Ionic avec Firebase
seo_desc: 'By Ryan Gordon

  A lot of apps these days need to maintain some form of user authentication. This
  helps users manage their accounts and store their info securely. But account creation
  can be a bad experience for some users. Some do not want to have ano...'
---

Par Ryan Gordon

De nombreuses applications de nos jours nécessitent une forme d'authentification utilisateur. Cela aide les utilisateurs à gérer leurs comptes et à stocker leurs informations en toute sécurité. Mais la création de compte peut être une mauvaise expérience pour certains utilisateurs. Certains ne veulent pas avoir un autre compte sur un site web où ils doivent se souvenir d'un autre mot de passe, parce que leur oncle Mick a recommandé de ne jamais utiliser le même mot de passe.

Dans l'intérêt d'améliorer l'UX pour ces utilisateurs, il est utile de mettre en place un moyen de se connecter avec des comptes qu'ils possèdent déjà, tels que Google, Facebook ou Github.

OAuth est la manière dont nous pouvons y parvenir. Chacun de ces fournisseurs et bien d'autres proposent une authentification OAuth que nous pouvons utiliser pour connecter ces utilisateurs avec leurs informations existantes. De plus, si un utilisateur aime se connecter avec plusieurs fournisseurs, nous pouvons lier un compte utilisateur à un ou plusieurs fournisseurs. Cela signifie qu'un utilisateur peut se connecter avec Google ou Facebook et toujours accéder au même compte dans notre système.

**Vous voulez juste le code au lieu de suivre le post ? Consultez le [dépôt](https://github.com/Ryan-Gordon/Ionic-Firestarter) (et donnez-lui une étoile si vous le trouvez utile) !**

Pour suivre ce tutoriel, vous aurez besoin de Node.js et d'Ionic installés.

### Pour commencer

Pour installer Ionic et Cordova (qui est nécessaire pour les plugins pour le moment), exécutez la commande suivante dans le terminal après avoir installé Node :

```bash
npm install -g ionic cordova
```

> _Si vous obtenez EACCES : permission refusée, vous devrez peut-être exécuter la commande avec sudo ?_

![Image](https://cdn-media-1.freecodecamp.org/images/1*O7an59vwaCcUeF8YHm9frg.png)

Pour créer une application avec Ionic, commencez <nomdelapp> <modèle>. Pour cela, nous utiliserons un modèle vide comme point de départ.

Le code pour la connexion Google sera placé dans une classe de fournisseur qui sera appelée par la page ayant besoin d'utiliser cette méthode de connexion.

```
ionic g provider auth
```

### Configurer l'application avec Firebase et obtenir les identifiants

Pour que Firebase fonctionne avec les plateformes natives Android et iOS, nous devrons effectuer deux configurations pour l'application, chacune étant un peu différente.

Pour chaque appareil, nous devrons configurer l'API Google Sign In.

#### iOS

![Image](https://cdn-media-1.freecodecamp.org/images/1*KlFx5bRuIjvvlsaK5JTc6g.png)

Pour la configuration iOS, vous devez fournir l'ID de bundle. Il s'agit de la valeur dans config.xml qui est généralement définie sur io.ionic.starter. Changez cela en ce que vous voulez, et ce sera votre ID de bundle.

Assurez-vous de ne pas le laisser à la valeur par défaut.

Après la configuration, vous obtiendrez un fichier GoogleService-Info.plist. Enregistrez ce fichier à la racine du dossier du projet Ionic. Après avoir effectué ces étapes, vous avez terminé ! Pour iOS au moins...

Vous devriez maintenant voir l'interface utilisateur suivante et avoir votre fichier Plist téléchargé et prêt à l'emploi.

![Image](https://cdn-media-1.freecodecamp.org/images/1*04dZ4snRrJ7hyuim6C2Q-w.png)

#### Android

Le processus d'ajout de la connexion Google à la plateforme Android est presque identique, avec une exigence supplémentaire. Pour commencer, rendez-vous [sur ce lien](https://developers.google.com/mobile/add?platform=android&cntapi=signin), et commencez à créer votre application Android.

> _Il est important de noter que pour construire sur Android (et aussi pour utiliser ce plugin), vous devrez installer les outils de construction Android version 19.1.0 ou supérieure._

#### Acquisition de la clé ?

Une fois les outils de construction installés et que vous avez confirmé cela, le keystore devrait être disponible pour obtenir la valeur SHA-1 dont nous avons besoin pour la partie Android du processus. Le keystore est utilisé pour contenir les clés de signature que vous utilisez pour les applications que vous construisez.

Exécutez cette commande dans le terminal pour acquérir la valeur SHA-1 nécessaire :

```
keytool -exportcert -list -v -alias androiddebugkey -keystore ~/.android/debug.keystore
```

> **_Important_**_: Cela sera différent du keystore que vous utiliseriez si vous mettez l'application en production. Arrêtez-vous à ce stade et réfléchissez — allez-vous la publier ? Il peut être judicieux d'utiliser le keystore de publication si c'est le cas._

![Image](https://cdn-media-1.freecodecamp.org/images/1*QelLvXTfoua-6TSoJJjTpQ.png)

Après cette étape, rendez-vous [sur ce lien](https://developers.google.com/mobile/add?platform=android&cntapi=signin), et ajoutez votre projet Android.

Assurez-vous à nouveau que vous avez changé la valeur 'id' dans config.xml pour votre projet afin qu'elle ne soit plus `io.ionic.starter`.

Il vous demandera la valeur SHA-1 que nous avons obtenue depuis le terminal. Entrez-la et vous aurez la possibilité de télécharger un fichier google-services.json. Téléchargez ce fichier et enregistrez-le à la racine de votre projet. Gardez-le en sécurité !

### Installation de la connexion Google dans votre base de code

L'une des bonnes choses à propos d'Ionic est sa documentation. Elle dispose de docs disponibles pour la plupart des plugins et composants. La documentation de la connexion Google pour Ionic [peut être trouvée ici.](https://ionicframework.com/docs/native/google-plus/)

Exécutez ces commandes dans le terminal pour ajouter le plugin au projet.

```bash
$ ionic cordova plugin add cordova-plugin-googleplus --variable REVERSED_CLIENT_ID=myreversedclientid
$ npm install --save @ionic-native/google-plus
```

À ce stade, vous avez configuré l'API Google Sign-in pour iOS et Android. Vous avez deux fichiers de configuration (un pour chaque plateforme) et deux plugins installés et prêts à l'emploi.

### Configuration de Firebase

Firebase sera l'hôte des connexions OAuth comme Google Plus. Avant de pouvoir l'utiliser dans le projet, vous devez configurer le projet dans Firebase. Si vous ne l'avez jamais fait auparavant, rendez-vous [sur ce post pour savoir comment](https://medium.com/@ryangordon210/adding-firebase-and-angular-fire-to-an-ionic-project-23ca243b79a4) configurer une configuration Firebase et initialiser Firebase lui-même.

Au minimum, vous devez avoir ces packages installés :

```bash
npm install angularfire2 firebase
```

#### Utilisation du plugin

La première étape consiste à configurer un écouteur qui réagira aux événements, tels que lorsqu'un utilisateur se connecte ou se déconnecte. Si un événement de connexion se produit, l'objet utilisateur contiendra des informations d'identification pour cet utilisateur, telles que son nom et sa photo de profil.

```ts
//Configurer un écouteur pour quand l'état d'authentification change (Connexion/Déconnexion) et effectuer une action.
  firebase.auth().onAuthStateChanged( user => {
    if (user){
      this.userProfile = user;
    } else { 
        this.userProfile = null;
    }
  });
```

Ce morceau de code doit être dans le constructeur soit de home.ts dans ce projet, soit de toute page où vous voulez suivre l'état de l'AuthState.

#### Code de connexion Google

Vous êtes arrivé jusqu'ici. Doot doot ! ?.

La dernière partie pour connecter les utilisateurs est le flux d'authentification Google lui-même.

Vous devez tester cette partie sur un appareil, car le plugin Ionic Native utilise Cordova qui nécessite une construction sur un appareil.

```ts
googleLogin(): Promise<any> {
  return new Promise((resolve, reject) => { 
      this.googlePlus.login({
        'webClientId': '5351366995-npuh9q89gaoiagoc4jssqck26gorj7hh.apps.googleusercontent.com',
        'offline': true
      }).then( res => {
              const googleCredential = firebase.auth.GoogleAuthProvider
                  .credential(res.idToken);

              firebase.auth().signInWithCredential(googleCredential)
            .then( response => {
                console.log("Succès Firebase : " + JSON.stringify(response));
                resolve(response)
            });
      }, err => {
          console.error("Erreur : ", err)
          reject(err);
      });
    });
    }
```

Le modèle que nous visons est de configurer les fonctions pour qu'elles retournent des promesses. Ensuite, si nous en avons besoin, nous pouvons effectuer une action avec le résultat.

Si la connexion est réussie, nous obtiendrons une information d'identification à partir du résultat et connecterons l'utilisateur à notre Firebase.

Enfin, selon le résultat, nous résoudrons ou rejetterons la promesse. Cela déclenchera soit la clause .then soit la clause .catch partout où cette fonction est appelée.

Dans le fichier home.ts, cette fonction googleLogin peut être appelée avec une clause .then et .catch, et le résultat sera passé en conséquence au cas où nous aurions besoin de faire quelque chose avec.

Lorsque la connexion est terminée, l'écouteur onAuthStateChanged sera déclenché et les informations de l'utilisateur seront mises à jour sur la page.

La connexion Google Plus est maintenant connectée à Firebase et fonctionne sur l'appareil. Si vous prévoyez de mettre cette application en production, comme indiqué, vous devrez refaire quelques choses et utiliser un keystore différent pour la publication.

### **Conclusion**

Dans cet article, nous avons configuré l'API Google Sign-in et travaillé sur une solution multiplateforme pour connecter les utilisateurs à notre Firebase avec Google Plus.

Bien qu'il y ait beaucoup de configuration requise entre la console des développeurs Google et Firebase, l'avantage est que nos utilisateurs peuvent maintenant se connecter à n'importe quelle application web que nous construisons avec leurs comptes Google existants.

Ce post est le premier d'une série que je prévois d'écrire pour les connexions Firebase / Ionic.

Si vous voulez accéder au code, voici à nouveau un lien vers le dépôt :

[**Ryan-Gordon/Ionic-Firestarter**](https://github.com/Ryan-Gordon/Ionic-Firestarter)  
[_Ionic-Firestarter - Ionic Firestarter est un projet open source mettant en avant différentes fonctionnalités de Firebase implémentées dans_](https://github.com/Ryan-Gordon/Ionic-Firestarter)  
[github.com](https://github.com/Ryan-Gordon/Ionic-Firestarter)

Vous voulez des posts similaires sur Ionic ? Voici quelques autres posts que j'ai faits :

[**Comment thématiser dynamiquement votre application Ionic et rendre vos utilisateurs heureux**  
_Concevoir un schéma de couleurs élégant pour votre application mobile peut prendre du temps. Pourquoi ne pas laisser l'utilisateur choisir son propre_](https://www.freecodecamp.org/news/how-to-dynamically-theme-your-ionic-application-and-make-your-users-happy-ffa17e15dbf7/)

[**Méthodes alternatives de connexion pour Firebase avec Ionic**](https://medium.com/@ryangordon210/alternative-sign-in-methods-for-firebase-with-ionic-52714ee9be83)  
[_Dans mes autres posts sur les connexions Firebase, l'accent a été mis sur les fournisseurs sociaux. Le point principal de cette emphase est de_](https://medium.com/@ryangordon210/alternative-sign-in-methods-for-firebase-with-ionic-52714ee9be83)  
[medium.com](https://medium.com/@ryangordon210/alternative-sign-in-methods-for-firebase-with-ionic-52714ee9be83)