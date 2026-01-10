---
title: 'Erreur HTTP 403 Interdit : Ce que cela signifie et comment la corriger'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-14T00:45:34.000Z'
originalURL: https://freecodecamp.org/news/http-error-403-forbidden-what-it-means-and-how-to-fix-it
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9eb4740569d1a4ca3e9f.jpg
tags:
- name: error handling
  slug: error-handling
- name: http
  slug: http
seo_title: 'Erreur HTTP 403 Interdit : Ce que cela signifie et comment la corriger'
seo_desc: 'By Jackson Bates

  Receiving any error code while online can be a frustrating experience. While we''ve
  become accustomed to 404 Not Found pages, even to the extent that it''s become common
  to see cute placeholder pages to entertain us whenever we get los...'
---

Par Jackson Bates

Recevoir un code d'erreur en ligne peut être une expérience frustrante. Bien que nous soyons habitués aux pages 404 Not Found, au point qu'il est devenu courant de voir des pages de remplacement [mignonnes](https://toggl.com/404) pour nous [divertir](https://weemss.com/page-not-found/) chaque fois que nous nous [perdons](http://www.limpfish.com/404), l'une des erreurs les plus déroutantes est la réponse 403 : Interdit.

## Que signifie-t-elle ?

Simplement : le serveur a déterminé que vous n'êtes pas autorisé à accéder à ce que vous avez demandé.

Selon [RFC 7231](https://tools.ietf.org/html/rfc7231#section-6.5.3) :

> Le code d'état 403 (Interdit) indique que le serveur a compris la demande mais refuse de l'autoriser... Si des informations d'authentification ont été fournies dans la demande, le serveur les considère insuffisantes pour accorder l'accès.

La réponse 403 appartient à la plage 4xx des réponses HTTP : Erreurs client. Cela signifie que vous ou votre navigateur avez fait quelque chose de mal.

Si vous rencontrez cette erreur, cela signifie généralement que vous vous êtes déjà authentifié auprès du serveur, c'est-à-dire que vous vous êtes connecté, mais que la ressource que vous avez demandée nécessite quelqu'un avec des privilèges plus élevés.

Le plus souvent, vous pouvez être connecté en tant qu'utilisateur standard, mais vous essayez d'accéder à une page d'administration.

## Comment la corriger ?

En tant qu'utilisateur sans accès au serveur, vous n'avez vraiment que quelques options :

### Authentifiez-vous avec un compte plus approprié

Encore une fois, selon [RFC 7231](https://tools.ietf.org/html/rfc7231#section-6.5.3) :

> Si des informations d'authentification ont été fournies dans la demande, le serveur les considère insuffisantes pour accorder l'accès. Le client NE DOIT PAS répéter automatiquement la demande avec les mêmes informations d'authentification. Le client PEUT répéter la demande avec de nouvelles informations d'authentification ou différentes.

C'est la seule option qui vous donne un pouvoir immédiat pour rectifier le problème.

Si vous avez plusieurs comptes pour un site et que vous essayez de faire quelque chose que vous pouvez généralement faire, mais que cette fois-ci vous en êtes empêché, c'est l'option que vous devriez essayer. Connectez-vous avec votre autre compte.

Vous pouvez constater que cette option nécessite également de vider votre cache ou vos cookies, au cas où la connexion en tant qu'autre utilisateur ne suffirait pas à effacer les jetons d'authentification précédents. Mais cela est généralement inutile.

En dernier recours, vous pourriez également essayer de désactiver les extensions de navigateur qui pourraient interférer avec votre utilisation du site. Cependant, cela est peu probable, car un 403 implique que vous êtes authentifié, mais non autorisé.

### Informez le propriétaire du site qu'un 403 est retourné alors que vous ne vous y attendez pas

Si vous pensez vraiment que vous devriez pouvoir accéder à la ressource en question, mais que vous voyez toujours cette erreur, il est judicieux d'informer l'équipe derrière le site - cela pourrait être une erreur de leur part.

Une fois de plus, selon [RFC 7231](https://tools.ietf.org/html/rfc7231#section-6.5.3) :

> Cependant, une demande peut être interdite pour des raisons sans rapport avec les informations d'authentification.

Une cause courante de ce problème survenant involontairement peut être qu'un serveur utilise des listes d'autorisation ou de refus pour des adresses IP ou des régions géographiques particulières.

Ils peuvent avoir une bonne raison de bloquer votre accès en dehors de leurs paramètres strictement définis, mais cela pourrait aussi être une simple négligence.

### Abandonnez.

Peut-être que vous n'êtes tout simplement pas censé pouvoir accéder à cette ressource. Cela arrive. C'est un grand internet et il est raisonnable de s'attendre à ce qu'il y ait certaines zones qui vous soient interdites personnellement.

Vous pourriez visiter [http.cat](https://http.cat) à la place tout en réfléchissant à pourquoi votre demande originale a été [interdite](https://http.cat/403).

---

En tant que lecteur de freeCodeCamp News, vous n'êtes presque certainement pas interdit de suivre [@JacksonBates](https://twitter.com/jacksonbates) sur Twitter pour plus de contenu technologique et de programmation.