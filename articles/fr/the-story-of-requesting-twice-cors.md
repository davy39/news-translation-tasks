---
title: L'histoire de la double requête - CORS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-06-13T06:25:10.000Z'
originalURL: https://freecodecamp.org/news/the-story-of-requesting-twice-cors
coverImage: https://www.freecodecamp.org/news/content/images/2019/06/priscilla-du-preez-234144-unsplash.jpg
tags:
- name: api
  slug: api
- name: CORS
  slug: cors
- name: JavaScript
  slug: javascript
- name: REST API
  slug: rest-api
- name: web
  slug: web
- name: Web App Security
  slug: web-app-security
- name: Web Development
  slug: web-development
seo_title: L'histoire de la double requête - CORS
seo_desc: 'By Lusan Das

  The story of requesting twice, allow me to explain how it all began.

  While working on a feature, I decided to look at the network tab and observed that
  the first request was sent with method OPTIONS, and the following request after
  it wa...'
---

Par Lusan Das

L'histoire de la double requête, permettez-moi d'expliquer comment tout a commencé.

En travaillant sur une fonctionnalité, j'ai décidé de regarder l'onglet réseau et j'ai observé que la première requête était envoyée avec la méthode OPTIONS, et la requête suivante après celle-ci était la requête avec la méthode correcte, par exemple GET, POST, etc., qui retourne la charge utile attendue. Basique, deux appels pour la même requête.

Voici, regardez les captures d'écran ci-dessous

![Image](https://cdn-media-1.freecodecamp.org/images/1*W7g8e0J9fwocmwX_Ce6VWA.png align="left")

*Requête avec la méthode OPTIONS*

![Image](https://cdn-media-1.freecodecamp.org/images/1*JgwOpH3t9oTrL8Q_UM01mw.png align="left")

*Requête avec la méthode GET*

Après avoir creusé quelques documents, j'ai réalisé que c'était un comportement attendu. Cela est lié au concept de contrôle d'accès HTTP (CORS).

Pour mieux le comprendre, permettez-moi d'expliquer un peu sur CORS et les requêtes.

### Contrôle d'accès HTTP (CORS)

Le partage de ressources cross-origin ([CORS](https://developer.mozilla.org/en-US/docs/Glossary/CORS)) est un mécanisme qui utilise des en-têtes [HTTP](https://developer.mozilla.org/en-US/docs/Glossary/HTTP) supplémentaires pour permettre à un [agent utilisateur](https://developer.mozilla.org/en-US/docs/Glossary/user_agent) d'obtenir la permission d'accéder à des ressources sélectionnées depuis un serveur sur une origine (domaine) différente de celle du site actuellement utilisé.

![Image](https://cdn-media-1.freecodecamp.org/images/1*wnTTrWj5tn6VCQJHk9PHKQ.png align="left")

*Partage de ressources cross-origin (*[*CORS*](https://developer.mozilla.org/en-US/docs/Glossary/CORS)*)*

Comprenons l'image ci-dessus pour mieux comprendre CORS.

1. **Requête Same Origin:** Nous avons ouvert **domain-a.com**, où nous demandons une **image bleue** hébergée sur le serveur web **domain-a.com.** Puisque nous effectuons nos requêtes dans le même domaine, cela s'appelle une requête same-origin.

2. **Requête Cross Origin:** Nous avons ouvert **domain-a.com**, où nous demandons une **image rouge** hébergée sur le serveur web **domain-b.com.** Puisque nous effectuons nos requêtes dans des domaines différents, cela s'appelle une requête Cross-origin.

### **Requêtes simples**

Ce sont des requêtes qui n'envoient pas leur première requête avec la méthode OPTIONS. Elles ne sont envoyées qu'une seule fois.

Cela soulève sûrement la question, pourquoi la première requête aurait-elle la méthode OPTIONS si nous ne l'envoyons pas, veuillez patienter, cela sera expliqué ci-dessous dans la section préflight ☺

Mais avant cela, comprenons quels sont les points qui rendent une requête simple.

1. Les seules méthodes autorisées dans une requête simple sont:

* [GET](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/GET)

* [HEAD](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/HEAD)

* [POST](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/POST)

2. En dehors des en-têtes définis automatiquement par l'agent utilisateur (par exemple, connection, [User-Agent](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent), ou l'un des autres en-têtes avec des noms définis dans la spécification Fetch comme un "nom d'en-tête interdit"), les seuls en-têtes qui sont autorisés à être définis manuellement sont [ceux que la spécification Fetch définit comme étant un "en-tête de requête CORS-safelisted"](https://fetch.spec.whatwg.org/#cors-safelisted-request-header), qui sont:

* Accept

* Accept-Language

* Content-Language

* Content-Type

* DPR

* Downlink

* Save-Data

* Viewport-Width

* Width

3. Les seules valeurs autorisées pour l'en-tête Content-Type sont:

* application/x-www-form-urlencoded

* multipart/form-data

* text/plain

4. Aucun écouteur d'événements n'est enregistré sur un objet XMLHttpRequestUpload utilisé dans la requête.

5. Aucun objet ReadableStream n'est utilisé dans la requête.

### Requêtes préflight

Une requête préflight est un type de requête qui envoie une requête HTTP par la méthode OPTIONS à la ressource sur l'autre domaine, afin de déterminer si la requête réelle est sûre à envoyer. Les requêtes cross-site sont préflightées de cette manière car elles peuvent avoir des implications sur les données utilisateur. Cela est évident d'après les captures d'écran ci-dessus.

Pour des requêtes comme PUT, DELETE, PATCH, etc., des requêtes préflight sont envoyées.

Le diagramme ci-dessous résume très bien son fonctionnement.

![Image](https://cdn-media-1.freecodecamp.org/images/1*cYI52Rb-fWjSFiQPoCF9pQ.png align="left")

*Image Courtesy html5rocks*

Ce diagramme ouvre une porte à une toute nouvelle connaissance. Je ne peux m'empêcher d'apprécier à quel point il est bon!

> *Étrangement, même une requête GET a été observée avoir des préflights, ce qui dans mon cas était dû à la présence d'un en-tête personnalisé Authorization, ce qui peut être vu sur la capture d'écran ci-dessous*

![Image](https://cdn-media-1.freecodecamp.org/images/1*W7g8e0J9fwocmwX_Ce6VWA.png align="left")

![Image](https://cdn-media-1.freecodecamp.org/images/1*JgwOpH3t9oTrL8Q_UM01mw.png align="left")

#### La requête Preflight est-elle mauvaise?

C'est une petite requête sans corps, mais je l'ai toujours ressentie comme une gêne. C'est toujours une requête, et chaque requête a un coût, peu importe la taille de cette requête, donc je recommande définitivement d'essayer d'éviter de tels cas.

#### Comment l'éviter?

Eh bien, la solution la plus simple est d'éviter CORS, essayez de garder nos ressources et API dans le même domaine. C'est vraiment aussi simple que cela.

#### Conclusion

Il est toujours bon d'être armé de connaissances sur le fonctionnement des requêtes. Même si le coût est très faible, cela compte toujours. Économiser de petites requêtes peut rendre notre application vraiment rapide à long terme. Eh bien, je crois en l'avenir, qui est rapide et furieux.

> *Suivez-moi sur* [**twitter**](https://twitter.com/daslusan) *pour obtenir plus de mises à jour concernant les nouveaux articles et pour rester à jour dans les derniers développements frontend. Partagez également cet article sur twitter pour aider les autres à en savoir plus. Partager, c'est prendre soin ^_^*

### Quelques ressources utiles

Voici quelques liens qui ont inspiré cet article

1. [https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)

2. [https://stackoverflow.com/questions/24704638/options-request-makes-application-2x-slower](https://stackoverflow.com/questions/24704638/options-request-makes-application-2x-slower)

3. [https://stackoverflow.com/questions/29954037/why-is-an-options-request-sent-and-can-i-disable-it/29954326](https://stackoverflow.com/questions/29954037/why-is-an-options-request-sent-and-can-i-disable-it/29954326)

4. [https://www.html5rocks.com/en/tutorials/cors/](https://www.html5rocks.com/en/tutorials/cors/)