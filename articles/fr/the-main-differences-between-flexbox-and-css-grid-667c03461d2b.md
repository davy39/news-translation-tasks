---
title: Les principales différences entre Flexbox et CSS Grid
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-14T17:40:57.000Z'
originalURL: https://freecodecamp.org/news/the-main-differences-between-flexbox-and-css-grid-667c03461d2b
coverImage: https://cdn-media-1.freecodecamp.org/images/0*04uQld7C_oOhT6d0
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: UX
  slug: ux
seo_title: Les principales différences entre Flexbox et CSS Grid
seo_desc: 'By Shaira Williams

  Dimensions define the primary demarcation between Flexbox and CSS Grid. Flexbox
  was designed specifically for one-dimensional layouts, while CSS Grid is engineered
  to enable two-dimensional layouts. Therefore, CSS Grid can easily r...'
---

Par Shaira Williams

Les dimensions définissent la principale démarcation entre Flexbox et CSS Grid. Flexbox a été conçu spécifiquement pour les mises en page unidimensionnelles, tandis que CSS Grid est conçu pour permettre des mises en page bidimensionnelles. Par conséquent, CSS Grid peut facilement rendre les lignes et les colonnes simultanément.

En termes profanes, CSS Grid présente une toile plus grande, tandis que Flexbox offre une fonctionnalité minutieuse qui opère dans un espace restreint. Les grilles ont été conçues pour une organisation bidimensionnelle.

Cependant, les deux spécifications partagent certains points communs, et si vous savez comment utiliser les boîtes flexibles, vous trouverez certains concepts qui vous aideront à comprendre les grilles CSS.

Dans cet article, nous allons passer en revue les principales différences entre Grid et Flexbox, résumées comme suit :

* Flexbox est conçu pour les mises en page unidimensionnelles, et Grid pour les mises en page bidimensionnelles.
* L'approche de CSS Grid est la mise en page d'abord, tandis que l'approche Flexbox est principalement le contenu.
* La mise en page Flexbox est mieux adaptée aux composants d'application et aux mises en page à petite échelle, tandis que la mise en page Grid est conçue pour des mises en page à plus grande échelle qui ne sont pas linéaires dans leur conception.

### **_Faire connaissance avec Flexbox et Grid_**

#### Le Flexbox unidimensionnel

CSS Flexible Box Layout (ou Flexbox) permet aux concepteurs de positionner correctement les éléments réactifs dans les écrans de différentes tailles. Les outils incluent :

* la mise en page de boîte pour les documents,
* une mise en page en ligne pour définir l'apparence du texte sur les écrans,
* une mise en page de tableau pour représenter les données tabulaires en une dimension,
* et un mode de mise en page positionné qui permet un positionnement explicite des éléments réactifs.

Flexbox est populaire parmi les développeurs front-end, car il permet aux développeurs de créer plusieurs instances de mises en page dynamiques et d'aligner facilement le contenu dans des conteneurs.

Le [module de boîte flexible](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout/Basic_Concepts_of_Flexbox) a été conçu comme un modèle de présentation unidimensionnel et comme une méthode qui peut fournir une distribution d'espace entre les éléments d'interface et des fonctions d'alignement puissantes. Lorsque nous décrivons le flexbox comme unidimensionnel, nous décrivons le fait que le flexbox traite les mises en page dans une dimension à la fois, comme une ligne ou une colonne. Cela peut être comparé au modèle bidimensionnel de la mise en page de grille CSS, qui contrôle les colonnes et les lignes ensemble.

```
<div class="wrapper"> <div>One</div> <div>Two</div> <div>Three</div> <div>Four</div> <div>Five</div></div>
```

```
.wrapper { width: 500px; display: flex; flex-wrap: wrap;}.wrapper > div { flex: 1 1 150px;}
```

![Image](https://cdn-media-1.freecodecamp.org/images/6Ssxcnfne8C1dh1DJG3R5-YwWAIE9QvN9O2Z)

Avantages :

* Flex peut être arrangé dans n'importe quelle direction
* Flex peut avoir son ordre visuel inversé ou réarrangé.
* Les éléments peuvent être alignés dans votre conteneur ou entre eux.
* Support tous les navigateurs.

Inconvénients :

* Problèmes de performance

![Image](https://cdn-media-1.freecodecamp.org/images/D24zCPIeqAHHfGYHIKqpL6mvRA4RuwIElX3f)

#### La Grid bidimensionnelle

CSS Grid aligne les éléments en colonnes et en lignes, permettant aux développeurs de contrôler facilement le rendu et l'apparence des grandes mises en page et des pages entières destinées aux écrans de bureau, de tablette et de smartphone.

Les éléments sont placés à l'intérieur des cellules définies par la grille. La création et la définition des mises en page globales restent le point fort de CSS Grid. Internet Explorer, Chrome, Safari, Edge et Firefox supportent Grid. Notamment, Opera Mini, Blackberry Browser, QQ Browser et Baidu Browser ne supportent pas Grid.

Il offre une automatisation pour créer une mise en page, ou définir des règles de placement automatique qui effectuent des placements à l'intérieur d'une grille donnée.

```
<div class="wrapper"> <div>One</div> <div>Two</div> <div>Three</div> <div>Four</div> <div>Five</div></div>
```

```
.wrapper { display: grid; grid-template-columns: repeat(3, 1fr);}
```

![Image](https://cdn-media-1.freecodecamp.org/images/D63eH5bxTDwCD6Jcj5f40mijVkEslI1jgLUh)

Avantages :

* Les pistes de grille sont créées dans votre feuille de style.
* Réduction de la taille des fichiers.
* Le prototypage avec CSS Grid est rapide et efficace.

Inconvénients :

* Non supporté par tous les navigateurs

![Image](https://cdn-media-1.freecodecamp.org/images/PST350rKCFY3yBbxJHvjEPF61Ht8IoiEtQCo)

### **Différences entre Flex et Grid**

#### **Dimensionnalité et Flexibilité**

Flexbox offre un meilleur contrôle sur l'alignement et la distribution de l'espace entre les éléments. Étant unidimensionnel, Flexbox ne traite que des colonnes ou des lignes. Ce système fonctionne pour les petites mises en page, mais ne peut pas rendre les affichages complexes tels que le texte ou les propriétés centrées sur les documents qui permettent les flottants et les colonnes.

Grid a des capacités de mise en page bidimensionnelle qui permettent des largeurs flexibles comme unité de longueur. Cela compense les limitations de Flex.

#### **Alignement**

Flexbox permet un réglage fin des alignements pour garantir un partage exact des spécifications. Flex Direction permet aux développeurs d'aligner les éléments verticalement ou horizontalement, ce qui est utilisé lorsque les développeurs créent et inversent les lignes ou les colonnes.

Pour des alignements plus larges dans les deux dimensions simultanément, CSS Grid déploie des unités de mesure fractionnaires pour la fluidité de la grille et une fonctionnalité de mot-clé auto pour ajuster automatiquement les colonnes ou les lignes. L'automatisation intégrée évite aux développeurs les régimes de retravail qui peuvent potentiellement provenir de calculs confus.

#### **Gestion des éléments**

Flex Container est l'élément parent tandis que Flex Item représente les enfants. Le Flex Container peut garantir une représentation équilibrée en ajustant les dimensions des éléments. Cela permet aux développeurs de concevoir pour des tailles d'écran fluctuantes.

Pour affiner cette esthétique, Grid supporte à la fois le placement de contenu implicite et explicite. Son automatisation intégrée lui permet d'étendre automatiquement les éléments de ligne et de copier les valeurs dans la nouvelle création à partir de l'élément précédent.

### Conclusion

Flexbox et CSS Grid permettent tous deux une mesure puissante de contrôle sur leurs domaines respectifs de développement front-end. Cependant, leurs capacités sont exponentiées lorsqu'ils sont combinés, utilisant leurs forces respectives pour créer une expérience extrêmement fluide, personnalisable, belle, fluide et simple.

Combiner leur code entraîne également une configuration plus légère où l'abstraction dans les deux domaines déborde dans l'autre. Il existe de vastes applications pour les deux options, et encore plus lorsqu'elles sont combinées en une configuration puissante.

En savoir plus sur [la relation de la mise en page de grille avec d'autres méthodes de mise en page ici](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Grid_Layout/Relationship_of_Grid_Layout).

Cet article a été conseillé par des membres du [blog techiespad](https://techiespad.com/).