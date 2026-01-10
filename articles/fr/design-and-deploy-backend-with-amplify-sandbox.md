---
title: Comment concevoir presque n'importe quel backend et le déployer sur AWS sans
  code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-12-18T00:59:52.000Z'
originalURL: https://freecodecamp.org/news/design-and-deploy-backend-with-amplify-sandbox
coverImage: https://www.freecodecamp.org/news/content/images/2020/12/How-To-Design-Almost-Any-Backend-and-Deploy-to-AWS-with-No-Code.png
tags:
- name: AWS
  slug: aws
- name: backend
  slug: backend
- name: No Code
  slug: no-code
seo_title: Comment concevoir presque n'importe quel backend et le déployer sur AWS
  sans code
seo_desc: 'By swyx

  In this post I''ll show you how to design four different example apps - a SimpleNote
  clone, a Twitter clone, a Slack clone, and an E-commerce store. And we''ll do it
  with the coolest new toy released at AWS re:Invent 2020.

  Introducing the Ampli...'
---

Par swyx

Dans cet article, je vais vous montrer comment concevoir quatre applications exemples différentes - un clone de SimpleNote, un clone de Twitter, un clone de Slack et une boutique E-commerce. Et nous le ferons avec le nouveau jouet le plus cool sorti lors de l'AWS re:Invent 2020.

## Présentation du Bac à sable Amplify

[Amplify Admin UI](https://aws.amazon.com/blogs/aws/aws-amplify-admin-ui-helps-you-develop-app-backends-no-cloud-experience-required/) est une nouvelle interface low-code pour construire des backends d'applications qui ne nécessite aucune expertise AWS. Cependant, ce que beaucoup de gens peuvent manquer, c'est qu'Amplify Admin inclut également [un tout nouveau Bac à sable](https://sandbox.amplifyapp.com/) qui vous permet de commencer sans un compte AWS.

Ce Bac à sable est une version publiquement partageable de l'interface utilisateur Amplify Admin où vous pouvez créer et prototyper vos modèles de données sans même vous connecter à un compte AWS !

Actuellement, seul [le Bac à sable de données](https://sandbox.amplifyapp.com/start#datastore) est construit, mais avec le temps, les autres catégories AWS Amplify seront également mises à disposition.

Lorsque vous entrez pour la première fois dans un Bac à sable, vous êtes plongé dans un constructeur visuel où vous pouvez ajouter vos [modèles, énumérations et types personnalisés](https://docs.aws.amazon.com/appsync/latest/devguide/designing-your-schema.html). La plupart du temps, vous créerez simplement des modèles.

Vous pouvez nommer les modèles, ajouter des champs et spécifier des types (y compris s'ils sont optionnels ou des champs de tableau), et même ajouter des relations un-à-un, un-à-plusieurs ou plusieurs-à-plusieurs entre les modèles.

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-147.png)

De plus, il vous permet même de partager les modèles de données que vous créez ! Cela signifie que vous n'avez pas à repartir de zéro à chaque fois que vous créez un projet, et vous pouvez partager vos schémas de données comme vous partagez des extraits de code.

## Nos quatre exemples de bacs à sable

Je pensais que ce serait une excellente idée de démontrer à quel point cela est puissant en esquissant quatre exemples de bacs à sable que vous pouvez utiliser :

* Une application de **notes** (inspirée par l'application gratuite de prise de notes [SimpleNote](https://simplenote.com/))
* Une application de **chat** (inspirée par Slack)
* Une application de **réseaux sociaux** (inspirée par Twitter)
* Un backend **ecommerce** (inspiré par chaque expérience de shopping)

## Comment créer des diagrammes de relations entre entités

Amplify Admin UI facilite la mise en route, mais il vaut la peine de faire un peu de planification avant de commencer.

La méthode éprouvée pour cela est de dessiner des [diagrammes de relations entre entités](https://www.youtube.com/watch?v=QpdhBUYk7Kk). Nous avons choisi [d'utiliser Lucidcharts pour les nôtres](https://lucid.app/lucidchart/invitations/accept/563dc191-6613-44f5-aef0-24224ad5fbe1), mais vous pouvez utiliser n'importe quel outil de diagrammation pour cela.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/empty-relationship-diagrams.png)

## L'application de notes

Il s'agit d'une application minimale que j'utilise personnellement tous les jours, donc j'aime sa simplicité. Nous avons deux modèles : Notes et Tags, et une seule relation plusieurs-à-plusieurs entre eux pour une requête facile.

Vous pourriez étendre cela en offrant une édition collaborative basée sur les rôles, qui est disponible une fois que vous déployez ce modèle. Vous devriez également utiliser les [bibliothèques client-side DataStore](https://docs.amplify.aws/lib/datastore/getting-started/q/platform/js#datastore-with-amplify) pour vous assurer que vos notes fonctionnent hors ligne.

Vous pouvez voir le Bac à sable ici : [https://sandbox.amplifyapp.com/schema-design/1c782f02-1fe7-4785-9a02-22a27cc96d0d/clone](https://sandbox.amplifyapp.com/schema-design/1c782f02-1fe7-4785-9a02-22a27cc96d0d/clone). Notez que nous utilisons une relation **plusieurs à plusieurs** bidirectionnelle ici entre les modèles, car les notes peuvent avoir zéro ou plusieurs tags et vice versa.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/simplenote-clone.png)

## Le clone de Slack

Beaucoup d'entre nous utilisent des applications de chat pour le travail, donc nous sommes familiers avec ce cas d'utilisation d'application du côté utilisateur.

Les nouvelles nuances ici sont que chaque Message appartient à un Channel et à un User, et que chaque User peut à la fois créer des Channels et les rejoindre. Il y a donc une relation intéressante à trois voies entre les trois modèles principaux.

Vous pouvez voir le Bac à sable ici : [https://sandbox.amplifyapp.com/schema-design/5f863684-fd1e-41b4-bca1-36c2271e21a1/clone](https://sandbox.amplifyapp.com/schema-design/5f863684-fd1e-41b4-bca1-36c2271e21a1/clone). **Channel** est le modèle le plus complexe ici - notez comment nous utilisons pleinement tous les types de relations disponibles dans le Bac à sable :

* Les Channels peuvent avoir **plusieurs** Users, et les Users peuvent rejoindre **plusieurs** Channels
* Les Channels ne peuvent être créés que par **un** User, et il n'est pas nécessaire de garder une trace des channels qu'un utilisateur particulier a créés
* Les Channels peuvent avoir **plusieurs** Messages, mais chaque Message ne peut appartenir qu'à **un** Channel

![Image](https://www.freecodecamp.org/news/content/images/2024/04/slack-clone.png)

## Le clone de Twitter

Les réseaux sociaux sont souvent l'un des modèles de données les plus complexes à modéliser. Nous implémentons l'application de réseaux sociaux minimale viable - un modèle Tweet et un modèle User est tout ce que nous offrons.

Cependant, le Tweet lui-même a un ensemble complexe de relations. Il a un User auteur, et un ensemble de likes, de réponses et de citations qui doivent être modélisés.

D'autres modifications que vous pouvez envisager pour cette application : offrir d'autres types de tweets, y compris des sondages, des images et des vidéos, intégrer des publicités et des messages directs.

Vous pouvez voir le Bac à sable ici : [https://sandbox.amplifyapp.com/schema-design/ad5b5b7e-f207-42d1-92b1-0ccef056a26b/clone](https://sandbox.amplifyapp.com/schema-design/ad5b5b7e-f207-42d1-92b1-0ccef056a26b/clone). Notez que la récursion est implémentée ici en modélisant les likes, les réponses et les citations comme un **tableau** des ID respectifs de l'User et du Tweet.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/twitter-clone.png)

## La boutique E-commerce

Les enjeux sont plus élevés lorsqu'il y a de l'argent en jeu. Garder une trace des commandes et garantir une excellente expérience client est primordial.

Nous modélisons un backend e-commerce typique en nous assurant que nous avons des modèles séparés pour les Fournisseurs, les Produits, les Commandes et les Clients. Pour entrer dans les nuances d'une expérience de commande typique, nous incluons également la possibilité de spécifier les quantités de produits dans une seule commande, ainsi que d'appliquer des coupons.

Puisqu'il existe une infinité de variations de l'expérience e-commerce, nous ne pouvons pas toutes les modéliser, mais j'espère que cela servira de bon point de départ. Partagez les vôtres si vous avez des variantes de ce concept !

Vous pouvez voir le Bac à sable ici : [https://sandbox.amplifyapp.com/schema-design/aa0e7a61-aa72-4b27-b6db-ea8e2031f95e/clone](https://sandbox.amplifyapp.com/schema-design/aa0e7a61-aa72-4b27-b6db-ea8e2031f95e/clone). Notez la complexité de ce modèle est facilement gérée par les fonctionnalités du Bac à sable. Une Commande ne peut avoir qu'un seul Client, mais un Client peut avoir plusieurs Commandes.

Lorsque vous configurez cela sur le modèle Client, le Bac à sable est suffisamment intelligent pour configurer automatiquement un champ customerID correspondant en tant que "Source de relation" sur le modèle Commande. Cela sera très pratique pour les requêtes GraphQL à l'avenir.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/ecommerce-store.png)

## Comment déployer le modèle sur AWS

Une fois que vous avez terminé votre modèle, le Bac à sable vous invite à le tester localement en le téléchargeant avec le [CLI Amplify](https://docs.amplify.aws/cli). Cependant, si vous souhaitez simplement le mettre en ligne sur AWS, vous pouvez sauter cette étape et passer directement à l'étape "Déployer sur AWS" :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-142.png)

Une fois que vous cliquez sur "Se connecter pour déployer sur AWS", c'est terminé ! Imaginez cela - vous venez de créer un modèle de données backend réel **sans écrire une seule ligne de code** et vous l'avez déployé directement sur AWS. 🤯

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-143.png)

À partir de là, vous pouvez configurer une personnalisation supplémentaire, y compris l'ajout d'authentification, l'invitation d'utilisateurs et l'attribution de rôles, l'ajout de règles d'autorisation sur chaque modèle, la création de contenu avec notre éditeur WYSIWYG, et plus encore.

Si vous souhaitez en savoir plus, [Ali Spittel a écrit un excellent article](https://welearncode.com/intro-amplify-admin-ui/) sur la puissance de l'interface utilisateur Amplify Admin après l'avoir déployée, tandis que cet article a porté sur l'environnement de Bac à sable ne nécessitant pas de compte avant le déploiement.

Nader Dabit a également écrit sur [10 autres fonctionnalités que vous pourriez être impatient d'essayer](https://acloudguru.com/blog/engineering/10-exciting-features-of-the-new-amplify-admin-ui).

Avec le Bac à sable Amplify, il est vraiment facile de modéliser et de réfléchir à n'importe quel scénario de backend d'application, donc j'espère que ces exemples stimuleront votre créativité. Si vous avez des demandes ou des soumissions, [faites-le moi savoir](https://twitter.com/swyx) !