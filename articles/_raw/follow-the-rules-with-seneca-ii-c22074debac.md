---
title: Writing a chess microservice using Node.js and Seneca, Part 2
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
seo_title: null
seo_desc: 'By Jeff M Lowery

  Handling new requirements without refactoring

  Part 1 of this series talked about defining and calling microservices using Seneca.
  A handful of services were created to return all legal moves of a lone chess piece
  on a chessboard. The...'
---

By Jeff M Lowery

#### Handling new requirements without refactoring

[Part 1](https://medium.freecodecamp.com/follow-the-rules-with-seneca-b3cf3d08fe5d) of this series talked about defining and calling microservices using Seneca. A handful of services were created to return all legal moves of a lone chess piece on a chessboard. The series continues in [Part 3](https://medium.com/@jefflowery/writing-a-chess-microservice-using-node-js-and-seneca-part-3-ab38b8ef9b0a).

#### A quick review:

* Seneca services are identified by a pattern consisting of `role` and `cmd` properties. Additional properties can be added to the pattern as well.

```js
this.add({
        role: "movement",
        cmd: "legalMoves"   //, otherProp: value, ...
    }, (msg, reply) => {...}
```

* Services also have an implementation that takes a `msg` object and a reply callback. The`msg` object contains the pattern properties in addition to all other data sent to the service.
* `Seneca.act()`is used to indirectly invoke a service. The `act` method takes an object and a callback function. The object contains the `role`, `cmd`, and other properties that comprise the message to the service.

```js
seneca.act({
            role: "movement",
            cmd: "legalMoves",
            piece: p,
            board: board
        }, (err, msg) => {
```

* When an action could be handled by more than one service that matches the pattern, the service with the [most specific pattern match](http://senecajs.org/getting-started/#how-patterns-work) will be invoked.

There were a handful of services defined in the [first part](https://medium.freecodecamp.com/follow-the-rules-with-seneca-b3cf3d08fe5d) of this series. One of three`rawMoves` services took a piece and its position as parameters and returned 15 x 15 movement mask. These were truncated to an 8 x 8 board using a`legalSquares` service. The result was that the services together can return all the legal moves of any piece on any legal square of the otherwise empty chessboard.

### Microservices and Technical Debt

One of the motivations for microservices is to [reduce technical debt](http://www.infoworld.com/article/2878659/application-development/reducing-technical-debt-with-microservices.html). Every project has deadlines and, as they loom larger, expediency often trumps quality. FIXME and TODO comments litter the source code after a while. Those comments identify technical debt that “someday” will be taken care of.

#### Someday never comes

Microservices focus on functional decomposition and loose coupling. Neither of those are new ideas, but it is a rethinking about how to implement those concepts. A microservice should be small, single-purposed, and extensible. Extending a service can happen with few or no side-effects. A new service can extend an existing service, and neither the old service nor the client that once called it will know the service implementation changed. Less refactoring of classes, methods, method signatures, process flow… all this makes it easier to deal with dreaded TD.

### Back to the game in progress…

Moving a single chess piece around a lonely board is not really all that entertaining. In a real chess game the chessboard is shared with friendly and hostile pieces, and these impact each other’s movement.

Right now I have a`legalSquares` service which can be the basis of a more complete`legalMoves`service. If you recall, the `legalSquares` service would invoke a `rawMoves`service, then remove all the ‘bad’ squares that didn’t belong on a chessboard.

The new `legalMoves` service will take into account other pieces, something that `legalSquares` didn’t. This requires an extra parameter, one called `board`. The `board` is just going to be an array of **ChessPiece** instances, and will assume that the pieces on the board have already been checked for validity. For instance, two pieces don’t occupy the same square, pawns aren’t on the first rank, kings aren’t be next to each other, and so forth.

The following pattern will identify the service:

```js
'role: movement;cmd: legalMoves'
```

This pattern is a stringified version of JSON called **jsonic**; you can use a regular JSON object if you prefer. The message to the service will contain the pattern. It will also contain a ChessPiece instance that has a piece type such as ‘K’ing, ‘Q’ueen, ‘R’ook and board position (see algebraic notation). Later I’ll add to this class a piece color (White or Black) so that the service can tell friend from foe. But for now the service will assume all pieces are friendly.

Since a friendly piece cannot be captured, it will restrict movement of other friendly pieces. Determining those restrictions is a bit of work. I made it harder for myself in the implementation of the `rawMoves` service… which brings me to:

### Microservices are not a Panacea

If you design a service that retrieves or calculates information and **doesn’t** pass that data on up the chain, some service upstream may have to redo that work later. In my example, `rawMoves` returned an array of move objects (file and rank positions on the board). Let’s take the method that generates diagonal moves for a piece using the `rawMoves` service:

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

At first glance, there’s nothing wrong with this. But, those four`move.push` operations actually operate along **movement vectors**. I could have constructed four movement vectors, then returned a list of moves by concatenating them, like so:

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

As it stood, there was no point in doing this. But later on those vectors would have come in handy for truncating movements along diagonals (or ranks or files) when a friendly piece is in the way. Instead, I had to decompose the move list along vectors in services upstream — more work and inefficiency which you will see later.

The real flaw, though, was that I returned an array, rather than a data object. Data objects have properties that are extendable, not so arrays. As a consequence, all my upstream services depend on receiving a movement array, and **only** a movement array. No flexibility. I can’t now add a list of movement vectors **in addition** to a move list. But I could if I had returned an object from this method and the service that called it instead.

Lesson learned? Consider returning data objects from your services. Have your upstream services work on parts of the data, but pass all data they receive back upstream. Exceptions to this rule will abound, of course.

### With Friends like These…

In Part 1, there was a service under the pattern:

`role:"movement",cmd:"legalSquares"`

It returned all moves of an unimpeded piece. Since this will be the base service for determining legal moves on a populated chessboard, I’ll rename the `cmd`to `legalMoves`. Now I want to extend that to take into account friendly pieces that might be blocking a path of my chosen piece.

#### The extended service

The service that extends `role:"movement",cmd:"legalMoves"` is… `role:"movement",cmd:"legalMoves"` !

Yep, it has the same service pattern as the service it calls. You may recall that services are identified by pattern, and so how it this going to work? When the program acts on `role:"movement",cmd:"legalMoves"`, it will use the most recently defined service. But the new service has to call the former`legalMoves` service. That can be solved easily:

```js
this.add({
        role: "movement",
        cmd: "legalMoves"
    }, (msg, reply) => {//returns unimpeded moves}
    
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

This new service is able to call the former service by using the `prior()` method in Seneca. If no `board` parameter is supplied in the incoming `msg` object, then this service will just act as a pass-thru to the former service. But what if there is a board?

I’m not going to show a complete code listing here (see link below), but the gist of it is:

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

Remember our old friend `diagonalMoves` from the `rawMoves` service? In order to do a range check on diagonals without handy vectors, the new `legalMoves` service calls this:

```js
// m: proposed move
// blockers: blocking pieces
// pp: current piece position
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

Ugly, no? I’d be happy if some algorithmically-inclined reader reduced this to two lines in the comments section. Three, even.

So that takes care of friendly pieces. The next installment will deal with hostile pieces, which can be captured.

Full source code for this article can be found at [GitHub](https://github.com/JeffML/ms-chess2).

