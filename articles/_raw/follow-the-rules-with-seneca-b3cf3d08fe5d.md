---
title: Writing a chess microservice using Node.js and Seneca, Part 1
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-05-29T23:47:32.000Z'
originalURL: https://freecodecamp.org/news/follow-the-rules-with-seneca-b3cf3d08fe5d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*QVKnJrXn5COBq3KjJ1OJvQ.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Microservices
  slug: microservices
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: seneca
  slug: seneca
seo_title: null
seo_desc: 'By Jeff M Lowery

  (This is Part 1 of a three-part series [Part 2, Part 3])

  I’ve begun wrapping my head around microservices. Up to this time I regarded it
  as a scalability pattern and overlooked the functional programming principles behind
  it.

  The rul...'
---

By Jeff M Lowery

(This is Part 1 of a three-part series [[Part 2](https://medium.com/@jefflowery/follow-the-rules-with-seneca-ii-c22074debac), [Part 3](https://medium.com/@jefflowery/writing-a-chess-microservice-using-node-js-and-seneca-part-3-ab38b8ef9b0a)])

I’ve begun wrapping my head around microservices. Up to this time I regarded it as a scalability pattern and overlooked the functional programming principles behind it.

The [rules of chess](https://www.chess.com/learn-how-to-play-chess) can be decomposed easily into microservices. They are neither random nor ambiguous, which is perfect for writing small, stateless services that deal with movements of various pieces.

In this post, I’ll walk through several services I created that determine what the legal moves are for lone pieces on an empty chessboard. We’ll use the [Seneca framework](http://senecajs.org/), a microservices toolkit for Node.js, because it’s intuitive and well documented.

### Setting up Seneca

[Seneca](http://senecajs.org/getting-started/) is a Node.js module that is installed using npm:

`npm install seneca`

Also, we’ll rely on globally installed [mocha/chai](http://chaijs.com/api/bdd/) modules for the tests that will illustrate functionality.

### Find all the legal moves

It’s actually not necessary to maintain an in-memory representation of a chessboard, just the pieces and their location on an 8x8 coordinate grid. [Algebraic notation](https://en.wikipedia.org/wiki/Algebraic_notation_(chess)) is commonly used to describe the coordinates on a chessboard, where the files are denoted by letters and the ranks by numbers:

![Image](https://cdn-media-1.freecodecamp.org/images/1*CIAIhpn7wBT1n15aOw0pkA.gif)
_View from White side of board_

For the player who is White, the rightmost bottom corner is h1; for Black it is a8. A rook on b2, moving to square f2, would be denoted as Rb2-f2.

### Raw Moves

I am defining **raw moves** as the moves a piece would make if unimpeded by other pieces _or the edge of the board_. That last bit may seem odd, but it allows me to construct a 15x15 movement mask, which is then truncated to fit the 8x8 board. A fellow named [Procrustes](https://en.wikipedia.org/wiki/Procrustes) came up with a similar idea ages ago.

Kings, Queens, Bishops and Rooks move along diagonals and/or files, so I will use one service for the movements of those four pieces. Pawns have unique movement characteristics, so a special service will be used for them. The same goes for Knights, since they can jump over pieces and don’t move along files or ranks.

For example, a rook can move 7 squares along any rank or file on an 15x15 board in which the rook is centered. Similar rules apply to bishop and queen. The king is limited to a one-square range in any direction(the exception is castling, which I will deal with in a future post).

I will use a `ChessPiece` class to hold information about the type and location of each chess piece. It won’t play too important a role for now, but it will later when I expand the scope of the rules covered by the services.

### First service: Rook, Bishop, Queen and King moves

In Seneca, services are invoked via `role` and `cmd`. The `role` is akin to a category, and `cmd` names a specific service. As we’ll see later, a service can be further specified by additional parameters.

Services are added using `seneca.add()`, and invoked via `seneca.act()`. Let’s look at the service, first (from Movement.js):

```js
 this.add({
        role: "movement",
        cmd: "rawMoves",
    }, (msg, reply) => {
        var err = null;
        var rawMoves = [];

        var pos = msg.piece.position;

        switch (msg.piece.piece) {
        case 'R':
            rawMoves = rankAndFile(pos);
            break;
        case 'B':
            rawMoves = diagonal(pos);
            break;
        case 'Q':
            rawMoves = rankAndFile(pos)
                .concat(diagonal(pos));
            break;
        case 'K':
            rawMoves = rankAndFile(pos, 1)
                .concat(diagonal(pos, 1))
            break;
        default:
            err = "unhandled " + msg.piece;
            break;
        };

        reply(err, rawMoves);
    });
```

Now let’s see how the test invokes the service (movesTest.js):

```js
 var Ba1 = new ChessPiece('Ba1');
        seneca.act({
            role: "movement",
            cmd: "rawMoves",
            piece: Ba1
        }, (err, msg) => {...});
```

Note that in addition to `role` and `cmd`, there is a `piece` argument. This, along with the `role` and `cmd`, are properties of the `msg` argument received by the service. Before you can invoke the service, though, you must tell Seneca which services to use:

```js
var movement = require(‘../services/Movement’)
const seneca = require('seneca')({
        log: 'silent'
    })
   
 .use(movement);
```

The raw moves for a bishop at square a1 are in the `msg` received _back_ from the service:

[ { file: ‘`’, rank: ‘0’ },  
 { file: ‘b’, rank: ‘2’ },  
 { file: ‘`’, rank: ‘2’ },  
 { file: ‘b’, rank: ‘0’ },  
 { file: ‘_’, rank: ‘/’ },  
 { file: ‘c’, rank: ‘3’ },  
 { file: ‘_’, rank: ‘3’ },  
 { file: ‘c’, rank: ‘/’ },  
 { file: ‘^’, rank: ‘.’ },  
 { file: ‘d’, rank: ‘4’ },  
 { file: ‘^’, rank: ‘4’ },  
 { file: ‘d’, rank: ‘.’ },  
 { file: ‘]’, rank: ‘-’ },  
 { file: ‘e’, rank: ‘5’ },  
 { file: ‘]’, rank: ‘5’ },  
 { file: ‘e’, rank: ‘-’ },  
 { file: ‘\\’, rank: ‘,’ },  
 { file: ‘f’, rank: ‘6’ },  
 { file: ‘\\’, rank: ‘6’ },  
 { file: ‘f’, rank: ‘,’ },  
 { file: ‘[‘, rank: ‘+’ },  
 { file: ‘g’, rank: ‘7’ },  
 { file: ‘[‘, rank: ‘7’ },  
 { file: ‘g’, rank: ‘+’ },  
 { file: ‘Z’, rank: ‘*’ },  
 { file: ‘h’, rank: ‘8’ },  
 { file: ‘Z’, rank: ‘8’ },  
 { file: ‘h’, rank: ‘*’ } ]

Note that there are some weird squares listed! These are the positions that “fall off” the 8x8 board and will be eliminated later by another service.

#### What just happened?

A service was defined with `role=”movement”` and `cmd=”rawMoves”`. When `act()` is later invoked, the parameters of the act request are matched against a service that handles those parameters (this is called the service’s **pattern**). As mentioned previously and as will be shown in the next example, `role` and `cmd` are not necessarily the only parameters that determine the service invoked.

### **Next services: Pawns and Knights**

Pawns move one square forward unless they are on their original square, in which case they can move one or two squares forward. There are other moves a pawn can make when it is not the lone piece on an empty board, but that’s for future consideration. Pawns alway start on the second rank, and can never move backwards.

Knights move in an L-shape pattern. In our imaginary 15x15 board with the knight centered, there will always be eight possible moves.

I’ll write two services (one for pawns, the other for knights) and place both in one module (SpecialMovements.js):

```js
module.exports = function specialMovement(options) {
  //...
      this.add({
        role: "movement",
        cmd: "rawMoves",
        isPawn: true
    }, (msg, reply) => {
        if (msg.piece.piece !== 'P') {
            return ("piece was not a pawn")
        }
        
        var pos = msg.piece.position;

        const rawMoves = pawnMoves(pos);
        reply(null, rawMoves);
    });

    this.add({
        role: "movement",
        cmd: "rawMoves",
        isKnight: true
    }, (msg, reply) => {
        if (msg.piece.piece !== 'N') {
            return ("piece was not a knight")
        }

        var rawMoves = [];
        var pos = msg.piece.position;

        rawMoves = knightMoves(pos);
        reply(null, rawMoves);
    });
}
```

See the `isPawn` and `isKnight` parameters in the services? The first object passed to Seneca `add()` is called the **service pattern**. What happens is that Seneca will invoke the service with the _most specific_ pattern match. In order to invoke the right service, I need to add `isPawn:true` or `isKnight:true` to the act request:

```js
var movement = require('../services/Movement')
var specialMovement = require('../services/SpecialMovement')

const seneca = require('seneca')({
        log: 'silent'
    })
    .use(specialMovement)

...

var p = new ChessPiece('Pe2');
        seneca.act({
            role: "movement",
            cmd: "rawMoves",
            piece: p,
...
            
isPawn: true
        }, (err, msg) => {...}
        
...
 var p = new ChessPiece('Nd4');
        seneca.act({
            role: "movement",
            cmd: "rawMoves",
            piece: p,
            
isKnight: true
        }, (err, msg) => {
```

### Legal Moves

Our rudimentary legal move service will just filter out all the square positions that are not on files a-h or ranks 1–8. The legal move service will be called directly with a `ChessPiece` instance as part of the service payload. The legal move service will then invoke the raw move service to get the movement mask. The mask will be truncated to the edges of the board, and the result will be the square positions that can legally be played.

```js
    this.add({
        role: "movement",
        cmd: "legalSquares",
    }, (msg, reply) => {
        const isPawn = msg.piece.piece === 'P';
        const isKnight = msg.piece.piece === 'N';

        this.act({
            role: "movement",
            cmd: "rawMoves",
            piece: msg.piece,
            isPawn: isPawn,
            isKnight: isKnight
        }, (err, msg) => {
            const squared = [];

            msg.forEach((move) => {
                if (move.file >= 'a' && move.file <= 'h') {
                    if (move.rank >= 1 && move.rank <= 8) {
                        squared.push(move)
                    }
                }
            })

            reply(null, squared);
        });
    })
```

The `legalSquares` service first invokes the `rawMoves` service. This gets us the 15x15 movement mask for whatever piece is passed via the `msg` parameter. It is important, though, that the right service is invoked by setting the `isKnight` or `isPawn` pattern field to true for either of those two pieces… if both are false, then the “regular” `rawMoves` service for K,Q,B,R will be invoked.

Once the raw moves are retrieved, then the `legalSquares` service removes the invalid positions and returns what is left. So if I invoke the service with the piece at Na1, I get:

```js
[ { file: ‘c’, rank: ‘2’ }, { file: ‘b’, rank: ‘3’ } ]
```

If instead I pass in Rd4, legalSquares returns:  
[ { file: ‘c’, rank: ‘4’ },  
 { file: ‘d’, rank: ‘5’ },  
 { file: ‘e’, rank: ‘4’ },  
 { file: ‘d’, rank: ‘3’ },  
 { file: ‘b’, rank: ‘4’ },  
 { file: ‘d’, rank: ‘6’ },  
 { file: ‘f’, rank: ‘4’ },  
 { file: ‘d’, rank: ‘2’ },  
 { file: ‘a’, rank: ‘4’ },  
 { file: ‘d’, rank: ‘7’ },  
 { file: ‘g’, rank: ‘4’ },  
 { file: ‘d’, rank: ‘1’ },  
 { file: ‘d’, rank: ‘8’ },  
 { file: ‘h’, rank: ‘4’ } ]

which is a little harder to decipher, but contains all files along the 4th rank and all ranks along the d-file (trust me!).

That’s it for now! In a future post I’ll go over services that deal with friendly pieces impeding movement, then dealing with the potential capture of hostile pieces. Further services will handle rules for castling, _en passant,_ check, checkmate, and stalemate.

All source code can be found [here](https://github.com/JeffML/ms-chess).

Continue to [Part 2 of this series](https://medium.com/@jefflowery/follow-the-rules-with-seneca-ii-c22074debac).

