---
title: Algorithmes de Force Brute Expliqués
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-06T18:38:00.000Z'
originalURL: https://freecodecamp.org/news/brute-force-algorithms-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e20740569d1a4ca3b74.jpg
tags:
- name: algorithms
  slug: algorithms
- name: toothbrush
  slug: toothbrush
seo_title: Algorithmes de Force Brute Expliqués
seo_desc: 'Brute Force Algorithms are exactly what they sound like – straightforward
  methods of solving a problem that rely on sheer computing power and trying every
  possibility rather than advanced techniques to improve efficiency.

  For example, imagine you hav...'
---

Les algorithmes de force brute sont exactement ce à quoi ils ressemblent – des méthodes simples de résolution d'un problème qui reposent sur la puissance de calcul brute et qui essaient toutes les possibilités plutôt que des techniques avancées pour améliorer l'efficacité.

Par exemple, imaginez que vous avez un petit cadenas à 4 chiffres, chacun allant de 0 à 9. Vous avez oublié votre combinaison, mais vous ne voulez pas acheter un autre cadenas. Puisque vous ne vous souvenez d'aucun des chiffres, vous devez utiliser une méthode de force brute pour ouvrir le cadenas.

Vous remettez donc tous les chiffres à 0 et vous les essayez un par un : 0001, 0002, 0003, et ainsi de suite jusqu'à ce qu'il s'ouvre. Dans le pire des cas, il faudrait 10<sup>4</sup>, soit 10 000 essais pour trouver votre combinaison.

Un exemple classique en informatique est le problème du voyageur de commerce (TSP). Supposons qu'un représentant doive visiter 10 villes à travers le pays. Comment déterminer l'ordre dans lequel ces villes doivent être visitées de sorte que la distance totale parcourue soit minimisée ?

La solution de force brute consiste simplement à calculer la distance totale pour chaque itinéraire possible, puis à sélectionner le plus court. Cela n'est pas particulièrement efficace car il est possible d'éliminer de nombreux itinéraires possibles grâce à des algorithmes astucieux.

La complexité temporelle de la force brute est **O(m**n**)**, ce qui est parfois écrit comme **O(n*m)**. Donc, si nous devions rechercher une chaîne de "n" caractères dans une chaîne de "m" caractères en utilisant la force brute, cela nous prendrait n * m essais.

## Plus d'informations sur les algorithmes

En informatique, un algorithme est simplement un ensemble de procédures étape par étape pour résoudre un problème donné. Les algorithmes peuvent être conçus pour effectuer des calculs, traiter des données ou effectuer des tâches de raisonnement automatisé.

Voici comment le dictionnaire définit les [algorithmes](https://www.merriam-webster.com/dictionary/algorithm) en termes simples :

> une procédure étape par étape pour résoudre un problème ou accomplir une tâche.

Il existe certaines exigences qu'un algorithme doit respecter :

1. Définition : Chaque étape du processus est précisément énoncée.
2. Calculabilité effective : Chaque étape du processus peut être exécutée par un ordinateur.
3. Finitude : Le programme se terminera éventuellement avec succès.

Certains types courants d'algorithmes incluent :

* algorithmes de tri
* algorithmes de recherche
* algorithmes de compression.

Les classes d'algorithmes incluent :

* Graphes
* Programmation dynamique
* Tri
* Recherche
* Chaînes de caractères
* Mathématiques
* Géométrie computationnelle
* Optimisation
* Divers.

Bien que techniquement pas une classe d'algorithmes, les structures de données sont souvent regroupées avec eux.

### **Efficacité**

Les algorithmes sont le plus souvent jugés par leur efficacité et la quantité de ressources informatiques qu'ils nécessitent pour accomplir leur tâche.

Un moyen courant d'évaluer un algorithme est de regarder sa complexité temporelle. Cela montre comment le temps d'exécution de l'algorithme augmente à mesure que la taille de l'entrée augmente. Puisque les algorithmes d'aujourd'hui doivent fonctionner sur de grandes entrées de données, il est essentiel que nos algorithmes aient un temps d'exécution raisonnablement rapide.

### **Algorithmes de Tri**

Les algorithmes de tri existent en diverses variantes selon vos besoins. Certains, très courants et largement utilisés sont :

#### **Quicksort**

Il n'y a pas de discussion sur le tri qui puisse se terminer sans mentionner le tri rapide. Voici le concept de base : [Quick Sort](http://me.dt.in.th/page/Quicksort/)

#### **Mergesort**

Un algorithme de tri qui repose sur le concept de fusion de tableaux triés pour obtenir un seul tableau trié. En savoir plus ici : [Mergesort](https://www.geeksforgeeks.org/merge-sort/)

Le programme de freeCodeCamp met fortement l'accent sur la création d'algorithmes. Cela est dû au fait que l'apprentissage des algorithmes est un bon moyen de pratiquer les compétences en programmation. Les recruteurs testent le plus souvent les candidats sur les algorithmes lors des entretiens d'embauche pour les développeurs.

## Livres sur les algorithmes en JavaScript :

_Structures de Données en JavaScript_

* Livre gratuit qui couvre les structures de données en JavaScript
* [GitBook](https://www.gitbook.com/book/pmary/data-structure-in-javascript/details)

_Apprendre les Structures de Données et les Algorithmes en JavaScript - Deuxième Édition_

* Couvre la programmation orientée objet, l'héritage prototypal, les algorithmes de tri et de recherche, quicksort, mergesort, les arbres binaires de recherche et les concepts avancés d'algorithmes
* [Amazon](https://www.amazon.com/Learning-JavaScript-Data-Structures-Algorithms/dp/1785285491)
* ISBN-13 : 978-1785285493

_Structures de Données et Algorithmes avec JavaScript : Appliquer les approches classiques de l'informatique au Web_

* Couvre la récursivité, les algorithmes de tri et de recherche, les listes chaînées et les arbres binaires de recherche.
* [Amazon](https://www.amazon.com/Data-Structures-Algorithms-JavaScript-approaches/dp/1449364934)
* ISBN-13 : 978-1449364939