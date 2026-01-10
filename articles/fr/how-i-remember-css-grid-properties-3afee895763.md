---
title: Comment je retiens les propriétés de CSS Grid
subtitle: ''
author: Zell Liew
co_authors: []
series: null
date: '2018-10-25T05:38:32.000Z'
originalURL: https://freecodecamp.org/news/how-i-remember-css-grid-properties-3afee895763
coverImage: https://cdn-media-1.freecodecamp.org/images/0*9_DylWfIulrq5tTl.png
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
seo_title: Comment je retiens les propriétés de CSS Grid
seo_desc: 'The syntax for CSS Grid is foreign and hard to remember. But if you can’t
  remember CSS Grid’s syntax, you won’t be confident when you use CSS Grid.

  To wield CSS Grid effectively, you need to remember its properties and values.

  I want to share how I r...'
---

La syntaxe de CSS Grid est étrangère et difficile à retenir. Mais si vous ne pouvez pas retenir la syntaxe de CSS Grid, vous ne serez pas confiant lorsque vous l'utiliserez.

Pour maîtriser CSS Grid efficacement, vous devez retenir ses propriétés et valeurs.

Je veux partager comment je retiens les propriétés les plus courantes de CSS Grid aujourd'hui. Cela vous aidera à utiliser CSS Grid sans chercher frénétiquement sur Google.

### Groupes de propriétés

Je retiens CSS Grid selon quatre groupes de propriétés :

1. La grille explicite
2. Les espaces
3. L'alignement des éléments
4. La grille implicite

### La grille explicite

Disons que vous voulez créer une grille avec 4 colonnes et 3 lignes. Vous dites ces 4 colonnes et 3 lignes à voix haute. C'est explicite.

Si vous déclarez le nombre de lignes et de colonnes dans votre grille, la grille est explicite.

Vous pouvez utiliser deux propriétés pour créer une grille explicite :

1. `grid-template-columns`
2. `grid-template-rows`

`grid-template-columns` vous permet de définir le nombre de colonnes. `grid-template-rows` vous permet de définir le nombre de lignes.

```
.grid {  display: grid;   grid-template-columns: 1fr 1fr 1fr 1fr;   grid-template-rows: 3em 3em 3em;}
```

Cela crée une grille avec quatre colonnes et trois lignes.

Voir le Pen [XPyGZp](https://codepen.io/zellwk/pen/XPyGZp/) par Zell Liew ([@zellwk](https://codepen.io/zellwk)) sur [CodePen](https://codepen.io/).

Comment savez-vous qu'il y a quatre colonnes et trois lignes ?

`grid-template-columns` crée une nouvelle colonne pour chaque valeur de longueur que vous ajoutez. Dans la déclaration `grid-template-columns` ci-dessus, nous avons quatre valeurs `1fr`. Cela signifie quatre colonnes.

`grid-template-rows` fonctionne de la même manière. La grille ci-dessus a trois valeurs `3em`, ce qui signifie qu'elle a 3 lignes.

`grid-template-columns` et `grid-template-rows` peuvent également prendre des valeurs comme `repeat`, `autofill`, `autofit`, `minmax`. Nous n'aborderons pas ces valeurs dans cet article.

Ce que vous devez savoir maintenant, c'est que vous pouvez créer une grille explicite avec deux propriétés :

1. `grid-template-columns` : crée des colonnes
2. `grid-template-rows` : crée des lignes

### Positionnement des éléments dans votre grille

Vous pouvez contrôler la position des éléments dans une grille avec deux propriétés.

Ces deux propriétés ne peuvent être utilisées que sur un élément de grille.

`grid-column` vous permet de choisir dans quelle(s) colonne(s) vous voulez placer votre élément de grille. C'est une abréviation pour `grid-column-start` et `grid-column-end`.

Cela fonctionne ainsi : `grid-column-start / grid-columns-end`.

```
/* Utilisation de la forme longue */.grid-item {  grid-column-start: 1;   grid-column-end: 3;}
```

```
/* Utilisation de la forme courte */.grid-item {  grid-column: 1 / 3;}
```

Note : Vous pouvez également utiliser le mot-clé `span` pour indiquer à CSS Grid combien de colonnes vous voulez que votre élément occupe.

```
/* Utilisation de la forme longue */.grid-item {  grid-column-start: 1; /* Commence à la colonne un */  grid-column-end: span 2; /* Largeur de deux colonnes */}
```

Voir le Pen [Propriétés de la grille explicite](https://codepen.io/zellwk/pen/dqQrmm/) par Zell Liew ([@zellwk](https://codepen.io/zellwk)) sur [CodePen](https://codepen.io/).

`grid-row` vous permet de choisir dans quelle(s) ligne(s) vous voulez placer votre élément de grille. C'est une abréviation pour `grid-row-start` et `grid-row-end`.

Cela fonctionne ainsi : `grid-row-start / grid-row-end`.

```
/* Utilisation de la forme longue */.grid-item {  grid-row-start: 1;   grid-row-end: span 2;}
```

```
/* Utilisation de la forme courte */.grid-item {  grid-row: 1 / span 2;}
```

Voir le Pen [Positionnement des éléments (lignes)](https://codepen.io/zellwk/pen/OoaqoG/) par Zell Liew ([@zellwk](https://codepen.io/zellwk)) sur [CodePen](https://codepen.io/).

### Positionnement des éléments dans des zones nommées

Vous pouvez nommer des parties de votre grille si vous n'aimez pas compter les lignes et les colonnes. Ces parties nommées sont appelées zones de grille. Pour créer une zone de grille, vous utilisez `grid-template-area` sur la grille.

Quelques notes sur la création de zones de grille :

1. Vous devez nommer chaque zone de grille
2. Si vous ne voulez pas nommer une zone, utilisez `.`
3. Chaque groupe séparé par des guillemets (`"ligne1" "ligne2"`) signifie une ligne
4. Chaque valeur à l'intérieur des guillemets (`"zone1 zone2"`) signifie une zone

L'exemple ci-dessous a trois zones de grille :

1. `header` sur les deux premières et occupe 4 colonnes
2. `main` sur la deuxième ligne et occupe les 2 colonnes du milieu
3. `footer` sur la troisième ligne et occupe 4 colonnes

```
.grid {  grid-template-areas: "header header header header"                      ".      main   main   .     "                      "footer footer footer footer";}
```

Pour placer des éléments dans une zone de grille, vous utilisez la propriété `grid-area` sur l'élément de grille.

Pour placer des éléments sur une zone de grille, vous utilisez `grid-area`.

```
.grid {  display: grid;   /* ... */}
```

```
main {  grid-area: main}
```

Voir le Pen [Grid-template-area](https://codepen.io/zellwk/pen/PdxLyg/) par Zell Liew ([@zellwk](https://codepen.io/zellwk)) sur [CodePen](https://codepen.io/).

### Comment retenir ces propriétés

Vous avez appris 6 propriétés jusqu'à présent :

1. `grid-template-columns`
2. `grid-template-rows`
3. `grid-template-areas`
4. `grid-column`
5. `grid-row`
6. `grid-area`

Quelques conseils pour retenir ces 6 propriétés :

1. Le mot-clé `template` ne peut être utilisé que sur la grille  
 a) Ils sont utilisés pour déclarer des grilles et des zones nommées  
 b) Les propriétés avec le mot-clé `template` sont au pluriel
2. Les propriétés pour les éléments de grille n'ont pas le mot-clé `template`  
a) Ces propriétés sont au singulier  
b) Ces propriétés affectent le positionnement

### Espaces

Lorsque vous créez une grille, vous pouvez créer des espaces entre les colonnes et les lignes. Ces espaces sont appelés gaps.

Il y a trois propriétés à retenir :

1. `grid-column-gap`
2. `grid-row-gap`
3. `grid-gap`

`grid-column-gap` détermine l'espace entre les colonnes.

`grid-row-gap` détermine l'espace entre les lignes.

`grid-gap` est une abréviation pour `grid-column-gap` et `grid-row-gap`.

Pour cette abréviation :

1. la valeur `column` vient en premier : `column-gap / row-gap`
2. Si vous utilisez un seul nombre, les deux valeurs seront ce nombre.

```
/* Valeurs différentes */.grid {  grid-column-gap: 1em;  grid-row-gap: 2em;}
```

```
.grid {  grid-gap: 1em / 2em; }/* Même valeurs */.grid {  grid-column-gap: 1em;  grid-row-gap: 1em;}
```

```
.grid {  grid-gap: 1em;}
```

Voir le Pen [Explicit Grid with gap](https://codepen.io/zellwk/pen/bxQZZG/) par Zell Liew ([@zellwk](https://codepen.io/zellwk)) sur [CodePen](https://codepen.io/).

### Alignement des éléments

C'est là que beaucoup de gens se perdent.

Il y a six propriétés pour aligner les éléments :

1. `justify-content`
2. `align-content`
3. `justify-items`
4. `align-items`
5. `justify-self`
6. `align-self`

Vous pouvez voir deux groupes de motifs ici :

* Le premier groupe est `justify` vs `align`
* Le second groupe est `content`, `items`, et `self`

Ces deux groupes de propriétés vous indiquent ce que vous traitez. Si vous comprenez le mot-clé de la propriété, vous saurez comment les utiliser.

### Justify vs align

Chaque CSS Grid a deux axes :

1. L'axe principal
2. L'axe transversal

Lorsque vous `justifiez` quelque chose, vous changez l'alignement selon l'_axe principal_. Lorsque vous `alignez` quelque chose, vous changez l'alignement selon l'_axe transversal_.

Voici un moyen facile d'identifier l'axe principal et l'axe transversal :

1. Identifiez la direction de la langue
2. L'axe principal est la façon dont vous lisez la langue
3. L'axe transversal est la façon dont vous lisez après avoir lu la fin de la première ligne.

Prenons l'anglais comme exemple. Comment lisez-vous l'anglais ?

1. De gauche à droite
2. De haut en bas

Donc l'axe principal et l'axe transversal sont :

1. Principal : de gauche à droite
2. Transversal : de haut en bas

Note : les axes principal et transversal changent si vous changez la direction de la langue avec `writing-mode`.

### Content, items, et self

`justify-content` et `align-content` vous permettent d'aligner la grille elle-même à l'espace disponible en dehors de la grille. Vous n'aurez besoin de ces propriétés que si votre grille est plus petite que sa zone définie (ce qui est rare).

```
.grid {  justify-content: /* une valeur */;   align-content: /* une valeur */; }
```

Vous pouvez choisir parmi sept valeurs :

1. **start** : aligne la grille au début de l'axe
2. **end** : aligne la grille à la fin de l'axe
3. **center** : aligne la grille au centre de l'axe
4. **stretch** : la grille remplit l'axe (c'est la valeur par défaut)
5. **space-between** : répartit l'espace blanc entre les éléments de la grille. Pas d'espace blanc aux extrémités
6. **space-around** : répartit l'espace blanc autour de chaque élément de la grille
7. **space-evenly** : répartit l'espace blanc uniformément autour de tous les éléments de la grille, y compris les extrémités

![Image](https://cdn-media-1.freecodecamp.org/images/Bji3J37rICTz6Njcts4IL6ejCB-Z4Usg6DkH)

Les images ci-dessus sont tirées du [Guide complet de Grid](https://css-tricks.com/snippets/css/complete-guide-grid/) de CSS Tricks. Il explique ce que fait chaque valeur en détail. Vous pouvez le lire pour plus d'informations.

Notre objectif ici est de retenir les propriétés et comment les utiliser. Revenons à la prochaine série de propriétés.

`justify-items` et `align-items` vous permettent d'aligner les éléments de la grille à tout espace blanc disponible dans leurs cellules respectives. La plupart du temps, lorsque vous essayez d'aligner des éléments, vous cherchez soit `justify-items`, soit `align-items`.

```
.grid {  justify-items: /* une valeur */;   align-items: /* une valeur */; }
```

Vous pouvez choisir parmi les mêmes quatre valeurs :

1. **start** : aligne l'élément au début de l'axe
2. **end** : aligne l'élément à la fin de l'axe
3. **center** : aligne l'élément au centre de l'axe
4. **stretch** : remplit l'axe (c'est la valeur par défaut)

![Image](https://cdn-media-1.freecodecamp.org/images/QsF6-6HHFmOHMEv4utrE0MZd-xelyg5ueVb6)

`justify-self` et `align-self` font la même chose que `justify-items` et `align-items`. La différence est qu'ils vous permettent de changer l'alignement pour un seul élément de la grille.

```
.grid-item {  justify-self: /* une valeur */;  align-self: /* une valeur */;}
```

### Grille implicite

Disons que vous avez créé une grille CSS, mais que vous n'avez pas assez de lignes. Dans l'exemple ci-dessous, j'ai seulement créé une grille explicite pour trois éléments (3 colonnes, 1 ligne).

```
.grid {  display: grid;   grid-template-columns: 1fr 1fr 1fr;  grid-template-row: 3em;}
```

Mais j'ai six éléments !

```
<!-- Ceci est du HTML -->
```

```
<div class="grid">  <div class="grid-item"></div>  <div class="grid-item"></div>  <div class="grid-item"></div>  <div class="grid-item"></div>  <div class="grid-item"></div>  <div class="grid-item"></div></div>
```

Lorsque vous n'avez pas assez d'espace dans votre grille explicite, CSS Grid vous aidera à créer des grilles supplémentaires automatiquement. Par défaut, il créera plus de lignes.

Si vous voulez changer la direction de la grille, vous définirez `grid-auto-flow` sur `row`.

Ces parties créées automatiquement sont appelées la grille implicite.

Vous pouvez ajuster les colonnes ou lignes créées automatiquement avec ces deux propriétés :

1. `grid-auto-columns`
2. `grid-auto-rows`

```
.grid {  display: grid;   grid-template-columns: 1fr 1fr 1fr;  grid-template-rows: 3em;   grid-auto-rows: 6em;}
```

Voir le Pen [Implicit grid](https://codepen.io/zellwk/pen/yxQrJb/) par Zell Liew ([@zellwk](https://codepen.io/zellwk)) sur [CodePen](https://codepen.io/).

### Comment retenir la grille implicite

`auto` est le mot-clé auquel vous devez faire attention.

1. `template` crée la grille explicite
2. `auto` crée la grille implicite

J'utilise beaucoup la grille implicite. Je partagerai comment j'utilise CSS Grid dans un autre article.

### Conclusion

Cela représente presque toutes les propriétés de CSS Grid que vous devez connaître pour 80 % de vos grilles ! Voici un résumé des propriétés que vous avez apprises :

* Création d'une grille  
a. Explicite :   
 1) `grid-template-columns`   
 2) `grid-template-rows`   
 3) `grid-template-areas`   
b. Implicite :  
 1) `grid-auto-columns`   
 2) `grid-auto-rows`
* Espaces   
 1) `grid-column-gap`  
 2) `grid-row-gap`   
 3) `grid-gap`
* Positionnement des éléments dans une grille  
1) `grid-column`  
2) `grid-row`
* Alignement des éléments  
1) `justify-content`   
2) `align-content`   
3) `justify-items`   
4) `align-items`   
5) `justify-self`   
6) `align-self`

J'espère que cela vous aidera à retenir CSS Grid ! Bonne chance !

Merci d'avoir lu. Cet article vous a-t-il aidé d'une manière ou d'une autre ? Si c'est le cas, [j'espère que vous envisagerez de le partager](http://twitter.com/share?text=Comment%20je%20retiens%20les%20propriétés%20de%20CSS%20Grid%20par%20@zellwk%20?%20&url=https://zellwk.com/blog/remember-css-grid-properties/&hashtags=). Vous pourriez aider quelqu'un. Merci !

Cet article a été initialement publié sur [zellwk.com](https://zellwk.com/blog/remember-css-grid-properties/).  
Inscrivez-vous à ma [newsletter](https://zellwk.com/) si vous voulez plus d'articles pour vous aider à devenir un meilleur développeur frontend.