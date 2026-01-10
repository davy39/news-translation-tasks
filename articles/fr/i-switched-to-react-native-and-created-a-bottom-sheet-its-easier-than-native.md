---
title: Pourquoi je suis passé à React Native pour créer une Bottom Sheet super facile
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-04-18T22:30:00.000Z'
originalURL: https://freecodecamp.org/news/i-switched-to-react-native-and-created-a-bottom-sheet-its-easier-than-native
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9b91740569d1a4ca2ca4.jpg
tags:
- name: Android
  slug: android
- name: android app development
  slug: android-app-development
- name: React Native
  slug: react-native
seo_title: Pourquoi je suis passé à React Native pour créer une Bottom Sheet super
  facile
seo_desc: "By Ayusch Jain\nI recently switched jobs, and one of my first tasks was\
  \ to create a bottom sheet in React Native. \nComing from a native Android development\
  \ background, I thought it was going to be as daunting as creating a bottom sheet\
  \ in native. But ..."
---

Par Ayusch Jain

J'ai récemment changé de travail, et l'une de mes premières tâches était de créer une bottom sheet en React Native. 

Venant d'un milieu de développement natif Android, je pensais que cela allait être aussi intimidant que de créer une bottom sheet en natif. Mais j'avais tort ! J'ai été tellement impressionné que j'ai décidé d'écrire un tutoriel simple sur la création d'une bottom sheet en React Native.

Une bottom sheet est un composant utile qui glisse depuis le bas de l'écran et contient souvent différentes options. Elle est très courante dans le design moderne et utilisée par des applications telles qu'Uber, Zomato, et bien d'autres.

Voici à quoi ressemblera le résultat final :

![Image](http://ayusch.com/wp-content/uploads/2020/03/tuxpi.com_.1585128093.jpg)
_Source : https://ayusch.com/_

Alors, voyons comment créer une bottom sheet en React Native.

## Installation

Tout d'abord, créez un nouveau projet en React Native. J'utilise expo-cli pour cela. Si vous ne connaissez pas expo-cli ou si vous débutez avec React Native, consultez [ce lien](https://reactnative.dev/docs/getting-started). 

J'ai nommé mon projet BottomSheetDemo.

Ensuite, nous devons installer react-native-modalbox. Cela nous offre de nombreuses capacités intégrées telles que des animations, des positions, des arrière-plans, etc.

> $ expo install react-native-modalbox@1.7.1

Note : N'oubliez pas d'installer la version 1.7.1. La dernière version a un bug où backdropPressToClose ne fonctionne pas.

## Création du Modal

Il est temps de créer notre modal. Supprimez le code fourni au début et ajoutez ce qui suit à votre fichier App.js :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/carbon.png)

Ceci est la structure de base de notre bottom sheet/modal. Nous allons simplement afficher un texte au centre du modal.

## Ajout d'Interaction

Nous avons besoin que la bottom sheet apparaisse lorsqu'un bouton est pressé. Ajoutons une interaction.

Je vais ajouter un bouton simple au milieu de l'écran :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/carbon--1-.png)

En cliquant sur ce bouton, nous devons afficher/masquer notre bottom sheet. Pour cela, nous allons maintenir un état en utilisant le hook useState de React.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/carbon--2-.png)

Notre modal a une prop nommée "isOpen" que nous pouvons basculer pour afficher/masquer notre bottom sheet. Pour l'afficher, nous allons simplement définir modalVisible à false et vice-versa.

Mais d'abord, séparons notre modal du reste du code car cela commence à devenir un peu désordonné. Je vais créer une fonction séparée qui retournera mon modal.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/carbon--3-.png)

Le code semble beaucoup plus propre maintenant. Mais notre bottom sheet ne ressemble toujours pas exactement à une bottom sheet. Nous devons ajouter un peu de style.

## Ajout de Style !

Créez une feuille de style et ajoutez les styles suivants :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/carbon--4-.png)

Voici à quoi ressemble le code final :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/carbon--5-.png)

Nous avons enfin créé notre bottom sheet en React Native. C'est si simple et beaucoup plus facile à créer qu'en natif Android. 

Je ne peux pas commenter iOS puisque je ne l'ai jamais essayé.

Alors, si vous êtes un développeur iOS ou avez de l'expérience dans la création d'une bottom sheet en iOS, faites-moi savoir quelle a été votre expérience.

Rejoignez l'espace de travail AndroidVille [SLACK](https://rebrand.ly/73lbl3) pour les développeurs mobiles où les gens partagent leurs apprentissages sur les dernières technologies, en particulier le développement Android, RxJava, Kotlin, Flutter, et le développement mobile en général.

[Cliquez sur ce lien pour rejoindre l'espace de travail. C'est absolument gratuit](https://rebrand.ly/73lbl3).

_Aimez ce que vous lisez ? N'oubliez pas de partager cet article sur [Facebook](https://www.facebook.com/AndroidVille), Whatsapp, et_ [_LinkedIn_](https://www.linkedin.com)_._

_Vous pouvez me suivre sur [LinkedIn](https://www.linkedin.com/in/ayuschjain), [Quora](https://www.quora.com/profile/Ayusch-Jain), [Twitter](https://twitter.com/ayuschjain), et [Instagram](https://www.instagram.com/androidville/) où je réponds aux questions liées au développement mobile, en particulier Android et Flutter._