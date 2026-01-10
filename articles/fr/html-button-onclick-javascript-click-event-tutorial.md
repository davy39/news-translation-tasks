---
title: Bouton HTML onclick – Tutoriel sur l'événement de clic JavaScript
date: '2021-08-16T17:58:05.000Z'
author: Kolade Chris
authorURL: https://www.freecodecamp.org/news/author/koladechris/
originalURL: https://freecodecamp.org/news/html-button-onclick-javascript-click-event-tutorial
posteditor: ''
proofreader: ''
co_authors: []
series: null
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/javascript-onclick.png
tags:
- name: HTML
  slug: html
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_desc: 'Whenever you visit a website, you''ll probably click on something like
  a link or button.

  Links take you to a certain part of the page, another page of the website, or another
  website entirely. Buttons, on the other hand, are usually manipulated by Jav...'
---


Chaque fois que vous visitez un site web, vous cliquez probablement sur quelque chose comme un lien ou un bouton.

<!-- more -->

Les liens vous mènent à une partie précise de la page, à une autre page du site ou à un autre site entièrement. Les boutons, en revanche, sont généralement manipulés par des événements JavaScript afin de déclencher certaines fonctionnalités.

Dans ce tutoriel, nous allons explorer deux manières différentes d'exécuter des événements de clic en JavaScript en utilisant deux méthodes distinctes.

Tout d'abord, nous examinerons le style traditionnel `onclick` que l'on utilise directement depuis la page HTML. Ensuite, nous verrons comment fonctionne l' `eventListener` "click" plus moderne, qui permet de séparer le HTML du JavaScript.

### Voici un Scrim interactif sur le bouton HTML onclick

<iframe src="https://scrimba.com/scrim/cob064720ad708e33a795aefa?pl=pz9wDSk&amp;embed=freecodecamp,mini-header" width="100%" height="420" title="Embedded content" loading="lazy"></iframe>

## Comment utiliser l'événement `onclick` en JavaScript

L'événement `onclick` exécute une certaine fonctionnalité lorsqu'un bouton est cliqué. Cela peut se produire lorsqu'un utilisateur soumet un formulaire, lorsque vous modifiez un certain contenu sur la page web, et d'autres choses de ce genre.

Vous placez la fonction JavaScript que vous souhaitez exécuter à l'intérieur de la balise ouvrante du bouton.

### Syntaxe de base de `onclick`

```
<element onclick="functionToExecute()">Click</element>
```

Par exemple :

```
<button onclick="functionToExecute()">Click</button>
```

Notez que l'attribut `onclick` est purement du JavaScript. La valeur qu'il prend, qui est la fonction que vous souhaitez exécuter, dit tout, car elle est invoquée directement dans la balise ouvrante.

En JavaScript, vous invoquez une fonction en appelant son nom, puis vous placez des parenthèses après l'identifiant de la fonction (le nom).

## Exemple d'événement `onclick`

J'ai préparé du HTML de base avec un peu de mise en forme afin que nous puissions mettre l'événement `onclick` en pratique dans un cas réel.

```
<div>
  <p class="name">freeCodeCamp</p>
  <button>Change to Blue</button>
</div>
```

Et voici le CSS pour rendre le tout esthétique, ainsi que le reste du code d'exemple :

```
 body {
   display: flex;
   align-items: center;
   justify-content: center;
   height: 100vh;
      }
p {
   font-size: 2rem;
}

button {
    padding: 7px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

button.blue {
    background-color: #3498db;
}

button.green {
    background-color: #2ecc71;
}

button.orange {
   background-color: orangered;
}
```

Ainsi, sur la page web, voici ce que nous avons : ![changeColor](https://www.freecodecamp.org/news/content/images/2021/08/changeColor.png)

Notre objectif est de changer la couleur du texte en bleu lorsque nous cliquons sur le bouton. Nous devons donc ajouter un attribut `onclick` à notre bouton, puis écrire la fonction JavaScript pour changer la couleur.

Nous devons donc apporter une légère modification à notre HTML :

```
<div>
  <p class="name">freeCodeCamp</p>
  <button onclick="changeColor()">Change to Blue</button>
</div>
```

La fonction que nous voulons exécuter est `changeColor()`. Nous devons donc l'écrire dans un fichier JavaScript, ou dans le fichier HTML à l'intérieur d'une balise `<script>`.

Si vous souhaitez écrire votre script dans un fichier JavaScript, vous devez le lier dans le HTML en utilisant la syntaxe ci-dessous :

```
<script src="path-to-javascript-file"></script>
```

Si vous souhaitez écrire le script dans un fichier HTML, placez-le simplement à l'intérieur de la balise script :

```
<script>
  // Vos Scripts
</script>
```

Maintenant, écrivons notre fonction `changeColor()`.

Tout d'abord, nous devons sélectionner l'élément que nous voulons manipuler, qui est le texte freeCodeCamp à l'intérieur de la balise `<p>`.

En JavaScript, vous faites cela avec les méthodes du DOM `getElementById()`, `getElementsByClassName()`, ou `querySelector()`. Ensuite, vous stockez la valeur dans une variable.

Dans ce tutoriel, j'utiliserai `querySelector()` car c'est plus moderne et plus rapide. J'utiliserai également `const` pour déclarer nos variables au lieu de `let` et `var`, car avec `const`, les choses sont plus sûres puisque la variable devient en lecture seule.

```
const name = document.querySelector(".name");
```

Maintenant que nous avons sélectionné le texte, écrivons notre fonction. En JavaScript, la syntaxe de base d'une fonction ressemble à ceci :

```
function funcctionName () {
    // Ce qu'il faut faire
}
```

Écrivons donc notre fonction :

```
function changeColor() {
    name.style.color = "blue";
}
```

Que se passe-t-il ?

Rappelez-vous dans le HTML que `changeColor()` est la fonction que nous allons exécuter. C'est pourquoi l'identifiant (nom) de notre fonction est défini sur `changeColor`. Si le nom ne correspond pas à ce qui est dans le HTML, cela ne fonctionnera pas.

Dans le DOM (Document Object Model, qui fait référence à l'ensemble du HTML), pour modifier tout ce qui concerne le style, vous devez écrire « style » suivi d'un point (.). Ceci est suivi de ce que vous voulez changer, qui peut être la couleur, la couleur d'arrière-plan, la taille de la police, etc.

Ainsi, à l'intérieur de notre fonction, nous prenons la variable `name` que nous avons déclarée pour obtenir notre texte freeCodeCamp, puis nous changeons la couleur en bleu.

La couleur de notre texte devient bleue chaque fois que le bouton est cliqué :

![changeColor](https://www.freecodecamp.org/news/content/images/2021/08/changeColor.gif)

Notre code fonctionne !

Nous pourrions aller un peu plus loin en changeant notre texte avec plus de couleurs :

```
<div>
      <p class="name">freeCodeCamp</p>
      <button onclick="changeColor('blue')" class="blue">Blue</button>
      <button onclick="changeColor('green')" class="green">Green</button>
      <button onclick="changeColor('orangered')" class="orange">Orange</button>
</div>
```

Ce que nous voulons faire, c'est changer le texte en bleu, vert et rouge-orangé.

Cette fois-ci, les fonctions `onclick` dans notre HTML prennent les valeurs de la couleur vers laquelle nous voulons changer le texte. Celles-ci sont appelées paramètres en JavaScript. La fonction que nous allons écrire prendra également le sien, que nous appellerons « color ».

Notre page web a un peu changé :

![changeColors](https://www.freecodecamp.org/news/content/images/2021/08/changeColors.png)

Sélectionnons donc notre texte freeCodeCamp et écrivons la fonction pour changer sa couleur en bleu, vert et rouge-orangé :

```
const name = document.querySelector(".name");

function changeColor(color) {
   name.style.color = color;
}
```

Le bloc de code dans la fonction utilise la variable `name` (où nous avons stocké notre texte freeCodeCamp), puis définit la couleur sur celle que nous avons passée dans les fonctions `changeColor()` des boutons HTML. ![changeColors](https://www.freecodecamp.org/news/content/images/2021/08/changeColors.gif)

## Comment utiliser l' `eventListener` click en JavaScript

En JavaScript, il existe plusieurs façons de faire la même chose. À mesure que JavaScript lui-même a évolué au fil du temps, nous avons commencé à avoir besoin de séparer le code HTML, CSS et JavaScript afin de respecter les bonnes pratiques.

Les écouteurs d'événements (event listeners) rendent cela possible car ils vous permettent de séparer le JavaScript du HTML. Vous pouvez également le faire avec `onclick`, mais adoptons une autre approche ici.

### Voici un scrim interactif sur les écouteurs d'événements :

<iframe src="https://scrimba.com/scrim/cof804618b5a4eff5ca0b3dff?pl=pz9wDSk&amp;embed=freecodecamp,mini-header" width="100%" height="420" title="Embedded content" loading="lazy"></iframe>

### Syntaxe de base d' `eventListener`

```
 element.addEventListener("type-of-event", functionToExecute)
```

Maintenant, changeons le texte freeCodeCamp en bleu en utilisant l' `eventListener` click.

Voici notre nouveau HTML :

```
 <div>
      <p class="name">freeCodeCamp</p>
      <button>Change Color</button>
 </div>
```

Et voici à quoi cela ressemble :

![colorChange](https://www.freecodecamp.org/news/content/images/2021/08/colorChange.png)

Cette fois-ci dans notre script, nous devons également sélectionner le bouton (pas seulement le texte freeCodeCamp). C'est parce qu'il n'y a pas de JavaScript dans la balise ouvrante de notre bouton, ce qui est une bonne chose.

Ainsi, notre script ressemble à ceci :

```
const name = document.querySelector(".name");
const btn = document.querySelector("button");

      btn.addEventListener("click", function () {
        name.style.color = "blue";
 });
```

Nous pouvons également séparer totalement notre fonction de l' `eventListener` et notre fonctionnalité restera la même :

```
btn.addEventListener("click", changeColor);
      function changeColor() {
        name.style.color = "blue";
}
```

![changeColorWithEvents](https://www.freecodecamp.org/news/content/images/2021/08/changeColorWithEvents.gif)

## Comment créer un bouton « Afficher plus » et « Afficher moins » avec JavaScript

L'une des meilleures façons d'apprendre est de réaliser des projets. Utilisons donc ce que nous avons appris sur `onclick` et l' `eventListener` "click" pour construire quelque chose.

Lorsque vous visitez un blog, vous voyez souvent d'abord des extraits d'articles. Ensuite, vous pouvez cliquer sur un bouton "lire la suite" pour afficher le reste. Essayons de faire cela.

Voici le HTML que nous utilisons :

```
 <article id="content">
      <p>
        freeCodeCamp is one of the best platforms to learn how to code.
        freeCodeCamp has a detailed curriculum that will take you from zero to
        hero in web development, software engineering, machine learning, and
        more.
      </p>

      <p>
        freeCodeCamp also has a YouTube channel containing over 1000 videos on
        web development, software engineering, machine learning, data science,
        freelance web development, database administration, and pretty much
        anything related to tech. To get updates when videos are uploaded, you
        need to subscribe to the channel and turn on notifications. You can also
        follow freeCodeCamp on Twitter, where links to well written articles and
        videos are tweeted daily.
      </p>

      <p>
        Since no one has to pay to learn how to code on freeCodeCamp,
        freeCodeCamp runs on voluntary donations from donors all around the
        world in order to pay employees and maintain servers. If you are
        generous enough consider joining the donors.
      </p>
    </article>

<button onclick="showMore()">Show more</button>
```

C'est un HTML simple avec quelques faits sur freeCodeCamp. Et il y a un bouton auquel nous avons déjà attaché un `onclick`. La fonction que nous voulons exécuter est `showMore()`, que nous écrirons bientôt.

Sans CSS, voici ce que nous avons : ![articleunstyled](https://www.freecodecamp.org/news/content/images/2021/08/articleunstyled.png)

Ce n'est pas extrêmement laid, mais nous pouvons le rendre plus beau et faire en sorte qu'il agisse comme nous le souhaitons. Voici donc le CSS que j'expliquerai ci-dessous :

```
<style>
      * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
      }

      body {
        background: #f1f1f1;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-direction: column;
      }

      article {
        width: 400px;
        background: #fff;
        padding: 20px 20px 0;
        font-size: 18px;
        max-height: 270px;
        overflow: hidden;
        transition: max-height 1s;
        text-align: justify;
        margin-top: 20px;
      }

      p {
        margin-bottom: 16px;
      }

      article.open {
        max-height: 1000px;
      }

      button {
        background: #0e0b22;
        color: #fff;
        padding: 0.6rem;
        margin-top: 20px;
        border: none;
        border-radius: 4px;
      }

      button:hover {
        cursor: pointer;
        background: #1e1d25;
      }
</style>
```

Que fait le CSS ?

Avec le sélecteur universel (`*`), nous supprimons la marge et le rembourrage (padding) par défaut attribués aux éléments afin de pouvoir ajouter nos propres marges et rembourrages.

Nous avons également défini `box-sizing` sur `border-box` afin de pouvoir inclure le rembourrage et la bordure dans la largeur et la hauteur totales de nos éléments.

Nous avons tout centré dans le corps (`body`) avec Flexbox et lui avons donné un arrière-plan gris clair.

Notre élément `<article>`, qui contient le texte, a une largeur de `400px`, un arrière-plan blanc (#fff), et un rembourrage de 20px en haut, 20 à gauche et à droite, et 0 en bas.

Les balises de paragraphe à l'intérieur ont une taille de police de 18px, puis nous leur avons donné une hauteur maximale de `270px`. En raison de la hauteur maximale de l'élément article, tout le texte ne sera pas contenu et débordera. Pour corriger cela, nous avons défini `overflow` sur `hidden` afin de ne pas afficher ce texte au début.

La propriété `transition` garantit que chaque changement se produit après 1 seconde. Tout le texte à l'intérieur de l' `article` est justifié et possède une marge supérieure de 20 pixels pour qu'il ne reste pas trop collé au haut de la page.

Parce que nous avons supprimé la marge par défaut, nos paragraphes se sont retrouvés tous serrés. Nous avons donc défini une marge inférieure de 16 pixels afin de les séparer les uns des autres.

Notre sélecteur, `article.open`, a une propriété `max-height` définie sur `1000px`. Cela signifie que chaque fois que l'élément article a une classe `open` qui lui est attachée, la hauteur maximale passera de `270px` à `1000px` pour afficher le reste de l'article. C'est possible grâce à JavaScript – notre moteur de changement.

Nous avons stylisé notre bouton avec un arrière-plan sombre et l'avons mis en blanc. Nous avons défini sa bordure sur `none` pour supprimer la bordure par défaut du HTML sur les boutons, et nous lui avons donné un `border-radius` de `4px` pour qu'il ait une bordure légèrement arrondie.

Enfin, nous avons utilisé la pseudo-classe `hover` en CSS pour changer le curseur du bouton en pointeur. La couleur d'arrière-plan change légèrement lorsqu'un utilisateur survole le bouton avec son curseur.

Et voilà – c'est le CSS.

Notre page a maintenant une meilleure apparence :

![articlestyled](https://www.freecodecamp.org/news/content/images/2021/08/articlestyled.png)

La prochaine chose que nous devons faire est d'écrire notre JavaScript afin de pouvoir voir le reste de l'article qui est caché.

Nous avons un attribut `onclick` à l'intérieur de la balise ouvrante de notre bouton prêt à exécuter une fonction `showMore()`, alors écrivons cette fonction.

Nous devons d'abord sélectionner notre article, car nous devons en afficher le reste :

```
const article = document.querySelector("#content");
```

La chose suivante que nous devons faire est d'écrire la fonction `showMore()` afin de pouvoir basculer entre voir le reste de l'article et le masquer.

```
function showMore() {
     if (article.className == "open") {
       // lire moins
       article.className = "";
       button.innerHTML = "Show more";
     } else {
       //lire plus
       article.className = "open";
       button.innerHTML = "Show less";
     }
  }
```

Que fait la fonction ?

Nous utilisons ici une instruction `if…else`. C'est une partie cruciale de JavaScript qui vous aide à prendre des décisions dans votre code si une certaine condition est remplie.

La syntaxe de base ressemble à ceci :

```
if (condition == "something") {
  // Faire quelque chose
} else {
  // Faire autre chose
}
```

Ici, si le nom de classe de l'article est égal à `open` (c'est-à-dire que nous voulons lui ajouter la classe `open`, qui a été définie à une hauteur maximale de 1000px dans le CSS), alors nous voulons voir le reste de l'article. Sinon, nous voulons que l'article revienne à l'état initial où une partie est cachée.

Nous faisons cela en lui attribuant une classe `open` dans le bloc `else`, ce qui lui permet d'afficher le reste de l'article. Ensuite, nous définissons la classe sur une chaîne vide (rien) dans le bloc `if`, ce qui le fait revenir à l'état initial.

Notre code fonctionne parfaitement avec une transition fluide : ![article](https://www.freecodecamp.org/news/content/images/2021/08/article.gif)

Nous pouvons séparer le HTML et le JavaScript et toujours utiliser `onclick`, car `onclick` est du JavaScript. Il est donc possible d'écrire cela dans un fichier JavaScript au lieu de commencer par le HTML.

```
 button.onclick = function () {
     if (article.className == "open") {
       // lire moins
       article.className = "";
       button.innerHTML = "Show more";
     } else {
       //lire plus
       article.className = "open";
       button.innerHTML = "Show less";
     }
  };
```

![articleonclick](https://www.freecodecamp.org/news/content/images/2021/08/articleonclick.gif)

Nous pouvons également le faire en utilisant un `eventListener` :

```
<article id="content">
      <p>
        freeCodeCamp is one of the best platforms to learn how to code.
        freeCodeCamp has a detailed curriculum that will take you from zero to
        hero in web development, software engineering, machine learning, and
        many more.
      </p>

      <p>
        freeCodeCamp also has a YouTube channel containing over 1000 videos on
        web development, software engineering, machine learning, data science,
        freelance web development, database administration, and pretty more
        anything related to tech. To get updates when videos are uploaded, you
        need to subscribe to the channel and turn on notifications. You can also
        follow freeCodeCamp on Twitter, where links to well written articles and
        videos are tweeted daily.
      </p>

      <p>
        Since no one has to pay to learn how to code on freeCodeCamp,
        freeCodeCamp runs on voluntary donations from donors all around the
        world in order to pay employees and maintain servers. If you are
        generous enough consider joining the donors.
      </p>
</article>

<button id="read-more">Show more</button>
```

```
 const article = document.querySelector("#content");
 const button = document.querySelector("#read-more");

button.addEventListener("click", readMore);

function readMore() {
     if (article.className == "open") {
       // Lire moins
     article.className = "";
     button.innerHTML = "Show more";
   } else {
     article.className = "open";
     button.innerHTML = "Show less";
   }
}
```

Notre fonctionnalité reste la même !

## Conclusion

J'espère que ce tutoriel vous aidera à comprendre comment fonctionne l'événement de clic en JavaScript. Nous avons exploré deux méthodes différentes ici, vous pouvez donc maintenant commencer à les utiliser dans vos projets de programmation.

Merci de votre lecture, et continuez à coder.