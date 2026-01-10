---
title: Une introduction aux microservices
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-04-04T02:02:08.000Z'
originalURL: https://freecodecamp.org/news/an-introduction-to-microservices-2705e7758f9
coverImage: https://cdn-media-1.freecodecamp.org/images/1*-_7x5pNS-GeHsa_wsI_snA.jpeg
tags:
- name: Devops
  slug: devops
- name: Microservices
  slug: microservices
- name: General Programming
  slug: programming
- name: Software Engineering
  slug: software-engineering
- name: Web Development
  slug: web-development
seo_title: Une introduction aux microservices
seo_desc: 'By Sanchit Gera

  Network architectures based on the micro service pattern have gained quite some
  popularity in recent years. Micro services have emerged as a solution to large,
  unwieldy monolithic applications.

  This design attempts to solve the proble...'
---

Par Sanchit Gera

Les architectures réseau basées sur le modèle de microservices ont gagné en popularité ces dernières années. Les microservices sont apparus comme une solution aux grandes applications monolithiques encombrantes.

Cette conception tente de résoudre les problèmes qui émergent lorsque votre base de code dépasse une certaine taille, et qu'il devient de plus en plus difficile à maintenir.

Les services à petite échelle sont nés de la nécessité de se développer rapidement tout en gardant votre code gérable. Netflix, Amazon et Spotify sont quelques-uns des acteurs les plus importants et intéressants qui se tournent vers ce type de modèle. Explorons pourquoi.

#### Qu'est-ce que les microservices ?

Définir les microservices est une affaire délicate. Il n'y a pas d'exigence ou de spécification précise que votre base de code doit respecter pour être considérée comme "micro". Au lieu de cela, les développeurs et les architectes doivent adhérer à un ensemble d'idées générales afin de concevoir un système qui fonctionne pour eux.

> Le style architectural des microservices est une approche pour développer une seule application comme une suite de petits services, chacun fonctionnant dans son propre processus et communiquant avec des mécanismes légers, souvent une API de ressources HTTP. **_Martin Fowler_**

Dans [Building Microservices](http://shop.oreilly.com/product/0636920033158.do), Sam Newman liste deux idées clés qui doivent être gardées à l'esprit lors de la conception de ces services : **le couplage lâche** et **la haute cohésion**. Ces termes peuvent sembler être des mots à la mode, mais permettez-moi de les expliquer.

#### Couplage lâche

Idéalement, vous voulez que les services aient peu ou pas de dépendance les uns envers les autres. Les services doivent être modifiables et déployables indépendamment, sans nécessiter de changements dans d'autres parties du système.

Les services doivent exposer uniquement les informations absolument nécessaires afin d'empêcher les applications qui consomment leurs données de se lier trop étroitement à eux. Cela facilite le déploiement des changements à l'avenir.

#### Haute cohésion

La haute cohésion peut être considérée comme un corollaire au couplage lâche. La cohésion fait référence à l'idée que toute la logique concernant une entité particulière dans le système doit être regroupée en un seul endroit. Cela facilite la modification du comportement d'une partie du système, car cela minimise le nombre d'endroits où le code doit être mis à jour.

Il est important de garder à l'esprit qu'il n'y a rien dans une structure monolithique qui vous empêcherait d'appliquer les mêmes principes. La modularité est encouragée dans toute base de code. Les grandes bases de code ont traditionnellement reposé sur les concepts de modules et de bibliothèques partagés afin de faire respecter un degré similaire de séparation logique. Les microservices vont plus loin en rendant ces frontières plus évidentes et légèrement plus difficiles à franchir.

### Facteurs inducteurs

Pour comprendre les microservices, vous devez comprendre qu'il y a certains inconvénients dans une structure monolithique traditionnelle, qui sont les raisons pour lesquelles les développeurs se tournent vers des services plus faiblement couplés.

#### Diversité technologique

À mesure que votre application grandit en taille, le nombre de fonctionnalités qu'elle implémente augmente, et par extension, le nombre d'exigences technologiques imposées à votre système.

Par exemple, certaines parties de votre application peuvent nécessiter une bibliothèque spécifique écrite dans un langage spécifique qui se trouve être l'outil idéal pour elle. Certaines parties de votre application peuvent bénéficier de la nature statiquement typée et sécurisée de Java. Alors que d'autres parties peuvent être moins exigeantes. De même, la base de données optimale peut varier considérablement à travers l'application.

![Image](https://cdn-media-1.freecodecamp.org/images/X84PfjMzsz-w7NW2pmNQrsRRACDEqubPZ8L4)

Cela offre également une bonne opportunité d'expérimenter avec de nouveaux langages et frameworks dans un cadre limité. L'expérimentation, d'une certaine manière, devient moins risquée puisqu'elle est limitée à seulement quelques services qui peuvent être restaurés à leur état d'origine assez rapidement.

En général, dans une application monolithique, les outils que vous choisissez finissent généralement par être le "plus petit dénominateur commun", plutôt que d'être optimisés pour la tâche à accomplir.

Il y a, cependant, un inconvénient à tout cela. En pratique, il est possible que le grand nombre de frameworks et de langages utilisés par différents services devienne lui-même un désordre. Déplacer des développeurs entre des équipes (généralement une équipe par service) peut être un cauchemar s'ils ne sont pas familiers avec la nouvelle pile technologique.

Intéressamment, Spotify — un grand défenseur du modèle d'architecture des microservices — a une politique de tolérance zéro en ce qui concerne la variété des langages utilisés sur leurs services de production. Essentiellement, chaque service déployé en production doit être écrit en Java et en Java uniquement (invalidant ainsi cet argument).

Néanmoins, la diversité technologique est un avantage clé d'une conception basée sur les microservices, même si elle n'est utilisée que de manière parcimonieuse.

#### Tolérance aux pannes

L'idée de tolérance aux pannes est fortement liée au concept de _couplage lâche_ discuté précédemment. Les équipes doivent se concentrer sur la création de chaque service aussi indépendant que possible. Cela garantit que si un service tombe en panne, il n'affecte pas les autres services (sauf ceux qui en dépendent directement).

En tant qu'utilisateur final, votre expérience peut être dégradée et limitée, mais l'application doit rester fonctionnelle. Dans la plupart des cas, cela est bien mieux que de faire planter toute l'application.

Prenons l'exemple d'Amazon. Supposons qu'Amazon soit composé de plusieurs services différents, chacun gérant une partie cruciale de l'application.

* Service d'inventaire : Responsable de la gestion de tous les articles que vend Amazon, ainsi que de leurs niveaux de stock
* Service de commande : Responsable de la prise des commandes des clients et de l'expédition des articles
* Service de recommandation : Responsable de la génération de recommandations sur les produits qui pourraient intéresser un client

Ce n'est en aucun cas une description complète ou précise de la structure d'Amazon. Mais cela fonctionne bien pour cet exemple.

Considérons le scénario où le service de recommandation décide de planter. Dans une application monolithique traditionnelle, cela pourrait entraîner l'arrêt d'Amazon ! Oh là là !

Dans le cas présent, cependant, un utilisateur pourrait se voir servir une page sans aucune recommandation, tandis que les autres parties de l'application continuent de fonctionner tout aussi bien. Une expérience sous-optimale, mais toujours fonctionnelle. Pas mal !

#### Évolutivité

La question de l'évolutivité est d'une importance immense pour une entreprise en croissance rapide. Lorsque vous avez une seule application gigantesque, toutes ses parties ne sont pas également intensives en charge. Certaines peuvent être responsables de choses plus passives et routinières, comme servir des informations statiques, tandis que d'autres peuvent être plus intensives, nécessitant beaucoup d'interactions avec la base de données et/ou de puissance de calcul.

Le problème avec une base de code monolithique est que, quelle que soit la nature des différentes opérations qu'elle effectue, vous devez mettre à l'échelle l'ensemble de l'application en fonction des besoins. Comme cela ne représente pas précisément les demandes réelles sur votre système, cela conduit à des quantités énormes de puissance de calcul et de ressources gaspillées.

C'est l'un des problèmes que les microservices tentent de résoudre. Parce que la fonctionnalité est séparée en différentes "boîtes", chaque boîte peut être mise à l'échelle indépendamment, sans affecter le reste du système. Ainsi, vous passez d'un système qui ressemble à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/NgI47CQ2s5hPph69Uz-tpuzWnzq9BDazS-zh)
_Emprunté à la conférence de Kevin Goldsmith à GOTO Berlin 2015_

à un système qui ressemble à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/NjsgG9RbkKGtSOqiIFo9mBCDog5sfrJhd9mD)
_Emprunté à la conférence de Kevin Goldsmith à GOTO Berlin 2015_

Voilà !

#### Facilité de déploiement

Enfin, parlons un peu de la manière dont le déploiement de ces services fonctionnerait. Étant donné le nombre impressionnant de services déployés, cela peut sembler un peu être un contre-argument au premier abord. Cependant, la chose clé à retenir est que tout changement dans le comportement d'une partie particulière de l'application nécessite généralement un changement dans une partie, et de préférence une seule partie de l'application, isolée dans un microservice dans ce cas.

Lorsque vous avez un petit changement, cette différence se résume à redéployer un petit service plutôt qu'une application d'un million de lignes. En pratique, les applications monolithiques sont rarement redéployées à ce rythme. Par conséquent, les changements s'accumulent généralement entre les versions, conduisant à des versions plus grandes et plus complètes. Le nombre impressionnant de changements déployés pourrait lui-même être un risque potentiel.

Mais comme toujours, il y a un compromis impliqué ici. Bien que les microservices vous permettent de déployer des changements rapidement, ils nécessitent que tous les clients de votre service soient synchronisés avec vos versions. Cela pourrait être trivial si le nombre de services dépendant de vos services est petit, mais dans une organisation plus grande, cela peut ne pas toujours être le cas. Un compromis peut être atteint, et vous pourriez très bien finir par supporter les versions précédentes de vos microservices pour les clients qui en dépendent, jusqu'à ce qu'ils se mettent à niveau !

Dans cet article, je n'ai fait qu'effleurer la surface. Il y a plusieurs autres idées que vous devriez considérer avant de vous lancer dans la voie des microservices. Des concepts comme [la décentralisation des données](http://microservices.io/patterns/data/database-per-service.html) et [la découverte de services](http://microservices.io/patterns/client-side-discovery.html) sont centraux pour une architecture robuste, et nécessitent plus d'étude. (Peut-être un futur article !)

Je suis relativement nouveau dans ce style de développement moi-même. Si j'ai omis ou mal représenté quelque chose, n'hésitez pas à me le faire savoir dans les commentaires :)

_Si c'est un sujet que vous souhaitez approfondir, voici quelques ressources que j'ai trouvées utiles en rédigeant cet article :_

* [_Building Microservices — Sam Newman_](http://www.amazon.com/Building-Microservices-Sam-Newman/dp/1491950358/ref=sr_1_1?ie=UTF8&qid=1459727753&sr=8-1&keywords=building+microservices)
* [_Article de Martin Fowler_](http://martinfowler.com/articles/microservices.html)
* [_microservices.io_](http://microservices.io)
* [_Microservices @ Spotify_](https://www.youtube.com/watch?v=7LGPeBgNFuU)
* [_Défis dans la mise en œuvre des Microservices_](https://www.youtube.com/watch?v=yPf5MfOZPY0)