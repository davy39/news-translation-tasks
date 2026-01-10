---
title: Comprendre Array.prototype.reduce() et la récursivité en utilisant une tarte
  aux pommes
subtitle: ''
author: Victoria Drake
co_authors: []
series: null
date: '2017-05-30T02:10:07.000Z'
originalURL: https://freecodecamp.org/news/understanding-array-prototype-reduce-and-recursion-using-apple-pie-f60cde58ea51
coverImage: https://cdn-media-1.freecodecamp.org/images/0*VsKg3XJwl9mJScFc.
tags:
- name: algorithms
  slug: algorithms
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comprendre Array.prototype.reduce() et la récursivité en utilisant une
  tarte aux pommes
seo_desc: I was having trouble understanding reduce() and recursion in JavaScript,
  so I wrote this article to explain it to myself (hey, look, recursion!). These concepts
  share some similarities with making apple pies. I hope you find my examples both
  helpful ...
---

J'avais du mal à comprendre `reduce()` et la récursivité en JavaScript, alors j'ai écrit cet article pour me l'expliquer à moi-même (hé, regardez, de la récursivité !). Ces concepts partagent certaines similitudes avec la fabrication de tartes aux pommes. J'espère que vous trouverez mes exemples à la fois utiles et délicieux.

Étant donné un tableau avec des tableaux imbriqués :

```
var arr = [1, [2], [3, [[4]]]]
```

Nous voulons produire ceci :

```
var flat = [1, 2, 3, 4]
```

### Utilisation de boucles for et d'instructions if

Si nous connaissons le nombre maximum de tableaux imbriqués que nous rencontrerons (il y en a 4 dans cet exemple), nous pouvons utiliser des boucles `for` pour itérer à travers chaque élément du tableau, puis des instructions `if` pour vérifier si cet élément est lui-même un tableau, et ainsi de suite...

```js
function flatten() {
    var flat = [];
    for (var i=0; i<arr.length; i++) {
    if (Array.isArray(arr[i])) {
        for (var ii=0; ii<arr[i].length; ii++) {
        if (Array.isArray(arr[i][ii])) {
            for (var iii=0; iii<arr[i][ii].length; iii++) {
            for (var iiii=0; iiii<arr[i][ii][iii].length; iiii++) {
                if (Array.isArray(arr[i][ii][iii])) {
                flat.push(arr[i][ii][iii][iiii]);
                } else {
                flat.push(arr[i][ii][iii]);
                }
            }
            }
        } else {
            flat.push(arr[i][ii]);
        }
        }
    } else {
    flat.push(arr[i]);
    }
    }
}

// [1, 2, 3, 4]
```

...Ce qui fonctionne, mais est à la fois difficile à lire et encore plus difficile à comprendre. De plus, cela ne fonctionne que si vous savez combien de tableaux imbriqués vous devez traiter, et pouvez-vous imaginer devoir déboguer ce désordre ?! (Minute, je pense qu'il y a un `i` en trop quelque part.)

### Utilisation de reduce

JavaScript dispose de quelques méthodes que nous pouvons utiliser pour rendre notre code plus concis et plus facile à suivre. L'une d'entre elles est `reduce()` et elle ressemble à ceci :

```js
var flat = arr.reduce(function(done,curr){
    return done.concat(curr);
}, []);

// [ 1, 2, 3, [ [ 4 ] ] ]
```

C'est beaucoup moins de code, mais nous n'avons pas traité certains des tableaux imbriqués. Examinons d'abord ensemble `reduce()` et voyons ce qu'il fait pour voir comment nous allons corriger cela.

> _Array.prototype.reduce()_

> _La méthode reduce() applique une fonction contre un accumulateur et chaque élément du tableau (de gauche à droite) pour le réduire à une seule valeur._ [(MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/Reduce?v=example))

Ce n'est pas aussi compliqué qu'il y paraît. Pensons à `reduce()` comme à un développeur sans emploi (l'IA a pris tous les emplois de dev) avec un panier vide. Nous l'appellerons Adam. La principale fonction d'Adam est maintenant de prendre des pommes dans une pile, de les faire briller et de les mettre une par une dans le panier. Ce panier de pommes brillantes est destiné à devenir de délicieuses tartes aux pommes. C'est un travail très important.

![Image](https://cdn-media-1.freecodecamp.org/images/0*T57I3z5jYDfhqNb_.)
_Des pommes plus un effort humain égalent une tarte. À ne pas confondre avec une tarte aux pommes humaines, qui est moins appétissante._

Dans notre exemple ci-dessus, la pile de pommes est notre tableau, `arr`. Notre panier est `done`, l'accumulateur. La valeur initiale de `done` est un tableau vide, que nous voyons comme `[]` à la fin de notre fonction reduce. La pomme qu'Adam est en train de faire briller, vous l'avez deviné, est `curr`. Une fois qu'Adam a traité la pomme actuelle, il la place dans le panier (`.concat()`). Lorsqu'il n'y a plus de pommes dans la pile, il nous retourne le panier de pommes polies et rentre chez lui pour voir son chat.

### Utilisation de reduce de manière récursive pour traiter les tableaux imbriqués

Donc, tout cela est bien et bon, et maintenant nous avons un panier de pommes polies. Mais nous avons encore quelques tableaux imbriqués à traiter. Revenons à notre analogie, disons que certaines des pommes dans la pile sont dans des boîtes. Dans chaque boîte, il pourrait y avoir plus de pommes, et/ou plus de boîtes contenant des pommes plus petites et plus mignonnes.

![Image](https://cdn-media-1.freecodecamp.org/images/0*X3isJJiuOFuWkESZ.)
_Des pommes adorables, légèrement asymétriques, veulent juste être aimées/mangées._

Voici ce que nous voulons que notre fonction de traitement des pommes/Adam fasse :

1. Si la pile de pommes est une pile de pommes, prendre une pomme de la pile.
2. Si la pomme est une pomme, la faire briller, la mettre dans le panier.
3. Si la pomme est une boîte, ouvrir la boîte. Si la boîte contient une pomme, aller à l'étape 2.
4. Si la boîte contient une autre boîte, ouvrir cette boîte, et aller à l'étape 3.
5. Lorsque la pile n'existe plus, nous donner le panier de pommes brillantes.
6. Si la pile de pommes n'est pas une pile de pommes, rendre ce qu'elle est.

Une fonction reduce récursive qui accomplit cela est :

```js
function flatten(arr) {
  if (Array.isArray(arr)) {
  return arr.reduce(function(done,curr){
    return done.concat(flatten(curr));
    }, []);
  } else {
    return arr;
  }
}

// [ 1, 2, 3, 4 ]
```

Patience, je vais expliquer.

> **_Récursivité_**

> _Un acte où une fonction s'appelle elle-même. La récursivité est utilisée pour résoudre des problèmes qui contiennent des sous-problèmes plus petits. Une fonction récursive peut recevoir deux entrées : un cas de base (met fin à la récursivité) ou un cas récursif (continue la récursivité)._ [(MDN](https://developer.mozilla.org/en-US/docs/Glossary/Recursion))

Si vous examinez notre code ci-dessus, vous verrez que `flatten()` apparaît deux fois. La première fois qu'il apparaît, il dit à Adam quoi faire avec la pile de pommes. La deuxième fois, il lui dit quoi faire avec la chose qu'il tient actuellement, en fournissant des instructions au cas où c'est une pomme, et au cas où ce n'est pas une pomme. La chose à noter est que ces instructions sont une _répétition des instructions originales avec lesquelles nous avons commencé_ - et c'est la récursivité.

Nous allons le décomposer ligne par ligne pour plus de clarté :

1. `function flatten(arr) {` - nous nommons notre fonction globale et spécifions qu'elle prendra un argument, `arr`.
2. `if (Array.isArray(arr)) {` - nous examinons l'"arrgument" fourni (je sais, je suis très drôle) pour déterminer s'il s'agit d'un tableau.
3. `return arr.reduce(function(done,curr){` - si la ligne précédente est vraie et que l'argument est un tableau, nous voulons le réduire. C'est notre cas récursif. Nous appliquerons la fonction suivante à chaque élément du tableau...
4. `return done.concat(flatten(curr));` - un rebondissement inattendu apparaît ! La fonction que nous voulons appliquer est la fonction même dans laquelle nous nous trouvons. Colloquialement : reprenez depuis le début.
5. `}, []);` - nous disons à notre fonction reduce de commencer avec un accumulateur vide (`done`), et nous l'enveloppons.
6. `} else {` - cela résout notre instruction if à la ligne 2. Si l'argument fourni n'est pas un tableau...
7. `return arr;` - retourner ce que `arr` est. (Espérons une pomme mignonne.) C'est notre cas de base qui nous sort de la récursivité.
8. `}` - fin de l'instruction else.
9. `}` - fin de la fonction globale.

Et nous avons terminé ! Nous sommes passés de notre solution de boucle `for` imbriquée sur 24 lignes et 4 niveaux de profondeur à une solution récursive reduce beaucoup plus concise de 9 lignes. Reduce et la récursivité peuvent sembler un peu impénétrables au premier abord, mais ce sont des outils précieux qui vous feront économiser beaucoup d'efforts futurs une fois que vous les aurez compris.

Et ne vous inquiétez pas pour Adam, notre développeur sans emploi. Il a eu tellement de presse après avoir été présenté dans cet article qu'il a ouvert sa propre usine de tartes aux pommes gérée par l'IA. Il est très heureux.

![Image](https://cdn-media-1.freecodecamp.org/images/0*liHR63UMBiJon9Gc.)
_+1 pour vous si vous avez vu celle-ci venir._

_Merci d'avoir lu ! Vous pouvez trouver plus d'articles expliquant les concepts de codage avec de la nourriture [sur mon blog](https://victoria.dev/verbose/)._