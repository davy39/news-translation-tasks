---
title: Les meilleurs exemples CSS et CSS3
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-18T17:46:00.000Z'
originalURL: https://freecodecamp.org/news/css-example-css3
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9f3c740569d1a4ca4181.jpg
tags:
- name: CSS
  slug: css
- name: CSS3
  slug: css3
seo_title: Les meilleurs exemples CSS et CSS3
seo_desc: 'CSS provides the style of a website.

  The background property lets you use images and colors to create backgrounds for
  your web pages.

  Background Color Example

  The background color property allows you to choose the color of your element. This
  can be t...'
---

CSS fournit le style d'un site web.

La propriété background vous permet d'utiliser des images et des couleurs pour créer des arrière-plans pour vos pages web.

### **Exemple de couleur d'arrière-plan**

La propriété de couleur d'arrière-plan vous permet de choisir la couleur de votre élément. Cela peut être l'arrière-plan pour toute la page ou l'arrière-plan d'une section de votre page.

* Un élément est un morceau de HTML tel qu'un en-tête ou un paragraphe sur une page web.

Voici un exemple de définition de la couleur d'arrière-plan pour une page web en vert.

```css
  body {
    background-color: green;
  }
```

![Image](https://www.freecodecamp.org/news/content/images/2020/03/green-bg-100-1.png)

Voici un exemple de définition des couleurs pour deux éléments. Cela définira l'arrière-plan de l'en-tête en violet et le reste de la page en bleu.

```css
  body {
    background-color: blue;
  }
  h1 {
    background-color: purple;
  }
```

![Image](https://www.freecodecamp.org/news/content/images/2020/03/31036152-0607936a-a539-11e7-9e9f-a5e60ade042d.png)

En CSS, la couleur peut être définie de trois manières :

* Un nom de couleur valide tel que `blue`
* Une valeur HEX telle que `#FFFFF` (C'est la valeur hexadécimale pour le blanc.)
* Une valeur RGB telle que `rgb(76,175,80)` (C'est la valeur RGB pour le vert clair.)

### **Images d'arrière-plan**

Vous pouvez utiliser la propriété background-image pour définir une image comme arrière-plan pour un élément. L'image est répétée par défaut afin qu'elle couvre tout l'élément.

```css
body {
  background-image: url("barn.jpg");
}
```

![Image](https://www.freecodecamp.org/news/content/images/2020/03/31036366-eb1fc260-a539-11e7-835d-e3f935a22c86.png)

Vous pouvez également lier des images ou des gifs que vous trouvez en ligne en utilisant leur lien (par exemple, à partir d'une recherche Google Images).

```css
body {
  background-image: url("https://mdn.mozillademos.org/files/11983/starsolid.gif");
}
```

### **Image d'arrière-plan - La propriété Repeat**



L'image d'arrière-plan est répétée à la fois verticalement (haut et bas) et horizontalement (à travers la page web) par défaut. Vous pouvez utiliser la propriété background-repeat pour répéter l'image verticalement ou horizontalement.

Voici un exemple qui répète l'image verticalement :

```css
body {
  background-image: url("barn.jpg");
  background-repeat: repeat-y;
}

```

![Image](https://www.freecodecamp.org/news/content/images/2020/03/31039770-8962c7a6-a54e-11e7-9d25-4fb09760d219.png)

Vous pouvez répéter l'image horizontalement en définissant la propriété background-repeat sur "repeat-x".

```css
body {
  background-image: url("barn.jpg");
  background-repeat: repeat-x;
}
```

Vous pouvez également utiliser la propriété background-repeat pour définir une image à ne pas répéter.

```css
body {
  background-image: url("barn.jpg");
  background-repeat: no-repeat;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2020/03/31039801-c8761efc-a54e-11e7-8bb9-ec5b88885a50.png)

### **Image d'arrière-plan – La propriété Position**

Vous pouvez utiliser la propriété position pour spécifier où votre image sera située sur une page web.

```css
body {
  background-image: url("barn.jpg");
  background-repeat: no-repeat;
  background-position: right top;
}

```

![Image](https://www.freecodecamp.org/news/content/images/2020/03/31039828-077d1038-a54f-11e7-8aa6-092253ca92b8.png)

### **Image d'arrière-plan – La position fixe**

Vous pouvez utiliser la propriété background-attachment pour définir une image à une position fixe. Une position fixe fait en sorte qu'une image ne fait pas défiler avec le reste de la page.

```css
body {
  background-image: url("barn.jpg");
  background-repeat: no-repeat;
  background-position: right top;
  background-attachment: fixed;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2020/03/31039859-39612c92-a54f-11e7-93ca-9d7bcb938225.png)

### **Dégradés d'arrière-plan**

Un dégradé est une transition entre deux couleurs ou plus et peut être utilisé via CSS de manière similaire à une image d'arrière-plan.

La syntaxe d'un arrière-plan dégradé peut être assez complexe et est souvent encore utilisée avec des préfixes de fournisseurs en raison des incohérences entre les navigateurs pris en charge.

L'[Éditeur de dégradés Colorzilla](http://www.colorzilla.com/gradient-editor/) est un excellent outil en ligne pour générer des dégradés personnalisés et le balisage CSS associé.

### **Arrière-plan – La propriété raccourcie**

Vous pouvez écrire les propriétés d'arrière-plan sur une seule ligne. Cela s'appelle la propriété raccourcie.

```css
body {
  background: url("barn.jpg") no-repeat right top;
}
```

Vous pouvez omettre les propriétés dont vous n'avez pas besoin lorsque vous utilisez la propriété raccourcie, mais les propriétés doivent être utilisées dans un certain ordre. L'ordre est :

* couleur
* image
* répétition
* attachement
* position

### **Images d'arrière-plan multiples**

Vous pouvez spécifier plusieurs images d'arrière-plan dans une seule propriété d'arrière-plan.

```css
body {
  background: url("barn.jpg"), url("stars.jpg"), linear-gradient(rgba(0, 0, 255, 0.5), rgba(255, 255, 0, 0.5));
}
```

La première image (ou dégradé) spécifiée est la plus haute, la seconde vient ensuite, et ainsi de suite. Si l'un des éléments n'est pas correct en raison de son URL ou de sa syntaxe, toute la ligne sera ignorée par le navigateur.

### **Quelques propriétés de base de l'arrière-plan en CSS**

Les propriétés de l'arrière-plan CSS sont utilisées pour définir les effets d'arrière-plan pour les éléments.

Propriétés de l'arrière-plan CSS : background-color, background-image, background-repeat, background-attachment, background-position

## Exemple de point d'arrêt CSS

Un point d'arrêt CSS est un point spécifique où la mise en page d'un site web change, basé sur une requête média (Media Query) devenant active.

Généralement, vous spécifiez un point d'arrêt lorsque vous souhaitez réadapter la mise en page du site web à la taille de la fenêtre du navigateur ; principalement, à la largeur de la fenêtre.

Par exemple, si le contenu de votre site web semble parfait sur une fenêtre étroite (comme sur un navigateur de smartphone), mais qu'il commence à mal paraître sur des écrans plus grands (par exemple, peut-être que la taille des polices est trop petite et difficile à lire), alors vous pourriez vouloir introduire un nouveau point d'arrêt pour les écrans plus grands qui rend les polices plus grandes :

Les points d'arrêt CSS peuvent être considérés comme le cœur du design web réactif, car ils définissent comment le contenu se comporte ou est disposé à différentes largeurs/échelles de périphérique. Cela vous permet de montrer la meilleure mise en page possible à l'utilisateur.

![Exemple](https://getflywheel.com/wp-content/uploads/2018/02/css-breakpoints-layouts-01.jpg)

## **Définir des points d'arrêt**

Les points d'arrêt sont généralement définis sur la base de l'une des options suivantes :

* Points d'arrêt basés sur la largeur du périphérique
* Points d'arrêt basés sur le contenu

### **Points d'arrêt basés sur la largeur du périphérique**

Il est assez évident que tous nos périphériques n'ont pas les mêmes largeurs/tailles d'écran. Il s'agit maintenant d'une décision de conception d'inclure un ensemble de périphériques particuliers et de coder les règles CSS en conséquence. 

Nous avons déjà suffisamment de périphériques à considérer, et lorsqu'un nouveau sort avec une largeur différente, revenir à votre CSS et ajouter un nouveau point d'arrêt partout est chronophage.

Voici un exemple :

```text
/* ----------- iPhone 6, 6S, 7 et 8 ----------- */

/* Portrait */

@media only screen

and (min-device-width: 375px)

and (max-device-width: 667px)

and (-webkit-min-device-pixel-ratio: 2)

and (orientation: portrait) {

}

/* Paysage */

@media only screen

and (min-device-width: 375px)

and (max-device-width: 667px)

and (-webkit-min-device-pixel-ratio: 2)

and (orientation: landscape) {

}

/* ----------- Google Pixel ----------- */

/* Portrait */

@media screen

and (device-width: 360px)

and (device-height: 640px)

and (-webkit-device-pixel-ratio: 3)

and (orientation: portrait) {

}

/* Paysage */

@media screen

and (device-width: 360px)

and (device-height: 640px)

and (-webkit-device-pixel-ratio: 3)

and (orientation: landscape) {

}
```

Avec cette approche, vous finirez par avoir une longue liste de requêtes média.

### **Points d'arrêt basés sur le contenu**

C'est le choix préféré lors de la création ou de l'écriture des règles de points d'arrêt. Parce qu'il est plus facile d'ajuster votre contenu selon une mise en page particulière uniquement lorsqu'il nécessite un changement.

```text
@media only screen (min-width: 768px){
...
}
```

Ce point d'arrêt signifie que le CSS s'appliquera lorsque la largeur du périphérique est de 768px et plus.

#### **Vous pouvez également définir une plage avec des points d'arrêt, de sorte que le CSS ne s'appliquera qu'à l'intérieur de ces limites.**

```text
@media only screen and (min-width: 768px) and (max-width: 959px){

...

}
```

**Note** Essayez toujours de créer des points d'arrêt basés sur votre propre contenu, pas sur les périphériques. Divisez-les en une largeur logique plutôt qu'en une largeur aléatoire et gardez-les en nombre gérable, afin que la modification reste simple et claire.

**Les points d'arrêt CSS** sont utiles lorsque vous souhaitez mettre à jour les styles en fonction de la taille de l'écran. Par exemple, à partir d'un périphérique mesurant 1200px de largeur et plus, utilisez `font-size: 20px;`, sinon utilisez `font-size: 16px;`.

Ce avec quoi nous avons commencé est à partir de périphériques supérieurs à 1200px, une largeur courante d'écran de portable. Vous avez peut-être également remarqué que nous avons mentionné 'supérieur à', ce qui signifie que nous utilisons en quelque sorte une instruction 'si-alors'.

Transformons cela en code CSS :

```css
.text1 {
    font-size: 16px;
}
@media (min-width: 1200px) {
    .text1 {
        font-size: 20px;
    }
}
```

**Pour notre commodité**, nous écrivons d'abord le style de base `.text1`... puis nous spécifions les règles `@media`.

**Astuce** : vous pouvez voir dans un Framework CSS courant appelé 'Bootstrap' qu'ils ont adopté 'min-width' et plus dans leur Bootstrap v4.0, par rapport à leur ancien Bootstrap v3.0 utilisant 'max-width' et moins. Ce n'est qu'une **préférence**, et il n'y a rien de mal à dire 'cette taille et moins' versus 'cette taille et plus'.

Il est parfaitement acceptable d'utiliser `@media (max-width) {}` . Voici un exemple :

```css
.text1 {
    font-size: 20px;
}
@media (max-width: 1199px) {
    font-size: 16px;
}
```

```css
// Styles normaux, de base
// qui ont fiere allure sur les petits écrans
// mais pas sur les écrans plus grands
body {
  font-size: 16px;
}

// Définir un nouveau point d'arrêt, avec une requête média.
// Dans ce cas, lorsque la largeur de la fenêtre est
// d'au moins 512px de large.
@media (min-width: 512px) {
	body {
		font-size: 20px;
	}
}
```

Les points d'arrêt basés sur le contenu plutôt que sur le périphérique sont moins compliqués. Voici un extrait simple qui se déclenche lorsque la largeur du périphérique est supérieure à `code 700px`, environ la taille d'un écran de smartphone

```css
@media only screen and (min-width: 700px) {
  something {
    something: something;
  }
}
```

Vous pouvez également définir une largeur minimale et maximale, ce qui vous permet d'expérimenter avec différentes plages. Cela se déclenche environ entre les tailles de smartphone et les tailles de bureau et de moniteur plus grandes :

```code
@media only screen and (min-width: 700px) and (max-width: 1500px) {
  something {
    something: something;
  }
}
```

## Exemple de couleur CSS

### Couleurs

CSS Colors est un module CSS qui traite des couleurs, des types de couleurs, du mélange de couleurs et de l'opacité. Toutes les propriétés CSS qui prennent une valeur ne font pas partie de ce module, mais elles en dépendent. 

En CSS, vous pouvez changer la couleur de presque n'importe quel élément dans votre page HTML. Des propriétés comme `background-color`, `color`, et `border-color` définissent la couleur de ces éléments.

CSS prend en charge les noms de couleurs, les valeurs hexadécimales et les couleurs RVB. En plus de l'introduction de la déclaration `opacity`, les couleurs en CSS3 peuvent maintenant être spécifiées en utilisant des noms de couleurs, ou des valeurs RVB, HEX, HSL, RGBA, HSLA.

HTML prend en charge 140 noms de couleurs standard [color names](https://www.w3schools.com/colors/colors_names.asp).

### **RGB(A)**

RGB signifie "Rouge, Vert, Bleu". Une valeur RGB est une combinaison de valeurs d'intensité pour le rouge, le vert et le bleu. Chacune est comprise entre 0 (noir) et 255 (intensité maximale). Les valeurs de couleur RGBA sont une extension des valeurs de couleur RGB avec un canal alpha - qui spécifie l'opacité pour une couleur. Le paramètre alpha est un nombre entre 0.0 (totalement transparent) et 1.0 (totalement opaque).

Une valeur de couleur RGB est spécifiée avec : rgb(rouge, vert, bleu). Une valeur de couleur RGBA est similaire, avec la valeur alpha en dernière position : rgba(rouge, vert, bleu, alpha).

### **HSL(A)**

HSL signifie "Teinte, Saturation et Luminosité". La teinte est un degré sur la roue chromatique (de 0 à 360) : 0 (ou 360) est rouge, 120 est vert, 240 est bleu. La saturation est une valeur en pourcentage : 100% est la couleur pleine. La luminosité est également un pourcentage ; 0% est sombre (noir) et 100% est blanc. 

Les valeurs de couleur HSLA sont une extension des valeurs de couleur HSL avec un canal alpha - qui spécifie l'opacité pour une couleur.

Une valeur de couleur HSL est spécifiée avec : hsl(teinte, saturation, luminosité). Une valeur de couleur HSLA est similaire, avec la valeur alpha en dernière position : hsla(teinte, saturation, luminosité, alpha).

### **CMYK**

Les couleurs CMYK sont une combinaison de CYAN, MAGENTA, JAUNE et NOIR. Les écrans d'ordinateur affichent les couleurs en utilisant des valeurs de couleur RVB. Les imprimantes présentent souvent les couleurs en utilisant des valeurs de couleur CMYK. CMYK n'est pas pris en charge en HTML, mais il est suggéré comme nouvelle norme en CSS4.

Exemples de couleurs : CMYK Rouge : cmyk(0%, 100%, 100%, 0%), CMYK Vert : cmyk(100%, 0%, 100%, 0%), ou CMYK Bleu : cmyk(100%, 100%, 0%, 0%).

### **Hexcodes**

Hexcode, abréviation de code hexadécimal, est un moyen d'exprimer une valeur de couleur à votre ordinateur. Il est nommé ainsi car 16 symboles uniques peuvent être utilisés comme valeurs. Dans ce cas, les chiffres de 0 à 9 et les lettres de a à f sont utilisés.

Les codes hexadécimaux sont exprimés dans ce format : #000000, qui serait la couleur noire dans ce cas. Six caractères sont utilisés dans chaque code hexadécimal, en utilisant l'un des 16 caractères mentionnés précédemment. Ces six caractères sont divisés en trois paires de deux.

Ces trois paires expriment chacune une valeur pour la quantité de rouge, de vert et de bleu dans une couleur particulière. Prenons le code hexadécimal de couleur #AA11BB, AA est la quantité de rouge, 11 la quantité de vert, et BB la quantité de bleu. 0 est la valeur la plus basse d'une couleur tandis que f est la valeur la plus élevée.

Les codes hexadécimaux ne sont pas sensibles à la casse, ce qui signifie que #FFFFFF et #ffffff seraient la même couleur : blanc.

De plus, il y a 16 777 216 combinaisons de couleurs possibles en utilisant le code hexadécimal.

### **Opacité**

La propriété d'opacité CSS3 définit l'opacité pour tout l'élément (à la fois la couleur d'arrière-plan et le texte seront opaques/transparents). Contrairement aux valeurs alpha spécifiées avec rgba et hsla, l'opacité est héritée par les éléments enfants.

La valeur de la propriété d'opacité doit être un nombre entre 0.0 (totalement transparent) et 1.0 (totalement opaque).

#### **Exemples**

```html
<html>
  <body>
    <p>Hello Moto</p>
  </body>
</html>
```

```css
body {
  background-color: green;
  color: white;
}
```

Dans l'exemple ci-dessus, `background-color: green` rend l'élément `<body>` vert. Cela rend toute la page web verte. Les éléments `<p>` sont tous blancs après `color: white` également. Vous pouvez utiliser des noms de couleurs, comme `green`, `blue`, `yellow`, `red`, `purple`, et bien d'autres. Mais pour des couleurs personnalisées, vous pouvez utiliser des codes hexadécimaux (`#147ACC`), des valeurs RVB (`rgb(20, 122, 204)`), et même des valeurs HSL (`hsl(145, 59%, 30%)`).

```css
p {
  color: rgba(244, 145, 14, 0.80); // orange vif
}

h2 {
 color: #FA8072; //saumon 
}
```

Vous pouvez également ajouter une valeur alpha, ou transparence aux couleurs. La transparence permet au texte d'être superposé sur une image et de laisser l'image partiellement visible à travers le texte, ou peut être utilisée pour changer la nuance de la couleur si aucun autre élément n'est devant ou derrière le texte. Utilisez `rgba()` ou `hsla()` et remplissez vos valeurs de couleur. La valeur alpha vient en dernier et est un pourcentage converti en décimal. (Par exemple, 20% est 0.2, 75% est 0.75, etc.)

```css
body {
  background-color: hsl(184, 87%, 94%); // bleu vif
}
```

Ci-dessus, les paragraphes sont stylisés en orange vif et 20% transparents, les éléments h2 en rose saumon, et l'arrière-plan du corps en bleu vif.

Pour obtenir des couleurs personnalisées à utiliser en CSS, vous pourriez trouver un sélecteur de couleurs utile. Certains éditeurs de texte ont des sélecteurs de couleurs intégrés, comme Visual Studio Code. Si vous recherchez "color picker" sur Google ou DuckDuckGo, vous obtiendrez un sélecteur de couleurs que vous pourrez utiliser. Google Chrome et Firefox ont également des modules complémentaires de sélecteur de couleurs que vous pouvez installer. Adobe Color CC ne vous aide pas seulement à choisir une couleur, mais vous aidera également à choisir une palette de couleurs pour votre page web ! 

Il est bon de vérifier que vous avez suffisamment de contraste entre votre texte et les couleurs d'arrière-plan en utilisant un outil comme le Vérificateur de Contraste de Couleurs de WebAIM.

## Exemple de couleurs en CSS

Les couleurs en CSS sont utilisées pour colorer les éléments dans nos pages web. Il existe de nombreuses façons d'assigner des couleurs aux éléments. Vous pouvez utiliser les noms réels des couleurs, leurs valeurs RVB ou les valeurs hexadécimales. En CSS3, le hsl (teinte-saturation-luminosité) a été ajouté à la spécification.

### **Noms de couleurs**

Actuellement, il y a 140 noms de couleurs pris en charge en HTML, qui peuvent être assignés dans les règles CSS en tapant simplement leur nom. Par exemple :

### **Syntaxe**

```text
p {
  color: green;
}
```

Cette règle change toute la couleur de police pour tous les éléments <p> en vert.  
Pour la liste complète des 140 couleurs, voir ici : [https://www.w3schools.com/colors/colors_names.asp](https://www.w3schools.com/colors/colors_names.asp)

### **Valeurs RVB**

RVB signifie "Rouge", "Vert" et "Bleu" et nous pouvons également assigner des couleurs en tapant leurs valeurs RVB dans nos règles. Une valeur RVB ressemblerait à ceci : rgb(255,0,0), où chaque nombre définit combien de chaque couleur sera dans le mélange final.

Les valeurs vont de 0 à 255, et dans notre exemple, nous voyons que seule la première valeur est 255 tandis que les deux autres sont définies à 0. Cela signifie qu'il n'y a que du rouge dans notre valeur et que l'élément respectif sera coloré en rouge. Une valeur RVB de (0, 0, 0) donnerait du noir et une valeur de (255, 255, 255) donnerait du blanc.

Il est impossible d'essayer de mémoriser chaque code de couleur, et pour cette raison, il existe de nombreux outils en ligne pour choisir les couleurs que vous voulez pour vos projets. Par exemple : [https://www.w3schools.com/colors/colors_picker.asp](https://www.w3schools.com/colors/colors_picker.asp) ou [http://htmlcolorcodes.com/color-picker/](http://htmlcolorcodes.com/color-picker/).

```css
p {
  color: rgb(0, 255, 0);
}
```

Cette règle change la couleur de police de tous les éléments p en vert, comme ci-dessus.

### **Valeurs hexadécimales**

Les valeurs hexadécimales sont une autre façon de définir les couleurs en CSS et elles fonctionnent de manière assez similaire aux valeurs RVB.

Un code hexadécimal aléatoire ressemblerait à ceci : `#29432b`, où les deux premiers caractères après le dièse représentent la quantité de ROUGE dans le mélange, les deux suivants représentent la quantité de Vert, et les deux derniers représentent la quantité de Bleu.

Les valeurs de `#000000` et `#ffffff` représentent respectivement le noir et le blanc.  
Vous pouvez trouver les couleurs hexadécimales spécifiques dont vous avez besoin en utilisant les mêmes outils mentionnés pour les valeurs RVB.

### **Syntaxe**

```text
p {
  color: #00fe00;
}
```

Cette règle change à nouveau la couleur de police de tous les éléments p en vert.

### **HSL**

HSL a trois valeurs. La première est la **Teinte**, qui est mesurée en degrés. Donc 0 (ou 360) représente la couleur rouge, à 120 c'est vert, et 240 est bleu. 

La deuxième est la **Saturation** qui a une valeur en pourcentage avec une plage de 0 à 100%. 

Et la troisième est la **Luminosité** qui a également une valeur en pourcentage avec une plage de 0 à 100%. 0% est noir foncé, 50% moyen, 100% est blanc.

### **Syntaxe**

```text
p {
  color: hsl(0, 100%, 50%);
}
```

### **Sortie**

[JSfiddle](https://jsfiddle.net/qcw2n145/)

### **Pourquoi utiliser les valeurs RGB ou HEX ?**

Les noms de couleurs ne prennent que 140 valeurs, tandis que les valeurs RGB et HEX ont 16 777 216 combinaisons possibles. Donc si vous voulez que vos projets aient exactement l'apparence que vous avez imaginée, vous devriez utiliser les deux dernières options et garder les valeurs des noms de couleurs pour les maquettes et les tests.

### Le mot-clé currentColor

Le mot-clé currentColor, comme son nom l'indique, est une valeur de couleur valide en CSS. Cela représente la valeur de la propriété `color` de l'élément spécifique. Cela vous permet d'utiliser la valeur de la propriété `color` pour les propriétés qui ne la reçoivent pas par défaut.

Par exemple, si nous déclarons chaque `div` pour avoir une bordure de 3px de couleur `currentColor`, ce qui signifie que chaque bordure de `div` sera colorée avec la même valeur que sa propriété `color`[:](http://jsfiddle.net/tjkp0cm3/)

```css
div{
  /* Le mot-clé currentColor pour la valeur de couleur, ce qui signifie que la bordure aura la valeur de la propriété color respective de la div */
  border: 3px solid currentColor;
}

/* Cette div aura des bordures vertes, car sa valeur de couleur est verte. */
#div1{
  color: green;
}

/* Cette div aura des bordures bleues, car sa valeur de couleur est bleue. */
#div2{
  color: blue;
}
```

### **Application pratique avec un SVG**

Voici un exemple très courant sur le web - un bouton avec une icône SVG et du texte dedans. La couleur de la bordure, du texte et des icônes change lorsque l'on survole le bouton. L'image ci-dessous représente les états initial et survolé du bouton dans l'ordre.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/button_variations.png)

Les polices d'icônes pourraient également être utilisées à cette fin, mais il existe divers avantages du SVG en ligne par rapport aux polices d'icônes, et cela peut faire des SVG le choix de nombreux développeurs. Citant [CSS-Tricks](https://css-tricks.com/icon-fonts-vs-svg/),

> Il peut être frustrant de positionner une icône de police. Les icônes sont insérées via un pseudo-élément, et cela dépend de `line-height`, `vertical-align`, `letter-spacing`, `word-spacing`, de la façon dont le glyphe de la police est conçu (a-t-il naturellement de l'espace autour de lui ? a-t-il des informations de crénage ?). Ensuite, le type d'affichage des pseudo-éléments affecte si ces propriétés ont un effet ou non. SVG a simplement la taille qu'il est.  
>   
> Pour résumer, il peut parfois être frustrant d'utiliser des icônes de police avec du texte.

Nous pourrions utiliser ce code pour obtenir le comportement souhaité :

```css
button {
  color: #016898;
}

.emailIcon {
  fill: #016898;
}

button:hover {
  color: #19B5FE;
}

button:hover .emailIcon {
  fill: #19B5FE;
}
```

Maintenant, au lieu de changer la couleur de remplissage `fill` du SVG au survol explicitement, nous pouvons définir le remplissage sur `currentColor`. Cela change automatiquement la couleur du SVG à la valeur de la propriété `color` du bouton. Nous devons maintenant simplement changer la propriété `color` du bouton. Cela rend le code CSS plus court et plus intelligent :

```css
.emailIcon {
  fill: currentColor;
}

button {
  color: #016898;
}

button:hover {
  color: #19B5FE;
}
```

Consultez l'exemple en direct à l'adresse [https://repl.it/NNt9/2](https://repl.it/NNt9/2).

## **Exemple de requêtes média CSS3**

Les requêtes média vous permettent d'avoir différents styles pour différents périphériques/tailles d'écran. Leur introduction dans CSS3 a grandement facilité la construction de pages web réactives.

La meilleure approche lors de la conception d'un site web réactif est de penser d'abord mobile ; ce qui signifie que vous créez votre page en commençant par la conception et le contenu de la version mobile. 

Vous pourriez penser qu'avec certaines tailles scalables (%, vw ou vh), votre page s'adaptera parfaitement à n'importe quel périphérique. Mais ce ne sera pas le cas. Peut-être pour un design très basique, mais certainement pas pour des pages plus courantes ou complexes !

Lorsque vous concevez votre page pour des périphériques plus petits, vous vous concentrerez sur le contenu principal. Sur un écran plus grand, vous devrez réadapter certaines tailles de police, marges, rembourrages, etc., afin de garder votre site confortable et lisible. Mais vous voudrez/devrez également ajouter plus de contenu, les éléments que vous n'avez pas jugés fondamentaux, et remplir l'espace créé par la taille de l'écran.

Le processus de réflexion devrait être :

1. Quel contenu montrer ?
2. Comment disposer ?
3. Taille ?

### **La syntaxe de base**

```css
    @media only screen and (min-width: 768px) {
      p {padding: 30px;}
    }
```

La balise `p` aura un remplissage de 30px dès que l'écran atteint une largeur minimale de 768px.

### **La syntaxe AND**

```css
  @media only screen and (min-height: 768px) and (orientation: landscape) {
    p {padding: 30px;}
  }
```

La balise `p` aura un remplissage de 30px dès que l'écran atteint une hauteur minimale de 768px et que son orientation est en mode paysage.

### **La syntaxe OR**

```css
    @media only screen and (min-width: 768px), (min-resolution: 150dpi) {
      p {padding: 30px;}
    }
```

La balise `p` aura un remplissage de 30px dès que l'écran atteint une largeur minimale de 768px ou que sa résolution atteint un minimum de 150dpi.

## **Exemple de polices CSS**

Les différentes propriétés de police CSS définissent la taille, le poids, le style, la hauteur de ligne et la famille de polices / type de police du texte sur la page.

### **Famille de polices**

La famille de polices ou le type de police du texte est défini en utilisant la propriété `font-family`.

Cette propriété fonctionne avec un système de secours - si votre navigateur ne prend pas en charge la première police, il essaiera chacune des polices suivantes jusqu'à ce qu'il en trouve une qu'il prend en charge. Si le nom de la police est plus long qu'un mot, il doit être entouré de guillemets. Par exemple :

```css
p {
    font-family: "Times New Roman", Times, serif;   
}
```

Times New Roman est composé de trois mots et doit être entouré de guillemets. Pendant ce temps, serif est juste un mot, donc il n'a pas besoin de guillemets.

Le dernier élément de la liste doit toujours être un nom de famille de polices générique tel que serif, sans-serif, monospace, cursive, fantasy, system-ui.

### **Style de police**

La propriété `font-style` peut être utilisée pour mettre le texte en italique ou en oblique.

Il y a trois valeurs possibles pour cette propriété :

* normal - Le texte est affiché normalement
* italic - Le texte est affiché en _italique_
* oblique - Le texte est affiché en penché

```css
.normal {
    font-style: normal;
}

.italic {
    font-style: italic;
}

.oblique {
    font-style: oblique;
}
```

### **Taille de police**

Utilisez la propriété `font-size` pour ajuster la taille du texte. La taille par défaut du texte est `16px` dans la plupart des navigateurs.

Voici les valeurs de taille de police les plus couramment utilisées :

* `px` (pixels)
* `em` - `1em` – la taille de police du parent
* `rem` – la taille de police de l'élément racine
* `%` - pourcentages

```css
.with-pixels {
    font-size: 14px;
}

.with-ems {
    font-size: 0.875em;
}

.with-absolute {
    font-size: large;
}

.with-percentage {
    font-size: 80%;
}
```

### **Poids de la police**

La propriété `font-weight` ajuste le poids du texte. Cette propriété accepte des valeurs de mots-clés comme `bold` ou `normal`, et des valeurs de mots-clés numériques telles que `400` et `700`.

Voici quelques valeurs de mots-clés et valeurs de mots-clés numériques courantes :

| Valeurs de mots-clés | Valeurs de mots-clés numériques |
| :---: | :---: |
| 100 | `thin` |
| 300 | `light` |
| 400 | `normal` |
| 500 | `medium` |
| 700 | `bold` |
| 900 | `black` |


Le poids de police par défaut est `400` ou `normal`.

```css
p {
   font-weight: bold
}
```

**Note :** Toutes les valeurs de mots-clés ou valeurs de mots-clés numériques ne sont pas disponibles pour chaque famille de polices. Par exemple, si vous chargez une famille de polices depuis Google Fonts, vous devez sélectionner tous les poids de police que vous souhaitez utiliser.

## **Exemple d'alignement de texte CSS**

Cette propriété CSS décrit l'alignement horizontal du contenu en ligne dans son élément de bloc parent. `text-align` ne contrôle pas l'alignement des éléments de bloc, il n'affecte que leur contenu en ligne.

### **Valeurs :**

La propriété `text-align` est spécifiée comme un seul mot-clé choisi dans la liste des valeurs ci-dessous :

`text-align: left;` aligne le texte à gauche

`text-align: right;` aligne le texte à droite

`text-align: center;` aligne le texte au centre

`text-align: justify;` rend les lignes de la même largeur

`text-align: justify-all;` rend les lignes de la même largeur, y compris la dernière

`text-align: start;` aligne la dernière ligne au début de la ligne

`text-align: end;` aligne la dernière ligne à la fin de la ligne

`text-align: match-parent;` calcule les valeurs de début et de fin selon la direction du parent et est remplacé par la valeur gauche ou droite appropriée.

**Valeurs d'alignement de bloc (syntaxe non standard) :**

`text-align: -moz-center;`

`text-align: -webkit-center;`

**Valeurs globales :**

`text-align: inherit;` hérite de son élément parent

`text-align: initial;` valeur par défaut

`text-align: unset;` applique soit la valeur inherit soit la valeur initial, selon les propriétés par défaut de l'élément

## **Exemple de modèle de boîte CSS**

Comprendre le modèle de boîte CSS est crucial pour pouvoir correctement mettre en page une page web.

Lorsque qu'un navigateur rend (dessine) une page web, chaque élément, par exemple, un morceau de texte ou une image, est dessiné comme une boîte rectangulaire suivant les règles du modèle de boîte CSS.

Au centre de la boîte se trouve le contenu lui-même, qui prend une certaine hauteur et largeur. Cette région est connue sous le nom de **Zone de contenu**. La taille de la zone de contenu peut être déterminée automatiquement, ou vous pouvez définir explicitement la taille de la hauteur et de la largeur (voir la note ci-dessous concernant `box-sizing`).

![Image de la zone de contenu](https://raw.githubusercontent.com/johnkennedy9147/Resources/master/CSS%20Box%20Model%20Images/content%20area.jpg)

Autour de la zone de contenu, il y a une région connue sous le nom de **Zone de remplissage**. La taille du remplissage peut être la même tout autour (définie avec `padding`), ou vous pouvez la définir individuellement pour les remplissages supérieur, droit, inférieur et gauche (avec `padding-top`, `padding-right`, `padding-bottom` et `padding-left`).

![Image de la zone de remplissage](https://raw.githubusercontent.com/johnkennedy9147/Resources/master/CSS%20Box%20Model%20Images/padding%20area.jpg)

Ensuite, il y a une **Zone de bordure**. Cela crée une bordure autour de l'élément et de son remplissage. Vous pouvez définir l'épaisseur (`border-width`), la couleur (`border-color`), et le style (`border-style`) de la bordure. Les options de style incluent `none` (pas de bordure), `solid`, `dashed`, `dotted` et plusieurs autres. 

De plus, vous pouvez définir les bordures sur les 4 côtés individuellement ; par exemple, la bordure supérieure avec `border-top-width`, `border-top-color` et `border-top-style` pour son épaisseur, sa couleur et son style. (Voir la note ci-dessous concernant `box-sizing`.)

![Image de la zone de bordure](https://raw.githubusercontent.com/johnkennedy9147/Resources/master/CSS%20Box%20Model%20Images/border%20area.jpg)

Enfin, il y a la **Zone de marge**. Cela crée un espace clair autour de l'élément, du remplissage et de la bordure. Encore une fois, vous pouvez définir individuellement les marges supérieure, droite, inférieure et gauche (avec `margin-top`, `margin-right`, `margin-bottom` et `margin-left`). Dans certaines circonstances, un effondrement de marge se produit et les marges entre les éléments adjacents peuvent être partagées.

![Image de la zone de marge](https://raw.githubusercontent.com/johnkennedy9147/Resources/master/CSS%20Box%20Model%20Images/margin%20area2.jpg)

**Propriété `box-sizing` :** La valeur par défaut de cette propriété est `content-box`. Si vous utilisez la valeur par défaut, alors le modèle de boîte permettra à l'auteur de spécifier la taille de la zone de contenu. Cependant, il est possible de les utiliser pour spécifier plutôt la taille de la zone de bordure. Cela se fait en changeant la propriété `box-sizing` en `border-box`. Cela peut parfois faciliter les mises en page. Vous pouvez définir la propriété `box-sizing` par élément comme souhaité.

## **Curseurs CSS**

La propriété cursor spécifie le type de curseur à afficher lorsque vous survolez un élément. Elle a 36 valeurs possibles :

```css
    .auto            { cursor: auto; }
    .default         { cursor: default; }
    .none            { cursor: none; }
    .context-menu    { cursor: context-menu; }
    .help            { cursor: help; }
    .pointer         { cursor: pointer; }
    .progress        { cursor: progress; }
    .wait            { cursor: wait; }
    .cell            { cursor: cell; }
    .crosshair       { cursor: crosshair; }
    .text            { cursor: text; }
    .vertical-text   { cursor: vertical-text; }
    .alias           { cursor: alias; }
    .copy            { cursor: copy; }
    .move            { cursor: move; }
    .no-drop         { cursor: no-drop; }
    .not-allowed     { cursor: not-allowed; }
    .all-scroll      { cursor: all-scroll; }
    .col-resize      { cursor: col-resize; }
    .row-resize      { cursor: row-resize; }
    .n-resize        { cursor: n-resize; }
    .e-resize        { cursor: e-resize; }
    .s-resize        { cursor: s-resize; }
    .w-resize        { cursor: w-resize; }
    .ns-resize       { cursor: ns-resize; }
    .ew-resize       { cursor: ew-resize; }
    .ne-resize       { cursor: ne-resize; }
    .nw-resize       { cursor: nw-resize; }
    .se-resize       { cursor: se-resize; }
    .sw-resize       { cursor: sw-resize; }
    .nesw-resize     { cursor: nesw-resize; }
    .nwse-resize     { cursor: nwse-resize; }
```

![Image](https://www.freecodecamp.org/news/content/images/2020/04/24_cursor_styles.gif)

Vous pouvez également définir une image comme curseur.

```text
.custom-cursor {
  cursor: url(cursor-image.png);
}
```