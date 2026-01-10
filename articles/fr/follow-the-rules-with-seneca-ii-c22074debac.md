---
title: Écrire un microservice d'échecs en utilisant Node.js et Seneca, Partie 2
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-06-14T19:44:26.000Z'
originalURL: https://freecodecamp.org/news/follow-the-rules-with-seneca-ii-c22074debac
coverImage: https://cdn-media-1.freecodecamp.org/images/1*kKyKqEjIfVK--SJT2-SoXQ.jpeg
tags:
- name: chess
  slug: chess
- name: JavaScript
  slug: javascript
- name: Microservices
  slug: microservices
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Écrire un microservice d'échecs en utilisant Node.js et Seneca, Partie
  2
seo_desc: 'By Jeff M Lowery

  Handling new requirements without refactoring

  Part 1 of this series talked about defining and calling microservices using Seneca.
  A handful of services were created to return all legal moves of a lone chess piece
  on a chessboard. The...'
---

Par Jeff M Lowery

#### Gérer de nouvelles exigences sans refactorisation

La [Partie 1](https://medium.freecodecamp.com/follow-the-rules-with-seneca-b3cf3d08fe5d) de cette série parlait de la définition et de l'appel de microservices en utilisant Seneca. Une poignée de services ont été créés pour retourner tous les mouvements légaux d'une pièce d'échecs seule sur un échiquier. La série continue dans la [Partie 3](https://medium.com/@jefflowery/writing-a-chess-microservice-using-node-js-and-seneca-part-3-ab38b8ef9b0a).

#### Un rapide rappel :

* Les services Seneca sont identifiés par un motif constitué de propriétés `role` et `cmd`. Des propriétés supplémentaires peuvent être ajoutées au motif également.

```js
this.add({
        role: "movement",
        cmd: "legalMoves"   //, otherProp: value, ...
    }, (msg, reply) => {...}
```

* Les services ont également une implémentation qui prend un objet `msg` et une fonction de rappel. L'objet `msg` contient les propriétés du motif en plus de toutes les autres données envoyées au service.
* `Seneca.act()` est utilisé pour invoquer indirectement un service. La méthode `act` prend un objet et une fonction de rappel. L'objet contient le `role`, `cmd`, et d'autres propriétés qui composent le message au service.

```js
seneca.act({
            role: "movement",
            cmd: "legalMoves",
            piece: p,
            board: board
        }, (err, msg) => {
```

* Lorsqu'une action pourrait être gérée par plus d'un service correspondant au motif, le service avec la [correspondance de motif la plus spécifique](http://senecajs.org/getting-started/#how-patterns-work) sera invoqué.

Il y avait une poignée de services définis dans la [première partie](https://medium.freecodecamp.com/follow-the-rules-with-seneca-b3cf3d08fe5d) de cette série. L'un des trois services `rawMoves` prenait une pièce et sa position en paramètres et retournait un masque de mouvement de 15 x 15. Ceux-ci étaient tronqués à un plateau de 8 x 8 en utilisant un service `legalSquares`. Le résultat était que les services ensemble pouvaient retourner tous les mouvements légaux de n'importe quelle pièce sur n'importe quelle case légale de l'échiquier autrement vide.

### Microservices et dette technique

L'une des motivations pour les microservices est de [réduire la dette technique](http://www.infoworld.com/article/2878659/application-development/reducing-technical-debt-with-microservices.html). Chaque projet a des délais et, à mesure qu'ils approchent, l'expédience l'emporte souvent sur la qualité. Les commentaires FIXME et TODO jonchent le code source après un certain temps. Ces commentaires identifient la dette technique qui « un jour » sera prise en charge.

#### Un jour qui n'arrive jamais

Les microservices se concentrent sur la décomposition fonctionnelle et le couplage lâche. Aucune de ces idées n'est nouvelle, mais c'est une réflexion sur la manière de mettre en œuvre ces concepts. Un microservice doit être petit, avoir un seul but et être extensible. L'extension d'un service peut se faire avec peu ou pas d'effets secondaires. Un nouveau service peut étendre un service existant, et ni l'ancien service ni le client qui l'appelait auparavant ne sauront que l'implémentation du service a changé. Moins de refactorisation de classes, de méthodes, de signatures de méthodes, de flux de processus... tout cela facilite la gestion de la redoutable dette technique.

### Retour au jeu en cours...

Déplacer une seule pièce d'échecs sur un échiquier solitaire n'est pas vraiment très divertissant. Dans un vrai jeu d'échecs, l'échiquier est partagé avec des pièces amies et hostiles, et celles-ci impactent les mouvements les unes des autres.

Actuellement, j'ai un service `legalSquares` qui peut servir de base à un service `legalMoves` plus complet. Si vous vous souvenez, le service `legalSquares` invoquait un service `rawMoves`, puis supprimait toutes les cases « mauvaises » qui n'appartenaient pas à un échiquier.

Le nouveau service `legalMoves` tiendra compte des autres pièces, ce que `legalSquares` ne faisait pas. Cela nécessite un paramètre supplémentaire, appelé `board`. Le `board` va simplement être un tableau d'instances de **ChessPiece**, et supposera que les pièces sur l'échiquier ont déjà été vérifiées pour leur validité. Par exemple, deux pièces n'occupent pas la même case, les pions ne sont pas sur la première rangée, les rois ne sont pas côte à côte, et ainsi de suite.

Le motif suivant identifiera le service :

```js
'role: movement;cmd: legalMoves'
```

Ce motif est une version stringifiée de JSON appelée **jsonic** ; vous pouvez utiliser un objet JSON régulier si vous préférez. Le message au service contiendra le motif. Il contiendra également une instance ChessPiece qui a un type de pièce tel que 'K'ing, 'Q'ueen, 'R'ook et une position sur l'échiquier (voir notation algébrique). Plus tard, j'ajouterai à cette classe une couleur de pièce (Blanc ou Noir) afin que le service puisse distinguer les amis des ennemis. Mais pour l'instant, le service supposera que toutes les pièces sont amies.

Puisqu'une pièce amie ne peut pas être capturée, elle restreindra le mouvement des autres pièces amies. Déterminer ces restrictions demande un peu de travail. Je me suis compliqué la tâche dans l'implémentation du service `rawMoves`... ce qui m'amène à :

### Les microservices ne sont pas une panacée

Si vous concevez un service qui récupère ou calcule des informations et **ne** transmet pas ces données en amont de la chaîne, un service en amont pourrait devoir refaire ce travail plus tard. Dans mon exemple, `rawMoves` retournait un tableau d'objets de mouvement (positions de fichier et de rang sur l'échiquier). Prenons la méthode qui génère les mouvements diagonaux pour une pièce en utilisant le service `rawMoves` :

```js
module.exports = function diagonal(position, range = 7) {
    var moves = [];
    const cFile = position.file.charCodeAt()
    const cRank = position.rank.charCodeAt();
    
for (var i = 1; i < range + 1; i++) {
        moves.push({
            file: String.fromCharCode(cFile - i),
            rank: String.fromCharCode(cRank - i)
        });
        moves.push({
            file: String.fromCharCode(cFile + i),
            rank: String.fromCharCode(cRank + i)
        });
        moves.push({
            file: String.fromCharCode(cFile - i),
            rank: String.fromCharCode(cRank + i)
        });
        moves.push({
            file: String.fromCharCode(cFile + i),
            rank: String.fromCharCode(cRank - i)
        });
    }
    return moves;
}
```

À première vue, il n'y a rien de mal avec cela. Mais ces quatre opérations `move.push` fonctionnent en réalité le long de **vecteurs de mouvement**. J'aurais pu construire quatre vecteurs de mouvement, puis retourner une liste de mouvements en les concaténant, comme ceci :

```js
function diagonalMoves(position, range) {
    var vectors = [[], [], [], []];
    const cFile = position.file.charCodeAt()
    const cRank = position.rank.charCodeAt();

    for (var i = 1; i < range + 1; i++) {
        vectors[0].push({
            file: String.fromCharCode(cFile - i),
            rank: String.fromCharCode(cRank - i)
        });
        vectors[1].push({
            file: String.fromCharCode(cFile + i),
            rank: String.fromCharCode(cRank + i)
        });
        vectors[2].push({
            file: String.fromCharCode(cFile - i),
            rank: String.fromCharCode(cRank + i)
        });
        vectors[3].push({
            file: String.fromCharCode(cFile + i),
            rank: String.fromCharCode(cRank - i)
        });
    }

    const moves = Array.prototype.concat(...vectors)
    return moves;
}
```

Tel qu'il était, il n'y avait aucun intérêt à faire cela. Mais plus tard, ces vecteurs auraient été utiles pour tronquer les mouvements le long des diagonales (ou des rangées ou des fichiers) lorsqu'une pièce amie est sur le chemin. Au lieu de cela, j'ai dû décomposer la liste des mouvements le long des vecteurs dans les services en amont — plus de travail et d'inefficacité, comme vous le verrez plus tard.

Le vrai défaut, cependant, était que j'ai retourné un tableau, plutôt qu'un objet de données. Les objets de données ont des propriétés qui sont extensibles, ce qui n'est pas le cas des tableaux. En conséquence, tous mes services en amont dépendent de la réception d'un tableau de mouvements, et **uniquement** d'un tableau de mouvements. Aucune flexibilité. Je ne peux pas maintenant ajouter une liste de vecteurs de mouvement **en plus** d'une liste de mouvements. Mais j'aurais pu si j'avais retourné un objet de cette méthode et du service qui l'a appelée.

Leçon apprise ? Envisagez de retourner des objets de données de vos services. Faites en sorte que vos services en amont travaillent sur des parties des données, mais transmettent toutes les données qu'ils reçoivent en amont. Les exceptions à cette règle seront nombreuses, bien sûr.

### Avec des amis comme ceux-ci...

Dans la Partie 1, il y avait un service sous le motif :

`role:"movement",cmd:"legalSquares"`

Il retournait tous les mouvements d'une pièce non entravée. Puisque ce sera le service de base pour déterminer les mouvements légaux sur un échiquier peuplé, je vais renommer le `cmd` en `legalMoves`. Maintenant, je veux étendre cela pour prendre en compte les pièces amies qui pourraient bloquer un chemin de ma pièce choisie.

#### Le service étendu

Le service qui étend `role:"movement",cmd:"legalMoves"` est... `role:"movement",cmd:"legalMoves"` !

Oui, il a le même motif de service que le service qu'il appelle. Vous vous souvenez peut-être que les services sont identifiés par motif, alors comment cela va-t-il fonctionner ? Lorsque le programme agit sur `role:"movement",cmd:"legalMoves"`, il utilisera le service défini le plus récemment. Mais le nouveau service doit appeler l'ancien service `legalMoves`. Cela peut être résolu facilement :

```js
this.add({
        role: "movement",
        cmd: "legalMoves"
    }, (msg, reply) => {//retourne les mouvements non entravés}
    
this.add('role:movement,cmd:legalMoves', function (msg, reply) {
        this.
prior(msg, function (err, moves) {
            if (msg.board) {
                const boardMoves = legalMovesWithBoard(msg, moves);
                reply(err, boardMoves);
                return;
            }
            reply(err, moves);
        });
    });
```

Ce nouveau service est capable d'appeler l'ancien service en utilisant la méthode `prior()` dans Seneca. Si aucun paramètre `board` n'est fourni dans l'objet `msg` entrant, alors ce service agira simplement comme un passe-plat vers l'ancien service. Mais que se passe-t-il s'il y a un échiquier ?

Je ne vais pas montrer une liste de code complète ici (voir le lien ci-dessous), mais l'essentiel est :

```js
module.exports = function (msg, moves) {
    if (!msg.board) return moves;
    
const blockers = moves.filter(m => {
        return (msg.board.pieceAt(m))
    })
    
var newMoves = [];
    const pp = msg.piece.position;
    
const rangeChecks = {
        B: diagonalChecks,
        R: rankAndFileChecks,
        K: panopticonChecks,
        Q: panopticonChecks,
        P: pawnChecks,
        N: knightChecks
    };
    
var rangeCheck = rangeChecks[msg.piece.piece];
    // console.error(msg.piece.piece, rangeCheck.name)
    newMoves = moves.filter(m => {
        return rangeCheck(m, blockers, pp);
    })
    return newMoves;
}
```

Vous vous souvenez de notre vieil ami `diagonalMoves` du service `rawMoves` ? Afin de faire une vérification de portée sur les diagonales sans vecteurs pratiques, le nouveau service `legalMoves` appelle ceci :

```js
// m: mouvement proposé
// blockers: pièces bloquantes
// pp: position actuelle de la pièce
function diagonalChecks(m, blockers, pp) {
    let isGood = true;
for (const b of blockers) {
        if (b.rank > pp.rank && b.file > pp.file) {
            if (m.rank > pp.rank && m.file > pp.file) {
                isGood = isGood && (m.rank < b.rank && m.file < b.file);
            }
        }
        if (b.rank > pp.rank && b.file < pp.file) {
            if (m.rank > pp.rank && m.file < pp.file) {
                isGood = isGood && (m.rank < b.rank && m.file > b.file)
            }
        }
        if (b.rank < pp.rank && b.file > pp.file) {
            if (m.rank < pp.rank && m.file > pp.file) {
                isGood = isGood && (m.rank > b.rank && m.file < b.file)
            }
        }
        if (b.rank < pp.rank && b.file < pp.file) {
            if (m.rank < pp.rank && m.file < pp.file) {
                isGood = isGood && (m.rank > b.rank && m.file > b.file)
            }
        }
    }
return isGood;
}
```

Moche, n'est-ce pas ? Je serais heureux qu'un lecteur enclin à l'algorithme réduise cela à deux lignes dans la section des commentaires. Trois, même.

Cela prend donc en charge les pièces amies. La prochaine partie traitera des pièces hostiles, qui peuvent être capturées.

Le code source complet de cet article peut être trouvé sur [GitHub](https://github.com/JeffML/ms-chess2).