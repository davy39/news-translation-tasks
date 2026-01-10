---
title: Comment programmer une calculatrice avec jQuery
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-16T14:51:19.000Z'
originalURL: https://freecodecamp.org/news/programming-a-calculator-8263966a8019
coverImage: https://cdn-media-1.freecodecamp.org/images/0*UYnfseaB8q66tNX3.
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Comment programmer une calculatrice avec jQuery
seo_desc: 'By Jennifer Bland

  Previously, I showed you how to use CSS border-radius property to create the following
  calculator. Now I will show you how to use jQuery to implement the functionality
  of the calculator.


  Calculator using the CSS border-radius featu...'
---

Par Jennifer Bland

Précédemment, je vous ai montré comment utiliser [la propriété CSS border-radius pour créer la calculatrice suivante](https://medium.freecodecamp.org/learn-css-border-radius-property-by-building-a-calculator-53497cd8071d). Maintenant, je vais vous montrer comment utiliser jQuery pour implémenter la fonctionnalité de la calculatrice.

![Image](https://cdn-media-1.freecodecamp.org/images/X7MbaFdBptj9fzN4SHHyJsslKfnEB6Fb1otG)
_Calculatrice utilisant la fonctionnalité CSS border-radius_

#### Ajout de jQuery

Nous allons utiliser jQuery dans ce projet pour répondre aux événements lorsque l'utilisateur clique sur un bouton. Nous devons ajouter la bibliothèque jQuery à notre application. J'utiliserai la bibliothèque CDN cdnjs pour ajouter jQuery.

Au bas de mon fichier index.html, j'ajouterai la balise de script suivante :

```
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
```

#### Gestion des boutons opérateurs et nombres

Avant d'écrire mon code, j'ai décidé de réfléchir à la manière dont je gérerais la fonctionnalité derrière la calculatrice. Je divise les boutons de la calculatrice en deux groupes : **opérateur** et **nombre**.

Un bouton nombre correspondrait aux nombres 0–9. Tous les autres boutons sont des opérateurs.

#### Variables globales pour notre opération

L'étape suivante consiste à déterminer combien de variables globales nous aurons besoin. Les variables globales contiendront la fonctionnalité de notre calculatrice. Par exemple, un utilisateur peut entrer la séquence suivante :

```
2 + 3 = 5
```

De même, un utilisateur peut entrer cette séquence beaucoup plus longue :

```
2 + 3 * 4 / 5 - 6 = -2
```

Lors de la considération initiale des variables globales, nous pourrions envisager de créer une nouvelle variable chaque fois que l'utilisateur appuie sur une touche. Cela ne serait pas très efficace. Nous devrions suivre qui sait combien de variables lorsque l'utilisateur appuie sur des touches.

Pour améliorer cela, nous pouvons simplifier les choses pour n'avoir besoin que de quatre variables globales :

* num1
* num2
* operator
* total

Permettez-moi de vous montrer comment cela fonctionne. Le premier nombre que l'utilisateur appuie est stocké dans la variable num1. L'opérateur (c'est-à-dire +, –, *, / ou entrer) est stocké dans l'opérateur. Le nombre suivant entré est stocké dans la variable 2. Une fois le deuxième opérateur entré, le total est calculé. Le total est stocké dans la variable total.

Une question logique serait : que faites-vous avec le troisième ou quatrième nombre qu'un utilisateur entre ? La réponse simple est que nous réutilisons num1 et num2.

Une fois le total calculé, nous pouvons remplacer la valeur dans num1 par le total. Nous devrions ensuite vider les variables operator et num2. Parcourons cela avec notre deuxième exemple ci-dessus :

```
2 + 3 * 4 / 5 - 6 = -2// num1 se voit attribuer la valeur de 2// operator se voit attribuer la valeur de +// num2 se voit attribuer la valeur de 3// total se voit attribuer la valeur de 5// num1 se voit attribuer la valeur de 5// num2 et operator sont effacés// operator se voit attribuer la valeur de *// num2 se voit attribuer la valeur de 4// total se voit attribuer la valeur de 20// num1 se voit attribuer la valeur de 20// num2 et operator sont effacés// operator est stocké la valeur de /// num2 se voit attribuer la valeur de 5// total se voit attribuer la valeur de 4// num1 se voit attribuer la valeur de 4// num2 et operator sont effacés// operator se voit attribuer la valeur de -// num2 se voit attribuer la valeur de 6// total se voit attribuer la valeur de -2// num1 se voit attribuer la valeur de -2// num2 et operator sont effacés// operator se voit attribuer la valeur de =
```

Maintenant, vous voyez que nous pouvons gérer toutes les combinaisons possibles de boutons pressés par l'utilisateur en utilisant ces 4 variables.

#### Obtenir la touche pressée par l'utilisateur

Maintenant que nous avons parcouru notre logique, nous devons commencer le processus de gestion de la touche pressée par l'utilisateur. Au bas de mon fichier index.html, je vais créer une balise de script qui contiendra mon code.

La première étape consiste à obtenir la touche qu'un utilisateur a pressée. Voici un extrait de mon fichier index.html qui montre tous les boutons sur une ligne de la calculatrice :

```
<div class="flex-row">    <button class="calc-btn">1</button>    <button class="calc-btn">2</button>    <button class="calc-btn">3</button>    <button class="calc-btn">+</button></div>
```

Chaque bouton, qu'il s'agisse d'un nombre ou d'un opérateur, est défini à l'aide d'un élément `<button></button>`. Nous pouvons utiliser cela pour détecter lorsqu'un utilisateur clique sur un bouton.

Dans jQuery, vous pouvez avoir une fonction de clic de bouton. Lorsqu'un bouton est cliqué, la fonction reçoit un objet événement. Le `event.target` contiendra le bouton qui a été cliqué. Je peux obtenir la valeur du bouton en utilisant la propriété `innerHTML`.

Voici le code qui affichera dans la console le bouton sur lequel un utilisateur clique.

```
<script>$(document).ready(function() {    $('button').on('click', function(e) {        console.log('e', e.target.innerHTML);    });});</script>
```

Maintenant, si vous testez le code, vous verrez la valeur de la touche que vous pressez. Cela fonctionne pour tous les boutons de la calculatrice.

#### Création de nos variables globales

Maintenant que nous avons la capacité de déterminer quelle touche a été pressée, nous devons commencer à les stocker dans nos variables globales. Je vais créer mes quatre variables globales :

```
let num1 = '';let num2 = '';let operator = '';let total = '';
```

#### Gestion du bouton lors du clic

Lorsque l'utilisateur clique sur un bouton, il cliquera sur un nombre ou un opérateur. Pour cette raison, je vais créer deux fonctions :

```
function handleNumber(num) {    // code ici}
```

```
function handleOperator(oper) {    // code ici}
```

Dans ma fonction de clic de bouton précédente, je peux remplacer le console.log par un appel à la fonction appropriée. Pour déterminer si un bouton ou un opérateur a été cliqué, je peux comparer `e.target.innerHTML` pour voir s'il est compris entre 0 et 9. Si c'est le cas, l'utilisateur a cliqué sur un nombre. Sinon, l'utilisateur a cliqué sur un opérateur.

Voici mon étape initiale pour tester afin de m'assurer que je peux dire quel bouton a été cliqué :

```
$(document).ready(function() {    $('button').on('click', function(e) {        let btn = e.target.innerHTML;        if (btn >= '0' && btn <= '9') {            console.log('nombre');        } else {            console.log('opérateur');        }    });});
```

Une fois que je suis satisfait d'avoir identifié chaque bouton cliqué, je peux remplacer le console.log par un appel à la fonction appropriée :

```
$(document).ready(function() {    $('button').on('click', function(e) {        let btn = e.target.innerHTML;        if (btn >= '0' && btn <= '9') {            handleNumber(btn);        } else {            handleOperator(btn);        }    });});
```

#### Gestion des boutons nombres

Lorsque l'utilisateur appuie sur un nombre, il sera assigné soit à la variable num1, soit à la variable num2. num1 est assigné la valeur de `''`. Nous pouvons utiliser cela pour déterminer quelle variable assigner le nombre. Si num1 est vide, alors nous assignons le nombre à celui-ci. Sinon, nous l'assignons à num2.

Voici à quoi ressemble ma fonction handleNumber :

```
function handleNumber(num) {    if (num1 === '') {        num1 = num;    } else {        num2 = num;    }}
```

#### Gestion des boutons opérateurs

Notre fonction pour gérer lorsque l'utilisateur appuie sur un bouton opérateur est très simple. Tout ce que nous avons à faire est d'assigner la valeur à notre variable opérateur.

Voici à quoi ressemble ma fonction handleOperator :

```
function handleOperator(oper) {    operator = oper;}
```

#### Affichage des boutons

L'étape suivante consiste à afficher réellement le bouton pressé à l'utilisateur. Si vous vérifiez la fonctionnalité de la calculatrice sur votre téléphone, vous remarquerez qu'elle n'affiche que les nombres. Si un utilisateur appuie sur la touche `+`, elle n'est pas affichée.

Dans notre fichier index.html, nous avons une div avec une classe `'calc-result-input'` qui affiche notre entrée. Nous utiliserons cela pour afficher les nombres à nos utilisateurs.

Puisque nous avons séparé l'activité de notre calculatrice en fonctions, nous créerons une fonction pour afficher le bouton.

Voici à quoi ressemble ma fonction displayButton :

```
function displayButton(btn) {    $('.calc-result-input').text(btn);}
```

Puisque nous mettons à jour l'affichage uniquement lorsque l'utilisateur appuie sur un nombre, nous pouvons appeler la fonction `displayButton` depuis la fonction `handleNumber`.

Voici à quoi ressemble ma fonction handleNumber maintenant :

```
function handleNumber(num) {    if (num1 === '') {        num1 = num;    } else {        num2 = num;    }    displayButton(num);}
```

#### **Gestion des totaux**

L'étape suivante consiste à calculer un total. Un total n'est calculé qu'après qu'un utilisateur a pressé un opérateur après avoir attribué une valeur à num1 **et** num2.

Par exemple, si l'utilisateur entre :

```
2 + 3 =
```

Nous voulons additionner num1 et num2 et afficher le total.

Si l'utilisateur entre :

```
2 - 1 =
```

Nous voulons soustraire num2 de num1 et afficher le total.

Nous créons une fonction `handleTotal` pour gérer cela. Cette fonction créera un total en fonction de l'opérateur pressé. Puisqu'il y a plusieurs opérateurs qui peuvent être pressés, nous utiliserons une instruction case pour les gérer.

Pour simplifier, je vais seulement montrer le code pour gérer lorsque l'utilisateur clique sur le bouton opérateur `+`.

Voici la fonction handleTotal :

```
function handleTotal() {    switch (operator) {        case '+':            total = +num1 + +num2;            displayButton(total);            break;    }}
```

#### Conversion de chaîne en nombre pour le calcul

Lorsque nous obtenons le `innerHTML` du bouton qui est pressé, nous obtenons une valeur de chaîne. Pour additionner deux variables, elles doivent être converties en nombre. Il existe une notation abrégée en JavaScript qui convertira une chaîne en nombre en préfixant la variable avec un signe `+`. Vous pouvez voir où je fais cette conversion sur cette ligne :

```
total = +num1 + +num2;
```

#### Quand appeler la fonction handleTotal

Maintenant que nous avons une fonction pour calculer le total, nous devons l'appeler au moment approprié. Nous ne calculons le total qu'après qu'un utilisateur a entré son deuxième opérateur.

Pour gérer cela, nous devrons apporter une modification à notre fonction `handleOperator` existante. Précédemment, nous assignions à la variable opérateur la valeur du bouton opérateur que l'utilisateur a cliqué. Maintenant, nous devons savoir si c'est le premier opérateur que l'utilisateur a cliqué ou non. Nous ne calculons pas un total lorsque l'utilisateur clique sur le premier opérateur.

Pour tenir compte de cela, nous pouvons vérifier si la variable opérateur a une valeur de `''`. Si c'est le cas, c'est le premier opérateur. Si l'opérateur a une valeur, alors nous voudrons calculer un total.

Voici à quoi ressemble la fonction handleOperator() maintenant :

```
function handleOperator(oper) {    if (operator === '') {        operator = oper;    } else {        handleTotal();        operator = oper;    }             }
```

#### Déplacement du script vers le fichier app.js

Actuellement, notre code HTML et JavaScript sont tous contenus dans le fichier index.html. Nous voulons séparer la logique dans un fichier distinct. Je crée un nouveau fichier appelé `app.js`.

Je copie l'intégralité du contenu de la balise `<script>` dans ce fichier. Je supprime la balise d'ouverture `<script>` et la balise de fermeture `</script>` dans mon fichier index.html.

La dernière chose que nous devons faire est d'indiquer à notre fichier index.html où se trouvent nos scripts. Nous faisons cela en ajoutant cette ligne sous la balise `<script>` qui charge jQuery au bas du fichier index.html :

```
<script src="app.js"></script>
```

#### Fichiers finaux

J'ai maintenant ces trois fichiers :

* index.html
* app.js
* style.css

Le fichier **index.html** est utilisé pour afficher la calculatrice à l'utilisateur sur la page web.

Le fichier **style.css** est utilisé pour styliser ma calculatrice. Veuillez consulter mon article précédent qui parle de [l'utilisation de la propriété CSS border-radius](https://medium.freecodecamp.org/learn-css-border-radius-property-by-building-a-calculator-53497cd8071d) pour styliser la calculatrice.

Le fichier **app.js** contient la logique derrière la calculatrice.

Voici à quoi ressemble mon fichier app.js :

```
let num1 = '';let num2 = '';let operator = '';let total = '';
```

```
$(document).ready(function() {    $('button').on('click', function(e) {        let btn = e.target.innerHTML;        if (btn >= '0' && btn <= '9') {            handleNumber(btn);        } else {            handleOperator(btn);        }    });});
```

```
function handleNumber(num) {    if (num1 === '') {        num1 = num;    } else {        num2 = num;    }    displayButton(num);}
```

```
function handleOperator(oper) {    if (operator === '') {        operator = oper;    } else {        handleTotal();        operator = oper;    }}
```

```
function handleTotal() {    switch (operator) {        case '+':            total = +num1 + +num2;            displayButton(total);            break;        case '-':            total = +num1 - +num2;            displayButton(total);            break;        case '/':            total = +num1 / +num2;            displayButton(total);            break;        case 'X':            total = +num1 * +num2;            displayButton(total);            break;    }    updateVariables();}
```

```
function displayButton(btn) {    $('.calc-result-input').text(btn);}
```

```
function updateVariables() {    num1 = total;    num2 = '';}
```

#### Résumé

Notre calculatrice fonctionne, mais seulement si l'utilisateur clique sur l'opérateur `+`. Vous pouvez ajouter à la fonctionnalité dans la fonction handleTotal pour tenir compte de tous les opérateurs. J'ai toute la fonctionnalité [dans mon dépôt que vous pouvez trouver ici](https://github.com/ratracegrad/programming-a-calculator).

#### Lectures complémentaires

[Recherche en largeur d'abord en JavaScript](https://hackernoon.com/breadth-first-search-in-javascript-e655cd824fa4) — Les deux méthodes les plus courantes pour rechercher un graphe ou un arbre sont la recherche en profondeur d'abord et la recherche en largeur d'abord. Cet article vous montre comment utiliser une recherche en largeur d'abord d'un graphe ou d'un arbre.

[Modèles d'instanciation en JavaScript](https://medium.com/dailyjs/instantiation-patterns-in-javascript-8fdcf69e8f9b) — Les modèles d'instanciation sont des moyens de créer quelque chose en JavaScript. JavaScript fournit quatre méthodes différentes pour créer des objets. Apprenez à créer les quatre dans cet article.

[Utilisation de Node.js & Express.js pour sauvegarder des données dans une base de données MongoDB](https://codeburst.io/hitchhikers-guide-to-back-end-development-with-examples-3f97c70e0073) — La pile MEAN est utilisée pour décrire le développement utilisant MongoDB, Express.js, Angular.jS et Node.js. Dans ce tutoriel, je vais vous montrer comment utiliser Express.js, Node.js et MongoDB.js. Nous allons créer une application Node très simple, qui permettra aux utilisateurs de saisir des données qu'ils souhaitent stocker dans une base de données MongoDB.