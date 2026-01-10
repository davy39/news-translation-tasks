---
title: Comment répondre à n'importe quelle question d'entretien technique – Exemple
  inclus
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-17T17:48:26.000Z'
originalURL: https://freecodecamp.org/news/how-to-answer-any-technical-interview-question-with-example
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c99a9740569d1a4ca2106.jpg
tags:
- name: coding interview
  slug: coding-interview
- name: interview questions
  slug: interview-questions
- name: Interview tips
  slug: interview-tips
- name: Job Interview
  slug: job-interview
seo_title: Comment répondre à n'importe quelle question d'entretien technique – Exemple
  inclus
seo_desc: "By Sameer Khoja\nTechnical interviews can be extremely daunting. From the\
  \ beginning of each question to the end, it's important to know what to expect,\
  \ and to be aware of the areas you might be asked about. \nFortunately, there's\
  \ a way to prepare for a..."
---

Par Sameer Khoja

Les entretiens techniques peuvent être extrêmement intimidants. Dès le début de chaque question jusqu'à la fin, il est important de savoir à quoi s'attendre et d'être conscient des domaines qui pourraient être abordés. 

Heureusement, il existe une méthode pour se préparer à toute question qui pourrait se présenter. Elle comporte quatre parties :

1. **Comprendre la question**
2. **Discuter des compromis des solutions**
3. **Écrire le code**
4. **Tester le code**

Essayons cette technique avec un problème d'exemple impliquant des LinkedLists.

## Le Problème

**Question :** Étant donné deux nœuds de LinkedList simplement chaînées, déterminer si les deux listes s'intersectent. Retourner le nœud d'intersection. Notez que l'intersection est définie par référence, et non par valeur. Si le k-ième nœud de la première liste chaînée est exactement le même nœud (par référence) que le j-ième nœud de la deuxième liste chaînée, alors elles s'intersectent.

![Image](https://cdn.substack.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F13a33ada-6399-4679-a631-0e43be042886_1076x292.png)

## Étape 1 : Comprendre la question.

Il est vraiment important de savoir exactement ce que cette question demande. Certaines questions que nous pourrions poser à l'intervieweur sont :

1. Que voulons-nous exactement retourner ? _(R : Le nœud d'intersection)._
2. Cela signifie-t-il que nous pouvons supposer que les listes chaînées s'intersectent toujours ? _(R : Oui)_

Il est toujours important de bien comprendre la question avant de penser à l'approche pour la résoudre.

## Étape 2 : Discuter des compromis des différentes solutions.

Une solution immédiate consiste à parcourir les deux listes chaînées en même temps jusqu'à atteindre une intersection. Pour cet exemple, nous créerions un **pointeur** aux nœuds 2 et 7, et nous **parcourrions** chacun d'eux un par un jusqu'à atteindre un nœud commun.

Cependant, comme vous l'avez peut-être remarqué, cela ne fonctionnera pas si les longueurs des deux LinkedLists diffèrent. Ce que nous voulons faire, c'est essentiellement "supprimer" la partie initiale de la LinkedListNode la plus longue, puis itérer de manière répétée.

Ce serait le genre de conversation à avoir avec votre intervieweur.

## Étape 3 : Écrire le code.

Voici la méthode pour y parvenir.

![Image](https://cdn.substack.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fa761d963-8a59-4c0a-bd90-489931e6c5e2_1330x660.png)

Nous utilisons ici des **méthodes auxiliaires**. Nous utilisons `getKthNode()` pour obtenir le k-ième nœud de la liste chaînée donnée. Cela est utile lors du parcours de la liste chaînée la plus longue pour "supprimer" les nœuds supplémentaires. 

Nous utilisons également `getTailAndSize()` qui capture à la fois la longueur et le dernier nœud de la liste donnée. Cela est utile car nous avons définitivement besoin de la taille pour comparer les longueurs des listes. Nous avons également besoin des queues car si les queues des deux listes sont inégales, alors elles ne s'intersectent pas du tout. 

Notez que lorsque nous disons "inégales", nous voulons dire que les deux nœuds ne référencent pas le même **objet**. Même s'ils peuvent avoir la même valeur et sembler identiques, ils doivent référencer le même LinkedListNode pour être considérés comme égaux. (Vous pouvez trouver plus d'informations à ce sujet [ici](http://shortn/_xLxPLI0JXV).) 

Revenons à la question, si nous rencontrons le cas où les queues sont inégales, nous retournons une valeur d'échec (null).

![Image](https://cdn.substack.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fa50b3b05-93d6-4f2b-bd40-1b2127c18490_1072x966.png)

## Étape 4 : Tester le code.

Voici quelques bons cas de test que nous pouvons ajouter. Une règle empirique utile pour les cas de test est la suivante :

* Cas vide/null
* Considérer les options au milieu/début/fin
* Tailles égales ou différentes

Cette stratégie ne s'applique pas seulement aux questions sur les LinkedList – elle fonctionnerait pour les tableaux, les Strings et essentiellement toute autre structure de données. 

Pour cette question, nos tests LinkedList seraient les suivants :

* Deux listes chaînées qui s'intersectent au début/milieu/fin
* Les deux/une des listes chaînées est nulle (doit retourner null)
* Les listes chaînées sont de la même/taille différente

Nous avons terminé !

![Coding GIF by memecandy](https://cdn.substack.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_lossy/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F8cae3ba9-33c1-4c92-a8ea-fb0119929389_300x300.gif)

**Plus de questions :**

* [Circular Linked List](https://leetcode.com/problems/linked-list-cycle/)
* [Reversing a Linked List](https://leetcode.com/problems/reverse-linked-list/)
* [Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/)

_Intéressé à se lancer dans l'informatique ? Désireux d'élargir votre base de connaissances et d'apprendre de nouvelles choses ? Aimez résoudre des problèmes ?_

_Si c'est le cas, [SWEPrep](http://sweprep.com) pourrait être la newsletter qu'il vous faut. Abonnez-vous pour obtenir des prompts d'entretien entièrement expliqués, couramment donnés dans les entretiens d'ingénierie, des Arrays à la Programmation Dynamique. Les questions sortent chaque semaine et sont également catégorisées par sujet et difficulté. Le post ci-dessus est un Guest Post de l'auteur, Sameer Khoja._

  
_[Abonnez-vous](http://sweprep.com) pour obtenir un accès complet à la newsletter. Ne manquez jamais une mise à jour._