---
title: Comment Créer Votre Propre Émulateur Chip-8
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-27T23:55:57.000Z'
originalURL: https://freecodecamp.org/news/creating-your-very-own-chip-8-emulator
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/chip8thumbnail-1.png
tags:
- name: bitwise
  slug: bitwise
- name: 'emulator '
  slug: emulator
- name: JavaScript
  slug: javascript
seo_title: Comment Créer Votre Propre Émulateur Chip-8
seo_desc: "By Eric Grandt\nBefore diving into this article, I'd like to provide a\
  \ quick introduction to what emulators are. In the simplest terms, an emulator is\
  \ software that allows for one system to behave like another system. \nA very popular\
  \ use for emulators..."
---

Par Eric Grandt

Avant de plonger dans cet article, je voudrais fournir une rapide introduction à ce que sont les émulateurs. En termes simples, un émulateur est un logiciel qui permet à un système de se comporter comme un autre système. 

Une utilisation très populaire des émulateurs de nos jours est d'émuler de vieux systèmes de jeux vidéo tels que la Nintendo 64, la Gamecube, et ainsi de suite. 

Par exemple, avec un émulateur Nintendo 64, nous pouvons exécuter des jeux Nintendo 64 directement sur un ordinateur Windows 10, sans avoir besoin de la console réelle. Dans notre cas, nous émulerons le Chip-8 sur notre système hôte grâce à l'émulateur que nous allons créer dans cet article.

L'une des manières les plus simples d'apprendre à créer vos propres émulateurs est de commencer par un émulateur Chip-8. Avec seulement 4 Ko de mémoire et 36 instructions, vous pouvez avoir votre propre émulateur Chip-8 opérationnel en moins d'une journée. Vous acquerrez également les connaissances nécessaires pour passer à des émulateurs plus grands et plus approfondis.

Cet article sera très détaillé et long dans l'espoir de clarifier tout. Avoir une compréhension de base de l'hexadécimal, du binaire et des opérations bit à bit serait bénéfique. 

Chaque section est divisée par le fichier sur lequel nous travaillons, et divisée à nouveau par la fonction sur laquelle nous travaillons pour, espérons-le, faciliter le suivi. Une fois que nous aurons terminé chaque fichier, je fournirai un lien vers le code complet, avec des commentaires.

Pour cet article entier, nous nous référerons à la [référence technique Chip-8](http://devernay.free.fr/hacks/chip8/C8TECH10.HTM#2.2) de Cowgod qui explique chaque détail du Chip-8. 

Vous pouvez utiliser n'importe quel langage que vous voulez pour créer l'émulateur, bien que cet article utilisera JavaScript. Je pense que c'est le langage le plus simple à utiliser pour la création d'émulateurs pour la première fois, car il fournit un support pour le rendu, le clavier et le son dès le départ. 

La chose la plus importante est que vous compreniez le processus d'émulation, alors utilisez le langage avec lequel vous êtes le plus à l'aise.

Si vous décidez d'utiliser JavaScript, vous devrez exécuter un serveur web local pour les tests. J'utilise Python pour cela, ce qui vous permet de démarrer un serveur web dans le dossier courant en exécutant `python3 -m http.server`.

Nous allons commencer par créer les fichiers `index.html` et `style.css`, puis passer au rendu, au clavier, au haut-parleur et enfin au CPU lui-même. Notre structure de projet ressemblera à ceci :

```
- roms
- scripts
    chip8.js
    cpu.js
    keyboard.js
    renderer.js
    speaker.js
index.html
style.css
```

## Index et Styles

Il n'y a rien de compliqué avec ces deux fichiers, ils sont très basiques. Le fichier `index.html` charge simplement les styles, crée un élément canvas et charge le fichier `chip8.js`.

```html
<!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
        <canvas></canvas>

        <script type="module" src="scripts/chip8.js"></script>
    </body>
</html>
```

Le fichier `style.css` est encore plus simple, car la seule chose stylisée est le canvas pour le rendre plus facile à repérer.

```css
canvas {
    border: 2px solid black;
}
```

Vous n'aurez plus à toucher à ces deux fichiers tout au long de cet article, mais n'hésitez pas à styliser la page comme vous le souhaitez.

## renderer.js

Notre moteur de rendu gérera tout ce qui est lié aux graphiques. Il initialisera notre élément canvas, basculera les pixels dans notre affichage et rendra ces pixels sur notre canvas.

```javascript
class Renderer {

}

export default Renderer;
```

### constructor(scale)

La première chose à faire est de construire notre moteur de rendu. Ce constructeur prendra un seul argument, `scale`, qui nous permettra de mettre à l'échelle l'affichage en agrandissant ou en réduisant les pixels.

```javascript
class Renderer {
    constructor(scale) {

    }
}

export default Renderer;
```

Nous devons initialiser quelques éléments dans ce constructeur. Tout d'abord, la taille de l'affichage, qui pour le Chip-8 est de 64x32 pixels.

```javascript
this.cols = 64;
this.rows = 32;
```

Sur un système moderne, cela est incroyablement petit et difficile à voir, c'est pourquoi nous voulons mettre à l'échelle l'affichage pour le rendre plus convivial. Restant dans notre constructeur, nous voulons définir l'échelle, récupérer le canvas, obtenir le contexte et définir la largeur et la hauteur du canvas.

```javascript
this.scale = scale;

this.canvas = document.querySelector('canvas');
this.ctx = this.canvas.getContext('2d');

this.canvas.width = this.cols * this.scale;
this.canvas.height = this.rows * this.scale;
```

Comme vous pouvez le voir, nous utilisons la variable `scale` pour augmenter la largeur et la hauteur de notre canvas. Nous utiliserons à nouveau `scale` lorsque nous commencerons à rendre les pixels à l'écran.

Le dernier élément que nous devons ajouter à notre constructeur est un tableau qui agira comme notre affichage. Puisqu'un affichage Chip-8 est de 64x32 pixels, la taille de notre tableau est simplement 64 * 32 (cols * rows), ou 2048. En gros, nous représentons chaque pixel, allumé (1) ou éteint (0), sur un affichage Chip-8 avec ce tableau.

```javascript
this.display = new Array(this.cols * this.rows);
```

Cela sera utilisé plus tard pour rendre les pixels dans notre canvas aux bons endroits.

### setPixel(x, y)

Chaque fois que notre émulateur bascule un pixel allumé ou éteint, le tableau d'affichage sera modifié pour représenter cela. 

Parlant de basculer les pixels allumés ou éteints, créons la fonction qui s'en charge. Nous appellerons la fonction `setPixel` et elle prendra une position `x` et `y` comme paramètres.

```javascript
setPixel(x, y) {

}
```

Selon la référence technique, si un pixel est positionné en dehors des limites de l'affichage, il doit s'enrouler du côté opposé, nous devons donc en tenir compte.

```javascript
if (x > this.cols) {
    x -= this.cols;
} else if (x < 0) {
    x += this.cols;
}

if (y > this.rows) {
    y -= this.rows;
} else if (y < 0) {
    y += this.rows;
}
```

Avec cela, nous pouvons calculer correctement l'emplacement du pixel sur l'affichage.

```javascript
let pixelLoc = x + (y * this.cols);
```

Si vous n'êtes pas familier avec les opérations bit à bit, la prochaine partie de code peut être déroutante. Selon la référence technique, les sprites sont XORés sur l'affichage :

```javascript
this.display[pixelLoc] ^= 1;
```

Tout ce que fait cette ligne est de basculer la valeur à `pixelLoc` (0 à 1 ou 1 à 0). Une valeur de 1 signifie qu'un pixel doit être dessiné, une valeur de 0 signifie qu'un pixel doit être effacé. De là, nous retournons simplement une valeur pour signifier si un pixel a été effacé ou non. 

Cette partie, en particulier, est importante plus tard lorsque nous arrivons au CPU et à l'écriture des différentes instructions.

```javascript
return !this.display[pixelLoc];
```

Si cela retourne vrai, un pixel a été effacé. Si cela retourne faux, rien n'a été effacé. Lorsque nous arriverons à l'instruction qui utilise cette fonction, cela aura plus de sens.

### clear()

Cette fonction efface complètement notre tableau `display` en le réinitialisant.

```javascript
clear() {
    this.display = new Array(this.cols * this.rows);
}
```

### render()

La fonction `render` est responsable du rendu des pixels dans le tableau `display` à l'écran. Pour ce projet, elle s'exécutera 60 fois par seconde.

```javascript
render() {
    // Efface l'affichage à chaque cycle de rendu. Typique pour une boucle de rendu.
    this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);

    // Parcourt notre tableau d'affichage
    for (let i = 0; i < this.cols * this.rows; i++) {
        // Récupère la position x du pixel en fonction de `i`
        let x = (i % this.cols) * this.scale;

        // Récupère la position y du pixel en fonction de `i`
        let y = Math.floor(i / this.cols) * this.scale;

        // Si la valeur à this.display[i] == 1, alors dessine un pixel.
        if (this.display[i]) {
            // Définit la couleur du pixel en noir
            this.ctx.fillStyle = '#000';

            // Place un pixel à la position (x, y) avec une largeur et une hauteur de scale
            this.ctx.fillRect(x, y, this.scale, this.scale);
        }
    }
}
```

### testRender()

À des fins de test, créons une fonction qui dessinerait quelques pixels à l'écran.

```javascript
testRender() {
    this.setPixel(0, 0);
    this.setPixel(5, 2);
}
```

[Code complet de renderer.js](https://github.com/Erigitic/chip8-emulator/blob/master/scripts/renderer.js)

## chip8.js

Maintenant que nous avons notre moteur de rendu, nous devons l'initialiser dans notre fichier `chip8.js`.

```javascript
import Renderer from './renderer.js';

const renderer = new Renderer(10);
```

De là, nous devons créer une boucle qui s'exécute à, selon la référence technique, 60hz ou 60 images par seconde. Tout comme notre fonction de rendu, cela n'est pas spécifique à Chip-8 et peut être modifié un peu pour fonctionner avec pratiquement n'importe quel autre projet.

```javascript
let loop;

let fps = 60, fpsInterval, startTime, now, then, elapsed;

function init() {
    fpsInterval = 1000 / fps;
    then = Date.now();
    startTime = then;

    // CODE DE TEST. À RETIRER QUAND LE TEST EST TERMINÉ.
    renderer.testRender();
    renderer.render();
    // FIN DU CODE DE TEST

    loop = requestAnimationFrame(step);
}

function step() {
    now = Date.now();
    elapsed = now - then;

    if (elapsed > fpsInterval) {
        // Cycle le CPU. Nous reviendrons plus tard pour le remplir.
    }

    loop = requestAnimationFrame(step);
}

init();
```

Si vous démarrez le serveur web et chargez la page dans un navigateur web, vous devriez voir deux pixels dessinés à l'écran. Si vous le souhaitez, jouez avec l'échelle et trouvez quelque chose qui fonctionne le mieux pour vous.

## keyboard.js

[Référence du Clavier](http://devernay.free.fr/hacks/chip8/C8TECH10.HTM#2.3)

La référence technique nous dit que Chip-8 utilise un pavé hexadécimal de 16 touches disposé comme suit :

|     |     |     |     |
| --- | --- | --- | --- |
| 1   | 2   | 3   | C   |
| 4   | 5   | 6   | D   |
| 7   | 8   | 9   | E   |
| A   | 0   | B   | F   |

Pour que cela fonctionne sur les systèmes modernes, nous devons mapper une touche de notre clavier à chacune de ces touches Chip-8. Nous allons faire cela dans notre constructeur, ainsi que quelques autres choses.

### constructor()

```javascript
class Keyboard {
    constructor() {
        this.KEYMAP = {
            49: 0x1, // 1
            50: 0x2, // 2
            51: 0x3, // 3
            52: 0xc, // 4
            81: 0x4, // Q
            87: 0x5, // W
            69: 0x6, // E
            82: 0xD, // R
            65: 0x7, // A
            83: 0x8, // S
            68: 0x9, // D
            70: 0xE, // F
            90: 0xA, // Z
            88: 0x0, // X
            67: 0xB, // C
            86: 0xF  // V
        }

        this.keysPressed = [];

        // Certaines instructions Chip-8 nécessitent d'attendre la prochaine pression de touche. Nous initialisons cette fonction ailleurs si nécessaire.
        this.onNextKeyPress = null;

        window.addEventListener('keydown', this.onKeyDown.bind(this), false);
        window.addEventListener('keyup', this.onKeyUp.bind(this), false);
    }
}

export default Keyboard;
```

Dans le constructeur, nous avons créé une map de touches qui mappe les touches de notre clavier aux touches du clavier Chip-8. En plus de cela, nous avons un tableau pour suivre les touches pressées, une variable nulle (dont nous parlerons plus tard), et quelques écouteurs d'événements pour gérer les entrées du clavier.

### isKeyPressed(keyCode)

Nous avons besoin d'un moyen de vérifier si une certaine touche est pressée. Cela vérifiera simplement le tableau `keysPressed` pour le `keyCode` Chip-8 spécifié.

```javascript
isKeyPressed(keyCode) {
    return this.keysPressed[keyCode];
}
```

### onKeyDown(event)

Dans notre constructeur, nous avons ajouté un écouteur d'événement `keydown` qui appellera cette fonction lorsqu'il sera déclenché.

```javascript
onKeyDown(event) {
    let key = this.KEYMAP[event.which];
    this.keysPressed[key] = true;

    // Assurez-vous que onNextKeyPress est initialisé et que la touche pressée est effectivement mappée à une touche Chip-8
    if (this.onNextKeyPress !== null && key) {
        this.onNextKeyPress(parseInt(key));
        this.onNextKeyPress = null;
    }
}
```

Tout ce que nous faisons ici est d'ajouter la touche pressée à notre tableau `keysPressed`, et d'exécuter `onNextKeyPress` si elle est initialisée et qu'une touche valide a été pressée.

Parlons de cette instruction if. L'une des instructions Chip-8 (`Fx0A`) attend une pression de touche avant de continuer l'exécution. Nous ferons en sorte que l'instruction `Fx0A` initialise la fonction `onNextKeyPress`, ce qui nous permettra de reproduire ce comportement d'attente jusqu'à la prochaine pression de touche. Une fois que nous aurons écrit cette instruction, je l'expliquerai plus en détail car cela devrait avoir plus de sens lorsque vous la verrez.

### onKeyUp(event)

Nous avons également un écouteur d'événement pour gérer les événements `keyup`, et cette fonction sera appelée lorsque cet événement sera déclenché.

```javascript
onKeyUp(event) {
    let key = this.KEYMAP[event.which];
    this.keysPressed[key] = false;
}
```

[Code complet de keyboard.js](https://github.com/Erigitic/chip8-emulator/blob/master/scripts/keyboard.js)

## chip8.js

Avec la classe clavier créée, nous pouvons retourner dans `chip8.js` et connecter le clavier.

```javascript
import Renderer from './renderer.js';
import Keyboard from './keyboard.js'; // NOUVEAU

const renderer = new Renderer(10);
const keyboard = new Keyboard(); // NOUVEAU
```

## speaker.js

Faisons maintenant quelques sons. Ce fichier est assez simple et implique la création d'un son simple et son démarrage/arrêt.

### constructor

```javascript
class Speaker {
    constructor() {
        const AudioContext = window.AudioContext || window.webkitAudioContext;

        this.audioCtx = new AudioContext();

        // Crée un gain, qui nous permettra de contrôler le volume
        this.gain = this.audioCtx.createGain();
        this.finish = this.audioCtx.destination;

        // Connecte le gain au contexte audio
        this.gain.connect(this.finish);
    }
}

export default Speaker;
```

Tout ce que nous faisons ici est de créer un `AudioContext` et de connecter un gain à celui-ci afin que nous puissions contrôler le volume. Je n'ajouterai pas de contrôle de volume dans ce tutoriel, mais si vous souhaitez l'ajouter vous-même, vous utilisez simplement ce qui suit :

```javascript
// Couper le son
this.gain.setValueAtTime(0, this.audioCtx.currentTime);
```

```javascript
// Rétablir le son
this.gain.setValueAtTime(1, this.audioCtx.currentTime);
```

### play(frequency)

Cette fonction fait exactement ce que son nom suggère : elle joue un son à la fréquence souhaitée.

```javascript
play(frequency) {
    if (this.audioCtx && !this.oscillator) {
        this.oscillator = this.audioCtx.createOscillator();

        // Définit la fréquence
        this.oscillator.frequency.setValueAtTime(frequency || 440, this.audioCtx.currentTime);

        // Onde carrée
        this.oscillator.type = 'square';

        // Connecte le gain et démarre le son
        this.oscillator.connect(this.gain);
        this.oscillator.start();
    }
}
```

Nous créons un oscillateur qui sera ce qui jouera notre son. Nous définissons sa fréquence, le type, le connectons au gain, puis enfin jouons le son. Rien de trop compliqué ici.

### stop()

Nous devons éventuellement arrêter le son pour qu'il ne joue pas constamment.

```javascript
stop() {
    if (this.oscillator) {
        this.oscillator.stop();
        this.oscillator.disconnect();
        this.oscillator = null;
    }
}
```

Tout ce que cela fait est d'arrêter le son, de le déconnecter et de le définir à null afin qu'il puisse être réinitialisé dans `play()`.

[Code complet de speaker.js](https://github.com/Erigitic/chip8-emulator/blob/master/scripts/speaker.js)

## chip8.js

Nous pouvons maintenant connecter le haut-parleur à notre fichier principal `chip8.js`.

```javascript
import Renderer from './renderer.js';
import Keyboard from './keyboard.js';
import Speaker from './speaker.js'; // NOUVEAU

const renderer = new Renderer(10);
const keyboard = new Keyboard();
const speaker = new Speaker(); // NOUVEAU
```

## cpu.js

Maintenant, nous entrons dans l'émulateur Chip-8 proprement dit. C'est là que les choses deviennent un peu compliquées, mais je vais faire de mon mieux pour expliquer tout de manière à ce que cela ait du sens.

### constructor(renderer, keyboard, speaker)

Nous devons initialiser quelques variables spécifiques à Chip-8 dans notre constructeur, ainsi que quelques autres variables. Nous allons nous référer à la [section 2](http://devernay.free.fr/hacks/chip8/C8TECH10.HTM#2.0) de la référence technique pour déterminer les spécifications de notre émulateur Chip-8.

Voici les spécifications pour Chip-8 :

- 4 Ko (4096 octets) de mémoire
- 16 registres de 8 bits
- Un registre de 16 bits (`this.i`) pour stocker les adresses mémoire
- Deux temporisateurs. Un pour le délai, et un pour le son.
- Un compteur de programme qui stocke l'adresse actuellement exécutée
- Un tableau pour représenter la pile

Nous avons également une variable qui stocke si l'émulateur est en pause ou non, et la vitesse d'exécution de l'émulateur.

```javascript
class CPU {
    constructor(renderer, keyboard, speaker) {
        this.renderer = renderer;
        this.keyboard = keyboard;
        this.speaker = speaker;

        // 4 Ko (4096 octets) de mémoire
        this.memory = new Uint8Array(4096);

        // 16 registres de 8 bits
        this.v = new Uint8Array(16);

        // Stocke les adresses mémoire. Définissez ceci à 0 puisque nous ne stockons rien à l'initialisation.
        this.i = 0;

        // Temporisateurs
        this.delayTimer = 0;
        this.soundTimer = 0;

        // Compteur de programme. Stocke l'adresse actuellement exécutée.
        this.pc = 0x200;

        // Ne pas initialiser ceci avec une taille afin d'éviter des résultats vides.
        this.stack = new Array();

        // Certaines instructions nécessitent une pause, comme Fx0A.
        this.paused = false;

        this.speed = 10;
    }
}

export default CPU;
```

### loadSpritesIntoMemory()

Pour cette fonction, nous allons nous référer à la [section 2.4](http://devernay.free.fr/hacks/chip8/C8TECH10.HTM#2.4) de la référence technique.

Chip-8 utilise 16 sprites de 5 octets. Ces sprites sont simplement les chiffres hexadécimaux de 0 à F. Vous pouvez voir tous les sprites, avec leurs valeurs binaires et hexadécimales, dans la section 2.4. 

Dans notre code, nous stockons simplement les valeurs hexadécimales des sprites que la référence technique fournit dans un tableau. Si vous ne voulez pas les taper tous à la main, n'hésitez pas à copier et coller le tableau dans votre projet.

La référence indique que ces sprites sont stockés dans la section d'interprétation de la mémoire (0x000 à 0x1FFF). Allons-y et regardons le code de cette fonction pour voir comment cela est fait.

```javascript
loadSpritesIntoMemory() {
    // Tableau des valeurs hexadécimales pour chaque sprite. Chaque sprite fait 5 octets.
    // La référence technique nous fournit chacune de ces valeurs.
    const sprites = [
        0xF0, 0x90, 0x90, 0x90, 0xF0, // 0
        0x20, 0x60, 0x20, 0x20, 0x70, // 1
        0xF0, 0x10, 0xF0, 0x80, 0xF0, // 2
        0xF0, 0x10, 0xF0, 0x10, 0xF0, // 3
        0x90, 0x90, 0xF0, 0x10, 0x10, // 4
        0xF0, 0x80, 0xF0, 0x10, 0xF0, // 5
        0xF0, 0x80, 0xF0, 0x90, 0xF0, // 6
        0xF0, 0x10, 0x20, 0x40, 0x40, // 7
        0xF0, 0x90, 0xF0, 0x90, 0xF0, // 8
        0xF0, 0x90, 0xF0, 0x10, 0xF0, // 9
        0xF0, 0x90, 0xF0, 0x90, 0x90, // A
        0xE0, 0x90, 0xE0, 0x90, 0xE0, // B
        0xF0, 0x80, 0x80, 0x80, 0xF0, // C
        0xE0, 0x90, 0x90, 0x90, 0xE0, // D
        0xF0, 0x80, 0xF0, 0x80, 0xF0, // E
        0xF0, 0x80, 0xF0, 0x80, 0x80  // F
    ];

    // Selon la référence technique, les sprites sont stockés dans la section d'interprétation de la mémoire à partir de l'hexadécimal 0x000
    for (let i = 0; i < sprites.length; i++) {
        this.memory[i] = sprites[i];
    }
}
```

Tout ce que nous avons fait est de parcourir chaque octet dans le tableau `sprites` et de le stocker en mémoire à partir de l'hexadécimal `0x000`.

### loadProgramIntoMemory(program)

Pour exécuter des ROMs, nous devons les charger en mémoire. Cela est beaucoup plus facile que cela ne semble. Tout ce que nous devons faire est de parcourir le contenu de la ROM/programme et de le stocker en mémoire. La référence technique nous dit spécifiquement [ici](http://devernay.free.fr/hacks/chip8/C8TECH10.HTM#2.1) que "la plupart des programmes Chip-8 commencent à l'emplacement 0x200". Donc lorsque nous chargeons la ROM en mémoire, nous commençons à `0x200` et incrémentons à partir de là.

```javascript
loadProgramIntoMemory(program) {
    for (let loc = 0; loc < program.length; loc++) {
        this.memory[0x200 + loc] = program[loc];
    }
}
```

### loadRom(romName)

Maintenant, nous avons un moyen de charger la ROM en mémoire, mais nous devons d'abord récupérer la ROM du système de fichiers avant qu'elle ne puisse être chargée en mémoire. Pour que cela fonctionne, vous devez avoir une ROM. J'en ai inclus quelques-unes dans le [dépôt GitHub](https://github.com/Erigitic/chip8-emulator/tree/master/roms) pour que vous puissiez les télécharger et les mettre dans le dossier `roms` de votre projet.

JavaScript fournit un moyen de faire une requête HTTP et de récupérer un fichier. J'ai ajouté des commentaires au code ci-dessous pour expliquer ce qui se passe :

```javascript
loadRom(romName) {
    var request = new XMLHttpRequest;
    var self = this;

    // Gère la réponse reçue de l'envoi (request.send()) de notre requête
    request.onload = function() {
        // Si la réponse de la requête contient du contenu
        if (request.response) {
            // Stocke le contenu de la réponse dans un tableau de 8 bits
            let program = new Uint8Array(request.response);

            // Charge la ROM/programme en mémoire
            self.loadProgramIntoMemory(program);
        }
    }

    // Initialise une requête GET pour récupérer la ROM de notre dossier roms
    request.open('GET', 'roms/' + romName);
    request.responseType = 'arraybuffer';

    // Envoie la requête GET
    request.send();
}
```

À partir de là, nous pouvons commencer le cycle du CPU qui gérera l'exécution des instructions, ainsi que quelques autres choses.

### cycle()

Je pense qu'il sera plus facile de tout comprendre si vous pouvez voir ce qui se passe à chaque fois que le CPU cycle. C'est la fonction que nous allons appeler dans notre fonction `step` dans `chip8.js`, qui, si vous vous souvenez, est exécutée environ 60 fois par seconde. Nous allons prendre cette fonction morceau par morceau.

À ce stade, les fonctions appelées dans `cycle` n'ont pas encore été créées. Nous les créerons bientôt.

Le premier morceau de code dans notre fonction `cycle` est une boucle for qui gère l'exécution des instructions. C'est là que notre variable `speed` entre en jeu. Plus cette valeur est élevée, plus d'instructions seront exécutées à chaque cycle.

```javascript
cycle() {
    for (let i = 0; i < this.speed; i++) {

    }
}
```

Nous devons également garder à l'esprit que les instructions ne doivent être exécutées que lorsque l'émulateur est en cours d'exécution.

```javascript
cycle() {
    for (let i = 0; i < this.speed; i++) {
        if (!this.paused) {

        }
    }
}
```

Si vous regardez la [section 3.1](http://devernay.free.fr/hacks/chip8/C8TECH10.HTM#3.1), vous pouvez voir toutes les différentes instructions et leurs opcodes. Ils ressemblent à quelque chose comme `00E0` ou `9xy0` pour donner quelques exemples. Donc notre travail est de récupérer cet opcode de la mémoire et de le passer à une autre fonction qui gérera l'exécution de cette instruction. Regardons d'abord le code, puis je l'expliquerai :

```javascript
cycle() {
    for (let i = 0; i < this.speed; i++) {
        if (!this.paused) {
            let opcode = (this.memory[this.pc] << 8 | this.memory[this.pc + 1]);
            this.executeInstruction(opcode);
        }
    }
}
```

Regardons cette ligne en particulier : `let opcode = (this.memory[this.pc] << 8 | this.memory[this.pc + 1]);`. Pour ceux qui ne sont pas très familiers avec les opérations bit à bit, cela peut être très intimidant.

Tout d'abord, chaque instruction est de 16 bits (2 octets) de long ([3.0](http://devernay.free.fr/hacks/chip8/C8TECH10.HTM#3.0)), mais notre mémoire est composée de morceaux de 8 bits (1 octet). Cela signifie que nous devons combiner deux morceaux de mémoire afin d'obtenir l'opcode complet. C'est pourquoi nous avons `this.pc` et `this.pc + 1` dans la ligne de code ci-dessus. Nous récupérons simplement les deux moitiés de l'opcode. 

Mais vous ne pouvez pas simplement combiner deux valeurs de 1 octet pour obtenir une valeur de 2 octets. Pour le faire correctement, nous devons décaler le premier morceau de mémoire, `this.memory[this.pc]`, de 8 bits vers la gauche pour le rendre de 2 octets de long. En termes les plus basiques, cela ajoutera deux zéros, ou plus précisément la valeur hexadécimale `0x00` sur le côté droit de notre valeur de 1 octet, la rendant de 2 octets. 

Par exemple, décaler l'hexadécimal `0x11` de 8 bits vers la gauche nous donnera l'hexadécimal `0x1100`. À partir de là, nous faisons un OU bit à bit (`|`) avec le deuxième morceau de mémoire, `this.memory[this.pc + 1])`.

Voici un exemple étape par étape qui vous aidera à mieux comprendre ce que tout cela signifie.

Supposons quelques valeurs, chacune de 1 octet de taille :

`this.memory[this.pc] = PC = 0x10`
`this.memory[this.pc + 1] = PC + 1 = 0xF0`

Décalez `PC` de 8 bits (1 octet) vers la gauche pour le rendre de 2 octets :

`PC = 0x1000`

OU bit à bit `PC` et `PC + 1` :

`PC | PC + 1 = 0x10F0`

ou

`0x1000 | 0xF0 = 0x10F0`

Enfin, nous voulons mettre à jour nos temporisateurs lorsque notre émulateur est en cours d'exécution (non en pause), jouer des sons et rendre les sprites à l'écran :

```javascript
cycle() {
    for (let i = 0; i < this.speed; i++) {
        if (!this.paused) {
            let opcode = (this.memory[this.pc] << 8 | this.memory[this.pc + 1]);
            this.executeInstruction(opcode);
        }
    }

    if (!this.paused) {
        this.updateTimers();
    }

    this.playSound();
    this.renderer.render();
}
```

Cette fonction est en quelque sorte le cerveau de notre émulateur. Elle gère l'exécution des instructions, met à jour les temporisateurs, joue du son et rend le contenu à l'écran. 

Nous n'avons encore aucune de ces fonctions créées, mais voir comment le CPU cycle à travers tout cela devrait, espérons-le, rendre ces fonctions beaucoup plus compréhensibles lorsque nous les créerons.

### updateTimers()

Passons à la [section 2.5](http://devernay.free.fr/hacks/chip8/C8TECH10.HTM#2.5) et mettons en place la logique pour les temporisateurs et le son.

Chaque temporisateur, délai et son, décrémente de 1 à un rythme de 60Hz. En d'autres termes, toutes les 60 images, nos temporisateurs décrémenteront de 1.

```javascript
updateTimers() {
    if (this.delayTimer > 0) {
        this.delayTimer -= 1;
    }

    if (this.soundTimer > 0) {
        this.soundTimer -= 1;
    }
}
```

Le temporisateur de délai est utilisé pour suivre quand certains événements se produisent. Ce temporisateur n'est utilisé que dans deux instructions : une pour définir sa valeur, et une autre pour lire sa valeur et brancher à une autre instruction si une certaine valeur est présente.

Le temporisateur de son est ce qui contrôle la durée du son. Tant que la valeur de `this.soundTimer` est supérieure à zéro, le son continuera à jouer. Lorsque le temporisateur de son atteint zéro, le son s'arrête. Cela nous amène à notre prochaine fonction où nous ferons exactement cela.

### playSound()

Pour réitérer, tant que le temporisateur de son est supérieur à zéro, nous voulons jouer un son. Nous utiliserons la fonction `play` de notre classe `Speaker` que nous avons créée précédemment pour jouer un son avec une fréquence de 440.

```javascript
playSound() {
    if (this.soundTimer > 0) {
        this.speaker.play(440);
    } else {
        this.speaker.stop();
    }
}
```

### executeInstruction(opcode)

Pour cette fonction entière, nous allons nous référer aux [sections 3.0 et 3.1](http://devernay.free.fr/hacks/chip8/C8TECH10.HTM#3.0) de la référence technique.

C'est la dernière fonction dont nous avons besoin pour ce fichier, et celle-ci est longue. Nous devons écrire la logique pour les 36 instructions Chip-8. Heureusement, la plupart de ces instructions ne nécessitent que quelques lignes de code.

La première information à connaître est que toutes les instructions font 2 octets de long. Donc chaque fois que nous exécutons une instruction, ou exécutons cette fonction, nous devons incrémenter le compteur de programme (`this.pc`) de 2 afin que le CPU sache où se trouve la prochaine instruction.

```javascript
executeInstruction(opcode) {
    // Incrémente le compteur de programme pour le préparer à l'instruction suivante.
    // Chaque instruction fait 2 octets de long, donc incrémentez-le de 2.
    this.pc += 2;
}
```

Regardons maintenant cette partie de la section 3.0 :

```
Dans ces listes, les variables suivantes sont utilisées :

nnn ou addr - Une valeur de 12 bits, les 12 bits les plus bas de l'instruction
n ou nibble - Une valeur de 4 bits, les 4 bits les plus bas de l'instruction
x - Une valeur de 4 bits, les 4 bits les plus bas de l'octet haut de l'instruction
y - Une valeur de 4 bits, les 4 bits les plus hauts de l'octet bas de l'instruction
kk ou byte - Une valeur de 8 bits, les 8 bits les plus bas de l'instruction
```

Pour éviter de répéter du code, nous devrions créer des variables pour les valeurs `x` et `y` car ce sont celles utilisées par presque toutes les instructions. Les autres variables listées ci-dessus ne sont pas utilisées assez pour justifier le calcul de leurs valeurs à chaque fois.

Ces deux valeurs font chacune 4 bits (aka. un demi-octet ou un nibble) de taille. La valeur `x` est située dans les 4 bits les plus bas de l'octet haut et `y` est située dans les 4 bits les plus hauts de l'octet bas.

Par exemple, si nous avons une instruction `0x5460`, l'octet haut serait `0x54` et l'octet bas serait `0x60`. Les 4 bits les plus bas, ou nibble, de l'octet haut seraient `0x4` et les 4 bits les plus hauts de l'octet bas seraient `0x6`. Par conséquent, dans cet exemple, `x = 0x4` et `y = 0x6`.

Sachant tout cela, écrivons le code qui récupérera les valeurs `x` et `y`.

```javascript
executeInstruction(opcode) {
    this.pc += 2;

    // Nous avons seulement besoin du 2ème nibble, donc récupérez la valeur du 2ème nibble
    // et décalez-la de 8 bits vers la droite pour vous débarrasser de tout sauf ce 2ème nibble.
    let x = (opcode & 0x0F00) >> 8;

    // Nous avons seulement besoin du 3ème nibble, donc récupérez la valeur du 3ème nibble
    // et décalez-la de 4 bits vers la droite pour vous débarrasser de tout sauf ce 3ème nibble.
    let y = (opcode & 0x00F0) >> 4;
}
```

Pour expliquer cela, supposons une fois de plus que nous avons une instruction `0x5460`. Si nous `&` (ET bit à bit) cette instruction avec la valeur hexadécimale `0x0F00`, nous obtiendrons `0x0400`. Décalez cela de 8 bits vers la droite et nous obtiendrons `0x04` ou `0x4`. Même chose pour `y`. Nous `&` l'instruction avec la valeur hexadécimale `0x00F0` et obtenons `0x0060`. Décalez cela de 4 bits vers la droite et nous obtiendrons `0x006` ou `0x6`.

Maintenant, la partie amusante, écrire la logique pour les 36 instructions. Pour chaque instruction, avant d'écrire le code, je vous recommande vivement de lire ce que fait cette instruction dans la référence technique, car vous la comprendrez beaucoup mieux.

Je vais vous fournir l'instruction switch vide que vous allez utiliser, car elle est assez longue.

```javascript
switch (opcode & 0xF000) {
    case 0x0000:
        switch (opcode) {
            case 0x00E0:
                break;
            case 0x00EE:
                break;
        }

        break;
    case 0x1000:
        break;
    case 0x2000:
        break;
    case 0x3000:
        break;
    case 0x4000:
        break;
    case 0x5000:
        break;
    case 0x6000:
        break;
    case 0x7000:
        break;
    case 0x8000:
        switch (opcode & 0xF) {
            case 0x0:
                break;
            case 0x1:
                break;
            case 0x2:
                break;
            case 0x3:
                break;
            case 0x4:
                break;
            case 0x5:
                break;
            case 0x6:
                break;
            case 0x7:
                break;
            case 0xE:
                break;
        }

        break;
    case 0x9000:
        break;
    case 0xA000:
        break;
    case 0xB000:
        break;
    case 0xC000:
        break;
    case 0xD000:
        break;
    case 0xE000:
        switch (opcode & 0xFF) {
            case 0x9E:
                break;
            case 0xA1:
                break;
        }

        break;
    case 0xF000:
        switch (opcode & 0xFF) {
            case 0x07:
                break;
            case 0x0A:
                break;
            case 0x15:
                break;
            case 0x18:
                break;
            case 0x1E:
                break;
            case 0x29:
                break;
            case 0x33:
                break;
            case 0x55:
                break;
            case 0x65:
                break;
        }

        break;

    default:
        throw new Error('Opcode inconnu ' + opcode);
}
```

Comme vous pouvez le voir à partir de `switch (opcode & 0xF000)`, nous récupérons les 4 bits supérieurs de l'octet le plus significatif de l'opcode. Si vous regardez les différentes instructions dans la référence technique, vous remarquerez que nous pouvons réduire les différents opcodes par ce tout premier nibble.

#### 0nnn - SYS addr

Cet opcode peut être ignoré.

#### 00E0 - CLS

Efface l'affichage.

```javascript
case 0x00E0:
    this.renderer.clear();
    break;
```

#### 00EE - RET

Dépile le dernier élément du tableau `stack` et le stocke dans `this.pc`. Cela nous ramènera d'une sous-routine.

```javascript
case 0x00EE:
    this.pc = this.stack.pop();
    break;
```

La référence technique indique que cette instruction "soustrait également 1 du pointeur de pile". Le pointeur de pile est utilisé pour pointer vers le niveau le plus élevé de la pile. Mais grâce à notre tableau `stack`, nous n'avons pas à nous soucier de l'endroit où se trouve le sommet de la pile puisque c'est géré par le tableau. Donc pour le reste des instructions, si cela dit quelque chose sur le pointeur de pile, vous pouvez l'ignorer en toute sécurité.

#### 1nnn - JP addr

Définissez le compteur de programme sur la valeur stockée dans `nnn`.

```javascript
case 0x1000:
    this.pc = (opcode & 0xFFF);
    break;
```

`0xFFF` récupère la valeur de `nnn`. Donc `0x1426 & 0xFFF` nous donnera `0x426` et nous stockons cela dans `this.pc`.

#### 2nnn - CALL addr

Pour cela, la référence technique dit que nous devons incrémenter le pointeur de pile pour qu'il pointe vers la valeur actuelle de `this.pc`. Encore une fois, nous n'utilisons pas de pointeur de pile dans notre projet car notre tableau `stack` gère cela pour nous. Donc au lieu d'incrémenter cela, nous poussons simplement `this.pc` sur la pile, ce qui nous donnera le même résultat. Et tout comme avec l'opcode `1nnn`, nous récupérons la valeur de `nnn` et la stockons dans `this.pc`.

```javascript
case 0x2000:
    this.stack.push(this.pc);
    this.pc = (opcode & 0xFFF);
    break;
```

#### 3xkk - SE Vx, byte

C'est là que notre valeur `x` que nous avons calculée ci-dessus entre en jeu.

Cette instruction compare la valeur stockée dans le registre `x` (`Vx`) à la valeur de `kk`. Notez que `V` signifie un registre, et la valeur qui le suit, dans ce cas `x`, est le numéro du registre. Si elles sont égales, nous incrémentons le compteur de programme de 2, sautant effectivement l'instruction suivante.

```javascript
case 0x3000:
    if (this.v[x] === (opcode & 0xFF)) {
        this.pc += 2;
    }
    break;
```

La partie `opcode & 0xFF` de l'instruction if récupère simplement le dernier octet de l'opcode. Il s'agit de la partie `kk` de l'opcode.

#### 4xkk - SNE Vx, byte

Cette instruction est très similaire à `3xkk`, mais saute l'instruction suivante si `Vx` et `kk` ne sont PAS égaux.

```javascript
case 0x4000:
    if (this.v[x] !== (opcode & 0xFF)) {
        this.pc += 2;
    }
    break;
```

#### 5xy0 - SE Vx, Vy

Maintenant, nous utilisons à la fois `x` et `y`. Cette instruction, comme les deux précédentes, sautera l'instruction suivante si une condition est remplie. Dans le cas de cette instruction, si `Vx` est égal à `Vy`, nous sautons l'instruction suivante.

```javascript
case 0x5000:
    if (this.v[x] === this.v[y]) {
        this.pc += 2;
    }
    break;
```

#### 6xkk - LD Vx, byte

Cette instruction définira la valeur de `Vx` à la valeur de `kk`.

```javascript
case 0x6000:
    this.v[x] = (opcode & 0xFF);
    break;
```

#### 7xkk - ADD Vx, byte

Cette instruction ajoute `kk` à `Vx`.

```javascript
case 0x7000:
    this.v[x] += (opcode & 0xFF);
    break;
```

#### 8xy0 - LD Vx, Vy

Avant de discuter de cette instruction, j'aimerais expliquer ce qui se passe avec `switch (opcode & 0xF)`. Pourquoi le switch dans un switch ? 

La raison derrière cela est que nous avons une poignée d'instructions différentes qui tombent sous `case 0x8000:`. Si vous regardez ces instructions dans la référence technique, vous remarquerez que le dernier nibble de chacune de ces instructions se termine par une valeur `0-7` ou `E`. 

Nous avons ce switch pour récupérer ce dernier nibble, puis créer un cas pour chacun afin de le gérer correctement. Nous faisons cela quelques fois de plus tout au long de l'instruction switch principale.

Avec cela expliqué, passons à l'instruction. Rien de compliqué avec celle-ci, il suffit de définir la valeur de `Vx` égale à la valeur de `Vy`.

```javascript
case 0x0:
    this.v[x] = this.v[y];
    break;
```

#### 8xy1 - OR Vx, Vy

Définissez `Vx` à la valeur de `Vx OR Vy`.

```javascript
case 0x1:
    this.v[x] |= this.v[y];
    break;
```

#### 8xy2 - AND Vx, Vy

Définissez `Vx` égal à la valeur de `Vx AND Vy`.

```javascript
case 0x2:
    this.v[x] &= this.v[y];
    break;
```

#### 8xy3 - XOR Vx, Vy

Définissez `Vx` égal à la valeur de `Vx XOR Vy`.

```javascript
case 0x3:
    this.v[x] ^= this.v[y];
    break;
```

#### 8xy4 - ADD Vx, Vy

Cette instruction définit `Vx` à `Vx + Vy`. Cela semble facile, mais il y a un peu plus à cela. Si nous lisons la description de cette instruction fournie dans la référence technique, elle dit ce qui suit :

> Si le résultat est supérieur à 8 bits (c'est-à-dire > 255,) VF est défini à 1, sinon 0. Seuls les 8 bits les plus bas du résultat sont conservés et stockés dans Vx.

```javascript
case 0x4:
    let sum = (this.v[x] += this.v[y]);

    this.v[0xF] = 0;

    if (sum > 0xFF) {
        this.v[0xF] = 1;
    }

    this.v[x] = sum;
    break;
```

En prenant cela ligne par ligne, nous additionnons d'abord `this.v[y]` à `this.v[x]` et stockons cette valeur dans une variable `sum`. À partir de là, nous définissons `this.v[0xF]`, ou `VF`, à 0. Nous faisons cela pour éviter d'avoir à utiliser une instruction if-else à la ligne suivante. Si la somme est supérieure à 255, ou hex `0xFF`, nous définissons `VF` à 1. Enfin, nous définissons `this.v[x]`, ou `Vx`, à la somme.

Vous vous demandez peut-être comment nous faisons pour nous assurer que "seuls les 8 bits les plus bas du résultat sont conservés et stockés dans Vx". Grâce à `this.v` étant un `Uint8Array`, toute valeur supérieure à 8 bits a automatiquement les 8 bits les plus bas, les plus à droite, pris et stockés dans le tableau. Par conséquent, nous n'avons pas besoin de faire quoi que ce soit de spécial avec cela.

Permettez-moi de vous fournir un exemple pour que cela ait plus de sens. Supposons que nous essayons de mettre le décimal 257 dans le tableau `this.v`. En binaire, cette valeur est `100000001`, une valeur de 9 bits. Lorsque nous tentons de stocker cette valeur de 9 bits dans le tableau, il ne prendra que les 8 bits les plus bas. Cela signifie que le binaire `00000001`, qui est 1 en décimal, serait stocké dans `this.v`.

#### 8xy5 - SUB Vx, Vy

Cette instruction soustrait `Vy` de `Vx`. Tout comme le débordement est géré dans l'instruction précédente, nous devons gérer le sous-débordement pour celle-ci.

```javascript
case 0x5:
    this.v[0xF] = 0;

    if (this.v[x] > this.v[y]) {
        this.v[0xF] = 1;
    }

    this.v[x] -= this.v[y];
    break;
```

Encore une fois, puisque nous utilisons un `Uint8Array`, nous n'avons pas à faire quoi que ce soit pour gérer le sous-débordement car cela est pris en charge pour nous. Donc -1 deviendra 255, -2 devient 254, et ainsi de suite.

#### 8xy6 - SHR Vx {, Vy}

```javascript
case 0x6:
    this.v[0xF] = (this.v[x] & 0x1);

    this.v[x] >>= 1;
    break;
```

Cette ligne `this.v[0xF] = (this.v[x] & 0x1);` va déterminer le bit le moins significatif et définir `VF` en conséquence.

Cela est beaucoup plus facile à comprendre si vous regardez sa représentation binaire. Si `Vx`, en binaire, est `1001`, `VF` sera défini à 1 puisque le bit le moins significatif est 1. Si `Vx` est `1000`, `VF` sera défini à 0.

#### 8xy7 - SUBN Vx, Vy

```javascript
case 0x7:
    this.v[0xF] = 0;

    if (this.v[y] > this.v[x]) {
        this.v[0xF] = 1;
    }

    this.v[x] = this.v[y] - this.v[x];
    break;
```

Cette instruction soustrait `Vx` de `Vy` et stocke le résultat dans `Vx`. Si `Vy` est plus grand que `Vx`, nous devons stocker 1 dans `VF`, sinon nous stockons 0.

#### 8xyE - SHL Vx {, Vy}

Cette instruction non seulement décale `Vx` de 1 vers la gauche, mais définit également `VF` à 0 ou 1 selon qu'une condition est remplie ou non.

```javascript
case 0xE:
    this.v[0xF] = (this.v[x] & 0x80);
    this.v[x] <<= 1;
    break;
```

La première ligne de code, `this.v[0xF] = (this.v[x] & 0x80);`, récupère le bit le plus significatif de `Vx` et le stocke dans `VF`. Pour expliquer cela, nous avons un registre de 8 bits, `Vx`, et nous voulons obtenir le bit le plus significatif, ou le plus à gauche. Pour ce faire, nous devons faire un ET bit à bit entre `Vx` et le binaire `10000000`, ou `0x80` en hexadécimal. Cela permettra de définir `VF` à la valeur appropriée.

Après cela, nous multiplions simplement `Vx` par 2 en le décalant de 1 vers la gauche.

#### 9xy0 - SNE Vx, Vy

Cette instruction incrémente simplement le compteur de programme de 2 si `Vx` et `Vy` ne sont pas égaux.

```javascript
case 0x9000:
    if (this.v[x] !== this.v[y]) {
        this.pc += 2;
    }
    break;
```

#### Annn - LD I, addr

Définissez la valeur du registre `i` à `nnn`. Si l'opcode est `0xA740`, alors `(opcode & 0xFFF)` retournera `0x740`.

```javascript
case 0xA000:
    this.i = (opcode & 0xFFF);
    break;
```

#### Bnnn - JP V0, addr

Définissez le compteur de programme (`this.pc`) à `nnn` plus la valeur du registre 0 (`V0`).

```javascript
case 0xB000:
    this.pc = (opcode & 0xFFF) + this.v[0];
    break;
```

#### Cxkk - RND Vx, byte

```javascript
case 0xC000:
    let rand = Math.floor(Math.random() * 0xFF);

    this.v[x] = rand & (opcode & 0xFF);
    break;
```

Génère un nombre aléatoire dans la plage 0-255 puis fait un ET bit à bit avec l'octet le plus bas de l'opcode. Par exemple, si l'opcode est `0xB849`, alors `(opcode & 0xFF)` retournerait `0x49`.

#### Dxyn - DRW Vx, Vy, nibble

C'est une grosse instruction ! Cette instruction gère le dessin et l'effacement des pixels à l'écran. Je vais vous fournir tout le code et l'expliquer ligne par ligne.

```javascript
case 0xD000:
    let width = 8;
    let height = (opcode & 0xF);

    this.v[0xF] = 0;

    for (let row = 0; row < height; row++) {
        let sprite = this.memory[this.i + row];

        for (let col = 0; col < width; col++) {
            // Si le bit (sprite) n'est pas 0, dessine/efface le pixel
            if ((sprite & 0x80) > 0) {
                // Si setPixel retourne 1, ce qui signifie qu'un pixel a été effacé, définis VF à 1
                if (this.renderer.setPixel(this.v[x] + col, this.v[y] + row)) {
                    this.v[0xF] = 1;
                }
            }

            // Décale le sprite de 1 vers la gauche. Cela déplacera le prochain col/bit du sprite à la première position.
            // Ex. 10010000 << 1 deviendra 0010000
            sprite <<= 1;
        }
    }

    break;
```

Nous avons une variable `width` définie à 8 car chaque sprite fait 8 pixels de large, donc il est sûr de coder en dur cette valeur. Ensuite, nous définissons `height` à la valeur du dernier nibble (`n`) de l'opcode. Si notre opcode est `0xD235`, `height` sera défini à 5. À partir de là, nous définissons `VF` à 0, qui, si nécessaire, sera défini à 1 plus tard si des pixels sont effacés.

Maintenant, passons aux boucles for. Rappelez-vous qu'un sprite ressemble à ceci :

```
11110000
10010000
10010000
10010000
11110000
```

Notre code parcourt ligne par ligne (première boucle `for`), puis il parcourt bit par bit ou colonne par colonne (deuxième boucle `for`) ce sprite.

Ce morceau de code, `let sprite = this.memory[this.i + row];`, récupère 8 bits de mémoire, ou une seule ligne d'un sprite, qui est stockée à `this.i + row`. La référence technique indique que nous commençons à l'adresse stockée dans `I`, ou `this.i` dans notre cas, lorsque nous lisons les sprites de la mémoire.

Dans notre deuxième boucle `for`, nous avons une instruction `if` qui récupère le bit le plus à gauche et vérifie s'il est supérieur à 0. 

Une valeur de 0 indique que le sprite n'a pas de pixel à cet endroit, donc nous n'avons pas à nous soucier de le dessiner ou de l'effacer. Si la valeur est 1, nous passons à une autre instruction if qui vérifie la valeur de retour de `setPixel`. Regardons les valeurs passées à cette fonction.

Notre appel `setPixel` ressemble à ceci : `this.renderer.setPixel(this.v[x] + col, this.v[y] + row)`. Selon la référence technique, les positions `x` et `y` sont situées dans `Vx` et `Vy` respectivement. Ajoutez le numéro `col` à `Vx` et le numéro `row` à `Vy`, et vous obtenez la position souhaitée pour dessiner/effacer un pixel. 

Si `setPixel` retourne 1, nous effaçons le pixel et définissons `VF` à 1. Si elle retourne 0, nous ne faisons rien, gardant la valeur de `VF` égale à 0.

Enfin, nous décalons le sprite de 1 bit vers la gauche. Cela nous permet de parcourir chaque bit du sprite. 

Par exemple, si `sprite` est actuellement défini à `10010000`, il deviendra `0010000` après avoir été décalé vers la gauche. À partir de là, nous pouvons parcourir une autre itération de notre boucle `for` interne pour déterminer s'il faut dessiner un pixel ou non. Et continuer ce processus jusqu'à ce que nous atteignions la fin de notre sprite.

#### Ex9E - SKP Vx

Celle-ci est assez simple et saute simplement l'instruction suivante si la touche stockée dans `Vx` est pressée, en incrémentant le compteur de programme de 2.

```javascript
case 0x9E:
    if (this.keyboard.isKeyPressed(this.v[x])) {
        this.pc += 2;
    }
    break;
```

#### ExA1 - SKNP Vx

Cela fait l'inverse de l'instruction précédente. Si la touche spécifiée n'est pas pressée, sautez l'instruction suivante.

```javascript
case 0xA1:
    if (!this.keyboard.isKeyPressed(this.v[x])) {
        this.pc += 2;
    }
    break;
```

#### Fx07 - LD Vx, DT

Une autre instruction simple. Nous définissons simplement `Vx` à la valeur stockée dans `delayTimer`.

```javascript
case 0x07:
    this.v[x] = this.delayTimer;
    break;
```

#### Fx0A - LD Vx, K

En regardant la référence technique, cette instruction met en pause l'émulateur jusqu'à ce qu'une touche soit pressée. Voici le code pour cela :

```javascript
case 0x0A:
    this.paused = true;

    this.keyboard.onNextKeyPress = function(key) {
        this.v[x] = key;
        this.paused = false;
    }.bind(this);
    break;
```

Nous définissons d'abord `paused` à true afin de mettre en pause l'émulateur. Ensuite, si vous vous souvenez de notre fichier `keyboard.js` où nous avons défini `onNextKeyPress` à null, c'est là que nous l'initialisons. Avec la fonction `onNextKeyPress` initialisée, la prochaine fois que l'événement `keydown` est déclenché, le code suivant dans notre fichier `keyboard.js` sera exécuté :

```javascript
// keyboard.js
if (this.onNextKeyPress !== null && key) {
    this.onNextKeyPress(parseInt(key));
    this.onNextKeyPress = null;
}
```

À partir de là, nous définissons `Vx` au code de la touche pressée et enfin redémarrons l'émulateur en définissant `paused` à false.

### Fx15 - LD DT, Vx

Cette instruction définit simplement la valeur du temporisateur de délai à la valeur stockée dans le registre `Vx`.

```javascript
case 0x15:
    this.delayTimer = this.v[x];
    break;
```

#### Fx18 - LD ST, Vx

Cette instruction est très similaire à Fx15 mais définit le temporisateur de son à `Vx` au lieu du temporisateur de délai.

```javascript
case 0x18:
    this.soundTimer = this.v[x];
    break;
```

#### Fx1E - ADD I, Vx

Ajoute `Vx` à `I`.

```javascript
case 0x1E:
    this.i += this.v[x];
    break;
```

#### Fx29 - LD F, Vx - ADD I, Vx

Pour celle-ci, nous définissons `I` à l'emplacement du sprite à `Vx`. Il est multiplié par 5 car chaque sprite fait 5 octets de long.

```javascript
case 0x29:
    this.i = this.v[x] * 5;
    break;
```

#### Fx33 - LD B, Vx

Cette instruction va récupérer les chiffres des centaines, des dizaines et des unités du registre `Vx` et les stocker dans les registres `I`, `I+1`, et `I+2` respectivement.

```javascript
case 0x33:
    // Obtient le chiffre des centaines et le place dans I.
    this.memory[this.i] = parseInt(this.v[x] / 100);

    // Obtient le chiffre des dizaines et le place dans I+1. Obtient une valeur entre 0 et 99,
    // puis divise par 10 pour nous donner une valeur entre 0 et 9.
    this.memory[this.i + 1] = parseInt((this.v[x] % 100) / 10);

    // Obtient la valeur du chiffre des unités (dernier) et le place dans I+2.
    this.memory[this.i + 2] = parseInt(this.v[x] % 10);
    break;
```

#### Fx55 - LD [I], Vx

Dans cette instruction, nous parcourons les registres `V0` à `Vx` et stockons leur valeur en mémoire à partir de `I`.

```javascript
case 0x55:
    for (let registerIndex = 0; registerIndex <= x; registerIndex++) {
        this.memory[this.i + registerIndex] = this.v[registerIndex];
    }
    break;
```

#### Fx65 - LD Vx, [I]

Passons maintenant à la dernière instruction. Celle-ci fait l'inverse de `Fx55`. Elle lit les valeurs de la mémoire à partir de `I` et les stocke dans les registres `V0` à `Vx`.

```javascript
case 0x65:
    for (let registerIndex = 0; registerIndex <= x; registerIndex++) {
        this.v[registerIndex] = this.memory[this.i + registerIndex];
    }
    break;
```

## chip8.js

Avec notre classe CPU créée, terminons notre fichier `chip8.js` en chargeant une ROM et en cyclant notre CPU. Nous devons importer `cpu.js` et initialiser un objet CPU :

```javascript
import Renderer from './renderer.js';
import Keyboard from './keyboard.js';
import Speaker from './speaker.js';
import CPU from './cpu.js'; // NOUVEAU

const renderer = new Renderer(10);
const keyboard = new Keyboard();
const speaker = new Speaker();
const cpu = new CPU(renderer, keyboard, speaker); // NOUVEAU
```

Notre fonction `init` devient :

```javascript
function init() {
    fpsInterval = 1000 / fps;
    then = Date.now();
    startTime = then;

    cpu.loadSpritesIntoMemory(); // NOUVEAU
    cpu.loadRom('BLITZ'); // NOUVEAU
    loop = requestAnimationFrame(step);
}
```

Lorsque notre émulateur est initialisé, nous chargerons les sprites en mémoire et chargerons la rom `BLITZ`. Maintenant, nous devons simplement cycler le CPU :

```javascript
function step() {
    now = Date.now();
    elapsed = now - then;

    if (elapsed > fpsInterval) {
        cpu.cycle(); // NOUVEAU
    }

    loop = requestAnimationFrame(step);
}
```

Avec cela fait, nous devrions maintenant avoir un émulateur Chip8 fonctionnel.

## Conclusion

J'ai commencé ce projet il y a quelque temps et j'en ai été fasciné. La création d'émulateurs était toujours quelque chose qui m'intéressait mais qui n'avait jamais de sens pour moi. C'était jusqu'à ce que j'apprenne le Chip-8 et sa simplicité par rapport aux systèmes plus avancés qui existent. 

Le moment où j'ai terminé cet émulateur, j'ai su que je devais le partager avec d'autres personnes en fournissant un guide détaillé, étape par étape, pour le créer soi-même. Les connaissances que j'ai acquises, et que vous avez probablement acquises, seront sans aucun doute utiles ailleurs.

Dans l'ensemble, j'espère que vous avez apprécié l'article et appris quelque chose. J'ai visé à expliquer tout en détail et de la manière la plus simple possible. 

Quoi qu'il en soit, si quelque chose est encore confus pour vous ou si vous avez simplement une question, n'hésitez pas à me le faire savoir sur [Twitter](https://twitter.com/ericgrandt) ou à poster un problème sur le [dépôt GitHub](https://github.com/Erigitic/chip8-emulator/issues) car je serais ravi de vous aider.

J'aimerais vous laisser avec quelques idées de fonctionnalités que vous pouvez ajouter à votre émulateur Chip-8 :

- Contrôle audio (muet, changer de fréquence, changer de type d'onde (sinus, triangle), etc.)
- Capacité à changer l'échelle de rendu et la vitesse de l'émulateur depuis l'interface utilisateur
- Pause et reprise
- Capacité à sauvegarder et charger une sauvegarde
- Sélection de ROM