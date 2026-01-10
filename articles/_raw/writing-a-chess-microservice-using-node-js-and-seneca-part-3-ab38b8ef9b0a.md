---
title: Writing a chess microservice using Node.js and Seneca, Part 3
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
seo_title: null
seo_desc: 'By Jeff M Lowery

  Finishing up a three-part series on writing a rules engine with Seneca microservices.

  Parts 1 & 2 of this series covered:


  The Seneca microservices Node.js module

  How to write a service, how to identify it by pattern and how to call ...'
---

By Jeff M Lowery

Finishing up a three-part series on writing a rules engine with Seneca microservices.

Parts [1](https://medium.freecodecamp.org/follow-the-rules-with-seneca-b3cf3d08fe5d) & [2](https://medium.com/@jefflowery/follow-the-rules-with-seneca-ii-c22074debac) of this series covered:

* The Seneca microservices Node.js module
* How to write a service, how to identify it by pattern and how to call it
* How to string service calls together
* How to enhance an existing service

Along the way, I pondered what a service should return. I came to the conclusion that returning a data object (JSON in this case) was the most flexible. It allows services to **embellish** the output without affecting existing clients of the service.

**Embellish?** By that I mean intermediate results can be maintained as a means of tracking information that might be useful later, to a service not yet written. In the present case, I had a `rawMoves` service that returned a list of moves. That was immediately sufficient for the clients I had. The service calculated moves along movement vectors, and combined them into a 1-dimensional array.

![Image](https://cdn-media-1.freecodecamp.org/images/1*BKDwcC-G7LiTG911r56aVQ.gif)
_Queen movement vectors_

Later though, I discovered that those movement vectors would have come in handy when a `legalMoves` service written later needed to take into account friendly pieces that were blocking movement. Vectors would have made those calculations simpler and more efficient, but they were “tossed out” by the `rawMoves` service.

To go back and add the vectors (in addition to the move list) meant changing the clients of the original service to accept an object, not an array. True, I could have made the original service stateful, but that would have been overkill. I had a choice: refactor the service and its clients, or **Deal with It™️**. In Part 2, I chose the latter.

Yet in this installment, time has come to refactor. `rawMoves` now returns `{moves, moveVectors}`, and the upstream clients of the service can choose what to pay attention to. Care has to be taken, though, that `moves` and `moveVectors` are in sync at all times.

Let’s see what the advantage is. In the original code, finding `legalMoves` was an involved process if given just a piece, move list, and friendly pieces elsewhere on the board ([example)](https://github.com/JeffML/ms-chess2a/blob/master/services/helpers/legalMovesWithBoard.js). Compare that code to one that uses `moveVectors`:

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

Much, much simpler…and more efficient. The wrapping function is exported and used by the `legalMoves` [service](https://github.com/JeffML/ms-chess3/blob/master/services/Movement.js).

```js
const legalMovesWithBoard = require("./helpers/legalMovesWithBoard")
//...
    this.add('role:movement,cmd:legalMoves', function (msg, reply) {
        this.prior(msg, function (err, result) {
            if (msg.board) {
                const result2 = legalMovesWithBoard(msg, result);
         
    //...
```

### Back to the Game

#### Service Overview

All movement requests are handled by the `legalMoves` service, which relies on several other services and helper methods:

* Call the `rawMoves` service   
This will return all moves of a lone piece on a virtual 15x15 chessboard (referred to as the **movement mask**). Explained in Part 1
* Call the base `legalMoves` service   
This will clip the **movement mask** at the edge of the “real” 8x8 board, with proper [algebraic coordinates](https://en.wikipedia.org/wiki/Algebraic_notation_%28chess%29). Explained in Part 2
* Call the overriding `legalMoves` service  
If there is a board as part of the incoming message (the service pattern), then a series of checks is done to account for the presence of friendly and opposing pieces, because these will affect movement. Explained in this part (Part 3).

So [Part 2](https://medium.com/@jefflowery/follow-the-rules-with-seneca-ii-c22074debac) took care of friendly pieces blocking other friendly pieces, but now there are those annoying enemy pieces to deal with. Like friendly pieces, enemy pieces can block movement, but they can also be captured. Under some conditions, enemy pieces may even increase our movement options.

Then there’s castling: the only move where two pieces can shift their position at once. Special considerations apply, some of which involve enemy pieces.

#### Queen, Rook, & Bishop

The new rules involving enemy pieces extend or modify the original `legalMoves` service in Part 2 that dealt with friendly pieces only. The new microservice extension will need to know if the blocking piece is friend or foe. If friend, then movement is blocked at the square before. If foe, then movement is blocked by the square of the opposing piece (by capture). In the list of legal moves returned by a piece, we will denote captures by setting a `hasCaptured` flag, along with the type of enemy piece to be captured.

![Image](https://cdn-media-1.freecodecamp.org/images/1*HbU0Bv04ybhZe0LxCR_O6Q.png)
_The Queen can go to f3, but not g4; it can go to d3 and c4 (by capture)_

The `vectorChecks` helper method shown in the previous gist listing handles all vector-based movement for Queen, Rook, and Bishop.

#### Knight

Knights jump around the board, so are only blocked by friendly pieces that are on one of its potential landing squares. An enemy piece does not block, but would be captured if a Knight landed on it. The method used by the `legalMoves` service is easy to write.

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

#### Pawn

Pawns at first seem like a pretty simple case. The pawn is blocked if any piece whether friend or enemy stands in front of it. But it can to move one square diagonally forward to capture an enemy that sits in that square.

![Image](https://cdn-media-1.freecodecamp.org/images/1*T4gv4p2TwUz9e3rLgaDIiA.png)
_The pawn at e4 is blocked at e5, but can capture at f5_

There is also the **en passant** rule, where a pawn can capture an adjacent enemy pawn that **just** moved two squares on the previous turn:

![Image](https://cdn-media-1.freecodecamp.org/images/1*QfWgeV-2-_8tM_IQ9G5bUA.png)
_The Black pawn at e4 can capture the White pawn at d4 by moving to d3(!)_

And then there’s the issue of mandatory promotion once a pawn reaches the 8th rank. Confusingly, this refers to the eighth rank in front of the pawn, which would be the first rank of the board coordinates if playing Black.

All these considerations make for a rather involved set of rules to determine the pawn’s movement options. These can be [found](https://github.com/JeffML/ms-chess3/blob/master/services/helpers/legalMovesWithBoard.js) in the accompanying [source code](https://github.com/JeffML/ms-chess3) at GitHub.

#### King

The Pawn was a bit of work, but the king even more so. There are several conditions:

* Is a potential move square controlled by an enemy piece?   
Eliminate that option.
* Is the king in check?   
If so, it **must** move this turn  
* If it is in check, and can’t move out of check, game over! Checkmate!  
* If it is not in check, but there are no other legal moves by any friendly piece on the board, stalemate!
* Can the King castle (queen side or king side)?  
* King is in check: No.  
* King has previously moved: No.  
* Rook has previously moved: No.  
* Intervening squares between K and R occupied: No.  
* Intervening squares empty, but controlled by enemy piece: No.  
* Otherwise: Yes.

This service I will break down into detail. As you may recall, the `legalMoves` service is broken into two parts. One part treats a piece as if it is alone on the board. The other part deals with friendly and opposing pieces. Let’s look at the listing:

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

For every piece but the King, we simply call the base service (via the Seneca framework’s `prior()` method) followed by the helper method `legalMovesWithBoard()`, parts of which were listed in the previous gists of this post.

If the piece is a King, the additional helper method `legalMovesWithKing()` is called. The calling parameters are the `this` reference, a `msg` object containing board and the piece being moved (the King), the `result2` which was came from the base `legalMoves` service call (this contains movement info), and the `reply` callback.

There’s a bit of code to slog through, so I will refer to sections by line number:

```js
module.exports = function (boardAndPiece, candidateMoves, reply) {
    const opposingColor = boardAndPiece.piece.color === 'W' ? 'black' : 'white';

    //temporarily remove the K to avoid cycles
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
        // add the removed K back in
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

Let start from the middle, at line 30. A service called `squaresControlledBy` is imported into the framework from [SquareControl.js](https://gist.github.com/JeffML/a44d20e88767df03581b264e50b5a99d). It gathers all legal moves of the opposing side and calls those the controlled squares. We need this information because the King cannot move into a square ‘controlled’ by the enemy. The King cannot move into check.

There’s a tricky bit to this, and that is because the `squaresControlledBy` service relies on the `legalMoves` service. What can happen is that:

* `legalMoves` service is called for friendly piece
* if the friendly piece is a King, `squaresControlledBy` is called for opposing side
* `squaresControlledBy` requests `legalMoves` for all opposing sides pieces
* if `legalMoves` is requested for the opposing King, it will call service `squaresControlledBy` for **its** opposing side (our side).
* we’ve come full circle, and round and round we go…

These cycles are one of the gotchas of microservices, and have to be carefully accounted for. I won’t go into the various strategies for dealing with this, but Seneca provides trace options for actions `( — seneca.print.tree)`and service invocations `( — seneca.log.all)` that can be helpful in debugging.

The trick I used to avoid endless cycling was to temporarily remove the friendly king from the board (line 5) and later add it back in (line 46). I would say that best practice would be to not modify incoming service action data. There are potential hard-to-track side-effects. For purposes of finishing this series in a reasonable time frame, though, I will overlook a bit of fudging.

We push additional information (`inCheck`, castle options [lines 7–28], `checkmate`) to the `reply` by storing it in a local data structure and then using `Object.assign()` to merge it into the `candidateMoves` structure. The `candidateMoves` object will now have moves long with new properties provided by the additional object (lines 54–73).

![Image](https://cdn-media-1.freecodecamp.org/images/1*eNTwiOlyhPNvZNyoJ5vgSA.png)
_Black King can’t castle because it’s in check; White King can’t castle because of intervening friendly Bishop (kingside) and opposing control of d1 square (queenside)_

That wraps it up! Remember, if you found this series useful and engaging, please don’t forget to recommend it (click that little heart icon). Feedback always welcome.

Full source (including tests) for this Part 3 of the series can be found [here](https://github.com/JeffML/ms-chess3).

