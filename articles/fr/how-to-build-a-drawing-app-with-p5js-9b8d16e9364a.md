---
title: Comment créer une application de dessin avec p5js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-15T15:53:42.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-drawing-app-with-p5js-9b8d16e9364a
coverImage: https://cdn-media-1.freecodecamp.org/images/0*YgE7CTX63DNOO6P6.png
tags:
- name: coding
  slug: coding
- name: creativity
  slug: creativity
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment créer une application de dessin avec p5js
seo_desc: 'By Florin Pop

  The theme for week #5 of the Weekly Coding Challenge is:

  Creating a Drawing Application

  This is the first application that we are building in the #weeklyCodingChallenge
  program. So far we have built smaller projects, so this is pretty e...'
---

Par Florin Pop

Le **thème** pour la semaine #5 du [Défi de Codage Hebdomadaire](https://www.florin-pop.com/blog/2019/03/weekly-coding-challenge/) est :

### Créer une Application de Dessin

C'est la première application que nous construisons dans le programme #weeklyCodingChallenge. Jusqu'à présent, nous avons construit des projets plus petits, donc c'est assez excitant si vous me demandez ! ?

Dans cet article, nous utiliserons p5js, une bibliothèque de dessin, pour construire une [Application de Dessin](https://codepen.io/FlorinPop17/full/VNYyZQ) :

Consultez le CodePen ici :

%[https://codepen.io/FlorinPop17/pen/VNYyZQ]

Si vous souhaitez en savoir plus sur p5js et ce qu'il fait, vous pouvez visiter leur [site officiel](http://p5js.org/). Basiquement, je l'utilise parce qu'il fonctionne très bien sur l'élément [canvas](https://www.w3schools.com/html/html5_canvas.asp) du navigateur en fournissant une API claire.

### Le HTML

Comme vous pouvez le remarquer dans l'exemple ci-dessus, sur le côté gauche de l'écran, nous avons une `.sidebar`. Nous y mettrons nos 'outils' - un sélecteur de `couleur`, un sélecteur de `poids` et le bouton `effacer` (icône de poubelle) :

```html
<div class="sidebar">
    <ul>
        <li>
            <label for="color">Couleur :</label>
            <input type="color" id="color" />
        </li>
        <li>
            <label for="weight">Trait :</label>
            <input type="number" id="weight" min="2" max="200" value="3" />
        </li>
        <li>
            <button id="clear"><i class="fa fa-trash"></i></button>
        </li>
    </ul>
</div>
```

### Le CSS

En utilisant CSS, nous déplacerons la `.sidebar` et tout ce qui s'y trouve sur le côté gauche. Nous allons le styliser un peu pour le rendre plus joli (rien de fancy, du CSS basique) :

```css
.sidebar {
    background-color: #333;
    box-shadow: 0px 0px 10px rgba(30, 30, 30, 0.7);
    color: #fff;
    position: absolute;
    left: 0;
    top: 0;
    height: 100vh;
    padding: 5px;
    z-index: 1000;
}

.sidebar ul {
    display: flex;
    justify-content: center;
    align-items: flex-start;
    flex-direction: column;
    list-style-type: none;
    padding: 0;
    margin: 0;
    height: 100%;
}

.sidebar ul li {
    padding: 5px 0;
}

.sidebar input,
.sidebar button {
    text-align: center;
    width: 45px;
}

.sidebar li:last-of-type {
    margin-top: auto;
}

.sidebar button {
    background-color: transparent;
    border: none;
    color: #fff;
    font-size: 20px;
}

.sidebar label {
    display: block;
    font-size: 12px;
    margin-bottom: 3px;
}
```

Maintenant, la partie **importante**...

### Le JS / P5JS

Comme vous l'avez peut-être remarqué, nous n'avons pas ajouté d'élément `canvas` à notre HTML puisque p5js le créera pour nous.

Il y a deux fonctions importantes que nous utiliserons de la bibliothèque [p5js](http://p5js.org/) :

* [setup](http://p5js.org/reference/#/p5/setup) — est appelée une fois lorsque le programme démarre. Elle est utilisée pour définir les propriétés initiales de l'environnement telles que la taille de l'écran et la couleur de fond.
* [draw](http://p5js.org/reference/#/p5/draw) — est appelée directement après `setup()`. La fonction `draw()` exécute continuellement les lignes de code contenues dans son bloc.

```js
function setup() {
    // créer un canvas qui est en pleine largeur et hauteur
    createCanvas(window.innerWidth, window.innerHeight);

    // Ajouter un fond blanc au canvas
    background(255);
}

function draw() {}
```

Avant de continuer, arrêtons-nous un moment pour voir ce que nous voulons accomplir.

Donc, basiquement, nous voulons ajouter un écouteur d'événement `mousepressed` au `canvas` qui commencera à 'dessiner' une forme à l'intérieur tant que le `mouseIsPressed`.

Nous créerons un tableau de points que nous utiliserons pour créer un `path` (ou une forme) en utilisant les méthodes [beginShape](http://p5js.org/reference/#/p5/beginShape) et [endShape](http://p5js.org/reference/#/p5/endShape) pour dessiner cette forme à l'intérieur du canvas. La forme sera construite en connectant une série de sommets (voir [vertex](http://p5js.org/reference/#/p5/vertex) pour plus d'informations).

Comme nous voulons que cette forme soit _redessinée_ à chaque fois, nous mettrons ce code à l'intérieur de la méthode `draw` :

```js
const path = [];

function draw() {
    // désactiver le remplissage de la géométrie - fonction p5js
    noFill();

    if (mouseIsPressed) {
        // Stocker l'emplacement de la souris
        const point = {
            x: mouseX,
            y: mouseY
        };
        path.push(point);
    }

    beginShape();
    path.forEach(point => {
        // créer un sommet à l'emplacement spécifié
        vertex(point.x, point.y);
    });
    endShape();
}
```

Comme vous pouvez le voir, p5js a un indicateur [mouseIsPressed](http://p5js.org/reference/#/p5/mouseIsPressed) que nous pouvons utiliser pour détecter lorsque les boutons de la souris sont pressés.

Tout semble bien jusqu'à présent, mais il y a un **gros** problème. Une fois que le bouton de la souris est relâché et que nous essayons de dessiner une autre forme, le dernier point de la forme précédente sera connecté au premier point de la nouvelle forme. Ce n'est définitivement pas ce que nous voulons, donc nous devons changer un peu notre approche.

Au lieu d'avoir un seul tableau de points (le tableau path), nous créerons un `pathsarray` et nous allons stocker tous les `paths` à l'intérieur. Basiquement, nous aurons un tableau double avec des points. De plus, pour cela, nous devrons garder une trace du `currentPath` tant que la souris est encore pressée. Nous réinitialiserons ce tableau une fois que le bouton de la souris sera pressé à nouveau. Confus ? ? Regardons le code et je parie que cela deviendra plus clair :

```js
const paths = [];
let currentPath = [];

function draw() {
    noFill();

    if (mouseIsPressed) {
        const point = {
            x: mouseX,
            y: mouseY
        };
        // Ajout du point au tableau `currentPath`
        currentPath.push(point);
    }

    // Boucle sur tous les paths et dessin de tous les points à l'intérieur
    paths.forEach(path => {
        beginShape();
        path.forEach(point => {
            stroke(point.color);
            strokeWeight(point.weight);
            vertex(point.x, point.y);
        });
        endShape();
    });
}

// Lorsque la souris est pressée, cet événement se déclenche
function mousePressed() {
    // Nettoyer le currentPath
    currentPath = [];

    // Pousser le path à l'intérieur du tableau `paths`
    paths.push(currentPath);
}
```

J'ai également ajouté quelques commentaires dans le code ci-dessus, assurez-vous de les vérifier.

La fonction [mousePressed](http://p5js.org/reference/#/p5/mousePressed) _est appelée une fois après chaque fois qu'un bouton de la souris est pressé_ — du p5js ! ?

Super ! Maintenant nous pouvons dessiner des formes individuelles dans notre canvas ! ?

La dernière chose à faire est de _connecter_ ces boutons que nous avons créés dans le HTML et d'utiliser les valeurs qui s'y trouvent pour styliser la forme :

```js
const colorInput = document.getElementById('color');
const weight = document.getElementById('weight');
const clear = document.getElementById('clear');

function draw() {
    noFill();

    if (mouseIsPressed) {
        const point = {
            x: mouseX,
            y: mouseY,
            // stocker la couleur et les poids fournis par les entrées pour chaque point
            color: colorInput.value,
            weight: weight.value
        };
        currentPath.push(point);
    }

    paths.forEach(path => {
        beginShape();
        path.forEach(point => {
            // utiliser la couleur et le poids pour styliser le trait
            stroke(point.color);
            strokeWeight(point.weight);
            vertex(point.x, point.y);
        });
        endShape();
    });
}

clear.addEventListener('click', () => {
    // Supprimer tous les paths
    paths.splice(0);

    // Effacer le fond
    background(255);
});
```

Et avec cela, nous avons terminé notre petite application ! Hourra ! ?

### Le code JS complet

```js
const colorInput = document.getElementById('color');
const weight = document.getElementById('weight');
const clear = document.getElementById('clear');
const paths = [];
let currentPath = [];

function setup() {
    createCanvas(window.innerWidth, window.innerHeight);
    background(255);
}

function draw() {
    noFill();

    if (mouseIsPressed) {
        const point = {
            x: mouseX,
            y: mouseY,
            color: colorInput.value,
            weight: weight.value
        };
        currentPath.push(point);
    }

    paths.forEach(path => {
        beginShape();
        path.forEach(point => {
            stroke(point.color);
            strokeWeight(point.weight);
            vertex(point.x, point.y);
        });
        endShape();
    });
}

function mousePressed() {
    currentPath = [];
    paths.push(currentPath);
}

clear.addEventListener('click', () => {
    paths.splice(0);
    background(255);
});
```

Assurez-vous également d'importer le fichier `p5js` dans votre html avant d'importer ce fichier `js`.

### Conclusion

J'espère que vous avez aimé cette application de dessin que nous avons construite. Il y a un tas de fonctionnalités qui pourraient être ajoutées à cette application et je vous lance le défi de laisser votre esprit créatif proposer de nouvelles idées ! ?

Et si vous pouviez sauvegarder le dessin en tant qu'image (`.png` ou `.jpg`) ? ? (vous pouvez faire cela avec la bibliothèque p5js).

Pour l'instant, nous ne vérifions que les événements de la `souris`. Peut-être pourriez-vous le faire fonctionner sur mobile également, en découvrant les événements `tactiles` ? Le ciel est la limite avec la quantité de fonctionnalités qui pourraient être ajoutées à cette application !

J'adorerais voir ce que vous allez construire ! Tweetez-moi [@florinpop1705](https://twitter.com/florinpop1705) avec votre création !

Vous pourriez également aimer l'un des autres défis du programme Weekly Coding Challenge. Découvrez-les [ici](https://www.florin-pop.com/blog/2019/03/weekly-coding-challenge/).

À la prochaine ! Bon codage ! ?

_Publié à l'origine sur [www.florin-pop.com](https://www.florin-pop.com/blog/2019/04/drawing-app-built-with-p5js/)._