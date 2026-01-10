---
title: Couleur d'arrière-plan Div – Comment changer la couleur d'arrière-plan en CSS
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-02-03T16:50:46.000Z'
originalURL: https://freecodecamp.org/news/div-background-color-how-to-change-background-color-in-css
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/backgroundcolor.png
tags:
- name: colors
  slug: colors
- name: CSS
  slug: css
- name: HTML
  slug: html
seo_title: Couleur d'arrière-plan Div – Comment changer la couleur d'arrière-plan
  en CSS
seo_desc: "If you're working on a web development project, setting a nice background\
  \ color can give the website a more enticing look. \nTo set a background color for\
  \ a div or related element in CSS, you use the background-color property.\nWhile\
  \ setting this backg..."
---

Si vous travaillez sur un projet de développement web, définir une belle couleur d'arrière-plan peut donner au site web un aspect plus attrayant. 

Pour définir une couleur d'arrière-plan pour un `div` ou un élément similaire en CSS, vous utilisez la propriété `background-color`.

Lors de la définition de cette couleur d'arrière-plan, votre créativité est votre seule limite quant à la distance que vous souhaitez parcourir. 

Alors dans cet article, je vais vous montrer comment vous pouvez définir cette couleur d'arrière-plan.

## Comment définir la couleur d'arrière-plan avec des couleurs nommées

Avec les couleurs nommées, vous pouvez définir la couleur d'arrière-plan en utilisant la propriété `background-color` et en lui attribuant une valeur exprimée en nom de couleur comme `red`, `green`, `blue`, etc.

```css
 div {
      background: green;
    }
```
![ss-1-1](https://www.freecodecamp.org/news/content/images/2022/02/ss-1-1.png)

Vous pouvez utiliser les styles suivants pour améliorer l'apparence de la page web. Il suffit de définir une largeur et une hauteur pour le `div`, afin que la couleur d'arrière-plan puisse prendre effet :

```css
body {
   display: flex;
   align-items: center;
   justify-content: center;
   height: 100vh;
   background-color: #d3d3d3;
 }

div {
   background: green;
 }
```

Les navigateurs modernes reconnaissent environ 147 couleurs, donc vous êtes encore un peu limité. 

## Comment définir la couleur d'arrière-plan avec des couleurs hexadécimales

Avec les valeurs hexadécimales, vous pouvez définir une couleur d'arrière-plan pour un `div` ou tout autre élément avec un total de 6 caractères. 

Les couleurs hexadécimales commencent par le signe dièse (#), suivi de n'importe quel chiffre de 0 à 9, et enfin de n'importe quelle lettre de A à F.

Les deux premières valeurs représentent le rouge, les deux suivantes représentent le vert, et les deux dernières représentent le bleu. 

Avec les valeurs hexadécimales, vous pouvez explorer en profondeur la roue chromatique et même utiliser des couleurs que personne n'a jamais utilisées.

```css
div {
   background: #2ecc71;
 }
```
![ss-2-1](https://www.freecodecamp.org/news/content/images/2022/02/ss-2-1.png)

Vous pouvez [en savoir plus sur les couleurs hexadécimales ici](https://www.freecodecamp.org/news/how-hex-code-colors-work-how-to-choose-colors-without-a-color-picker/).

## Comment définir la couleur d'arrière-plan avec des couleurs RVB

RVB signifie Rouge, Vert et Bleu. 

Pour définir la couleur d'arrière-plan avec le RVB, vous spécifiez la quantité de rouge, de vert et de bleu que vous souhaitez avec des nombres compris entre 0 et 255.
```css
div {
      background: rgb(220, 20, 60);
    }
```
![ss-3](https://www.freecodecamp.org/news/content/images/2022/02/ss-3.png)

Le RVB a également une variation appelée RGBA. Le dernier A signifie alpha et il vous permet de déterminer à quel point vous souhaitez que la couleur soit opaque.

L'alpha prend une valeur de 0.0 à 1.0. 0.0 signifie 0 % d'opacité, 0.5 signifie 50 % d'opacité, et 1.0 signifie 100 % d'opacité.

```css
div {
    background: rgb(220, 20, 60, 0.6);
 }
 ```
![ss-4](https://www.freecodecamp.org/news/content/images/2022/02/ss-4.png)

Vous pouvez [en savoir plus sur les couleurs RVB ici](https://www.freecodecamp.org/news/rgb-color-html-and-css-guide/).

## Comment définir la couleur d'arrière-plan avec des couleurs TSL

TSL signifie Teinte, Saturation et Luminosité. C'est la méthode la plus dynamique parmi les façons de spécifier une couleur d'arrière-plan pour un `div` ou d'autres éléments.  

- **Teinte** représente la roue chromatique en 360°. 0° est le rouge, 120° est le vert et 240° est le bleu
- **Saturation** est la quantité de gris dans la couleur exprimée en pourcentages. 0 % est la nuance de gris et 100 % est la couleur elle-même.
- Comme son nom l'indique, la **luminosité** est la quantité de noirceur et de luminosité dans la couleur exprimée en pourcentage. 0 % est le noir et 100 % est le blanc.
```css
div {
   background: hsl(16, 100%, 50%);
 }
```
![ss-5](https://www.freecodecamp.org/news/content/images/2022/02/ss-5.png)

## Conclusion
Puisque vous pouvez appliquer des couleurs de 4 manières différentes, vous devez vous demander laquelle vous devriez utiliser. 

Lorsque vous utilisez des couleurs nommées, vous êtes un peu limité dans la mesure où vous pouvez appliquer différentes nuances de couleurs. 

Chaque couleur comme le rouge, le vert, le bleu, le jaune ou toute autre couleur a de nombreuses variations auxquelles vous n'aurez pas accès avec les couleurs nommées. 

Vous ne pouvez accéder qu'à environ 147 couleurs prédéfinies reconnues par les navigateurs.
Les couleurs hexadécimales, en revanche, sont très dynamiques. Elles sont principalement utilisées parmi les développeurs, et la créativité est la seule limite. Ces couleurs hexadécimales vous permettent d'utiliser différentes nuances de la même couleur.

Les couleurs RVB sont aussi dynamiques que les couleurs hexadécimales. Vous pouvez spécifier la quantité de rouge, de vert et de bleu de 0 à 255, et vous pouvez également utiliser la valeur alpha ajoutée pour spécifier la transparence de la couleur.

Le TSL est le plus dynamique de tous. Vous pouvez spécifier exactement la couleur de 0 à 360 degrés dans la roue chromatique, définir la saturation et l'obscurité en pourcentage, et définir l'opacité à n'importe quelle valeur entre 0.0 et 1.0.  

Donc, décider laquelle utiliser entre les couleurs nommées, hexadécimales, RVB et TSL dépend de vous, de votre créativité et des besoins de votre projet.

Merci d'avoir lu.