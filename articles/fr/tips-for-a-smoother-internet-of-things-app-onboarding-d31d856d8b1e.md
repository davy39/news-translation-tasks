---
title: Conseils pour une intégration plus fluide des applications de l'Internet des
  objets
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-10T14:26:27.000Z'
originalURL: https://freecodecamp.org/news/tips-for-a-smoother-internet-of-things-app-onboarding-d31d856d8b1e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*DRosbUtK79XSLJvXDcCXUA.jpeg
tags:
- name: Design
  slug: design
- name: iot
  slug: iot
- name: mobile app development
  slug: mobile-app-development
- name: 'tech '
  slug: tech
- name: UX
  slug: ux
seo_title: Conseils pour une intégration plus fluide des applications de l'Internet
  des objets
seo_desc: 'By Sofia Coppol

  Onboarding is a critical phase in a user’s journey with your app. It’s primarily
  the first contact point and thus is necessary for making a great first impression.
  The simpler the onboarding is for an app, the easier it is for users t...'
---

Par Sofia Coppol

L'intégration est une phase critique dans le parcours d'un utilisateur avec votre application. C'est principalement le premier point de contact et il est donc nécessaire de faire une excellente première impression. Plus l'intégration est simple pour une application, plus il est facile pour les utilisateurs de l'accepter et de l'utiliser. C'est la bonne intégration qui met les utilisateurs en action.

Mais pour un développeur, il n'a jamais été facile de développer un plan d'intégration qui engage les utilisateurs dès qu'ils ouvrent une application pour la première fois. Les développeurs font face à des défis uniques pour faire démarrer les utilisateurs avec leurs applications, sans qu'ils se sentent submergés.

Une bonne intégration contribue toujours à la réussite ou à l'échec d'une application. Une application est considérée comme réussie lorsqu'elle est activement utilisée. Selon les données de mai 2016 d'une firme d'analyse Localytics, une application sur quatre est désinstallée juste après une seule utilisation.

Dans cet article, je vais présenter mes meilleurs conseils pour aider les développeurs d'applications de l'Internet des objets (IoT) à élaborer un plan d'intégration parfait pour leur application. Mais d'abord, nous allons examiner les principaux défis de l'intégration des applications.

#### Défis de l'intégration des applications

Une application IoT est toujours liée à un produit physique. Cela ajoute un nouvel ensemble de difficultés pour les utilisateurs qui intègrent une nouvelle application ainsi qu'un produit qui interagira avec l'application. Les développeurs doivent identifier tous ces points de frustration qui causent de la frustration chez les utilisateurs.

* Applications difficiles à ouvrir ou laissant une empreinte excessive
* Instructions longues qui nécessitent que les utilisateurs apprennent beaucoup avant d'utiliser un produit
* Synchronisation problématique de l'application avec l'appareil IoT nécessitant que les utilisateurs suivent plusieurs étapes

Parce qu'une application IoT combine les défis liés à l'application elle-même et à l'appareil IoT avec lequel l'application interagit, il est important pour les développeurs d'applications IoT de former un plan d'intégration solide, de la configuration initiale aux tutoriels en passant par la rétention des utilisateurs.

Voici donc une liste de choses que vous devez faire pour avoir une expérience d'intégration fluide :

#### Mettre les instructions de téléchargement de l'application dans l'emballage du produit

En ce qui concerne une application IoT, elle sera toujours utilisée comme un produit secondaire par rapport à l'appareil physique réel que le consommateur achète. L'application n'est qu'une interface pour interagir avec le produit IoT. Assurez-vous d'avoir fourni des instructions simples sur la manière dont les consommateurs accéderont à l'application et la téléchargeront sur leurs appareils mobiles. Vous pouvez inclure un lien raccourci ou simple ou un code QR sur l'emballage du produit. Le lien ou le code QR doit diriger les consommateurs vers une page de destination.

![Image](https://cdn-media-1.freecodecamp.org/images/1*jEQ14szeCHrM5n9zmE5VyQ.png)

Une page de destination d'application doit détecter automatiquement le type d'appareil du consommateur et le rediriger vers le magasin d'applications approprié.

De nombreux fournisseurs de produits exécutent un serveur SMS qui nécessite que les utilisateurs envoient un message SMS, puis un lien de téléchargement de l'application leur est envoyé.

Vous pouvez choisir l'une des méthodes ci-dessus, un lien raccourci/simple, un code QR ou une demande SMS.

#### **Simplifiez la connexion avec les connexions sociales**

JanRain, un fournisseur de logiciels de gestion de profils et d'identités clients, affirme que [92 % des utilisateurs](https://www.intercom.com/blog/strategies-for-onboarding-new-users/) quitteront un site web s'ils sont invités à suivre un long processus lors de la connexion ou de la récupération des identifiants.

Ce comportement des utilisateurs a créé le terme connu sous le nom de fatigue de compte. Il met les utilisateurs sous la pression de se souvenir des noms d'utilisateur et des mots de passe pour leurs comptes. Sans doute, les utilisateurs se souviennent encore des identifiants de quelques-uns de leurs services les plus utilisés, comme Gmail et Facebook.

Les utilisateurs ne peuvent pas se souvenir de tous leurs noms d'utilisateur et mots de passe pour tous leurs comptes en ligne. Et cela les empêche de s'engager facilement avec un produit en ligne. Cette situation peut être évitée en permettant aux utilisateurs de se connecter à leurs comptes en utilisant leurs profils de réseaux sociaux, comme Facebook, Twitter ou Gmail.

#### **Mettez en avant les avantages du produit IoT et de l'application**

Le produit doit parler des avantages et fonctionnalités principaux du produit IoT et de la manière dont l'application peut être utilisée pour gérer facilement l'appareil et tirer parti de ces avantages.

![Image](https://cdn-media-1.freecodecamp.org/images/1*oAnYtOpxScZv07QzLbEZOw.png)

Cette approche peut être appliquée aux tutoriels pas à pas, qui mettent en avant chacune des fonctionnalités individuellement.

Voici ce que vous devez considérer lors de la création d'un tutoriel pas à pas :

* **Ajouter un diaporama** - Lorsque vous ajoutez un tutoriel pour informer les utilisateurs sur les avantages et les fonctionnalités, gardez-le simple et bref.
* **Ajouter un bouton de saut** - pour les utilisateurs qui ont déjà téléchargé et utilisé l'application auparavant.
* **Utiliser des flèches pour pointer vers les fonctionnalités** - De nombreux développeurs utilisent des flèches pour informer les utilisateurs de l'emplacement des fonctionnalités. Les flèches avec une ligne de détail informent de manière interactive les utilisateurs sur ce qui se trouve où. Lorsque vous cliquez sur le titre qui décrit la fonctionnalité, un nouveau titre apparaît qui informe l'utilisateur sur la deuxième fonctionnalité/fonction de l'application.

#### **Inclure des tutoriels vidéo**

Ajouter un tutoriel vidéo est l'une des meilleures façons d'éduquer les utilisateurs sur votre application. Inclure des tutoriels vidéo dans votre application aidera les utilisateurs à configurer facilement leur produit IoT et les guidera sur la manière dont l'application interagit avec celui-ci.

Par exemple, regardez comment Nest présente leur thermostat intelligent dans cette vidéo.

#### **Montrer la progression du tutoriel**

Les consommateurs peuvent s'ennuyer à lire un tutoriel s'ils ne connaissent pas leur progression et combien ils ont complété. Vous pouvez éviter cela en leur fournissant un indicateur de la progression du tutoriel afin que les utilisateurs soient motivés à le compléter, ce qui entraîne une intégration plus fluide.

#### **Faciliter l'accès au support client**

Même après avoir accès à des manuels et des tutoriels, les consommateurs peuvent avoir besoin de contacter le support client. Vous pouvez rendre votre support client très réactif en ajoutant de la documentation à l'application et en fournissant un accès facile au support intégré. Vous pouvez également ajouter un lien qui redirige les utilisateurs vers une section de support mobile de votre site web.

Vous pouvez également inclure un chat intégré qui dirige directement les clients vers les représentants du service client. Lorsque les utilisateurs ont un moyen facile d'accéder aux services de support client via l'application elle-même, il est plus probable qu'ils demandent de l'aide lorsqu'ils rencontrent un problème et cela augmente la satisfaction et l'engagement globaux avec l'application.

#### **Gamifiez votre application**

Les gens adorent débloquer des réalisations ou avoir accès à une interface interactive. Les applications de jeu le font depuis longtemps, ce qui augmente l'engagement de leurs utilisateurs. Le même concept de gamification peut être ajouté aux applications IoT, gardant les utilisateurs engagés avec l'application et les encourageant à l'utiliser plus fréquemment.

#### **Comptez sur les notifications intégrées et push**

Les [applications IoT](http://www.rapidsofttechnologies.com/ioT.php) sont de bons candidats pour les notifications intégrées et push. Vous pouvez utiliser des notifications pour informer les utilisateurs de compléter leurs profils ou leur rappeler qu'ils n'ont pas utilisé l'application depuis un certain temps. Les notifications peuvent être déclenchées en fonction de la progression d'une tâche ou d'une réalisation que l'utilisateur est sur le point d'atteindre. Cela aide également les utilisateurs à voir le statut et les actions associés à l'appareil IoT connecté.

#### Conclusion

Lors de la conception d'une application en gardant à l'esprit les conseils mentionnés ci-dessus, une équipe de développement réussit à créer une expérience d'intégration géniale qui engage instantanément les utilisateurs avec l'application de l'appareil IoT. Bien que tous les conseils ci-dessus ne soient pas applicables à chaque application IoT, chacun d'eux peut être essayé individuellement et leurs effets sur la rétention de l'application observés.

_Sofia est une experte en marketing numérique chez Rapidsoft Technologies, une [société de développement de logiciels offshore](http://www.rapidsofttechnologies.com/offshore-development-center.php) qui développe des logiciels pour les secteurs de l'éducation, de l'automatisation, de la construction et de la finance à travers le monde. Elle aime écrire sur les dernières tendances mobiles, les technologies, les startups et les entreprises._