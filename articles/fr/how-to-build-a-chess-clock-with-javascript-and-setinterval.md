---
title: Comment créer une horloge d'échecs avec JavaScript et setInterval
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-04-14T16:09:14.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-chess-clock-with-javascript-and-setinterval
coverImage: https://www.freecodecamp.org/news/content/images/2021/04/cover_image_1920x1005-1.png
tags:
- name: JavaScript
  slug: javascript
- name: mobile app development
  slug: mobile-app-development
seo_title: Comment créer une horloge d'échecs avec JavaScript et setInterval
seo_desc: "By Brandon Wallace\nChess games can sometimes go on for quite some time.\
  \ I once heard a story of a chess game between two famous chess grandmasters that\
  \ went on for over eight hours, with the crowd waiting for them to make a move.\
  \ \nAfter a while one p..."
---

Par Brandon Wallace

Les parties d'échecs peuvent parfois durer assez longtemps. J'ai déjà entendu une histoire d'une partie d'échecs entre deux grands maîtres qui a duré plus de huit heures, avec la foule attendant qu'ils fassent un mouvement.

Après un moment, un joueur a dit à l'autre : "Tu ne vas pas jouer ?" Son adversaire a répondu : "Je pensais que c'était à ton tour."

## Introduction

Les horloges d'échecs sont utilisées pour limiter une partie d'échecs à une certaine durée. Une horloge d'échecs peut ajouter beaucoup d'excitation à une partie. Beaucoup de gens utilisent ces horloges lors de tournois ou simplement pour s'amuser.

Avec une horloge d'échecs, le but est de faire échec et mat à votre adversaire avant que votre temps ne s'écoule. La première personne dont le temps s'écoule sans avoir fait échec et mat à son adversaire perd la partie.

Je vais vous montrer comment créer une horloge d'échecs basique en utilisant JavaScript et la méthode [setInterval](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous/Timeouts_and_intervals). `setInterval` vous permet d'exécuter un événement temporisé de manière répétée en spécifiant un temps en millisecondes. `setInterval` peut être assigné à un identifiant et arrêté en appelant `clearInterval` sur l'identifiant de `setInterval`.

Voici un exemple simple de comment fonctionne setInterval :

```javascript
let count = 1;

// Assigner un événement temporisé à la variable timerId.

const timerId = setInterval(() => {
    
    console.log(`Exécution de la fonction pendant ${count} secondes.`);
    
    // Incrémenter la variable count de un.
    count++;
    
    if (count === 11) {
        
        // Arrêter l'événement en appelant clearInterval sur timerId.
        clearInterval(timerId);
        console.log(`Événement temporisé effacé.`);
        
    }
    
}, 1000); // Exécuter l'événement chaque seconde (1000 millisecondes = 1 seconde).

```

![setinterval-output.png](https://i.postimg.cc/RhQQDHTk/setinterval-output.png)
_sortie_

Voici le plan de comment l'application apparaîtra sur desktop et mobile.

![chessclockblueprint2.png](https://i.postimg.cc/4NbLXWDD/chessclockblueprint2.png)

**Les exigences de programmation pour ce projet sont :**

* Nous avons besoin de deux horloges qui comptent à rebours jusqu'à zéro.
* Nous avons besoin d'un bouton de démarrage et d'un bouton de réinitialisation.
* Et nous avons besoin d'un moyen de basculer entre les horloges pendant que le temps s'écoule.

## Commençons par configurer le projet

Créez les répertoires `css`, `js` et `audio` pour garder le projet organisé.

```bash
$ mkdir css js audio

```

Créez les fichiers `index.html`, `style.css` et `script.js`.

```bash
$ touch index.html css/style.css js/script.js

```

Ajoutez ce code au fichier `index.html`.

```html
<!DOCTYPE html>
<html lang="fr">

  <head>

    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, height=device-height, initial-scale=1.0">
    <link rel="stylesheet" href="css/style.css">
    <title>horloge d'échecs</title>

  </head>

  <body>

    <main>
    
      <div class="player">
      
        <div class="player__tile player-1">
          <div class="player__digits">
            <span id="min1">10</span>:<span id="sec1">00</span>
          </div>
        </div>
        
        <div class="player__tile player-2">
          <div class="player__digits">
            <span id="min2">10</span>:<span id="sec2">00</span>
          </div>
        </div>
        
      </div>
      
      <div class="timer__buttons">
        <button class="timer__start-bttn bttn" type="button">DÉMARRER</button>
        <button class="timer__reset-bttn bttn" type="button">RÉINITIALISER</button>
      </div>

    </main>

    <footer>

      <p>Appuyez sur la barre d'espace ou cliquez sur le minuteur après un mouvement pour changer l'horloge du joueur.</p>

    </footer>

    <script src="js/script.js"></script>

  </body>

</html>

```

Voici ce que nous avons sans aucun CSS.

![setinterval-no-css.png](https://i.postimg.cc/bJ6qH67W/setinterval-no-css.png)

## Ajoutez du CSS pour styliser le projet

Ajoutez ce code CSS au fichier `style.css` pour styliser le projet en mobile first.

```css
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

html,
body {
    width: 100%;
    height: 100%;
    background-color: #14A7FF;
}

body {
    font-size: 100%;
    font-family: monospace, monospace;
}

main {
    width: 100%;
    padding: 0 10px;
    box-sizing: border-box;
}

.player {
    margin: 1em 0 5px 0;
    display: flex;
    flex-direction: column;
}

.player__tile {
    width: 100%;
    height: 300px;
    display: flex;
    margin: 0 auto;
    color: #000000;
    max-width: 400px;
    border-radius: 8px;
    align-items: center;
    justify-content: center;
    background-color: #FFFFFF;
    box-shadow: inset 3px 3px 0 #000, 
                inset -3px 3px 0 black, 
                inset -3px -3px 0 black, 
                inset 3px -3px 0 black;
}

.player-2 {
    color: #FFFFFF;
    margin-top: 5px;
    background-color: #2D2C2C;
}

.player__digits {
    font-size: 6rem;
    font-weight: bold;
}

.timer__buttons {
    margin-bottom: 1em;
}

.timer__start-bttn, 
.timer__reset-bttn {
    width: 100%;
    display: block;
    color: #020202;
    min-height: 50px;
    max-width: 400px;
    font-size: 1.5rem;
    font-weight: bold;
    border-radius: 8px;
    letter-spacing: 2px;
    margin: 0 auto 5px auto;
    border: 4px solid #000000;
}

.timer__start-bttn {
    color: #FFFFFF;
    background-color: #0071D5;
}

.timer__start-bttn:hover {
    color: #000000;
    background-color: #FFFFFF;
}

.timer__reset-bttn:hover {
    color: #FFFFFF;
    background-color: #0071D5;
}

footer p {
    text-align: center;
}

/* Media queries pour le développement mobile first. */
/* Media queries pour le mode paysage sur les appareils mobiles */
@media only screen and (orientation: landscape) and (max-width: 850px) {
    .player {
        max-width: 610px;
        flex-direction: row;
        margin: 5px auto 0 auto;
    }
    .player__tile {
        max-width: 300px;
        max-height: 250px;
        margin: 0 3px 5px 3px;
    }
    .player__digits {
        font-size: 5rem;
    }
    .timer__buttons {
        display: flex;
        margin: 0 auto;
        max-width: 610px;
    }
    .timer__start-bttn, 
    .timer__reset-bttn {
        display: block;
        max-width: 300px;
        margin: 0 3px 5px 3px;
    }
}

/* Media queries pour le mode portrait */
@media only screen and (orientation: portrait) and (min-width: 400px) {
    .player__tile {
        height: 400px;
    }
    .player__digits {
        font-size: 6rem;
    }
}

/* Les écrans plus larges que 850px utiliseront ces paramètres. */
@media only screen and (min-width: 850px) {
    .player {
        margin: 1em auto 10px auto;
        max-width: 810px;
        flex-direction: row;
    }
    .player__tile {
        height: 400px;
    }
    .player-2 {
        margin-top: 0;
    }
    .player__digits {
        font-size: 7rem;
    }
    .timer__buttons {
        display: flex;
        margin: 0 auto;
        max-width: 810px;
    }
    .timer__start-bttn, 
    .timer__reset-bttn {
        padding: .7em;
        font-size: 1.8rem;
    }
}


```

Avec le CSS ajouté, le projet commence à prendre forme.

![setinterval-with-css.png](https://i.postimg.cc/YCVngQDR/setinterval-with-css.png)

## Ajoutez du code JavaScript pour faire fonctionner l'horloge

Je vais d'abord ajouter les fonctions nécessaires pour faire fonctionner le projet.

Éditez le fichier `script.js` :

```bash
$ vim js/script.js

```

Et ajoutez les fonctions fléchées ES6 suivantes :

```javascript

// Ajoute un zéro devant les nombres inférieurs à 10.
const padZero = () => {
    // code
}

// Avertit le joueur si le temps passe sous trente secondes.
const timeWarning = () => {
    // code
}

// Crée une classe pour le minuteur.
class Timer {
    // code
}

// Basculer le minuteur du joueur après un mouvement (player1 = 1, player2 = 2).
const swapPlayer = () => {
    // code
}

// Démarrer le compte à rebours du minuteur jusqu'à zéro.
const startTimer = () => {
    // code
    let timerId = setInterval(function() {
        // code
    }, 1000)
}
```

Maintenant, nous pouvons remplir les fonctions JavaScript avec du code pour faire fonctionner l'horloge.

Nous commençons par ajouter quelques variables au projet. Si la variable `playing` est vraie, l'horloge fonctionne.

La variable `currentPlayer` stocke la valeur 1 pour le joueur un ou 2 pour le joueur deux. Nous pouvons ajouter des sons [(de freesound.org)](https://freesound.org/) pour lorsque l'horloge bascule d'un joueur à l'autre et pour alerter lorsque le temps est écoulé.

La fonction `padZero` ajoutera un zéro devant les nombres inférieurs à 10.

Éditez le fichier `script.js` comme ceci :

```bash
$ vim js/script.js
```

```javascript
let playing = false;
let currentPlayer = 1;
const panel = document.querySelector('.player');
const buttons = document.querySelectorAll('.bttn');
// Effets sonores pour le projet.
const timesUp = new Audio('audio/460133__eschwabe3__robot-affirmative.wav');
const click = new Audio('audio/561660__mattruthsound.wav');

// Ajoute un zéro devant les nombres inférieurs à 10.

const padZero = (number) => {
    if (number < 10) {
        return '0' + number;
    }
    return number;
}

```

Donnez à chaque joueur une notification visuelle que le temps est en train de s'écouler en changeant les nombres en couleur rouge.

```javascript
// Avertit le joueur si le temps passe sous une minute et trente secondes.

const timeWarning = (player, min, sec) => {
    // Change les nombres en rouge en dessous de 0 minutes et 30 secondes
    if (min < 1 && sec <= 30) {
        if (player === 1) {
            document.querySelector('.player-1 .player__digits').style.color = '#CC0000';
        } else {
            document.querySelector('.player-2 .player__digits').style.color = '#CC0000';
        }
    }
}
```

![setinterval-red-numbers.png](https://i.postimg.cc/DzwjbnTr/setinterval-red-numbers.png)

Nous allons créer une classe pour configurer le minuteur pour chaque joueur.

```javascript
// Crée une classe pour le minuteur.

class Timer {
    constructor(player, minutes) {
        this.player = player;
        this.minutes = minutes;
    }
    getMinutes(timeId) {
        return document.getElementById(timeId).textContent;
    }
}

// Crée une instance du minuteur pour chaque joueur.

let p1time = new Timer('min1', document.getElementById('min1').textContent);
let p2time = new Timer('min2', document.getElementById('min2').textContent);

```

La fonction `swapPlayer` bascule le minuteur entre le joueur 1 et le joueur 2 en utilisant un opérateur ternaire.

Si la variable `playing` est fausse, les horloges ne fonctionnent pas et la fonction se termine.

```javascript
// Basculer le minuteur du joueur après un mouvement (player1 = 1, player2 = 2).

const swapPlayer = () => {
    if (!playing) return;
    // Basculer le joueur actuel.
    currentPlayer = currentPlayer === 1 ? 2 : 1;
    // Jouer le son de clic.
    click.play();
}

```

La fonction startTimer utilise `setInterval` pour faire un compte à rebours pour chaque minuteur.

La variable `playing` est définie sur true pour faire fonctionner l'horloge.

L'instruction if vérifie quel joueur est le joueur actuel, puis commence à compter à rebours le minuteur pour ce joueur.

Si les secondes atteignent 60, un nombre est soustrait des minutes. L'élément HTML est mis à jour avec le temps chaque seconde. Une fois que les secondes et les minutes atteignent zéro, `clearInterval()` est appelé pour arrêter le minuteur.

```javascript
// Démarrer le compte à rebours du minuteur jusqu'à zéro.

const startTimer = () => {
    playing = true;
    let p1sec = 60;
    let p2sec = 60;

    let timerId = setInterval(function() {
        // Joueur 1.
        if (currentPlayer === 1) {
            if (playing) {
                buttons[0].disabled = true;
                p1time.minutes = parseInt(p1time.getMinutes('min1'), 10);
                if (p1sec === 60) {
                    p1time.minutes = p1time.minutes - 1;
                }
                p1sec = p1sec - 1;
                document.getElementById('sec1').textContent = padZero(p1sec);
                document.getElementById('min1').textContent = padZero(p1time.minutes);
                if (p1sec === 0) {
                    // Si les minutes et les secondes sont à zéro, arrêter le minuteur avec la méthode clearInterval.
                    if (p1sec === 0 && p1time.minutes === 0) {
                        // Jouer un effet sonore.
                        timesUp.play();
                        // Arrêter le minuteur.
                        clearInterval(timerId);
                        playing = false;
                    }
                    p1sec = 60;
                }
            }
        } else {
            // Joueur 2.
            if (playing) {
                p2time.minutes = parseInt(p2time.getMinutes('min2'), 10);
                if (p2sec === 60) {
                    p2time.minutes = p2time.minutes - 1;
                }
                p2sec = p2sec - 1;
                document.getElementById('sec2').textContent = padZero(p2sec);
                document.getElementById('min2').textContent = padZero(p2time.minutes);
                if (p2sec === 0) {
                    // Si les minutes et les secondes sont à zéro, arrêter le minuteur avec la méthode clearInterval.
                    if (p2sec === 0 && p2time.minutes === 0) {
                        // Jouer un effet sonore.
                        timesUp.play();
                        // Arrêter le minuteur.
                        clearInterval(timerId);
                        playing = false;
                    }
                    p2sec = 60;
                }
            }
        }
    }, 1000);
}

```

Pour faire fonctionner le minuteur, je vais ajouter un écouteur d'événement aux boutons HTML. L'écouteur d'événement écoutera également un clic ou un appui sur le div `.player` ou si quelqu'un appuie sur la barre d'espace pour basculer entre les minuteurs.

```javascript
// Écouter un clic de souris ou un appui sur l'écran pour basculer entre les minuteurs.

timerPanel.addEventListener('click', swapPlayer);

// Parcourir les boutons de démarrage et de réinitialisation.

for (let i = 0; i < buttons.length; i++) {
    buttons[i].addEventListener('click', () => {
        if (buttons[i].textContent === 'DÉMARRER') {
            // Changer la couleur du bouton en gris pour signifier un bouton désactivé.
            buttons[i].style.color = '#EEEEEE';
            buttons[i].style.backgroundColor = '#606060';
            startTimer();
        } else {
            // Réinitialiser tout en rechargeant la page.
            location.reload(true);
        }
    });
}

// Écouter l'appui sur la barre d'espace sur Windows, Linux et Mac.

document.addEventListener('keypress', event => {
    if (event.keyCode === 32 || event.which === 32) {
        swapPlayer();
    }
});
```

### Voici le résultat final :

![screenshot-project-complete.png](https://i.postimg.cc/SxPXhfDW/screenshot-project-complete.png)

Vous pouvez le voir [en direct ici](https://chessclock.cf), et vous pouvez consulter le [dépôt GitHub ici](https://github.com/brandon-wallace/chess_clock2).

## Conclusion

Voici une façon de créer une horloge d'échecs basique. Si vous êtes un passionné d'échecs, ce pourrait être un projet amusant à construire et quelque chose que vous pouvez utiliser.

Ce projet montre une bonne façon d'utiliser la méthode setInterval, comment utiliser les écouteurs d'événements et le développement mobile first. Vous pourriez ajouter d'autres fonctionnalités au projet telles qu'un moyen de régler le temps, de mettre en pause le minuteur, différents modes de minuteur, et plus encore.

Suivez-moi sur [Github](https://github.com/brandon-wallace) | [Dev.to](https://dev.to/brandonwallace)