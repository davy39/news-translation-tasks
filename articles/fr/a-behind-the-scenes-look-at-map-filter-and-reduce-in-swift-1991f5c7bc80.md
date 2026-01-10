---
title: Un regard derrière les coulisses de Map, Filter et Reduce en Swift
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-05T23:35:14.000Z'
originalURL: https://freecodecamp.org/news/a-behind-the-scenes-look-at-map-filter-and-reduce-in-swift-1991f5c7bc80
coverImage: https://cdn-media-1.freecodecamp.org/images/1*nRIbaovXFpRyPpFeHBTFLA.png
tags:
- name: Functional Programming
  slug: functional-programming
- name: iOS
  slug: ios
- name: General Programming
  slug: programming
- name: Swift
  slug: swift
- name: technology
  slug: technology
seo_title: Un regard derrière les coulisses de Map, Filter et Reduce en Swift
seo_desc: 'By Boudhayan Biswas

  A function takes some input, does something to it and creates an output. A function
  has a signature and a body. If you give the same input to a function then you always
  get the same output. That is in short a definition for the fu...'
---

Par Boudhayan Biswas

Une fonction prend une entrée, fait quelque chose avec et crée une sortie. Une fonction a une signature et un corps. Si vous donnez la même entrée à une fonction, vous obtenez toujours la même sortie. C'est en bref une définition de la **_fonction_**.

Maintenant, nous allons parler davantage des fonctions en les examinant de plus près. Nous allons explorer les fonctions d'ordre supérieur en Swift. Une fonction qui prend une autre fonction en entrée ou retourne une fonction est appelée une fonction d'ordre supérieur.

En Swift, nous utilisons **map, filter, reduce** tous les jours. Lorsque nous utilisons ces fonctions, cela semble magique. À ce stade, vous n'avez peut-être pas une idée de ce qui se passe derrière les coulisses. Map, Filter et Reduce fonctionnent à travers les idées et les approches de la programmation fonctionnelle. Même si Swift n'est pas un langage fonctionnel pur, il vous permet de faire des choses fonctionnelles.

Maintenant, examinons un par un ce qui se passe en arrière-plan pour eux. D'abord, nous allons implémenter les versions de base de ces fonctions pour certains types de données particuliers, puis nous essaierons d'implémenter une version générique.

#### Fonction Map

Supposons que nous avons un tableau d'entiers et que nous devons écrire une fonction qui retourne un nouveau tableau après avoir ajouté une certaine valeur delta à chaque élément du tableau original. Nous pouvons facilement écrire une fonction pour cela en utilisant une simple boucle for comme ci-dessous :

Maintenant, nous avons besoin d'une autre fonction qui retourne un nouveau tableau en doublant chaque élément du tableau original. Pour cela, nous pouvons l'implémenter comme ci-dessous :

Si nous regardons les deux fonctions ci-dessus, nous pouvons constater qu'elles font essentiellement la même chose. Seule la fonctionnalité à l'intérieur de la boucle for est différente. Elles prennent toutes deux un tableau d'_Integer_ en entrée, transforment chaque élément en utilisant une boucle for et retournent un nouveau tableau. Donc, essentiellement, la chose principale est de transformer chaque élément en quelque chose de nouveau.

Puisque Swift supporte les fonctions d'ordre supérieur, nous pouvons écrire une fonction qui prendra un tableau d'entiers, transformera la fonction en entrée et retournera un nouveau tableau en appliquant la fonction de transformation à chaque élément du tableau original.

Mais il y a encore un problème avec ce qui précède : il ne retourne qu'un tableau d'entiers. Si nous avons besoin de convertir le tableau d'entiers en entrée en un tableau de chaînes, par exemple, alors nous ne pouvons pas faire cela avec cette fonction. Pour cela, nous devons écrire une fonction générique qui fonctionne pour n'importe quel type.

Nous pouvons implémenter une fonction générique dans une extension de Array comme ceci :

1. Déclarer une fonction map dans l'extension Array qui fonctionne avec un type générique **T**.
2. La fonction prend une fonction de type **(Element) -> T** en entrée
3. Déclarer un tableau de résultats vide qui contient les données de type **T** à l'intérieur de la fonction.
4. Implémenter une boucle for qui itère et appelle la fonction de transformation pour convertir l'élément en type **T**
5. Ajouter la valeur convertie dans le tableau résultant

C'est ainsi que la fonction **map** fonctionne en Swift. Si nous devons implémenter la fonction **map**, alors nous l'implémenterions comme ci-dessus. Donc, essentiellement, elle ne fait pas de magie dans un tableau — nous aurions facilement pu définir la fonction nous-mêmes.

#### Fonction Filter

Supposons que nous avons un tableau d'entiers et que nous voulons garder uniquement les nombres pairs dans le tableau. Nous pouvons implémenter cela en utilisant une simple boucle for :

Maintenant, supposons que nous avons un tableau de chaînes représentant les noms de fichiers de classe d'un projet et que nous voulons garder uniquement les fichiers **_.swift**_. Cela peut également être fait avec une seule boucle comme ci-dessous :

Si nous regardons de près l'implémentation des deux fonctions ci-dessus, alors nous pouvons comprendre qu'elles font essentiellement la même chose — seul le type de données est différent pour les deux tableaux. Nous pouvons généraliser cela en implémentant une fonction de filtre générique, qui prend un tableau et une fonction en entrée, et en fonction de la sortie de la fonction **includeElement**, elle décide si elle ajoute l'élément dans le tableau résultant.

#### Fonction Reduce

Supposons que nous avons un tableau d'entiers et que nous voulons implémenter deux fonctions qui retournent la somme et le produit des éléments. Nous pouvons implémenter cela en utilisant une simple boucle for :

Maintenant, au lieu d'avoir un tableau d'entiers, supposons que nous avons un tableau de chaînes et que nous voulons concaténer tous les éléments du tableau :

Les trois fonctions font essentiellement la même chose. Elles prennent un tableau en entrée, initialisent une variable résultante, itèrent sur le tableau et mettent à jour la variable résultante.

À partir de là, nous pouvons implémenter une fonction générique qui devrait fonctionner pour tous. Pour cela, nous avons besoin de la valeur initiale de la variable résultante et de la fonction pour mettre à jour cette variable à chaque itération.

Nous pouvons donc implémenter la fonction générique avec la définition suivante :

L'implémentation ci-dessus est générique pour tout tableau d'entrée de type **[Element]**. Elle calculera un résultat de type **T**. Pour fonctionner, elle a besoin d'une valeur initiale de type **T** à attribuer à une variable résultante. Ensuite, elle a besoin d'une fonction de type **(T, Element) -> T** qui sera utilisée à l'intérieur de la boucle for à chaque itération pour mettre à jour la variable résultante.

#### Merci d'avoir lu !