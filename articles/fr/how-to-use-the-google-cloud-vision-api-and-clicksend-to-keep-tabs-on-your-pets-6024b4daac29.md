---
title: Comment utiliser l'API Google Cloud Vision et ClickSend pour surveiller vos
  animaux de compagnie
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-06T16:17:07.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-the-google-cloud-vision-api-and-clicksend-to-keep-tabs-on-your-pets-6024b4daac29
coverImage: https://cdn-media-1.freecodecamp.org/images/1*4bblfUcScLKK4bWm3_FE0A.png
tags:
- name: Google
  slug: google
- name: image recognition
  slug: image-recognition
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment utiliser l'API Google Cloud Vision et ClickSend pour surveiller
  vos animaux de compagnie
seo_desc: 'By Namratha Subramanya

  Just like people, dogs are scared by all kinds of things. Most often, it’s a result
  of having a negative experience or not being handled when their natural fears surface.
  In this article, we’ll create a way to make sure your do...'
---

Par Namratha Subramanya

Tout comme les humains, les chiens sont effrayés par toutes sortes de choses. Le plus souvent, cela résulte d'une expérience négative ou du fait de ne pas avoir été rassurés lorsque leurs peurs naturelles surgissent. Dans cet article, nous allons créer un moyen de s'assurer que votre chien est en sécurité lorsque vous êtes absent.

Vous pouvez attacher une caméra au collier de votre chien pour capturer des images, et utiliser l'API Vision pour détecter et reconnaître les images.

Supposons que votre chien ait peur des chats, et que vous souhaitiez vous assurer que votre petit ami poilu est en sécurité loin des chats pendant qu'il joue dans le jardin en votre absence. Vous pourriez construire une application où vous recevriez des alertes SMS sur votre appareil lorsque des chats sont reconnus par l'API Cloud Vision.

Dans ce tutoriel, vous apprendrez à reconnaître une image en utilisant l'API Google Cloud Vision et à alerter l'utilisateur avec un SMS en utilisant l'API ClickSend. PubNub forme le squelette de l'application et interconnecte les fonctionnalités.

[**Le dépôt GitHub complet du projet est disponible ici.**](https://github.com/namrathasubramanya/PubNub-VisionAPI-ClickSend)

### Commençons à construire

Supposons que la webcam de votre ordinateur portable est la caméra fixée au collier de votre chien. Voici le code qui ouvre votre webcam et prend des photos pour vous. Vous pourriez définir un intervalle de temps pour capturer des images fréquemment. Ces images vont dans un élément canvas et peuvent être sauvegardées sur votre appareil. Vous pouvez trouver le code pour cliquer et sauvegarder les images ci-dessous.

### API Cloud Vision

L'API Google Cloud Vision permet aux développeurs de comprendre le contenu d'une image grâce à ses puissants modèles de machine learning. Pour commencer à implémenter l'API Vision, vous devez créer un nouveau projet [ici](https://console.cloud.google.com/cloud-resource-manager?_ga=2.203919383.-603090119.1528760418). Avant de créer un nouveau projet, vous devez configurer votre compte de facturation. Après cela, vous devez activer l'API Vision.

Pour plus de détails, consultez ce guide de démarrage rapide [lien](https://cloud.google.com/vision/docs/quickstart).

Exécutez la commande suivante dans votre terminal :

```
pip install --upgrade google-cloud-vision
```

Pour exécuter la bibliothèque cliente, vous devez d'abord configurer l'authentification en créant un compte de service [ici](https://console.cloud.google.com/apis/credentials) et en définissant une variable d'environnement.

* Dans la liste déroulante **Compte de service**, sélectionnez **Nouveau compte de service**.
* Entrez un nom dans le champ **Nom du compte de service**.
* Ne sélectionnez pas de valeur dans la liste déroulante **Rôle**. Aucun rôle n'est requis pour accéder à ce service.
* Cliquez sur **Créer**. Une note apparaît, avertissant que ce compte de service n'a aucun rôle.
* Cliquez sur **Créer sans rôle**. Un fichier JSON contenant votre clé sera téléchargé sur votre ordinateur.

Maintenant, définissez la variable d'environnement `GOOGLE_APPLICATION_CREDENTIALS` sur le chemin du fichier JSON contenant votre clé de compte de service. Cela peut être fait comme suit :

Pour Linux/Mac OS :

```
export GOOGLE_APPLICATION_CREDENTIALS="[PATH]"
```

Pour Windows :

```
set GOOGLE_APPLICATION_CREDENTIALS=[PATH]
```

Maintenant, vous êtes prêt à exécuter le code qui reconnaît vos images. Voici le code Python qui prend les captures d'écran du répertoire où vous les avez sauvegardées (le mien est Téléchargements) et répond avec des libellés.

Le résultat de la reconnaissance d'image est envoyé à l'utilisateur en utilisant [PubNub Real-time Messaging](https://www.pubnub.com/docs/tutorials/pubnub-publish-subscribe/?utm_source=Syndication&utm_medium=Medium&utm_campaign=SYN-CY18-Q2-Medium-June-28). Vous devez simplement abonner votre appareil à un canal, par exemple, `alert_notify` auquel l'API Vision envoie les résultats de la reconnaissance d'image.

![Image](https://cdn-media-1.freecodecamp.org/images/0*u-0bRBK1pv8V8YsA.jpg)

### Alerte de notification Web utilisant PubNub

Vous devrez maintenant initialiser vos clés PubNub. [Inscrivez-vous pour un compte PubNub](https://www.pubnub.com/docs/tutorials/pubnub-publish-subscribe/?utm_source=Syndication&utm_medium=Medium&utm_campaign=SYN-CY18-Q2-Medium-June-28) et créez un projet dans le [Tableau de bord d'administration](https://admin.pubnub.com/#/login/?utm_source=Syndication&utm_medium=Medium&utm_campaign=SYN-CY18-Q2-Medium-June-28).

Maintenant, vous pouvez publier le message d'alerte dans votre code Python que vous pouvez envoyer en tant que notification push web à votre appareil. L'appareil, à son tour, s'abonne au canal `alert_notify` et reçoit le message d'alerte de votre caméra.

Vous pouvez concevoir la notification push web en utilisant l'[API de notification](https://developer.mozilla.org/en-US/docs/Web/API/notification) en HTML5.

### API ClickSend

L'[API ClickSend](https://developers.clicksend.com/) permet aux développeurs d'intégrer des SMS, des appels vocaux, des fax, des posts ou des emails dans leurs applications. Vous pourriez envoyer un SMS à votre appareil mobile ainsi que des notifications push web en utilisant PubNub. L'API ClickSend est bien documentée pour les développeurs.

Vous pouvez utiliser l'[API HTTP](https://clicksendhttpapiv2.docs.apiary.io/#) de ClickSend. Chaque fois que l'API Vision reconnaît une image, vous recevez un SMS sur votre appareil.

### Félicitations !

Maintenant que vous avez configuré l'API Cloud Vision et l'API ClickSend pour communiquer entre elles via le Publish-Subscribe de PubNub, vous serez en mesure de recevoir des notifications web et des alertes SMS envoyées à votre appareil chaque fois que votre caméra capture une image d'un chat. Sans aucun doute, c'est un excellent point de départ pour construire des applications utilisant différentes API et les connecter via PubNub.

_Publié à l'origine sur [www.pubnub.com](https://www.pubnub.com/blog/image-recognition-using-vision-api-and/?utm_source=Syndication&utm_medium=Medium&utm_campaign=SYN-CY18-Q2-Medium-June-28)._