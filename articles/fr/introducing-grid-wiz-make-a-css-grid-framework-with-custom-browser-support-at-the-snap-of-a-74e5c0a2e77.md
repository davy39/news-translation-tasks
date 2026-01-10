---
title: 'Présentation de Grid Wiz : Créez un framework CSS grid avec support personnalisé
  en un clin d''œil'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-09T21:38:16.000Z'
originalURL: https://freecodecamp.org/news/introducing-grid-wiz-make-a-css-grid-framework-with-custom-browser-support-at-the-snap-of-a-74e5c0a2e77
coverImage: https://cdn-media-1.freecodecamp.org/images/1*KfiUYX2s29EMn7Kkn-uHUg.png
tags:
- name: CSS
  slug: css
- name: flexbox
  slug: flexbox
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Design
  slug: web-design
seo_title: 'Présentation de Grid Wiz : Créez un framework CSS grid avec support personnalisé
  en un clin d''œil'
seo_desc: 'By James Y Rauhut

  Today, I am thrilled to share with you a new, flexible grid framework generator:
  Grid Wiz!

  Grid frameworks are essential for experiences that span many codebases to keep the
  layouts aligned. The grid keeps columns at specific dimens...'
---

Par James Y Rauhut

Aujourd'hui, je suis ravi de vous présenter un nouveau générateur de framework de grille flexible : Grid Wiz !

Les frameworks de grille sont essentiels pour les expériences qui s'étendent sur de nombreuses bases de code afin de garder les mises en page alignées. La grille maintient les colonnes à des dimensions spécifiques lorsque l'utilisateur navigue entre différentes pages de l'expérience.

Alors que j'étais chez IBM, j'ai [présenté CSS Gridish](https://medium.freecodecamp.org/introducing-css-gridish-helping-teams-to-adapt-css-grid-today-3e031ab222de). Il avait une prémisse simple : donnez un fichier de configuration de votre conception de grille et obtenez à la fois CSS Flexbox et CSS Grid en retour. Cela aide les équipes à passer à CSS Grid une fois que les navigateurs de leurs utilisateurs [supportent la spécification finale](https://developer.mozilla.org/en-US/docs/Web/CSS/display#Browser_compatibility).

Il y avait deux décisions fondamentales dans CSS Gridish qui me troublaient : l'utilisation des unités `vw` et Node Sass. Les unités `vw` créaient plus de bugs et de mauvaises expériences de développement qu'elles n'en résolvaient. Node Sass est puissant et utilisé par beaucoup chez IBM, mais il limitait la flexibilité de l'environnement du package.

Alors pour mon prochain projet personnel, je me suis lancé dans Grid Wiz. Voyons pourquoi je suis beaucoup plus enthousiaste à propos de ce projet...

### Avantages

#### Support Flexible des Navigateurs

Différentes expériences ont différentes exigences de navigateurs en fonction des utilisateurs qui les visitent. Votre framework de grille doit également être performant avec la plus petite quantité de code nécessaire. Avec une compatibilité spécifique des navigateurs, vous pouvez supporter les bons navigateurs avec un code minimal.

![Image](https://cdn-media-1.freecodecamp.org/images/1*f4gTEp-z8ORl1vlHuXOkCw.gif)
_Ici, une démonstration du passage entre le mode `displayFlex` et `displayGrid` sans changements visuels._

Besoin de supporter des navigateurs jusqu'à Internet Explorer ? Utilisez le mode Flexbox avec le plus de code. Pas besoin d'Internet Explorer, mais de couvrir quelques versions légèrement plus anciennes des navigateurs actuels ? Le mode CSS Variables vous fera économiser beaucoup de code avec exactement la même sortie visuelle. Lorsque la base d'utilisateurs est enfin prête pour CSS Grid, vous obtiendrez la fonctionnalité supplémentaire avec le moins de code possible.

Voici une répartition des modes de support entre lesquels vous pouvez basculer :

![Image](https://cdn-media-1.freecodecamp.org/images/1*FDv0-546LbyfeobP57z6og.png)
_Passez entre ces modes de support [sur la démonstration en direct](https://grid-wiz.now.sh" rel="noopener" target="_blank" title=") pour voir la taille du CSS changer._

#### **Grilles Imbriquées**

Le HTML n'est pas écrit sur une seule couche. Un bon framework de grille doit vous permettre d'embarquer des divs dans des divs, tout en se souvenant du nombre de colonnes disponibles.

Sans les "subgrids", les utilisateurs de votre framework de grille risquent de sortir accidentellement de votre spécification de conception.

La prochaine mise à jour de CSS Grid inclura des subgrids nativement. Cependant, Grid Wiz vous permet de commencer à utiliser les subgrids dès aujourd'hui. Une fois que les navigateurs seront mis à jour avec la future fonctionnalité de CSS Grid, un nouveau mode de support sera ajouté pour la performance.

#### Flexibilité de l'Environnement

Écrire le code source en JavaScript isomorphe crée de nombreux cas d'utilisation possibles pour Grid Wiz. Voici quelques-unes des façons dont vous pouvez utiliser Grid Wiz :

![Image](https://cdn-media-1.freecodecamp.org/images/1*FNZBqNds2AZ58kKCBnhNjw.gif)
_Le site web de Grid Wiz est sans complexe une application web progressive. Enregistrez-le sur votre téléphone et modifiez les grilles pendant que vous êtes dans un avion si vous êtes bizarre comme ça._

* **Modifiez votre grille directement dans la [démonstration en direct](https://grid-wiz.now.sh) puis copiez le CSS directement dans votre base de code.** C'est une excellente méthode pour ceux qui sont encore nouveaux dans le développement web.
* **Distribuez votre grille à plusieurs projets avec un package Node.** [Ajoutez Grid Wiz comme dépendance](https://www.npmjs.com/package/grid-wiz) et compilez-le avec Gulp, Webpack, Rollup, ou autre chose.
* **Compilez la grille directement dans le processus de construction de votre application.** Cela peut sembler irresponsable, mais n'affecte pas vraiment les applications rendues côté serveur comme [le site web de Grid Wiz](https://grid-wiz.now.sh) lui-même. (Merci à [Next.js](https://nextjs.org/) pour avoir rendu le SSR facile.)

### Comment Utiliser Grid Wiz

Comment fonctionne Grid Wiz ? De la manière la plus simple possible.

Il suffit de fournir la spécification de conception de votre grille sous forme d'objet et d'obtenir une chaîne de CSS en retour :

```js
// Consultez https://grid-wiz.now.sh pour plus d'informations
const gridWiz = require("grid-wiz");

var yourGridCSS = gridWiz({
  prefix: "bx--", // Préfixe pour tous les noms de classes CSS. Peut être vide.
  support: "displayGrid", // `displayFlex`, `cssVariables`, ou `displayGrid`
  maxWidth: 1584, // Largeur maximale de la grille entière en pixels. Optionnel.
  progressive: false, // Inclure toutes les solutions de repli pour les navigateurs plus anciens que le support sélectionné
  subgrid: true, // Les grilles et lignes imbriquées connaissent le nombre restant de colonnes disponibles.
  breakpoints: [
    {
      name: "sm", // Préfixe du nom de classe pour le breakpoint.
      size: 0, // Largeur d'écran de départ en pixels du breakpoint.
      columns: 4, // Nombre de colonnes disponibles.
      gutter: 32, // Espace entre le contenu des colonnes adjacentes en pixels.
      margin: 0 // Espace à l'extérieur de la grille entière en pixels.
    },
    {
      name: "md",
      size: 672,
      columns: 8,
      gutter: 32,
      margin: 16
    },
    {
      name: "lg",
      size: 1056,
      columns: 16,
      gutter: 32,
      margin: 16
    }
  ]
});
```

### Conclusion

Grid Wiz permet aux équipes de passer en douceur des anciennes spécifications des navigateurs à CSS Grid, puis aux fonctionnalités pas encore publiées.

Je suis ravi de soutenir ce projet open-source à l'avenir et j'espère que vous contribuerez également. Si vous rencontrez des problèmes, n'hésitez pas à créer une nouvelle issue sur le [dépôt GitHub de Grid Wiz](https://github.com/seejamescode/grid-wiz) !

Si Grid Wiz vous aide, n'oubliez pas de laisser une étoile au [dépôt GitHub](https://github.com/seejamescode/grid-wiz) ! Vous pouvez également me suivre sur [Twitter](https://twitter.com/seejamescode).

![Image](https://cdn-media-1.freecodecamp.org/images/1*XUpzpAb6KjvcoENeAeiuXA.png)
_Merci à Twitter pour avoir open-sourcé leur bibliothèque [Twemoji](https://github.com/twitter/twemoji" rel="noopener" target="_blank" title=") !_

Un merci spécial à [Diego Hernandez](https://github.com/diego-codes), [Jen Downs](https://github.com/jendowns), et [Josh Black](https://twitter.com/__joshblack) pour leurs retours qui ont façonné ce projet. Merci également aux mainteneurs de [Babel](https://babeljs.io/), [Next.js](https://nextjs.org), et [Rollup](https://rollupjs.org) pour avoir rendu ce projet facile à réaliser.

Comme toujours, merci à freeCodeCamp et à la communauté pour être une excellente plateforme pour partager ces outils.