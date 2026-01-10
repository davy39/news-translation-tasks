---
title: Comment accélérer votre site web - 5 conseils ultimes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-03-31T01:12:49.000Z'
originalURL: https://freecodecamp.org/news/speed-up-website
coverImage: https://www.freecodecamp.org/news/content/images/2020/03/Screenshot-2020-03-31-at-12.47.19-AM.png
tags:
- name: servers
  slug: servers
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: Comment accélérer votre site web - 5 conseils ultimes
seo_desc: 'By Mehul Mohan

  Site speed is important. It affects your users'' experience directly, and a good
  user experience is extremely important to help drive sales and keep customers and
  visitors happy. Not only does it improve your site''s UX, but a correctly ...'
---

Par Mehul Mohan

La vitesse du site est importante. Elle affecte directement l'expérience de vos utilisateurs, et une bonne expérience utilisateur est extrêmement importante pour stimuler les ventes et garder les clients et visiteurs satisfaits. Non seulement elle améliore l'UX de votre site, mais un site correctement configuré consomme moins de ressources et décharge le travail du serveur principal.

Dans cet article, je vais discuter de ce que j'ai appris en obtenant un A sur GTMetrix sur [codedamn](https://codedamn.com) - une plateforme pour les développeurs afin d'apprendre la programmation d'une nouvelle manière. Commençons !

## #1: Compresser les images

Les images brutes sont hautement compressibles, et vous seriez surpris de découvrir combien de bande passante et de données vous pourriez économiser simplement en compressant toutes vos images.

Pour les sites en production, je recommande des outils comme [TinyPNG CLI](https://www.npmjs.com/package/tinypng-cli) qui peuvent compresser vos images sur le serveur dans un répertoire. Voici un aperçu rapide de la manière dont TinyPNG a économisé plus de 2 Mo sur une photo haute résolution que j'ai téléchargée sur leur site :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Screenshot-2020-03-31-at-12.45.11-AM.png)

Le plus intéressant est que TinyPNG permet 500 images gratuites par mois, donc pour un site petit à moyen, vous pouvez presque toujours rester dans la limite gratuite !

## #2: Division de code ET division de bundles

La division de code signifie que vous divisez votre code en plusieurs morceaux et les chargez de manière paresseuse lorsque nécessaire. Vous avez toujours besoin de cela sur votre site.

La division de bundles fait référence à la division des fichiers individuels générés par la division de code en bundles plus petits. Cela améliore le caching dans les navigateurs ainsi que le caching du bytecode par les navigateurs.

Bien que la division de bundles puisse être critiquée car elle augmente les requêtes HTTP, HTTP/2 a peu ou pas d'impact sur les multiples requêtes jusqu'à ce que les limites de concurrency soient atteintes. Et heureusement, les limites de concurrency sont de l'ordre de centaines de requêtes.

Donc, si vous ne faites pas des centaines de requêtes HTTP (ce que vous ne faites probablement pas), vous devriez être bon avec la division de bundles.

Pour la division de code et de bundles, vous devez intégrer votre projet avec un module bundler comme parcel ou webpack.

Une fois que vous les configurez correctement, ils fonctionnent comme par magie. Et ils peuvent vraiment réduire la charge à la fois sur votre serveur et sur les navigateurs des clients.

Ils le font en mettant en cache les ressources et en ne téléchargeant pas les ressources dont vous n'avez pas besoin actuellement - par exemple, pourquoi voulez-vous envoyer le code JS pour la route `/about` lorsque je suis sur la route `/feedback`.

Vous devriez également minifier vos builds JS/CSS. Pour webpack, il existe des plugins comme UglifyJS disponibles. Cela aide à réduire la taille en supprimant les espaces blancs, les commentaires, en raccourcissant le code, etc. - ce qui réduira finalement la taille du contenu.

## #3: Ne pas utiliser les services d'hébergement mutualisé

Si vous êtes un développeur ou quelqu'un qui a une compréhension de base de la façon de travailler avec bash un peu, il n'y a tout simplement aucune raison d'opter pour les services d'hébergement mutualisé.

Dans presque tous les cas, soit vous pouvez héberger vos actifs statiques gratuitement sur des sites comme GitHub pages, soit vous pouvez opter pour des options plus contrôlées comme l'hébergement cloud. Presque tous ces fournisseurs d'hébergement cloud comme AWS, Google Cloud et DigitalOcean offrent tant de crédits gratuits que vous pouvez consommer beaucoup de leurs services gratuitement pendant longtemps !

Dans certains cas, l'hébergement mutualisé est moins cher que des alternatives comme l'hébergement DigitalOcean à 5 $. Mais ces serveurs ont des ressources très limitées allouées à votre site web, ce qui dégrade les performances globales du site. Les shells jailed, les vCPUs partagés et la RAM limitée sont quelques-unes des choses à commencer.

Puisque nous, en tant que développeurs, voulons toujours être en contrôle, et opter pour un IaaS ou un PaaS est toujours une solution.

Bien que vous puissiez choisir n'importe quel fournisseur cloud de votre choix, je recommande DigitalOcean - celui que j'utilise actuellement pour [codedamn](https://codedamn.com). Il est extrêmement simple à configurer, et vous pouvez obtenir [100 $ de crédits cloud gratuits avec ce lien](https://codedamn.com/go/digitalocean).

Choisir un fournisseur cloud peut vraiment vous donner des ressources et une infrastructure qui amélioreront automatiquement les performances de votre serveur (et de votre site) un peu.

## #4: Définir les en-têtes d'expiration HTTP

Tout comme nous l'avons discuté ci-dessus, le caching est extrêmement important à configurer correctement. Les en-têtes d'expiration HTTP informent le navigateur de ce qu'il doit mettre en cache et pour combien de temps. Les ressources mises en cache ne sont pas récupérées depuis les serveurs distants, il est donc important de ne pas mettre en cache les ressources principales comme `index.html` - le premier fichier que vous servez. Vous devez également implémenter le cache busting de manière appropriée.

Encore une fois, pour les module bundlers comme webpack, vous pouvez implémenter le cache busting en ayant `[contenthash]` dans le nom des bundles qu'il génère. De plus, cela nécessite que les navigateurs ne mettent jamais en cache votre `index.html` ou tout autre fichier HTML que vous utilisez comme point d'entrée de votre site. Comment pouvons-nous y parvenir ?

Pour le service de fichiers statiques et les en-têtes d'expiration HTTP, utilisez NGiNX. NGiNX peut gérer tout cela pour vous. Voici une configuration d'exemple recommandée pour définir les en-têtes d'expiration HTTP :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Screenshot-2020-03-31-at-12.32.38-AM.png)

Cette configuration désactive simplement le caching pour les ressources `text/html`. Pour les autres, elle le définit à la durée maximale possible pendant laquelle le navigateur peut conserver le cache.

Notez que cette configuration repose fortement sur le fait que vous avez implémenté des mécanismes de cache busting dans votre module bundler (comme le `[contenthash]` dont nous avons parlé ci-dessus).

## #5: Activer la compression Brotli

La compression Brotli est un algorithme de compression conçu par Google, qui est 20-25 % plus efficace que la compression GZIP bien connue.

La compression Brotli peut être implémentée sur les sites, encore une fois, en utilisant NGiNX. Jetons un coup d'œil à un exemple de ce qui se passe lorsque la compression Brotli est activée :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Screenshot-2020-03-31-at-12.40.32-AM.png)

La première taille de fichier est de 3,33 Mo - sans compression.

Lorsque le fichier est compressé avec Brotli - la taille tombe à 572 Ko.

Lorsque le fichier est compressé avec GZIP - la taille ne tombe qu'à 783 Ko.

Brotli économise plus de 200 Ko par rapport à GZIP, et plus de 2,5 Mo par rapport à aucune compression. Et il ne fonctionne même pas à son pic de performance ! C'est plus de 82 % de compression ! Très cool.

## C'est tout !

C'est à peu près tout ! Sans entrer dans les détails de la mise en œuvre de ces techniques spécifiques, nous avons couvert certaines des choses les plus importantes à considérer lors de l'accélération de votre site.

Je ne suis pas entré dans les détails spécifiques car votre expérience peut varier en fonction de vos configurations et setups de serveur - mais le concept général reste le même.

Assurez-vous de suivre ces meilleures pratiques et faites-moi savoir ce que vous en pensez en disant Bonjour sur mon [compte twitter](https://twitter.com/mehulmpt).

Si vous avez aimé cet article, rencontrons-nous sur les réseaux sociaux. Voici mon [Instagram](https://instagram.com/mehulmpt) et [Twitter](https://twitter.com/mehulmpt). Je suis super actif, et j'adorerais discuter ! Restons en contact.