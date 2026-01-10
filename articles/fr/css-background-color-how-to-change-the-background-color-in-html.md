---
title: Couleur d'arrière-plan CSS – Comment changer la couleur d'arrière-plan en HTML
subtitle: ''
author: Ilenia Magoni
co_authors: []
series: null
date: '2021-08-04T14:46:14.000Z'
originalURL: https://freecodecamp.org/news/css-background-color-how-to-change-the-background-color-in-html
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/html-background-color.png
tags:
- name: colors
  slug: colors
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: Couleur d'arrière-plan CSS – Comment changer la couleur d'arrière-plan
  en HTML
seo_desc: 'You have started creating your HTML page, and you want to give it some
  color – maybe change the color of the text or set a nice background. So how do you
  do that?

  In this article I''ll show you how you can change the background color of a page
  in a fe...'
---

Vous avez commencé à créer votre page HTML, et vous souhaitez lui donner un peu de couleur – peut-être changer la couleur du texte ou définir un bel arrière-plan. Alors comment faire ?

Dans cet article, je vais vous montrer comment vous pouvez changer la couleur d'arrière-plan d'une page de plusieurs manières différentes.

# Comment changer la couleur d'arrière-plan d'un élément HTML

Vous pouvez changer la couleur d'arrière-plan d'un élément HTML en utilisant la propriété CSS `background-color` et en lui donnant une valeur de couleur.

```css
p {
  background-color: pink;
}
```

Par exemple, ce code donnera à tous les éléments de paragraphe de votre fichier HTML un arrière-plan rose car la propriété `background-color` a une valeur de `pink`.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/image-16.png)

Il existe environ 140 noms de couleurs que vous pouvez utiliser, comme `teal`, `hotpink`, `indigo` et bien d'autres.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/image-23.png)
_Quelques-uns des noms de couleurs possibles que vous pouvez utiliser_

Remarque : si vous donnez une couleur d'arrière-plan à un élément et que vous ne voyez pas de changement, cela peut être une erreur de syntaxe, ou cela peut aussi être dû au fait que l'élément n'a pas de largeur ou de hauteur. Essayez d'y mettre du contenu, ou donnez-lui une largeur et une hauteur en utilisant les propriétés CSS `width` et `height`.

Il existe en réalité près de 16,8 millions de couleurs que vous pouvez utiliser. Vous pouvez utiliser toutes ces couleurs en utilisant les valeurs RVB. Il existe également des couleurs TSL où vous avez environ 3,7 millions de couleurs parmi lesquelles choisir. Dans la section suivante, vous apprendrez toutes ces différentes façons de créer des couleurs.

# Différentes notations de couleurs

La propriété `background-color` accepte les couleurs comme valeurs possibles. Ici, vous verrez quatre notations différentes pour les valeurs de couleur.

La première sera les noms de couleurs, et il existe environ 140 mots-clés que vous pouvez utiliser. C'est le moyen le plus simple de choisir une couleur car il ne nécessite pas de comprendre des notations spéciales – mais il offre un choix limité.

Les deuxième et troisième façons de nommer ou de choisir des couleurs sont les valeurs RVB et les valeurs hexadécimales. Dans ces notations, les couleurs sont identifiées par la quantité de rouge, de vert et de bleu qu'elles contiennent.

Cela vient de la manière dont un écran produit de la couleur. Un écran est composé de pixels, et chaque pixel est éclairé par des LED de trois couleurs différentes, vert, bleu et rouge, qui peuvent briller à différentes intensités.

La quatrième notation est les couleurs TSL, ou Teinte-Saturation-Lumière. Cette notation vient du design graphique, car elle reflète une manière plus naturelle pour les humains de penser à la couleur : une couleur pure (teinte), dont la saturation et la lumière peuvent être variées.

Vous pouvez utiliser l'une de ces notations de couleurs pour donner une couleur à l'arrière-plan, mais examinons-les plus en détail, afin que vous puissiez choisir celle que vous préférez.

## Noms de couleurs HTML

Il existe 16 couleurs de base reconnues dans la première version de HTML. Maintenant, il y a plus de 140 couleurs nommées que vous pouvez utiliser.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/image-24.png)
_Les 16 couleurs de base_

```css
body {
  background-color: black;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2021/08/image-17.png)
_Un exemple de page HTML avec le `body` ayant une `background-color` de `black`_

Vous pouvez voir toutes les couleurs nommées dans l'annexe à la fin de l'article.

## Couleurs RVB

RVB signifie Rouge-Vert-Bleu. Les couleurs dans ce format sont écrites `rgb(0,0,0)`, où chaque valeur est un nombre entre `0` et `255` représentant la quantité de rouge, de vert et de bleu utilisée pour créer chaque couleur, respectivement.

Par exemple, si vous avez `rgb(0,0,0)` vous obtenez du noir.

Pour obtenir du rouge, vous écrivez `rgb(255,0,0)`, où il y a autant de rouge que possible avec `255`, `0` pour le bleu, et `0` pour le vert.

Vous pouvez obtenir d'autres variations de rouge avec de petites quantités de vert et/ou de bleu, et un peu moins de rouge. Par exemple, vous pouvez obtenir un rouge orangé avec `rgb(255,69,0)` ou un rouge foncé avec `rgb(139,0,0)`.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/image-25.png)
_Les couleurs des valeurs RVB présentées ci-dessus._

```css
div {
  background-color: rgb(139,0,0);
}
```

![Image](https://www.freecodecamp.org/news/content/images/2021/08/image-18.png)
_Un exemple de page HTML avec l'élément `div` ayant une `background-color` de `rgb(139,0,0)`_

Ci-dessous un exemple de la manière dont la couleur change lorsque vous ajustez deux des valeurs RVB : le coin supérieur gauche du carré coloré est égal à `rgb(0,0,0)`, le coin supérieur droit est égal à `rgb(0,0,255)`, le coin inférieur gauche à `rgb(0,255,0)` et le coin inférieur droit à `rgb(0,255,255)`.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/image-28.png)

Heureusement, vous n'avez pas besoin de deviner les nombres pour obtenir la couleur que vous voulez. Vous pouvez trouver divers sélecteurs de couleurs en ligne qui vous permettent de choisir la couleur avec des curseurs (ou d'autres méthodes) et de vous donner la valeur de couleur RVB que vous souhaitez utiliser.

## Couleurs hexadécimales

Les couleurs hexadécimales sont une autre façon d'écrire les couleurs RVB. Avec les hexadécimaux, vous avez également trois nombres, un pour chaque couleur, avec 256 valeurs possibles.

Dans ce cas, cependant, chaque couleur a deux chiffres qui vont de `0` à `F` (c'est-à-dire, `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, et `A`, `B`, `C`, `D`, `E`, `F`). Un seul chiffre a 16 valeurs possibles, et deux chiffres ont 256 valeurs possibles, de `00` à `FF` (255).

Les couleurs hexadécimales sont écrites avec un `#` devant la valeur. Le rouge est écrit comme `#FF0000`, le rouge foncé comme `#8B0000`, et le rouge orangé comme `#FF4500`, par exemple.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/image-2.png)
_Les couleurs mentionnées dans la section ci-dessus._

```
h1 {
  background-color: #FF4500;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2021/08/image-19.png)
_Un exemple de page HTML avec l'élément `h1` ayant une `background-color` de `#FF4500`_

Vous pouvez également utiliser des sélecteurs de couleurs pour générer des valeurs hexadécimales.

### Raccourci hexadécimal

Vous pouvez écrire les nombres hexadécimaux sous forme abrégée, en utilisant seulement trois chiffres au lieu de six. Par exemple, vous pouvez écrire le rouge comme `#F00`. Cela réduit le nombre de couleurs possibles à un peu plus de 4 000, mais c'est plus court à écrire, et parfois c'est ce qui est important.

Chaque chiffre est à la place de deux chiffres identiques, donc nous ne pouvons pas écrire `#8B0000` sous forme abrégée, car `8` et `B` ne sont pas identiques. Mais nous pouvons écrire `#800` qui est égal à `#880000`, assez similaire à l'autre rouge foncé. Et le rouge orangé peut être `#F40` (égal à `#FF4400`).

![Image](https://www.freecodecamp.org/news/content/images/2021/08/image-8.png)
_Les couleurs mentionnées dans la section ci-dessus._

## Couleurs TSL

TSL signifie Teinte-Saturation-Lumière, et c'est une façon complètement différente d'écrire les couleurs par rapport à ce que nous avons vu jusqu'à présent.

Les couleurs TSL sont représentées par trois nombres : la teinte va de `0` à `360`, et la saturation et la lumière de `0` à `100`.

La teinte détermine la couleur de base, et sa valeur est un angle, un degré sur la roue chromatique. Dans ce cas, le rouge est `0`, le vert est `120`, le bleu est `240`, et `360` est à nouveau le rouge.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/image-11.png)
_Toutes les couleurs possibles en changeant seulement la teinte, avec une teinte de 0 à gauche et une teinte de 360 à droite._

La saturation va de `0`, ce qui rend la couleur grise, à `100`, qui montre la couleur complète.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/image-9.png)
_Variation de la saturation pour le rouge, 0% à gauche, 100% à droite._

La lumière est la quantité de noir ou de blanc ajoutée à la couleur. `0` est noir, `50` est la couleur elle-même, et `100` est blanc.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/image-10.png)
_Variation de la lumière, avec 0% à gauche, et 100% à droite._

Par exemple, vous écrirez le rouge comme `hsl(0,100%,50%)`, le rouge orangé comme `hsl(16,100%,50%)`, et le rouge foncé comme `hsl(0,100%,27%)`.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/image-26.png)

Il peut être plus facile de trouver des couleurs similaires en utilisant TSL qu'avec les autres schémas de couleurs. Avec le rouge et ses variations, vous avez vu que pour obtenir un rouge plus foncé, vous pouvez simplement changer le pourcentage de lumière, et mélanger le rouge avec une autre couleur suffit à changer un peu sa valeur de teinte.

Voyons cela en action avec une couleur mixte en hexadécimal, comme l'orange (`#FFA500` ou `rgb(255,166,0)`), écrite en TSL comme `hsl(39,100%,50%)`. Vous pouvez obtenir un orange plus clair simplement en augmentant la lumière.

Par exemple, vous pouvez écrire `hsl(39,100%,65%)` pour obtenir cet orange plus clair. Avec les autres notations, vous auriez dû écrire `rgb(255,193,77)` ou `#FFC14D`.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/image-27.png)

![Image](https://www.freecodecamp.org/news/content/images/2021/08/image-20.png)
_Un exemple de page HTML avec l'élément `main` ayant une `background-color` de `hsl(39, 100%, 65%)`_

Vous pouvez également trouver des sélecteurs de couleurs en ligne pour les couleurs TSL.

# Raccourci du nom de la propriété

Vous pouvez également définir la couleur d'arrière-plan en utilisant la propriété raccourcie `background`.

```css
p {
  background: pink;
}

body {
  background: black;
}

div {
  background: rgb(139,0,0);
}

h1 {
  background: #FF4500;
}

main {
  background: hsl(39,100%,65%);
}
```

![Image](https://www.freecodecamp.org/news/content/images/2021/08/image-21.png)
_Un exemple de page HTML avec tous les éléments ayant une couleur d'arrière-plan._

Il s'agit d'une propriété plus polyvalente, [car elle est un raccourci pour diverses propriétés `background`](https://www.freecodecamp.org/news/learn-css-background-properties/), comme `background-image` et `background-position`. Lorsque vous l'utilisez avec une valeur de couleur, elle fonctionne exactement de la même manière que `background-color`.

# Conclusion

Vous avez appris comment donner une couleur d'arrière-plan à vos éléments HTML en utilisant la propriété `background-color` et son raccourci `background`, et en utilisant différentes notations de couleurs.

Maintenant, vous avez tous les outils nécessaires pour ajouter les couleurs que vous souhaitez à vos pages web. Amusez-vous bien !

# Annexe

## Toutes les 140+ couleurs nommées

![Image](https://www.freecodecamp.org/news/content/images/2021/08/CodePen-colored-squares-2.png)

## Variations d'orthographe

Les noms de couleurs contenant le mot "Gray" peuvent également s'écrire avec l'orthographe "Grey" comme montré ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/image-22.png)