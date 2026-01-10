---
title: Générateurs récursifs et comment ne pas épuiser toute votre mémoire en les
  utilisant
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-02-07T17:07:44.000Z'
originalURL: https://freecodecamp.org/news/recursive-generator-f8bc30e5e412
coverImage: https://cdn-media-1.freecodecamp.org/images/1*pfeC96_K9bAt1CSAfKC-IA.jpeg
tags:
- name: algorithms
  slug: algorithms
- name: Computer Science
  slug: computer-science
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
seo_title: Générateurs récursifs et comment ne pas épuiser toute votre mémoire en
  les utilisant
seo_desc: 'By Jeff M Lowery

  A short while back I wrote a post touching upon combinatorics. Part of the code
  of that article used a Combinator object, which generated combinations of choices
  and stored them in an array.

  The problem with combinatorial operations ...'
---

Par Jeff M Lowery

Il y a peu de temps, [j'ai écrit un article](https://medium.com/@jefflowery/combinatorics-handle-with-care-ed808b48e5dd#.2nv74yf0c) abordant la combinatoire. Une partie du code de cet article utilisait un objet [Combinator](https://gist.github.com/JeffML/0cee0d09d32347ea95e0f9cb4f851cd8), qui générait des combinaisons de choix et les stockait dans un tableau.

Le problème avec les opérations combinatoires est que le nombre de combinaisons [peut croître de manière explosive](https://en.wikipedia.org/wiki/Combinatorial_explosion) avec chaque choix supplémentaire ajouté — plus vite qu'exponentiellement, dans certains cas.

Si j'ai trois éléments et que je permets 0, 1, 2 ou 3 de ceux-ci d'être choisis, j'obtiens 8 choix uniques si je **néglige l'ordre, n'autorise pas de répétitions et inclut l'ensemble nul**. Doublez cela à six éléments et vous obtenez 64 choix (8*8). Doublez cela à nouveau (12 éléments), il y a 4096 choix (64*64). Dans ce cas, avec les restrictions notées ci-dessus, le nombre de combinaisons est 2 à la puissance n choix, donc il croît de manière simplement(!) exponentielle.

Pour un grand nombre d'éléments, stocker chaque combinaison dans un tableau pourrait conduire à l'épuisement de la mémoire. Au lieu de faire retourner au Combinator un tableau uniquement après que toutes les combinaisons ont été générées, que se passerait-il s'il retournait chaque combo un par un, selon les besoins ? Puisque le Combinator est en train de _générer_ des combinaisons, peut-il être converti en un [générateur](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function*) ?

### Combinator.js original

Dans le code original, chaque combinaison créée en appelant **combine()** est stockée dans un tableau **combinations** :

```js
var Combinator = function (opts) {
    var combinations = [];

    function combine(current, remainder) {
        if (remainder.length === 0) {
            if (current.length >= (opts.min || 0) &&
                current.length <= (opts.max || current.length))
                combinations.push(current);
        } else {
            combine(current.concat(remainder[0]), remainder.slice(1, remainder.length));
            combine(current, remainder.slice(1, remainder.length));
        }
        return this;
    }
    return {
        combinations: combinations,
        combine: combine
    }
}

module.exports = Combinator;
```

L'algorithme est un peu embelli avec l'ajout d'options min/max — celles-ci limitent le nombre de combinaisons qui contiennent au moins **min**, et au plus **max**, éléments. Il peut être utilisé comme suit :

```js
var menu = {
   threeItems: {
        min: 0,
        max: 3,
        values: [1, 2, 3]
    }
}

var threeCombos = new Combinator({
            min: menu.threeItems.min,
            max: menu.threeItems.max
        })
        .combine([], menu.threeItems.values)
        .combinations;
```

La propriété **menu.threeItems.values** a (surprise !) trois valeurs. Les propriétés **min** et **max** déterminent l'ensemble des combinaisons à générer. Dans ce cas, nous demandons des ensembles de longueur 0 (l'ensemble nul) à longueur complète (l'ensemble complet des valeurs). Rappelez-vous que nous ne nous intéressons pas à l'ordre, ni ne permettons les doublons. Voyons cela en action :

```js
console.log('threeCombos.length =', threeCombos.length, threeCombos);

-- sortie --

threeCombos.length = 8 [ [ 1, 2, 3 ], [ 1, 2 ], [ 1, 3 ], [ 1 ], [ 2, 3 ], [ 2 ], [ 3 ], [] ]
```

Maintenant, au lieu d'utiliser un tableau pour stocker toutes les combinaisons, convertissons ce bout de JavaScript pour utiliser la nouvelle fonctionnalité de générateur ES6. Un générateur est une fonction étatique qui produit des valeurs une par une, de manière itérative.

### Tentative naïve

Une fonction génératrice est déclarée en utilisant **function*** au lieu de **function**. L'opérateur **yield** est appelé dans la fonction génératrice pour retourner des valeurs uniques à l'appelant. Le générateur se souvient de l'état de l'appel précédent, donc les **yield** suivants retourneront la valeur logique suivante. L'appelant utilise la méthode **next()** pour obtenir chaque valeur suivante de la fonction génératrice. Pas besoin de tableaux !

![Image](https://cdn-media-1.freecodecamp.org/images/1*TEk49bwXt313Cj-_aCL4Bg.jpeg)

Je peux être assez paresseux parfois, donc j'ai pris l'approche tl;dr de la [documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function*) sur les générateurs et je me suis lancé. La première tentative était :

```js
var CombinatorGenerator = function (opts) {
    function* combine(current, remainder) {
        if (remainder.length === 0) {
            if (current.length >= (opts.min || 0) &&
                current.length <= (opts.max || current.length)) {
                yield(current);
            }
        } else {
            combine(current.concat(remainder[0]), remainder.slice(1, remainder.length))
            combine(current, remainder.slice(1, remainder.length))
        }
    }
    return {
        combine: combine
    }
}
```

Cela a du sens, non ? Au lieu de pousser un ensemble de choix vers un tableau, je me contente de produire une valeur. Dans le code client, je continue à appeler next() jusqu'à ce que le générateur me dise qu'il a terminé.

```js
var menu = require('./menu');
var Combinator = require('./Combinator-generator-naive');

function run() {
    var threeCombos = new Combinator({
            min: menu.threeItems.min,
            max: menu.threeItems.max
        })
        .combine([], menu.threeItems.values);

    for (;;) {
        var it = threeCombos.next();
        if (it.done) {
            console.log("terminé !")
            break;
        }
        console.log("choix", it.value);
    }
}

run();
```

Hélas, mes espoirs ont été déçus. La sortie est :

```
PS C:\Users\Jeff\workspace\Generator> node .\test-generated.js

terminé !
```

D'accord, donc évidemment le nouveau Combinator retourne avant que le premier yield ne se produise, donc nous sommes "terminés !" avant d'avoir vraiment terminé.

### Tentative intuitive

Toujours réticent à lire la documentation, j'essaie ensuite de deviner la correction du bug. Alors, que se passe-t-il si je me contente de produire à partir des appels internes **combine** — logique, non ? Au lieu de :

```js
} else {
            combine(current.concat(remainder[0]), remainder.slice(1, remainder.length))
            combine(current, remainder.slice(1, remainder.length))
        }
```

J'essaie de produire à partir des appels récursifs :

```js
} else {
   yield combine(current.concat(remainder[0]), remainder.slice(1, remainder.length)).next()
   yield combine(current, remainder.slice(1, remainder.length)).next()
}
```

En vérité, cela fonctionnera. Alors, exécutons-le :

```bash
PS C:\Users\Jeff\workspace\Generator> node .\generated.js
choice { value: { value: { value: [Object], done: false }, done: false },
  done: false }
choice { value: { value: { value: [Object], done: false }, done: false },
  done: false }
terminé !
```

Hmmm… ce n'est pas bon — ce qui est retourné sont les états des générateurs récursifs, mais pas les valeurs réelles des opérations **yield**.

### Tentative réfléchie

D'accord, il est temps de se mettre au travail. Une petite recherche sur "recursive generator" révèle une référence au **yield from** de Python. Cette syntaxe délègue les appels yield à un autre générateur. Y a-t-il un équivalent en JavaScript ?

Oui ! — et c'est la syntaxe **yield***. Cela est en fait dans le lien de documentation sur les [générateurs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function*) ; si je l'avais lu, j'aurais peut-être compris cela plus tôt (la paresse, comme le crime, ne [paie] pas toujours). La syntaxe correcte est :

```js
} else {
            yield* combine(current.concat(remainder[0]), remainder.slice(1, remainder.length))
            yield* combine(current, remainder.slice(1, remainder.length))
        }
```

Et maintenant, lorsque j'appelle la méthode **combine**, je vois :

```
node .\generated.js
choice [ 1, 2, 3 ]
choice [ 1, 2 ]
choice [ 1, 3 ]
choice [ 1 ]
choice [ 2, 3 ]
choice [ 2 ]
choice [ 3 ]
choice []
terminé !
```

Bien ! Je récupère toutes les combinaisons, une par une. Succès !

Le code complet utilisé dans cet article peut être trouvé [ici](https://github.com/JeffML/Generator). Bonne génération !

**_Mise à jour 26/02/2017_**

Après avoir lu [cet article](https://medium.com/javascript-scene/7-surprising-things-i-learned-writing-a-fibonacci-generator-4886a5c87710#.qy4p75tvg) par l'infatigable Eric Elliott, j'ai commencé à penser que j'avais échangé un type d'épuisement des ressources (mémoire) contre un autre (pile). Cependant, j'ai exécuté le Combinator avec un tableau d'entrée de longueur 30 et il a fonctionné jusqu'à la fin : cela fait 2³⁰ combinaisons générées (plus d'un milliard). Notez que l'algorithme

1. n'utilise pas de récursion terminale (ou peut-être est-ce une récursion "split-tail" ?) ; et
2. **yield ***, selon l'article d'Eric, ne devrait pas être optimisé comme un appel récursif terminal dans tous les cas

Pourtant, cela fonctionne. La preuve peut être trouvée en exécutant generated30.js dans le dépôt git de cet article.