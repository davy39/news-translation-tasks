---
title: Qu'est-ce que le DOM ? Un guide des coulisses
subtitle: ''
author: Kedar Makode
co_authors: []
series: null
date: '2022-09-30T14:50:00.000Z'
originalURL: https://freecodecamp.org/news/what-is-dom-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/What-is-DOM-and-Events--in-JavaScipt--2-.png
tags:
- name: Document Object Model
  slug: document-object-model
- name: DOM
  slug: dom
- name: JavaScript
  slug: javascript
seo_title: Qu'est-ce que le DOM ? Un guide des coulisses
seo_desc: 'Understanding how the DOM and events work in JavaScript is key if you want
  to be an effective front end developer.

  In this article, you''ll learn what the DOM is and how it works.

  What is the DOM?

  DOM stands for Document Object Model. It''s the interfa...'
---

Comprendre le fonctionnement du DOM et des événements en JavaScript est essentiel si vous voulez être un développeur front-end efficace.

Dans cet article, vous apprendrez ce qu'est le DOM et comment il fonctionne.

## Qu'est-ce que le DOM ?

DOM signifie Document Object Model. C'est l'interface entre JavaScript et le navigateur web.

Grâce au DOM, vous pouvez écrire du JavaScript pour créer, modifier et supprimer des éléments HTML, définir des styles, des classes et des attributs, ainsi qu'écouter et répondre à des événements.

L'arborescence du DOM est générée à partir d'un document HTML, avec lequel vous pouvez ensuite interagir. Le DOM est une API très complexe qui possède des méthodes et des propriétés pour interagir avec l'arborescence du DOM.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/Frame-70-1.png align="left")

*Illustration du DOM*

Vous pouvez visualiser l'arborescence du DOM [ici](https://fritscher.ch/dom-css/).

## Comment fonctionne le DOM – Dans les coulisses

Le DOM est organisé de manière très ingénieuse. L'élément parent est appelé l'EventTarget. Vous pouvez mieux comprendre son fonctionnement à l'aide du schéma ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2022/09/DOM-behind-the-scene-1.png align="left")

L'interface EventTarget est implémentée par des objets qui peuvent recevoir des événements et peuvent avoir des écouteurs pour ceux-ci. En d'autres termes, toute cible d'événements implémente les trois méthodes associées à cette interface. **Element**, et ses enfants, ainsi que **Document** et **Window** sont les cibles d'événements les plus courantes, mais d'autres objets peuvent également être des cibles d'événements.

Window représente la fenêtre du navigateur. Tous les objets, fonctions et variables JavaScript globaux deviennent automatiquement des membres de l'objet window. Les variables globales sont des propriétés de l'objet window. Les fonctions globales sont des méthodes de l'objet window. Même l'objet document (du DOM HTML) est une propriété de l'objet window.

```js
window.document.getElementById("header");

// Les deux sont identiques

document.getElementById("header");
```

Les nœuds (Nodes) se trouvent dans le DOM, alias Document Object Model. Dans le DOM, toutes les parties du document, telles que les éléments, les attributs, le texte, etc., sont organisées dans une structure hiérarchique en forme d'arbre composée de parents et d'enfants. Ces parties individuelles du document sont appelées nœuds.

Le Node dans le schéma ci-dessus est représenté par un objet JavaScript. Nous travaillons principalement avec le document qui possède les méthodes les plus couramment utilisées comme document.querySelector(), document.getElementById(), et ainsi de suite.

Maintenant, nous allons jeter un œil au document.

## Comment sélectionner, créer et supprimer des éléments à l'aide du DOM

Grâce au DOM, nous pouvons sélectionner, supprimer et créer des éléments en JavaScript.

### Comment sélectionner des éléments

Il existe plusieurs façons de sélectionner des éléments HTML en JavaScript. Voici les méthodes que nous allons examiner ici :

* document.getElementById();
    
* document.getElementByClassName();
    
* document.getElementByTagName();
    
* document.querySelector();
    
* document.querySelectorAll();
    

#### Comment utiliser la méthode `document.getElementById()`

La méthode `getElementById()` renvoie un élément dont l'id correspond à une chaîne de caractères transmise. Étant donné que les ids des éléments HTML sont censés être uniques, c'est un moyen plus rapide de sélectionner un élément avec des ids.

Exemple :

```js
const ele = document.getElementById("IDName");
console.log(ele); // Cela affichera l'élément HTML complet
```

#### Comment utiliser la méthode `document.getElementByClassName()`

La méthode `document.getElementByClassName()` renvoie une `HTMLCollection` d'éléments qui correspondent au nom de classe transmis. Nous pouvons rechercher plusieurs noms de classe en transmettant les noms de classe séparés par des espaces. Elle renverra une HTMLCollection en direct (live).

Alors, que signifie le fait que la HTMLCollection soit « en direct » ? Eh bien, cela signifie qu'une fois que nous obtenons la HTMLCollection pour un nom de classe, si nous ajoutons un élément avec le même nom de classe, la HTMLCollection est mise à jour automatiquement.

Exemple :

```js
const ele = document.getElementByClassName("ClassName");
console.log(ele); // Affiche la HTMLCollection en direct
```

#### Comment utiliser la méthode `document.getElementByTagName();`

La méthode `document.getElementByTagName()` renvoie la HTMLCollection des éléments qui correspondent au nom de balise transmis. Elle peut être appelée sur n'importe quel élément HTML. Elle renvoie une HTMLCollection qui est une collection en direct.

Exemple :

```js
const paragraph = document.getElementByTagName("p");
const heading = document.getElementByTagName("h1");

console.log(paragraph); // HTMLCollection de l'élément p
console.log(heading); // HTMLCollection de l'élément h1
```

#### Comment utiliser la méthode document.querySelector()

La méthode `document.querySelector()` renvoie le premier élément qui correspond au sélecteur transmis. Ici, nous pouvons passer un nom de classe, un id et un nom de balise. Jetez un œil à l'exemple ci-dessous :

```js
const id = document.querySelector("#idname"); // en utilisant l'id
const classname = document.querySelector(".classname"); // en utilisant la classe
const tag = document.querySelector("p"); // en utilisant le nom de la balise
```

Règles de sélection :

* Lors de la sélection à l'aide d'une classe, utilisez un point (.) au début. Par exemple (".classname")
    
* Lors de la sélection à l'aide d'un id, utilisez un dièse (#) au début. Par exemple ("#id")
    
* Lors de la sélection à l'aide d'une balise, sélectionnez simplement directement. Par exemple ("p")
    

#### Comment utiliser la méthode document.querySelectorAll()

La méthode `document.querySelectorAll()` est une extension de la méthode `querySelector`. Cette méthode renvoie **tous** les éléments qui correspondent au sélecteur transmis. Elle renvoie la collection Nodelist qui n'est pas en direct.

```js
const ele = document.querySelectorAll("p");
console.log(ele); // renvoie une collection nodelist de la balise p
```

**REMARQUE** : HTMLCollection est une collection en direct, tandis que la collection Nodelist est une collection statique.

### Comment créer des éléments

Vous pouvez créer des éléments HTML en JavaScript et les ajouter au HTML dynamiquement. Vous pouvez créer n'importe quel élément HTML avec `document.createElement()` en passant le nom de la balise entre parenthèses.

Après avoir créé l'élément, vous pouvez ajouter le nom de la classe, des attributs et du contenu textuel à cet élément.

**Voici un exemple :**

```js
const ele = document.createElement("a");
ele.innerText = "Click Me";
ele.classList.add("text-left");
ele.setAttribute("href", "www.google.com");

// mise à jour de l'élément existant dans le HTML
document.querySelector(".links").prepend(ele);
document.querySelector(".links").append(ele);
document.querySelector(".links").befor(ele);
document.querySelector(".links").after(ele);

// Similaire à la balise d'ancrage ci-dessous
// <a href="www.google.com">Click Me</a>
```

Dans l'exemple ci-dessus, nous avons créé une balise d'ancrage en JavaScript et ajouté des attributs et un nom de classe à cette balise. Nous avons quatre méthodes dans l'exemple ci-dessus pour mettre à jour l'élément créé dans le HTML.

* prepend() : insère les données au début de son premier élément enfant.
    
* append() : insère les données ou le contenu à l'intérieur d'un élément au dernier index.
    
* before() : insère les données avant l'élément sélectionné.
    
* after() : place l'élément après l'élément spécifié. Ou vous pouvez dire qu'il insère des données à l'extérieur d'un élément (faisant du contenu son frère) dans l'ensemble des éléments correspondants.
    

### Comment supprimer des éléments

Nous savons comment créer des éléments en JavaScript et les injecter dans le HTML. Mais que faire si nous voulons supprimer des éléments existants dans le HTML ? C'est facile – il nous suffit d'utiliser la méthode `remove()` sur cet élément.

**Voici un exemple :**

```js
const ele = document.querySelector("p");

// Cela supprimera ele lors d'un clic
ele.addEventListner('click', function(){
	ele.remove();
})
```

## Comment manipuler le CSS depuis JavaScript

Nous savons comment manipuler le HTML depuis JavaScript. Maintenant, nous allons apprendre à manipuler le CSS depuis JavaScript. Cela peut vous aider à modifier le style de vos pages web de manière dynamique.

Par exemple, si vous cliquez sur un élément, sa couleur d'arrière-plan devrait changer. Cela est possible en manipulant le CSS depuis JavaScript.

**Voici un exemple de syntaxe :**

```js
const ele = document.querySelector("desired element");

ele.style.propertyName = value;

// Par ex. -
ele.style.color = red;
```

Lors de la modification des propriétés CSS à l'aide de JavaScript, vous devez vous assurer que chaque fois qu'il y a un `-` dans le CSS, vous mettez la lettre suivante en majuscule. Par exemple, en CSS vous écririez `background-color`, mais en JavaScript, `backgroundColor` (avec un C majuscule).

**Voici un exemple :**

```js
const ele = document.querySelector("div");
ele.style.backgroundColor = "red";
```

Supposons maintenant que vous ayez déjà écrit du CSS pour votre projet et que vous souhaitiez ajouter des classes à l'aide de JavaScript. Nous pouvons le faire en utilisant `classList` en JavaScript.

**Voici un exemple :**

```js
const ele = document.querySelector(".link");
ele.classList.add("bg-red"); // ajoute la classe bg-red à la liste des classes existantes
ele.classList.remove("pb-4");// supprime la classe pb-4 de la liste des classes existantes
ele.classList.toggle("bg-green"); // bascule la classe bg-green dans la liste des classes existantes, ce qui signifie que si elle existe déjà, elle sera supprimée, et si elle n'existe pas, elle sera ajoutée.
```

Lorsque nous utilisons classList, cela ajoute, supprime ou bascule des classes directement sur l'élément. C'est comme une mise à jour avec les classes existantes.

Contrairement à element.className, cela supprime toutes les classes existantes et ajoute la classe donnée.

**Voici un exemple :**

```js
const ele = document.querySelector(".link");
ele.classList.add("bg-red"); // ajoute la classe bg-red à la liste des classes existantes
ele.classList.remove("pb-4");// supprime la classe pb-4 de la liste des classes existantes

ele.className = "p-10"; // Maintenant, cela supprimera toutes les classes existantes et ajoutera seulement la classe "p-10" à l'élément.
```

## Comment utiliser les gestionnaires d'événements

Le changement d'état d'un objet est connu sous le nom d'**Événement**. Le processus de réaction aux événements est appelé **Gestion d'événements**.

Les événements se produisent lorsqu'un utilisateur fait quelque chose comme cliquer, survoler un élément, appuyer sur une touche, etc. Ainsi, lorsqu'un événement se produit et que vous souhaitez effectuer une certaine action ou manipuler quoi que ce soit, vous utilisez des gestionnaires d'événements pour déclencher cet événement.

Nous utilisons des gestionnaires d'événements pour exécuter un certain code lorsque cet événement particulier se produit. Il existe de nombreux gestionnaires d'événements en JavaScript (voici une [liste de ceux-ci](https://way2tutorial.com/html/html5_events_handler_list.php)), mais vous utilisez le même processus pour ajouter des gestionnaires d'événements à n'importe quel élément.

**Voici la syntaxe :**

```js
const ele = document.querySelector("a");

ele.addEventListner("event", function(){
	// fonction de rappel
});
```

Quelques événements que vous pouvez utiliser :

* click
    
* mouseover
    
* mouseout
    
* keypress
    
* keydown
    

**Et voici un exemple d'utilisation de l'événement "click" :**

```js
const ele = document.querySelector("a");

ele.addEventListner("click", function(){
	ele.style.backgroundColor = "pink";
});
```

## Propagation d'événements : Bubbling et Capturing

La propagation d'événements détermine dans quel ordre les éléments reçoivent l'événement ou les événements. Il existe deux façons de gérer cet ordre de propagation des événements dans le DOM : l'Event Bubbling et l'Event Capturing.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/Frame-71-1.png align="left")

### Qu'est-ce que l'Event Bubbling ?

Lorsqu'un événement se produit sur un composant, il exécute d'abord le gestionnaire d'événements sur celui-ci, puis sur son composant parent, puis remonte jusqu'aux autres composants ancêtres.

Par défaut, tous les gestionnaires d'événements suivent cet ordre, de l'événement du composant central à l'événement du composant le plus externe.

### Qu'est-ce que l'Event Capturing ?

C'est l'opposé du bubbling. Le gestionnaire d'événements agit d'abord sur son composant parent, puis sur le composant où il était réellement censé se déclencher.

En résumé, cela signifie que l'événement est d'abord capturé par l'élément le plus externe et propagé vers les éléments internes. On l'appelle aussi « trickle down » (descente).

**Essayons l'exemple ci-dessous :**

```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Exemple</title>
    <style>
        nav{
            display: flex;
            justify-content: center;
            padding: 30px;
        }

        nav li{
            list-style: none;
            padding: 5px;
        }

        nav li a{
            text-decoration: none;
            padding: 20px;
        }
    </style>
</head>
<body>
    
    <div>
        <nav>
            <li><a href="#">Accueil</a></li>
            <li><a href="#">À propos</a></li>
            <li><a href="#">Contact</a></li>
        </nav>
    </div>

    <script>
        const navbar = document.querySelector("nav");
        navbar.addEventListener('click', function(){
            navbar.style.backgroundColor="green"
        });

        const anchor = document.querySelector("a");
        anchor.addEventListener("click", function(){
            anchor.style.backgroundColor="pink";
        })
    </script>
</body>
</html>
```

Ce code nous donne ce qui suit :

![Image](https://www.freecodecamp.org/news/content/images/2022/09/Screenshot-2022-09-26-142920.png align="left")

Maintenant, étudiez attentivement l'exemple ci-dessus. J'ai ajouté un écouteur d'événement à la balise `nav` et à la balise `anchor`. Lorsque vous cliquez sur nav, la couleur d'arrière-plan change en vert. Lorsque vous cliquez sur la balise d'ancrage, la couleur d'arrière-plan change en rose.

Mais lorsque vous cliquez sur la balise d'ancrage, la couleur d'arrière-plan de l'ancre ainsi que celle de nav changent. Cela est dû à l'**event bubbling.**

**C'est ce qui se passe lorsque vous cliquez uniquement sur l'élément nav :**

![Image](https://www.freecodecamp.org/news/content/images/2022/09/Frame-72--1-.png align="left")

***C'est ce qui se passe lorsque vous cliquez uniquement sur l'élément nav.***

**C'est ce qui se passe lorsque vous cliquez uniquement sur l'élément d'ancrage :**

![Image](https://www.freecodecamp.org/news/content/images/2022/09/Frame-73--1-.png align="left")

***C'est ce qui se passe lorsque vous cliquez uniquement sur l'élément d'ancrage***

Pour arrêter la propagation de l'événement, nous pouvons utiliser `stoppropagation()` sur l'écouteur d'événement à cause duquel la propagation de l'événement se produit. Cela empêchera l'écouteur d'événement de l'élément nav de s'activer dans l'exemple ci-dessus.

```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Exemple</title>
    <style>
        nav{
            display: flex;
            justify-content: center;
            padding: 30px;
        }

        nav li{
            list-style: none;
            padding: 5px;
        }

        nav li a{
            text-decoration: none;
            padding: 20px;
        }
    </style>
</head>
<body>
    
    <div>
        <nav>
            <li><a href="#">Accueil</a></li>
            <li><a href="#">À propos</a></li>
            <li><a href="#">Contact</a></li>
        </nav>
    </div>

    <script>
        const navbar = document.querySelector("nav");
        navbar.addEventListener('click', function(){
            navbar.style.backgroundColor="green"
        });

        const anchor = document.querySelector("a");
        anchor.addEventListener("click", function(e){
            e.stopPropagation();
            anchor.style.backgroundColor="pink";
        })
    </script>
</body>
</html>
```

## Comment parcourir le DOM

« Un bon développeur JavaScript doit savoir comment parcourir le DOM — c’est **l’acte de sélectionner un élément à partir d’un autre élément.** » – [Zell Liew](https://zellwk.com/blog/dom-traversals/)

Nous allons maintenant voir pourquoi parcourir le DOM est préférable à l'utilisation de la méthode `document.querySelector()`, et comment le parcourir comme un pro.

Il existe 3 façons de parcourir le DOM :

* Vers le haut
    
* Vers le bas
    
* Latéralement
    

### Comment parcourir le DOM vers le haut

Il existe deux méthodes qui vous aident à parcourir le DOM vers le haut :

* parentElement
    
* closest
    

`parentElement` est une propriété qui sélectionne l'élément parent, comme ceci :

```js
const ele = document.querySelector("a");
console.log(ele.parentElement); // <div>
```

Le parentElement est idéal pour sélectionner un niveau au-dessus. Mais `closest` vous permet de trouver un élément qui peut se trouver plusieurs niveaux au-dessus de l'élément actuel. `closest` vous permet de sélectionner l'élément ancêtre le plus proche qui correspond à un sélecteur.

Voici un exemple d'utilisation de `closest` :

```html
<article id="target">
    <h1 id="heading">C'est le titre principal</h1>
    <div id="outer-div">
        C'est la div extérieure
        <div id="inner-div">C'est la div intérieure</div>
    </div>
</article>
```

```js
const innerDiv = document.querySelector("#inner-div");
console.log(innerDiv.closest("#target")); // article#target
```

Dans le code ci-dessus, nous essayons d'obtenir l'élément le plus proche de `.heading` qui a une classe de `.demo`.

### Comment parcourir le DOM vers le bas

Nous pouvons parcourir vers le bas en utilisant la méthode `children` sur un sélecteur. Avec children, vous pouvez sélectionner l'enfant direct de l'élément sélectionné.

**Voici un exemple :**

```html
<div>
    <a href="#">Lien-1</a>
    <a href="#">Lien-2</a>
    <a href="#">Lien-3</a>
    <a href="#">Lien-4</a>
</div>
```

```js
const ele = document.querySelector("div");
const child = ele.children;

console.log(child); // donne une HTMLCollection
// 4 éléments à l'intérieur de la div
```

### Comment parcourir le DOM latéralement

Il est très intéressant de parcourir le DOM latéralement. Il existe principalement deux méthodes que nous pouvons utiliser :

* previousElementSibling
    
* nextElementSibling
    

À l'aide de la méthode `previousElementSibling`, nous pouvons sélectionner les éléments précédents dans le HTML comme ceci :

```html
<div>
    <a href="#">Lien-1</a>
    <h1>Titre</h1>
</div>
```

```js
const ele = document.querySelector("h1");
console.log(ele.previousElementSibling); // <a href="#">Lien-1</a>
```

À l'aide de `nextElementSibling`, nous pouvons sélectionner l'élément suivant dans le HTML comme ceci :

```html
<div>
    <a href="#">Lien-1</a>
    <h1>Titre</h1>
</div>
```

```js
const ele = document.querySelector("a");
console.log(ele.nextElementSibling); // <h1>Titre</h1>
```

## **Conclusion**

J'espère que vous comprenez maintenant comment le DOM fonctionne en JavaScript. Merci de m'avoir lu !

Vous pouvez me suivre sur :

* [Twitter](https://twitter.com/Kedar__98)
    
* [LinkedIn](https://www.linkedin.com/in/kedar-makode-9833321ab/?originalSubdomain=in)
    
* [Instagram](https://www.instagram.com/kedar_98/)