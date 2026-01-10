---
title: Exemple de Media Query CSS – Largeur d'écran Max et Min pour le Design Réactif
  Mobile
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2021-10-25T14:02:26.000Z'
originalURL: https://freecodecamp.org/news/media-query-css-example-max-and-min-screen-width-for-mobile-responsive-design
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/ferenc-almasi-NzERTNpnaDw-unsplash.jpg
tags:
- name: CSS
  slug: css
- name: responsive design
  slug: responsive-design
seo_title: Exemple de Media Query CSS – Largeur d'écran Max et Min pour le Design
  Réactif Mobile
seo_desc: "When you are designing a website, it is really important that your content\
  \ looks good on all screen sizes. \nIn this article, I will talk about how to use\
  \ responsive design and media queries to make this happen. I will also provide code\
  \ examples for m..."
---

Lorsque vous concevez un site web, il est vraiment important que votre contenu ait une belle apparence sur toutes les tailles d'écran. 

Dans cet article, je vais parler de la manière d'utiliser le design réactif et les media queries pour y parvenir. Je vais également fournir des exemples de code pour les media queries utilisant les largeurs d'écran maximales et minimales. 

## Qu'est-ce que le Design Réactif ? 

Le Design Réactif est la pratique qui consiste à s'assurer que votre contenu ait une belle apparence sur toutes les tailles d'écran. Tout sur le site web, y compris les mises en page, les polices et les images, doit s'adapter automatiquement à l'appareil de l'utilisateur. 

Au début des années 2000, les développeurs se concentraient sur le fait que leurs sites web aient une belle apparence sur les grandes tailles d'écran comme les ordinateurs portables et les ordinateurs de bureau. Dans le monde d'aujourd'hui, vous devez prendre en compte des appareils comme les téléphones mobiles, les tablettes, et même les montres.

Un composant important du design réactif est les media queries. 

## Qu'est-ce qu'une Media Query ? 

En CSS, une media query est utilisée pour appliquer un ensemble de styles basés sur les caractéristiques du navigateur, y compris la largeur, la hauteur ou la résolution de l'écran. 

Vous pouvez voir un exemple de media query sur la [page d'apprentissage de freeCodeCamp](https://www.freecodecamp.org/learn).

Pour les grandes tailles d'écran comme les ordinateurs de bureau, nous pouvons voir un menu de recherche dans le coin supérieur gauche.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/Screen-Shot-2021-10-19-at-7.50.41-PM.png)

Mais sur les appareils mobiles, il n'y a pas de menu de recherche et nous n'avons que les options de menu et le bouton de connexion.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/Screen-Shot-2021-10-19-at-7.54.59-PM.png)

## Syntaxe de base d'une media query

Voici la syntaxe de base pour une media query en CSS :

```css
@media media-type (media-feature){
/*Les styles vont ici*/
}
```

Décomposons ce que signifie cette syntaxe.

Le `@media` est un type de `At-rule` en CSS. Ces règles dicteront à quoi ressemblera le CSS en fonction de certaines conditions. 

Le type de media fait référence à la catégorie de media pour l'appareil. Les différents types de media incluent `all`, `print`, `screen` et `speech`.

* all - fonctionne pour tous les appareils
* print - fonctionne pour les appareils où le media est en mode aperçu avant impression
* screen - fonctionne pour les appareils avec écrans
* speech - fonctionne pour les appareils comme les lecteurs d'écran où le contenu est lu à haute voix à l'utilisateur

Selon la [documentation](https://developer.mozilla.org/en-US/docs/Web/CSS/@media), 

> Sauf lors de l'utilisation des opérateurs logiques `not` ou `only`, le type de media est facultatif et le type `all` est implicite. 

Vous pouvez choisir d'omettre le type de media et utiliser cette syntaxe à la place.

```css
@media (media-feature){
/*Les styles vont ici*/
}
```

La caractéristique de media fait référence aux caractéristiques du navigateur qui incluent la hauteur et la largeur de la fenêtre, l'orientation ou le rapport d'aspect. Pour une liste complète des caractéristiques de media possibles, veuillez [visiter la documentation MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/Media_Queries/Using_media_queries#media_features). 

Pour cet article, nous allons nous concentrer sur la caractéristique de media de largeur.

Si vous souhaitez créer des media queries plus complexes, vous pouvez utiliser des opérateurs logiques. 

* `and` - Cet opérateur est utilisé pour joindre plusieurs caractéristiques de media. Si toutes les caractéristiques de media sont vraies, alors les styles à l'intérieur des accolades seront appliqués à la page. 
* `not` - Cet opérateur inverse une requête vraie en une fausse et une requête fausse en une vraie. 
* `,` (virgule) - Cet opérateur séparera plusieurs caractéristiques de media par des virgules et appliquera les styles à l'intérieur des accolades si l'une des conditions est vraie. 

## Exemples de media queries

Examinons quelques exemples qui montrent comment utiliser les media queries en CSS.

Dans ce premier exemple, nous voulons que la couleur de fond change en bleu lorsque la largeur de l'appareil est de 600px ou moins.

En CSS, nous voulons ajouter un `(max-width: 600px)` pour la media query qui indique à l'ordinateur de cibler les appareils avec une largeur d'écran de 600px et moins.

À l'intérieur de la media query, nous changeons les styles de fond pour le body en `background-color: #87ceeb;`.

Voici la media query complète :

```css
@media (max-width: 600px) {
  body {
    background-color: #87ceeb;
  }
}
```

Voici l'exemple CodePen. Si vous cliquez sur Edit on CodePen dans le coin supérieur droit, vous pouvez tester cela sur Codepen. 

%[https://codepen.io/jessica-wilkins/pen/MWvJvoW?editors=1100]

![Image](https://www.freecodecamp.org/news/content/images/2021/10/Screen-Shot-2021-10-23-at-1.24.25-PM.png)

Dans ce deuxième exemple, nous voulons changer la couleur de fond de bleu à rouge si l'appareil a une largeur entre 600 et 768px. Nous pouvons utiliser l'opérateur `and` pour y parvenir.

```css
@media (min-width: 600px) and (max-width: 768px) {
  body {
    background-color: #de3163;
  }
}
```

Voici l'exemple CodePen complet pour que vous puissiez l'essayer :

%[https://codepen.io/jessica-wilkins/pen/rNzjGvp?editors=1100]

Lorsque vous le testez, vous devriez voir que la couleur de fond est bleue si la largeur de l'écran est inférieure à 600px ou supérieure à 768px. 

## Doit-on écrire des media queries séparées pour chaque appareil sur le marché ? 

La réponse courte à cette question est non.

Il y a beaucoup trop d'appareils sur le marché pour essayer d'écrire une media query pour chaque appareil. La technologie est toujours en évolution, ce qui signifie que de nouveaux appareils seront toujours mis sur le marché. 

Il est plus important de cibler une gamme d'appareils en utilisant des media queries. Dans [l'article de Cem Eygi sur freeCodeCamp](https://www.freecodecamp.org/news/css-media-queries-breakpoints-media-types-standard-resolutions-and-more/), il liste certains points de rupture courants utilisés pour les media queries. 

* 320px

480px : Appareils mobiles
* 481px

768px : iPads, Tablettes
* 769px

1024px : Petits écrans, ordinateurs portables
* 1025px

1200px : Ordinateurs de bureau, grands écrans
* 1201px et plus

 Écrans extra larges, TV

## Conclusion

Le Design Réactif est la pratique qui consiste à s'assurer que votre contenu ait une belle apparence sur toutes les tailles d'écran. Tout sur le site web, y compris les mises en page, les polices et les images, doit s'adapter automatiquement à l'appareil de l'utilisateur. 

En CSS, une media query est utilisée pour appliquer un ensemble de styles basés sur les caractéristiques du navigateur, y compris la largeur, la hauteur ou la résolution de l'écran. 

Voici la syntaxe de base pour une media query en CSS.

```css
@media media-type (media-feature){
/*Les styles vont ici*/
}
```

Le type de media est facultatif sauf si vous utilisez les opérateurs logiques `not` ou `only`. Si le type de media est omis, alors la media query ciblera tous les appareils. 

J'espère que vous avez trouvé cet article utile et bonne chance dans votre parcours CSS.