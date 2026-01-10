---
title: Comment gérer les inconnues et faire des hypothèses lors de la conception d'une
  base de données cloud
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-09-21T16:21:47.000Z'
originalURL: https://freecodecamp.org/news/how-to-handle-unknowns-and-make-assumptions-when-designing-a-cloud-database-df002068a83b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*YbuEATHnaNlM4yPP5qYZzg.jpeg
tags:
- name: Cloud Computing
  slug: cloud-computing
- name: database
  slug: database
- name: iOS
  slug: ios
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment gérer les inconnues et faire des hypothèses lors de la conception
  d'une base de données cloud
seo_desc: 'By Rick Mak

  Scenario: Shoebox or social app?

  Say you’re a developer who wants to build a note taking app. Let’s look at one feature
  detail with huge implications on your back-end. To write a note, your app will need
  to be able to save the data.

  Savin...'
---

Par Rick Mak

### Scénario : Application de type boîte à chaussures ou application sociale ?

Disons que vous êtes un développeur qui souhaite créer une application de prise de notes. Examinons un détail de fonctionnalité avec des implications majeures sur votre back-end. Pour écrire une note, votre application devra pouvoir sauvegarder les données.

Sauvegarder un enregistrement dans une base de données est simple. Les questions clés sont :

* Qui devra accéder à cet enregistrement ?
* Sera-ce uniquement votre utilisateur, ou votre utilisateur le partagera-t-il avec d'autres ?
* Votre produit sera-t-il une application de type boîte à chaussures ou une application sociale ?

Si vous prévoyez que les notes restent privées pour l'auteur, vous pouvez conclure que vous créez une application de type boîte à chaussures. Cela signifie que toutes les données vont dans une base de données (BD) privée.

Si vous prévoyez que votre application partage des notes avec d'autres, vous pouvez conclure qu'elle devrait utiliser une BD publique.

Mais saurez-vous laquelle choisir avant de commencer ?

Et que ferez-vous si vous devez modifier votre produit en cours de route ? BD publique et BD privée n'est pas la première chose à laquelle la plupart des développeurs pensent lorsqu'ils créent une application. Nous avons rencontré ces questions lors de la création de notre produit back-end pour nos développeurs, [Skygear](https://skygear.io/).

Grâce à notre expérience dans la création d'applications pour des clients, nous avons **supposé** qu'il existait un choix de base de données approprié. Et que nos utilisateurs sauraient comment choisir.

Comment construire un back-end pour des développeurs qui ne sont pas encore sûrs des besoins de leur produit ? Ou pour ceux qui veulent garder leurs options ouvertes pour l'avenir ?

En tant que responsable technique du projet, je souhaite partager avec vous notre processus de prise de décision d'il y a 2 ans. J'espère que cela aidera les futures équipes de développement à aborder les inconnues et les hypothèses.

### Pourquoi avons-nous commencé à réfléchir aux BD privées et publiques ?

De nombreuses applications nécessitent un back-end pour stocker et interroger les données utilisateur. Le back-end demande beaucoup de travail à construire et, soyons honnêtes, ce n'est pas très agréable à créer. [Skygear](https://skygear.io/) est notre back-end serverless open-source. Il aide à répondre aux fonctionnalités de développement courantes pour les applications mobiles et web.

La fonctionnalité dont je vais parler est notre Cloud DB, où vous stockez et interrogez les données utilisateur. Lorsque nous avons commencé à concevoir Cloud DB, nous nous sommes demandé comment différentes applications stockent et interrogent les données utilisateur.

Nous avons examiné le portefeuille d'applications mobiles de notre entreprise [portfolio](https://oursky.com/works/) pour nous inspirer. Notre entreprise fait tout, des applications grand public aux applications de commerce électronique. Nous les avons donc regroupées en applications "boîte à chaussures" et "sociales".

Les applications de type boîte à chaussures stockent des données personnelles que l'utilisateur souhaite garder privées. Par exemple, notre projet parallèle [Spentable](https://itunes.apple.com/app/spentable-track-your-daily-expense-and-savings/id500630565?mt=8) aide un utilisateur à suivre ses dépenses quotidiennes. Les données stockées dans l'application sont destinées à rester privées, dans une boîte à chaussures.

Mais il y a des choses que nous voulons partager publiquement ou avec des amis. Cela signifie également que l'utilisateur doit contrôler qui peut lire ses données. Ces deux types d'applications présentent un défi dans la conception de la Cloud DB de Skygear. Nous voulions rendre le stockage des données dans Cloud DB aussi simple que possible. Pour les applications de type boîte à chaussures, les développeurs n'ont besoin que d'une base de données où chaque utilisateur ne peut voir que les données qu'il y a mises. Pourtant, dans les applications sociales, les développeurs ont besoin de fonctionnalités telles que l'ACL (contrôle d'accès). Comment pouvons-nous simplifier les choses pour les développeurs des deux types d'applications ?

### Avoir le beurre et l'argent du beurre

Nous avons décidé de résoudre ce problème en introduisant le concept de plusieurs bases de données dans le [Cloud DB](https://docs.skygear.io/guides/cloud-db/basics/ios/) : BD privée et BD publique. Chaque utilisateur dispose d'une BD privée pour y mettre des données, et ces données ne sont disponibles que pour le même utilisateur. L'application dispose également d'une BD publique partagée entre tous les utilisateurs.

Un développeur d'application de type boîte à chaussures peut se concentrer sur la sauvegarde et la récupération des données sans se soucier des permissions, car les données dans la BD privée sont toujours privées.

Cependant, la BD privée ne fonctionne pas du tout pour les applications sociales. Les développeurs d'applications sociales doivent mettre les données dans la BD publique, car les données des applications sociales sont destinées à être partagées.

![Image](https://cdn-media-1.freecodecamp.org/images/4DkWIWQuZyWsomMvOcP0ld7KBmzYtn7-IJId)

Avant d'ajouter la prise en charge de l'[ACL](https://docs.skygear.io/guides/cloud-db/acl/ios/), cette simple distinction pour les données publiques et privées nous a bien servis (ainsi que nos utilisateurs). Tout dans la BD privée est vraiment privé, tandis que tout dans la BD publique est vraiment public.

"Tout est public" n'est pas suffisant. La plupart des applications sociales ont des cas d'utilisation où les données ne sont partagées qu'entre un groupe d'amis.

L'ACL est un autre sujet difficile et intéressant qui mérite son propre article.

### Nous ne pouvions pas avoir le meilleur des deux bases de données

Séparer la BD en bases privées et publiques était une bonne idée. Nous pensions qu'elles prenaient en charge le cas d'utilisation pour la majorité des applications.

Mais les premiers adopteurs ont trouvé nos options privées et publiques déroutantes.

Nos premiers utilisateurs nous ont donné des retours inestimables. Nous avons également prêté attention aux questions de support que nous avons reçues. Voici ce que nous avons appris des retours des développeurs lorsqu'ils ont utilisé notre Cloud DB :

1. Il n'est pas évident pour les développeurs de savoir ce qu'ils construisent au début
Bien qu'il puisse être évident de déterminer quel type d'application un développeur crée en regardant le produit rétrospectivement, ce n'est pas évident dès le départ. Obliger le développeur à décider s'il crée une application de type boîte à chaussures ou sociale au début est difficile, sinon impossible.
2. Les développeurs veulent simplement commencer rapidement
Nous voulons que les développeurs apprennent les bases aussi rapidement que possible. Devoir apprendre un concept supplémentaire pour choisir quelle BD utiliser avant de pouvoir sauvegarder et récupérer des données est trop demander pour les nouveaux utilisateurs.
3. La décision pour une BD publique ou privée, une fois prise, n'est pas facile à inverser
Supposons qu'un développeur commence avec une idée d'application de type boîte à chaussures et qu'il met tout dans la BD privée. Plus tard, il peut réaliser qu'il devrait plutôt rendre l'application sociale. Il n'est pas facile de migrer les données une fois qu'elles sont mises dans une BD particulière.
4. Les permissions sont généralement une réflexion après coup
La sécurité des données est une priorité dans notre entreprise. Mais la sécurité des données n'est pas la première chose à laquelle pense un développeur. Surtout lorsqu'il fait simplement un prototype de preuve de concept. Il veut se concentrer sur la fonctionnalité d'abord, et s'occuper de la sécurité plus tard.

### Nos conclusions

Nous réfléchissons toujours à la manière dont nous pourrions améliorer nos produits. Nous pourrions faire mieux en termes d'architecture logicielle, de documentation utilisateur et de facilité d'utilisation. Nous réfléchissons parfois à ce que nous ferions si nous pouvions remonter le temps de deux ans pour recommencer. Mais voici ce que nous dirions à nos anciens nous-mêmes :

1. Si les développeurs sont déjà familiers avec un concept existant, adoptez-le
La plupart des développeurs sont familiers avec le concept de base de données. C'est une sorte de conteneur où les développeurs peuvent sauvegarder du contenu. Ils peuvent également récupérer des données et prendre en charge la propriété CRUD (Create, Read, Update, and Delete).

Parce que les développeurs sont déjà familiers avec le concept de base de données, ils trouveraient une seule base de données sur Cloud DB simple à utiliser.
2. Introduisez de nouveaux concepts lorsque les développeurs sont prêts pour eux
Cette idée est en fait une autre façon de dire que nous devrions rendre la courbe d'apprentissage aussi facile que possible. Skygear était un prototype à sa manière. Nous venons de lancer la V[1.0](https://skygear.io/) !

Vous ne voulez jamais rendre la vie difficile à vos premiers adopteurs. Devoir tout apprendre avant que les développeurs puissent faire quoi que ce soit ne fonctionne pas bien d'un point de vue produit. Jusqu'à ce que les développeurs aient besoin de réfléchir aux permissions des données, ils ne devraient pas avoir besoin de connaître la différence entre une BD privée et une BD publique. Nous devrions laisser nos utilisateurs commencer avec les concepts communs d'abord pour se familiariser avec une nouvelle plateforme.

Ce n'est qu'une fois qu'ils sont à l'aise que nous devrions introduire de nouveaux concepts pour offrir plus d'options. Dans ce cas, il n'y a pas de mal pour un développeur de découvrir qu'il a besoin d'ACL, donc le nouveau concept est une étape naturelle après avoir appris à utiliser Cloud DB.

### Ce que nous avons appris

Lorsque nous avons commencé à travailler sur Skygear il y a deux ans, nous voulions construire un produit génial avec 2 à 4 de nos développeurs seniors. Nous avions des testeurs prêts parmi nos propres développeurs internes, qui ont donné beaucoup de retours critiques. Nous pensions utiliser notre expérience dans le développement d'applications web et mobiles pour prendre de meilleures décisions sur la façon de concevoir des outils pour d'autres développeurs.

Mais notre expérience a également créé des hypothèses sur ce que nous attendions de nos utilisateurs avant d'utiliser notre produit.

Le bon côté d'avoir obtenu des retours des utilisateurs sur Cloud DB au fur et à mesure était que nous avons appris que nos hypothèses étaient incorrectes. Notre leçon la plus précieuse a été le rappel humble d'un principe de base des startups. Peu importe notre expérience, nous ne savons souvent pas exactement ce que nous construisons.

Bien sûr, cela ne nous empêche pas d'essayer de construire cette pierre philosophale pour faciliter la vie de nos collègues développeurs. Comme l'a dit mon cofondateur, Ben, l'un de ses jours les plus productifs a été celui où il a jeté 1000 lignes de code.

Je tiens à créditer mon collègue [cheungpat](https://medium.com/u/cdd8a0d1e292) qui a travaillé sur le Cloud DB avec moi et a aidé à écrire cet article.

Mon équipe serait ravie d'entendre vos retours critiques sur [Skygear](https://skygear.io/). Consultez également notre [documentation](https://docs.skygear.io/) et nos [dépôts GitHub](https://github.com/SkygearIO/features) pour voir comment nous discutons des fonctionnalités de Skygear.