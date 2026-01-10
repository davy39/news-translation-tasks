---
title: Var, Let et Const – Quelles sont les différences ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-04-02T14:10:03.000Z'
originalURL: https://freecodecamp.org/news/var-let-and-const-whats-the-difference
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9bd4740569d1a4ca2e24.jpg
tags:
- name: ES6
  slug: es6
- name: frontend
  slug: frontend
- name: JavaScript
  slug: javascript
seo_title: Var, Let et Const – Quelles sont les différences ?
seo_desc: "By Sarah Chima Atuonwu\nA lot of shiny new features came out with ES2015\
  \ (ES6). And now, since it's 2020, it's assumed that a lot of JavaScript developers\
  \ have become familiar with and have started using these features. \nWhile this\
  \ assumption might be..."
---

Par Sarah Chima Atuonwu

Beaucoup de nouvelles fonctionnalités ont été introduites avec ES2015 (ES6). Et maintenant, puisque nous sommes en 2020, il est supposé que de nombreux développeurs JavaScript sont devenus familiers avec ces fonctionnalités et ont commencé à les utiliser. 

Bien que cette supposition puisse être partiellement vraie, il est encore possible que certaines de ces fonctionnalités restent un mystère pour certains développeurs.

L'une des fonctionnalités introduites avec ES6 est l'ajout de `let` et `const`, qui peuvent être utilisés pour la déclaration de variables. La question est, qu'est-ce qui les différencie de l'ancien `var` que nous avons toujours utilisé ? Si vous n'êtes toujours pas clair à ce sujet, alors cet article est pour vous.

Dans cet article, nous discuterons de `var`, `let` et `const` en ce qui concerne leur portée, leur utilisation et leur hoisting. En lisant, notez les différences entre eux que je vais souligner.

### Voici un Scrim interactif sur Var, Let et Const

<iframe src="https://scrimba.com/scrim/coede4c58a4461640298cc925?embed=freecodecamp,mini-header,no-sidebar" width="100%" height="420"></iframe>

## Var

Avant l'arrivée de ES6, les déclarations `var` dominaient. Il y a des problèmes associés aux variables déclarées avec `var`, cependant. C'est pourquoi il était nécessaire que de nouvelles façons de déclarer des variables émergent. D'abord, comprenons mieux `var` avant de discuter de ces problèmes.

### Portée de var

**Portée** signifie essentiellement où ces variables sont disponibles pour être utilisées. Les déclarations `var` sont soit globales, soit de portée fonction/locale. 

La portée est globale lorsqu'une variable `var` est déclarée en dehors d'une fonction. Cela signifie que toute variable déclarée avec `var` en dehors d'un bloc de fonction est disponible pour être utilisée dans toute la fenêtre. 

`var` est de portée fonction lorsqu'elle est déclarée dans une fonction. Cela signifie qu'elle est disponible et peut être accessible uniquement dans cette fonction.

Pour mieux comprendre, regardez l'exemple ci-dessous.

```javascript
    var greeter = "hey hi";
    
    function newFunction() {
        var hello = "hello";
    }

```

Ici, `greeter` est de portée globale car elle existe en dehors d'une fonction, tandis que `hello` est de portée fonction. Nous ne pouvons donc pas accéder à la variable `hello` en dehors de la fonction. Donc si nous faisons ceci :

```javascript
    var tester = "hey hi";
    
    function newFunction() {
        var hello = "hello";
    }
    console.log(hello); // erreur : hello n'est pas défini

```

Nous obtiendrons une erreur qui est le résultat de `hello` n'étant pas disponible en dehors de la fonction.

### Les variables var peuvent être redéclarées et mises à jour

Cela signifie que nous pouvons faire ceci dans la même portée sans obtenir d'erreur.

```javascript
    var greeter = "hey hi";
    var greeter = "say Hello instead";

```

et aussi ceci

```javascript
    var greeter = "hey hi";
    greeter = "say Hello instead";

```

### Hoisting de var

Le hoisting est un mécanisme JavaScript où les déclarations de variables et de fonctions sont déplacées en haut de leur portée avant l'exécution du code. Cela signifie que si nous faisons ceci :

```javascript
    console.log (greeter);
    var greeter = "say hello"

```

cela est interprété comme ceci :

```javascript
    var greeter;
    console.log(greeter); // greeter est undefined
    greeter = "say hello"

```

Ainsi, les variables `var` sont hoistées en haut de leur portée et initialisées avec une valeur de `undefined`.

### Problème avec var

Il y a une faiblesse qui vient avec `var`. Je vais utiliser l'exemple ci-dessous pour expliquer :

```javascript
    var greeter = "hey hi";
    var times = 4;

    if (times > 3) {
        var greeter = "say Hello instead"; 
    }
    
    console.log(greeter) // "say Hello instead"

```

Donc, puisque `times > 3` retourne vrai, `greeter` est redéfini en `"say Hello instead"`. Bien que cela ne pose pas de problème si vous souhaitez délibérément que `greeter` soit redéfini, cela devient un problème lorsque vous ne réalisez pas qu'une variable `greeter` a déjà été définie auparavant.

Si vous avez utilisé `greeter` dans d'autres parties de votre code, vous pourriez être surpris par le résultat obtenu. Cela causera probablement beaucoup de bugs dans votre code. C'est pourquoi `let` et `const` sont nécessaires.

## Let

`let` est maintenant préféré pour la déclaration de variables. Ce n'est pas une surprise car il s'agit d'une amélioration par rapport aux déclarations `var`. Il résout également le problème avec `var` que nous venons de couvrir. Voyons pourquoi.

### let est de portée de bloc

Un bloc est un morceau de code délimité par {}. Un bloc vit dans des accolades. Tout ce qui se trouve dans des accolades est un bloc. 

Ainsi, une variable déclarée dans un bloc avec `let` n'est disponible que pour une utilisation dans ce bloc. Laissez-moi expliquer cela avec un exemple :

```javascript
   let greeting = "say Hi";
   let times = 4;

   if (times > 3) {
        let hello = "say Hello instead";
        console.log(hello);// "say Hello instead"
    }
   console.log(hello) // hello n'est pas défini

```

Nous voyons que l'utilisation de `hello` en dehors de son bloc (les accolades où il a été défini) retourne une erreur. Cela est dû au fait que les variables `let` sont de portée de bloc.

### let peut être mis à jour mais pas redéclaré.

Tout comme `var`, une variable déclarée avec `let` peut être mise à jour dans sa portée. Contrairement à `var`, une variable `let` ne peut pas être redéclarée dans sa portée. Donc, alors que cela fonctionnera :

```javascript
    let greeting = "say Hi";
    greeting = "say Hello instead";

```

cela retournera une erreur :

```javascript
    let greeting = "say Hi";
    let greeting = "say Hello instead"; // erreur : L'identifiant 'greeting' a déjà été déclaré

```

Cependant, si la même variable est définie dans des portées différentes, il n'y aura pas d'erreur :

```javascript
    let greeting = "say Hi";
    if (true) {
        let greeting = "say Hello instead";
        console.log(greeting); // "say Hello instead"
    }
    console.log(greeting); // "say Hi"

```

Pourquoi n'y a-t-il pas d'erreur ? Cela est dû au fait que les deux instances sont traitées comme des variables différentes puisqu'elles ont des portées différentes.

Ce fait fait de `let` un meilleur choix que `var`. Lorsque vous utilisez `let`, vous n'avez pas à vous soucier si vous avez utilisé un nom pour une variable auparavant, car une variable n'existe que dans sa portée. 

De plus, puisque une variable ne peut pas être déclarée plus d'une fois dans une portée, alors le problème discuté précédemment qui se produit avec `var` ne se produit pas.

### Hoisting de let

Tout comme `var`, les déclarations `let` sont hoistées en haut. Contrairement à `var` qui est initialisé comme `undefined`, le mot-clé `let` n'est pas initialisé. Donc, si vous essayez d'utiliser une variable `let` avant sa déclaration, vous obtiendrez une `Reference Error`.

## Const

Les variables déclarées avec `const` maintiennent des valeurs constantes. Les déclarations `const` partagent certaines similitudes avec les déclarations `let`.

### Les déclarations const sont de portée de bloc

Comme les déclarations `let`, les déclarations `const` ne peuvent être accessibles que dans le bloc où elles ont été déclarées.

### const ne peut pas être mis à jour ou redéclaré

Cela signifie que la valeur d'une variable déclarée avec `const` reste la même dans sa portée. Elle ne peut pas être mise à jour ou redéclarée. Donc, si nous déclarons une variable avec `const`, nous ne pouvons ni faire ceci :

```javascript
    const greeting = "say Hi";
    greeting = "say Hello instead";// erreur : Assignment to constant variable. 

```

ni ceci :

```javascript
    const greeting = "say Hi";
    const greeting = "say Hello instead";// erreur : Identifier 'greeting' has already been declared

```

Chaque déclaration `const` doit donc être initialisée au moment de la déclaration.

Ce comportement est quelque peu différent lorsqu'il s'agit d'objets déclarés avec `const`. Bien qu'un objet `const` ne puisse pas être mis à jour, les propriétés de cet objet peuvent être mises à jour. Par conséquent, si nous déclarons un objet `const` comme ceci :

```javascript
    const greeting = {
        message: "say Hi",
        times: 4
    }

```

tandis que nous ne pouvons pas faire ceci :

```javascript
    greeting = {
        words: "Hello",
        number: "five"
    } // erreur :  Assignment to constant variable.

```

nous pouvons faire ceci :

```javascript
    greeting.message = "say Hello instead";

```

Cela mettra à jour la valeur de `greeting.message` sans retourner d'erreurs.

### Hoisting de const

Tout comme `let`, les déclarations `const` sont hoistées en haut mais ne sont pas initialisées.

Donc, au cas où vous auriez manqué les différences, les voici :

* Les déclarations `var` sont de portée globale ou de portée fonction, tandis que `let` et `const` sont de portée de bloc.
* Les variables `var` peuvent être mises à jour et redéclarées dans leur portée ; les variables `let` peuvent être mises à jour mais pas redéclarées ; les variables `const` ne peuvent ni être mises à jour ni redéclarées.
* Elles sont toutes hoistées en haut de leur portée. Mais tandis que les variables `var` sont initialisées avec `undefined`, les variables `let` et `const` ne sont pas initialisées.
* Alors que `var` et `let` peuvent être déclarées sans être initialisées, `const` doit être initialisé lors de la déclaration.

C'est tout. Vous avez des questions ou des ajouts ? Faites-le moi savoir.

Merci d'avoir lu :)