---
title: Le guide de manipulation du DOM JavaScript
subtitle: ''
author: Benjamin Semah
co_authors: []
series: null
date: '2024-01-10T15:12:57.000Z'
originalURL: https://freecodecamp.org/news/the-javascript-dom-manipulation-handbook
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/The-JavaScript-DOM-Manipulation-Handbook-Cover.png
tags:
- name: DOM
  slug: dom
- name: Front-end Development
  slug: front-end-development
- name: handbook
  slug: handbook
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: Le guide de manipulation du DOM JavaScript
seo_desc: 'DOM Manipulation is one of the most exciting topics to learn about in JavaScript.
  This is because one of JavaScript''s main uses is to make web pages interactive
  – and the Document Object Model (DOM) plays a major role in this.

  The DOM is a powerful t...'
---

La manipulation du DOM est l'un des sujets les plus passionnants à apprendre en JavaScript. Cela est dû au fait que l'une des principales utilisations de JavaScript est de rendre les pages web interactives – et le Document Object Model (DOM) joue un rôle majeur dans cela.

Le DOM est un outil puissant qui vous permet d'interagir avec et de manipuler les éléments d'une page web. Et ce guide vous aidera à comprendre et à devenir confiant dans le travail avec celui-ci.

Vous commencerez par apprendre ce qu'est le DOM et ce que vous pouvez faire avec lui. Ensuite, nous plongerons dans la façon de sélectionner, modifier et styliser les éléments du DOM. Vous apprendrez également à créer de nouveaux éléments et à les ajouter à votre page web.

Le guide couvre également des sujets comme la façon de parcourir le DOM, ce que sont les événements du DOM, et inclut quelques idées de projets pour la pratique.

Commençons !

## Table des matières

* [Qu'est-ce que le DOM ?](#quest-ce-que-le-dom)
    
    * [Ce que vous pouvez faire avec le DOM](#ce-que-vous-pouvez-faire-avec-le-dom)
        
* [Comment sélectionner les éléments du DOM](#comment-selectionner-les-elements-du-dom)
    
    * [getElementById](#1-getelementbyid)
        
    * [getElementsByClassName](#2-getelementsbyclassname)
        
    * [getElementsByTagName](#3-getelementsbytagname)
        
    * [querySelector](#4-queryselector)
        
    * [querySelectorAll](#5-queryselectorall)
        
* [Comment changer le contenu des éléments du DOM](#comment-changer-le-contenu-des-elements-du-dom)
    
    * [La propriété innerHTML](#la-propriete-innerhtml)
        
    * [Risques de sécurité avec innerHTML](#risques-de-securite-avec-innerhtml)
        
    * [Les propriétés innerText et textContent](#les-proprietes-innertext-et-textcontent)
        
* [Comment travailler avec les attributs des éléments du DOM](#comment-travailler-avec-les-attributs-des-elements-du-dom)
    
    * [La méthode getAttribute](#la-methode-getattribute)
        
    * [La méthode setAttribute](#la-methode-setattribute)
        
    * [La méthode removeAttribute](#la-methode-removeattribute)
        
    * [La méthode hasAttribute](#la-methode-hasattribute)
        
* [Comment changer les styles des éléments du DOM](#comment-changer-les-styles-des-elements-du-dom)
    
    * [Définir les styles avec la propriété .style](#definir-les-styles-avec-la-propriete-style)
        
    * [Définir les styles avec des classes](#definir-les-styles-avec-des-classes)
        
* [Comment parcourir le DOM](#comment-parcourir-le-dom)
    
    * [Différence entre un nœud et un élément](#difference-entre-un-noeud-et-un-element)
        
    * [Sélectionner un parent avec parentNode vs parentElement](#selectionner-un-parent-avec-parentnode-vs-parentelement)
        
    * [Sélectionner des éléments avec childNodes vs children](#selectionner-des-elements-avec-childnodes-vs-children)
        
    * [Sélectionner le premier ou le dernier enfant/élément](#selectionner-le-premier-ou-le-dernier-enfant-element)
        
    * [Sélectionner un frère de nœuds dans le DOM](#selectionner-un-fere-de-noeuds-dans-le-dom)
        
* [Événements du DOM et écouteurs d'événements](#evenements-du-dom-et-ecouteurs-devenements)
    
    * [Différence entre l'écouteur d'événements et le gestionnaire d'événements](#difference-entre-lecouteur-devenements-et-le-gestionnaire-devenements)
        
    * [Trois façons d'enregistrer des événements en JavaScript](#trois-facons-denregistrer-des-evenements-en-javascript)
        
    * [Défi pratique](#defi-pratique)
        
    * [Solution au défi pratique](#solution-au-defi-pratique)
        
    * [L'objet événement](#lobjet-evenement)
        
    * [Types d'événements](#types-devenements)
        
* [Flux d'événements en JavaScript](#flux-devenements-en-javascript)
    
    * [Propagation d'événements](#propagation-devenements)
        
    * [Capture d'événements](#capture-devenements)
        
    * [La méthode stopPropagation de l'événement](#la-methode-stoppropagation-de-levenement)
        
* [Idées de projets de manipulation du DOM JS](#idees-de-projets-de-manipulation-du-dom-js)
    
* [Conclusion](#conclusion)
    

## Qu'est-ce que le DOM ?

DOM signifie Document Object Model. Mais que signifie cela ? Décomposons-le.

La partie **Document** fait référence à la page web que vous voyez dans le navigateur. Plus précisément, le document HTML qui gère la structure du contenu de la page. Cela inclut le texte, les images, les liens et autres éléments qui composent la page.

**Object** signifie que les éléments comme les images, les en-têtes et les paragraphes sont traités comme des objets. Chaque objet a ses propriétés (comme id, class, style) et méthodes. En utilisant ces propriétés et méthodes, vous pouvez manipuler les éléments.

Le **Model** dans DOM signifie qu'il s'agit d'une représentation ou d'une copie du document HTML sous forme d'arbre hiérarchique. Cet arbre inclut tous les éléments. Et il capture les relations parent-enfant entre eux.

Le DOM est toujours identique au document HTML. Les navigateurs s'assurent qu'ils sont synchronisés. Donc, si quelque chose change dans le HTML, le DOM change aussi, et vice versa.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/JavaScript--2-.png align="left")

*Une représentation graphique de l'arbre DOM HTML*

En haut de la hiérarchie se trouve l'objet Document. Il n'a qu'un seul enfant – l'élément `html`. L'élément `html`, également connu sous le nom d'élément racine, a deux enfants, les éléments `head` et `body`. Et chacun d'eux a aussi ses propres enfants.

La relation parent-enfant entre les éléments est ce qui vous permet de parcourir ou de vous déplacer entre eux et de les sélectionner. Plus sur cela plus tard.

### Ce que vous pouvez faire avec le DOM

La manipulation du DOM permet aux développeurs d'interagir avec la structure, le style et le contenu des pages web. Voici quelques-unes des choses que vous pouvez faire avec le DOM :

* Changer et supprimer des éléments existants dans le DOM.
    
* Créer et ajouter de nouveaux éléments à la page.
    
* Changer les styles des éléments.
    
* Ajouter des écouteurs d'événements aux éléments pour les rendre interactifs.
    

## Comment sélectionner les éléments du DOM

Pour faire quelque chose avec les éléments du DOM, vous devez d'abord sélectionner ou accéder à l'élément en question. Dans cette section, vous apprendrez quelques méthodes courantes pour sélectionner les éléments du DOM.

Utilisons le balisage suivant pour montrer comment les différentes méthodes de sélection du DOM fonctionnent.

```html
  <h1 id="page-title">Répertoire téléphonique</h1>
  
  <p class="family">Marie</p>
  <p class="family">Jose</p>
  <p class="work">Anne</p>
  <p class="work">Joan</p>
```

Le balisage inclut un en-tête avec un id de `page-title` et quatre paragraphes. Les deux premiers paragraphes ont tous deux une classe de `family`, et les deux derniers ont une classe de `work`.

### 1\. getElementById

Vous utilisez cette méthode pour sélectionner des éléments avec un attribut id. Les id sont des identifiants uniques. Par exemple, si un élément d'en-tête a un attribut id avec une valeur de "page-title", aucun autre élément de la page ne doit également avoir un id avec la même valeur.

Cela signifie que chaque fois que vous utilisez la méthode `getElementById`, vous allez sélectionner un seul élément du DOM.

Regardons un exemple :

L'en-tête `h1` a une valeur d'id de `page-title`. Voici comment vous pouvez le sélectionner en utilisant la méthode `getElementById` :

```javascript
const titleElement = document.getElementById("page-title")
console.log(titleElement)
```

L'exemple sélectionne l'élément d'en-tête et l'assigne à la variable `titleElement`.

![Image](https://www.freecodecamp.org/news/content/images/2023/12/Screenshot-2023-12-02-at-9.01.01-AM.png align="left")

*Résultat de l'accès à l'élément avec la méthode getElementById.*

Si aucun élément dans le DOM n'a l'id donné, la méthode `getElementById()` retournera `null`.

### 2\. getElementsByClassName

Vous pouvez utiliser cette méthode pour sélectionner plus d'un objet. Cette méthode prend la valeur d'un attribut de classe comme argument et sélectionne tous les éléments dans le DOM qui ont la classe donnée. Contrairement aux id, vous pouvez donner la même valeur de classe à différents éléments HTML.

Voici un exemple :

```javascript
const famContacts = document.getElementsByClassName("family")
console.log(famContacts)
```

Cela retourne une collection HTML de tous les éléments avec la classe donnée. L'instruction de journalisation imprimera ce qui suit dans la console :

![Image](https://www.freecodecamp.org/news/content/images/2023/12/Screenshot-2023-12-01-at-10.35.51-AM.png align="left")

*La méthode* `getElementsByClassName()` retourne une collection HTML.

Note : La collection HTML ressemble à un tableau, mais ce n'en est pas un. Vous pouvez accéder aux éléments en utilisant la notation entre crochets comme vous le feriez avec un tableau – mais vous ne pouvez pas appliquer de méthodes de tableau comme `map`, `filter`, et `forEach` dessus.

```javascript
console.log(famContacts[0])
```

Cela obtiendra le premier élément de la collection HTML, qui est le paragraphe avec le nom Marie.

![Image](https://www.freecodecamp.org/news/content/images/2023/12/Screenshot-2023-12-02-at-9.03.35-AM-1.png align="left")

*Résultat de l'accès à l'élément HTMLCollection avec la notation entre crochets.*

Mais que faire si vous souhaitez parcourir tous les éléments de la collection HTML `famContacts` ? Vous devrez d'abord convertir la collection HTML en un tableau. Ensuite, vous pourrez utiliser l'une des méthodes de tableau.

Une façon simple de créer un tableau à partir de la collection HTML est d'utiliser l'opérateur de propagation, comme ceci :

```javascript
let famContactsArray = [...famContacts]

famContactsArray.forEach(element => console.log(element))
```

![Image](https://www.freecodecamp.org/news/content/images/2023/12/Screenshot-2023-12-02-at-9.06.48-AM.png align="left")

*Un résultat de la journalisation de tous les éléments dans la HTMLCollection.*

En utilisant la méthode `forEach`, vous pouvez accéder à chacun des éléments dans le `famContactsArray`. Le navigateur générera une erreur si vous essayez d'appliquer une méthode de tableau comme `map` à la collection HTML sans d'abord créer un tableau à partir de celle-ci.

![Image](https://www.freecodecamp.org/news/content/images/2023/12/Screenshot-2023-12-01-at-11.57.27-AM.png align="left")

*Message d'erreur lorsque vous utilisez des méthodes de tableau sur une HTMLCollection.*

### 3\. getElementsByTagName

Cette méthode sélectionnera les éléments en utilisant leur nom de balise. Par exemple, `getElementByTagName('p')` sélectionnera tous les paragraphes de la page.

Comme `getElementsByClassName`, cette méthode retourne également une collection HTML des éléments sélectionnés.

Voici un exemple :

```javascript
const allContacts = document.getElementsByTagName('p')
console.log(allContacts)
```

![Image](https://www.freecodecamp.org/news/content/images/2023/12/Screenshot-2023-12-02-at-8.39.36-AM.png align="left")

*Une HTMLCollection contenant tous les éléments de paragraphe.*

Vous pouvez créer un tableau à partir de la collection HTML et utiliser l'une des méthodes de tableau dessus.

```javascript
let allContactsArray = [...allContacts]

allContactsArray.map(element => console.log(element))
```

![Image](https://www.freecodecamp.org/news/content/images/2023/12/Screenshot-2023-12-02-at-9.08.26-AM.png align="left")

*Résultat de l'utilisation de la méthode map sur* `allContactsArray`.

### 4\. querySelector

Vous pouvez utiliser cette méthode pour sélectionner n'importe quel élément HTML dans le DOM. Elle retourne seulement un élément : le premier élément qui correspond au sélecteur donné.

La méthode `querySelector` fonctionne comme les sélecteurs CSS.

Par exemple, que faites-vous lorsque vous voulez sélectionner un élément avec un id ? Vous utilisez le symbole dièse `#`. Et si vous voulez sélectionner des éléments avec une classe ? Vous mettez un point `.` devant le nom de la classe.

Voici un exemple :

```javascript
const firstWorkContact = document.querySelector('.work')
console.log(firstWorkContact)
```

![Image](https://www.freecodecamp.org/news/content/images/2023/12/Screenshot-2023-12-02-at-11.38.12-AM.png align="left")

*Un exemple d'utilisation de la méthode* `querySelector`.

L'exemple ci-dessus retourne seulement le premier élément avec une classe de `work` et ignore le reste.

Voyons un autre exemple pour montrer comment querySelector fonctionne comme les sélecteurs CSS. Le suivant est un élément `div` avec quatre boutons :

```html
<div>
    <button>Premier bouton</button>
    <button>Deuxième bouton</button>
    <button>Troisième bouton</button>
    <button>Quatrième bouton</button>
</div>
```

En supposant que vous vouliez sélectionner le troisième bouton, vous pourriez utiliser `querySelector` comme celui ci-dessous. Le code utilise le sélecteur CSS `nth-child` pour obtenir le troisième bouton à l'intérieur de la div.

```javascript
const thirdBtn = document.querySelector('div button:nth-child(3)')
console.log(thirdBtn)
```

![Image](https://www.freecodecamp.org/news/content/images/2023/12/Screenshot-2023-12-02-at-2.42.48-PM.png align="left")

*Résultat de la sélection du troisième bouton avec la méthode* `querySelector`.

Mais que faire si vous voulez sélectionner les quatre éléments de bouton et pas seulement le premier ? Alors vous pourriez utiliser la méthode `querySelectorAll` à la place.

### 5\. querySelectorAll

Comme la méthode `querySelector`, `querySelectorAll` sélectionne également les éléments HTML en utilisant les sélecteurs CSS. La différence est qu'elle retourne tous les éléments qui correspondent au sélecteur au lieu de retourner seulement le premier.

En utilisant l'exemple précédent, sélectionnons tous les boutons avec `querySelectorAll`.

```javascript
const allBtns = document.querySelectorAll('button')
console.log(allBtns)
```

![Image](https://www.freecodecamp.org/news/content/images/2023/12/Screenshot-2023-12-02-at-3.04.18-PM.png align="left")

*La méthode* `querySelectorAll` retourne une NodeList des éléments sélectionnés.

Note : `querySelectorAll` retourne une `NodeList`. Une `NodeList` est légèrement différente d'une collection HTML. Vous n'avez pas besoin de la convertir en tableau pour appliquer une méthode comme `forEach` dessus.

```javascript
allBtns.forEach(btn => console.log(btn))
```

![Image](https://www.freecodecamp.org/news/content/images/2023/12/Screenshot-2023-12-02-at-3.00.19-PM.png align="left")

*Résultat de l'utilisation de la méthode* `forEach` sur la NodeList.

Mais vous ne pouvez toujours pas appliquer des méthodes de tableau comme `map`, `filter`, et autres sur une NodeList. Vous devrez d'abord créer un tableau à partir de celle-ci.

Vous pouvez lire cet [article freeCodeCamp sur la différence entre HTML collection et NodeList](https://www.freecodecamp.org/news/dom-manipulation-htmlcollection-vs-nodelist/) pour en savoir plus.

## Comment changer le contenu des éléments du DOM

Jusqu'à présent, vous avez appris différentes façons de sélectionner les éléments du DOM. Mais ce n'est que le début. Maintenant, voyons comment vous pouvez manipuler le DOM pour changer le contenu d'une page web.

La première chose que vous devez faire est de sélectionner l'élément. Vous pouvez le faire en utilisant l'une des méthodes que vous avez apprises dans la section précédente.

Après avoir sélectionné l'élément, il existe plusieurs méthodes que vous pouvez utiliser pour ajouter ou mettre à jour le contenu.

### La propriété `innerHTML`

Il s'agit d'une méthode qui vous permet de lire ou de mettre à jour à la fois la structure et le contenu des éléments. Voyons un exemple de la façon dont vous pouvez utiliser la méthode `innerHTML`.

Voici un balisage de trois paragraphes, chacun avec un id.

```html
  <p id="topic">Méthodes de tableau JS</p>
  <p id="first-method">map</p>
  <p id="second-method">filter</p>
```

![Image](https://www.freecodecamp.org/news/content/images/2023/12/Screenshot-2023-12-03-at-8.17.55-AM.png align="left")

*Balisage simple avec trois éléments de paragraphe*

Vous pouvez lire ou obtenir le contenu de l'un des paragraphes en utilisant `innerHTML`. Par exemple, obtenons le contenu du premier paragraphe.

```javascript
const topicElement = document.querySelector('#topic')
console.log(topicElement.innerHTML)
```

![Image](https://www.freecodecamp.org/news/content/images/2023/12/Screenshot-2023-12-03-at-8.10.36-AM.png align="left")

*Instruction de journalisation du* `innerHTML` de l'élément `topicElement`

Maintenant, disons que vous voulez mettre à jour le sujet de "Méthodes de tableau JS" à "Méthodes de tableau JavaScript". Vous pouvez le faire en assignant le nouveau texte à l'`innerHTML` de l'élément.

```javascript
const topicElement = document.querySelector('#topic')
topicElement.innerHTML = "Méthodes de tableau JavaScript"
```

![Image](https://www.freecodecamp.org/news/content/images/2023/12/Screenshot-2023-12-03-at-8.16.59-AM-1.png align="left")

*Le sujet est mis à jour de "Méthodes de tableau JS" à "Méthodes de tableau JavaScript"*

Avec `innerHTML`, vous pouvez changer plus que le contenu. Vous pouvez également changer la structure HTML de l'élément. Par exemple, si vous voulez mettre le mot "JavaScript" en gras, vous pourriez faire ceci :

```javascript
topicElement.innerHTML = "<b>JavaScript</b> méthodes de tableau"
```

![Image](https://www.freecodecamp.org/news/content/images/2023/12/Screenshot-2023-12-03-at-8.27.45-AM.png align="left")

*Le mot "JavaScript" est mis en gras en utilisant innerHTML*

### Risques de sécurité avec `innerHTML`

L'utilisation de `innerHTML` présente des risques potentiels pour la sécurité. Un exemple est les [attaques par script inter-sites (XSS)](https://www.freecodecamp.org/news/cross-site-scripting-what-is-xss/).

Si le contenu que vous insérez provient d'une entrée utilisateur ou de toute source non fiable, assurez-vous de le valider et de le nettoyer avant d'utiliser `innerHTML` pour prévenir les attaques XSS. Vous pouvez utiliser une bibliothèque comme [DOMPurify](https://www.npmjs.com/package/dompurify) pour cela.

De plus, si vous travaillez avec du contenu texte brut, envisagez d'utiliser des méthodes comme `innerText` et `textContent`.

### Les propriétés `innerText` et `textContent`

`innerText` et `textContent` ignorent les balises HTML et les traitent comme faisant partie d'une chaîne. Vous pouvez utiliser les deux méthodes pour lire ou mettre à jour le texte des éléments du DOM.

Une différence clé entre les deux réside dans la manière dont elles traitent le texte. L'utilisation de `innerText` retourne le texte tel qu'il apparaît à l'écran. Et l'utilisation de `textContent` retourne le texte tel qu'il apparaît dans le balisage. Voyons un exemple ci-dessous.

```html
<p>Clé =<span style="display: none;">     ABC123<span></p>
```

![Image](https://www.freecodecamp.org/news/content/images/2023/12/Screenshot-2023-12-03-at-10.03.41-AM.png align="left")

*Un élément de paragraphe avec du texte et un élément span caché à l'intérieur*

L'exemple inclut un élément de paragraphe. À l'intérieur du paragraphe se trouve un span qui contient une clé. La clé n'apparaît pas à l'écran car son style en ligne est défini sur un affichage de none.

Maintenant, sélectionnons le paragraphe et imprimons à la fois la valeur `innerText` et la valeur `textContent` pour voir la différence.

```javascript
const paragraph = document.querySelector('p');

console.log("innerText: ", paragraph.innerText)
console.log("textContent: ", paragraph.textContent)
```

![Image](https://www.freecodecamp.org/news/content/images/2023/12/Screenshot-2023-12-03-at-10.06.11-AM.png align="left")

*Résultat de l'instruction de journalisation pour* `innerText` et `textContent`.

Remarquez comment `innerText` retourne le texte tel qu'il apparaît à l'écran (sans la valeur de la clé qui est cachée avec CSS). Et remarquez comment `textContent` retourne le texte y compris les éléments cachés et les espaces blancs.

Voyons un autre exemple pour ajouter du texte à un élément. Le code suivant inclut deux paragraphes, chacun avec du texte en gras et un span vide, ainsi qu'une ligne horizontale entre eux.

```html
  <p>
    <b>Exemple innerText</b>
    <span id="inner-text"></span>
  </p>
  
  <hr>	
 
  <p>
    <b>Exemple textContent</b>
    <span id="textContent"></span>
  </p>
```

![Image](https://www.freecodecamp.org/news/content/images/2023/12/Screenshot-2023-12-03-at-10.48.11-AM.png align="left")

*Exemple pour démontrer les propriétés* `innerText` et `textContent`

Maintenant, sélectionnons les deux éléments span et ajoutons-leur le même texte. Cela vous aidera à mieux comprendre la différence entre `innerText` et `textContent`.

```javascript
const example1 = document.querySelector('#inner-text');
const example2 = document.querySelector('#text-content');

let address = `
  Rue ABC,
  Route de Spintex,
  Accra,
  Ghana.
`;

example1.innerText = address;
example2.textContent = address;
```

Le code donne la même variable `address` aux deux exemples. Le premier utilise `innerText` et le second utilise `textContent`. Voir les résultats ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2023/12/Screenshot-2023-12-03-at-10.46.46-AM.png align="left")

*Résultat de la mise à jour du contenu avec* `innerText` et `textContent`.

Remarquez comment `innerText` utilise les sauts de ligne mais pas l'exemple `textContent`.

Une autre différence clé entre les deux méthodes est leur comportement lorsqu'elles sont utilisées à l'intérieur de boucles. `innerText` peut être plus lent que `textContent` lorsqu'il s'agit d'opérations en masse ou de mises à jour fréquentes dans une boucle.

[Lisez cet article freeCodeCamp](https://www.freecodecamp.org/news/innerhtml-vs-innertext-vs-textcontent/) pour en savoir plus sur la différence entre `innerHTML`, `innerText`, et `textContent`.

## Comment travailler avec les attributs des éléments du DOM

Les [attributs HTML](https://www.freecodecamp.org/news/html-attributes-explained/) fournissent des informations utiles sur les éléments HTML. Ces attributs sont toujours inclus dans la balise d'ouverture de l'élément. Un attribut est composé d'un nom et d'une valeur (bien qu'il existe des exceptions où seul un nom est présent).

Lorsque le navigateur génère le DOM en fonction de la structure HTML, il traduit ces attributs en propriétés dynamiques des objets DOM.

Voici un exemple :

Supposons qu'il y ait un bouton dans le document HTML avec les attributs suivants :

```html
<button id="myBtn" type="submit">Cliquez ici</button>
```

Pour cet exemple, le navigateur créera un objet `HTMLButtonElement` dans le DOM. Et l'objet aura des propriétés correspondant aux attributs.

* `HTMLButtonElement.id` avec une valeur de `myBtn`.
    
* `HTMLButtonElement.type` avec une valeur de `submit`.
    

Pour interagir avec et manipuler ces attributs en utilisant JavaScript, vous pouvez utiliser des méthodes comme `getAttribute` et `setAttribute` pour accéder directement aux propriétés.

### La méthode `getAttribute`

Comme le suggère le nom, vous pouvez utiliser cette méthode pour obtenir la valeur d'un attribut existant sur un élément.

Elle accepte un argument (le nom de l'attribut) et retourne la valeur de l'attribut. Si l'attribut que vous lui avez passé en argument n'existe pas sur l'élément, la méthode retournera `null`.

Voici un exemple :

```html
<img src="image.jpg" alt="Une image d'exemple">
```

```javascript
const imageElement = document.querySelector('img')
console.log(imageElement.getAttribute('src'))
```

![Image](https://www.freecodecamp.org/news/content/images/2023/12/Screenshot-2023-12-09-at-9.00.25-AM.png align="left")

*La méthode* `getAttribute` est utilisée pour obtenir la valeur de l'attribut `src`.

En utilisant la méthode `getAttribute` dans l'exemple ci-dessus, vous pouvez obtenir la valeur de l'attribut `src` pour l'élément image.

### La méthode `setAttribute`

Celle-ci est utilisée pour définir ou changer l'attribut d'un élément. La méthode prend deux arguments. Le premier argument est le nom de l'attribut que vous souhaitez changer, et le second est la nouvelle valeur que vous souhaitez donner à l'attribut.

Voici un exemple :

```html
<img src="image.jpg" alt="Une image d'exemple">
```

```javascript
const imageElement = document.querySelector('img')

console.log("AVANT :", imageElement.getAttribute('src'))
imageElement.setAttribute('src', 'new-image.jpg')
console.log("APRÈS :", imageElement.getAttribute('src'))
```

![Image](https://www.freecodecamp.org/news/content/images/2023/12/Screenshot-2023-12-09-at-9.27.14-AM.png align="left")

*La méthode* `setAttribute` est utilisée pour mettre à jour la valeur de l'attribut `src`.

Ce code exemple journalise la valeur de l'attribut `src` avant et après l'utilisation de `setAttribute` pour la changer de `image.jpg` à `new-image.jpg`.

Lorsque vous passez un argument à la méthode `setAttribute` et que cet attribut n'existe pas sur l'élément, il créera un nouvel attribut. Par exemple, vous pouvez ajouter une propriété de hauteur à l'élément image comme ceci :

```javascript
const imageElement = document.querySelector('img')

console.log("AVANT :", imageElement.getAttribute('height'))
imageElement.setAttribute('height', '200')
console.log("APRÈS :", imageElement.getAttribute('height'))
```

![Image](https://www.freecodecamp.org/news/content/images/2023/12/Screenshot-2023-12-09-at-9.32.53-AM.png align="left")

*Un exemple d'ajout d'un nouvel attribut de hauteur à l'élément image.*

La première instruction de journalisation retourne `null` car l'attribut de hauteur était inexistant. Mais après l'avoir défini avec la méthode `setAttribute`, la deuxième instruction de journalisation retourne la valeur correcte de la hauteur.

### La méthode `removeAttribute`

Dans la section précédente, vous avez appris à ajouter un nouvel attribut en utilisant la méthode `setAttribute`. Que faire si vous souhaitez supprimer un attribut existant ?

Vous pouvez utiliser la méthode `removeAttribute`. Vous passez le nom de l'attribut que vous souhaitez supprimer de l'élément comme argument à la méthode.

Voici un exemple :

```html
  <img src="image.jpg" alt="Une image d'exemple" height="200">
```

Utilisons la méthode `removeAttribute` pour supprimer l'attribut `height` de l'élément image.

```javascript
const imageElement = document.querySelector('img')

console.log("AVANT :", imageElement.getAttribute('height'))
imageElement.removeAttribute('height', '200')
console.log("APRÈS :", imageElement.getAttribute('height'))
```

![Image](https://www.freecodecamp.org/news/content/images/2023/12/Screenshot-2023-12-09-at-10.09.35-AM.png align="left")

*Un exemple d'utilisation de la méthode* `removeAttribute`.

Avant d'utiliser `removeAttribute`, la première instruction de journalisation imprime la valeur de l'attribut de hauteur, `200`. Mais après avoir utilisé la méthode `removeAttribute`, la deuxième instruction de journalisation imprime `null`, confirmant la suppression de l'attribut de hauteur de l'élément image.

### La méthode `hasAttribute`

Une autre méthode pour travailler avec les attributs dans le DOM est la méthode `hasAttribute`. Vous pouvez utiliser cette méthode pour vérifier si un élément possède un attribut spécifique ou non.

La méthode `hasAttribute` retourne `true` si l'attribut spécifié existe et retourne `false` s'il n'existe pas.

Voici un exemple :

```html
<img src="image.jpg" alt="Une image d'exemple" height="200">
```

Utilisons `hasAttribute` pour vérifier la présence des valeurs `height` et `width` sur l'élément image.

```javascript
const imageElement = document.querySelector('img')

console.log("HAUTEUR", imageElement.hasAttribute('height'))
console.log("LARGEUR", imageElement.hasAttribute('width'))
```

![Image](https://www.freecodecamp.org/news/content/images/2023/12/Screenshot-2023-12-09-at-10.20.53-AM.png align="left")

*Exemple d'utilisation de la méthode* `hasAttribute` pour vérifier si un attribut existe.

La vérification de la hauteur retourne `true` car il s'agit d'un attribut existant, tandis que la vérification de la largeur retourne `false` car il n'existe pas.

## Comment changer les styles des éléments du DOM

Il existe deux principales façons de styliser les éléments lors de la manipulation du DOM en JavaScript. Vous pouvez utiliser la propriété `.style` ou vous pouvez utiliser des classes. Chacune a ses avantages et ses situations où elle est la mieux adaptée.

### Définir les styles avec la propriété `.style`

Vous utilisez la propriété `.style` lorsque vous souhaitez apporter des modifications spécifiques à un seul élément. La propriété `.style` vous permet de définir des styles directement en tant que [styles en ligne](https://www.freecodecamp.org/news/inline-style-in-html/) pour les éléments. Cela signifie qu'elle remplace les styles que vous avez dans votre feuille de style CSS.

En utilisant la propriété `.style`, vous obtenez l'accès à toutes les propriétés CSS individuelles. Voir la démonstration ci-dessous :

```html
  <h1>Styliser les éléments avec JavaScript</h1>
```

```javascript
const header = document.querySelector('h1')
console.log(header.style)
```

![Image](https://www.freecodecamp.org/news/content/images/2023/12/ezgif.com-video-to-gif--8-.gif align="left")

*CSSStyleDeclarations pour un élément* `h1` journalisé dans la console.

Le `console.log` imprime les déclarations de style CSS avec toutes les propriétés CSS pour cet élément.

Maintenant, voyons un exemple de la façon d'utiliser la propriété `.style`.

```html
  <h1>J'aime JavaScript</h1>
```

![Image](https://www.freecodecamp.org/news/content/images/2023/12/Screenshot-2023-12-11-at-7.56.41-AM.png align="left")

*Un exemple d'élément d'en-tête* `h1`

Voici un en-tête `h1`. Maintenant, ajoutons du style en utilisant la propriété `.style`.

```javascript
const paragraph = document.querySelector('h1')

paragraph.style.color = 'white'
paragraph.style.backgroundColor = 'green'
```

![Image](https://www.freecodecamp.org/news/content/images/2023/12/Screenshot-2023-12-11-at-7.59.15-AM.png align="left")

*La propriété style est utilisée pour ajouter une couleur de fond à l'élément* `h1`.

NOTE : Comme il s'agit de JavaScript, vous ne pouvez pas utiliser le tiret si le nom de la propriété CSS inclut deux mots ou plus. Par exemple, en CSS, vous écririez `background-color`. Mais dans votre code JavaScript, vous devez utiliser la casse camel. Donc `background-color` devient `backgroundColor`.

Vous pouvez également supprimer un style sur un élément en définissant la valeur de la propriété sur une chaîne vide.

```javascript
element.style.propertyName = ""
```

### Définir les styles avec des classes

Avec les classes, vous pouvez créer des styles une fois et les appliquer à différents éléments. Cela aide à rendre votre code plus maintenable.

#### La propriété `className`

La propriété `className` représente l'attribut de classe d'un élément DOM. Et vous pouvez l'utiliser pour obtenir ou définir la valeur de l'attribut de classe.

Voici un exemple :

```html
<p class="food rice-dish">Riz Jollof</p>
```

```javascript
const jollofParagraph = document.querySelector('p')

console.log(jollofParagraph.className)

jollofParagraph.className = 'favorite'

console.log(jollofParagraph.className)
```

![Image](https://www.freecodecamp.org/news/content/images/2023/12/Screenshot-2023-12-11-at-9.13.37-AM.png align="left")

*Exemple de changement de la valeur d'une classe avec la propriété* `className`.

Le `className` lit ou remplace également la classe actuelle. Dans l'exemple ci-dessus, la première instruction de journalisation imprime la valeur originale de la classe. Et après la mise à jour du `className`, la deuxième instruction de journalisation imprime la nouvelle valeur de la classe.

Mais il existe une propriété plus flexible. Par exemple, que faire si, au lieu de remplacer l'ancienne classe par la nouvelle classe, vous souhaitiez ajouter une autre classe ? C'est là que la propriété `classList` entre en jeu.

#### La propriété `classList`

Avec la propriété `classList`, vous pouvez ajouter et supprimer des classes. Vous pouvez également basculer des classes, remplacer les valeurs de classe existantes par de nouvelles, et même vérifier si la classe contient une valeur spécifique.

Voici un exemple :

```html
<p class="food">Riz Jollof</p>
```

```javascript
const jollofParagraph = document.querySelector('p')
console.log(jollofParagraph.classList)
```

![Image](https://www.freecodecamp.org/news/content/images/2023/12/Screenshot-2023-12-11-at-9.43.30-AM.png align="left")

*Affiche la classList actuelle avec une seule valeur*

#### Ajout de classes avec `classList.add()`

```javascript
jollofParagraph.classList.add('fav', 'tasty')

console.log(jollofParagraph.classList)
```

![Image](https://www.freecodecamp.org/news/content/images/2023/12/Screenshot-2023-12-11-at-9.46.14-AM.png align="left")

*Exemple d'ajout de nouvelles classes avec* `classList.add`.

Le code ajoute deux nouvelles classes `fav` et `tasty` à la liste des classes.

#### Suppression de classes avec `classList.remove()`

```javascript
jollofParagraph.classList.remove('tasty')

console.log(jollofParagraph.classList)
```

![Image](https://www.freecodecamp.org/news/content/images/2023/12/Screenshot-2023-12-11-at-9.50.26-AM.png align="left")

*Exemple de suppression de classes avec* `classList.remove`.

Le code supprime la classe `tasty` de la liste des classes.

#### Remplacement de classes avec `classList.replace()`

```javascript
jollofParagraph.classList.replace('fav', 'favorite')

console.log(jollofParagraph.classList)
```

Le code remplace la classe `fav` par `favorite`

![Image](https://www.freecodecamp.org/news/content/images/2023/12/Screenshot-2023-12-11-at-9.53.30-AM.png align="left")

*Exemple de remplacement de classes avec* `classList.replace`.

#### Vérification de la présence d'une classe avec `classList.contains()`

```javascript
const isFavorite = jollofParagraph.classList.contains('favorite')
const isSoup = jollofParagraph.classList.contains('soup')

console.log("Contient favorite: ", isFavorite)
console.log("Contient soup: ", isSoup)
```

![Image](https://www.freecodecamp.org/news/content/images/2023/12/Screenshot-2023-12-11-at-10.09.53-AM.png align="left")

*Exemple de vérification de l'existence d'une classe avec* `classList.contains`.

Le code vérifie si la classe passée est contenue dans la liste des classes.

Il retourne `true` si elle est incluse dans la liste des classes (par exemple `favorite`) et `false` si elle n'est pas incluse dans la liste des classes (par exemple `soup`)

#### Basculer une classe avec `classList.toggle()`

Lorsque vous utilisez la propriété `toggle`, elle vérifie d'abord si la classe existe. Si elle existe, elle la supprimera. Et si elle n'existe pas, elle l'ajoutera.

```javascript
jollofParagraph.classList.toggle('favorite')
console.log(jollofParagraph.classList)

jollofParagraph.classList.toggle('favorite')
console.log(jollofParagraph.classList)

jollofParagraph.classList.toggle('favorite')
console.log(jollofParagraph.classList)
```

![Image](https://www.freecodecamp.org/news/content/images/2023/12/Screenshot-2023-12-11-at-10.19.18-AM.png align="left")

*Exemple de basculement d'une valeur de classe avec* `classList.toggle`.

La première fois que le basculement s'exécute, `favorite` existe dans la liste des classes. Donc, le basculement le supprime.

La deuxième fois que le basculement s'exécute, `favorite` n'existe pas, donc le basculement ajoute `favorite` à la liste des classes.

La fois suivante où le basculement s'exécute, `favorite` existe à nouveau. Donc, il le supprime de la liste des classes.

Le basculement continue d'ajouter ou de supprimer la valeur de la liste des classes en fonction de sa présence ou de son absence.

## Comment parcourir le DOM

Parcourir le DOM signifie se déplacer entre les différents éléments/nœuds au sein du document HTML. Cela peut inclure la sélection ou l'accès aux éléments ou nœuds parents, enfants ou frères. Vous faites cela pour obtenir des informations ou manipuler la structure du document.

Mais avant de nous plonger dans la façon de parcourir le DOM, vous devez comprendre la différence entre les nœuds et les éléments.

### Différence entre un nœud et un élément

Les nœuds sont les éléments de base du DOM. Ils représentent différents composants dans la structure HTML.

Les éléments sont un type spécifique de nœud, mais tous les nœuds ne sont pas des éléments. D'autres types de contenu comme les attributs des éléments, le contenu textuel et les commentaires dans le code sont également des nœuds. Mais ils ne sont pas des éléments.

Un élément est un type spécifique de nœud qui définit la structure du contenu du document. Pensez aux éléments comme aux balises HTML familières que vous utilisez. Les exemples incluent `<div>`, `<p>`, et `<ul>`. Chaque élément peut consister en des attributs, du contenu textuel et d'autres éléments imbriqués.

### Sélectionner un parent avec `parentNode` vs `parentElement`

Lorsque vous souhaitez sélectionner le parent d'un élément DOM, vous pouvez utiliser soit `parentNode` soit `parentElement`. Les deux vous permettront d'obtenir le parent de l'élément que vous leur passez.

D'un point de vue pratique, le parent d'un élément ou d'un nœud sera toujours un élément. Donc, peu importe celui que vous utilisez, vous obtiendrez le bon parent de l'élément sélectionné.

Voyons un exemple de sélection du parent d'un élément.

```html
  <div class="container">
    <p class="full-text">
        <i id="italics">Un texte en italique</i>
    </p>
  </div>
```

```json
const italicizedText = document.getElementById('italics')

console.log(italicizedText.parentNode)
console.log(italicizedText.parentNode.parentNode)
```

D'abord, vous sélectionnez l'élément. Ensuite, vous enchaînez la méthode `parentNode` pour obtenir le parent. Vous pouvez également enchaîner une autre propriété `parentNode` pour obtenir le parent d'un élément parent comme la deuxième instruction de journalisation.

La capture d'écran ci-dessous montre la sortie des deux instructions de journalisation.

![Image](https://www.freecodecamp.org/news/content/images/2023/12/Screenshot-2023-12-12-at-9.44.45-AM.png align="left")

*Exemple de sélection du parent d'un élément.*

### Sélectionner des éléments avec `childNodes` vs `children`

Vous pouvez sélectionner le contenu d'un élément en utilisant à la fois les propriétés `.childNodes` et `.children`. Mais elles fonctionnent différemment.

`childNodes` : retourne une NodeList de tous les nœuds enfants au sein des éléments sélectionnés. Elle inclura les éléments et les nœuds non-éléments comme les nœuds de texte, les nœuds de commentaire, etc.

`.children` : retourne une collection HTML des seuls éléments enfants (nœuds d'éléments) des objets sélectionnés. Elle n'inclura aucun nœud non-élément comme les textes ou les commentaires.

Voyons un exemple qui montre la différence :

```html
  <div id="container">
    Un nœud de texte
    <p>Un paragraphe</p>
    <!-- Ceci est un commentaire -->
    <span>Élément Span</span>
  </div>
```

Le code ci-dessus n'a que 2 éléments enfants (nœuds d'éléments) : le paragraphe et le span. Mais il y a aussi d'autres éléments – un nœud de texte et un commentaire :

```javascript
const container = document.getElementById('container');

const containerChildNodes = container.childNodes;
const containerChildren = container.children;

console.log(containerChildNodes);
console.log(containerChildren);
```

![Image](https://www.freecodecamp.org/news/content/images/2023/12/Screenshot-2023-12-12-at-10.29.23-AM.png align="left")

*Un exemple d'utilisation de la propriété .childNodes*

Le `childNodes` retournera tous les nœuds enfants (à la fois les éléments et les non-éléments). Il inclut également les espaces blancs entre les éléments en tant que nœuds de texte.

Cela peut être déroutant à utiliser. Donc, sauf si vous avez une bonne raison de ne pas le faire, vous devriez vous en tenir à la propriété `.children`.

Le `children` ne retournera que les éléments enfants (le paragraphe et le span).

![Image](https://www.freecodecamp.org/news/content/images/2023/12/Screenshot-2023-12-12-at-10.34.08-AM.png align="left")

*Un exemple d'utilisation de la propriété* `.children`

### Sélectionner le premier ou le dernier enfant/élément

Si vous devez sélectionner uniquement le premier/dernier enfant ou élément, vous pouvez utiliser ces quatre propriétés.

* `firstChild` : Sélectionne uniquement le premier nœud enfant de l'élément parent.
    
* `lastChild` : Sélectionne uniquement le dernier nœud enfant de l'élément parent.
    
* `firstElementChild` : Sélectionne uniquement le premier élément enfant du parent.
    
* `lastElementChild` : Sélectionne uniquement le dernier élément enfant du parent.
    

Utilisons le même exemple de la section précédente pour voir comment chacun fonctionne :

```html
  <div id="container">
    Un nœud de texte
    <p>Un paragraphe</p>
    <!-- Ceci est un commentaire -->
    <span>Élément Span</span>
  </div>
```

```javascript
const container = document.getElementById('container');

console.log("PREMIER ENFANT :", container.firstChild)
console.log("DERNIER ENFANT :", container.lastChild)
console.log("PREMIER ÉLÉMENT : ", container.firstElementChild)
console.log("DERNIER ÉLÉMENT :", container.lastElementChild)
```

![Image](https://www.freecodecamp.org/news/content/images/2023/12/Screenshot-2023-12-13-at-7.43.25-AM.png align="left")

*Exemple de démonstration de la sélection du premier enfant/élément et du dernier enfant/élément*

Remarquez comment `firstChild` retourne le premier nœud de texte mais `firstElementChild` retourne le premier paragraphe à la place. Cela signifie qu'il a ignoré le nœud de texte qui précède le paragraphe.

Et remarquez également comment `lastChild` retourne un nœud de texte – même si, d'après le balisage, il semble qu'il n'y ait rien après le span. C'est parce que la propriété `lastChild` considère le saut de ligne/espace blanc entre la balise de fermeture du span et la balise de fermeture des éléments div comme un nœud.

C'est pourquoi il est généralement plus sûr de s'en tenir à `firstElementChild` et `lastElementChild`.

### Sélectionner un frère de nœuds dans le DOM

Vous avez appris à sélectionner un parent ou un enfant d'un élément. Vous pouvez également sélectionner un frère d'un élément. Vous le faites en utilisant les propriétés suivantes :

* `nextSibling` : Sélectionne le nœud suivant au sein du même élément parent.
    
* `nextElementSibling` : Sélectionne l'élément suivant, et ignore tout nœud non-élément.
    
* `previousSibling` : Sélectionne le nœud précédent au sein du même élément parent.
    
* `previousElementSibling` : Sélectionne l'élément précédent, et ignore tout nœud non-élément.
    

Voici un exemple :

```html
  <div>
    <p id="one">Premier paragraphe</p>
    nœud de texte
    <p id="two">Deuxième paragraphe</p>
    un autre nœud de texte
    <p id="three">Troisième paragraphe</p>
    <p id="four">Quatrième paragraphe</p>
  </div>
```

```javascript
const paragraphTwo = document.getElementById('two')

console.log("nextSibling: ", paragraphTwo.nextSibling)
console.log("nextElementSibling: ", paragraphTwo.nextElementSibling)
console.log("previousSibling: ", paragraphTwo.previousSibling)
console.log("previousElementSibling: ", paragraphTwo.previousElementSibling)
```

![Image](https://www.freecodecamp.org/news/content/images/2023/12/Screenshot-2023-12-13-at-7.57.18-AM.png align="left")

*Exemples de sélection de frères d'un nœud.*

`nextSibling` et `previousSibling` sélectionnent les nœuds de texte car ils considèrent tous les nœuds au sein du parent. Alors que `nextElementSibling` et `previousElementSibling` sélectionnent uniquement les éléments de paragraphe car ils ignorent les nœuds non-éléments comme le texte.

## Événements du DOM et écouteurs d'événements

Les événements du DOM sont des actions qui se produisent dans le navigateur. Ces événements sont ce qui permet de rendre les sites web interactifs.

Certains événements du DOM sont initiés par l'utilisateur, comme le clic, le déplacement de la souris ou la frappe au clavier. D'autres sont initiés par le navigateur, comme lorsque le chargement d'une page est terminé.

### Différence entre l'écouteur d'événements et le gestionnaire d'événements

Un écouteur d'événements est une méthode qui vous informe lorsqu'un événement s'est produit. Il vous permet d'"écouter" ou de surveiller les événements du DOM. Ainsi, lorsqu'un événement se produit, vous pouvez faire quelque chose.

Un gestionnaire d'événements est une réponse à l'événement. C'est une fonction qui s'exécute lorsqu'un événement se produit.

Par exemple, vous pouvez attacher un écouteur d'événements à un bouton qui vous informe lorsque l'utilisateur clique sur ce bouton. Ensuite, vous pouvez écrire un gestionnaire d'événements (une fonction) qui affiche quelque chose à l'écran chaque fois qu'un événement de clic se produit.

Dans ce cas, l'écouteur d'événements est ce qui informe votre application lorsqu'un clic se produit et déclenche ensuite une réponse. Et la réponse (la fonction qui s'exécute lorsque le clic se produit) est un exemple de gestionnaire d'événements.

### Trois façons d'enregistrer des événements en JavaScript

Voici trois façons différentes d'écouter et de répondre aux événements du DOM en utilisant JavaScript.

* **Utilisation de gestionnaires d'événements en ligne** : Cela consiste à ajouter l'écouteur d'événements en tant qu'attribut aux éléments HTML. Aux premiers jours de JavaScript, c'était la seule façon d'utiliser les événements. Voir l'exemple ci-dessous :
    

```javascript
// Exemple d'utilisation d'un gestionnaire d'événements en ligne

<button onclick="alert('Bonjour')">Cliquez-moi !</button>
```

* **Utilisation de gestionnaires d'événements on-event** : Vous utilisez cela lorsqu'un élément n'a qu'un seul gestionnaire d'événements. Lorsque vous ajoutez plus d'un gestionnaire d'événements en utilisant cette méthode, seul le dernier gestionnaire d'événements s'exécutera, car il remplacera les autres avant lui.
    

```html
<!-- Un exemple d'utilisation d'un gestionnaire d'événements on-event -->

<button>Cliquez-moi !</button>

<script>
  const myButton = document.querySelector('button')
	
  myButton.onclick = function() {
    console.log("Exécuter le premier gestionnaire")
  }
	
  myButton.onclick = function() {
    console.log("Exécuter le deuxième gestionnaire")
  }
</script>
```

![Image](https://www.freecodecamp.org/news/content/images/2023/12/Screenshot-2023-12-14-at-7.41.49-AM.png align="left")

*Seul le deuxième gestionnaire d'événements est exécuté.*

Comme vous pouvez le voir à partir du résultat dans la console, le navigateur exécute le code pour le deuxième gestionnaire d'événements uniquement.

* **Utilisation de la méthode** `addEventListener` : Cette méthode vous permet d'attacher plus d'un gestionnaire d'événements à un élément. Et elle les exécutera dans l'ordre dans lequel ils ont été ajoutés.
    

En règle générale, vous devriez vous en tenir à `addEventListener`, sauf si vous avez une raison impérieuse de ne pas le faire.

La méthode `addEventListener` prend deux arguments. Le premier est l'événement que vous souhaitez écouter, et le second est le gestionnaire d'événements qui est la fonction que vous souhaitez exécuter lorsque l'événement se produit.

```html
<!-- Un exemple d'utilisation de la méthode addEventListener -->

<button>Cliquez-moi !</button>

<script>
  const myButton = document.querySelector('button')
	
  myButton.addEventListener('click', function() {
    console.log("Exécuter le premier gestionnaire")
  })
	
  myButton.addEventListener('click', function() {
    console.log("Exécuter le deuxième gestionnaire")
  })
</script>
```

![Image](https://www.freecodecamp.org/news/content/images/2023/12/Screenshot-2023-12-14-at-7.51.22-AM.png align="left")

*La méthode* `addEventListener` exécute les deux gestionnaires d'événements.

### Défi pratique

Voici un défi pour vous avant de continuer. Essayez de le résoudre par vous-même avant de regarder la solution.

Considérez le code HTML et CSS ci-dessous.

Le défi inclut deux éléments. Une div `#gift-box` et un bouton `#click-btn`. La boîte cadeau est cachée avec la classe `.hide`.

Votre tâche est d'écrire du code JavaScript qui écoute un événement de clic sur le bouton et affiche la boîte cachée lorsque l'utilisateur clique sur le bouton.

```html
<!DOCTYPE html>
<html lang="en">
  <head></head>
  <body>
    
      <div id="gift-box" class="hide">🎁</div>
      <button id="click-btn">Afficher la boîte</button>
      
  </body>
</html>
```

```css
.hide {
  display: none;
}

#gift-box {
  font-size: 5em;
}
```

<a href="https://stackblitz.com/edit/js-cywa91?file=index.html,style.css,index.js" target="_blank"

**Résolvez le défi sur StackBlitz**  
  

![Image](https://www.freecodecamp.org/news/content/images/2023/12/ezgif.com-video-to-gif-converted.gif align="left")

*Gif de démonstration pour la solution finale du défi*

### Solution au défi pratique

Félicitations si vous avez réussi à résoudre le défi. Si ce n'est pas le cas, ce n'est pas grave. La solution et l'explication sont fournies ci-dessous :

```javascript
const giftBoxElement = document.getElementById('gift-box')
const buttonElement = document.getElementById('click-btn')

buttonElement.addEventListener('click', function() {
  giftBoxElement.classList.remove('hide')
})
```

Pour résoudre ce défi, vous devez d'abord sélectionner à la fois l'élément `#gift-box` et `#click-btn`.

Ensuite, vous ajoutez un écouteur d'événements au bouton. Comme mentionné précédemment, la méthode `addEventListener` prend deux arguments.

Dans ce cas, le premier argument est l'événement 'click', et le second argument est une fonction.

Le but est d'afficher la boîte. La boîte a une classe `hide` qui définit `display` sur `none` dans le CSS. Une façon d'afficher la boîte en utilisant JavaScript est de supprimer `hide` de la classList.

### L'objet événement

Il s'agit d'un objet JavaScript que le navigateur passe en argument à la fonction de gestionnaire d'événements chaque fois qu'un événement se produit. L'objet inclut certaines propriétés et méthodes utiles comme les suivantes :

* `type` : le type d'événement qui s'est produit (comme click, mouseover, keydown, etc.)
    
* `target` : l'élément sur lequel l'événement s'est produit
    
* `clientX` et `clientY` : les coordonnées horizontales et verticales du pointeur de la souris au moment où l'événement s'est produit.
    
* `preventDefault()` : empêche les actions par défaut associées aux événements comme empêcher la soumission d'un formulaire lors de l'événement de soumission.
    
* `stopPropagation()` : empêche l'événement de se propager à travers le DOM. Plus sur cela plus tard.
    

Vous pouvez voir une liste complète des propriétés et méthodes sur [la documentation MDN web](https://developer.mozilla.org/en-US/docs/Web/API/Event).

### Types d'événements

Il existe de nombreux types différents d'événements DOM que les navigateurs vous permettent d'écouter. Voici quelques-uns des plus courants.

**Événements de la souris :**

* `click` : lorsque l'élément est cliqué.
    
* `dbclick` : lorsque l'élément est double-cliqué.
    
* `mouseover` : lorsque le pointeur de la souris entre dans l'élément.
    
* `mouseleave` : lorsque le pointeur de la souris quitte l'élément.
    
* `mousedown` : lorsque la souris est enfoncée sur un élément.
    
* `mouseup` : lorsque la souris est relâchée sur un élément.
    

**Événements du clavier :**

* `keydown` : lorsqu'une touche du clavier est enfoncée.
    
* `keyup` : lorsqu'une touche du clavier est relâchée.
    
* `keypress` : lorsqu'une touche est pressée et montre la touche réelle qui a été pressée. Notez que cet événement n'est pas déclenché pour toutes les touches, en particulier les touches non imprimables.
    

**Événements de formulaire :**

* `submit` : lorsqu'un formulaire est soumis.
    
* `input` : lorsque la valeur d'un champ de saisie change.
    
* `change` : lorsque la valeur d'un élément de formulaire change et perd le focus.
    

**Événements de fenêtre :**

* `load` : lorsque le navigateur a fini de charger la page.
    
* `unload` : lorsque l'utilisateur quitte la page.
    
* `resize` : lorsque la fenêtre du navigateur est redimensionnée.
    
* `scroll` : lorsque l'utilisateur fait défiler le document.
    

Vous pouvez voir [une liste complète des événements DOM ici](https://www.w3schools.com/jsref/dom_obj_event.asp).

## Flux d'événements en JavaScript

Lorsque qu'un événement JavaScript se produit, l'événement est propagé ou voyage soit de la cible où l'événement s'est produit vers l'élément le plus externe dans le DOM, soit vice versa.

Par exemple, supposons que vous cliquez sur un bouton sur une page. En cliquant sur le bouton, vous avez également cliqué sur son élément parent et sur tout élément dans lequel le bouton se trouve dans la hiérarchie du DOM.

### Propagation d'événements

C'est lorsque l'événement est d'abord enregistré sur la cible (ou l'élément spécifié) sur lequel l'événement s'est produit, puis enregistré vers l'extérieur vers le parent et ainsi de suite jusqu'à l'élément le plus externe.

Voici un exemple :

```html
<!DOCTYPE html>
<html>
    <head>
        <title>DÉMO de propagation d'événements</title>
    </head>
    <body>
        <div id="outer">
            <div id="inner">
              <button id='btn'>Cliquez ici</button>
            </div>
        </div>
    </body>
</html>
```

L'exemple ici contient un bouton `#btn`. Avec la propagation d'événements, lorsqu'un événement se produit (par exemple un clic) sur le bouton, l'événement passe par la séquence suivante.

![Image](https://www.freecodecamp.org/news/content/images/2023/12/4.png align="left")

*Propagation d'événements dans la manipulation du DOM : du bouton à div#inner à div#outer à body à HTML à document.*

L'événement commence à remonter de l'élément cible vers l'ancêtre le plus externe.

### Capture d'événements

La capture d'événements est l'inverse de la propagation d'événements. L'événement commence à partir de l'élément ancêtre le plus externe et descend dans l'arbre DOM jusqu'à l'élément cible.

![Image](https://www.freecodecamp.org/news/content/images/2023/12/JavaScript--2-.png align="left")

*Capture d'événements dans la manipulation du DOM*

Pendant la phase de capture, les écouteurs d'événements attachés aux éléments sont exécutés dans l'ordre de la hiérarchie, de l'ancêtre le plus élevé à l'élément cible.

Au cas où vous vous demanderiez pourquoi cela est important, voyons un exemple pratique en utilisant le même exemple de balisage HTML que précédemment :

```html
<!DOCTYPE html>
<html>
    <head>
        <title>DÉMO de propagation d'événements</title>
    </head>
    <body>
        <div id="outer">
            <div id="inner">
              <button id='btn'>Cliquez ici</button>
            </div>
        </div>
    </body>
</html>
```

Ajoutons des écouteurs d'événements au bouton, à la div `#inner` et à la div `#outer` :

```javascript
const button = document.getElementById('btn')
const innerDiv = document.getElementById('inner')
const outerDiv = document.getElementById('outer')

button.addEventListener('click', function() {
  console.log('Clic sur le bouton')
})

innerDiv.addEventListener('click', function() {
  console.log('Clic sur la div intérieure')
})

outerDiv.addEventListener('click', function() {
  console.log('Clic sur la div extérieure')
})
```

Par défaut, les navigateurs utilisent l'approche de propagation d'événements. Il n'est donc pas nécessaire d'ajouter un argument à l'écouteur d'événements. Voici l'ordre dans lequel les gestionnaires d'événements s'exécuteront en réponse à un clic sur le bouton :

1. `button`
    
2. `#innerDiv`
    
3. `#outerDiv`
    

![Image](https://www.freecodecamp.org/news/content/images/2023/12/Screenshot-2023-12-15-at-11.54.07-AM.png align="left")

*Les événements sont exécutés de l'élément à l'élément le plus externe dans la phase de propagation.*

Pour utiliser le modèle de capture d'événements, vous devez passer un troisième argument `true` à l'écouteur d'événements.

```javascript
const button = document.getElementById('btn')
const innerDiv = document.getElementById('inner')
const outerDiv = document.getElementById('outer')

button.addEventListener('click', function() {
  console.log('Clic sur le bouton')
}, true)

innerDiv.addEventListener('click', function() {
  console.log('Clic sur la div intérieure')
}, true)

outerDiv.addEventListener('click', function() {
  console.log('Clic sur la div extérieure')
}, true)
```

L'ordre d'exécution des gestionnaires d'événements s'exécutera maintenant dans le sens inverse, comme ceci :

1. `#outerDiv`
    
2. `#innerDiv`
    
3. `button`
    

![Image](https://www.freecodecamp.org/news/content/images/2023/12/Screenshot-2023-12-15-at-11.58.38-AM.png align="left")

*Les événements sont exécutés de l'élément le plus externe à l'élément dans la phase de capture.*

### La méthode `stopPropagation()` de l'événement

Vous avez appris comment la propagation d'événements enregistre un événement sur un élément et continue d'enregistrer l'événement jusqu'à l'élément ancêtre le plus externe. Vous avez également vu comment la capture d'événements fait l'inverse.

Mais que faire si vous ne voulez pas que l'événement soit enregistré sur tous les ancêtres ? C'est là que la méthode `stopPropagation` entre en jeu. Vous pouvez utiliser cette méthode pour empêcher l'événement de se propager à travers tout le DOM.

Utilisons la méthode `stopPropagation` sur le même exemple que précédemment :

```javascript
button.addEventListener('click', function(event) {
  event.stopPropagation()
  console.log('Clic sur le bouton')
})

innerDiv.addEventListener('click', function() {
  console.log('Clic sur la div intérieure')
})

outerDiv.addEventListener('click', function() {
  console.log('Clic sur la div extérieure')
})
```

![Image](https://www.freecodecamp.org/news/content/images/2023/12/Screenshot-2023-12-15-at-2.48.37-PM.png align="left")

*La méthode* `stopPropagation` permet l'exécution uniquement du premier écouteur d'événements.

Maintenant, seul le gestionnaire d'événements sur le bouton est déclenché. Ceux sur `innerDiv` et `outerDiv` ne le sont pas à cause de la méthode `stopPropagation` sur le bouton.

De plus, notez que pour obtenir l'objet événement, vous devez le passer en argument à la fonction de gestionnaire d'événements.

## Idées de projets de manipulation du DOM JS

Construire des projets est un excellent moyen d'améliorer votre compréhension des concepts de codage. Alors, retroussez vos manches et préparez-vous à travailler !

Voici cinq idées de projets de manipulation du DOM JS pour vous aider à pratiquer et à consolider vos compétences.

### Interrupteur à bascule

Concevez un interrupteur à bascule qui change d'état (on/off) lorsqu'il est cliqué. Mettez à jour le DOM (par exemple avec une couleur de fond) qui reflète l'état actuel de l'interrupteur à bascule.

### Sélecteur de couleur aléatoire

Créez une application simple où les utilisateurs peuvent cliquer sur un bouton pour générer une couleur aléatoire. Incluez une forme à l'écran qui se remplit avec la couleur choisie. Affichez également le code de la couleur à l'écran.

### Minuterie de compte à rebours

Construisez une minuterie qui commence à partir d'un temps spécifié. L'application se met à jour en temps réel et affiche le temps restant à l'écran.

### Compteur de mots

Développez une application qui fournit un champ de saisie ou une zone de texte pour que l'utilisateur puisse taper. Affichez le nombre de mots en temps réel à l'écran au fur et à mesure que l'utilisateur tape.

### Une liste de tâches interactive

Créez une application qui permet aux utilisateurs d'ajouter, de supprimer ou de modifier des tâches. Vous pouvez vous amuser avec celle-ci et ajouter autant de fonctionnalités avancées que vous le souhaitez. Par exemple, ajouter des fonctionnalités comme marquer les tâches comme terminées, filtrer les tâches ou les trier.

## Conclusion

Si vous êtes arrivé jusqu'ici, vous avez maintenant une bonne compréhension de la manipulation du DOM JavaScript. Avec de la pratique, vous serez suffisamment confiant pour aborder des projets avancés qui nécessitent la connaissance de ces concepts de manipulation du DOM.

Une bonne base des concepts de manipulation du DOM Vanilla JS sera également utile lors de l'apprentissage des bibliothèques/frameworks JavaScript comme React, Angular, Vue, Svelte, et ainsi de suite.

Merci d'avoir lu, et bon codage ! Pour des tutoriels plus approfondis, n'hésitez pas à [vous abonner à ma chaîne YouTube](https://www.youtube.com/@DevAfterHours).