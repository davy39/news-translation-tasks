---
title: Aperçu du modèle de conception MVVM en Swift
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-12T17:07:16.000Z'
originalURL: https://freecodecamp.org/news/an-overview-of-the-mvvm-design-pattern-in-swift-fb815ea5da40
coverImage: https://cdn-media-1.freecodecamp.org/images/1*eSFq7WQEopQBOjggm3MEwA.png
tags:
- name: Design
  slug: design
- name: iOS
  slug: ios
- name: General Programming
  slug: programming
- name: Swift
  slug: swift
- name: technology
  slug: technology
seo_title: Aperçu du modèle de conception MVVM en Swift
seo_desc: 'By Azhar

  This article assumes you are comfortable with the MVC pattern, which is the baseline
  design pattern adopted and recommended by Apple.


  What is MVVM?

  MVVM is a structural design pattern. Imagine that you have two views with a different
  layout...'
---

Par Azhar

Cet article suppose que vous êtes à l'aise avec le modèle MVC, qui est le modèle de conception de base adopté et recommandé par Apple.

![Image](https://cdn-media-1.freecodecamp.org/images/1*eSFq7WQEopQBOjggm3MEwA.png)

### Qu'est-ce que MVVM ?

MVVM est un modèle de conception structurel. Imaginez que vous avez deux vues avec des dispositions différentes qui doivent être remplies avec des données provenant de la même classe de modèle. MVVM vous permet d'utiliser des données d'une seule classe de modèle et de les représenter de différentes manières pour remplir une vue.

#### Modèles

Ils contiennent les données de l'application. Ce sont les structs et les classes que vous avez créées pour contenir les données que vous recevez d'une API REST ou d'une autre source de données.

#### Vues

Elles affichent les éléments de l'interface utilisateur à l'écran. Ce sont généralement des classes qui sous-classent UIView et utilisent UIKit.

#### Modèles de vue

Ces classes sont où vous prenez les informations des classes de modèle et les transformez en valeurs qui peuvent être affichées dans une vue particulière.

### Comment utiliser cela ?

Utilisez ce modèle pour transformer les données d'une classe de modèle en une représentation qui fonctionne pour une vue différente. Par exemple, vous pouvez utiliser un modèle de vue pour transformer une String en NSAttributedString ou une Date en une String formatée.

Ce modèle est similaire à MVC, ce qui explique peut-être pourquoi il est relativement simple de l'ajouter à une base de code MVC. Tout ce que vous avez à faire est d'ajouter vos classes de modèle de vue à la base de code existante et de les utiliser pour représenter les données comme vous en avez besoin. Cela minimise le rôle du View Controller, ce qui aide à soulager vos classes View Controller. Vous aussi pouvez éviter le problème du 'Massive View Controller'.

**_Avertissement_** : MVVM ne peut pas vous aider à éviter le problème du massive view controller à lui seul. Vous pouvez diversifier la charge d'une classe view controller en utilisant des modèles de conception en conjonction les uns avec les autres, comme le modèle de délégué, le modèle singleton, etc.

Voyons comment MVVM fonctionne en code.

Ouvrez Xcode et créez un nouveau projet Playground. Sélectionnez Single View sous l'onglet iOS pour commencer. Cliquez sur l'éditeur assistant (icône avec deux cercles qui s'intersectent) pour afficher la fenêtre Live View. Vous devriez voir ceci.

![Image](https://cdn-media-1.freecodecamp.org/images/1*rZ_OI7oHbdFRT8YLfwItTQ.png)

Vous pouvez supprimer la classe MyController. Nous allons configurer nos vues manuellement.

Prétendons que nous travaillons sur une application de magasin d'oiseaux. Commençons par créer une classe de modèle pour les oiseaux. Juste en dessous de l'accolade fermante de la classe MyViewController, ajoutez la classe suivante.

Chaque oiseau a un nom, un niveau de rareté et une image. Supposons que nous devons afficher ces propriétés dans une vue. La propriété de rareté est une énumération que nous ne pouvons pas afficher dans une vue sans une sorte de représentation utile pour un élément de vue à rendre. C'est le moment idéal pour créer un modèle de vue d'oiseau pour cette représentation. Essayons d'afficher le prix de chaque oiseau sous forme de chaîne en fonction du niveau de rareté de l'oiseau.

Ajoutez la classe suivante à votre terrain de jeu.

Voici ce qui se passe dans le code du modèle de vue :

1. Nous créons une propriété bird privée de type Bird afin de pouvoir accéder aux propriétés de la classe de modèle. Nous écrivons également une méthode init pour définir la propriété bird.
2. Nous créons deux propriétés calculées qui obtiennent leurs valeurs à partir des propriétés associées à la propriété bird privée. Nous ne modifions pas les propriétés car elles sont déjà dans la bonne représentation pour notre vue.
3. Nous créons une propriété purchaseFeeText qui est une propriété calculée. Cette propriété utilise les valeurs de rareté de la propriété bird privée pour attribuer un coût à l'aide d'une instruction switch. **C'est là que notre classe de modèle de vue prend les données de l'objet de classe de modèle et les convertit en une représentation que nous voulons utiliser dans une vue.**

Maintenant, écrivons le code pour la UIView que nous utiliserons pour afficher les informations de la classe de modèle de vue. Ajoutez la classe suivante à votre fichier de terrain de jeu.

Vous pouvez télécharger l'image utilisée par l'imageView [ici](https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&ved=2ahUKEwiMnIqolaThAhUTbisKHXYhD78QjRx6BAgBEAU&url=https%3A%2F%2Fwww.iconfinder.com%2Ficons%2F1829980%2Fbrand_logo_network_social_swift_icon&psig=AOvVaw25fA-XJq_9BsiEnSwWxchz&ust=1553839488282677). Ajoutez-la au dossier Resources dans le Project Navigator et renommez-la « swifty.png ».

Maintenant que nous avons notre classe de vue d'oiseau configurée, ajoutons le code pour la voir dans la vue en direct du terrain de jeu. Ajoutez ce qui suit après l'accolade fermante de la classe BirdView.

Voici ce qui se passe :

1. Nous créons une nouvelle instance d'oiseau à partir de la classe de modèle nommée « swifty »
2. Nous créons une nouvelle instance à partir de la classe de modèle de vue à partir de l'objet swifty.
3. Nous créons une propriété frame puis initialisons la BirdView en utilisant ce frame.
4. Nous configurons les vues en utilisant les propriétés de l'instance du modèle de vue.
5. Nous définissons la vue pour la vue en direct du terrain de jeu qui rend ensuite tout dans l'éditeur assistant.

Vous pouvez voir la vue en direct en sélectionnant **View**>**Assistant Editor**>**Show Assistant Editor** dans la barre de menu supérieure.

### Quand utiliser cela ?

Si vous vous retrouvez à avoir besoin d'utiliser des données d'une classe de modèle dans des vues avec différentes représentations des données, il serait judicieux d'utiliser le modèle MVVM. MVVM ne sera probablement pas le point de départ de votre application. Vous commencerez probablement par MVC. Gardez un œil sur vos exigences, vous pouvez toujours introduire MVVM (et la plupart des autres modèles de conception) à un stade ultérieur dans votre base de code.