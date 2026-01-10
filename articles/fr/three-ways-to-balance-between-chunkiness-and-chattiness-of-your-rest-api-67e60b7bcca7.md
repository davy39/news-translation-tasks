---
title: Comment équilibrer la granularité et la verbosité lors de la conception de
  votre API REST
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-02-27T21:39:58.000Z'
originalURL: https://freecodecamp.org/news/three-ways-to-balance-between-chunkiness-and-chattiness-of-your-rest-api-67e60b7bcca7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*UXNH96dwNg_hj-txjStXVQ.png
tags:
- name: api
  slug: api
- name: GraphQL
  slug: graphql
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: Comment équilibrer la granularité et la verbosité lors de la conception
  de votre API REST
seo_desc: 'By Suhas Chatekar

  One of the challenges of building any API is that you don’t know who will use your
  API, or how they will use it.

  You may have an internal consumer who calls your API over a LAN connection. This
  consumer would not mind making massive...'
---

Par Suhas Chatekar

L'un des défis de la création de toute API est que vous ne savez pas qui utilisera votre API, ni comment ils l'utiliseront.

Vous pouvez avoir un consommateur interne qui appelle votre API via une connexion LAN. Ce consommateur n'aurait pas de problème à recevoir des réponses API massives (granulaires), ou à effectuer plusieurs appels API pour obtenir toutes les différentes parties des données qu'il souhaite (verbosité).

Ou vous pouvez avoir un consommateur externe se connectant via Internet. Ce consommateur souhaiterait effectuer un petit nombre d'appels réseau. Ces consommateurs veulent également que l'API retourne juste assez de données.

![Image](https://cdn-media-1.freecodecamp.org/images/1*UXNH96dwNg_hj-txjStXVQ.png)

Les consommateurs se connectant depuis un réseau mobile sont particulièrement sensibles aux appels réseau. Pour eux, les appels réseau entraînent des frais de carrier pour leurs utilisateurs. Une grande quantité de données retournées par les API n'est pas idéale pour eux, car cela peut entraîner une utilisation importante de la batterie lors du traitement.

En tant que développeur d'API, vous ne pouvez pas décider si votre API doit être verbale ou granulaire ou aucune des deux. Les consommateurs de votre API veulent décider cela. La vérité est que la plupart des API ont des consommateurs des deux camps. Alors, comment gérez-vous ces demandes ? La réponse facile est de donner plus de pouvoir aux consommateurs de vos API. Laissez les consommateurs être aux commandes et laissez-les dire à votre API ce qu'ils veulent.

Dans cet article, je vais parler de trois techniques qui vous permettent de faire cela.

### Technique #1 : Utiliser Lazy Get pour contrôler la taille de votre charge utile

La plupart des outils de mappage objet-relationnel (ORM) ont une fonctionnalité appelée Lazy Loading. Les ORM utilisent cette fonctionnalité pour retourner uniquement l'entité de niveau supérieur lorsqu'ils exécutent un script SQL. Les entités associées ne sont pas chargées complètement, mais seulement leurs identifiants sont chargés. Lorsque l'application tente d'accéder à l'entité associée, l'ORM intervient. Il charge cette entité en utilisant son identifiant qu'il avait chargé précédemment. C'est intelligent car l'ORM ne devine pas quand l'application a besoin de quoi. Au lieu de cela, il donne à l'application la capacité de récupérer à la demande ce dont elle a besoin.

Lazy Get est similaire. Avec Lazy Get, vous ne retournez pas une ressource liée par défaut. Au lieu de cela, vous retournez une version superficielle avec uniquement les attributs de niveau supérieur remplis. Le consommateur de l'API peut

1. Instruire le serveur de retourner les ressources liées dans la même réponse
2. Récupérer les ressources liées ultérieurement en utilisant le lien retourné dans la réponse originale

Cela est mieux expliqué avec un exemple. Supposons que nous construisons une plateforme de rencontre. Les gens peuvent créer des groupes d'intérêt et organiser des rencontres en utilisant notre plateforme. Les membres de la plateforme peuvent

1. Rejoindre les groupes qu'ils aiment
2. Se connecter avec d'autres membres de la plateforme
3. Répondre aux événements organisés par divers groupes

C'est un ensemble de fonctionnalités de base que toute plateforme de rencontre peut avoir.

Cette plateforme est activée par API et nous avons une méthode API pour récupérer une ressource `member` qui ressemble à ceci.

Pour plus de concision, le code ci-dessus ne montre pas la représentation complète des ressources `memberships`, `rsvps` et `friends`. En réalité, ces ressources auront plus d'attributs que ce que je montre ici. Elles pourraient même avoir leurs propres ressources liées.

Un consommateur de cette API n'aura peut-être pas besoin de toutes ces données tout le temps. Un consommateur se connectant via un LAN accepterait volontiers beaucoup de données retournées. Mais un développeur d'applications mobiles se connectant via une connexion Internet lente ne voudrait pas de cela. Devinez quoi ? Vous pouvez implémenter Lazy Get sur cette méthode API et laisser le consommateur décider quelles données il veut recevoir. Vous faites cela en supportant un nouveau paramètre de requête nommé `expand`. Ce paramètre accepte les noms séparés par des virgules des ressources liées que le consommateur veut que le serveur retourne. Par exemple, si l'URL pour récupérer la ressource membre ci-dessus était

`[https://myapi.com/v1/member/34234](https://myapi.com/v1/member/34234)`

Si un consommateur veut uniquement les informations sur les adhésions retournées, il peut envoyer une requête à l'URL suivante

```
https://myapi.com/v1/member/34234?expand=memberships
```

C'est bien. Maintenant, le consommateur a un contrôle sur les données que le serveur retourne. Mais qu'arrive-t-il aux autres ressources, c'est-à-dire `rsvps` et `friends` ? Le serveur va-t-il simplement les exclure de la réponse ? Si le serveur les exclut, comment le consommateur obtient-il ces ressources lorsqu'il en a besoin ?

Au lieu de cela, ce que fait le serveur est exactement la même chose que ce que fait tout ORM avec sa fonctionnalité de chargement paresseux. Le serveur retourne un identifiant de la ressource à la place de la ressource complète.

Ainsi, si le consommateur décide de récupérer les ressources `rsvps` ou `friends`, tout ce qu'il a à faire est d'émettre une requête GET sur les URL correspondantes.

#### Utiliser l'hypermédia pour améliorer cela

Dans l'exemple précédent, comment un client récupérerait-il une ressource `friend` avec l'id 5678 ? Où obtiendrait-il l'URL réelle pour récupérer cette ressource ? Nous pouvons utiliser l'[hypermedia](https://en.wikipedia.org/wiki/HATEOAS) pour nous aider ici. Si vous avez déjà utilisé l'hypermédia, vous avez peut-être deviné de quoi je parle.

Vous pouvez utiliser l'une des spécifications d'hypermédia comme [Siren](https://github.com/kevinswiber/siren), [HAL](https://tools.ietf.org/html/draft-kelly-json-hal-08) ou [Collection+JSON](http://amundsen.com/media-types/collection/) pour retourner l'URL réelle de la ressource au lieu de simplement l'id. Si vous êtes encore au [Richardson Maturity Model — Niveau 2 ou inférieur](https://martinfowler.com/articles/richardsonMaturityModel.html), ne vous inquiétez pas. Vous pouvez faire ce que nous avons fait dans de tels cas. Nous ne retournons pas l'identifiant de la ressource liée. Pour nos clients, cela ne signifie rien. Nous retournons plutôt un attribut `href`. Cet attribut contient l'URL sur laquelle les clients peuvent envoyer une requête GET pour récupérer cette ressource. Voici comment notre ressource `member` apparaît avec l'attribut `href` retourné.

Et nous retournons cet attribut par défaut pour toutes nos ressources.

### Technique #2 : Utiliser une méthode API de hachage pour devenir moins bavard

Lazy Get est bon pour contrôler la taille de la charge utile de la réponse. Ne serait-il pas bon de ne pas avoir à faire cet appel API encore et encore ? C'est le cas, si le consommateur met en cache la réponse qu'il a reçue.

Un inconvénient évident de la mise en cache est que vous ne saurez pas quand votre cache devient obsolète. Le serveur peut retourner des informations d'expiration du cache dans les en-têtes de réponse. Le consommateur peut invalider le cache en fonction de ces informations. Mais tout ce que vous faites ici est de déplacer le problème du client vers le serveur. Le serveur devine toujours le dernier moment où le cache doit expirer. Pire encore, la plupart des implémentations définissent cela à une valeur par défaut.

La méthode API de hachage offre une alternative pour les applications qui

1. Ne peuvent pas compter sur la mise en cache car elles doivent toujours travailler sur une copie fraîche des données
2. Ne peuvent pas faire des appels API fréquents et lourds en raison de l'environnement dans lequel elles opèrent, c'est-à-dire les applications mobiles.

Une implémentation de la méthode API de hachage aura les éléments suivants

1. Chaque ressource qui doit supporter une méthode API de hachage doit inclure un attribut de hachage
2. La valeur de cet attribut est le hachage de la représentation de la ressource sous forme de chaîne (JSON/XML)
3. Le serveur recalcule le hachage chaque fois que l'état de la ressource change.
4. Une nouvelle méthode API pour retourner la dernière valeur de hachage pour chaque ressource

Supposons que nous voulons supporter la méthode API de hachage pour la ressource membre de notre exemple précédent. Donc, d'abord, nous ajoutons un attribut de hachage comme suit

Le serveur utilise un mécanisme de son choix pour calculer la valeur de l'attribut de hachage. Cela pourrait également être une chaîne aléatoire. Le serveur doit mettre à jour sa valeur chaque fois que l'état de la ressource change.

Ensuite, nous ajoutons la nouvelle méthode API suivante qui retourne la dernière valeur de hachage pour la ressource membre

```
https://myapi.com/v1/member/{memberid}/hash
```

Cette méthode API retourne une réponse avec le statut `200 OK`. Le corps de la réponse contient la valeur de l'attribut de hachage de la ressource membre. Le point clé ici est de rendre cette API aussi rapide que possible. Le serveur peut mettre en cache une carte de l'id de la ressource et de la valeur de hachage pour réduire le temps de réponse.

Tout ce qu'un consommateur soucieux de la bande passante doit faire maintenant est d'effectuer un appel sur la méthode API de hachage. Il peut ensuite comparer la valeur de hachage retournée avec la valeur de hachage qu'il a de la récupération précédente de la ressource. Si les valeurs de hachage sont les mêmes, alors il est sûr de supposer que la ressource n'a pas changé depuis que le consommateur l'a récupérée pour la dernière fois. Si les valeurs de hachage sont différentes, alors il est temps de récupérer la dernière valeur de la ressource.

#### Maintenir le hachage à jour en permanence

À mesure que de plus en plus de consommateurs commencent à utiliser la méthode API de hachage, il devient important de s'assurer que les hachages sont toujours maintenus à jour. Cela nécessite une réflexion appropriée et une conception optimale. Considérez les situations suivantes

1. Lorsqu'une ressource est partiellement/complètement mise à jour, le hachage doit être mis à jour
2. Si votre hachage inclut les ressources liées, chaque fois qu'une ressource est mise à jour, toutes les autres ressources qui lient cette ressource doivent mettre à jour leur hachage.
3. Lorsqu'une ressource est supprimée, la méthode de hachage pour cette ressource doit retourner un `404 Not Found` et chaque application consommateur doit gérer cette réponse pour supprimer leur copie mise en cache de la ressource

Si vous décidez d'utiliser la méthode API de hachage, pensez à ces situations dès le premier jour. Gérer ces situations comme une réflexion après coup peut être coûteux.

### Technique #3 : Utiliser GraphQL pour récupérer exactement ce dont vous avez besoin

GraphQL est un projet Open Source de Facebook. Il a commencé comme une idée il y a quelques années, mais a progressé vers une spécification bien définie maintenant. Il existe une poignée de bibliothèques pour les principales plateformes de programmation qui supportent GraphQL. Selon le [site web de GraphQL](http://graphql.org/) :

> « GraphQL est un langage de requête pour les API et un runtime pour remplir ces requêtes avec vos données existantes. GraphQL fournit une description complète et compréhensible des données dans votre API, donne aux clients le pouvoir de demander exactement ce dont ils ont besoin et rien de plus, facilite l'évolution des API au fil du temps et permet des outils de développement puissants. »

Cela ressemble à Lazy Get, mais en réalité, c'est encore plus puissant que cela. Nous verrons dans un instant comment. GraphQL facilite également la prise en charge de la méthode API de hachage sans avoir à ajouter un endpoint spécial. Avant d'entrer dans ces détails, regardons un exemple rapide de ce que GraphQL offre.

Si un consommateur d'API a besoin d'une copie superficielle de la ressource membre sans aucune ressource liée, il doit envoyer la requête GraphQL suivante

Ignorons certains détails comme l'URL de destination de cette requête et la gestion de la requête sur le serveur. Cette requête retourne les attributs spécifiés de la ressource membre ayant l'id 34342.

Si un autre consommateur veut uniquement `firstname` et `lastname`, il spécifie ces deux attributs dans sa requête. Le serveur retournera ces attributs. Vous voyez à quel point cela peut être puissant. Avec Lazy Get, vous obtenez toutes les ressources liées complètement hydratées ou aucune. Mais il n'était pas possible de supprimer certains attributs.

La capacité de GraphQL à spécifier exactement quels attributs nous voulons voir retournés nous permet de supporter la méthode API de hachage dès le départ. Un consommateur souhaitant obtenir la dernière valeur de hachage de la ressource membre dans l'exemple ci-dessus enverrait simplement la requête suivante

Rappelez-vous, il s'agit toujours du même endpoint API sur le serveur qui traite ces requêtes. Cela donne un contrôle très granulaire aux consommateurs de l'API. Les consommateurs peuvent équilibrer entre les réponses granulaires et les appels API bavards tout seuls.

**Une chose qui vaut la peine d'être mentionnée est la performance de la méthode API de hachage utilisant GraphQL**. Un principe fondamental de la méthode API de hachage est qu'elle doit retourner aussi rapidement que possible. Si nous avons notre propre implémentation de la méthode API de hachage, nous avons un contrôle total pour effectuer tout réglage fin dont nous avons besoin. Avec GraphQL, nous sommes limités par ce que la bibliothèque GraphQL que nous utilisons offre. Si vous utilisez la version GraphQL de la méthode API de hachage, assurez-vous qu'elle est optimisée pour les performances du cas d'utilisation.

#### GraphQL est tout au sujet de donner le contrôle aux consommateurs de votre API

J'ai montré deux exemples simples de ce qui est possible avec GraphQL. Mais GraphQL n'est pas limité aux simples requêtes. Vous pouvez faire

1. Spécifier des filtres supplémentaires sur les attributs comme les 10 premiers, les 30 derniers ou contient
2. Spécifier des filtres sur plus d'un attribut
3. Grouper les attributs retournés couramment dans des [fragments](http://facebook.github.io/graphql/#sec-Language.Fragments)
4. [Validation de requête](http://facebook.github.io/graphql/#sec-Validation)
5. [Paramétrer les requêtes](http://facebook.github.io/graphql/#sec-Language.Variables) en utilisant des variables
6. Changer dynamiquement le comportement de la requête en utilisant des [directives](http://facebook.github.io/graphql/#sec-Language.Directives)
7. [Mutations de données après la récupération](http://facebook.github.io/graphql/#OperationType)

Une API qui supporte pleinement GraphQL donne à son consommateur un contrôle total sur les données qu'il récupère à quel moment.

### `Consommateur d'API heureux == Développeur d'API heureux == Grande API`

L'une des façons de fournir une bonne expérience développeur est de leur donner un certain contrôle sur les API avec lesquelles ils interagissent. Lazy Get, la méthode API de hachage et GraphQL fournissent un mécanisme par lequel les développeurs d'API peuvent donner ce contrôle à leurs consommateurs.

_☞ Si vous aimez mon article, n'oubliez pas de cliquer sur ♡ pour le recommander aux autres._

_Aussi, pour être informé de mes nouveaux articles et histoires, suivez-moi sur [Medium](https://medium.com/@suhas_chatekar) et [Twitter](https://twitter.com/suhas_chatekar). Vous pouvez également me trouver sur [LinkedIn](https://www.linkedin.com/in/chatekar). Santé !_

[**Pourquoi devriez-vous utiliser les méthodes HTTP standard lors de la conception d'API REST ?**](https://medium.com/@suhas_chatekar/why-you-should-use-the-recommended-http-methods-in-your-rest-apis-981359828bf7)  
[_L'une des caractéristiques d'une bonne API REST est qu'elle utilise les méthodes HTTP standard de la manière dont elles sont censées être utilisées..._medium.com](https://medium.com/@suhas_chatekar/why-you-should-use-the-recommended-http-methods-in-your-rest-apis-981359828bf7)[**Visualiser des API complexes en utilisant API Map**](https://medium.com/@suhas_chatekar/visualising-complex-apis-using-api-map-f09f617acb32)  
[_Une image vaut mille mots..._medium.com](https://medium.com/@suhas_chatekar/visualising-complex-apis-using-api-map-f09f617acb32)