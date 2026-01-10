---
title: Qu'est-ce que le DOM ? Signification du Document Object Model en JavaScript
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2021-09-27T16:23:19.000Z'
originalURL: https://freecodecamp.org/news/what-is-the-dom-document-object-model-meaning-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/joan-gamell-ZS67i1HLllo-unsplash-1.jpg
tags:
- name: beginners guide
  slug: beginners-guide
- name: Document Object Model
  slug: document-object-model
- name: DOM
  slug: dom
- name: JavaScript
  slug: javascript
seo_title: Qu'est-ce que le DOM ? Signification du Document Object Model en JavaScript
seo_desc: "If you have just started learning JavaScript, you might have heard of the\
  \ DOM. But what is it exactly?\nIn this article, I will explain what the DOM is\
  \ and provide some JavaScript code examples. \nWe will take a look at how to select\
  \ elements from an H..."
---

Si vous venez de commencer à apprendre JavaScript, vous avez peut-être entendu parler du DOM. Mais qu'est-ce que c'est exactement ?

Dans cet article, je vais expliquer ce qu'est le DOM et fournir quelques exemples de code JavaScript. 

Nous allons voir comment sélectionner des éléments d'un document HTML, comment créer des éléments, comment changer les styles CSS en ligne et comment écouter les événements. 

## Qu'est-ce que le DOM ?

DOM signifie Document Object Model. C'est une interface de programmation qui nous permet de créer, modifier ou supprimer des éléments du document. Nous pouvons également ajouter des événements à ces éléments pour rendre notre page plus dynamique. 

Le DOM voit un document HTML comme un arbre de nœuds. Un nœud représente un élément HTML. 

Examinons ce code HTML pour mieux comprendre la structure de l'arbre DOM. 

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Structure de l'arbre DOM</title>
  </head>
  <body>
    <h1>Structure de l'arbre DOM</h1>
	<h2>Apprendre sur le DOM</h2>
  </body>
</html>
```

Notre document est appelé le nœud racine et contient un nœud enfant qui est l'élément `<html>`. L'élément `<html>` contient deux enfants qui sont les éléments `<head>` et `<body>`. 

Les éléments `<head>` et `<body>` ont leurs propres enfants. 

Voici une autre façon de visualiser cet arbre de nœuds. 

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Document.jpg)

Nous pouvons accéder à ces éléments dans le document et leur apporter des modifications en utilisant JavaScript. 

Examinons quelques exemples de la façon dont nous pouvons travailler avec le DOM en utilisant JavaScript.

## Comment sélectionner des éléments dans le document

Il existe plusieurs méthodes différentes pour sélectionner un élément dans le document HTML.

Dans cet article, nous allons nous concentrer sur trois de ces méthodes :

* `getElementById()`
* `querySelector()` 
* `querySelectorAll()`

### `getElementById()`

En HTML, les `id` sont utilisés comme identifiants uniques pour les éléments HTML. Cela signifie que vous ne pouvez pas avoir le même nom d'`id` pour deux éléments différents.

Cela serait incorrect :

```html
<p id="para">Ceci est mon premier paragraphe.</p>
<p id="para">Ceci est mon deuxième paragraphe.</p>
```

Vous devriez vous assurer que ces `id` sont uniques comme ceci :

```html
<p id="para1">Ceci est mon premier paragraphe.</p>
<p id="para2">Ceci est mon deuxième paragraphe.</p>
```

 En JavaScript, nous pouvons récupérer une balise HTML en référençant le nom de l'`id`.

```js
document.getElementById("id name goes here")
```

Ce code indique à l'ordinateur de récupérer l'élément `<p>` avec l'`id` de `para1` et d'imprimer l'élément dans la console.

```js
const paragraph1 = document.getElementById("para1");
console.log(paragraph1);
```

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-26-at-2.25.49-PM.png)

Si nous voulions simplement lire le contenu du paragraphe, alors nous pouvons utiliser la propriété `textContent` à l'intérieur du `console.log()`. 

```js
const paragraph1 = document.getElementById("para1");
console.log(paragraph1.textContent);
```

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-26-at-2.35.31-PM.png)

### `querySelector()`

Vous pouvez utiliser cette méthode pour trouver des éléments avec un ou plusieurs sélecteurs CSS. 

J'ai créé cet exemple HTML de mes émissions de télévision préférées :

```html
<h1>Émissions de télévision préférées</h1>
<ul class="list">
  <li>Golden Girls</li>
  <li>Archer</li>
  <li>Rick and Morty</li>
  <li>The Crown</li>
</ul>
```

Si je voulais trouver et imprimer dans la console l'élément `h1`, alors je pourrais utiliser ce nom de balise à l'intérieur du `querySelector()`. 

```js
const h1Element = document.querySelector("h1");
console.log(h1Element);
```

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-26-at-3.15.59-PM.png)

Si je voulais cibler la `class="list"` pour imprimer la liste non ordonnée dans la console, alors j'utiliserais `.list` à l'intérieur du `querySelector()`. 

Le `.` avant `list` indique à l'ordinateur de cibler un nom de classe. Si vous vouliez cibler un `id`, alors vous utiliseriez un symbole `#` avant le nom. 

```js
const list = document.querySelector(".list");
console.log(list);
```

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-26-at-3.22.45-PM.png)

### `querySelectorAll()`

Cette méthode trouve tous les éléments qui correspondent au sélecteur CSS et retourne une liste de tous ces nœuds. 

Si je voulais trouver tous les éléments `<li>` dans notre exemple, je pourrais utiliser le combinateur enfant `>` pour trouver tous les enfants du `<ul>`. 

```js
const listItems = document.querySelectorAll("ul > li");
console.log(listItems); 
```

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-26-at-3.30.46-PM.png)

Si nous voulions imprimer les éléments `<li>` réels avec les émissions de télévision, nous pouvons utiliser un `forEach()` pour parcourir la NodeList et imprimer chaque élément.

```js
const listItems = document.querySelectorAll("ul > li");

listItems.forEach((item) => {
  console.log(item);
});
```

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-26-at-3.42.13-PM.png)

## Comment ajouter de nouveaux éléments au document

Nous pouvons utiliser `document.createElement()` pour ajouter de nouveaux éléments à l'arbre DOM. 

Examinons cet exemple :

```html
<h1>Raisons pour lesquelles j'aime freeCodeCamp :</h1>
```

Pour l'instant, je n'ai qu'une balise `<h1>` sur la page. Mais je veux ajouter une liste de raisons pour lesquelles j'aime freeCodeCamp sous cette balise `<h1>` en utilisant JavaScript. 

Nous pouvons d'abord créer un élément `<ul>` en utilisant `document.createElement()`. Je vais l'assigner à une variable appelée `unorderedList`. 

```js
let unorderedList = document.createElement("ul");

```

Ensuite, nous devons ajouter cet élément `<ul>` au document en utilisant la méthode `appendChild()`. 

```js
document.body.appendChild(unorderedList);
```

La partie suivante consiste à ajouter quelques éléments `<li>` à l'intérieur de l'élément `<ul>` en utilisant la méthode `createElement()`.

```js
let listItem1 = document.createElement("li");

let listItem2 = document.createElement("li");
```

Ensuite, nous pouvons utiliser la propriété `textContent` pour ajouter le texte de nos éléments de liste. 

```js
let listItem1 = document.createElement("li");
listItem1.textContent = "C'est gratuit";

let listItem2 = document.createElement("li");
listItem2.textContent = "C'est génial";

```

La dernière partie consiste à utiliser la méthode `appendChild()` pour que les éléments de liste puissent être ajoutés à la liste non ordonnée. 

```js
let listItem1 = document.createElement("li");
listItem1.textContent = "C'est gratuit";
unorderedList.appendChild(listItem1);

let listItem2 = document.createElement("li");
listItem2.textContent = "C'est génial";
unorderedList.appendChild(listItem2);
```

Voici à quoi ressemble le code dans son ensemble.

```js
let unorderedList = document.createElement("ul");
document.body.appendChild(unorderedList);

let listItem1 = document.createElement("li");
listItem1.textContent = "C'est gratuit";
unorderedList.appendChild(listItem1);

let listItem2 = document.createElement("li");
listItem2.textContent = "C'est génial";
unorderedList.appendChild(listItem2);
```

Voici à quoi ressemble la sortie sur la page :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-26-at-4.21.55-PM.png)

## Comment utiliser la propriété Style pour changer les styles CSS en ligne

La propriété `style` vous donne la possibilité de changer le CSS dans votre document HTML. 

Dans cet exemple, nous allons changer le texte `h1` de noir à bleu en utilisant la propriété `style`. 

Voici notre HTML.

```html
<h1>J'ai été changé en bleu en utilisant JavaScript</h1>

```

Nous devons d'abord récupérer la balise `h1` en utilisant la méthode `querySelector()`.

```js
const h1 = document.querySelector("h1");
```

Nous utilisons ensuite `h1.style.color` pour changer le texte `h1` de noir à bleu.

```js
const h1 = document.querySelector("h1");
h1.style.color = "blue";
```

Voici à quoi ressemble le résultat dans le navigateur :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-26-at-4.33.44-PM.png)

Vous pouvez utiliser cette propriété `style` pour changer un certain nombre de styles CSS en ligne, y compris `background-color`, `border-style`, `font-size` et plus encore. 

## Comment utiliser addEventListener() pour écouter les événements sur la page

Cette méthode vous permet d'attacher un événement à un élément HTML comme un bouton. 

Dans cet exemple, lorsque l'utilisateur clique sur le bouton, un message d'alerte s'affichera. 

Dans notre HTML, nous avons un élément bouton avec l'`id` de `btn`.

```html
  <button id="btn">Afficher l'alerte</button>

```

Nous pouvons cibler cet élément dans notre JavaScript en utilisant la méthode `getElementById()` et l'assigner à la variable appelée `button`.

```js
const button = document.getElementById("btn");

```

Le `addEventListener()` prend un type d'événement et une fonction. Le type d'événement sera un événement `click` et la fonction déclenchera le message d'alerte. 

Voici le code pour ajouter l'écouteur d'événement à la variable `button`.

```js
button.addEventListener("click", () => {
  alert("Merci d'avoir cliqué sur moi");
});
```

Voici le code complet où vous pouvez cliquer sur le bouton et le message d'alerte s'affichera :

%[https://codepen.io/jessica-wilkins/pen/abwQwPb?editors=1010]

## Comment utiliser le DOM dans des projets réels

C'était une brève introduction à certaines des méthodes DOM que vous pouvez utiliser. Il existe de nombreux autres exemples que nous n'avons pas couverts dans cet article. 

Si vous voulez commencer à construire des projets JavaScript pour débutants et travailler avec le DOM, alors je vous suggère de consulter mon article [40 projets JavaScript pour débutants](https://www.freecodecamp.org/news/javascript-projects-for-beginners/).

## Conclusion

DOM signifie Document Object Model et est une interface de programmation qui nous permet de créer, modifier ou supprimer des éléments du document. Nous pouvons également ajouter des événements à ces éléments pour rendre notre page plus dynamique. 

Vous pouvez sélectionner des éléments en JavaScript en utilisant des méthodes comme `getElementById(), querySelector()`, et `querySelectorAll()`.

Si vous voulez ajouter de nouveaux éléments au document, vous pouvez utiliser `document.createElement()`. 

Vous pouvez également changer les styles CSS en ligne des éléments en utilisant la propriété `style`.

Si vous voulez ajouter des événements à des éléments comme des boutons, alors vous pouvez utiliser `addEventListener()`. 

J'espère que vous avez apprécié cet article et bonne chance dans votre parcours JavaScript.