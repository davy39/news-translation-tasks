---
title: Comment centrer du texte verticalement avec CSS
subtitle: ''
author: Joe Attardi
co_authors: []
series: null
date: '2023-10-23T19:44:32.000Z'
originalURL: https://freecodecamp.org/news/how-to-center-text-vertically-with-css
coverImage: https://www.freecodecamp.org/news/content/images/2023/10/pexels-alexander-ermakov-12154194.jpg
tags:
- name: CSS
  slug: css
- name: CSS Grid
  slug: css-grid
- name: flexbox
  slug: flexbox
- name: Web Development
  slug: web-development
seo_title: Comment centrer du texte verticalement avec CSS
seo_desc: 'If you have some text inside a div, and nothing else, the div''s height
  will match the text height. Suppose, though, you have some text and an image. Your
  text will be aligned at the bottom of the div, which is usually not what you want.

  In this artic...'
---

Si vous avez du texte à l'intérieur d'une `div`, et rien d'autre, la hauteur de la `div` correspondra à la hauteur du texte. Supposons, cependant, que vous ayez du texte et une image. Votre texte sera aligné en bas de la `div`, ce qui n'est généralement pas ce que vous voulez.

Dans cet article, vous apprendrez quelques façons de centrer verticalement votre texte à l'intérieur d'une telle `div` ou d'un autre élément.

## Comment centrer du texte en utilisant la hauteur de ligne

Cette approche est limitée, mais peut être utile si vous avez défini votre élément à une hauteur fixe en utilisant la propriété `height`.

La propriété `line-height` détermine la hauteur de la boîte dans laquelle le navigateur rend le texte. Par défaut, celle-ci est définie à une valeur légèrement supérieure à 1 pour fournir un espacement confortable entre les lignes de texte.

Si vous définissez la `height` et la `line-height` de l'élément à la même valeur, le texte sera centré verticalement :

```css
.my-element {
  height: 3rem;
  line-height: 3rem;
}

```

![Image](https://www.freecodecamp.org/news/content/images/2023/10/image-91.png)
_Texte centré verticalement en utilisant line-height_

Il y a cependant une mise en garde importante à cette approche. Cela ne fonctionne que si votre texte peut tenir sur une seule ligne.

Si le texte se retourne à la ligne, vous verrez la première ligne centrée verticalement. Parce que vous avez défini la `line-height` pour qu'elle soit la même que la `height` de l'élément, la ligne de texte retournée déborde maintenant de l'élément.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/image-94.png)
_Texte retourné débordant du conteneur_

Si cela semble trop rigide, continuez à lire. Ensuite, vous verrez comment utiliser Flexbox pour centrer verticalement votre texte, ainsi que tout autre contenu à l'intérieur de l'élément.

## Comment centrer du texte en utilisant Flexbox

Une meilleure solution, plus polyvalente, consiste à utiliser une mise en page Flexbox avec `align-items` défini sur `center`.

Un élément utilisant Flexbox (le conteneur flex) dispose les éléments (éléments flex) soit en ligne soit en colonne. Une mise en page Flexbox a deux lignes imaginaires qui la traversent. La première est l'axe _principal_, le long duquel les éléments seront placés. Pour une flexbox en `row`, l'axe principal est l'axe horizontal.

L'axe _transversal_ est perpendiculaire à l'axe principal. Vous pouvez utiliser l'axe transversal pour définir l'alignement vertical des éléments à l'intérieur du conteneur flex.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/image-92.png)
_L'axe principal et l'axe transversal dans une mise en page Flexbox horizontale_

Voici le CSS dont vous aurez besoin pour appliquer une mise en page Flexbox et centrer verticalement le texte :

```css
.my-element {
	/* Utiliser une mise en page flexbox */
	display: flex;
	
	/* Créer une flexbox horizontale (par défaut) */
	flex-direction: row;
	
	/* La partie importante : centrer verticalement les éléments */
	align-items: center;
}

```

Cela crée une mise en page Flexbox horizontale (le `flex-direction: row` n'est pas strictement nécessaire, car c'est la valeur par défaut). La propriété `align-items` détermine l'alignement des éléments le long de l'axe transversal, ou vertical. Il existe plusieurs valeurs que vous pouvez utiliser, mais ici vous pouvez utiliser `center` pour centrer verticalement le texte.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/image-96.png)
_Le texte avec align-items: center_

Cela fonctionne bien, et cela gère même plusieurs lignes de texte retourné. Si vous avez d'autres contenus à l'intérieur de l'élément, comme une image, tout sera aligné verticalement.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/image-95.png)
_Le texte est aligné verticalement avec d'autres contenus_

## Comment centrer du texte en utilisant CSS Grid

Vous pouvez également centrer votre contenu verticalement en utilisant CSS Grid.

Pour une seule `div` contenant le texte à centrer, vous pouvez la transformer en une mise en page de grille avec une ligne et une colonne.

```css
.my-element {
	display: grid;
	align-items: center;
}
```

Dans une mise en page de grille, la propriété `align-items` spécifie l'alignement du contenu dans la cellule, le long de l'axe des colonnes (vertical). Cela aligne verticalement votre texte dans l'élément `div`.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/image-98.png)
_Texte centré verticalement en utilisant une mise en page de grille 1x1_

Si l'élément contenant votre texte fait déjà partie d'une mise en page de grille, vous pouvez soit appliquer `align-items: center` à l'ensemble de la grille, soit si vous souhaitez simplement contrôler l'alignement vertical de cette cellule de grille, vous pouvez utiliser `align-self: center`.

## Conclusion

Maintenant, vous savez comment centrer verticalement du texte. La prochaine fois que vous verrez un tweet sur le centrage d'une `div`, vous pourrez répondre avec vos nouvelles connaissances en CSS !