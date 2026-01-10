---
title: Comment les requêtes Cross-Origin Resource Sharing affectent les performances
  de votre application
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-02T09:43:09.000Z'
originalURL: https://freecodecamp.org/news/the-terrible-performance-cost-of-cors-api-on-the-single-page-application-spa-6fcf71e50147
coverImage: https://cdn-media-1.freecodecamp.org/images/1*SFc7VmGOTTIKCRTiQSc96Q.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Microservices
  slug: microservices
- name: General Programming
  slug: programming
- name: ' Single Page Applications '
  slug: single-page-applications
- name: technology
  slug: technology
seo_title: Comment les requêtes Cross-Origin Resource Sharing affectent les performances
  de votre application
seo_desc: 'By Ankur Anand

  The title may lead you to think that this post is another ranting post about the
  downside of a “Single Page Application”. It is more about shedding some light on
  the performance perspective to keep in mind while designing the SPA. Espe...'
---

Par Ankur Anand

Le titre peut vous faire penser que cet article est un autre article râleur sur les inconvénients d'une "Single Page Application". Il s'agit plutôt d'éclairer la perspective de performance à garder à l'esprit lors de la conception de l'SPA. Surtout si votre SPA consomme des API de différents services de domaine.

Si vous concevez une SPA qui consomme l'API du même domaine que la SPA, alors c'est parfait. Vous pouvez sauter cet article si votre SPA ne tire des données que de l'API du même domaine.

La plupart des SPAs impliquent des "microservices". Elles consomment différents endpoints de services servis par différents domaines au sein de la SPA. Cela ajoute de la résilience, de la tolérance aux pannes et une expérience utilisateur améliorée de notre produit. Les requêtes multi-domaines deviennent inévitables à moins que nous n'adhérions strictement au même domaine d'application **API Gateway — Microservices Pattern** pour notre SPA.

![Image](https://cdn-media-1.freecodecamp.org/images/PcHWxtFEw5vzZI3anByzWY67x-uPCaIAOFd4)
_SPA + Cors ne réduit pas toujours la latence._

Imaginons que nous avons une API `GET` `/users/report/:id` servie depuis le domaine `api.example.com`. Notre SPA est servie depuis `spa.example.com`. Le `:id` signifie qu'il s'agit d'une valeur qui peut changer pour chaque requête.

Pouvez-vous deviner le problème avec la conception de l'API ci-dessus en ce qui concerne [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) (Cross-Origin Resource Sharing) et son impact sur les performances de notre SPA ?

Voici une brève introduction à CORS depuis [MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) :

![Image](https://cdn-media-1.freecodecamp.org/images/xvd3slhsPc14xXUGV4GnBNqmK8PzfJIwNSHO)

CORS est parfait tant qu'il s'agit d'une [simple requête](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS#Simple_requests) qui ne déclenche pas de [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS#Preflighted_requests) preflight. Mais le plus souvent, nous faisons des requêtes qui ne sont pas des "[simple requêtes](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS#Simple_requests)".

Cela est dû au fait que nous devons envoyer un en-tête qui n'est pas [CORS-safelisted-request-header](https://fetch.spec.whatwg.org/#cors-safelisted-request-header). Un exemple d'en-tête est `Authorization, x-corelation-id`. Fréquemment, la valeur de notre en-tête `Content-Type` est `application/json`. Ce n'est pas une valeur autorisée pour l'en-tête `[Content-Type](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Type)` pour [cors-safelisted-request-header](https://fetch.spec.whatwg.org/#cors-safelisted-request-header).

Si notre serveur `api.example.com` accepte `content-type` de `application/json`, notre domaine SPA `spa.example.com` enverra d'abord une requête HTTP par la méthode `[OPTIONS](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/OPTIONS)`. Elle est envoyée à la ressource `/users/report/12345` sur l'autre domaine `api.example.com`. Pour déterminer si la requête réelle est sûre à envoyer, l'option est envoyée en préflight. Les requêtes cross-site sont toujours préflightées de cette manière, car elles peuvent avoir des implications pour les données utilisateur.

C'est le travail du serveur `api.example.com` de laisser l'autre domaine `spa.example.com` savoir qu'il est sûr d'envoyer les données. Vous avez peut-être fait quelque chose de similaire pour CORS dans votre application.

![Image](https://cdn-media-1.freecodecamp.org/images/EPbbVhWxAMi9cCXNxD2x-L3qGSu5dACKlOIB)
_Autoriser CORS sur un serveur Express.js_

Une fois que le serveur `api.example.com` envoie la réponse appropriée de la méthode "OPTIONS" à l'autre domaine `spa.example.com`, alors seulement les données réelles avec la requête que vous essayiez de faire sont envoyées.

> _Ainsi, pour accéder à une ressource `api.example.com/users/report/12345`, **deux requêtes réelles ont été effectuées.**_

Vous pourriez dire oui. Nous pouvons utiliser l'[en-tête Access-Control-Max-Age](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS#Preflighted_requests#Access-Control-Max-Age) pour mettre en cache les résultats d'une requête préflight. La prochaine fois que nous accédons à la ressource `api.example.com/users/report/12345` depuis `spa.example.com`, il n'y a pas de requête préflight.

Oui, c'est vrai, mais rappelez-vous le titre — Le coût de performance terrible des requêtes **CORS** sur les applications monopage (SPA). Cela provient de l'API que nous consommons et de la manière dont elle a été conçue. Dans notre exemple, nous avons conçu notre API `/users/report/:id`, où `:id` signifie qu'il s'agit d'une valeur qui peut changer.

> _La manière dont le cache préflight fonctionne est par URL, pas seulement par origine. Cela signifie que tout changement dans le chemin (qui inclut les paramètres de requête) nécessite une autre requête préflight._

Ainsi, dans notre cas, pour accéder aux ressources `api.example.com/users/report/12345` et `api.example.com/users/report/123987`, cela déclenchera quatre requêtes depuis notre SPA au total.

Si vous avez un réseau lent, cela pourrait être un énorme revers. Surtout lorsqu'une requête OPTIONS prend 2 secondes pour répondre, et 2 autres secondes pour les données.

**Imaginez maintenant votre application SPA faisant des millions de telles requêtes pour différents domaines.** Cela aura un impact terrible sur les performances de votre SPA. Vous doublez la latence de chaque requête.

> _Les SPAs sont excellentes dans leur propre domaine. Mais pour consommer différents domaines, elles viennent avec leur propre coût. Si l'API est mal conçue, les problèmes de latence de votre SPA peuvent faire plus de mal que les avantages qu'elles apportent._

Il n'y a pas de solution ou de technologie qui soit entièrement bonne ou mauvaise. Connaître ses lacunes et ce qu'il faut pour la faire fonctionner est ce qui compte. C'est ce qui différencie votre application des autres.