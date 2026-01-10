---
title: Apprendre les bases de Flexbox en seulement 10 minutes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-05-25T06:43:21.000Z'
originalURL: https://freecodecamp.org/news/flexbox-in-10-minutes-7295497804ed
coverImage: https://cdn-media-1.freecodecamp.org/images/1*8fC9bK5XBVtAlNEHlrtfsQ.jpeg
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: technology
  slug: technology
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: Apprendre les bases de Flexbox en seulement 10 minutes
seo_desc: 'By Justin Yek

  What is Flexbox?

  Flexbox, short for “flexible box,” is a layout mode introduced in CSS3 that determines
  how elements are arranged on a page so that they behave predictably under different
  screen sizes and devices.

  It is called Flexbox b...'
---

Par Justin Yek

### Qu'est-ce que Flexbox ?

[Flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS3), abréviation de « flexible box », est un mode de mise en page introduit dans [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS3) qui détermine comment les éléments sont disposés sur une page afin qu'ils se comportent de manière prévisible sous différentes tailles d'écran et appareils.

Il est appelé Flexbox en raison de sa capacité à étendre et réduire les éléments à l'intérieur de la boîte flexible pour remplir au mieux l'espace disponible. Comparé aux anciennes méthodes de mise en page telles que l'affichage en tableau et les blocs en ligne flottants, Flexbox est un moyen plus puissant de :

* Disposer les éléments dans différentes directions
* Réorganiser l'ordre d'affichage des éléments
* Changer l'alignement des éléments
* Adapter dynamiquement les éléments au conteneur

### Quand ne pas utiliser Flexbox ?

Bien que Flexbox soit excellent pour la mise à l'échelle, l'alignement et la réorganisation des éléments, essayez d'éviter de l'utiliser pour :

* [la mise en page globale de la page](https://jakearchibald.com/2014/dont-use-flexbox-for-page-layout/)
* les sites web qui prennent entièrement en charge les anciens navigateurs

![Image](https://cdn-media-1.freecodecamp.org/images/sgdvNGmWdodCeaBHUy1oUmWYnRyvrF0oL5oN)
_Support des navigateurs pour Flexbox de [Can I Use…](http://caniuse.com/#search=flex" rel="noopener" target="_blank" title=")_

Les anciens navigateurs, comme IE 11 ou versions antérieures, ne prennent pas en charge ou ne prennent que partiellement en charge Flexbox. Si vous souhaitez jouer la sécurité, vous devriez revenir à d'autres méthodes de mise en page CSS, telles que `display: inline-block` avec `float` et `display: table`.

Cependant, si vous ne ciblez que les navigateurs modernes, Flexbox vaut définitivement le coup d'œil.

### Terminologie

![Image](https://cdn-media-1.freecodecamp.org/images/cn2fNZwwOcXbjDk6bUcGdTYcoqrL6XDJMbhc)

Dans le modèle Flexbox, il y a trois concepts principaux :

* les éléments flexibles, les éléments qui doivent être disposés
* le conteneur flexible, qui contient les éléments flexibles
* la direction du flux, qui détermine la direction de la mise en page des éléments flexibles

Les humains apprennent mieux par l'expérience et les exemples, alors commençons !

### Niveau 1 — Basique

1) Créer un conteneur flexible

```
<div class="flex-container">    <div class="flex-item"></div>  <div class="flex-item"></div></div>
```

```
.flex-container {  display: flex;}
```

Pour créer un conteneur flexible, vous devez simplement ajouter la propriété `display: flex` à un élément. Par défaut, tous les enfants directs sont considérés comme des éléments flexibles et sont disposés horizontalement en une seule ligne de gauche à droite. Si la largeur totale des éléments flexibles est plus grande que le conteneur, les éléments seront réduits pour qu'ils s'adaptent au conteneur.

2) Placer les éléments flexibles dans une seule colonne

```
.flex-container {  display: flex;  flex-direction: column;}
```

Les éléments flexibles peuvent être disposés verticalement en définissant `flex-direction: column`. Il est également possible de les disposer dans l'ordre inverse en définissant `flex-direction: column-reverse` ou `flex-direction: row-reverse`.

```
.flex-container {  display: flex;  flex-direction: column-reverse;}
```

### Niveau 2 — Débutant

1) Aligner les éléments flexibles à droite

```
.flex-container {  display: flex;  justify-content: flex-end;}
```

Rappelons qu'il y a une direction de flex pour chaque modèle Flexbox. `justify-content` est utilisé pour spécifier où les éléments flexibles doivent être placés le long de la direction de flex. Dans l'exemple ci-dessus, `justify-content: flex-end` signifie que les éléments sont justifiés à la fin du conteneur flexible dans la direction horizontale. C'est pourquoi ils sont placés à droite.

2) Centrer les éléments flexibles

```
.flex-container {  display: flex;  justify-content: center;}
```

3) Étaler les éléments flexibles

Vous pouvez spécifier combien d'espace doit apparaître entre les éléments dans un conteneur en utilisant l'une des trois valeurs d'espacement possibles pour la propriété `justify-content` :

* `space-evenly` : l'espace entre le bord de départ du conteneur et le premier élément est égal à l'espacement entre chaque élément et l'élément adjacent.
* `space-between` : l'espace entre deux éléments adjacents est le même, mais pas nécessairement égal à l'espace entre le premier/dernier élément et son bord le plus proche ; l'espace entre le bord de départ et le premier élément est égal à l'espace entre le bord de fin et le dernier élément.
* `space-around` : l'espace de chaque côté d'un élément est le même pour chaque élément dans le conteneur. Notez que cela signifie que l'espace entre deux éléments adjacents sera deux fois plus grand que l'espace entre le premier/dernier élément et son bord le plus proche.

4) Aligner les éléments flexibles dans une seconde direction

```
.flex-container {  display: flex;  justify-content: center;  align-items: center;}
```

Habituellement, nous aimerions disposer les éléments le long de la direction de flex tout en alignant également les éléments dans la direction perpendiculaire à celle-ci. En définissant `justify-content: center` et `align-items: center`, les éléments flexibles peuvent être placés au centre du conteneur flexible à la fois horizontalement et verticalement.

5) Aligner un élément flexible particulier

```
.flex-container {  display: flex;  align-items: center;}
```

```
.flex-bottom {  align-self: flex-end;}
```

Il est possible d'aligner un élément flexible particulier différemment des autres dans le conteneur en utilisant la propriété CSS `align-self` sur cet élément.

### Niveau 3 — Intermédiaire

1) Permettre aux éléments flexibles de s'enrouler dans d'autres lignes/colonnes

```
.flex-container {  display: flex;  flex-wrap: wrap;}
```

Par défaut, les éléments flexibles ne sont pas autorisés à s'enrouler et ils sont redimensionnés pour s'adapter à une seule ligne ou colonne si le conteneur flexible n'est pas assez grand pour tous les contenir. En ajoutant `flex-wrap: wrap`, les éléments flexibles qui dépasseraient du conteneur seront enveloppés dans une autre ligne.

2) Enveloppement inversé

```
.flex-container {  display: flex;  flex-wrap: wrap-reverse;}
```

Les éléments flexibles sont toujours disposés en plusieurs lignes `flex-wrap: wrap-reverse` mais ils commencent à partir de la fin du conteneur flexible.

3) Justifier la position des lignes d'éléments

```
.flex-container {  display: flex;  flex-wrap: wrap;  align-content: flex-start;}
```

Par défaut, les lignes d'éléments flexibles qui s'enroulent sont étirées pour occuper tout l'espace restant avec un espacement égal entre les lignes adjacentes. Vous pouvez définir `align-content` sur le conteneur flexible pour déterminer le positionnement des lignes lorsque l'enveloppement se produit. Les valeurs possibles sont `flex-start`, `flex-end`, `center`, `space-between`, `space-around` et `stretch` (par défaut).

### Niveau 4 — Avancé

1) Étendre les éléments

```
.flex-container {  display: flex;}
```

```
.flex-item:nth-of-type(1){  flex-grow: 1;}
```

```
.flex-item:nth-of-type(2) {  flex-grow: 2;}
```

`flex-grow` prend effet uniquement lorsqu'il y a de l'espace restant dans le conteneur flexible. La propriété `flex-grow` d'un élément flexible spécifie combien un élément s'étendra par rapport aux autres éléments afin de remplir la boîte flexible. La valeur par défaut est 1. Lorsqu'elle est définie à 0, l'élément ne s'étendra pas pour remplir l'espace restant. Dans cet exemple, le rapport des deux éléments est de 1:2, ce qui signifie que le premier élément occupera ⅓, tandis que le second élément occupera ⅔ de l'espace restant.

2) Réduire les éléments

```
.flex-container {  display: flex;}
```

```
.flex-item:nth-of-type(1) {  flex-shrink: 1;}
```

```
.flex-item:nth-of-type(2) {  flex-shrink: 2;}
```

`flex-shrink` ne prend effet que lorsque les éléments flexibles débordent du conteneur flexible en raison d'un espace insuffisant. Il spécifie combien un élément se réduira par rapport aux autres éléments afin que les éléments ne débordent pas de la boîte flexible. La valeur par défaut est 1. Lorsqu'elle est définie à 0, l'élément flexible ne se réduira pas du tout. Dans cet exemple, le rapport est de 1:2, ce qui signifie que le premier élément se réduira de ⅓, tandis que le second élément se réduira de ⅔ de l'espace débordé.

3) Définir la taille des éléments

```
.flex-container {  display: flex;}
```

```
.flex-item:nth-of-type(1) {  flex-basis: 200px;}
```

```
.flex-item:nth-of-type(2) {  flex-basis: 10%;}
```

Au lieu d'utiliser la taille initiale d'un élément, vous pouvez personnaliser sa taille avec `flex-basis`. Par défaut, sa valeur est `flex-basis: auto`, ce qui signifie que la taille est calculée à partir des règles CSS non-Flexbox. Vous pouvez également la définir à une valeur absolue ou à une valeur qui représente un pourcentage du conteneur flexible ; par exemple `flex-basis: 200px` et `flex-basis: 10%`.

4) Mettre ensemble flex-grow, flex-shrink et flex-basis

```
.flex-container {  display: flex;}
```

```
.flex-item:nth-of-type(1) {  flex: 1 0 100px;}
```

```
.flex-item:nth-of-type(2) {  flex: 2 0 10%;}
```

`flex` est une abréviation pour `flex-grow`, `flex-shrink` et `flex-basis`. Dans cet exemple, le premier élément flexible est défini pour être `flex-grow=1`, `flex-shrink=0`, `flex-basis=100px` et le second élément flexible est défini pour être `flex-grow=2`, `flex-shrink=0`, `flex-basis=10%`. Dans ce cas, puisque qu'il y a de l'espace restant dans le conteneur flexible, seul `flex-grow` prend effet et `flex-shrink` est ignoré.

### Conclusion

Flexbox est facile à apprendre et à manipuler. La connaissance de son utilisation est particulièrement utile puisque le cycle de développement web est court et les itérations sont rapides. Si vous souhaitez expérimenter davantage avec Flexbox avant de l'utiliser dans vos projets, vous pouvez visiter [Flexyboxes](http://the-echoplex.net/flexyboxes/) et [Flexbox Froggy](http://flexboxfroggy.com/) pour vous entraîner. Vous pouvez également lire plus sur [CSS trick: A guide to Flexbox](https://css-tricks.com/snippets/css/a-guide-to-flexbox/) et [W3C: CSS Flexible Box](https://drafts.csswg.org/css-flexbox/).

_Cet article a été initialement publié sur le [blog](http://altitudelabs.com/blog/) d'Altitude Labs et a été écrit par notre ingénieur logiciel, Felix Yau. [Altitude Labs](http://altitudelabs.com) est une agence logicielle spécialisée dans les applications React personnalisées et mobiles-first._