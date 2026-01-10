---
title: Comment créer un clone de Wordle en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-03-01T23:35:30.000Z'
originalURL: https://freecodecamp.org/news/build-a-wordle-clone-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/pexels-skitterphoto-695571.jpg
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: JavaScript
  slug: javascript
- name: projects
  slug: projects
- name: Web Development
  slug: web-development
seo_title: Comment créer un clone de Wordle en JavaScript
seo_desc: "By Paul Akinyemi\nIn this article, you will be recreating the guessing\
  \ game Wordle. This article covers the core game logic but does not implement sharing\
  \ your results. The article also doesn't cover the functionality that generates\
  \ game statistics. \n..."
---

Par Paul Akinyemi

Dans cet article, vous allez recréer le jeu de devinettes [Wordle](https://www.nytimes.com/games/wordle/index.html). Cet article couvre la logique principale du jeu mais n'implémente pas le partage de vos résultats. L'article ne couvre pas non plus la fonctionnalité qui génère les statistiques du jeu. 

Ce tutoriel est destiné aux développeurs front-end débutants qui souhaitent construire un projet amusant en JavaScript vanilla.

Vous pouvez consulter une démonstration du projet terminé [ici](https://wordle-clone-drab.vercel.app).

## Prérequis

Ce tutoriel suppose une compréhension de base de :

* HTML
* CSS
* JavaScript
* NPM

## Comment construire le clone de Wordle

Voici les étapes que vous allez suivre pour construire le clone de Wordle :

* Installation du projet
* Création du plateau de jeu
* Création du clavier à l'écran
* Acceptation de l'entrée utilisateur
* Ajout de notifications
* Faire en sorte que le clavier à l'écran génère une entrée
* Ajout d'animations

## Installation du projet

Avant de construire le jeu, vous devez mettre en place certains composants. Tout d'abord, vous devez créer un dossier pour tout le code source de notre clone. Appelez ce dossier build. 

Après avoir fait cela, configurez votre serveur de développement.

### Live-server

Vous allez utiliser un serveur de développement appelé live-server. Cette étape est facultative, mais elle vous évite d'avoir à recharger la page après chaque modification du code source.

Installez live-server en tapant ce qui suit dans votre terminal :

```bash
npm install live-server
```

### Configuration HTML

À l'intérieur de build, créez un fichier HTML et nommez-le index.html. Placez le code suivant à l'intérieur :

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Wordle</title>
</head>
<body>
    <h1> Clone de Wordle </h1>
    
    <div id="game-board">

    </div>
</body>
</html>
```

Le code HTML crée un en-tête pour notre jeu et fait le conteneur pour le plateau de jeu.

Vous allez utiliser une bibliothèque JavaScript appelée [Toastr](https://github.com/CodeSeven/toastr) pour les notifications en jeu et une bibliothèque CSS appelée [Animate.css](https://animate.style) pour les animations du plateau. 

Pour les inclure dans votre projet, ajoutez les liens suivants à l'en-tête de votre fichier index.html.

```html
 <link href="https://cdnjs.cloudflare.com/ajax/libs/toastr.js/latest/toastr.min.css" rel="stylesheet"/>
 
<link
    rel="stylesheet"
		href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css"
  />
```

Ces liens récupéreront le CSS pour Animate.css et Toastr. Placez le code suivant dans index.html, juste avant la balise de fermeture body :

```html
<script
src="https://code.jquery.com/jquery-3.6.0.min.js"
integrity="sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4="
crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/toastr.js/latest/toastr.min.js"></script>

```

Ce code récupérera le JavaScript pour Toastr et jQuery (parce que Toastr en dépend).

### Configuration JavaScript

Votre JavaScript sera dans un fichier appelé script.js. Créez script.js et placez-le dans build.

Placez ce code en haut de script.js :

```javascript
import { WORDS } from "./words.js";

const NUMBER_OF_GUESSES = 6;
let guessesRemaining = NUMBER_OF_GUESSES;
let currentGuess = [];
let nextLetter = 0;
let rightGuessString = WORDS[Math.floor(Math.random() * WORDS.length)]
console.log(rightGuessString)
```

Ce code initialise les variables globales que nous utiliserons pour notre jeu et choisit un mot aléatoire dans le tableau `WORDS` comme étant le bon mot à deviner pour ce tour. Nous enregistrons également le bon mot dans la console, pour déboguer notre code si nécessaire. 

La liste des mots autorisés que nous utiliserons sera codée en dur et stockée sous forme de tableau dans le fichier words.js. Créez words.js, à l'intérieur de build, et copiez le JavaScript de ce [lien](https://github.com/Morgenstern2573/wordle_clone/blob/master/build/words.js) à l'intérieur.

Words.js devrait ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/03/wordsjs_screenshot-1.png)
_à quoi words.js devrait ressembler_

### Configuration CSS

Nommez votre fichier CSS style.css. Style.css doit également être placé dans build. 

```css
h1 {
 text-align: center;
}
```

La seule configuration CSS dont nous avons besoin est un peu de code pour centrer le texte de notre en-tête.

### Mettre le tout ensemble

Enfin, liez script.js en tant que module dans votre index.html, puis liez style.css.

À ce stade, votre index.html devrait ressembler à ceci :

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Wordle</title>
    <link rel="stylesheet" href="style.css">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/toastr.js/latest/toastr.min.css" rel="stylesheet"/>
    <link
    rel="stylesheet"
    href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css"
  />
</head>
<body>
    <h1> Clone de Wordle </h1>
    
    <div id="game-board">

    </div>
<script
src="https://code.jquery.com/jquery-3.6.0.min.js"
integrity="sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4="
crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/toastr.js/latest/toastr.min.js"></script>
<script src="script.js" type="module"></script>
</body>
</html>
```

et votre structure de fichiers devrait ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-from-2022-02-28-13-49-21.png)
_capture d'écran de l'arborescence des fichiers_

Démarrez live-server en tapant ceci dans votre console :

```bash
live-server build
```

C'est tout pour l'installation.

## Comment créer le plateau de jeu

Vous allez créer le plateau de jeu en écrivant une fonction JavaScript. Appelons la fonction `initBoard`. Ajoutez ce code à votre fichier script.js :

```javascript
function initBoard() {
    let board = document.getElementById("game-board");

    for (let i = 0; i < NUMBER_OF_GUESSES; i++) {
        let row = document.createElement("div")
        row.className = "letter-row"
        
        for (let j = 0; j < 5; j++) {
            let box = document.createElement("div")
            box.className = "letter-box"
            row.appendChild(box)
        }

        board.appendChild(row)
    }
}

initBoard()
```

Alors, que fait ce code ? `initBoard` crée une ligne pour chaque essai que nous donnons à l'utilisateur et crée 5 cases pour chaque ligne. Il y a une case pour chaque lettre de l'essai, et la fonction en fait toutes des enfants de la ligne. 

`initBoard` ajoute ensuite chaque ligne au conteneur du plateau. Chaque ligne reçoit la classe `letter-row`, et chaque case se voit attribuer `letter-box`.

Ensuite, vous allez styliser le plateau avec un peu de CSS. Placez le code suivant dans votre fichier style.css :

```css
#game-board {
  display: flex;
  align-items: center;
  flex-direction: column;
}

.letter-box {
  border: 2px solid gray;
  border-radius: 3px;
  margin: 2px;
  font-size: 2.5rem;
  font-weight: 700;
  height: 3rem;
  width: 3rem;
  display: flex;
  justify-content: center;
  align-items: center;
  text-transform: uppercase;
}

.filled-box {
  border: 2px solid black;
}

.letter-row {
  display: flex;
}
```

Ce CSS fait quelques choses :

* centre les lignes du plateau horizontalement et verticalement
* définit une hauteur, une largeur et une bordure pour chaque case du plateau
* crée un look distinct pour une case remplie avec une lettre

À ce stade, lorsque vous chargez index.html dans votre navigateur, cela devrait ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/screenshot1.png)
_capture d'écran du jeu_

## Comment créer le clavier à l'écran

La manière la plus simple de créer le clavier est avec HTML. Ajoutez ce code à votre index.html, après la div du plateau de jeu :

```html
   <div id="keyboard-cont">
        <div class="first-row">
            <button class="keyboard-button">q</button>
            <button class="keyboard-button">w</button>
            <button class="keyboard-button">e</button>
            <button class="keyboard-button">r</button>
            <button class="keyboard-button">t</button>
            <button class="keyboard-button">y</button>
            <button class="keyboard-button">u</button>
            <button class="keyboard-button">i</button>
            <button class="keyboard-button">o</button>
            <button class="keyboard-button">p</button>
        </div>
        <div class="second-row">
            <button class="keyboard-button">a</button>
            <button class="keyboard-button">s</button>
            <button class="keyboard-button">d</button>
            <button class="keyboard-button">f</button>
            <button class="keyboard-button">g</button>
            <button class="keyboard-button">h</button>
            <button class="keyboard-button">j</button>
            <button class="keyboard-button">k</button>
            <button class="keyboard-button">l</button>
        </div>
        <div class="third-row">
            <button class="keyboard-button">Del</button>
            <button class="keyboard-button">z</button>
            <button class="keyboard-button">x</button>
            <button class="keyboard-button">c</button>
            <button class="keyboard-button">v</button>
            <button class="keyboard-button">b</button>
            <button class="keyboard-button">n</button>
            <button class="keyboard-button">m</button>
            <button class="keyboard-button">Enter</button>
        </div>
    </div>
```

Maintenant, stylisez le balisage en ajoutant ce CSS à la fin de style.css :

```css
#keyboard-cont {
  margin: 1rem 0;
  display: flex;
  flex-direction: column;
  align-items: center;
}

#keyboard-cont div {
  display: flex;
}

.second-row {
  margin: 0.5rem 0;
}

.keyboard-button {
  font-size: 1rem;
  font-weight: 700;
  padding: 0.5rem;
  margin: 0 2px;
  cursor: pointer;
  text-transform: uppercase;
}

```

Voici à quoi devrait ressembler votre index.html dans le navigateur maintenant :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/screenshot2.png)
_capture d'écran du clavier à l'écran_

## Comment accepter l'entrée utilisateur

La stratégie pour l'entrée utilisateur est simple : lorsque le joueur appuie sur une touche du clavier, nous voulons placer cette touche au bon endroit sur le plateau. Vous allez accomplir cela en écoutant l'événement keyup. 

Lorsque le joueur appuie sur une touche, vous voulez savoir quelle était cette touche. Si la touche était une lettre unique, vous voulez la mettre au bon endroit sur le plateau. 

Vous déterminez où se trouve le bon endroit sur le plateau en vérifiant le nombre d'essais restants au joueur et combien de lettres le joueur a entrées jusqu'à présent.

Si la touche pressée était Entrée ou Retour arrière, vous vérifiez l'essai ou supprimez une lettre de l'essai actuel. Toute autre touche est ignorée.

Ajoutez ce code à script.js :

```javascript

document.addEventListener("keyup", (e) => {

    if (guessesRemaining === 0) {
        return
    }

    let pressedKey = String(e.key)
    if (pressedKey === "Backspace" && nextLetter !== 0) {
        deleteLetter()
        return
    }

    if (pressedKey === "Enter") {
        checkGuess()
        return
    }

    let found = pressedKey.match(/[a-z]/gi)
    if (!found || found.length > 1) {
        return
    } else {
        insertLetter(pressedKey)
    }
})
```

Le code utilise une expression régulière pour vérifier que la touche que nous avons pressée était une touche alphabétique représentant une seule lettre. Si le nom de la touche n'a pas de lettres (c'était un nombre), ou s'il a plusieurs lettres (Shift, Tab), nous ignorons l'événement. Sinon, nous insérons la lettre dans le plateau.

### insertLetter

Définissons la fonction `insertLetter`. Elle ressemble à ceci :

```javascript
function insertLetter (pressedKey) {
    if (nextLetter === 5) {
        return
    }
    pressedKey = pressedKey.toLowerCase()

    let row = document.getElementsByClassName("letter-row")[6 - guessesRemaining]
    let box = row.children[nextLetter]
    box.textContent = pressedKey
    box.classList.add("filled-box")
    currentGuess.push(pressedKey)
    nextLetter += 1
}
```

`insertLetter` vérifie qu'il reste encore de la place dans l'essai pour cette lettre, trouve la ligne appropriée et place la lettre dans la case.

### deleteLetter

`deleteLetter` ressemble à ceci :

```javascript
function deleteLetter () {
    let row = document.getElementsByClassName("letter-row")[6 - guessesRemaining]
    let box = row.children[nextLetter - 1]
    box.textContent = ""
    box.classList.remove("filled-box")
    currentGuess.pop()
    nextLetter -= 1
}
```

`deleteLetter` obtient la ligne correcte, trouve la dernière case et la vide, puis réinitialise le compteur nextLetter.

### checkGuess

La fonction `checkGuess` ressemble à ceci :

```javascript
function checkGuess () {
    let row = document.getElementsByClassName("letter-row")[6 - guessesRemaining]
    let guessString = ''
    let rightGuess = Array.from(rightGuessString)

    for (const val of currentGuess) {
        guessString += val
    }

    if (guessString.length != 5) {
        alert("Not enough letters!")
        return
    }

    if (!WORDS.includes(guessString)) {
        alert("Word not in list!")
        return
    }

    
    for (let i = 0; i < 5; i++) {
        let letterColor = ''
        let box = row.children[i]
        let letter = currentGuess[i]
        
        let letterPosition = rightGuess.indexOf(currentGuess[i])
        // is letter in the correct guess
        if (letterPosition === -1) {
            letterColor = 'grey'
        } else {
            // now, letter is definitely in word
            // if letter index and right guess index are the same
            // letter is in the right position 
            if (currentGuess[i] === rightGuess[i]) {
                // shade green 
                letterColor = 'green'
            } else {
                // shade box yellow
                letterColor = 'yellow'
            }

            rightGuess[letterPosition] = "#"
        }

        let delay = 250 * i
        setTimeout(()=> {
            //shade box
            box.style.backgroundColor = letterColor
            shadeKeyBoard(letter, letterColor)
        }, delay)
    }

    if (guessString === rightGuessString) {
        alert("You guessed right! Game over!")
        guessesRemaining = 0
        return
    } else {
        guessesRemaining -= 1;
        currentGuess = [];
        nextLetter = 0;

        if (guessesRemaining === 0) {
            alert("You've run out of guesses! Game over!")
            alert(`The right word was: "${rightGuessString}"`)
        }
    }
}
```

`checkGuess` est assez long, alors décomposons-le. Il fait quelques choses :

* S'assure que l'essai est de 5 lettres
* S'assure que l'essai est une liste valide
* Vérifie chaque lettre du mot et les ombre
* Informe l'utilisateur de la fin du jeu

`checkGuess` utilise un algorithme simple pour décider de la couleur à ombrer pour chaque lettre :

1. Vérifie si la lettre est dans le mot correct
2. Si la lettre n'est pas dans le mot, ombre la lettre en gris
3. Si la lettre est dans le mot, vérifie si elle est à la bonne position
4. Si la lettre est à la bonne position, ombre en vert
5. Sinon, ombre en jaune

`checkGuess` utilise une fonction `shadeKeyboard` pour colorer les touches du clavier à l'écran, mais elle n'est pas encore définie. Faisons cela ensuite.

### shadeKeyboard

```javascript
function shadeKeyBoard(letter, color) {
    for (const elem of document.getElementsByClassName("keyboard-button")) {
        if (elem.textContent === letter) {
            let oldColor = elem.style.backgroundColor
            if (oldColor === 'green') {
                return
            } 

            if (oldColor === 'yellow' && color !== 'green') {
                return
            }

            elem.style.backgroundColor = color
            break
        }
    }
}
```

`shadeKeyBoard` reçoit la lettre sur le clavier à l'écran que nous voulons ombrer et la couleur avec laquelle nous voulons l'ombrer. Voici l'algorithme :

1. Trouve la touche qui correspond à la lettre donnée
2. Si la touche est déjà verte, ne fait rien
3. Si la touche est actuellement jaune, ne permet que de devenir verte
4. Sinon, ombre la touche passée à la fonction

## Comment ajouter des notifications

Ensuite, vous allez remplacer les alertes JavaScript dans `checkGuess` par des toasts, en utilisant Toastr.

Passez en revue `checkGuess`, et remplacez toutes les alertes qui informent l'utilisateur d'une erreur par des appels à `toastr.error()`. 

L'alerte qui informe l'utilisateur d'un bon essai doit être remplacée par `toastr.success()`, et l'alerte qui indique à l'utilisateur quel était le bon essai doit être remplacée par `toastr.info()`.

Voici à quoi devrait ressembler checkGuess une fois que vous avez terminé :

```javascript
function checkGuess () {
    let row = document.getElementsByClassName("letter-row")[6 - guessesRemaining]
    let guessString = ''
    let rightGuess = Array.from(rightGuessString)

    for (const val of currentGuess) {
        guessString += val
    }

    if (guessString.length != 5) {
        toastr.error("Not enough letters!")
        return
    }

    if (!WORDS.includes(guessString)) {
        toastr.error("Word not in list!")
        return
    }

    
    for (let i = 0; i < 5; i++) {
        let letterColor = ''
        let box = row.children[i]
        let letter = currentGuess[i]
        
        let letterPosition = rightGuess.indexOf(currentGuess[i])
        // is letter in the correct guess
        if (letterPosition === -1) {
            letterColor = 'grey'
        } else {
            // now, letter is definitely in word
            // if letter index and right guess index are the same
            // letter is in the right position 
            if (currentGuess[i] === rightGuess[i]) {
                // shade green 
                letterColor = 'green'
            } else {
                // shade box yellow
                letterColor = 'yellow'
            }

            rightGuess[letterPosition] = "#"
        }

        let delay = 250 * i
        setTimeout(()=> {
            //shade box
            box.style.backgroundColor = letterColor
            shadeKeyBoard(letter, letterColor)
        }, delay)
    }

    if (guessString === rightGuessString) {
        toastr.success("You guessed right! Game over!")
        guessesRemaining = 0
        return
    } else {
        guessesRemaining -= 1;
        currentGuess = [];
        nextLetter = 0;

        if (guessesRemaining === 0) {
            toastr.error("You've run out of guesses! Game over!")
            toastr.info(`The right word was: "${rightGuessString}"`)
        }
    }
}
```

## Comment faire en sorte que le clavier à l'écran génère une entrée

Pour faire fonctionner votre clavier à l'écran, tout ce que vous avez à faire est de déclencher un événement key up chaque fois qu'une touche de votre clavier à l'écran est cliquée. Pour cela, ajoutez ce code à script.js :

```javascript
document.getElementById("keyboard-cont").addEventListener("click", (e) => {
    const target = e.target
    
    if (!target.classList.contains("keyboard-button")) {
        return
    }
    let key = target.textContent

    if (key === "Del") {
        key = "Backspace"
    } 

    document.dispatchEvent(new KeyboardEvent("keyup", {'key': key}))
})
```

Cette fonction écoute un clic sur le conteneur du clavier ou l'un de ses enfants (les boutons). Si l'élément cliqué n'était pas un bouton, nous quittons la fonction. Sinon, nous déclenchons un événement key up correspondant à la touche cliquée.

## Comment ajouter une animation

Nous avons déjà installé animate.css, alors maintenant écrivons une fonction JavaScript pour l'utiliser.

```javascript
const animateCSS = (element, animation, prefix = 'animate__') =>
  // Nous créons une Promise et la retournons
  new Promise((resolve, reject) => {
    const animationName = `${prefix}${animation}`;
    // const node = document.querySelector(element);
    const node = element
    node.style.setProperty('--animate-duration', '0.3s');
    
    node.classList.add(`${prefix}animated`, animationName);

    // Lorsque l'animation se termine, nous nettoyons les classes et résolvons la Promise
    function handleAnimationEnd(event) {
      event.stopPropagation();
      node.classList.remove(`${prefix}animated`, animationName);
      resolve('Animation ended');
    }

    node.addEventListener('animationend', handleAnimationEnd, {once: true});
});
```

Cette fonction provient de la [page d'accueil d'Animate.css](https://animate.style#javascript). Elle applique des classes à la cible de l'animation pour déclencher une animation, et lorsque l'animation se termine, elle supprime les classes qu'elle a ajoutées. 

La fonction retourne une promesse pour vous permettre d'effectuer des actions qui doivent s'exécuter uniquement après la fin de l'animation, mais vous n'aurez pas besoin de l'implémenter dans ce tutoriel.

Maintenant que nous avons une fonction pour animer n'importe quel élément, appliquons-la. Revenez à notre fonction `insertLetter`, et ajoutez la ligne suivante avant de remplacer le `textContent` de `box` :

```javascript
    animateCSS(box, "pulse")
```

Voici à quoi devrait ressembler `insertLetter` maintenant :

```javascript
function insertLetter (pressedKey) {
    if (nextLetter === 5) {
        return
    }
    pressedKey = pressedKey.toLowerCase()

    let row = document.getElementsByClassName("letter-row")[6 - guessesRemaining]
    let box = row.children[nextLetter]
    animateCSS(box, "pulse")
    box.textContent = pressedKey
    box.classList.add("filled-box")
    currentGuess.push(pressedKey)
    nextLetter += 1
}
```

Le code indique à `insertLetter` de faire pulser chaque case rapidement, juste avant de la remplir avec une lettre.

Ensuite, vous voulez animer chaque lettre d'un essai pendant que vous le vérifiez.

Revenez en arrière et modifiez `checkGuess`, comme suit :

```javascript
let delay = 250 * i
setTimeout(()=> {
    //flip box
    animateCSS(box, 'flipInX')
    //shade box
    box.style.backgroundColor = letterColor
    shadeKeyBoard(letter, letterColor)
}, delay)
```

Ce code ajoute une animation pour faire basculer chaque case verticalement, juste avant de changer la couleur.

## Conclusion

Cela conclut le tutoriel. Vous venez de construire un clone de Wordle, et j'espère que vous vous êtes amusé en cours de route. Vous pouvez trouver le code complet sur le [dépôt GitHub](https://github.com/Morgenstern2573/wordle_clone) de ce projet. 

Si vous avez aimé cet article, vous pouvez trouver plus de mes écrits [ici](https://www.freecodecamp.org/news/p/86e257bb-206c-402b-bbaa-493e4f7f644b/dev.to/morgenstern2573), ou me suivre sur [Twitter](https://twitter.com/apexPaul09).