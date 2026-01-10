---
title: Comment trouver le nombre de voyelles dans une chaîne avec JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-01-18T17:27:04.000Z'
originalURL: https://freecodecamp.org/news/find-the-number-of-vowels-in-a-string-with-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2021/01/Screen-Shot-2021-01-17-at-6.16.19-PM.png
tags:
- name: interview questions
  slug: interview-questions
- name: JavaScript
  slug: javascript
- name: Problem Solving
  slug: problem-solving
seo_title: Comment trouver le nombre de voyelles dans une chaîne avec JavaScript
seo_desc: "By Madison Kanna\nIn this tutorial, we’ll learn how to find the number\
  \ of vowels in a string with JavaScript. This is a problem you might be asked in\
  \ junior developer job interviews, and it’s also a CodeWars problem. \nBefore we\
  \ get started coding, let..."
---

Par Madison Kanna

Dans ce tutoriel, nous allons apprendre comment trouver le nombre de voyelles dans une chaîne avec JavaScript. C'est un problème qui pourrait vous être posé lors d'entretiens pour un poste de développeur junior, et c'est aussi un problème [CodeWars](https://www.codewars.com/kata/54ff3102c1bad923760001f3). 

Avant de commencer à coder, lisons attentivement la description du problème :

**Retourner le nombre (compte) de voyelles dans une chaîne donnée. Nous considérerons a, e, i, o et u comme des voyelles, mais pas y. La chaîne d'entrée ne contiendra que des lettres minuscules et/ou des espaces.**

## Étape 1 : Élaborer un plan pour résoudre le problème

Pour ce problème, nous allons créer une fonction, appelée `getCount`, qui prend en entrée une chaîne et retourne en sortie le nombre de voyelles présentes dans cette chaîne.  
  
Passons en revue quelques exemples.

![Image](https://lh4.googleusercontent.com/0NnD6g02UboUYJkZ0KOJMw7abNXVH-e9iuq9kv1qg-OFzJ_k8t3ZVfMzj6MkPE45fjQxVBIshpJJNxF_e6KGDWSCdwp7BWd8vVasgeiJ1nYiK-7ufFJz1XuyIXcHNApmtBhn7Kk9)

Avec le premier exemple, nous voyons que notre fonction retourne 5, ce qui correspond au nombre de fois où une voyelle apparaît dans la chaîne `abracadabra`. Avec la chaîne `abc`, seul 1 est retourné, car une seule voyelle (a) apparaît.

Pour résoudre ce problème, nous allons créer une variable `vowelsCount` qui gardera une trace du nombre de voyelles dans la chaîne. 

Nous allons également créer un tableau, vowels, qui contiendra toutes nos voyelles. Nous allons parcourir chaque caractère de notre chaîne. Si le caractère est une voyelle, nous allons augmenter notre variable `vowelsCount`.

Enfin, nous allons retourner la variable `vowelsCount`.  
  
Commençons !

## Étape 2 : Écrire le code pour résoudre le problème

Tout d'abord, nous écrivons notre fonction, `getCount`. Ensuite, nous allons créer une variable, `vowelsCount`, et la définir à `0`.

![Image](https://lh4.googleusercontent.com/3C2OuHNi9S9SL-SUEYzM8PSodXO1bYULEd9LLec7clus1o5TEvqBBgVy1STfDUoq3hFLT85VLVGAAzL8h949fazt9_36S54Oe97U39IjJhl9LBDTWCpSFd9w9wMFpkHdfSbeFpAq)

  
Nous allons créer notre tableau de voyelles ensuite. Cela nous permet d'avoir toutes les voyelles au même endroit, et nous pourrons utiliser ce tableau plus tard.

![Image](https://lh6.googleusercontent.com/g6F__ll7kJNmOq6c3kT6Z7X_zcslPkO8AuF5kUDYFcLcnJ9v-rpf3bm1NUSDPCAVWWnfpq9GS7cADMuN5GS3CdiTbAfun9Gth0CBUFGFl5vhviLMrKHKfQa9KPfWkujtV1_SLWHG)

  
Maintenant, nous devons parcourir chaque caractère de notre chaîne d'entrée, `str`. Nous devons examiner chaque caractère de notre chaîne pour déterminer s'il s'agit d'une voyelle ou non.

Pour ce faire, nous pouvons utiliser l'instruction `for...of` qui fonctionne sur les chaînes. Vous pouvez en lire plus à ce sujet [ici](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of).

![Image](https://lh3.googleusercontent.com/mMSkKHhYAhJxh9F71Ccs4B9MyKpjHNlyIumJwJ9n7bTo-o6eR1YQLHsPe13VCVx7XlFU20TQHr2B5bXv52cbIHvTs2Jl2xIwBPo5hD0-ILOAW-o66sG2uyxUF5WljDTgDrsqgP7X)

  
Maintenant, à l'intérieur de notre boucle for, nous avons la possibilité d'examiner chaque caractère de notre chaîne.   
  
Ensuite, nous voulons vérifier si chaque caractère est une voyelle. 

Pour ce faire, nous pouvons utiliser la méthode `includes`. La méthode `includes()` détermine si un tableau contient une certaine valeur parmi ses entrées. Elle retourne true si c'est le cas, et false sinon. 

En utilisant `includes`, nous allons vérifier si notre tableau de voyelles contient le caractère que nous sommes en train d'itérer dans notre boucle.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-89.png)

Nous avons créé notre `instruction if` pour vérifier si le caractère actuel est une voyelle. Si le caractère est une voyelle, alors nous voulons augmenter notre variable `vowelsCount`. Pour ce faire, nous pouvons utiliser l'opérateur d'incrémentation en JavaScript :

![Image](https://lh4.googleusercontent.com/YELFhUaEOI51eOBznA9delrQlT5_brpGzM71vXiO6S1ARcy-IAbM06mYgPr6zQVC-0eytb87eQX8_5UBcZ0rMPLfTpf3uGHbJhpTWymoXGwLMDscQbp9BR1SIzbsrQSssmH689t2)

  
À ce stade de notre code, nous avons examiné chaque caractère de la chaîne, déterminé s'il s'agissait d'une voyelle ou non, et augmenté le nombre stocké dans `vowelsCount` si c'était le cas.

Enfin, tout ce que nous devons faire est de faire en sorte que notre fonction retourne notre variable `vowelsCount`. Nous pouvons le faire en retournant la variable en dehors de notre boucle.

![Image](https://lh6.googleusercontent.com/4U_WmVuqES_Z5Tb79te7k7nCorSGuIvsKoWVXPjV1e7dug-pSylt7GMa7MNvkDBX-1PT0EtfFmCi0n-pqN0YGpo2Rs7xntRQViCzLBEYuVi0rDJOQsQJxkgScPdGHXT8ThDLvn5I)

  
Nous y voilà.

## C'est tout !

Nous avons maintenant écrit une fonction qui prend en entrée une chaîne et retourne en sortie le nombre de fois où une voyelle est apparue dans la chaîne. 

### Si vous avez aimé cet article, rejoignez mon [coding club](https://madisonkanna.us14.list-manage.com/subscribe/post?u=323fd92759e9e0b8d4083d008&id=033dfeb98f), où nous relevons ensemble des défis de codage chaque dimanche.  
  
Si vous avez des commentaires ou des questions sur cet article, n'hésitez pas à me tweeter @madisonkanna.