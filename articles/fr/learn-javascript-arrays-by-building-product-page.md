---
title: Apprenez à utiliser les tableaux JavaScript en créant une page produit iPhone
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-04-22T00:10:02.000Z'
originalURL: https://freecodecamp.org/news/learn-javascript-arrays-by-building-product-page
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/pexels-caleb-oquendo-9667337-min-1--1.jpg
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
- name: projects
  slug: projects
seo_title: Apprenez à utiliser les tableaux JavaScript en créant une page produit
  iPhone
seo_desc: 'By Samuel A. Olubiyo

  I had the idea for this tutorial while browsing the official iPhone website. Apple
  is known for its great products and impeccable design, and if you spend enough time
  checking out its website, you can learn a thing or two about b...'
---

Par Samuel A. Olubiyo

J'ai eu l'idée de ce tutoriel en parcourant le site officiel de l'iPhone. Apple est connue pour ses excellents produits et son design impeccable, et si vous passez suffisamment de temps à explorer son site web, vous pouvez apprendre une ou deux choses sur le branding et le bon design. 

L'une des choses qui a attiré mon attention en parcourant la page produit de l'iPhone 13 est la fonctionnalité où l'utilisateur peut sélectionner une couleur de téléphone parmi un choix de 3 ou 4 couleurs. Vous faites cela en cliquant sur un bouton de la couleur correspondante et la couleur du téléphone changera. 

Lorsque j'ai écrit cela, je ne savais pas comment Apple avait réalisé cela – mais pour démontrer mes connaissances des tableaux JavaScript, j'ai décidé de construire une version simple d'une page produit iPhone. Elle aurait des boutons qui pourraient changer la couleur du téléphone lorsqu'on clique dessus. 

Après avoir construit la page (et cela a fonctionné), j'ai réalisé que cela pourrait ne pas être la technique utilisée par Apple après tout. (Je partagerai pourquoi je pense cela dans la partie conclusion de ce tutoriel.) Toujours est-il, c'est un projet amusant et une façon d'apprendre les tableaux en JS.

Voici ce que nous allons couvrir :

* Comment configurer le HTML
* Comment configurer le CSS
* Comment configurer le JavaScript

Ce tutoriel suppose que vous avez quelques connaissances en manipulation du DOM avec JavaScript, HTML et CSS. Beaucoup de choses auront plus de sens si vous en avez. 

J'essaierai également, dans la mesure du possible, d'expliquer chaque partie du code en détail. Cela dit, commençons.

## Comment configurer le HTML

Avant de commencer, téléchargez des images de 3 ou 4 iPhones de différentes couleurs sur Internet. Vous pouvez trouver de telles images sur le site web de l'iPhone ou sur des sites de critique de téléphones.

Assurez-vous que les images que vous téléchargez ont des arrière-plans transparents, sont de la même taille et du même type (c'est-à-dire, si une image montre l'appareil photo arrière, toutes les images doivent être comme cela – mais de différentes couleurs et de la même taille.). 

Une fois que vous avez vos images, enregistrez-les dans un dossier et nommez le dossier **images**. À ce stade, vous devriez avoir créé un dossier principal pour ce projet. Si vous ne l'avez pas encore fait, vous pouvez le faire maintenant. Nommez votre dossier comme vous le souhaitez, mais assurez-vous que le dossier images que vous avez créé précédemment est dans le dossier principal.

Maintenant que vos dossiers sont prêts, il est temps de commencer à coder. Dans votre éditeur de code préféré (le mien est VSCode), naviguez jusqu'au dossier principal que vous avez créé précédemment et créez un nouveau fichier HTML. J'ai nommé le mien phone.html mais vous pouvez nommer le vôtre comme vous le souhaitez. 

Pour gagner du temps, j'ai utilisé une fonction emmet pour générer un modèle HTML – il suffit de presser un point d'exclamation et d'appuyer sur entrée.

Dans la balise body, créez une div principale et donnez-lui une classe « main » comme ceci :

```html
<div class="main">
</div>
```

Dans cette div principale, créez une autre div et donnez-lui un Id de « phone » comme ceci :

```html
<div id="phone">
</div>
```

Maintenant, dans la div « phone », créez une balise h3 et entrez : « J'adore les iPhones » ou vous pouvez remplacer 'adore' par un emoji. Dans mon cas, j'ai fait quelque chose comme ceci :

`<h3>J'&hearts; les iPhones</h3>`

En dessous de cette balise h3, créez une autre div et donnez-lui un id de « phoneshow » comme ceci :

`<div id="phoneShow"></div>`

Laissez cette div vide, mais en dessous, créez une autre div et donnez-lui un Id de « buttons ». Dans cette div, créez 4 balises span pour représenter les 4 boutons – c'est-à-dire, si vous avez téléchargé 4 images d'iPhone. 

Dans chaque balise span, créez une balise button et donnez à chaque bouton un id différent correspondant à la couleur des images du téléphone. Voici un exemple :

```html
<div id="buttons">
<span><button id="black"></button></span>
<span><button id="blue"></button></span>
<span><button id="pink"></button></span>
<span><button id="starlight"></button></span>
</div>
```

Après avoir fait cela, vous avez presque terminé avec la partie HTML de ce tutoriel. Il ne reste plus qu'à lier les fichiers CSS et JavaScript. 

Si vous n'avez pas encore créé de fichier CSS et JavaScript, c'est le moment de le faire. Dans mon cas, j'ai créé un fichier phone.css et un fichier phone.js. Ensuite, liez le fichier CSS dans la balise head comme ceci :

`<link rel="stylesheet" href="phone.css">`

Maintenant, liez votre fichier JavaScript en dessous de la dernière balise div de fermeture et juste au-dessus de la balise body de fermeture avec ce code :

`<script src="phone.js"></script>`

Après avoir fait cela, votre code HTML est complet.

## Comment configurer le CSS

Le code CSS pour ce projet est assez simple. Stylez le body, la div « main », la div « phone », la div « phoneshow », la div « buttons » et les boutons comme ceci :

```css
body{
display: flex;
flex-direction: column;
align-items: center;
justify-content: center;
background-color: rgb(255, 255, 255)
}

.main{
display: flex;
flex-direction: row;
flex-wrap: wrap;
align-items: center;
justify-content: center;
background-color: #ffff;
border-radius: 10px;
}

#phone{
display: flex;
flex-direction: column;
margin-bottom: 5px;
flex-wrap: nowrap;
align-items: center;
justify-content: center;
background-color: rgb(255, 255, 255);
border-radius: 10px;
}

#phoneShow{
display: flex;
flex-direction: row;
flex-wrap: wrap;
align-items: center;
justify-content: center;
background-color: #ffff;
border-radius: 10px;
}

#buttons{
display: flex;
flex-direction: row;
}

button{
margin-right: 10px;
border-radius: 50%;
padding: 15px;
border: none;
}
```

Note : `#buttons` est différent de `buttons`. Alors que le premier est une div, le second est l'élément bouton – d'où l'absence de sélecteur devant lui. Border-radius: 50%; rendra les boutons complètement ronds.

Ce code CSS utilise Flexbox.

Donnez à chaque bouton une couleur d'arrière-plan différente en stylisant leurs différents Ids en fonction de la couleur des images d'iPhone que vous avez téléchargées. Voici un exemple :

```css
#black{
background-color: black;
}
```

```css
#blue{
background-color: blue;
}
```

```css
#pink{
background-color: pink;
}
```

```css
#starlight{
background-color: silver;
}
```

Après avoir fait cela, vous pouvez prévisualiser votre progression dans le navigateur. Vous devriez voir 4 boutons ronds de différentes couleurs, centrés sur la page.

## Comment configurer le JavaScript

C'est la partie la plus importante de ce tutoriel. Jusqu'à présent, vous avez créé la structure de base et le style de la page. Mais pour afficher et changer les images du téléphone sur la page, la magie opère ici.

Tout d'abord, créez un tableau des répertoires des images que vous avez téléchargées au début de ce tutoriel. Vous souvenez-vous du dossier images de tout à l'heure ? Ce que vous devez faire, c'est stocker le chemin relatif de chaque image dans le dossier à l'intérieur d'un tableau sous forme de chaîne. Comme ceci :

```js
const phoneImages = ["images/Black.png", "images/Blue.png", "images/Pink.png", "images/Starlight.png"]
```

(En supposant que vos images sont enregistrées sous Black.png, Blue.png, etc.)

Ensuite, obtenez l'Id de la div où les images du téléphone apparaîtront. Pour ce tutoriel, les téléphones apparaîtront dans la div « phoneshow » de tout à l'heure. Stockez l'Id obtenu dans une variable comme ceci :

`let phoneCont = document.getElementById("phoneshow")`

Ensuite, obtenez les Ids de tous les boutons et stockez-les dans des variables, voici un exemple :

`let black=document.getElementById("black")`

`let blue=document.getElementById("blue")`

`let pink=document.getElementById("pink")`

`let starlight=document.getElementById("starlight")`

Après avoir fait cela, il est temps de faire apparaître une image d'iPhone. Pour ce faire, créez une variable appelée « defaultImgItems » car pour que la page fonctionne, il doit y avoir une image par défaut sur la page que l'utilisateur peut changer. 

Vous pouvez utiliser le code suivant pour cela :

```js
let defaultImgItems =`<img src= "${phoneImages.at(0)}">`
```

Permettez-moi d'expliquer :

L'utilisation de backticks `` nous permet d'insérer du code HTML dans notre JavaScript. Dans ce cas, je veux une balise image intégrée dans la variable `defaultImgItems`. La source est le premier élément du tableau phoneImages. Vous pouvez y accéder par la méthode `at()`.

Pour afficher l'image dans la div sélectionnée, utilisez simplement le code ci-dessous :

`phoneCont.innerHTML = defaultImgItems`

`phoneCont` est la variable où vous avez stocké la div avec l'Id « phoneshow » précédemment. Si vous actualisez la page dans le navigateur, vous devriez voir la première image d'iPhone dans le tableau `phoneImages` affichée. 

Après avoir fait cela, créez des variables similaires pour les trois autres couleurs comme ceci :

```js
let blueImgItems=`<img src= "${phoneImages.at(1)}">`
let pinkImgItems=`<img src= "${phoneImages.at(2)}">`
let starImgItems=`<img src= "${phoneImages.at(3)}">`
```

(Ces variables sont pour les deuxième, troisième et quatrième éléments du tableau `phoneImages`.)

### Comment faire fonctionner les boutons

Si vous avez fait cela avec succès, l'étape suivante consiste à rendre les boutons fonctionnels. Les boutons doivent pouvoir changer la couleur de l'iPhone en fonction de la couleur correspondante des boutons – c'est-à-dire que le bouton bleu doit afficher un iPhone bleu et ainsi de suite.

Pour y parvenir, attachez des écouteurs d'événements aux boutons et faites-les changer les propriétés `innerHTML` de phoneCont. Comme ceci :

```js
black.addEventListener("click", function(){
phoneCont.innerHTML=defaultImgItems
})
```

Le code ci-dessus fera en sorte que le bouton noir, lorsqu'on clique dessus, affiche un iPhone noir. Les extraits de code restants sont les suivants :

```js
blue.addEventListener("click", function(){
phoneCont.innerHTML = blueImgItems
})

pink.addEventListener("click", function(){
phoneCont.innerHTML = pinkImgItems
})

starlight.addEventListener("click", function(){
phoneCont.innerHTML = starImgItems
})
```

Après avoir fait cela, actualisez votre navigateur et cliquez sur chaque bouton à tour de rôle. Les images de l'iPhone devraient changer à chaque clic.

## Conclusion :

Dans ce tutoriel, vous avez appris une utilisation pratique des tableaux dans des projets réels. Vous avez également appris comment accéder aux éléments d'un tableau en utilisant la méthode .at().

Au début de ce tutoriel, j'ai mentionné que je ne pensais pas qu'Apple ait utilisé cette méthode pour construire leur page produit iPhone. Cela est dû au fait que lorsque vous chargez la page créée avec ce tutoriel et que vous cliquez sur chaque bouton à tour de rôle, les images de l'iPhone ne changent pas en douceur – plutôt, elles semblent sauter. Ce n'est qu'après que tous les boutons ont été cliqués que les images changent en douceur lorsque vous cliquez sur un nouveau bouton. Toujours est-il, j'espère que ce tutoriel vous a été bénéfique.

Vous pouvez me suivre sur Twitter pour des mises à jour sur ce que je fais ou toute nouvelle idée qui me vient à l'esprit à l'adresse https://[www.twitter.com/lordsamdev](http://www.twitter.com/lordsamdev). Vous pouvez également me faire savoir ce que vous pensez du code dans ce tutoriel – je suis ouvert à vos idées.

Merci d'avoir lu !