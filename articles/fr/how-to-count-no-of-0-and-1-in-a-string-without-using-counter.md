---
title: Comment compter le nombre de 0 et de 1 dans une chaîne sans utiliser de compteur
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-08-23T22:17:23.000Z'
originalURL: https://freecodecamp.org/news/how-to-count-no-of-0-and-1-in-a-string-without-using-counter
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca0ae740569d1a4ca4a21.jpg
tags:
- name: interview questions
  slug: interview-questions
- name: Job Hunting
  slug: job-hunting
seo_title: Comment compter le nombre de 0 et de 1 dans une chaîne sans utiliser de
  compteur
seo_desc: 'By Ujjwal Gupta

  This question is often asked in interviews to test the candidate''s approach to
  thinking about code.

  Problem Statement

  You have a string which contains only 0''s and 1''s. You need to write a program
  which will return the number of 0''s a...'
---

Par Ujjwal Gupta

Cette question est souvent posée lors des entretiens pour tester l'approche du candidat à la réflexion sur le code.

### Énoncé du problème

Vous avez une chaîne qui ne contient que des 0 et des 1. Vous devez écrire un programme qui retournera le nombre de 0 et de 1, et vous n'êtes pas autorisé à utiliser une variable de compteur de quelque manière que ce soit.

Cela semble compliqué, n'est-ce pas ?

Ne vous inquiétez pas - c'est très simple. Je vais vous apprendre à le faire de deux manières :

* Avec un compteur (l'approche classique)
* Sans utiliser de compteur (comme requis dans la question d'entretien)

## Commençons à coder

### Avec un compteur

```javascript
function count(str) {
  var countForZero = 0;
  var countForOne = 0;
    
  for (var i = 0, length = str.length; i < length; i++) {
    if (str[i] === '0') {
      countForZero++;
    }
    else {
      countForOne++;
    }
  }
    
  return {
    'zero': countForZero,
    'One': countForOne
  };
}

```

**La logique du code ci-dessus est :**

* Maintenez deux variables pour compter les zéros et les uns.
* Parcourez les caractères de la chaîne, et lorsqu'un zéro est trouvé, incrémentez countForZero. Lorsqu'un un est trouvé, incrémentez countForOne.
* Dans la dernière partie, nous retournons le compte dans un objet.

Vous pouvez essayer le code ci-dessus en utilisant ce lien : [https://repl.it/repls/PurpleIdolizedInstructions](https://repl.it/repls/PurpleIdolizedInstructions)

Maintenant, voyons la solution sans compteur.

### Sans compteur

```
function count(str) {
  var sum = 0;
  
  for (var i = 0, length = str.length; i < length; i++) {
    sum += Number(str[i]);
  }
  
  return {
    'zero': str.length - sum,
    'One': sum
  };
}
```

Comme vous pouvez le voir dans le code ci-dessus, je n'utilise aucun compteur, mais plutôt une variable appelée sum. Alors, quel est le concept ici ?

**Le concept est :**

> La somme d'un caractère d'une chaîne qui contient des zéros et des uns sera toujours égale au nombre de 1.

Par exemple : 0011001 : 0+0+1+1+0+0+1 = 3 = nombre de 1

> Et le nombre de zéros = longueur de la chaîne - nombre de 1

**La logique du code ci-dessus est :**

* Maintenez une variable sum initialisée avec la valeur zéro.
* Parcourez les caractères de la chaîne et faites la somme de tous les caractères.
* La somme de tous les caractères de la chaîne sera le nombre de 1, et le nombre de zéros sera (longueur de la chaîne - nombre de 1).
* Dans la dernière partie, nous retournons le compte dans un objet.

Vous pouvez essayer le code ci-dessus en utilisant ce lien : [https://repl.it/repls/ComfortableOrdinaryConversions](https://repl.it/repls/ComfortableOrdinaryConversions)

J'espère que vous êtes maintenant capable de comprendre comment répondre à cette question avec et sans compteur.

Si vous avez des questions, n'hésitez pas à demander dans la section des commentaires. Ou si vous avez d'autres astuces, faites-le moi savoir également.