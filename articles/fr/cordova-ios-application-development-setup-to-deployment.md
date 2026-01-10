---
title: Développement d'applications Cordova iOS expliqué de l'installation au déploiement
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-01T20:01:00.000Z'
originalURL: https://freecodecamp.org/news/cordova-ios-application-development-setup-to-deployment
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e58740569d1a4ca3c99.jpg
tags:
- name: app development
  slug: app-development
- name: iOS
  slug: ios
seo_title: Développement d'applications Cordova iOS expliqué de l'installation au
  déploiement
seo_desc: 'Hybrid Application development for Android is a breeze, be it for development
  or production configuration. But I personally find Cordova iOS setup, development,
  and deployment a bit complicated.

  Most of the Hybrid Application Developers who are in th...'
---

![iphone_1737513_1920](https://image.ibb.co/iKCSuQ/Xz_J197k8_QI32.jpg)

Le développement d'applications hybrides pour Android est un jeu d'enfant, que ce soit pour la configuration de développement ou de production. Mais personnellement, je trouve que la configuration, le développement et le déploiement de Cordova iOS sont un peu compliqués.

La plupart des développeurs d'applications hybrides qui sont en phase d'apprentissage ne peuvent pas explorer le processus de développement d'applications iOS hybrides simplement parce qu'ils ne possèdent pas de Mac. Et le développement d'applications iOS nécessite le SDK iOS et XCode (contrairement au SDK Android qui fonctionne sur n'importe quel système d'exploitation de bureau).

Par conséquent, l'objectif de ce guide est de montrer le flux de travail de base du développement d'applications iOS hybrides sur un Mac. Ainsi, les développeurs peuvent voir comment cela se fait même s'ils ne peuvent pas développer les applications.

## **Création d'un projet Cordova**

Commencez par ouvrir le terminal et créer un nouveau projet Cordova (utilisez sudo uniquement si vous avez des problèmes de permission, c'est-à-dire des erreurs EACCESS) :

```text
sudo cordova create iosdemo
cd iosdemo
sudo cordova platform add ios
```

Au moment de la rédaction de ce guide, la version de la plateforme Cordova iOS est 4.3.1.

Nous ne modifierons aucun code source de l'application – plutôt, nous continuerons simplement avec le code d'exemple par défaut qui est ajouté automatiquement par Cordova lorsque nous exécutons la commande create. Cependant, il est supposé que nous ajouterons des plugins et modifierons le code dans le dossier `www` pendant le flux de développement normal.

L'étape suivante consiste à exécuter la commande de construction Cordova. Cela convertira notre code d'application en un fichier .xcodeproj que nous utiliserons ensuite.

```text
sudo cordova build ios
```

Le fichier de projet Xcode généré sera ici :

```text
[Votre Dossier d'Application]/platforms/ios/[Nom de votre Application].xcodeproj
```

Dans le cas d'Android, la signature du code est effectuée à l'aide du fichier Keystore qui est au format .jks. Cependant, dans iOS, il est nécessaire que vous ayez un compte développeur Apple pour distribuer des applications iOS. Cela permet de générer les _Certificats_ et les _Profils de provisionnement_ nécessaires pour distribuer l'application.

Pour les informations sur les prix et autres concernant un compte développeur, consultez [cette page](https://developer.apple.com/support/purchase-activation/).

## **Création de certificats de développement**

Une fois que vous avez le compte prêt, nous pouvons continuer et nous connecter à votre [compte développeur Apple](https://developer.apple.com/account/).

L'écran du tableau de bord devrait ressembler à ceci :

![Ouverture du projet dans Xcode](https://image.ibb.co/j0d8zQ/Clipboard_image_2017_09_18_11_35_58.png)

Cliquez sur `Certificats, Identifiants et Profils`. Cela devrait vous amener à l'écran suivant, qui par défaut affiche les certificats émis depuis votre compte :

![Certificats, Identifiants et Profils](https://image.ibb.co/fk8mm5/1.png)

Les certificats iOS sont principalement de deux types : Développement ou Distribution. Cliquez sur le bouton Plus (+) dans le coin supérieur droit de la liste, ce qui ouvrira la page suivante :

![Ajouter un certificat iOS](https://image.ibb.co/dksXtk/2.png)

Commençons par créer un profil de développement. Sélectionnez _Développement d'applications iOS_ et cliquez sur continuer.

Cela devrait vous amener à l'écran suivant, où il vous est demandé de créer et de télécharger un fichier de demande de signature de certificat ou CSR.

![Télécharger le fichier CSR](https://image.ibb.co/iwBE65/3.png)

Suivez les instructions à l'écran pour le générer, et continuez. Une fois le certificat prêt, téléchargez-le sur votre Mac et double-cliquez dessus. Cela l'ajoutera à l'accès au trousseau dans le Mac.

![Télécharger le certificat de développement](https://image.ibb.co/dJg6m5/4.png)

## **Création de certificats de distribution**

La création de certificats de distribution est similaire au processus de création de certificats de développement. Cependant, ici nous sélectionnons `App Store et Ad Hoc` dans la section `Production` de la page `Ajouter un certificat iOS` :

![Ajouter un certificat iOS](https://image.ibb.co/bEKFeQ/5.png)

## **Création de l'ID de l'application**

Sélectionnez `ID d'applications` dans la section `Identifiants`. Cela ouvrira la liste des ID d'applications existants. Cliquez ensuite sur le bouton Plus en haut à droite (+). Cela ouvrira la page _Inscrire les ID d'applications iOS_.

![Inscrire les ID d'applications iOS](https://image.ibb.co/iXTuOk/6.png)

Sélectionnez l'ID d'application explicite. La description de l'application peut être n'importe quel nom lié – c'est ce qui sera affiché dans la liste des ID d'applications contre l'ID d'application particulier.

Un ID d'application est une chaîne au format _AB11A1ABCD.com.mycompany.myapp_ où _AB11A1ABCD_ est le préfixe de l'ID d'application qui est par défaut l'ID de l'équipe et _com.mycompany.myapp_ est l'ID de bundle qui est unique pour chaque application.

Il est recommandé que l'ID de bundle soit une chaîne de style nom de domaine inversé. Par exemple, la société MYCOMPANY peut avoir deux applications (App1 et App2). Ainsi, l'URL HTTP pour chaque application est généralement app1.mycompany.com et app2.mycompany.com. Par conséquent, les ID de bundle pour chaque application seront com.mycompany.app1 et com.mycompany.app2.

Ensuite, sélectionnez les services dont vous avez besoin dans votre application, tels que les notifications push, Wallet, etc. Cliquez ensuite sur continuer et confirmez les détails et enfin enregistrez l'ID de l'application.

## **Ajout de dispositifs à votre compte développeur**

Sélectionnez `Tous` dans la section `Dispositifs`. Cela ouvrira la liste des dispositifs déjà ajoutés à votre compte développeur Apple. Seuls ces dispositifs sont autorisés à exécuter l'application pendant le développement.

Pour ajouter un nouveau dispositif, cliquez sur le bouton Plus en haut à droite (+). L'écran suivant sera affiché :

![écran d'ajout de dispositif](https://image.ibb.co/gTmW3k/8.png)

Ici, le nom peut être n'importe quel nom facilement compréhensible, par exemple iPhone 5s ABC Pvt Ltd. L'UDID du dispositif est l'ID unique associé à chaque dispositif Apple.

Pour trouver l'UDID d'un dispositif, suivez ces étapes :

1. Connectez le dispositif à votre Mac.
2. Ouvrez l'application Informations système située dans le dossier /Applications/Utilitaires.
3. Sélectionnez USB sous Matériel dans la colonne de gauche.
4. À droite, sélectionnez le dispositif connecté sous Arbre des dispositifs USB. L'ID du dispositif, ou « Numéro de série », apparaît ci-dessous.

Une fois que vous avez entré l'UDID du dispositif et le nom, cliquez sur continuer, puis confirmez les détails et enregistrez.

## **Création d'un profil de provisionnement de développement**

Pour créer un profil de provisionnement de développement, cliquez sur Profils de provisionnement -> Tous. Cela devrait afficher tous les profils, de développement ainsi que de distribution. Cliquez ensuite sur le bouton Plus en haut à droite (+). Cela devrait afficher la page suivante :

![Création d'un profil de provisionnement de développement](https://image.ibb.co/dk3KOk/7.png)

Ici, sélectionnez `Développement d'applications iOS` et cliquez sur continuer. Dans la liste déroulante qui s'affiche, sélectionnez l'ID d'application que nous avons créé précédemment et continuez.

Ensuite, une liste de certificats est affichée à partir de laquelle nous pouvons en sélectionner un ou plusieurs. Ce sont des certificats de développement et non de distribution. Le profil de provisionnement généré sera lié à ces certificats.

Lorsque vous cliquez sur Continuer, une liste de dispositifs est affichée. Sélectionnez un, plusieurs ou tous. Seuls les dispositifs sélectionnés seront autorisés à exécuter l'application en utilisant ce profil de provisionnement.

Ensuite, après avoir cliqué sur continuer, entrez le nom pour le profil de provisionnement, et téléchargez le fichier .mobileprovision généré.

**Notes** : c'est le même processus pour créer votre profil de provisionnement de distribution Adhoc. C'est aussi très similaire pour créer votre profil de provisionnement de distribution AppStore, sauf que pour celui-ci nous ne sélectionnons pas de dispositifs, car l'application sera disponible publiquement via l'AppStore.

Maintenant que nous avons tout ce dont nous avons besoin, nous pouvons continuer à générer l'ipa réel en utilisant Xcode.

_La commande de construction Cordova convertit notre code d'application en un projet xcode. En utilisant Xcode, nous créons un fichier .ipa qui est l'application réelle à installer._

Avant de continuer, double-cliquez sur les deux certificats pour les ajouter à votre trousseau.

## **Continuation dans Xcode**

Ensuite, double-cliquez sur le fichier .xcodeproj qui devrait l'ouvrir dans Xcode. (Veuillez utiliser la dernière version de Xcode – j'ai utilisé Xcode 8.3.2.)

![Ouverture du projet dans Xcode](https://image.ibb.co/mPdGKQ/Screen_Shot_2017_09_18_at_11_06_55_AM.png)

L'écran Xcode devrait ressembler à quelque chose comme ci-dessus.

Cliquez sur le nom de l'application dans le coin supérieur gauche de la fenêtre. Cela ouvrira la vue détaillée sur le côté droit.

![Paramètres du projet](https://image.ibb.co/fqb3ZQ/Screen_Shot_2017_09_18_at_5_07_53_PM.png)

Ensuite, cliquez sur Cibles-> Nom de l'application :

![cibles](https://image.ibb.co/i0znTk/Screen_Shot_2017_09_18_at_5_11_28_PM.png)

Cela affichera l'onglet de détails suivant :

![détails de la cible](https://image.ibb.co/ksBj8k/Screen_Shot_2017_09_18_at_5_15_29_PM.png)

Cliquez sur général, ce qui devrait afficher ceci :

![détails généraux](https://image.ibb.co/k8KFEQ/Screen_Shot_2017_09_18_at_5_18_29_PM.png)

Décochez la case Gérer automatiquement la signature.

Cela devrait afficher l'erreur suivante, indiquant que AppNAme nécessite un profil de provisionnement :

![erreur de profil](https://image.ibb.co/mDq5EQ/Screen_Shot_2017_09_18_at_5_20_35_PM.png)

Ensuite, sous Signature (Debug), cliquez sur le menu déroulant Profil de provisionnement et sélectionnez l'option _importer le profil_. Dans la boîte de dialogue de sélection de fichier qui s'ouvre, accédez au chemin où le profil de provisionnement de développement est téléchargé, et sélectionnez-le. Il aura une extension _.mobileprovision_.

Après avoir sélectionné cela, l'erreur devrait disparaître, et il devrait afficher Équipe comme le nom de l'équipe dans votre compte développeur Apple et le nom du certificat de signature.

Faites la même chose pour la section Signature (Release) – mais dans la boîte de dialogue de sélection de fichier, sélectionnez le profil de distribution Ad Hoc.

Maintenant que les étapes de signature du code sont terminées, nous pouvons soit

* exécuter l'application directement sur le dispositif
* exécuter l'application sur un simulateur
* générer un fichier ipa pour la distribution
* télécharger l'application sur l'appstore

## **Exécution de l'application directement sur le dispositif**

Pour exécuter l'application sur un dispositif, connectez le dispositif au Mac via USB. Ensuite, dans le coin supérieur gauche dans la liste des dispositifs, sélectionnez le dispositif connecté, et cliquez sur le bouton exécuter ou lecture (bouton triangulaire noir) :

![exécuter le dispositif](https://image.ibb.co/k4xo15/Screen_Shot_2017_09_18_at_5_34_14_PM.png)

![exécuter le dispositif](https://image.ibb.co/hjzhuQ/Screen_Shot_2017_09_18_at_5_36_55_PM.png)

Le statut de construction sera affiché dans la barre d'état en haut de la fenêtre. Si tout se passe bien, l'application devrait être installée sur le dispositif, et elle devrait se charger automatiquement après un certain temps.

**Note** : les étapes sont les mêmes pour exécuter l'application sur un simulateur. Mais au lieu d'un dispositif réel, nous utilisons les simulateurs iPhone et iPad disponibles dans la liste des dispositifs.

## **Générer un fichier ipa pour la distribution**

Cette approche peut être utilisée si vous devez distribuer l'application à l'équipe de test, etc. Cependant, le dispositif utilisé par eux doit avoir un UDID présent dans le profil de provisionnement.

Dans le menu Xcode, sélectionnez `Produit` -> `Nettoyer`, puis `Produit` -> `Archiver`. L'organisateur d'archives apparaît et affiche la nouvelle archive.

![organisateur d'archives ios](https://image.ibb.co/iunfMG/6_ios_archive_organizer_2x.png)

Dans le panneau de droite, sélectionnez l'option Exporter et une liste d'options apparaîtra.

Pour distribuer votre application aux utilisateurs avec des dispositifs désignés, sélectionnez « Enregistrer pour le déploiement Ad Hoc ». L'application sera signée avec le certificat de distribution.

Pour distribuer votre application pour des tests internes, sélectionnez « Enregistrer pour le déploiement de développement ». L'application sera signée avec votre certificat de développement.

![organisateur d'archives ios exporter en ad hoc](https://image.ibb.co/jQJLMG/6_ios_createappstorepackage_1_2x.png)

Dans la boîte de dialogue qui apparaît, choisissez une équipe dans le menu contextuel et cliquez sur Choisir.

![exportation ios sélectionner l'équipe](https://image.ibb.co/gH2VMG/6_ios_export_choose_team_2x.png)

Ensuite, la boîte de dialogue de sélection du dispositif apparaît. Sélectionnez soit _Tous les dispositifs_ soit _dispositifs spécifiques_ et cliquez sur suivant.

Ensuite, la boîte de dialogue de révision est affichée. Ici, il affichera le certificat de signature et le profil de provisionnement utilisés pour générer la version. Passez en revue et cliquez sur suivant. Enfin, la boîte de dialogue d'enregistrement du fichier apparaît pour sélectionner l'emplacement dans le système de fichiers pour stocker le fichier d'application exporté.

L'application est exportée en tant que fichier .ipa.

Pour exécuter ce fichier sur le dispositif, il suffit de double-cliquer dessus, ce qui l'ouvrira dans iTunes.

Ensuite, connectez votre dispositif (cela devrait afficher une petite icône de dispositif dans le coin supérieur gauche de la fenêtre iTunes). En cliquant dessus, vous verrez le résumé du dispositif tel que les applications, la musique, etc. sur le dispositif. Sélectionnez l'onglet applications, et dans le volet de gauche, sélectionnez l'application à installer et cliquez sur installer. Attendez que le processus se termine et cliquez sur appliquer. Cela devrait installer le fichier ipa sur votre dispositif.

Pour déboguer l'application :

1. ouvrez Safari
2. ouvrez l'application sur le dispositif
3. dans la barre de menu Safari, sélectionnez `Développer --> Nom de votre dispositif --> Votre application`.

## **C'est tout pour aujourd'hui !**