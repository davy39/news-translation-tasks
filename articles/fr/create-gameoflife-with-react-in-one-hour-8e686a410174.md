---
title: Comment coder le "Jeu de la Vie" avec React en moins d'une heure
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-04T02:20:37.000Z'
originalURL: https://freecodecamp.org/news/create-gameoflife-with-react-in-one-hour-8e686a410174
coverImage: https://cdn-media-1.freecodecamp.org/images/1*MQ_6N0WX9UCSAKC3DLFOQw.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment coder le "Jeu de la Vie" avec React en moins d'une heure
seo_desc: 'By Charlee Li

  Recently I watched the famous video that creates a snake game in less than 5 minutes
  (on Youtube). It looked pretty interesting to do this type of quick coding, so I
  decided to do one by myself.

  When I started to learn programming as a ...'
---

Par Charlee Li

Récemment, j'ai regardé la célèbre vidéo qui crée un jeu de serpent en moins de 5 minutes (sur [YouTube](https://www.youtube.com/watch?v=xGmXxpIj6vs)). Cela semblait assez intéressant de faire ce type de codage rapide, alors j'ai décidé d'en faire un moi-même.

Quand j'ai commencé à apprendre la programmation enfant, j'ai appris un jeu appelé « [Jeu de la Vie](https://en.wikipedia.org/wiki/Conway's_Game_of_Life) ». C'est un excellent exemple d'automatisation cellulaire et de la manière dont des règles simples peuvent aboutir à des motifs complexes. Imaginez une sorte de forme de vie vivant dans un monde. À chaque tour, elles suivent quelques règles simples pour décider si une vie est vivante ou morte.

[**Jeu de la Vie de Conway - Wikipédia**](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)
[_Depuis sa publication, le Jeu de la Vie de Conway a suscité beaucoup d'intérêt, en raison des façons surprenantes dont..._ en.wikipedia.org](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)

J'ai donc décidé de coder ce jeu. Comme il ne nécessite pas trop de graphismes — juste une grille et quelques blocs — j'ai décidé que React serait un bon choix, et il peut être utilisé comme un tutoriel rapide pour React. Commençons !

### Installation de React

Tout d'abord, nous devons installer React. L'outil incroyable `[create-react-app](https://github.com/facebook/create-react-app)` est très pratique pour démarrer un nouveau projet React :

```
$ npm install -g create-react-app
$ create-react-app react-gameoflife
```

Après moins d'une minute, `react-gameoflife` sera prêt. Maintenant, tout ce que nous avons à faire est de le démarrer :

```
$ cd react-gameoflife
$ npm start
```

Cela démarrera un serveur de développement à l'adresse [http://localhost:3000](http://localhost:3000), et une fenêtre de navigateur s'ouvrira à cette adresse.

### Choix de conception

L'écran final que nous voulons créer ressemble à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/VdXPrJSLu6cEFtDpryJmUPMfHTfVUCT6i9H4)
_Jeu de la Vie de Conway_

Il s'agit simplement d'un plateau avec une grille et quelques tuiles blanches (« cellules ») qui peuvent être placées ou supprimées en cliquant sur la grille. Le bouton « Run » démarrera les itérations à un intervalle donné.

Cela semble assez simple, n'est-ce pas ? Réfléchissons à la manière de faire cela avec React. Tout d'abord, React n'est **pas** un framework graphique, donc nous ne penserons pas à utiliser canvas. (Vous pouvez jeter un œil à [PIXI](http://www.pixijs.com/) ou [Phaser](https://phaser.io/) si vous êtes intéressé par l'utilisation de canvas.)

Le plateau peut être un composant et peut être rendu avec un seul `<div>`. Et la grille ? Il n'est pas faisable de dessiner les grilles avec des `<div>`, et comme la grille est statique, c'est aussi inutile. En effet, nous pouvons utiliser le dégradé linéaire CSS3 pour la grille.

En ce qui concerne les cellules, nous pouvons utiliser `<div>` pour dessiner chaque cellule. Nous en ferons un composant séparé. Ce composant accepte x, y en entrées afin que le plateau puisse spécifier sa position.

### Première étape : le plateau

Créons d'abord le plateau. Créez un fichier appelé `Game.js` sous le répertoire `src` et tapez le code suivant :

```
import React from 'react';
import './Game.css';
```

```
const CELL_SIZE = 20;
const WIDTH = 800;
const HEIGHT = 600;
```

```
class Game extends React.Component {
  render() {
    return (
      <div>
        <div className="Board"
          style={{ width: WIDTH, height: HEIGHT }}>
        </div>
      </div>
    );
  }
}
```

```
export default Game;
```

Nous avons également besoin du fichier `Game.css` pour définir les styles :

```
.Board {
  position: relative;
  margin: 0 auto;
  background-color: #000;
}
```

Mettez à jour `App.js` pour importer notre `Game.js` et placer le composant `Game` sur l'écran. Maintenant, nous pouvons voir un plateau de jeu complètement noir.

Notre prochaine étape est de créer la grille. La grille peut être créée avec une seule ligne de `linear-gradient` (ajoutez ceci à `Game.css`) :

```
background-image:
    linear-gradient(#333 1px, transparent 1px),
    linear-gradient(90deg, #333 1px, transparent 1px);
```

En fait, nous devons également spécifier le style `background-size` pour que cela fonctionne. Mais comme la constante `CELL_SIZE` est définie dans `Game.js`, nous spécifierons la taille de l'arrière-plan avec le style en ligne directement. Changez la ligne `style` dans `Game.js` :

```
<div className="Board"
  style={{ width: WIDTH, height: HEIGHT,
    backgroundSize: `${CELL_SIZE}px ${CELL_SIZE}px`}}></div>
```

Actualisez le navigateur et vous verrez une belle grille.

![Image](https://cdn-media-1.freecodecamp.org/images/HcVZMkOP0xyAXJs6kXciMYrzgnraPUf-ZZVQ)
_Grille, réalisée avec le dégradé CSS3._

### Créer les cellules

L'étape suivante consiste à permettre à l'utilisateur d'interagir avec le plateau pour créer les cellules. Nous utiliserons un tableau 2D `this.board` pour conserver l'état du plateau, et une liste de cellules `this.state.cells` pour conserver la position des cellules. Une fois l'état du plateau mis à jour, une méthode `this.makeCells()` sera appelée pour générer la liste des cellules à partir de l'état du plateau.

Ajoutez ces méthodes à la classe `Game` :

```
class Game extends React.Component {
  constructor() {
    super();
    this.rows = HEIGHT / CELL_SIZE;
    this.cols = WIDTH / CELL_SIZE;
    this.board = this.makeEmptyBoard();
  }
```

```
  state = {
    cells: [],
  }
```

```
  // Créer un plateau vide
  makeEmptyBoard() {
    let board = [];
    for (let y = 0; y < this.rows; y++) {
      board[y] = [];
      for (let x = 0; x < this.cols; x++) {
        board[y][x] = false;
      }
    }
    return board;
  }
```

```
  // Créer des cellules à partir de this.board
  makeCells() {
    let cells = [];
    for (let y = 0; y < this.rows; y++) {
      for (let x = 0; x < this.cols; x++) {
        if (this.board[y][x]) {
          cells.push({ x, y });
        }
      }
    }
    return cells;
  }
  ...}
```

Ensuite, nous permettrons à l'utilisateur de cliquer sur le plateau pour placer ou supprimer une cellule. Dans React, un `<div>` peut être attaché avec un gestionnaire d'événements `onClick`, qui pourrait récupérer la coordonnée du clic via l'événement de clic. Cependant, la coordonnée est relative à la zone cliente (la zone visible du navigateur), donc nous avons besoin d'un code supplémentaire pour la convertir en une coordonnée qui est relative au plateau.

Ajoutez le gestionnaire d'événements à la méthode `render()`. Ici, nous sauvegardons également la référence de l'élément du plateau afin de récupérer l'emplacement du plateau plus tard.

```
render() {
  return (
    <div>
      <div className="Board"
        style={{ width: WIDTH, height: HEIGHT,
          backgroundSize: `${CELL_SIZE}px ${CELL_SIZE}px`}}
        onClick={this.handleClick}
        ref={(n) => { this.boardRef = n; }}>
      </div>
    </div>
  );
}
```

Et voici quelques méthodes supplémentaires. Ici, `getElementOffset()` calculera la position de l'élément du plateau. `handleClick()` récupérera la position du clic, puis la convertira en position relative, et calculera les colonnes et les lignes de la cellule cliquée. Ensuite, l'état de la cellule est inversé.

```
class Game extends React.Component {
  ...
  getElementOffset() {
    const rect = this.boardRef.getBoundingClientRect();
    const doc = document.documentElement;

    return {
      x: (rect.left + window.pageXOffset) - doc.clientLeft,
      y: (rect.top + window.pageYOffset) - doc.clientTop,
    };
  }
```

```
  handleClick = (event) => {
    const elemOffset = this.getElementOffset();
    const offsetX = event.clientX - elemOffset.x;
    const offsetY = event.clientY - elemOffset.y;
        const x = Math.floor(offsetX / CELL_SIZE);
    const y = Math.floor(offsetY / CELL_SIZE);
```

```
    if (x >= 0 && x <= this.cols && y >= 0 && y <= this.rows) {
      this.board[y][x] = !this.board[y][x];
    }
```

```
    this.setState({ cells: this.makeCells() });
  }
  ...}
```

En tant que dernière étape, nous allons rendre les cellules `this.state.cells` sur le plateau :

```
class Cell extends React.Component {
  render() {
    const { x, y } = this.props;
    return (
      <div className="Cell" style={{
        left: `${CELL_SIZE * x + 1}px`,
        top: `${CELL_SIZE * y + 1}px`,
        width: `${CELL_SIZE - 1}px`,
        height: `${CELL_SIZE - 1}px`,
      }} />
    );
  }
}
```

```
class Game extends React.Component {
  ...
  render() {
    const { cells } = this.state;
    return (
      <div>
        <div className="Board"
          style={{ width: WIDTH, height: HEIGHT,
            backgroundSize: `${CELL_SIZE}px ${CELL_SIZE}px`}}
          onClick={this.handleClick}
          ref={(n) => { this.boardRef = n; }}>
          {cells.map(cell => (
            <Cell x={cell.x} y={cell.y}
                key={`${cell.x},${cell.y}`}/>
          ))}
        </div>
              </div>
    );
  }
  ...}
```

Et n'oubliez pas d'ajouter des styles pour le composant `Cell` (dans `Game.css`) :

```
.Cell {
  background: #ccc;
  position: absolute;
}
```

Actualisez le navigateur et essayez de cliquer sur le plateau. Les cellules peuvent maintenant être placées ou supprimées !

![Image](https://cdn-media-1.freecodecamp.org/images/haXwArXI6t0pARVfN7IMbkUTKLkjexifGZCR)
_Les cellules peuvent être placées ou supprimées en cliquant sur le plateau._

### Exécuter le jeu

Maintenant, nous avons besoin de quelques helpers pour exécuter le jeu. Tout d'abord, ajoutons quelques contrôleurs.

```
class Game extends React.Component {
  state = {
    cells: [],
    interval: 100,
    isRunning: false,
  }
  ...
```

```
  runGame = () => {
    this.setState({ isRunning: true });
  }
```

```
  stopGame = () => {
    this.setState({ isRunning: false });
  }
```

```
  handleIntervalChange = (event) => {
    this.setState({ interval: event.target.value });
  }
```

```
  render() {
    return (
      ...
        <div className="controls">
          Update every <input value={this.state.interval}
              onChange={this.handleIntervalChange} /> msec
          {isRunning ?
            <button className="button"
              onClick={this.stopGame}>Stop</button> :
            <button className="button"
              onClick={this.runGame}>Run</button>
          }
        </div>
      ...
    );
  }
}
```

Ce code ajoutera une entrée d'intervalle et un bouton en bas de l'écran.

![Image](https://cdn-media-1.freecodecamp.org/images/5IdZVY7GD1McREviUPScFMMMX7U0SGmMgnqn)
_Contrôleurs_

Notez que cliquer sur Run n'a aucun effet, car nous n'avons rien écrit pour exécuter le jeu. Alors faisons cela maintenant.

Dans ce jeu, l'état du plateau est mis à jour à chaque itération. Ainsi, nous avons besoin d'une méthode `runIteration()` à appeler à chaque itération, disons, toutes les 100 ms. Cela peut être réalisé en utilisant `window.setTimeout()`.

Lorsque le bouton Run est cliqué, `runIteration()` sera appelé. Avant qu'il ne se termine, il appellera `window.setTimeout()` pour organiser une autre itération après 100 ms. De cette manière, `runIteration()` sera appelé de manière répétée. Lorsque le bouton Stop est cliqué, nous annulerons le timeout organisé en appelant `window.clearTimeout()` afin que les itérations puissent être arrêtées.

```
class Game extends React.Component {
  ...
  runGame = () => {
    this.setState({ isRunning: true });
    this.runIteration();
  }
```

```
  stopGame = () => {
    this.setState({ isRunning: false });
    if (this.timeoutHandler) {
      window.clearTimeout(this.timeoutHandler);
      this.timeoutHandler = null;
    }
  }
```

```
  runIteration() {
    console.log('running iteration');
    let newBoard = this.makeEmptyBoard();
```

```
    // TODO: Ajouter la logique pour chaque itération ici.
```

```
    this.board = newBoard;
    this.setState({ cells: this.makeCells() });
```

```
    this.timeoutHandler = window.setTimeout(() => {
      this.runIteration();
    }, this.state.interval);
  }
  ...}
```

Rechargez le navigateur et cliquez sur le bouton « Run ». Nous verrons le message de log « running iteration » dans la console. (Si vous ne savez pas comment afficher la console, essayez d'appuyer sur Ctrl-Shift-I.)

Maintenant, nous devons ajouter les règles du jeu à la méthode `runIteration()`. Selon Wikipédia, le Jeu de la Vie a quatre règles :

> 1. Toute cellule vivante avec moins de deux voisins vivants meurt, comme si cela était causé par une sous-population.

> 2. Toute cellule vivante avec deux ou trois voisins vivants vit jusqu'à la génération suivante.

> 3. Toute cellule vivante avec plus de trois voisins vivants meurt, comme par surpopulation.

> 4. Toute cellule morte avec exactement trois voisins vivants devient une cellule vivante, comme par reproduction.

Nous pouvons ajouter une méthode `calculateNeighbors()` pour calculer le nombre de voisins d'une cellule donnée `(x, y)`. (Le code source de `calculateNeighbors()` sera omis dans cet article, mais vous pouvez le trouver [ici](https://github.com/charlee/react-gameoflife/blob/master/src/Game.js#L134).) Ensuite, nous pouvons implémenter les règles de manière directe :

```
for (let y = 0; y < this.rows; y++) {
  for (let x = 0; x < this.cols; x++) {
    let neighbors = this.calculateNeighbors(this.board, x, y);
    if (this.board[y][x]) {
      if (neighbors === 2 || neighbors === 3) {
        newBoard[y][x] = true;
      } else {
        newBoard[y][x] = false;
      }
    } else {
      if (!this.board[y][x] && neighbors === 3) {
        newBoard[y][x] = true;
      }
    }
  }
}
```

Rechargez le navigateur, placez quelques cellules initiales, puis appuyez sur le bouton Run. Vous pourriez voir quelques animations incroyables !

![Image](https://cdn-media-1.freecodecamp.org/images/Dzw9iypiLw8DF4gtJCTpUPNTMVDjDmQF9DSQ)
_Pistolet planeur de Gosper_

### Conclusion

Afin de rendre le jeu plus amusant, j'ai également ajouté un bouton Random et un bouton Clear pour aider à placer les cellules. Le code source complet peut être trouvé sur mon [GitHub](https://github.com/charlee/react-gameoflife).

Merci pour votre lecture ! Si vous trouvez cet article intéressant, veuillez le partager avec plus de personnes en le recommandant.