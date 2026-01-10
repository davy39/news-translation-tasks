---
title: JavaScript dans le navigateur – Comment fonctionne le Document Object Model
  (DOM) et les événements
subtitle: ''
author: Samyak Jain
co_authors: []
series: null
date: '2024-02-15T20:07:14.000Z'
originalURL: https://freecodecamp.org/news/javascript-in-the-browser-dom-and-events
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/JavaScript-in-the-Browser-with-Photo-Cover.png
tags:
- name: browser
  slug: browser
- name: Document Object Model
  slug: document-object-model
- name: DOM
  slug: dom
- name: events
  slug: events
- name: handbook
  slug: handbook
- name: JavaScript
  slug: javascript
seo_title: JavaScript dans le navigateur – Comment fonctionne le Document Object Model
  (DOM) et les événements
seo_desc: "In this in-depth tutorial, you'll learn all about the Document Object Model,\
  \ or DOM for short. As a web developer, understanding the DOM is fundamental for\
  \ interacting with web browsers and creating dynamic web applications. \nThroughout\
  \ this guide, w..."
---

Dans ce tutoriel approfondi, vous apprendrez tout sur le Document Object Model, ou DOM en abrégé. En tant que développeur web, comprendre le DOM est fondamental pour interagir avec les navigateurs web et créer des applications web dynamiques. 

Tout au long de ce guide, nous explorerons la structure arborescente hiérarchique du DOM, les propriétés essentielles et les méthodes pour accéder et modifier les nœuds. Nous plongerons également dans la gestion des événements et diverses techniques pour une manipulation efficace du DOM.

À la fin de ce guide, vous devriez être en mesure de manipuler le DOM en toute confiance pour répondre aux exigences de vos projets de développement web.

### Prérequis :

Bien que ce guide soit conçu pour être accessible aux débutants, avoir une compréhension de base des fondamentaux de JavaScript améliorera grandement votre capacité à saisir les concepts pratiques couverts. 

De plus, la familiarité avec HTML et CSS est un atout et vous aidera à comprendre et appliquer le matériel que nous couvrons. 

Si vous êtes nouveau en JavaScript, envisagez de vous familiariser avec les variables, les types de données, les fonctions, les boucles et les techniques de base de manipulation du DOM avant de plonger dans ce tutoriel. Ces connaissances fondamentales garantiront une expérience d'apprentissage plus fluide alors que nous explorons des sujets plus avancés liés au Document Object Model (DOM).

## Table des matières

1. [Qu'est-ce que le Browser Object Model (BOM)](#browser-object-model-bom-)?
2. [Qu'est-ce que le Document Object Model (DOM)](#quest-ce-que-le-document-object-model-dom)
3. [Structure arborescente du DOM](#heading-installation)  
– [Types de nœuds dans l'arborescence DOM](#heading-types-de-noeuds-dans-larbre-dom)  
– [Relations entre nœuds](#heading-relations-entre-noeuds)
4. [Comment travailler avec les éléments DOM](#heading-comment-travailler-avec-les-elements-dom)  
– [Parcourir le DOM](#methodes-pour-parcourir-le-dom-)  
– [Méthodes pour interroger les éléments DOM](#heading-methodes-pour-interroger-les-elements-dom)  
– [Sélecteurs spécialisés (Matches, Closest, Contains)](#heading-matches-closest-et-contains)  
– [Comment inspecter les éléments DOM](#heading-comment-inspecter-les-elements-dom)  
– [Navigation dans les tableaux du DOM](#heading-navigation-dans-les-tableaux-du-dom)
5. [Comment modifier les éléments DOM](#heading-comment-modifier-les-elements-dom)  
– [Comment manipuler le contenu et la visibilité des éléments](#heading-comment-manipuler-le-contenu-et-la-visibilite-des-elements)  
– [Comment modifier les attributs des éléments](#heading-comment-modifier-les-attributs-des-elements)  
– [Méthodes d'insertion HTML](#heading-methodes-dinsertion-html)  
– [Comment manipuler les classes avec JavaScript](#heading-comment-manipuler-les-classes-avec-javascript)
6. [Gestion des événements dans le DOM](#heading-gestion-des-evenements-dans-le-dom)  
– [Types courants d'événements](#heading-types-courants-devenements)  
– [Gestionnaires d'événements](#heading-gestionnaires-devenements)  
– [Propagation des événements](#heading-propagation-des-evenements)  
– [Remontée d'événements](#heading-remontee-devenements)  
– [Délégation d'événements](#heading-delegation-devenements)
7. [Conclusion](#heading-conclusion)

## Qu'est-ce que le Browser Object Model (BOM) ?

Le Browser Object Model est comme un ensemble d'outils fourni par le navigateur lui-même. Il ne fait pas partie de la spécification officielle du DOM, mais il est spécifique aux navigateurs web. Par conséquent, les objets et méthodes disponibles dans le BOM peuvent varier entre différents navigateurs.

Le BOM fournit à JavaScript l'accès à des éléments spécifiques au navigateur comme l'historique du navigateur, l'emplacement et la fenêtre du navigateur elle-même.

### Objet Window

L'objet `window` sert d'objet global dans le navigateur, représentant la fenêtre du navigateur et est l'objet de niveau supérieur en JavaScript lorsque nous travaillons dans un navigateur web. Vous pouvez y accéder en tapant `window` dans la console du navigateur :

```javascript
console.log(window); // imprime l'objet Window
```

Puisqu'il est global, vous pouvez y accéder de n'importe où et l'utiliser pour accéder à d'autres objets globaux tels que la console et la fonction d'alerte.

L'objet `window` est une partie clé du BOM et fournit l'accès à de nombreuses choses liées au navigateur. Par exemple, `window.location.href` vous donne l'URL de la page web actuelle.

Les fonctions comme `alert()`, `prompt()`, et `confirm()` font également partie du BOM, vous permettant d'interagir avec les utilisateurs via des boîtes de dialogue pop-up.

## Qu'est-ce que le Document Object Model (DOM) ?

Le Document Object Model (DOM) est une interface de programmation pour les documents web. Il représente la structure d'une page web, permettant l'interaction avec ses éléments à l'aide de langages de programmation comme JavaScript.

Le DOM contient l'objet `document`, qui représente la structure DOM de la page web actuelle et possède des propriétés et des méthodes qui vous permettent de manipuler le DOM.

Vous pouvez accéder à l'objet `document` en tapant `document` dans la console du navigateur :

```javascript
console.log(document); // imprime l'objet DOM
```

Vous utilisez l'objet `document` pour accéder et manipuler différentes parties du document HTML. Les éléments au sein du DOM peuvent être accessibles en utilisant les propriétés et méthodes de cet objet.

Les exemples incluent l'accès à l'élément `body` ou `title`, la récupération du contenu HTML (`innerHTML`), l'accès au contenu textuel (`innerText`) et la modification des `styles`.

```javascript
// Accéder au titre du document
console.log(document.title);

// Changer le titre du document
document.title = "Titre modifié";

// Accéder au corps du document 
console.log(document.body);

```

```javascript
// Changer la couleur de fond de l'élément body en utilisant le CSS en ligne
document.body.style.backgroundColor = "red";

```

Vous pouvez utiliser le DOM pour interagir avec les pages web de manière dynamique. Cela permet à JavaScript d'accéder, de modifier et de manipuler le contenu, la structure et le style d'un document web en réponse aux actions de l'utilisateur ou à d'autres événements. 

Illustrons le concept de manipulation du DOM avec un exemple simple :

```html
<html>
  <body>
    <div id="container">
      <p id="message">Bonjour, le Monde !</p>
      <button id="changeText">Changer le texte</button>
    </div>

    <script>
      // nous sélectionnons l'élément paragraphe par son ID
      let messageElement = document.getElementById("message");

      // ajoutons un écouteur d'événement à l'élément bouton en utilisant l'ID
      document
        .getElementById("changeText")
        .addEventListener("click", function () {
          // ceci changera le contenu textuel de l'élément paragraphe
          messageElement.textContent = "Texte changé !";
        });
    </script>
  </body>
</html>

```

Dans cet exemple, nous avons un document HTML avec un conteneur `<div>` contenant un élément `<p>` et un élément `<button>`. 

En utilisant JavaScript, nous pouvons sélectionner l'élément `<p>` par son ID et attacher un écouteur d'événement à l'élément `<button>`. Lorsque le bouton est cliqué, le contenu textuel de l'élément paragraphe est changé dynamiquement.

## Structure arborescente du DOM

Le DOM représente la disposition des documents HTML et XML sous forme de structure arborescente, ressemblant à l'arrangement hiérarchique des éléments sur une page web. Dans cet arbre, chaque nœud représente une partie du document, telle que les éléments HTML, les attributs et le texte.

Le nœud de niveau supérieur dans l'arbre est appelé le **nœud document**, qui représente l'ensemble du document HTML. À partir de là, il se ramifie pour inclure tous les éléments et leurs relations au sein du document. Voici une représentation visuelle de cela :

![Image](https://www.freecodecamp.org/news/content/images/2024/02/pic_htmltree-1.gif)
_Arbre DOM des objets_

### Types de nœuds dans l'arborescence DOM

Il existe deux principaux types de nœuds dans le DOM :

1. **Nœuds d'élément** : Représentent les éléments HTML tels que `<div>`, `<h1>`, `<p>`, `<span>`, et ainsi de suite. Ces nœuds constituent l'épine dorsale de l'arborescence DOM et forment la structure du document HTML.
2. **Nœuds de texte** : Représentent le contenu textuel au sein des éléments HTML. Le texte sert toujours de dernier enfant (nœud feuille) d'un nœud d'élément et ne peut contenir aucun nœud enfant.

En HTML, les espaces blancs tels que les espaces, les tabulations et les retours à la ligne sont considérés comme faisant partie du contenu textuel au sein des éléments HTML et sont représentés comme des **nœuds de texte**.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/image-62.png)
_Le retour à la ligne est le 1er nœud enfant, div (Bleu) est le 2ème, retour à la ligne à nouveau le 3ème_

![Image](https://www.freecodecamp.org/news/content/images/2024/02/image-64.png)
_Nous pouvons voir tous les nœuds ici, y compris les non-éléments (comme les nœuds de texte ou les nœuds de commentaire)_

Nous avons également :

* **Nœuds d'attribut** : Représentent les attributs des éléments HTML, par exemple `id`, `class`, `src`, `href`, et ainsi de suite.
* **Nœuds de commentaire** : Nœuds représentant les commentaires dans le balisage HTML.

Pour accéder et manipuler les éléments DOM, nous pouvons "parcourir" la structure arborescente en utilisant JavaScript. Par exemple :

* `document.head` : Sélectionne l'élément `<head>` du document HTML actuel.
* `document.body` : Sélectionne l'élément `<body>` du document HTML actuel.
* `document.documentElement` : Sélectionne l'élément racine de l'arborescence DOM, c'est-à-dire `<html>`.

Une fois que nous avons accédé à un élément, nous pouvons modifier ses attributs ou propriétés en conséquence. Par exemple, nous pouvons modifier la couleur de fond de l'élément `<body>` en rouge en exécutant `document.body.style.backgroundColor = "red"` dans la console.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/image-80.png)
_Nous pouvons voir que la couleur du corps a changé en "rouge"_

### Relations entre nœuds

Les nœuds dans l'arborescence DOM ont des relations parent-enfant, qui forment la structure hiérarchique de l'arbre. Un enfant est un élément qui réside directement au sein d'un autre élément (le parent).

```html
<div id="container">
    <p>Bonjour, le Monde !</p>
    <button>Cliquez-moi</button>
</div>

```

Dans l'arborescence DOM, les éléments frères sont disposés linéairement. L'élément à droite de l'élément actuel est appelé le frère suivant, tandis que l'élément à gauche est appelé le frère précédent.

Dans l'exemple ci-dessus, l'élément `<p>` (frère précédent de <button>) et l'élément `<button>` (frère suivant de <p>) sont des **nœuds frères** car ils partagent le même parent. Ils sont tous deux des **nœuds enfants** de l'élément `<div>` avec l'ID "container". Ainsi, l'élément `<div>` sert de **nœud parent** à la fois pour les éléments `<p>` et `<button>`.

Les éléments positionnés au-dessus d'un élément donné dans la hiérarchie de l'arborescence DOM sont appelés ancêtres. Dans le code donné, l'élément `<html>` agit comme l'**ancêtre** des éléments `<body>`, `<h1>`, et `<p>`, et ils sont des **descendants** de l'élément `<html>`.

## Comment travailler avec les éléments DOM

Maintenant, plongeons dans l'accès aux nœuds dans le DOM en utilisant diverses propriétés et méthodes.

### Parcourir le DOM :

Lorsque vous travaillez avec le Document Object Model (DOM), il est important de comprendre la distinction entre les nœuds d'élément (éléments HTML) et les nœuds non-élément (comme les nœuds de texte, les commentaires, etc.). Certaines propriétés et méthodes traitent spécifiquement soit des nœuds d'élément, soit de tous les types de nœuds, y compris les nœuds non-élément.

**NodeList vs. HTMLCollection :** Différentes propriétés retournent différentes collections de nœuds. NodeList contient tous les types de nœuds, tandis que HTMLCollection contient spécifiquement des nœuds d'élément. Comprendre cette distinction est crucial pour interpréter les résultats.

**Propriétés pour tous les nœuds (y compris les nœuds non-élément) :** Ces propriétés retournent des nœuds de tous les types, y compris les nœuds d'élément, les nœuds de texte et les nœuds de commentaire. 

`childNodes` retourne une NodeList contenant tous les nœuds enfants et la propriété `parentNode` retourne le nœud parent du nœud spécifié. Par exemple :

```javascript
// Accéder au premier enfant du nœud body
console.log(document.body.childNodes[0]);


// parentnode; le parent d'un élément <p> au sein d'un <div> serait le <div> lui-même.
let p = document.querySelector('p'); // Sélectionner l'élément <p>
console.log(p.parentNode); // Sortie : élément <div> (parent de p); 
```

Les espaces entre les balises et les retours à la ligne dans le code HTML sont considérés comme des nœuds de texte par le navigateur. Ainsi, le premier nœud enfant réel pourrait ne pas être celui auquel vous vous attendez.

`firstChild`/`lastChild` : Retourne le premier/dernier nœud enfant, incluant à nouveau tous les types.

```javascript
document.body.firstChild; // Sorties : Premier nœud enfant (probablement un retour à la ligne (nœud de texte))
document.body.lastChild; // Sorties : Dernier nœud enfant (probablement une balise script)

```

Nous pouvons donc dire ce qui suit :

```javascript
element.childNodes[0] === element.firstChild;
element.childNodes[element.childNodes.length - 1] === element.lastChild;

```

`nextSibling`/`previousSibling` : retourne le nœud frère suivant/précédent, incluant tous les types.

**Propriétés spécifiques aux éléments ou navigation uniquement par éléments :** Ces propriétés fournissent un moyen pratique d'accéder uniquement aux nœuds d'élément, à l'exclusion des nœuds de texte et des commentaires.

`children` retourne une HTMLCollection live des éléments enfants directs, et la propriété `parentElement` retourne le nœud élément parent du nœud spécifié.

Dans la capture d'écran ci-dessous, vous pouvez voir la différence entre `childNodes` et `children` :

![Image](https://www.freecodecamp.org/news/content/images/2024/02/image-62.png)
_Ici, le retour à la ligne (nœud de texte) sera considéré comme le 1er nœud enfant de l'élément body, tandis que div.color (Bleu) sera considéré comme le 1er enfant._

Par exemple, supposons que nous avons ce code :

```javascript
// childnode
console.log(document.body.childNodes);

// children
console.log(document.body.children);
```

```
// childnode
NodeList(19) [text, div.color, text, div.color, text, comment, text, div.color, text, div.color, text, div.color, text, script, text, comment, text, script, text]


// children
HTMLCollection(7) [div.color, div.color, div.color, div.color, div.color, script, script]

```

et, si nous actualisons la page, la sortie devient :

```
NodeList(14) [text, div.color, text, div.color, text, comment, text, div.color, text, div.color, text, div.color, text, script]
HTMLCollection(6) [div.color, div.color, div.color, div.color, div.color, script]
```

Initialement, la `NodeList` contient 19 nœuds. Ces nœuds consistent en des nœuds de texte, des éléments `div` avec la classe "color", un nœud de commentaire et des éléments `script`. La `HTMLCollection` contient 7 éléments, qui sont les éléments `div` avec la classe "color" et les éléments `script`.

Lorsque la page est actualisée, certains éléments ou nœuds sont supprimés ou modifiés dynamiquement via JavaScript ou d'autres moyens, conduisant aux changements observés dans la structure du DOM.

`firstElementChild`/`lastElementChild` retourne le premier/dernier enfant, à l'exclusion des nœuds non-élément.

```javascript
// Les deux excluront les nœuds de texte et les nœuds de commentaire.
document.body.firstElementChild; // Sorties : <div class="color">
document.body.lastElementChild; // Sorties : <script src="script.js">

```

**Points clés :**

* Choisissez la bonne propriété en fonction de vos besoins pour cibler tous les nœuds ou spécifiquement les nœuds d'élément.
* N'oubliez pas que des propriétés comme `firstChild` et `previousSibling` peuvent retourner des nœuds d'élément et non-élément, tandis que leurs homologues spécifiques aux éléments (`firstElementChild` et `previousElementSibling`) se concentrent uniquement sur les éléments.

### Méthodes pour interroger les éléments DOM :

JavaScript fournit plusieurs méthodes pour accéder aux éléments dans le DOM :

* **`getElementById` :** Cette méthode récupère un élément par son attribut ID unique.

```javascript
let element = document.getElementById("myElement");

```

* **`getElementsByClassName` :** Cette méthode retourne une collection d'éléments avec le nom de classe spécifié.

```javascript
let elements = document.getElementsByClassName("myClass");

```

* **`getElementsByTagName` :** Cette méthode retourne une liste de collection d'éléments avec le nom de balise spécifié.

```javascript
let elements = document.getElementsByTagName("div");

```

* **`querySelector` :** Cette méthode récupère le premier élément qui correspond à un sélecteur CSS spécifié.

```javascript
let element = document.querySelector("cssSelector");

```

* **`querySelectorAll` :** Cette méthode récupère tous les éléments qui correspondent à un sélecteur CSS.

```javascript
let elements = document.querySelectorAll("cssSelector");

```

Vous vous demandez peut-être comment `querySelector` diffère de `querySelectorAll`.

Eh bien, `querySelector` retourne le premier élément dans le document qui correspond au sélecteur spécifié. En revanche, `querySelectorAll` retourne une NodeList statique représentant une liste des éléments du document qui correspondent au groupe de sélecteurs spécifié.

Lorsque vous utilisez `querySelectorAll`, vous recevez une NodeList, qui est similaire à un tableau mais pas exactement la même chose. Vous ne pouvez pas manipuler directement tous les éléments comme appliquer des styles à tous les éléments dans une NodeList en utilisant des méthodes comme `style.backgroundColor = 'red'`. Nous utilisons donc une boucle `forEach`. Par exemple :

```javascript
console.log(document.querySelectorAll(".box"));

document.querySelectorAll('.box').forEach(element => {
    // Dans la boucle forEach, nous accédons à chaque élément et définissons sa couleur de fond en vert.
    element.style.backgroundColor = "green";
});

```

Voyons ce qui se passe dans ce code :

* Dans la première ligne, nous changeons directement la couleur de fond de l'élément avec la classe 'box' en utilisant querySelector.
* Dans la deuxième ligne, nous utilisons querySelectorAll pour sélectionner tous les éléments avec la classe 'box' et enregistrons la NodeList dans la console.
* Dans la troisième ligne, puisque `querySelectorAll` retourne une NodeList, nous devons itérer à travers chaque élément dans la NodeList afin d'appliquer la couleur de fond à chaque élément séparément.
* Donc, en gros, nous pouvons dire que `querySelector` est équivalent à `querySelectorAll('section')[0]`.

D'accord, une dernière méthode à considérer :

* **`getElementsByName`** : Cette méthode retourne une liste de collection d'éléments avec l'attribut name spécifié.

```javascript
let items = document.getElementsByName('some-name-attribute');
console.log(items);
```

Ces méthodes sont importantes à comprendre car elles sont utilisées dans diverses situations. 

Par exemple, lorsque nous voulons sélectionner tous les éléments `div` dans le document, nous pouvons utiliser la méthode `querySelectorAll` ou la méthode `getElementsByTagName`. Les deux méthodes retourneront le même résultat, mais `querySelectorAll` est plus flexible car elle peut sélectionner des éléments qui correspondent à n'importe quel sélecteur CSS. `getElementsByTagName` ne peut sélectionner que des éléments qui ont le même nom de balise.

### Matches, Closest, et Contains : 

Lorsque vous travaillez avec JavaScript et que vous traitez des pages web, vous devez souvent trouver des parties spécifiques de la page ou effectuer des actions avec elles. Trois méthodes que vous pourriez utiliser sont `matches()`, `closest()`, et `contains()`.

**`matches()`** vérifie si un élément correspond à une certaine règle de style. Par exemple, si vous avez un bouton et que vous voulez voir s'il a une classe "active", vous pourriez utiliser `button.matches('.active')`. Il retournera vrai si le bouton a cette classe, et faux sinon.

```javascript
const button = document.querySelector('button');
if (button.matches('.active')) {
  console.log('Le bouton est actif');
} else {
  console.log('Le bouton n\'est pas actif');
}

```

Si vous avez un élément et que vous voulez trouver son parent le plus proche avec une certaine classe, vous pouvez utiliser `**closest()**` comme ceci : `element.closest('.classname')`. 

Par exemple, si vous avez un lien à l'intérieur d'un élément de liste et que vous voulez trouver l'élément de liste le plus proche, vous pourriez faire `link.closest('li')`.

```javascript
const link = document.querySelector('a');
const listItem = link.closest('li');
console.log(listItem); // Cela vous donnera l'élément de liste le plus proche

```

Et **`contains()`** vérifie si un élément est à l'intérieur d'un autre. Par exemple, si vous avez une div et un paragraphe à l'intérieur, vous pourriez vérifier si la div contient le paragraphe avec `div.contains(paragraph)`. Il retournera vrai si le paragraphe est à l'intérieur de la div, et faux sinon.

```javascript
const div = document.querySelector('div');
const paragraph = document.querySelector('p');
if (div.contains(paragraph)) {
  console.log('La div contient un paragraphe');
} else {
  console.log('La div ne contient aucun paragraphe');
}

```

Ces méthodes sont pratiques pour naviguer autour de votre page web et faire différentes choses avec ses éléments.

### Comment inspecter les éléments DOM

**Utilisation de console.dir() :** `console.dir()` n'est pas une méthode du DOM. C'est une méthode fournie par l'API Console du navigateur, spécifiquement utilisée pour journaliser les objets JavaScript dans la console.

Si nous journalisons un élément en utilisant `console.log()`, nous voyons sa représentation HTML. Mais avec `console.dir()`, nous obtenons une liste interactive montrant tous les attributs et fonctions disponibles pour cet élément.

**`tagName`** et `nodeName` : `tagName` est une propriété spécifique aux éléments HTML. Elle retourne le nom de la balise d'un élément HTML en lettres majuscules. Par exemple, si vous avez un élément HTML `<div>`, `tagName` retournera `"DIV"`.

D'autre part, `nodeName` est une propriété des nœuds DOM qui représente le nom du nœud. Pour les nœuds d'élément, elle retourne le nom de la balise en majuscules. Pour les autres types de nœuds, elle retourne une chaîne représentant le type de nœud (par exemple, "#text" pour les nœuds de texte, "#comment" pour les nœuds de commentaire).

**Découverte du type d'un nœud :** Chaque nœud dans le DOM a une propriété `nodeType` qui indique son type. Elle a une valeur numérique : `1` pour les éléments, `2` pour les attributs, `3` pour les nœuds de texte, `8` pour les commentaires et `9` pour le document. En lecture seule. Cette propriété peut être utilisée pour distinguer les nœuds d'élément des nœuds de texte. Par exemple :

```javascript
const element = document.createElement('div');
console.log(element.nodeType); // Sortie : 1

```

### Navigation dans les tableaux du DOM

Maintenant, apprenons à naviguer dans un élément de tableau et ses nœuds enfants en utilisant le DOM. Ici, au lieu d'écrire manuellement un tableau, nous utiliserons le tableau prédéfini de Bootstrap.

Avant de plonger dans la navigation des tableaux, discutons de Bootstrap, un framework front-end populaire offrant des composants et des styles prédessinés pour construire des pages web réactives efficacement.

Pour intégrer Bootstrap dans notre projet, nous allons :

1. Copier le tableau prédéfini depuis [ici](https://getbootstrap.com/docs/5.3/content/tables/).
2. Le coller dans un conteneur `<div>` dans notre HTML.
3. Inclure les fichiers CSS et JS de Bootstrap dans notre page web (que vous pouvez copier depuis [ici](https://getbootstrap.com/docs/5.3/getting-started/introduction/)).

Voici à quoi ressemblera notre code HTML après l'intégration :

```html
<!DOCTYPE html>
<html>
<head>
    <title>Navigation dans les tableaux</title>
    <link rel="stylesheet" href="styles.css">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KK94CHFLLe+nY2dmCWGMq91rCGa5gtU4mk92HdvYe+M/SXH301p5ILy+dN9+nJOZ" crossorigin="anonymous">
</head>
<body>
   <div class="container">
    <!-- Tableau Bootstrap -->
    <table class="table">
        <!-- En-tête du tableau -->
        <thead>
          <tr>
            <th scope="col">#</th>
            <th scope="col">First</th>
            <th scope="col">Last</th>
            <th scope="col">Handle</th>
          </tr>
        </thead>
        <!-- Corps du tableau -->
        <tbody>
          <tr>
            <th scope="row">1</th>
            <td>Mark</td>
            <td>Otto</td>
            <td>@mdo</td>
          </tr>
          <tr>
            <th scope="row">2</th>
            <td>Jacob</td>
            <td>Thornton</td>
            <td>@fat</td>
          </tr>
          <tr>
            <th scope="row">3</th>
            <td colspan="2">Larry the Bird</td>
            <td>@twitter</td>
          </tr>
        </tbody>
      </table>
   </div>
    <script src="script.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ENjdO4Dr2bkBIFxQpeoTz1HIcje39Wm4jDKdf19U8gI4ddQ3GYNS7NTKfAdVQSZe" crossorigin="anonymous"></script>
</body>
</html>

```

#### Propriétés de navigation dans les tableaux :

L'élément tableau prend en charge diverses propriétés pour une navigation pratique, telles que :

* `table.rows` : Retourne une HTMLCollection de toutes les lignes du tableau.
* `table.caption` : Retourne l'élément de légende du tableau.
* `table.tHead` : Retourne l'élément thead du tableau.
* `table.tFoot` : Retourne l'élément tfoot du tableau.
* `table.tBodies` : Retourne une HTMLCollection de tous les éléments tbody du tableau.

De même, l'élément tr (ligne de tableau) prend en charge des propriétés comme :

* `tr.cells` : Retourne une HTMLCollection de toutes les cellules de la ligne.
* `tr.sectionRowIndex` : Retourne l'index de la ligne dans la section actuelle (thead, tbody ou tfoot).
* `tr.rowIndex` : Retourne l'index de la ligne dans le tableau.

L'élément td (cellule de tableau) prend également en charge la propriété `td.cellIndex`, retournant l'index de la cellule dans la ligne.

Par exemple, pour imprimer toutes les lignes du tableau :

```javascript
let t = document.body.firstElementChild.firstElementChild; // Sélection du tableau
for (let i = 0; i < t.rows.length; i++) {
    let row = t.rows[i];
    console.log(row)
}

```

Pour imprimer les cellules de la première ligne :

```javascript
let t = document.body.firstElementChild.firstElementChild; // Sélection du tableau
let row = t.rows[0]; // Sélection de la première ligne
for (let i = 0; i < row.cells.length; i++) {
    let cell = row.cells[i];
    console.log(cell)
}

```

## Comment modifier les éléments DOM 

Une fois que vous avez accès aux éléments DOM, vous pouvez les modifier de diverses manières en utilisant JavaScript.

### Comment manipuler le contenu et la visibilité des éléments

#### `innerHTML` et `outerHTML`

Vous pouvez utiliser `innerHTML` pour accéder ou changer le contenu HTML à l'intérieur d'un élément sous forme de chaîne. `outerHTML`, en revanche, vous permet d'obtenir ou de définir le contenu HTML d'un élément sous forme de chaîne, y compris l'élément original lui-même.

Voici un exemple :

```html
<body>
	Bonjour le Monde
    <span>Hey je suis un span</span>
    <script src="script.js"></script>
</body>
```

```javascript
let first = document.getElementsByTagName("span")[0]; // 

// journaliser et changer le HTML interne
console.log(first.innerHTML); // Sortie : Hey je suis un span
first.innerHTML = "Hey je suis changé"; // Modifier le contenu de l'élément <span>

// journaliser et changer le HTML externe
console.log(first.outerHTML); // Sortie : <span>Hey je suis un span</span>
first.outerHTML = "<h1>Hey je suis changé</h1>"; // Recharger la page pour voir le changement


```

#### Propriété `textContent`

La propriété `textContent` vous permet de définir ou de récupérer le contenu textuel d'un élément, en ignorant toutes les balises HTML qu'il contient. Elle est utile lorsque vous souhaitez mettre à jour le contenu textuel d'un élément sans affecter sa structure HTML.

```javascript
console.log(first.textContent); // sortie : Hey je suis un span

// changer le contenu textuel
first.textContent = "Hey je suis changé";
```

#### Propriété `innerText`

La propriété `innerText` retourne uniquement le contenu textuel visible d'un élément, en excluant tout texte à l'intérieur des éléments `<script>` et `<style>`, et en tenant compte du style CSS qui affecte la visibilité. Elle prend en compte le style CSS, tel que `display: none`, `visibility: hidden`, etc., et retourne uniquement le texte qui est rendu à l'écran. 

#### Propriété `style` 

Cette propriété fournit l'accès à un objet pour manipuler les styles en ligne d'un élément (par exemple, `element.style.color = "red"`).

#### Propriété `hidden`

La propriété `hidden` fournit un moyen simple et pratique de contrôler la visibilité des éléments dans le DOM sans manipuler directement leurs propriétés de style.

```javascript
document.getElementsByTagName('span')[0].hidden = true;

// Lorsque hidden est défini sur false, l'élément est visible.

```

Notez que définir la propriété `hidden` d'un élément sur `true` ne fait que le masquer à la vue, mais il occupe toujours de l'espace dans la mise en page du document. 

### Comment modifier les attributs des éléments

La méthode `getAttribute()` récupère la valeur d'un attribut spécifié d'un élément, tandis que `setAttribute()` définit ou met à jour la valeur d'un attribut spécifié. 

`hasAttribute()` vérifie si un élément possède un attribut spécifique, en retournant vrai ou faux. La méthode `removeAttribute()` supprime un attribut spécifié d'un élément.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/image-68.png)

En HTML5, il est possible de définir des attributs personnalisés pour les éléments. Mais pour éviter les conflits potentiels avec les futures mises à jour de HTML ou JavaScript, vous devez préfixer les attributs personnalisés avec `data-`. Par exemple :

```html
<div id="element1" class="sample" data-category="music" data-rating="5">
    C'est le premier élément.
</div>

```

Pour accéder à ces attributs personnalisés en utilisant JavaScript, nous pouvons utiliser la propriété `dataset`. Par exemple :

```javascript
console.log(element1.dataset);

```

Cela affichera un objet `DOMStringMap` contenant tous les attributs personnalisés associés à la div "element1". Des attributs personnalisés spécifiques peuvent également être accessibles par leurs noms. Par exemple :

```javascript
console.log(element1.dataset.category);

// Ce code afficherait la valeur de l'attribut personnalisé "category", qui dans ce cas est "music"
```

### Méthodes d'insertion HTML

En HTML, il existe plusieurs façons d'insérer un nouveau contenu ou de modifier un contenu existant de manière dynamique en utilisant JavaScript. Ce sont ce que l'on appelle les méthodes d'insertion HTML. 

Considérons le HTML suivant comme notre exemple :

```html
<html>
<head>
</head>
<body>
	<div class="container">
        <div id="first">premier élément</div>
    </div>
    <script src="script.js"></script>
</body>
</html>
```

#### Méthode classique pour insérer du HTML :

Une méthode conventionnelle pour insérer du HTML consiste à utiliser la propriété `innerHTML`. Par exemple, supposons que nous voulons ajouter un élément `h1` avec le texte "Bonjour le Monde" à l'intérieur du premier `div`. Nous pouvons faire cela en utilisant le code suivant :

```javascript
let a = document.getElementsByTagName('div')[0];
a.innerHTML = '<h1>Bonjour le Monde</h1>';
```

Nous pourrions également ajouter un nouveau HTML au HTML existant à l'intérieur de l'élément `div`. Par exemple :

```javascript
// Cela conservera l'ancien contenu et ajoutera un nouvel élément h1.
let a = document.getElementsByTagName('div')[0];
a.innerHTML = a.innerHTML + '<h1>Bonjour le Monde</h1>';
```

#### Utilisation de `createElement` pour insérer du HTML : 

Une autre méthode consiste à créer un nouvel élément en utilisant `createElement`, à définir son contenu en utilisant `innerHTML`, puis à l'ajouter à l'élément cible en utilisant `appendChild`.

#### Autres méthodes d'insertion HTML :

```html
<!DOCTYPE html>
<html>
<head>
</head>
<body>
Je suis en dehors de la div (début)
<div class="container">
	Je suis le début de ce conteneur
        <div id="first">Je suis le premier élément</div>
	Je suis la fin de ce conteneur
</div>
Je suis en dehors de la div (fin)
    <script src="script.js"></script>
</body>
</html>

```

Maintenant, considérons d'autres méthodes pour insérer du contenu HTML de manière dynamique :

```javascript
let a = document.getElementsByTagName('div')[0];

// Utilisation de createElement et appendChild
let div = document.createElement('div');
div.innerHTML = '<h1>Bonjour le Monde (append)</h1>';
a.appendChild(div);

// Utilisation de prepend
let div = document.createElement('div');
div.innerHTML = '<h1>Bonjour le Monde (prepend)</h1>';
a.prepend(div);

// Utilisation de before
let div = document.createElement('div');
div.innerHTML = '<h1>Bonjour le Monde (before)</h1>';
a.before(div);

// Utilisation de after
let div = document.createElement('div');
div.innerHTML = '<h1>Bonjour le Monde (after)</h1>';
a.after(div);

// Utilisation de replaceWith
let div = document.createElement('div');
div.innerHTML = '<h1>Bonjour le Monde (replaced)</h1>';
a.replaceWith(div);

```

Ce code démontre différentes méthodes pour insérer dynamiquement du contenu HTML dans le DOM en utilisant JavaScript.

* `a.append(div)` : Cette méthode ajoute l'élément `div` comme dernier enfant de l'élément `a`.
* `a.prepend(div)` : Cette méthode ajoute l'élément `div` comme premier enfant de l'élément `a`.
* `a.before(div)` : Cette méthode ajoute l'élément `div` avant l'élément `a`.
* `a.after(div)` : Cette méthode ajoute l'élément `div` après l'élément `a`.
* `a.replaceWith(div)` : Cette méthode remplace l'élément `a` par l'élément `div`.

### Les méthodes `insertAdjacentHTML`, `insertAdjacentElement`, et `insertAdjacentText`

Ces méthodes sont utilisées pour insérer du contenu dans le DOM à une position spécifiée par rapport à un élément donné. Elles sont utiles lorsque vous devez ajouter dynamiquement de nouveaux éléments ou du texte à votre page web.

#### `insertAdjacentHTML` :

`insertAdjacentHTML` vous permet d'insérer une chaîne de HTML à une position spécifiée par rapport à l'élément.

Le premier paramètre spécifie où la chaîne HTML sera insérée :

* `beforebegin` : Avant l'élément lui-même.
* `afterbegin` : Juste à l'intérieur de l'élément, avant son premier enfant.
* `beforeend` : Juste à l'intérieur de l'élément, après son dernier enfant.
* `afterend` : Après l'élément lui-même.

Exemple d'utilisation :

```javascript
let element = document.getElementById('example');
element.insertAdjacentHTML('beforebegin', '<div>Nouveau contenu</div>');

```

#### `insertAdjacentElement` :

C'est similaire à `insertAdjacentHTML`, mais au lieu d'insérer du HTML, vous pouvez insérer un élément DOM.

Exemple d'utilisation :

```javascript
let element = document.getElementById('example');
let newElement = document.createElement('div');
newElement.textContent = 'Nouveau contenu';
element.insertAdjacentElement('beforebegin', newElement);

```

#### `insertAdjacentText` :

C'est similaire à `insertAdjacentHTML`, mais au lieu d'insérer du HTML, vous pouvez insérer du texte brut.

Exemple d'utilisation :

```javascript
let element = document.getElementById('example');
element.insertAdjacentText('beforebegin', 'Nouveau contenu');

```

#### Suppression de nœud :

La méthode `remove` supprime l'élément du DOM.

Exemple d'utilisation :

```javascript
let element = document.getElementById('example');
element.remove();

```

Ces méthodes vous permettent de manipuler le DOM de manière dynamique, en ajoutant ou en supprimant du contenu en fonction de certaines conditions ou interactions utilisateur.

Lorsque vous utilisez `insertAdjacentHTML`, `insertAdjacentElement`, ou `insertAdjacentText`, vous spécifiez où le nouveau contenu doit être inséré par rapport à l'élément donné.

Lorsque vous utilisez `remove`, vous supprimez simplement l'élément du DOM entièrement.

Ces méthodes sont utiles pour mettre à jour dynamiquement le contenu de votre page web sans avoir à recharger toute la page.

### Comment manipuler les classes avec JavaScript

En HTML, nous utilisons des classes pour regrouper des éléments et appliquer des styles en utilisant CSS. Par exemple, nous avons une div avec un id "first" dans notre HTML.

```html
<div id="first">
    <span>Bonjour, ceci est du texte</span>
</div>

```

Nous avons également des styles CSS pour des classes comme "yellow", "red", et "text-dark" pour changer la couleur de fond et la couleur du texte.

```css
.yellow {
    background-color: yellow;
    color: white;
}
.red {
    background-color: red;
    color: white;
}
.text-dark {
    color: black;
}

```

**`className` :** En JavaScript, nous pouvons changer la classe d'un élément en utilisant la propriété `className`. Par exemple, si nous voulons changer la classe de l'élément avec l'id "first" en "red text-dark", nous ferions :

```javascript
// nous appliquons 2 classes ici
first.className = "red text-dark";

```

Si nous voulons ajouter une autre classe sans supprimer celles existantes, nous utilisons l'opérateur `+=` :

```javascript
first.className += " yellow"; // Ajoute la classe "yellow" sans supprimer les classes existantes

```

**`classList` :** La propriété `classList` vous permet de manipuler les classes d'un élément. Nous pouvons utiliser des méthodes comme `add`, `remove`, `toggle`, et `contains` pour ajouter, supprimer, basculer ou vérifier la présence d'une classe.

* `classList.remove()` : Supprime une classe spécifique de l'élément :

```javascript
first.classList.remove('text-dark'); // Supprime la classe "text-dark"

```

* `classList.add()` : Mais attendez, c'était mieux avec cette classe ! Nous pouvons aussi l'ajouter à nouveau avec :

```javascript
first.classList.add('text-dark'); // Ajoute la classe "text-dark"

```

* `classList.toggle()` : Basculer une classe en fonction de sa présence :

```javascript
first.classList.toggle('text-dark'); // Basculer la classe "text-dark" (ajoute si absente, supprime si présente)


```

* `classList.contains()` : Vérifie si une classe est présente sur l'élément :

```javascript
console.log(first.classList.contains('text-dark')); // Retourne vrai si la classe "text-dark" est présente

```

## Gestion des événements dans le DOM

Les événements sont des actions ou des occurrences qui se produisent dans le système que vous programmez, et auxquels le système peut avoir besoin de répondre d'une certaine manière. 

Dans le contexte du développement web, les événements (**Événements du navigateur**) peuvent être des interactions utilisateur comme des clics, des mouvements de souris, des pressions de touches, etc. JavaScript vous permet de gérer ces événements et d'effectuer des actions en réponse à ceux-ci.

En HTML, vous pouvez spécifier directement ce qui doit se passer lorsqu'un événement se produit en utilisant des attributs comme `onclick`, `onmouseover`, etc. Par exemple :

```html
<button onclick="alert('bonjour')">Cliquez-moi</button>

```

Bien que vous puissiez écrire du JavaScript directement dans les attributs HTML, il est toujours préférable de garder votre HTML propre et de gérer les événements dans le code JavaScript séparément. Cela rend votre code plus facile à lire et à maintenir.

Vous pouvez le faire en sélectionnant des éléments de la page web en utilisant JavaScript, puis en attachant un gestionnaire d'événements à ceux-ci. Voici comment vous pourriez le faire :

```javascript
let container = document.getElementById("container");
container.onclick = function() {
    console.log("Hey, ceci est journalisé depuis le script !");
}

```

Dans ce code, nous sélectionnons l'élément avec l'id "container" en utilisant `document.getElementById()`. Ensuite, nous attachons une fonction à l'événement `onclick` de cet élément. Cette fonction sera exécutée chaque fois que l'élément est cliqué.

### Types courants d'événements :

1. **Événements de souris** : Ces événements sont liés aux interactions avec la souris. 

* **click** : Lorsque vous cliquez sur un élément.
* **contextmenu** : Lorsque vous faites un clic droit sur un élément.
* **mouseover / mouseout** : Lorsque le curseur de la souris entre ou quitte un élément.
* **mousedown / mouseup** : Lorsque vous appuyez ou relâchez un bouton de la souris sur un élément.
* **mousemove** : Lorsque la souris est déplacée.

Quelques exemples d'événements de souris :

```javascript
// Exemple de propriété du bouton de la souris :

<div onmousedown="console.log('Bouton de la souris :', event.button)">Cliquez-moi</div>

```

Dans cet exemple, la propriété event.button est utilisée pour journaliser quel bouton de la souris a été pressé.

```javascript
// Exemple de touches modificatrices :

<div onclick="if(event.ctrlKey) console.log('Ctrl + Clic !')">Ctrl + Cliquez-moi</div>

```

Cet exemple journalise un message lorsque l'utilisateur clique sur l'élément tout en maintenant la touche Ctrl enfoncée.

```javascript
// Exemple de coordonnées :

<div onmousemove="console.log('clientX :', event.clientX, 'clientY :', event.clientY)">Déplacez votre souris ici</div>

```

Cet exemple journalise les coordonnées clientX et clientY du pointeur de la souris lorsqu'il se déplace sur l'élément.

```javascript
// Exemple de prévention de la sélection :

<span ondblclick="console.log('Double cliqué !')" onmousedown="return false;">Double-cliquez-moi</span>

```

Dans cet exemple, l'instruction return false dans le gestionnaire d'événement onmousedown empêche le comportement de sélection par défaut lorsque l'élément est double-cliqué.

2.  **Événements du clavier** – **keydown / keyup** : Lorsqu'une touche est pressée ou relâchée sur le clavier.

Quelques exemples d'événements du clavier :

```javascript
<input type="text" onkeydown="console.log('Touche pressée !')" onkeyup="console.log('Touche relâchée !')">

```

Dans cet exemple, le champ de saisie déclenche des événements lorsqu'une touche est pressée (keydown) et relâchée (keyup).

```javascript
// Exemple de modificateurs d'événement :

<input type="text" onkeydown="if(event.ctrlKey && event.key === 'c') console.log('Ctrl + C pressé !')">

```

Cet exemple journalise un message lorsque l'utilisateur appuie simultanément sur la touche Ctrl et la touche 'c' dans le champ de saisie.

```javascript
// Exemple d'accès aux informations sur les touches :

<input type="text" onkeydown="console.log('Touche pressée :', event.key)">
```

Cet exemple journalise la touche qui a été pressée dans le champ de saisie.

3.  **Événements des éléments de formulaire** : Ces événements se produisent lorsque vous interagissez avec des éléments de formulaire, comme la soumission d'un formulaire, la mise au point sur un champ de saisie, etc.

4.  **Événements du document** : Ces événements sont liés à l'objet document lui-même. Exemple : **DOMContentLoaded** (lorsque le HTML est entièrement chargé et que le DOM est prêt)

5.  **Événements CSS** : Ces événements sont liés aux animations CSS. Exemple : **transitionend** (Lorsque une animation CSS se termine)

Maintenant, voyons un exemple démontrant l'application pratique de la gestion des événements et de la validation des entrées dans le développement web :

```html
<html>
<head>
<title>Exemple de validation d'entrée</title>
<script>
function checkPhoneNumber(event) {
  const validKeys = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '(', ')', '-'];
  if (!validKeys.includes(event.key)) {
    event.preventDefault(); // Empêcher l'action par défaut pour les touches invalides
  }
}
</script>
</head>
<body>
<label for="phone">Entrez le numéro de téléphone :</label>
<input type="tel" id="phone" onkeydown="checkPhoneNumber(event)">
<p>Seuls les chiffres, +, (, ), et - sont autorisés.</p>
</body>
</html>

```

Dans cet exemple, nous implémentons la validation des entrées pour un champ de saisie de numéro de téléphone. L'événement `onkeydown` déclenche la fonction `checkPhoneNumber`, qui vérifie si la touche pressée est valide (chiffres, signe plus, parenthèses ou trait d'union). Si la touche n'est pas valide, l'action par défaut (saisie de caractère) est empêchée.

Vous pouvez [explorer plus d'informations sur les événements ici](https://www.freecodecamp.org/news/dom-events-and-javascript-event-listeners/).

### Gestionnaires d'événements

Pour réagir à ces événements, nous utilisons des gestionnaires d'événements. Un gestionnaire d'événements est simplement une fonction qui s'exécute lorsqu'un événement spécifique se produit. Il existe différentes façons d'assigner des gestionnaires d'événements en JavaScript :

1. **Attribut HTML** : Vous pouvez définir un gestionnaire d'événements directement dans le code HTML en utilisant un attribut comme `onclick`, `onmouseover`, etc.

```html
<button onclick="alert('Bouton cliqué !')">Cliquez-moi</button>

```

2.  **Propriété DOM** : Vous pouvez assigner un gestionnaire en utilisant une propriété DOM comme `onclick`, `onmouseover`, etc.

```html
<button id="myButton">Cliquez-moi</button>
<script>
  document.getElementById("myButton").onclick = function() {
    alert('Bouton cliqué !');
  };
</script>

```

3.  **Écouteurs d'événements** : Les écouteurs d'événements sont des fonctions qui attendent qu'un événement spécifique se produise, puis exécutent une fonction désignée. Cela se fait généralement en utilisant la méthode `addEventListener`. 

### `addEventListener()` et `removeEventListener()` :

Ce sont des méthodes utilisées pour assigner et supprimer des gestionnaires d'événements, respectivement, en JavaScript.

* `**addEventListener()**` est utilisé pour attacher un écouteur d'événement à un élément, qui écoute un événement spécifique (par exemple, un clic ou un survol de souris). Il offre plus de flexibilité, surtout lorsque vous devez ajouter plusieurs gestionnaires au même événement.

```html
<button id="myButton">Cliquez-moi</button>
<script>
  document.getElementById("myButton").addEventListener('click', function() {
    alert('Bouton cliqué !');
  });
</script>

```

```javascript
const btn = document.getElementById('btn');

// Exemple 1 : Ajout d'écouteurs d'événements directement avec des fonctions anonymes
btn.addEventListener('click', function(e) {
    console.log("Bouton cliqué !"); // Journalise un message lorsque le bouton est cliqué
});

// Exemple 2 : Définition de fonctions séparément puis ajout d'écouteurs d'événements
function greet() {
    console.log("Bonjour !");
}
function farewell() {
    console.log("Au revoir !");
}
btn.addEventListener('mouseenter', greet); // Salue lorsque la souris entre dans le bouton
btn.addEventListener('mouseleave', farewell); // Dit au revoir lorsque la souris quitte le bouton

```

Avec `addEventListener`, vous pouvez également spécifier des options supplémentaires comme troisième argument. Certaines options courantes sont :

* `once` : Une valeur booléenne qui spécifie si l'écouteur d'événement doit être supprimé après avoir été invoqué une fois.
* `capture` : Une valeur booléenne qui spécifie si l'événement doit être capturé pendant la phase de capture. La phase de capture se produit avant la phase de remontée.

Par exemple :

```javascript
btn.addEventListener('click', handleClick, { once: true, capture: true });

```

Cela ajoutera un écouteur d'événement de clic à l'élément bouton qui est déclenché une seule fois et capture l'événement pendant la phase de capture.

* `**removeEventListener()**` est utilisé pour supprimer un écouteur d'événement précédemment attaché d'un élément. 

```html
// Exemple 1

<button id="myButton">Cliquez-moi</button>
<script>
  function handleClick() {
    alert('Bouton cliqué !');
  }

  document.getElementById("myButton").addEventListener('click', handleClick);
  // Supprimer le gestionnaire d'événement
  document.getElementById("myButton").removeEventListener('click', handleClick);
</script>

```

```javascript
// Exemple 2
// Supposons une préférence utilisateur
const allowGreetings = true;

// Suppression des écouteurs d'événements en fonction de la préférence utilisateur
if (!allowGreetings) {
    btn.removeEventListener('mouseenter', greet);
}

```

### Gestionnaires d'objets : `handleEvent`

Au lieu d'assigner une fonction comme gestionnaire d'événement, vous pouvez également assigner un objet qui a une méthode `handleEvent`. Lorsque l'événement se produit, la méthode `handleEvent` de l'objet sera appelée.

```html
<button id="myButton">Cliquez-moi</button>
<script>
  let myObject = {
    handleEvent: function(event) {
      alert('Bouton cliqué !');
    }
  };

  document.getElementById("myButton").addEventListener('click', myObject);
</script>

```

Dans cet exemple, lorsque le bouton est cliqué, la méthode `handleEvent` de `myObject` est appelée.

### Objet Événement :

Lorsque un événement se produit, le navigateur crée un objet événement qui contient des informations sur l'événement, telles que le type d'événement, l'élément cible, et toute donnée supplémentaire. 

Cet objet est passé en argument à la fonction de gestionnaire d'événement qui peut être accédé au sein de la fonction de rappel d'un écouteur d'événement.

```javascript
element.addEventListener('click', function(event) {
    console.log(event.type); // Sortie : "click"
    console.log(event.target); // Sortie : L'élément qui a été cliqué
     // Nous pouvons accéder à plus de propriétés comme event.clientX, event.clientY, etc.
});
```

### Propagation des événements :

Les événements dans le DOM peuvent se propager à travers l'arborescence DOM en deux phases : la phase de capture et la phase de remontée. 

Lorsque un événement se produit sur un élément, comme un clic ou une pression de touche, le navigateur doit décider quels éléments doivent être notifiés de l'événement. 

La capture et la remontée d'événements décrivent l'ordre dans lequel les éléments sont notifiés de l'événement. Comprendre la propagation des événements est important lorsque l'on traite avec des éléments imbriqués et la délégation d'événements.

1. **Phase de capture** : Dans la phase de capture, l'événement commence depuis le haut de la hiérarchie DOM (généralement l'élément `<html>`) et descend jusqu'à l'élément cible. Pendant cette phase, les gestionnaires d'événements attachés avec `addEventListener` et l'option `capture` définie sur `true` sont déclenchés. Ces gestionnaires sont exécutés avant que l'événement n'atteigne l'élément cible.
2. **Phase cible** : Une fois que l'événement atteint l'élément cible, il entre dans la phase cible. Les gestionnaires d'événements attachés avec `addEventListener` sans l'option `capture` (ou avec `false` comme valeur) sont déclenchés pendant cette phase. Les gestionnaires attachés dans cette phase sont exécutés lorsque l'événement cible directement l'élément.
3. **Phase de remontée** : Après la phase cible, l'événement remonte de l'élément cible au haut de la hiérarchie DOM. Pendant cette phase, les gestionnaires d'événements attachés avec `addEventListener` sans l'option `capture` (ou avec `false` comme valeur) sont à nouveau déclenchés. Les gestionnaires attachés dans cette phase sont exécutés lorsque l'événement remonte de l'élément cible.

Examinons un exemple. Considérons une `<div>` imbriquée dans une autre `<div>`. Si un événement de clic se produit sur la `<div>` interne, la phase de capture commence depuis la `<div>` externe et descend jusqu'à la `<div>` interne. Ensuite, la phase cible se produit sur la `<div>` interne, et enfin, la phase de remontée se produit de la `<div>` interne jusqu'à la `<div>` externe.

```html
<div id="outerDiv">
  Outer Div
  <div id="innerDiv">Inner Div</div>
</div>

<script>
  const outerDiv = document.getElementById('outerDiv');
  const innerDiv = document.getElementById('innerDiv');

  outerDiv.addEventListener('click', () => console.log('Capturing: Outer Div'), true);
  innerDiv.addEventListener('click', () => console.log('Target: Inner Div'));
  outerDiv.addEventListener('click', () => console.log('Bubbling: Outer Div'));
</script>

```

Comprenons la remontée d'événements en détail.

### Remontée d'événements :

La remontée d'événements est un mécanisme en JavaScript où, lorsqu'un événement se produit sur un élément, tel qu'un clic, cet événement se déclenche d'abord sur l'élément cible puis "remonte" à travers ses éléments ancêtres jusqu'à la racine du document (généralement `<html>`). Cela déclenche le même événement sur chaque ancêtre le long du chemin. Voici un exemple :

```html
<form onclick="alert('form')">
  FORM
  <div onclick="alert('div')">
    DIV
    <p onclick="alert('p')">P</p>
  </div>
</form>

```

Si vous cliquez sur l'élément `<p>`, l'événement de clic se déclenchera d'abord sur l'élément `<p>`, puis sur le `<div>`, et enfin sur le `<form>`. Cela est dû au fait que l'événement remonte à travers chaque élément parent dans la hiérarchie DOM.

**`event.target`** vs. `this` :

* `event.target` fait référence à l'élément qui a initié l'événement. Il reste le même tout au long du processus de remontée. Dans l'exemple ci-dessus, si vous cliquez sur l'élément `<p>`, `event.target` sera l'élément `<p>`.
* `this` (ou `event.currentTarget`) fait référence à l'élément actuel auquel le gestionnaire d'événement est attaché. Dans l'exemple ci-dessus, si le gestionnaire d'événement est attaché au `<form>`, `this` sera l'élément `<form>`.

#### Comment arrêter la remontée d'événements :

Parfois, vous pouvez vouloir empêcher l'événement de remonter plus loin. Vous pouvez le faire en utilisant la méthode `event.stopPropagation()`. Cette méthode arrête l'événement de se propager aux éléments parents.

```html
<body onclick="alert('la remontée n\'atteint pas ici')">
  <button onclick="event.stopPropagation()">Cliquez ici</button>
</body>

```

Dans cet exemple, cliquer sur le bouton ne déclenchera pas l'`alert` sur l'élément body car `event.stopPropagation()` est appelé dans le gestionnaire d'événement de clic du bouton.

`event.stopImmediatePropagation()` est similaire à `event.stopPropagation()`, mais empêche également les autres gestionnaires sur l'élément actuel de s'exécuter.

### Délégation d'événements :

La délégation d'événements est une technique qui vous permet de gérer les événements plus efficacement en attachant un seul écouteur d'événement à un élément parent au lieu d'attacher plusieurs écouteurs d'événement à des éléments enfants individuels. Cela est particulièrement utile lorsque vous avez un grand nombre d'éléments similaires qui nécessitent la même logique de gestion d'événement.

```javascript
parentElement.addEventListener('click', function(event) {
    if (event.target.classList.contains('childElement')) {
        // Action à effectuer lorsqu'un élément enfant est cliqué
    }
});

```

```javascript
<!-- Exemple : Délégation d'événement -->
<ul id="myList">
    <li>Élément 1</li>
    <li>Élément 2</li>
    <li>Élément 3</li>
</ul>

<script>
    // Ajout d'un écouteur d'événement de clic à l'élément parent ul
    document.getElementById("myList").addEventListener("click", function(event) {
        // Vérification si l'élément cliqué est un li
        if (event.target.tagName === "LI") {
            // Code à exécuter lorsqu'un li est cliqué
            console.log("Élément cliqué :", event.target.textContent);
        }
    });
</script>

```

Cette approche réduit le nombre d'écouteurs d'événement et améliore les performances.

## Conclusion

Le DOM, ou Document Object Model, est une interface qui représente la structure des documents HTML. Il sert de pont entre le code JavaScript et le navigateur, permettant la manipulation des éléments HTML, des styles, des attributs et la gestion des événements. 

L'API DOM fournit des méthodes et des propriétés pour interagir avec l'arborescence DOM. Exemples : `querySelector`, `addEventListener`, `createElement`, `innerHTML`, `textContent`, etc.

Grâce à la manipulation du DOM, les développeurs peuvent changer dynamiquement divers aspects d'une page web, y compris le contenu textuel, les attributs HTML et la structure du document lui-même (par exemple, insérer, mettre à jour ou supprimer des éléments HTML).

Les frameworks et bibliothèques JavaScript comme React utilisent souvent les capacités de manipulation du DOM pour gérer et mettre à jour efficacement les interfaces utilisateur. Cela permet aux développeurs de créer des applications web complexes avec des expériences utilisateur interactives et réactives.

Pour en savoir plus sur le DOM, voici quelques ressources que vous pouvez consulter :

Tout d'abord, j'ai écrit un article de suivi, que vous pouvez trouver ici : 
[Gestion des formulaires côté client avec JavaScript](#https://www.freecodecamp.org/news/form-validation-in-javascript/).

Vous pouvez également lire plus d'informations dans les articles suivants :

* [Cycle de vie des événements DOM et chargement efficace des scripts](https://www.samyakinfo.tech/blog/document-and-resource-loading)
* Le [manuel de manipulation du DOM JavaScript](https://www.freecodecamp.org/news/the-javascript-dom-manipulation-handbook/)
* La [documentation web MDN](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model)
* [Meilleures pratiques de manipulation du DOM JavaScript](https://www.freecodecamp.org/news/dom-manipulation-best-practices/)
* [Manipulation du DOM JS en espagnol - cours complet](https://www.freecodecamp.org/news/learn-javascript-for-dom-manipulation-in-spanish-course-for-beginners/)