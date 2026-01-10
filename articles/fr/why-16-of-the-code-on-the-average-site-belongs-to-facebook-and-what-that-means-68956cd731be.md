---
title: Pourquoi les boutons J'aime de Facebook représentent 16 % du code d'un site
  web moyen
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-09-03T23:39:08.000Z'
originalURL: https://freecodecamp.org/news/why-16-of-the-code-on-the-average-site-belongs-to-facebook-and-what-that-means-68956cd731be
coverImage: https://cdn-media-1.freecodecamp.org/images/1*YrHFWabESezXSeFmt_Co-Q.png
tags:
- name: Facebook
  slug: facebook
- name: JavaScript
  slug: javascript
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Pourquoi les boutons J'aime de Facebook représentent 16 % du code d'un
  site web moyen
seo_desc: 'By Ben Regenspan

  According to data collected by BuiltWith.com, 6% of the top 10,000 most high-traffic
  sites load content from Facebook’s servers. For the vast majority of them, that
  content is likely Facebook’s Javascript SDK, a huge block of code th...'
---

Par Ben Regenspan

Selon les [données collectées par BuiltWith.com](https://trends.builtwith.com/cdn/Facebook-CDN), 6 % des 10 000 sites les plus fréquentés chargent du contenu depuis les serveurs de Facebook. Pour la grande majorité d'entre eux, ce contenu est probablement le SDK Javascript de Facebook, un énorme bloc de code nécessaire pour afficher des fonctionnalités telles que le bouton J'aime (comme on en voit sur de nombreux sites médias) et les widgets de commentaires Facebook (également utilisés sur de nombreux grands sites médias, dont Buzzfeed).

Ce code SDK est si volumineux qu'il représente environ 16 % de la taille totale de tout le JavaScript sur la [page web moyenne](http://httparchive.org/trends.php#bytesJS&reqJS).

![Image](https://cdn-media-1.freecodecamp.org/images/XTrx22wjKCYtC7DVJChFX-yLoMBdiQgGkIwa)
_L'un des responsables du temps de téléchargement des sites web modernes_

En tant que bibliothèque logicielle volumineuse et largement utilisée, le SDK Facebook est un bon moyen d'illustrer certaines des réponses aux questions suivantes : pourquoi le site moyen d'aujourd'hui est-il si volumineux ? Et dans quelle mesure la taille compte-t-elle vraiment ?

### Pourquoi si volumineux ?

Le SDK Facebook est très complet, dupliquant de nombreux outils que le site moyen est susceptible d'inclure déjà pour ses propres développeurs : des méthodes pour récupérer des données d'autres sites, pour déterminer quel navigateur et quel appareil l'utilisateur utilise afin de cibler des fonctionnalités spécifiques, et pour afficher des éléments d'interface utilisateur (comme des boîtes de dialogue de confirmation et des boutons). Si nous [catégorisons toutes les parties](https://docs.google.com/spreadsheets/d/1vdRzi-wlYNQOoAt4bGOseDMt7vgmpv9BoSfy4yM1SYY/edit?usp=sharing) du SDK, la répartition ressemble à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/fmjSpUO8iwQb-e-p6xHljRv5VM8Kce6m6gwT)
_La contribution de chaque ensemble de fonctionnalités du SDK à la taille totale du fichier. (Notez que ceci est la taille du fichier avant qu'il ne soit compressé ; le package final sera plus petit.) [[Données sources, méthodologie et tableau de données plus compatible avec les lecteurs d'écran](https://docs.google.com/spreadsheets/d/1vdRzi-wlYNQOoAt4bGOseDMt7vgmpv9BoSfy4yM1SYY/edit#gid=873242422" rel="noopener" target="_blank" title=")]_

Parmi les ensembles de fonctionnalités, trois se distinguent particulièrement :

![Image](https://cdn-media-1.freecodecamp.org/images/ZxophdegZjOmW0hweYCPJniEBJ4dmHj8fZuL)
_Les trois ensembles de fonctionnalités du SDK qui sont complètement irrélevants pour la grande majorité des utilisateurs sur la plupart des sites. Les éliminer — si cela était possible — réduirait d'environ 20 % la taille du fichier SDK. [[Données sources, méthodologie et tableau de données plus compatible avec les lecteurs d'écran](https://docs.google.com/spreadsheets/d/1vdRzi-wlYNQOoAt4bGOseDMt7vgmpv9BoSfy4yM1SYY/edit#gid=873242422" rel="noopener" target="_blank" title=")]_

« Canvas » est le système de Facebook pour les applications destinées à être chargées dans Facebook (Facebook a fait une grande poussée par le passé pour encourager les développeurs à créer des applications qui vivaient dans Facebook ; je ne suis pas entièrement sûr de la fréquence à laquelle de telles applications sont utilisées aujourd'hui, mais dans tous les cas, un site web régulier n'utilise aucune des fonctionnalités liées à Canvas.) Le coût de leur inclusion dans le SDK est assez marginal : seulement 1,5 % de la taille totale.

Ensuite, nous avons la prise en charge des fonctionnalités héritées. Cela reflète le fait qu'une API accumulera plusieurs interfaces pour gérer les mêmes fonctionnalités au fil du temps. Par exemple, les développeurs peuvent écrire du code qui appelle soit **FB.getLoginStatus()** (l'approche héritée pour demander le statut de connexion actuel de l'utilisateur à Facebook) soit **Auth.getLoginStatus()** (la nouvelle approche encouragée). La manière de contourner le besoin d'inclure les deux ensembles de méthodes est de les publier dans des versions séparées du SDK, mais Facebook a choisi de ne pas le faire, probablement pour simplifier l'expérience des développeurs et pour maximiser le nombre de sites utilisant le fichier exact (pour augmenter la probabilité que l'utilisateur moyen l'ait déjà téléchargé). Cette décision a un petit coût : environ 3,5 % du code SDK est destiné à gérer les fonctionnalités explicitement marquées comme « héritées » (et il est tout à fait possible qu'il existe de nombreuses autres fonctionnalités « héritées » qui ne sont tout simplement pas explicitement marquées comme telles).

Plus significativement, le SDK inclut un certain nombre de polyfills et d'utilitaires de type polyfill, qui représentent plus de 15 % de son code. Les polyfills sont utilisés pour fournir des fonctionnalités présentes dans les navigateurs plus récents aux navigateurs plus anciens, et parfois aussi pour fournir des fonctionnalités plus récentes qui sont à venir mais qui n'ont pas encore été ajoutées à aucun navigateur. La plupart des polyfills inclus par le SDK Facebook sont pour des fonctionnalités déjà incluses dans les navigateurs utilisés par la grande majorité des utilisateurs d'Internet. Ils servent uniquement à faire fonctionner le SDK pour les [<](http://gs.statcounter.com/browser-version-market-share) 1 % des utilisateurs mondiaux d'Internet qui utilisent des navigateurs anciens comme Internet Explorer 8, que de nombreux (sinon la grande majorité des) grands sites ont abandonné à supporter.

Pour les ~80 % restants du SDK, il est un peu plus difficile de démêler quelles fonctionnalités sont nécessaires pour quel usage. Cela est dû au fait qu'il est écrit de telle manière que, pour utiliser une fonctionnalité simple comme le bouton J'aime, il faut également inclure du code qui n'est utilisé que pour les commentaires, les intégrations vidéo, les boutons de connexion et d'autres fonctionnalités sans rapport. Facebook aurait pu choisir de distribuer des fichiers beaucoup plus petits pour inclure uniquement des fonctionnalités simples comme les boutons J'aime, mais a un objectif commercial d'encourager les sites à utiliser autant de fonctionnalités fournies par FB que possible.

### La taille compte-t-elle ?

En raison de l'utilisation généralisée du SDK de Facebook, et du fait qu'il change [relativement peu fréquemment](https://github.com/nfriedly/facebook-js-sdk), de nombreux utilisateurs ont probablement déjà téléchargé le SDK avant de charger un site. En fait, cela fait partie de la raison pour laquelle Facebook distribuerait un fichier aussi volumineux, plutôt que des fichiers plus petits pour des fonctionnalités spécifiques comme les boutons J'aime. Et sur la plupart des connexions réseau des utilisateurs — au moins celles des pays développés — le temps nécessaire pour télécharger le fichier est marginal.

Mais, indépendamment du fait que le navigateur de l'utilisateur ait déjà téléchargé le SDK, il y a toujours un surcoût lié à l'exécution d'un grand bloc de Javascript, en particulier sur les appareils mobiles. Sur le MacBook Pro relativement nouveau sur lequel j'écris ceci, le SDK de Facebook prend environ 50 ms (1/20ème de seconde) pour s'exécuter sur un site comme Buzzfeed. Pas mal — surtout lorsqu'on le met en contexte avec le reste du code JS, y compris le code lié aux publicités qui prend beaucoup plus de temps à s'exécuter — mais toujours un coût non négligeable pour quelque chose qui n'est utilisé que pour afficher des commentaires tout en bas de la page.

![Image](https://cdn-media-1.freecodecamp.org/images/NKYO49MdQzV4gQmTtpw3llLD1za7M61faSFy)
_Évaluation du script dans Chrome sur un MacBook Pro récent_

Sur un smartphone très récent (Google Pixel), le temps d'exécution du JS est doublé, prenant maintenant plus de 1/10ème de seconde :

![Image](https://cdn-media-1.freecodecamp.org/images/7AiXlQH2A-fsvhsNZP8M1R2mSqAqekWUyg5D)
_Évaluation du script sur un smartphone Google Pixel_

Lorsqu'on le regarde dans son contexte, cela représente une infime fraction du temps total d'exécution du code sur la page. Mais cela s'ajoute au temps pendant lequel le défilement ou toute autre interaction avec la page peut être une expérience saccadée et désagréable. Et cela soulève un point important : ce SDK particulier a un coût marginal, mais les sites web modernes — en particulier les sites médias — incluent souvent des codes similaires provenant d'un grand nombre de tiers ([cet exemple que j'ai capturé de Gawker avant qu'il ne soit tué par un milliardaire vampire](http://ben.regenspan.com/your-script-loader-is-killing-you/#/4/4) montre à quel point de telles requêtes peuvent être nombreuses).

Même en mettant de côté l'impact sur la vie privée de l'envoi de certaines informations utilisateur à chacun de ces tiers, le coût de toutes ces fonctionnalités s'additionne rapidement. Chaque script tiers qu'un site ajoute a un coût, à la fois en termes de performance et en aidant à rationaliser l'ajout du prochain morceau de code tiers « relativement inoffensif » plus tard. En plus de l'impact immédiat sur la performance du coût additif de tout ce code, cela affecte le moral des développeurs : imaginez travailler pendant des jours pour réduire de 10 % le temps de chargement de votre propre code, pour voir ensuite un énorme bloc de code tiers ajouté qui éclipse l'impact de cet effort minutieux. Et puis (si vous travaillez pour un site média), voir ce même schéma se répéter encore et encore tous les quelques mois.

### Devriez-vous l'inclure ?

Si vous devez utiliser une fonctionnalité comme les commentaires Facebook, il est impossible de contourner le besoin de charger le SDK Facebook. Mais selon la structure de votre site, vous pourriez être en mesure de limiter l'impact sur la performance du SDK en ne le chargeant que lorsque cela est nécessaire (par exemple, une fois que l'utilisateur a fait défiler jusqu'au point où les commentaires doivent devenir visibles).

Si vous souhaitez utiliser le bouton J'aime, arrêtez-vous et réfléchissez. Facebook n'affiche plus les J'aime d'une page de manière proéminente (ou, dans la plupart des cas, pas du tout) sur les fils d'actualité des utilisateurs. Il est préférable d'[utiliser un simple bouton ou lien de partage personnalisé](https://jonsuh.com/blog/social-share-links/#use-share-urls), et en plus, cela empêchera Facebook de suivre toutes les visites sur votre page et d'interférer avec la vie privée de vos utilisateurs. Les sites qui ont éliminé le bouton J'aime n'ont pas identifié d'impact négatif sur les références de trafic Facebook.

_CORRECTION du titre : À l'origine, j'ai intitulé ceci « Pourquoi 16 % du code sur le site moyen appartient à Facebook, et ce que cela signifie ». Comme certains l'ont justement souligné, cela implique qu'un plein 16 % du JavaScript sur tous les sites de l'Internet (ou au moins sur tous les principaux sites) se compose du SDK JavaScript de Facebook. Ce n'était pas mon intention et je peux voir comment cela a pu paraître excessivement sensationnaliste._

_Espérons que le nouveau titre clarifie que le SDK Facebook représente 16 % de la taille du JavaScript du site moyen, et ne suggère plus qu'il représente 16 % du JavaScript total des sites sur l'Internet. Comme [David Gilbertson le note ici](https://medium.com/@david.gilbertson/maybe-i-missed-something-but-isnt-your-article-s-title-100-false-d2dcc51fc9ed), le nombre global réel serait beaucoup plus petit — 0,96 %. Il soulève également un bon point concernant la mise en cache : le SDK JavaScript de Facebook n'est pas du tout mis en cache de manière optimale, il n'est mis en cache de la manière la plus idéale que pendant 20 minutes, après quoi le navigateur de l'utilisateur vérifie à nouveau avec les serveurs de Facebook pour confirmer qu'il dispose déjà de la dernière version._