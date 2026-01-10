---
title: Comment développer un excellent flux de connexion Facebook avec Firebase et
  Ionic
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-05T22:09:49.000Z'
originalURL: https://freecodecamp.org/news/how-to-develop-a-great-facebook-login-flow-with-firebase-and-ionic-656a295c4fe9
coverImage: https://cdn-media-1.freecodecamp.org/images/1*YftIGPfmk-Sok90hvhY05Q.png
tags:
- name: authentication
  slug: authentication
- name: Facebook
  slug: facebook
- name: Firebase
  slug: firebase
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment développer un excellent flux de connexion Facebook avec Firebase
  et Ionic
seo_desc: 'By Ryan Gordon

  It’s helpful to use social sign-ins with Ionic for your users who would rather not
  create and remember another username:password combination. Instead, you can allow
  users to sign in with accounts they already own. You don’t need to sto...'
---

Par Ryan Gordon

Il est utile d'utiliser des connexions sociales avec Ionic pour vos utilisateurs qui préféreraient ne pas créer et mémoriser une autre combinaison nom d'utilisateur:mot de passe. Au lieu de cela, vous pouvez permettre aux utilisateurs de se connecter avec des comptes qu'ils possèdent déjà. Vous n'avez pas besoin de stocker des mots de passe hachés pour les comparer, vous n'avez pas à gérer l'envoi d'e-mails d'inscription, et vous n'avez pas besoin de réinitialiser les mots de passe. Le fournisseur choisi par l'utilisateur gérera tout cela pour vous.

**Vous voulez simplement consulter le code au lieu de suivre l'article ? N'hésitez pas à donner une étoile au [dépôt](https://github.com/Ryan-Gordon/Ionic-Firestarter) si vous le trouvez utile !**

Une partie de cet article sera très similaire aux autres tutoriels de ma page. Si vous avez Ionic et Node installés et que vous avez un projet configuré, vous pouvez passer directement au code [ici](#6156).

Pour suivre ce tutoriel, vous aurez besoin d'avoir Node.js et Ionic installés.

Pour installer Ionic et Cordova, qui est nécessaire pour les plugins pour le moment, exécutez la commande suivante dans votre terminal après avoir installé Node :

```bash
npm install -g ionic cordova
```

Si vous obtenez EACCES: permission denied, vous devrez peut-être exécuter la commande avec sudo.

![Image](https://cdn-media-1.freecodecamp.org/images/1*O7an59vwaCcUeF8YHm9frg.png)

Créez une application avec ionic start <appname> <template>. Pour cela, utilisez un modèle vide comme point de départ.

Le code pour la connexion Facebook sera placé dans une classe de fournisseur qui sera appelée par toute page ayant besoin d'utiliser cette méthode de connexion.

```bash
ionic g provider auth
```

### Configurer l'application avec Firebase et obtenir les identifiants

Pour que Firebase fonctionne avec la plateforme Facebook, nous devrons effectuer trois étapes :

— Configurer une nouvelle application dans le portail des développeurs Facebook

— Configurer la connexion Facebook sur Firebase

— Implémenter le flux de connexion

#### Portail des développeurs Facebook

Le Portail des Développeurs Facebook est une interface pour tous les outils de développement et les API disponibles. C'est ce que nous utiliserons pour configurer l'API de connexion du côté de Facebook.

![Image](https://cdn-media-1.freecodecamp.org/images/1*8GTVmvTMHbsN8-i0_BJp0w.png)

Choisissez un nom et une adresse e-mail de contact pour votre application. L'e-mail de contact peut être affiché aux utilisateurs, assurez-vous donc qu'il est professionnel.

Après cela, l'application sera créée sur Facebook et nous pourrons ajouter le plugin à notre application !

Il y aura deux plugins nécessaires. Le plugin Cordova conçu pour fonctionner avec Facebook de manière native, et un wrapper pour celui-ci.

```bash
$ ionic plugin add cordova-plugin-facebook4 --variable APP_ID="123456789" --variable APP_NAME="myApplication"
```

Vous devrez remplacer les valeurs de `APP_ID` et `APP_NAME` par vos véritables identifiants. Vous pouvez trouver ces deux informations dans votre tableau de bord du Développeur Facebook.

L'autre plugin nous permettra de travailler avec le premier, via TypeScript.

```bash
npm install --save @ionic-native/facebook 
```

Maintenant, nous avons le plugin installé et connecté à la console Facebook.

Il reste deux étapes finales pour cela : sélectionner les plateformes que nous utiliserons sur le Portail des Développeurs FB et importer dans le app.module.

#### Sélection des plateformes dans le portail FB

Notre application est créée, cependant, nous devons spécifier quelles applications peuvent utiliser notre API de connexion. Cela se fait en ajoutant des plateformes avec un identifiant de bundle que nous spécifions.

![Image](https://cdn-media-1.freecodecamp.org/images/1*3apVFW4u2k0k_2piCMPA9w.png)

Pour commencer, cliquez sur Ajouter une plateforme, puis sélectionnez Android ou iOS. Les deux plateformes devront connaître l'ID généré de votre application lorsqu'elle est en déploiement.

La valeur de l'ID trouvée en haut de votre fichier config.xml sera utilisée à la fois pour le nom du package du Google Play Store et le BundleID.

> N'oubliez pas d'importer également le plugin dans votre fichier `_app.module.ts_` et de le spécifier comme fournisseur pour le projet.

### Configurer la connexion Facebook sur Firebase

Configurer la connexion dans Firebase sera la tâche la plus facile. Une fois l'application créée sur le portail des développeurs FB, elle aura un APPID et un APPSECRET. Ces deux valeurs sont nécessaires pour lier Firebase à notre application Facebook.

![Image](https://cdn-media-1.freecodecamp.org/images/1*58Khs2B3iNFKDVWxsGwviA.png)

Une fois ces valeurs saisies, cliquez sur activer et c'est tout !

### Implémenter le flux de connexion

Après toute la configuration, nous arrivons à la partie amusante : coder et tester !

Si vous avez suivi jusqu'à présent, les deux plugins Facebook Ionic sont maintenant installés et l'application est configurée dans Firebase et le Portail des Développeurs FB.

Avant de pouvoir utiliser le plugin dans notre code, nous devons l'importer et le mettre en portée avec le constructeur. Après cela, nous sommes libres d'utiliser le plugin n'importe où dans ce fournisseur.

```ts
import { Facebook } from '@ionic-native/facebook';

@Injectable()

export class AuthProvider {
    
constructor(private googlePlus: GooglePlus, private facebook:Facebook) {
    
}
```

Le code pour la connexion elle-même vous semblera très familier si vous avez vu les autres articles. Ce que nous faisons ici, c'est utiliser le plugin Facebook natif pour effectuer un flux de connexion. Si c'est réussi, prenez la réponse d'authentification fournie et connectez-vous à Firebase.

Cette fonction peut être appelée n'importe où dans l'application en important le fournisseur d'authentification. La manière prévue d'utiliser cela sera qu'une page (comme `home.ts`) aura AuthProvider en portée. Lorsque l'utilisateur clique sur un bouton de connexion FB, nous déléguerons la connexion à notre AuthProvider.

Maintenant, lorsque cette fonction est appelée, une interface utilisateur native de Facebook s'ouvrira pour demander une connexion. Ou si l'utilisateur est déjà connecté, il demandera simplement l'autorisation OAuth — et c'est tout ! Nous obtenons un jeton que nous pouvons utiliser pour créer un identifiant, et cet identifiant est ensuite utilisé pour se connecter à Firebase.

```ts
facebookLogin(): Promise<any> {
    return this.facebook.login(['email'])
      .then( response => {
        const facebookCredential = firebase.auth.FacebookAuthProvider
          .credential(response.authResponse.accessToken);
  
        firebase.auth().signInWithCredential(facebookCredential)
          .then( success => { 
            console.log("Firebase success: " + JSON.stringify(success)); 
          });
  
      }).catch((error) => { console.log(error) });
  }
```

### Conclusion

Dans cet article, nous avons configuré l'API de connexion Facebook et travaillé sur une solution multiplateforme pour connecter les utilisateurs à notre Firebase avec Facebook.

Comme pour la connexion Google, une certaine configuration était nécessaire (bien que moins). Maintenant, l'avantage est que nos utilisateurs peuvent se connecter à toutes les applications web que nous développons avec leurs comptes Facebook existants. Si vous avez également suivi le premier article, alors l'application dispose maintenant de la connexion Google et Facebook !

Tout le code de ce tutoriel (et tous mes autres tutoriels) peut être [trouvé ici](https://github.com/Ryan-Gordon/Ionic-Firestarter). Je vise à implémenter autant de fonctionnalités Firebase que possible, et OUI, je recherche des contributeurs !

Si vous voulez accéder au code, voici à nouveau un lien vers le dépôt :

[**Ryan-Gordon/Ionic-Firestarter**](https://github.com/Ryan-Gordon/Ionic-Firestarter)  
[_Ionic-Firestarter — Ionic Firestarter est un projet open source mettant en avant différentes fonctionnalités Firebase implémentées dans…_](https://github.com/Ryan-Gordon/Ionic-Firestarter)  
[github.com](https://github.com/Ryan-Gordon/Ionic-Firestarter)

Vous voulez des articles similaires sur Ionic ? Voici quelques autres articles que j'ai écrits :

[**Comment thématiser dynamiquement votre application Ionic et rendre vos utilisateurs heureux**  
_Concevoir un schéma de couleurs élégant pour votre application mobile peut prendre du temps. Pourquoi ne pas laisser l'utilisateur choisir son propre…_](https://www.freecodecamp.org/news/how-to-dynamically-theme-your-ionic-application-and-make-your-users-happy-ffa17e15dbf7/)  


[**Méthodes alternatives de connexion pour Firebase avec Ionic**](https://medium.com/@ryangordon210/alternative-sign-in-methods-for-firebase-with-ionic-52714ee9be83)  
[_Dans mes autres articles sur les connexions Firebase, l'accent a été mis sur les fournisseurs sociaux. Le point principal de cette emphase est de…_](https://medium.com/@ryangordon210/alternative-sign-in-methods-for-firebase-with-ionic-52714ee9be83)