---
title: Comment rendre votre HTML réactif en ajoutant une seule ligne de CSS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-08T05:37:03.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-your-html-responsive-by-adding-a-single-line-of-css-2a62de81e431
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Bx0gNW69lAXaSRqRw0_8dw.jpeg
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Comment rendre votre HTML réactif en ajoutant une seule ligne de CSS
seo_desc: 'By Per Harald Borgen

  In this article, I’ll teach you how to use CSS Grid to create a super cool image
  grid which varies the number of columns with the width of the screen.

  And the most beautiful part: the responsiveness will be added with a single li...'
---

Par Per Harald Borgen

Dans cet article, je vais vous apprendre à utiliser CSS Grid pour créer une grille d'images super cool qui varie le nombre de colonnes en fonction de la largeur de l'écran.

Et la partie la plus belle : **la réactivité sera ajoutée avec une seule ligne de CSS.**

Cela signifie que nous n'avons pas à encombrer le HTML avec des noms de classes laids (c'est-à-dire `col-sm-4`, `col-md-8`) ou créer des requêtes média pour chaque taille d'écran.

Si vous souhaitez apprendre à construire des sites web réactifs de manière professionnelle, vous pouvez envisager de consulter le [bootcamp de design web réactif de Scrimba](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gresponsive_single_line_responsive), car il emmène les étudiants du niveau débutant à avancé à travers 15 heures de tutoriels interactifs.

Maintenant, plongeons-nous dans le sujet !

### L'installation

Pour cet article, nous allons continuer avec la grille que nous avons utilisée dans [mon premier article sur CSS Grid](https://medium.freecodecamp.org/learn-css-grid-in-5-minutes-f582e87b1228). Ensuite, nous ajouterons les images à la fin de l'article. Voici à quoi ressemble notre grille initiale :

![Image](https://cdn-media-1.freecodecamp.org/images/1*fJNIdDiScjhI9CZjdxv3Eg.png)

Voici le HTML :

```html
<div class="container">  
  <div>1</div>  
  <div>2</div>  
  <div>3</div>  
  <div>4</div>  
  <div>5</div>  
  <div>6</div>  
</div>

```

Et le CSS :

```css
.container {  
    display: grid;  
    grid-template-columns: 100px 100px 100px;  
    grid-template-rows: 50px 50px;  
}

```

Note : l'exemple contient également un peu de style de base, que je ne vais pas aborder ici, car cela n'a rien à voir avec CSS Grid.

Si ce code vous confond, je vous recommande de lire mon article [Apprendre CSS Grid en 5 minutes](https://medium.freecodecamp.org/learn-css-grid-in-5-minutes-f582e87b1228), où j'explique les bases du module de mise en page.

Commençons par rendre les colonnes réactives.

### Réactivité de base avec l'unité de fraction

CSS Grid apporte avec lui une toute nouvelle valeur appelée unité de fraction. L'unité de fraction s'écrit comme `fr`, et elle vous permet de diviser le conteneur en autant de fractions que vous le souhaitez.

Changeons chaque colonne pour qu'elle ait une largeur d'une unité de fraction.

```css
.container {  
    display: grid;  
    grid-template-columns: 1fr 1fr 1fr;  
    grid-template-rows: 50px 50px;  
}

```

Ce qui se passe ici, c'est que la grille divise toute la largeur en trois fractions et que chaque colonne occupe une unité. Voici le résultat :

![Image](https://cdn-media-1.freecodecamp.org/images/1*JgGPqT2AfFNDD8DhG2wPdQ.gif)

Si nous changeons la valeur de `grid-template-columns` en `1fr 2fr 1fr`, la deuxième colonne sera maintenant deux fois plus large que les deux autres colonnes. La largeur totale est maintenant de quatre unités de fraction, et la deuxième colonne en occupe deux, tandis que les autres en occupent une chacune. Voici à quoi cela ressemble :

![Image](https://cdn-media-1.freecodecamp.org/images/1*cpfokc1HBgCwOTNhRU9SHg.gif)

En d'autres termes, la valeur de l'unité de fraction rend super facile le changement de la largeur des colonnes.

### Réactivité avancée

Cependant, l'exemple ci-dessus ne nous donne pas la réactivité que nous voulons, car cette grille sera toujours large de trois colonnes. Nous voulons que notre grille varie le nombre de colonnes en fonction de la largeur du conteneur. Pour y parvenir, vous devrez apprendre trois nouveaux concepts.

#### repeat()

Nous allons commencer par la fonction `repeat()`. Il s'agit d'une manière plus puissante de spécifier vos colonnes et vos lignes. Prenons notre grille originale et changeons-la pour utiliser repeat() :

```css
.container {  
    display: grid;  
    grid-template-columns: repeat(3, 100px);  
    grid-template-rows: repeat(2, 50px);  
}

```

En d'autres termes, `repeat(3, 100px)` est identique à `100px 100px 100px`. Le premier paramètre spécifie le nombre de colonnes ou de lignes que vous souhaitez, et le second spécifie leur largeur, donc cela nous donnera simplement la même mise en page exacte que celle avec laquelle nous avons commencé :

![Image](https://cdn-media-1.freecodecamp.org/images/1*fJNIdDiScjhI9CZjdxv3Eg.png)

#### auto-fit

Ensuite, il y a auto-fit. Sautons le fait d'avoir un nombre fixe de colonnes, et remplaçons plutôt 3 par `auto-fit`.

```css
.container {  
    display: grid;  
    grid-gap: 5px;  
    grid-template-columns: repeat(auto-fit, 100px);
    grid-template-rows: repeat(2, 100px);  
}

```

Cela donne le comportement suivant :

![Image](https://cdn-media-1.freecodecamp.org/images/1*vLZ9RD3dt0Q3hCieYfRuMg.gif)

La grille varie maintenant le nombre de colonnes en fonction de la largeur du conteneur.

Elle essaie simplement de faire tenir autant de colonnes de 100px de large que possible dans le conteneur.

Cependant, si nous codons en dur toutes les colonnes pour qu'elles soient exactement de 100px, nous n'obtiendrons jamais la flexibilité que nous voulons, car elles s'additionneront rarement à la largeur totale. Comme vous pouvez le voir sur le gif ci-dessus, la grille laisse souvent un espace blanc sur le côté droit.

#### minmax()

Le dernier ingrédient dont nous avons besoin pour corriger cela s'appelle `minmax()`. Nous allons simplement remplacer 100px par `minmax(100px, 1fr)`. Voici le CSS final.

```css
.container {  
    display: grid;  
    grid-gap: 5px;  
    grid-template-columns: repeat(auto-fit, minmax(100px, 1fr));
    grid-template-rows: repeat(2, 100px);  
}

```

Remarquez que toute la réactivité se produit en une seule ligne de CSS.

Cela donne le comportement suivant :

![Image](https://cdn-media-1.freecodecamp.org/images/1*1FOrkyNbaabo3_LJxcdDbg.gif)

Et comme vous pouvez le voir, cela fonctionne parfaitement. La fonction `minmax()` définit une plage de taille supérieure ou égale à **min** et inférieure ou égale à max.

Ainsi, les colonnes auront toujours au moins 100px de large. Cependant, s'il y a plus d'espace disponible, la grille le distribuera simplement de manière égale à chacune des colonnes, car les colonnes se transforment en une unité de fraction au lieu de 100 px.

#### Ajout des images

Maintenant, la dernière étape consiste à ajouter les images. Cela n'a rien à voir avec CSS Grid, mais regardons tout de même le code.

Nous allons commencer par ajouter une balise image à l'intérieur de chacun des éléments de la grille.

```html
<div>
    <img src="img/forest.jpg"/>
</div>

```

Pour que l'image s'adapte à l'élément, nous allons la définir pour qu'elle soit aussi large et haute que l'élément lui-même, puis utiliser `object-fit: cover;`. Cela fera en sorte que l'image couvre tout son conteneur, et le navigateur la rognera si nécessaire.

```css
.container > div > img {  
    width: 100%;  
    height: 100%;  
    object-fit: cover;  
}

```

Ce qui se termine comme suit :

![Image](https://cdn-media-1.freecodecamp.org/images/1*jCNANupl0ECRzF6cOLuWNw.gif)

Et c'est tout ! Vous connaissez maintenant l'un des concepts les plus complexes de CSS Grid, alors félicitez-vous.

#### Support des navigateurs

Avant de terminer, je dois également mentionner le support des navigateurs. Au moment de la rédaction de cet article, [93 % du trafic mondial des sites web supporte CSS Grid](https://caniuse.com/#feat=css-grid), et ce chiffre est en augmentation. Il devient de plus en plus clair que Grid devient une compétence incontournable pour les développeurs front-end. Un peu comme ce qui s'est passé avec CSS Flexbox il y a quelques années.

Si vous souhaitez apprendre Flexbox, Grid et le design réactif une fois pour toutes, vous devriez consulter le [bootcamp de design web réactif sur Scrimba](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gresponsive_single_line_responsive). Il vous emmènera du niveau débutant à avancé à travers des tutoriels interactifs faciles à suivre.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/bootcamp-banner.png)
_[Cliquez ici pour accéder au bootcamp avancé.](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=gresponsive_single_line_responsive)_

---

Merci d'avoir lu ! Je m'appelle Per Borgen, je suis le co-fondateur de Scrimba, une plateforme d'apprentissage interactive pour apprendre à coder.