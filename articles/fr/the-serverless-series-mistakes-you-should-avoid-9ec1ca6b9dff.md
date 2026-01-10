---
title: Serverless a ses pièges. Voici comment les éviter.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-27T06:24:41.000Z'
originalURL: https://freecodecamp.org/news/the-serverless-series-mistakes-you-should-avoid-9ec1ca6b9dff
coverImage: https://cdn-media-1.freecodecamp.org/images/1*hyAp4Q0OPmp-wOaeSqA7nA.jpeg
tags:
- name: Cloud Computing
  slug: cloud-computing
- name: General Programming
  slug: programming
- name: serverless
  slug: serverless
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Serverless a ses pièges. Voici comment les éviter.
seo_desc: 'By Nicolas Dao

  In this post, I will share the lessons I learned over the past year while using
  Serverless to build mobile and web apps for a tech consultancy in Sydney. For each
  drawback, I will also recommend one or multiple solutions.

  1. FaaS - Con...'
---

Par Nicolas Dao

Dans cet article, je vais partager les leçons que j'ai apprises au cours de l'année passée en utilisant Serverless pour [construire des applications mobiles et web pour une société de conseil technologique à Sydney](https://neap.co/). Pour chaque inconvénient, je recommanderai également une ou plusieurs solutions.

#### 1. FaaS - Limitation du Pooling de Connexions

Les conversations sur FaaS ne mentionnent pas souvent cette limitation. Les fournisseurs de cloud commercialisent FaaS comme une solution pouvant s'adapter à l'infini. Bien que cela puisse s'appliquer à la fonction elle-même, la plupart des ressources dont votre fonction dépend ne seront pas infiniment scalables.

Le nombre de connexions simultanées que votre base de données relationnelle supporte est l'une de ces ressources limitées. L'incompatibilité de FaaS avec le [connection pooling](https://en.wikipedia.org/wiki/Connection_pool) est ce qui rend ce problème si important.

En effet, comme je l'ai mentionné précédemment, chaque instance de votre fonction vit dans son environnement stateless isolé. Cela signifie que lorsqu'elle se connecte à une base de données relationnelle (par exemple PostgreSQL, MySQL, Oracle), elle devrait probablement utiliser un pool de connexions pour éviter de se reconnecter sans cesse à votre base de données.

Votre base de données relationnelle ne peut gérer qu'un certain nombre de connexions simultanées (généralement, le défaut est 20). Lancer plus de 20 instances de votre fonction épuisera rapidement les connexions de votre base de données, empêchant d'autres systèmes d'y accéder.

Pour cette raison, je recommande d'éviter tout FaaS si votre fonction doit communiquer avec une base de données relationnelle en utilisant un pool de connexions. Si vous devez utiliser un pool de connexions, alors quelques options sont disponibles :

* Utilisez un BaaS à la place.
* Certaines bases de données relationnelles comme PostgreSQL offrent des plugins qui peuvent résoudre ce problème en [multiplexant le nombre de connexions simultanées disponibles](https://blog.zappa.io/posts/multiplex-rds-connections).

#### 2. FaaS - Pas de Support pour WebSockets

Celui-ci est assez évident. Mais pour ceux qui pensent pouvoir avoir le beurre et l'argent du beurre, vous ne pouvez pas espérer maintenir un WebSocket sur un système qui est par conception éphémère. Si vous cherchez un WebSocket Serverless, alors vous devrez utiliser un BaaS comme Zeit Now à la place.

Alternativement, si vous essayez de créer une API GraphQL Serverless, il est possible d'utiliser des Subscriptions (qui reposent sur WebSockets) en utilisant [AWS AppSync](https://aws.amazon.com/appsync/). Un excellent article qui explique ce cas d'utilisation en détail est [Running a scalable & reliable GraphQL endpoint with Serverless](https://hackernoon.com/running-a-scalable-reliable-graphql-endpoint-with-serverless-db16e42dc266).

#### 3. FaaS — Cold Start

Les solutions FaaS comme [AWS Lambda](https://aws.amazon.com/lambda) ont démontré d'énormes gains lors de la résolution de défis Map-Reduce (par exemple, [Leveraging AWS Lambda for Image Compression at Scale](https://medium.com/squad-engineering/leveraging-aws-lambda-for-image-compression-at-scale-a01afd756a12)). Cependant, si vous essayez de fournir une réponse rapide à des événements comme des requêtes HTTP, vous devrez prendre en compte le temps nécessaire à la fonction pour se réchauffer.

Votre fonction vit dans un environnement virtuel qui doit être lancé pour s'adapter en fonction du trafic qu'elle reçoit (quelque chose que vous ne contrôlez naturellement pas). Ce processus de lancement prend quelques secondes, et après que votre fonction soit inactive en raison d'un faible trafic, elle devra être relancée.

Je l'ai appris à mes dépens lors du déploiement d'une API REST de reporting relativement complexe sur Google Cloud Functions. Cette API faisait partie d'un effort de refactorisation de microservices pour décomposer notre grande API web monolithique. J'ai commencé avec un endpoint à faible trafic, ce qui signifiait que la fonction était souvent dans un état inactif. Les rapports alimentés par ce microservice sont devenus lents la première fois qu'ils étaient accessibles.

Pour résoudre ce problème, j'ai déplacé notre microservice de Google Cloud Function (FaaS) vers Zeit Now (BaaS). Cette migration m'a permis de garder au moins une instance active en permanence (plus d'informations sur Zeit Now dans mon prochain article : Pourquoi nous aimons Zeit Now et quand l'utiliser à la place de FaaS).

#### 4. FaaS - Processus de Longue Durée, Ne Perdez Pas Votre Temps !

AWS Lambda et Google Cloud Functions ne peuvent pas fonctionner plus de 5 et 9 minutes, respectivement. Si votre logique métier est une tâche de longue durée, vous devrez passer à un BaaS comme Zeit Now à la place.

Pour plus de détails sur les limitations de FaaS, veuillez consulter [AWS Lambda quotas](https://docs.aws.amazon.com/lambda/latest/dg/limits.html) et [Google Cloud Functions quotas](https://cloud.google.com/functions/quotas).

#### 5. BaaS & FaaS - Perte de Contrôle sur l'Infrastructure

Si les exigences de votre produit nécessitent un certain degré de contrôle sur votre infrastructure, alors Serverless vous laissera probablement dans l'embarras. Exemples de tels problèmes pourraient être :

* Orchestration du déploiement de microservices. Se retrouver avec une myriade de microservices Serverless deviendra rapidement un cauchemar de déploiement, surtout s'ils doivent être versionnés ensemble ou par domaine.
* Contrôler le cycle de vie de chaque serveur pour économiser sur les coûts.
* Avoir des tâches de longue durée sur plusieurs serveurs.
* Contrôler la version exacte du système d'exploitation sous-jacent du serveur, ou installer des bibliothèques spécifiques requises par votre application.
* Contrôler la réplication géographique exacte de votre application ou de vos données pour garantir des performances cohérentes et rapides à l'échelle mondiale (il existe des moyens de surmonter cela dans certains scénarios. Consultez [Build a serverless multi-region, active-active backend solution in an hour](https://read.acloud.guru/building-a-serverless-multi-region-active-active-backend-36f28bed4ecf)).

Serverless peut être insuffisant dans tous les cas d'utilisation ci-dessus. Cependant, comme je l'ai discuté précédemment, Serverless n'est qu'une extension de PaaS. Pour garder autant de concentration que possible sur l'écriture de code plutôt que de trop s'inquiéter de la scalabilité et de la fiabilité de l'infrastructure sous-jacente, tirer parti des dernières stratégies de conteneurisation PaaS telles que [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine/) peut vous rapprocher de ce que Serverless a à offrir.

#### 6. BaaS & FaaS - Conformité & Sécurité

Serverless partage toutes les plaintes habituelles liées au cloud. Vous abandonnez le contrôle de votre infrastructure à un ou plusieurs tiers. Selon le fournisseur, Serverless peut ou non fournir les bons niveaux de SLA et de sécurité pour votre cas d'utilisation.

Que Serverless soit une solution viable ou non du point de vue de la conformité et de la sécurité dépend vraiment de votre cas particulier. De nombreux articles discutent de ce sujet en détail (comme [The state of serverless security](https://read.acloud.guru/the-state-of-serverless-security-fall-2017-fb2b8936044f)).

### Conclusion

Serverless n'est pas une solution miracle. Les gains que vous pouvez en tirer dépendent de votre connaissance de celui-ci. La bonne nouvelle est que la barrière à l'entrée est si basse que vous devriez être compétent en un rien de temps.

### À VENIR...

Bien sûr, Serverless a des limitations. Toutes les solutions techniques en ont. La question maintenant est de savoir comment nous les surmontons. Dans mon prochain article, j'écrirai sur les suggestions que mon équipe et moi avons développées pour faire face à ces limitations : « Pourquoi nous aimons Zeit Now et quand l'utiliser à la place de FaaS ».

Suivez-moi sur Medium - [Nicolas Dao](https://www.freecodecamp.org/news/the-serverless-series-mistakes-you-should-avoid-9ec1ca6b9dff/undefined) - si vous êtes intéressé par ce qui va suivre :

Articles actuels de cette série sur Serverless :

* [Savez-vous vraiment ce qu'est Serverless ?](https://hackernoon.com/the-serverless-series-what-is-serverless-d651fbacf3f4)
* [L'impact de Serverless sur le leadership technologique](https://hackernoon.com/the-serverless-series-automating-it-engineers-reshaping-tech-leadership-788cf9b625d5)
* [Comment Serverless automatise les ingénieurs IT](https://hackernoon.com/the-serverless-series-automating-it-engineers-reshaping-tech-leadership-788cf9b625d5)

Articles futurs de la série :

* Pourquoi nous aimons [Zeit Now](https://zeit.co/now) et quand l'utiliser à la place de FaaS
* Architecture Serverless pilotée par événements : L'ajustement naturel
* Comment gérer la contre-pression avec Serverless ?
* GraphQL sur Serverless en moins de 2 minutes