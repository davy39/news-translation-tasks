---
title: Tout ce que vous devez savoir sur l'algorithme de tri par insertion
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-07T13:32:38.000Z'
originalURL: https://freecodecamp.org/news/everything-you-need-to-know-about-insertion-sort-algorithm
coverImage: https://www.freecodecamp.org/news/content/images/2019/06/image-44-1.png
tags:
- name: algorithms
  slug: algorithms
- name: Backend Development
  slug: backend-development
- name: coding
  slug: coding
- name: creative coding
  slug: creative-coding
- name: Java
  slug: java
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: Tout ce que vous devez savoir sur l'algorithme de tri par insertion
seo_desc: 'By Sanjula Madurapperuma

  Introduction

  Hi! I am Sanjula, and in this guide I hope to teach you a little bit about the Insertion
  Sort algorithm including:


  What is Insertion sort?

  Why is insertion sort important?

  Performance of Insertion Sort

  How does ...'
---

Par Sanjula Madurapperuma

### **Introduction**

Bonjour ! Je suis [Sanjula](https://www.linkedin.com/in/sanjula-madurapperuma/), et dans ce guide, j'espère vous enseigner un peu sur l'algorithme de tri par insertion, notamment :

* Qu'est-ce que le tri par insertion ?
* Pourquoi le tri par insertion est-il important ?
* Performance du tri par insertion
* Comment fonctionne le tri par insertion ?
* Implémentation Java du tri par insertion

Commençons !

### **Qu'est-ce que le tri par insertion ?**

C'est un algorithme de tri simple qui trie un tableau un élément à la fois.

### **Pourquoi le tri par insertion est-il important ?**

Le tri par insertion présente plusieurs avantages, notamment :

* La simplicité pure de l'algorithme.
* L'ordre relatif des éléments avec des clés égales ne change pas.
* La capacité à trier une liste au fur et à mesure de sa réception.
* Efficace pour les petits ensembles de données, surtout en pratique par rapport à d'autres algorithmes quadratiques — c'est-à-dire O(n²).
* Il ne nécessite qu'une quantité constante d'espace mémoire supplémentaire — O(1).

### **Performance du tri par insertion**

* La performance dans le pire des cas du tri par insertion est O(n²) comparaisons et échanges.
* La performance dans le meilleur des cas est O(n) comparaisons et O(1) échanges.
* La performance moyenne est O(n²) comparaisons et échanges.

### **Comment fonctionne le tri par insertion ?**

À chaque itération, le tri par insertion compare l'élément actuel avec l'élément suivant et détermine si l'élément actuel est plus grand que celui avec lequel il a été comparé.

Si c'est _vrai_, alors il laisse l'élément à sa place et passe à l'élément suivant. Si c'est _faux_, alors il trouve sa position correcte dans le tableau trié et le déplace à cette position en décalant tous les éléments qui sont plus grands dans le tableau trié d'une position vers l'avant.

### **Implémentation Java du tri par insertion**

P.S. — Essayez de l'implémenter vous-même d'abord !

<script src="https://gist.github.com/sanjulamadurapperuma/25677635f216b9fa858d8051140e47f2.js"></script>

---

**Félicitations !!!** Vous avez maintenant acquis les connaissances de base mais essentielles sur le fonctionnement du tri par insertion.

Pour référence ou pour signaler des problèmes concernant le code ci-dessus, utilisez le lien suivant vers le Gist public GitHub [lien](https://gist.github.com/sanjulamadurapperuma/25677635f216b9fa858d8051140e47f2).

---

J'espère que cela a été utile. Merci d'avoir lu ! 😊