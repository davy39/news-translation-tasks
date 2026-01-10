---
title: Instructions Return en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-21T21:42:00.000Z'
originalURL: https://freecodecamp.org/news/javascript-return-statements
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9da5740569d1a4ca38df.jpg
tags:
- name: JavaScript
  slug: javascript
- name: toothbrush
  slug: toothbrush
seo_title: Instructions Return en JavaScript
seo_desc: "Introduction\nWhen a return statement is called in a function, the execution\
  \ of this function is stopped. If specified, a given value is returned to the function\
  \ caller. If the expression is omitted, undefined is returned instead.\n    return\
  \ expressio..."
---

## **Introduction**

Lorsque l'instruction **return** est appelée dans une fonction, l'exécution de cette fonction est arrêtée. Si une valeur est spécifiée, elle est retournée à l'appelant de la fonction. Si l'expression est omise, `undefined` est retourné à la place.

```js
    return expression;
```

Les fonctions peuvent retourner :

* Valeurs primitives (chaîne de caractères, nombre, booléen, etc.)
* Types d'objets (tableaux, objets, fonctions, etc.)

Ne retournez jamais quelque chose sur une nouvelle ligne sans utiliser de parenthèses. C'est une particularité de JavaScript et le résultat sera undefined. Essayez toujours d'utiliser des parenthèses lorsque vous retournez quelque chose sur plusieurs lignes.

```javascript
function foo() {
    return 
      1;
}

function boo() {
    return (
      1
    );
}

foo(); --> undefined
boo(); --> 1
```

## **Exemples**

La fonction suivante retourne le carré de son argument, **x**, où **x** est un nombre.

```js
    function square(x) {
       return x * x;
    }
```

![:rocket:](https://forum.freecodecamp.com/images/emoji/emoji_one/rocket.png?v=2)

[Exécuter le Code](https://repl.it/C7VT/0)

La fonction suivante retourne le produit de ses arguments, **arg1** et **arg2**.

```js
    function myfunction(arg1, arg2){
       var r;
       r = arg1 * arg2;
       return(r);
    }
```

![:rocket:](https://forum.freecodecamp.com/images/emoji/emoji_one/rocket.png?v=2)

[Exécuter le Code](https://repl.it/C7VU/0)

Lorsque une fonction `return` une valeur, cette valeur peut être assignée à une variable en utilisant l'opérateur d'assignation (`=`). Dans l'exemple ci-dessous, la fonction retourne le carré de l'argument. Lorsque la fonction se résout ou se termine, sa valeur est la valeur `return`ée. La valeur est ensuite assignée à la variable `squared2`.

```javascript
    function square(x) {
        return x * x;
    }
    
    let squared2 = square(2); // 4
```

S'il n'y a pas d'instruction return explicite, c'est-à-dire que la fonction manque du mot-clé `return`, la fonction retourne automatiquement `undefined`.

Dans l'exemple suivant, la fonction `square` manque du mot-clé `return`. Lorsque le résultat de l'appel de la fonction est assigné à une variable, la variable a une valeur de `undefined`.

```javascript
    function square(x) {
        let y = x * x;
    }
    
    let squared2 = square(2); // undefined
```

![:rocket:](https://forum.freecodecamp.com/images/emoji/emoji_one/rocket.png?v=2)

[Exécuter le Code](https://repl.it/M8BE)