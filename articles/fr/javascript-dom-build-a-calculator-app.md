---
title: Tutoriel JavaScript DOM – Comment créer une application calculatrice en JS
subtitle: ''
author: Spruce Emmanuel
co_authors: []
series: null
date: '2022-09-02T15:40:00.000Z'
originalURL: https://freecodecamp.org/news/javascript-dom-build-a-calculator-app
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/Web-capture_31-8-2022_83456_localhost.jpeg
tags:
- name: DOM
  slug: dom
- name: JavaScript
  slug: javascript
seo_title: Tutoriel JavaScript DOM – Comment créer une application calculatrice en
  JS
seo_desc: 'You''re going to spend a lot of time working on webpages when using JavaScript.
  In fact, while you''re using JavaScript, the webpage is where all the exciting and
  important stuff takes place.

  A webpage is one big document for a JavaScript developer sin...'
---

Vous allez passer beaucoup de temps à travailler sur des pages web lorsque vous utilisez JavaScript. En fait, pendant que vous utilisez JavaScript, la page web est l'endroit où se déroulent toutes les choses passionnantes et importantes.

Une page web est un grand document pour un développeur JavaScript car chaque élément de la page est connecté (comme une grande famille). Tout est composé de parents (parentNodes) et d'enfants (childNodes). Le Document Object Model est le nom de cette famille (DOM).

Dans cet article, vous découvrirez le DOM ainsi que les boucles et les événements en créant une application simple de calculatrice iOS.

## Table des matières

1. [Prérequis](#heading-prerequis)
    
2. [Qu'est-ce que le DOM ?](#heading-quest-ce-que-le-dom)
    
3. [Comment sélectionner des éléments dans le DOM](#heading-comment-selectionner-des-elements-dans-le-dom)
    
4. [Comment créer et ajouter des éléments au DOM](#heading-comment-creer-et-ajouter-des-elements-au-dom)
    
5. [Comment modifier des éléments dans le DOM](#heading-comment-modifier-des-elements-dans-le-dom)
    
6. [Comment supprimer des éléments du DOM](#heading-comment-supprimer-des-elements-du-dom)
    
7. [Boucles et itérations](#heading-boucles-et-iterations)
    
8. [Événements DOM](#heading-evenements-dom)
    
9. [Gestion des événements en JavaScript](#heading-gestion-des-evenements-en-javascript)
    
10. [Comment créer l'application calculatrice](#heading-comment-creer-lapplication-calculatrice)
    
11. [Comment ajouter des fonctionnalités à la calculatrice](#heading-comment-ajouter-des-fonctionnalites-a-la-calculatrice)
    
12. [Conclusion](#heading-conclusion)
    

### Prérequis

**Alors, de quoi allez-vous avoir besoin pour tirer le meilleur parti de ce tutoriel ?**

Vous aurez besoin d'un navigateur, d'un éditeur de texte (VS Code) et de quelques connaissances de base en JavaScript. Pour bien commencer, je vous recommande de consulter [l'un de ces excellents cours d'introduction](https://www.freecodecamp.org/news/learn-javascript-free-js-courses-for-beginners/).

Vous pouvez également lire cet excellent article sur les [bases de JavaScript](https://www.freecodecamp.org/news/learn-javascript-by-building-a-project/).

Si vous avez déjà lu l'article et participé au défi, voici ma solution simple.

%[https://codepen.io/Spruce_khalifa/pen/PoRLqGL] 

Cet article suppose également que vous avez une compréhension de base du HTML et du CSS, ainsi que du fonctionnement du web.

Sur ce, plongeons dans le vif du sujet.

## Qu'est-ce que le DOM ?

Le Document Object Model (DOM) est une structure logique qui définit comment les éléments d'un document peuvent être manipulés et modifiés. Parce que le DOM est structuré de cette manière, il est communément appelé un arbre dans lequel tout est connecté.

Voici un exemple :

![Image](https://lh4.googleusercontent.com/F2-Cq8eWERd3pCUseD4CprU2HNN1pg7Bp-znXM5KF5XjB60ADt4HVggy9bmpGzo_1rcrrqjfGbNWywdpoaONDU-3asY4FlNdqjscx6y_X4h-iTgIu60E11IYE26zmKTC2nXcQi0k1OfkkHR3t5snxtI align="left")

Vous pouvez accéder, modifier, supprimer ou ajouter de nouveaux éléments ou du contenu à un document à l'aide du DOM. En résumé, le DOM vous permet de manipuler presque tout sur une page web.

Retroussez vos manches et mettons-nous au travail maintenant que nous avons une meilleure compréhension de ce qu'est le DOM.

## Comment sélectionner des éléments dans le DOM

L'une des toutes premières choses que vous ferez en travaillant avec le DOM est de sélectionner des éléments dans le document.

En fait, vous devez d'abord apprendre à accéder aux éléments du DOM avant de pouvoir le manipuler.

Vous pouvez sélectionner (ou accéder aux) éléments de différentes manières. Ci-dessous, nous passerons en revue les quelques méthodes dont vous aurez le plus besoin.

### Comment sélectionner des éléments du DOM par ID

Avec `getElementById()`, vous pouvez sélectionner n'importe quel élément d'une page web qui possède un `id`. Tout ce que vous avez à faire est de passer l' `id` de l'élément que vous souhaitez sélectionner.

```html
...
  <body>
    <form>
      <input type="text" />
      <button id="btn">Submit</button>
    </form>
...
```

Voici le JavaScript :

```js
const button = document.getElementById("btn");

console.log(button)
```

Il est important de se rappeler que la méthode `getElementById` ne sélectionne que le premier élément d'une page s'il y a plusieurs éléments avec le même id. Notez qu'un id doit être unique et que vous ne devriez jamais avoir plusieurs éléments avec le même id.

```html
...
  <body>
    <form>
      <input type="text" />
      <button id="btn">one</button>
      <button id="btn">two</button>
      <button id="btn">three</button>
      ...
    </form>
...
```

Et voici le JavaScript :

```js
const button = document.getElementById("button");

console.log(button); // seul le premier bouton est sélectionné
```

### Comment sélectionner des éléments du DOM par nom de classe

Vous pouvez utiliser la méthode `getElementsByClassName` pour sélectionner n'importe quel élément qui possède une classe :

```html
...
  <body>
    <form>
      <input type="text" />
      <button class="btn">Submit</button>
    </form>
  </body>
...
```

Le JavaScript :

```js
const button = document.getElementsByClassName("btn");

console.log(button);
```

Gardez à l'esprit qu'il est écrit getElements – Éléments avec un "s". Cela indique que tous les éléments avec la classe `btn` seront sélectionnés par le sélecteur, et qu'ils seront tous ajoutés à une `HTMLCollection` (un tableau). Vous vous souvenez de ce qu'est un tableau, n'est-ce pas ?

```html
...
  <body>
    <form>
      <input type="text" />
      <button class="btn">one</button>
      <button class="btn">two</button>
      <button class="btn">three</button>
      ...
    </form>
...
```

Le JavaScript :

```js
const buttons = document.getElementsByClassName("btn");

console.log(buttons); // retourne une HTMLCollection de tous les boutons
```

### Comment sélectionner des éléments du DOM par nom de balise

Cela fonctionne de manière similaire à `getElementsByClassName` : cela retourne une HTMLCollection de toutes les balises (Tags) trouvées dans le document.

```html
...
  <body>
    <article class="article">
      <p>This is a paragraph</p>
      <p>This is the second paragraph</p>
      <p>This is the third paragraph</p>
      <p>This is fourth paragraph</p>
    </article>
  </body>
...
```

Le JavaScript :

```js
const p_tag = document.getElementsByTagName("p");

console.log(p_tag);
```

### Comment sélectionner des éléments en utilisant des sélecteurs CSS

Voici mes sélecteurs préférés : `querySelector()` et `querySelectorAll()`. Avec ces sélecteurs, vous pouvez sélectionner n'importe quel élément du DOM de la même manière que vous sélectionneriez n'importe quel élément avec CSS.

```js
const img = document.querySelector("img"); // sélectionne l'élément par nom de balise
const input = document.querySelector("input[type='text']");
const last_div = document.querySelector("form > *:last-child");
const button = document.querySelector(".btn") // sélectionne l'élément par nom de classe
const button = document.querySelector("#btn") // sélectionne l'élément par id
```

Vous utilisez `querySelector()` pour sélectionner un seul élément. Si le sélecteur correspond à plusieurs éléments sur la page, seul le premier est retourné.

```html
...
  <body>
    <article class="article">
      <p>This is a paragraph</p>
      <p>This is the second paragraph</p>
      <p>This is the third paragraph</p>
      <p>This is fourth paragraph</p>
    </article>
  </body>
...
```

Le JavaScript :

```js
const p_tag = document.querySelector("p")

console.log(p_tag)
```

`querySelectorAll()`, en revanche, sélectionnera tous les éléments du document qui correspondent au sélecteur et les stockera dans une NodeList (un tableau) similaire à ceux vus ci-dessus.

```js
const p_tags = document.querySelectorAll("p");

console.log(p_tags);
```

Il est à noter que lorsque vous utilisez `document.querySelector()`, vous recherchez l'élément dans tout le document. Mais lorsque vous effectuez `element.querySelector()`, vous ne recherchez que dans l'élément sélectionné.

Considérez l'exemple suivant : `querySelector()`. Le sélecteur ne cherchera que les éléments correspondants à l'intérieur de l'élément.

```html
...
  <body>
    <form>
      <input type="text" />
      <button class="btn">one</button>
      <button class="btn">two</button>
      <button class="btn">two</button>
    </form>
    <button class="btn">button one outside the form</button>
    <button class="btn">button two outside the form</button>
  </body>
...
```

Le JavaScript :

```js
const form = document.querySelector("form")

const form_btns = form.querySelectorAll(".btn")

console.log(form_btns); // seuls les boutons à l'intérieur du formulaire seront sélectionnés
```

Le `form.querySelectorAll()` ne sélectionnera que les boutons à l'intérieur du formulaire. Cela s'applique également à tous les éléments et sélecteurs.

## Comment créer et ajouter des éléments au DOM

Après avoir appris à sélectionner des éléments HTML déjà créés dans le DOM, essayons de créer nos propres éléments en utilisant JavaScript.

Il y a quelques étapes à suivre pour ajouter des éléments au DOM avec JavaScript. Nous allons passer en revue chacune d'elles ci-dessous.

### Comment créer un élément du DOM

JavaScript exige que tout élément soit créé avant de pouvoir être ajouté au DOM. Pour cela, nous utilisons la méthode `document.createElement()`.

```js
const new_div = document.createElement("div");
const new_paragraph = document.createElement("p");
const new_link = document.createElement("a");
const new_image = document.createElement("img");
```

Nous venons de créer les balises ci-dessus en JavaScript et ne les avons pas encore ajoutées au DOM. Néanmoins, ce sont encore simplement des balises sans attributs ni contenu textuel, corrigeons cela tout de suite.

### Comment définir les attributs des éléments

Pour définir les attributs, comme ajouter une classe, changer l'ID ou changer le SRC, nous utilisons simplement la méthode `setAttribute()` sur le nouvel élément.

La méthode `setAttribute("attribut", "valeur")` prend deux paramètres, l'attribut et la valeur à appliquer à l'attribut.

```js
const new_div = document.createElement("div");
const new_paragraph = document.createElement("p");
const new_link = document.createElement("a");
const new_image = document.createElement("img");

// définition des attributs
new_div.setAttribute("class", "my_div"); // définition d'un attribut class
new_paragraph.setAttribute("id", "my_paragraph"); // définition d'un attribut id
new_link.setAttribute("href", "https://example.com"); // définition de l'attribut href
new_image.setAttribute("src", "https://image-link.png"); // définition de l'attribut src de l'image
```

### Comment ajouter le contenu textuel

Certains de nos éléments nouvellement créés nécessitent encore l'ajout de texte pour que nous puissions les utiliser dans le document – même après l'ajout d'attributs.

Pour créer les textes et les ajouter à nos éléments nouvellement créés, utilisez la méthode `createTextNode()`.

```js
const new_div = document.createElement("div");
const new_paragraph = document.createElement("p");
const new_link = document.createElement("a");
const new_image = document.createElement("img");

...

// création des textNodes
const new_div_text = document.createTextNode("Hello world");
const new_paragraph_text = document.createTextNode("This is a paragraph");
const new_link_text = document.createTextNode("Click to visit link");

// ajout des textNodes aux éléments
new_div.append(new_div_text);
new_paragraph.append(new_paragraph_text);
new_link.append(new_link_text);

console.log(new_div, new_paragraph, new_link, new_image);
```

Et à partir de là, nous pouvons réellement ajouter l'élément nouvellement créé au DOM.

### Comment ajouter des éléments au DOM

La seule façon d'ajouter des éléments nouvellement créés au DOM est de les insérer dans un élément existant.

```html
...
  <body>
    <div class="container">
      
    </div>
  </body>
...
```

Le JavaScript :

```js
const new_div = document.createElement("div");
const new_paragraph = document.createElement("p");
const new_link = document.createElement("a");
const new_image = document.createElement("img");

...

// ajout d'éléments au DOM

// sélection de l'élément parent
const container = document.querySelector(".container");

container.appendChild(new_div);
container.appendChild(new_paragraph);
container.appendChild(new_link);
container.appendChild(new_image);
```

Le nouvel élément sera ajouté comme enfant de l'élément existant déjà sélectionné en utilisant la méthode `appendChild()`.

Il existe, bien sûr, d'autres façons d'ajouter de nouveaux éléments au DOM, mais je vous laisse les découvrir par vous-même.

## Comment modifier des éléments dans le DOM

En plus de créer et d'ajouter des éléments au DOM, JavaScript nous permet également de modifier des éléments du DOM déjà existants. Nous pouvons changer leur contenu, ajouter ou supprimer des attributs, ou même changer leurs styles.

### Comment modifier le texte

Utilisez `textContent` ou `innerText` pour modifier le texte de n'importe quel élément. Voir l'exemple ci-dessous :

```js
...
  <body>
    <article class="article">
      <p>This is a paragraph</p>
    </article>
  </body>
...
```

Le JavaScript :

```js
const p_tag = document.querySelector("article p");

// modification du contenu textuel avec textContent
p_tag.textContent = "Override existing text";

// modification du contenu textuel avec innerText
p_tag.innerText = "Override existing text using innerText";
```

En dehors du texte, nous pouvons également modifier les attributs.

### Comment modifier les attributs

Vous pouvez utiliser la méthode `setAttribute()` pour modifier n'importe quel attribut qu'un élément peut avoir en plus d'en ajouter de nouveaux, comme nous l'avons déjà vu dans une section précédente.

```html
...
  <body>
    <article class="article">
      <p class="my_paragraph">This is a paragraph</p>
    </article>
  </body>
...
```

Le JavaScript :

```js
const p_tag = document.querySelector("article p");

p_tag.setAttribute("class", "new_paragraph");

console.log(p_tag);
```

Puisque nous parlons de changer les attributs, nous pouvons également ajouter, supprimer et basculer entre l'ajout et la suppression d'un attribut de classe sur un élément en utilisant respectivement les méthodes `classList.add()`, `classList.remove()` et `classList.toggle()`.

```js
const p_tag = document.querySelector("article p");

p_tag.classList.add("active") // ajoute une nouvelle classe
p_tag.classList.remove("active") // supprime une classe
p_tag.classList.toggle("active") // supprimera la classe si elle existe ou l'ajoutera si elle n'existe pas
```

### Comment modifier les styles des éléments

Vous pouvez modifier les styles des éléments directement en JavaScript. Sélectionnez simplement l'élément et ajoutez la propriété style suivie du style CSS que vous souhaitez utiliser.

```html
...
  <body>
    <div class="container">
      <p>This is a paragraph</p>
    </div>
  </body>
...
```

Le JavaScript :

```js
const container = document.querySelector(".container");

container.style.display = "none";
```

Vous pouvez ajouter n'importe quel style CSS que vous voulez. La principale différence est que les propriétés CSS sont séparées par des traits d'union (-), par exemple, `background-color`. Mais en JavaScript, les propriétés CSS sont écrites en camelCase – `backgroundColor`.

```js
container.style.backgroundColor = "red";
```

## Comment supprimer des éléments du DOM

Tout ce qui peut être créé peut également être supprimé, y compris les éléments du DOM. Par exemple, vous pouvez supprimer l'enfant d'un élément parent en utilisant `removeChild()`. De même, vous pouvez supprimer l'élément p dans le div ci-dessous en utilisant `removeChild()` :

```html
...
  <body>
    <div class="container">
      <p>This is a paragraph</p>
    </div>
  </body>
...
```

Le JavaScript :

```js
const parent_element = document.querySelector(".container");
const child_element = document.querySelector(".container p");

parent_element.removeChild(child_element);
```

Ci-dessus, nous avons sélectionné l'élément parent puis supprimé l'enfant. Vous pouvez également simplement supprimer le `p` directement en utilisant `remove()`.

```js
const child_element = document.querySelector(".container p");

child_element.remove();
```

Le choix de la méthode de suppression des éléments vous appartient entièrement.

## Boucles et itérations

Les boucles nous permettent d'accomplir des tâches répétées, comme imprimer un nombre de nombreuses fois ou itérer à travers un tableau.

Avec les boucles, nous pouvons accéder à chaque élément d'un tableau, comme on le voit dans l'exemple ci-dessous, où nous imprimons tous les éléments d'un tableau.

```js
const my_array = [1, 3, 5, "hello", 55, "60", "JavaScript"];

for (let i = 0; i < my_array.length; i++) {
  const item = my_array[i];

  console.log(item);
}
```

Le code ci-dessus imprimerait chaque élément du tableau jusqu'à ce qu'il atteigne le dernier lorsque vous l'exécutez.

Mais que se passerait-il si nous voulions nous arrêter à un certain point ? Vous pouvez utiliser l'instruction `break` pour quitter une boucle. Par exemple, nous pourrions décider d'arrêter d'imprimer les éléments de ce tableau lorsque nous atteignons le cinquième.

```js
const my_array = [1, 3, 5, "hello", 55, "60", "JavaScript"];

for (let i = 0; i < my_array.length; i++) {
  const item = my_array[i];

  if (i == 5) {
    break;
  }

  console.log(item);
}
```

L'instruction break met fin à l'exécution de la boucle.

Vous voyez, il y a de nombreuses années, la boucle for (la boucle ci-dessus) était une excellente méthode pour itérer sur les éléments d'un tableau. Mais comme le monde et JavaScript ont changé, nous avons maintenant des moyens plus élégants et plus rapides pour itérer sur les tableaux. Nous allons maintenant explorer les plus courants.

### Comment utiliser les méthodes `forEach()` et `map()`

La méthode `forEach()` est l'une des nouvelles façons élégantes de boucler sur des tableaux. La méthode `forEach()` va parcourir le tableau et exécuter une fonction que vous définissez pour chaque élément du tableau.

```js
const my_array = [1, 3, 5, "hello", 55, "60", "JavaScript"];

my_array.forEach(function (item) {
  console.log(item);
});
```

C'est encore plus court lorsque vous utilisez des fonctions fléchées (arrow functions) :

```js
const my_array = [1, 3, 5, "hello", 55, "60", "JavaScript"];

my_array.forEach((item) => console.log(item));
```

La fonction que vous fournissez doit prendre au moins un paramètre qui est l'élément actuel du tableau. Les deux autres paramètres sont facultatifs : l'index (l'index de l'élément actuel, qui est un nombre) et le dernier paramètre est le tableau d'origine que vous parcourez.

```js
my_array.forEach(callback_function, index, original_array)
```

La seule différence entre `Array.map()` et `Array.forEach()` est que `Array.map()` retournera un nouveau tableau après la fonction de rappel (callback), alors que `Array.forEach()` n'en retourne aucun. `Array.map()` fera exactement ce que `Array.forEach()` fera, c'est-à-dire exécuter une fonction pour chaque élément du tableau.

Contrairement à la boucle for, l'instruction break est inefficace dans les méthodes `Array.forEach()` et `Array.map()`.

### La boucle for...of

La boucle for...of, qui accepte une variable et le tableau sur lequel vous souhaitez itérer, est l'une des nouvelles façons élégantes de boucler sur n'importe quel élément itérable.

```js
const my_array = [1, 3, 5, "hello", 55, "60", "JavaScript"];

for (const item of my_array) {
  console.log(item);
}
```

Tout comme dans une boucle régulière, l'instruction break peut être utilisée dans une boucle for...of.

```js
const my_array = [1, 3, 5, "hello", 55, "60", "JavaScript"];

for (const item of my_array) {
  console.log(item);
  if (item >= 6) {
    break;
  }
}
```

## Événements DOM

Les utilisateurs s'engageront dans une variété d'actions lors de l'utilisation de votre application, telles que cliquer sur des boutons, survoler des éléments à l'écran, soumettre des formulaires, rafraîchir des pages et d'autres activités que les utilisateurs apprécient.

En JavaScript, toutes ces interactions utilisateur sont appelées Événements.

Il existe de nombreux événements en JavaScript, il contient donc des écouteurs d'événements (event listeners) qui peuvent être utilisés pour répondre à chacun d'eux. Cependant, nous n'allons parler que des plus typiques dans cet article.

| Événement | Description |
| --- | --- |
| click | Lorsqu'un utilisateur clique sur un élément, cet événement est déclenché. |
| mouseover | Le survol d'éléments dans le DOM provoque le déclenchement de cet événement. |
| input | Lorsque la valeur d'un élément input ou select change, cet événement est déclenché. |
| submit | Lorsqu'un formulaire est soumis, cet événement est déclenché. |
| keydown | Lorsqu'une touche du clavier est enfoncée, l'événement keydown est déclenché. |
| Keyup | Déclenché lorsqu'une touche enfoncée est relâchée. C'est l'opposé de Keydown. |
| DOMContentLoaded | Cet événement est déclenché lorsque le DOM a été chargé, mais avant que toute ressource externe (comme le CSS et les images) ne soit téléchargée. |
| load | D'autre part, cet événement ne sera pas déclenché tant que tous les éléments du DOM, y compris les ressources externes, n'auront pas été chargés. |

Il existe de nombreux autres événements en JavaScript, mais nous nous arrêterons ici. Vous pouvez consulter d'autres événements dans la [référence des événements DOM de MDN](https://developer.mozilla.org/en-US/docs/Web/Events).

Maintenant que nous avons vu plusieurs types d'événements, voyons comment nous pourrions y répondre.

## Gestion des événements en JavaScript

La méthode addEventListener est la manière recommandée de gérer les événements en JavaScript. Cette méthode vous permet de définir une fonction qui sera exécutée chaque fois que l'événement que vous spécifiez est déclenché.

```js
const input = document.querySelector("input[type='text']");

const handle_input = (e) => {
  console.log(e.target.value);
};

input.addEventListener("input", handle_input);
```

La fonction que vous passez dans la méthode `addEventListener()` acceptera un argument : une référence à l'objet Event, qui possède un ensemble de propriétés décrivant l'événement qui vient de se produire.

Vous pouvez également supprimer un écouteur d'événement d'un élément en utilisant `removeEventListener()`. Cette méthode doit prendre exactement la même fonction que celle que vous avez passée dans la méthode `addEventListener()`.

```js
const input = document.querySelector("input[type='text']");

const handle_input = (e) => {
  console.log(e.target.value)
};

const handle_input2 = (e) => {
  console.log(e.target.value);
  console.log(e);
};

input.removeEventListener("input", handle_input); // cela fonctionnera

input.removeEventListener("input", handle_input2); // passer une fonction différente ne fonctionnera pas
```

Et pour l'instant, c'est tout pour les événements et la gestion des événements. Assez discuté, pratiquons tout ce que nous avons appris jusqu'à présent.

## Comment créer l'application calculatrice

Nous allons créer la calculatrice iPhone de base pour mettre à l'épreuve nos nouvelles compétences en JavaScript. Pour commencer, créez un fichier HTML, un fichier CSS, puis un fichier JavaScript.

À présent, je suppose que vous savez comment configurer un environnement de base en utilisant ces trois outils. Vous pouvez utiliser un éditeur de code en ligne comme CodePen, ce que je ferai dans cette leçon, si vous n'avez pas accès à un PC où vous pouvez générer ces fichiers.

Nous commencerons par construire la base de notre application. Ouvrez le fichier HTML que vous avez préparé et collez-y le code suivant.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>iPhone Calculator</title>
    <script defer src="script.js"></script>
    <link rel="stylesheet" href="style.css" />
  </head>
  <body>
    <main id="main">
      <form id="calc_form">
        <header class="calc_header">
          <input
            type="text"
            disabled
            id="output"
            class="calc_output"
            value="0"
          />
        </header>
        <footer class="calc_footer">
          <div class="btn_group">
            <button
              data-type="clear"
              type="reset"
              value="clear"
              class="btn btn-grey"
            >
              AC
            </button>
            <button data-type="operator" value="invert" class="btn btn-grey">
              +/-
            </button>
            <button data-type="operator" value="%" class="btn btn-grey">
              %
            </button>
            <button data-type="operator" value="/" class="btn btn-orange">
              ÷
            </button>
          </div>
          <div class="btn_group">
            <button
              data-type="operand"
              value="7"
              class="btn btn-dark-grey"
              id="7"
            >
              7
            </button>
            <button data-type="operand" value="8" class="btn btn-dark-grey">
              8
            </button>
            <button data-type="operand" value="9" class="btn btn-dark-grey">
              9
            </button>
            <button data-type="operator" value="*" class="btn btn-orange">
              x
            </button>
          </div>
          <div class="btn_group">
            <button data-type="operand" value="4" class="btn btn-dark-grey">
              4
            </button>
            <button data-type="operand" value="5" class="btn btn-dark-grey">
              5
            </button>
            <button data-type="operand" value="6" class="btn btn-dark-grey">
              6
            </button>
            <button data-type="operator" value="-" class="btn btn-orange">
              -
            </button>
          </div>
          <div class="btn_group">
            <button data-type="operand" value="1" class="btn btn-dark-grey">
              1
            </button>
            <button data-type="operand" value="2" class="btn btn-dark-grey">
              2
            </button>
            <button data-type="operand" value="3" class="btn btn-dark-grey">
              3
            </button>
            <button data-type="operator" value="+" class="btn btn-orange">
              +
            </button>
          </div>
          <div class="btn_group">
            <button
              data-type="operand"
              value="0"
              class="btn btn-grow btn-dark-grey"
            >
              0
            </button>
            <button data-type="operand" value="." class="btn btn-dark-grey">
              .
            </button>
            <button value="=" data-type="operator" class="btn btn-orange">
              =
            </button>
          </div>
        </footer>
      </form>
    </main>
  </body>
</html>
```

Comme vous pouvez le voir ci-dessus, notre calculatrice est essentiellement un formulaire HTML avec beaucoup de boutons et un champ de saisie. Pour la styliser, ajoutons du CSS afin qu'elle ressemble à la calculatrice des iPhones. Ouvrez le fichier CSS que vous avez créé et ajoutez le code suivant :

```css
*,
*::after,
*::before {
  padding: 0px;
  margin: 0px;
  font-family: inherit;
}

body {
  background-color: #333333;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 16px;
}

body,
html {
  height: 100vh;
  font-family: sans-serif;
}

button {
  cursor: pointer;
  border: 0px;
}

input[type="text"] {
  background-color: transparent;
  text-align: end;
  width: 100%;
  color: #d2d2d2;
  border: 0px;
  font-size: 4rem;
}

#main {
  border: 2px solid #ededed;
  border-radius: 50px;
  width: 100%;
  max-width: 280px;
  background-color: #000000;
  padding: 2rem 1rem;
}

.calc_header {
  margin-top: 90px;
  padding: 12px;
}

.calc_footer > * + * {
  margin-top: 1rem;
}

.calc_footer > *:last-child {
  gap: 1rem;
}

.btn_group {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 0.3rem;
}

.btn {
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 50%;
  width: 60px;
  height: 60px;
  color: #ffffff;
  font-size: 20px;
  transition: all 0.3s cubic-bezier(0.19, 1, 0.22, 1);
}

.btn.btn-grow {
  flex-grow: 1;
  border-radius: 40px;
}

.btn:hover {
  transform: translate(-2px, -3px);
}

.btn.active {
  background-color: #ffffff;
  color: #f69906;
}

.btn-grey {
  background-color: #9f9f9f;
  color: #000;
}

.btn-grey:hover {
  background-color: #ededed;
}

.btn-dark-grey {
  background-color: #313131;
}

.btn-dark-grey:hover {
  background-color: #999999;
}

.btn-orange {
  background-color: #f69906;
}

.btn-orange:hover {
  background-color: orange;
}
```

Et maintenant, nous avons une application de calculatrice simple sans fonctionnalité pour le moment. Voici à quoi ressemble l'aperçu en direct :

%[https://codepen.io/freeCodeCamp/pen/jOpwqmR] 

D'après l'exemple ci-dessus, chaque fois que vous cliquez sur un bouton, le formulaire est soumis et la page est rechargée. Mais nous ne voulons pas que cela se produise.

Si vous vous souvenez de la section Événements, nous avons discuté de l'événement submit qui est déclenché chaque fois que nous soumettons un formulaire. Nous pouvons utiliser cet événement pour empêcher notre formulaire de se soumettre chaque fois que nous cliquons sur un bouton.

Pour ce faire, ouvrez le fichier JavaScript que vous avez créé et ajoutez le code suivant :

```js
const form = document.getElementById("calc_form");

form.addEventListener("submit", (e) => {
  e.preventDefault();
});
```

Si vous revenez au code HTML ci-dessus et que vous y prêtez attention, vous verrez que chaque bouton a une propriété value et un attribut data-type qui est soit operator soit operand :

```html
<button data-type="operand" value="6" class="btn btn-dark-grey">
6
</button>
<button data-type="operator" value="-" class="btn btn-orange">
-
</button>
```

La raison en est que nous puissions distinguer les nombres (opérandes) et les opérateurs lors de la sélection des boutons en JavaScript.

### Comment ajouter des fonctionnalités à la calculatrice

Maintenant que nous avons fait cela, nous pouvons commencer à ajouter des fonctionnalités à notre application.

Pour commencer, affichons les valeurs de nos opérandes lorsque nous cliquons sur les boutons. Ajoutez le code suivant à votre fichier JavaScript.

```js
const output = document.getElementById("output");
const form = document.getElementById("calc_form");
const operand_btns = document.querySelectorAll("button[data-type=operand]");
...
let is_operator = false;
operand_btns.forEach((btn) => {
  btn.addEventListener("click", (e) => {
    if (output.value == "0") {
      output.value = e.target.value;
    } else if (is_operator) {
      is_operator = false;
      output.value = e.target.value;
    } else if (output.value.includes(".")) {
      output.value = output.value + "" + e.target.value.replace(".", "");
    } else {
      output.value = output.value + "" + e.target.value;
    }
  });
});
```

Au lieu de sélectionner tous les boutons les uns après les autres (ce qui est fastidieux d'ailleurs), nous avons utilisé `querySelectorAll()`. Cela sélectionnera tous les boutons que nous avons spécifiés et les placera dans une NodeList (un tableau avec des éléments de nœud).

```js
const operand_btns = document.querySelectorAll("button[data-type=operand]");
```

Si vous vous souvenez de ce que nous avons discuté dans la section Boucles et Itérations, vous ne pouvez accéder à aucun de ces boutons sélectionnés à moins d'itérer sur le tableau en utilisant l'une des méthodes de boucle dont nous avons discuté dans cette section.

```js
operand_btns.forEach((btn) => {
  // vous pouvez accéder à chaque bouton ici
});
```

Enfin, nous avons ajouté un écouteur d'événement `click` à chaque bouton comme ceci :

```js
btn.addEventListener("click", (e) => {
  // contrôle ce qui se passe lorsqu'un bouton est cliqué
});
```

Maintenant, chaque fois que nous cliquons sur une valeur d'opérande, la valeur de ce nombre est affichée sur la calculatrice.

Dans l'instruction `else..if`, nous vérifions s'il y a une décimale dans notre valeur de sortie. S'il y en a une, nous arrêtons simplement d'ajouter tout point décimal supplémentaire en le remplaçant par une chaîne vide.

```js
output.value = output.value + "" + e.target.value.replace(".", "");
```

Une autre instruction `else..if` vérifie si nous avons précédemment cliqué sur un bouton d'opérateur. Si c'est le cas et que nous cliquons ensuite sur un bouton d'opérande, nous voulons définir la valeur `is_operator` sur false et redémarrer la valeur dans la sortie à partir de la nouvelle valeur.

```js
else if (is_operator) {
  is_operator = false;
  output.value = e.target.value;
}
```

Voici l'aperçu en direct de l'exemple ci-dessus :

%[https://codepen.io/freeCodeCamp/pen/yLqXOgm] 

Maintenant, sélectionnons également les boutons avec le `data-type` operator et spécifions ce qui se passera chaque fois que nous cliquons sur l'un des boutons.

Ouvrez votre fichier JavaScript et ajoutez le code suivant :

```js
const operator_btns = document.querySelectorAll("button[data-type=operator]");
...
let equation = [];
operator_btns.forEach((btn) => {
  btn.addEventListener("click", (e) => {
    e.currentTarget.classList.add("active");

    switch (e.target.value) {
      case "%":
        output.value = parseFloat(output.value) / 100;
        break;
      case "invert":
        output.value = parseFloat(output.value) * -1;
        break;
      case "=":
        equation.push(output.value);
        output.value = eval(equation.join(""));
        equation = [];
        break;
      default:
        let last_item = equation[equation.length - 1];
        if (["/", "*", "+", "-"].includes(last_item) && is_operator) {
          equation.pop();
          equation.push(e.target.value);
        } else {
          equation.push(output.value);
          equation.push(e.target.value);
        }
        is_operator = true;
        break;
    }
  });
});
```

La première chose que nous faisons dans le code ci-dessus, après avoir ajouté un écouteur d'événement de clic à notre bouton, est d'ajouter la classe `active` à tous les boutons d'opérateur sur lesquels nous cliquons. Nous avons précédemment défini le style de cette classe active dans notre CSS.

```css
.btn.active {
  background-color: #ffffff;
  color: #f69906;
}
```

Nous voulons appliquer ces styles sur le bouton sur lequel nous venons de cliquer chaque fois que nous appuyons sur le bouton d'opérateur.

Nous aurions pu utiliser une instruction `if..else` ici également, mais qui dit que nous ne pouvons pas essayer de nouvelles choses ? L'instruction switch qui suit est une instruction conditionnelle en JavaScript, tout comme l'instruction if que nous avons vue.

L'instruction `switch` accepte une valeur (la condition), dans cet exemple la valeur du bouton qui a été cliqué. Pour chaque cas (case), la valeur est vérifiée. Dans le premier cas, un `%` convertit simplement le nombre en sortie en un pourcentage.

```js
case "%":
  output.value = parseFloat(output.value) / 100;
  break;
```

S'il s'agissait du bouton `invert`, nous inverserions simplement le résultat de sortie en le multipliant par "-1".

```js
case "invert":
  output.value = parseFloat(output.value) * -1;
  break;
```

Si le bouton `=` a été cliqué, nous ajoutons la dernière valeur de la sortie à notre tableau d'équation, utilisons `eval()` pour évaluer rapidement chaque équation s'y trouvant, puis effaçons le tableau d'équation.

```js
case "=":
  equation.push(output.value);
  output.value = eval(equation.join(""));
  equation = [];
  break;
```

REMARQUE : `eval()` est une fonction dangereuse. Elle peut exécuter du code lorsqu'elle est passée en tant qu'entrée, et les utilisateurs peuvent l'utiliser pour écrire du code malveillant qui peut être dangereux. Ne l'utilisez que si vous avez confiance en la source de l'entrée qui sera fournie.

Le code dans le default s'exécute lorsqu'un autre bouton d'opérateur qui n'est pas l'un de ceux listés précédemment est cliqué. Dans le default, nous obtenons d'abord le dernier élément du tableau en utilisant ce code :

```js
let last_item = equation[equation.length - 1];
```

Ensuite, si le bouton précédent sur lequel nous avons cliqué était un opérateur — c'est-à-dire s'il s'agissait de l'un des suivants : `/`, `*`, `+` ou `-` — nous le supprimons simplement de l'équation en utilisant `equation.pop()` et ajoutons le nouveau sur lequel nous avons cliqué avec `equation.push()`.

Si notre dernier élément de tableau n'était pas un opérateur, nous ajoutons la valeur de sortie et la valeur du bouton sur lequel nous avons cliqué au tableau d'équation.

```js
else {
  equation.push(output.value);
  equation.push(e.target.value);
}
```

Enfin, nous définissons également la valeur de `is_operator` sur true chaque fois que nous cliquons sur un bouton `operator` :

```js
default:
  let last_item = equation[equation.length - 1];
  if (["/", "*", "+", "-"].includes(last_item) && is_operator) {
    equation.pop();
    equation.push(e.target.value);
  } else {
    equation.push(output.value);
    equation.push(e.target.value);
  }
  is_operator = true;
  break;
```

Vous remarquerez que pour chaque cas, nous passons l'instruction `break`. L'instruction `break` ici arrêtera l'exécution du switch chaque fois qu'un cas est vrai et que le code finit de s'exécuter.

Et voilà – une application de calculatrice entièrement fonctionnelle ! Et voici l'aperçu en direct :

%[https://codepen.io/freeCodeCamp/pen/ZEjyWeE] 

Avant de terminer, il y a un petit problème avec notre calculatrice : la classe `active` que nous avons ajoutée à nos boutons d'opérateur lorsqu'ils sont cliqués reste active même après avoir cliqué sur un autre bouton.

Remédions à cela en créant une fonction qui supprime la classe active de tout bouton d'opérateur.

```js
const remove_active = () => {
  operator_btns.forEach((btn) => {
    btn.classList.remove("active");
  });
};
```

Maintenant, nous avons simplement besoin d'appeler cette fonction avant d'ajouter la classe active à n'importe quel bouton.

```js
operator_btns.forEach((btn) => {
  btn.addEventListener("click", (e) => {
    remove_active();
    e.currentTarget.classList.add("active");
    ...
  });
});
```

Nous devons également supprimer la classe active des opérateurs chaque fois qu'un bouton d'opérande est cliqué.

```js
operand_btns.forEach((btn) => {
  btn.addEventListener("click", (e) => {
    remove_active();
    ...
  });
});
```

C'est maintenant beaucoup mieux. Vous pouvez trouver le code complet et l'aperçu en direct de notre application dans le Pen ci-dessous :

%[https://codepen.io/freeCodeCamp/pen/rNrweyV] 

### Défi JavaScript

Bien que notre application de calculatrice soit maintenant complètement opérationnelle, il y a quelques fonctionnalités que je n'ai pas incluses et qui, selon moi, seraient une merveilleuse occasion pour vous de pratiquer vos nouvelles compétences en JavaScript.

* Le bouton d'effacement : Lorsque nous cliquons sur un bouton d'opérande, la valeur du bouton devrait passer de AC à C. Lorsque ce bouton est cliqué, nous effaçons le formulaire et supprimons toute classe active de nos boutons d'opérateur.
    
* La calculatrice iPhone n'autorise qu'un maximum de 9 chiffres comme opérandes. Vous ne pouvez pas dépasser cette limite, ce qui, je pense, serait une fonctionnalité utile pour notre logiciel de calculatrice également.
    
* Des virgules sont automatiquement ajoutées aux nombres dans la sortie de la calculatrice iPhone, et notre programme n'a pas actuellement cette capacité.
    
* Si nous utilisons deux opérandes décimaux, le résultat est parfois affecté par une erreur d'arrondi en virgule flottante. Notre application de calculatrice ne gère aucun arrondi pour le moment. Consultez [cet article](https://0.30000000000000004.com/) si vous souhaitez en savoir plus sur ce sujet.
    

Pensez-vous pouvoir relever l'un de ces défis ? Bonne chance !

## Conclusion

Félicitations, as du JavaScript ! Vous êtes arrivé jusqu'ici. Dans ce tutoriel, nous avons appris le DOM, les boucles, les événements JavaScript et comment les gérer, et nous avons construit une calculatrice simple à la fin.

Si vous participez au défi de cet article, n'hésitez pas à partager votre solution en ligne et à me taguer [@sprucekhalifa](https://twitter.com/sprucekhalifa) sur Twitter. Et n'oubliez pas de me suivre également, car je tweete sur JavaScript.

Oh, et bon codage !