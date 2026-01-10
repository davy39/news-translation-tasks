---
title: Pourquoi GraphQL est l'avenir des APIs
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-08T19:07:28.000Z'
originalURL: https://freecodecamp.org/news/why-graphql-is-the-future-of-apis-6a900fb0bc81
coverImage: https://cdn-media-1.freecodecamp.org/images/1*QFl5u-rZN3dou7XDNNwuBA.png
tags:
- name: GraphQL
  slug: graphql
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: Software Engineering
  slug: software-engineering
- name: technology
  slug: technology
seo_title: Pourquoi GraphQL est l'avenir des APIs
seo_desc: 'By Leonardo Maldonado

  Since the beginning of the web, developing APIs has been a difficult task for developers.
  The way we develop our APIs must evolve with time so that we can always build good,
  intuitive and well-designed APIs.

  In the last few year...'
---

Par Leonardo Maldonado

Depuis le début du web, le développement d'APIs a été une tâche difficile pour les développeurs. La manière dont nous développons nos APIs doit évoluer avec le temps afin que nous puissions toujours construire de bonnes APIs, intuitives et bien conçues.

Ces dernières années, GraphQL a gagné en popularité parmi les développeurs. De nombreuses entreprises ont commencé à adopter cette technologie pour construire leurs APIs. GraphQL est un langage de requête développé par Facebook en 2012 et rendu public en 2015. Il a gagné beaucoup d'adeptes. Il a été adopté par de nombreuses grandes entreprises telles que Spotify, Facebook, GitHub, NYTimes, Netflix, Walmart, et bien d'autres.

Dans cette série de tutoriels, nous allons examiner GraphQL, comprendre ce que c'est, et voir quelles fonctionnalités rendent ce langage de requête si intuitif et facile à utiliser.

Alors, commençons par examiner les problèmes avec REST, et comment GraphQL les résout. Nous découvrirons également pourquoi les entreprises construisent leurs APIs avec GraphQL, et pourquoi c'est l'avenir des APIs.

### Oh, REST

Il y a longtemps, lorsque nous avons changé notre conception d'API de SOAP à REST, nous pensions que ce changement donnerait aux développeurs plus de flexibilité dans leur travail. Nous ne pouvons pas nier que cela a plutôt bien fonctionné pendant un certain temps et que c'était un bon choix à l'époque. À mesure que les applications et le web sont devenus de plus en plus sophistiqués, les APIs ont naturellement évolué également, suivant ces changements.

Cependant, REST présente de nombreux problèmes. Voyons quels sont ces problèmes :

#### Beaucoup d'endpoints

Chaque ressource dans REST est représentée par un endpoint. Ainsi, dans une application réelle, nous aurions un grand nombre d'endpoints pour un grand nombre de ressources. Si vous souhaitez faire une requête GET, vous aurez besoin d'un endpoint spécifique à cette requête, avec des paramètres spécifiques. Si vous souhaitez faire une requête POST, vous aurez besoin d'un autre endpoint juste pour cette requête.

![Image](https://cdn-media-1.freecodecamp.org/images/QaAcN24U8whrNKZNHauw8quMx2dxXTV6QJWk)

Mais, quel est le problème avec cela ? Imaginons que nous construisons une énorme application de réseau social comme Facebook. Nous allons finir avec un grand nombre d'endpoints, ce qui signifie que plus de temps de développement sera consacré au développement et à la maintenance de ces APIs.

#### Sur-récupération et sous-récupération d'informations

Un problème réel qui agace beaucoup de développeurs est la sur-récupération et la sous-récupération d'informations via les APIs REST. Cela est dû au fait que les APIs REST retournent toujours une structure fixe. Nous ne pouvons pas obtenir exactement les données que nous voulons, sauf si nous créons un endpoint spécifique pour cela.

Ainsi, si nous avons besoin d'une seule petite partie de données, nous devons travailler avec l'objet entier. Par exemple, si nous avons seulement besoin d'obtenir le `firstName`, `lastName`, et `age` d'un utilisateur dans une API REST, il n'y a aucun moyen d'obtenir exactement ces données sans récupérer l'objet entier.

![Image](https://cdn-media-1.freecodecamp.org/images/7oVDwxTOP3hSztQqeOs98Qp8jXHF-MvmqWUl)

Il y a aussi un problème avec la sous-récupération d'informations. Si nous voulons obtenir des données de deux ressources différentes, nous devons faire des appels différents à deux endpoints différents. Dans une énorme application, cela ne s'adapte pas très bien puisque des cas se présenteront où nous n'avons besoin d'obtenir qu'une partie spécifique des données, et non l'objet entier. Maintenant, imaginons que nous construisons une application qui va avoir 100 endpoints. Imaginez la quantité de travail et de code que nous devons écrire. Cela deviendra plus difficile avec le temps. Le code devient également difficile à maintenir, et les développeurs se perdent dans le processus.

#### Versioning

L'un des points douloureux dans REST, à mon avis, est le versioning. Avec les APIs REST, il est très courant de voir beaucoup d'APIs avec v1 ou v2. Dans GraphQL, il n'y a pas besoin de cela puisque vous pouvez faire évoluer vos APIs en ajoutant de nouveaux types ou en supprimant les anciens.

Dans GraphQL, tout ce que vous avez à faire pour faire évoluer votre API est d'écrire du nouveau code. Vous pouvez écrire de nouveaux types, requêtes et mutations sans avoir besoin de livrer une autre version de votre API.

Ainsi, vous ne verrez pas d'APIs GraphQL avec des endpoints comme les suivants :

```
https://example.com/api/v1/users/12312https://example.com/api/v2/users/12312
```

### Pourquoi GraphQL est l'avenir

En 2012, Facebook a été confronté à un problème lors du développement de ses applications mobiles, ce qui les a conduits à créer GraphQL. Ces problèmes sont très courants, surtout lorsque nous parlons de la conception d'APIs RESTful. Comme discuté, ces problèmes sont :

* Mauvaise performance
* Beaucoup d'endpoints
* Sur-récupération ou sous-récupération de données
* Livraison d'une autre version chaque fois que nous devons inclure ou supprimer quelque chose
* Difficulté à comprendre les APIs

Avec de nombreux concepts en tête, les développeurs de Facebook ont développé une meilleure façon de concevoir les APIs et l'ont ensuite nommée GraphQL. Basiquement, c'est le remplacement de REST, avec beaucoup d'améliorations.

Avec GraphQL, nous obtenons beaucoup de nouvelles fonctionnalités qui vous donnent des super-pouvoirs lorsque vous construisez vos APIs. Examinons-les une par une :

#### Un seul endpoint

Il n'est pas nécessaire de construire beaucoup d'endpoints ! Avec GraphQL, nous n'avons qu'un seul endpoint, et avec celui-ci, nous pouvons obtenir autant de données que nous voulons en une seule requête. Basiquement, GraphQL enveloppe toutes vos requêtes, mutations et abonnements dans un seul endpoint et les met à votre disposition. Cela améliore votre cycle de développement car vous n'avez pas besoin de faire deux requêtes pour obtenir des données de deux ressources différentes. De plus, imaginons que nous construisons une énorme application, nous n'aurons pas beaucoup d'endpoints et une tonne de code comme avec REST. Nous aurons un seul endpoint, et avec cet endpoint, nous pouvons faire autant de requêtes que nous voulons.

![Image](https://cdn-media-1.freecodecamp.org/images/HKILGdrpW082ziY6D85tJu0oHDgHuW7p1txZ)

De plus, comme je l'ai dit ci-dessus, une approche "endpoint-only" rend votre API auto-documentée puisque vous n'avez pas besoin de construire de la documentation car vos développeurs savent déjà comment l'utiliser. Ils peuvent comprendre l'API simplement en regardant le code, ou en regardant le playground. Nous allons en apprendre davantage à ce sujet plus tard (prochain tutoriel de cette série). Cela semble magique, mais c'est juste GraphQL !

#### Avec GraphQL, vous ne récupérez que les données dont vous avez besoin

Plus de sur-récupération ou de sous-récupération d'informations. Vous ne récupérez que les données dont vous avez besoin. Vous vous souvenez des problèmes de mauvaise performance dont nous avons discuté initialement ? Nous n'avons plus cela puisque GraphQL améliore la performance de votre API, surtout en cas de connexion réseau lente.

![Image](https://cdn-media-1.freecodecamp.org/images/vdFkjXxnavnLBoxg0yoY6bKV2oD1EbfmZUaf)

#### GraphQL facilite le début de la construction d'APIs et la cohérence

Beaucoup de gens pensent que GraphQL est assez compliqué car il implique un schéma et un seul endpoint. Une fois que vous commencez à développer des APIs avec, vous découvrez que c'est plus facile que vous ne le pensiez. Une API "endpoint-only" aide beaucoup lorsque vous développez votre site web/application. Cela rend votre API plus auto-documentée, et il n'est pas nécessaire d'écrire beaucoup de documentation à ce sujet.

Si vous n'utilisez pas JavaScript comme langage principal, ce n'est pas un problème. GraphQL est un langage de requête agnostique, ce qui signifie que vous pouvez l'utiliser avec n'importe quel langage. Au moment de la rédaction de ce tutoriel, GraphQL prend en charge plus de 12 langages.

### GraphQL est l'avenir

Le fait que GraphQL soit un langage de requête open source signifie que la communauté peut contribuer à son amélioration. Lorsque Facebook l'a rendu public, il a gagné beaucoup d'adeptes et d'approbation de la part des développeurs. Maintenant, GraphQL se développe rapidement alors que de plus en plus de développeurs commencent à construire des APIs avec. Cependant, certaines personnes se demandent si cela va vraiment remplacer REST ou devenir la nouvelle façon de construire des APIs pour des applications réelles.

![Image](https://cdn-media-1.freecodecamp.org/images/NjUC53CCVGcuzj5M2PTNiLRnssUJcTKRgXUz)

Au début, je pensais que GraphQL n'était qu'un battage médiatique et juste une autre façon de créer des APIs. Cependant, lorsque j'ai commencé à l'étudier, j'ai découvert que GraphQL possède les fonctionnalités essentielles nécessaires pour créer des APIs modernes pour des applications modernes car il s'intègre vraiment bien avec les stacks modernes.

Donc, si je pouvais vous dire quelque chose maintenant, ce serait : oui, **GraphQL est vraiment l'avenir des APIs**. C'est pourquoi les grandes entreprises parient sur lui.

En novembre 2018, GraphQL a créé une GraphQL Foundation, en partenariat avec la Linux Foundation. Ce langage de requête encourage ses développeurs à construire plus de documentation, d'outils et de support pour le langage. Cette fondation garantira un avenir stable, neutre et durable pour GraphQL. Donc, c'est une autre raison de considérer GraphQL comme l'avenir des APIs.

Bien sûr, il ne remplacera pas REST immédiatement car de nombreuses applications l'utilisent encore et il est impossible de les réécrire du jour au lendemain. À mesure que de plus en plus d'entreprises adoptent GraphQL, à la fois l'UX et le DX s'amélioreront.

### Conclusion

GraphQL est vraiment l'avenir des APIs, et nous devons en apprendre davantage à ce sujet. C'est pourquoi j'ai décidé de créer une série de 4 tutoriels qui montreront comment nous pouvons travailler avec le meilleur de GraphQL, en commençant par les Queries et Mutations, puis les Subscriptions, et l'Authentification.

Dans le prochain tutoriel de cette série, je vais plonger profondément dans GraphQL, montrer comment GraphQL fonctionne avec les types, et créer nos premières Queries et Mutations.

Alors, restez à l'écoute et à la prochaine !

? S[**uivez-moi sur Twitter !**](https://twitter.com/leonardomso)

_Cet article a été initialement publié sur Hashnode. Si vous aimez cet article, lisez-le là-bas aussi pour me soutenir et m'aider à écrire plus d'articles ! V[ous pouvez le lire ici](https://hashnode.com/post/why-graphql-is-the-future-of-apis-cjs1r2hhe000rn9s23v9bydoq) !_