---
title: Une introduction au DOM JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-27T18:19:32.000Z'
originalURL: https://freecodecamp.org/news/an-introduction-to-the-javascript-dom-512463dd62ec
coverImage: https://cdn-media-1.freecodecamp.org/images/0*QqW2LsIY0wf5BeDv
tags:
- name: Document Object Model
  slug: document-object-model
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Une introduction au DOM JavaScript
seo_desc: 'By Gabriel Tanner

  The Javascript DOM (Document Object Model) is an interface that allows developers
  to manipulate the content, structure and style of a website. In this article, we
  will learn what the DOM is and how you can manipulate it using Javasc...'
---

Par Gabriel Tanner

Le DOM JavaScript (Document Object Model) est une interface qui permet aux développeurs de manipuler le contenu, la structure et le style d'un site web. Dans cet article, nous allons apprendre ce qu'est le DOM et comment vous pouvez le manipuler en utilisant JavaScript. Cet article peut également être utilisé comme référence pour les opérations de base du DOM.

### Qu'est-ce que le DOM ?

Au niveau le plus basique, un site web se compose d'un document HTML et CSS. Le navigateur crée une représentation du document connue sous le nom de Document Object Model (DOM). Ce document permet à JavaScript d'accéder et de manipuler les éléments et les styles d'un site web. Le modèle est construit dans une structure d'arbre d'objets et définit :

* Les éléments HTML en tant qu'objets
* Les propriétés et les événements des éléments HTML
* Les méthodes pour accéder aux éléments HTML

![Image](https://cdn-media-1.freecodecamp.org/images/g42eKZ-RmFNQVN5EZ1lF2wj67VqIdX7DMk4Z)
_Model DOM HTML_

Les emplacements des éléments sont appelés nœuds. Non seulement les éléments obtiennent des nœuds, mais aussi les attributs des éléments et le texte obtiennent leur propre nœud (nœuds d'attributs et nœuds de texte).

### Document DOM

Le Document DOM est le propriétaire de tous les autres objets dans votre page web. Cela signifie que si vous voulez accéder à un objet sur votre page web, vous devez toujours commencer par le document. Il contient également de nombreuses propriétés et méthodes importantes qui nous permettent d'accéder et de modifier notre site web.

### Trouver des éléments HTML

Maintenant que nous comprenons ce qu'est le document DOM, nous pouvons commencer à obtenir nos premiers éléments HTML. Il existe de nombreuses façons différentes de le faire en utilisant le DOM JavaScript, voici les plus courantes :

#### Obtenir un élément par ID

La méthode _getElementById()_ est utilisée pour obtenir un seul élément par son ID. Regardons un exemple :

```
var title = document.getElementById('header-title');
```

Ici, nous obtenons l'élément avec l'ID header-title et le sauvegardons dans une variable.

#### Obtenir des éléments par nom de classe

Nous pouvons également obtenir plus d'un objet en utilisant la méthode _getElementsByClassName()_ qui retourne un tableau d'éléments.

```
var items = document.getElementsByClassName('list-items');
```

Ici, nous obtenons tous les éléments avec la classe _list-items_ et les sauvegardons dans une variable.

#### Obtenir un élément par nom de balise

Nous pouvons également obtenir nos éléments par nom de balise en utilisant la méthode _getElementsByTagName()_.

```
var listItems = document.getElementsByTagName('li');
```

Ici, nous obtenons tous les éléments _li_ de notre document HTML et les sauvegardons dans une variable.

#### QuerySelector

La méthode _querySelector()_ retourne le premier élément qui correspond à un sélecteur CSS spécifié. Cela signifie que vous pouvez obtenir des éléments par ID, classe, balise et tous les autres sélecteurs CSS valides. Voici quelques-unes des options les plus populaires.

**Obtenir par ID :**

```
var header = document.querySelector('#header')
```

**Obtenir par classe :**

```
var items = document.querySelector('.list-items')
```

**Obtenir par balise :**

```
var headings = document.querySelector('h1');
```

**Obtenir des éléments plus spécifiques :**

Nous pouvons également obtenir des éléments plus spécifiques en utilisant des _sélecteurs CSS_.

```
document.querySelector("h1.heading");
```

Dans cet exemple, nous recherchons une balise et une classe en même temps et retournons le premier élément qui passe le sélecteur CSS.

#### QuerySelectorAll

La méthode _querySelectorAll()_ est complètement identique à _querySelector()_ sauf qu'elle retourne tous les éléments qui correspondent au sélecteur CSS.

```
var heading = document.querySelectorAll('h1.heading');
```

Dans cet exemple, nous obtenons toutes les balises _h1_ qui ont une classe _heading_ et les stockons dans un tableau.

### Changer les éléments HTML

Le DOM HTML nous permet de changer le contenu et le style d'un élément HTML en modifiant ses propriétés.

#### Changer le HTML

La propriété innerHTML peut être utilisée pour changer le contenu d'un élément HTML.

```
document.getElementById("#header").innerHTML = "Hello World!";
```

Dans cet exemple, nous obtenons l'élément avec l'ID header et définissons le contenu interne sur "Hello World!".

InnerHTML peut également être utilisé pour mettre des balises dans une autre balise.

```
document.getElementsByTagName("div").innerHTML = "<h1>Hello World!</h1>"
```

Ici, nous mettons une balise h1 dans toutes les div déjà existantes.

#### **Changer la valeur d'un attribut**

Vous pouvez également changer la valeur d'un attribut en utilisant le DOM.

```
document.getElementsByTag("img").src = "test.jpg";
```

Dans cet exemple, nous changeons le src de toutes les balises _<img/>_ en test.jpg.

#### Changer le style

Pour changer le style d'un élément HTML, nous devons changer la propriété style de nos éléments. Voici un exemple de syntaxe pour changer les styles :

```
document.getElementById(id).style.property = new style
```

Maintenant, regardons un exemple où nous obtenons un élément et changeons la bordure inférieure en une ligne noire solide :

```
document.getElementsByTag("h1").style.borderBottom = "solid 3px #000";
```

Les propriétés CSS doivent être écrites en camelCase au lieu du nom de propriété CSS normal. Dans cet exemple, nous avons utilisé borderBottom au lieu de border-bottom.

### Ajouter et supprimer des éléments

Maintenant, nous allons voir comment nous pouvons ajouter de nouveaux éléments et supprimer ceux qui existent.

#### Ajouter des éléments

```
var div = document.createElement('div');
```

Ici, nous créons simplement un élément div en utilisant la méthode _createElement()_ qui prend un nom de balise comme paramètre et le sauvegarde dans une variable. Après cela, nous devons simplement lui donner du contenu et ensuite l'insérer dans notre document DOM.

```js
var newContent = document.createTextNode("Hello World!"); 
div.appendChild(newContent);
document.body.insertBefore(div, currentDiv);
```

Ici, nous créons du contenu en utilisant la méthode createTextNode() qui prend une chaîne comme paramètre, puis nous insérons notre nouvel élément div avant une div qui existe déjà dans notre document.

#### Supprimer des éléments

```js
var elem = document.querySelector('#header');
elem.parentNode.removeChild(elem);
```

Ici, nous obtenons un élément et le supprimons en utilisant la méthode removeChild().

#### Remplacer des éléments

Maintenant, voyons comment nous pouvons remplacer des éléments.

```js
var div = document.querySelector('#div');
var newDiv = document.createElement('div');
newDiv.innerHTML = "Hello World2"
div.parentNode.replaceChild(newDiv, div);
```

Ici, nous remplaçons un élément en utilisant la méthode _replaceChild()_. Le premier argument est le nouvel élément et le deuxième argument est l'élément que nous voulons remplacer.

#### Écrire directement dans le flux de sortie HTML

Nous pouvons également écrire des expressions HTML et JavaScript directement dans le flux de sortie HTML en utilisant la méthode write().

```js
document.write("<h1>Hello World!</h1><p>This is a paragraph!</p>");
```

Nous pouvons également passer des expressions JavaScript comme un objet date.

```
document.write(Date());
```

La méthode write() peut également prendre plusieurs arguments qui seront ajoutés au document dans l'ordre de leur occurrence.

### Gestionnaires d'événements

Le DOM HTML permet également à JavaScript de réagir aux événements HTML. Voici quelques-uns des plus importants :

* clic de souris
* chargement de page
* mouvement de souris
* changement de champ de saisie

#### Assigner des événements

Vous pouvez définir des événements directement dans votre code HTML en utilisant des attributs sur vos balises. Voici un exemple d'un événement _onclick_ :

```
<h1 onclick="this.innerHTML = 'Hello!'">Click me!</h1>
```

Dans cet exemple, le texte du <h1/> changera en "Hello!" lorsque vous cliquerez sur le bouton.

Vous pouvez également appeler des fonctions lorsqu'un événement est déclenché comme vous pouvez le voir dans l'exemple suivant.

```
<h1 onclick="changeText(this)">Click me!</h1>
```

Ici, nous appelons la méthode _changeText()_ lorsque le bouton est cliqué et passons l'élément en tant qu'attribut.

Nous pouvons également assigner les mêmes événements dans notre code JavaScript.

```
document.getElementById("btn").onclick = changeText();
```

#### Assigner des écouteurs d'événements

Maintenant, voyons comment vous pouvez assigner des écouteurs d'événements à vos éléments HTML.

```
document.getElementById("btn").addEventListener('click', runEvent);
```

Ici, nous avons simplement assigné un événement de clic qui appelle la méthode runEvent lorsque notre élément btn est cliqué.

Vous pouvez également assigner plusieurs événements à un seul élément :

```
document.getElementById("btn").addEventListener('mouseover', runEvent);
```

### Relations entre nœuds

Les nœuds dans le Document DOM ont une relation hiérarchique les uns avec les autres. Cela signifie que les nœuds sont structurés comme un arbre. Nous utilisons les termes parent, frère et enfant pour décrire la relation entre les nœuds.

Le nœud supérieur est appelé la racine et est le seul nœud qui n'a pas de parent. La racine dans un document HTML normal est la balise <html/> car elle n'a pas de parent et est la balise supérieure du document.

#### Navigation entre les nœuds

Nous pouvons naviguer entre les nœuds en utilisant ces propriétés :

* parentNode
* childNodes
* firstChild
* lastChild
* nextSibling

Voici un exemple de la façon dont vous pouvez obtenir l'élément parent d'un h1.

```
var parent = document.getElementById("heading").parentNode
```

### Conclusion

Vous avez réussi jusqu'à la fin ! Espérons que cet article vous a aidé à comprendre le DOM JavaScript et comment l'utiliser pour manipuler les éléments de votre site web.

Si vous souhaitez lire plus d'articles comme celui-ci, vous pouvez visiter mon [site web](https://gabrieltanner.org/) ou commencer à suivre mon [bulletin d'information](https://gabrieltanner.us20.list-manage.com/subscribe/post?u=9d67fc028348a0eb71318768e&id=6845ed3555).

Si vous avez des questions ou des commentaires, faites-le moi savoir dans les commentaires ci-dessous.