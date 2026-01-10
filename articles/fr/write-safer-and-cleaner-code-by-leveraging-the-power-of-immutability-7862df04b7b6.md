---
title: Écrivez un code plus sûr et plus propre en exploitant le pouvoir de l'« Immuabilité
  »
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-05-17T17:51:34.000Z'
originalURL: https://freecodecamp.org/news/write-safer-and-cleaner-code-by-leveraging-the-power-of-immutability-7862df04b7b6
coverImage: https://cdn-media-1.freecodecamp.org/images/1*eO8-0-GT5ht8CR7TdK9knA.jpeg
tags:
- name: Computer Science
  slug: computer-science
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Écrivez un code plus sûr et plus propre en exploitant le pouvoir de l'«
  Immuabilité »
seo_desc: 'By Guido Schmitz

  Immutability is one of the building blocks of functional programming. It allows
  you to write safer and cleaner code. I’ll show you how you can achieve immutability
  through some JavaScript examples.

  According to Wikipedia (source):


  A...'
---

Par Guido Schmitz

L'immuabilité est l'un des piliers de la programmation fonctionnelle. Elle permet d'écrire un code plus sûr et plus propre. Je vais vous montrer comment atteindre l'immuabilité à travers quelques exemples en JavaScript.

**Selon Wikipedia ([source](https://en.wikipedia.org/wiki/Immutable_object)) :**

> Un objet immuable (objet non modifiable) est un objet dont l'état ne peut pas être modifié après sa création. Cela contraste avec un objet mutable (objet modifiable), qui peut être modifié après sa création. Dans certains cas, un objet est considéré comme immuable même si certains attributs utilisés en interne changent, mais l'état de l'objet semble inchangé depuis un point de vue externe.

### Tableaux immuables

Les tableaux sont un bon point de départ pour comprendre comment fonctionne réellement l'immuabilité. Examinons cela.

```
const arrayA = [1, 2, 3];arrayA.push(4); const arrayB = arrayA;arrayB.push(5); console.log(arrayA); // [1, 2, 3, 4, 5]console.log(arrayB); // [1, 2, 3, 4, 5]
```

Cet exemple assigne **arrayB** à une référence de **arrayA**, donc la méthode push ajoute la valeur 5 dans les deux variables. Notre code mute indirectement d'autres valeurs, ce qui n'est pas ce que nous voulons faire. Cela viole le principe d'immuabilité.

Nous pouvons améliorer notre exemple pour qu'il soit immuable en utilisant la fonction [slice](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/slice), et le comportement du code est différent.

```
const arrayA = [1, 2, 3];arrayA.push(4); const arrayB = arrayA.slice(0);arrayB.push(5); console.log(arrayA); // [1, 2, 3, 4]console.log(arrayB); // [1, 2, 3, 4, 5]
```

C'est exactement ce que nous voulons. Le code ne mute pas les autres valeurs.

Rappel : Lorsque vous utilisez [push](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/push) pour ajouter une valeur à un tableau, vous **mutez** le tableau. Vous devez éviter de muter les variables car cela peut causer des effets secondaires dans votre code. La fonction [slice](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/slice) retourne une copie du tableau.

### Fonctions

Maintenant que vous savez comment éviter de muter d'autres valeurs, comment écrire des fonctions pour qu'elles soient « pures » ? Pure est un autre terme pour désigner une fonction qui n'a aucun effet secondaire et ne changera pas d'état.

Examinons une fonction qui utilise le même principe que l'exemple des tableaux. D'abord, nous créons une fonction qui mute une autre valeur, puis nous améliorons la fonction pour qu'elle soit « pure ».

```
const add = (arrayInput, value) => {  arrayInput.push(value);   return arrayInput;};
```

```
const array = [1, 2, 3]; console.log(add(array, 4)); // [1, 2, 3, 4]console.log(add(array, 5)); // [1, 2, 3, 4, 5]
```

Ainsi, nous **mutons** à nouveau notre entrée, ce qui crée une fonction imprévisible. Dans le monde de la programmation fonctionnelle, il existe une règle d'or concernant les fonctions : **une fonction avec la même entrée doit toujours retourner le même résultat**.

La fonction ci-dessus viole la règle d'or. Chaque fois que notre fonction **add** est appelée, elle mute la variable **array** et le résultat est différent.

Voyons comment nous pouvons changer l'implémentation de notre fonction **add** pour qu'elle soit immuable.

```
const add = (arrayInput, value) => {  const copiedArray = arrayInput.slice(0);  copiedArray.push(value);   return copiedArray;}; const array = [1, 2, 3];
```

```
const resultA = add(array, 4);console.log(resultA); // [1, 2, 3, 4]
```

```
const resultB = add(array, 5);console.log(resultB); // [1, 2, 3, 5]
```

Maintenant, nous pouvons appeler notre fonction plusieurs fois et nous attendre à ce que la sortie soit la même, en fonction de l'entrée. Cela est dû au fait que nous ne mutons plus la variable **array**. Nous pouvons appeler cette fonction une « fonction pure ».

> **Note :** Vous pouvez également utiliser **concat**, au lieu de **slice** et **push**.  
> Donc : arrayInput.concat(value);

Nous pouvons utiliser la [syntaxe de décomposition](https://developer.mozilla.org/nl/docs/Web/JavaScript/Reference/Operators/Spread_operator), disponible en ES6, pour raccourcir cette fonction.

```
const add = (arrayInput, value) => [...arrayInput, value];
```

### Concurrence

Les applications NodeJS utilisent un concept appelé concurrence. Une opération concurrente signifie que deux calculs peuvent tous deux progresser indépendamment l'un de l'autre. S'il y a deux threads, le second calcul n'a pas besoin d'attendre la fin du premier pour avancer.

![Image](https://cdn-media-1.freecodecamp.org/images/ajQNacOo6-0-aOa4K4a5wH-1SoCEfKAEftij)
_Visualisation d'une opération concurrente_

NodeJS rend la concurrence possible avec la boucle d'événements. La boucle d'événements prend répétitivement un événement et déclenche les gestionnaires d'événements écoutant cet événement un par un. Ce modèle permet à une application NodeJS de traiter un grand nombre de requêtes. Si vous souhaitez en savoir plus, lisez [cet article sur la boucle d'événements](https://nodejs.org/en/docs/guides/event-loop-timers-and-nexttick).

Quel est le rapport entre l'immuabilité et la concurrence ? Puisque plusieurs opérations peuvent modifier une valeur en dehors de la portée de la fonction de manière concurrente, cela crée des sorties peu fiables et provoque des résultats inattendus. Méfiez-vous d'une fonction qui mute des variables en dehors de sa portée, car cela peut être vraiment dangereux.

### Prochaines étapes

L'immuabilité est un concept important à comprendre sur votre chemin pour apprendre la programmation fonctionnelle. Vous pourriez vouloir jeter un coup d'œil à [ImmutableJS](https://facebook.github.io/immutable-js), écrit par des développeurs chez Facebook. La bibliothèque fournit certaines structures de données immuables comme **Map**, **Set**, et **List**.

[**Immutable.js, persistent data structures and structural sharing**](https://medium.com/@dtinth/immutable-js-persistent-data-structures-and-structural-sharing-6d163fbd73d2)  
[_Why use Immutable.js instead of normal JavaScript object?_medium.com](https://medium.com/@dtinth/immutable-js-persistent-data-structures-and-structural-sharing-6d163fbd73d2)[**Higher Order Functions: Using Filter, Map and Reduce for More Maintainable Code**](https://medium.freecodecamp.org/higher-order-functions-in-javascript-d9101f9cf528)  
[_Higher order functions can help you to step up your JavaScript game by making your code more declarative. That is…_medium.freecodecamp.org](https://medium.freecodecamp.org/higher-order-functions-in-javascript-d9101f9cf528)

_Cliquez sur le ? ci-dessous pour que d'autres personnes voient cet article ici sur Medium. Merci pour votre lecture._

![Image](https://cdn-media-1.freecodecamp.org/images/0pF5DeetY83EjRZztJ7vbRQek2p9bcgiWnrV)