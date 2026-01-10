---
title: La récursion peut sembler effrayante – Mais elle n'a pas à l'être
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-05-07T16:59:53.000Z'
originalURL: https://freecodecamp.org/news/recursion-doesnt-have-to-be-scary
coverImage: https://www.freecodecamp.org/news/content/images/2021/05/recursion-image.jpeg
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: Recursion
  slug: recursion
- name: software development
  slug: software-development
- name: Web Development
  slug: web-development
seo_title: La récursion peut sembler effrayante – Mais elle n'a pas à l'être
seo_desc: 'By Dave Gray

  Any concept that we don''t fully understand can be scary at first.

  Recursion is a topic that programming students don''t learn right away. But that
  doesn''t mean it needs to be scary or cause anxiety.

  In fact, recursion is a concept that we...'
---

Par Dave Gray

Tout concept que nous ne comprenons pas entièrement peut être effrayant au début.

La récursion est un sujet que les étudiants en programmation n'apprennent pas tout de suite. Mais cela ne signifie pas qu'elle doive être effrayante ou provoquer de l'anxiété.

En fait, la récursion est un concept que nous pouvons définir assez simplement.

Selon [Wikipedia](https://en.wikipedia.org/wiki/Recursion_(computer_science)) :

> En informatique, la récursion est une méthode de résolution d'un problème où la solution dépend de solutions à des instances plus petites du même problème.

Et vous pouvez appliquer la récursion dans votre code en créant une fonction qui s'appelle elle-même.

## Toute fonction avec une boucle peut être récursive à la place

Voici une fonction appelée `countToTen` qui utilise une boucle `while` pour enregistrer chaque nombre de un à dix :

```js
const countToTen = (num = 1) => {
    while (num <= 10) {
        console.log(num);
        num++;
    }
}

countToTen();

```

Nous pouvons écrire la même fonction avec la récursion au lieu d'une boucle.

Remarquez que les fonctions récursives ont deux parties :

1. La fonction s'appelle elle-même (également appelée l'appel récursif)
2. Au moins une condition pour quitter la récursion (également appelée le cas de base)

```js
const countToTen = (num = 1) => {
    if (num > 10) return; //cas de base
    console.log(num);
    num++;
    countToTen(num); //appel récursif
}

countToTen();

```

Cela ne veut pas dire que nous **devrions** **toujours** remplacer les boucles par la récursion.

Il y a des cas où l'utilisation de la récursion est le meilleur choix – et de même, il y a des cas où ce n'est pas le meilleur choix.

## Pourquoi utiliser la récursion

Examinons quelques raisons d'utiliser la récursion. Nous verrons quelques exemples ci-dessous.

### Moins de lignes de code

L'application de la récursion donne généralement une solution avec moins de lignes de code qu'une solution qui n'utilise pas la récursion.

### Un code plus élégant

En plus d'avoir moins de lignes de code, les solutions récursives sont généralement plus agréables à regarder. En d'autres termes, les solutions récursives sont généralement considérées comme élégantes.

### Une meilleure lisibilité

Les raisons 1 et 2 se combinent généralement pour créer la raison 3, qui est l'augmentation de la lisibilité de votre code. N'oubliez pas que nous n'écrivons pas de code uniquement pour nous-mêmes. Nous écrivons du code pour les développeurs qui nous suivent et qui doivent comprendre notre code.

## Raisons de NE PAS utiliser la récursion

### Pertes de performance

La répétition d'appels de fonction n'est pas aussi efficace ou performante que l'application d'une boucle. Nous ne voulons pas simplement choisir la récursion parce que nous le pouvons.

### Problèmes de débogage

La logique de la récursion n'est pas toujours facile à suivre. L'utilisation de la récursion peut rendre votre code plus difficile à déboguer.

### La lisibilité est-elle améliorée ?

Une meilleure lisibilité n'est pas garantie par l'utilisation de la récursion. En fait, cela peut être subjectif et/ou situationnel. Vous devriez évaluer la lisibilité, et si elle n'est pas améliorée, la récursion n'est peut-être pas la meilleure réponse.

## Exemples de récursion

Les problèmes de récursion sont les favoris des entretiens.

L'un de ces problèmes demande une fonction qui renvoie `x` nombres de la suite de Fibonacci.

La suite de Fibonacci additionne les deux nombres précédents de la suite pour créer le nombre suivant dans la suite. Voici les dix premiers nombres de la suite :  
`[0,1,1,2,3,5,8,13,21,34]`

Nous pouvons écrire cette fonction sans récursion :

```js
const fibonacci = (num = 2, array = [0, 1]) => {
    while (num > 2) {
        const [nextToLast, last] = array.slice(-2);
        array.push(nextToLast + last);
        num -= 1;
    }
    return array;
}

console.log(fibonacci(10));

```

Et voici une version récursive de la même fonction :

```js
const fibonacci = (num = 2, array = [0, 1]) => {
    if (num < 2) return array.slice(0, array.length - 1);
    const [nextToLast, last] = array.slice(-2);
    return fibonacci(num - 1, [...array, nextToLast + last]);
}

console.log(fibonacci(10));

```

La fonction récursive a effectivement moins de lignes de code. Mais je ne suis pas sûr que nous puissions dire avec certitude qu'elle a une élégance ou une lisibilité accrue.

Regardons un autre problème où la récursion a un impact plus important.

Un autre favori des entretiens consiste à demander une fonction qui renvoie le nième nombre de la suite de Fibonacci. Par conséquent, si la fonction reçoit `10` comme paramètre, elle devrait renvoyer `34`.

Sans l'utilisation de la récursion, une solution possible ressemble à ceci :

```js
const fibonacciPos = (pos = 1) => {
    if (pos < 2) return pos;
    const seq = [0, 1];
    for (let i = 2; i <= pos; i++) {
        const [nextToLast, last] = seq.slice(-2);
        seq.push(nextToLast + last);
    }
    return seq[pos];
}

console.log(fibonacciPos(10));

```

Cependant, avec la récursion, la solution est beaucoup plus courte et sans doute plus élégante :

```js
const fibonacciPos = (pos = 1) => {
    if (pos < 2) return pos;
    return fibonacciPos(pos - 1) + fibonacciPos(pos - 2);
}

console.log(fibonacciPos(10));

```

Wow ! Cela a fait une énorme différence.

Remarquez comment la ligne de retour appelle réellement la fonction deux fois.

Comprenez-vous la logique de ces fonctions récursives ? Si ce n'est pas le cas, passez du temps à les expérimenter pour comprendre comment elles fonctionnent. Après l'avoir fait, vous conviendrez probablement que la lisibilité est également améliorée.

Pour souligner à quel point l'amélioration de la lisibilité est subjective, regardons la même fonction récursive que ci-dessus écrite en une seule ligne (la ligne peut s'enrouler dans votre navigateur, mais c'est une seule ligne de code) :

```js
const fibonacciPos= pos => pos < 2 ? pos : fibonacciPos(pos - 1) + fibonacciPos(pos - 2);

console.log(fibonacciPos(10));

```

Notre solution récursive originale est passée de quatre lignes de code à une seule !

Est-ce plus lisible pour vous ? Suivez-vous toujours la logique qui se cache derrière ?

Votre réponse dépendra de votre niveau de compréhension actuel. La solution en une ligne utilise une instruction ternaire, présente une fonction fléchée sans parenthèses qui implique également une instruction de retour, et applique la récursion comme précédemment.

Je n'écris pas habituellement de fonctions comme la solution en une ligne ci-dessus parce que j'enseigne fréquemment des cours de développement web pour débutants. Par conséquent, je divise souvent mon code en étapes délibérées qui sont plus faciles à suivre.

Cela ne veut pas dire qu'il y a quelque chose de mal avec la solution en une ligne ci-dessus.

En fait, la fonction est élégante, lisible et très efficace si vous en comprenez la logique.

Si vous travaillez en équipe, votre équipe peut avoir un guide de style. Si une fonction en une ligne est préférée lorsque c'est possible, allez-y ! Si un style plus délibéré, étape par étape, est préféré, suivez votre guide. Ces décisions sont totalement situationnelles.

## Conclusion

La récursion peut sembler effrayante, mais elle n'a pas à l'être.

Nous pouvons décomposer le concept de récursion en une définition simple.

N'utilisez pas le pouvoir de la récursion simplement parce que vous le pouvez.

Vous devriez baser la décision d'utiliser la récursion dans votre code sur l'efficacité, la performance, l'élégance et la lisibilité.

Vous vous demandez peut-être où la récursion pourrait être appliquée dans le "monde réel" au lieu de simplement répondre à des questions d'entretien sur la suite de Fibonacci.

Je vous laisse avec un tutoriel de ma chaîne Youtube. Non seulement j'examine de plus près les exemples ci-dessus, mais je révèle également des cas du "monde réel" où l'application de la récursion est le meilleur choix :

%[https://youtu.be/Q0alTGQ-lXk]