---
title: Comment j'ai construit un remplacement pour Heroku et réduit mes coûts de plateforme
  par 4
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-10T07:15:41.000Z'
originalURL: https://freecodecamp.org/news/how-i-cut-my-heroku-cost-by-400-5b9d0220ce13
coverImage: https://cdn-media-1.freecodecamp.org/images/1*7BLMBLZSSgAeaxDPP9MS3A.png
tags:
- name: Docker
  slug: docker
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment j'ai construit un remplacement pour Heroku et réduit mes coûts
  de plateforme par 4
seo_desc: 'By Kasra Bigdeli

  You can skip to What Does it Do section if you want to get directly to the business.

  2019 UPDATE: CaptainDuckDuck is now rebranded and distributed as CapRover. See https://github.com/caprover/caprover

  The Pain

  A couple of years ago, ...'
---

Par Kasra Bigdeli

*Vous pouvez passer directement à la section **Que fait-il ?** si vous souhaitez aller directement à l'essentiel.*

**MISE À JOUR 2019** : *CaptainDuckDuck est maintenant rebrandé et distribué sous le nom de CapRover. Voir* [https://github.com/caprover/caprover](https://github.com/caprover/caprover)

### La Douleur

Il y a quelques années, j'ai commencé à jouer avec des langages côté serveur — principalement Node JS. Après quelques jours de lutte, j'ai réussi à déployer une application Hello World sur mon `localhost`. C'était amusant, jusqu'à ce que je décide de franchir l'étape suivante et de déployer l'un de mes projets sur Internet afin que les gens puissent y accéder depuis une URL publique comme `http://www.some-awesome-web-app.com`.

À ce moment-là, j'ai réalisé qu'il y avait tout un nouvel ensemble de technologies que je devais apprendre pour déployer mon application web. Je devais savoir comment construire des outils et des pipelines de déploiement, comment fonctionnent le routage nginx et le SSL, et bien d'autres choses...

![Image](https://cdn-media-1.freecodecamp.org/images/hBdlbmkSkNYy0mEVC8cVeOp0uMtaWYVEGGme)

Inutile de dire que le déploiement était une expérience douloureuse. J'ai réalisé que je devais passer presque autant de temps à déployer le code sur le serveur, à construire, à installer des dépendances et à maintenir le serveur qu'à coder. C'est simplement stupide ! Je devais passer du temps à faire encore et encore les mêmes choses.

Je préférerais passer mon temps à coder un produit/service qui sera utilisé par des utilisateurs, plutôt que de passer des heures et des jours à configurer HTTPS. Après tout, mon HTTPS n'est pas différent des centaines de milliers d'autres sites HTTPS sur Internet. Il devait y avoir une solution plus simple.

### Le Sauveur Temporaire

Cette expérience douloureuse a pris fin lorsque j'ai découvert Heroku, une plateforme prête à l'emploi pour déployer des applications. Je me suis dit « Super ! C'est ce dont une plateforme de déploiement a besoin ! ». J'ai adoré la façon dont ils ont abstrait toute la complexité derrière une interface facile. Vous pouvez simplement créer une application avec un simple clic et la pousser. Elle devient immédiatement disponible avec une URL publique. Elle est disponible gratuitement avec un petit coût de mise en veille après 30 minutes d'inactivité. Les choses ne pouvaient pas être meilleures !

Tout allait bien. Jusqu'à ce que je me lance dans des projets qui nécessitaient une exécution continue 24h/24 (un bot lecteur). J'ai dû passer à la version payante. Ce n'était pas trop mal, seulement 7 $ par mois. Mais les choses ont commencé à devenir folles après avoir déployé de plus en plus d'applications. Certaines étaient des projets personnels, et d'autres étaient liées à des activités professionnelles qui nécessitaient soit plus de 512 Mo (limite gratuite) de RAM, soit une disponibilité continue 24h/24.

Il n'a pas fallu longtemps pour que je réalise que je payais plus de 100 $ à Heroku. Cela n'avait tout simplement pas de sens. Certains de mes bots lecteurs qui nécessitent une disponibilité 24h/24 ne consomment que 128 Mo de RAM. Pourtant, je devais payer pour la RAM inutilisée également. Je ne pouvais pas partager la RAM/CPU entre les applications. C'est pire avec les applications à forte utilisation de RAM. Si j'ai une application qui nécessite 1 Go de RAM — je dois payer au minimum 50 $ par mois.

![Image](https://cdn-media-1.freecodecamp.org/images/JiDh9qsFhOCgnfjVNo699m7Paz8lIqKXF4FN)

Espérant trouver de meilleures offres, j'ai commencé à regarder AWS, Digital Ocean, Vultr et autres fournisseurs de serveurs. Les prix que j'ai vus m'ont simplement soufflé l'esprit. Sur Digital Ocean, par exemple, je pouvais obtenir un serveur avec 2 Go de RAM pour 20 $ par mois. Je pouvais faire tenir 2 instances de mon application nécessitant 1 Go de RAM dans cette machine pour 20 $ au lieu de 100 $. **Je pouvais réduire mes coûts par 4 !**

Il y a un piège à ce prix moins cher. Si vous ne savez pas ce que c'est, vous n'avez pas lu le premier paragraphe, *La Douleur*. Le problème avec l'utilisation de ces fournisseurs de serveurs basiques (par opposition à des services comme Heroku) est que je dois faire tout le travail que Heroku faisait pour moi.

### À la Recherche du Sauveur Éternel

Je savais ce que je voulais : j'avais besoin de quelque chose qui transforme un serveur basique (comme AWS ou Digital Ocean) en une plateforme de type Heroku. À mesure que j'acquérais plus d'expérience, je savais qu'il devait y avoir une sorte d'équivalent open-source à Heroku quelque part sur GitHub. Effectivement, j'avais raison. Il n'y en a pas seulement un, mais une tonne.

Cependant, après avoir passé une heure ou deux avec chacun, j'ai réalisé qu'aucun d'entre eux n'était la solution vraiment facile comme Heroku que je recherchais. Certains étaient super basiques et n'avaient qu'une fine couche d'interface avec peu ou pas de documentation. D'autres étaient extrêmement avancés avec une tonne de fonctionnalités que je n'utilisais pas. Et avoir ces fonctionnalités signifiait simplement un processus de configuration et de maintenance compliqué. Je cherchais une solution à la fois facile et performante.

### Construire le Sauveur Éternel

Puisque je n'ai pas eu de chance à trouver un bon remplacement pour Heroku, j'ai décidé d'en construire un. Heureusement, tous les outils dont j'avais besoin étaient disponibles gratuitement — du serveur web HTTP nginx pour le routage des requêtes, à Docker pour la conteneurisation des applications, et ainsi de suite.

Après quelques mois de planification, de conception, de construction, de suppression et de recommencement à zéro, le projet était prêt.

J'ai publié la version initiale de CaptainDuckDuck en octobre 2017. Cela ne fait que deux mois et il y a eu une tonne de retours positifs. Après la première version, qui était principalement pour le déploiement d'applications web, la communauté a demandé plus. Ils voulaient principalement la possibilité de déployer des bases de données et des applications en un clic. Juste cette semaine, j'ai publié la version 0.2.1 avec toutes ces fonctionnalités demandées :)

### Que fait-il ?

Mon objectif était de permettre à un développeur d'applications web typique de créer une instance de serveur de type Heroku en moins de 10 minutes. Je suis heureux de dire que j'y suis parvenu !

Vous copiez et collez simplement une ligne sur votre serveur et vous aurez votre propre Heroku.

* Vous pouvez déployer des applications web (nodejs, php, etc.) avec une simple commande CLI de déploiement.
* Vous pouvez activer HTTPS en cliquant simplement sur le bouton « Activer HTTPS ».
* Vous pouvez choisir parmi des applications/bases de données en un clic comme WordPress, MongoDB, MySQL, Parse et autres.
* Vous pouvez connecter plusieurs serveurs pour créer un cluster de serveurs simplement en entrant les adresses IP et les identifiants des serveurs dans l'interface web.

CaptainDuckDuck est écrit en NodeJS. Mais ce n'est pas le NodeJS avec lequel vos utilisateurs finaux interagissent. Les principaux moteurs que Captain utilise sous le capot sont nginx et docker. Tous deux sont parmi les outils les plus fiables, prêts pour la production. La partie NodeJS de CaptainDuckDuck n'est utilisée que lors du déploiement d'une application sur le serveur. Théoriquement, vous pouvez tuer le processus CaptainDuckDuck dans votre serveur après le déploiement et les utilisateurs ne remarqueront aucun changement.

### Tutoriel

Si vous voulez un guide complet, je recommande de regarder le [tutoriel vidéo](https://www.youtube.com/watch?v=576RsaocNUE) et de lire la [page GitHub](https://github.com/githubsaturn/captainduckduck). La vidéo a été réalisée avec la première version, donc elle ne contient pas les bases de données et les applications en un clic. Mais c'est un bon point de départ.

![Image](https://cdn-media-1.freecodecamp.org/images/fPSXo6a50qDpqxGr8kiGaFgyh2lGphosLhYv)

![Image](https://cdn-media-1.freecodecamp.org/images/RhbupzCjT8UvQH2lu4n3vn3xAZEJGeG5oL3l)