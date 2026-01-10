---
title: Erreur HTTP 500 – Erreur Interne du Serveur Expliquée en Français Simple
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-21T23:39:17.000Z'
originalURL: https://freecodecamp.org/news/http-error-500-internal-server-error-explained-in-plain-english
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9a24740569d1a4ca23d2.jpg
tags:
- name: http
  slug: http
seo_title: Erreur HTTP 500 – Erreur Interne du Serveur Expliquée en Français Simple
seo_desc: "By Jackson Bates\nError codes in the 4xx range mean you or your browser\
  \ did something wrong. Maybe you weren't logged in, tried to access something you\
  \ didn't have permission for, or simply got lost. \nHowever, error codes in the\
  \ 5xx range means the er..."
---

Par Jackson Bates

Les codes d'erreur dans la plage 4xx signifient que vous ou votre navigateur avez fait quelque chose de mal. Peut-être que vous n'étiez pas connecté, que vous avez essayé d'accéder à quelque chose pour lequel vous n'aviez pas la permission, ou que vous vous êtes simplement perdu. 

Cependant, les codes d'erreur dans la plage 5xx signifient que l'erreur est entièrement hors de votre contrôle (sauf si vous êtes le développeur/administrateur du serveur). Peut-être que le deuxième* code d'erreur le plus frustrant que vous pouvez rencontrer sur Internet est le redouté 500.

## Que signifie-t-il ?

Simplement, le serveur a essayé de faire quelque chose et a échoué.

Selon [RFC 7231](https://tools.ietf.org/html/rfc7231#section-6.6.1) :

> Le code d'état 500 (Internal Server Error) indique que le serveur a rencontré une condition inattendue qui l'a empêché de satisfaire la requête.

La cause de cela peut être n'importe quoi, vraiment ! 

Imaginons que vous accédez à un site web utilisant une API Laravel PHP pour son backend. 

La chose qui génère l'erreur 500 pourrait être quelque chose d'aussi simple qu'un `error_log` erroné essayant de logger un tableau au lieu d'une chaîne de caractères – quelque chose de complètement sans rapport avec votre requête, mais néanmoins une erreur que PHP lancerait et qui tuerait la requête que vous avez faite au serveur.

Habituellement, quelque chose d'aussi trivial que cela serait attrapé avant le déploiement (espérons-le), mais cela montre simplement que, en tant qu'utilisateur d'un site web ou d'une application, l'erreur est vraiment hors de votre contrôle.

## Comment la corriger ?

En tant qu'utilisateur sans accès au serveur, vous n'avez vraiment qu'une seule option :

### Informez le propriétaire du site qu'un 500 est retourné alors que vous vous attendiez à autre chose

Si vous pensez vraiment que vous devriez pouvoir accéder à la ressource en question, mais que vous voyez cette erreur, il est judicieux d'en informer l'équipe derrière le site.

Essayez de donner aux développeurs/à l'équipe de support autant d'informations que possible sur ce que vous tentiez de faire afin qu'ils puissent rapidement reproduire le problème pour identifier le bug.

Si vous vous sentez particulièrement serviable ou curieux, vous pourrez peut-être trouver plus d'indices dans l'onglet réseau des outils de développement de votre navigateur. 

Sur Firefox, vous pouvez ouvrir l'onglet réseau avec les touches de raccourci `ctrl + shift + E`. Sur Chrome, vous pouvez ouvrir les outils de développement avec `ctrl + shift + I` puis sélectionner l'onglet réseau. 

Avec cet onglet ouvert, tentez à nouveau votre requête et cherchez le code de retour 500 dans la sortie réseau. Parfois, vous pourrez voir une réponse serveur légèrement plus détaillée décrivant le problème que vous avez rencontré. Vous pouvez donner cette information aux développeurs pour accélérer la résolution du problème.

Si vous êtes le développeur, alors vous devez traquer le bug et le corriger ! Cela pourrait être n'importe quoi, donc je ne peux pas vous dire comment faire. Mais si vous êtes nouveau dans le développement, je vous recommande de commencer par chercher des indices dans les logs du serveur si le problème n'est pas déjà évident.

## Restez patient

Ayant signalé le problème, vous avez fait tout ce que vous pouviez raisonnablement faire.

* vous vous demandez quel est le code d'erreur le plus frustrant à rencontrer dans la nature ? [418 : Je suis une théière](https://en.wikipedia.org/wiki/Hyper_Text_Coffee_Pot_Control_Protocol). Si vous tombez sur cela comme une véritable erreur, cela signifie que le développeur a fait l'effort de l'implémenter comme réponse d'erreur, mais c'est une blague et cela ne vous donne pas d'information. Cela arrive.

Si vous promettez de ne jamais retourner un 418 en réponse à une véritable erreur côté client, alors vous êtes le bienvenu pour rester en contact avec moi sur Twitter [@JacksonBates](https://twitter.com/jacksonbates).