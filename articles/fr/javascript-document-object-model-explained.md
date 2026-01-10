---
title: Comment manipuler le DOM en JavaScript – Techniques les plus couramment utilisées
subtitle: ''
author: Nathan Sebhastian
co_authors: []
series: null
date: '2023-12-07T22:19:23.000Z'
originalURL: https://freecodecamp.org/news/javascript-document-object-model-explained
coverImage: https://www.freecodecamp.org/news/content/images/2023/12/js-dom-manipulation-1.png
tags:
- name: Document Object Model
  slug: document-object-model
- name: DOM
  slug: dom
- name: JavaScript
  slug: javascript
seo_title: Comment manipuler le DOM en JavaScript – Techniques les plus couramment
  utilisées
seo_desc: 'Hi everyone! In this article, I’m going to cover everything you need to
  know about manipulating the DOM.

  Basically, each Element object in the DOM has properties and methods that you can
  use to interact with that element.

  The following are the most c...'
---

Bonjour à tous ! Dans cet article, je vais couvrir tout ce que vous devez savoir sur la manipulation du DOM.

En gros, chaque objet `Element` dans le DOM a des propriétés et des méthodes que vous pouvez utiliser pour interagir avec cet élément.

Voici les méthodes les plus courantes et pratiques pour manipuler l'objet `Element` :

1. [Changer le contenu d'un élément](#heading-changer-le-contenu-dun-element)
2. [Manipuler l'attribut de classe](#heading-manipuler-lattribut-de-classe)
3. [Définir des styles CSS en utilisant JavaScript](#heading-definir-des-styles-css-en-utilisant-javascript)
4. [Créer, ajouter et supprimer des éléments](#heading-creer-ajouter-et-supprimer-des-elements)
5. [Insérer un élément à une position spécifique](#heading-inserer-un-element-a-une-position-specifique)
6. [Manipuler les attributs d'élément](#heading-manipuler-les-attributs-delement)
7. [Manipuler les attributs de données](#heading-manipuler-les-attributs-de-donnees)

Manipuler le DOM semble complexe en théorie, mais comme vous le verrez dans cet article, il existe quelques méthodes que vous utiliserez encore et encore dans de nombreux scénarios.

Une fois que vous connaîtrez ces méthodes, vous aurez amélioré vos compétences en manipulation du DOM. Commençons !

## Changer le contenu d'un élément

Vous pouvez changer la valeur ou le contenu d'un élément en définissant la propriété `innerText` de cet élément.

Par exemple, supposons que vous avez un élément de paragraphe comme suit :

```html
<p class="myParagraph">Ceci est un paragraphe</p>

```

Ensuite, vous sélectionnez l'élément et changez sa valeur `innerText` comme ceci :

```js
const p = document.querySelector('.myParagraph');

p.innerText = 'Un nouveau jour se lève';

```

L'élément `p` aurait sa valeur changée comme vous le voyez ci-dessous :

```html
<p class="myParagraph">Un nouveau jour se lève</p>

```

Et c'est ainsi que vous changez la valeur d'un élément.

## Manipuler l'attribut de classe

Vous pouvez ajouter un nouvel attribut `class` à un `Element` en utilisant la méthode `add()` de l'objet `classList` :

```js
Element.classList.add('myClass');

```

Vous pouvez supprimer une classe en utilisant la méthode `remove()` :

```js
Element.classList.remove('myClass');

```

L'objet `classList` est un objet de collection que vous pouvez utiliser pour manipuler l'attribut `class` d'un `Element`.

Vous ne pouvez pas éditer directement la propriété `classList` car c'est une propriété en lecture seule. Mais vous pouvez utiliser ses méthodes pour changer les classes de l'élément.

Pour remplacer une classe existante par une nouvelle classe, utilisez la méthode `replace()` :

```js
Element.classList.replace('oldClass', 'newClass');

```

Il y a aussi la méthode `toggle()`, qui fonctionne comme un interrupteur : ajoute une classe si elle n'est pas là, supprime une classe si elle est là.

```js
Element.classList.toggle('myClass');

```

Pour vérifier si un élément contient une classe spécifique, utilisez la méthode `contains()` et passez la classe que vous voulez vérifier sous forme de chaîne :

```js
Element.classList.contains('myClass');

```

La méthode retourne `true` lorsque la classe est spécifiée. Sinon, elle retourne `false`.

## Définir des styles CSS en utilisant JavaScript

Puisque vous avez appris comment définir et supprimer des classes d'un élément, vous pouvez contrôler le style d'un élément en ajoutant ou en supprimant des classes qui changent les règles de style appliquées à un élément.

Par exemple, vous pourriez avoir les règles de style suivantes dans votre code CSS :

```css
.color-primary {
  color: #007bff;
}

.color-secondary {
  color: #6c757d;
}

.bold {
  font-weight: 700;
}

```

Si vous avez un élément avec la classe `color-primary` appliquée, vous pouvez la remplacer par la classe `color-secondary`, ou ajouter la classe `bold`.

Supposons que vous avez un élément de paragraphe comme suit :

```html
<p class="myParagraph">Un nouveau jour se lève</p>

```

Voici comment vous changez le style en utilisant des classes :

```js
const p = document.querySelector('.myParagraph');

// ajouter une classe à l'élément
p.classList.add('color-primary');

// remplacer une classe
p.classList.replace('color-primary', 'color-secondary');

// supprimer une classe
p.classList.remove('color-secondary');

```

Parfois, vous pourriez avoir besoin d'appliquer du CSS directement à l'élément DOM que vous avez sélectionné.

L'objet `Element` vous fournit la propriété `style` qui contrôle le style en ligne de l'élément.

Par exemple, vous pouvez changer le poids de la police d'un élément en utilisant la propriété `Element.style.fontWeight` comme ceci :

```js
const p = document.querySelector('.myParagraph');

p.style.fontWeight = '700'; // définir le poids de la police
p.style.textTransform = 'uppercase'; // définir en majuscules
p.style.color = '#007bff'; // définir la couleur

```

Vous pouvez changer le style de bordure d'un élément comme suit :

```js
p.style.border = '1px solid black';

```

La propriété `style` utilise le camelCase au lieu du hyphen-case, donc `font-weight` devient `fontWeight` et `text-transform` devient `textTransform`.

Et maintenant vous savez comment définir des styles CSS en utilisant JavaScript. Je vous recommande de changer les styles des éléments en ajoutant et en supprimant des classes car c'est plus maintenable et suit l'approche commune.

N'accédez à la propriété `style` que si vous n'utiliserez pas le même style ailleurs.

## Créer, ajouter et supprimer des éléments

En plus de créer un arbre DOM à partir de votre fichier HTML, vous avez également la capacité de créer des éléments DOM de manière programmatique en utilisant JavaScript.

Cela est possible car l'objet `document` dispose également de la méthode `createElement()`, qui vous permet de créer n'importe quel objet `Element`, qui est essentiellement les balises que vous écrivez dans votre fichier HTML.

Par exemple, vous pouvez créer un élément de paragraphe comme ceci :

```js
const p = document.createElement('p');

```

Après avoir créé cet élément, vous pouvez y ajouter du contenu en utilisant la propriété `innerText` :

```js
p.innerText = 'Ce paragraphe est créé en utilisant JavaScript';

```

Maintenant, vous devez l'ajouter à l'arbre DOM existant pour qu'il apparaisse à l'écran. Vous pouvez attacher l'élément n'importe où à l'intérieur de votre structure d'arbre existante.

Supposons que vous voulez ajouter le paragraphe à la balise `body`. Vous devez alors utiliser la méthode `querySelector()` pour sélectionner le `body`, et appeler la méthode `append()` sur l'élément :

```js
const p = document.createElement('p');

p.innerText = 'Ce paragraphe est créé en utilisant JavaScript';

const body = document.querySelector('body');

body.append(p);

```

Le paragraphe sera ajouté en tant qu'enfant de la balise `body` comme suit :

```html
<body>
<p>Ce paragraphe est créé en utilisant JavaScript</p>
</body>

```

Si vous voulez supprimer un élément, vous pouvez appeler la méthode `remove()` depuis l'élément que vous voulez supprimer.

Ce code supprimera l'élément de paragraphe :

```js
p.remove();

```

## Insérer un élément à une position spécifique

La méthode `append()` que nous avons explorée ci-dessus insérera un nouvel élément en tant que dernier enfant de l'élément parent.

Si vous voulez insérer l'élément à une position spécifique, vous pouvez utiliser la méthode `insertBefore()`.

Voyons un exemple simple. Supposons que vous avez un contenu HTML comme suit :

```html
<body>
    <p id="first">Le premier paragraphe</p>
</body>

```

Pour insérer un élément avant le premier paragraphe, vous devez appeler la méthode `insertBefore()` depuis l'élément parent (qui est la balise `body`) et lui passer deux arguments :

1. Le nouvel élément que vous voulez ajouter
2. L'élément frère avant lequel le nouvel élément est inséré

Voici un exemple de création d'un deuxième paragraphe et de son insertion avant le premier paragraphe :

```js
let p2 = document.createElement('p');

p2.innerText = 'Le deuxième paragraphe';

let body = document.querySelector('body');
let p1 = document.querySelector('#first');

body.insertBefore(p2, p1);

```

En résultat de l'exécution du script ci-dessus, le deuxième paragraphe sera inséré avant le premier paragraphe :

```html
<body>
    <p>Le deuxième paragraphe</p>
    <p id="first">Le premier paragraphe</p>
</body>

```

Gardez à l'esprit que le DOM ne fournit pas de méthode `insertAfter`, car ce n'est pas nécessaire.

Vous utilisez la méthode `append()` pour insérer un élément à la dernière position, et si vous voulez contrôler la position, utilisez la méthode `insertBefore()`.

## Manipuler les attributs d'élément

L'objet `classList` ne fournit que des méthodes pour changer la `class` d'un élément. Si vous voulez changer d'autres attributs comme `id`, `href`, ou `src`, vous pouvez utiliser la méthode `setAttribute()`.

La méthode `setAttribute()` accepte deux arguments :

1. Le nom de l'attribut à définir
2. La valeur de l'attribut à définir

Par exemple, voici comment définir l'attribut `src` d'une balise `img` :

```html
<img id="profile-pic" src="feature-image.png" />

```

Sélectionnez l'élément `img` en utilisant `querySelector()`, puis appelez la méthode `setAttribute()` sur l'élément :

```js
const img = document.querySelector('#profile-pic');

img.setAttribute('src', 'new-image.jpg');

```

La valeur de l'attribut `src` serait changée comme suit :

```html
<img id="profile-pic" src="new-image.jpg" />

```

Si vous voulez obtenir la valeur d'un attribut, vous pouvez utiliser la méthode `getAttribute()`.

Passez l'attribut que vous voulez vérifier en tant qu'argument à la méthode. Si l'attribut est défini, la méthode retourne la valeur de cet attribut sous forme de chaîne. Sinon, elle retourne `null` :

```js
img.getAttribute('src'); // new-image.jpg
img.getAttribute('href'); // null

```

Vous pouvez utiliser les méthodes `setAttribute()` et `getAttribute()` pour interagir avec n'importe quel attribut HTML.

Si vous voulez supprimer un attribut, utilisez la méthode `removeAttribute()` :

```js
const img = document.querySelector('#profile-pic');

// Supprimer l'attribut src
img.removeAttribute('src');

```

## Manipuler les attributs de données

L'attribut de données est utilisé pour stocker des informations supplémentaires sur les éléments HTML. La manière dont vous utilisez les données vous appartient.

Supposons que vous avez une balise HTML comme suit :

```html
<div id="intro" data-attribute-theme="light" data-session="2022">
  Bonjour le monde !
</div>

```

Vous pouvez accéder aux attributs de données depuis la propriété `dataset` de l'élément ci-dessus comme ceci :

```js
// Sélectionner le div
let myDiv = document.querySelector('#intro');

// Accéder à la propriété dataset
console.log(myDiv.dataset.session) // 2022

// Utiliser le camelCase lorsque votre attribut de données est composé de plusieurs mots
console.log(myDiv.dataset.attributeTheme) // light

```

Si vous voulez changer la valeur de l'attribut, vous pouvez réassigner la bonne propriété `dataset` à une nouvelle valeur directement :

```js
// Sélectionner le div
let myDiv = document.querySelector('#intro');

// Changer la valeur d'un attribut de données
myDiv.dataset.session = '2023'

```

Si vous voulez supprimer l'attribut de données, utilisez la méthode `removeAttribute()` de manière similaire à la suppression d'un attribut régulier :

```js
let myDiv = document.querySelector('#intro');

// Supprimer l'attribut data-session
myDiv.removeAttribute('data-session');

// Supprimer l'attribut data-attribute-theme
myDiv.removeAttribute('data-attribute-theme');

```

Et c'est ainsi que vous manipulez l'attribut de données en utilisant JavaScript.

## Conclusion

Et c'est tout pour l'instant sur les manipulations d'éléments DOM. À ce stade, j'espère que vous pouvez voir pourquoi JavaScript est nécessaire pour construire une application web moderne. Il vous permet d'interagir et de changer le contenu qui existe sur votre site web.

Cela permet de nombreux changements dynamiques sur le site web que vous avez créé.

Si vous avez aimé cet article et que vous souhaitez faire passer vos compétences en JavaScript au niveau supérieur, je vous recommande de consulter mon nouveau livre _Beginning Modern JavaScript_ [ici](https://www.amazon.com/dp/B0CQXHMF8G).

[![beginning-js-cover](https://www.freecodecamp.org/news/content/images/2024/01/beginning-js-cover.png)](https://www.amazon.com/dp/B0CQXHMF8G)

Le livre est conçu pour être facile à comprendre et accessible à toute personne souhaitant apprendre JavaScript. Il fournit un guide progressif et doux qui vous aidera à comprendre comment utiliser JavaScript pour créer une application dynamique.

Voici ma promesse : _Vous allez vraiment avoir l'impression de comprendre ce que vous faites avec JavaScript._

À la prochaine fois !