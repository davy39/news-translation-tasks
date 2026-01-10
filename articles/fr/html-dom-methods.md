---
title: Méthodes du DOM HTML
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-17T23:57:00.000Z'
originalURL: https://freecodecamp.org/news/html-dom-methods
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9dcb740569d1a4ca39af.jpg
tags:
- name: DOM
  slug: dom
- name: HTML
  slug: html
- name: toothbrush
  slug: toothbrush
seo_title: Méthodes du DOM HTML
seo_desc: 'querySelector()

  The Document method querySelector() returns the first element within the document
  that matches the specified selector, or group of selectors. If no matches are found,
  null is returned.

  HTML content:

  <div id="id-example"></div>

  <div cl...'
---

## querySelector()

La méthode `querySelector()` du Document retourne le `premier` élément dans le document qui correspond au sélecteur spécifié, ou à un groupe de sélecteurs. Si aucune correspondance n'est trouvée, null est retourné.

### Contenu HTML :

```html
<div id="id-example"></div>
<div class="class-example"></div>
<a>element-example</a> 
```

### Contenu JavaScript :

```javascript
document.querySelector("#id-example"); // Retourne l'élément avec l'id "id-example"
document.querySelector(".class-example"); // Retourne l'élément avec la classe "class-example"
document.querySelector("a"); // Retourne l'élément "a" 
```

Notez que `querySelector()` retourne le premier élément correspondant. Pour retourner toutes les correspondances, utilisez plutôt la méthode querySelectorAll().

```html
<div id="example">First</div>
<div id="example">Second</div>
```

```javascript
document.querySelector("#example"); // Retourne uniquement l'élément contenant 'First'
```

## **innerHTML** 

La propriété `innerHTML` retourne le contenu HTML à l'intérieur d'un élément sélectionné et permet également de définir un nouveau contenu HTML.

### Obtenir le contenu d'un élément

```html
<div id="demo">
  <p>Demo</p>
</div>
```

```javascript
var element = document.getElementById("demo");
console.log(element.innerHTML) // Affiche <p>Demo</p>
```

### Définir le contenu d'un élément

```html
<div id="demo"></div>
```

```javascript
var element = document.getElementById("demo");
element.innerHTML = "<div>Demo</div>";
```

Le HTML sera maintenant comme suit :

```html
<div id="demo">
  <div>Demo</div>
</div>
```

### Considérations de sécurité

La valeur attribuée à `innerHTML` doit provenir de sources fiables, car JavaScript placera n'importe quoi à l'intérieur de cet élément et cela sera exécuté comme du HTML simple.

Exemple :

Définir une valeur "`<script>alert();</script>`" provoquera l'exécution de la fonction JavaScript "alert()" :

```javascript
var element = document.getElementById("demo");

element.innerHTML = "<script>alert();</script>";
```

Ce type d'attaque est appelé [Cross Site Scripting, ou XSS](https://en.wikipedia.org/wiki/Cross-site_scripting).

C'est l'une des méthodes les plus courantes pour commettre une attaque XSS. Si vous souhaitez en apprendre un peu plus et apprendre à vous en défendre, [consultez cette ressource](https://xss-game.appspot.com/).

## getElementById()

La méthode `getElementById()` retourne l'élément qui a l'attribut id avec la valeur spécifiée. Elle prend un argument, qui est une chaîne de caractères sensible à la casse de l'id de l'élément que vous souhaitez.

Cette méthode est l'une des méthodes les plus courantes dans le DOM HTML et est utilisée presque chaque fois que vous souhaitez manipuler ou obtenir des informations d'un élément dans votre document. Voici un exemple simple de la syntaxe :

**Contenu HTML :**

```html
<div id="demo"></div>
```

**Contenu JavaScript :**

```javascript
document.getElementById("demo"); // Retourne l'élément avec l'id "demo"
```

Si vous avez plus d'un élément avec la même valeur d'`id` (mauvaise pratique !), `getElementById` retournera le premier élément trouvé :

```html
<div id="demo">First</div>
<div id="demo">Second</div>
```

```javascript
document.getElementById("demo"); // Retourne l'élément avec l'id "demo" contenant 'First'
```

#### **Plus d'informations :**

[document.getElementById()](https://developer.mozilla.org/en-US/docs/Web/API/Document/getElementById)

#### **Solutions alternatives :**

Une alternative couramment utilisée à `document.getElementById` est l'utilisation d'un sélecteur jQuery, que vous pouvez lire plus en détail [ici](https://github.com/freeCodeCamp/guides/tree/master/src/pages/jquery).

## Plus d'informations sur le DOM HTML

Avec le DOM HTML, JavaScript peut accéder et modifier tous les éléments d'un document HTML.

Lorsqu'une page web est chargée, le navigateur crée un **M**odèle **O**bjet **D**ocument de la page.

Le modèle DOM HTML est construit sous forme d'arbre d'objets :

Chaque élément dans le DOM est également appelé un nœud.

```html
<html>
<head>
  <title> Mon titre </title>
</head>
<body>
  <a href="#">Mon lien</a>
  <h1> Mon en-tête </h1>
</body>
</html>
```

Le DOM pour le HTML ci-dessus est le suivant :

![Arbre DOM](https://www.w3schools.com/js/pic_htmltree.gif)

Avec le modèle objet, JavaScript obtient tout le pouvoir dont il a besoin pour créer du HTML dynamique :

* JavaScript peut changer tous les éléments HTML dans la page
* JavaScript peut changer tous les attributs HTML dans la page
* JavaScript peut changer tous les styles CSS dans la page
* JavaScript peut supprimer des éléments et attributs HTML existants
* JavaScript peut ajouter de nouveaux éléments et attributs HTML
* JavaScript peut réagir à tous les événements HTML existants dans la page
* JavaScript peut créer de nouveaux événements HTML dans la page