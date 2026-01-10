---
title: Le DOM expliqué aux débutants – Comment fonctionne le Document Object Model
subtitle: ''
author: Kingsley Ubah
co_authors: []
series: null
date: '2021-05-17T17:45:50.000Z'
originalURL: https://freecodecamp.org/news/dom-explained-everything-you-need-to-know-about-the-document-object-model
coverImage: https://www.freecodecamp.org/news/content/images/2021/05/DOM--1-.png
tags:
- name: Document Object Model
  slug: document-object-model
- name: DOM
  slug: dom
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: Le DOM expliqué aux débutants – Comment fonctionne le Document Object Model
seo_desc: 'When I started out as a web developer, people often threw around the term
  "DOM" in the industry. Every JavaScript tutorial mentioned it, but I didn''t know
  what it meant.

  Fast forward two years, and now that I know what it''s all about, I am going to
  e...'
---

Quand j'ai commencé en tant que développeur web, les gens utilisaient souvent le terme "DOM" dans le milieu. Chaque tutoriel JavaScript le mentionnait, mais je ne savais pas ce que cela signifiait.

Deux ans plus tard, maintenant que je sais de quoi il s'agit, je vais expliquer ce qu'est le **Document Object Model** en un français simple et clair.

## Qu'est-ce que le DOM ?

Imaginez ceci : vous avez allumé la télévision. Vous n'aimez pas l'émission diffusée et vous voulez en changer. Vous voulez aussi augmenter le volume.

Pour ce faire, il doit y avoir un moyen pour vous d'interagir avec votre téléviseur. Et qu'utilisez-vous pour cela ?

**Une télécommande**.

La télécommande sert de **pont** qui vous permet d'interagir avec votre téléviseur.

Vous rendez la télévision **active** et **dynamique** via la télécommande. De la même manière, JavaScript rend la page HTML active et dynamique via le **DOM**.

Tout comme la télévision ne peut pas faire grand-chose par elle-même, JavaScript ne fait pas beaucoup plus que de vous permettre d'effectuer quelques calculs ou de travailler avec des chaînes de caractères de base.

Ainsi, pour rendre un document HTML plus interactif et dynamique, le script doit pouvoir accéder au contenu du document et doit également savoir quand l'utilisateur interagit avec lui.

Il le fait en communiquant avec le navigateur à l'aide des propriétés, méthodes et événements de l'interface appelée Document Object Model, ou DOM.

Par exemple, supposons que vous vouliez qu'un bouton change de couleur lorsqu'on clique dessus ou qu'une image glisse lorsque la souris passe dessus. Tout d'abord, vous devez référencer ces éléments à partir de votre JavaScript.

Le DOM est une représentation sous forme d'arbre de la page web qui est chargée dans le navigateur.

Il représente la page web à l'aide d'une série d'objets. L'objet principal est l'objet document, qui abrite à son tour d'autres objets qui abritent également leurs propres objets, et ainsi de suite.

### L'objet Document

C'est l'objet le plus élevé dans le DOM. Il possède des **propriétés** et des **méthodes** que vous pouvez utiliser pour obtenir des informations sur le document en utilisant une règle connue sous le nom de notation pointée.

![The Document Object Model Tree](https://www.freecodecamp.org/news/content/images/2021/05/table.png align="left")

*Arbre du document. Source https://w3.org*

Après le document, vous placez un point suivi d'une propriété ou d'une méthode.

Regardons une démonstration simple qui montre comment un script peut accéder au contenu d'un document HTML via le DOM :

```html
<h1>Login to your account</h1>‌
<form name=”LoginFrm” action=”login.php” method=”post”>‌Username 
    <input type=”text” name=”txtUsername” size=”15”/> <br/>‌Password 
    <input type=”password” name=”numPassword” size=”15”/> <br/>‌
    <input type=”submit” value=”Log In” />‌
</form>‌
<p> New user? <a href=”register.php”> Register here</a> 
<a href=”lostPassword.php”> Retrieve password </a> 
</p>
```

```js
var username = document.LoginFrm.txtUsername.value // Récupère la saisie du nom d'utilisateur
```

D'accord. C'est le code HTML d'un formulaire de connexion. Vous pouvez accéder à tous ces éléments en JavaScript avec l'ensemble de propriétés et de méthodes fourni par l'API DOM. Mais quelles sont ces méthodes ?

En plus de la propriété et de la méthode incluses dans l'extrait de code, jetons un coup d'œil à d'autres méthodes populaires :

### La méthode querySelectorAll()

Vous utilisez cette méthode pour accéder à un ou plusieurs éléments du DOM qui correspondent à un ou plusieurs sélecteurs CSS :

```html
<div> first div </div>
<p> first paragraph </p>
<div> second div </p>
<p> second paragraph </p>
<div> another div </div>
```

```js
var paragraphs = document.querySelectorAll( 'p' );
paragraphs.forEach(paragraph => paragraph.display = 'none')
```

### La méthode createElement()

Vous utilisez cette méthode pour créer un élément spécifié et l'insérer dans le DOM :

```html
<div>first div</div>
<p> first paragraph</p> 
<div>second div</div>
<p>second paragraph</p> 
<div>another div</div>
```

```js
var thirdParagraph = document.createElement('p');
```

### La méthode getElementById()

Vous utilisez cette méthode pour obtenir un élément du document par son attribut id unique :

```html
<div id='first'> first div </div> 
<p> first paragraph</p>
<div>second div</div>
<p> second paragraph</p>
<div>another div</div>
```

```js
var firstDiv = getElementById("first")
```

### La méthode getElementsByTagname()

Vous utilisez cette méthode pour accéder à un ou plusieurs éléments par leur nom de balise HTML :

```html
<div> first div </div> 
<p> first paragraph</p> 
<div> second div</div> 
<p>second paragraph</p> 
<div>another div</div>
```

```js
divs = document.getElementByTagname("div");
```

### L'élément appendChild()

Vous utilisez cet élément pour accéder à un ou plusieurs éléments par leur nom de balise HTML.

Il ajoute un élément comme dernier enfant de l'élément HTML qui invoque cette méthode.

L'enfant à insérer peut être soit un élément nouvellement créé, soit un élément déjà existant. S'il existe déjà, il sera déplacé de sa position précédente vers la position du dernier enfant.

```html
<div
     <h2>Mangoes</h1>
</div>
```

```js
var p = document.createElement( 'p' );
var h2 = document.querySelector( 'h2' );
var div = document.querySelector( 'div' );
h1.textContent = 'Mangoes are great...'
div.appendChild('p');
```

### La propriété innerHTML

Vous utilisez cette propriété pour accéder au contenu textuel d'un élément.

### La propriété addEventListener()

Cette propriété attache un écouteur d'événements à votre élément.

Elle prend un callback qui s'exécutera lorsque cet événement sera déclenché.

```html
<button>Click to submit</button>‌
```

```js
var btn = document.querySelector( 'button' );‌
btn.addEventListener( 'click' ,foo);‌
function foo() { alert( 'submitted!' ); 
  				btn.innerHTML = '';
          }
```

### La propriété replaceChild()

Cette propriété remplace un élément enfant par un autre élément enfant, nouveau ou existant. S'il existe déjà, il sera déplacé de sa position précédente vers la position du dernier enfant.

```html
<div>‌
    <h1>Mangoes‌</h1>‌
</div>
```

```js
var h2 = document.createElement( 'h2' );‌
var h1 = document.querySelector( 'h1' );‌
var div = document.querySelector( 'div' );‌
h2.textContent = 'Apple';‌
div.insertBefore(h1, h2);
```

### La méthode setAttribute()

Vous utilisez cette méthode pour définir ou modifier la valeur de l'attribut d'un élément.

Supposons que nous ayons un attribut "id" contenant la valeur "favourite". Mais nous voulons changer la valeur en "worst". Voici comment faire avec du code :

```html
<div>‌
    <h1 id='favourite'>Mangoes‌‌</h1>
</div>
```

```js
var h1 = document.querySelector( 'h1' );
h1.setAttribute(div, 'worst');
```

### La méthode node

Chaque élément d'une page HTML est connu sous le nom de nœud (node).

Vous pouvez accéder à n'importe quel élément en utilisant les propriétés suivantes avec l'objet node :

* `node.childNodes` – accède aux nœuds enfants d'un parent sélectionné‌
    
* `node.firstChild` – accède au premier enfant d'un parent sélectionné‌
    
* `node.lastChild` – accède au dernier enfant d'un parent sélectionné.‌
    
* `node.parentNode` – accède au parent d'un nœud enfant sélectionné.‌
    
* `node.nextSibling` – accède à l'élément consécutif suivant (frère) d'un élément sélectionné.‌
    
* `node.previousSibling` – accède à l'élément précédent (frère) d'un élément sélectionné
    

```html
<ul id-“list”>‌
    <li><a href= ”about.html”‌class = ”list_one”> About‌</a></li>‌
    <li><a href= ”policy.html”> Policy‌</a></ li>‌
    <li><a href= ”map.html”> Map‌</a></ li>‌
    <li><a href= ”Refund.html”> Refund‌</a></li>‌
</ul>
```

```js
var list = document.getElementsById( “site-list” )‌
var firstItem = list‌.childNodes[0].childNodes[0];
```

## Résumé

Le DOM est une représentation descendante de tous les éléments qui composent une page web. C'est l'interface par laquelle votre script interagit avec votre HTML.

Il existe de nombreuses propriétés et méthodes que vous pouvez utiliser pour obtenir des informations sur le DOM et le manipuler.

C'est tout pour cet article. J'espère que vous avez appris quelque chose d'utile.

Si vous l'avez aimé, vous pouvez m'offrir un café [ici](https://ubahthebuilder.tech).

Merci et à bientôt.