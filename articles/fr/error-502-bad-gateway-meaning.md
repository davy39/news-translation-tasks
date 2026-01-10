---
title: Signification de l'erreur 502 Bad Gateway
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-06-08T20:21:52.000Z'
originalURL: https://freecodecamp.org/news/error-502-bad-gateway-meaning
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/502b.png
tags:
- name: error
  slug: error
- name: http
  slug: http
seo_title: Signification de l'erreur 502 Bad Gateway
seo_desc: "When you visit a website and you get a “502 Bad Gateway” error, it means\
  \ there’s an issue with the servers powering the website.  \nOn many occasions,\
  \ this error is an issue with the website itself, so on your end, there’s nothing\
  \ you can do to solve ..."
---

Lorsque vous visitez un site web et que vous obtenez une erreur "502 Bad Gateway", cela signifie qu'il y a un problème avec les serveurs alimentant le site web. 

À de nombreuses occasions, cette erreur est un problème avec le site web lui-même, donc de votre côté, il n'y a rien que vous puissiez faire pour la résoudre. 

Mais l'erreur peut également se produire si vos adaptateurs réseau ou les paramètres réseau de votre ordinateur sont mal configurés. 

Le "502" dans l'erreur est un code de statut HTTP qui indique qu'un serveur a reçu une réponse invalide d'un autre serveur.

Google affiche l'erreur de cette manière :
![502-error](https://www.freecodecamp.org/news/content/images/2022/06/502-error.png)

Parfois, un forum populaire dans mon pays l'affiche de cette manière :
![cloudflare-502-bad-gateway-error](https://www.freecodecamp.org/news/content/images/2022/06/cloudflare-502-bad-gateway-error.png)

Il semble que les sites web alimentés par Cloudflare affichent l'erreur de cette manière.

D'autres sites web l'affichent de manière personnalisée.

## Que signifie exactement 502 Bad Gateway ?

La force de travail internationale en ingénierie (IETF) définit l'erreur 502 Bad Gateway de manière plus extensive :

> Le code de statut 502 (Bad Gateway) indique que le serveur, agissant en tant que passerelle ou proxy, a reçu une réponse invalide d'un serveur entrant auquel il a accédé en tentant de satisfaire la demande.

Le "serveur proxy" est un système ou un routeur qui agit comme une passerelle entre votre ordinateur et Internet. 

Le serveur entrant, en revanche, est celui qui transmet une connexion entrante à votre ordinateur. C'est-à-dire, un serveur web.

## Qu'est-ce qui cause une erreur Bad Gateway ?

Comme cela a été souligné précédemment, 502 Bad Gateway est une erreur de serveur tout comme d'autres erreurs de code de statut HTTP dans la plage des 500 telles que 501 (Non Implémenté), 503 (Service Indisponible), 504 (Délai de la Passerelle Écoulé), et 505 (Version HTTP non supportée).

Cette erreur de serveur particulière pourrait être due à un serveur surchargé, une erreur de programmation et de configuration backend, ou même un nom de domaine pas encore propagé.

Mais parfois, le navigateur pourrait afficher cette erreur en raison de mises à jour en retard, de bloqueurs de publicités, d'extensions de navigateur, ou de problèmes avec le serveur DNS de l'ordinateur.


## Réflexions finales 

J'espère que cet article vous aide à comprendre ce que signifie l'erreur 502 Bad Gateway.

Si vous êtes administrateur web et que vos utilisateurs se plaignent de cette erreur, vous devriez essayer de la corriger dès que possible car elle pourrait avoir un effet négatif sur le référencement de votre site web.

Si vous rencontrez cette erreur en tant qu'utilisateur, il y a de fortes chances qu'elle provienne du site web que vous essayez de visiter. Parfois, cela pourrait être dû à un routeur et des paramètres mal configurés.

Vous pouvez essayer d'actualiser la page web, de vider le cache de votre navigateur et de passer à un autre navigateur.

Pour voir comment vous pouvez résoudre l'erreur en tant qu'utilisateur, j'ai écrit [un article détaillé qui peut vous aider](https://www.freecodecamp.org/news/502-bad-gateway-error-solved/).

Merci d'avoir lu.