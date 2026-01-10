---
title: Comment utiliser Jigsaw pour construire rapidement et facilement des sites
  statiques
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-04T21:54:10.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-jigsaw-to-quickly-and-easily-build-static-sites-8a3304c3ad7e
coverImage: https://cdn-media-1.freecodecamp.org/images/0*CCMaHN9JpmvIFNdi
tags:
- name: Laravel
  slug: laravel
- name: PHP
  slug: php
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment utiliser Jigsaw pour construire rapidement et facilement des sites
  statiques
seo_desc: 'By Rick West

  Let’s dive in to Jigsaw — a framework for rapidly building static sites using the
  same modern tooling that powers Laravel applications.

  Static sites aren’t a new concept. However, fully fledged, dynamic, Content Management
  System (CMS’s)...'
---

Par Rick West

#### Plongeons dans Jigsaw — un framework pour construire rapidement des sites statiques en utilisant les mêmes outils modernes qui alimentent les applications Laravel.

Les sites statiques ne sont pas un concept nouveau. Cependant, les systèmes de gestion de contenu (CMS) entièrement développés et dynamiques, tels que WordPress, Drupal et Joomla, semblaient avoir pris le dessus. C'est-à-dire, jusqu'à récemment, où il y a eu un regain de popularité des générateurs de sites statiques tels que Jekyll, Hugo, Pelican et maintenant Jigsaw.

Bien que les CMS fournissent un outil puissant et utile pour servir l'utilisateur dans certaines situations, la tendance est devenue que les développeurs essaient de les forcer dans des situations où ils n'appartiennent tout simplement pas, ou du moins ne correspondent pas au cas d'utilisation prévu.

Comme son nom l'indique, l'objectif principal d'un « Système de Gestion de Contenu » est de faire exactement cela, gérer le contenu. Et ils excellent dans cette tâche, surtout dans les situations où les blogueurs, les marketeurs de contenu et les propriétaires de sites doivent mettre à jour leur site web régulièrement.

Cependant, en tant que solution pour construire un site marketing de style brochure pour une entreprise ou un simple blog personnel/portfolio ? À mon avis ? Pas si génial.

### Qu'est-ce qu'un générateur de site statique ?

Simplement, un générateur de site statique est une application qui prend du contenu (généralement écrit en Markdown), l'applique à des templates, et génère un ensemble de fichiers HTML purement statiques, prêts à être livrés aux visiteurs.

Les générateurs de sites statiques combinent la puissance des outils modernes et des bibliothèques de templating avec la simplicité des pages web statiques en HTML.

La sortie déployable d'un générateur de site statique ne nécessite aucune exécution ou interprétation par un serveur web.

![Image](https://cdn-media-1.freecodecamp.org/images/0*CCMaHN9JpmvIFNdi)
_Source de l'image ([https://www.slideshare.net/mackato/blogging-on-jekyll](https://www.slideshare.net/mackato/blogging-on-jekyll" rel="noopener" target="_blank" title="))_

### Avantages d'un générateur de site statique

#### Technologie éprouvée

Les générateurs de sites statiques produisent des fichiers statiques composés uniquement de HTML, CSS et JavaScript. Cela signifie qu'ils ne nécessitent aucun traitement par un serveur et peuvent être servis directement à partir du système de fichiers du serveur web exactement comme ils sont stockés. C'est une technologie rapide, simple, éprouvée.

#### Hébergement minimal et peu coûteux

Les générateurs de sites statiques fonctionnent le plus souvent sur votre machine locale, puis la sortie peut être poussée vers un hébergeur web simple — n'importe quel hébergeur web fera l'affaire, puisqu'ils ne serviront que des fichiers statiques. Par conséquent, les sites statiques peuvent être hébergés totalement gratuitement sur des plateformes telles que [Github Pages](https://pages.github.com/) ou [Netlify](https://www.netlify.com/).

#### Sécurité

L'une des plus grandes menaces du développement avec un CMS dynamique est le manque de sécurité. Leur besoin d'une infrastructure côté serveur plus importante ouvre la voie à des violations potentielles.

Parce qu'un site statique n'a pas de couche de base de données et peu ou pas de fonctionnalités côté serveur, il n'y a pas d'exposition de surfaces d'attaque supplémentaires.

#### Vitesse et performance

Parce que les générateurs de sites statiques construisent des fichiers déjà compilés qui sont ensuite servis au navigateur, sans avoir à extraire dynamiquement des informations d'une base de données, il y a très peu de temps de chargement, ce qui entraîne des performances exceptionnelles dans la majorité des cas.

#### Flexibilité

La résurgence de la popularité des générateurs de sites statiques est probablement liée au gain de popularité de JavaScript.

JavaScript peut désormais effectuer de nombreuses tâches similaires à celles des langages de script côté serveur réguliers tels que PHP ou Python.

Cela a conduit à une flexibilité beaucoup plus grande dans les sites statiques, comme la possibilité de s'intégrer facilement avec des services web externes tels que l'analyse, les options de soumission de formulaires/inscription à une liste de diffusion et les passerelles de paiement.

Bien que les générateurs de sites statiques puissent initialement demander plus de compétences techniques à un développeur, par rapport à la simple production de pages statiques ou à l'utilisation d'un CMS, nous sommes également récompensés par une liberté infiniment plus grande.

### Options de sites statiques pour les développeurs PHP

Il existe des centaines de générateurs de sites statiques disponibles, mais si, comme moi, PHP est votre langage de programmation principal, cela aide à réduire considérablement les options.

Choisir un outil écrit dans un langage que vous connaissez est assez important lorsque l'on considère la courbe d'apprentissage, l'extensibilité, le débogage et le développement de votre projet.

En utilisant [https://www.staticgen.com/](https://www.staticgen.com/), j'ai pu obtenir une belle comparaison des générateurs de sites statiques PHP les plus populaires.

![Image](https://cdn-media-1.freecodecamp.org/images/0*sA3Jpj2t1OPIqn9s)
_Une comparaison des générateurs de sites statiques PHP de [https://www.staticgen.com/](https://www.staticgen.com/" rel="noopener" target="_blank" title=")_

Comme vous pouvez le voir sur l'image, [Sculpin](https://sculpin.io/) et [Jigsaw](https://jigsaw.tighten.co/) sont des favoris assez clairs.

Sculpin a été publié pour la première fois en 2012, c'est donc un choix mature et solide, construit sur des composants [Symfony](https://symfony.com/).

Jigsaw, en revanche, a été publié en 2015 par l'équipe de [Tighten](https://tighten.co/) et utilise plusieurs composants Laravel, tels que Blade et Laravel Mix.

Étant construit sur Laravel, et compte tenu de la popularité notable et de la communauté entourant [Laravel](https://laravel.com/), cela fait de [Jigsaw](https://jigsaw.tighten.co/) une option vraiment excitante ?.

Cela dit, approfondissons un peu Jigsaw...

### Jigsaw — Un framework pour construire rapidement des sites statiques en utilisant les mêmes outils modernes qui alimentent votre application Laravel.

![Image](https://cdn-media-1.freecodecamp.org/images/1*gyYn7QH6v4SVAt0tdB5h6Q.png)

### Qu'est-ce que Jigsaw

Développé par l'équipe de [Tighten](https://tighten.co/), [Jigsaw](https://jigsaw.tighten.co/) est un générateur de sites statiques qui utilise des composants du framework [Laravel](https://laravel.com/) pour construire des sites web statiques.

Ces composants incluent le moteur de templating Blade, les Collections et Laravel Mix pour gérer les assets.

> « Des sites statiques pour les développeurs Laravel.

> Jigsaw est un framework pour construire rapidement des sites statiques en utilisant les mêmes outils modernes qui alimentent votre application web. »

Compte tenu de tout cela, il n'est pas surprenant que Jigsaw « semble » beaucoup à Laravel. Une syntaxe très propre, expressive, facile à configurer, infiniment puissante et tout « fonctionne simplement » ?.

Admettons-le, le plan de Laravel est éprouvé, c'est le framework backend le plus populaire pour une raison. Donc, avec Jigsaw utilisant des composants Laravel et incarnant l'éthos de Laravel, il est définitivement bien parti.

![Image](https://cdn-media-1.freecodecamp.org/images/1*fwXQdEaEeAOttQL1gS_h1w.png)
_[https://jigsaw.tighten.co/](https://jigsaw.tighten.co/" rel="noopener" target="_blank" title=")_

### Commencer avec Jigsaw

Dans le cadre des recherches que j'ai faites sur Jigsaw (c'était à l'origine un projet universitaire que j'ai transformé en une série d'articles de blog !), j'ai contacté [Keith Damiani](https://medium.com/@rickwest8/jigsaw-my-interview-with-keith-damiani-senior-developer-at-tighten-and-lead-developer-on-the-55ead103514d), un développeur senior chez Tighten, qui est également le responsable du projet Jigsaw. En ses propres mots, [Keith décrit Jigsaw](https://medium.com/@rickwest8/jigsaw-my-interview-with-keith-damiani-senior-developer-at-tighten-and-lead-developer-on-the-55ead103514d) :

> _« Il est définitivement destiné aux développeurs qui sont à l'aise dans l'écosystème Laravel, car il s'appuie tellement sur Blade ; donc pour quelqu'un qui écrit Laravel (ou même PHP) toute la journée, c'est un choix naturel qui implique une courbe d'apprentissage assez courte pour se lancer. »_

Génial.

Pour utiliser Jigsaw, vous avez juste besoin de PHP 7, Composer, Node et NPM installés sur votre machine. Tous des outils standard, faisant partie d'un workflow de développement PHP moderne.

Se lancer à partir de là est ensuite assez simple, car la qualité de la [documentation de Jigsaw](https://jigsaw.tighten.co/docs/installation/) est vraiment fantastique.

L'installation de Jigsaw jusqu'à la prévisualisation de quelque chose dans votre navigateur peut être réalisée en aussi peu que 4 étapes simples :

1. Installez Jigsaw via Composer :

```
composer require tightenco/jigsaw
```

2. Initialisez votre projet Jigsaw :

```
./vendor/bin/jigsaw init
```

3. Générez votre site en exécutant la commande de build :

```
./vendor/bin/jigsaw build
```

4. Prévoyez votre site avec PHP en utilisant la commande serve :

```
./vendor/bin/jigsaw serve
```

Boom ! Cela met en évidence à quel point il est facile de commencer avec Jigsaw. Comme je l'ai mentionné auparavant, cela « fonctionne simplement » !

Prenons un regard plus approfondi sur certains autres aspects importants du framework...

### Écosystème et support

[Tighten](https://tighten.co/), la force motrice derrière Jigsaw, est une partie intégrale de l'écosystème Laravel plus large ainsi qu'un « [Laravel Partner](https://laravel.com/partners) » officiel.

Avec Jigsaw étant construit sur, et donc étroitement couplé à, certains des composants Laravel, cette connexion Tighten/Laravel est très prometteuse pour Jigsaw et son développement futur.

Tighten et de nombreux membres de son personnel sont également bien connus dans la communauté PHP/Laravel pour plusieurs autres projets fantastiques [open source](https://github.com/tightenco), produisant des tutoriels en ligne et hébergeant des podcasts.

Être soutenu par une entreprise aussi passionnée, proéminente et réussie est un grand signe d'encouragement, et déjà Tighten construit une communauté autour du projet Jigsaw. En fait, ils ont déjà créé [Built With Jigsaw](https://builtwithjigsaw.com/), un site web pour collecter et mettre en avant certains des grands exemples de projets construits avec Jigsaw, ainsi que des ressources communautaires et d'autres cas d'utilisation intéressants de Jigsaw.

Il est également intéressant de noter que lorsque [j'ai contacté Keith](https://medium.com/@rickwest8/jigsaw-my-interview-with-keith-damiani-senior-developer-at-tighten-and-lead-developer-on-the-55ead103514d) concernant l'interview pour mon projet, il a été plus que ravi de prendre un peu de temps dans sa journée pour répondre à quelques-unes de mes questions. Cette volonté de s'engager directement avec quelqu'un de la communauté plus large (un inconnu du Royaume-Uni) a vraiment souligné à quel point l'équipe Jigsaw est engagée envers la communauté et enthousiaste. Crédit à Keith et à l'attitude de Tighten dans son ensemble.

### Performance et évolutivité

Lors de [mon interview avec Keith](https://medium.com/@rickwest8/jigsaw-my-interview-with-keith-damiani-senior-developer-at-tighten-and-lead-developer-on-the-55ead103514d), il a révélé qu'ils connaissent plusieurs développeurs qui ont construit des sites très grands (avec 6 000+ pages) en utilisant Jigsaw.

L'équipe Jigsaw a également travaillé sur l'optimisation des temps de build de Jigsaw, ce qui sera particulièrement intéressant pour ceux qui maintiennent, ou prévoient de construire, de grands sites Jigsaw car cela réduit les temps de build d'environ 75 %.

### Fonctionnalités, flexibilité et extensibilité

Jigsaw est livré avec de nombreuses fonctionnalités qui aident au développement rapide de sites web statiques.

En me référant à la [documentation brillante](https://jigsaw.tighten.co/docs/installation/), j'ai résumé certaines de ces fonctionnalités principales ci-dessous :

#### Blade

L'épine dorsale de Jigsaw est le moteur de templating Blade. L'un des plus grands avantages d'un langage de templating est l'héritage de templates, la capacité à créer des layouts et des partials réutilisables. Cela réduit considérablement la duplication de code et diminue le temps de développement.

![Image](https://cdn-media-1.freecodecamp.org/images/1*bQxQDqNIR00k4v_WC9AI1Q.png)
_Exemple de Blade, pris de [https://jigsaw.tighten.co/](https://jigsaw.tighten.co/" rel="noopener" target="_blank" title=")_

#### Markdown

Comme avec de nombreux générateurs de sites statiques, Jigsaw supporte le contenu écrit en Markdown. Markdown est un format d'écriture fantastique pour des choses comme des articles, des billets de blog et des pages de documentation.

Jigsaw rend la création d'un layout dans Blade et son remplissage avec du contenu écrit en Markdown sans douleur.

#### Laravel Mix

Dès la sortie de la boîte, Jigsaw est livré avec Laravel Mix configuré et prêt à l'emploi. Laravel Mix fournit une API fluide pour définir les étapes de build Webpack pour votre application en utilisant plusieurs préprocesseurs CSS et JavaScript courants.

En tant que développeur junior, et quelqu'un avec une exposition limitée à Webpack et aux outils modernes de front-end, Laravel Mix enlève tout le stress et rend le démarrage avec Webpack et la compilation d'assets un jeu d'enfant.

#### Événements

Cette pull request [https://github.com/tightenco/jigsaw/pull/189](https://github.com/tightenco/jigsaw/pull/189) a ajouté 3 événements à Jigsaw auxquels vous pouvez vous accrocher, afin d'exécuter du code personnalisé avant et après que le build de l'application soit traité.

Les trois événements sont 'beforeBuild', 'afterCollections' et 'afterBuild'.

L'enregistrement d'un écouteur d'événement est très simple, et ces événements offrent une grande opportunité d'ajouter du code personnalisé. Cela serait particulièrement utile, par exemple, dans le cas où l'on souhaite récupérer du contenu d'un CMS basé sur une API externe comme [Contentful](https://www.contentful.com/) ou en [générant un sitemap automatisé](https://mattstauffer.com/blog/adding-an-auto-generated-sitemap-to-your-jigsaw-based-static-site/) après la construction du site.

#### Collections

Jigsaw fournit des fonctionnalités puissantes pour travailler avec des groupes de pages liées, ou collections. Les collections vous donnent la capacité d'accéder à votre contenu à un niveau agrégé, vous permettant d'ajouter facilement des fonctionnalités quasi dynamiques comme des menus, une pagination, des catégories et des tags à votre site statique.

Les collections peuvent être utilisées pour générer des pages de contenu lié — par exemple, des billets de blog ou des articles triés par date, avec une page d'index affichant des résumés des cinq billets les plus récents — ou pour intégrer des blocs de contenu liés dans une page, pour du contenu comme des biographies de personnel, des descriptions de produits, ou un portfolio de projets.

#### Packages

Bien que pas encore officiellement publiés, l'équipe Jigsaw/Tighten travaille sur quelques templates de démarrage pour Jigsaw. Un pour un blog et un pour un site web de style documentation.

En travaillant avec le designer [Steve Schoger](https://twitter.com/steveschoger), il ne fait aucun doute que ces templates seront assez géniaux, mais c'est aussi un grand indicateur que l'équipe fait les premiers pas pour rendre Jigsaw extensible avec l'ajout d'un écosystème de plugins externes.

Il ne fait aucun doute que, une fois l'intégration des plugins possible, les communautés Jigsaw et Laravel commenceront à trouver des moyens d'étendre Jigsaw de nombreuses manières innovantes !

### Résumé

Jigsaw est un framework stable, performant et intrinsèquement sécurisé, rempli de fonctionnalités puissantes et faciles à implémenter qui rendent notre vie de développeurs plus facile et donc plus heureuse ?.

Il est si facile de commencer avec, ayant une barrière d'entrée si basse pour quelqu'un familier avec le développement PHP moderne, que vous pouvez prendre un projet de 'jigsaw init' à être hébergé GRATUITEMENT sur Netlify ou Github Pages en un rien de temps.

À mon avis, deux des facteurs les plus importants lors de la considération de tout framework ou bibliothèque sont la qualité de la documentation ainsi que l'écosystème et le support qui l'entourent.

Dans ces cas, Jigsaw excelle, au-delà des attentes. J'ai trouvé la documentation claire, concise et bien présentée, et la communauté et le support entourant Jigsaw sont sans égal (peut-être à l'exception de Laravel lui-même !).

**Assurez-vous d'essayer Jigsaw dans votre prochain projet, ou lorsque vous vous déciderez enfin à construire ce blog dont vous parlez sans cesse.**

**Plus d'excuses. Jigsaw est génial.**

_*Dans le cadre de mes recherches pour cet article, j'ai contacté [Keith Damiani](https://twitter.com/keithdamiani), un développeur senior chez Tighten, qui est également le responsable du projet Jigsaw._

_Keith a eu la gentillesse de répondre à quelques-unes de mes questions concernant le développement de Jigsaw et les plans pour l'avenir._

_Vous pouvez lire cette interview complète ici...[https://medium.com/@rickwest8/jigsaw-my-interview-with-keith-damiani-senior-developer-at-tighten-and-lead-developer-on-the-55ead103514d](https://medium.com/@rickwest8/jigsaw-my-interview-with-keith-damiani-senior-developer-at-tighten-and-lead-developer-on-the-55ead103514d)_

Merci d'avoir lu ! ? Si vous avez aimé, cliquez sur ce bouton d'applaudissements ci-dessous. J'apprécie vraiment votre soutien et cela aide les autres à voir l'histoire.

Je suis toujours heureux d'entendre des personnes qui pensent comme moi, alors n'hésitez pas à m'envoyer un email ou à dire bonjour sur [Twitter](http://twitter.com/rick_west8).