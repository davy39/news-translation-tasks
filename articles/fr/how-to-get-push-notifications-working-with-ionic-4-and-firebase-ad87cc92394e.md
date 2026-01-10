---
title: Comment activer les notifications push avec Ionic 4 et Firebase
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-25T14:27:04.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-push-notifications-working-with-ionic-4-and-firebase-ad87cc92394e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*EciBTQhuzIrkzA12dfsQJQ.jpeg
tags:
- name: Apps
  slug: apps-tag
- name: Firebase
  slug: firebase
- name: General Programming
  slug: programming
- name: push notification
  slug: push-notification
- name: 'tech '
  slug: tech
seo_title: Comment activer les notifications push avec Ionic 4 et Firebase
seo_desc: 'By Filip Jerga

  A full step-by-step tutorial that will get you on the right track for iOS and Android


  Setting up push notifications can be truly frustrating and time consuming. So I
  went through all of the setups and prepared this tutorial for you.

  P...'
---

Par Filip Jerga

#### Un tutoriel étape par étape complet qui vous mettra sur la bonne voie pour iOS et Android

![Image](https://cdn-media-1.freecodecamp.org/images/1*EciBTQhuzIrkzA12dfsQJQ.jpeg)

Configurer les notifications push peut être vraiment frustrant et chronophage. J'ai donc passé en revue toutes les configurations et préparé ce tutoriel pour vous.

### Prérequis

Ionic 4 doit déjà être installé.

### Navigation dans les sections

1. [Installation des packages](https://www.freecodecamp.org/news/how-to-get-push-notifications-working-with-ionic-4-and-firebase-ad87cc92394e/#1-installation-des-packages)
2. [Configuration Firebase pour Android et iOS](https://www.freecodecamp.org/news/how-to-get-push-notifications-working-with-ionic-4-and-firebase-ad87cc92394e/#2-configuration-firebase-pour-ios-et-android)
3. [Implémentation du code de notification push](https://www.freecodecamp.org/news/how-to-get-push-notifications-working-with-ionic-4-and-firebase-ad87cc92394e/#3-implémentation-du-code-de-notification-push)
4. [Test des notifications push sur Android](https://www.freecodecamp.org/news/how-to-get-push-notifications-working-with-ionic-4-and-firebase-ad87cc92394e/#4-test-des-notifications-push-sur-android)
5. [Pré-configuration des notifications push pour iOS](https://www.freecodecamp.org/news/how-to-get-push-notifications-working-with-ionic-4-and-firebase-ad87cc92394e/#5-pré-configuration-des-notifications-push-pour-ios)
6. [Test des notifications push sur iOS](https://www.freecodecamp.org/news/how-to-get-push-notifications-working-with-ionic-4-and-firebase-ad87cc92394e/#6-test-des-notifications-push-sur-ios)

### 1. Installation des packages

Ouvrez votre projet Ionic dans l'éditeur de code de votre choix, et ouvrez également votre terminal. Naviguez jusqu'au dossier de votre projet.

Tout d'abord, nous allons installer tous les packages requis.

**Ce dont nous avons besoin pour installer :**

* **Plugin Cordova pour Firebase :** `ionic cordova plugin add cordova-plugin-firebase`
* **Package natif Firebase :** comme Ionic 4 est en bêta, vérifiez vos packages Ionic-native dans `package.json` et installez la même version que les autres packages Ionic-native. Enfin, tapons : `npm install --save @ionic-native/firebase@5.0.0-beta.14`

![Image](https://cdn-media-1.freecodecamp.org/images/1*4R0G8E3rY6N8xrwRYpWO8A.png)
_J'ai la version bêta.14_

* Un dernier package, **AngularFire 2**. Il s'agit d'une bibliothèque pour Angular et Firebase : `npm install --save angularfire2 firebase`

Les packages sont installés, c'est fait ! Passons à la deuxième section.

### 2. Configuration Firebase pour iOS et Android

Avant de commencer toute la configuration, je dois vous avertir que vous ne pouvez pas tester vos notifications push sur l'émulateur iOS. Pour le tester, vous devez avoir un compte développeur Apple, qui coûte environ 99 USD par an. Je vous suggère de passer par la configuration iOS quand même afin d'avoir une meilleure compréhension pour les futurs projets.

**Note :** Les étapes à partir d'ici sont très importantes, alors soyez patient. Lisez lentement et assurez-vous de tout faire correctement. Chercher des problèmes après toute la configuration peut être très frustrant, croyez-moi — je parle de ma propre expérience.

#### iOS

[Accédez à la page Firebase](https://firebase.google.com) et connectez-vous à la console. Si vous n'avez pas encore de projet créé, faites-le maintenant. Vous devriez voir cet écran.

![Image](https://cdn-media-1.freecodecamp.org/images/1*YKEMKgcl7nukC-1QOOqmAw.png)

Cliquez sur le bouton iOS et vous verrez ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*yzwF8xD5qUFfy5yBWmmkZw.png)

Maintenant, nous devons fournir notre identifiant de bundle iOS et celui-ci doit être le même que dans votre projet Ionic. Supposons que je veux avoir le nom de bundle `com.filipjerga.angularcourse`, alors je dois faire ce qui suit :

Ouvrez vos projets Ionic et naviguez jusqu'au fichier « config.xml ». Inspectons l'élément widget. L'attribut **Id** contient l'identifiant unique de votre application. J'ai dit avant que si vous avez spécifié votre nom de bundle à `com.filipjerga.angularcourse` dans Firebase, l'**id** dans votre projet Ionic doit être le même ! Vous pouvez également laisser l'**id** tel que vous l'avez déjà dans votre projet Ionic, mais alors vous devez le changer dans Firebase.

![Image](https://cdn-media-1.freecodecamp.org/images/1*nKaEn3rqKjQQSK5DbOTx1Q.png)
_l'élément widget id est ce que nous devons spécifier dans Firebase_

Après avoir obtenu la valeur de **id**, n'oubliez pas de la fournir à votre application Firebase en tant qu'identifiant de bundle.

![Image](https://cdn-media-1.freecodecamp.org/images/1*80_WthW7_5CQbd5Dcg6BvA.png)
_L'identifiant de bundle doit être le même que votre identifiant de widget_

Cela devrait être tout dans la première étape de l'enregistrement de l'application. Cette étape est cruciale, alors vérifiez à nouveau la valeur de **id** sur le widget et l'identifiant de bundle de votre application Firebase.

Laissez les autres champs vides et cliquez sur « Enregistrer l'application ».

Maintenant, nous devons télécharger « GoogleService-Info.plist ».

![Image](https://cdn-media-1.freecodecamp.org/images/1*OdG0hBlzpiMMvYT7w6gPxg.png)

Quand il est téléchargé, collez-le dans le dossier de base de vos projets. Vous pouvez voir une structure de dossier dans [mon projet ici](https://github.com/Jerga99/heartStoneLib).

Nous pouvons sauter toutes les étapes suivantes, car elles ne sont pas requises pour la configuration du projet Ionic. Vous devriez avoir votre application IOS prête.

![Image](https://cdn-media-1.freecodecamp.org/images/1*HVdgpvS2Rv2a1dfuNDPgtw.png)
_Passez cette étape_

#### Android

Les étapes suivantes pour Android sont presque les mêmes que pour la configuration iOS :

* Cliquez sur « ajouter une application » pour Android, comme nous l'avons fait pour iOS précédemment.
* Le nom du package Android doit être le même que notre identifiant de widget, dans mon cas : `com.filipjerga.angularcourse`
* Ensuite, téléchargez `google-services.json`. Comme avant avec le fichier iOS, nous devons le copier dans le dossier de base de nos applications
* Cliquez sur « Suivant » jusqu'à ce que vous soyez à la dernière étape, que vous pouvez sauter, et vous devriez vous retrouver avec les deux applications créées.

Hourra ! Félicitations ! Mais il est encore trop tôt pour se réjouir.

![Image](https://cdn-media-1.freecodecamp.org/images/1*QN0VI93SeNd5aJ1-yDHJSg.png)
_Les applications iOS et Angular sont créées._

### 3. Implémentation du code de notification push

#### Importation des packages

Le moment est venu de enfin réchauffer nos doigts en tapant du code. Nous allons commencer par importer les packages que nous avons installés précédemment.

1. Allez dans `app.module.ts`
2. Votre fichier devrait ressembler à ceci :

```ts
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { RouterModule, RouteReuseStrategy } from '@angular/router';

import { IonicModule, IonicRouteStrategy } from '@ionic/angular';
import { SplashScreen } from '@ionic-native/splash-screen/ngx';
import { StatusBar } from '@ionic-native/status-bar/ngx';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

import { AngularFireModule } from 'angularfire2';
import { AngularFirestoreModule } from 'angularfire2/firestore';
import { Firebase } from '@ionic-native/firebase/ngx';

const config = {
    apiKey: "AIzaSyD-K6SlFECXKmd8iHwEvggVtavKgyPF2k8",
    authDomain: "angular2-course-9270e.firebaseapp.com",
    databaseURL: "https://angular2-course-9270e.firebaseio.com",
    projectId: "angular2-course-9270e",
    storageBucket: "angular2-course-9270e.appspot.com",
    messagingSenderId: "443316848633"
  };

@NgModule({
  declarations: [AppComponent],
  entryComponents: [],
  imports: [
    BrowserModule,
    IonicModule.forRoot(),
    AppRoutingModule,
    IonicStorageModule.forRoot(),
    AngularFireModule.initializeApp(config),
    AngularFirestoreModule],
  providers: [
    StatusBar,
    SplashScreen,
    Firebase,
    { provide: RouteReuseStrategy, useClass: IonicRouteStrategy }
  ],
  bootstrap: [AppComponent]
})
export class AppModule {}
```

Vous pouvez voir `Firebase` dans le tableau des providers, et `AngularFirestoreModule` et `AngularFireModule` dans les imports.

Mais d'où vient l'objet `config` ? Vous pouvez voir beaucoup d'informations là-bas comme « apiKey, authDomain » et ainsi de suite.

Pour répondre à cela, nous devons retourner à notre console Firebase et créer une **application web**.

![Image](https://cdn-media-1.freecodecamp.org/images/1*js9Izqbu8Bceb2kIZSDzRg.png)
_Sélectionnez la plateforme web_

Vous devez cliquer sur l'icône de la plateforme web à droite de l'icône Android (voir l'image ci-dessus). Lorsque l'application web est sélectionnée, vous verrez votre propre objet **config**.

![Image](https://cdn-media-1.freecodecamp.org/images/1*5a3ry984v5Mer9Ob63axZQ.png)
_Mon objet config pour Firebase après avoir sélectionné l'application web._

Maintenant, il est temps de copier tout l'objet **config** dans `app.module.ts` dans nos projets Ionic. Veuillez **vous assurer** de le changer pour votre objet config ! Le mien ne fonctionnera pas pour vous.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Gkp_0kiAs4f_t3UL_hUNVw.png)
_Fournir config à app.module.ts_

Maintenant, nous pouvons commencer à travailler sur l'implémentation du service de notification push.

#### Service de notification push

Créons un nouveau service. Appelez-le comme vous voulez. Je vais appeler le mien `fcm.service.ts`. FCM signifie Firebase Cloud Messaging.

Tout d'abord, jetons un coup d'œil à l'implémentation du service. Je vais l'expliquer ligne par ligne.

```ts
import { Injectable } from '@angular/core';
import { Firebase } from '@ionic-native/firebase/ngx';
import { Platform } from '@ionic/angular';
import { AngularFirestore } from 'angularfire2/firestore';

@Injectable()
export class FcmService {

  constructor(private firebase: Firebase,
              private afs: AngularFirestore,
              private platform: Platform) {}

  async getToken() {
    let token;

    if (this.platform.is('android')) {
      token = await this.firebase.getToken();
    }

    if (this.platform.is('ios')) {
      token = await this.firebase.getToken();
      await this.firebase.grantPermission();
    }

    this.saveToken(token);
  }

  private saveToken(token) {
    if (!token) return;

    const devicesRef = this.afs.collection('devices');

    const data = {
      token,
      userId: 'testUserId'
    };

    return devicesRef.doc(token).set(data);
  }

  onNotifications() {
    return this.firebase.onNotificationOpen();
  }
}
```

Si nous voulons envoyer une notification push à un appareil, nous devons obtenir un identifiant unique de l'appareil. Dans ce cas, il est appelé `token`.

Nous devons vérifier le type spécifique de l'appareil, à cause d'une étape supplémentaire dans la configuration iOS. iOS nécessite des permissions explicites pour recevoir des notifications push.

Maintenant, nous devons stocker ce token quelque part, mais où ? Nous allons stocker les tokens dans la **base de données Firebase**. Vous pouvez voir que je crée une collection **devices** et que je la remplis avec des `data` qui contiennent le `token` et juste un `UserId` de test. Parfait ! Maintenant, nous avons stocké notre token et nous pouvons nous abonner aux notifications.

S'abonner aux notifications est en fait très simple. Nous devons simplement appeler `this.firebase.onNotificationOpen()`

Incroyable. Service vérifié !

Tout cela est bien, mais un peu inutile, puisque nous n'utilisons pas encore notre service. Corrigons cela !

Allez dans votre `app.component.ts` et écrivez ce qui suit :

```ts
import { Component } from '@angular/core';

import { Platform } from '@ionic/angular';
import { SplashScreen } from '@ionic-native/splash-screen/ngx';
import { StatusBar } from '@ionic-native/status-bar/ngx';

import { FcmService } from './shared/service/fcm.service';
import { ToastService } from './shared/service/toast.service';
import { ToastController } from '@ionic/angular';

@Component({
  selector: 'app-root',
  templateUrl: 'app.component.html'
})
export class AppComponent {

  constructor(
    private platform: Platform,
    private splashScreen: SplashScreen,
    private statusBar: StatusBar,
    private fcm: FcmService,
    private toastr: ToastService,
    public toastController: ToastController

  ) {
    this.initializeApp();
  }

  private async presentToast(message) {
    const toast = await this.toastController.create({
      message,
      duration: 3000
    });
    toast.present();
  }

  private notificationSetup() {
    this.fcm.getToken();
    this.fcm.onNotifications().subscribe(
      (msg) => {
        if (this.platform.is('ios')) {
          this.presentToast(msg.aps.alert);
        } else {
          this.presentToast(msg.body);
        }
      });
  }

  initializeApp() {
    this.platform.ready().then(() => {
      this.statusBar.styleDefault();
      this.splashScreen.hide();
      this.notificationSetup();
    });
  }
}
```

La fonction `notificationSetup` est particulièrement importante ici.

Nous obtenons d'abord un token unique de l'appareil.

Nous nous abonnons également aux notifications entrantes de Firebase.

Lorsque le message est reçu, nous devons vérifier, à nouveau, les plateformes spécifiques. Sur iOS, le texte de votre message se trouve sous `aps.alert`. Sur Android, il se trouve sous `body`.

Ensuite, nous allons simplement afficher le message reçu sous forme de `Toast`.

Maintenant, la configuration du code est terminée. Nous y sommes presque ! Il est temps de le tester.

### 4. Test des notifications push sur Android

Toutes les configurations requises pour Android devraient être terminées maintenant. Vous pouvez commencer à émuler votre application avec :

`ionic cordova emulate android`

ou

`ionic cordova build android` et ouvrez votre build manuellement dans Android Studio.

Lançons nos applications et allons dans le menu Accueil, afin de voir une notification push là-bas. Assurez-vous que votre application a été lancée correctement dans l'émulateur et que vous n'avez pas d'erreurs.

Retournez à vos navigateurs sur vos applications Firebase. Il est maintenant temps d'inspecter notre base de données Firebase. Vous pouvez trouver l'option de base de données dans le panneau de gauche sous la catégorie **Développer**.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ev05fxLy5yySp_Xa-uA4JQ.png)
_Base de données Firebase_

Après que votre application a été lancée dans les émulateurs, le code de **app.component.ts** que nous avons écrit il y a quelques instants a été exécuté. Pas étonnant que notre base de données soit peuplée. Dans la fonction « saveToken », nous avons spécifié la collection « devices » et nous avons sauvegardé le token avec l'identifiant utilisateur en tant que document dans cette collection d'appareils. C'est ce que nous voyons dans notre base de données.

Dans mon cas, j'ai plusieurs tokens dans ma base de données, mais vous devriez en avoir un seul puisque nous avons exécuté notre application pour la première fois. Vous créerez un nouveau document par appareil/émulateur unique sur lequel vous exécutez votre application.

Il est maintenant temps de copier ce token afin d'envoyer une notification push à un appareil spécifique.

![Image](https://cdn-media-1.freecodecamp.org/images/1*tGtpXyvp46jGuGr9SzsBTg.png)
_Collection de la base de données Firebase, vous ne verrez qu'un seul document_

**Naviguez vers le panneau de gauche dans l'onglet de croissance** et cliquez sur la messagerie cloud.

![Image](https://cdn-media-1.freecodecamp.org/images/1*_oO9cu4Gw3IAXbvGuWeWOQ.png)
_Cliquez sur Cloud Messaging_

Maintenant, nous devons remplir les données nécessaires. Entrez le texte de votre message et fournissez le token de l'appareil de la base de données que nous venons de copier.

![Image](https://cdn-media-1.freecodecamp.org/images/1*vdXEcVntcKkfqr8ll49r6Q.png)

Lorsque vous envoyez un message, ouvrez votre appareil émulé simultanément et regardez ce qui se passe.

Envoyez un message, et félicitations ! Maintenant, votre configuration Android est terminée et vous êtes en mesure d'envoyer des notifications push ! N'est-ce pas génial ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*HwQKVZAHeF6Tb1QZV46Zzw.png)
_Notification push sur Android._

### 5. Pré-configuration des notifications push pour iOS

Attachez vos ceintures, la configuration iOS arrive. Séparons cette configuration en plusieurs étapes, afin de ne pas avoir de crise de panique. Creusons !

**Tout d'abord**, construisez votre application pour iOS : `ionic cordova build ios`

Ouvrez votre Xcode, et trouvez votre application construite dans `platforms/ios/nomdevotreapp.xcodeproj`. Ouvrez-la.

![Image](https://cdn-media-1.freecodecamp.org/images/1*2J27mF3dE36yro4TDuDbZA.png)
_Ouvrez votre .xcodeproj_

Cela devrait ouvrir une structure arborescente de votre application sur le côté gauche. Double-cliquez sur le fichier racine de cette structure. Cela ouvrira un menu supplémentaire avec plus de paramètres pour votre application.

![Image](https://cdn-media-1.freecodecamp.org/images/1*CwCbrVvqy_lYJhOHahe5qQ.png)
_Plus de paramètres_

Connectez-vous avec votre compte développeur.

![Image](https://cdn-media-1.freecodecamp.org/images/1*AD1U9EEfHRozZHoUn3d5Ng.png)
_Connectez-vous avec un compte développeur_

5. Ouvrez l'onglet supérieur « Capacités » et activez « Notifications Push ».

![Image](https://cdn-media-1.freecodecamp.org/images/1*4lOdzB6p9BWGiVkYuC1G1w.png)
_Activer les notifications push_

6. Naviguez jusqu'à votre [page de compte développeur Apple](https://developer.apple.com). Sous « Certificats », sélectionnez « Tous » et cliquez sur « `+` » pour **ajouter** un nouveau certificat.

![Image](https://cdn-media-1.freecodecamp.org/images/1*M_sJ-0Y6UcfCSXvZexoh9g.png)
_Cliquez sur le signe plus._

Activez le service de notification push Apple et passez à l'étape suivante.

![Image](https://cdn-media-1.freecodecamp.org/images/1*sUsADfJUdEJcyi2xblFjwg.png)

Maintenant, choisissons votre application.

![Image](https://cdn-media-1.freecodecamp.org/images/1*nXick1xCKeQt8Xrv5LSdvw.png)

Nous devons **demander un certificat**. Sur votre Mac, allez dans « Accès aux trousseaux » -> « Assistant de certificat » -> « Demander un certificat à une autorité de certification ».

![Image](https://cdn-media-1.freecodecamp.org/images/1*rhTf5N0TL1AmKoXcWbhfoQ.png)

Remplissez toutes les informations nécessaires — votre email et votre nom commun — et enregistrez-le sur le disque.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ytVFGho1inBYnv2pYYLLbA.png)

Dans la console Apple, passez à l'étape suivante et **téléchargez** votre demande de certificat.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Qlz9edFubew4V3ozdt2X7A.png)

À l'étape suivante, votre certificat devrait être créé et vous pouvez le télécharger. **Vous en aurez besoin plus tard.**

![Image](https://cdn-media-1.freecodecamp.org/images/1*n5YZm8E6QYxNCDb9Ns7tyQ.png)

Maintenant, nous devons **créer une clé de service** pour activer les notifications push Apple. Sous « Clés », sélectionnez « Toutes ». Choisissez le nom de votre clé. Activez le « service de notifications push Apple (APNs) ».

![Image](https://cdn-media-1.freecodecamp.org/images/1*8lXVFTpEjwrApP2FArRaew.png)

Cliquez sur « Continuer » et confirmez votre clé. **Ne partagez jamais de telles données avec d'autres.** Vous pouvez maintenant télécharger votre clé.

![Image](https://cdn-media-1.freecodecamp.org/images/1*S_gRFhnecm29gSTaSWpfiA.png)

Maintenant, nous devons retourner à Firebase.

Dans Firebase, ouvrez votre application iOS et naviguez jusqu'à « Cloud Messaging ».

![Image](https://cdn-media-1.freecodecamp.org/images/1*10JoxYxq7LPUNv_magHS9A.png)

Nous devons **télécharger** notre clé d'authentification APN que nous avons générée il y a un moment. Cliquez sur « Télécharger ».

![Image](https://cdn-media-1.freecodecamp.org/images/1*jZtNNpy7gTjsv4tjZfsy9A.png)

Fournissez toutes les informations et téléchargez la clé.

Tout d'abord, téléchargez votre fichier « .p8 », téléchargé depuis la console Apple précédemment. Entrez votre ID de clé. Vous pouvez obtenir le préfixe de l'ID de l'application depuis la console Apple dans « Identifiants »->« ID d'application »->« Votre application »->« Préfixe ».

![Image](https://cdn-media-1.freecodecamp.org/images/1*TKeh5ZvgKRN6MXZvw7e0qw.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*l7g5BPKU9GvG0c9RJFWTUA.png)
_Télécharger le fichier p8 et obtenir keyID et le préfixe ID_

C'est tout. Des larmes de joie coulent sur mon visage.

Nous pouvons tester les notifications push sur iOS. N'oublions pas que nous devons utiliser un appareil réel.

### 6. Test des notifications push sur iOS

Tout d'abord, nous devons construire nos applications, alors exécutons : `ionic cordova build ios`

Dans Xcode, vous pouvez exécuter votre application sur un appareil connecté par USB à votre ordinateur.

![Image](https://cdn-media-1.freecodecamp.org/images/1*f4NOHT2xCJPgd2SXCXl-EA.png)
_Choisissez votre appareil_

Attendons que tout soit lancé. Nous pouvons maintenant répéter les étapes pour envoyer des notifications push depuis la [**Section 4**](https://medium.com/p/ad87cc92394e#0d9c), car c'est la même chose que sur Android.

N'oubliez pas que **vous devez utiliser un nouveau token** maintenant, qui a été généré pour votre appareil iOS. Allez dans les bases de données, obtenez un nouveau token, et envoyez une notification push. Votre résultat devrait ressembler à ceci.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZOE5hMQpOWxUIfE9zjDyfg.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*zBEkbPOB6EEurPt5j3qzrw.png)

J'espère que vous avez réussi à configurer vos notifications push. Cela prend du temps et de la patience pour tout faire correctement, mais le résultat et les avantages sont incroyables.

Si vous aimez mon tutoriel et que vous êtes intéressé par plus, vous pouvez consulter mon cours sur Udemy : [**Ionic 4 Crash Course with Heartstone API and Angular.**](http://bit.ly/2Ne2PhK)

Pour un projet complet, voir [mon dépôt Github](https://github.com/Jerga99/heartStoneLib).

Bon codage !

Filip