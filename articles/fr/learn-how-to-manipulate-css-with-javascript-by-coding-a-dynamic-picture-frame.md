---
title: Apprenez à manipuler le CSS avec JavaScript en codant un cadre photo dynamique
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-05-04T15:27:39.000Z'
originalURL: https://freecodecamp.org/news/learn-how-to-manipulate-css-with-javascript-by-coding-a-dynamic-picture-frame
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/Box-Model.png
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: Apprenez à manipuler le CSS avec JavaScript en codant un cadre photo dynamique
seo_desc: "By Samuel A. Olubiyo\nDOM manipulation can simply be defined as manipulating\
  \ HTML documents (or pages) with JavaScript. \nThe DOM stands for Document Object\
  \ Model that you can visualize as a tree-like structure made up of different HTML\
  \ elements. \nVisu..."
---

Par Samuel A. Olubiyo

La manipulation du DOM peut simplement être définie comme la manipulation de documents HTML (ou de pages) avec JavaScript.

Le DOM signifie Document Object Model que vous pouvez visualiser comme une structure en forme d'arbre composée de différents éléments HTML.

Visualiser un document HTML comme un arbre facilite l'accès à ses éléments et potentiellement leur modification. JavaScript nous aide à faire cela.

![Le DOM visualisé comme un arbre.](https://www.freecodecamp.org/news/content/images/2022/05/js-dom-model.png)
_Le DOM visualisé comme un arbre_

Maintenant, JavaScript est un langage puissant, donc non seulement nous pouvons manipuler des éléments HTML avec lui, mais nous pouvons également l'utiliser pour manipuler les propriétés CSS de n'importe quelle page web.

Dans ce tutoriel, je vais vous apprendre à manipuler le style d'une page web en construisant un simple projet.

Dans ce projet, nous allons coder un cadre photo en utilisant HTML et CSS, puis nous allons utiliser JavaScript pour rendre le cadre photo dynamique. Cela semble amusant ? Commençons !

## Comment créer le fichier HTML

Créez un dossier pour ce projet et nommez-le comme vous le souhaitez. Ensuite, naviguez jusqu'au dossier dans votre éditeur de code préféré et créez un nouveau fichier HTML. J'ai nommé le mien `box.html`, mais vous pouvez nommer le vôtre comme vous le souhaitez.

Ensuite, [générez un modèle HTML5](https://www.freecodecamp.org/news/html-starter-template-a-basic-html5-boilerplate-for-index-html/) en appuyant sur le point d'exclamation et en appuyant sur la touche Entrée.

À l'intérieur de la balise body, créez une balise h1 et tapez le titre de ce projet à l'intérieur. Dans mon cas, j'ai fait ceci :

`<h1>Cadre photo CSS</h1>`

Ensuite, créez une div et donnez-lui une classe "border" comme ceci :

`<div class = "border"></div>`

À l'intérieur de cette div, créez une autre div et donnez-lui une classe "padding" comme ceci :

`<div class = "padding"></div>`

À l'intérieur de la div "padding", créez une autre div et donnez-lui une classe "content" comme ceci :

`<div class = "content"></div>`

Maintenant, cette div "content" est l'endroit où l'image sera. Vous avez le choix d'utiliser soit une image, soit un emoji. J'ai choisi d'utiliser un emoji, donc j'ai fait quelque chose comme ceci :

`<div class = "content">🖼️</div>`

Jusqu'à présent, nous avons créé trois divs. Ensemble, elles devraient ressembler à ceci :

```html
<div class="border">
   <div class="padding">
       <div class="content">
            🖼️
                </div>
           </div>
       </div
```

Immédiatement en dessous du code ci-dessus, créez une nouvelle div et donnez-lui un Id "inputs" comme ceci :

`<div id = "inputs"></div>`

À l'intérieur de cette div "inputs", créez une autre div avec un Id "sliders", car nous allons créer des curseurs à l'intérieur.

Pour créer un curseur en HTML, faites simplement quelque chose comme ceci :

`<input type="range" name="" id=""  min="10" max="100">`

`<input type = "range">` crée une entrée de curseur, et les attributs `min` et `max` sont utilisés pour spécifier les valeurs minimale et maximale que le curseur peut avoir. Dans ce cas, le minimum est 10 et le maximum est 100.

Pour ce projet, nous avons besoin de 3 curseurs, un pour la "border", un pour le "padding", et un pour le "content", respectivement. Donnez à chaque curseur un Id qui a du sens ou vous pouvez simplement le faire comme je l'ai fait :

```html
<div id="sliders">
<h3>Border: </h3>
<input type="range" name="" id="border-range"  min="10" max="100">
<h3>Padding: </h3>
<input type="range" name="" id="padding-range" min="10" max="100">
<h3>Content: </h3>
<input type="range" name="" id="content-range" min="10" max="100">
</div>
```

En dessous de la div "sliders", créez une nouvelle div et donnez-lui un Id "colors", comme ceci :

`<div id = "colors"></div>`

car nous allons créer des sélecteurs de couleur dans cette div. Vous pouvez créer des sélecteurs de couleur en faisant ceci :

`<input type="color" name="" id="">`

Nous avons également besoin de 3 sélecteurs de couleur pour ce projet, un pour chaque div "border", "padding" et "content", respectivement. Alors, allez-y et créez trois sélecteurs de couleur dans la div "colors". Votre code devrait ressembler à ceci :

```html
<div id="colors">
<h3>Border:</h3>
<input type="color" name="" id="border-color">
<h3>Padding</h3>
<input type="color" name="" id="padding-color">
<h3>Content</h3>
<input type="color" name="" id="content-color">
</div>
```

Lorsque vous visualisez votre page dans le navigateur, vous devriez obtenir un résultat similaire à la capture d'écran ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screenshot--9--1.png)

L'étape suivante consiste à lier les fichiers CSS et JavaScript. Si vous ne l'avez pas déjà fait, vous devriez créer un fichier CSS et JS et les lier à votre HTML. Dans mon cas, j'ai créé un fichier `box.css` et un fichier `box.js`. N'oubliez pas de :

* Lier votre fichier CSS dans la balise head de votre HTML avec le code suivant : `<link rel="stylesheet" href="box.css">`
* Lier votre fichier JS dans la balise body tout en bas de votre code, immédiatement en dessous de la dernière div de fermeture et au-dessus de la balise body de fermeture comme ceci : `<script src="box.js"></script>`

Si vous avez fait cela avec succès, félicitations ! La partie HTML de ce tutoriel est maintenant complète. Voici le code HTML complet :

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Box Model</title>
    <link rel="stylesheet" href="box.css">
</head>
<body>
    <h1>CSS Picture Frame</h1>
        <div class="border">
            <div class="padding">
                <div class="content">
                    🖼️
                </div>
            </div>
        </div>

        <div id="inputs">
        <div id="sliders">
            <h3>Border: </h3>
            <input type="range" name="" id="border-range"  min="10" max="100">
            <h3>Padding: </h3>
            <input type="range" name="" id="padding-range" min="10" max="100">
            <h3>Content: </h3>
            <input type="range" name="" id="content-range" min="10" max="100"> 
        </div>

            <div id="colors">
                <h3>Border:</h3>
                <input type="color" name="" id="border-color">
                <h3>Padding</h3>
                <input type="color" name="" id="padding-color">
                <h3>Content</h3>
                <input type="color" name="" id="content-color">
            </div>
        </div>
        <script src="box.js"></script>
</body>
</html>
```

## Comment styliser la page web avec CSS

Ouvrez le fichier CSS que vous avez créé et ajoutez le code suivant :

```css
body{
display: flex;
align-items: center;
justify-content: center;
background-color: aquamarine;
flex-direction: column;
}
.border{
background-color: #0b67c4;
padding: 45px;
}
.padding{
background-color: #42b3dd;
padding: 45px;
}
.content{
background-color: #299baf;
padding: 45px;
font-size: 78px;
}
#inputs{
display: flex;
flex-direction: row;
}
#sliders{
margin-right: 30px;
}
```

**Note :** Ce style ne fonctionnera que si vous avez utilisé les mêmes Ids et classes que j'ai utilisés dans le HTML.

Maintenant, attardons-nous sur les styles `.border`, `.padding`, et `.content`. Vous remarquerez que, à part `.content`, ils ont tous deux règles à savoir : `background-color` et `padding`. Ce sont ces deux règles que nous allons manipuler avec notre code JavaScript.

Vous vous souvenez des curseurs et des sélecteurs de couleur que nous avons créés dans notre code HTML ? Nous allons utiliser les curseurs pour manipuler la propriété de padding de `.border`, `.padding`, et `.content` respectivement. Et nous allons utiliser les sélecteurs de couleur pour changer la propriété `background-color` de chacune des divs.

Lorsque vous actualisez votre navigateur, vous devriez avoir quelque chose de similaire à la capture d'écran ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screenshot--2--1.png)

## Comment écrire le JavaScript

Le code JS pour ce projet peut être divisé en trois parties. Tout d'abord, nous obtenons les Ids des curseurs et des sélecteurs de couleur et les stockons dans des variables. Ensuite, nous obtenons les classes des divs "border", "padding" et "content" et les stockons également dans des variables. Et enfin, nous attachons des écouteurs d'événements aux variables.

Puisque nous voulons que les curseurs changent la propriété de padding des divs et que les sélecteurs de couleur changent leurs couleurs de fond, nous utilisons l'écouteur d'événement de changement pour y parvenir.

Maintenant, il est temps de coder. Tout d'abord, obtenez les Ids des curseurs comme ceci et stockez-les dans des variables (en gardant à l'esprit les noms des Ids utilisés dans le code HTML.) :

```js
let borderRange = document.getElementById("border-range")
let paddingRange = document.getElementById("padding-range")
let contentRange = document.getElementById("content-range")
```

Ensuite, obtenez les Ids des sélecteurs de couleur et stockez-les également dans des variables, quelque chose comme ceci :

```js
let borderColor = document.getElementById("border-color")
let paddingColor = document.getElementById("padding-color")
let contentColor = document.getElementById("content-color")
```

Maintenant, obtenez les classes des divs border, padding et content en utilisant le `querySelector` comme ceci :

```js
let borderBox = document.querySelector(".border")
let paddingBox = document.querySelector(".padding")
let contentBox = document.querySelector(".content")
```

L'étape suivante après cela est d'attacher des écouteurs d'événements à chaque curseur et sélecteur de couleur. Pour faire en sorte que le premier curseur change la propriété CSS de padding de la div border, nous utilisons simplement le code suivant :

```js
borderRange.addEventListener("change", function(){
borderBox.style.padding = borderRange.value + "px"
})
```

Permettez-moi d'expliquer : L'écouteur d'événement de changement écoute un changement dans le curseur. Le code `borderBox.style.padding` est utilisé pour cibler la propriété de padding de borderBox.

`borderRange.value` obtient la valeur du curseur, et `+  "px"` ajoute px à quelle que soit cette valeur. Égaler `borderBox.style.padding` à `borderRange.value + "px"` est une façon de dire à notre code de changer la propriété de padding de borderBox à quelle que soit la valeur que borderRange saisit en pixels chaque fois que nous déplaçons le curseur (c'est-à-dire, l'événement de changement est déclenché).

Faites de même pour les divs padding et content comme ceci :

```js
paddingRange.addEventListener("change", function(){
paddingBox.style.padding = paddingRange.value + "px"
})
contentRange.addEventListener("change", function(){
contentBox.style.padding = contentRange.value + "px"
})
```

Après avoir fait cela, attachez des écouteurs d'événements aux sélecteurs de couleur en utilisant le même principe – sauf que, dans ce cas, les valeurs de couleur sont en hexadécimal, donc nous n'avons pas besoin d'ajouter d'unités à celles-ci.

Au lieu de cibler la propriété de padding, nous ciblons la propriété `backgroundColor` à la place. (Note : la syntaxe pour background-color en JS est en camel case.)

Votre code devrait ressembler à ceci :

```js
borderColor.addEventListener("change", function(){
borderBox.style.backgroundColor = borderColor.value
})
paddingColor.addEventListener("change", function(){
paddingBox.style.backgroundColor = paddingColor.value
})
contentColor.addEventListener("change", function(){
contentBox.style.backgroundColor = contentColor.value
})
```

Maintenant, lorsque vous actualisez votre navigateur, vous devriez être en mesure de changer les tailles des boîtes et leurs couleurs avec les curseurs et les sélecteurs de couleur. Avec ce code, vous pouvez créer un cadre photo de différentes tailles et couleurs.

![Image](https://www.freecodecamp.org/news/content/images/2024/08/sizes-and-colors-examples.jpg)

Voici le code JS complet :

```js
let borderRange = document.getElementById("border-range")

let paddingRange = document.getElementById("padding-range")

let contentRange = document.getElementById("content-range")


let borderColor = document.getElementById("border-color")

let paddingColor = document.getElementById("padding-color")

let contentColor = document.getElementById("content-color")


let borderBox = document.querySelector(".border")

let paddingBox = document.querySelector(".padding")

let contentBox = document.querySelector(".content")

borderRange.addEventListener("change", function(){
    borderBox.style.padding = borderRange.value + "px"
    console.log(borderRange.value)
   
})

paddingRange.addEventListener("change", function(){
    paddingBox.style.padding = paddingRange.value + "px"
    console.log(paddingRange.value)
   
})

contentRange.addEventListener("change", function(){
    contentBox.style.padding = contentRange.value + "px"
    console.log(contentRange.value)
})

borderColor.addEventListener("change", function(){
    borderBox.style.backgroundColor = borderColor.value
})


paddingColor.addEventListener("change", function(){
    paddingBox.style.backgroundColor = paddingColor.value
})

contentColor.addEventListener("change", function(){
    contentBox.style.backgroundColor = contentColor.value
})
```

## Conclusion

Vous pouvez utiliser les techniques de manipulation du DOM de JavaScript pour manipuler non seulement le fichier HTML mais aussi son style.

Les applications de cette connaissance ne sont limitées que par votre imagination. Vous pouvez créer de l'art CSS et des effets avec cette technique avec juste un peu de créativité.

Vous pouvez me suivre sur Twitter [à l'adresse https://www.twitter.com/lordsamdev](https://www.twitter.com/lordsamdev). Je tweete sur de nouvelles idées et projets sur lesquels je travaille. J'adorerais aussi voir ce que vous avez construit en suivant ce tutoriel.

Merci d'avoir lu.