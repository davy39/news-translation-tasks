---
title: Introduction à la mise en page CSS Grid (avec des exemples)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-26T16:15:21.000Z'
originalURL: https://freecodecamp.org/news/intro-to-css-grid-layout
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/1_4O4lprdERnQvKFbdbZPIig-1.jpeg
tags:
- name: CSS Grid
  slug: css-grid
seo_title: Introduction à la mise en page CSS Grid (avec des exemples)
seo_desc: "By Zafar Saleem\nCSS Grid has taken over the world of web design. It’s\
  \ really cool. There are plenty of tutorials, blogs and articles on the internet,\
  \ which are great sources of knowledge. \nBut the majority of them teach you the\
  \ basics with very few r..."
---

Par Zafar Saleem

CSS Grid a conquis le monde du design web. C'est vraiment génial. Il existe de nombreux tutoriels, blogs et articles sur Internet, qui sont d'excellentes sources de connaissances. 

Mais la majorité d'entre eux vous enseignent les bases avec très peu d'exemples concrets. Donc dans ce guide, nous allons examiner des exemples tout en apprenant.

## Qu'est-ce que Grid ?

CSS Grid nous permet de créer de meilleures mises en page en utilisant la capacité intégrée au navigateur des grilles. Avant CSS Grid, nous devions soit utiliser notre propre système de grille personnalisé, soit quelque chose comme Bootstrap. 

Ces autres options fonctionnent bien, mais CSS Grid élimine la plupart des problèmes que nous rencontrions avec ces solutions.

CSS Grid rend le développement de mises en page simples et complexes aussi facile que bonjour. Dans ce blog, nous allons apprendre quelques terminologies de base, puis passer à un exemple de mise en page simple.

## Terminologies de base

Les termes de base associés à CSS Grid sont les suivants :

1. Colonnes
2. Lignes
3. Cellules
4. Lignes de grille
5. Gouttière

![Image](https://www.freecodecamp.org/news/content/images/2020/06/1_B80r8wi2JB9HIrCIYJggxg.png)

Tous les termes sont expliqués dans le diagramme ci-dessus. Cet exemple est une grille de 3x2 colonnes, ce qui signifie 3 colonnes et 2 lignes.

## Exemple de mise en page

Maintenant que les concepts de base sont éclaircis, nous allons utiliser ces concepts pour créer une mise en page d'exemple comme celle ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/1_4VirrlRLYMrFWwmp852N3A.png)

Comme vous pouvez le voir, il y a un en-tête et un pied de page. Ensuite, la ligne centrale comporte 3 colonnes avec la navigation dans la première colonne, la barre latérale à droite et la zone de contenu principale au centre (qui occupe la majeure partie de la ligne).

Voici le HTML de cet exemple.

```html
<div class="wrapper">
  <header class="items">EN-TÊTE</header>
  <nav class="items">NAVIGATION</nav>
  <div class="items contents">CONTENU</div>
  <aside class="items">BARRE LATÉRALE</aside>
  <footer class="items">PIED DE PAGE</footer>
</div>
```

Maintenant que le HTML est prêt, plongeons dans le CSS. Tout d'abord, donnons-lui un peu de style pour que notre HTML ressemble à ce qui est montré ci-dessus. Ces règles CSS ne font pas partie de CSS Grid, donc vous pouvez les omettre si vous le souhaitez.

```css
.wrapper * {
  background: orange;
  display: flex;
  justify-content: center;
  align-items: center;
  margin-bottom: 1px;
  margin-right: 1px;
}
```

Comme vous pouvez le voir, je style tous les éléments à l'intérieur d'un conteneur wrapper. Je définis sa couleur de fond sur `orange` et je donne des `margins` `bottom` et `right`. Je définis `display` `flex` juste pour aligner les éléments au centre en définissant `justify-content` et `align-items` sur `center`.

Ensuite, passons à la partie CSS Grid.

```css
.wrapper {
  display: grid;
  grid-template-columns: 1fr 5fr 2fr;
  grid-template-rows: 5fr 20fr 5fr;
  grid-gap: 10px;
  height: 720px;
}
```

Dans le code ci-dessus, nous définissons `display` sur `grid` – d'où le titre de ce sujet. C'est ainsi que nous convertissons un conteneur en `grid`. 

Ensuite, nous définissons les colonnes et les lignes. Nous allons le faire en utilisant les propriétés `grid-template-columns` et `grid-template-rows`. `grid-template-columns` nous permet de définir le nombre de colonnes avec leur `width` appropriée. `grid-template-rows` nous permet de définir le nombre de `rows` avec leur `height` appropriée. 

Dans l'exemple ci-dessus, il y a 3 colonnes avec la première colonne prenant `1 fraction`, la deuxième colonne prenant `5 fractions` et la troisième colonne `2 fractions`. Une seule unité de fraction signifie _"une partie de combien de parties nous divisons cela"_.

Si vous regardez le même exemple ci-dessus, le même concept s'applique aux `rows`. Il y a trois lignes, et la première ligne contient l'`en-tête` qui prend toute la ligne à travers les trois colonnes. La deuxième ligne prend la navigation, le contenu et la barre latérale, tandis que le pied de page va à la troisième et dernière ligne et prend les trois colonnes.

Cela signifie que la première et la dernière ligne prennent la même quantité de hauteur, soit `5 fractions`. Et la ligne centrale prend le reste de la hauteur restante.

Ensuite, nous allons également créer une gouttière de 10px. Nous pouvons le faire dans CSS Grid en utilisant la propriété `grid-gap`. Enfin, nous définissons une hauteur pour notre conteneur wrapper.

Si nous regardons dans le navigateur, nous obtiendrons le résultat que nous recherchons :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/1_YpRMEUzHN96jqnQf8AVEow.png)

Maintenant, faisons en sorte que cela ressemble davantage à ce que nous voulons en définissant quelques propriétés pour l'en-tête et le pied de page. Nous allons dire à l'en-tête et au pied de page de prendre toute leur ligne.

Nous allons le faire en utilisant les propriétés `grid-column-start` et `grid-column-end`, comme ceci :

```css
header {
  grid-column-start: 1;
  grid-column-end: 4;
}

footer {
  grid-column-start: 1;
  grid-column-end: 4;
}
```

Comme vous pouvez le voir, l'en-tête et le pied de page commencent tous deux à la `ligne de grille` 1 et se terminent à la `ligne de grille` 4. Cela leur permet de prendre toute leur ligne. Cela donnera exactement le résultat que nous recherchons, comme ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/1_4VirrlRLYMrFWwmp852N3A--1-.png)

## Code complet

```html
<!DOCTYPE html>
<html>
<head>
	<title>CSS Grid</title>
	<style type="text/css">
		.wrapper {
			display: grid;
			grid-template-columns: 1fr 5fr 2fr;
			grid-template-rows: 5fr 20fr 5fr;
			grid-gap: 10px;
			height: 720px;
		}

		header {
			grid-column-start: 1;
			grid-column-end: 4;
		}

		footer {
			grid-column-start: 1;
			grid-column-end: 4;
		}

		.wrapper * {
			background: orange;
			display: flex;
			justify-content: center;
			align-items: center;
			margin-bottom: 1px;
			margin-right: 1px;
		}
	</style>
</head>
<body>
	<div class="wrapper">
		<header class="items">EN-TÊTE</header>
		<nav class="items">NAVIGATION</nav>
		<div class="items contents">CONTENU</div>
		<aside class="items">BARRE LATÉRALE</aside>
		<footer class="items">PIED DE PAGE</footer>
	</div>
</body>
</html>
```

C'est tout pour cet article. Vous pouvez me suivre [ici](https://www.freecodecamp.org/news/author/zafar/) pour plus d'articles. Si vous l'avez aimé, n'oubliez pas de le partager sur les réseaux sociaux.