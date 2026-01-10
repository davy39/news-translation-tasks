---
title: Écrire un microservice d'échecs en utilisant Node.js et Seneca, Partie 3
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-07-17T00:12:35.000Z'
originalURL: https://freecodecamp.org/news/writing-a-chess-microservice-using-node-js-and-seneca-part-3-ab38b8ef9b0a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*brvN_0vi3hLWd3YQvvcJrw.jpeg
tags:
- name: chess
  slug: chess
- name: JavaScript
  slug: javascript
- name: Microservices
  slug: microservices
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: Écrire un microservice d'échecs en utilisant Node.js et Seneca, Partie
  3
seo_desc: 'By Jeff M Lowery

  Finishing up a three-part series on writing a rules engine with Seneca microservices.

  Parts 1 & 2 of this series covered:


  The Seneca microservices Node.js module

  How to write a service, how to identify it by pattern and how to call ...'
---

Par Jeff M Lowery

Fin d'une série en trois parties sur l'écriture d'un moteur de règles avec les microservices Seneca.

Les parties [1](https://medium.freecodecamp.org/follow-the-rules-with-seneca-b3cf3d08fe5d) et [2](https://medium.com/@jefflowery/follow-the-rules-with-seneca-ii-c22074debac) de cette série ont couvert :

* Le module Node.js des microservices Seneca
* Comment écrire un service, comment l'identifier par motif et comment l'appeler
* Comment enchaîner les appels de service
* Comment améliorer un service existant

En cours de route, je me suis demandé ce qu'un service devrait retourner. J'en suis venu à la conclusion que retourner un objet de données (JSON dans ce cas) était le plus flexible. Cela permet aux services d'**embellir** la sortie sans affecter les clients existants du service.

**Embellir ?** Par là, je veux dire que les résultats intermédiaires peuvent être maintenus comme moyen de suivre les informations qui pourraient être utiles plus tard, pour un service pas encore écrit. Dans le cas présent, j'avais un service `rawMoves` qui retournait une liste de mouvements. Cela était immédiatement suffisant pour les clients que j'avais. Le service calculait les mouvements le long des vecteurs de mouvement et les combinait en un tableau unidimensionnel.

![Image](https://cdn-media-1.freecodecamp.org/images/1*BKDwcC-G7LiTG911r56aVQ.gif)
_Vecteurs de mouvement de la Reine_

Plus tard, cependant, j'ai découvert que ces vecteurs de mouvement auraient été utiles lorsqu'un service `legalMoves` écrit plus tard devait prendre en compte les pièces amicales qui bloquaient le mouvement. Les vecteurs auraient simplifié et rendu ces calculs plus efficaces, mais ils étaient « jetés » par le service `rawMoves`.

Pour revenir en arrière et ajouter les vecteurs (en plus de la liste des mouvements) signifiait changer les clients du service original pour accepter un objet, et non un tableau. Il est vrai que j'aurais pu rendre le service original stateful, mais cela aurait été excessif. J'avais un choix : refactoriser le service et ses clients, ou **Deal with It™️**. Dans la Partie 2, j'ai choisi cette dernière option.

Pourtant, dans cet épisode, il est temps de refactoriser. `rawMoves` retourne maintenant `{moves, moveVectors}`, et les clients en amont du service peuvent choisir à quoi prêter attention. Il faut cependant veiller à ce que `moves` et `moveVectors` soient toujours synchronisés.

Voyons quel est l'avantage. Dans le code original, trouver `legalMoves` était un processus complexe si l'on ne disposait que d'une pièce, d'une liste de mouvements et de pièces amicales ailleurs sur l'échiquier ([exemple](https://github.com/JeffML/ms-chess2a/blob/master/services/helpers/legalMovesWithBoard.js)). Comparez ce code à celui qui utilise `moveVectors` :

```js
module.exports = function (boardAndPiece, candidateMoves) {
    if (!boardAndPiece.board) return candidateMoves;

    const rangeChecks = {
        B: vectorChecks,
        R: vectorChecks,
        K: vectorChecks,
        Q: vectorChecks,
        P: pawnChecks,
        N: knightChecks
    };

    var rangeCheck = rangeChecks[boardAndPiece.piece.piece];
    return rangeCheck(boardAndPiece, candidateMoves)
}

//...

function vectorChecks(boardAndPiece, candidateMoves) {
    for (const [j, v] of candidateMoves.moveVectors.entries()) {
        for (const [i, m] of v.entries()) {
            const p = boardAndPiece.board.pieceAt(m);
            if (p) {
                if (p.color === boardAndPiece.piece.color) {
                    candidateMoves.moveVectors[j] = v.slice(0, i);
                    break;
                } else {
                    candidateMoves.moveVectors[j] = v.slice(0, i + 1);
                    Object.assign(candidateMoves.moveVectors[j].slice(-1)[0], {
                        hasCaptured: p
                    })
                    break;
                }
            }
        }
    }

    return {
        moveVectors: candidateMoves.moveVectors,
        moves: Array.prototype.concat(...candidateMoves.moveVectors)
    }
}
```

Beaucoup, beaucoup plus simple... et plus efficace. La fonction d'enveloppement est exportée et utilisée par le service `legalMoves` [service](https://github.com/JeffML/ms-chess3/blob/master/services/Movement.js).

```js
const legalMovesWithBoard = require("./helpers/legalMovesWithBoard")
//...
    this.add('role:movement,cmd:legalMoves', function (msg, reply) {
        this.prior(msg, function (err, result) {
            if (msg.board) {
                const result2 = legalMovesWithBoard(msg, result);
         
    //...
```

### Retour au jeu

#### Aperçu du service

Toutes les demandes de mouvement sont gérées par le service `legalMoves`, qui s'appuie sur plusieurs autres services et méthodes d'assistance :

* Appeler le service `rawMoves`
Cela retournera tous les mouvements d'une pièce seule sur un échiquier virtuel de 15x15 (appelé **masque de mouvement**). Expliqué dans la Partie 1
* Appeler le service de base `legalMoves`
Cela découpera le **masque de mouvement** au bord de l'échiquier « réel » de 8x8, avec les coordonnées algébriques appropriées ([notation algébrique](https://en.wikipedia.org/wiki/Algebraic_notation_%28chess%29)). Expliqué dans la Partie 2
* Appeler le service de substitution `legalMoves`
Si un échiquier fait partie du message entrant (le motif du service), une série de vérifications est effectuée pour tenir compte de la présence de pièces amicales et opposées, car celles-ci affecteront le mouvement. Expliqué dans cette partie (Partie 3).

Ainsi, la [Partie 2](https://medium.com/@jefflowery/follow-the-rules-with-seneca-ii-c22074debac) a pris en charge les pièces amicales bloquant d'autres pièces amicales, mais il y a maintenant ces pièces ennemies ennuyeuses à gérer. Comme les pièces amicales, les pièces ennemies peuvent bloquer le mouvement, mais elles peuvent aussi être capturées. Dans certaines conditions, les pièces ennemies peuvent même augmenter nos options de mouvement.

Ensuite, il y a le roque : le seul mouvement où deux pièces peuvent changer de position en même temps. Des considérations spéciales s'appliquent, certaines impliquant des pièces ennemies.

#### Reine, Tour et Fou

Les nouvelles règles impliquant les pièces ennemies étendent ou modifient le service `legalMoves` original de la Partie 2 qui ne traitait que des pièces amicales. La nouvelle extension de microservice devra savoir si la pièce bloquante est amie ou ennemie. Si elle est amie, le mouvement est bloqué à la case précédente. Si elle est ennemie, le mouvement est bloqué par la case de la pièce opposée (par capture). Dans la liste des mouvements légaux retournés par une pièce, nous désignerons les captures en définissant un indicateur `hasCaptured`, ainsi que le type de pièce ennemie à capturer.

![Image](https://cdn-media-1.freecodecamp.org/images/1*HbU0Bv04ybhZe0LxCR_O6Q.png)
_La Reine peut aller à f3, mais pas à g4 ; elle peut aller à d3 et c4 (par capture)_

La méthode d'assistance `vectorChecks` présentée dans la liste précédente gère tous les mouvements basés sur des vecteurs pour la Reine, la Tour et le Fou.

#### Cavalier

Les Cavaliers sautent autour de l'échiquier et ne sont donc bloqués que par des pièces amicales qui se trouvent sur l'une de leurs cases d'atterrissage potentielles. Une pièce ennemie ne bloque pas, mais serait capturée si un Cavalier atterrissait dessus. La méthode utilisée par le service `legalMoves` est facile à écrire.

```js
function knightChecks(boardAndPiece, candidateMoves) {
    const newMoves = [];

    for (const m of candidateMoves.moves) {
        const p = boardAndPiece.board.pieceAt(m)
        if (!p) {
            newMoves.push(m)
        } else if (p.color !== boardAndPiece.piece.color) {
            m.hasCaptured = p;
            newMoves.push(m)
        }
    }
    return {
        moves: newMoves,
        moveVectors: [newMoves]
    };
}
```

#### Pion

Les Pions semblent à première vue être un cas assez simple. Le pion est bloqué si une pièce, qu'elle soit amie ou ennemie, se trouve devant lui. Mais il peut se déplacer d'une case en diagonale vers l'avant pour capturer un ennemi qui se trouve sur cette case.

![Image](https://cdn-media-1.freecodecamp.org/images/1*T4gv4p2TwUz9e3rLgaDIiA.png)
_Le pion en e4 est bloqué en e5, mais peut capturer en f5_

Il y a aussi la règle de la **prise en passant**, où un pion peut capturer un pion ennemi adjacent qui **vient** de se déplacer de deux cases au tour précédent :

![Image](https://cdn-media-1.freecodecamp.org/images/1*QfWgeV-2-_8tM_IQ9G5bUA.png)
_Le pion noir en e4 peut capturer le pion blanc en d4 en se déplaçant en d3(!)_

Et puis il y a la question de la promotion obligatoire une fois qu'un pion atteint la 8ème rangée. De manière déroutante, cela fait référence à la huitième rangée devant le pion, qui serait la première rangée des coordonnées de l'échiquier si l'on joue avec les Noirs.

Toutes ces considérations font un ensemble de règles assez complexe pour déterminer les options de mouvement du pion. Celles-ci peuvent être [trouvées](https://github.com/JeffML/ms-chess3/blob/master/services/helpers/legalMovesWithBoard.js) dans le [code source](https://github.com/JeffML/ms-chess3) accompagnant sur GitHub.

#### Roi

Le Pion était un peu de travail, mais le Roi encore plus. Il y a plusieurs conditions :

* Une case de mouvement potentiel est-elle contrôlée par une pièce ennemie ?
Éliminez cette option.
* Le roi est-il en échec ?
Si oui, il **doit** se déplacer à ce tour
* S'il est en échec et ne peut pas se sortir de l'échec, partie terminée ! Échec et mat !
* S'il n'est pas en échec, mais qu'il n'y a pas d'autres mouvements légaux par une pièce amicale sur l'échiquier, pat !
* Le Roi peut-il roquer (côté reine ou côté roi) ?
* Roi en échec : Non.
* Roi a déjà bougé : Non.
* Tour a déjà bougé : Non.
* Cases intermédiaires entre K et R occupées : Non.
* Cases intermédiaires vides, mais contrôlées par une pièce ennemie : Non.
* Sinon : Oui.

Ce service, je vais le décomposer en détail. Comme vous vous en souvenez peut-être, le service `legalMoves` est divisé en deux parties. Une partie traite une pièce comme si elle était seule sur l'échiquier. L'autre partie traite des pièces amicales et opposées. Regardons la liste :

```js
    this.add('role:movement,cmd:legalMoves', function (msg, reply) {
        this.prior(msg, function (err, result) {
            if (msg.board) {
                const result2 = legalMovesWithBoard(msg, result);
                if (msg.piece.piece === 'K') {
                    legalMovesWithKing.call(this, msg, result2, reply)
                } else {
                    reply(err, result2);
                }
            } else {
                reply(err, result);
            }
        });
    });
```

Pour chaque pièce sauf le Roi, nous appelons simplement le service de base (via la méthode `prior()` du framework Seneca) suivi de la méthode d'assistance `legalMovesWithBoard()`, dont certaines parties ont été listées dans les extraits précédents de cet article.

Si la pièce est un Roi, la méthode d'assistance supplémentaire `legalMovesWithKing()` est appelée. Les paramètres d'appel sont la référence `this`, un objet `msg` contenant l'échiquier et la pièce déplacée (le Roi), le `result2` qui provient de l'appel au service de base `legalMoves` (celui-ci contient les informations de mouvement), et le callback `reply`.

Il y a un peu de code à parcourir, donc je vais me référer aux sections par numéro de ligne :

```js
module.exports = function (boardAndPiece, candidateMoves, reply) {
    const opposingColor = boardAndPiece.piece.color === 'W' ? 'black' : 'white';

    //temporairement retirer le K pour éviter les cycles
    boardAndPiece.board.removePiece(boardAndPiece.piece);

    function canCastle(king, rook, intervening, opposing) {
        // console.log("canCastle", arguments)

        const opposingControlled = [...opposing.controlled]
        const board = boardAndPiece.board;
        const canCastle = !candidateMoves.inCheck &&
            !king.hasMoved &&
            rook &&
            rook.color === king.color &&
            !rook.hasMoved;
        if (!canCastle) return false;

        const pieceInTheWay = !!intervening.find(sq => board.pieceAt(sq));
        if (pieceInTheWay) return false;

        const passThruCheck = !!intervening.find(sq =>
            opposingControlled.find(opp => (opp.rank === sq.rank && opp.file == sq.file))
        )
        if (passThruCheck) return false;

        return true;
    }

    this.use(require('../SquareControl'))

    this.act({
        role: "board",
        cmd: "squaresControlledBy",
        board: boardAndPiece.board,
        color: opposingColor,
    }, (err, opposing) => {
        if (err) {
            reply(err);
            return;
        }

        const king = boardAndPiece.piece;
        // console.log(opposing.controlled)
        // ajouter le K retiré
        boardAndPiece.board.addPiece(king);
        const filteredMoves = candidateMoves.moves.filter(m =>
            !!!opposing.controlled.find(o => o.rank === m.rank && o.file === m.file)
        )

        const kingSq = king.position;
        const inCheck = !!opposing.controlled.find(o => o.rank === kingSq.rank && o.file === kingSq.file)

        const additional = {}
        additional.inCheck = inCheck;

        additional.checkMated = (inCheck && filteredMoves.length === 0)

        const rank = additional.color === 'W' ? 1 : 8;
        let rook = boardAndPiece.board.pieceAt(`a${rank}`);
        let intervening = [`b${rank}`, `c${rank}`, `d${rank}`]

        additional.canQSideCastle = canCastle(king, rook, intervening, opposing)

        rook = boardAndPiece.board.pieceAt(`h${rank}`);
        intervening = [`f${rank}`, `g${rank}`]

        additional.canKSideCastle = canCastle(king, rook, intervening, opposing)

        candidateMoves.moves = filteredMoves;
        delete candidateMoves.moveVectors; // no longer valid, and no longer needed

        Object.assign(candidateMoves, additional);
        console.log(candidateMoves)
        reply(null, candidateMoves)
    });
};
```

Commençons par le milieu, à la ligne 30. Un service appelé `squaresControlledBy` est importé dans le framework depuis [SquareControl.js](https://gist.github.com/JeffML/a44d20e88767df03581b264e50b5a99d). Il rassemble tous les mouvements légaux du côté opposé et appelle ces cases les cases contrôlées. Nous avons besoin de cette information car le Roi ne peut pas se déplacer sur une case « contrôlée » par l'ennemi. Le Roi ne peut pas se déplacer en échec.

Il y a un point délicat à cela, et c'est parce que le service `squaresControlledBy` s'appuie sur le service `legalMoves`. Ce qui peut se produire est que :

* Le service `legalMoves` est appelé pour une pièce amicale
* Si la pièce amicale est un Roi, `squaresControlledBy` est appelé pour le côté opposé
* `squaresControlledBy` demande `legalMoves` pour toutes les pièces du côté opposé
* Si `legalMoves` est demandé pour le Roi opposé, il appellera le service `squaresControlledBy` pour **son** côté opposé (notre côté).
* Nous avons fait le tour complet, et nous tournons en rond...

Ces cycles sont l'un des pièges des microservices et doivent être soigneusement pris en compte. Je ne vais pas entrer dans les diverses stratégies pour traiter cela, mais Seneca fournit des options de trace pour les actions `( — seneca.print.tree)` et les invocations de service `( — seneca.log.all)` qui peuvent être utiles pour le débogage.

L'astuce que j'ai utilisée pour éviter les cycles sans fin a été de retirer temporairement le roi ami de l'échiquier (ligne 5) et de le remettre plus tard (ligne 46). Je dirais que la meilleure pratique serait de ne pas modifier les données d'action du service entrant. Il y a des effets secondaires potentiels difficiles à suivre. Cependant, pour les besoins de terminer cette série dans un délai raisonnable, je vais passer outre un peu de tricherie.

Nous poussons des informations supplémentaires (`inCheck`, options de roque [lignes 7–28], `checkmate`) à la `reply` en les stockant dans une structure de données locale puis en utilisant `Object.assign()` pour les fusionner dans la structure `candidateMoves`. L'objet `candidateMoves` aura maintenant des mouvements ainsi que de nouvelles propriétés fournies par l'objet supplémentaire (lignes 54–73).

![Image](https://cdn-media-1.freecodecamp.org/images/1*eNTwiOlyhPNvZNyoJ5vgSA.png)
_Le Roi noir ne peut pas roquer car il est en échec ; le Roi blanc ne peut pas roquer à cause du Fou ami intermédiaire (côté roi) et du contrôle opposé de la case d1 (côté reine)_

Cela conclut tout ! N'oubliez pas, si vous avez trouvé cette série utile et engageante, n'oubliez pas de la recommander (cliquez sur cette petite icône de cœur). Les commentaires sont toujours les bienvenus.

Le code source complet (y compris les tests) pour cette Partie 3 de la série peut être trouvé [ici](https://github.com/JeffML/ms-chess3).