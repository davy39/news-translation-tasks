---
title: Comment choisir la meilleure technologie pour votre site web
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-25T11:01:01.000Z'
originalURL: https://freecodecamp.org/news/how-to-decide-on-the-best-technology-for-your-website-815dbb92294b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*jy6j0_07UVXY8cX4qg2XVQ@2x.png
tags:
- name: JavaScript
  slug: javascript
- name: Microservices
  slug: microservices
- name: 'tech '
  slug: tech
- name: Vue.js
  slug: vuejs
- name: Web Development
  slug: web-development
seo_title: Comment choisir la meilleure technologie pour votre site web
seo_desc: 'By Ondřej Polesný

  You know how your website is going to look and have a good idea about the content
  structure. But no one wants to maintain a set of static pages, right? Let’s take
  a look at how to make your website dynamic and easily adjustable, so ...'
---

Par Ondřej Polesný

Vous savez à quoi votre site web va ressembler et vous avez une bonne idée de la structure du contenu. Mais personne ne veut maintenir un ensemble de pages statiques, n'est-ce pas ? Examinons comment rendre votre site web dynamique et facilement ajustable, afin que, pour chaque changement, vous n'ayez pas besoin de toucher au code et à l'implémentation du site web.

Mais par où commencer ?

Devons-nous installer des outils ? Est-il judicieux d'utiliser JavaScript ou de rester avec le rendu côté serveur en utilisant MVC ou un CMS tout-en-un ? Je vais expliquer comment donner vie à vos sites web et les préparer pour l'avenir.

Vous souhaitez donc construire un site web moderne. Un site web qui est rapide, sécurisé, esthétique et offre la meilleure expérience utilisateur. Le mot moderne est clé ici, car il est également lié à notre époque trépidante. Tout le monde est occupé, nos patrons veulent que nous gérions 120 % de notre travail assigné, et il y a à peine une demi-heure pour profiter du déjeuner chaque jour. Par conséquent, créer toute la fonctionnalité du site web à partir de zéro ne correspond pas à notre scénario. L'objectif est de le mettre en place et de le faire fonctionner le plus rapidement possible et de le partager avec le monde entier, de préférence aujourd'hui.

#### Une solution tout-en-un côté serveur

L'utilisation d'une solution tout-en-un telle qu'un système de gestion de contenu (CMS) garantira que votre site web est opérationnel rapidement. Au moins sa première version. Son installation et l'accès à l'interface d'administration pour la première fois pourraient vous prendre seulement quelques minutes si vous avez déjà l'environnement de développement prêt (sinon, ajoutez quelques heures pour l'installation).

Une fois connecté, vous pouvez configurer le site web, définir la politique d'URL et commencer à créer des modèles et des mises en page basés sur le design que vous avez choisi. La mise en place des modèles et du contenu dans le CMS peut prendre du temps. Notamment, vous devez :

* apprendre le concept des modèles de chaque CMS particulier (à partir de la documentation ou de l'e-learning)
* appliquer le concept à votre design
* apprendre les meilleures pratiques pour stocker le contenu dans chaque CMS
* ajuster finement le site web pour qu'il corresponde à vos attentes

Tout cela peut être fait très rapidement si vous êtes familier avec le CMS. Mais vos premiers sites web ne seront probablement pas candidats pour le Site de l'Année. 😉

Lorsque j'ai utilisé des systèmes CMS par le passé, tôt ou tard, j'ai toujours fini par créer des contrôles personnalisés (c'est-à-dire du code personnalisé), car la sortie HTML des contrôles standard n'était pas suffisante ou allait directement à l'encontre des nouvelles normes de l'industrie, comme les [Accelerated Mobile Pages](http://bit.ly/2QEMfX1). Je considère cela comme le plus grand inconvénient des systèmes CMS, ils vous limitent de diverses manières car ils se positionnent comme le moteur principal de votre site web. Je me suis toujours retrouvé à résoudre des petites tâches 80 % du temps.

Un autre problème que j'ai rencontré presque à chaque fois était lors du déploiement. Le premier déploiement est facile, vous mettez simplement tout sur un FTP distant et restaurez la base de données sur le serveur de votre fournisseur d'hébergement. Ce sont les déploiements ultérieurs qui compliquent les choses. Bien que ces systèmes disposent généralement d'un moyen d'apporter vos modifications de développement (ou simplement locales) sur le site en direct, cela tend à faire partie des niveaux de tarification plus élevés et cela prend un certain temps à apprendre et à configurer.

#### Approche Headless

J'ai expliqué les avantages de l'architecture microservice dans [un autre article](http://bit.ly/2Duglu1). De nos jours, tout le monde appelle cette approche headless, car la partie clé de l'architecture microservice est le CMS headless (par exemple [Kentico Cloud](http://bit.ly/2QzUALM)). Il agit comme un endroit où vous stockez tout le contenu et assure la livraison. L'avantage principal est qu'il s'agit simplement d'un autre service. Vous êtes le nouveau chef de votre site web. Vous dites comment les services vont travailler ensemble et lesquels vous allez utiliser. Le CMS headless est simplement un autre service dans toute la pile. Mais comment faire cela ?

Permettez-moi de vous montrer cela sur mon site web personnel. Lorsqu'un visiteur arrive, il s'attend à voir quelque chose comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/lNhIQF0NgiekbYntIVZj8gAdJ-ca1Kq1ePeN)

La page d'accueil de mon site web est simplement un code HTML avec du contenu. Maintenant, il y a deux façons dont ce code HTML peut être créé. Soit nous restons avec l'approche standard de tout construire sur le serveur :

![Image](https://cdn-media-1.freecodecamp.org/images/Y3QJf9uDimVupmPa1FDr2nKf9mnJZ-Mefoq0)

Soit nous donnons un peu de répit à notre serveur web et composons le code HTML sur le client :

![Image](https://cdn-media-1.freecodecamp.org/images/HgaJ5JgDKX262v43hpGFUN5wLQ0luIZo5p1k)

Vous voyez, le navigateur du visiteur accepte uniquement des données, pas toute la structure HTML avec le contenu. Mais comment le navigateur sait-il quoi afficher ? Comment traiter les données et les afficher dans notre design ?

### JavaScript moderne

Nous allons dire au navigateur quoi faire via JavaScript. Par le passé, JavaScript était mal vu. Il a toujours été une règle de base que chaque fois que vous créiez une fonctionnalité JavaScript, vous deviez faire la version alternative noscript. Mais les temps ont changé et les navigateurs ont évolué. Vous devez toujours vous conformer à certaines règles afin de rendre votre site web accessible, mais nous en parlerons plus tard.

Utiliser JavaScript pour construire un site web n'a jamais été aussi facile. Il existe de nombreux frameworks qui vous aident à atteindre votre objectif même avec une connaissance minimale de JavaScript pur. Et le meilleur, c'est que pour certains d'entre eux, vous n'avez pas besoin d'installer quoi que ce soit. Juste votre navigateur et votre éditeur de texte préféré suffisent. Mais commençons par les bases et sélectionnons le meilleur framework pour nos nouveaux sites web.

Globalement, il existe 3 grands frameworks JS qui ont beaucoup d'adeptes et une grande communauté autour d'eux. Cela garantit un développement et un support continus. De nombreux sites web réussis sont construits sur eux, dont certains que vous pouvez utiliser quotidiennement.

#### 1. AngularJS

Angular a l'histoire la plus riche de ces trois. Il a été fondé il y a presque 10 ans en 2009 ! Il est développé et maintenu par Google. Comparé à d'autres frameworks, il a une syntaxe plus complexe basée sur TypeScript et vous obligera à configurer un processus de construction. Cependant, il supporte la modularité et un modèle MVVM qui permet aux applications construites sur Angular d'être très robustes.

Je me souviens l'avoir utilisé pour la première fois en 2013 pour un projet semi-gouvernemental où il nous a permis de créer un front-end rapide pour gérer toutes sortes d'entités. Il était si facile de créer des listes riches avec des fonctionnalités de pagination, de filtrage et de tri.

#### 2. ReactJS

React a été fondé et open-sourcé à l'origine par Facebook en 2013. Il est basé sur des composants, ce qui le rend facile à apprendre. Ses composants sont implémentés en utilisant la syntaxe JSX, qui se situe entre JavaScript et HTML. Il est également facile de comprendre l'architecture initiale, car chaque composant est comme un module contribuant au HTML de sortie. Si vous aimez les Legos, vous aimerez React !

Il est possible de l'inclure dans un site web en tant que bibliothèque JS ou de configurer un processus de construction et d'utiliser TypeScript. React a également la plus grande communauté et possède un frère appelé React Native qui vous permet de construire des applications mobiles natives.

#### 3. VueJS

Vue a été publié en 2014 et connaît une croissance rapide — actuellement, il obtient la plus grande augmentation d'adeptes dans la communauté. Il est très similaire à React, mais légèrement plus facile pour les débutants. Il brille par sa documentation détaillée et son intégration très facile. Les composants sont basés sur du HTML simple, ce qui le rend très facile pour les débutants en JavaScript. C'est également le plus léger de ces trois.

Je l'ai personnellement utilisé sur des scénarios de panier d'achat plus avancés dans Prestashop et j'ai été émerveillé par la rapidité avec laquelle j'ai pu tout faire fonctionner ensemble sans aucune connaissance préalable de Vue.

Si vous souhaitez examiner la comparaison en profondeur, référez-vous au excellent article de [TechMagic](http://bit.ly/2xEJpcE) ou à la [comparaison de Jens Nauhaus](http://bit.ly/2MYz1S5) sur Medium.

#### Sélectionner le bon framework

Lorsqu'il s'agit de sélectionner le bon framework, les développeurs optent généralement pour celui avec lequel ils ont une expérience précédente (si c'était une bonne expérience). Mais si vous êtes nouveau dans le développement front-end, vous devez examiner les objectifs que vous avez fixés pour votre site web. Le bon choix dépend fortement du projet que vous construisez. Permettez-moi donc de résumer mes attentes :

* Courbe d'apprentissage rapide - Je dois construire le site web le plus rapidement possible
* Implémentation légère - le site sera assez petit, donc je veux minimiser le temps de chargement
* Intégration facile - Je ne veux pas configurer des processus de construction, mais commencer à travailler sur le site web immédiatement
* Bonne documentation - chaque fois que je suis nouveau dans quelque chose, je me retrouve à parcourir la documentation tout le temps pour des cas d'utilisation spécifiques
* Routage facile - il y a plusieurs pages dans mon site web donc j'ai besoin d'un routeur pour gérer diverses URL
* Livraison de contenu simple - J'utiliserai un système Content-as-a-Service donc j'ai besoin d'un moyen facile pour obtenir du contenu en JavaScript

Vous pouvez donc voir que dans mon cas, Vue.js convient le mieux. Il est facile à utiliser et à intégrer pour les débutants et dispose d'une documentation géniale avec des tutoriels faciles. Notez vos attentes et voyez si Vue.js leur convient également.

Le dernier point sur la livraison de contenu est très important. Tous ces frameworks JavaScript vous permettent d'obtenir du contenu via une API REST, mais implémenter des appels d'API bruts sera très chronophage et n'est pas du tout amusant. Certains systèmes de CMS headless comme [Kentico Cloud](http://bit.ly/2QzUALM) fournissent un [SDK pour JavaScript](http://bit.ly/2xbiwNf) qui est un wrapper autour de la communication REST avec de nombreuses fonctionnalités supplémentaires. Cela rendra la collecte de contenu beaucoup plus facile.

L'architecture finale du nouveau site web peut ressembler à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/5Vpup0NRAEU90P2YVdBUe0VL7i03o-6MGD6c)

La première requête pour le site web est résolue en retournant un modèle HTML principal avec des fichiers JavaScript. Lorsque le navigateur commence à traiter la logique JavaScript, Vue.js sera initialisé et il donnera vie à nos composants. Chacun de ces composants agit ensuite indépendamment - affiche du HTML, récupère des données depuis le CMS headless, ou envoie des données de soumissions de formulaires à un service web de formulaires.

Cette architecture nous permet de construire nos sites web très rapidement tout en prenant du plaisir. C'est comme construire une voiture avec des Legos. Le site web sera léger, rapide et globalement, beaucoup plus rentable. Mais laissons l'économie pour un autre article. Quelle est votre expérience ? Avez-vous déjà essayé les microservices ?

#### Autres articles de la série :

1. [Comment commencer à créer un site web impressionnant pour la première fois](http://bit.ly/2Duglu1)
2. Comment choisir la meilleure technologie pour votre site web (cet article) 😉
3. [Comment dynamiser votre site web avec Vue.js et un effort minimal](http://bit.ly/2zLRE8a)
4. [Comment mélanger un CMS headless avec un site web Vue.js et payer zéro](http://bit.ly/2CyDnhX)
5. [Comment sécuriser les soumissions de formulaires sur un site web API](http://bit.ly/2P0gidP)
6. [Construire un site web super-rapide et sécurisé avec un CMS n'est pas un gros problème. Ou est-ce le cas ?](http://bit.ly/2QVSm9a)
7. [Comment générer un site web statique avec Vue.js en un rien de temps](http://bit.ly/2PN46Jy)
8. [Comment configurer rapidement un processus de construction pour un site statique](http://bit.ly/2Dv2UGS)