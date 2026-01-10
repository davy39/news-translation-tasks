---
title: Écrire un microservice d'échecs en utilisant Node.js et Seneca, Partie 1
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
seo_title: Écrire un microservice d'échecs en utilisant Node.js et Seneca, Partie
  1
seo_desc: 'By Jeff M Lowery

  (This is Part 1 of a three-part series [Part 2, Part 3])

  I’ve begun wrapping my head around microservices. Up to this time I regarded it
  as a scalability pattern and overlooked the functional programming principles behind
  it.

  The rul...'
---

Par Jeff M Lowery

(Ceci est la Partie 1 d'une série en trois parties [[Partie 2](https://medium.com/@jefflowery/follow-the-rules-with-seneca-ii-c22074debac), [Partie 3](https://medium.com/@jefflowery/writing-a-chess-microservice-using-node-js-and-seneca-part-3-ab38b8ef9b0a)])

J'ai commencé à comprendre les microservices. Jusqu'à présent, je les considérais comme un modèle de scalabilité et je négligeais les principes de programmation fonctionnelle qui les sous-tendent.

Les [règles des échecs](https://www.chess.com/learn-how-to-play-chess) peuvent être facilement décomposées en microservices. Elles ne sont ni aléatoires ni ambiguës, ce qui est parfait pour écrire de petits services sans état qui traitent des mouvements de diverses pièces.

Dans cet article, je vais passer en revue plusieurs services que j'ai créés pour déterminer quels sont les mouvements légaux pour des pièces isolées sur un échiquier vide. Nous utiliserons le [Framework Seneca](http://senecajs.org/), une boîte à outils de microservices pour Node.js, car il est intuitif et bien documenté.

### Installation de Seneca

[Seneca](http://senecajs.org/getting-started/) est un module Node.js qui s'installe via npm :

`npm install seneca`

De plus, nous allons nous appuyer sur les modules [mocha/chai](http://chaijs.com/api/bdd/) installés globalement pour les tests qui illustreront la fonctionnalité.

### Trouver tous les mouvements légaux

Il n'est en fait pas nécessaire de maintenir une représentation en mémoire d'un échiquier, juste les pièces et leur position sur une grille de coordonnées 8x8. La [notation algébrique](https://en.wikipedia.org/wiki/Algebraic_notation_(chess)) est couramment utilisée pour décrire les coordonnées sur un échiquier, où les colonnes sont désignées par des lettres et les rangées par des nombres :

![Image](https://cdn-media-1.freecodecamp.org/images/1*CIAIhpn7wBT1n15aOw0pkA.gif)
_Vue du côté Blanc de l'échiquier_

Pour le joueur qui est Blanc, le coin inférieur droit est h1 ; pour Noir, c'est a8. Une tour sur b2, se déplaçant vers la case f2, serait désignée comme Tb2-f2.

### Mouvements bruts

Je définis les **mouvements bruts** comme les mouvements qu'une pièce ferait si elle n'était pas entravée par d'autres pièces _ou le bord de l'échiquier_. Ce dernier point peut sembler étrange, mais il me permet de construire un masque de mouvement 15x15, qui est ensuite tronqué pour s'adapter à l'échiquier 8x8. Un certain Procruste a eu une idée similaire il y a des siècles.

Les Rois, Dames, Fous et Tours se déplacent le long des diagonales et/ou des colonnes, donc je vais utiliser un seul service pour les mouvements de ces quatre pièces. Les Pions ont des caractéristiques de mouvement uniques, donc un service spécial sera utilisé pour eux. Il en va de même pour les Cavaliers, car ils peuvent sauter par-dessus les pièces et ne se déplacent pas le long des colonnes ou des rangées.

Par exemple, une tour peut se déplacer de 7 cases le long de n'importe quelle rangée ou colonne sur un échiquier 15x15 dans lequel la tour est centrée. Des règles similaires s'appliquent au fou et à la dame. Le roi est limité à une portée d'une case dans n'importe quelle direction (l'exception est le roque, que je traiterai dans un futur article).

Je vais utiliser une classe `ChessPiece` pour stocker des informations sur le type et la position de chaque pièce d'échecs. Elle ne jouera pas un rôle trop important pour l'instant, mais elle le sera plus tard lorsque j'élargirai la portée des règles couvertes par les services.

### Premier service : Mouvements de la Tour, du Fou, de la Dame et du Roi

Dans Seneca, les services sont invoqués via `role` et `cmd`. Le `role` est similaire à une catégorie, et `cmd` nomme un service spécifique. Comme nous le verrons plus tard, un service peut être davantage spécifié par des paramètres supplémentaires.

Les services sont ajoutés en utilisant `seneca.add()`, et invoqués via `seneca.act()`. Examinons d'abord le service (depuis Movement.js) :

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

Maintenant, voyons comment le test invoque le service (movesTest.js) :

```js
 var Ba1 = new ChessPiece('Ba1');
        seneca.act({
            role: "movement",
            cmd: "rawMoves",
            piece: Ba1
        }, (err, msg) => {...});
```

Notez qu'en plus de `role` et `cmd`, il y a un argument `piece`. Celui-ci, ainsi que le `role` et le `cmd`, sont des propriétés de l'argument `msg` reçu par le service. Avant de pouvoir invoquer le service, cependant, vous devez dire à Seneca quels services utiliser :

```js
var movement = require('../services/Movement')
const seneca = require('seneca')({
        log: 'silent'
    })
   
 .use(movement);
```

Les mouvements bruts pour un fou sur la case a1 sont dans le `msg` reçu _en retour_ du service :

[ { file: '`', rank: '0' },  
 { file: 'b', rank: '2' },  
 { file: '`', rank: '2' },  
 { file: 'b', rank: '0' },  
 { file: '_', rank: '/' },  
 { file: 'c', rank: '3' },  
 { file: '_', rank: '3' },  
 { file: 'c', rank: '/' },  
 { file: '^', rank: '.' },  
 { file: 'd', rank: '4' },  
 { file: '^', rank: '4' },  
 { file: 'd', rank: '.' },  
 { file: ']', rank: '-' },  
 { file: 'e', rank: '5' },  
 { file: ']', rank: '5' },  
 { file: 'e', rank: '-' },  
 { file: '\\', rank: ',' },  
 { file: 'f', rank: '6' },  
 { file: '\\', rank: '6' },  
 { file: 'f', rank: ',' },  
 { file: '[', rank: '+' },  
 { file: 'g', rank: '7' },  
 { file: '[', rank: '7' },  
 { file: 'g', rank: '+' },  
 { file: 'Z', rank: '*' },  
 { file: 'h', rank: '8' },  
 { file: 'Z', rank: '8' },  
 { file: 'h', rank: '*' } ]

Notez qu'il y a quelques cases étranges listées ! Ce sont les positions qui "tombent" hors de l'échiquier 8x8 et qui seront éliminées plus tard par un autre service.

#### Que vient-il de se passer ?

Un service a été défini avec `role="movement"` et `cmd="rawMoves"`. Lorsque `act()` est invoqué plus tard, les paramètres de la demande d'action sont comparés à un service qui gère ces paramètres (cela s'appelle le **modèle** du service). Comme mentionné précédemment et comme cela sera montré dans l'exemple suivant, `role` et `cmd` ne sont pas nécessairement les seuls paramètres qui déterminent le service invoqué.

### **Services suivants : Pions et Cavaliers**

Les Pions se déplacent d'une case vers l'avant, sauf s'ils sont sur leur case d'origine, auquel cas ils peuvent avancer d'une ou deux cases. Il existe d'autres mouvements qu'un pion peut faire lorsqu'il n'est pas la seule pièce sur un échiquier vide, mais cela sera considéré dans le futur. Les Pions commencent toujours sur la deuxième rangée et ne peuvent jamais reculer.

Les Cavaliers se déplacent en forme de L. Sur notre échiquier imaginaire 15x15 avec le cavalier centré, il y aura toujours huit mouvements possibles.

Je vais écrire deux services (un pour les pions, l'autre pour les cavaliers) et les placer tous les deux dans un seul module (SpecialMovements.js) :

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

Voyez les paramètres `isPawn` et `isKnight` dans les services ? Le premier objet passé à Seneca `add()` est appelé le **modèle de service**. Ce qui se passe, c'est que Seneca invoquera le service avec la correspondance de modèle la _plus spécifique_. Afin d'invoquer le bon service, je dois ajouter `isPawn:true` ou `isKnight:true` à la demande d'action :

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

### Mouvements légaux

Notre service de mouvements légaux rudimentaire va simplement filtrer toutes les positions de cases qui ne sont pas sur les colonnes a-h ou les rangées 1-8. Le service de mouvements légaux sera appelé directement avec une instance `ChessPiece` dans le cadre de la charge utile du service. Le service de mouvements légaux invoquera ensuite le service de mouvements bruts pour obtenir le masque de mouvement. Le masque sera tronqué aux bords de l'échiquier, et le résultat sera les positions de cases qui peuvent être jouées légalement.

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

Le service `legalSquares` invoque d'abord le service `rawMoves`. Cela nous donne le masque de mouvement 15x15 pour la pièce passée via le paramètre `msg`. Il est important, cependant, que le bon service soit invoqué en définissant le champ de modèle `isKnight` ou `isPawn` à vrai pour l'une ou l'autre de ces deux pièces... si les deux sont faux, alors le service `rawMoves` "régulier" pour K, Q, B, R sera invoqué.

Une fois les mouvements bruts récupérés, le service `legalSquares` supprime les positions invalides et retourne ce qui reste. Donc si j'invoque le service avec la pièce sur Na1, j'obtiens :

```js
[ { file: 'c', rank: '2' }, { file: 'b', rank: '3' } ]
```

Si, au lieu de cela, je passe Rd4, legalSquares retourne :  
[ { file: 'c', rank: '4' },  
 { file: 'd', rank: '5' },  
 { file: 'e', rank: '4' },  
 { file: 'd', rank: '3' },  
 { file: 'b', rank: '4' },  
 { file: 'd', rank: '6' },  
 { file: 'f', rank: '4' },  
 { file: 'd', rank: '2' },  
 { file: 'a', rank: '4' },  
 { file: 'd', rank: '7' },  
 { file: 'g', rank: '4' },  
 { file: 'd', rank: '1' },  
 { file: 'd', rank: '8' },  
 { file: 'h', rank: '4' } ]

ce qui est un peu plus difficile à déchiffrer, mais contient toutes les colonnes le long de la 4ème rangée et toutes les rangées le long de la colonne d (faites-moi confiance !).

C'est tout pour l'instant ! Dans un futur article, je passerai en revue les services qui traitent des pièces amicales entravant le mouvement, puis je traiterai de la capture potentielle de pièces hostiles. D'autres services géreront les règles pour le roque, la prise en passant, l'échec, l'échec et mat, et la pat.

Tout le code source peut être trouvé [ici](https://github.com/JeffML/ms-chess).

Continuez avec la [Partie 2 de cette série](https://medium.com/@jefflowery/follow-the-rules-with-seneca-ii-c22074debac).