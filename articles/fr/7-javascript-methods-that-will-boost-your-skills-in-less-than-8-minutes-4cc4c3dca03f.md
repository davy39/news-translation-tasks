---
title: Ces méthodes JavaScript amélioreront vos compétences en quelques minutes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-06T10:31:40.000Z'
originalURL: https://freecodecamp.org/news/7-javascript-methods-that-will-boost-your-skills-in-less-than-8-minutes-4cc4c3dca03f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*H-25KB7EbSHjv70HXrdl6w.png
tags:
- name: JavaScript
  slug: javascript
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Ces méthodes JavaScript amélioreront vos compétences en quelques minutes
seo_desc: 'By Dler Ari

  Most of the applications we build today require some sort of data collection modification.
  Processing items in a collection is a common operation you will most likely encounter.
  Forget the conventional way of doing for-loop like (let i=0;...'
---

Par Dler Ari

La plupart des applications que nous construisons aujourd'hui nécessitent une certaine forme de modification de collecte de données. Le traitement des éléments d'une collection est une opération courante que vous rencontrerez très probablement. Oubliez la méthode conventionnelle de faire une boucle `for` comme `(let i=0; i < value.length; i++`).

> Petit rappel, utiliser `const` dans une boucle `for` vous donnera une erreur. La raison en est qu'elle redéclare la valeur à chaque exécution, donc `i` est modifié par `i++`. Donc, chaque fois que vous pensez à utiliser `const` ou `let`, demandez-vous — Cette valeur sera-t-elle redéclarée ? Si la réponse est **oui**, utilisez `let`, et si **non**, utilisez `const`. [Plus d'informations](https://stackoverflow.com/questions/41067790/why-does-const-work-in-some-for-loops-in-javascript).

Disons que vous voulez afficher une liste de produits et les catégoriser, filtrer, rechercher, modifier ou mettre à jour une collection. Ou peut-être que vous voulez effectuer des calculs rapides tels que des sommes, des multiplications, et ainsi de suite. Quelle est la manière optimale d'y parvenir ?

Peut-être que vous n'aimez pas les **fonctions fléchées**, vous ne voulez pas passer trop de temps à apprendre quelque chose de nouveau, ou elles ne sont tout simplement pas pertinentes pour vous. Ne vous inquiétez pas, vous n'êtes pas seul. Je vais vous montrer comment cela se fait en ES5 (déclaration fonctionnelle) et en ES6 (fonctions fléchées).

**Attention :** Les fonctions fléchées et les déclarations/expressions de fonctions ne sont pas équivalentes et ne peuvent pas être [remplacées aveuglément](https://stackoverflow.com/questions/34361379/arrow-function-vs-function-declaration-expressions-are-they-equivalent-exch?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa). Gardez à l'esprit que le mot-clé `this` fonctionne différemment entre les deux.

#### Les méthodes que nous allons examiner :

1. Opérateur de décomposition (Spread operator)
2. Itérateur for...of
3. includes()
4. some()
5. every()
6. filter()
7. map()
8. reduce()

> Si vous voulez devenir un meilleur développeur web, créer votre propre entreprise, enseigner aux autres ou améliorer vos compétences en développement, je publierai des conseils et astuces hebdomadaires sur les derniers langages de développement web.

### 1. Opérateur de décomposition (Spread operator)

L'opérateur de décomposition **développe** un tableau en ses éléments. Il peut également être utilisé pour les littéraux d'objets.

**Pourquoi devrais-je l'utiliser ?**

* C'est une manière simple et rapide d'afficher les éléments d'un tableau
* Il fonctionne pour les tableaux et les littéraux d'objets
* C'est une manière rapide et intuitive de passer des arguments
* Il ne nécessite que trois points...

**Exemple :**   
Disons que vous voulez afficher une liste de plats préférés sans créer de fonction de boucle. Utilisez un opérateur de décomposition comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*NPgk0vqyWiXXkNDPMbxujA.png)

### 2. Itérateur for...of

L'instruction `for...of` parcourt/itère à travers la collection et vous offre la possibilité de modifier des éléments spécifiques. Elle remplace la manière conventionnelle de faire une boucle `for`.

**Pourquoi devrais-je l'utiliser ?**

* C'est une manière simple d'ajouter ou de mettre à jour un élément
* Pour effectuer des calculs (somme, multiplication, etc.)
* Lorsque vous utilisez des instructions conditionnelles (if, while, switch, etc.)
* Conduit à un code propre et lisible

**Exemple :**   
Disons que vous avez une boîte à outils et que vous voulez afficher tous les outils à l'intérieur. L'itérateur `for...of` le rend facile.

![Image](https://cdn-media-1.freecodecamp.org/images/1*kjQYvjeeHUuP8inZYqjJVg.png)
_opérateur for...of_

### 3. Méthode includes()

La méthode `includes()` est utilisée pour vérifier si une chaîne spécifique existe dans une collection et retourne `true` ou `false`. Gardez à l'esprit qu'elle est sensible à la casse : si l'élément dans la collection est `SCHOOL` et que vous recherchez `school`, elle retournera `false`.

**Pourquoi devrais-je l'utiliser ?**

* Pour construire une fonctionnalité de recherche simple
* C'est une approche intuitive pour déterminer si une chaîne existe
* Elle utilise des instructions conditionnelles pour modifier, filtrer, etc.
* Conduit à un code lisible

**Exemple :**  
Disons que, pour une raison quelconque, vous n'êtes pas au courant des voitures que vous avez dans votre garage et que vous avez besoin d'un système pour vérifier si la voiture que vous voulez existe ou non. `includes()` à la rescousse !

![Image](https://cdn-media-1.freecodecamp.org/images/1*m1InU7VDxdfpxMXuV2A1MA.png)
_méthode includes() avec fonction fléchée_

### 4. Méthode some()

La méthode `some()` vérifie si certains éléments existent dans un tableau et retourne `true` ou `false`. Cela est quelque peu similaire au concept de la méthode `includes()`, sauf que l'argument est une fonction et non une chaîne.

**Pourquoi devrais-je l'utiliser ?**

* Elle s'assure que **certains** éléments passent le test
* Elle effectue des instructions conditionnelles en utilisant des fonctions
* Rendez votre code déclaratif
* Some est suffisamment bon

**Exemple :**   
Disons que vous êtes propriétaire d'un club et que vous ne vous souciez pas de qui entre dans le club. Mais certains ne sont pas autorisés à entrer, parce qu'ils ont trop bu (ma créativité à son meilleur). Découvrez les différences entre ES5 et ES6 ci-dessous :

#### ES5 :

![Image](https://cdn-media-1.freecodecamp.org/images/1*-5YnlNy48wi0FHnIG3bXDg.png)
_méthode some()_

#### ES6 :

![Image](https://cdn-media-1.freecodecamp.org/images/1*pmaXrKpg5vI__WwztfATGg.png)
_méthode some() avec fonction fléchée_

### 5. Méthode every()

La méthode `every()` parcourt le tableau, vérifie chaque élément et retourne `true` ou `false`. Même concept que `some()`. Sauf que chaque élément doit satisfaire l'instruction conditionnelle, sinon, elle retournera `false`.

**Pourquoi devrais-je l'utiliser ?**

* Elle s'assure que **chaque** élément passe le test
* Vous pouvez effectuer des instructions conditionnelles en utilisant des fonctions
* Rendez votre code déclaratif

**Exemple :**   
La dernière fois, vous avez permis à `some()` d'étudiants mineurs d'entrer dans le club, quelqu'un a signalé cela et la police vous a attrapé. Cette fois, vous ne laisserez pas cela arriver et vous vous assurerez que **tout le monde** passe la limite d'âge avec l'opérateur `every()`.

#### ES5

![Image](https://cdn-media-1.freecodecamp.org/images/1*DNQqzRJ_K01ognj3_c8HqQ.png)
_méthode every()_

#### ES6

![Image](https://cdn-media-1.freecodecamp.org/images/1*avukLSBlIG1ycSzoHLMOYA.png)
_méthode every() avec fonction fléchée_

### 6. Méthode filter()

La méthode `filter()` crée un nouveau tableau avec tous les éléments qui passent le test.

**Pourquoi devrais-je l'utiliser ?**

* Pour éviter de modifier le tableau principal
* Elle vous permet de filtrer les éléments dont vous n'avez pas besoin
* Vous offre un code plus lisible

**Exemple :**   
Disons que vous voulez retourner uniquement les prix qui sont supérieurs ou égaux à 30. Filtrez tous ces autres prix...

#### ES5

![Image](https://cdn-media-1.freecodecamp.org/images/1*O9EhGZRxC1DWan0822fKvQ.png)
_méthode filter()_

#### ES6

![Image](https://cdn-media-1.freecodecamp.org/images/1*1C22z5zvw_Gw_SiJnLuTig.png)
_méthode filter() avec fonction fléchée_

### 7. Méthode map()

La méthode `map()` est similaire à la méthode `filter()` en termes de retour d'un nouveau tableau. Cependant, la seule différence est qu'elle est utilisée pour modifier les éléments.

**Pourquoi devrais-je l'utiliser ?**

* Elle vous permet d'éviter de faire des changements au tableau principal
* Vous pouvez modifier les éléments que vous voulez
* Vous offre un code plus lisible

**Exemple :**   
Disons que vous avez une liste de produits avec des prix. Votre manager a besoin d'une liste pour montrer les nouveaux prix après qu'ils aient été taxés de 25%. La méthode `map()` peut vous aider.

#### ES5

![Image](https://cdn-media-1.freecodecamp.org/images/1*iIOcN4rc6r-55YWrHQVNHw.png)
_méthode map()_

#### ES6

![Image](https://cdn-media-1.freecodecamp.org/images/1*s2ePAwDuw-qJOju7WAm9Uw.png)
_méthode map() avec fonction fléchée_

### 8. Méthode reduce()

La méthode `reduce()` peut être utilisée pour transformer un tableau en autre chose, qui pourrait être un entier, un objet, une chaîne de promesses (exécution séquentielle de promesses), etc. Pour des raisons pratiques, un cas d'utilisation simple serait de faire la somme d'une liste d'entiers. En bref, elle « réduit » tout le tableau en une seule valeur.

**Pourquoi devrais-je l'utiliser ?**

* Effectuer des calculs
* Calculer une valeur
* Compter les doublons
* Grouper les objets par propriété
* Exécuter des promesses de manière séquentielle
* C'est une manière rapide d'effectuer des calculs

**Exemple :**   
Disons que vous voulez connaître vos dépenses totales pour une semaine. Utilisez `reduce()` pour obtenir cette valeur.

#### ES5

![Image](https://cdn-media-1.freecodecamp.org/images/1*OX1oPjVVoPXfIsAqHD3TTQ.png)
_méthode reduce()_

#### ES6

![Image](https://cdn-media-1.freecodecamp.org/images/1*DGa7HZwy40o71B4_ICP6kQ.png)
_méthode reduce() avec fonction fléchée_

Vous pouvez me trouver sur Developer News où je publie chaque semaine. Ou vous pouvez me suivre sur [Twitter](http://twitter.com/dleroari), où je poste des conseils et astuces pertinents sur le développement web.