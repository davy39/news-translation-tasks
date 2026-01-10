---
title: Comment obtenir un nouveau jeton d'accès en utilisant Redux Observables et
  l'API de jeton de rafraîchissement
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-22T16:21:31.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-a-new-access-token-using-redux-observables-and-the-refresh-token-api-d38d875a8add
coverImage: https://cdn-media-1.freecodecamp.org/images/1*0nvsQXICkyKVMAq4hbYRPg.jpeg
tags:
- name: api
  slug: api
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: Comment obtenir un nouveau jeton d'accès en utilisant Redux Observables
  et l'API de jeton de rafraîchissement
seo_desc: 'By Sachin Kumar

  This article is about how I handled a 401 status code on an API response. I will
  show you how to get a new access token using the refresh token with Redux Observable
  in a React project.

  However before we begin, we should understand so...'
---

Par Sachin Kumar

Cet article explique comment j'ai géré un code de statut 401 sur une réponse d'API. Je vais vous montrer comment obtenir un nouveau jeton d'accès en utilisant le jeton de rafraîchissement avec [**Redux Observable**](https://redux-observable.js.org/) dans un projet [React](https://reactjs.org/).

Cependant, avant de commencer, nous devons comprendre certains concepts préalables qui nous aideront à mieux comprendre la solution. Il s'agit d'une solution architecturale générale à un problème courant, vous n'avez donc pas besoin de connaître [**Redux**](https://redux.js.org/) pour continuer. Commençons !

### **Jeton d'accès**

> Un jeton d'accès est une information d'identification qui peut être utilisée par une application pour accéder à une API. Lorsqu'un jeton d'accès expire, il renvoie un code de statut **401** dans la réponse d'erreur. 
> Le schéma suivant montre comment un jeton d'accès fonctionne avec le serveur. — [auth0.com](https://auth0.com/docs/tokens/access-token)

![Image](https://cdn-media-1.freecodecamp.org/images/1*SSh_IFE-CEs5dUV2UGleNg.png)
_L'API reçoit le jeton d'accès du serveur d'authentification._

Voici comment un service d'authentification fonctionne lorsque l'utilisateur se connecte avec succès et récupère un jeton d'accès et rafraîchit le jeton après une authentification réussie.

### **Jeton de rafraîchissement**

> Un jeton de rafraîchissement est un type spécial de jeton qui peut être utilisé pour obtenir un nouveau jeton d'accès — qui permet d'accéder à une ressource protégée — à tout moment. Vous pouvez demander de nouveaux jetons d'accès jusqu'à ce que le jeton de rafraîchissement soit blacklisté. Les jetons de rafraîchissement doivent être stockés de manière sécurisée par une application car ils permettent essentiellement à un utilisateur de rester authentifié indéfiniment. — [auth0.com](https://auth0.com/docs/tokens/access-token)

Nous devons obtenir un nouveau jeton d'accès en utilisant ce jeton de rafraîchissement, puis appeler à nouveau la même API avec le nouveau jeton d'accès. Nous voulons faire cela sans que l'utilisateur sache que sa session a expiré ou que l'API a renvoyé une erreur.

Comprenons comment le jeton de rafraîchissement fonctionne avec le serveur. Nous récupérons un nouveau jeton d'accès lorsque l'API renvoie un code de statut 401.

![Image](https://cdn-media-1.freecodecamp.org/images/1*G0SuCVnu90Q5suy0qQiJaA.png)
_C'est ainsi qu'un jeton de rafraîchissement reçoit un nouveau jeton en utilisant le jeton d'accès_

L'appel à l'API de rafraîchissement du jeton reçoit un nouveau jeton d'accès du serveur d'authentification en utilisant le jeton de rafraîchissement enregistré lors de la première authentification.

Nous pouvons mieux comprendre ce processus grâce à ce simple schéma.

![Image](https://cdn-media-1.freecodecamp.org/images/1*5vWZxAH-ffLyThTCwTp9ww.png)

### **Observables**

Vous pouvez considérer un observable comme un tableau dont les éléments arrivent de manière asynchrone au fil du temps. **Les observables vous aident à gérer des données asynchrones**, telles que les données provenant d'un service backend.

Dans RxJS, cela peut devenir assez complexe lorsque l'on manipule des flux observables. Ne vous inquiétez pas — nous allons simplifier cela avec des extraits de code simples.

Commençons par un simple appel d'API dans redux-observable. Voici à quoi ressemble une fonction simple pour une API fetch :

### Solution

Maintenant que nous avons les concepts de base, voyons comment nous pouvons gérer un code de statut 401 (invalid_token ou session expirée) sur une réponse d'API. Nous verrons également comment obtenir le nouveau jeton d'accès en utilisant le jeton de rafraîchissement dans Redux Observable.

Nous devons apporter deux modifications à la fonction ci-dessus :

1. Envelopper notre appel d'API dans Observables.defer(). Nous voulons obtenir cette fonction pour l'appeler à nouveau lorsque le nouveau jeton d'accès valide est reçu.
2. Lorsque nous recevons un statut 401 dans catch error. Nous devons faire un appel d'API pour obtenir le nouveau jeton d'accès. Nous utilisons le jeton de rafraîchissement stocké lors de la première authentification réussie.

Voyons les différences entre les deux fonctions :

1. La fonction catch donne toujours la **source** du flux parent. Nous pouvons l'utiliser pour redémarrer le flux qui a échoué en raison d'un jeton d'accès invalide.
2. Démarrez maintenant un nouveau flux d'événements pour écouter les événements de succès du jeton de rafraîchissement. Nous nous arrêtons lorsque l'API du jeton de rafraîchissement échoue (utilisez takeUntil pour cela).
3. Assurez-vous maintenant d'utiliser l'opérateur **take** pour toujours obtenir le premier événement du flux. Si vous avez plusieurs flux, votre flux de sortie peut être compromis.
4. Si le nouveau jeton d'accès a été reçu, utilisez mergeMap pour fusionner la source du flux précédent. Nous le fusionnons à nouveau avec le flux parent, et il appellera la fonction get data avec le nouveau jeton d'accès.
5. Vous vous demandez peut-être comment merge fonctionne. Donc, merge appelle indépendamment et démarrera son propre flux pour récupérer le nouveau jeton d'accès en utilisant le jeton de rafraîchissement (voir la fonction suivante). Lorsque le succès du jeton de rafraîchissement apparaît, il passera à **l'étape 2** et ainsi de suite.

Nous pouvons utiliser cette approche pour gérer d'autres cas spéciaux pour différents codes de statut tels que 500, 403.

**ProTip** : assurez-vous de vérifier la condition de boucle infinie si l'API du jeton de rafraîchissement renvoie un 401. Vous pouvez maintenir un compteur à chaque appel de jeton de rafraîchissement. Si le nombre dépasse, arrêtez le flux. Ensuite, effectuez une gestion d'erreur, par exemple en affichant un message indiquant qu'une erreur s'est produite, et déconnectez l'utilisateur.

### Conclusion

Nous avons implémenté un gestionnaire de jeton invalide en utilisant une API de jeton de rafraîchissement avec Redux-observables dans React. Cette approche peut être utilisée pour gérer d'autres cas spéciaux d'API également.

_J'espère que vous avez apprécié cet article, si vous l'avez aimé, suivez-moi sur [Twitter](https://twitter.com/_i_am_sachin) et [Github](https://github.com/sachinKumarGautam) pour plus de conseils et d'articles sur JavaScript. ?_

### Quelques ressources utiles

1. [https://redux-observable.js.org/](https://redux-observable.js.org/)
2. [https://rxjs-dev.firebaseapp.com/api](https://rxjs-dev.firebaseapp.com/api)
3. [https://rxjs-dev.firebaseapp.com/api/index/function/defer](https://rxjs-dev.firebaseapp.com/api/index/function/defer)
4. [https://rxjs-dev.firebaseapp.com/api/index/function/merge](https://rxjs-dev.firebaseapp.com/api/index/function/merge)