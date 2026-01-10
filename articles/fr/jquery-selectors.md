---
title: 'Sélecteurs jQuery expliqués : sélecteurs de classe, sélecteurs d''ID et plus'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-28T01:35:00.000Z'
originalURL: https://freecodecamp.org/news/jquery-selectors
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d58740569d1a4ca3745.jpg
tags:
- name: jQuery
  slug: jquery
- name: toothbrush
  slug: toothbrush
seo_title: 'Sélecteurs jQuery expliqués : sélecteurs de classe, sélecteurs d''ID et
  plus'
seo_desc: 'jQuery Selectors

  jQuery uses CSS-style selectors to select parts, or elements, of an HTML page. It
  then lets you do something with the elements using jQuery methods, or functions.

  To use one of these selectors, type a dollar sign and parentheses afte...'
---

## **Sélecteurs jQuery**

jQuery utilise des sélecteurs de style CSS pour sélectionner des parties, ou des éléments, d'une page HTML. Il permet ensuite de faire quelque chose avec les éléments en utilisant des méthodes jQuery, ou des fonctions.

Pour utiliser l'un de ces sélecteurs, tapez un signe dollar suivi de parenthèses : `$()`. C'est une abréviation pour la fonction `jQuery()`. À l'intérieur des parenthèses, ajoutez l'élément que vous souhaitez sélectionner. Vous pouvez utiliser des guillemets simples ou doubles. Après cela, ajoutez un point après les parenthèses et la méthode que vous souhaitez utiliser.

Dans jQuery, les sélecteurs de classe et d'ID sont similaires à ceux de CSS. Faisons un rapide rappel avant de continuer.

## **Sélecteur d'ID en CSS**

Le sélecteur d'ID CSS applique des styles à un élément HTML spécifique. Le sélecteur d'ID CSS doit correspondre à l'attribut ID d'un élément HTML. Contrairement aux classes, qui peuvent être appliquées à plusieurs éléments sur un site, un ID spécifique ne peut être appliqué qu'à un seul élément sur un site. Le CSS ID remplacera les propriétés de la classe CSS. Pour sélectionner un élément avec un ID spécifique, écrivez un caractère dièse (#), suivi de l'ID de l'élément.

### **Syntaxe**

```css
#specified_id { /* styles */ }
```

Vous pouvez combiner le sélecteur d'ID avec d'autres types de sélecteurs pour styliser un élément très spécifique.

```css
section#about:hover { color: blue; }

div.classname#specified_id { color: green; }
```

### **Note sur les IDs**

Il est préférable d'éviter d'utiliser les IDs pour le style lorsque cela est possible. Comme ils ont une spécificité élevée et ne peuvent être remplacés que si vous utilisez des styles en ligne ou ajoutez des styles dans `<style>`. Le poids de l'ID remplace les sélecteurs de classe et les sélecteurs de type.

Rappelez-vous, le sélecteur d'ID doit correspondre à l'attribut ID d'un élément HTML.

```html
<div id="specified_id"><!-- content --></div>
```

### **Spécificité**

Les sélecteurs d'ID ont une spécificité élevée, ce qui les rend difficiles à remplacer. Les classes ont une spécificité beaucoup plus faible et sont généralement la méthode préférée pour styliser les éléments afin d'éviter les problèmes de spécificité.

Voici un exemple de méthode jQuery qui sélectionne tous les éléments de paragraphe et ajoute une classe "selected" :

```javascript
<p>Ceci est un paragraphe sélectionné par une méthode jQuery.</p>
<p>Ceci est également un paragraphe sélectionné par une méthode jQuery.</p>

$("p").addClass("selected");
```

## Ok, retour à jQuery

Dans jQuery, les sélecteurs de classe et d'ID sont les mêmes que dans CSS. Si vous souhaitez sélectionner des éléments avec une certaine classe, utilisez un point (`.`) et le nom de la classe. Si vous souhaitez sélectionner des éléments avec un certain ID, utilisez le symbole dièse (`#`) et le nom de l'ID. Notez que HTML n'est pas sensible à la casse, il est donc préférable de garder le balisage HTML et les sélecteurs CSS en minuscules.

Sélection par classe :

```javascript
<p class="p-with-class">Paragraphe avec une classe.</p>

$(".p-with-class").css("color", "blue"); // colorie le texte en bleu
```

Sélection par ID :

```javascript
<li id="li-with-id">Élément de liste avec un ID.</li>

$("#li-with-id").replaceWith("<p>Chaussettes</p>");
```

Vous pouvez également sélectionner certains éléments avec leurs classes et IDs :

### **Sélection par classe**

Si vous souhaitez sélectionner des éléments avec une certaine classe, utilisez un point (.) et le nom de la classe.

```html
<p class="pWithClass">Paragraphe avec une classe.</p>
```

```javascript
$(".pWithClass").css("color", "blue"); // colorie le texte en bleu
```

Vous pouvez également utiliser le sélecteur de classe en combinaison avec un nom de balise pour être plus spécifique.

```html
<ul class="wishList">Ma liste de souhaits</ul>`<br>
```

```javascript
$("ul.wishList").append("<li>Nouveau mixeur</li>");
```

### **Sélection par ID**

Si vous souhaitez sélectionner des éléments avec une certaine valeur d'ID, utilisez le symbole dièse (#) et le nom de l'ID.

```html
<li id="liWithID">Élément de liste avec un ID.</li>
```

```javascript
$("#liWithID").replaceWith("<p>Chaussettes</p>");
```

Comme avec le sélecteur de classe, cela peut également être utilisé en combinaison avec un nom de balise.

```html
<h1 id="headline">Titre de l'actualité</h1>
```

```javascript
$("h1#headline").css("font-size", "2em");
```

### **Sélecteurs qui agissent comme des filtres**

Il existe également des sélecteurs qui agissent comme des filtres - ils commencent généralement par des deux-points. Par exemple, le sélecteur `:first` sélectionne l'élément qui est le premier enfant de son parent. Voici un exemple de liste non ordonnée avec quelques éléments de liste. Le sélecteur jQuery sous la liste sélectionne le premier élément `<li>` de la liste - l'élément de liste "One" - puis utilise la méthode `.css` pour rendre le texte vert.

```html
   <ul>
      <li>One</li>
      <li>Two</li>
      <li>Three</li>
   </ul>
```

```javascript
$("li:first").css("color", "green");
```

**Note :** N'oubliez pas qu'appliquer du CSS en JavaScript n'est pas une bonne pratique. Vous devez toujours définir vos styles dans des fichiers CSS.

Un autre sélecteur de filtrage, `:contains(text)`, sélectionne les éléments qui contiennent un certain texte. Placez le texte que vous souhaitez faire correspondre entre parenthèses. Voici un exemple avec deux paragraphes. Le sélecteur jQuery prend le mot "World" et change sa couleur en jaune.

```html
    <p>Bonjour</p>
    <p>Monde</p>
```

```javascript
$("p:contains('World')").css("color", "yellow");
```

De même, le sélecteur `:last` sélectionne l'élément qui est le dernier enfant de son parent. Le sélecteur jQuery ci-dessous sélectionne le dernier élément `<li>` de la liste - l'élément de liste "Three" - puis utilise la méthode `.css` pour rendre le texte jaune.

`$("li:last").css("color", "yellow");`

**Note :** Dans le sélecteur jQuery, `World` est entre guillemets simples car il est déjà à l'intérieur d'une paire de guillemets doubles. Utilisez toujours des guillemets simples à l'intérieur de guillemets doubles pour éviter de terminer une chaîne de caractères par inadvertance.

**Sélecteurs multiples** Dans jQuery, vous pouvez utiliser plusieurs sélecteurs pour appliquer les mêmes modifications à plus d'un élément, en utilisant une seule ligne de code. Pour ce faire, séparez les différents IDs par une virgule. Par exemple, si vous souhaitez définir la couleur de fond de trois éléments avec les IDs cat, dog et rat respectivement en rouge, faites simplement :

```text
$("#cat,#dog,#rat").css("background-color","red");
```

Ce ne sont là que quelques-uns des sélecteurs disponibles pour une utilisation dans jQuery. Voir la section Plus d'informations pour un lien vers la liste complète sur le site web de jQuery.

#### **Plus d'informations :**

* [Liste complète des sélecteurs jQuery](http://api.jquery.com/category/selectors/)