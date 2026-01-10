---
title: Les avantages de l'architecture RESTful – Qu'est-ce que REST et pourquoi vous
  devriez l'apprendre
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-12-31T23:10:37.000Z'
originalURL: https://freecodecamp.org/news/benefits-of-rest
coverImage: https://www.freecodecamp.org/news/content/images/2020/12/1_sPLooWMag11pjZnzYXIQCA.png
tags:
- name: REST
  slug: rest
- name: REST API
  slug: rest-api
seo_title: Les avantages de l'architecture RESTful – Qu'est-ce que REST et pourquoi
  vous devriez l'apprendre
seo_desc: 'By Yiğit Kemal Erinç

  In this article, we will take a look at Representational State Transfer (REST) principles
  to learn what they are and what benefits you can get from applying them.

  I believe it is important to understand why you''re learning someth...'
---

Par Yiğit Kemal Erinç

Dans cet article, nous allons examiner les principes de Representational State Transfer (REST) pour apprendre ce qu'ils sont et quels avantages vous pouvez en tirer en les appliquant.

Je crois qu'il est important de comprendre pourquoi vous apprenez quelque chose – y compris REST. Alors, examinons ce que les principes REST apportent.

## Qu'est-ce que REST ?

Representational State Transfer (REST) est un style architectural qui a gagné beaucoup de popularité ces dernières années en raison de sa simplicité et de sa scalabilité. 

Avant que REST ne devienne populaire, SOAP était la méthode de facto pour accéder aux ressources et communiquer sur le web.

## Pourquoi devriez-vous vous soucier de REST ?

Dans cette section, je vais discuter de l'importance des principes REST et pourquoi il vaut la peine de faire l'effort d'en apprendre davantage à leur sujet. Vous apprendrez également comment les appliquer à vos projets backend.

### 1) REST est facile à comprendre et à implémenter

REST est conçu pour fonctionner sur HTTP (en fait, HTTP a été influencé par REST). Par conséquent, il utilise des verbes HTTP que la plupart d'entre nous connaissent, tels que GET, POST et PUT. 

Même si vous ne savez pas ce que ces verbes signifient, leurs noms sont assez explicites. De plus, la séparation claire du code client et serveur facilite le travail de différentes équipes sur différentes parties (frontend ou backend) des applications.

Puisqu'il est facile à comprendre et aussi à implémenter, les principes REST peuvent aider à augmenter la productivité de votre équipe de développement. Ils sont également importants si vous allez publier une API publique pour que les gens développent des applications. 

Beaucoup de gens connaissent REST et HTTP, il sera donc beaucoup plus facile pour eux de comprendre et d'utiliser votre API.

![Comment garder votre équipe de développeurs heureuse : Lead Dev New York 2019 | Blog Arc](https://ucarecdn.com/f9a4640d-ba7f-4f85-82eb-901a56362a9a/)
_Développeurs heureux_

### 2) REST rend votre application plus scalable

Il y a 2 raisons principales pour lesquelles REST peut aider à rendre votre application plus scalable :

#### Pas d'état

Comme nous le verrons dans la section suivante (Principes de REST), l'un des principes fondamentaux de REST est qu'il est sans état côté serveur. Par conséquent, chaque requête sera traitée indépendamment des précédentes.

Dans les applications avec un état côté serveur ou des sessions, une session est stockée pour chaque utilisateur connecté. Ces données de session peuvent facilement devenir volumineuses et commencer à occuper beaucoup de ressources sur le serveur. 

D'autre part, les serveurs sans état n'occupent des ressources (mémoire) que lorsqu'ils traitent une requête et les libèrent dès que la requête est traitée.

Puisque la tendance actuelle en matière de scalabilité est le scaling horizontal (typiquement dans le cloud), le stockage des sessions côté serveur peut également rendre difficile la mise à l'échelle de votre application car cela crée certains problèmes difficiles. 

Par exemple, supposons que vous avez plusieurs serveurs qui fonctionnent derrière un équilibreur de charge. Que se passera-t-il si le client arrive sur le serveur1 lors de sa première requête (le serveur1 a maintenant la session du client) et, plus tard, en raison de la charge sur le serveur1, le client arrive sur le serveur2 qui ne connaît pas les données de session précédentes stockées sur le serveur1 ? Bien sûr, ce problème a des solutions, mais il rend la scalabilité plus difficile.

#### Format d'échange de données plus rapide

Les API RESTful utilisent généralement JSON comme format d'échange de données. JSON est beaucoup plus compact et plus petit en taille par rapport à XML. Il peut également être analysé plus rapidement que XML. ([source](http://ijcsn.org/IJCSN-2014/3-4/JSON-vs-XML-A-Comparative-Performance-Analysis-of-Data-Exchange-Formats.pdf))

Bien qu'ils fonctionnent principalement avec JSON, gardez à l'esprit que les API REST peuvent toujours répondre avec différents formats en utilisant l'en-tête [Accept](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Accept).

### 3) La mise en cache est plus facile avec REST

La mise en cache est un facteur critique pour la scalabilité et les performances d'une application web moderne. Un mécanisme de cache bien établi (avec les meilleurs taux de succès possibles) peut réduire considérablement le temps de réponse moyen de votre serveur.

REST vise à faciliter la mise en cache. Puisque le serveur est sans état et que chaque requête peut être traitée individuellement, les requêtes GET doivent généralement retourner la même réponse indépendamment des précédentes et de la session.

Cela rend les requêtes GET facilement mise en cache et les navigateurs les traitent généralement comme telles. Nous pouvons également rendre nos requêtes POST mise en cache en utilisant les en-têtes **Cache-Control** et **Expires**. 

### 4) REST est flexible

Par flexibilité, j'entends qu'il est facile à modifier et qu'il est également capable de répondre à de nombreux clients qui peuvent demander différents types de données (XML, JSON, etc.). 

Le client peut spécifier le type en utilisant l'en-tête **Accept** (comme je l'ai mentionné précédemment) et l'API REST peut retourner différentes réponses en fonction de cela.

Un autre mécanisme qui mérite d'être mentionné est [HATEOAS](https://www.wikiwand.com/en/HATEOAS#:~:text=Hypermedia%20as%20the%20Engine%20of,provide%20information%20dynamically%20through%20hypermedia.). Si vous ne connaissez pas le terme, ne vous inquiétez pas, cela signifie simplement : Retourner les URLs liées dans la réponse du serveur pour une ressource particulière. 

Jetez un coup d'œil à cet exemple de Wikipedia. Le client demande des informations de compte avec `account_number` à une API bancaire et obtient cette réponse :

```

{
    "account": {
        "account_number": 12345,
        "balance": {
            "currency": "usd",
            "value": 100.00
        },
        "links": {
            "deposit": "/accounts/12345/deposit",
            "withdraw": "/accounts/12345/withdraw",
            "transfer": "/accounts/12345/transfer",
            "close": "/accounts/12345/close"
        }
    }
}
```

Ce serveur utilise HATEOAS et retourne les liens pour les actions correspondantes. Cela rend très facile l'exploration de l'API et la rend flexible en permettant au serveur de changer les endpoints.

Pensez à cela : si le serveur n'appliquait pas HATEOAS, le client devrait coder en dur les endpoints comme "/accounts/:account-id/deposit". Mais si le serveur change l'URL en "/accounts/:account-id/depositMoney", le code client doit également être modifié. 

Avec l'aide des liens HATEOAS, le client peut vérifier le lien en analysant ce JSON et faire facilement la requête. Si l'endpoint change, ils recevront le nouveau sans avoir besoin de changer le code client.

Pour plus d'informations sur ce sujet, vous pouvez consulter [cet](https://roy.gbiv.com/untangled/2008/rest-apis-must-be-hypertext-driven) article de blog de Roy Fielding lui-même.

## Conclusion

Dans cet article, j'ai essayé d'exprimer pourquoi j'apprécie REST et pourquoi je crois que vous devriez l'apprécier également. J'espère qu'après avoir lu cela, les raisons d'appliquer les normes REST sont maintenant plus claires pour vous.

Cet article peut servir de motivation pour en apprendre davantage sur le sujet. Et j'ai une bonne nouvelle : je prévois d'écrire sur les meilleures pratiques REST et les erreurs courantes dans un avenir proche. 

Si vous êtes intéressé, vous pouvez garder un œil sur ou vous abonner à mon [blog](http://erinc.io/). Vous pouvez également consulter mes publications précédentes là-bas :)

Si vous avez des questions ou souhaitez discuter davantage du sujet, vous pouvez me contacter librement.

Passez une bonne année et merci pour votre lecture. :)