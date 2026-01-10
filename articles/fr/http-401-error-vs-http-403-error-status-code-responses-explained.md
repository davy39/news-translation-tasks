---
title: Erreur HTTP 401 vs Erreur HTTP 403 – Explication des codes de statut
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-24T05:00:00.000Z'
originalURL: https://freecodecamp.org/news/http-401-error-vs-http-403-error-status-code-responses-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9a15740569d1a4ca2366.jpg
tags:
- name: error handling
  slug: error-handling
- name: http
  slug: http
seo_title: Erreur HTTP 401 vs Erreur HTTP 403 – Explication des codes de statut
seo_desc: "By Jackson Bates\nWe've covered the 403 (Forbidden) HTTP Error code in\
  \ some detail before, but it also has a near identical sibling. \nSo what exactly\
  \ is the difference between the 401 (Unauthorized) and 403 (Forbidden) status codes?\
  \ Surely they mean t..."
---

Par Jackson Bates

Nous avons déjà couvert en détail le code [403 (Interdit) Erreur HTTP](https://www.freecodecamp.org/news/http-error-403-forbidden-what-it-means-and-how-to-fix-it/), mais il a également un frère presque identique.

Alors, quelle est exactement la différence entre les codes de statut 401 (Non autorisé) et 403 (Interdit) ? Ils doivent bien signifier la même chose, non ? Examinons cela de plus près !

## Normes RFC

La norme RFC la plus récente définissant le 401 (Non autorisé) est [RFC 7235](https://tools.ietf.org/html/rfc7235#section-3.1)

> Le code de statut 401 (Non autorisé) indique que la requête n'a pas été appliquée car elle manque de justificatifs d'authentification valides pour la ressource cible... L'agent utilisateur PEUT répéter la requête avec un nouvel en-tête d'autorisation ou remplacé.

Alors que le 403 (Interdit) est défini plus récemment dans [RFC 7231](https://tools.ietf.org/html/rfc7231#section-6.5.3)

> Le code de statut 403 (Interdit) indique que le serveur a compris la requête mais refuse de l'autoriser... Si des justificatifs d'authentification ont été fournis dans la requête, le serveur les considère insuffisants pour accorder l'accès.

## Causes courantes

Comme mentionné dans l'article précédent, l'erreur 403 peut survenir lorsqu'un utilisateur est connecté mais n'a pas les privilèges suffisants pour accéder à la ressource demandée. Par exemple, un utilisateur générique peut tenter de charger une route 'admin'.

Le moment le plus évident où vous rencontreriez une erreur 401, en revanche, est lorsque vous n'êtes pas connecté du tout, ou avez fourni un mot de passe incorrect.

Ce sont les deux causes les plus courantes pour cette paire d'erreurs.

## Causes moins courantes

Il existe certains cas où ce n'est pas aussi simple que cela, cependant.

Les erreurs 403 peuvent se produire en raison de restrictions qui ne dépendent pas entièrement des identifiants de l'utilisateur connecté.

Par exemple, un serveur peut avoir verrouillé certaines ressources pour n'autoriser l'accès que depuis une plage prédéfinie d'adresses IP, ou peut utiliser le géoblocage. Ce dernier peut être potentiellement contourné avec un VPN.

Les erreurs 401 peuvent se produire même si l'utilisateur entre les identifiants corrects. Cela est rare, et pourrait être quelque chose que vous ne rencontrez vraiment que lors du développement de vos propres back-ends authentifiés. Mais si l'en-tête d'autorisation est mal formé, il retournera un 401.

Par exemple, vous pourriez avoir un JWT (JSON Web Token) que vous souhaitez inclure dans l'en-tête de la requête, qui attend le format `Authorization: Bearer eyJhbGci......yJV_adQssw5c`. Si vous oubliez le mot 'Bearer' avant le JWT, vous rencontrerez l'erreur 401.

Je suis moi-même tombé sur ce problème en testant des APIs en développement avec Postman et en oubliant la syntaxe correcte pour les en-têtes d'authentification !

## C'est tout

J'espère que cela clarifie toute confusion entourant ces erreurs très similaires.

Si vous avez trouvé cela utile, ou souhaitez contester ou étendre quelque chose soulevé ici, n'hésitez pas à me contacter sur Twitter [@JacksonBates.](https://twitter.com/JacksonBates)