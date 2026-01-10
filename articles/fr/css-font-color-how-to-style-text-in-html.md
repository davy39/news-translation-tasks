---
title: Couleur de police CSS – Comment styliser du texte en HTML
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2021-09-01T17:27:17.000Z'
originalURL: https://freecodecamp.org/news/css-font-color-how-to-style-text-in-html
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/Cssfontcolor.png
tags:
- name: colors
  slug: colors
- name: CSS
  slug: css
- name: fonts
  slug: fonts
- name: HTML
  slug: html
seo_title: Couleur de police CSS – Comment styliser du texte en HTML
seo_desc: 'Setting text color on a website you''re building might be confusing at
  first. But in this article, you''ll learn how to do it.

  How to Set Text Color in HTML

  In CSS, the background-color property is pretty straightforward for setting the
  background colo...'
---

Définir la couleur du texte sur un site web que vous construisez peut sembler confus au début. Mais dans cet article, vous apprendrez comment le faire.

## Comment définir la couleur du texte en HTML

En CSS, la propriété `background-color` est assez simple pour définir la couleur de fond de n'importe quoi. 

Alors, que faire si vous souhaitez définir la couleur de premier plan de quelque chose sur la page ? Surtout pour le texte, que vous ne voudriez pas, dans des conditions normales, définir une couleur de fond.

Il n'existe pas de propriété `foreground-color` en CSS, donc ce qui rend cela possible est la propriété `color`.

Dans cet article, je vais vous expliquer comment définir la couleur du texte en utilisant la propriété color. Nous examinerons également les différentes façons dont elle prend des valeurs.

La propriété color prend des valeurs de 4 manières différentes : couleur nommée, couleur hexadécimale, couleur RGB et couleur HSL. Examinons chacune d'entre elles maintenant.

## Couleurs nommées

Comme le nom l'indique, vous utilisez la propriété color et appliquez la valeur en nommant la couleur que vous souhaitez. Cela peut être rouge, vert, bleu, orange, cramoisi, cyan, ou toute autre couleur nommée. Il existe environ 147 couleurs nommées reconnues par les navigateurs. 

La syntaxe de base ressemble à ceci :

```css 
élement {
    color: colorName
}
```

```html
<p>freeCodeCamp</p>
```

```css
 p {
     color: crimson;
}
```

![named-color](https://www.freecodecamp.org/news/content/images/2021/09/named-color.png)

## Couleurs hexadécimales (ou simplement couleurs Hex)

Les valeurs hexadécimales sont utilisées pour représenter des couleurs avec un total de 6 caractères. Elles commencent par le signe livre/nombre (#), puis n'importe quel nombre de 0 à 9, et enfin n'importe quelle lettre de A à F.

Les deux premières valeurs représentent le rouge, les deux suivantes représentent le vert, et les deux dernières représentent le bleu. Avec les valeurs hexadécimales, il n'y a pas de limite aux nuances de couleurs que vous pouvez utiliser.

```html
<p>freeCodeCamp</p>
```

```css
 p {
    color: #dc143c;
 }
```

## Couleurs RGB

RGB signifie rouge, vert et bleu. Avec les couleurs RGB, vous spécifiez la couleur en termes de quantité de rouge, de vert et de bleu que vous souhaitez. Les trois sont exprimés avec des nombres entre 0 et 255.

Il existe un type de RGB appelé `rgba`. Le a supplémentaire signifie alpha, ce qui vous permet de spécifier l'opacité de la couleur. Il prend une valeur de 0.0 à 1.0 – 0.0 signifie 0% d'opacité, 0.5 signifie 50% d'opacité, et 1.0 signifie 100% d'opacité.

La syntaxe de base est `rgba(amountOfRed, amountOfGreen, amountOfBlue, alpha)`. 

Vous pouvez la limiter à `rgba(amountOfRed, amountOfGreen, amountOfBlue)` si vous ne souhaitez pas de valeur alpha.

Voici la syntaxe pour les valeurs RGB régulières :

```html
<p>freeCodeCamp</p>
```

```css
 p {
   color: rgb(220, 20, 60);
 }
```

![rgb-color](https://www.freecodecamp.org/news/content/images/2021/09/rgb-color.png)

Et voici une démonstration de la valeur alpha en action avec 50% (0.5) d'opacité :

```css
p {
    color: rgb(219, 20, 60, 0.5);
}
```

![rgb-fifty-percent-opacity](https://www.freecodecamp.org/news/content/images/2021/09/rgb-fifty-percent-opacity.png)

## Couleurs HSL

HSL signifie teinte, saturation et luminosité. C'est une autre façon de spécifier la couleur pour le texte (et tout autre élément qui prend une couleur) en CSS. 

- La teinte représente la roue chromatique en 360°. Donc, 0° est rouge, 120° est vert et 240° est bleu. 
- La saturation est la quantité de gris dans la couleur, exprimée en pourcentage. 0% est la nuance de gris et 100% est la couleur elle-même.
- La luminosité est la quantité de noirceur et de luminosité dans la couleur exprimée en pourcentage. 0% est noir et 100% est blanc.

Tout comme les couleurs RGB, vous pouvez également définir l'opacité de la couleur. Donc, il y a aussi hsla.

La syntaxe de base complète est `hsl(colorDegree, saturationPercentage, lightnessPercentage, alpha)`. Vous pouvez la limiter à `hsl(colorDegree, saturationPercentage, lightnessPercentage)` si vous ne souhaitez pas de valeur alpha.

```html
<p>freeCodeCamp</p>
```

```css
 p {
   color: hsl(348, 83%, 47%);
 }
```

![hsl-color](https://www.freecodecamp.org/news/content/images/2021/09/hsl-color.png)

Vous pouvez appliquer une opacité particulière à la couleur hsl comme ceci :

```css
 p {
   color: hsla(348, 83%, 47%, 0.5);
  }
```

![hsl-fifty-percent-opacity-1](https://www.freecodecamp.org/news/content/images/2021/09/hsl-fifty-percent-opacity-1.png)

## Doit-on utiliser des couleurs nommées, des couleurs hexadécimales, des couleurs RGB ou des couleurs HSL pour attribuer des couleurs ?

L'une des choses merveilleuses à propos de CSS est qu'il existe plusieurs façons de faire la même chose. Vous l'avez vu en appliquant des couleurs au texte. 

Puisque vous pouvez appliquer des couleurs de 4 manières différentes, vous devez vous demander laquelle est la meilleure à utiliser.

Lorsque vous utilisez des couleurs nommées, vous êtes quelque peu limité dans la mesure où vous pouvez appliquer différentes nuances de couleurs. Le rouge, le vert, le bleu, le jaune, ou toute autre couleur nommée a de nombreuses variations auxquelles vous n'aurez pas accès avec les couleurs nommées. Vous n'aurez accès qu'à environ 147 couleurs prédéfinies reconnues par les navigateurs.

Les couleurs hexadécimales sont très dynamiques. Elles sont les plus couramment utilisées parmi les développeurs parce que votre limite est votre créativité. Avec les couleurs hexadécimales, vous pouvez utiliser diverses nuances et même utiliser une couleur que personne n'a jamais utilisée.

Les couleurs RGB sont aussi dynamiques que les couleurs hexadécimales. En plus de pouvoir spécifier combien de rouge, de vert et de bleu vous voulez de 0 à 255, vous pouvez également définir à quel point vous voulez que la couleur soit transparente avec la valeur alpha supplémentaire.

HSL est le plus dynamique de tous. Vous pouvez spécifier la couleur exacte que vous voulez en degrés de 0 à 360 dans la roue chromatique, définir à quel point vous voulez qu'elle soit saturée et sombre en pourcentages, et également définir une opacité de 0.0 à 1.0.

Donc, vraiment, cela dépend de vous et de votre cas d'utilisation – et de votre niveau de créativité ou de spécificité.

## Conclusion

Appliquer des couleurs au texte aide à rendre votre site web plus attrayant pour les visiteurs. La bonne combinaison de couleurs peut également aider votre contenu à devenir plus lisible.

Dans cet article, vous avez appris comment appliquer des couleurs au texte avec les 4 différents types de valeurs que vous pouvez utiliser avec la propriété color.

Merci d'avoir lu, et continuez à coder.