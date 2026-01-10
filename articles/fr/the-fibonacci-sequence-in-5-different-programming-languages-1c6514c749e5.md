---
title: La suite de Fibonacci – Expliquée en Python, JavaScript, C++, Java et Swift
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-01T15:38:00.000Z'
originalURL: https://freecodecamp.org/news/the-fibonacci-sequence-in-5-different-programming-languages-1c6514c749e5
coverImage: https://cdn-media-1.freecodecamp.org/images/0*74G0BbEUwrCaw8iQ.
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: 'tech '
  slug: tech
seo_title: La suite de Fibonacci – Expliquée en Python, JavaScript, C++, Java et Swift
seo_desc: 'By Pau Pavón

  The Fibonacci sequence is, by definition, the integer sequence in which every number
  after the first two is the sum of the two preceding numbers. To simplify:

  0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, …

  It has many applications in ma...'
---

Par Pau Pavón

La suite de Fibonacci est, par définition, la suite d'entiers dans laquelle chaque nombre après les deux premiers est la somme des deux nombres précédents. Pour simplifier :

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, …

Elle a de nombreuses applications en mathématiques et même en trading (oui, vous avez bien lu : trading), mais ce n'est pas le sujet de cet article. Mon objectif aujourd'hui est de vous montrer comment vous pouvez calculer n'importe quel terme de cette série de nombres dans cinq langages de programmation différents en utilisant des fonctions récursives.

Les fonctions récursives sont celles qui, en gros, s'appellent elles-mêmes.

Je tiens à noter que ce n'est pas la meilleure méthode pour le faire — en fait, elle pourrait être considérée comme la méthode la plus basique à cette fin. Cela est dû à la puissance de calcul requise pour calculer les termes plus grands de la série, qui est immense. Le nombre de fois où la fonction est appelée provoque un débordement de pile dans la plupart des langages.

Quoi qu'il en soit, pour les besoins de ce tutoriel, commençons.

Tout d'abord, réfléchissons à ce que le code va ressembler. Il inclura :

· Une fonction récursive F (F pour Fibonacci) : pour calculer la valeur du terme suivant.

· Rien d'autre : je vous avais prévenu que c'était assez basique.

Notre fonction prendra _n_ comme entrée, qui se référera au _n_ième terme de la séquence que nous voulons calculer. Ainsi, F(4) devrait retourner le quatrième terme de la séquence.

Planifions cela. Le code devrait, quel que soit le langage, ressembler à quelque chose comme ceci :

[`function F(n)  if n = 0`](https://unsplash.com?utm_source=medium&utm_medium=referral)  
    [`return 0  if n = 1`](https://unsplash.com?utm_source=medium&utm_medium=referral)  
    [`return 1  else`](https://unsplash.com?utm_source=medium&utm_medium=referral)  
    [`return F(n-1) + F(n-2)`](https://unsplash.com?utm_source=medium&utm_medium=referral)

Note : le terme 0 de la séquence sera considéré comme étant 0, donc le premier terme sera 1 ; le deuxième, 1 ; le troisième, 2 ; et ainsi de suite. Vous avez compris.

Analysons la fonction un instant. Si elle reçoit 0 comme entrée, elle retourne 0. Si elle reçoit 1, elle retourne 1. Si elle reçoit 2… Eh bien, dans ce cas, elle tombe dans l'instruction else, qui appellera à nouveau la fonction pour les termes 2-1 (1) et 2-2 (0). Cela retournera 1 et 0, et les deux résultats seront additionnés, retournant 1. Parfait.

Maintenant, vous pouvez voir pourquoi les fonctions récursives posent problème dans certains cas. Imaginez que vous vouliez le 100ème terme de la séquence. La fonction s'appellerait elle-même pour le 99ème et le 98ème, qui à leur tour appelleraient la fonction à nouveau pour les 98ème et 97ème, et 97ème et 96ème termes… et ainsi de suite. Ce serait **vraiment** lent.

Mais la bonne nouvelle, c'est que cela fonctionne réellement !

Alors, commençons avec les différents langages. Je ne donnerai pas trop de détails (en fait, aucun détail) pour améliorer votre expérience de lecture. Il n'y a pas grand-chose à détailler de toute façon.

Plongeons-nous dedans :

### Python

[`def F(n):  if n == 0:`](https://unsplash.com?utm_source=medium&utm_medium=referral)  
    [`return 0  if n == 1:`](https://unsplash.com?utm_source=medium&utm_medium=referral)  
    [`return 1  else:`](https://unsplash.com?utm_source=medium&utm_medium=referral)  
    [`return F(n-1) + F(n-2)`](https://unsplash.com?utm_source=medium&utm_medium=referral)

### Swift

[`func F(_ n: Int) -> Int {  if n == 0 {    return 0`](https://unsplash.com?utm_source=medium&utm_medium=referral)  
  [`}  if n == 1 {    return 1`](https://unsplash.com?utm_source=medium&utm_medium=referral)  
  [`}  else {    return F(n-1) + F(n-2)`](https://unsplash.com?utm_source=medium&utm_medium=referral)  
  [`}}`](https://unsplash.com?utm_source=medium&utm_medium=referral)

### JavaScript

[`function F(n) {  if(n == 0) {    return 0;`](https://unsplash.com?utm_source=medium&utm_medium=referral)  
  [`}  if(n == 1) {    return 1;`](https://unsplash.com?utm_source=medium&utm_medium=referral)  
  [`}  else {    return F(n-1) + F(n-2);`](https://unsplash.com?utm_source=medium&utm_medium=referral)  
  [`}}`](https://unsplash.com?utm_source=medium&utm_medium=referral)

### Java

[`public static int F(int n) {  if(n == 0) {    return 0;`](https://unsplash.com?utm_source=medium&utm_medium=referral)  
  [`}  if(n == 1) {    return 1;`](https://unsplash.com?utm_source=medium&utm_medium=referral)  
  [`}  else {    return F(n-1) + F(n-2);`](https://unsplash.com?utm_source=medium&utm_medium=referral)  
  [`}}`](https://unsplash.com?utm_source=medium&utm_medium=referral)

### C++

[`int F(int n) {  if(n == 0) {    return 0;`](https://unsplash.com?utm_source=medium&utm_medium=referral)  
  [`}  if(n == 1) {    return 1;`](https://unsplash.com?utm_source=medium&utm_medium=referral)  
  [`}  else {    return F(n-1) + F(n-2);`](https://unsplash.com?utm_source=medium&utm_medium=referral)  
  [`}}`](https://unsplash.com?utm_source=medium&utm_medium=referral)

Et c'est tout. J'ai choisi ces langages simplement en fonction de leur popularité — ou du moins parce que ces cinq sont les plus courants que j'utilise. Ils ne sont dans aucun ordre particulier. Ils pourraient être classés par difficulté de syntaxe, à mon avis, de Python (le plus facile) à C++ (le plus difficile). Mais cela dépend de votre opinion personnelle et de votre expérience avec chaque langage.

J'espère que vous avez aimé cet article et, si vous avez des questions/recommandations ou si vous voulez simplement dire bonjour, commentez ci-dessous !