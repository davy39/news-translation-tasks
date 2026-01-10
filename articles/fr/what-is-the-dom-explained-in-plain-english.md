---
title: Qu'est-ce que le DOM ? Le Modèle d'Objets de Document expliqué en français
subtitle: ''
author: Damilola Oladele
co_authors: []
series: null
date: '2022-06-22T17:54:50.000Z'
originalURL: https://freecodecamp.org/news/what-is-the-dom-explained-in-plain-english
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/DOM-cover-2.png
tags:
- name: Document Object Model
  slug: document-object-model
- name: DOM
  slug: dom
- name: Web Development
  slug: web-development
seo_title: Qu'est-ce que le DOM ? Le Modèle d'Objets de Document expliqué en français
seo_desc: 'Modern web pages are dynamic. This means we need a suitable and convenient
  way to modify and manipulate a web document''s structure.

  This modification in an HTML document, for instance, usually takes the form of creating,
  adding, or removing elements ...'
---

Les pages web modernes sont dynamiques. Cela signifie que nous avons besoin d'une manière appropriée et pratique de modifier et manipuler la structure d'un document web.

Cette modification dans un document HTML, par exemple, prend généralement la forme de la création, de l'ajout ou de la suppression d'éléments dans le document.

Dans cet article, vous apprendrez ce qu'est le **Document Object Model (DOM)**, un peu de son histoire, et comment l'utiliser pour manipuler des documents web, en particulier des documents HTML.

## Qu'est-ce que le Document Object Model (DOM) ?

Le DOM est une interface web, développée et publiée par le **World Wide Web Consortium (**[**W3C**](https://www.w3.org/)**)**. Cette organisation a été fondée pour établir des standards pour le World Wide Web.

Le DOM est une API web qui est neutre en termes de langage. Cela signifie que vous pouvez l'implémenter et l'adopter dans n'importe quel langage de programmation.

Le DOM représente les pièces structurelles d'un document web sous forme d'objets qui peuvent être accessibles et manipulés. En d'autres termes, le DOM vous permet, en tant que développeur logiciel, de faire ce qui suit :

* Créer et construire des documents web.

* Naviguer dans la structure des documents web.

* Ajouter, modifier ou supprimer des éléments et du contenu dans les documents web.

## Histoire du DOM

L'histoire du DOM est relative à JavaScript et JScript en tant que premiers langages de script largement utilisés. Ces langages ont aidé à rendre les pages web interactives.

Avant le développement d'une spécification DOM standard par le W3C, JavaScript et JScript avaient différentes manières de permettre l'accès à la manipulation des documents HTML.

Ces méthodes et interfaces limitées qui vous permettaient de manipuler les documents HTML de cette manière sont devenues le **DOM Level 0**.

En 1998, le W3C a terminé son projet de la première spécification DOM standard, qui est devenue la norme recommandée pour tous les navigateurs. Cette spécification DOM standard est devenue le **DOM Level 1**. Le DOM Level 1 fournissait un modèle complet pour manipuler à la fois les documents HTML et XML.

En 2000, le W3C a publié le **DOM Level 2**, qui a introduit des méthodes telles que `getElementById()`, ainsi qu'un modèle d'événement standardisé et le support des espaces de noms XML et CSS.

Le **DOM Level 3**, publié en 2004, a ajouté le support pour XPath et la gestion des événements clavier. Et à la fin de 2015, la dernière spécification DOM, **DOM Level 4**, est devenue une norme publiée.

## Qu'est-ce que l'arbre DOM ?

La représentation structurelle créée par le DOM ressemble beaucoup à un arbre. Il contient plusieurs objets appelés nœuds.

Le navigateur utilise la représentation de l'arbre DOM qu'il construit à partir d'un document HTML pour déterminer ce qu'il doit rendre sur une page web. Par exemple, une représentation visuelle d'un arbre DOM ressemblera à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/06/DOM-tree.png align="left")

*L'arbre DOM*

Le document HTML de l'arbre DOM ci-dessus ressemble à ceci :

```javascript
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TITLE</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div>
        <h1>HELLO WORLD</h1>
    </div>
    <a href="link text">Document Object Model</a>
</body>
</html>
```

### Nœuds vs Éléments dans le DOM

Souvent, les développeurs confondent nœuds et éléments. Nous devons donc distinguer les deux dès le début de cet article pour éviter toute confusion.

Les **nœuds** sont tous les composants dont un document de page web est constitué. En d'autres termes, une page web est une collection de nœuds.

Un **élément** est un type de nœud dans un document. Par exemple, la propriété DOM `nodes.childNodes`, lorsqu'elle est utilisée sur un nœud parent, renverra tous les différents nœuds contenus dans ce nœud parent spécifié.

Dans l'exemple ci-dessous, la propriété childNodes est utilisée sur le nœud d'élément `<body>` du document HTML donné ci-dessus :

```javascript
//javascript content

//select the <body> element node with the DOM method querySelector
const body = document.querySelector('body') 
//select the children nodes with the <body> element node with the DOM property node.childNodes
const childrenNodes = body.childNodes
//console log the children nodes
console.log(childrenNodes)//NodeList(5) [text, div, text, a, text]
```

Remarquez qu'il y a cinq éléments dans la `nodeList`. Cela est dû au fait que nous avons un autre type de nœud, les nœuds de texte, différents des nœuds d'éléments dans le nœud d'élément `<body>`.

Pour enquêter davantage, suivez les étapes suivantes dans votre console :

1. Cliquez sur l'icône de liste déroulante juste avant "nodeList".

2. Sélectionnez le nœud de texte en cliquant sur l'icône de liste déroulante avant "test".

3. Vérifiez l'option textContent dans les options de la liste dans la liste déroulante.

Si vous suivez les instructions ci-dessus, vous verrez que le contenu de test du premier nœud de texte est "/n ". Il s'agit d'un nœud de texte indiquant une nouvelle ligne après le nœud d'élément `<body>`, le nœud d'élément `<div>`, et le nœud d'élément `<a>`.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/Screenshot--143--1.jpg align="left")

### Relations entre les nœuds dans l'arbre DOM

Les nœuds dans l'arbre DOM ont une relation hiérarchique les uns avec les autres dans l'arbre DOM. Ils sont définis par leur position relative les uns par rapport aux autres dans l'arbre DOM.

Voici les positions des nœuds présentes dans l'illustration de l'arbre DOM ci-dessus :

* **Nœud racine** : Le nœud racine est toujours au sommet de l'arbre DOM. Dans un document HTML, le nœud racine est toujours l'élément `<html>`.

* **Nœud enfant** : Un nœud enfant est un nœud intégré à l'intérieur d'un autre nœud. Dans l'illustration donnée ci-dessus, les éléments `<head>` et `<body>` sont les enfants de l'élément `<html>`.

* **Nœud descendant** : Tout nœud positionné en dessous d'un autre nœud dans l'ordre hiérarchique est le descendant des nœuds positionnés au-dessus. Par exemple, bien que l'élément `<h1>` ne soit pas l'enfant direct de l'élément `<body>`, il est un descendant des éléments `<body>` et racine `<html>`.

* **Nœud parent** : Tout nœud qui contient un autre nœud à l'intérieur est un nœud parent. Par exemple, l'élément `<body>` est le parent des éléments `<div>` et `<a>` dans l'exemple ci-dessus. Notez que seuls les nœuds de type élément peuvent être un nœud parent.

* **Nœuds frères** : Les nœuds qui sont au même niveau dans l'ordre hiérarchique dans l'arbre DOM sont des nœuds frères. Par exemple, les éléments `<div>` et `<a>` dans l'exemple ci-dessus sont des frères.

* **Nœuds feuilles** : Le texte à l'intérieur des éléments sont des nœuds feuilles. Cela est dû au fait qu'ils ne peuvent pas avoir de nœuds enfants à eux seuls.

## HTMLCollection vs nodeList

Pour manipuler l'arbre DOM, vous avez besoin d'une manière de sélectionner des éléments individuels ou une collection d'éléments.

Vous pouvez utiliser un langage de programmation comme JavaScript pour sélectionner un élément ou une collection d'éléments dans l'arbre DOM en utilisant quelques méthodes fournies par le DOM.

Les méthodes `getElementById()` et `querySelector()` peuvent sélectionner des éléments individuels. Les méthodes `getElementsByClassName()`, `getElementsByTagName()`, ou `querySelectorAll()` peuvent sélectionner une collection d'éléments.

Dans l'arbre DOM, nous pouvons obtenir soit une HTMLCollection, soit une NodeList en fonction de la méthode utilisée pour sélectionner une collection d'éléments. Les méthodes `getElementsByClassName()` et `getElementsByTagName()` renvoient des HTMLCollections, tandis que `querySelectorAll` renvoie une nodeList.

HTMLCollection et nodeList partagent certaines similitudes et différences. Elles sont similaires de la manière suivante :

* Ce sont des objets de type tableau.

* Ce sont des collections d'éléments.

* Elles peuvent être converties en tableau en utilisant la méthode `Array.from()`.

* Elles ont toutes deux un indexage basé sur zéro.

* Elles peuvent toutes deux être parcourues avec une boucle for...loop.

* Elles ont une propriété length.

* Elles n'ont pas de méthodes de tableau disponibles.

Ci-dessous se trouve un exemple de document HTML et de code JavaScript pour souligner ces similitudes :

```html
<!-- html documant -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
   <ul>
    <li>item one</li>
    <li>item two</li>
    <li>item three</li>
    <li>item four</li>
   </ul>

    <script src="main.js"></script>
</body>
</html>
```

```javascript
//javascript content

const listItemsHtmlCollection = document.getElementsByTagName("li")
console.log(listItemsHtmlCollection) // HTMLCollection(4) [li, li, li, li]

const listItemsNodeList = document.querySelectorAll("li")
console.log(listItemsNodeList) // NodeList(4) [li, li, li, li]
```

Vous pouvez voir à partir de ce qui précède que tandis que `getElementsByTagName` renvoie une HTMLCollection avec des éléments correspondant à la balise `<li>` spécifiée, `querySelectorAll` renvoie une nodeList.

Maintenant, utilisons une boucle for...loop pour itérer sur les deux collections :

```javascript
for(let i = 0; i < listItemsHtmlCollection.length; i++) {
    listItemsHtmlCollection[i].style.color = 'red'
}

for(let i = 0; i < listItemsHtmlCollection.length; i++) {
    listItemsHtmlCollection[i].style.color = 'red'
}
```

Dans les deux cas, la couleur du texte sera changée en rouge.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/Screenshot--145-.png align="left")

Maintenant, supprimons l'itération de la boucle for...loop et utilisons une méthode de tableau sur map pour itérer sur les deux collections :

```javascript
listItemsHtmlCollection.map( element => element.style.color = 'red' )
listItemsNodeList.map( element => element.style.color = 'red' )
```

![Image](https://www.freecodecamp.org/news/content/images/2022/06/Screenshot--146-.png align="left")

Pour utiliser la méthode map du tableau avec succès, vous devez convertir les deux éléments en un tableau avec la méthode `Array.from()` comme ceci :

```javascript
Array.from(listItemsHtmlCollection).map( element => element.style.color = 'red' )
Array.from(listItemsNodeList).map( element => element.style.color = 'red' )
```

Il y a deux principales différences entre HTMLCollection et nodeList. Elles sont :

* Une nodeList vient avec certaines méthodes et propriétés intégrées non disponibles dans une HTMLCollection. Les méthodes incluent `forEach()` et la méthode `entries` pour itérer sur une nodeList. Les propriétés incluent la propriété keys et la propriété value.

* Une HTMLCollection est toujours live, tandis qu'une nodeList peut être soit live soit statique. Une collection de nœuds est live si un changement dans l'arbre DOM met à jour la collection automatiquement. Si un changement dans l'arbre DOM n'affecte pas la collection, alors elle est statique. Les changements DOM peuvent être l'ajout d'un nouveau nœud ou la suppression d'un nœud existant. Les méthodes DOM telles que `getElementById()` et `getElementsByClassName()` renvoient des HTMLCollections, qui sont toujours live. La méthode `querySelectorAll()` renvoie une nodeList statique.

## Méthodes DOM HTML

Le DOM level 1 core, Dom level 2 core, et Dom level 3 core ont introduit plusieurs méthodes qui permettent aux développeurs web de manipuler l'arbre DOM. Certaines de ces méthodes sont les suivantes :

### La méthode DOM `createElement()`

La méthode `createElement()` crée un élément du type spécifié comme argument.

```html
//html document

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
   <ul>
    <li>item one</li>
    <li>item two</li>
    <li>item three</li>
    <li>item four</li>
   </ul>

    <script src="main.js"></script>
</body>
</html>
```

```javascript
//javascript content

//select the parent element
const list = document.querySelector('ul')
//create a new element
const listItem = document.createElement('li')
//make the newly created element a child of the parent
list.appendChild('listItem')
console.log(list)
```

Maintenant, vérifiez la console pour la liste console logged. Vous verrez qu'il y a maintenant cinq éléments `<li>` dans l'élément parent `<ul>`.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/Screenshot--147--1.png align="left")

### La méthode DOM `createTextNode()`

La méthode `createTextNode()` crée un nœud de texte avec la chaîne spécifiée comme argument. Ajoutons du texte à l'élément `<li>` que nous avons créé ci-dessus.

```javascript
//javascript content

const listText = document.createTextNode("item five")
listItem.appendChild(listText)
```

Maintenant, enregistrez votre fichier JavaScript et rechargez votre page web.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/Screenshot--149-.png align="left")

### La méthode DOM `appendChild()`

La méthode `appendChild()` ajoute un nœud à la fin de la liste des enfants d'un nœud parent.

Si l'enfant spécifié est un nœud existant dans le document, `appendChild()` le déplace de sa position actuelle dans l'arbre DOM vers la nouvelle position. Nous avons utilisé la méthode plus tôt pour faire de notre nouvel élément `<li>` un enfant de l'élément `<ul>`.

### La méthode DOM `getElementById()`

Cette méthode sélectionne et renvoie l'élément dont l'ID est spécifié à l'intérieur comme argument. Si un tel élément n'existe pas, la méthode renvoie null. Ajoutons un attribut *id* à notre élément `<ul>` dans le document HTML et donnons-lui une bordure rouge.

```html
//html document

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
   <ul id="ulList">
    <li>item one</li>
    <li>item two</li>
    <li>item three</li>
    <li>item four</li>
   </ul>


    <script src="main.js"></script>
</body>
</html>
```

```javascript
//javascript content

const ulList = document.getElementById("ulList") 
ulList.style.border = '2px solid red'
```

![Image](https://www.freecodecamp.org/news/content/images/2022/06/Screenshot--150-.png align="left")

### La méthode DOM `getElementsByClassName()`

La méthode `getElementsByClassName()` sélectionne tous les éléments avec le nom de classe spécifié et les renvoie sous forme d'HTMLCollection dans l'ordre où ils apparaissent dans l'arbre DOM.

Vous pouvez accéder aux éléments individuels dans l'HTMLCollection par leur numéro d'index. Ajoutons un attribut de classe aux deux premiers éléments `<li>` dans notre document HTML et changeons leur couleur de texte en rouge comme ceci :

```html
//html document

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
   <ul id="ulList">
    <li class="itemOneAndTwo">item one</li>
    <li class="itemOneAndTwo">item two</li>
    <li>item three</li>
    <li>item four</li>
   </ul>


    <script src="main.js"></script>
</body>
</html>
```

```javascript
//javascript content

//select by elements one and two by their class name
const itemOneAndTwo = document.getElementsByClassName("itemOneAndTwo")
//change text color to red with use of index
itemOneAndTwo[0].style.color = 'red'
itemOneAndTwo[1].style.color = 'red'
```

![Image](https://www.freecodecamp.org/news/content/images/2022/06/Screenshot--151-.png align="left")

### La méthode DOM `getElementsByTagName()`

La méthode `getElementsByTagName()` renvoie une HTMLCollection de tous les éléments avec le nom de balise spécifié comme argument, dans l'ordre où ils apparaissent dans l'arbre DOM.

Sélectionnons les éléments `<li>` avec la méthode `getElementsBytagName()` et changeons leur style de police en italique.

```javascript
//javascript content

const liTags = document.getElementsByTagName("li") 
for(let i = 0; i < liTags.length; i++) {
    liTags[i].style.fontStyle = 'italic'
}
```

![Image](https://www.freecodecamp.org/news/content/images/2022/06/Screenshot--152-.png align="left")

### La méthode DOM `querySelector()`

La méthode `querySelector()` accepte n'importe quel sélecteur de chaîne CSS comme argument. Elle utilise ensuite le sélecteur spécifié pour sélectionner le premier élément dans le document qui correspond à ce sélecteur spécifié.

Changeons la sélection de nos deux premiers éléments `<li>` avec la méthode `querySelector()` et changeons leur couleur de texte en noir.

```javascript
//javascript content

const querySelectItem = document.querySelector("itemOneAndTwo")
querySelectItem.style.color = 'black'
```

![Image](https://www.freecodecamp.org/news/content/images/2022/06/Screenshot--153-.png align="left")

Remarquez que seul le premier élément de la liste a vu sa couleur changée en noir.

### La méthode DOM `querySelectorAll()`

La méthode `querySelectorAll()`, tout comme la méthode `querySelector`, accepte n'importe quel sélecteur de chaîne CSS comme argument. Elle utilise ensuite le sélecteur de chaîne CSS spécifié pour sélectionner tous les éléments qui correspondent à ce sélecteur spécifié, les place dans une nodeList, et renvoie cette nodeList.

Maintenant, utilisons-la pour changer tout le texte dans nos éléments de liste en vert.

```javascript
//javascript content

const querySelectAllItems = document.querySelectorAll("li")
for(let i = 0; i < querySelectAllItems.length; i++) {
    querySelectAllItems[i].style.color = 'green'
}
```

![Image](https://www.freecodecamp.org/news/content/images/2022/06/Screenshot--154-.png align="left")

### La méthode DOM `setAttribute()`

La méthode `setAttribute()` ajoute un nouveau nom d'attribut à un élément. Si un attribut avec ce nom est déjà présent dans l'élément, sa valeur changera pour celle définie dans l'argument.

La méthode accepte deux arguments. Le premier argument est le nom de l'attribut que vous souhaitez créer. Le deuxième argument est la valeur à définir sur l'attribut, qui est toujours une chaîne.

Utilisons-la pour donner à notre troisième élément un attribut de classe et changer la couleur du texte en noir.

```javascript
//javascript content

const itemThree = querySelectAllItems[2] 
itemThree.setAttribute("class", "attributeValue")  
const attributeValue = document.querySelector('.attributeValue')
attributeValue.style.color = 'black'
```

![Image](https://www.freecodecamp.org/news/content/images/2022/06/Screenshot--155-.png align="left")

### La méthode DOM `removeAttribute()`

La méthode `removeAttribute()` supprime un attribut spécifié. Elle prend le nom de l'attribut à supprimer comme argument. Supprimons l'attribut *id* de l'élément parent `<ul>` et utilisons l'id supprimé pour supprimer sa bordure rouge.

```javascript
//javascript content

//remove attribute
ul.removeAttribute('id')
ul.style.border = 'none'
```

Maintenant, enregistrez votre fichier JavaScript et rechargez votre page web. Remarquez que les bordures sont toujours là. Si vous vérifiez la console, vous verrez un message d'erreur indiquant que *ul* n'est plus défini.

### La méthode DOM `contains()`

La méthode `contains()` renvoie true si un nœud est un descendant d'un nœud et renvoie false sinon.

```html
<--HTML document--> 
<body>   
    <h1>Heading</h1> 
</body>
```

```javascript
//javascript content
const body = document.querySelector('body')
const h1Element = document.querySelector('h1')
console.log( body.contains(h1Element) ) // true
```

### La méthode DOM `item()`

La méthode `item()` renvoie l'élément spécifié à l'index spécifié comme argument lorsqu'elle est utilisée sur une collection.

```html
<--HTML document--> 
<body>   
    <p>Paragraph</p> 
    <p>Paragraph</p> 
</body>
```

```javascript
//javascript content
const pElements = document.querySelectorAll("p") 
console.log(pElements.item(0)) // <p></p>
```

### La méthode DOM `hasChildNodes()`

La méthode `hasChildNodes` renvoie true si l'élément sur lequel elle est appelée a des nœuds enfants à l'intérieur et renvoie false sinon.

```html
<--HTML document--> 
<body>   
    <p>Paragraph</p> 
    <p>Paragraph</p> 
</body>
```

```javascript
//javascript content

const body = document.querySelector("body")

console.log(body.hasChildNodes()) // true
```

## Qu'est-ce que les événements DOM ?

Pour rendre notre page web logiquement interactive en initiant des réponses ou des incidents automatiques sur la page web, nous avons besoin d'événements.

Les événements DOM sont :

> des actions ou des occurrences qui se produisent dans le système que vous programmez, que le système vous signale afin que votre code puisse réagir à eux. (Source : [MDN](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Events#event_objects))

Un exemple courant d'un événement est lorsque l'utilisateur clique sur un bouton de soumission dans un formulaire, qui envoie ensuite les données saisies par l'utilisateur en réponse au clic.

Un autre exemple est lorsque l'utilisateur clique sur une icône de menu, ce qui déclenche ensuite un menu déroulant de navigation ou d'options.

Vous pouvez utiliser des langages de script tels que JavaScript pour enregistrer des gestionnaires d'événements ou des écouteurs sur des éléments à l'intérieur de l'arbre DOM, qui s'exécutent lorsque l'événement spécifié se déclenche.

Un gestionnaire d'événements est :

> un bloc de code (généralement une fonction JavaScript que vous créez en tant que programmeur) qui s'exécute lorsque l'événement se déclenche. Lorsqu'un tel bloc de code est défini pour s'exécuter en réponse à un événement, nous disons que nous **enregistrons un gestionnaire d'événements**. (Source : [MDN](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Events#event_objects))

Des exemples d'événements utilisés sur des éléments dans l'arbre DOM incluent :

* **click** : Un événement de clic est un mousedown ou mouseup sur un élément d'une page web.

* **keypress** : Un événement keypress se produit lorsque des touches du clavier sont pressées.

* **mouseover** : Un événement mouseover se produit lorsque le dispositif de pointage est déplacé sur un élément.

* **dblclick** : Un dblclick se produit lorsqu'il y a un événement de double-clic sur un élément d'une page web.

* **submit** : Un événement submit se produit lorsqu'un formulaire est soumis.

## Conclusion

Le DOM est l'épine dorsale du dynamisme web moderne. Il représente chaque pièce d'un document web sous forme d'objet et fournit aux langages de programmation les méthodes nécessaires pour manipuler et modifier chaque pièce.

Si vous avez apprécié cet article, vous devriez me donner un [*shoutout*](https://twitter.com/activus_d).

### Références et lectures complémentaires

1. [https://dom.spec.whatwg.org/](https://dom.spec.whatwg.org/)

2. [https://www.w3.org/TR/1998/REC-DOM-Level-1-19981001/level-one-core.html](https://www.w3.org/TR/1998/REC-DOM-Level-1-19981001/level-one-core.html)

3. [https://www.w3.org/TR/1998/REC-DOM-Level-1-19981001/level-one-html.html](https://www.w3.org/TR/1998/REC-DOM-Level-1-19981001/level-one-html.html)

4. [https://www.w3.org/TR/DOM-Level-2-HTML/](https://www.w3.org/TR/DOM-Level-2-HTML/)

5. [https://www.w3.org/TR/DOM-Level-3-Core/core.html](https://www.w3.org/TR/DOM-Level-3-Core/core.html)