---
title: Une introduction rapide au développement piloté par les tests avec Jest
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-25T21:18:39.000Z'
originalURL: https://freecodecamp.org/news/a-quick-introduction-to-test-driven-development-with-jest-cac71cb94e50
coverImage: https://cdn-media-1.freecodecamp.org/images/1*0jCUKud4CkbbmNrFDzIQZw.png
tags:
- name: JavaScript
  slug: javascript
- name: Jest
  slug: jest
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: test driven development
  slug: test-driven-development
seo_title: Une introduction rapide au développement piloté par les tests avec Jest
seo_desc: 'By Nicolas Mitchell

  This article is a simple walkthrough of how to apply Test Driven Development (TDD)
  principles to a JavaScript exercise using Jest.

  Intro

  After a few years of experience developing on my own personal projects, I recently
  decided to...'
---

Par Nicolas Mitchell

Cet article est un guide simple sur la manière d'appliquer les principes du développement piloté par les tests (TDD) à un exercice JavaScript en utilisant Jest.

### Introduction

Après quelques années d'expérience dans le développement de mes propres projets personnels, j'ai récemment décidé de devenir développeur Full-Stack.

Cette nouvelle situation m'a encouragé à commencer à réfléchir à des pratiques que j'ai négligées jusqu'à présent, comme le test de mon code.

C'est pourquoi j'ai voulu commencer mon voyage à travers le développement piloté par les tests. J'ai décidé de partager mes premiers pas ici avec vous.

### L'exercice

J'ai décidé de commencer avec le premier kata TDD d'Osherove. Vous pouvez accéder à l'exercice complet [ici](http://osherove.com/tdd-kata-1/).

Le but est de fournir une fonction qui prend une entrée de chaîne (`"1, 2, 3"` par exemple) et retourne la somme de tous les nombres.

Notre projet aura la structure suivante :

```
js-kata-jest/
```

```
├─ src/
```

```
  └─ kata.js
```

```
├─ test/
```

```
  └─ kata.test.js
```

```
└─ package.json
```

### Configuration de l'environnement de test

Tout d'abord, nous devons configurer l'environnement de test. En tant que développeur React, j'ai décidé d'utiliser [Jest](https://facebook.github.io/jest/). Vous pouvez utiliser toute autre bibliothèque de test de votre choix.

#### Installation de la dépendance de développement Jest

```
yarn add --dev jest
```

ou avec [npm](https://www.npmjs.com/) :

```
npm install --save-dev jest
```

#### Activation de Jest sur votre éditeur de code

J'utilise Atom comme éditeur de code et j'ai installé le package [tester-jest](https://atom.io/packages/tester-jest). Cela m'a permis d'exécuter mes tests à chaque sauvegarde pour tout fichier `*.test.js`.

### Développement piloté par les tests

La théorie derrière le TDD est assez simple et repose sur 3 étapes :

1. Écrire un test pour une petite partie d'une fonctionnalité et vérifier que ce nouveau test échoue (Étape Rouge)
2. Écrire le code qui fait passer le test, puis vérifier que votre test précédent et le nouveau sont réussis (Étape Verte)
3. Refactoriser le code pour s'assurer qu'il est clair, compréhensible et se comporte bien avec les fonctionnalités précédentes

Dans la partie suivante, nous allons entrer dans le détail de chacune de ces étapes.

### Résolution de l'exercice

#### Première boucle

Tout d'abord, nous voulons gérer le cas où notre fonction `add` reçoit une chaîne vide ou une chaîne avec un seul élément.

1. **Écrire les tests**

* Le premier test vérifie qu'une chaîne vide retourne 0
* Le second vérifie qu'une chaîne avec un seul élément retourne l'élément fourni

**2. Écrire le code**

* Tout d'abord, nous retournons 0 par défaut
* Ensuite, nous fournissons une instruction `if` qui gère l'analyse d'un seul élément fourni

Voici le code final :

**3. Refactoriser le code**

Comme il s'agit de notre première fonctionnalité, nous pouvons sauter cette étape pour l'instant — mais nous y reviendrons bientôt. ;)

#### Deuxième boucle

Nous allons maintenant gérer le cas où la chaîne contient plusieurs éléments :

1. **Écrire les tests**

Le nouveau test s'assure que le calcul d'une chaîne à plusieurs éléments est effectué correctement :

**2. Écrire le code**

* Tout d'abord, nous créons une nouvelle instruction `if` exprès pour être sûr que nos deux premiers tests affectent la nouvelle solution
* Ensuite, nous créons un nouveau tableau à partir de la chaîne d'entrée, en utilisant la `,` comme séparateur
* Enfin, nous analysons chaque élément du nouveau tableau pour calculer la somme

Voici le code final :

**3. Refactoriser le code**

Comme nous pouvons le voir ci-dessus, il y a plusieurs problèmes dans notre code :

* les deux instructions `if` ne devraient pas être décorrelées, car ajouter un ou plusieurs à zéro devrait se comporter de la même manière.
* la valeur du séparateur est noyée dans le code. Cela ajoute de la complexité si nous voulons changer pour un séparateur `;` par exemple.
* une grande partie de notre code est située dans une instruction `if`. Nous pourrions inverser la logique pour extraire notre code principal de celle-ci.

Nous pouvons donc ajouter une nouvelle variable `separator`, qui décidera du type de séparateur. Nous pouvons également fusionner les deux instructions `if` en une seule, puis inverser la logique.

Nous pouvons maintenant relancer notre test avant de passer à la boucle suivante.

#### Troisième boucle

Nous pouvons maintenant gérer la déclaration de nouveaux séparateurs et éviter l'entrée de nombres négatifs.

1. **Écrire les tests**

* Le premier nouveau test se concentre sur un seul séparateur parmi les valeurs par défaut.
* Le second s'assurera que nous pouvons configurer un nouveau séparateur directement dans l'entrée.
* Le troisième vérifiera qu'une erreur est lancée lorsqu'une valeur négative est passée en entrée.

**2. Écrire le code**

* Tout d'abord, nous remplaçons la chaîne `separator` par un tableau `separators`, où nous ajoutons la valeur `\n`.
* Ensuite, nous introduisons une nouvelle recherche de séparateur via une expression régulière. Celle-ci sera ajoutée au tableau précédent.
* Nous pouvons maintenant joindre les éléments du tableau précédent pour diviser la chaîne avec eux.
* Nous filtrons le tableau résultant pour supprimer tous les éléments non numériques.
* Nous ajoutons un nouveau tableau, `negatives`, qui repérera les valeurs négatives dans l'entrée.
* Si le tableau `negatives` n'est pas vide, lancer une erreur.

Voici le code final :

**3. Refactoriser le code**

Nous avons maintenant deux nouvelles optimisations possibles :

* Nous utilisons l'expression régulière deux fois et souhaitons la changer facilement. Nous pouvons l'extraire dans une nouvelle `const regexp`.
* Nous calculons `parseInt(list[i])` plusieurs fois, nous devrions donc stocker la valeur une seule fois pour accélérer la boucle `for`.

### Conclusion

Nous pouvons maintenant relancer nos tests pour nous assurer que toutes nos fonctionnalités attendues fonctionnent toujours.

Vous pouvez maintenant continuer par vous-même. Consultez la version définitive du kata avec tous les tests réussis [ici](https://github.com/nclsmitchell/js-kata-jest).

N'hésitez pas à me contacter sur Twitter si vous avez des questions ou des commentaires [@nclsmitchell](https://twitter.com/nclsmitchell) ou via Medium :)

Merci pour votre lecture, et n'hésitez pas à applaudir si vous aimez cet article.