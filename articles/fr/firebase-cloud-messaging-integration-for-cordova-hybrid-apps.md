---
title: Intégration de Firebase Cloud Messaging pour les applications hybrides Cordova
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-18T19:13:00.000Z'
originalURL: https://freecodecamp.org/news/firebase-cloud-messaging-integration-for-cordova-hybrid-apps
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9dc2740569d1a4ca397b.jpg
tags:
- name: Apps
  slug: apps-tag
- name: Cloud Computing
  slug: cloud-computing
- name: Firebase
  slug: firebase
seo_title: Intégration de Firebase Cloud Messaging pour les applications hybrides
  Cordova
seo_desc: 'By t1tan1um

  This is a basic straight forward walk through regarding how to implement push notification
  in Android as well as iOS using the cordova plugin for fcm and Google Firebase FCM
  from scratch. I will be using Ubuntu 16.04 LTS for this, but OS ...'
---

Par t1tan1um

Ce guide simple et direct explique comment implémenter les notifications push sur Android ainsi que sur iOS en utilisant le [plugin Cordova pour FCM](https://github.com/fechanique/cordova-plugin-fcm) et Google Firebase FCM à partir de zéro. J'utiliserai Ubuntu 16.04 LTS pour cela, mais le système d'exploitation utilisé pour le développement ne devrait pas avoir beaucoup d'importance.

## **Intégration de FCM pour les applications hybrides Cordova**

### **Implémentation Android**

Créez un dossier vide pushSample

```text
cd '/opt/lampp/htdocs'
mkdir pushSample
cd pushSample
cordova create pushSample
cd pushSample
cordova platform add android
cordova plugin add cordova-plugin-fcm
```

Lors de l'ajout du plugin FCM Cordova, une erreur s'affichera :

```text
Erreur : cordova-plugin-fcm : Vous avez installé la plateforme android mais le fichier 'google-services.json' n'a pas été trouvé dans le dossier racine de votre projet Cordova.
```

Note : Cela est dû au fait que nous n'avons pas encore ajouté le fichier google-services.json qui doit être créé dans les étapes suivantes.

Ensuite, ouvrez la [console Google Firebase](https://console.firebase.google.com/) et ajoutez un projet (c'est-à-dire créez un nouveau projet).

Une fois le projet créé, cliquez sur la section Notifications dans le panneau latéral gauche.

Maintenant, cliquez sur l'icône Android pour ajouter la prise en charge de la plateforme **Android** à notre projet.

Dans le formulaire popup suivant, remplissez les détails comme suit : **Nom du package Android :** Le nom ou l'ID du package est l'identifiant unique d'une application dans le Play Store. Notez que c'est une valeur très importante qui ne peut pas être modifiée pour une application une fois qu'elle est téléchargée sur le Play Store. Il sera en syntaxe de nom de domaine inversé : par exemple, hello.pushSample.com aura l'ID d'application : com.pushSample.hello. De plus, dans le fichier **config.xml** de votre projet Cordova, définissez le même ID d'application. Pour notre projet d'exemple, il se trouvera dans : pushSample/pushSample/config.xml. Par exemple, pour moi, le contenu de ce fichier est :

```xml
<?xml version='1.0' encoding='utf-8'?>
<widget id="io.cordova.hellocordova" version="1.0.0" xmlns="http://www.w3.org/ns/widgets" xmlns:cdv="http://cordova.apache.org/ns/1.0">
    <name>HelloCordova</name>
    <description>
        Une application Apache Cordova exemple qui répond à l'événement deviceready.
    </description>
    <author email="dev@cordova.apache.org" href="http://cordova.io">
        Équipe Apache Cordova
    </author>
    <content src="index.html" />
    <plugin name="cordova-plugin-whitelist" spec="1" />
    <access origin="*" />
    <allow-intent href="http://*/*" />
    <allow-intent href="https://*/*" />
    <allow-intent href="tel:*" />
    <allow-intent href="sms:*" />
    <allow-intent href="mailto:*" />
    <allow-intent href="geo:*" />
    <platform name="android">
        <allow-intent href="market:*" />
    </platform>
    <platform name="ios">
        <allow-intent href="itms:*" />
        <allow-intent href="itms-apps:*" />
    </platform>
</widget>
```

Notez la balise

```xml
<widget id="io.cordova.hellocordova" version="1.0.0" xmlns="http://www.w3.org/ns/widgets" xmlns:cdv="http://cordova.apache.org/ns/1.0">
```

Ici, l'attribut id est l'**id** du package qui sera par défaut **io.cordova.hellocordova**. Changez-le pour l'ID d'application que vous avez spécifié dans la console Firebase. J'utiliserai com.pushSample.hello.

Le champ suivant à remplir dans la popup de la console Firebase est :

**Surnom de l'application (facultatif) :** Cela peut être le même nom d'application qui est affiché dans le menu pour l'application. Cela peut également être modifié dans le config.xml. Par défaut, ce sera HelloCordova. Je vais le mettre à jour pour **PushSample**.

**Certificat de signature de débogage SHA-1 (facultatif) :** Cela est facultatif, veuillez le laisser vide.

Ensuite, cliquez sur **Enregistrer l'application**.

L'étape suivante consiste à télécharger le fichier **google services json**.

![télécharger google services json](https://preview.ibb.co/nEjbwv/1_Wje_TClf8o9z_Dxw3_W_wkpw.png)

Cliquez sur le bouton **Télécharger google-services.json**, ce qui devrait télécharger le fichier sur votre PC.

Une fois que vous avez le fichier, collez-le dans le dossier racine de votre projet Cordova. Dans mon cas :

```text
/opt/lampp/htdocs/pushSample/pushSample
```

Ensuite, construisez le projet.

```text
cordova build android
```

Après avoir ajouté le fichier google-services.json, il devrait se construire avec succès.

Ensuite, nous devons écrire le code côté client pour gérer les notifications push :

```js
FCMPlugin.getToken(function(token) {
    // ceci est le jeton FCM qui peut être utilisé
    // pour envoyer une notification à un appareil spécifique
    console.log(token);
    // FCMPlugin.onNotification( onNotificationCallback(data), successCallback(msg), errorCallback(err) )
    // Ici, vous définissez le comportement de votre application en fonction des données de notification.
    FCMPlugin.onNotification(function(data) {
        console.log(data);
        // data.wasTapped == true signifie en arrière-plan : La notification a été reçue dans la barre de l'appareil et a été appuyée par l'utilisateur.
        // data.wasTapped == false signifie au premier plan : La notification a été reçue au premier plan. Peut-être que l'utilisateur doit être notifié.
        // if (data.wasTapped) {
        //     // Notification reçue dans la barre de l'appareil et appuyée par l'utilisateur.
        //     alert(JSON.stringify(data));
        // } else {
        //     // Notification reçue au premier plan. Peut-être que l'utilisateur doit être notifié.
        //     alert(JSON.stringify(data));
        // }
    });
});
```

Le code appelle d'abord la fonction **getToken** pour obtenir un jeton FCM de Firebase, puis dans le callback, enregistre un autre callback **onNotification** pour gérer ce qui se passe lorsqu'une notification push est reçue.

La fonction **onNotification** a une valeur de données qui contient les données de notification. data.wasTapped indique si la notification est envoyée lorsque l'application est au premier plan ou en arrière-plan, afin que nous puissions définir une logique séparée pour chaque cas. Pour déclencher une notification push d'exemple, cliquez sur la section Notification dans le panneau latéral gauche. Cela devrait maintenant vous montrer le compositeur de notifications Firebase, affichant la liste des notifications passées envoyées.

Au cas où vous n'auriez pas encore envoyé de notifications push, vous devriez voir un bouton **envoyer votre première notification**.

**Note :** Le compositeur de notifications ressemblera à ceci :

![envoyer votre première notification](https://preview.ibb.co/b4qc3a/1_s_W2_Ad_QJz_JEFjto6rz1_8r_A.png)

Notez que lors de l'envoi de notifications push en utilisant la console Firebase, vous devez sélectionner le nom de l'application **com.pushSample.hello** dans mon cas.

Pour envoyer les données spécifiques à l'application personnalisées, sélectionnez les options avancées -> Paires clé-valeur.

![options avancées](https://preview.ibb.co/ensbUF/1_qp9_Mz_XBZvn_PYawyo0_TQBRA.png)

L'objet de données dans le callback onNotification ressemblera à ceci :

```js
{myKey2: "valuefor2", myKey: "valuefor1", wasTapped: false}
```

Notez également que lors de l'envoi de notifications push en utilisant les API REST depuis votre serveur d'application au lieu du compositeur de notifications Firebase, vous devez utiliser la syntaxe suivante :

```js
// POST : https://fcm.googleapis.com/fcm/send
// EN-TÊTE : Content-Type : application/json
// EN-TÊTE : Authorization : key=AIzaSy*******************
{
  "notification": {
    "title": "Titre de la notification",
    "body": "Corps de la notification",
    "sound": "default",
    "click_action": "FCM_PLUGIN_ACTIVITY",
    "icon": "fcm_push_icon"
  },
  "data": {
    "param1": "value1",
    "param2": "value2"
  },
  "to": "/topics/topicExample",
  "priority": "high",
  "restricted_package_name": ""
}
// sound : champ facultatif si vous voulez un son avec la notification
// click_action : doit être présent avec la valeur spécifiée pour Android
// icon : nom de la ressource d'icône blanche pour Android >5.0
// data : mettez n'importe quel "param":"value" et récupérez-les dans le callback de notification JavaScript
// to : jeton de l'appareil ou /topic/topicExample
// priority : doit être défini sur "high" pour livrer les notifications sur les applications iOS fermées
// restricted_package_name : champ facultatif si vous voulez envoyer uniquement à un package d'application restreint (par exemple : com.myapp.test)
```

**Note : le champ "click_action":"FCM_PLUGIN_ACTIVITY"** est très important car ne pas le mentionner n'exécutera pas le callback onNotification en mode premier plan.

![terminé avec l'implémentation Android](https://image.ibb.co/gRS1UF/0_QIzc_JZH9_Nqzpjygg.jpg)

### **Implémentation iOS**

Pour l'implémentation iOS, nous aurons besoin des éléments suivants à générer dans la [page du développeur Apple](https://developer.apple.com/). J'utilise Xcode 8.3.

ID d'application : com.example.app
Clé d'authentification Apple Push Notification (APNs Auth Key)
Profil de provisionnement de développement avec les notifications push activées.
Certificats APNs

De plus, la [documentation Firebase pour les notifications push](https://firebase.google.com/docs/cloud-messaging/ios/client) est un excellent point de départ approfondi.

Note : Vous ne pouvez pas exécuter de notifications push dans le simulateur, vous aurez besoin d'un appareil réel.

Commençons.

Tout d'abord, connectez-vous à la console des développeurs Firebase et sélectionnez un projet existant ou créez un nouveau projet. Nous utiliserons le même projet pushSample. Dans l'aperçu du projet, ajoutez une autre application avec iOS comme plateforme. Dans la popup qui apparaît, entrez les détails suivants :

* Étape 1 **Bundle ID :** il s'agit de l'identifiant unique utilisé pour identifier une application dans l'App Store d'Apple. Cela doit être identique au Bundle ID que vous spécifierez dans le fichier config.xml du projet Cordova ou dans la section Bundle ID dans Xcode. Nous utiliserons **com.pushSample.hello**
**Nom de l'application :** Il s'agit du surnom de l'identifiant optionnel. Nous utiliserons le même nom qui s'affichera dans le menu de l'application iOS, qui est PushSample.
**ID de l'App Store :** Laissez ce champ vide.

Une fois que vous cliquez sur « Enregistrer l'application », l'étape 2 de l'application iOS apparaît.

* Étape 2 Ici, cliquez sur le bouton de téléchargement **Googleservice-info.plist** pour télécharger le fichier que nous utiliserons dans les étapes suivantes.

**Étape 3 et Étape 4** nous pouvons les ignorer car elles seront gérées en interne par le plugin FCM Cordova.

Une fois l'application iOS ajoutée à votre projet, cliquez sur l'icône d'engrenage à côté du libellé « Aperçu » dans le panneau latéral gauche et sélectionnez les paramètres du projet. (Voir l'image ci-dessous.) Cela devrait ouvrir par défaut l'onglet Général des paramètres de votre projet.

![Paramètres du projet](https://preview.ibb.co/ddcwwv/1_c_Pee_Xdmf76l_W0_YRr_I83_Log.png)

Ensuite, cliquez sur votre application iOS dans Vos applications -> Applications iOS. Dans les détails de l'application iOS, mettez à jour le **Préfixe de l'ID d'application**, dont la valeur se trouve dans le Centre des membres Apple sous l'onglet Adhésion.

Maintenant, basculez vers l'onglet **Messagerie Cloud** -> section de configuration de l'application iOS.

![messagerie cloud](https://preview.ibb.co/m2Ktbv/1_0p_Vvf_JGYb_TEUIhwr_DIek_Q.png)

Ici, comme discuté précédemment, téléchargez la clé d'authentification APNs que vous avez générée dans le centre des membres Apple. Ensuite, nous effectuons la configuration côté client de l'application. Créez un nouveau dossier sampleApp dans votre dossier de développement. Pour moi, c'est

```text
/Volumes/Development/
```

donc le nouveau dossier sera

```text
/Volumes/Development/pushSample
cd /Volumes/Development/pushSample
```

Créez un nouveau projet Cordova, **Note : Utilisez sudo si nécessaire**

```text
cordova create pushSample
cd pushSample
```

Maintenant, ajoutez la dernière plateforme iOS

```text
sudo cordova platform add ios
```

Maintenant, collez le fichier **Googleservice-info.plist** que nous avons téléchargé précédemment dans le dossier racine du projet Cordova. Pour moi, c'est

```text
/Volumes/Development/pushSample/pushSample
```

ajoutez le plugin FCM Cordova.

```text
cordova plugin add cordova-plugin-fcm
```

Mettez à jour l'ID d'application par défaut et le nom de l'application avec le Bundle ID que nous avons décidé précédemment lors de la configuration de la console Firebase et le nom de l'application.

```xml
<widget id="com.pushSample.hello" version="1.0.0" xmlns="http://www.w3.org/ns/widgets" xmlns:cdv="http://cordova.apache.org/ns/1.0">
    <name>PushSample</name>
```

À ce stade, le code exemple aura un fichier app.js, que vous pouvez modifier et ajouter les fonctions getToken et onNotification comme pour Android. Le code JavaScript est le même pour les deux plateformes.

Ensuite, exécutez la commande de construction Cordova

```text
sudo cordova build ios
```

Une fois la commande de construction Cordova réussie, ouvrez l'application dans Xcode. Pour cela, ouvrez le fichier xcode.proj, qui se trouvera dans

```text
votre_projet_cordova/platforms/ios/nom_de_l_application.xcodeproj
```

pour moi, c'est

```text
/Volumes/Development/pushSample/pushSample/platforms/ios/PushSample.xcodeproj
```

![Projet Xcode](https://preview.ibb.co/hePLOa/1_Xe_Kh4_VXU_o_BQ05_UGRa_B6_A.png)

Ensuite, activez les notifications push dans l'onglet Capacités du projet.

Connectez un appareil réel et exécutez l'application.

Maintenant, déclenchez la notification push à partir du compositeur de notifications Firebase et tout devrait fonctionner...

![steve heureux](https://image.ibb.co/jz8VOa/1vnhjv.jpg)