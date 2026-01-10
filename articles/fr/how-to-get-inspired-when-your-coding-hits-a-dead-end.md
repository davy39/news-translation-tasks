---
title: Comment trouver l'inspiration lorsque votre codage atteint une impasse
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-09-25T17:23:22.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-inspired-when-your-coding-hits-a-dead-end
coverImage: https://www.freecodecamp.org/news/content/images/2020/09/codinginspiration-2.png
tags:
- name: Inspiration
  slug: inspiration
- name: motivation
  slug: motivation
- name: 'self-improvement '
  slug: self-improvement
seo_title: Comment trouver l'inspiration lorsque votre codage atteint une impasse
seo_desc: "By Ryan Dawson\nHitting a dead-end is common when you're programming. It’s\
  \ common with any type of problem-solving. \nWe get stuck on a particular way of\
  \ seeing the problem and it can be difficult to achieve a new perspective. \nI recently\
  \ came across a..."
---

Par Ryan Dawson

Atteindre une impasse est courant lorsque vous programmez. C'est courant avec tout type de résolution de problèmes. 

Nous restons bloqués sur une manière particulière de voir le problème et il peut être difficile d'adopter une nouvelle perspective. 

Je suis récemment tombé sur un outil issu des arts créatifs et j'ai réalisé qu'il pouvait être adapté pour fonctionner en programmation.

L'outil qui m'a inspiré est les cartes Oblique Strategies. Ce sont des invites pour briser un cycle de pensée et nous inspirer à penser différemment. Les cartes incluent « Supprimer les spécificités et convertir en ambiguïtés » et « Utiliser une vieille idée ». 

L'une de leurs utilisations les plus célèbres a été sur l'album _Heroes_ de David Bowie. Sur la piste « Sense of Doubt », par exemple, Bowie et Brian Eno ont tourné à tour de rôle des overdubs basés sur les cartes Oblique Strategies [sans révéler à l'autre ce que leur carte avait dit](https://dangerousminds.net/comments/brian_eno_and_peter_schmidts_oblique_strategies_the_original_handwritt).

Je pense que les impasses de codage ont besoin de quelque chose de plus direct. Dans les moments où nous sommes bloqués sur un problème, nous avons besoin à la fois d'inspiration et de réassurance. 

## La solution ? La Machine à Inspiration de Codage

J'ai donc recueilli des citations sur le processus de codage d'experts – des personnes qui ont créé des langages de programmation et des systèmes d'exploitation. Et j'ai mis ces paroles sages dans un [design de Gordana Minovska](https://github.com/gminovska/RandomQuoteMachine) qui donne aux citations une place centrale.

![Image](https://lh5.googleusercontent.com/vFx4xkI63PkxfNy1UQGuiGvKYBeVl_-83ScRc68smMQSa1AgRRGi9mPtHnet_XHDYk-hZono_wHUz_F7fXY1dbYhsJ0nq24ynFU52md65YZfqmdMRd_LQR-4zYID4ZK0Vg7l0NVD)
_[https://ryandawsonuk.github.io/CodingInspirationMachine/](https://ryandawsonuk.github.io/CodingInspirationMachine/)_

Le but est d'avoir un outil pour passer de « Je ne vois aucune solution » à « peut-être que cette approche mènera quelque part » à « aha ». 

Nous restons souvent bloqués dans une perspective qui ne nous permet pas de voir les approches « peut-être ». Dans ces moments, nous pourrions utiliser quelques paroles sages d'un maître en résolution de problèmes pour nous donner un coup de pouce. 

Par exemple, ces mots de Robert C. Martin :

> Lorsque vous travaillez sur un problème, vous vous en approchez parfois si près que vous ne pouvez pas voir toutes les options. Vous ratez des solutions élégantes parce que la partie créative de votre esprit est supprimée par l'intensité de votre concentration.

L'idée est soit de mettre en favoris [l'URL](https://ryandawsonuk.github.io/CodingInspirationMachine/), soit de forker le dépôt et de configurer GitHub Pages pour héberger votre propre version. 

Avec un fork, vous pouvez changer les citations en ce que vous trouvez le plus utile. Ensuite, vous pouvez revenir à la Machine à Inspiration de Codage lorsque vous êtes bloqué.

Bien sûr, ce n'est qu'un outil d'inspiration parmi d'autres. Il ne remplacera pas d'autres outils comme le brainstorming et les cartes mentales. 

David Bowie a utilisé de nombreux outils pour s'inspirer et sa musique doit probablement plus d'inspiration aux [découpages de journaux](http://www.openculture.com/2019/05/how-david-bowie-used-william-s-burroughs-cut-up-method-to-write-his-unforgettable-lyrics.html) qu'aux cartes Oblique Strategies. 

Mais l'idée avec la Machine à Inspiration de Codage est d'avoir un outil facile et accessible pour nous rappeler qu'il est normal de rester bloqué, que c'est censé être difficile, et qu'il y aura des moyens de progresser.

## Applications réelles pour la Machine à Inspiration de Codage

Voici quelques situations que j'ai rencontrées récemment et qui m'ont fait réfléchir à cette technique.

### Devenir créatif

Il y avait un problème d'autorisation avec un système sur lequel je travaille. Le code d'autorisation qui fonctionnait avec plusieurs fournisseurs d'autorisation ne fonctionnait pas pour une configuration particulière d'Active Directory. 

Nous ne savions pas initialement si c'était un problème de configuration du côté du fournisseur, de configuration du côté de l'application, un problème de connectivité, ou un problème dans notre code. Nous avons même [construit un outil de test personnalisé](https://github.com/ryandawsonuk/oauth2-test-tool) pour réduire le problème. 

Il s'est finalement avéré que nous avions besoin d'un paramètre resource_uri supplémentaire à inclure dans l'un de nos appels http.

### Trouver une solution

Pour ce même système, nous voulions afficher des métriques sur de longues périodes. Cela nous a amenés à essayer de faire des requêtes Prometheus sur des plages de données trop grandes pour les requêtes Prometheus. 

Il existe plusieurs façons de gérer cela, allant de la modification de ce que nous interrogeons, à l'utilisation d'outils différents/plus nombreux, à la restructuration des données. Nous avons choisi ce qui revient à [restructurer les données](https://github.com/SeldonIO/seldon-core/pull/2484).

### Voir la réponse moins évidente

Mon beau-père m'a montré que sa smart TV ne fonctionnait pas avec Netflix. 

Après avoir navigué dans plusieurs menus confus et essayé divers réseaux sans fil, nous avons découvert qu'il s'agissait d'un problème de force du signal avec le réseau que la TV préférait (elle fonctionnait bien avec un réseau que la TV pensait être de force inférieure).

## Conclusion

Ces problèmes sont tous différents mais ils partagent des caractéristiques communes. 

Chacun a nécessité des recherches et des expérimentations et l'élimination de possibilités. Chacun d'eux était initialement surprenant et il a fallu du temps pour ajuster les attentes et réaliser pourquoi le problème était là. Il était nécessaire d'explorer plusieurs chemins et chaque fois qu'un chemin était infructueux, c'était décourageant. 

Il est facile de rester bloqué dans ces situations et de constater que nous ne voyons plus aucun chemin. Les mots des autres qui ont été là avant nous peuvent nous aider à voir ces situations avec un regard neuf.

Jetez un coup d'œil à la [Machine à Inspiration de Codage](https://ryandawsonuk.github.io/CodingInspirationMachine/) et n'hésitez pas à soumettre des suggestions au [dépôt github](https://github.com/ryandawsonuk/CodingInspirationMachine) ou à [me contacter sur twitter](https://twitter.com/ryandawsongb).