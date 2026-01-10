---
title: 'Grille 8 points : Typographie sur le Web'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-13T16:22:43.000Z'
originalURL: https://freecodecamp.org/news/8-point-grid-typography-on-the-web-be5dc97db6bc
coverImage: https://cdn-media-1.freecodecamp.org/images/1*a9-nNNgjaAsA8ImC-JF4NA.png
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: Design Systems
  slug: design-systems
- name: technology
  slug: technology
- name: typography
  slug: typography
seo_title: 'Grille 8 points : Typographie sur le Web'
seo_desc: 'By Elliot Dahl

  Web typography is confusing. Do you know the best practices?

  When I started looking around at popular websites to figure out the best practices
  for web typography, I must admit I was baffled. Below are some examples of typography
  scale...'
---

Par Elliot Dahl

## La typographie web est déroutante. Connaissez-vous les meilleures pratiques ?

Lorsque j'ai commencé à examiner des sites web populaires pour comprendre les meilleures pratiques en matière de typographie web, je dois admettre que j'étais perplexe. Voici quelques exemples d'échelles typographiques que j'ai tirées de quelques sites web et systèmes de design populaires. Pouvez-vous trouver le motif unificateur ?

![Image](https://cdn-media-1.freecodecamp.org/images/p7a5EwZKGq5FrIg-oXZ58WptVdYXB372hY97)
_Échantillons simplifiés pour s'adapter à une échelle standard_

Il est clair qu'il existe différentes approches des systèmes de typographie. La réalité est que, en tant que communauté web, nous ne sommes pas tous d'accord. Cependant, comme pour la plupart des problèmes de design, tout commence par répondre aux besoins des utilisateurs.

## Les trois archétypes des systèmes de typographie

Voici trois archétypes généraux de systèmes de typographie. La plupart des entreprises utiliseront ces trois approches à un moment donné, mais il est important de reconnaître les besoins sous-jacents des utilisateurs auxquels chaque orientation répond.

#### Site marketing

* **Objectif** : Conçu pour raconter une histoire spécifique et inspirer les visiteurs à passer du temps et/ou de l'argent sur le site.
* **Exigences** : Chaque police de caractères aura besoin de son propre ensemble de styles et la variété des tailles sera basée sur la direction artistique plus que sur l'ajustement des éléments.
* **Cas d'utilisation responsive** : Le système devra s'adapter à travers plusieurs tailles, du mobile au desktop.

![Image](https://cdn-media-1.freecodecamp.org/images/q4CC1WIXgGD1tXirl1L3tpkh7SOKKDgKPdT4)

Les expériences web conçues pour vous vendre quelque chose se retrouvent dans cette catégorie. Les plus ambitieuses brisent toutes les règles de la typographie pour créer des expériences convaincantes et captivantes.

Bien que beaucoup de réflexion soit mise dans ces sites, l'accent est mis sur le fait de faire une entrée en matière plutôt que sur un système extensible qui peut être construit dans le futur. Ces sites ont généralement une durée de vie courte et sont entièrement abandonnés pour une refonte complète.

Un exemple avancé de cela est la fonction d'interpolation utilisée par [Leigh Taylor](https://twitter.com/lat) et [Nick Jones](https://twitter.com/narrowd) sur [la page d'accueil d'Invision](https://www.invisionapp.com/).

Le `<h1>` a une `font-size: calc(32px + ((24 * (100vw — 800px))/799))`. La typographie de la page est calculée de manière méticuleuse pour fonctionner à chaque taille d'écran.

> « Utiliser les maths pour faire de la direction artistique dynamique » — [Leigh Taylor](https://twitter.com/lat)

#### Blog/Site d'information

* **Objectif** : Transmettre une grande quantité d'informations basées sur du texte.
* **Exigences** : La zone de lecture principale peut utiliser un système de hauteur de ligne basé sur un ratio, comme le fait cet article Medium.
* **Cas d'utilisation responsive** : Sera probablement responsive mais en maintenant l'accent sur la lisibilité.

![Image](https://cdn-media-1.freecodecamp.org/images/JWKQZX2pnsELv6JkIOGshLQ3imrMOaRYEkTk)

Cet article Medium est un exemple d'expérience web construite pour la lecture de longs formats.

L'accent n'est pas mis sur l'interprétation de petites visualisations ou le remplissage de formulaires. Les ratios de taille qu'ils ont choisis sont spécifiquement conçus pour la lisibilité, contraints pour obtenir la longueur de ligne souhaitée. Je peux lire chaque ligne confortablement parce que la typographie a été soigneusement élaborée pour répondre à mes besoins en tant que lecteur.

#### Produit

* **Objectif** : Conçu pour résoudre un problème utilisateur comme la déclaration d'impôts, la gestion d'un dépôt git, ou la visualisation de métriques de performance.
* **Exigences** : Le texte doit s'intégrer parfaitement dans la hiérarchie des éléments. Le texte est principalement utilisé pour les étiquettes, les instructions et les données affichées.
* **Cas d'utilisation responsive** : Minimalement responsive. Les produits hautement développés utiliseront un design adaptatif, ce qui signifie différentes expériences pour le mobile et le desktop. L'accent est mis sur la hiérarchie des éléments qui soutiennent l'expérience utilisateur.

![Image](https://cdn-media-1.freecodecamp.org/images/AFvMJ3ln64feUAj9J5VvI-qsRE9hgmpSSff0)

Le Material Design de Google est un langage de design populaire applicable à de nombreux cas d'utilisation de produits.

La [méthode d'espacement](https://material.io/design/layout/spacing-methods.html#baseline) de Material est basée sur un système de grille de composants de 8pt et une grille de base de 4pt pour la typographie. Ils essaient de mettre à l'échelle les hauteurs de ligne avec des incréments de 4. La mise à l'échelle par incréments de 8 avec votre grille de base peut être difficile car les hauteurs de ligne disponibles sont trop éloignées pour certaines tailles de texte.

Permettre à certaines des tailles de police d'être accompagnées d'une hauteur de ligne plus appropriée est une excellente voie à suivre. Vous pouvez toujours ajuster l'espacement au-dessus ou en dessous d'une ligne donnée de 4px pour l'aligner avec la grille atomique plus grande.

Lorsqu'elle est appliquée, le système de grille de base a la capacité d'aligner le système spatial des éléments (grille de 8pt) avec le système de typographie pour créer un rythme vertical convaincant dans le design.

## Mise en œuvre de la typographie web — en réalité

Il est possible d'avoir une interface utilisateur structurée et opinionnée, adhérant à une grille de 8pt, qui possède également une zone de lecture en long format.

Permettez au système de grille de base fixe de gérer le texte à l'intérieur de vos composants structurés et utilisez une échelle modulaire pour créer une expérience de lecture optimale pour le blog ou la documentation que vous avez ajoutés à votre site.

La plupart des entreprises de produits numériques font déjà cela entre leur page de destination marketing, le produit numérique et leur documentation. Prendre la décision de structurer ces domaines typographiques séparément peut vous libérer d'une complexité insoutenable.

![Image](https://cdn-media-1.freecodecamp.org/images/AQRwQogPt9TiBR82ig3AbFMJBPZO8wz-KQG2)
_Mélange de types de contenu ensemble_

## Le piège — Ems, rems et pixels, oh là là !

Pour exprimer un système clair et cohérent, les mesures typographiques doivent être facilement interprétées par l'équipe produit qui le construit.

Les unités relatives comme [rems et ems](https://css-tricks.com/rem-global-em-local/) sont parfois mal comprises et, selon mon expérience, cela conduit à un système typographique insoutenable. Par exemple, le ratio entre une taille de police de 14px et une hauteur de ligne de 20px ne devrait pas être capturé en unités relatives car ce ratio devrait changer à mesure que la taille de la police augmente.

Définir une hauteur de ligne de 1,4285714286em est ridicule, car la plupart des gens ne peuvent pas faire ce genre de maths dans leur tête. Si la taille de la police augmente à 16px, le navigateur rendra une hauteur de ligne de 22,857142px et ce genre de division de pixels est un casse-tête en attente de se produire. Cela crée de la confusion et est un mauvais usage des unités relatives. Voir une liste complète des [unités absolues vs relatives ici](https://www.w3schools.com/cssref/css_units.asp).

Pourquoi tant de systèmes de design sont-ils basés sur un dimensionnement relatif aujourd'hui ? La réponse est « accessibilité ».

Cependant, les navigateurs ne mettent pas à l'échelle la taille de base de la police lorsque vous zoomez avec `command +`. Il existe des outils d'accessibilité qui mettront à l'échelle les tailles de base de la police pour les utilisateurs qui en ont besoin. Je recommande de le tester correctement pour vous assurer que c'est l'expérience que vous voulez que les utilisateurs aient. L'accessibilité « cocher la case » peut faire plus de mal que de bien.

Utiliser des rems et des ems dans votre site/application est incroyablement puissant. Il existe de nombreux cas d'utilisation très intéressants et ils devraient être une partie importante de votre boîte à outils.

Ma suggestion est de les utiliser avec parcimonie jusqu'à ce que vous ayez une utilisation solide pour eux. Les intégrer au cœur de votre système typographique peut vous ouvrir à la confusion et à des expériences utilisateur inattendues.

## Typographie sur grille de 8 points

La partie la plus puissante du concept de grille de 8 points est sa capacité à garantir la cohérence dans tous vos designs. Vous devrez évaluer les besoins de vos utilisateurs et la meilleure façon de mettre à l'échelle votre typographie pour répondre à ces besoins.

Je vous encourage vivement à ce que le design et l'ingénierie collaborent pour finaliser ces normes pour une entreprise/produit.

Voici des exemples de quelques noms familiers : [Google Material](https://material.io/design/typography/the-type-system.html#type-scale), [Pivotal](https://styleguide.pivotal.io/typography), [Atlassian](https://atlassian.design/server/foundations/typography/), [Intuit](https://designsystem.quickbooks.com/foundations/typography/).

![Image](https://cdn-media-1.freecodecamp.org/images/F8E-aK4T2KYa7HSEcgDUrq5ahyP9mvJv-M7e)
_Échantillons simplifiés pour s'adapter à une échelle standard_

#### Références et lectures connexes

* Priyanka Godbole : [Un framework pour créer un système d'espacement prévisible et harmonieux pour un handoff design-dev plus rapide](https://blog.prototypr.io/a-framework-for-creating-a-predictable-and-harmonious-spacing-system-8eee8aaf773c)
* Richard Rutter : [Les éléments du style typographique appliqués au Web](http://webtypography.net/intro/)
* Ian Yates : [Comment établir une échelle typographique modulaire](https://webdesign.tutsplus.com/articles/how-to-establish-a-modular-typographic-scale--webdesign-14927)
* Nathan Curtis : [L'espace dans les systèmes de design](https://medium.com/eightshapes-llc/space-in-design-systems-188bcbae0d62)
* Vincent De Oliveira : [Plongée profonde en CSS : métriques de police, hauteur de ligne et alignement vertical](https://iamvdo.me/en/blog/css-font-metrics-line-height-and-vertical-align)
* Kezz Bracey : [Pourquoi vous devriez utiliser des mises en page basées sur Rem](https://webdesign.tutsplus.com/tutorials/why-you-should-be-using-rem-based-layouts--cms-27828)

#### Articles précédents sur la grille 8 points :

1. [Introduction au système de grille 8 points](https://builttoadapt.io/intro-to-the-8-point-grid-system-d2573cde8632)
2. [Grille 8 points : Bordures et mises en page](https://builttoadapt.io/8-point-grid-borders-and-layouts-e91eb97f5091)
3. [Grille 8 points : Rythme vertical](https://builttoadapt.io/8-point-grid-vertical-rhythm-90d05ad95032)

#### Questions :

C'est quelque chose que je continue d'explorer. Avez-vous un bon exemple à partager ? Avez-vous une approche différente pour un système typographique 8pt ?

Si vous avez des idées, n'hésitez pas à laisser un commentaire ou à me contacter sur [Twitter](https://twitter.com/Elliotdahl).