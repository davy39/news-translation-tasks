---
title: Pourquoi Gatsby est si rapide
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-01T17:49:37.000Z'
originalURL: https://freecodecamp.org/news/how-gatsby-is-so-blazing-fast-c99a6f2d405e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*rcK0xeuBYK_yTArHwNJh5Q.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Pourquoi Gatsby est si rapide
seo_desc: 'By Luan Orlandi

  Performance greatly affects the user experience. Gatsby builds fast websites out-of-the-box.

  When creating the tool, they noticed that slow websites are slow in different ways,
  but fast websites are fast in similar ways. So baking opt...'
---

Par Luan Orlandi

La performance affecte grandement l'expérience utilisateur. Gatsby crée des sites web rapides dès la sortie de la boîte.

Lors de la création de l'outil, ils ont remarqué que les sites web lents sont lents de différentes manières, mais que les sites web rapides sont rapides de manières similaires. Ainsi, l'intégration d'approches d'optimisation dans un framework a abouti à Gatsby.

D'après mon expérience, Gatsby a configuré [webpack](https://webpack.js.org/) pour obtenir les performances les plus optimales. Webpack est un bundler de modules pour JavaScript utilisé par de nombreux projets front-end.

![Image](https://cdn-media-1.freecodecamp.org/images/1*bMLE3-PipX9X0N7eCHIGow.png)
_Une grande communauté développe Gatsby sur GitHub, contribuant également à la [conception du logo](https://github.com/gatsbyjs/gatsby/issues/408#issuecomment-245861049" rel="noopener" target="_blank" title=")._

### Mélanger les sites statiques avec les applications dynamiques

Gatsby est un générateur de sites statiques qui utilise React. Il crée des fichiers HTML pour chaque page de votre site web.

Ainsi, lors de la construction de votre site web, Node.js montera l'application React pour créer des fichiers HTML avec le contenu rendu pour chaque route. C'est le cœur de Gatsby.

> "Au lieu d'attendre de générer les pages lorsqu'elles sont demandées, Gatsby pré-génère les pages" — [gatsbyjs.org](https://www.gatsbyjs.org/)

Revenons aux bases pour voir pourquoi cela est important pour la performance.

Lorsque l'utilisateur accède à une page via un fichier HTML, le navigateur rend le contenu. Sans aucun cache ou JavaScript, l'utilisation d'une balise d'ancrage chargera un autre fichier HTML lorsqu'elle sera cliquée. En conséquence, l'utilisateur pourrait devoir attendre ou pire, voir une page blanche pendant le rendu du contenu.

C'est la manière la plus traditionnelle dont le Web a été conçu jusqu'à l'arrivée des Single Page Applications (SPA).

SPA rend la page en mettant à jour le contenu avec JavaScript. Il est beaucoup plus rapide de mettre à jour que de télécharger des fichiers statiques. Parce qu'ils chargent un seul fichier HTML et mettent à jour dynamiquement cette page lorsque l'utilisateur interagit.

React est une bibliothèque pour gérer la couche de vue pour SPA. De tels frameworks et bibliothèques comme React ne savent pas quoi rendre à moins que du code JavaScript ne commence à s'exécuter. Ainsi, les construire en tant que SPA affectera drastiquement le [Critical Rendering Path](https://calendar.perfplanet.com/2012/deciphering-the-critical-rendering-path/).

![Image](https://cdn-media-1.freecodecamp.org/images/1*aAoiF2OcphAPg8DoYwXqpA.png)
_Critical Rendering Path bloque le rendu pendant le chargement et l'exécution de JavaScript._

Gatsby a une configuration webpack pour fournir suffisamment de contenu pour le premier rendu :

* **Balises HTML**
* **Code JavaScript** défini comme [async](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/script#Attributes), nécessaire pour l'interaction utilisateur mais pas pour le premier rendu
* **CSS** en ligne, donc pas besoin de les télécharger

### Division de code et cache

Lors de la construction d'une page, Gatsby peut voir quels composants la page nécessite et laisser webpack faire la division de code automatiquement. Cela est appliqué en configurant les [Imports Dynamiques](https://webpack.js.org/guides/code-splitting/#dynamic-imports).

De cette manière, le navigateur ne demandera que les fichiers nécessaires pour la page, et non l'ensemble du site web, accélérant ainsi le temps d'interaction avec la page.

En conséquence, les liens vers d'autres pages téléchargeront leurs fichiers uniquement lorsque l'utilisateur interagira avec le lien, ralentissant la navigation.

Pour éviter ce problème, la configuration webpack de Gatsby applique une technique appelée [Préchargement de liens](https://developer.mozilla.org/en-US/docs/Web/HTTP/Link_prefetching_FAQ).

Après que le navigateur ait terminé de charger la page, il recherche silencieusement des liens avec des attributs de préchargement pour les télécharger. Ensuite, lorsqu'un utilisateur clique sur un lien, les fichiers demandés pour la page auront de grandes chances d'être déjà dans le cache.

### Chaque page est une application React

Naviguer à travers les pages d'un site statique nécessite toujours le chargement de fichiers HTML, mais pas pour Gatsby — ce sont des applications React.

> "Gatsby génère les pages HTML de votre site, mais crée également un runtime JavaScript qui prend le relais dans le navigateur une fois le HTML initial chargé" — gatsbyjs.org

Chaque balise d'ancrage pour une autre page deviendra une route par [Reach Router](https://reach.tech/router) (un outil pour construire des routes sur React avec accessibilité). Cela semble changer d'un fichier HTML à un autre alors qu'en fait, c'est une SPA mettant à jour le contenu sur la page.

### Optimisation des images

[HTTP Archive](https://httparchive.org/) suit de nombreux sites web populaires, la plupart des types de données demandés par les pages sont des images.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ymIv-FahsytuypmNU560UQ.png)
_[taille de transfert](https://httparchive.org/reports/page-weight#bytesTotal" rel="noopener" target="_blank" title="">Kiloctets totaux</a> — La somme de <a href="https://www.w3.org/TR/resource-timing-2/#dom-performanceresourcetiming-transfersize" rel="noopener" target="_blank" title=") de toutes les ressources demandées par la page est d'environ 1285,5 Ko pour mobile._

![Image](https://cdn-media-1.freecodecamp.org/images/1*AyrHOyvvLoTQAoBzRyBP-A.png)
_[Octets d'image](https://httparchive.org/reports/page-weight#bytesImg" rel="noopener" target="_blank" title=")s — La somme de la taille de transfert de toutes les images externes demandées par la page est de 491,0 Ko pour mobile._

L'optimisation des images peut être l'une des meilleures améliorations de performance sur un site web.

Moins d'octets à télécharger signifie moins de bande passante requise, donc le navigateur peut télécharger et rendre le contenu plus rapidement. Voici quelques-unes des optimisations que nous pouvons faire :

* Redimensionner à la même quantité d'espace nécessaire
* Générer des [images réactives](https://developer.mozilla.org/en-US/docs/Learn/HTML/Multimedia_and_embedding/Responsive_images#How_do_you_create_responsive_images) avec différentes résolutions pour ordinateur et téléphones
* Supprimer les métadonnées et appliquer la compression
* Appliquer le chargement paresseux pour accélérer le chargement initial de la page
* Afficher un espace réservé pendant le chargement de l'image

Cela peut demander beaucoup d'efforts et Gatsby a une solution : ce processus entier peut être automatisé.

Comme de nombreux outils dans Gatsby, [gatsbyjs-image](https://www.gatsbyjs.org/packages/gatsby-image/) est alimenté par GraphQL. Ce plugin configure les images avec différentes résolutions pour le téléchargement. Il crée des miniatures et applique la compression. Tout cela lors de l'étape de construction.

Lorsque l'image est en cours de chargement, une technique de "flou progressif" affiche un aperçu en très basse qualité qui est déjà dans le fichier HTML (ou simplement l'arrière-plan). Tout le travail est réduit à la rédaction de requêtes GraphQL pour créer l'optimisation automatisée. Consultez cette démonstration :

![Image](https://cdn-media-1.freecodecamp.org/images/1*NtTh_CL3BXESFTWvMfzR9w.gif)
_[Démonstration de Gatsby](https://using-gatsby-image.gatsbyjs.org/" rel="noopener" target="_blank" title=") pour des performances optimisées avec des images. La technique de "flou progressif" est également utilisée par Medium._

### Minification et noms de fichiers uniques

Ces techniques sont déjà largement utilisées par les frameworks et bibliothèques populaires, et dans Gatsby, il n'y a pas beaucoup de différence.

[Tous les fichiers sont minifiés](https://webpack.js.org/guides/production/#minification) par défaut lors de la construction avec webpack. Parce que les navigateurs ne se soucient pas du beau code, alors pourquoi ne pas tout écrire en une seule ligne ?

Les fichiers sont uniques lorsqu'ils sont construits en attribuant un hachage au nom du fichier. Si quelque chose change, un nouveau nom est donné au fichier.

La raison derrière cela est de permettre au serveur qui héberge ces fichiers de donner une longue durée pour le cache du navigateur.

Ainsi, lorsque l'utilisateur revient sur le site web, il a déjà les fichiers. Les mises à jour de vos fichiers donneront un nouveau nom de fichier lors de la construction. Ainsi, le navigateur télécharge le fichier car il n'y aura pas de correspondance avec celui du cache.

### Plus de ressources et au-delà

Gatsby se soucie de l'optimisation des performances afin que vous n'ayez pas à le faire.

Si vous êtes plus curieux de savoir comment Gatsby fonctionne sous le capot, consultez la [documentation](https://www.gatsbyjs.org/docs/behind-the-scenes/).

Je recommande également ce webinaire de l'équipe Gatsby, [Behind the Scenes: What makes Gatsby Great](https://www.gatsbyjs.com/behind-the-scenes/).

J'enseigne [Gatsby sur Udemy](https://www.udemy.com/gatsby-crie-seu-site-pessoal/) et j'ai travaillé sur le développement d'un [site web d'entreprise](http://upx.com) avec Gatsby, ainsi que mon [site web personnel](http://luanorlandi.github.io).

**J'enseigne et je diffuse à quel point Gatsby est génial. [Suivez-moi sur Twitter](https://twitter.com/luanorlandi) pour lire plus de sujets sur la tech et Gatsby.**