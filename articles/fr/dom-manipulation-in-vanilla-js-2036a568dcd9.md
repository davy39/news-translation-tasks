---
title: Comment manipuler le DOM en Vanilla JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-12T07:44:07.000Z'
originalURL: https://freecodecamp.org/news/dom-manipulation-in-vanilla-js-2036a568dcd9
coverImage: https://cdn-media-1.freecodecamp.org/images/1*G7VizI4PMgWNbR6rRV28Rw.png
tags:
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Comment manipuler le DOM en Vanilla JavaScript
seo_desc: 'By carlos da costa

  So you have learned variables, selection structures, and loops. Now it is time to
  learn about DOM manipulation and to start doing some cool JavaScript projects.

  In this tutorial, we will learn how to manipulate the DOM with vanilla...'
---

Par carlos da costa

Vous avez donc appris les variables, les structures de sélection et les boucles. Il est maintenant temps d'apprendre la manipulation du DOM et de commencer à réaliser des projets JavaScript cool.

Dans ce tutoriel, nous allons apprendre comment manipuler le DOM avec du JavaScript vanilla. Sans plus attendre, plongeons directement dans le sujet.

### 1. D'abord les bases

Avant de nous lancer dans le codage, apprenons ce qu'est vraiment le DOM :

> Le Document Object Model (DOM) est une interface de programmation pour les documents HTML et XML. Il représente la page de sorte que les programmes peuvent changer la structure, le style et le contenu du document. Le DOM représente le document sous forme de nœuds et d'objets. Ainsi, les langages de programmation peuvent se connecter à la page. [Source](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction)

En gros, lorsqu'un navigateur charge une page, il crée un modèle objet de cette page et l'affiche à l'écran. Le modèle objet est représenté dans une structure de données en arbre, chaque nœud est un objet avec des propriétés et des méthodes, et le nœud le plus haut est l'objet document.

Un langage de programmation peut être utilisé pour accéder et modifier ce modèle objet, et cette action est appelée manipulation du DOM. Et nous allons le faire avec JavaScript parce que JS est génial.

### 2. Le tutoriel proprement dit

Pour le tutoriel, nous allons avoir besoin de deux fichiers, un index.html, et l'autre manipulation.js.

```html
<!-- Fichier Index.html -->
<html>  
  <head>    
    <title>Manipulation du DOM</title>  
  </head>  

  <body>     
    <div id="division">
      <h1 id="head">
        <em>DOM<em> manipulation
      </h1>      

      <p class="text" id="middle">Tutoriel</p>
      <p>Frère</p>      
      <p class="text">Tutoriel Medium</p>    
    </div>    

    <p class="text">En dehors de la div</p>    

    <!-- Ensuite, nous appelons le fichier javascript -->
    <script src="manipulation.js"></script>  
  </body>
</html>

```

Voici donc notre fichier HTML, et comme vous pouvez le voir, nous avons une div avec l'id division. À l'intérieur de celle-ci, nous avons un élément h1, et sur la même ligne, vous comprendrez pourquoi plus tard, nous avons deux éléments p et la balise de fermeture de la div. Enfin, nous avons un élément p avec une classe de texte.

#### 2.1. Accéder aux éléments

Nous pouvons accéder à un seul élément ou à plusieurs éléments.

#### 2.1.1. Accéder à un seul élément

Pour accéder à un seul élément, nous allons examiner deux méthodes : getElementByID et querySelector.

```html
// la méthode ci-dessous sélectionne l'élément avec l'id head

let id = document.getElementById('head');
```

```html
// Le code ci-dessous sélectionne le premier élément p à l'intérieur de la première div

let q = document.querySelector('div p');

```

```html
/* Code supplémentaire */

// Cela change la couleur en rouge
id.style.color = 'red';

// Donne une taille de police de 30px
q.style.fontSize = '30px';

```

Nous avons maintenant accédé à deux éléments, l'élément h1 avec l'id **head** et le premier élément **p** à l'intérieur de la div.

**getElementById** prend comme argument un id, et **querySelector** prend comme argument un sélecteur CSS et retourne le premier élément qui correspond au sélecteur. Comme vous pouvez le voir, j'ai assigné le résultat des méthodes dans des variables, puis j'ai ajouté un peu de style à la fin.

#### 2.1.2. Accéder à plusieurs éléments

Lors de l'accès à plusieurs éléments, une liste de nœuds est retournée. Ce n'est pas un tableau mais cela fonctionne comme un. Vous pouvez donc parcourir la liste et utiliser la propriété length pour obtenir la taille de la liste de nœuds. Si vous voulez obtenir un élément spécifique, vous pouvez utiliser la notation de tableau ou la méthode item. Vous les verrez dans le code.

Pour accéder à plusieurs éléments, nous allons utiliser trois méthodes : getElementsByClassName, getElementsByTagName et querySelectorAll.

```html
// obtient chaque élément avec la classe text

let className = document.getElementsByClassName('text');
```

```html
// imprime la liste de nœuds

console.log(className);
```

```html
/* imprime le troisième élément de la liste de nœuds en utilisant la notation de tableau */

console.log(className[2]);
```

```html
/* imprime le troisième élément de la liste de nœuds en utilisant la fonction item */

console.log(className.item(2));
```

```html
let tagName = document.getElementsByTagName('p');
let selector = document.querySelectorAll('div p');
```

Le code semble être auto-explicatif, mais je vais l'expliquer quand même parce que je suis un type sympa. :)

Tout d'abord, nous utilisons **getElementsByClassName** qui prend un nom de classe comme argument. Il retourne une liste de nœuds avec chaque élément qui a **text** comme classe. Ensuite, nous imprimons la liste de nœuds sur la console. Nous imprimons également le troisième élément de la liste en utilisant la **notation de tableau** et la **méthode item**.

Ensuite, nous sélectionnons chaque élément **p** en utilisant la méthode getElementsByTagName qui prend un nom de balise comme argument et retourne une liste de nœuds de cet élément.

Enfin, nous utilisons la méthode **querySelectorAll**, qui prend comme argument un sélecteur CSS. Dans ce cas, il prend **div p** donc il retournera une liste de nœuds d'éléments **p** à l'intérieur d'une div.

En tant qu'exercice pratique, imprimez tous les éléments des listes de nœuds **tagName** et **selector** et découvrez leur taille.

#### 2.2. Parcourir le DOM

Jusqu'à présent, nous avons trouvé un moyen d'accéder à des éléments spécifiques. Que faire si nous voulons accéder à un élément à côté d'un élément auquel nous avons déjà accédé, ou accéder au nœud parent d'un élément précédemment accédé ? Les propriétés **firstChild, lastChild, parentNode, nextSibling** et **previousSibling** peuvent faire ce travail pour nous.

**firstChild** est utilisé pour obtenir le premier élément enfant d'un nœud. **lastChild**, comme vous l'avez deviné, obtient le dernier élément enfant d'un nœud. **parentNode** est utilisé pour accéder à un nœud parent d'un élément. **nextSibling** obtient pour nous l'élément suivant l'élément déjà accédé, et **previousSibling** obtient pour nous l'élément précédent l'élément déjà accédé.

```html
// Obtient le premier enfant de l'élément avec l'id division
let fChild = document.getElementById('division').firstChild;

// Affiche le premier enfant dans la console
console.log(fChild);

```

```html
// Obtient le dernier élément de l'élément avec l'id division
let lChild = document.querySelector('#division').lastChild;

```

```html
// Obtient le nœud parent de l'élément avec l'id division
let parent = document.querySelector('#division').parentNode;

// Affiche le nœud parent dans la console
console.log(parent);

```

```html
// Sélectionne l'élément avec l'id middle
let middle = document.getElementById('middle');

// Affiche dans la console le frère suivant de middle
console.log(middle.nextSibling);

```

Le code ci-dessus obtient d'abord l'élément **firstChild** de l'élément avec l'id division, puis l'affiche dans la console. Ensuite, il obtient l'élément **lastChild** du même élément avec l'id division. Ensuite, il obtient le **parentNode** de l'élément avec l'id division et l'affiche dans la console. Enfin, il sélectionne l'élément avec l'id middle et affiche son nœud **nextSibling**.

La plupart des navigateurs traitent les espaces blancs entre les éléments comme des nœuds de texte, ce qui fait que ces propriétés fonctionnent différemment dans différents navigateurs.

#### 2.3. Obtenir et mettre à jour le contenu des éléments

**2.3.1. Définir et obtenir le contenu textuel**

Nous pouvons obtenir ou définir le contenu textuel des éléments. Pour accomplir cette tâche, nous allons utiliser deux propriétés : **nodeValue** et **textContent**.

**nodeValue** est utilisé pour définir ou obtenir le contenu textuel d'un nœud de texte. **textContent** est utilisé pour définir ou obtenir le texte d'un élément contenant.

```html
// Obtenir le texte avec nodeValue
let nodeValue = document.getElementById('middle').firstChild.nodeValue;

// Afficher la valeur dans la console
console.log(nodeValue);

```

```html
// Définir le texte avec nodeValue
document.getElementById('middle').firstChild.nodeValue = "texte nodeValue";

```

```html
// Obtenir le texte avec textContent
let textContent = document.querySelectorAll('.text')[1].textContent;

// Afficher le textContent dans la console
console.log(textContent);

```

```
// Définir le texte avec textContent
document.querySelectorAll('.text')[1].textContent = 'nouveau textContent défini';

```

Avez-vous remarqué la différence entre **nodeValue** et **textContent** ?

Si vous regardez attentivement le code ci-dessus, vous verrez que pour obtenir ou définir le texte avec **nodeValue**, nous avons d'abord dû sélectionner le nœud de texte. Tout d'abord, nous avons obtenu l'élément avec l'id **middle**, puis nous avons obtenu son **firstChild** qui est le nœud de texte, puis nous avons obtenu le **nodeValue** qui a retourné le mot Tutoriel.

Maintenant avec **textContent**, il n'est pas nécessaire de sélectionner le nœud de texte, nous avons simplement obtenu l'élément puis nous avons obtenu son **textContent**, soit pour définir ou obtenir le texte.

**2.3.2. Ajouter et supprimer du contenu HTML**

Vous pouvez ajouter et supprimer du contenu HTML dans le DOM. Pour cela, nous allons examiner trois méthodes et une propriété.

Commençons par la propriété **innerHTML** car c'est le moyen le plus simple d'ajouter et de supprimer du contenu HTML. **innerHTML** peut être utilisé pour obtenir ou définir du contenu HTML. Mais soyez prudent lorsque vous utilisez innerHTML pour définir du contenu HTML, car il supprime le contenu HTML qui se trouve à l'intérieur de l'élément et ajoute le nouveau.

```html
// Définir innerHTML de l'élément avec l'id 'division'
document.getElementById('division').innerHTML =
`<ul>
  <li>Angular</li>
  <li>Vue</li>
  <li>React</li>
</ul>`;

```

Si vous exécutez le code, vous remarquerez que tout le reste dans la div avec l'id division disparaîtra, et la liste sera ajoutée.

Nous pouvons utiliser les méthodes : **createElement()**, **createTextNode()**, et **appendChild()** pour résoudre ce problème.

createElement est utilisé pour créer un nouvel élément HTML, createTextNode est utilisé pour créer un nœud de texte, et appendChild est utilisé pour ajouter un nouvel élément dans un élément parent.

```html
// Tout d'abord, nous créons un nouvel élément p en utilisant createElement
let newElement = document.createElement('p');

/* Ensuite, nous créons un nouveau nœud de texte et 
ajoutons le nœud de texte à l'élément créé */
let text = document.createTextNode('Texte ajouté !');
newElement.appendChild(text);

```

```html
/* Ensuite, nous ajoutons le nouvel élément avec le nœud de texte 
dans la div avec l'id division. */
document.getElementById('division').appendChild(newElement);

```

Il existe également une méthode appelée **removeChild** utilisée pour supprimer des éléments HTML.

```html
// Tout d'abord, nous obtenons l'élément que nous voulons supprimer
let toBeRemoved = document.getElementById('head');

// Ensuite, nous obtenons le nœud parent, en utilisant la propriété parentNode
let parent = toBeRemoved.parentNode;

/* Ensuite, nous utilisons la méthode removeChild, avec 
l'élément à supprimer comme paramètre. */
parent.removeChild(toBeRemoved);

```

Nous obtenons d'abord l'élément que nous voulons supprimer, puis nous obtenons son nœud parent. Ensuite, nous appelons la méthode removeChild pour supprimer l'élément.

#### 2.4. Nœud d'attribut

Maintenant que nous savons comment gérer les éléments, apprenons à gérer les attributs de ces éléments. Il existe certaines méthodes comme **GetAttribute**, **setAttribute**, **hasAttribute**, **removeAttribute**, et certaines propriétés comme **className** et **id**.

**getAttribute**, comme son nom peut le suggérer, est utilisé pour obtenir un attribut. Comme le nom de la classe, le nom de l'id, le href d'un lien ou tout autre attribut HTML.

**setAttribute** est utilisé pour définir un nouvel attribut à un élément. Il prend deux arguments, d'abord l'attribut et ensuite le nom de l'attribut.

**hasAttribute** est utilisé pour vérifier si un attribut existe, prend un attribut comme argument.

**removeAttribute** est utilisé pour supprimer un attribut, il prend un attribut comme argument.

**Id** cette propriété est utilisée pour définir ou obtenir l'id d'un élément.

**ClassName** est utilisé pour définir ou obtenir la classe d'un élément.

```html
// Sélectionne la première div
let d = document.querySelector('div');

// Vérifie si elle a un attribut id, retourne vrai/faux
console.log('vérifie id: '+d.hasAttribute('id'));

// Définit un nouvel attribut de classe
d.setAttribute('class','newClass');

// Retourne le nom de la classe
console.log(d.className);

```

Je sais que je suis un bon gars, mais ce code est simplement auto-explicatif.

### Conclusion

C'est tout ! Nous avons appris tant de concepts, mais il y a encore plus à apprendre sur la manipulation du DOM. Ce que nous avons couvert ici vous donne une bonne base.

Allez-y et pratiquez, et créez quelque chose de nouveau pour cimenter cette nouvelle connaissance.

Bonne journée, bon codage.