---
title: Comment coder le Jeu de la Vie avec React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-05T02:02:27.000Z'
originalURL: https://freecodecamp.org/news/coding-the-game-of-life-with-react-7de2385b7356
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Z2we98iWm4lJhulaYN_hwg.jpeg
tags:
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: technology
  slug: technology
seo_title: Comment coder le Jeu de la Vie avec React
seo_desc: 'By Pablo Regen

  The Game of Life involves a two-dimensional orthogonal grid of square cells, each
  of which is in one of two possible states, alive or dead. At each step, every cell
  interacts with its eight adjacent neighbors by following a simple set ...'
---

Par Pablo Regen

Le [Jeu de la Vie](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) implique une grille orthogonale bidimensionnelle de cellules carrées, chacune d'entre elles étant dans l'un des deux états possibles, vivant ou mort. À chaque étape, chaque cellule interagit avec ses huit voisins adjacents en suivant un ensemble simple de règles résultant en des naissances et des morts.

C'est un jeu à zéro joueur. Son évolution est déterminée par son état initial, ne nécessitant aucune autre entrée de la part des joueurs. On interagit avec le jeu en créant une configuration initiale et en observant comment elle évolue, ou, pour les joueurs avancés, en créant des motifs avec des propriétés particulières.

#### Règles

1. Toute cellule vivante avec moins de deux voisins vivants meurt, comme par sous-population
2. Toute cellule vivante avec deux ou trois voisins vivants vit jusqu'à la génération suivante
3. Toute cellule vivante avec plus de trois voisins vivants meurt, comme par surpopulation
4. Toute cellule morte avec exactement trois voisins vivants devient une cellule vivante, comme par reproduction

Bien que le jeu puisse être parfaitement codé avec du JavaScript vanilla, j'étais heureux de relever le défi avec React. Alors commençons.

### Installation de React

Il existe plusieurs façons de configurer React, mais si vous êtes nouveau dans ce domaine, je vous recommande de consulter la documentation **Create React App** [docs](https://reactjs.org/docs/create-a-new-react-app.html#create-react-app) et [github](https://github.com/facebook/create-react-app), ainsi que l'aperçu détaillé de React par [Tania Rascia](https://www.taniarascia.com/getting-started-with-react/).

### Conception du jeu

![Image](https://cdn-media-1.freecodecamp.org/images/1*i4rSdvv7psUjpMMMMk4WRg.jpeg)
_Contrôleurs_

L'image principale en haut est mon implémentation du jeu. La grille du plateau contenant des cellules claires (vivantes) et sombres (mortes) affiche l'évolution du jeu. Les contrôleurs vous permettent de démarrer/arrêter, d'avancer étape par étape, de configurer un nouveau plateau ou de l'effacer pour expérimenter avec vos propres motifs en cliquant sur les cellules individuelles. Le curseur contrôle la vitesse, et la génération informe du nombre d'itérations complétées.

En plus du composant principal contenant l'état, je vais créer séparément une fonction pour générer l'état de toutes les cellules du plateau à partir de zéro, un composant pour la grille du plateau et un autre pour le curseur.

### Configuration de App.js

Tout d'abord, importons React et React.Component depuis "react". Ensuite, établissons combien de lignes et de colonnes la grille du plateau a. Je choisis 40 par 60, mais n'hésitez pas à jouer avec différents nombres. Ensuite, viennent la fonction séparée et les composants de fonction (remarquez la première lettre en majuscule) décrits ci-dessus ainsi que le composant de classe contenant l'état et les méthodes, y compris le rendu. Enfin, exportons le composant principal App.

```js
import React, { Component } from 'react';

const totalBoardRows = 40;
const totalBoardColumns = 60;

const newBoardStatus = () => {};
const BoardGrid = () => {};
const Slider = () => {};

class App extends Component {
    state = {};

    // Méthodes ...

    render() {
        return (
            
        );
    }
}

export default App;
```

#### Génération d'un nouvel état de cellule de plateau

Puisque nous devons connaître l'état de chaque cellule **et** de ses 8 voisins pour chaque itération, créons une fonction qui retourne un tableau de tableaux contenant chacun des cellules avec des valeurs booléennes. Le nombre de tableaux dans le tableau principal correspondra au nombre de lignes, et le nombre de valeurs dans chacun de ces tableaux correspondra au nombre de colonnes. Ainsi, chaque valeur booléenne représentera l'état de chaque cellule, "vivante" ou "morte". Le paramètre de la fonction est par défaut inférieur à 30% de chance d'être vivant, mais vous pouvez expérimenter avec d'autres nombres.

```js
const newBoardStatus = (cellStatus = () => Math.random() < 0.3) => {
    const grid = [];
    for (let r = 0; r < totalBoardRows; r++) {
        grid[r] = [];
        for (let c = 0; c < totalBoardColumns; c++) {
            grid[r][c] = cellStatus();
        }
    }
    return grid;
};

/* Retourne un tableau de tableaux, chacun contenant des valeurs booléennes
(40) [Array(60), Array(60), ... ]
0: (60) [true, false, true, ... ]
1: (60) [false, false, false, ... ]
2: (60) [false, false, true, ...]
...
*/
```

#### Génération de la grille du plateau

Définissons un composant de fonction qui crée la grille du plateau et l'assigne à une variable. La fonction reçoit l'état de l'état complet du plateau et une méthode qui permet aux utilisateurs de basculer l'état des cellules individuelles en tant que props. Cette méthode est définie sur le composant principal où tout l'état de l'application est conservé.

Chaque cellule est représentée par un <td> de tableau et a un attribut className dont la valeur dépend de la valeur booléenne de la cellule correspondante du plateau. Le joueur cliquant sur une cellule entraîne l'appel de la méthode passée en tant que props avec l'emplacement de la ligne et de la colonne de la cellule en tant qu'argument.

Consultez [Lifting State Up](https://reactjs.org/docs/lifting-state-up.html#lifting-state-up) pour plus d'informations sur le passage des méthodes en tant que props, et n'oubliez pas d'ajouter les [keys](https://reactjs.org/docs/lists-and-keys.html#keys).

```js
const BoardGrid = ({ boardStatus, onToggleCellStatus }) => {
    const handleClick = (r,c) => onToggleCellStatus(r,c);

    const tr = [];
    for (let r = 0; r < totalBoardRows; r++) {
        const td = [];
        for (let c = 0; c < totalBoardColumns; c++) {
            td.push(
                <td
                    key={`${r},${c}`}
                    className={boardStatus[r][c] ? 'alive' : 'dead'}
                    onClick={() => handleClick(r,c)}
                />
            );
        }
        tr.push(<tr key={r}>{td}</tr>);
    }
    return <table><tbody>{tr}</tbody></table>;
};
```

#### Création du curseur de vitesse

Ce composant de fonction crée un curseur pour permettre aux joueurs de changer la vitesse des itérations. Il reçoit l'état de la vitesse actuelle et une méthode pour gérer le changement de vitesse en tant que props. Vous pouvez essayer différentes valeurs minimales, maximales et de pas. Un changement de vitesse entraîne l'appel de la méthode passée en tant que props avec la vitesse souhaitée en tant qu'argument.

```js
const Slider = ({ speed, onSpeedChange }) => {
    const handleChange = e => onSpeedChange(e.target.value);

    return (
        <input
            type='range'
            min='50'
            max='1000'
            step='50'
            value={speed}
            onChange={handleChange}
        />
    );
};
```

### Composant principal

Puisqu'il contient l'état de l'application, faisons-en un composant de classe. Notez que je n'utilise pas les [Hooks](https://reactjs.org/docs/hooks-intro.html), une nouvelle addition dans React 16.8 qui vous permet d'utiliser l'état et d'autres fonctionnalités de React sans écrire de classe. Je préfère utiliser la [syntaxe de champ de classe publique expérimentale](https://reactjs.org/docs/handling-events.html), donc je ne lie pas les méthodes dans le constructeur.

Décortiquons-le.

#### État

Je définis l'état comme un objet avec les propriétés pour l'état du plateau, le nombre de générations, le jeu en cours ou arrêté et la vitesse des itérations. Lorsque le jeu commence, l'état des cellules du plateau sera celui retourné par l'appel à la fonction qui génère un nouvel état de plateau. La génération commence à 0 et le jeu ne s'exécutera qu'après que l'utilisateur ait décidé. La vitesse par défaut est de 500ms.

```js
class App extends Component {
    state = {
        boardStatus: newBoardStatus(),
        generation: 0,
        isGameRunning: false,
        speed: 500
    };

    // Autres méthodes ...

}
```

#### Bouton Démarrer/Arrêter

Fonction qui retourne un élément de bouton différent en fonction de l'état du jeu : en cours ou arrêté.

```js
class App extends Component {
    state = {...};

    runStopButton = () => {
        return this.state.isGameRunning ?
        <button type='button' onClick={this.handleStop}>Arrêter</button> :
        <button type='button' onClick={this.handleRun}>Démarrer</button>;
    }
    
    // Autres méthodes ...
}
```

#### Effacer et nouveau plateau

Méthodes pour gérer la demande des joueurs de commencer avec un nouvel état aléatoire des cellules du plateau ou d'effacer complètement le plateau afin qu'ils puissent ensuite expérimenter en basculant l'état des cellules individuelles. La différence entre elles est que celle qui efface le plateau définit l'état de toutes les cellules à false, tandis que l'autre ne passe aucun argument à la méthode newBoardStatus afin que l'état de chaque cellule devienne par défaut une valeur booléenne aléatoire.

```js
class App extends Component {
    state = {...};
    runStopButton = () => {...}
    
    handleClearBoard = () => {
        this.setState({
            boardStatus: newBoardStatus(() => false),
            generation: 0
        });
    }

    handleNewBoard = () => {
        this.setState({
            boardStatus: newBoardStatus(),
            generation: 0
        });
    }
    
    // Plus de méthodes ...
    
 }
```

#### Basculer l'état de la cellule

![Image](https://cdn-media-1.freecodecamp.org/images/1*ANLpEyZqmtk4HTqjXTSRvA.jpeg)
_Cliquer sur une cellule bascule son état entre vrai (vivant) et faux (mort)_

Nous avons besoin d'une méthode pour gérer les demandes des joueurs de basculer l'état des cellules individuelles, ce qui est utile pour expérimenter avec des motifs personnalisés directement sur le plateau. Le composant BoardGrid l'appelle chaque fois que le joueur clique sur une cellule. Il définit les états de l'état du plateau en appelant une fonction et [en lui passant l'état précédent comme argument](https://reactjs.org/docs/state-and-lifecycle.html#state-updates-may-be-asynchronous).

La fonction clone en profondeur l'état précédent du plateau pour éviter de le modifier par référence lors de la mise à jour d'une cellule individuelle à la ligne suivante. (L'utilisation de `const clonedBoardStatus = [...boardStatus]` modifierait l'état original car la syntaxe Spread va effectivement à un niveau de profondeur lors de la copie d'un tableau, donc elle peut être [inadaptée pour copier des tableaux multidimensionnels](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax#Spread_in_array_literals). Notez que `JSON.parse(JSON.stringify(obj))` ne fonctionne pas si l'objet cloné utilise des fonctions). La fonction retourne enfin l'état du plateau cloné mis à jour, mettant ainsi à jour l'état du plateau.

Pour le clonage en profondeur, consultez [ici](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/assign#Deep_Clone), [ici](https://stackoverflow.com/questions/122102/what-is-the-most-efficient-way-to-deep-clone-an-object-in-javascript) et [ici](https://stackoverflow.com/questions/728360/how-do-i-correctly-clone-a-javascript-object).

```js
class App extends Component {
    state = {...};
    runStopButton = () => {...}
    handleClearBoard = () => {...}
    handleNewBoard = () => {...}

    handleToggleCellStatus = (r,c) => {
        const toggleBoardStatus = prevState => {
            const clonedBoardStatus = JSON.parse(JSON.stringify(prevState.boardStatus));
            clonedBoardStatus[r][c] = !clonedBoardStatus[r][c];
            return clonedBoardStatus;
        };

        this.setState(prevState => ({
            boardStatus: toggleBoardStatus(prevState)
        }));
    }
    
    // Autres méthodes ...
    
}
```

#### Génération de l'étape suivante

C'est ici que la prochaine itération du jeu est générée en définissant l'état de l'état du plateau à la valeur retournée par une fonction. Elle ajoute également un à l'état de la génération pour informer le joueur du nombre d'itérations produites jusqu'à présent.

La fonction ("nextStep") définit deux variables : l'état du plateau et un état du plateau cloné en profondeur. Ensuite, une fonction calcule le nombre de voisins (dans le plateau) avec la valeur true pour une cellule individuelle, chaque fois qu'elle est appelée. En raison des règles, il n'est pas nécessaire de compter plus de quatre voisins vrais par cellule. Enfin, et selon les règles, elle met à jour l'état de la cellule individuelle du plateau cloné et retourne l'état du plateau cloné, qui est utilisé dans le setState.

```js
class App extends Component {
    state = {...};
    runStopButton = () => {...}
    handleClearBoard = () => {...}
    handleNewBoard = () => {...}
    handleToggleCellStatus = () => {...}

    handleStep = () => {
        const nextStep = prevState => {
            const boardStatus = prevState.boardStatus;
            const clonedBoardStatus = JSON.parse(JSON.stringify(boardStatus));
			
            const amountTrueNeighbors = (r,c) => {
                const neighbors = [[-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1]];
                return neighbors.reduce((trueNeighbors, neighbor) => {
                    const x = r + neighbor[0];
                    const y = c + neighbor[1];
                    const isNeighborOnBoard = (x >= 0 && x < totalBoardRows && y >= 0 && y < totalBoardColumns);
                    /* Pas besoin de compter plus de 4 voisins vivants */
                    if (trueNeighbors < 4 && isNeighborOnBoard && boardStatus[x][y]) {
                        return trueNeighbors + 1;
                    } else {
			return trueNeighbors;
		    }
                }, 0);
            };
			
            for (let r = 0; r < totalBoardRows; r++) {
                for (let c = 0; c < totalBoardColumns; c++) {
                    const totalTrueNeighbors = amountTrueNeighbors(r,c);
					
                    if (!boardStatus[r][c]) {
                        if (totalTrueNeighbors === 3) clonedBoardStatus[r][c] = true;
                    } else {
                        if (totalTrueNeighbors < 2 || totalTrueNeighbors > 3) clonedBoardStatus[r][c] = false;
                    }
                }
            }
			
            return clonedBoardStatus;
        };
		
        this.setState(prevState => ({
            boardStatus: nextStep(prevState),
            generation: prevState.generation + 1
        }));
    }
	
    // Autres méthodes ...
}

```

#### Gestion du changement de vitesse et de l'action démarrer/arrêter

Ces 3 méthodes définissent uniquement la valeur de l'état pour les propriétés de vitesse et isGameRunning.

Ensuite, dans la méthode de cycle de vie componentDidUpdate, effaçons et/ou définissons un minuteur en fonction de différentes combinaisons de valeurs. Le minuteur planifie un appel à la méthode handleStep à des intervalles de vitesse spécifiés.

```js
class App extends Component {
    state = {...};
    runStopButton = () => {...}
    handleClearBoard = () => {...}
    handleNewBoard = () => {...}
    handleToggleCellStatus = () => {...}
    handleStep = () => {...}
                        
    handleSpeedChange = newSpeed => {
        this.setState({ speed: newSpeed });
    }

    handleRun = () => {
        this.setState({ isGameRunning: true });
    }

    handleStop = () => {
        this.setState({ isGameRunning: false });
    }

    componentDidUpdate(prevProps, prevState) {
        const { isGameRunning, speed } = this.state;
        const speedChanged = prevState.speed !== speed;
        const gameStarted = !prevState.isGameRunning && isGameRunning;
        const gameStopped = prevState.isGameRunning && !isGameRunning;

        if ((isGameRunning && speedChanged) || gameStopped) {
            clearInterval(this.timerID);
        }

        if ((isGameRunning && speedChanged) || gameStarted) {
            this.timerID = setInterval(() => {
                this.handleStep();
            }, speed);
        }
    }
                        
    // Méthode de rendu ...
}
```

#### La méthode de rendu

La dernière méthode dans le composant App retourne la structure et les informations souhaitées de la page à afficher. Puisque l'état appartient au composant App, nous passons l'état et les méthodes aux composants qui en ont besoin en tant que props.

```js
class App extends Component {
    // Toutes les méthodes précédentes ...

    render() {
        const { boardStatus, isGameRunning, generation, speed } = this.state;

        return (
            <div>
                <h1>Jeu de la Vie</h1>
                <BoardGrid boardStatus={boardStatus} onToggleCellStatus={this.handleToggleCellStatus} />
                <div className='flexRow upperControls'
                    <span>
                        {'+ '}
                        <Slider speed={speed} onSpeedChange={this.handleSpeedChange} />
                        {' -'}
                    </span>
                    {`Génération: ${generation}`}
                </div>
                <div className='flexRow lowerControls'>
                    {this.runStopButton()}
                    <button type='button' disabled={isGameRunning} onClick={this.handleStep}>Étape</button>
                    <button type='button' onClick={this.handleClearBoard}>Effacer le plateau</button>
                    <button type='button' onClick={this.handleNewBoard}>Nouveau plateau</button>
                </div>
            </div>
        );
    }
}
```

#### Exportation de l'application par défaut

Enfin, exportons l'application par défaut (`export default App;`), qui est importée avec les styles depuis "index.scss" par "index.js", puis rendue dans le DOM.

#### **Et c'est tout ! ?**

Consultez le **code complet** sur [github](https://github.com/PabloRegen/game-of-life) et **jouez au jeu** [ici](https://pabloregen.github.io/game-of-life/). Essayez [ces](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life#Examples_of_patterns) motifs ci-dessous ou créez les vôtres pour le plaisir.

![Image](https://cdn-media-1.freecodecamp.org/images/1*1sjLBUCncLtAeAKrdjaiVQ.jpeg)
_De Wikipedia : exemples fréquemment rencontrés_

Merci d'avoir lu.