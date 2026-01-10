---
title: Comment gérer élégamment les échecs dans un client API Node.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-10-10T21:36:56.000Z'
originalURL: https://freecodecamp.org/news/how-to-gracefully-handle-failures-in-a-node-js-api-client-605673cb72ab
coverImage: https://cdn-media-1.freecodecamp.org/images/1*qMJClMkWWIHzXfOJiLf8pw.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment gérer élégamment les échecs dans un client API Node.js
seo_desc: 'By Roger Jin

  There are two facts of life: you breathe air, and errors will occur in your programs.

  We’ve all experienced trouble connecting to Wi-Fi, or had a phone call drop on us
  abruptly. Intermittent failures across internet works are statistical...'
---

Par Roger Jin

Il y a deux faits de la vie : vous respirez de l'air, et des erreurs se produiront dans vos programmes.

Nous avons tous connu des problèmes de connexion au Wi-Fi, ou eu un appel téléphonique coupé abruptement. Les échecs intermittents sur Internet sont statistiquement rares dans l'ensemble, mais ils sont toujours susceptibles de se produire. Cela signifie que pour les programmeurs, tout ce qui attend une réponse sur un réseau est sujet à des erreurs.

Je suis architecte pour un « système de gestion de contenu en tant que service » appelé [ButterCMS](https://buttercms.com/), donc j'explorerai la fiabilité en utilisant cet outil. Il se compose de :

* un tableau de bord hébergé pour les éditeurs de contenu
* une API JSON pour récupérer ce contenu
* des SDK pour intégrer ButterCMS dans du code natif.

La base de données, la logique et le tableau de bord administratif sont un service via une API web. La question est « Que pouvez-vous faire avec les erreurs inévitables dans votre client Node.js ? » Les erreurs via une API client sont susceptibles de se produire—c'est ce que vous en faites qui compte le plus.

Dans cet article, je vais expliquer comment j'ai ajouté une meilleure gestion des échecs au client JavaScript de l'API ButterCMS. À la fin de cet article, vous aurez, je l'espère, une meilleure compréhension de la façon de gérer les échecs dans vos propres clients API.

### Gestion de base des exceptions

Pour commencer, examinons un exemple de requête API pour récupérer un article de blog depuis l'API Butter :

```
butter.post.retrieve('example-post')  .then(function onSuccess(resp) {    console.log(resp.data);  });
```

Cela fonctionnera, mais cela vous laisse aveugle face à toute exception que le client peut vous lancer. Notez que l'API client utilise des [promesses](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises) pour obtenir les données du blog. Gardez cela à l'esprit, car JavaScript prend une nouvelle dimension grâce aux promesses.

Pour gérer les exceptions en utilisant une promesse, ajoutez un `catch()` à la fin.

Par exemple :

```
butter.post.retrieve('example-post')  .catch(function onError(error) {    console.log(error);  });
```

Fini ! Une promesse JavaScript gère toutes les erreurs pour vous et exécute la fonction de rappel `onError()`. L'objet `error` contient des informations très utiles sur ce qui s'est mal passé.

Si vous regardez sous le capot de l'API client ButterCMS, vous verrez qu'elle utilise [axios](https://github.com/mzabriskie/axios). Axios est un client HTTP basé sur les promesses qui fonctionne dans le navigateur et Node.js.

En examinant l'objet d'erreur Axios que vous obtenez via une promesse, vous découvrez l'objet d'erreur suivant :

```
{data:Object, status:401, statusText:'Unauthorized', headers:Object, config:Object}
```

Le code de statut HTTP vous indique quelle était l'erreur.

### Meilleure gestion des exceptions

Le type d'erreurs que vous obtenez dépendra du comportement de l'API. Par exemple, la documentation de l'API ButterCMS répertorie toutes les [réponses possibles](https://buttercms.com/docs/api/?javascript#errors). Vous pouvez obtenir un 400, un 401 ou un 404 selon la requête.

Une façon de gérer ces exceptions est de traiter chaque statut de manière différente. Par exemple, vous pourriez gérer les erreurs :

```
butter.post.retrieve('example-post')  .catch(function onError(error) {    if (error.status === 400) {      console.log('Mauvaise requête, souvent due à un paramètre requis manquant.');    } else if (error.status === 401) {      console.log('Aucune clé API valide fournie.');    } else if (error.status === 404) {      console.log('La ressource demandée n\'existe pas.');    }  });
```

En utilisant le statut HTTP comme source de vérité, vous pouvez interpréter la raison de l'erreur comme vous le souhaitez.

D'autres entreprises, comme le [client API Stripe](https://github.com/stripe/stripe-node), résolvent le problème avec un [type d'erreur](https://github.com/stripe/stripe-node/blob/master/lib/Error.js) dans la réponse. Le code de `typestatus` de l'erreur vous indique quel type d'erreur est retourné dans la réponse.

Avec tout cela, une dernière question subsiste. « Que se passe-t-il lorsque la requête réseau expire ? »

Pour une API client, toute requête sur un réseau est très risquée. La connectivité réseau peut être un luxe que l'on ne peut pas toujours se permettre.

Examinons quelle exception d'erreur vous obtenez lorsqu'elle expire. L'API client ButterCMS a une valeur par défaut de 3000 ms ou 3 secondes.

Jetez un œil à cet objet d'erreur lorsqu'il expire depuis le gestionnaire d'exceptions :

```
{code:'ECONNABORTED', message:String, stack:String, timeout:3000}
```

Comme tout bon objet d'erreur, il contient de nombreux détails sur l'exception. Notez que cet objet d'erreur est différent de celui que nous avons vu précédemment. Une différence distincte est la propriété `timeout`. Cela peut être utile pour traiter ce type d'exception de manière unique.

La question est, « Existe-t-il une manière élégante de gérer ces types d'exceptions ? »

### Gestion des erreurs réseau

Une idée est de relancer automatiquement la requête après son échec. Tout ce qui attend une réponse réseau peut échouer. L'échec se produit en raison de circonstances hors de votre contrôle direct. En tant que développeurs, il est agréable d'être en contrôle, mais la vie vient avec de nombreuses exceptions.

[Polly-js](https://github.com/mauricedb/polly-js) peut tenter de relancer l'action une fois qu'il détecte une erreur. La bibliothèque polly-js peut gérer les exceptions via une promesse JavaScript. Cette promesse attrape l'exception au cas où toutes les tentatives échouent et exécute le `catch()`. Mais, nous avons décidé de ne pas utiliser polly-js car c'est une dépendance supplémentaire qui alourdit l'API client.

Un principe de conception en jeu ici est : « Un peu de copier-coller est mieux qu'une dépendance supplémentaire. » La majeure partie de la logique de relance est minimale et contient exactement ce dont nous avons besoin pour résoudre le problème.

Le cœur des relances automatiques retourne une promesse JavaScript :

```
function executeForPromiseWithDelay(config, cb) {  return new Promise(function (resolve, reject) {    function execute() {      var original = cb();
```

```
original.then(function (e) {        resolve(e);      }, function (e) {        var delay = config.delays.shift();
```

```
if (delay && config.handleFn(e)) {          setTimeout(execute, delay);        } else {          reject(e);        }      });    }
```

```
execute();  });}
```

La promesse encapsule les fonctions de rappel `resolve` et `reject` pour les relances automatiques. La fonction de rappel `config.handleFn()` détermine quelle condition entraînera une relance. La méthode `config.delays.shift()` supprimera le premier élément de la liste et retardera la prochaine tentative.

La bonne nouvelle est qu'elle peut répondre à une condition spécifique avant toute relance. La bibliothèque dispose d'une fonction `handle()` pour définir la fonction de rappel qui évalue la condition. Vous lui indiquez combien de relances, donnez la condition et la gestion finale des exceptions.

L'API client ButterCMS dispose de capacités de `retry` dès la sortie de la boîte. Pour activer les relances automatiques, vous avez besoin de ceci :

```
butter.post.retrieve('example-post')  .handle(function onError(error) {    // Ne relancer qu'en cas de timeout    return error.timeout;  })  .executeWithAutoRetry(3)  .then(function onSuccess(resp) {    console.log(resp.data);  })  .catch(function onTimeoutError(error) {    if (error.timeout) {      console.log('La requête réseau a expiré.');    }  });
```

La méthode `executeWithAutoRetry()` échelonne les requêtes suivantes et relance en cas d'échec. Par exemple, la première tentative échouera puis attendra 100 ms avant la deuxième tentative. La deuxième tentative, si elle échoue, attendra 200 ms avant la troisième. La troisième tentative attendra 400 ms avant la quatrième et dernière tentative.

Avec le client API ButterCMS, vous disposez désormais d'une manière élégante de gérer les exceptions basées sur les promesses. Tout ce que vous avez à faire est de le configurer à votre guise.

### Conclusion

En matière d'erreurs, vous pouvez soit enterrer votre tête dans le sable, soit gérer l'inattendu avec grâce et élégance. Toute API client qui attend une réponse via une connexion est sujette aux exceptions. Le choix vous appartient de savoir quoi faire lorsque des comportements erratiques se produisent.

Considérez une exception comme un comportement imprévisible. Sauf que, parce qu'il est imprévisible, cela ne signifie pas que vous ne pouvez pas vous préparer à l'avance. Lors de la gestion des exceptions, concentrez-vous sur l'anticipation de ce qui s'est mal passé, et non sur la logique de l'application.

La connectivité réseau est l'un des pires responsables des échecs. Assurez-vous de vous préparer à l'avance, pour donner une seconde chance aux requêtes en cas de connexion échouée.

Cet article a été initialement publié sur notre [blog](https://buttercms.com/blog/how-to-gracefully-handle-failures-in-a-nodejs-api-client).

Pour plus de contenu comme celui-ci, suivez ButterCMS sur [Twitter](https://twitter.com/buttercms/).