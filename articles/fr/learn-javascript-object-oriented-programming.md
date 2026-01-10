---
title: Apprendre la programmation orientée objet en JavaScript en créant une application
  de minuterie
subtitle: ''
author: Miya Liu
co_authors: []
series: null
date: '2023-04-11T17:06:00.000Z'
originalURL: https://freecodecamp.org/news/learn-javascript-object-oriented-programming
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/
seo_title: Apprendre la programmation orientée objet en JavaScript en créant une application
  de minuterie
---

.jpg
tags:
- name: JavaScript
  slug: javascript
- name: Programmation Orientée Objet
  slug: programmation-orientee-objet
seo_title: null
seo_desc: 'Dans cet article, vous apprendrez la programmation orientée objet en JavaScript
  en créant une simple application de minuterie.

  La programmation orientée objet est un paradigme de programmation important. Elle organise le code
  en objets ce qui le rend plus facile à gérer et à maintenir...'
---

Dans cet article, vous apprendrez la programmation orientée objet en JavaScript en créant une simple application de minuterie.

La programmation orientée objet est un paradigme de programmation important. Elle organise le code en objets ce qui le rend plus facile à gérer et à maintenir vos applications.

De nombreux articles expliquent en détail les avantages de la programmation orientée objet et comment vous pouvez l'utiliser pour construire des applications.

Mais les débutants peuvent avoir des questions : Pourquoi devrais-je appliquer la programmation orientée objet ? Quand devrais-je l'utiliser ?

Cet article aidera les débutants à comprendre ces questions en construisant la même fonctionnalité de minuterie basée sur les méthodes de programmation procédurale et orientée objet.

## Ce que nous allons couvrir

- Les bases du HTML, telles que les méthodes DOM et les événements DOM
- Les bases du CSS, comme les dispositions flexibles
- Les connaissances JavaScript, telles que les expressions régulières, les `class`es, les `constructor()`s, les objets, le mot-clé `this`, la méthode `setInterval()`, les mécanismes d'événements, et ainsi de suite.

## Table des matières

- [Comment créer une interface de minuterie avec HTML et CSS](#heading-comment-creer-une-interface-de-minuterie-avec-html-et-css)
- [Comment construire une minuterie en utilisant la programmation procédurale](#heading-comment-construire-une-minuterie-en-utilisant-la-programmation-procedurale)
  - [Construire les fonctions de base](#heading-construire-les-fonctions-de-base)
  - [Comment restreindre la plage de saisie des heures, minutes et secondes](#heading-comment-restreindre-la-plage-de-saisie-des-heures-minutes-et-secondes)
  - [Comment optimiser le format des heures, minutes et secondes](#heading-comment-optimiser-le-format-des-heures-minutes-et-secondes)
- [Comment construire une minuterie en utilisant la programmation orientée objet](#heading-comment-construire-une-minuterie-en-utilisant-la-programmation-orientee-objet)
  - [Nouvelle classe Timer](#heading-nouvelle-classe-timer)
  - [Mise à jour du Timer](#heading-mise-a-jour-du-timer)
  - [Démarrer le Timer](#heading-demarrer-le-timer)
  - [Arrêter le Timer](#heading-arreter-le-timer)
  - [Mettre en pause le Timer](#heading-mettre-en-pause-le-timer)
  - [Afficher l'heure actuelle](#heading-afficher-lheure-actuelle)
  - [Créer des instances d'objets](#heading-creer-des-instances-dobjets)
  - [Interaction de l'interface utilisateur avec les fonctions](#heading-interaction-de-linterface-utilisateur-avec-les-fonctions)
- [Comment ajouter le mécanisme d'événement à la programmation orientée objet](#heading-comment-ajouter-le-mecanisme-devenement-a-la-programmation-orientee-objet)
  - [Créer le générateur d'événements](#heading-creer-le-generateur-devenements)
  - [Nouvelle classe Timer](#heading-nouvelle-classe-timer)
  - [Créer des instances d'objets](#heading-creer-des-instances-dobjets)
  - [Interaction de l'interface utilisateur avec les fonctions](#heading-interaction-de-linterface-utilisateur-avec-les-fonctions)
- [Conclusion](#heading-conclusion)

<h2 id="comment-creer-une-interface-de-minuterie-avec-html-et-css">Comment créer une interface de minuterie avec HTML et CSS</h2>

Tout d'abord, écrivons une interface de minuterie de base avec HTML et CSS, incluant un champ de saisie pour afficher l'heure et quelques boutons.

<img src="https://www.freecodecamp.org/news/content/images/2023/04/image-70.png" class="center db">

Le HTML ressemble à ceci :

```html
<!DOCTYPE html>
<html>

<head>
    <title>Minuterie</title>
</head>

<body>
    <div class="container">
        <h1>Minuterie</h1>
        <div class="ipt">
            <input id="inputh" type="number" placeholder="heure">
            <input id="inputm" type="number" placeholder="minute">
            <input id="inputs" type="number" placeholder="seconde">
        </div>
        <div class="btn">
            <button id="btn-start" onclick="start_counting()">Démarrer</button>
            <button id="btn-pause" onclick="pause_counting()">Pause</button>
            <button id="btn-stop" onclick="end_counting()">Arrêter</button>
        </div>
        <p id="currentTime">heure actuelle : </p>
    </div>
</body>
```

La minuterie contient trois éléments de saisie, avec des `id` de `inputh`, `inputm` et `inputs`, et des `type`s de `number`. Ceux-ci permettent à l'utilisateur de saisir les valeurs des heures, minutes et secondes.

Sous le champ de saisie, trois éléments `button` démarrent, mettent en pause et arrêtent la minuterie, respectivement. 

Chaque bouton a un événement `onclick`. La valeur de la propriété de l'`onclick` est une fonction, et nous écrirons le code pour cette fonction dans la section JavaScript. Lorsque l'utilisateur clique sur un bouton, la fonction correspondante est exécutée. 

En JavaScript, nous appelons la fonction par son nom, donc nous devons mettre des parenthèses après le nom de la fonction.

Vous pouvez en apprendre plus sur l'événement `onclick` dans [cet article](https://www.freecodecamp.org/news/html-button-onclick-javascript-click-event-tutorial/).

L'élément `p` sous le bouton synchronise l'heure dans les éléments de saisie.

Ajoutons un peu de CSS simple à la minuterie et stylisons-la :

```css
<style>
    .container {
        margin: 0 auto;
        width: 300px;
        height: 300px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }

    .ipt {
        margin: 0 auto;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    input {
        width: 100px;
        height: 50px;
        font-size: 20px;
        text-align: center;
    }

    .btn {
        margin: 10px;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    button {
        margin: 10px 10px;
        width: 50px;
        height: 30px;
        font-size: 10px;
    }

    #currentTime {
        margin: 10px;
        color: green;
    }
</style>
```

Nous utilisons Flexbox pour centrer les éléments. Ajoutez le CSS ci-dessous à l'élément parent :

```css
display: flex;
justify-content: center;
align-items: center;
```

Cela centre l'élément enfant horizontalement et verticalement, par rapport à l'élément parent.

Vous pouvez voir plus d'informations sur [CSS Layout](https://www.freecodecamp.org/news/how-to-center-a-div-with-css-10-different-ways/) dans cet article, ou vous pouvez styliser davantage la minuterie comme vous le souhaitez.

Ensuite, nous ajouterons le code JavaScript pour démarrer, mettre en pause et arrêter la minuterie.

<h2 id="timer-pp">Comment construire une minuterie en utilisant la programmation procédurale</h2>

<h3 id="basic-functions"> Construire les fonctions de base</h3>

Ce code montre un programme de minuterie conçu avec un état d'esprit procédural piloté par événements consistant en :

- 2 ensembles de variables globales : les variables heure/minute/seconde et la valeur de retour de la fonction `setInterval()`
- 4 fonctions clés : les gestionnaires d'événements pour les boutons démarrer, pause et arrêter, et la fonction d'exécution qui est appelée en boucle pendant le compte à rebours

Tout d'abord, initialisez l'état du bouton avec la méthode DOM `document.getElementById().disabled`.

```javascript
// initialiser l'état du bouton
document.getElementById("btn-pause").disabled = true;
document.getElementById("btn-stop").disabled = true;
```

Ensuite, nous définissons des variables globales pour stocker les valeurs d'heure, de minute et de seconde.

```javascript
// définir des variables globales
var timer = null; // stocke la valeur retournée par le timer
var h = 0; // stocke la valeur de l'heure
var m = 0; // stocke la valeur de la minute
var s = 0; // stocke la valeur de la seconde
```

Dans la fonction `start_counting()` qui démarre la minuterie, nous utilisons `document.getElementById().value` pour obtenir les valeurs des éléments avec les `id` `inputh`, `inputm` et `inputs`, respectivement. Ce sont les valeurs des heures, minutes et secondes saisies par l'utilisateur dans le champ de saisie de la minuterie, et nous attribuons des valeurs à `h`, `m` et `s`.

Ensuite, nous vérifions les valeurs d'heure, de minute et de seconde saisies par l'utilisateur via l'instruction `if`. Si les valeurs sont toutes égales à 0, ou si l'une des valeurs est inférieure à 0, cela affiche le message popup `Le temps saisi est invalide !` et retourne, et le programme arrête l'exécution.

Attribuez la valeur `setInterval()` à la variable de timer `timer`. Cette méthode prend deux arguments, le premier étant une fonction et le second étant un temps en millisecondes. Dans cet exemple, nous spécifions que le timer exécute une fonction `counting` toutes les 1000 millisecondes (c'est-à-dire 1 seconde), qui est décrite ci-dessous.

Pour plus d'informations sur la méthode `setInterval()`, vous pouvez consulter la [documentation MDN](https://developer.mozilla.org/en-US/docs/Web/API/setInterval).

Après cela, changez l'état des boutons et des champs de saisie pour interdire aux utilisateurs de resaisir des nombres.

```javascript
// définir une fonction
// démarrer le timer
function start_counting() {
    // obtenir le temps saisi ou définir une valeur par défaut
    h = +document.getElementById("inputh").value || h;
    m = +document.getElementById("inputm").value || m;
    s = +document.getElementById("inputs").value || s;

    // vérifier les entrées invalides
    if (
        (h == 0 && m == 0 && s == 0) ||
        (h < 0 || m < 0 || s < 0)
    ) {
        alert("Le temps saisi est invalide !");
        return;
    }

    // démarrer le timer
    timer = setInterval(counting, 1000);

    // changer l'état des boutons et des champs de saisie pour interdire aux utilisateurs de resaisir des nombres
    document.getElementById("btn-start").disabled = true;
    document.getElementById("btn-pause").disabled = false;
    document.getElementById("btn-stop").disabled = false;
    document.getElementById("inputh").disabled = true;
    document.getElementById("inputm").disabled = true;
    document.getElementById("inputs").disabled = true;
}
```

Ensuite, dans la fonction `pause_counting()`, qui est responsable de la mise en pause du timer, vous définissez l'état des boutons et des champs de saisie lorsque le timer est en pause, et appelez `clearInterval()` pour supprimer le timer et arrêter le compte à rebours.

```javascript
// mettre en pause le timer
function pause_counting() {
    // changer l'état des boutons et des champs de saisie pour permettre aux utilisateurs de resaisir des nombres
    document.getElementById("btn-start").disabled = false;
    document.getElementById("btn-pause").disabled = true;
    document.getElementById("btn-stop").disabled = false;
    document.getElementById("inputh").disabled = false;
    document.getElementById("inputm").disabled = false;
    document.getElementById("inputs").disabled = false;

    // mettre en pause le timer
    clearInterval(timer);
}
```

La fonction `end_counting()` met fin au timer. Elle appelle également `clearInterval()`, et réinitialise les heures, minutes et secondes à 0. Le texte ci-dessous, "Heure actuelle :", est mis à jour en "Minuterie arrêtée".

```javascript
// arrêter le timer
function end_counting() {
    // changer l'état des boutons et des champs de saisie pour permettre aux utilisateurs de resaisir des nombres
    document.getElementById("btn-start").disabled = false;
    document.getElementById("btn-pause").disabled = true;
    document.getElementById("btn-stop").disabled = true;
    document.getElementById("inputh").disabled = false;
    document.getElementById("inputm").disabled = false;
    document.getElementById("inputs").disabled = false;

    // arrêter le timer
    clearInterval(timer);

    // réinitialiser les variables de temps
    h = 0;
    m = 0;
    s = 0;
    document.getElementById("currentTime").innerHTML = "Minuterie arrêtée";
}
```

Ensuite, la fonction `counting()`, qui est la fonction appelée dans `setInterval()`. Elle vérifie si l'heure, la minute ou la seconde est 0 avec une instruction `if`, et effectue l'action relative. 

C'est l'implémentation conventionnelle pour les timers, et elle est facile à comprendre avec notre expérience de la vie quotidienne, par exemple, lorsque le nombre de secondes atteint 0, il devient alors 59 en "empruntant" 1 au nombre de minutes – comme ceci : 00:03:02, 00:03:01, 00:03:00, 00:02:59...

La méthode `setInterval()` met à jour les valeurs de `h`, `m` et `s` une fois par seconde. Nous synchronisons le temps mis à jour dans le texte `heure actuelle :` en utilisant `document.getElementById().innerHTML`.

Enfin, l'instruction `if` vérifie les valeurs d'heure, de minute et de seconde, et lorsque les trois valeurs sont 0, la fonction `end_counting()` et la fonction `setTimeout()` sont exécutées. Dans la fonction `setTimeout()`, exécutez le message popup "Le temps est écoulé !".

> Voici un fait intéressant : vous pouvez essayer de supprimer `setTimeout()` et d'exécuter `alert("Le temps est écoulé !")` directement après `end_counting()`, vous verrez que la popup bloque le rendu du DOM - c'est-à-dire qu'elle fait apparaître le "Le temps est écoulé !" puis change l'état du bouton et des champs de saisie. Lorsque nous utilisons `setTimeout()`, ces deux actions se produisent de manière synchrone. Vous pouvez réfléchir à la fonction de `setTimeout()` ici.

Si vous voulez en savoir plus sur l'utilisation de `setTimeout()`, consultez [cet article](https://www.freecodecamp.org/news/javascript-wait-how-to-sleep-n-seconds-in-js-with-settimeout/) sur freeCodeCamp.

```javascript
// compte à rebours
function counting() {
    // vérifier si la seconde est 0
    if (s == 0) {
        // vérifier si la minute est 0 lorsque la seconde est 0
        if (m == 0) {
            // le temps saisi a déjà été vérifié pour sa légalité avant de démarrer le timer, donc il n'est pas nécessaire de vérifier à nouveau la valeur de la variable h ici
            h--;
            m = 59;
            s = 59;
        } else {
            // lorsque la minute n'est pas 0, la minute moins 1 et la seconde devient 59
            m--;
            s = 59;
        }
    } else {
        // lorsque la seconde n'est pas 0, la seconde moins 1
        s--;
    }

    // afficher l'heure actuelle
    document.getElementById("currentTime").innerHTML = "heure actuelle : " + h + " h " + m + " m " + s + " s";
    document.getElementById("inputh").value = h;
    document.getElementById("inputm").value = m;
    document.getElementById("inputs").value = s;

    // vérifier si la seconde est 0
    if (s == 0) {
        // lorsque la seconde est 0, vérifier si la minute est 0
        if (m == 0) {
            // lorsque la minute est 0, vérifier si l'heure est 0
            if (h == 0) {
                // lorsque l'heure est 0, arrêter le timer
                // arrêter le timer
                end_counting();
                // exécuter la popup dans la prochaine boucle d'événements pour l'empêcher de bloquer le rendu du DOM
                setTimeout(function () {
                    alert("Le temps est écoulé !");
                }, 0);
                return;
            }
        }
    }
}
```

Parfois, l'utilisateur peut entrer un nombre négatif dans les champs de saisie des heures, minutes ou secondes, et le code alerte l'utilisateur en faisant apparaître "Le temps saisi est invalide !". D'autres fois, l'utilisateur peut entrer des heures supérieures à 24, ou des minutes et secondes supérieures à 59, ce qui ne fonctionne pas non plus.

De plus, pour rendre l'affichage de l'heure plus beau, nous pouvons vouloir afficher les heures, minutes et secondes sur deux chiffres.

Nous pouvons améliorer le code ci-dessus de deux manières.

<h3 id="inputs-range">Comment restreindre la plage de saisie des heures, minutes et secondes</h3>

Lorsque le nombre d'heures saisi est supérieur à 24, nous voulons le modifier automatiquement à 24. De même, lorsqu'il est inférieur à 0, nous voulons le modifier à 0.

Et lorsque le nombre de minutes et de secondes saisi est supérieur à 59, nous voulons qu'il soit automatiquement modifié à 59. Lorsqu'il est inférieur à 0, le modifier à 0.

La méthode d'écouteur d'événement `addEventListener()` est utilisée ici pour exécuter la fonction lorsque l'événement `input` se produit. `parseInt()` est également utilisé pour convertir les valeurs de saisie en types numériques.

```javascript
var inputh = document.getElementById("inputh");
inputh.addEventListener("input", function() { 
    inputh.value = parseInt(inputh.value||0);
    if (inputh.value > 24) inputh.value = 24;
    if (inputh.value < 0) inputh.value = 0;
});

var inputm = document.getElementById("inputm");
inputm.addEventListener("input", function() {
    inputm.value = parseInt(inputm.value||0);
    if (inputm.value > 59) inputm.value = 59;
    if (inputm.value < 0) inputm.value = 0;
});

var inputs = document.getElementById("inputs");
inputs.addEventListener("input", function() {
    inputs.value = parseInt(inputs.value||0);
    if (inputs.value > 59) inputs.value = 59;
    if (inputs.value < 0) inputs.value = 0;
});
```

<h3 id="inputs-format">Comment optimiser le format des heures, minutes et secondes</h3>

Lorsque les nombres d'heures, de minutes ou de secondes sont à un seul chiffre, nous pouvons les préfixer avec 0 en utilisant une expression régulière.

```javascript
h = h.toString();
m = m.toString();
s = s.toString();
if (h.match(/^\d$/)) { // Si l'heure est un seul chiffre, ajouter 0 au début
    h = "0" + h;
}
if (m.match(/^\d$/)) { // Si la minute est un seul chiffre, ajouter 0 au début
    m = "0" + m;
}
if (s.match(/^\d$/)) { // Si la seconde est un seul chiffre, ajouter 0 au début
    s = "0" + s;
}
```

<img src="https://www.freecodecamp.org/news/content/images/2023/04/pp.gif" class="center db">

Vous pouvez voir la démonstration en ligne [demo](https://codepen.io/miyaliu666-the-styleful/pen/VwEYwoJ) sur CodePen :

<p class="codepen" data-height="300" data-default-tab="js,result" data-slug-hash="VwEYwoJ" data-preview="true" data-editable="true" data-user="miyaliu666-the-styleful" style="height: 300px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid; margin: 1em 0; padding: 1em;">
  <span>See the Pen <a href="https://codepen.io/miyaliu666-the-styleful/pen/VwEYwoJ">
  pp</a> by miyaliu666 (<a href="https://codepen.io/miyaliu666-the-styleful">@miyaliu666-the-styleful</a>)
  on <a href="https://codepen.io">CodePen</a>.</span>
</p>
<script async src="https://cpwebassets.codepen.io/assets/embed/ei.js"></script>

D'accord, nous avons construit une minuterie !

Vous pourriez penser : et si je veux ajouter plusieurs minuteries à un projet ?

Dans ce cas, vous devrez définir différents `id`s pour chaque champ `input` de la minuterie afin que `document.getElementById().value` obtienne la valeur correspondante.

Par exemple, pour la minuterie n°1 avec l'`id` `inputh1`, nous attribuons `h1 = +document.getElementById("inputh1").value` à `start_counting()`. Pour la minuterie n°2 avec l'`id` `inputh2`, nous attribuons `h2 = +document.getElementById("inputh1").value`, et ainsi de suite.

Le projet réel n'est généralement pas aussi simple que de créer un tas de minuteries. Comme vous pouvez l'imaginer, le code peut facilement devenir long et désordonné.

Il est donc temps d'introduire la programmation orientée objet.

<h2 id="timer-oop">Comment construire une minuterie en utilisant la programmation orientée objet</h2>

Vous avez peut-être entendu des développeurs dire qu'ils doivent "créer un objet" à certaines occasions - comme si vous pouviez obtenir ce que vous voulez en utilisant simplement le mot-clé `new`. Derrière cela se cache le concept de programmation orientée objet.

Dans cette section, nous allons refactoriser la minuterie de la section précédente avec la programmation orientée objet, en séparant la "fonction de minuterie" de l'"interaction de l'interface utilisateur".

Le HTML et le CSS sont similaires à la section précédente, donc nous ne les passerons pas en revue ici. Vous pouvez voir l'ensemble du code dans [cette démonstration CodePen](https://codepen.io/miyaliu666-the-styleful/pen/oNaggXR).

<p class="codepen" data-height="300" data-default-tab="js,result" data-slug-hash="oNaggXR" data-preview="true" data-editable="true" data-user="miyaliu666-the-styleful" style="height: 300px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid; margin: 1em 0; padding: 1em;">
  <span>See the Pen <a href="https://codepen.io/miyaliu666-the-styleful/pen/oNaggXR">
  oop</a> by miyaliu666 (<a href="https://codepen.io/miyaliu666-the-styleful">@miyaliu666-the-styleful</a>)
  on <a href="https://codepen.io">CodePen</a>.</span>
</p>
<script async src="https://cpwebassets.codepen.io/assets/embed/ei.js"></script>

Si vous avez suivi le cours de [Programmation Orientée Objet](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/object-oriented-programming/) de freeCodeCamp, vous vous souviendrez probablement que "les objets en JavaScript sont utilisés pour modéliser des objets du monde réel, leur donnant des propriétés et des comportements tout comme leurs homologues du monde réel", comme les voitures, les magasins et les oiseaux.

Alors commençons par définir les propriétés et les méthodes (comportement) des objets :)

<h3 id="new-class-1">Nouvelle classe Timer</h3>

Le mot-clé `class` crée une classe nommée `Timer` qui a un `constructor()` avec les méthodes `_on_update()`, `start()`, `stop()`, `pause()`, et `show()`.

```javascript
<script>
    class Timmer {
        constructor() {
            this.name = 'undefined';
            this.timmer = undefined;
            this.h = 0;
            this.m = 0;
            this.s = 10;

            this._on_update_callback = undefined;
            this._on_stop_callback = undefined;
        }

        _on_update() {

        }

        start() {

        }

        stop() {

        }

        pause() {

        }

        show() {

        }
    }

</script>
```

Selon [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/constructor),

> La méthode **`constructor`** est une méthode spéciale d'une [classe](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes) pour créer et initialiser une instance d'objet de cette classe.

Dans celle-ci, nous initialisons plusieurs variables – c'est-à-dire des propriétés de l'objet – avec le mot-clé `this`. 

En JavaScript, la valeur de `this` dépend du contexte. Dans ce cas, il fait référence à l'objet qui appelle la fonction, c'est-à-dire une instance de `Timer`. 

Nous utilisons également `this` pour initialiser la fonction de rappel `_on_update_callback` lorsque le timer est mis à jour et la fonction de rappel `_on_stop_callback` lorsque le timer est arrêté.

Les méthodes `_on_update()`, `start()`, `stop()`, `pause()`, et `show()` sont utilisées pour mettre à jour, démarrer, arrêter et mettre en pause le timer, et afficher l'heure actuelle, respectivement. Nous ajouterons du code pour elles étape par étape.

<h3 id="timer-update">Mise à jour du Timer</h3>

Nous allons gérer la mise à jour du timer en utilisant la méthode `_on_update()`. Comme ci-dessus, nous utiliserons toujours l'instruction `if` pour exécuter le code lorsque les heures, minutes et secondes sont à 0.

Appeler la fonction de rappel externe `_on_update_callback` si elle existe.

```javascript
_on_update() { 
    if (0 === this.h && 0 === this.m && 0 === this.s) {
        this.stop();
        return;
    } else if (0 === this.s) {
        this.s = 59;
        if (0 === this.m) {
            this.m = 59;
            this.h = this.h - 1;
        } else {
            this.m = this.m - 1;
        }
    } else {
        this.s = this.s - 1;
    }

    this.show();
    if (0 === this.h && 0 === this.m && 0 === this.s) {
        this.stop();
    }

    // appeler la fonction de rappel externe si elle existe
    if (this._on_update_callback && typeof this._on_update_callback === 'function') {
        this._on_update_callback();
    }
}
```

<h3 id="timer-start">Démarrer le Timer</h3>

Nous utilisons la méthode `start()` pour démarrer le compte à rebours – c'est-à-dire qu'elle est exécutée après que l'utilisateur a cliqué sur le bouton `Start`. Avec la méthode `setInterval()`, `_on_update()` est exécutée une fois par seconde.

```javascript
start() {
    if (this.timmer) {
        console.log(`[${this.name}] démarré`);
        return;
    }
    console.log(`[${this.name}] démarre`);
    this.timmer = setInterval(() => {
        this._on_update();
    }, 1000);
    this.show();
}
```

<h3 id="timer-stop">Arrêter le Timer</h3>

La méthode `stop()` est utilisée pour arrêter le timer. Utilisez `clearInterval()` pour arrêter le compte à rebours. Appelez la fonction de rappel externe `_on_stop_callback()` si elle existe.

```javascript
stop() {
    console.log(`[${this.name}] arrêté`);
    clearInterval(this.timmer);
    this.timmer = undefined;

    // similaire à la mise à jour, vérifier la fonction de rappel d'arrêt
    if (this._on_stop_callback && typeof this._on_stop_callback === 'function') {
        this._on_stop_callback();
    }
}
```

<h3 id="timer-pause">Mettre en pause le Timer</h3>

Utilisez la méthode `pause()` pour mettre en pause le timer et utilisez `clearInterval()` pour arrêter le compte à rebours.

```javascript
pause() {
    console.log(`[${this.name}] mis en pause`);
    clearInterval(this.timmer);
    this.timmer = undefined;
}
```

<h3 id="show-current-time">Afficher l'heure actuelle</h3>

Utilisez la méthode `show()` pour imprimer l'heure actuelle sur la console.

```javascript
show() { // afficher l'heure actuelle
    console.log(`[${this.name}] heure actuelle : ${this.h}:${this.m}:${this.s}`);
}
```

<h3 id="create-objects-1">Créer des instances d'objets</h3>

Ensuite, utilisez le mot-clé `new` pour créer deux instances d'objets, c'est-à-dire deux timers, qui ont les propriétés et méthodes de l'objet `Timer`.

Selon [MDN](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Operators/new),

> L'opérateur **`new`** permet aux développeurs de créer une instance d'un type d'objet défini par l'utilisateur ou de l'un des types d'objets intégrés qui a une fonction constructeur.

Attribuez deux objets à `t1` et `t2` et placez-les dans le tableau `list_timmer`. Créez également un tableau de sons `list_sound`, que nous utiliserons plus tard.

```javascript
const t1 = new Timmer();
t1.name = 'Timer 1';
const t2 = new Timmer();
t2.name = 'Timer 2';
const list_timmer = [t1, t2];
const list_sound = ['meow', 'woof'];
```

<h3 id="UI-with-functions-1">Interaction de l'interface utilisateur avec les fonctions</h3>

Ensuite, nous allons créer 6 fonctions.

La première fonction, `play_audio()`, a un argument. La fonction crée un élément `audio` dans le DOM et l'attribue à `audio`. Ensuite, elle définit la valeur de la propriété `src` à une [littérale de gabarit](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals) et appelle sa méthode `play()` pour jouer le son.

```javascript
function play_audio(sound) {
    // meow.mp3 et woof.mp3 sont des fichiers locaux et doivent être dans le même répertoire que le fichier HTML
    const audio = document.createElement('audio');
    audio.src = `${sound}.mp3`;
    audio.play();
}
```

La deuxième fonction, `btn_start_onclick()`, a un argument, `i`. Cette fonction est appelée lorsque les boutons "start" des deux timers sont cliqués, passant soit 1 soit 2 comme argument :

```html
<input id="tmr-1-btn-start" class=" btn" type="button" value="start" onclick="btn_start_onclick(1)" />
```

```html
<input id="tmr-2-btn-start" class="btn" type="button" value="start" onclick="btn_start_onclick(2)" />
```

La fonction obtient d'abord la valeur du champ de saisie et l'attribue au timer. Ensuite, elle définit l'état du champ de saisie et du bouton avec la fonction `dom_update_inputs()`. Nous définirons `dom_update_inputs()` plus tard.

**Rappelez-vous que nous avons initialisé deux fonctions de rappel au début ? Ici, nous allons leur attribuer une fonction fléchée.**

`_on_stop_callback` exécute la fonction de rappel `dom_update_inputs`, que nous discuterons ci-dessous.

La fonction de rappel `play_audio()` est également exécutée ici avec l'argument `list_sound[i - 1]`, c'est-à-dire qu'elle prend l'élément `meow` ou `woof` du tableau `list_sound` défini précédemment et le passe à la propriété `src` de `audio` pour jouer le son correspondant lorsque le timer est arrêté. Par exemple, lorsque `i` est 1, `audio.src = meow.mp3;`.

`_on_update_callback` exécute la fonction de rappel ` dom_update_timmer()`, dont nous parlerons bientôt.

Prenez le timer correspondant dans le tableau des timers via `const tmr = list_timmer[i - 1];` et exécutez la méthode `start()` pour démarrer le timer.

```javascript
function btn_start_onclick(i) {
    // obtenir la valeur de saisie
    const ipt_h = document.getElementById(`ipt-${i}-h`);
    const ipt_m = document.getElementById(`ipt-${i}-m`);
    const ipt_s = document.getElementById(`ipt-${i}-s`);

    // définir l'état des champs de saisie et des boutons
    dom_update_inputs(i, "COUNTING");
    // prendre le timer correspondant dans le tableau des timers
    const tmr = list_timmer[i - 1];
    // attribuer la valeur de saisie au timer
    tmr.h = Number(ipt_h.value);
    tmr.m = Number(ipt_m.value);
    tmr.s = Number(ipt_s.value);

    // définir la fonction de rappel
    tmr._on_stop_callback = () => {
        // jouer le son
        play_audio(list_sound[i - 1]);
        // définir l'état des champs de saisie et des boutons
        dom_update_inputs(i, "STOPPED");
    }
    tmr._on_update_callback = () => {
        dom_update_timmer(i);
    }
    // démarrer le timer
    tmr.start();
}
```

La troisième fonction, `btn_pause_onclick()`, a un argument et est appelée lorsque les boutons `pause` des deux timers sont cliqués, passant soit 1 soit 2. La fonction de rappel, `dom_update_inputs`, est exécutée pour définir l'état des champs de saisie et des boutons, et la méthode `pause()` est exécutée pour mettre en pause le timer.

```javascript
function btn_pause_onclick(i) {
    dom_update_inputs(i, "PAUSED");

    // prendre le timer correspondant dans le tableau des timers
    const tmr = list_timmer[i - 1];

    // mettre en pause le timer
    tmr.pause();
}
```

La quatrième fonction, `btn_stop_onclick()`, est similaire à la troisième fonction. Elle est appelée lorsque les boutons "stop" des deux timers sont cliqués, et définit l'état des champs de saisie et des boutons lorsque le timer est arrêté. Ensuite, la méthode `stop()` est exécutée pour arrêter le timer.

```javascript
function btn_stop_onclick(i) {
    dom_update_inputs(i, "STOPED");

    // prendre le timer correspondant dans le tableau des timers
    const tmr = list_timmer[i - 1];


    // arrêter le timer
    tmr.stop();
}
```

La cinquième fonction `dom_update_inputs()` a deux arguments, `i` et `status`. Elle définit l'état des champs de saisie et des boutons via des instructions `if.... .else if... ` lorsque `status` est rencontré. 

Lorsque cette fonction est appelée dans les deuxième, troisième et quatrième fonctions ci-dessus, elle définit l'état des champs de saisie et des boutons lorsque le timer est démarré, mis en pause et arrêté.

```javascript
function dom_update_inputs(i, status) {
    if ('COUNTING' === status) {
        // définir l'état des champs de saisie
        document.getElementById(`ipt-${i}-h`).disabled = true;
        document.getElementById(`ipt-${i}-m`).disabled = true;
        document.getElementById(`ipt-${i}-s`).disabled = true;

        // définir l'état des boutons
        document.getElementById(`tmr-${i}-btn-start`).disabled = true;
        document.getElementById(`tmr-${i}-btn-pause`).disabled = false;
        document.getElementById(`tmr-${i}-btn-stop`).disabled = false;
    } else if ('PAUSED' === status) {
        // définir l'état des champs de saisie
        document.getElementById(`ipt-${i}-h`).disabled = false;
        document.getElementById(`ipt-${i}-m`).disabled = false;
        document.getElementById(`ipt-${i}-s`).disabled = false;

        // définir l'état des boutons
        document.getElementById(`tmr-${i}-btn-start`).disabled = false;
        document.getElementById(`tmr-${i}-btn-pause`).disabled = true;
        document.getElementById(`tmr-${i}-btn-stop`).disabled = false;
    } else if ('STOPPED' === status) {
        // définir l'état des champs de saisie
        document.getElementById(`ipt-${i}-h`).disabled = false;
        document.getElementById(`ipt-${i}-m`).disabled = false;
        document.getElementById(`ipt-${i}-s`).disabled = false;

        // définir l'état des boutons
        document.getElementById(`tmr-${i}-btn-start`).disabled = false;
        document.getElementById(`tmr-${i}-btn-pause`).disabled = true;
        document.getElementById(`tmr-${i}-btn-stop`).disabled = true;
    }
}
```

La sixième fonction `dom_update_timmer()` est utilisée pour synchroniser l'heure avec la page.

```javascript
function dom_update_timmer(i) {
    // prendre le timer correspondant dans le tableau des timers
    const tmr = list_timmer[i - 1];

    // synchroniser l'heure avec la page
    document.getElementById(`ipt-${i}-h`).value = tmr.h;
    document.getElementById(`ipt-${i}-m`).value = tmr.m;
    document.getElementById(`ipt-${i}-s`).value = tmr.s;
} 
```

Ci-dessus, nous avons encapsulé la "fonction de minuterie" dans la classe Timmer et gardé l'"interaction de l'interface utilisateur" dans la portée globale, de sorte que plusieurs minuteries en tant qu'instances de la classe Timmer peuvent fonctionner simultanément.

<img src="https://www.freecodecamp.org/news/content/images/2023/04/oop.gif" class="center db">

Dans cette section, je n'ai pas défini de limite sur la plage des entrées d'heure, de minute et de seconde ou optimisé leur format. Si vous êtes intéressé, vous pouvez vous référer au code de la section précédente et le faire vous-même dans la démonstration CodePen :)

En réfléchissant plus loin, que se passe-t-il si notre projet a d'autres modules fonctionnels en plus de cet ensemble de deux minuteries - par exemple, deux ensembles de minuteries, qui sont des instances d'objet du même type `Timer` ? Lors de l'attribution de valeurs à la fonction de rappel `_on_stop_callback`, un ensemble d'instances doit jouer un bip via la fonction `play_audio()`, tandis que l'autre ensemble doit définir la couleur de la minuterie par une autre fonction. Ensuite, la deuxième attribution écrasera la première.

Ici, nous introduirons le mécanisme d'événement pour résoudre ce problème.

<h2 id="timer-oop-with-events">Comment ajouter le mécanisme d'événement à la programmation orientée objet</h2>

Cette section est similaire à la section précédente, sauf que nous ajouterons un mécanisme d'événement pour remplacer la fonction de rappel originale. 

L'avantage du mécanisme d'événement est que plusieurs objets peuvent être notifiés lorsque l'état du timer change. Dans notre cas, lorsque l'état du timer change, il notifie les boutons sur la page afin que les états des boutons changent de manière synchrone.

Encore une fois, le HTML et le CSS sont similaires à la première section, donc je ne les répéterai pas ici.

Vous pouvez voir le code complet dans cette [démonstration CodePen](https://codepen.io/miyaliu666-the-styleful/pen/JjmooXz).

<p class="codepen" data-height="300" data-default-tab="js,result" data-slug-hash="JjmooXz" data-preview="true" data-editable="true" data-user="miyaliu666-the-styleful" style="height: 300px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid; margin: 1em 0; padding: 1em;">
  <span>See the Pen <a href="https://codepen.io/miyaliu666-the-styleful/pen/JjmooXz">
  oop_with_events</a> by miyaliu666 (<a href="https://codepen.io/miyaliu666-the-styleful">@miyaliu666-the-styleful</a>)
  on <a href="https://codepen.io">CodePen</a>.</span>
</p>
<script async src="https://cpwebassets.codepen.io/assets/embed/ei.js"></script>

<h3 id="eventemitter">Créer le générateur d'événements</h3>

Tout d'abord, nous créons une nouvelle classe `EventEmitter`, qui est un émetteur d'événements utilisé pour implémenter le mécanisme d'événement – dans ce cas, pour implémenter la notification de changement d'état du timer.

`on` est utilisé pour écouter (s'abonner à) des événements. Lorsqu'un événement se produit, une fonction de rappel est exécutée, et les paramètres de la fonction de rappel sont les paramètres de l'événement. `this` dans la fonction de rappel fait référence au déclencheur de l'événement.

`emit` est utilisé pour émettre (lancer) l'événement.

`removeListener` est utilisé pour supprimer un écouteur d'un événement.

```javascript
class EventEmitter {
    constructor() {
        this._events = {};
    }

    on(type, listener) {
        if (this._events[type]) {
            this._events[type].push(listener);
        } else {
            this._events[type] = [listener];
        }
    }

    emit(type, ...args) {
        if (this._events[type]) {
            this._events[type].forEach(listener => {
                listener(...args);
            });
        }
    }

    removeListener(type, listener) {
        if (this._events[type] && listener) {
            this._events[type] = this._events[type].filter(l => l !== listener);
        } else if (this._events[type] && !listener) {
            this._events[type] = [];
        }
    }
}
```

<h3 id="new-class-2">Nouvelle classe Timer</h3>

Ici, nous créons une nouvelle classe `Timmer`. Le mot-clé `extends` signifie que `Timmer` est une classe enfant de la classe `EventEmitter`. La classe enfant hérite de toutes les propriétés et méthodes de la classe parente.

Consultez cette [documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/extends) pour plus d'informations sur le mot-clé `extends`.

```javascript
class Timmer extends EventEmitter {
    constructor() {
        super();
        this.name = 'undefined';
        this.timmer = undefined;
        this.h = 0;
        this.m = 0;
        this.s = 10;
    }

    _on_update() {
        if (0 === this.h && 0 === this.m && 0 === this.s) {
            this.stop();
            return;
        } else if (0 === this.s) {
            this.s = 59;
            if (0 === this.m) {
                this.m = 59;
                this.h = this.h - 1;
            } else {
                this.m = this.m - 1;
            }
        } else {
            this.s = this.s - 1;
        }

        this.show()
        // émettre un événement
        this.emit('update', {
            h: this.h,
            m: this.m,
            s: this.s
        });
        if (0 === this.h && 0 === this.m && 0 === this.s) {
            this.stop();
        }
    }

    start() {
        if (this.timmer) {
            console.log(`[${this.name}] démarré`);
            return;
        }
        console.log(`[${this.name}] démarre`);
        this.timmer = setInterval(() => {
            this._on_update();
        }, 1000);
        this.show();

        // émettre un événement
        this.emit('start', {
            h: this.h,
            m: this.m,
            s: this.s
        });
    }

    stop() {
        console.log(`[${this.name}] arrêté`);
        clearInterval(this.timmer);
        this.timmer = undefined;

        // émettre un événement
        this.emit('stop', {
            h: this.h,
            m: this.m,
            s: this.s
        });
    }

    pause() {
        console.log(`[${this.name}] mis en pause`);
        clearInterval(this.timmer);
        this.timmer = undefined;

        // émettre un événement
        this.emit('pause', {
            h: this.h,
            m: this.m,
            s: this.s
        });
    }

    show() {
        console.log(`[${this.name}] heure actuelle : ${this.h}:${this.m}:${this.s}`);
    }
}
```

Dans le code ci-dessus, vous pouvez voir dans les commentaires qu'il y a quatre "lancer des événements". La méthode `emit` lance quatre événements `update`, `start`, `stop`, et `pause`, qui émettent les changements à l'intérieur du timer. Tous les objets abonnés à ces événements exécuteront les fonctions de rappel correspondantes.

<h3 id="create-objects-2">Créer des instances d'objets</h3>

De même, nous créons deux nouvelles instances d'objets timer `t1` et `t2`, et des tableaux stockant les timers et les sons attribués à `list_timmer` et `list_sound`.

```javascript
const t1 = new Timmer();
t1.name = 'Timer 1';
const t2 = new Timmer();
t2.name = 'Timer 2';
const list_timmer = [t1, t2];
const list_sound = ['meow', 'woof'];
const list_sound_str = ['🐱meow~~~', '🐶woof~woof~woof~'];
```

<h3 id="UI-with-functions-2">Interaction de l'interface utilisateur avec les fonctions</h3>

Dans ce cas, nous allons créer 6 fonctions également.

Parmi elles, `play_audio()`, `btn_pause_onclick`, `btn_stop_onclick`, `dom_update_inputs()`, `dom_update_timmer()` sont les mêmes que les fonctions de la section précédente.

Prenons la fonction `btn_start_onclick()` comme exemple pour illustrer le mécanisme d'abonnement aux événements.

```javascript
function btn_start_onclick(i) {
    // obtenir la valeur de saisie
    const ipt_h = document.getElementById(`ipt-${i}-h`);
    const ipt_m = document.getElementById(`ipt-${i}-m`);
    const ipt_s = document.getElementById(`ipt-${i}-s`);

    // définir l'état des champs de saisie et des boutons
    dom_update_inputs(i, "COUNTING");

    // prendre le timer correspondant dans le tableau des timers
    const tmr = list_timmer[i - 1];
    // attribuer la valeur de saisie au timer
    tmr.h = Number(ipt_h.value);
    tmr.m = Number(ipt_m.value);
    tmr.s = Number(ipt_s.value);

    // écouter l'événement de mise à jour du timer et synchroniser l'heure avec la page
    tmr.removeListener('update');
    tmr.removeListener('stop');
    tmr.on('update', () => dom_update_timmer(i));
    tmr.on('stop', () => {
        console.log(list_sound_str[i - 1]);
    });
    tmr.on('stop', () => {
        // jouer le son
        play_audio(list_sound[i - 1]);
        // définir l'état des champs de saisie et des boutons
        dom_update_inputs(i, "STOPPED");
    });

    // démarrer le timer
    tmr.start();
}
```

Cette fonction est appelée lorsque l'utilisateur clique sur le bouton "Start". Elle écoute l'événement `update` via la méthode `on()`, et exécute la fonction de rappel `dom_update_timmer()`.

Elle s'abonne à l'événement `stop` deux fois, exécutant différents modules de fonction - d'abord pour imprimer le texte du son dans la console, puis pour jouer un son et définir l'état des champs de saisie et des boutons (sans interférer les uns avec les autres). 

**C'est l'avantage du mécanisme d'événement par rapport à la fonction de rappel `_on_stop_callback` de la section précédente.**

Notez le `tmr.removeListener('update');` et `tmr.removeListener('stop');` au début - cela permet de supprimer l'écouteur d'événement (s'il y en a un) chaque fois que `this.start()` est exécuté.

<h2 id="conclusion">Conclusion</h2>

Dans cet article, nous avons construit des minuteries basées à la fois sur la programmation procédurale et la programmation orientée objet. Nous avons également ajouté un mécanisme d'événement à notre application construite avec la programmation orientée objet et exploré certaines bonnes pratiques du paradigme de programmation étape par étape. 

Si vous souhaitez discuter de cet article avec moi ou me donner des suggestions, veuillez m'envoyer un message sur le [Forum freeCodeCamp](https://forum.freecodecamp.org/). Mon identifiant est miyaliu.

Merci d'avoir lu cet article. Bon codage !

Image de couverture par <a href="https://unsplash.com/@yogendras31?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Yogendra Singh</a> sur <a href="https://unsplash.com/s/photos/timer?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>