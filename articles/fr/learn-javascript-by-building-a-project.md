---
title: Apprendre les bases de JavaScript en créant une application de compteur
subtitle: ''
author: Spruce Emmanuel
co_authors: []
series: null
date: '2022-08-15T20:31:44.000Z'
originalURL: https://freecodecamp.org/news/learn-javascript-by-building-a-project
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/pexels-antonio-batinic--4164418--1-.jpg
tags:
- name: beginners guide
  slug: beginners-guide
- name: JavaScript
  slug: javascript
seo_title: Apprendre les bases de JavaScript en créant une application de compteur
seo_desc: 'JavaScript allows you to make dynamic web sites. It''s the final part of
  the web development trinity with HTML and CSS, and you use it to make your static
  pages dynamic.

  You''ll likely start learning JavaScript as soon as you''ve covered the basics of
  H...'
---

JavaScript permet de créer des sites web dynamiques. C'est la partie finale de la trinité du développement web avec HTML et CSS, et vous l'utilisez pour rendre vos pages statiques dynamiques.

Vous commencerez probablement à apprendre JavaScript dès que vous aurez couvert les bases de HTML et CSS. Ensuite, après un certain temps, vous pourriez tomber dans l'une des catégories suivantes :

* Vous avez appris toute la syntaxe sophistiquée de JavaScript mais vous ne parvenez pas à la comprendre.

* Vous comprenez la syntaxe mais ne pouvez pas l'appliquer à vos projets personnels.

* Vous voulez abandonner ou pensez à changer de carrière.

Nous allons adopter une approche pratique pour apprendre JavaScript dans cet article et ceux qui suivent. Je promets de ne pas vous ennuyer trop avec la syntaxe, mais plutôt nous allons apprendre en construisant des projets.

Je vais supposer que vous connaissez les bases de HTML et CSS pour cet article et ceux qui pourraient suivre. Mais si ce n'est pas le cas, vous pouvez plonger dans ce [cours pour débutants](https://www.freecodecamp.org/news/learn-html-beginners-course/) pour apprendre ou rafraîchir vos connaissances avant de continuer ce tutoriel.

## Quels outils ai-je besoin pour apprendre JavaScript ?

JavaScript ne nécessite pas une configuration élaborée ou coûteuse. Tout ce dont vous avez vraiment besoin est un ordinateur avec les éléments suivants :

* Un éditeur de texte (comme Visual Studio Code)

* Un navigateur web moderne (comme Chrome, Edge, Firefox, etc.)

Si vous n'avez pas d'ordinateur, vous pouvez toujours suivre la leçon en utilisant un éditeur de code en ligne tel que [codepen.io](https://codepen.io/).

## Comment commencer avec JavaScript

Comme indiqué ci-dessus, tout ce dont vous avez besoin est un éditeur de texte et un navigateur pour commencer. Lancez votre éditeur de texte — dans mon cas, VSCode — dans le répertoire où vous souhaitez que vos fichiers de code soient situés.

Créez un nouveau fichier appelé `index.html`. Si vous utilisez VS Code, votre configuration de projet devrait ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/08/Screenshot--5--1.png align="left")

### Comment prévisualiser votre code dans le navigateur

Une fois que vous avez terminé de créer votre fichier HTML, vous voudrez voir le produit fini dans votre navigateur.

Pour faciliter ce processus, nous devons installer l'extension "live server" sur VS Code. Cette extension fera en sorte que la page web se rafraîchisse immédiatement chaque fois que nous apportons des modifications à notre fichier HTML.

Cliquez sur l'icône d'extension dans le côté droit de VSCode.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/Screenshot--7-.png align="left")

Recherchez et installez l'extension live server. Retournez à votre fichier HTML et choisissez "Open with live server" dans le menu contextuel.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/Screenshot--8-.png align="left")

Votre page web devrait maintenant être visible dans votre navigateur.

### Comment intégrer JavaScript dans votre page HTML

Vous pouvez inclure du code JavaScript dans votre HTML en le plaçant directement dans la balise script.

```xml
<!DOCTYPE html>
<html lang="en">
  <head>
    ...
    <script>
      let my_variable = "hello JavaScript";

      // tout code JavaScript peut aller ici
    </script>
  </head>
  <body>
    <h1>Hello world</h1>
   
  </body>
</html>
```

Mais gardez à l'esprit que la méthode ci-dessus n'est pas conseillée. Au lieu de cela, vous devriez générer un fichier JavaScript externe avec l'extension `.js`.

Créez un nouveau fichier nommé `script.js` dans votre répertoire de projet, puis liez-le à votre fichier HTML en utilisant l'URL de votre code JavaScript externe, comme ceci :

```xml
<!DOCTYPE html>
<html lang="en">
  <head>
   ...
    <script src="script.js"></script>
    <title>Compteur</title>
  </head>
  <body>
    ...
  </body>
</html>
```

Le JavaScript s'exécutera avant tout HTML. Cela cause généralement des problèmes puisque les éléments HTML que vous sélectionnez avec JavaScript seront indéfinis parce que le navigateur lit le code HTML de haut en bas.

Nous utiliserons l'attribut `defer` de l'élément script pour corriger cela, ce qui indique au navigateur de charger le HTML en premier avant d'exécuter le code JavaScript.

```js
<script defer src="script.js"></script>
```

Maintenant que nous sommes tous prêts, plongeons dans quelques bases de JavaScript.

### Comment utiliser les variables en JavaScript

Une variable est un espace réservé pour des valeurs que vous pourriez avoir besoin d'utiliser à l'avenir. Avec JavaScript, tout est stocké dans des variables.

Pour déclarer une variable, vous pouvez utiliser le mot-clé `let` ou `const`.

```js
let first_variable
const last_variable
```

Vous utilisez le signe d'égalité pour assigner une valeur à une variable.

```js
let first_variable = "hello world"
```

Si vous déclarez une variable avec let, vous pouvez la modifier. En revanche, si vous déclarez des variables avec `const`, vous ne pouvez pas changer leurs valeurs — d'où le nom.

En JavaScript, vous pouvez stocker plusieurs types de données dans des variables :

* Chaînes de caractères — Toute valeur qui est simple ou double et enveloppée dans des guillemets est une chaîne de caractères.

```js
let my_string = "Hello world" // chaîne de caractères
let my_second_string = "24" // chaîne de caractères
```

* Nombres — Ces nombres ne sont pas enfermés dans des guillemets.

```js
let my_number = 15 // nombre
let my_second_number = "15" // chaîne de caractères
```

* Tableaux — Le tableau est votre meilleure option si vous voulez stocker plusieurs valeurs dans une seule variable.

```js
let my_array = [1, "hello", "4", "world"]
```

* Booléen — Vous n'avez pas besoin d'enfermer une valeur booléenne dans des guillemets car il s'agit d'une valeur vraie ou fausse et non d'une chaîne de caractères.

```js
let my_boolean = true;
```

* Objets — Les objets vous permettent de stocker des données en paires clé-valeur.

```js
let my_obj = {
    name: "John snow",
    aim: "Apprendre JavaScript",
    age: 20,
}
```

Puisque JavaScript interprète tout comme un objet, vous pouvez même enregistrer des références aux éléments HTML dans des variables.

```js
let my_button = document.querySelector("#id")
```

Nous sélectionnons des éléments sur une page web en fonction de leur id lorsque nous utilisons `document.querySelector("#id")`. Ne vous inquiétez pas, nous entrerons dans plus de détails sur cela plus tard.

Pour utiliser une variable en JavaScript, appelez simplement le nom de la variable comme ceci :

```js
my_button
```

Pour démontrer comment les variables fonctionnent en JavaScript, construisons une application de compteur de base. Ajoutez le code suivant au fichier HTML que vous avez précédemment créé :

```xml
...
<body>
    <div class="counter_conatiner">
      <button id="subtract">-</button><span id="output">0</span
      ><button id="add">+</button>
    </div>
  </body>
...
```

Créez un fichier `style.css` et ajoutez les styles suivants pour lui donner un peu de vie en utilisant CSS :

```css
*,
*::after,
*::before {
  padding: 0px;
  margin: 0px;
  font-family: inherit;
}
html,
body {
  height: 100vh;
}

body {
  font-family: sans-serif;
  font-size: 16px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background-color: aliceblue;
}
.counter_conatiner {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 6px;
  margin-top: 1rem;
}
span {
  font-size: 3rem;
  background-color: #00bb00;
  padding: 2px 12px;
  margin-left: 16px;
  margin-right: 16px;
  border-radius: 4px;
  color: #fff;
}
button {
  font-size: 3rem;
  cursor: pointer;
  background-color: transparent;
  border: 0px;
}
```

N'oubliez pas de lier le fichier CSS à votre HTML comme ceci :

```xml
<head>
   ...
    <link rel="stylesheet" href="style.css" />
    <title>Compteur</title>
  </head>
```

Et voilà — une application de compteur de base construite avec HTML et CSS.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/Web-capture_13-8-2022_75125_127.0.0.1.jpeg align="left")

Gardez à l'esprit que les variables peuvent contenir des références aux éléments HTML. Enregistrons maintenant les références à nos boutons dans des variables. Ouvrez le fichier script.js que nous avons créé précédemment et ajoutez le code suivant :

```js
let add = document.querySelector("#add");
let subract = document.querySelector("#subtract");

console.log(add, subract);
```

Attendez une minute, les variables sont amusantes, n'est-ce pas ? Bien qu'elles puissent contenir n'importe quoi, il y a quelques règles fondamentales que vous devriez connaître avant d'utiliser des variables :

* Évitez d'utiliser des underscores au début des noms de variables, comme `_my_variable`, car ils sont très confus.

* JavaScript ne vous permettra pas de commencer les noms de variables par des chiffres, comme `8_variable`.

* `my_variable`, `MY_VARIABLE`, et `my_Variable` sont toutes des choses entièrement différentes en JavaScript en raison de la sensibilité à la casse.

* Et en aucun cas vous ne devriez utiliser des [mots réservés JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#reserved_words), y compris let, const, true, false, function, et tout autre.

Hey, ne violez pas ces règles fondamentales. Alors passons à d'autres choses intéressantes que nous pouvons faire en utilisant JavaScript.

### Comment utiliser les opérateurs en JavaScript

Sans les maths, quel serait le monde ? Et quel serait JavaScript sans quelques maths ?

En JavaScript, nous avons un ensemble de symboles mathématiques que vous pouvez utiliser pour effectuer des opérations mathématiques simples.

Ne vous inquiétez pas, vous êtes probablement déjà familier avec la plupart d'entre eux :

* Addition — En JavaScript, vous utilisez le signe plus (+) pour concaténer (joindre) des chaînes de caractères ou ajouter des nombres.

```js
let addition = 1 + 1 // 2
let addition = 1 + "1" // "11"
let addition = "hello" + "world" // "hello world"
```

* Soustraction — vous utilisez le signe moins (-) pour soustraire des nombres.

```js
let subtraction = 10 - 9 // 1
```

* Multiplication — vous utilisez un astérisque pour la multiplication en JavaScript lorsque vous multipliez des nombres.

```js
let multiplication = 2 * 2 // 4
```

* Division — vous utilisez le signe de division (/) pour diviser des nombres.

```js
let division = 4 / 2 // 2
```

* Égalité — vous utilisez le double signe égal (==) pour vérifier si deux valeurs sont égales en JavaScript.

```js
let if_true = 2 + 4 == 6 // true
let if_false = 5 + 6 == 10 // false
```

Il existe d'autres opérateurs JavaScript disponibles, mais je n'entrerai pas dans les détails ici.

Maintenant que nous sommes familiers avec les opérateurs, retournons à notre application de compteur et modifions-la pour qu'elle augmente chaque fois que nous cliquons sur le bouton "+" de la page.

Nous avons déclaré quelques variables et enregistré une référence aux boutons HTML comme valeurs dans la section précédente.

```js
let add = document.querySelector("#add");
let subract = document.querySelector("#subtract");

...
```

Maintenant, tout ce que nous avons à faire pour utiliser notre variable `add` est d'appeler son nom.

```js
add
```

Mais cela est insuffisant. Nous devons savoir s'il a été cliqué, et JavaScript nous fournit ce que nous appelons des Événements. Nous les utilisons pour écouter les événements qui se produisent sur une page web, comme lorsqu'un utilisateur clique sur un bouton ou fait défiler la page, entre autres.

Voici à quoi cela ressemble :

```js
add.addEventListener("click", function () {
 // Chaque fois que le bouton d'ajout est pressé, ce code sera exécuté.
});
```

Il n'est pas nécessaire que cela ait du sens tout de suite. Dans ce cas, nous avons utilisé `addEventListener` pour ajouter un événement de clic au bouton. Nous parlerons exclusivement des événements dans une autre section.

Maintenant, tout code qui se trouve dans le callback du listener est appelé lorsque le bouton est cliqué.

Maintenant que nous en sommes conscients, augmentons la valeur de sortie. Pour ce faire, obtenez simplement la valeur de sortie puis augmentez-la de un chaque fois que le bouton est pressé. Voici le code pour faire cela :

```js
let add = document.querySelector("#add");

add.addEventListener("click", function () {
  let output = document.querySelector("#output");
  let result = output.innerText + 1;

  output.innerText = result;
});
```

À l'exception de `innerText`, qui est utilisé en JavaScript pour obtenir le texte des éléments HTML sur une page web et peut également modifier le texte d'un élément HTML comme vu ci-dessus, la majorité de la syntaxe ci-dessus devrait maintenant être reconnaissable.

Dans l'exemple ci-dessous, cliquez sur le bouton d'ajout (+) pour voir le compteur s'incrémenter.

%[https://codepen.io/Spruce_khalifa/pen/JjLmoMa?editors=0010] 

Ce n'est pas ce à quoi vous vous attendiez, n'est-ce pas ? Parce que la valeur de `let output = document.querySelector("#output")` est une chaîne de caractères et JavaScript ne vous permet pas d'ajouter des chaînes de caractères et des nombres, vous devez convertir la sortie en un nombre avant d'ajouter.

```js
let result = Number(output.innerText) + 1;
```

Dans le code ci-dessus, nous avons transformé notre chaîne en un nombre en utilisant la méthode `Number()`.

Essayons à nouveau l'exemple précédent après avoir apporté les modifications.

%[https://codepen.io/Spruce_khalifa/pen/gOeBbeO?editors=0010] 

Cela fonctionne maintenant comme prévu.

### Comment utiliser les conditionnelles en JavaScript

Et si... ? Les conditionnelles sont utilisées pour résoudre des questions comme, "Et si nous voulons que notre application de compteur arrête de compter à 10 ?" ou "Et si nous voulons sauter un nombre ?" Lorsque vous êtes confronté à des questions conditionnelles comme celles-ci, vous avez besoin d'une conditionnelle.

Les seules conditionnelles que nous examinerons aujourd'hui en JavaScript sont les instructions if...else.

```js
if (condition) {
  /* code à exécuter si la condition est vraie */
} else {
  /* exécuter un autre code à la place */
}
```

Les conditionnelles nous permettent d'exécuter du code uniquement lorsqu'une condition donnée est remplie. Par exemple, si notre compteur est supérieur à 10, nous pouvons le réinitialiser à zéro (0).

```js
let add = document.querySelector("#add");

add.addEventListener("click", function () {
  let output = document.querySelector("#output");
  let result = output.innerText + 1;

  if (result > 10) {
    result = 0;
  }

  output.innerText = result;
});
```

Si le résultat est supérieur à 10, l'instruction if dans le code précédent réinitialise le résultat à 0. Dans l'exemple suivant, essayez d'augmenter le compteur à un nombre supérieur à 10.

%[https://codepen.io/Spruce_khalifa/pen/GRxYgYg?editors=0010] 

Vous verrez que nous avons omis l'instruction else. C'est parce qu'elle est facultative.

### Comment utiliser les fonctions en JavaScript

Nous terminons enfin notre petite application de compteur. Ajoutons la possibilité de soustraire. Tout ce que nous avons à faire est de déduire 1 de la sortie.

```js
let add = document.querySelector("#add");
let subract = document.querySelector("#subtract");

add.addEventListener("click", function () {
  let output = document.querySelector("#output");
  let result = Number(output.innerText) + 1;

  if (result > 10) {
    result = 0;
  }

  output.innerText = result;
});

subract.addEventListener("click", function () {
  let output = document.querySelector("#output");
  let result = Number(output.innerText) - 1;

  if (result < 0) {
    result = 0;
  }

  output.innerText = result;
});
```

Et voilà, une application de compteur JavaScript de base.

%[https://codepen.io/Spruce_khalifa/pen/Barqyvz?editors=0010] 

Jetez un coup d'œil au code complet de la plume ci-dessus et décrivez ce que vous observez.

Eh bien, je remarque beaucoup de code dupliqué, ce qui n'est pas bon. Vous devriez éviter la répétition dans votre code.

Et pour cette raison, nous utilisons des fonctions. Nous pouvons écrire un morceau de code et ensuite l'utiliser autant de fois que nous le souhaitons avec des fonctions.

Vous pouvez utiliser le mot-clé function en JavaScript pour créer une fonction.

```js
function add() {
  alert("hello world")
}
```

Les fonctions peuvent également prendre des paramètres.

```js
function add(number1, number2) {
 return number1 + number2
}
```

Ces paramètres sont utilisés de la même manière que les variables dans une fonction. Ils sont essentiellement des espaces réservés.

Les fonctions, comme les variables, sont appelées par leurs noms. La seule différence est que lors de l'appel d'une fonction, vous devez inclure des parenthèses — ().

```js
add(2,4) // 6
```

Vous avez peut-être vu des fonctions déclarées de cette manière également :

```js
const add = (number1, number2) => number1 + number2;
```

Ce qui précède est équivalent à la fonction formelle `add()`. Elles sont connues sous le nom de fonctions fléchées, et c'est ainsi que nous déclarerons nos fonctions à partir de maintenant.

Je crois que cela suffit d'informations pour l'introduction à ce stade, alors je vous laisse avec cette tâche.

### Défi hebdomadaire JavaScript

Nous avons créé une application de comptage simple dans cette leçon, mais elle contient beaucoup de code répétitif, alors voici un défi pour vous :

* Créez une seule fonction appelée `addAndSubtract()` qui peut gérer à la fois les opérations d'addition et de soustraction sans avoir à répéter de code.

## Conclusion

Dans cet article, nous avons appris à utiliser JavaScript, développé une petite application de compteur et appris les variables, les conditionnelles et les fonctions.

N'hésitez pas à me contacter sur Twitter à [@sprucekhalifa](https://twitter.com/sprucekhalifa) si vous avez des questions.

Aussi, bon codage !