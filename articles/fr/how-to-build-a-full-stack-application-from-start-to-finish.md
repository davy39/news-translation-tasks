---
title: Comment architecturer une application Full-Stack de A à Z
subtitle: ''
author: Lane Wagner
co_authors: []
series: null
date: '2022-10-04T17:49:10.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-full-stack-application-from-start-to-finish
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/jeremy-thomas-FO7bKvgETgQ-unsplash.jpg
tags:
- name: full stack
  slug: full-stack
- name: software architecture
  slug: software-architecture
- name: Web Applications
  slug: web-applications
seo_title: Comment architecturer une application Full-Stack de A à Z
seo_desc: "Software architecture is a massive topic. That said, I think I can give\
  \ you a simple method you can use to approach the architecture of a full-stack application.\
  \ \nIn particular, I want to talk about the order in which you should think about\
  \ and build..."
---

L'architecture logicielle est un sujet vaste. Cela dit, je pense pouvoir vous donner une méthode simple que vous pouvez utiliser pour aborder l'architecture d'une application Full-Stack. 

En particulier, je veux parler de l'*ordre* dans lequel vous devriez réfléchir et construire les pièces d'une application web typique.

Mon conseil est que **pour chaque fonctionnalité**, vous devriez :

1. Concevoir le front-end
2. Construire le front-end
3. Construire la couche de persistance (base de données back-end et modèles de données)
4. Construire l'API (application back-end)

_La meilleure façon est une approche front -> back -> middle._

## Pourquoi commencer par le Front-End ?

En supposant que vous travailliez avec une bonne équipe produit (ou peut-être que vous êtes une équipe d'une seule personne, donc vous _êtes_ l'équipe produit), la chose la plus importante est l'expérience de l'utilisateur final. Par conséquent, il est plus logique de commencer par le front-end. 

Ce n'est qu'en concevant et en construisant le front-end que vous apprendrez quels types d'exigences vous aurez pour le back-end de votre application.

L'utilisateur du code front-end est le client. L'utilisateur du code back-end est le code front-end.

## Comment construire un Front-End sans Back-End auquel se connecter ?

C'est toute la beauté de commencer par le front-end. Commencez par simuler (mocker) toutes les données qui remplissent votre interface utilisateur. Par exemple, au lieu d'écrire un code comme celui-ci :

```js
const resp = await fetch(userUrl)
const user = await resp.json()
```

Vous écririez simplement :

```js
const user = {
    id: 1,
    username: "bobbyjoe",
    email: "bobbyjoe@example.com",
    profilePictureUrl: "https://fakewebsite.com/fakeimageurl.jpeg"
}
```

Ensuite, vous écririez tout le reste du code front-end comme vous le feriez normalement. Au moment où vous aurez terminé, vous saurez _exactement_ quel type de données votre back-end devra stocker et servir. 

Et quand vous en viendrez enfin à construire le back-end, vous n'aurez qu'à remplacer ces objets JSON simulés par des requêtes `fetch`.

## Créer le modèle de données et le schéma de la base de données

D'accord, vous avez donc construit le front-end pour votre nouvelle fonctionnalité, et vous avez simulé toutes les données que vous avez décidé de stocker sur le back-end. Il est maintenant temps de décider comment vous allez modéliser ces données dans votre base de données.

J'aime passer directement du front-end à la base de données. C'est parce qu'il est plus important de bien concevoir la façon dont vous stockez les données dans la base que la façon dont vous les servez via votre API – du moins, si le consommateur de votre API est votre propre équipe (ou vous-même).

![Image](https://www.freecodecamp.org/news/content/images/2022/10/well.jpeg)
_Obi Wan écrivant des API pour lui-même_

[Changer les schémas de base de données est _difficile_](https://wagslane.dev/posts/keep-your-data-raw-at-rest/). Il est beaucoup plus facile d'ajouter un point de terminaison `/v2` à votre back-end que de réécrire votre couche de persistance. 

Pour cette raison, réfléchir à la manière dont vous allez stocker vos données, et donner la priorité à cette conception, vous évitera généralement bien des maux de tête par la suite.

En règle générale, une fois que le front-end est construit, vous disposez de toutes les informations nécessaires pour concevoir un schéma de base de données solide.

Par exemple, vous savez peut-être que vous avez besoin de :

* Stocker des utilisateurs, chacun avec un e-mail et une photo de profil
* Permettre aux utilisateurs de rejoindre, créer et quitter des organisations

Dans cette optique, et en supposant que vous utilisiez une base de données SQL relationnelle comme Postgres, vous pouvez probablement commencer par quelque chose comme :

* Une table `users` avec les champs `id`, `created_at`, `email`, et `profile_picture_url` 
* Une table `organizations` avec les champs `id`, `created_at`, et `name` 
* Une table `users_organizations` avec les champs `id`, `user_id`, `organization_id`, et `role` 

Les utilisateurs vont dans la table `users`, les organisations dans la table `organizations`, et la table `users_organizations` est une table de jointure pour suivre quels utilisateurs font partie de quelles organisations et quel est leur rôle. Par exemple, ils peuvent être `admin` ou `member`. 

Si vous n'êtes pas familier avec toute cette terminologie SQL, vous pouvez consulter mon [cours Learn SQL](https://boot.dev/learn/learn-sql) sur [Boot.dev](https://boot.dev/).

## Enfin, construisez l'application Back-End

Maintenant que vous savez de quelles données votre front-end a besoin, et comment vous pouvez les modéliser au mieux dans votre base de données, votre dernière tâche consiste à lier le tout avec une API back-end. 

Commencez par l'API la plus simple possible.

Ne construisez pas de capacités de jointure complexes pour commencer. Ne construisez pas de fonctionnalités de pagination ou de filtrage complexes si vous n'en avez pas besoin. Vous pourrez toujours ajouter de nouveaux points de terminaison et paramètres plus tard afin de répondre aux besoins de performance au fur et à mesure qu'ils se présentent. Je suis un grand fan de l'[optimisation pour la simplicité d'abord](https://wagslane.dev/posts/optimize-for-simplicit-first/).

Quoi qu'il en soit, cela ne veut pas dire que vous n'aurez pas besoin de quelque chose de plus complexe que quelques points de terminaison CRUD – c'est possible. Si c'est le cas, au moins vous avez toutes les informations devant vous pour prendre une décision éclairée. 

Ne construisez pas plus que ce que le front-end exige, et essayez d'utiliser les modèles de données simples que vous avez créés dans la base de données.

Gardez à l'esprit qu'il y aura des allers-retours. Ne vous sentez pas mal si vous avez oublié une fonctionnalité sur le front-end et que vous devez y revenir pour l'ajouter. Ou peut-être avez-vous négligé la lenteur de chargement d'une certaine vue dans votre application si vous stockez les données d'une certaine manière dans votre base de données. Cela peut être un processus itératif, et cela devrait l'être.

## Une dernière note : ne faites pas de Waterfall

Je tiens à souligner à nouveau le fait que vous devriez faire cela *par fonctionnalité*. Je ne préconise pas de planifier une application entière à l'avance. Vous devriez toujours pratiquer le développement de produit itératif.

Bonne chance, et si vous avez besoin d'aide pour apprendre le développement back-end, n'hésitez pas à aller voir ce que je construis sur [Boot.dev](https://boot.dev/)!