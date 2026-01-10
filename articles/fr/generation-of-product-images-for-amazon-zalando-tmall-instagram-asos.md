---
title: Comment générer des images de produits pour Amazon, Instagram, Zalando et Tmall
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-26T15:54:54.000Z'
originalURL: https://freecodecamp.org/news/generation-of-product-images-for-amazon-zalando-tmall-instagram-asos
coverImage: https://www.freecodecamp.org/news/content/images/2019/11/123brand.png
tags:
- name: image
  slug: image
- name: 'image optimization '
  slug: image-optimization
- name: image processing
  slug: image-processing
- name: responsive images
  slug: responsive-images
seo_title: Comment générer des images de produits pour Amazon, Instagram, Zalando
  et Tmall
seo_desc: 'By Anton Garcia Diaz

  Millions of people have already shifted from traditional tv to online content, and
  from traditional malls to online stores. Because of this, e-commerce and marketing
  teams need to deploy and maintain strong online presences for t...'
---

Par Anton Garcia Diaz

Des millions de personnes ont déjà abandonné la télévision traditionnelle au profit du contenu en ligne, et les centres commerciaux traditionnels au profit des boutiques en ligne. En conséquence, les équipes e-commerce et marketing doivent déployer et maintenir une forte présence en ligne pour leurs entreprises.

Cela signifie généralement gérer la boutique en ligne de la marque et être présent sur différentes places de marché couvrant diverses régions et segments de population. La liste sans fin des places de marché possibles pour présenter, promouvoir et vendre des produits ne fait que s'allonger.

Pour compliquer les choses, différentes places de marché ont des exigences et restrictions différentes concernant les images, ce qui peut ajouter une charge de travail pour les équipes devops et marketing. C'est également une source d'incohérence dans l'image publique d'une marque.

Ici, nous passerons en revue les principaux aspects à considérer lors de la mise en place d'un pipeline propre pour la production transparente d'images omnicanal.

## Une seule image maître via un seul pipeline

Pour simplifier les flux de travail et les rendre durables, une bonne pratique consiste à appliquer les principes de l'omnicanal aux images. Cela signifie essentiellement établir un pipeline unique et facile à configurer pour la création de variantes, à partir des mêmes images maîtresses ou pristinées. Avec cette approche, nous pouvons utiliser **la même image de produit pour chaque canal**. 

Notre pipeline doit recevoir des images maîtresses et produire les dérivés nécessaires pour alimenter les places de marché. Au minimum, il doit gérer un flux de travail comme celui-ci.

%[https://store.abraia.me/05bf471cbb3f9fa9ed785718e6f60e28/product-images-for-amazon-zalando-tmall-lamoda-ssg/generation-of-variants/index.html]

Bien sûr, un front-end et un stockage cloud ne sont pas nécessaires. Le pipeline peut simplement fonctionner en surveillant un dossier actif et en créant les variantes dès que les images maîtresses y sont déposées. Nous examinerons également cette option.

## Transformation et optimisation des images

Chaque canal web a son propre design et sa propre mise en page. En ce qui concerne les images, cela signifie des ratios d'aspect différents et spécifiques. De plus, chaque place de marché a généralement une politique d'images en place, qui limite la résolution et le poids de l'image et définit le format d'image admissible. Habituellement, elle spécifie également d'autres directives de style.

Examinons les principales opérations que nous souhaiterons accomplir avec notre pipeline.

### Redimensionnement, rognage, remplissage

Pour changer le ratio d'aspect d'une image, nous pouvons la rogner ou la remplir. Pour obtenir une image carrée à partir d'une image verticale, nous pouvons couper les parties supérieure et inférieure ou nous pouvons remplir les côtés gauche et droit avec des bandes blanches. 

Il existe des outils open source – comme ImageMagick – qui permettent d'effectuer ces opérations efficacement. Redimensionner une image avec ImageMagick pour limiter ses dimensions maximales à 800 px est aussi simple que cela :

```
convert input.jpg -resize 800x800 resized.jpg 
```

Cette instruction respecte le ratio d'aspect. Si l'image originale n'est pas carrée, alors l'image redimensionnée a une dimension inférieure à 800 px. Supposons que l'image est verticale et que nous la voulons pour Tmall, qui nécessite une image carrée de 800x800 px. Nous pouvons alors la remplir comme ceci :

```
convert resized.jpg  -gravity center -extent 800x800 padded.jpg
```

De plus, nous pouvons simplement la rogner pour qu'elle s'adapte aux dimensions :

```
convert input.jpg -gravity Center  -crop 800x800+0+0 +repage crop.jpg
```

Alors que certaines places de marché comme Tmall encouragent le remplissage des images avec des bandes blanches et leur marquage avec des logos pour les utiliser dans les pages de catégories, d'autres comme Amazon ou Lamoda interdisent cette pratique. 

![Image](https://www.freecodecamp.org/news/content/images/2019/11/crop_pad.png)
_Rognage (gauche), Redimensionnement (centre), Redimensionnement et remplissage (droite)_

Lorsque nous remplissons une image pour correspondre au ratio d'aspect, nous ne risquons pas de rogner des parties importantes. En fait, le remplissage est une astuce pour garder le ratio d'aspect inchangé. Cependant, le risque est réel lorsque nous rognons l'image. 

Il est donc bon de s'assurer en studio que nous respectons certaines exigences de composition fixées par chaque canal. Nous devons produire des images maîtresses avec une vue du produit compatible avec les différents ratios d'aspect que nous livrerons.

### Rognage intelligent

Il existe des algorithmes inspirés par l'attention humaine et la perception esthétique qui offrent une protection renforcée contre les mauvais rognages automatiques. Dans l'exemple suivant, avec le rognage intelligent d'images (ligne blanche), nous évitons de couper le visage contrairement à un simple rognage centré (ligne rouge).

![Image](https://www.freecodecamp.org/news/content/images/2019/11/smart-cropping-1.png)
_Exemple de rognage intelligent avec un [service cloud](https://abraia.me/workflows/) vs rognage centré_

Cette option est disponible dans certains services cloud. Si nous allons l'utiliser, nous devons vérifier qu'elle fonctionne correctement pour nous car de nombreuses solutions n'utilisent qu'une carte d'attention et ne prennent pas en compte les aspects esthétiques. Habituellement, choisir un certain nombre d'images représentatives, effectuer quelques tests avec elles et enfin vérifier les résultats suffit pour obtenir une bonne compréhension.

### Superposition de logos et de texte

Nous pouvons également avoir besoin d'ajouter notre logo de marque ou d'ajouter un message à l'image en superposant un graphique vectoriel ou un texte. De plus, dans de nombreux cas, nous avons besoin d'une stratégie de localisation de contenu en place – comme adapter les remises et la langue à une région de marché. En restant dans notre exemple, avec ImageMagick, nous pouvons superposer du texte sur une image remplie.

```
convert -fill black -pointsize 70 -gravity center -draw "rotate -90 text 0,-330 'MyBrandHere'" padded.jpg padded-with-brand.jpg
```

Une fois configuré pour une image, nous pouvons l'appliquer à toute autre image de mêmes dimensions. 

![Image](https://www.freecodecamp.org/news/content/images/2019/11/brand.png)
_Exemples de marquage d'images par lots utilisant le [service cloud d'Abraia](https://abraia.me/workflows/)_

Sinon, la gestion des typographies et des différents paramètres peut devenir délicate dans des flux de travail d'une certaine complexité. À cet égard, un [service cloud](https://abraia.me/workflows/) fournit généralement une interface front-end pour rendre la configuration intuitive et rapide, et plus pratique à gérer. Il traite également d'autres éléments comme les typographies ou la préservation de la qualité dans la recompression d'images. 

## Les flux de travail 

Il existe de nombreuses façons de déployer un pipeline de traitement d'images. Selon le débit d'images, nous pouvons avoir besoin de supporter différents types de flux de travail.  

### Traitement par lots

Dans le cas le plus simple – lorsque le débit est faible – une solution de traitement d'images par lots peut suffire. Avec ImageMagick, nous pouvons utiliser _mogrify_ (au lieu de convert) pour traiter toutes les images à l'intérieur d'un dossier. 

Dans certains cas, comme les versions d'images avec un texte dans différentes langues, nous pouvons avoir besoin de coder un script, mais ce n'est pas non plus un gros problème. Pour simplifier encore, nous pouvons utiliser un outil de traitement par lots dans le cloud où nous déposons des images et qui nous renvoie toutes les variantes dont nous avons besoin, comme dans la vidéo au début de l'article.

### Dossiers actifs

Pour les déploiements en interne où nous avons besoin de quelque chose de plus que le simple traitement d'images par lots, l'utilisation de dossiers actifs peut être une bonne option. Dans ce cas, nous devons configurer un worker qui surveille un dossier. Chaque fois qu'une image est déposée dans le dossier, le surveillant déclenche le processus qui crée toutes les variantes dont nous avons besoin.

À cet égard, Gulp est très pratique pour implémenter un pipeline de surveillance de dossier. [Ce dépôt GitHub apporte une implémentation prête à l'emploi de dossier actif](https://github.com/abraia/workflows) basée sur Gulp. Il nous permet de transformer des images en utilisant le service cloud d'Abraia ou de les optimiser en utilisant Imagemin (une solution open source). Une fois installé, le surveillant est facilement démarré avec une seule commande dans le terminal.

```
$ gulp
```

Cette vidéo montre le processus en action.

%[https://store.abraia.me/05bf471cbb3f9fa9ed785718e6f60e28/product-images-for-amazon-zalando-tmall-lamoda-ssg/hot-folder-gulp/index.html]

### Cloud complet

Les services cloud apportent généralement la solution la plus flexible et rapide à déployer. Cependant, il existe différentes façons d'adopter le cloud complet. Dans l'approche la plus simple du point de vue de l'utilisateur, un service de gestion et d'optimisation d'images prend en charge la transformation. Il gère également la livraison aux utilisateurs finaux (via un CDN) ou à d'autres canaux web comme les places de marché et les réseaux sociaux. L'utilisateur n'a besoin que de télécharger les images maîtresses et de configurer les transformations, généralement avec une interface graphique intuitive.

Dans les entreprises de taille moyenne à grande qui gèrent leur propre cloud, les services de différents fournisseurs sont généralement combinés. Dans ce cas, nous devons probablement gérer des buckets privés et publics. Nous pouvons avoir un service accédant à un bucket, créant les variantes et livrant les ressources ou les renvoyant simplement à un bucket différent. 

De plus, un pipeline cloud peut être partiellement implémenté en interne. Dans ce cas, nous avons des possibilités infinies. Cependant, un tel effort de développement n'a de sens que lorsqu'aucun service ne répond aux exigences et qu'il existe un besoin justifié pour une solution sur mesure.

## Résumé

La prise de vue en studio et la retouche photographique sont des opérations chronophages et coûteuses. Pouvoir utiliser le même matériel maître partout est très important pour garder les temps et les coûts sous contrôle.

Nous avons passé en revue les principaux aspects d'un pipeline complet chargé de créer des variantes d'images. D'une part, nous avons examiné les transformations que vous devez effectuer, du redimensionnement, du rognage ou du remplissage, à la superposition de textes et de graphiques. D'autre part, nous avons examiné les flux de travail à implémenter, du traitement par lots aux dossiers actifs ou aux solutions cloud complètes. Nous avons passé en revue certaines ressources open source importantes (comme ImageMagick ou Gulp) qui rendent possible la mise en place d'un pipeline que vous développez vous-même. 

En fin de compte, il y a deux principaux facteurs à considérer lors de la décision d'utiliser un service interne ou cloud. Premièrement, vous devez évaluer votre volonté de prendre en charge l'effort de développement. Deuxièmement, vous devez décider des fonctionnalités dont vous avez besoin, d'une interface facile à utiliser pour la configuration des variantes à des fonctionnalités avancées comme le rognage intelligent.