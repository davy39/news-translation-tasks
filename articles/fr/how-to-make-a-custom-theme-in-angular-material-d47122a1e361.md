---
title: Comment créer un thème personnalisé dans Angular Material
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-07T00:37:26.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-a-custom-theme-in-angular-material-d47122a1e361
coverImage: https://cdn-media-1.freecodecamp.org/images/1*u2PGM1dBW-M9oaRPMAVCXA.jpeg
tags:
- name: Angular
  slug: angular
- name: CSS
  slug: css
- name: Material Design
  slug: material-design
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment créer un thème personnalisé dans Angular Material
seo_desc: 'By Charlee Li

  Angular Material is a great library that implements Material Design for Angular
  2+. The official document is sufficient regarding the component usages, while there
  are few articles about how to customize the theme itself, specifically, ...'
---

Par Charlee Li

[Angular Material](https://material.angular.io/) est une excellente bibliothèque qui implémente [Material Design](https://material.io/design/) pour Angular 2+. La documentation officielle est suffisante concernant l'utilisation des composants, tandis qu'il existe peu d'articles sur la manière de personnaliser le thème lui-même, spécifiquement, les couleurs utilisées dans le thème.

Dans cet article, je souhaite résumer ce que j'ai appris ces derniers mois en personnalisant les thèmes Angular Material.

_Notez que cet article ne traite PAS d'[AngularJS Material](https://material.angularjs.org/latest/), qui est utilisé pour [AngularJS 1.x](https://angularjs.org/)._

### Articles Connexes

Quelques articles courants sur la personnalisation des thèmes sont :

* « [Theming your Angular Material app](https://material.angular.io/guide/theming) », le guide officiel pour les thèmes personnalisés,
* « [The complete guide to Angular Material Themes](https://medium.com/@tomastrajan/the-complete-guide-to-angular-material-themes-4d165a9d24d1) » par [Tomas Trajan](https://medium.com/@tomastrajan?source=post_header_lockup), qui fournit de nombreuses instructions non documentées. **Fortement recommandé.**

Je n'ai pas trouvé d'autres articles utiles et j'apprécierais que quelqu'un puisse fournir des ressources dans les commentaires.

### Comment Créer un Thème Personnalisé

Créer un thème Material est extrêmement simple : vous devez simplement choisir trois couleurs — **primaire**, **accent** et **avertissement** — et Angular Material fera le reste pour vous. [La page de la palette Material](https://material.io/design/color/#tools-for-picking-colors) explique clairement comment cela fonctionne, et vous pouvez également créer un thème visuellement avec [Color Tool](https://material.io/tools/color/).

En ce qui concerne le code, tout ce que vous devez faire est de créer le fichier de thème suivant :

```
// theme.scss@import '~@angular/material/theming';
```

```
$my-theme-primary: mat-palette($mat-green);$my-theme-accent : mat-palette($mat-amber);$my-theme-warn   : mat-palette($mat-red);
```

```
$my-theme: mat-light-theme(    $my-theme-primary,    $my-theme-accent,    $my-theme-warn);
```

Ensuite, vous devez appliquer ce thème dans votre fichier principal `style.scss` :

```
@import "theme.scss";
```

```
@include mat-core();@include angular-material-theme($my-theme);
```

### Comment Utiliser un Thème Personnalisé dans les Composants

Après avoir créé notre propre thème, des exigences comme celle-ci peuvent survenir :

> Je veux créer une zone de texte. La couleur du texte, la couleur de fond et la couleur de la bordure doivent toutes provenir de notre propre thème, et non être codées en dur.

Cette exigence est assez courante — après tout, pouvoir être utilisé dans les composants est exactement la raison pour laquelle nous voulons créer un thème personnalisé. Le problème est de savoir comment.

#### L'approche par mixin

Le premier document officiel que j'ai partagé proposait une méthode d'utilisation des mixins SCSS. Je l'appelle une approche « bottom-up », qui comprend les étapes suivantes :

1. Chaque composant définit un mixin de thème et récupère les couleurs à partir du paramètre `$theme`.
2. Un fichier global `theme.scss` définit le thème personnalisé, puis inclut tous les mixins de thème des composants et les appelle avec le thème personnalisé.

![Image](https://cdn-media-1.freecodecamp.org/images/ZZFo93hwLrqUn3ntyKFegxNciXyufD0I3nnv)

En plus de la définition de `theme.scss` mentionnée ci-dessus, chaque composant doit créer un fichier de thème comme ceci :

```
// src/app/comp-a/comp-a.theme.scss@import '~@angular/material/theming';
```

```
@mixin comp-a-theme($theme) {          // définir le mixin  $primary: map-get($theme, primary);  // récupérer la définition de couleur  button {                             // appliquer le thème au composant    background-color: mat-color($primary);  }}
```

Et probablement, vous voulez un fichier `custom-theme.scss` pour importer tous les thèmes au niveau des composants :

```
// src/app/custom-theme.scss@import '~@angular/material/theming';@import 'src/app/comp-a/comp-a.theme';@import 'src/app/comp-b/comp-b.theme';
```

```
@mixin custom-themes($theme) {  @include comp-a-theme($theme);  @include comp-b-theme($theme);}
```

Ensuite, importez le fichier `custom-theme.scss` ci-dessus dans votre fichier `theme.scss` :

```
// theme.scss...@import './custom-theme';@include custom-themes($my-theme);
```

Cette hiérarchie fonctionne et est probablement la seule façon _lorsque vous devez supporter plusieurs thèmes_.

Cependant, la plupart du temps, nous ne supportons qu'un seul thème, et l'utilisation d'un mixin peut être fastidieuse. Principalement, il y a trois inconvénients avec cette approche :

1. Chaque référence de couleur individuelle nécessite un fichier `.theme.scss` séparé.
2. `custom-theme.scss` doit savoir exactement quels composants fournissent des thèmes personnalisés. Cela crée des dépendances inutiles.
3. Plus important encore, les fichiers de thème au niveau des composants ne sont pas encapsulés.

Les premier et deuxième points sont assez explicites. Permettez-moi d'expliquer un peu le point 3. Cela implique quelques connaissances de fond appelées « View Encapsulation ».

Angular utilise une technique appelée « [View Encapsulation](https://angular.io/api/core/ViewEncapsulation) » pour [garder le CSS des composants local](https://angular.io/guide/component-styles). En d'autres termes, les règles définies pour un composant resteront dans ce composant et n'affecteront pas les autres composants.

De cette manière, vous pouvez définir librement les noms de classes CSS dans votre composant sans vous soucier des conflits de noms. Cependant, l'encapsulation de la vue n'est effectuée que si le CSS est défini via `@Component`, c'est-à-dire `@Component({ styleUrls: ['./comp-a.scss'] })`.

En ce qui concerne notre fichier de thème personnalisé `comp-a.theme.scss`, puisque celui-ci est importé directement par `custom-theme.scss`, _ses règles ne sont pas encapsulées_ et s'appliqueront donc à tous les éléments de la page. Dans l'exemple ci-dessus, j'ai utilisé le code suivant (qui était FAUX !) :

```
@mixin comp-a-theme($theme) {  button { ... }    // Cela s'appliquera à TOUS les boutons !}
```

Mais cela appliquera le style à tous les boutons au lieu de ceux appartenant uniquement à `comp-a`. Vous devez faire quelque chose comme `comp-a button` pour que cela fonctionne correctement.

#### L'approche directe

Par conséquent, je propose une meilleure approche. Au lieu d'utiliser un mixin, nous laissons chaque composant inclure le fichier de thème et utiliser directement la définition des couleurs.

Dans cette approche, le fichier de thème du composant ressemblera à ceci :

```
// NOTE: faites simplement cela dans votre fichier scss régulier.
// Pas besoin de créer un fichier de thème séparé !// src/app/comp-a/comp-a.scss@import 'src/theme.scss';
```

```
$primary: map-get($my-theme, primary);button {  background-color: mat-color($primary);}
```

Et c'est tout.

Voyons comment cela fonctionne. Tout d'abord, les règles liées au thème sont placées dans le fichier SCSS du composant, donc aucun fichier de thème supplémentaire au niveau du composant n'est requis. Deuxièmement, le fichier principal `theme.scss` n'a pas besoin de connaître les thèmes au niveau des composants (puisqu'il n'a pas besoin de les importer), donc une simple définition de thème est adéquate. Troisièmement, le fichier SCSS du composant est utilisé avec `@Component` et est donc correctement encapsulé, ce qui signifie que nous pouvons simplement définir des règles pour `button`.

### Clés de Thème Prédéfini

Probablement, vous avez remarqué le problème suivant. Que sont `foreground`, `primary` dans les fichiers de thème ci-dessus (`map-get($my-theme, primary)`) ? Y a-t-il d'autres clés que je peux utiliser ?

Eh bien, ces « clés » font référence à différentes couleurs définies dans le thème. Cependant, je n'ai pas trouvé de documents expliquant ces « clés », donc la seule façon que j'ai trouvée est de _lire le code source_. (Bien qu'il soit dit que les bons programmeurs devraient lire le code, _devoir_ lire le code n'est définitivement pas un bon signe pour une bibliothèque.)

Ouvrez `node_modules/@angular/material/_theming.scss` et vous verrez les définitions de ces clés. Pour référence future, je souhaite résumer les clés ici.

```
$theme  |- primary  |- accent  |- warn  |- foreground  |   |- base  |   |- divider  |   |- dividers  |   |- disabled  |   |- disabled-button  |   |- disabled-text  |   |- hint-text  |   |- secondary-text  |   |- icon  |   |- icons  |   |- text  |   |- slider-min  |   |- slider-off  |   `- slider-off-active  |- background  |   |- status-bar  |   |- app-bar  |   |- background  |   |- hover  |   |- card  |   |- dialog  |   |- disabled-button  |   |- raised-button  |   |- focused-button  |   |- selected-button  |   |- selected-disabled-button  |   |- disabled-button-toggle  |   |- unselected-chip  |   `- disabled-list-option  `- is-dark         // bool, si thème sombre ou non
```

Par exemple, si vous souhaitez rendre un texte désactivé dans votre composant, vous pouvez utiliser le code suivant :

```
$foreground: map-get($my-theme, foreground);.disabled-text {  color: mat-color($foreground, disabled-text);}
```

D'accord, ce sont quelques leçons que j'ai apprises en luttant avec Angular Material. J'espère que cet article est utile si vous êtes confronté à des problèmes similaires.